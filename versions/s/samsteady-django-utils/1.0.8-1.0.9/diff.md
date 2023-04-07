# Comparing `tmp/samsteady-django-utils-1.0.8.tar.gz` & `tmp/samsteady-django-utils-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/samsteady-django-utils-1.0.8.tar", last modified: Sat Jul 17 00:17:07 2021, max compression
+gzip compressed data, was "dist/samsteady-django-utils-1.0.9.tar", last modified: Sat Jul 17 22:03:42 2021, max compression
```

## Comparing `samsteady-django-utils-1.0.8.tar` & `samsteady-django-utils-1.0.9.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 Sam        (501) staff       (20)        0 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/
--rw-r--r--   0 Sam        (501) staff       (20)      807 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/PKG-INFO
--rw-r--r--   0 Sam        (501) staff       (20)       16 2020-10-04 03:25:31.000000 samsteady-django-utils-1.0.8/README.md
-drwxr-xr-x   0 Sam        (501) staff       (20)        0 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/django_utils/
--rw-r--r--   0 Sam        (501) staff       (20)        0 2020-10-04 03:17:55.000000 samsteady-django-utils-1.0.8/django_utils/__init__.py
--rw-r--r--   0 Sam        (501) staff       (20)      220 2020-10-12 21:12:57.000000 samsteady-django-utils-1.0.8/django_utils/consumers.py
--rw-r--r--   0 Sam        (501) staff       (20)      466 2020-10-04 03:17:00.000000 samsteady-django-utils-1.0.8/django_utils/exceptions.py
--rw-r--r--   0 Sam        (501) staff       (20)     4192 2021-07-02 22:34:02.000000 samsteady-django-utils-1.0.8/django_utils/fields.py
--rw-r--r--   0 Sam        (501) staff       (20)     2320 2020-10-06 22:22:48.000000 samsteady-django-utils-1.0.8/django_utils/filters.py
--rw-r--r--   0 Sam        (501) staff       (20)     2968 2021-06-01 01:15:16.000000 samsteady-django-utils-1.0.8/django_utils/jwt_url_auth.py
-drwxr-xr-x   0 Sam        (501) staff       (20)        0 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/django_utils/migrations/
--rw-r--r--   0 Sam        (501) staff       (20)        0 2019-12-09 20:56:55.000000 samsteady-django-utils-1.0.8/django_utils/migrations/__init__.py
--rw-r--r--   0 Sam        (501) staff       (20)       73 2020-10-04 03:08:16.000000 samsteady-django-utils-1.0.8/django_utils/mock_request.py
--rw-r--r--   0 Sam        (501) staff       (20)      794 2020-12-12 21:10:19.000000 samsteady-django-utils-1.0.8/django_utils/pagination.py
--rw-r--r--   0 Sam        (501) staff       (20)     1296 2020-10-06 01:58:16.000000 samsteady-django-utils-1.0.8/django_utils/permissions.py
--rw-r--r--   0 Sam        (501) staff       (20)     6130 2021-07-02 20:27:01.000000 samsteady-django-utils-1.0.8/django_utils/serializers.py
--rw-r--r--   0 Sam        (501) staff       (20)      546 2020-10-05 22:17:49.000000 samsteady-django-utils-1.0.8/django_utils/utils.py
--rw-r--r--   0 Sam        (501) staff       (20)     4376 2020-10-06 22:26:55.000000 samsteady-django-utils-1.0.8/django_utils/views.py
-drwxr-xr-x   0 Sam        (501) staff       (20)        0 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/samsteady_django_utils.egg-info/
--rw-r--r--   0 Sam        (501) staff       (20)      807 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/samsteady_django_utils.egg-info/PKG-INFO
--rw-r--r--   0 Sam        (501) staff       (20)      603 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/samsteady_django_utils.egg-info/SOURCES.txt
--rw-r--r--   0 Sam        (501) staff       (20)        1 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/samsteady_django_utils.egg-info/dependency_links.txt
--rw-r--r--   0 Sam        (501) staff       (20)       40 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/samsteady_django_utils.egg-info/requires.txt
--rw-r--r--   0 Sam        (501) staff       (20)       13 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/samsteady_django_utils.egg-info/top_level.txt
--rw-r--r--   0 Sam        (501) staff       (20)      864 2021-07-17 00:17:07.000000 samsteady-django-utils-1.0.8/setup.cfg
--rw-r--r--   0 Sam        (501) staff       (20)       94 2020-10-04 00:37:39.000000 samsteady-django-utils-1.0.8/setup.py
+drwxr-xr-x   0 Sam        (501) staff       (20)        0 2021-07-17 22:03:42.000000 samsteady-django-utils-1.0.9/
+-rw-r--r--   0 Sam        (501) staff       (20)      807 2021-07-17 22:03:42.000000 samsteady-django-utils-1.0.9/PKG-INFO
+-rw-r--r--   0 Sam        (501) staff       (20)       16 2020-10-04 03:25:31.000000 samsteady-django-utils-1.0.9/README.md
+drwxr-xr-x   0 Sam        (501) staff       (20)        0 2021-07-17 22:03:42.000000 samsteady-django-utils-1.0.9/django_utils/
+-rw-r--r--   0 Sam        (501) staff       (20)        0 2020-10-04 03:17:55.000000 samsteady-django-utils-1.0.9/django_utils/__init__.py
+-rw-r--r--   0 Sam        (501) staff       (20)      220 2020-10-12 21:12:57.000000 samsteady-django-utils-1.0.9/django_utils/consumers.py
+-rw-r--r--   0 Sam        (501) staff       (20)      466 2020-10-04 03:17:00.000000 samsteady-django-utils-1.0.9/django_utils/exceptions.py
+-rw-r--r--   0 Sam        (501) staff       (20)     4366 2021-07-17 22:01:33.000000 samsteady-django-utils-1.0.9/django_utils/fields.py
+-rw-r--r--   0 Sam        (501) staff       (20)     2320 2020-10-06 22:22:48.000000 samsteady-django-utils-1.0.9/django_utils/filters.py
+-rw-r--r--   0 Sam        (501) staff       (20)     2968 2021-06-01 01:15:16.000000 samsteady-django-utils-1.0.9/django_utils/jwt_url_auth.py
+drwxr-xr-x   0 Sam        (501) staff       (20)        0 2021-07-17 22:03:42.000000 samsteady-django-utils-1.0.9/django_utils/migrations/
+-rw-r--r--   0 Sam        (501) staff       (20)        0 2019-12-09 20:56:55.000000 samsteady-django-utils-1.0.9/django_utils/migrations/__init__.py
+-rw-r--r--   0 Sam        (501) staff       (20)       73 2020-10-04 03:08:16.000000 samsteady-django-utils-1.0.9/django_utils/mock_request.py
+-rw-r--r--   0 Sam        (501) staff       (20)      794 2020-12-12 21:10:19.000000 samsteady-django-utils-1.0.9/django_utils/pagination.py
+-rw-r--r--   0 Sam        (501) staff       (20)     1296 2020-10-06 01:58:16.000000 samsteady-django-utils-1.0.9/django_utils/permissions.py
+-rw-r--r--   0 Sam        (501) staff       (20)     6433 2021-07-17 22:01:59.000000 samsteady-django-utils-1.0.9/django_utils/serializers.py
+-rw-r--r--   0 Sam        (501) staff       (20)      546 2020-10-05 22:17:49.000000 samsteady-django-utils-1.0.9/django_utils/utils.py
+-rw-r--r--   0 Sam        (501) staff       (20)     4376 2020-10-06 22:26:55.000000 samsteady-django-utils-1.0.9/django_utils/views.py
+drwxr-xr-x   0 Sam        (501) staff       (20)        0 2021-07-17 22:03:42.000000 samsteady-django-utils-1.0.9/samsteady_django_utils.egg-info/
+-rw-r--r--   0 Sam        (501) staff       (20)      807 2021-07-17 22:03:41.000000 samsteady-django-utils-1.0.9/samsteady_django_utils.egg-info/PKG-INFO
+-rw-r--r--   0 Sam        (501) staff       (20)      603 2021-07-17 22:03:41.000000 samsteady-django-utils-1.0.9/samsteady_django_utils.egg-info/SOURCES.txt
+-rw-r--r--   0 Sam        (501) staff       (20)        1 2021-07-17 22:03:41.000000 samsteady-django-utils-1.0.9/samsteady_django_utils.egg-info/dependency_links.txt
+-rw-r--r--   0 Sam        (501) staff       (20)       57 2021-07-17 22:03:41.000000 samsteady-django-utils-1.0.9/samsteady_django_utils.egg-info/requires.txt
+-rw-r--r--   0 Sam        (501) staff       (20)       13 2021-07-17 22:03:41.000000 samsteady-django-utils-1.0.9/samsteady_django_utils.egg-info/top_level.txt
+-rw-r--r--   0 Sam        (501) staff       (20)      882 2021-07-17 22:03:42.000000 samsteady-django-utils-1.0.9/setup.cfg
+-rw-r--r--   0 Sam        (501) staff       (20)       94 2020-10-04 00:37:39.000000 samsteady-django-utils-1.0.9/setup.py
```

### Comparing `samsteady-django-utils-1.0.8/PKG-INFO` & `samsteady-django-utils-1.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: samsteady-django-utils
-Version: 1.0.8
+Version: 1.0.9
 Summary: Django utils
 Home-page: UNKNOWN
 License: MIT
 Description: # Django Utils
         
         
 Platform: UNKNOWN
```

### Comparing `samsteady-django-utils-1.0.8/django_utils/fields.py` & `samsteady-django-utils-1.0.9/django_utils/fields.py`

 * *Files 3% similar despite different names*

```diff
@@ -48,14 +48,22 @@
         return data
 
     def to_representation(self, value):
         if value is None:
             return None
         return str(value)
 
+class JsonFieldSerializerField(serializers.Field):
+
+    def to_representation(self, value):
+        return value
+
+    def to_internal_value(self, data):
+        return data
+
 class IntStrMinValueValidator(MinValueValidator):
     def compare(self, a, b):
         return int(a) < int(b)
 
 
 class IntStrMaxValueValidator(MaxValueValidator):
     def compare(self, a, b):
```

### Comparing `samsteady-django-utils-1.0.8/django_utils/filters.py` & `samsteady-django-utils-1.0.9/django_utils/filters.py`

 * *Files identical despite different names*

### Comparing `samsteady-django-utils-1.0.8/django_utils/jwt_url_auth.py` & `samsteady-django-utils-1.0.9/django_utils/jwt_url_auth.py`

 * *Files identical despite different names*

### Comparing `samsteady-django-utils-1.0.8/django_utils/pagination.py` & `samsteady-django-utils-1.0.9/django_utils/pagination.py`

 * *Files identical despite different names*

### Comparing `samsteady-django-utils-1.0.8/django_utils/permissions.py` & `samsteady-django-utils-1.0.9/django_utils/permissions.py`

 * *Files identical despite different names*

### Comparing `samsteady-django-utils-1.0.8/django_utils/serializers.py` & `samsteady-django-utils-1.0.9/django_utils/serializers.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,25 +1,32 @@
 from functools import wraps
 
-from django_utils.fields import BigIntStrRepr, BigIntStrReprSerializerField
+from django_utils.fields import BigIntStrRepr, BigIntStrReprSerializerField, JsonFieldSerializerField
 from django_utils.mock_request import MockRequest
 from global_requests import get_thread_user
 from guardian_queryset.serializers import ValidateForeignKeyUserMixin, AssignActiveUserDefaultPermissionMixin
 from rest_framework import serializers
 from reversable_primary_key.serializers import CreatedSerializerMixin
+from jsonfield import JSONField
 
 
 class BigIntStrReprSerializerMixin(serializers.Serializer):
 
     @property
     def serializer_field_mapping(self):
         mapping = super().serializer_field_mapping.copy()
         mapping[BigIntStrRepr] = BigIntStrReprSerializerField
         return mapping
 
+class JsonFieldSerializerMixin(serializers.Serializer):
+    @property
+    def serializer_field_mapping(self):
+        mapping = super().serializer_field_mapping.copy()
+        mapping[JSONField] = JsonFieldSerializerField
+        return mapping
 
 class WithMockRequesterSerializerMixin(serializers.Serializer):
 
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         if "request" not in self._context:
             user = get_thread_user()
```

### Comparing `samsteady-django-utils-1.0.8/django_utils/utils.py` & `samsteady-django-utils-1.0.9/django_utils/utils.py`

 * *Files identical despite different names*

### Comparing `samsteady-django-utils-1.0.8/django_utils/views.py` & `samsteady-django-utils-1.0.9/django_utils/views.py`

 * *Files identical despite different names*

### Comparing `samsteady-django-utils-1.0.8/samsteady_django_utils.egg-info/PKG-INFO` & `samsteady-django-utils-1.0.9/samsteady_django_utils.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: samsteady-django-utils
-Version: 1.0.8
+Version: 1.0.9
 Summary: Django utils
 Home-page: UNKNOWN
 License: MIT
 Description: # Django Utils
         
         
 Platform: UNKNOWN
```

### Comparing `samsteady-django-utils-1.0.8/samsteady_django_utils.egg-info/SOURCES.txt` & `samsteady-django-utils-1.0.9/samsteady_django_utils.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `samsteady-django-utils-1.0.8/setup.cfg` & `samsteady-django-utils-1.0.9/setup.cfg`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = samsteady-django-utils
-version = 1.0.8
+version = 1.0.9
 description = Django utils
 long_description = file:README.md
 long_description_content_type = text/markdown
 license = MIT
 classifiers = 
 	Development Status :: 4 - Beta
 	Environment :: Web Environment
@@ -22,12 +22,13 @@
 packages = find:
 python_requires = >=3.6
 setup_requires = 
 	setuptools >= 38.3.0
 install_requires = 
 	django<2.3,>=2
 	djangorestframework>=3.7
+	jsonfield>=3.1.0
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

