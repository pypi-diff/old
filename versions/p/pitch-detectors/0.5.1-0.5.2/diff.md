# Comparing `tmp/pitch-detectors-0.5.1.tar.gz` & `tmp/pitch-detectors-0.5.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pitch-detectors-0.5.1.tar", last modified: Fri Apr  7 07:23:29 2023, max compression
+gzip compressed data, was "pitch-detectors-0.5.2.tar", last modified: Fri Apr  7 09:43:36 2023, max compression
```

## Comparing `pitch-detectors-0.5.1.tar` & `pitch-detectors-0.5.2.tar`

### file list

```diff
@@ -1,53 +1,53 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5654 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.626106 pitch-detectors-0.5.1/pitch_detectors/
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/pitch_detectors/algorithms/
--rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2611 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/crepe.py
--rw-r--r--   0 runner    (1001) docker     (123)     2993 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/ensemble.py
--rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/penn.py
--rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/piptrack.py
--rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/praatac.py
--rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/praatcc.py
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/praatshs.py
--rw-r--r--   0 runner    (1001) docker     (123)      745 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/pyin.py
--rw-r--r--   0 runner    (1001) docker     (123)      632 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/rapt.py
--rw-r--r--   0 runner    (1001) docker     (123)      799 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/reaper.py
--rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/spice.py
--rw-r--r--   0 runner    (1001) docker     (123)      635 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/swipe.py
--rw-r--r--   0 runner    (1001) docker     (123)     1396 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/torchcrepe.py
--rw-r--r--   0 runner    (1001) docker     (123)      713 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/torchyin.py
--rw-r--r--   0 runner    (1001) docker     (123)      486 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/world.py
--rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/yaapt.py
--rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/algorithms/yin.py
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/pitch_detectors/evaluation/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/mdb_stem_synth.py
--rw-r--r--   0 runner    (1001) docker     (123)     1447 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/mir_1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3752 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/evaluation/table.py
--rw-r--r--   0 runner    (1001) docker     (123)      437 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pitch_detectors/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.626106 pitch-detectors-0.5.1/pitch_detectors.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      353 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 07:23:29.000000 pitch-detectors-0.5.1/pitch_detectors.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     4580 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)     1246 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/scripts/run_algorithm.py
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:29.630106 pitch-detectors-0.5.1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/algorithms_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     1046 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)      341 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/ensemble_test.py
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-07 07:23:14.000000 pitch-detectors-0.5.1/tests/gpu_test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:36.959754 pitch-detectors-0.5.2/
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-07 09:43:36.959754 pitch-detectors-0.5.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5654 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:36.951753 pitch-detectors-0.5.2/pitch_detectors/
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:36.955754 pitch-detectors-0.5.2/pitch_detectors/algorithms/
+-rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2611 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/crepe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3095 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/ensemble.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/penn.py
+-rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/piptrack.py
+-rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/praatac.py
+-rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/praatcc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/praatshs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      745 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/pyin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      632 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/rapt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      799 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/reaper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/spice.py
+-rw-r--r--   0 runner    (1001) docker     (123)      635 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/swipe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1396 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/torchcrepe.py
+-rw-r--r--   0 runner    (1001) docker     (123)      713 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/torchyin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      486 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/world.py
+-rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/yaapt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/algorithms/yin.py
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:36.955754 pitch-detectors-0.5.2/pitch_detectors/evaluation/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/evaluation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/evaluation/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:36.955754 pitch-detectors-0.5.2/pitch_detectors/evaluation/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/evaluation/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/evaluation/datasets/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/evaluation/datasets/mdb_stem_synth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1447 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/evaluation/datasets/mir_1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3752 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/evaluation/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)      762 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pitch_detectors/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:36.951753 pitch-detectors-0.5.2/pitch_detectors.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-07 09:43:36.000000 pitch-detectors-0.5.2/pitch_detectors.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-04-07 09:43:36.000000 pitch-detectors-0.5.2/pitch_detectors.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 09:43:36.000000 pitch-detectors-0.5.2/pitch_detectors.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      353 2023-04-07 09:43:36.000000 pitch-detectors-0.5.2/pitch_detectors.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 09:43:36.000000 pitch-detectors-0.5.2/pitch_detectors.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     4615 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:36.955754 pitch-detectors-0.5.2/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)     1246 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/scripts/run_algorithm.py
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 09:43:36.959754 pitch-detectors-0.5.2/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:36.959754 pitch-detectors-0.5.2/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/tests/algorithms_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1051 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)      341 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/tests/ensemble_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-07 09:43:18.000000 pitch-detectors-0.5.2/tests/gpu_test.py
```

### Comparing `pitch-detectors-0.5.1/README.md` & `pitch-detectors-0.5.2/README.md`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/__init__.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/__init__.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/base.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/base.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/crepe.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/crepe.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/ensemble.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/ensemble.py`

 * *Files 5% similar despite different names*

```diff
@@ -26,14 +26,16 @@
     single_n = int(seconds * pitch_fs)
     t_resampled = np.linspace(0, seconds, single_n)
     f0_resampled = {}
     F0_arr = np.empty((len(algorithms), single_n))
     for i, (name, data) in enumerate(algorithms.items()):
         t = data.t
         f0 = data.f0
+        if len(f0) == 0:
+            raise ValueError(f'algorithm {name} returned an empty f0 array')
         f0_resampled[name] = np.full_like(t_resampled, fill_value=np.nan)
         notna_slices = np.ma.clump_unmasked(np.ma.masked_invalid(f0))
 
         for sl in notna_slices:
             t_slice = t[sl]
             f0_slice = f0[sl]
             t_start, t_stop = t_slice[0], t_slice[-1]
```

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/penn.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/penn.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/piptrack.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/piptrack.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/praatac.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/praatac.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/praatcc.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/praatcc.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/praatshs.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/praatshs.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/pyin.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/pyin.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/rapt.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/rapt.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/reaper.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/reaper.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/spice.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/spice.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/swipe.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/swipe.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/torchcrepe.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/torchcrepe.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/torchyin.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/torchyin.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/yaapt.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/yaapt.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/algorithms/yin.py` & `pitch-detectors-0.5.2/pitch_detectors/algorithms/yin.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/evaluation/__main__.py` & `pitch-detectors-0.5.2/pitch_detectors/evaluation/__main__.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/base.py` & `pitch-detectors-0.5.2/pitch_detectors/evaluation/datasets/base.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/mdb_stem_synth.py` & `pitch-detectors-0.5.2/pitch_detectors/evaluation/datasets/mdb_stem_synth.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/evaluation/datasets/mir_1k.py` & `pitch-detectors-0.5.2/pitch_detectors/evaluation/datasets/mir_1k.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/evaluation/table.py` & `pitch-detectors-0.5.2/pitch_detectors/evaluation/table.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors/util.py` & `pitch-detectors-0.5.2/pitch_detectors/util.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pitch_detectors.egg-info/SOURCES.txt` & `pitch-detectors-0.5.2/pitch_detectors.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/pyproject.toml` & `pitch-detectors-0.5.2/pyproject.toml`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "pitch-detectors"
-version = "0.5.1"
+version = "0.5.2"
 authors = [
     {name = "Alexander Rodionov", email = "tandav@tandav.me"},
 ]
 description = "collection of pitch detection algorithms with unified interface"
 requires-python = ">=3.8,<3.11"
 dependencies = [
     "AMFM-decompy",
@@ -63,15 +63,15 @@
 
 [tool.setuptools.packages.find]
 exclude = ["data*"]
 
 # ==============================================================================
 
 [tool.bumpver]
-current_version = "v0.5.1"
+current_version = "v0.5.2"
 version_pattern = "vMAJOR.MINOR.PATCH"
 commit_message = "bump version {old_version} -> {new_version}"
 commit = true
 tag = true
 
 [tool.bumpver.file_patterns]
 "pyproject.toml" = [
@@ -104,14 +104,17 @@
 strict_optional = true
 warn_no_return = true
 warn_redundant_casts = true
 warn_return_any = true
 warn_unreachable = true
 warn_unused_configs = true
 warn_unused_ignores = true
+plugins = [
+    "pydantic.mypy",
+]
 
 [[tool.mypy.overrides]]
 module = ["tests.*"]
 disallow_untyped_defs = false
 
 # ==============================================================================
```

### Comparing `pitch-detectors-0.5.1/scripts/run_algorithm.py` & `pitch-detectors-0.5.2/scripts/run_algorithm.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/tests/algorithms_test.py` & `pitch-detectors-0.5.2/tests/algorithms_test.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.5.1/tests/conftest.py` & `pitch-detectors-0.5.2/tests/conftest.py`

 * *Files 2% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 from pitch_detectors import util
 from pitch_detectors.schemas import Record
 
 
 @pytest.fixture
 def record():
     fs, a = util.load_wav(Path(__file__).parent.parent / 'data' / 'b1a5da49d564a7341e7e1327aa3f229a.wav')
-    return Record(fs, a)
+    return Record(fs=fs, a=a)
 
 
 @pytest.fixture
 def environ():
     env = {
         'PITCH_DETECTORS_GPU_MEMORY_LIMIT': 'true',
         'LD_LIBRARY_PATH': util.ld_library_path(),
```

### Comparing `pitch-detectors-0.5.1/tests/gpu_test.py` & `pitch-detectors-0.5.2/tests/gpu_test.py`

 * *Files identical despite different names*

