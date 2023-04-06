# Comparing `tmp/lsst-resources-26.0.0a20230400.tar.gz` & `tmp/lsst-resources-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lsst-resources-26.0.0a20230400.tar", last modified: Thu Jan 26 09:56:03 2023, max compression
+gzip compressed data, was "lsst-resources-26.0.0a20230500.tar", last modified: Thu Feb  2 14:05:08 2023, max compression
```

## Comparing `lsst-resources-26.0.0a20230400.tar` & `lsst-resources-26.0.0a20230500.tar`

### file list

```diff
@@ -1,38 +1,44 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:03.199569 lsst-resources-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/COPYRIGHT
--rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       33 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1744 2023-01-26 09:56:03.199569 lsst-resources-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      912 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:03.195569 lsst-resources-26.0.0a20230400/doc/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:03.195569 lsst-resources-26.0.0a20230400/doc/lsst.resources/
--rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/doc/lsst.resources/CHANGES.rst
--rw-r--r--   0 runner    (1001) docker     (123)      524 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/doc/lsst.resources/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3279 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:03.195569 lsst-resources-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:03.195569 lsst-resources-26.0.0a20230400/python/lsst/
--rw-r--r--   0 runner    (1001) docker     (123)      466 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:03.195569 lsst-resources-26.0.0a20230400/python/lsst/resources/
--rw-r--r--   0 runner    (1001) docker     (123)      628 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    48281 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/_resourcePath.py
--rw-r--r--   0 runner    (1001) docker     (123)    20353 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/file.py
--rw-r--r--   0 runner    (1001) docker     (123)    12072 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/gs.py
--rw-r--r--   0 runner    (1001) docker     (123)    23506 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/http.py
--rw-r--r--   0 runner    (1001) docker     (123)     7979 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/location.py
--rw-r--r--   0 runner    (1001) docker     (123)      934 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/mem.py
--rw-r--r--   0 runner    (1001) docker     (123)     1919 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/packageresource.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/py.typed
--rw-r--r--   0 runner    (1001) docker     (123)    17138 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/s3.py
--rw-r--r--   0 runner    (1001) docker     (123)     7097 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/s3utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     9581 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/schemeless.py
--rw-r--r--   0 runner    (1001) docker     (123)    32858 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/tests.py
--rw-r--r--   0 runner    (1001) docker     (123)     4697 2023-01-26 09:55:50.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 09:56:03.000000 lsst-resources-26.0.0a20230400/python/lsst/resources/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:03.199569 lsst-resources-26.0.0a20230400/python/lsst_resources.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1744 2023-01-26 09:56:03.000000 lsst-resources-26.0.0a20230400/python/lsst_resources.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      900 2023-01-26 09:56:03.000000 lsst-resources-26.0.0a20230400/python/lsst_resources.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:03.000000 lsst-resources-26.0.0a20230400/python/lsst_resources.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      220 2023-01-26 09:56:03.000000 lsst-resources-26.0.0a20230400/python/lsst_resources.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-01-26 09:56:03.000000 lsst-resources-26.0.0a20230400/python/lsst_resources.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:02.000000 lsst-resources-26.0.0a20230400/python/lsst_resources.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      168 2023-01-26 09:56:03.199569 lsst-resources-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.890030 lsst-resources-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/COPYRIGHT
+-rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       33 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1744 2023-02-02 14:05:08.890030 lsst-resources-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      912 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.886030 lsst-resources-26.0.0a20230500/doc/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.886030 lsst-resources-26.0.0a20230500/doc/lsst.resources/
+-rw-r--r--   0 runner    (1001) docker     (123)     2068 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/doc/lsst.resources/CHANGES.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      524 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/doc/lsst.resources/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3280 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.886030 lsst-resources-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.886030 lsst-resources-26.0.0a20230500/python/lsst/
+-rw-r--r--   0 runner    (1001) docker     (123)      466 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.886030 lsst-resources-26.0.0a20230500/python/lsst/resources/
+-rw-r--r--   0 runner    (1001) docker     (123)      682 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.890030 lsst-resources-26.0.0a20230500/python/lsst/resources/_resourceHandles/
+-rw-r--r--   0 runner    (1001) docker     (123)       76 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/_resourceHandles/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4377 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/_resourceHandles/_baseResourceHandle.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3478 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/_resourceHandles/_fileResourceHandle.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5893 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/_resourceHandles/_httpResourceHandle.py
+-rw-r--r--   0 runner    (1001) docker     (123)    11426 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/_resourceHandles/_s3ResourceHandle.py
+-rw-r--r--   0 runner    (1001) docker     (123)    49359 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/_resourcePath.py
+-rw-r--r--   0 runner    (1001) docker     (123)    20399 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/file.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12162 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/gs.py
+-rw-r--r--   0 runner    (1001) docker     (123)    24669 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/http.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7979 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/location.py
+-rw-r--r--   0 runner    (1001) docker     (123)      934 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/mem.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2008 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/packageresource.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/py.typed
+-rw-r--r--   0 runner    (1001) docker     (123)    16564 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/s3.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8912 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/s3utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9581 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/schemeless.py
+-rw-r--r--   0 runner    (1001) docker     (123)    32859 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/tests.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4697 2023-02-02 14:04:52.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:05:08.000000 lsst-resources-26.0.0a20230500/python/lsst/resources/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:05:08.890030 lsst-resources-26.0.0a20230500/python/lsst_resources.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1744 2023-02-02 14:05:08.000000 lsst-resources-26.0.0a20230500/python/lsst_resources.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1197 2023-02-02 14:05:08.000000 lsst-resources-26.0.0a20230500/python/lsst_resources.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:08.000000 lsst-resources-26.0.0a20230500/python/lsst_resources.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      220 2023-02-02 14:05:08.000000 lsst-resources-26.0.0a20230500/python/lsst_resources.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-02-02 14:05:08.000000 lsst-resources-26.0.0a20230500/python/lsst_resources.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:05:08.000000 lsst-resources-26.0.0a20230500/python/lsst_resources.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      168 2023-02-02 14:05:08.890030 lsst-resources-26.0.0a20230500/setup.cfg
```

### Comparing `lsst-resources-26.0.0a20230400/LICENSE` & `lsst-resources-26.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `lsst-resources-26.0.0a20230400/PKG-INFO` & `lsst-resources-26.0.0a20230500/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-resources
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: An abstraction layer for reading and writing from URI file resources.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: BSD 3-Clause License
 Project-URL: Homepage, https://github.com/lsst/resources
 Keywords: lsst
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: BSD License
```

### Comparing `lsst-resources-26.0.0a20230400/README.md` & `lsst-resources-26.0.0a20230500/README.md`

 * *Files identical despite different names*

### Comparing `lsst-resources-26.0.0a20230400/doc/lsst.resources/CHANGES.rst` & `lsst-resources-26.0.0a20230500/doc/lsst.resources/CHANGES.rst`

 * *Files identical despite different names*

### Comparing `lsst-resources-26.0.0a20230400/doc/lsst.resources/index.rst` & `lsst-resources-26.0.0a20230500/doc/lsst.resources/index.rst`

 * *Files identical despite different names*

### Comparing `lsst-resources-26.0.0a20230400/pyproject.toml` & `lsst-resources-26.0.0a20230500/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -99,15 +99,15 @@
     [[tool.towncrier.type]]
         directory = "removal"
         name = "An API Removal or Deprecation"
         showcontent = true
 
 [tool.black]
 line-length = 110
-target-version = ["py38"]
+target-version = ["py310"]
 
 [tool.isort]
 profile = "black"
 line_length = 110
 
 [tool.lsst_versions]
 write_to = "python/lsst/resources/version.py"
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/__init__.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/__init__.py`

 * *Files 13% similar despite different names*

```diff
@@ -8,10 +8,12 @@
 #
 # Use of this source code is governed by a 3-clause BSD-style
 # license that can be found in the LICENSE file.
 
 
 """ResourcePath is a package for abstracting access to local or remote files."""
 
+from ._resourceHandles import ResourceHandleProtocol
+
 # Should only expose ResourcePath and its input type alias
 from ._resourcePath import ResourcePath, ResourcePathExpression
 from .version import *
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/_resourcePath.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/_resourcePath.py`

 * *Files 2% similar despite different names*

```diff
@@ -25,29 +25,30 @@
 import urllib.parse
 from pathlib import Path, PurePath, PurePosixPath
 from random import Random
 
 __all__ = ("ResourcePath", "ResourcePathExpression")
 
 from typing import (
-    IO,
     TYPE_CHECKING,
     Any,
     Dict,
     Iterable,
     Iterator,
     List,
     Literal,
     Optional,
     Tuple,
     Type,
     Union,
     overload,
 )
 
+from ._resourceHandles._baseResourceHandle import ResourceHandleProtocol
+
 if TYPE_CHECKING:
     from .utils import TransactionProtocol
 
 
 log = logging.getLogger(__name__)
 
 # Regex for looking for URI escapes
@@ -1233,15 +1234,15 @@
     @contextlib.contextmanager
     def open(
         self,
         mode: str = "r",
         *,
         encoding: Optional[str] = None,
         prefer_file_temporary: bool = False,
-    ) -> Iterator[IO]:
+    ) -> Iterator[ResourceHandleProtocol]:
         """Return a context manager that wraps an object that behaves like an
         open file at the location of the URI.
 
         Parameters
         ----------
         mode : `str`
             String indicating the mode in which to open the file.  Values are
@@ -1295,27 +1296,58 @@
                 with open(local_uri.ospath, mode=mode, encoding=encoding) as file_buffer:
                     if "a" in mode:
                         file_buffer.seek(0, io.SEEK_END)
                     yield file_buffer
                 if "r" not in mode or "+" in mode:
                     self.transfer_from(local_uri, transfer="copy", overwrite=("x" not in mode))
         else:
-            if "r" in mode or "a" in mode:
-                in_bytes = self.read()
-            else:
-                in_bytes = b""
-            if "b" in mode:
-                bytes_buffer = io.BytesIO(in_bytes)
-                if "a" in mode:
-                    bytes_buffer.seek(0, io.SEEK_END)
-                yield bytes_buffer
-                out_bytes = bytes_buffer.getvalue()
-            else:
-                if encoding is None:
-                    encoding = locale.getpreferredencoding(False)
-                str_buffer = io.StringIO(in_bytes.decode(encoding))
-                if "a" in mode:
-                    str_buffer.seek(0, io.SEEK_END)
-                yield str_buffer
-                out_bytes = str_buffer.getvalue().encode(encoding)
-            if "r" not in mode or "+" in mode:
-                self.write(out_bytes, overwrite=("x" not in mode))
+            with self._openImpl(mode, encoding=encoding) as handle:
+                yield handle
+
+    @contextlib.contextmanager
+    def _openImpl(
+        self, mode: str = "r", *, encoding: Optional[str] = None
+    ) -> Iterator[ResourceHandleProtocol]:
+        """Implement opening of a resource handle.
+
+        This private method may be overridden by specific `ResourcePath`
+        implementations to provide a customized handle like interface.
+
+        Parameters
+        ----------
+        mode : `str`
+            The mode the handle should be opened with
+        encoding : `str`, optional
+            The byte encoding of any binary text
+
+        Yields
+        ------
+        handle : `BaseResourceHandle`
+            A handle that conforms to the `BaseResourcehandle interface
+
+        Notes
+        -----
+        The base implementation of a file handle reads in a files entire
+        contents into a buffer for manipulation, and then writes it back out
+        upon close. Subclasses of this class may offer more fine grained
+        control.
+        """
+        if "r" in mode or "a" in mode:
+            in_bytes = self.read()
+        else:
+            in_bytes = b""
+        if "b" in mode:
+            bytes_buffer = io.BytesIO(in_bytes)
+            if "a" in mode:
+                bytes_buffer.seek(0, io.SEEK_END)
+            yield bytes_buffer
+            out_bytes = bytes_buffer.getvalue()
+        else:
+            if encoding is None:
+                encoding = locale.getpreferredencoding(False)
+            str_buffer = io.StringIO(in_bytes.decode(encoding))
+            if "a" in mode:
+                str_buffer.seek(0, io.SEEK_END)
+            yield str_buffer
+            out_bytes = str_buffer.getvalue().encode(encoding)
+        if "r" not in mode or "+" in mode:
+            self.write(out_bytes, overwrite=("x" not in mode))
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/file.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/file.py`

 * *Files 5% similar despite different names*

```diff
@@ -21,14 +21,15 @@
 import shutil
 import urllib.parse
 
 __all__ = ("FileResourcePath",)
 
 from typing import IO, TYPE_CHECKING, Iterator, List, Optional, Tuple, Union
 
+from ._resourceHandles._fileResourceHandle import FileResourceHandle
 from ._resourcePath import ResourcePath
 from .utils import NoTransaction, os2posix, posix2os
 
 if TYPE_CHECKING:
     from .utils import TransactionProtocol
 
 
@@ -473,17 +474,15 @@
 
         if parsed.params or parsed.query:
             log.warning("Additional items unexpectedly encountered in file URI: %s", parsed.geturl())
 
         return parsed, dirLike
 
     @contextlib.contextmanager
-    def open(
+    def _openImpl(
         self,
         mode: str = "r",
         *,
         encoding: Optional[str] = None,
-        prefer_file_temporary: bool = False,
     ) -> Iterator[IO]:
-        # Docstring inherited.
-        with open(self.ospath, mode=mode, encoding=encoding) as buffer:
-            yield buffer
+        with FileResourceHandle(mode=mode, log=log, filename=self.ospath, encoding=encoding) as buffer:
+            yield buffer  # type: ignore
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/gs.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/gs.py`

 * *Files 2% similar despite different names*

```diff
@@ -15,15 +15,17 @@
 
 __all__ = ("GSResourcePath",)
 
 import contextlib
 import logging
 import re
 import tempfile
-from typing import IO, TYPE_CHECKING, Iterator, List, Optional, Set, Tuple, Union
+from typing import TYPE_CHECKING, Iterator, List, Optional, Set, Tuple, Union
+
+from ._resourceHandles._baseResourceHandle import ResourceHandleProtocol
 
 try:
     import google.api_core.retry as retry
     import google.cloud.storage as storage
     from google.cloud.exceptions import (
         BadGateway,
         InternalServerError,
@@ -258,15 +260,15 @@
     @contextlib.contextmanager
     def open(
         self,
         mode: str = "r",
         *,
         encoding: Optional[str] = None,
         prefer_file_temporary: bool = False,
-    ) -> Iterator[IO]:
+    ) -> Iterator[ResourceHandleProtocol]:
         # Docstring inherited
         if self.isdir() or self.is_root:
             raise IsADirectoryError(f"Can not 'open' a directory URI: {self}")
         if "x" in mode:
             if self.exists():
                 raise FileExistsError(f"File at {self} already exists.")
             mode = mode.replace("x", "w")
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/http.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/http.py`

 * *Files 3% similar despite different names*

```diff
@@ -7,33 +7,35 @@
 # for details of code ownership.
 #
 # Use of this source code is governed by a 3-clause BSD-style
 # license that can be found in the LICENSE file.
 
 from __future__ import annotations
 
+__all__ = ("HttpResourcePath",)
+
+import contextlib
 import functools
+import io
 import logging
 import os
 import os.path
 import random
 import stat
 import tempfile
+from typing import TYPE_CHECKING, BinaryIO, Iterator, Optional, Tuple, Union, cast
 
 import requests
-
-__all__ = ("HttpResourcePath",)
-
-from typing import TYPE_CHECKING, BinaryIO, Optional, Tuple, Union
-
 from lsst.utils.timer import time_this
 from requests.adapters import HTTPAdapter
 from requests.auth import AuthBase
 from urllib3.util.retry import Retry
 
+from ._resourceHandles import ResourceHandleProtocol
+from ._resourceHandles._httpResourceHandle import HttpReadResourceHandle
 from ._resourcePath import ResourcePath
 
 if TYPE_CHECKING:
     from .utils import TransactionProtocol
 
 log = logging.getLogger(__name__)
 
@@ -570,14 +572,39 @@
                 log.debug("PUT request to %s redirected to %s", self.geturl(), final_url)
 
         # Send data to its final destination.
         resp = self.put_session.put(final_url, data=data, timeout=TIMEOUT)
         if resp.status_code not in [200, 201, 202, 204]:
             raise ValueError(f"Can not write file {self}, status code: {resp.status_code}")
 
+    @contextlib.contextmanager
+    def _openImpl(
+        self,
+        mode: str = "r",
+        *,
+        encoding: Optional[str] = None,
+    ) -> Iterator[ResourceHandleProtocol]:
+        url = self.geturl()
+        response = self.session.head(url, timeout=TIMEOUT, allow_redirects=True)
+        accepts_range = "Accept-Ranges" in response.headers
+        handle: ResourceHandleProtocol
+        if mode in ("rb", "r") and accepts_range:
+            handle = HttpReadResourceHandle(
+                mode, log, url=self.geturl(), session=self.session, timeout=TIMEOUT
+            )
+            if mode == "r":
+                # cast because the protocol is compatible, but does not have
+                # BytesIO in the inheritance tree
+                yield io.TextIOWrapper(cast(io.BytesIO, handle), encoding=encoding)
+            else:
+                yield handle
+        else:
+            with super()._openImpl(mode, encoding=encoding) as http_handle:
+                yield http_handle
+
 
 def _is_protected(filepath: str) -> bool:
     """Return true if the permissions of file at filepath only allow for access
     by its owner.
 
     Parameters
     ----------
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/location.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/location.py`

 * *Files identical despite different names*

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/mem.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/mem.py`

 * *Files identical despite different names*

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/packageresource.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/packageresource.py`

 * *Files 14% similar despite different names*

```diff
@@ -7,20 +7,21 @@
 # for details of code ownership.
 #
 # Use of this source code is governed by a 3-clause BSD-style
 # license that can be found in the LICENSE file.
 
 import contextlib
 import logging
-from typing import IO, Iterator, Optional
+from typing import Iterator, Optional
 
 import pkg_resources
 
 __all__ = ("PackageResourcePath",)
 
+from ._resourceHandles._baseResourceHandle import ResourceHandleProtocol
 from ._resourcePath import ResourcePath
 
 log = logging.getLogger(__name__)
 
 
 class PackageResourcePath(ResourcePath):
     """URI referring to a Python package resource.
@@ -42,15 +43,15 @@
     @contextlib.contextmanager
     def open(
         self,
         mode: str = "r",
         *,
         encoding: Optional[str] = None,
         prefer_file_temporary: bool = False,
-    ) -> Iterator[IO]:
+    ) -> Iterator[ResourceHandleProtocol]:
         # Docstring inherited.
         if "r" not in mode or "+" in mode:
             raise RuntimeError(f"Package resource URI {self} is read-only.")
         if "b" in mode:
             with pkg_resources.resource_stream(self.netloc, self.relativeToPathRoot) as buffer:
                 yield buffer
         else:
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/s3.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/s3.py`

 * *Files 4% similar despite different names*

```diff
@@ -7,97 +7,50 @@
 # for details of code ownership.
 #
 # Use of this source code is governed by a 3-clause BSD-style
 # license that can be found in the LICENSE file.
 
 from __future__ import annotations
 
+import contextlib
+import io
 import logging
 import re
+import sys
 import tempfile
 import threading
 
 __all__ = ("S3ResourcePath",)
 
-from http.client import HTTPException, ImproperConnectionState
-from types import ModuleType
-from typing import IO, TYPE_CHECKING, Any, Callable, Iterator, List, Optional, Tuple, Union, cast
+from typing import IO, TYPE_CHECKING, Iterator, List, Optional, Tuple, Union, cast
 
 from botocore.exceptions import ClientError
 from lsst.utils.timer import time_this
-from urllib3.exceptions import HTTPError, RequestError
 
+from ._resourceHandles._baseResourceHandle import ResourceHandleProtocol
+from ._resourceHandles._s3ResourceHandle import S3ResourceHandle
 from ._resourcePath import ResourcePath
-from .s3utils import bucketExists, getS3Client, s3CheckFileExists
+from .s3utils import (
+    _TooManyRequestsException,
+    all_retryable_errors,
+    backoff,
+    bucketExists,
+    getS3Client,
+    max_retry_time,
+    retryable_io_errors,
+    s3CheckFileExists,
+)
 
 if TYPE_CHECKING:
     try:
         import boto3
     except ImportError:
         pass
     from .utils import TransactionProtocol
 
-# https://pypi.org/project/backoff/
-try:
-    import backoff
-except ImportError:
-
-    class Backoff:
-        @staticmethod
-        def expo(func: Callable, *args: Any, **kwargs: Any) -> Callable:
-            return func
-
-        @staticmethod
-        def on_exception(func: Callable, *args: Any, **kwargs: Any) -> Callable:
-            return func
-
-    backoff = cast(ModuleType, Backoff)
-
-
-class _TooManyRequestsException(Exception):
-    """Private exception that can be used for 429 retry.
-
-    botocore refuses to deal with 429 error itself so issues a generic
-    ClientError.
-    """
-
-    pass
-
-
-# settings for "backoff" retry decorators. these retries are belt-and-
-# suspenders along with the retries built into Boto3, to account for
-# semantic differences in errors between S3-like providers.
-retryable_io_errors = (
-    # http.client
-    ImproperConnectionState,
-    HTTPException,
-    # urllib3.exceptions
-    RequestError,
-    HTTPError,
-    # built-ins
-    TimeoutError,
-    ConnectionError,
-    # private
-    _TooManyRequestsException,
-)
-
-# Client error can include NoSuchKey so retry may not be the right
-# thing. This may require more consideration if it is to be used.
-retryable_client_errors = (
-    # botocore.exceptions
-    ClientError,
-    # built-ins
-    PermissionError,
-)
-
-# Combine all errors into an easy package. For now client errors
-# are not included.
-all_retryable_errors = retryable_io_errors
-max_retry_time = 60
-
 
 log = logging.getLogger(__name__)
 
 
 class ProgressPercentage:
     """Progress bar for S3 file uploads."""
 
@@ -448,7 +401,25 @@
             return
         else:
             yield self, dirnames, filenames
 
         for dir in dirnames:
             new_uri = self.join(dir)
             yield from new_uri.walk(file_filter)
+
+    @contextlib.contextmanager
+    def _openImpl(
+        self,
+        mode: str = "r",
+        *,
+        encoding: Optional[str] = None,
+    ) -> Iterator[ResourceHandleProtocol]:
+        with S3ResourceHandle(mode, log, self.client, self.netloc, self.relativeToPathRoot) as handle:
+            if "b" in mode:
+                yield handle
+            else:
+                if encoding is None:
+                    encoding = sys.getdefaultencoding()
+                # cast because the protocol is compatible, but does not have
+                # BytesIO in the inheritance tree
+                with io.TextIOWrapper(cast(io.BytesIO, handle), encoding=encoding, write_through=True) as sub:
+                    yield sub
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/s3utils.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/s3utils.py`

 * *Files 25% similar despite different names*

```diff
@@ -13,33 +13,104 @@
 
 __all__ = (
     "getS3Client",
     "s3CheckFileExists",
     "bucketExists",
     "setAwsEnvCredentials",
     "unsetAwsEnvCredentials",
+    "backoff",
+    "all_retryable_errors",
+    "max_retry_time",
+    "retryable_io_errors",
+    "retryable_client_errors",
+    "_TooManyRequestsException",
 )
 
 import functools
 import os
-from typing import Optional, Tuple, Union
+from http.client import HTTPException, ImproperConnectionState
+from types import ModuleType
+from typing import Any, Callable, Optional, Tuple, Union, cast
+
+from botocore.exceptions import ClientError
+from urllib3.exceptions import HTTPError, RequestError
 
 try:
     import boto3
 except ImportError:
     boto3 = None
 
 try:
     import botocore
 except ImportError:
     botocore = None
 
+
 from ._resourcePath import ResourcePath
 from .location import Location
 
+# https://pypi.org/project/backoff/
+try:
+    import backoff
+except ImportError:
+
+    class Backoff:
+        @staticmethod
+        def expo(func: Callable, *args: Any, **kwargs: Any) -> Callable:
+            return func
+
+        @staticmethod
+        def on_exception(func: Callable, *args: Any, **kwargs: Any) -> Callable:
+            return func
+
+    backoff = cast(ModuleType, Backoff)
+
+
+class _TooManyRequestsException(Exception):
+    """Private exception that can be used for 429 retry.
+
+    botocore refuses to deal with 429 error itself so issues a generic
+    ClientError.
+    """
+
+    pass
+
+
+# settings for "backoff" retry decorators. these retries are belt-and-
+# suspenders along with the retries built into Boto3, to account for
+# semantic differences in errors between S3-like providers.
+retryable_io_errors = (
+    # http.client
+    ImproperConnectionState,
+    HTTPException,
+    # urllib3.exceptions
+    RequestError,
+    HTTPError,
+    # built-ins
+    TimeoutError,
+    ConnectionError,
+    # private
+    _TooManyRequestsException,
+)
+
+# Client error can include NoSuchKey so retry may not be the right
+# thing. This may require more consideration if it is to be used.
+retryable_client_errors = (
+    # botocore.exceptions
+    ClientError,
+    # built-ins
+    PermissionError,
+)
+
+
+# Combine all errors into an easy package. For now client errors
+# are not included.
+all_retryable_errors = retryable_io_errors
+max_retry_time = 60
+
 
 def getS3Client() -> boto3.client:
     """Create a S3 client with AWS (default) or the specified endpoint.
 
     Returns
     -------
     s3client : `botocore.client.S3`
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/schemeless.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/schemeless.py`

 * *Files identical despite different names*

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/tests.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/tests.py`

 * *Files 0% similar despite different names*

```diff
@@ -767,15 +767,15 @@
         with ResourcePath.temporary_uri(prefix=tmpdir, suffix=".txt") as tmp:
             _check_open(self, tmp, mode_suffixes=("", "t"))
             _check_open(self, tmp, mode_suffixes=("t",), encoding="utf-16")
             _check_open(self, tmp, mode_suffixes=("t",), prefer_file_temporary=True)
             _check_open(self, tmp, mode_suffixes=("t",), encoding="utf-16", prefer_file_temporary=True)
         with ResourcePath.temporary_uri(prefix=tmpdir, suffix=".dat") as tmp:
             _check_open(self, tmp, mode_suffixes=("b",))
-            _check_open(self, tmp, mode_suffixes=("b"), prefer_file_temporary=True)
+            _check_open(self, tmp, mode_suffixes=("b",), prefer_file_temporary=True)
 
         with self.assertRaises(IsADirectoryError):
             with self.root_uri.open():
                 pass
 
     def test_mexists(self) -> None:
         root = self.tmpdir.join("mexists/")
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst/resources/utils.py` & `lsst-resources-26.0.0a20230500/python/lsst/resources/utils.py`

 * *Files identical despite different names*

### Comparing `lsst-resources-26.0.0a20230400/python/lsst_resources.egg-info/PKG-INFO` & `lsst-resources-26.0.0a20230500/python/lsst_resources.egg-info/PKG-INFO`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lsst-resources
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: An abstraction layer for reading and writing from URI file resources.
 Author-email: Rubin Observatory Data Management <dm-admin@lists.lsst.org>
 License: BSD 3-Clause License
 Project-URL: Homepage, https://github.com/lsst/resources
 Keywords: lsst
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: BSD License
```

### Comparing `lsst-resources-26.0.0a20230400/python/lsst_resources.egg-info/SOURCES.txt` & `lsst-resources-26.0.0a20230500/python/lsst_resources.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -18,13 +18,18 @@
 python/lsst/resources/py.typed
 python/lsst/resources/s3.py
 python/lsst/resources/s3utils.py
 python/lsst/resources/schemeless.py
 python/lsst/resources/tests.py
 python/lsst/resources/utils.py
 python/lsst/resources/version.py
+python/lsst/resources/_resourceHandles/__init__.py
+python/lsst/resources/_resourceHandles/_baseResourceHandle.py
+python/lsst/resources/_resourceHandles/_fileResourceHandle.py
+python/lsst/resources/_resourceHandles/_httpResourceHandle.py
+python/lsst/resources/_resourceHandles/_s3ResourceHandle.py
 python/lsst_resources.egg-info/PKG-INFO
 python/lsst_resources.egg-info/SOURCES.txt
 python/lsst_resources.egg-info/dependency_links.txt
 python/lsst_resources.egg-info/requires.txt
 python/lsst_resources.egg-info/top_level.txt
 python/lsst_resources.egg-info/zip-safe
```

