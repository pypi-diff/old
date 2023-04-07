# Comparing `tmp/dictkit-0.1.3.tar.gz` & `tmp/dictkit-0.1.4.tar.gz`

## Comparing `dictkit-0.1.3.tar` & `dictkit-0.1.4.tar`

### file list

```diff
@@ -1,9 +1,8 @@
--rw-r--r--   0        0        0       68 2020-02-02 00:00:00.000000 dictkit-0.1.3/dictkit/__init__.py
--rw-r--r--   0        0        0    47877 2020-02-02 00:00:00.000000 dictkit-0.1.3/dictkit/_type_info.py
--rw-r--r--   0        0        0    11072 2020-02-02 00:00:00.000000 dictkit-0.1.3/dictkit/categorize.py
--rw-r--r--   0        0        0     6235 2020-02-02 00:00:00.000000 dictkit-0.1.3/dictkit/render.py
--rw-r--r--   0        0        0    11488 2020-02-02 00:00:00.000000 dictkit-0.1.3/dictkit/utildict.py
--rw-r--r--   0        0        0     2024 2020-02-02 00:00:00.000000 dictkit-0.1.3/.gitignore
--rw-r--r--   0        0        0     3122 2020-02-02 00:00:00.000000 dictkit-0.1.3/README.md
--rw-r--r--   0        0        0     1365 2020-02-02 00:00:00.000000 dictkit-0.1.3/pyproject.toml
--rw-r--r--   0        0        0     3618 2020-02-02 00:00:00.000000 dictkit-0.1.3/PKG-INFO
+-rw-r--r--   0        0        0       68 2020-02-02 00:00:00.000000 dictkit-0.1.4/dictkit/__init__.py
+-rw-r--r--   0        0        0    11072 2020-02-02 00:00:00.000000 dictkit-0.1.4/dictkit/categorize.py
+-rw-r--r--   0        0        0     6235 2020-02-02 00:00:00.000000 dictkit-0.1.4/dictkit/render.py
+-rw-r--r--   0        0        0    10424 2020-02-02 00:00:00.000000 dictkit-0.1.4/dictkit/utildict.py
+-rw-r--r--   0        0        0     2024 2020-02-02 00:00:00.000000 dictkit-0.1.4/.gitignore
+-rw-r--r--   0        0        0     3122 2020-02-02 00:00:00.000000 dictkit-0.1.4/README.md
+-rw-r--r--   0        0        0     1365 2020-02-02 00:00:00.000000 dictkit-0.1.4/pyproject.toml
+-rw-r--r--   0        0        0     3618 2020-02-02 00:00:00.000000 dictkit-0.1.4/PKG-INFO
```

### Comparing `dictkit-0.1.3/dictkit/categorize.py` & `dictkit-0.1.4/dictkit/categorize.py`

 * *Files identical despite different names*

### Comparing `dictkit-0.1.3/dictkit/render.py` & `dictkit-0.1.4/dictkit/render.py`

 * *Files identical despite different names*

### Comparing `dictkit-0.1.3/dictkit/utildict.py` & `dictkit-0.1.4/dictkit/utildict.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,28 +1,12 @@
 from __future__ import annotations
-import sys
 from collections import ChainMap
-from typing import overload, Iterable, Mapping, TypeVar
+from typing import overload, Iterable, Mapping, TypeVar, Literal
 from copy import copy
 
-if "pandas" in sys.modules:
-    # If pandas is already imported, we can speed up our code by never checking anymore
-    import pandas
-
-    def get_pandas():  # type:ignore
-        return pandas
-
-else:
-
-    def get_pandas():
-        if "pandas" in sys.modules:
-            import pandas
-
-            return pandas
-
 
 def is_valid_normal_iterable(item) -> bool:
     """
     Returns True if the average human would say, "Yes, that looks like a
     regular iterable to me"
     """
     if not isinstance(item, Iterable):
@@ -61,18 +45,16 @@
     Add items, while returning a modified copy of self
       - `my_dict.add(a=5)` -> {<existing key/values>, 'a': 5}
 
     Drop items, while returning a modified copy of self
       - `my_dict.drop('a', 'b')` -> {<key/values excluding 'a' and 'b'>}
 
     Accepts a variety of argument types at creation
-      - Accepts other dictionaries, 2-column dataframes, or iterables (lists or tuples) of
+      - Accepts other dictionaries, iterables (lists or tuples) of
         length 2, to make key-value pairs from.
-      - 2-column dataframes will be converted to key/value pairs using the first
-        column as values
       - 2-element iterables will be converted to dictionaries with one key/value pair
         before being combined with other arguments
 
     Examples
     --------
 
     GPT-4 came up with and wrote all of these, given nothing other than the source code
@@ -137,31 +119,14 @@
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
     }
 
-    Add items from a 2-column dataframe
-    >>> import pandas as pd
-    >>> sd = UtilDict(a=1, b=2)
-    >>> df = pd.DataFrame({"key": ["c", "d"], "value": [3, 4]})
-    >>> df
-      key  value
-    0   c      3
-    1   d      4
-    >>> sd2 = sd.add(df)
-    >>> sd2
-    {
-       'a': 1,
-       'b': 2,
-       'c': 3,
-       'd': 4
-    }
-
     Drop multiple items at once
     >>> sd = UtilDict(a=1, b=2, c=3, d=4)
     >>> sd2 = sd.drop("a", "c")
     >>> sd2
     {
        'b': 2,
        'd': 4
@@ -272,58 +237,75 @@
 
         for k in keys:
             new.pop(k)
 
         if not inplace:
             return new
 
+    @overload
+    def deep_uniform(self, reverse: Literal[False]) -> UtilDict[K, V]:
+        ...
+
+    @overload
+    def deep_uniform(self, reverse: Literal[True]) -> dict:
+        ...
+
+    def deep_uniform(self, reverse=False):
+        """
+        Recursively convert all child instances of `dict` to
+        Self's type.
+
+        If `reverse=True`, then the opposite happens. Converts all nested UtilDict
+        to `dict`, and returns a `dict`
+        """
+
+        def uniform(value):
+            if isinstance(value, (UtilDict, dict)):
+                value = {k: uniform(v) for k, v in value.items()}
+                if not reverse:
+                    value = UtilDict(value)
+            elif isinstance(value, (list, tuple)):
+                value = type(value)(uniform(x) for x in value)
+            return value
+
+        new = self.copy()
+        for key, value in new.items():
+            new[key] = uniform(value)
+
+        if reverse:
+            return dict(**new)
+        return new
+
     def __getattr__(self, k):
         return self.__getitem__(k)
 
     def __setitem__(self, key, val):
         special_key_types = (list, type(...))
         if not isinstance(key, special_key_types):
             return super().__setitem__(key, val)
 
         if isinstance(key, type(...)):
-            if (pd := get_pandas()) and isinstance(val, pd.DataFrame):
-                for c in val:
-                    super().__setitem__(c, val[c])
-            elif (pd := get_pandas()) and isinstance(val, pd.Series):
-                for k, v in val.to_dict():
-                    super().__setitem__(k, v)
-            elif isinstance(val, dict):
+            if isinstance(val, dict):
                 for k, v in val.items():
                     super().__setitem__(k, v)
-            else:
-                raise ValueError(val)
-            return
+                return
+            raise ValueError(val)
 
         assert isinstance(key, list), type(key)
 
-        if isinstance(val, tuple) or (
-            (pd := get_pandas()) and isinstance(val, pd.Series)
-        ):
+        if isinstance(val, tuple):
             if len(val) == len(key):
                 for k, v in zip(key, val):
                     super().__setitem__(k, v)
             else:
                 raise ValueError(
                     "Number of values assigned must equal number of keys assigning to"
                 )
             return
 
-        if (pd := get_pandas()) and isinstance(val, pd.DataFrame):
-            if len(val.columns) == len(key):
-                for i, k in enumerate(key):
-                    super().__setitem__(k, val[val.columns[i]])
-            else:
-                raise ValueError("pd.DataFrame must have same number of columns as key")
-            return
-
         for k in key:
             super().__setitem__(k, copy(val))
 
     @overload
     def __getitem__(self, key: K) -> V:
         ...
 
@@ -347,27 +329,14 @@
         return new
 
     def __copy__(self) -> UtilDict:
         return self.copy()
 
     def _iterable_to_dict(self, arg) -> dict:
 
-        if pd := get_pandas():
-            if isinstance(arg, pd.DataFrame):
-                if len(arg.columns) == 2:
-                    return dict(zip(arg[arg.columns[0]], arg[arg.columns[1]]))
-                if len(arg.columns) == 1:
-                    return arg[arg.columns[0]].to_dict()
-                raise ValueError(
-                    "pd.DataFrame must have one or two columns, to make key/val pairs from"
-                )
-
-            if isinstance(arg, pd.Series):
-                return arg.to_dict()
-
         if isinstance(arg, Mapping):
             return dict(arg)
 
         if not isinstance(arg, Iterable):
             # Let dict throw the error if not hashable
             return {arg: self.get(arg)}
 
@@ -417,8 +386,9 @@
 
     def __repr__(self):
         return self.render()
 
 
 if __name__ == "__main__":
     from doctest import testmod
+
     testmod()
```

### Comparing `dictkit-0.1.3/.gitignore` & `dictkit-0.1.4/.gitignore`

 * *Files identical despite different names*

### Comparing `dictkit-0.1.3/README.md` & `dictkit-0.1.4/README.md`

 * *Files identical despite different names*

### Comparing `dictkit-0.1.3/pyproject.toml` & `dictkit-0.1.4/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "dictkit"
-version = "0.1.3"
+version = "0.1.4"
 python_requires = ">=3.10"
 description = "Utility data structures with simple but powerful features."
 authors = [
     {name = "Ryan Young", email = "dev@ryayoung.com"}
 ]
 readme = "README.md"
 license = "MIT"
```

### Comparing `dictkit-0.1.3/PKG-INFO` & `dictkit-0.1.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dictkit
-Version: 0.1.3
+Version: 0.1.4
 Summary: Utility data structures with simple but powerful features.
 Author-email: Ryan Young <dev@ryayoung.com>
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3.11
```

