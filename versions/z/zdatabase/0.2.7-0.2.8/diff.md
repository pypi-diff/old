# Comparing `tmp/zdatabase-0.2.7.tar.gz` & `tmp/zdatabase-0.2.8.tar.gz`

## Comparing `zdatabase-0.2.7.tar` & `zdatabase-0.2.8.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0      672 2020-02-02 00:00:00.000000 zdatabase-0.2.7/src/zdatabase/__init__.py
--rw-r--r--   0        0        0     2647 2020-02-02 00:00:00.000000 zdatabase-0.2.7/src/zdatabase/model.py
--rw-r--r--   0        0        0     5421 2020-02-02 00:00:00.000000 zdatabase-0.2.7/src/zdatabase/utility.py
--rw-r--r--   0        0        0       10 2020-02-02 00:00:00.000000 zdatabase-0.2.7/.gitignore
--rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 zdatabase-0.2.7/LICENSE
--rw-r--r--   0        0        0       31 2020-02-02 00:00:00.000000 zdatabase-0.2.7/README.md
--rw-r--r--   0        0        0      669 2020-02-02 00:00:00.000000 zdatabase-0.2.7/pyproject.toml
--rw-r--r--   0        0        0      624 2020-02-02 00:00:00.000000 zdatabase-0.2.7/PKG-INFO
+-rw-r--r--   0        0        0      672 2020-02-02 00:00:00.000000 zdatabase-0.2.8/src/zdatabase/__init__.py
+-rw-r--r--   0        0        0     2647 2020-02-02 00:00:00.000000 zdatabase-0.2.8/src/zdatabase/model.py
+-rw-r--r--   0        0        0     5625 2020-02-02 00:00:00.000000 zdatabase-0.2.8/src/zdatabase/utility.py
+-rw-r--r--   0        0        0       10 2020-02-02 00:00:00.000000 zdatabase-0.2.8/.gitignore
+-rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 zdatabase-0.2.8/LICENSE
+-rw-r--r--   0        0        0       31 2020-02-02 00:00:00.000000 zdatabase-0.2.8/README.md
+-rw-r--r--   0        0        0      669 2020-02-02 00:00:00.000000 zdatabase-0.2.8/pyproject.toml
+-rw-r--r--   0        0        0      624 2020-02-02 00:00:00.000000 zdatabase-0.2.8/PKG-INFO
```

### Comparing `zdatabase-0.2.7/src/zdatabase/__init__.py` & `zdatabase-0.2.8/src/zdatabase/__init__.py`

 * *Files identical despite different names*

### Comparing `zdatabase-0.2.7/src/zdatabase/model.py` & `zdatabase-0.2.8/src/zdatabase/model.py`

 * *Files identical despite different names*

### Comparing `zdatabase-0.2.7/src/zdatabase/utility.py` & `zdatabase-0.2.8/src/zdatabase/utility.py`

 * *Files 4% similar despite different names*

```diff
@@ -191,10 +191,18 @@
     @classmethod
     def get_attrs_(cls, attr_names, **kwargs):
         flts = cls.make_flts(**kwargs)
         attrs = [getattr(cls, attr_name) for attr_name in attr_names]
         return cls.query_(*attrs).filter(*flts).all()
 
     @classmethod
+    def get_map_(cls, attr_names):
+        rst_map = {}
+        for item in cls.get_attrs_(attr_names):
+            a, b = item
+            rst_map[a] = b
+        return rst_map
+
+    @classmethod
     def delete_list_(cls, **kwargs):
         cls.make_query(**kwargs).delete(synchronize_session=False)
         cls.commit()
```

### Comparing `zdatabase-0.2.7/LICENSE` & `zdatabase-0.2.8/LICENSE`

 * *Files identical despite different names*

### Comparing `zdatabase-0.2.7/pyproject.toml` & `zdatabase-0.2.8/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "zdatabase"
-version = "0.2.7"
+version = "0.2.8"
 authors = [
   { name="inspirare6", email="inspirare6@163.com" },
 ]
 description = "zen database library"
 readme = "README.md"
 requires-python = ">=3.7"
 dependencies = [
```

### Comparing `zdatabase-0.2.7/PKG-INFO` & `zdatabase-0.2.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: zdatabase
-Version: 0.2.7
+Version: 0.2.8
 Summary: zen database library
 Project-URL: Homepage, https://github.com/inspirare6/zdatabase
 Project-URL: Bug Tracker, https://github.com/inspirare6/zdatabase/issues
 Author-email: inspirare6 <inspirare6@163.com>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

