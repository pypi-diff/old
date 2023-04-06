# Comparing `tmp/generic_configuration_builder-1.1.0.tar.gz` & `tmp/generic_configuration_builder-1.2.0.tar.gz`

## Comparing `generic_configuration_builder-1.1.0.tar` & `generic_configuration_builder-1.2.0.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 generic_configuration_builder-1.1.0/.gitattributes
--rw-r--r--   0        0        0       73 2020-02-02 00:00:00.000000 generic_configuration_builder-1.1.0/src/generic_configuration_builder/__init__.py
--rw-r--r--   0        0        0    11363 2020-02-02 00:00:00.000000 generic_configuration_builder-1.1.0/src/generic_configuration_builder/configuration_builder.py
--rw-r--r--   0        0        0     2763 2020-02-02 00:00:00.000000 generic_configuration_builder-1.1.0/.gitignore
--rw-r--r--   0        0        0     1076 2020-02-02 00:00:00.000000 generic_configuration_builder-1.1.0/LICENSE
--rw-r--r--   0        0        0     6534 2020-02-02 00:00:00.000000 generic_configuration_builder-1.1.0/README.md
--rw-r--r--   0        0        0     1004 2020-02-02 00:00:00.000000 generic_configuration_builder-1.1.0/pyproject.toml
--rw-r--r--   0        0        0     8663 2020-02-02 00:00:00.000000 generic_configuration_builder-1.1.0/PKG-INFO
+-rw-r--r--   0        0        0       66 2020-02-02 00:00:00.000000 generic_configuration_builder-1.2.0/.gitattributes
+-rw-r--r--   0        0        0       73 2020-02-02 00:00:00.000000 generic_configuration_builder-1.2.0/src/generic_configuration_builder/__init__.py
+-rw-r--r--   0        0        0    13734 2020-02-02 00:00:00.000000 generic_configuration_builder-1.2.0/src/generic_configuration_builder/configuration_builder.py
+-rw-r--r--   0        0        0     2763 2020-02-02 00:00:00.000000 generic_configuration_builder-1.2.0/.gitignore
+-rw-r--r--   0        0        0     1076 2020-02-02 00:00:00.000000 generic_configuration_builder-1.2.0/LICENSE
+-rw-r--r--   0        0        0     7188 2020-02-02 00:00:00.000000 generic_configuration_builder-1.2.0/README.md
+-rw-r--r--   0        0        0     1004 2020-02-02 00:00:00.000000 generic_configuration_builder-1.2.0/pyproject.toml
+-rw-r--r--   0        0        0     9317 2020-02-02 00:00:00.000000 generic_configuration_builder-1.2.0/PKG-INFO
```

### Comparing `generic_configuration_builder-1.1.0/src/generic_configuration_builder/configuration_builder.py` & `generic_configuration_builder-1.2.0/src/generic_configuration_builder/configuration_builder.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,25 +1,30 @@
 import inspect
 import configparser
 from collections import OrderedDict
 import os
 import ast
 from typing import Union, Dict, Callable
+import re
 
 ### Optional Imports
 
+SPECIAL_TYPES = []
+
 try:
     import torch
     HAS_TORCH = True
+    SPECIAL_TYPES.append(torch.tensor)
 except ImportError:
     HAS_TORCH = False
 
 try:
     import numpy as np
     HAS_NUMPY = True
+    SPECIAL_TYPES.append(np.ndarray)
 except ImportError:
     HAS_NUMPY = False
 
 ### Keywords
 
 MODULE_MARKER = "~MODULE"
 CLASS_MARKER = "~CLASS"
@@ -166,37 +171,32 @@
     annotations_dict = full_arg_spec.annotations
     annotations_dict.pop("return", None)
 
     init_args_types.update(annotations_dict)
 
     init_args_instances = {}
     for arg_name, arg_string in init_args_string_dict.items():
-        if(arg_string.startswith(INSTANCE_INDICATOR)):
-            instance = _get_attribute(argument_string=arg_string[len(INSTANCE_INDICATOR):], variables_dict=variables_dict)
-            init_args_instances[arg_name] = instance
-            continue
-        
         if arg_name in init_args_types:
-            init_args_instances[arg_name] = _parse_value(dtype=init_args_types[arg_name],string=arg_string)
+            init_args_instances[arg_name] = _parse_value(string=arg_string, variables_dict=variables_dict, dtype=init_args_types[arg_name])
         elif full_arg_spec.varkw != None:
-            init_args_instances[arg_name] = ast.literal_eval(arg_string)
+            init_args_instances[arg_name] = _parse_value(string=arg_string, variables_dict=variables_dict, dtype=None)
 
     return _class(**init_args_instances)
 
 def _load_class(module_name: str, class_name: str) -> type:
     """Loads a class type given its location by strings.
 
     Args:
         module_name (str): String that leads to the module of the class
         class_name (str): Name of the class
 
     Returns:
         type: According python class type object
     """
-    module = __import__(module_name, fromlist=class_name)
+    module = __import__(module_name, fromlist = class_name)
     _class = getattr(module, class_name)
     return _class
 
 def _get_attribute(argument_string: str, variables_dict: Dict[str, object]) -> object:
     """Gets an attribute of an instance.
 
     Args:
@@ -216,55 +216,104 @@
         raise Exception(f'"{argument_attributes[0]}" has not been assigned a value yet.') from key_error
     instance = base_instance
     for attribute_name in argument_attributes[1:]:
         instance = getattr(instance, attribute_name)
 
     return instance
 
-def _parse_value(dtype: type, string: str) -> object:
+def _parse_value(string: str, variables_dict: Dict[str, any], dtype: type = None) -> any:
     """Parse Python base datatypes from a string.
 
     Args:
         dtype (type): type to cast to.
+        variables_dict (Dict[str, any]):  Dictionary of already initialized classes.
         string (str): String to cast.
 
     Raises:
         Exception: When string could not be cast into desired into a datatype. Function no necessarily tries to parse to type dtype.
 
     Returns:
         object: Parsed string as Python object
     """
     try:
-        parsed = _parse_function_of(dtype)(string)
+        if dtype != None and dtype in SPECIAL_TYPES:
+            parse_function = _parse_function_of(dtype=dtype)
+            return parse_function(string)
+        else:
+            parsed = _parse_literal_with_instance_markers(value_string = string, variables_dict = variables_dict)
     except Exception as error:
-        raise Exception(f"Error while trying to parse: {string} as: {dtype}").with_traceback(error.__traceback__)
-
+        raise Exception(f"Error while trying to parse: {string}") from error
     return parsed
 
 def _parse_function_of(dtype: type) -> Callable:
     """Returns function to parse a string to dtype.
-        Always returns ast.literal_eval if dtype is not torch.Tensor or np.ndarray.
-
     Args:
         dtype (type): Type for which the parse function is needed.
-
     Returns:
         Callable: According parse function
     """
     if( HAS_TORCH and dtype == torch.Tensor):
         return _parse_torch_tensor
     if( HAS_NUMPY and dtype == np.ndarray):
         return _parse_numpy_array
 
-    return ast.literal_eval
+    raise Exception(f'No special parse function implemented for dtype: "{dtype}"')
+
+def _parse_literal_with_instance_markers(value_string: str, variables_dict: Dict[str, any]) -> any:
+    """Parses a string to a python object. 
+    If string contain INSTANCE_INDICATOR than replace that string with the according instance.
+
+    Args:
+        value_string (str): String to parse
+        variables_dict (Dict[str, any]): Already initialized instances.
+
+    Returns:
+        any: _description_
+    """
+      
+    regex = f'([{INSTANCE_INDICATOR}][\w.]+)'
+    prog = re.compile(regex)
+    matches = re.findall(prog, value_string)
+    if len(matches) == 0:
+        return ast.literal_eval(value_string)
+    else:
+        for match in matches:
+            value_string = value_string.replace(match, f"'{match}'")
+
+        parsed_with_placeholders = ast.literal_eval(value_string)
+        return replace_strings(data=parsed_with_placeholders, to_replace=matches, variables_dict=variables_dict)
+        
+
+def replace_strings(data: any, to_replace: list[str], variables_dict: Dict[str, any]) -> any:
+    """Recursively iterates over a nested collection and replaces strings 
+        that are part of to_replace with instances.
+
+    Args:
+        data (any): A construct of nested collections containing list, tuples and dictionaries
+        to_replace (list[str]): List of strings that should be replaced with an instance.
+        variables_dict (Dict[str, any]):  Dictionary of already initialized classes. These are used to replace the according strings.
+
+    Returns:
+        any: The same structure of nested collections but with replaced strings.
+    """
 
-### Special parse functions
+    if isinstance(data, list):
+        return [replace_strings(item, to_replace, variables_dict) for item in data]
+    elif isinstance(data, tuple):
+        return tuple(replace_strings(item, to_replace, variables_dict) for item in data)
+    elif isinstance(data, dict):
+        return {replace_strings(key, to_replace, variables_dict): replace_strings(value, to_replace, variables_dict) for key, value in data.items()}
+    elif isinstance(data, str):
+        if data in to_replace:
+            return _get_attribute(argument_string=data[len(INSTANCE_INDICATOR):], variables_dict=variables_dict)
+    return data
 
 def _parse_unmarked_string_list(list_string: str) -> list[str]:
-    """ Converts a string that represents a list without INSTANCE_INDICATOR to a list of strings. Each entry is assumed to be a variable.
+    """ Converts a string that represents a list without INSTANCE_INDICATOR to a list of strings. 
+        Each entry is assumed to be a variable.
 
     Args:
         list_string (str): String that represents a list.
 
     Returns:
         list[str]: List of strings where each string represents an instance.
     """
```

### Comparing `generic_configuration_builder-1.1.0/.gitignore` & `generic_configuration_builder-1.2.0/.gitignore`

 * *Files identical despite different names*

### Comparing `generic_configuration_builder-1.1.0/LICENSE` & `generic_configuration_builder-1.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `generic_configuration_builder-1.1.0/README.md` & `generic_configuration_builder-1.2.0/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -19,19 +19,19 @@
 The .ini file format is used as follows:
 
 ```
 [instance_name]
 ~Module = module_of.the_class
 ~Class = ClassName
 constructor_argument_1 = 42
-constructor_argument_2 = "int, strings, lists, dicts and tuples are supported"
+constructor_argument_2 = "int, strings, lists, dicts, tuples and None are supported"
 constructor_argument_3 = [1,2,3,4]
 constructor_argument_4 = (5,6,7,8)
 constructor_argument_5 = {"key_1": "value_1",
-                        "key_2": "value_2"}
+                        "key_2": None}
 
 [another_instance]
 ~MODULE = a_different.module
 ~CLASS = DifferentClass
 argument_that_requieres_the_previous_class = *instance_name
 more_arguments = ["a", 2]
 
@@ -92,17 +92,33 @@
 ~MODULE = foos.module
 ~CLASS = FooClass
 argument_that_needs_chield_from previous_instance = *name_of_previous_instance.child
 ```
 
 This works recursively, so you could write `*instance.child.subchild` as well.
 
+### Using nested instances
+
+You can nested an instance inside a list, tuple or dictionary and it will still be recognized. This also works recursively. For example like this:
+
+```
+[some_thing]
+~MODULE = some
+~CLASS = Thing
+dict_with_instance = {"object": *this_is_an_instance, 
+                    {"sub_dictionary_key": *this_is_another_instance}},
+                    {*instance_as_key : "some value"}
+list_of_tuple = [(*instance_1, *instance_2.child, 'a normal string'),
+                 (*instance_3, None, 'another_string')]
+```
+Note that not all objects can be keys of dictionaries.
+
 ### Parsing torch and numpy arrays
 
-If you have numpy or pytorch installed AND the class you want to instantiate uses type hints in the signature of its `__init__` function, then you may pass an array as arguments in addition to the other data types. The correct format here is the one you get when you `print()` the according array or tensor.
+If you have numpy or pytorch installed AND the class you want to instantiate uses type hints in the signature of its `__init__` function, then you may pass an array as arguments in addition to the other data types. The correct format here is the one you get when you `print()` the according array or tensor. These special data types can not be nested inside collections.
 
 ## Examples 
 Specific examples without any other python packages are not very helpful as native python classes usually don't need this kind of construction. 
 So here is a simple example with some made-up classes.
 Assume the existence of `classes.py` in the working directory with the following content:
 ```
 class ChildClass():
```

### Comparing `generic_configuration_builder-1.1.0/pyproject.toml` & `generic_configuration_builder-1.2.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "generic_configuration_builder"
-version = "1.1.0"
+version = "1.2.0"
 authors = [
   { name="Sebastian Griesbach", email="sebastian.griesbach@zoho.eu" },
 ]
 description = "A simple library for parsing a configuration file format which is intended to build dependencies and hold parameters - well suited for experimentaton settings in which different experiments use different clases."
 readme = "README.md"
 license = {file = "LICENSE"}
 requires-python = ">=3.7"
```

### Comparing `generic_configuration_builder-1.1.0/PKG-INFO` & `generic_configuration_builder-1.2.0/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: generic_configuration_builder
-Version: 1.1.0
+Version: 1.2.0
 Summary: A simple library for parsing a configuration file format which is intended to build dependencies and hold parameters - well suited for experimentaton settings in which different experiments use different clases.
 Project-URL: Homepage, https://github.com/Sebastian-Griesbach/Generic-Configuration-Builder
 Project-URL: Bug Tracker, https://github.com/Sebastian-Griesbach/Generic-Configuration-Builder/issues
 Author-email: Sebastian Griesbach <sebastian.griesbach@zoho.eu>
 License: MIT License
         
         Copyright (c) 2022 Sebastian Griesbach
@@ -56,19 +56,19 @@
 The .ini file format is used as follows:
 
 ```
 [instance_name]
 ~Module = module_of.the_class
 ~Class = ClassName
 constructor_argument_1 = 42
-constructor_argument_2 = "int, strings, lists, dicts and tuples are supported"
+constructor_argument_2 = "int, strings, lists, dicts, tuples and None are supported"
 constructor_argument_3 = [1,2,3,4]
 constructor_argument_4 = (5,6,7,8)
 constructor_argument_5 = {"key_1": "value_1",
-                        "key_2": "value_2"}
+                        "key_2": None}
 
 [another_instance]
 ~MODULE = a_different.module
 ~CLASS = DifferentClass
 argument_that_requieres_the_previous_class = *instance_name
 more_arguments = ["a", 2]
 
@@ -129,17 +129,33 @@
 ~MODULE = foos.module
 ~CLASS = FooClass
 argument_that_needs_chield_from previous_instance = *name_of_previous_instance.child
 ```
 
 This works recursively, so you could write `*instance.child.subchild` as well.
 
+### Using nested instances
+
+You can nested an instance inside a list, tuple or dictionary and it will still be recognized. This also works recursively. For example like this:
+
+```
+[some_thing]
+~MODULE = some
+~CLASS = Thing
+dict_with_instance = {"object": *this_is_an_instance, 
+                    {"sub_dictionary_key": *this_is_another_instance}},
+                    {*instance_as_key : "some value"}
+list_of_tuple = [(*instance_1, *instance_2.child, 'a normal string'),
+                 (*instance_3, None, 'another_string')]
+```
+Note that not all objects can be keys of dictionaries.
+
 ### Parsing torch and numpy arrays
 
-If you have numpy or pytorch installed AND the class you want to instantiate uses type hints in the signature of its `__init__` function, then you may pass an array as arguments in addition to the other data types. The correct format here is the one you get when you `print()` the according array or tensor.
+If you have numpy or pytorch installed AND the class you want to instantiate uses type hints in the signature of its `__init__` function, then you may pass an array as arguments in addition to the other data types. The correct format here is the one you get when you `print()` the according array or tensor. These special data types can not be nested inside collections.
 
 ## Examples 
 Specific examples without any other python packages are not very helpful as native python classes usually don't need this kind of construction. 
 So here is a simple example with some made-up classes.
 Assume the existence of `classes.py` in the working directory with the following content:
 ```
 class ChildClass():
```

