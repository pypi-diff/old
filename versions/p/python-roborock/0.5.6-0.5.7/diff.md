# Comparing `tmp/python_roborock-0.5.6.tar.gz` & `tmp/python_roborock-0.5.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "python_roborock-0.5.6.tar", max compression
+gzip compressed data, was "python_roborock-0.5.7.tar", max compression
```

## Comparing `python_roborock-0.5.6.tar` & `python_roborock-0.5.7.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0    35149 2023-04-06 21:27:56.651006 python_roborock-0.5.6/LICENSE
--rw-r--r--   0        0        0     2221 2023-04-06 21:27:56.651006 python_roborock-0.5.6/README.md
--rw-r--r--   0        0        0     1175 2023-04-06 21:27:57.451013 python_roborock-0.5.6/pyproject.toml
--rw-r--r--   0        0        0      300 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/__init__.py
--rw-r--r--   0        0        0    17099 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/api.py
--rw-r--r--   0        0        0     3957 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/cli.py
--rw-r--r--   0        0        0     8276 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/cloud_api.py
--rw-r--r--   0        0        0     3704 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/code_mappings.py
--rw-r--r--   0        0        0     8866 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/containers.py
--rw-r--r--   0        0        0     1022 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/exceptions.py
--rw-r--r--   0        0        0     7030 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/local_api.py
--rw-r--r--   0        0        0     1194 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/offline/offline.py
--rw-r--r--   0        0        0     6030 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/roborock_message.py
--rw-r--r--   0        0        0      644 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/roborock_queue.py
--rw-r--r--   0        0        0    12471 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/typing.py
--rw-r--r--   0        0        0      809 2023-04-06 21:27:56.651006 python_roborock-0.5.6/roborock/util.py
--rw-r--r--   0        0        0     3348 1970-01-01 00:00:00.000000 python_roborock-0.5.6/PKG-INFO
+-rw-r--r--   0        0        0    35149 2023-04-07 13:52:55.275350 python_roborock-0.5.7/LICENSE
+-rw-r--r--   0        0        0     2221 2023-04-07 13:52:55.275350 python_roborock-0.5.7/README.md
+-rw-r--r--   0        0        0     1175 2023-04-07 13:52:55.999358 python_roborock-0.5.7/pyproject.toml
+-rw-r--r--   0        0        0      300 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/__init__.py
+-rw-r--r--   0        0        0    17099 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/api.py
+-rw-r--r--   0        0        0     3957 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/cli.py
+-rw-r--r--   0        0        0     8276 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/cloud_api.py
+-rw-r--r--   0        0        0     3704 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/code_mappings.py
+-rw-r--r--   0        0        0     9190 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/containers.py
+-rw-r--r--   0        0        0     1022 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/exceptions.py
+-rw-r--r--   0        0        0     7030 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/local_api.py
+-rw-r--r--   0        0        0     1194 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/offline/offline.py
+-rw-r--r--   0        0        0     6030 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/roborock_message.py
+-rw-r--r--   0        0        0      644 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/roborock_queue.py
+-rw-r--r--   0        0        0    12471 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/typing.py
+-rw-r--r--   0        0        0      809 2023-04-07 13:52:55.275350 python_roborock-0.5.7/roborock/util.py
+-rw-r--r--   0        0        0     3348 1970-01-01 00:00:00.000000 python_roborock-0.5.7/PKG-INFO
```

### Comparing `python_roborock-0.5.6/LICENSE` & `python_roborock-0.5.7/LICENSE`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/README.md` & `python_roborock-0.5.7/README.md`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/pyproject.toml` & `python_roborock-0.5.7/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "python-roborock"
-version = "0.5.6"
+version = "0.5.7"
 description = "A package to control Roborock vacuums."
 authors = ["humbertogontijo <humbertogontijo@users.noreply.github.com>"]
 license = "GPL-3.0-only"
 readme = "README.md"
 repository = "https://github.com/humbertogontijo/python-roborock"
 classifiers = [
     "Development Status :: 5 - Production/Stable",
```

### Comparing `python_roborock-0.5.6/roborock/api.py` & `python_roborock-0.5.7/roborock/api.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/cli.py` & `python_roborock-0.5.7/roborock/cli.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/cloud_api.py` & `python_roborock-0.5.7/roborock/cloud_api.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/code_mappings.py` & `python_roborock-0.5.7/roborock/code_mappings.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/containers.py` & `python_roborock-0.5.7/roborock/containers.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,39 +1,48 @@
+from __future__ import annotations
+
 import re
-from dataclasses import dataclass
+from dataclasses import dataclass, asdict
 from enum import Enum
 from typing import Any, Optional
 
 from dacite import from_dict, Config
 
 from roborock.code_mappings import RoborockDockWashTowelModeCode, RoborockDockTypeCode, RoborockMopIntensityCode, \
     RoborockStateCode
 from .code_mappings import RoborockMopModeCode, RoborockDockErrorCode, \
     RoborockErrorCode, RoborockDockDustCollectionModeCode, RoborockFanPowerCode
 
 
-def to_snake(s):
+def camelize(s: str):
+    first, *others = s.split('_')
+    return ''.join([first.lower(), *map(str.title, others)])
+
+
+def decamelize(s: str):
     return re.sub('([A-Z]+)', '_\\1', s).lower()
 
 
-def decamelize(d):
+def decamelize_obj(d: dict | list):
     if isinstance(d, list):
-        return [decamelize(i) if isinstance(i, (dict, list)) else i for i in d]
-    return {to_snake(a): decamelize(b) if isinstance(b, (dict, list)) else b for a, b in d.items()}
+        return [decamelize_obj(i) if isinstance(i, (dict, list)) else i for i in d]
+    return {decamelize(a): decamelize_obj(b) if isinstance(b, (dict, list)) else b for a, b in d.items()}
 
 
 @dataclass
 class RoborockBase:
 
     @classmethod
     def from_dict(cls, data: dict[str, any]):
-        return from_dict(cls, decamelize(data), config=Config(cast=[Enum]))
+        return from_dict(cls, decamelize_obj(data), config=Config(cast=[Enum]))
 
     def as_dict(self):
-        return self.__dict__
+        return asdict(self, dict_factory=lambda _fields: {
+            camelize(key): value for (key, value) in _fields if value is not None
+        })
 
 
 @dataclass
 class Reference(RoborockBase):
     r: Optional[str] = None
     a: Optional[str] = None
     m: Optional[str] = None
```

### Comparing `python_roborock-0.5.6/roborock/exceptions.py` & `python_roborock-0.5.7/roborock/exceptions.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/local_api.py` & `python_roborock-0.5.7/roborock/local_api.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/offline/offline.py` & `python_roborock-0.5.7/roborock/offline/offline.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/roborock_message.py` & `python_roborock-0.5.7/roborock/roborock_message.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/roborock_queue.py` & `python_roborock-0.5.7/roborock/roborock_queue.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/typing.py` & `python_roborock-0.5.7/roborock/typing.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/roborock/util.py` & `python_roborock-0.5.7/roborock/util.py`

 * *Files identical despite different names*

### Comparing `python_roborock-0.5.6/PKG-INFO` & `python_roborock-0.5.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: python-roborock
-Version: 0.5.6
+Version: 0.5.7
 Summary: A package to control Roborock vacuums.
 Home-page: https://github.com/humbertogontijo/python-roborock
 License: GPL-3.0-only
 Author: humbertogontijo
 Author-email: humbertogontijo@users.noreply.github.com
 Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 5 - Production/Stable
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: python-roborock Version: 0.5.6 Summary: A package
+Metadata-Version: 2.1 Name: python-roborock Version: 0.5.7 Summary: A package
 to control Roborock vacuums. Home-page: https://github.com/humbertogontijo/
 python-roborock License: GPL-3.0-only Author: humbertogontijo Author-email:
 humbertogontijo@users.noreply.github.com Requires-Python: >=3.9,<4.0
 Classifier: Development Status :: 5 - Production/Stable Classifier: Intended
 Audience :: Developers Classifier: License :: OSI Approved :: GNU General
 Public License v3 (GPLv3) Classifier: Natural Language :: English Classifier:
 Operating System :: OS Independent Classifier: Programming Language :: Python
```

