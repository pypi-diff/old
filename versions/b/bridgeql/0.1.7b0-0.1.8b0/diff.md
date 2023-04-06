# Comparing `tmp/bridgeql-0.1.7b0.tar.gz` & `tmp/bridgeql-0.1.8b0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bridgeql-0.1.7b0.tar", last modified: Wed Mar 22 19:13:22 2023, max compression
+gzip compressed data, was "bridgeql-0.1.8b0.tar", last modified: Thu Mar 23 15:00:58 2023, max compression
```

## Comparing `bridgeql-0.1.7b0.tar` & `bridgeql-0.1.8b0.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 piyusk     (502) staff       (20)        0 2023-03-22 19:13:22.414732 bridgeql-0.1.7b0/
--rw-r--r--   0 piyusk     (502) staff       (20)     1512 2023-03-22 08:41:33.000000 bridgeql-0.1.7b0/LICENSE
--rw-r--r--   0 piyusk     (502) staff       (20)      403 2023-03-15 16:47:31.000000 bridgeql-0.1.7b0/NOTICE
--rw-r--r--   0 piyusk     (502) staff       (20)     4314 2023-03-22 19:13:22.414409 bridgeql-0.1.7b0/PKG-INFO
--rw-r--r--   0 piyusk     (502) staff       (20)     3133 2023-03-22 19:02:11.000000 bridgeql-0.1.7b0/README.md
-drwxr-xr-x   0 piyusk     (502) staff       (20)        0 2023-03-22 19:13:22.400311 bridgeql-0.1.7b0/bridgeql/
--rw-r--r--   0 piyusk     (502) staff       (20)      119 2023-03-22 18:54:19.000000 bridgeql-0.1.7b0/bridgeql/__init__.py
-drwxr-xr-x   0 piyusk     (502) staff       (20)        0 2023-03-22 19:13:22.413914 bridgeql-0.1.7b0/bridgeql/django/
--rw-r--r--   0 piyusk     (502) staff       (20)      119 2023-03-22 18:54:19.000000 bridgeql-0.1.7b0/bridgeql/django/__init__.py
--rw-r--r--   0 piyusk     (502) staff       (20)     1020 2023-03-22 18:41:53.000000 bridgeql-0.1.7b0/bridgeql/django/bridge.py
--rw-r--r--   0 piyusk     (502) staff       (20)      280 2023-03-22 18:31:38.000000 bridgeql-0.1.7b0/bridgeql/django/exceptions.py
--rw-r--r--   0 piyusk     (502) staff       (20)     1106 2023-03-22 18:32:04.000000 bridgeql-0.1.7b0/bridgeql/django/helpers.py
--rw-r--r--   0 piyusk     (502) staff       (20)     2871 2023-03-22 18:55:27.000000 bridgeql-0.1.7b0/bridgeql/django/models.py
--rw-r--r--   0 piyusk     (502) staff       (20)     1119 2023-03-22 18:36:01.000000 bridgeql-0.1.7b0/bridgeql/django/query.py
--rw-r--r--   0 piyusk     (502) staff       (20)      366 2023-03-22 18:33:54.000000 bridgeql-0.1.7b0/bridgeql/django/urls.py
--rw-r--r--   0 piyusk     (502) staff       (20)      402 2023-03-17 12:12:56.000000 bridgeql-0.1.7b0/bridgeql/utils.py
-drwxr-xr-x   0 piyusk     (502) staff       (20)        0 2023-03-22 19:13:22.402421 bridgeql-0.1.7b0/bridgeql.egg-info/
--rw-r--r--   0 piyusk     (502) staff       (20)     4314 2023-03-22 19:13:22.000000 bridgeql-0.1.7b0/bridgeql.egg-info/PKG-INFO
--rw-r--r--   0 piyusk     (502) staff       (20)      401 2023-03-22 19:13:22.000000 bridgeql-0.1.7b0/bridgeql.egg-info/SOURCES.txt
--rw-r--r--   0 piyusk     (502) staff       (20)        1 2023-03-22 19:13:22.000000 bridgeql-0.1.7b0/bridgeql.egg-info/dependency_links.txt
--rw-r--r--   0 piyusk     (502) staff       (20)        9 2023-03-22 19:13:22.000000 bridgeql-0.1.7b0/bridgeql.egg-info/top_level.txt
--rw-r--r--   0 piyusk     (502) staff       (20)       84 2023-03-17 11:25:16.000000 bridgeql-0.1.7b0/pyproject.toml
--rw-r--r--   0 piyusk     (502) staff       (20)       38 2023-03-22 19:13:22.414823 bridgeql-0.1.7b0/setup.cfg
--rw-r--r--   0 piyusk     (502) staff       (20)     1572 2023-03-22 19:09:23.000000 bridgeql-0.1.7b0/setup.py
+drwxr-xr-x   0 piyusk     (502) staff       (20)        0 2023-03-23 15:00:58.248975 bridgeql-0.1.8b0/
+-rw-r--r--   0 piyusk     (502) staff       (20)     1512 2023-03-22 08:41:33.000000 bridgeql-0.1.8b0/LICENSE
+-rw-r--r--   0 piyusk     (502) staff       (20)      403 2023-03-15 16:47:31.000000 bridgeql-0.1.8b0/NOTICE
+-rw-r--r--   0 piyusk     (502) staff       (20)     4455 2023-03-23 15:00:58.248609 bridgeql-0.1.8b0/PKG-INFO
+-rw-r--r--   0 piyusk     (502) staff       (20)     3274 2023-03-23 14:11:27.000000 bridgeql-0.1.8b0/README.md
+drwxr-xr-x   0 piyusk     (502) staff       (20)        0 2023-03-23 15:00:58.241941 bridgeql-0.1.8b0/bridgeql/
+-rw-r--r--   0 piyusk     (502) staff       (20)      119 2023-03-22 18:54:19.000000 bridgeql-0.1.8b0/bridgeql/__init__.py
+drwxr-xr-x   0 piyusk     (502) staff       (20)        0 2023-03-23 15:00:58.248099 bridgeql-0.1.8b0/bridgeql/django/
+-rw-r--r--   0 piyusk     (502) staff       (20)      173 2023-03-23 14:11:27.000000 bridgeql-0.1.8b0/bridgeql/django/__init__.py
+-rw-r--r--   0 piyusk     (502) staff       (20)     1031 2023-03-23 14:11:27.000000 bridgeql-0.1.8b0/bridgeql/django/bridge.py
+-rw-r--r--   0 piyusk     (502) staff       (20)      280 2023-03-22 18:31:38.000000 bridgeql-0.1.8b0/bridgeql/django/exceptions.py
+-rw-r--r--   0 piyusk     (502) staff       (20)     1106 2023-03-22 18:32:04.000000 bridgeql-0.1.8b0/bridgeql/django/helpers.py
+-rw-r--r--   0 piyusk     (502) staff       (20)     4180 2023-03-23 14:11:27.000000 bridgeql-0.1.8b0/bridgeql/django/models.py
+-rw-r--r--   0 piyusk     (502) staff       (20)     1119 2023-03-22 18:36:01.000000 bridgeql-0.1.8b0/bridgeql/django/query.py
+-rw-r--r--   0 piyusk     (502) staff       (20)      366 2023-03-22 18:33:54.000000 bridgeql-0.1.8b0/bridgeql/django/urls.py
+-rw-r--r--   0 piyusk     (502) staff       (20)      402 2023-03-17 12:12:56.000000 bridgeql-0.1.8b0/bridgeql/utils.py
+drwxr-xr-x   0 piyusk     (502) staff       (20)        0 2023-03-23 15:00:58.244357 bridgeql-0.1.8b0/bridgeql.egg-info/
+-rw-r--r--   0 piyusk     (502) staff       (20)     4455 2023-03-23 15:00:58.000000 bridgeql-0.1.8b0/bridgeql.egg-info/PKG-INFO
+-rw-r--r--   0 piyusk     (502) staff       (20)      401 2023-03-23 15:00:58.000000 bridgeql-0.1.8b0/bridgeql.egg-info/SOURCES.txt
+-rw-r--r--   0 piyusk     (502) staff       (20)        1 2023-03-23 15:00:58.000000 bridgeql-0.1.8b0/bridgeql.egg-info/dependency_links.txt
+-rw-r--r--   0 piyusk     (502) staff       (20)        9 2023-03-23 15:00:58.000000 bridgeql-0.1.8b0/bridgeql.egg-info/top_level.txt
+-rw-r--r--   0 piyusk     (502) staff       (20)       84 2023-03-17 11:25:16.000000 bridgeql-0.1.8b0/pyproject.toml
+-rw-r--r--   0 piyusk     (502) staff       (20)       38 2023-03-23 15:00:58.249075 bridgeql-0.1.8b0/setup.cfg
+-rw-r--r--   0 piyusk     (502) staff       (20)     1572 2023-03-23 14:58:35.000000 bridgeql-0.1.8b0/setup.py
```

### Comparing `bridgeql-0.1.7b0/LICENSE` & `bridgeql-0.1.8b0/LICENSE`

 * *Files identical despite different names*

### Comparing `bridgeql-0.1.7b0/PKG-INFO` & `bridgeql-0.1.8b0/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,34 +1,34 @@
 Metadata-Version: 2.1
 Name: bridgeql
-Version: 0.1.7b0
+Version: 0.1.8b0
 Summary: Query language to bridge the gap between REST API and ORM capability
 Home-page: https://github.com/vmware/bridgeql
 Author: Piyus Kumar
 Author-email: piyusk@vmware.com
 License: BSD-2
 Project-URL: Bug Tracker, https://github.com/vmware/bridgeql/issues
 Keywords: django
 Platform: Any
+Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Classifier: Programming Language :: Python :: 2.7
+Classifier: Development Status :: 4 - Beta
+Classifier: Intended Audience :: Developers
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Framework :: Django :: 1.11
+Classifier: Programming Language :: Python :: 3.9
 Classifier: Framework :: Django :: 4.1
 Classifier: Framework :: Django
-Classifier: Framework :: Django :: 1.11
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3.8
-Classifier: Intended Audience :: Developers
-Classifier: Development Status :: 4 - Beta
-Classifier: Programming Language :: Python :: 3.9
+Classifier: Natural Language :: English
 Classifier: License :: OSI Approved :: BSD License
-Classifier: Framework :: Django :: 2.2
 Classifier: Framework :: Django :: 3.2
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 2.7
-Classifier: Natural Language :: English
 Classifier: Programming Language :: Python
-Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Classifier: Framework :: Django :: 2.2
 Requires-Python: >=2.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 License-File: NOTICE
 
 # BridgeQL
 
@@ -48,14 +48,21 @@
 
 `bridgeql` is release under the BSD-2 license, see the [LICENSE](LICENSE) file.
 
 SPDX-License-Identifier: BSD-2-Clause
 
 ## Django Integration
 
+### Installation
+
+You can install it directly from [pypi.org](https://pypi.org/project/bridgeql/) using
+```shell
+pip install bridgeql
+```
+
 The bridgeql library can be integrated to the Django app by editing settings
 file by including `bridgeql` in the `settings.INSTALLED_APPS` variable.
 Another change required is to add a url to your existing project as
 
 ```
     projectname/projectname/settings.py
 ```
@@ -82,15 +89,15 @@
     ...
 ]
 ...
 ```
 This way your app will be ready to serve the REST API to expose model query, you can request an API like follows:
 ```python
     params = {
-       'using': 'db1',
+       'db_name': 'db1',
        'app_name': 'machine', # required
        'model_name': 'Machine', # required
        'filter': {
            'os__name': 'os-name-1'
         },
         'fields': ['ip', 'name', 'id'],
         'exclude': {
```

### Comparing `bridgeql-0.1.7b0/README.md` & `bridgeql-0.1.8b0/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -16,14 +16,21 @@
 
 `bridgeql` is release under the BSD-2 license, see the [LICENSE](LICENSE) file.
 
 SPDX-License-Identifier: BSD-2-Clause
 
 ## Django Integration
 
+### Installation
+
+You can install it directly from [pypi.org](https://pypi.org/project/bridgeql/) using
+```shell
+pip install bridgeql
+```
+
 The bridgeql library can be integrated to the Django app by editing settings
 file by including `bridgeql` in the `settings.INSTALLED_APPS` variable.
 Another change required is to add a url to your existing project as
 
 ```
     projectname/projectname/settings.py
 ```
@@ -50,15 +57,15 @@
     ...
 ]
 ...
 ```
 This way your app will be ready to serve the REST API to expose model query, you can request an API like follows:
 ```python
     params = {
-       'using': 'db1',
+       'db_name': 'db1',
        'app_name': 'machine', # required
        'model_name': 'Machine', # required
        'filter': {
            'os__name': 'os-name-1'
         },
         'fields': ['ip', 'name', 'id'],
         'exclude': {
```

### Comparing `bridgeql-0.1.7b0/bridgeql/django/bridge.py` & `bridgeql-0.1.8b0/bridgeql/django/bridge.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 # -*- coding: utf-8 -*-
 # Copyright © 2023 VMware, Inc.  All rights reserved.
 # SPDX-License-Identifier: BSD-2-Clause
 
 import json
-from django.views.decorators.http import require_POST
+from django.views.decorators.http import require_GET, require_POST
 
 from bridgeql.django.helpers import JSONResponse
 from bridgeql.django.models import ModelBuilder
 
 
-@require_POST
+@require_GET
 def read_django_model(request):
-    params = request.POST.get('payload', None)
+    params = request.GET.get('payload', None)
     try:
         params = json.loads(params)
         mb = ModelBuilder(params)
         qset = mb.queryset()  # get the result based on the given parameters
         res = {'data': qset, 'message': '', 'success': True}
         return JSONResponse(res)
     except Exception as e:
```

### Comparing `bridgeql-0.1.7b0/bridgeql/django/helpers.py` & `bridgeql-0.1.8b0/bridgeql/django/helpers.py`

 * *Files identical despite different names*

### Comparing `bridgeql-0.1.7b0/bridgeql/django/query.py` & `bridgeql-0.1.8b0/bridgeql/django/query.py`

 * *Files identical despite different names*

### Comparing `bridgeql-0.1.7b0/bridgeql.egg-info/PKG-INFO` & `bridgeql-0.1.8b0/bridgeql.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,34 +1,34 @@
 Metadata-Version: 2.1
 Name: bridgeql
-Version: 0.1.7b0
+Version: 0.1.8b0
 Summary: Query language to bridge the gap between REST API and ORM capability
 Home-page: https://github.com/vmware/bridgeql
 Author: Piyus Kumar
 Author-email: piyusk@vmware.com
 License: BSD-2
 Project-URL: Bug Tracker, https://github.com/vmware/bridgeql/issues
 Keywords: django
 Platform: Any
+Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Classifier: Programming Language :: Python :: 2.7
+Classifier: Development Status :: 4 - Beta
+Classifier: Intended Audience :: Developers
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Framework :: Django :: 1.11
+Classifier: Programming Language :: Python :: 3.9
 Classifier: Framework :: Django :: 4.1
 Classifier: Framework :: Django
-Classifier: Framework :: Django :: 1.11
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3.8
-Classifier: Intended Audience :: Developers
-Classifier: Development Status :: 4 - Beta
-Classifier: Programming Language :: Python :: 3.9
+Classifier: Natural Language :: English
 Classifier: License :: OSI Approved :: BSD License
-Classifier: Framework :: Django :: 2.2
 Classifier: Framework :: Django :: 3.2
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 2.7
-Classifier: Natural Language :: English
 Classifier: Programming Language :: Python
-Classifier: Topic :: Software Development :: Libraries :: Python Modules
+Classifier: Framework :: Django :: 2.2
 Requires-Python: >=2.7
 Description-Content-Type: text/markdown
 License-File: LICENSE
 License-File: NOTICE
 
 # BridgeQL
 
@@ -48,14 +48,21 @@
 
 `bridgeql` is release under the BSD-2 license, see the [LICENSE](LICENSE) file.
 
 SPDX-License-Identifier: BSD-2-Clause
 
 ## Django Integration
 
+### Installation
+
+You can install it directly from [pypi.org](https://pypi.org/project/bridgeql/) using
+```shell
+pip install bridgeql
+```
+
 The bridgeql library can be integrated to the Django app by editing settings
 file by including `bridgeql` in the `settings.INSTALLED_APPS` variable.
 Another change required is to add a url to your existing project as
 
 ```
     projectname/projectname/settings.py
 ```
@@ -82,15 +89,15 @@
     ...
 ]
 ...
 ```
 This way your app will be ready to serve the REST API to expose model query, you can request an API like follows:
 ```python
     params = {
-       'using': 'db1',
+       'db_name': 'db1',
        'app_name': 'machine', # required
        'model_name': 'Machine', # required
        'filter': {
            'os__name': 'os-name-1'
         },
         'fields': ['ip', 'name', 'id'],
         'exclude': {
```

### Comparing `bridgeql-0.1.7b0/setup.py` & `bridgeql-0.1.8b0/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -7,15 +7,15 @@
 
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="bridgeql",
-    version="0.1.7-beta",
+    version="0.1.8-beta",
     author="Piyus Kumar",
     author_email="piyusk@vmware.com",
     description="Query language to bridge the gap between REST API and ORM capability",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='BSD-2',
     platforms=['Any'],
```

