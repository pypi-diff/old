# Comparing `tmp/spiderYdb-0.1.8-py3-none-any.whl.zip` & `tmp/spiderYdb-0.1.9-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,14 +1,14 @@
-Zip file size: 8206 bytes, number of entries: 12
--rw-rw-rw-  2.0 fat       95 b- defN 22-Nov-30 13:51 spiderYdb/__init__.py
--rw-rw-rw-  2.0 fat      349 b- defN 22-Oct-29 16:40 spiderYdb/config.py
--rw-rw-rw-  2.0 fat     3071 b- defN 22-Nov-15 08:03 spiderYdb/core.py
--rw-rw-rw-  2.0 fat     1912 b- defN 22-Nov-04 13:12 spiderYdb/entity.py
--rw-rw-rw-  2.0 fat     3436 b- defN 22-Nov-15 07:27 spiderYdb/entityMeta.py
--rw-rw-rw-  2.0 fat     3587 b- defN 22-Nov-30 13:51 spiderYdb/fields.py
--rw-rw-rw-  2.0 fat     4659 b- defN 22-Nov-15 07:55 spiderYdb/query.py
--rw-rw-rw-  2.0 fat     1090 b- defN 22-Nov-30 13:52 spiderYdb-0.1.8.dist-info/LICENSE
--rw-rw-rw-  2.0 fat      266 b- defN 22-Nov-30 13:52 spiderYdb-0.1.8.dist-info/METADATA
--rw-rw-rw-  2.0 fat       92 b- defN 22-Nov-30 13:52 spiderYdb-0.1.8.dist-info/WHEEL
--rw-rw-rw-  2.0 fat       10 b- defN 22-Nov-30 13:52 spiderYdb-0.1.8.dist-info/top_level.txt
-?rw-rw-r--  2.0 fat      927 b- defN 22-Nov-30 13:52 spiderYdb-0.1.8.dist-info/RECORD
-12 files, 19494 bytes uncompressed, 6662 bytes compressed:  65.8%
+Zip file size: 8288 bytes, number of entries: 12
+-rw-rw-rw-  2.0 fat       95 b- defN 23-Jan-26 12:17 spiderYdb/__init__.py
+-rw-rw-rw-  2.0 fat      349 b- defN 22-Dec-14 11:31 spiderYdb/config.py
+-rw-rw-rw-  2.0 fat     3071 b- defN 22-Dec-14 11:31 spiderYdb/core.py
+-rw-rw-rw-  2.0 fat     1912 b- defN 22-Dec-14 11:31 spiderYdb/entity.py
+-rw-rw-rw-  2.0 fat     3525 b- defN 23-Jan-26 12:14 spiderYdb/entityMeta.py
+-rw-rw-rw-  2.0 fat     3587 b- defN 22-Dec-14 11:31 spiderYdb/fields.py
+-rw-rw-rw-  2.0 fat     4922 b- defN 23-Jan-26 12:17 spiderYdb/query.py
+-rw-rw-rw-  2.0 fat     1090 b- defN 23-Jan-26 12:23 spiderYdb-0.1.9.dist-info/LICENSE
+-rw-rw-rw-  2.0 fat      266 b- defN 23-Jan-26 12:23 spiderYdb-0.1.9.dist-info/METADATA
+-rw-rw-rw-  2.0 fat       92 b- defN 23-Jan-26 12:23 spiderYdb-0.1.9.dist-info/WHEEL
+-rw-rw-rw-  2.0 fat       10 b- defN 23-Jan-26 12:23 spiderYdb-0.1.9.dist-info/top_level.txt
+?rw-rw-r--  2.0 fat      927 b- defN 23-Jan-26 12:23 spiderYdb-0.1.9.dist-info/RECORD
+12 files, 19846 bytes uncompressed, 6744 bytes compressed:  66.0%
```

## zipnote {}

```diff
@@ -15,23 +15,23 @@
 
 Filename: spiderYdb/fields.py
 Comment: 
 
 Filename: spiderYdb/query.py
 Comment: 
 
-Filename: spiderYdb-0.1.8.dist-info/LICENSE
+Filename: spiderYdb-0.1.9.dist-info/LICENSE
 Comment: 
 
-Filename: spiderYdb-0.1.8.dist-info/METADATA
+Filename: spiderYdb-0.1.9.dist-info/METADATA
 Comment: 
 
-Filename: spiderYdb-0.1.8.dist-info/WHEEL
+Filename: spiderYdb-0.1.9.dist-info/WHEEL
 Comment: 
 
-Filename: spiderYdb-0.1.8.dist-info/top_level.txt
+Filename: spiderYdb-0.1.9.dist-info/top_level.txt
 Comment: 
 
-Filename: spiderYdb-0.1.8.dist-info/RECORD
+Filename: spiderYdb-0.1.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## spiderYdb/__init__.py

```diff
@@ -1,3 +1,3 @@
 # from __future__ import absolute_import
-__version__ = '0.1.8'
+__version__ = '0.1.9'
 from spiderYdb.core import *
```

## spiderYdb/entityMeta.py

```diff
@@ -62,14 +62,17 @@
     def _select_all(cls, args, kwargs):
         return Query(cls, args, kwargs).select()
 
     def select(cls, *args, **kwargs):
         query = cls._select_all(args, kwargs)
         return query
 
+    def count(cls, *args, **kwargs):
+        return Query(cls, args, kwargs).count()
+
     def bulk(cls, item_list=[], *args, **kwargs):
         query = Query(cls, args, kwargs)
         query.bulk(item_list)
 
     def _delete(cls, args, kwargs):
         return Query(cls, args, kwargs).delete()
```

## spiderYdb/query.py

```diff
@@ -1,20 +1,26 @@
 import ydb
 
 
 class Query:
     def __init__(self, table, args, kwargs):
         self.args = args
         self.table = table
+        self.q = '*'
         self.database = table._database_
 
     def select(self):
         objects = self[:]
         return [self.table.from_dict(item) for item in objects]
 
+    def count(self):
+        self.q = 'count(*) AS c'
+        objects = self[:]
+        return objects[0]['c']
+
     def bulk(self, item_list):
         column_types = ydb.BulkUpsertColumns()
         # column_list = []
         for key in item_list[0]:
             if key in self.table.attrs_dict:
                 column_types.add_column(key, self.table.attrs_dict[key].ydb_type)
         return self.database.bulk(self.table.table_name, column_types, item_list)
@@ -48,24 +54,27 @@
     def _fetch(self, limit=None, offset=None, lazy=False):
         return QueryResult(self, limit, offset, lazy=lazy)
 
     def _actual_fetch(self, limit, offset):
         declare = []
         where = []
         params = {}
+        i = 0
         for _ in self.args:
             t, field, value = _
-            name, title = f"{field.name}", field.title
+            # name, title = f"{field.name}", field.title
+            name, param, title = f"{field.name}", f"param{i}", field.title
             if t in ['in']:
-                declare.append(f"DECLARE ${name} AS List<{title}>;")
+                declare.append(f"DECLARE ${param} AS List<{title}>;")
             else:
-                declare.append(f"DECLARE ${name} AS {title};")
-            params[f'${name}'] = value
-            where.append(f'{name} {t} ${name}')
-        sql = f'SELECT * from {self.table.table_name}'
+                declare.append(f"DECLARE ${param} AS {title};")
+            params[f'${param}'] = value
+            where.append(f'{name} {t} ${param}')
+            i += 1
+        sql = f'SELECT {self.q} from {self.table.table_name}'
         if declare:
             sql = '\n'.join(declare) + '\n' + sql
         if where:
             sql = sql + '\nWHERE ' + ' AND '.join(where)
         # print(sql)
         return self.database.query(sql, params)
```

## Comparing `spiderYdb-0.1.8.dist-info/LICENSE` & `spiderYdb-0.1.9.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `spiderYdb-0.1.8.dist-info/RECORD` & `spiderYdb-0.1.9.dist-info/RECORD`

 * *Files 18% similar despite different names*

```diff
@@ -1,12 +1,12 @@
-spiderYdb/__init__.py,sha256=7YI-YZgg6AqymWkF9lrhj09rIj8bA-T4nmQ4ogUOYeU,95
+spiderYdb/__init__.py,sha256=PdrhgX6doqk6owjFbKsUAOgaD8Y4Sz3kzLtMGIsUx7Y,95
 spiderYdb/config.py,sha256=mcWIzUlgE3a_soMov-F8ZlYZL2H4vuvBXhrBvwcNUnQ,349
 spiderYdb/core.py,sha256=FUkUX41XIKT8oF4-vYoP1T9icjCoxFgkbdP4tOPs7j4,3071
 spiderYdb/entity.py,sha256=NW34zGUts6qJEe5jKdtasqsU7LPGIiON8UDA_PV-ALU,1912
-spiderYdb/entityMeta.py,sha256=6Y4fRyaMo8HX4fmrPbrLgQp6J8FiliMb3mXIjpxfrEc,3436
+spiderYdb/entityMeta.py,sha256=KTXC_nkZEXBJvr0owOpQ2fkNR-Y4LzSQ-j3JB91Zixs,3525
 spiderYdb/fields.py,sha256=uPUsn9aazpBef6viRGNY7dRl1ptTmBOAJcAWXC7sbR8,3587
-spiderYdb/query.py,sha256=SOMx0i2cotfaB1F2IuW8ap9bQxBNFh0PWtjI_ZdHLt8,4659
-spiderYdb-0.1.8.dist-info/LICENSE,sha256=s6A7KiSEZISWC-xFDot8mFiaExKEaDAzp5JBY-fEdwg,1090
-spiderYdb-0.1.8.dist-info/METADATA,sha256=GjH8hFp97eDtpA9QdWYueugaTuxsKQkYlgoOyvDYzaU,266
-spiderYdb-0.1.8.dist-info/WHEEL,sha256=OqRkF0eY5GHssMorFjlbTIq072vpHpF60fIQA6lS9xA,92
-spiderYdb-0.1.8.dist-info/top_level.txt,sha256=fGf3eJV4AUx4yNfF06V5ekvNXak-mN5tD6Slu-ys3rs,10
-spiderYdb-0.1.8.dist-info/RECORD,,
+spiderYdb/query.py,sha256=rgliqLOuJ94--4IwABEu1e_pXrTPLW6Go9PaXf58ABk,4922
+spiderYdb-0.1.9.dist-info/LICENSE,sha256=s6A7KiSEZISWC-xFDot8mFiaExKEaDAzp5JBY-fEdwg,1090
+spiderYdb-0.1.9.dist-info/METADATA,sha256=tGvI1sTOixI9TJctI_0RcBAqxMAINcB9ugxaFSDa9oc,266
+spiderYdb-0.1.9.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+spiderYdb-0.1.9.dist-info/top_level.txt,sha256=fGf3eJV4AUx4yNfF06V5ekvNXak-mN5tD6Slu-ys3rs,10
+spiderYdb-0.1.9.dist-info/RECORD,,
```

