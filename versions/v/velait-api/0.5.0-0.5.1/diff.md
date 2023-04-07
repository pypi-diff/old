# Comparing `tmp/velait_api-0.5.0.tar.gz` & `tmp/velait_api-0.5.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "velait_api-0.5.0.tar", last modified: Thu Mar 16 07:35:51 2023, max compression
+gzip compressed data, was "velait_api-0.5.1.tar", last modified: Fri Apr  7 09:25:55 2023, max compression
```

## Comparing `velait_api-0.5.0.tar` & `velait_api-0.5.1.tar`

### file list

```diff
@@ -1,46 +1,55 @@
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.876757 velait_api-0.5.0/
--rw-rw-rw-   0        0        0      189 2023-03-16 07:35:51.876757 velait_api-0.5.0/PKG-INFO
--rw-rw-rw-   0        0        0        0 2023-02-14 06:59:16.000000 velait_api-0.5.0/README.md
--rw-rw-rw-   0        0        0       42 2023-03-16 07:35:51.877755 velait_api-0.5.0/setup.cfg
--rw-rw-rw-   0        0        0      439 2023-03-16 07:35:47.000000 velait_api-0.5.0/setup.py
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.838763 velait_api-0.5.0/velait/
--rw-rw-rw-   0        0        0        0 2023-03-15 06:47:28.000000 velait_api-0.5.0/velait/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.844754 velait_api-0.5.0/velait/main/
--rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.0/velait/main/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.849754 velait_api-0.5.0/velait/main/api/
--rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.0/velait/main/api/__init__.py
--rw-rw-rw-   0        0        0     1572 2023-03-16 05:55:42.000000 velait_api-0.5.0/velait/main/api/exception_handlers.py
--rw-rw-rw-   0        0        0     5012 2023-03-15 06:50:44.000000 velait_api-0.5.0/velait/main/api/pagination.py
--rw-rw-rw-   0        0        0     1341 2023-02-24 08:04:34.000000 velait_api-0.5.0/velait/main/api/responses.py
--rw-rw-rw-   0        0        0     1326 2023-03-16 06:14:42.000000 velait_api-0.5.0/velait/main/api/serializers.py
--rw-rw-rw-   0        0        0     5346 2023-03-16 05:57:04.000000 velait_api-0.5.0/velait/main/api/views.py
--rw-rw-rw-   0        0        0      150 2023-02-21 05:58:35.000000 velait_api-0.5.0/velait/main/apps.py
--rw-rw-rw-   0        0        0      507 2023-03-15 06:51:08.000000 velait_api-0.5.0/velait/main/exceptions.py
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.850754 velait_api-0.5.0/velait/main/migrations/
--rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.0/velait/main/migrations/__init__.py
--rw-rw-rw-   0        0        0     1249 2023-03-16 05:57:41.000000 velait_api-0.5.0/velait/main/models.py
--rw-rw-rw-   0        0        0      506 2023-02-21 05:58:35.000000 velait_api-0.5.0/velait/main/parser.py
--rw-rw-rw-   0        0        0      479 2023-03-15 06:45:44.000000 velait_api-0.5.0/velait/main/render.py
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.852760 velait_api-0.5.0/velait/main/services/
--rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.0/velait/main/services/__init__.py
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.854752 velait_api-0.5.0/velait/main/services/search/
--rw-rw-rw-   0        0        0        0 2023-03-15 06:49:26.000000 velait_api-0.5.0/velait/main/services/search/__init__.py
--rw-rw-rw-   0        0        0     3895 2023-03-15 06:53:04.000000 velait_api-0.5.0/velait/main/services/search/base_search.py
--rw-rw-rw-   0        0        0     2135 2023-03-15 06:52:14.000000 velait_api-0.5.0/velait/main/services/search/search.py
--rw-rw-rw-   0        0        0      380 2023-02-21 05:58:35.000000 velait_api-0.5.0/velait/main/services/utils.py
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.860754 velait_api-0.5.0/velait/velait_users/
--rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.0/velait/velait_users/__init__.py
--rw-rw-rw-   0        0        0      168 2023-03-15 06:45:44.000000 velait_api-0.5.0/velait/velait_users/apps.py
--rw-rw-rw-   0        0        0      263 2023-03-15 06:48:57.000000 velait_api-0.5.0/velait/velait_users/exceptions.py
--rw-rw-rw-   0        0        0     2693 2023-03-15 06:45:44.000000 velait_api-0.5.0/velait/velait_users/middleware.py
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.861754 velait_api-0.5.0/velait/velait_users/migrations/
--rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.0/velait/velait_users/migrations/__init__.py
--rw-rw-rw-   0        0        0     1206 2023-03-15 06:45:44.000000 velait_api-0.5.0/velait/velait_users/services.py
--rw-rw-rw-   0        0        0      388 2023-03-15 06:45:44.000000 velait_api-0.5.0/velait/velait_users/urls.py
--rw-rw-rw-   0        0        0     1873 2023-03-15 06:45:44.000000 velait_api-0.5.0/velait/velait_users/views.py
-drwxrwxrwx   0        0        0        0 2023-03-16 07:35:51.875762 velait_api-0.5.0/velait_api.egg-info/
--rw-rw-rw-   0        0        0      189 2023-03-16 07:35:51.000000 velait_api-0.5.0/velait_api.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1002 2023-03-16 07:35:51.000000 velait_api-0.5.0/velait_api.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-16 07:35:51.000000 velait_api-0.5.0/velait_api.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       85 2023-03-16 07:35:51.000000 velait_api-0.5.0/velait_api.egg-info/requires.txt
--rw-rw-rw-   0        0        0        7 2023-03-16 07:35:51.000000 velait_api-0.5.0/velait_api.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.712113 velait_api-0.5.1/
+-rw-rw-rw-   0        0        0      189 2023-04-07 09:25:55.712113 velait_api-0.5.1/PKG-INFO
+-rw-rw-rw-   0        0        0        0 2023-02-14 06:59:16.000000 velait_api-0.5.1/README.md
+-rw-rw-rw-   0        0        0       42 2023-04-07 09:25:55.712113 velait_api-0.5.1/setup.cfg
+-rw-rw-rw-   0        0        0      495 2023-04-07 08:57:56.000000 velait_api-0.5.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.376928 velait_api-0.5.1/velait/
+-rw-rw-rw-   0        0        0        0 2023-03-15 06:47:28.000000 velait_api-0.5.1/velait/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.681029 velait_api-0.5.1/velait/main/
+-rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.1/velait/main/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.686316 velait_api-0.5.1/velait/main/api/
+-rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.1/velait/main/api/__init__.py
+-rw-rw-rw-   0        0        0     1572 2023-03-16 05:55:42.000000 velait_api-0.5.1/velait/main/api/exception_handlers.py
+-rw-rw-rw-   0        0        0     5012 2023-03-15 06:50:44.000000 velait_api-0.5.1/velait/main/api/pagination.py
+-rw-rw-rw-   0        0        0     1341 2023-02-24 08:04:34.000000 velait_api-0.5.1/velait/main/api/responses.py
+-rw-rw-rw-   0        0        0     1326 2023-03-16 06:14:42.000000 velait_api-0.5.1/velait/main/api/serializers.py
+-rw-rw-rw-   0        0        0     5346 2023-03-16 05:57:04.000000 velait_api-0.5.1/velait/main/api/views.py
+-rw-rw-rw-   0        0        0      210 2023-04-07 09:18:38.000000 velait_api-0.5.1/velait/main/apps.py
+-rw-rw-rw-   0        0        0      507 2023-03-15 06:51:08.000000 velait_api-0.5.1/velait/main/exceptions.py
+-rw-rw-rw-   0        0        0     3475 2023-04-04 10:05:12.000000 velait_api-0.5.1/velait/main/logging.py
+-rw-rw-rw-   0        0        0      590 2023-04-04 09:22:28.000000 velait_api-0.5.1/velait/main/middleware.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.687318 velait_api-0.5.1/velait/main/migrations/
+-rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.1/velait/main/migrations/__init__.py
+-rw-rw-rw-   0        0        0     1335 2023-04-07 09:01:13.000000 velait_api-0.5.1/velait/main/models.py
+-rw-rw-rw-   0        0        0      506 2023-02-21 05:58:35.000000 velait_api-0.5.1/velait/main/parser.py
+-rw-rw-rw-   0        0        0      479 2023-03-15 06:45:44.000000 velait_api-0.5.1/velait/main/render.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.688315 velait_api-0.5.1/velait/main/services/
+-rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.1/velait/main/services/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.691316 velait_api-0.5.1/velait/main/services/search/
+-rw-rw-rw-   0        0        0        0 2023-03-15 06:49:26.000000 velait_api-0.5.1/velait/main/services/search/__init__.py
+-rw-rw-rw-   0        0        0     3895 2023-03-15 06:53:04.000000 velait_api-0.5.1/velait/main/services/search/base_search.py
+-rw-rw-rw-   0        0        0     2135 2023-03-15 06:52:14.000000 velait_api-0.5.1/velait/main/services/search/search.py
+-rw-rw-rw-   0        0        0      380 2023-02-21 05:58:35.000000 velait_api-0.5.1/velait/main/services/utils.py
+-rw-rw-rw-   0        0        0      818 2023-04-04 09:59:51.000000 velait_api-0.5.1/velait/main/settings.py
+-rw-rw-rw-   0        0        0     2633 2023-04-07 09:23:26.000000 velait_api-0.5.1/velait/main/signals.py
+-rw-rw-rw-   0        0        0      193 2023-04-04 09:22:21.000000 velait_api-0.5.1/velait/main/utils.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.699347 velait_api-0.5.1/velait/velait_users/
+-rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.1/velait/velait_users/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.702070 velait_api-0.5.1/velait/velait_users/api/
+-rw-rw-rw-   0        0        0        0 2023-04-07 08:52:46.000000 velait_api-0.5.1/velait/velait_users/api/__init__.py
+-rw-rw-rw-   0        0        0      322 2023-04-07 08:53:32.000000 velait_api-0.5.1/velait/velait_users/api/serializers.py
+-rw-rw-rw-   0        0        0      421 2023-04-07 08:55:32.000000 velait_api-0.5.1/velait/velait_users/api/views.py
+-rw-rw-rw-   0        0        0      168 2023-03-15 06:45:44.000000 velait_api-0.5.1/velait/velait_users/apps.py
+-rw-rw-rw-   0        0        0      263 2023-03-15 06:48:57.000000 velait_api-0.5.1/velait/velait_users/exceptions.py
+-rw-rw-rw-   0        0        0     2799 2023-04-04 09:56:27.000000 velait_api-0.5.1/velait/velait_users/middleware.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.703054 velait_api-0.5.1/velait/velait_users/migrations/
+-rw-rw-rw-   0        0        0        0 2023-02-21 05:58:35.000000 velait_api-0.5.1/velait/velait_users/migrations/__init__.py
+-rw-rw-rw-   0        0        0     1206 2023-03-15 06:45:44.000000 velait_api-0.5.1/velait/velait_users/services.py
+-rw-rw-rw-   0        0        0      388 2023-03-15 06:45:44.000000 velait_api-0.5.1/velait/velait_users/urls.py
+-rw-rw-rw-   0        0        0     1873 2023-04-07 08:53:00.000000 velait_api-0.5.1/velait/velait_users/views.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:25:55.711058 velait_api-0.5.1/velait_api.egg-info/
+-rw-rw-rw-   0        0        0      189 2023-04-07 09:25:55.000000 velait_api-0.5.1/velait_api.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1227 2023-04-07 09:25:55.000000 velait_api-0.5.1/velait_api.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 09:25:55.000000 velait_api-0.5.1/velait_api.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0      117 2023-04-07 09:25:55.000000 velait_api-0.5.1/velait_api.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        7 2023-04-07 09:25:55.000000 velait_api-0.5.1/velait_api.egg-info/top_level.txt
```

### Comparing `velait_api-0.5.0/velait/main/api/exception_handlers.py` & `velait_api-0.5.1/velait/main/api/exception_handlers.py`

 * *Files identical despite different names*

### Comparing `velait_api-0.5.0/velait/main/api/pagination.py` & `velait_api-0.5.1/velait/main/api/pagination.py`

 * *Files identical despite different names*

### Comparing `velait_api-0.5.0/velait/main/api/responses.py` & `velait_api-0.5.1/velait/main/api/responses.py`

 * *Files identical despite different names*

### Comparing `velait_api-0.5.0/velait/main/api/serializers.py` & `velait_api-0.5.1/velait/main/api/serializers.py`

 * *Files identical despite different names*

### Comparing `velait_api-0.5.0/velait/main/api/views.py` & `velait_api-0.5.1/velait/main/api/views.py`

 * *Files identical despite different names*

### Comparing `velait_api-0.5.0/velait/main/models.py` & `velait_api-0.5.1/velait/main/models.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 from uuid import uuid4
 
 from django.db import models
+from auditlog.registry import auditlog
 from safedelete import HARD_DELETE_NOCASCADE
 from safedelete.models import SafeDeleteModel
 from django.contrib.postgres.indexes import BrinIndex
 from django.utils.translation import gettext_lazy as _
 
 
 class BaseModel(SafeDeleteModel):
@@ -27,7 +28,10 @@
         indexes = (
             models.Index(fields=('id',)),
             BrinIndex(fields=('uuid',)),
         )
         ordering = (
             'uuid',
         )
+
+
+register_model_audit = auditlog.register
```

### Comparing `velait_api-0.5.0/velait/main/services/search/base_search.py` & `velait_api-0.5.1/velait/main/services/search/base_search.py`

 * *Files identical despite different names*

### Comparing `velait_api-0.5.0/velait/main/services/search/search.py` & `velait_api-0.5.1/velait/main/services/search/search.py`

 * *Files identical despite different names*

### Comparing `velait_api-0.5.0/velait/velait_users/middleware.py` & `velait_api-0.5.1/velait/velait_users/middleware.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 import json
 
 import requests
 from django.conf import settings
 from django.contrib.auth import get_user_model
 from django.contrib.auth.models import AnonymousUser
 from django.contrib.auth.middleware import AuthenticationMiddleware as BaseAuthMiddleware
+from defender.middleware import FailedLoginMiddleware
 
 from velait.velait_users.services import authorize_user
 
 
 User = get_user_model()
 
 
@@ -74,7 +75,12 @@
 
         user_data = self.get_user_data(request.COOKIES.get('access_token'))
         if user_data is None:
             return self._refresh_user(request)
 
         request.user = user_data
         return self.get_response(request)
+
+
+UserBanMiddleware = FailedLoginMiddleware
+
+
```

### Comparing `velait_api-0.5.0/velait/velait_users/services.py` & `velait_api-0.5.1/velait/velait_users/services.py`

 * *Files identical despite different names*

### Comparing `velait_api-0.5.0/velait/velait_users/views.py` & `velait_api-0.5.1/velait/velait_users/views.py`

 * *Files identical despite different names*

### Comparing `velait_api-0.5.0/velait_api.egg-info/SOURCES.txt` & `velait_api-0.5.1/velait_api.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -1,16 +1,21 @@
 README.md
 setup.py
 velait/__init__.py
 velait/main/__init__.py
 velait/main/apps.py
 velait/main/exceptions.py
+velait/main/logging.py
+velait/main/middleware.py
 velait/main/models.py
 velait/main/parser.py
 velait/main/render.py
+velait/main/settings.py
+velait/main/signals.py
+velait/main/utils.py
 velait/main/api/__init__.py
 velait/main/api/exception_handlers.py
 velait/main/api/pagination.py
 velait/main/api/responses.py
 velait/main/api/serializers.py
 velait/main/api/views.py
 velait/main/migrations/__init__.py
@@ -22,13 +27,16 @@
 velait/velait_users/__init__.py
 velait/velait_users/apps.py
 velait/velait_users/exceptions.py
 velait/velait_users/middleware.py
 velait/velait_users/services.py
 velait/velait_users/urls.py
 velait/velait_users/views.py
+velait/velait_users/api/__init__.py
+velait/velait_users/api/serializers.py
+velait/velait_users/api/views.py
 velait/velait_users/migrations/__init__.py
 velait_api.egg-info/PKG-INFO
 velait_api.egg-info/SOURCES.txt
 velait_api.egg-info/dependency_links.txt
 velait_api.egg-info/requires.txt
 velait_api.egg-info/top_level.txt
```

