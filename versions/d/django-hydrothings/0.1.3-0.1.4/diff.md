# Comparing `tmp/django-hydrothings-0.1.3.tar.gz` & `tmp/django-hydrothings-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-hydrothings-0.1.3.tar", last modified: Fri Mar 24 21:21:16 2023, max compression
+gzip compressed data, was "django-hydrothings-0.1.4.tar", last modified: Thu Apr  6 22:45:31 2023, max compression
```

## Comparing `django-hydrothings-0.1.3.tar` & `django-hydrothings-0.1.4.tar`

### file list

```diff
@@ -1,95 +1,96 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.416291 django-hydrothings-0.1.3/
--rw-r--r--   0 runner    (1001) docker     (123)     1094 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (123)      109 2023-03-24 21:21:16.416291 django-hydrothings-0.1.3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2145 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       80 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      403 2023-03-24 21:21:16.416291 django-hydrothings-0.1.3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       93 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.404290 django-hydrothings-0.1.3/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.408290 django-hydrothings-0.1.3/src/django_hydrothings.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      109 2023-03-24 21:21:16.000000 django-hydrothings-0.1.3/src/django_hydrothings.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3065 2023-03-24 21:21:16.000000 django-hydrothings-0.1.3/src/django_hydrothings.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 21:21:16.000000 django-hydrothings-0.1.3/src/django_hydrothings.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      142 2023-03-24 21:21:16.000000 django-hydrothings-0.1.3/src/django_hydrothings.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       12 2023-03-24 21:21:16.000000 django-hydrothings-0.1.3/src/django_hydrothings.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-24 21:21:16.000000 django-hydrothings-0.1.3/src/django_hydrothings.egg-info/zip-safe
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.408290 django-hydrothings-0.1.3/src/hydrothings/
--rw-r--r--   0 runner    (1001) docker     (123)      324 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.408290 django-hydrothings-0.1.3/src/hydrothings/backends/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.408290 django-hydrothings-0.1.3/src/hydrothings/backends/frostserver/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/frostserver/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/frostserver/apps.py
--rw-r--r--   0 runner    (1001) docker     (123)     1661 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/frostserver/engine.py
--rw-r--r--   0 runner    (1001) docker     (123)      297 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/frostserver/renderers.py
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/frostserver/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.412291 django-hydrothings-0.1.3/src/hydrothings/backends/odm2/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/odm2/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/odm2/apps.py
--rw-r--r--   0 runner    (1001) docker     (123)      979 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/odm2/engine.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/odm2/models.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/odm2/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)      170 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/odm2/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.412291 django-hydrothings-0.1.3/src/hydrothings/backends/sensorthings/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/sensorthings/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      176 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/sensorthings/apps.py
--rw-r--r--   0 runner    (1001) docker     (123)     8180 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/sensorthings/engine.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/sensorthings/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      320 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/backends/sensorthings/urls.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.412291 django-hydrothings-0.1.3/src/hydrothings/components/
--rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.412291 django-hydrothings-0.1.3/src/hydrothings/components/datastreams/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/datastreams/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3006 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/datastreams/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     4045 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/datastreams/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.412291 django-hydrothings-0.1.3/src/hydrothings/components/featuresofinterest/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/featuresofinterest/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1389 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/featuresofinterest/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     4550 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/featuresofinterest/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.412291 django-hydrothings-0.1.3/src/hydrothings/components/historicallocations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/historicallocations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1569 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/historicallocations/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     4603 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/historicallocations/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.412291 django-hydrothings-0.1.3/src/hydrothings/components/locations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/locations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1787 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/locations/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     3931 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/locations/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.412291 django-hydrothings-0.1.3/src/hydrothings/components/observations/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/observations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3637 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/observations/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     3441 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/observations/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     5482 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/observations/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.416291 django-hydrothings-0.1.3/src/hydrothings/components/observedproperties/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/observedproperties/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1192 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/observedproperties/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     4476 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/observedproperties/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.416291 django-hydrothings-0.1.3/src/hydrothings/components/root/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/root/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      466 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/root/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)      757 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/root/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.416291 django-hydrothings-0.1.3/src/hydrothings/components/sensors/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/sensors/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1494 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/sensors/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     1476 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/sensors/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     3776 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/sensors/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.416291 django-hydrothings-0.1.3/src/hydrothings/components/things/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/things/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1939 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/things/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     3783 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/components/things/views.py
--rw-r--r--   0 runner    (1001) docker     (123)     8656 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/engine.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.416291 django-hydrothings-0.1.3/src/hydrothings/extras/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/extras/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      940 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/extras/iso_types.py
--rw-r--r--   0 runner    (1001) docker     (123)     8068 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/main.py
--rw-r--r--   0 runner    (1001) docker     (123)     8369 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/middleware.py
--rw-r--r--   0 runner    (1001) docker     (123)     2003 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/schemas.py
--rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/settings.py
--rw-r--r--   0 runner    (1001) docker     (123)     5055 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     2726 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/src/hydrothings/validators.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-24 21:21:16.416291 django-hydrothings-0.1.3/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      849 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/tests/test_allow_partial_decorator.py
--rw-r--r--   0 runner    (1001) docker     (123)     1301 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/tests/test_iso_interval_type.py
--rw-r--r--   0 runner    (1001) docker     (123)      726 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/tests/test_iso_time_type.py
--rw-r--r--   0 runner    (1001) docker     (123)     1557 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/tests/test_metadata_field_validator.py
--rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/tests/test_resolve_chained_entity_url.py
--rw-r--r--   0 runner    (1001) docker     (123)     1188 2023-03-24 21:20:56.000000 django-hydrothings-0.1.3/tests/test_whitespace_validator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.244373 django-hydrothings-0.1.4/
+-rw-r--r--   0 runner    (1001) docker     (123)     1094 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      109 2023-04-06 22:45:31.244373 django-hydrothings-0.1.4/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2145 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       80 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      403 2023-04-06 22:45:31.244373 django-hydrothings-0.1.4/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       93 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.232373 django-hydrothings-0.1.4/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.236373 django-hydrothings-0.1.4/src/django_hydrothings.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      109 2023-04-06 22:45:31.000000 django-hydrothings-0.1.4/src/django_hydrothings.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3108 2023-04-06 22:45:31.000000 django-hydrothings-0.1.4/src/django_hydrothings.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 22:45:31.000000 django-hydrothings-0.1.4/src/django_hydrothings.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-04-06 22:45:31.000000 django-hydrothings-0.1.4/src/django_hydrothings.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       12 2023-04-06 22:45:31.000000 django-hydrothings-0.1.4/src/django_hydrothings.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 22:45:31.000000 django-hydrothings-0.1.4/src/django_hydrothings.egg-info/zip-safe
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.236373 django-hydrothings-0.1.4/src/hydrothings/
+-rw-r--r--   0 runner    (1001) docker     (123)      324 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.236373 django-hydrothings-0.1.4/src/hydrothings/backends/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.236373 django-hydrothings-0.1.4/src/hydrothings/backends/frostserver/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/frostserver/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/frostserver/apps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1661 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/frostserver/engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)      297 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/frostserver/renderers.py
+-rw-r--r--   0 runner    (1001) docker     (123)      352 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/frostserver/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.236373 django-hydrothings-0.1.4/src/hydrothings/backends/odm2/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/odm2/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/odm2/apps.py
+-rw-r--r--   0 runner    (1001) docker     (123)      979 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/odm2/engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/odm2/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/odm2/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)      170 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/odm2/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.236373 django-hydrothings-0.1.4/src/hydrothings/backends/sensorthings/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/sensorthings/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      176 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/sensorthings/apps.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8180 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/sensorthings/engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/sensorthings/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      320 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/backends/sensorthings/urls.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.236373 django-hydrothings-0.1.4/src/hydrothings/components/
+-rw-r--r--   0 runner    (1001) docker     (123)     1124 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/components/datastreams/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/datastreams/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3021 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/datastreams/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4045 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/datastreams/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/components/featuresofinterest/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/featuresofinterest/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1395 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/featuresofinterest/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4550 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/featuresofinterest/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/components/historicallocations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/historicallocations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1578 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/historicallocations/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4603 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/historicallocations/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/components/locations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/locations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1796 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/locations/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3931 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/locations/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/components/observations/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/observations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3652 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/observations/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3441 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/observations/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5482 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/observations/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/components/observedproperties/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/observedproperties/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1201 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/observedproperties/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4476 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/observedproperties/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/components/root/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/root/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      466 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/root/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)      757 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/root/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/components/sensors/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/sensors/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1500 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/sensors/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1476 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/sensors/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3776 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/sensors/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/components/things/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/things/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1951 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/things/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3783 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/components/things/views.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9277 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/engine.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/src/hydrothings/extras/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/extras/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      940 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/extras/iso_types.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8068 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/main.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8369 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/middleware.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2012 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/schemas.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2104 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/settings.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5055 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2726 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/src/hydrothings/validators.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 22:45:31.240373 django-hydrothings-0.1.4/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      849 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/tests/test_allow_partial_decorator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1301 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/tests/test_iso_interval_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)      726 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/tests/test_iso_time_type.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1557 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/tests/test_metadata_field_validator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/tests/test_resolve_chained_entity_url.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4473 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/tests/test_sensorthings_abstract_engine.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1188 2023-04-06 22:45:16.000000 django-hydrothings-0.1.4/tests/test_whitespace_validator.py
```

### Comparing `django-hydrothings-0.1.3/LICENSE.txt` & `django-hydrothings-0.1.4/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/README.md` & `django-hydrothings-0.1.4/README.md`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/django_hydrothings.egg-info/SOURCES.txt` & `django-hydrothings-0.1.4/src/django_hydrothings.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -67,8 +67,9 @@
 src/hydrothings/extras/__init__.py
 src/hydrothings/extras/iso_types.py
 tests/test_allow_partial_decorator.py
 tests/test_iso_interval_type.py
 tests/test_iso_time_type.py
 tests/test_metadata_field_validator.py
 tests/test_resolve_chained_entity_url.py
+tests/test_sensorthings_abstract_engine.py
 tests/test_whitespace_validator.py
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/backends/frostserver/engine.py` & `django-hydrothings-0.1.4/src/hydrothings/backends/frostserver/engine.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/backends/odm2/engine.py` & `django-hydrothings-0.1.4/src/hydrothings/backends/odm2/engine.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/backends/sensorthings/engine.py` & `django-hydrothings-0.1.4/src/hydrothings/backends/sensorthings/engine.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/__init__.py` & `django-hydrothings-0.1.4/src/hydrothings/components/__init__.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/datastreams/schemas.py` & `django-hydrothings-0.1.4/src/hydrothings/components/datastreams/schemas.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from typing import TYPE_CHECKING, Literal, List, Union
-from pydantic import Field, HttpUrl
+from pydantic import Field, AnyHttpUrl
 from ninja import Schema
 from hydrothings.schemas import BaseListResponse, BaseGetResponse, BasePostBody, BasePatchBody, EntityId, NestedEntity
 from hydrothings.validators import allow_partial
 from hydrothings.extras.iso_types import ISOTime, ISOInterval
 
 if TYPE_CHECKING:
     from hydrothings.components.things.schemas import Thing
@@ -19,15 +19,15 @@
     'http://www.opengis.net/def/observationType/OGC-OM/2.0/OM_TruthObservation'
 ]
 
 
 class UnitOfMeasurement(Schema):
     name: str
     symbol: str
-    definition: HttpUrl
+    definition: AnyHttpUrl
 
 
 # TODO Add validation for temporal duration types.
 class DatastreamFields(Schema):
     name: str
     description: str
     unit_of_measurement: UnitOfMeasurement = Field(..., alias='unitOfMeasurement')
@@ -65,14 +65,14 @@
 class DatastreamPatchBody(BasePatchBody, DatastreamFields):
     thing: EntityId = Field(..., alias='Thing')
     sensor: EntityId = Field(..., alias='Sensor')
     observed_property: EntityId = Field(..., alias='ObservedProperty')
 
 
 class DatastreamGetResponse(BaseGetResponse, DatastreamFields):
-    thing_link: HttpUrl = Field(..., alias='Thing@iot.navigationLink')
-    sensor_link: HttpUrl = Field(..., alias='Sensor@iot.navigationLink')
-    observed_property_link: HttpUrl = Field(..., alias='ObservedProperty@iot.navigationLink')
+    thing_link: AnyHttpUrl = Field(..., alias='Thing@iot.navigationLink')
+    sensor_link: AnyHttpUrl = Field(..., alias='Sensor@iot.navigationLink')
+    observed_property_link: AnyHttpUrl = Field(..., alias='ObservedProperty@iot.navigationLink')
 
 
 class DatastreamListResponse(BaseListResponse):
     value: List[DatastreamGetResponse]
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/datastreams/views.py` & `django-hydrothings-0.1.4/src/hydrothings/components/datastreams/views.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/featuresofinterest/schemas.py` & `django-hydrothings-0.1.4/src/hydrothings/components/featuresofinterest/schemas.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from typing import TYPE_CHECKING, Literal, List
-from pydantic import Field, HttpUrl
+from pydantic import Field, AnyHttpUrl
 from geojson_pydantic import Feature
 from ninja import Schema
 from hydrothings.schemas import BaseListResponse, BaseGetResponse, BasePostBody, BasePatchBody, NestedEntity
 from hydrothings.validators import allow_partial
 
 if TYPE_CHECKING:
     from hydrothings.components.observations.schemas import Observation
@@ -36,12 +36,12 @@
 
 @allow_partial
 class FeatureOfInterestPatchBody(FeatureOfInterestFields, BasePatchBody):
     pass
 
 
 class FeatureOfInterestGetResponse(BaseGetResponse, FeatureOfInterestFields):
-    observations_link: HttpUrl = Field(..., alias='Observations@iot.navigationLink')
+    observations_link: AnyHttpUrl = Field(..., alias='Observations@iot.navigationLink')
 
 
 class FeatureOfInterestListResponse(BaseListResponse):
     value: List[FeatureOfInterestGetResponse]
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/featuresofinterest/views.py` & `django-hydrothings-0.1.4/src/hydrothings/components/featuresofinterest/views.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/historicallocations/schemas.py` & `django-hydrothings-0.1.4/src/hydrothings/components/historicallocations/schemas.py`

 * *Files 5% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 from typing import TYPE_CHECKING, List, Union
 from datetime import datetime
-from pydantic import Field, HttpUrl
+from pydantic import Field, AnyHttpUrl
 from ninja import Schema
 from hydrothings.schemas import BaseListResponse, BaseGetResponse, BasePostBody, BasePatchBody, EntityId, NestedEntity
 from hydrothings.validators import allow_partial
 
 if TYPE_CHECKING:
     from hydrothings.components.things.schemas import Thing
     from hydrothings.components.locations.schemas import Location
@@ -35,13 +35,13 @@
 @allow_partial
 class HistoricalLocationPatchBody(HistoricalLocationFields, BasePatchBody):
     thing: EntityId = Field(..., alias='Thing')
     locations: List[EntityId] = Field(..., alias='Locations')
 
 
 class HistoricalLocationGetResponse(BaseGetResponse, HistoricalLocationFields):
-    thing_link: HttpUrl = Field(..., alias='Thing@iot.navigationLink')
-    historical_locations_link: HttpUrl = Field(..., alias='Locations@iot.navigationLink')
+    thing_link: AnyHttpUrl = Field(..., alias='Thing@iot.navigationLink')
+    historical_locations_link: AnyHttpUrl = Field(..., alias='Locations@iot.navigationLink')
 
 
 class HistoricalLocationListResponse(BaseListResponse):
     value: List[HistoricalLocationGetResponse]
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/historicallocations/views.py` & `django-hydrothings-0.1.4/src/hydrothings/components/historicallocations/views.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/locations/schemas.py` & `django-hydrothings-0.1.4/src/hydrothings/components/locations/schemas.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from typing import TYPE_CHECKING, Literal, List, Union
-from pydantic import Field, HttpUrl
+from pydantic import Field, AnyHttpUrl
 from geojson_pydantic import Feature
 from ninja import Schema
 from hydrothings.schemas import BaseListResponse, BaseGetResponse, BasePostBody, BasePatchBody, EntityId, NestedEntity
 from hydrothings.validators import allow_partial
 
 if TYPE_CHECKING:
     from hydrothings.components.things.schemas import Thing
@@ -42,13 +42,13 @@
 @allow_partial
 class LocationPatchBody(LocationFields, BasePatchBody):
     things: List[EntityId] = Field([], alias='Things')
     historical_locations: List[EntityId] = Field([], alias='HistoricalLocations')
 
 
 class LocationGetResponse(BaseGetResponse, LocationFields):
-    things_link: HttpUrl = Field(..., alias='Things@iot.navigationLink')
-    historical_locations_link: HttpUrl = Field(..., alias='HistoricalLocations@iot.navigationLink')
+    things_link: AnyHttpUrl = Field(..., alias='Things@iot.navigationLink')
+    historical_locations_link: AnyHttpUrl = Field(..., alias='HistoricalLocations@iot.navigationLink')
 
 
 class LocationListResponse(BaseListResponse):
     value: List[LocationGetResponse]
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/locations/views.py` & `django-hydrothings-0.1.4/src/hydrothings/components/locations/views.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/observations/schemas.py` & `django-hydrothings-0.1.4/src/hydrothings/components/observations/schemas.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from typing import TYPE_CHECKING, Literal, Union, List
-from pydantic import Field, HttpUrl
+from pydantic import Field, AnyHttpUrl
 from ninja import Schema
 from hydrothings.schemas import BaseListResponse, BaseGetResponse, BasePostBody, BasePatchBody, EntityId, \
     NestedEntity, QueryParams
 from hydrothings.extras.iso_types import ISOTime, ISOInterval
 from hydrothings.validators import allow_partial
 
 if TYPE_CHECKING:
@@ -26,15 +26,15 @@
 
 observationResultFormats = Literal['dataArray']
 
 
 class UnitOfMeasurement(Schema):
     name: str
     symbol: str
-    definition: HttpUrl
+    definition: AnyHttpUrl
 
 
 class ObservationFields(Schema):
     phenomenon_time: Union[ISOTime, ISOInterval, None] = Field(None, alias='phenomenonTime')
     result: str
     result_time: Union[ISOTime, None] = Field(..., alias='resultTime')
     result_quality: Union[str, None] = Field(None, alias='resultQuality')
@@ -48,15 +48,15 @@
 
 
 class Observation(ObservationFields, ObservationRelations):
     pass
 
 
 class ObservationDataArray(Schema):
-    datastream: HttpUrl = Field(..., alias='Datastream@iot.navigationLink')
+    datastream: AnyHttpUrl = Field(..., alias='Datastream@iot.navigationLink')
     components: List[observationComponents]
     data_array: List[list] = Field(..., alias='dataArray')
 
     class Config:
         allow_population_by_field_name = True
 
 
@@ -78,16 +78,16 @@
 @allow_partial
 class ObservationPatchBody(BasePatchBody, ObservationFields):
     datastream: EntityId = Field(..., alias='Datastream')
     feature_of_interest: EntityId = Field(..., alias='FeatureOfInterest')
 
 
 class ObservationGetResponse(ObservationFields, BaseGetResponse):
-    datastream_link: HttpUrl = Field(..., alias='Datastream@iot.navigationLink')
-    feature_of_interest_link: HttpUrl = Field(..., alias='FeatureOfInterest@iot.navigationLink')
+    datastream_link: AnyHttpUrl = Field(..., alias='Datastream@iot.navigationLink')
+    feature_of_interest_link: AnyHttpUrl = Field(..., alias='FeatureOfInterest@iot.navigationLink')
 
     class Config:
         allow_population_by_field_name = True
 
 
 class ObservationListResponse(BaseListResponse):
     value: List[ObservationGetResponse]
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/observations/utils.py` & `django-hydrothings-0.1.4/src/hydrothings/components/observations/utils.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/observations/views.py` & `django-hydrothings-0.1.4/src/hydrothings/components/observations/views.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/observedproperties/schemas.py` & `django-hydrothings-0.1.4/src/hydrothings/components/observedproperties/schemas.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,20 +1,20 @@
 from typing import TYPE_CHECKING, List
-from pydantic import Field, HttpUrl
+from pydantic import Field, AnyHttpUrl
 from ninja import Schema
 from hydrothings.schemas import BaseListResponse, BaseGetResponse, BasePostBody, BasePatchBody, NestedEntity
 from hydrothings.validators import allow_partial
 
 if TYPE_CHECKING:
     from hydrothings.components.datastreams.schemas import Datastream
 
 
 class ObservedPropertyFields(Schema):
     name: str
-    definition: HttpUrl
+    definition: AnyHttpUrl
     description: str
     properties: dict = {}
 
 
 class ObservedPropertyRelations(Schema):
     datastreams: List['Datastream'] = []
 
@@ -31,12 +31,12 @@
 
 @allow_partial
 class ObservedPropertyPatchBody(BasePatchBody, ObservedPropertyFields):
     pass
 
 
 class ObservedPropertyGetResponse(ObservedPropertyFields, BaseGetResponse):
-    datastreams_link: HttpUrl = Field(..., alias='Datastreams@iot.navigationLink')
+    datastreams_link: AnyHttpUrl = Field(..., alias='Datastreams@iot.navigationLink')
 
 
 class ObservedPropertyListResponse(BaseListResponse):
     value: List[ObservedPropertyGetResponse]
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/observedproperties/views.py` & `django-hydrothings-0.1.4/src/hydrothings/components/observedproperties/views.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/root/views.py` & `django-hydrothings-0.1.4/src/hydrothings/components/root/views.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/sensors/schemas.py` & `django-hydrothings-0.1.4/src/hydrothings/components/sensors/schemas.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from typing import TYPE_CHECKING, Literal, List
-from pydantic import Field, HttpUrl, validator
+from pydantic import Field, AnyHttpUrl, validator
 from ninja import Schema
 from hydrothings.schemas import BaseListResponse, BaseGetResponse, BasePostBody, BasePatchBody, NestedEntity
 from hydrothings.validators import allow_partial
 from hydrothings.components.sensors.utils import metadata_validator
 
 if TYPE_CHECKING:
     from hydrothings.components.datastreams.schemas import Datastream
@@ -42,12 +42,12 @@
 
 @allow_partial
 class SensorPatchBody(BasePatchBody, SensorFields):
     pass
 
 
 class SensorGetResponse(SensorFields, BaseGetResponse):
-    datastreams_link: HttpUrl = Field(..., alias='Datastreams@iot.navigationLink')
+    datastreams_link: AnyHttpUrl = Field(..., alias='Datastreams@iot.navigationLink')
 
 
 class SensorListResponse(BaseListResponse):
     value: List[SensorGetResponse]
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/sensors/utils.py` & `django-hydrothings-0.1.4/src/hydrothings/components/sensors/utils.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/sensors/views.py` & `django-hydrothings-0.1.4/src/hydrothings/components/sensors/views.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/things/schemas.py` & `django-hydrothings-0.1.4/src/hydrothings/components/things/schemas.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from typing import TYPE_CHECKING, Union, List
-from pydantic import Field, HttpUrl
+from pydantic import Field, AnyHttpUrl
 from ninja import Schema
 from hydrothings.schemas import BaseListResponse, BaseGetResponse, BasePostBody, BasePatchBody, EntityId, NestedEntity
 from hydrothings.validators import allow_partial
 
 if TYPE_CHECKING:
     from hydrothings.components.locations.schemas import Location
     from hydrothings.components.historicallocations.schemas import HistoricalLocation
@@ -43,17 +43,17 @@
 
 @allow_partial
 class ThingPatchBody(BasePatchBody, ThingFields):
     locations: List[EntityId] = Field([], alias='Locations')
 
 
 class ThingGetResponse(ThingFields, BaseGetResponse):
-    locations_link: HttpUrl = Field(..., alias='Locations@iot.navigationLink')
-    historical_locations_link: HttpUrl = Field(..., alias='HistoricalLocations@iot.navigationLink')
-    datastreams_link: HttpUrl = Field(..., alias='Datastreams@iot.navigationLink')
+    locations_link: AnyHttpUrl = Field(..., alias='Locations@iot.navigationLink')
+    historical_locations_link: AnyHttpUrl = Field(..., alias='HistoricalLocations@iot.navigationLink')
+    datastreams_link: AnyHttpUrl = Field(..., alias='Datastreams@iot.navigationLink')
 
 
 class ThingListResponse(BaseListResponse):
     value: List[ThingGetResponse]
 
 
 class ThingGetResponseODM(ThingGetResponse):
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/components/things/views.py` & `django-hydrothings-0.1.4/src/hydrothings/components/things/views.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/engine.py` & `django-hydrothings-0.1.4/src/hydrothings/engine.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from abc import ABCMeta, abstractmethod
 from uuid import UUID
 from pydantic.fields import SHAPE_LIST
-from typing import Union, Tuple, List
+from typing import Union, Tuple, List, Optional
 from django.http import HttpRequest
 from hydrothings import components as component_schemas
 from hydrothings import settings
 from hydrothings.schemas import BasePostBody, BasePatchBody
 
 
 class SensorThingsAbstractEngine(metaclass=ABCMeta):
@@ -117,14 +117,33 @@
         return dict(
             entity,
             **{
                 'self_link': self.get_ref(entity['id'] if is_collection is True else None)
             }
         )
 
+    def build_next_link(self, top: int, skip: int) -> str:
+        """
+        Creates SensorThings next link for paginated responses.
+
+        Parameters
+        ----------
+        top : int
+            An integer representing how many records are returned in the response.
+        skip : int
+            An integer representing how many records are skipped in the response.
+
+        Returns
+        -------
+        str
+            A URL that links to the next dataset following the subset of data in the current response.
+        """
+
+        return f'{self.get_ref()}?$top={top}&$skip={top+skip}'
+
     @abstractmethod
     def resolve_entity_id_chain(self, entity_chain: List[Tuple[str, Union[UUID, int, str]]]) -> bool:
         """
         Abstract method for resolving an entity chain passed to the API.
 
         SensorThings supports nested references to entities in URL paths. The Django HydroThings middleware will check
         the nested components to ensure each one is related to its parent and build a list of IDs that need to be
@@ -188,15 +207,15 @@
 
         pass
 
     @abstractmethod
     def get(
             self,
             entity_id: str
-    ) -> dict:
+    ) -> Optional[dict]:
         """
         Abstract method for handling GET entity requests.
 
         This method should return a dictionary representing an entity with the given entity ID.
 
         Parameters
         ----------
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/extras/iso_types.py` & `django-hydrothings-0.1.4/src/hydrothings/extras/iso_types.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/main.py` & `django-hydrothings-0.1.4/src/hydrothings/main.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/middleware.py` & `django-hydrothings-0.1.4/src/hydrothings/middleware.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/schemas.py` & `django-hydrothings-0.1.4/src/hydrothings/schemas.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 from uuid import UUID
-from pydantic import Field, Extra, HttpUrl, validator
+from pydantic import Field, Extra, AnyHttpUrl, validator
 from typing import Union
 from ninja import Schema
 from hydrothings.validators import nested_entities_check, whitespace_to_none
 
 
 class EntityId(Schema):
     id: UUID = Field(..., alias='@iot.id')
@@ -59,23 +59,23 @@
         extra = Extra.forbid
         allow_population_by_field_name = True
 
 
 class BaseListResponse(Schema):
     count: Union[int, None] = Field(None, alias='@iot.count')
     value: list = []
-    next_link: Union[HttpUrl, None] = Field(None, alias='@iot.nextLink')
+    next_link: Union[AnyHttpUrl, None] = Field(None, alias='@iot.nextLink')
 
     class Config:
         allow_population_by_field_name = True
 
 
 class BaseGetResponse(Schema):
     id: UUID = Field(..., alias='@iot.id')
-    self_link: HttpUrl = Field(..., alias='@iot.selfLink')
+    self_link: AnyHttpUrl = Field(..., alias='@iot.selfLink')
 
     class Config:
         allow_population_by_field_name = True
 
 
 class QueryParams(Schema):
     filters: str = Field(None, alias='$filter')
```

### Comparing `django-hydrothings-0.1.3/src/hydrothings/settings.py` & `django-hydrothings-0.1.4/src/hydrothings/settings.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/utils.py` & `django-hydrothings-0.1.4/src/hydrothings/utils.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/src/hydrothings/validators.py` & `django-hydrothings-0.1.4/src/hydrothings/validators.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/tests/test_allow_partial_decorator.py` & `django-hydrothings-0.1.4/tests/test_allow_partial_decorator.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/tests/test_iso_interval_type.py` & `django-hydrothings-0.1.4/tests/test_iso_interval_type.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/tests/test_iso_time_type.py` & `django-hydrothings-0.1.4/tests/test_iso_time_type.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/tests/test_metadata_field_validator.py` & `django-hydrothings-0.1.4/tests/test_metadata_field_validator.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/tests/test_resolve_chained_entity_url.py` & `django-hydrothings-0.1.4/tests/test_resolve_chained_entity_url.py`

 * *Files identical despite different names*

### Comparing `django-hydrothings-0.1.3/tests/test_whitespace_validator.py` & `django-hydrothings-0.1.4/tests/test_whitespace_validator.py`

 * *Files identical despite different names*

