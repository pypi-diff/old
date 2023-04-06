# Comparing `tmp/sagemath-environment-9.8b7.tar.gz` & `tmp/sagemath-environment-9.8rc0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sagemath-environment-9.8b7.tar", last modified: Thu Jan 19 06:51:53 2023, max compression
+gzip compressed data, was "sagemath-environment-9.8rc0.tar", last modified: Sun Jan 29 23:47:20 2023, max compression
```

## Comparing `sagemath-environment-9.8b7.tar` & `sagemath-environment-9.8rc0.tar`

### file list

```diff
@@ -1,107 +1,107 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:53.810954 sagemath-environment-9.8b7/
--rw-r--r--   0 runner    (1001) docker     (123)      293 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     2757 2023-01-19 06:51:53.810954 sagemath-environment-9.8b7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1519 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/VERSION.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:53.802954 sagemath-environment-9.8b7/bin/
--rwxr-xr-x   0 runner    (1001) docker     (123)      793 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/math-readline
--rwxr-xr-x   0 runner    (1001) docker     (123)    43257 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage
--rwxr-xr-x   0 runner    (1001) docker     (123)      651 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-cachegrind
--rwxr-xr-x   0 runner    (1001) docker     (123)      442 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-callgrind
--rwxr-xr-x   0 runner    (1001) docker     (123)     7405 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-cleaner
--rwxr-xr-x   0 runner    (1001) docker     (123)    10212 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-coverage
--rwxr-xr-x   0 runner    (1001) docker     (123)     1363 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-cython
--rw-r--r--   0 runner    (1001) docker     (123)    21921 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-env
--rw-r--r--   0 runner    (1001) docker     (123)     2071 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-env-config.in
--rwxr-xr-x   0 runner    (1001) docker     (123)      246 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-eval
--rwxr-xr-x   0 runner    (1001) docker     (123)     6144 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-fixdoctests
--rwxr-xr-x   0 runner    (1001) docker     (123)       99 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-grep
--rwxr-xr-x   0 runner    (1001) docker     (123)       93 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-grepdoc
--rwxr-xr-x   0 runner    (1001) docker     (123)      234 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-inline-fortran
--rwxr-xr-x   0 runner    (1001) docker     (123)     1345 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-ipynb2rst
--rwxr-xr-x   0 runner    (1001) docker     (123)      360 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-ipython
--rwxr-xr-x   0 runner    (1001) docker     (123)     3668 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-list-packages
--rwxr-xr-x   0 runner    (1001) docker     (123)      613 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-massif
--rwxr-xr-x   0 runner    (1001) docker     (123)     8347 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-notebook
--rwxr-xr-x   0 runner    (1001) docker     (123)     3141 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-num-threads.py
--rwxr-xr-x   0 runner    (1001) docker     (123)      595 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-omega
--rwxr-xr-x   0 runner    (1001) docker     (123)    10614 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-preparse
--rwxr-xr-x   0 runner    (1001) docker     (123)       28 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-python
--rwxr-xr-x   0 runner    (1001) docker     (123)     1524 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-rebase.bat
--rwxr-xr-x   0 runner    (1001) docker     (123)     2260 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-rebase.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)     1752 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-rebaseall.bat
--rwxr-xr-x   0 runner    (1001) docker     (123)      747 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-rebaseall.sh
--rwxr-xr-x   0 runner    (1001) docker     (123)      707 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-run
--rwxr-xr-x   0 runner    (1001) docker     (123)      253 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-run-cython
--rwxr-xr-x   0 runner    (1001) docker     (123)    11131 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-runtests
--rw-r--r--   0 runner    (1001) docker     (123)     1607 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-src-env-config.in
--rwxr-xr-x   0 runner    (1001) docker     (123)     6227 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-startuptime.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     3597 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-update-version
--rwxr-xr-x   0 runner    (1001) docker     (123)     1133 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-valgrind
--rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-venv-config
--rw-r--r--   0 runner    (1001) docker     (123)      404 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/bin/sage-version.sh
--rw-r--r--   0 runner    (1001) docker     (123)      171 2023-01-19 06:47:53.000000 sagemath-environment-9.8b7/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      260 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/pyproject.toml.m4
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/requirements.txt.m4
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:53.806954 sagemath-environment-9.8b7/sage/
--rw-r--r--   0 runner    (1001) docker     (123)      138 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/all__sagemath_environment.py
--rw-r--r--   0 runner    (1001) docker     (123)    20998 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/env.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:53.806954 sagemath-environment-9.8b7/sage/features/
--rw-r--r--   0 runner    (1001) docker     (123)    30477 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      816 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/all.py
--rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/bliss.py
--rw-r--r--   0 runner    (1001) docker     (123)      795 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/cddlib.py
--rw-r--r--   0 runner    (1001) docker     (123)     2239 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/csdp.py
--rw-r--r--   0 runner    (1001) docker     (123)      815 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/cython.py
--rw-r--r--   0 runner    (1001) docker     (123)     6459 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/databases.py
--rw-r--r--   0 runner    (1001) docker     (123)     1303 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/dvipng.py
--rw-r--r--   0 runner    (1001) docker     (123)     4715 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/ffmpeg.py
--rw-r--r--   0 runner    (1001) docker     (123)     1639 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/four_ti_2.py
--rw-r--r--   0 runner    (1001) docker     (123)     1710 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/gap.py
--rw-r--r--   0 runner    (1001) docker     (123)      651 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/gfan.py
--rw-r--r--   0 runner    (1001) docker     (123)     5445 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/graph_generators.py
--rw-r--r--   0 runner    (1001) docker     (123)     3418 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/graphviz.py
--rw-r--r--   0 runner    (1001) docker     (123)      916 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/igraph.py
--rw-r--r--   0 runner    (1001) docker     (123)     4958 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/imagemagick.py
--rw-r--r--   0 runner    (1001) docker     (123)     7157 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/interfaces.py
--rw-r--r--   0 runner    (1001) docker     (123)     1507 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/internet.py
--rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/join_feature.py
--rw-r--r--   0 runner    (1001) docker     (123)     1904 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/kenzo.py
--rw-r--r--   0 runner    (1001) docker     (123)     7834 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/latex.py
--rw-r--r--   0 runner    (1001) docker     (123)     1914 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/latte.py
--rw-r--r--   0 runner    (1001) docker     (123)     5231 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/lrs.py
--rw-r--r--   0 runner    (1001) docker     (123)      882 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/mcqd.py
--rw-r--r--   0 runner    (1001) docker     (123)      927 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/meataxe.py
--rw-r--r--   0 runner    (1001) docker     (123)     3316 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/mip_backends.py
--rw-r--r--   0 runner    (1001) docker     (123)     1787 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/msolve.py
--rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/nauty.py
--rw-r--r--   0 runner    (1001) docker     (123)      862 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/normaliz.py
--rw-r--r--   0 runner    (1001) docker     (123)     2122 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/palp.py
--rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/pandoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1367 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/pdf2svg.py
--rw-r--r--   0 runner    (1001) docker     (123)      759 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/phitigra.py
--rw-r--r--   0 runner    (1001) docker     (123)     6464 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/pkg_systems.py
--rw-r--r--   0 runner    (1001) docker     (123)      875 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/polymake.py
--rw-r--r--   0 runner    (1001) docker     (123)     2193 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/poppler.py
--rw-r--r--   0 runner    (1001) docker     (123)     5041 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/rubiks.py
--rw-r--r--   0 runner    (1001) docker     (123)     8779 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/sagemath.py
--rw-r--r--   0 runner    (1001) docker     (123)      709 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/singular.py
--rw-r--r--   0 runner    (1001) docker     (123)      785 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/sphinx.py
--rw-r--r--   0 runner    (1001) docker     (123)      744 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/sage/features/tdlib.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:53.810954 sagemath-environment-9.8b7/sage/misc/
--rw-r--r--   0 runner    (1001) docker     (123)       50 2023-01-19 06:47:41.000000 sagemath-environment-9.8b7/sage/misc/all__sagemath_environment.py
--rw-r--r--   0 runner    (1001) docker     (123)    25028 2023-01-19 06:47:41.000000 sagemath-environment-9.8b7/sage/misc/package.py
--rw-r--r--   0 runner    (1001) docker     (123)     8090 2023-01-19 06:47:41.000000 sagemath-environment-9.8b7/sage/misc/package_dir.py
--rw-r--r--   0 runner    (1001) docker     (123)    19226 2023-01-19 06:47:41.000000 sagemath-environment-9.8b7/sage/misc/temporary_file.py
--rw-r--r--   0 runner    (1001) docker     (123)    12080 2023-01-19 06:47:41.000000 sagemath-environment-9.8b7/sage/misc/viewer.py
--rw-r--r--   0 runner    (1001) docker     (123)      230 2023-01-19 06:47:41.000000 sagemath-environment-9.8b7/sage/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-19 06:51:53.810954 sagemath-environment-9.8b7/sagemath_environment.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2757 2023-01-19 06:51:52.000000 sagemath-environment-9.8b7/sagemath_environment.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2241 2023-01-19 06:51:53.000000 sagemath-environment-9.8b7/sagemath_environment.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-19 06:51:52.000000 sagemath-environment-9.8b7/sagemath_environment.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      183 2023-01-19 06:51:52.000000 sagemath-environment-9.8b7/sagemath_environment.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-19 06:51:52.000000 sagemath-environment-9.8b7/sagemath_environment.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1597 2023-01-19 06:51:53.810954 sagemath-environment-9.8b7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2706 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/setup.cfg.m4
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/setup.py
--rw-r--r--   0 runner    (1001) docker     (123)     1828 2023-01-19 06:47:40.000000 sagemath-environment-9.8b7/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:20.001610 sagemath-environment-9.8rc0/
+-rw-r--r--   0 runner    (1001) docker     (123)      293 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     2758 2023-01-29 23:47:20.001610 sagemath-environment-9.8rc0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1519 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/VERSION.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:19.997610 sagemath-environment-9.8rc0/bin/
+-rwxr-xr-x   0 runner    (1001) docker     (123)      793 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/math-readline
+-rwxr-xr-x   0 runner    (1001) docker     (123)    43257 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage
+-rwxr-xr-x   0 runner    (1001) docker     (123)      651 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-cachegrind
+-rwxr-xr-x   0 runner    (1001) docker     (123)      442 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-callgrind
+-rwxr-xr-x   0 runner    (1001) docker     (123)     7405 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-cleaner
+-rwxr-xr-x   0 runner    (1001) docker     (123)    10212 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-coverage
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1363 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-cython
+-rw-r--r--   0 runner    (1001) docker     (123)    21921 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-env
+-rw-r--r--   0 runner    (1001) docker     (123)     2071 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-env-config.in
+-rwxr-xr-x   0 runner    (1001) docker     (123)      246 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-eval
+-rwxr-xr-x   0 runner    (1001) docker     (123)     6144 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-fixdoctests
+-rwxr-xr-x   0 runner    (1001) docker     (123)       99 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-grep
+-rwxr-xr-x   0 runner    (1001) docker     (123)       93 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-grepdoc
+-rwxr-xr-x   0 runner    (1001) docker     (123)      234 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-inline-fortran
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1345 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-ipynb2rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)      360 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-ipython
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3668 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-list-packages
+-rwxr-xr-x   0 runner    (1001) docker     (123)      613 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-massif
+-rwxr-xr-x   0 runner    (1001) docker     (123)     8347 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-notebook
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3141 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-num-threads.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)      595 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-omega
+-rwxr-xr-x   0 runner    (1001) docker     (123)    10614 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-preparse
+-rwxr-xr-x   0 runner    (1001) docker     (123)       28 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-python
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1524 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-rebase.bat
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2260 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-rebase.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1752 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-rebaseall.bat
+-rwxr-xr-x   0 runner    (1001) docker     (123)      747 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-rebaseall.sh
+-rwxr-xr-x   0 runner    (1001) docker     (123)      707 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-run
+-rwxr-xr-x   0 runner    (1001) docker     (123)      253 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-run-cython
+-rwxr-xr-x   0 runner    (1001) docker     (123)    11131 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-runtests
+-rw-r--r--   0 runner    (1001) docker     (123)     1607 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-src-env-config.in
+-rwxr-xr-x   0 runner    (1001) docker     (123)     6227 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-startuptime.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3597 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-update-version
+-rwxr-xr-x   0 runner    (1001) docker     (123)     1133 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-valgrind
+-rw-r--r--   0 runner    (1001) docker     (123)     1213 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-venv-config
+-rw-r--r--   0 runner    (1001) docker     (123)      400 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/bin/sage-version.sh
+-rw-r--r--   0 runner    (1001) docker     (123)      171 2023-01-29 23:43:56.000000 sagemath-environment-9.8rc0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      260 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/pyproject.toml.m4
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/requirements.txt.m4
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:19.997610 sagemath-environment-9.8rc0/sage/
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/all__sagemath_environment.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20998 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/env.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:20.001610 sagemath-environment-9.8rc0/sage/features/
+-rw-r--r--   0 runner    (1001) docker     (123)    30477 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      816 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/all.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1984 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/bliss.py
+-rw-r--r--   0 runner    (1001) docker     (123)      795 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/cddlib.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2239 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/csdp.py
+-rw-r--r--   0 runner    (1001) docker     (123)      815 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/cython.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6459 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/databases.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1303 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/dvipng.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4715 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/ffmpeg.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1639 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/four_ti_2.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1710 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/gap.py
+-rw-r--r--   0 runner    (1001) docker     (123)      651 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/gfan.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5445 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/graph_generators.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3418 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/graphviz.py
+-rw-r--r--   0 runner    (1001) docker     (123)      916 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/igraph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4958 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/imagemagick.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7157 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1507 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/internet.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4040 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/join_feature.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1904 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/kenzo.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7834 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/latex.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1914 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/latte.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5231 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/lrs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      882 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/mcqd.py
+-rw-r--r--   0 runner    (1001) docker     (123)      927 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/meataxe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3316 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/mip_backends.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1787 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/msolve.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1705 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/nauty.py
+-rw-r--r--   0 runner    (1001) docker     (123)      862 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/normaliz.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2122 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/palp.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/pandoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1367 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/pdf2svg.py
+-rw-r--r--   0 runner    (1001) docker     (123)      759 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/phitigra.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6464 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/pkg_systems.py
+-rw-r--r--   0 runner    (1001) docker     (123)      875 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/polymake.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2193 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/poppler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5041 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/rubiks.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8779 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/sagemath.py
+-rw-r--r--   0 runner    (1001) docker     (123)      709 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/singular.py
+-rw-r--r--   0 runner    (1001) docker     (123)      785 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/sphinx.py
+-rw-r--r--   0 runner    (1001) docker     (123)      744 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/features/tdlib.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:20.001610 sagemath-environment-9.8rc0/sage/misc/
+-rw-r--r--   0 runner    (1001) docker     (123)       50 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/misc/all__sagemath_environment.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25028 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/misc/package.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8090 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/misc/package_dir.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19226 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/misc/temporary_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12080 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/misc/viewer.py
+-rw-r--r--   0 runner    (1001) docker     (123)      226 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/sage/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-29 23:47:20.001610 sagemath-environment-9.8rc0/sagemath_environment.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2758 2023-01-29 23:47:18.000000 sagemath-environment-9.8rc0/sagemath_environment.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2241 2023-01-29 23:47:19.000000 sagemath-environment-9.8rc0/sagemath_environment.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-29 23:47:18.000000 sagemath-environment-9.8rc0/sagemath_environment.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      187 2023-01-29 23:47:18.000000 sagemath-environment-9.8rc0/sagemath_environment.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-29 23:47:18.000000 sagemath-environment-9.8rc0/sagemath_environment.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1601 2023-01-29 23:47:20.001610 sagemath-environment-9.8rc0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2706 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/setup.cfg.m4
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/setup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1828 2023-01-29 23:43:48.000000 sagemath-environment-9.8rc0/tox.ini
```

### Comparing `sagemath-environment-9.8b7/PKG-INFO` & `sagemath-environment-9.8rc0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sagemath-environment
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: System and software environment
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sagemath-environment-9.8b7/README.rst` & `sagemath-environment-9.8rc0/README.rst`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/math-readline` & `sagemath-environment-9.8rc0/bin/math-readline`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage` & `sagemath-environment-9.8rc0/bin/sage`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-cachegrind` & `sagemath-environment-9.8rc0/bin/sage-cachegrind`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-cleaner` & `sagemath-environment-9.8rc0/bin/sage-cleaner`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-coverage` & `sagemath-environment-9.8rc0/bin/sage-coverage`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-cython` & `sagemath-environment-9.8rc0/bin/sage-cython`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-env` & `sagemath-environment-9.8rc0/bin/sage-env`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-env-config.in` & `sagemath-environment-9.8rc0/bin/sage-env-config.in`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-fixdoctests` & `sagemath-environment-9.8rc0/bin/sage-fixdoctests`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-ipynb2rst` & `sagemath-environment-9.8rc0/bin/sage-ipynb2rst`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-list-packages` & `sagemath-environment-9.8rc0/bin/sage-list-packages`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-massif` & `sagemath-environment-9.8rc0/bin/sage-massif`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-notebook` & `sagemath-environment-9.8rc0/bin/sage-notebook`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-num-threads.py` & `sagemath-environment-9.8rc0/bin/sage-num-threads.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-omega` & `sagemath-environment-9.8rc0/bin/sage-omega`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-preparse` & `sagemath-environment-9.8rc0/bin/sage-preparse`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-rebase.bat` & `sagemath-environment-9.8rc0/bin/sage-rebase.bat`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-rebase.sh` & `sagemath-environment-9.8rc0/bin/sage-rebase.sh`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-rebaseall.bat` & `sagemath-environment-9.8rc0/bin/sage-rebaseall.bat`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-rebaseall.sh` & `sagemath-environment-9.8rc0/bin/sage-rebaseall.sh`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-run` & `sagemath-environment-9.8rc0/bin/sage-run`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-runtests` & `sagemath-environment-9.8rc0/bin/sage-runtests`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-src-env-config.in` & `sagemath-environment-9.8rc0/bin/sage-src-env-config.in`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-startuptime.py` & `sagemath-environment-9.8rc0/bin/sage-startuptime.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-update-version` & `sagemath-environment-9.8rc0/bin/sage-update-version`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-valgrind` & `sagemath-environment-9.8rc0/bin/sage-valgrind`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/bin/sage-venv-config` & `sagemath-environment-9.8rc0/bin/sage-venv-config`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/env.py` & `sagemath-environment-9.8rc0/sage/env.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/__init__.py` & `sagemath-environment-9.8rc0/sage/features/__init__.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/all.py` & `sagemath-environment-9.8rc0/sage/features/all.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/bliss.py` & `sagemath-environment-9.8rc0/sage/features/bliss.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/cddlib.py` & `sagemath-environment-9.8rc0/sage/features/cddlib.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/csdp.py` & `sagemath-environment-9.8rc0/sage/features/csdp.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/cython.py` & `sagemath-environment-9.8rc0/sage/features/cython.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/databases.py` & `sagemath-environment-9.8rc0/sage/features/databases.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/dvipng.py` & `sagemath-environment-9.8rc0/sage/features/dvipng.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/ffmpeg.py` & `sagemath-environment-9.8rc0/sage/features/ffmpeg.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/four_ti_2.py` & `sagemath-environment-9.8rc0/sage/features/four_ti_2.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/gap.py` & `sagemath-environment-9.8rc0/sage/features/gap.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/gfan.py` & `sagemath-environment-9.8rc0/sage/features/gfan.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/graph_generators.py` & `sagemath-environment-9.8rc0/sage/features/graph_generators.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/graphviz.py` & `sagemath-environment-9.8rc0/sage/features/graphviz.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/igraph.py` & `sagemath-environment-9.8rc0/sage/features/igraph.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/imagemagick.py` & `sagemath-environment-9.8rc0/sage/features/imagemagick.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/interfaces.py` & `sagemath-environment-9.8rc0/sage/features/interfaces.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/internet.py` & `sagemath-environment-9.8rc0/sage/features/internet.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/join_feature.py` & `sagemath-environment-9.8rc0/sage/features/join_feature.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/kenzo.py` & `sagemath-environment-9.8rc0/sage/features/kenzo.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/latex.py` & `sagemath-environment-9.8rc0/sage/features/latex.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/latte.py` & `sagemath-environment-9.8rc0/sage/features/latte.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/lrs.py` & `sagemath-environment-9.8rc0/sage/features/lrs.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/mcqd.py` & `sagemath-environment-9.8rc0/sage/features/mcqd.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/meataxe.py` & `sagemath-environment-9.8rc0/sage/features/meataxe.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/mip_backends.py` & `sagemath-environment-9.8rc0/sage/features/mip_backends.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/msolve.py` & `sagemath-environment-9.8rc0/sage/features/msolve.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/nauty.py` & `sagemath-environment-9.8rc0/sage/features/nauty.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/normaliz.py` & `sagemath-environment-9.8rc0/sage/features/normaliz.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/palp.py` & `sagemath-environment-9.8rc0/sage/features/palp.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/pandoc.py` & `sagemath-environment-9.8rc0/sage/features/pandoc.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/pdf2svg.py` & `sagemath-environment-9.8rc0/sage/features/pdf2svg.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/phitigra.py` & `sagemath-environment-9.8rc0/sage/features/phitigra.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/pkg_systems.py` & `sagemath-environment-9.8rc0/sage/features/pkg_systems.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/polymake.py` & `sagemath-environment-9.8rc0/sage/features/polymake.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/poppler.py` & `sagemath-environment-9.8rc0/sage/features/poppler.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/rubiks.py` & `sagemath-environment-9.8rc0/sage/features/rubiks.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/sagemath.py` & `sagemath-environment-9.8rc0/sage/features/sagemath.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/singular.py` & `sagemath-environment-9.8rc0/sage/features/singular.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/sphinx.py` & `sagemath-environment-9.8rc0/sage/features/sphinx.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/features/tdlib.py` & `sagemath-environment-9.8rc0/sage/features/tdlib.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/misc/package.py` & `sagemath-environment-9.8rc0/sage/misc/package.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/misc/package_dir.py` & `sagemath-environment-9.8rc0/sage/misc/package_dir.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/misc/temporary_file.py` & `sagemath-environment-9.8rc0/sage/misc/temporary_file.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sage/misc/viewer.py` & `sagemath-environment-9.8rc0/sage/misc/viewer.py`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/sagemath_environment.egg-info/PKG-INFO` & `sagemath-environment-9.8rc0/sagemath_environment.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sagemath-environment
-Version: 9.8b7
+Version: 9.8rc0
 Summary: Sage: Open Source Mathematics Software: System and software environment
 Home-page: https://www.sagemath.org
 Author: The Sage Developers
 Author-email: sage-support@googlegroups.com
 License: GNU General Public License (GPL) v2 or later
 Classifier: Development Status :: 6 - Mature
 Classifier: Intended Audience :: Education
```

### Comparing `sagemath-environment-9.8b7/sagemath_environment.egg-info/SOURCES.txt` & `sagemath-environment-9.8rc0/sagemath_environment.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/setup.cfg` & `sagemath-environment-9.8rc0/setup.cfg`

 * *Files 4% similar despite different names*

```diff
@@ -41,19 +41,19 @@
 	bin/sage-env
 	bin/sage-num-threads.py
 	bin/sage-venv-config
 	bin/sage-version.sh
 	bin/sage-python
 
 [options.extras_require]
-conf = sage-conf ~= 9.8b7
-docbuild = sage-docbuild ~= 9.8b7
-sage = sagelib ~= 9.8b7
+conf = sage-conf ~= 9.8rc0
+docbuild = sage-docbuild ~= 9.8rc0
+sage = sagelib ~= 9.8rc0
 cython = cython >=0.29.21, <1.0
 pytest = 
 rst2ipynb = rst2ipynb >=0.2.2
-sws2rst = sage-sws2rst ~= 9.8b7
+sws2rst = sage-sws2rst ~= 9.8rc0
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `sagemath-environment-9.8b7/setup.cfg.m4` & `sagemath-environment-9.8rc0/setup.cfg.m4`

 * *Files identical despite different names*

### Comparing `sagemath-environment-9.8b7/tox.ini` & `sagemath-environment-9.8rc0/tox.ini`

 * *Files 8% similar despite different names*

```diff
@@ -29,15 +29,15 @@
     # Sage scripts such as sage-runtests like to use $HOME/.sage
                              HOME={envdir}
     # We supply pip options by environment variables so that they
     # apply both to the installation of the dependencies and of the package
     sagewheels:              PIP_FIND_LINKS=file://{env:SAGE_SPKG_WHEELS:{env:SAGE_VENV:{toxinidir}/../../../../venv}/var/lib/sage/wheels}
     nopypi:                  PIP_NO_INDEX=true
 
-whitelist_externals =
+allowlist_externals =
     bash
 
 commands =
     # Beware of the treacherous non-src layout. "./sage/" shadows the installed sage package.
     {envpython} -c 'import sys; "" in sys.path and sys.path.remove(""); from sage.features.all import all_features; print(sorted(all_features(), key=lambda x: x.name)); import sage.misc.package'
 
 [testenv:sagepython]
```

