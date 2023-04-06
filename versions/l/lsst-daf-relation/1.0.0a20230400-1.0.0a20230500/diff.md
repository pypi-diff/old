# Comparing `tmp/lsst-daf-relation-1.0.0a20230400.tar.gz` & `tmp/lsst-daf-relation-1.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-daf-relation-1.0.0a20230400.tar", last modified: Thu Jan 26 09:56:12 2023, max compression
+gzip compressed data, was "lsst-daf-relation-1.0.0a20230500.tar", last modified: Thu Feb  2 14:05:24 2023, max compression
```

## Comparing `lsst-daf-relation-1.0.0a20230400.tar` & `lsst-daf-relation-1.0.0a20230500.tar`

### file list

```diff
@@ -1,61 +1,61 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.621492 lsst-daf-relation-1.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)    35147 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1377 2023-01-26 09:56:12.621492 lsst-daf-relation-1.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      591 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     2576 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.613492 lsst-daf-relation-1.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.617492 lsst-daf-relation-1.0.0a20230400/python/lsst/
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.617492 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/
--rw-r--r--   0 runner    (1001) docker     (123)       67 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.617492 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/
--rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8302 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_binary_operation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.617492 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/
--rw-r--r--   0 runner    (1001) docker     (123)     1020 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7455 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/_container.py
--rw-r--r--   0 runner    (1001) docker     (123)    18969 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/_expression.py
--rw-r--r--   0 runner    (1001) docker     (123)    11999 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/_predicate.py
--rw-r--r--   0 runner    (1001) docker     (123)     1917 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/_tag.py
--rw-r--r--   0 runner    (1001) docker     (123)     6987 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_diagnostics.py
--rw-r--r--   0 runner    (1001) docker     (123)    16054 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)     5625 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_leaf_relation.py
--rw-r--r--   0 runner    (1001) docker     (123)     5090 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_marker_relation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2457 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_materialization.py
--rw-r--r--   0 runner    (1001) docker     (123)     7719 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operation_relations.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.621492 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/
--rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5491 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_calculation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2384 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_chain.py
--rw-r--r--   0 runner    (1001) docker     (123)     2826 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_deduplication.py
--rw-r--r--   0 runner    (1001) docker     (123)    15632 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_join.py
--rw-r--r--   0 runner    (1001) docker     (123)     5224 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_projection.py
--rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_selection.py
--rw-r--r--   0 runner    (1001) docker     (123)     5801 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_slice.py
--rw-r--r--   0 runner    (1001) docker     (123)     4887 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_sort.py
--rw-r--r--   0 runner    (1001) docker     (123)    11830 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_processor.py
--rw-r--r--   0 runner    (1001) docker     (123)    31805 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_relation.py
--rw-r--r--   0 runner    (1001) docker     (123)     2381 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_transfer.py
--rw-r--r--   0 runner    (1001) docker     (123)    20905 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_unary_operation.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.621492 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/iteration/
--rw-r--r--   0 runner    (1001) docker     (123)      973 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/iteration/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    16996 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/iteration/_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     8842 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/iteration/_row_iterable.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/py.typed
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.621492 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/sql/
--rw-r--r--   0 runner    (1001) docker     (123)      991 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/sql/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    38073 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/sql/_engine.py
--rw-r--r--   0 runner    (1001) docker     (123)     2264 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/sql/_payload.py
--rw-r--r--   0 runner    (1001) docker     (123)    11347 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/sql/_select.py
--rw-r--r--   0 runner    (1001) docker     (123)     6582 2023-01-26 09:55:59.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/tests.py
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-01-26 09:56:12.000000 lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:12.621492 lsst-daf-relation-1.0.0a20230400/python/lsst_daf_relation.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1377 2023-01-26 09:56:12.000000 lsst-daf-relation-1.0.0a20230400/python/lsst_daf_relation.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2018 2023-01-26 09:56:12.000000 lsst-daf-relation-1.0.0a20230400/python/lsst_daf_relation.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:12.000000 lsst-daf-relation-1.0.0a20230400/python/lsst_daf_relation.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-01-26 09:56:12.000000 lsst-daf-relation-1.0.0a20230400/python/lsst_daf_relation.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 09:56:12.000000 lsst-daf-relation-1.0.0a20230400/python/lsst_daf_relation.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:12.000000 lsst-daf-relation-1.0.0a20230400/python/lsst_daf_relation.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      186 2023-01-26 09:56:12.621492 lsst-daf-relation-1.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.676133 lsst-daf-relation-1.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)    35147 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1377 2023-02-02 14:05:24.676133 lsst-daf-relation-1.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      591 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     2576 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.672133 lsst-daf-relation-1.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.672133 lsst-daf-relation-1.0.0a20230500/python/lsst/
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.672133 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/
+-rw-r--r--   0 runner    (1001) docker     (123)       67 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.676133 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/
+-rw-r--r--   0 runner    (1001) docker     (123)     1371 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8302 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_binary_operation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.676133 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/
+-rw-r--r--   0 runner    (1001) docker     (123)     1020 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7455 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/_container.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18969 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/_expression.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11999 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/_predicate.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1917 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/_tag.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6987 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_diagnostics.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16054 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5625 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_leaf_relation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5090 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_marker_relation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2457 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_materialization.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7719 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operation_relations.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.676133 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/
+-rw-r--r--   0 runner    (1001) docker     (123)     1118 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5491 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_calculation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2384 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_chain.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2825 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_deduplication.py
+-rw-r--r--   0 runner    (1001) docker     (123)    15632 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_join.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5224 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_projection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4818 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_selection.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5801 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_slice.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4886 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_sort.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11830 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_processor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    31766 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_relation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2381 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_transfer.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20905 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_unary_operation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.676133 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/iteration/
+-rw-r--r--   0 runner    (1001) docker     (123)      973 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/iteration/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16996 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/iteration/_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8842 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/iteration/_row_iterable.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/py.typed
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.676133 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/sql/
+-rw-r--r--   0 runner    (1001) docker     (123)      991 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/sql/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38385 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/sql/_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2264 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/sql/_payload.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11347 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/sql/_select.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6633 2023-02-02 14:05:09.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/tests.py
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-02-02 14:05:24.000000 lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:24.676133 lsst-daf-relation-1.0.0a20230500/python/lsst_daf_relation.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1377 2023-02-02 14:05:24.000000 lsst-daf-relation-1.0.0a20230500/python/lsst_daf_relation.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2018 2023-02-02 14:05:24.000000 lsst-daf-relation-1.0.0a20230500/python/lsst_daf_relation.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:24.000000 lsst-daf-relation-1.0.0a20230500/python/lsst_daf_relation.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-02-02 14:05:24.000000 lsst-daf-relation-1.0.0a20230500/python/lsst_daf_relation.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:05:24.000000 lsst-daf-relation-1.0.0a20230500/python/lsst_daf_relation.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:24.000000 lsst-daf-relation-1.0.0a20230500/python/lsst_daf_relation.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      186 2023-02-02 14:05:24.680133 lsst-daf-relation-1.0.0a20230500/setup.cfg
```

### Comparing `lsst-daf-relation-1.0.0a20230400/LICENSE` & `lsst-daf-relation-1.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/PKG-INFO` & `lsst-daf-relation-1.0.0a20230500/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-daf-relation
-Version: 1.0.0a20230400
+Version: 1.0.0a20230500
 Summary: An abstract system for operating on SQL and in-memory tables with relational algebra.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/daf_relation
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-daf-relation-1.0.0a20230400/README.md` & `lsst-daf-relation-1.0.0a20230500/README.md`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/pyproject.toml` & `lsst-daf-relation-1.0.0a20230500/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/__init__.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_binary_operation.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_binary_operation.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/__init__.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/_container.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/_container.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/_expression.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/_expression.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/_predicate.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/_predicate.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_columns/_tag.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_columns/_tag.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_diagnostics.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_diagnostics.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_engine.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_engine.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_exceptions.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_exceptions.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_leaf_relation.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_leaf_relation.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_marker_relation.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_marker_relation.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_materialization.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_materialization.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operation_relations.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operation_relations.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/__init__.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_calculation.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_calculation.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_chain.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_chain.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_deduplication.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_deduplication.py`

 * *Files 2% similar despite different names*

```diff
@@ -62,15 +62,15 @@
         # problematic, rather than just checking isinstance(Projection).
         if not current.columns >= current.target.columns:
             return UnaryCommutator(
                 first=None,
                 second=current.operation,
                 done=False,
                 messages=(
-                    f"deduplication columns would change from "
+                    "deduplication columns would change from "
                     f"{set(current.columns)} to {set(current.target.columns)}",
                 ),
             )
         if current.operation.is_count_dependent:
             return UnaryCommutator(
                 first=None,
                 second=current.operation,
```

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_join.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_join.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_projection.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_projection.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_selection.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_selection.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_slice.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_slice.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_operations/_sort.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_operations/_sort.py`

 * *Files 0% similar despite different names*

```diff
@@ -39,15 +39,14 @@
     from .._columns import ColumnExpression
     from .._engine import Engine
     from .._relation import Relation
 
 
 @dataclasses.dataclass
 class SortTerm:
-
     expression: ColumnExpression
     ascending: bool = True
 
     def __str__(self) -> str:
         return f"{'' if self.ascending else '-'}{self.expression}"
```

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_processor.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_processor.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_relation.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_relation.py`

 * *Files 0% similar despite different names*

```diff
@@ -685,18 +685,15 @@
             in {
                 "LeafRelation",
                 "UnaryOperationRelation",
                 "BinaryOperationRelation",
                 "MarkerRelation",
             }
             or cls.__base__.__name__ != "Relation"
-        ), (
-            "Relation inheritance is closed to predefined types "
-            "in daf_relation and MarkerRelation subclasses."
-        )
+        ), "Relation inheritance is closed to predefined types in daf_relation and MarkerRelation subclasses."
 
     @property
     @_copy_relation_docs
     def is_join_identity(self: Relation) -> bool:
         return not self.columns and self.max_rows == 1 and self.min_rows == 1
 
     @property
```

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_transfer.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_transfer.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/_unary_operation.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/_unary_operation.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/iteration/__init__.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/iteration/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/iteration/_engine.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/iteration/_engine.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/iteration/_row_iterable.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/iteration/_row_iterable.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/sql/__init__.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/sql/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/sql/_engine.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/sql/_engine.py`

 * *Files 1% similar despite different names*

```diff
@@ -75,15 +75,15 @@
 
 
 _L = TypeVar("_L")
 
 
 @dataclasses.dataclass(repr=False, eq=False, kw_only=True)
 class Engine(
-    GenericConcreteEngine[Callable[..., sqlalchemy.sql.ColumnElement]],
+    GenericConcreteEngine[Callable[..., sqlalchemy.sql.ColumnElement[Any]]],
     Generic[_L],
 ):
     """A concrete engine class for relations backed by a SQL database.
 
     See the `.sql` module documentation for details.
     """
 
@@ -188,15 +188,17 @@
         # Docstring inherited.
         select_columns: list[sqlalchemy.sql.ColumnElement] = []
         self.handle_empty_columns(select_columns)
         return Payload[_L](sqlalchemy.sql.select(*select_columns).subquery())
 
     def get_doomed_payload(self, columns: Set[ColumnTag]) -> Payload[_L]:
         # Docstring inherited.
-        select_columns = [sqlalchemy.sql.literal(None).label(tag.qualified_name) for tag in columns]
+        select_columns: list[sqlalchemy.sql.ColumnElement] = [
+            sqlalchemy.sql.literal(None).label(tag.qualified_name) for tag in columns
+        ]
         self.handle_empty_columns(select_columns)
         subquery = sqlalchemy.sql.select(*select_columns).subquery()
         return Payload(
             subquery,
             where=[sqlalchemy.sql.literal(False)],
             columns_available=self.extract_mapping(columns, subquery.columns),
         )
@@ -439,15 +441,15 @@
         Notes
         -----
         This method is responsible for handling the case where ``items`` is
         empty, typically by delegating to `handle_empty_columns`.
 
         This method must be overridden to support a custom logical columns.
         """
-        select_columns = [
+        select_columns: list[sqlalchemy.sql.ColumnElement] = [
             cast(sqlalchemy.sql.ColumnElement, logical_column).label(tag.qualified_name)
             for tag, logical_column in items
         ]
         select_columns.extend(extra)
         self.handle_empty_columns(select_columns)
         return sqlalchemy.sql.select(*select_columns).select_from(sql_from)
 
@@ -528,14 +530,15 @@
         -----
         This method handles trees terminated with `Select`, the operation
         relation types managed by `Select`, and `Chain` operations nested
         directly as the `skip_to` target of a `Select`.  It delegates to
         `to_payload` for all other relation types.
         """
         columns_available: Mapping[ColumnTag, _L] | None = None
+        executable: sqlalchemy.sql.Select | sqlalchemy.sql.CompoundSelect
         match select.skip_to:
             case BinaryOperationRelation(operation=Chain(), lhs=lhs, rhs=rhs):
                 lhs_executable = self._select_to_executable(cast(Select, lhs), extra_columns)
                 rhs_executable = self._select_to_executable(cast(Select, rhs), extra_columns)
                 if select.has_deduplication:
                     executable = sqlalchemy.sql.union(lhs_executable, rhs_executable)
                 else:
@@ -610,15 +613,18 @@
             ):
                 lhs_payload = self.to_payload(lhs)
                 rhs_payload = self.to_payload(rhs)
                 assert common_columns is not None, "Guaranteed by Join.apply and PartialJoin.apply."
                 on_terms: list[sqlalchemy.sql.ColumnElement] = []
                 if common_columns:
                     on_terms.extend(
-                        lhs_payload.columns_available[tag] == rhs_payload.columns_available[tag]
+                        cast(
+                            sqlalchemy.sql.ColumnElement,
+                            lhs_payload.columns_available[tag] == rhs_payload.columns_available[tag],
+                        )
                         for tag in common_columns
                     )
                 columns_available = {**lhs_payload.columns_available, **rhs_payload.columns_available}
                 if predicate.as_trivial() is not True:
                     on_terms.extend(self.convert_flattened_predicate(predicate, columns_available))
                 on_clause: sqlalchemy.sql.ColumnElement
                 if not on_terms:
@@ -674,15 +680,15 @@
             case ColumnLiteral(value=value):
                 return self.convert_column_literal(value)
             case ColumnReference(tag=tag):
                 return columns_available[tag]
             case ColumnFunction(name=name, args=args):
                 sql_args = [self.convert_column_expression(arg, columns_available) for arg in args]
                 if (function := self.get_function(name)) is not None:
-                    return function(*sql_args)
+                    return cast(_L, function(*sql_args))
                 return getattr(sql_args[0], name)(*sql_args[1:])
         raise AssertionError(
             f"matches should be exhaustive and all branches should return; got {expression!r}."
         )
 
     def convert_column_literal(self, value: Any) -> _L:
         """Convert a Python literal value to a logical column.
@@ -701,15 +707,15 @@
         -----
         This method must be overridden to support a custom logical columns.
 
         See Also
         --------
         :ref:`lsst.daf.relation-sql-logical-columns`
         """
-        return sqlalchemy.sql.literal(value)
+        return cast(_L, sqlalchemy.sql.literal(value))
 
     def expect_column_scalar(self, logical_column: _L) -> sqlalchemy.sql.ColumnElement:
         """Convert a logical column value to a SQLAlchemy expression.
 
         Parameters
         ----------
         logical_column
```

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/sql/_payload.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/sql/_payload.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/sql/_select.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/sql/_select.py`

 * *Files identical despite different names*

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst/daf/relation/tests.py` & `lsst-daf-relation-1.0.0a20230500/python/lsst/daf/relation/tests.py`

 * *Files 5% similar despite different names*

```diff
@@ -29,16 +29,16 @@
 import re
 import unittest
 from typing import Any
 
 try:
     from sqlalchemy.dialects.sqlite.pysqlite import dialect as sql_dialect
 except ImportError:
-
-    def sql_dialect() -> Any:
+    # MyPy doesn't like this trick.
+    def sql_dialect() -> Any:  # type: ignore
         raise unittest.SkipTest("sqlalchemy SQLite dialect not available")
 
 
 from ._operation_relations import BinaryOperationRelation, UnaryOperationRelation
 from ._relation import Relation
```

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst_daf_relation.egg-info/PKG-INFO` & `lsst-daf-relation-1.0.0a20230500/python/lsst_daf_relation.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-daf-relation
-Version: 1.0.0a20230400
+Version: 1.0.0a20230500
 Summary: An abstract system for operating on SQL and in-memory tables with relational algebra.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/daf_relation
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-daf-relation-1.0.0a20230400/python/lsst_daf_relation.egg-info/SOURCES.txt` & `lsst-daf-relation-1.0.0a20230500/python/lsst_daf_relation.egg-info/SOURCES.txt`

 * *Files identical despite different names*

