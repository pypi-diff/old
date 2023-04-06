# Comparing `tmp/mythic-0.1.0rc2.tar.gz` & `tmp/mythic-0.1.0rc3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mythic-0.1.0rc2.tar", last modified: Tue Mar 28 14:57:28 2023, max compression
+gzip compressed data, was "mythic-0.1.0rc3.tar", last modified: Thu Apr  6 15:01:43 2023, max compression
```

## Comparing `mythic-0.1.0rc2.tar` & `mythic-0.1.0rc3.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 itsafeature   (501) staff       (20)        0 2023-03-28 14:57:28.322476 mythic-0.1.0rc2/
--rw-r--r--   0 itsafeature   (501) staff       (20)     2058 2023-03-28 14:57:28.322087 mythic-0.1.0rc2/PKG-INFO
--rwxr-xr-x   0 itsafeature   (501) staff       (20)     1710 2023-03-28 14:56:54.000000 mythic-0.1.0rc2/README.md
-drwxr-xr-x   0 itsafeature   (501) staff       (20)        0 2023-03-28 14:57:28.319705 mythic-0.1.0rc2/mythic/
--rwxr-xr-x   0 itsafeature   (501) staff       (20)       29 2022-01-31 22:46:05.000000 mythic-0.1.0rc2/mythic/__init__.py
--rw-r--r--   0 itsafeature   (501) staff       (20)     6998 2023-03-27 23:12:17.000000 mythic-0.1.0rc2/mythic/graphql_queries.py
--rw-r--r--   0 itsafeature   (501) staff       (20)    93379 2023-03-28 14:45:47.000000 mythic-0.1.0rc2/mythic/mythic.py
--rw-r--r--   0 itsafeature   (501) staff       (20)     3623 2023-03-28 14:56:43.000000 mythic-0.1.0rc2/mythic/mythic_classes.py
--rw-r--r--   0 itsafeature   (501) staff       (20)        1 2022-03-21 21:08:15.000000 mythic-0.1.0rc2/mythic/mythic_exceptions.py
--rw-r--r--   0 itsafeature   (501) staff       (20)     7582 2023-03-22 20:38:43.000000 mythic-0.1.0rc2/mythic/mythic_utilities.py
-drwxr-xr-x   0 itsafeature   (501) staff       (20)        0 2023-03-28 14:57:28.321624 mythic-0.1.0rc2/mythic.egg-info/
--rw-r--r--   0 itsafeature   (501) staff       (20)     2058 2023-03-28 14:57:28.000000 mythic-0.1.0rc2/mythic.egg-info/PKG-INFO
--rw-r--r--   0 itsafeature   (501) staff       (20)      309 2023-03-28 14:57:28.000000 mythic-0.1.0rc2/mythic.egg-info/SOURCES.txt
--rw-r--r--   0 itsafeature   (501) staff       (20)        1 2023-03-28 14:57:28.000000 mythic-0.1.0rc2/mythic.egg-info/dependency_links.txt
--rw-r--r--   0 itsafeature   (501) staff       (20)       40 2023-03-28 14:57:28.000000 mythic-0.1.0rc2/mythic.egg-info/requires.txt
--rw-r--r--   0 itsafeature   (501) staff       (20)        7 2023-03-28 14:57:28.000000 mythic-0.1.0rc2/mythic.egg-info/top_level.txt
--rw-r--r--   0 itsafeature   (501) staff       (20)       38 2023-03-28 14:57:28.322594 mythic-0.1.0rc2/setup.cfg
--rwxr-xr-x   0 itsafeature   (501) staff       (20)      821 2023-03-28 14:56:12.000000 mythic-0.1.0rc2/setup.py
+drwxr-xr-x   0 itsafeature   (501) staff       (20)        0 2023-04-06 15:01:43.364386 mythic-0.1.0rc3/
+-rw-r--r--   0 itsafeature   (501) staff       (20)     2059 2023-04-06 15:01:43.364003 mythic-0.1.0rc3/PKG-INFO
+-rwxr-xr-x   0 itsafeature   (501) staff       (20)     1711 2023-04-06 15:01:27.000000 mythic-0.1.0rc3/README.md
+drwxr-xr-x   0 itsafeature   (501) staff       (20)        0 2023-04-06 15:01:43.361692 mythic-0.1.0rc3/mythic/
+-rwxr-xr-x   0 itsafeature   (501) staff       (20)       29 2022-01-31 22:46:05.000000 mythic-0.1.0rc3/mythic/__init__.py
+-rw-r--r--   0 itsafeature   (501) staff       (20)     7198 2023-04-06 01:01:59.000000 mythic-0.1.0rc3/mythic/graphql_queries.py
+-rw-r--r--   0 itsafeature   (501) staff       (20)    94328 2023-04-06 14:43:47.000000 mythic-0.1.0rc3/mythic/mythic.py
+-rw-r--r--   0 itsafeature   (501) staff       (20)     3623 2023-04-06 15:00:49.000000 mythic-0.1.0rc3/mythic/mythic_classes.py
+-rw-r--r--   0 itsafeature   (501) staff       (20)        1 2022-03-21 21:08:15.000000 mythic-0.1.0rc3/mythic/mythic_exceptions.py
+-rw-r--r--   0 itsafeature   (501) staff       (20)     7582 2023-03-22 20:38:43.000000 mythic-0.1.0rc3/mythic/mythic_utilities.py
+drwxr-xr-x   0 itsafeature   (501) staff       (20)        0 2023-04-06 15:01:43.363529 mythic-0.1.0rc3/mythic.egg-info/
+-rw-r--r--   0 itsafeature   (501) staff       (20)     2059 2023-04-06 15:01:43.000000 mythic-0.1.0rc3/mythic.egg-info/PKG-INFO
+-rw-r--r--   0 itsafeature   (501) staff       (20)      309 2023-04-06 15:01:43.000000 mythic-0.1.0rc3/mythic.egg-info/SOURCES.txt
+-rw-r--r--   0 itsafeature   (501) staff       (20)        1 2023-04-06 15:01:43.000000 mythic-0.1.0rc3/mythic.egg-info/dependency_links.txt
+-rw-r--r--   0 itsafeature   (501) staff       (20)       40 2023-04-06 15:01:43.000000 mythic-0.1.0rc3/mythic.egg-info/requires.txt
+-rw-r--r--   0 itsafeature   (501) staff       (20)        7 2023-04-06 15:01:43.000000 mythic-0.1.0rc3/mythic.egg-info/top_level.txt
+-rw-r--r--   0 itsafeature   (501) staff       (20)       38 2023-04-06 15:01:43.364503 mythic-0.1.0rc3/setup.cfg
+-rwxr-xr-x   0 itsafeature   (501) staff       (20)      821 2023-04-06 14:47:24.000000 mythic-0.1.0rc3/setup.py
```

### Comparing `mythic-0.1.0rc2/PKG-INFO` & `mythic-0.1.0rc3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mythic
-Version: 0.1.0rc2
+Version: 0.1.0rc3
 Summary: Interact with Mythic C2 Framework Instances
 Home-page: https://docs.mythic-c2.net/scripting
 Author: @its_a_feature_
 Author-email: 
 License: BSD3
 Classifier: License :: Other/Proprietary License
 Classifier: Programming Language :: Python :: 3.10
@@ -33,13 +33,13 @@
 Version 0.0.21-25 of the `mythic` package supports version 2.2.8+ of the Mythic project (reports as version "3").
 
 Version 0.0.26 of the `mythic` package supports version 2.3+ of the Mythic project (reports as version "3").
 
 Version 0.0.29-0.0.36 of the `mythic` package supports version 2.3+ of the Mythic project utilizing the new GraphQL endpoints and reports as version "3".
 This will be the last version that supports the old mythic_rest interface. Starting with version 0.1.0, the `mythic` PyPi package will only support the new GraphQL interface and will report as version "4".
 
-Version 0.1.0rc1 of the `mythic` package supports version 3.0 of the Mythic project utilizing the new GraphQL endpoints.
+Version 0.1.0rc1+ of the `mythic` package supports version 3.0 of the Mythic project utilizing the new GraphQL endpoints.
 
 # Information
 
 The Jupyter Notebook container within Mythic provides many examples on how to use the package. 
 The `mythic` package leverages async HTTP requests and WebSocket connections, so it's important to make sure your codebase is running asynchronously.
```

### Comparing `mythic-0.1.0rc2/README.md` & `mythic-0.1.0rc3/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -21,13 +21,13 @@
 Version 0.0.21-25 of the `mythic` package supports version 2.2.8+ of the Mythic project (reports as version "3").
 
 Version 0.0.26 of the `mythic` package supports version 2.3+ of the Mythic project (reports as version "3").
 
 Version 0.0.29-0.0.36 of the `mythic` package supports version 2.3+ of the Mythic project utilizing the new GraphQL endpoints and reports as version "3".
 This will be the last version that supports the old mythic_rest interface. Starting with version 0.1.0, the `mythic` PyPi package will only support the new GraphQL interface and will report as version "4".
 
-Version 0.1.0rc1 of the `mythic` package supports version 3.0 of the Mythic project utilizing the new GraphQL endpoints.
+Version 0.1.0rc1+ of the `mythic` package supports version 3.0 of the Mythic project utilizing the new GraphQL endpoints.
 
 # Information
 
 The Jupyter Notebook container within Mythic provides many examples on how to use the package. 
 The `mythic` package leverages async HTTP requests and WebSocket connections, so it's important to make sure your codebase is running asynchronously.
```

### Comparing `mythic-0.1.0rc2/mythic/graphql_queries.py` & `mythic-0.1.0rc3/mythic/graphql_queries.py`

 * *Files 1% similar despite different names*

```diff
@@ -85,14 +85,25 @@
         can_have_children
         name_text
         parent_path_text
         full_path_text
         metadata
     }
 """
+operator_fragment = """
+    fragment operator_fragment on operator {
+        id
+        username
+        admin
+        active
+        last_login
+        current_operation_id
+        deleted
+    }
+"""
 callback_fragment = """
     fragment callback_fragment on callback {
         architecture
         description
         domain
         external_ip
         host
```

### Comparing `mythic-0.1.0rc2/mythic/mythic.py` & `mythic-0.1.0rc3/mythic/mythic.py`

 * *Files 0% similar despite different names*

```diff
@@ -585,15 +585,14 @@
     }}
     {graphql_queries.task_fragment if custom_return_attributes is None else ''}
     """
     variables = {"task_display_id": task_display_id}
     async for result in mythic_utilities.graphql_subscription(
         mythic=mythic, query=subscription, variables=variables, timeout=timeout
     ):
-        print(result)
         if len(result["task_stream"]) != 1:
             raise Exception("task not found")
         if "error" in result["task_stream"][0]["status"] or result["task_stream"][0]["completed"]:
             return result["task_stream"][0]
 
 
 async def issue_task_all_active_callbacks(
@@ -1327,14 +1326,46 @@
         }
         """,
         variables={"user_id": resp["operator"][0]["id"], "new_password": new_password, "old_password": old_password},
     )
     return response["updatePassword"]
 
 
+async def get_operator(mythic: mythic_classes.Mythic, username: str, custom_return_attributes: str = None) -> dict:
+    resp = await execute_custom_query(
+        mythic=mythic,
+        query=f"""
+        query getUserID($username: String!) {{
+            operator(where: {{username: {{_eq: $username}}}}){{
+                {custom_return_attributes if custom_return_attributes is not None else '...operator_fragment'}
+            }}
+        }}
+        {graphql_queries.operator_fragment if custom_return_attributes is None else ''}
+        """,
+        variables={"username": username}
+    )
+    return resp
+
+
+async def get_me(mythic: mythic_classes.Mythic) -> dict:
+    resp = await execute_custom_query(
+        mythic=mythic,
+        query=f"""
+        query getMe {{
+            meHook{{
+                status
+                error
+                current_operation_id
+                current_operation
+            }}
+        }}
+        """,
+    )
+    return resp
+
 # ########## File Functions ##############
 
 
 async def register_file(
     mythic: mythic_classes.Mythic, filename: str, contents: bytes
 ) -> str:
     """
```

### Comparing `mythic-0.1.0rc2/mythic/mythic_classes.py` & `mythic-0.1.0rc3/mythic/mythic_classes.py`

 * *Files 0% similar despite different names*

```diff
@@ -24,15 +24,15 @@
         self.server_ip = server_ip
         self.server_port = server_port
         self.server_api_version = server_api_version
         self.ssl = ssl
         self.http = "http://" if not ssl else "https://"
         self.ws = "ws://" if not ssl else "wss://"
         self.global_timeout = global_timeout if global_timeout is not None else -1
-        self.scripting_version = "0.1.0rc2"
+        self.scripting_version = "0.1.0rc3"
         self.current_operation_id = 0
         self.operator_id = None
         self.operator = None
         self.schema = schema
 
     def __str__(self):
         return json.dumps(
```

### Comparing `mythic-0.1.0rc2/mythic/mythic_utilities.py` & `mythic-0.1.0rc3/mythic/mythic_utilities.py`

 * *Files identical despite different names*

### Comparing `mythic-0.1.0rc2/mythic.egg-info/PKG-INFO` & `mythic-0.1.0rc3/mythic.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mythic
-Version: 0.1.0rc2
+Version: 0.1.0rc3
 Summary: Interact with Mythic C2 Framework Instances
 Home-page: https://docs.mythic-c2.net/scripting
 Author: @its_a_feature_
 Author-email: 
 License: BSD3
 Classifier: License :: Other/Proprietary License
 Classifier: Programming Language :: Python :: 3.10
@@ -33,13 +33,13 @@
 Version 0.0.21-25 of the `mythic` package supports version 2.2.8+ of the Mythic project (reports as version "3").
 
 Version 0.0.26 of the `mythic` package supports version 2.3+ of the Mythic project (reports as version "3").
 
 Version 0.0.29-0.0.36 of the `mythic` package supports version 2.3+ of the Mythic project utilizing the new GraphQL endpoints and reports as version "3".
 This will be the last version that supports the old mythic_rest interface. Starting with version 0.1.0, the `mythic` PyPi package will only support the new GraphQL interface and will report as version "4".
 
-Version 0.1.0rc1 of the `mythic` package supports version 3.0 of the Mythic project utilizing the new GraphQL endpoints.
+Version 0.1.0rc1+ of the `mythic` package supports version 3.0 of the Mythic project utilizing the new GraphQL endpoints.
 
 # Information
 
 The Jupyter Notebook container within Mythic provides many examples on how to use the package. 
 The `mythic` package leverages async HTTP requests and WebSocket connections, so it's important to make sure your codebase is running asynchronously.
```

### Comparing `mythic-0.1.0rc2/setup.py` & `mythic-0.1.0rc3/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 
 # The text of the README file
 README = (HERE / "README.md").read_text()
 
 # This call to setup() does all the work
 setup(
     name="mythic",
-    version="0.1.0rc2",
+    version="0.1.0rc3",
     description="Interact with Mythic C2 Framework Instances",
     long_description=README,
     long_description_content_type="text/markdown",
     url="https://docs.mythic-c2.net/scripting",
     author="@its_a_feature_",
     author_email="",
     license="BSD3",
```

