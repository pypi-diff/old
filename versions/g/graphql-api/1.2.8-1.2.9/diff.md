# Comparing `tmp/graphql-api-1.2.8.tar.gz` & `tmp/graphql-api-1.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "graphql-api-1.2.8.tar", last modified: Thu Sep 22 11:22:08 2022, max compression
+gzip compressed data, was "graphql-api-1.2.9.tar", last modified: Thu Sep 22 17:17:08 2022, max compression
```

## Comparing `graphql-api-1.2.8.tar` & `graphql-api-1.2.9.tar`

### file list

```diff
@@ -1,30 +1,30 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-22 11:22:08.378125 graphql-api-1.2.8/
--rwxrwxrwx   0 root         (0) root         (0)     1069 2022-09-22 11:21:58.000000 graphql-api-1.2.8/LICENSE
--rwxrwxrwx   0 root         (0) root         (0)       73 2022-09-22 11:21:58.000000 graphql-api-1.2.8/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1964 2022-09-22 11:22:08.378125 graphql-api-1.2.8/PKG-INFO
--rwxrwxrwx   0 root         (0) root         (0)     1268 2022-09-22 11:21:58.000000 graphql-api-1.2.8/README.md
--rw-rw-rw-   0 root         (0) root         (0)        7 2022-09-22 11:22:07.000000 graphql-api-1.2.8/VERSION
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-22 11:22:08.376124 graphql-api-1.2.8/graphql_api/
--rwxrwxrwx   0 root         (0) root         (0)      251 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/__init__.py
--rwxrwxrwx   0 root         (0) root         (0)     6728 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/api.py
--rwxrwxrwx   0 root         (0) root         (0)      560 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/context.py
--rwxrwxrwx   0 root         (0) root         (0)     3166 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/dataclass_mapping.py
--rw-rw-rw-   0 root         (0) root         (0)      403 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/decorators.py
--rwxrwxrwx   0 root         (0) root         (0)      592 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/error.py
--rwxrwxrwx   0 root         (0) root         (0)       52 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/exception.py
--rwxrwxrwx   0 root         (0) root         (0)     4686 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/executor.py
--rwxrwxrwx   0 root         (0) root         (0)    22748 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/mapper.py
--rwxrwxrwx   0 root         (0) root         (0)     2093 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/middleware.py
--rwxrwxrwx   0 root         (0) root         (0)     6915 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/reduce.py
--rwxrwxrwx   0 root         (0) root         (0)     3122 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/relay.py
--rwxrwxrwx   0 root         (0) root         (0)    33657 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/remote.py
--rwxrwxrwx   0 root         (0) root         (0)     2648 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/types.py
--rwxrwxrwx   0 root         (0) root         (0)     5618 2022-09-22 11:21:58.000000 graphql-api-1.2.8/graphql_api/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-22 11:22:08.378125 graphql-api-1.2.8/graphql_api.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1964 2022-09-22 11:22:08.000000 graphql-api-1.2.8/graphql_api.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      580 2022-09-22 11:22:08.000000 graphql-api-1.2.8/graphql_api.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-09-22 11:22:08.000000 graphql-api-1.2.8/graphql_api.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      141 2022-09-22 11:22:08.000000 graphql-api-1.2.8/graphql_api.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       12 2022-09-22 11:22:08.000000 graphql-api-1.2.8/graphql_api.egg-info/top_level.txt
--rwxrwxrwx   0 root         (0) root         (0)       79 2022-09-22 11:22:08.378125 graphql-api-1.2.8/setup.cfg
--rwxrwxrwx   0 root         (0) root         (0)     1442 2022-09-22 11:21:58.000000 graphql-api-1.2.8/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-22 17:17:08.619816 graphql-api-1.2.9/
+-rwxrwxrwx   0 root         (0) root         (0)     1069 2022-09-22 17:16:58.000000 graphql-api-1.2.9/LICENSE
+-rwxrwxrwx   0 root         (0) root         (0)       73 2022-09-22 17:16:58.000000 graphql-api-1.2.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1945 2022-09-22 17:17:08.619816 graphql-api-1.2.9/PKG-INFO
+-rwxrwxrwx   0 root         (0) root         (0)     1269 2022-09-22 17:16:58.000000 graphql-api-1.2.9/README.md
+-rw-rw-rw-   0 root         (0) root         (0)        7 2022-09-22 17:17:08.000000 graphql-api-1.2.9/VERSION
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-22 17:17:08.617816 graphql-api-1.2.9/graphql_api/
+-rwxrwxrwx   0 root         (0) root         (0)      286 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/__init__.py
+-rwxrwxrwx   0 root         (0) root         (0)     6728 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/api.py
+-rwxrwxrwx   0 root         (0) root         (0)      560 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/context.py
+-rwxrwxrwx   0 root         (0) root         (0)     3166 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/dataclass_mapping.py
+-rw-rw-rw-   0 root         (0) root         (0)      403 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/decorators.py
+-rwxrwxrwx   0 root         (0) root         (0)      592 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/error.py
+-rwxrwxrwx   0 root         (0) root         (0)       52 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/exception.py
+-rwxrwxrwx   0 root         (0) root         (0)     4686 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/executor.py
+-rwxrwxrwx   0 root         (0) root         (0)    22758 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/mapper.py
+-rwxrwxrwx   0 root         (0) root         (0)     2093 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/middleware.py
+-rwxrwxrwx   0 root         (0) root         (0)     6915 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/reduce.py
+-rwxrwxrwx   0 root         (0) root         (0)     3122 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/relay.py
+-rwxrwxrwx   0 root         (0) root         (0)    33657 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/remote.py
+-rwxrwxrwx   0 root         (0) root         (0)     2648 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/types.py
+-rwxrwxrwx   0 root         (0) root         (0)     5618 2022-09-22 17:16:58.000000 graphql-api-1.2.9/graphql_api/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-09-22 17:17:08.619816 graphql-api-1.2.9/graphql_api.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1945 2022-09-22 17:17:08.000000 graphql-api-1.2.9/graphql_api.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      580 2022-09-22 17:17:08.000000 graphql-api-1.2.9/graphql_api.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-09-22 17:17:08.000000 graphql-api-1.2.9/graphql_api.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      141 2022-09-22 17:17:08.000000 graphql-api-1.2.9/graphql_api.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       12 2022-09-22 17:17:08.000000 graphql-api-1.2.9/graphql_api.egg-info/top_level.txt
+-rwxrwxrwx   0 root         (0) root         (0)       79 2022-09-22 17:17:08.619816 graphql-api-1.2.9/setup.cfg
+-rwxrwxrwx   0 root         (0) root         (0)     1442 2022-09-22 17:16:58.000000 graphql-api-1.2.9/setup.py
```

### Comparing `graphql-api-1.2.8/LICENSE` & `graphql-api-1.2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/PKG-INFO` & `graphql-api-1.2.9/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,18 +1,17 @@
 Metadata-Version: 2.1
 Name: graphql-api
-Version: 1.2.8
+Version: 1.2.9
 Summary: A framework for building Python GraphQL APIs.
 Home-page: https://gitlab.com/parob/graphql-api
+Download-URL: https://gitlab.com/parob/graphql/-/archive/v1.2.9/graphql-api-v1.2.9.tar.gz
 Author: Robert Parker
 Author-email: rob@parob.com
 License: MIT
-Download-URL: https://gitlab.com/parob/graphql/-/archive/v1.2.8/graphql-api-v1.2.8.tar.gz
 Keywords: GraphQL,GraphQL-API,GraphQLAPI,Server
-Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 Provides-Extra: dev
@@ -21,14 +20,15 @@
 # GraphQL-API
 Framework for building a GraphQL API with Python
 
 [![coverage report](https://gitlab.com/parob/graphql-api/badges/master/coverage.svg)](https://gitlab.com/parob/graphql-api/commits/master)
 
 [![pipeline status](https://gitlab.com/parob/graphql-api/badges/master/pipeline.svg)](https://gitlab.com/parob/graphql-api/commits/master)
 
+
 ## Installation
 
 ##### Pip
 ```
 pip install graphql-api
 ```
 
@@ -79,9 +79,7 @@
 print(result.data)
 ```
 
 ``` text
 $ python example.py
 >>> {'isOdd': 'No'}
 ```
-
-
```

### Comparing `graphql-api-1.2.8/README.md` & `graphql-api-1.2.9/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 # GraphQL-API
 Framework for building a GraphQL API with Python
 
 [![coverage report](https://gitlab.com/parob/graphql-api/badges/master/coverage.svg)](https://gitlab.com/parob/graphql-api/commits/master)
 
 [![pipeline status](https://gitlab.com/parob/graphql-api/badges/master/pipeline.svg)](https://gitlab.com/parob/graphql-api/commits/master)
 
+
 ## Installation
 
 ##### Pip
 ```
 pip install graphql-api
 ```
```

### Comparing `graphql-api-1.2.8/graphql_api/api.py` & `graphql-api-1.2.9/graphql_api/api.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/context.py` & `graphql-api-1.2.9/graphql_api/context.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/dataclass_mapping.py` & `graphql-api-1.2.9/graphql_api/dataclass_mapping.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/error.py` & `graphql-api-1.2.9/graphql_api/error.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/executor.py` & `graphql-api-1.2.9/graphql_api/executor.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/mapper.py` & `graphql-api-1.2.9/graphql_api/mapper.py`

 * *Files 0% similar despite different names*

```diff
@@ -276,15 +276,15 @@
             value_type = type(value)
 
             if isinstance(value, GraphQLRemoteObject):
                 value_type = value.python_type
 
             for arg, mapped_type in union_map.items():
                 if issubclass(value_type, arg):
-                    return mapped_type
+                    return mapped_type.name
 
         names = [arg.__name__ for arg in union_args]
         name = f"{''.join(names)}{self.suffix}Union"
 
         return GraphQLUnionType(
             name,
             types=[*union_map.values()],
@@ -368,15 +368,15 @@
         interface_name = f"{name}{self.suffix}Interface"
         description = inspect.getdoc(class_type)
 
         def local_resolve_type():
             local_self = self
 
             def resolve_type(value, info, _type):
-                return local_self.map(type(value))
+                return local_self.map(type(value)).name
             return resolve_type
 
         def local_fields():
             local_self = self
             local_class_funcs = class_funcs
             local_class_type = class_type
             local_name = name
```

### Comparing `graphql-api-1.2.8/graphql_api/middleware.py` & `graphql-api-1.2.9/graphql_api/middleware.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/reduce.py` & `graphql-api-1.2.9/graphql_api/reduce.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/relay.py` & `graphql-api-1.2.9/graphql_api/relay.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/remote.py` & `graphql-api-1.2.9/graphql_api/remote.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/types.py` & `graphql-api-1.2.9/graphql_api/types.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api/utils.py` & `graphql-api-1.2.9/graphql_api/utils.py`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/graphql_api.egg-info/PKG-INFO` & `graphql-api-1.2.9/graphql_api.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,18 +1,17 @@
 Metadata-Version: 2.1
 Name: graphql-api
-Version: 1.2.8
+Version: 1.2.9
 Summary: A framework for building Python GraphQL APIs.
 Home-page: https://gitlab.com/parob/graphql-api
+Download-URL: https://gitlab.com/parob/graphql/-/archive/v1.2.9/graphql-api-v1.2.9.tar.gz
 Author: Robert Parker
 Author-email: rob@parob.com
 License: MIT
-Download-URL: https://gitlab.com/parob/graphql/-/archive/v1.2.8/graphql-api-v1.2.8.tar.gz
 Keywords: GraphQL,GraphQL-API,GraphQLAPI,Server
-Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 Provides-Extra: dev
@@ -21,14 +20,15 @@
 # GraphQL-API
 Framework for building a GraphQL API with Python
 
 [![coverage report](https://gitlab.com/parob/graphql-api/badges/master/coverage.svg)](https://gitlab.com/parob/graphql-api/commits/master)
 
 [![pipeline status](https://gitlab.com/parob/graphql-api/badges/master/pipeline.svg)](https://gitlab.com/parob/graphql-api/commits/master)
 
+
 ## Installation
 
 ##### Pip
 ```
 pip install graphql-api
 ```
 
@@ -79,9 +79,7 @@
 print(result.data)
 ```
 
 ``` text
 $ python example.py
 >>> {'isOdd': 'No'}
 ```
-
-
```

### Comparing `graphql-api-1.2.8/graphql_api.egg-info/SOURCES.txt` & `graphql-api-1.2.9/graphql_api.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `graphql-api-1.2.8/setup.py` & `graphql-api-1.2.9/setup.py`

 * *Files identical despite different names*

