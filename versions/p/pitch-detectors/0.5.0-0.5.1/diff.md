# Comparing `tmp/pitch-detectors-0.5.0.tar.gz` & `tmp/pitch-detectors-0.5.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pitch-detectors-0.5.0.tar", last modified: Thu Apr  6 18:11:42 2023, max compression
+gzip compressed data, was "pitch-detectors-0.5.1.tar", last modified: Fri Apr  7 07:23:29 2023, max compression
```

## Comparing `pitch-detectors-0.5.0.tar` & `pitch-detectors-0.5.1.tar`

### file list

```diff
@@ -1,53 +1,53 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5654 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.229628 pitch-detectors-0.5.0/pitch_detectors/
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/pitch_detectors/algorithms/
--rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2611 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/crepe.py
--rw-r--r--   0 runner    (1001) docker     (123)     2993 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/ensemble.py
--rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/penn.py
--rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/piptrack.py
--rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/praatac.py
--rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/praatcc.py
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/praatshs.py
--rw-r--r--   0 runner    (1001) docker     (123)      745 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/pyin.py
--rw-r--r--   0 runner    (1001) docker     (123)      632 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/rapt.py
--rw-r--r--   0 runner    (1001) docker     (123)      799 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/reaper.py
--rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/spice.py
--rw-r--r--   0 runner    (1001) docker     (123)      635 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/swipe.py
--rw-r--r--   0 runner    (1001) docker     (123)     1396 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/torchcrepe.py
--rw-r--r--   0 runner    (1001) docker     (123)      713 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/torchyin.py
--rw-r--r--   0 runner    (1001) docker     (123)      486 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/world.py
--rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/yaapt.py
--rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/yin.py
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/pitch_detectors/evaluation/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/mdb_stem_synth.py
--rw-r--r--   0 runner    (1001) docker     (123)     1447 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/mir_1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3752 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/table.py
--rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.229628 pitch-detectors-0.5.0/pitch_detectors.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      344 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     4564 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)     1241 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/scripts/run_algorithm.py
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/algorithms_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     1046 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)      341 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/ensemble_test.py
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/gpu_test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5654 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.626106 pitch-detectors-0.5.1/pitch_detectors/
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/pitch_detectors/algorithms/
+-rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2611 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/crepe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2993 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/ensemble.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/penn.py
+-rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/piptrack.py
+-rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/praatac.py
+-rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/praatcc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/praatshs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      745 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/pyin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      632 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/rapt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      799 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/reaper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/spice.py
+-rw-r--r--   0 runner    (1001) docker     (123)      635 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/swipe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1396 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/torchcrepe.py
+-rw-r--r--   0 runner    (1001) docker     (123)      713 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/torchyin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      486 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/world.py
+-rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/yaapt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/yin.py
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/pitch_detectors/evaluation/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/mdb_stem_synth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1447 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/mir_1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3752 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)      437 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.626106 pitch-detectors-0.5.1/pitch_detectors.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      353 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     4580 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)     1246 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/scripts/run_algorithm.py
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/algorithms_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1046 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)      341 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/ensemble_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/gpu_test.py
```

### Comparing `pitch-detectors-0.5.0/README.md` & `pitch-detectors-0.5.1/README.md`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/__init__.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/__init__.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/base.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/base.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/crepe.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/crepe.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/ensemble.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/ensemble.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/penn.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/penn.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/piptrack.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/piptrack.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/praatac.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/praatac.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/praatcc.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/praatcc.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/praatshs.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/praatshs.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/pyin.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/pyin.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/rapt.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/rapt.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/reaper.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/reaper.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/spice.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/spice.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/swipe.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/swipe.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/torchcrepe.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/torchcrepe.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/torchyin.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/torchyin.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/yaapt.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/yaapt.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/algorithms/yin.py` & `pitch-detectors-0.5.1/pitch_detectors/algorithms/yin.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/evaluation/__main__.py` & `pitch-detectors-0.5.1/pitch_detectors/evaluation/__main__.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/base.py` & `pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/base.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/mdb_stem_synth.py` & `pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/mdb_stem_synth.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/mir_1k.py` & `pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/mir_1k.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/evaluation/table.py` & `pitch-detectors-0.5.1/pitch_detectors/evaluation/table.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors/util.py` & `pitch-detectors-0.5.1/pitch_detectors/util.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pitch_detectors.egg-info/SOURCES.txt` & `pitch-detectors-0.5.1/pitch_detectors.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/pyproject.toml` & `pitch-detectors-0.5.1/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "pitch-detectors"
-version = "0.5.0"
+version = "0.5.1"
 authors = [
     {name = "Alexander Rodionov", email = "tandav@tandav.me"},
 ]
 description = "collection of pitch detection algorithms with unified interface"
 requires-python = ">=3.8,<3.11"
 dependencies = [
     "AMFM-decompy",
@@ -23,14 +23,15 @@
     "tensorflow-hub",
     "torch",
     "torch-yin",
     "torchcrepe>=0.0.18",
     "penn",
     "nvidia-cudnn-cu11",
     "tensorrt",
+    "pydantic",
 ]
 
 [project.optional-dependencies]
 dev = [
     "bumpver",
     "pre-commit",
     "pytest",
@@ -62,15 +63,15 @@
 
 [tool.setuptools.packages.find]
 exclude = ["data*"]
 
 # ==============================================================================
 
 [tool.bumpver]
-current_version = "v0.5.0"
+current_version = "v0.5.1"
 version_pattern = "vMAJOR.MINOR.PATCH"
 commit_message = "bump version {old_version} -> {new_version}"
 commit = true
 tag = true
 
 [tool.bumpver.file_patterns]
 "pyproject.toml" = [
```

### Comparing `pitch-detectors-0.5.0/scripts/run_algorithm.py` & `pitch-detectors-0.5.1/scripts/run_algorithm.py`

 * *Files 8% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 def main(
     audio_path: str,
     algorithm: str,
 ) -> None:
     fs, a = util.load_wav(audio_path)
     if algorithm == 'ensemble':
         alg = Ensemble(a, fs, algorithms=algorithms.ALGORITHMS)
-        algorithms_cache = {k.name(): F0(alg.t, alg.f0) for k, alg in alg._algorithms.items()}
+        algorithms_cache = {k.name(): F0(t=alg.t, f0=alg.f0) for k, alg in alg._algorithms.items()}
         vm = vote_and_median(algorithms_cache, alg.seconds)
         assert np.array_equal(alg.t, vm.t)
         assert np.array_equal(alg.f0, vm.f0, equal_nan=True)
     else:
         alg = getattr(algorithms, os.environ['PITCH_DETECTORS_ALGORITHM'])(a, fs)
 
     assert alg.f0.shape == alg.t.shape
```

### Comparing `pitch-detectors-0.5.0/tests/algorithms_test.py` & `pitch-detectors-0.5.1/tests/algorithms_test.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/tests/conftest.py` & `pitch-detectors-0.5.1/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.0/tests/gpu_test.py` & `pitch-detectors-0.5.1/tests/gpu_test.py`

 * *Files identical despite different names*

