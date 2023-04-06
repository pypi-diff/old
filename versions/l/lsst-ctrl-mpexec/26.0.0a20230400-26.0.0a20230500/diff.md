# Comparing `tmp/lsst-ctrl-mpexec-26.0.0a20230400.tar.gz` & `tmp/lsst-ctrl-mpexec-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-ctrl-mpexec-26.0.0a20230400.tar", last modified: Thu Jan 26 09:56:20 2023, max compression
+gzip compressed data, was "lsst-ctrl-mpexec-26.0.0a20230500.tar", last modified: Thu Feb  2 14:08:21 2023, max compression
```

## Comparing `lsst-ctrl-mpexec-26.0.0a20230400.tar` & `lsst-ctrl-mpexec-26.0.0a20230500.tar`

### file list

```diff
@@ -1,69 +1,69 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.133480 lsst-ctrl-mpexec-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)      369 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)    35147 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-01-26 09:56:20.133480 lsst-ctrl-mpexec-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      690 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.125481 lsst-ctrl-mpexec-26.0.0a20230400/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.125481 lsst-ctrl-mpexec-26.0.0a20230400/doc/lsst.ctrl.mpexec/
--rw-r--r--   0 runner    (1001) docker     (123)     6093 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/doc/lsst.ctrl.mpexec/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (123)    18922 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/doc/lsst.ctrl.mpexec/configuring-pipetask-tasks.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1343 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/doc/lsst.ctrl.mpexec/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)      106 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/doc/lsst.ctrl.mpexec/pipetask.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3460 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.125481 lsst-ctrl-mpexec-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.125481 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/
--rw-r--r--   0 runner    (1001) docker     (123)     1044 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.129480 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/
--rw-r--r--   0 runner    (1001) docker     (123)     1044 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.129480 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/
--rw-r--r--   0 runner    (1001) docker     (123)     1276 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.129480 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/
--rw-r--r--   0 runner    (1001) docker     (123)      919 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.129480 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/cmd/
--rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/cmd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9132 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/cmd/commands.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.129480 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/opt/
--rw-r--r--   0 runner    (1001) docker     (123)      996 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/opt/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1084 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/opt/arguments.py
--rw-r--r--   0 runner    (1001) docker     (123)     6557 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/opt/optionGroups.py
--rw-r--r--   0 runner    (1001) docker     (123)    16497 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/opt/options.py
--rw-r--r--   0 runner    (1001) docker     (123)     1655 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/pipetask.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.133480 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/
--rw-r--r--   0 runner    (1001) docker     (123)     1138 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3406 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/build.py
--rw-r--r--   0 runner    (1001) docker     (123)     4086 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/cleanup.py
--rw-r--r--   0 runner    (1001) docker     (123)     3156 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/confirmable.py
--rw-r--r--   0 runner    (1001) docker     (123)     2091 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/pre_exec_init_qbb.py
--rw-r--r--   0 runner    (1001) docker     (123)     9319 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/purge.py
--rw-r--r--   0 runner    (1001) docker     (123)     8530 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/qgraph.py
--rw-r--r--   0 runner    (1001) docker     (123)     7597 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/run.py
--rw-r--r--   0 runner    (1001) docker     (123)     3796 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/run_qbb.py
--rw-r--r--   0 runner    (1001) docker     (123)     6100 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    35369 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cmdLineFwk.py
--rw-r--r--   0 runner    (1001) docker     (123)     5863 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/dataid_match.py
--rw-r--r--   0 runner    (1001) docker     (123)    11778 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/dotTools.py
--rw-r--r--   0 runner    (1001) docker     (123)     4672 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/execFixupDataId.py
--rw-r--r--   0 runner    (1001) docker     (123)     2422 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/executionGraphFixup.py
--rw-r--r--   0 runner    (1001) docker     (123)     9333 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/log_capture.py
--rw-r--r--   0 runner    (1001) docker     (123)     8635 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/mock_task.py
--rw-r--r--   0 runner    (1001) docker     (123)    26806 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/mpGraphExecutor.py
--rw-r--r--   0 runner    (1001) docker     (123)    24133 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/preExecInit.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)     4389 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/quantumGraphExecutor.py
--rw-r--r--   0 runner    (1001) docker     (123)     5449 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/reports.py
--rw-r--r--   0 runner    (1001) docker     (123)    13819 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/showInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)    13273 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/simple_pipeline_executor.py
--rw-r--r--   0 runner    (1001) docker     (123)    27884 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/singleQuantumExecutor.py
--rw-r--r--   0 runner    (1001) docker     (123)     2266 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/taskFactory.py
--rw-r--r--   0 runner    (1001) docker     (123)     5434 2023-01-26 09:56:06.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/util.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 09:56:19.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:20.133480 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-01-26 09:56:20.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2156 2023-01-26 09:56:20.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:20.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-01-26 09:56:20.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)      176 2023-01-26 09:56:20.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 09:56:20.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:19.000000 lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-01-26 09:56:20.133480 lsst-ctrl-mpexec-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.833491 lsst-ctrl-mpexec-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)      369 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)    35147 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-02-02 14:08:21.833491 lsst-ctrl-mpexec-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      690 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.825491 lsst-ctrl-mpexec-26.0.0a20230500/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.825491 lsst-ctrl-mpexec-26.0.0a20230500/doc/lsst.ctrl.mpexec/
+-rw-r--r--   0 runner    (1001) docker     (123)     6093 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/doc/lsst.ctrl.mpexec/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    18922 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/doc/lsst.ctrl.mpexec/configuring-pipetask-tasks.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1343 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/doc/lsst.ctrl.mpexec/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      106 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/doc/lsst.ctrl.mpexec/pipetask.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3460 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.825491 lsst-ctrl-mpexec-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.825491 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/
+-rw-r--r--   0 runner    (1001) docker     (123)     1044 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.829491 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/
+-rw-r--r--   0 runner    (1001) docker     (123)     1044 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.829491 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/
+-rw-r--r--   0 runner    (1001) docker     (123)     1276 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.829491 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)      919 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.829491 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/cmd/
+-rw-r--r--   0 runner    (1001) docker     (123)     1095 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/cmd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9132 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/cmd/commands.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.829491 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/opt/
+-rw-r--r--   0 runner    (1001) docker     (123)      996 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/opt/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1084 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/opt/arguments.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6557 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/opt/optionGroups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16497 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/opt/options.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1654 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/pipetask.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.833491 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/
+-rw-r--r--   0 runner    (1001) docker     (123)     1138 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3406 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/build.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4086 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/cleanup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3156 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/confirmable.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2091 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/pre_exec_init_qbb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9319 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/purge.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8530 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/qgraph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7597 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/run.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3796 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/run_qbb.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6100 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    35361 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cmdLineFwk.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5863 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/dataid_match.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11775 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/dotTools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4672 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/execFixupDataId.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2422 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/executionGraphFixup.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9329 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/log_capture.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8634 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/mock_task.py
+-rw-r--r--   0 runner    (1001) docker     (123)    26804 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/mpGraphExecutor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24130 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/preExecInit.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)     4389 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/quantumGraphExecutor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5449 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13815 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/showInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13273 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/simple_pipeline_executor.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27879 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/singleQuantumExecutor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2266 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/taskFactory.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5434 2023-02-02 14:08:07.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/util.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:08:21.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:08:21.833491 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1470 2023-02-02 14:08:21.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2156 2023-02-02 14:08:21.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:08:21.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-02-02 14:08:21.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      176 2023-02-02 14:08:21.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:08:21.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:08:21.000000 lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-02-02 14:08:21.833491 lsst-ctrl-mpexec-26.0.0a20230500/setup.cfg
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/LICENSE` & `lsst-ctrl-mpexec-26.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/PKG-INFO` & `lsst-ctrl-mpexec-26.0.0a20230500/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-mpexec
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Pipeline execution infrastructure for the Rubin Observatory LSST Science Pipelines.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_mpexec
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/README.rst` & `lsst-ctrl-mpexec-26.0.0a20230500/README.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/doc/lsst.ctrl.mpexec/CHANGES.rst` & `lsst-ctrl-mpexec-26.0.0a20230500/doc/lsst.ctrl.mpexec/CHANGES.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/doc/lsst.ctrl.mpexec/configuring-pipetask-tasks.rst` & `lsst-ctrl-mpexec-26.0.0a20230500/doc/lsst.ctrl.mpexec/configuring-pipetask-tasks.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/doc/lsst.ctrl.mpexec/index.rst` & `lsst-ctrl-mpexec-26.0.0a20230500/doc/lsst.ctrl.mpexec/index.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/pyproject.toml` & `lsst-ctrl-mpexec-26.0.0a20230500/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/__init__.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/__init__.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/__init__.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/__init__.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/cmd/__init__.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/cmd/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/cmd/commands.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/cmd/commands.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/opt/__init__.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/opt/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/opt/arguments.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/opt/arguments.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/opt/optionGroups.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/opt/optionGroups.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/opt/options.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/opt/options.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/pipetask.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/pipetask.py`

 * *Files 1% similar despite different names*

```diff
@@ -27,15 +27,14 @@
     log_level_option,
     log_tty_option,
     long_log_option,
 )
 
 
 class PipetaskCLI(LoaderCLI):
-
     localCmdPkg = "lsst.ctrl.mpexec.cli.cmd"
 
 
 @click.command(cls=PipetaskCLI, context_settings=dict(help_option_names=["-h", "--help"]))
 @log_level_option()
 @long_log_option()
 @log_file_option()
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/__init__.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/build.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/build.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/cleanup.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/cleanup.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/confirmable.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/confirmable.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/pre_exec_init_qbb.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/pre_exec_init_qbb.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/purge.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/purge.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/qgraph.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/qgraph.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/run.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/run.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/script/run_qbb.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/script/run_qbb.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cli/utils.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cli/utils.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/cmdLineFwk.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/cmdLineFwk.py`

 * *Files 2% similar despite different names*

```diff
@@ -493,37 +493,31 @@
             pipeline = Pipeline.from_uri(args.pipeline)
         else:
             pipeline = Pipeline("anonymous")
 
         # loop over all pipeline actions and apply them in order
         for action in args.pipeline_actions:
             if action.action == "add_instrument":
-
                 pipeline.addInstrument(action.value)
 
             elif action.action == "new_task":
-
                 pipeline.addTask(action.value, action.label)
 
             elif action.action == "delete_task":
-
                 pipeline.removeTask(action.label)
 
             elif action.action == "config":
-
                 # action value string is "field=value", split it at '='
                 field, _, value = action.value.partition("=")
                 pipeline.addConfigOverride(action.label, field, value)
 
             elif action.action == "configfile":
-
                 pipeline.addConfigFile(action.label, action.value)
 
             else:
-
                 raise ValueError(f"Unexpected pipeline action: {action.action}")
 
         if args.save_pipeline:
             pipeline.write_to_uri(args.save_pipeline)
 
         if args.pipeline_dot:
             pipeline2dot(pipeline, args.pipeline_dot)
@@ -808,15 +802,14 @@
                 raise ValueError("Failed to make instance of graph fixup") from exc
             if not isinstance(fixup, ExecutionGraphFixup):
                 raise ValueError("Graph fixup is not an instance of ExecutionGraphFixup class")
             return fixup
         return None
 
     def preExecInitQBB(self, task_factory: TaskFactory, args: SimpleNamespace) -> None:
-
         # Load quantum graph. We do not really need individual Quanta here,
         # but we need datastore records for initInputs, and those are only
         # available from Quanta, so load the whole thing.
         qgraph = QuantumGraph.loadUri(args.qgraph, graphID=args.qgraph_id)
         universe = qgraph.universe
 
         # Collect all init input/output dataset IDs.
@@ -851,15 +844,14 @@
         )
 
         # Save all InitOutputs, configs, etc.
         preExecInit = PreExecInitLimited(butler, task_factory)
         preExecInit.initialize(qgraph)
 
     def runGraphQBB(self, task_factory: TaskFactory, args: SimpleNamespace) -> None:
-
         # Load quantum graph.
         nodes = args.qgraph_node_id or None
         qgraph = QuantumGraph.loadUri(args.qgraph, nodes=nodes, graphID=args.qgraph_id)
 
         if qgraph.metadata is None:
             raise ValueError("QuantumGraph is missing metadata, cannot ")
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/dataid_match.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/dataid_match.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/dotTools.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/dotTools.py`

 * *Files 0% similar despite different names*

```diff
@@ -163,18 +163,16 @@
         file = open(file, "w")
         close = True
 
     print("digraph QuantumGraph {", file=file)
 
     allDatasetRefs: dict[str, str] = {}
     for taskId, taskDef in enumerate(qgraph.taskGraph):
-
         quanta = qgraph.getNodesForTask(taskDef)
         for qId, quantumNode in enumerate(quanta):
-
             # node for a task
             taskNodeName = "task_{}_{}".format(taskId, qId)
             _renderQuantumNode(taskNodeName, taskDef, quantumNode, file)
 
             # quantum inputs
             for dsRefs in quantumNode.quantum.inputs.values():
                 for dsRef in dsRefs:
@@ -250,15 +248,14 @@
 
     # The next two lines are a workaround until DM-29658 at which time metadata
     # connections should start working with the above code
     labelToTaskName = {}
     metadataNodesToLink = set()
 
     for idx, taskDef in enumerate(sorted(pipeline, key=lambda x: x.label)):
-
         # node for a task
         taskNodeName = "task{}".format(idx)
 
         # next line is workaround until DM-29658
         labelToTaskName[taskDef.label] = taskNodeName
 
         _renderTaskNode(taskNodeName, taskDef, file, None)
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/execFixupDataId.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/execFixupDataId.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/executionGraphFixup.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/executionGraphFixup.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/log_capture.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/log_capture.py`

 * *Files 2% similar despite different names*

```diff
@@ -141,44 +141,42 @@
                     logging.getLogger().removeHandler(log_handler_file)
                     log_handler_file.close()
                     if ctx.store:
                         self._ingest_log_records(quantum, taskDef.logOutputDatasetName, log_file)
                     shutil.rmtree(tmpdir, ignore_errors=True)
 
             else:
-
                 log_handler_memory = ButlerLogRecordHandler()
                 logging.getLogger().addHandler(log_handler_memory)
 
                 try:
                     with ButlerMDC.set_mdc(mdc):
                         yield ctx
                 finally:
                     # Ensure that the logs are stored in butler.
                     logging.getLogger().removeHandler(log_handler_memory)
                     if ctx.store:
                         self._store_log_records(quantum, taskDef.logOutputDatasetName, log_handler_memory)
                     log_handler_memory.records.clear()
 
         else:
-
             with ButlerMDC.set_mdc(mdc):
                 yield ctx
 
     def _store_log_records(
         self, quantum: Quantum, dataset_type: str, log_handler: ButlerLogRecordHandler
     ) -> None:
         # DatasetRef has to be in the Quantum outputs, can lookup by name.
         try:
             [ref] = quantum.outputs[dataset_type]
         except LookupError as exc:
             raise InvalidQuantumError(
                 f"Quantum outputs is missing log output dataset type {dataset_type};"
-                f" this could happen due to inconsistent options between QuantumGraph generation"
-                f" and execution"
+                " this could happen due to inconsistent options between QuantumGraph generation"
+                " and execution"
             ) from exc
 
         if self.full_butler is None:
             # If full butler is not available then we need fully
             # resolved reference for limited butler.
             if ref.id is None:
                 raise InvalidQuantumError(
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/mock_task.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/mock_task.py`

 * *Files 0% similar despite different names*

```diff
@@ -116,15 +116,14 @@
 
     def _checkMembership(self, ref: Union[List[DatasetRef], DatasetRef], inout: set) -> None:
         # docstring is inherited from the base class
         return
 
 
 class MockPipelineTaskConfig(PipelineTaskConfig, pipelineConnections=PipelineTaskConnections):
-
     failCondition: Field[str] = Field(
         dtype=str,
         default="",
         doc=(
             "Condition on DataId to raise an exception. String expression which includes attributes of "
             "quantum DataId using a syntax of daf_butler user expressions (e.g. 'visit = 123')."
         ),
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/mpGraphExecutor.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/mpGraphExecutor.py`

 * *Files 0% similar despite different names*

```diff
@@ -436,15 +436,14 @@
             `QuantumGraph` that is to be executed
         report : `Report`
             Object for reporting execution status.
         """
         successCount, totalCount = 0, len(graph)
         failedNodes: set[QuantumNode] = set()
         for qnode in graph:
-
             assert qnode.quantum.dataId is not None, "Quantum DataId cannot be None"
 
             # Any failed inputs mean that the quantum has to be skipped.
             inputNodes = graph.determineInputsToQuantumNode(qnode)
             if inputNodes & failedNodes:
                 _LOG.error(
                     "Upstream job failed for task <%s dataId=%s>, skipping this task.",
@@ -542,15 +541,14 @@
             if not taskDef.taskClass.canMultiprocess:
                 raise MPGraphExecutorError(
                     f"Task {taskDef.taskName} does not support multiprocessing; use single process"
                 )
 
         finishedCount, failedCount = 0, 0
         while jobs.pending or jobs.running:
-
             _LOG.debug("#pendingJobs: %s", len(jobs.pending))
             _LOG.debug("#runningJobs: %s", len(jobs.running))
 
             # See if any jobs have finished
             for job in jobs.running:
                 assert job.process is not None, "Process cannot be None"
                 if not job.process.is_alive():
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/preExecInit.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/preExecInit.py`

 * *Files 0% similar despite different names*

```diff
@@ -182,15 +182,15 @@
                     )
                     obj_from_store = self.butler.getDirect(init_output_ref)
                     # Types are supposed to be identical.
                     # TODO: Check that object contents is identical too.
                     if type(obj_from_store) is not type(init_output_var):
                         raise TypeError(
                             f"Stored initOutput object type {type(obj_from_store)} "
-                            f"is different  from task-generated type "
+                            "is different from task-generated type "
                             f"{type(init_output_var)} for task {taskDef}"
                         )
                 else:
                     _LOG.debug("Saving InitOutputs for task=%s key=%s", taskDef.label, name)
                     # This can still raise if there is a concurrent write.
                     self.butler.putDirect(init_output_var, init_output_ref)
 
@@ -250,15 +250,14 @@
             Raised if existing object in butler is incompatible with new data.
         """
         packages = Packages.fromSystem()
         _LOG.debug("want to save packages: %s", packages)
 
         # start transaction to rollback any changes on exceptions
         with self.transaction():
-
             old_packages, dataset_ref = self.find_packages(graph)
 
             if old_packages is not None:
                 # Note that because we can only detect python modules that have
                 # been imported, the stored list of products may be more or
                 # less complete than what we have now.  What's important is
                 # that the products that are in common have the same version.
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/quantumGraphExecutor.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/quantumGraphExecutor.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/reports.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/reports.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/showInfo.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/showInfo.py`

 * *Files 1% similar despite different names*

```diff
@@ -61,15 +61,15 @@
 
         if mat:
             pattern = mat.group(1)
             self._pattern = re.compile(fnmatch.translate(pattern))
         else:
             if pattern != pattern.lower():
                 print(
-                    f'Matching "{pattern}" without regard to case ' "(append :NOIGNORECASE to prevent this)",
+                    f'Matching "{pattern}" without regard to case (append :NOIGNORECASE to prevent this)',
                     file=self.stream,
                 )
             self._pattern = re.compile(fnmatch.translate(pattern), re.IGNORECASE)
 
     def write(self, showStr: str) -> None:
         # Strip off doc string line(s) and cut off at "=" for string matching
         matchStr = showStr.rstrip().split("\n")[-1].split("=")[0]
@@ -232,15 +232,14 @@
 
         tasks = util.filterTasks(pipeline, taskName)
         if not tasks:
             raise ValueError(f"Pipeline has no tasks named {taskName}")
 
         found = False
         for taskDef in tasks:
-
             config = taskDef.config
 
             # Look for any matches in the config hierarchy for this name
             for nmatch, thisName in enumerate(fnmatch.filter(config.names(), pattern)):
                 if nmatch > 0:
                     print("", file=self.stream)
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/simple_pipeline_executor.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/simple_pipeline_executor.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/singleQuantumExecutor.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/singleQuantumExecutor.py`

 * *Files 1% similar despite different names*

```diff
@@ -204,15 +204,14 @@
             )
 
         if self.butler is not None:
             log_capture = LogCapture.from_full(self.butler)
         else:
             log_capture = LogCapture.from_limited(limited_butler)
         with log_capture.capture_logging(taskDef, quantum) as captureLog:
-
             # Save detailed resource usage before task start to metadata.
             quantumMetadata = _TASK_METADATA_TYPE()
             logInfo(None, "prep", metadata=quantumMetadata)  # type: ignore[arg-type]
 
             # check whether to skip or delete old outputs, if it returns True
             # or raises an exception do not try to store logs, as they may be
             # already in butler.
@@ -408,15 +407,15 @@
                 if self.clobberOutputs:
                     # only prune
                     _LOG.info("Removing partial outputs for task %s: %s", taskDef, existingRefs)
                     self.butler.pruneDatasets(existingRefs, disassociate=True, unstore=True, purge=True)
                     return False
                 else:
                     raise RuntimeError(
-                        f"Registry inconsistency while checking for existing outputs:"
+                        "Registry inconsistency while checking for existing outputs:"
                         f" collection={self.butler.run} existingRefs={existingRefs}"
                         f" missingRefs={missingRefs}"
                     )
 
         # need to re-run
         return False
 
@@ -444,15 +443,14 @@
             Updated Quantum instance
         """
         anyChanges = False
         updatedInputs: defaultdict[DatasetType, list] = defaultdict(list)
         for key, refsForDatasetType in quantum.inputs.items():
             newRefsForDatasetType = updatedInputs[key]
             for ref in refsForDatasetType:
-
                 # Inputs may already be resolved even if they do not exist, but
                 # we have to re-resolve them because IDs are ignored on output.
                 # Check datastore for existence first to cover calibration
                 # dataset types, as they would need a timespan for findDataset.
                 resolvedRef: DatasetRef | None
                 checked_datastore = False
                 if ref.id is not None and limited_butler.datastore.exists(ref):
@@ -581,16 +579,16 @@
         if taskDef.metadataDatasetName is not None:
             # DatasetRef has to be in the Quantum outputs, can lookup by name
             try:
                 [ref] = quantum.outputs[taskDef.metadataDatasetName]
             except LookupError as exc:
                 raise InvalidQuantumError(
                     f"Quantum outputs is missing metadata dataset type {taskDef.metadataDatasetName};"
-                    f" this could happen due to inconsistent options between QuantumGraph generation"
-                    f" and execution"
+                    " this could happen due to inconsistent options between QuantumGraph generation"
+                    " and execution"
                 ) from exc
             if self.butler is not None:
                 # Dataset ref can already be resolved, for non-QBB executor we
                 # have to ignore that because may be overriding run
                 # collection.
                 if ref.id is not None:
                     ref = ref.unresolved()
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/taskFactory.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/taskFactory.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst/ctrl/mpexec/util.py` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst/ctrl/mpexec/util.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/PKG-INFO` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-mpexec
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Pipeline execution infrastructure for the Rubin Observatory LSST Science Pipelines.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_mpexec
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-mpexec-26.0.0a20230400/python/lsst_ctrl_mpexec.egg-info/SOURCES.txt` & `lsst-ctrl-mpexec-26.0.0a20230500/python/lsst_ctrl_mpexec.egg-info/SOURCES.txt`

 * *Files identical despite different names*

