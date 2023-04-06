# Comparing `tmp/django-postgres-extra-2.0a7.tar.gz` & `tmp/django-postgres-extra-2.0a9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/django-postgres-extra-2.0a7.tar", last modified: Mon Oct  7 08:08:55 2019, max compression
+gzip compressed data, was "dist/django-postgres-extra-2.0a9.tar", last modified: Sun Nov 10 20:55:43 2019, max compression
```

## Comparing `django-postgres-extra-2.0a7.tar` & `django-postgres-extra-2.0a9.tar`

### file list

```diff
@@ -1,104 +1,137 @@
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/
--rw-r--r--   0 swen       (501) staff       (20)     5706 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/PKG-INFO
--rw-r--r--   0 swen       (501) staff       (20)     4234 2019-10-05 17:54:51.000000 django-postgres-extra-2.0a7/README.md
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/django_postgres_extra.egg-info/
--rw-r--r--   0 swen       (501) staff       (20)     5706 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/django_postgres_extra.egg-info/PKG-INFO
--rw-r--r--   0 swen       (501) staff       (20)     3096 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/django_postgres_extra.egg-info/SOURCES.txt
--rw-r--r--   0 swen       (501) staff       (20)        1 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/django_postgres_extra.egg-info/dependency_links.txt
--rw-r--r--   0 swen       (501) staff       (20)       16 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/django_postgres_extra.egg-info/top_level.txt
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/
--rw-r--r--   0 swen       (501) staff       (20)       61 2019-05-23 06:25:50.000000 django-postgres-extra-2.0a7/psqlextra/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)      138 2019-05-23 06:25:50.000000 django-postgres-extra-2.0a7/psqlextra/apps.py
--rw-r--r--   0 swen       (501) staff       (20)     5102 2019-09-19 19:40:07.000000 django-postgres-extra-2.0a7/psqlextra/auto_partition.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/backend/
--rw-r--r--   0 swen       (501) staff       (20)        0 2019-04-18 14:00:50.000000 django-postgres-extra-2.0a7/psqlextra/backend/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)     1602 2019-09-14 15:50:48.000000 django-postgres-extra-2.0a7/psqlextra/backend/base.py
--rw-r--r--   0 swen       (501) staff       (20)     2280 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/psqlextra/backend/base_impl.py
--rw-r--r--   0 swen       (501) staff       (20)     4095 2019-09-16 12:13:15.000000 django-postgres-extra-2.0a7/psqlextra/backend/introspection.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/
--rw-r--r--   0 swen       (501) staff       (20)      103 2019-09-15 09:55:04.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/__init__.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/
--rw-r--r--   0 swen       (501) staff       (20)      814 2019-09-14 17:16:10.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)     1366 2019-09-15 09:02:47.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/add_default_partition.py
--rw-r--r--   0 swen       (501) staff       (20)     1745 2019-09-15 09:03:01.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/add_list_partition.py
--rw-r--r--   0 swen       (501) staff       (20)     2187 2019-09-15 09:02:54.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/add_range_partition.py
--rw-r--r--   0 swen       (501) staff       (20)     2293 2019-09-16 16:41:16.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/create_partitioned_model.py
--rw-r--r--   0 swen       (501) staff       (20)      825 2019-09-15 09:06:02.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_default_partition.py
--rw-r--r--   0 swen       (501) staff       (20)      867 2019-09-15 09:20:10.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_list_partition.py
--rw-r--r--   0 swen       (501) staff       (20)     1254 2019-09-15 09:03:12.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_partition.py
--rw-r--r--   0 swen       (501) staff       (20)     1087 2019-09-14 22:05:35.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_partitioned_model.py
--rw-r--r--   0 swen       (501) staff       (20)      952 2019-09-15 09:20:10.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_range_partition.py
--rw-r--r--   0 swen       (501) staff       (20)      820 2019-09-15 08:57:33.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/partition.py
--rw-r--r--   0 swen       (501) staff       (20)     3592 2019-09-15 08:57:17.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/patched_autodetector.py
--rw-r--r--   0 swen       (501) staff       (20)      504 2019-09-15 09:55:15.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/patched_migrations.py
--rw-r--r--   0 swen       (501) staff       (20)     1715 2019-09-15 08:16:14.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/patched_project_state.py
--rw-r--r--   0 swen       (501) staff       (20)     5227 2019-09-15 08:16:14.000000 django-postgres-extra-2.0a7/psqlextra/backend/migrations/state.py
--rw-r--r--   0 swen       (501) staff       (20)      786 2019-09-15 19:28:53.000000 django-postgres-extra-2.0a7/psqlextra/backend/operations.py
--rw-r--r--   0 swen       (501) staff       (20)    10388 2019-09-16 11:47:08.000000 django-postgres-extra-2.0a7/psqlextra/backend/schema.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/backend/side_effects/
--rw-r--r--   0 swen       (501) staff       (20)      229 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/psqlextra/backend/side_effects/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)     5842 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/psqlextra/backend/side_effects/hstore_required.py
--rw-r--r--   0 swen       (501) staff       (20)     6027 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/psqlextra/backend/side_effects/hstore_unique.py
--rw-r--r--   0 swen       (501) staff       (20)    11192 2019-10-07 08:08:09.000000 django-postgres-extra-2.0a7/psqlextra/compiler.py
--rw-r--r--   0 swen       (501) staff       (20)     2228 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/psqlextra/datastructures.py
--rw-r--r--   0 swen       (501) staff       (20)     6471 2019-10-06 17:48:02.000000 django-postgres-extra-2.0a7/psqlextra/expressions.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/fields/
--rw-r--r--   0 swen       (501) staff       (20)       65 2019-05-23 06:25:50.000000 django-postgres-extra-2.0a7/psqlextra/fields/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)     2026 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/psqlextra/fields/hstore_field.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/indexes/
--rw-r--r--   0 swen       (501) staff       (20)      199 2019-10-05 16:38:39.000000 django-postgres-extra-2.0a7/psqlextra/indexes/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)     1362 2019-10-06 06:25:34.000000 django-postgres-extra-2.0a7/psqlextra/indexes/case_insensitive_unique_index.py
--rw-r--r--   0 swen       (501) staff       (20)     2104 2019-10-05 15:42:12.000000 django-postgres-extra-2.0a7/psqlextra/indexes/conditional_unique_index.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/management/
--rw-r--r--   0 swen       (501) staff       (20)        0 2019-09-14 18:32:33.000000 django-postgres-extra-2.0a7/psqlextra/management/__init__.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/management/commands/
--rw-r--r--   0 swen       (501) staff       (20)        0 2019-09-14 18:32:42.000000 django-postgres-extra-2.0a7/psqlextra/management/commands/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)     2375 2019-09-16 14:36:30.000000 django-postgres-extra-2.0a7/psqlextra/management/commands/pgautopartition.py
--rw-r--r--   0 swen       (501) staff       (20)      387 2019-09-16 09:53:47.000000 django-postgres-extra-2.0a7/psqlextra/management/commands/pgmakemigrations.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/manager/
--rw-r--r--   0 swen       (501) staff       (20)      261 2019-09-15 19:28:58.000000 django-postgres-extra-2.0a7/psqlextra/manager/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)     1920 2019-10-05 17:55:44.000000 django-postgres-extra-2.0a7/psqlextra/manager/manager.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/psqlextra/models/
--rw-r--r--   0 swen       (501) staff       (20)      139 2019-09-16 13:24:34.000000 django-postgres-extra-2.0a7/psqlextra/models/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)      304 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/psqlextra/models/base.py
--rw-r--r--   0 swen       (501) staff       (20)      464 2019-09-15 09:14:59.000000 django-postgres-extra-2.0a7/psqlextra/models/options.py
--rw-r--r--   0 swen       (501) staff       (20)     1374 2019-09-15 09:50:23.000000 django-postgres-extra-2.0a7/psqlextra/models/partitioned.py
--rw-r--r--   0 swen       (501) staff       (20)    17502 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/psqlextra/query.py
--rw-r--r--   0 swen       (501) staff       (20)      153 2019-05-23 06:25:50.000000 django-postgres-extra-2.0a7/psqlextra/signals.py
--rw-r--r--   0 swen       (501) staff       (20)     6369 2019-10-06 16:20:51.000000 django-postgres-extra-2.0a7/psqlextra/sql.py
--rw-r--r--   0 swen       (501) staff       (20)      772 2019-09-16 11:34:10.000000 django-postgres-extra-2.0a7/psqlextra/types.py
--rw-r--r--   0 swen       (501) staff       (20)      396 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/psqlextra/util.py
--rw-r--r--   0 swen       (501) staff       (20)      422 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/setup.cfg
--rw-r--r--   0 swen       (501) staff       (20)     4263 2019-10-07 08:08:30.000000 django-postgres-extra-2.0a7/setup.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/tests/
--rw-r--r--   0 swen       (501) staff       (20)        0 2019-04-18 14:00:50.000000 django-postgres-extra-2.0a7/tests/__init__.py
-drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-10-07 08:08:55.000000 django-postgres-extra-2.0a7/tests/benchmarks/
--rw-r--r--   0 swen       (501) staff       (20)        0 2019-04-18 14:00:50.000000 django-postgres-extra-2.0a7/tests/benchmarks/__init__.py
--rw-r--r--   0 swen       (501) staff       (20)     1446 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/benchmarks/test_insert_nothing.py
--rw-r--r--   0 swen       (501) staff       (20)     1410 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/benchmarks/test_upsert.py
--rw-r--r--   0 swen       (501) staff       (20)     1763 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/benchmarks/test_upsert_bulk.py
--rw-r--r--   0 swen       (501) staff       (20)      523 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/conftest.py
--rw-r--r--   0 swen       (501) staff       (20)     1962 2019-10-05 16:36:42.000000 django-postgres-extra-2.0a7/tests/fake_model.py
--rw-r--r--   0 swen       (501) staff       (20)     7404 2019-09-16 12:00:00.000000 django-postgres-extra-2.0a7/tests/migrations.py
--rw-r--r--   0 swen       (501) staff       (20)    10149 2019-09-19 19:40:07.000000 django-postgres-extra-2.0a7/tests/test_auto_partition.py
--rw-r--r--   0 swen       (501) staff       (20)     2093 2019-10-06 14:40:30.000000 django-postgres-extra-2.0a7/tests/test_case_insensitive_unique_index.py
--rw-r--r--   0 swen       (501) staff       (20)     4739 2019-10-05 16:48:26.000000 django-postgres-extra-2.0a7/tests/test_conditional_unique_index.py
--rw-r--r--   0 swen       (501) staff       (20)      352 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_db_backend.py
--rw-r--r--   0 swen       (501) staff       (20)     2644 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_hstore_autodetect.py
--rw-r--r--   0 swen       (501) staff       (20)      995 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_hstore_field.py
--rw-r--r--   0 swen       (501) staff       (20)     4304 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_hstore_required.py
--rw-r--r--   0 swen       (501) staff       (20)     5704 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_hstore_unique.py
--rw-r--r--   0 swen       (501) staff       (20)     3799 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_insert.py
--rw-r--r--   0 swen       (501) staff       (20)     1907 2019-09-16 08:09:04.000000 django-postgres-extra-2.0a7/tests/test_make_migrations.py
--rw-r--r--   0 swen       (501) staff       (20)     1852 2019-10-06 13:56:30.000000 django-postgres-extra-2.0a7/tests/test_manager.py
--rw-r--r--   0 swen       (501) staff       (20)      639 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_manager_context.py
--rw-r--r--   0 swen       (501) staff       (20)     6363 2019-09-14 18:49:14.000000 django-postgres-extra-2.0a7/tests/test_migration_operations.py
--rw-r--r--   0 swen       (501) staff       (20)    12213 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_on_conflict.py
--rw-r--r--   0 swen       (501) staff       (20)     5435 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_on_conflict_nothing.py
--rw-r--r--   0 swen       (501) staff       (20)     3914 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_on_conflict_update.py
--rw-r--r--   0 swen       (501) staff       (20)     2214 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_partitioned_model.py
--rw-r--r--   0 swen       (501) staff       (20)     3434 2019-09-14 18:49:14.000000 django-postgres-extra-2.0a7/tests/test_partitioned_model_state.py
--rw-r--r--   0 swen       (501) staff       (20)     2442 2019-09-15 20:19:52.000000 django-postgres-extra-2.0a7/tests/test_query.py
--rw-r--r--   0 swen       (501) staff       (20)     2108 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_query_values.py
--rw-r--r--   0 swen       (501) staff       (20)     5908 2019-09-16 09:15:43.000000 django-postgres-extra-2.0a7/tests/test_schema_editor.py
--rw-r--r--   0 swen       (501) staff       (20)     5590 2019-09-14 15:12:17.000000 django-postgres-extra-2.0a7/tests/test_upsert.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/
+-rw-r--r--   0 swen       (501) staff       (20)     6017 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/PKG-INFO
+-rw-r--r--   0 swen       (501) staff       (20)     4463 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/README.md
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/django_postgres_extra.egg-info/
+-rw-r--r--   0 swen       (501) staff       (20)     6017 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/django_postgres_extra.egg-info/PKG-INFO
+-rw-r--r--   0 swen       (501) staff       (20)     4441 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/django_postgres_extra.egg-info/SOURCES.txt
+-rw-r--r--   0 swen       (501) staff       (20)        1 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/django_postgres_extra.egg-info/dependency_links.txt
+-rw-r--r--   0 swen       (501) staff       (20)      427 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/django_postgres_extra.egg-info/requires.txt
+-rw-r--r--   0 swen       (501) staff       (20)       16 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/django_postgres_extra.egg-info/top_level.txt
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/
+-rw-r--r--   0 swen       (501) staff       (20)       61 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)      138 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/apps.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/backend/
+-rw-r--r--   0 swen       (501) staff       (20)        0 2019-11-09 19:47:16.000000 django-postgres-extra-2.0a9/psqlextra/backend/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)     1602 2019-11-10 15:22:36.000000 django-postgres-extra-2.0a9/psqlextra/backend/base.py
+-rw-r--r--   0 swen       (501) staff       (20)     2280 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/base_impl.py
+-rw-r--r--   0 swen       (501) staff       (20)     5606 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/backend/introspection.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/
+-rw-r--r--   0 swen       (501) staff       (20)      103 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/__init__.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/
+-rw-r--r--   0 swen       (501) staff       (20)     1286 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)     1366 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/add_default_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     1745 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/add_list_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     2187 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/add_range_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     1264 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/apply_state.py
+-rw-r--r--   0 swen       (501) staff       (20)     2262 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/create_materialized_view_model.py
+-rw-r--r--   0 swen       (501) staff       (20)     2293 2019-10-21 15:12:54.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/create_partitioned_model.py
+-rw-r--r--   0 swen       (501) staff       (20)     2166 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/create_view_model.py
+-rw-r--r--   0 swen       (501) staff       (20)      825 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_default_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)      867 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_list_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     1116 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_materialized_view_model.py
+-rw-r--r--   0 swen       (501) staff       (20)     1254 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     1087 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_partitioned_model.py
+-rw-r--r--   0 swen       (501) staff       (20)      952 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_range_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     1052 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_view_model.py
+-rw-r--r--   0 swen       (501) staff       (20)      820 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     8734 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/patched_autodetector.py
+-rw-r--r--   0 swen       (501) staff       (20)      504 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/patched_migrations.py
+-rw-r--r--   0 swen       (501) staff       (20)     2167 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/patched_project_state.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/state/
+-rw-r--r--   0 swen       (501) staff       (20)      488 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/state/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)      501 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/state/materialized_view.py
+-rw-r--r--   0 swen       (501) staff       (20)     3518 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/state/model.py
+-rw-r--r--   0 swen       (501) staff       (20)     3691 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/state/partitioning.py
+-rw-r--r--   0 swen       (501) staff       (20)     1659 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/backend/migrations/state/view.py
+-rw-r--r--   0 swen       (501) staff       (20)      786 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/operations.py
+-rw-r--r--   0 swen       (501) staff       (20)    16597 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/backend/schema.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/backend/side_effects/
+-rw-r--r--   0 swen       (501) staff       (20)      229 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/side_effects/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)     5842 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/side_effects/hstore_required.py
+-rw-r--r--   0 swen       (501) staff       (20)     6027 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/backend/side_effects/hstore_unique.py
+-rw-r--r--   0 swen       (501) staff       (20)    11192 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/compiler.py
+-rw-r--r--   0 swen       (501) staff       (20)     5732 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/expressions.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/fields/
+-rw-r--r--   0 swen       (501) staff       (20)       65 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/fields/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)     2294 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/fields/hstore_field.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/indexes/
+-rw-r--r--   0 swen       (501) staff       (20)      199 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/indexes/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)     1372 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/indexes/case_insensitive_unique_index.py
+-rw-r--r--   0 swen       (501) staff       (20)     2115 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/indexes/conditional_unique_index.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/management/
+-rw-r--r--   0 swen       (501) staff       (20)        0 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/management/__init__.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/management/commands/
+-rw-r--r--   0 swen       (501) staff       (20)        0 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/management/commands/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)      387 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/management/commands/pgmakemigrations.py
+-rw-r--r--   0 swen       (501) staff       (20)     4187 2019-11-10 20:52:41.000000 django-postgres-extra-2.0a9/psqlextra/management/commands/pgpartition.py
+-rw-r--r--   0 swen       (501) staff       (20)     1556 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/management/commands/pgrefreshmv.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/manager/
+-rw-r--r--   0 swen       (501) staff       (20)      261 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/manager/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)     1920 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/manager/manager.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/models/
+-rw-r--r--   0 swen       (501) staff       (20)      279 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/models/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)      304 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/models/base.py
+-rw-r--r--   0 swen       (501) staff       (20)      978 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/models/options.py
+-rw-r--r--   0 swen       (501) staff       (20)     1374 2019-10-20 16:09:27.000000 django-postgres-extra-2.0a9/psqlextra/models/partitioned.py
+-rw-r--r--   0 swen       (501) staff       (20)     4455 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/models/view.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/
+-rw-r--r--   0 swen       (501) staff       (20)      244 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)      481 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/config.py
+-rw-r--r--   0 swen       (501) staff       (20)      209 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/error.py
+-rw-r--r--   0 swen       (501) staff       (20)     6920 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/manager.py
+-rw-r--r--   0 swen       (501) staff       (20)     1001 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     1272 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/range_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)      615 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/range_strategy.py
+-rw-r--r--   0 swen       (501) staff       (20)     2484 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/shorthands.py
+-rw-r--r--   0 swen       (501) staff       (20)      578 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/strategy.py
+-rw-r--r--   0 swen       (501) staff       (20)     1536 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/time_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     2922 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/time_partition_size.py
+-rw-r--r--   0 swen       (501) staff       (20)     3058 2019-11-10 20:32:09.000000 django-postgres-extra-2.0a9/psqlextra/partitioning/time_strategy.py
+-rw-r--r--   0 swen       (501) staff       (20)    17502 2019-10-19 12:37:22.000000 django-postgres-extra-2.0a9/psqlextra/query.py
+-rw-r--r--   0 swen       (501) staff       (20)     6284 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/sql.py
+-rw-r--r--   0 swen       (501) staff       (20)      766 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/type_assertions.py
+-rw-r--r--   0 swen       (501) staff       (20)      875 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/psqlextra/types.py
+-rw-r--r--   0 swen       (501) staff       (20)      396 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/psqlextra/util.py
+-rw-r--r--   0 swen       (501) staff       (20)      361 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/setup.cfg
+-rw-r--r--   0 swen       (501) staff       (20)     5417 2019-11-10 20:52:56.000000 django-postgres-extra-2.0a9/setup.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/tests/
+-rw-r--r--   0 swen       (501) staff       (20)        0 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/__init__.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/tests/benchmarks/
+-rw-r--r--   0 swen       (501) staff       (20)        0 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/benchmarks/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)     1446 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/benchmarks/test_insert_nothing.py
+-rw-r--r--   0 swen       (501) staff       (20)     1410 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/benchmarks/test_upsert.py
+-rw-r--r--   0 swen       (501) staff       (20)     1763 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/benchmarks/test_upsert_bulk.py
+-rw-r--r--   0 swen       (501) staff       (20)      737 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/conftest.py
+-rw-r--r--   0 swen       (501) staff       (20)     1321 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/db_introspection.py
+-rw-r--r--   0 swen       (501) staff       (20)     2989 2019-11-10 18:30:13.000000 django-postgres-extra-2.0a9/tests/fake_model.py
+-rw-r--r--   0 swen       (501) staff       (20)     7499 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/migrations.py
+drwxr-xr-x   0 swen       (501) staff       (20)        0 2019-11-10 20:55:43.000000 django-postgres-extra-2.0a9/tests/snapshots/
+-rw-r--r--   0 swen       (501) staff       (20)        0 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/tests/snapshots/__init__.py
+-rw-r--r--   0 swen       (501) staff       (20)     3101 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/tests/snapshots/snap_test_management_command_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     2093 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_case_insensitive_unique_index.py
+-rw-r--r--   0 swen       (501) staff       (20)     4739 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_conditional_unique_index.py
+-rw-r--r--   0 swen       (501) staff       (20)      352 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_db_backend.py
+-rw-r--r--   0 swen       (501) staff       (20)     2644 2019-10-19 12:37:45.000000 django-postgres-extra-2.0a9/tests/test_hstore_autodetect.py
+-rw-r--r--   0 swen       (501) staff       (20)      995 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_hstore_field.py
+-rw-r--r--   0 swen       (501) staff       (20)     4304 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_hstore_required.py
+-rw-r--r--   0 swen       (501) staff       (20)     5704 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_hstore_unique.py
+-rw-r--r--   0 swen       (501) staff       (20)     3799 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_insert.py
+-rw-r--r--   0 swen       (501) staff       (20)     6444 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/test_make_migrations.py
+-rw-r--r--   0 swen       (501) staff       (20)     5908 2019-11-10 20:54:32.000000 django-postgres-extra-2.0a9/tests/test_management_command_partition.py
+-rw-r--r--   0 swen       (501) staff       (20)     1852 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_manager.py
+-rw-r--r--   0 swen       (501) staff       (20)      639 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_manager_context.py
+-rw-r--r--   0 swen       (501) staff       (20)     1074 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/test_materialized_view_model.py
+-rw-r--r--   0 swen       (501) staff       (20)     6086 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/tests/test_migration_operations.py
+-rw-r--r--   0 swen       (501) staff       (20)    12213 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_on_conflict.py
+-rw-r--r--   0 swen       (501) staff       (20)     5435 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_on_conflict_nothing.py
+-rw-r--r--   0 swen       (501) staff       (20)     3914 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_on_conflict_update.py
+-rw-r--r--   0 swen       (501) staff       (20)     2208 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/test_partitioned_model.py
+-rw-r--r--   0 swen       (501) staff       (20)     3432 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/test_partitioned_model_state.py
+-rw-r--r--   0 swen       (501) staff       (20)     2780 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/tests/test_partitioning_manager.py
+-rw-r--r--   0 swen       (501) staff       (20)    21312 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/tests/test_partitioning_time.py
+-rw-r--r--   0 swen       (501) staff       (20)     2442 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_query.py
+-rw-r--r--   0 swen       (501) staff       (20)     2239 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/test_query_values.py
+-rw-r--r--   0 swen       (501) staff       (20)     8026 2019-11-10 20:11:16.000000 django-postgres-extra-2.0a9/tests/test_schema_editor_partitioning.py
+-rw-r--r--   0 swen       (501) staff       (20)     4710 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/test_schema_editor_view.py
+-rw-r--r--   0 swen       (501) staff       (20)     5590 2019-10-10 18:26:58.000000 django-postgres-extra-2.0a9/tests/test_upsert.py
+-rw-r--r--   0 swen       (501) staff       (20)     3445 2019-11-09 15:08:27.000000 django-postgres-extra-2.0a9/tests/test_view_models.py
```

### Comparing `django-postgres-extra-2.0a7/PKG-INFO` & `django-postgres-extra-2.0a9/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,31 +1,32 @@
 Metadata-Version: 2.1
 Name: django-postgres-extra
-Version: 2.0a7
+Version: 2.0a9
 Summary: Bringing all of PostgreSQL's awesomeness to Django.
 Home-page: https://github.com/SectorLabs/django-postgres-extra
 Author: Sector Labs
 Author-email: open-source@sectorlabs.ro
 License: MIT License
 Description:   
         |  |  |  |
         |--------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
         | :white_check_mark: | **Tests** | [![CircleCI](https://circleci.com/gh/SectorLabs/django-postgres-extra/tree/master.svg?style=svg)](https://circleci.com/gh/SectorLabs/django-postgres-extra/tree/master) |
         | :memo: | **License** | [![License](https://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org) |
         | :package: | **PyPi** | [![PyPi](https://badge.fury.io/py/django-postgres-extra.svg)](https://pypi.python.org/pypi/django-postgres-extra) |
-        | <img src="https://icon-library.net/images/django-icon/django-icon-0.jpg" width="22px" height="22px" align="center" /> | **Django Versions** | 2.0, 2.1, 2.2 |
+        | :four_leaf_clover: | **Code coverage** | [![Coverage Status](https://coveralls.io/repos/github/SectorLabs/django-postgres-extra/badge.svg?branch=coveralls)](https://coveralls.io/github/SectorLabs/django-postgres-extra?branch=master) |
+        | <img src="https://icon-library.net/images/django-icon/django-icon-0.jpg" width="22px" height="22px" align="center" /> | **Django Versions** | 2.0, 2.1, 2.2, 3.0 |
         | <img src="http://www.iconarchive.com/download/i73027/cornmanthe3rd/plex/Other-python.ico" width="22px" height="22px" align="center" /> | **Python Versions** | 3.7, 3.8 |
-        | :book: | **Documentation** | [Read The Docs](https://django-postgres-extra.readthedocs.io) |
-        | :warning: | **Upgrade** | [Upgrade fom v1.x](https://django-postgres-extra.readthedocs.io/major-releases#v2x)
-        | :checkered_flag: | **Installation** | [Installation Guide](https://django-postgres-extra.readthedocs.io/#installation) |
-        | :fire: | **Features** | [Features & Documentation](https://django-postgres-extra.readthedocs.io/#features) |
+        | :book: | **Documentation** | [Read The Docs](https://django-postgres-extra.readthedocs.io/en/master/) |
+        | :warning: | **Upgrade** | [Upgrade from v1.x](https://django-postgres-extra.readthedocs.io/en/master/major_releases.html#new-features)
+        | :checkered_flag: | **Installation** | [Installation Guide](https://django-postgres-extra.readthedocs.io/en/master/installation.html) |
+        | :fire: | **Features** | [Features & Documentation](https://django-postgres-extra.readthedocs.io/en/master/index.html#features) |
         | :droplet: | **Future enhancements** | [Potential features](https://github.com/SectorLabs/django-postgres-extra/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement) |
         
         `django-postgres-extra` aims to make all of PostgreSQL's awesome features available through the Django ORM. We do this by taking care of all the hassle. As opposed to the many small packages that are available to try to bring a single feature to Django with minimal effort. ``django-postgres-extra`` goes the extra mile, with well tested implementations, seamless migrations and much more.
-        
+         
         With seamless we mean that any features we add will work truly seamlessly. You should not have to manually modify your migrations to work with fields and objects provided by this package.
         
         ---
         
         :warning: **This README is for v2 which is currently under development. See the `v1` branch for v1.x.**
         
         ---
@@ -35,15 +36,14 @@
         [See the full list](http://django-postgres-extra.readthedocs.io/#features)
         
         * **Native upserts**
         
             * Single query
             * Concurrency safe
             * With bulk support (single query)
-            * Expressions to select individual keys
         
         * **Extended support for HStoreField**
         
             * Unique constraints
             * Null constraints
             * Select individual keys using ``.values()`` or ``.values_list()``
         
@@ -60,15 +60,15 @@
             * Conditional unique index.
             * Case sensitive unique index.
         
         ## Working with the code
         ### Prerequisites
         
         * PostgreSQL 10 or newer.
-        * Django 2.0 or newer.
+        * Django 2.0 or newer (including 3.0).
         * Python 3.7 or newer.
         
         ### Getting started
         
         1. Clone the repository:
         
                 λ git clone https://github.com/SectorLabs/django-postgres-extra.git
@@ -86,16 +86,15 @@
         
            Hint: if you're using virtualenvwrapper, you might find it beneficial to put
            the ``export`` line in ``$VIRTUAL_ENV/bin/postactivate`` so that it's always
            available when using this virtualenv.
         
         4. Install the development/test dependencies:
         
-               λ pip install -r requirements/test.txt
-               λ pip install -r requirements/analysis.txt
+               λ pip install .[test] .[analysis]
         
         5. Run the tests:
         
                λ tox
         
         6. Run the benchmarks:
         
@@ -112,8 +111,12 @@
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Topic :: Internet :: WWW/HTTP
 Classifier: Topic :: Internet :: WWW/HTTP :: Dynamic Content
+Requires-Python: >=3.7
 Description-Content-Type: text/markdown
+Provides-Extra: docs
+Provides-Extra: test
+Provides-Extra: analysis
```

### Comparing `django-postgres-extra-2.0a7/README.md` & `django-postgres-extra-2.0a9/README.md`

 * *Files 14% similar despite different names*

```diff
@@ -3,24 +3,25 @@
 </h1>
   
 |  |  |  |
 |--------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 | :white_check_mark: | **Tests** | [![CircleCI](https://circleci.com/gh/SectorLabs/django-postgres-extra/tree/master.svg?style=svg)](https://circleci.com/gh/SectorLabs/django-postgres-extra/tree/master) |
 | :memo: | **License** | [![License](https://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org) |
 | :package: | **PyPi** | [![PyPi](https://badge.fury.io/py/django-postgres-extra.svg)](https://pypi.python.org/pypi/django-postgres-extra) |
-| <img src="https://icon-library.net/images/django-icon/django-icon-0.jpg" width="22px" height="22px" align="center" /> | **Django Versions** | 2.0, 2.1, 2.2 |
+| :four_leaf_clover: | **Code coverage** | [![Coverage Status](https://coveralls.io/repos/github/SectorLabs/django-postgres-extra/badge.svg?branch=coveralls)](https://coveralls.io/github/SectorLabs/django-postgres-extra?branch=master) |
+| <img src="https://icon-library.net/images/django-icon/django-icon-0.jpg" width="22px" height="22px" align="center" /> | **Django Versions** | 2.0, 2.1, 2.2, 3.0 |
 | <img src="http://www.iconarchive.com/download/i73027/cornmanthe3rd/plex/Other-python.ico" width="22px" height="22px" align="center" /> | **Python Versions** | 3.7, 3.8 |
-| :book: | **Documentation** | [Read The Docs](https://django-postgres-extra.readthedocs.io) |
-| :warning: | **Upgrade** | [Upgrade fom v1.x](https://django-postgres-extra.readthedocs.io/major-releases#v2x)
-| :checkered_flag: | **Installation** | [Installation Guide](https://django-postgres-extra.readthedocs.io/#installation) |
-| :fire: | **Features** | [Features & Documentation](https://django-postgres-extra.readthedocs.io/#features) |
+| :book: | **Documentation** | [Read The Docs](https://django-postgres-extra.readthedocs.io/en/master/) |
+| :warning: | **Upgrade** | [Upgrade from v1.x](https://django-postgres-extra.readthedocs.io/en/master/major_releases.html#new-features)
+| :checkered_flag: | **Installation** | [Installation Guide](https://django-postgres-extra.readthedocs.io/en/master/installation.html) |
+| :fire: | **Features** | [Features & Documentation](https://django-postgres-extra.readthedocs.io/en/master/index.html#features) |
 | :droplet: | **Future enhancements** | [Potential features](https://github.com/SectorLabs/django-postgres-extra/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement) |
 
 `django-postgres-extra` aims to make all of PostgreSQL's awesome features available through the Django ORM. We do this by taking care of all the hassle. As opposed to the many small packages that are available to try to bring a single feature to Django with minimal effort. ``django-postgres-extra`` goes the extra mile, with well tested implementations, seamless migrations and much more.
-
+ 
 With seamless we mean that any features we add will work truly seamlessly. You should not have to manually modify your migrations to work with fields and objects provided by this package.
 
 ---
 
 :warning: **This README is for v2 which is currently under development. See the `v1` branch for v1.x.**
 
 ---
@@ -30,15 +31,14 @@
 [See the full list](http://django-postgres-extra.readthedocs.io/#features)
 
 * **Native upserts**
 
     * Single query
     * Concurrency safe
     * With bulk support (single query)
-    * Expressions to select individual keys
 
 * **Extended support for HStoreField**
 
     * Unique constraints
     * Null constraints
     * Select individual keys using ``.values()`` or ``.values_list()``
 
@@ -55,15 +55,15 @@
     * Conditional unique index.
     * Case sensitive unique index.
 
 ## Working with the code
 ### Prerequisites
 
 * PostgreSQL 10 or newer.
-* Django 2.0 or newer.
+* Django 2.0 or newer (including 3.0).
 * Python 3.7 or newer.
 
 ### Getting started
 
 1. Clone the repository:
 
         λ git clone https://github.com/SectorLabs/django-postgres-extra.git
@@ -81,16 +81,15 @@
 
    Hint: if you're using virtualenvwrapper, you might find it beneficial to put
    the ``export`` line in ``$VIRTUAL_ENV/bin/postactivate`` so that it's always
    available when using this virtualenv.
 
 4. Install the development/test dependencies:
 
-       λ pip install -r requirements/test.txt
-       λ pip install -r requirements/analysis.txt
+       λ pip install .[test] .[analysis]
 
 5. Run the tests:
 
        λ tox
 
 6. Run the benchmarks:
```

### Comparing `django-postgres-extra-2.0a7/django_postgres_extra.egg-info/PKG-INFO` & `django-postgres-extra-2.0a9/django_postgres_extra.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,31 +1,32 @@
 Metadata-Version: 2.1
 Name: django-postgres-extra
-Version: 2.0a7
+Version: 2.0a9
 Summary: Bringing all of PostgreSQL's awesomeness to Django.
 Home-page: https://github.com/SectorLabs/django-postgres-extra
 Author: Sector Labs
 Author-email: open-source@sectorlabs.ro
 License: MIT License
 Description:   
         |  |  |  |
         |--------------------|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
         | :white_check_mark: | **Tests** | [![CircleCI](https://circleci.com/gh/SectorLabs/django-postgres-extra/tree/master.svg?style=svg)](https://circleci.com/gh/SectorLabs/django-postgres-extra/tree/master) |
         | :memo: | **License** | [![License](https://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org) |
         | :package: | **PyPi** | [![PyPi](https://badge.fury.io/py/django-postgres-extra.svg)](https://pypi.python.org/pypi/django-postgres-extra) |
-        | <img src="https://icon-library.net/images/django-icon/django-icon-0.jpg" width="22px" height="22px" align="center" /> | **Django Versions** | 2.0, 2.1, 2.2 |
+        | :four_leaf_clover: | **Code coverage** | [![Coverage Status](https://coveralls.io/repos/github/SectorLabs/django-postgres-extra/badge.svg?branch=coveralls)](https://coveralls.io/github/SectorLabs/django-postgres-extra?branch=master) |
+        | <img src="https://icon-library.net/images/django-icon/django-icon-0.jpg" width="22px" height="22px" align="center" /> | **Django Versions** | 2.0, 2.1, 2.2, 3.0 |
         | <img src="http://www.iconarchive.com/download/i73027/cornmanthe3rd/plex/Other-python.ico" width="22px" height="22px" align="center" /> | **Python Versions** | 3.7, 3.8 |
-        | :book: | **Documentation** | [Read The Docs](https://django-postgres-extra.readthedocs.io) |
-        | :warning: | **Upgrade** | [Upgrade fom v1.x](https://django-postgres-extra.readthedocs.io/major-releases#v2x)
-        | :checkered_flag: | **Installation** | [Installation Guide](https://django-postgres-extra.readthedocs.io/#installation) |
-        | :fire: | **Features** | [Features & Documentation](https://django-postgres-extra.readthedocs.io/#features) |
+        | :book: | **Documentation** | [Read The Docs](https://django-postgres-extra.readthedocs.io/en/master/) |
+        | :warning: | **Upgrade** | [Upgrade from v1.x](https://django-postgres-extra.readthedocs.io/en/master/major_releases.html#new-features)
+        | :checkered_flag: | **Installation** | [Installation Guide](https://django-postgres-extra.readthedocs.io/en/master/installation.html) |
+        | :fire: | **Features** | [Features & Documentation](https://django-postgres-extra.readthedocs.io/en/master/index.html#features) |
         | :droplet: | **Future enhancements** | [Potential features](https://github.com/SectorLabs/django-postgres-extra/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement) |
         
         `django-postgres-extra` aims to make all of PostgreSQL's awesome features available through the Django ORM. We do this by taking care of all the hassle. As opposed to the many small packages that are available to try to bring a single feature to Django with minimal effort. ``django-postgres-extra`` goes the extra mile, with well tested implementations, seamless migrations and much more.
-        
+         
         With seamless we mean that any features we add will work truly seamlessly. You should not have to manually modify your migrations to work with fields and objects provided by this package.
         
         ---
         
         :warning: **This README is for v2 which is currently under development. See the `v1` branch for v1.x.**
         
         ---
@@ -35,15 +36,14 @@
         [See the full list](http://django-postgres-extra.readthedocs.io/#features)
         
         * **Native upserts**
         
             * Single query
             * Concurrency safe
             * With bulk support (single query)
-            * Expressions to select individual keys
         
         * **Extended support for HStoreField**
         
             * Unique constraints
             * Null constraints
             * Select individual keys using ``.values()`` or ``.values_list()``
         
@@ -60,15 +60,15 @@
             * Conditional unique index.
             * Case sensitive unique index.
         
         ## Working with the code
         ### Prerequisites
         
         * PostgreSQL 10 or newer.
-        * Django 2.0 or newer.
+        * Django 2.0 or newer (including 3.0).
         * Python 3.7 or newer.
         
         ### Getting started
         
         1. Clone the repository:
         
                 λ git clone https://github.com/SectorLabs/django-postgres-extra.git
@@ -86,16 +86,15 @@
         
            Hint: if you're using virtualenvwrapper, you might find it beneficial to put
            the ``export`` line in ``$VIRTUAL_ENV/bin/postactivate`` so that it's always
            available when using this virtualenv.
         
         4. Install the development/test dependencies:
         
-               λ pip install -r requirements/test.txt
-               λ pip install -r requirements/analysis.txt
+               λ pip install .[test] .[analysis]
         
         5. Run the tests:
         
                λ tox
         
         6. Run the benchmarks:
         
@@ -112,8 +111,12 @@
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Topic :: Internet :: WWW/HTTP
 Classifier: Topic :: Internet :: WWW/HTTP :: Dynamic Content
+Requires-Python: >=3.7
 Description-Content-Type: text/markdown
+Provides-Extra: docs
+Provides-Extra: test
+Provides-Extra: analysis
```

### Comparing `django-postgres-extra-2.0a7/django_postgres_extra.egg-info/SOURCES.txt` & `django-postgres-extra-2.0a9/django_postgres_extra.egg-info/SOURCES.txt`

 * *Files 17% similar despite different names*

```diff
@@ -1,88 +1,118 @@
 README.md
 setup.cfg
 setup.py
 django_postgres_extra.egg-info/PKG-INFO
 django_postgres_extra.egg-info/SOURCES.txt
 django_postgres_extra.egg-info/dependency_links.txt
+django_postgres_extra.egg-info/requires.txt
 django_postgres_extra.egg-info/top_level.txt
 psqlextra/__init__.py
 psqlextra/apps.py
-psqlextra/auto_partition.py
 psqlextra/compiler.py
-psqlextra/datastructures.py
 psqlextra/expressions.py
 psqlextra/query.py
-psqlextra/signals.py
 psqlextra/sql.py
+psqlextra/type_assertions.py
 psqlextra/types.py
 psqlextra/util.py
 psqlextra/backend/__init__.py
 psqlextra/backend/base.py
 psqlextra/backend/base_impl.py
 psqlextra/backend/introspection.py
 psqlextra/backend/operations.py
 psqlextra/backend/schema.py
 psqlextra/backend/migrations/__init__.py
 psqlextra/backend/migrations/patched_autodetector.py
 psqlextra/backend/migrations/patched_migrations.py
 psqlextra/backend/migrations/patched_project_state.py
-psqlextra/backend/migrations/state.py
 psqlextra/backend/migrations/operations/__init__.py
 psqlextra/backend/migrations/operations/add_default_partition.py
 psqlextra/backend/migrations/operations/add_list_partition.py
 psqlextra/backend/migrations/operations/add_range_partition.py
+psqlextra/backend/migrations/operations/apply_state.py
+psqlextra/backend/migrations/operations/create_materialized_view_model.py
 psqlextra/backend/migrations/operations/create_partitioned_model.py
+psqlextra/backend/migrations/operations/create_view_model.py
 psqlextra/backend/migrations/operations/delete_default_partition.py
 psqlextra/backend/migrations/operations/delete_list_partition.py
+psqlextra/backend/migrations/operations/delete_materialized_view_model.py
 psqlextra/backend/migrations/operations/delete_partition.py
 psqlextra/backend/migrations/operations/delete_partitioned_model.py
 psqlextra/backend/migrations/operations/delete_range_partition.py
+psqlextra/backend/migrations/operations/delete_view_model.py
 psqlextra/backend/migrations/operations/partition.py
+psqlextra/backend/migrations/state/__init__.py
+psqlextra/backend/migrations/state/materialized_view.py
+psqlextra/backend/migrations/state/model.py
+psqlextra/backend/migrations/state/partitioning.py
+psqlextra/backend/migrations/state/view.py
 psqlextra/backend/side_effects/__init__.py
 psqlextra/backend/side_effects/hstore_required.py
 psqlextra/backend/side_effects/hstore_unique.py
 psqlextra/fields/__init__.py
 psqlextra/fields/hstore_field.py
 psqlextra/indexes/__init__.py
 psqlextra/indexes/case_insensitive_unique_index.py
 psqlextra/indexes/conditional_unique_index.py
 psqlextra/management/__init__.py
 psqlextra/management/commands/__init__.py
-psqlextra/management/commands/pgautopartition.py
 psqlextra/management/commands/pgmakemigrations.py
+psqlextra/management/commands/pgpartition.py
+psqlextra/management/commands/pgrefreshmv.py
 psqlextra/manager/__init__.py
 psqlextra/manager/manager.py
 psqlextra/models/__init__.py
 psqlextra/models/base.py
 psqlextra/models/options.py
 psqlextra/models/partitioned.py
+psqlextra/models/view.py
+psqlextra/partitioning/__init__.py
+psqlextra/partitioning/config.py
+psqlextra/partitioning/error.py
+psqlextra/partitioning/manager.py
+psqlextra/partitioning/partition.py
+psqlextra/partitioning/range_partition.py
+psqlextra/partitioning/range_strategy.py
+psqlextra/partitioning/shorthands.py
+psqlextra/partitioning/strategy.py
+psqlextra/partitioning/time_partition.py
+psqlextra/partitioning/time_partition_size.py
+psqlextra/partitioning/time_strategy.py
 tests/__init__.py
 tests/conftest.py
+tests/db_introspection.py
 tests/fake_model.py
 tests/migrations.py
-tests/test_auto_partition.py
 tests/test_case_insensitive_unique_index.py
 tests/test_conditional_unique_index.py
 tests/test_db_backend.py
 tests/test_hstore_autodetect.py
 tests/test_hstore_field.py
 tests/test_hstore_required.py
 tests/test_hstore_unique.py
 tests/test_insert.py
 tests/test_make_migrations.py
+tests/test_management_command_partition.py
 tests/test_manager.py
 tests/test_manager_context.py
+tests/test_materialized_view_model.py
 tests/test_migration_operations.py
 tests/test_on_conflict.py
 tests/test_on_conflict_nothing.py
 tests/test_on_conflict_update.py
 tests/test_partitioned_model.py
 tests/test_partitioned_model_state.py
+tests/test_partitioning_manager.py
+tests/test_partitioning_time.py
 tests/test_query.py
 tests/test_query_values.py
-tests/test_schema_editor.py
+tests/test_schema_editor_partitioning.py
+tests/test_schema_editor_view.py
 tests/test_upsert.py
+tests/test_view_models.py
 tests/benchmarks/__init__.py
 tests/benchmarks/test_insert_nothing.py
 tests/benchmarks/test_upsert.py
-tests/benchmarks/test_upsert_bulk.py
+tests/benchmarks/test_upsert_bulk.py
+tests/snapshots/__init__.py
+tests/snapshots/snap_test_management_command_partition.py
```

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/base.py` & `django-postgres-extra-2.0a9/psqlextra/backend/base.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/base_impl.py` & `django-postgres-extra-2.0a9/psqlextra/backend/base_impl.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/add_default_partition.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/add_default_partition.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/add_list_partition.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/add_list_partition.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/add_range_partition.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/add_range_partition.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/create_partitioned_model.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/create_partitioned_model.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_default_partition.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_default_partition.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_list_partition.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_list_partition.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_partition.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_partition.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_partitioned_model.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_partitioned_model.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/delete_range_partition.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/delete_range_partition.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/operations/partition.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/operations/partition.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/patched_project_state.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/patched_project_state.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,34 +1,48 @@
 from contextlib import contextmanager
 from unittest import mock
 
 from django.db.migrations.state import ProjectState
 
-from psqlextra.models import PostgresPartitionedModel
-
-from .state import PostgresPartitionedModelState
+from psqlextra.models import (
+    PostgresMaterializedViewModel,
+    PostgresPartitionedModel,
+    PostgresViewModel,
+)
+
+from .state import (
+    PostgresMaterializedViewModelState,
+    PostgresPartitionedModelState,
+    PostgresViewModelState,
+)
 
 # original `ProjectState.from_apps` function,
 # saved here so the patched version can call
 # the original
 original_from_apps = ProjectState.from_apps
 
 
 def project_state_from_apps(apps):
     """Creates a :see:ProjectState instance from the specified list of apps."""
 
     project_state = original_from_apps(apps)
     for model in apps.get_models(include_swapped=True):
-        # for partitioned models, use the more specific model
+        model_state = None
+
+        # for some of our custom models, use the more specific model
         # state.. for everything else, business as usual
-        if not issubclass(model, PostgresPartitionedModel):
+        if issubclass(model, PostgresPartitionedModel):
+            model_state = PostgresPartitionedModelState.from_model(model)
+        elif issubclass(model, PostgresMaterializedViewModel):
+            model_state = PostgresMaterializedViewModelState.from_model(model)
+        elif issubclass(model, PostgresViewModel):
+            model_state = PostgresViewModelState.from_model(model)
+        else:
             continue
 
-        model_state = PostgresPartitionedModelState.from_model(model)
-
         model_state_key = (model_state.app_label, model_state.name_lower)
         project_state.models[model_state_key] = model_state
 
     return project_state
 
 
 @contextmanager
```

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/migrations/state.py` & `django-postgres-extra-2.0a9/psqlextra/backend/migrations/state/partitioning.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,63 +1,50 @@
-from typing import Dict, List
-
-from django.db.migrations.state import ModelState
-from django.db.models import Model
+from typing import Dict, List, Type
 
 from psqlextra.models import PostgresPartitionedModel
 
+from .model import PostgresModelState
 
-class PostgresPartitionState:
-    """Represents the state of a partition for a.
 
-    :see:PostgresPartitionedModel during a migration.
-    """
+class PostgresPartitionState:
+    """Represents the state of a partition for a :see:PostgresPartitionedModel
+    during a migration."""
 
     def __init__(self, app_label: str, model_name: str, name: str) -> None:
         self.app_label = app_label
         self.model_name = model_name
         self.name = name
 
 
 class PostgresRangePartitionState(PostgresPartitionState):
-    """Represents the state of a range partition for a.
-
-    :see:PostgresPartitionedModel during a migration.
-    """
+    """Represents the state of a range partition for a
+    :see:PostgresPartitionedModel during a migration."""
 
     def __init__(
         self, app_label: str, model_name: str, name: str, from_values, to_values
     ):
         super().__init__(app_label, model_name, name)
 
         self.from_values = from_values
         self.to_values = to_values
 
 
 class PostgresListPartitionState(PostgresPartitionState):
-    """Represents the state of a list partition for a.
-
-    :see:PostgresPartitionedModel during a migration.
-    """
+    """Represents the state of a list partition for a
+    :see:PostgresPartitionedModel during a migration."""
 
     def __init__(self, app_label: str, model_name: str, name: str, values):
         super().__init__(app_label, model_name, name)
 
         self.values = values
 
 
-class PostgresPartitionedModelState(ModelState):
-    """Represents a :see:PostgresPartitionedModel.
-
-    We don't use the actual model class to represent models in migration
-    state as its not designed to have its options changed over time.
-
-    Instead, this state is used and after applying all migrations/
-    mutations, this gets rendered into a model.
-    """
+class PostgresPartitionedModelState(PostgresModelState):
+    """Represents the state of a :see:PostgresPartitionedModel in the
+    migrations."""
 
     def __init__(
         self,
         *args,
         partitions: List[PostgresPartitionState] = [],
         partitioning_options={},
         **kwargs
@@ -85,81 +72,47 @@
 
     def delete_partition(self, name: str):
         """Deletes a partition from this partitioned model state."""
 
         del self.partitions[name]
 
     @classmethod
-    def from_model(
-        cls, model: PostgresPartitionedModel, *args, **kwargs
+    def _pre_new(
+        cls,
+        model: PostgresPartitionedModel,
+        model_state: "PostgresPartitionedModelState",
     ) -> "PostgresPartitionedModelState":
-        """Creates a new :see:PartitionedModelState object from the specified
+        """Called when a new model state is created from the specified
         model."""
 
-        model_state = super().from_model(model, *args, **kwargs)
         model_state.partitions = dict()
         model_state.partitioning_options = dict(
             model._partitioning_meta.original_attrs
         )
-
-        # django does not add abstract bases as a base in migrations
-        # because it assumes the base does not add anything important
-        # in a migration.. but it does, so we replace the Model
-        # base with the actual base: PostgresPartitionedModel
-        bases = tuple()
-        for base in model_state.bases:
-            if issubclass(base, Model):
-                bases += (PostgresPartitionedModel,)
-            else:
-                bases += (base,)
-
-        model_state.bases = bases
         return model_state
 
-    def clone(self) -> "PostgresPartitionedModelState":
-        """Gets an exact copy of this :see:PostgresPartitionedModelState."""
+    def _pre_clone(
+        self, model_state: "PostgresPartitionedModelState"
+    ) -> "PostgresPartitionedModelState":
+        """Called when this model state is cloned."""
 
-        model_state = super().clone()
         model_state.partitions = dict(self.partitions)
         model_state.partitioning_options = dict(self.partitioning_options)
-
         return model_state
 
-    def render(self, apps):
-        """Renders this state into an actual model."""
+    def _pre_render(self, name: str, bases, attributes):
+        """Called when this model state is rendered into a model."""
 
-        # TODO: figure out a way to do this witout pretty much
-        #       copying the base class's implementation
-        #       ---
-        #       all we need is to add `PartitioningMeta` to
-        #       the class that is being declared
-
-        try:
-            bases = tuple(
-                (apps.get_model(base) if isinstance(base, str) else base)
-                for base in self.bases
-            )
-        except LookupError:
-            # TODO: this should be a InvalidBaseError
-            raise ValueError(
-                "Cannot resolve one or more bases from %r" % (self.bases,)
-            )
-
-        fields = {name: field.clone() for name, field in self.fields}
-        meta = type(
-            "Meta",
-            (),
-            {"app_label": self.app_label, "apps": apps, **self.options},
-        )
         partitioning_meta = type(
             "PartitioningMeta", (), dict(self.partitioning_options)
         )
+        return (
+            name,
+            bases,
+            {**attributes, "PartitioningMeta": partitioning_meta},
+        )
 
-        attributes = {
-            **fields,
-            "Meta": meta,
-            "PartitioningMeta": partitioning_meta,
-            "__module__": "__fake__",
-            **dict(self.construct_managers()),
-        }
+    @classmethod
+    def _get_base_model_class(self) -> Type[PostgresPartitionedModel]:
+        """Gets the class to use as a base class for rendered models."""
 
-        return type(self.name, bases, attributes)
+        return PostgresPartitionedModel
```

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/operations.py` & `django-postgres-extra-2.0a9/psqlextra/backend/operations.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/side_effects/hstore_required.py` & `django-postgres-extra-2.0a9/psqlextra/backend/side_effects/hstore_required.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/backend/side_effects/hstore_unique.py` & `django-postgres-extra-2.0a9/psqlextra/backend/side_effects/hstore_unique.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/compiler.py` & `django-postgres-extra-2.0a9/psqlextra/compiler.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/expressions.py` & `django-postgres-extra-2.0a9/psqlextra/expressions.py`

 * *Files 8% similar despite different names*

```diff
@@ -143,41 +143,14 @@
         original_expression = super().resolve_expression(*args, **kwargs)
         expression = HStoreColumn(
             original_expression.alias, original_expression.target, self.key
         )
         return expression
 
 
-class NonGroupableFunc(expressions.Func):
-    """A version of Django's :see:Func expression that is _never_ included in
-    the GROUP BY clause."""
-
-    def get_group_by_cols(self):
-        """Gets the columns to be included in the GROUP BY clause.
-
-        We have to override this because Django's default behavior is to
-        include function calls in GROUP by clauses.
-        """
-        return []
-
-
-class Min(NonGroupableFunc):
-    """Exposes PostgreSQL's MIN(..) func."""
-
-    def __init__(self, expression):
-        super().__init__(expression, function="MIN")
-
-
-class Max(NonGroupableFunc):
-    """Exposes PostgreSQL's Max(..) func."""
-
-    def __init__(self, expression):
-        super().__init__(expression, function="Max")
-
-
 class DateTimeEpochColumn(expressions.Col):
     """Gets the date/time column as a UNIX epoch timestamp."""
 
     contains_column_references = True
 
     def as_sql(self, compiler, connection):
         """Compiles this expression into SQL."""
```

### Comparing `django-postgres-extra-2.0a7/psqlextra/fields/hstore_field.py` & `django-postgres-extra-2.0a9/psqlextra/fields/hstore_field.py`

 * *Files 16% similar despite different names*

```diff
@@ -17,15 +17,24 @@
     def __init__(
         self,
         *args,
         uniqueness: List[Union[str, Tuple[str, ...]]] = None,
         required: List[str] = None,
         **kwargs
     ):
-        """Initializes a new instance of :see:HStoreField."""
+        """Initializes a new instance of :see:HStoreField.
+
+        Arguments:
+            uniqueness:
+                List of keys to enforce as unique. Use tuples
+                to enforce multiple keys together to be unique.
+
+            required:
+                List of keys that should be enforced as required.
+        """
 
         super(HStoreField, self).__init__(*args, **kwargs)
 
         self.uniqueness = uniqueness
         self.required = required
 
     def get_prep_value(self, value):
```

### Comparing `django-postgres-extra-2.0a7/psqlextra/indexes/case_insensitive_unique_index.py` & `django-postgres-extra-2.0a9/psqlextra/indexes/case_insensitive_unique_index.py`

 * *Files 8% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 
 class CaseInsensitiveUniqueIndex(Index):
     sql_create_unique_index = (
         "CREATE UNIQUE INDEX %(name)s ON %(table)s (%(columns)s)%(extra)s"
     )
 
-    def create_sql(self, model, schema_editor, using=""):
+    def create_sql(self, model, schema_editor, using="", **kwargs):
         statement = super().create_sql(model, schema_editor, using)
         statement.template = self.sql_create_unique_index
 
         column_collection = statement.parts["columns"]
         statement.parts["columns"] = ", ".join(
             [
                 "LOWER(%s)" % self._quote_column(column_collection, column, idx)
```

### Comparing `django-postgres-extra-2.0a7/psqlextra/indexes/conditional_unique_index.py` & `django-postgres-extra-2.0a9/psqlextra/indexes/conditional_unique_index.py`

 * *Files 17% similar despite different names*

```diff
@@ -4,31 +4,32 @@
 
 
 class ConditionalUniqueIndex(Index):
     """Creates a partial unique index based on a given condition.
 
     Useful, for example, if you need unique combination of foreign keys, but you might want to include
     NULL as a valid value. In that case, you can just use:
+
     >>> class Meta:
-    ...    indexes = [
-    ...        ConditionalUniqueIndex(fields=['a', 'b', 'c'], condition='"c" IS NOT NULL'),
-    ...        ConditionalUniqueIndex(fields=['a', 'b'], condition='"c" IS NULL')
-    ...    ]
+    >>>    indexes = [
+    >>>        ConditionalUniqueIndex(fields=['a', 'b', 'c'], condition='"c" IS NOT NULL'),
+    >>>        ConditionalUniqueIndex(fields=['a', 'b'], condition='"c" IS NULL')
+    >>>    ]
     """
 
     sql_create_index = "CREATE UNIQUE INDEX %(name)s ON %(table)s (%(columns)s)%(extra)s WHERE %(condition)s"
 
     def __init__(self, condition: str, fields=[], name=None):
         """Initializes a new instance of :see:ConditionalUniqueIndex."""
 
         super().__init__(fields=fields, name=name)
 
         self._condition = condition
 
-    def create_sql(self, model, schema_editor, using=""):
+    def create_sql(self, model, schema_editor, using="", **kwargs):
         """Creates the actual SQL used when applying the migration."""
         if django.VERSION >= (2, 0):
             statement = super().create_sql(model, schema_editor, using)
             statement.template = self.sql_create_index
             statement.parts["condition"] = self._condition
             return statement
         else:
```

### Comparing `django-postgres-extra-2.0a7/psqlextra/manager/manager.py` & `django-postgres-extra-2.0a9/psqlextra/manager/manager.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/models/partitioned.py` & `django-postgres-extra-2.0a9/psqlextra/models/partitioned.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/query.py` & `django-postgres-extra-2.0a9/psqlextra/query.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/psqlextra/sql.py` & `django-postgres-extra-2.0a9/psqlextra/sql.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,11 @@
-from collections import OrderedDict
 from typing import List, Optional, Tuple
 
+import django
+
 from django.core.exceptions import SuspiciousOperation
 from django.db import connections, models
 from django.db.models import sql
 from django.db.models.constants import LOOKUP_SEP
 
 from .compiler import PostgresInsertCompiler, PostgresUpdateCompiler
 from .expressions import HStoreColumn
@@ -47,70 +48,65 @@
                 raise SuspiciousOperation(
                     (
                         'Cannot rename annotation "{old_name}" to "{new_name}", because there'
                         ' is no annotation named "{old_name}".'
                     ).format(old_name=old_name, new_name=new_name)
                 )
 
-            self._annotations = OrderedDict(
-                [
-                    (new_name, v) if k == old_name else (k, v)
-                    for k, v in self._annotations.items()
-                ]
-            )
-
-    def add_fields(
-        self, field_names: List[str], allow_m2m: bool = True
-    ) -> bool:
-        """Adds the given (model) fields to the select set. The field names are
-        added in the order specified.
-
-        This overrides the base class's add_fields method. This is called by
-        the .values() or .values_list() method of the query set. It instructs
-        the ORM to only select certain values. A lot of processing is neccesarry
-        because it can be used to easily do joins. For example, `my_fk__name` pulls
-        in the `name` field in foreign key `my_fk`.
-
-        In our case, we want to be able to do `title__en`, where `title` is a HStoreField
-        and `en` a key. This doesn't really involve a join. We iterate over the specified
-        field names and filter out the ones that refer to HStoreField and compile it into
-        an expression which is added to the list of to be selected fields using `self.add_select`.
+            self.annotations[new_name] = annotation
+            del self.annotations[old_name]
+
+    def add_fields(self, field_names: List[str], *args, **kwargs) -> bool:
+        """Adds the given (model) fields to the select set.
+
+        The field names are added in the order specified. This overrides
+        the base class's add_fields method. This is called by the
+        .values() or .values_list() method of the query set. It
+        instructs the ORM to only select certain values. A lot of
+        processing is neccesarry because it can be used to easily do
+        joins. For example, `my_fk__name` pulls in the `name` field in
+        foreign key `my_fk`. In our case, we want to be able to do
+        `title__en`, where `title` is a HStoreField and `en` a key. This
+        doesn't really involve a join. We iterate over the specified
+        field names and filter out the ones that refer to HStoreField
+        and compile it into an expression which is added to the list of
+        to be selected fields using `self.add_select`.
         """
 
-        alias = self.get_initial_alias()
-        opts = self.get_meta()
-        cols = []
+        # django knows how to do all of this natively from v2.1
+        # see: https://github.com/django/django/commit/20bab2cf9d02a5c6477d8aac066a635986e0d3f3
+        if django.VERSION >= (2, 1):
+            return super().add_fields(field_names, *args, **kwargs)
+
+        select = []
+        field_names_without_hstore = []
+
         for name in field_names:
             parts = name.split(LOOKUP_SEP)
 
             # it cannot be a special hstore thing if there's no __ in it
             if len(parts) > 1:
                 column_name, hstore_key = parts[:2]
                 is_hstore, field = self._is_hstore_field(column_name)
                 if is_hstore:
-                    cols.append(
+                    select.append(
                         HStoreColumn(
                             self.model._meta.db_table or self.model.name,
                             field,
                             hstore_key,
                         )
                     )
                     continue
 
-            join_info = self.setup_joins(
-                parts, opts, alias, allow_many=allow_m2m
-            )
-            targets, final_alias, joins = self.trim_joins(
-                join_info[1], join_info[3], join_info[4]
-            )
-
-            for target in targets:
-                cols.append(target.get_col(final_alias))
-        if cols:
-            self.set_select(cols)
+            field_names_without_hstore.append(name)
+
+        super().add_fields(field_names_without_hstore, *args, **kwargs)
+
+        if len(select) > 0:
+            self.set_select(self.select + tuple(select))
 
     def _is_hstore_field(
         self, field_name: str
     ) -> Tuple[bool, Optional[models.Field]]:
         """Gets whether the field with the specified name is a HStoreField.
 
         Returns     A tuple of a boolean indicating whether the field
```

### Comparing `django-postgres-extra-2.0a7/psqlextra/types.py` & `django-postgres-extra-2.0a9/psqlextra/types.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,9 +1,12 @@
 from enum import Enum
-from typing import List
+from typing import Any, Dict, List, Tuple, Union
+
+SQL = str
+SQLWithParams = Tuple[str, Union[Tuple[Any, ...], Dict[str, Any]]]
 
 
 class StrEnum(str, Enum):
     @classmethod
     def all(cls) -> List["PostgresPartitioningMethod"]:
         return [choice for choice in cls]
```

### Comparing `django-postgres-extra-2.0a7/setup.py` & `django-postgres-extra-2.0a9/setup.py`

 * *Files 16% similar despite different names*

```diff
@@ -32,15 +32,15 @@
     os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8"
 ) as readme:
     README = readme.read().split("h1>\n", 2)[1]
 
 
 setup(
     name="django-postgres-extra",
-    version="2.0a7",
+    version="2.0a9",
     packages=find_packages(),
     include_package_data=True,
     license="MIT License",
     description="Bringing all of PostgreSQL's awesomeness to Django.",
     long_description=README,
     long_description_content_type="text/markdown",
     url="https://github.com/SectorLabs/django-postgres-extra",
@@ -54,21 +54,48 @@
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         "Programming Language :: Python",
         "Programming Language :: Python :: 3.5",
         "Topic :: Internet :: WWW/HTTP",
         "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
     ],
+    python_requires=">=3.7",
+    install_requires=[
+        "Django>=2.0",
+        "enforce==0.3.4",
+        "python-dateutil==2.8.0",
+        "structlog==19.1.0",
+        "ansimarkup==1.4.0",
+    ],
+    extras_require={
+        "docs": ["Sphinx==2.2.0", "sphinx-rtd-theme==0.4.3"],
+        "test": [
+            "psycopg2==2.8.4",
+            "dj-database-url==0.5.0",
+            "pytest==5.2.2",
+            "pytest-benchmark==3.2.2",
+            "pytest-django==3.6.0",
+            "pytest-cov==2.8.1",
+            "tox==3.14.0",
+            "freezegun==0.3.12",
+            "coveralls==1.8.2",
+            "snapshottest==0.5",
+        ],
+        "analysis": [
+            "black==19.3b0",
+            "flake8==3.7.7",
+            "autoflake==1.3",
+            "autopep8==1.4.4",
+            "isort==4.3.20",
+            "sl-docformatter==1.4",
+        ],
+    },
     cmdclass={
         "lint": create_command(
-            "Lints the code",
-            [
-                ["flake8", "setup.py", "psqlextra", "tests"],
-                ["pycodestyle", "setup.py", "psqlextra", "tests"],
-            ],
+            "Lints the code", [["flake8", "setup.py", "psqlextra", "tests"]]
         ),
         "lint_fix": create_command(
             "Lints the code",
             [
                 [
                     "autoflake",
                     "--remove-all-unused-imports",
@@ -119,17 +146,29 @@
                 ["python", "setup.py", "sort_imports"],
                 ["python", "setup.py", "lint_fix"],
             ],
         ),
         "verify": create_command(
             "Verifies whether the code is auto-formatted and has no linting errors",
             [
+                ["python", "setup.py", "format_verify"],
+                ["python", "setup.py", "format_docstrings_verify"],
+                ["python", "setup.py", "sort_imports_verify"],
+                ["python", "setup.py", "lint"],
+            ],
+        ),
+        "test": create_command(
+            "Runs all the tests",
+            [
                 [
-                    ["python", "setup.py", "format_verify"],
-                    ["python", "setup.py", "format_docstrings_verify"],
-                    ["python", "setup.py", "sort_imports_verify"],
-                    ["python", "setup.py", "lint"],
+                    "pytest",
+                    "--cov=psqlextra",
+                    "--cov-report=term",
+                    "--cov-report=xml:reports/xml",
+                    "--cov-report=html:reports/html",
+                    "--junitxml=reports/junit/tests.xml",
+                    "--reuse-db",
                 ]
             ],
         ),
     },
 )
```

### Comparing `django-postgres-extra-2.0a7/tests/benchmarks/test_insert_nothing.py` & `django-postgres-extra-2.0a9/tests/benchmarks/test_insert_nothing.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/benchmarks/test_upsert.py` & `django-postgres-extra-2.0a9/tests/benchmarks/test_upsert.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/benchmarks/test_upsert_bulk.py` & `django-postgres-extra-2.0a9/tests/benchmarks/test_upsert_bulk.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/conftest.py` & `django-postgres-extra-2.0a9/tests/conftest.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,15 +1,25 @@
 import pytest
 
 from django.contrib.postgres.signals import register_type_handlers
 from django.db import connection
 
+from .fake_model import define_fake_app
+
 
 @pytest.fixture(scope="function", autouse=True)
 def database_access(db):
     """Automatically enable database access for all tests."""
 
     # enable the hstore extension on our database because
     # our tests rely on it...
     with connection.schema_editor() as schema_editor:
         schema_editor.execute("CREATE EXTENSION IF NOT EXISTS hstore")
         register_type_handlers(schema_editor.connection)
+
+
+@pytest.fixture
+def fake_app():
+    """Creates a fake Django app and deletes it at the end of the test."""
+
+    with define_fake_app() as fake_app:
+        yield fake_app
```

### Comparing `django-postgres-extra-2.0a7/tests/fake_model.py` & `django-postgres-extra-2.0a9/tests/fake_model.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,23 +1,29 @@
 import os
 import sys
 import uuid
 
-from typing import List
+from contextlib import contextmanager
 
 from django.apps import AppConfig, apps
 from django.db import connection
-from django.db.models import Model
 
-from psqlextra.models import PostgresModel, PostgresPartitionedModel
+from psqlextra.models import (
+    PostgresMaterializedViewModel,
+    PostgresModel,
+    PostgresPartitionedModel,
+    PostgresViewModel,
+)
 
 
 def define_fake_model(
     fields=None, model_base=PostgresModel, meta_options={}, **attributes
 ):
+    """Defines a fake model (but does not create it in the database)."""
+
     name = str(uuid.uuid4()).replace("-", "")[:8].title()
 
     attributes = {
         "app_label": meta_options.get("app_label") or "tests",
         "__module__": __name__,
         "__name__": name,
         "Meta": type("Meta", (object,), meta_options),
@@ -29,51 +35,92 @@
 
     model = type(name, (model_base,), attributes)
 
     apps.app_configs[attributes["app_label"]].models[name] = model
     return model
 
 
-def define_fake_partitioning_model(
+def define_fake_view_model(
+    fields=None, view_options={}, meta_options={}, model_base=PostgresViewModel
+):
+    """Defines a fake view model."""
+
+    model = define_fake_model(
+        fields=fields,
+        model_base=model_base,
+        meta_options=meta_options,
+        ViewMeta=type("ViewMeta", (object,), view_options),
+    )
+
+    return model
+
+
+def define_fake_materialized_view_model(
+    fields=None,
+    view_options={},
+    meta_options={},
+    model_base=PostgresMaterializedViewModel,
+):
+    """Defines a fake materialized view model."""
+
+    model = define_fake_model(
+        fields=fields,
+        model_base=model_base,
+        meta_options=meta_options,
+        ViewMeta=type("ViewMeta", (object,), view_options),
+    )
+
+    return model
+
+
+def define_fake_partitioned_model(
     fields=None, partitioning_options={}, meta_options={}
 ):
+    """Defines a fake partitioned model."""
+
     model = define_fake_model(
         fields=fields,
         model_base=PostgresPartitionedModel,
         meta_options=meta_options,
         PartitioningMeta=type(
             "PartitioningMeta", (object,), partitioning_options
         ),
     )
 
     return model
 
 
 def get_fake_model(fields=None, model_base=PostgresModel, meta_options={}):
-    """Creates a fake model to use during unit tests."""
+    """Defines a fake model and creates it in the database."""
 
     model = define_fake_model(fields, model_base, meta_options)
 
     with connection.schema_editor() as schema_editor:
         schema_editor.create_model(model)
 
     return model
 
 
-def define_fake_app(models: List[Model] = []):
+@contextmanager
+def define_fake_app():
+    """Creates and registers a fake Django app."""
+
     name = str(uuid.uuid4()).replace("-", "")[:8] + "-app"
 
     app_config_cls = type(
         name + "Config",
         (AppConfig,),
         {"name": name, "path": os.path.dirname(__file__)},
     )
 
     app_config = app_config_cls(name, "")
     app_config.apps = apps
-
-    app_config.models = {model.__name__: model for model in models}
+    app_config.models = {}
 
     apps.app_configs[name] = app_config
     sys.modules[name] = {}
 
-    return app_config
+    try:
+        yield app_config
+    finally:
+        del apps.app_configs[name]
+        del sys.modules[name]
```

### Comparing `django-postgres-extra-2.0a7/tests/migrations.py` & `django-postgres-extra-2.0a9/tests/migrations.py`

 * *Files 10% similar despite different names*

```diff
@@ -6,15 +6,14 @@
 from django.db import connection, migrations
 from django.db.migrations.autodetector import MigrationAutodetector
 from django.db.migrations.executor import MigrationExecutor
 from django.db.migrations.loader import MigrationLoader
 from django.db.migrations.questioner import NonInteractiveMigrationQuestioner
 from django.db.migrations.state import ProjectState
 
-from psqlextra.backend.migrations import postgres_patched_migrations
 from psqlextra.backend.schema import PostgresSchemaEditor
 
 from .fake_model import define_fake_model
 
 
 @contextmanager
 def filtered_schema_editor(*filters: List[str]):
@@ -72,39 +71,44 @@
         executor.apply_migration(state, migration)
     else:
         executor.unapply_migration(state, migration)
 
     return migration
 
 
-@postgres_patched_migrations()
-def make_migration(app_label="tests"):
+def make_migration(app_label="tests", from_state=None, to_state=None):
     """Generates migrations based on the specified app's state."""
 
     app_labels = [app_label]
 
     loader = MigrationLoader(None, ignore_no_migrations=True)
     loader.check_consistent_history(connection)
 
     questioner = NonInteractiveMigrationQuestioner(
         specified_apps=app_labels, dry_run=False
     )
 
     autodetector = MigrationAutodetector(
-        loader.project_state(), ProjectState.from_apps(apps), questioner
+        from_state or loader.project_state(),
+        to_state or ProjectState.from_apps(apps),
+        questioner,
     )
 
     changes = autodetector.changes(
         graph=loader.graph,
         trim_to_apps=app_labels or None,
         convert_apps=app_labels or None,
         migration_name="test",
     )
 
-    return changes[app_label][0]
+    changes_for_app = changes.get(app_label)
+    if not changes_for_app or len(changes_for_app) == 0:
+        return None
+
+    return changes_for_app[0]
 
 
 @contextmanager
 def create_drop_model(field, filters: List[str]):
     """Creates and drops a model with the specified field.
 
     Arguments:
```

### Comparing `django-postgres-extra-2.0a7/tests/test_case_insensitive_unique_index.py` & `django-postgres-extra-2.0a9/tests/test_case_insensitive_unique_index.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_conditional_unique_index.py` & `django-postgres-extra-2.0a9/tests/test_conditional_unique_index.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_hstore_autodetect.py` & `django-postgres-extra-2.0a9/tests/test_hstore_autodetect.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_hstore_field.py` & `django-postgres-extra-2.0a9/tests/test_hstore_field.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_hstore_required.py` & `django-postgres-extra-2.0a9/tests/test_hstore_required.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_hstore_unique.py` & `django-postgres-extra-2.0a9/tests/test_hstore_unique.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_insert.py` & `django-postgres-extra-2.0a9/tests/test_insert.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_manager.py` & `django-postgres-extra-2.0a9/tests/test_manager.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_manager_context.py` & `django-postgres-extra-2.0a9/tests/test_manager_context.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_migration_operations.py` & `django-postgres-extra-2.0a9/tests/test_migration_operations.py`

 * *Files 3% similar despite different names*

```diff
@@ -4,69 +4,55 @@
 from django.db import connection, migrations, models
 
 from psqlextra.backend.migrations import operations
 from psqlextra.manager import PostgresManager
 from psqlextra.models import PostgresPartitionedModel
 from psqlextra.types import PostgresPartitioningMethod
 
+from . import db_introspection
 from .migrations import apply_migration
 
 
 def _partitioned_table_exists(op: operations.PostgresCreatePartitionedModel):
     """Checks whether the specified partitioned model operation was succesfully
     applied."""
 
     model_table_name = f"tests_{op.name}"
 
-    with connection.cursor() as cursor:
-        table = connection.introspection.get_partitioned_table(
-            cursor, model_table_name
-        )
-
-        if not table:
-            return False
-
-        part_options = op.partitioning_options
-
-        if table.method != part_options["method"]:
-            return False
-
-        if table.key != part_options["key"]:
-            return False
-
-    return True
+    table = db_introspection.get_partitioned_table(model_table_name)
+    if not table:
+        return False
+
+    part_options = op.partitioning_options
+    return (
+        table.method == part_options["method"]
+        and table.key == part_options["key"]
+    )
 
 
 def _partition_exists(model_op, op):
     """Checks whether the parttitioned model and partition operations were
     succesfully applied."""
 
     model_table_name = f"tests_{model_op.name}"
 
-    with connection.cursor() as cursor:
-        table = connection.introspection.get_partitioned_table(
-            cursor, model_table_name
-        )
-
-        if not table:
-            return False
-
-        partition = next(
-            (
-                partition
-                for partition in table.partitions
-                if partition.name == f"{model_table_name}_{op.name}"
-            ),
-            None,
-        )
-
-        if not partition:
-            return False
+    table = db_introspection.get_partitioned_table(model_table_name)
+    if not table:
+        return False
+
+    partition = next(
+        (
+            partition
+            for partition in table.partitions
+            if partition.full_name == f"{model_table_name}_{op.name}"
+        ),
+        None,
+    )
 
-    return True
+    return bool(partition)
 
 
 @pytest.fixture
 def create_model():
     """Factory for creating a :see:PostgresCreatePartitionedModel operation."""
 
     def _create_model(method):
```

### Comparing `django-postgres-extra-2.0a7/tests/test_on_conflict.py` & `django-postgres-extra-2.0a9/tests/test_on_conflict.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_on_conflict_nothing.py` & `django-postgres-extra-2.0a9/tests/test_on_conflict_nothing.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_on_conflict_update.py` & `django-postgres-extra-2.0a9/tests/test_on_conflict_update.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_partitioned_model.py` & `django-postgres-extra-2.0a9/tests/test_partitioned_model.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from psqlextra.models import PostgresPartitionedModel
 from psqlextra.types import PostgresPartitioningMethod
 
-from .fake_model import define_fake_partitioning_model
+from .fake_model import define_fake_partitioned_model
 
 
 def test_partitioned_model_abstract():
     """Tests whether :see:PostgresPartitionedModel is abstract."""
 
     assert PostgresPartitionedModel._meta.abstract
 
@@ -20,53 +20,53 @@
 
 def test_partitioned_model_default_options():
     """Tests whether the default partitioning options are set as expected on.
 
     :see:PostgresPartitionedModel.
     """
 
-    model = define_fake_partitioning_model()
+    model = define_fake_partitioned_model()
 
     assert model._partitioning_meta.method == PostgresPartitioningMethod.RANGE
     assert model._partitioning_meta.key == []
 
 
 def test_partitioned_model_method_option():
     """Tests whether the `method` partitioning option is properly copied onto
     the options object."""
 
-    model = define_fake_partitioning_model(
+    model = define_fake_partitioned_model(
         partitioning_options=dict(method=PostgresPartitioningMethod.LIST)
     )
 
     assert model._partitioning_meta.method == PostgresPartitioningMethod.LIST
 
 
 def test_partitioned_model_method_option_none():
     """Tests whether setting the `method` partitioning option results in the
     default being set."""
 
-    model = define_fake_partitioning_model(
+    model = define_fake_partitioned_model(
         partitioning_options=dict(method=None)
     )
 
     assert model._partitioning_meta.method == PostgresPartitioningMethod.RANGE
 
 
 def test_partitioned_model_key_option():
     """Tests whether the `key` partitioning option is properly copied onto the
     options object."""
 
-    model = define_fake_partitioning_model(
+    model = define_fake_partitioned_model(
         partitioning_options=dict(key=["timestamp"])
     )
 
     assert model._partitioning_meta.key == ["timestamp"]
 
 
 def test_partitioned_model_key_option_none():
     """Tests whether setting the `key` partitioning option results in the
     default being set."""
 
-    model = define_fake_partitioning_model(partitioning_options=dict(key=None))
+    model = define_fake_partitioned_model(partitioning_options=dict(key=None))
 
     assert model._partitioning_meta.key == []
```

### Comparing `django-postgres-extra-2.0a7/tests/test_partitioned_model_state.py` & `django-postgres-extra-2.0a9/tests/test_partitioned_model_state.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,27 +9,27 @@
     PostgresPartitionedModelState,
     PostgresPartitionState,
 )
 from psqlextra.manager import PostgresManager
 from psqlextra.models import PostgresPartitionedModel
 from psqlextra.types import PostgresPartitioningMethod
 
-from .fake_model import define_fake_partitioning_model
+from .fake_model import define_fake_partitioned_model
 
 
 @pytest.fixture
 def model():
     fields = {"name": models.TextField(), "category": models.TextField()}
 
     partitioning_options = {
         "method": PostgresPartitioningMethod.LIST,
         "key": ["category"],
     }
 
-    model = define_fake_partitioning_model(fields, partitioning_options)
+    model = define_fake_partitioned_model(fields, partitioning_options)
     return model
 
 
 def test_partitioned_model_state_copies():
     """Tests whether cloning the model state properly copies all the options.
 
     If it does not copy them, bad things can happen as the state is
```

### Comparing `django-postgres-extra-2.0a7/tests/test_query.py` & `django-postgres-extra-2.0a9/tests/test_query.py`

 * *Files identical despite different names*

### Comparing `django-postgres-extra-2.0a7/tests/test_query_values.py` & `django-postgres-extra-2.0a9/tests/test_query_values.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+import django
 import pytest
 
 from django.db import models
 
 from psqlextra.fields import HStoreField
 
 from .fake_model import get_fake_model
@@ -46,20 +47,24 @@
     query set's .values_list() works properly."""
 
     result = list(model.objects.values_list("title__en", "title__ar"))[0]
     assert result[0] == modelobj.title["en"]
     assert result[1] == modelobj.title["ar"]
 
 
-@pytest.mark.xfail(reason="has to be fixed as part of issue #8")
 def test_query_values_hstore_key_through_fk():
     """Tests whether selecting a single key from a :see:HStoreField using the
     query set's .values() works properly when there's a foreign key
     relationship involved."""
 
+    # this starting working in django 2.1
+    # see: https://github.com/django/django/commit/20bab2cf9d02a5c6477d8aac066a635986e0d3f3
+    if django.VERSION < (2, 1):
+        return
+
     fmodel = get_fake_model({"name": HStoreField()})
 
     model = get_fake_model(
         {"fk": models.ForeignKey(fmodel, on_delete=models.CASCADE)}
     )
 
     fobj = fmodel.objects.create(name={"en": "swen", "ar": "arabic swen"})
```

### Comparing `django-postgres-extra-2.0a7/tests/test_schema_editor.py` & `django-postgres-extra-2.0a9/psqlextra/partitioning/manager.py`

 * *Files 25% similar despite different names*

```diff
@@ -1,188 +1,206 @@
-import pytest
+from dataclasses import dataclass
+from typing import List, Optional, Tuple
 
-from django.core.exceptions import ImproperlyConfigured
-from django.db import connection, models
+from ansimarkup import ansiprint
+from django.db import connections
 
-from psqlextra.backend.schema import PostgresSchemaEditor
-from psqlextra.types import PostgresPartitioningMethod
+from psqlextra.models import PostgresPartitionedModel
 
-from .fake_model import define_fake_partitioning_model
-
-
-def test_schema_editor_create_delete_partitioned_model_range():
-    """Tests whether creating a partitioned model and adding a list partition
-    to it using the.
-
-    :see:PostgresSchemaEditor works.
-    """
-
-    method = PostgresPartitioningMethod.RANGE
-    key = ["timestamp"]
-
-    model = define_fake_partitioning_model(
-        {"name": models.TextField(), "timestamp": models.DateTimeField()},
-        {"method": method, "key": key},
-    )
-
-    schema_editor = PostgresSchemaEditor(connection)
-    schema_editor.create_partitioned_model(model)
-
-    schema_editor.add_range_partition(model, "pt1", "2019-01-01", "2019-02-01")
-
-    with connection.cursor() as cursor:
-        introspection = connection.introspection
-
-        table = introspection.get_partitioned_table(
-            cursor, model._meta.db_table
-        )
-        assert table.name == model._meta.db_table
-        assert table.method == method
-        assert table.key == key
-        assert table.partitions[0].name == model._meta.db_table + "_pt1"
-
-    schema_editor.delete_partitioned_model(model)
-
-    with connection.cursor() as cursor:
-        introspection = connection.introspection
-
-        table = introspection.get_partitioned_table(
-            cursor, model._meta.db_table
-        )
-        assert not table
-
-        partitions = introspection.get_partitions(cursor, model._meta.db_table)
-        assert len(partitions) == 0
-
-
-def test_schema_editor_create_delete_partitioned_model_list():
-    """Tests whether creating a partitioned model and adding a range partition
-    to it using the.
-
-    :see:PostgresSchemaEditor works.
-    """
-
-    method = PostgresPartitioningMethod.LIST
-    key = ["category"]
-
-    model = define_fake_partitioning_model(
-        {"name": models.TextField(), "category": models.TextField()},
-        {"method": method, "key": key},
-    )
-
-    schema_editor = PostgresSchemaEditor(connection)
-    schema_editor.create_partitioned_model(model)
-
-    schema_editor.add_list_partition(model, "pt1", ["car", "boat"])
-
-    with connection.cursor() as cursor:
-        introspection = connection.introspection
-
-        table = introspection.get_partitioned_table(
-            cursor, model._meta.db_table
-        )
-        assert table.name == model._meta.db_table
-        assert table.method == method
-        assert table.key == key
-        assert table.partitions[0].name == model._meta.db_table + "_pt1"
-
-    schema_editor.delete_partitioned_model(model)
-
-    with connection.cursor() as cursor:
-        introspection = connection.introspection
-
-        table = introspection.get_partitioned_table(
-            cursor, model._meta.db_table
-        )
-        assert not table
-
-        partitions = introspection.get_partitions(cursor, model._meta.db_table)
-        assert len(partitions) == 0
-
-
-def test_schema_editor_create_delete_partitioned_model_default():
-    """Tests whether creating a partitioned model and adding a default
-    partition to it using the.
-
-    :see:PostgresSchemaEditor works.
-    """
-
-    method = PostgresPartitioningMethod.LIST
-    key = ["category"]
-
-    model = define_fake_partitioning_model(
-        {"name": models.TextField(), "category": models.TextField()},
-        {"method": method, "key": key},
-    )
-
-    schema_editor = PostgresSchemaEditor(connection)
-    schema_editor.create_partitioned_model(model)
-
-    schema_editor.add_default_partition(model, "default")
-
-    with connection.cursor() as cursor:
-        introspection = connection.introspection
-
-        table = introspection.get_partitioned_table(
-            cursor, model._meta.db_table
-        )
-        assert table.name == model._meta.db_table
-        assert table.method == method
-        assert table.key == key
-        assert table.partitions[0].name == model._meta.db_table + "_default"
-
-    schema_editor.delete_partitioned_model(model)
-
-    with connection.cursor() as cursor:
-        introspection = connection.introspection
-
-        table = introspection.get_partitioned_table(
-            cursor, model._meta.db_table
-        )
-        assert not table
-
-        partitions = introspection.get_partitions(cursor, model._meta.db_table)
-        assert len(partitions) == 0
-
-
-def test_schema_editor_create_partitioned_model_no_method():
-    """Tests whether its possible to create a partitioned model without
-    explicitly setting a partitioning method.
-
-    The default is "range" so setting one explicitely should not be
-    needed.
-    """
-
-    model = define_fake_partitioning_model(
-        {"name": models.TextField(), "timestamp": models.DateTimeField()},
-        {"key": ["timestamp"]},
-    )
-
-    schema_editor = PostgresSchemaEditor(connection)
-    schema_editor.create_partitioned_model(model)
-
-    with connection.cursor() as cursor:
-        introspection = connection.introspection
-
-        pt = introspection.get_partitioned_table(cursor, model._meta.db_table)
-        assert pt.method == PostgresPartitioningMethod.RANGE
-        assert len(pt.partitions) == 0
-
-
-def test_schema_editor_create_partitioned_model_no_key():
-    """Tests whether trying to create a partitioned model without a
-    partitioning key raises.
-
-    :see:ImproperlyConfigured as its not possible to create
-    a partitioned model without one and we cannot
-    have a sane default.
-    """
-
-    model = define_fake_partitioning_model(
-        {"name": models.TextField(), "timestamp": models.DateTimeField()},
-        {"method": PostgresPartitioningMethod.RANGE},
-    )
-
-    schema_editor = PostgresSchemaEditor(connection)
-
-    with pytest.raises(ImproperlyConfigured):
-        schema_editor.create_partitioned_model(model)
+from .config import PostgresPartitioningConfig
+from .error import PostgresPartitioningError
+from .partition import PostgresPartition
+
+PartitionList = List[Tuple[PostgresPartitionedModel, List[PostgresPartition]]]
+
+
+@dataclass
+class PostgresModelPartitionPlan:
+    model: PostgresPartitionedModel
+    created_partitions: List[PostgresPartition]
+    deleted_partitions: List[PostgresPartition]
+
+    def print(self) -> None:
+        if (
+            len(self.created_partitions) == 0
+            and len(self.deleted_partitions) == 0
+        ):
+            return
+
+        ansiprint(f"<b><white>{self.model.__name__}:</white></b>")
+
+        for partition in self.deleted_partitions:
+            ansiprint("<b><red>  - %s</red></b>" % partition.name())
+            for key, value in partition.deconstruct().items():
+                ansiprint(f"<white>     <b>{key}</b>: {value}</white>")
+
+        for partition in self.created_partitions:
+            ansiprint("<b><green>  + %s</green></b>" % partition.name())
+            for key, value in partition.deconstruct().items():
+                ansiprint(f"<white>     <b>{key}</b>: {value}</white>")
+
+
+class PostgresPartitioningManager:
+    """Helps managing partitions by automatically creating new partitions and
+    deleting old ones according to the configuration."""
+
+    # comment placed on partition tables created by the partitioner
+    # partition tables that do not have this comment will _never_
+    # be deleted by the partitioner, this is a safety mechanism so
+    # manually created partitions aren't accidently cleaned up
+    _partition_table_comment: str = "psqlextra_auto_partitioned"
+
+    def __init__(self, configs: List[PostgresPartitioningConfig]) -> None:
+        self.configs = configs
+        self._validate_configs(self.configs)
+
+    def apply(
+        self,
+        no_delete: bool = False,
+        no_create: bool = False,
+        dry_run: bool = False,
+        using: Optional[str] = None,
+    ) -> None:
+        """Applies the partitioning plan by computing which partitions to
+        create and which ones to delete.
+
+        Arguments:
+            no_delete:
+                If set to True, no partitions will be marked
+                for deletion, regardless of the configuration.
+
+            no_create:
+                If set to True, no partitions will be marked
+                for creation, regardless of the configuration.
+
+            dry_run:
+                If set to True, the partitions will not be
+                created/deleted. The return value remains
+                the same.
+
+                Use this to discover what partitions would
+                be created/deleted.
+
+            using:
+                Name of the database connection to use.
+
+        Returns:
+            A plan of which partitons have been created/deleted
+            or will be created/deleted if dry_run=True.
+        """
+
+        plans = []
+
+        for config in self.configs:
+            created_partitions = (
+                self._auto_create(config, dry_run=dry_run, using=using)
+                if not no_create
+                else []
+            )
+
+            deleted_partitions = (
+                self._auto_delete(config, dry_run=dry_run, using=using)
+                if not no_delete
+                else []
+            )
+
+            plans.append(
+                PostgresModelPartitionPlan(
+                    model=config.model,
+                    created_partitions=created_partitions,
+                    deleted_partitions=deleted_partitions,
+                )
+            )
+
+        return plans
+
+    def find_by_model(
+        self, model: PostgresPartitionedModel
+    ) -> Optional[PostgresPartitioningConfig]:
+        """Finds the partitioning config for the specified model."""
+
+        return next(
+            (config for config in self.configs if config.model == model), None
+        )
+
+    def _auto_create(
+        self,
+        config: PostgresPartitioningConfig,
+        dry_run: bool = False,
+        using: Optional[str] = None,
+    ) -> List[PostgresPartition]:
+        connection = connections[using or "default"]
+        table = self._get_partitioned_table(connection, config.model)
+
+        created_partitions = []
+
+        with connection.schema_editor() as schema_editor:
+            for partition in config.strategy.to_create():
+                if table.partition_by_name(name=partition.name()):
+                    continue
+
+                created_partitions.append(partition)
+
+                if not dry_run:
+                    partition.create(
+                        config.model,
+                        schema_editor,
+                        comment=self._partition_table_comment,
+                    )
+
+        return created_partitions
+
+    def _auto_delete(
+        self,
+        config: PostgresPartitioningConfig,
+        dry_run: bool = False,
+        using: Optional[str] = None,
+    ) -> List[PostgresPartition]:
+        connection = connections[using or "default"]
+        table = self._get_partitioned_table(connection, config.model)
+        deleted_partitions = []
+
+        with connection.schema_editor() as schema_editor:
+            for partition in config.strategy.to_delete():
+                introspected_partition = table.partition_by_name(
+                    name=partition.name()
+                )
+                if not introspected_partition:
+                    continue
+
+                if (
+                    introspected_partition.comment
+                    != self._partition_table_comment
+                ):
+                    continue
+
+                deleted_partitions.append(partition)
+                if not dry_run:
+                    partition.delete(config.model, schema_editor)
+
+        return deleted_partitions
+
+    @staticmethod
+    def _get_partitioned_table(connection, model: PostgresPartitionedModel):
+        with connection.cursor() as cursor:
+            table = connection.introspection.get_partitioned_table(
+                cursor, model._meta.db_table
+            )
+
+        if not table:
+            raise PostgresPartitioningError(
+                f"Model {model.__name__}, with table "
+                "{model._meta.db_table} does not exists in the "
+                "database. Did you run `python manage.py migrate`?"
+            )
+
+        return table
+
+    @staticmethod
+    def _validate_configs(configs: List[PostgresPartitioningConfig]):
+        """Ensures there is only one config per model."""
+
+        models = set([config.model.__name__ for config in configs])
+        if len(models) != len(configs):
+            raise PostgresPartitioningError(
+                "Only one partitioning config per model is allowed"
+            )
```

### Comparing `django-postgres-extra-2.0a7/tests/test_upsert.py` & `django-postgres-extra-2.0a9/tests/test_upsert.py`

 * *Files identical despite different names*

