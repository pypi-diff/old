# Comparing `tmp/CrossPy-0.0.0a3.dev8.tar.gz` & `tmp/CrossPy-0.0.0a3.dev9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "CrossPy-0.0.0a3.dev8.tar", last modified: Tue Mar 28 23:58:54 2023, max compression
+gzip compressed data, was "CrossPy-0.0.0a3.dev9.tar", last modified: Wed Mar 29 20:47:53 2023, max compression
```

## Comparing `CrossPy-0.0.0a3.dev8.tar` & `CrossPy-0.0.0a3.dev9.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-28 23:58:54.065385 CrossPy-0.0.0a3.dev8/
-drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-28 23:58:53.989385 CrossPy-0.0.0a3.dev8/CrossPy.egg-info/
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)      310 2023-03-28 23:58:52.000000 CrossPy-0.0.0a3.dev8/CrossPy.egg-info/PKG-INFO
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)      602 2023-03-28 23:58:52.000000 CrossPy-0.0.0a3.dev8/CrossPy.egg-info/SOURCES.txt
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)        1 2023-03-28 23:58:52.000000 CrossPy-0.0.0a3.dev8/CrossPy.egg-info/dependency_links.txt
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)        6 2023-03-28 23:58:52.000000 CrossPy-0.0.0a3.dev8/CrossPy.egg-info/requires.txt
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)        8 2023-03-28 23:58:52.000000 CrossPy-0.0.0a3.dev8/CrossPy.egg-info/top_level.txt
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     1517 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/LICENSE
--rw-r--r--   0 byou     (63260) cdgc     (64897)      310 2023-03-28 23:58:54.064385 CrossPy-0.0.0a3.dev8/PKG-INFO
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     1160 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/README.md
-drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-28 23:58:54.011385 CrossPy-0.0.0a3.dev8/crosspy/
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     4564 2023-03-28 23:52:39.000000 CrossPy-0.0.0a3.dev8/crosspy/__init__.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     2936 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/array.py
-drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-28 23:58:54.019385 CrossPy-0.0.0a3.dev8/crosspy/core/
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)       61 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/core/__init__.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)    34480 2023-03-28 23:58:27.000000 CrossPy-0.0.0a3.dev8/crosspy/core/ndarray.py
-drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-28 23:58:54.032385 CrossPy-0.0.0a3.dev8/crosspy/device/
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)      650 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/device/__init__.py
-drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-28 23:58:54.046385 CrossPy-0.0.0a3.dev8/crosspy/device/cpu/
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)      819 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/device/cpu/__init__.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     1065 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/device/cpu/component.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     4160 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/device/cpu/generic.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     2091 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/device/detail.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     6709 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/device/device.py
-drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-28 23:58:54.060385 CrossPy-0.0.0a3.dev8/crosspy/device/gpu/
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)      985 2023-03-28 19:51:03.000000 CrossPy-0.0.0a3.dev8/crosspy/device/gpu/__init__.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     6166 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/device/gpu/component.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     4983 2023-03-27 21:33:23.000000 CrossPy-0.0.0a3.dev8/crosspy/device/gpu/cuda.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)    19012 2023-03-27 21:32:44.000000 CrossPy-0.0.0a3.dev8/crosspy/ldevice.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)      296 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/mapping.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     2074 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/placement.py
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     1375 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev8/crosspy/utils.py
--rw-r--r--   0 byou     (63260) cdgc     (64897)       38 2023-03-28 23:58:54.065385 CrossPy-0.0.0a3.dev8/setup.cfg
--rwxr-xr-x   0 byou     (63260) cdgc     (64897)     8992 2023-03-28 23:58:34.000000 CrossPy-0.0.0a3.dev8/setup.py
+drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-29 20:47:53.410713 CrossPy-0.0.0a3.dev9/
+drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-29 20:47:53.332713 CrossPy-0.0.0a3.dev9/CrossPy.egg-info/
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)      310 2023-03-29 20:47:52.000000 CrossPy-0.0.0a3.dev9/CrossPy.egg-info/PKG-INFO
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)      602 2023-03-29 20:47:52.000000 CrossPy-0.0.0a3.dev9/CrossPy.egg-info/SOURCES.txt
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)        1 2023-03-29 20:47:52.000000 CrossPy-0.0.0a3.dev9/CrossPy.egg-info/dependency_links.txt
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)        6 2023-03-29 20:47:52.000000 CrossPy-0.0.0a3.dev9/CrossPy.egg-info/requires.txt
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)        8 2023-03-29 20:47:52.000000 CrossPy-0.0.0a3.dev9/CrossPy.egg-info/top_level.txt
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     1517 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/LICENSE
+-rw-r--r--   0 byou     (63260) cdgc     (64897)      310 2023-03-29 20:47:53.409713 CrossPy-0.0.0a3.dev9/PKG-INFO
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     1160 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/README.md
+drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-29 20:47:53.353713 CrossPy-0.0.0a3.dev9/crosspy/
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     5752 2023-03-29 20:46:34.000000 CrossPy-0.0.0a3.dev9/crosspy/__init__.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     2936 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/array.py
+drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-29 20:47:53.362713 CrossPy-0.0.0a3.dev9/crosspy/core/
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)       61 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/core/__init__.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)    34794 2023-03-29 20:47:10.000000 CrossPy-0.0.0a3.dev9/crosspy/core/ndarray.py
+drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-29 20:47:53.374713 CrossPy-0.0.0a3.dev9/crosspy/device/
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)      650 2023-03-29 14:47:04.000000 CrossPy-0.0.0a3.dev9/crosspy/device/__init__.py
+drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-29 20:47:53.390713 CrossPy-0.0.0a3.dev9/crosspy/device/cpu/
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)      819 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/device/cpu/__init__.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     1065 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/device/cpu/component.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     4160 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/device/cpu/generic.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     2091 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/device/detail.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     6709 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/device/device.py
+drwxr-sr-x   0 byou     (63260) cdgc     (64897)        0 2023-03-29 20:47:53.406713 CrossPy-0.0.0a3.dev9/crosspy/device/gpu/
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)      985 2023-03-28 19:51:03.000000 CrossPy-0.0.0a3.dev9/crosspy/device/gpu/__init__.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     6166 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/device/gpu/component.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     4983 2023-03-27 21:33:23.000000 CrossPy-0.0.0a3.dev9/crosspy/device/gpu/cuda.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)    19056 2023-03-29 20:18:40.000000 CrossPy-0.0.0a3.dev9/crosspy/ldevice.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)      296 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/mapping.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     2074 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/placement.py
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     1375 2023-03-24 03:54:32.000000 CrossPy-0.0.0a3.dev9/crosspy/utils.py
+-rw-r--r--   0 byou     (63260) cdgc     (64897)       38 2023-03-29 20:47:53.410713 CrossPy-0.0.0a3.dev9/setup.cfg
+-rwxr-xr-x   0 byou     (63260) cdgc     (64897)     8992 2023-03-29 20:47:43.000000 CrossPy-0.0.0a3.dev9/setup.py
```

### Comparing `CrossPy-0.0.0a3.dev8/CrossPy.egg-info/SOURCES.txt` & `CrossPy-0.0.0a3.dev9/CrossPy.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/LICENSE` & `CrossPy-0.0.0a3.dev9/LICENSE`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/README.md` & `CrossPy-0.0.0a3.dev9/README.md`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/__init__.py` & `CrossPy-0.0.0a3.dev9/crosspy/__init__.py`

 * *Files 18% similar despite different names*

```diff
@@ -23,14 +23,38 @@
 from .ldevice import PartitionScheme
 
 # from .device import get_all_devices
 # print(get_all_devices())
 
 __all__ = ['numpy', 'cupy', 'array', 'cpu', 'gpu', 'PartitionScheme']
 
+class PerObjWrapper:
+    initial_devices = {}
+    initial_shape = {}
+
+    def __init__(self, wrapper, perserve_device=False, perserve_shape=False) -> None:
+        def attr_wrapper(obj, *args, **kwds):
+            device_ = getattr(obj, "device", "cpu") if perserve_device else None
+            shape_ = getattr(obj, "shape", None) if perserve_shape else None
+
+            wrapped_obj = wrapper(obj, *args, **kwds)
+
+            if not hasattr(wrapped_obj, "device") and device_ is not None:
+                self.initial_devices[id(wrapped_obj)] = device_
+            if not hasattr(wrapped_obj, "shape") and shape_ is not None:
+                self.initial_shape[id(wrapped_obj)] = shape_
+
+            return wrapped_obj
+
+        self._wrapper = attr_wrapper
+
+    def __call__(self, obj, *args, **kwds):
+        return self._wrapper(obj, *args, **kwds)
+        
+
 def array(
     obj: Iterable,
     dtype=None,
     shape=None,
     # offset=0,
     # strides=None,
     # formats=None,
@@ -55,29 +79,32 @@
     :return: A CrossPy array.
     """
     assert obj is not None, NotImplementedError("array with no content not supported")
 
     from .array import is_array
     if is_array(obj):  # numpy, cupy, crosspy
         if partition is not None:
+            if wrapper:
+                wrapper = PerObjWrapper(wrapper, perserve_device=True, perserve_shape=True)
             obj = partition_with(obj, partition=partition, wrapper=wrapper)
             dim = 0  # TODO warning when dim is not 0
+            arr = CrossPyArray(obj, dim=dim, initial_devices=wrapper.initial_devices)
         else:
-            obj = [obj]
-        arr = CrossPyArray(obj, dim=dim)
+            arr = CrossPyArray([obj], dim=dim)
     else:
         try:
             arr = numpy.asarray(obj) # TODO: hinted by placement
         except:
             assert isinstance(obj, (list, tuple)), "assumption"
             def _recursive_parse(list_of_obj, d):
                 if all(is_array(a) for a in list_of_obj):
                     if wrapper:
+                        wrapper = PerObjWrapper(wrapper, perserve_device=True, perserve_shape=True)
                         return CrossPyArray([wrapper(obj)for obj in list_of_obj], dim=d)
-                    return CrossPyArray(list_of_obj, dim=d)
+                    return CrossPyArray(list_of_obj, dim=d, initial_devices=wrapper.initial_devices)
                 raise NotImplementedError
                 if all(isinstance(o, (list, tuple)) for o in list_of_obj):
                     d = d or 0
                     return CrossPyArray([_recursive_parse(o, d+1) for o in list_of_obj], dim=d)
             arr = _recursive_parse(obj, dim)
 
     assert isinstance(arr, CrossPyArray)
```

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/array.py` & `CrossPy-0.0.0a3.dev9/crosspy/array.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/core/ndarray.py` & `CrossPy-0.0.0a3.dev9/crosspy/core/ndarray.py`

 * *Files 1% similar despite different names*

```diff
@@ -89,15 +89,15 @@
 
 class CrossPyArray(numpy.lib.mixins.NDArrayOperatorsMixin):
     """
     Heterougeneous N-dimensional array compatible with the numpy API with custom implementations of numpy functionality.
 
     https://numpy.org/doc/stable/user/basics.dispatch.html#basics-dispatch
     """
-    def __init__(self, obj, dim: Optional[int] = None, shape = None) -> None:
+    def __init__(self, obj, dim: Optional[int] = None, shape = None, **kwargs) -> None:
         # super().__init__()
         self._original_data = obj
 
         if not isinstance(obj, (list, tuple)):
             assert dim is None, "assumption: no concat for non-list objs"
             self._shape = getattr(obj, 'shape') # TODO shortcut other attribute computation
             list_obj = [obj]
@@ -122,16 +122,22 @@
 
         self._shape = getattr(self._original_data, 'shape', self._init_shape(shapes))
 
         self._bounds = numpy.cumsum(shapes, dtype=numpy.uint64)
 
         self._device_to_indices = defaultdict(list)
         self._device_types = set()
+        initial_devices = kwargs.get('initial_devices', None)
         for i, block in enumerate(list_obj):
-            device = getattr(block, 'device', 'cpu')
+            if hasattr(block, 'device'):
+                device = getattr(block, 'device')
+            elif initial_devices and id(block) in initial_devices:
+                device = initial_devices[id(block)]
+            else:
+                raise Exception("Unknown device for block %d" % i)
             if self._concat_dim is not None:
                 self._device_to_indices[
                     repr(device)].append(
                     slice(self._bounds[i-1] % self._bounds[-1], self._bounds[i]))
             self._device_types.add(type(device))  # TODO remove string
```

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/device/__init__.py` & `CrossPy-0.0.0a3.dev9/crosspy/device/__init__.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/device/cpu/__init__.py` & `CrossPy-0.0.0a3.dev9/crosspy/device/cpu/__init__.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/device/cpu/component.py` & `CrossPy-0.0.0a3.dev9/crosspy/device/cpu/component.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/device/cpu/generic.py` & `CrossPy-0.0.0a3.dev9/crosspy/device/cpu/generic.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/device/detail.py` & `CrossPy-0.0.0a3.dev9/crosspy/device/detail.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/device/device.py` & `CrossPy-0.0.0a3.dev9/crosspy/device/device.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/device/gpu/__init__.py` & `CrossPy-0.0.0a3.dev9/crosspy/device/gpu/__init__.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/device/gpu/component.py` & `CrossPy-0.0.0a3.dev9/crosspy/device/gpu/component.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/device/gpu/cuda.py` & `CrossPy-0.0.0a3.dev9/crosspy/device/gpu/cuda.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/ldevice.py` & `CrossPy-0.0.0a3.dev9/crosspy/ldevice.py`

 * *Files 0% similar despite different names*

```diff
@@ -204,15 +204,16 @@
             in which case the device and/or memory associated with the logical device is passed along with the index.
         :param memory_kind: The kind of memory in which to place the data.
         :return: A :class:`list` of objects returned by `data` and copied to the appropriate device.
         """
         def hacked_wrapper(x):  # ad hoc to preserve shape
             s = x.shape
             x = wrapper(x)
-            x.shape = s
+            if not hasattr(x, "shape"):
+                x.shape = s
             return x
         data = _wrapper_for_partition_function(data)
         return [
             hacked_wrapper(data(
                 i,
                 memory=self.memory(i, kind=memory_kind),
                 device=self.device(i)
```

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/placement.py` & `CrossPy-0.0.0a3.dev9/crosspy/placement.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/crosspy/utils.py` & `CrossPy-0.0.0a3.dev9/crosspy/utils.py`

 * *Files identical despite different names*

### Comparing `CrossPy-0.0.0a3.dev8/setup.py` & `CrossPy-0.0.0a3.dev9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
 # Step 2:
 # twine upload --repository testpypi dist/*
 # twine upload dist/*
 
 # Step 3:
 # pip install -U --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ crosspy
 
-VERSION = '0.0.0a3.dev8'
+VERSION = '0.0.0a3.dev9'
 
 # Always prefer setuptools over distutils
 from setuptools import setup, find_packages
 import pathlib
 
 here = pathlib.Path(__file__).parent.resolve()
```

