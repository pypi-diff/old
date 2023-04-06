# Comparing `tmp/jaraco.collections-4.0.0.tar.gz` & `tmp/jaraco.collections-4.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "jaraco.collections-4.0.0.tar", last modified: Tue Mar 28 15:16:19 2023, max compression
+gzip compressed data, was "jaraco.collections-4.1.0.tar", last modified: Thu Apr  6 10:18:56 2023, max compression
```

## Comparing `jaraco.collections-4.0.0.tar` & `jaraco.collections-4.1.0.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 15:16:19.674648 jaraco.collections-4.0.0/
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/.coveragerc
--rw-r--r--   0 runner    (1001) docker     (123)      246 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/.editorconfig
--rw-r--r--   0 runner    (1001) docker     (123)      136 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/.flake8
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 15:16:19.674648 jaraco.collections-4.0.0/.github/
--rw-r--r--   0 runner    (1001) docker     (123)       34 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/.github/FUNDING.yml
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/.github/dependabot.yml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 15:16:19.674648 jaraco.collections-4.0.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     3294 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/.github/workflows/main.yml
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/.readthedocs.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     2921 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-03-28 15:16:19.674648 jaraco.collections-4.0.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2763 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 15:16:19.674648 jaraco.collections-4.0.0/docs/
--rw-r--r--   0 runner    (1001) docker     (123)     1429 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/docs/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)       81 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/docs/history.rst
--rw-r--r--   0 runner    (1001) docker     (123)      332 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/docs/index.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 15:16:19.674648 jaraco.collections-4.0.0/jaraco/
--rw-r--r--   0 runner    (1001) docker     (123)    25619 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/jaraco/collections.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 15:16:19.674648 jaraco.collections-4.0.0/jaraco.collections.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-03-28 15:16:19.000000 jaraco.collections-4.0.0/jaraco.collections.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      531 2023-03-28 15:16:19.000000 jaraco.collections-4.0.0/jaraco.collections.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-28 15:16:19.000000 jaraco.collections-4.0.0/jaraco.collections.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      329 2023-03-28 15:16:19.000000 jaraco.collections-4.0.0/jaraco.collections.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-03-28 15:16:19.000000 jaraco.collections-4.0.0/jaraco.collections.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      154 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/mypy.ini
--rw-r--r--   0 runner    (1001) docker     (123)      378 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1238 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/pytest.ini
--rw-r--r--   0 runner    (1001) docker     (123)     1110 2023-03-28 15:16:19.674648 jaraco.collections-4.0.0/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 15:16:19.674648 jaraco.collections-4.0.0/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      672 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/tests/test_collections.py
--rw-r--r--   0 runner    (1001) docker     (123)      795 2023-03-28 15:15:53.000000 jaraco.collections-4.0.0/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:18:56.609048 jaraco.collections-4.1.0/
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/.coveragerc
+-rw-r--r--   0 runner    (1001) docker     (123)      246 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/.editorconfig
+-rw-r--r--   0 runner    (1001) docker     (123)      136 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/.flake8
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:18:56.609048 jaraco.collections-4.1.0/.github/
+-rw-r--r--   0 runner    (1001) docker     (123)       34 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/.github/FUNDING.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/.github/dependabot.yml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:18:56.609048 jaraco.collections-4.1.0/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     3294 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/.github/workflows/main.yml
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/.readthedocs.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     3151 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1050 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-04-06 10:18:56.609048 jaraco.collections-4.1.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2763 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:18:56.609048 jaraco.collections-4.1.0/docs/
+-rw-r--r--   0 runner    (1001) docker     (123)     1501 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/docs/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)       81 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/docs/history.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      332 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/docs/index.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:18:56.609048 jaraco.collections-4.1.0/jaraco/
+-rw-r--r--   0 runner    (1001) docker     (123)    26507 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/jaraco/collections.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:18:56.609048 jaraco.collections-4.1.0/jaraco.collections.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3348 2023-04-06 10:18:56.000000 jaraco.collections-4.1.0/jaraco.collections.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      531 2023-04-06 10:18:56.000000 jaraco.collections-4.1.0/jaraco.collections.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:18:56.000000 jaraco.collections-4.1.0/jaraco.collections.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      329 2023-04-06 10:18:56.000000 jaraco.collections-4.1.0/jaraco.collections.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-06 10:18:56.000000 jaraco.collections-4.1.0/jaraco.collections.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      154 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/mypy.ini
+-rw-r--r--   0 runner    (1001) docker     (123)      378 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1272 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/pytest.ini
+-rw-r--r--   0 runner    (1001) docker     (123)     1110 2023-04-06 10:18:56.609048 jaraco.collections-4.1.0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:18:56.609048 jaraco.collections-4.1.0/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      672 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/tests/test_collections.py
+-rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-06 10:18:34.000000 jaraco.collections-4.1.0/tox.ini
```

### Comparing `jaraco.collections-4.0.0/.github/workflows/main.yml` & `jaraco.collections-4.1.0/.github/workflows/main.yml`

 * *Files identical despite different names*

### Comparing `jaraco.collections-4.0.0/CHANGES.rst` & `jaraco.collections-4.1.0/CHANGES.rst`

 * *Files 6% similar despite different names*

```diff
@@ -1,7 +1,18 @@
+v4.1.0
+======
+
+``Projection`` now accepts an iterable or callable or pattern
+for matching keys.
+
+``Projection`` now retains order of keys from the underlying
+mapping.
+
+``DictFilter`` is now deprecated in favor of ``Projection``.
+
 v4.0.0
 ======
 
 ``DictFilter`` no longer accepts ``include_keys`` and requires
 ``include_pattern`` as a keyword argument.
 
 v3.11.0
```

### Comparing `jaraco.collections-4.0.0/LICENSE` & `jaraco.collections-4.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `jaraco.collections-4.0.0/PKG-INFO` & `jaraco.collections-4.1.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jaraco.collections
-Version: 4.0.0
+Version: 4.1.0
 Summary: Collection objects similar to those in stdlib by jaraco
 Home-page: https://github.com/jaraco/jaraco.collections
 Author: Jason R. Coombs
 Author-email: jaraco@jaraco.com
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `jaraco.collections-4.0.0/README.rst` & `jaraco.collections-4.1.0/README.rst`

 * *Files identical despite different names*

### Comparing `jaraco.collections-4.0.0/docs/conf.py` & `jaraco.collections-4.1.0/docs/conf.py`

 * *Files 13% similar despite different names*

```diff
@@ -26,26 +26,31 @@
             ),
         ],
     )
 }
 
 # Be strict about any broken references
 nitpicky = True
-
-nitpick_ignore = [
-    # jaraco/jaraco.collections#11
-    ('py:class', 'v, remove specified key and return the corresponding value.'),
-    ('py:class', 'None.  Update D from dict/iterable E and F.'),
-    ('py:class', 'D[k] if k in D, else d.  d defaults to None.'),
-]
+nitpick_ignore = []
 
 # Include Python intersphinx mapping to prevent failures
 # jaraco/skeleton#51
 extensions += ['sphinx.ext.intersphinx']
 intersphinx_mapping = {
     'python': ('https://docs.python.org/3', None),
 }
 
 # Preserve authored syntax for defaults
 autodoc_preserve_defaults = True
 
 extensions += ['jaraco.tidelift']
+
+# jaraco/jaraco.collections#11
+nitpick_ignore += [
+    ('py:class', 'v, remove specified key and return the corresponding value.'),
+    ('py:class', 'None.  Update D from dict/iterable E and F.'),
+    ('py:class', 'D[k] if k in D, else d.  d defaults to None.'),
+]
+
+nitpick_ignore += [
+    ('py:class', 're.Pattern'),
+]
```

### Comparing `jaraco.collections-4.0.0/jaraco/collections.py` & `jaraco.collections-4.1.0/jaraco/collections.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,77 +1,106 @@
 import re
 import operator
 import collections.abc
 import itertools
 import copy
 import functools
 import random
-from collections.abc import Mapping, Iterable
+import warnings
+from collections.abc import Container, Iterable, Mapping
+from typing import Callable, Union
 
 import jaraco.text
 
 
+_Matchable = Union[Callable, Container, Iterable, re.Pattern]
+
+
+def _dispatch(obj: _Matchable) -> Callable:
+    # can't rely on singledispatch for Union[Container, Iterable]
+    # due to ambiguity
+    # (https://peps.python.org/pep-0443/#abstract-base-classes).
+    if isinstance(obj, re.Pattern):
+        return obj.fullmatch
+    if not isinstance(obj, Callable):  # type: ignore
+        if not isinstance(obj, Container):
+            obj = set(obj)  # type: ignore
+        obj = obj.__contains__
+    return obj  # type: ignore
+
+
 class Projection(collections.abc.Mapping):
     """
     Project a set of keys over a mapping
 
     >>> sample = {'a': 1, 'b': 2, 'c': 3}
     >>> prj = Projection(['a', 'c', 'd'], sample)
-    >>> prj == {'a': 1, 'c': 3}
+    >>> dict(prj)
+    {'a': 1, 'c': 3}
+
+    Projection also accepts an iterable or callable or pattern.
+
+    >>> iter_prj = Projection(iter('acd'), sample)
+    >>> call_prj = Projection(lambda k: ord(k) in (97, 99, 100), sample)
+    >>> pat_prj = Projection(re.compile(r'[acd]'), sample)
+    >>> prj == iter_prj == call_prj == pat_prj
     True
 
     Keys should only appear if they were specified and exist in the space.
+    Order is retained.
 
-    >>> sorted(list(prj.keys()))
+    >>> list(prj)
     ['a', 'c']
 
     Attempting to access a key not in the projection
     results in a KeyError.
 
     >>> prj['b']
     Traceback (most recent call last):
     ...
     KeyError: 'b'
 
     Use the projection to update another dict.
 
     >>> target = {'a': 2, 'b': 2}
     >>> target.update(prj)
-    >>> target == {'a': 1, 'b': 2, 'c': 3}
-    True
+    >>> target
+    {'a': 1, 'b': 2, 'c': 3}
 
-    Also note that Projection keeps a reference to the original dict, so
-    if you modify the original dict, that could modify the Projection.
+    Projection keeps a reference to the original dict, so
+    modifying the original dict may modify the Projection.
 
     >>> del sample['a']
     >>> dict(prj)
     {'c': 3}
     """
 
-    def __init__(self, keys: Iterable, space: Mapping):
-        self._keys = set(keys)
+    def __init__(self, keys: _Matchable, space: Mapping):
+        self._match = _dispatch(keys)
         self._space = space
 
     def __getitem__(self, key):
-        if key not in self._keys:
+        if not self._match(key):
             raise KeyError(key)
         return self._space[key]
 
     def _keys_resolved(self):
-        return self._keys.intersection(self._space)
+        return filter(self._match, self._space)
 
     def __iter__(self):
-        return iter(self._keys_resolved())
+        return self._keys_resolved()
 
     def __len__(self):
-        return len(self._keys_resolved())
+        return len(tuple(self._keys_resolved()))
 
 
 class DictFilter(Projection):
     """
+    *Deprecated*
+
     Takes a dict and simulates a sub-dict based on a pattern.
 
     >>> sample = dict(a=1, b=2, c=3, d=4, ef=5)
 
     Filter for only single-character keys:
 
     >>> filtered = DictFilter(sample, include_pattern='.$')
@@ -85,32 +114,32 @@
 
     >>> 'e' in filtered
     False
 
     Pattern is useful for excluding keys with a prefix.
 
     >>> filtered = DictFilter(sample, include_pattern=r'(?![ace])')
-    >>> dict(filtered) == dict(b=2, d=4)
+    >>> filtered == dict(b=2, d=4)
     True
 
-    Also note that DictFilter keeps a reference to the original dict, so
-    if you modify the original dict, that could modify the filtered dict.
+    DictFilter keeps a reference to the original dict, so
+    modifying the original dict may modify the filtered dict.
 
     >>> del sample['d']
     >>> dict(filtered)
     {'b': 2}
     """
 
     def __init__(self, dict, *, include_pattern):
-        self._space = dict
-        self._include_pattern = re.compile(include_pattern)
-
-    @property
-    def _keys(self):
-        return set(filter(self._include_pattern.match, self._space))
+        warnings.warn(
+            "DictFilter is deprecated. Pass re.Pattern to Projection instead.",
+            DeprecationWarning,
+            stacklevel=2,
+        )
+        super().__init__(re.compile(include_pattern).match, dict)
 
 
 def dict_map(function, dictionary):
     """
     dict_map is much like the built-in function map.  It takes a dictionary
     and applys a function to the values of that dictionary, returning a
     new dictionary with the mapped values in the original keys.
@@ -129,27 +158,27 @@
     key_match_comparator, which defaults to less-than-or-equal.
     A value is returned for a key if it is the first key that matches in
     the sorted list of keys.
 
     One may supply keyword parameters to be passed to the sort function used
     to sort keys (i.e. key, reverse) as sort_params.
 
-    Let's create a map that maps 1-3 -> 'a', 4-6 -> 'b'
+    Create a map that maps 1-3 -> 'a', 4-6 -> 'b'
 
     >>> r = RangeMap({3: 'a', 6: 'b'})  # boy, that was easy
     >>> r[1], r[2], r[3], r[4], r[5], r[6]
     ('a', 'a', 'a', 'b', 'b', 'b')
 
     Even float values should work so long as the comparison operator
     supports it.
 
     >>> r[4.5]
     'b'
 
-    But you'll notice that the way rangemap is defined, it must be open-ended
+    Notice that the way rangemap is defined, it must be open-ended
     on one side.
 
     >>> r[0]
     'a'
     >>> r[-1]
     'a'
 
@@ -259,15 +288,15 @@
 
 def __identity(x):
     return x
 
 
 def sorted_items(d, key=__identity, reverse=False):
     """
-    Return the items of the dictionary sorted by the keys
+    Return the items of the dictionary sorted by the keys.
 
     >>> sample = dict(foo=20, bar=42, baz=10)
     >>> tuple(sorted_items(sample))
     (('bar', 42), ('baz', 10), ('foo', 20))
 
     >>> reverse_string = lambda s: ''.join(reversed(s))
     >>> tuple(sorted_items(sample, key=reverse_string))
```

### Comparing `jaraco.collections-4.0.0/jaraco.collections.egg-info/PKG-INFO` & `jaraco.collections-4.1.0/jaraco.collections.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jaraco.collections
-Version: 4.0.0
+Version: 4.1.0
 Summary: Collection objects similar to those in stdlib by jaraco
 Home-page: https://github.com/jaraco/jaraco.collections
 Author: Jason R. Coombs
 Author-email: jaraco@jaraco.com
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `jaraco.collections-4.0.0/jaraco.collections.egg-info/SOURCES.txt` & `jaraco.collections-4.1.0/jaraco.collections.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `jaraco.collections-4.0.0/pytest.ini` & `jaraco.collections-4.1.0/pytest.ini`

 * *Files 4% similar despite different names*

```diff
@@ -26,7 +26,9 @@
 	# realpython/pytest-mypy#152
 	ignore:'encoding' argument not specified::pytest_mypy
 
 	# python/cpython#100750
 	ignore:'encoding' argument not specified::platform
 
 	## end upstream
+
+	ignore:DictFilter is deprecated
```

### Comparing `jaraco.collections-4.0.0/setup.cfg` & `jaraco.collections-4.1.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `jaraco.collections-4.0.0/tests/test_collections.py` & `jaraco.collections-4.1.0/tests/test_collections.py`

 * *Files identical despite different names*

### Comparing `jaraco.collections-4.0.0/tox.ini` & `jaraco.collections-4.1.0/tox.ini`

 * *Files identical despite different names*

