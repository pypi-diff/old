# Comparing `tmp/event_vision_library-0.0.0a0.tar.gz` & `tmp/event_vision_library-0.0.0b0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "event_vision_library-0.0.0a0.tar", max compression
+gzip compressed data, was "event_vision_library-0.0.0b0.tar", max compression
```

## Comparing `event_vision_library-0.0.0a0.tar` & `event_vision_library-0.0.0b0.tar`

### file list

```diff
@@ -1,23 +1,40 @@
--rw-r--r--   0        0        0     1070 2023-03-27 15:18:24.186641 event_vision_library-0.0.0a0/LICENSE
--rw-r--r--   0        0        0     3265 2023-03-27 15:18:24.186641 event_vision_library-0.0.0a0/README.md
--rw-r--r--   0        0        0     2260 2023-03-27 15:18:43.467204 event_vision_library-0.0.0a0/pyproject.toml
--rw-r--r--   0        0        0       28 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/__init__.py
--rw-r--r--   0        0        0       28 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/__init__.py
--rw-r--r--   0        0        0      229 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/block_access.py
--rw-r--r--   0        0        0      495 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/fileformat/__init__.py
--rw-r--r--   0        0        0        0 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/fileformat/_block_access.py
--rw-r--r--   0        0        0      319 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/fileformat/_iterator_access.py
--rw-r--r--   0        0        0     2661 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/fileformat/aedat.py
--rw-r--r--   0        0        0     2308 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/fileformat/conversion.py
--rw-r--r--   0        0        0      603 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/fileformat/evk.py
--rw-r--r--   0        0        0     2084 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/fileformat/hdf5.py
--rw-r--r--   0        0        0        0 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/fileformat/npy.py
--rw-r--r--   0        0        0     3342 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/fileformat/text.py
--rw-r--r--   0        0        0      238 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/codec/iterator_access.py
--rw-r--r--   0        0        0       28 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/processing/__init__.py
--rw-r--r--   0        0        0        0 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/py.typed
--rw-r--r--   0        0        0      145 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/representation/__init__.py
--rw-r--r--   0        0        0     1811 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/representation/histogram.py
--rw-r--r--   0        0        0     1462 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/representation/time_map.py
--rw-r--r--   0        0        0     2225 2023-03-27 15:18:24.190641 event_vision_library-0.0.0a0/src/evlib/representation/voxel_grid.py
--rw-r--r--   0        0        0     4367 1970-01-01 00:00:00.000000 event_vision_library-0.0.0a0/PKG-INFO
+-rw-r--r--   0        0        0     1070 2023-04-06 15:28:48.708961 event_vision_library-0.0.0b0/LICENSE
+-rw-r--r--   0        0        0     3265 2023-04-06 15:28:48.708961 event_vision_library-0.0.0b0/README.md
+-rw-r--r--   0        0        0     2802 2023-04-06 15:29:00.281004 event_vision_library-0.0.0b0/pyproject.toml
+-rw-r--r--   0        0        0      111 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/__init__.py
+-rw-r--r--   0        0        0    23618 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/_version.py
+-rw-r--r--   0        0        0       21 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/__init__.py
+-rw-r--r--   0        0        0      265 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/block_access.py
+-rw-r--r--   0        0        0      552 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/fileformat/__init__.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/fileformat/_block_access.py
+-rw-r--r--   0        0        0      319 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/fileformat/_iterator_access.py
+-rw-r--r--   0        0        0     2560 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/fileformat/aedat.py
+-rw-r--r--   0        0        0     2712 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/fileformat/conversion.py
+-rw-r--r--   0        0        0      677 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/fileformat/evk.py
+-rw-r--r--   0        0        0     2155 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/fileformat/hdf5.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/fileformat/npy.py
+-rw-r--r--   0        0        0     3362 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/fileformat/text.py
+-rw-r--r--   0        0        0      274 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/codec/iterator_access.py
+-rw-r--r--   0        0        0      131 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/constant.py
+-rw-r--r--   0        0        0       25 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/__init__.py
+-rw-r--r--   0        0        0       90 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/__init__.py
+-rw-r--r--   0        0        0     4673 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/__init__.py
+-rw-r--r--   0        0        0      821 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/base_model.py
+-rw-r--r--   0        0        0     3453 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/image_reconstructor.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/model/__init__.py
+-rw-r--r--   0        0        0     2971 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/model/model.py
+-rw-r--r--   0        0        0     8677 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/model/submodules.py
+-rw-r--r--   0        0        0     7788 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/model/unet.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/utils/__init__.py
+-rw-r--r--   0        0        0     7154 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/utils/inference_utils.py
+-rw-r--r--   0        0        0      871 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/processing/reconstruction/e2vid_module/utils/loading_utils.py
+-rw-r--r--   0        0        0        0 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/py.typed
+-rw-r--r--   0        0        0      182 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/representation/__init__.py
+-rw-r--r--   0        0        0     1787 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/representation/histogram.py
+-rw-r--r--   0        0        0     1430 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/representation/time_map.py
+-rw-r--r--   0        0        0     2201 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/representation/voxel_grid.py
+-rw-r--r--   0        0        0       33 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/utils/__init__.py
+-rw-r--r--   0        0        0     1062 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/utils/basics.py
+-rw-r--r--   0        0        0      638 2023-04-06 15:28:48.712962 event_vision_library-0.0.0b0/src/evlib/version.py
+-rw-r--r--   0        0        0     4722 1970-01-01 00:00:00.000000 event_vision_library-0.0.0b0/PKG-INFO
```

### Comparing `event_vision_library-0.0.0a0/LICENSE` & `event_vision_library-0.0.0b0/LICENSE`

 * *Files identical despite different names*

### Comparing `event_vision_library-0.0.0a0/README.md` & `event_vision_library-0.0.0b0/README.md`

 * *Files identical despite different names*

### Comparing `event_vision_library-0.0.0a0/pyproject.toml` & `event_vision_library-0.0.0b0/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,36 +1,49 @@
 [tool.poetry]
 name = "event-vision-library"
-version = "0.0.0a"
+version = "0.0.0b"
 description = "Event Vision Library"
 authors = ["Shintaro Shiba <shiba.shintaro@gmail.com>", "Friedhelm Hamann <friedhelmha2@gmail.com>"]
+maintainers = [
+    "Shintaro Shiba <shiba.shintaro@gmail.com>",
+    "Friedhelm Hamann <friedhelmha2@gmail.com>",
+]
 license = "MIT"
 readme = "README.md"
 homepage = "https://github.com/shiba24/event-vision-library"
 repository = "https://github.com/shiba24/event-vision-library"
 documentation = "https://event-vision-library.readthedocs.io"
 packages = [
     { include = "evlib", from = "src" },
 ]
 classifiers = [
-    "Development Status :: 1 - Planning",
+    "Development Status :: 2 - Pre-Alpha",
 ]
 
 [tool.poetry.urls]
 Changelog = "https://github.com/shiba24/event-vision-library/releases"
 
 [tool.poetry.dependencies]
 python = "^3.7,<3.11"
 click = ">=8.0.1"
 wheel = ">=0.38.4"
 numpy = ">=1.21.2"
 h5py = ">=3.2"
 expelliarmus = ">=1.1.12"
 dv = ">=1.0.11"
 opencv-python = ">=4.6"
+scipy = [
+    {version = "==1.9.1", python = ">=3.8,<3.11"},
+    {version = "<=1.9.1", python = "==3.7"}
+]  # TODO check newer version of scipy
+torch = [
+    {version = ">=2.0.0", python = ">=3.8,<3.11"},
+    {version = "<=2.0.0", python = "==3.7"}
+]  # TODO check newer version of torch
+# check https://github.com/python-poetry/poetry/issues/6409 and https://github.com/pytorch/pytorch/issues/76557
 
 [tool.poetry.dev-dependencies]
 Pygments = ">=2.10.0"
 black = ">=21.10b0"
 coverage = {extras = ["toml"], version = ">=6.2"}
 darglint = ">=1.8.1"
 flake8 = ">=4.0.1"
@@ -86,11 +99,12 @@
 show_column_numbers = true
 show_error_codes = true
 show_error_context = true
 allow_untyped_calls = true
 ignore_missing_imports = true
 disallow_any_generics = false
 mypy_path = "src"
+implicit_reexport = true
 
 [build-system]
 requires = ["poetry-core>=1.0.0"]
 build-backend = "poetry.core.masonry.api"
```

### Comparing `event_vision_library-0.0.0a0/src/evlib/codec/fileformat/aedat.py` & `event_vision_library-0.0.0b0/src/evlib/codec/fileformat/aedat.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,7 +1,9 @@
+"""aedat file formats, mainly for DV software by iniVation.
+"""
 import logging
 from typing import Any
 from typing import Dict
 
 import dv
 import numpy as np
 from dv import AedatFile
@@ -34,31 +36,28 @@
 
     def __next__(self) -> Dict[str, Any]:
         """
         Returns:
             dict: {"x", "y", "t", "p": all np.ndarray (N)}
         """
         ev = self.file_iter.__next__()
-        return {"x": ev["y"], "y": ev["x"], "t": ev["timestamp"], "p": ev["polarity"]}
+        return {"x": ev["x"], "y": ev["y"], "t": ev["timestamp"], "p": ev["polarity"]}
 
 
 class IteratorAedat4Trigger(IteratorAedat4):
     def __init__(self, aedat4file: str) -> None:
         super().__init__(aedat4file)
         self.file_iter = self.file["triggers"]
 
     def __next__(self) -> Dict[str, Any]:
         """
         Returns:
             dict: {"trigger": (1, 2)}
         """
         tr = self.file_iter.__next__()
-        # print('-=-=-', tr, tr.type)
-        # trigger_type = np.array([trig.type for trig in tr])
-        # trigger_ts = np.array([trig.timestamp for trig in tr])
         trigger = np.array([[tr.timestamp, tr.type]], dtype=np.float64)
         return {"trigger": trigger, "num": len(trigger)}
 
 
 class IteratorAedat4Imu(IteratorAedat4):
     def __init__(self, aedat4file: str) -> None:
         super().__init__(aedat4file)
```

### Comparing `event_vision_library-0.0.0a0/src/evlib/codec/fileformat/conversion.py` & `event_vision_library-0.0.0b0/src/evlib/codec/fileformat/conversion.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,7 +1,9 @@
+"""conversion functions across different formats.
+"""
 import logging
 from typing import Any
 from typing import Dict
 from typing import List
 from typing import Tuple
 
 import h5py
@@ -10,14 +12,16 @@
 from ._iterator_access import IteratorAccess
 from .hdf5 import hdf5append
 
 
 logger = logging.getLogger(__name__)
 
 
+# TODO this file should be abstracted layer of each fileformat R/W.
+# Move this function to hdf5
 def convert_iterator_access_to_hdf5(
     iterator_access: IteratorAccess,
     hdf5file: str,
     key_pairs: Dict[str, str],
     image_keys: List[str] = [],
 ) -> int:
     """Convert IteratorAccess data format into HDF5 format.
@@ -60,7 +64,16 @@
                         )
             else:
                 for (k, v) in key_pairs.items():
                     hdf5append(f[v], iter_data[k])
             i += len(iter_data)
     logger.info(f"Done. Total {i} data points are processed.")
     return i
+
+
+# TODO this file should be abstracted layer of each fileformat R/W.
+# Move this function to text
+def write_to_text(
+    event: np.ndarray,
+    file_name: str
+) -> None:
+    np.savetxt(file_name, event[:, [2, 1, 0, 3]], fmt=['%.9f', '%d', '%d', '%d'])
```

### Comparing `event_vision_library-0.0.0a0/src/evlib/codec/fileformat/hdf5.py` & `event_vision_library-0.0.0b0/src/evlib/codec/fileformat/hdf5.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,7 +1,9 @@
+"""hdf5 formats for various existing datasets.
+"""
 import logging
 from typing import Any
 from typing import Dict
 from typing import List
 from typing import Tuple
 from typing import Union
 
@@ -20,14 +22,15 @@
     """Load all the contents of .hdf5 file at once.
     Args:
         path (str) ... Path to the .hdf5 file.
         key_dtype_pairs (list of tuple) ... A triplet, or list of triplets of
             (key of the return dictionary, key of the hdf5 file data, data type for numpy).
             For example,
             [("ts", "raw_events/ts", np.int32), ("x", "raw_events/x", np.int16), ...]
+
     Returns:
         dict ... {key of the return dictionary: np.ndarray}
     """
     if isinstance(key_dtype_pairs, tuple):
         key_dtype_pairs = [key_dtype_pairs]  # make it list.
     f = h5py.File(path, "r")
     data = {k: np.array(f[v], dtype=t) for (k, v, t) in key_dtype_pairs}
@@ -35,29 +38,32 @@
     return data
 
 
 def open_hdf5(path: str) -> Any:
     """Open .hdf5 file, not to load them at once.
     Args:
         path (str) ... Path to the .hdf5 file.
+
     Returns:
         (Any) opened hdf5 object.
     """
     return h5py.File(path, "r")
 
 
 def load_event_timestamp_hdf5(
     path: str, key_pairs: Tuple[str, str], dtype: type = np.int32
 ) -> Dict[str, np.ndarray]:
     """For utility: load only timestamps from the hdf5 data.
     Args:
         path (str) ... Path to the .hdf5 file.
         key_pairs  ... The tuple of
             (key of the return dictionary, key of the hdf5 file data)
+    
     Returns:
+        dict
     """
     data = load_hdf5(path, list(key_pairs + (dtype,)))  # type: ignore
     if np.max(data[key_pairs[0]]) == np.iinfo(dtype):
         w = f"Please check the size of the data and data type. {dtype} may not be enough."
         logger.warning(w)
     return data
```

### Comparing `event_vision_library-0.0.0a0/src/evlib/codec/fileformat/text.py` & `event_vision_library-0.0.0b0/src/evlib/codec/fileformat/text.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,7 +1,9 @@
+"""Text format.
+"""
 import logging
 import os
 from typing import Any
 from typing import Dict
 from typing import List
 
 import cv2
@@ -49,16 +51,16 @@
         x = np.zeros((_l,), dtype=np.int32)
         y = np.zeros((_l,), dtype=np.int32)
         t = np.zeros((_l,), dtype=np.float64)
         p = np.zeros((_l,), dtype=bool)
         for _i, line in enumerate(lines):
             val = line.split()
             t[_i] = np.float64(val[0])
-            x[_i] = int(val[2])
-            y[_i] = int(val[1])
+            x[_i] = int(val[1])
+            y[_i] = int(val[2])
             p[_i] = int(val[3])
         self.count += _l
         return {"x": x, "y": y, "t": t, "p": p, "num": _l}
 
 
 class IteratorTextPose(IteratorText):
     def __next__(self) -> Dict[str, Any]:
```

### Comparing `event_vision_library-0.0.0a0/src/evlib/representation/histogram.py` & `event_vision_library-0.0.0b0/src/evlib/representation/histogram.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 from typing import Any
 from typing import Tuple
 
 import numpy as np
 
 
 class Histogram:
-    def __init__(self, image_shape: Tuple[int, int], use_polarity: bool = True) -> None:
-        """Create a 2D histogram from event camera data.
+    """Create a 2D histogram from event camera data.
 
-        Args:
-            image_shape: (height, width)
-            use_polarity: if True, counts every positive events as +1
-                          and every negative events as -1, if False,
-                          counts every events as +1
-        """
+    Args:
+        image_shape: (height, width)
+        use_polarity: if True, counts every positive events as +1
+                        and every negative events as -1, if False,
+                        counts every events as +1
+    """
+    def __init__(self, image_shape: Tuple[int, int], use_polarity: bool = True) -> None:
         assert image_shape[0] > 0
         assert image_shape[1] > 0
         self.image_shape = image_shape
         self.use_polarity = use_polarity
 
     def _make_histogram(self, events: np.ndarray) -> np.ndarray:
         y = events[:, 0].astype(int)
```

### Comparing `event_vision_library-0.0.0a0/src/evlib/representation/time_map.py` & `event_vision_library-0.0.0b0/src/evlib/representation/time_map.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,25 +1,25 @@
 from typing import Any
 from typing import Tuple
 
 import numpy as np
 
 
 class TimeMap:
+    """Create a time map of events. Adapted from:
+    Lagorce, Xavier, et al. "Hots: a hierarchy of event-based time-surfaces for pattern recognition."
+    IEEE transactions on pattern analysis and machine intelligence 39.7 (2016): 1346-1359.
+
+    Note that this implementation is a "random access implementation" and does not hold a state.
+
+    Args:
+        image_shape: (height, width)
+        decay: the factor in the exponential. A higher value leads to a stronger decay (sharper edges).
+    """
     def __init__(self, image_shape: Tuple[int, int], decay: float) -> None:
-        """Create a time map of events. Adapted from:
-        Lagorce, Xavier, et al. "Hots: a hierarchy of event-based time-surfaces for pattern recognition."
-        IEEE transactions on pattern analysis and machine intelligence 39.7 (2016): 1346-1359.
-
-        Note that this implementation is a "random access implementation" and does not hold a state.
-
-        Args:
-            image_shape: (height, width)
-            decay: the factor in the exponential. A higher value leads to a stronger decay (sharper edges).
-        """
         assert image_shape[0] > 0
         assert image_shape[1] > 0
         self.image_shape = image_shape
         self.decay = decay
 
     def __call__(self, events: np.ndarray) -> np.ndarray:
         """Create time map.
```

### Comparing `event_vision_library-0.0.0a0/src/evlib/representation/voxel_grid.py` & `event_vision_library-0.0.0b0/src/evlib/representation/voxel_grid.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 from typing import Any
 from typing import Tuple
 
 import numpy as np
 
 
 class VoxelGrid:
-    def __init__(self, image_shape: Tuple[int, int], num_bins: int) -> None:
-        """Create a voxel grid from events.
-        Implementation inspired by https://github.com/uzh-rpg/rpg_e2vid.
+    """Create a voxel grid from events.
+    Implementation inspired by https://github.com/uzh-rpg/rpg_e2vid.
 
-        Args:
-            image_shape: (height, width)
-            num_bins: number of bins in the temporal axis of the voxel grid
-        """
+    Args:
+        image_shape: (height, width)
+        num_bins: number of bins in the temporal axis of the voxel grid
+    """
+    def __init__(self, image_shape: Tuple[int, int], num_bins: int) -> None:
         assert image_shape[0] > 0
         assert image_shape[1] > 0
         assert num_bins > 0
         self.image_shape = image_shape
         self.num_bins = num_bins
 
     def __call__(self, events: np.ndarray) -> np.ndarray:
```

### Comparing `event_vision_library-0.0.0a0/PKG-INFO` & `event_vision_library-0.0.0b0/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,29 +1,35 @@
 Metadata-Version: 2.1
 Name: event-vision-library
-Version: 0.0.0a0
+Version: 0.0.0b0
 Summary: Event Vision Library
 Home-page: https://github.com/shiba24/event-vision-library
 License: MIT
 Author: Shintaro Shiba
 Author-email: shiba.shintaro@gmail.com
+Maintainer: Shintaro Shiba
+Maintainer-email: shiba.shintaro@gmail.com
 Requires-Python: >=3.7,<3.11
-Classifier: Development Status :: 1 - Planning
+Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Requires-Dist: click (>=8.0.1)
 Requires-Dist: dv (>=1.0.11)
 Requires-Dist: expelliarmus (>=1.1.12)
 Requires-Dist: h5py (>=3.2)
 Requires-Dist: numpy (>=1.21.2)
 Requires-Dist: opencv-python (>=4.6)
+Requires-Dist: scipy (<=1.9.1) ; python_version == "3.7"
+Requires-Dist: scipy (==1.9.1) ; python_version >= "3.8" and python_version < "3.11"
+Requires-Dist: torch (<=2.0.0) ; python_version == "3.7"
+Requires-Dist: torch (>=2.0.0) ; python_version >= "3.8" and python_version < "3.11"
 Requires-Dist: wheel (>=0.38.4)
 Project-URL: Changelog, https://github.com/shiba24/event-vision-library/releases
 Project-URL: Documentation, https://event-vision-library.readthedocs.io
 Project-URL: Repository, https://github.com/shiba24/event-vision-library
 Description-Content-Type: text/markdown
 
 # Event Vision Library
```

