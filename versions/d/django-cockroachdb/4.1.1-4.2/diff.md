# Comparing `tmp/django-cockroachdb-4.1.1.tar.gz` & `tmp/django-cockroachdb-4.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-cockroachdb-4.1.1.tar", last modified: Tue Dec  6 18:07:35 2022, max compression
+gzip compressed data, was "django-cockroachdb-4.2.tar", last modified: Thu Apr  6 21:11:23 2023, max compression
```

## Comparing `django-cockroachdb-4.1.1.tar` & `django-cockroachdb-4.2.tar`

### file list

```diff
@@ -1,31 +1,33 @@
-drwxrwxr-x   0 tim       (1000) tim       (1000)        0 2022-12-06 18:07:35.637177 django-cockroachdb-4.1.1/
--rw-r--r--   0 tim       (1000) tim       (1000)    11357 2019-11-13 18:21:15.000000 django-cockroachdb-4.1.1/LICENSE
--rw-rw-r--   0 tim       (1000) tim       (1000)     7891 2022-12-06 18:07:35.637177 django-cockroachdb-4.1.1/PKG-INFO
--rw-rw-r--   0 tim       (1000) tim       (1000)     6839 2022-12-06 18:06:44.000000 django-cockroachdb-4.1.1/README.md
-drwxrwxr-x   0 tim       (1000) tim       (1000)        0 2022-12-06 18:07:35.633177 django-cockroachdb-4.1.1/django_cockroachdb/
--rw-rw-r--   0 tim       (1000) tim       (1000)      343 2022-12-06 18:06:44.000000 django-cockroachdb-4.1.1/django_cockroachdb/__init__.py
--rw-rw-r--   0 tim       (1000) tim       (1000)     4696 2022-12-06 18:06:39.000000 django-cockroachdb-4.1.1/django_cockroachdb/base.py
--rw-rw-r--   0 tim       (1000) tim       (1000)     1976 2022-12-06 15:36:55.000000 django-cockroachdb-4.1.1/django_cockroachdb/client.py
--rw-rw-r--   0 tim       (1000) tim       (1000)      397 2021-12-08 22:08:11.000000 django-cockroachdb-4.1.1/django_cockroachdb/creation.py
--rw-rw-r--   0 tim       (1000) tim       (1000)    15409 2022-12-06 18:06:44.000000 django-cockroachdb-4.1.1/django_cockroachdb/features.py
--rw-rw-r--   0 tim       (1000) tim       (1000)     3372 2022-10-11 13:37:01.000000 django-cockroachdb-4.1.1/django_cockroachdb/functions.py
--rw-rw-r--   0 tim       (1000) tim       (1000)      367 2022-10-11 13:37:01.000000 django-cockroachdb-4.1.1/django_cockroachdb/introspection.py
--rw-rw-r--   0 tim       (1000) tim       (1000)      354 2022-12-01 14:28:54.000000 django-cockroachdb-4.1.1/django_cockroachdb/lookups.py
--rw-rw-r--   0 tim       (1000) tim       (1000)     4607 2022-12-06 18:06:39.000000 django-cockroachdb-4.1.1/django_cockroachdb/operations.py
--rw-rw-r--   0 tim       (1000) tim       (1000)     5273 2022-12-06 18:06:39.000000 django-cockroachdb-4.1.1/django_cockroachdb/schema.py
--rw-rw-r--   0 tim       (1000) tim       (1000)      774 2021-10-05 15:32:35.000000 django-cockroachdb-4.1.1/django_cockroachdb/utils.py
-drwxrwxr-x   0 tim       (1000) tim       (1000)        0 2022-12-06 18:07:35.637177 django-cockroachdb-4.1.1/django_cockroachdb.egg-info/
--rw-rw-r--   0 tim       (1000) tim       (1000)     7891 2022-12-06 18:07:35.000000 django-cockroachdb-4.1.1/django_cockroachdb.egg-info/PKG-INFO
--rw-rw-r--   0 tim       (1000) tim       (1000)      788 2022-12-06 18:07:35.000000 django-cockroachdb-4.1.1/django_cockroachdb.egg-info/SOURCES.txt
--rw-rw-r--   0 tim       (1000) tim       (1000)        1 2022-12-06 18:07:35.000000 django-cockroachdb-4.1.1/django_cockroachdb.egg-info/dependency_links.txt
--rw-rw-r--   0 tim       (1000) tim       (1000)       42 2022-12-06 18:07:35.000000 django-cockroachdb-4.1.1/django_cockroachdb.egg-info/top_level.txt
-drwxrwxr-x   0 tim       (1000) tim       (1000)        0 2022-12-06 18:07:35.637177 django-cockroachdb-4.1.1/django_cockroachdb_gis/
--rw-rw-r--   0 tim       (1000) tim       (1000)       64 2021-10-05 15:32:35.000000 django-cockroachdb-4.1.1/django_cockroachdb_gis/__init__.py
--rw-rw-r--   0 tim       (1000) tim       (1000)      470 2022-12-03 14:26:39.000000 django-cockroachdb-4.1.1/django_cockroachdb_gis/base.py
--rw-rw-r--   0 tim       (1000) tim       (1000)     4910 2022-12-06 18:06:39.000000 django-cockroachdb-4.1.1/django_cockroachdb_gis/features.py
--rw-rw-r--   0 tim       (1000) tim       (1000)      264 2021-10-05 15:32:35.000000 django-cockroachdb-4.1.1/django_cockroachdb_gis/functions.py
--rw-rw-r--   0 tim       (1000) tim       (1000)      284 2021-11-16 14:43:26.000000 django-cockroachdb-4.1.1/django_cockroachdb_gis/introspection.py
--rw-rw-r--   0 tim       (1000) tim       (1000)     1490 2022-10-11 13:37:01.000000 django-cockroachdb-4.1.1/django_cockroachdb_gis/operations.py
--rw-rw-r--   0 tim       (1000) tim       (1000)      255 2022-10-11 13:37:01.000000 django-cockroachdb-4.1.1/django_cockroachdb_gis/schema.py
--rw-rw-r--   0 tim       (1000) tim       (1000)     1196 2022-12-06 18:07:35.637177 django-cockroachdb-4.1.1/setup.cfg
--rw-rw-r--   0 tim       (1000) tim       (1000)       38 2021-12-10 22:42:06.000000 django-cockroachdb-4.1.1/setup.py
+drwxrwxr-x   0 tim       (1000) tim       (1000)        0 2023-04-06 21:11:23.252748 django-cockroachdb-4.2/
+-rw-rw-r--   0 tim       (1000) tim       (1000)      102 2023-04-06 21:11:08.000000 django-cockroachdb-4.2/CHANGELOG.md
+-rw-r--r--   0 tim       (1000) tim       (1000)    11357 2019-11-13 18:21:15.000000 django-cockroachdb-4.2/LICENSE
+-rw-rw-r--   0 tim       (1000) tim       (1000)       21 2023-04-06 20:06:17.000000 django-cockroachdb-4.2/MANIFEST.in
+-rw-rw-r--   0 tim       (1000) tim       (1000)     7996 2023-04-06 21:11:23.252748 django-cockroachdb-4.2/PKG-INFO
+-rw-rw-r--   0 tim       (1000) tim       (1000)     6946 2023-04-06 21:11:08.000000 django-cockroachdb-4.2/README.md
+drwxrwxr-x   0 tim       (1000) tim       (1000)        0 2023-04-06 21:11:23.244748 django-cockroachdb-4.2/django_cockroachdb/
+-rw-rw-r--   0 tim       (1000) tim       (1000)      341 2023-04-06 21:11:08.000000 django-cockroachdb-4.2/django_cockroachdb/__init__.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)     4477 2023-04-06 21:11:08.000000 django-cockroachdb-4.2/django_cockroachdb/base.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)     1976 2022-12-06 22:16:12.000000 django-cockroachdb-4.2/django_cockroachdb/client.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)      397 2021-12-08 22:08:11.000000 django-cockroachdb-4.2/django_cockroachdb/creation.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)    18419 2023-04-06 21:11:08.000000 django-cockroachdb-4.2/django_cockroachdb/features.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)     3372 2023-01-30 16:03:09.000000 django-cockroachdb-4.2/django_cockroachdb/functions.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)     1382 2023-04-06 20:01:23.000000 django-cockroachdb-4.2/django_cockroachdb/introspection.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)      354 2022-12-01 14:28:54.000000 django-cockroachdb-4.2/django_cockroachdb/lookups.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)     3944 2023-04-06 21:11:08.000000 django-cockroachdb-4.2/django_cockroachdb/operations.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)     5749 2023-04-06 21:11:08.000000 django-cockroachdb-4.2/django_cockroachdb/schema.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)      774 2021-10-05 15:32:35.000000 django-cockroachdb-4.2/django_cockroachdb/utils.py
+drwxrwxr-x   0 tim       (1000) tim       (1000)        0 2023-04-06 21:11:23.248748 django-cockroachdb-4.2/django_cockroachdb.egg-info/
+-rw-rw-r--   0 tim       (1000) tim       (1000)     7996 2023-04-06 21:11:23.000000 django-cockroachdb-4.2/django_cockroachdb.egg-info/PKG-INFO
+-rw-rw-r--   0 tim       (1000) tim       (1000)      813 2023-04-06 21:11:23.000000 django-cockroachdb-4.2/django_cockroachdb.egg-info/SOURCES.txt
+-rw-rw-r--   0 tim       (1000) tim       (1000)        1 2023-04-06 21:11:23.000000 django-cockroachdb-4.2/django_cockroachdb.egg-info/dependency_links.txt
+-rw-rw-r--   0 tim       (1000) tim       (1000)       42 2023-04-06 21:11:23.000000 django-cockroachdb-4.2/django_cockroachdb.egg-info/top_level.txt
+drwxrwxr-x   0 tim       (1000) tim       (1000)        0 2023-04-06 21:11:23.252748 django-cockroachdb-4.2/django_cockroachdb_gis/
+-rw-rw-r--   0 tim       (1000) tim       (1000)       64 2021-10-05 15:32:35.000000 django-cockroachdb-4.2/django_cockroachdb_gis/__init__.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)      828 2023-04-06 21:11:08.000000 django-cockroachdb-4.2/django_cockroachdb_gis/base.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)     5248 2023-04-06 21:11:08.000000 django-cockroachdb-4.2/django_cockroachdb_gis/features.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)      264 2021-10-05 15:32:35.000000 django-cockroachdb-4.2/django_cockroachdb_gis/functions.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)      284 2021-11-16 14:43:26.000000 django-cockroachdb-4.2/django_cockroachdb_gis/introspection.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)     1490 2023-01-30 16:03:09.000000 django-cockroachdb-4.2/django_cockroachdb_gis/operations.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)      255 2023-01-30 16:03:09.000000 django-cockroachdb-4.2/django_cockroachdb_gis/schema.py
+-rw-rw-r--   0 tim       (1000) tim       (1000)     1196 2023-04-06 21:11:23.256748 django-cockroachdb-4.2/setup.cfg
+-rw-rw-r--   0 tim       (1000) tim       (1000)       38 2021-12-10 22:42:06.000000 django-cockroachdb-4.2/setup.py
```

### Comparing `django-cockroachdb-4.1.1/LICENSE` & `django-cockroachdb-4.2/LICENSE`

 * *Files identical despite different names*

### Comparing `django-cockroachdb-4.1.1/PKG-INFO` & `django-cockroachdb-4.2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 Metadata-Version: 2.1
 Name: django-cockroachdb
-Version: 4.1.1
+Version: 4.2
 Summary: Django backend for CockroachDB
 Home-page: https://github.com/cockroachdb/django-cockroachdb
 Maintainer: Cockroach Labs
 Maintainer-email: python@cockroachlabs.com
 License: Apache Software License
 Project-URL: Source, https://github.com/cockroachdb/django-cockroachdb
 Project-URL: Tracker, https://github.com/cockroachdb/django-cockroachdb/issues
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Framework :: Django
-Classifier: Framework :: Django :: 4.1
+Classifier: Framework :: Django :: 4.2
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -24,31 +24,36 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # CockroachDB backend for Django
 
 ## Prerequisites
 
-You must install either:
+You must install:
+
+* [psycopg](https://pypi.org/project/psycopg/), which may have some
+ prerequisites [depending on which version you use](https://www.psycopg.org/psycopg3/docs/basic/install.html).
+
+You can also use either:
 
 * [psycopg2](https://pypi.org/project/psycopg2/), which has some
   [prerequisites](https://www.psycopg.org/docs/install.html#prerequisites) of
   its own.
 
 * [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
 
 The binary package is a practical choice for development and testing but in
 production it is advised to use the package built from sources.
 
 ## Install and usage
 
 Use the version of django-cockroachdb that corresponds to your version of
-Django. For example, to get the latest compatible release for Django 4.1.x:
+Django. For example, to get the latest compatible release for Django 4.2.x:
 
-`pip install django-cockroachdb==4.1.*`
+`pip install django-cockroachdb==4.2.*`
 
 The minor release number of Django doesn't correspond to the minor release
 number of django-cockroachdb. Use the latest minor release of each.
 
 Configure the Django `DATABASES` setting similar to this:
 
 ```python
@@ -126,14 +131,17 @@
    - CockroachDB executes `ALTER COLUMN` queries asynchronously which is at
      odds with Django's assumption that the database is altered before the next
      migration operation begins. CockroachDB will give an error like
      `unimplemented: table <...> is currently undergoing a schema change` if a
      later operation tries to modify the table before the asynchronous query
      finishes. A future version of CockroachDB [may fix this](https://github.com/cockroachdb/cockroach/issues/47137).
 
+- The `Field.db_comment` and `Meta.db_table_comment` options aren't supported
+  due to [poor performance](https://github.com/cockroachdb/cockroach/issues/95068).
+
 - Unsupported queries:
    - [Mixed type addition in SELECT](https://github.com/cockroachdb/django-cockroachdb/issues/19):
      `unsupported binary operator: <int> + <float>`
    - [Division that yields a different type](https://github.com/cockroachdb/django-cockroachdb/issues/21):
      `unsupported binary operator: <int> / <int> (desired <int>)`
    - [The power() database function doesn't accept negative exponents](https://github.com/cockroachdb/django-cockroachdb/issues/22):
      `power(): integer out of range`
@@ -163,13 +171,8 @@
        overlaps_below (&>|)](https://github.com/cockroachdb/cockroach/issues/57098)
      - [strictly_above (|>>), strictly_below (<<|)](https://github.com/cockroachdb/cockroach/issues/57095)
 
 ## Known issues and limitations in CockroachDB 22.1.x and earlier
 
 - `QuerySet.select_for_update(skip_locked=True)` isn't supported.
 
-## Known issues and limitations in CockroachDB 21.2.x and earlier
-
-- Unsupported query: [UPDATE float column with integer column](https://github.com/cockroachdb/django-cockroachdb/issues/20):
-  `value type int doesn't match type FLOAT8 of column <name>`
-
```

### Comparing `django-cockroachdb-4.1.1/README.md` & `django-cockroachdb-4.2/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -1,28 +1,33 @@
 # CockroachDB backend for Django
 
 ## Prerequisites
 
-You must install either:
+You must install:
+
+* [psycopg](https://pypi.org/project/psycopg/), which may have some
+ prerequisites [depending on which version you use](https://www.psycopg.org/psycopg3/docs/basic/install.html).
+
+You can also use either:
 
 * [psycopg2](https://pypi.org/project/psycopg2/), which has some
   [prerequisites](https://www.psycopg.org/docs/install.html#prerequisites) of
   its own.
 
 * [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
 
 The binary package is a practical choice for development and testing but in
 production it is advised to use the package built from sources.
 
 ## Install and usage
 
 Use the version of django-cockroachdb that corresponds to your version of
-Django. For example, to get the latest compatible release for Django 4.1.x:
+Django. For example, to get the latest compatible release for Django 4.2.x:
 
-`pip install django-cockroachdb==4.1.*`
+`pip install django-cockroachdb==4.2.*`
 
 The minor release number of Django doesn't correspond to the minor release
 number of django-cockroachdb. Use the latest minor release of each.
 
 Configure the Django `DATABASES` setting similar to this:
 
 ```python
@@ -100,14 +105,17 @@
    - CockroachDB executes `ALTER COLUMN` queries asynchronously which is at
      odds with Django's assumption that the database is altered before the next
      migration operation begins. CockroachDB will give an error like
      `unimplemented: table <...> is currently undergoing a schema change` if a
      later operation tries to modify the table before the asynchronous query
      finishes. A future version of CockroachDB [may fix this](https://github.com/cockroachdb/cockroach/issues/47137).
 
+- The `Field.db_comment` and `Meta.db_table_comment` options aren't supported
+  due to [poor performance](https://github.com/cockroachdb/cockroach/issues/95068).
+
 - Unsupported queries:
    - [Mixed type addition in SELECT](https://github.com/cockroachdb/django-cockroachdb/issues/19):
      `unsupported binary operator: <int> + <float>`
    - [Division that yields a different type](https://github.com/cockroachdb/django-cockroachdb/issues/21):
      `unsupported binary operator: <int> / <int> (desired <int>)`
    - [The power() database function doesn't accept negative exponents](https://github.com/cockroachdb/django-cockroachdb/issues/22):
      `power(): integer out of range`
@@ -136,12 +144,7 @@
      - [overlaps_left (&<), overlaps_right (&>), overlaps_above (&<|),
        overlaps_below (&>|)](https://github.com/cockroachdb/cockroach/issues/57098)
      - [strictly_above (|>>), strictly_below (<<|)](https://github.com/cockroachdb/cockroach/issues/57095)
 
 ## Known issues and limitations in CockroachDB 22.1.x and earlier
 
 - `QuerySet.select_for_update(skip_locked=True)` isn't supported.
-
-## Known issues and limitations in CockroachDB 21.2.x and earlier
-
-- Unsupported query: [UPDATE float column with integer column](https://github.com/cockroachdb/django-cockroachdb/issues/20):
-  `value type int doesn't match type FLOAT8 of column <name>`
```

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb/base.py` & `django-cockroachdb-4.2/django_cockroachdb/base.py`

 * *Files 3% similar despite different names*

```diff
@@ -3,22 +3,20 @@
 from contextlib import contextmanager
 
 from django.conf import settings
 from django.core.exceptions import ImproperlyConfigured
 from django.utils.functional import cached_property
 
 try:
-    import psycopg2  # noqa
-    import psycopg2.extensions  # noqa
-    import psycopg2.extras  # noqa
-except ImportError as err:
-    raise ImproperlyConfigured(
-        'Error loading psycopg2 module.\n'
-        'Did you install psycopg2 or psycopg2-binary?'
-    ) from err
+    try:
+        import psycopg  # noqa
+    except ImportError:
+        import psycopg2  # noqa
+except ImportError:
+    raise ImproperlyConfigured("Error loading psycopg or psycopg2 module")
 
 from django.db.backends.postgresql.base import (
     DatabaseWrapper as PostgresDatabaseWrapper,
 )
 
 from . import __version__ as django_cockroachdb_version
 from .client import DatabaseClient
@@ -87,18 +85,14 @@
         # (https://github.com/cockroachdb/cockroach/issues/19444) so this
         # method is a no-op.
         pass
 
     def chunked_cursor(self):
         return self.cursor()
 
-    def _set_autocommit(self, autocommit):
-        with self.wrap_database_errors:
-            self.connection.autocommit = autocommit
-
     @contextmanager
     def _nodb_cursor(self):
         # Overidden to avoid inapplicable "Django was unable to create a
         # connection to the 'postgres' database and will use the first
         # PostgreSQL database instead." warning.
         with super(PostgresDatabaseWrapper, self)._nodb_cursor() as cursor:
             yield cursor
```

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb/client.py` & `django-cockroachdb-4.2/django_cockroachdb/client.py`

 * *Files identical despite different names*

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb/features.py` & `django-cockroachdb-4.2/django_cockroachdb/features.py`

 * *Files 14% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 from django.db.backends.postgresql.features import (
     DatabaseFeatures as PostgresDatabaseFeatures,
 )
 from django.utils.functional import cached_property
 
 
 class DatabaseFeatures(PostgresDatabaseFeatures):
-    minimum_database_version = (21, 2)
+    minimum_database_version = (22, 1)
 
     # Cloning databases doesn't speed up tests.
     # https://github.com/cockroachdb/django-cockroachdb/issues/206
     can_clone_databases = False
 
     # Not supported: https://github.com/cockroachdb/cockroach/issues/40476
     has_select_for_update_skip_locked = property(operator.attrgetter('is_cockroachdb_22_2'))
@@ -45,27 +45,29 @@
     # Not supported: https://github.com/cockroachdb/cockroach/issues/41645
     supports_regex_backreferencing = False
 
     # CockroachDB sorts NULL values first with ASC and last with DESC.
     # PostgreSQL behaves the opposite.
     nulls_order_largest = False
 
+    # pg_catalog.obj_description is very slow:
+    # https://github.com/cockroachdb/cockroach/issues/95068
+    supports_comments = False
+
     @cached_property
     def introspected_field_types(self):
         return {
             **super().introspected_field_types,
             'AutoField': 'BigIntegerField',
             'BigAutoField': 'BigIntegerField',
             'IntegerField': 'BigIntegerField',
             'PositiveIntegerField': 'BigIntegerField',
             'SmallAutoField': 'SmallIntegerField',
         }
 
-    supports_order_by_nulls_modifier = property(operator.attrgetter('is_cockroachdb_22_1'))
-
     # CockroachDB doesn't create indexes on foreign keys.
     indexes_foreign_keys = False
 
     # Not supported: https://github.com/cockroachdb/cockroach/issues/59567
     supports_non_deterministic_collations = False
 
     test_collations = {
@@ -73,18 +75,14 @@
         # CockroachDB doesn't introspect that properly:
         # https://github.com/cockroachdb/cockroach/issues/54817
         'non_default': 'sv',
         'swedish_ci': 'sv-x-icu',
     }
 
     @cached_property
-    def is_cockroachdb_22_1(self):
-        return self.connection.cockroachdb_version >= (22, 1)
-
-    @cached_property
     def is_cockroachdb_22_2(self):
         return self.connection.cockroachdb_version >= (22, 2)
 
     @cached_property
     def django_test_expected_failures(self):
         expected_failures = super().django_test_expected_failures
         expected_failures.update({
@@ -115,18 +113,14 @@
             'serializers.test_data.SerializerDataTests.test_json_serializer',
             'serializers.test_data.SerializerDataTests.test_jsonl_serializer',
             'serializers.test_data.SerializerDataTests.test_python_serializer',
             'serializers.test_data.SerializerDataTests.test_xml_serializer',
             'serializers.test_data.SerializerDataTests.test_yaml_serializer',
             # No sequence for AutoField in CockroachDB.
             'introspection.tests.IntrospectionTests.test_sequence_list',
-            # Unsupported query: unsupported binary operator: <int> / <int>:
-            # https://github.com/cockroachdb/django-cockroachdb/issues/21
-            'expressions.tests.ExpressionOperatorTests.test_lefthand_division',
-            'expressions.tests.ExpressionOperatorTests.test_right_hand_division',
             # CockroachDB doesn't support disabling constraints:
             # https://github.com/cockroachdb/cockroach/issues/19444
             'auth_tests.test_views.UUIDUserTests.test_admin_password_change',
             'backends.tests.FkConstraintsTests.test_check_constraints',
             'backends.tests.FkConstraintsTests.test_check_constraints_sql_keywords',
             'backends.tests.FkConstraintsTests.test_disable_constraint_checks_context_manager',
             'backends.tests.FkConstraintsTests.test_disable_constraint_checks_manually',
@@ -135,14 +129,15 @@
             # keys.
             'model_options.test_tablespaces.TablespacesTests.test_tablespace_for_many_to_many_field',
             # ALTER COLUMN TYPE requiring rewrite of on-disk data is currently
             # not supported for columns that are part of an index.
             # https://go.crdb.dev/issue/47636
             'migrations.test_executor.ExecutorTests.test_alter_id_type_with_fk',
             'migrations.test_operations.OperationTests.test_alter_field_pk_fk',
+            'migrations.test_operations.OperationTests.test_alter_field_pk_fk_char_to_int',
             'migrations.test_operations.OperationTests.test_alter_field_pk_fk_db_collation',
             'migrations.test_operations.OperationTests.test_alter_field_reloads_state_on_fk_target_changes',
             'migrations.test_operations.OperationTests.test_alter_field_reloads_state_fk_with_to_field_related_name_target_type_change',  # noqa
             'migrations.test_operations.OperationTests.test_alter_field_reloads_state_on_fk_with_to_field_target_changes',  # noqa
             'migrations.test_operations.OperationTests.test_alter_field_reloads_state_on_fk_with_to_field_target_type_change',  # noqa
             'migrations.test_operations.OperationTests.test_rename_field_reloads_state_on_fk_target_changes',
             'schema.tests.SchemaTests.test_alter_auto_field_to_char_field',
@@ -193,26 +188,70 @@
             # https://github.com/cockroachdb/cockroach/issues/73587
             'aggregation.tests.AggregateTestCase.test_aggregation_default_expression',
             # DataError: incompatible COALESCE expressions: expected pi() to be
             # of type decimal, found type float
             # https://github.com/cockroachdb/cockroach/issues/73587#issuecomment-988408190
             'aggregation.tests.AggregateTestCase.test_aggregation_default_using_decimal_from_database',
         })
-        if not self.connection.features.is_cockroachdb_22_1:
+        if self.uses_server_side_binding:
             expected_failures.update({
-                # ProgrammingError: value type float doesn't match type decimal of
-                # column "n2":
-                # INSERT INTO "db_functions_decimalmodel" ("n1", "n2") VALUES ( -5.75, PI())
-                'db_functions.math.test_round.RoundTests.test_decimal_with_precision',
-                # Passing a naive datetime to cursor.execute() doesn't work in
-                # older versions of CockroachDB.
-                'timezones.tests.LegacyDatabaseTests.test_cursor_execute_accepts_naive_datetime',
-                # unknown signature: date_trunc(string, interval):
-                # https://github.com/cockroachdb/cockroach/issues/76960
-                'db_functions.datetime.test_extract_trunc.DateFunctionTests.test_extract_second_func_no_fractional',
+                # could not determine data type of placeholder:
+                # https://github.com/cockroachdb/cockroach/issues/91396
+                'backends.tests.EscapingChecks.test_parameter_escaping',
+                'backends.tests.EscapingChecksDebug.test_parameter_escaping',
+                'expressions.tests.BasicExpressionsTests.test_annotate_values_filter',
+                'expressions_case.tests.CaseDocumentationExamples.test_lookup_example',
+                'expressions_case.tests.CaseDocumentationExamples.test_simple_example',
+                'expressions_case.tests.CaseExpressionTests.test_aggregation_empty_cases',
+                'expressions_case.tests.CaseExpressionTests.test_annotate',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_exclude',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_values_not_in_order_by',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_with_aggregation_in_condition',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_with_aggregation_in_predicate',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_with_annotation_in_condition',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_with_annotation_in_predicate',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_with_empty_when',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_with_expression_as_condition',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_with_full_when',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_with_join_in_condition',
+                'expressions_case.tests.CaseExpressionTests.test_annotate_with_join_in_predicate',
+                'expressions_case.tests.CaseExpressionTests.test_case_reuse',
+                'expressions_case.tests.CaseExpressionTests.test_combined_q_object',
+                'expressions_case.tests.CaseExpressionTests.test_lookup_different_fields',
+                'expressions_case.tests.CaseExpressionTests.test_lookup_in_condition',
+                'expressions_case.tests.CaseExpressionTests.test_update_generic_ip_address',
+                'lookup.tests.LookupQueryingTests.test_conditional_expression',
+                'ordering.tests.OrderingTests.test_order_by_constant_value',
+                'queries.test_bulk_update.BulkUpdateNoteTests.test_batch_size',
+                'queries.test_bulk_update.BulkUpdateNoteTests.test_multiple_fields',
+                'queries.test_bulk_update.BulkUpdateNoteTests.test_simple',
+                'queries.test_bulk_update.BulkUpdateTests.test_custom_pk',
+                'queries.test_bulk_update.BulkUpdateTests.test_database_routing',
+                'queries.test_bulk_update.BulkUpdateTests.test_database_routing_batch_atomicity',
+                'queries.test_bulk_update.BulkUpdateTests.test_falsey_pk_value',
+                'queries.test_bulk_update.BulkUpdateTests.test_inherited_fields',
+                'queries.test_bulk_update.BulkUpdateTests.test_large_batch',
+                'queries.test_bulk_update.BulkUpdateTests.test_updated_rows_when_passing_duplicates',
+                'queries.test_q.QCheckTests.test_expression',
+                # unsupported binary operator: <interval> / <decimal>
+                'expressions.tests.FTimeDeltaTests.test_durationfield_multiply_divide',
+                # InvalidParameterValue: unsupported binary operator: <int4> / <float>
+                'queries.tests.Ticket23605Tests.test_ticket_23605',
+                # InvalidParameterValue: unsupported binary operator: <int2> + <float>
+                'annotations.tests.NonAggregateAnnotationTestCase.test_combined_annotation_commutative',
+                # incompatible COALESCE expressions: unsupported binary
+                # operator: <decimal> / <float>  (desired <decimal>)
+                'aggregation.tests.AggregateTestCase.test_aggregation_default_passed_another_aggregate',
+            })
+        else:
+            expected_failures.update({
+                # Unsupported query: unsupported binary operator: <int> / <int>:
+                # https://github.com/cockroachdb/django-cockroachdb/issues/21
+                'expressions.tests.ExpressionOperatorTests.test_lefthand_division',
+                'expressions.tests.ExpressionOperatorTests.test_right_hand_division',
             })
         return expected_failures
 
     @cached_property
     def django_test_skips(self):
         skips = super().django_test_skips
         skips.update({
@@ -234,26 +273,19 @@
             'Skip to prevents some error output in the logs.': {
                 # Since QuerySet.select_for_update() was enabled, this test is
                 # already skipped by the 'Database took too long to lock the row'
                 # logic in the test. Skipping it entirely prevents some error
                 # output in the logs:
                 # Exception in thread Thread-1:
                 # ...
-                # psycopg2.errors.SerializationFailure: restart transaction:
+                # psycopg.errors.SerializationFailure: restart transaction:
                 # TransactionRetryWithProtoRefreshError: WriteTooOldError: write
                 # at timestamp 1598314405.858850941,0 too old; wrote at
                 # 1598314405.883337663,1
                 'get_or_create.tests.UpdateOrCreateTransactionTests.test_creation_in_transaction',
                 # Sometimes fails as above or with
                 # AssertionError: datetime.timedelta(microseconds=28529) not
                 # greater than datetime.timedelta(microseconds=500000)
                 'get_or_create.tests.UpdateOrCreateTransactionTests.test_updates_in_transaction',
             },
         })
-        if not self.connection.features.is_cockroachdb_22_1:
-            skips.update({
-                # https://github.com/cockroachdb/django-cockroachdb/issues/20
-                'Unsupported query: UPDATE float column with integer column.': {
-                    'expressions.tests.ExpressionsNumericTests',
-                },
-            })
         return skips
```

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb/functions.py` & `django-cockroachdb-4.2/django_cockroachdb/functions.py`

 * *Files identical despite different names*

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb/schema.py` & `django-cockroachdb-4.2/django_cockroachdb/schema.py`

 * *Files 10% similar despite different names*

```diff
@@ -20,14 +20,23 @@
     # creating this foreign key. This isn't supported by CockroachDB.
     sql_create_column_inline_fk = 'CONSTRAINT %(name)s REFERENCES %(to_table)s(%(to_column)s)%(deferrable)s'
 
     # The PostgreSQL backend uses "SET CONSTRAINTS ... IMMEDIATE" after this
     # statement. This isn't supported by CockroachDB.
     sql_update_with_default = "UPDATE %(table)s SET %(column)s = %(default)s WHERE %(column)s IS NULL"
 
+    def __enter__(self):
+        super().__enter__()
+        # As long as DatabaseFeatures.can_rollback_ddl = False, compose() may
+        # fail if connection is None as per
+        # https://github.com/django/django/pull/15687#discussion_r1038175823.
+        # See also https://github.com/django/django/pull/15687#discussion_r1041503991.
+        self.connection.ensure_connection()
+        return self
+
     def add_index(self, model, index, concurrently=False):
         if index.contains_expressions and not self.connection.features.supports_expression_indexes:
             return None
         super().add_index(model, index, concurrently)
 
     def remove_index(self, model, index, concurrently=False):
         if index.contains_expressions and not self.connection.features.supports_expression_indexes:
@@ -71,36 +80,39 @@
                 self.execute(self.sql_alter_column % {
                     'table': self.quote_name(model._meta.db_table),
                     'changes': 'ALTER COLUMN %(column)s DROP DEFAULT' % {
                         'column': self.quote_name(new_field.column),
                     }
                 })
 
-    def _alter_column_type_sql(self, model, old_field, new_field, new_type):
-        self.sql_alter_column_type = 'ALTER COLUMN %(column)s TYPE %(type)s'
+    def _alter_column_type_sql(self, model, old_field, new_field, new_type, old_collation, new_collation):
         new_internal_type = new_field.get_internal_type()
         old_internal_type = old_field.get_internal_type()
         # Make ALTER TYPE with AutoField make sense.
         auto_field_types = {'AutoField', 'BigAutoField', 'SmallAutoField'}
         old_is_auto = old_internal_type in auto_field_types
         new_is_auto = new_internal_type in auto_field_types
         if new_is_auto and not old_is_auto:
             column = strip_quotes(new_field.column)
             return (
                 (
                     self.sql_alter_column_type % {
                         "column": self.quote_name(column),
                         "type": new_type,
+                        "collation": "",
                     },
                     [],
                 ),
                 # The PostgreSQL backend manages the column's identity here but
                 # this isn't applicable on CockroachDB because unique_rowid()
                 # is used instead.
                 [],
             )
         else:
-            return BaseDatabaseSchemaEditor._alter_column_type_sql(self, model, old_field, new_field, new_type)
+            return BaseDatabaseSchemaEditor._alter_column_type_sql(
+                self, model, old_field, new_field, new_type,
+                old_collation, new_collation,
+            )
 
     def _field_should_be_indexed(self, model, field):
         # Foreign keys are automatically indexed by cockroachdb.
         return not isinstance(field, ForeignKey) and super()._field_should_be_indexed(model, field)
```

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb/utils.py` & `django-cockroachdb-4.2/django_cockroachdb/utils.py`

 * *Files identical despite different names*

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb.egg-info/PKG-INFO` & `django-cockroachdb-4.2/django_cockroachdb.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 Metadata-Version: 2.1
 Name: django-cockroachdb
-Version: 4.1.1
+Version: 4.2
 Summary: Django backend for CockroachDB
 Home-page: https://github.com/cockroachdb/django-cockroachdb
 Maintainer: Cockroach Labs
 Maintainer-email: python@cockroachlabs.com
 License: Apache Software License
 Project-URL: Source, https://github.com/cockroachdb/django-cockroachdb
 Project-URL: Tracker, https://github.com/cockroachdb/django-cockroachdb/issues
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Framework :: Django
-Classifier: Framework :: Django :: 4.1
+Classifier: Framework :: Django :: 4.2
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
@@ -24,31 +24,36 @@
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # CockroachDB backend for Django
 
 ## Prerequisites
 
-You must install either:
+You must install:
+
+* [psycopg](https://pypi.org/project/psycopg/), which may have some
+ prerequisites [depending on which version you use](https://www.psycopg.org/psycopg3/docs/basic/install.html).
+
+You can also use either:
 
 * [psycopg2](https://pypi.org/project/psycopg2/), which has some
   [prerequisites](https://www.psycopg.org/docs/install.html#prerequisites) of
   its own.
 
 * [psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
 
 The binary package is a practical choice for development and testing but in
 production it is advised to use the package built from sources.
 
 ## Install and usage
 
 Use the version of django-cockroachdb that corresponds to your version of
-Django. For example, to get the latest compatible release for Django 4.1.x:
+Django. For example, to get the latest compatible release for Django 4.2.x:
 
-`pip install django-cockroachdb==4.1.*`
+`pip install django-cockroachdb==4.2.*`
 
 The minor release number of Django doesn't correspond to the minor release
 number of django-cockroachdb. Use the latest minor release of each.
 
 Configure the Django `DATABASES` setting similar to this:
 
 ```python
@@ -126,14 +131,17 @@
    - CockroachDB executes `ALTER COLUMN` queries asynchronously which is at
      odds with Django's assumption that the database is altered before the next
      migration operation begins. CockroachDB will give an error like
      `unimplemented: table <...> is currently undergoing a schema change` if a
      later operation tries to modify the table before the asynchronous query
      finishes. A future version of CockroachDB [may fix this](https://github.com/cockroachdb/cockroach/issues/47137).
 
+- The `Field.db_comment` and `Meta.db_table_comment` options aren't supported
+  due to [poor performance](https://github.com/cockroachdb/cockroach/issues/95068).
+
 - Unsupported queries:
    - [Mixed type addition in SELECT](https://github.com/cockroachdb/django-cockroachdb/issues/19):
      `unsupported binary operator: <int> + <float>`
    - [Division that yields a different type](https://github.com/cockroachdb/django-cockroachdb/issues/21):
      `unsupported binary operator: <int> / <int> (desired <int>)`
    - [The power() database function doesn't accept negative exponents](https://github.com/cockroachdb/django-cockroachdb/issues/22):
      `power(): integer out of range`
@@ -163,13 +171,8 @@
        overlaps_below (&>|)](https://github.com/cockroachdb/cockroach/issues/57098)
      - [strictly_above (|>>), strictly_below (<<|)](https://github.com/cockroachdb/cockroach/issues/57095)
 
 ## Known issues and limitations in CockroachDB 22.1.x and earlier
 
 - `QuerySet.select_for_update(skip_locked=True)` isn't supported.
 
-## Known issues and limitations in CockroachDB 21.2.x and earlier
-
-- Unsupported query: [UPDATE float column with integer column](https://github.com/cockroachdb/django-cockroachdb/issues/20):
-  `value type int doesn't match type FLOAT8 of column <name>`
-
```

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb.egg-info/SOURCES.txt` & `django-cockroachdb-4.2/django_cockroachdb.egg-info/SOURCES.txt`

 * *Files 7% similar despite different names*

```diff
@@ -1,8 +1,10 @@
+CHANGELOG.md
 LICENSE
+MANIFEST.in
 README.md
 setup.cfg
 setup.py
 django_cockroachdb/__init__.py
 django_cockroachdb/base.py
 django_cockroachdb/client.py
 django_cockroachdb/creation.py
```

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb_gis/features.py` & `django-cockroachdb-4.2/django_cockroachdb_gis/features.py`

 * *Files 2% similar despite different names*

```diff
@@ -33,28 +33,25 @@
             'gis_tests.geoapp.test_functions.GISFunctionsTests.test_diff_intersection_union',
             'gis_tests.geoapp.test_functions.GISFunctionsTests.test_union_mixed_srid',
             'gis_tests.geoapp.test_functions.GISFunctionsTests.test_union',
             'gis_tests.geoapp.tests.GeoLookupTest.test_gis_lookups_with_complex_expressions',
             'gis_tests.geoapp.tests.GeoLookupTest.test_relate_lookup',
             # NotSupportedError: this box2d comparison operator is experimental
             'gis_tests.geoapp.tests.GeoLookupTest.test_contains_contained_lookups',
-            # unknown signature: st_dwithin(geography, geometry, decimal) (desired <bool>)
-            # https://github.com/cockroachdb/cockroach/issues/53720
-            'gis_tests.geogapp.tests.GeographyTest.test02_distance_lookup',
             # unknown signature: st_distancespheroid(geometry, geometry, string)
             # https://github.com/cockroachdb/cockroach/issues/48922#issuecomment-693096502
             'gis_tests.distapp.tests.DistanceTest.test_distance_lookups_with_expression_rhs',
             'gis_tests.distapp.tests.DistanceTest.test_geodetic_distance_lookups',
             'gis_tests.distapp.tests.DistanceFunctionsTests.test_distance_geodetic_spheroid',
             # st_lengthspheroid(): unimplemented:
             # https://github.com/cockroachdb/cockroach/issues/48968
             'gis_tests.distapp.tests.DistanceFunctionsTests.test_length',
             # Unsupported ~= (https://github.com/cockroachdb/cockroach/issues/57096)
             # and @ operators (https://github.com/cockroachdb/cockroach/issues/56124).
-            'gis_tests.geogapp.tests.GeographyTest.test04_invalid_operators_functions',
+            'gis_tests.geogapp.tests.GeographyTest.test_operators_functions_unavailable_for_geography',
             # unknown function: st_3dperimeter
             # https://github.com/cockroachdb/cockroach/issues/60871
             'gis_tests.geo3d.tests.Geo3DFunctionsTests.test_perimeter',
             # unknown function: st_3dextent()
             # https://github.com/cockroachdb/cockroach/issues/60864
             'gis_tests.geo3d.tests.Geo3DTest.test_extent',
             # unknown signature: st_scale(geometry, decimal, decimal, decimal)
@@ -70,8 +67,19 @@
             # data is currently not supported for columns that are part of an
             # index: https://github.com/cockroachdb/cockroach/issues/47636
             'gis_tests.gis_migrations.test_operations.OperationTests.test_alter_geom_field_dim',
             # 3D opclass not present on CockroachDB:
             # https://github.com/cockroachdb/cockroach/issues/47420#issuecomment-969578772
             'gis_tests.gis_migrations.test_operations.OperationTests.test_add_3d_field_opclass',
         })
+        if self.uses_server_side_binding:
+            expected_failures.update({
+                # unknown signature: st_scale(geometry, int, int)
+                'gis_tests.geoapp.test_functions.GISFunctionsTests.test_scale',
+            })
+        else:
+            expected_failures.update({
+                # unknown signature: st_dwithin(geography, geometry, decimal) (desired <bool>)
+                # https://github.com/cockroachdb/cockroach/issues/53720
+                'gis_tests.geogapp.tests.GeographyTest.test02_distance_lookup',
+            })
         return expected_failures
```

### Comparing `django-cockroachdb-4.1.1/django_cockroachdb_gis/operations.py` & `django-cockroachdb-4.2/django_cockroachdb_gis/operations.py`

 * *Files identical despite different names*

### Comparing `django-cockroachdb-4.1.1/setup.cfg` & `django-cockroachdb-4.2/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 license = Apache Software License
 description = Django backend for CockroachDB
 long_description = file: README.md
 long_description_content_type = text/markdown
 classifiers = 
 	Development Status :: 5 - Production/Stable
 	Framework :: Django
-	Framework :: Django :: 4.1
+	Framework :: Django :: 4.2
 	License :: OSI Approved :: Apache Software License
 	Operating System :: OS Independent
 	Programming Language :: Python
 	Programming Language :: Python :: 3
 	Programming Language :: Python :: 3.8
 	Programming Language :: Python :: 3.9
 	Programming Language :: Python :: 3.10
```

