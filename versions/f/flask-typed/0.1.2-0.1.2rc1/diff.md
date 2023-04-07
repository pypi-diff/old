# Comparing `tmp/flask_typed-0.1.2.tar.gz` & `tmp/flask_typed-0.1.2rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "flask_typed-0.1.2.tar", max compression
+gzip compressed data, was "flask_typed-0.1.2rc1.tar", max compression
```

## Comparing `flask_typed-0.1.2.tar` & `flask_typed-0.1.2rc1.tar`

### file list

```diff
@@ -1,17 +1,17 @@
--rw-r--r--   0        0        0     1076 2023-02-23 09:44:30.241842 flask_typed-0.1.2/LICENSE
--rw-r--r--   0        0        0      983 2023-03-28 09:49:00.808886 flask_typed-0.1.2/README.md
--rw-r--r--   0        0        0      160 2023-03-28 09:49:00.808886 flask_typed-0.1.2/flask_typed/__init__.py
--rw-r--r--   0        0        0      252 2023-03-28 09:49:00.812219 flask_typed-0.1.2/flask_typed/annotations.py
--rw-r--r--   0        0        0        0 2023-03-28 09:49:00.812219 flask_typed-0.1.2/flask_typed/docs/__init__.py
--rw-r--r--   0        0        0     4881 2023-03-28 09:49:00.812219 flask_typed-0.1.2/flask_typed/docs/responses.py
--rw-r--r--   0        0        0     2072 2023-03-28 09:49:00.812219 flask_typed-0.1.2/flask_typed/docs/utils.py
--rw-r--r--   0        0        0     1682 2023-03-28 09:49:00.812219 flask_typed-0.1.2/flask_typed/errors.py
--rw-r--r--   0        0        0     6009 2023-03-28 13:50:35.901220 flask_typed-0.1.2/flask_typed/handler.py
--rw-r--r--   0        0        0     6789 2023-03-28 09:49:00.812219 flask_typed-0.1.2/flask_typed/parameter.py
--rw-r--r--   0        0        0     1399 2023-03-28 09:49:00.812219 flask_typed-0.1.2/flask_typed/parsers.py
--rw-r--r--   0        0        0     2498 2023-03-28 09:49:00.812219 flask_typed-0.1.2/flask_typed/response.py
--rw-r--r--   0        0        0     3144 2023-04-07 12:40:19.525529 flask_typed-0.1.2/flask_typed/typed_api.py
--rw-r--r--   0        0        0     1601 2023-02-23 09:44:30.245175 flask_typed-0.1.2/flask_typed/typed_resource.py
--rw-r--r--   0        0        0      473 2023-04-07 12:57:22.318828 flask_typed-0.1.2/pyproject.toml
--rw-r--r--   0        0        0     1752 1970-01-01 00:00:00.000000 flask_typed-0.1.2/setup.py
--rw-r--r--   0        0        0     1514 1970-01-01 00:00:00.000000 flask_typed-0.1.2/PKG-INFO
+-rw-r--r--   0        0        0     1076 2023-02-23 09:44:30.241842 flask_typed-0.1.2rc1/LICENSE
+-rw-r--r--   0        0        0      983 2023-03-28 09:49:00.808886 flask_typed-0.1.2rc1/README.md
+-rw-r--r--   0        0        0      160 2023-03-28 09:49:00.808886 flask_typed-0.1.2rc1/flask_typed/__init__.py
+-rw-r--r--   0        0        0      252 2023-03-28 09:49:00.812219 flask_typed-0.1.2rc1/flask_typed/annotations.py
+-rw-r--r--   0        0        0        0 2023-03-28 09:49:00.812219 flask_typed-0.1.2rc1/flask_typed/docs/__init__.py
+-rw-r--r--   0        0        0     4881 2023-03-28 09:49:00.812219 flask_typed-0.1.2rc1/flask_typed/docs/responses.py
+-rw-r--r--   0        0        0     2072 2023-03-28 09:49:00.812219 flask_typed-0.1.2rc1/flask_typed/docs/utils.py
+-rw-r--r--   0        0        0     1682 2023-03-28 09:49:00.812219 flask_typed-0.1.2rc1/flask_typed/errors.py
+-rw-r--r--   0        0        0     6009 2023-03-28 13:50:35.901220 flask_typed-0.1.2rc1/flask_typed/handler.py
+-rw-r--r--   0        0        0     6789 2023-03-28 09:49:00.812219 flask_typed-0.1.2rc1/flask_typed/parameter.py
+-rw-r--r--   0        0        0     1399 2023-03-28 09:49:00.812219 flask_typed-0.1.2rc1/flask_typed/parsers.py
+-rw-r--r--   0        0        0     2498 2023-03-28 09:49:00.812219 flask_typed-0.1.2rc1/flask_typed/response.py
+-rw-r--r--   0        0        0     3144 2023-04-07 12:40:19.525529 flask_typed-0.1.2rc1/flask_typed/typed_api.py
+-rw-r--r--   0        0        0     1601 2023-02-23 09:44:30.245175 flask_typed-0.1.2rc1/flask_typed/typed_resource.py
+-rw-r--r--   0        0        0      476 2023-04-07 12:42:45.785524 flask_typed-0.1.2rc1/pyproject.toml
+-rw-r--r--   0        0        0     1755 1970-01-01 00:00:00.000000 flask_typed-0.1.2rc1/setup.py
+-rw-r--r--   0        0        0     1517 1970-01-01 00:00:00.000000 flask_typed-0.1.2rc1/PKG-INFO
```

### Comparing `flask_typed-0.1.2/LICENSE` & `flask_typed-0.1.2rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/README.md` & `flask_typed-0.1.2rc1/README.md`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/flask_typed/docs/responses.py` & `flask_typed-0.1.2rc1/flask_typed/docs/responses.py`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/flask_typed/docs/utils.py` & `flask_typed-0.1.2rc1/flask_typed/docs/utils.py`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/flask_typed/errors.py` & `flask_typed-0.1.2rc1/flask_typed/errors.py`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/flask_typed/handler.py` & `flask_typed-0.1.2rc1/flask_typed/handler.py`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/flask_typed/parameter.py` & `flask_typed-0.1.2rc1/flask_typed/parameter.py`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/flask_typed/parsers.py` & `flask_typed-0.1.2rc1/flask_typed/parsers.py`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/flask_typed/response.py` & `flask_typed-0.1.2rc1/flask_typed/response.py`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/flask_typed/typed_api.py` & `flask_typed-0.1.2rc1/flask_typed/typed_api.py`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/flask_typed/typed_resource.py` & `flask_typed-0.1.2rc1/flask_typed/typed_resource.py`

 * *Files identical despite different names*

### Comparing `flask_typed-0.1.2/setup.py` & `flask_typed-0.1.2rc1/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 ['docstring-parser>=0.15,<0.16',
  'flask>=2.2.3,<3.0.0',
  'openapi-schema-pydantic>=1.2.4,<2.0.0',
  'pydantic>=1.10.5,<2.0.0']
 
 setup_kwargs = {
     'name': 'flask-typed',
-    'version': '0.1.2',
+    'version': '0.1.2rc1',
     'description': '',
     'long_description': '# flask-typed\n\nA Flask extension for developing HTTP APIs using type annotations. Type annotations are used for the validation of requests and generating API documentation.\n\n## Example\n\n```python\nfrom flask import Flask\nfrom pydantic import BaseModel\n\nfrom flask_typed import TypedResource, TypedAPI\n\n\nclass HelloResponse(BaseModel):\n\n    message: str\n    sender: str\n    receiver: str\n\n\nclass HelloResource(TypedResource):\n\n    def get(self, sender: str, receiver: str) -> HelloResponse:\n        """\n        Greets someone\n\n        :param sender: Greeter\n        :param receiver: The one being greeted\n        :return: Greetings\n        """\n        return HelloResponse(\n            message=f"Hello to {receiver} from {sender}!",\n            sender=sender,\n            receiver=receiver\n        )\n\n\napp = Flask(__name__)\napi = TypedAPI(app, version="1.0", description="Greetings API")\n\napi.add_resource(HelloResource, "/hello/<sender>")\n\nif __name__ == "__main__":\n    app.run()\n```',
     'author': 'Mustafa Efendioğlu',
     'author_email': 'mfnd@protonmail.com',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `flask_typed-0.1.2/PKG-INFO` & `flask_typed-0.1.2rc1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: flask-typed
-Version: 0.1.2
+Version: 0.1.2rc1
 Summary: 
 Author: Mustafa Efendioğlu
 Author-email: mfnd@protonmail.com
 Requires-Python: >=3.10,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
```

