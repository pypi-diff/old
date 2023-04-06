# Comparing `tmp/energyplus_regressions-2.0.0.tar.gz` & `tmp/energyplus_regressions-2.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "energyplus_regressions-2.0.0.tar", last modified: Thu Mar 30 15:36:27 2023, max compression
+gzip compressed data, was "energyplus_regressions-2.0.2.tar", last modified: Thu Apr  6 18:31:03 2023, max compression
```

## Comparing `energyplus_regressions-2.0.0.tar` & `energyplus_regressions-2.0.2.tar`

### file list

```diff
@@ -1,65 +1,69 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.811925 energyplus_regressions-2.0.0/
--rw-r--r--   0 runner    (1001) docker     (122)     1735 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)       97 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (122)     3751 2023-03-30 15:36:27.811925 energyplus_regressions-2.0.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     2985 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.799925 energyplus_regressions-2.0.0/energyplus_regressions/
--rw-r--r--   0 runner    (1001) docker     (122)       18 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)       64 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/__main__.py
--rwxr-xr-x   0 runner    (1001) docker     (122)    11982 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/build_files_to_run.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.803925 energyplus_regressions-2.0.0/energyplus_regressions/builds/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/builds/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     5426 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/builds/base.py
--rw-r--r--   0 runner    (1001) docker     (122)     2835 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/builds/install.py
--rw-r--r--   0 runner    (1001) docker     (122)     3292 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/builds/makefile.py
--rw-r--r--   0 runner    (1001) docker     (122)     3649 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/builds/visualstudio.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.803925 energyplus_regressions-2.0.0/energyplus_regressions/diffs/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/diffs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    13954 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/diffs/ci_compare_script.py
--rwxr-xr-x   0 runner    (1001) docker     (122)     1528 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/diffs/math_diff.config
--rwxr-xr-x   0 runner    (1001) docker     (122)    25132 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/diffs/math_diff.py
--rwxr-xr-x   0 runner    (1001) docker     (122)     4120 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/diffs/mycsv.py
--rwxr-xr-x   0 runner    (1001) docker     (122)    21208 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/diffs/table_diff.py
--rwxr-xr-x   0 runner    (1001) docker     (122)     4270 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/diffs/thresh_dict.py
--rwxr-xr-x   0 runner    (1001) docker     (122)     9426 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/energyplus.py
--rw-r--r--   0 runner    (1001) docker     (122)    10741 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/ep.png
--rw-r--r--   0 runner    (1001) docker     (122)      860 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/ep_platform.py
--rw-r--r--   0 runner    (1001) docker     (122)    64569 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/epw_map.py
--rwxr-xr-x   0 runner    (1001) docker     (122)      766 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/runner.py
--rwxr-xr-x   0 runner    (1001) docker     (122)    64399 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/runtests.py
--rwxr-xr-x   0 runner    (1001) docker     (122)    20990 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/structures.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.807925 energyplus_regressions-2.0.0/energyplus_regressions/tests/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.807925 energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)     3177 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/test_base.py
--rw-r--r--   0 runner    (1001) docker     (122)     1695 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/test_install.py
--rw-r--r--   0 runner    (1001) docker     (122)     2593 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/test_makefile.py
--rw-r--r--   0 runner    (1001) docker     (122)     2968 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/test_visualstudio.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.807925 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/
--rw-r--r--   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.807925 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/csv_resources/
--rwxr-xr-x   0 runner    (1001) docker     (122)     1530 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/csv_resources/test_math_diff.config
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.807925 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/tbl_resources/
--rwxr-xr-x   0 runner    (1001) docker     (122)     1530 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/tbl_resources/test_table_diff.config
--rw-r--r--   0 runner    (1001) docker     (122)    18306 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_ci_compare_script.py
--rw-r--r--   0 runner    (1001) docker     (122)    17039 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_math_diff.py
--rw-r--r--   0 runner    (1001) docker     (122)     5252 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_mycsv.py
--rw-r--r--   0 runner    (1001) docker     (122)    23636 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_table_diff.py
--rw-r--r--   0 runner    (1001) docker     (122)     3154 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_thresh_dict.py
--rw-r--r--   0 runner    (1001) docker     (122)     9624 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/test_build_files_to_run.py
--rw-r--r--   0 runner    (1001) docker     (122)     8230 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/test_energyplus.py
--rw-r--r--   0 runner    (1001) docker     (122)     2106 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/test_epw_map.py
--rw-r--r--   0 runner    (1001) docker     (122)      895 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/test_platform.py
--rw-r--r--   0 runner    (1001) docker     (122)   113719 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/test_runtests.py
--rw-r--r--   0 runner    (1001) docker     (122)     9993 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tests/test_structures.py
--rw-r--r--   0 runner    (1001) docker     (122)    54426 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/energyplus_regressions/tk_window.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-03-30 15:36:27.803925 energyplus_regressions-2.0.0/energyplus_regressions.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)     3751 2023-03-30 15:36:27.000000 energyplus_regressions-2.0.0/energyplus_regressions.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)     2285 2023-03-30 15:36:27.000000 energyplus_regressions-2.0.0/energyplus_regressions.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-03-30 15:36:27.000000 energyplus_regressions-2.0.0/energyplus_regressions.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)       89 2023-03-30 15:36:27.000000 energyplus_regressions-2.0.0/energyplus_regressions.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (122)       24 2023-03-30 15:36:27.000000 energyplus_regressions-2.0.0/energyplus_regressions.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)       23 2023-03-30 15:36:27.000000 energyplus_regressions-2.0.0/energyplus_regressions.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)      182 2023-03-30 15:36:27.811925 energyplus_regressions-2.0.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)     1071 2023-03-30 15:36:14.000000 energyplus_regressions-2.0.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.138130 energyplus_regressions-2.0.2/
+-rw-r--r--   0 runner    (1001) docker     (122)     1735 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)      192 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)     3751 2023-04-06 18:31:03.138130 energyplus_regressions-2.0.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     2985 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.130130 energyplus_regressions-2.0.2/energyplus_regressions/
+-rw-r--r--   0 runner    (1001) docker     (122)       50 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)       64 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/__main__.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)    11982 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/build_files_to_run.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.130130 energyplus_regressions-2.0.2/energyplus_regressions/builds/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/builds/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5426 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/builds/base.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2835 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/builds/install.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3292 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/builds/makefile.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3649 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/builds/visualstudio.py
+-rw-r--r--   0 runner    (1001) docker     (122)      338 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/configure.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.130130 energyplus_regressions-2.0.2/energyplus_regressions/diffs/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/diffs/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    13954 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/diffs/ci_compare_script.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)     1528 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/diffs/math_diff.config
+-rwxr-xr-x   0 runner    (1001) docker     (122)    25132 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/diffs/math_diff.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)     4120 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/diffs/mycsv.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)    21208 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/diffs/table_diff.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)     4270 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/diffs/thresh_dict.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)     9426 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/energyplus.py
+-rw-r--r--   0 runner    (1001) docker     (122)      860 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/ep_platform.py
+-rw-r--r--   0 runner    (1001) docker     (122)    64569 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/epw_map.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.134130 energyplus_regressions-2.0.2/energyplus_regressions/icons/
+-rw-r--r--   0 runner    (1001) docker     (122)    18638 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/icons/icon.icns
+-rw-r--r--   0 runner    (1001) docker     (122)    15187 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/icons/icon.ico
+-rw-r--r--   0 runner    (1001) docker     (122)    25254 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/icons/icon.png
+-rwxr-xr-x   0 runner    (1001) docker     (122)      766 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/runner.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)    64399 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/runtests.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)    20990 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/structures.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.134130 energyplus_regressions-2.0.2/energyplus_regressions/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.134130 energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3177 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/test_base.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1695 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/test_install.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2593 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/test_makefile.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2968 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/test_visualstudio.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.134130 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.134130 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/csv_resources/
+-rwxr-xr-x   0 runner    (1001) docker     (122)     1530 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/csv_resources/test_math_diff.config
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.134130 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/tbl_resources/
+-rwxr-xr-x   0 runner    (1001) docker     (122)     1530 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/tbl_resources/test_table_diff.config
+-rw-r--r--   0 runner    (1001) docker     (122)    18306 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_ci_compare_script.py
+-rw-r--r--   0 runner    (1001) docker     (122)    17039 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_math_diff.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5252 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_mycsv.py
+-rw-r--r--   0 runner    (1001) docker     (122)    23636 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_table_diff.py
+-rw-r--r--   0 runner    (1001) docker     (122)     3154 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_thresh_dict.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9624 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/test_build_files_to_run.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8230 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/test_energyplus.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2106 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/test_epw_map.py
+-rw-r--r--   0 runner    (1001) docker     (122)      895 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/test_platform.py
+-rw-r--r--   0 runner    (1001) docker     (122)   113719 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/test_runtests.py
+-rw-r--r--   0 runner    (1001) docker     (122)     9993 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tests/test_structures.py
+-rw-r--r--   0 runner    (1001) docker     (122)    55441 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/energyplus_regressions/tk_window.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 18:31:03.130130 energyplus_regressions-2.0.2/energyplus_regressions.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     3751 2023-04-06 18:31:03.000000 energyplus_regressions-2.0.2/energyplus_regressions.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     2406 2023-04-06 18:31:03.000000 energyplus_regressions-2.0.2/energyplus_regressions.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 18:31:03.000000 energyplus_regressions-2.0.2/energyplus_regressions.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      185 2023-04-06 18:31:03.000000 energyplus_regressions-2.0.2/energyplus_regressions.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       40 2023-04-06 18:31:03.000000 energyplus_regressions-2.0.2/energyplus_regressions.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       23 2023-04-06 18:31:03.000000 energyplus_regressions-2.0.2/energyplus_regressions.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      182 2023-04-06 18:31:03.138130 energyplus_regressions-2.0.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1391 2023-04-06 18:30:49.000000 energyplus_regressions-2.0.2/setup.py
```

### Comparing `energyplus_regressions-2.0.0/LICENSE` & `energyplus_regressions-2.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/PKG-INFO` & `energyplus_regressions-2.0.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: energyplus_regressions
-Version: 2.0.0
+Version: 2.0.2
 Summary: A Python 3 library for evaluating regressions between EnergyPlus builds.
 Home-page: https://github.com/NREL/EnergyPlusRegressionTool
 Author: Edwin Lee
 Author-email: 
 License: UNKNOWN
 Description: # EnergyPlus Regressions
```

### Comparing `energyplus_regressions-2.0.0/README.md` & `energyplus_regressions-2.0.2/README.md`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/build_files_to_run.py` & `energyplus_regressions-2.0.2/energyplus_regressions/build_files_to_run.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/builds/base.py` & `energyplus_regressions-2.0.2/energyplus_regressions/builds/base.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/builds/install.py` & `energyplus_regressions-2.0.2/energyplus_regressions/builds/install.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/builds/makefile.py` & `energyplus_regressions-2.0.2/energyplus_regressions/builds/makefile.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/builds/visualstudio.py` & `energyplus_regressions-2.0.2/energyplus_regressions/builds/visualstudio.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/diffs/ci_compare_script.py` & `energyplus_regressions-2.0.2/energyplus_regressions/diffs/ci_compare_script.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/diffs/math_diff.config` & `energyplus_regressions-2.0.2/energyplus_regressions/diffs/math_diff.config`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/diffs/math_diff.py` & `energyplus_regressions-2.0.2/energyplus_regressions/diffs/math_diff.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/diffs/mycsv.py` & `energyplus_regressions-2.0.2/energyplus_regressions/diffs/mycsv.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/diffs/table_diff.py` & `energyplus_regressions-2.0.2/energyplus_regressions/diffs/table_diff.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/diffs/thresh_dict.py` & `energyplus_regressions-2.0.2/energyplus_regressions/diffs/thresh_dict.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/energyplus.py` & `energyplus_regressions-2.0.2/energyplus_regressions/energyplus.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/ep_platform.py` & `energyplus_regressions-2.0.2/energyplus_regressions/ep_platform.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/epw_map.py` & `energyplus_regressions-2.0.2/energyplus_regressions/epw_map.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/runner.py` & `energyplus_regressions-2.0.2/energyplus_regressions/runner.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/runtests.py` & `energyplus_regressions-2.0.2/energyplus_regressions/runtests.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/structures.py` & `energyplus_regressions-2.0.2/energyplus_regressions/structures.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/test_base.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/test_base.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/test_install.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/test_install.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/test_makefile.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/test_makefile.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/builds/test_visualstudio.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/builds/test_visualstudio.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/csv_resources/test_math_diff.config` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/csv_resources/test_math_diff.config`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/tbl_resources/test_table_diff.config` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/tbl_resources/test_table_diff.config`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_ci_compare_script.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_ci_compare_script.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_math_diff.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_math_diff.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_mycsv.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_mycsv.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_table_diff.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_table_diff.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/diffs/test_thresh_dict.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/diffs/test_thresh_dict.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/test_build_files_to_run.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/test_build_files_to_run.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/test_energyplus.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/test_energyplus.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/test_epw_map.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/test_epw_map.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/test_platform.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/test_platform.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/test_runtests.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/test_runtests.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tests/test_structures.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tests/test_structures.py`

 * *Files identical despite different names*

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions/tk_window.py` & `energyplus_regressions-2.0.2/energyplus_regressions/tk_window.py`

 * *Files 2% similar despite different names*

```diff
@@ -18,16 +18,18 @@
     E, W,  # Cardinal directions N, S,
     X, Y, BOTH,  # Orthogonal directions (for fill)
     END, LEFT, TOP,  # relative directions (RIGHT, TOP)
     filedialog, simpledialog,  # system dialogs
 )
 from typing import List, Union
 
+from plan_tools.runtime import fixup_taskbar_icon_on_windows
 from pubsub import pub
 
+import energyplus_regressions
 from energyplus_regressions import VERSION
 from energyplus_regressions.builds.base import KnownBuildTypes, autodetect_build_dir_type, BaseBuildDirectoryStructure
 from energyplus_regressions.builds.install import EPlusInstallDirectory
 from energyplus_regressions.builds.makefile import CMakeCacheMakeFileBuildDirectory
 from energyplus_regressions.builds.visualstudio import CMakeCacheVisualStudioBuildDirectory
 from energyplus_regressions.epw_map import get_epw_for_idf
 from energyplus_regressions.runtests import TestRunConfiguration, SuiteRunner
@@ -136,18 +138,35 @@
 class MyApp(Frame):
 
     def __init__(self):
         self.root = Tk(className='energyplus_regression_runner')
         Frame.__init__(self, self.root)
 
         # add the taskbar icon, but its having issues reading the png on Mac, not sure.
-        self.icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ep.png')
-        if system() != 'Darwin':
-            img = PhotoImage(file=self.icon_path)
-            self.root.iconphoto(False, img)
+        if system() == 'Darwin':
+            self.icon_path = Path(__file__).resolve().parent / 'icons' / 'icon.icns'
+            if self.icon_path.exists():
+                self.root.iconbitmap(str(self.icon_path))
+            else:
+                print(f"Could not set icon for Mac, expecting to find it at {self.icon_path}")
+        elif system() == 'Windows':
+            self.icon_path = Path(__file__).resolve().parent / 'icons' / 'icon.png'
+            img = PhotoImage(file=str(self.icon_path))
+            if self.icon_path.exists():
+                self.root.iconphoto(False, img)
+            else:
+                print(f"Could not set icon for Windows, expecting to find it at {self.icon_path}")
+        else:  # Linux
+            self.icon_path = Path(__file__).resolve().parent / 'icons' / 'icon.png'
+            img = PhotoImage(file=str(self.icon_path))
+            if self.icon_path.exists():
+                self.root.iconphoto(False, img)
+            else:
+                print(f"Could not set icon for Windows, expecting to find it at {self.icon_path}")
+        fixup_taskbar_icon_on_windows(energyplus_regressions.NAME)
 
         # high level GUI configuration
         self.root.geometry('1000x600')
         self.root.resizable(width=True, height=True)
         self.root.option_add('*tearOff', False)  # keeps file menus from looking weird
 
         # members related to the background thread and operator instance
```

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions.egg-info/PKG-INFO` & `energyplus_regressions-2.0.2/energyplus_regressions.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: energyplus-regressions
-Version: 2.0.0
+Version: 2.0.2
 Summary: A Python 3 library for evaluating regressions between EnergyPlus builds.
 Home-page: https://github.com/NREL/EnergyPlusRegressionTool
 Author: Edwin Lee
 Author-email: 
 License: UNKNOWN
 Description: # EnergyPlus Regressions
```

### Comparing `energyplus_regressions-2.0.0/energyplus_regressions.egg-info/SOURCES.txt` & `energyplus_regressions-2.0.2/energyplus_regressions.egg-info/SOURCES.txt`

 * *Files 15% similar despite different names*

```diff
@@ -2,16 +2,16 @@
 MANIFEST.in
 README.md
 setup.cfg
 setup.py
 energyplus_regressions/__init__.py
 energyplus_regressions/__main__.py
 energyplus_regressions/build_files_to_run.py
+energyplus_regressions/configure.py
 energyplus_regressions/energyplus.py
-energyplus_regressions/ep.png
 energyplus_regressions/ep_platform.py
 energyplus_regressions/epw_map.py
 energyplus_regressions/runner.py
 energyplus_regressions/runtests.py
 energyplus_regressions/structures.py
 energyplus_regressions/tk_window.py
 energyplus_regressions.egg-info/PKG-INFO
@@ -28,14 +28,17 @@
 energyplus_regressions/diffs/__init__.py
 energyplus_regressions/diffs/ci_compare_script.py
 energyplus_regressions/diffs/math_diff.config
 energyplus_regressions/diffs/math_diff.py
 energyplus_regressions/diffs/mycsv.py
 energyplus_regressions/diffs/table_diff.py
 energyplus_regressions/diffs/thresh_dict.py
+energyplus_regressions/icons/icon.icns
+energyplus_regressions/icons/icon.ico
+energyplus_regressions/icons/icon.png
 energyplus_regressions/tests/__init__.py
 energyplus_regressions/tests/test_build_files_to_run.py
 energyplus_regressions/tests/test_energyplus.py
 energyplus_regressions/tests/test_epw_map.py
 energyplus_regressions/tests/test_platform.py
 energyplus_regressions/tests/test_runtests.py
 energyplus_regressions/tests/test_structures.py
```

