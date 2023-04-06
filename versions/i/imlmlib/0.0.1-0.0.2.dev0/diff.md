# Comparing `tmp/imlmlib-0.0.1.tar.gz` & `tmp/imlmlib-0.0.2.dev0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "imlmlib-0.0.1.tar", max compression
+gzip compressed data, was "imlmlib-0.0.2.dev0.tar", max compression
```

## Comparing `imlmlib-0.0.1.tar` & `imlmlib-0.0.2.dev0.tar`

### file list

```diff
@@ -1,9 +1,9 @@
--rw-r--r--   0        0        0     1071 2023-03-09 16:42:28.654825 imlmlib-0.0.1/LICENSE
--rw-r--r--   0        0        0     1329 2023-03-09 08:42:45.345552 imlmlib-0.0.1/imlmlib/ACTR_2005.py
--rw-r--r--   0        0        0        0 2023-03-09 08:44:38.530581 imlmlib-0.0.1/imlmlib/__init__.py
--rw-r--r--   0        0        0     4853 2023-03-09 13:44:59.936190 imlmlib-0.0.1/imlmlib/exponential_forgetting.py
--rw-r--r--   0        0        0     8571 2023-03-09 16:33:30.833834 imlmlib-0.0.1/imlmlib/mem_utils.py
--rw-r--r--   0        0        0     3145 2023-03-09 16:09:26.014485 imlmlib-0.0.1/imlmlib/mle_utils.py
--rw-r--r--   0        0        0      507 2023-03-09 09:15:11.018170 imlmlib-0.0.1/pyproject.toml
--rw-r--r--   0        0        0      682 2023-03-09 16:44:37.365158 imlmlib-0.0.1/setup.py
--rw-r--r--   0        0        0      560 2023-03-09 16:44:37.365343 imlmlib-0.0.1/PKG-INFO
+-rw-r--r--   0        0        0     1071 2023-03-09 16:42:28.654825 imlmlib-0.0.2.dev0/LICENSE
+-rw-r--r--   0        0        0     1329 2023-03-09 08:42:45.345552 imlmlib-0.0.2.dev0/imlmlib/ACTR_2005.py
+-rw-r--r--   0        0        0       28 2023-04-06 16:03:27.202899 imlmlib-0.0.2.dev0/imlmlib/__init__.py
+-rw-r--r--   0        0        0    12655 2023-04-06 14:17:58.826258 imlmlib-0.0.2.dev0/imlmlib/exponential_forgetting.py
+-rw-r--r--   0        0        0     8852 2023-04-06 14:07:43.550669 imlmlib-0.0.2.dev0/imlmlib/mem_utils.py
+-rw-r--r--   0        0        0     8573 2023-04-06 15:26:08.825945 imlmlib-0.0.2.dev0/imlmlib/mle_utils.py
+-rw-r--r--   0        0        0      551 2023-04-06 16:03:27.202899 imlmlib-0.0.2.dev0/pyproject.toml
+-rw-r--r--   0        0        0      741 2023-04-06 16:03:57.381568 imlmlib-0.0.2.dev0/setup.py
+-rw-r--r--   0        0        0      646 2023-04-06 16:03:57.381757 imlmlib-0.0.2.dev0/PKG-INFO
```

### Comparing `imlmlib-0.0.1/LICENSE` & `imlmlib-0.0.2.dev0/LICENSE`

 * *Files identical despite different names*

### Comparing `imlmlib-0.0.1/imlmlib/ACTR_2005.py` & `imlmlib-0.0.2.dev0/imlmlib/ACTR_2005.py`

 * *Files identical despite different names*

### Comparing `imlmlib-0.0.1/imlmlib/mem_utils.py` & `imlmlib-0.0.2.dev0/imlmlib/mem_utils.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,27 +1,36 @@
 import numpy
 from abc import ABC, abstractmethod
 
 
 class MemoryModel:
     def __init__(self, nitems, *args, seed=None, **kwargs):
         self.nitems = nitems
+        self._original_seed = seed
         self.rng = numpy.random.default_rng(seed=seed)
 
     @abstractmethod
     def update(self, item, time):
         raise NotImplementedError
 
     @abstractmethod
     def compute_probabilities(self, time=None):
         raise NotImplementedError
 
-    @abstractmethod
+    @property
+    def seed(self):
+        if getattr(self, "_seed", None) is None:
+            return self._original_seed
+        else:
+            return self._seed
+
     def reset(self):
-        raise NotImplementedError
+        if isinstance(self.seed, numpy.random.SeedSequence):
+            self._seed = self._original_seed.spawn(1)[0]
+        return
 
     def query_item(self, item, time):
         prob = self.compute_probabilities(time=time)[item]
         return (self.rng.random() < prob, prob)
 
 
 def trial(memory_model, schedule, reset=True):
```

### Comparing `imlmlib-0.0.1/setup.py` & `imlmlib-0.0.2.dev0/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -4,19 +4,22 @@
 packages = \
 ['imlmlib']
 
 package_data = \
 {'': ['*']}
 
 install_requires = \
-['numpy>=1.24.2,<2.0.0', 'scipy>=1.10.1,<2.0.0']
+['matplotlib>=3.7.1,<4.0.0',
+ 'numpy>=1.24.2,<2.0.0',
+ 'scipy>=1.10.1,<2.0.0',
+ 'tqdm>=4.65.0,<5.0.0']
 
 setup_kwargs = {
     'name': 'imlmlib',
-    'version': '0.0.1',
+    'version': '0.0.2.dev0',
     'description': 'Utilities for parametric modeling of interaction modalities that leverage memory',
     'long_description': None,
     'author': 'jgori',
     'author_email': 'juliengori@gmail.com',
     'maintainer': None,
     'maintainer_email': None,
     'url': None,
```

