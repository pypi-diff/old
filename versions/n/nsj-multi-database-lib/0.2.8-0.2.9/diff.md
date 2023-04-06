# Comparing `tmp/nsj_multi_database_lib-0.2.8.tar.gz` & `tmp/nsj_multi_database_lib-0.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nsj_multi_database_lib-0.2.8.tar", max compression
+gzip compressed data, was "nsj_multi_database_lib-0.2.9.tar", max compression
```

## Comparing `nsj_multi_database_lib-0.2.8.tar` & `nsj_multi_database_lib-0.2.9.tar`

### file list

```diff
@@ -1,19 +1,19 @@
--rw-r--r--   0        0        0       74 2023-03-28 20:25:56.147472 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/__init__.py
--rw-r--r--   0        0        0      288 2023-04-04 19:57:17.883245 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/crypt_key_sample.py
--rw-r--r--   0        0        0      268 2023-04-04 20:21:13.326375 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/crypt_util.py
--rw-r--r--   0        0        0        0 2023-04-04 20:10:35.147562 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/dao/__init__.py
--rw-r--r--   0        0        0     1889 2023-04-04 22:15:13.749068 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/dao/database.py
--rw-r--r--   0        0        0      746 2023-04-04 22:15:15.361042 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/dao/usuario.py
--rw-r--r--   0        0        0     1815 2023-04-04 19:56:47.149295 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/db_pool_config.py
--rw-r--r--   0        0        0        0 2023-04-04 20:10:34.108804 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/decorator/__init__.py
--rw-r--r--   0        0        0     3187 2023-04-04 20:23:09.091114 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/decorator/multi_database.py
--rw-r--r--   0        0        0        0 2023-04-04 20:10:33.178011 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/dto/__init__.py
--rw-r--r--   0        0        0     1536 2023-03-28 20:25:56.147472 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/dto/database.py
--rw-r--r--   0        0        0        0 2023-04-04 20:10:28.477901 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/entity/__init__.py
--rw-r--r--   0        0        0     1036 2023-04-04 20:09:01.287665 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/entity/database.py
--rw-r--r--   0        0        0      892 2023-04-04 19:56:47.149295 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/env_config.py
--rw-r--r--   0        0        0       45 2023-03-28 20:28:47.947978 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/exception.py
--rw-r--r--   0        0        0     1837 2023-03-28 20:25:56.147472 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/injector_factory.py
--rw-r--r--   0        0        0      447 2023-04-04 19:56:47.177294 nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/settings.py
--rw-r--r--   0        0        0      574 2023-04-04 22:15:32.036775 nsj_multi_database_lib-0.2.8/pyproject.toml
--rw-r--r--   0        0        0      876 1970-01-01 00:00:00.000000 nsj_multi_database_lib-0.2.8/PKG-INFO
+-rw-r--r--   0        0        0       74 2023-03-20 17:20:24.769414 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/__init__.py
+-rw-r--r--   0        0        0      288 2023-04-05 18:58:22.270978 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/crypt_key_sample.py
+-rw-r--r--   0        0        0      268 2023-04-05 18:58:22.270978 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/crypt_util.py
+-rw-r--r--   0        0        0        0 2023-04-05 18:58:22.270978 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/dao/__init__.py
+-rw-r--r--   0        0        0     1891 2023-04-05 18:59:17.463320 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/dao/database.py
+-rw-r--r--   0        0        0      746 2023-03-20 15:23:18.477000 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/dao/usuario.py
+-rw-r--r--   0        0        0     1815 2023-04-04 13:38:20.905178 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/db_pool_config.py
+-rw-r--r--   0        0        0        0 2023-04-05 18:58:22.270978 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/decorator/__init__.py
+-rw-r--r--   0        0        0     3187 2023-04-05 18:58:22.270978 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/decorator/multi_database.py
+-rw-r--r--   0        0        0        0 2023-04-05 18:58:22.270978 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/dto/__init__.py
+-rw-r--r--   0        0        0     1536 2023-03-20 15:23:28.959000 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/dto/database.py
+-rw-r--r--   0        0        0        0 2023-04-05 18:58:22.270978 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/entity/__init__.py
+-rw-r--r--   0        0        0     1036 2023-04-05 18:58:22.270978 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/entity/database.py
+-rw-r--r--   0        0        0      892 2023-04-04 13:38:20.905178 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/env_config.py
+-rw-r--r--   0        0        0       45 2023-04-04 13:38:18.605144 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/exception.py
+-rw-r--r--   0        0        0     1837 2023-03-20 17:41:38.321573 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/injector_factory.py
+-rw-r--r--   0        0        0      447 2023-04-05 18:58:22.270978 nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/settings.py
+-rw-r--r--   0        0        0      574 2023-04-05 18:59:52.271534 nsj_multi_database_lib-0.2.9/pyproject.toml
+-rw-r--r--   0        0        0      876 1970-01-01 00:00:00.000000 nsj_multi_database_lib-0.2.9/PKG-INFO
```

### Comparing `nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/dao/database.py` & `nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/dao/database.py`

 * *Files 2% similar despite different names*

```diff
@@ -31,15 +31,15 @@
         
         return resp[0]
     
     def list_all(self) -> List[EntityBase]:
         databases = []
 
         limit = 20
-        fields = ["id", "host", "porta", "nome", "tenant", "user", "password"]
+        fields = ["id", "host", "porta", "nome", "tenant", '"user"', "password"]
         response = self.list(after=None, limit=limit, fields=fields, order_fields=None, filters=None)
         databases += response
 
         while True:
             if len(response) == limit:
                 last_id = getattr(response[-1], response[-1].get_pk_column_name())
                 response = self.list(after=last_id, limit=limit, fields=fields, order_fields=None, filters=None)
```

### Comparing `nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/dao/usuario.py` & `nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/dao/usuario.py`

 * *Files identical despite different names*

### Comparing `nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/db_pool_config.py` & `nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/db_pool_config.py`

 * *Files identical despite different names*

### Comparing `nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/decorator/multi_database.py` & `nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/decorator/multi_database.py`

 * *Files identical despite different names*

### Comparing `nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/dto/database.py` & `nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/dto/database.py`

 * *Files identical despite different names*

### Comparing `nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/entity/database.py` & `nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/entity/database.py`

 * *Files identical despite different names*

### Comparing `nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/env_config.py` & `nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/env_config.py`

 * *Files identical despite different names*

### Comparing `nsj_multi_database_lib-0.2.8/nsj_multi_database_lib/injector_factory.py` & `nsj_multi_database_lib-0.2.9/nsj_multi_database_lib/injector_factory.py`

 * *Files identical despite different names*

### Comparing `nsj_multi_database_lib-0.2.8/pyproject.toml` & `nsj_multi_database_lib-0.2.9/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "nsj-multi-database-lib"
-version = "0.2.8"
+version = "0.2.9"
 description = "Modulo que permite o uso de múltiplos bancos de dados na mesma aplicação."
 authors = ["Wallace Pinho <wallacepinho@nasajon.com.br>"]
 
 [tool.poetry.dependencies]
 python = "^3.6"
 Flask = "*"
 nsj_rest_lib = "^0.1.6"
```

### Comparing `nsj_multi_database_lib-0.2.8/PKG-INFO` & `nsj_multi_database_lib-0.2.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: nsj-multi-database-lib
-Version: 0.2.8
+Version: 0.2.9
 Summary: Modulo que permite o uso de múltiplos bancos de dados na mesma aplicação.
 Author: Wallace Pinho
 Author-email: wallacepinho@nasajon.com.br
 Requires-Python: >=3.6,<4.0
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
```

