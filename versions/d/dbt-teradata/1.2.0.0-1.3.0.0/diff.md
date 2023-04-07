# Comparing `tmp/dbt-teradata-1.2.0.0.tar.gz` & `tmp/dbt-teradata-1.3.0.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dbt-teradata-1.2.0.0.tar", last modified: Mon Jan 30 11:23:49 2023, max compression
+gzip compressed data, was "dbt-teradata-1.3.0.0.tar", last modified: Fri Apr  7 11:39:49 2023, max compression
```

## Comparing `dbt-teradata-1.2.0.0.tar` & `dbt-teradata-1.3.0.0.tar`

### file list

```diff
@@ -1,42 +1,43 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)    16996 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    16158 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.682274 dbt-teradata-1.2.0.0/dbt/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.682274 dbt-teradata-1.2.0.0/dbt/adapters/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.682274 dbt-teradata-1.2.0.0/dbt/adapters/teradata/
--rw-r--r--   0 runner    (1001) docker     (123)      519 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/adapters/teradata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       20 2023-01-30 11:23:47.000000 dbt-teradata-1.2.0.0/dbt/adapters/teradata/__version__.py
--rw-r--r--   0 runner    (1001) docker     (123)      605 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/adapters/teradata/column.py
--rw-r--r--   0 runner    (1001) docker     (123)     9499 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/adapters/teradata/connections.py
--rw-r--r--   0 runner    (1001) docker     (123)    11132 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/adapters/teradata/impl.py
--rw-r--r--   0 runner    (1001) docker     (123)      945 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/adapters/teradata/relation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.682274 dbt-teradata-1.2.0.0/dbt/include/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/dbt/include/teradata/
--rw-r--r--   0 runner    (1001) docker     (123)       51 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)       76 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/dbt_project.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/
--rw-r--r--   0 runner    (1001) docker     (123)     9880 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/adapters.sql
--rw-r--r--   0 runner    (1001) docker     (123)     1543 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/apply_grants.sql
--rw-r--r--   0 runner    (1001) docker     (123)     5330 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/catalog.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.682274 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/incremental/
--rw-r--r--   0 runner    (1001) docker     (123)      809 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/incremental/helpers.sql
--rw-r--r--   0 runner    (1001) docker     (123)     2308 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/incremental/incremental.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/seed/
--rw-r--r--   0 runner    (1001) docker     (123)     5020 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/seed/seed.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/snapshot/
--rw-r--r--   0 runner    (1001) docker     (123)    10294 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/snapshot/snapshot.sql
--rw-r--r--   0 runner    (1001) docker     (123)      893 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/snapshot/snapshot_merge.sql
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/snapshot/strategies.sql
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/test/
--rw-r--r--   0 runner    (1001) docker     (123)      513 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/test/test.sql
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-01-30 11:23:26.000000 dbt-teradata-1.2.0.0/dbt/include/teradata/sample_profiles.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/dbt_teradata.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    16996 2023-01-30 11:23:49.000000 dbt-teradata-1.2.0.0/dbt_teradata.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1115 2023-01-30 11:23:49.000000 dbt-teradata-1.2.0.0/dbt_teradata.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 11:23:49.000000 dbt-teradata-1.2.0.0/dbt_teradata.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       39 2023-01-30 11:23:49.000000 dbt-teradata-1.2.0.0/dbt_teradata.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        4 2023-01-30 11:23:49.000000 dbt-teradata-1.2.0.0/dbt_teradata.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-30 11:23:49.686274 dbt-teradata-1.2.0.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1811 2023-01-30 11:23:47.000000 dbt-teradata-1.2.0.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.812340 dbt-teradata-1.3.0.0/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)    21235 2023-04-07 11:39:49.812340 dbt-teradata-1.3.0.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    20969 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.808340 dbt-teradata-1.3.0.0/dbt/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.808340 dbt-teradata-1.3.0.0/dbt/adapters/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.808340 dbt-teradata-1.3.0.0/dbt/adapters/teradata/
+-rw-r--r--   0 runner    (1001) docker     (123)      519 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/adapters/teradata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       20 2023-04-07 11:39:48.000000 dbt-teradata-1.3.0.0/dbt/adapters/teradata/__version__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      605 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/adapters/teradata/column.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9499 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/adapters/teradata/connections.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11715 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/adapters/teradata/impl.py
+-rw-r--r--   0 runner    (1001) docker     (123)      945 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/adapters/teradata/relation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.808340 dbt-teradata-1.3.0.0/dbt/include/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.808340 dbt-teradata-1.3.0.0/dbt/include/teradata/
+-rw-r--r--   0 runner    (1001) docker     (123)       51 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)       76 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/dbt_project.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.808340 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/
+-rw-r--r--   0 runner    (1001) docker     (123)     9880 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/adapters.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     1543 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/apply_grants.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     5330 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/catalog.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.808340 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.812340 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/incremental/
+-rw-r--r--   0 runner    (1001) docker     (123)     1128 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/incremental/helpers.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     2765 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/incremental/incremental.sql
+-rw-r--r--   0 runner    (1001) docker     (123)     1235 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/incremental/strategies.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.812340 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/seed/
+-rw-r--r--   0 runner    (1001) docker     (123)     5020 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/seed/seed.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.812340 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/snapshot/
+-rw-r--r--   0 runner    (1001) docker     (123)    10294 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/snapshot/snapshot.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      893 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/snapshot/snapshot_merge.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/snapshot/strategies.sql
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.812340 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/test/
+-rw-r--r--   0 runner    (1001) docker     (123)      513 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/test/test.sql
+-rw-r--r--   0 runner    (1001) docker     (123)      403 2023-04-07 11:39:24.000000 dbt-teradata-1.3.0.0/dbt/include/teradata/sample_profiles.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 11:39:49.812340 dbt-teradata-1.3.0.0/dbt_teradata.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    21235 2023-04-07 11:39:49.000000 dbt-teradata-1.3.0.0/dbt_teradata.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1187 2023-04-07 11:39:49.000000 dbt-teradata-1.3.0.0/dbt_teradata.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 11:39:49.000000 dbt-teradata-1.3.0.0/dbt_teradata.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       39 2023-04-07 11:39:49.000000 dbt-teradata-1.3.0.0/dbt_teradata.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        4 2023-04-07 11:39:49.000000 dbt-teradata-1.3.0.0/dbt_teradata.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 11:39:49.812340 dbt-teradata-1.3.0.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1877 2023-04-07 11:39:48.000000 dbt-teradata-1.3.0.0/setup.py
```

### Comparing `dbt-teradata-1.2.0.0/LICENSE` & `dbt-teradata-1.3.0.0/LICENSE`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/PKG-INFO` & `dbt-teradata-1.3.0.0/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dbt-teradata
-Version: 1.2.0.0
+Version: 1.3.0.0
 Summary: The Teradata adapter plugin for dbt (data build tool)
 Home-page: https://github.com/Teradata/dbt-teradata
 Author: Teradata Corporation
 Author-email: developers@teradata.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
@@ -26,15 +26,15 @@
 
 ## Installation
 
 ```
 pip install dbt-teradata
 ```
 
-If you are new to dbt on Teradata see [dbt with Teradata Vantage tutorial](https://quickstarts.teradata.com/docs/17.10/dbt.html).
+If you are new to dbt on Teradata see [dbt with Teradata Vantage tutorial](https://quickstarts.teradata.com/dbt.html).
 
 ## Sample profile
 
 Here is a working example of a `dbt-teradata` profile:
 
 ```yaml
 my-teradata-db-profile:
@@ -57,14 +57,15 @@
 | -------------- | ----------- | ----------- | ----------- | ----------- | ----------- |
 | 0.19.0.x           | ✅          | ✅          | ✅          | ❌          | ❌          |
 | 0.20.0.x           | ✅          | ✅          | ✅          | ✅          | ❌          |
 | 0.21.1.x           | ✅          | ✅          | ✅          | ✅          | ❌          |
 | 1.0.0.x           | ❌           | ✅          | ✅          | ✅          | ❌          |
 |1.1.0.x            | ❌           | ✅          | ✅          | ✅          | ✅          |
 |1.2.0.x            | ❌           | ✅          | ✅          | ✅          | ✅          |
+|1.3.0.x            | ❌           | ✅          | ✅          | ✅          | ✅          |
 
 
 ##  dbt dependent packages version compatibility
 | dbt-teradta |  dbt-core  | dbt-teradata-util |  dbt-util      |
 |-------------|------------|-------------------|----------------|
 | 1.2.x       | 1.2.x      | 0.1.0             | 0.9.x or below |
 
@@ -211,14 +212,21 @@
 ### Materializations
 
 * `view`
 * `table`
 * `ephemeral`
 * `incremental`
 
+#### Incremental Materialization
+The following incremental materialization strategies are supported:
+* `append` (default)
+* `delete+insert`
+
+To learn more about dbt incremental strategies please check [the dbt incremental strategy documentation](https://docs.getdbt.com/docs/build/incremental-models#about-incremental_strategy).
+
 ### Commands
 
 All dbt commands are supported.
 
 ### Custom configurations
 
 #### General
@@ -469,16 +477,15 @@
     seeds:
       <project-name>:
         +use_fastload: true
     ```
 
 #### Grants
 
-Grants are supported in dbt-teradata adapter with release version 1.2.0 and above
-You can manage access to the datasets you're producing with dbt by using grants. To implement these permissions, define grants as resource configs on each model, seed, or snapshot. Define the default grants that apply to the entire project in your ```dbt_project.yml```, and define model-specific grants within each model's SQL or YAML file.
+Grants are supported in dbt-teradata adapter with release version 1.2.0 and above. You can use grants to manage access to the datasets you're producing with dbt. To implement these permissions, define grants as resource configs on each model, seed, or snapshot. Define the default grants that apply to the entire project in your `dbt_project.yml`, and define model-specific grants within each model's SQL or YAML file.
 
 for e.g. :
   models/schema.yml
   ```yaml
   models:
     - name: model_name
       config:
@@ -493,32 +500,90 @@
   - name: model_name
     config:
       materialized: table
       grants:
         select: ["user_b"]
         insert: ["user_c"]
   ```
+> :information_source: `copy_grants` is not supported in Teradata.
+
+More on Grants can be found at https://docs.getdbt.com/reference/resource-configs/grants
+
+### Cross DB macros
+Starting with release 1.3, some macros were migrated from [teradata-dbt-utils](https://github.com/Teradata/dbt-teradata-utils) dbt package to the connector. See the table below for the macros supported from the connector.
+
+For using cross DB macros, teradata-utils as a macro namespace will not be used, as cross DB macros have been migrated from teradata-utils to Dbt-Teradata.
+
+
+#### Compatibility
+
+|     Macro Group       |           Macro Name          |         Status        |                                 Comment                                |
+|:---------------------:|:-----------------------------:|:---------------------:|:----------------------------------------------------------------------:|
+| Cross-database macros | current_timestamp             | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | dateadd                       | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | datediff                      | :white_check_mark:    | custom macro provided, see [compatibility note](#datediff)             |
+| Cross-database macros | split_part                    | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | date_trunc                    | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | hash                          | :white_check_mark:    | custom macro provided, see [compatibility note](#hash)                 |
+| Cross-database macros | replace                       | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | type_string                   | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | last_day                      | :white_check_mark:    | no customization needed, see [compatibility note](#last_day)           |
+| Cross-database macros | width_bucket                  | :white_check_mark:    | no customization
+
 
-copy_grants is not supported in Teradata.
-More on Grants can be found over https://docs.getdbt.com/reference/resource-configs/grants
+#### examples for cross DB macros
+Replace:
+{{ dbt.replace("string_text_column", "old_chars", "new_chars") }}
+{{ replace('abcgef', 'g', 'd') }}
 
+Date truncate:
+{{ dbt.date_trunc("date_part", "date") }}
+{{ dbt.date_trunc("DD", "'2018-01-05 12:00:00'") }}
+
+#### <a name="datediff"></a>datediff
+`datediff` macro in teradata supports difference between dates. Differece between timestamps is not supported.
+
+#### <a name="hash"></a>hash
+
+`Hash` macro needs an `md5` function implementation. Teradata doesn't support `md5` natively. You need to install a User Defined Function (UDF):
+1. Download the md5 UDF implementation from Teradata (registration required): https://downloads.teradata.com/download/extensibility/md5-message-digest-udf.
+1. Unzip the package and go to `src` directory.
+1. Start up `bteq` and connect to your database.
+1. Create database `GLOBAL_FUNCTIONS` that will host the UDF. You can't change the database name as it's hardcoded in the macro:
+    ```sql
+    CREATE DATABASE GLOBAL_FUNCTIONS AS PERMANENT = 60e6, SPOOL = 120e6;
+    ```
+1. Create the UDF. Replace `<CURRENT_USER>` with your current database user:
+    ```sql
+    GRANT CREATE FUNCTION ON GLOBAL_FUNCTIONS TO <CURRENT_USER>;
+    DATABASE GLOBAL_FUNCTIONS;
+    .run file = hash_md5.btq
+    ```
+1. Grant permissions to run the UDF with grant option.
+    ```sql
+    GRANT EXECUTE FUNCTION ON GLOBAL_FUNCTIONS TO PUBLIC WITH GRANT OPTION;
+    ```
+#### <a name="last_day"></a>last_day
+
+`last_day` in `teradata_utils`, unlike the corresponding macro in `dbt_utils`, doesn't support `quarter` datepart.
 
 ## Common Teradata-specific tasks
 * *collect statistics* - when a table is created or modified significantly, there might be a need to tell Teradata to collect statistics for the optimizer. It can be done using `COLLECT STATISTICS` command. You can perform this step using dbt's `post-hooks`, e.g.:
   ```yaml
   {{ config(
     post_hook=[
       "COLLECT STATISTICS ON  {{ this }} COLUMN (column_1,  column_2  ...);"
       ]
   )}}
   ```
   See [Collecting Statistics documentation](https://docs.teradata.com/r/76g1CuvvQlYBjb2WPIuk3g/RAyUdGfvREwbO9J0DMNpLw) for more information.
 
 ## Support for `dbt-utils` package
 `dbt-utils` package is supported through `teradata/teradata_utils` dbt package. The package provides a compatibility layer between `dbt_utils` and `dbt-teradata`. See [teradata_utils](https://hub.getdbt.com/teradata/teradata_utils/latest/) package for install instructions.
+
 ## Limitations
 
 ### Transaction mode
 Only ANSI transaction mode is supported.
 
 ## Credits
```

### Comparing `dbt-teradata-1.2.0.0/README.md` & `dbt-teradata-1.3.0.0/dbt_teradata.egg-info/PKG-INFO`

 * *Files 27% similar despite different names*

```diff
@@ -1,18 +1,40 @@
+Metadata-Version: 2.1
+Name: dbt-teradata
+Version: 1.3.0.0
+Summary: The Teradata adapter plugin for dbt (data build tool)
+Home-page: https://github.com/Teradata/dbt-teradata
+Author: Teradata Corporation
+Author-email: developers@teradata.com
+License: UNKNOWN
+Platform: UNKNOWN
+Classifier: Development Status :: 5 - Production/Stable
+Classifier: License :: OSI Approved :: Apache Software License
+Classifier: Operating System :: Microsoft :: Windows
+Classifier: Operating System :: MacOS :: MacOS X
+Classifier: Operating System :: POSIX :: Linux
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Requires-Python: >=3.7,<3.11
+Description-Content-Type: text/markdown
+License-File: LICENSE
+
 # dbt-teradata
 
 This plugin ports [dbt](https://getdbt.com) functionality to Teradata Vantage.
 
 ## Installation
 
 ```
 pip install dbt-teradata
 ```
 
-If you are new to dbt on Teradata see [dbt with Teradata Vantage tutorial](https://quickstarts.teradata.com/docs/17.10/dbt.html).
+If you are new to dbt on Teradata see [dbt with Teradata Vantage tutorial](https://quickstarts.teradata.com/dbt.html).
 
 ## Sample profile
 
 Here is a working example of a `dbt-teradata` profile:
 
 ```yaml
 my-teradata-db-profile:
@@ -35,14 +57,15 @@
 | -------------- | ----------- | ----------- | ----------- | ----------- | ----------- |
 | 0.19.0.x           | ✅          | ✅          | ✅          | ❌          | ❌          |
 | 0.20.0.x           | ✅          | ✅          | ✅          | ✅          | ❌          |
 | 0.21.1.x           | ✅          | ✅          | ✅          | ✅          | ❌          |
 | 1.0.0.x           | ❌           | ✅          | ✅          | ✅          | ❌          |
 |1.1.0.x            | ❌           | ✅          | ✅          | ✅          | ✅          |
 |1.2.0.x            | ❌           | ✅          | ✅          | ✅          | ✅          |
+|1.3.0.x            | ❌           | ✅          | ✅          | ✅          | ✅          |
 
 
 ##  dbt dependent packages version compatibility
 | dbt-teradta |  dbt-core  | dbt-teradata-util |  dbt-util      |
 |-------------|------------|-------------------|----------------|
 | 1.2.x       | 1.2.x      | 0.1.0             | 0.9.x or below |
 
@@ -189,14 +212,21 @@
 ### Materializations
 
 * `view`
 * `table`
 * `ephemeral`
 * `incremental`
 
+#### Incremental Materialization
+The following incremental materialization strategies are supported:
+* `append` (default)
+* `delete+insert`
+
+To learn more about dbt incremental strategies please check [the dbt incremental strategy documentation](https://docs.getdbt.com/docs/build/incremental-models#about-incremental_strategy).
+
 ### Commands
 
 All dbt commands are supported.
 
 ### Custom configurations
 
 #### General
@@ -447,16 +477,15 @@
     seeds:
       <project-name>:
         +use_fastload: true
     ```
 
 #### Grants
 
-Grants are supported in dbt-teradata adapter with release version 1.2.0 and above
-You can manage access to the datasets you're producing with dbt by using grants. To implement these permissions, define grants as resource configs on each model, seed, or snapshot. Define the default grants that apply to the entire project in your ```dbt_project.yml```, and define model-specific grants within each model's SQL or YAML file.
+Grants are supported in dbt-teradata adapter with release version 1.2.0 and above. You can use grants to manage access to the datasets you're producing with dbt. To implement these permissions, define grants as resource configs on each model, seed, or snapshot. Define the default grants that apply to the entire project in your `dbt_project.yml`, and define model-specific grants within each model's SQL or YAML file.
 
 for e.g. :
   models/schema.yml
   ```yaml
   models:
     - name: model_name
       config:
@@ -471,37 +500,97 @@
   - name: model_name
     config:
       materialized: table
       grants:
         select: ["user_b"]
         insert: ["user_c"]
   ```
+> :information_source: `copy_grants` is not supported in Teradata.
+
+More on Grants can be found at https://docs.getdbt.com/reference/resource-configs/grants
+
+### Cross DB macros
+Starting with release 1.3, some macros were migrated from [teradata-dbt-utils](https://github.com/Teradata/dbt-teradata-utils) dbt package to the connector. See the table below for the macros supported from the connector.
+
+For using cross DB macros, teradata-utils as a macro namespace will not be used, as cross DB macros have been migrated from teradata-utils to Dbt-Teradata.
+
+
+#### Compatibility
+
+|     Macro Group       |           Macro Name          |         Status        |                                 Comment                                |
+|:---------------------:|:-----------------------------:|:---------------------:|:----------------------------------------------------------------------:|
+| Cross-database macros | current_timestamp             | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | dateadd                       | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | datediff                      | :white_check_mark:    | custom macro provided, see [compatibility note](#datediff)             |
+| Cross-database macros | split_part                    | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | date_trunc                    | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | hash                          | :white_check_mark:    | custom macro provided, see [compatibility note](#hash)                 |
+| Cross-database macros | replace                       | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | type_string                   | :white_check_mark:    | custom macro provided                                                  |
+| Cross-database macros | last_day                      | :white_check_mark:    | no customization needed, see [compatibility note](#last_day)           |
+| Cross-database macros | width_bucket                  | :white_check_mark:    | no customization
+
 
-copy_grants is not supported in Teradata.
-More on Grants can be found over https://docs.getdbt.com/reference/resource-configs/grants
+#### examples for cross DB macros
+Replace:
+{{ dbt.replace("string_text_column", "old_chars", "new_chars") }}
+{{ replace('abcgef', 'g', 'd') }}
 
+Date truncate:
+{{ dbt.date_trunc("date_part", "date") }}
+{{ dbt.date_trunc("DD", "'2018-01-05 12:00:00'") }}
+
+#### <a name="datediff"></a>datediff
+`datediff` macro in teradata supports difference between dates. Differece between timestamps is not supported.
+
+#### <a name="hash"></a>hash
+
+`Hash` macro needs an `md5` function implementation. Teradata doesn't support `md5` natively. You need to install a User Defined Function (UDF):
+1. Download the md5 UDF implementation from Teradata (registration required): https://downloads.teradata.com/download/extensibility/md5-message-digest-udf.
+1. Unzip the package and go to `src` directory.
+1. Start up `bteq` and connect to your database.
+1. Create database `GLOBAL_FUNCTIONS` that will host the UDF. You can't change the database name as it's hardcoded in the macro:
+    ```sql
+    CREATE DATABASE GLOBAL_FUNCTIONS AS PERMANENT = 60e6, SPOOL = 120e6;
+    ```
+1. Create the UDF. Replace `<CURRENT_USER>` with your current database user:
+    ```sql
+    GRANT CREATE FUNCTION ON GLOBAL_FUNCTIONS TO <CURRENT_USER>;
+    DATABASE GLOBAL_FUNCTIONS;
+    .run file = hash_md5.btq
+    ```
+1. Grant permissions to run the UDF with grant option.
+    ```sql
+    GRANT EXECUTE FUNCTION ON GLOBAL_FUNCTIONS TO PUBLIC WITH GRANT OPTION;
+    ```
+#### <a name="last_day"></a>last_day
+
+`last_day` in `teradata_utils`, unlike the corresponding macro in `dbt_utils`, doesn't support `quarter` datepart.
 
 ## Common Teradata-specific tasks
 * *collect statistics* - when a table is created or modified significantly, there might be a need to tell Teradata to collect statistics for the optimizer. It can be done using `COLLECT STATISTICS` command. You can perform this step using dbt's `post-hooks`, e.g.:
   ```yaml
   {{ config(
     post_hook=[
       "COLLECT STATISTICS ON  {{ this }} COLUMN (column_1,  column_2  ...);"
       ]
   )}}
   ```
   See [Collecting Statistics documentation](https://docs.teradata.com/r/76g1CuvvQlYBjb2WPIuk3g/RAyUdGfvREwbO9J0DMNpLw) for more information.
 
 ## Support for `dbt-utils` package
 `dbt-utils` package is supported through `teradata/teradata_utils` dbt package. The package provides a compatibility layer between `dbt_utils` and `dbt-teradata`. See [teradata_utils](https://hub.getdbt.com/teradata/teradata_utils/latest/) package for install instructions.
+
 ## Limitations
 
 ### Transaction mode
 Only ANSI transaction mode is supported.
 
 ## Credits
 
 The adapter was originally created by [Doug Beatty](https://github.com/dbeatty10). Teradata took over the adapter in January 2022. We are grateful to Doug for founding the project and accelerating the integration of dbt + Teradata.
 
 ## License
 
 The adapter is published using Apache-2.0 License. Please see [the license](LICENSE) for terms and conditions, such as creating derivative work and the support model. 
+
+
```

### Comparing `dbt-teradata-1.2.0.0/dbt/adapters/teradata/__init__.py` & `dbt-teradata-1.3.0.0/dbt/adapters/teradata/__init__.py`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/adapters/teradata/column.py` & `dbt-teradata-1.3.0.0/dbt/adapters/teradata/column.py`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/adapters/teradata/connections.py` & `dbt-teradata-1.3.0.0/dbt/adapters/teradata/connections.py`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/adapters/teradata/impl.py` & `dbt-teradata-1.3.0.0/dbt/adapters/teradata/impl.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,318 +1,323 @@
-from concurrent.futures import Future
-from dataclasses import dataclass, asdict
-from typing import Optional, List, Dict, Any, Union, Iterable, Callable, Set
-import agate
-
-import dbt
-import dbt.exceptions
-
-from dbt.adapters.base.impl import catch_as_completed
-from dbt.adapters.base.relation import InformationSchema
-from dbt.adapters.sql import SQLAdapter
-from dbt.adapters.teradata import TeradataConnectionManager
-from dbt.adapters.teradata import TeradataRelation
-from dbt.adapters.teradata import TeradataColumn
-from dbt.adapters.base.meta import available
-from dbt.adapters.base import BaseRelation
-from dbt.clients.agate_helper import DEFAULT_TYPE_TESTER, table_from_rows
-from dbt.contracts.graph.manifest import Manifest
-from dbt.events import AdapterLogger
-logger = AdapterLogger("teradata")
-from dbt.utils import executor
-
-LIST_SCHEMAS_MACRO_NAME = 'list_schemas'
-LIST_RELATIONS_MACRO_NAME = 'list_relations_without_caching'
-GET_CATALOG_MACRO_NAME = 'get_catalog'
-
-def _expect_row_value(key: str, row: agate.Row):
-    if key not in row.keys():
-        raise dbt.exceptions.InternalException(
-            f'Got a row without \'{key}\' column, columns: {row.keys()}'
-        )
-
-    return row[key]
-
-def _catalog_filter_schemas(manifest: Manifest) -> Callable[[agate.Row], bool]:
-    schemas = frozenset((None, s.lower()) for d, s in manifest.get_used_schemas())
-
-    def test(row: agate.Row) -> bool:
-        table_database = _expect_row_value('table_database', row)
-        table_schema = _expect_row_value('table_schema', row)
-        if table_schema is None:
-            return False
-        return (table_database, table_schema.lower()) in schemas
-
-    return test
-
-
-class TeradataAdapter(SQLAdapter):
-    Relation = TeradataRelation
-    Column = TeradataColumn
-    ConnectionManager = TeradataConnectionManager
-
-    @classmethod
-    def date_function(cls):
-        return 'current_date()'
-
-    @available
-    def verify_database(self, database):
-        if database.startswith('"'):
-            database = database.strip('"')
-        expected = self.config.credentials.schema
-        if database.lower() != expected.lower():
-            raise dbt.exceptions.NotImplementedException(
-                'Cross-db references not allowed in {} ({} vs {})'
-                .format(self.type(), database, expected)
-            )
-        # return an empty string on success so macros can call this
-        return ''
-
-    @classmethod
-    def convert_text_type(cls, agate_table: agate.Table, col_idx: int) -> str:
-        return "LONG VARCHAR"
-
-    @classmethod
-    def convert_datetime_type(cls, agate_table: agate.Table, col_idx: int) -> str:
-        return "TIMESTAMP(0)"
-
-    @classmethod
-    def convert_time_type(cls, agate_table: agate.Table, col_idx: int) -> str:
-        return "TIME"
-
-    @classmethod
-    def convert_date_type(cls, agate_table: agate.Table, col_idx: int) -> str:
-        return "DATE"
-
-    @classmethod
-    def convert_boolean_type(cls, agate_table: agate.Table, col_idx: int) -> str:
-        return "BYTEINT"
-
-    @classmethod
-    def convert_number_type(
-        cls, agate_table: agate.Table, col_idx: int
-    ) -> str:
-        decimals = agate_table.aggregate(agate.MaxPrecision(col_idx))
-        return "FLOAT" if decimals else "INTEGER"
-
-    def quote(self, identifier):
-        return '"{}"'.format(identifier)
-
-    def list_relations_without_caching(
-        self, schema_relation: TeradataRelation
-    ) -> List[TeradataRelation]:
-        kwargs = {'schema_relation': schema_relation}
-        try:
-            results = self.execute_macro(
-                LIST_RELATIONS_MACRO_NAME,
-                kwargs=kwargs
-            )
-        except dbt.exceptions.RuntimeException as e:
-            errmsg = getattr(e, 'msg', '')
-            if f"Teradata database '{schema_relation}' not found" in errmsg:
-                return []
-            else:
-                description = "Error while retrieving information about"
-                logger.debug(f"{description} {schema_relation}: {e.msg}")
-                return []
-
-        relations = []
-        for row in results:
-            if len(row) != 4:
-                raise dbt.exceptions.RuntimeException(
-                    f'Invalid value from "teradata__list_relations_without_caching({kwargs})", '
-                    f'got {len(row)} values, expected 4'
-                )
-            _, name, _schema, relation_type = row
-            relation = self.Relation.create(
-                schema=_schema,
-                identifier=name,
-                type=relation_type
-            )
-            relations.append(relation)
-
-        return relations
-
-    def get_relation(
-        self, database: str, schema: str, identifier: str
-    ) -> Optional[BaseRelation]:
-        if not self.Relation.include_policy.database:
-            database = None
-
-        return super().get_relation(database, schema, identifier)
-
-    def get_catalog(self, manifest):
-        schema_map = self._get_catalog_schemas(manifest)
-        with executor(self.config) as tpe:
-            futures: List[Future[agate.Table]] = []
-            for info, schemas in schema_map.items():
-                for schema in schemas:
-                    futures.append(tpe.submit_connected(
-                        self, schema,
-                        self._get_one_catalog, info, [schema], manifest
-                    ))
-            catalogs, exceptions = catch_as_completed(futures)
-        return catalogs, exceptions
-
-    def _get_one_catalog(
-        self,
-        information_schema: InformationSchema,
-        schemas: Set[str],
-        manifest: Manifest,
-    ) -> agate.Table:
-        if len(schemas) != 1:
-            dbt.exceptions.raise_compiler_error(
-                f'Expected only one schema in _get_one_catalog() for Teradata adapter, found '
-                f'{schemas}'
-            )
-
-        return super()._get_one_catalog(information_schema, schemas, manifest)
-
-    @classmethod
-    def _catalog_filter_table(cls, table: agate.Table, manifest: Manifest) -> agate.Table:
-        table = table_from_rows(
-            table.rows,
-            table.column_names,
-            text_only_columns=['table_schema', 'table_name'],
-        )
-        return table.where(_catalog_filter_schemas(manifest))
-
-    def check_schema_exists(self, database, schema):
-        results = self.execute_macro(
-            LIST_SCHEMAS_MACRO_NAME,
-            kwargs={'database': database}
-        )
-
-        exists = True if schema in [row[0] for row in results] else False
-        return exists
-
-    # Methods used in adapter tests
-    def update_column_sql(
-        self,
-        dst_name: str,
-        dst_column: str,
-        clause: str,
-        where_clause: Optional[str] = None,
-    ) -> str:
-        clause = f'update {dst_name} set {dst_column} = {clause}'
-        if where_clause is not None:
-            clause += f' where {where_clause}'
-        return clause
-
-    def timestamp_add_sql(
-        self, add_to: str, number: int = 1, interval: str = 'hour'
-    ) -> str:
-        # for backwards compatibility, we're compelled to set some sort of
-        # default. A lot of searching has lead me to believe that the
-        # '+ interval' syntax used in postgres/redshift is relatively common
-        # and might even be the SQL standard's intention.
-        return f"{add_to} + interval '{number}' {interval}"
-
-    def string_add_sql(
-        self, add_to: str, value: str, location='append',
-    ) -> str:
-        if location == 'append':
-            return f"concat(cast(trim({add_to}) as varchar(63800)), '{value}')"
-        elif location == 'prepend':
-            return f"concat('{value}', cast(trim({add_to}) as varchar(63800))"
-        else:
-            raise RuntimeException(
-                f'Got an unexpected location value of "{location}"'
-            )
-
-    def get_rows_different_sql(
-        self,
-        relation_a: TeradataRelation,
-        relation_b: TeradataRelation,
-        column_names: Optional[List[str]] = None,
-    ) -> str:
-        # This method only really exists for test reasons
-        names: List[str]
-        if column_names is None:
-            columns = self.get_columns_in_relation(relation_a)
-            names = sorted((self.quote(c.name) for c in columns))
-        else:
-            names = sorted((self.quote(n) for n in column_names))
-
-        alias_a = "A"
-        alias_b = "B"
-        columns_csv_a = ', '.join([f"{alias_a}.{name}" for name in names])
-        columns_csv_b = ', '.join([f"{alias_b}.{name}" for name in names])
-        join_condition = ' AND '.join([f"{alias_a}.{name} = {alias_b}.{name}" for name in names])
-        first_column = names[0]
-
-        # Simulate an EXCEPT or MINUS operator
-        COLUMNS_EQUAL_SQL = '''
-        WITH
-        a_except_b as (
-            SELECT
-                {columns_a}
-            FROM {relation_a} as {alias_a}
-            LEFT OUTER JOIN {relation_b} as {alias_b}
-                ON {join_condition}
-            WHERE {alias_b}.{first_column} is null
-        ),
-        b_except_a as (
-            SELECT
-                {columns_b}
-            FROM {relation_b} as {alias_b}
-            LEFT OUTER JOIN {relation_a} as {alias_a}
-                ON {join_condition}
-            WHERE {alias_a}.{first_column} is null
-        ),
-        diff_count as (
-            SELECT
-                1 as id,
-                COUNT(*) as num_missing FROM (
-                    SELECT * FROM a_except_b
-                    UNION ALL
-                    SELECT * FROM b_except_a
-                ) as missing
-        ),
-        table_a as (
-            SELECT COUNT(*) as num_rows FROM {relation_a}
-        ),
-        table_b as (
-            SELECT COUNT(*) as num_rows FROM {relation_b}
-        ),
-        row_count_diff as (
-            SELECT
-                1 as id,
-                table_a.num_rows - table_b.num_rows as difference
-            FROM table_a, table_b
-        )
-        SELECT
-            row_count_diff.difference as row_count_difference,
-            diff_count.num_missing as num_mismatched
-        FROM row_count_diff
-        INNER JOIN diff_count ON row_count_diff.id = diff_count.id
-        '''.strip()
-
-        sql = COLUMNS_EQUAL_SQL.format(
-            alias_a=alias_a,
-            alias_b=alias_b,
-            first_column=first_column,
-            columns_a=columns_csv_a,
-            columns_b=columns_csv_b,
-            join_condition=join_condition,
-            relation_a=str(relation_a),
-            relation_b=str(relation_b),
-        )
-
-        return sql
-
-    
-    @available
-    def standardize_grants_dict(self, grants_table: agate.Table) -> dict:
-        """overridden this method as there were extra spaces that needed
-         to be stripped
-        """
-        grants_dict: Dict[str, List[str]] = {}
-        for row in grants_table:
-            grantee = row["grantee"].strip()
-            privilege = row["privilege_type"].strip()
-            if privilege in grants_dict.keys():
-                grants_dict[privilege].append(grantee)
-            else:
-                grants_dict.update({privilege: [grantee]})
-        return grants_dict
-    
+from concurrent.futures import Future
+from dataclasses import dataclass, asdict
+from typing import Optional, List, Dict, Any, Union, Iterable, Callable, Set
+import agate
+
+import dbt
+import dbt.exceptions
+
+from dbt.adapters.base.impl import catch_as_completed
+from dbt.adapters.base.relation import InformationSchema
+from dbt.adapters.sql import SQLAdapter
+from dbt.adapters.teradata import TeradataConnectionManager
+from dbt.adapters.teradata import TeradataRelation
+from dbt.adapters.teradata import TeradataColumn
+from dbt.adapters.base.meta import available
+from dbt.adapters.base import BaseRelation
+from dbt.clients.agate_helper import DEFAULT_TYPE_TESTER, table_from_rows
+from dbt.contracts.graph.manifest import Manifest
+from dbt.events import AdapterLogger
+logger = AdapterLogger("teradata")
+from dbt.utils import executor
+
+LIST_SCHEMAS_MACRO_NAME = 'list_schemas'
+LIST_RELATIONS_MACRO_NAME = 'list_relations_without_caching'
+GET_CATALOG_MACRO_NAME = 'get_catalog'
+
+def _expect_row_value(key: str, row: agate.Row):
+    if key not in row.keys():
+        raise dbt.exceptions.InternalException(
+            f'Got a row without \'{key}\' column, columns: {row.keys()}'
+        )
+
+    return row[key]
+
+def _catalog_filter_schemas(manifest: Manifest) -> Callable[[agate.Row], bool]:
+    schemas = frozenset((None, s.lower()) for d, s in manifest.get_used_schemas())
+
+    def test(row: agate.Row) -> bool:
+        table_database = _expect_row_value('table_database', row)
+        table_schema = _expect_row_value('table_schema', row)
+        if table_schema is None:
+            return False
+        return (table_database, table_schema.lower()) in schemas
+
+    return test
+
+
+class TeradataAdapter(SQLAdapter):
+    Relation = TeradataRelation
+    Column = TeradataColumn
+    ConnectionManager = TeradataConnectionManager
+
+    @classmethod
+    def date_function(cls):
+        return 'current_date()'
+
+    @available
+    def verify_database(self, database):
+        if database.startswith('"'):
+            database = database.strip('"')
+        expected = self.config.credentials.schema
+        if database.lower() != expected.lower():
+            raise dbt.exceptions.NotImplementedException(
+                'Cross-db references not allowed in {} ({} vs {})'
+                .format(self.type(), database, expected)
+            )
+        # return an empty string on success so macros can call this
+        return ''
+
+    @classmethod
+    def convert_text_type(cls, agate_table: agate.Table, col_idx: int) -> str:
+        return "LONG VARCHAR"
+
+    @classmethod
+    def convert_datetime_type(cls, agate_table: agate.Table, col_idx: int) -> str:
+        return "TIMESTAMP(0)"
+
+    @classmethod
+    def convert_time_type(cls, agate_table: agate.Table, col_idx: int) -> str:
+        return "TIME"
+
+    @classmethod
+    def convert_date_type(cls, agate_table: agate.Table, col_idx: int) -> str:
+        return "DATE"
+
+    @classmethod
+    def convert_boolean_type(cls, agate_table: agate.Table, col_idx: int) -> str:
+        return "BYTEINT"
+
+    @classmethod
+    def convert_number_type(
+        cls, agate_table: agate.Table, col_idx: int
+    ) -> str:
+        decimals = agate_table.aggregate(agate.MaxPrecision(col_idx))
+        return "FLOAT" if decimals else "INTEGER"
+
+    def quote(self, identifier):
+        return '"{}"'.format(identifier)
+
+    def list_relations_without_caching(
+        self, schema_relation: TeradataRelation
+    ) -> List[TeradataRelation]:
+        kwargs = {'schema_relation': schema_relation}
+        try:
+            results = self.execute_macro(
+                LIST_RELATIONS_MACRO_NAME,
+                kwargs=kwargs
+            )
+        except dbt.exceptions.RuntimeException as e:
+            errmsg = getattr(e, 'msg', '')
+            if f"Teradata database '{schema_relation}' not found" in errmsg:
+                return []
+            else:
+                description = "Error while retrieving information about"
+                logger.debug(f"{description} {schema_relation}: {e.msg}")
+                return []
+
+        relations = []
+        for row in results:
+            if len(row) != 4:
+                raise dbt.exceptions.RuntimeException(
+                    f'Invalid value from "teradata__list_relations_without_caching({kwargs})", '
+                    f'got {len(row)} values, expected 4'
+                )
+            _, name, _schema, relation_type = row
+            relation = self.Relation.create(
+                schema=_schema,
+                identifier=name,
+                type=relation_type
+            )
+            relations.append(relation)
+
+        return relations
+
+    def get_relation(
+        self, database: str, schema: str, identifier: str
+    ) -> Optional[BaseRelation]:
+        if not self.Relation.include_policy.database:
+            database = None
+
+        return super().get_relation(database, schema, identifier)
+
+    def get_catalog(self, manifest):
+        schema_map = self._get_catalog_schemas(manifest)
+        with executor(self.config) as tpe:
+            futures: List[Future[agate.Table]] = []
+            for info, schemas in schema_map.items():
+                for schema in schemas:
+                    futures.append(tpe.submit_connected(
+                        self, schema,
+                        self._get_one_catalog, info, [schema], manifest
+                    ))
+            catalogs, exceptions = catch_as_completed(futures)
+        return catalogs, exceptions
+
+    def _get_one_catalog(
+        self,
+        information_schema: InformationSchema,
+        schemas: Set[str],
+        manifest: Manifest,
+    ) -> agate.Table:
+        if len(schemas) != 1:
+            dbt.exceptions.raise_compiler_error(
+                f'Expected only one schema in _get_one_catalog() for Teradata adapter, found '
+                f'{schemas}'
+            )
+
+        return super()._get_one_catalog(information_schema, schemas, manifest)
+
+    @classmethod
+    def _catalog_filter_table(cls, table: agate.Table, manifest: Manifest) -> agate.Table:
+        table = table_from_rows(
+            table.rows,
+            table.column_names,
+            text_only_columns=['table_schema', 'table_name'],
+        )
+        return table.where(_catalog_filter_schemas(manifest))
+
+    def check_schema_exists(self, database, schema):
+        results = self.execute_macro(
+            LIST_SCHEMAS_MACRO_NAME,
+            kwargs={'database': database}
+        )
+
+        exists = True if schema in [row[0] for row in results] else False
+        return exists
+
+    # Methods used in adapter tests
+    def update_column_sql(
+        self,
+        dst_name: str,
+        dst_column: str,
+        clause: str,
+        where_clause: Optional[str] = None,
+    ) -> str:
+        clause = f'update {dst_name} set {dst_column} = {clause}'
+        if where_clause is not None:
+            clause += f' where {where_clause}'
+        return clause
+
+    def timestamp_add_sql(
+        self, add_to: str, number: int = 1, interval: str = 'hour'
+    ) -> str:
+        # for backwards compatibility, we're compelled to set some sort of
+        # default. A lot of searching has lead me to believe that the
+        # '+ interval' syntax used in postgres/redshift is relatively common
+        # and might even be the SQL standard's intention.
+        return f"{add_to} + interval '{number}' {interval}"
+
+    def string_add_sql(
+        self, add_to: str, value: str, location='append',
+    ) -> str:
+        if location == 'append':
+            return f"concat(cast(trim({add_to}) as varchar(63800)), '{value}')"
+        elif location == 'prepend':
+            return f"concat('{value}', cast(trim({add_to}) as varchar(63800))"
+        else:
+            raise RuntimeException(
+                f'Got an unexpected location value of "{location}"'
+            )
+
+    def get_rows_different_sql(
+        self,
+        relation_a: TeradataRelation,
+        relation_b: TeradataRelation,
+        column_names: Optional[List[str]] = None,
+    ) -> str:
+        # This method only really exists for test reasons
+        names: List[str]
+        if column_names is None:
+            columns = self.get_columns_in_relation(relation_a)
+            names = sorted((self.quote(c.name) for c in columns))
+        else:
+            names = sorted((self.quote(n) for n in column_names))
+
+        alias_a = "A"
+        alias_b = "B"
+        columns_csv_a = ', '.join([f"{alias_a}.{name}" for name in names])
+        columns_csv_b = ', '.join([f"{alias_b}.{name}" for name in names])
+        join_condition = ' AND '.join([f"{alias_a}.{name} = {alias_b}.{name}" for name in names])
+        first_column = names[0]
+
+        # Simulate an EXCEPT or MINUS operator
+        COLUMNS_EQUAL_SQL = '''
+        WITH
+        a_except_b as (
+            SELECT
+                {columns_a}
+            FROM {relation_a} as {alias_a}
+            LEFT OUTER JOIN {relation_b} as {alias_b}
+                ON {join_condition}
+            WHERE {alias_b}.{first_column} is null
+        ),
+        b_except_a as (
+            SELECT
+                {columns_b}
+            FROM {relation_b} as {alias_b}
+            LEFT OUTER JOIN {relation_a} as {alias_a}
+                ON {join_condition}
+            WHERE {alias_a}.{first_column} is null
+        ),
+        diff_count as (
+            SELECT
+                1 as id,
+                COUNT(*) as num_missing FROM (
+                    SELECT * FROM a_except_b
+                    UNION ALL
+                    SELECT * FROM b_except_a
+                ) as missing
+        ),
+        table_a as (
+            SELECT COUNT(*) as num_rows FROM {relation_a}
+        ),
+        table_b as (
+            SELECT COUNT(*) as num_rows FROM {relation_b}
+        ),
+        row_count_diff as (
+            SELECT
+                1 as id,
+                table_a.num_rows - table_b.num_rows as difference
+            FROM table_a, table_b
+        )
+        SELECT
+            row_count_diff.difference as row_count_difference,
+            diff_count.num_missing as num_mismatched
+        FROM row_count_diff
+        INNER JOIN diff_count ON row_count_diff.id = diff_count.id
+        '''.strip()
+
+        sql = COLUMNS_EQUAL_SQL.format(
+            alias_a=alias_a,
+            alias_b=alias_b,
+            first_column=first_column,
+            columns_a=columns_csv_a,
+            columns_b=columns_csv_b,
+            join_condition=join_condition,
+            relation_a=str(relation_a),
+            relation_b=str(relation_b),
+        )
+
+        return sql
+
+    
+    @available
+    def standardize_grants_dict(self, grants_table: agate.Table) -> dict:
+        """overridden this method as there were extra spaces that needed
+         to be stripped
+        """
+        grants_dict: Dict[str, List[str]] = {}
+        for row in grants_table:
+            grantee = row["grantee"].strip()
+            privilege = row["privilege_type"].strip()
+            if privilege in grants_dict.keys():
+                grants_dict[privilege].append(grantee)
+            else:
+                grants_dict.update({privilege: [grantee]})
+        return grants_dict
+    
+    def valid_incremental_strategies(self):
+        """The set of standard builtin strategies which this adapter supports out-of-the-box.
+        Not used to validate custom strategies defined by end users.
+        """
+        return ["delete+insert","append"]
```

### Comparing `dbt-teradata-1.2.0.0/dbt/adapters/teradata/relation.py` & `dbt-teradata-1.3.0.0/dbt/adapters/teradata/relation.py`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/include/teradata/macros/adapters.sql` & `dbt-teradata-1.3.0.0/dbt/include/teradata/macros/adapters.sql`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/include/teradata/macros/apply_grants.sql` & `dbt-teradata-1.3.0.0/dbt/include/teradata/macros/apply_grants.sql`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/include/teradata/macros/catalog.sql` & `dbt-teradata-1.3.0.0/dbt/include/teradata/macros/catalog.sql`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/incremental/incremental.sql` & `dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/incremental/incremental.sql`

 * *Files 20% similar despite different names*

```diff
@@ -1,65 +1,78 @@
-
-
-{% materialization incremental, adapter='teradata' -%}
-
-{% set unique_key = config.get('unique_key') %}
-
-{% set target_relation = this.incorporate(type='table') %}
-{% set existing_relation = load_relation(this) %}
-{% set tmp_relation = make_temp_relation(this) %}
-
-{% set on_schema_change = incremental_validate_on_schema_change(config.get('on_schema_change'), default='ignore') %}
-
-{{ run_hooks(pre_hooks, inside_transaction=False) }}
-
--- `BEGIN` happens here:
-{{ run_hooks(pre_hooks, inside_transaction=True) }}
-
-{% set to_drop = [] %}
-{% if existing_relation is none %}
-   {% set build_sql = create_table_as(False, target_relation, sql) %}
-{% elif existing_relation.is_view or should_full_refresh() %}
-   {#-- Make sure the backup doesn't exist so we don't encounter issues with the rename below #}
-   {% set backup_identifier = existing_relation.identifier ~ "__dbt_backup" %}
-   {% set backup_relation = existing_relation.incorporate(path={"identifier": backup_identifier}) %}
-   {% do adapter.drop_relation(backup_relation) %}
-
-   {% do adapter.rename_relation(target_relation, backup_relation) %}
-   {% set build_sql = create_table_as(False, target_relation, sql) %}
-   {% do to_drop.append(backup_relation) %}
-{% else %}
-   {% set tmp_relation = make_temp_relation(target_relation) %}
-   {% do run_query(create_table_as(True, tmp_relation, sql)) %}
-   {% do adapter.expand_target_column_types(
-          from_relation=tmp_relation,
-          to_relation=target_relation) %}
-   {% set build_sql = incremental_upsert(on_schema_change, tmp_relation, target_relation, existing_relation, unique_key=unique_key) %}
-   {% do to_drop.append(tmp_relation) %}
-{% endif %}
-
-{% call statement("main") %}
-   {{ build_sql }}
-{% endcall %}
-
--- apply grants
-{%- set grant_config = config.get('grants') -%}
-{% set should_revoke = should_revoke(existing_relation, full_refresh_mode) %}
-{% do apply_grants(target_relation, grant_config, should_revoke) %}
-
-{% do persist_docs(target_relation, model) %}
-
-{{ run_hooks(post_hooks, inside_transaction=True) }}
-
-
--- `COMMIT` happens here
-{% do adapter.commit() %}
-
-{% for rel in to_drop %}
-   {% do adapter.drop_relation(rel) %}
-{% endfor %}
-
-{{ run_hooks(post_hooks, inside_transaction=False) }}
-
-{{ return({'relations': [target_relation]}) }}
-
-{%- endmaterialization %}
+
+
+{% materialization incremental, adapter='teradata' -%}
+
+{% set unique_key = config.get('unique_key') %}
+
+{% set target_relation = this.incorporate(type='table') %}
+{% set existing_relation = load_relation(this) %}
+{% set tmp_relation = make_temp_relation(this) %}
+
+-- {#-- Validate early so we don't run SQL if the strategy is invalid --#}
+{% set strategy = teradata__validate_get_incremental_strategy(config) %}
+
+{% set on_schema_change = incremental_validate_on_schema_change(config.get('on_schema_change'), default='ignore') %}
+
+{{ run_hooks(pre_hooks, inside_transaction=False) }}
+
+-- `BEGIN` happens here:
+{{ run_hooks(pre_hooks, inside_transaction=True) }}
+
+{% set to_drop = [] %}
+{% if existing_relation is none %}
+   {% set build_sql = create_table_as(False, target_relation, sql) %}
+{% elif existing_relation.is_view or should_full_refresh() %}
+   {#-- Make sure the backup doesn't exist so we don't encounter issues with the rename below #}
+   {% set backup_identifier = existing_relation.identifier ~ "__dbt_backup" %}
+   {% set backup_relation = existing_relation.incorporate(path={"identifier": backup_identifier}) %}
+   {% do adapter.drop_relation(backup_relation) %}
+
+   {% do adapter.rename_relation(target_relation, backup_relation) %}
+   {% set build_sql = create_table_as(False, target_relation, sql) %}
+   {% do to_drop.append(backup_relation) %}
+{% else %}
+   {% set tmp_relation = make_temp_relation(target_relation) %}
+   {% do run_query(create_table_as(True, tmp_relation, sql)) %}
+   {% do adapter.expand_target_column_types(
+          from_relation=tmp_relation,
+          to_relation=target_relation) %}
+   
+
+   {% set dest_columns = process_schema_changes(on_schema_change, tmp_relation, existing_relation) %}
+    {% if not dest_columns %}
+        {%- set dest_columns = adapter.get_columns_in_relation(target_relation) -%}
+    {% endif %}
+	
+	
+   {% set build_sql = teradata__get_incremental_sql(strategy, target_relation, tmp_relation, unique_key, dest_columns) %}
+
+
+   {% do to_drop.append(tmp_relation) %}
+{% endif %}
+
+{% call statement("main") %}
+   {{ build_sql }}
+{% endcall %}
+
+-- apply grants
+{%- set grant_config = config.get('grants') -%}
+{% set should_revoke = should_revoke(existing_relation, full_refresh_mode) %}
+{% do apply_grants(target_relation, grant_config, should_revoke) %}
+
+{% do persist_docs(target_relation, model) %}
+
+{{ run_hooks(post_hooks, inside_transaction=True) }}
+
+
+-- `COMMIT` happens here
+{% do adapter.commit() %}
+
+{% for rel in to_drop %}
+   {% do adapter.drop_relation(rel) %}
+{% endfor %}
+
+{{ run_hooks(post_hooks, inside_transaction=False) }}
+
+{{ return({'relations': [target_relation]}) }}
+
+{%- endmaterialization %}
```

### Comparing `dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/seed/seed.sql` & `dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/seed/seed.sql`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/snapshot/snapshot.sql` & `dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/snapshot/snapshot.sql`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/snapshot/snapshot_merge.sql` & `dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/snapshot/snapshot_merge.sql`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt/include/teradata/macros/materializations/test/test.sql` & `dbt-teradata-1.3.0.0/dbt/include/teradata/macros/materializations/test/test.sql`

 * *Files identical despite different names*

### Comparing `dbt-teradata-1.2.0.0/dbt_teradata.egg-info/SOURCES.txt` & `dbt-teradata-1.3.0.0/dbt_teradata.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -11,14 +11,15 @@
 dbt/include/teradata/dbt_project.yml
 dbt/include/teradata/sample_profiles.yml
 dbt/include/teradata/macros/adapters.sql
 dbt/include/teradata/macros/apply_grants.sql
 dbt/include/teradata/macros/catalog.sql
 dbt/include/teradata/macros/materializations/incremental/helpers.sql
 dbt/include/teradata/macros/materializations/incremental/incremental.sql
+dbt/include/teradata/macros/materializations/incremental/strategies.sql
 dbt/include/teradata/macros/materializations/seed/seed.sql
 dbt/include/teradata/macros/materializations/snapshot/snapshot.sql
 dbt/include/teradata/macros/materializations/snapshot/snapshot_merge.sql
 dbt/include/teradata/macros/materializations/snapshot/strategies.sql
 dbt/include/teradata/macros/materializations/test/test.sql
 dbt_teradata.egg-info/PKG-INFO
 dbt_teradata.egg-info/SOURCES.txt
```

