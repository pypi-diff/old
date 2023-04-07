# Comparing `tmp/resolwe-9.0.0a3.tar.gz` & `tmp/resolwe-9.0.0a4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/resolwe-9.0.0a3.tar", last modified: Wed May  9 21:10:30 2018, max compression
+gzip compressed data, was "dist/resolwe-9.0.0a4.tar", last modified: Mon May 14 10:02:51 2018, max compression
```

## Comparing `resolwe-9.0.0a3.tar` & `resolwe-9.0.0a4.tar`

### file list

```diff
@@ -1,394 +1,394 @@
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/
--rw-r--r--   0 domen      (501) staff       (20)     6003 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/PKG-INFO
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe.egg-info/
--rw-r--r--   0 domen      (501) staff       (20)     6003 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe.egg-info/PKG-INFO
--rw-r--r--   0 domen      (501) staff       (20)    12156 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe.egg-info/SOURCES.txt
--rw-r--r--   0 domen      (501) staff       (20)      674 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe.egg-info/requires.txt
--rw-r--r--   0 domen      (501) staff       (20)        8 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe.egg-info/top_level.txt
--rw-r--r--   0 domen      (501) staff       (20)        1 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe.egg-info/dependency_links.txt
--rw-r--r--   0 domen      (501) staff       (20)    10153 2018-04-12 10:11:32.000000 resolwe-9.0.0a3/.pylintrc
--rw-r--r--   0 domen      (501) staff       (20)    11358 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/LICENSE
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/tests/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/tests/.test_data/
--rw-r--r--   0 domen      (501) staff       (20)      118 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/tests/.test_data/README.rst
--rw-r--r--   0 domen      (501) staff       (20)      236 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/tests/__init__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/tests/.test_runtime/
--rw-r--r--   0 domen      (501) staff       (20)      118 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/tests/.test_runtime/README.rst
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/tests/.test_upload/
--rw-r--r--   0 domen      (501) staff       (20)      118 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/tests/.test_upload/README.rst
--rw-r--r--   0 domen      (501) staff       (20)      348 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/tests/.env
--rw-r--r--   0 domen      (501) staff       (20)     6930 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/tests/settings.py
--rw-r--r--   0 domen      (501) staff       (20)      457 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/tests/celery_conf.py
--rw-r--r--   0 domen      (501) staff       (20)     1007 2018-03-30 07:32:59.000000 resolwe-9.0.0a3/tests/docker-compose.yml
--rwxr-xr-x   0 domen      (501) staff       (20)      834 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/tests/manage.py
--rw-r--r--   0 domen      (501) staff       (20)      273 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/tests/urls.py
--rw-r--r--   0 domen      (501) staff       (20)     1163 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/MANIFEST.in
--rw-r--r--   0 domen      (501) staff       (20)       67 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/.coveragerc
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/docs/
--rw-r--r--   0 domen      (501) staff       (20)      717 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/docs/index.rst
--rw-r--r--   0 domen      (501) staff       (20)     3776 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/docs/contributing.rst
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/docs/images/
--rw-r--r--   0 domen      (501) staff       (20)    11809 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/images/resolwe_02_internals.png
--rw-r--r--   0 domen      (501) staff       (20)    18436 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/images/proc_02_flow.png
--rw-r--r--   0 domen      (501) staff       (20)    23450 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/images/proc_03_types.png
--rw-r--r--   0 domen      (501) staff       (20)    13981 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/images/resolwe_01_context.png
--rw-r--r--   0 domen      (501) staff       (20)     7006 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/images/proc_01.png
--rw-r--r--   0 domen      (501) staff       (20)    12023 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/images/resolwe_04_workers.png
--rw-r--r--   0 domen      (501) staff       (20)    17823 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/docs/images/resolwe_03_workflow.png
--rw-r--r--   0 domen      (501) staff       (20)      272 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/intro.rst
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/docs/example/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/docs/example/example/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/docs/example/example/processes/
--rw-r--r--   0 domen      (501) staff       (20)      185 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/example/example/processes/minimal.yml
--rw-r--r--   0 domen      (501) staff       (20)      815 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/example/example/processes/example.yml
--rw-r--r--   0 domen      (501) staff       (20)      162 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/example/example/processes/all_fields.yml
--rw-r--r--   0 domen      (501) staff       (20)      271 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/example/example/processes/example_basic.yml
--rw-r--r--   0 domen      (501) staff       (20)     3081 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/conf.py
--rw-r--r--   0 domen      (501) staff       (20)     1693 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/docs/overview.rst
--rw-r--r--   0 domen      (501) staff       (20)    24381 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/docs/proc.rst
--rw-r--r--   0 domen      (501) staff       (20)     3730 2018-03-30 07:32:59.000000 resolwe-9.0.0a3/docs/composer.rst
--rw-r--r--   0 domen      (501) staff       (20)      373 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/docs/ref.rst
--rw-r--r--   0 domen      (501) staff       (20)    10920 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/docs/flow.rst
--rw-r--r--   0 domen      (501) staff       (20)    25775 2018-05-09 21:04:27.000000 resolwe-9.0.0a3/docs/CHANGELOG.rst
--rw-r--r--   0 domen      (501) staff       (20)     3013 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/docs/api.rst
--rw-r--r--   0 domen      (501) staff       (20)     4023 2018-04-12 10:11:32.000000 resolwe-9.0.0a3/setup.py
--rw-r--r--   0 domen      (501) staff       (20)     2698 2018-04-12 10:11:32.000000 resolwe-9.0.0a3/tox.ini
--rw-r--r--   0 domen      (501) staff       (20)      557 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/setup.cfg
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/test/
--rw-r--r--   0 domen      (501) staff       (20)     1115 2018-03-30 07:32:59.000000 resolwe-9.0.0a3/resolwe/test/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     6738 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/test/utils.py
--rw-r--r--   0 domen      (501) staff       (20)     8249 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/test/tests.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/test/testcases/
--rw-r--r--   0 domen      (501) staff       (20)      767 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/test/testcases/setting_overrides.py
--rw-r--r--   0 domen      (501) staff       (20)     6640 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/test/testcases/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     9697 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/test/testcases/api.py
--rw-r--r--   0 domen      (501) staff       (20)    27330 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/test/testcases/process.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/elastic/
--rw-r--r--   0 domen      (501) staff       (20)     1535 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/elastic/signals.py
--rw-r--r--   0 domen      (501) staff       (20)     2376 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/elastic/mixins.py
--rw-r--r--   0 domen      (501) staff       (20)     3415 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/elastic/fields.py
--rw-r--r--   0 domen      (501) staff       (20)     2443 2018-04-03 11:04:23.000000 resolwe-9.0.0a3/resolwe/elastic/composer.py
--rw-r--r--   0 domen      (501) staff       (20)     9275 2018-04-23 20:32:50.000000 resolwe-9.0.0a3/resolwe/elastic/viewsets.py
--rw-r--r--   0 domen      (501) staff       (20)     5505 2018-04-19 09:44:26.000000 resolwe-9.0.0a3/resolwe/elastic/lookup.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/elastic/tests/
--rw-r--r--   0 domen      (501) staff       (20)      863 2018-04-03 11:04:23.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_composer.py
--rw-r--r--   0 domen      (501) staff       (20)    14092 2018-04-19 09:44:26.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_viewsets.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_app/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_app/migrations/
--rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_app/migrations/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     1983 2018-03-30 07:32:59.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_app/migrations/0001_initial.py
--rw-r--r--   0 domen      (501) staff       (20)      930 2018-03-30 07:32:59.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_app/models.py
--rw-r--r--   0 domen      (501) staff       (20)     1944 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_app/viewsets.py
--rw-r--r--   0 domen      (501) staff       (20)       36 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_app/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     4457 2018-03-30 07:32:59.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_app/elastic_indexes.py
--rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/elastic/tests/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)    20038 2018-04-03 11:04:23.000000 resolwe-9.0.0a3/resolwe/elastic/tests/test_index.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/elastic/management/
--rw-r--r--   0 domen      (501) staff       (20)       18 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/elastic/management/__init__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/elastic/management/commands/
--rw-r--r--   0 domen      (501) staff       (20)      383 2018-04-03 11:04:23.000000 resolwe-9.0.0a3/resolwe/elastic/management/commands/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      899 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/elastic/management/commands/elastic_purge.py
--rw-r--r--   0 domen      (501) staff       (20)      865 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/elastic/management/commands/elastic_index.py
--rw-r--r--   0 domen      (501) staff       (20)      810 2018-04-03 11:04:23.000000 resolwe-9.0.0a3/resolwe/elastic/management/commands/elastic_mapping.py
--rw-r--r--   0 domen      (501) staff       (20)      941 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/elastic/__init__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/elastic/utils/
--rw-r--r--   0 domen      (501) staff       (20)     1646 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/elastic/utils/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     1074 2018-04-06 07:17:35.000000 resolwe-9.0.0a3/resolwe/elastic/apps.py
--rw-r--r--   0 domen      (501) staff       (20)    17474 2018-04-03 11:04:23.000000 resolwe-9.0.0a3/resolwe/elastic/builder.py
--rw-r--r--   0 domen      (501) staff       (20)    14883 2018-05-09 19:54:04.000000 resolwe-9.0.0a3/resolwe/elastic/indices.py
--rw-r--r--   0 domen      (501) staff       (20)     1607 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/elastic/pagination.py
--rw-r--r--   0 domen      (501) staff       (20)      538 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/elastic/routers.py
--rw-r--r--   0 domen      (501) staff       (20)      484 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/elastic/dependencies.py
--rw-r--r--   0 domen      (501) staff       (20)      350 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      920 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/api_urls.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/permissions/
--rw-r--r--   0 domen      (501) staff       (20)     4463 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/mixins.py
--rw-r--r--   0 domen      (501) staff       (20)    16111 2018-04-12 10:11:32.000000 resolwe-9.0.0a3/resolwe/permissions/shortcuts.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/permissions/tests/
--rw-r--r--   0 domen      (501) staff       (20)     2442 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/permissions/tests/test_utils.py
--rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/tests/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     5814 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/permissions/tests/test_collection.py
--rw-r--r--   0 domen      (501) staff       (20)    27623 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/permissions/tests/test_shortcuts.py
--rw-r--r--   0 domen      (501) staff       (20)    16099 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/permissions/tests/test_data.py
--rw-r--r--   0 domen      (501) staff       (20)     1893 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/permissions/tests/test_tool.py
--rw-r--r--   0 domen      (501) staff       (20)    20990 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/permissions/tests/test_permissions.py
--rw-r--r--   0 domen      (501) staff       (20)       27 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     8056 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/permissions/utils.py
--rw-r--r--   0 domen      (501) staff       (20)     2565 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/loader.py
--rw-r--r--   0 domen      (501) staff       (20)     2606 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/permissions.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/permissions/fixtures/
--rw-r--r--   0 domen      (501) staff       (20)      700 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/fixtures/collections.yaml
--rw-r--r--   0 domen      (501) staff       (20)     5473 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/fixtures/permissions.yaml
--rw-r--r--   0 domen      (501) staff       (20)     2071 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/fixtures/users.yaml
--rw-r--r--   0 domen      (501) staff       (20)     1231 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/fixtures/processes.yaml
--rw-r--r--   0 domen      (501) staff       (20)      792 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/permissions/fixtures/data.yaml
--rw-r--r--   0 domen      (501) staff       (20)     5489 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/fixtures/readme.txt
--rw-r--r--   0 domen      (501) staff       (20)      963 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/permissions/filters.py
--rw-r--r--   0 domen      (501) staff       (20)     1025 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/utils.py
--rw-r--r--   0 domen      (501) staff       (20)      779 2018-05-09 21:09:45.000000 resolwe-9.0.0a3/resolwe/__about__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/test_helpers/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/test_helpers/management/
--rw-r--r--   0 domen      (501) staff       (20)      250 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/test_helpers/management/__init__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/test_helpers/management/commands/
--rw-r--r--   0 domen      (501) staff       (20)       34 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/test_helpers/management/commands/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     2194 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/test_helpers/management/commands/show_profile.py
--rw-r--r--   0 domen      (501) staff       (20)       99 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/test_helpers/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)    26845 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/test_helpers/test_runner.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/toolkit/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/toolkit/tools/
--rwxr-xr-x   0 domen      (501) staff       (20)     1681 2017-12-26 13:24:10.000000 resolwe-9.0.0a3/resolwe/toolkit/tools/parse_tabular_file.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/toolkit/processes/
--rw-r--r--   0 domen      (501) staff       (20)     3236 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/toolkit/processes/files.yml
--rw-r--r--   0 domen      (501) staff       (20)     1310 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/toolkit/processes/archiver.yml
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/
--rw-r--r--   0 domen      (501) staff       (20)      890 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/test_archiver.py
--rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     2232 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/test_files.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/
--rw-r--r--   0 domen      (501) staff       (20)       81 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/tab_file_tabular.tab.gz
--rw-r--r--   0 domen      (501) staff       (20)     6865 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/file binary
--rw-r--r--   0 domen      (501) staff       (20)       80 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/xlsx_file_tabular.tab.gz
--rw-r--r--   0 domen      (501) staff       (20)     6865 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/file image.png
--rw-r--r--   0 domen      (501) staff       (20)     5269 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/file tab.1.xlsx
--rw-r--r--   0 domen      (501) staff       (20)       73 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/csv_file_tabular.tab.gz
--rw-r--r--   0 domen      (501) staff       (20)       67 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/file tab.csv.gz
--rw-r--r--   0 domen      (501) staff       (20)    19968 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/file tab.xls
--rw-r--r--   0 domen      (501) staff       (20)       66 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/file tab.tab.gz
--rw-r--r--   0 domen      (501) staff       (20)       78 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/xls_file_tabular.tab.gz
--rw-r--r--   0 domen      (501) staff       (20)       33 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/tests/files/file tab.txt
--rw-r--r--   0 domen      (501) staff       (20)      170 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/__init__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/archiver/
--rw-r--r--   0 domen      (501) staff       (20)      188 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/archiver/Dockerfile
--rw-r--r--   0 domen      (501) staff       (20)      131 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/archiver/README.md
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/upload-tab-file/
--rw-r--r--   0 domen      (501) staff       (20)      197 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/upload-tab-file/Dockerfile
--rw-r--r--   0 domen      (501) staff       (20)      138 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/upload-tab-file/README.md
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/
--rw-r--r--   0 domen      (501) staff       (20)     1236 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-16.04
--rw-r--r--   0 domen      (501) staff       (20)     1236 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-17.10
--rw-r--r--   0 domen      (501) staff       (20)     1236 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-18.04
--rw-r--r--   0 domen      (501) staff       (20)     5093 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/re-import.sh
--rw-r--r--   0 domen      (501) staff       (20)      652 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/README.md
--rw-r--r--   0 domen      (501) staff       (20)      874 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.fedora-26
--rw-r--r--   0 domen      (501) staff       (20)      773 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/curlprogress.py
--rw-r--r--   0 domen      (501) staff       (20)     1236 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-14.04
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/rest/
--rw-r--r--   0 domen      (501) staff       (20)      543 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/rest/fields.py
--rw-r--r--   0 domen      (501) staff       (20)      529 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/rest/serializers.py
--rw-r--r--   0 domen      (501) staff       (20)       32 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/rest/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     3628 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/rest/tests.py
--rw-r--r--   0 domen      (501) staff       (20)     3098 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/rest/projection.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/
--rw-r--r--   0 domen      (501) staff       (20)     1533 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/signals.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/migrations/
--rw-r--r--   0 domen      (501) staff       (20)     1763 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0013_migration_history.py
--rw-r--r--   0 domen      (501) staff       (20)     3133 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0015_make_data_indexes.py
--rw-r--r--   0 domen      (501) staff       (20)     1268 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0010_add_secret.py
--rw-r--r--   0 domen      (501) staff       (20)      636 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0022_data_sha1_to_sha256.py
--rw-r--r--   0 domen      (501) staff       (20)     2430 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0014_add_entity.py
--rw-r--r--   0 domen      (501) staff       (20)      454 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0019_data_descriptor_dirty.py
--rw-r--r--   0 domen      (501) staff       (20)     3725 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0024_add_relations.py
--rw-r--r--   0 domen      (501) staff       (20)     2417 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0025_set_get_last_by.py
--rw-r--r--   0 domen      (501) staff       (20)      626 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0012_require_checksum.py
--rw-r--r--   0 domen      (501) staff       (20)     2199 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0008_fix_jsonfields.py
--rw-r--r--   0 domen      (501) staff       (20)      612 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0027_scheduling_class.py
--rw-r--r--   0 domen      (501) staff       (20)      626 2018-03-27 07:51:11.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0014_track_resources.py
--rw-r--r--   0 domen      (501) staff       (20)     1686 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0004_autoslug_field.py
--rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/migrations/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      576 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0011_preserve_parents.py
--rw-r--r--   0 domen      (501) staff       (20)      514 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0010_fix_jsonfields.py
--rw-r--r--   0 domen      (501) staff       (20)      832 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0008_compute_size.py
--rw-r--r--   0 domen      (501) staff       (20)      627 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0017_update_checksum.py
--rw-r--r--   0 domen      (501) staff       (20)     1445 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0005_data_dependency_3.py
--rw-r--r--   0 domen      (501) staff       (20)     1336 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0002_set_process_owners.py
--rw-r--r--   0 domen      (501) staff       (20)     1663 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0006_add_total_size.py
--rw-r--r--   0 domen      (501) staff       (20)      647 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0029_data_checksum_index.py
--rw-r--r--   0 domen      (501) staff       (20)     1525 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0003_data_dependency_1.py
--rw-r--r--   0 domen      (501) staff       (20)      472 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0009_data_parents.py
--rw-r--r--   0 domen      (501) staff       (20)      786 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0026_tags.py
--rw-r--r--   0 domen      (501) staff       (20)     2029 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0007_add_owner.py
--rw-r--r--   0 domen      (501) staff       (20)    18280 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0001_squashed_0030_change_slug_field.py
--rw-r--r--   0 domen      (501) staff       (20)      515 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0028_remove_public_processes.py
--rw-r--r--   0 domen      (501) staff       (20)      472 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0021_entity_descriptor_completed.py
--rw-r--r--   0 domen      (501) staff       (20)     1476 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0016_update_versionfield.py
--rw-r--r--   0 domen      (501) staff       (20)      628 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0023_update_checksum.py
--rw-r--r--   0 domen      (501) staff       (20)      431 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0009_make_size_mandatory.py
--rw-r--r--   0 domen      (501) staff       (20)    11468 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0001_initial.py
--rw-r--r--   0 domen      (501) staff       (20)      467 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0005_process_data_name.py
--rw-r--r--   0 domen      (501) staff       (20)      930 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0002_project_to_collection.py
--rw-r--r--   0 domen      (501) staff       (20)      452 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0007_data_size.py
--rw-r--r--   0 domen      (501) staff       (20)     1201 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0004_data_dependency_2.py
--rw-r--r--   0 domen      (501) staff       (20)      991 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0003_support_sample.py
--rw-r--r--   0 domen      (501) staff       (20)      793 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0018_remove_triggers.py
--rw-r--r--   0 domen      (501) staff       (20)      630 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0020_collection_descriptor_dirty.py
--rw-r--r--   0 domen      (501) staff       (20)      515 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0013_add_requirements.py
--rw-r--r--   0 domen      (501) staff       (20)      450 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0006_data_named_by_user.py
--rw-r--r--   0 domen      (501) staff       (20)      622 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0011_calculate_checksum.py
--rw-r--r--   0 domen      (501) staff       (20)     1308 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0012_recreate_empty_parents.py
--rw-r--r--   0 domen      (501) staff       (20)     1927 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migrations/0030_change_slug_field.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/expression_engines/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/expression_engines/jinja/
--rw-r--r--   0 domen      (501) staff       (20)     6535 2018-02-05 10:50:16.000000 resolwe-9.0.0a3/resolwe/flow/expression_engines/jinja/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     3361 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/expression_engines/jinja/filters.py
--rw-r--r--   0 domen      (501) staff       (20)      180 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/expression_engines/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      243 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/expression_engines/exceptions.py
--rw-r--r--   0 domen      (501) staff       (20)      876 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/expression_engines/base.py
--rw-r--r--   0 domen      (501) staff       (20)      686 2018-03-27 07:24:44.000000 resolwe-9.0.0a3/resolwe/flow/tasks.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/elastic_indexes/
--rw-r--r--   0 domen      (501) staff       (20)       92 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/elastic_indexes/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     2367 2018-04-23 20:33:01.000000 resolwe-9.0.0a3/resolwe/flow/elastic_indexes/base.py
--rw-r--r--   0 domen      (501) staff       (20)     2161 2018-05-09 21:04:27.000000 resolwe-9.0.0a3/resolwe/flow/elastic_indexes/data.py
--rw-r--r--   0 domen      (501) staff       (20)     2431 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/finders.py
--rw-r--r--   0 domen      (501) staff       (20)    12328 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/serializers.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/managers/
--rw-r--r--   0 domen      (501) staff       (20)    37847 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/managers/dispatcher.py
--rw-r--r--   0 domen      (501) staff       (20)     1334 2018-03-26 07:08:26.000000 resolwe-9.0.0a3/resolwe/flow/managers/protocol.py
--rw-r--r--   0 domen      (501) staff       (20)      142 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/managers/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      680 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/managers/consumer.py
--rw-r--r--   0 domen      (501) staff       (20)      418 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/managers/utils.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/
--rw-r--r--   0 domen      (501) staff       (20)     2172 2018-03-27 07:24:44.000000 resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/slurm.py
--rw-r--r--   0 domen      (501) staff       (20)      943 2018-03-27 07:24:44.000000 resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/local.py
--rw-r--r--   0 domen      (501) staff       (20)      282 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     1430 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/celery.py
--rw-r--r--   0 domen      (501) staff       (20)     1088 2018-03-27 07:24:44.000000 resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/base.py
--rw-r--r--   0 domen      (501) staff       (20)     9939 2018-04-12 10:11:32.000000 resolwe-9.0.0a3/resolwe/flow/managers/state.py
--rw-r--r--   0 domen      (501) staff       (20)    20549 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/managers/listener.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/
--rw-r--r--   0 domen      (501) staff       (20)     9253 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_expression_filters.py
--rw-r--r--   0 domen      (501) staff       (20)      657 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_resources.py
--rw-r--r--   0 domen      (501) staff       (20)     1938 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_utils.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/fields_test_app/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/fields_test_app/migrations/
--rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/fields_test_app/migrations/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      753 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/fields_test_app/migrations/0001_initial.py
--rw-r--r--   0 domen      (501) staff       (20)      441 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/fields_test_app/models.py
--rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/fields_test_app/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     3554 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_serializers.py
--rw-r--r--   0 domen      (501) staff       (20)    37074 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_validation.py
--rw-r--r--   0 domen      (501) staff       (20)     5261 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_access_api.py
--rw-r--r--   0 domen      (501) staff       (20)     1784 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_env_vars.py
--rw-r--r--   0 domen      (501) staff       (20)    11417 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_executors.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/
--rw-r--r--   0 domen      (501) staff       (20)      814 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/secrets.yml
--rw-r--r--   0 domen      (501) staff       (20)     1556 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/workflow.yml
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/second_version/
--rw-r--r--   0 domen      (501) staff       (20)      154 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/second_version/tests.yml
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/first_version/
--rw-r--r--   0 domen      (501) staff       (20)      154 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/first_version/tests.yml
--rw-r--r--   0 domen      (501) staff       (20)     1240 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/spawned.yml
--rw-r--r--   0 domen      (501) staff       (20)    12888 2018-04-12 09:00:05.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/tests.yml
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/wrong_defaults/
--rw-r--r--   0 domen      (501) staff       (20)      512 2018-04-12 09:00:05.000000 resolwe-9.0.0a3/resolwe/flow/tests/processes/wrong_defaults/tests.yml
--rw-r--r--   0 domen      (501) staff       (20)     1774 2018-02-15 20:36:59.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_docs.py
--rw-r--r--   0 domen      (501) staff       (20)     1252 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_runtime.py
--rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     7680 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_commands.py
--rw-r--r--   0 domen      (501) staff       (20)     3857 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_fields.py
--rw-r--r--   0 domen      (501) staff       (20)    28889 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_models.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/files/
--rw-r--r--   0 domen      (501) staff       (20)       65 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/files/contents.rst
--rw-r--r--   0 domen      (501) staff       (20)        0 2018-04-20 10:45:41.000000 resolwe-9.0.0a3/resolwe/flow/tests/files/errors.txt
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/files/processes/
--rw-r--r--   0 domen      (501) staff       (20)     4705 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/files/processes/test.yaml
--rw-r--r--   0 domen      (501) staff       (20)      501 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/files/conf.py
--rw-r--r--   0 domen      (501) staff       (20)     2348 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_secrets.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/tests/fixtures/
--rw-r--r--   0 domen      (501) staff       (20)      161 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/fixtures/relationtypes.yaml
--rw-r--r--   0 domen      (501) staff       (20)    35653 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_api.py
--rw-r--r--   0 domen      (501) staff       (20)     7515 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_manager.py
--rw-r--r--   0 domen      (501) staff       (20)     1364 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_descriptors.py
--rw-r--r--   0 domen      (501) staff       (20)      819 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_tool.py
--rw-r--r--   0 domen      (501) staff       (20)      323 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/tests/expression_filters.py
--rw-r--r--   0 domen      (501) staff       (20)    16353 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_purge.py
--rw-r--r--   0 domen      (501) staff       (20)    11595 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_relations.py
--rw-r--r--   0 domen      (501) staff       (20)     1486 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_ordering.py
--rw-r--r--   0 domen      (501) staff       (20)    11554 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/tests/test_filtering.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/management/
--rw-r--r--   0 domen      (501) staff       (20)      227 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/management/__init__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/management/commands/
--rw-r--r--   0 domen      (501) staff       (20)    13791 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/management/commands/register.py
--rw-r--r--   0 domen      (501) staff       (20)       34 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/management/commands/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      806 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/management/commands/purge.py
--rw-r--r--   0 domen      (501) staff       (20)     4613 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/management/commands/collecttools.py
--rw-r--r--   0 domen      (501) staff       (20)     5129 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/management/commands/list_docker_images.py
--rw-r--r--   0 domen      (501) staff       (20)     1210 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/management/commands/runlistener.py
--rw-r--r--   0 domen      (501) staff       (20)      219 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/__init__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/utils/
--rw-r--r--   0 domen      (501) staff       (20)     3237 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/utils/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     5714 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/utils/purge.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/utils/docs/
--rw-r--r--   0 domen      (501) staff       (20)    15698 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/utils/docs/autoprocess.py
--rw-r--r--   0 domen      (501) staff       (20)       25 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/utils/docs/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     3086 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/utils/iterators.py
--rw-r--r--   0 domen      (501) staff       (20)      985 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/utils/exceptions.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/models/
--rw-r--r--   0 domen      (501) staff       (20)      894 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/descriptor.py
--rw-r--r--   0 domen      (501) staff       (20)     1173 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/functions.py
--rw-r--r--   0 domen      (501) staff       (20)     7771 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/fields.py
--rw-r--r--   0 domen      (501) staff       (20)     1841 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     2310 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/secret.py
--rw-r--r--   0 domen      (501) staff       (20)    22760 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/utils.py
--rw-r--r--   0 domen      (501) staff       (20)     2213 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/storage.py
--rw-r--r--   0 domen      (501) staff       (20)     2156 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/collection.py
--rw-r--r--   0 domen      (501) staff       (20)     1095 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/migrations.py
--rw-r--r--   0 domen      (501) staff       (20)     2846 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/entity.py
--rw-r--r--   0 domen      (501) staff       (20)     6079 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/process.py
--rw-r--r--   0 domen      (501) staff       (20)     2074 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/base.py
--rw-r--r--   0 domen      (501) staff       (20)    17503 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/models/data.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/execution_engines/
--rw-r--r--   0 domen      (501) staff       (20)      175 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/execution_engines/__init__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/execution_engines/bash/
--rw-r--r--   0 domen      (501) staff       (20)     2433 2018-05-09 19:54:04.000000 resolwe-9.0.0a3/resolwe/flow/execution_engines/bash/__init__.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/execution_engines/workflow/
--rw-r--r--   0 domen      (501) staff       (20)     4790 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/execution_engines/workflow/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      247 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/execution_engines/exceptions.py
--rw-r--r--   0 domen      (501) staff       (20)      658 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/execution_engines/base.py
--rw-r--r--   0 domen      (501) staff       (20)      557 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/apps.py
--rw-r--r--   0 domen      (501) staff       (20)     3434 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/engine.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/executors/
--rw-r--r--   0 domen      (501) staff       (20)    10265 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/run.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/executors/docker/
--rw-r--r--   0 domen      (501) staff       (20)    40139 2017-12-26 18:16:18.000000 resolwe-9.0.0a3/resolwe/flow/executors/docker/seccomp.py
--rw-r--r--   0 domen      (501) staff       (20)     9305 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/docker/run.py
--rw-r--r--   0 domen      (501) staff       (20)      251 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/executors/docker/constants.py
--rw-r--r--   0 domen      (501) staff       (20)      204 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/docker/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     1906 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/executors/docker/prepare.py
--rw-r--r--   0 domen      (501) staff       (20)       74 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/executors/requirements.txt
--rw-r--r--   0 domen      (501) staff       (20)     1334 2018-03-26 07:08:26.000000 resolwe-9.0.0a3/resolwe/flow/executors/protocol.py
--rw-r--r--   0 domen      (501) staff       (20)      265 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     1044 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/global_settings.py
--rw-r--r--   0 domen      (501) staff       (20)     2503 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/logger.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/executors/local/
--rw-r--r--   0 domen      (501) staff       (20)     1577 2018-03-26 07:08:26.000000 resolwe-9.0.0a3/resolwe/flow/executors/local/run.py
--rw-r--r--   0 domen      (501) staff       (20)      199 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/local/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)     1028 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/local/prepare.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/executors/null/
--rw-r--r--   0 domen      (501) staff       (20)      718 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/null/run.py
--rw-r--r--   0 domen      (501) staff       (20)      194 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/null/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      399 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/executors/null/prepare.py
--rw-r--r--   0 domen      (501) staff       (20)     2763 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/manager_commands.py
--rw-r--r--   0 domen      (501) staff       (20)     1622 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/__main__.py
--rw-r--r--   0 domen      (501) staff       (20)     3721 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/executors/prepare.py
--rw-r--r--   0 domen      (501) staff       (20)      341 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/resolwe/flow/routing.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/static/
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/static/flow/
--rw-r--r--   0 domen      (501) staff       (20)    14118 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/static/flow/typeSchema.json
--rw-r--r--   0 domen      (501) staff       (20)      971 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/static/flow/descriptorSchema.json
--rw-r--r--   0 domen      (501) staff       (20)    15461 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/static/flow/fieldSchema.json
--rw-r--r--   0 domen      (501) staff       (20)     5790 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/static/flow/processSchema.json
--rw-r--r--   0 domen      (501) staff       (20)    22286 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/migration_ops.py
-drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-09 21:10:30.000000 resolwe-9.0.0a3/resolwe/flow/views/
--rw-r--r--   0 domen      (501) staff       (20)     1053 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/views/descriptor.py
--rw-r--r--   0 domen      (501) staff       (20)     5569 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/views/relation.py
--rw-r--r--   0 domen      (501) staff       (20)     7277 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/views/mixins.py
--rw-r--r--   0 domen      (501) staff       (20)      933 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/views/__init__.py
--rw-r--r--   0 domen      (501) staff       (20)      623 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/views/storage.py
--rw-r--r--   0 domen      (501) staff       (20)     4551 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/views/collection.py
--rw-r--r--   0 domen      (501) staff       (20)     6025 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/views/entity.py
--rw-r--r--   0 domen      (501) staff       (20)     1376 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/views/process.py
--rw-r--r--   0 domen      (501) staff       (20)     9492 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/views/data.py
--rw-r--r--   0 domen      (501) staff       (20)     3670 2018-04-16 07:58:52.000000 resolwe-9.0.0a3/resolwe/flow/filters.py
--rw-r--r--   0 domen      (501) staff       (20)     3854 2018-03-20 12:27:36.000000 resolwe-9.0.0a3/README.rst
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/
+-rw-r--r--   0 domen      (501) staff       (20)     6003 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/PKG-INFO
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe.egg-info/
+-rw-r--r--   0 domen      (501) staff       (20)     6003 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe.egg-info/PKG-INFO
+-rw-r--r--   0 domen      (501) staff       (20)    12156 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe.egg-info/SOURCES.txt
+-rw-r--r--   0 domen      (501) staff       (20)      674 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe.egg-info/requires.txt
+-rw-r--r--   0 domen      (501) staff       (20)        8 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe.egg-info/top_level.txt
+-rw-r--r--   0 domen      (501) staff       (20)        1 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe.egg-info/dependency_links.txt
+-rw-r--r--   0 domen      (501) staff       (20)    10153 2018-04-12 10:11:32.000000 resolwe-9.0.0a4/.pylintrc
+-rw-r--r--   0 domen      (501) staff       (20)    11358 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/LICENSE
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/tests/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/tests/.test_data/
+-rw-r--r--   0 domen      (501) staff       (20)      118 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/tests/.test_data/README.rst
+-rw-r--r--   0 domen      (501) staff       (20)      236 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/tests/__init__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/tests/.test_runtime/
+-rw-r--r--   0 domen      (501) staff       (20)      118 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/tests/.test_runtime/README.rst
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/tests/.test_upload/
+-rw-r--r--   0 domen      (501) staff       (20)      118 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/tests/.test_upload/README.rst
+-rw-r--r--   0 domen      (501) staff       (20)      348 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/tests/.env
+-rw-r--r--   0 domen      (501) staff       (20)     6930 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/tests/settings.py
+-rw-r--r--   0 domen      (501) staff       (20)      457 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/tests/celery_conf.py
+-rw-r--r--   0 domen      (501) staff       (20)     1007 2018-03-30 07:32:59.000000 resolwe-9.0.0a4/tests/docker-compose.yml
+-rwxr-xr-x   0 domen      (501) staff       (20)      834 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/tests/manage.py
+-rw-r--r--   0 domen      (501) staff       (20)      273 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/tests/urls.py
+-rw-r--r--   0 domen      (501) staff       (20)     1163 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/MANIFEST.in
+-rw-r--r--   0 domen      (501) staff       (20)       67 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/.coveragerc
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/docs/
+-rw-r--r--   0 domen      (501) staff       (20)      717 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/docs/index.rst
+-rw-r--r--   0 domen      (501) staff       (20)     3776 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/docs/contributing.rst
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/docs/images/
+-rw-r--r--   0 domen      (501) staff       (20)    11809 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/images/resolwe_02_internals.png
+-rw-r--r--   0 domen      (501) staff       (20)    18436 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/images/proc_02_flow.png
+-rw-r--r--   0 domen      (501) staff       (20)    23450 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/images/proc_03_types.png
+-rw-r--r--   0 domen      (501) staff       (20)    13981 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/images/resolwe_01_context.png
+-rw-r--r--   0 domen      (501) staff       (20)     7006 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/images/proc_01.png
+-rw-r--r--   0 domen      (501) staff       (20)    12023 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/images/resolwe_04_workers.png
+-rw-r--r--   0 domen      (501) staff       (20)    17823 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/docs/images/resolwe_03_workflow.png
+-rw-r--r--   0 domen      (501) staff       (20)      272 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/intro.rst
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/docs/example/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/docs/example/example/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/docs/example/example/processes/
+-rw-r--r--   0 domen      (501) staff       (20)      185 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/example/example/processes/minimal.yml
+-rw-r--r--   0 domen      (501) staff       (20)      815 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/example/example/processes/example.yml
+-rw-r--r--   0 domen      (501) staff       (20)      162 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/example/example/processes/all_fields.yml
+-rw-r--r--   0 domen      (501) staff       (20)      271 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/example/example/processes/example_basic.yml
+-rw-r--r--   0 domen      (501) staff       (20)     3081 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/conf.py
+-rw-r--r--   0 domen      (501) staff       (20)     1693 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/docs/overview.rst
+-rw-r--r--   0 domen      (501) staff       (20)    24381 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/docs/proc.rst
+-rw-r--r--   0 domen      (501) staff       (20)     3730 2018-03-30 07:32:59.000000 resolwe-9.0.0a4/docs/composer.rst
+-rw-r--r--   0 domen      (501) staff       (20)      373 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/docs/ref.rst
+-rw-r--r--   0 domen      (501) staff       (20)    10920 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/docs/flow.rst
+-rw-r--r--   0 domen      (501) staff       (20)    25845 2018-05-14 09:57:58.000000 resolwe-9.0.0a4/docs/CHANGELOG.rst
+-rw-r--r--   0 domen      (501) staff       (20)     3013 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/docs/api.rst
+-rw-r--r--   0 domen      (501) staff       (20)     4023 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/setup.py
+-rw-r--r--   0 domen      (501) staff       (20)     2698 2018-04-12 10:11:32.000000 resolwe-9.0.0a4/tox.ini
+-rw-r--r--   0 domen      (501) staff       (20)      557 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/setup.cfg
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/test/
+-rw-r--r--   0 domen      (501) staff       (20)     1115 2018-03-30 07:32:59.000000 resolwe-9.0.0a4/resolwe/test/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     6738 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/test/utils.py
+-rw-r--r--   0 domen      (501) staff       (20)     8249 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/test/tests.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/test/testcases/
+-rw-r--r--   0 domen      (501) staff       (20)      767 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/test/testcases/setting_overrides.py
+-rw-r--r--   0 domen      (501) staff       (20)     6640 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/test/testcases/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     9697 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/test/testcases/api.py
+-rw-r--r--   0 domen      (501) staff       (20)    27330 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/test/testcases/process.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/elastic/
+-rw-r--r--   0 domen      (501) staff       (20)     1535 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/elastic/signals.py
+-rw-r--r--   0 domen      (501) staff       (20)     2376 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/elastic/mixins.py
+-rw-r--r--   0 domen      (501) staff       (20)     3415 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/elastic/fields.py
+-rw-r--r--   0 domen      (501) staff       (20)     2443 2018-04-03 11:04:23.000000 resolwe-9.0.0a4/resolwe/elastic/composer.py
+-rw-r--r--   0 domen      (501) staff       (20)     9275 2018-04-23 20:32:50.000000 resolwe-9.0.0a4/resolwe/elastic/viewsets.py
+-rw-r--r--   0 domen      (501) staff       (20)     5505 2018-04-19 09:44:26.000000 resolwe-9.0.0a4/resolwe/elastic/lookup.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/elastic/tests/
+-rw-r--r--   0 domen      (501) staff       (20)      863 2018-04-03 11:04:23.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_composer.py
+-rw-r--r--   0 domen      (501) staff       (20)    14092 2018-04-19 09:44:26.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_viewsets.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_app/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_app/migrations/
+-rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_app/migrations/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     1983 2018-03-30 07:32:59.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_app/migrations/0001_initial.py
+-rw-r--r--   0 domen      (501) staff       (20)      930 2018-03-30 07:32:59.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_app/models.py
+-rw-r--r--   0 domen      (501) staff       (20)     1944 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_app/viewsets.py
+-rw-r--r--   0 domen      (501) staff       (20)       36 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_app/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     4457 2018-03-30 07:32:59.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_app/elastic_indexes.py
+-rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/elastic/tests/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)    20038 2018-04-03 11:04:23.000000 resolwe-9.0.0a4/resolwe/elastic/tests/test_index.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/elastic/management/
+-rw-r--r--   0 domen      (501) staff       (20)       18 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/elastic/management/__init__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/elastic/management/commands/
+-rw-r--r--   0 domen      (501) staff       (20)      383 2018-04-03 11:04:23.000000 resolwe-9.0.0a4/resolwe/elastic/management/commands/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      899 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/elastic/management/commands/elastic_purge.py
+-rw-r--r--   0 domen      (501) staff       (20)      865 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/elastic/management/commands/elastic_index.py
+-rw-r--r--   0 domen      (501) staff       (20)      810 2018-04-03 11:04:23.000000 resolwe-9.0.0a4/resolwe/elastic/management/commands/elastic_mapping.py
+-rw-r--r--   0 domen      (501) staff       (20)      941 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/elastic/__init__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/elastic/utils/
+-rw-r--r--   0 domen      (501) staff       (20)     1646 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/elastic/utils/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     1074 2018-04-06 07:17:35.000000 resolwe-9.0.0a4/resolwe/elastic/apps.py
+-rw-r--r--   0 domen      (501) staff       (20)    17721 2018-05-14 09:57:58.000000 resolwe-9.0.0a4/resolwe/elastic/builder.py
+-rw-r--r--   0 domen      (501) staff       (20)    14816 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/resolwe/elastic/indices.py
+-rw-r--r--   0 domen      (501) staff       (20)     1607 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/elastic/pagination.py
+-rw-r--r--   0 domen      (501) staff       (20)      538 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/elastic/routers.py
+-rw-r--r--   0 domen      (501) staff       (20)      484 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/elastic/dependencies.py
+-rw-r--r--   0 domen      (501) staff       (20)      350 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      920 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/api_urls.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/permissions/
+-rw-r--r--   0 domen      (501) staff       (20)     4463 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/mixins.py
+-rw-r--r--   0 domen      (501) staff       (20)    16111 2018-04-12 10:11:32.000000 resolwe-9.0.0a4/resolwe/permissions/shortcuts.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/permissions/tests/
+-rw-r--r--   0 domen      (501) staff       (20)     2442 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/permissions/tests/test_utils.py
+-rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/tests/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     5814 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/permissions/tests/test_collection.py
+-rw-r--r--   0 domen      (501) staff       (20)    27623 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/permissions/tests/test_shortcuts.py
+-rw-r--r--   0 domen      (501) staff       (20)    16099 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/permissions/tests/test_data.py
+-rw-r--r--   0 domen      (501) staff       (20)     1893 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/permissions/tests/test_tool.py
+-rw-r--r--   0 domen      (501) staff       (20)    20990 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/permissions/tests/test_permissions.py
+-rw-r--r--   0 domen      (501) staff       (20)       27 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     8056 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/permissions/utils.py
+-rw-r--r--   0 domen      (501) staff       (20)     2565 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/loader.py
+-rw-r--r--   0 domen      (501) staff       (20)     2606 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/permissions.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/permissions/fixtures/
+-rw-r--r--   0 domen      (501) staff       (20)      700 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/fixtures/collections.yaml
+-rw-r--r--   0 domen      (501) staff       (20)     5473 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/fixtures/permissions.yaml
+-rw-r--r--   0 domen      (501) staff       (20)     2071 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/fixtures/users.yaml
+-rw-r--r--   0 domen      (501) staff       (20)     1231 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/fixtures/processes.yaml
+-rw-r--r--   0 domen      (501) staff       (20)      792 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/permissions/fixtures/data.yaml
+-rw-r--r--   0 domen      (501) staff       (20)     5489 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/fixtures/readme.txt
+-rw-r--r--   0 domen      (501) staff       (20)      963 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/permissions/filters.py
+-rw-r--r--   0 domen      (501) staff       (20)     1025 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/utils.py
+-rw-r--r--   0 domen      (501) staff       (20)      779 2018-05-14 10:01:14.000000 resolwe-9.0.0a4/resolwe/__about__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/test_helpers/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/test_helpers/management/
+-rw-r--r--   0 domen      (501) staff       (20)      250 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/test_helpers/management/__init__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/test_helpers/management/commands/
+-rw-r--r--   0 domen      (501) staff       (20)       34 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/test_helpers/management/commands/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     2194 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/test_helpers/management/commands/show_profile.py
+-rw-r--r--   0 domen      (501) staff       (20)       99 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/test_helpers/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)    26845 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/resolwe/test_helpers/test_runner.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/toolkit/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/toolkit/tools/
+-rwxr-xr-x   0 domen      (501) staff       (20)     1681 2017-12-26 13:24:10.000000 resolwe-9.0.0a4/resolwe/toolkit/tools/parse_tabular_file.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/toolkit/processes/
+-rw-r--r--   0 domen      (501) staff       (20)     3236 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/toolkit/processes/files.yml
+-rw-r--r--   0 domen      (501) staff       (20)     1310 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/toolkit/processes/archiver.yml
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/
+-rw-r--r--   0 domen      (501) staff       (20)      890 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/test_archiver.py
+-rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     2232 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/test_files.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/
+-rw-r--r--   0 domen      (501) staff       (20)       81 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/tab_file_tabular.tab.gz
+-rw-r--r--   0 domen      (501) staff       (20)     6865 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/file binary
+-rw-r--r--   0 domen      (501) staff       (20)       80 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/xlsx_file_tabular.tab.gz
+-rw-r--r--   0 domen      (501) staff       (20)     6865 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/file image.png
+-rw-r--r--   0 domen      (501) staff       (20)     5269 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/file tab.1.xlsx
+-rw-r--r--   0 domen      (501) staff       (20)       73 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/csv_file_tabular.tab.gz
+-rw-r--r--   0 domen      (501) staff       (20)       67 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/file tab.csv.gz
+-rw-r--r--   0 domen      (501) staff       (20)    19968 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/file tab.xls
+-rw-r--r--   0 domen      (501) staff       (20)       66 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/file tab.tab.gz
+-rw-r--r--   0 domen      (501) staff       (20)       78 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/xls_file_tabular.tab.gz
+-rw-r--r--   0 domen      (501) staff       (20)       33 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/tests/files/file tab.txt
+-rw-r--r--   0 domen      (501) staff       (20)      170 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/__init__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/archiver/
+-rw-r--r--   0 domen      (501) staff       (20)      188 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/archiver/Dockerfile
+-rw-r--r--   0 domen      (501) staff       (20)      131 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/archiver/README.md
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/upload-tab-file/
+-rw-r--r--   0 domen      (501) staff       (20)      197 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/upload-tab-file/Dockerfile
+-rw-r--r--   0 domen      (501) staff       (20)      138 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/upload-tab-file/README.md
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/
+-rw-r--r--   0 domen      (501) staff       (20)     1236 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-16.04
+-rw-r--r--   0 domen      (501) staff       (20)     1236 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-17.10
+-rw-r--r--   0 domen      (501) staff       (20)     1236 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-18.04
+-rw-r--r--   0 domen      (501) staff       (20)     5093 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/re-import.sh
+-rw-r--r--   0 domen      (501) staff       (20)      652 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/README.md
+-rw-r--r--   0 domen      (501) staff       (20)      874 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.fedora-26
+-rw-r--r--   0 domen      (501) staff       (20)      773 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/curlprogress.py
+-rw-r--r--   0 domen      (501) staff       (20)     1236 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-14.04
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/rest/
+-rw-r--r--   0 domen      (501) staff       (20)      543 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/rest/fields.py
+-rw-r--r--   0 domen      (501) staff       (20)      529 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/rest/serializers.py
+-rw-r--r--   0 domen      (501) staff       (20)       32 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/rest/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     3628 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/rest/tests.py
+-rw-r--r--   0 domen      (501) staff       (20)     3098 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/rest/projection.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/
+-rw-r--r--   0 domen      (501) staff       (20)     1533 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/signals.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/migrations/
+-rw-r--r--   0 domen      (501) staff       (20)     1763 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0013_migration_history.py
+-rw-r--r--   0 domen      (501) staff       (20)     3133 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0015_make_data_indexes.py
+-rw-r--r--   0 domen      (501) staff       (20)     1268 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0010_add_secret.py
+-rw-r--r--   0 domen      (501) staff       (20)      636 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0022_data_sha1_to_sha256.py
+-rw-r--r--   0 domen      (501) staff       (20)     2430 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0014_add_entity.py
+-rw-r--r--   0 domen      (501) staff       (20)      454 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0019_data_descriptor_dirty.py
+-rw-r--r--   0 domen      (501) staff       (20)     3725 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0024_add_relations.py
+-rw-r--r--   0 domen      (501) staff       (20)     2417 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0025_set_get_last_by.py
+-rw-r--r--   0 domen      (501) staff       (20)      626 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0012_require_checksum.py
+-rw-r--r--   0 domen      (501) staff       (20)     2199 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0008_fix_jsonfields.py
+-rw-r--r--   0 domen      (501) staff       (20)      612 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0027_scheduling_class.py
+-rw-r--r--   0 domen      (501) staff       (20)      626 2018-03-27 07:51:11.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0014_track_resources.py
+-rw-r--r--   0 domen      (501) staff       (20)     1686 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0004_autoslug_field.py
+-rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/migrations/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      576 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0011_preserve_parents.py
+-rw-r--r--   0 domen      (501) staff       (20)      514 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0010_fix_jsonfields.py
+-rw-r--r--   0 domen      (501) staff       (20)      832 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0008_compute_size.py
+-rw-r--r--   0 domen      (501) staff       (20)      627 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0017_update_checksum.py
+-rw-r--r--   0 domen      (501) staff       (20)     1445 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0005_data_dependency_3.py
+-rw-r--r--   0 domen      (501) staff       (20)     1336 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0002_set_process_owners.py
+-rw-r--r--   0 domen      (501) staff       (20)     1663 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0006_add_total_size.py
+-rw-r--r--   0 domen      (501) staff       (20)      647 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0029_data_checksum_index.py
+-rw-r--r--   0 domen      (501) staff       (20)     1525 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0003_data_dependency_1.py
+-rw-r--r--   0 domen      (501) staff       (20)      472 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0009_data_parents.py
+-rw-r--r--   0 domen      (501) staff       (20)      786 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0026_tags.py
+-rw-r--r--   0 domen      (501) staff       (20)     2029 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0007_add_owner.py
+-rw-r--r--   0 domen      (501) staff       (20)    18280 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0001_squashed_0030_change_slug_field.py
+-rw-r--r--   0 domen      (501) staff       (20)      515 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0028_remove_public_processes.py
+-rw-r--r--   0 domen      (501) staff       (20)      472 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0021_entity_descriptor_completed.py
+-rw-r--r--   0 domen      (501) staff       (20)     1476 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0016_update_versionfield.py
+-rw-r--r--   0 domen      (501) staff       (20)      628 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0023_update_checksum.py
+-rw-r--r--   0 domen      (501) staff       (20)      431 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0009_make_size_mandatory.py
+-rw-r--r--   0 domen      (501) staff       (20)    11468 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0001_initial.py
+-rw-r--r--   0 domen      (501) staff       (20)      467 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0005_process_data_name.py
+-rw-r--r--   0 domen      (501) staff       (20)      930 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0002_project_to_collection.py
+-rw-r--r--   0 domen      (501) staff       (20)      452 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0007_data_size.py
+-rw-r--r--   0 domen      (501) staff       (20)     1201 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0004_data_dependency_2.py
+-rw-r--r--   0 domen      (501) staff       (20)      991 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0003_support_sample.py
+-rw-r--r--   0 domen      (501) staff       (20)      793 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0018_remove_triggers.py
+-rw-r--r--   0 domen      (501) staff       (20)      630 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0020_collection_descriptor_dirty.py
+-rw-r--r--   0 domen      (501) staff       (20)      515 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0013_add_requirements.py
+-rw-r--r--   0 domen      (501) staff       (20)      450 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0006_data_named_by_user.py
+-rw-r--r--   0 domen      (501) staff       (20)      622 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0011_calculate_checksum.py
+-rw-r--r--   0 domen      (501) staff       (20)     1308 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0012_recreate_empty_parents.py
+-rw-r--r--   0 domen      (501) staff       (20)     1927 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migrations/0030_change_slug_field.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/expression_engines/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/expression_engines/jinja/
+-rw-r--r--   0 domen      (501) staff       (20)     6535 2018-02-05 10:50:16.000000 resolwe-9.0.0a4/resolwe/flow/expression_engines/jinja/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     3361 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/expression_engines/jinja/filters.py
+-rw-r--r--   0 domen      (501) staff       (20)      180 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/expression_engines/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      243 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/expression_engines/exceptions.py
+-rw-r--r--   0 domen      (501) staff       (20)      876 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/expression_engines/base.py
+-rw-r--r--   0 domen      (501) staff       (20)      686 2018-03-27 07:24:44.000000 resolwe-9.0.0a4/resolwe/flow/tasks.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/elastic_indexes/
+-rw-r--r--   0 domen      (501) staff       (20)       92 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/elastic_indexes/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     2367 2018-04-23 20:33:01.000000 resolwe-9.0.0a4/resolwe/flow/elastic_indexes/base.py
+-rw-r--r--   0 domen      (501) staff       (20)     2161 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/resolwe/flow/elastic_indexes/data.py
+-rw-r--r--   0 domen      (501) staff       (20)     2431 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/finders.py
+-rw-r--r--   0 domen      (501) staff       (20)    12328 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/serializers.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/managers/
+-rw-r--r--   0 domen      (501) staff       (20)    37847 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/resolwe/flow/managers/dispatcher.py
+-rw-r--r--   0 domen      (501) staff       (20)     1334 2018-03-26 07:08:26.000000 resolwe-9.0.0a4/resolwe/flow/managers/protocol.py
+-rw-r--r--   0 domen      (501) staff       (20)      142 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/managers/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      680 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/resolwe/flow/managers/consumer.py
+-rw-r--r--   0 domen      (501) staff       (20)      418 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/managers/utils.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/
+-rw-r--r--   0 domen      (501) staff       (20)     2172 2018-03-27 07:24:44.000000 resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/slurm.py
+-rw-r--r--   0 domen      (501) staff       (20)      943 2018-03-27 07:24:44.000000 resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/local.py
+-rw-r--r--   0 domen      (501) staff       (20)      282 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     1430 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/celery.py
+-rw-r--r--   0 domen      (501) staff       (20)     1088 2018-03-27 07:24:44.000000 resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/base.py
+-rw-r--r--   0 domen      (501) staff       (20)     9939 2018-04-12 10:11:32.000000 resolwe-9.0.0a4/resolwe/flow/managers/state.py
+-rw-r--r--   0 domen      (501) staff       (20)    20549 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/resolwe/flow/managers/listener.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/
+-rw-r--r--   0 domen      (501) staff       (20)     9253 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_expression_filters.py
+-rw-r--r--   0 domen      (501) staff       (20)      657 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_resources.py
+-rw-r--r--   0 domen      (501) staff       (20)     1938 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_utils.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/fields_test_app/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/fields_test_app/migrations/
+-rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/fields_test_app/migrations/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      753 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/fields_test_app/migrations/0001_initial.py
+-rw-r--r--   0 domen      (501) staff       (20)      441 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/fields_test_app/models.py
+-rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/fields_test_app/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     3554 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_serializers.py
+-rw-r--r--   0 domen      (501) staff       (20)    37074 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_validation.py
+-rw-r--r--   0 domen      (501) staff       (20)     5261 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_access_api.py
+-rw-r--r--   0 domen      (501) staff       (20)     1784 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_env_vars.py
+-rw-r--r--   0 domen      (501) staff       (20)    11417 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_executors.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/
+-rw-r--r--   0 domen      (501) staff       (20)      814 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/secrets.yml
+-rw-r--r--   0 domen      (501) staff       (20)     1556 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/workflow.yml
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/second_version/
+-rw-r--r--   0 domen      (501) staff       (20)      154 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/second_version/tests.yml
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/first_version/
+-rw-r--r--   0 domen      (501) staff       (20)      154 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/first_version/tests.yml
+-rw-r--r--   0 domen      (501) staff       (20)     1240 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/spawned.yml
+-rw-r--r--   0 domen      (501) staff       (20)    12888 2018-04-12 09:00:05.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/tests.yml
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/wrong_defaults/
+-rw-r--r--   0 domen      (501) staff       (20)      512 2018-04-12 09:00:05.000000 resolwe-9.0.0a4/resolwe/flow/tests/processes/wrong_defaults/tests.yml
+-rw-r--r--   0 domen      (501) staff       (20)     1774 2018-02-15 20:36:59.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_docs.py
+-rw-r--r--   0 domen      (501) staff       (20)     1252 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_runtime.py
+-rw-r--r--   0 domen      (501) staff       (20)        0 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     7680 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_commands.py
+-rw-r--r--   0 domen      (501) staff       (20)     3857 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_fields.py
+-rw-r--r--   0 domen      (501) staff       (20)    28889 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_models.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/files/
+-rw-r--r--   0 domen      (501) staff       (20)       65 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/files/contents.rst
+-rw-r--r--   0 domen      (501) staff       (20)        0 2018-04-20 10:45:41.000000 resolwe-9.0.0a4/resolwe/flow/tests/files/errors.txt
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/files/processes/
+-rw-r--r--   0 domen      (501) staff       (20)     4705 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/files/processes/test.yaml
+-rw-r--r--   0 domen      (501) staff       (20)      501 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/files/conf.py
+-rw-r--r--   0 domen      (501) staff       (20)     2348 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_secrets.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/tests/fixtures/
+-rw-r--r--   0 domen      (501) staff       (20)      161 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/fixtures/relationtypes.yaml
+-rw-r--r--   0 domen      (501) staff       (20)    35653 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_api.py
+-rw-r--r--   0 domen      (501) staff       (20)     7515 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_manager.py
+-rw-r--r--   0 domen      (501) staff       (20)     1364 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_descriptors.py
+-rw-r--r--   0 domen      (501) staff       (20)      819 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_tool.py
+-rw-r--r--   0 domen      (501) staff       (20)      323 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/tests/expression_filters.py
+-rw-r--r--   0 domen      (501) staff       (20)    16353 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_purge.py
+-rw-r--r--   0 domen      (501) staff       (20)    11595 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_relations.py
+-rw-r--r--   0 domen      (501) staff       (20)     1486 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_ordering.py
+-rw-r--r--   0 domen      (501) staff       (20)    11554 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/tests/test_filtering.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/management/
+-rw-r--r--   0 domen      (501) staff       (20)      227 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/management/__init__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/management/commands/
+-rw-r--r--   0 domen      (501) staff       (20)    13791 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/management/commands/register.py
+-rw-r--r--   0 domen      (501) staff       (20)       34 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/management/commands/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      806 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/management/commands/purge.py
+-rw-r--r--   0 domen      (501) staff       (20)     4613 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/management/commands/collecttools.py
+-rw-r--r--   0 domen      (501) staff       (20)     5129 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/management/commands/list_docker_images.py
+-rw-r--r--   0 domen      (501) staff       (20)     1210 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/management/commands/runlistener.py
+-rw-r--r--   0 domen      (501) staff       (20)      219 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/__init__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/utils/
+-rw-r--r--   0 domen      (501) staff       (20)     3237 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/utils/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     5714 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/utils/purge.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/utils/docs/
+-rw-r--r--   0 domen      (501) staff       (20)    15698 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/utils/docs/autoprocess.py
+-rw-r--r--   0 domen      (501) staff       (20)       25 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/utils/docs/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     3086 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/utils/iterators.py
+-rw-r--r--   0 domen      (501) staff       (20)      985 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/utils/exceptions.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/models/
+-rw-r--r--   0 domen      (501) staff       (20)      894 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/descriptor.py
+-rw-r--r--   0 domen      (501) staff       (20)     1173 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/functions.py
+-rw-r--r--   0 domen      (501) staff       (20)     7771 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/fields.py
+-rw-r--r--   0 domen      (501) staff       (20)     1841 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     2310 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/secret.py
+-rw-r--r--   0 domen      (501) staff       (20)    22760 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/utils.py
+-rw-r--r--   0 domen      (501) staff       (20)     2213 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/storage.py
+-rw-r--r--   0 domen      (501) staff       (20)     2156 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/collection.py
+-rw-r--r--   0 domen      (501) staff       (20)     1095 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/migrations.py
+-rw-r--r--   0 domen      (501) staff       (20)     2846 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/entity.py
+-rw-r--r--   0 domen      (501) staff       (20)     6079 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/process.py
+-rw-r--r--   0 domen      (501) staff       (20)     2074 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/models/base.py
+-rw-r--r--   0 domen      (501) staff       (20)    17503 2018-05-11 18:53:35.000000 resolwe-9.0.0a4/resolwe/flow/models/data.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/execution_engines/
+-rw-r--r--   0 domen      (501) staff       (20)      175 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/execution_engines/__init__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/execution_engines/bash/
+-rw-r--r--   0 domen      (501) staff       (20)     2433 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/resolwe/flow/execution_engines/bash/__init__.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/execution_engines/workflow/
+-rw-r--r--   0 domen      (501) staff       (20)     4790 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/execution_engines/workflow/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      247 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/execution_engines/exceptions.py
+-rw-r--r--   0 domen      (501) staff       (20)      658 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/execution_engines/base.py
+-rw-r--r--   0 domen      (501) staff       (20)      557 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/apps.py
+-rw-r--r--   0 domen      (501) staff       (20)     3434 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/engine.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/executors/
+-rw-r--r--   0 domen      (501) staff       (20)    10265 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/run.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/executors/docker/
+-rw-r--r--   0 domen      (501) staff       (20)    40139 2017-12-26 18:16:18.000000 resolwe-9.0.0a4/resolwe/flow/executors/docker/seccomp.py
+-rw-r--r--   0 domen      (501) staff       (20)     9305 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/docker/run.py
+-rw-r--r--   0 domen      (501) staff       (20)      251 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/executors/docker/constants.py
+-rw-r--r--   0 domen      (501) staff       (20)      204 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/docker/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     1906 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/executors/docker/prepare.py
+-rw-r--r--   0 domen      (501) staff       (20)       74 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/executors/requirements.txt
+-rw-r--r--   0 domen      (501) staff       (20)     1334 2018-03-26 07:08:26.000000 resolwe-9.0.0a4/resolwe/flow/executors/protocol.py
+-rw-r--r--   0 domen      (501) staff       (20)      265 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     1044 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/global_settings.py
+-rw-r--r--   0 domen      (501) staff       (20)     2503 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/logger.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/executors/local/
+-rw-r--r--   0 domen      (501) staff       (20)     1577 2018-03-26 07:08:26.000000 resolwe-9.0.0a4/resolwe/flow/executors/local/run.py
+-rw-r--r--   0 domen      (501) staff       (20)      199 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/local/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)     1028 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/local/prepare.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/executors/null/
+-rw-r--r--   0 domen      (501) staff       (20)      718 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/null/run.py
+-rw-r--r--   0 domen      (501) staff       (20)      194 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/null/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      399 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/resolwe/flow/executors/null/prepare.py
+-rw-r--r--   0 domen      (501) staff       (20)     2763 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/manager_commands.py
+-rw-r--r--   0 domen      (501) staff       (20)     1622 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/__main__.py
+-rw-r--r--   0 domen      (501) staff       (20)     3721 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/executors/prepare.py
+-rw-r--r--   0 domen      (501) staff       (20)      341 2018-05-14 09:24:57.000000 resolwe-9.0.0a4/resolwe/flow/routing.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/static/
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/static/flow/
+-rw-r--r--   0 domen      (501) staff       (20)    14118 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/static/flow/typeSchema.json
+-rw-r--r--   0 domen      (501) staff       (20)      971 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/static/flow/descriptorSchema.json
+-rw-r--r--   0 domen      (501) staff       (20)    15461 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/static/flow/fieldSchema.json
+-rw-r--r--   0 domen      (501) staff       (20)     5790 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/static/flow/processSchema.json
+-rw-r--r--   0 domen      (501) staff       (20)    22286 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/migration_ops.py
+drwxr-xr-x   0 domen      (501) staff       (20)        0 2018-05-14 10:02:51.000000 resolwe-9.0.0a4/resolwe/flow/views/
+-rw-r--r--   0 domen      (501) staff       (20)     1053 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/views/descriptor.py
+-rw-r--r--   0 domen      (501) staff       (20)     5569 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/views/relation.py
+-rw-r--r--   0 domen      (501) staff       (20)     7277 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/views/mixins.py
+-rw-r--r--   0 domen      (501) staff       (20)      933 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/views/__init__.py
+-rw-r--r--   0 domen      (501) staff       (20)      623 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/views/storage.py
+-rw-r--r--   0 domen      (501) staff       (20)     4551 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/views/collection.py
+-rw-r--r--   0 domen      (501) staff       (20)     6025 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/views/entity.py
+-rw-r--r--   0 domen      (501) staff       (20)     1376 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/views/process.py
+-rw-r--r--   0 domen      (501) staff       (20)     9492 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/views/data.py
+-rw-r--r--   0 domen      (501) staff       (20)     3670 2018-04-16 07:58:52.000000 resolwe-9.0.0a4/resolwe/flow/filters.py
+-rw-r--r--   0 domen      (501) staff       (20)     3854 2018-03-20 12:27:36.000000 resolwe-9.0.0a4/README.rst
```

### Comparing `resolwe-9.0.0a3/PKG-INFO` & `resolwe-9.0.0a4/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: resolwe
-Version: 9.0.0a3
+Version: 9.0.0a4
 Summary: Open source enterprise dataflow engine in Django
 Home-page: https://github.com/genialis/resolwe
 Author: Genialis d.o.o.
 Author-email: dev-team@genialis.com
 License: Apache License (2.0)
 Description-Content-Type: UNKNOWN
 Description: =======
```

### Comparing `resolwe-9.0.0a3/resolwe.egg-info/PKG-INFO` & `resolwe-9.0.0a4/resolwe.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: resolwe
-Version: 9.0.0a3
+Version: 9.0.0a4
 Summary: Open source enterprise dataflow engine in Django
 Home-page: https://github.com/genialis/resolwe
 Author: Genialis d.o.o.
 Author-email: dev-team@genialis.com
 License: Apache License (2.0)
 Description-Content-Type: UNKNOWN
 Description: =======
```

### Comparing `resolwe-9.0.0a3/resolwe.egg-info/SOURCES.txt` & `resolwe-9.0.0a4/resolwe.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe.egg-info/requires.txt` & `resolwe-9.0.0a4/resolwe.egg-info/requires.txt`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/.pylintrc` & `resolwe-9.0.0a4/.pylintrc`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/LICENSE` & `resolwe-9.0.0a4/LICENSE`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/tests/settings.py` & `resolwe-9.0.0a4/tests/settings.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/tests/docker-compose.yml` & `resolwe-9.0.0a4/tests/docker-compose.yml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/tests/manage.py` & `resolwe-9.0.0a4/tests/manage.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/MANIFEST.in` & `resolwe-9.0.0a4/MANIFEST.in`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/index.rst` & `resolwe-9.0.0a4/docs/index.rst`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/contributing.rst` & `resolwe-9.0.0a4/docs/contributing.rst`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/images/resolwe_02_internals.png` & `resolwe-9.0.0a4/docs/images/resolwe_02_internals.png`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/images/proc_02_flow.png` & `resolwe-9.0.0a4/docs/images/proc_02_flow.png`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/images/proc_03_types.png` & `resolwe-9.0.0a4/docs/images/proc_03_types.png`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/images/resolwe_01_context.png` & `resolwe-9.0.0a4/docs/images/resolwe_01_context.png`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/images/proc_01.png` & `resolwe-9.0.0a4/docs/images/proc_01.png`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/images/resolwe_04_workers.png` & `resolwe-9.0.0a4/docs/images/resolwe_04_workers.png`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/images/resolwe_03_workflow.png` & `resolwe-9.0.0a4/docs/images/resolwe_03_workflow.png`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/example/example/processes/example.yml` & `resolwe-9.0.0a4/docs/example/example/processes/example.yml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/conf.py` & `resolwe-9.0.0a4/docs/conf.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/overview.rst` & `resolwe-9.0.0a4/docs/overview.rst`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/proc.rst` & `resolwe-9.0.0a4/docs/proc.rst`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/composer.rst` & `resolwe-9.0.0a4/docs/composer.rst`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/flow.rst` & `resolwe-9.0.0a4/docs/flow.rst`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/docs/CHANGELOG.rst` & `resolwe-9.0.0a4/docs/CHANGELOG.rst`

 * *Files 0% similar despite different names*

```diff
@@ -9,14 +9,15 @@
 ==========
 Unreleased
 ==========
 
 Changed
 -------
 - Make sorting by contributor case insensitive in Elasticsearch endpoints
+- Delete ES documents in post delete signal instead of pre delete one
 
 Added
 -----
 - **BACKWARD INCOMPATIBLE:** Add on-register validation of default values in
   process and schemas
 - **BACKWARD INCOMPATIBLE:** Validate that field names in processes and
   schemas starts with a letter
```

### Comparing `resolwe-9.0.0a3/docs/api.rst` & `resolwe-9.0.0a4/docs/api.rst`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/setup.py` & `resolwe-9.0.0a4/setup.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/tox.ini` & `resolwe-9.0.0a4/tox.ini`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/setup.cfg` & `resolwe-9.0.0a4/setup.cfg`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/test/__init__.py` & `resolwe-9.0.0a4/resolwe/test/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/test/utils.py` & `resolwe-9.0.0a4/resolwe/test/utils.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/test/tests.py` & `resolwe-9.0.0a4/resolwe/test/tests.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/test/testcases/setting_overrides.py` & `resolwe-9.0.0a4/resolwe/test/testcases/setting_overrides.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/test/testcases/__init__.py` & `resolwe-9.0.0a4/resolwe/test/testcases/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/test/testcases/api.py` & `resolwe-9.0.0a4/resolwe/test/testcases/api.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/test/testcases/process.py` & `resolwe-9.0.0a4/resolwe/test/testcases/process.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/signals.py` & `resolwe-9.0.0a4/resolwe/elastic/signals.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/mixins.py` & `resolwe-9.0.0a4/resolwe/elastic/mixins.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/fields.py` & `resolwe-9.0.0a4/resolwe/elastic/fields.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/composer.py` & `resolwe-9.0.0a4/resolwe/elastic/composer.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/viewsets.py` & `resolwe-9.0.0a4/resolwe/elastic/viewsets.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/lookup.py` & `resolwe-9.0.0a4/resolwe/elastic/lookup.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/tests/test_composer.py` & `resolwe-9.0.0a4/resolwe/elastic/tests/test_composer.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/tests/test_viewsets.py` & `resolwe-9.0.0a4/resolwe/elastic/tests/test_viewsets.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/tests/test_app/migrations/0001_initial.py` & `resolwe-9.0.0a4/resolwe/elastic/tests/test_app/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/tests/test_app/models.py` & `resolwe-9.0.0a4/resolwe/elastic/tests/test_app/models.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/tests/test_app/viewsets.py` & `resolwe-9.0.0a4/resolwe/elastic/tests/test_app/viewsets.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/tests/test_app/elastic_indexes.py` & `resolwe-9.0.0a4/resolwe/elastic/tests/test_app/elastic_indexes.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/tests/test_index.py` & `resolwe-9.0.0a4/resolwe/elastic/tests/test_index.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/management/commands/elastic_purge.py` & `resolwe-9.0.0a4/resolwe/elastic/management/commands/elastic_purge.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/management/commands/elastic_index.py` & `resolwe-9.0.0a4/resolwe/elastic/management/commands/elastic_index.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/management/commands/elastic_mapping.py` & `resolwe-9.0.0a4/resolwe/elastic/management/commands/elastic_mapping.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/__init__.py` & `resolwe-9.0.0a4/resolwe/elastic/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/utils/__init__.py` & `resolwe-9.0.0a4/resolwe/elastic/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/apps.py` & `resolwe-9.0.0a4/resolwe/elastic/apps.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/builder.py` & `resolwe-9.0.0a4/resolwe/elastic/builder.py`

 * *Files 2% similar despite different names*

```diff
@@ -80,15 +80,19 @@
         cached = self._cache[self._get_cache_key(obj)]
         build_kwargs = {}
 
         if 'model' in cached and 'pks' in cached:
             build_kwargs['queryset'] = cached['model'].objects.filter(pk__in=cached['pks'])
 
         elif 'obj' in cached:
-            build_kwargs['obj'] = cached['obj']
+            if cached['obj'].__class__.objects.filter(pk=cached['obj'].pk).exists():
+                build_kwargs['obj'] = cached['obj']
+            else:
+                # Object was deleted in the meantime.
+                build_kwargs['queryset'] = cached['obj'].__class__.objects.none()
 
         self._clean_cache(obj)
 
         return build_kwargs
 
 
 class ElasticSignal(object):
@@ -372,17 +376,17 @@
 
     def _connect_signal(self, index):
         """Create signals for building indexes."""
         post_save_signal = ElasticSignal(index, 'build')
         post_save_signal.connect(post_save, sender=index.object_type)
         self.signals.append(post_save_signal)
 
-        pre_delete_signal = ElasticSignal(index, 'remove_object')
-        pre_delete_signal.connect(pre_delete, sender=index.object_type)
-        self.signals.append(pre_delete_signal)
+        post_delete_signal = ElasticSignal(index, 'remove_object')
+        post_delete_signal.connect(post_delete, sender=index.object_type)
+        self.signals.append(post_delete_signal)
 
         # Connect signals for all dependencies.
         for dependency in index.get_dependencies():
             # Automatically convert m2m fields to dependencies.
             if isinstance(dependency, (models.ManyToManyField, ManyToManyDescriptor)):
                 dependency = ManyToManyDependency(dependency)
             elif not isinstance(dependency, Dependency):
```

### Comparing `resolwe-9.0.0a3/resolwe/elastic/indices.py` & `resolwe-9.0.0a4/resolwe/elastic/indices.py`

 * *Files 0% similar despite different names*

```diff
@@ -17,15 +17,14 @@
 from __future__ import absolute_import, division, print_function, unicode_literals
 
 import copy
 import logging
 import threading
 
 import elasticsearch_dsl as dsl
-from elasticsearch.exceptions import NotFoundError
 from elasticsearch.helpers import bulk
 from elasticsearch_dsl.connections import connections
 from elasticsearch_dsl.exceptions import IllegalOperation
 
 from django.contrib.contenttypes.models import ContentType
 
 from guardian.conf.settings import ANONYMOUS_USER_NAME
@@ -386,16 +385,15 @@
     def get_dependencies(self):
         """Return dependencies, which should trigger updates of this index."""
         return []
 
     def remove_object(self, obj):
         """Remove current object from the ElasticSearch."""
         obj_id = self.generate_id(obj)
-        try:
-            index = self.document_class.get(obj_id)
-            index.delete(refresh=True)
-        except NotFoundError:
-            pass  # object doesn't exist in index
+        es_obj = self.document_class.get(obj_id, ignore=[404])
+        # Object may not exist in this index.
+        if es_obj:
+            es_obj.delete(refresh=True)
 
     def search(self):
         """Return search query of document object."""
         return self.document_class.search()
```

### Comparing `resolwe-9.0.0a3/resolwe/elastic/pagination.py` & `resolwe-9.0.0a4/resolwe/elastic/pagination.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/elastic/routers.py` & `resolwe-9.0.0a4/resolwe/elastic/routers.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/api_urls.py` & `resolwe-9.0.0a4/resolwe/api_urls.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/mixins.py` & `resolwe-9.0.0a4/resolwe/permissions/mixins.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/shortcuts.py` & `resolwe-9.0.0a4/resolwe/permissions/shortcuts.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/tests/test_utils.py` & `resolwe-9.0.0a4/resolwe/permissions/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/tests/test_collection.py` & `resolwe-9.0.0a4/resolwe/permissions/tests/test_collection.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/tests/test_shortcuts.py` & `resolwe-9.0.0a4/resolwe/permissions/tests/test_shortcuts.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/tests/test_data.py` & `resolwe-9.0.0a4/resolwe/permissions/tests/test_data.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/tests/test_tool.py` & `resolwe-9.0.0a4/resolwe/permissions/tests/test_tool.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/tests/test_permissions.py` & `resolwe-9.0.0a4/resolwe/permissions/tests/test_permissions.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/utils.py` & `resolwe-9.0.0a4/resolwe/permissions/utils.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/loader.py` & `resolwe-9.0.0a4/resolwe/permissions/loader.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/permissions.py` & `resolwe-9.0.0a4/resolwe/permissions/permissions.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/fixtures/collections.yaml` & `resolwe-9.0.0a4/resolwe/permissions/fixtures/collections.yaml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/fixtures/permissions.yaml` & `resolwe-9.0.0a4/resolwe/permissions/fixtures/permissions.yaml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/fixtures/users.yaml` & `resolwe-9.0.0a4/resolwe/permissions/fixtures/users.yaml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/fixtures/processes.yaml` & `resolwe-9.0.0a4/resolwe/permissions/fixtures/processes.yaml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/fixtures/data.yaml` & `resolwe-9.0.0a4/resolwe/permissions/fixtures/data.yaml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/fixtures/readme.txt` & `resolwe-9.0.0a4/resolwe/permissions/fixtures/readme.txt`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/permissions/filters.py` & `resolwe-9.0.0a4/resolwe/permissions/filters.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/utils.py` & `resolwe-9.0.0a4/resolwe/utils.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/__about__.py` & `resolwe-9.0.0a4/resolwe/__about__.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 #       interfere with a global variable __name__ denoting object's name.
 __title__ = 'resolwe'
 __summary__ = 'Open source enterprise dataflow engine in Django'
 __url__ = 'https://github.com/genialis/resolwe'
 
 # Semantic versioning is used. For more information see:
 # https://packaging.python.org/en/latest/distributing/#semantic-versioning-preferred
-__version__ = '9.0.0a3'
+__version__ = '9.0.0a4'
 
 __author__ = 'Genialis d.o.o.'
 __email__ = 'dev-team@genialis.com'
 
 __license__ = 'Apache License (2.0)'
 __copyright__ = '2015-2018, ' + __author__
```

### Comparing `resolwe-9.0.0a3/resolwe/test_helpers/management/commands/show_profile.py` & `resolwe-9.0.0a4/resolwe/test_helpers/management/commands/show_profile.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/test_helpers/test_runner.py` & `resolwe-9.0.0a4/resolwe/test_helpers/test_runner.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/tools/parse_tabular_file.py` & `resolwe-9.0.0a4/resolwe/toolkit/tools/parse_tabular_file.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/processes/files.yml` & `resolwe-9.0.0a4/resolwe/toolkit/processes/files.yml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/processes/archiver.yml` & `resolwe-9.0.0a4/resolwe/toolkit/processes/archiver.yml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/tests/test_archiver.py` & `resolwe-9.0.0a4/resolwe/toolkit/tests/test_archiver.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/tests/test_files.py` & `resolwe-9.0.0a4/resolwe/toolkit/tests/test_files.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/tests/files/file binary` & `resolwe-9.0.0a4/resolwe/toolkit/tests/files/file binary`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/tests/files/file image.png` & `resolwe-9.0.0a4/resolwe/toolkit/tests/files/file image.png`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/tests/files/file tab.1.xlsx` & `resolwe-9.0.0a4/resolwe/toolkit/tests/files/file tab.1.xlsx`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/tests/files/file tab.xls` & `resolwe-9.0.0a4/resolwe/toolkit/tests/files/file tab.xls`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-16.04` & `resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-16.04`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-17.10` & `resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-17.10`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-18.04` & `resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-18.04`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/re-import.sh` & `resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/re-import.sh`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/README.md` & `resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/README.md`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.fedora-26` & `resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.fedora-26`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/curlprogress.py` & `resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/curlprogress.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-14.04` & `resolwe-9.0.0a4/resolwe/toolkit/docker_images/base/Dockerfile.ubuntu-14.04`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/rest/fields.py` & `resolwe-9.0.0a4/resolwe/rest/fields.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/rest/serializers.py` & `resolwe-9.0.0a4/resolwe/rest/serializers.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/rest/tests.py` & `resolwe-9.0.0a4/resolwe/rest/tests.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/rest/projection.py` & `resolwe-9.0.0a4/resolwe/rest/projection.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/signals.py` & `resolwe-9.0.0a4/resolwe/flow/signals.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0013_migration_history.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0013_migration_history.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0015_make_data_indexes.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0015_make_data_indexes.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0010_add_secret.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0010_add_secret.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0022_data_sha1_to_sha256.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0022_data_sha1_to_sha256.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0014_add_entity.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0014_add_entity.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0024_add_relations.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0024_add_relations.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0025_set_get_last_by.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0025_set_get_last_by.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0012_require_checksum.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0012_require_checksum.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0008_fix_jsonfields.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0008_fix_jsonfields.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0027_scheduling_class.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0027_scheduling_class.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0014_track_resources.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0014_track_resources.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0004_autoslug_field.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0004_autoslug_field.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0011_preserve_parents.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0011_preserve_parents.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0010_fix_jsonfields.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0010_fix_jsonfields.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0008_compute_size.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0008_compute_size.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0017_update_checksum.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0017_update_checksum.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0005_data_dependency_3.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0005_data_dependency_3.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0002_set_process_owners.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0002_set_process_owners.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0006_add_total_size.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0006_add_total_size.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0029_data_checksum_index.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0029_data_checksum_index.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0003_data_dependency_1.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0003_data_dependency_1.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0026_tags.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0026_tags.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0007_add_owner.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0007_add_owner.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0001_squashed_0030_change_slug_field.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0001_squashed_0030_change_slug_field.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0028_remove_public_processes.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0028_remove_public_processes.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0016_update_versionfield.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0016_update_versionfield.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0023_update_checksum.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0023_update_checksum.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0001_initial.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0002_project_to_collection.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0002_project_to_collection.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0004_data_dependency_2.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0004_data_dependency_2.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0003_support_sample.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0003_support_sample.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0018_remove_triggers.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0018_remove_triggers.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0020_collection_descriptor_dirty.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0020_collection_descriptor_dirty.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0013_add_requirements.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0013_add_requirements.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0011_calculate_checksum.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0011_calculate_checksum.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0012_recreate_empty_parents.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0012_recreate_empty_parents.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migrations/0030_change_slug_field.py` & `resolwe-9.0.0a4/resolwe/flow/migrations/0030_change_slug_field.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/expression_engines/jinja/__init__.py` & `resolwe-9.0.0a4/resolwe/flow/expression_engines/jinja/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/expression_engines/jinja/filters.py` & `resolwe-9.0.0a4/resolwe/flow/expression_engines/jinja/filters.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/expression_engines/base.py` & `resolwe-9.0.0a4/resolwe/flow/expression_engines/base.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tasks.py` & `resolwe-9.0.0a4/resolwe/flow/tasks.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/elastic_indexes/base.py` & `resolwe-9.0.0a4/resolwe/flow/elastic_indexes/base.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/elastic_indexes/data.py` & `resolwe-9.0.0a4/resolwe/flow/elastic_indexes/data.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/finders.py` & `resolwe-9.0.0a4/resolwe/flow/finders.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/serializers.py` & `resolwe-9.0.0a4/resolwe/flow/serializers.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/managers/dispatcher.py` & `resolwe-9.0.0a4/resolwe/flow/managers/dispatcher.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/managers/protocol.py` & `resolwe-9.0.0a4/resolwe/flow/managers/protocol.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/managers/consumer.py` & `resolwe-9.0.0a4/resolwe/flow/managers/consumer.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/slurm.py` & `resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/slurm.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/local.py` & `resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/local.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/celery.py` & `resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/celery.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/managers/workload_connectors/base.py` & `resolwe-9.0.0a4/resolwe/flow/managers/workload_connectors/base.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/managers/state.py` & `resolwe-9.0.0a4/resolwe/flow/managers/state.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/managers/listener.py` & `resolwe-9.0.0a4/resolwe/flow/managers/listener.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_expression_filters.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_expression_filters.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_resources.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_resources.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_utils.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_utils.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/fields_test_app/migrations/0001_initial.py` & `resolwe-9.0.0a4/resolwe/flow/tests/fields_test_app/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_serializers.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_serializers.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_validation.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_validation.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_access_api.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_access_api.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_env_vars.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_env_vars.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_executors.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_executors.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/processes/secrets.yml` & `resolwe-9.0.0a4/resolwe/flow/tests/processes/secrets.yml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/processes/workflow.yml` & `resolwe-9.0.0a4/resolwe/flow/tests/processes/workflow.yml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/processes/spawned.yml` & `resolwe-9.0.0a4/resolwe/flow/tests/processes/spawned.yml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/processes/tests.yml` & `resolwe-9.0.0a4/resolwe/flow/tests/processes/tests.yml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/processes/wrong_defaults/tests.yml` & `resolwe-9.0.0a4/resolwe/flow/tests/processes/wrong_defaults/tests.yml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_docs.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_docs.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_runtime.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_runtime.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_commands.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_commands.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_fields.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_fields.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_models.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_models.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/files/processes/test.yaml` & `resolwe-9.0.0a4/resolwe/flow/tests/files/processes/test.yaml`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_secrets.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_secrets.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_api.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_api.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_manager.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_manager.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_descriptors.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_descriptors.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_tool.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_tool.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_purge.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_purge.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_relations.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_relations.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_ordering.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_ordering.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/tests/test_filtering.py` & `resolwe-9.0.0a4/resolwe/flow/tests/test_filtering.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/management/commands/register.py` & `resolwe-9.0.0a4/resolwe/flow/management/commands/register.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/management/commands/purge.py` & `resolwe-9.0.0a4/resolwe/flow/management/commands/purge.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/management/commands/collecttools.py` & `resolwe-9.0.0a4/resolwe/flow/management/commands/collecttools.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/management/commands/list_docker_images.py` & `resolwe-9.0.0a4/resolwe/flow/management/commands/list_docker_images.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/management/commands/runlistener.py` & `resolwe-9.0.0a4/resolwe/flow/management/commands/runlistener.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/utils/__init__.py` & `resolwe-9.0.0a4/resolwe/flow/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/utils/purge.py` & `resolwe-9.0.0a4/resolwe/flow/utils/purge.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/utils/docs/autoprocess.py` & `resolwe-9.0.0a4/resolwe/flow/utils/docs/autoprocess.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/utils/iterators.py` & `resolwe-9.0.0a4/resolwe/flow/utils/iterators.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/utils/exceptions.py` & `resolwe-9.0.0a4/resolwe/flow/utils/exceptions.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/descriptor.py` & `resolwe-9.0.0a4/resolwe/flow/models/descriptor.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/functions.py` & `resolwe-9.0.0a4/resolwe/flow/models/functions.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/fields.py` & `resolwe-9.0.0a4/resolwe/flow/models/fields.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/__init__.py` & `resolwe-9.0.0a4/resolwe/flow/models/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/secret.py` & `resolwe-9.0.0a4/resolwe/flow/models/secret.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/utils.py` & `resolwe-9.0.0a4/resolwe/flow/models/utils.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/storage.py` & `resolwe-9.0.0a4/resolwe/flow/models/storage.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/collection.py` & `resolwe-9.0.0a4/resolwe/flow/models/collection.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/migrations.py` & `resolwe-9.0.0a4/resolwe/flow/models/migrations.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/entity.py` & `resolwe-9.0.0a4/resolwe/flow/models/entity.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/process.py` & `resolwe-9.0.0a4/resolwe/flow/models/process.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/base.py` & `resolwe-9.0.0a4/resolwe/flow/models/base.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/models/data.py` & `resolwe-9.0.0a4/resolwe/flow/models/data.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/execution_engines/bash/__init__.py` & `resolwe-9.0.0a4/resolwe/flow/execution_engines/bash/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/execution_engines/workflow/__init__.py` & `resolwe-9.0.0a4/resolwe/flow/execution_engines/workflow/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/execution_engines/base.py` & `resolwe-9.0.0a4/resolwe/flow/execution_engines/base.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/apps.py` & `resolwe-9.0.0a4/resolwe/flow/apps.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/engine.py` & `resolwe-9.0.0a4/resolwe/flow/engine.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/run.py` & `resolwe-9.0.0a4/resolwe/flow/executors/run.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/docker/seccomp.py` & `resolwe-9.0.0a4/resolwe/flow/executors/docker/seccomp.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/docker/run.py` & `resolwe-9.0.0a4/resolwe/flow/executors/docker/run.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/docker/prepare.py` & `resolwe-9.0.0a4/resolwe/flow/executors/docker/prepare.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/protocol.py` & `resolwe-9.0.0a4/resolwe/flow/executors/protocol.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/global_settings.py` & `resolwe-9.0.0a4/resolwe/flow/executors/global_settings.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/logger.py` & `resolwe-9.0.0a4/resolwe/flow/executors/logger.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/local/run.py` & `resolwe-9.0.0a4/resolwe/flow/executors/local/run.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/local/prepare.py` & `resolwe-9.0.0a4/resolwe/flow/executors/local/prepare.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/null/run.py` & `resolwe-9.0.0a4/resolwe/flow/executors/null/run.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/manager_commands.py` & `resolwe-9.0.0a4/resolwe/flow/executors/manager_commands.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/__main__.py` & `resolwe-9.0.0a4/resolwe/flow/executors/__main__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/executors/prepare.py` & `resolwe-9.0.0a4/resolwe/flow/executors/prepare.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/static/flow/typeSchema.json` & `resolwe-9.0.0a4/resolwe/flow/static/flow/typeSchema.json`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/static/flow/descriptorSchema.json` & `resolwe-9.0.0a4/resolwe/flow/static/flow/descriptorSchema.json`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/static/flow/fieldSchema.json` & `resolwe-9.0.0a4/resolwe/flow/static/flow/fieldSchema.json`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/static/flow/processSchema.json` & `resolwe-9.0.0a4/resolwe/flow/static/flow/processSchema.json`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/migration_ops.py` & `resolwe-9.0.0a4/resolwe/flow/migration_ops.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/views/descriptor.py` & `resolwe-9.0.0a4/resolwe/flow/views/descriptor.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/views/relation.py` & `resolwe-9.0.0a4/resolwe/flow/views/relation.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/views/mixins.py` & `resolwe-9.0.0a4/resolwe/flow/views/mixins.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/views/__init__.py` & `resolwe-9.0.0a4/resolwe/flow/views/__init__.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/views/storage.py` & `resolwe-9.0.0a4/resolwe/flow/views/storage.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/views/collection.py` & `resolwe-9.0.0a4/resolwe/flow/views/collection.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/views/entity.py` & `resolwe-9.0.0a4/resolwe/flow/views/entity.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/views/process.py` & `resolwe-9.0.0a4/resolwe/flow/views/process.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/views/data.py` & `resolwe-9.0.0a4/resolwe/flow/views/data.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/resolwe/flow/filters.py` & `resolwe-9.0.0a4/resolwe/flow/filters.py`

 * *Files identical despite different names*

### Comparing `resolwe-9.0.0a3/README.rst` & `resolwe-9.0.0a4/README.rst`

 * *Files identical despite different names*

