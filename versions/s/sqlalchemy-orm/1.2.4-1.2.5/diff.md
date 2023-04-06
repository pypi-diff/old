# Comparing `tmp/sqlalchemy-orm-1.2.4.tar.gz` & `tmp/sqlalchemy-orm-1.2.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sqlalchemy-orm-1.2.4.tar", last modified: Wed Feb  1 23:54:30 2023, max compression
+gzip compressed data, was "sqlalchemy-orm-1.2.5.tar", last modified: Thu Apr  6 23:15:31 2023, max compression
```

## Comparing `sqlalchemy-orm-1.2.4.tar` & `sqlalchemy-orm-1.2.5.tar`

### file list

```diff
@@ -1,45 +1,45 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-01 23:54:30.506936 sqlalchemy-orm-1.2.4/
--rwxrwxrwx   0 root         (0) root         (0)     1069 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/LICENSE
--rwxrwxrwx   0 root         (0) root         (0)       33 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1704 2023-02-01 23:54:30.506936 sqlalchemy-orm-1.2.4/PKG-INFO
--rwxrwxrwx   0 root         (0) root         (0)     1036 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/README.md
--rw-rw-rw-   0 root         (0) root         (0)        6 2023-02-01 23:54:29.000000 sqlalchemy-orm-1.2.4/VERSION
--rwxrwxrwx   0 root         (0) root         (0)       79 2023-02-01 23:54:30.507936 sqlalchemy-orm-1.2.4/setup.cfg
--rwxrwxrwx   0 root         (0) root         (0)     1360 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-01 23:54:30.499935 sqlalchemy-orm-1.2.4/sqlalchemy_orm/
--rw-rw-rw-   0 root         (0) root         (0)      212 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-01 23:54:30.502936 sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/
--rwxrwxrwx   0 root         (0) root         (0)        0 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     1184 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/base.py
--rwxrwxrwx   0 root         (0) root         (0)     4581 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/helper.py
--rwxrwxrwx   0 root         (0) root         (0)      655 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/inheritance.py
--rwxrwxrwx   0 root         (0) root         (0)     9913 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/mapper.py
--rw-rw-rw-   0 root         (0) root         (0)     1778 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/custom_types.py
--rw-rw-rw-   0 root         (0) root         (0)     6381 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/database.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-01 23:54:30.505936 sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/
--rw-rw-rw-   0 root         (0) root         (0)        0 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)      777 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/cst.py
--rw-rw-rw-   0 root         (0) root         (0)     1325 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/helpers.py
--rw-rw-rw-   0 root         (0) root         (0)    10433 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/main.py
--rw-rw-rw-   0 root         (0) root         (0)     6250 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/models.py
--rw-rw-rw-   0 root         (0) root         (0)     5233 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/parser.py
--rw-rw-rw-   0 root         (0) root         (0)     2771 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/sqla.py
--rw-rw-rw-   0 root         (0) root         (0)       18 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/version.py
--rwxrwxrwx   0 root         (0) root         (0)     1430 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/filter.py
--rwxrwxrwx   0 root         (0) root         (0)     1319 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/order_by.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-01 23:54:30.506936 sqlalchemy-orm-1.2.4/sqlalchemy_orm/patterns/
--rwxrwxrwx   0 root         (0) root         (0)        0 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/patterns/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     2278 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/patterns/tag.py
--rwxrwxrwx   0 root         (0) root         (0)     1250 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/patterns/tag_mixin.py
--rwxrwxrwx   0 root         (0) root         (0)      143 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/patterns/taggable.py
--rw-rw-rw-   0 root         (0) root         (0)     4982 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/proxy.py
--rw-rw-rw-   0 root         (0) root         (0)      953 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/query.py
--rw-rw-rw-   0 root         (0) root         (0)      266 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/session.py
--rw-rw-rw-   0 root         (0) root         (0)     2300 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/typemapper.py
--rw-rw-rw-   0 root         (0) root         (0)     1496 2023-02-01 23:54:21.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-02-01 23:54:30.500935 sqlalchemy-orm-1.2.4/sqlalchemy_orm.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1704 2023-02-01 23:54:30.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1081 2023-02-01 23:54:30.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-02-01 23:54:30.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       93 2023-02-01 23:54:30.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       15 2023-02-01 23:54:30.000000 sqlalchemy-orm-1.2.4/sqlalchemy_orm.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:15:31.684888 sqlalchemy-orm-1.2.5/
+-rwxrwxrwx   0 root         (0) root         (0)     1069 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/LICENSE
+-rwxrwxrwx   0 root         (0) root         (0)       33 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1704 2023-04-06 23:15:31.684888 sqlalchemy-orm-1.2.5/PKG-INFO
+-rwxrwxrwx   0 root         (0) root         (0)     1036 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/README.md
+-rw-rw-rw-   0 root         (0) root         (0)        6 2023-04-06 23:15:31.000000 sqlalchemy-orm-1.2.5/VERSION
+-rwxrwxrwx   0 root         (0) root         (0)       79 2023-04-06 23:15:31.684888 sqlalchemy-orm-1.2.5/setup.cfg
+-rwxrwxrwx   0 root         (0) root         (0)     1360 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:15:31.676888 sqlalchemy-orm-1.2.5/sqlalchemy_orm/
+-rw-rw-rw-   0 root         (0) root         (0)      212 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:15:31.680888 sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/
+-rwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     1184 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/base.py
+-rwxrwxrwx   0 root         (0) root         (0)     4581 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/helper.py
+-rwxrwxrwx   0 root         (0) root         (0)      655 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/inheritance.py
+-rwxrwxrwx   0 root         (0) root         (0)     9913 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/mapper.py
+-rw-rw-rw-   0 root         (0) root         (0)     1778 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/custom_types.py
+-rw-rw-rw-   0 root         (0) root         (0)     6381 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/database.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:15:31.682888 sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)      777 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/cst.py
+-rw-rw-rw-   0 root         (0) root         (0)     1325 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/helpers.py
+-rw-rw-rw-   0 root         (0) root         (0)    10433 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/main.py
+-rw-rw-rw-   0 root         (0) root         (0)     6250 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/models.py
+-rw-rw-rw-   0 root         (0) root         (0)     5233 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/parser.py
+-rw-rw-rw-   0 root         (0) root         (0)     2771 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/sqla.py
+-rw-rw-rw-   0 root         (0) root         (0)       18 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/version.py
+-rwxrwxrwx   0 root         (0) root         (0)     1430 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/filter.py
+-rwxrwxrwx   0 root         (0) root         (0)     1319 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/order_by.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:15:31.683888 sqlalchemy-orm-1.2.5/sqlalchemy_orm/patterns/
+-rwxrwxrwx   0 root         (0) root         (0)        0 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/patterns/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     3855 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/patterns/tag.py
+-rwxrwxrwx   0 root         (0) root         (0)     1814 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/patterns/tag_mixin.py
+-rwxrwxrwx   0 root         (0) root         (0)      143 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/patterns/taggable.py
+-rw-rw-rw-   0 root         (0) root         (0)     4982 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/proxy.py
+-rw-rw-rw-   0 root         (0) root         (0)      953 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/query.py
+-rw-rw-rw-   0 root         (0) root         (0)      266 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/session.py
+-rw-rw-rw-   0 root         (0) root         (0)     2351 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/typemapper.py
+-rw-rw-rw-   0 root         (0) root         (0)     1496 2023-04-06 23:15:21.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 23:15:31.678888 sqlalchemy-orm-1.2.5/sqlalchemy_orm.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1704 2023-04-06 23:15:31.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1081 2023-04-06 23:15:31.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 23:15:31.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       93 2023-04-06 23:15:31.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       15 2023-04-06 23:15:31.000000 sqlalchemy-orm-1.2.5/sqlalchemy_orm.egg-info/top_level.txt
```

### Comparing `sqlalchemy-orm-1.2.4/LICENSE` & `sqlalchemy-orm-1.2.5/LICENSE`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/PKG-INFO` & `sqlalchemy-orm-1.2.5/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: sqlalchemy-orm
-Version: 1.2.4
+Version: 1.2.5
 Summary: Data Relation Mapping framework for Python.
 Home-page: https://gitlab.com/parob/sqlalchemy-orm
-Download-URL: https://gitlab.com/parob/sqlalchemy-orm/-/archive/v1.2.4/sqlalchemy-orm-v1.2.4.tar.gz
+Download-URL: https://gitlab.com/parob/sqlalchemy-orm/-/archive/v1.2.5/sqlalchemy-orm-v1.2.5.tar.gz
 Author: Robert Parker
 Author-email: rob@parob.com
 License: MIT
 Keywords: SQLAlchemy,ORM
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `sqlalchemy-orm-1.2.4/README.md` & `sqlalchemy-orm-1.2.5/README.md`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/setup.py` & `sqlalchemy-orm-1.2.5/setup.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/base.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/base.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/helper.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/helper.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/inheritance.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/inheritance.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/base/mapper.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/base/mapper.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/custom_types.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/custom_types.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/database.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/database.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/cst.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/cst.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/helpers.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/helpers.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/main.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/main.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/models.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/models.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/parser.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/parser.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/eralchemy/sqla.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/eralchemy/sqla.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/filter.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/filter.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/order_by.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/order_by.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/patterns/tag_mixin.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/patterns/tag_mixin.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,46 +1,65 @@
 import uuid
+from typing import List
 
+from sqlalchemy import ForeignKey
 from sqlalchemy.ext.associationproxy import association_proxy
-from sqlalchemy.orm import relationship
+from sqlalchemy.orm import relationship, mapped_column
 from sqlalchemy.orm.decl_api import declared_attr
 
 from sqlalchemy_orm.base.helper import HelperBase
 from sqlalchemy_orm.patterns.taggable import Taggable
-from sqlalchemy_orm.utils import Memoized
 
 
 class TagMixin(Taggable):
 
+    cached_tag_class = None
+
     @classmethod
-    @Memoized
     def tag_cls(cls):
+        if cls.cached_tag_class is not None:
+            return cls.cached_tag_class
+
         if not issubclass(cls, HelperBase):
             raise TypeError(
                 f"TagMixin class {cls} must be a subclass of {HelperBase}."
             )
 
+        parent_table = cls.__tablename__
+        primary_key = cls.primary_keys()[0].name
+
         class Tag(cls.declarative_base):
             id: str = uuid.uuid4
             tag: str
-            parent: cls = None
+            parent_id = mapped_column(
+                ForeignKey(f"{parent_table}.{primary_key}")
+            )
+            parent = relationship(cls)
 
             __tablename__ = cls.__tablename__ + '_tag'
             __inheritance__ = False
+            __parent_cls__ = cls
 
         Tag.__name__ = cls.__name__ + Tag.__name__
+        Tag.__qualname__ = Tag.__name__
         Tag.__module__ = cls.__module__ + Tag.__module__
+        cls.cached_tag_class = Tag
 
         return Tag
 
     @declared_attr
-    def tags_relationship(self):
-        Tag = self.tag_cls()
-        return relationship(Tag, cascade="all, delete, delete-orphan")
+    def tag_objects(self):
+        tag_class = self.tag_cls()
+        return relationship(
+            tag_class,
+            back_populates='parent',
+            cascade="all, delete, delete-orphan",
+            lazy='dynamic'
+        )
 
     @declared_attr
-    def tags(self):
+    def tags(self) -> List[str]:
         return association_proxy(
-            'tags_relationship',
+            'tag_objects',
             'tag',
             creator=lambda tag: self.tag_cls()(tag=tag)
         )
```

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/proxy.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/proxy.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/query.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/query.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/typemapper.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/typemapper.py`

 * *Files 2% similar despite different names*

```diff
@@ -43,14 +43,16 @@
                 python_type = type_obj.python_type
 
             except (NotImplementedError, AssertionError, TypeError):
                 if type_ in types:
                     raise TypeError(
                         f"Custom type '{type}' did not specify a Python type"
                     )
+            except Exception:
+                pass
             else:
                 type_map = self.type_map
                 if python_type not in type_map.keys() or \
                         issubclass(type_map[python_type].__class__, type_):
                     self.type_map[python_type] = type_obj
                 elif type_obj in self.type_map.values():
                     raise TypeError(
```

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm/utils.py` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm/utils.py`

 * *Files identical despite different names*

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm.egg-info/PKG-INFO` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: sqlalchemy-orm
-Version: 1.2.4
+Version: 1.2.5
 Summary: Data Relation Mapping framework for Python.
 Home-page: https://gitlab.com/parob/sqlalchemy-orm
-Download-URL: https://gitlab.com/parob/sqlalchemy-orm/-/archive/v1.2.4/sqlalchemy-orm-v1.2.4.tar.gz
+Download-URL: https://gitlab.com/parob/sqlalchemy-orm/-/archive/v1.2.5/sqlalchemy-orm-v1.2.5.tar.gz
 Author: Robert Parker
 Author-email: rob@parob.com
 License: MIT
 Keywords: SQLAlchemy,ORM
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `sqlalchemy-orm-1.2.4/sqlalchemy_orm.egg-info/SOURCES.txt` & `sqlalchemy-orm-1.2.5/sqlalchemy_orm.egg-info/SOURCES.txt`

 * *Files identical despite different names*

