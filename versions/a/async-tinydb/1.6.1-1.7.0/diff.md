# Comparing `tmp/async_tinydb-1.6.1.tar.gz` & `tmp/async_tinydb-1.7.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "async_tinydb-1.6.1.tar", max compression
+gzip compressed data, was "async_tinydb-1.7.0.tar", max compression
```

## Comparing `async_tinydb-1.6.1.tar` & `async_tinydb-1.7.0.tar`

### file list

```diff
@@ -1,18 +1,18 @@
--rw-r--r--   0        0        0     1061 2022-10-12 02:56:42.755698 async_tinydb-1.6.1/LICENSE
--rw-r--r--   0        0        0     8472 2022-11-04 05:55:14.893700 async_tinydb-1.6.1/README.md
--rw-r--r--   0        0        0     1289 2022-10-18 07:49:00.364331 async_tinydb-1.6.1/asynctinydb/__init__.py
--rw-r--r--   0        0        0    12380 2023-03-11 13:16:59.408381 async_tinydb-1.6.1/asynctinydb/database.py
--rw-r--r--   0        0        0     5729 2023-03-11 13:22:01.053489 async_tinydb-1.6.1/asynctinydb/indices.py
--rw-r--r--   0        0        0     4768 2022-10-18 15:04:59.497829 async_tinydb-1.6.1/asynctinydb/middlewares.py
--rw-r--r--   0        0        0    15551 2023-03-11 13:15:31.712977 async_tinydb-1.6.1/asynctinydb/modifier.py
--rw-r--r--   0        0        0     1075 2022-10-18 15:04:45.020284 async_tinydb-1.6.1/asynctinydb/mypy_plugin.py
--rw-r--r--   0        0        0     1161 2022-10-18 15:04:38.632479 async_tinydb-1.6.1/asynctinydb/operations.py
--rw-r--r--   0        0        0        0 2022-09-14 10:01:02.219030 async_tinydb-1.6.1/asynctinydb/py.typed
--rw-r--r--   0        0        0    19857 2023-03-11 13:12:28.933144 async_tinydb-1.6.1/asynctinydb/queries.py
--rw-r--r--   0        0        0    13007 2023-03-11 13:14:26.703362 async_tinydb-1.6.1/asynctinydb/storages.py
--rw-r--r--   0        0        0    30881 2023-03-11 13:16:16.869870 async_tinydb-1.6.1/asynctinydb/table.py
--rw-r--r--   0        0        0       25 2022-10-21 09:26:01.913798 async_tinydb-1.6.1/asynctinydb/transaction.py
--rw-r--r--   0        0        0     4130 2023-03-11 13:21:05.697240 async_tinydb-1.6.1/asynctinydb/utils.py
--rw-r--r--   0        0        0       22 2023-04-03 12:55:36.905544 async_tinydb-1.6.1/asynctinydb/version.py
--rw-r--r--   0        0        0     3106 2023-04-03 12:55:43.723703 async_tinydb-1.6.1/pyproject.toml
--rw-r--r--   0        0        0    10314 1970-01-01 00:00:00.000000 async_tinydb-1.6.1/PKG-INFO
+-rw-r--r--   0        0        0     1061 2022-10-12 02:56:42.755698 async_tinydb-1.7.0/LICENSE
+-rw-r--r--   0        0        0     8472 2022-11-04 05:55:14.893700 async_tinydb-1.7.0/README.md
+-rw-r--r--   0        0        0     1289 2022-10-18 07:49:00.364331 async_tinydb-1.7.0/asynctinydb/__init__.py
+-rw-r--r--   0        0        0    12380 2023-03-11 13:16:59.408381 async_tinydb-1.7.0/asynctinydb/database.py
+-rw-r--r--   0        0        0     5729 2023-03-11 13:22:01.053489 async_tinydb-1.7.0/asynctinydb/indices.py
+-rw-r--r--   0        0        0     4768 2023-04-07 05:25:52.539017 async_tinydb-1.7.0/asynctinydb/middlewares.py
+-rw-r--r--   0        0        0    21179 2023-04-07 09:56:11.636984 async_tinydb-1.7.0/asynctinydb/modifier.py
+-rw-r--r--   0        0        0     1075 2022-10-18 15:04:45.020284 async_tinydb-1.7.0/asynctinydb/mypy_plugin.py
+-rw-r--r--   0        0        0     1161 2022-10-18 15:04:38.632479 async_tinydb-1.7.0/asynctinydb/operations.py
+-rw-r--r--   0        0        0        0 2022-09-14 10:01:02.219030 async_tinydb-1.7.0/asynctinydb/py.typed
+-rw-r--r--   0        0        0    19857 2023-03-11 13:12:28.933144 async_tinydb-1.7.0/asynctinydb/queries.py
+-rw-r--r--   0        0        0    13007 2023-04-07 08:34:22.740846 async_tinydb-1.7.0/asynctinydb/storages.py
+-rw-r--r--   0        0        0    30699 2023-04-07 10:12:57.560019 async_tinydb-1.7.0/asynctinydb/table.py
+-rw-r--r--   0        0        0       25 2022-10-21 09:26:01.913798 async_tinydb-1.7.0/asynctinydb/transaction.py
+-rw-r--r--   0        0        0     2903 2023-04-07 10:13:01.552064 async_tinydb-1.7.0/asynctinydb/utils.py
+-rw-r--r--   0        0        0       22 2023-04-07 10:12:19.155061 async_tinydb-1.7.0/asynctinydb/version.py
+-rw-r--r--   0        0        0     3216 2023-04-07 10:12:25.111540 async_tinydb-1.7.0/pyproject.toml
+-rw-r--r--   0        0        0    10410 1970-01-01 00:00:00.000000 async_tinydb-1.7.0/PKG-INFO
```

### Comparing `async_tinydb-1.6.1/LICENSE` & `async_tinydb-1.7.0/LICENSE`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/README.md` & `async_tinydb-1.7.0/README.md`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/asynctinydb/__init__.py` & `async_tinydb-1.7.0/asynctinydb/__init__.py`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/asynctinydb/database.py` & `async_tinydb-1.7.0/asynctinydb/database.py`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/asynctinydb/indices.py` & `async_tinydb-1.7.0/asynctinydb/indices.py`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/asynctinydb/middlewares.py` & `async_tinydb-1.7.0/asynctinydb/middlewares.py`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/asynctinydb/modifier.py` & `async_tinydb-1.7.0/asynctinydb/modifier.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,20 +1,23 @@
 """Modifier class for TinyDB."""
 
 from __future__ import annotations
-from typing import Any, Callable, TypeVar, overload
+import time
+from typing import Any, Callable, Mapping, Sequence, TypeVar, overload
 import datetime as dt
+import cachetools
 from warnings import warn
 from functools import partial
-from .storages import Storage, StorageWithWriteReadPrePostHooks
+from cachetools import Cache
 from vermils.asynctools import async_run
 from vermils.collections.fridge import FrozenDict
 from vermils.gadgets import sort_class
+from .storages import Storage, StorageWithWriteReadPrePostHooks
 from .database import TinyDB
-from .table import Table, IncreID, Document, BaseDocument
+from .table import BaseID, Table, IncreID, Document, BaseDocument
 
 
 T = TypeVar("T", bound=Table)
 S = TypeVar('S', bound=Storage)
 SWRPH = TypeVar("SWRPH", bound=StorageWithWriteReadPrePostHooks)
 
 
@@ -413,7 +416,174 @@
 
             if access:
                 @tab.on.read
                 def access_time(_: str, tab: Table, doc: BaseDocument):
                     doc[fields["access"]] = get_time()
 
             return tab
+
+    class Caching:
+        """
+        ## Bounded Caching
+
+        **WARNING: This is NOT CachingMiddleware, it will PURGE data in the database
+        that expires. 
+        If you want to cache your data for performance, use `CachingMiddleware` instead.**
+
+        ** Note modifiers in this class are still UNDER DEVELOPMENT, current implementation
+        is flawed and only works well if you access the data using `doc_id`. Conditional
+        searching/updating will mess up with the cache order, you may purge incorrect data.**
+
+        This class provides modifiers that turn TinyDB instances into cache system
+        with a bounded size.
+
+        You can choose algorithms such as `LRUCache`, `LFUCache`...
+        Or even implement your own.
+
+        """
+
+        @staticmethod
+        def _add_cache(
+                tab: Table | TinyDB,
+                cacheT: type[Cache],
+                maxsize: int,
+                getsizeof: Callable[[Any], float] | None,
+                **kw):
+
+            if isinstance(tab, TinyDB):
+                tab = tab.default_table
+            tab._cook
+            if tab.no_dbcache:
+                raise ValueError("Modifier relies on db-level cache")
+
+            def _cook(raw: Mapping[Any, Mapping]
+                      ) -> Cache[BaseID, BaseDocument]:
+                nonlocal tab
+                doc_cls = tab.document_class
+                id_cls = tab.document_id_class
+                cache = cacheT(
+                    maxsize=maxsize,
+                    getsizeof=getsizeof,
+                    **kw)
+                for rid, rdoc in raw.items():
+                    doc_id = id_cls(rid)
+                    doc = doc_cls(rdoc, doc_id)
+                    cache[doc_id] = doc
+                return cache
+
+            tab._cook = _cook  # type: ignore[method-assign]
+
+        @classmethod
+        def LRUCache(
+                cls,
+                tab: Table | TinyDB,
+                maxsize: int,
+                getsizeof: Callable[[Any], float] = None,
+        ) -> Table[BaseID, BaseDocument]:
+            """
+            ### LRUCache
+            Least Recently Used Cache
+            """
+            cls._add_cache(tab, cachetools.LRUCache, maxsize, getsizeof)
+            return tab
+
+        @classmethod
+        def LFUCache(
+                cls,
+                tab: Table | TinyDB,
+                maxsize: int,
+                getsizeof: Callable[[Any], float] = None,
+        ) -> Table[BaseID, BaseDocument]:
+            """
+            ### LFUCache
+            Least Frequently Used Cache
+            """
+            cls._add_cache(tab, cachetools.LFUCache, maxsize, getsizeof)
+            return tab
+
+        @classmethod
+        def RRCache(
+                cls,
+                tab: Table | TinyDB,
+                maxsize: int,
+                getsizeof: Callable[[Any], float] = None,
+                choice: Callable[[Sequence], Any] = None,
+        ) -> Table[BaseID, BaseDocument]:
+            """
+            ### RRCache
+            Random Replacement Cache
+            """
+            cls._add_cache(tab, cachetools.RRCache, maxsize, getsizeof,
+                           choice=choice)
+            return tab
+
+        @classmethod
+        def TTLCache(
+                cls,
+                tab: Table | TinyDB,
+                maxsize: int,
+                ttl: float,
+                getsizeof: Callable[[Any], float] = None,
+                timer: Callable[[], float] = time.monotonic,
+        ) -> Table[BaseID, BaseDocument]:
+            """
+            ### TTLCache
+            Time To Live Cache
+            """
+            cls._add_cache(tab, cachetools.TTLCache, maxsize, getsizeof,
+                           ttl=ttl, timer=timer)
+            return tab
+
+        @classmethod
+        def TLRUCache(
+                cls,
+                tab: Table | TinyDB,
+                maxsize: int,
+                ttu: Callable[[Any, Any, float], float],
+                getsizeof: Callable[[Any], float] = None,
+                timer: Callable[[], float] = time.monotonic,
+        ) -> Table[BaseID, BaseDocument]:
+            """
+            ### TLRUCache
+            Time To Live Least Recently Used Cache
+
+            ```
+            from datetime import datetime, timedelta
+
+            def my_ttu(_key, value, now):
+                # assume value.ttl contains the item's time-to-live in hours
+                return now + timedelta(hours=value.ttl)
+
+            cache = TLRUCache(maxsize=10, ttu=my_ttu, timer=datetime.now)
+            ```
+            """
+            cls._add_cache(tab, cachetools.TLRUCache, maxsize, getsizeof,
+                           ttu=ttu, timer=timer)
+            return tab
+
+        @classmethod
+        def FIFOCache(
+                cls,
+                tab: Table | TinyDB,
+                maxsize: int,
+                getsizeof: Callable[[Any], float] = None,
+        ) -> Table[BaseID, BaseDocument]:
+            """
+            ### FIFOCache
+            First In First Out Cache
+            """
+            cls._add_cache(tab, cachetools.FIFOCache, maxsize, getsizeof)
+            return tab
+
+        @classmethod
+        def MRUCache(
+                cls,
+                tab: Table | TinyDB,
+                maxsize: int,
+                getsizeof: Callable[[Any], float] = None,
+        ) -> Table[BaseID, BaseDocument]:
+            """
+            ### MRUCache
+            Most Recently Used Cache
+            """
+            cls._add_cache(tab, cachetools.MRUCache, maxsize, getsizeof)
+            return tab
```

### Comparing `async_tinydb-1.6.1/asynctinydb/mypy_plugin.py` & `async_tinydb-1.7.0/asynctinydb/mypy_plugin.py`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/asynctinydb/operations.py` & `async_tinydb-1.7.0/asynctinydb/operations.py`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/asynctinydb/queries.py` & `async_tinydb-1.7.0/asynctinydb/queries.py`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/asynctinydb/storages.py` & `async_tinydb-1.7.0/asynctinydb/storages.py`

 * *Files identical despite different names*

### Comparing `async_tinydb-1.6.1/asynctinydb/table.py` & `async_tinydb-1.7.0/asynctinydb/table.py`

 * *Files 2% similar despite different names*

```diff
@@ -108,42 +108,32 @@
     @classmethod
     def clear_cache(cls, table: Table):
         cls._cache.pop(table.name, None)
 
 
 class UUID(uuid.UUID, BaseID):
     """ID class using uuid4 UUIDs."""
-    _cache: dict[str, set[uuid.UUID]] = {}
 
     def __init__(self, value: str | uuid.UUID):  # skipcq: PYL-W0231
         super().__init__(str(value))
 
     def __hash__(self):
         return uuid.UUID.__hash__(self)
 
     @classmethod
     def next_id(cls, table: Table, keys: Collection[UUID]) -> UUID:
-        if table.name not in cls._cache:
-            cls._cache[table.name] = set()
-        while True:
-            new_id = cls(uuid.uuid4())
-            if (new_id not in cls._cache[table.name]  # pragma: no branch
-                    and new_id not in keys):
-                cls._cache[table.name].add(new_id)
-                return new_id
+        return cls(uuid.uuid4())
 
     @classmethod
     def mark_existed(cls, table: Table, new_id: UUID):
-        cache = cls._cache.get(table.name, set())
-        cache.add(new_id)
-        cls._cache[table.name] = cache
+        ...
 
     @classmethod
     def clear_cache(cls, table: Table):
-        cls._cache.pop(table.name, None)
+        ...
 
 
 class BaseDocument(MutableMapping[IDVar, Any]):
     @property
     @abstractmethod
     def doc_id(self) -> IDVar:
         raise NotImplementedError()
@@ -247,15 +237,15 @@
         """The class used for document IDs in this table."""
         self.document_class = document_class
         """The class used to represent documents in this table."""
         self.no_dbcache = no_dbcache
         """Whether to disable the DB-level cache for this table."""
         self._storage = storage
         self._name = name
-        self._cache: dict[IDVar, DocVar] = None  # type: ignore
+        self._cache: MutableMapping[IDVar, DocVar] = None  # type: ignore[assignment]
         """Cache for documents in this table."""
         self._query_cache: LRUCache[QueryLike, tuple[IDVar, ...]] \
             = self.query_cache_class(capacity=cache_size)
         """Cache for query results in this table."""
 
         self.document_id_class.clear_cache(self)  # clear the ID cache
 
@@ -318,15 +308,15 @@
 
         # Make sure the document implements the ``Mapping`` interface
         if not isinstance(document, Mapping):
             raise ValueError("Document is not a Mapping")
 
         doc_id: IDVar = None  # type: ignore
 
-        def updater(table: dict[IDVar, DocVar]):
+        def updater(table: MutableMapping[IDVar, DocVar]):
             # Now, we update the table and add the document
             nonlocal doc_id
             nonlocal document
 
             if isinstance(document, self.document_class):
                 # For a `Document` object we use the specified ID
                 doc_id = self.document_id_class(document.doc_id)
@@ -360,15 +350,15 @@
 
         :param documents: an Iterable of documents to insert
         :returns: a list containing the inserted documents' IDs
         """
 
         doc_ids = []
 
-        def updater(table: dict[IDVar, DocVar]):
+        def updater(table: MutableMapping[IDVar, DocVar]):
             existing_keys = table.keys()
             for document in documents:
 
                 # Make sure the document implements the ``Mapping`` interface
                 if not isinstance(document, Mapping):
                     raise ValueError("Document is not a Mapping")
 
@@ -476,15 +466,15 @@
         """
         if cond is None and doc_id is None:
             raise ValueError("You have to pass either cond or doc_id")
         return (await self.get(cond, doc_id=doc_id)) is not None
 
     async def update(
         self,
-        fields: Mapping | Callable[[Mapping], None],
+        fields: Mapping | Callable[[MutableMapping], None],
         cond: QueryLike = None,
         doc_ids: Iterable[IDVar] = None,
     ) -> list[IDVar]:
         """
         Update all matching documents to have a given set of fields.
 
         :param fields: the fields that the matching documents will have
@@ -492,32 +482,32 @@
         :param cond: which documents to update
         :param doc_ids: a list of document IDs
         :returns: a list containing the updated document's ID
         """
 
         # Define the function that will perform the update
         if callable(fields):
-            def perform_update(table: dict[IDVar, DocVar], doc_id: IDVar):
+            def perform_update(table: MutableMapping[IDVar, DocVar], doc_id: IDVar):
                 # Update documents by calling the update function provided by
                 # the user
                 fields(table[doc_id])  # type: ignore
         else:
-            def perform_update(table: dict[IDVar, DocVar], doc_id: IDVar):
+            def perform_update(table: MutableMapping[IDVar, DocVar], doc_id: IDVar):
                 nonlocal fields
                 if self._isolevel >= 2:
                     fields = deepcopy(fields)
                 # Update documents by setting all fields from the provided data
                 table[doc_id].update(fields)  # type: ignore
 
         docs = await self.search(cond, doc_ids=doc_ids)
         ids = [doc.doc_id for doc in docs]
 
         updated_ids = []
 
-        def updater(table: dict[IDVar, DocVar]):
+        def updater(table: MutableMapping[IDVar, DocVar]):
             # Process all documents
             for doc_id in ids:
                 # Add ID to list of updated documents
                 updated_ids.append(doc_id)
 
                 # Perform the update (see above)
                 perform_update(table, doc_id)
@@ -539,15 +529,15 @@
         Update all matching documents to have a given set of fields.
 
         :returns: a list containing the updated document's ID
         """
 
         # Define the function that will perform the update
         def perform_update(fields: Callable[[Mapping], None] | Mapping,
-                           table: dict[IDVar, DocVar], doc_id: IDVar):
+                           table: MutableMapping[IDVar, DocVar], doc_id: IDVar):
             if callable(fields):
                 # Update documents by calling the update function provided
                 # by the user
                 fields(table[doc_id])
             else:
                 if self._isolevel >= 2:
                     fields = deepcopy(fields)
@@ -556,15 +546,15 @@
                 table[doc_id].update(fields)
 
         # Perform the update operation for documents specified by a query
 
         # Collect affected doc_ids
         updated_ids = []
 
-        def updater(table: dict[IDVar, DocVar]):
+        def updater(table: MutableMapping[IDVar, DocVar]):
             # We need to convert the keys iterator to a list because
             # we may remove entries from the ``table`` dict during
             # iteration and doing this without the list conversion would
             # result in an exception (RuntimeError: dictionary changed size
             # during iteration)
             for doc_id in list(table.keys()):
                 for fields, cond in updates:
@@ -641,15 +631,15 @@
 
         if cond is None and doc_ids is None:
             raise RuntimeError('Use truncate() to remove all documents')
 
         docs = await self.search(cond, doc_ids=doc_ids)
         ids = [doc.doc_id for doc in docs]
 
-        def rm_updater(table: dict[IDVar, DocVar]):
+        def rm_updater(table: MutableMapping[IDVar, DocVar]):
             for doc_id in ids:
                 # Other threads may have already removed the document
                 with suppress(KeyError):
                     doc = table.pop(doc_id)
                     self.event_hook.emit("delete", self, doc)
 
         # Perform the remove operation
@@ -748,15 +738,15 @@
     def __del__(self):
         """
         Clean up the table.
         """
         self._sink.close()
 
     def _search(self, cond: QueryLike | None,
-                docs: dict[IDVar, DocVar],
+                docs: MutableMapping[IDVar, DocVar],
                 limit: int | None,
                 doc_ids: Iterable[IDVar] | None) -> dict[IDVar, DocVar]:
         limit = len(docs) if limit is None else limit
         if limit < 0:
             raise ValueError("Limit must be non-negative")
         cacheable = cond is not None and is_cacheable(cond)
         cond = cast(QueryLike, cond)
@@ -803,44 +793,48 @@
         # Trigger event
         if self.event_hook["read"]:
             for doc in docs.values():
                 self.event_hook.emit("read", self, doc)
 
         # deepcopy if isolation level is >= 2
         # otherwise return shallow copy in case of no sieve been applied
+        # ps: sieves will perform a shallow copy.
+        if not isinstance(docs, dict):
+            docs = dict(docs)
+
         return deepcopy(docs) if self._isolevel >= 2 else docs.copy()
 
-    async def _read_table(self) -> dict[IDVar, DocVar]:
+    async def _read_table(self) -> MutableMapping[IDVar, DocVar]:
         """
         Read the table data from the underlying storage 
         if cache is not exist.
         """
 
         # If cache exists
         if self._cache is not None:
             return self._cache
 
         # Read the table data from the underlying storage
         raw = await self._read_raw_table()
         cooked: dict[IDVar, DocVar] | None = None
 
-        def cook():
-            nonlocal cooked
-            doc_cls = self.document_class
-            id_cls = self.document_id_class
-            cooked = {
-                id_cls(doc_id): doc_cls(rdoc, doc_id=id_cls(doc_id))
-                for doc_id, rdoc in raw.items()
-            }
-            if not self.no_dbcache:
-                # Caching if no_dbcache is not set
-                self._cache = cooked
-
-        await self._run_with_iso(cook)
-        return self._cache or cooked
+        cooked = await self._run_with_iso(self._cook, raw)
+        if not self.no_dbcache:
+            # Caching if no_dbcache is not set
+            self._cache = cooked
+        return cooked
+
+    def _cook(self, raw: Mapping[Any, Mapping]
+              ) -> MutableMapping[IDVar, DocVar]:
+        doc_cls = self.document_class
+        id_cls = self.document_id_class
+        return {
+            id_cls(doc_id): doc_cls(rdoc, doc_id=id_cls(doc_id))
+            for doc_id, rdoc in raw.items()
+        }
 
     async def _read_raw_table(self) -> MutableMapping[Any, Mapping]:
         """
         Read the table data from the underlying storage.
 
         Documents and doc_ids are NOT yet transformed, as 
         we may not want to convert *all* documents when returning
@@ -853,15 +847,16 @@
         if tables is None:
             # The database is empty
             return {}
 
         # Retrieve the current table's data
         return tables.get(self.name, {})
 
-    async def _update_table(self, updater: Callable[[dict[IDVar, DocVar]], None]):
+    async def _update_table(self,
+                            updater: Callable[[MutableMapping[IDVar, DocVar]], None]):
         """
         Perform a table update operation.
 
         The storage interface used by TinyDB only allows to read/write the
         complete database data, but not modifying only portions of it. Thus,
         to only update portions of the table data, we first perform a read
         operation, perform the update on the table data and then write
```

### Comparing `async_tinydb-1.6.1/asynctinydb/utils.py` & `async_tinydb-1.7.0/asynctinydb/utils.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,17 +1,19 @@
 """
 Utility functions.
 """
 
 from __future__ import annotations
 from collections import OrderedDict
 from contextlib import suppress
-from typing import Iterator, TypeVar, Generic, Type, \
-    TYPE_CHECKING, Callable,  MutableMapping
+from typing import Any, Iterator, TypeVar, Generic, Type, \
+    TYPE_CHECKING, Callable
 
+from contextlib import suppress
+from cachetools import LRUCache as _LRUCache
 from vermils.collections.fridge import FrozenDict, FrozenList, freeze
 from vermils.collections.strchain import StrChain
 from vermils.gadgets import mimics, sort_class, stringify_keys, supports_in
 from vermils.asynctools import *
 from vermils.asynctools import __all__ as _async_tools_all
 
 K = TypeVar("K")
@@ -22,15 +24,16 @@
 V_co = TypeVar("V_co", covariant=True)
 S = TypeVar("S", bound="StrChain")
 C = TypeVar("C", bound=Callable)
 
 __all__ = (("LRUCache", "freeze", "with_typehint", "stringify_keys",
             "supports_in", "is_container", "is_iterable", "is_hashable",
             "StrChain", "FrozenDict", "mimics", "sort_class", "FrozenList",
-            ) + _async_tools_all)
+            ) + _async_tools_all
+           )
 
 
 def with_typehint(baseclass: Type[T]):
     """
     Add type hints from a specified class to a base class:
 
     >>> class Foo(with_typehint(Bar)):
@@ -62,80 +65,34 @@
     return hasattr(obj, "__iter__")
 
 
 def is_container(obj) -> bool:
     return hasattr(obj, "__contains__")
 
 
-class LRUCache(MutableMapping, Generic[K, V]):
+class LRUCache(_LRUCache, Generic[K, V]):
     """
     A least-recently used (LRU) cache with a fixed cache size.
 
     This class acts as a dictionary but has a limited size. If the number of
     entries in the cache exceeds the cache size, the least-recently accessed
     entry will be discarded.
 
-    This is implemented using an ``OrderedDict``. On every access the accessed
-    entry is moved to the front by re-inserting it into the ``OrderedDict``.
-    When adding an entry and the cache size is exceeded, the last entry will
-    be discarded.
+    This is implemented uses the ``cachetools`` package.
     """
 
-    def __init__(self, capacity=None) -> None:
-        self.capacity = capacity
-        self.cache: OrderedDict[K, V] = OrderedDict()
+    def __init__(self, capacity=None,
+                 getsizeof: Callable[[Any], int] = None) -> None:
+        capacity = float("inf") if capacity is None else capacity
+        super().__init__(maxsize=capacity, getsizeof=getsizeof)
 
     @property
     def lru(self) -> list[K]:
-        return list(self.cache.keys())
+        return list(self.keys())
 
     @property
     def length(self) -> int:
-        return len(self.cache)
-
-    def clear(self) -> None:
-        self.cache.clear()
-
-    def __len__(self) -> int:
-        return self.length
-
-    def __contains__(self, key: object) -> bool:
-        return key in self.cache
+        return len(self)
 
     def __setitem__(self, key: K, value: V) -> None:
-        self.set(key, value)
-
-    def __delitem__(self, key: K) -> None:
-        del self.cache[key]
-
-    def __getitem__(self, key) -> V:
-        value = self.get(key)
-        if value is None:
-            raise KeyError(key)
-
-        return value
-
-    def __iter__(self) -> Iterator[K]:
-        return iter(self.cache)
-
-    def get(self, key: K, default: D = None) -> V | D | None:
-        value = self.cache.get(key)
-
-        if value is not None:
-            self.cache.move_to_end(key, last=True)
-
-            return value
-
-        return default
-
-    def set(self, key: K, value: V):
-        if self.cache.get(key):
-            self.cache.move_to_end(key, last=True)
-
-        else:
-            self.cache[key] = value
-
-            # Check, if the cache is full and we have to remove old items
-            # If the queue is of unlimited size, self.capacity is NaN and
-            # x > NaN is always False in Python and the cache won't be cleared.
-            if self.capacity is not None and self.length > self.capacity:
-                self.cache.popitem(last=False)
+        with suppress(ValueError):
+            super().__setitem__(key, value)
```

### Comparing `async_tinydb-1.6.1/pyproject.toml` & `async_tinydb-1.7.0/pyproject.toml`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "async-tinydb"
-version = "1.6.1"
+version = "1.7.0"
 description = "Yet Another Async TinyDB"
 authors = ["VermiIIi0n <dungeon.behind0t@icloud.com>", "Markus Siemens <markus@m-siemens.de>", ]
 license = "MIT"
 
 readme = "README.md"
 
 homepage = "https://github.com/VermiIIi0n/async-tinydb"
@@ -30,14 +30,17 @@
     "Operating System :: OS Independent",
     "Typing :: Typed",
 ]
 
 packages = [
     { include = "asynctinydb" }
 ]
+[tool.poetry.group.dev.dependencies]
+autopep8 = "^2.0.2"
+
 
 [tool.pytest.ini_options]
 asyncio_mode = "auto"
 addopts = "--verbose --cov-append --cov-report term --cov asynctinydb --cov-config .coveragerc"
 filterwarnings = ["ignore::DeprecationWarning:coverage"]
 
 [tool.mypy]
@@ -86,14 +89,16 @@
 nest-asyncio = "^1.5.5"
 ujson = "^5.4.0"
 pycryptodome = {version = "^3.15.0", optional = true}
 Brotli = {version = "^1.0.9", optional = true}
 blosc2 = {version = "^0.4.1", optional = true}
 types-ujson = "^5.5.0"
 vermils = "^0.3.0"
+cachetools = "^5.3.0"
+types-cachetools = "^5.3.0.5"
 
 [tool.poetry.extras]
 encryption = ["pycryptodome"]
 compression = ["Brotli", "blosc2"]
 all = ["pycryptodome", "Brotli", "blosc2"]
 
 [tool.poetry.dev-dependencies]
```

### Comparing `async_tinydb-1.6.1/PKG-INFO` & `async_tinydb-1.7.0/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: async-tinydb
-Version: 1.6.1
+Version: 1.7.0
 Summary: Yet Another Async TinyDB
 Home-page: https://github.com/VermiIIi0n/async-tinydb
 License: MIT
 Keywords: database,nosql,async
 Author: VermiIIi0n
 Author-email: dungeon.behind0t@icloud.com
 Requires-Python: >=3.10,<4.0
@@ -29,16 +29,18 @@
 Classifier: Topic :: Utilities
 Classifier: Typing :: Typed
 Provides-Extra: all
 Provides-Extra: compression
 Provides-Extra: encryption
 Requires-Dist: Brotli (>=1.0.9,<2.0.0) ; extra == "compression" or extra == "all"
 Requires-Dist: blosc2 (>=0.4.1,<0.5.0) ; extra == "compression" or extra == "all"
+Requires-Dist: cachetools (>=5.3.0,<6.0.0)
 Requires-Dist: nest-asyncio (>=1.5.5,<2.0.0)
 Requires-Dist: pycryptodome (>=3.15.0,<4.0.0) ; extra == "encryption" or extra == "all"
+Requires-Dist: types-cachetools (>=5.3.0.5,<6.0.0.0)
 Requires-Dist: types-ujson (>=5.5.0,<6.0.0)
 Requires-Dist: ujson (>=5.4.0,<6.0.0)
 Requires-Dist: vermils (>=0.3.0,<0.4.0)
 Project-URL: Issues, https://github.com/VermiIIi0n/async-tinydb/issues
 Description-Content-Type: text/markdown
 
 <img src="./artwork/logo.png" alt="logo" style="zoom:50%;" />
```

