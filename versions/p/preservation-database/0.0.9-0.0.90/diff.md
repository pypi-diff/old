# Comparing `tmp/preservation-database-0.0.9.tar.gz` & `tmp/preservation-database-0.0.90.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "preservation-database-0.0.9.tar", last modified: Mon Feb 13 14:55:35 2023, max compression
+gzip compressed data, was "preservation-database-0.0.90.tar", last modified: Thu Apr  6 15:37:28 2023, max compression
```

## Comparing `preservation-database-0.0.9.tar` & `preservation-database-0.0.90.tar`

### file list

```diff
@@ -1,28 +1,27 @@
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-02-13 14:55:35.203262 preservation-database-0.0.9/
--rw-rw-r--   0 martin    (1000) martin    (1000)      129 2023-02-06 17:29:02.000000 preservation-database-0.0.9/MANIFEST.in
--rw-rw-r--   0 martin    (1000) martin    (1000)     3795 2023-02-13 14:55:35.203262 preservation-database-0.0.9/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)     3016 2023-02-13 14:55:29.000000 preservation-database-0.0.9/README.md
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-02-13 14:55:35.203262 preservation-database-0.0.9/preservation_database.egg-info/
--rw-rw-r--   0 martin    (1000) martin    (1000)     3795 2023-02-13 14:55:35.000000 preservation-database-0.0.9/preservation_database.egg-info/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)      710 2023-02-13 14:55:35.000000 preservation-database-0.0.9/preservation_database.egg-info/SOURCES.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-02-13 14:55:35.000000 preservation-database-0.0.9/preservation_database.egg-info/dependency_links.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)      138 2023-02-13 14:55:35.000000 preservation-database-0.0.9/preservation_database.egg-info/requires.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)       21 2023-02-13 14:55:35.000000 preservation-database-0.0.9/preservation_database.egg-info/top_level.txt
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-02-13 14:55:35.203262 preservation-database-0.0.9/preservationdatabase/
--rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:14:23.000000 preservation-database-0.0.9/preservationdatabase/__init__.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      409 2023-01-03 14:16:24.000000 preservation-database-0.0.9/preservationdatabase/asgi.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     5595 2023-02-13 10:37:44.000000 preservation-database-0.0.9/preservationdatabase/cli.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      398 2023-02-06 09:32:15.000000 preservation-database-0.0.9/preservationdatabase/constants.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     3458 2023-01-27 18:48:10.000000 preservation-database-0.0.9/preservationdatabase/example_settings.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    23943 2023-02-13 14:54:53.000000 preservation-database-0.0.9/preservationdatabase/models.py
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-02-13 14:55:35.203262 preservation-database-0.0.9/preservationdatabase/test_data/
--rw-rw-r--   0 martin    (1000) martin    (1000)      888 2023-02-06 10:17:59.000000 preservation-database-0.0.9/preservationdatabase/test_data/tests.jsonl
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-02-13 14:55:35.203262 preservation-database-0.0.9/preservationdatabase/tests/
--rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:20:11.000000 preservation-database-0.0.9/preservationdatabase/tests/__init__.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     2072 2023-02-06 10:15:46.000000 preservation-database-0.0.9/preservationdatabase/tests/test_archives.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      807 2023-02-06 09:31:41.000000 preservation-database-0.0.9/preservationdatabase/urls.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    12346 2023-02-13 14:46:28.000000 preservation-database-0.0.9/preservationdatabase/utils.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      540 2023-02-06 09:31:54.000000 preservation-database-0.0.9/preservationdatabase/views.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      409 2023-01-03 14:16:24.000000 preservation-database-0.0.9/preservationdatabase/wsgi.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     1118 2023-02-13 14:55:24.000000 preservation-database-0.0.9/pyproject.toml
--rw-rw-r--   0 martin    (1000) martin    (1000)     1065 2023-02-13 14:55:35.203262 preservation-database-0.0.9/setup.cfg
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:37:28.489812 preservation-database-0.0.90/
+-rw-rw-r--   0 martin    (1000) martin    (1000)      129 2023-02-06 17:29:02.000000 preservation-database-0.0.90/MANIFEST.in
+-rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 15:37:28.489812 preservation-database-0.0.90/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)     4701 2023-04-06 15:37:24.000000 preservation-database-0.0.90/README.md
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:37:28.489812 preservation-database-0.0.90/preservation_database.egg-info/
+-rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 15:37:28.000000 preservation-database-0.0.90/preservation_database.egg-info/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)      691 2023-04-06 15:37:28.000000 preservation-database-0.0.90/preservation_database.egg-info/SOURCES.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-04-06 15:37:28.000000 preservation-database-0.0.90/preservation_database.egg-info/dependency_links.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)      208 2023-04-06 15:37:28.000000 preservation-database-0.0.90/preservation_database.egg-info/requires.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)       21 2023-04-06 15:37:28.000000 preservation-database-0.0.90/preservation_database.egg-info/top_level.txt
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:37:28.489812 preservation-database-0.0.90/preservationdatabase/
+-rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:14:23.000000 preservation-database-0.0.90/preservationdatabase/__init__.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    15336 2023-04-06 14:03:38.000000 preservation-database-0.0.90/preservationdatabase/cli.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)      660 2023-03-01 11:09:55.000000 preservation-database-0.0.90/preservationdatabase/constants.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1597 2023-03-05 12:44:30.000000 preservation-database-0.0.90/preservationdatabase/environment.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     3450 2023-02-19 18:38:37.000000 preservation-database-0.0.90/preservationdatabase/example_settings.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    34278 2023-04-06 15:37:22.000000 preservation-database-0.0.90/preservationdatabase/exporter.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    42928 2023-04-06 14:20:58.000000 preservation-database-0.0.90/preservationdatabase/models.py
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:37:28.489812 preservation-database-0.0.90/preservationdatabase/test_data/
+-rw-rw-r--   0 martin    (1000) martin    (1000)      888 2023-02-06 10:17:59.000000 preservation-database-0.0.90/preservationdatabase/test_data/tests.jsonl
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:37:28.489812 preservation-database-0.0.90/preservationdatabase/tests/
+-rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:20:11.000000 preservation-database-0.0.90/preservationdatabase/tests/__init__.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     2072 2023-02-06 10:15:46.000000 preservation-database-0.0.90/preservationdatabase/tests/test_archives.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)      767 2023-02-19 18:38:37.000000 preservation-database-0.0.90/preservationdatabase/urls.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    20636 2023-04-06 13:59:40.000000 preservation-database-0.0.90/preservationdatabase/utils.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1238 2023-04-06 15:33:11.000000 preservation-database-0.0.90/pyproject.toml
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1143 2023-04-06 15:37:28.493812 preservation-database-0.0.90/setup.cfg
```

### Comparing `preservation-database-0.0.9/preservation_database.egg-info/SOURCES.txt` & `preservation-database-0.0.90/preservation_database.egg-info/SOURCES.txt`

 * *Files 13% similar despite different names*

```diff
@@ -4,19 +4,18 @@
 setup.cfg
 preservation_database.egg-info/PKG-INFO
 preservation_database.egg-info/SOURCES.txt
 preservation_database.egg-info/dependency_links.txt
 preservation_database.egg-info/requires.txt
 preservation_database.egg-info/top_level.txt
 preservationdatabase/__init__.py
-preservationdatabase/asgi.py
 preservationdatabase/cli.py
 preservationdatabase/constants.py
+preservationdatabase/environment.py
 preservationdatabase/example_settings.py
+preservationdatabase/exporter.py
 preservationdatabase/models.py
 preservationdatabase/urls.py
 preservationdatabase/utils.py
-preservationdatabase/views.py
-preservationdatabase/wsgi.py
 preservationdatabase/test_data/tests.jsonl
 preservationdatabase/tests/__init__.py
 preservationdatabase/tests/test_archives.py
```

### Comparing `preservation-database-0.0.9/preservationdatabase/example_settings.py` & `preservation-database-0.0.90/preservationdatabase/example_settings.py`

 * *Files 12% similar despite different names*

```diff
@@ -11,122 +11,115 @@
 """
 import os
 from pathlib import Path
 
 # Build paths inside the project like this: BASE_DIR / 'subdir'.
 BASE_DIR = Path(__file__).resolve().parent.parent
 
-
 # Quick-start development settings - unsuitable for production
 # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
 
 # SECURITY WARNING: keep the secret key used in production secret!
-SECRET_KEY = 'SECRET-KEY-HERE'
+SECRET_KEY = "SECRET-KEY-HERE"
 
 # SECURITY WARNING: don't run with debug turned on in production!
 DEBUG = True
 
-ALLOWED_HOSTS = ['*']
-CSRF_TRUSTED_ORIGINS = ['https://thevault.fly.dev']
-
+ALLOWED_HOSTS = ["*"]
+CSRF_TRUSTED_ORIGINS = ["https://thevault.fly.dev"]
 
 # Application definition
 
 INSTALLED_APPS = [
-    'django.contrib.admin',
-    'django.contrib.auth',
-    'django.contrib.contenttypes',
-    'django.contrib.sessions',
-    'django.contrib.messages',
-    'django.contrib.staticfiles',
-
-    'macros',
-    'rest_framework',
-
-    'preservationData',
-    'api'
+    "django.contrib.admin",
+    "django.contrib.auth",
+    "django.contrib.contenttypes",
+    "django.contrib.sessions",
+    "django.contrib.messages",
+    "django.contrib.staticfiles",
+    "macros",
+    "rest_framework",
+    "preservationData",
+    "api",
 ]
 
 MIDDLEWARE = [
-    'django.middleware.security.SecurityMiddleware',
-    'django.contrib.sessions.middleware.SessionMiddleware',
-    'django.middleware.common.CommonMiddleware',
-    'django.middleware.csrf.CsrfViewMiddleware',
-    'django.contrib.auth.middleware.AuthenticationMiddleware',
-    'django.contrib.messages.middleware.MessageMiddleware',
-    'django.middleware.clickjacking.XFrameOptionsMiddleware',
+    "django.middleware.security.SecurityMiddleware",
+    "django.contrib.sessions.middleware.SessionMiddleware",
+    "django.middleware.common.CommonMiddleware",
+    "django.middleware.csrf.CsrfViewMiddleware",
+    "django.contrib.auth.middleware.AuthenticationMiddleware",
+    "django.contrib.messages.middleware.MessageMiddleware",
+    "django.middleware.clickjacking.XFrameOptionsMiddleware",
 ]
 
-ROOT_URLCONF = 'preservationData.urls'
+ROOT_URLCONF = "preservationData.urls"
 
 TEMPLATES = [
     {
-        'BACKEND': 'django.template.backends.django.DjangoTemplates',
-        'DIRS': [BASE_DIR / 'templates']
-        ,
-        'APP_DIRS': True,
-        'OPTIONS': {
-            'context_processors': [
-                'django.template.context_processors.debug',
-                'django.template.context_processors.request',
-                'django.contrib.auth.context_processors.auth',
-                'django.contrib.messages.context_processors.messages',
+        "BACKEND": "django.template.backends.django.DjangoTemplates",
+        "DIRS": [BASE_DIR / "templates"],
+        "APP_DIRS": True,
+        "OPTIONS": {
+            "context_processors": [
+                "django.template.context_processors.debug",
+                "django.template.context_processors.request",
+                "django.contrib.auth.context_processors.auth",
+                "django.contrib.messages.context_processors.messages",
             ],
         },
     },
 ]
 
-WSGI_APPLICATION = 'preservationData.wsgi.application'
-
+WSGI_APPLICATION = "preservationData.wsgi.application"
 
 # Database
 # https://docs.djangoproject.com/en/4.1/ref/settings/#databases
 
 DATABASES = {
-    'default': {
-        'ENGINE': 'django.db.backends.sqlite3',
-        'NAME': BASE_DIR / 'db.sqlite3',
+    "default": {
+        "ENGINE": "django.db.backends.sqlite3",
+        "NAME": BASE_DIR / "db.sqlite3",
     }
 }
 
-
 # Password validation
 # https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
 
 AUTH_PASSWORD_VALIDATORS = [
     {
-        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
+        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
     },
     {
-        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
+        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
     },
     {
-        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
+        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
     },
     {
-        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
+        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
     },
 ]
 
-
 # Internationalization
 # https://docs.djangoproject.com/en/4.1/topics/i18n/
 
-LANGUAGE_CODE = 'en-us'
+LANGUAGE_CODE = "en-us"
 
-TIME_ZONE = 'UTC'
+TIME_ZONE = "UTC"
 
 USE_I18N = True
 
 USE_TZ = True
 
-
 # Static files (CSS, JavaScript, Images)
 # https://docs.djangoproject.com/en/4.1/howto/static-files/
 
-STATIC_URL = 'static/'
-STATIC_ROOT = '/home/martin/Documents/Programming/crossref/preservationData/static_media/'
+STATIC_URL = "static/"
+STATIC_ROOT = (
+    "/home/martin/Documents/Programming/crossref/preservationData/static_media/"
+)
 
 # Default primary key field type
 # https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field
 
-DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
+DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
```

### Comparing `preservation-database-0.0.9/preservationdatabase/test_data/tests.jsonl` & `preservation-database-0.0.90/preservationdatabase/test_data/tests.jsonl`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.9/preservationdatabase/tests/test_archives.py` & `preservation-database-0.0.90/preservationdatabase/tests/test_archives.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.9/preservationdatabase/urls.py` & `preservation-database-0.0.90/preservationdatabase/urls.py`

 * *Files 22% similar despite different names*

```diff
@@ -12,12 +12,10 @@
 Including another URLconf
     1. Import the include() function: from django.urls import include, path
     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
 """
 from django.contrib import admin
 from django.urls import path, include
 
-from preservationdatabase import views
-
 urlpatterns = [
-    path('admin/', admin.site.urls),
+    path("admin/", admin.site.urls),
 ]
```

### Comparing `preservation-database-0.0.9/preservationdatabase/utils.py` & `preservation-database-0.0.90/preservationdatabase/utils.py`

 * *Files 26% similar despite different names*

```diff
@@ -1,107 +1,231 @@
+import csv
+import gc
 import logging
 import re
+import sys
+import tracemalloc
 from csv import DictReader
 from io import StringIO
+from random import randint
 
+import django
 import requests
-from crossref.restful import Etiquette, Works
-from django.db.models import QuerySet
+from crossref.restful import Etiquette, Journals, Works
+from django.db import transaction
+from django.db.models import QuerySet, Count
+
 from lxml import etree as ET
 
 
-def show_preservation(container_title: str, issn: str, volume: str,
-                      no: str | None, doi: str,
-                      archive: str = None) -> (dict | None, str):
+def expand_issns(issn) -> set:
+    """
+    Expands a list of ISSNs using the ISSNL lookup database.
+    :param issn: the list of ISSNs to expand
+    :return: a set of expanded ISSNs
+    """
+    from preservationdatabase.models import ISSN, ISSNL
+
+    final_issn_list = []
+
+    for issn_item in issn:
+        final_issn_list.append(issn_item)
+        issn_objs = ISSN.objects.filter(identifier=issn_item)
+        issnl_objs = ISSNL.objects.filter(identifier=issn_item)
+
+        for issn_obj in issn_objs:
+            issnl_objs = ISSNL.objects.filter(
+                identifier=issn_obj.issnl.identifier
+            )
+
+            for issnl_obj in issnl_objs:
+                issn_reversed = ISSN.objects.filter(issnl=issnl_obj)
+
+                for issn_reversed_obj in issn_reversed:
+                    final_issn_list.append(issn_reversed_obj.identifier)
+
+        for issn_reversed in issnl_objs:
+            final_issn_list.append(issn_reversed.identifier)
+
+            issn_objs = ISSN.objects.filter(issnl=issn_reversed)
+
+            for issn_obj in issn_objs:
+                final_issn_list.append(issn_obj.identifier)
+
+    final_issn_list = set(final_issn_list)
+
+    return final_issn_list
+
+
+def show_preservation(
+    container_title: str,
+    issn: set,
+    volume: str,
+    no: str | None,
+    doi: str,
+    archive: str = None,
+    year: str | None = None,
+    no_issn: bool = False,
+    verbose: bool = False,
+) -> (dict | None, str):
     """
     Determine whether an item is preserved
     :param container_title: the journal/container name
     :param issn: the ISSN
     :param volume: the volume
     :param no: the number
     :param doi: the DOI
+    :param no_issn: if true, will not look up ISSNs for expansion
+    :param year: the year
+    :param verbose: if true, will print status updates
     :param archive: the archive to query (or None for all archives)
     :return: a dictionary of preservations and a doi
     """
     from preservationdatabase import constants
 
+    # extend ISSNs
+    issn = [] if not issn else issn
+    issn = set(issn)
+
+    # extend the ISSN using the ISSNL lookup table
+    if no_issn:
+        final_issn_list = issn
+    else:
+        final_issn_list = expand_issns(issn)
+
+    if issn != final_issn_list and verbose:
+        logging.info(
+            f"Expanded ISSN list for title from {issn} to {final_issn_list}"
+        )
+
     if archive is None:
         preservation_systems = [*constants.archives.values()]
     else:
         preservation_systems = [constants.archives[archive]]
 
     preservations = {}
 
     for system in preservation_systems:
-        preserved, done = system.preservation(container_title, issn, volume, no)
+        preserved, done = system.preservation(
+            container_title, final_issn_list, volume, no=no, year=year, doi=doi
+        )
         preservations[system.name()] = preserved, done
 
     return preservations, doi
 
 
-def unpack_range(s):
-    """ Converts a range of numbers to a full set"""
+def unpack_range(s: str) -> list:
+    """Converts a range of numbers to a full set"""
     r = []
-    for i in s.split(','):
-        if '-' not in i:
+    for i in s.split(","):
+        if "-" not in i and " to " not in i:
             r.append(int(i))
+        elif " to " in i:
+            l, h = map(int, i.split(" to "))
+            r += range(l, h + 1)
         else:
-            l, h = map(int, i.split('-'))
+            l, h = map(int, i.split("-"))
             r += range(l, h + 1)
     return r
 
 
-def show_preservation_for_doi(doi: str,
-                              archive: str = None) -> (dict | None, str):
+def show_preservation_for_doi(
+    doi_input: str, archive: str = None, no_issn: bool = False
+) -> (dict | None, str):
     """
     Determine whether a DOI is preserved with resolution via the REST API
-    :param doi: the DOI to look up
+    :param doi_input: the DOI to look up
+    :param no_issn: if true, will not look up ISSNs for expansion
     :param archive: the archive to query (or None for all archives)
     :return:
     """
-    # TODO: caching
-    # TODO: tests
-    # TODO: type hints
-    # TODO: externalize settings
 
-    my_etiquette = Etiquette('Preservation Status', '0.01',
-                             'https://eve.gd', 'meve@crossref.org')
+    my_etiquette = Etiquette(
+        "Preservation Status", "0.01", "https://eve.gd", "meve@crossref.org"
+    )
 
     works = Works(etiquette=my_etiquette)
-    doi = works.doi(doi)
+    doi = works.doi(doi_input)
+
+    if not doi:
+        logging.info(f"Unable to resolve DOI: {doi_input}")
+        return {}, doi_input
+
+    container_title = (
+        doi["container-title"] if "container-title" in doi else None
+    )
+    issns = set(doi["ISSN"]) if "ISSN" in doi else None
+
+    volume = doi["volume"] if "volume" in doi else None
+    no = doi["issue"] if "issue" in doi else None
+
+    logging.info(
+        f'Checking {doi["DOI"]}: {container_title} '
+        f"({issns}) v{volume} n{no}"
+    )
+
+    year = None
+    # "published": {"date-parts": [[2005, 12, 30]]}}}
+
+    if "published" in doi:
+        year = doi["published"]["date-parts"][0][0]
+
+    preserves, doi_echo = show_preservation(
+        container_title,
+        issns,
+        volume,
+        no,
+        doi,
+        archive,
+        year=year,
+        no_issn=no_issn,
+    )
+
+    # the "archive" field is apparently returned if deposited
+
+    archives = set(doi["archive"]) if "archive" in doi else set()
+
+    if "archive" in doi:
+        for archive in archives:
+            if archive in preserves and preserves[archive][0]:
+                logging.info(
+                    f"{doi_input} correctly asserts preservation in {archive}."
+                )
+            else:
+                logging.info(
+                    f"{doi_input} incorrectly asserts preservation in {archive}."
+                )
 
-    container_title = doi['container-title']
-    issn = doi['ISSN']
-    volume = doi['volume']
-    no = doi['issue']
+    else:
+        logging.info(f"{doi_input} asserts no preservation information.")
 
-    return show_preservation(container_title, issn, volume, no, doi, archive)
+    return preserves, doi_input
 
 
 def normalize_doi(doi: str) -> str:
     """
     Normalize a DOI
     :param doi: the DOI to normalize
     :return: a DOI without the prefix
     """
 
     # extract the DOI from the input
     # note that this is not as rigorous as it could be, but writing a single
     # expression that captures everything is hard.
     # See: https://www.crossref.org/blog/dois-and-matching-regular-expressions/
-    pattern = r'(10.\d{4,9}/[-._;()/:A-Z0-9]+)'
+    pattern = r"(10.\d{4,9}/[-._;()/:A-Z0-9]+)"
 
     result = re.search(pattern, doi, re.IGNORECASE)
 
     return result.group(0) if result else None
 
 
-def generic_lockss_import(url: str, model,
-                          skip_first_line: bool = False,
-                          local: bool = False) -> None:
+def generic_lockss_import(
+    url: str, model, skip_first_line: bool = False, local: bool = False
+) -> None:
     """
     The generic import function for LOCKSS-like models
     :param url: the URL to download
     :param model: the model class to use
     :param local: whether to use a local file
     :param skip_first_line: whether to skip the first line of the file
     :return: None
@@ -119,77 +243,103 @@
         # #Keepers CLOCKSS serials 2022-12-19
         if skip_first_line:
             next(input_file)
 
         csv_reader = DictReader(input_file)
 
         for row in csv_reader:
-            publisher, created = \
-                Publisher.objects.get_or_create(name=row['Publisher'])
+            # trim the publisher field if needed
+            publisher_name = row["Publisher"][:254]
 
-            if model.name() == 'CLOCKSS' or model.name() == 'LOCKSS'\
-                    or model.name() == 'Cariniana':
+            publisher, created = Publisher.objects.get_or_create(
+                name=publisher_name
+            )
+
+            if (
+                model.name() == "CLOCKSS"
+                or model.name() == "LOCKSS"
+                or model.name() == "Cariniana"
+            ):
                 # create the item
                 model.create_preservation(
-                    issn=row['ISSN'], eissn=row['eISSN'], title=row['Title'],
-                    preserved_volumes=row['Preserved Volumes'],
-                    preserved_years=row['Preserved Years'],
-                    in_progress_volumes=row['In Progress Volumes'],
-                    in_progress_years=row['In Progress Years'],
-                    publisher=publisher, model=model
+                    issn=row["ISSN"],
+                    eissn=row["eISSN"],
+                    title=row["Title"],
+                    preserved_volumes=row["Preserved Volumes"],
+                    preserved_years=row["Preserved Years"],
+                    in_progress_volumes=row["In Progress Volumes"],
+                    in_progress_years=row["In Progress Years"],
+                    publisher=publisher,
+                    model=model,
                 )
-            elif model.name() == 'PKP PLN':
+            elif model.name() == "PKP PLN":
                 model.create_preservation(
-                    issn=row['ISSN'], title=row['Title'],
-                    preserved_volumes=row['Vol'],
-                    preserved_no=row['No'],
-                    publisher=publisher, model=model
+                    issn=row["ISSN"],
+                    title=row["Title"],
+                    preserved_volumes=row["Vol"],
+                    preserved_no=row["No"],
+                    publisher=publisher,
+                    model=model,
                 )
 
             logging.info(f'Added {row["Title"]} to {model.name()} data')
 
 
 def clear_out(model):
-    logging.info(f'Clearing previous {model.name()} data')
+    if hasattr(model, "name"):
+        logging.info(f"Clearing previous {model.name()} data")
     model.objects.all().delete()
 
 
-def download_remote(local, model, url, bucket="", s3client=None, decode=True,
-                    file=False, filename=''):
+def download_remote(
+    local,
+    model,
+    url,
+    bucket="",
+    s3client=None,
+    decode=True,
+    file=False,
+    filename="",
+):
     if s3client:
         if not file:
             if decode:
-                return s3client.get_object(Bucket=bucket, Key=url)[
-                    'Body'].read().decode('utf-8')
+                return (
+                    s3client.get_object(Bucket=bucket, Key=url)["Body"]
+                    .read()
+                    .decode("utf-8")
+                )
             else:
                 return s3client.get_object(Bucket=bucket, Key=url)[
-                    'Body'].read()
+                    "Body"
+                ].read()
         else:
-            logging.info('Storing downloaded file as {}'.format(filename))
+            logging.info("Storing downloaded file as {}".format(filename))
             s3client.download_file(bucket, url, filename)
             return filename
 
     if not local:
-        logging.info(f'Downloading: {model.name()} data')
+        logging.info(f"Downloading: {model.name()} data")
         csv_file = requests.get(url).text
     else:
-        logging.info(f'Using local file for {model.name()} data')
+        logging.info(f"Using local file for {model.name()} data")
 
         if decode:
-            with open(url, 'r') as f:
+            with open(url, "r") as f:
                 csv_file = f.read()
         else:
-            with open(url, 'rb') as f:
+            with open(url, "rb") as f:
                 csv_file = f.read()
 
     return csv_file
 
 
-def preservation_status(model, container_title, issn, volume,
-                        no=None) -> (dict | None, str):
+def preservation_status(
+    model, container_title, issn, volume, no=None, year=None
+) -> (dict | None, str):
     """
     Determine whether a DOI is preserved in model
     :param model: the model class to use
     :param container_title: the container title
     :param issn: the ISSN
     :param volume: the volume
     :param no: the issue number
@@ -198,24 +348,33 @@
     """
     preserved_item = get_preserved_item_record(model, container_title, issn)
 
     if not preserved_item or len(preserved_item) == 0:
         return None, False
 
     for pi in preserved_item:
-        vols = [x.strip() for x in pi.preserved_volumes.split(';')]
-        vols_in_prog = [x.strip() for x in pi.in_progress_volumes.split(';')]
+        vols = [x.strip() for x in pi.preserved_volumes.split(";")]
+        vols_in_prog = [x.strip() for x in pi.in_progress_volumes.split(";")]
 
         volume = str(volume)
 
         if volume in vols:
             return preserved_item, True
         elif volume in vols_in_prog:
             return preserved_item, False
 
+        if year:
+            years = [x.strip() for x in pi.preserved_years.split(";")]
+            years_in_prog = [x.strip() for x in pi.in_progress_years.split(";")]
+
+            if str(year) in years:
+                return preserved_item, True
+            elif str(year) in years_in_prog:
+                return preserved_item, False
+
     return None, False
 
 
 def get_preserved_item_record(model, container_title, issn) -> QuerySet | None:
     """
     Retrieves preservation records from the model
     :param model: the preservation model to use
@@ -223,33 +382,45 @@
     :param issn: a list of ISSNs
     :return: a queryset of preservation model records or None
     """
     fields = [f.name for f in model._meta.get_fields()]
 
     # test ISSN
     try:
-        if issn and 'issn' in fields:
-            preserved_item = model.objects.filter(issn=issn[0])
+        if issn and "issn" in fields:
+            preserved_item = None
+
+            for sub_issn in issn:
+                preserved_item = model.objects.filter(issn=sub_issn)
+                if len(preserved_item) > 0:
+                    break
+
             if not preserved_item or len(preserved_item) == 0:
                 raise model.DoesNotExist
         else:
             raise model.DoesNotExist
     except model.DoesNotExist:
         # test EISSN
         try:
-            if issn and 'eissn' in fields:
-                preserved_item = model.objects.filter(eissn=issn[0])
+            if issn and "eissn" in fields:
+                preserved_item = None
+
+                for sub_issn in issn:
+                    preserved_item = model.objects.filter(eissn=sub_issn)
+                    if len(preserved_item) > 0:
+                        break
+
                 if not preserved_item or len(preserved_item) == 0:
                     raise model.DoesNotExist
             else:
                 raise model.DoesNotExist
         except model.DoesNotExist:
             # test container title
             try:
-                if container_title and 'container_title' in fields:
+                if container_title and "container_title" in fields:
                     preserved_item = model.objects.filter(title=container_title)
                     if not preserved_item or len(preserved_item) == 0:
                         raise model.DoesNotExist
                 else:
                     raise model.DoesNotExist
             except model.DoesNotExist:
                 return None
@@ -257,108 +428,279 @@
     return preserved_item
 
 
 def process_onix(xml_file, elements, callback) -> None:
     """
     A faster method for processing ONIX XML than using DOM methods
     """
-    current_object = {'volumes': [], 'issues': []}
+    current_object = {"volumes": [], "issues": []}
 
     collect = False
 
-    for event, elem in ET.iterparse(xml_file, events=('start', 'end')):
+    count = 0
 
-        if event == 'end' and elem.tag == '{http://www.editeur.org/onix/' \
-                                          'serials/SOH}HoldingsRecord':
+    for event, elem in ET.iterparse(xml_file, events=("start", "end")):
+        if (
+            event == "end"
+            and elem.tag == "{http://www.editeur.org/onix/"
+            "serials/SOH}HoldingsRecord"
+        ):
             callback(current_object)
 
-            current_object = {'volumes': [], 'issues': []}
+            gc.collect()
+
+            current_object = {"volumes": [], "issues": []}
+
+            count = count + 1
+            stats = []
+
+            filters = [tracemalloc.Filter(inclusive=True, filename_pattern="*")]
+
+            if count % 100 == 0:
+                django.db.reset_queries()
+
+            # free memory (urgh)
+            # a note: without this, the elementree will simply grow in memory
+            # and previously iterated elements will not be garbage collected
+            elem.clear()
 
         # detect if it's an ISSN
-        if event == 'start' \
-                and elem.tag == '{http://www.editeur.org/onix/' \
-                                'serials/SOH}ResourceVersionIDType' \
-                and elem.text == '07':
+        if (
+            event == "start"
+            and elem.tag == "{http://www.editeur.org/onix/"
+            "serials/SOH}ResourceVersionIDType"
+            and elem.text == "07"
+        ):
             collect = True
-        elif event == 'start' \
-                and elem.tag == '{http://www.editeur.org/onix/' \
-                                'serials/SOH}ResourceVersionIDType' \
-                and elem.text != '07':
+        elif (
+            event == "start"
+            and elem.tag == "{http://www.editeur.org/onix/"
+            "serials/SOH}ResourceVersionIDType"
+            and elem.text != "07"
+        ):
             collect = False
 
-        if event == 'start' and elem.tag == '{http://www.editeur.org/onix/' \
-                                            'serials/SOH}IDValue' and collect:
-            current_object['issn'] = normalize_issn(elem.text)
-
-        if event == 'start' and elem.tag == '{http://www.editeur.org/onix/' \
-                                            'serials/SOH}TitleText' and collect:
-            current_object['title'] = elem.text
-
-        if event == 'start' \
-                and elem.tag == '{http://www.editeur.org/onix/' \
-                                'serials/SOH}PublisherName' \
-                and collect:
-            current_object['publisher'] = elem.text
-
-        if event == 'start' \
-                and elem.tag == '{http://www.editeur.org/onix/' \
-                                'serials/SOH}Coverage' and collect:
+        if (
+            event == "start"
+            and elem.tag == "{http://www.editeur.org/onix/"
+            "serials/SOH}IDValue"
+            and collect
+        ):
+            current_object["issn"] = normalize_issn(elem.text)
+
+        if (
+            event == "start"
+            and elem.tag == "{http://www.editeur.org/onix/"
+            "serials/SOH}TitleText"
+            and collect
+        ):
+            current_object["title"] = elem.text
+
+        if (
+            event == "start"
+            and elem.tag == "{http://www.editeur.org/onix/"
+            "serials/SOH}PublisherName"
+            and collect
+        ):
+            current_object["publisher"] = elem.text
+
+        if (
+            event == "start"
+            and elem.tag == "{http://www.editeur.org/onix/"
+            "serials/SOH}Coverage"
+            and collect
+        ):
             coverage = elem
 
-            volume = ''
-            issue = ''
+            volume = ""
+            issue = ""
 
             level_one = coverage.find(
-                ".//{http://www.editeur.org/onix/serials/SOH}Level1")
+                ".//{http://www.editeur.org/onix/serials/SOH}Level1"
+            )
             level_two = coverage.find(
-                ".//{http://www.editeur.org/onix/serials/SOH}Level2")
+                ".//{http://www.editeur.org/onix/serials/SOH}Level2"
+            )
 
             levels = [level_one, level_two]
             unit = None
 
             for level in levels:
                 if level:
                     unit = level.find(
-                        ".//{http://www.editeur.org/onix/serials/SOH}Unit")
+                        ".//{http://www.editeur.org/onix/serials/SOH}Unit"
+                    )
 
                     # no idea why, but this HAS to be an explicit comparison
                     # with None rather than a boolean comparison
                     unit = unit.text if unit is not None else None
 
                     number = level.find(
-                        ".//{http://www.editeur.org/onix/serials/SOH}Number")
+                        ".//{http://www.editeur.org/onix/serials/SOH}Number"
+                    )
 
                     number = number.text if number is not None else None
 
-                    if unit == 'Volume':
+                    if unit == "Volume":
                         volume = number
-                    elif unit == 'Issue':
+                    elif unit == "Issue":
                         issue = number
                     else:
-                        print('Unrecognised unit: {}'.format(unit))
+                        print("Unrecognised unit: {}".format(unit))
 
             if unit:
-                current_object['volumes'].append(volume)
-                current_object['issues'].append(issue)
+                current_object["volumes"].append(volume)
+                current_object["issues"].append(issue)
 
-        if event == 'start' \
-                and elem.tag == '{http://www.editeur.org/onix/' \
-                                'serials/SOH}PreservationStatusCode'\
-                and collect:
-            current_object['status'] = elem.text
-
-        if event == 'start' \
-                and elem.tag == '{http://www.editeur.org/onix/' \
-                                'serials/SOH}VerificationStatus'\
-                and collect:
-            current_object['verification'] = elem.text
+        if (
+            event == "start"
+            and elem.tag == "{http://www.editeur.org/onix/"
+            "serials/SOH}PreservationStatusCode"
+            and collect
+        ):
+            current_object["status"] = elem.text
+
+        if (
+            event == "start"
+            and elem.tag == "{http://www.editeur.org/onix/"
+            "serials/SOH}VerificationStatus"
+            and collect
+        ):
+            current_object["verification"] = elem.text
 
     return
 
 
 def normalize_issn(issn) -> str:
     """
     Normalizes an ISSN
     :param issn: the ISSN
     :return: the normalized ISSN
     """
-    return f'{issn[0:4]}-{issn[4:8]}' if '-' not in issn else issn
+    issn = "" if issn is None else issn.strip()
+
+    return f"{issn[0:4]}-{issn[4:8]}" if issn and "-" not in issn else issn
+
+
+@transaction.atomic
+def random_db_entries(model, count, only_crossref=False) -> list:
+    """
+    Returns random entries from a database model
+    :param model: the model to use
+    :param count: the number of random entries to return
+    :param only_crossref: whether to only return crossref entries
+    :return: a list of random entries
+    """
+
+    # NB we do it like this because queryset.order_by('?') can be incredibly
+    # slow
+    output = []
+
+    total = model.objects.all().count()
+
+    my_etiquette = Etiquette(
+        "Preservation Status", "0.01", "https://eve.gd", "meve@crossref.org"
+    )
+
+    jrnls = Journals(etiquette=my_etiquette)
+
+    while len(output) < count - 1:
+        random_index = randint(0, total - 1)
+
+        entry = model.objects.all()[random_index]
+
+        if only_crossref:
+            append = False
+
+            new_issns = expand_issns([entry.issn])
+
+            for issn in new_issns:
+                jrnl = jrnls.journal(issn=issn)
+
+                if jrnl:
+                    append = True
+                    break
+
+            if hasattr(entry, "eissn"):
+                new_eissns = expand_issns([entry.eissn])
+
+                for issn in new_eissns:
+                    jrnl = jrnls.journal(issn=issn)
+
+                    if jrnl:
+                        append = True
+                        break
+
+            if append:
+                output.append(entry)
+                print(
+                    "Found crossref entry ({}): {}".format(len(output), entry)
+                )
+        else:
+            output.append(entry)
+
+    return output
+
+
+def in_archive(item, archive) -> bool:
+    """
+    Determines whether a container is in an archive
+    :param item: the container to check
+    :param archive: the archive to check
+    :return: True if both items are in the same archive, False otherwise
+    """
+
+    fields = item._meta.fields
+
+    if "issn" in fields:
+        issns = archive.objects.filter(issn=item["issn"])
+
+        if len(issns) > 0:
+            return True
+
+    if "eissn" in fields:
+        try:
+            issns = archive.objects.filter(eissn=item["eissn"])
+
+            if len(issns) > 0:
+                return True
+        except:
+            issns = archive.objects.filter(issn=item["eissn"])
+
+            if len(issns) > 0:
+                return True
+
+    if "title" in fields:
+        titles = archive.objects.filter(title=item["title"])
+
+        if len(titles) > 0:
+            return True
+
+    return False
+
+
+def import_issnl(issnl_file, issnl_model, issn_model):
+    from rich.progress import track
+
+    csv.field_size_limit(sys.maxsize)
+
+    clear_out(issn_model)
+    clear_out(issnl_model)
+
+    logging.info("Erased existing ISSN-ISSNL mappings.")
+
+    with open(issnl_file, "r") as input_file:
+        csv_reader = csv.DictReader(input_file, delimiter="\t")
+
+        for row in track(csv_reader):
+            if row["ISSN"] != row["ISSN-L"]:
+                issnl, created = issnl_model.objects.get_or_create(
+                    identifier=row["ISSN-L"]
+                )
+
+                issn, created = issn_model.objects.get_or_create(
+                    identifier=row["ISSN"], issnl=issnl
+                )
+
+                logging.info(
+                    f"Created ISSN-ISSNL mapping: {issn.identifier} {issnl.identifier}"
+                )
```

### Comparing `preservation-database-0.0.9/pyproject.toml` & `preservation-database-0.0.90/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "preservation-database"
-version = "0.0.9"
+version = "0.0.90"
 description = "A database builder for digital preservation information."
 readme = "README.md"
 requires-python = ">=3.8"
 license = {file = "LICENSE.md"}
 keywords = ["digital preservation", "academic"]
 authors = [
   {email = "meve@crossref.org"},
@@ -27,15 +27,22 @@
     "crossrefapi",
     "django-macros",
     "gunicorn",
     "djangorestframework",
     "markdown",
     "django-filter",
     "apache-airflow",
-    "boto3"
+    "boto3",
+    "pytz",
+    "msgspec",
+    "humanfriendly",
+    "psycopg2-binary",
+    "lxml",
+    "joblib",
+    "case-converter"
 ]
 
 [project.urls]
 homepage = "https://labs.crossref.org"
 documentation = "https://labs.crossref.org"
 repository = "https://gitlab.com/crossref/labs/preservationDatabase"
 changelog = "https://gitlab.com/crossref/labs/preservation-data/-/blob/main/CHANGELOG.md"
```

### Comparing `preservation-database-0.0.9/setup.cfg` & `preservation-database-0.0.90/setup.cfg`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = preservation-database
-version = 0.0.9
+version = 0.0.90
 description = A database builder for digital preservation information.
 url = https://gitlab.com/crossref/labs/preservationDatabase
 author = Martin Paul Eve
 author_email = martin@eve.gd
 license = MIT
 classifiers = 
 	Environment :: Web Environment
@@ -36,12 +36,19 @@
 	django-macros
 	gunicorn
 	djangorestframework
 	markdown
 	django-filter
 	apache-airflow
 	boto3
+	pytz
+	msgspec
+	humanfriendly
+	psycopg2-binary
+	lxml
+	joblib
+	case-converter
 
 [egg_info]
 tag_build = 
 tag_date = 0
```

