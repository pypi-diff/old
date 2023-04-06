# Comparing `tmp/lmdb-1.4.0.tar.gz` & `tmp/lmdb-1.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lmdb-1.4.0.tar", last modified: Wed Dec  7 03:28:59 2022, max compression
+gzip compressed data, was "lmdb-1.4.1.tar", last modified: Thu Apr  6 06:42:21 2023, max compression
```

## Comparing `lmdb-1.4.0.tar` & `lmdb-1.4.1.tar`

### file list

```diff
@@ -1,72 +1,72 @@
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.319876 lmdb-1.4.0/
--rw-r--r--   0 runner    (1001) docker     (116)    16077 2022-12-07 03:28:47.000000 lmdb-1.4.0/ChangeLog
--rw-r--r--   0 runner    (1001) docker     (116)     2214 2022-12-07 03:28:47.000000 lmdb-1.4.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (116)      134 2022-12-07 03:28:47.000000 lmdb-1.4.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (116)     1165 2022-12-07 03:28:59.319876 lmdb-1.4.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)      730 2022-12-07 03:28:47.000000 lmdb-1.4.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.311876 lmdb-1.4.0/docs/
--rw-r--r--   0 runner    (1001) docker     (116)     5556 2022-12-07 03:28:47.000000 lmdb-1.4.0/docs/Makefile
--rw-r--r--   0 runner    (1001) docker     (116)     8734 2022-12-07 03:28:47.000000 lmdb-1.4.0/docs/conf.py
--rw-r--r--   0 runner    (1001) docker     (116)    26345 2022-12-07 03:28:47.000000 lmdb-1.4.0/docs/index.rst
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.311876 lmdb-1.4.0/docs/themes/
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.315876 lmdb-1.4.0/docs/themes/acid/
--rw-r--r--   0 runner    (1001) docker     (116)      682 2022-12-07 03:28:47.000000 lmdb-1.4.0/docs/themes/acid/conf.py.conf
--rw-r--r--   0 runner    (1001) docker     (116)     3852 2022-12-07 03:28:47.000000 lmdb-1.4.0/docs/themes/acid/layout.html
--rw-r--r--   0 runner    (1001) docker     (116)       22 2022-12-07 03:28:47.000000 lmdb-1.4.0/docs/themes/acid/sourcelink.html
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.315876 lmdb-1.4.0/docs/themes/acid/static/
--rw-r--r--   0 runner    (1001) docker     (116)    25703 2022-12-07 03:28:47.000000 lmdb-1.4.0/docs/themes/acid/static/acid.css
--rw-r--r--   0 runner    (1001) docker     (116)      735 2022-12-07 03:28:47.000000 lmdb-1.4.0/docs/themes/acid/theme.conf
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.315876 lmdb-1.4.0/examples/
--rw-r--r--   0 runner    (1001) docker     (116)     2165 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/address-book.py
--rw-r--r--   0 runner    (1001) docker     (116)     3739 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/dirtybench-gdbm.py
--rw-r--r--   0 runner    (1001) docker     (116)     7117 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/dirtybench.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.315876 lmdb-1.4.0/examples/keystore/
--rw-r--r--   0 runner    (1001) docker     (116)     1507 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/keystore/README.md
--rw-r--r--   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/keystore/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     3147 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/keystore/interfaces.py
--rw-r--r--   0 runner    (1001) docker     (116)     4035 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/keystore/lmdb.py
--rw-r--r--   0 runner    (1001) docker     (116)      622 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/keystore/main.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.315876 lmdb-1.4.0/examples/keystore/static/
--rw-r--r--   0 runner    (1001) docker     (116)     1885 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/keystore/static/index.html
--rw-r--r--   0 runner    (1001) docker     (116)     2424 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/keystore/web.py
--rw-r--r--   0 runner    (1001) docker     (116)     1798 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/keystore/webapi.py
--rw-r--r--   0 runner    (1001) docker     (116)     2180 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/nastybench.py
--rw-r--r--   0 runner    (1001) docker     (116)     2436 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/parabench.py
--rw-r--r--   0 runner    (1001) docker     (116)   663661 2022-12-07 03:28:47.000000 lmdb-1.4.0/examples/words.gz
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.315876 lmdb-1.4.0/lib/
--rw-r--r--   0 runner    (1001) docker     (116)    74014 2022-12-07 03:28:47.000000 lmdb-1.4.0/lib/lmdb.h
--rw-r--r--   0 runner    (1001) docker     (116)   291569 2022-12-07 03:28:47.000000 lmdb-1.4.0/lib/mdb.c
--rw-r--r--   0 runner    (1001) docker     (116)     6588 2022-12-07 03:28:47.000000 lmdb-1.4.0/lib/midl.c
--rw-r--r--   0 runner    (1001) docker     (116)     5711 2022-12-07 03:28:47.000000 lmdb-1.4.0/lib/midl.h
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.315876 lmdb-1.4.0/lib/py-lmdb/
--rw-r--r--   0 runner    (1001) docker     (116)     3851 2022-12-07 03:28:47.000000 lmdb-1.4.0/lib/py-lmdb/env-copy-txn.patch
--rw-r--r--   0 runner    (1001) docker     (116)     1689 2022-12-07 03:28:47.000000 lmdb-1.4.0/lib/py-lmdb/preload.h
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.319876 lmdb-1.4.0/lib/win32/
--rw-r--r--   0 runner    (1001) docker     (116)     8051 2022-12-07 03:28:47.000000 lmdb-1.4.0/lib/win32/inttypes.h
--rw-r--r--   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:47.000000 lmdb-1.4.0/lib/win32/unistd.h
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.319876 lmdb-1.4.0/lib/win32-stdint/
--rw-r--r--   0 runner    (1001) docker     (116)     8092 2022-12-07 03:28:47.000000 lmdb-1.4.0/lib/win32-stdint/stdint.h
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.319876 lmdb-1.4.0/lmdb/
--rw-r--r--   0 runner    (1001) docker     (116)     1710 2022-12-07 03:28:47.000000 lmdb-1.4.0/lmdb/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)      861 2022-12-07 03:28:47.000000 lmdb-1.4.0/lmdb/__main__.py
--rw-r--r--   0 runner    (1001) docker     (116)      247 2022-12-07 03:28:54.000000 lmdb-1.4.0/lmdb/_config.py
--rw-r--r--   0 runner    (1001) docker     (116)    92210 2022-12-07 03:28:47.000000 lmdb-1.4.0/lmdb/cffi.py
--rw-r--r--   0 runner    (1001) docker     (116)   105566 2022-12-07 03:28:47.000000 lmdb-1.4.0/lmdb/cpython.c
--rwxr-xr-x   0 runner    (1001) docker     (116)    19675 2022-12-07 03:28:47.000000 lmdb-1.4.0/lmdb/tool.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.319876 lmdb-1.4.0/lmdb.egg-info/
--rw-r--r--   0 runner    (1001) docker     (116)     1165 2022-12-07 03:28:54.000000 lmdb-1.4.0/lmdb.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)     1160 2022-12-07 03:28:54.000000 lmdb-1.4.0/lmdb.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (116)        1 2022-12-07 03:28:54.000000 lmdb-1.4.0/lmdb.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (116)       13 2022-12-07 03:28:54.000000 lmdb-1.4.0/lmdb.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (116)       38 2022-12-07 03:28:59.319876 lmdb-1.4.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (116)     7614 2022-12-07 03:28:47.000000 lmdb-1.4.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2022-12-07 03:28:59.319876 lmdb-1.4.0/tests/
--rw-r--r--   0 runner    (1001) docker     (116)    10752 2022-12-07 03:28:47.000000 lmdb-1.4.0/tests/crash_test.py
--rw-r--r--   0 runner    (1001) docker     (116)    11215 2022-12-07 03:28:47.000000 lmdb-1.4.0/tests/cursor_test.py
--rw-r--r--   0 runner    (1001) docker     (116)    28112 2022-12-07 03:28:47.000000 lmdb-1.4.0/tests/env_test.py
--rw-r--r--   0 runner    (1001) docker     (116)     2829 2022-12-07 03:28:47.000000 lmdb-1.4.0/tests/getmulti_test.py
--rw-r--r--   0 runner    (1001) docker     (116)     8831 2022-12-07 03:28:47.000000 lmdb-1.4.0/tests/iteration_test.py
--rw-r--r--   0 runner    (1001) docker     (116)     2058 2022-12-07 03:28:47.000000 lmdb-1.4.0/tests/package_test.py
--rw-r--r--   0 runner    (1001) docker     (116)     4205 2022-12-07 03:28:47.000000 lmdb-1.4.0/tests/testlib.py
--rw-r--r--   0 runner    (1001) docker     (116)     1624 2022-12-07 03:28:47.000000 lmdb-1.4.0/tests/tool_test.py
--rw-r--r--   0 runner    (1001) docker     (116)    16854 2022-12-07 03:28:47.000000 lmdb-1.4.0/tests/txn_test.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.875925 lmdb-1.4.1/
+-rw-r--r--   0 runner    (1001) docker     (122)    16137 2023-04-06 06:42:11.000000 lmdb-1.4.1/ChangeLog
+-rw-r--r--   0 runner    (1001) docker     (122)     2214 2023-04-06 06:42:11.000000 lmdb-1.4.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)      134 2023-04-06 06:42:11.000000 lmdb-1.4.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)     1165 2023-04-06 06:42:21.875925 lmdb-1.4.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      730 2023-04-06 06:42:11.000000 lmdb-1.4.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.863926 lmdb-1.4.1/docs/
+-rw-r--r--   0 runner    (1001) docker     (122)     5556 2023-04-06 06:42:11.000000 lmdb-1.4.1/docs/Makefile
+-rw-r--r--   0 runner    (1001) docker     (122)     8734 2023-04-06 06:42:11.000000 lmdb-1.4.1/docs/conf.py
+-rw-r--r--   0 runner    (1001) docker     (122)    26345 2023-04-06 06:42:11.000000 lmdb-1.4.1/docs/index.rst
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.859926 lmdb-1.4.1/docs/themes/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.863926 lmdb-1.4.1/docs/themes/acid/
+-rw-r--r--   0 runner    (1001) docker     (122)      682 2023-04-06 06:42:11.000000 lmdb-1.4.1/docs/themes/acid/conf.py.conf
+-rw-r--r--   0 runner    (1001) docker     (122)     3852 2023-04-06 06:42:11.000000 lmdb-1.4.1/docs/themes/acid/layout.html
+-rw-r--r--   0 runner    (1001) docker     (122)       22 2023-04-06 06:42:11.000000 lmdb-1.4.1/docs/themes/acid/sourcelink.html
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.863926 lmdb-1.4.1/docs/themes/acid/static/
+-rw-r--r--   0 runner    (1001) docker     (122)    25703 2023-04-06 06:42:11.000000 lmdb-1.4.1/docs/themes/acid/static/acid.css
+-rw-r--r--   0 runner    (1001) docker     (122)      735 2023-04-06 06:42:11.000000 lmdb-1.4.1/docs/themes/acid/theme.conf
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.867926 lmdb-1.4.1/examples/
+-rw-r--r--   0 runner    (1001) docker     (122)     2165 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/address-book.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3739 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/dirtybench-gdbm.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7117 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/dirtybench.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.867926 lmdb-1.4.1/examples/keystore/
+-rw-r--r--   0 runner    (1001) docker     (122)     1507 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/keystore/README.md
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/keystore/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3147 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/keystore/interfaces.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4035 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/keystore/lmdb.py
+-rw-r--r--   0 runner    (1001) docker     (122)      622 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/keystore/main.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.867926 lmdb-1.4.1/examples/keystore/static/
+-rw-r--r--   0 runner    (1001) docker     (122)     1885 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/keystore/static/index.html
+-rw-r--r--   0 runner    (1001) docker     (122)     2424 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/keystore/web.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1798 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/keystore/webapi.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2180 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/nastybench.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2436 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/parabench.py
+-rw-r--r--   0 runner    (1001) docker     (122)   663661 2023-04-06 06:42:11.000000 lmdb-1.4.1/examples/words.gz
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.871925 lmdb-1.4.1/lib/
+-rw-r--r--   0 runner    (1001) docker     (122)    74014 2023-04-06 06:42:11.000000 lmdb-1.4.1/lib/lmdb.h
+-rw-r--r--   0 runner    (1001) docker     (122)   291569 2023-04-06 06:42:11.000000 lmdb-1.4.1/lib/mdb.c
+-rw-r--r--   0 runner    (1001) docker     (122)     6588 2023-04-06 06:42:11.000000 lmdb-1.4.1/lib/midl.c
+-rw-r--r--   0 runner    (1001) docker     (122)     5711 2023-04-06 06:42:11.000000 lmdb-1.4.1/lib/midl.h
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.871925 lmdb-1.4.1/lib/py-lmdb/
+-rw-r--r--   0 runner    (1001) docker     (122)     3851 2023-04-06 06:42:11.000000 lmdb-1.4.1/lib/py-lmdb/env-copy-txn.patch
+-rw-r--r--   0 runner    (1001) docker     (122)     1689 2023-04-06 06:42:11.000000 lmdb-1.4.1/lib/py-lmdb/preload.h
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.871925 lmdb-1.4.1/lib/win32/
+-rw-r--r--   0 runner    (1001) docker     (122)     8051 2023-04-06 06:42:11.000000 lmdb-1.4.1/lib/win32/inttypes.h
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:11.000000 lmdb-1.4.1/lib/win32/unistd.h
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.871925 lmdb-1.4.1/lib/win32-stdint/
+-rw-r--r--   0 runner    (1001) docker     (122)     8092 2023-04-06 06:42:11.000000 lmdb-1.4.1/lib/win32-stdint/stdint.h
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.871925 lmdb-1.4.1/lmdb/
+-rw-r--r--   0 runner    (1001) docker     (122)     1710 2023-04-06 06:42:11.000000 lmdb-1.4.1/lmdb/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      861 2023-04-06 06:42:11.000000 lmdb-1.4.1/lmdb/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      247 2023-04-06 06:42:17.000000 lmdb-1.4.1/lmdb/_config.py
+-rw-r--r--   0 runner    (1001) docker     (122)    92210 2023-04-06 06:42:11.000000 lmdb-1.4.1/lmdb/cffi.py
+-rw-r--r--   0 runner    (1001) docker     (122)   105566 2023-04-06 06:42:11.000000 lmdb-1.4.1/lmdb/cpython.c
+-rwxr-xr-x   0 runner    (1001) docker     (122)    19675 2023-04-06 06:42:11.000000 lmdb-1.4.1/lmdb/tool.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.875925 lmdb-1.4.1/lmdb.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     1165 2023-04-06 06:42:17.000000 lmdb-1.4.1/lmdb.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     1160 2023-04-06 06:42:17.000000 lmdb-1.4.1/lmdb.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 06:42:17.000000 lmdb-1.4.1/lmdb.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       13 2023-04-06 06:42:17.000000 lmdb-1.4.1/lmdb.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-06 06:42:21.875925 lmdb-1.4.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     7614 2023-04-06 06:42:11.000000 lmdb-1.4.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 06:42:21.875925 lmdb-1.4.1/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)    10752 2023-04-06 06:42:11.000000 lmdb-1.4.1/tests/crash_test.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11215 2023-04-06 06:42:11.000000 lmdb-1.4.1/tests/cursor_test.py
+-rw-r--r--   0 runner    (1001) docker     (122)    28112 2023-04-06 06:42:11.000000 lmdb-1.4.1/tests/env_test.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2829 2023-04-06 06:42:11.000000 lmdb-1.4.1/tests/getmulti_test.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8831 2023-04-06 06:42:11.000000 lmdb-1.4.1/tests/iteration_test.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2058 2023-04-06 06:42:11.000000 lmdb-1.4.1/tests/package_test.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4205 2023-04-06 06:42:11.000000 lmdb-1.4.1/tests/testlib.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1624 2023-04-06 06:42:11.000000 lmdb-1.4.1/tests/tool_test.py
+-rw-r--r--   0 runner    (1001) docker     (122)    16854 2023-04-06 06:42:11.000000 lmdb-1.4.1/tests/txn_test.py
```

### Comparing `lmdb-1.4.0/ChangeLog` & `lmdb-1.4.1/ChangeLog`

 * *Files 2% similar despite different names*

```diff
@@ -1,7 +1,10 @@
+2022-04-04 v1.4.1
+* Update CI to build manylinux binaries.
+
 2022-12-06 v1.4.0
 * Add Python 3.11 support.
 
 2021-12-30 v1.3.0
 * Add aarch64 architecture builds.  Contributed by odidev.
 
 * Add Python 3.10 support.
```

### Comparing `lmdb-1.4.0/LICENSE` & `lmdb-1.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/PKG-INFO` & `lmdb-1.4.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lmdb
-Version: 1.4.0
+Version: 1.4.1
 Summary: Universal Python binding for the LMDB 'Lightning' Database
 Home-page: http://github.com/jnwatson/py-lmdb/
 Author: David Wilson
 Maintainer: Nic Watson
 License: OLDAP-2.8
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: Implementation :: CPython
```

### Comparing `lmdb-1.4.0/README.md` & `lmdb-1.4.1/README.md`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/docs/Makefile` & `lmdb-1.4.1/docs/Makefile`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/docs/conf.py` & `lmdb-1.4.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/docs/index.rst` & `lmdb-1.4.1/docs/index.rst`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/docs/themes/acid/conf.py.conf` & `lmdb-1.4.1/docs/themes/acid/conf.py.conf`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/docs/themes/acid/layout.html` & `lmdb-1.4.1/docs/themes/acid/layout.html`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/docs/themes/acid/static/acid.css` & `lmdb-1.4.1/docs/themes/acid/static/acid.css`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/docs/themes/acid/theme.conf` & `lmdb-1.4.1/docs/themes/acid/theme.conf`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/address-book.py` & `lmdb-1.4.1/examples/address-book.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/dirtybench-gdbm.py` & `lmdb-1.4.1/examples/dirtybench-gdbm.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/dirtybench.py` & `lmdb-1.4.1/examples/dirtybench.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/keystore/README.md` & `lmdb-1.4.1/examples/keystore/README.md`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/keystore/interfaces.py` & `lmdb-1.4.1/examples/keystore/interfaces.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/keystore/lmdb.py` & `lmdb-1.4.1/examples/keystore/lmdb.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/keystore/main.py` & `lmdb-1.4.1/examples/keystore/main.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/keystore/static/index.html` & `lmdb-1.4.1/examples/keystore/static/index.html`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/keystore/web.py` & `lmdb-1.4.1/examples/keystore/web.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/keystore/webapi.py` & `lmdb-1.4.1/examples/keystore/webapi.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/nastybench.py` & `lmdb-1.4.1/examples/nastybench.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/parabench.py` & `lmdb-1.4.1/examples/parabench.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/examples/words.gz` & `lmdb-1.4.1/examples/words.gz`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lib/lmdb.h` & `lmdb-1.4.1/lib/lmdb.h`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lib/mdb.c` & `lmdb-1.4.1/lib/mdb.c`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lib/midl.c` & `lmdb-1.4.1/lib/midl.c`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lib/midl.h` & `lmdb-1.4.1/lib/midl.h`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lib/py-lmdb/env-copy-txn.patch` & `lmdb-1.4.1/lib/py-lmdb/env-copy-txn.patch`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lib/py-lmdb/preload.h` & `lmdb-1.4.1/lib/py-lmdb/preload.h`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lib/win32/inttypes.h` & `lmdb-1.4.1/lib/win32/inttypes.h`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lib/win32-stdint/stdint.h` & `lmdb-1.4.1/lib/win32-stdint/stdint.h`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lmdb/__init__.py` & `lmdb-1.4.1/lmdb/__init__.py`

 * *Files 6% similar despite different names*

```diff
@@ -46,8 +46,8 @@
     if (not _reading_docs()) and os.getenv('LMDB_FORCE_CPYTHON') is not None:
         raise
     from lmdb.cffi import *
     from lmdb.cffi import open
     from lmdb.cffi import __all__
     from lmdb.cffi import __doc__
 
-__version__ = '1.4.0'
+__version__ = '1.4.1'
```

### Comparing `lmdb-1.4.0/lmdb/__main__.py` & `lmdb-1.4.1/lmdb/__main__.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lmdb/cffi.py` & `lmdb-1.4.1/lmdb/cffi.py`

 * *Files 0% similar despite different names*

```diff
@@ -1178,15 +1178,15 @@
                 If ``True``, indicates keys in the database are C unsigned
                 or ``size_t`` integers encoded in native byte order. Keys must
                 all be either unsigned or ``size_t``, they cannot be mixed in a
                 single database.
 
             `integerdup`:
                 If ``True``, values in the
-                database are C unsigned or ``size_t`` integers encode din
+                database are C unsigned or ``size_t`` integers encoded in
                 native byte order.  Implies `dupsort` and `dupfixed` are
                 ``True``.
 
             `dupfixed`:
                 If ``True``, values for each key
                 in database are of fixed size, allowing each additional
                 duplicate value for a key to be stored without a header
```

### Comparing `lmdb-1.4.0/lmdb/cpython.c` & `lmdb-1.4.1/lmdb/cpython.c`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lmdb/tool.py` & `lmdb-1.4.1/lmdb/tool.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/lmdb.egg-info/PKG-INFO` & `lmdb-1.4.1/lmdb.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lmdb
-Version: 1.4.0
+Version: 1.4.1
 Summary: Universal Python binding for the LMDB 'Lightning' Database
 Home-page: http://github.com/jnwatson/py-lmdb/
 Author: David Wilson
 Maintainer: Nic Watson
 License: OLDAP-2.8
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: Implementation :: CPython
```

### Comparing `lmdb-1.4.0/lmdb.egg-info/SOURCES.txt` & `lmdb-1.4.1/lmdb.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/setup.py` & `lmdb-1.4.1/setup.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/tests/crash_test.py` & `lmdb-1.4.1/tests/crash_test.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/tests/cursor_test.py` & `lmdb-1.4.1/tests/cursor_test.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/tests/env_test.py` & `lmdb-1.4.1/tests/env_test.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/tests/getmulti_test.py` & `lmdb-1.4.1/tests/getmulti_test.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/tests/iteration_test.py` & `lmdb-1.4.1/tests/iteration_test.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/tests/package_test.py` & `lmdb-1.4.1/tests/package_test.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/tests/testlib.py` & `lmdb-1.4.1/tests/testlib.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/tests/tool_test.py` & `lmdb-1.4.1/tests/tool_test.py`

 * *Files identical despite different names*

### Comparing `lmdb-1.4.0/tests/txn_test.py` & `lmdb-1.4.1/tests/txn_test.py`

 * *Files identical despite different names*

