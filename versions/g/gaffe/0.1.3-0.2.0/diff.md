# Comparing `tmp/gaffe-0.1.3.tar.gz` & `tmp/gaffe-0.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gaffe-0.1.3.tar", max compression
+gzip compressed data, was "gaffe-0.2.0.tar", max compression
```

## Comparing `gaffe-0.1.3.tar` & `gaffe-0.2.0.tar`

### file list

```diff
@@ -1,10 +1,10 @@
--rw-r--r--   0        0        0     1085 2023-03-11 10:29:04.023741 gaffe-0.1.3/LICENSE
--rw-r--r--   0        0        0     2282 2023-03-28 07:32:41.225348 gaffe-0.1.3/README.md
--rw-r--r--   0        0        0       52 2023-03-28 06:50:25.858844 gaffe-0.1.3/gaffe/__init__.py
--rw-r--r--   0        0        0     3806 2023-03-27 12:47:30.864357 gaffe-0.1.3/gaffe/error.py
--rw-r--r--   0        0        0      778 2023-03-16 08:12:57.267648 gaffe-0.1.3/gaffe/mypy.py
--rw-r--r--   0        0        0        0 2023-04-05 07:20:35.011928 gaffe-0.1.3/gaffe/py.typed
--rw-r--r--   0        0        0      719 2023-03-28 07:12:55.837252 gaffe-0.1.3/gaffe/raises.py
--rw-r--r--   0        0        0     1238 2023-04-05 07:21:16.093244 gaffe-0.1.3/pyproject.toml
--rw-r--r--   0        0        0     2931 1970-01-01 00:00:00.000000 gaffe-0.1.3/setup.py
--rw-r--r--   0        0        0     3177 1970-01-01 00:00:00.000000 gaffe-0.1.3/PKG-INFO
+-rw-r--r--   0        0        0     1085 2023-03-11 10:29:04.023741 gaffe-0.2.0/LICENSE
+-rw-r--r--   0        0        0     2390 2023-04-07 07:43:09.479337 gaffe-0.2.0/README.md
+-rw-r--r--   0        0        0       52 2023-03-28 06:50:25.858844 gaffe-0.2.0/gaffe/__init__.py
+-rw-r--r--   0        0        0     3806 2023-03-27 12:47:30.864357 gaffe-0.2.0/gaffe/error.py
+-rw-r--r--   0        0        0     1958 2023-04-07 07:26:54.594092 gaffe-0.2.0/gaffe/mypy.py
+-rw-r--r--   0        0        0        0 2023-04-05 07:20:35.011928 gaffe-0.2.0/gaffe/py.typed
+-rw-r--r--   0        0        0      725 2023-04-05 08:13:10.342515 gaffe-0.2.0/gaffe/raises.py
+-rw-r--r--   0        0        0     1295 2023-04-07 07:43:49.522793 gaffe-0.2.0/pyproject.toml
+-rw-r--r--   0        0        0     3042 1970-01-01 00:00:00.000000 gaffe-0.2.0/setup.py
+-rw-r--r--   0        0        0     3285 1970-01-01 00:00:00.000000 gaffe-0.2.0/PKG-INFO
```

### Comparing `gaffe-0.1.3/LICENSE` & `gaffe-0.2.0/LICENSE`

 * *Files identical despite different names*

### Comparing `gaffe-0.1.3/README.md` & `gaffe-0.2.0/README.md`

 * *Files 9% similar despite different names*

```diff
@@ -1,49 +1,52 @@
-Introducing Gaffe: Streamlined Exception Handling for Python
+# Introducing Gaffe: Streamlined Exception Handling for Python
 
 Are you tired of managing messy, unstructured exceptions in your Python projects? Gaffe is here to save the day! This elegant library offers a metaclass-based approach for highly extensible and easy-to-integrate custom exceptions, leading to better error handling and improved code readability.
 
-🔥 Key Features
+## 🔥 Key Features
 
-🎯 Simple, concise syntax for defining custom errors with optional subtypes
-🧩 Clean integration through metaclass-based approach
-🌳 Supports inheritance and composition of custom errors
-🏗️ Automatic generation of error classes with custom attributes
-🧮 Easy error comparison with the __eq__ method, supporting both class and instance comparisons
-🕵️‍♂️ raises decorator to inspect and validate exceptions raised by functions or methods
-🚀 Quick Installation
+- 🎯 Simple, concise syntax for defining custom errors with optional subtypes
+- 🧩 Clean integration through metaclass-based approach
+- 🌳 Supports inheritance and composition of custom errors
+- 🏗️ Automatic generation of error classes with custom attributes
+- 🧮 Easy error comparison with the __eq__ method, supporting both class and instance comparisons
+- 🕵️‍♂️ raises decorator to inspect and validate exceptions raised by functions or methods
+- 🚀 Quick Installation
 
 For pip enthusiasts:
 
-bash
-Copy code
+```bash
 pip install gaffe
+```
+
 For poetry aficionados:
 
-bash
-Copy code
+```bash
 poetry add gaffe
-💡 Getting Started
+```
+
+# 💡 Getting Started
 
 To employ Gaffe's custom error system, import the Error class and create custom errors by inheriting from it:
 
-python
-Copy code
+```python
 from gaffe import Error
 
 class NotFoundError(Exception):
     ...
 
 class MyError(Error):
     not_found: NotFoundError
     invalid_input: ...
     authentication_error = "authentication_error"
+```
+    
 With this example, you'll get three custom errors under the MyError class, ready to be used just like any other Python exceptions.
 
-🎩 Raises Decorator
+## 🎩 Raises Decorator
 
 Harness the power of the raises decorator to define and validate the types of exceptions a function or method can raise:
 
 ```python
 from gaffe import raises
 
 @raises(TypeError, ValueError)
@@ -53,15 +56,15 @@
     return x / y
 ```
 
 The raises decorator ensures that my_function can only raise TypeError and ValueError. If it tries to raise an unlisted exception, an AssertionError will be raised with a suitable error message.
 
 ## 🤖 Mypy Integration
 
-To keep mypy happy, use the gaffe.mypy:plugin in your config file:
+To keep mypy happy, use the gaffe.mypy:plugin in your config file, and ensure that error properties are annotated with `Exception` type instead of `...`
 
 ```toml
 [tool.mypy]
 plugins = "gaffe.mypy:plugin"
 ```
```

### Comparing `gaffe-0.1.3/gaffe/error.py` & `gaffe-0.2.0/gaffe/error.py`

 * *Files identical despite different names*

### Comparing `gaffe-0.1.3/gaffe/raises.py` & `gaffe-0.2.0/gaffe/raises.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 from functools import wraps
 from typing import TypeVar, Callable, Type, Any
 
 T = TypeVar("T")
 
 
-def raises(*allowed_errors: Type[Exception]) -> Callable[[T], T]:
+def raises(*allowed_errors: Type[Exception]) -> Callable:
 
-    def _decorate(what: T) -> T:
+    def _decorate(what: Callable) -> Callable:
 
         @wraps(what)
         def _execute_what(*args, **kwargs) -> Any:
             try:
                 return what(*args, **kwargs)
             except Exception as error:
                 if not isinstance(error, allowed_errors):
```

### Comparing `gaffe-0.1.3/pyproject.toml` & `gaffe-0.2.0/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "gaffe"
-version = "0.1.3"
+version = "0.2.0"
 description = "Simple structured exceptions for python."
 authors = [
     "Dawid Kraczkowski <dawid.kraczkowski@gmail.com>"
 ]
 license = "MIT"
 readme = "README.md"
 
@@ -26,14 +26,17 @@
 [tool.poetry.dev-dependencies]
 isort = "^5.7.0"
 pytest = "^6.2.5"
 pytest-cov = "^2.5"
 black = "^22.3.0"
 mypy = "^0.961"
 
+[tool.poetry.group.dev.dependencies]
+pylint = "^2.17.2"
+
 [tool.mypy]
 plugins = "gaffe.mypy:plugin"
 
 [tool.black]
 exclude = ".venv"
 line-length = 120
 target-version = ["py38"]
```

### Comparing `gaffe-0.1.3/setup.py` & `gaffe-0.2.0/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -5,17 +5,17 @@
 ['gaffe']
 
 package_data = \
 {'': ['*']}
 
 setup_kwargs = {
     'name': 'gaffe',
-    'version': '0.1.3',
+    'version': '0.2.0',
     'description': 'Simple structured exceptions for python.',
-    'long_description': 'Introducing Gaffe: Streamlined Exception Handling for Python\n\nAre you tired of managing messy, unstructured exceptions in your Python projects? Gaffe is here to save the day! This elegant library offers a metaclass-based approach for highly extensible and easy-to-integrate custom exceptions, leading to better error handling and improved code readability.\n\n🔥 Key Features\n\n🎯 Simple, concise syntax for defining custom errors with optional subtypes\n🧩 Clean integration through metaclass-based approach\n🌳 Supports inheritance and composition of custom errors\n🏗️ Automatic generation of error classes with custom attributes\n🧮 Easy error comparison with the __eq__ method, supporting both class and instance comparisons\n🕵️\u200d♂️ raises decorator to inspect and validate exceptions raised by functions or methods\n🚀 Quick Installation\n\nFor pip enthusiasts:\n\nbash\nCopy code\npip install gaffe\nFor poetry aficionados:\n\nbash\nCopy code\npoetry add gaffe\n💡 Getting Started\n\nTo employ Gaffe\'s custom error system, import the Error class and create custom errors by inheriting from it:\n\npython\nCopy code\nfrom gaffe import Error\n\nclass NotFoundError(Exception):\n    ...\n\nclass MyError(Error):\n    not_found: NotFoundError\n    invalid_input: ...\n    authentication_error = "authentication_error"\nWith this example, you\'ll get three custom errors under the MyError class, ready to be used just like any other Python exceptions.\n\n🎩 Raises Decorator\n\nHarness the power of the raises decorator to define and validate the types of exceptions a function or method can raise:\n\n```python\nfrom gaffe import raises\n\n@raises(TypeError, ValueError)\ndef my_function(x: int, y: int) -> float:\n    if x <= 0 or y <= 0:\n        raise ValueError("x and y must be positive")\n    return x / y\n```\n\nThe raises decorator ensures that my_function can only raise TypeError and ValueError. If it tries to raise an unlisted exception, an AssertionError will be raised with a suitable error message.\n\n## 🤖 Mypy Integration\n\nTo keep mypy happy, use the gaffe.mypy:plugin in your config file:\n\n```toml\n[tool.mypy]\nplugins = "gaffe.mypy:plugin"\n```\n\n\nReady to revolutionize your Python exception handling? Get started with Gaffe today and check out the test scenarios for more examples!\n',
+    'long_description': '# Introducing Gaffe: Streamlined Exception Handling for Python\n\nAre you tired of managing messy, unstructured exceptions in your Python projects? Gaffe is here to save the day! This elegant library offers a metaclass-based approach for highly extensible and easy-to-integrate custom exceptions, leading to better error handling and improved code readability.\n\n## 🔥 Key Features\n\n- 🎯 Simple, concise syntax for defining custom errors with optional subtypes\n- 🧩 Clean integration through metaclass-based approach\n- 🌳 Supports inheritance and composition of custom errors\n- 🏗️ Automatic generation of error classes with custom attributes\n- 🧮 Easy error comparison with the __eq__ method, supporting both class and instance comparisons\n- 🕵️\u200d♂️ raises decorator to inspect and validate exceptions raised by functions or methods\n- 🚀 Quick Installation\n\nFor pip enthusiasts:\n\n```bash\npip install gaffe\n```\n\nFor poetry aficionados:\n\n```bash\npoetry add gaffe\n```\n\n# 💡 Getting Started\n\nTo employ Gaffe\'s custom error system, import the Error class and create custom errors by inheriting from it:\n\n```python\nfrom gaffe import Error\n\nclass NotFoundError(Exception):\n    ...\n\nclass MyError(Error):\n    not_found: NotFoundError\n    invalid_input: ...\n    authentication_error = "authentication_error"\n```\n    \nWith this example, you\'ll get three custom errors under the MyError class, ready to be used just like any other Python exceptions.\n\n## 🎩 Raises Decorator\n\nHarness the power of the raises decorator to define and validate the types of exceptions a function or method can raise:\n\n```python\nfrom gaffe import raises\n\n@raises(TypeError, ValueError)\ndef my_function(x: int, y: int) -> float:\n    if x <= 0 or y <= 0:\n        raise ValueError("x and y must be positive")\n    return x / y\n```\n\nThe raises decorator ensures that my_function can only raise TypeError and ValueError. If it tries to raise an unlisted exception, an AssertionError will be raised with a suitable error message.\n\n## 🤖 Mypy Integration\n\nTo keep mypy happy, use the gaffe.mypy:plugin in your config file, and ensure that error properties are annotated with `Exception` type instead of `...`\n\n```toml\n[tool.mypy]\nplugins = "gaffe.mypy:plugin"\n```\n\n\nReady to revolutionize your Python exception handling? Get started with Gaffe today and check out the test scenarios for more examples!\n',
     'author': 'Dawid Kraczkowski',
     'author_email': 'dawid.kraczkowski@gmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'https://github.com/kodemore/gaffe',
     'packages': packages,
     'package_data': package_data,
```

### Comparing `gaffe-0.1.3/PKG-INFO` & `gaffe-0.2.0/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gaffe
-Version: 0.1.3
+Version: 0.2.0
 Summary: Simple structured exceptions for python.
 Home-page: https://github.com/kodemore/gaffe
 License: MIT
 Keywords: error,exception,structured,simple,gaffe
 Author: Dawid Kraczkowski
 Author-email: dawid.kraczkowski@gmail.com
 Requires-Python: >=3.8,<4.0
@@ -16,56 +16,59 @@
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Software Development :: Libraries
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Project-URL: Documentation, https://github.com/kodemore/gaffe
 Project-URL: Repository, https://github.com/kodemore/gaffe
 Description-Content-Type: text/markdown
 
-Introducing Gaffe: Streamlined Exception Handling for Python
+# Introducing Gaffe: Streamlined Exception Handling for Python
 
 Are you tired of managing messy, unstructured exceptions in your Python projects? Gaffe is here to save the day! This elegant library offers a metaclass-based approach for highly extensible and easy-to-integrate custom exceptions, leading to better error handling and improved code readability.
 
-🔥 Key Features
+## 🔥 Key Features
 
-🎯 Simple, concise syntax for defining custom errors with optional subtypes
-🧩 Clean integration through metaclass-based approach
-🌳 Supports inheritance and composition of custom errors
-🏗️ Automatic generation of error classes with custom attributes
-🧮 Easy error comparison with the __eq__ method, supporting both class and instance comparisons
-🕵️‍♂️ raises decorator to inspect and validate exceptions raised by functions or methods
-🚀 Quick Installation
+- 🎯 Simple, concise syntax for defining custom errors with optional subtypes
+- 🧩 Clean integration through metaclass-based approach
+- 🌳 Supports inheritance and composition of custom errors
+- 🏗️ Automatic generation of error classes with custom attributes
+- 🧮 Easy error comparison with the __eq__ method, supporting both class and instance comparisons
+- 🕵️‍♂️ raises decorator to inspect and validate exceptions raised by functions or methods
+- 🚀 Quick Installation
 
 For pip enthusiasts:
 
-bash
-Copy code
+```bash
 pip install gaffe
+```
+
 For poetry aficionados:
 
-bash
-Copy code
+```bash
 poetry add gaffe
-💡 Getting Started
+```
+
+# 💡 Getting Started
 
 To employ Gaffe's custom error system, import the Error class and create custom errors by inheriting from it:
 
-python
-Copy code
+```python
 from gaffe import Error
 
 class NotFoundError(Exception):
     ...
 
 class MyError(Error):
     not_found: NotFoundError
     invalid_input: ...
     authentication_error = "authentication_error"
+```
+    
 With this example, you'll get three custom errors under the MyError class, ready to be used just like any other Python exceptions.
 
-🎩 Raises Decorator
+## 🎩 Raises Decorator
 
 Harness the power of the raises decorator to define and validate the types of exceptions a function or method can raise:
 
 ```python
 from gaffe import raises
 
 @raises(TypeError, ValueError)
@@ -75,15 +78,15 @@
     return x / y
 ```
 
 The raises decorator ensures that my_function can only raise TypeError and ValueError. If it tries to raise an unlisted exception, an AssertionError will be raised with a suitable error message.
 
 ## 🤖 Mypy Integration
 
-To keep mypy happy, use the gaffe.mypy:plugin in your config file:
+To keep mypy happy, use the gaffe.mypy:plugin in your config file, and ensure that error properties are annotated with `Exception` type instead of `...`
 
 ```toml
 [tool.mypy]
 plugins = "gaffe.mypy:plugin"
 ```
```

