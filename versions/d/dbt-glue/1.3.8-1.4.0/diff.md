# Comparing `tmp/dbt-glue-1.3.8.tar.gz` & `tmp/dbt-glue-1.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dbt-glue-1.3.8.tar", last modified: Thu Dec 29 17:25:29 2022, max compression
+gzip compressed data, was "dbt-glue-1.4.0.tar", last modified: Fri Apr  7 08:31:34 2023, max compression
```

## Comparing `dbt-glue-1.3.8.tar` & `dbt-glue-1.4.0.tar`

### file list

```diff
@@ -1,50 +1,48 @@
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.237782 dbt-glue-1.3.8/
--rw-r--r--   0 menuetb    (504) staff       (20)    10142 2022-04-05 16:42:41.000000 dbt-glue-1.3.8/LICENSE
--rw-r--r--   0 menuetb    (504) staff       (20)       67 2022-04-05 16:42:41.000000 dbt-glue-1.3.8/NOTICE
--rw-r--r--   0 menuetb    (504) staff       (20)    37177 2022-12-29 17:25:29.237007 dbt-glue-1.3.8/PKG-INFO
--rw-r--r--   0 menuetb    (504) staff       (20)    36327 2022-11-24 09:31:50.000000 dbt-glue-1.3.8/README.md
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.192588 dbt-glue-1.3.8/dbt/
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.191936 dbt-glue-1.3.8/dbt/adapters/
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.207186 dbt-glue-1.3.8/dbt/adapters/glue/
--rw-r--r--   0 menuetb    (504) staff       (20)      394 2022-07-11 06:48:28.000000 dbt-glue-1.3.8/dbt/adapters/glue/__init__.py
--rw-r--r--   0 menuetb    (504) staff       (20)       17 2022-12-29 17:25:21.000000 dbt-glue-1.3.8/dbt/adapters/glue/__version__.py
--rw-r--r--   0 menuetb    (504) staff       (20)     3442 2022-07-11 06:48:28.000000 dbt-glue-1.3.8/dbt/adapters/glue/connections.py
--rw-r--r--   0 menuetb    (504) staff       (20)     2474 2022-11-24 09:26:04.000000 dbt-glue-1.3.8/dbt/adapters/glue/credentials.py
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.212898 dbt-glue-1.3.8/dbt/adapters/glue/gluedbapi/
--rw-r--r--   0 menuetb    (504) staff       (20)      140 2022-04-05 16:42:41.000000 dbt-glue-1.3.8/dbt/adapters/glue/gluedbapi/__init__.py
--rw-r--r--   0 menuetb    (504) staff       (20)     1216 2022-07-11 06:48:28.000000 dbt-glue-1.3.8/dbt/adapters/glue/gluedbapi/commons.py
--rw-r--r--   0 menuetb    (504) staff       (20)     8771 2022-12-08 07:32:35.000000 dbt-glue-1.3.8/dbt/adapters/glue/gluedbapi/connection.py
--rw-r--r--   0 menuetb    (504) staff       (20)     8232 2022-10-12 06:58:28.000000 dbt-glue-1.3.8/dbt/adapters/glue/gluedbapi/cursor.py
--rw-r--r--   0 menuetb    (504) staff       (20)    26105 2022-11-24 09:41:29.000000 dbt-glue-1.3.8/dbt/adapters/glue/impl.py
--rw-r--r--   0 menuetb    (504) staff       (20)     1220 2022-04-05 16:42:41.000000 dbt-glue-1.3.8/dbt/adapters/glue/relation.py
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.192890 dbt-glue-1.3.8/dbt/include/
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.216497 dbt-glue-1.3.8/dbt/include/glue/
--rw-r--r--   0 menuetb    (504) staff       (20)       51 2022-04-05 16:42:41.000000 dbt-glue-1.3.8/dbt/include/glue/__init__.py
--rw-r--r--   0 menuetb    (504) staff       (20)       72 2022-07-11 06:48:28.000000 dbt-glue-1.3.8/dbt/include/glue/dbt_project.yml
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.217888 dbt-glue-1.3.8/dbt/include/glue/macros/
--rw-r--r--   0 menuetb    (504) staff       (20)     5844 2022-11-25 08:59:23.000000 dbt-glue-1.3.8/dbt/include/glue/macros/adapters.sql
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.220707 dbt-glue-1.3.8/dbt/include/glue/macros/generic_test_sql/
--rw-r--r--   0 menuetb    (504) staff       (20)      494 2022-07-11 06:48:28.000000 dbt-glue-1.3.8/dbt/include/glue/macros/generic_test_sql/accepted_values.sql
--rw-r--r--   0 menuetb    (504) staff       (20)      370 2022-07-11 06:48:28.000000 dbt-glue-1.3.8/dbt/include/glue/macros/generic_test_sql/relationships.sql
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.224520 dbt-glue-1.3.8/dbt/include/glue/macros/materializations/
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.226981 dbt-glue-1.3.8/dbt/include/glue/macros/materializations/incremental/
--rw-r--r--   0 menuetb    (504) staff       (20)     3433 2022-11-24 08:24:34.000000 dbt-glue-1.3.8/dbt/include/glue/macros/materializations/incremental/incremental.sql
--rw-r--r--   0 menuetb    (504) staff       (20)     1689 2022-10-07 12:46:47.000000 dbt-glue-1.3.8/dbt/include/glue/macros/materializations/incremental/strategies.sql
--rw-r--r--   0 menuetb    (504) staff       (20)     1436 2022-07-11 06:48:28.000000 dbt-glue-1.3.8/dbt/include/glue/macros/materializations/seed.sql
--rw-r--r--   0 menuetb    (504) staff       (20)     4944 2022-09-27 13:12:03.000000 dbt-glue-1.3.8/dbt/include/glue/macros/materializations/snapshot.sql
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.228491 dbt-glue-1.3.8/dbt/include/glue/macros/materializations/table/
--rw-r--r--   0 menuetb    (504) staff       (20)     1159 2022-11-03 13:40:21.000000 dbt-glue-1.3.8/dbt/include/glue/macros/materializations/table/iceberg_table_replace.sql
--rw-r--r--   0 menuetb    (504) staff       (20)      112 2022-07-11 06:48:28.000000 dbt-glue-1.3.8/dbt/include/glue/macros/materializations/view.sql
--rw-r--r--   0 menuetb    (504) staff       (20)      592 2022-10-21 07:23:23.000000 dbt-glue-1.3.8/dbt/include/glue/sample_profiles.yml
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.195714 dbt-glue-1.3.8/dbt/include/glue/tests/
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.229737 dbt-glue-1.3.8/dbt/include/glue/tests/generic/
--rw-r--r--   0 menuetb    (504) staff       (20)      290 2022-07-11 06:48:28.000000 dbt-glue-1.3.8/dbt/include/glue/tests/generic/builtin.sql
-drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2022-12-29 17:25:29.235862 dbt-glue-1.3.8/dbt_glue.egg-info/
--rw-r--r--   0 menuetb    (504) staff       (20)    37177 2022-12-29 17:25:29.000000 dbt-glue-1.3.8/dbt_glue.egg-info/PKG-INFO
--rw-r--r--   0 menuetb    (504) staff       (20)     1230 2022-12-29 17:25:29.000000 dbt-glue-1.3.8/dbt_glue.egg-info/SOURCES.txt
--rw-r--r--   0 menuetb    (504) staff       (20)        1 2022-12-29 17:25:29.000000 dbt-glue-1.3.8/dbt_glue.egg-info/dependency_links.txt
--rw-r--r--   0 menuetb    (504) staff       (20)        1 2022-05-12 16:43:26.000000 dbt-glue-1.3.8/dbt_glue.egg-info/not-zip-safe
--rw-r--r--   0 menuetb    (504) staff       (20)       46 2022-12-29 17:25:29.000000 dbt-glue-1.3.8/dbt_glue.egg-info/requires.txt
--rw-r--r--   0 menuetb    (504) staff       (20)        4 2022-12-29 17:25:29.000000 dbt-glue-1.3.8/dbt_glue.egg-info/top_level.txt
--rw-r--r--   0 menuetb    (504) staff       (20)       38 2022-12-29 17:25:29.238054 dbt-glue-1.3.8/setup.cfg
--rw-r--r--   0 menuetb    (504) staff       (20)     2822 2022-12-29 17:25:21.000000 dbt-glue-1.3.8/setup.py
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.684668 dbt-glue-1.4.0/
+-rw-r--r--   0 menuetb    (504) staff       (20)    10142 2022-04-05 16:42:41.000000 dbt-glue-1.4.0/LICENSE
+-rw-r--r--   0 menuetb    (504) staff       (20)       67 2022-04-05 16:42:41.000000 dbt-glue-1.4.0/NOTICE
+-rw-r--r--   0 menuetb    (504) staff       (20)    43753 2023-04-07 08:31:34.683086 dbt-glue-1.4.0/PKG-INFO
+-rw-r--r--   0 menuetb    (504) staff       (20)    42903 2023-04-06 14:05:38.000000 dbt-glue-1.4.0/README.md
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.637272 dbt-glue-1.4.0/dbt/
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.636739 dbt-glue-1.4.0/dbt/adapters/
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.653197 dbt-glue-1.4.0/dbt/adapters/glue/
+-rw-r--r--   0 menuetb    (504) staff       (20)      394 2023-04-06 15:48:24.000000 dbt-glue-1.4.0/dbt/adapters/glue/__init__.py
+-rw-r--r--   0 menuetb    (504) staff       (20)       17 2023-04-06 14:07:03.000000 dbt-glue-1.4.0/dbt/adapters/glue/__version__.py
+-rw-r--r--   0 menuetb    (504) staff       (20)     3431 2023-04-06 15:50:22.000000 dbt-glue-1.4.0/dbt/adapters/glue/connections.py
+-rw-r--r--   0 menuetb    (504) staff       (20)     2590 2023-04-06 15:50:17.000000 dbt-glue-1.4.0/dbt/adapters/glue/credentials.py
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.657436 dbt-glue-1.4.0/dbt/adapters/glue/gluedbapi/
+-rw-r--r--   0 menuetb    (504) staff       (20)      140 2022-04-05 16:42:41.000000 dbt-glue-1.4.0/dbt/adapters/glue/gluedbapi/__init__.py
+-rw-r--r--   0 menuetb    (504) staff       (20)     1216 2022-07-11 06:48:28.000000 dbt-glue-1.4.0/dbt/adapters/glue/gluedbapi/commons.py
+-rw-r--r--   0 menuetb    (504) staff       (20)     8767 2023-04-06 14:25:36.000000 dbt-glue-1.4.0/dbt/adapters/glue/gluedbapi/connection.py
+-rw-r--r--   0 menuetb    (504) staff       (20)     8229 2023-04-06 15:56:20.000000 dbt-glue-1.4.0/dbt/adapters/glue/gluedbapi/cursor.py
+-rw-r--r--   0 menuetb    (504) staff       (20)    35933 2023-04-07 08:10:50.000000 dbt-glue-1.4.0/dbt/adapters/glue/impl.py
+-rw-r--r--   0 menuetb    (504) staff       (20)     1264 2023-04-07 07:53:59.000000 dbt-glue-1.4.0/dbt/adapters/glue/relation.py
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.637433 dbt-glue-1.4.0/dbt/include/
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.661321 dbt-glue-1.4.0/dbt/include/glue/
+-rw-r--r--   0 menuetb    (504) staff       (20)       51 2022-04-05 16:42:41.000000 dbt-glue-1.4.0/dbt/include/glue/__init__.py
+-rw-r--r--   0 menuetb    (504) staff       (20)       72 2022-07-11 06:48:28.000000 dbt-glue-1.4.0/dbt/include/glue/dbt_project.yml
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.664059 dbt-glue-1.4.0/dbt/include/glue/macros/
+-rw-r--r--   0 menuetb    (504) staff       (20)     5352 2023-01-17 10:30:07.000000 dbt-glue-1.4.0/dbt/include/glue/macros/adapters.sql
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.666901 dbt-glue-1.4.0/dbt/include/glue/macros/generic_test_sql/
+-rw-r--r--   0 menuetb    (504) staff       (20)      494 2022-07-11 06:48:28.000000 dbt-glue-1.4.0/dbt/include/glue/macros/generic_test_sql/accepted_values.sql
+-rw-r--r--   0 menuetb    (504) staff       (20)      370 2022-07-11 06:48:28.000000 dbt-glue-1.4.0/dbt/include/glue/macros/generic_test_sql/relationships.sql
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.670213 dbt-glue-1.4.0/dbt/include/glue/macros/materializations/
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.672385 dbt-glue-1.4.0/dbt/include/glue/macros/materializations/incremental/
+-rw-r--r--   0 menuetb    (504) staff       (20)     4348 2023-01-18 17:12:34.000000 dbt-glue-1.4.0/dbt/include/glue/macros/materializations/incremental/incremental.sql
+-rw-r--r--   0 menuetb    (504) staff       (20)     1689 2022-10-07 12:46:47.000000 dbt-glue-1.4.0/dbt/include/glue/macros/materializations/incremental/strategies.sql
+-rw-r--r--   0 menuetb    (504) staff       (20)     1436 2023-01-06 16:44:08.000000 dbt-glue-1.4.0/dbt/include/glue/macros/materializations/seed.sql
+-rw-r--r--   0 menuetb    (504) staff       (20)    10358 2023-01-18 17:12:34.000000 dbt-glue-1.4.0/dbt/include/glue/macros/materializations/snapshot.sql
+-rw-r--r--   0 menuetb    (504) staff       (20)      112 2022-07-11 06:48:28.000000 dbt-glue-1.4.0/dbt/include/glue/macros/materializations/view.sql
+-rw-r--r--   0 menuetb    (504) staff       (20)      592 2022-10-21 07:23:23.000000 dbt-glue-1.4.0/dbt/include/glue/sample_profiles.yml
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.639593 dbt-glue-1.4.0/dbt/include/glue/tests/
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.673470 dbt-glue-1.4.0/dbt/include/glue/tests/generic/
+-rw-r--r--   0 menuetb    (504) staff       (20)      290 2022-07-11 06:48:28.000000 dbt-glue-1.4.0/dbt/include/glue/tests/generic/builtin.sql
+drwxr-xr-x   0 menuetb    (504) staff       (20)        0 2023-04-07 08:31:34.681885 dbt-glue-1.4.0/dbt_glue.egg-info/
+-rw-r--r--   0 menuetb    (504) staff       (20)    43753 2023-04-07 08:31:34.000000 dbt-glue-1.4.0/dbt_glue.egg-info/PKG-INFO
+-rw-r--r--   0 menuetb    (504) staff       (20)     1157 2023-04-07 08:31:34.000000 dbt-glue-1.4.0/dbt_glue.egg-info/SOURCES.txt
+-rw-r--r--   0 menuetb    (504) staff       (20)        1 2023-04-07 08:31:34.000000 dbt-glue-1.4.0/dbt_glue.egg-info/dependency_links.txt
+-rw-r--r--   0 menuetb    (504) staff       (20)        1 2022-05-12 16:43:26.000000 dbt-glue-1.4.0/dbt_glue.egg-info/not-zip-safe
+-rw-r--r--   0 menuetb    (504) staff       (20)       46 2023-04-07 08:31:34.000000 dbt-glue-1.4.0/dbt_glue.egg-info/requires.txt
+-rw-r--r--   0 menuetb    (504) staff       (20)        4 2023-04-07 08:31:34.000000 dbt-glue-1.4.0/dbt_glue.egg-info/top_level.txt
+-rw-r--r--   0 menuetb    (504) staff       (20)       38 2023-04-07 08:31:34.684891 dbt-glue-1.4.0/setup.cfg
+-rw-r--r--   0 menuetb    (504) staff       (20)     2822 2023-04-06 14:09:13.000000 dbt-glue-1.4.0/setup.py
```

### Comparing `dbt-glue-1.3.8/LICENSE` & `dbt-glue-1.4.0/LICENSE`

 * *Files identical despite different names*

### Comparing `dbt-glue-1.3.8/PKG-INFO` & `dbt-glue-1.4.0/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbt-glue
-Version: 1.3.8
+Version: 1.4.0
 Summary: dbt (data build tool) adapter for Aws Glue
 Home-page: https://github.com/aws-samples/dbt-glue
 Author: moshirm,menuetb,mamallem,segnina
 Author-email: moshirm@amazon.fr, menuetb@amazon.fr, mamallem@amazon.fr, segnina@amazon.fr 
 Classifier: Development Status :: 4 - Beta
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: Microsoft :: Windows
@@ -263,28 +263,28 @@
 | Option  | Description                                        | Required?               | Example                  |
 |---------|----------------------------------------------------|-------------------------|--------------------------|
 | file_format | The file format to use when creating tables (`parquet`, `csv`, `json`, `text`, `jdbc` or `orc`). | Optional | `parquet`|
 | partition_by  | Partition the created table by the specified columns. A directory is created for each partition. | Optional                | `date_day`              |
 | clustered_by  | Each partition in the created table will be split into a fixed number of buckets by the specified columns. | Optional               | `country_code`              |
 | buckets  | The number of buckets to create while clustering | Required if `clustered_by` is specified                | `8`              |
 | custom_location  | By default, the adapter will store your data in the following path: `location path`/`schema`/`table`. If you don't want to follow that default behaviour, you can use this parameter to set your own custom location on S3 | No | `s3://mycustombucket/mycustompath`              |
-
+| hudi_options | When using file_format `hudi`, gives the ability to overwrite any of the default configuration options. | Optional | `{'hoodie.schema.on.read.enable': 'true'}` |
 ## Incremental models
 
 dbt seeks to offer useful and intuitive modeling abstractions by means of its built-in configurations and materializations.
 
 For that reason, the dbt-glue plugin leans heavily on the [`incremental_strategy` config](configuring-incremental-models#about-incremental_strategy). This config tells the incremental materialization how to build models in runs beyond their first. It can be set to one of three values:
  - **`append`** (default): Insert new records without updating or overwriting any existing data.
  - **`insert_overwrite`**: If `partition_by` is specified, overwrite partitions in the table with new data. If no `partition_by` is specified, overwrite the entire table with new data.
- - **`merge`** (Apache Hudi only): Match records based on a `unique_key`; update old records, insert new ones. (If no `unique_key` is specified, all new data is inserted, similar to `append`.)
+ - **`merge`** (Apache Hudi and Apache Iceberg only): Match records based on a `unique_key`; update old records, insert new ones. (If no `unique_key` is specified, all new data is inserted, similar to `append`.)
  
 Each of these strategies has its pros and cons, which we'll discuss below. As with any model config, `incremental_strategy` may be specified in `dbt_project.yml` or within a model file's `config()` block.
 
 **Notes:**
-The default strategie is **`insert_overwrite`**
+The default strategy is **`insert_overwrite`**
 
 ### The `append` strategy
 
 Following the `append` strategy, dbt will perform an `insert into` statement with all new data. The appeal of this strategy is that it is straightforward and functional across all platforms, file types, connection methods, and Apache Spark versions. However, this strategy _cannot_ update, overwrite, or delete existing data, so it is likely to insert duplicate records for many data sources.
 
 #### Source code
 ```sql
@@ -383,15 +383,15 @@
 Specifying `insert_overwrite` as the incremental strategy is optional, since it's the default strategy used when none is specified.
 
 ### The `merge` strategy
 
 **Compatibility:**
 - Hudi : OK
 - Delta Lake : OK
-- Iceberg : On going
+- Iceberg : OK
 - Lake Formation Governed Tables : On going
 
 The simpliest way to work with theses advanced features is to install theses using [Glue connectors](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html).
 
 When using a connector be sure that your IAM role has these policies:
 ```
 {
@@ -444,15 +444,18 @@
 
 #### Source Code example
 ```sql
 {{ config(
     materialized='incremental',
     incremental_strategy='merge',
     unique_key='user_id',
-    file_format='hudi'
+    file_format='hudi',
+    hudi_options={
+        'hoodie.datasource.write.precombine.field': 'eventtime',
+    }
 ) }}
 
 with new_events as (
 
     select * from {{ ref('events') }}
 
     {% if is_incremental() %}
@@ -530,75 +533,161 @@
     max(date_day) as last_seen,
     current_date() as dt
 
 from events
 group by 1
 ```
 
-## Iceberg
+#### Iceberg
 
-The adaptor support Iceberg as an Open Table Format. In order to work with Iceberg,
-setup an Iceberg connector and then create an Iceberg connection in Glue connections.
-Then use the following `conf` in your profile
-```
-connections: iceberg_connection
-conf: "spark.sql.catalog.iceberg_catalog=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.iceberg_catalog.warehouse=s3://your_bucket/prefix --conf spark.sql.catalog.iceberg_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog --conf spark.sql.catalog.iceberg_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.sources.partitionOverwriteMode=dynamic --conf spark.sql.iceberg.handle-timestamp-without-timezone=true"
+**Usage notes:** The `merge` with Iceberg incremental strategy requires:
+- To attach the AmazonEC2ContainerRegistryReadOnly Manged policy to your execution role :
+- To add the following policy to your execution role to enable commit locking in a dynamodb table (more info [here](https://iceberg.apache.org/docs/latest/aws/#dynamodb-lock-manager)). Note that the DynamoDB table specified in the ressource field of this policy should be the one that is mentionned in your dbt profiles (`--conf spark.sql.catalog.glue_catalog.lock.table=myGlueLockTable`). By default, this table is named `myGlueLockTable` and is created automatically (with On-Demand Pricing) when running a dbt-glue model with Incremental Materialization and Iceberg file format. If you want to name the table differently or to create your own table without letting Glue do it on your behalf, please provide the `iceberg_glue_commit_lock_table` parameter with your table name (eg. `MyDynamoDbTable`) in your dbt profile.
+```yaml
+iceberg_glue_commit_lock_table: "MyDynamoDbTable"
 ```
-The `warehouse` conf must be provided, but it's overwritten by the adapter `location` in your profile or `custom_location` in model configuration.
+- the latest connector for icerberg in AWS marketplace uses Ver 0.14.0 where Kryo serialization fails when writing iceberg, use "org.apache.spark.serializer.JavaSerializer" for spark.serializer instead, more info [here](https://github.com/apache/iceberg/pull/546)
 
-As it is now, due to some dbt internal, the iceberg catalog used internally has a hardcoded name `iceberg_catalog`.
-
-
-### Table materialization
-Using table materialization, as for the other formats, the table is dropped and then recreated.
-An example of config is:
+Make sure you update your conf with `--conf spark.sql.catalog.glue_catalog.lock.table=<YourDynamoDBLockTableName>` and, you change the below iam permission with your correct table name.
+```
+{
+    "Version": "2012-10-17",
+    "Statement": [
+        {
+            "Sid": "CommitLockTable",
+            "Effect": "Allow",
+            "Action": [
+                "dynamodb:CreateTable",
+                "dynamodb:BatchGetItem",
+                "dynamodb:BatchWriteItem",
+                "dynamodb:ConditionCheckItem",
+                "dynamodb:PutItem",
+                "dynamodb:DescribeTable",
+                "dynamodb:DeleteItem",
+                "dynamodb:GetItem",
+                "dynamodb:Scan",
+                "dynamodb:Query",
+                "dynamodb:UpdateItem"
+            ],
+            "Resource": "arn:aws:dynamodb:<AWS_REGION>:<AWS_ACCOUNT_ID>:table/myGlueLockTable"
+        }
+    ]
+}
+```
+- To add `file_format: Iceberg` in your table configuration
+- To add a connections in your profile : `connections: name_of_your_iceberg_connector` (
+  - For Athena version 3: 
+    - The adapter is compatible with the Iceberg Connector from AWS Marketplace with Glue 3.0 as Fulfillment option and 0.14.0 (Oct 11, 2022) as Software version)
+    - the latest connector for iceberg in AWS marketplace uses Ver 0.14.0 where Kryo serialization fails when writing iceberg, use "org.apache.spark.serializer.JavaSerializer" for spark.serializer instead, more info [here](https://github.com/apache/iceberg/pull/546) 
+  - For Athena version 2: The adapter is compatible with the Iceberg Connector from AWS Marketplace with Glue 3.0 as Fulfillment option and 0.12.0-2 (Feb 14, 2022) as Software version)
+- To add the following config in your Interactive Session Config (in your profile):  
+```--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions 
+    --conf spark.serializer=org.apache.spark.serializer.KryoSerializer
+    --conf spark.sql.warehouse=s3://<your-bucket-name>
+    --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog 
+    --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog 
+    --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO 
+    --conf spark.sql.catalog.glue_catalog.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager 
+    --conf spark.sql.catalog.glue_catalog.lock.table=myGlueLockTable  
+    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
+```
+
+dbt will run an [atomic `merge` statement](https://iceberg.apache.org/docs/latest/spark-writes/) which looks nearly identical to the default merge behavior on Snowflake and BigQuery. You need to provide a `unique_key` to perform merge operation otherwise it will fail. This key is to provide in a Python list format and can contains multiple column name to create a composite unique_key. 
+
+##### Notes
+- When using a custom_location in Iceberg, avoid to use final trailing slash. Adding a final trailing slash lead to an un-proper handling of the location, and issues when reading the data from query engines like Trino. The issue should be fixed for Iceberg version > 0.13. Related Github issue can be find [here](https://github.com/apache/iceberg/issues/4582).
+- Iceberg also supports `insert_overwrite` and `append` strategies. 
+- The `warehouse` conf must be provided, but it's overwritten by the adapter `location` in your profile or `custom_location` in model configuration.
+- By default, this materialization has `iceberg_expire_snapshots` set to 'True', if you need to have historical auditable changes, set: `iceberg_expire_snapshots='False'`.
+- Currently, due to some dbt internal, the iceberg catalog used internally when running glue interactive sessions with dbt-glue has a hardcoded name `glue_catalog`. This name is an alias pointing to the AWS Glue Catalog but is specific to each session. If you want to interact with your data in another session without using dbt-glue (from a Glue Studio notebook, for example), you can configure another alias (ie. another name for the Iceberg Catalog). To illustrate this concept, you can set in your configuration file : 
+```
+--conf spark.sql.catalog.RandomCatalogName=org.apache.iceberg.spark.SparkCatalog
+```
+And then run in an AWS Glue Studio Notebook a session with the following config: 
+```
+--conf spark.sql.catalog.AnotherRandomCatalogName=org.apache.iceberg.spark.SparkCatalog
+```
+In both cases, the underlying catalog would be the AWS Glue Catalog, unique in your AWS Account and Region, and you would be able to work with the exact same data. Also make sure that if you change the name of the Glue Catalog Alias, you change it in all the other `--conf` where it's used: 
+```
+ --conf spark.sql.catalog.RandomCatalogName=org.apache.iceberg.spark.SparkCatalog 
+ --conf spark.sql.catalog.RandomCatalogName.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog 
+ ...
+ --conf spark.sql.catalog.RandomCatalogName.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager
+```
+- A full reference to `table_properties` can be found [here](https://iceberg.apache.org/docs/latest/configuration/).
+- Iceberg Tables are natively supported by Athena. Therefore, you can query tables created and operated with dbt-glue adapter from Athena.
+- Incremental Materialization with Iceberg file format supports dbt snapshot. You are able to run a dbt snapshot command that queries an Iceberg Table and create a dbt fashioned snapshot of it. 
 
+#### Profile config example
+```yaml
+test_project:
+  target: dev
+  outputs:
+    dev:
+      type: glue
+      query-comment: my comment
+      role_arn: arn:aws:iam::1234567890:role/GlueInteractiveSessionRole
+      region: eu-west-1
+      glue_version: "3.0"
+      workers: 2
+      worker_type: G.1X
+      schema: "dbt_test_project"
+      session_provisionning_timeout_in_seconds: 120
+      location: "s3://aws-dbt-glue-datalake-1234567890-eu-west-1/"
+      connections: name_of_your_iceberg_connector
+      conf: --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.warehouse=s3://aws-dbt-glue-datalake-1234567890-eu-west-1/dbt_test_project --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO --conf spark.sql.catalog.glue_catalog.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager --conf spark.sql.catalog.glue_catalog.lock.table=myGlueLockTable  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions 
 ```
+
+#### Source Code example
+```sql
 {{ config(
-    materialized='table',
+    materialized='incremental',
+    incremental_strategy='merge',
+    unique_key=['user_id'],
     file_format='iceberg',
-    partition_by=['status'],
-    table_properties={
-    	'write.target-file-size-bytes': '268435456'
-    }
+    iceberg_expire_snapshots='False', 
+    partition_by=['status']
+    table_properties={'write.target-file-size-bytes': '268435456'}
 ) }}
-```
-
 
-### Table replace materialization
-It's possible to use a `materialized='iceberg_table_replace'`, in order to avoid destructive behaviors.
-When `iceberg_table_replace` is used the DDL used under the hood is a `CREATE OR REPLACE`, tha means that
-a new snapshot (or a new version) is added to the table, and old data is still retained.
+with new_events as (
 
-By default, this materialization has `expire_snapshots` set to True, if you need to have historical auditable changes,
-set: `expire_snapshots=False`.
+    select * from {{ ref('events') }}
 
-Full config example:
+    {% if is_incremental() %}
+    where date_day >= date_add(current_date, -1)
+    {% endif %}
 
-```
-{{ config(
-    materialized='iceberg_table_replace',
-    partition_by=['status'],
-    expire_snapshots=False,
-    table_properties={
-    	'write.target-file-size-bytes': '268435456'
-    }
 )
-}}
+
+select
+    user_id,
+    max(date_day) as last_seen
+
+from events
+group by 1
 ```
-A full reference to `table_properties` can be found [here](https://iceberg.apache.org/docs/latest/configuration/).
+#### Iceberg Snapshot source code example
+```sql
 
-### Notes
+{% snapshot demosnapshot %}
+
+{{
+    config(
+        strategy='timestamp',
+        target_schema='jaffle_db',
+        updated_at='dt',
+        file_format='iceberg'
+) }}
 
-#### Trailing slashes in custom location
-When using a custom_location in Iceberg, avoid to use final trailing slash.
-Adding a final trailing slash lead to an un-proper handling of the location, and issues when reading the data from
-query engines like Trino. 
-The issue should be fixed for Iceberg version > 0.13.
-Related Github issue can be find [here](https://github.com/apache/iceberg/issues/4582).
+select * from {{ ref('customers') }}
+
+{% endsnapshot %}
+
+```
 
 ## Monitoring your Glue Interactive Session
 
 Monitoring is an important part of maintaining the reliability, availability,
 and performance of AWS Glue and your other AWS solutions. AWS provides monitoring
 tools that you can use to watch AWS Glue, identify the required number of workers
 required for your Glue Interactive Session, report when something is wrong and
```

### Comparing `dbt-glue-1.3.8/README.md` & `dbt-glue-1.4.0/dbt_glue.egg-info/PKG-INFO`

 * *Files 9% similar despite different names*

```diff
@@ -1,7 +1,28 @@
+Metadata-Version: 2.1
+Name: dbt-glue
+Version: 1.4.0
+Summary: dbt (data build tool) adapter for Aws Glue
+Home-page: https://github.com/aws-samples/dbt-glue
+Author: moshirm,menuetb,mamallem,segnina
+Author-email: moshirm@amazon.fr, menuetb@amazon.fr, mamallem@amazon.fr, segnina@amazon.fr 
+Classifier: Development Status :: 4 - Beta
+Classifier: License :: OSI Approved :: Apache Software License
+Classifier: Operating System :: Microsoft :: Windows
+Classifier: Operating System :: MacOS :: MacOS X
+Classifier: Operating System :: POSIX :: Linux
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Requires-Python: >=3.7
+Description-Content-Type: text/markdown
+License-File: LICENSE
+License-File: NOTICE
+
 <p align="center">
   <img src="/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
 </p>
 
 **[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.
 dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.
 
@@ -242,28 +263,28 @@
 | Option  | Description                                        | Required?               | Example                  |
 |---------|----------------------------------------------------|-------------------------|--------------------------|
 | file_format | The file format to use when creating tables (`parquet`, `csv`, `json`, `text`, `jdbc` or `orc`). | Optional | `parquet`|
 | partition_by  | Partition the created table by the specified columns. A directory is created for each partition. | Optional                | `date_day`              |
 | clustered_by  | Each partition in the created table will be split into a fixed number of buckets by the specified columns. | Optional               | `country_code`              |
 | buckets  | The number of buckets to create while clustering | Required if `clustered_by` is specified                | `8`              |
 | custom_location  | By default, the adapter will store your data in the following path: `location path`/`schema`/`table`. If you don't want to follow that default behaviour, you can use this parameter to set your own custom location on S3 | No | `s3://mycustombucket/mycustompath`              |
-
+| hudi_options | When using file_format `hudi`, gives the ability to overwrite any of the default configuration options. | Optional | `{'hoodie.schema.on.read.enable': 'true'}` |
 ## Incremental models
 
 dbt seeks to offer useful and intuitive modeling abstractions by means of its built-in configurations and materializations.
 
 For that reason, the dbt-glue plugin leans heavily on the [`incremental_strategy` config](configuring-incremental-models#about-incremental_strategy). This config tells the incremental materialization how to build models in runs beyond their first. It can be set to one of three values:
  - **`append`** (default): Insert new records without updating or overwriting any existing data.
  - **`insert_overwrite`**: If `partition_by` is specified, overwrite partitions in the table with new data. If no `partition_by` is specified, overwrite the entire table with new data.
- - **`merge`** (Apache Hudi only): Match records based on a `unique_key`; update old records, insert new ones. (If no `unique_key` is specified, all new data is inserted, similar to `append`.)
+ - **`merge`** (Apache Hudi and Apache Iceberg only): Match records based on a `unique_key`; update old records, insert new ones. (If no `unique_key` is specified, all new data is inserted, similar to `append`.)
  
 Each of these strategies has its pros and cons, which we'll discuss below. As with any model config, `incremental_strategy` may be specified in `dbt_project.yml` or within a model file's `config()` block.
 
 **Notes:**
-The default strategie is **`insert_overwrite`**
+The default strategy is **`insert_overwrite`**
 
 ### The `append` strategy
 
 Following the `append` strategy, dbt will perform an `insert into` statement with all new data. The appeal of this strategy is that it is straightforward and functional across all platforms, file types, connection methods, and Apache Spark versions. However, this strategy _cannot_ update, overwrite, or delete existing data, so it is likely to insert duplicate records for many data sources.
 
 #### Source code
 ```sql
@@ -362,15 +383,15 @@
 Specifying `insert_overwrite` as the incremental strategy is optional, since it's the default strategy used when none is specified.
 
 ### The `merge` strategy
 
 **Compatibility:**
 - Hudi : OK
 - Delta Lake : OK
-- Iceberg : On going
+- Iceberg : OK
 - Lake Formation Governed Tables : On going
 
 The simpliest way to work with theses advanced features is to install theses using [Glue connectors](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html).
 
 When using a connector be sure that your IAM role has these policies:
 ```
 {
@@ -423,15 +444,18 @@
 
 #### Source Code example
 ```sql
 {{ config(
     materialized='incremental',
     incremental_strategy='merge',
     unique_key='user_id',
-    file_format='hudi'
+    file_format='hudi',
+    hudi_options={
+        'hoodie.datasource.write.precombine.field': 'eventtime',
+    }
 ) }}
 
 with new_events as (
 
     select * from {{ ref('events') }}
 
     {% if is_incremental() %}
@@ -509,75 +533,161 @@
     max(date_day) as last_seen,
     current_date() as dt
 
 from events
 group by 1
 ```
 
-## Iceberg
+#### Iceberg
 
-The adaptor support Iceberg as an Open Table Format. In order to work with Iceberg,
-setup an Iceberg connector and then create an Iceberg connection in Glue connections.
-Then use the following `conf` in your profile
-```
-connections: iceberg_connection
-conf: "spark.sql.catalog.iceberg_catalog=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.iceberg_catalog.warehouse=s3://your_bucket/prefix --conf spark.sql.catalog.iceberg_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog --conf spark.sql.catalog.iceberg_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.sources.partitionOverwriteMode=dynamic --conf spark.sql.iceberg.handle-timestamp-without-timezone=true"
+**Usage notes:** The `merge` with Iceberg incremental strategy requires:
+- To attach the AmazonEC2ContainerRegistryReadOnly Manged policy to your execution role :
+- To add the following policy to your execution role to enable commit locking in a dynamodb table (more info [here](https://iceberg.apache.org/docs/latest/aws/#dynamodb-lock-manager)). Note that the DynamoDB table specified in the ressource field of this policy should be the one that is mentionned in your dbt profiles (`--conf spark.sql.catalog.glue_catalog.lock.table=myGlueLockTable`). By default, this table is named `myGlueLockTable` and is created automatically (with On-Demand Pricing) when running a dbt-glue model with Incremental Materialization and Iceberg file format. If you want to name the table differently or to create your own table without letting Glue do it on your behalf, please provide the `iceberg_glue_commit_lock_table` parameter with your table name (eg. `MyDynamoDbTable`) in your dbt profile.
+```yaml
+iceberg_glue_commit_lock_table: "MyDynamoDbTable"
 ```
-The `warehouse` conf must be provided, but it's overwritten by the adapter `location` in your profile or `custom_location` in model configuration.
-
-As it is now, due to some dbt internal, the iceberg catalog used internally has a hardcoded name `iceberg_catalog`.
+- the latest connector for icerberg in AWS marketplace uses Ver 0.14.0 where Kryo serialization fails when writing iceberg, use "org.apache.spark.serializer.JavaSerializer" for spark.serializer instead, more info [here](https://github.com/apache/iceberg/pull/546)
 
+Make sure you update your conf with `--conf spark.sql.catalog.glue_catalog.lock.table=<YourDynamoDBLockTableName>` and, you change the below iam permission with your correct table name.
+```
+{
+    "Version": "2012-10-17",
+    "Statement": [
+        {
+            "Sid": "CommitLockTable",
+            "Effect": "Allow",
+            "Action": [
+                "dynamodb:CreateTable",
+                "dynamodb:BatchGetItem",
+                "dynamodb:BatchWriteItem",
+                "dynamodb:ConditionCheckItem",
+                "dynamodb:PutItem",
+                "dynamodb:DescribeTable",
+                "dynamodb:DeleteItem",
+                "dynamodb:GetItem",
+                "dynamodb:Scan",
+                "dynamodb:Query",
+                "dynamodb:UpdateItem"
+            ],
+            "Resource": "arn:aws:dynamodb:<AWS_REGION>:<AWS_ACCOUNT_ID>:table/myGlueLockTable"
+        }
+    ]
+}
+```
+- To add `file_format: Iceberg` in your table configuration
+- To add a connections in your profile : `connections: name_of_your_iceberg_connector` (
+  - For Athena version 3: 
+    - The adapter is compatible with the Iceberg Connector from AWS Marketplace with Glue 3.0 as Fulfillment option and 0.14.0 (Oct 11, 2022) as Software version)
+    - the latest connector for iceberg in AWS marketplace uses Ver 0.14.0 where Kryo serialization fails when writing iceberg, use "org.apache.spark.serializer.JavaSerializer" for spark.serializer instead, more info [here](https://github.com/apache/iceberg/pull/546) 
+  - For Athena version 2: The adapter is compatible with the Iceberg Connector from AWS Marketplace with Glue 3.0 as Fulfillment option and 0.12.0-2 (Feb 14, 2022) as Software version)
+- To add the following config in your Interactive Session Config (in your profile):  
+```--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions 
+    --conf spark.serializer=org.apache.spark.serializer.KryoSerializer
+    --conf spark.sql.warehouse=s3://<your-bucket-name>
+    --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog 
+    --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog 
+    --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO 
+    --conf spark.sql.catalog.glue_catalog.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager 
+    --conf spark.sql.catalog.glue_catalog.lock.table=myGlueLockTable  
+    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
+```
+
+dbt will run an [atomic `merge` statement](https://iceberg.apache.org/docs/latest/spark-writes/) which looks nearly identical to the default merge behavior on Snowflake and BigQuery. You need to provide a `unique_key` to perform merge operation otherwise it will fail. This key is to provide in a Python list format and can contains multiple column name to create a composite unique_key. 
+
+##### Notes
+- When using a custom_location in Iceberg, avoid to use final trailing slash. Adding a final trailing slash lead to an un-proper handling of the location, and issues when reading the data from query engines like Trino. The issue should be fixed for Iceberg version > 0.13. Related Github issue can be find [here](https://github.com/apache/iceberg/issues/4582).
+- Iceberg also supports `insert_overwrite` and `append` strategies. 
+- The `warehouse` conf must be provided, but it's overwritten by the adapter `location` in your profile or `custom_location` in model configuration.
+- By default, this materialization has `iceberg_expire_snapshots` set to 'True', if you need to have historical auditable changes, set: `iceberg_expire_snapshots='False'`.
+- Currently, due to some dbt internal, the iceberg catalog used internally when running glue interactive sessions with dbt-glue has a hardcoded name `glue_catalog`. This name is an alias pointing to the AWS Glue Catalog but is specific to each session. If you want to interact with your data in another session without using dbt-glue (from a Glue Studio notebook, for example), you can configure another alias (ie. another name for the Iceberg Catalog). To illustrate this concept, you can set in your configuration file : 
+```
+--conf spark.sql.catalog.RandomCatalogName=org.apache.iceberg.spark.SparkCatalog
+```
+And then run in an AWS Glue Studio Notebook a session with the following config: 
+```
+--conf spark.sql.catalog.AnotherRandomCatalogName=org.apache.iceberg.spark.SparkCatalog
+```
+In both cases, the underlying catalog would be the AWS Glue Catalog, unique in your AWS Account and Region, and you would be able to work with the exact same data. Also make sure that if you change the name of the Glue Catalog Alias, you change it in all the other `--conf` where it's used: 
+```
+ --conf spark.sql.catalog.RandomCatalogName=org.apache.iceberg.spark.SparkCatalog 
+ --conf spark.sql.catalog.RandomCatalogName.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog 
+ ...
+ --conf spark.sql.catalog.RandomCatalogName.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager
+```
+- A full reference to `table_properties` can be found [here](https://iceberg.apache.org/docs/latest/configuration/).
+- Iceberg Tables are natively supported by Athena. Therefore, you can query tables created and operated with dbt-glue adapter from Athena.
+- Incremental Materialization with Iceberg file format supports dbt snapshot. You are able to run a dbt snapshot command that queries an Iceberg Table and create a dbt fashioned snapshot of it. 
 
-### Table materialization
-Using table materialization, as for the other formats, the table is dropped and then recreated.
-An example of config is:
-
+#### Profile config example
+```yaml
+test_project:
+  target: dev
+  outputs:
+    dev:
+      type: glue
+      query-comment: my comment
+      role_arn: arn:aws:iam::1234567890:role/GlueInteractiveSessionRole
+      region: eu-west-1
+      glue_version: "3.0"
+      workers: 2
+      worker_type: G.1X
+      schema: "dbt_test_project"
+      session_provisionning_timeout_in_seconds: 120
+      location: "s3://aws-dbt-glue-datalake-1234567890-eu-west-1/"
+      connections: name_of_your_iceberg_connector
+      conf: --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.warehouse=s3://aws-dbt-glue-datalake-1234567890-eu-west-1/dbt_test_project --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO --conf spark.sql.catalog.glue_catalog.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager --conf spark.sql.catalog.glue_catalog.lock.table=myGlueLockTable  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions 
 ```
+
+#### Source Code example
+```sql
 {{ config(
-    materialized='table',
+    materialized='incremental',
+    incremental_strategy='merge',
+    unique_key=['user_id'],
     file_format='iceberg',
-    partition_by=['status'],
-    table_properties={
-    	'write.target-file-size-bytes': '268435456'
-    }
+    iceberg_expire_snapshots='False', 
+    partition_by=['status']
+    table_properties={'write.target-file-size-bytes': '268435456'}
 ) }}
-```
-
 
-### Table replace materialization
-It's possible to use a `materialized='iceberg_table_replace'`, in order to avoid destructive behaviors.
-When `iceberg_table_replace` is used the DDL used under the hood is a `CREATE OR REPLACE`, tha means that
-a new snapshot (or a new version) is added to the table, and old data is still retained.
+with new_events as (
 
-By default, this materialization has `expire_snapshots` set to True, if you need to have historical auditable changes,
-set: `expire_snapshots=False`.
+    select * from {{ ref('events') }}
 
-Full config example:
+    {% if is_incremental() %}
+    where date_day >= date_add(current_date, -1)
+    {% endif %}
 
-```
-{{ config(
-    materialized='iceberg_table_replace',
-    partition_by=['status'],
-    expire_snapshots=False,
-    table_properties={
-    	'write.target-file-size-bytes': '268435456'
-    }
 )
-}}
+
+select
+    user_id,
+    max(date_day) as last_seen
+
+from events
+group by 1
 ```
-A full reference to `table_properties` can be found [here](https://iceberg.apache.org/docs/latest/configuration/).
+#### Iceberg Snapshot source code example
+```sql
 
-### Notes
+{% snapshot demosnapshot %}
+
+{{
+    config(
+        strategy='timestamp',
+        target_schema='jaffle_db',
+        updated_at='dt',
+        file_format='iceberg'
+) }}
 
-#### Trailing slashes in custom location
-When using a custom_location in Iceberg, avoid to use final trailing slash.
-Adding a final trailing slash lead to an un-proper handling of the location, and issues when reading the data from
-query engines like Trino. 
-The issue should be fixed for Iceberg version > 0.13.
-Related Github issue can be find [here](https://github.com/apache/iceberg/issues/4582).
+select * from {{ ref('customers') }}
+
+{% endsnapshot %}
+
+```
 
 ## Monitoring your Glue Interactive Session
 
 Monitoring is an important part of maintaining the reliability, availability,
 and performance of AWS Glue and your other AWS solutions. AWS provides monitoring
 tools that you can use to watch AWS Glue, identify the required number of workers
 required for your Glue Interactive Session, report when something is wrong and
```

### Comparing `dbt-glue-1.3.8/dbt/adapters/glue/connections.py` & `dbt-glue-1.4.0/dbt/adapters/glue/connections.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from contextlib import contextmanager
 import agate
 from typing import Any, List
 from dbt.adapters.sql import SQLConnectionManager
 from dbt.contracts.connection import AdapterResponse
 from dbt.exceptions import (
-    FailedToConnectException,
-    RuntimeException
+    FailedToConnectError,
+    DbtRuntimeError
 )
 import dbt
 from dbt.adapters.glue.gluedbapi import GlueConnection, GlueCursor
 from dbt.events import AdapterLogger
 
 logger = AdapterLogger("Glue")
 
@@ -39,33 +39,33 @@
             return connection
         except Exception as e:
             logger.error(
                 f"Got an error when attempting to open a GlueSession : {e}"
             )
             connection.handle = None
             connection.state = GlueSessionState.FAIL
-            raise FailedToConnectException(f"Got an error when attempting to open a GlueSessions: {e}")
+            raise FailedToConnectError(f"Got an error when attempting to open a GlueSessions: {e}")
 
     def cancel(self, connection):
         """ cancel ongoing queries """
         connection.handle.cancel()
 
     @contextmanager
     def exception_handler(self, sql: str):
         try:
             yield
         except Exception as e:
             logger.debug("Unhandled error while running:\n{}".format(sql))
             self.release()
-            if isinstance(e, RuntimeException):
+            if isinstance(e, DbtRuntimeError):
                 # during a sql query, an internal to dbt exception was raised.
                 # this sounds a lot like a signal handler and probably has
                 # useful information, so raise it without modification.
                 raise
-            raise RuntimeException(str(e))
+            raise DbtRuntimeError(str(e))
 
     @classmethod
     def get_response(cls, cursor) -> AdapterResponse:
         """
         new to support dbt 0.19: this method replaces get_response
         """
         message = ReturnCode.OK
```

### Comparing `dbt-glue-1.3.8/dbt/adapters/glue/credentials.py` & `dbt-glue-1.4.0/dbt/adapters/glue/credentials.py`

 * *Files 14% similar despite different names*

```diff
@@ -23,14 +23,15 @@
     extra_py_files: Optional[str] = None
     delta_athena_prefix: Optional[str] = None
     tags: Optional[str] = None
     database: Optional[str] # type: ignore
     seed_format: Optional[str] = "parquet"
     seed_mode: Optional[str] = "overwrite"
     default_arguments: Optional[str] = None
+    iceberg_glue_commit_lock_table: Optional[str] = "myGlueLockTable"
 
     @property
     def type(self):
         return "glue"
 
     @property
     def unique_field(self):
@@ -42,15 +43,15 @@
         if "database" not in data:
             data["database"] = None
         return data
 
     def __post_init__(self):
         # spark classifies database and schema as the same thing
         if self.database is not None and self.database != self.schema:
-            raise dbt.exceptions.RuntimeException(
+            raise dbt.exceptions.DbtRuntimeError(
                 f"    schema: {self.schema} \n"
                 f"    database: {self.database} \n"
                 f"On Spark, database must be omitted or have the same value as"
                 f" schema."
             )
         self.database = None
 
@@ -73,9 +74,10 @@
             'connections',
             'conf',
             'extra_py_files',
             'delta_athena_prefix',
             'tags',
             'seed_format',
             'seed_mode',
-            'default_arguments'
+            'default_arguments', 
+            'iceberg_glue_commit_lock_table'
         ]
```

### Comparing `dbt-glue-1.3.8/dbt/adapters/glue/gluedbapi/commons.py` & `dbt-glue-1.4.0/dbt/adapters/glue/gluedbapi/commons.py`

 * *Files identical despite different names*

### Comparing `dbt-glue-1.3.8/dbt/adapters/glue/gluedbapi/connection.py` & `dbt-glue-1.4.0/dbt/adapters/glue/gluedbapi/connection.py`

 * *Files 1% similar despite different names*

```diff
@@ -99,15 +99,15 @@
                     "PythonVersion": "3"
                 },
                 **additional_args)
         except Exception as e:
             logger.error(
                 f"Got an error when attempting to open a GlueSession : {e}"
             )
-            raise dbterrors.FailedToConnectException(str(e))
+            raise dbterrors.FailedToConnectError(str(e))
 
         for elapsed in wait(1):
             if self.state == GlueSessionState.READY:
                 return self._session
             if elapsed > self.credentials.session_provisioning_timeout_in_seconds:
                 raise TimeoutError(f"GlueSession took more than {self.credentials.session_provisioning_timeout_in_seconds} seconds to start")
```

### Comparing `dbt-glue-1.3.8/dbt/adapters/glue/gluedbapi/cursor.py` & `dbt-glue-1.4.0/dbt/adapters/glue/gluedbapi/cursor.py`

 * *Files 7% similar despite different names*

```diff
@@ -120,26 +120,26 @@
             else:
                 error_message=f"Glue returned `{status}` for statement {self.statement_id} for code {self.code}, {output.get('ErrorName')}: {output.get('ErrorValue')}"
                 if output.get('ErrorValue').find("is not a view"):
                     self.state = GlueCursorState.ERROR
                     logger.error(error_message)
                 else:
                     logger.debug(error_message)
-                    raise dbterrors.DatabaseException(msg=error_message)
+                    raise dbterrors.DbtDatabaseError(msg=error_message)
 
         if self.state == GlueCursorState.ERROR:
             self._post()
             output = response.get("Statement", {}).get("Output", {})
             error_message=f"Glue cursor returned `{output.get('Status')}` for statement {self.statement_id} for code {self.code}, {output.get('ErrorName')}: {output.get('ErrorValue')}"
             logger.debug(error_message)
-            raise dbterrors.DatabaseException(msg=error_message)
+            raise dbterrors.DbtDatabaseError(msg=error_message)
 
         if self.state in [GlueCursorState.CANCELLED, GlueCursorState.CANCELLING]:
             self._post()
-            raise dbterrors.DatabaseException(
+            raise dbterrors.DbtDatabaseError(
                 msg=f"Statement {self.connection.session_id}.{self.statement_id} cancelled.")
 
         logger.debug("GlueCursor execute successfully")
         return self.response
 
     @property
     def columns(self):
```

### Comparing `dbt-glue-1.3.8/dbt/adapters/glue/relation.py` & `dbt-glue-1.4.0/dbt/adapters/glue/relation.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from typing import Optional
-from dataclasses import dataclass
+from dataclasses import dataclass, field
 from dbt.adapters.base.relation import BaseRelation, Policy
-from dbt.exceptions import RuntimeException
+from dbt.exceptions import DbtRuntimeError
 
 
 @dataclass
 class SparkQuotePolicy(Policy):
     database: bool = False
     schema: bool = False
     identifier: bool = False
@@ -16,26 +16,26 @@
     database: bool = False
     schema: bool = True
     identifier: bool = True
 
 
 @dataclass(frozen=True, eq=False, repr=False)
 class SparkRelation(BaseRelation):
-    quote_policy: SparkQuotePolicy = SparkQuotePolicy()
-    include_policy: SparkIncludePolicy = SparkIncludePolicy()
+    quote_policy: Policy = field(default_factory=lambda: SparkQuotePolicy())
+    include_policy: Policy = field(default_factory=lambda: SparkIncludePolicy())
     quote_character: str = '`'
     is_delta: Optional[bool] = None
     is_hudi: Optional[bool] = None
     information: str = None
 
     def __post_init__(self):
         return
         if self.database != self.schema and self.database:
-            raise RuntimeException('Cannot set database in spark!')
+            raise DbtRuntimeError('Cannot set database in spark!')
 
     def render(self):
         if self.include_policy.database and self.include_policy.schema:
-            raise RuntimeException(
+            raise DbtRuntimeError(
                 'Got a spark relation with schema and database set to '
                 'include, but only one can be set'
             )
         return super().render()
```

### Comparing `dbt-glue-1.3.8/dbt/include/glue/macros/adapters.sql` & `dbt-glue-1.4.0/dbt/include/glue/macros/adapters.sql`

 * *Files 10% similar despite different names*

```diff
@@ -2,39 +2,39 @@
   {%- set custom_location = config.get('custom_location', validator=validation.any[basestring]) -%}
   {%- set file_format = config.get('file_format', validator=validation.any[basestring]) -%}
   {%- set materialized = config.get('materialized') -%}
 
   {%- if custom_location is not none %}
     location '{{ custom_location }}'
   {%- else -%}
-    {% if file_format == 'iceberg' or materialized == 'iceberg_table_replace' %}
+    {% if file_format == 'iceberg' %}
       {{ adapter.get_iceberg_location(relation) }}
     {%- else -%}
     	{{ adapter.get_location(relation) }}
     {%- endif %}
   {%- endif %}
 {%- endmacro -%}
 
 
 {% macro glue__create_csv_table(model, agate_table) -%}
-  {{ adapter.create_csv_table(model, agate_table) }}
+    {{ adapter.create_csv_table(model, agate_table) }}
 {%- endmacro %}
 
 
 {% macro glue__load_csv_rows(model, agate_table) %}
   {{return('')}}
 {%- endmacro %}
 
 {% macro glue__drop_relation(relation) -%}
   {% call statement('drop_relation', auto_begin=False) -%}
   {% set rel_type = adapter.get_table_type(relation)  %}
     {%- if rel_type is not none and rel_type != 'iceberg_table' %}
         drop {{ rel_type }} if exists {{ relation }}
     {%- elif rel_type is not none and rel_type == 'iceberg_table' %}
-    	{%- set default_catalog = 'iceberg_catalog' -%}
+    	{%- set default_catalog = 'glue_catalog' -%}
         drop table if exists {{ default_catalog }}.{{ relation }}
   	{%- else -%}
         drop table if exists {{ relation }}
     {%- endif %}
   {%- endcall %}
 {% endmacro %}
 
@@ -61,26 +61,21 @@
 {% macro glue__create_table_as(temporary, relation, sql) -%}
   {%- set file_format = config.get('file_format', validator=validation.any[basestring]) -%}
   {%- set table_properties = config.get('table_properties', default={}) -%}
 
   {% if temporary -%}
     {{ create_temporary_view(relation, sql) }}
   {%- else -%}
-    {% if file_format == 'iceberg' %}
-    {%- set default_catalog = 'iceberg_catalog' -%}
-    	create table {{ default_catalog }}.{{ relation }}
-    {% else %}
     	create table {{ relation }}
-    {% endif %}
-    {{ glue__file_format_clause() }}
-    {{ partition_cols(label="partitioned by") }}
-    {{ clustered_cols(label="clustered by") }}
-    {{ set_table_properties(table_properties) }}
-    {{ glue__location_clause(relation) }}
-    {{ comment_clause() }}
+  {{ glue__file_format_clause() }}
+	{{ partition_cols(label="partitioned by") }}
+	{{ clustered_cols(label="clustered by") }}
+	{{ set_table_properties(table_properties) }}
+	{{ glue__location_clause(relation) }}
+	{{ comment_clause() }}
 	as
 	{{ sql }}
   {%- endif %}
 {%- endmacro -%}
 
 {% macro glue__create_tmp_table_as(relation, sql) -%}
   {% call statement("create_tmp_table_as", fetch_result=false, auto_begin=false) %}
@@ -146,19 +141,14 @@
   {% endcall %}
 {% endmacro %}
 
 {% macro spark__type_string() -%}
     STRING
 {%- endmacro %}
 
-{% macro iceberg_expire_snapshots(relation, timestamp, keep_versions) -%}
-    {%- set default_catalog = 'iceberg_catalog' -%}
-    {%- set result = adapter.iceberg_expire_snapshots(default_catalog, relation, timestamp, keep_versions ) -%}
-{%- endmacro %}
-
 
 {% macro set_table_properties(table_properties) -%}
 	{%- set table_properties_formatted = [] -%}
 
 	{%- for k in table_properties -%}
   	{% set _ = table_properties_formatted.append("'" + k + "'='" + table_properties[k] + "'") -%}
   {%- endfor -%}
```

### Comparing `dbt-glue-1.3.8/dbt/include/glue/macros/materializations/incremental/incremental.sql` & `dbt-glue-1.4.0/dbt/include/glue/macros/materializations/incremental/incremental.sql`

 * *Files 18% similar despite different names*

```diff
@@ -1,38 +1,52 @@
 {% materialization incremental, adapter='glue' -%}
   
   {#-- Validate early so we don't run SQL if the file_format + strategy combo is invalid --#}
   {%- set raw_file_format = config.get('file_format', default='parquet') -%}
   {%- set raw_strategy = config.get('incremental_strategy', default='insert_overwrite') -%}
   
-  {%- set file_format = dbt_spark_validate_get_file_format(raw_file_format) -%}
-  {%- set strategy = dbt_spark_validate_get_incremental_strategy(raw_strategy, file_format) -%}
-
+  {% if raw_file_format == 'iceberg' %} 
+    {%- set file_format = 'iceberg' -%}
+    {%- set strategy = raw_strategy -%}
+  {% else %}
+    {%- set file_format = dbt_spark_validate_get_file_format(raw_file_format) -%}
+    {%- set strategy = dbt_spark_validate_get_incremental_strategy(raw_strategy, file_format) -%}
+  {% endif %}
   {%- set unique_key = config.get('unique_key', none) -%}
   {% if unique_key is none and file_format == 'hudi' %}
     {{ exceptions.raise_compiler_error("unique_key model configuration is required for HUDI incremental materializations.") }}
   {% endif %}
   {%- set partition_by = config.get('partition_by', none) -%}
   {%- set custom_location = config.get('custom_location', default='empty') -%}
+  {%- set expire_snapshots = config.get('iceberg_expire_snapshots', 'True') -%}
+  {%- set table_properties = config.get('table_properties', default='empty') -%}
+
 
   {%- set full_refresh_config = config.get('full_refresh', default=False) -%}
-  {%- set full_refresh_mode = (flags.FULL_REFRESH == True or full_refresh_config == True) -%}
+  {%- set full_refresh_mode = (flags.FULL_REFRESH == 'True' or full_refresh_config == 'True') -%}
 
   {% set target_relation = this %}
   {% set existing_relation_type = adapter.get_table_type(target_relation)  %}
   {% set tmp_relation = make_temp_relation(target_relation, '_tmp') %}
   {% set is_incremental = 'False' %}
 
   {% call statement() %}
     set spark.sql.autoBroadcastJoinThreshold=-1
   {% endcall %}
 
   {% if file_format == 'hudi' %}
-        {{ adapter.hudi_merge_table(target_relation, sql, unique_key, partition_by, custom_location) }}
+        {%- set hudi_options = config.get('hudi_options', default={}) -%}
+        {{ adapter.hudi_merge_table(target_relation, sql, unique_key, partition_by, custom_location, hudi_options) }}
         {% set build_sql = "select * from " + target_relation.schema + "." + target_relation.identifier + " limit 1 "%}
+  {% elif file_format == 'iceberg' %}
+        {{ adapter.iceberg_write(target_relation, sql, unique_key, partition_by, custom_location, strategy, table_properties) }}
+        {% set build_sql = "select * from glue_catalog." + target_relation.schema + "." + target_relation.identifier + " limit 1 "%}
+        {%- if expire_snapshots == 'True' -%}
+  	      {%- set result = adapter.iceberg_expire_snapshots(target_relation) -%}
+        {%- endif -%}
   {% else %}
       {% if strategy == 'insert_overwrite' and partition_by %}
         {% call statement() %}
           set spark.sql.sources.partitionOverwriteMode = DYNAMIC
         {% endcall %}
       {% endif %}
       {% if existing_relation_type is none %}
@@ -52,19 +66,23 @@
         {% endif %}
       {% else %}
         {{ glue__create_tmp_table_as(tmp_relation, sql) }}
         {% set is_incremental = 'True' %}
         {% set build_sql = dbt_glue_get_incremental_sql(strategy, tmp_relation, target_relation, unique_key) %}
       {% endif %}
   {% endif %}
+	
+  {{ run_hooks(pre_hooks) }}
 
   {%- call statement('main') -%}
      {{ build_sql }}
   {%- endcall -%}
 
+  {{ run_hooks(post_hooks) }}
+
   {% if is_incremental == 'True' %}
     {{ glue__drop_relation(tmp_relation) }}
     {% if file_format == 'delta' %}
         {{ adapter.delta_update_manifest(target_relation, custom_location) }}
     {% endif %}
   {% endif %}
```

### Comparing `dbt-glue-1.3.8/dbt/include/glue/macros/materializations/incremental/strategies.sql` & `dbt-glue-1.4.0/dbt/include/glue/macros/materializations/incremental/strategies.sql`

 * *Files identical despite different names*

### Comparing `dbt-glue-1.3.8/dbt/include/glue/macros/materializations/seed.sql` & `dbt-glue-1.4.0/dbt/include/glue/macros/materializations/seed.sql`

 * *Files identical despite different names*

### Comparing `dbt-glue-1.3.8/dbt/include/glue/sample_profiles.yml` & `dbt-glue-1.4.0/dbt/include/glue/sample_profiles.yml`

 * *Files identical despite different names*

### Comparing `dbt-glue-1.3.8/dbt_glue.egg-info/PKG-INFO` & `dbt-glue-1.4.0/README.md`

 * *Files 11% similar despite different names*

```diff
@@ -1,28 +1,7 @@
-Metadata-Version: 2.1
-Name: dbt-glue
-Version: 1.3.8
-Summary: dbt (data build tool) adapter for Aws Glue
-Home-page: https://github.com/aws-samples/dbt-glue
-Author: moshirm,menuetb,mamallem,segnina
-Author-email: moshirm@amazon.fr, menuetb@amazon.fr, mamallem@amazon.fr, segnina@amazon.fr 
-Classifier: Development Status :: 4 - Beta
-Classifier: License :: OSI Approved :: Apache Software License
-Classifier: Operating System :: Microsoft :: Windows
-Classifier: Operating System :: MacOS :: MacOS X
-Classifier: Operating System :: POSIX :: Linux
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-License-File: LICENSE
-License-File: NOTICE
-
 <p align="center">
   <img src="/etc/dbt-logo-full.svg" alt="dbt logo" width="500"/>
 </p>
 
 **[dbt](https://www.getdbt.com/)** enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications.
 dbt is the T in ELT. Organize, cleanse, denormalize, filter, rename, and pre-aggregate the raw data in your warehouse so that it's ready for analysis.
 
@@ -263,28 +242,28 @@
 | Option  | Description                                        | Required?               | Example                  |
 |---------|----------------------------------------------------|-------------------------|--------------------------|
 | file_format | The file format to use when creating tables (`parquet`, `csv`, `json`, `text`, `jdbc` or `orc`). | Optional | `parquet`|
 | partition_by  | Partition the created table by the specified columns. A directory is created for each partition. | Optional                | `date_day`              |
 | clustered_by  | Each partition in the created table will be split into a fixed number of buckets by the specified columns. | Optional               | `country_code`              |
 | buckets  | The number of buckets to create while clustering | Required if `clustered_by` is specified                | `8`              |
 | custom_location  | By default, the adapter will store your data in the following path: `location path`/`schema`/`table`. If you don't want to follow that default behaviour, you can use this parameter to set your own custom location on S3 | No | `s3://mycustombucket/mycustompath`              |
-
+| hudi_options | When using file_format `hudi`, gives the ability to overwrite any of the default configuration options. | Optional | `{'hoodie.schema.on.read.enable': 'true'}` |
 ## Incremental models
 
 dbt seeks to offer useful and intuitive modeling abstractions by means of its built-in configurations and materializations.
 
 For that reason, the dbt-glue plugin leans heavily on the [`incremental_strategy` config](configuring-incremental-models#about-incremental_strategy). This config tells the incremental materialization how to build models in runs beyond their first. It can be set to one of three values:
  - **`append`** (default): Insert new records without updating or overwriting any existing data.
  - **`insert_overwrite`**: If `partition_by` is specified, overwrite partitions in the table with new data. If no `partition_by` is specified, overwrite the entire table with new data.
- - **`merge`** (Apache Hudi only): Match records based on a `unique_key`; update old records, insert new ones. (If no `unique_key` is specified, all new data is inserted, similar to `append`.)
+ - **`merge`** (Apache Hudi and Apache Iceberg only): Match records based on a `unique_key`; update old records, insert new ones. (If no `unique_key` is specified, all new data is inserted, similar to `append`.)
  
 Each of these strategies has its pros and cons, which we'll discuss below. As with any model config, `incremental_strategy` may be specified in `dbt_project.yml` or within a model file's `config()` block.
 
 **Notes:**
-The default strategie is **`insert_overwrite`**
+The default strategy is **`insert_overwrite`**
 
 ### The `append` strategy
 
 Following the `append` strategy, dbt will perform an `insert into` statement with all new data. The appeal of this strategy is that it is straightforward and functional across all platforms, file types, connection methods, and Apache Spark versions. However, this strategy _cannot_ update, overwrite, or delete existing data, so it is likely to insert duplicate records for many data sources.
 
 #### Source code
 ```sql
@@ -383,15 +362,15 @@
 Specifying `insert_overwrite` as the incremental strategy is optional, since it's the default strategy used when none is specified.
 
 ### The `merge` strategy
 
 **Compatibility:**
 - Hudi : OK
 - Delta Lake : OK
-- Iceberg : On going
+- Iceberg : OK
 - Lake Formation Governed Tables : On going
 
 The simpliest way to work with theses advanced features is to install theses using [Glue connectors](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html).
 
 When using a connector be sure that your IAM role has these policies:
 ```
 {
@@ -444,15 +423,18 @@
 
 #### Source Code example
 ```sql
 {{ config(
     materialized='incremental',
     incremental_strategy='merge',
     unique_key='user_id',
-    file_format='hudi'
+    file_format='hudi',
+    hudi_options={
+        'hoodie.datasource.write.precombine.field': 'eventtime',
+    }
 ) }}
 
 with new_events as (
 
     select * from {{ ref('events') }}
 
     {% if is_incremental() %}
@@ -530,75 +512,161 @@
     max(date_day) as last_seen,
     current_date() as dt
 
 from events
 group by 1
 ```
 
-## Iceberg
+#### Iceberg
 
-The adaptor support Iceberg as an Open Table Format. In order to work with Iceberg,
-setup an Iceberg connector and then create an Iceberg connection in Glue connections.
-Then use the following `conf` in your profile
-```
-connections: iceberg_connection
-conf: "spark.sql.catalog.iceberg_catalog=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.iceberg_catalog.warehouse=s3://your_bucket/prefix --conf spark.sql.catalog.iceberg_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog --conf spark.sql.catalog.iceberg_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.sql.sources.partitionOverwriteMode=dynamic --conf spark.sql.iceberg.handle-timestamp-without-timezone=true"
+**Usage notes:** The `merge` with Iceberg incremental strategy requires:
+- To attach the AmazonEC2ContainerRegistryReadOnly Manged policy to your execution role :
+- To add the following policy to your execution role to enable commit locking in a dynamodb table (more info [here](https://iceberg.apache.org/docs/latest/aws/#dynamodb-lock-manager)). Note that the DynamoDB table specified in the ressource field of this policy should be the one that is mentionned in your dbt profiles (`--conf spark.sql.catalog.glue_catalog.lock.table=myGlueLockTable`). By default, this table is named `myGlueLockTable` and is created automatically (with On-Demand Pricing) when running a dbt-glue model with Incremental Materialization and Iceberg file format. If you want to name the table differently or to create your own table without letting Glue do it on your behalf, please provide the `iceberg_glue_commit_lock_table` parameter with your table name (eg. `MyDynamoDbTable`) in your dbt profile.
+```yaml
+iceberg_glue_commit_lock_table: "MyDynamoDbTable"
 ```
-The `warehouse` conf must be provided, but it's overwritten by the adapter `location` in your profile or `custom_location` in model configuration.
-
-As it is now, due to some dbt internal, the iceberg catalog used internally has a hardcoded name `iceberg_catalog`.
+- the latest connector for icerberg in AWS marketplace uses Ver 0.14.0 where Kryo serialization fails when writing iceberg, use "org.apache.spark.serializer.JavaSerializer" for spark.serializer instead, more info [here](https://github.com/apache/iceberg/pull/546)
 
+Make sure you update your conf with `--conf spark.sql.catalog.glue_catalog.lock.table=<YourDynamoDBLockTableName>` and, you change the below iam permission with your correct table name.
+```
+{
+    "Version": "2012-10-17",
+    "Statement": [
+        {
+            "Sid": "CommitLockTable",
+            "Effect": "Allow",
+            "Action": [
+                "dynamodb:CreateTable",
+                "dynamodb:BatchGetItem",
+                "dynamodb:BatchWriteItem",
+                "dynamodb:ConditionCheckItem",
+                "dynamodb:PutItem",
+                "dynamodb:DescribeTable",
+                "dynamodb:DeleteItem",
+                "dynamodb:GetItem",
+                "dynamodb:Scan",
+                "dynamodb:Query",
+                "dynamodb:UpdateItem"
+            ],
+            "Resource": "arn:aws:dynamodb:<AWS_REGION>:<AWS_ACCOUNT_ID>:table/myGlueLockTable"
+        }
+    ]
+}
+```
+- To add `file_format: Iceberg` in your table configuration
+- To add a connections in your profile : `connections: name_of_your_iceberg_connector` (
+  - For Athena version 3: 
+    - The adapter is compatible with the Iceberg Connector from AWS Marketplace with Glue 3.0 as Fulfillment option and 0.14.0 (Oct 11, 2022) as Software version)
+    - the latest connector for iceberg in AWS marketplace uses Ver 0.14.0 where Kryo serialization fails when writing iceberg, use "org.apache.spark.serializer.JavaSerializer" for spark.serializer instead, more info [here](https://github.com/apache/iceberg/pull/546) 
+  - For Athena version 2: The adapter is compatible with the Iceberg Connector from AWS Marketplace with Glue 3.0 as Fulfillment option and 0.12.0-2 (Feb 14, 2022) as Software version)
+- To add the following config in your Interactive Session Config (in your profile):  
+```--conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions 
+    --conf spark.serializer=org.apache.spark.serializer.KryoSerializer
+    --conf spark.sql.warehouse=s3://<your-bucket-name>
+    --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog 
+    --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog 
+    --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO 
+    --conf spark.sql.catalog.glue_catalog.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager 
+    --conf spark.sql.catalog.glue_catalog.lock.table=myGlueLockTable  
+    --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions
+```
+
+dbt will run an [atomic `merge` statement](https://iceberg.apache.org/docs/latest/spark-writes/) which looks nearly identical to the default merge behavior on Snowflake and BigQuery. You need to provide a `unique_key` to perform merge operation otherwise it will fail. This key is to provide in a Python list format and can contains multiple column name to create a composite unique_key. 
+
+##### Notes
+- When using a custom_location in Iceberg, avoid to use final trailing slash. Adding a final trailing slash lead to an un-proper handling of the location, and issues when reading the data from query engines like Trino. The issue should be fixed for Iceberg version > 0.13. Related Github issue can be find [here](https://github.com/apache/iceberg/issues/4582).
+- Iceberg also supports `insert_overwrite` and `append` strategies. 
+- The `warehouse` conf must be provided, but it's overwritten by the adapter `location` in your profile or `custom_location` in model configuration.
+- By default, this materialization has `iceberg_expire_snapshots` set to 'True', if you need to have historical auditable changes, set: `iceberg_expire_snapshots='False'`.
+- Currently, due to some dbt internal, the iceberg catalog used internally when running glue interactive sessions with dbt-glue has a hardcoded name `glue_catalog`. This name is an alias pointing to the AWS Glue Catalog but is specific to each session. If you want to interact with your data in another session without using dbt-glue (from a Glue Studio notebook, for example), you can configure another alias (ie. another name for the Iceberg Catalog). To illustrate this concept, you can set in your configuration file : 
+```
+--conf spark.sql.catalog.RandomCatalogName=org.apache.iceberg.spark.SparkCatalog
+```
+And then run in an AWS Glue Studio Notebook a session with the following config: 
+```
+--conf spark.sql.catalog.AnotherRandomCatalogName=org.apache.iceberg.spark.SparkCatalog
+```
+In both cases, the underlying catalog would be the AWS Glue Catalog, unique in your AWS Account and Region, and you would be able to work with the exact same data. Also make sure that if you change the name of the Glue Catalog Alias, you change it in all the other `--conf` where it's used: 
+```
+ --conf spark.sql.catalog.RandomCatalogName=org.apache.iceberg.spark.SparkCatalog 
+ --conf spark.sql.catalog.RandomCatalogName.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog 
+ ...
+ --conf spark.sql.catalog.RandomCatalogName.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager
+```
+- A full reference to `table_properties` can be found [here](https://iceberg.apache.org/docs/latest/configuration/).
+- Iceberg Tables are natively supported by Athena. Therefore, you can query tables created and operated with dbt-glue adapter from Athena.
+- Incremental Materialization with Iceberg file format supports dbt snapshot. You are able to run a dbt snapshot command that queries an Iceberg Table and create a dbt fashioned snapshot of it. 
 
-### Table materialization
-Using table materialization, as for the other formats, the table is dropped and then recreated.
-An example of config is:
-
+#### Profile config example
+```yaml
+test_project:
+  target: dev
+  outputs:
+    dev:
+      type: glue
+      query-comment: my comment
+      role_arn: arn:aws:iam::1234567890:role/GlueInteractiveSessionRole
+      region: eu-west-1
+      glue_version: "3.0"
+      workers: 2
+      worker_type: G.1X
+      schema: "dbt_test_project"
+      session_provisionning_timeout_in_seconds: 120
+      location: "s3://aws-dbt-glue-datalake-1234567890-eu-west-1/"
+      connections: name_of_your_iceberg_connector
+      conf: --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions --conf spark.serializer=org.apache.spark.serializer.KryoSerializer --conf spark.sql.warehouse=s3://aws-dbt-glue-datalake-1234567890-eu-west-1/dbt_test_project --conf spark.sql.catalog.glue_catalog=org.apache.iceberg.spark.SparkCatalog --conf spark.sql.catalog.glue_catalog.catalog-impl=org.apache.iceberg.aws.glue.GlueCatalog --conf spark.sql.catalog.glue_catalog.io-impl=org.apache.iceberg.aws.s3.S3FileIO --conf spark.sql.catalog.glue_catalog.lock-impl=org.apache.iceberg.aws.glue.DynamoLockManager --conf spark.sql.catalog.glue_catalog.lock.table=myGlueLockTable  --conf spark.sql.extensions=org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions 
 ```
+
+#### Source Code example
+```sql
 {{ config(
-    materialized='table',
+    materialized='incremental',
+    incremental_strategy='merge',
+    unique_key=['user_id'],
     file_format='iceberg',
-    partition_by=['status'],
-    table_properties={
-    	'write.target-file-size-bytes': '268435456'
-    }
+    iceberg_expire_snapshots='False', 
+    partition_by=['status']
+    table_properties={'write.target-file-size-bytes': '268435456'}
 ) }}
-```
-
 
-### Table replace materialization
-It's possible to use a `materialized='iceberg_table_replace'`, in order to avoid destructive behaviors.
-When `iceberg_table_replace` is used the DDL used under the hood is a `CREATE OR REPLACE`, tha means that
-a new snapshot (or a new version) is added to the table, and old data is still retained.
+with new_events as (
 
-By default, this materialization has `expire_snapshots` set to True, if you need to have historical auditable changes,
-set: `expire_snapshots=False`.
+    select * from {{ ref('events') }}
 
-Full config example:
+    {% if is_incremental() %}
+    where date_day >= date_add(current_date, -1)
+    {% endif %}
 
-```
-{{ config(
-    materialized='iceberg_table_replace',
-    partition_by=['status'],
-    expire_snapshots=False,
-    table_properties={
-    	'write.target-file-size-bytes': '268435456'
-    }
 )
-}}
+
+select
+    user_id,
+    max(date_day) as last_seen
+
+from events
+group by 1
 ```
-A full reference to `table_properties` can be found [here](https://iceberg.apache.org/docs/latest/configuration/).
+#### Iceberg Snapshot source code example
+```sql
 
-### Notes
+{% snapshot demosnapshot %}
+
+{{
+    config(
+        strategy='timestamp',
+        target_schema='jaffle_db',
+        updated_at='dt',
+        file_format='iceberg'
+) }}
 
-#### Trailing slashes in custom location
-When using a custom_location in Iceberg, avoid to use final trailing slash.
-Adding a final trailing slash lead to an un-proper handling of the location, and issues when reading the data from
-query engines like Trino. 
-The issue should be fixed for Iceberg version > 0.13.
-Related Github issue can be find [here](https://github.com/apache/iceberg/issues/4582).
+select * from {{ ref('customers') }}
+
+{% endsnapshot %}
+
+```
 
 ## Monitoring your Glue Interactive Session
 
 Monitoring is an important part of maintaining the reliability, availability,
 and performance of AWS Glue and your other AWS solutions. AWS provides monitoring
 tools that you can use to watch AWS Glue, identify the required number of workers
 required for your Glue Interactive Session, report when something is wrong and
```

### Comparing `dbt-glue-1.3.8/dbt_glue.egg-info/SOURCES.txt` & `dbt-glue-1.4.0/dbt_glue.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -19,15 +19,14 @@
 dbt/include/glue/macros/generic_test_sql/accepted_values.sql
 dbt/include/glue/macros/generic_test_sql/relationships.sql
 dbt/include/glue/macros/materializations/seed.sql
 dbt/include/glue/macros/materializations/snapshot.sql
 dbt/include/glue/macros/materializations/view.sql
 dbt/include/glue/macros/materializations/incremental/incremental.sql
 dbt/include/glue/macros/materializations/incremental/strategies.sql
-dbt/include/glue/macros/materializations/table/iceberg_table_replace.sql
 dbt/include/glue/tests/generic/builtin.sql
 dbt_glue.egg-info/PKG-INFO
 dbt_glue.egg-info/SOURCES.txt
 dbt_glue.egg-info/dependency_links.txt
 dbt_glue.egg-info/not-zip-safe
 dbt_glue.egg-info/requires.txt
 dbt_glue.egg-info/top_level.txt
```

### Comparing `dbt-glue-1.3.8/setup.py` & `dbt-glue-1.4.0/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -34,15 +34,15 @@
             return line.split(delim)[1]
     else:
         raise RuntimeError("Unable to find version string.")
 
 
 package_name = "dbt-glue"
 package_version = get_version("dbt/adapters/glue/__version__.py")
-dbt_version = "1.3.0"
+dbt_version = "1.4.5"
 description = """dbt (data build tool) adapter for Aws Glue"""
 long_description = read('README.md')
 setup(
     name=package_name,
     version=package_version,
     description=description,
     long_description=long_description,
```

