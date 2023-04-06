# Comparing `tmp/asbestos_snow-1.1.0.tar.gz` & `tmp/asbestos_snow-1.2.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "asbestos_snow-1.1.0.tar", max compression
+gzip compressed data, was "asbestos_snow-1.2.0.tar", max compression
```

## Comparing `asbestos_snow-1.1.0.tar` & `asbestos_snow-1.2.0.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     1077 2023-03-24 18:43:53.196175 asbestos_snow-1.1.0/LICENSE.md
--rw-r--r--   0        0        0     2362 2023-03-24 18:43:53.196175 asbestos_snow-1.1.0/README.md
--rw-r--r--   0        0        0      367 2023-03-24 18:43:53.196175 asbestos_snow-1.1.0/asbestos/__init__.py
--rw-r--r--   0        0        0    17321 2023-03-24 18:43:53.196175 asbestos_snow-1.1.0/asbestos/asbestos.py
--rw-r--r--   0        0        0      360 2023-03-24 18:43:53.196175 asbestos_snow-1.1.0/asbestos/exceptions.py
--rw-r--r--   0        0        0     1618 2023-03-24 18:43:53.200175 asbestos_snow-1.1.0/pyproject.toml
--rw-r--r--   0        0        0     3440 1970-01-01 00:00:00.000000 asbestos_snow-1.1.0/PKG-INFO
+-rw-r--r--   0        0        0     1077 2023-04-06 15:57:51.958541 asbestos_snow-1.2.0/LICENSE.md
+-rw-r--r--   0        0        0     2362 2023-04-06 15:57:51.958541 asbestos_snow-1.2.0/README.md
+-rw-r--r--   0        0        0      367 2023-04-06 15:57:51.958541 asbestos_snow-1.2.0/asbestos/__init__.py
+-rw-r--r--   0        0        0    18017 2023-04-06 15:57:51.958541 asbestos_snow-1.2.0/asbestos/asbestos.py
+-rw-r--r--   0        0        0      360 2023-04-06 15:57:51.958541 asbestos_snow-1.2.0/asbestos/exceptions.py
+-rw-r--r--   0        0        0     1618 2023-04-06 15:57:51.958541 asbestos_snow-1.2.0/pyproject.toml
+-rw-r--r--   0        0        0     3440 1970-01-01 00:00:00.000000 asbestos_snow-1.2.0/PKG-INFO
```

### Comparing `asbestos_snow-1.1.0/LICENSE.md` & `asbestos_snow-1.2.0/LICENSE.md`

 * *Files identical despite different names*

### Comparing `asbestos_snow-1.1.0/README.md` & `asbestos_snow-1.2.0/README.md`

 * *Files identical despite different names*

### Comparing `asbestos_snow-1.1.0/asbestos/asbestos.py` & `asbestos_snow-1.2.0/asbestos/asbestos.py`

 * *Files 6% similar despite different names*

```diff
@@ -313,23 +313,24 @@
 
         Saves the SQL and any passed-in data to the cursor and starts the
         process of finding your pre-saved response. To get the data, you will
         need to call one of the fetch* methods listed below.
         """
         self.query = query
         self.data = inserted_data
-        self._get()
+        self._get(remove_ephemeral=False)
 
     def execute_async(self, *args, **kwargs) -> None:
         """Functions the same as `.execute()`."""
         self.execute(*args, **kwargs)
 
-    def _get(self) -> dict | list[dict]:
+    def _get(self, remove_ephemeral: bool = True) -> dict | list[dict]:
         resp = self.config.lookup_query(self.query, self.data)
-        self.config.remove_ephemeral_response(resp)
+        if remove_ephemeral:
+            self.config.remove_ephemeral_response(resp)
         self.config.last_run_query = resp
         return OVERRIDE_RESPONSE if OVERRIDE_RESPONSE else resp.response
 
     def fetchone(self) -> dict:
         """
         Return the first result from the saved response for a query.
 
@@ -362,15 +363,18 @@
         with asbestos_cursor() as cursor:
             cursor.execute("A")
             resp = cursor.fetchall()
 
         # resp = [{'a':1}, {'b': 2}]
         ```
         """
-        return self.config.last_run_query.response
+        resp = self._get()
+        if not isinstance(resp, list) and resp != OVERRIDE_RESPONSE:
+            return list(resp)
+        return resp
 
     def fetchmany(self, size: int = None) -> list[dict]:
         """
         Return a paged subset of the saved response.
 
         Uses `cursor.arraysize` to control the page size or just pass your
         requested page size into the function: `.fetchmany(200)`. Automatically
@@ -396,19 +400,28 @@
         if self.last_paginated_query != self.config.last_run_query.sfqid:
             # this is the first time we're paginating here
             self.last_page_start = 0
             self.last_paginated_query: int = self.config.last_run_query.sfqid
         if query_forced_page_size := self.config.last_run_query.force_pagination_size:
             size = query_forced_page_size
 
-        response = self.config.last_run_query.response[
-            self.last_page_start : size + self.last_page_start
-        ]
-        self.last_page_start += size
-        return response
+        resp = self._get(remove_ephemeral=False)
+        if resp == OVERRIDE_RESPONSE:
+            # shortcut if the override has manually been set
+            return resp
+
+        # everything this normally handles should be one of these types.
+        if resp and isinstance(resp, (list, tuple)):
+            response = resp[self.last_page_start : size + self.last_page_start]
+            self.last_page_start += size
+            if len(response) == 0:
+                self.config.remove_ephemeral_response(self.config.last_run_query)
+            return response
+        self.config.remove_ephemeral_response(self.config.last_run_query)
+        return list(resp) if not isinstance(resp, list) else resp
 
     def close(self) -> None:
         """
         Reset the queries and "close" the connection.
         """
         self.config.clear_queries()
         return
```

### Comparing `asbestos_snow-1.1.0/pyproject.toml` & `asbestos_snow-1.2.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "asbestos-snow"
-version = "1.1.0"
+version = "1.2.0"
 description = "An easy way to mock Snowflake connections in Python!"
 authors = ["Joe Kaufeld <jkaufeld@spoton.com>", "SpotOn <opensource@spoton.com>"]
 readme = "README.md"
 packages = [{include = "asbestos"}]
 repository = "https://github.com/spotoninc/asbestos"
 documentation = "https://spotoninc.github.io/asbestos"
 classifiers = [
```

### Comparing `asbestos_snow-1.1.0/PKG-INFO` & `asbestos_snow-1.2.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: asbestos-snow
-Version: 1.1.0
+Version: 1.2.0
 Summary: An easy way to mock Snowflake connections in Python!
 Home-page: https://github.com/spotoninc/asbestos
 Author: Joe Kaufeld
 Author-email: jkaufeld@spoton.com
 Requires-Python: >=3.10,<4.0
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Developers
```

