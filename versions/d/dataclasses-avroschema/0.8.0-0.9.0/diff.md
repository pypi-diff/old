# Comparing `tmp/dataclasses-avroschema-0.8.0.tar.gz` & `tmp/dataclasses-avroschema-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/dataclasses-avroschema-0.8.0.tar", last modified: Mon Jan  6 20:51:00 2020, max compression
+gzip compressed data, was "dist/dataclasses-avroschema-0.9.0.tar", last modified: Fri Jan 24 14:01:45 2020, max compression
```

## Comparing `dataclasses-avroschema-0.8.0.tar` & `dataclasses-avroschema-0.9.0.tar`

### file list

```diff
@@ -1,24 +1,25 @@
-drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-06 20:51:00.000000 dataclasses-avroschema-0.8.0/
--rw-r--r--   0 marcos     (501) staff       (20)     3111 2020-01-06 20:51:00.000000 dataclasses-avroschema-0.8.0/PKG-INFO
--rw-r--r--   0 marcos     (501) staff       (20)     2098 2020-01-06 20:49:26.000000 dataclasses-avroschema-0.8.0/README.md
-drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-06 20:51:00.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema/
--rw-r--r--   0 marcos     (501) staff       (20)        0 2019-06-25 16:57:46.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema/__init__.py
--rw-r--r--   0 marcos     (501) staff       (20)    17849 2020-01-06 20:49:26.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema/fields.py
--rw-r--r--   0 marcos     (501) staff       (20)     4452 2019-11-15 14:17:12.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema/schema_definition.py
--rw-r--r--   0 marcos     (501) staff       (20)     1848 2019-11-15 23:33:06.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema/schema_generator.py
--rw-r--r--   0 marcos     (501) staff       (20)      851 2019-11-21 15:03:19.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema/utils.py
-drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-06 20:51:00.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema.egg-info/
--rw-r--r--   0 marcos     (501) staff       (20)     3111 2020-01-06 20:50:59.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema.egg-info/PKG-INFO
--rw-r--r--   0 marcos     (501) staff       (20)      589 2020-01-06 20:51:00.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema.egg-info/SOURCES.txt
--rw-r--r--   0 marcos     (501) staff       (20)        1 2020-01-06 20:50:59.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema.egg-info/dependency_links.txt
--rw-r--r--   0 marcos     (501) staff       (20)       15 2020-01-06 20:50:59.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema.egg-info/requires.txt
--rw-r--r--   0 marcos     (501) staff       (20)       29 2020-01-06 20:50:59.000000 dataclasses-avroschema-0.8.0/dataclasses_avroschema.egg-info/top_level.txt
--rw-r--r--   0 marcos     (501) staff       (20)       38 2020-01-06 20:51:00.000000 dataclasses-avroschema-0.8.0/setup.cfg
--rw-r--r--   0 marcos     (501) staff       (20)      989 2020-01-06 20:50:02.000000 dataclasses-avroschema-0.8.0/setup.py
-drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-06 20:51:00.000000 dataclasses-avroschema-0.8.0/tests/
-drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-06 20:51:00.000000 dataclasses-avroschema-0.8.0/tests/fields/
--rw-r--r--   0 marcos     (501) staff       (20)        0 2019-11-16 13:23:11.000000 dataclasses-avroschema-0.8.0/tests/fields/__init__.py
--rw-r--r--   0 marcos     (501) staff       (20)     3168 2020-01-06 20:49:26.000000 dataclasses-avroschema-0.8.0/tests/fields/consts.py
--rw-r--r--   0 marcos     (501) staff       (20)     9731 2019-11-21 15:03:19.000000 dataclasses-avroschema-0.8.0/tests/fields/test_complex_types.py
--rw-r--r--   0 marcos     (501) staff       (20)     3313 2019-11-16 13:23:11.000000 dataclasses-avroschema-0.8.0/tests/fields/test_logical_types.py
--rw-r--r--   0 marcos     (501) staff       (20)     1613 2019-11-16 13:23:11.000000 dataclasses-avroschema-0.8.0/tests/fields/test_primitive_types.py
+drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/
+-rw-r--r--   0 marcos     (501) staff       (20)     3109 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/PKG-INFO
+-rw-r--r--   0 marcos     (501) staff       (20)     2098 2020-01-06 20:49:26.000000 dataclasses-avroschema-0.9.0/README.md
+drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema/
+-rw-r--r--   0 marcos     (501) staff       (20)        0 2019-06-25 16:57:46.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema/__init__.py
+-rw-r--r--   0 marcos     (501) staff       (20)    18972 2020-01-24 13:59:46.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema/fields.py
+-rw-r--r--   0 marcos     (501) staff       (20)     4559 2020-01-24 13:59:46.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema/schema_definition.py
+-rw-r--r--   0 marcos     (501) staff       (20)     1830 2020-01-24 13:59:46.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema/schema_generator.py
+-rw-r--r--   0 marcos     (501) staff       (20)      923 2020-01-24 13:59:46.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema/utils.py
+drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema.egg-info/
+-rw-r--r--   0 marcos     (501) staff       (20)     3109 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema.egg-info/PKG-INFO
+-rw-r--r--   0 marcos     (501) staff       (20)      620 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema.egg-info/SOURCES.txt
+-rw-r--r--   0 marcos     (501) staff       (20)        1 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema.egg-info/dependency_links.txt
+-rw-r--r--   0 marcos     (501) staff       (20)       15 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema.egg-info/requires.txt
+-rw-r--r--   0 marcos     (501) staff       (20)       29 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/dataclasses_avroschema.egg-info/top_level.txt
+-rw-r--r--   0 marcos     (501) staff       (20)       38 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/setup.cfg
+-rw-r--r--   0 marcos     (501) staff       (20)      987 2020-01-24 14:00:48.000000 dataclasses-avroschema-0.9.0/setup.py
+drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/tests/
+drwxr-xr-x   0 marcos     (501) staff       (20)        0 2020-01-24 14:01:45.000000 dataclasses-avroschema-0.9.0/tests/fields/
+-rw-r--r--   0 marcos     (501) staff       (20)        0 2019-11-16 13:23:11.000000 dataclasses-avroschema-0.9.0/tests/fields/__init__.py
+-rw-r--r--   0 marcos     (501) staff       (20)     3168 2020-01-24 13:59:46.000000 dataclasses-avroschema-0.9.0/tests/fields/consts.py
+-rw-r--r--   0 marcos     (501) staff       (20)     1704 2020-01-24 12:44:05.000000 dataclasses-avroschema-0.9.0/tests/fields/test_BaseField.py
+-rw-r--r--   0 marcos     (501) staff       (20)     9731 2020-01-24 13:59:46.000000 dataclasses-avroschema-0.9.0/tests/fields/test_complex_types.py
+-rw-r--r--   0 marcos     (501) staff       (20)     3314 2020-01-24 13:59:46.000000 dataclasses-avroschema-0.9.0/tests/fields/test_logical_types.py
+-rw-r--r--   0 marcos     (501) staff       (20)     1614 2020-01-24 13:59:46.000000 dataclasses-avroschema-0.9.0/tests/fields/test_primitive_types.py
```

### Comparing `dataclasses-avroschema-0.8.0/PKG-INFO` & `dataclasses-avroschema-0.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: dataclasses-avroschema
-Version: 0.8.0
+Version: 0.9.0
 Summary: Generate Avro Schemas from a Python class
 Home-page: https://github.com/marcosschroh/dataclasses-avroschema
 Author: Marcos Schroh
 Author-email: schrohm@gmail.com
-License: GPLv3
+License: MIT
 Description: # Dataclasses Avro Schema Generator
         
         Generate [Avro](https://avro.apache.org/docs/1.8.2/spec.html) Schemas from a Python class
         
         [![Build Status](https://travis-ci.org/marcosschroh/dataclasses-avroschema.svg?branch=master)](https://travis-ci.org//dataclasses-avroschema)
         [![GitHub license](https://img.shields.io/github/license/marcosschroh/dataclasses-avroschema.svg)](https://github.com/marcosschroh/dataclasses-avroschema/blob/master/LICENSE)
         [![codecov](https://codecov.io/gh/marcosschroh/dataclasses-avroschema/branch/master/graph/badge.svg)](https://codecov.io/gh/marcosschroh/dataclasses-avroschema)
```

### Comparing `dataclasses-avroschema-0.8.0/README.md` & `dataclasses-avroschema-0.9.0/README.md`

 * *Files identical despite different names*

### Comparing `dataclasses-avroschema-0.8.0/dataclasses_avroschema/fields.py` & `dataclasses-avroschema-0.9.0/dataclasses_avroschema/fields.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,18 @@
-import json
+import abc
+import collections
 import dataclasses
-import typing
-import inflect
 import datetime
+import json
+import typing
 import uuid
-import collections
-
 from collections import OrderedDict
 
+import inflect
+
 from dataclasses_avroschema import schema_generator, utils
 
 p = inflect.engine()
 
 BOOLEAN = "boolean"
 NULL = "null"
 INT = "int"
@@ -27,15 +28,14 @@
 TIMESTAMP_MILLIS = "timestamp-millis"
 UUID = "uuid"
 LOGICAL_DATE = {"type": INT, "logicalType": DATE}
 LOGICAL_TIME = {"type": INT, "logicalType": TIME_MILLIS}
 LOGICAL_DATETIME = {"type": LONG, "logicalType": TIMESTAMP_MILLIS}
 LOGICAL_UUID = {"type": STRING, "logicalType": UUID}
 
-
 PYTHON_TYPE_TO_AVRO = {
     bool: BOOLEAN,
     type(None): NULL,
     int: INT,
     float: FLOAT,
     bytes: BYTES,
     str: STRING,
@@ -60,17 +60,20 @@
 PRIMITIVE_AND_LOGICAL_TYPES = PYTHON_INMUTABLE_TYPES + PYTHON_LOGICAL_TYPES
 
 PythonPrimitiveTypes = typing.Union[str, int, bool, float, list, tuple, dict]
 
 
 @dataclasses.dataclass
 class BaseField:
+    avro_type: typing.ClassVar
+
     name: str
     type: typing.Any  # store the python primitive type
     default: typing.Any = dataclasses.MISSING
+    metadata: typing.Dict = dataclasses.MISSING
 
     @staticmethod
     def _get_self_reference_type(a_type):
         internal_type = a_type.__args__[0]
 
         return internal_type.__forward_arg__
 
@@ -78,14 +81,24 @@
     def get_singular_name(name):
         singular = p.singular_noun(name)
 
         if singular:
             return singular
         return name
 
+    def get_metadata(self) -> typing.List[typing.Tuple[str, str]]:
+        meta_data_for_template = []
+        try:
+            metadata = dict(self.metadata)
+            for name, value in metadata.items():
+                meta_data_for_template.append((name, value))
+        except (ValueError, TypeError):
+            return meta_data_for_template
+        return meta_data_for_template
+
     def render(self) -> OrderedDict:
         """
         Render the fields base on the avro field
 
         At least will have name and type.
 
         returns:
@@ -98,15 +111,17 @@
             The default key is optional.
 
             If self.type is:
                 * list, the OrderedDict will contains the key items inside type
                 * tuple, he OrderedDict will contains the key symbols inside type
                 * dict, he OrderedDict will contains the key values inside type
         """
-        template = OrderedDict([("name", self.name), ("type", self.get_avro_type())])
+        template = OrderedDict(
+            [("name", self.name), ("type", self.get_avro_type())] + self.get_metadata()
+        )
 
         default = self.get_default_value()
         if default is not None:
             template["default"] = default
 
         return template
 
@@ -126,14 +141,18 @@
 
     def to_json(self) -> str:
         return json.dumps(self.render(), indent=2)
 
     def to_dict(self) -> dict:
         return json.loads(self.to_json())
 
+    @abc.abstractmethod
+    def get_avro_type(self):
+        ...  # pragma: no cover
+
 
 class InmutableField(BaseField):
     def get_avro_type(self) -> PythonPrimitiveTypes:
         if self.default is not dataclasses.MISSING:
             if self.default is not None:
                 return [self.avro_type, NULL]
             # means that default value is None
@@ -561,26 +580,48 @@
 
 PRIMITIVE_LOGICAL_TYPES_FIELDS_CLASSES = {
     **INMUTABLE_FIELDS_CLASSES,
     **LOGICAL_TYPES_FIELDS_CLASSES,
 }
 
 
+FieldType = typing.Union[
+    StringField,
+    BooleanField,
+    FloatField,
+    BytesField,
+    NoneField,
+    TupleField,
+    ListField,
+    DictField,
+    UnionField,
+    SelfReferenceField,
+    LogicalTypeField,
+    DateField,
+    TimeField,
+    DatetimeField,
+    UUIDField,
+    RecordField,
+]
+
+
 def field_factory(
     name: str,
     native_type: typing.Any,
     default: typing.Any = dataclasses.MISSING,
     default_factory: typing.Any = dataclasses.MISSING,
-):
-
+    metadata: typing.Dict = dataclasses.MISSING,
+) -> FieldType:
     if native_type in PYTHON_INMUTABLE_TYPES:
         klass = INMUTABLE_FIELDS_CLASSES[native_type]
-        return klass(name=name, type=native_type, default=default)
+        return klass(name=name, type=native_type, default=default, metadata=metadata)
     elif utils.is_self_referenced(native_type):
-        return SelfReferenceField(name=name, type=native_type, default=default)
+        return SelfReferenceField(
+            name=name, type=native_type, default=default, metadata=metadata
+        )
     elif isinstance(native_type, typing._GenericAlias):
         origin = native_type.__origin__
 
         if origin not in (
             tuple,
             list,
             dict,
@@ -598,16 +639,19 @@
 
         klass = CONTAINER_FIELDS_CLASSES[origin]
         return klass(
             name=name,
             type=native_type,
             default=default,
             default_factory=default_factory,
+            metadata=metadata,
         )
     elif native_type in PYTHON_LOGICAL_TYPES:
         klass = LOGICAL_TYPES_FIELDS_CLASSES[native_type]
-        return klass(name=name, type=native_type, default=default)
+        return klass(name=name, type=native_type, default=default, metadata=metadata)
     else:
-        return RecordField(name=name, type=native_type, default=default)
+        return RecordField(
+            name=name, type=native_type, default=default, metadata=metadata
+        )
 
 
 Field = field_factory
```

### Comparing `dataclasses-avroschema-0.8.0/dataclasses_avroschema/schema_definition.py` & `dataclasses-avroschema-0.9.0/dataclasses_avroschema/schema_definition.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,61 +1,64 @@
+import abc
 import dataclasses
 import inspect
 import typing
 from collections import OrderedDict
 
 from dataclasses_avroschema import fields
 
 try:
     import faust
 except ImportError:  # pragma: no cover
     faust = None  # pragma: no cover
 
 
 @dataclasses.dataclass
-class BaseSchemaDefinition:
+class BaseSchemaDefinition(abc.ABC):
     """
     Minimal Schema definition
     """
 
     type: str
-    klass_or_instance: dataclasses.dataclass
+    klass_or_instance: typing.Any
 
+    @abc.abstractmethod
     def get_rendered_fields(self):
-        raise NotImplementedError
+        ...  # pragma: no cover
 
+    @abc.abstractmethod
     def render(self):
-        raise NotImplementedError
+        ...  # pragma: no cover
 
     def get_schema_name(self):
         if inspect.isclass(self.klass_or_instance):
             return self.klass_or_instance.__name__
         return self.klass_or_instance.__class__.__name__
 
     def generate_documentation(self):
         doc = self.klass_or_instance.__doc__
 
         if doc is not None:
             return doc.replace("\n", "")
 
     @property
-    def is_faust_record(self):
+    def is_faust_record(self) -> bool:
         if faust:
             if inspect.isclass(self.klass_or_instance):
                 return issubclass(self.klass_or_instance, faust.Record)
             return issubclass(self.klass_or_instance.__class__, faust.Record)
 
         return False
 
 
 @dataclasses.dataclass
 class AvroSchemaDefinition(BaseSchemaDefinition):
     aliases: typing.List[str] = None
     namespace: str = None
-    fields: typing.List["fields.Field"] = None
+    fields: typing.List["fields.FieldType"] = None
     include_schema_doc: bool = True
 
     def __post_init__(self):
         self.generate_extra_avro_attributes()
         self.fields = self.parse_dataclasses_fields()
 
     def parse_dataclasses_fields(self) -> typing.List["fields.Field"]:
@@ -66,14 +69,15 @@
     def parse_fields(self):
         return [
             fields.Field(
                 dataclass_field.name,
                 dataclass_field.type,
                 dataclass_field.default,
                 dataclass_field.default_factory,
+                dataclass_field.metadata,
             )
             for dataclass_field in dataclasses.fields(self.klass_or_instance)
         ]
 
     def parse_faust_record_fields(self) -> typing.List["fields.Field"]:
         schema_fields = []
```

### Comparing `dataclasses-avroschema-0.8.0/dataclasses_avroschema/schema_generator.py` & `dataclasses-avroschema-0.9.0/dataclasses_avroschema/schema_generator.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,19 +1,19 @@
-import json
 import dataclasses
+import json
 import typing
 
 from dataclasses_avroschema.schema_definition import AvroSchemaDefinition
 
 
 class SchemaGenerator:
     def __init__(self, klass_or_instance, include_schema_doc: bool = True) -> None:
         self.dataclass = self.generate_dataclass(klass_or_instance)
         self.include_schema_doc = include_schema_doc
-        self.schema_definition = None
+        self.schema_definition: AvroSchemaDefinition = None
 
     @staticmethod
     def generate_dataclass(klass_or_instance):
         if dataclasses.is_dataclass(klass_or_instance):
             return klass_or_instance
         return dataclasses.dataclass(klass_or_instance)
 
@@ -27,18 +27,16 @@
             schema_definition = self._generate_avro_schema()
         else:
             raise ValueError("Invalid type. Expected avro schema type.")
 
         # cache the schema
         self.schema_definition = schema_definition
 
-        # cache the schema
-        self.schema_definition = schema_definition
-
-        return self.schema_definition.render()
+        if self.schema_definition:
+            return self.schema_definition.render()
 
     def _generate_avro_schema(self) -> AvroSchemaDefinition:
         return AvroSchemaDefinition(
             "record", self.dataclass, include_schema_doc=self.include_schema_doc
         )
 
     def avro_schema(self) -> str:
```

### Comparing `dataclasses-avroschema-0.8.0/dataclasses_avroschema/utils.py` & `dataclasses-avroschema-0.9.0/dataclasses_avroschema/utils.py`

 * *Files 10% similar despite different names*

```diff
@@ -8,19 +8,21 @@
     Arguments:
         a_type (typing.Any): python type
 
     Returns:
         bool
     """
     return (
-        isinstance(a_type, typing._GenericAlias) and a_type.__origin__ is typing.Union
+        isinstance(a_type, typing._GenericAlias)
+        and a_type.__origin__  # type: ignore
+        is typing.Union
     )
 
 
-def is_self_referenced(a_type):
+def is_self_referenced(a_type) -> bool:
     """
     Given a python type, return True if is self referenced, meaning
     that is instance of typing.ForwardRef, otherwise False
 
     Arguments:
         a_type (typing.Any): python type
 
@@ -29,11 +31,11 @@
 
     Example:
         a_type = typing.Type["User"]]
 
         is_self_referenced(a_type) # True
     """
     return (
-        isinstance(a_type, typing._GenericAlias)
+        isinstance(a_type, typing._GenericAlias)  # type: ignore
         and a_type.__args__
-        and isinstance(a_type.__args__[0], typing.ForwardRef)
+        and isinstance(a_type.__args__[0], typing.ForwardRef)  # type: ignore
     )
```

### Comparing `dataclasses-avroschema-0.8.0/dataclasses_avroschema.egg-info/PKG-INFO` & `dataclasses-avroschema-0.9.0/dataclasses_avroschema.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 Metadata-Version: 2.1
 Name: dataclasses-avroschema
-Version: 0.8.0
+Version: 0.9.0
 Summary: Generate Avro Schemas from a Python class
 Home-page: https://github.com/marcosschroh/dataclasses-avroschema
 Author: Marcos Schroh
 Author-email: schrohm@gmail.com
-License: GPLv3
+License: MIT
 Description: # Dataclasses Avro Schema Generator
         
         Generate [Avro](https://avro.apache.org/docs/1.8.2/spec.html) Schemas from a Python class
         
         [![Build Status](https://travis-ci.org/marcosschroh/dataclasses-avroschema.svg?branch=master)](https://travis-ci.org//dataclasses-avroschema)
         [![GitHub license](https://img.shields.io/github/license/marcosschroh/dataclasses-avroschema.svg)](https://github.com/marcosschroh/dataclasses-avroschema/blob/master/LICENSE)
         [![codecov](https://codecov.io/gh/marcosschroh/dataclasses-avroschema/branch/master/graph/badge.svg)](https://codecov.io/gh/marcosschroh/dataclasses-avroschema)
```

### Comparing `dataclasses-avroschema-0.8.0/dataclasses_avroschema.egg-info/SOURCES.txt` & `dataclasses-avroschema-0.9.0/dataclasses_avroschema.egg-info/SOURCES.txt`

 * *Files 16% similar despite different names*

```diff
@@ -8,10 +8,11 @@
 dataclasses_avroschema.egg-info/PKG-INFO
 dataclasses_avroschema.egg-info/SOURCES.txt
 dataclasses_avroschema.egg-info/dependency_links.txt
 dataclasses_avroschema.egg-info/requires.txt
 dataclasses_avroschema.egg-info/top_level.txt
 tests/fields/__init__.py
 tests/fields/consts.py
+tests/fields/test_BaseField.py
 tests/fields/test_complex_types.py
 tests/fields/test_logical_types.py
 tests/fields/test_primitive_types.py
```

### Comparing `dataclasses-avroschema-0.8.0/setup.py` & `dataclasses-avroschema-0.9.0/setup.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
 """ setup.py for dataclasses-avroschema."""
 
-from setuptools import setup, find_packages
+from setuptools import find_packages, setup
 
-__version__ = "0.8.0"
+__version__ = "0.9.0"
 
 with open("README.md") as readme_file:
     long_description = readme_file.read()
 
 setup(
     name="dataclasses-avroschema",
     version=__version__,
@@ -19,15 +19,15 @@
     author="Marcos Schroh",
     install_requires=["inflect==2.1.0"],
     author_email="schrohm@gmail.com",
     url="https://github.com/marcosschroh/dataclasses-avroschema",
     download_url="",
     packages=find_packages(exclude=("tests",)),
     include_package_data=True,
-    license="GPLv3",
+    license="MIT",
     classifiers=[
         "Programming Language :: Python :: 3.7",
         "Topic :: Software Development",
     ],
     keywords=(
         """
         Python, Data Classes, Avro Schema, Avro, Apache, Data Streaming
```

### Comparing `dataclasses-avroschema-0.8.0/tests/fields/consts.py` & `dataclasses-avroschema-0.9.0/tests/fields/consts.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-import typing
 import datetime
+import typing
 import uuid
 
 from dataclasses_avroschema import fields
 
 now = datetime.datetime.now()
 
 PRIMITIVE_TYPES = (
```

### Comparing `dataclasses-avroschema-0.8.0/tests/fields/test_complex_types.py` & `dataclasses-avroschema-0.9.0/tests/fields/test_complex_types.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -1,11 +1,11 @@
-import pytest
 import dataclasses
 import typing
 
+import pytest
 from faker import Faker
 
 from dataclasses_avroschema import fields
 
 from . import consts
 
 faker = Faker()
```

### Comparing `dataclasses-avroschema-0.8.0/tests/fields/test_logical_types.py` & `dataclasses-avroschema-0.9.0/tests/fields/test_logical_types.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,11 +1,12 @@
-import pytest
 import datetime
 import uuid
 
+import pytest
+
 from dataclasses_avroschema import fields
 
 from . import consts
 
 
 @pytest.mark.parametrize(
     "python_type,avro_type,logical_type", consts.LOGICAL_TYPES_AND_DEFAULTS
```

### Comparing `dataclasses-avroschema-0.8.0/tests/fields/test_primitive_types.py` & `dataclasses-avroschema-0.9.0/tests/fields/test_primitive_types.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,11 @@
-import pytest
 import dataclasses
 
+import pytest
+
 from dataclasses_avroschema import fields
 
 from . import consts
 
 
 @pytest.mark.parametrize("primitive_type", fields.PYTHON_INMUTABLE_TYPES)
 def test_primitive_types(primitive_type):
```

