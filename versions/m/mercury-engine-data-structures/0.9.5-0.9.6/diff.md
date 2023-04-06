# Comparing `tmp/mercury-engine-data-structures-0.9.5.tar.gz` & `tmp/mercury-engine-data-structures-0.9.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mercury-engine-data-structures-0.9.5.tar", last modified: Sat Jan 29 00:06:57 2022, max compression
+gzip compressed data, was "mercury-engine-data-structures-0.9.6.tar", last modified: Sat Feb  5 02:59:49 2022, max compression
```

## Comparing `mercury-engine-data-structures-0.9.5.tar` & `mercury-engine-data-structures-0.9.6.tar`

### file list

```diff
@@ -1,88 +1,88 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.945531 mercury-engine-data-structures-0.9.5/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.925531 mercury-engine-data-structures-0.9.5/.github/
--rw-r--r--   0 runner    (1001) docker     (121)      442 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/.github/dependabot.yml
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.925531 mercury-engine-data-structures-0.9.5/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)     2663 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/.github/workflows/python.yml
--rw-r--r--   0 runner    (1001) docker     (121)     1924 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)     1087 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     1367 2022-01-29 00:06:57.945531 mercury-engine-data-structures-0.9.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      758 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.933531 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)       90 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.937531 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/__pyinstaller/
--rw-r--r--   0 runner    (1001) docker     (121)      415 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/__pyinstaller/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      231 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/__pyinstaller/hook-mercury_engine_data_structures.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.937531 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/adapters/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/adapters/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      365 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/adapters/enum_adapter.py
--rw-r--r--   0 runner    (1001) docker     (121)     1176 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/adapters/offset.py
--rw-r--r--   0 runner    (1001) docker     (121)     7427 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/cli.py
--rw-r--r--   0 runner    (1001) docker     (121)     7596 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/common_types.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.937531 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4591 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/alignment.py
--rw-r--r--   0 runner    (1001) docker     (121)      503 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/enum.py
--rw-r--r--   0 runner    (1001) docker     (121)      547 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/json.py
--rw-r--r--   0 runner    (1001) docker     (121)     2115 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/misc.py
--rw-r--r--   0 runner    (1001) docker     (121)     4910 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/strings.py
--rw-r--r--   0 runner    (1001) docker     (121)     1019 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/version.py
--rw-r--r--   0 runner    (1001) docker     (121)     5733 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/crc.py
--rw-r--r--   0 runner    (1001) docker     (121)     1189 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/dread_data.py
--rw-r--r--   0 runner    (1001) docker     (121)   805127 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/dread_types.json
--rw-r--r--   0 runner    (1001) docker     (121)    13697 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/file_tree_editor.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.941531 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/
--rw-r--r--   0 runner    (1001) docker     (121)     1193 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1094 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/base_resource.py
--rw-r--r--   0 runner    (1001) docker     (121)      380 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/bmbls.py
--rw-r--r--   0 runner    (1001) docker     (121)     5981 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/bmsad.py
--rw-r--r--   0 runner    (1001) docker     (121)     2126 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/bmscc.py
--rw-r--r--   0 runner    (1001) docker     (121)     2257 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/bmssd.py
--rw-r--r--   0 runner    (1001) docker     (121)      370 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/brem.py
--rw-r--r--   0 runner    (1001) docker     (121)      370 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/bres.py
--rw-r--r--   0 runner    (1001) docker     (121)      371 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/brev.py
--rw-r--r--   0 runner    (1001) docker     (121)     1336 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/brfld.py
--rw-r--r--   0 runner    (1001) docker     (121)      361 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/brsa.py
--rw-r--r--   0 runner    (1001) docker     (121)   705040 2022-01-29 00:06:49.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/dread_types.py
--rw-r--r--   0 runner    (1001) docker     (121)     5797 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/pkg.py
--rw-r--r--   0 runner    (1001) docker     (121)     1987 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/property_enum.py
--rw-r--r--   0 runner    (1001) docker     (121)      737 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/standard_format.py
--rw-r--r--   0 runner    (1001) docker     (121)     1412 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/toc.py
--rw-r--r--   0 runner    (1001) docker     (121)      852 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/txt.py
--rw-r--r--   0 runner    (1001) docker     (121)     1645 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/game_check.py
--rw-r--r--   0 runner    (1001) docker     (121)     3253 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/object.py
--rw-r--r--   0 runner    (1001) docker     (121)     3147 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/pointer_set.py
--rw-r--r--   0 runner    (1001) docker     (121)  1487309 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/property_names.json
--rw-r--r--   0 runner    (1001) docker     (121)  3658843 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/resource_names.json
--rw-r--r--   0 runner    (1001) docker     (121)     6627 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/type_lib.py
--rw-r--r--   0 runner    (1001) docker     (121)      142 2022-01-29 00:06:57.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.933531 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     1367 2022-01-29 00:06:57.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3139 2022-01-29 00:06:57.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-29 00:06:57.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       88 2022-01-29 00:06:57.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-29 00:06:47.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)       18 2022-01-29 00:06:57.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       31 2022-01-29 00:06:57.000000 mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      289 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       87 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)      807 2022-01-29 00:06:57.945531 mercury-engine-data-structures-0.9.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      602 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.941531 mercury-engine-data-structures-0.9.5/test/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      416 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.941531 mercury-engine-data-structures-0.9.5/test/formats/
--rw-r--r--   0 runner    (1001) docker     (121)      414 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/formats/test_bmbls.py
--rw-r--r--   0 runner    (1001) docker     (121)    66285 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/formats/test_bmsad.py
--rw-r--r--   0 runner    (1001) docker     (121)      344 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/formats/test_bmssd.py
--rw-r--r--   0 runner    (1001) docker     (121)      338 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/formats/test_brfld.py
--rw-r--r--   0 runner    (1001) docker     (121)     2199 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/formats/test_pkg.py
--rw-r--r--   0 runner    (1001) docker     (121)      421 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/formats/test_toc.py
--rw-r--r--   0 runner    (1001) docker     (121)      363 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/formats/text_txt.py
--rw-r--r--   0 runner    (1001) docker     (121)      613 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/test_common_types.py
--rw-r--r--   0 runner    (1001) docker     (121)     1406 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/test/test_lib.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-29 00:06:57.945531 mercury-engine-data-structures-0.9.5/tools/
--rw-r--r--   0 runner    (1001) docker     (121)     9630 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/tools/create_class_definitions.py
--rw-r--r--   0 runner    (1001) docker     (121)    26628 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/tools/ghidra_export.py
--rw-r--r--   0 runner    (1001) docker     (121)   252182 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/tools/plot_simple_map.py
--rw-r--r--   0 runner    (1001) docker     (121)      935 2022-01-29 00:06:30.000000 mercury-engine-data-structures-0.9.5/tools/update_hashes_with_field_names.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.965772 mercury-engine-data-structures-0.9.6/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.953772 mercury-engine-data-structures-0.9.6/.github/
+-rw-r--r--   0 runner    (1001) docker     (121)      442 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/.github/dependabot.yml
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.953772 mercury-engine-data-structures-0.9.6/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (121)     2663 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/.github/workflows/python.yml
+-rw-r--r--   0 runner    (1001) docker     (121)     1924 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (121)     1087 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     1348 2022-02-05 02:59:49.965772 mercury-engine-data-structures-0.9.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      758 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.961772 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)       90 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.961772 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/__pyinstaller/
+-rw-r--r--   0 runner    (1001) docker     (121)      415 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/__pyinstaller/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      231 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/__pyinstaller/hook-mercury_engine_data_structures.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.961772 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/adapters/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/adapters/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      365 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/adapters/enum_adapter.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1176 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/adapters/offset.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7427 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/cli.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7596 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/common_types.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.961772 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4591 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/alignment.py
+-rw-r--r--   0 runner    (1001) docker     (121)      503 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/enum.py
+-rw-r--r--   0 runner    (1001) docker     (121)      547 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/json.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2115 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/misc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4910 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/strings.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1019 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/version.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5733 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/crc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1189 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/dread_data.py
+-rw-r--r--   0 runner    (1001) docker     (121)   805127 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/dread_types.json
+-rw-r--r--   0 runner    (1001) docker     (121)    13817 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/file_tree_editor.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.961772 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/
+-rw-r--r--   0 runner    (1001) docker     (121)     1193 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1094 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/base_resource.py
+-rw-r--r--   0 runner    (1001) docker     (121)      380 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/bmbls.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5981 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/bmsad.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2126 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/bmscc.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2257 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/bmssd.py
+-rw-r--r--   0 runner    (1001) docker     (121)      370 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/brem.py
+-rw-r--r--   0 runner    (1001) docker     (121)      370 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/bres.py
+-rw-r--r--   0 runner    (1001) docker     (121)      371 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/brev.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1336 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/brfld.py
+-rw-r--r--   0 runner    (1001) docker     (121)      361 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/brsa.py
+-rw-r--r--   0 runner    (1001) docker     (121)   705040 2022-02-05 02:59:43.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/dread_types.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5797 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/pkg.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1987 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/property_enum.py
+-rw-r--r--   0 runner    (1001) docker     (121)      737 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/standard_format.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1412 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/toc.py
+-rw-r--r--   0 runner    (1001) docker     (121)      856 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/txt.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1645 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/game_check.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3253 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/object.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3147 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/pointer_set.py
+-rw-r--r--   0 runner    (1001) docker     (121)  1487309 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/property_names.json
+-rw-r--r--   0 runner    (1001) docker     (121)  3658843 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/resource_names.json
+-rw-r--r--   0 runner    (1001) docker     (121)     6627 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/type_lib.py
+-rw-r--r--   0 runner    (1001) docker     (121)      142 2022-02-05 02:59:49.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/version.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.961772 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     1348 2022-02-05 02:59:49.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     3139 2022-02-05 02:59:49.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-02-05 02:59:49.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       88 2022-02-05 02:59:49.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-02-05 02:59:42.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)       18 2022-02-05 02:59:49.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       31 2022-02-05 02:59:49.000000 mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      289 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)       87 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      807 2022-02-05 02:59:49.965772 mercury-engine-data-structures-0.9.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)      602 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.965772 mercury-engine-data-structures-0.9.6/test/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      416 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.965772 mercury-engine-data-structures-0.9.6/test/formats/
+-rw-r--r--   0 runner    (1001) docker     (121)      414 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/formats/test_bmbls.py
+-rw-r--r--   0 runner    (1001) docker     (121)    66285 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/formats/test_bmsad.py
+-rw-r--r--   0 runner    (1001) docker     (121)      344 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/formats/test_bmssd.py
+-rw-r--r--   0 runner    (1001) docker     (121)      338 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/formats/test_brfld.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2199 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/formats/test_pkg.py
+-rw-r--r--   0 runner    (1001) docker     (121)      421 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/formats/test_toc.py
+-rw-r--r--   0 runner    (1001) docker     (121)      363 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/formats/text_txt.py
+-rw-r--r--   0 runner    (1001) docker     (121)      613 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/test_common_types.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1406 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/test/test_lib.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-02-05 02:59:49.965772 mercury-engine-data-structures-0.9.6/tools/
+-rw-r--r--   0 runner    (1001) docker     (121)     9630 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/tools/create_class_definitions.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26628 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/tools/ghidra_export.py
+-rw-r--r--   0 runner    (1001) docker     (121)   252182 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/tools/plot_simple_map.py
+-rw-r--r--   0 runner    (1001) docker     (121)      935 2022-02-05 02:59:29.000000 mercury-engine-data-structures-0.9.6/tools/update_hashes_with_field_names.py
```

### Comparing `mercury-engine-data-structures-0.9.5/.github/workflows/python.yml` & `mercury-engine-data-structures-0.9.6/.github/workflows/python.yml`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/.gitignore` & `mercury-engine-data-structures-0.9.6/.gitignore`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/LICENSE` & `mercury-engine-data-structures-0.9.6/LICENSE`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/PKG-INFO` & `mercury-engine-data-structures-0.9.6/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 Metadata-Version: 2.1
 Name: mercury-engine-data-structures
-Version: 0.9.5
+Version: 0.9.6
 Summary: Construct file definitions for the Mercury Engine, the in-house game engine from MercurySteam
-Home-page: UNKNOWN
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `mercury-engine-data-structures-0.9.5/README.md` & `mercury-engine-data-structures-0.9.6/README.md`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/adapters/offset.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/adapters/offset.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/cli.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/cli.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/common_types.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/common_types.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/alignment.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/alignment.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/json.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/json.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/misc.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/misc.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/strings.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/strings.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/construct_extensions/version.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/construct_extensions/version.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/crc.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/crc.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/dread_data.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/dread_data.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/dread_types.json` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/dread_types.json`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/file_tree_editor.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/file_tree_editor.py`

 * *Files 1% similar despite different names*

```diff
@@ -297,15 +297,17 @@
         # Update the toc for the modified (and new) files
         for asset_id, data in self._modified_resources.items():
             if data is not None:
                 self._toc.add_file(asset_id, len(data))
                 if None in self._files_for_asset_id[asset_id]:
                     path = self._name_for_asset_id[asset_id]
                     logger.info("Writing to %s with %d bytes", path, len(data))
-                    output_path.joinpath(path).write_bytes(data)
+                    target_path = output_path.joinpath(path)
+                    target_path.parent.mkdir(parents=True, exist_ok=True)
+                    target_path.write_bytes(data)
             else:
                 self._toc.remove_file(asset_id)
 
         # Update the Toc's own entry and then write
         self._toc.add_file(Toc.system_files_name(), len(self._toc.build()))
         toc_path = output_path.joinpath(Toc.system_files_name())
         toc_path.parent.mkdir(parents=True, exist_ok=True)
```

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/__init__.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/__init__.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/base_resource.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/base_resource.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/bmsad.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/bmsad.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/bmscc.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/bmscc.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/bmssd.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/bmssd.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/brfld.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/brfld.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/dread_types.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/dread_types.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/pkg.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/pkg.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/property_enum.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/property_enum.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/standard_format.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/standard_format.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/toc.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/toc.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/formats/txt.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/formats/txt.py`

 * *Files 21% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 from mercury_engine_data_structures.formats import BaseResource
 from mercury_engine_data_structures.game_check import Game
 
 
 TXT = Struct(
     "magic" / Const(b'BTXT'),
     "version" / Const(b'\x01\x00\x0a\x00'),
-    "strings" / DictAdapter(GreedyRange(DictElement(CStringRobust("utf16"))))
+    "strings" / DictAdapter(GreedyRange(DictElement(CStringRobust("utf-16-le"))))
 )
 
 class Txt(BaseResource):
     @classmethod
     def construct_class(cls, target_game: Game) -> Construct:
         return TXT
```

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/game_check.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/game_check.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/object.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/object.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/pointer_set.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/pointer_set.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/property_names.json` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/property_names.json`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/resource_names.json` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/resource_names.json`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures/type_lib.py` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures/type_lib.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/PKG-INFO` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 Metadata-Version: 2.1
 Name: mercury-engine-data-structures
-Version: 0.9.5
+Version: 0.9.6
 Summary: Construct file definitions for the Mercury Engine, the in-house game engine from MercurySteam
-Home-page: UNKNOWN
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
```

### Comparing `mercury-engine-data-structures-0.9.5/mercury_engine_data_structures.egg-info/SOURCES.txt` & `mercury-engine-data-structures-0.9.6/mercury_engine_data_structures.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/setup.cfg` & `mercury-engine-data-structures-0.9.6/setup.cfg`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/setup.py` & `mercury-engine-data-structures-0.9.6/setup.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/test/formats/test_bmsad.py` & `mercury-engine-data-structures-0.9.6/test/formats/test_bmsad.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/test/formats/test_pkg.py` & `mercury-engine-data-structures-0.9.6/test/formats/test_pkg.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/test/test_common_types.py` & `mercury-engine-data-structures-0.9.6/test/test_common_types.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/test/test_lib.py` & `mercury-engine-data-structures-0.9.6/test/test_lib.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/tools/create_class_definitions.py` & `mercury-engine-data-structures-0.9.6/tools/create_class_definitions.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/tools/ghidra_export.py` & `mercury-engine-data-structures-0.9.6/tools/ghidra_export.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/tools/plot_simple_map.py` & `mercury-engine-data-structures-0.9.6/tools/plot_simple_map.py`

 * *Files identical despite different names*

### Comparing `mercury-engine-data-structures-0.9.5/tools/update_hashes_with_field_names.py` & `mercury-engine-data-structures-0.9.6/tools/update_hashes_with_field_names.py`

 * *Files identical despite different names*

