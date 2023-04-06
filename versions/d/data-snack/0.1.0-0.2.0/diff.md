# Comparing `tmp/data_snack-0.1.0.tar.gz` & `tmp/data_snack-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "data_snack-0.1.0.tar", last modified: Thu Jan 26 22:48:08 2023, max compression
+gzip compressed data, was "data_snack-0.2.0.tar", last modified: Thu Apr  6 13:17:22 2023, max compression
```

## Comparing `data_snack-0.1.0.tar` & `data_snack-0.2.0.tar`

### file list

```diff
@@ -1,43 +1,43 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 22:48:08.828505 data_snack-0.1.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1072 2023-01-26 22:47:52.000000 data_snack-0.1.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       62 2023-01-26 22:47:52.000000 data_snack-0.1.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     5365 2023-01-26 22:48:08.828505 data_snack-0.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     4799 2023-01-26 22:47:52.000000 data_snack-0.1.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      160 2023-01-26 22:47:52.000000 data_snack-0.1.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-01-26 22:47:52.000000 data_snack-0.1.0/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)      694 2023-01-26 22:48:08.828505 data_snack-0.1.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      661 2023-01-26 22:47:52.000000 data_snack-0.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 22:48:08.820505 data_snack-0.1.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 22:48:08.824505 data_snack-0.1.0/src/data_snack/
--rw-r--r--   0 runner    (1001) docker     (123)      104 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 22:48:08.824505 data_snack-0.1.0/src/data_snack/connections/
--rw-r--r--   0 runner    (1001) docker     (123)       29 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/connections/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2121 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/connections/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1048 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/connections/memcached.py
--rw-r--r--   0 runner    (1001) docker     (123)     1008 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/connections/redis.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 22:48:08.824505 data_snack-0.1.0/src/data_snack/entities/
--rw-r--r--   0 runner    (1001) docker     (123)       64 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/entities/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      983 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/entities/entity.py
--rw-r--r--   0 runner    (1001) docker     (123)      926 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/entities/entity_meta.py
--rw-r--r--   0 runner    (1001) docker     (123)      147 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/entities/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)      314 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/entities/registry.py
--rw-r--r--   0 runner    (1001) docker     (123)      752 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/entities/schema.py
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/exceptions.py
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/key_factory.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 22:48:08.824505 data_snack-0.1.0/src/data_snack/serializers/
--rw-r--r--   0 runner    (1001) docker     (123)       72 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/serializers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      520 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/serializers/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1198 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/serializers/dataclass.py
--rw-r--r--   0 runner    (1001) docker     (123)     6220 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/snack.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 22:48:08.824505 data_snack-0.1.0/src/data_snack/wrap/
--rw-r--r--   0 runner    (1001) docker     (123)      112 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/wrap/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/wrap/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     1599 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/wrap/data_frame.py
--rw-r--r--   0 runner    (1001) docker     (123)     1341 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/wrap/entity.py
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-01-26 22:47:52.000000 data_snack-0.1.0/src/data_snack/wrap/exceptions.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 22:48:08.824505 data_snack-0.1.0/src/data_snack.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5365 2023-01-26 22:48:08.000000 data_snack-0.1.0/src/data_snack.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1018 2023-01-26 22:48:08.000000 data_snack-0.1.0/src/data_snack.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 22:48:08.000000 data_snack-0.1.0/src/data_snack.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 22:48:08.000000 data_snack-0.1.0/src/data_snack.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-01-26 22:48:08.000000 data_snack-0.1.0/src/data_snack.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:17:22.422586 data_snack-0.2.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1072 2023-04-06 13:17:09.000000 data_snack-0.2.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       62 2023-04-06 13:17:09.000000 data_snack-0.2.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     5365 2023-04-06 13:17:22.422586 data_snack-0.2.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     4799 2023-04-06 13:17:09.000000 data_snack-0.2.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-04-06 13:17:09.000000 data_snack-0.2.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-06 13:17:09.000000 data_snack-0.2.0/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      694 2023-04-06 13:17:22.422586 data_snack-0.2.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      661 2023-04-06 13:17:09.000000 data_snack-0.2.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:17:22.410586 data_snack-0.2.0/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:17:22.414586 data_snack-0.2.0/src/data_snack/
+-rw-r--r--   0 runner    (1001) docker     (123)      104 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:17:22.418586 data_snack-0.2.0/src/data_snack/connections/
+-rw-r--r--   0 runner    (1001) docker     (123)       29 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/connections/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2278 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/connections/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1078 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/connections/memcached.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/connections/redis.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:17:22.418586 data_snack-0.2.0/src/data_snack/entities/
+-rw-r--r--   0 runner    (1001) docker     (123)       64 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/entities/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1029 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/entities/entity.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1034 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/entities/entity_meta.py
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/entities/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      314 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/entities/registry.py
+-rw-r--r--   0 runner    (1001) docker     (123)      758 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/entities/schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/exceptions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      403 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/key_factory.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:17:22.418586 data_snack-0.2.0/src/data_snack/serializers/
+-rw-r--r--   0 runner    (1001) docker     (123)       72 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/serializers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      570 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/serializers/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/serializers/dataclass.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6091 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/snack.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:17:22.422586 data_snack-0.2.0/src/data_snack/wrap/
+-rw-r--r--   0 runner    (1001) docker     (123)      112 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/wrap/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2130 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/wrap/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1599 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/wrap/data_frame.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1341 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/wrap/entity.py
+-rw-r--r--   0 runner    (1001) docker     (123)       52 2023-04-06 13:17:09.000000 data_snack-0.2.0/src/data_snack/wrap/exceptions.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:17:22.418586 data_snack-0.2.0/src/data_snack.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5365 2023-04-06 13:17:22.000000 data_snack-0.2.0/src/data_snack.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1018 2023-04-06 13:17:22.000000 data_snack-0.2.0/src/data_snack.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:17:22.000000 data_snack-0.2.0/src/data_snack.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-04-06 13:17:22.000000 data_snack-0.2.0/src/data_snack.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 13:17:22.000000 data_snack-0.2.0/src/data_snack.egg-info/top_level.txt
```

### Comparing `data_snack-0.1.0/LICENSE` & `data_snack-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `data_snack-0.1.0/PKG-INFO` & `data_snack-0.2.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: data_snack
-Version: 0.1.0
+Version: 0.2.0
 Home-page: https://github.com/webinterpret-ds/data-snack
 Author: webinterpret-datascience
 Author-email: data-science@webinterpret.com
 Project-URL: Bug Tracker, https://github.com/webinterpret-ds/data-snack/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Classifier: Operating System :: OS Independent
```

### Comparing `data_snack-0.1.0/README.md` & `data_snack-0.2.0/README.md`

 * *Files identical despite different names*

### Comparing `data_snack-0.1.0/setup.cfg` & `data_snack-0.2.0/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = data-snack
-version = 0.1.0
+version = 0.2.0
 author = webinterpret-datascience
 author_email = data-science@webinterpret.com
 description = 
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/webinterpret-ds/data-snack
 project_urls =
```

### Comparing `data_snack-0.1.0/setup.py` & `data_snack-0.2.0/setup.py`

 * *Files identical despite different names*

### Comparing `data_snack-0.1.0/src/data_snack/connections/base.py` & `data_snack-0.2.0/src/data_snack/connections/base.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,22 +1,23 @@
-from typing import Any, Dict, List, Protocol, Text, Union
+from typing import Any, Dict, List, Protocol, Text, Union, Optional
 
 
 class Connection(Protocol):
     """
     An interface used for by `Snack` to access db.
     If you want to create a custom connection to a db for your choosing,
     create a new class that follows this protocol.
     """
 
     connection: Any
 
-    def get(self, key: Text) -> bytes:
+    def get(self, key: Text) -> Optional[bytes]:
         """
         Reads data from db based on provided key.
+        If key was missing in db, it returns None.
 
         :param key: unique data identifier
         :return: retrieved data
         """
         ...
 
     def set(self, key: Text, value: Union[Text, bytes], expire: int = 0) -> bool:
@@ -35,17 +36,18 @@
         Deletes value for provided key.
 
         :param key: unique data identifier
         :return: True if data were deleted
         """
         ...
 
-    def get_many(self, keys: List[Text]) -> Dict[Text, bytes]:
+    def get_many(self, keys: List[Text]) -> Dict[Text, Optional[bytes]]:
         """
         Reads multiple values from db based on provided list of keys.
+        If a certain key was missing in db, it returns None for that value.
 
         :param keys: a list of keys
         :return: a dictionary with retrieved values assigned to each key
         """
         ...
 
     def set_many(self, values: Dict[Text, Union[Text, bytes]]) -> List[Text]:
```

### Comparing `data_snack-0.1.0/src/data_snack/connections/memcached.py` & `data_snack-0.2.0/src/data_snack/connections/memcached.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,27 +1,27 @@
 from dataclasses import dataclass
-from typing import Dict, List, Text
+from typing import Dict, List, Text, Optional
 
 from .base import Connection
 
 
 @dataclass
 class MemcachedConnection(Connection):
     connection: "Client"
 
-    def get(self, key: Text) -> bytes:
+    def get(self, key: Text) -> Optional[bytes]:
         return self.connection.get(key)
 
     def set(self, key: Text, value: Text, expire: int = 0) -> bool:
         return self.connection.set(key, value, expire=expire)
 
     def delete(self, key: Text) -> bool:
         return self.connection.delete(key, noreply=False)
 
-    def get_many(self, keys: List[Text]) -> Dict[Text, bytes]:
+    def get_many(self, keys: List[Text]) -> Dict[Text, Optional[bytes]]:
         return self.connection.get_many(keys)
 
     def set_many(self, values: Dict[Text, Text]) -> List[Text]:
         failed_keys = self.connection.set_many(values)
         return list(set(values.keys()) - set(failed_keys))
 
     def delete_many(
```

### Comparing `data_snack-0.1.0/src/data_snack/connections/redis.py` & `data_snack-0.2.0/src/data_snack/connections/redis.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,29 +1,29 @@
 from dataclasses import dataclass
-from typing import Dict, List, Text
+from typing import Dict, List, Text, Optional
 
 from .base import Connection
 
 
 @dataclass
 class RedisConnection(Connection):
     connection: "Redis"
 
-    def get(self, key: Text) -> bytes:
+    def get(self, key: Text) -> Optional[bytes]:
         return self.connection.get(key)
 
     def set(self, key: Text, value: Text, expire: int = 0) -> bool:
         ex = expire if expire > 0 else None
         return self.connection.set(key, value, ex=ex)
 
     def delete(self, key: Text) -> bool:
         n_deleted = self.connection.delete(key)
         return n_deleted == 1
 
-    def get_many(self, keys: List[Text]) -> Dict[Text, bytes]:
+    def get_many(self, keys: List[Text]) -> Dict[Text, Optional[bytes]]:
         return dict(zip(keys, self.connection.mget(keys)))
 
     def set_many(self, values: Dict[Text, Text]) -> List[Text]:
         return self.connection.mset(values)
 
     def delete_many(self, keys: List[Text]) -> bool:
         n_deleted = self.connection.delete(*keys)
```

### Comparing `data_snack-0.1.0/src/data_snack/entities/entity.py` & `data_snack-0.2.0/src/data_snack/entities/entity.py`

 * *Files 12% similar despite different names*

```diff
@@ -18,15 +18,19 @@
     def get_all_fields(cls) -> List[str]:
         """Gets all Entity fields."""
         return list(get_type_hints(cls))
 
     @classmethod
     def get_fields(cls) -> List[str]:
         """Gets Entity fields if not excluded."""
-        return [field for field in cls.get_all_fields() if field not in cls.get_excluded_fields()]
+        return [
+            field
+            for field in cls.get_all_fields()
+            if field not in cls.get_excluded_fields()
+        ]
 
     @classmethod
     def get_excluded_fields(cls) -> List[str]:
         """Gets Entity excluded keys only."""
         return cls.Meta.excluded_fields
 
     @classmethod
```

### Comparing `data_snack-0.1.0/src/data_snack/entities/entity_meta.py` & `data_snack-0.2.0/src/data_snack/entities/entity_meta.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,20 +1,30 @@
 from abc import ABCMeta, ABC
 
-from .exceptions import MetaFieldsException, MetaEmptyKeysException, NonExistingMetaError
+from .exceptions import (
+    MetaFieldsException,
+    MetaEmptyKeysException,
+    NonExistingMetaError,
+)
 
 
 class EntityMetaClass(ABCMeta):
 
     meta_fields = ["keys", "excluded_fields"]
 
     def __new__(mcs, name, bases, dct):
         entity_class = super().__new__(mcs, name, bases, dct)
         # TODO: consider encapsulation of each validation rule to function to make this class cleaner.
         if "Meta" not in dir(entity_class):
-            raise NonExistingMetaError(f"Private class `Meta not defined for {entity_class.__name__}.")
-        if bases != (ABC, ):
-            if missing_fields := [field for field in mcs.meta_fields if field not in dir(entity_class.Meta)]:
+            raise NonExistingMetaError(
+                f"Private class `Meta not defined for {entity_class.__name__}."
+            )
+        if bases != (ABC,):
+            if missing_fields := [
+                field
+                for field in mcs.meta_fields
+                if field not in dir(entity_class.Meta)
+            ]:
                 raise MetaFieldsException(f"Missing Meta fields: {missing_fields}.")
             if not entity_class.Meta.keys:
                 raise MetaEmptyKeysException("Meta keys can not be empty.")
         return entity_class
```

### Comparing `data_snack-0.1.0/src/data_snack/entities/schema.py` & `data_snack-0.2.0/src/data_snack/entities/schema.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,17 @@
 
 from data_snack.entities import Entity
 
 
 EntitySchemaGetter = Callable[[Type[Entity], bool], Dict[str, Any]]
 
 
-def get_entity_schema(entity_type: Type[Entity], exclude_fields: bool = False) -> Dict[str, Any]:
+def get_entity_schema(
+    entity_type: Type[Entity], exclude_fields: bool = False
+) -> Dict[str, Any]:
     """
     Gets `Entity` schema, i.e. {field: data type} mapping. Allows excluding Entities excluded fields.
     :param entity_type: Entity definition (class)
     :param exclude_fields: excludes Entity excluded fields if True
     :return: Entity schema
     """
     schema = get_type_hints(entity_type)
```

### Comparing `data_snack-0.1.0/src/data_snack/serializers/dataclass.py` & `data_snack-0.2.0/src/data_snack/serializers/dataclass.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,33 +1,38 @@
 import ast
 import zlib
 from dataclasses import dataclass
-from typing import List, Union, get_type_hints
+from typing import List, Union, get_type_hints, Optional
 
 import pandas as pd
 
 from data_snack.entities import Entity
 from data_snack.serializers.base import Serializer
 
 
 @dataclass
 class DataclassSerializer(Serializer):
     def __post_init__(self):
         self.entity_fields = list(get_type_hints(self.entity_type).keys())
 
-    def _serialize(self, entity: Entity) -> bytes:
+    def _serialize(self, entity: Optional[Entity]) -> Optional[bytes]:
         entity_fields = entity.__dict__
-        values = [entity_fields[field] if pd.notnull(entity_fields[field]) else None for field in self.entity_fields]
+        values = [
+            entity_fields[field] if pd.notnull(entity_fields[field]) else None
+            for field in self.entity_fields
+        ]
         return zlib.compress(str(values).encode())
 
     def serialize(
         self, entity: Union[Entity, List[Entity]], many: bool = False
     ) -> Union[bytes, List[bytes]]:
         return [self._serialize(e) for e in entity] if many else self._serialize(entity)
 
-    def _deserialize(self, data: bytes) -> Entity:
+    def _deserialize(self, data: Optional[bytes]) -> Optional[Entity]:
+        if not data:
+            return
         return self.entity_type(*ast.literal_eval(zlib.decompress(data).decode()))
 
     def deserialize(
-        self, data: Union[bytes, List[bytes]], many: bool = False
-    ) -> Union[Entity, List[Entity]]:
+        self, data: Union[Optional[bytes], List[Optional[bytes]]], many: bool = False
+    ) -> Union[Optional[Entity], List[Optional[Entity]]]:
         return [self._deserialize(d) for d in data] if many else self._deserialize(data)
```

### Comparing `data_snack-0.1.0/src/data_snack/snack.py` & `data_snack-0.2.0/src/data_snack/snack.py`

 * *Files 5% similar despite different names*

```diff
@@ -55,15 +55,16 @@
         return wrap_type(self, entity_type)
 
     def _get_serializer(self, type_name: Text) -> Serializer:
         return self.registry[type_name].serializer
 
     def _build_record_key(self, type_name: Text, entity: Entity) -> Text:
         key_values = [
-            getattr(entity, key) for key in self.registry[type_name].entity_type.get_keys()
+            getattr(entity, key)
+            for key in self.registry[type_name].entity_type.get_keys()
         ]
         return self.key_factory(type_name, *key_values)
 
     def set(self, entity: Entity, expire: int = 0) -> Optional[Text]:
         """
         Sets provided `Entity` object in db.
         Notice the entity stored in the db will be overwritten,
@@ -75,29 +76,27 @@
         """
         type_name = entity.__class__.__name__
         key = self._build_record_key(type_name, entity)
         record = self._get_serializer(type_name).serialize(entity)
         if self.connection.set(key, record, expire):
             return key
 
-    def get(self, cls: Type[Entity], key_values: List[Any]) -> Entity:
+    def get(self, cls: Type[Entity], key_values: List[Any]) -> Optional[Entity]:
         """
         Gets ane entity of `Entity` type from db based on provided key values.
         Notice, key is represented as a list of strings, since one Entity can have multiple key fields.
 
         :param cls: `Entity` type
         :param key_values: a list of key values representing the entity
         :return: a retrieved Entity object
         """
         type_name = cls.__name__
         _key = self.key_factory(type_name, *key_values)
-        if value := self.connection.get(_key):
-            return self._get_serializer(type_name).deserialize(value)
-        else:
-            raise KeyError(f"Key {_key} not found.")
+        value = self.connection.get(_key)
+        return self._get_serializer(type_name).deserialize(value)
 
     def delete(self, cls: Type[Entity], key_values: List[Any]) -> bool:
         """
         Deletes one entity of `Entity` type from db based on provided key values.
         Notice, key is represented as a list of strings, since one Entity can have multiple key fields.
 
         :param cls: `Entity` type
@@ -106,27 +105,25 @@
         """
         type_name = cls.__name__
         _key = self.key_factory(type_name, *key_values)
         return self.connection.delete(_key)
 
     def get_many(
         self, cls: Type[Entity], keys_values: List[List[Any]]
-    ) -> List[Entity]:
+    ) -> List[Optional[Entity]]:
         """
         Gets list of `Entity` objects from db based on provided list of keys.
 
         :param cls: `Entity` type
         :param keys_values: list of keys, each list defines a set key values for one Entity object
         :return: a list of retrieved Entity objects
         """
         type_name = cls.__name__
         _keys = [self.key_factory(type_name, *key_values) for key_values in keys_values]
         records = list(self.connection.get_many(_keys).values())
-        if not records:
-            raise KeyError(f"None of requested keys found.")
         return self._get_serializer(type_name).deserialize(records, many=True)
 
     def set_many(self, entities: List[Entity]) -> List[Text]:
         """
         Saves multiple `Entity` objects in db.
 
         :param entities: a list of Entity objects
```

### Comparing `data_snack-0.1.0/src/data_snack/wrap/base.py` & `data_snack-0.2.0/src/data_snack/wrap/base.py`

 * *Files identical despite different names*

### Comparing `data_snack-0.1.0/src/data_snack/wrap/data_frame.py` & `data_snack-0.2.0/src/data_snack/wrap/data_frame.py`

 * *Files identical despite different names*

### Comparing `data_snack-0.1.0/src/data_snack/wrap/entity.py` & `data_snack-0.2.0/src/data_snack/wrap/entity.py`

 * *Files identical despite different names*

### Comparing `data_snack-0.1.0/src/data_snack.egg-info/PKG-INFO` & `data_snack-0.2.0/src/data_snack.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: data-snack
-Version: 0.1.0
+Version: 0.2.0
 Home-page: https://github.com/webinterpret-ds/data-snack
 Author: webinterpret-datascience
 Author-email: data-science@webinterpret.com
 Project-URL: Bug Tracker, https://github.com/webinterpret-ds/data-snack/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Classifier: Operating System :: OS Independent
```

### Comparing `data_snack-0.1.0/src/data_snack.egg-info/SOURCES.txt` & `data_snack-0.2.0/src/data_snack.egg-info/SOURCES.txt`

 * *Files identical despite different names*

