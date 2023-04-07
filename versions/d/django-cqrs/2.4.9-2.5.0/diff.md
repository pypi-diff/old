# Comparing `tmp/django-cqrs-2.4.9.tar.gz` & `tmp/django_cqrs-2.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-cqrs-2.4.9.tar", last modified: Mon Jan 30 14:16:33 2023, max compression
+gzip compressed data, was "django_cqrs-2.5.0.tar", max compression
```

## Comparing `django-cqrs-2.4.9.tar` & `django_cqrs-2.5.0.tar`

### file list

```diff
@@ -1,60 +1,42 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/
--rw-r--r--   0 runner    (1001) docker     (123)    11369 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      352 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)    12101 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     9058 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/dj_cqrs/
--rw-r--r--   0 runner    (1001) docker     (123)      196 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7567 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/_validation.py
--rw-r--r--   0 runner    (1001) docker     (123)     1735 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/admin.py
--rw-r--r--   0 runner    (1001) docker     (123)      289 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/apps.py
--rw-r--r--   0 runner    (1001) docker     (123)      728 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/constants.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/dj_cqrs/controller/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/controller/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2847 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/controller/consumer.py
--rw-r--r--   0 runner    (1001) docker     (123)      285 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/controller/producer.py
--rw-r--r--   0 runner    (1001) docker     (123)      698 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/correlation.py
--rw-r--r--   0 runner    (1001) docker     (123)     4986 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/dataclasses.py
--rw-r--r--   0 runner    (1001) docker     (123)     2229 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/delay.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/dj_cqrs/management/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/dj_cqrs/management/commands/
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4084 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_bulk_dump.py
--rw-r--r--   0 runner    (1001) docker     (123)     3564 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_bulk_load.py
--rw-r--r--   0 runner    (1001) docker     (123)     5370 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_consume.py
--rw-r--r--   0 runner    (1001) docker     (123)     5149 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_dead_letters.py
--rw-r--r--   0 runner    (1001) docker     (123)     1545 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_deleted_diff_master.py
--rw-r--r--   0 runner    (1001) docker     (123)     2397 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_deleted_diff_replica.py
--rw-r--r--   0 runner    (1001) docker     (123)     1178 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_deleted_sync_replica.py
--rw-r--r--   0 runner    (1001) docker     (123)     2502 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_diff_master.py
--rw-r--r--   0 runner    (1001) docker     (123)     1776 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_diff_replica.py
--rw-r--r--   0 runner    (1001) docker     (123)     2132 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_diff_sync.py
--rw-r--r--   0 runner    (1001) docker     (123)     4319 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_sync.py
--rw-r--r--   0 runner    (1001) docker     (123)      484 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/management/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)    12366 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/managers.py
--rw-r--r--   0 runner    (1001) docker     (123)     5321 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/metas.py
--rw-r--r--   0 runner    (1001) docker     (123)    16750 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/mixins.py
--rw-r--r--   0 runner    (1001) docker     (123)     1402 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/registries.py
--rw-r--r--   0 runner    (1001) docker     (123)     5158 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/signals.py
--rw-r--r--   0 runner    (1001) docker     (123)     1855 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/tracker.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/dj_cqrs/transport/
--rw-r--r--   0 runner    (1001) docker     (123)      545 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/transport/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      997 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/transport/base.py
--rw-r--r--   0 runner    (1001) docker     (123)     6231 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/transport/kombu.py
--rw-r--r--   0 runner    (1001) docker     (123)     3136 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/transport/mixins.py
--rw-r--r--   0 runner    (1001) docker     (123)      316 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/transport/mock.py
--rw-r--r--   0 runner    (1001) docker     (123)    14710 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/transport/rabbit_mq.py
--rw-r--r--   0 runner    (1001) docker     (123)     1501 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/dj_cqrs/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/django_cqrs.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)    12101 2023-01-30 14:16:33.000000 django-cqrs-2.4.9/django_cqrs.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1486 2023-01-30 14:16:33.000000 django-cqrs-2.4.9/django_cqrs.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 14:16:33.000000 django-cqrs-2.4.9/django_cqrs.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-01-30 14:16:33.000000 django-cqrs-2.4.9/django_cqrs.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       32 2023-01-30 14:16:33.000000 django-cqrs-2.4.9/django_cqrs.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-30 14:15:19.000000 django-cqrs-2.4.9/django_cqrs.egg-info/zip-safe
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/requirements/
--rw-r--r--   0 runner    (1001) docker     (123)      119 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/requirements/dev.txt
--rw-r--r--   0 runner    (1001) docker     (123)      273 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/requirements/test.txt
--rw-r--r--   0 runner    (1001) docker     (123)      428 2023-01-30 14:16:33.429533 django-cqrs-2.4.9/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1645 2023-01-30 14:14:57.000000 django-cqrs-2.4.9/setup.py
+-rw-r--r--   0        0        0    11369 2023-04-07 09:19:27.302033 django_cqrs-2.5.0/LICENSE
+-rw-r--r--   0        0        0     9066 2023-04-07 09:19:27.302033 django_cqrs-2.5.0/README.md
+-rw-r--r--   0        0        0      196 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/__init__.py
+-rw-r--r--   0        0        0     7567 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/_validation.py
+-rw-r--r--   0        0        0     1842 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/admin.py
+-rw-r--r--   0        0        0      289 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/apps.py
+-rw-r--r--   0        0        0      728 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/constants.py
+-rw-r--r--   0        0        0       60 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/controller/__init__.py
+-rw-r--r--   0        0        0     3086 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/controller/consumer.py
+-rw-r--r--   0        0        0      285 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/controller/producer.py
+-rw-r--r--   0        0        0      698 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/correlation.py
+-rw-r--r--   0        0        0     4758 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/dataclasses.py
+-rw-r--r--   0        0        0     2229 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/delay.py
+-rw-r--r--   0        0        0       60 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/__init__.py
+-rw-r--r--   0        0        0       60 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/__init__.py
+-rw-r--r--   0        0        0     4084 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_bulk_dump.py
+-rw-r--r--   0        0        0     3564 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_bulk_load.py
+-rw-r--r--   0        0        0     5915 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_consume.py
+-rw-r--r--   0        0        0     5149 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_dead_letters.py
+-rw-r--r--   0        0        0     1545 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_deleted_diff_master.py
+-rw-r--r--   0        0        0     2397 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_deleted_diff_replica.py
+-rw-r--r--   0        0        0     1178 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_deleted_sync_replica.py
+-rw-r--r--   0        0        0     2502 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_diff_master.py
+-rw-r--r--   0        0        0     1776 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_diff_replica.py
+-rw-r--r--   0        0        0     2132 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_diff_sync.py
+-rw-r--r--   0        0        0     4319 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_sync.py
+-rw-r--r--   0        0        0      484 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/management/utils.py
+-rw-r--r--   0        0        0    12661 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/managers.py
+-rw-r--r--   0        0        0     5321 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/metas.py
+-rw-r--r--   0        0        0    17101 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/mixins.py
+-rw-r--r--   0        0        0     1392 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/registries.py
+-rw-r--r--   0        0        0     5197 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/signals.py
+-rw-r--r--   0        0        0     1855 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/tracker.py
+-rw-r--r--   0        0        0      545 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/transport/__init__.py
+-rw-r--r--   0        0        0     1003 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/transport/base.py
+-rw-r--r--   0        0        0     6561 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/transport/kombu.py
+-rw-r--r--   0        0        0     3250 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/transport/mixins.py
+-rw-r--r--   0        0        0      316 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/transport/mock.py
+-rw-r--r--   0        0        0    15323 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/transport/rabbit_mq.py
+-rw-r--r--   0        0        0     1501 2023-04-07 09:19:27.306033 django_cqrs-2.5.0/dj_cqrs/utils.py
+-rw-r--r--   0        0        0     2956 2023-04-07 09:21:46.757298 django_cqrs-2.5.0/pyproject.toml
+-rw-r--r--   0        0        0    10645 1970-01-01 00:00:00.000000 django_cqrs-2.5.0/PKG-INFO
```

### Comparing `django-cqrs-2.4.9/LICENSE` & `django_cqrs-2.5.0/LICENSE`

 * *Files 0% similar despite different names*

```diff
@@ -183,15 +183,15 @@
       replaced with your own identifying information. (Don't include
       the brackets!)  The text should be enclosed in the appropriate
       comment syntax for the file format. We also recommend that a
       file or class name and description of purpose be included on the
       same "printed page" as the copyright notice for easier
       identification within third-party archives.
 
-   Copyright 2020 Ingram Micro Inc. All rights reserved.
+   Copyright 2023 Ingram Micro Inc. All rights reserved.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
```

### Comparing `django-cqrs-2.4.9/PKG-INFO` & `django_cqrs-2.5.0/README.md`

 * *Files 21% similar despite different names*

```diff
@@ -1,275 +1,248 @@
-Metadata-Version: 2.1
-Name: django-cqrs
-Version: 2.4.9
-Summary: Django CQRS data synchronisation
-Home-page: http://connect.cloudblue.com
-Author: CloudBlue
-License: Apache License, Version 2.0
-Description: Django CQRS
-        ===========
-        ![pyversions](https://img.shields.io/pypi/pyversions/django-cqrs.svg)
-        [![PyPi Status](https://img.shields.io/pypi/v/django-cqrs.svg)](https://pypi.org/project/django-cqrs/)
-        [![Docs](https://readthedocs.org/projects/django-cqrs/badge/?version=latest)](https://readthedocs.org/projects/django-cqrs)
-        [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=django-cqrs&metric=coverage)](https://sonarcloud.io/dashboard?id=django-cqrs)
-        [![Build Status](https://travis-ci.org/cloudblue/django-cqrs.svg?branch=master)](https://travis-ci.org/cloudblue/django-cqrs)
-        [![PyPI status](https://img.shields.io/pypi/status/django-cqrs.svg)](https://pypi.python.org/pypi/django-cqrs/)
-        [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=django-cqrs&metric=alert_status)](https://sonarcloud.io/dashboard?id=django-cqrs)
-        [![PyPI Downloads](https://img.shields.io/pypi/dm/django-cqrs)](https://pypi.org/project/django-cqrs/)
-        
-        `django-cqrs` is an Django application, that implements CQRS data synchronisation between several Django microservices.
-        
-        
-        CQRS
-        ----
-        In Connect we have a rather complex Domain Model. There are many microservices, that are [decomposed by subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html) and which follow [database-per-service](https://microservices.io/patterns/data/database-per-service.html) pattern. These microservices have rich and consistent APIs. They are deployed in cloud k8s cluster and scale automatically under load. Many of these services aggregate data from other ones and usually [API Composition](https://microservices.io/patterns/data/api-composition.html) is totally enough. But, some services are working too slowly with API JOINS, so another pattern needs to be applied.
-        
-        The pattern, that solves this issue is called [CQRS - Command Query Responsibility Segregation](https://microservices.io/patterns/data/cqrs.html). Core idea behind this pattern is that view databases (replicas) are defined for efficient querying and DB joins. Applications keep their replicas up to data by subscribing to [Domain events](https://microservices.io/patterns/data/domain-event.html) published by the service that owns the data. Data is [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency) and that's okay for non-critical business transactions.
-        
-        
-        Documentation
-        =============
-        
-        Full documentation is available at [https://django-cqrs.readthedocs.org](https://django-cqrs.readthedocs.org).
-        
-        
-        Examples
-        ========
-        
-        You can find an example project [here](examples/demo_project/README.md)
-        
-        Integration
-        -----------
-        * Setup `RabbitMQ`
-        * Install `django-cqrs`
-        * Apply changes to master service, according to RabbitMQ settings
-        ```python
-        # models.py
-        
-        from django.db import models
-        from dj_cqrs.mixins import MasterMixin, RawMasterMixin
-        
-        
-        class Account(MasterMixin, models.Model):
-            CQRS_ID = 'account'
-            CQRS_PRODUCE = True  # set this to False to prevent sending instances to Transport
-            
-            
-        class Author(MasterMixin, models.Model):
-            CQRS_ID = 'author'
-            CQRS_SERIALIZER = 'app.api.AuthorSerializer'
-        
-        
-        # For cases of Diamond Multi-inheritance or in case of Proxy Django-models the following approach could be used:
-        from mptt.models import MPTTModel
-        from dj_cqrs.metas import MasterMeta
-        
-        class ComplexInheritanceModel(MPTTModel, RawMasterMixin):
-            CQRS_ID = 'diamond'
-        
-        class BaseModel(RawMasterMixin):
-            CQRS_ID = 'base'
-        
-        class ProxyModel(BaseModel):
-            class Meta:
-                proxy = True
-        
-        MasterMeta.register(ComplexInheritanceModel)
-        MasterMeta.register(BaseModel)
-        ```
-        
-        ```python
-        # settings.py
-        
-        CQRS = {
-            'transport': 'dj_cqrs.transport.rabbit_mq.RabbitMQTransport',
-            'host': RABBITMQ_HOST,
-            'port': RABBITMQ_PORT,
-            'user': RABBITMQ_USERNAME,
-            'password': RABBITMQ_PASSWORD,
-        }
-        
-        ```
-        * Apply changes to replica service, according to RabbitMQ settings
-        ```python
-        from django.db import models
-        from dj_cqrs.mixins import ReplicaMixin
-        
-        
-        class AccountRef(ReplicaMixin, models.Model):
-            CQRS_ID = 'account'
-            
-            id = models.IntegerField(primary_key=True)
-            
-        
-        class AuthorRef(ReplicaMixin, models.Model):
-            CQRS_ID = 'author'
-            CQRS_CUSTOM_SERIALIZATION = True
-            
-            @classmethod
-            def cqrs_create(cls, sync, mapped_data, previous_data=None, meta=None):
-                # Override here
-                pass
-                
-            def cqrs_update(self, sync, mapped_data, previous_data=None, meta=None):
-                # Override here
-                pass
-        ```
-        
-        ```python
-        # settings.py
-        
-        CQRS = {
-            'transport': 'dj_cqrs.transport.RabbitMQTransport',
-            'queue': 'account_replica',
-            'host': RABBITMQ_HOST,
-            'port': RABBITMQ_PORT,
-            'user': RABBITMQ_USERNAME,
-            'password': RABBITMQ_PASSWORD,
-        }
-        ```
-        * Apply migrations on both services
-        * Run consumer worker on replica service. Management command: `python manage.py cqrs_consume -w 2`
-        
-        Notes
-        -----
-        
-        * When there are master models with related entities in CQRS_SERIALIZER, it's important to have operations within atomic transactions. CQRS sync will happen on transaction commit. 
-        * Please, avoid saving different instances of the same entity within transaction to reduce syncing and potential racing on replica side.
-        * Updating of related model won't trigger CQRS automatic synchronization for master model. This needs to be done manually.
-        * By default `update_fields` doesn't trigger CQRS logic, but it can be overridden for the whole application in settings:
-        ```python
-        settings.CQRS = {
-            ...
-            'master': {
-                'CQRS_AUTO_UPDATE_FIELDS': True,
-            },
-            ...
-        }
-        ```
-        or a special flag can be used in each place, where it's required to trigger CQRS flow:
-        ```python
-        instance.save(update_fields=['name'], update_cqrs_fields=True)
-        ```
-        * When only needed instances need to be synchronized, there is a method `is_sync_instance` to set filtering rule. 
-        It's important to understand, that CQRS counting works even without syncing and rule is applied every time model is updated.
-        
-        Example:
-        ```python
-        
-        class FilteredSimplestModel(MasterMixin, models.Model):
-            CQRS_ID = 'filter'
-        
-            name = models.CharField(max_length=200)
-        
-            def is_sync_instance(self):
-                return len(str(self.name)) > 2
-        ```
-        
-        Django Admin
-        -----------
-        
-        Add action to synchronize master items from Django Admin page.
-        
-        ```python
-        from django.db import models
-        from django.contrib import admin
-        
-        from dj_cqrs.admin_mixins import CQRSAdminMasterSyncMixin
-        
-        
-        class AccountAdmin(CQRSAdminMasterSyncMixin, admin.ModelAdmin):
-            ...
-        
-        
-        admin.site.register(models.Account, AccountAdmin)
-        
-        ```
-        
-        * If necessary, override ```_cqrs_sync_queryset``` from ```CQRSAdminMasterSyncMixin``` to adjust the QuerySet and use it for synchronization.
-        
-        
-        Utilities
-        ---------
-        Bulk synchronizer without transport (usage example: it may be used for initial configuration). May be used at planned downtime.
-        * On master service: `python manage.py cqrs_bulk_dump --cqrs-id=author` -> `author.dump`
-        * On replica service: `python manage.py cqrs_bulk_load -i=author.dump`
-        
-        Filter synchronizer over transport (usage example: sync some specific records to a given replica). Can be used dynamically.
-        * To sync all replicas: `python manage.py cqrs_sync --cqrs-id=author -f={"id__in": [1, 2]}`
-        * To sync all instances only with one replica: `python manage.py cqrs_sync --cqrs-id=author -f={} -q=replica`
-        
-        Set of diff synchronization tools:
-        * To get diff and synchronize master service with replica service in K8S: 
-        ```bash
-        kubectl exec -i MASTER_CONTAINER -- python manage.py cqrs_diff_master --cqrs-id=author | 
-            kubectl exec -i REPLICA_CONTAINER -- python manage.py cqrs_diff_replica |
-            kubectl exec -i MASTER_CONTAINER -- python manage.py cqrs_diff_sync
-        ```
-        
-        * If it's important to check sync and clean up deleted objects within replica service in K8S:
-        ```bash
-        kubectl exec -i REPLICA_CONTAINER -- python manage.py cqrs_deleted_diff_replica --cqrs-id=author | 
-            kubectl exec -i MASTER_CONTAINER -- python manage.py cqrs_deleted_diff_master |
-            kubectl exec -i REPLICA_CONTAINER -- python manage.py cqrs_deleted_sync_replica
-        ```
-        
-        Development
-        ===========
-        
-        1. Python 3.7 +
-        2. Install dependencies `requirements/dev.txt`
-        3. We use `isort` library to order and format our imports, and we check it using `flake8-isort` library (automatically on `flake8` run).  
-        For convenience you may run `isort .` to order imports.
-        
-        
-        Testing
-        =======
-        
-        Unit testing
-        ------
-        1. Python 3.7 +
-        2. Install dependencies `requirements/test.txt`
-        3. `export PYTHONPATH=/your/path/to/django-cqrs/`
-        
-        Run tests with various RDBMS:
-        - `cd integration_tests`
-        - `DB=postgres docker-compose -f docker-compose.yml -f rdbms.yml run app_test`
-        - `DB=mysql docker-compose -f docker-compose.yml -f rdbms.yml run app_test`
-        
-        Check code style: `flake8`
-        Run tests: `pytest`
-        
-        Tests reports are generated in `tests/reports`. 
-        * `out.xml` - JUnit test results
-        * `coverage.xml` - Coverage xml results
-        
-        To generate HTML coverage reports use:
-        `--cov-report html:tests/reports/cov_html`
-        
-        
-        Integrational testing
-        ------
-        1. docker-compose
-        0. `cd integration_tests`
-        0. `docker-compose run master`
-Keywords: django cqrs sql mixin amqp
-Platform: UNKNOWN
-Classifier: Development Status :: 5 - Production/Stable
-Classifier: Framework :: Django :: 2.2
-Classifier: Framework :: Django :: 3.0
-Classifier: Framework :: Django :: 3.1
-Classifier: Framework :: Django :: 3.2
-Classifier: Framework :: Django :: 4.0
-Classifier: Framework :: Django :: 4.1
-Classifier: Intended Audience :: Developers
-Classifier: License :: OSI Approved :: Apache Software License
-Classifier: Operating System :: Unix
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Classifier: Programming Language :: Python :: 3.11
-Classifier: Topic :: Communications
-Classifier: Topic :: Database
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
+Django CQRS
+===========
+![pyversions](https://img.shields.io/pypi/pyversions/django-cqrs.svg)
+![PyPI](https://img.shields.io/pypi/v/django-cqrs)
+[![Docs](https://readthedocs.org/projects/django-cqrs/badge/?version=latest)](https://readthedocs.org/projects/django-cqrs)
+[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=django-cqrs&metric=coverage)](https://sonarcloud.io/dashboard?id=django-cqrs)
+![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/cloudblue/django-cqrs/build.yml)
+[![PyPI status](https://img.shields.io/pypi/status/django-cqrs.svg)](https://pypi.python.org/pypi/django-cqrs/)
+[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=django-cqrs&metric=alert_status)](https://sonarcloud.io/dashboard?id=django-cqrs)
+[![PyPI Downloads](https://img.shields.io/pypi/dm/django-cqrs)](https://pypi.org/project/django-cqrs/)
+![GitHub](https://img.shields.io/github/license/cloudblue/django-cqrs)
+
+`django-cqrs` is an Django application, that implements CQRS data synchronisation between several Django microservices.
+
+
+CQRS
+----
+In Connect we have a rather complex Domain Model. There are many microservices, that are [decomposed by subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html) and which follow [database-per-service](https://microservices.io/patterns/data/database-per-service.html) pattern. These microservices have rich and consistent APIs. They are deployed in cloud k8s cluster and scale automatically under load. Many of these services aggregate data from other ones and usually [API Composition](https://microservices.io/patterns/data/api-composition.html) is totally enough. But, some services are working too slowly with API JOINS, so another pattern needs to be applied.
+
+The pattern, that solves this issue is called [CQRS - Command Query Responsibility Segregation](https://microservices.io/patterns/data/cqrs.html). Core idea behind this pattern is that view databases (replicas) are defined for efficient querying and DB joins. Applications keep their replicas up to data by subscribing to [Domain events](https://microservices.io/patterns/data/domain-event.html) published by the service that owns the data. Data is [eventually consistent](https://en.wikipedia.org/wiki/Eventual_consistency) and that's okay for non-critical business transactions.
+
+
+Documentation
+=============
+
+Full documentation is available at [https://django-cqrs.readthedocs.org](https://django-cqrs.readthedocs.org).
+
+
+Examples
+========
+
+You can find an example project [here](examples/demo_project/README.md)
+
+Integration
+-----------
+* Setup `RabbitMQ`
+* Install `django-cqrs`
+* Apply changes to master service, according to RabbitMQ settings
+```python
+# models.py
+
+from django.db import models
+from dj_cqrs.mixins import MasterMixin, RawMasterMixin
+
+
+class Account(MasterMixin, models.Model):
+    CQRS_ID = 'account'
+    CQRS_PRODUCE = True  # set this to False to prevent sending instances to Transport
+    
+    
+class Author(MasterMixin, models.Model):
+    CQRS_ID = 'author'
+    CQRS_SERIALIZER = 'app.api.AuthorSerializer'
+
+
+# For cases of Diamond Multi-inheritance or in case of Proxy Django-models the following approach could be used:
+from mptt.models import MPTTModel
+from dj_cqrs.metas import MasterMeta
+
+class ComplexInheritanceModel(MPTTModel, RawMasterMixin):
+    CQRS_ID = 'diamond'
+
+class BaseModel(RawMasterMixin):
+    CQRS_ID = 'base'
+
+class ProxyModel(BaseModel):
+    class Meta:
+        proxy = True
+
+MasterMeta.register(ComplexInheritanceModel)
+MasterMeta.register(BaseModel)
+```
+
+```python
+# settings.py
+
+CQRS = {
+    'transport': 'dj_cqrs.transport.rabbit_mq.RabbitMQTransport',
+    'host': RABBITMQ_HOST,
+    'port': RABBITMQ_PORT,
+    'user': RABBITMQ_USERNAME,
+    'password': RABBITMQ_PASSWORD,
+}
+
+```
+* Apply changes to replica service, according to RabbitMQ settings
+```python
+from django.db import models
+from dj_cqrs.mixins import ReplicaMixin
+
+
+class AccountRef(ReplicaMixin, models.Model):
+    CQRS_ID = 'account'
+    
+    id = models.IntegerField(primary_key=True)
+    
+
+class AuthorRef(ReplicaMixin, models.Model):
+    CQRS_ID = 'author'
+    CQRS_CUSTOM_SERIALIZATION = True
+    
+    @classmethod
+    def cqrs_create(cls, sync, mapped_data, previous_data=None, meta=None):
+        # Override here
+        pass
+        
+    def cqrs_update(self, sync, mapped_data, previous_data=None, meta=None):
+        # Override here
+        pass
+```
+
+```python
+# settings.py
+
+CQRS = {
+    'transport': 'dj_cqrs.transport.RabbitMQTransport',
+    'queue': 'account_replica',
+    'host': RABBITMQ_HOST,
+    'port': RABBITMQ_PORT,
+    'user': RABBITMQ_USERNAME,
+    'password': RABBITMQ_PASSWORD,
+}
+```
+* Apply migrations on both services
+* Run consumer worker on replica service. Management command: `python manage.py cqrs_consume -w 2`
+
+Notes
+-----
+
+* When there are master models with related entities in CQRS_SERIALIZER, it's important to have operations within atomic transactions. CQRS sync will happen on transaction commit. 
+* Please, avoid saving different instances of the same entity within transaction to reduce syncing and potential racing on replica side.
+* Updating of related model won't trigger CQRS automatic synchronization for master model. This needs to be done manually.
+* By default `update_fields` doesn't trigger CQRS logic, but it can be overridden for the whole application in settings:
+```python
+settings.CQRS = {
+    ...
+    'master': {
+        'CQRS_AUTO_UPDATE_FIELDS': True,
+    },
+    ...
+}
+```
+or a special flag can be used in each place, where it's required to trigger CQRS flow:
+```python
+instance.save(update_fields=['name'], update_cqrs_fields=True)
+```
+* When only needed instances need to be synchronized, there is a method `is_sync_instance` to set filtering rule. 
+It's important to understand, that CQRS counting works even without syncing and rule is applied every time model is updated.
+
+Example:
+```python
+
+class FilteredSimplestModel(MasterMixin, models.Model):
+    CQRS_ID = 'filter'
+
+    name = models.CharField(max_length=200)
+
+    def is_sync_instance(self):
+        return len(str(self.name)) > 2
+```
+
+Django Admin
+-----------
+
+Add action to synchronize master items from Django Admin page.
+
+```python
+from django.db import models
+from django.contrib import admin
+
+from dj_cqrs.admin_mixins import CQRSAdminMasterSyncMixin
+
+
+class AccountAdmin(CQRSAdminMasterSyncMixin, admin.ModelAdmin):
+    ...
+
+
+admin.site.register(models.Account, AccountAdmin)
+
+```
+
+* If necessary, override ```_cqrs_sync_queryset``` from ```CQRSAdminMasterSyncMixin``` to adjust the QuerySet and use it for synchronization.
+
+
+Utilities
+---------
+Bulk synchronizer without transport (usage example: it may be used for initial configuration). May be used at planned downtime.
+* On master service: `python manage.py cqrs_bulk_dump --cqrs-id=author` -> `author.dump`
+* On replica service: `python manage.py cqrs_bulk_load -i=author.dump`
+
+Filter synchronizer over transport (usage example: sync some specific records to a given replica). Can be used dynamically.
+* To sync all replicas: `python manage.py cqrs_sync --cqrs-id=author -f={"id__in": [1, 2]}`
+* To sync all instances only with one replica: `python manage.py cqrs_sync --cqrs-id=author -f={} -q=replica`
+
+Set of diff synchronization tools:
+* To get diff and synchronize master service with replica service in K8S: 
+```bash
+kubectl exec -i MASTER_CONTAINER -- python manage.py cqrs_diff_master --cqrs-id=author | 
+    kubectl exec -i REPLICA_CONTAINER -- python manage.py cqrs_diff_replica |
+    kubectl exec -i MASTER_CONTAINER -- python manage.py cqrs_diff_sync
+```
+
+* If it's important to check sync and clean up deleted objects within replica service in K8S:
+```bash
+kubectl exec -i REPLICA_CONTAINER -- python manage.py cqrs_deleted_diff_replica --cqrs-id=author | 
+    kubectl exec -i MASTER_CONTAINER -- python manage.py cqrs_deleted_diff_master |
+    kubectl exec -i REPLICA_CONTAINER -- python manage.py cqrs_deleted_sync_replica
+```
+
+Development
+===========
+
+1. Python >= 3.7
+2. Install dependencies `requirements/dev.txt`
+3. We use `isort` library to order and format our imports, and we check it using `flake8-isort` library (automatically on `flake8` run).  
+For convenience you may run `isort .` to order imports.
+
+
+Testing
+=======
+
+Unit testing
+------
+1. Python >= 3.7
+2. Install dependencies `requirements/test.txt`
+3. `export PYTHONPATH=/your/path/to/django-cqrs/`
+
+Run tests with various RDBMS:
+- `cd integration_tests`
+- `DB=postgres docker-compose -f docker-compose.yml -f rdbms.yml run app_test`
+- `DB=mysql docker-compose -f docker-compose.yml -f rdbms.yml run app_test`
+
+Check code style: `flake8`
+Run tests: `pytest`
+
+Tests reports are generated in `tests/reports`. 
+* `out.xml` - JUnit test results
+* `coverage.xml` - Coverage xml results
+
+To generate HTML coverage reports use:
+`--cov-report html:tests/reports/cov_html`
+
+
+Integrational testing
+------
+1. docker-compose
+2. `cd integration_tests`
+3. `docker-compose run master`
```

### Comparing `django-cqrs-2.4.9/README.md` & `django_cqrs-2.5.0/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,17 +1,58 @@
+Metadata-Version: 2.1
+Name: django-cqrs
+Version: 2.5.0
+Summary: Django CQRS data synchronisation
+Home-page: https://django-cqrs.readthedocs.org
+License: Apache-2.0
+Keywords: django,cqrs,sql,mixin,amqp
+Author: CloudBlue LLC
+Requires-Python: >=3.7,<4
+Classifier: Development Status :: 5 - Production/Stable
+Classifier: Framework :: Django :: 3.2
+Classifier: Framework :: Django :: 4.0
+Classifier: Framework :: Django :: 4.1
+Classifier: Framework :: Django :: 4.2
+Classifier: Intended Audience :: Developers
+Classifier: License :: OSI Approved :: Apache Software License
+Classifier: Operating System :: Unix
+Classifier: Programming Language :: Python :: 3
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Topic :: Communications
+Classifier: Topic :: Database
+Requires-Dist: django (>=3.2)
+Requires-Dist: django-model-utils (>=4.0.0)
+Requires-Dist: kombu (>=4.6)
+Requires-Dist: pika (>=1.0.0)
+Requires-Dist: python-dateutil (>=2.4)
+Requires-Dist: ujson (>=5.4.0)
+Requires-Dist: watchfiles (>=0.18.1,<0.19.0)
+Project-URL: Repository, https://github.com/cloudblue/django-cqrs
+Description-Content-Type: text/markdown
+
 Django CQRS
 ===========
 ![pyversions](https://img.shields.io/pypi/pyversions/django-cqrs.svg)
-[![PyPi Status](https://img.shields.io/pypi/v/django-cqrs.svg)](https://pypi.org/project/django-cqrs/)
+![PyPI](https://img.shields.io/pypi/v/django-cqrs)
 [![Docs](https://readthedocs.org/projects/django-cqrs/badge/?version=latest)](https://readthedocs.org/projects/django-cqrs)
 [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=django-cqrs&metric=coverage)](https://sonarcloud.io/dashboard?id=django-cqrs)
-[![Build Status](https://travis-ci.org/cloudblue/django-cqrs.svg?branch=master)](https://travis-ci.org/cloudblue/django-cqrs)
+![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/cloudblue/django-cqrs/build.yml)
 [![PyPI status](https://img.shields.io/pypi/status/django-cqrs.svg)](https://pypi.python.org/pypi/django-cqrs/)
 [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=django-cqrs&metric=alert_status)](https://sonarcloud.io/dashboard?id=django-cqrs)
 [![PyPI Downloads](https://img.shields.io/pypi/dm/django-cqrs)](https://pypi.org/project/django-cqrs/)
+![GitHub](https://img.shields.io/github/license/cloudblue/django-cqrs)
 
 `django-cqrs` is an Django application, that implements CQRS data synchronisation between several Django microservices.
 
 
 CQRS
 ----
 In Connect we have a rather complex Domain Model. There are many microservices, that are [decomposed by subdomain](https://microservices.io/patterns/decomposition/decompose-by-subdomain.html) and which follow [database-per-service](https://microservices.io/patterns/data/database-per-service.html) pattern. These microservices have rich and consistent APIs. They are deployed in cloud k8s cluster and scale automatically under load. Many of these services aggregate data from other ones and usually [API Composition](https://microservices.io/patterns/data/api-composition.html) is totally enough. But, some services are working too slowly with API JOINS, so another pattern needs to be applied.
@@ -205,26 +246,26 @@
     kubectl exec -i MASTER_CONTAINER -- python manage.py cqrs_deleted_diff_master |
     kubectl exec -i REPLICA_CONTAINER -- python manage.py cqrs_deleted_sync_replica
 ```
 
 Development
 ===========
 
-1. Python 3.7 +
+1. Python >= 3.7
 2. Install dependencies `requirements/dev.txt`
 3. We use `isort` library to order and format our imports, and we check it using `flake8-isort` library (automatically on `flake8` run).  
 For convenience you may run `isort .` to order imports.
 
 
 Testing
 =======
 
 Unit testing
 ------
-1. Python 3.7 +
+1. Python >= 3.7
 2. Install dependencies `requirements/test.txt`
 3. `export PYTHONPATH=/your/path/to/django-cqrs/`
 
 Run tests with various RDBMS:
 - `cd integration_tests`
 - `DB=postgres docker-compose -f docker-compose.yml -f rdbms.yml run app_test`
 - `DB=mysql docker-compose -f docker-compose.yml -f rdbms.yml run app_test`
@@ -239,9 +280,10 @@
 To generate HTML coverage reports use:
 `--cov-report html:tests/reports/cov_html`
 
 
 Integrational testing
 ------
 1. docker-compose
-0. `cd integration_tests`
-0. `docker-compose run master`
+2. `cd integration_tests`
+3. `docker-compose run master`
+
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/_validation.py` & `django_cqrs-2.5.0/dj_cqrs/_validation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import logging
 from inspect import getfullargspec, isfunction
 
 from django.utils.module_loading import import_string
 
 from dj_cqrs.constants import (
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/admin.py` & `django_cqrs-2.5.0/dj_cqrs/admin.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 from django.utils.translation import gettext_lazy
 
 
 class CQRSAdminMasterSyncMixin:
     """
     Mixin that includes a custom action in AdminModel. This action allows synchronizing
@@ -18,25 +18,30 @@
             self.actions = list(self.actions) + ['sync_items']
         return super().get_actions(request)
 
     def _cqrs_sync_queryset(self, queryset):
         """
         This function is used to adjust the QuerySet before sending the sync signal.
 
-        :param queryset: Original queryset
-        :type queryset: Queryset
-        :return: Updated queryset
-        :rtype: Queryset
+        Args:
+            queryset (Queryset): Original queryset.
+
+        Returns:
+            (Queryset): Updated queryset.
         """
         return queryset
 
     def sync_items(self, request, queryset):
         """
         This method synchronizes selected items from the Admin Page.
         It is registered as a custom action in Django Admin
+
+        Args:
+            request (Request): Original request.
+            queryset (Queryset): Original queryset.
         """
         items_not_synced = []
         for item in self._cqrs_sync_queryset(queryset):
             if not item.cqrs_sync():
                 items_not_synced.append(item)
 
         total = len(queryset)
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/constants.py` & `django_cqrs-2.5.0/dj_cqrs/constants.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 ALL_BASIC_FIELDS = '__all__'
 
 FIELDS_TRACKER_FIELD_NAME = '__fields_tracker'
 TRACKED_FIELDS_ATTR_NAME = '__tracked_fields'
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/controller/consumer.py` & `django_cqrs-2.5.0/dj_cqrs/controller/consumer.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,13 +1,14 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import copy
 import logging
 from contextlib import ExitStack
 
+from django.conf import settings
 from django.db import Error, close_old_connections, transaction
 
 from dj_cqrs.constants import SignalType
 from dj_cqrs.registries import ReplicaRegistry
 
 
 logger = logging.getLogger('django-cqrs')
@@ -21,60 +22,69 @@
     payload = copy.deepcopy(payload)
     return route_signal_to_replica_model(
         payload.signal_type,
         payload.cqrs_id,
         payload.instance_data,
         previous_data=payload.previous_data,
         meta=payload.meta,
+        queue=payload.queue,
     )
 
 
 def route_signal_to_replica_model(
-    signal_type, cqrs_id, instance_data, previous_data=None, meta=None,
+    signal_type, cqrs_id, instance_data, previous_data=None, meta=None, queue=None,
 ):
     """ Routes signal to model method to create/update/delete replica instance.
 
     :param dj_cqrs.constants.SignalType signal_type: Consumed signal type.
     :param str cqrs_id: Replica model CQRS unique identifier.
     :param dict instance_data: Master model data.
     :param dict or None previous_data: Previous model data for changed tracked fields, if exists.
     :param dict or None meta: Payload metadata, if exists.
+    :param str or None queue: Synced queue.
     """
     if signal_type not in (SignalType.DELETE, SignalType.SAVE, SignalType.SYNC):
         logger.error('Bad signal type "{0}" for CQRS_ID "{1}".'.format(signal_type, cqrs_id))
         return
 
     model_cls = ReplicaRegistry.get_model_by_cqrs_id(cqrs_id)
-    if model_cls:
-        db_is_needed = not model_cls.CQRS_NO_DB_OPERATIONS
-        if db_is_needed:
-            close_old_connections()
-
-        is_meta_supported = model_cls.CQRS_META
-        try:
-            with transaction.atomic(savepoint=False) if db_is_needed else ExitStack():
-                if signal_type == SignalType.DELETE:
-                    if is_meta_supported:
-                        return model_cls.cqrs_delete(instance_data, meta=meta)
-
-                    return model_cls.cqrs_delete(instance_data)
+    if not model_cls:
+        return
 
-                f_kw = {'previous_data': previous_data}
+    this_queue = settings.CQRS['queue']
+    if signal_type == SignalType.SYNC and model_cls.CQRS_ONLY_DIRECT_SYNCS and queue != this_queue:
+        return True
+
+    db_is_needed = not model_cls.CQRS_NO_DB_OPERATIONS
+    if db_is_needed:
+        close_old_connections()
+
+    is_meta_supported = model_cls.CQRS_META
+    try:
+        with transaction.atomic(savepoint=False) if db_is_needed else ExitStack():
+            if signal_type == SignalType.DELETE:
                 if is_meta_supported:
-                    f_kw['meta'] = meta
+                    return model_cls.cqrs_delete(instance_data, meta=meta)
 
-                if signal_type == SignalType.SAVE:
-                    return model_cls.cqrs_save(instance_data, **f_kw)
+                return model_cls.cqrs_delete(instance_data)
 
-                if signal_type == SignalType.SYNC:
-                    f_kw['sync'] = True
-                    return model_cls.cqrs_save(instance_data, **f_kw)
-
-        except Error as e:
-            pk_value = instance_data.get(model_cls._meta.pk.name)
-            cqrs_revision = instance_data.get('cqrs_revision')
-
-            logger.error(
-                '{0}\nCQRS {1} error: pk = {2}, cqrs_revision = {3} ({4}).'.format(
-                    str(e), signal_type, pk_value, cqrs_revision, model_cls.CQRS_ID,
-                ),
-            )
+            f_kw = {'previous_data': previous_data}
+            if is_meta_supported:
+                f_kw['meta'] = meta
+
+            if signal_type == SignalType.SAVE:
+                return model_cls.cqrs_save(instance_data, **f_kw)
+
+            if signal_type == SignalType.SYNC:
+                f_kw['sync'] = True
+                return model_cls.cqrs_save(instance_data, **f_kw)
+
+    except Error as e:
+        pk_name = getattr(model_cls._meta.pk, 'name', 'id')
+        pk_value = instance_data.get(pk_name)
+        cqrs_revision = instance_data.get('cqrs_revision')
+
+        logger.error(
+            '{0}\nCQRS {1} error: pk = {2}, cqrs_revision = {3} ({4}).'.format(
+                str(e), signal_type, pk_value, cqrs_revision, model_cls.CQRS_ID,
+            ),
+        )
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/correlation.py` & `django_cqrs-2.5.0/dj_cqrs/correlation.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 from django.conf import settings
 
 
 def get_correlation_id(signal_type, cqrs_id, instance_pk, queue):
     """
     :param signal_type: Type of the signal for this message.
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/dataclasses.py` & `django_cqrs-2.5.0/dj_cqrs/dataclasses.py`

 * *Files 20% similar despite different names*

```diff
@@ -1,54 +1,46 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 from dateutil.parser import parse as dateutil_parse
 from django.utils import timezone
 
 from dj_cqrs.correlation import get_correlation_id
 from dj_cqrs.utils import get_json_valid_value, get_message_expiration_dt
 
 
 class TransportPayload:
     """Transport message payload.
 
-    :param signal_type: Type of the signal for this message.
-    :type signal_type: dj_cqrs.constants.SignalType
-    :param cqrs_id: The unique CQRS identifier of the model.
-    :type cqrs_id: str
-    :param instance_data: Serialized data of the instance that
-                            generates the event.
-    :type instance_data: dict
-    :param instance_pk: Primary key of the instance.
-    :param queue: Queue to synchronize, defaults to None.
-    :type queue: str, optional
-    :param previous_data: Previous values for fields tracked for changes,
-                                defaults to None.
-    :type previous_data: dict, optional
-    :param correlation_id: Correlation ID of process, where this payload is used.
-    :type correlation_id: str, optional
-    :param retries: Current number of message retries.
-    :type retries: int, optional
-    :param expires: Message expiration datetime, infinite if None
-    :type expires: datetime, optional
-    :param meta: Payload metadata
-    :type meta: dict, optional
+    Args:
+        signal_type (dj_cqrs.constants.SignalType): Type of the signal for this message.
+        cqrs_id (str): The unique CQRS identifier of the model.
+        instance_data (dict): Serialized data of the instance that
+            generates the event.
+        instance_pk (str): Primary key of the instance.
+        queue (str): Queue to synchronize, defaults to None.
+        previous_data (dict): Previous values for fields tracked for changes,
+            defaults to None.
+        correlation_id (str): Correlation ID of process, where this payload is used.
+        retries (int): Current number of message retries.
+        expires (datetime): Message expiration datetime, infinite if None
+        meta (dict): Payload metadata
     """
 
     def __init__(
         self,
         signal_type,
-        cqrs_id,
-        instance_data,
-        instance_pk,
-        queue=None,
-        previous_data=None,
-        correlation_id=None,
+        cqrs_id: str,
+        instance_data: dict,
+        instance_pk: str,
+        queue: str = None,
+        previous_data: dict = None,
+        correlation_id: str = None,
         expires=None,
-        retries=0,
-        meta=None,
+        retries: int = 0,
+        meta: dict = None,
     ):
         self.__signal_type = signal_type
         self.__cqrs_id = cqrs_id
         self.__instance_data = instance_data
         self.__instance_pk = instance_pk
         self.__queue = queue
         self.__previous_data = previous_data
@@ -62,18 +54,19 @@
         self.__expires = expires
         self.__retries = retries
 
     @classmethod
     def from_message(cls, dct):
         """Builds payload from message data.
 
-        :param dct: Deserialized message body data.
-        :type dct: dict
-        :return: TransportPayload instance.
-        :rtype: TransportPayload
+        Args:
+            dct (dict): Deserialized message body data.
+
+        Returns:
+            (TransportPayload): TransportPayload instance.
         """
         if 'expires' in dct:
             expires = dct['expires']
             if dct['expires'] is not None:
                 expires = dateutil_parse(dct['expires'])
         else:
             # Backward compatibility for old messages otherwise they are infinite by default.
@@ -132,19 +125,19 @@
         return self.__retries
 
     @retries.setter
     def retries(self, value):
         assert value >= 0, "Payload retries field should be 0 or positive integer."
         self.__retries = value
 
-    def to_dict(self):
+    def to_dict(self) -> dict:
         """Return the payload as a dictionary.
 
-        :return: This payload.
-        :rtype: dict
+        Returns:
+            (dict): This payload.
         """
         expires = self.__expires
         if expires:
             expires = expires.replace(microsecond=0).isoformat()
 
         return {
             'signal_type': self.__signal_type,
@@ -157,14 +150,14 @@
             'expires': expires,
             'meta': self.__meta,
         }
 
     def is_expired(self):
         """Checks if this payload is expired.
 
-        :return: True if payload is expired, False otherwise.
-        :rtype: bool
+        Returns:
+            (bool): True if payload is expired, False otherwise.
         """
         return (
             self.__expires is not None
             and self.__expires <= timezone.now()
         )
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/delay.py` & `django_cqrs-2.5.0/dj_cqrs/delay.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 from queue import Full, PriorityQueue
 
 from django.utils import timezone
 
 
 class DelayMessage:
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_bulk_dump.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_bulk_dump.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import datetime
 import os
 import sys
 import time
 
 import ujson
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_bulk_load.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_bulk_load.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import os
 import sys
 
 import ujson
 from django.core.management.base import BaseCommand, CommandError
 from django.db import DatabaseError, transaction
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_consume.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_consume.py`

 * *Files 12% similar despite different names*

```diff
@@ -8,23 +8,33 @@
 from watchfiles import watch
 from watchfiles.filters import PythonFilter
 from watchfiles.run import start_process
 
 from dj_cqrs.registries import ReplicaRegistry
 
 
-logger = logging.getLogger('django_cqrs.cqrs_consume')
+logger = logging.getLogger('django-cqrs')
 
 
 def consume(**kwargs):
     import django
     django.setup()
 
     from dj_cqrs.transport import current_transport
-    current_transport.consume(**kwargs)
+    try:
+        current_transport.consume(**kwargs)
+    except KeyboardInterrupt:
+        pass
+
+
+def _display_path(path):
+    try:
+        return f'"{path.relative_to(Path.cwd())}"'
+    except ValueError:  # pragma: no cover
+        return f'"{path}"'
 
 
 class WorkersManager:
 
     def __init__(
             self,
             consume_kwargs,
@@ -61,14 +71,18 @@
             signal.signal(signal.SIGHUP, self.restart)
 
         self.start()
 
         if self.reload:
             for files_changed in self:
                 if files_changed:
+                    logger.warning(
+                        'Detected changes in %s. Reloading...',
+                        ', '.join(map(_display_path, files_changed)),
+                    )
                     self.restart()
         else:
             self.stop_event.wait()
 
         self.terminate()
 
     def start(self):
@@ -76,19 +90,21 @@
             process = start_process(
                 consume,
                 'function',
                 (),
                 self.consume_kwargs,
             )
             self.pool.append(process)
+            logger.info(f'Consumer process with pid {process.pid} started')
 
     def terminate(self, *args, **kwargs):
         while self.pool:
             process = self.pool.pop()
             process.stop(sigint_timeout=self.sigint_timeout, sigkill_timeout=self.sigkill_timeout)
+            logger.info(f'Consumer process with pid {process.pid} stopped.')
 
     def restart(self, *args, **kwargs):
         self.terminate()
         self.start()
 
     def __iter__(self):
         return self
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_dead_letters.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_dead_letters.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import ujson
 from django.core.management.base import BaseCommand, CommandError
 
 from dj_cqrs.constants import DEFAULT_MASTER_MESSAGE_TTL
 from dj_cqrs.dataclasses import TransportPayload
 from dj_cqrs.registries import ReplicaRegistry
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_deleted_diff_master.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_deleted_diff_master.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import sys
 
 import ujson
 from django.core.management.base import BaseCommand, CommandError
 
 from dj_cqrs.registries import MasterRegistry
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_deleted_diff_replica.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_deleted_diff_replica.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import ujson
 from django.core.exceptions import FieldError
 from django.core.management.base import BaseCommand, CommandError
 from django.utils.timezone import now
 
 from dj_cqrs.management.utils import batch_qs
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_deleted_sync_replica.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_deleted_sync_replica.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import sys
 
 import ujson
 from django.core.management.base import BaseCommand, CommandError
 from django.db import DatabaseError
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_diff_master.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_diff_master.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import ujson
 from django.core.exceptions import FieldError
 from django.core.management.base import BaseCommand, CommandError
 from django.utils.timezone import now
 
 from dj_cqrs.management.utils import batch_qs
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_diff_replica.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_diff_replica.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import sys
 
 import ujson
 from django.conf import settings
 from django.core.management.base import BaseCommand, CommandError
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_diff_sync.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_diff_sync.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import sys
 
 from django.core.management.base import BaseCommand, CommandError
 
 from dj_cqrs.constants import NO_QUEUE
 from dj_cqrs.management.commands.cqrs_sync import (
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/management/commands/cqrs_sync.py` & `django_cqrs-2.5.0/dj_cqrs/management/commands/cqrs_sync.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import datetime
 import sys
 import time
 
 import ujson
 from django.core.exceptions import FieldError
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/managers.py` & `django_cqrs-2.5.0/dj_cqrs/managers.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import logging
 
 from django.core.exceptions import ValidationError
 from django.db import Error, transaction
 from django.db.models import F, Manager
 from django.utils import timezone
@@ -15,31 +15,33 @@
 
 class MasterManager(Manager):
     def bulk_create(self, objs, **kwargs):
         """
         Custom bulk create method to support sending of create signals.
         This can be used only in cases, when IDs are generated on client or DB returns IDs.
 
-        :param django.db.models.Model objs: List of objects for creation
-        :param kwargs: Bulk create kwargs
+        Args:
+            objs (List[django.db.models.Model]): List of objects for creation.
+            kwargs (dict): Bulk create kwargs.
         """
         for obj in objs:
             obj.save_tracked_fields()
         objs = super().bulk_create(objs, **kwargs)
 
         if objs:
             self.model.call_post_bulk_create(objs, using=self.db)
 
         return objs
 
     def bulk_update(self, queryset, **kwargs):
         """ Custom update method to support sending of update signals.
 
-        :param django.db.models.QuerySet queryset: Django Queryset (f.e. filter)
-        :param kwargs: Update kwargs
+        Args:
+            queryset (django.db.models.QuerySet): Django Queryset (f.e. filter).
+            kwargs (dict): Update kwargs.
         """
         prev_data_mapper = {}
         collect_prev_data = hasattr(self.model, FIELDS_TRACKER_FIELD_NAME)
 
         # Add filter by list of ids in case of update kwargs
         # are the same as the chain filter kwargs in the Queryset.
         # If that happen the .all() method will refresh after update and
@@ -70,23 +72,31 @@
 
         queryset.model.call_post_update(objs, using=queryset.db)
 
         return result
 
 
 class ReplicaManager(Manager):
-    def save_instance(self, master_data, previous_data=None, sync=False, meta=None):
+    def save_instance(
+        self,
+        master_data: dict,
+        previous_data: dict = None,
+        sync: bool = False,
+        meta: dict = None,
+    ):
         """ This method saves (creates or updates) model instance from CQRS master instance data.
 
-        :param dict master_data: CQRS master instance data.
-        :param dict previous_data: Previous values for tracked fields.
-        :param bool sync: Sync package flag.
-        :param dict or None meta: Payload metadata, if exists.
-        :return: Model instance.
-        :rtype: django.db.models.Model
+        Args:
+            master_data (dict): CQRS master instance data.
+            previous_data (dict): Previous values for tracked fields.
+            sync (bool): Sync package flag.
+            meta (dict): Payload metadata, if exists.
+
+        Returns:
+            (django.db.models.Model): Model instance.
         """
         mapped_data = self._map_save_data(master_data)
         mapped_previous_data = self._map_previous_data(previous_data) if previous_data else None
         if mapped_data:
             pk_name = self._get_model_pk_name()
             pk_value = mapped_data[pk_name]
             f_kwargs = {pk_name: pk_value}
@@ -109,23 +119,31 @@
             return self.create_instance(
                 mapped_data,
                 previous_data=mapped_previous_data,
                 sync=sync,
                 meta=meta,
             )
 
-    def create_instance(self, mapped_data, previous_data=None, sync=False, meta=None):
+    def create_instance(
+        self,
+        mapped_data: dict,
+        previous_data: dict = None,
+        sync: bool = False,
+        meta: dict = None,
+    ):
         """ This method creates model instance from mapped CQRS master instance data.
 
-        :param dict mapped_data: Mapped CQRS master instance data.
-        :param dict previous_data: Previous values for tracked fields.
-        :param bool sync: Sync package flag.
-        :param dict or None meta: Payload metadata, if exists.
-        :return: ReplicaMixin model instance.
-        :rtype: django.db.models.Model
+        Args:
+            mapped_data (dict): Mapped CQRS master instance data.
+            previous_data (dict): Previous values for tracked fields.
+            sync (bool): Sync package flag.
+            meta (dict): Payload metadata, if exists.
+
+        Returns:
+            (django.db.models.Model): ReplicaMixin instance.
         """
         f_kw = {'previous_data': previous_data}
         if self.model.CQRS_META:
             f_kw['meta'] = meta
 
         try:
             return self.model.cqrs_create(sync, mapped_data, **f_kw)
@@ -134,24 +152,33 @@
 
             logger.error(
                 '{0}\nCQRS create error: pk = {1} ({2}).'.format(
                     str(e), pk_value, self.model.CQRS_ID,
                 ),
             )
 
-    def update_instance(self, instance, mapped_data, previous_data=None, sync=False, meta=None):
+    def update_instance(
+        self,
+        instance,
+        mapped_data: dict,
+        previous_data: dict = None,
+        sync: bool = False,
+        meta: dict = None,
+    ):
         """ This method updates model instance from mapped CQRS master instance data.
 
-        :param django.db.models.Model instance: ReplicaMixin model instance.
-        :param dict mapped_data: Mapped CQRS master instance data.
-        :param dict previous_data: Previous values for tracked fields.
-        :param dict or None meta: Payload metadata, if exists.
-        :param bool sync: Sync package flag.
-        :return: ReplicaMixin model instance.
-        :rtype: django.db.models.Model
+        Args:
+            instance (django.db.models.Model): ReplicaMixin model instance.
+            mapped_data (dict): Mapped CQRS master instance data.
+            previous_data (dict): Previous values for tracked fields.
+            sync (bool): Sync package flag.
+            meta (dict): Payload metadata, if exists.
+
+        Returns:
+            (django.db.models.Model): ReplicaMixin instance.
         """
         pk_value = mapped_data[self._get_model_pk_name()]
         current_cqrs_revision = mapped_data['cqrs_revision']
         existing_cqrs_revision = instance.cqrs_revision
 
         if sync:
             if existing_cqrs_revision > current_cqrs_revision:
@@ -207,20 +234,22 @@
         except (Error, ValidationError) as e:
             logger.error(
                 '{0}\nCQRS update error: pk = {1}, cqrs_revision = {2} ({3}).'.format(
                     str(e), pk_value, current_cqrs_revision, self.model.CQRS_ID,
                 ),
             )
 
-    def delete_instance(self, master_data):
+    def delete_instance(self, master_data: dict) -> bool:
         """ This method deletes model instance from mapped CQRS master instance data.
 
-        :param dict master_data: CQRS master instance data.
-        :return: Flag, if delete operation is successful (even if nothing was deleted).
-        :rtype: bool
+        Args:
+            master_data (dict): CQRS master instance data.
+
+        Returns:
+            Flag, if delete operation is successful (even if nothing was deleted).
         """
         mapped_data = self._map_delete_data(master_data)
 
         if mapped_data:
             pk_name = self._get_model_pk_name()
             pk_value = mapped_data[pk_name]
             try:
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/metas.py` & `django_cqrs-2.5.0/dj_cqrs/metas.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 from django.db.models import base
 
 from dj_cqrs.constants import ALL_BASIC_FIELDS
 from dj_cqrs.registries import MasterRegistry, ReplicaRegistry
 from dj_cqrs.signals import MasterSignals
 from dj_cqrs.tracker import CQRSTracker
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/mixins.py` & `django_cqrs-2.5.0/dj_cqrs/mixins.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import logging
 
 from django.conf import settings
 from django.db import router, transaction
 from django.db.models import (
     DateField,
@@ -129,51 +129,52 @@
                     data = tracker.changed()
                 setattr(self, TRACKED_FIELDS_ATTR_NAME, data)
 
     @property
     def _update_cqrs_fields_default(self):
         return settings.CQRS['master']['CQRS_AUTO_UPDATE_FIELDS']
 
-    def to_cqrs_dict(self, using=None, sync=False):
+    def to_cqrs_dict(self, using: str = None, sync: bool = False) -> dict:
         """CQRS serialization for transport payload.
 
-        :param using: The using argument can be used to force the database
-                      to use, defaults to None
-        :type using: str, optional
-        :type sync: bool, optional
-        :return: The serialized instance data.
-        :rtype: dict
+        Args:
+            using (str): The using argument can be used to force the database to use,
+                defaults to None.
+            sync (bool): optional
+
+        Returns:
+            (dict): The serialized instance data.
         """
         if self.CQRS_SERIALIZER:
             data = self._class_serialization(using, sync=sync)
         else:
             self._refresh_f_expr_values(using)
             data = self._common_serialization(using)
         return data
 
-    def get_tracked_fields_data(self):
+    def get_tracked_fields_data(self) -> dict:
         """CQRS serialization for tracked fields to include
         in the transport payload.
 
-        :return: Previous values for tracked fields.
-        :rtype: dict
+        Returns:
+            (dict): Previous values for tracked fields.
         """
         return getattr(self, TRACKED_FIELDS_ATTR_NAME, None)
 
-    def cqrs_sync(self, using=None, queue=None):
+    def cqrs_sync(self, using: str = None, queue: str = None) -> bool:
         """Manual instance synchronization.
 
-        :param using: The using argument can be used to force the database
-                      to use, defaults to None
-        :type using: str, optional
-        :param queue: Syncing can be executed just for a single queue, defaults to None
-                      (all queues)
-        :type queue: str, optional
-        :return: True if instance can be synced, False otherwise.
-        :rtype: bool
+        Args:
+            using (str): The using argument can be used to force the database
+                to use, defaults to None.
+            queue (str): Syncing can be executed just for a single queue, defaults to None
+                 (all queues).
+
+        Returns:
+            (bool): True if instance can be synced, False otherwise.
         """
         if self._state.adding:
             return False
 
         if not self.CQRS_SERIALIZER:
             try:
                 self.refresh_from_db()
@@ -181,31 +182,33 @@
                 return False
 
         MasterSignals.post_save(
             self._meta.model, instance=self, using=using, queue=queue, sync=True,
         )
         return True
 
-    def is_sync_instance(self):
+    def is_sync_instance(self) -> bool:
         """
         This method can be overridden to apply syncing only to instances by some rules.
         For example, only objects with special status or after some creation date, etc.
 
-        :return: True if this instance needs to be synced, False otherwise
-        :rtype: bool
+        Returns:
+            (bool): True if this instance needs to be synced, False otherwise.
         """
         return True
 
-    def get_cqrs_meta(self, **kwargs):
+    def get_cqrs_meta(self, **kwargs: dict) -> dict:
         """
         This method can be overridden to collect model/instance specific metadata.
 
-        :type kwargs: Signal type, payload data, etc.
-        :return: Metadata dictionary if it's provided.
-        :rtype: dict
+        Args:
+            kwargs (dict): Signal type, payload data, etc.
+
+        Returns:
+            (dict): Metadata dictionary if it's provided.
         """
         generic_meta_func = settings.CQRS['master']['meta_function']
         if generic_meta_func:
             return generic_meta_func(obj=self, **kwargs)
 
         return {}
 
@@ -213,45 +216,49 @@
     def relate_cqrs_serialization(cls, queryset):
         """
         This method shoud be overriden to optimize database access
         for example using `select_related` and `prefetch_related`
         when related models must be included into the master model
         representation.
 
-        :param queryset: The initial queryset.
-        :type queryset: django.db.models.QuerySet
-        :return: The optimized queryset.
-        :rtype: django.db.models.QuerySet
+        Args:
+            queryset (django.db.models.QuerySet): The initial queryset.
+
+        Returns:
+            (django.db.models.QuerySet): The optimized queryset.
+
         """
         return queryset
 
     def get_custom_cqrs_delete_data(self):
         """ This method should be overridden when additional data is needed in DELETE payload. """
         pass
 
     @classmethod
-    def call_post_bulk_create(cls, instances, using=None):
+    def call_post_bulk_create(cls, instances: list, using=None):
         """ Post bulk create signal caller (django doesn't support it by default).
 
-        .. code-block:: python
+        ``` py3
 
             # Used automatically by cqrs.bulk_create()
             instances = model.cqrs.bulk_create(instances)
+        ```
         """
         post_bulk_create.send(cls, instances=instances, using=using)
 
     @classmethod
     def call_post_update(cls, instances, using=None):
         """ Post bulk update signal caller (django doesn't support it by default).
 
-        .. code-block:: python
+        ``` py3
 
             # Used automatically by cqrs.bulk_update()
             qs = model.objects.filter(k1=v1)
             model.cqrs.bulk_update(qs, k2=v2)
+        ```
         """
         post_update.send(cls, instances=instances, using=using)
 
     def _common_serialization(self, using):
         opts = self._meta
 
         if isinstance(self.CQRS_FIELDS, str) and self.CQRS_FIELDS == ALL_BASIC_FIELDS:
@@ -347,39 +354,40 @@
         raise NotImplementedError
 
     @classmethod
     def cqrs_delete(cls, master_data, **kwargs):
         raise NotImplementedError
 
     @staticmethod
-    def should_retry_cqrs(current_retry, exception=None):
+    def should_retry_cqrs(current_retry: int, exception=None) -> bool:
         """Checks if we should retry the message after current attempt.
 
-        :param current_retry: Current number of message retries.
-        :type current_retry: int
-        :param exception: Exception instance raised during message consume.
-        :type exception: Exception, optional
-        :return: True if message should be retried, False otherwise.
-        :rtype: bool
+        Args:
+            current_retry (int): Current number of message retries.
+            exception (Exception): Exception instance raised during message consume.
+
+        Returns:
+            (bool): True if message should be retried, False otherwise.
         """
         max_retries = settings.CQRS['replica']['CQRS_MAX_RETRIES']
         if max_retries is None:
             # Infinite
             return True
 
         return current_retry < max_retries
 
     @staticmethod
-    def get_cqrs_retry_delay(current_retry):
+    def get_cqrs_retry_delay(current_retry: int) -> int:
         """Returns number of seconds to wait before requeuing the message.
 
-        :param current_retry: Current number of message retries.
-        :type current_retry: int
-        :return: Delay in seconds.
-        :rtype: int
+        Args:
+            current_retry (int): Current number of message retries.
+
+        Returns:
+            (int): Delay in seconds.
         """
         return settings.CQRS['replica']['CQRS_RETRY_DELAY']
 
 
 class ReplicaMixin(RawReplicaMixin, Model, metaclass=ReplicaMeta):
     """
     Mixin for the replica CQRS model, that will receive data updates from master. Models, using
@@ -399,78 +407,107 @@
 
     CQRS_NO_DB_OPERATIONS = False
     """Set it to True to disable any default DB operations for this model."""
 
     CQRS_META = False
     """Set it to True to receive meta data for this model."""
 
+    CQRS_ONLY_DIRECT_SYNCS = False
+    """Set it to True to ignore broadcast sync packages and to receive only direct queue syncs."""
+
     objects = Manager()
     cqrs = ReplicaManager()
     """Manager that adds needed CQRS queryset methods."""
 
     cqrs_revision = IntegerField()
     cqrs_updated = DateTimeField()
 
     class Meta:
         abstract = True
 
     @classmethod
-    def cqrs_save(cls, master_data, previous_data=None, sync=False, meta=None):
+    def cqrs_save(
+        cls,
+        master_data: dict,
+        previous_data: dict = None,
+        sync: bool = False,
+        meta: dict = None,
+    ):
         """ This method saves (creates or updates) model instance from CQRS master instance data.
         This method must not be overridden. Otherwise, sync checks need to be implemented manually.
 
-        :param dict master_data: CQRS master instance data.
-        :param dict previous_data: Previous values for tracked fields.
-        :param bool sync: Sync package flag.
-        :param dict or None meta: Payload metadata, if exists.
-        :return: Model instance.
-        :rtype: django.db.models.Model
+        Args:
+            master_data (dict): CQRS master instance data.
+            previous_data (dict): Previous values for tracked fields.
+            sync (bool): Sync package flag.
+            meta (dict): Payload metadata, if exists.
+
+        Returns:
+            (django.db.models.Model): Model instance.
         """
         if cls.CQRS_NO_DB_OPERATIONS:
             return super().cqrs_save(master_data, previous_data=previous_data, sync=sync, meta=meta)
 
         return cls.cqrs.save_instance(master_data, previous_data, sync, meta)
 
     @classmethod
-    def cqrs_create(cls, sync, mapped_data, previous_data=None, meta=None):
+    def cqrs_create(
+        cls,
+        sync: bool,
+        mapped_data: dict,
+        previous_data: dict = None,
+        meta: dict = None,
+    ):
         """ This method creates model instance from CQRS mapped instance data. It must be overridden
         by replicas of master models with custom serialization.
 
-        :param bool sync: Sync package flag.
-        :param dict mapped_data: CQRS mapped instance data.
-        :param dict previous_data: Previous mapped values for tracked fields.
-        :param dict or None meta: Payload metadata, if exists.
-        :return: Model instance.
-        :rtype: django.db.models.Model
+        Args:
+            sync (dict): Sync package flag.
+            mapped_data (dict): CQRS mapped instance data.
+            previous_data (dict): Previous mapped values for tracked fields.
+            meta (dict): Payload metadata, if exists.
+
+        Returns:
+            (django.db.models.Model): Model instance.
         """
         return cls._default_manager.create(**mapped_data)
 
-    def cqrs_update(self, sync, mapped_data, previous_data=None, meta=None):
+    def cqrs_update(
+        self,
+        sync: bool,
+        mapped_data: dict,
+        previous_data: dict = None,
+        meta: dict = None,
+    ):
         """ This method updates model instance from CQRS mapped instance data. It must be overridden
         by replicas of master models with custom serialization.
 
-        :param bool sync: Sync package flag.
-        :param dict mapped_data: CQRS mapped instance data.
-        :param dict previous_data: Previous mapped values for tracked fields.
-        :param dict or None meta: Payload metadata, if exists.
-        :return: Model instance.
-        :rtype: django.db.models.Model
+        Args:
+            sync (dict): Sync package flag.
+            mapped_data (dict): CQRS mapped instance data.
+            previous_data (dict): Previous mapped values for tracked fields.
+            meta (dict): Payload metadata, if exists.
+
+        Returns:
+            (django.db.models.Model): Model instance.
         """
 
         for key, value in mapped_data.items():
             setattr(self, key, value)
         self.save()
         return self
 
     @classmethod
-    def cqrs_delete(cls, master_data, meta=None):
+    def cqrs_delete(cls, master_data: dict, meta: dict = None) -> bool:
         """ This method deletes model instance from mapped CQRS master instance data.
 
-        :param dict master_data: CQRS master instance data.
-        :param dict or None meta: Payload metadata, if exists.
-        :return: Flag, if delete operation is successful (even if nothing was deleted).
-        :rtype: bool
+        Args:
+            master_data (dict): CQRS master instance data.
+            meta (dict): Payload metadata, if exists.
+
+        Returns:
+            (bool): Flag, if delete operation is successful (even if nothing was deleted).
         """
         if cls.CQRS_NO_DB_OPERATIONS:
             return super().cqrs_delete(master_data, meta=meta)
 
         return cls.cqrs.delete_instance(master_data)
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/registries.py` & `django_cqrs-2.5.0/dj_cqrs/registries.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import logging
 
 from django.conf import settings
 
 
 logger = logging.getLogger('django-cqrs')
@@ -19,19 +19,20 @@
         cls.models[model_cls.CQRS_ID] = model_cls
 
     @classmethod
     def get_model_by_cqrs_id(cls, cqrs_id):
         """
         Returns the model class given its CQRS_ID.
 
-        :param cqrs_id: The CQRS_ID of the model to be retrieved.
-        :type cqrs_id: str
-        :return: The model that correspond to the given CQRS_ID or None if it
+        Args:
+            cqrs_id (str): The CQRS_ID of the model to be retrieved.
+
+        Returns:
+            (django.db.models.Model): The model that correspond to the given CQRS_ID or None if it
                  has not been registered.
-        :rtype: django.db.models.Model
         """
         if cqrs_id in cls.models:
             return cls.models[cqrs_id]
 
         logger.error('No model with such CQRS_ID: {0}.'.format(cqrs_id))
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/signals.py` & `django_cqrs-2.5.0/dj_cqrs/signals.py`

 * *Files 11% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import logging
 
 from django.db import models, transaction
 from django.dispatch import Signal
 from django.utils.timezone import now
 
@@ -30,28 +30,29 @@
 class MasterSignals:
     """ Signals registry and handlers for CQRS master models. """
     @classmethod
     def register_model(cls, model_cls):
         """
         Registers signals for a model.
 
-        :param model_cls:  Model class inherited from CQRS MasterMixin.
-        :type model_cls: dj_cqrs.mixins.MasterMixin
+        Args:
+            model_cls (dj_cqrs.mixins.MasterMixin): Model class inherited from CQRS MasterMixin.
         """
 
         models.signals.post_save.connect(cls.post_save, sender=model_cls)
         models.signals.post_delete.connect(cls.post_delete, sender=model_cls)
 
         post_bulk_create.connect(cls.post_bulk_create, sender=model_cls)
         post_update.connect(cls.post_bulk_update, sender=model_cls)
 
     @classmethod
     def post_save(cls, sender, **kwargs):
         """
-        :param dj_cqrs.mixins.MasterMixin sender: Class or instance inherited from CQRS MasterMixin.
+        Args:
+            sender (dj_cqrs.mixins.MasterMixin): Class or instance inherited from CQRS MasterMixin.
         """
         if not sender.CQRS_PRODUCE:
             return
 
         update_fields = kwargs.get('update_fields')
         if update_fields and ('cqrs_revision' not in update_fields):
             return
@@ -103,15 +104,16 @@
             meta=meta,
         )
         producer.produce(payload)
 
     @classmethod
     def post_delete(cls, sender, **kwargs):
         """
-        :param dj_cqrs.mixins.MasterMixin sender: Class or instance inherited from CQRS MasterMixin.
+        Args:
+            sender (dj_cqrs.mixins.MasterMixin): Class or instance inherited from CQRS MasterMixin.
         """
         if not sender.CQRS_PRODUCE:
             return
 
         instance = kwargs['instance']
         if not instance.is_sync_instance():
             return
@@ -143,22 +145,24 @@
         )
         # Delete is always in transaction!
         transaction.on_commit(lambda: producer.produce(payload))
 
     @classmethod
     def post_bulk_create(cls, sender, **kwargs):
         """
-        :param dj_cqrs.mixins.MasterMixin sender: Class or instance inherited from CQRS MasterMixin.
+        Args:
+            sender (dj_cqrs.mixins.MasterMixin): Class or instance inherited from CQRS MasterMixin.
         """
         cls._post_bulk(sender, **kwargs)
 
     @classmethod
     def post_bulk_update(cls, sender, **kwargs):
         """
-        :param dj_cqrs.mixins.MasterMixin sender: Class or instance inherited from CQRS MasterMixin.
+        Args:
+            sender (dj_cqrs.mixins.MasterMixin): Class or instance inherited from CQRS MasterMixin.
         """
         cls._post_bulk(sender, **kwargs)
 
     @classmethod
     def _post_bulk(cls, sender, **kwargs):
         for instance in kwargs['instances']:
             cls.post_save(sender, instance=instance, using=kwargs['using'])
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/tracker.py` & `django_cqrs-2.5.0/dj_cqrs/tracker.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 from model_utils import FieldTracker
 from model_utils.tracker import FieldInstanceTracker
 
 from dj_cqrs.constants import ALL_BASIC_FIELDS, FIELDS_TRACKER_FIELD_NAME
 from dj_cqrs.utils import get_json_valid_value
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/transport/__init__.py` & `django_cqrs-2.5.0/dj_cqrs/transport/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 from django.conf import settings
 from django.utils.module_loading import import_string
 
 from dj_cqrs.transport.base import BaseTransport
 from dj_cqrs.transport.kombu import KombuTransport
 from dj_cqrs.transport.rabbit_mq import RabbitMQTransport
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/transport/base.py` & `django_cqrs-2.5.0/dj_cqrs/transport/base.py`

 * *Files 27% similar despite different names*

```diff
@@ -1,31 +1,33 @@
-#  Copyright © 2020 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 
 class BaseTransport:
     """
     CQRS pattern can be implemented over any transport (AMQP, HTTP, etc.)
     All transports need to inherit from this base class.
     Transport must be set in Django settings:
 
-    .. code-block:: python
+    ``` py3
 
         CQRS = {
             'transport': 'dj_cqrs.transport.rabbit_mq.RabbitMQTransport',
         }
+    ```
     """
 
     consumers = {}
 
     @staticmethod
     def produce(payload):
         """
         Send data from master model to replicas.
 
-        :param dj_cqrs.dataclasses.TransportPayload payload: Transport payload from master model.
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
         """
         raise NotImplementedError
 
     @staticmethod
     def consume(*args, **kwargs):
         """Receive data from master model."""
         raise NotImplementedError
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/transport/kombu.py` & `django_cqrs-2.5.0/dj_cqrs/transport/kombu.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import logging
 
 import ujson
 from django.conf import settings
 from kombu import (
     Connection,
@@ -71,23 +71,29 @@
                 prefetch_count=self.prefetch_count,
                 auto_declare=True,
             ),
         ]
 
 
 class KombuTransport(LoggingMixin, BaseTransport):
+    """Transport class for Kombu."""
     CONSUMER_RETRY_TIMEOUT = 5
 
     @classmethod
     def clean_connection(cls):
         """Nothing to do here"""
         pass
 
     @classmethod
     def consume(cls, cqrs_ids=None):
+        """Receive data from master model.
+
+        Args:
+            cqrs_ids (str): cqrs ids.
+        """
         queue_name, prefetch_count = cls._get_consumer_settings()
         url, exchange_name = cls._get_common_settings()
 
         consumer = _KombuConsumer(
             url,
             exchange_name,
             queue_name,
@@ -95,14 +101,20 @@
             cls._consume_message,
             cqrs_ids=cqrs_ids,
         )
         consumer.run()
 
     @classmethod
     def produce(cls, payload):
+        """
+        Send data from master model to replicas.
+
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
+        """
         url, exchange_name = cls._get_common_settings()
 
         connection = None
         try:
             # Decided not to create context-manager to stay within the class
             connection, channel = cls._get_producer_kombu_objects(url, exchange_name)
             exchange = cls._create_exchange(exchange_name)
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/transport/mixins.py` & `django_cqrs-2.5.0/dj_cqrs/transport/mixins.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,86 +1,94 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import logging
 
 
 logger = logging.getLogger('django-cqrs')
 
 
 class LoggingMixin:
     _BASE_PAYLOAD_LOG_TEMPLATE = "CQRS is %s: pk = %s (%s), correlation_id = %s."
 
     @staticmethod
     def log_consumed(payload):
         """
-        :param dj_cqrs.dataclasses.TransportPayload payload: Transport payload from master model.
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
         """
         msg = "CQRS is received: pk = %s (%s), correlation_id = %s."
         logger.info(msg, payload.pk, payload.cqrs_id, payload.correlation_id)
 
     @staticmethod
     def log_consumed_accepted(payload):
         """
-        :param dj_cqrs.dataclasses.TransportPayload payload: Transport payload from master model.
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
         """
         msg = "CQRS is applied: pk = %s (%s), correlation_id = %s."
         logger.info(msg, payload.pk, payload.cqrs_id, payload.correlation_id)
 
     @staticmethod
     def log_consumed_denied(payload):
         """
-        :param dj_cqrs.dataclasses.TransportPayload payload: Transport payload from master model.
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
         """
         msg = "CQRS is denied: pk = %s (%s), correlation_id = %s."
         logger.warning(msg, payload.pk, payload.cqrs_id, payload.correlation_id)
 
     @staticmethod
     def log_consumed_failed(payload):
         """
-        :param dj_cqrs.dataclasses.TransportPayload payload: Transport payload from master model.
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
         """
         msg = (
             "CQRS is failed: pk = %s (%s), correlation_id = %s, retries = %s.",
         )
         logger.warning(
             msg, payload.pk, payload.cqrs_id, payload.correlation_id, payload.retries,
         )
 
     @staticmethod
     def log_dead_letter(payload):
         """
-        :param dj_cqrs.dataclasses.TransportPayload payload: Transport payload from master model.
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
         """
         msg = "CQRS is added to dead letter queue: pk = %s (%s), correlation_id = %s."
         logger.warning(msg, payload.pk, payload.cqrs_id, payload.correlation_id)
 
     @staticmethod
     def log_delayed(payload, delay, eta):
         """
-        :param dj_cqrs.dataclasses.TransportPayload payload: Transport payload from master model.
-        :param delay: Seconds to wait before requeuing message.
-        :param eta: Requeuing datetime.
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
+            delay (int): Seconds to wait before requeuing message.
+            eta (datetime): Requeuing datetime.
         """
         msg = (
             "CQRS is delayed: pk = %s (%s), correlation_id = %s, delay = %s sec, eta = %s.",
         )
         logger.warning(
-            msg, payload.pk, payload.cqrs_id, payload.correlation_id,  delay, eta,
+            msg, payload.pk, payload.cqrs_id, payload.correlation_id, delay, eta,
         )
 
     @staticmethod
     def log_requeued(payload):
         """
-        :param dj_cqrs.dataclasses.TransportPayload payload: Transport payload from master model.
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
         """
         msg = (
             "CQRS is requeued: pk = %s (%s), correlation_id = %s.",
         )
         logger.warning(msg, payload.pk, payload.cqrs_id, payload.correlation_id)
 
     @staticmethod
     def log_produced(payload):
         """
-        :param dj_cqrs.dataclasses.TransportPayload payload: Transport payload from master model.
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
         """
         msg = "CQRS is published: pk = %s (%s), correlation_id = %s."
         logger.info(msg, payload.pk, payload.cqrs_id, payload.correlation_id)
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/transport/rabbit_mq.py` & `django_cqrs-2.5.0/dj_cqrs/transport/rabbit_mq.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2021 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import logging
 import time
 from datetime import timedelta
 from socket import gaierror
 from urllib.parse import unquote, urlparse
 
@@ -28,34 +28,41 @@
 from dj_cqrs.utils import get_delay_queue_max_size, get_messages_prefetch_count_per_worker
 
 
 logger = logging.getLogger('django-cqrs')
 
 
 class RabbitMQTransport(LoggingMixin, BaseTransport):
+    """Transport class for RabbitMQ."""
     CONSUMER_RETRY_TIMEOUT = 5
     PRODUCER_RETRIES = 1
 
     _producer_connection = None
     _producer_channel = None
 
     @classmethod
     def clean_connection(cls):
+        """Clean the RabbitMQ connection."""
         connection = cls._producer_connection
         if connection and not connection.is_closed:
             try:
                 connection.close()
             except (exceptions.StreamLostError, exceptions.ConnectionClosed, ConnectionError):
                 logger.warning("Connection was closed or is closing. Skip it...")
 
         cls._producer_connection = None
         cls._producer_channel = None
 
     @classmethod
     def consume(cls, cqrs_ids=None):
+        """Receive data from master model.
+
+        Args:
+            cqrs_ids (str): cqrs ids.
+        """
         consumer_rabbit_settings = cls._get_consumer_settings()
         common_rabbit_settings = cls._get_common_settings()
 
         while True:
             connection = None
             try:
                 delay_queue = DelayQueue(max_size=get_delay_queue_max_size())
@@ -77,14 +84,20 @@
                 time.sleep(cls.CONSUMER_RETRY_TIMEOUT)
             finally:
                 if connection and not connection.is_closed:
                     connection.close()
 
     @classmethod
     def produce(cls, payload):
+        """
+        Send data from master model to replicas.
+
+        Args:
+            payload (dj_cqrs.dataclasses.TransportPayload): Transport payload from master model.
+        """
         cls._produce_with_retries(payload, retries=cls.PRODUCER_RETRIES)
 
     @classmethod
     def _produce_with_retries(cls, payload, retries):
         try:
             rmq_settings = cls._get_common_settings()
             exchange = rmq_settings[-1]
@@ -92,26 +105,35 @@
             _, channel = cls._get_producer_rmq_objects(
                 *rmq_settings, signal_type=payload.signal_type,
             )
 
             cls._produce_message(channel, exchange, payload)
             cls.log_produced(payload)
         except (
-            exceptions.AMQPError, exceptions.ChannelError, exceptions.ReentrancyError,
+            exceptions.AMQPError,
+            exceptions.ChannelError,
+            exceptions.ReentrancyError,
             AMQPConnectorException,
-        ):
-            logger.error("CQRS couldn't be published: pk = {0} ({1}).{2}".format(
-                payload.pk, payload.cqrs_id, " Reconnect..." if retries else "",
-            ))
-
+            AssertionError,
+        ) as e:
             # in case of any error - close connection and try to reconnect
             cls.clean_connection()
 
-            if retries:
-                cls._produce_with_retries(payload, retries - 1)
+            base_log_message = "CQRS couldn't be published: pk = {0} ({1}).".format(
+                payload.pk, payload.cqrs_id,
+            )
+            if not retries:
+                logger.exception(base_log_message)
+                return
+
+            logger.warning('{0} Error: {1}. Reconnect...'.format(
+                base_log_message, e.__class__.__name__,
+            ))
+
+            cls._produce_with_retries(payload, retries - 1)
 
     @classmethod
     def _consume_message(cls, ch, method, properties, body, delay_queue):
         try:
             dct = ujson.loads(body)
         except ValueError:
             logger.error("CQRS couldn't be parsed: {0}.".format(body))
```

### Comparing `django-cqrs-2.4.9/dj_cqrs/utils.py` & `django_cqrs-2.5.0/dj_cqrs/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-#  Copyright © 2022 Ingram Micro Inc. All rights reserved.
+#  Copyright © 2023 Ingram Micro Inc. All rights reserved.
 
 import logging
 from datetime import date, datetime, timedelta
 from uuid import UUID
 
 from django.conf import settings
 from django.utils import timezone
```

