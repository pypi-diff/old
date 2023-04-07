# Comparing `tmp/drb-driver-zip-1.1.0.tar.gz` & `tmp/drb-driver-zip-1.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "drb-driver-zip-1.1.0.tar", last modified: Mon Dec 19 13:36:05 2022, max compression
+gzip compressed data, was "drb-driver-zip-1.2.0.tar", last modified: Fri Apr  7 13:44:35 2023, max compression
```

## Comparing `drb-driver-zip-1.1.0.tar` & `drb-driver-zip-1.2.0.tar`

### file list

```diff
@@ -1,27 +1,40 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-19 13:36:05.776099 drb-driver-zip-1.1.0/
--rw-rw-rw-   0 root         (0) root         (0)       58 2022-12-19 10:42:26.000000 drb-driver-zip-1.1.0/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1754 2022-12-19 13:36:05.776099 drb-driver-zip-1.1.0/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)     1181 2022-12-19 10:07:56.000000 drb-driver-zip-1.1.0/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-19 13:36:05.768099 drb-driver-zip-1.1.0/drb/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-19 13:36:05.768099 drb-driver-zip-1.1.0/drb/drivers/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-19 13:36:05.840100 drb-driver-zip-1.1.0/drb/drivers/zip/
--rw-rw-rw-   0 root         (0) root         (0)      232 2022-12-19 10:07:56.000000 drb-driver-zip-1.1.0/drb/drivers/zip/__init__.py
--rw-r--r--   0 root         (0) root         (0)      497 2022-12-19 13:36:05.840100 drb-driver-zip-1.1.0/drb/drivers/zip/_version.py
--rw-rw-rw-   0 root         (0) root         (0)    10127 2022-12-19 13:19:25.000000 drb-driver-zip-1.1.0/drb/drivers/zip/zip.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-19 13:36:05.772099 drb-driver-zip-1.1.0/drb/exceptions/
--rw-rw-rw-   0 root         (0) root         (0)       97 2022-12-19 13:19:25.000000 drb-driver-zip-1.1.0/drb/exceptions/zip.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-19 13:36:05.768099 drb-driver-zip-1.1.0/drb/topics/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-19 13:36:05.772099 drb-driver-zip-1.1.0/drb/topics/zip/
--rw-rw-rw-   0 root         (0) root         (0)        0 2022-12-19 10:07:56.000000 drb-driver-zip-1.1.0/drb/topics/zip/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      121 2022-12-19 10:07:56.000000 drb-driver-zip-1.1.0/drb/topics/zip/cortex.yml
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-12-19 13:36:05.776099 drb-driver-zip-1.1.0/drb_driver_zip.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1754 2022-12-19 13:36:05.000000 drb-driver-zip-1.1.0/drb_driver_zip.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      455 2022-12-19 13:36:05.000000 drb-driver-zip-1.1.0/drb_driver_zip.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-12-19 13:36:05.000000 drb-driver-zip-1.1.0/drb_driver_zip.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       84 2022-12-19 13:36:05.000000 drb-driver-zip-1.1.0/drb_driver_zip.egg-info/entry_points.txt
--rw-r--r--   0 root         (0) root         (0)       34 2022-12-19 13:36:05.000000 drb-driver-zip-1.1.0/drb_driver_zip.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        4 2022-12-19 13:36:05.000000 drb-driver-zip-1.1.0/drb_driver_zip.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)       33 2022-12-19 10:07:56.000000 drb-driver-zip-1.1.0/requirements.txt
--rw-rw-rw-   0 root         (0) root         (0)      208 2022-12-19 13:36:05.776099 drb-driver-zip-1.1.0/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)     1297 2022-12-19 10:07:56.000000 drb-driver-zip-1.1.0/setup.py
--rw-rw-rw-   0 root         (0) root         (0)    83021 2022-12-19 10:07:56.000000 drb-driver-zip-1.1.0/versioneer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.123805 drb-driver-zip-1.2.0/
+-rw-rw-rw-   0 root         (0) root         (0)     7651 2023-01-19 13:43:02.000000 drb-driver-zip-1.2.0/LICENCE.txt
+-rw-rw-rw-   0 root         (0) root         (0)       58 2022-12-19 10:42:26.000000 drb-driver-zip-1.2.0/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1781 2023-04-07 13:44:35.123805 drb-driver-zip-1.2.0/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)     1181 2022-12-19 10:07:56.000000 drb-driver-zip-1.2.0/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.111805 drb-driver-zip-1.2.0/docs/
+-rw-rw-rw-   0 root         (0) root         (0)     1560 2022-12-19 10:07:56.000000 drb-driver-zip-1.2.0/docs/conf.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.103805 drb-driver-zip-1.2.0/docs/dev/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.111805 drb-driver-zip-1.2.0/docs/dev/example/
+-rw-rw-rw-   0 root         (0) root         (0)      789 2022-12-19 10:07:56.000000 drb-driver-zip-1.2.0/docs/dev/example/open.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.107805 drb-driver-zip-1.2.0/drb/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.107805 drb-driver-zip-1.2.0/drb/drivers/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.127805 drb-driver-zip-1.2.0/drb/drivers/zip/
+-rw-rw-rw-   0 root         (0) root         (0)      232 2022-12-19 10:07:56.000000 drb-driver-zip-1.2.0/drb/drivers/zip/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      497 2023-04-07 13:44:35.127805 drb-driver-zip-1.2.0/drb/drivers/zip/_version.py
+-rw-rw-rw-   0 root         (0) root         (0)     8999 2023-04-06 08:41:32.000000 drb-driver-zip-1.2.0/drb/drivers/zip/zip.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.115805 drb-driver-zip-1.2.0/drb/exceptions/
+-rw-rw-rw-   0 root         (0) root         (0)       97 2022-12-19 13:19:25.000000 drb-driver-zip-1.2.0/drb/exceptions/zip.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.107805 drb-driver-zip-1.2.0/drb/topics/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.115805 drb-driver-zip-1.2.0/drb/topics/zip/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2022-12-19 10:07:56.000000 drb-driver-zip-1.2.0/drb/topics/zip/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      121 2023-04-07 13:43:53.000000 drb-driver-zip-1.2.0/drb/topics/zip/cortex.yml
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.119805 drb-driver-zip-1.2.0/drb_driver_zip.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1781 2023-04-07 13:44:35.000000 drb-driver-zip-1.2.0/drb_driver_zip.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      636 2023-04-07 13:44:35.000000 drb-driver-zip-1.2.0/drb_driver_zip.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 13:44:35.000000 drb-driver-zip-1.2.0/drb_driver_zip.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       83 2023-04-07 13:44:35.000000 drb-driver-zip-1.2.0/drb_driver_zip.egg-info/entry_points.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 13:44:34.000000 drb-driver-zip-1.2.0/drb_driver_zip.egg-info/not-zip-safe
+-rw-r--r--   0 root         (0) root         (0)       11 2023-04-07 13:44:35.000000 drb-driver-zip-1.2.0/drb_driver_zip.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       20 2023-04-07 13:44:35.000000 drb-driver-zip-1.2.0/drb_driver_zip.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)      101 2023-03-24 13:31:07.000000 drb-driver-zip-1.2.0/pyproject.toml
+-rw-rw-rw-   0 root         (0) root         (0)       10 2023-03-24 13:31:07.000000 drb-driver-zip-1.2.0/requirements.txt
+-rw-rw-rw-   0 root         (0) root         (0)     1039 2023-04-07 13:44:35.123805 drb-driver-zip-1.2.0/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)      124 2023-03-24 13:31:07.000000 drb-driver-zip-1.2.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 13:44:35.123805 drb-driver-zip-1.2.0/tests/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-03-24 13:31:07.000000 drb-driver-zip-1.2.0/tests/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     4188 2022-12-19 10:07:56.000000 drb-driver-zip-1.2.0/tests/test_impl.py
+-rw-rw-rw-   0 root         (0) root         (0)     1802 2023-03-24 13:31:07.000000 drb-driver-zip-1.2.0/tests/test_signature.py
+-rw-rw-rw-   0 root         (0) root         (0)    12735 2023-03-24 13:31:07.000000 drb-driver-zip-1.2.0/tests/test_zip.py
+-rw-rw-rw-   0 root         (0) root         (0)    83021 2022-12-19 10:07:56.000000 drb-driver-zip-1.2.0/versioneer.py
```

### Comparing `drb-driver-zip-1.1.0/PKG-INFO` & `drb-driver-zip-1.2.0/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 Metadata-Version: 2.1
 Name: drb-driver-zip
-Version: 1.1.0
-Summary: DRB Zip driver
+Version: 1.2.0
+Summary: DRB driver Zip
 Home-page: https://gitlab.com/drb-python/impl/zip
 Author: GAEL Systems
 Author-email: drb-python@gael.fr
-License: UNKNOWN
+License: LGPLv3
 Project-URL: Documentation, https://drb-python.gitlab.io/impl/zip
 Project-URL: Source, https://gitlab.com/drb-python/impl/zip
-Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3.8
-Classifier: License :: OSI Approved :: Apache Software License
+Classifier: License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
+License-File: LICENCE.txt
 
 # ZipNode Driver
 This drb-driver-zip module implements access to zip containers with DRB data model. It is able to navigates among the zip contents.
 
 ## Zip Factory and Zip Node
 The module implements the basic factory model defined in DRB in its node resolver. Based on the python entry point mechanism, this module can be dynamically imported into applications.
 
@@ -34,9 +34,7 @@
 
 ## Using this module
 To include this module into your project, the `drb-driver-zip` module shall be referenced into `requirements.txt` file, or the following pip line can be run:
 
 ```commandline
 pip install drb-driver-zip
 ```
-
-
```

### Comparing `drb-driver-zip-1.1.0/README.md` & `drb-driver-zip-1.2.0/README.md`

 * *Files identical despite different names*

### Comparing `drb-driver-zip-1.1.0/drb/drivers/zip/zip.py` & `drb-driver-zip-1.2.0/drb/drivers/zip/zip.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,19 +1,18 @@
 import enum
 import io
 import zipfile
 from typing import Any, List, Dict, Optional, Tuple
 from zipfile import ZipExtFile, ZipInfo
+from deprecated import deprecated
 
 from drb.core import DrbNode, ParsedPath, DrbFactory
-from drb.exceptions.core import DrbException, DrbNotImplementationException
+from drb.exceptions.core import DrbNotImplementationException
 from drb.nodes.abstract_node import AbstractNode
 from drb.topics.resolver import resolve_children
-
-import drb
 from drb.exceptions.zip import DrbZipNodeException
 
 
 class DrbZipAttributeNames(enum.Enum):
     SIZE = 'size'
     """
     The size of the file in bytes.
@@ -42,76 +41,51 @@
                             each file in the ZIP archive.
 
     """
 
     def __init__(self, parent: DrbNode, zip_info: ZipInfo):
         super().__init__()
         self._zip_info = zip_info
-        self._attributes: Dict[Tuple[str, str], Any] = None
-        self._name = None
+        if zip_info is not None:
+            self.name = self.__retrieve_name(zip_info)
+            if zip_info.is_dir():
+                self._available_impl.clear()
+            else:
+                self._available_impl.append(ZipExtFile)
+        self.__init_attributes_from_info(zip_info)
         self._parent: DrbNode = parent
         self._children: List[DrbNode] = None
         self._path = None
 
-    @property
-    def parent(self) -> Optional[DrbNode]:
-        return self._parent
-
-    @property
-    def path(self) -> ParsedPath:
-        if self._path is None:
-            self._path = self.parent.path / self.name
-        return self._path
+    def __setitem__(self, key, value):
+        raise NotImplementedError
 
-    @property
-    def name(self) -> str:
-        if self._name is None:
-            if self._zip_info.filename.endswith('/'):
-                self._name = self._zip_info.filename[:-1]
-            else:
-                self._name = self._zip_info.filename
-            if '/' in self._name:
-                self._name = self._name[self._name.rindex('/') + 1:]
-        return self._name
-
-    @property
-    def namespace_uri(self) -> Optional[str]:
-        return None
-
-    @property
-    def value(self) -> Optional[Any]:
-        return None
+    def __delitem__(self, key):
+        raise NotImplementedError
 
-    @property
-    def attributes(self) -> Dict[Tuple[str, str], Any]:
-        if self._attributes is None:
-            self._attributes = {}
-            name_attribute = DrbZipAttributeNames.DIRECTORY.value
-            self._attributes[name_attribute, None] = self._zip_info.is_dir()
-
-            name_attribute = DrbZipAttributeNames.SIZE.value
-            self._attributes[name_attribute, None] = self._zip_info.file_size
-
-            name_attribute = DrbZipAttributeNames.RATIO.value
-            if self._zip_info.compress_size > 0:
-                self._attributes[name_attribute, None] = \
-                    self._zip_info.file_size / self._zip_info.compress_size
+    def __init_attributes_from_info(self, info: ZipInfo):
+        if info is not None:
+            self @= (DrbZipAttributeNames.DIRECTORY.value, info.is_dir())
+            self @= DrbZipAttributeNames.SIZE.value, info.file_size
+            if info.compress_size > 0:
+                ratio = info.file_size / info.compress_size
             else:
-                self._attributes[name_attribute, None] = 0
-            name_attribute = DrbZipAttributeNames.PACKED.value
-            self._attributes[name_attribute, None] = \
-                self._zip_info.compress_size
-        return self._attributes
-
-    def get_attribute(self, name: str, namespace_uri: str = None) -> Any:
-        key = (name, namespace_uri)
-        if key in self.attributes.keys():
-            return self.attributes[key]
-        raise DrbException(f'Attribute not found name: {name}, '
-                           f'namespace: {namespace_uri}')
+                ratio = 0
+            self @= (DrbZipAttributeNames.RATIO.value, ratio)
+            self @= (DrbZipAttributeNames.PACKED.value, info.compress_size)
+
+    @staticmethod
+    def __retrieve_name(zip_info: ZipInfo) -> str:
+        if zip_info.filename.endswith('/'):
+            name = zip_info.filename[:-1]
+        else:
+            name = zip_info.filename
+        if '/' in name:
+            name = name[name.rindex('/') + 1:]
+        return name
 
     def get_file_list(self):
         return self.parent.get_file_list()
 
     def _is_a_child(self, filename):
         if not filename.startswith(self._zip_info.filename):
             return False
@@ -127,37 +101,29 @@
 
         # Either the name do not contains sep either only one a last position
         return '/' not in filename or filename.index('/') == (
                 len(filename) - 1)
 
     @property
     @resolve_children
+    @deprecated(version="1.2.0", reason="drb core deprecation since 2.1.0")
     def children(self) -> List[DrbNode]:
         if self._children is None:
             self._children = [DrbZipNode(self, entry) for entry in
                               self.get_file_list()
                               if self._is_a_child(entry.filename)]
             self._children = sorted(self._children,
                                     key=lambda entry_cmp: entry_cmp.name)
 
         return self._children
 
-    def has_impl(self, impl: type) -> bool:
-        if issubclass(ZipExtFile, impl):
-            return not self.get_attribute(
-                DrbZipAttributeNames.DIRECTORY.value, None)
-
     def get_impl(self, impl: type, **kwargs) -> Any:
         if self.has_impl(impl):
             return self.parent.open_entry(self._zip_info)
-        raise DrbNotImplementationException(f'no {impl} '
-                                            f'implementation found')
-
-    def close(self):
-        pass
+        raise DrbNotImplementationException(f'no {impl} implementation found')
 
     def open_entry(self, zip_info: ZipInfo):
         # open the entry on zip file to return ZipExtFile
         # we back to the first node_file to open is
         return self.parent.open_entry(zip_info)
 
 
@@ -204,24 +170,14 @@
 
         Returns:
             str: the base node name
         """
         return self.base_node.name
 
     @property
-    def namespace_uri(self) -> Optional[str]:
-        """
-        Return the namespace uri of the base node.
-
-        Returns:
-            str: the base node namespace
-        """
-        return self.base_node.namespace_uri
-
-    @property
     def value(self) -> Optional[Any]:
         """
         Return the value of the base node.
 
         Returns:
             Any: the value
         """
@@ -267,15 +223,20 @@
                                           f' {self.name} ') from e
         return self._zip_file
 
     def has_impl(self, impl: type) -> bool:
         return self.base_node.has_impl(impl)
 
     def get_impl(self, impl: type, **kwargs) -> Any:
-        return self.base_node.get_impl(impl)
+        if self.base_node.has_impl(impl):
+            return self.base_node.get_impl(impl)
+        raise DrbNotImplementationException
+
+    def impl_capabilities(self) -> List[type]:
+        return self.base_node.impl_capabilities()
 
     def close(self):
         if self._zip_file_source is not None:
             self._zip_file_source.close()
         if self._zip_file is not None:
             self._zip_file.close()
         self.base_node.close()
```

### Comparing `drb-driver-zip-1.1.0/drb_driver_zip.egg-info/PKG-INFO` & `drb-driver-zip-1.2.0/drb_driver_zip.egg-info/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 Metadata-Version: 2.1
 Name: drb-driver-zip
-Version: 1.1.0
-Summary: DRB Zip driver
+Version: 1.2.0
+Summary: DRB driver Zip
 Home-page: https://gitlab.com/drb-python/impl/zip
 Author: GAEL Systems
 Author-email: drb-python@gael.fr
-License: UNKNOWN
+License: LGPLv3
 Project-URL: Documentation, https://drb-python.gitlab.io/impl/zip
 Project-URL: Source, https://gitlab.com/drb-python/impl/zip
-Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3.8
-Classifier: License :: OSI Approved :: Apache Software License
+Classifier: License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
+License-File: LICENCE.txt
 
 # ZipNode Driver
 This drb-driver-zip module implements access to zip containers with DRB data model. It is able to navigates among the zip contents.
 
 ## Zip Factory and Zip Node
 The module implements the basic factory model defined in DRB in its node resolver. Based on the python entry point mechanism, this module can be dynamically imported into applications.
 
@@ -34,9 +34,7 @@
 
 ## Using this module
 To include this module into your project, the `drb-driver-zip` module shall be referenced into `requirements.txt` file, or the following pip line can be run:
 
 ```commandline
 pip install drb-driver-zip
 ```
-
-
```

### Comparing `drb-driver-zip-1.1.0/versioneer.py` & `drb-driver-zip-1.2.0/versioneer.py`

 * *Files identical despite different names*

