# Comparing `tmp/annlite-0.5.8.tar.gz` & `tmp/annlite-0.5.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/annlite/annlite/dist/.tmp-05mpdxu5/annlite-0.5.8.tar", last modified: Fri Mar 24 11:08:00 2023, max compression
+gzip compressed data, was "/home/runner/work/annlite/annlite/dist/.tmp-v_0oi5fe/annlite-0.5.9.tar", last modified: Fri Apr  7 04:11:14 2023, max compression
```

## Comparing `annlite-0.5.8.tar` & `annlite-0.5.9.tar`

### file list

```diff
@@ -1,77 +1,77 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/
--rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-03-24 11:07:38.000000 annlite-0.5.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      123 2023-03-24 11:07:38.000000 annlite-0.5.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    15898 2023-03-24 11:08:00.000000 annlite-0.5.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    14977 2023-03-24 11:07:38.000000 annlite-0.5.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite/
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    15114 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/container.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite/core/
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite/core/codec/
--rw-r--r--   0 runner    (1001) docker     (123)       86 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/codec/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      888 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/codec/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    13397 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/codec/pq.py
--rw-r--r--   0 runner    (1001) docker     (123)     5176 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/codec/projector.py
--rw-r--r--   0 runner    (1001) docker     (123)     2717 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/codec/vq.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite/core/index/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/index/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1426 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/index/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     2178 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/index/flat_index.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite/core/index/hnsw/
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/index/hnsw/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6835 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/index/hnsw/index.py
--rw-r--r--   0 runner    (1001) docker     (123)     1548 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/core/index/pq_index.py
--rw-r--r--   0 runner    (1001) docker     (123)      704 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/enums.py
--rw-r--r--   0 runner    (1001) docker     (123)    14801 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/executor.py
--rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/filter.py
--rw-r--r--   0 runner    (1001) docker     (123)     1086 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/helper.py
--rw-r--r--   0 runner    (1001) docker     (123)     9249 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/hubble_tools.py
--rw-r--r--   0 runner    (1001) docker     (123)    35233 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/index.py
--rw-r--r--   0 runner    (1001) docker     (123)     3796 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/math.py
--rw-r--r--   0 runner    (1001) docker     (123)     2371 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/profile.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite/storage/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/storage/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1300 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/storage/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     4724 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/storage/kv.py
--rw-r--r--   0 runner    (1001) docker     (123)    14184 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/storage/table.py
--rw-r--r--   0 runner    (1001) docker     (123)     1908 2023-03-24 11:07:38.000000 annlite-0.5.8/annlite/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    15898 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1511 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      228 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-03-24 11:08:00.000000 annlite-0.5.8/annlite.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/bindings/
--rw-r--r--   0 runner    (1001) docker     (123)    38735 2023-03-24 11:07:38.000000 annlite-0.5.8/bindings/hnsw_bindings.cpp
--rw-r--r--   0 runner    (1001) docker     (123)  1083425 2023-03-24 11:07:58.000000 annlite-0.5.8/bindings/pq_bindings.cpp
--rw-r--r--   0 runner    (1001) docker     (123)     9965 2023-03-24 11:07:38.000000 annlite-0.5.8/bindings/pq_bindings.pyx
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/include/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/include/hnswlib/
--rw-r--r--   0 runner    (1001) docker     (123)     5519 2023-03-24 11:07:38.000000 annlite-0.5.8/include/hnswlib/bruteforce.h
--rw-r--r--   0 runner    (1001) docker     (123)    25159 2023-03-24 11:07:38.000000 annlite-0.5.8/include/hnswlib/fusefilter.h
--rw-r--r--   0 runner    (1001) docker     (123)    60442 2023-03-24 11:07:38.000000 annlite-0.5.8/include/hnswlib/hnswalg.h
--rw-r--r--   0 runner    (1001) docker     (123)     5372 2023-03-24 11:07:38.000000 annlite-0.5.8/include/hnswlib/hnswlib.h
--rw-r--r--   0 runner    (1001) docker     (123)    12613 2023-03-24 11:07:38.000000 annlite-0.5.8/include/hnswlib/space_ip.h
--rw-r--r--   0 runner    (1001) docker     (123)    10162 2023-03-24 11:07:38.000000 annlite-0.5.8/include/hnswlib/space_l2.h
--rw-r--r--   0 runner    (1001) docker     (123)     2203 2023-03-24 11:07:38.000000 annlite-0.5.8/include/hnswlib/space_pq.h
--rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-03-24 11:07:38.000000 annlite-0.5.8/include/hnswlib/visited_list_pool.h
--rw-r--r--   0 runner    (1001) docker     (123)      165 2023-03-24 11:07:38.000000 annlite-0.5.8/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      111 2023-03-24 11:07:38.000000 annlite-0.5.8/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-24 11:08:00.000000 annlite-0.5.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     6825 2023-03-24 11:07:38.000000 annlite-0.5.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 11:08:00.000000 annlite-0.5.8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     1637 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_codec.py
--rw-r--r--   0 runner    (1001) docker     (123)     2772 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_crud.py
--rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_dump.py
--rw-r--r--   0 runner    (1001) docker     (123)      152 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_enums.py
--rw-r--r--   0 runner    (1001) docker     (123)     6980 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_filter.py
--rw-r--r--   0 runner    (1001) docker     (123)      896 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_hnsw_load_save.py
--rw-r--r--   0 runner    (1001) docker     (123)     9856 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     2189 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_pq_bind.py
--rw-r--r--   0 runner    (1001) docker     (123)     5110 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_pq_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     1847 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_projector.py
--rw-r--r--   0 runner    (1001) docker     (123)     1584 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_projector_index.py
--rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_store.py
--rw-r--r--   0 runner    (1001) docker     (123)     3639 2023-03-24 11:07:38.000000 annlite-0.5.8/tests/test_table.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/
+-rw-r--r--   0 runner    (1001) docker     (123)    11357 2023-04-07 04:10:57.000000 annlite-0.5.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      123 2023-04-07 04:10:57.000000 annlite-0.5.9/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)    15898 2023-04-07 04:11:14.000000 annlite-0.5.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    14977 2023-04-07 04:10:57.000000 annlite-0.5.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite/
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15114 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/container.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite/core/
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite/core/codec/
+-rw-r--r--   0 runner    (1001) docker     (123)       86 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/codec/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      888 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/codec/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13397 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/codec/pq.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5176 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/codec/projector.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2717 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/codec/vq.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite/core/index/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/index/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1426 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/index/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2178 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/index/flat_index.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite/core/index/hnsw/
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/index/hnsw/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6835 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/index/hnsw/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1548 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/core/index/pq_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)      704 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/enums.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14801 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3557 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1086 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/helper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9249 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/hubble_tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35233 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3796 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/math.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2371 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/profile.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite/storage/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/storage/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1300 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/storage/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4702 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/storage/kv.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14184 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/storage/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1908 2023-04-07 04:10:57.000000 annlite-0.5.9/annlite/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)    15898 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1511 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      227 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-07 04:11:14.000000 annlite-0.5.9/annlite.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/bindings/
+-rw-r--r--   0 runner    (1001) docker     (123)    38735 2023-04-07 04:10:57.000000 annlite-0.5.9/bindings/hnsw_bindings.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)  1083488 2023-04-07 04:11:12.000000 annlite-0.5.9/bindings/pq_bindings.cpp
+-rw-r--r--   0 runner    (1001) docker     (123)     9965 2023-04-07 04:10:57.000000 annlite-0.5.9/bindings/pq_bindings.pyx
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/include/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/include/hnswlib/
+-rw-r--r--   0 runner    (1001) docker     (123)     5519 2023-04-07 04:10:57.000000 annlite-0.5.9/include/hnswlib/bruteforce.h
+-rw-r--r--   0 runner    (1001) docker     (123)    25159 2023-04-07 04:10:57.000000 annlite-0.5.9/include/hnswlib/fusefilter.h
+-rw-r--r--   0 runner    (1001) docker     (123)    60442 2023-04-07 04:10:57.000000 annlite-0.5.9/include/hnswlib/hnswalg.h
+-rw-r--r--   0 runner    (1001) docker     (123)     5372 2023-04-07 04:10:57.000000 annlite-0.5.9/include/hnswlib/hnswlib.h
+-rw-r--r--   0 runner    (1001) docker     (123)    12613 2023-04-07 04:10:57.000000 annlite-0.5.9/include/hnswlib/space_ip.h
+-rw-r--r--   0 runner    (1001) docker     (123)    10162 2023-04-07 04:10:57.000000 annlite-0.5.9/include/hnswlib/space_l2.h
+-rw-r--r--   0 runner    (1001) docker     (123)     2203 2023-04-07 04:10:57.000000 annlite-0.5.9/include/hnswlib/space_pq.h
+-rw-r--r--   0 runner    (1001) docker     (123)     1995 2023-04-07 04:10:57.000000 annlite-0.5.9/include/hnswlib/visited_list_pool.h
+-rw-r--r--   0 runner    (1001) docker     (123)      165 2023-04-07 04:10:57.000000 annlite-0.5.9/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      110 2023-04-07 04:10:57.000000 annlite-0.5.9/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 04:11:14.000000 annlite-0.5.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     6825 2023-04-07 04:10:57.000000 annlite-0.5.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 04:11:14.000000 annlite-0.5.9/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     1637 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_codec.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2772 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_crud.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1097 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_dump.py
+-rw-r--r--   0 runner    (1001) docker     (123)      152 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_enums.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6980 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_filter.py
+-rw-r--r--   0 runner    (1001) docker     (123)      896 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_hnsw_load_save.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9856 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2189 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_pq_bind.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5110 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_pq_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1847 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_projector.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1584 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_projector_index.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_store.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3639 2023-04-07 04:10:57.000000 annlite-0.5.9/tests/test_table.py
```

### Comparing `annlite-0.5.8/LICENSE` & `annlite-0.5.9/LICENSE`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/PKG-INFO` & `annlite-0.5.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: annlite
-Version: 0.5.8
+Version: 0.5.9
 Summary: Fast and Light Approximate Nearest Neighbor Search Library integrated with the Jina Ecosystem
 Home-page: https://github.com/jina-ai/annlite
 Download-URL: https://github.com/jina-ai/pqlite/tags
 Author: Jina AI
 Author-email: team@jina.ai
 License: Apache License 2.0
 Keywords: product-quantization approximate-nearest-neighbor hnsw
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: annlite Version: 0.5.8 Summary: Fast and Light
+Metadata-Version: 2.1 Name: annlite Version: 0.5.9 Summary: Fast and Light
 Approximate Nearest Neighbor Search Library integrated with the Jina Ecosystem
 Home-page: https://github.com/jina-ai/annlite Download-URL: https://github.com/
 jina-ai/pqlite/tags Author: Jina AI Author-email: team@jina.ai License: Apache
 License 2.0 Keywords: product-quantization approximate-nearest-neighbor hnsw
 Classifier: Intended Audience :: Developers Classifier: Intended Audience ::
 Science/Research Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent Classifier: Programming Language
```

### Comparing `annlite-0.5.8/README.md` & `annlite-0.5.9/README.md`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/container.py` & `annlite-0.5.9/annlite/container.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/core/codec/base.py` & `annlite-0.5.9/annlite/core/codec/base.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/core/codec/pq.py` & `annlite-0.5.9/annlite/core/codec/pq.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/core/codec/projector.py` & `annlite-0.5.9/annlite/core/codec/projector.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/core/codec/vq.py` & `annlite-0.5.9/annlite/core/codec/vq.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/core/index/base.py` & `annlite-0.5.9/annlite/core/index/base.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/core/index/flat_index.py` & `annlite-0.5.9/annlite/core/index/flat_index.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/core/index/hnsw/index.py` & `annlite-0.5.9/annlite/core/index/hnsw/index.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/core/index/pq_index.py` & `annlite-0.5.9/annlite/core/index/pq_index.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/enums.py` & `annlite-0.5.9/annlite/enums.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/executor.py` & `annlite-0.5.9/annlite/executor.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/filter.py` & `annlite-0.5.9/annlite/filter.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/helper.py` & `annlite-0.5.9/annlite/helper.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/hubble_tools.py` & `annlite-0.5.9/annlite/hubble_tools.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/index.py` & `annlite-0.5.9/annlite/index.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/math.py` & `annlite-0.5.9/annlite/math.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/profile.py` & `annlite-0.5.9/annlite/profile.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/storage/base.py` & `annlite-0.5.9/annlite/storage/base.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/storage/kv.py` & `annlite-0.5.9/annlite/storage/kv.py`

 * *Files 8% similar despite different names*

```diff
@@ -49,38 +49,38 @@
         self._size = len(list(self._db.keys()))
 
         self._is_closed = False
 
     def insert(self, docs: 'DocumentArray'):
         write_batch = WriteBatch(raw_mode=True)
         write_opt = WriteOptions()
-        write_opt.set_sync(True)
+        write_opt.sync = True
         batch_size = 0
         for doc in docs:
             write_batch.put(doc.id.encode(), doc.to_bytes(**self._serialize_config))
             batch_size += 1
         self._db.write(write_batch, write_opt=write_opt)
         self._size += batch_size
 
     def update(self, docs: 'DocumentArray'):
         write_batch = WriteBatch(raw_mode=True)
         write_opt = WriteOptions()
-        write_opt.set_sync(True)
+        write_opt.sync = True
         for doc in docs:
             key = doc.id.encode()
             if key not in self._db:
                 raise ValueError(f'The Doc ({doc.id}) does not exist in database!')
 
             write_batch.put(key, doc.to_bytes(**self._serialize_config))
         self._db.write(write_batch, write_opt=write_opt)
 
     def delete(self, doc_ids: List[str]):
         write_batch = WriteBatch(raw_mode=True)
         write_opt = WriteOptions()
-        write_opt.set_sync(True)
+        write_opt.sync = True
         for doc_id in doc_ids:
             write_batch.delete(doc_id.encode())
         self._db.write(write_batch, write_opt=write_opt)
         self._size -= len(doc_ids)
 
     def get(self, doc_ids: Union[str, list]) -> DocumentArray:
         docs = DocumentArray()
@@ -135,15 +135,15 @@
     def last_transaction_id(self):
         return self._db.latest_sequence_number()
 
     def batched_iterator(self, batch_size: int = 1, **kwargs) -> 'DocumentArray':
         count = 0
         docs = DocumentArray()
 
-        read_opt = ReadOptions(raw_mode=True)
+        read_opt = ReadOptions()
 
         for value in self._db.values(read_opt=read_opt):
             doc = Document.from_bytes(value, **self._serialize_config)
             docs.append(doc)
             count += 1
 
             if count == batch_size:
```

### Comparing `annlite-0.5.8/annlite/storage/table.py` & `annlite-0.5.9/annlite/storage/table.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite/utils.py` & `annlite-0.5.9/annlite/utils.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/annlite.egg-info/PKG-INFO` & `annlite-0.5.9/annlite.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: annlite
-Version: 0.5.8
+Version: 0.5.9
 Summary: Fast and Light Approximate Nearest Neighbor Search Library integrated with the Jina Ecosystem
 Home-page: https://github.com/jina-ai/annlite
 Download-URL: https://github.com/jina-ai/pqlite/tags
 Author: Jina AI
 Author-email: team@jina.ai
 License: Apache License 2.0
 Keywords: product-quantization approximate-nearest-neighbor hnsw
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: annlite Version: 0.5.8 Summary: Fast and Light
+Metadata-Version: 2.1 Name: annlite Version: 0.5.9 Summary: Fast and Light
 Approximate Nearest Neighbor Search Library integrated with the Jina Ecosystem
 Home-page: https://github.com/jina-ai/annlite Download-URL: https://github.com/
 jina-ai/pqlite/tags Author: Jina AI Author-email: team@jina.ai License: Apache
 License 2.0 Keywords: product-quantization approximate-nearest-neighbor hnsw
 Classifier: Intended Audience :: Developers Classifier: Intended Audience ::
 Science/Research Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent Classifier: Programming Language
```

### Comparing `annlite-0.5.8/annlite.egg-info/SOURCES.txt` & `annlite-0.5.9/annlite.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/bindings/hnsw_bindings.cpp` & `annlite-0.5.9/bindings/hnsw_bindings.cpp`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/bindings/pq_bindings.cpp` & `annlite-0.5.9/bindings/pq_bindings.cpp`

 * *Files 0% similar despite different names*

```diff
@@ -1,16 +1,16 @@
-/* Generated by Cython 0.29.33 */
+/* Generated by Cython 0.29.34 */
 
 /* BEGIN: Cython Metadata
 {
     "distutils": {
         "depends": [],
         "include_dirs": [
-            "/tmp/build-env-9d4f38za/lib/python3.7/site-packages/pybind11/include",
-            "/tmp/build-env-9d4f38za/lib/python3.7/site-packages/numpy/core/include",
+            "/tmp/build-env-4tno18gw/lib/python3.7/site-packages/pybind11/include",
+            "/tmp/build-env-4tno18gw/lib/python3.7/site-packages/numpy/core/include",
             "/opt/hostedtoolcache/Python/3.7.16/x64/include/python3.7m"
         ],
         "language": "c++",
         "name": "annlite.pq_bind",
         "sources": [
             "./bindings/pq_bindings.pyx"
         ]
@@ -24,16 +24,16 @@
 #endif /* PY_SSIZE_T_CLEAN */
 #include "Python.h"
 #ifndef Py_PYTHON_H
     #error Python headers needed to compile C extensions, please install development version of Python.
 #elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
     #error Cython requires Python 2.6+ or Python 3.3+.
 #else
-#define CYTHON_ABI "0_29_33"
-#define CYTHON_HEX_VERSION 0x001D21F0
+#define CYTHON_ABI "0_29_34"
+#define CYTHON_HEX_VERSION 0x001D22F0
 #define CYTHON_FUTURE_DIVISION 0
 #include <stddef.h>
 #ifndef offsetof
   #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
 #endif
 #if !defined(WIN32) && !defined(MS_WINDOWS)
   #ifndef __stdcall
@@ -218,15 +218,15 @@
   #elif !defined(CYTHON_USE_ASYNC_SLOTS)
     #define CYTHON_USE_ASYNC_SLOTS 1
   #endif
   #if PY_VERSION_HEX < 0x02070000
     #undef CYTHON_USE_PYLONG_INTERNALS
     #define CYTHON_USE_PYLONG_INTERNALS 0
   #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
-    #define CYTHON_USE_PYLONG_INTERNALS 1
+    #define CYTHON_USE_PYLONG_INTERNALS (PY_VERSION_HEX < 0x030C00A5)
   #endif
   #ifndef CYTHON_USE_PYLIST_INTERNALS
     #define CYTHON_USE_PYLIST_INTERNALS 1
   #endif
   #ifndef CYTHON_USE_UNICODE_INTERNALS
     #define CYTHON_USE_UNICODE_INTERNALS 1
   #endif
@@ -257,15 +257,15 @@
   #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
     #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
   #endif
   #ifndef CYTHON_USE_TP_FINALIZE
     #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
   #endif
   #ifndef CYTHON_USE_DICT_VERSIONS
-    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
+    #define CYTHON_USE_DICT_VERSIONS ((PY_VERSION_HEX >= 0x030600B1) && (PY_VERSION_HEX < 0x030C00A5))
   #endif
   #if PY_VERSION_HEX >= 0x030B00A4
     #undef CYTHON_USE_EXC_INFO_STACK
     #define CYTHON_USE_EXC_INFO_STACK 0
   #elif !defined(CYTHON_USE_EXC_INFO_STACK)
     #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
   #endif
@@ -22912,28 +22912,28 @@
                             "BaseException");
             goto bad;
         }
         PyException_SetCause(value, fixed_cause);
     }
     PyErr_SetObject(type, value);
     if (tb) {
-#if CYTHON_COMPILING_IN_PYPY
-        PyObject *tmp_type, *tmp_value, *tmp_tb;
-        PyErr_Fetch(&tmp_type, &tmp_value, &tmp_tb);
-        Py_INCREF(tb);
-        PyErr_Restore(tmp_type, tmp_value, tb);
-        Py_XDECREF(tmp_tb);
-#else
+#if CYTHON_FAST_THREAD_STATE
         PyThreadState *tstate = __Pyx_PyThreadState_Current;
         PyObject* tmp_tb = tstate->curexc_traceback;
         if (tb != tmp_tb) {
             Py_INCREF(tb);
             tstate->curexc_traceback = tb;
             Py_XDECREF(tmp_tb);
         }
+#else
+        PyObject *tmp_type, *tmp_value, *tmp_tb;
+        PyErr_Fetch(&tmp_type, &tmp_value, &tmp_tb);
+        Py_INCREF(tb);
+        PyErr_Restore(tmp_type, tmp_value, tb);
+        Py_XDECREF(tmp_tb);
 #endif
     }
 bad:
     Py_XDECREF(owned_instance);
     return;
 }
 #endif
```

### Comparing `annlite-0.5.8/bindings/pq_bindings.pyx` & `annlite-0.5.9/bindings/pq_bindings.pyx`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/include/hnswlib/bruteforce.h` & `annlite-0.5.9/include/hnswlib/bruteforce.h`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/include/hnswlib/fusefilter.h` & `annlite-0.5.9/include/hnswlib/fusefilter.h`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/include/hnswlib/hnswalg.h` & `annlite-0.5.9/include/hnswlib/hnswalg.h`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/include/hnswlib/hnswlib.h` & `annlite-0.5.9/include/hnswlib/hnswlib.h`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/include/hnswlib/space_ip.h` & `annlite-0.5.9/include/hnswlib/space_ip.h`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/include/hnswlib/space_l2.h` & `annlite-0.5.9/include/hnswlib/space_l2.h`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/include/hnswlib/space_pq.h` & `annlite-0.5.9/include/hnswlib/space_pq.h`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/include/hnswlib/visited_list_pool.h` & `annlite-0.5.9/include/hnswlib/visited_list_pool.h`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/setup.py` & `annlite-0.5.9/setup.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_codec.py` & `annlite-0.5.9/tests/test_codec.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_crud.py` & `annlite-0.5.9/tests/test_crud.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_dump.py` & `annlite-0.5.9/tests/test_dump.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_filter.py` & `annlite-0.5.9/tests/test_filter.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_hnsw_load_save.py` & `annlite-0.5.9/tests/test_hnsw_load_save.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_index.py` & `annlite-0.5.9/tests/test_index.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_pq_bind.py` & `annlite-0.5.9/tests/test_pq_bind.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_pq_index.py` & `annlite-0.5.9/tests/test_pq_index.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_projector.py` & `annlite-0.5.9/tests/test_projector.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_projector_index.py` & `annlite-0.5.9/tests/test_projector_index.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_store.py` & `annlite-0.5.9/tests/test_store.py`

 * *Files identical despite different names*

### Comparing `annlite-0.5.8/tests/test_table.py` & `annlite-0.5.9/tests/test_table.py`

 * *Files identical despite different names*

