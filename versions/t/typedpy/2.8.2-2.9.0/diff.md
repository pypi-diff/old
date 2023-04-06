# Comparing `tmp/typedpy-2.8.2.tar.gz` & `tmp/typedpy-2.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "typedpy-2.8.2.tar", last modified: Wed Dec 15 14:23:19 2021, max compression
+gzip compressed data, was "typedpy-2.9.0.tar", last modified: Sat Dec 25 04:20:43 2021, max compression
```

## Comparing `typedpy-2.8.2.tar` & `typedpy-2.9.0.tar`

### file list

```diff
@@ -1,25 +1,25 @@
-drwxrwxr-x   0 dannyloya  (1000) dannyloya  (1000)        0 2021-12-15 14:23:19.639522 typedpy-2.8.2/
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     1057 2020-05-12 01:12:02.000000 typedpy-2.8.2/LICENSE.txt
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     3386 2021-12-15 14:23:19.639522 typedpy-2.8.2/PKG-INFO
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     2549 2021-07-17 20:40:01.000000 typedpy-2.8.2/README.md
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)      621 2021-12-15 14:23:19.640522 typedpy-2.8.2/setup.cfg
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     1278 2021-12-15 14:15:24.000000 typedpy-2.8.2/setup.py
-drwxrwxr-x   0 dannyloya  (1000) dannyloya  (1000)        0 2021-12-15 14:23:19.638522 typedpy-2.8.2/typedpy/
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     2045 2021-12-15 13:30:52.000000 typedpy-2.8.2/typedpy/__init__.py
--rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     1166 2021-12-08 14:14:59.000000 typedpy-2.8.2/typedpy/commons.py
--rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     2797 2021-06-14 12:56:26.000000 typedpy-2.8.2/typedpy/errors.py
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     6030 2021-11-19 03:36:37.000000 typedpy-2.8.2/typedpy/extfields.py
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)    55687 2021-11-19 03:36:01.000000 typedpy-2.8.2/typedpy/fields.py
--rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)    21874 2021-12-13 00:01:54.000000 typedpy-2.8.2/typedpy/json_schema_mapping.py
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     8393 2021-11-30 02:47:40.000000 typedpy-2.8.2/typedpy/mappers.py
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)    29680 2021-11-30 02:47:40.000000 typedpy-2.8.2/typedpy/serialization.py
--rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     8725 2021-11-19 03:59:39.000000 typedpy-2.8.2/typedpy/serialization_wrappers.py
--rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)    50598 2021-12-15 14:11:30.000000 typedpy-2.8.2/typedpy/structures.py
--rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     9288 2021-12-15 13:30:52.000000 typedpy-2.8.2/typedpy/structures_reuse.py
--rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     1708 2021-06-27 19:46:11.000000 typedpy-2.8.2/typedpy/utility.py
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     2306 2021-11-24 02:28:49.000000 typedpy-2.8.2/typedpy/versioned_mapping.py
-drwxrwxr-x   0 dannyloya  (1000) dannyloya  (1000)        0 2021-12-15 14:23:19.639522 typedpy-2.8.2/typedpy.egg-info/
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     3386 2021-12-15 14:23:19.000000 typedpy-2.8.2/typedpy.egg-info/PKG-INFO
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)      467 2021-12-15 14:23:19.000000 typedpy-2.8.2/typedpy.egg-info/SOURCES.txt
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)        1 2021-12-15 14:23:19.000000 typedpy-2.8.2/typedpy.egg-info/dependency_links.txt
--rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)        8 2021-12-15 14:23:19.000000 typedpy-2.8.2/typedpy.egg-info/top_level.txt
+drwxrwxr-x   0 dannyloya  (1000) dannyloya  (1000)        0 2021-12-25 04:20:43.995971 typedpy-2.9.0/
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     1057 2020-05-12 01:12:02.000000 typedpy-2.9.0/LICENSE.txt
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     3386 2021-12-25 04:20:43.995971 typedpy-2.9.0/PKG-INFO
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     2549 2021-07-17 20:40:01.000000 typedpy-2.9.0/README.md
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)      621 2021-12-25 04:20:43.995971 typedpy-2.9.0/setup.cfg
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     1278 2021-12-25 04:16:16.000000 typedpy-2.9.0/setup.py
+drwxrwxr-x   0 dannyloya  (1000) dannyloya  (1000)        0 2021-12-25 04:20:43.994971 typedpy-2.9.0/typedpy/
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     2045 2021-12-15 13:30:52.000000 typedpy-2.9.0/typedpy/__init__.py
+-rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     1166 2021-12-08 14:14:59.000000 typedpy-2.9.0/typedpy/commons.py
+-rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     2797 2021-06-14 12:56:26.000000 typedpy-2.9.0/typedpy/errors.py
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     6030 2021-11-19 03:36:37.000000 typedpy-2.9.0/typedpy/extfields.py
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)    55687 2021-11-19 03:36:01.000000 typedpy-2.9.0/typedpy/fields.py
+-rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)    21874 2021-12-13 00:01:54.000000 typedpy-2.9.0/typedpy/json_schema_mapping.py
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     8393 2021-11-30 02:47:40.000000 typedpy-2.9.0/typedpy/mappers.py
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)    30050 2021-12-25 04:03:15.000000 typedpy-2.9.0/typedpy/serialization.py
+-rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     8725 2021-11-19 03:59:39.000000 typedpy-2.9.0/typedpy/serialization_wrappers.py
+-rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)    50917 2021-12-24 19:44:07.000000 typedpy-2.9.0/typedpy/structures.py
+-rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     9298 2021-12-17 13:27:29.000000 typedpy-2.9.0/typedpy/structures_reuse.py
+-rw-r--r--   0 dannyloya  (1000) dannyloya  (1000)     1708 2021-06-27 19:46:11.000000 typedpy-2.9.0/typedpy/utility.py
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     2306 2021-11-24 02:28:49.000000 typedpy-2.9.0/typedpy/versioned_mapping.py
+drwxrwxr-x   0 dannyloya  (1000) dannyloya  (1000)        0 2021-12-25 04:20:43.995971 typedpy-2.9.0/typedpy.egg-info/
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)     3386 2021-12-25 04:20:43.000000 typedpy-2.9.0/typedpy.egg-info/PKG-INFO
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)      467 2021-12-25 04:20:43.000000 typedpy-2.9.0/typedpy.egg-info/SOURCES.txt
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)        1 2021-12-25 04:20:43.000000 typedpy-2.9.0/typedpy.egg-info/dependency_links.txt
+-rw-rw-r--   0 dannyloya  (1000) dannyloya  (1000)        8 2021-12-25 04:20:43.000000 typedpy-2.9.0/typedpy.egg-info/top_level.txt
```

### Comparing `typedpy-2.8.2/LICENSE.txt` & `typedpy-2.9.0/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/PKG-INFO` & `typedpy-2.9.0/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: typedpy
-Version: 2.8.2
+Version: 2.9.0
 Summary: Type-safe Python
 Home-page: http://github.com/loyada/typedpy
 Author: Danny Loya
 Author-email: dan.loya@gmail.com
 License: MIT
-Download-URL: https://github.com/loyada/typedpy/archive/v2.8.2.tar.gz
+Download-URL: https://github.com/loyada/typedpy/archive/v2.9.0.tar.gz
 Keywords: testing,type-safe,strict,schema,validation
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
```

### Comparing `typedpy-2.8.2/README.md` & `typedpy-2.9.0/README.md`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/setup.cfg` & `typedpy-2.9.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/setup.py` & `typedpy-2.9.0/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -25,17 +25,17 @@
     author_email="dan.loya@gmail.com",
     classifiers=classifiers,
     description="Type-safe Python",
     long_description_content_type="text/markdown",
     license="MIT",
     long_description=long_description,
     url="http://github.com/loyada/typedpy",
-    download_url ="https://github.com/loyada/typedpy/archive/v2.8.2.tar.gz",
+    download_url ="https://github.com/loyada/typedpy/archive/v2.9.0.tar.gz",
     keywords=['testing', 'type-safe', 'strict', 'schema', 'validation'],
-    version='2.8.2'
+    version='2.9.0'
 )
 
 # coverage run --source=typedpy/ setup.py test
 # coverage html
 # load in browser from coverage_html_report
 
 # pylint --rcfile=setup.cfg typedpy
```

### Comparing `typedpy-2.8.2/typedpy/__init__.py` & `typedpy-2.9.0/typedpy/__init__.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy/commons.py` & `typedpy-2.9.0/typedpy/commons.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy/errors.py` & `typedpy-2.9.0/typedpy/errors.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy/extfields.py` & `typedpy-2.9.0/typedpy/extfields.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy/fields.py` & `typedpy-2.9.0/typedpy/fields.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy/json_schema_mapping.py` & `typedpy-2.9.0/typedpy/json_schema_mapping.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy/mappers.py` & `typedpy-2.9.0/typedpy/mappers.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy/serialization.py` & `typedpy-2.9.0/typedpy/serialization.py`

 * *Files 0% similar despite different names*

```diff
@@ -821,14 +821,20 @@
                 result[mapped_key] = serialize_val(
                     the_field_definition,
                     key,
                     mapped_value or val,
                     mapper=sub_mapper,
                     camel_case_convert=camel_case_convert,
                 )
+    if getattr(structure, "_additional_serialization", None):
+        additional_props = structure._additional_serialization()
+        if not isinstance(additional_props, dict):
+            raise TypeError("_additional_serialization must return a dict")
+        for key, value in additional_props.items():
+            result[key] = value() if callable(value) else value
     return result
 
 
 def serialize(value, *, mapper: Dict = None, compact=False, camel_case_convert=False):
     """
     Serialize an instance of :class:`Structure` to a JSON-like dict.
```

### Comparing `typedpy-2.8.2/typedpy/serialization_wrappers.py` & `typedpy-2.9.0/typedpy/serialization_wrappers.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy/structures.py` & `typedpy-2.9.0/typedpy/structures.py`

 * *Files 1% similar despite different names*

```diff
@@ -981,14 +981,23 @@
 
     def __bool__(self):
         internal_props = ["_instantiated"]
         return any(
             v is not None for k, v in self.__dict__.items() if k not in internal_props
         )
 
+    def _additional_serialization(self) -> dict:
+        """
+        :return: additional fields when serializing a structure,
+            Each key is a key in the output json, and each value
+            can either be a function with no parameters, a method, or a
+            simple value
+        """
+        return {}
+
     @classmethod
     def get_all_fields_by_name(cls):
         return _get_all_fields_by_name(cls)
 
     @classmethod
     def get_aggregated_serialization_mapper(cls):
         return _get_all_values_of_attribute(cls, SERIALIZATION_MAPPER)
```

### Comparing `typedpy-2.8.2/typedpy/structures_reuse.py` & `typedpy-2.9.0/typedpy/structures_reuse.py`

 * *Files 1% similar despite different names*

```diff
@@ -84,15 +84,15 @@
                     or not isinstance(clazz[1], str)
                 )
             ):
                 raise TypeError(
                     "Partial must have a Structure class as a parameter, and an optional name for the class"
                 )
         clazz, classname = (
-            clazz if isinstance(clazz, tuple) else (clazz, f"Partial{clazz.__name__}")
+            clazz if isinstance(clazz, tuple) else (clazz, f"AllFieldsRequired{clazz.__name__}")
         )
 
         cls_dict = _init_class_dict(clazz)
         cls_dict[REQUIRED_FIELDS] = []
         for k, v in clazz.get_all_fields_by_name().items():
             cls_dict[k] = v
             if getattr(v, "_default") is None:
```

### Comparing `typedpy-2.8.2/typedpy/utility.py` & `typedpy-2.9.0/typedpy/utility.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy/versioned_mapping.py` & `typedpy-2.9.0/typedpy/versioned_mapping.py`

 * *Files identical despite different names*

### Comparing `typedpy-2.8.2/typedpy.egg-info/PKG-INFO` & `typedpy-2.9.0/typedpy.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: typedpy
-Version: 2.8.2
+Version: 2.9.0
 Summary: Type-safe Python
 Home-page: http://github.com/loyada/typedpy
 Author: Danny Loya
 Author-email: dan.loya@gmail.com
 License: MIT
-Download-URL: https://github.com/loyada/typedpy/archive/v2.8.2.tar.gz
+Download-URL: https://github.com/loyada/typedpy/archive/v2.9.0.tar.gz
 Keywords: testing,type-safe,strict,schema,validation
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
```

