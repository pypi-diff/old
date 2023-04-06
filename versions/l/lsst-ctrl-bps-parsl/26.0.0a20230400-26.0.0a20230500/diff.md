# Comparing `tmp/lsst-ctrl-bps-parsl-26.0.0a20230400.tar.gz` & `tmp/lsst-ctrl-bps-parsl-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-ctrl-bps-parsl-26.0.0a20230400.tar", last modified: Thu Jan 26 09:54:53 2023, max compression
+gzip compressed data, was "lsst-ctrl-bps-parsl-26.0.0a20230500.tar", last modified: Thu Feb  2 14:05:27 2023, max compression
```

## Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400.tar` & `lsst-ctrl-bps-parsl-26.0.0a20230500.tar`

### file list

```diff
@@ -1,35 +1,35 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:54:53.781613 lsst-ctrl-bps-parsl-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)      181 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     2296 2023-01-26 09:54:53.781613 lsst-ctrl-bps-parsl-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     3092 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:54:53.777613 lsst-ctrl-bps-parsl-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:54:53.777613 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:54:53.777613 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:54:53.777613 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:54:53.777613 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/
--rw-r--r--   0 runner    (1001) docker     (123)      115 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4420 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/configuration.py
--rw-r--r--   0 runner    (1001) docker     (123)      922 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/environment.py
--rw-r--r--   0 runner    (1001) docker     (123)     8885 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/job.py
--rw-r--r--   0 runner    (1001) docker     (123)     2491 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/service.py
--rw-r--r--   0 runner    (1001) docker     (123)     6231 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/site.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:54:53.781613 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/
--rw-r--r--   0 runner    (1001) docker     (123)       68 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1265 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/local.py
--rw-r--r--   0 runner    (1001) docker     (123)     3181 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/nersc.py
--rw-r--r--   0 runner    (1001) docker     (123)     4156 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/princeton.py
--rw-r--r--   0 runner    (1001) docker     (123)     2532 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/slac.py
--rw-r--r--   0 runner    (1001) docker     (123)    11138 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/slurm.py
--rw-r--r--   0 runner    (1001) docker     (123)     5309 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/work_queue.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 09:54:53.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/version.py
--rw-r--r--   0 runner    (1001) docker     (123)    10049 2023-01-26 09:54:33.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/workflow.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:54:53.781613 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst_ctrl_bps_parsl.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     2296 2023-01-26 09:54:53.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst_ctrl_bps_parsl.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      960 2023-01-26 09:54:53.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst_ctrl_bps_parsl.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:54:53.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst_ctrl_bps_parsl.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      108 2023-01-26 09:54:53.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst_ctrl_bps_parsl.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 09:54:53.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst_ctrl_bps_parsl.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:54:53.000000 lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst_ctrl_bps_parsl.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-01-26 09:54:53.785613 lsst-ctrl-bps-parsl-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:27.453524 lsst-ctrl-bps-parsl-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)      181 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     2296 2023-02-02 14:05:27.453524 lsst-ctrl-bps-parsl-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1553 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     3092 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:27.449524 lsst-ctrl-bps-parsl-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:27.449524 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:27.449524 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:27.449524 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:27.453524 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/
+-rw-r--r--   0 runner    (1001) docker     (123)      115 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4420 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/configuration.py
+-rw-r--r--   0 runner    (1001) docker     (123)      922 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/environment.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8885 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/job.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2491 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/service.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6231 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/site.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:27.453524 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/
+-rw-r--r--   0 runner    (1001) docker     (123)       68 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1265 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/local.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3181 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/nersc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4156 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/princeton.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2532 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/slac.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11138 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/slurm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5410 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/work_queue.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:05:27.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/version.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10049 2023-02-02 14:05:13.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/workflow.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:27.453524 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst_ctrl_bps_parsl.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     2296 2023-02-02 14:05:27.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst_ctrl_bps_parsl.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      960 2023-02-02 14:05:27.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst_ctrl_bps_parsl.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:27.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst_ctrl_bps_parsl.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      108 2023-02-02 14:05:27.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst_ctrl_bps_parsl.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:05:27.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst_ctrl_bps_parsl.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:27.000000 lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst_ctrl_bps_parsl.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-02-02 14:05:27.453524 lsst-ctrl-bps-parsl-26.0.0a20230500/setup.cfg
```

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/LICENSE` & `lsst-ctrl-bps-parsl-26.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/PKG-INFO` & `lsst-ctrl-bps-parsl-26.0.0a20230500/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-bps-parsl
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Parsl-based plugin for lsst-ctrl-bps.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_bps_parsl
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/README.md` & `lsst-ctrl-bps-parsl-26.0.0a20230500/README.md`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/pyproject.toml` & `lsst-ctrl-bps-parsl-26.0.0a20230500/pyproject.toml`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/configuration.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/configuration.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/environment.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/environment.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/job.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/job.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/service.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/service.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/site.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/site.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/local.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/local.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/nersc.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/nersc.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/princeton.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/princeton.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/slac.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/slac.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/slurm.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/slurm.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/sites/work_queue.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/sites/work_queue.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,14 +1,18 @@
 from typing import TYPE_CHECKING, Any, Dict, List
 
 from parsl.executors import WorkQueueExecutor
 from parsl.executors.base import ParslExecutor
 from parsl.launchers import SrunLauncher
 from parsl.providers import LocalProvider
-from parsl.providers.provider_base import ExecutionProvider
+
+try:
+    from parsl.providers.base import ExecutionProvider
+except ImportError:
+    from parsl.providers.provider_base import ExecutionProvider  # type: ignore
 
 from ..configuration import get_bps_config_value
 from ..site import SiteConfig
 
 if TYPE_CHECKING:
     from ..job import ParslJob
```

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst/ctrl/bps/parsl/workflow.py` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst/ctrl/bps/parsl/workflow.py`

 * *Files identical despite different names*

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst_ctrl_bps_parsl.egg-info/PKG-INFO` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst_ctrl_bps_parsl.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-ctrl-bps-parsl
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: Parsl-based plugin for lsst-ctrl-bps.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: GPLv3+ License
 Project-URL: Homepage, https://github.com/lsst/ctrl_bps_parsl
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
```

### Comparing `lsst-ctrl-bps-parsl-26.0.0a20230400/python/lsst_ctrl_bps_parsl.egg-info/SOURCES.txt` & `lsst-ctrl-bps-parsl-26.0.0a20230500/python/lsst_ctrl_bps_parsl.egg-info/SOURCES.txt`

 * *Files identical despite different names*

