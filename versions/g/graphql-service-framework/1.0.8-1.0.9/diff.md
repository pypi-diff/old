# Comparing `tmp/graphql_service_framework-1.0.8.tar.gz` & `tmp/graphql_service_framework-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "graphql_service_framework-1.0.8.tar", last modified: Thu Apr  6 07:57:02 2023, max compression
+gzip compressed data, was "graphql_service_framework-1.0.9.tar", last modified: Thu Apr  6 09:41:55 2023, max compression
```

## Comparing `graphql_service_framework-1.0.8.tar` & `graphql_service_framework-1.0.9.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 07:57:02.452929 graphql_service_framework-1.0.8/
--rwxrwxrwx   0 root         (0) root         (0)     1069 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/LICENSE
--rwxrwxrwx   0 root         (0) root         (0)       99 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)      693 2023-04-06 07:57:02.452929 graphql_service_framework-1.0.8/PKG-INFO
--rwxrwxrwx   0 root         (0) root         (0)       29 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/README.md
--rw-rw-rw-   0 root         (0) root         (0)        6 2023-04-06 07:57:01.000000 graphql_service_framework-1.0.8/VERSION
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 07:57:02.450929 graphql_service_framework-1.0.8/graphql_service_framework/
--rw-rw-rw-   0 root         (0) root         (0)      351 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/graphql_service_framework/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1383 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/graphql_service_framework/context.py
--rw-rw-rw-   0 root         (0) root         (0)    14811 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/graphql_service_framework/manager.py
--rw-rw-rw-   0 root         (0) root         (0)     9655 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/graphql_service_framework/schema.py
--rw-rw-rw-   0 root         (0) root         (0)     7650 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/graphql_service_framework/schema_tracker.py
--rw-rw-rw-   0 root         (0) root         (0)      237 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/graphql_service_framework/service_manager_default.graphql
--rw-rw-rw-   0 root         (0) root         (0)     4888 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/graphql_service_framework/utils.py
--rw-rw-rw-   0 root         (0) root         (0)       93 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/graphql_service_framework/wsgi.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 07:57:02.452929 graphql_service_framework-1.0.8/graphql_service_framework.egg-info/
--rw-r--r--   0 root         (0) root         (0)      693 2023-04-06 07:57:02.000000 graphql_service_framework-1.0.8/graphql_service_framework.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      619 2023-04-06 07:57:02.000000 graphql_service_framework-1.0.8/graphql_service_framework.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 07:57:02.000000 graphql_service_framework-1.0.8/graphql_service_framework.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      149 2023-04-06 07:57:02.000000 graphql_service_framework-1.0.8/graphql_service_framework.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       26 2023-04-06 07:57:02.000000 graphql_service_framework-1.0.8/graphql_service_framework.egg-info/top_level.txt
--rwxrwxrwx   0 root         (0) root         (0)       79 2023-04-06 07:57:02.453929 graphql_service_framework-1.0.8/setup.cfg
--rwxrwxrwx   0 root         (0) root         (0)     1370 2023-04-06 07:56:52.000000 graphql_service_framework-1.0.8/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:41:55.702175 graphql_service_framework-1.0.9/
+-rwxrwxrwx   0 root         (0) root         (0)     1069 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/LICENSE
+-rwxrwxrwx   0 root         (0) root         (0)       99 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)      693 2023-04-06 09:41:55.702175 graphql_service_framework-1.0.9/PKG-INFO
+-rwxrwxrwx   0 root         (0) root         (0)       29 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/README.md
+-rw-rw-rw-   0 root         (0) root         (0)        6 2023-04-06 09:41:55.000000 graphql_service_framework-1.0.9/VERSION
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:41:55.701175 graphql_service_framework-1.0.9/graphql_service_framework/
+-rw-rw-rw-   0 root         (0) root         (0)      351 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/graphql_service_framework/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1383 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/graphql_service_framework/context.py
+-rw-rw-rw-   0 root         (0) root         (0)    14811 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/graphql_service_framework/manager.py
+-rw-rw-rw-   0 root         (0) root         (0)     9496 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/graphql_service_framework/schema.py
+-rw-rw-rw-   0 root         (0) root         (0)     7650 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/graphql_service_framework/schema_tracker.py
+-rw-rw-rw-   0 root         (0) root         (0)      237 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/graphql_service_framework/service_manager_default.graphql
+-rw-rw-rw-   0 root         (0) root         (0)     4888 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/graphql_service_framework/utils.py
+-rw-rw-rw-   0 root         (0) root         (0)       93 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/graphql_service_framework/wsgi.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 09:41:55.702175 graphql_service_framework-1.0.9/graphql_service_framework.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      693 2023-04-06 09:41:55.000000 graphql_service_framework-1.0.9/graphql_service_framework.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      619 2023-04-06 09:41:55.000000 graphql_service_framework-1.0.9/graphql_service_framework.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 09:41:55.000000 graphql_service_framework-1.0.9/graphql_service_framework.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      149 2023-04-06 09:41:55.000000 graphql_service_framework-1.0.9/graphql_service_framework.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       26 2023-04-06 09:41:55.000000 graphql_service_framework-1.0.9/graphql_service_framework.egg-info/top_level.txt
+-rwxrwxrwx   0 root         (0) root         (0)       79 2023-04-06 09:41:55.703175 graphql_service_framework-1.0.9/setup.cfg
+-rwxrwxrwx   0 root         (0) root         (0)     1370 2023-04-06 09:41:46.000000 graphql_service_framework-1.0.9/setup.py
```

### Comparing `graphql_service_framework-1.0.8/LICENSE` & `graphql_service_framework-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `graphql_service_framework-1.0.8/PKG-INFO` & `graphql_service_framework-1.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: graphql_service_framework
-Version: 1.0.8
+Version: 1.0.9
 Summary: GraphQL Service Framework.
 Home-page: https://gitlab.com/parob/graphql-service-framework
-Download-URL: https://gitlab.com/parob/graphql-service-framework/-/archive/master/graphql-service-framework-v1.0.8.zip
+Download-URL: https://gitlab.com/parob/graphql-service-framework/-/archive/master/graphql-service-framework-v1.0.9.zip
 Author: Robert Parker
 Author-email: rob@parob.com
 License: MIT
 Keywords: GraphQL
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `graphql_service_framework-1.0.8/graphql_service_framework/context.py` & `graphql_service_framework-1.0.9/graphql_service_framework/context.py`

 * *Files identical despite different names*

### Comparing `graphql_service_framework-1.0.8/graphql_service_framework/manager.py` & `graphql_service_framework-1.0.9/graphql_service_framework/manager.py`

 * *Files identical despite different names*

### Comparing `graphql_service_framework-1.0.8/graphql_service_framework/schema.py` & `graphql_service_framework-1.0.9/graphql_service_framework/schema.py`

 * *Files 6% similar despite different names*

```diff
@@ -54,36 +54,31 @@
         if api_version:
             cls.api_version = api_version
         else:
             cls.api_version = "0.0.dev1"
         super().__init__(name, bases, namespace)
 
 
-class ConfigRootType:
-    """
-    For subclasses of ConfigRootType the "create_app" config dict
-    will be available from the config property
-    """
-
-    def __init__(self, config: Dict = None):
-        self.config = config
-
-
+# noinspection PyBroadException
 class Schema(GraphQLRootTypeDelegate, metaclass=APIVersion):
     api_version: str = None
     validate_schema: bool = True
     criticality: Optional[CriticalityLevel] = CriticalityLevel.NonBreaking
     ignore_description_changes: bool = True
 
-    def __new__(cls, url: str = None, *args, **kwargs):
+    def __init__(self, config: Dict = None, url: str = None):
+        self.config = config
+        self.url = url
+
+    def __new__(cls, config: Dict = None, url: str = None, *args, **kwargs):
         schema_class = cls.get_schema_class()
         if cls == schema_class:
             return cls.client(url=url)
 
-        return super(Schema, cls).__new__(cls, *args, **kwargs)
+        return super(Schema, cls).__new__(cls)
 
     @classmethod
     def get_schema_class(cls):
         bases = list(inspect.getmro(cls))
         reversed_bases = list(reversed(bases))
         found_schema = False
         for base in reversed_bases:
@@ -113,81 +108,79 @@
                     cls.criticality,
                     cls.ignore_description_changes
                 )
 
         return schema
 
     @classmethod
-    def create_app(cls, config: Dict = None) -> WSGIApp:
+    def client(cls: TClient, url: str = None) -> TClient:
+        if not url:
+            name = to_snake_case(cls.__name__).upper()
+            url = os.getenv(f"{name}_URL")
+            if not url:
+                raise ValueError(
+                    f"A URL for client {cls.__name__} could not be found"
+                )
+        # noinspection PyTypeChecker
+        return GraphQLRemoteObject(
+            executor=GraphQLRemoteExecutor(url),
+            api=GraphQLAPI(root=cls)
+        )
+
+    @classmethod
+    def graphql_schema(cls) -> GraphQLSchema:
+        return GraphQLAPI(root=cls).graphql_schema()[0]
+
+    def create_app(self, config: Dict = None) -> WSGIApp:
         if not config:
             config = {}
-        service_name = config.get("service_name", to_snake_case(cls.__name__))
+
+        config = {**self.config, **config}
+
+        service_name = config.get(
+            "service_name", to_snake_case(self.__class__.__name__)
+        )
         graphiql_default = config.get("graphiql_default", "")
         relative_path = config.get("http_relative_path", "")
         health_path = config.get("http_health_path", f"{relative_path}/health")
-        api_version = config.get("api_version", cls.api_version)
+        api_version = config.get("api_version", self.__class__.api_version)
         service_management_path = config.get(
             "http_service_management_path", f"{relative_path}/service")
 
         if not graphiql_default:
             try:
-                dirname = os.path.dirname(inspect.getfile(cls))
+                dirname = os.path.dirname(inspect.getfile(self.__class__))
                 graphiql_default = open(
                     os.path.join(dirname, '../graphiql_default.graphql'),
                     mode='r'
                 ).read()
             except Exception:
                 try:
-                    dirname = os.path.dirname(inspect.getfile(cls))
+                    dirname = os.path.dirname(inspect.getfile(self.__class__))
                     graphiql_default = open(
                         os.path.join(dirname, '../.graphql'),
                         mode='r'
                     ).read()
                 except Exception:
                     pass
 
-        if issubclass(cls, ConfigRootType) and config:
-            cls: Type[ConfigRootType]
-            root_value = cls(config=config)
-        else:
-            root_value = None
-
         graphql_http_server = GraphQLHTTPServer.from_api(
-            api=GraphQLAPI(root=cls),
-            root_value=root_value,
+            api=GraphQLAPI(root=self.__class__),
+            root_value=self,
             graphiql_default_query=graphiql_default,
             health_path=health_path
         )
 
         app = ServiceContextMiddleware(
             graphql_http_server.app(),
             ServiceManager(name=service_name, api_version=api_version),
             service_management_path=service_management_path
         )
         return app
 
-    @classmethod
-    def client(cls: TClient, url: str = None) -> TClient:
-        if not url:
-            name = to_snake_case(cls.__name__).upper()
-            url = os.getenv(f"{name}_URL")
-            if not url:
-                raise ValueError(
-                    f"A URL for client {cls.__name__} could not be found"
-                )
-        # noinspection PyTypeChecker
-        return GraphQLRemoteObject(
-            executor=GraphQLRemoteExecutor(url),
-            api=GraphQLAPI(root=cls)
-        )
-
-    @classmethod
-    def graphql_schema(cls) -> GraphQLSchema:
-        return GraphQLAPI(root=cls).graphql_schema()[0]
-
 
 def validate(
         graphql_schema: GraphQLSchema,
         service_schema: Type[Schema],
         criticality: CriticalityLevel,
         ignore_description_changes: bool = True
 ):
```

### Comparing `graphql_service_framework-1.0.8/graphql_service_framework/schema_tracker.py` & `graphql_service_framework-1.0.9/graphql_service_framework/schema_tracker.py`

 * *Files identical despite different names*

### Comparing `graphql_service_framework-1.0.8/graphql_service_framework/utils.py` & `graphql_service_framework-1.0.9/graphql_service_framework/utils.py`

 * *Files identical despite different names*

### Comparing `graphql_service_framework-1.0.8/graphql_service_framework.egg-info/PKG-INFO` & `graphql_service_framework-1.0.9/graphql_service_framework.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 Metadata-Version: 2.1
 Name: graphql-service-framework
-Version: 1.0.8
+Version: 1.0.9
 Summary: GraphQL Service Framework.
 Home-page: https://gitlab.com/parob/graphql-service-framework
-Download-URL: https://gitlab.com/parob/graphql-service-framework/-/archive/master/graphql-service-framework-v1.0.8.zip
+Download-URL: https://gitlab.com/parob/graphql-service-framework/-/archive/master/graphql-service-framework-v1.0.9.zip
 Author: Robert Parker
 Author-email: rob@parob.com
 License: MIT
 Keywords: GraphQL
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `graphql_service_framework-1.0.8/graphql_service_framework.egg-info/SOURCES.txt` & `graphql_service_framework-1.0.9/graphql_service_framework.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `graphql_service_framework-1.0.8/setup.py` & `graphql_service_framework-1.0.9/setup.py`

 * *Files identical despite different names*

