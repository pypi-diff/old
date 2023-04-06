# Comparing `tmp/vermils-0.3.0.tar.gz` & `tmp/vermils-0.3.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vermils-0.3.0.tar", max compression
+gzip compressed data, was "vermils-0.3.1.tar", max compression
```

## Comparing `vermils-0.3.0.tar` & `vermils-0.3.1.tar`

### file list

```diff
@@ -1,38 +1,38 @@
--rw-r--r--   0        0        0     1061 2022-11-17 09:33:04.310180 vermils-0.3.0/LICENSE
--rw-r--r--   0        0        0     3942 2023-03-28 18:00:26.740248 vermils-0.3.0/README.md
--rw-r--r--   0        0        0     3430 2023-04-03 12:46:28.661116 vermils-0.3.0/pyproject.toml
--rw-r--r--   0        0        0       61 2023-03-11 12:26:03.346413 vermils-0.3.0/vermils/__init__.py
--rw-r--r--   0        0        0      167 2022-11-17 05:01:38.613644 vermils-0.3.0/vermils/asynctools/__init__.py
--rw-r--r--   0        0        0    11331 2023-03-28 18:00:26.751286 vermils-0.3.0/vermils/asynctools/asinkrunner.py
--rw-r--r--   0        0        0     9114 2023-03-28 18:00:26.753550 vermils-0.3.0/vermils/asynctools/tools.py
--rw-r--r--   0        0        0      184 2023-03-23 12:05:30.190436 vermils-0.3.0/vermils/collections/__init__.py
--rw-r--r--   0        0        0     5650 2023-03-28 18:00:26.755471 vermils-0.3.0/vermils/collections/fridge.py
--rw-r--r--   0        0        0     5014 2022-11-19 15:13:29.013831 vermils-0.3.0/vermils/collections/objdict.py
--rw-r--r--   0        0        0     4731 2022-11-17 11:15:42.360179 vermils-0.3.0/vermils/collections/strchain.py
--rw-r--r--   0        0        0      191 2022-11-19 15:12:56.882494 vermils-0.3.0/vermils/gadgets/__init__.py
--rw-r--r--   0        0        0     7897 2023-03-29 11:10:08.667455 vermils-0.3.0/vermils/gadgets/misc.py
--rw-r--r--   0        0        0     5349 2023-04-02 19:22:57.308872 vermils-0.3.0/vermils/gadgets/monologger.py
--rw-r--r--   0        0        0     3332 2023-03-21 11:28:23.498195 vermils-0.3.0/vermils/gadgets/sidelogging/__init__.py
--rw-r--r--   0        0        0      165 2023-03-11 12:29:46.925809 vermils-0.3.0/vermils/io/__init__.py
--rw-r--r--   0        0        0      187 2022-11-19 15:12:39.619881 vermils-0.3.0/vermils/io/aio/__init__.py
--rw-r--r--   0        0        0       36 2023-03-21 13:57:43.165843 vermils-0.3.0/vermils/io/aio/atomic.py
--rw-r--r--   0        0        0      526 2022-11-19 13:16:07.310489 vermils-0.3.0/vermils/io/aio/os.py
--rw-r--r--   0        0        0      530 2022-11-19 15:12:33.188077 vermils-0.3.0/vermils/io/aio/path.py
--rw-r--r--   0        0        0      564 2022-11-19 15:12:29.231677 vermils-0.3.0/vermils/io/aio/tempfile.py
--rw-r--r--   0        0        0     4193 2023-03-11 02:37:01.818269 vermils-0.3.0/vermils/io/aio/wrappers.py
--rw-r--r--   0        0        0       79 2023-03-21 13:56:42.877399 vermils-0.3.0/vermils/io/atomic.py
--rw-r--r--   0        0        0      753 2022-11-19 07:36:35.873791 vermils-0.3.0/vermils/io/misc.py
--rw-r--r--   0        0        0      120 2022-11-19 15:12:01.815868 vermils-0.3.0/vermils/io/puller/__init__.py
--rw-r--r--   0        0        0     7389 2022-11-21 11:26:58.242720 vermils-0.3.0/vermils/io/puller/modifier.py
--rw-r--r--   0        0        0    16614 2023-03-28 18:00:26.760453 vermils-0.3.0/vermils/io/puller/pullers.py
--rw-r--r--   0        0        0        0 2022-11-17 07:00:14.505466 vermils-0.3.0/vermils/py.typed
--rw-r--r--   0        0        0      187 2023-04-03 12:45:21.373300 vermils-0.3.0/vermils/react/__init__.py
--rw-r--r--   0        0        0     8051 2023-03-28 18:00:26.765410 vermils-0.3.0/vermils/react/actionchain.py
--rw-r--r--   0        0        0     3426 2023-03-28 18:00:26.767251 vermils-0.3.0/vermils/react/eventhook.py
--rw-r--r--   0        0        0      176 2022-11-17 11:06:38.303463 vermils-0.3.0/vermils/tensorflow/__init__.py
--rw-r--r--   0        0        0        0 2022-11-17 11:05:46.699753 vermils-0.3.0/vermils/tensorflow/callbacks/__init__.py
--rw-r--r--   0        0        0        0 2022-11-17 11:04:02.664554 vermils-0.3.0/vermils/tensorflow/inspect/__init__.py
--rw-r--r--   0        0        0        0 2022-11-17 11:04:08.451719 vermils-0.3.0/vermils/tensorflow/layers/__init__.py
--rw-r--r--   0        0        0        0 2022-11-17 11:06:00.011160 vermils-0.3.0/vermils/tensorflow/metrics/__init__.py
--rw-r--r--   0        0        0        0 2022-11-17 11:04:11.042462 vermils-0.3.0/vermils/tensorflow/models/__init__.py
--rw-r--r--   0        0        0     5287 1970-01-01 00:00:00.000000 vermils-0.3.0/PKG-INFO
+-rw-r--r--   0        0        0     1061 2022-11-17 09:33:04.310180 vermils-0.3.1/LICENSE
+-rw-r--r--   0        0        0     3942 2023-03-28 18:00:26.740248 vermils-0.3.1/README.md
+-rw-r--r--   0        0        0     3430 2023-04-06 09:01:27.443182 vermils-0.3.1/pyproject.toml
+-rw-r--r--   0        0        0       61 2023-03-11 12:26:03.346413 vermils-0.3.1/vermils/__init__.py
+-rw-r--r--   0        0        0      167 2022-11-17 05:01:38.613644 vermils-0.3.1/vermils/asynctools/__init__.py
+-rw-r--r--   0        0        0    11331 2023-03-28 18:00:26.751286 vermils-0.3.1/vermils/asynctools/asinkrunner.py
+-rw-r--r--   0        0        0     9096 2023-04-04 17:51:41.191498 vermils-0.3.1/vermils/asynctools/tools.py
+-rw-r--r--   0        0        0      184 2023-03-23 12:05:30.190436 vermils-0.3.1/vermils/collections/__init__.py
+-rw-r--r--   0        0        0     5650 2023-03-28 18:00:26.755471 vermils-0.3.1/vermils/collections/fridge.py
+-rw-r--r--   0        0        0     5014 2022-11-19 15:13:29.013831 vermils-0.3.1/vermils/collections/objdict.py
+-rw-r--r--   0        0        0     4731 2022-11-17 11:15:42.360179 vermils-0.3.1/vermils/collections/strchain.py
+-rw-r--r--   0        0        0      191 2022-11-19 15:12:56.882494 vermils-0.3.1/vermils/gadgets/__init__.py
+-rw-r--r--   0        0        0     8896 2023-04-06 08:51:45.886283 vermils-0.3.1/vermils/gadgets/misc.py
+-rw-r--r--   0        0        0     5349 2023-04-02 19:22:57.308872 vermils-0.3.1/vermils/gadgets/monologger.py
+-rw-r--r--   0        0        0     3332 2023-04-05 18:00:35.578896 vermils-0.3.1/vermils/gadgets/sidelogging/__init__.py
+-rw-r--r--   0        0        0      165 2023-03-11 12:29:46.925809 vermils-0.3.1/vermils/io/__init__.py
+-rw-r--r--   0        0        0      187 2022-11-19 15:12:39.619881 vermils-0.3.1/vermils/io/aio/__init__.py
+-rw-r--r--   0        0        0       36 2023-03-21 13:57:43.165843 vermils-0.3.1/vermils/io/aio/atomic.py
+-rw-r--r--   0        0        0      526 2022-11-19 13:16:07.310489 vermils-0.3.1/vermils/io/aio/os.py
+-rw-r--r--   0        0        0      530 2022-11-19 15:12:33.188077 vermils-0.3.1/vermils/io/aio/path.py
+-rw-r--r--   0        0        0      564 2022-11-19 15:12:29.231677 vermils-0.3.1/vermils/io/aio/tempfile.py
+-rw-r--r--   0        0        0     4193 2023-03-11 02:37:01.818269 vermils-0.3.1/vermils/io/aio/wrappers.py
+-rw-r--r--   0        0        0       79 2023-03-21 13:56:42.877399 vermils-0.3.1/vermils/io/atomic.py
+-rw-r--r--   0        0        0      753 2022-11-19 07:36:35.873791 vermils-0.3.1/vermils/io/misc.py
+-rw-r--r--   0        0        0      120 2022-11-19 15:12:01.815868 vermils-0.3.1/vermils/io/puller/__init__.py
+-rw-r--r--   0        0        0     7389 2022-11-21 11:26:58.242720 vermils-0.3.1/vermils/io/puller/modifier.py
+-rw-r--r--   0        0        0    16614 2023-03-28 18:00:26.760453 vermils-0.3.1/vermils/io/puller/pullers.py
+-rw-r--r--   0        0        0        0 2022-11-17 07:00:14.505466 vermils-0.3.1/vermils/py.typed
+-rw-r--r--   0        0        0      187 2023-04-03 12:45:21.373300 vermils-0.3.1/vermils/react/__init__.py
+-rw-r--r--   0        0        0     8051 2023-03-28 18:00:26.765410 vermils-0.3.1/vermils/react/actionchain.py
+-rw-r--r--   0        0        0     3426 2023-03-28 18:00:26.767251 vermils-0.3.1/vermils/react/eventhook.py
+-rw-r--r--   0        0        0      176 2022-11-17 11:06:38.303463 vermils-0.3.1/vermils/tensorflow/__init__.py
+-rw-r--r--   0        0        0        0 2022-11-17 11:05:46.699753 vermils-0.3.1/vermils/tensorflow/callbacks/__init__.py
+-rw-r--r--   0        0        0        0 2022-11-17 11:04:02.664554 vermils-0.3.1/vermils/tensorflow/inspect/__init__.py
+-rw-r--r--   0        0        0        0 2022-11-17 11:04:08.451719 vermils-0.3.1/vermils/tensorflow/layers/__init__.py
+-rw-r--r--   0        0        0        0 2022-11-17 11:06:00.011160 vermils-0.3.1/vermils/tensorflow/metrics/__init__.py
+-rw-r--r--   0        0        0        0 2022-11-17 11:04:11.042462 vermils-0.3.1/vermils/tensorflow/models/__init__.py
+-rw-r--r--   0        0        0     5287 1970-01-01 00:00:00.000000 vermils-0.3.1/PKG-INFO
```

### Comparing `vermils-0.3.0/LICENSE` & `vermils-0.3.1/LICENSE`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/README.md` & `vermils-0.3.1/README.md`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/pyproject.toml` & `vermils-0.3.1/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "vermils"
-version = "0.3.0"
+version = "0.3.1"
 description = ""
 authors = ["VermiIIi0n <dungeon.behind0t@icloud.com>"]
 readme = "README.md"
 packages = [{ include = "vermils" }]
 license = "MIT"
 homepage = "https://github.com/VermiIIi0n/VermilsMagicPocket"
```

### Comparing `vermils-0.3.0/vermils/asynctools/asinkrunner.py` & `vermils-0.3.1/vermils/asynctools/asinkrunner.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/asynctools/tools.py` & `vermils-0.3.1/vermils/asynctools/tools.py`

 * *Files 3% similar despite different names*

```diff
@@ -227,34 +227,33 @@
 
 async def select(awaitables: Sequence[Awaitable[T] | AsyncGenerator[T, Any]],
                  return_future=False):
     """
     similar to asyncio.as_completed but returns the results as they are done.
 
     If one of the tasks raised an exception, it will be raised by `select`
-     after other tasks are done.
+    if `return_future` is False, otherwise the future will be returned.
 
     * `awaitables` - the awaitables to wait for, can be `coroutine`, `future`,
      `AsyncGenerator`
     * `buffersize` - if > 0, the max number of results to buffer before yielding,
-     this can prevent the generator from eating up RAM if the results are slow
-      to be comsumed. Sometimes
+     this can prevent the generator from eating up RAM.
     * `return_future` - if True, the future will be returned instead of the
         result.
 
     Usage:
     ```
     async for result in select([func1(), func2(), func3()]):
         print(result)
     ```
     """
 
     async def _run(aw: Awaitable[T] | AsyncGenerator[T, Any]):
         if inspect.isasyncgen(aw):
-            task = asyncio.ensure_future(aw.asend(None))
+            task = asyncio.create_task(aw.asend(None))
         else:
             aw = cast(Awaitable[T], aw)
             task = asyncio.ensure_future(aw)
         await wait_until(task)
         return (aw, task)
 
     loop = asyncio.get_running_loop()
```

### Comparing `vermils-0.3.0/vermils/collections/fridge.py` & `vermils-0.3.1/vermils/collections/fridge.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/collections/objdict.py` & `vermils-0.3.1/vermils/collections/objdict.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/collections/strchain.py` & `vermils-0.3.1/vermils/collections/strchain.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/gadgets/misc.py` & `vermils-0.3.1/vermils/gadgets/misc.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,44 +1,45 @@
 """
 Utility functions.
 """
 
 from __future__ import annotations
 import http.cookiejar as hjar
 import sys
-import os
 import re
 import inspect
-import pathlib
 import importlib
 import contextlib
-from typing import Mapping, NoReturn, Sequence, TypeVar, Iterable, Callable, Any
+from pathlib import Path
+from typing import Mapping, NoReturn, Sequence, TypeVar, Iterable, Callable, Any, cast
 from typing import Literal, overload
 
 C = TypeVar("C", bound=Callable)
 
 __all__ = ("stringify_keys", "supports_in", "mimics", "sort_class",
            "str_to_object", "real_dir", "real_path", "version_cmp",
            "to_ordinal", "selenium_cookies_to_jar", "DummyLogger",
-           "load_module", "check")
+           "load_module", "check", "relative_to")
 
 
 def mimics(_: C) -> Callable[[Callable], C]:
     """
+    ### `mimics()`
     Type trick. This decorator is used to make a function mimic the signature
     of another function.
     """
     def decorator(wrapper: Callable) -> C:
         return wrapper  # type: ignore
 
     return decorator
 
 
 def supports_in(obj) -> bool:
     """
+    ### `supports_in()`
     Check if an object supports the ``in`` operator.
 
     Be careful: When a `Generator` be evaluated when using ``in``
     and the desired value never appears, the statement could never end.
     """
     return any(hasattr(obj, attr)
                for attr in ("__contains__", "__iter__", "__getitem__"))
@@ -56,15 +57,18 @@
         return memo[id(data)]
     if isinstance(data, list | tuple):
         return [stringify_keys(v, memo) for v in data]
     return data
 
 
 def sort_class(cls: Iterable[type]) -> list[type]:
-    """Sort classes by inheritance. From child to parent."""
+    """
+    ### `sort_class()`
+    Sort classes by inheritance. From child to parent.
+    """
     ls: list[type] = []
     for c in cls:
         it = iter(enumerate(ls))
         try:
             while True:
                 i, p = next(it)
                 if issubclass(c, p):
@@ -73,58 +77,86 @@
         except StopIteration:
             ls.append(c)
     return ls
 
 
 def str_to_object(object_name: str, module: str = "__main__") -> Any:
     """
+    ### `str_to_object()`
     Get object by its name and module(default to main module)
     """
     return getattr(sys.modules[module], object_name)
 
 
-def load_module(module_name: str, module_path: str | pathlib.Path):
+def load_module(module_name: str,
+                module_path: str | Path | None = None):
     """
+    ### `load_module()`
     Load a module from a path.
     """
     if module_name in sys.modules:
         return sys.modules[module_name]
-    module_path = real_path(module_path)
-    if module_path not in sys.path:
-        sys.path.append(str(module_path))
+    if module_path:
+        module_path = module_path.resolve()
+        if module_path not in sys.path:
+            sys.path.append(str(module_path))
     module = importlib.import_module(module_name)
     return module
 
 
-def real_dir(path: str | pathlib.Path | None = None) -> pathlib.Path:
+def real_dir(path: str | Path | None = None) -> Path:
     """
+    ### `real_dir()`
     Get the real path of the directory of the given file.
-    
+
     When `path` is `None`, the directory of the main module will be returned.
-    
+
     If main module is not a file, the current working directory will be returned.
     """
-    path = path or getattr(sys.modules["__main__"], "__file__", '') or ''
-    path = os.path.dirname(real_path(path))
-    return pathlib.Path(path)
+    path = path or getattr(sys.modules["__main__"], "__file__", '.')
+    path = Path(cast(str, path)).resolve()
+    return path.parent
 
 
-def real_path(path: str | pathlib.Path) -> pathlib.Path:
+def real_path(path: str | Path) -> Path:
     """
+    ### `real_path()`
     Get the real path of the given file.
+
+    *This helper function was written before I knew about `pathlib.Path.resolve()`...
+    Just leave it here for compatibility.
     """
-    path = os.path.expanduser(path)
-    path = os.path.expandvars(path)
-    path = os.path.normpath(path)
-    path = os.path.realpath(path)
-    return pathlib.Path(path)
+    # path = os.path.expanduser(path)
+    # path = os.path.expandvars(path)
+    # path = os.path.normpath(path)
+    # path = os.path.realpath(path)
+    return Path(path).resolve()
+
+
+def relative_to(path: Path | str, anchor: Path | str | None = None) -> Path:
+    """
+    ### `relative_to()` 
+    Expand relative path based on the anchor
+    Default to the main file.
+
+    >>> relative_to("foo/bar", "dir/baz") == Path("dir/foo/bar")
+
+    >>> relative_to("../", "foo/bar") == Path("foo/")
+    """
+    anchor = anchor or getattr(sys.modules["__main__"], "__file__", '.')
+    anchor = anchor if isinstance(anchor, Path) else Path(cast(str, anchor))
+    path = path if isinstance(path, Path) else Path(path)
+    if path.is_absolute():
+        return path
+    return anchor.parent / path
 
 
 def version_cmp(v1: str, v2: str) -> int:
     """
+    ### `version_cmp()`
     Compare two version strings.
     Versions must be valid SemVer strings or 'v'/'V' prefixed SemVer strings,
     or a `ValueError` will be raised.
 
     Returns positive `int` if v1 > v2, `0` if v1 == v2, negative `int` if v1 < v2.
     """
     v1s: dict[str, Sequence] = {}
@@ -163,35 +195,39 @@
 
     # Pre-release versions are always lower than release versions
     return len(v2s["pre"]) - len(v1s["pre"])
 
 
 def to_ordinal(num: int) -> str:
     """
+    ### `to_ordinal()`
     Convert a number to its ordinal representation.
     """
     abs_num = abs(num)
     if abs_num % 100 in [11, 12, 13]:
         return f"{num}th"
     return f"{num}{['th', 'st', 'nd', 'rd'][abs_num % 10 if abs_num % 10 < 4 else 0]}"
 
 
 @overload
 def check(cond: Literal[False, 0, b'', '', None], msg: str = None,
           exc: type[Exception] = AssertionError,) -> NoReturn:
     ...
 
+
 @overload
 def check(cond: Any, msg: str = None,
           exc: type[Exception] = AssertionError,) -> None | NoReturn:
     ...
 
+
 def check(cond: Any, msg: str = None,
           exc: type[Exception] = AssertionError,) -> None | NoReturn:
     """
+    ### `check()`
     Raise an exception if the condition is not met.
 
     `assert` may be unavailable in some cases, so this function is provided.
     """
     if not cond:
         if msg is None:  # pragma: no branch
             curframe = inspect.currentframe()
```

### Comparing `vermils-0.3.0/vermils/gadgets/monologger.py` & `vermils-0.3.1/vermils/gadgets/monologger.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/gadgets/sidelogging/__init__.py` & `vermils-0.3.1/vermils/gadgets/sidelogging/__init__.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/io/aio/os.py` & `vermils-0.3.1/vermils/io/aio/os.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/io/aio/path.py` & `vermils-0.3.1/vermils/io/aio/path.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/io/aio/tempfile.py` & `vermils-0.3.1/vermils/io/aio/tempfile.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/io/aio/wrappers.py` & `vermils-0.3.1/vermils/io/aio/wrappers.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/io/misc.py` & `vermils-0.3.1/vermils/io/misc.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/io/puller/modifier.py` & `vermils-0.3.1/vermils/io/puller/modifier.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/io/puller/pullers.py` & `vermils-0.3.1/vermils/io/puller/pullers.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/react/actionchain.py` & `vermils-0.3.1/vermils/react/actionchain.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/vermils/react/eventhook.py` & `vermils-0.3.1/vermils/react/eventhook.py`

 * *Files identical despite different names*

### Comparing `vermils-0.3.0/PKG-INFO` & `vermils-0.3.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vermils
-Version: 0.3.0
+Version: 0.3.1
 Summary: 
 Home-page: https://github.com/VermiIIi0n/VermilsMagicPocket
 License: MIT
 Keywords: utilities
 Author: VermiIIi0n
 Author-email: dungeon.behind0t@icloud.com
 Requires-Python: >=3.10,<4.0
```

