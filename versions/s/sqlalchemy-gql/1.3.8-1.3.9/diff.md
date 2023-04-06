# Comparing `tmp/sqlalchemy-gql-1.3.8.tar.gz` & `tmp/sqlalchemy-gql-1.3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sqlalchemy-gql-1.3.8.tar", last modified: Wed Nov 30 16:42:11 2022, max compression
+gzip compressed data, was "sqlalchemy-gql-1.3.9.tar", last modified: Thu Feb  2 00:00:03 2023, max compression
```

## Comparing `sqlalchemy-gql-1.3.8.tar` & `sqlalchemy-gql-1.3.9.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-30 16:42:11.010629 sqlalchemy-gql-1.3.8/
--rw-rw-rw-   0 root         (0) root         (0)     1070 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/LICENSE
--rw-rw-rw-   0 root         (0) root         (0)       15 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      754 2022-11-30 16:42:11.010629 sqlalchemy-gql-1.3.8/PKG-INFO
--rwxrwxrwx   0 root         (0) root         (0)       86 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/README.md
--rw-rw-rw-   0 root         (0) root         (0)        6 2022-11-30 16:42:10.000000 sqlalchemy-gql-1.3.8/VERSION
--rw-rw-rw-   0 root         (0) root         (0)       79 2022-11-30 16:42:11.011629 sqlalchemy-gql-1.3.8/setup.cfg
--rwxrwxrwx   0 root         (0) root         (0)     1267 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-30 16:42:11.007629 sqlalchemy-gql-1.3.8/sqlalchemy_gql/
--rwxrwxrwx   0 root         (0) root         (0)      203 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     4245 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql/mapper.py
--rw-rw-rw-   0 root         (0) root         (0)     4656 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql/mixin.py
--rwxrwxrwx   0 root         (0) root         (0)     3587 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql/orm_base.py
--rwxrwxrwx   0 root         (0) root         (0)     7389 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql/relay_base.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-30 16:42:11.009629 sqlalchemy-gql-1.3.8/sqlalchemy_gql.egg-info/
--rw-r--r--   0 root         (0) root         (0)      754 2022-11-30 16:42:10.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      469 2022-11-30 16:42:10.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-11-30 16:42:10.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       79 2022-11-30 16:42:10.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       21 2022-11-30 16:42:10.000000 sqlalchemy-gql-1.3.8/sqlalchemy_gql.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-11-30 16:42:11.010629 sqlalchemy-gql-1.3.8/tests/
--rw-rw-rw-   0 root         (0) root         (0)        0 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/tests/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1123 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/tests/test_base.py
--rw-rw-rw-   0 root         (0) root         (0)     2542 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/tests/test_relay_base.py
--rw-rw-rw-   0 root         (0) root         (0)     2399 2022-11-30 16:42:02.000000 sqlalchemy-gql-1.3.8/tests/test_sqlalachemy_orm.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-02 00:00:03.477826 sqlalchemy-gql-1.3.9/
+-rw-rw-rw-   0 root         (0) root         (0)     1070 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/LICENSE
+-rw-rw-rw-   0 root         (0) root         (0)       15 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      754 2023-02-02 00:00:03.477826 sqlalchemy-gql-1.3.9/PKG-INFO
+-rwxrwxrwx   0 root         (0) root         (0)       86 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/README.md
+-rw-rw-rw-   0 root         (0) root         (0)        6 2023-02-02 00:00:02.000000 sqlalchemy-gql-1.3.9/VERSION
+-rw-rw-rw-   0 root         (0) root         (0)       79 2023-02-02 00:00:03.478826 sqlalchemy-gql-1.3.9/setup.cfg
+-rwxrwxrwx   0 root         (0) root         (0)     1267 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-02 00:00:03.474826 sqlalchemy-gql-1.3.9/sqlalchemy_gql/
+-rwxrwxrwx   0 root         (0) root         (0)      203 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     4197 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql/mapper.py
+-rw-rw-rw-   0 root         (0) root         (0)     4656 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql/mixin.py
+-rwxrwxrwx   0 root         (0) root         (0)     3587 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql/orm_base.py
+-rwxrwxrwx   0 root         (0) root         (0)     7389 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql/relay_base.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-02 00:00:03.475826 sqlalchemy-gql-1.3.9/sqlalchemy_gql.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      754 2023-02-02 00:00:03.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      469 2023-02-02 00:00:03.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-02-02 00:00:03.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       79 2023-02-02 00:00:03.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       21 2023-02-02 00:00:03.000000 sqlalchemy-gql-1.3.9/sqlalchemy_gql.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-02 00:00:03.477826 sqlalchemy-gql-1.3.9/tests/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/tests/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     2076 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/tests/test_base.py
+-rw-rw-rw-   0 root         (0) root         (0)     2542 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/tests/test_relay_base.py
+-rw-rw-rw-   0 root         (0) root         (0)     2399 2023-02-01 23:59:54.000000 sqlalchemy-gql-1.3.9/tests/test_sqlalachemy_orm.py
```

### Comparing `sqlalchemy-gql-1.3.8/LICENSE` & `sqlalchemy-gql-1.3.9/LICENSE`

 * *Files identical despite different names*

### Comparing `sqlalchemy-gql-1.3.8/PKG-INFO` & `sqlalchemy-gql-1.3.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: sqlalchemy-gql
-Version: 1.3.8
+Version: 1.3.9
 Summary: Map SQLAlchemy models to GraphQL Objects.
 Home-page: https://gitlab.com/parob/sqlalchemy-gql
-Download-URL: https://gitlab.com/parob/sqlalchemy-gql/-/archive/v1.3.8/sqlalchemy-gql-v1.3.8.tar.gz
+Download-URL: https://gitlab.com/parob/sqlalchemy-gql/-/archive/v1.3.9/sqlalchemy-gql-v1.3.9.tar.gz
 Author: Robert Parker
 Author-email: rob@parob.com
 License: MIT
 Keywords: GraphQL,GraphQL API,Server,DataRM,ORM
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `sqlalchemy-gql-1.3.8/setup.py` & `sqlalchemy-gql-1.3.9/setup.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-gql-1.3.8/sqlalchemy_gql/mapper.py` & `sqlalchemy-gql-1.3.9/sqlalchemy_gql/mapper.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,16 +5,15 @@
 
 from graphql import GraphQLString
 from graphql.type.definition import \
     GraphQLType, \
     GraphQLList, \
     GraphQLScalarType
 
-from sqlalchemy import Column
-from sqlalchemy.databases import postgres
+from sqlalchemy import Column, UUID, Enum
 from sqlalchemy.ext.associationproxy import AssociationProxy
 from sqlalchemy.orm import interfaces, RelationshipProperty, relationship
 from sqlalchemy.sql.type_api import TypeEngine
 
 
 from graphql_api.mapper import GraphQLTypeMapper
 from graphql_api.types import GraphQLUUID
@@ -80,16 +79,16 @@
                 return GraphQLSQLAlchemyHelpers.map_type(column_type_class)
         else:
             return mapper.map(python_type)
 
     @staticmethod
     def map_type(type_: Type[TypeEngine]) -> GraphQLScalarType:
         scalar_map = [
-            ([postgres.UUID], GraphQLUUID),
-            ([postgres.ENUM], GraphQLString)
+            ([UUID], GraphQLUUID),
+            ([Enum], GraphQLString)
         ]
 
         for test_types, graphql_type in scalar_map:
             for test_type in test_types:
                 if issubclass(type_, test_type):
                     return graphql_type
```

### Comparing `sqlalchemy-gql-1.3.8/sqlalchemy_gql/mixin.py` & `sqlalchemy-gql-1.3.9/sqlalchemy_gql/mixin.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-gql-1.3.8/sqlalchemy_gql/orm_base.py` & `sqlalchemy-gql-1.3.9/sqlalchemy_gql/orm_base.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-gql-1.3.8/sqlalchemy_gql/relay_base.py` & `sqlalchemy-gql-1.3.9/sqlalchemy_gql/relay_base.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-gql-1.3.8/sqlalchemy_gql.egg-info/PKG-INFO` & `sqlalchemy-gql-1.3.9/sqlalchemy_gql.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: sqlalchemy-gql
-Version: 1.3.8
+Version: 1.3.9
 Summary: Map SQLAlchemy models to GraphQL Objects.
 Home-page: https://gitlab.com/parob/sqlalchemy-gql
-Download-URL: https://gitlab.com/parob/sqlalchemy-gql/-/archive/v1.3.8/sqlalchemy-gql-v1.3.8.tar.gz
+Download-URL: https://gitlab.com/parob/sqlalchemy-gql/-/archive/v1.3.9/sqlalchemy-gql-v1.3.9.tar.gz
 Author: Robert Parker
 Author-email: rob@parob.com
 License: MIT
 Keywords: GraphQL,GraphQL API,Server,DataRM,ORM
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `sqlalchemy-gql-1.3.8/tests/test_base.py` & `sqlalchemy-gql-1.3.9/tests/test_base.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,10 +1,13 @@
+import uuid
+
 from graphql_api import GraphQLAPI
 
 # noinspection DuplicatedCode
+from sqlalchemy import UUID
 from sqlalchemy.orm import declarative_base
 from sqlalchemy_gql.mixin import GraphQLSQLAlchemyMixin
 
 
 class TestModel:
 
     def test_basic(self):
@@ -45,7 +48,44 @@
             "person": {
                 "name": "ed",
                 "age": 55
             }
         }
 
         assert expected == result.data
+
+    def test_uuid(self):
+
+        Base = declarative_base()
+
+        from sqlalchemy import Column, Integer, String
+
+        class Person(GraphQLSQLAlchemyMixin, Base):
+            __tablename__ = 'people'
+            id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
+            name = Column(String)
+
+        person_id = uuid.uuid4()
+
+        person = Person(id=person_id, name='joe')
+
+
+        schema = GraphQLAPI()
+
+        @schema.type(root=True)
+        class Root:
+
+            @schema.field
+            def person(self) -> Person:
+                return person
+
+        gql_query = '''
+                query GetPerson {
+                    person {
+                        id
+                        name
+                    }
+                }
+            '''
+
+        result = schema.executor().execute(gql_query)
+        assert person_id == uuid.UUID(result.data["person"]["id"])
```

### Comparing `sqlalchemy-gql-1.3.8/tests/test_relay_base.py` & `sqlalchemy-gql-1.3.9/tests/test_relay_base.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-gql-1.3.8/tests/test_sqlalachemy_orm.py` & `sqlalchemy-gql-1.3.9/tests/test_sqlalachemy_orm.py`

 * *Files identical despite different names*

