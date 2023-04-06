# Comparing `tmp/lsst-ctrl-bps-26.0.0a20230400.tar.gz` & `tmp/lsst-ctrl-bps-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-ctrl-bps-26.0.0a20230400.tar", last modified: Thu Jan 26 09:56:11 2023, max compression
+gzip compressed data, was "lsst-ctrl-bps-26.0.0a20230500.tar", last modified: Thu Feb  2 14:06:50 2023, max compression
```

## Comparing `lsst-ctrl-bps-26.0.0a20230400.tar` & `lsst-ctrl-bps-26.0.0a20230500.tar`

### file list

```diff
@@ -1,60 +1,60 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.014913 lsst-ctrl-bps-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)       61 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       32 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1363 2023-01-26 09:56:11.014913 lsst-ctrl-bps-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      609 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.006913 lsst-ctrl-bps-26.0.0a20230400/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.010913 lsst-ctrl-bps-26.0.0a20230400/doc/lsst.ctrl.bps/
--rw-r--r--   0 runner    (1001) docker     (123)    14198 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/doc/lsst.ctrl.bps/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1035 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/doc/lsst.ctrl.bps/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)    38338 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/doc/lsst.ctrl.bps/quickstart.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3224 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.006913 lsst-ctrl-bps-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.010913 lsst-ctrl-bps-26.0.0a20230400/python/lsst/
--rw-r--r--   0 runner    (1001) docker     (123)      984 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.010913 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/
--rw-r--r--   0 runner    (1001) docker     (123)      984 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.010913 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/
--rw-r--r--   0 runner    (1001) docker     (123)     1184 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    11978 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/bps_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     1603 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/bps_draw.py
--rw-r--r--   0 runner    (1001) docker     (123)     9776 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/bps_reports.py
--rw-r--r--   0 runner    (1001) docker     (123)     7618 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/bps_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2936 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cancel.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.010913 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1918 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/bps.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.010913 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/cmd/
--rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/cmd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4636 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/cmd/commands.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.014913 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/opt/
--rw-r--r--   0 runner    (1001) docker     (123)      992 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/opt/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1152 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/opt/arguments.py
--rw-r--r--   0 runner    (1001) docker     (123)     2129 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/opt/option_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)     2089 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/opt/options.py
--rw-r--r--   0 runner    (1001) docker     (123)    16641 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/clustered_quantum_graph.py
--rw-r--r--   0 runner    (1001) docker     (123)     1351 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/constants.py
--rw-r--r--   0 runner    (1001) docker     (123)    19293 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/drivers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.014913 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/etc/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/etc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4479 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/etc/bps_defaults.yaml
--rw-r--r--   0 runner    (1001) docker     (123)    27353 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/generic_workflow.py
--rw-r--r--   0 runner    (1001) docker     (123)     1854 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/ping.py
--rw-r--r--   0 runner    (1001) docker     (123)     9257 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/pre_transform.py
--rw-r--r--   0 runner    (1001) docker     (123)     3239 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/prepare.py
--rw-r--r--   0 runner    (1001) docker     (123)    12024 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/quantum_clustering_funcs.py
--rw-r--r--   0 runner    (1001) docker     (123)     3900 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/report.py
--rw-r--r--   0 runner    (1001) docker     (123)     1915 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/restart.py
--rw-r--r--   0 runner    (1001) docker     (123)     2801 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/submit.py
--rw-r--r--   0 runner    (1001) docker     (123)    36091 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/transform.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 09:56:10.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/version.py
--rw-r--r--   0 runner    (1001) docker     (123)    11648 2023-01-26 09:55:57.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/wms_service.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:11.014913 lsst-ctrl-bps-26.0.0a20230400/python/lsst_ctrl_bps.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1363 2023-01-26 09:56:10.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst_ctrl_bps.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1567 2023-01-26 09:56:11.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst_ctrl_bps.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:10.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst_ctrl_bps.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      198 2023-01-26 09:56:10.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst_ctrl_bps.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 09:56:10.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst_ctrl_bps.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:10.000000 lsst-ctrl-bps-26.0.0a20230400/python/lsst_ctrl_bps.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-01-26 09:56:11.014913 lsst-ctrl-bps-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.329202 lsst-ctrl-bps-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       32 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1363 2023-02-02 14:06:50.329202 lsst-ctrl-bps-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      609 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.321202 lsst-ctrl-bps-26.0.0a20230500/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.325202 lsst-ctrl-bps-26.0.0a20230500/doc/lsst.ctrl.bps/
+-rw-r--r--   0 runner    (1001) docker     (123)    14198 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/doc/lsst.ctrl.bps/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1035 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/doc/lsst.ctrl.bps/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    38338 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/doc/lsst.ctrl.bps/quickstart.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3224 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.321202 lsst-ctrl-bps-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.325202 lsst-ctrl-bps-26.0.0a20230500/python/lsst/
+-rw-r--r--   0 runner    (1001) docker     (123)      984 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.325202 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/
+-rw-r--r--   0 runner    (1001) docker     (123)      984 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.325202 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/
+-rw-r--r--   0 runner    (1001) docker     (123)     1184 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11978 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/bps_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1603 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/bps_draw.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9776 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/bps_reports.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7618 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/bps_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2936 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cancel.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.325202 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1917 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/bps.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.329202 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/cmd/
+-rw-r--r--   0 runner    (1001) docker     (123)     1122 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/cmd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4636 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/cmd/commands.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.329202 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/opt/
+-rw-r--r--   0 runner    (1001) docker     (123)      992 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/opt/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1152 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/opt/arguments.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2129 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/opt/option_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2089 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/opt/options.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16641 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/clustered_quantum_graph.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1351 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/constants.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19293 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/drivers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.329202 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/etc/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/etc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4479 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/etc/bps_defaults.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)    28679 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/generic_workflow.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1854 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/ping.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9256 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/pre_transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3239 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/prepare.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12000 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/quantum_clustering_funcs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3899 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/report.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1915 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/restart.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2801 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/submit.py
+-rw-r--r--   0 runner    (1001) docker     (123)    36091 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/transform.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:06:50.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/version.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11648 2023-02-02 14:06:37.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/wms_service.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:50.329202 lsst-ctrl-bps-26.0.0a20230500/python/lsst_ctrl_bps.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1363 2023-02-02 14:06:50.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst_ctrl_bps.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1567 2023-02-02 14:06:50.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst_ctrl_bps.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:06:50.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst_ctrl_bps.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      198 2023-02-02 14:06:50.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst_ctrl_bps.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:06:50.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst_ctrl_bps.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:06:49.000000 lsst-ctrl-bps-26.0.0a20230500/python/lsst_ctrl_bps.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-02-02 14:06:50.329202 lsst-ctrl-bps-26.0.0a20230500/setup.cfg
```

### Comparing `lsst-ctrl-bps-26.0.0a20230400/LICENSE` & `lsst-ctrl-bps-26.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/PKG-INFO` & `lsst-ctrl-bps-26.0.0a20230500/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-bps
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Pluggable execution of workflow graphs from Rubin pipelines.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_bps
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-bps-26.0.0a20230400/README.md` & `lsst-ctrl-bps-26.0.0a20230500/README.md`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/doc/lsst.ctrl.bps/CHANGES.rst` & `lsst-ctrl-bps-26.0.0a20230500/doc/lsst.ctrl.bps/CHANGES.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/doc/lsst.ctrl.bps/index.rst` & `lsst-ctrl-bps-26.0.0a20230500/doc/lsst.ctrl.bps/index.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/doc/lsst.ctrl.bps/quickstart.rst` & `lsst-ctrl-bps-26.0.0a20230500/doc/lsst.ctrl.bps/quickstart.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/pyproject.toml` & `lsst-ctrl-bps-26.0.0a20230500/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/__init__.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/__init__.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/__init__.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/bps_config.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/bps_config.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/bps_draw.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/bps_draw.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/bps_reports.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/bps_reports.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/bps_utils.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/bps_utils.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cancel.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cancel.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/bps.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/bps.py`

 * *Files 0% similar despite different names*

```diff
@@ -39,15 +39,14 @@
 However, the current version does not support starting the submission process
 from any of these intermediate points.
 """
 )
 
 
 class BpsCli(LoaderCLI):
-
     localCmdPkg = "lsst.ctrl.bps.cli.cmd"
 
 
 @click.command(cls=BpsCli, context_settings=dict(help_option_names=["-h", "--help"]), epilog=epilog)
 @log_level_option(default=["INFO"])
 @long_log_option()
 @log_file_option()
```

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/cmd/__init__.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/cmd/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/cmd/commands.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/cmd/commands.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/opt/__init__.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/opt/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/opt/arguments.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/opt/arguments.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/opt/option_groups.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/opt/option_groups.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/cli/opt/options.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/cli/opt/options.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/clustered_quantum_graph.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/clustered_quantum_graph.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/constants.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/constants.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/drivers.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/drivers.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/etc/bps_defaults.yaml` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/etc/bps_defaults.yaml`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/generic_workflow.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/generic_workflow.py`

 * *Files 4% similar despite different names*

```diff
@@ -25,15 +25,15 @@
 __all__ = ["GenericWorkflow", "GenericWorkflowFile", "GenericWorkflowJob", "GenericWorkflowExec"]
 
 
 import dataclasses
 import itertools
 import logging
 import pickle
-from collections import Counter
+from collections import Counter, defaultdict
 from typing import Optional
 
 from lsst.utils.iteration import ensure_iterable
 from networkx import DiGraph, topological_sort
 from networkx.algorithms.dag import is_directed_acyclic_graph
 
 from .bps_draw import draw_networkx_dot
@@ -366,14 +366,15 @@
         super().__init__(incoming_graph_data, **attr)
         self._name = name
         self.run_attrs = {}
         self._files = {}
         self._executables = {}
         self._inputs = {}  # mapping job.names to list of GenericWorkflowFile
         self._outputs = {}  # mapping job.names to list of GenericWorkflowFile
+        self._labels = defaultdict(list)  # mapping job label to list of GenericWorkflowJob
         self.run_id = None
         self._final = None
 
     @property
     def name(self):
         """Retrieve name of generic workflow.
 
@@ -391,28 +392,35 @@
         for job_name in self:
             gwjob = self.get_job(job_name)
             if gwjob.quanta_counts is not None:
                 qcounts += gwjob.quanta_counts
         return qcounts
 
     @property
+    def labels(self):
+        """List of job labels (`list` [`str`], read-only)"""
+        return list(self._labels.keys())
+
+    def regenerate_labels(self):
+        """Regenerate the list of job labels."""
+        self._labels = defaultdict(list)
+        for job_name in self:
+            job = self.get_job(job_name)
+            self._labels[job.label].append(job)
+
+    @property
     def job_counts(self):
         """Count of jobs per job label (`collections.Counter`)."""
-        jcounts = Counter()
-        for job_name in self:
-            gwjob = self.get_job(job_name)
-            jcounts[gwjob.label] += 1
+        jcounts = Counter({label: len(jobs) for label, jobs in self._labels.items()})
 
         # Final is separate
         final = self.get_final()
         if final:
             if isinstance(final, GenericWorkflow):
-                for job_name in final:
-                    gwjob = final.get_job(job_name)
-                    jcounts[gwjob.label] += 1
+                jcounts.update(final.job_counts())
             else:
                 jcounts[final.label] += 1
 
         return jcounts
 
     def __iter__(self):
         """Return iterator of job names in topologically sorted order."""
@@ -463,14 +471,15 @@
             raise RuntimeError(f"Invalid type for job to be added to GenericWorkflowGraph ({type(job)}).")
         if self.has_node(job.name):
             raise RuntimeError(f"Job {job.name} already exists in GenericWorkflowGraph.")
         super().add_node(job.name, job=job)
         self.add_job_relationships(parent_names, job.name)
         self.add_job_relationships(job.name, child_names)
         self.add_executable(job.executable)
+        self._labels[job.label].append(job)
 
     def add_node(self, node_for_adding, **attr):
         """Override networkx function to call more specific add_job function.
 
         Parameters
         ----------
         node_for_adding : `lsst.ctrl.bps.GenericWorkflowJob`
@@ -545,20 +554,26 @@
         """Delete job from generic workflow leaving connected graph.
 
         Parameters
         ----------
         job_name : `str`
             Name of job to delete from workflow.
         """
+        job = self.get_job(job_name)
+        self._labels[job.label].remove(job)
+        # Don't leave keys around if removed last job
+        if not self._labels[job.label]:
+            del self._labels[job.label]
+
         # Connect all parent jobs to all children jobs.
         parents = self.predecessors(job_name)
         children = self.successors(job_name)
         self.add_job_relationships(parents, children)
 
-        # Delete job node (which deleted edges).
+        # Delete job node (which deletes edges).
         self.remove_node(job_name)
 
     def add_job_inputs(self, job_name, files):
         """Add files as inputs to specified job.
 
         Parameters
         ----------
@@ -773,14 +788,23 @@
 
         # Files are stored separately so copy them.
         for job_name in workflow:
             self.add_job_inputs(job_name, workflow.get_job_inputs(job_name, data=True))
             self.add_job_outputs(job_name, workflow.get_job_outputs(job_name, data=True))
             self.add_executable(workflow.get_job(job_name).executable)
 
+        # Note: label ordering inferred from dict order
+        #       so adding given source workflow first
+        labels = defaultdict(list)
+        for label in workflow._labels:
+            labels[label] = workflow._labels[label]
+        for label in self._labels:
+            labels[label] = self._labels[label]
+        self._labels = labels
+
     def add_final(self, final):
         """Add special final job/workflow to the generic workflow.
 
         Parameters
         ----------
         final : `lsst.ctrl.bps.GenericWorkflowJob` or \
                 `lsst.ctrl.bps.GenericWorkflow`
@@ -843,7 +867,22 @@
         for name, executable in self._executables.items():
             if not transfer_only or executable.transfer_executable:
                 if not data:
                     execs.append(name)
                 else:
                     execs.append(executable)
         return execs
+
+    def get_jobs_by_label(self, label: str):
+        """Retrieve jobs by label from workflow.
+
+        Parameters
+        ----------
+        label : `str`
+            Label of jobs to retrieve.
+
+        Returns
+        -------
+        jobs : list[`lsst.ctrl.bps.GenericWorkflowJob`]
+            Jobs having given label.
+        """
+        return self._labels[label]
```

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/ping.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/ping.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/pre_transform.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/pre_transform.py`

 * *Files 0% similar despite different names*

```diff
@@ -108,15 +108,15 @@
     with time_this(log=_LOG, level=logging.INFO, prefix=None, msg="Completed reading quantum graph"):
         qgraph = read_quantum_graph(qgraph_filename, config["butlerConfig"])
 
     if when_create.upper() == "QGRAPH_CMDLINE":
         if not os.path.exists(execution_butler_dir):
             raise OSError(
                 f"Missing execution butler dir ({execution_butler_dir}) after "
-                f"creating QuantumGraph (whenMakeExecutionButler == QGRAPH_CMDLINE"
+                "creating QuantumGraph (whenMakeExecutionButler == QGRAPH_CMDLINE"
             )
     elif when_create.upper() == "ACQUIRE":
         _create_execution_butler(config, qgraph_filename, execution_butler_dir, config["submitPath"])
 
     return qgraph_filename, qgraph, execution_butler_dir
```

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/prepare.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/prepare.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/quantum_clustering_funcs.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/quantum_clustering_funcs.py`

 * *Files 1% similar despite different names*

```diff
@@ -295,13 +295,12 @@
                     )
             except KeyError as e:  # pragma: no cover
                 # For debugging a problem internal to method
                 nid = NodeId(e.args[0], qgraph.graphID)
                 qnode = qgraph.getQuantumNodeByNodeId(nid)
 
                 print(
-                    f"Quanta missing when clustering: {qnode.taskDef.label}, "
-                    f"{qnode.quantum.dataId.byName()}"
+                    f"Quanta missing when clustering: {qnode.taskDef.label}, {qnode.quantum.dataId.byName()}"
                 )
                 raise
 
     return cqgraph
```

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/report.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/report.py`

 * *Files 0% similar despite different names*

```diff
@@ -99,15 +99,15 @@
 
             run_brief.clear()
             run_report.clear()
         if not runs and not message:
             print(
                 f"No records found for job id '{run_id}'. "
                 f"Hints: Double check id, retry with a larger --hist value (currently: {hist_days}), "
-                f"and/or use --global to search all job queues."
+                "and/or use --global to search all job queues."
             )
     else:
         for run in runs:
             run_brief.add(run, use_global_id=is_global)
         run_brief.sort("ID")
         print(run_brief)
     if message:
```

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/restart.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/restart.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/submit.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/submit.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/transform.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/transform.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst/ctrl/bps/wms_service.py` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst/ctrl/bps/wms_service.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst_ctrl_bps.egg-info/PKG-INFO` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst_ctrl_bps.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-bps
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Pluggable execution of workflow graphs from Rubin pipelines.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_bps
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-bps-26.0.0a20230400/python/lsst_ctrl_bps.egg-info/SOURCES.txt` & `lsst-ctrl-bps-26.0.0a20230500/python/lsst_ctrl_bps.egg-info/SOURCES.txt`

 * *Files identical despite different names*

