# Comparing `tmp/oarepo-runtime-1.2.8.tar.gz` & `tmp/oarepo-runtime-1.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "oarepo-runtime-1.2.8.tar", last modified: Thu Mar 16 09:43:39 2023, max compression
+gzip compressed data, was "oarepo-runtime-1.2.9.tar", last modified: Thu Mar 16 11:57:58 2023, max compression
```

## Comparing `oarepo-runtime-1.2.8.tar` & `oarepo-runtime-1.2.9.tar`

### file list

```diff
@@ -1,76 +1,76 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.494000 oarepo-runtime-1.2.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1777 2023-03-16 09:43:39.494000 oarepo-runtime-1.2.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.485999 oarepo-runtime-1.2.8/oarepo_runtime/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.485999 oarepo-runtime-1.2.8/oarepo_runtime/cf/
--rw-r--r--   0 runner    (1001) docker     (123)     1322 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/cf/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      552 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/cf/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     4038 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/cf/mappings.py
--rw-r--r--   0 runner    (1001) docker     (123)       71 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/cli.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.485999 oarepo-runtime-1.2.8/oarepo_runtime/config/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/config/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2596 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/config/permissions_presets.py
--rw-r--r--   0 runner    (1001) docker     (123)      313 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/config/service.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.490000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/
--rw-r--r--   0 runner    (1001) docker     (123)      674 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/batch.py
--rw-r--r--   0 runner    (1001) docker     (123)     4586 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/catalogue.py
--rw-r--r--   0 runner    (1001) docker     (123)     1936 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)      884 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/config.py
--rw-r--r--   0 runner    (1001) docker     (123)     4851 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/datastreams.py
--rw-r--r--   0 runner    (1001) docker     (123)      690 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     5344 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/fixtures.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.490000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/
--rw-r--r--   0 runner    (1001) docker     (123)      858 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3287 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/excel.py
--rw-r--r--   0 runner    (1001) docker     (123)      759 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/json.py
--rw-r--r--   0 runner    (1001) docker     (123)      947 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/service.py
--rw-r--r--   0 runner    (1001) docker     (123)      332 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/yaml.py
--rw-r--r--   0 runner    (1001) docker     (123)     1204 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/transformers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.490000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/writers/
--rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/writers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2187 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/writers/service.py
--rw-r--r--   0 runner    (1001) docker     (123)     1243 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/datastreams/writers/yaml.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.490000 oarepo-runtime-1.2.8/oarepo_runtime/expansions/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/expansions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      745 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/expansions/expandable_fields.py
--rw-r--r--   0 runner    (1001) docker     (123)      144 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/expansions/service.py
--rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/ext.py
--rw-r--r--   0 runner    (1001) docker     (123)     1402 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/ext_config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.494000 oarepo-runtime-1.2.8/oarepo_runtime/facets/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/facets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      410 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/facets/max_facet.py
--rw-r--r--   0 runner    (1001) docker     (123)      962 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/facets/nested_facet.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.494000 oarepo-runtime-1.2.8/oarepo_runtime/i18n/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/i18n/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1040 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/i18n/schema.py
--rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/i18n/validation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.494000 oarepo-runtime-1.2.8/oarepo_runtime/relations/
--rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/relations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8329 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/relations/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1556 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/relations/internal.py
--rw-r--r--   0 runner    (1001) docker     (123)      848 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/relations/lookup.py
--rw-r--r--   0 runner    (1001) docker     (123)     1012 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/relations/mapping.py
--rw-r--r--   0 runner    (1001) docker     (123)     2063 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/relations/pid_relation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.494000 oarepo-runtime-1.2.8/oarepo_runtime/tasks/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/tasks/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9151 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/tasks/datastreams.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.494000 oarepo-runtime-1.2.8/oarepo_runtime/ui/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/ui/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2240 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/ui/marshmallow.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.494000 oarepo-runtime-1.2.8/oarepo_runtime/validation/
--rw-r--r--   0 runner    (1001) docker     (123)      102 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/validation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      622 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/oarepo_runtime/validation/dates.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 09:43:39.485999 oarepo-runtime-1.2.8/oarepo_runtime.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1777 2023-03-16 09:43:39.000000 oarepo-runtime-1.2.8/oarepo_runtime.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2045 2023-03-16 09:43:39.000000 oarepo-runtime-1.2.8/oarepo_runtime.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 09:43:39.000000 oarepo-runtime-1.2.8/oarepo_runtime.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      231 2023-03-16 09:43:39.000000 oarepo-runtime-1.2.8/oarepo_runtime.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-03-16 09:43:39.000000 oarepo-runtime-1.2.8/oarepo_runtime.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-16 09:43:39.000000 oarepo-runtime-1.2.8/oarepo_runtime.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      102 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1009 2023-03-16 09:43:39.494000 oarepo-runtime-1.2.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-03-16 09:39:46.000000 oarepo-runtime-1.2.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.646314 oarepo-runtime-1.2.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1777 2023-03-16 11:57:58.646314 oarepo-runtime-1.2.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.618313 oarepo-runtime-1.2.9/oarepo_runtime/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.622313 oarepo-runtime-1.2.9/oarepo_runtime/cf/
+-rw-r--r--   0 runner    (1001) docker     (123)     1322 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/cf/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      552 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/cf/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4038 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/cf/mappings.py
+-rw-r--r--   0 runner    (1001) docker     (123)       71 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/cli.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.626313 oarepo-runtime-1.2.9/oarepo_runtime/config/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/config/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2596 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/config/permissions_presets.py
+-rw-r--r--   0 runner    (1001) docker     (123)      313 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/config/service.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.630313 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/
+-rw-r--r--   0 runner    (1001) docker     (123)      674 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      276 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/batch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4586 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/catalogue.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1936 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)      884 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4851 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/datastreams.py
+-rw-r--r--   0 runner    (1001) docker     (123)      690 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5344 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/fixtures.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.634314 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/
+-rw-r--r--   0 runner    (1001) docker     (123)      858 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3287 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/excel.py
+-rw-r--r--   0 runner    (1001) docker     (123)      759 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/json.py
+-rw-r--r--   0 runner    (1001) docker     (123)      947 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/service.py
+-rw-r--r--   0 runner    (1001) docker     (123)      332 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/yaml.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1204 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/transformers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.634314 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/writers/
+-rw-r--r--   0 runner    (1001) docker     (123)     1336 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/writers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2330 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/writers/service.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1312 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/datastreams/writers/yaml.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.634314 oarepo-runtime-1.2.9/oarepo_runtime/expansions/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/expansions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      745 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/expansions/expandable_fields.py
+-rw-r--r--   0 runner    (1001) docker     (123)      144 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/expansions/service.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/ext.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1402 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/ext_config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.638314 oarepo-runtime-1.2.9/oarepo_runtime/facets/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/facets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      410 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/facets/max_facet.py
+-rw-r--r--   0 runner    (1001) docker     (123)      962 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/facets/nested_facet.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.638314 oarepo-runtime-1.2.9/oarepo_runtime/i18n/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/i18n/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1040 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/i18n/schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)      236 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/i18n/validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.642314 oarepo-runtime-1.2.9/oarepo_runtime/relations/
+-rw-r--r--   0 runner    (1001) docker     (123)      373 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/relations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8329 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/relations/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1556 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/relations/internal.py
+-rw-r--r--   0 runner    (1001) docker     (123)      848 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/relations/lookup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1012 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/relations/mapping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2063 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/relations/pid_relation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.642314 oarepo-runtime-1.2.9/oarepo_runtime/tasks/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/tasks/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9151 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/tasks/datastreams.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.642314 oarepo-runtime-1.2.9/oarepo_runtime/ui/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/ui/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2240 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/ui/marshmallow.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.646314 oarepo-runtime-1.2.9/oarepo_runtime/validation/
+-rw-r--r--   0 runner    (1001) docker     (123)      102 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/validation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      622 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/oarepo_runtime/validation/dates.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-16 11:57:58.622313 oarepo-runtime-1.2.9/oarepo_runtime.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1777 2023-03-16 11:57:58.000000 oarepo-runtime-1.2.9/oarepo_runtime.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2045 2023-03-16 11:57:58.000000 oarepo-runtime-1.2.9/oarepo_runtime.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-16 11:57:58.000000 oarepo-runtime-1.2.9/oarepo_runtime.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      231 2023-03-16 11:57:58.000000 oarepo-runtime-1.2.9/oarepo_runtime.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      289 2023-03-16 11:57:58.000000 oarepo-runtime-1.2.9/oarepo_runtime.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-16 11:57:58.000000 oarepo-runtime-1.2.9/oarepo_runtime.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      102 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1009 2023-03-16 11:57:58.646314 oarepo-runtime-1.2.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-03-16 11:54:23.000000 oarepo-runtime-1.2.9/setup.py
```

### Comparing `oarepo-runtime-1.2.8/LICENSE` & `oarepo-runtime-1.2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/PKG-INFO` & `oarepo-runtime-1.2.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: oarepo-runtime
-Version: 1.2.8
+Version: 1.2.9
 Summary: A set of runtime extensions of Invenio repository
 Description-Content-Type: text/markdown
 Provides-Extra: devs
 Provides-Extra: tests
 License-File: LICENSE
 
 # OARepo runtime
```

### Comparing `oarepo-runtime-1.2.8/README.md` & `oarepo-runtime-1.2.9/README.md`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/cf/__init__.py` & `oarepo-runtime-1.2.9/oarepo_runtime/cf/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/cf/cli.py` & `oarepo-runtime-1.2.9/oarepo_runtime/cf/cli.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/cf/mappings.py` & `oarepo-runtime-1.2.9/oarepo_runtime/cf/mappings.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/config/permissions_presets.py` & `oarepo-runtime-1.2.9/oarepo_runtime/config/permissions_presets.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/__init__.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/catalogue.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/catalogue.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/cli.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/cli.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/config.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/config.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/datastreams.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/datastreams.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/errors.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/errors.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/fixtures.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/fixtures.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/__init__.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/__init__.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/excel.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/excel.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/json.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/json.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/readers/service.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/readers/service.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/transformers.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/transformers.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/writers/__init__.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/writers/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -14,14 +14,21 @@
     @abstractmethod
     def write(self, entry: StreamEntry, *args, **kwargs):
         """Writes the input entry to the target output.
         :returns: nothing
                   Raises WriterException in case of errors.
         """
 
+    @abstractmethod
+    def delete(self, entry: StreamEntry, *args, **kwargs):
+        """Removes the stream entry
+        :returns: nothing
+                  Raises WriterException in case of errors.
+        """
+
     def finish(self):
         """Finalizes writing"""
 
 
 class BatchWriter(ABC):
     def __init__(self, **kwargs) -> None:
         """kwargs for extensions"""
```

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/writers/service.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/writers/service.py`

 * *Files 10% similar despite different names*

```diff
@@ -49,7 +49,11 @@
                 return self._service.update(self._identity, entry_id, updated)
 
         except ValidationError as err:
             raise WriterError([{"ValidationError": err.messages}])
         except InvalidRelationValue as err:
             # TODO: Check if we can get the error message easier
             raise WriterError([{"InvalidRelationValue": err.args[0]}])
+
+    def delete(self, stream_entry: StreamEntry):
+        entry = stream_entry.entry
+        self._service.delete(self._identity, entry["id"])
```

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/datastreams/writers/yaml.py` & `oarepo-runtime-1.2.9/oarepo_runtime/datastreams/writers/yaml.py`

 * *Files 6% similar despite different names*

```diff
@@ -32,11 +32,14 @@
             if not self._stream:
                 self._stream = open(self._file, "w")
         else:
             self._stream.write("---\n")
         yaml.safe_dump(entry.entry, self._stream)
         return entry
 
+    def delete(self, stream_entry: StreamEntry):
+        """noop"""
+
     def finish(self):
         """Finalizes writing"""
         if not hasattr(self._file, "read") and self._stream:
             self._stream.close()
```

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/expansions/expandable_fields.py` & `oarepo-runtime-1.2.9/oarepo_runtime/expansions/expandable_fields.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/ext.py` & `oarepo-runtime-1.2.9/oarepo_runtime/ext.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/ext_config.py` & `oarepo-runtime-1.2.9/oarepo_runtime/ext_config.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/facets/nested_facet.py` & `oarepo-runtime-1.2.9/oarepo_runtime/facets/nested_facet.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/i18n/schema.py` & `oarepo-runtime-1.2.9/oarepo_runtime/i18n/schema.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/relations/base.py` & `oarepo-runtime-1.2.9/oarepo_runtime/relations/base.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/relations/internal.py` & `oarepo-runtime-1.2.9/oarepo_runtime/relations/internal.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/relations/lookup.py` & `oarepo-runtime-1.2.9/oarepo_runtime/relations/lookup.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/relations/mapping.py` & `oarepo-runtime-1.2.9/oarepo_runtime/relations/mapping.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/relations/pid_relation.py` & `oarepo-runtime-1.2.9/oarepo_runtime/relations/pid_relation.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/tasks/datastreams.py` & `oarepo-runtime-1.2.9/oarepo_runtime/tasks/datastreams.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/ui/marshmallow.py` & `oarepo-runtime-1.2.9/oarepo_runtime/ui/marshmallow.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime/validation/dates.py` & `oarepo-runtime-1.2.9/oarepo_runtime/validation/dates.py`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime.egg-info/PKG-INFO` & `oarepo-runtime-1.2.9/oarepo_runtime.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: oarepo-runtime
-Version: 1.2.8
+Version: 1.2.9
 Summary: A set of runtime extensions of Invenio repository
 Description-Content-Type: text/markdown
 Provides-Extra: devs
 Provides-Extra: tests
 License-File: LICENSE
 
 # OARepo runtime
```

### Comparing `oarepo-runtime-1.2.8/oarepo_runtime.egg-info/SOURCES.txt` & `oarepo-runtime-1.2.9/oarepo_runtime.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `oarepo-runtime-1.2.8/setup.cfg` & `oarepo-runtime-1.2.9/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = oarepo-runtime
-version = 1.2.8
+version = 1.2.9
 description = A set of runtime extensions of Invenio repository
 authors = Alzbeta
 readme = README.md
 long_description = file:README.md
 long_description_content_type = text/markdown
 
 [options]
```

