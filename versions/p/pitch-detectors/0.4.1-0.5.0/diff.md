# Comparing `tmp/pitch-detectors-0.4.1.tar.gz` & `tmp/pitch-detectors-0.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pitch-detectors-0.4.1.tar", last modified: Wed Apr  5 05:12:50 2023, max compression
+gzip compressed data, was "pitch-detectors-0.5.0.tar", last modified: Thu Apr  6 18:11:42 2023, max compression
```

## Comparing `pitch-detectors-0.4.1.tar` & `pitch-detectors-0.5.0.tar`

### file list

```diff
@@ -1,53 +1,53 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:50.246020 pitch-detectors-0.4.1/
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-05 05:12:50.246020 pitch-detectors-0.4.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5654 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:50.238020 pitch-detectors-0.4.1/pitch_detectors/
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:50.246020 pitch-detectors-0.4.1/pitch_detectors/algorithms/
--rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2611 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/base.py
--rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/crepe.py
--rw-r--r--   0 runner    (1001) docker     (123)     3146 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/ensemble.py
--rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/penn.py
--rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/piptrack.py
--rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/praatac.py
--rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/praatcc.py
--rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/praatshs.py
--rw-r--r--   0 runner    (1001) docker     (123)      745 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/pyin.py
--rw-r--r--   0 runner    (1001) docker     (123)      632 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/rapt.py
--rw-r--r--   0 runner    (1001) docker     (123)      799 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/reaper.py
--rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/spice.py
--rw-r--r--   0 runner    (1001) docker     (123)      635 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/swipe.py
--rw-r--r--   0 runner    (1001) docker     (123)     1396 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/torchcrepe.py
--rw-r--r--   0 runner    (1001) docker     (123)      713 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/torchyin.py
--rw-r--r--   0 runner    (1001) docker     (123)      486 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/world.py
--rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/yaapt.py
--rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/algorithms/yin.py
--rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/config.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:50.246020 pitch-detectors-0.4.1/pitch_detectors/evaluation/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/evaluation/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/evaluation/__main__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:50.246020 pitch-detectors-0.4.1/pitch_detectors/evaluation/datasets/
--rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/evaluation/datasets/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/evaluation/datasets/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/evaluation/datasets/mdb_stem_synth.py
--rw-r--r--   0 runner    (1001) docker     (123)     1447 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/evaluation/datasets/mir_1k.py
--rw-r--r--   0 runner    (1001) docker     (123)     3752 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/evaluation/table.py
--rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pitch_detectors/util.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:50.242020 pitch-detectors-0.4.1/pitch_detectors.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-05 05:12:50.000000 pitch-detectors-0.4.1/pitch_detectors.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-04-05 05:12:50.000000 pitch-detectors-0.4.1/pitch_detectors.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-05 05:12:50.000000 pitch-detectors-0.4.1/pitch_detectors.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      344 2023-04-05 05:12:50.000000 pitch-detectors-0.4.1/pitch_detectors.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-05 05:12:50.000000 pitch-detectors-0.4.1/pitch_detectors.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     4557 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:50.246020 pitch-detectors-0.4.1/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)     1385 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/scripts/run_algorithm.py
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-05 05:12:50.246020 pitch-detectors-0.4.1/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:50.246020 pitch-detectors-0.4.1/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/tests/algorithms_test.py
--rw-r--r--   0 runner    (1001) docker     (123)     1046 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)      341 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/tests/ensemble_test.py
--rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-05 05:12:32.000000 pitch-detectors-0.4.1/tests/gpu_test.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5654 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.229628 pitch-detectors-0.5.0/pitch_detectors/
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/pitch_detectors/algorithms/
+-rw-r--r--   0 runner    (1001) docker     (123)     1345 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2611 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)      658 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/crepe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2993 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/ensemble.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1455 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/penn.py
+-rw-r--r--   0 runner    (1001) docker     (123)      869 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/piptrack.py
+-rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/praatac.py
+-rw-r--r--   0 runner    (1001) docker     (123)      790 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/praatcc.py
+-rw-r--r--   0 runner    (1001) docker     (123)      789 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/praatshs.py
+-rw-r--r--   0 runner    (1001) docker     (123)      745 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/pyin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      632 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/rapt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      799 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/reaper.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1706 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/spice.py
+-rw-r--r--   0 runner    (1001) docker     (123)      635 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/swipe.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1396 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/torchcrepe.py
+-rw-r--r--   0 runner    (1001) docker     (123)      713 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/torchyin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      486 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/world.py
+-rw-r--r--   0 runner    (1001) docker     (123)      797 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/yaapt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      725 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/algorithms/yin.py
+-rw-r--r--   0 runner    (1001) docker     (123)       25 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/config.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/pitch_detectors/evaluation/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3787 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/
+-rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      751 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/mdb_stem_synth.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1447 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/mir_1k.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3752 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/evaluation/table.py
+-rw-r--r--   0 runner    (1001) docker     (123)      317 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2158 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pitch_detectors/util.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.229628 pitch-detectors-0.5.0/pitch_detectors.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      445 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1459 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      344 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 18:11:42.000000 pitch-detectors-0.5.0/pitch_detectors.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     4564 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)     1241 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/scripts/run_algorithm.py
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:42.233629 pitch-detectors-0.5.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1589 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/algorithms_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1046 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)      341 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/ensemble_test.py
+-rw-r--r--   0 runner    (1001) docker     (123)      646 2023-04-06 18:11:28.000000 pitch-detectors-0.5.0/tests/gpu_test.py
```

### Comparing `pitch-detectors-0.4.1/README.md` & `pitch-detectors-0.5.0/README.md`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/__init__.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/__init__.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/base.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/base.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/crepe.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/crepe.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/ensemble.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/ensemble.py`

 * *Files 9% similar despite different names*

```diff
@@ -8,69 +8,78 @@
 from pitch_detectors.algorithms.base import TorchGPU
 from pitch_detectors.schemas import F0
 
 PDT: TypeAlias = type[PitchDetector]
 AlgoDict: TypeAlias = dict[PDT, PitchDetector] | dict[PDT, F0] | dict
 
 
+def vote_and_median(
+    algorithms: dict[str, F0],
+    seconds: float,
+    pitch_fs: int = 1024,
+    min_duration: float = 1,
+    min_algorithms: int = 3,
+    # algorithm_weights: dict[str, float] = {},
+) -> F0:
+    if len(algorithms) < min_algorithms:
+        raise ValueError(f'at least {min_algorithms} algorithms must be provided, because min_algorithms={min_algorithms}')
+
+    single_n = int(seconds * pitch_fs)
+    t_resampled = np.linspace(0, seconds, single_n)
+    f0_resampled = {}
+    F0_arr = np.empty((len(algorithms), single_n))
+    for i, (name, data) in enumerate(algorithms.items()):
+        t = data.t
+        f0 = data.f0
+        f0_resampled[name] = np.full_like(t_resampled, fill_value=np.nan)
+        notna_slices = np.ma.clump_unmasked(np.ma.masked_invalid(f0))
+
+        for sl in notna_slices:
+            t_slice = t[sl]
+            f0_slice = f0[sl]
+            t_start, t_stop = t_slice[0], t_slice[-1]
+            duration = t_stop - t_start
+            if duration < min_duration:
+                continue
+            mask = (t_start < t_resampled) & (t_resampled < t_stop)
+            t_interp = t_resampled[mask]
+            f0_interp = np.interp(t_interp, t_slice, f0_slice)
+            f0_resampled[name][mask] = f0_interp
+        F0_arr[i] = f0_resampled[name]
+
+    F0_mask = np.isfinite(F0_arr).astype(int)
+    F0_mask_sum = F0_mask.sum(axis=0)
+    min_alg_mask = F0_mask_sum > min_algorithms
+    f0_mean = np.full_like(t_resampled, fill_value=np.nan)
+    f0_mean[min_alg_mask] = np.nanmedian(F0_arr[:, min_alg_mask], axis=0)
+    return F0(t=t_resampled, f0=f0_mean)
+
+
 class Ensemble(TensorflowGPU, TorchGPU, PitchDetector):
     """https://github.com/tandav/pitch-detectors/blob/master/pitch_detectors/algorithms/ensemble.py"""
 
     def __init__(
         self,
         a: np.ndarray,
         fs: int,
-        pitch_fs: int = 1024,
-        min_duration: float = 1,
-        min_algorithms: int = 3,
-        algorithms: tuple[PDT, ...] | None = None,
+        algorithms: tuple[PDT, ...],
         algorithms_kwargs: dict[PDT, dict[str, Any]] | None = None,
-        algorithms_cache: dict[PDT, F0] | None = None,
-        # algorithm_weights: dict[PDT, float] = {},
         gpu: bool | None = None,
+        vote_and_median_kwargs: dict[str, Any] | None = None,
     ):
         TensorflowGPU.__init__(self, gpu)
         TorchGPU.__init__(self, gpu)
         PitchDetector.__init__(self, a, fs)
 
-        if algorithms_cache is not None:
-            if (algorithms is not None or algorithms_kwargs is not None):
-                raise ValueError('algorithms and algorithms_kwargs cannot be used with algorithms_cache')
-            self._algorithms = algorithms_cache
-        elif algorithms is None:
-            raise ValueError('algorithms or algorithms_cache must be provided')
-        else:
-            self._algorithms = {}
-            algorithms_kwargs = algorithms_kwargs or {}
-
-            for algorithm_cls in algorithms:
-                self._algorithms[algorithm_cls] = algorithm_cls(a, fs, **algorithms_kwargs.get(algorithm_cls, {}))  # type: ignore
-        single_n = int(self.seconds * pitch_fs)
-        t_resampled = np.linspace(0, self.seconds, single_n)
-        f0_resampled = {}
-        F0 = np.empty((len(self._algorithms), single_n))
-        for i, (alg_cls, algorithm) in enumerate(self._algorithms.items()):
-            t = algorithm.t
-            f0 = algorithm.f0
-            f0_resampled[alg_cls] = np.full_like(t_resampled, fill_value=np.nan)
-            notna_slices = np.ma.clump_unmasked(np.ma.masked_invalid(f0))
-
-            for sl in notna_slices:
-                t_slice = t[sl]
-                f0_slice = f0[sl]
-                t_start, t_stop = t_slice[0], t_slice[-1]
-                duration = t_stop - t_start
-                if duration < min_duration:
-                    continue
-                mask = (t_start < t_resampled) & (t_resampled < t_stop)
-                t_interp = t_resampled[mask]
-                f0_interp = np.interp(t_interp, t_slice, f0_slice)
-                f0_resampled[alg_cls][mask] = f0_interp
-            F0[i] = f0_resampled[alg_cls]
-
-        F0_mask = np.isfinite(F0).astype(int)
-        F0_mask_sum = F0_mask.sum(axis=0)
-        min_alg_mask = F0_mask_sum > min_algorithms
-        f0_mean = np.full_like(t_resampled, fill_value=np.nan)
-        f0_mean[min_alg_mask] = np.nanmedian(F0[:, min_alg_mask], axis=0)
-        self.t = t_resampled
-        self.f0 = f0_mean
+        self._algorithms = {}
+        algorithms_kwargs = algorithms_kwargs or {}
+
+        for cls in algorithms:
+            self._algorithms[cls] = cls(a, fs, **algorithms_kwargs.get(cls, {}))
+
+        f0 = vote_and_median(
+            {k.name(): F0(t=v.t, f0=v.f0) for k, v in self._algorithms.items()},
+            self.seconds,
+            **(vote_and_median_kwargs or {}),
+        )
+        self.t = f0.t
+        self.f0 = f0.f0
```

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/penn.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/penn.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/piptrack.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/piptrack.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/praatac.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/praatac.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/praatcc.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/praatcc.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/praatshs.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/praatshs.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/pyin.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/pyin.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/rapt.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/rapt.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/reaper.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/reaper.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/spice.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/spice.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/swipe.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/swipe.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/torchcrepe.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/torchcrepe.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/torchyin.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/torchyin.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/yaapt.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/yaapt.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/algorithms/yin.py` & `pitch-detectors-0.5.0/pitch_detectors/algorithms/yin.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/evaluation/__main__.py` & `pitch-detectors-0.5.0/pitch_detectors/evaluation/__main__.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/evaluation/datasets/base.py` & `pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/base.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/evaluation/datasets/mdb_stem_synth.py` & `pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/mdb_stem_synth.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/evaluation/datasets/mir_1k.py` & `pitch-detectors-0.5.0/pitch_detectors/evaluation/datasets/mir_1k.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/evaluation/table.py` & `pitch-detectors-0.5.0/pitch_detectors/evaluation/table.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors/util.py` & `pitch-detectors-0.5.0/pitch_detectors/util.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pitch_detectors.egg-info/SOURCES.txt` & `pitch-detectors-0.5.0/pitch_detectors.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/pyproject.toml` & `pitch-detectors-0.5.0/pyproject.toml`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "pitch-detectors"
-version = "0.4.1"
+version = "0.5.0"
 authors = [
     {name = "Alexander Rodionov", email = "tandav@tandav.me"},
 ]
 description = "collection of pitch detection algorithms with unified interface"
 requires-python = ">=3.8,<3.11"
 dependencies = [
     "AMFM-decompy",
@@ -62,15 +62,15 @@
 
 [tool.setuptools.packages.find]
 exclude = ["data*"]
 
 # ==============================================================================
 
 [tool.bumpver]
-current_version = "v0.4.1"
+current_version = "v0.5.0"
 version_pattern = "vMAJOR.MINOR.PATCH"
 commit_message = "bump version {old_version} -> {new_version}"
 commit = true
 tag = true
 
 [tool.bumpver.file_patterns]
 "pyproject.toml" = [
@@ -180,15 +180,15 @@
 ignore="E501,E701"
 recursive = true
 aggressive = 3
 
 # ==============================================================================
 
 [tool.pyright]
-venvPath = "/home/tandav/.virtualenvs"
+venvPath = "/home/tandav/.cache/.virtualenvs"
 venv = "pitch-detectors"
 
 # ==============================================================================
 
 [tool.pytest.ini_options]
 filterwarnings = [
     "ignore:pkg_resources is deprecated as an API",
```

### Comparing `pitch-detectors-0.4.1/scripts/run_algorithm.py` & `pitch-detectors-0.5.0/scripts/run_algorithm.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,38 +1,35 @@
 import argparse
 import os
 
 import numpy as np
 
 from pitch_detectors import algorithms
 from pitch_detectors import util
+from pitch_detectors.algorithms.ensemble import Ensemble
+from pitch_detectors.algorithms.ensemble import vote_and_median
 from pitch_detectors.schemas import F0
 
 
 def main(
     audio_path: str,
     algorithm: str,
 ) -> None:
     fs, a = util.load_wav(audio_path)
     if algorithm == 'ensemble':
-        alg = algorithms.Ensemble(a, fs, algorithms=algorithms.ALGORITHMS)
+        alg = Ensemble(a, fs, algorithms=algorithms.ALGORITHMS)
+        algorithms_cache = {k.name(): F0(alg.t, alg.f0) for k, alg in alg._algorithms.items()}
+        vm = vote_and_median(algorithms_cache, alg.seconds)
+        assert np.array_equal(alg.t, vm.t)
+        assert np.array_equal(alg.f0, vm.f0, equal_nan=True)
     else:
         alg = getattr(algorithms, os.environ['PITCH_DETECTORS_ALGORITHM'])(a, fs)
 
     assert alg.f0.shape == alg.t.shape
 
-    if algorithm == 'ensemble':
-        algorithms_cache = {k: F0(alg.t, alg.f0) for k, alg in alg._algorithms.items()}
-        alg_from_cache = algorithms.Ensemble(a, fs, algorithms_cache=algorithms_cache)
-        assert np.array_equal(alg.t, alg_from_cache.t)
-        assert np.array_equal(alg.f0, alg_from_cache.f0, equal_nan=True)
-        # data = alg.dict()
-        # data['algorithms_cache'] = {k: _alg.dict() for k, _alg in alg._algorithms.items()}
-        # print(json.dumps(alg.dict(), allow_nan=True))
-
 
 if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('--audio-path', type=str, default=os.environ.get('PITCH_DETECTORS_AUDIO_PATH', 'data/b1a5da49d564a7341e7e1327aa3f229a.wav'))
     parser.add_argument('--algorithm', type=str, default=os.environ.get('PITCH_DETECTORS_ALGORITHM'))
     args = parser.parse_args()
     main(**vars(args))
```

### Comparing `pitch-detectors-0.4.1/tests/algorithms_test.py` & `pitch-detectors-0.5.0/tests/algorithms_test.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/tests/conftest.py` & `pitch-detectors-0.5.0/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `pitch-detectors-0.4.1/tests/gpu_test.py` & `pitch-detectors-0.5.0/tests/gpu_test.py`

 * *Files identical despite different names*

