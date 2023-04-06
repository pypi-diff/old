# Comparing `tmp/seamm-2023.4.8.tar.gz` & `tmp/seamm-220.8.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "seamm-2023.4.8.tar", last modified: Thu Mar  9 15:15:11 2023, max compression
+gzip compressed data, was "dist/seamm-220.8.3.tar", last modified: Mon Aug  3 19:36:19 2020, max compression
```

## Comparing `seamm-2023.4.8.tar` & `seamm-220.8.3.tar`

### file list

```diff
@@ -1,90 +1,65 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.044723 seamm-2023.4.8/
--rw-r--r--   0 runner    (1001) docker     (123)      151 2023-03-09 15:14:49.000000 seamm-2023.4.8/AUTHORS.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3235 2023-03-09 15:14:49.000000 seamm-2023.4.8/CONTRIBUTING.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1378 2023-03-09 15:14:49.000000 seamm-2023.4.8/HISTORY.rst
--rw-r--r--   0 runner    (1001) docker     (123)     7653 2023-03-09 15:14:49.000000 seamm-2023.4.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      353 2023-03-09 15:14:49.000000 seamm-2023.4.8/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     4354 2023-03-09 15:15:11.044723 seamm-2023.4.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2074 2023-03-09 15:14:49.000000 seamm-2023.4.8/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.036723 seamm-2023.4.8/docs/
--rw-r--r--   0 runner    (1001) docker     (123)     6758 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/Makefile
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.036723 seamm-2023.4.8/docs/_static/
--rw-r--r--   0 runner    (1001) docker     (123)    20790 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/_static/SEAMM inverted.png
--rw-r--r--   0 runner    (1001) docker     (123)    17802 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/_static/SEAMM logo.png
--rw-r--r--   0 runner    (1001) docker     (123)    79373 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/_static/molssi_main_logo.png
--rw-r--r--   0 runner    (1001) docker     (123)    68255 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/_static/molssi_main_logo_inverted_white.png
--rw-r--r--   0 runner    (1001) docker     (123)    63967 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/_static/molssi_square.png
--rw-r--r--   0 runner    (1001) docker     (123)    32355 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/_static/nsf.png
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.040723 seamm-2023.4.8/docs/api/
--rw-r--r--   0 runner    (1001) docker     (123)       89 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/api/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/authors.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)     9467 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/conf.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.040723 seamm-2023.4.8/docs/developer_guide/
--rw-r--r--   0 runner    (1001) docker     (123)       36 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/developer_guide/contributing.rst
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/developer_guide/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1446 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/developer_guide/installation.rst
--rw-r--r--   0 runner    (1001) docker     (123)       76 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/developer_guide/usage.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.040723 seamm-2023.4.8/docs/getting_started/
--rw-r--r--   0 runner    (1001) docker     (123)     1013 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/getting_started/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/history.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1228 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6457 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/make.bat
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.040723 seamm-2023.4.8/docs/user_guide/
--rw-r--r--   0 runner    (1001) docker     (123)      261 2023-03-09 15:14:49.000000 seamm-2023.4.8/docs/user_guide/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-03-09 15:14:49.000000 seamm-2023.4.8/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-09 15:14:49.000000 seamm-2023.4.8/requirements_dev.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.048723 seamm-2023.4.8/seamm/
--rw-r--r--   0 runner    (1001) docker     (123)     1978 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    10013 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/__main__.py
--rw-r--r--   0 runner    (1001) docker     (123)      500 2023-03-09 15:15:11.048723 seamm-2023.4.8/seamm/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)     2012 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/builtins.py
--rw-r--r--   0 runner    (1001) docker     (123)     7132 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/dashboard_handler.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.044723 seamm-2023.4.8/seamm/data/
--rw-r--r--   0 runner    (1001) docker     (123)    17802 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/data/SEAMM logo.png
--rw-r--r--   0 runner    (1001) docker     (123)    62090 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/data/SEAMM.png
--rw-r--r--   0 runner    (1001) docker     (123)    21448 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/data/SEAMM.svg
--rw-r--r--   0 runner    (1001) docker     (123)    41902 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/data/SEAMM_notext.png
--rw-r--r--   0 runner    (1001) docker     (123)    19358 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/data/SEAMM_notext.svg
--rw-r--r--   0 runner    (1001) docker     (123)      280 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/data/dashboards.ini
--rw-r--r--   0 runner    (1001) docker     (123)      116 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/data.py
--rw-r--r--   0 runner    (1001) docker     (123)    10317 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/exec_flowchart.py
--rw-r--r--   0 runner    (1001) docker     (123)    10799 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/exec_local.py
--rw-r--r--   0 runner    (1001) docker     (123)    18338 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/flowchart.py
--rw-r--r--   0 runner    (1001) docker     (123)     5712 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/graph.py
--rw-r--r--   0 runner    (1001) docker     (123)     1493 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/join_node.py
--rw-r--r--   0 runner    (1001) docker     (123)    40279 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/node.py
--rw-r--r--   0 runner    (1001) docker     (123)    22012 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)     1754 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/plugin_manager.py
--rw-r--r--   0 runner    (1001) docker     (123)    14861 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/run_flowchart.py
--rw-r--r--   0 runner    (1001) docker     (123)     3884 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/seammrc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/split_node.py
--rw-r--r--   0 runner    (1001) docker     (123)     6517 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/standard_parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)     2062 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/start_node.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.044723 seamm-2023.4.8/seamm/templates/
--rw-r--r--   0 runner    (1001) docker     (123)     2477 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/templates/band_structure.graph_template
--rw-r--r--   0 runner    (1001) docker     (123)     3157 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/templates/band_structure.html_template
--rw-r--r--   0 runner    (1001) docker     (123)     1852 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/templates/line.graph_template
--rw-r--r--   0 runner    (1001) docker     (123)     2492 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/templates/line.html_template
--rw-r--r--   0 runner    (1001) docker     (123)     5004 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/tk_edge.py
--rw-r--r--   0 runner    (1001) docker     (123)    50609 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/tk_flowchart.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    28129 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/tk_job_handler.py
--rw-r--r--   0 runner    (1001) docker     (123)     1209 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/tk_join_node.py
--rw-r--r--   0 runner    (1001) docker     (123)    38255 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/tk_node.py
--rw-r--r--   0 runner    (1001) docker     (123)    31896 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/tk_open.py
--rw-r--r--   0 runner    (1001) docker     (123)     7135 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/tk_publish.py
--rw-r--r--   0 runner    (1001) docker     (123)     1143 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/tk_split_node.py
--rw-r--r--   0 runner    (1001) docker     (123)     9550 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/tk_start_node.py
--rw-r--r--   0 runner    (1001) docker     (123)     5868 2023-03-09 15:14:49.000000 seamm-2023.4.8/seamm/variables.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.044723 seamm-2023.4.8/seamm.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4354 2023-03-09 15:15:11.000000 seamm-2023.4.8/seamm.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1758 2023-03-09 15:15:11.000000 seamm-2023.4.8/seamm.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-09 15:15:11.000000 seamm-2023.4.8/seamm.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      226 2023-03-09 15:15:11.000000 seamm-2023.4.8/seamm.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      208 2023-03-09 15:15:11.000000 seamm-2023.4.8/seamm.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        6 2023-03-09 15:15:11.000000 seamm-2023.4.8/seamm.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      345 2023-03-09 15:15:11.044723 seamm-2023.4.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     3034 2023-03-09 15:14:49.000000 seamm-2023.4.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-09 15:15:11.044723 seamm-2023.4.8/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-03-09 15:14:49.000000 seamm-2023.4.8/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      572 2023-03-09 15:14:49.000000 seamm-2023.4.8/tests/test_molssi_workflow.py
--rw-r--r--   0 runner    (1001) docker     (123)    68611 2023-03-09 15:14:49.000000 seamm-2023.4.8/versioneer.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-03 19:36:19.202370 seamm-220.8.3/
+-rw-rw-r--   0 travis    (2000) travis    (2000)      151 2020-08-03 19:34:30.000000 seamm-220.8.3/AUTHORS.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3235 2020-08-03 19:34:30.000000 seamm-220.8.3/CONTRIBUTING.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)       89 2020-08-03 19:34:30.000000 seamm-220.8.3/HISTORY.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7653 2020-08-03 19:34:30.000000 seamm-220.8.3/LICENSE
+-rw-rw-r--   0 travis    (2000) travis    (2000)      309 2020-08-03 19:34:30.000000 seamm-220.8.3/MANIFEST.in
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3268 2020-08-03 19:36:19.206368 seamm-220.8.3/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1924 2020-08-03 19:34:30.000000 seamm-220.8.3/README.rst
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-03 19:36:19.198372 seamm-220.8.3/docs/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6758 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/Makefile
+-rw-rw-r--   0 travis    (2000) travis    (2000)       28 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/authors.rst
+-rwxrwxr-x   0 travis    (2000) travis    (2000)     8349 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/conf.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)       33 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/contributing.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)       28 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/history.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)      290 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/index.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2404 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/installation.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6457 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/make.bat
+-rw-rw-r--   0 travis    (2000) travis    (2000)       27 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/readme.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)       65 2020-08-03 19:34:30.000000 seamm-220.8.3/docs/usage.rst
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-03 19:36:19.206368 seamm-220.8.3/seamm/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1884 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6434 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/__main__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      499 2020-08-03 19:36:19.206368 seamm-220.8.3/seamm/_version.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2028 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/builtins.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-03 19:36:19.202370 seamm-220.8.3/seamm/data/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    17802 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/data/SEAMM logo.png
+-rw-rw-r--   0 travis    (2000) travis    (2000)    62090 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/data/SEAMM.png
+-rw-rw-r--   0 travis    (2000) travis    (2000)    21448 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/data/SEAMM.svg
+-rw-rw-r--   0 travis    (2000) travis    (2000)    41902 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/data/SEAMM_notext.png
+-rw-rw-r--   0 travis    (2000) travis    (2000)    19358 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/data/SEAMM_notext.svg
+-rw-rw-r--   0 travis    (2000) travis    (2000)      116 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/data.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6190 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/exec_flowchart.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7168 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/exec_local.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    12489 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/flowchart.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6073 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/graph.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1538 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/join_node.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18487 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/node.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    22183 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/parameters.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1763 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/plugin_manager.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    10255 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/run_flowchart.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1561 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/split_node.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2469 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/start_node.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-03 19:36:19.202370 seamm-220.8.3/seamm/templates/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1852 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/templates/line.graph_template
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2492 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/templates/line.html_template
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4912 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/tk_edge.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    50456 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/tk_flowchart.py
+-rwxrwxr-x   0 travis    (2000) travis    (2000)    26558 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/tk_job_handler.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1338 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/tk_join_node.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    29046 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/tk_node.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1294 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/tk_split_node.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1459 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/tk_start_node.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5928 2020-08-03 19:34:30.000000 seamm-220.8.3/seamm/variables.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-03 19:36:19.202370 seamm-220.8.3/seamm.egg-info/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3268 2020-08-03 19:36:19.000000 seamm-220.8.3/seamm.egg-info/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1145 2020-08-03 19:36:19.000000 seamm-220.8.3/seamm.egg-info/SOURCES.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-08-03 19:36:19.000000 seamm-220.8.3/seamm.egg-info/dependency_links.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      227 2020-08-03 19:36:19.000000 seamm-220.8.3/seamm.egg-info/entry_points.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      144 2020-08-03 19:36:19.000000 seamm-220.8.3/seamm.egg-info/requires.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)        6 2020-08-03 19:36:19.000000 seamm-220.8.3/seamm.egg-info/top_level.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      533 2020-08-03 19:36:19.206368 seamm-220.8.3/setup.cfg
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2950 2020-08-03 19:34:30.000000 seamm-220.8.3/setup.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-08-03 19:36:19.202370 seamm-220.8.3/tests/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       60 2020-08-03 19:34:30.000000 seamm-220.8.3/tests/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      572 2020-08-03 19:34:30.000000 seamm-220.8.3/tests/test_molssi_workflow.py
```

### Comparing `seamm-2023.4.8/CONTRIBUTING.rst` & `seamm-220.8.3/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/LICENSE` & `seamm-220.8.3/LICENSE`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/docs/Makefile` & `seamm-220.8.3/docs/Makefile`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/docs/_static/SEAMM logo.png` & `seamm-220.8.3/seamm/data/SEAMM logo.png`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/docs/conf.py` & `seamm-220.8.3/docs/conf.py`

 * *Files 15% similar despite different names*

```diff
@@ -16,273 +16,240 @@
 import sys
 import os
 
 # If extensions (or modules to document with autodoc) are in another
 # directory, add these directories to sys.path here. If the directory is
 # relative to the documentation root, use os.path.abspath to make it
 # absolute, like shown here.
-# sys.path.insert(0, os.path.abspath('.'))
+#sys.path.insert(0, os.path.abspath('.'))
 
 # Get the project root dir, which is the parent dir of this
 cwd = os.getcwd()
 project_root = os.path.dirname(cwd)
 
 # Insert the project root dir as the first element in the PYTHONPATH.
 # This lets us ensure that the source package is imported, and that its
 # version is used.
 sys.path.insert(0, project_root)
 
-import seamm  # noqa: E402
+import seamm
 
 # -- General configuration ---------------------------------------------
 
 # If your documentation needs a minimal Sphinx version, state it here.
-# needs_sphinx = '1.0'
+#needs_sphinx = '1.0'
 
 # Add any Sphinx extension module names here, as strings. They can be
 # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
-extensions = [
-    'sphinx.ext.autodoc',
-    'sphinx.ext.githubpages',
-    'sphinx.ext.napoleon',
-    'sphinx.ext.viewcode',
-    'sphinx_design',
-    'sphinx_copybutton',
-    'sphinx.ext.todo',
-]
+extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']
 
 # Add any paths that contain templates here, relative to this directory.
 templates_path = ['_templates']
 
 # The suffix of source filenames.
 source_suffix = '.rst'
 
 # The encoding of source files.
-# source_encoding = 'utf-8-sig'
+#source_encoding = 'utf-8-sig'
 
 # The master toctree document.
 master_doc = 'index'
 
 # General information about the project.
 project = u'SEAMM'
-copyright = u"2017-2023, Molecular Sciences Software Institute (MolSSI)"
+copyright = u"2018, Paul Saxe"
 
 # The version info for the project you're documenting, acts as replacement
 # for |version| and |release|, also used in various other places throughout
 # the built documents.
 #
 # The short X.Y version.
 version = seamm.__version__
 # The full version, including alpha/beta/rc tags.
 release = seamm.__version__
 
 # The language for content autogenerated by Sphinx. Refer to documentation
 # for a list of supported languages.
-# language = None
+#language = None
 
 # There are two options for replacing |today|: either, you set today to
 # some non-false value, then it is used:
-# today = ''
+#today = ''
 # Else, today_fmt is used as the format for a strftime call.
-# today_fmt = '%B %d, %Y'
+#today_fmt = '%B %d, %Y'
 
 # List of patterns, relative to source directory, that match files and
 # directories to ignore when looking for source files.
 exclude_patterns = ['_build']
 
 # The reST default role (used for this markup: `text`) to use for all
 # documents.
-# default_role = None
+#default_role = None
 
 # If true, '()' will be appended to :func: etc. cross-reference text.
-# add_function_parentheses = True
+#add_function_parentheses = True
 
 # If true, the current module name will be prepended to all description
 # unit titles (such as .. function::).
-# add_module_names = True
+#add_module_names = True
 
 # If true, sectionauthor and moduleauthor directives will be shown in the
 # output. They are ignored by default.
-# show_authors = False
+#show_authors = False
 
 # The name of the Pygments (syntax highlighting) style to use.
-pygments_style = 'default'
+pygments_style = 'sphinx'
 
 # A list of ignored prefixes for module index sorting.
-# modindex_common_prefix = []
+#modindex_common_prefix = []
 
 # If true, keep warnings as "system message" paragraphs in the built
 # documents.
-# keep_warnings = False
+#keep_warnings = False
 
 
 # -- Options for HTML output -------------------------------------------
 
 # The theme to use for HTML and HTML Help pages.  See the documentation for
 # a list of builtin themes.
-html_theme = "pydata_sphinx_theme"
+html_theme = 'default'
 
 # Theme options are theme-specific and customize the look and feel of a
 # theme further.  For a list of options available for each theme, see the
 # documentation.
-# html_theme_options = {}
-html_theme_options = {
-    "github_url": "https://github.com/molssi-seamm/seamm",
-    "twitter_url": "https://twitter.com/MolSSI_NSF",
-    "logo": {
-        "image_light": "SEAMM logo.png",
-        "image_dark": "SEAMM Inverted 288x181.png",
-        "text": "SEAMM Package",
-        "molssi_light": "molssi_main_logo.png",
-        "molssi_dark": "molssi_main_logo_inverted_white.png",
-    },
-    "show_toc_level": 2,
-    "header_links_before_dropdown": 4,
-    "external_links": [
-        {"name": "SEAMM Documentation", "url": "https://molssi-seamm.github.io"},
-        {"name": "MolSSI", "url": "https://molssi.org"}
-    ],
-    "secondary_sidebar_items": ["page-toc", "sourcelink"],
-    "footer_items": [ "molssi_footer" ],
-}
+#html_theme_options = {}
 
 # Add any paths that contain custom themes here, relative to this directory.
-# html_theme_path = []
+#html_theme_path = []
 
 # The name for this set of Sphinx documents.  If None, it defaults to
 # "<project> v<release> documentation".
-# html_title = None
+#html_title = None
 
 # A shorter title for the navigation bar.  Default is the same as
 # html_title.
-# html_short_title = None
+#html_short_title = None
 
 # The name of an image file (relative to this directory) to place at the
 # top of the sidebar.
-# html_logo = None
+#html_logo = None
 
 # The name of an image file (within the static path) to use as favicon
 # of the docs.  This file should be a Windows icon file (.ico) being
 # 16x16 or 32x32 pixels large.
-# html_favicon = None
+#html_favicon = None
 
 # Add any paths that contain custom static files (such as style sheets)
 # here, relative to this directory. They are copied after the builtin
 # static files, so a file named "default.css" will overwrite the builtin
 # "default.css".
 html_static_path = ['_static']
 
-# These paths are either relative to html_static_path
-# or fully qualified paths (eg. https://...)
-html_css_files = [
-    'css/custom.css',
-]
-
 # If not '', a 'Last updated on:' timestamp is inserted at every page
 # bottom, using the given strftime format.
-# html_last_updated_fmt = '%b %d, %Y'
+#html_last_updated_fmt = '%b %d, %Y'
 
 # If true, SmartyPants will be used to convert quotes and dashes to
 # typographically correct entities.
-# html_use_smartypants = True
+#html_use_smartypants = True
 
 # Custom sidebar templates, maps document names to template names.
-# html_sidebars = {}
+#html_sidebars = {}
 
 # Additional templates that should be rendered to pages, maps page names
 # to template names.
-# html_additional_pages = {}
+#html_additional_pages = {}
 
 # If false, no module index is generated.
-# html_domain_indices = True
+#html_domain_indices = True
 
 # If false, no index is generated.
-# html_use_index = True
+#html_use_index = True
 
 # If true, the index is split into individual pages for each letter.
-# html_split_index = False
+#html_split_index = False
 
 # If true, links to the reST sources are added to the pages.
-# html_show_sourcelink = True
+#html_show_sourcelink = True
 
 # If true, "Created using Sphinx" is shown in the HTML footer.
 # Default is True.
-html_show_sphinx = False
+#html_show_sphinx = True
 
 # If true, "(C) Copyright ..." is shown in the HTML footer.
 # Default is True.
-html_show_copyright = False
+#html_show_copyright = True
 
 # If true, an OpenSearch description file will be output, and all pages
 # will contain a <link> tag referring to it.  The value of this option
 # must be the base URL from which the finished HTML is served.
-# html_use_opensearch = ''
+#html_use_opensearch = ''
 
 # This is the file name suffix for HTML files (e.g. ".xhtml").
-# html_file_suffix = None
+#html_file_suffix = None
 
 # Output file base name for HTML help builder.
 htmlhelp_basename = 'seammdoc'
 
 
 # -- Options for LaTeX output ------------------------------------------
 
 latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
-    # 'papersize': 'letterpaper',
+    #'papersize': 'letterpaper',
 
     # The font size ('10pt', '11pt' or '12pt').
-    # 'pointsize': '10pt',
+    #'pointsize': '10pt',
 
     # Additional stuff for the LaTeX preamble.
-    # 'preamble': '',
+    #'preamble': '',
 }
 
 # Grouping the document tree into LaTeX files. List of tuples
 # (source start file, target name, title, author, documentclass
 # [howto/manual]).
 latex_documents = [
     ('index', 'seamm.tex',
      u'SEAMM Documentation',
      u'Paul Saxe', 'manual'),
 ]
 
 # The name of an image file (relative to this directory) to place at
 # the top of the title page.
-# latex_logo = None
+#latex_logo = None
 
 # For "manual" documents, if this is true, then toplevel headings
 # are parts, not chapters.
-# latex_use_parts = False
+#latex_use_parts = False
 
 # If true, show page references after internal links.
-# latex_show_pagerefs = False
+#latex_show_pagerefs = False
 
 # If true, show URL addresses after external links.
-# latex_show_urls = False
+#latex_show_urls = False
 
 # Documents to append as an appendix to all manuals.
-# latex_appendices = []
+#latex_appendices = []
 
 # If false, no module index is generated.
-# latex_domain_indices = True
+#latex_domain_indices = True
 
 
 # -- Options for manual page output ------------------------------------
 
 # One entry per manual page. List of tuples
 # (source start file, name, description, authors, manual section).
 man_pages = [
     ('index', 'seamm',
      u'SEAMM Documentation',
      [u'Paul Saxe'], 1)
 ]
 
 # If true, show URL addresses after external links.
-# man_show_urls = False
+#man_show_urls = False
 
 
 # -- Options for Texinfo output ----------------------------------------
 
 # Grouping the document tree into Texinfo files. List of tuples
 # (source start file, target name, title, author,
 #  dir menu entry, description, category)
@@ -292,17 +259,17 @@
      u'Paul Saxe',
      'seamm',
      'One line description of project.',
      'Miscellaneous'),
 ]
 
 # Documents to append as an appendix to all manuals.
-# texinfo_appendices = []
+#texinfo_appendices = []
 
 # If false, no module index is generated.
-# texinfo_domain_indices = True
+#texinfo_domain_indices = True
 
 # How to display URL addresses: 'footnote', 'no', or 'inline'.
-# texinfo_show_urls = 'footnote'
+#texinfo_show_urls = 'footnote'
 
 # If true, do not generate a @detailmenu in the "Top" node's menu.
-# texinfo_no_detailmenu = False
+#texinfo_no_detailmenu = False
```

### Comparing `seamm-2023.4.8/docs/make.bat` & `seamm-220.8.3/docs/make.bat`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/seamm/__init__.py` & `seamm-220.8.3/seamm/__init__.py`

 * *Files 12% similar despite different names*

```diff
@@ -3,20 +3,22 @@
 """
 seamm
 Simulation Environment for Atomistic and Molecular Modeling.
 """
 
 import textwrap
 
+# Text handling
+from textwrap import dedent  # noqa: F401
+
 # Bring up the classes so that they appear to be directly in
 # the seamm package.
 
 from seamm.parameters import Parameter  # noqa: F401
 from seamm.parameters import Parameters  # noqa: F401
-import seamm.standard_parameters  # noqa: F401
 from seamm.variables import Variables  # noqa: F401
 from seamm.variables import flowchart_variables  # noqa: F401
 from seamm.plugin_manager import PluginManager  # noqa: F401
 from seamm.flowchart import Flowchart  # noqa: F401
 from seamm.tk_flowchart import TkFlowchart  # noqa: F401
 from seamm.graph import Graph  # noqa: F401
 from seamm.graph import Edge  # noqa: F401
@@ -30,23 +32,20 @@
 from seamm.split_node import Split  # noqa: F401
 from seamm.tk_split_node import TkSplit  # noqa: F401
 from seamm.builtins import SplitStep  # noqa: F401
 from seamm.join_node import Join  # noqa: F401
 from seamm.tk_join_node import TkJoin  # noqa: F401
 from seamm.builtins import JoinStep  # noqa: F401
 from seamm.tk_job_handler import TkJobHandler  # noqa: F401
-from .dashboard_handler import DashboardHandler  # noqa: F401
 from seamm.run_flowchart import run as run_flowchart  # noqa: F401
-from .seammrc import SEAMMrc  # noqa: F401
 
 wrap_text = textwrap.TextWrapper(width=120)
 wrap_stdout = textwrap.TextWrapper(width=120)
 
 # Handle versioneer
 from ._version import get_versions  # noqa: E402
-
 __author__ = """Paul Saxe"""
-__email__ = "psaxe@molssi.org"
+__email__ = 'psaxe@molssi.org'
 versions = get_versions()
-__version__ = versions["version"]
-__git_revision__ = versions["full-revisionid"]
+__version__ = versions['version']
+__git_revision__ = versions['full-revisionid']
 del get_versions, versions
```

### Comparing `seamm-2023.4.8/seamm/builtins.py` & `seamm-220.8.3/seamm/builtins.py`

 * *Files 12% similar despite different names*

```diff
@@ -6,55 +6,57 @@
 nodes."""
 
 import seamm
 
 
 class SplitStep(object):
     my_description = {
-        "description": "An interface for a node to split the control flow",
-        "group": "Control",
-        "name": "Split",
+        'description': 'An interface for a node to split the control flow',
+        'group': 'Control',
+        'name': 'Split'
     }
 
     def __init__(self, flowchart=None, gui=None):
         """Initialize this helper class, which is used by
         the application via stevedore to get information about
         and create node objects for the flowchart
         """
         pass
 
     def description(self):
-        """Return a description of what this extension does"""
+        """Return a description of what this extension does
+        """
         return SplitStep.my_description
 
     def create_node(self, flowchart=None, **kwargs):
         """Return the new node object"""
         return seamm.Split(flowchart=flowchart, **kwargs)
 
     def create_tk_node(self, canvas=None, **kwargs):
         """Return the graphical Tk node object"""
         return seamm.TkSplit(canvas=canvas, **kwargs)
 
 
 class JoinStep(object):
     my_description = {
-        "description": "An interface for a node to join the control flow",
-        "group": "Control",
-        "name": "Join",
+        'description': 'An interface for a node to join the control flow',
+        'group': 'Control',
+        'name': 'Join'
     }
 
     def __init__(self, flowchart=None, gui=None):
         """Initialize this helper class, which is used by
         the application via stevedore to get information about
         and create node objects for the flowchart
         """
         pass
 
     def description(self):
-        """Return a description of what this extension does"""
+        """Return a description of what this extension does
+        """
         return JoinStep.my_description
 
     def create_node(self, flowchart=None, **kwargs):
         """Return the new node object"""
         return seamm.Join(flowchart=flowchart, **kwargs)
 
     def create_tk_node(self, canvas=None, **kwargs):
```

### Comparing `seamm-2023.4.8/seamm/data/SEAMM.png` & `seamm-220.8.3/seamm/data/SEAMM.png`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/seamm/data/SEAMM.svg` & `seamm-220.8.3/seamm/data/SEAMM.svg`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/seamm/data/SEAMM_notext.png` & `seamm-220.8.3/seamm/data/SEAMM_notext.png`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/seamm/data/SEAMM_notext.svg` & `seamm-220.8.3/seamm/data/SEAMM_notext.svg`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/seamm/exec_flowchart.py` & `seamm-220.8.3/seamm/exec_flowchart.py`

 * *Files 26% similar despite different names*

```diff
@@ -6,261 +6,177 @@
 It provides the environment for running the computational tasks
 locally or remotely, using what is commonly called workflow management
 system (WMS).  The WMS concept, as used here, means tools that run
 given tasks without knowing anything about chemistry. The chemistry
 specialization is contained in the Flowchart and the nodes that it
 contains."""
 
-import calendar
 import logging
 import os.path
-from pathlib import Path
-import string
 import sys
 import traceback
 
-from molsystem import SystemDB
 import reference_handler
 import seamm
+from seamm_util import to_mmcif, to_cif
 import seamm_util.printing as printing
 from seamm_util.printing import FormattedText as __  # noqa: F401
-from seamm_util import getParser
 
 logger = logging.getLogger(__name__)
 job = printing.getPrinter()
 
 
 class ExecFlowchart(object):
+
     def __init__(self, flowchart=None):
         """Execute a flowchart, providing support for the actual
-        execution of codes"""
-        logger.info("In ExecFlowchart.init()")
+        execution of codes """
 
         self.flowchart = flowchart
 
     def run(self, root=None):
-        logger.info("In ExecFlowchart.run()")
         if not self.flowchart:
-            raise RuntimeError("There is no flowchart to run!")
-
-        # Get the command line options
-        parser = getParser(name="SEAMM")
-        options = parser.get_options()
-
-        # Set the options in each step
-        for node in self.flowchart:
-            step_type = node.step_type
-            logger.info(f"    setting options for {step_type}")
-            if step_type in options:
-                node._options = options[step_type]
-            if "SEAMM" in options:
-                node._global_options = options["SEAMM"]
+            raise RuntimeError('There is no flowchart to run!')
 
-        # Create the global context
-        logger.info("Creating global variables space")
+        logger.debug('Creating global variables space')
         seamm.flowchart_variables = seamm.Variables()
 
-        # And add the printer
-        seamm.flowchart_variables.set_variable("printer", job)
-
-        # Setup the citations
-        filename = os.path.join(self.flowchart.root_directory, "references.db")
-        references = None
-        try:
-            references = reference_handler.Reference_Handler(filename)
-        except Exception as e:
-            job.job("Error with references:")
-            job.job(e)
-
-        if references is not None:
-            template = string.Template(
-                """\
-                @misc{seamm,
-                  address      = {Virginia Tech, Blacksburg, VA, USA},
-                  author       = {Jessica Nash and
-                                  Eliseo Marin-Rimoldi and
-                                  Mohammad Mostafanejad and
-                                  Paul Saxe},
-                  doi          = {10.5281/zenodo.5153984},
-                  month        = {$month},
-                  note         = {Funding: NSF OAC-1547580 and CHE-2136142},
-                  organization = {The Molecular Sciences Software Institute (MolSSI)},
-                  publisher    = {Zenodo},
-                  title        = {SEAMM: Simulation Environment for Atomistic and
-                                  Molecular Modeling},
-                  url          = {https://doi.org/10.5281/zenodo.5153984},
-                  version      = {$version},
-                  year         = $year
-                }"""
-            )
-
-            try:
-                version = seamm.__version__
-                year, month = version.split(".")[0:2]
-                month = calendar.month_abbr[int(month)].lower()
-                citation = template.substitute(
-                    month=month,
-                    version=version,
-                    year=year,
-                )
-
-                references.cite(
-                    raw=citation,
-                    alias="SEAMM",
-                    module="seamm",
-                    level=1,
-                    note="The principle citation for SEAMM.",
-                )
-            except Exception as e:
-                job.job(f"Exception in citation {type(e)}: {e}")
-                job.job(traceback.format_exc())
-
-        # Create the system database, default system and configuration
-        if "SEAMM" in options:
-            seamm_options = options["SEAMM"]
-            read_only = "read_only" in seamm_options and seamm_options["read_only"]
-            db_file = seamm_options["database"]
-            if ":memory:" in db_file:
-                db = SystemDB(filename=db_file)
-            else:
-                path = Path(db_file).expanduser().resolve()
-                uri = "file:" + str(path)
-                if read_only:
-                    uri += "?mode=ro"
-                db = SystemDB(filename=uri)
-        else:
-            db = SystemDB(filename="file:seamm.db")
-
-        # Put the system database in the global context for access.
-        seamm.flowchart_variables.set_variable("_system_db", db)
-
         self.flowchart.root_directory = root
 
         # Correctly number the nodes
         self.flowchart.set_ids()
 
         # Write out an initial summary of the flowchart before doing anything
         # Reset the visited flag for traversal
         self.flowchart.reset_visited()
 
         # Get the start node
-        next_node = self.flowchart.get_node("1")
+        next_node = self.flowchart.get_node('1')
 
         # describe ourselves
-        job.job(("\nDescription of the flowchart" "\n----------------------------"))
+        job.job(
+            (
+                '\nDescription of the flowchart'
+                '\n----------------------------'
+            )
+        )
 
         while next_node:
-            # and print the description
             try:
                 next_node = next_node.describe()
             except Exception:
-                message = "Error describing the flowchart\n\n" + traceback.format_exc()
+                message = (
+                    'Error describing the flowchart\n\n' +
+                    traceback.format_exc()
+                )
                 print(message)
                 logger.critical(message)
                 raise
             except:  # noqa: E722
                 message = (
-                    "Unexpected error describing the flowchart\n\n"
-                    + traceback.format_exc()
+                    'Unexpected error describing the flowchart\n\n' +
+                    traceback.format_exc()
                 )
                 print(message)
                 logger.critical(message)
                 raise
 
-        job.job("")
+        job.job('')
 
         # And actually run it!
-        job.job(("Running the flowchart\n" "---------------------"))
+        job.job(('Running the flowchart\n' '---------------------'))
 
-        try:
-            next_node = self.flowchart.get_node("1")
-            while next_node is not None:
-                try:
-                    next_node = next_node.run()
-                except DeprecationWarning as e:
-                    print("\nDeprecation warning: " + str(e))
-                    traceback.print_exc(file=sys.stderr)
-                    traceback.print_exc(file=sys.stdout)
-        finally:
-            # Write the final structure
-            db = seamm.flowchart_variables.get_variable("_system_db")
-            system = db.system
-            if system is not None:
-                configuration = system.configuration
-                if configuration is not None:
-                    output = []
-                    if configuration.n_atoms > 0:
-                        # MMCIF file has bonds
-                        filename = os.path.join(
-                            self.flowchart.root_directory, "final_structure.mmcif"
-                        )
-                        text = None
-                        try:
-                            text = configuration.to_mmcif_text()
-                        except Exception:
-                            message = (
-                                "Error creating the final mmcif file\n\n"
-                                + traceback.format_exc()
-                            )
-                            print(message)
-                            logger.critical(message)
+        next_node = self.flowchart.get_node('1')
+        while next_node is not None:
+            try:
+                next_node = next_node.run()
+            except DeprecationWarning as e:
+                print('\nDeprecation warning: ' + str(e))
+                traceback.print_exc(file=sys.stderr)
+                traceback.print_exc(file=sys.stdout)
+            except Exception:
+                message = (
+                    'Error running the flowchart\n\n' + traceback.format_exc()
+                )
+                print(message)
+                logger.critical(message)
+                break
+            except:  # noqa: E722
+                message = (
+                    'Unexpected error running the flowchart\n\n' +
+                    traceback.format_exc()
+                )
+                print(message)
+                logger.critical(message)
+                raise
 
-                        if text is not None:
-                            with open(filename, "w") as fd:
-                                print(text, file=fd)
-                            output.append("final_structure.mmcif")
-                        # CIF file has cell
-                        if configuration.periodicity == 3:
-                            filename = os.path.join(
-                                self.flowchart.root_directory, "final_structure.cif"
-                            )
-                            with open(filename, "w") as fd:
-                                print(configuration.to_cif_text(), file=fd)
-                                output.append("final_structure.cif")
-                        if len(output) > 0:
-                            files = "' and '".join(output)
-                            job.job(
-                                f"\nWrote the final structure to '{files}' for viewing."
-                            )
+        # Write the final structure
+        if seamm.data.structure is not None:
+            system = seamm.data.structure
+            # MMCIF file has bonds
+            filename = os.path.join(
+                self.flowchart.root_directory, 'final_structure.mmcif'
+            )
+            with open(filename, 'w') as fd:
+                print(to_mmcif(system), file=fd)
+            job.job(
+                "\nWrote the final structure to 'final_structure.mmcif' for "
+                'viewing.'
+            )
+            # CIF file has cell
+            if system['periodicity'] == 3:
+                filename = os.path.join(
+                    self.flowchart.root_directory, 'final_structure.cif'
+                )
+                with open(filename, 'w') as fd:
+                    print(to_cif(seamm.data.structure), file=fd)
+                job.job(
+                    "\nWrote the final structure to 'final_structure.cif' for "
+                    'viewing.'
+                )
 
-            # And print out the references
-            filename = os.path.join(self.flowchart.root_directory, "references.db")
-            try:
-                references = reference_handler.Reference_Handler(filename)
-            except Exception as e:
-                job.job("Error with references:")
-                job.job(e)
-
-            if references.total_citations() > 0:
-                tmp = {}
-                citations = references.dump(fmt="text")
-                for citation, text, count, level in citations:
-                    if level not in tmp:
-                        tmp[level] = {}
-                    tmp[level][citation] = (text, count)
-
-                n = 0
-                for level in sorted(tmp.keys()):
-                    ref_dict = tmp[level]
-                    if level == 1:
-                        job.job("\nPrimary references:\n")
-                        n = 0
-                    elif level == 2:
-                        job.job("\nSecondary references:\n")
-                        n = 0
-                    else:
-                        job.job("\nLess important references:\n")
-                        n = 0
+        # And print out the references
+        filename = os.path.join(self.flowchart.root_directory, 'references.db')
+        try:
+            references = reference_handler.Reference_Handler(filename)
+        except Exception as e:
+            job.job('Error with references:')
+            job.job(e)
 
-                    lines = []
-                    for citation in sorted(ref_dict.keys()):
-                        n += 1
-                        text, count = ref_dict[citation]
-                        if count == 1:
-                            lines.append("({}) {:s}".format(n, text))
-                        else:
-                            lines.append(
-                                "({}) {:s} (used {:d} times)".format(n, text, count)
+        if references.total_citations() > 0:
+            tmp = {}
+            citations = references.dump(fmt='text')
+            for citation, text, count, level in citations:
+                if level not in tmp:
+                    tmp[level] = {}
+                tmp[level][citation] = (text, count)
+
+            for level in sorted(tmp.keys()):
+                ref_dict = tmp[level]
+                if level == 1:
+                    job.job('\nPrimary references:\n')
+                elif level == 2:
+                    job.job('\nSecondary references:\n')
+                else:
+                    job.job('\nLess important references:\n')
+
+                lines = []
+                for citation in sorted(ref_dict.keys()):
+                    text, count = ref_dict[citation]
+                    if count == 1:
+                        lines.append('({}) {:s}'.format(citation, text))
+                    else:
+                        lines.append(
+                            '({}) {:s} (used {:d} times)'.format(
+                                citation, text, count
                             )
-                    job.job(
-                        __("\n\n".join(lines), indent=4 * " ", indent_initial=False)
+                        )
+                job.job(
+                    __(
+                        '\n\n'.join(lines),
+                        indent=4 * ' ',
+                        indent_initial=False
                     )
+                )
+        # Close the reference handler, which should force it to close the
+        # connection.
+        del references
```

### Comparing `seamm-2023.4.8/seamm/exec_local.py` & `seamm-220.8.3/seamm/run_flowchart.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,311 +1,338 @@
 # -*- coding: utf-8 -*-
 
-"""The ExecLocal object does what it name implies: it executes, or
-runs, an executable locally."""
+"""Run a SEAMM flowchart.
 
-import glob
-import humanize
+SEAMM flowcharts have a 'magic' line, so that they can be executed directly.
+Or, run_flowchart can be invoked with the name of flowchart.
+"""
+
+import configargparse
+import cpuinfo
+import datetime
+import fasteners
+import json
+import locale
 import logging
+import seamm
+import seamm_util.printing as printing
 import os
 import os.path
-import platform
-import pprint
-import pyuca
+import re
 import shutil
-import stat
-import subprocess
 import sys
-import tempfile
 import time
 
-if platform.system() != "Windows":
-    import grp
-    import pwd
-
 logger = logging.getLogger(__name__)
+variables = seamm.Variables()
 
 
-class ExecLocal(object):
-    def __init__(self):
-        """Execute a flowchart, providing support for the actual
-        execution of codes"""
-
-        # times for formating 'ls' like output
-        self.now = int(time.time())
-        self.recent = self.now - (6 * 30 * 24 * 60 * 60)  # 6 months ago
-
-    def run(
-        self,
-        cmd=[],
-        input_data=None,
-        files=None,
-        env={},
-        return_files=[],
-        shell=False,
-        in_situ=False,
-        directory=None,
-    ):
-        """Execute 'cmd' in a temporary directory. 'files' is a dict
-        keyed by filename of files to write before execution."""
-
-        # Create temporary directory and write the files, being
-        # careful about both errors and security.
-
-        if in_situ:
-            if directory is None:
-                tmpdir = os.getcwd()
-            else:
-                tmpdir = str(directory)
-        else:
-            tmpdir = tempfile.mkdtemp()
-            # Ensure the file is read/write by the creator only
-            saved_umask = os.umask(0o077)
-
-        logging.info(f"Running locally in {tmpdir}")
-
-        if files is not None:
-            # Write locally if directory is given
-            if not in_situ and directory is not None:
-                for filename in files:
-                    path = os.path.join(directory, filename)
-                    mode = "wb" if type(files[filename]) is bytes else "w"
-                    with open(path, mode) as fd:
-                        fd.write(files[filename])
-            for filename in files:
-                path = os.path.join(tmpdir, filename)
-                mode = "wb" if type(files[filename]) is bytes else "w"
-                try:
-                    with open(path, mode) as fd:
-                        fd.write(files[filename])
-                except IOError:
-                    logging.exception(
-                        "An I/O error occured writing file '{}'".format(path)
-                    )
-                    if not in_situ:
-                        os.umask(saved_umask)
-                        shutil.rmtree(tmpdir)
-                    return None
-                except Exception:
-                    logging.exception(
-                        "An unexpected error occured writing file '{}'".format(path)
-                    )
-                    os.remove(path)
-                    if not in_situ:
-                        os.umask(saved_umask)
-                        shutil.rmtree(tmpdir)
-                    return None
-        # get a list of all existing files so we can determine what to delete
-        if in_situ:
-            existing = []
-            existing_directories = []
-            for dirpath, dirs, files in os.walk(tmpdir):
-                for name in files:
-                    existing.append(os.path.join(dirpath, name))
-                for name in dirs:
-                    existing_directories.append(os.path.join(dirpath, name))
-
-        # Now execute the program in the temp directory
-        logger.debug("about to run " + " ".join(cmd))
-
-        p = subprocess.run(
-            cmd,
-            input=input_data,
-            env=dict(os.environ, **env),
-            cwd=tmpdir,
-            universal_newlines=True,
-            stdout=subprocess.PIPE,
-            stderr=subprocess.PIPE,
-            shell=shell,
-        )
+class cd:
+    """Context manager for changing the current working directory"""
 
-        logger.debug("\n" + pprint.pformat(p))
+    def __init__(self, newPath):
+        self.newPath = os.path.expanduser(newPath)
 
-        if not in_situ:
-            os.umask(saved_umask)
+    def __enter__(self):
+        self.savedPath = os.getcwd()
+        os.chdir(self.newPath)
+
+    def __exit__(self, etype, value, traceback):
+        os.chdir(self.savedPath)
+
+
+def run(job_id=None, wdir=None, setup_logging=True):
+    """The standalone flowchart app
+    """
+
+    parser = configargparse.ArgParser(
+        auto_env_var_prefix='',
+        default_config_files=[
+            '/etc/seamm/seamm.ini',
+            '~/.seamm/seamm.ini',
+        ],
+        description='Execute a SEAMM flowchart'
+    )
+
+    parser.add_argument(
+        "--standalone",
+        action='store_true',
+        help="Run this workflow as-is without using the datastore, etc."
+    )
+    parser.add_argument(
+        '--seamm-configfile',
+        is_config_file=True,
+        default=None,
+        help='a configuration file to override others'
+    )
+    parser.add_argument(
+        "-v",
+        "--verbose",
+        dest="verbose_count",
+        action="count",
+        default=0,
+        help="increases log verbosity for each occurence."
+    )
+    parser.add_argument(
+        "--title",
+        dest="title",
+        default='',
+        action="store",
+        env_var='SEAMM_TITLE',
+        help="The title for this run."
+    )
+    parser.add_argument(
+        "--datastore",
+        dest="datastore",
+        default='.',
+        action="store",
+        env_var='SEAMM_DATASTORE',
+        help="The datastore (directory) for this run."
+    )
+    parser.add_argument(
+        "--job-id-file",
+        dest="job_id_file",
+        default=None,
+        action="store",
+        help="The job_id file to use."
+    )
+    parser.add_argument(
+        "--project",
+        dest="projects",
+        action="append",
+        env_var='SEAMM_PROJECT',
+        help="The project(s) for this job."
+    )
+    parser.add_argument("--force", dest="force", action='store_true')
+    parser.add_argument(
+        "--output",
+        choices=['files', 'stdout', 'both'],
+        default='files',
+        help='whether to put the output in files, direct to stdout, or both'
+    )
+    parser.add_argument(
+        "filename",
+        nargs='?',
+        help='the filename of the flowchart'
+    )  # yapf: disable
+
+    args, unknown = parser.parse_known_args()
+
+    # Whether to just run as-is, without getting a job_id, using the
+    # datastore, etc.
+    standalone = 'standalone' in args and args.standalone
+
+    if setup_logging:
+        # Set up logging level to WARNING by default, going more verbose
+        # for each new -v, to INFO and then DEBUG and finally ALL with 3 -v's
+
+        numeric_level = max(3 - args.verbose_count, 0) * 10
+        logging.basicConfig(level=numeric_level)
+
+    # Create the working directory where files, output, etc. go.
+    # At the moment this is datastore/job_id
+
+    if standalone:
+        print('Running in standalone mode.')
+        wdir = os.getcwd()
+    else:
+        datastore = os.path.expanduser(args.datastore)
+
+        if job_id is None:
+            if args.job_id_file is None:
+                job_id_file = os.path.join(datastore, 'job.id')
+
+            # Get the job_id from the file, creating the file if necessary
+            job_id = get_job_id(job_id_file)
+        if wdir is None:
+            if args.projects is None:
+                projects = ['default']
+            else:
+                projects = args.projects
 
-        # capture the return code and output
-        result = {
-            "returncode": p.returncode,
-            "stdout": p.stdout,
-            "stderr": p.stderr,
-        }
-
-        # capture the list of files in the directory
-        c = pyuca.Collator()
-        listing = ""
-        self.now = int(time.time())
-        self.recent = self.now - (6 * 30 * 24 * 60 * 60)  # 6 months ago
-        for dirpath, dirs, files in os.walk(tmpdir):
-            # Do locale sensitive sort of files to list
-            listing += (
-                dirpath
-                + "\n"
-                + "\n\t".join(self.ls_format(dirpath, sorted(files, key=c.sort_key)))
+            # And put it all together
+            wdir = os.path.abspath(
+                os.path.join(
+                    datastore, 'projects', projects[0],
+                    'Job_{:06d}'.format(job_id)
+                )
             )
-        result["listing"] = listing
 
-        # capture the requested files
-        result["files"] = []
-        returned = []
-        for pattern in return_files:
-            filenames = glob.glob(os.path.join(tmpdir, pattern))
-            for path in filenames:
-                returned.append(path)
-                filename = os.path.basename(path)
-                data = None
-                exception = None
-                result["files"].append(filename)
-                try:
-                    with open(path, "r") as fd:
-                        data = fd.read()
+            if os.path.exists(wdir):
+                if args.force:
+                    shutil.rmtree(wdir)
+                else:
+                    msg = "Directory '{}' exists, use --force to overwrite"\
+                          .format(wdir)
 
-                except UnicodeDecodeError:
-                    with open(path, "rb") as fd:
-                        data = fd.read()
-
-                except IOError:
-                    exception = sys.exc_info()
-                    logging.warning(
-                        "An I/O error occurred reading file '{}'".format(filename),
-                        exc_info=exception,
-                    )
-                except Exception:
-                    exception = sys.exc_info()
-                    logging.warning(
-                        "An unexpected error occured reading file '{}'".format(
-                            filename
-                        ),
-                        exc_info=exception,
-                    )
-                finally:
-                    result[filename] = {"exception": exception, "data": data}
+                    logging.critical(msg)
+                    sys.exit(msg)
 
-        # Clean up the temporary directory
-        if in_situ:
-            # Remove any files not originally here, or requested to return.
-            for dirpath, dirs, files in os.walk(tmpdir):
-                for name in files:
-                    filename = os.path.join(dirpath, name)
-                    if filename not in existing and filename not in returned:
-                        os.remove(filename)
-                for name in dirs:
-                    dirname = os.path.join(dirpath, name)
-                    if dirname not in existing_directories:
-                        os.rmdir(filename)
-            # And move any files the need to go in subdirectories
-            for filename in result["files"]:
-                if filename[0] == "@":
-                    subdir, fname = filename[1:].split("+")
-                    from_path = os.path.join(directory, filename)
-                    to_path = os.path.join(directory, subdir, fname)
-                    os.rename(from_path, to_path)
-        else:
-            shutil.rmtree(tmpdir)
+            os.makedirs(wdir, exist_ok=False)
 
-            # And write the results locally
-            if directory is not None:
-                for filename in result["files"]:
-                    if filename[0] == "@":
-                        subdir, fname = filename[1:].split("+")
-                        path = os.path.join(directory, subdir, fname)
-                    else:
-                        path = os.path.join(directory, filename)
-
-                    if result[filename]["data"] is not None:
-                        mode = "wb" if type(result[filename]["data"]) is bytes else "w"
-                        with open(path, mode=mode) as fd:
-                            fd.write(result[filename]["data"])
-                    else:
-                        with open(path, mode="w") as fd:
-                            fd.write(result[filename]["exception"])
-
-        # Write any stdout and stderr
-
-        if directory is not None:
-            if "stdout" in result and result["stdout"] != "":
-                path = os.path.join(directory, "stdout.txt")
-                with open(path, mode="w") as fd:
-                    fd.write(result["stdout"])
-
-            if result["stderr"] != "":
-                path = os.path.join(directory, "stderr.txt")
-                with open(path, mode="w") as fd:
-                    fd.write(result["stderr"])
-
-        return result
-
-    def get_mode_info(self, filename, mode):
-        """Get the mode information for 'ls' like listing"""
-
-        perms = "-"
-        link = ""
-
-        if stat.S_ISDIR(mode):
-            perms = "d"
-        elif stat.S_ISLNK(mode):
-            perms = "l"
-            link = os.readlink(filename)
-        mode = stat.S_IMODE(mode)
-        for who in "USR", "GRP", "OTH":
-            for what in "R", "W", "X":
-                # lookup attributes at runtime using getattr
-                if mode & getattr(stat, "S_I" + what + who):
-                    perms = perms + what.lower()
-                else:
-                    perms = perms + "-"
-        # return multiple bits of info in a tuple
-        return (perms, link)
-
-    def ls_format(self, path, files):
-        """Format a list of files as in 'ls'"""
-
-        result = []
-        for filename in files:
-            try:  # exceptions
-                # Get all the file info
-                stat_info = os.lstat(os.path.join(path, filename))
-            except Exception:
-                result.append("{}: No such file or directory".format(filename))
-                continue
+    logging.info("The working directory is '{}'".format(wdir))
+
+    # Set up the root printer, and add handlers to print to the file
+    # 'job.out' in the working directory and to stdout, as requested
+    # in the options. Since all printers are children of the root
+    # printer, all output at the right levels will flow here
+
+    printer = printing.getPrinter()
+
+    # Set up our formatter
+    formatter = logging.Formatter(fmt='{message:s}', style='{')
+
+    # A handler for stdout
+    if standalone or wdir is None:
+        console_handler = logging.StreamHandler()
+        # console_handler.setLevel(printing.JOB)
+        console_handler.setLevel(printing.NORMAL)
+        console_handler.setFormatter(formatter)
+        printer.addHandler(console_handler)
+
+    # A handler for the file
+    file_handler = logging.FileHandler(os.path.join(wdir, 'job.out'))
+    file_handler.setLevel(printing.NORMAL)
+    file_handler.setFormatter(formatter)
+    printer.addHandler(file_handler)
+
+    # And ... finally ... run!
+    printer.job("Running in directory '{}'".format(wdir))
+
+    flowchart_path = os.path.join(wdir, 'flowchart.flow')
+    if args.filename is not None:
+        # copy the flowchart to the root directory for later reference
+        shutil.copy2(args.filename, flowchart_path)
+
+    flowchart = seamm.Flowchart(directory=wdir, output=args.output)
+    flowchart.read(flowchart_path)
+
+    # Change to the working directory and run the flowchart
+    with cd(wdir):
+        if os.path.exists('job_data.json'):
+            with open('job_data.json', 'r') as fd:
+                data = json.load(fd)
+        else:
+            data = {}
 
-            perms, link = self.get_mode_info(
-                os.path.join(path, filename), stat_info.st_mode
+        # Set up the initial metadata for the job.
+        data.update(cpuinfo.get_cpu_info())
+        if 'command line' not in data:
+            data['command line'] = sys.argv
+        if 'title' not in data:
+            data['title'] = args.title
+        data['working directory'] = wdir
+        data['start time'] = time.strftime("%Y-%m-%d %H:%M:%S %Z")
+        data['state'] = 'started'
+        if not standalone:
+            if 'projects' not in data:
+                data['projects'] = projects
+            data['datastore'] = datastore
+            data['job id'] = job_id
+
+        # Output the initial metadate for the job.
+        with open('job_data.json', 'w') as fd:
+            json.dump(data, fd, indent=3, sort_keys=True)
+
+        t0 = time.time()
+        pt0 = time.process_time()
+
+        # And run the flowchart
+        try:
+            exec = seamm.ExecFlowchart(flowchart)
+            exec.run(root=wdir)
+            data['state'] = 'finished'
+        except Exception as e:
+            data['state'] = 'error'
+            data['error type'] = type(e).__name__
+            data['error message'] = str(e)
+
+        # Wrap things up
+        t1 = time.time()
+        pt1 = time.process_time()
+        data['end time'] = time.strftime("%Y-%m-%d %H:%M:%S %Z")
+        t = t1 - t0
+        pt = pt1 - pt0
+        data['elapsed time'] = t
+        data['process time'] = pt
+
+        with open('job_data.json', 'w') as fd:
+            json.dump(data, fd, indent=3, sort_keys=True)
+
+        printer.job(
+            "\nProcess time: {} ({:.3f} s)".format(
+                datetime.timedelta(seconds=pt), pt
             )
+        )
+        printer.job(
+            "Elapsed time: {} ({:.3f} s)".format(
+                datetime.timedelta(seconds=t), t
+            )
+        )
 
-            nlink = "%4d" % stat_info.st_nlink  # formatting strings
 
-            if platform.system() == "Windows":
-                name = 8 * " "
-                group = 8 * " "
-            else:
-                try:
-                    name = "%-8s" % pwd.getpwuid(stat_info.st_uid)[0]
-                except KeyError:
-                    name = "%-8s" % stat_info.st_uid
+def get_job_id(filename):
+    """Get the next job id from the given file.
 
+    This uses the fasteners module to provide locking so that
+    only one job at a time can access the file, so that the job
+    ids are unique and monotonically increasing.
+    """
+
+    lock_file = filename + '.lock'
+    lock = fasteners.InterProcessLock(lock_file)
+    locked = lock.acquire(blocking=True, timeout=5)
+
+    if locked:
+        if not os.path.isfile(filename):
+            job_id = 1
+            with open(filename, 'w') as fd:
+                fd.write('!MolSSI job_id 1.0\n')
+                fd.write('1\n')
+            lock.release()
+        else:
+            with open(filename, 'r+') as fd:
+                line = fd.readline()
+                pos = fd.tell()
+                if line == '':
+                    lock.release()
+                    raise EOFError(
+                        "job_id file '{}' is empty".format(filename)
+                    )
+                line = line.strip()
+                match = re.fullmatch(
+                    r'!MolSSI job_id ([0-9]+(?:\.[0-9]+)*)', line
+                )
+                if match is None:
+                    lock.release()
+                    raise RuntimeError(
+                        'The job_id file has an incorrect header: {}'
+                        .format(line)
+                    )
+                line = fd.readline()
+                if line == '':
+                    lock.release()
+                    raise EOFError(
+                        "job_id file '{}' is truncated".format(filename)
+                    )
                 try:
-                    group = "%-8s" % grp.getgrgid(stat_info.st_gid)[0]
-                except KeyError:
-                    group = "%-8s" % stat_info.st_gid
-
-            size = humanize.naturalsize(stat_info.st_size)
-
-            # Get time stamp of file
-            ts = stat_info.st_mtime
-            if (ts < self.recent) or (ts > self.now):  # boolean operators
-                time_fmt = "%b %e  %Y"
-            else:
-                time_fmt = "%b %e %R"
-            time_str = time.strftime(time_fmt, time.gmtime(ts))
-
-            # Format the result
-            tmp = "{} {} {} {} {} {} {}".format(
-                perms, nlink, name, group, size, time_str, filename
-            )
+                    job_id = int(line)
+                except TypeError:
+                    raise TypeError(
+                        "The job_id in file '{}' is not an integer: {}".format(
+                            filename, line
+                        )
+                    )
+                job_id += 1
+                fd.seek(pos)
+                fd.write('{:d}\n'.format(job_id))
+    else:
+        raise RuntimeError(
+            "Could not lock the job_id file '{}'".format(filename)
+        )
 
-            if link:
-                tmp += " -> " + link
+    return job_id
 
-            result.append(tmp)
 
-        return result
+if __name__ == "__main__":
+    locale.setlocale(locale.LC_ALL, '')
+    run()
```

### Comparing `seamm-2023.4.8/seamm/join_node.py` & `seamm-220.8.3/seamm/join_node.py`

 * *Files 12% similar despite different names*

```diff
@@ -5,48 +5,53 @@
 import seamm
 import seamm_util.printing as printing
 from seamm_util.printing import FormattedText as __
 import logging
 
 logger = logging.getLogger(__name__)
 job = printing.getPrinter()
-printer = printing.getPrinter("join")
+printer = printing.getPrinter('join')
 
 
 class Join(seamm.Node):
-    def __init__(self, flowchart=None, extension="Join"):
-        """Initialize a node for joining the flow together again
+
+    def __init__(self, flowchart=None, extension='Join'):
+        '''Initialize a node for joining the flow together again
 
         Keyword arguments:
-        """
-        logger.debug("Constructing join node {}".format(self))
-        super().__init__(flowchart=flowchart, title="Join", extension=extension)
+        '''
+        logger.debug('Constructing join node {}'.format(self))
+        super().__init__(
+            flowchart=flowchart, title='Join', extension=extension
+        )
 
     @property
     def version(self):
-        """The semantic version of this module."""
+        """The semantic version of this module.
+        """
         return seamm.__version__
 
     @property
     def git_revision(self):
-        """The git version of this module."""
+        """The git version of this module.
+        """
         return seamm.__git_revision__
 
     def description_text(self, P=None):
         """Return a short description of this step.
 
         Return a nicely formatted string describing what this step will
             do.
 
         Keyword arguments:
             P: a dictionary of parameter values, which may be variables
                 or final values. If None, then the parameters values will
                 be used as is.
-        """
+            """
 
         # if not P:
         #     P = self.parameters.values_to_dict()
 
-        text = ""
-        text += "Join threads together"
+        text = ''
+        text += 'Join threads together'
 
-        return self.header + "\n" + __(text, indent=4 * " ").__str__()
+        return self.header + '\n' + __(text, indent=4 * ' ').__str__()
```

### Comparing `seamm-2023.4.8/seamm/parameters.py` & `seamm-220.8.3/seamm/parameters.py`

 * *Files 2% similar despite different names*

```diff
@@ -32,32 +32,32 @@
     This is object is a dict-like mutable mapping with properties
     to make it appear to be a simple object with attributes.
     """
 
     def __init__(self, *args, **kwargs):
         """Initialize this parameter"""
 
-        logger.debug("\nParameter.__init__")
+        logger.debug('\nParameter.__init__')
 
         self._data = {}
         self.dimensionality = None
         self._widget = None
 
         self.reset()
 
         # Handle positional or keyword arguments
         for data in args:
             if isinstance(data, dict):
                 self.update(data)
             else:
-                raise RuntimeError("Positional arguments must be dicts")
+                raise RuntimeError('Positional arguments must be dicts')
 
         self.update(kwargs)
 
-        logger.debug("Finished constructing Parameter\n")
+        logger.debug('Finished constructing Parameter\n')
 
     def __getitem__(self, key):
         """Allow [] access to the dictionary!"""
         return self._data[key]
 
     def __setitem__(self, key, value):
         """Allow x[key] access to the data"""
@@ -73,60 +73,57 @@
 
     def __len__(self):
         """The len() command"""
         return len(self._data)
 
     def __repr__(self):
         """The official string representation of this object"""
-        if self.units is None or self.units == "":
+        if self.units is None or self.units == '':
             return self.value
         else:
-            return ("{} {}").format(self.value, self.units)
+            return ('{} {}').format(self.value, self.units)
 
     def __str__(self):
-        if self.units is None or self.units == "":
-            if self.kind == "integer":
+        if self.units is None or self.units == '':
+            if self.kind == 'integer':
                 try:
                     value = int(self.value)
-                    return ("{:" + self.format_string + "}").format(value)
+                    return ('{:' + self.format_string + '}').format(value)
                 except Exception:
-                    return ("{}").format(self.value)
-            if self.kind == "float":
+                    return ('{}').format(self.value)
+            if self.kind == 'float':
                 try:
                     value = float(self.value)
-                    return ("{:" + self.format_string + "}").format(value)
+                    return ('{:' + self.format_string + '}').format(value)
                 except ValueError:
-                    return ("{}").format(self.value)
-            if self.format_string == "":
+                    return ('{}').format(self.value)
+            if self.format_string == '':
                 return str(self.value)
             else:
-                return ("{:" + self.format_string + "}").format(self.value)
+                return ('{:' + self.format_string + '}').format(self.value)
         else:
-            if self.kind == "integer":
+            if self.kind == 'integer':
                 try:
                     value = int(self.value)
-                    return ("{:" + self.format_string + "} {}").format(
-                        value, self.units
-                    )
+                    return ('{:' + self.format_string +
+                            '} {}').format(value, self.units)
                 except ValueError:
-                    return ("{} {}").format(self.value, self.units)
-            if self.kind == "float":
+                    return ('{} {}').format(self.value, self.units)
+            if self.kind == 'float':
                 try:
                     value = float(self.value)
-                    return ("{:" + self.format_string + "} {}").format(
-                        value, self.units
-                    )
+                    return ('{:' + self.format_string +
+                            '} {}').format(value, self.units)
                 except Exception:
-                    return ("{} {}").format(self.value, self.units)
-            if self.format_string == "":
-                return "{} {}".format(self.value, self.units)
+                    return ('{} {}').format(self.value, self.units)
+            if self.format_string == '':
+                return '{} {}'.format(self.value, self.units)
             else:
-                return ("{:" + self.format_string + "} {}").format(
-                    self.value, self.units
-                )
+                return ('{:' + self.format_string +
+                        '} {}').format(self.value, self.units)
 
     def __contains__(self, item):
         """Return a boolean indicating if a key exists."""
         if item in self._data:
             return True
         return False
 
@@ -140,104 +137,107 @@
 
     @property
     def value(self):
         """The current value of the parameter. May be a value, a
         Python expression containing variables prefix with $,
         standard operators or parentheses."""
 
-        if "value" not in self._data:
-            self._data["value"] = self._data["default"]
+        if 'value' not in self._data:
+            self._data['value'] = self._data['default']
 
-        result = self._data["value"]
+        result = self._data['value']
         if result is None:
-            result = self._data["default"]
+            result = self._data['default']
 
         return result
 
     @value.setter
     def value(self, value):
-        self._data["value"] = value
+        self._data['value'] = value
 
     @property
     def default(self):
         """The current default of the parameter. May be a value, a
         Python expression containing variables prefix with $,
         standard operators or parenthesise, or a pint units
         quantity."""
 
-        return self._data["default"]
+        return self._data['default']
 
     @default.setter
     def default(self, value):
-        self._data["default"] = value
+        self._data['default'] = value
 
     @property
     def kind(self):
         """The type of the parameter: integer, float, string,
         enum or special.
         This can be used to convert the value to the correct
         type in e.g. get_value."""
 
-        return self._data["kind"]
+        return self._data['kind']
 
     @kind.setter
     def kind(self, value):
-        if value not in ("integer", "float", "string"):
+        if value not in ('integer', 'float', 'string'):
             raise RuntimeError(
                 "The 'kind' must be 'integer', 'float', or "
                 "'string', not '{}'".format(value)
             )
-        self._data["kind"] = value
+        self._data['kind'] = value
 
     @property
     def units(self):
         """The units, as a string. These need to be compatible with
         pint"""
-        if "units" not in self._data:
-            self._data["units"] = self._data["default_units"]
+        if 'units' not in self._data:
+            self._data['units'] = self._data['default_units']
 
-        if self._data["units"] is None:
-            return self["default_units"]
+        if self._data['units'] is None:
+            return self['default_units']
 
-        return self._data["units"]
+        return self._data['units']
 
     @units.setter
     def units(self, value):
+
         logger.debug("units: value = '{}'".format(value))
 
-        if value == "":
+        if value == '':
             value = None
         if value is None:
             self.dimensionality = None
         else:
             tmp = ureg(value)
             logger.debug("   tmp = '{}'".format(tmp))
             if self.dimensionality is None:
                 self.dimensionality = tmp.dimensionality
 
-            logger.debug("   dimensionality = '{}'".format(self.dimensionality))
+            logger.debug(
+                "   dimensionality = '{}'".format(self.dimensionality)
+            )
 
             if tmp.dimensionality != self.dimensionality:
                 raise RuntimeError(
                     (
                         "Units '{}' have a different dimensionality than "
                         "the parameters: '{}' != '{}'"
                     ).format(value, tmp.dimensionality, self.dimensionality)
                 )
-        self._data["units"] = value
+        self._data['units'] = value
 
     @property
     def default_units(self):
         """The default units, as a string. These need to be compatible with
         pint"""
-        return self._data["default_units"]
+        return self._data['default_units']
 
     @default_units.setter
     def default_units(self, value):
-        if value == "":
+        if value == '':
             value = None
         if value is None:
             self.dimensionality = None
         else:
             tmp = ureg(value)
             if self.dimensionality is None:
                 self.dimensionality = tmp.dimensionality
@@ -246,127 +246,126 @@
                 raise RuntimeError(
                     (
                         "The default units '{}' have a different "
                         "dimensionality than the parameters: "
                         "'{}' != '{}'"
                     ).format(value, tmp.dimensionality, self.dimensionality)
                 )
-        self._data["default_units"] = value
+        self._data['default_units'] = value
 
     @property
     def enumeration(self):
         """The possible values for an enumerated type."""
-        return self._data["enumeration"]
+        return self._data['enumeration']
 
     @property
     def format_string(self):
         """The format string for the value"""
-        return self._data["format_string"]
+        return self._data['format_string']
 
     @format_string.setter
     def format_string(self, value):
-        self._data["format_string"] = value
+        self._data['format_string'] = value
 
     @property
     def description(self):
         """Short description of this parameter, preferable just a
         few words"""
-        return self._data["description"]
+        return self._data['description']
 
     @description.setter
     def description(self, value):
-        self._data["description"] = value
+        self._data['description'] = value
 
     @property
     def help_text(self):
         """A longer description of this parameter that is suitable
         for e.g. help text."""
-        return self._data["help_text"]
+        return self._data['help_text']
 
     @help_text.setter
     def help_text(self, value):
-        self._data["help_text"] = value
+        self._data['help_text'] = value
 
     @property
     def has_units(self):
         """Does this parameter have units associated?"""
         if self.dimensionality is None:
             return False
-        if self.dimensionality == "":
+        if self.dimensionality == '':
             return False
         return True
 
     @property
     def is_expr(self):
         """Is the current value a variable reference or
         expression?"""
         if isinstance(self.value, str) and len(self.value) > 0:
-            return self.value and self.value[0] == "$"
+            return self.value and self.value[0] == '$'
         else:
             return False
 
     def get(self, context=None, formatted=False, units=True):
         """Return the value evaluated in the given context"""
         if self.is_expr:
             if context is None:
                 global root_context
                 if root_context is None:
-                    raise RuntimeError("No context available")
+                    raise RuntimeError('No context available')
                 result = eval(self.value[1:], root_context)
             else:
                 result = eval(self.value[1:], context)
         else:
             result = self.value
 
         # If it is an enum, just return that.
         if self.enumeration is not None and result in self.enumeration:
-            if self.kind == "boolean":
+            if self.kind == 'boolean':
                 return bool(strtobool(result))
             else:
                 return result
 
         # convert to proper type
-        if self.kind == "integer":
+        if self.kind == 'integer':
             result = int(result)
-        elif self.kind == "float":
+        elif self.kind == 'float':
             result = float(result)
-        elif self.kind == "boolean":
+        elif self.kind == 'boolean':
             if isinstance(result, str):
                 result = bool(strtobool(result))
             elif not isinstance(result, bool):
                 result = bool(result)
-        elif self.kind == "list" or self.kind == "periodic table":
+        elif self.kind == 'list' or self.kind == 'periodic table':
             if not isinstance(result, list):
-                if isinstance(result, str) and len(result) > 0 and result[0] != "$":
+                if (
+                    isinstance(result, str) and len(result) > 0 and
+                    result[0] != '$'
+                ):
                     result = json.loads(result)
             return result
-        elif self.kind == "dictionary":
+        elif self.kind == 'dictionary':
             if not isinstance(result, dict):
                 result = json.loads(result)
             return result
 
         # format if requested
         if formatted:
-            fstring = self.format_string
-            if fstring is not None and fstring != "":
-                result = f"{result:{fstring}}"
-            if self.units is not None and self.units != "":
-                result += " " + self.units
+            result = self.format_string.format(result)
+            if self.units is not None and self.units != '':
+                result += ' ' + self.units
 
         # and run into pint quantity if requested
-        if units and self.units is not None and self.units != "":
+        if units and self.units is not None and self.units != '':
             result = Q_(result, self.units)
 
         return result
 
     def set(self, value):
         """Set the fields based on the type of value given"""
-        if self.kind == "special" or self.kind == "periodic table":
-            self.value = value
-        elif self.kind == "list":
+        if self.kind == 'special' or self.kind == 'periodic table':
             self.value = value
         elif isinstance(value, tuple) or isinstance(value, list):
             if len(value) == 1:
                 self.value = value[0]
             elif len(value) == 2:
                 self.value = value[0]
                 self.units = value[1]
@@ -377,100 +376,102 @@
                 )
         else:
             self.value = value
 
     def reset(self):
         """Reset to an empty state"""
         self._data = {
-            "default": None,
-            "kind": None,
-            "widget": None,
-            "default_units": None,
-            "enumeration": None,
-            "format_string": None,
-            "group": "",
-            "description": None,
-            "help_text": None,
+            'default': None,
+            'kind': None,
+            'widget': None,
+            'default_units': None,
+            'enumeration': None,
+            'format_string': None,
+            'group': '',
+            'description': None,
+            'help_text': None,
         }
         self.dimensionality = None
 
     def widget(self, frame, **kwargs):
         """Return a widget for handling the parameter"""
         # Will this keep the graphics isolated?
         import seamm_widgets as sw
 
-        logger.debug("Creating widget for {}".format(type(self)))
+        logger.debug('Creating widget for {}'.format(type(self)))
 
         if self._widget is not None:
-            logger.debug("   Destroying existing widget.")
+            logger.debug('   Destroying existing widget.')
             try:
                 self._widget.destroy()
             except Exception:
                 pass
 
-        labeltext = kwargs.pop("labeltext", self.description)
+        labeltext = kwargs.pop('labeltext', self.description)
 
-        if self.kind == "special":
-            module_name, class_name = self["widget"].split(".")
+        if self.kind == 'special':
+            module_name, class_name = self['widget'].split('.')
             mdl = importlib.import_module(module_name)
             cls = getattr(mdl, class_name)
             w = cls(frame, labeltext=labeltext, **kwargs)
             w.set(self.value)
-        elif self.kind == "periodic table":
+        elif self.kind == 'periodic table':
             w = sw.PeriodicTable(frame, **kwargs)
             w.set(self.value)
         elif self.enumeration is not None:
             if len(self.enumeration) > 0:
                 width = max(len(x) for x in self.enumeration)
                 if width < 10:
                     width = 10
             else:
                 width = 10
             if self.dimensionality is None:
-                logger.debug("    making LabeledCombobox")
+                logger.debug('    making LabeledCombobox')
                 w = sw.LabeledCombobox(
                     frame,
                     labeltext=labeltext,
                     values=self.enumeration,
                     width=width,
-                    **kwargs,
+                    **kwargs
                 )
                 w.set(self.value)
             else:
-                logger.debug("   making UnitCombobox")
+                logger.debug('   making UnitCombobox')
                 w = sw.UnitCombobox(
                     frame,
                     labeltext=labeltext,
                     values=self.enumeration,
                     width=width,
-                    **kwargs,
+                    **kwargs
                 )
                 w.set(self.value, self.units)
         else:
             if self.dimensionality is None:
-                logger.debug("   making LabeledEntry")
+                logger.debug('   making LabeledEntry')
                 w = sw.LabeledEntry(frame, labeltext=labeltext, **kwargs)
                 w.set(self.value)
             else:
-                logger.debug("   making UnitEntry")
+                logger.debug('   making UnitEntry')
                 w = sw.UnitEntry(frame, labeltext=labeltext, **kwargs)
                 w.set(self.value, self.units)
 
         self._widget = w
 
-        logger.debug("   returning {}".format(w))
+        logger.debug('   returning {}'.format(w))
         return w
 
     def set_from_widget(self):
-        """Set the value from the widget, ignoring if there is no widget."""
+        """Set the value from the widget, ignoring if there is no widget.
+        """
         if self._widget is not None:
             self.set(self._widget.get())
 
     def reset_widget(self):
-        """Reset the values in the widget, if it has been created."""
+        """Reset the values in the widget, if it has been created.
+        """
         if self._widget is not None:
             if self.dimensionality is None:
                 self._widget.set(self.value)
             else:
                 self._widget.set(self.value, self.units)
 
     def to_dict(self):
@@ -478,87 +479,93 @@
         result = dict()
         # if self['kind'] == 'list':
         #     result['value'] = json.dumps(self.value)
         # elif self['kind'] == 'dict':
         #     result['value'] = json.dumps(self.value)
         # else:
         #     result['value'] = self.value
-        result["value"] = self.value
-        result["units"] = self.units
+        result['value'] = self.value
+        result['units'] = self.units
         return result
 
     def update(self, data):
         """Update values from a dict
 
         This assumes that the static data such as 'kind' and
         'default' has been created already.
         """
 
-        logger.debug("Parameter.update....")
+        logger.debug('Parameter.update....')
         for key, value in data.items():
-            logger.debug("{:>10s} {}".format(key, value))
-            if key in ("value", "default"):
+            logger.debug('{:>10s} {}'.format(key, value))
+            if key in ('value', 'default'):
                 # if self['kind'] in ('list', 'dictionary'):
                 #     self._data[key] = json.loads(value)
                 # else:
                 self._data[key] = value
-            elif key == "units":
+            elif key == 'units':
                 self._data[key] = value
             elif key not in self:
                 raise RuntimeError(
-                    "update: dictionary not compatible with Parameters,"
+                    'update: dictionary not compatible with Parameters,'
                     " which do not have an attribute '{}'".format(key)
                 )
             else:
                 self._data[key] = value
 
         # Update the dimensionality if needed
-        if "units" in self._data:
-            self.units = self._data["units"]
-        if "default_units" in self._data:
-            self.default_units = self._data["default_units"]
+        if 'units' in self._data:
+            self.units = self._data['units']
+        if 'default_units' in self._data:
+            self.default_units = self._data['default_units']
 
     def debug_print(self):
-        logger.debug("\nParameter instance:\n{}".format(pprint.pformat(self._data)))
+        logger.debug(
+            '\nParameter instance:\n{}'.format(pprint.pformat(self._data))
+        )
 
 
 class Parameters(collections.abc.MutableMapping):
     """A dict-like container for parameters"""
 
     def __init__(self, defaults={}, data=None):
         """Create an instance, optionally from a dict"""
 
-        logger.debug("\nParameters.__init__")
+        logger.debug('\nParameters.__init__')
         logger.debug(pprint.pformat(defaults))
 
         self.defaults = defaults
-        logger.debug("\ndefaults:\n{}".format(pprint.pformat(defaults)))
+        logger.debug('\ndefaults:\n{}'.format(pprint.pformat(defaults)))
 
         self._data = {}
 
         self.initialize()
 
         if logger.isEnabledFor(logging.DEBUG):
             logger.debug("\nafter defaults:")
             for key, value in self.items():
-                logger.debug("  {}: {}".format(key, pprint.pformat(value._data)))
+                logger.debug(
+                    '  {}: {}'.format(key, pprint.pformat(value._data))
+                )
 
         if data:
             if isinstance(data, dict):
                 self.update(data)
 
                 if logger.isEnabledFor(logging.DEBUG):
                     logger.debug("\nafter data:")
                     for key, value in self.items():
                         logger.debug(
-                            "  {}: {}".format(key, pprint.pformat(value._data))
+                            '  {}: {}'.format(
+                                key, pprint.pformat(value._data)
+                            )
                         )
             else:
                 raise RuntimeError(
-                    "A Parameters object can be initialized with a dict object"
+                    'A Parameters object can be initialized with a dict object'
                 )
 
     def __getitem__(self, key):
         """Allow [] access to the dictionary!"""
         return self._data[key]
 
     def __setitem__(self, key, value):
@@ -607,19 +614,22 @@
         """
         data = {}
         for key in self:
             try:
                 data[key] = self[key].to_dict()
             except:  # noqa: E722
                 logger.critical(
-                    ("An error occurred in Parameters.to_dict " "with key '{}'").format(
-                        key
-                    )
+                    (
+                        "An error occurred in Parameters.to_dict "
+                        "with key '{}'"
+                    ).format(key)
+                )
+                logger.critical(
+                    ("The type of the key is '{}'").format(type(self[key]))
                 )
-                logger.critical(("The type of the key is '{}'").format(type(self[key])))
                 raise
         return data
 
     def from_dict(self, data):
         """Recreate the object from a dictionary"""
         self._data = dict()
         # Put back in all the constant data
@@ -641,37 +651,43 @@
 
         data = {}
         for key in self:
             try:
                 data[key] = str(self[key])
             except Exception as e:
                 logger.warning("Cannot format '{}': {}".format(key, str(e)))
-                data[key] = "#err#"
+                data[key] = '#err#'
 
         return data
 
-    def current_values_to_dict(self, context=None, formatted=False, units=True):
+    def current_values_to_dict(
+        self, context=None, formatted=False, units=True
+    ):
         """Return the current values of the parameters, resolving
         any expressions, etc. in the given context or the root
         context is none is given."""
 
         data = {}
         for key in self:
-            data[key] = self[key].get(context=context, formatted=formatted, units=units)
+            data[key] = self[key].get(
+                context=context, formatted=formatted, units=units
+            )
 
         return data
 
     def set_from_widgets(self):
         """Convenience function to set the parameters from their widgets."""
         for key in self:
             self[key].set_from_widget()
 
     def reset_widgets(self):
         """Convenience function to reset the widgets to the current value."""
         for key in self:
             try:
                 self[key].reset_widget()
             except ValueError as e:
-                logger.warning("Error resetting widget for {}: {}".format(key, str(e)))
+                logger.warning(
+                    'Error resetting widget for {}: {}'.format(key, str(e))
+                )
                 raise
             except Exception:
                 raise
```

### Comparing `seamm-2023.4.8/seamm/plugin_manager.py` & `seamm-220.8.3/seamm/plugin_manager.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 # -*- coding: utf-8 -*-
 
 import logging
 import pprint
 import stevedore
-
 """A plugin manager based on Stevedore"""
 
 logger = logging.getLogger(__name__)
 
 
 class PluginManager(object):
+
     def __init__(self, namespace):
-        logger.info("Initializing extensions for {}".format(namespace))
+        logger.info('Initializing extensions for {}'.format(namespace))
 
         self.namespace = namespace
         self.manager = stevedore.extension.ExtensionManager(
             namespace=self.namespace,
             invoke_on_load=True,
             on_load_failure_callback=self.load_failure,
         )
@@ -23,33 +23,34 @@
 
         logger.info(
             "Found {:d} extensions in '{:s}': {}".format(
                 len(self.manager.names()), self.namespace, self.manager.names()
             )
         )
 
-        logger.debug("Processing extensions")
+        logger.debug('Processing extensions')
 
         for name in self.manager.names():
-            logger.debug("    extension name: {}".format(name))
+            logger.debug('    extension name: {}'.format(name))
             extension = self.manager[name].obj
-            logger.debug("  extension object: {}".format(extension))
+            logger.debug('  extension object: {}'.format(extension))
             data = extension.description()
-            logger.debug("    extension data:")
+            logger.debug('    extension data:')
             logger.debug(pprint.pformat(data))
-            logger.debug("")
-            group = data["group"]
+            logger.debug('')
+            group = data['group']
             if group in self._plugins:
                 self._plugins[group].append(name)
             else:
                 self._plugins[group] = [name]
 
     def load_failure(self, mgr, ep, err):
-        """Called when the extension manager can't load an extension"""
-        logger.warning("Could not load %r: %s", ep.name, err)
+        """Called when the extension manager can't load an extension
+        """
+        logger.warning('Could not load %r: %s', ep.name, err)
 
     def get(self, name):
         return self.manager[name].obj
 
     def groups(self):
         return sorted(list(self._plugins.keys()))
```

### Comparing `seamm-2023.4.8/seamm/split_node.py` & `seamm-220.8.3/seamm/split_node.py`

 * *Files 10% similar despite different names*

```diff
@@ -5,48 +5,53 @@
 import seamm
 import seamm_util.printing as printing
 from seamm_util.printing import FormattedText as __
 import logging
 
 logger = logging.getLogger(__name__)
 job = printing.getPrinter()
-printer = printing.getPrinter("split")
+printer = printing.getPrinter('split')
 
 
 class Split(seamm.Node):
+
     def __init__(self, flowchart=None, extension=None):
         """Initialize a node for splitting the flow apart
 
         Keyword arguments:
         """
-        logger.debug("Constructing split node {}".format(self))
-        super().__init__(flowchart=flowchart, title="Split", extension=extension)
+        logger.debug('Constructing split node {}'.format(self))
+        super().__init__(
+            flowchart=flowchart, title='Split', extension=extension
+        )
 
     @property
     def version(self):
-        """The semantic version of this module."""
+        """The semantic version of this module.
+        """
         return seamm.__version__
 
     @property
     def git_revision(self):
-        """The git version of this module."""
+        """The git version of this module.
+        """
         return seamm.__git_revision__
 
     def description_text(self, P=None):
         """Return a short description of this step.
 
         Return a nicely formatted string describing what this step will
             do.
 
         Keyword arguments:
             P: a dictionary of parameter values, which may be variables
                 or final values. If None, then the parameters values will
                 be used as is.
-        """
+            """
 
         # if not P:
         #     P = self.parameters.values_to_dict()
 
-        text = ""
-        text += "Split into several threads of execution"
+        text = ''
+        text += 'Split into several threads of execution'
 
-        return self.header + "\n" + __(text, indent=4 * " ").__str__()
+        return self.header + '\n' + __(text, indent=4 * ' ').__str__()
```

### Comparing `seamm-2023.4.8/seamm/templates/band_structure.html_template` & `seamm-220.8.3/seamm/templates/line.html_template`

 * *Files 17% similar despite different names*

```diff
@@ -40,61 +40,41 @@
 			    {%- if 'x' in trace %}
 			    "x": {{ trace.x|jsonify }},
 			    {%- else %}
 			    "x0": {{ trace.x0 }},
 			    "dx": {{ trace.dx }},
 			    {%- endif %}
 			    "xaxis": "{{ trace.xaxis }}",
-			    {%- if 'y' in trace %}
 			    "y": {{ trace.y|jsonify }},
-			    {%- else %}
-			    "y0": {{ trace.y0 }},
-			    "dy": {{ trace.dy }},
-			    {%- endif %}
 			    "yaxis": "{{ trace.yaxis }}"
 			    {%- if loop.last %}
 			}
 			{%- else %}
 			},
 		    {%- endif %}
 		    {%- endfor %}
                     ],
                     {
-			"hovermode": "closest",
+			"hovermode": "x",
 			"legend": {
 			    "title": "",
 			    "tracegroupgap": 0
 			},
 			"title": {
 			    "x": 0.5,
 			    "text": "{{ title }}",
 			    "xanchor": "center"
 			},
 			{%- for axis in axes %}    
 			"{{ axis.name }}": {
 			    "anchor": "{{ axis.anchor }}",
-			    {%- if 'autorange' in axis %}
-			    "autorange": "{{ axis.autorange }}",
-			    {%- endif %}
 			    "domain": [
 				{{ axis.start }},
 				{{ axis.stop }}
 			    ],
-			    {%- if 'tickmode' in axis %}
-			    "tickmode": "{{ axis.tickmode }}",
-			    {%- endif %}
-			    {%- if 'ticklabelposition' in axis %}
-			    "ticklabelposition": "{{ axis.ticklabelposition }}",
-			    {%- endif %}
-			    {%- if 'tickvals' in axis %}
-			    "tickvals": {{ axis.tickvals|jsonify }},
-			    {%- endif %}
-			    {%- if 'ticktext' in axis %}
-			    "ticktext": {{ axis.ticktext|jsonify }},
-			    {%- endif %}
 			    "title": {
 				"text": "{{ axis.label }}"
 			    }
 			{%- if loop.last %}
 			}
 			{%- else %}
 			},
```

### Comparing `seamm-2023.4.8/seamm/templates/line.graph_template` & `seamm-220.8.3/seamm/templates/line.graph_template`

 * *Files identical despite different names*

### Comparing `seamm-2023.4.8/seamm/tk_edge.py` & `seamm-220.8.3/seamm/tk_edge.py`

 * *Files 22% similar despite different names*

```diff
@@ -21,99 +21,99 @@
     str_to_object = weakref.WeakValueDictionary()
 
     def __init__(
         self,
         graph,
         node1,
         node2,
-        edge_type="execution",
-        edge_subtype="next",
+        edge_type='execution',
+        edge_subtype='next',
         canvas=None,
-        anchor1="s",
-        anchor2="n",
+        anchor1='s',
+        anchor2='n',
         coords=None,
         **kwargs
     ):
         """Initialize the edge, ensuring that it is
         in the graph.
 
         Keyword arguments:
         """
         self._data = []
-        logger.debug("Creating TkEdge {}".format(self))
-        logger.debug("\tnode1 = {}".format(node1))
-        logger.debug("\tnode2 = {}".format(node2))
+        logger.debug('Creating TkEdge {}'.format(self))
+        logger.debug('\tnode1 = {}'.format(node1))
+        logger.debug('\tnode2 = {}'.format(node2))
 
         # Initialize the parent class
-        super().__init__(graph, node1, node2, edge_type, edge_subtype, **kwargs)
+        super().__init__(
+            graph, node1, node2, edge_type, edge_subtype, **kwargs
+        )
 
-        self._data["canvas"] = canvas
+        self._data['canvas'] = canvas
         self.anchor1 = anchor1
         self.anchor2 = anchor2
         if coords is None:
             x0, y0 = self.node1.anchor_point(self.anchor1)
             x1, y1 = self.node2.anchor_point(self.anchor2)
             self.coords = [x0, y0, x1, y1]
         else:
             self.coords = coords
 
         # Remember the object so can get from tags on the canvas
         TkEdge.str_to_object[str(id(self))] = self
 
         # Arrange that the graphics are deleted when we are
-        self._finalizer = weakref.finalize(self, self.canvas.delete, self.tag())
+        self._finalizer = weakref.finalize(
+            self, self.canvas.delete, self.tag()
+        )
         self._finalizer.atexit = False
 
-    def __eq__(self, other):
-        """Return a boolean if this object is equal to another"""
-        return super().__eq__(other)
-
     @property
     def canvas(self):
-        return self._data["canvas"]
+        return self._data['canvas']
 
     @property
     def anchor1(self):
-        return self._data["anchor1"]
+        return self._data['anchor1']
 
     @anchor1.setter
     def anchor1(self, value):
-        self._data["anchor1"] = value
+        self._data['anchor1'] = value
 
     @property
     def anchor2(self):
-        return self._data["anchor2"]
+        return self._data['anchor2']
 
     @anchor2.setter
     def anchor2(self, value):
-        self._data["anchor2"] = value
+        self._data['anchor2'] = value
 
     @property
     def coords(self):
-        return self._data["coords"]
+        return self._data['coords']
 
     @coords.setter
     def coords(self, value):
-        self._data["coords"] = value
+        self._data['coords'] = value
 
     @property
     def has_label(self):
-        return "label_id" in self._data
+        return 'label_id' in self._data
 
     @property
     def label_id(self):
-        return self._data["label_id"]
+        return self._data['label_id']
 
     @property
     def label_bg_id(self):
-        return self._data["label_bg_id"]
+        return self._data['label_bg_id']
 
     def tag(self):
         """Return a string tag for self"""
-        return "edge=" + str(id(self))
+        return 'edge=' + str(id(self))
 
     def draw(self):
         """Draw the arrow for this edge"""
         self.move()
 
     def move(self):
         """Redraw the arrow when the nodes have moved"""
@@ -122,55 +122,55 @@
         x1, y1 = self.node2.anchor_point(self.anchor2)
         self.coords[0] = x0
         self.coords[1] = y0
         self.coords[-2] = x1
         self.coords[-1] = y1
 
         # the arrow
-        self.canvas.delete(self.tag() + "&& type=arrow")
+        self.canvas.delete(self.tag() + '&& type=arrow')
         arrow_id = self.canvas.create_line(
-            self.coords, arrow=tk.LAST, tags=[self.tag(), "type=arrow"]
+            self.coords, arrow=tk.LAST, tags=[self.tag(), 'type=arrow']
         )
-        self._data["arrow_id"] = arrow_id
+        self._data['arrow_id'] = arrow_id
 
         # and the label
         if self.edge_subtype != "next":
-            self.canvas.delete(self.tag() + "&& type=label")
+            self.canvas.delete(self.tag() + '&& type=label')
             text = self.canvas.create_text(
                 self.label_position(x0, y0, x1, y1),
                 text=self.edge_subtype,
-                font=font.Font(family="Helvetica", size=8),
-                tags=[self.tag(), "type=label"],
+                font=font.Font(family='Helvetica', size=8),
+                tags=[self.tag(), 'type=label']
             )
-            self._data["label_id"] = text
-            self.canvas.delete(self.tag() + "&& type=label_bg")
+            self._data['label_id'] = text
+            self.canvas.delete(self.tag() + '&& type=label_bg')
             bg = self.canvas.create_rectangle(
                 self.canvas.bbox(text),
                 outline="white",
                 fill="white",
-                tags=[self.tag(), "type=label_bg"],
+                tags=[self.tag(), 'type=label_bg']
             )
-            self._data["label_bg_id"] = bg
+            self._data['label_bg_id'] = bg
             self.canvas.tag_lower(bg, text)
 
     def label_position(self, x0, y0, x1, y1, offset=15):
         """Work out the position for the label on an edge"""
         dx = x1 - x0
         dy = y1 - y0
         length = math.sqrt(dx * dx + dy * dy)
         if length < 2 * offset:
             offset = int(length / 2)
         xy = [
             x0 if dx == 0.0 else x0 + dx / length * offset,
-            y0 if dy == 0.0 else y0 + dy / length * offset,
+            y0 if dy == 0.0 else y0 + dy / length * offset
         ]
         return xy
 
     def undraw(self):
         """Remove any graphics"""
         self.canvas.delete(self.tag())
-        if "arrow_id" in self._data:
-            del self._data["arrow_id"]
-        if "label_id" in self._data:
-            del self._data["label_id"]
-        if "label_bg_id" in self._data:
-            del self._data["label_bg_id"]
+        if 'arrow_id' in self._data:
+            del self._data['arrow_id']
+        if 'label_id' in self._data:
+            del self._data['label_id']
+        if 'label_bg_id' in self._data:
+            del self._data['label_bg_id']
```

### Comparing `seamm-2023.4.8/seamm/tk_flowchart.py` & `seamm-220.8.3/seamm/tk_flowchart.py`

 * *Files 8% similar despite different names*

```diff
@@ -39,40 +39,40 @@
 same node as the tail/head for head/tail!). If the arrow is dropped
 anywhere else it just snaps back to its original place.
 """
 
 import copy
 import logging
 import math
+from PIL import ImageTk, Image
 import pkg_resources
 import pprint  # nopep8
 import sys
 import tkinter as tk
 import tkinter.filedialog as tk_filedialog
 import tkinter.ttk as ttk
 
-from PIL import ImageTk, Image
-
 import seamm
-from .tk_open import TkOpen
-from .tk_publish import TkPublish
 
 logger = logging.getLogger(__name__)
 
 
 def grey(value):
     return 255 - (255 - value) * 0.1
 
 
 class TkFlowchart(object):
-    def __init__(self, master=None, flowchart=None, namespace="org.molssi.seamm.tk"):
-        """Initialize a Flowchart object
+
+    def __init__(
+        self, master=None, flowchart=None, namespace='org.molssi.seamm.tk'
+    ):
+        '''Initialize a Flowchart object
 
         Keyword arguments:
-        """
+        '''
 
         self.toplevel = None
         self.master = master
         self._flowchart = flowchart
         self.filename = None
         self._stack = []
 
@@ -105,15 +105,17 @@
 
         # On the left put the tree of nodes
         self.tree = ttk.Treeview(self.pw)
         self.pw.add(self.tree)
         for group in self.plugin_manager.groups():
             self.tree.insert("", "end", group, text=group)
             for plugin in self.plugin_manager.plugins(group):
-                self.tree.insert(group, "end", plugin, text=plugin, tags="node")
+                self.tree.insert(
+                    group, "end", plugin, text=plugin, tags="node"
+                )
         self.tree.tag_bind(
             "node", sequence="<ButtonPress-1>", callback=self.create_node
         )
 
         # and the main canvas with scrollbars next to the right
         self.canvas_frame = ttk.Frame(self.pw)
 
@@ -128,28 +130,28 @@
 
         self.canvas = tk.Canvas(
             self.canvas_frame,
             width=self.canvas_width,
             height=self.canvas_height,
             xscrollcommand=self.xscrollbar.set,
             yscrollcommand=self.yscrollbar.set,
-            scrollregion=(0, 0, 2000, 2000),
+            scrollregion=(0, 0, 2000, 2000)
         )
         self.canvas.grid(row=0, column=0, sticky=tk.NSEW)
         self.xscrollbar.config(command=self.xview)
         self.yscrollbar.config(command=self.yview)
 
         self.pw.add(self.canvas_frame)
 
         # Set up scrolling on the canvas with the mouse scrollwheel or similar
-        self.canvas.bind("<Enter>", self._bound_to_mousewheel)
-        self.canvas.bind("<Leave>", self._unbound_to_mousewheel)
+        self.canvas.bind('<Enter>', self._bound_to_mousewheel)
+        self.canvas.bind('<Leave>', self._unbound_to_mousewheel)
 
         # background image
-        filepath = pkg_resources.resource_filename(__name__, "data/SEAMM.png")
+        filepath = pkg_resources.resource_filename(__name__, 'data/SEAMM.png')
         logger.info(filepath)
 
         self.image = Image.open(filepath)
         self.prepared_image = Image.eval(self.image.convert("RGB"), grey)
         w, h = self.image.size
         r_w = self.canvas_width / w
         r_h = self.canvas_height / h
@@ -160,31 +162,31 @@
         self.photo = ImageTk.PhotoImage(self.working_image)
         # self.background = self.canvas.create_image(
         #     self.canvas_width / 2,
         #     self.canvas_height / 2,
         #     image=self.photo,
         #     anchor='center')
         self.background = self.canvas.create_image(
-            0, 0, image=self.photo, anchor="center"
+            0, 0, image=self.photo, anchor='center'
         )
 
         # The gui partner for the start node...
         self.create_start_node()
 
         # Set up the bindings
-        self.canvas.bind("<Configure>", self.canvas_configure)
-        self.canvas.bind("<Motion>", self.mouse_motion)
-        self.canvas.bind("<ButtonPress-1>", self.click)
-        self.canvas.bind("<Double-ButtonPress-1>", self.double_click)
-        if sys.platform.startswith("darwin"):
-            self.canvas.bind("<ButtonPress-2>", self.right_click)
+        self.canvas.bind('<Configure>', self.canvas_configure)
+        self.canvas.bind('<Motion>', self.mouse_motion)
+        self.canvas.bind('<ButtonPress-1>', self.click)
+        self.canvas.bind('<Double-ButtonPress-1>', self.double_click)
+        if sys.platform.startswith('darwin'):
+            self.canvas.bind('<ButtonPress-2>', self.right_click)
         else:
-            self.canvas.bind("<ButtonPress-3>", self.right_click)
+            self.canvas.bind('<ButtonPress-3>', self.right_click)
 
-        logger.debug("Finished initializing tk_flowchart")
+        logger.debug('Finished initializing tk_flowchart')
 
     def __iter__(self):
         return self.graph.__iter__()
 
     @property
     def flowchart(self):
         """The flowchart, which holds the nodes"""
@@ -217,150 +219,142 @@
         if isinstance(tag, int):
             tag = str(tag)
         for node in self:
             if str(node.uuid) == tag:
                 return node
         return None
 
-    def last_node(self, tk_node="1"):
+    def last_node(self, tk_node='1'):
         """Find the last node walking down the main execution path
         from the given node, which defaults to the start node"""
 
-        logger.debug("Finding last node")
+        logger.debug('Finding last node')
         # Handle loops!
         for node in self:
             node.node.visited = False
             logger.debug(
-                "   reset visited {} {} = {}".format(
+                '   reset visited {} {} = {}'.format(
                     node.node.visited, node.title, node
                 )
             )
 
         return self.last_node_helper(tk_node)
 
     def last_node_helper(self, tk_node):
         """Helper routine to handle the recursion"""
 
         # get the node to start the traversal
         if isinstance(tk_node, str):
             tk_node = self.get_node(tk_node)
 
         logger.debug(
-            "   last tk_node helper: {} {} = {}".format(
+            '   last tk_node helper: {} {} = {}'.format(
                 tk_node.node.visited, tk_node.title, tk_node
             )
         )
 
         tk_node.node.visited = True
         next_tk_node = None
-        for edge in self.graph.edges(tk_node, direction="out"):
+        for edge in self.graph.edges(tk_node, direction='out'):
             if edge.edge_type == "execution":
+
                 if edge.node2.node.visited:
                     logger.debug(
-                        "\ttk_node {} {} has been visited".format(
+                        '\ttk_node {} {} has been visited'.format(
                             edge.node2.title, edge.node2
                         )
                     )
                     next_tk_node = edge.node2
                 else:
                     logger.debug(
-                        "\trecursing to tk_node {} {}".format(
+                        '\trecursing to tk_node {} {}'.format(
                             edge.node2.title, edge.node2
                         )
                     )
                     return self.last_node_helper(edge.node2)
 
         if next_tk_node is not None:
             tk_node = next_tk_node
             logger.debug(
-                "\tchecking visited tk_node {} {} for new nodes".format(
+                '\tchecking visited tk_node {} {} for new nodes'.format(
                     tk_node.title, tk_node
                 )
             )
             if tk_node.node.extension == "Join":
-                logger.debug("\t  tk_node is a join node, so look at next")
-                for edge in self.graph.edges(tk_node, direction="out"):
+                logger.debug('\t  tk_node is a join node, so look at next')
+                for edge in self.graph.edges(tk_node, direction='out'):
                     if edge.edge_type == "execution":
                         logger.debug(
-                            "\ttk_node after join node is {} {}".format(
+                            '\ttk_node after join node is {} {}'.format(
                                 edge.node2.title, edge.node2
                             )
                         )
                         tk_node = edge.node2
 
-            for edge in self.graph.edges(tk_node, direction="out"):
+            for edge in self.graph.edges(tk_node, direction='out'):
                 if edge.edge_type == "execution":
                     if edge.node2.node.visited:
                         logger.debug(
-                            "\tnode {} {} has been visited".format(
+                            '\tnode {} {} has been visited'.format(
                                 edge.node2.title, edge.node2
                             )
                         )
                     else:
                         logger.debug(
-                            "\trecursing to tk_node {} {}".format(
+                            '\trecursing to tk_node {} {}'.format(
                                 edge.node2.title, edge.node2
                             )
                         )
                         return self.last_node_helper(edge.node2)
 
-        logger.debug("\treturning {} {}".format(tk_node.title, tk_node))
+        logger.debug('\treturning {} {}'.format(tk_node.title, tk_node))
         return tk_node
 
-    def add_edge(self, u, v, edge_type="execution", edge_subtype="next", **kwargs):
+    def add_edge(
+        self, u, v, edge_type='execution', edge_subtype='next', **kwargs
+    ):
         edge = self.graph.add_edge(
             u,
             v,
             edge_type,
             edge_subtype,
             edge_class=seamm.TkEdge,
             canvas=self.canvas,
-            **kwargs,
+            **kwargs
         )
         edge.draw()
         return edge
 
-    def edges(self, node=None, direction="both"):
+    def edges(self, node=None, direction='both'):
         return self.graph.edges(node, direction)
 
     def new_file(self, event=None):
         self.filename = None
         self.clear()
-        # Reset the metadata
-        self.flowchart.reset_metadata()
 
     def help(self, event=None):
         print("Help!!!!")
 
     def debug(self, event):
         print(event)
 
     def open_file(self, event=None):
-        filename = tk_filedialog.askopenfilename(defaultextension=".flow")
-        if filename == "":
+        filename = tk_filedialog.askopenfilename(defaultextension='.flow')
+        if filename == '':
             return
         self.open(filename)
 
     def open(self, filename):
         if isinstance(filename, list):
             filename = filename[0]
 
         self.flowchart.read(filename)
         self.from_flowchart()
         self.filename = filename
 
-    def flowchart_search(self, event=None):
-        """Open a flowchart from Zenodo."""
-        opener = TkOpen(self.toplevel)
-        data = opener.open()
-        if data is not None:
-            self.flowchart.from_text(data)
-            self.filename = None
-            self.from_flowchart()
-
     def clear(self, all=False):
         """Clear our graphics"""
         for item in self.canvas.find_all():
             if item != self.background:
                 self.canvas.delete(item)
         # and the graph
         self.graph.clear()
@@ -369,68 +363,56 @@
         if not all:
             self.create_start_node()
             self.draw()
 
     def create_start_node(self):
         """Create the start node"""
         # Check if the start node exists
-        start_node = self.flowchart.get_node("1")
+        start_node = self.flowchart.get_node('1')
         if start_node is None:
             start_node = seamm.StartNode()
 
         tk_start_node = seamm.TkStartNode(
             tk_flowchart=self,
             canvas=self.canvas,
             node=start_node,
             x=self.grid_x / 2,
-            y=self.grid_y / 2,
+            y=self.grid_y / 2
         )
 
         self.graph.add_node(tk_start_node)
         logger.debug(
-            "Created start node {} at {}, {}".format(
+            'Created start node {} at {}, {}'.format(
                 tk_start_node, start_node.x, start_node.y
             )
         )
         return tk_start_node
 
-    def properties(self):
-        """Get and set the properties of the flowchart."""
-        start_node = self.get_node("1")
-        start_node.edit()
-
-    def publish(self, event=None):
-        """Publish the flowchart to a repository such as Zenodo."""
-        self.update_flowchart()
-
-        publisher = TkPublish(self)
-        publisher.edit()
-
     def save(self, event=None):
         if self.filename is None:
             self.save_file()
         else:
             self.update_flowchart()
             self.flowchart.write(self.filename)
             self.flowchart.clear()
 
     def save_file(self, event=None):
-        filename = tk_filedialog.asksaveasfilename(defaultextension=".flow")
-        if filename != "":
+        filename = tk_filedialog.asksaveasfilename(defaultextension='.flow')
+        if filename != '':
             # suffixes = pathlib.Path(filename).suffixes
             # if len(suffixes) == 0 or '.flow' not in suffixes:
             #     filename = filename + '.flow'
             self.filename = filename
             self.save()
 
-    def about(self, text="In about"):
+    def about(self, text='In about'):
         print(text)
 
     def preferences(self):
-        print("In preferences")
+        print('In preferences')
 
     def draw(self):
         for tk_node in self:
             tk_node.draw()
 
     def canvas_configure(self, event):
         """Redraw the background as the canvas changes size
@@ -461,168 +443,169 @@
         factor = r_w if r_w < r_h else r_h
         w = int(factor * w)
         h = int(factor * h)
 
         self.canvas.itemconfigure(self.background, image=None)
         # self.canvas.coords(self.background, cw / 2, ch / 2)
         self.canvas.coords(self.background, 0, 0)
-        del self.working_image
+        del (self.working_image)
         self.working_image = self.prepared_image.resize((w, h))
-        del self.photo
+        del (self.photo)
         self.photo = ImageTk.PhotoImage(self.working_image)
         # self.canvas.itemconfigure(
         #     self.background, image=self.photo, anchor='center')
-        self.canvas.itemconfigure(self.background, image=self.photo, anchor="nw")
+        self.canvas.itemconfigure(
+            self.background, image=self.photo, anchor='nw'
+        )
 
     def click(self, event):
         """Handle a left-click on the canvas by finding out what the
         mouse is on/in/near and doing the appropriate thing, such as
         selecting to preparing to move the item.
         """
 
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
         items = self.canvas.find_closest(cx, cy, self.halo)
         self.selection = []
         for item in items:
             tags = self.get_tags(item)
-            if "type" in tags and (
-                tags["type"] == "arrow_base" or tags["type"] == "arrow_head"
-            ):
-                arrow = int(tags["arrow"])
+            if 'type' in tags and \
+               (tags['type'] == 'arrow_base' or tags['type'] == 'arrow_head'):
+                arrow = int(tags['arrow'])
                 xys = self.canvas.coords(item)
                 x0 = xys[0]
                 y0 = xys[1]
                 x1 = xys[-2]
                 y1 = xys[-1]
                 self.data = self.get_tags(arrow)
-                self.data["arrow"] = arrow
+                self.data['arrow'] = arrow
                 self.data.update(self.get_tags(arrow))
-                self.data["x0"] = x0
-                self.data["y0"] = y0
-                self.data["x1"] = x1
-                self.data["y1"] = y1
+                self.data['x0'] = x0
+                self.data['y0'] = y0
+                self.data['x1'] = x1
+                self.data['y1'] = y1
                 self._x0 = cx
                 self._y0 = cy
 
-                logger.debug("self.data for dragging arrow head or base")
-                logger.debug("{}".format(self.data))
+                logger.debug('self.data for dragging arrow head or base')
+                logger.debug('{}'.format(self.data))
 
-                if tags["type"] == "arrow_base":
-                    self.data["arrow_base"] = item
-                    self.data["arrow_head"] = self.canvas.find_withtag(
-                        "type=arrow_head"
-                    )
-                    self.mouse_op = "drag arrow base"
-                    self.canvas.bind("<B1-Motion>", self.drag_arrow_base)
-                    self.canvas.bind("<ButtonRelease-1>", self.drop_arrow_base)
+                if tags['type'] == 'arrow_base':
+                    self.data['arrow_base'] = item
+                    self.data['arrow_head'] = \
+                        self.canvas.find_withtag('type=arrow_head')
+                    self.mouse_op = 'drag arrow base'
+                    self.canvas.bind('<B1-Motion>', self.drag_arrow_base)
+                    self.canvas.bind('<ButtonRelease-1>', self.drop_arrow_base)
                 else:
-                    self.data["arrow_base"] = self.canvas.find_withtag(
-                        "type=arrow_base"
-                    )
-                    self.data["arrow_head"] = item
-                    self.mouse_op = "drag arrow head"
-                    self.canvas.bind("<B1-Motion>", self.drag_arrow_head)
-                    self.canvas.bind("<ButtonRelease-1>", self.drop_arrow_head)
-
-            if "node" in tags:
-                node = tags["node"]
-                if tags["type"] == "active_anchor":
+                    self.data['arrow_base'] = \
+                        self.canvas.find_withtag('type=arrow_base')
+                    self.data['arrow_head'] = item
+                    self.mouse_op = 'drag arrow head'
+                    self.canvas.bind('<B1-Motion>', self.drag_arrow_head)
+                    self.canvas.bind('<ButtonRelease-1>', self.drop_arrow_head)
+
+            if 'node' in tags:
+                node = tags['node']
+                if tags['type'] == 'active_anchor':
                     # Connecting from an anchor to another node
-                    x, y = node.anchor_point(tags["anchor"])
-                    self.mouse_op = "Connect"
+                    x, y = node.anchor_point(tags['anchor'])
+                    self.mouse_op = 'Connect'
                     arrow = self.canvas.create_line(
-                        x, y, cx, cy, arrow=tk.LAST, tags="type=active_arrow"
+                        x, y, cx, cy, arrow=tk.LAST, tags='type=active_arrow'
                     )
-                    self.data = (node, tags["anchor"], x, y, arrow)
-                    self.canvas.bind("<B1-Motion>", self.drag_arrow)
-                    self.canvas.bind("<ButtonRelease-1>", self.drop_arrow)
+                    self.data = (node, tags['anchor'], x, y, arrow)
+                    self.canvas.bind('<B1-Motion>', self.drag_arrow)
+                    self.canvas.bind('<ButtonRelease-1>', self.drop_arrow)
                 else:
                     if node.is_inside(cx, cy, self.halo):
                         self.selection.append(node)
                         node.selected = True
                         self._x0 = cx
                         self._y0 = cy
-                        self.mouse_op = "Move"
-                        self.canvas.bind("<B1-Motion>", self.move)
-                        self.canvas.bind("<ButtonRelease-1>", self.end_move)
+                        self.mouse_op = 'Move'
+                        self.canvas.bind('<B1-Motion>', self.move)
+                        self.canvas.bind('<ButtonRelease-1>', self.end_move)
                     else:
                         node.selected = False
 
     def double_click(self, event):
         """Handle a double-click on the canvas by finding out what the
         mouse is on/in/near and doing the appropriate thing.
         """
 
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
         result = self.find_items(cx, cy)
         self.selection = []
         if result is None:
             # Handle a right-click out side anything
-            print("Double-click outside objects")
+            print('Double-click outside objects')
             return
 
-        if result[0] == "node":
+        if result[0] == 'node':
             node = result[1]
             if node.is_inside(cx, cy):
                 node.double_click(event)
                 return
 
-        if result[0] == "item":
+        if result[0] == 'item':
             item = result[1]
             tags = self.get_tags(item)
-            if "type" in tags and tags["type"] == "arrow":
+            if 'type' in tags and tags['type'] == 'arrow':
                 self.right_click_on_arrow(event, item, tags)
 
     def right_click(self, event):
         """Handle a right-click on the canvas by finding out what the
         mouse is on/in/near and doing the appropriate thing, such as
         posting an action menu
         """
 
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
         result = self.find_items(cx, cy)
         self.selection = []
         if result is None:
             # Handle a right-click out side anything
-            print("Right-click outside objects")
+            print('Right-click outside objects')
             return
 
-        if result[0] == "node":
+        if result[0] == 'node':
             node = result[1]
             if node.is_inside(cx, cy):
                 node.right_click(event)
                 return
 
-        if result[0] == "item":
+        if result[0] == 'item':
             item = result[1]
             tags = self.get_tags(item)
-            if "type" in tags and tags["type"] == "arrow":
+            if 'type' in tags and tags['type'] == 'arrow':
                 self.right_click_on_arrow(event, item, tags)
 
     def move(self, event):
-        """Move selected items"""
+        '''Move selected items
+        '''
 
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
         deltax = cx - self._x0
         deltay = cy - self._y0
 
         self._x0 = cx
         self._y0 = cy
 
         for item in self.selection:
             item.move(deltax, deltay)
 
     def end_move(self, event):
-        """End the move of selected items"""
-        self.canvas.bind("<B1-Motion>", "")
-        self.canvas.bind("<ButtonRelease-1>", "")
+        '''End the move of selected items
+        '''
+        self.canvas.bind('<B1-Motion>', '')
+        self.canvas.bind('<ButtonRelease-1>', '')
 
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
         deltax = cx - self._x0
         deltay = cy - self._y0
 
         for item in self.selection:
@@ -643,36 +626,36 @@
         # not scrolling the left pane yet
         item = self.tree.identify_row(event.y)
         plugin_name = self.tree.item(item, option="text")
 
         (last_node, x, y, anchor1, anchor2) = self.next_position()
         edge_subtype = last_node.default_edge_subtype()
 
-        logger.debug("creating {} node".format(plugin_name))
+        logger.debug('creating {} node'.format(plugin_name))
 
         # The node.
         node = self.flowchart.create_node(plugin_name)
 
         # The graphics partner
         plugin = self.plugin_manager.get(plugin_name)
-        logger.debug("  plugin object: {}".format(plugin))
+        logger.debug('  plugin object: {}'.format(plugin))
         tk_node = plugin.create_tk_node(
             tk_flowchart=self, canvas=self.canvas, x=0, y=0, node=node
         )
         self.graph.add_node(tk_node)
 
         # And figure out where the node should be
         # Use the grid approach
         x0 = last_node.x
         y0 = last_node.y
 
-        if anchor1 == "s":
+        if anchor1 == 's':
             tk_node.x = x0
             tk_node.y = y0 + self.grid_y
-        elif anchor1 == "e":
+        elif anchor1 == 'e':
             tk_node.x = x0 + self.grid_x
             tk_node.y = y0
         else:
             dx, dy = tk_node.anchor_point(anchor2)
 
             # flip sign to get direction right
             tk_node.x = x - dx
@@ -680,31 +663,31 @@
 
         # And connect this to the last node in the existing flowchart,
         # which is probably what the user wants.
 
         self.add_edge(
             last_node,
             tk_node,
-            "execution",
+            'execution',
             anchor1=anchor1,
             anchor2=anchor2,
-            edge_subtype=edge_subtype,
+            edge_subtype=edge_subtype
         )
 
         # And update the picture on screen
         self.draw()
 
     def remove_node(self, node):
         """Remove the given node"""
 
         # remove the graphical rendering
         node.undraw()
 
         # and edges
-        node.remove_edge("all")
+        node.remove_edge('all')
 
         # and the node itself
         self.graph.remove_node(node)
 
     def next_position(self):
         """Find a reasonable place to position the next step
         in the flowchart."""
@@ -714,15 +697,15 @@
         # center of node
         x0 = last_node.x
         y0 = last_node.y
 
         # Get the anchor point the last node wants to use
         anchor1 = last_node.next_anchor()
         # and the inverse for the new node
-        anchor2 = anchor1.translate("".maketrans("news", "swen"))
+        anchor2 = anchor1.translate(''.maketrans('news', 'swen'))
 
         # Find the point 'gap' past the anchor point of the last
         # node, looking from the center (0, 0)
 
         x1, y1 = last_node.anchor_point(anchor1)
         dx = x1 - x0
         dy = y1 - y0
@@ -749,80 +732,84 @@
         if self.in_callback:
             print("IN CALLBACK!!!!!!")
             return
         self.in_callback = True
 
         result = None
 
-        self.canvas.delete("type=active_anchor")
-        self.canvas.delete("type=arrow_base")
-        self.canvas.delete("type=arrow_head")
+        self.canvas.delete('type=active_anchor')
+        self.canvas.delete('type=arrow_base')
+        self.canvas.delete('type=arrow_head')
 
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
 
         active = []
         items = self.canvas.find_overlapping(
-            cx + self.halo / 2,
-            cy + self.halo / 2,
-            cx - self.halo / 2,
-            cy - self.halo / 2,
+            cx + self.halo / 2, cy + self.halo / 2, cx - self.halo / 2,
+            cy - self.halo / 2
         )
         if len(items) == 0:
             # If we are within e.g. a rectangle, it may not overlap
             # but will be the current item, so if nothing overlaps
             # use the current item (if there is one).
 
-            items = self.canvas.find_withtag("current")
+            items = self.canvas.find_withtag('current')
 
         # Loop backwards since the 'top' item is at the end of the list
         # and is probably the item we want.
 
         for item in items[::-1]:
             if item in exclude:
                 continue
             tags = self.get_tags(item)
 
             # on an arrow?
-            if "type" in tags and tags["type"] == "arrow":
+            if 'type' in tags and tags['type'] == 'arrow':
                 xys = self.canvas.coords(item)
                 x0 = xys[0]
                 y0 = xys[1]
                 x1 = xys[-2]
                 y1 = xys[-1]
                 self.canvas.create_rectangle(
                     x0 - self.halo / 2,
                     y0 - self.halo / 2,
                     x0 + self.halo / 2,
                     y0 + self.halo / 2,
-                    tags=["type=arrow_base", "arrow=" + str(item), tags["edge"].tag()],
-                    outline="red",
-                    fill="red",
+                    tags=[
+                        'type=arrow_base', 'arrow=' + str(item),
+                        tags['edge'].tag()
+                    ],
+                    outline='red',
+                    fill='red'
                 )
                 self.canvas.create_rectangle(
                     x1 - self.halo / 2,
                     y1 - self.halo / 2,
                     x1 + self.halo / 2,
                     y1 + self.halo / 2,
-                    tags=["type=arrow_head", "arrow=" + str(item), tags["edge"].tag()],
-                    outline="red",
-                    fill="red",
+                    tags=[
+                        'type=arrow_head', 'arrow=' + str(item),
+                        tags['edge'].tag()
+                    ],
+                    outline='red',
+                    fill='red'
                 )
                 break
-            if "node" in tags:
-                node = tags["node"]
+            if 'node' in tags:
+                node = tags['node']
                 if node.is_inside(cx, cy, self.halo):
                     active.append(node)
                     if node not in self.active_nodes:
                         node.activate()
                         self.active_nodes.append(node)
                     # are we close to any anchor points?
                     point = node.check_anchor_points(cx, cy, self.halo)
                     if point is None:
-                        self.canvas.delete("type=active_anchor")
+                        self.canvas.delete('type=active_anchor')
                     else:
                         node.activate_anchor_point(point, self.halo)
                         result = (node, point)
                     break
 
         # deactivate any previously active nodes
         for node in self.active_nodes:
@@ -844,383 +831,408 @@
         Instead we use find_overlapping, which does return a list. However,
         if the mouse is e.g. inside a rectangle bat far enough from the edges
         find_overlapping does not find it. In this case we use the current
         tag to find the object.
         """
 
         items = self.canvas.find_overlapping(
-            x + self.halo / 2, y + self.halo / 2, x - self.halo / 2, y - self.halo / 2
+            x + self.halo / 2, y + self.halo / 2, x - self.halo / 2,
+            y - self.halo / 2
         )
         if len(items) == 0:
             # If we are within e.g. a rectangle, it may not overlap
             # but will be the current item, so if nothing overlaps
             # use the current item (if there is one).
 
-            items = self.canvas.find_withtag("current")
+            items = self.canvas.find_withtag('current')
 
         # Loop backwards since the 'top' item is at the end of the list
         # and is probably the item we want.
 
         for item in items[::-1]:
             if item in exclude:
                 continue
 
             tags = self.get_tags(item)
-            if "node" in tags:
-                node = tags["node"]
+            if 'node' in tags:
+                node = tags['node']
                 if node.is_inside(x, y, self.halo):
                     # are we close to any anchor points?
                     point = node.check_anchor_points(x, y, self.halo)
-                    return ("node", node, point)
-            return ("item", item)
+                    return ('node', node, point)
+            return ('item', item)
         return None
 
     def get_tags(self, item):
-        """Return the tags of "item" as a dict. Any added tags
+        '''Return the tags of "item" as a dict. Any added tags
         like "active" are added to the "extra" dict entry.
-        """
+        '''
 
         tags = {}
-        tags["extra"] = []
+        tags['extra'] = []
         for x in self.canvas.gettags(item):
-            if "=" in x:
-                key, value = x.split("=")
-                if "node" in key:
+            if '=' in x:
+                key, value = x.split('=')
+                if 'node' in key:
                     tags[key] = self.get_node(value)
-                elif "edge" == key:
+                elif 'edge' == key:
                     tags[key] = seamm.TkEdge.str_to_object[value]
                 else:
                     tags[key] = value
             else:
-                tags["extra"].append(x)
+                tags['extra'].append(x)
         return tags
 
     def drag_arrow(self, event):
-        """Drag an arrow from the anchor on the node to the mouse
+        '''Drag an arrow from the anchor on the node to the mouse
         Used when creating a new edge.
-        """
+        '''
 
-        logger.debug("drag arrow")
+        logger.debug('drag arrow')
         node, anchor, x, y, arrow = self.data
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
         logger.debug(
-            "  x = {}, y = {}, cx = {}, cy = {}, arrow = {}".format(x, y, cx, cy, arrow)
+            '  x = {}, y = {}, cx = {}, cy = {}, arrow = {}'.format(
+                x, y, cx, cy, arrow
+            )
         )
         self.canvas.coords(arrow, x, y, cx, cy)
         # Check for being near another nodes anchor point
         result = self.find_items(cx, cy, exclude=(arrow,))
-        logger.debug("  result = {}".format(result))
-        if result is not None and result[0] == "node":
-            logger.debug("       node = {}".format(node))
-            logger.debug("  result[1] = {}".format(result[1]))
+        logger.debug('  result = {}'.format(result))
+        if result is not None and result[0] == 'node':
+            logger.debug('       node = {}'.format(node))
+            logger.debug('  result[1] = {}'.format(result[1]))
             if node == result[1]:
-                self.canvas.delete("type=active_anchor")
-                logger.debug("  deactivate {}".format(result[1]))
+                self.canvas.delete('type=active_anchor')
+                logger.debug('  deactivate {}'.format(result[1]))
                 result[1].deactivate()
             else:
-                logger.debug("  activate_node {} {}".format(result[1], result[2]))
+                logger.debug(
+                    '  activate_node {} {}'.format(result[1], result[2])
+                )
                 self.activate_node(result[1], result[2])
 
     def drop_arrow(self, event):
-        """The user has dropped a new arrow somewhere!
+        '''The user has dropped a new arrow somewhere!
         If it is on another node, make the connection.
         If it is in empty space or on the original node,
         just cancel the operation.
-        """
+        '''
 
-        self.canvas.bind("<B1-Motion>", "")
-        self.canvas.bind("<ButtonRelease-1>", "")
+        self.canvas.bind('<B1-Motion>', '')
+        self.canvas.bind('<ButtonRelease-1>', '')
 
         node, anchor, x, y, arrow = self.data
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
         self.canvas.coords(arrow, x, y, cx, cy)
         # Check for being near another nodes anchor point
         result = self.find_items(cx, cy)
         self.canvas.delete(arrow)
 
-        if result is not None and result[0] == "node":
+        if result is not None and result[0] == 'node':
             other_node, point = result[1:]
             if node != other_node and point is not None:
                 edge_subtype = node.default_edge_subtype()
                 self.add_edge(
                     node,
                     other_node,
-                    "execution",
+                    'execution',
                     anchor1=anchor,
                     anchor2=point,
-                    edge_subtype=edge_subtype,
+                    edge_subtype=edge_subtype
                 )
 
         self.data = None
         self.mouse_op = None
 
     def drag_arrow_base(self, event):
-        """Drag the base of an exisiting arrow"""
+        '''Drag the base of an exisiting arrow
+        '''
 
         # move arrow
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
-        self.canvas.coords(self.data["arrow"], cx, cy, self.data["x1"], self.data["y1"])
+        self.canvas.coords(
+            self.data['arrow'], cx, cy, self.data['x1'], self.data['y1']
+        )
 
         # move base icon
         deltax = cx - self._x0
         deltay = cy - self._y0
 
         self._x0 = cx
         self._y0 = cy
 
-        self.canvas.move(self.data["arrow_base"], deltax, deltay)
+        self.canvas.move(self.data['arrow_base'], deltax, deltay)
 
         # move the label if there is one
-        edge = self.data["edge"]
+        edge = self.data['edge']
         if edge.has_label:
             self.canvas.coords(
                 edge.label_id,
-                edge.label_position(cx, cy, self.data["x1"], self.data["y1"]),
+                edge.label_position(cx, cy, self.data['x1'], self.data['y1'])
+            )
+            self.canvas.coords(
+                edge.label_bg_id, self.canvas.bbox(edge.label_id)
             )
-            self.canvas.coords(edge.label_bg_id, self.canvas.bbox(edge.label_id))
 
         # Check for being near another nodes anchor point
         result = self.find_items(
-            cx, cy, exclude=(self.data["arrow"], self.data["arrow_base"])
+            cx, cy, exclude=(self.data['arrow'], self.data['arrow_base'])
         )
 
-        if result is not None and result[0] == "node":
-            self.activate_node(result[1], result[2], exclude=(self.data["edge"].node2,))
+        if result is not None and result[0] == 'node':
+            self.activate_node(
+                result[1], result[2], exclude=(self.data['edge'].node2,)
+            )
 
     def activate_node(self, node, point=None, exclude=()):
-        """Activate a node, i.e. display the anchor points,
+        '''Activate a node, i.e. display the anchor points,
         unless it is in the exclusion list. Also, if the
         anchor point is given, make it active.
-        """
+        '''
 
         active = []
         if node in exclude:
-            self.canvas.delete("type=active_anchor")
+            self.canvas.delete('type=active_anchor')
             node.deactivate()
         else:
             active.append(node)
             if node not in self.active_nodes:
                 node.activate()
                 self.active_nodes.append(node)
             if point is None:
-                self.canvas.delete("type=active_anchor")
+                self.canvas.delete('type=active_anchor')
             else:
                 node.activate_anchor_point(point, self.halo)
 
         # deactivate any previously active nodes
         for node in self.active_nodes:
             if node not in active:
                 node.deactivate()
         self.active_nodes = active
 
     def drop_arrow_base(self, event):
-        """The user has dropped the arrow somewhere!
+        '''The user has dropped the arrow somewhere!
         If it is on another node, make the connection.
         If it is in empty space or on the original node,
         just cancel the operation.
-        """
+        '''
 
-        self.canvas.bind("<B1-Motion>", "")
-        self.canvas.bind("<ButtonRelease-1>", "")
+        self.canvas.bind('<B1-Motion>', '')
+        self.canvas.bind('<ButtonRelease-1>', '')
 
         # Check for being near another nodes anchor point
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
         result = self.find_items(cx, cy)
 
-        edge = self.data["edge"]
+        edge = self.data['edge']
 
         if result is None:
             # dropped on empty space
-            self.canvas.delete("type=arrow_base")
-            self.canvas.delete("type=arrow_head")
+            self.canvas.delete('type=arrow_base')
+            self.canvas.delete('type=arrow_head')
             edge.draw()
-        elif result[0] == "node":
+        elif result[0] == 'node':
             # dropped on another node
             node1, anchor1 = result[1:]
             if edge.node1 == node1:
                 edge.anchor1 = anchor1
                 edge.draw()
             else:
                 # remove current connection and create new, in
                 # that order -- otherwise tend to remove edge
                 # completely if it is moved on same node.
 
                 node2 = edge.node2
                 anchor2 = edge.anchor2
                 edge_subtype = edge.edge_subtype
 
-                self.remove_edge(self.data["arrow"])
+                self.remove_edge(self.data['arrow'])
 
                 self.add_edge(
                     node1,
                     node2,
-                    edge_type="execution",
+                    edge_type='execution',
                     edge_subtype=edge_subtype,
                     anchor1=anchor1,
                     anchor2=anchor2,
                 )
 
         self.data = None
         self.mouse_op = None
 
     def drag_arrow_head(self, event):
-        """Drag the head of an arrow"""
+        '''Drag the head of an arrow
+        '''
 
         # move arrow
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
-        self.canvas.coords(self.data["arrow"], self.data["x0"], self.data["y0"], cx, cy)
+        self.canvas.coords(
+            self.data['arrow'], self.data['x0'], self.data['y0'], cx, cy
+        )
 
         # move base icon
         deltax = cx - self._x0
         deltay = cy - self._y0
 
         self._x0 = cx
         self._y0 = cy
 
-        self.canvas.move(self.data["arrow_head"], deltax, deltay)
+        self.canvas.move(self.data['arrow_head'], deltax, deltay)
 
         # move the label if there is one
-        edge = self.data["edge"]
+        edge = self.data['edge']
         if edge.has_label:
             self.canvas.coords(
                 edge.label_id,
-                edge.label_position(self.data["x0"], self.data["y0"], cx, cy),
+                edge.label_position(self.data['x0'], self.data['y0'], cx, cy)
+            )
+            self.canvas.coords(
+                edge.label_bg_id, self.canvas.bbox(edge.label_id)
             )
-            self.canvas.coords(edge.label_bg_id, self.canvas.bbox(edge.label_id))
 
         # Check for being near another nodes anchor point
         result = self.find_items(
-            cx, cy, exclude=(self.data["arrow"], self.data["arrow_head"])
+            cx, cy, exclude=(self.data['arrow'], self.data['arrow_head'])
         )
 
-        if result is not None and result[0] == "node":
-            self.activate_node(result[1], result[2], exclude=(self.data["edge"].node1,))
+        if result is not None and result[0] == 'node':
+            self.activate_node(
+                result[1], result[2], exclude=(self.data['edge'].node1,)
+            )
 
     def drop_arrow_head(self, event):
-        """The user has dropped the arrow somewhere!
+        '''The user has dropped the arrow somewhere!
         If it is on another node, make the connection.
         If it is in empty space or on the original node,
         just cancel the operation.
-        """
+        '''
 
-        self.canvas.bind("<B1-Motion>", "")
-        self.canvas.bind("<ButtonRelease-1>", "")
+        self.canvas.bind('<B1-Motion>', '')
+        self.canvas.bind('<ButtonRelease-1>', '')
 
         # Check for being near another nodes anchor point
         cx = int(self.canvas.canvasx(event.x))
         cy = int(self.canvas.canvasy(event.y))
         result = self.find_items(cx, cy)
 
-        edge = self.data["edge"]
+        edge = self.data['edge']
 
         if result is None:
             # dropped on empty space
-            self.canvas.delete("type=arrow_base")
-            self.canvas.delete("type=arrow_head")
+            self.canvas.delete('type=arrow_base')
+            self.canvas.delete('type=arrow_head')
             edge.draw()
-        elif result[0] == "node":
+        elif result[0] == 'node':
             # dropped on another node
             node2, anchor2 = result[1:]
             if edge.node2 == node2:
                 edge.anchor2 = anchor2
                 edge.draw()
             else:
                 # remove current connection and create new, in
                 # that order -- otherwise tend to remove edge
                 # completely if it is moved on same node.
 
                 node1 = edge.node1
                 anchor1 = edge.anchor1
 
-                self.remove_edge(self.data["arrow"])
+                self.remove_edge(self.data['arrow'])
 
                 self.add_edge(
-                    node1, node2, "execution", anchor1=anchor1, anchor2=anchor2
+                    node1,
+                    node2,
+                    'execution',
+                    anchor1=anchor1,
+                    anchor2=anchor2
                 )
 
         self.data = None
         self.mouse_op = None
 
     def right_click_on_arrow(self, event, item, tags):
-        """Handle a right click on an arrow"""
+        '''Handle a right click on an arrow
+        '''
 
         if self.popup_menu is not None:
             self.popup_menu.destroy()
 
         self.popup_menu = tk.Menu(self.canvas, tearoff=0)
         self.popup_menu.add_command(
             label="Delete", command=lambda: self.remove_edge(item)
         )
 
         self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
 
     def remove_edge(self, item):
-        """Remove an edge from the graph and visually"""
+        '''Remove an edge from the graph and visually
+        '''
 
         tags = self.get_tags(item)
-        edge = tags["edge"]
+        edge = tags['edge']
         tag = edge.tag()
         self.graph.remove_edge(
             edge.node1, edge.node2, edge.edge_type, edge.edge_subtype
         )
 
         # Delete the tag, not item, so that we get all labels, etc.
         self.canvas.delete(tag)
-        self.canvas.delete("type=arrow_base")
-        self.canvas.delete("type=arrow_head")
+        self.canvas.delete('type=arrow_base')
+        self.canvas.delete('type=arrow_head')
 
     def print_edges(self, event=None):
-        """Print all the edges. Useful for debugging!"""
+        '''Print all the edges. Useful for debugging!
+        '''
 
-        print("All edges in tk_flowchart")
+        print('All edges in tk_flowchart')
         for edge in self.edges():
             print(
-                "   {} {} {} {} {} {}".format(
-                    edge.node1.tag,
-                    edge.anchor1,
-                    edge.node2.tag,
-                    edge.anchor2,
-                    edge.edge_type,
-                    edge.edge_subtype,
+                '   {} {} {} {} {} {}'.format(
+                    edge.node1.tag, edge.anchor1, edge.node2.tag, edge.anchor2,
+                    edge.edge_type, edge.edge_subtype
                 )
             )
 
     def print_items(self):
-        """Print all the items on the canvas, for debugging"""
+        """Print all the items on the canvas, for debugging
+        """
 
         print()
-        for item in self.canvas.find_withtag("type=arrow"):
-            print("{}: {}".format(item, self.canvas.gettags(item)))
+        for item in self.canvas.find_withtag('type=arrow'):
+            print('{}: {}'.format(item, self.canvas.gettags(item)))
 
     def run(self, event=None):
         """Run the current flowchart"""
 
-        # Ensure that the flowchart is up-to-date
-        flowchart = self.update_flowchart()
+        self.update_flowchart()
+        flowchart = self.flowchart.to_text()
 
-        # Do the graphical "stuff"
         self._job_handler.submit_with_dialog(flowchart=flowchart)
 
     def push(self):
-        """Save a copy of the current flowchart on the stack."""
+        """Save a copy of the current flowchart on the stack.
+        """
         self.update_flowchart()
         self._stack.append(self.flowchart.to_dict())
 
     def pop(self):
-        """Replace the current flowchart with the version on the stack."""
+        """Replace the current flowchart with the version on the stack.
+        """
         self.flowchart.from_dict(self._stack.pop())
         self.from_flowchart()
 
     def pop_and_discard(self):
-        """Remove the saved copy from the stack"""
+        """Remove the saved copy from the stack
+        """
         self._stack.pop()
 
     def update_flowchart(self):
         """Update the non-graphical flowchart"""
         wf = self.flowchart
 
         # Make sure there is nothing in the flowchart
@@ -1233,56 +1245,58 @@
             translate[node] = wf.add_node(copy.copy(node.node))
             node.update_flowchart()
 
         # And the edges
         for edge in self.edges():
             attr = {}
             for key in edge:
-                if key not in ("node1", "node2", "edge_type", "edge_subtype", "canvas"):
+                if key not in (
+                    'node1', 'node2', 'edge_type', 'edge_subtype', 'canvas'
+                ):
                     attr[key] = edge[key]
             node1 = translate[edge.node1]
             node2 = translate[edge.node2]
-            wf.add_edge(node1, node2, edge.edge_type, edge.edge_subtype, **attr)
-
-        return wf
+            wf.add_edge(
+                node1, node2, edge.edge_type, edge.edge_subtype, **attr
+            )
 
     def from_flowchart(self):
         """Recreate the graphics from the non-graphical flowchart"""
         wf = self.flowchart
 
         self.clear()
 
         # Add all the non-graphical nodes, making copies so that
         # when the flowchart is cleared our objects still exist
         translate = {}
         for node in wf:
             extension = node.extension
             if extension is None:
                 # Start node
-                translate[node] = self.get_node("1")
+                translate[node] = self.get_node('1')
             else:
                 new_node = copy.copy(node)
-                logger.debug("creating {} node".format(extension))
+                logger.debug('creating {} node'.format(extension))
                 plugin = self.plugin_manager.get(extension)
-                logger.debug("  plugin object: {}".format(plugin))
+                logger.debug('  plugin object: {}'.format(plugin))
                 tk_node = plugin.create_tk_node(
                     tk_flowchart=self, canvas=self.canvas, node=new_node
                 )
                 translate[node] = tk_node
                 tk_node.from_flowchart()
                 self.graph.add_node(tk_node)
                 tk_node.draw()
 
         # And the edges
         for edge in wf.edges():
             node1 = translate[edge.node1]
             node2 = translate[edge.node2]
             attr = {}
             for key in edge:
-                if key not in ("node1", "node2"):
+                if key not in ('node1', 'node2'):
                     attr[key] = edge[key]
             self.add_edge(node1, node2, **attr)
 
     def _bound_to_mousewheel(self, event):
         """Set the bindings on the canvas, used when the
         mouse enters the canvas
         """
@@ -1313,81 +1327,88 @@
         if event.num == 5 or event.delta < 0:
             delta = 1
         else:
             delta = -1
 
         self.canvas.yview_scroll(delta, "units")
 
-        x0, y0, x1, y1 = self.canvas.cget("scrollregion").split(" ")
+        x0, y0, x1, y1 = self.canvas.cget('scrollregion').split(' ')
         f0, f1 = self.canvas.yview()
         y = (int(y1) - int(y0)) * f0
 
-        tk._default_root.tk.call(self.canvas, "moveto", self.background, 0, y)
+        tk._default_root.tk.call(self.canvas, 'moveto', self.background, 0, y)
 
     def xview(self, command, amount, *args):
-        """Scroll in the x direction, keeping the background picture stationary"""
+        """Scroll in the x direction, keeping the background picture stationary
+        """
         self.canvas.xview(command, amount, *args)
 
-        x0, y0, x1, y1 = self.canvas.cget("scrollregion").split(" ")
+        x0, y0, x1, y1 = self.canvas.cget('scrollregion').split(' ')
         f0, f1 = self.canvas.xview()
         x = (int(x1) - int(x0)) * f0
         f0, f1 = self.canvas.yview()
         y = (int(y1) - int(y0)) * f0
 
-        tk._default_root.tk.call(self.canvas, "moveto", self.background, x, y)
+        tk._default_root.tk.call(self.canvas, 'moveto', self.background, x, y)
 
     def yview(self, command, amount, *args):
-        """Scroll in the y direction, keeping the background picture stationary"""
+        """Scroll in the y direction, keeping the background picture stationary
+        """
         self.canvas.yview(command, amount, *args)
 
-        x0, y0, x1, y1 = self.canvas.cget("scrollregion").split(" ")
+        x0, y0, x1, y1 = self.canvas.cget('scrollregion').split(' ')
         f0, f1 = self.canvas.xview()
         x = (int(x1) - int(x0)) * f0
         f0, f1 = self.canvas.yview()
         y = (int(y1) - int(y0)) * f0
 
-        tk._default_root.tk.call(self.canvas, "moveto", self.background, x, y)
+        tk._default_root.tk.call(self.canvas, 'moveto', self.background, x, y)
 
     def clean_layout(self, event=None):
-        """Clean the visual layout of the flowchart"""
+        """Clean the visual layout of the flowchart
+        """
 
         # clear the visited flag
         for node in self:
             node.node.visited = False
 
         # get the node to start the traversal
-        node = self.get_node("1")
+        node = self.get_node('1')
 
         # traverse the nodes, finding what loops they are in
         self._loops = {}  # what loops a node is in
-        self._in_loop = {"start": []}  # ordered list of nodes directly in a loop
+        self._in_loop = {  # ordered list of nodes directly in a loop
+            'start': []
+        }
         loops = tuple()
 
         self._loop_helper(loops, node)
 
-        logger.debug("\nloops\n\n{}".format(pprint.pformat(self._loops)))
-        logger.debug("\nin loops\n\n{}".format(pprint.pformat(self._in_loop)))
+        logger.debug('\nloops\n\n{}'.format(pprint.pformat(self._loops)))
+        logger.debug('\nin loops\n\n{}'.format(pprint.pformat(self._in_loop)))
 
         # Move the nodes to the correct place on the grid
         x = 0
         y = 0
-        self._loopxy = {"start": (0, 0)}
-        self._layout_nodes("start", x, y)
+        self._loopxy = {'start': (0, 0)}
+        self._layout_nodes('start', x, y)
 
-        logger.debug("\nmax x,y\n\n{}".format(pprint.pformat(self._loopxy)))
+        logger.debug('\nmax x,y\n\n{}'.format(pprint.pformat(self._loopxy)))
 
         # Fix the edges
         for edge in self.edges():
             # only work on edges that go upwards
             x0, y0 = edge.node1.anchor_point(edge.anchor1)
             x1, y1 = edge.node2.anchor_point(edge.anchor2)
-            logger.debug("   edge {}: {}, {} to {}, {}".format(edge, x0, y0, x1, y1))
+            logger.debug(
+                '   edge {}: {}, {} to {}, {}'.format(edge, x0, y0, x1, y1)
+            )
             if y1 < y0:
                 edge.coords = [x0, y0]
-                logger.debug("   edge.node1 = {}".format(edge.node1))
+                logger.debug('   edge.node1 = {}'.format(edge.node1))
                 loop = self._loops[edge.node1][-1]
                 xmax, ymax = self._loopxy[loop]
                 xmax = (xmax + 1) * self.grid_x
                 ymax = (ymax + 1) * self.grid_y
 
                 dx = 10 * len(self._loops[edge.node1])
                 dy = 0
@@ -1411,23 +1432,24 @@
         self.draw()
 
         del self._loops
         del self._in_loop
         del self._loopxy
 
     def _layout_nodes(self, loop, x, y):
-        """Recursively position nodes"""
+        """Recursively position nodes
+        """
         for node in self._in_loop[loop]:
             x0 = int(node.x)
             y0 = int(node.y)
             node.x = int((x + 0.5) * self.grid_x)
             node.y = int((y + 0.5) * self.grid_y)
 
             logger.debug(
-                "node {} {} = {:3d} {:3d} ({:3d} {:3d}) {}".format(
+                'node {} {} = {:3d} {:3d} ({:3d} {:3d}) {}'.format(
                     x, y, int(node.x), int(node.y), x0, y0, node
                 )
             )
 
             xmax, ymax = self._loopxy[loop]
             if x > xmax:
                 xmax = x
@@ -1441,40 +1463,43 @@
                 self._loopxy[loop] = (x1, y)
             else:
                 y += 1
 
         return x, y
 
     def _loop_helper(self, loops, node):
-        """A helper to traverse graph finding the grid locations of the nodes"""
+        """A helper to traverse graph finding the grid locations of the nodes
+        """
         node.node.visited = True
         self._loops[node] = loops
 
-        logger.debug("node = {}, loops = {}".format(node, loops))
+        logger.debug('node = {}, loops = {}'.format(node, loops))
 
         if len(loops) == 0:
-            self._in_loop["start"].append(node)
+            self._in_loop['start'].append(node)
         else:
             self._in_loop[loops[-1]].append(node)
 
-        if node.node_type == "loop":
+        if node.node_type == 'loop':
             loops = loops + (node,)
             self._in_loop[node] = []
             # nodes in the loop
-            for edge in self.graph.edges(node, direction="out"):
-                if edge.edge_type == "execution" and edge.edge_subtype == "loop":
+            for edge in self.graph.edges(node, direction='out'):
+                if edge.edge_type == "execution" and \
+                   edge.edge_subtype == 'loop':
                     node2 = edge.node2
                     if not node2.node.visited:
                         self._loop_helper(loops, node2)
             loops = loops[0:-1]
             # end exiting the loop
-            for edge in self.graph.edges(node, direction="out"):
-                if edge.edge_type == "execution" and edge.edge_subtype == "exit":
+            for edge in self.graph.edges(node, direction='out'):
+                if edge.edge_type == "execution" and \
+                   edge.edge_subtype == 'exit':
                     node2 = edge.node2
                     if not node2.node.visited:
                         self._loop_helper(loops, node2)
         else:
-            for edge in self.graph.edges(node, direction="out"):
+            for edge in self.graph.edges(node, direction='out'):
                 if edge.edge_type == "execution":
                     node2 = edge.node2
                     if not node2.node.visited:
                         self._loop_helper(loops, node2)
```

### Comparing `seamm-2023.4.8/seamm/tk_job_handler.py` & `seamm-220.8.3/seamm/tk_job_handler.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,567 +1,670 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
-"""
-The graphical interface for submitting SEAMM jobs.
+"""The graphical interface for submitting SEAMM jobs.
 
 A job in SEAMM is composed of a flowchart and any other files that the
 flowchart requires. This module provides the TkJobHandler class, which
 provides a use interface and the machinery to gather the necessary
 files and submit the job to a dashboard.
 """
 
 import configparser
 import logging
 from pathlib import Path
-import pkg_resources
-import shlex
+import requests
 import tkinter as tk
 from tkinter import messagebox
-from tkinter import simpledialog
 import tkinter.ttk as ttk
 
 import Pmw
 
-from .dashboard_handler import DashboardHandler
 import seamm_widgets as sw
 
 logger = logging.getLogger(__name__)
 
 
 class TkJobHandler(object):
+
     def __init__(self, root=None):
         """Setup the Job Handler object.
 
         Parameters
         ----------
         root : Tk window
             The root Tk window.
+
         """
         self._root = root
         self.config = configparser.ConfigParser()
+        self.configfile = Path.home() / '.seamm' / 'dashboards.ini'
         self.dialog = None
-
-        self._dashboard_handler = None
-
-        self._flowchart = None
         self._widgets = {}
-        self._variable_value = {}
-        self.resource_path = Path(pkg_resources.resource_filename(__name__, "data/"))
-
-        s = ttk.Style()
-        s.configure("Border.TLabel", relief="ridge", anchor=tk.W, padding=5)
-
-    # Provide dict like access to the widgets to make
-    # the code cleaner
-
-    def __getitem__(self, key):
-        """Allow [] access to the widgets."""
-        return self._widgets[key]
 
-    def __setitem__(self, key, value):
-        """Allow [key] access to set a widgets."""
-        self._widgets[key] = value
-
-    def __delitem__(self, key):
-        """Allow deletion of widgets."""
-        try:
-            if key in self._widgets:
-                self._widgets[key].destroy()
-        except Exception:
-            pass
-        del self._widgets[key]
-
-    def __iter__(self):
-        """Allow iteration over the widgets"""
-        return iter(self._widgets)
-
-    def __len__(self):
-        """Provide the nmber of widgets, for e.g. len() command."""
-        return len(self._widgets)
-
-    @property
-    def current_dashboard(self):
-        "The current dashboard, from dashboard_handler"
-        return self.dashboard_handler.current_dashboard
-
-    @current_dashboard.setter
-    def current_dashboard(self, dashboard):
-        self.current_dashboard.current_dashboard = dashboard
-
-    @property
-    def dashboard_handler(self):
-        "The connection to the dashboards."
-        if self._dashboard_handler is None:
-            self._dashboard_handler = DashboardHandler()
-        return self._dashboard_handler
-
-    def add_dashboard_cb(self):
-        """Post a dialog for adding a dashboard to the list."""
-        dialog = Pmw.Dialog(
-            self._root,
-            buttons=("OK", "Cancel"),
-            master=self._root,
-            title="Add Dashboard to list",
-            command=self.handle_add_dialog,
+        # Read in the dashboard information if present
+        self.get_configuration()
+        self.current_dashboard = self.config.get(
+            'global options', 'current_dashboard', fallback=None
         )
-        dialog.withdraw()
-        w = self["add"] = {"dialog": dialog}
-
-        d = dialog.interior()
-        name = sw.LabeledEntry(d, labeltext="Name", width=50)
-        url = sw.LabeledEntry(d, labeltext="URL")
-        protocol = sw.LabeledCombobox(
-            d, labeltext="Protocol", values=["http", "sshtunnel"]
+        self.timeout = self.config.get(
+            'global options', 'timeout', fallback=0.5
         )
-        protocol.set("http")
-
-        w["name"] = name
-        w["url"] = url
-        w["protocol"] = protocol
 
-        name.grid(row=0, column=0, sticky=tk.EW)
-        url.grid(row=1, column=0, sticky=tk.EW)
-        protocol.grid(row=2, column=0, sticky=tk.W)
-
-        sw.align_labels([name, url, protocol])
+        s = ttk.Style()
+        s.configure("Border.TLabel", relief='ridge', anchor=tk.W, padding=5)
 
-        dialog.activate(geometry="centerscreenfirst")
+    @property
+    def dashboards(self):
+        """The list of dashboards."""
+        result = []
+        for dashboard in self.config:
+            if (
+                dashboard
+                not in ('global options', self.config.default_section)
+            ):
+                result.append(dashboard)
+        return sorted(result)
 
-    def ask_for_credentials(self, dashboard, user=None, password=None):
-        """Prompt the user for the login for the dashboard
+    def submit_with_dialog(self, flowchart=None):
+        """
+        Allow the user to choose the dashboard and other parameters,
+        and submit the job as requested.
 
         Parameters
         ----------
-        dashboard : str
-            The name of the dashboard.
-        user : str
-            The username for that dashboard.
-        password : str
-            The password for the user.
+        flowchart : text, optional
+            The flowchart to use. If not given, prompt the user for
+            one.
 
         Returns
         -------
-        (str, str)
-            A tuple with the username and password.
+        job_id : integer
+            The id of the submitted job.
         """
-        dialog = Pmw.Dialog(
-            self._root,
-            buttons=("OK", "Cancel"),
-            master=self._root,
-            title=f"Log-in for {dashboard}",
-        )
-        dialog.withdraw()
-
-        d = dialog.interior()
-        w_user = sw.LabeledEntry(d, labeltext="Username:", width=50)
-        w_password = sw.LabeledEntry(d, labeltext="Password:", show="*")
-
-        w_user.grid(row=0, column=0, sticky=tk.EW)
-        w_password.grid(row=1, column=0, sticky=tk.EW)
-
-        sw.align_labels([w_user, w_password], sticky=tk.E)
+        if self.dialog is None:
+            self.create_submit_dialog()
 
-        result = dialog.activate(geometry="centerscreenfirst")
+        result = self.dialog.activate(geometry='centerscreenfirst')
 
-        if result == "OK":
-            user = w_user.get()
-            password = w_password.get()
+        if result is not None:
+            job_id = self.submit(flowchart, **result)
+            return job_id
+        else:
+            return None
 
-        dialog.destroy()
+    def submit(self, flowchart, dashboard, **job):
+        """Submit the job to the given dashboard.
+        """
+        job['flowchart'] = flowchart
+        job['path'] = 'unset'
 
-        return user, password
+        url = self.config[dashboard]['url']
 
-    def check_status_cb(self):
-        """Helper for checking the status of a dashboard."""
-        w = self["edit dashboard"]
-        dashboard = w["dashboard"]
-        status = self.dashboard_handler.get_dashboard(dashboard).status()
-        w["status"].set(status)
+        response = requests.post(url + '/api/jobs', json=job)
+        if response.status_code != 201:
+            raise RuntimeError(
+                'POST /api/jobs/ {}'.format(response.status_code)
+            )
+        job_id = response.json()['id']
+        logger.info('Submitted job #{}'.format(job_id))
+        return job_id
 
-    def create_submit_dialog(self, title="", description=""):
+    def create_submit_dialog(self):
         """Create the dialog for submitting a job.
 
-        Parameters
-        ----------
-        flowchart : seamm.Flowchart
-            The flowchart object
         """
-        logger.debug("Creating submit dialog")
+        logger.debug('Creating submit dialog')
         self.dialog = Pmw.Dialog(
             self._root,
-            buttons=("OK", "Cancel"),
+            buttons=('OK', 'Cancel'),
             master=self._root,
-            title="Submit job to SEAMM",
-            command=self.handle_dialog,
+            title='Submit job to SEAMM',
+            command=self.handle_dialog
         )
         self.dialog.withdraw()
 
+        w = self._widgets
         d = self.dialog.interior()
 
         # Dashboard
-        dashboards = self.dashboard_handler.dashboards
-        self["dashboard"] = sw.LabeledCombobox(
-            d, labeltext="Dashboard:", values=dashboards
+        dashboards = sorted(self.config.sections())
+        w['dashboard'] = sw.LabeledCombobox(
+            d, labeltext='Dashboard:', values=dashboards
         )
-        self["dashboard"].combobox.bind("<<ComboboxSelected>>", self.dashboard_cb)
+        w['dashboard'].combobox.bind("<<ComboboxSelected>>", self.dashboard_cb)
 
-        self["add"] = ttk.Button(
-            d, text="add dashboard...", command=self.add_dashboard_cb
+        w['add'] = ttk.Button(
+            d, text='add dashboard...', command=self.add_dashboard_cb
         )
 
         # User and project
-        self["project"] = sw.LabeledCombobox(d, labeltext="Project:", state="readonly")
-        self["project"].bind("<<ComboboxSelected>>", self.project_cb)
+        w['username'] = sw.LabeledEntry(d, labeltext='User:')
+        w['username'].set(self.configfile.owner())
+        w['project'] = sw.LabeledCombobox(d, labeltext='Project:')
 
         # Title
-        self["title"] = sw.LabeledEntry(d, labeltext="Title:", width=100)
-        self["title"].set(title)
+        w['title'] = sw.LabeledEntry(d, labeltext='Title:', width=100)
 
         # Description
-        self["description label"] = ttk.Label(d, text="Description:")
         frame = sw.ScrolledFrame(
             d, scroll_vertically=True, borderwidth=2, relief=tk.SUNKEN
         )
         f = frame.interior()
-        self["description"] = tk.Text(f)
-        self["description"].grid(sticky=tk.EW)
-        self["description"].insert("1.0", description)
+        w['description'] = tk.Text(f)
+        w['description'].grid(sticky=tk.EW)
 
         f.rowconfigure(0, weight=1)
         f.columnconfigure(0, weight=1)
 
-        # Reset and clear buttons
-        rf = self["reset frame"] = tk.Frame(d)
-        self["reset title"] = ttk.Button(
-            rf, text="reset title", command=self.reset_title
-        )
-        self["clear title"] = ttk.Button(
-            rf, text="clear title", command=self.clear_title
-        )
-        self["reset description"] = ttk.Button(
-            rf, text="reset description", command=self.reset_description
-        )
-        self["clear description"] = ttk.Button(
-            rf, text="clear description", command=self.clear_description
-        )
-        self["reset title"].grid(row=0, column=0)
-        self["clear title"].grid(row=0, column=1)
-        self["reset description"].grid(row=0, column=2)
-        self["clear description"].grid(row=0, column=3)
-
-        # Space for any parameters
-        self["parameters label"] = ttk.Label(d, text="Parameters:")
-        self["parameters"] = sw.ScrolledColumns(
-            d,
-            columns=[
-                "Name",
-                "Value",
-                "",
-                "Description",
-            ],
-        )
-
         # Set up the dashboard and projects if needed
         if len(dashboards) > 0:
-            self["dashboard"].set(self.current_dashboard.name)
+            tmp = self.config.get(
+                'global options', 'current_dashboard', fallback=dashboards[0]
+            )
+            if tmp not in dashboards:
+                tmp = dashboards[0]
+
+            if self.current_dashboard != tmp:
+                self.current_dashboard = tmp
+                self.save_configuration()
+
+            w['dashboard'].set(tmp)
             self.dashboard_cb()
 
         # Grid the widgets into rows and columns
-        self["dashboard"].grid(row=0, column=0, sticky=tk.EW)
-        self["add"].grid(row=0, column=1, sticky=tk.W)
-        self["project"].grid(row=1, column=0, sticky=tk.EW)
-        self["title"].grid(row=2, column=0, columnspan=2, sticky=tk.W)
-        self["description label"].grid(row=3, column=0, columnspan=2, sticky=tk.W)
-        frame.grid(row=4, column=0, columnspan=2, sticky=tk.NSEW)
-        self["reset frame"].grid(row=5, column=0, columnspan=2)
-        self["parameters label"].grid(row=6, column=0, columnspan=2, sticky=tk.W)
-        self["parameters"].grid(row=7, column=0, columnspan=2, sticky=tk.NSEW)
+        w['dashboard'].grid(row=0, column=0, sticky=tk.EW)
+        w['add'].grid(row=0, column=1, sticky=tk.W)
+        w['username'].grid(row=1, column=0, sticky=tk.EW)
+        w['project'].grid(row=1, column=1, sticky=tk.EW)
+        w['title'].grid(row=2, column=0, columnspan=2, sticky=tk.W)
+        frame.grid(row=3, column=0, columnspan=2, sticky=tk.NSEW)
 
-        sw.align_labels([self["dashboard"], self["project"], self["title"]])
+        sw.align_labels([w['dashboard'], w['username'], w['title']])
 
-        d.rowconfigure(4, weight=1)
-        d.rowconfigure(7, weight=1)
+        d.rowconfigure(3, weight=1)
         d.columnconfigure(1, weight=1)
 
+    def handle_dialog(self, result):
+        """Handle the submit dialog being completed.
+        """
+        if result is None or result == 'Cancel':
+            self.dialog.deactivate(None)
+        else:
+            w = self._widgets
+            self.dialog.deactivate(
+                {
+                    'username': w['username'].get(),
+                    'project': w['project'].get(),
+                    'title': w['title'].get(),
+                    'dashboard': w['dashboard'].get(),
+                    'description': w['description'].get(1.0, tk.END)
+                }
+            )
+
+    def get_configuration(self):
+        """Get the list of dashboards from the config file.
+        """
+        # The path to the configfile
+        if self.configfile.exists():
+            self.config.read(self.configfile)
+        else:
+            self.config.clear()
+
+    def save_configuration(self):
+        """Save the list of dashboards to disk.
+        """
+        # Make sure the directory exists
+        self.configfile.parent.mkdir(exist_ok=True)
+
+        # Update the current dashboard
+        if self.current_dashboard is not None:
+            if 'global options' not in self.config:
+                self.config['global options'] = {}
+            defaults = self.config['global options']
+            defaults['current_dashboard'] = self.current_dashboard
+
+        with self.configfile.open('w') as fd:
+            self.config.write(fd)
+
+    def add_dashboard_cb(self):
+        """Post a dialog for adding a dashboard to the list.
+        """
+        dialog = Pmw.Dialog(
+            self._root,
+            buttons=('OK', 'Cancel'),
+            master=self._root,
+            title='Add Dashboard to list',
+            command=self.handle_add_dialog
+        )
+        dialog.withdraw()
+        w = self._widgets['add'] = {'dialog': dialog}
+
+        d = dialog.interior()
+        name = sw.LabeledEntry(d, labeltext='Name', width=50)
+        url = sw.LabeledEntry(d, labeltext='URL')
+        protocol = sw.LabeledCombobox(
+            d, labeltext='Protocol', values=['http', 'sshtunnel']
+        )
+        protocol.set('http')
+
+        w['name'] = name
+        w['url'] = url
+        w['protocol'] = protocol
+
+        name.grid(row=0, column=0, sticky=tk.EW)
+        url.grid(row=1, column=0, sticky=tk.EW)
+        protocol.grid(row=2, column=0, sticky=tk.W)
+
+        sw.align_labels([name, url, protocol])
+
+        dialog.activate(geometry='centerscreenfirst')
+
+    def handle_add_dialog(self, result):
+        """Handle the dialog to add a dashboard to the list.
+        """
+        w = self._widgets['add']
+        dialog = w['dialog']
+        if result is None or result == 'Cancel':
+            dialog.deactivate(result)
+        else:
+            name = w['name'].get()
+            url = w['url'].get()
+            protocol = w['protocol'].get()
+
+            if name in self.config:
+                messagebox.showwarning(
+                    'Duplicate name', (
+                        "There is already a dashboard called '{}'\n"
+                        'Use a different name.'
+                    ).format(name)
+                )
+                return
+
+            dialog.deactivate(result)
+        dialog.destroy()
+        del self._widgets['add']
+
+        # Now add to the configuration
+        self.config[name] = {'url': url, 'protocol': protocol}
+
+        self.save_configuration()
+
+        # And reset the list in the dashboard combobox
+        c = self._widgets['dashboard']
+        c.combobox.config({'value': self.config.sections()})
+        c.set(name)
+
     def dashboard_cb(self, event=None):
         """The selected dashboard has been changed"""
-        dashboard = self["dashboard"].get()
+        w = self._widgets
+        dashboard = w['dashboard'].get()
+
+        url = self.config[dashboard]['url']
 
-        projects = self.dashboard_handler.get_dashboard(dashboard).list_projects()
-        if len(projects) == 0:
+        try:
+            response = requests.get(
+                url + '/api/list-projects', timeout=self.timeout
+            )
+            if response.status_code != 200:
+                logger.warning(
+                    (
+                        'Encountered an error getting the projects from '
+                        "dashboard '{}', error code: {}"
+                    ).format(dashboard, response.status_code)
+                )
+                messagebox.showerror(
+                    title='Dashboard error',
+                    message="Dashboard '{}' returned an error: {}".format(
+                        dashboard, response.status_code
+                    )
+                )
+                if self.current_dashboard is not None:
+                    w['dashboard'].set(self.current_dashboard)
+                return
+            else:
+                projects = response.json()['projects']
+        except requests.exceptions.Timeout:
+            logger.warning(
+                'A timeout occurred contacting the dashboard ' + dashboard
+            )
+            messagebox.showerror(
+                title='Dashboard error',
+                message="Could not reach dashboard '{}'".format(dashboard)
+            )
             if self.current_dashboard is not None:
-                self["dashboard"].set(self.current_dashboard.name)
+                w['dashboard'].set(self.current_dashboard)
+            return
+        except requests.exceptions.ConnectionError:
+            logger.warning(
+                'A connection error occurred contacting the dashboard ' +
+                dashboard
+            )
+            messagebox.showerror(
+                title='Dashboard error',
+                message=(
+                    "A connection error occured reaching dashboard '{}'"
+                ).format(dashboard)
+            )  # yapf: disable
+            if self.current_dashboard is not None:
+                w['dashboard'].set(self.current_dashboard)
             return
 
         # All OK, changed the widgets
-        projects.append("-- Create new project --")
-        self["project"].combobox.config({"value": projects})
+        w['project'].combobox.config({'value': projects})
         if len(projects) > 0:
-            self["project"].set(projects[0])
+            w['project'].set(projects[0])
         else:
-            self["project"].set("")
+            w['project'].set('')
         self.current_dashboard = dashboard
+        self.save_configuration()
 
     def display_dashboards(self):
         """Display a list of all the dashboards with their status.
 
         Allow users to edit, remove and add dashboards.
         """
         # statuses = self.get_all_status(master=self._root)
 
         dialog = Pmw.Dialog(
             self._root,
-            buttons=("OK", "Edit", "Remove", "Cancel"),
+            buttons=('OK', 'Edit', 'Remove', 'Cancel'),
             master=self._root,
-            title="Dashboards",
-            command=self.handle_dashboard_dialog,
+            title='Dashboards',
+            command=self.handle_dashboard_dialog
         )
         dialog.withdraw()
-        w = self["display"] = {"dialog": dialog}
+        w = self._widgets['display'] = {'dialog': dialog}
 
         d = dialog.interior()
-        w["table"] = sw.ScrolledColumns(
+        w['table'] = sw.ScrolledColumns(
             d,
             columns=[
-                "Select",
-                "Dashboard",
-                "URL",
-                "Status",
+                'Select',
+                'Dashboard',
+                'URL',
+                'Status',
             ],
-            header_style="Border.TLabel",
+            header_style='Border.TLabel'
         )
-        w["table"].grid(row=0, column=0, sticky=tk.NSEW)
+        w['table'].grid(row=0, column=0, sticky=tk.NSEW)
         d.columnconfigure(0, weight=1)
         d.rowconfigure(0, weight=1)
 
         # Button to update all status
-        w["update all"] = ttk.Button(
-            d, text="Update Status of All Dashboards", command=self.fill_statuses
+        w['update all'] = ttk.Button(
+            d,
+            text="Update Status of All Dashboards",
+            command=self.fill_statuses
         )
-        w["update all"].grid()
+        w['update all'].grid()
 
         # Fill in the dashboards
-        table = w["table"]
+        table = w['table']
         f = table.interior()
         row = 0
-        w["selected"] = tk.StringVar()
+        w['selected'] = tk.StringVar()
         if self.current_dashboard is not None:
-            w["selected"].set(self.current_dashboard.name)
-        for dashboard in self.dashboard_handler.dashboards:
+            w['selected'].set(self.current_dashboard)
+        for dashboard in self.dashboards:
             table[row, 0] = ttk.Radiobutton(
                 f,
-                variable=w["selected"],
+                variable=w['selected'],
                 value=dashboard,
             )
-            table[row, 1] = ttk.Label(f, text=dashboard, style="Border.TLabel")
+            table[row, 1] = ttk.Label(f, text=dashboard, style='Border.TLabel')
             table[row, 2] = ttk.Label(
-                f, text=self.config[dashboard]["url"], style="Border.TLabel"
+                f, text=self.config[dashboard]['url'], style='Border.TLabel'
             )
-            state = self.config.get(dashboard, "state", fallback="active")
-            if state == "active":
-                table[row, 3] = ttk.Label(f, width=16, style="Border.TLabel")
+            state = self.config.get(dashboard, 'state', fallback='active')
+            if state == 'active':
+                table[row, 3] = ttk.Label(f, width=16, style='Border.TLabel')
             else:
                 table[row, 3] = ttk.Label(
-                    f, text=state, width=16, style="Border.TLabel"
+                    f, text=state, width=16, style='Border.TLabel'
                 )
             table[row, 0].grid(sticky=tk.EW)
             table[row, 1].grid(sticky=tk.EW)
             table[row, 2].grid(sticky=tk.EW)
             table[row, 3].grid(sticky=tk.EW)
             row += 1
 
         self.fit_dialog(dialog)
 
-        dialog.activate(geometry="centerscreenfirst")
+        dialog.activate(geometry='centerscreenfirst')
 
         dialog.destroy()
-        del self["display"]
+        del self._widgets['display']
+
+    def fill_statuses(self):
+        w = self._widgets['display']
+        dialog = w['dialog']
+        table = w['table']
+
+        dialog.configure(title='Dashboards -- Updating Status')
+        progress = ttk.Progressbar(
+            dialog.interior(),
+            orient=tk.HORIZONTAL,
+            maximum=table.nrows + 1,
+            mode='determinate',
+            value=1
+        )
+        progress.grid(sticky=tk.EW)
+
+        for row in range(table.nrows):
+            current_status = table[row, 3].cget('text')
+            if current_status != 'inactive':
+                table[row, 3].configure(text='...')
+                table.update()
+                status = self.status(table[row, 1].cget('text'))
+                table[row, 3].configure(text=status)
+            progress.step()
+            table.update()
+        progress.destroy()
+        dialog.configure(title='Dashboards')
+
+    def status(self, dashboard, timeout=1):
+        """The status of the given dashboard.
+
+        Contact the given dashboard, checking for errors, timeouts,
+        etc. and report back the current status.
+
+        Return
+        ------
+        status : enum (a string...)
+            'up'
+            'down'
+            'error'
+        """
+
+        url = self.config[dashboard]['url']
+
+        try:
+            response = requests.get(url + '/api/status', timeout=timeout)
+            if response.status_code != 200:
+                logger.info(
+                    (
+                        'Encountered an error getting the status from '
+                        "dashboard '{}', error code: {}"
+                    ).format(dashboard, response.status_code)
+                )
+                result = 'dashboard error'
+            else:
+                result = response.text
+        except requests.exceptions.Timeout:
+            logger.info(
+                'A timeout occurred contacting the dashboard ' + dashboard
+            )
+            result = 'down'
+        except requests.exceptions.ConnectionError as e:
+            logger.info(
+                'A connection error occurred contacting the dashboard ' +
+                dashboard
+            )
+            if e.response is not None:
+                logger.info(
+                    'Status code = {}, {}'.format(
+                        e.response.status_code, e.response.text
+                    )
+                )
+            result = 'connection error'
+
+        return result
+
+    def handle_dashboard_dialog(self, result):
+        """Handle the dialog to add a dashboard to the list.
+        """
+        w = self._widgets['display']
+        dialog = w['dialog']
+        dashboard = w['selected'].get()
+        if result is None or result == 'Cancel':
+            dialog.deactivate(None)
+        elif result == 'Edit':
+            self.edit_cb(dashboard)
+        elif result == 'Remove':
+            self.remove_cb(dashboard)
+        else:
+            dialog.deactivate(None)
 
     def edit_cb(self, dashboard):
-        """Edit the information for a dashboard."""
-        table = self["display"]["table"]
+        """Edit the information for a dashboard.
+        """
+        table = self._widgets['display']['table']
         for trow in range(table.nrows):
-            if table[trow, 1].cget("text") == dashboard:
+            if table[trow, 1].cget('text') == dashboard:
                 break
 
         dialog = Pmw.Dialog(
             self._root,
-            buttons=("OK", "Cancel"),
-            title="Edit " + dashboard.title(),
+            buttons=('OK', 'Cancel'),
+            title='Edit ' + dashboard.title(),
         )
         dialog.withdraw()
-        w = self["edit dashboard"] = {"dialog": dialog, "dashboard": dashboard}
+        w = self._widgets['edit dashboard'] = {
+            'dialog': dialog,
+            'dashboard': dashboard
+        }
 
         d = dialog.interior()
-        name = sw.LabeledEntry(d, labeltext="Name:", width=50)
-        name.set(table[trow, 1].cget("text"))
-        url = sw.LabeledEntry(d, labeltext="URL:", width=50)
-        url.set(table[trow, 2].cget("text"))
-        state = sw.LabeledCombobox(d, labeltext="State:", values=["active", "inactive"])
-        current_status = table[trow, 3].cget("text")
-        if current_status == "inactive":
-            state.set("inactive")
+        name = sw.LabeledEntry(d, labeltext='Name:', width=50)
+        name.set(table[trow, 1].cget('text'))
+        url = sw.LabeledEntry(d, labeltext='URL:', width=50)
+        url.set(table[trow, 2].cget('text'))
+        state = sw.LabeledCombobox(
+            d, labeltext='State:', values=['active', 'inactive']
+        )
+        current_status = table[trow, 3].cget('text')
+        if current_status == 'inactive':
+            state.set('inactive')
         else:
-            state.set("active")
-        status = sw.LabeledEntry(d, labeltext="Status:", width=16)
+            state.set('active')
+        status = sw.LabeledEntry(d, labeltext='Status:', width=16)
         status.set(current_status)
-        check_status = ttk.Button(d, text="Check Status", command=self.check_status_cb)
-        w["status"] = status
+        check_status = ttk.Button(
+            d, text='Check Status', command=self.check_status_cb
+        )
+        w['status'] = status
 
         name.grid(row=0, columnspan=2, sticky=tk.EW)
         url.grid(row=1, columnspan=2, sticky=tk.EW)
         state.grid(row=2, columnspan=2, sticky=tk.EW)
         status.grid(row=3, sticky=tk.EW)
         check_status.grid(row=3, column=1)
 
         widgets = [name, url, state, status]
 
         # If there are any other items in the config file, put them in
         row = 3
         for key, value in self.config.items(dashboard):
-            if key not in ("url", "state", "status"):
+            if key not in ('url', 'state', 'status'):
                 row += 1
-                w[key] = sw.LabeledEntry(d, labeltext=key + ":")
+                w[key] = sw.LabeledEntry(d, labeltext=key + ':')
                 w[key].set(value)
                 w[key].grid(row=row, columnspan=2, sticky=tk.EW)
                 widgets.append(w[key])
 
         sw.align_labels(widgets)
 
-        result = dialog.activate(geometry="centerscreenfirst")
+        result = dialog.activate(geometry='centerscreenfirst')
 
-        if result == "OK":
+        if result == 'OK':
             if name.get() != dashboard:
-                self.dashboard_handler.rename_dashboard(dashboard, name.get())
                 # Changed the name. Move the section in the config file
+                tmp = {}
+                for key, value in self.config.items(dashboard):
+                    tmp[key] = value
+                self.config.remove_section(dashboard)
                 dashboard = name.get()
+                self.config[dashboard] = tmp
                 table[trow, 1].configure(text=dashboard)
                 table[trow, 0].configure(value=dashboard)
-                self["display"]["selected"].set(dashboard)
+                self._widgets['display']['selected'].set(dashboard)
                 self.current_dashboard = dashboard
 
-            dboard = self.dashboard_handler.get_dashboard(dashboard)
+            db_config = self.config[dashboard]
 
             table[trow, 2].configure(text=url.get())
-            dboard["url"] = url.get()
-            if state.get() == "active":
-                if status.get() == "inactive":
-                    table[trow, 3].configure(text="")
+            db_config['url'] = url.get()
+            if state.get() == 'active':
+                if status.get() == 'inactive':
+                    table[trow, 3].configure(text='')
                 else:
                     table[trow, 3].configure(text=status.get())
             else:
                 table[trow, 3].configure(text=state.get())
-            dboard["state"] = state.get()
+            db_config['state'] = state.get()
 
             for key, value in self.config.items(dashboard):
-                if key not in ("url", "state", "status"):
-                    dboard[key] = w[key].get()
-
-            self.dashboard_handler.update(dashboard)
-
-    def file_cb(self, table, row, name, data):
-        """Method to handle parameters with files
-
-        Parameters
-        ----------
-        table : sw.ScrolledColumns
-            The widget displaying the table of parameters.
-        row : int
-            The row of the table.
-        name : str
-            The name of the parameter.
-        data : dict(str, str)
-            The definition of the parameter.
-        """
-        multiple = data["nargs"] != "a single value"
-
-        filetypes = [
-            ("MOL", "*.mol"),
-            ("MOL", "*.mol2"),
-            ("SDF", "*.sdf"),
-            ("XYZ", "*.xyz"),
-            ("CIF", "*.cif"),
-            ("MMCIF", "*.mmcif"),
-            ("All files", "*"),
-        ]
-        filename = tk.filedialog.askopenfilename(filetypes=filetypes, multiple=multiple)
-        if filename == "":
-            return
-        w = table[row, 1]
-        if multiple:
-            current = shlex.split(w.get())
-            for name in filename:
-                if name not in current:
-                    current.append(name)
-            w.delete(0, tk.END)
-            w.insert(0, " " + shlex.join(current))
-        else:
-            w.delete(0, tk.END)
-            w.insert(0, filename)
+                if key not in ('url', 'state', 'status'):
+                    db_config[key] = w[key].get()
 
-    def fill_statuses(self):
-        w = self["display"]
-        dialog = w["dialog"]
-        table = w["table"]
-
-        dialog.configure(title="Dashboards -- Updating Status")
-        progress = ttk.Progressbar(
-            dialog.interior(),
-            orient=tk.HORIZONTAL,
-            maximum=table.nrows + 1,
-            mode="determinate",
-            value=1,
-        )
-        progress.grid(sticky=tk.EW)
+            self.save_configuration()
 
-        for row in range(table.nrows):
-            current_status = table[row, 3].cget("text")
-            if current_status != "inactive":
-                table[row, 3].configure(text="...")
-                table.update()
-                dashboard = table[row, 1].cget("text")
-                status = self.dashboard_handler.get_dashboard(dashboard).status()
-                table[row, 3].configure(text=status)
-            progress.step()
-            table.update()
-        progress.destroy()
-        dialog.configure(title="Dashboards")
+    def check_status_cb(self):
+        """Helper for checking the status of a dashboard."""
+        w = self._widgets['edit dashboard']
+        dashboard = w['dashboard']
+        status = self.status(dashboard)
+        w['status'].set(status)
 
     def fit_dialog(self, dialog):
         """Resize and fit the dialog to the current contents and the
         constraint of the window.
         """
-        logger.debug("Entering fit_dialog")
+        logger.debug('Entering fit_dialog')
 
-        widget = self["display"]["table"].interior()
-        logger.debug("  widget = {}".format(widget))
+        widget = self._widgets['display']['table'].interior()
+        logger.debug('  widget = {}'.format(widget))
         widget.update_idletasks()
 
         frame = dialog.interior()
         frame.update_idletasks()
         width = frame.winfo_width()
         height = frame.winfo_height()
         sw = frame.winfo_screenwidth()
         sh = frame.winfo_screenheight()
 
         logger.debug(
-            "  frame wxh = {} x {}, screen = {} x {}".format(width, height, sw, sh)
+            '  frame wxh = {} x {}, screen = {} x {}'.format(
+                width, height, sw, sh
+            )
         )
 
         mw = frame.winfo_reqwidth()
         mh = frame.winfo_reqheight()
-        logger.debug("  frame requested = {} x {}".format(mw, mh))
+        logger.debug('  frame requested = {} x {}'.format(mw, mh))
 
         # Need to handle scrolledtable using its inside frame
         ww = widget.winfo_width()
         hh = widget.winfo_height()
         w = widget.winfo_reqwidth()
         h = widget.winfo_reqheight()
-        logger.debug("  table wxh = {} x {}, requested = {} x {}".format(ww, hh, w, h))
+        logger.debug(
+            '  table wxh = {} x {}, requested = {} x {}'.format(ww, hh, w, h)
+        )
         h += 20  # Add a bit of space...
         if w > mw:
             mw = w
         if h > mh:
             mh = h
         if ww > width:
             width = ww
@@ -575,250 +678,137 @@
             width = int(0.9 * sw)
         if height < mh:
             height = mh
         height += 70
         if height > 0.9 * sh:
             height = int(0.9 * sh)
 
-        dialog.geometry("{}x{}".format(width, height))
+        dialog.geometry('{}x{}'.format(width, height))
 
     def get_all_status(self, show_progress=True, master=None):
         """Get the status of all the dashboards.
 
-        Parameters
-        ----------
+        Parameter
+        ---------
         show_progress : Boolean, optional
             Show a dialog with progress, default is True
         """
-        dashboards = self.dashboard_handler.dashboards
         if show_progress:
             dialog = tk.Toplevel(master=master)
             dialog.focus_set()  # set focus on the ProgressWindow
             dialog.grab_set()  # make a modal window
             dialog.transient(master)  # show only one window in the task bar
 
-            dialog.title("Getting Status of Dashboards")
+            dialog.title(u'Getting Status of Dashboards')
             dialog.resizable(False, False)  # window is not resizable
             # dialog.close gets fired when the window is destroyed
             # dialog.protocol(u'WM_DELETE_WINDOW', dialog.close)
-            dialog.geometry("400x200+200+200")
+            dialog.geometry('400x200+200+200')
             # cancel progress when <Escape> key is pressed
             # dialog.bind(u'<Escape>', self.close)
 
             progress = ttk.Progressbar(
                 dialog,
                 orient=tk.HORIZONTAL,
-                length=len(dashboards) + 1,
-                maximum=len(dashboards),
-                mode="determinate",
-                value=1,
+                length=len(self.dashboards) + 1,
+                maximum=len(self.dashboards),
+                mode='determinate',
+                value=1
             )
             progress.grid(ipady=20, sticky=tk.NSEW)
-            label = ttk.Label(dialog, text="Dashboard")
+            label = ttk.Label(dialog, text='Dashboard')
             label.grid()
             dialog.rowconfigure(0, minsize=30)
             dialog.columnconfigure(0, weight=1)
             dialog.update_idletasks()
             dialog.after(50)
 
         result = []
-        for dashboard in dashboards:
+        for dashboard in self.dashboards:
             if show_progress:
-                label.configure({"text": dashboard})
+                label.configure({'text': dashboard})
                 dialog.update_idletasks()
                 dialog.after(50)
             status = self.status(dashboard)
             result.append((dashboard, status))
             if show_progress:
                 progress.step()
-                label.configure({"text": dashboard})
+                label.configure({'text': dashboard})
                 dialog.update_idletasks()
                 dialog.after(50)
 
         if show_progress:
             master.focus_set()
             dialog.destroy()
 
         return result
 
-    def handle_add_dialog(self, result):
-        """Handle the dialog to add a dashboard to the list."""
-        w = self["add"]
-        dialog = w["dialog"]
-        if result is None or result == "Cancel":
-            dialog.deactivate(result)
-        else:
-            name = w["name"].get()
-            url = w["url"].get()
-            protocol = w["protocol"].get()
 
-            if name in self.config:
-                messagebox.showwarning(
-                    "Duplicate name",
-                    (
-                        "There is already a dashboard called '{}'\n"
-                        "Use a different name."
-                    ).format(name),
-                )
-                return
-
-            dialog.deactivate(result)
-
-            # Now add to the configuration
-            self.dashboard_handler.add_dashboard(name, url, protocol)
-
-            # And reset the list in the dashboard combobox
-            c = self["dashboard"]
-            c.combobox.config({"value": self.dashboard_handler.dashboards})
-            c.set(name)
-        dialog.destroy()
-        del self["add"]
-
-    def handle_dialog(self, result):
-        """Handle the submit dialog being completed."""
-        if result is None or result == "Cancel":
-            self.dialog.deactivate(None)
-        else:
-            w = self
-            self.dialog.deactivate(
-                {
-                    "project": w["project"].get(),
-                    "title": w["title"].get(),
-                    "dashboard": w["dashboard"].get(),
-                    "description": w["description"].get(1.0, tk.END).strip("\n"),
-                }
-            )
+if __name__ == "__main__":
+    import configargparse
+    import logging
+
+    logger = logging.getLogger(__name__)
+    parser = configargparse.ArgParser(
+        auto_env_var_prefix='',
+        default_config_files=[
+            '/etc/seamm/seamm.ini',
+            '~/.seamm/seamm.ini',
+        ],
+        description='Submit a SEAMM job to a dashboard'
+    )
+
+    parser.add_argument(
+        '--seamm-configfile',
+        is_config_file=True,
+        default=None,
+        help='a configuration file to override others'
+    )
+    parser.add_argument(
+        "-v",
+        "--verbose",
+        dest="verbose_count",
+        action="count",
+        default=0,
+        help="increases log verbosity for each occurence."
+    )
+
+    # Parse the configuration
+    args, unknown = parser.parse_known_args()
+
+    # Set up logging level to WARNING by default, going more verbose
+    # for each new -v, to INFO and then DEBUG and finally ALL with 3 -v's
+
+    numeric_level = max(3 - args.verbose_count, 0) * 10
+    logging.basicConfig(level=numeric_level)
+
+    # Initialize Tk
+    root = tk.Tk()
+    Pmw.initialise(root)
+
+    # s = ttk.Style()
+    # # print("Themes: " + str(s.theme_names()))
+    # rb = ttk.Progressbar()
+    # pprint.pprint(rb.configure())
+    # print('Label style: ' + rb['style'])
+    # class_ = rb.winfo_class()
+    # print('Label class: ' + class_)
+    # pprint.pprint(s.layout(class_))
+    # # pprint.pprint(s.element_options('Label'))
+    # # pprint.pprint(s.element_options('Label.border'))
+    # # s.configure("Border.TLabel", relief='ridge', anchor=tk.W, padding=5)
+
+    # Create the object
+    job_handler = TkJobHandler(root=root)
+
+    do_it = ttk.Button(
+        root, text='Submit...', command=job_handler.submit_with_dialog
+    )
+    do_it.grid(sticky=tk.EW)
+
+    status = ttk.Button(
+        root, text='Dashboards...', command=job_handler.display_dashboards
+    )
+    status.grid(row=1, sticky=tk.EW)
 
-    def handle_dashboard_dialog(self, result):
-        """Handle the dialog to add a dashboard to the list."""
-        w = self["display"]
-        dialog = w["dialog"]
-        dashboard = w["selected"].get()
-        if result is None or result == "Cancel":
-            dialog.deactivate(None)
-        elif result == "Edit":
-            self.edit_cb(dashboard)
-        elif result == "Remove":
-            self.remove_cb(dashboard)
-        else:
-            dialog.deactivate(None)
-
-    def project_cb(self, event=None):
-        """Handle a change in the project since it might be asking for adding a project
-        in which case prompt for the new project's name, create it, and sleect it in the
-        widget.
-        """
-        w = self
-        project = w["project"].get()
-        if project == "-- Create new project --":
-            result = simpledialog.askstring("Add Project", "Project name:")
-            if result is not None and result != "":
-                # Add the project
-                dashboard = w["dashboard"].get()
-                if self.dashboard_handler.add_project(dashboard, result):
-                    pass
-            self.dashboard_cb()
-            w["project"].set(result)
-
-    def reset_title(self):
-        self["title"].set(self._flowchart.metadata["title"])
-
-    def clear_title(self):
-        self["title"].set("")
-
-    def reset_description(self):
-        self["description"].delete("1.0", "end")
-        self["description"].insert("1.0", self._flowchart.metadata["description"])
-
-    def clear_description(self):
-        self["description"].delete("1.0", "end")
-
-    def submit_with_dialog(self, flowchart):
-        """
-        Allow the user to choose the dashboard and other parameters,
-        and submit the job as requested.
-
-        Parameters
-        ----------
-        flowchart : seamm.Flowchart
-            The flowchart to use.
-
-        Returns
-        -------
-        job_id : integer
-            The id of the submitted job.
-        """
-        self._flowchart = flowchart
-        if self.dialog is None:
-            title = flowchart.metadata["title"]
-            description = flowchart.metadata["description"]
-            self.create_submit_dialog(title=title, description=description)
-
-        value = self._variable_value
-
-        # Find any Parameter steps.
-        parameter_steps = []
-        step = flowchart.get_node("1")
-        while step:
-            if step.step_type == "control-parameters-step":
-                parameter_steps.append(step)
-            step = step.next()
-
-        if len(parameter_steps) == 0:
-            # Remove the parameter section
-            self["parameters label"].grid_forget()
-            self["parameters"].grid_forget()
-            d = self.dialog.interior()
-            d.rowconfigure(6, weight=0)
-        else:
-            self["parameters label"].grid(row=6, column=0, columnspan=2, sticky=tk.W)
-            table = self["parameters"]
-            table.clear()
-            table.grid(row=7, column=0, columnspan=2, sticky=tk.NSEW)
-            frame = table.interior()
-            d = self.dialog.interior()
-            d.rowconfigure(7, weight=1)
-            row = 0
-            for step in parameter_steps:
-                variables = step.parameters["variables"]
-                for name, data in variables.value.items():
-                    table[row, 0] = name
-                    if name not in value or value[name] is None:
-                        value[name] = data["default"]
-                    entry = ttk.Entry(frame)
-                    entry.insert(0, value[name])
-                    table[row, 1] = entry
-                    table[row, 1].grid(sticky=tk.EW)
-                    if data["type"] == "file":
-                        button = tk.Button(
-                            frame,
-                            text="...",
-                            command=(
-                                lambda t=table, r=row, n=name, d=data: self.file_cb(
-                                    t, r, n, d
-                                )
-                            ),
-                        )
-                        table[row, 2] = button
-                    table[row, 3] = data["help"]
-                    row += 1
-            frame.columnconfigure(1, weight=1)
-
-        # Post the dialog
-        result = self.dialog.activate(geometry="centerscreenfirst")
-
-        if result is not None:
-            if len(parameter_steps) == 0:
-                value = {}
-            else:
-                # Get the variable values
-                table = self["parameters"]
-                for row in range(table.nrows):
-                    name = table[row, 0].cget("text")
-                    value[name] = table[row, 1].get()
-
-            dashboard_name = result.pop("dashboard")
-            dashboard = self.dashboard_handler.get_dashboard(dashboard_name)
-            job_id = dashboard.submit(flowchart, values=value, **result)
-            return job_id
-        else:
-            return None
+    # Enter the event loop
+    root.mainloop()
```

### Comparing `seamm-2023.4.8/seamm/tk_join_node.py` & `seamm-220.8.3/seamm/tk_start_node.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,52 +1,68 @@
 # -*- coding: utf-8 -*-
 
-"""A node to join the flow in a flowchart"""
+"""The start node in a flowchart"""
 
-import logging
 import seamm
 
-logger = logging.getLogger(__name__)
 
-
-class TkJoin(seamm.TkNode):
-    """The Tk-based graphical representation of a joining node"""
+class TkStartNode(seamm.TkNode):
+    """The Tk-based graphical representation of a Start node"""
 
     anchor_points = {
-        "n": (0, -0.5),
-        "s": (0, 0.5),
-        "e": (0.5, 0.0),
-        "w": (-0.5, 0.0),
+        's': (0, 0.5),
+        'e': (0.5, 0.0),
+        'w': (-0.5, 0.0),
     }
 
     def __init__(
-        self, tk_flowchart=None, node=None, canvas=None, x=120, y=20, w=10, h=10
+        self,
+        tk_flowchart=None,
+        node=None,
+        canvas=None,
+        x=150,
+        y=50,
+        w=200,
+        h=50
     ):
-        """Initialize a node
+        '''Initialize a node
 
         Keyword arguments:
-        """
+        '''
         super().__init__(
-            tk_flowchart=tk_flowchart, node=node, canvas=canvas, x=x, y=y, w=w, h=h
+            tk_flowchart=tk_flowchart,
+            node=node,
+            canvas=canvas,
+            x=x,
+            y=y,
+            w=w,
+            h=h
         )
 
+    def right_click(self, event):
+        """At the moment, since we shouldn't delete the start node
+        there is nothing to do here.
+        """
+
+        pass
+
     def draw(self):
         """Draw the node on the given canvas, making it visible"""
-        # Remove any graphics items
-        self.undraw()
 
         # the outline
         x0 = self.x - self.w / 2
         x1 = x0 + self.w
         y0 = self.y - self.h / 2
         y1 = y0 + self.h
-        self.border = self.canvas.create_oval(
+        self._border = self.canvas.create_oval(
             x0,
             y0,
             x1,
             y1,
-            tags=[self.tag, "type=outline"],
-            fill="black",
+            tags=[self.tag, 'type=outline'],
+            fill='white',
         )
 
-        for direction, edge in self.connections():
-            edge.move()
+        # the label in the middle
+        self.title_label = self.canvas.create_text(
+            self.x, self.y, text=self.title, tags=[self.tag, 'type=title']
+        )
```

### Comparing `seamm-2023.4.8/seamm/tk_node.py` & `seamm-220.8.3/seamm/tk_node.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,775 +1,762 @@
 # -*- coding: utf-8 -*-
 
-"""The base class for Tk nodes (steps) in the GUI for flowcharts."""
-
 import collections.abc
 import copy
 import logging
 import json
 import Pmw
 import seamm
-from seamm_util import default_units
 import seamm_widgets as sw
 import tkinter as tk
 import tkinter.ttk as ttk
+"""A graphical node using Tk on a canvas"""
 
 logger = logging.getLogger(__name__)
 
 
 class TkNode(collections.abc.MutableMapping):
-    """The base class for Tk nodes (steps) in the GUI for flowcharts.
-
-    Parameters
-    ----------
-    tk_flowchart : seamm.TkFlowchart
-        The graphical flowchart this step is in.
-    node : seamm.Node
-        The non-graphical node this corresponds to.
-    node_type : "simple", "loop"
-        The type of node on the graph. "simple" has an in and out arrow. "loop" has
-        three arrows.
-    canvas: tkinter.Canvas
-        The Canvas widget that this node is drawn on.
-    x: int
-        The x-coordinate the drawing for the node on the canvas.
-    y: int
-        The y-coordinate of the drawing for the node on the canvas.
-    w: int
-        The width of the drawing for the node on the canvas.
-    h: int
-        The height of the drawing for the node on the canvas.
-    my_logger : logging.Logger, optional
-        The logger to use. Defaults to the global one defined in the module.
-
-    Fields
-    ------
-    border
-    canvas
-    dialog : tkinter.Toplevel
-        The dialog for editing the parameters.
-    flowchart
-    h
-    logger : logging.Logger
-        The logger for debug & warning output.
-    node : seamm.Node
-        The non-graphical node corresponding to this graphical one.
-    node_type : enum("simple", "loop")
-        The type of the node from the point of connectivity.
-    popup_menu : tkinter.Menu
-        The popup menu used for right-clicks.
-    selected
-    tag
-    title
-    title_label : tkinter.ttk.Label
-        The label for the title of the step on the display.
-    tk_flowchart : seamm.TkFlowchart
-        The Tk Flowchart that contains this step.
-    tk_subflowchart : seamm.TkFlowchart
-        The sub flowchart is if this step contains one.
-    w
-    x
-    y
-    uuid
-
-    Notes
-    -----
-    The state is held in the corresponding non-graphical node, `self.node`. Many of
-    the properties are thin-wrappers to the same property of the non-graphical node.
-    """
+    """The abstract base class for all Tk-based nodes"""
 
     anchor_points = {
-        "s": (+0.00, +0.50),
-        "sse": (+0.25, +0.50),
-        "se": (+0.50, +0.50),
-        "ese": (+0.50, +0.25),
-        "e": (+0.50, +0.00),
-        "ene": (+0.50, -0.25),
-        "ne": (+0.50, -0.50),
-        "nne": (+0.25, -0.50),
-        "n": (+0.00, -0.50),
-        "nnw": (-0.25, -0.50),
-        "nw": (-0.50, -0.50),
-        "wnw": (-0.50, -0.25),
-        "w": (-0.50, +0.00),
-        "wsw": (-0.50, +0.25),
-        "sw": (-0.50, +0.50),
-        "ssw": (-0.25, +0.50),
+        's': (+0.00, +0.50),
+        'sse': (+0.25, +0.50),
+        'se': (+0.50, +0.50),
+        'ese': (+0.50, +0.25),
+        'e': (+0.50, +0.00),
+        'ene': (+0.50, -0.25),
+        'ne': (+0.50, -0.50),
+        'nne': (+0.25, -0.50),
+        'n': (+0.00, -0.50),
+        'nnw': (-0.25, -0.50),
+        'nw': (-0.50, -0.50),
+        'wnw': (-0.50, -0.25),
+        'w': (-0.50, +0.00),
+        'wsw': (-0.50, +0.25),
+        'sw': (-0.50, +0.50),
+        'ssw': (-0.25, +0.50)
     }
 
     def __init__(
         self,
         tk_flowchart=None,
         node=None,
-        node_type="simple",
+        node_type='simple',
         canvas=None,
         x=None,
         y=None,
         w=None,
         h=None,
         my_logger=logger,
+        keyword_metadata=None,
+        keywords=None
     ):
         """Initialize a node
 
         Keyword arguments:
         """
-        self._border = None
-        self._selected = False
-        self._tmp = None
-        self._canvas = None
-
-        self.canvas = canvas
-
-        self.dialog = None
         self.logger = my_logger
-        self.node = node
-        self.node_type = node_type
-        self.popup_menu = None
-        self._tables = None  # Temporary list of all tables up to an including this node
-        self.title_label = None
         self.tk_flowchart = tk_flowchart
         self.tk_subflowchart = None
+        self.node = node
+        self._keyword_metadata = keyword_metadata
+        self.toplevel = None
+        self.canvas = canvas
 
         if self.node is not None:
             if self.node.x is None:
                 self.node.x = x
             if self.node.y is None:
                 self.node.y = y
             if self.node.w is None:
                 self.node.w = w
             if self.node.h is None:
                 self.node.h = h
 
+        self.node_type = node_type
+
+        self._border = None
+        self.title_label = None
+        self._selected = False
+        self.popup_menu = None
+        self._tmp = None
+        self.dialog = None
+        self.previous_grab = None
+
         # Widget information
         self._widget = {}
         self.tk_var = {}
         self.results_widgets = None
 
-        # Because the default for saving properties in the database is True
-        # we need to initialize the results to include them by default
-        if self.node.parameters is not None and "results" in self.node.parameters:
-            self.initialize_results()
-
     def __hash__(self):
-        """Provide a unique key to make iterable."""
+        """Make iterable!"""
         return self.node.uuid
 
     def __eq__(self, other):
-        """Test for equality (identity) with another node."""
-        return self.__class__ == other.__class__ and self.__hash__() == other.__hash__()
+        return (
+            self.__class__ == other.__class__ and
+            self.__hash__() == other.__hash__()
+        )
 
     # Provide dict like access to the widgets to make
     # the code cleaner
 
     def __getitem__(self, key):
-        """Allow [] access to the widgets."""
+        """Allow [] access to the widgets!"""
         return self._widget[key]
 
     def __setitem__(self, key, value):
-        """Allow [key] access to set a widget."""
+        """Allow x[key] access to the data"""
         self._widget[key] = value
 
     def __delitem__(self, key):
-        """Allow deletion of widgets."""
+        """Allow deletion of keys"""
         if key in self._widget:
             self._widget[key].destroy()
         del self._widget[key]
 
     def __iter__(self):
-        """Allow iteration over the widgets"""
+        """Allow iteration over the object"""
         return iter(self._widget)
 
     def __len__(self):
-        """Provide the nmber of widgets, for e.g. len() command."""
+        """The len() command"""
         return len(self._widget)
 
     @property
-    def border(self):
-        """The border of the picture in the flowchart"""
-        return self._border
-
-    @border.setter
-    def border(self, value):
-        self._border = value
+    def uuid(self):
+        """The uuid of the node"""
+        return self.node.uuid
 
     @property
-    def canvas(self):
-        """The canvas for drawing the node"""
-        return self._canvas
+    def title(self):
+        """The title to display"""
+        return self.node.title
 
-    @canvas.setter
-    def canvas(self, value):
-        self._canvas = value
+    @title.setter
+    def title(self, value):
+        self.node.title = value
+        if self.title_label is not None:
+            self.canvas.itemconfigure(self.title_label, text=value)
+
+    @property
+    def tag(self):
+        """The string representation of the uuid of the node"""
+        return self.node.tag
 
     @property
     def flowchart(self):
         """The flowchart object"""
         return self.node.flowchart
 
     @flowchart.setter
     def flowchart(self, value):
         """The flowchart object"""
         self.node.flowchart = value
 
     @property
+    def x(self):
+        """The x-position of the center of the graphical node"""
+        return self.node.x
+
+    @x.setter
+    def x(self, value):
+        self.node.x = value
+
+    @property
+    def y(self):
+        """The y-position of the center of the graphical node"""
+        return self.node.y
+
+    @y.setter
+    def y(self, value):
+        self.node.y = value
+
+    @property
+    def w(self):
+        """The width of the graphical node"""
+        return self.node.w
+
+    @w.setter
+    def w(self, value):
+        self.node.w = value
+
+    @property
     def h(self):
         """The height of the graphical node"""
         return self.node.h
 
     @h.setter
     def h(self, value):
         self.node.h = value
 
+    def set_uuid(self):
+        self.node.set_uuid()
+
+    def connections(self):
+        """Return a list of all the incoming and outgoing edges
+        for this node, giving the anchor points and other node
+        """
+
+        return self.tk_flowchart.edges(self)
+
     @property
     def selected(self):
         """Whether I am selected or not"""
         return self._selected
 
     @selected.setter
     def selected(self, value):
         self._selected = value
         if value:
-            self.canvas.itemconfigure(self.border, outline="red")
+            self.canvas.itemconfigure(self.border, outline='red')
         else:
-            self.canvas.itemconfigure(self.border, outline="black")
+            self.canvas.itemconfigure(self.border, outline='black')
 
     @property
-    def tag(self):
-        """The string representation of the uuid of the node"""
-        return self.node.tag
+    def canvas(self):
+        """The canvas for drawing the node"""
+        return self._canvas
+
+    @canvas.setter
+    def canvas(self, value):
+        if value:
+            self.toplevel = value.winfo_toplevel()
+        self._canvas = value
 
     @property
-    def title(self):
-        """The title to display"""
-        return self.node.title
+    def border(self):
+        """The border of the picture in the flowchart"""
+        return self._border
 
-    @title.setter
-    def title(self, value):
-        self.node.title = value
-        if self.title_label is not None:
-            self.canvas.itemconfigure(self.title_label, text=value)
+    @border.setter
+    def border(self, value):
+        self._border = value
 
-    @property
-    def w(self):
-        """The width of the graphical node"""
-        return self.node.w
+    def draw(self):
+        """Draw the node on the given canvas, making it visible"""
 
-    @w.setter
-    def w(self, value):
-        self.node.w = value
+        # Remove any graphics items
+        self.undraw()
 
-    @property
-    def x(self):
-        """The x-position of the center of the graphical node"""
-        return self.node.x
+        # the outline
+        x0 = self.x - self.w / 2
+        x1 = x0 + self.w
+        y0 = self.y - self.h / 2
+        y1 = y0 + self.h
+        self._border = self.canvas.create_rectangle(
+            x0,
+            y0,
+            x1,
+            y1,
+            tags=[self.tag, 'type=outline'],
+            fill='white',
+        )
 
-    @x.setter
-    def x(self, value):
-        self.node.x = value
+        # the label in the middle
+        self.title_label = self.canvas.create_text(
+            self.x, self.y, text=self.title, tags=[self.tag, 'type=title']
+        )
 
-    @property
-    def y(self):
-        """The y-position of the center of the graphical node"""
-        return self.node.y
+        for direction, edge in self.connections():
+            edge.move()
 
-    @y.setter
-    def y(self, value):
-        self.node.y = value
+    def undraw(self):
+        """Remove all of our visual components
+        """
 
-    @property
-    def uuid(self):
-        """The uuid of the node"""
-        return self.node.uuid
+        self.canvas.delete(self.tag)
+
+    def move(self, deltax, deltay):
+        if self._tmp is None:
+            self._tmp = self.connections()
+
+        self.x += deltax
+        self.y += deltay
+
+        self.canvas.move(self.tag, deltax, deltay)
+
+        for connection in self._tmp:
+            direction, edge = connection
+            edge.move()
+
+    def end_move(self, deltax, deltay):
+        self.move(deltax, deltay)
+        self._x0 = None
+        self._y0 = None
+        self._tmp = None
+
+    def right_click(self, event):
+        """Do whatever needs to be done for a right-click on this
+        item in the flowchart.
+
+        Subclasses should override this as appropriate! The menu
+        created in this base method is accessible in subclasses
+        which should make it relatively easy to override.
+        """
+
+        if self.popup_menu is not None:
+            self.popup_menu.destroy()
+
+        self.popup_menu = tk.Menu(self.canvas, tearoff=0)
+        self.popup_menu.add_command(
+            label="Delete",
+            command=lambda: self.tk_flowchart.remove_node(self)
+        )
+
+        if type(self) is seamm.tk_node.TkNode:
+            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
+
+    def double_click(self, event):
+        """Do whatever needs to be done for a double-click on this
+        item in the flowchart.
+
+        Subclasses should override this as appropriate!
+        """
+
+        self.edit()
 
     def activate(self):
-        """Add active handles at the anchor points and change the cursor."""
+        """Add active handles at the anchor points and change the
+        cursor
+        """
 
-        self.canvas.delete(self.tag + " && type=anchor")
+        self.canvas.delete(self.tag + ' && type=anchor')
         for pt, x, y in self.anchor_point("all"):
             x0 = x - 2
             y0 = y - 2
             x1 = x + 2
             y1 = y + 2
             self.canvas.create_oval(
                 x0,
                 y0,
                 x1,
                 y1,
-                fill="red",
-                outline="red",
-                tags=[self.tag, "type=anchor", "anchor=" + pt],
+                fill='red',
+                outline='red',
+                tags=[self.tag, 'type=anchor', 'anchor=' + pt]
             )
 
-    def activate_anchor_point(self, point, halo):
-        """Put a marker on the anchor point to indicate it is under the cursor."""
+    def deactivate(self):
+        """Remove the decorations indicate the anchor points
+        """
 
-        x, y = self.anchor_point(point)
-        self.canvas.create_oval(
-            x - halo,
-            y - halo,
-            x + halo,
-            y + halo,
-            fill="red",
-            outline="red",
-            tags=[self.tag, "type=active_anchor", "anchor=" + point],
-        )
+        self.canvas.delete(self.tag + ' && type=anchor')
+        self.canvas.delete(self.tag + ' && type=active_anchor')
 
     def anchor_point(self, anchor="all"):
         """Where the anchor points are located. If "all" is given
         a dictionary of all points is returned"""
 
         if anchor == "all":
             result = []
             for pt in type(self).anchor_points:
                 a, b = type(self).anchor_points[pt]
-                result.append((pt, int(self.x + a * self.w), int(self.y + b * self.h)))
+                result.append(
+                    (pt, int(self.x + a * self.w), int(self.y + b * self.h))
+                )
             return result
 
         if anchor in type(self).anchor_points:
             a, b = type(self).anchor_points[anchor]
             return (int(self.x + a * self.w), int(self.y + b * self.h))
 
-        raise NotImplementedError("anchor position '{}' not implemented".format(anchor))
+        raise NotImplementedError(
+            "anchor position '{}' not implemented".format(anchor)
+        )
 
     def check_anchor_points(self, x, y, halo):
         """If the position x, y is within halo or one of the anchor points
         activate the point and return the name of the anchor point
         """
 
         points = []
         for direction, edge in self.connections():
-            if direction == "out":
+            if direction == 'out':
                 points.append(edge.anchor1)
             else:
                 points.append(edge.anchor2)
 
         for point, x0, y0 in self.anchor_point():
-            if x >= x0 - halo and x <= x0 + halo and y >= y0 - halo and y <= y0 + halo:
+            if x >= x0 - halo and x <= x0 + halo and \
+               y >= y0 - halo and y <= y0 + halo:
                 if point in points:
                     return None
                 else:
                     return point
         return None
 
-    def connections(self):
-        """Return a list of all the incoming and outgoing edges
-        for this node, giving the anchor points and other node
+    def is_inside(self, x, y, halo=0):
+        """Return a boolean indicating whether the point x, y is inside
+        this node, using halo as a size around the point
         """
+        if x < self.x - self.w / 2 - halo:
+            return False
+        if x > self.x + self.w / 2 + halo:
+            return False
 
-        return self.tk_flowchart.edges(self)
+        if y < self.y - self.h / 2 - halo:
+            return False
+        if y > self.y + self.h / 2 + halo:
+            return False
+
+        return True
+
+    def activate_anchor_point(self, point, halo):
+        """Put a marker on the anchor point to indicate it is
+        active
+        """
+
+        x, y = self.anchor_point(point)
+        self.canvas.create_oval(
+            x - halo,
+            y - halo,
+            x + halo,
+            y + halo,
+            fill='red',
+            outline='red',
+            tags=[self.tag, 'type=active_anchor', 'anchor=' + point]
+        )
+
+    def remove_edge(self, edge):
+        """Remove a given edge, or all edges if 'all' is given
+        """
+
+        if isinstance(edge, str) and edge == 'all':
+            for direction, obj in self.connections():
+                self.remove_edge(obj)
+        else:
+            self.tk_flowchart.graph.remove_edge(
+                edge.node1, edge.node2, edge.edge_type, edge.edge_subtype
+            )
+
+    def edit(self):
+        """Present a dialog for editing this step's parameters.
+
+        Subclasses can override this.
+        """
+        # Create the dialog if it doesn't exist
+        if self.dialog is None:
+            self.create_dialog()
+            # After full creation, reset the dialog. This may do nothing,
+            # or may layout the widgets, but can only be done after fully
+            # creating the dialog.
+            self.reset_dialog()
+            # And resize the dialog to fit...
+            self.fit_dialog()
+
+        # And put it on-screen, the first time centered. If it contains
+        # a subflowchart, save it so it can be restored on a 'Cancel'
+        if self.tk_subflowchart is not None:
+            self.tk_subflowchart.push()
+
+        self.dialog.activate(geometry='centerscreenfirst')
 
     def create_dialog(
         self,
-        title="Edit step",
-        widget="frame",
+        title='Edit step',
+        widget='frame',
         results_tab=False,
     ):
         """Create the base dialog for editing the parameters for a step.
 
-        Parameters
-        ----------
-        title : str
-            The title of the dialog.
-        widget : enum
-            Whether to use a simple dialog ("frame") or use a notebook ("notebook").
-        results_tab : bool
-            **OBSOLETE** Not longer used.
+        At the moment I have removed the Help button.
         """
-        toplevel = self.canvas.winfo_toplevel()
-
-        self.logger.debug("Create dialog in tk_node base class")
+        self.logger.debug('Create dialog in tk_node base class')
         self.dialog = Pmw.Dialog(
-            toplevel,
-            buttons=("OK", "Cancel"),
-            master=toplevel,
+            self.toplevel,
+            buttons=('OK', 'Cancel'),
+            master=self.toplevel,
             title=title,
-            command=self.handle_dialog,
+            command=self.handle_dialog
         )
         self.dialog.withdraw()
 
-        results_tab = (
-            self.node.parameters is not None and "results" in self.node.parameters
-        )
-
-        if widget == "notebook" or results_tab or "keywords" in self.node.metadata:
+        if widget == 'frame':
+            # Create a frame to hold everything
+            frame = ttk.Frame(self.dialog.interior())
+            frame.pack(expand=tk.YES, fill=tk.BOTH)
+            self['frame'] = frame
+            return frame
+        elif (
+            widget == 'notebook' or results_tab or
+            self._keyword_metadata is not None
+        ):
             # A tabbed notebook
             notebook = ttk.Notebook(self.dialog.interior())
-            notebook.pack(side="top", fill=tk.BOTH, expand=tk.YES)
-            self["notebook"] = notebook
+            notebook.pack(side='top', fill=tk.BOTH, expand=tk.YES)
+            self['notebook'] = notebook
 
             # Main frame holding the widgets
             frame = ttk.Frame(notebook)
-            self["frame"] = frame
-            notebook.add(frame, text="Parameters", sticky=tk.NW)
-        elif widget == "frame":
-            # Create a frame to hold everything
-            frame = ttk.Frame(self.dialog.interior())
-            frame.pack(expand=tk.YES, fill=tk.BOTH)
-            self["frame"] = frame
-            return frame
+            self['frame'] = frame
+            notebook.add(frame, text='Parameters', sticky=tk.NW)
 
         if results_tab:
             # Second tab for results if requested
-            rframe = self["results frame"] = ttk.Frame(notebook)
-            notebook.add(rframe, text="Results", sticky=tk.NSEW)
+            rframe = self['results frame'] = ttk.Frame(notebook)
+            notebook.add(rframe, text='Results', sticky=tk.NSEW)
 
             # Shortcut for parameters
             P = self.node.parameters
 
-            if "create tables" in P:
-                var = self.tk_var["create tables"] = tk.IntVar()
-                if P["create tables"].value == "yes":
-                    var.set(1)
-                else:
-                    var.set(0)
-                self["create tables"] = ttk.Checkbutton(
-                    rframe, text="Create tables if needed", variable=var
-                )
-                self["create tables"].grid(row=0, column=0, sticky=tk.W)
+            var = self.tk_var['create tables'] = tk.IntVar()
+            if P['create tables'].value == 'yes':
+                var.set(1)
+            else:
+                var.set(0)
+            self['create tables'] = ttk.Checkbutton(
+                rframe, text='Create tables if needed', variable=var
+            )
+            self['create tables'].grid(row=0, column=0, sticky=tk.W)
 
-            self["results"] = sw.ScrolledColumns(
+            self['results'] = sw.ScrolledColumns(
                 rframe,
                 columns=[
-                    "Result",
-                    "Save in database",
-                    "",
-                    "Save in variable named",
-                    "Save in table",
-                    "as Column name",
-                    "Units",
-                ],
+                    'Result',
+                    'Save',
+                    'Variable name',
+                    'In table',
+                    'Column name',
+                ]
             )
-            self["results"].grid(row=1, column=0, sticky=tk.NSEW)
+            self['results'].grid(row=1, column=0, sticky=tk.NSEW)
             rframe.columnconfigure(0, weight=1)
             rframe.rowconfigure(1, weight=1)
 
-        if "keywords" in self.node.metadata:
+        if self._keyword_metadata is not None:
             # Next tab to handle adding keywords manually
-            self.logger.debug("Adding the keyword tab")
-            kframe = self["add_to_input"] = ttk.Frame(notebook)
-            notebook.add(kframe, text="Add to input", sticky=tk.NSEW)
-            self["keywords"] = sw.Keywords(
+            self.logger.debug('Adding the keyword tab')
+            kframe = self['add_to_input'] = ttk.Frame(notebook)
+            notebook.add(kframe, text='Add to input', sticky=tk.NSEW)
+            self['keywords'] = sw.Keywords(
                 kframe,
-                metadata=self.node.metadata["keywords"],
-                keywords=self.node.parameters["extra keywords"].value,
+                metadata=self._keyword_metadata,
+                keywords=self.node.parameters['extra keywords'].value
             )
-            self["keywords"].pack(expand="yes", fill="both")
+            self['keywords'].pack(expand='yes', fill='both')
 
         return frame
 
-    def deactivate(self):
-        """Remove the decorations that indicate active anchor points"""
-
-        self.canvas.delete(self.tag + " && type=anchor")
-        self.canvas.delete(self.tag + " && type=active_anchor")
-
-    def default_edge_subtype(self):
-        """Return the default subtype of the edge. Usually this is ''
-        but for nodes with two or more edges leaving them, such as a loop, this
-        method will return an appropriate default for the current edge. For
-        example, by default the first edge emanating from a loop-node is the
-        'loop' edge; the second, the 'exit' edge.
-
-        A return value of 'too many' indicates that the node exceeds the number
-        of allowed exit edges.
-        """
-
-        # how many outgoing edges are there?
-        n_edges = len(self.tk_flowchart.edges(self, direction="out"))
-
-        self.logger.debug("node.default_edge_label, n_edges = {}".format(n_edges))
-
-        if n_edges == 0:
-            return "next"
-        else:
-            return "too many"
-
-    def double_click(self, event):
-        """Handle a double-click on the node.
-
-        This method raises the dialog to edit the parameters.  Subclasses should
-        override this as appropriate!
-        """
-
-        self.edit()
-
-    def draw(self):
-        """Draw the node on the given canvas, making it visible"""
-        # Remove any graphics items
-        self.undraw()
+    def setup_results(self, properties, calculation='energy'):
+        """Layout the results tab of the dialog"""
+        results = self.node.parameters['results'].value
 
-        # the outline
-        x0 = self.x - self.w / 2
-        x1 = x0 + self.w
-        y0 = self.y - self.h / 2
-        y1 = y0 + self.h
-        self.border = self.canvas.create_rectangle(
-            x0,
-            y0,
-            x1,
-            y1,
-            tags=[self.tag, "type=outline"],
-            fill="white",
-        )
+        self.results_widgets = []
+        table = self['results']
+        frame = table.interior()
 
-        # the label in the middle
-        self.title_label = self.canvas.create_text(
-            self.x, self.y, text=self.title, tags=[self.tag, "type=title"]
-        )
+        row = 0
+        for key, entry in properties.items():
+            if 'calculation' not in entry:
+                continue
+            if calculation not in entry['calculation']:
+                continue
+            if 'dimensionality' not in entry:
+                continue
+            if entry['dimensionality'] != 'scalar':
+                continue
 
-        for direction, edge in self.connections():
-            edge.move()
+            widgets = []
+            widgets.append(key)
 
-    def edit(self):
-        """Present a dialog for editing this step's parameters.
+            table.cell(row, 0, entry['description'])
 
-        Subclasses can override this.
-        """
-        # Create the dialog if it doesn't exist
-        if self.dialog is None:
-            self.create_dialog()
-            # After full creation, reset the dialog. This may do nothing,
-            # or may layout the widgets, but can only be done after fully
-            # creating the dialog.
-            self.reset_dialog()
-            # And resize the dialog to fit...
-            self.fit_dialog()
+            # variable
+            var = self.tk_var[key] = tk.IntVar()
+            var.set(0)
+            w = ttk.Checkbutton(frame, variable=var)
+            table.cell(row, 1, w)
+            widgets.append(w)
+            e = ttk.Entry(frame, width=15)
+            e.insert(0, key.lower())
+            table.cell(row, 2, e)
+            widgets.append(e)
 
-        # And put it on-screen, the first time centered. If it contains
-        # a subflowchart, save it so it can be restored on a 'Cancel'
-        if self.tk_subflowchart is not None:
-            self.tk_subflowchart.push()
+            if key in results:
+                if 'variable' in results[key]:
+                    var.set(1)
+                    e.delete(0, tk.END)
+                    e.insert(0, results[key]['variable'])
 
-        self.dialog.activate(geometry="centerscreenfirst")
+            # table
+            w = ttk.Combobox(frame, width=10)
+            table.cell(row, 3, w)
+            widgets.append(w)
+            e = ttk.Entry(frame, width=15)
+            e.insert(0, key.lower())
+            table.cell(row, 4, e)
+            widgets.append(e)
 
-    def end_move(self, deltax, deltay):
-        """End moving the node on the canvas.
+            if key in results:
+                if 'table' in results[key]:
+                    w.set(results[key]['table'])
+                    e.delete(0, tk.END)
+                    e.insert(0, results[key]['column'])
 
-        Parameters
-        ----------
-        deltax : int
-            The number of pixels to move in the x-direction.
-        deltay : int
-            The number of pixels to move in the y-direction.
-        """
-        self.move(deltax, deltay)
-        self._x0 = None
-        self._y0 = None
-        self._tmp = None
+            self.results_widgets.append(widgets)
+            row += 1
 
     def fit_dialog(self):
         """Resize and fit the dialog to the current contents and the
         constraint of the window.
         """
-        self.logger.debug("Entering fit_dialog")
-        frame = self["frame"]
+        self.logger.debug('Entering fit_dialog')
+        frame = self['frame']
         frame.update_idletasks()
         width = frame.winfo_width()
         height = frame.winfo_height()
         sw = frame.winfo_screenwidth()
         sh = frame.winfo_screenheight()
 
         self.logger.debug(
-            "  frame wxh = {} x {}, screen = {} x {}".format(width, height, sw, sh)
+            '  frame wxh = {} x {}, screen = {} x {}'.format(
+                width, height, sw, sh
+            )
         )
 
         mw = 0
         mh = 0
-        if "notebook" in self:
-            for tab in self["notebook"].tabs():
+        if 'notebook' in self:
+            for tab in self['notebook'].tabs():
                 widget = frame.nametowidget(tab)
                 widget.update_idletasks()
-                self.logger.debug("  widget = {}".format(widget))
+                self.logger.debug('  widget = {}'.format(widget))
                 ww = widget.winfo_width()
                 hh = widget.winfo_height()
                 w = widget.winfo_reqwidth()
                 h = widget.winfo_reqheight()
                 self.logger.debug(
-                    "  tab {} wxh = {} x {}, requested = {} x {}".format(
+                    '  tab {} wxh = {} x {}, requested = {} x {}'.format(
                         tab, ww, hh, w, h
                     )
                 )
                 if w > mw:
                     mw = w
                 if h > mh:
                     mh = h
                 if ww > width:
                     width = ww
                 if hh > height:
                     height = hh
             # Need to do results again using the inside of the scrolled table..
-            if "results" in self:
-                widget = self["results"].interior()
-                self.logger.debug("  widget = {}".format(widget))
+            if 'results' in self:
+                widget = self['results'].interior()
+                self.logger.debug('  widget = {}'.format(widget))
                 widget.update_idletasks()
                 ww = widget.winfo_width()
                 hh = widget.winfo_height()
                 w = widget.winfo_reqwidth()
                 h = widget.winfo_reqheight()
                 self.logger.debug(
-                    "  tab {} wxh = {} x {}, requested = {} x {}".format(
+                    '  tab {} wxh = {} x {}, requested = {} x {}'.format(
                         tab, ww, hh, w, h
                     )
                 )
                 if w > mw:
                     mw = w
                 if h > mh:
                     mh = h
                 if ww > width:
                     width = ww
                 if hh > height:
                     height = hh
         else:
             mw = frame.winfo_reqwidth()
             mh = frame.winfo_reqheight()
-            self.logger.debug("  frame requested = {} x {}".format(mw, mh))
+            self.logger.debug('  frame requested = {} x {}'.format(mw, mh))
 
         if width < mw:
             width = mw
         width += 70
         if width + 70 > 0.9 * sw:
             width = int(0.9 * sw)
         if height < mh:
             height = mh
         height += 70
         if height > 0.9 * sh:
             height = int(0.9 * sh)
 
-        self.dialog.geometry("{}x{}".format(width, height))
-
-    def from_flowchart(self, tk_flowchart=None, flowchart=None):
-        """Recreate the graphics from the non-graphical flowchart.
-        Only used in nodes that contain flowchart"""
+        self.dialog.geometry('{}x{}'.format(width, height))
 
-        if self.tk_subflowchart is None or self.node.subflowchart is None:
-            return
-
-        self.tk_subflowchart.clear()
-
-        # Add all the non-graphical nodes, making copies so that
-        # when the flowchart is cleared our objects still exist
-        translate = {}
-        for node in self.node.subflowchart:
-            extension = node.extension
-            if extension is None:
-                # Start node
-                translate[node] = self.tk_subflowchart.get_node("1")
-            else:
-                new_node = copy.copy(node)
-                self.logger.debug("creating {} node".format(extension))
-                plugin = self.tk_subflowchart.plugin_manager.get(extension)
-                self.logger.debug("  plugin object: {}".format(plugin))
-                tk_node = plugin.create_tk_node(
-                    tk_flowchart=self.tk_subflowchart,
-                    canvas=self.tk_subflowchart.canvas,
-                    node=new_node,
-                )
-                translate[node] = tk_node
-                tk_node.from_flowchart()
-                self.tk_subflowchart.graph.add_node(tk_node)
-                tk_node.draw()
+    def reset_dialog(self, widget=None):
+        """Reset the layout of the dialog as needed for the parameters.
 
-        # And the edges
-        for edge in self.node.subflowchart.edges():
-            node1 = translate[edge.node1]
-            node2 = translate[edge.node2]
-            attr = {}
-            for key in edge:
-                if key not in ("node1", "node2"):
-                    attr[key] = edge[key]
-            self.tk_subflowchart.add_edge(node1, node2, **attr)
+        In this base class this does nothing. Override as needed in the
+        subclasses derived from this class.
+        """
+        pass
 
     def handle_dialog(self, result):
-        """Do the right thing when the dialog is closed."""
-        if result is None or result == "Cancel":
+        """Do the right thing when the dialog is closed.
+        """
+        if result is None or result == 'Cancel':
             self.dialog.deactivate(result)
 
             # If there is a subflowchart, revert to the saved copy
             if self.tk_subflowchart is not None:
                 self.tk_subflowchart.pop()
 
             # Reset the results widgets if they exist
             if self.results_widgets is not None:
-                results = self.node.parameters["results"]["value"]
-                self.logger.debug("Resetting results on Cancel")
+                results = self.node.parameters['results']['value']
+                self.logger.debug('Resetting results on Cancel')
                 if self.logger.isEnabledFor(logging.DEBUG):
-                    self.logger.debug("  results dict\n---------")
+                    self.logger.debug('  results dict\n---------')
                     for key, item in results.items():
                         self.logger.debug(key)
                         self.logger.debug(
                             json.dumps(results[key], sort_keys=True, indent=3)
                         )
 
-                for (
-                    key,
-                    w_property,
-                    w_check,
-                    w_variable,
-                    w_table,
-                    w_column,
-                    w_units,
-                ) in self.results_widgets:  # noqa: E501
-                    self.logger.debug("  key: {}".format(key))
+                for key, w_check, w_variable, w_table, w_column in self.results_widgets:  # noqa: E501
+                    self.logger.debug('  key: {}'.format(key))
                     w_variable.delete(0, tk.END)
-                    if w_table is not None:
-                        w_table.delete(0, tk.END)
-                    if w_column is not None:
-                        w_column.delete(0, tk.END)
+                    w_table.delete(0, tk.END)
+                    w_column.delete(0, tk.END)
                     if key in results:
                         tmp = results[key]
                         self.logger.debug(
-                            "  key dict\n---------\n"
-                            + json.dumps(tmp, sort_keys=True, indent=3)
-                            + "\n-----"
+                            '  key dict\n---------\n' +
+                            json.dumps(tmp, sort_keys=True, indent=3) +
+                            '\n-----'
                         )
-                        if "variable" in tmp:
+                        if 'variable' in tmp:
                             self.tk_var[key].set(1)
-                            w_variable.insert(0, tmp["variable"])
+                            w_variable.insert(0, tmp['variable'])
                         else:
                             self.tk_var[key].set(0)
-                            w_variable.insert(0, key.lower().replace(" ", "_"))
+                            w_variable.insert(0, key.lower())
 
-                        if w_table is not None:
-                            if "table" in tmp:
-                                w_table.insert(0, tmp["table"])
-                                w_column.insert(0, tmp["column"])
-                            else:
-                                w_table.set("")
-                                w_column.insert(0, key.lower().replace("_", " "))
-
-                        if w_property is not None:
-                            if "property" in tmp:
-                                self.tk_var["property " + key]["value"].set(1)
-                            else:
-                                self.tk_var["property " + key]["value"].set(0)
-
-                        if w_units is not None:
-                            if "units" in tmp:
-                                w_units.set(tmp["units"])
+                        if 'table' in tmp:
+                            w_table.insert(0, tmp['table'])
+                            w_column.insert(0, tmp['column'])
+                        else:
+                            w_table.set('')
+                            w_column.insert(0, key.lower())
                     else:
-                        self.logger.debug("  resetting widgets")
+                        self.logger.debug('  resetting widgets')
                         self.tk_var[key].set(0)
-                        w_variable.insert(0, key.lower().replace(" ", "_"))
-                        if w_column is not None:
-                            w_column.insert(0, key.lower().replace("_", " "))
+                        w_variable.insert(0, key.lower())
+                        w_column.insert(0, key.lower())
 
             # Reset the parameters, if any
             if self.node.parameters is not None:
                 self.node.parameters.reset_widgets()
 
             # Reset any keywords
-            if "keywords" in self:
-                self["keywords"].reset()
+            if 'keywords' in self:
+                self['keywords'].reset()
 
             # Reset the layout to make sure it is correct
             self.reset_dialog()
 
-        elif result == "Help":
+        elif result == 'Help':
             self.help()
-        elif result == "OK":
+        elif result == 'OK':
             self.dialog.deactivate(result)
 
             # Capture the parameters from the widgets
             if self.node.parameters is not None:
                 self.node.parameters.set_from_widgets()
 
             # If there is a subflowchart, throw the saved copy away
@@ -778,368 +765,154 @@
 
             # Get what results to store, if the results tab exists
             if self.results_widgets is not None:
                 # Shortcut for parameters
                 P = self.node.parameters
 
                 # and from the results tab...
-                if "create tables" in P:
-                    if self.tk_var["create tables"].get():
-                        P["create tables"].value = "yes"
-                    else:
-                        P["create tables"].value = "no"
+                if self.tk_var['create tables'].get():
+                    P['create tables'].value = 'yes'
+                else:
+                    P['create tables'].value = 'no'
 
-                results = P["results"].value = {}
-                for (
-                    key,
-                    w_property,
-                    w_check,
-                    w_variable,
-                    w_table,
-                    w_column,
-                    w_units,
-                ) in self.results_widgets:  # noqa: E501
-                    tmp = {}
-                    if self.tk_var[key].get():
-                        tmp["variable"] = w_variable.get()
-                        if w_units is not None:
-                            tmp["units"] = w_units.get()
-                    if w_table is not None:
-                        table = w_table.get()
-                        if table != "":
-                            tmp["table"] = table
-                            tmp["column"] = w_column.get()
-                            if w_units is not None:
-                                tmp["units"] = w_units.get()
-                    if w_property is not None:
-                        if self.tk_var["property " + key]["value"].get() == 1:
-                            tmp["property"] = self.tk_var["property " + key]["key"]
-                        elif "property" in tmp:
-                            del tmp["property"]
-                    if len(tmp) > 0:
-                        results[key] = tmp
+                results = P['results'].value = {}
+                for key, w_check, w_variable, w_table, w_column in self.results_widgets:  # noqa: E501
 
+                    if self.tk_var[key].get():
+                        tmp = results[key] = dict()
+                        tmp['variable'] = w_variable.get()
+                    table = w_table.get()
+                    if table != '':
+                        if key not in results:
+                            tmp = results[key] = dict()
+                        tmp['table'] = table
+                        tmp['column'] = w_column.get()
             # And any keywords
-            if "keywords" in self:
+            if 'keywords' in self:
                 P = self.node.parameters
-                P["extra keywords"].value = self["keywords"].get_keywords()
-                self["keywords"].keywords = P["extra keywords"].value
+                P['extra keywords'].value = self['keywords'].get_keywords()
+                self['keywords'].keywords = P['extra keywords'].value
         else:
             self.dialog.deactivate(result)
-            raise RuntimeError("Don't recognize dialog result '{}'".format(result))
+            raise RuntimeError(
+                "Don't recognize dialog result '{}'".format(result)
+            )
 
     def help(self):
         """Base class for presenting help, does nothing.
 
         Subclasses should override this.
         """
         pass
 
-    def initialize_results(self):
-        """Initialize the results if empty.
-
-        When the GUI for the step is first created the `results` parameter is empty.
-        However the default is to save properties to the database, so they need to
-        be put into the `results` parameter.
-        """
-        if self.node.parameters is None or "results" not in self.node.parameters:
-            return
-
-        results = self.node.parameters["results"].value
-        if len(results) == 0:
-            for key, entry in self.node.metadata["results"].items():
-                if "dimensionality" not in entry:
-                    continue
-                if self.node.calculation is not None and "calculation" in entry:
-                    if self.node.calculation not in entry["calculation"]:
-                        continue
-                if self.node.method is not None and "methods" in entry:
-                    if self.node.method not in entry["methods"]:
-                        continue
-
-                if "property" in entry:
-                    results[key] = {"property": entry["property"]}
-
-    @staticmethod
-    def is_expr(value):
-        """Return whether the value is an expression or constant.
-
-        Parameters
-        ----------
-        value : str
-            The value to test
-
-        Returns
-        -------
-        bool
-           True for an expression, False otherwise.
-        """
-        return len(value) > 0 and value[0] == "$"
-
-    def is_inside(self, x, y, halo=0):
-        """Return a boolean indicating whether the point x, y is inside
-        this node, using halo as a size around the point
-        """
-        if x < self.x - self.w / 2 - halo:
-            return False
-        if x > self.x + self.w / 2 + halo:
-            return False
-
-        if y < self.y - self.h / 2 - halo:
-            return False
-        if y > self.y + self.h / 2 + halo:
-            return False
-
-        return True
-
-    def move(self, deltax, deltay):
-        """Move the node on the canvas.
-
-        Parameters
-        ----------
-        deltax : int
-            The number of pixels to move in the x-direction.
-        deltay : int
-            The number of pixels to move in the y-direction.
-        """
-        if self._tmp is None:
-            self._tmp = self.connections()
-
-        self.x += deltax
-        self.y += deltay
-
-        self.canvas.move(self.tag, deltax, deltay)
-
-        for connection in self._tmp:
-            direction, edge = connection
-            edge.move()
-
-    def next_anchor(self):
-        """Return where the next node should be positioned. The default is
-        <gap> below the 's' anchor point.
-        """
-
-        return "s"
-
-    def remove_edge(self, edge):
-        """Remove a given edge, or all edges if 'all' is given"""
-
-        if isinstance(edge, str) and edge == "all":
-            for direction, obj in self.connections():
-                self.remove_edge(obj)
-        else:
-            self.tk_flowchart.graph.remove_edge(
-                edge.node1, edge.node2, edge.edge_type, edge.edge_subtype
-            )
-
-    def reset_dialog(self, widget=None):
-        """Reset the layout of the dialog as needed for the parameters.
-
-        In this base class this does nothing. Override as needed in the
-        subclasses derived from this class.
-        """
-        pass
-
-    def right_click(self, event):
-        """Respond to a right-click by posting the popup menu.
-
-        This method provides a popup menu with a **delete** command.
-
-        Subclasses should override or extend this as appropriate! The menu created in
-        this base method is accessible in subclasses which should make it easy to
-        override.
-        """
-
-        if self.popup_menu is not None:
-            self.popup_menu.destroy()
-
-        self.popup_menu = tk.Menu(self.canvas, tearoff=0)
-        self.popup_menu.add_command(
-            label="Delete",
-            command=lambda node=self: self.tk_flowchart.remove_node(node),
-        )
-
-        if type(self) is seamm.tk_node.TkNode:
-            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
-
-    def setup_results(self):
-        """Layout the results tab of the dialog"""
-        if self.node.parameters is None or "results" not in self.node.parameters:
-            return
-
-        results = self.node.parameters["results"].value
-
-        # Find what tables are in use.
-        tables = set()
-        for tmp in results.values():
-            if "table" in tmp:
-                tables.add(tmp["table"])
-        self.node.tables = sorted(tables)
-
-        tables.update(self.node.existing_tables())
-        self._tables = sorted(tables)
-        del tables
-
-        self.results_widgets = []
-        table = self["results"]
-        table.clear()
-        frame = table.interior()
-
-        row = 0
-        for key, entry in self.node.metadata["results"].items():
-            if "dimensionality" not in entry:
-                continue
-            if self.node.calculation is not None and "calculation" in entry:
-                if self.node.calculation not in entry["calculation"]:
-                    continue
-            if self.node.method is not None and "methods" in entry:
-                if self.node.method not in entry["methods"]:
-                    continue
-
-            widgets = []
-            widgets.append(key)
-
-            table.cell(row, 0, entry["description"])
-
-            # Property for DB. default is save
-            if "property" in entry:
-                var = self.tk_var["property " + key] = {
-                    "value": tk.IntVar(),
-                    "key": entry["property"],
-                }
-                if key in results and "property" in results[key]:
-                    var["value"].set(1)
-                else:
-                    var["value"].set(0)
-
-                w = ttk.Checkbutton(frame, variable=var["value"])
-                table.cell(row, 1, w)
-                widgets.append(w)
-            else:
-                widgets.append(None)
-
-            # variable
-            var = self.tk_var[key] = tk.IntVar()
-            var.set(0)
-            w = ttk.Checkbutton(frame, variable=var)
-            table.cell(row, 2, w)
-            widgets.append(w)
-            e = ttk.Entry(frame, width=15)
-            e.insert(0, key.lower().replace(" ", "_"))
-            table.cell(row, 3, e)
-            widgets.append(e)
-
-            if key in results:
-                if "variable" in results[key]:
-                    var.set(1)
-                    e.delete(0, tk.END)
-                    e.insert(0, results[key]["variable"])
-
-            if entry["dimensionality"] == "scalar":
-                # table
-                w = ttk.Combobox(frame, width=10, values=["", *self._tables])
-                table.cell(row, 4, w)
-                widgets.append(w)
-                w.bind("<<ComboboxSelected>>", self._table_cb)
-                w.bind("<Return>", self._table_cb)
-                w.bind("<FocusOut>", self._table_cb)
-                e = ttk.Entry(frame, width=15)
-                e.insert(0, key.lower().replace("_", " "))
-                table.cell(row, 5, e)
-                widgets.append(e)
-
-                if key in results:
-                    if "table" in results[key]:
-                        w.set(results[key]["table"])
-                        e.delete(0, tk.END)
-                        e.insert(0, results[key]["column"])
-            else:
-                widgets.append(None)
-                widgets.append(None)
-
-            # And units....
-            if "units" in entry and entry["units"] != "":
-                units = entry["units"]
-                w = ttk.Combobox(frame, width=10)
-                widgets.append(w)
-                table.cell(row, 6, w)
-                w.config(values=[*default_units(units), ""])
-                w.set(units)
-                if key in results and "units" in results[key]:
-                    w.set(results[key]["units"])
-            else:
-                widgets.append(None)
-
-            self.results_widgets.append(widgets)
-            row += 1
-
-    def set_uuid(self):
-        """Set the unique id of the node to a new uuid."""
-        self.node.set_uuid()
-
     def to_dict(self):
         """Serialize to a dict"""
         data = {
-            "x": self._x,
-            "y": self._y,
-            "w": self._w,
-            "h": self._h,
+            'x': self._x,
+            'y': self._y,
+            'w': self._w,
+            'h': self._h,
         }
 
         return data
 
-    def _table_cb(self, event):
-        "Update the list of tables as needed."
-        table = event.widget.get()
-
-        if table.strip() == "":
-            return
-
-        if table not in self._tables:
-            self._tables.append(table)
-            self._tables = sorted(self._tables)
-            self.node.tables.append(table)
-            self.node.tables.sort()
-
-            for (
-                key,
-                w_property,
-                w_check,
-                w_variable,
-                w_table,
-                w_column,
-                w_units,
-            ) in self.results_widgets:
-                if w_table is not None:
-                    w_table.configure(values=["", *self._tables])
-
     def update_flowchart(self, tk_flowchart=None, flowchart=None):
         """Update the nongraphical flowchart. Only used in nodes that contain
         flowcharts"""
-        if self.tk_subflowchart is None or self.node.subflowchart is None:
+        if tk_flowchart is None or flowchart is None:
             return
 
         # Make sure there is nothing in the flowchart
-        self.node.subflowchart.clear(all=True)
+        flowchart.clear(all=True)
 
         # Add all the non-graphical nodes, making copies so that
         # when the flowchart is cleared our objects still exist
         translate = {}
-        for node in self.tk_subflowchart:
-            translate[node] = self.node.subflowchart.add_node(copy.copy(node.node))
+        for node in tk_flowchart:
+            translate[node] = flowchart.add_node(copy.copy(node.node))
             node.update_flowchart()
 
         # And the edges
-        for edge in self.tk_subflowchart.edges():
+        for edge in tk_flowchart.edges():
             attr = {}
             for key in edge:
-                if key not in ("node1", "node2", "edge_type", "edge_subtype", "canvas"):
+                if key not in (
+                    'node1', 'node2', 'edge_type', 'edge_subtype', 'canvas'
+                ):
                     attr[key] = edge[key]
             node1 = translate[edge.node1]
             node2 = translate[edge.node2]
-            self.node.subflowchart.add_edge(
+            flowchart.add_edge(
                 node1, node2, edge.edge_type, edge.edge_subtype, **attr
             )
 
-    def undraw(self):
-        """Remove all the visual components from the canvas."""
-        self.canvas.delete(self.tag)
+    def from_flowchart(self, tk_flowchart=None, flowchart=None):
+        """Recreate the graphics from the non-graphical flowchart.
+        Only used in nodes that contain flowchart"""
+
+        if tk_flowchart is None or flowchart is None:
+            return
+
+        tk_flowchart.clear()
+
+        # Add all the non-graphical nodes, making copies so that
+        # when the flowchart is cleared our objects still exist
+        translate = {}
+        for node in flowchart:
+            extension = node.extension
+            if extension is None:
+                # Start node
+                translate[node] = tk_flowchart.get_node('1')
+            else:
+                new_node = copy.copy(node)
+                self.logger.debug('creating {} node'.format(extension))
+                plugin = tk_flowchart.plugin_manager.get(extension)
+                self.logger.debug('  plugin object: {}'.format(plugin))
+                tk_node = plugin.create_tk_node(
+                    tk_flowchart=tk_flowchart,
+                    canvas=tk_flowchart.canvas,
+                    node=new_node
+                )
+                translate[node] = tk_node
+                tk_node.from_flowchart()
+                tk_flowchart.graph.add_node(tk_node)
+                tk_node.draw()
+
+        # And the edges
+        for edge in flowchart.edges():
+            node1 = translate[edge.node1]
+            node2 = translate[edge.node2]
+            attr = {}
+            for key in edge:
+                if key not in ('node1', 'node2'):
+                    attr[key] = edge[key]
+            tk_flowchart.add_edge(node1, node2, **attr)
+
+    def default_edge_subtype(self):
+        """Return the default subtype of the edge. Usually this is ''
+        but for nodes with two or more edges leaving them, such as a loop, this
+        method will return an appropriate default for the current edge. For
+        example, by default the first edge emanating from a loop-node is the
+        'loop' edge; the second, the 'exit' edge.
+
+        A return value of 'too many' indicates that the node exceeds the number
+        of allowed exit edges.
+        """
+
+        # how many outgoing edges are there?
+        n_edges = len(self.tk_flowchart.edges(self, direction='out'))
+
+        self.logger.debug(
+            'node.default_edge_label, n_edges = {}'.format(n_edges)
+        )
+
+        if n_edges == 0:
+            return "next"
+        else:
+            return "too many"
+
+    def next_anchor(self):
+        """Return where the next node should be positioned. The default is
+        <gap> below the 's' anchor point.
+        """
+
+        return 's'
```

### Comparing `seamm-2023.4.8/seamm/tk_split_node.py` & `seamm-220.8.3/seamm/tk_join_node.py`

 * *Files 22% similar despite different names*

```diff
@@ -1,48 +1,65 @@
 # -*- coding: utf-8 -*-
 
-"""A node to split the flow in a flowchart"""
+"""A node to join the flow in a flowchart"""
 
 import logging
 import seamm
 
 logger = logging.getLogger(__name__)
 
 
-class TkSplit(seamm.TkNode):
-    """The Tk-based graphical representation of a splitting node"""
+class TkJoin(seamm.TkNode):
+    """The Tk-based graphical representation of a joining node"""
 
     anchor_points = {
-        "n": (0, 0),
-        "s": (0, 1),
-        "e": (0.5, 0.5),
-        "w": (-0.5, 0.5),
+        'n': (0, -0.5),
+        's': (0, 0.5),
+        'e': (0.5, 0.0),
+        'w': (-0.5, 0.0),
     }
 
     def __init__(
-        self, tk_flowchart=None, node=None, canvas=None, x=120, y=20, w=10, h=10
+        self,
+        tk_flowchart=None,
+        node=None,
+        canvas=None,
+        x=120,
+        y=20,
+        w=10,
+        h=10
     ):
-        """Initialize a node
+        '''Initialize a node
 
         Keyword arguments:
-        """
-        logger.debug("Creating TkSplit, {} {} {} {} {}".format(node, x, y, w, h))
+        '''
         super().__init__(
-            tk_flowchart=tk_flowchart, node=node, canvas=canvas, x=x, y=y, w=w, h=h
+            tk_flowchart=tk_flowchart,
+            node=node,
+            canvas=canvas,
+            x=x,
+            y=y,
+            w=w,
+            h=h
         )
 
     def draw(self):
         """Draw the node on the given canvas, making it visible"""
+        # Remove any graphics items
+        self.undraw()
 
         # the outline
         x0 = self.x - self.w / 2
         x1 = x0 + self.w
-        y0 = self.y
+        y0 = self.y - self.h / 2
         y1 = y0 + self.h
-        self.border = self.canvas.create_oval(
+        self._border = self.canvas.create_oval(
             x0,
             y0,
             x1,
             y1,
-            tags=[self.tag, "type=outline"],
-            fill="black",
+            tags=[self.tag, 'type=outline'],
+            fill='black',
         )
+
+        for direction, edge in self.connections():
+            edge.move()
```

### Comparing `seamm-2023.4.8/seamm/variables.py` & `seamm-220.8.3/seamm/variables.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,25 +1,24 @@
 # -*- coding: utf-8 -*-
 
-"""
-A dictionary-like object for holding variables accessible to the
-executing flowchart.
-"""
-
 import collections.abc
 import logging
 import seamm
 import pprint
+"""A dictionary-like object for holding variables accessible to the
+executing flowchart.
+"""
 
 logger = logging.getLogger(__name__)
 # Module level variable to be used in other modules
 flowchart_variables = None
 
 
 class Variables(collections.abc.MutableMapping):
+
     def __init__(self, **kwargs):
         self._data = dict(**kwargs)
 
     def __getitem__(self, key):
         """Allow [] access to the dictionary!"""
         return self._data[key]
 
@@ -65,108 +64,97 @@
         """Return the value of the variable or expression if it is an
         expression, i.e. starts with a $ and optionally has braces around the
         variable name.
 
         If it is not a variable, return the original string unchanged
         """
 
-        if isinstance(string, str) and string[0] == "$":
+        if isinstance(string, str) and string[0] == '$':
             expression = self.filter_expression(string)
 
             result = eval(expression, seamm.flowchart_variables._data)
             return result
         else:
             return string
 
     def set_variable(self, variable, value):
         """Set the value of the variable. The variable may be a simple string
         or start with a $ and optionally have braces around it, i.e.
 
             <name>
             $<name>
-
         or
-
             ${<name>}
-
         """
 
         name = self.variable(variable)
         self._data[name] = value
 
     def get_variable(self, variable):
         """Get the value of the variable. The variable may be a simple string
         or start with a $ and optionally have braces around it, i.e.
 
             <name>
             $<name>
-
         or
-
             ${<name>}
-
         """
 
         name = self.variable(variable)
         if name not in self._data:
-            raise RuntimeError("Workspace variable '{}' does not exist.".format(name))
+            raise RuntimeError(
+                "Workspace variable '{}' does not exist.".format(name)
+            )
         return self._data[name]
 
     def exists(self, variable):
         """Return whether a variable exists. The variable may be specified
         as a simple string or start with a $ and optionally have braces
         around it, i.e.
 
             <name>
             $<name>
-
         or
-
             ${<name>}
-
         """
 
         return self.variable(variable) in self._data
 
     def delete(self, variable):
         """Return whether a variable exists. The variable may be specified
         as a simple string or start with a $ and optionally have braces
         around it, i.e.
 
             <name>
             $<name>
-
         or
-
             ${<name>}
-
         """
 
         name = self.variable(variable)
         if name in self._data:
             del self._data[name]
 
     def variable(self, string):
         """Return the name of a variable. The variable may be specified
         as a simple string or start with a $ and optionally have braces
         around it, i.e.
 
             <string>
             $<string>
-
         or
-
             ${<string>}
-
         """
 
-        if string[0] == "$":
-            if string[1] == "{":
-                if string[-1] != "}":
-                    raise RuntimeError("'" + string + "'is not a valid string name")
+        if string[0] == '$':
+            if string[1] == '{':
+                if string[-1] != '}':
+                    raise RuntimeError(
+                        "'" + string + "'is not a valid string name"
+                    )
                 else:
                     return string[2:-1]
             else:
                 return string[1:]
         else:
             return string
 
@@ -176,43 +164,43 @@
         with braces, i.e. ${name}.
 
         This method filters out the variable markers, respecting
         quoted string, returning a string that can be eval'ed in
         the Python interpreter.
         """
 
-        result = ""
-        state = ""
+        result = ''
+        state = ''
         for char in string:
-            if state == "in single quotes":
+            if state == 'in single quotes':
                 result += char
                 if char == "'":
-                    state = ""
-            elif state == "in double quotes":
+                    state = ''
+            elif state == 'in double quotes':
                 result += char
                 if char == '"':
-                    state = ""
-            elif state == "protected":
+                    state = ''
+            elif state == 'protected':
                 result += char
-                state = ""
-            elif state == "in variable name":
-                if char == "}":
-                    state = ""
-                elif char == "{":
+                state = ''
+            elif state == 'in variable name':
+                if char == '}':
+                    state = ''
+                elif char == '{':
                     pass
                 else:
                     result += char
             else:
-                if char == "$":
-                    state = "in variable name"
+                if char == '$':
+                    state = 'in variable name'
                 elif char == "'":
                     result += char
-                    state = "in single quotes"
+                    state = 'in single quotes'
                 elif char == '"':
                     result += char
-                    state = "in double quotes"
-                elif char == "\\":
-                    state = "protected"
+                    state = 'in double quotes'
+                elif char == '\\':
+                    state = 'protected'
                 else:
                     result += char
 
         return result
```

### Comparing `seamm-2023.4.8/setup.py` & `seamm-220.8.3/setup.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
-"""seamm
-The core of the SEAMM environment and graphical interface.
+"""
+seamm
+The core of the SEAMM environment.
 """
 
 import sys
 from setuptools import setup, find_packages
 import versioneer
 
 short_description = __doc__.split("\n")
@@ -16,15 +17,15 @@
 
 with open('README.rst') as readme_file:
     readme = readme_file.read()
 
 with open('HISTORY.rst') as history_file:
     history = history_file.read()
 
-with open('requirements.txt') as fd:
+with open('requirements_install.txt') as fd:
     requirements = fd.read()
 
 setup(
     name='seamm',
     author="Paul Saxe",
     author_email='psaxe@molssi.org',
     description=short_description[1],
@@ -61,24 +62,23 @@
 
     # Manual control if final package is compressible or not, set False to
     # prevent the .egg from being made
     # zip_safe=False,
 
     keywords='seamm',
     classifiers=[
-        'Development Status :: 5 - Production/Stable',
+        'Development Status :: 2 - Pre-Alpha',
         'Intended Audience :: Developers',
-        'Topic :: Scientific/Engineering :: Chemistry',
-        'Topic :: Scientific/Engineering :: Physics',
         ('License :: OSI Approved :: GNU Lesser General Public License v3 or '
          'later (LGPLv3+)'),
         'Natural Language :: English',
         'Programming Language :: Python :: 3 :: Only',
-        'Programming Language :: Python :: 3.8',
-        'Programming Language :: Python :: 3.9',
+        'Programming Language :: Python :: 3.5',
+        'Programming Language :: Python :: 3.6',
+        'Programming Language :: Python :: 3.7',
     ],
     entry_points={
         'console_scripts': [
             'seamm=seamm.__main__:flowchart',
             'run_flowchart=seamm.run_flowchart:run'
         ],
         'org.molssi.seamm': [
```

### Comparing `seamm-2023.4.8/tests/test_molssi_workflow.py` & `seamm-220.8.3/tests/test_molssi_workflow.py`

 * *Files identical despite different names*

