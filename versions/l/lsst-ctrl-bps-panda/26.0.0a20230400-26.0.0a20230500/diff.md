# Comparing `tmp/lsst-ctrl-bps-panda-26.0.0a20230400.tar.gz` & `tmp/lsst-ctrl-bps-panda-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-ctrl-bps-panda-26.0.0a20230400.tar", last modified: Thu Jan 26 09:55:14 2023, max compression
+gzip compressed data, was "lsst-ctrl-bps-panda-26.0.0a20230500.tar", last modified: Thu Feb  2 14:07:06 2023, max compression
```

## Comparing `lsst-ctrl-bps-panda-26.0.0a20230400.tar` & `lsst-ctrl-bps-panda-26.0.0a20230500.tar`

### file list

```diff
@@ -1,41 +1,42 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.010774 lsst-ctrl-bps-panda-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)      116 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)    35147 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-01-26 09:55:14.010774 lsst-ctrl-bps-panda-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      763 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3274 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.006774 lsst-ctrl-bps-panda-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.002774 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.002774 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.002774 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.006774 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/
--rw-r--r--   0 runner    (1001) docker     (123)      969 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.006774 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cli/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cli/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.006774 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cli/cmd/
--rw-r--r--   0 runner    (1001) docker     (123)     1011 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cli/cmd/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1837 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cli/cmd/panda_auth_commands.py
--rw-r--r--   0 runner    (1001) docker     (123)     1531 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cli/panda_auth.py
--rw-r--r--   0 runner    (1001) docker     (123)     4449 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cmd_line_embedder.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.010774 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/conf_example/
--rw-r--r--   0 runner    (1001) docker     (123)     5855 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/conf_example/example_panda_SLAC.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      877 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/conf_example/pipelines_check_idf.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      399 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/conf_example/test_idf.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      487 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/conf_example/test_sdf.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      385 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/conf_example/test_usdf.yaml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.010774 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/edgenode/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/edgenode/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4184 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/edgenode/cmd_line_decoder.py
--rw-r--r--   0 runner    (1001) docker     (123)    19743 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/idds_tasks.py
--rw-r--r--   0 runner    (1001) docker     (123)     2177 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/panda_auth_drivers.py
--rw-r--r--   0 runner    (1001) docker     (123)     4712 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/panda_auth_utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    26201 2023-01-26 09:55:02.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/panda_service.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 09:55:13.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:14.010774 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst_ctrl_bps_panda.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-01-26 09:55:13.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst_ctrl_bps_panda.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1242 2023-01-26 09:55:14.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst_ctrl_bps_panda.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:55:13.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst_ctrl_bps_panda.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      219 2023-01-26 09:55:13.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst_ctrl_bps_panda.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 09:55:13.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst_ctrl_bps_panda.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:55:13.000000 lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst_ctrl_bps_panda.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-01-26 09:55:14.010774 lsst-ctrl-bps-panda-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.180408 lsst-ctrl-bps-panda-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)      116 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)    35147 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-02-02 14:07:06.180408 lsst-ctrl-bps-panda-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      763 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3274 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.176408 lsst-ctrl-bps-panda-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.176408 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.176408 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.176408 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.176408 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/
+-rw-r--r--   0 runner    (1001) docker     (123)      969 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.180408 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cli/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.180408 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cli/cmd/
+-rw-r--r--   0 runner    (1001) docker     (123)     1011 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cli/cmd/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1837 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cli/cmd/panda_auth_commands.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1530 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cli/panda_auth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4669 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cmd_line_embedder.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.180408 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/conf_example/
+-rw-r--r--   0 runner    (1001) docker     (123)     5855 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/conf_example/example_panda_SLAC.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      877 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/conf_example/pipelines_check_idf.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      399 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/conf_example/test_idf.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      487 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/conf_example/test_sdf.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      385 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/conf_example/test_usdf.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1373 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/constants.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.180408 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/edgenode/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/edgenode/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4278 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/edgenode/cmd_line_decoder.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2177 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/panda_auth_drivers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4712 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/panda_auth_utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11884 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/panda_service.py
+-rw-r--r--   0 runner    (1001) docker     (123)    19114 2023-02-02 14:06:48.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:07:06.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:07:06.180408 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst_ctrl_bps_panda.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1497 2023-02-02 14:07:06.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst_ctrl_bps_panda.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1277 2023-02-02 14:07:06.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst_ctrl_bps_panda.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:07:06.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst_ctrl_bps_panda.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      219 2023-02-02 14:07:06.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst_ctrl_bps_panda.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:07:06.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst_ctrl_bps_panda.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:07:05.000000 lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst_ctrl_bps_panda.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-02-02 14:07:06.180408 lsst-ctrl-bps-panda-26.0.0a20230500/setup.cfg
```

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/LICENSE` & `lsst-ctrl-bps-panda-26.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/PKG-INFO` & `lsst-ctrl-bps-panda-26.0.0a20230500/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-bps-panda
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: PanDA plugin for lsst-ctrl-bps.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_bps_panda
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/README.rst` & `lsst-ctrl-bps-panda-26.0.0a20230500/README.rst`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/pyproject.toml` & `lsst-ctrl-bps-panda-26.0.0a20230500/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/__init__.py` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cli/cmd/__init__.py` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cli/cmd/__init__.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cli/cmd/panda_auth_commands.py` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cli/cmd/panda_auth_commands.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cli/panda_auth.py` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cli/panda_auth.py`

 * *Files 1% similar despite different names*

```diff
@@ -26,15 +26,14 @@
     log_level_option,
     log_tty_option,
     long_log_option,
 )
 
 
 class PandaAuthCli(LoaderCLI):
-
     localCmdPkg = "lsst.ctrl.bps.panda.cli.cmd"
 
 
 @click.command(cls=PandaAuthCli, context_settings=dict(help_option_names=["-h", "--help"]), epilog=None)
 @log_level_option(default=["INFO"])
 @long_log_option()
 @log_file_option()
```

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/cmd_line_embedder.py` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/cmd_line_embedder.py`

 * *Files 7% similar despite different names*

```diff
@@ -17,14 +17,15 @@
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program.  If not, see <https://www.gnu.org/licenses/>.
 
 import logging
 import os
+import re
 
 _LOG = logging.getLogger(__name__)
 
 
 class CommandLineEmbedder:
     """
     Class embeds static (constant across a task) values
@@ -115,12 +116,16 @@
         Returns
         -------
         cmd_line: `str`
             processed command line
         file_name: `str`
             job pseudo input file name
         """
+        cmd_vals = set([m.group(1) for m in re.finditer(r"[^$]{([^}]+)}", cmd_line)])
+        actual_lazy_vars = {}
+        for key in cmd_vals:
+            actual_lazy_vars[key] = lazy_vars[key]
 
-        cmd_line = self.replace_static_parameters(cmd_line, lazy_vars)
+        cmd_line = self.replace_static_parameters(cmd_line, actual_lazy_vars)
         cmd_line = self.resolve_submission_side_env_vars(cmd_line)
-        file_name = job_name + self.attach_pseudo_file_params(lazy_vars)
+        file_name = job_name + self.attach_pseudo_file_params(actual_lazy_vars)
         return cmd_line, file_name
```

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/conf_example/example_panda_SLAC.yaml` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/conf_example/example_panda_SLAC.yaml`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/conf_example/pipelines_check_idf.yaml` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/conf_example/pipelines_check_idf.yaml`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/edgenode/cmd_line_decoder.py` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/edgenode/cmd_line_decoder.py`

 * *Files 2% similar despite different names*

```diff
@@ -17,18 +17,18 @@
 def replace_placeholders(cmd_line, tag, replancements):
     occurences_to_replace = re.findall(f"<{tag}:(.*?)>", cmd_line)
     for placeholder in occurences_to_replace:
         if placeholder in replancements:
             cmd_line = cmd_line.replace(f"<{tag}:{placeholder}>", replancements[placeholder])
         else:
             raise ValueError(
-                f"ValueError exception thrown, because "
+                "ValueError exception thrown, because "
                 f"{placeholder} is not found in the "
-                f"replacement values and could "
-                f"not be passed to the command line"
+                "replacement values and could "
+                "not be passed to the command line"
             )
     return cmd_line
 
 
 def replace_environment_vars(cmd_line):
     """Replaces placeholders to the actual environment variables.
 
@@ -106,15 +106,17 @@
                 files_to_copy = [src]
             dest_base = ResourcePath("", forceAbsolute=True, forceDirectory=True)
             if base_dir:
                 dest_base = dest_base.join(base_dir)
             for file_to_copy in files_to_copy:
                 dest = dest_base.join(file_to_copy.basename())
                 dest.transfer_from(file_to_copy, transfer="copy")
-                print(f"copied {file_to_copy.path} " f"to {dest.path}", file=sys.stderr)
+                print(f"copied {file_to_copy.path} to {dest.path}", file=sys.stderr)
+            if file_name_placeholder == "job_executable":
+                os.chmod(dest.path, 0o777)
 
 
 deliver_input_files(sys.argv[3], sys.argv[4], sys.argv[5])
 cmd_line = str(binascii.unhexlify(sys.argv[1]).decode())
 data_params = sys.argv[2].split("+")
 cmd_line = replace_environment_vars(cmd_line)
```

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/panda_auth_drivers.py` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/panda_auth_drivers.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst/ctrl/bps/panda/panda_auth_utils.py` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst/ctrl/bps/panda/panda_auth_utils.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst_ctrl_bps_panda.egg-info/PKG-INFO` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst_ctrl_bps_panda.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-bps-panda
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: PanDA plugin for lsst-ctrl-bps.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_bps_panda
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-bps-panda-26.0.0a20230400/python/lsst_ctrl_bps_panda.egg-info/SOURCES.txt` & `lsst-ctrl-bps-panda-26.0.0a20230500/python/lsst_ctrl_bps_panda.egg-info/SOURCES.txt`

 * *Files 18% similar despite different names*

```diff
@@ -1,18 +1,19 @@
 COPYRIGHT
 LICENSE
 README.rst
 pyproject.toml
 setup.cfg
 python/lsst/ctrl/bps/panda/__init__.py
 python/lsst/ctrl/bps/panda/cmd_line_embedder.py
-python/lsst/ctrl/bps/panda/idds_tasks.py
+python/lsst/ctrl/bps/panda/constants.py
 python/lsst/ctrl/bps/panda/panda_auth_drivers.py
 python/lsst/ctrl/bps/panda/panda_auth_utils.py
 python/lsst/ctrl/bps/panda/panda_service.py
+python/lsst/ctrl/bps/panda/utils.py
 python/lsst/ctrl/bps/panda/version.py
 python/lsst/ctrl/bps/panda/cli/__init__.py
 python/lsst/ctrl/bps/panda/cli/panda_auth.py
 python/lsst/ctrl/bps/panda/cli/cmd/__init__.py
 python/lsst/ctrl/bps/panda/cli/cmd/panda_auth_commands.py
 python/lsst/ctrl/bps/panda/conf_example/example_panda_SLAC.yaml
 python/lsst/ctrl/bps/panda/conf_example/pipelines_check_idf.yaml
```

