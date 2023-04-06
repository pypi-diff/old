# Comparing `tmp/django-iris-0.1.9b1.tar.gz` & `tmp/django-iris-0.2.0b1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-iris-0.1.9b1.tar", last modified: Sat Mar 19 18:59:31 2022, max compression
+gzip compressed data, was "django-iris-0.2.0b1.tar", last modified: Thu Apr  6 11:48:36 2023, max compression
```

## Comparing `django-iris-0.1.9b1.tar` & `django-iris-0.2.0b1.tar`

### file list

```diff
@@ -1,21 +1,61 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-19 18:59:31.974400 django-iris-0.1.9b1/
--rw-r--r--   0 runner    (1001) docker     (121)     1075 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     1536 2022-03-19 18:59:31.974400 django-iris-0.1.9b1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      607 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-19 18:59:31.974400 django-iris-0.1.9b1/django_iris/
--rw-r--r--   0 runner    (1001) docker     (121)      314 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/django_iris/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     6128 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/django_iris/base.py
--rw-r--r--   0 runner    (1001) docker     (121)      199 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/django_iris/creation.py
--rw-r--r--   0 runner    (1001) docker     (121)     1715 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/django_iris/cursor.py
--rw-r--r--   0 runner    (1001) docker     (121)      687 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/django_iris/features.py
--rw-r--r--   0 runner    (1001) docker     (121)     9652 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/django_iris/introspection.py
--rw-r--r--   0 runner    (1001) docker     (121)     3101 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/django_iris/operations.py
--rw-r--r--   0 runner    (1001) docker     (121)      981 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/django_iris/schema.py
--rw-r--r--   0 runner    (1001) docker     (121)      233 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/django_iris/validation.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-03-19 18:59:31.974400 django-iris-0.1.9b1/django_iris.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     1536 2022-03-19 18:59:31.000000 django-iris-0.1.9b1/django_iris.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      393 2022-03-19 18:59:31.000000 django-iris-0.1.9b1/django_iris.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)      123 2022-03-19 18:59:31.000000 django-iris-0.1.9b1/django_iris.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       12 2022-03-19 18:59:31.000000 django-iris-0.1.9b1/django_iris.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      896 2022-03-19 18:59:31.974400 django-iris-0.1.9b1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)      541 2022-03-19 18:59:16.000000 django-iris-0.1.9b1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:48:36.045909 django-iris-0.2.0b1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1075 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 11:48:36.045909 django-iris-0.2.0b1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      607 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:48:36.041909 django-iris-0.2.0b1/django_iris/
+-rw-r--r--   0 runner    (1001) docker     (123)     4245 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7093 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7738 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/compiler.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1521 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/creation.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1352 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/cursor.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8066 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/features.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10304 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/introspection.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13175 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/operations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4148 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/schema.py
+-rw-r--r--   0 runner    (1001) docker     (123)      795 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/django_iris/validation.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:48:36.041909 django-iris-0.2.0b1/django_iris.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1516 2023-04-06 11:48:36.000000 django-iris-0.2.0b1/django_iris.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1662 2023-04-06 11:48:36.000000 django-iris-0.2.0b1/django_iris.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-04-06 11:48:36.000000 django-iris-0.2.0b1/django_iris.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       41 2023-04-06 11:48:36.000000 django-iris-0.2.0b1/django_iris.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:48:36.045909 django-iris-0.2.0b1/intersystems_iris/
+-rw-rw-rw-   0 runner    (1001) docker     (123)      299 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_BufferReader.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1337 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_BufferWriter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1896 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_ConnectionInformation.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      578 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_ConnectionParameters.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1483 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_Constant.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    20104 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_DBList.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2311 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_Device.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      618 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_GatewayContext.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)       96 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_GatewayException.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2735 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_GatewayUtility.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    49548 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRIS.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    21467 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISConnection.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2614 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISEmbedded.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    12049 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISGlobalNode.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      797 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISGlobalNodeView.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6906 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISIterator.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    10247 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISList.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6756 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISNative.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)       82 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISOREF.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    14456 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISObject.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4905 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_IRISReference.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     6643 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_InStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4130 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_LegacyIterator.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      354 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_ListItem.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     2966 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_ListReader.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     5515 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_ListWriter.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     3797 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_LogFileStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1662 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_MessageHeader.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1327 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_OutStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1963 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_PrintStream.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)    41638 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_PythonGateway.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     4330 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/_SharedMemorySocket.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)     1773 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/__init__.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      218 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/intersystems_iris/__main__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:48:36.045909 django-iris-0.2.0b1/irisnative/
+-rw-rw-rw-   0 runner    (1001) docker     (123)      665 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/irisnative/_IRISNative.py
+-rw-rw-rw-   0 runner    (1001) docker     (123)      341 2023-04-06 11:48:35.000000 django-iris-0.2.0b1/irisnative/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      927 2023-04-06 11:48:36.045909 django-iris-0.2.0b1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      541 2023-04-06 11:48:22.000000 django-iris-0.2.0b1/setup.py
```

### Comparing `django-iris-0.1.9b1/LICENSE` & `django-iris-0.2.0b1/LICENSE`

 * *Files identical despite different names*

### Comparing `django-iris-0.1.9b1/PKG-INFO` & `django-iris-0.2.0b1/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,18 +1,17 @@
 Metadata-Version: 2.1
 Name: django-iris
-Version: 0.1.9b1
+Version: 0.2.0b1
 Summary: Django backend for InterSystems IRIS
 Home-page: https://github.com/caretdev/django-iris
 Maintainer: CaretDev
 Maintainer-email: dmitry@caretdev.com
 License: MIT
 Project-URL: Source, https://github.com/caretdev/django-iris
 Project-URL: Tracker, https://github.com/caretdev/django-iris/issues
-Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Framework :: Django
 Classifier: Framework :: Django :: 4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
@@ -54,9 +53,7 @@
         'USER': '_SYSTEM',
         'PASSWORD': 'SYS',
         'HOST': 'localhost',
         'PORT': '1972',
     },
 }
 ```
-
-
```

### Comparing `django-iris-0.1.9b1/README.md` & `django-iris-0.2.0b1/README.md`

 * *Files identical despite different names*

### Comparing `django-iris-0.1.9b1/django_iris/base.py` & `django-iris-0.2.0b1/django_iris/base.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,53 +1,41 @@
 from django.db.backends.base.base import BaseDatabaseWrapper
 from django.db.backends.base.client import BaseDatabaseClient
 from django.db.backends.base.creation import BaseDatabaseCreation
 from django.core.exceptions import ImproperlyConfigured
 from django.utils.asyncio import async_unsafe
+from django.utils.functional import cached_property
+from django.db.utils import DatabaseErrorWrapper
+from django.db.backends.utils import debug_transaction
 
 from .introspection import DatabaseIntrospection
 from .features import DatabaseFeatures
 from .schema import DatabaseSchemaEditor
 from .operations import DatabaseOperations
 from .cursor import CursorWrapper
 from .creation import DatabaseCreation
 from .validation import DatabaseValidation
 
-import iris as Database
-
-
-Database.Warning = type("StandardError", (object,), {})
-Database.Error = type("StandardError", (object,), {})
-
-Database.InterfaceError = type("Error", (object,), {})
-
-Database.DatabaseError = type("Error", (object,), {})
-Database.DataError = type("DatabaseError", (object,), {})
-Database.OperationalError = type("DatabaseError", (object,), {})
-Database.IntegrityError = type("DatabaseError", (object,), {})
-Database.InternalError = type("DatabaseError", (object,), {})
-Database.ProgrammingError = type("DatabaseError", (object,), {})
-Database.NotSupportedError = type("DatabaseError", (object,), {})
+import intersystems_iris.dbapi._DBAPI as Database
 
 
 def ignore(*args, **kwargs):
     pass
 
 
 class DatabaseClient(BaseDatabaseClient):
     runshell = ignore
 
-
 class DatabaseWrapper(BaseDatabaseWrapper):
     vendor = 'intersystems'
     display_name = 'InterSystems IRIS'
 
     data_types = {
-        'AutoField': 'INTEGER AUTO_INCREMENT',
-        'BigAutoField': 'BIGINT AUTO_INCREMENT',
+        'AutoField': 'IDENTITY',
+        'BigAutoField': 'IDENTITY',
         'BinaryField': 'LONG BINARY',
         'BooleanField': 'BIT',
         'CharField': 'VARCHAR(%(max_length)s)',
         'DateField': 'DATE',
         'DateTimeField': 'TIMESTAMP',
         'DecimalField': 'NUMERIC(%(max_digits)s, %(decimal_places)s)',
         'DurationField': 'BIGINT',
@@ -60,88 +48,101 @@
         'GenericIPAddressField': 'CHAR(39)',
         'JSONField': 'VARCHAR(32768)',
         'OneToOneField': 'INTEGER',
         'PositiveBigIntegerField': 'BIGINT',
         'PositiveIntegerField': 'INTEGER',
         'PositiveSmallIntegerField': 'SMALLINT',
         'SlugField': 'VARCHAR(%(max_length)s)',
-        'SmallAutoField': 'SMALLINT AUTO_INCREMENT',
+        'SmallAutoField': 'IDENTITY',
         'SmallIntegerField': 'SMALLINT',
-        # 'TextField': 'LONG',
-        # Stream not supported yet by db-api
-        'TextField': 'VARCHAR(255)',
+        'TextField': 'TEXT',
         'TimeField': 'TIME(6)',
         'UUIDField': 'CHAR(32)',
     }
 
     operators = {
         'exact': '= %s',
         'iexact': "LIKE %s ESCAPE '\\'",
         'contains': "LIKE %s ESCAPE '\\'",
         'icontains': "LIKE %s ESCAPE '\\'",
-        # 'regex': 'REGEXP %s',
-        # 'iregex': "REGEXP '(?i)' || %s",
+        # 'regex': "%%%%MATCHES %s ESCAPE '\\'",
+        # 'iregex': "%%%%MATCHES %s ESCAPE '\\'",
         'gt': '> %s',
         'gte': '>= %s',
         'lt': '< %s',
         'lte': '<= %s',
-        'startswith': "%STARTSWITH %s",
+        'startswith': "LIKE %s ESCAPE '\\'",
         'endswith': "LIKE %s ESCAPE '\\'",
-        'istartswith': "%STARTSWITH %s",
+        'istartswith': "LIKE %s ESCAPE '\\'",
         'iendswith': "LIKE %s ESCAPE '\\'",
+    }
+
+    pattern_esc = r"REPLACE(REPLACE(REPLACE({}, '\', '\\'), '%%', '\%%'), '_', '\_')"
+    pattern_ops = {
+        "contains": "LIKE '%%' || {} || '%%'",
+        "icontains": "LIKE '%%' || UPPER({}) || '%%'",
+        "startswith": "LIKE {} || '%%'",
+        "istartswith": "LIKE UPPER({}) || '%%'",
+        "endswith": "LIKE '%%' || {}",
+        "iendswith": "LIKE '%%' || UPPER({})",
 
     }
+
     Database = Database
 
-    _commit = ignore
-    _rollback = ignore
-    _close = ignore
-    _savepoint = ignore
-    _savepoint_commit = ignore
-    _savepoint_rollback = ignore
-    _set_autocommit = ignore
+    # _commit = ignore
+    # _rollback = ignore
+    # _savepoint = ignore
+    # _savepoint_commit = ignore
+    # _savepoint_rollback = ignore
+    # _set_autocommit = ignore
 
     SchemaEditorClass = DatabaseSchemaEditor
 
     client_class = DatabaseClient
     creation_class = DatabaseCreation
     features_class = DatabaseFeatures
     introspection_class = DatabaseIntrospection
     ops_class = DatabaseOperations
     validation_class = DatabaseValidation
 
+    _disable_constraint_checking = False
+
     def get_connection_params(self):
         settings_dict = self.settings_dict
 
         conn_params = {
             'username': None,
             'password': None,
+            'timeout': 30,
         }
         if settings_dict['USER']:
             conn_params['username'] = settings_dict['USER']
         if settings_dict['PASSWORD']:
             conn_params['password'] = settings_dict['PASSWORD']
+        if 'TIMEOUT' in settings_dict:
+            conn_params['timeout'] = settings_dict['TIMEOUT']
 
         if 'CONNECTION_STRING' in settings_dict:
             conn_params['connectionstr'] = settings_dict['CONNECTION_STRING']
         else:
             conn_params = {
                 'hostname': 'localhost',
                 'port': 1972,
                 'namespace': 'USER',
                 **conn_params,
             }
             if settings_dict['HOST']:
                 conn_params['hostname'] = settings_dict['HOST']
             if settings_dict['PORT']:
                 conn_params['port'] = settings_dict['PORT']
-            if settings_dict['NAME']:
-                conn_params['namespace'] = settings_dict['NAME']
             if 'NAMESPACE' in settings_dict:
                 conn_params['namespace'] = settings_dict['NAMESPACE']
+            if settings_dict['NAME']:
+                conn_params['namespace'] = settings_dict['NAME']
 
             if (
                 not conn_params['hostname'] or
                 not conn_params['port'] or
                 not conn_params['namespace']
             ):
                 raise ImproperlyConfigured(
@@ -154,31 +155,62 @@
             not conn_params['password']
         ):
             raise ImproperlyConfigured(
                 "settings.DATABASES is improperly configured. "
                 "Please supply the USER and PASSWORD"
             )
 
+        conn_params['application_name'] = 'django'
+        conn_params["autoCommit"] = self.autocommit
         return conn_params
 
     @async_unsafe
     def get_new_connection(self, conn_params):
         return Database.connect(**conn_params)
 
-    def init_connection_state(self):
-        cursor = self.connection.cursor()
-        # cursor.callproc('%SYSTEM_SQL.Util_SetOption', ['SELECTMODE', 1])
-        # cursor.callproc('%SYSTEM.SQL_SetSelectMode', [1])
+    def _close(self):
+        if self.connection is not None:
+            # Automatically rollbacks anyway
+            # self.in_atomic_block = False
+            # self.needs_rollback = False
+            with self.wrap_database_errors:
+                return self.connection.close()
 
     @async_unsafe
     def create_cursor(self, name=None):
         cursor = self.connection.cursor()
         return CursorWrapper(cursor)
 
     def is_usable(self):
         try:
             with self.connection.cursor() as cursor:
                 cursor.execute('SELECT 1')
         except:
             return False
         else:
             return True
+
+    @cached_property
+    def wrap_database_errors(self):
+        """
+        Context manager and decorator that re-throws backend-specific database
+        exceptions using Django's common wrappers.
+        """
+        return DatabaseErrorWrapper(self)
+
+    def _set_autocommit(self, autocommit):
+        with self.wrap_database_errors:
+            self.connection.setAutoCommit(autocommit)
+
+    def disable_constraint_checking(self):
+        self._disable_constraint_checking = True
+        return True
+
+    def enable_constraint_checking(self):
+        self._disable_constraint_checking = False
+
+    @async_unsafe
+    def savepoint_commit(self, sid):
+        """
+        IRIS does not have `RELEASE SAVEPOINT`
+        so, just ignore it
+        """
```

### Comparing `django-iris-0.1.9b1/django_iris/introspection.py` & `django-iris-0.2.0b1/django_iris/introspection.py`

 * *Files 12% similar despite different names*

```diff
@@ -6,14 +6,21 @@
 from django.db.models import Index
 from django.utils.datastructures import OrderedSet
 
 FieldInfo = namedtuple(
     'FieldInfo', BaseFieldInfo._fields + ('auto_increment', ))
 
 
+def schema_name(table_name):
+    table_schema = 'SQLUser'
+    if '.' in table_name:
+        [table_schema, table_name] = table_name.split('.')
+    return [table_schema, table_name, ]
+
+
 class DatabaseIntrospection(BaseDatabaseIntrospection):
     data_types_reverse = {
         'bigint': 'BigIntegerField',
         'varchar': 'CharField',
         'integer': 'IntegerField',
         'bit': 'BooleanField',
         'date': 'DateField',
@@ -44,76 +51,83 @@
         for field_info in self.get_table_description(cursor, table_name):
             if 'auto_increment' in field_info and field_info['auto_increment']:
                 return [{'table': table_name, 'column': field_info.name}]
         return []
 
     def get_table_list(self, cursor):
         cursor.execute("""
-          SELECT TABLE_NAME
+          SELECT TABLE_SCHEMA,TABLE_NAME
           FROM information_schema.tables
-          WHERE TABLE_SCHEMA = 'SQLUser'
+          WHERE TABLE_TYPE = 'BASE TABLE' 
+          AND NOT (TABLE_SCHEMA %%STARTSWITH 'Ens')
         """)
-        return [TableInfo(row[0], 't') for row in cursor.fetchall()]
+        rows = cursor.fetchall() or []
+        return [TableInfo(row[1] if row[0] == 'SQLUser' else row[0] + '.' + row[1], 't') for row in rows]
 
     def get_table_description(self, cursor, table_name):
         """
         Return a description of the table with the DB-API cursor.description
         interface.
         """
+        cursor.execute(
+            "SELECT TOP 1 * FROM %s" % self.connection.ops.quote_name(table_name)
+        )
 
         cursor.execute("""
             SELECT 
                 COLUMN_NAME,
                 DATA_TYPE,
                 CHARACTER_MAXIMUM_LENGTH,
                 NUMERIC_PRECISION,
                 NUMERIC_SCALE,
                 IS_NULLABLE,
-                AUTO_INCREMENT
+                AUTO_INCREMENT,
+                COLUMN_DEFAULT
             FROM INFORMATION_SCHEMA.COLUMNS 
             WHERE TABLE_SCHEMA = %s
             AND TABLE_NAME = %s
+            AND NOT (AUTO_INCREMENT = 'YES' AND PRIMARY_KEY = 'NO')
             ORDER BY ORDINAL_POSITION
         """,
-                       ['SQLUser', table_name]
+                       schema_name(table_name)
                        )
-
+        
         description = [
-            # name type_code display_size internal_size precision scale null_ok default collation
-            # auto_increment
             FieldInfo(
                 name,
-                data_type,
+                'longvarchar'
+                if data_type == 'varchar' and length == '-1' else data_type,
                 None,
                 length,
                 precision,
                 scale,
                 isnull == 'YES',
-                '',
+                column_default,
                 '',
                 auto_increment == 'YES',
             )
-            for name, data_type, length, precision, scale, isnull, auto_increment in cursor.fetchall()
+            for name, data_type, length, precision, scale, isnull, auto_increment, column_default in cursor.fetchall()
         ]
         return description
 
     def get_relations(self, cursor, table_name):
         """
         Return a dictionary of {field_name: (field_name_other_table, other_table)}
         representing all relationships to the given table.
         """
+
         # Dictionary of relations to return
         cursor.execute("""
             SELECT column_name, referenced_column_name, referenced_table_name
             FROM information_schema.key_column_usage
             WHERE table_schema = %s
                 AND table_name = %s
                 AND referenced_table_name IS NOT NULL
                 AND referenced_column_name IS NOT NULL
-        """, ['SQLUser', table_name])
+        """, schema_name(table_name))
         return {
             field_name: (other_field, other_table)
             for field_name, other_field, other_table in cursor.fetchall()
         }
 
     # def get_primary_key_column(self, cursor, table_name):
     #     """
@@ -147,21 +161,21 @@
                 kc.referenced_table_name, kc.referenced_column_name,
                 c.constraint_type
             FROM
                 information_schema.key_column_usage AS kc,
                 information_schema.table_constraints AS c
             WHERE
                 kc.table_schema = %s AND
+                kc.table_name = %s AND
                 c.table_schema = kc.table_schema AND
                 c.constraint_name = kc.constraint_name AND
-                c.constraint_type != 'CHECK' AND
-                kc.table_name = %s
+                c.constraint_type != 'CHECK'
             ORDER BY kc.ordinal_position
         """
-        cursor.execute(name_query, ['SQLUser', table_name])
+        cursor.execute(name_query, schema_name(table_name))
         for constraint, column, ref_table, ref_column, kind in cursor.fetchall():
             if constraint not in constraints:
                 constraints[constraint] = {
                     'columns': OrderedSet(),
                     'primary_key': kind == 'PRIMARY KEY',
                     'unique': kind in {'PRIMARY KEY', 'UNIQUE'},
                     'index': False,
@@ -184,15 +198,15 @@
                 WHERE
                     cc.constraint_schema = %s AND
                     tc.table_schema = cc.constraint_schema AND
                     cc.constraint_name = tc.constraint_name AND
                     tc.constraint_type = 'CHECK' AND
                     tc.table_name = %s
             """
-            cursor.execute(type_query, ['SQLUser', table_name])
+            cursor.execute(type_query, schema_name(table_name))
             for constraint, check_clause in cursor.fetchall():
                 constraint_columns = self._parse_constraint_columns(
                     check_clause, columns)
                 # Ensure uniqueness of unnamed constraints. Unnamed unique
                 # and check columns constraints have the same name as
                 # a column.
                 if set(constraint_columns) == {constraint}:
@@ -215,26 +229,28 @@
                 NON_UNIQUE,
                 ASC_OR_DESC
             FROM INFORMATION_SCHEMA. INDEXES
             WHERE TABLE_SCHEMA = %s
               AND TABLE_NAME = %s
             ORDER BY ORDINAL_POSITION
         """
-        cursor.execute(index_query, ['SQLUser', table_name])
+        cursor.execute(index_query, schema_name(table_name))
         for index, column, primary, non_unique, order in cursor.fetchall():
             if index not in constraints:
                 constraints[index] = {
                     'columns': OrderedSet(),
+                    'index': True,
                     'primary_key': primary == 1,
                     'unique': not non_unique,
                     'check': False,
                     'foreign_key': None,
                     'orders': [],
+                    "type": Index.suffix,
                 }
-                constraints[index]['columns'].add(column)
-                constraints[index]['orders'].append(
-                    'DESC' if order == 'D' else 'ASC')
+            constraints[index]['columns'].add(column)
+            # What's the point of orders, if IRIS don't care about it
+            constraints[index]['orders'].append('DESC' if order == 'D' else 'ASC')
 
         # Convert the sorted sets to lists
         for constraint in constraints.values():
             constraint['columns'] = list(constraint['columns'])
         return constraints
```

### Comparing `django-iris-0.1.9b1/django_iris.egg-info/PKG-INFO` & `django-iris-0.2.0b1/django_iris.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,18 +1,17 @@
 Metadata-Version: 2.1
 Name: django-iris
-Version: 0.1.9b1
+Version: 0.2.0b1
 Summary: Django backend for InterSystems IRIS
 Home-page: https://github.com/caretdev/django-iris
 Maintainer: CaretDev
 Maintainer-email: dmitry@caretdev.com
 License: MIT
 Project-URL: Source, https://github.com/caretdev/django-iris
 Project-URL: Tracker, https://github.com/caretdev/django-iris/issues
-Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Framework :: Django
 Classifier: Framework :: Django :: 4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
@@ -54,9 +53,7 @@
         'USER': '_SYSTEM',
         'PASSWORD': 'SYS',
         'HOST': 'localhost',
         'PORT': '1972',
     },
 }
 ```
-
-
```

### Comparing `django-iris-0.1.9b1/setup.cfg` & `django-iris-0.2.0b1/setup.cfg`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = django-iris
-version = 0.1.9b1
+version = 0.2.0b1
 url = https://github.com/caretdev/django-iris
 maintainer = CaretDev
 maintainer_email = dmitry@caretdev.com
 license = MIT
 description = Django backend for InterSystems IRIS
 long_description = file: README.md
 long_description_content_type = text/markdown
@@ -22,13 +22,15 @@
 project_urls = 
 	Source = https://github.com/caretdev/django-iris
 	Tracker = https://github.com/caretdev/django-iris/issues
 
 [options]
 packages = 
 	django_iris
+	intersystems_iris
+	irisnative
 python_requires = >=3.8
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

### Comparing `django-iris-0.1.9b1/setup.py` & `django-iris-0.2.0b1/setup.py`

 * *Files identical despite different names*

