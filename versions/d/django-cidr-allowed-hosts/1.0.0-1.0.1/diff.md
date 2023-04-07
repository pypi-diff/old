# Comparing `tmp/django-cidr-allowed-hosts-1.0.0.tar.gz` & `tmp/django-cidr-allowed-hosts-1.0.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-cidr-allowed-hosts-1.0.0.tar", last modified: Fri Apr  7 10:58:13 2023, max compression
+gzip compressed data, was "django-cidr-allowed-hosts-1.0.1.tar", last modified: Fri Apr  7 11:48:47 2023, max compression
```

## Comparing `django-cidr-allowed-hosts-1.0.0.tar` & `django-cidr-allowed-hosts-1.0.1.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 10:58:13.595482 django-cidr-allowed-hosts-1.0.0/
--rw-r--r--   0 bwozniak   (501) staff       (20)     1211 2023-04-07 10:22:22.000000 django-cidr-allowed-hosts-1.0.0/LICENSE
--rw-r--r--   0 bwozniak   (501) staff       (20)      295 2023-04-07 10:58:13.595315 django-cidr-allowed-hosts-1.0.0/PKG-INFO
--rw-r--r--   0 bwozniak   (501) staff       (20)     1324 2023-04-07 10:53:46.000000 django-cidr-allowed-hosts-1.0.0/README.md
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 10:58:13.594088 django-cidr-allowed-hosts-1.0.0/cidr/
--rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:32:59.000000 django-cidr-allowed-hosts-1.0.0/cidr/__init__.py
--rw-r--r--   0 bwozniak   (501) staff       (20)       83 2023-04-06 20:49:57.000000 django-cidr-allowed-hosts-1.0.0/cidr/apps.py
--rw-r--r--   0 bwozniak   (501) staff       (20)     2753 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.0/cidr/middleware.py
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 10:58:13.594668 django-cidr-allowed-hosts-1.0.0/django_cidr_allowed_hosts.egg-info/
--rw-r--r--   0 bwozniak   (501) staff       (20)      295 2023-04-07 10:58:13.000000 django-cidr-allowed-hosts-1.0.0/django_cidr_allowed_hosts.egg-info/PKG-INFO
--rw-r--r--   0 bwozniak   (501) staff       (20)      380 2023-04-07 10:58:13.000000 django-cidr-allowed-hosts-1.0.0/django_cidr_allowed_hosts.egg-info/SOURCES.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)        1 2023-04-07 10:58:13.000000 django-cidr-allowed-hosts-1.0.0/django_cidr_allowed_hosts.egg-info/dependency_links.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)       12 2023-04-07 10:58:13.000000 django-cidr-allowed-hosts-1.0.0/django_cidr_allowed_hosts.egg-info/requires.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)       11 2023-04-07 10:58:13.000000 django-cidr-allowed-hosts-1.0.0/django_cidr_allowed_hosts.egg-info/top_level.txt
--rw-r--r--   0 bwozniak   (501) staff       (20)       38 2023-04-07 10:58:13.595538 django-cidr-allowed-hosts-1.0.0/setup.cfg
--rw-r--r--   0 bwozniak   (501) staff       (20)      421 2023-04-07 10:56:22.000000 django-cidr-allowed-hosts-1.0.0/setup.py
-drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 10:58:13.595036 django-cidr-allowed-hosts-1.0.0/tests/
--rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:29:46.000000 django-cidr-allowed-hosts-1.0.0/tests/__init__.py
--rw-r--r--   0 bwozniak   (501) staff       (20)      189 2023-04-06 20:42:12.000000 django-cidr-allowed-hosts-1.0.0/tests/settings.py
--rw-r--r--   0 bwozniak   (501) staff       (20)     4461 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.0/tests/test_middleware.py
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 11:48:47.987681 django-cidr-allowed-hosts-1.0.1/
+-rw-r--r--   0 bwozniak   (501) staff       (20)     1211 2023-04-07 10:22:22.000000 django-cidr-allowed-hosts-1.0.1/LICENSE
+-rw-r--r--   0 bwozniak   (501) staff       (20)     2402 2023-04-07 11:48:47.987559 django-cidr-allowed-hosts-1.0.1/PKG-INFO
+-rw-r--r--   0 bwozniak   (501) staff       (20)     1470 2023-04-07 11:44:43.000000 django-cidr-allowed-hosts-1.0.1/README.rst
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 11:48:47.986180 django-cidr-allowed-hosts-1.0.1/cidr/
+-rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:32:59.000000 django-cidr-allowed-hosts-1.0.1/cidr/__init__.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)       83 2023-04-06 20:49:57.000000 django-cidr-allowed-hosts-1.0.1/cidr/apps.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)     2753 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.1/cidr/middleware.py
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 11:48:47.986967 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/
+-rw-r--r--   0 bwozniak   (501) staff       (20)     2402 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/PKG-INFO
+-rw-r--r--   0 bwozniak   (501) staff       (20)      381 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/SOURCES.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)        1 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/dependency_links.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)       12 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/requires.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)       11 2023-04-07 11:48:47.000000 django-cidr-allowed-hosts-1.0.1/django_cidr_allowed_hosts.egg-info/top_level.txt
+-rw-r--r--   0 bwozniak   (501) staff       (20)       38 2023-04-07 11:48:47.987725 django-cidr-allowed-hosts-1.0.1/setup.cfg
+-rw-r--r--   0 bwozniak   (501) staff       (20)     1116 2023-04-07 11:48:28.000000 django-cidr-allowed-hosts-1.0.1/setup.py
+drwxr-xr-x   0 bwozniak   (501) staff       (20)        0 2023-04-07 11:48:47.987374 django-cidr-allowed-hosts-1.0.1/tests/
+-rw-r--r--   0 bwozniak   (501) staff       (20)        0 2023-04-06 19:29:46.000000 django-cidr-allowed-hosts-1.0.1/tests/__init__.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)      189 2023-04-06 20:42:12.000000 django-cidr-allowed-hosts-1.0.1/tests/settings.py
+-rw-r--r--   0 bwozniak   (501) staff       (20)     4461 2023-04-07 09:24:34.000000 django-cidr-allowed-hosts-1.0.1/tests/test_middleware.py
```

### Comparing `django-cidr-allowed-hosts-1.0.0/LICENSE` & `django-cidr-allowed-hosts-1.0.1/LICENSE`

 * *Files identical despite different names*

### Comparing `django-cidr-allowed-hosts-1.0.0/README.md` & `django-cidr-allowed-hosts-1.0.1/README.rst`

 * *Files 26% similar despite different names*

```diff
@@ -1,46 +1,63 @@
-# Django CIDR Allowed Hosts
+Django CIDR Allowed Hosts
+=========================
 
-A Django middleware that allows you to specify a list of allowed hosts using CIDR notation.
+A Django middleware that allows you to specify a list of allowed hosts
+using CIDR notation.
 
-## Installation
+Installation
+------------
 
 Install using pip:
-```
-pip install django-cidr-allowed-hosts
-```
-
-Add the middleware at the top of your `MIDDLEWARE` settings:
-```python
-MIDDLEWARE = [
-    'cidr.middleware.CIDRMiddleware',
-    ...
-]
-```
-
-Add the `CIDR_ALLOWED_HOSTS` setting to your settings:
-```python
-CIDR_ALLOWED_HOSTS = ["0.0.0.0/0"] # allows any IPv4
-```
+
+::
+
+   pip install django-cidr-allowed-hosts
+
+Add the middleware at the top of your ``MIDDLEWARE`` settings:
+
+.. code:: python
+
+   MIDDLEWARE = [
+       'cidr.middleware.CIDRMiddleware',
+       ...
+   ]
+
+Add the ``CIDR_ALLOWED_HOSTS`` setting to your settings:
+
+.. code:: python
+
+   CIDR_ALLOWED_HOSTS = ["0.0.0.0/0"] # allows any IPv4
 
 And that should be it.
 
-## Features
+Features
+--------
 
-- `ALLOWED_HOSTS` will still work as expected. Since the middleware overrides the `ALLOWED_HOSTS` setting to `"*"`, the value provided originally to `ALLOWED_HOSTS` will be stored in `ORIGINAL_ALLOWED_HOSTS` and used to check if the request should be allowed.
-- If `CIDR_ALLOWED_HOSTS` is not set, the middleware will not be used.
-- If `ALLOWED_HOSTS` contains `"*"` and `CIDR_ALLOWED_HOSTS` is set, the middleware will raise `MiddlewareNotUsed` exception.
-- `CIDR_ALLOWED_HOSTS` must follow the [CIDR notation](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).
-- Only IPv4 is supported.
-
-## Development
-
-```
-python3 -m virtualenv venv
-source venv/bin/activate
-pip3 install tox
-tox
-```
+-  ``ALLOWED_HOSTS`` will still work as expected. Since the middleware
+   overrides the ``ALLOWED_HOSTS`` setting to ``"*"``, the value
+   provided originally to ``ALLOWED_HOSTS`` will be stored in
+   ``ORIGINAL_ALLOWED_HOSTS`` and used to check if the request should be
+   allowed.
+-  If ``CIDR_ALLOWED_HOSTS`` is not set, the middleware will not be
+   used.
+-  If ``ALLOWED_HOSTS`` contains ``"*"`` and ``CIDR_ALLOWED_HOSTS`` is
+   set, the middleware will raise ``MiddlewareNotUsed`` exception.
+-  ``CIDR_ALLOWED_HOSTS`` must follow the `CIDR
+   notation <https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation>`__.
+-  Only IPv4 is supported.
+
+Development
+-----------
+
+::
+
+   python3 -m virtualenv venv
+   source venv/bin/activate
+   pip3 install tox
+   tox
 
-## Credits
+Credits
+-------
 
-This project was inspired by [django-allow-cidr](https://github.com/mozmeao/django-allow-cidr)
+This project was inspired by
+`django-allow-cidr <https://github.com/mozmeao/django-allow-cidr>`__
```

### Comparing `django-cidr-allowed-hosts-1.0.0/cidr/middleware.py` & `django-cidr-allowed-hosts-1.0.1/cidr/middleware.py`

 * *Files identical despite different names*

### Comparing `django-cidr-allowed-hosts-1.0.0/tests/test_middleware.py` & `django-cidr-allowed-hosts-1.0.1/tests/test_middleware.py`

 * *Files identical despite different names*

