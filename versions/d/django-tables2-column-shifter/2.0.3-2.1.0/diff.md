# Comparing `tmp/django-tables2-column-shifter-2.0.3.tar.gz` & `tmp/django-tables2-column-shifter-2.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/django-tables2-column-shifter-2.0.3.tar", last modified: Wed Apr 14 20:07:15 2021, max compression
+gzip compressed data, was "django-tables2-column-shifter-2.1.0.tar", last modified: Thu Apr  6 14:28:37 2023, max compression
```

## Comparing `django-tables2-column-shifter-2.0.3.tar` & `django-tables2-column-shifter-2.1.0.tar`

### file list

```diff
@@ -1,56 +1,56 @@
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/
--rw-rw-r--   0 k2        (1000) k2        (1000)     1331 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/setup.py
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter.egg-info/
--rw-rw-r--   0 k2        (1000) k2        (1000)       34 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter.egg-info/requires.txt
--rw-rw-r--   0 k2        (1000) k2        (1000)     2126 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter.egg-info/SOURCES.txt
--rw-rw-r--   0 k2        (1000) k2        (1000)       30 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter.egg-info/top_level.txt
--rw-rw-r--   0 k2        (1000) k2        (1000)    13143 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter.egg-info/PKG-INFO
--rw-rw-r--   0 k2        (1000) k2        (1000)        1 2017-05-24 17:24:45.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter.egg-info/not-zip-safe
--rw-rw-r--   0 k2        (1000) k2        (1000)        1 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter.egg-info/dependency_links.txt
--rw-rw-r--   0 k2        (1000) k2        (1000)     2350 2021-04-14 19:59:54.000000 django-tables2-column-shifter-2.0.3/CHANGELOG.rst
--rw-rw-r--   0 k2        (1000) k2        (1000)     9964 2021-04-14 19:57:25.000000 django-tables2-column-shifter-2.0.3/README.rst
--rw-rw-r--   0 k2        (1000) k2        (1000)    13143 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/PKG-INFO
--rw-rw-r--   0 k2        (1000) k2        (1000)      231 2016-11-22 15:42:55.000000 django-tables2-column-shifter-2.0.3/MANIFEST.in
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pl/
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pl/LC_MESSAGES/
--rw-rw-r--   0 k2        (1000) k2        (1000)     1142 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.po
--rw-rw-r--   0 k2        (1000) k2        (1000)      713 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.mo
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pt_BR/
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/
--rw-rw-r--   0 k2        (1000) k2        (1000)     1021 2018-10-05 16:07:57.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.po
--rw-rw-r--   0 k2        (1000) k2        (1000)      600 2018-10-05 16:07:57.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.mo
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/el/
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/el/LC_MESSAGES/
--rw-rw-r--   0 k2        (1000) k2        (1000)      992 2018-10-05 16:07:57.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.po
--rw-rw-r--   0 k2        (1000) k2        (1000)      607 2018-10-05 16:07:57.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.mo
--rw-rw-r--   0 k2        (1000) k2        (1000)     2977 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tables.py
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/
--rw-rw-r--   0 k2        (1000) k2        (1000)      409 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/tables.py
--rw-rw-r--   0 k2        (1000) k2        (1000)      609 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/urls.py
--rw-rw-r--   0 k2        (1000) k2        (1000)     1042 2017-03-06 19:36:03.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/settings.py
--rw-rw-r--   0 k2        (1000) k2        (1000)     2302 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/views.py
--rw-r--r--   0 k2        (1000) k2        (1000)        0 2016-11-24 07:27:10.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/__init__.py
--rw-rw-r--   0 k2        (1000) k2        (1000)     7546 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/test_base.py
--rw-rw-r--   0 k2        (1000) k2        (1000)      755 2018-10-05 16:07:57.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/models.py
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/js/
--rw-rw-r--   0 k2        (1000) k2        (1000)     6504 2018-10-05 16:07:57.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.js
--rw-rw-r--   0 k2        (1000) k2        (1000)     1687 2018-10-05 16:07:57.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.min.js
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/img/
--rw-rw-r--   0 k2        (1000) k2        (1000)      349 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/img/uncheck.png
--rw-rw-r--   0 k2        (1000) k2        (1000)      847 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/img/loader.gif
--rw-rw-r--   0 k2        (1000) k2        (1000)      573 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/img/check.png
--rw-rw-r--   0 k2        (1000) k2        (1000)      274 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/img/cols.png
--rw-rw-r--   0 k2        (1000) k2        (1000)       68 2021-04-14 20:00:03.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/__init__.py
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/
-drwxrwxr-x   0 k2        (1000) k2        (1000)        0 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/
--rw-rw-r--   0 k2        (1000) k2        (1000)       62 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/table.html
--rw-rw-r--   0 k2        (1000) k2        (1000)     4782 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap5.html
--rw-rw-r--   0 k2        (1000) k2        (1000)     4598 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap2.html
--rw-rw-r--   0 k2        (1000) k2        (1000)     4599 2021-04-14 19:39:30.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap4.html
--rw-rw-r--   0 k2        (1000) k2        (1000)     4598 2018-10-05 16:07:57.000000 django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap3.html
--rw-rw-r--   0 k2        (1000) k2        (1000)      374 2021-04-14 20:07:15.000000 django-tables2-column-shifter-2.0.3/setup.cfg
--rw-rw-r--   0 k2        (1000) k2        (1000)     1570 2016-11-21 08:42:29.000000 django-tables2-column-shifter-2.0.3/LICENSE
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     2571 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/CHANGELOG.rst
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1570 2016-11-21 08:42:29.000000 django-tables2-column-shifter-2.1.0/LICENSE
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      231 2016-11-22 15:42:55.000000 django-tables2-column-shifter-2.1.0/MANIFEST.in
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)    11320 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/PKG-INFO
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)    10470 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/README.rst
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       68 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/__init__.py
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      607 2018-04-23 09:25:33.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.mo
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      992 2018-04-23 09:25:33.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.po
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      713 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.mo
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1142 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.po
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      600 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.mo
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1021 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.po
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      573 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/check.png
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      274 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/cols.png
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      847 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/loader.gif
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      349 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/uncheck.png
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     6504 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.js
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1687 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.min.js
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     3130 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tables.py
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     4886 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap2.html
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     4886 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap3.html
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     4887 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap4.html
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     5070 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap5.html
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       62 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/table.html
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/
+-rw-r--r--   0 grzegorz  (1000) grzegorz  (1000)        0 2016-11-24 07:27:10.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/__init__.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      755 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/models.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1093 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/settings.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      409 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/tables.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     9169 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/test_base.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      550 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/urls.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     2302 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/views.py
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)    11320 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/PKG-INFO
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     2126 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/SOURCES.txt
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)        1 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/dependency_links.txt
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)        1 2017-05-24 17:24:45.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/not-zip-safe
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       34 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/requires.txt
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       30 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/top_level.txt
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      374 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/setup.cfg
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1331 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/setup.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `django-tables2-column-shifter-2.0.3/setup.py` & `django-tables2-column-shifter-2.1.0/setup.py`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter.egg-info/SOURCES.txt` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter.egg-info/PKG-INFO` & `django-tables2-column-shifter-2.1.0/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,312 +1,325 @@
-Metadata-Version: 1.1
+Metadata-Version: 2.1
 Name: django-tables2-column-shifter
-Version: 2.0.3
+Version: 2.1.0
 Summary: Extension for django_tables2 can dynamically show or hide columns
 Home-page: https://github.com/djk2/django-tables2-column-shifter
 Author: Grzegorz Tężycki
 Author-email: grzegorz.tezycki@gmail.com
 License: BSD
-Description: django-tables2-column-shifter
-        ------------------------------
-        
-        
-        .. image:: https://badge.fury.io/py/django-tables2-column-shifter.svg
-            :target: https://badge.fury.io/py/django-tables2-column-shifter
-            :alt: Latest PyPI version
-        
-        
-        .. image:: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml/badge.svg?branch=master
-            :target: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml
-            :alt: GitHub Actions
-        
-        
-        .. image:: https://requires.io/github/djk2/django-tables2-column-shifter/requirements.svg?branch=master
-            :target: https://requires.io/github/djk2/django-tables2-column-shifter/requirements/?branch=master
-            :alt: Requirements Status
-        
-        
-        **About the app:**
-        Simple extension for django-tables2 to dynamically show or hide columns using jQuery.
-        Application uses web storage to store information whih columns are visible or not.
-        Using JQuery, Bootstrap3 or Bootstrap4 or Bootstrap5 and Django >=1.9.
-        
-        
-        **Warning** : - Since version 2.0 my extension works by default with bootstrap4.
-          I highly recommend to inherit explicite from tables class indicate on bootstrap version.
-          I.e if you use in your project bootstrap in version 5.
-          Your `Tables` classes should inherit from:
-          `django_tables2_column_shifter.tables.ColumnShiftTableBootstrap5`.
-        
-          Now you should inherit from:
-        
-          * for bootstrap2 - ColumnShiftTableBootstrap2,
-          * for bootstrap3 - ColumnShiftTableBootstrap3,
-          * for bootstrap4 - ColumnShiftTableBootstrap4,
-          * for bootstrap5 - ColumnShiftTableBootstrap5,
-        
-        **Tested by tox with:**
-        
-        * Python :3.6, 3.8
-        * Django : 1.9, 1.10, 1.11, 2.0, 2.1, 3.0, 3.1, 3.2, master
-        * django-tables2 : 1.5, 1.6, ..., 1.21, 2.0, 2.1, 2.2, 2.3, master
-        
-        **Supported:**
-        
-        * Django >= 1.9
-        * django-tables2 >= 1.5.0 (earlier version probably will be work but wasn't tested)
-        * **bootstrap2** / **bootstrap3** / **bootstrap4** / **bootstrap4.1.3** / **bootstrap5 beta3**
-        * **JQuery**
-        
-        **Supported locale:**
-        
-        * EN        - (English)
-        * PL        - (Polish)
-        * EL        - (Greek / Hellenic Republic)
-        * PT-BR     - (Portuguese - Brazilian)
-        
-        
-        More information about django-tables in here: https://django-tables2.readthedocs.io/
-        
-        
-        Screens:
-        ----------
-        
-        .. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr1.png
-            :alt: screen 1
-        
-        .. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr2.png
-            :alt: screen 2
-        
-        
-        How to Install:
-        ---------------
-        1. Install django-tables2-column-shifter using::
-        
-        
-                pip install django-tables2-column-shifter
-        
-            or
-        
-                pip install git+https://github.com/djk2/django-tables2-column-shifter
-        
-            or
-        
-                pip install django-tables2-column-shifter.zip
-        
-            or
-        
-                pip install django-tables2-column-shifter.tar.gz
-        
-        
-        2. Add ``django_tables2_column_shifter`` to your ``INSTALLED_APPS`` setting (after django_tables2) like this ::
-        
-            INSTALLED_APPS = [
-                ...,
-                'django_tables2',
-                'django_tables2_column_shifter',
-                ...,
-            ]
-        
-        3. Add path to js script: ``django_tables2_column_shifter.min.js`` in your base django template.
-           Script must be add after jquery.js and bootstrap.js and before </body> tag.
-           Draw attention to fact that beginning from version 4 of bootstrap,
-           the `Popper.js` is required to proper work of some of JS bootstrap scripts.
-           More about dependencies here:
-           https://getbootstrap.com/docs/4.0/getting-started/javascript/#dependencies
-        
-        
-          base.html::
-        
-            {% load static %}
-        
-            <body>
-                ...
-                ...
-                <script src="{% static "jquery.min.js" %}"></script> {# require #}
-                {# Popper is a dependency for bootstrap >= 4.0 #}
-                <script src="{% static "bootstrap/js/popper.min.js" %}"></script>
-                <script src="{% static "bootstrap/js/bootstrap.min.js" %}"></script>
-        
-                <script
-                    type="text/javascript"
-                    src="{% static "django_tables2_column_shifter/js/django_tables2_column_shifter.min.js" %}">
-                </script>
-            </body>
-        
-        
-        Usage:
-        ------
-        To use app, you must inherit your table class from ``django_tables2_column_shifter.tables.ColumnShiftTable``
-        
-          models.py - create ordinary model::
-        
-            from django.db import models
-        
-            class MyModel(models.Model):
-                first_name = models.CharField("First name", max_length=50)
-                last_name = models.CharField("Last name", max_length=50)
-        
-          tables.py - change inherit to one of: ColumnShiftTableBootstrap2,
-          ColumnShiftTableBootstrap3, ColumnShiftTableBootstrap4, ColumnShiftTableBootstrap5
-          (depends on which bootstrap version of bootstrap you are using)::
-        
-            from django_tables2_column_shifter.tables import (
-                ColumnShiftTableBootstrap2, # If you use bootstrap2
-                ColumnShiftTableBootstrap3, # If you use bootstrap3
-                ColumnShiftTableBootstrap4, # If you use bootstrap4
-                ColumnShiftTableBootstrap5, # If you use bootstrap5
-            )
-            from app.models import MyModel
-        
-            # By default you probably inherit from django_table2.Table
-            # Change inherit to ColumnShiftTableBootstrap4
-            # if you use bootstrap4
-            class MyModelTable(ColumnShiftTableBootstrap4):
-                class Meta:
-                    model = MyModel
-        
-            # or if you use bootstrap5
-            class MyModelTable(ColumnShiftTableBootstrap5):
-                class Meta:
-                    model = MyModel
-        
-        
-          views.py - In your view, nothing changes::
-        
-            from .tables import MyModelTable
-            from .models import MyModel
-        
-            def simple_list(request):
-                queryset = MyModel.objects.all()
-                table = MyModelTable(queryset)
-                return render(request, 'template.html', {'table': table})
-        
-          template.html - use default render_table tag to display table object (using bootstrap3 / bootstrap4 / bootstrap5)::
-        
-            {% extends "base.html" %}
-            {% load django_tables2 %}
-            {% render_table table %}
-        
-        
-        
-        JS API:
-        -------
-        To retrieve the invisible columns you can use the ``$.django_tables2_column_shifter_hidden()`` js API.
-        You can either pass the 0-based index of the table in the page (i.e use ``$.django_tables2_column_shifter_hidden(1)``
-        to get the hidden columns for the 2nd table in the page) or just use it without parameters to retrieve the hidden columns
-        for the first table. This API returns an array with the invisible column names.
-        
-        These columns can then be used when you want to export only the visible columns,
-        ie  when the user clicks on the export button it would append an ``&excluded_columns=col1,col2``
-        to the export button's ``href`` which would then be used by the django-tables2 ``TableExporter``
-        (http://django-tables2.readthedocs.io/en/latest/pages/export.html#excluding-columns) to exclude
-        these cols, i.e something like
-        
-            exporter = TableExport('csv', table, exclude_columns=self.request.GET.get('excluded_columns').split(',))
-        
-        
-        
-        Bootstrap2 (support for old projects):
-        --------------------------------------
-        If you use Bootstrap v2 in your project then table class has to inherit from `ColumnShiftTableBootstrap2`
-        imported from `django_tables2_column_shifter.tables`.
-        
-        Bootstrap3 (support for old projects):
-        --------------------------------------
-        If you use Bootstrap v3 in your project then table class has to inherit from `ColumnShiftTableBootstrap3`
-        imported from `django_tables2_column_shifter.tables`.
-        
-        Bootstrap4 :
-        --------------------------------------
-        If you use Bootstrap v4 in your project then table class has to inherit from `ColumnShiftTableBootstrap4`
-        imported from `django_tables2_column_shifter.tables`.
-        
-        Bootstrap5:
-        --------------------------------------
-        If you use Bootstrap v5 in your project then table class has to inherit from `ColumnShiftTableBootstrap5`
-        imported from `django_tables2_column_shifter.tables`.
-        
-        
-        
-        Warnings:
-        ----------
-        
-        - **Warning** : - If you use {% render_table %} tag with queryset (not table class instance),
-          django-tables2-column-shifter will not be work. Queryset does not have ``template`` attribute::
-        
-            {% load django_tables2 %}
-            {% render_table queryset %} {# not work #}
-        
-        
-        - **Warning** : - If you use a different template than ``django_tables2_column_shifter/bootstrap*.html``
-          to render your table, probably django-tables2-column-shifter will not be work.
-          Your custom template should inherit from ``django_tables2_column_shifter/bootstrap*.html``
-        
-        - **Warning** : - Since version 2.0 the default template is not used for Table class.
-          Moreover template ``django_tables2_column_shifter/table.html`` by default inherit from
-          ``django_tables2_column_shifter/bootstrap4.html``
-        
-        
-        
-        
-        Customizing:
-        -------------
-        1. If you use more then one instance of the same Table class, you should use a different prefix for each instance::
-        
-            tab1 = MyModelTable(queryset, prefix='tab1')
-            tab2 = MyModelTable(queryset, prefix='tab2')
-            tab3 = MyModelTable(queryset, prefix='tab3')
-        
-        2. To disable shifter mechanism - set ``False`` to ``shift_table_column`` in your table class (default value is True)::
-        
-            class MyModelTable(ColumnShiftTableBootstrap5):
-               shift_table_column = False
-               ...
-        
-        
-        3. By default, all columns from sequence are visible, if you want limit visible columns,
-           override method ``get_column_default_show(self)`` like that::
-        
-            class MyModelTable(ColumnShiftTableBootstrap5):
-                def get_column_default_show(self):
-                    self.column_default_show = ['column1', 'column2']
-                    return super(MyModelTable, self).get_column_default_show()
-        
-        
-        Run demo:
-        ---------
-        1. Download or clone project from `https://github.com/djk2/django-tables2-column-shifter`::
-        
-            git clone https://github.com/djk2/django-tables2-column-shifter.git
-        
-        2. Go to testproject directory::
-        
-            cd django-tables2-column-shifter/testproject
-        
-        3. Install requirements::
-        
-            pip install -r requirements.txt
-        
-        4. Run django developing server::
-        
-            python manage.py runserver
-        
-        
-        Links:
-        --------
-        - `Django documentation <https://docs.djangoproject.com/en/dev/>`_
-        - `django-tables2 documentation <https://django-tables2.readthedocs.io/en/latest/>`_
-        
 Keywords: django_tables2 django columns
-Platform: UNKNOWN
 Classifier: Environment :: Web Environment
 Classifier: Framework :: Django
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 2
 Classifier: Programming Language :: Python :: 2.7
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Topic :: Utilities
+License-File: LICENSE
+
+django-tables2-column-shifter
+------------------------------
+
+
+.. image:: https://badge.fury.io/py/django-tables2-column-shifter.svg
+    :target: https://badge.fury.io/py/django-tables2-column-shifter
+    :alt: Latest PyPI version
+
+
+.. image:: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml/badge.svg?branch=master
+    :target: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml
+    :alt: GitHub Actions
+
+
+.. image:: https://requires.io/github/djk2/django-tables2-column-shifter/requirements.svg?branch=master
+    :target: https://requires.io/github/djk2/django-tables2-column-shifter/requirements/?branch=master
+    :alt: Requirements Status
+
+
+**About the app:**
+Simple extension for django-tables2 to dynamically show or hide columns using jQuery.
+Application uses web storage to store information whih columns are visible or not.
+Using JQuery, Bootstrap3 or Bootstrap4 or Bootstrap5 and Django >=1.9.
+
+
+**Warning** : - Since version 2.0 my extension works by default with bootstrap4.
+  I highly recommend to inherit explicite from tables class indicate on bootstrap version.
+  I.e if you use in your project bootstrap in version 5.
+  Your `Table` classes should inherit from:
+  `django_tables2_column_shifter.tables.ColumnShiftTableBootstrap5`.
+
+  Now you should inherit from:
+
+  * for bootstrap2 - ColumnShiftTableBootstrap2,
+  * for bootstrap3 - ColumnShiftTableBootstrap3,
+  * for bootstrap4 - ColumnShiftTableBootstrap4,
+  * for bootstrap5 - ColumnShiftTableBootstrap5,
+
+**Tested by tox with:**
+
+* Python :3.6, 3.8, 3.10
+* Django : 1.9, 1.10, 1.11, 2.0, 2.1, 3.0, 3.1, 3.2, 4.0, 4.2, master
+* django-tables2 : 1.15, ..., 1.21, 2.0, 2.1, 2.2, 2.3, 2.5, master
+
+**Supported:**
+
+* Django >= 1.9
+* django-tables2 >= 1.15 (earlier version probably will work but wasn't tested)
+* **bootstrap2** / **bootstrap3** / **bootstrap4** / **bootstrap4.1.3** / **bootstrap5 beta3**
+* **JQuery**
+
+**Supported locale:**
+
+* EN        - (English)
+* PL        - (Polish)
+* EL        - (Greek / Hellenic Republic)
+* PT-BR     - (Portuguese - Brazilian)
+
+
+More information about django-tables in here: https://django-tables2.readthedocs.io/
+
+
+Screens:
+----------
+
+.. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr1.png
+    :alt: screen 1
+
+.. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr2.png
+    :alt: screen 2
+
+
+How to Install:
+---------------
+1. Install django-tables2-column-shifter using::
+
+
+        pip install django-tables2-column-shifter
+
+    or
+
+        pip install git+https://github.com/djk2/django-tables2-column-shifter
+
+    or
+
+        pip install django-tables2-column-shifter.zip
+
+    or
+
+        pip install django-tables2-column-shifter.tar.gz
+
+
+2. Add ``django_tables2_column_shifter`` to your ``INSTALLED_APPS`` setting (after django_tables2) like this ::
+
+    INSTALLED_APPS = [
+        ...,
+        'django_tables2',
+        'django_tables2_column_shifter',
+        ...,
+    ]
+
+3. Add path to js script: ``django_tables2_column_shifter.min.js`` in your base django template.
+   Script must be add after jquery.js and bootstrap.js and before </body> tag.
+   Draw attention to fact that beginning from version 4 of bootstrap,
+   the `Popper.js` is required to proper work of some of JS bootstrap scripts.
+   More about dependencies here:
+   https://getbootstrap.com/docs/4.0/getting-started/javascript/#dependencies
+
+
+  base.html::
+
+    {% load static %}
+
+    <body>
+        ...
+        ...
+        <script src="{% static "jquery.min.js" %}"></script> {# require #}
+        {# Popper is a dependency for bootstrap >= 4.0 #}
+        <script src="{% static "bootstrap/js/popper.min.js" %}"></script>
+        <script src="{% static "bootstrap/js/bootstrap.min.js" %}"></script>
+
+        <script
+            type="text/javascript"
+            src="{% static "django_tables2_column_shifter/js/django_tables2_column_shifter.min.js" %}">
+        </script>
+    </body>
+
+
+Usage:
+------
+To use app, you must inherit your table class from ``django_tables2_column_shifter.tables.ColumnShiftTable``
+
+  models.py - create ordinary model::
+
+    from django.db import models
+
+    class MyModel(models.Model):
+        first_name = models.CharField("First name", max_length=50)
+        last_name = models.CharField("Last name", max_length=50)
+
+  tables.py - change inherit to one of: ColumnShiftTableBootstrap2,
+  ColumnShiftTableBootstrap3, ColumnShiftTableBootstrap4, ColumnShiftTableBootstrap5
+  (depends on which bootstrap version of bootstrap you are using)::
+
+    from django_tables2_column_shifter.tables import (
+        ColumnShiftTableBootstrap2, # If you use bootstrap2
+        ColumnShiftTableBootstrap3, # If you use bootstrap3
+        ColumnShiftTableBootstrap4, # If you use bootstrap4
+        ColumnShiftTableBootstrap5, # If you use bootstrap5
+    )
+    from app.models import MyModel
+
+    # By default you probably inherit from django_table2.Table
+    # Change inherit to ColumnShiftTableBootstrap4
+    # if you use bootstrap4
+    class MyModelTable(ColumnShiftTableBootstrap4):
+        class Meta:
+            model = MyModel
+
+    # or if you use bootstrap5
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        class Meta:
+            model = MyModel
+
+
+  views.py - In your view, nothing changes::
+
+    from .tables import MyModelTable
+    from .models import MyModel
+
+    def simple_list(request):
+        queryset = MyModel.objects.all()
+        table = MyModelTable(queryset)
+        return render(request, 'template.html', {'table': table})
+
+  template.html - use default render_table tag to display table object (using bootstrap3 / bootstrap4 / bootstrap5)::
+
+    {% extends "base.html" %}
+    {% load django_tables2 %}
+    {% render_table table %}
+
+
+
+JS API:
+-------
+To retrieve the invisible columns you can use the ``$.django_tables2_column_shifter_hidden()`` js API.
+You can either pass the 0-based index of the table in the page (i.e use ``$.django_tables2_column_shifter_hidden(1)``
+to get the hidden columns for the 2nd table in the page) or just use it without parameters to retrieve the hidden columns
+for the first table. This API returns an array with the invisible column names.
+
+These columns can then be used when you want to export only the visible columns,
+ie  when the user clicks on the export button it would append an ``&excluded_columns=col1,col2``
+to the export button's ``href`` which would then be used by the django-tables2 ``TableExporter``
+(http://django-tables2.readthedocs.io/en/latest/pages/export.html#excluding-columns) to exclude
+these cols, i.e something like
+
+    exporter = TableExport('csv', table, exclude_columns=self.request.GET.get('excluded_columns').split(',))
+
+
+
+Bootstrap2 (support for old projects):
+--------------------------------------
+If you use Bootstrap v2 in your project then table class has to inherit from `ColumnShiftTableBootstrap2`
+imported from `django_tables2_column_shifter.tables`.
+
+Bootstrap3 (support for old projects):
+--------------------------------------
+If you use Bootstrap v3 in your project then table class has to inherit from `ColumnShiftTableBootstrap3`
+imported from `django_tables2_column_shifter.tables`.
+
+Bootstrap4 :
+--------------------------------------
+If you use Bootstrap v4 in your project then table class has to inherit from `ColumnShiftTableBootstrap4`
+imported from `django_tables2_column_shifter.tables`.
+
+Bootstrap5:
+--------------------------------------
+If you use Bootstrap v5 in your project then table class has to inherit from `ColumnShiftTableBootstrap5`
+imported from `django_tables2_column_shifter.tables`.
+
+
+
+Warnings:
+----------
+
+- **Warning** : - If you use {% render_table %} tag with queryset (not table class instance),
+  django-tables2-column-shifter will not be work. Queryset does not have ``template`` attribute::
+
+    {% load django_tables2 %}
+    {% render_table queryset %} {# not work #}
+
+
+- **Warning** : - If you use a different template than ``django_tables2_column_shifter/bootstrap*.html``
+  to render your table, probably django-tables2-column-shifter will not be work.
+  Your custom template should inherit from ``django_tables2_column_shifter/bootstrap*.html``
+
+- **Warning** : - Since version 2.0 the default template is not used for Table class.
+  Moreover template ``django_tables2_column_shifter/table.html`` by default inherit from
+  ``django_tables2_column_shifter/bootstrap4.html``
+
+
+
+
+Customizing:
+-------------
+1. If you use more then one instance of the same Table class, you should use a different prefix for each instance::
+
+    tab1 = MyModelTable(queryset, prefix='tab1')
+    tab2 = MyModelTable(queryset, prefix='tab2')
+    tab3 = MyModelTable(queryset, prefix='tab3')
+
+2. To disable shifter mechanism - set ``False`` to ``shift_table_column`` in your table class (default value is True)::
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+       shift_table_column = False
+       ...
+
+
+3. By default, all columns from sequence are visible, if you want limit visible columns,
+   override method ``get_column_default_show(self)`` like that::
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        def get_column_default_show(self):
+            self.column_default_show = ['column1', 'column2']
+            return super(MyModelTable, self).get_column_default_show()
+
+4. By default, all columns from sequence are visible, if you want exclude some colmumns and
+   block ability to manipulate then, use: ``column_excluded``
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        column_excluded = ['ex_column1', 'ex_column2']
+
+    or
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        def get_column_excluded(self):
+            self.column_excluded = ['ex_column1', 'ex_column2']
+            return super(MyModelTable, self).get_column_excluded()
+
+
+Run demo:
+---------
+1. Download or clone project from `https://github.com/djk2/django-tables2-column-shifter`::
+
+    git clone https://github.com/djk2/django-tables2-column-shifter.git
+
+2. Go to testproject directory::
+
+    cd django-tables2-column-shifter/testproject
+
+3. Install requirements::
+
+    pip install -r requirements.txt
+
+4. Run django developing server::
+
+    python manage.py runserver
+
+
+Links:
+--------
+- `Django documentation <https://docs.djangoproject.com/en/dev/>`_
+- `django-tables2 documentation <https://django-tables2.readthedocs.io/en/latest/>`_
```

### Comparing `django-tables2-column-shifter-2.0.3/CHANGELOG.rst` & `django-tables2-column-shifter-2.1.0/CHANGELOG.rst`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,19 @@
 CHANGELOG
 ===========
 
+v. 2.1.0
+--------
+
+    * Add possibility to exclude columns from shifting via `column_excluded`
+    * Support for Python 3.10
+    * Support for Django 4.0
+    * Support for Django 4.2
+    * Support django-tables2 v2.5.3
+
 v. 2.0.3
 --------
 
     * Fix small gaps for documentation in README.rst file
 
 v. 2.0.2
 --------
```

### Comparing `django-tables2-column-shifter-2.0.3/README.rst` & `django-tables2-column-shifter-2.1.0/README.rst`

 * *Files 5% similar despite different names*

```diff
@@ -22,34 +22,34 @@
 Application uses web storage to store information whih columns are visible or not.
 Using JQuery, Bootstrap3 or Bootstrap4 or Bootstrap5 and Django >=1.9.
 
 
 **Warning** : - Since version 2.0 my extension works by default with bootstrap4.
   I highly recommend to inherit explicite from tables class indicate on bootstrap version.
   I.e if you use in your project bootstrap in version 5.
-  Your `Tables` classes should inherit from:
+  Your `Table` classes should inherit from:
   `django_tables2_column_shifter.tables.ColumnShiftTableBootstrap5`.
 
   Now you should inherit from:
 
   * for bootstrap2 - ColumnShiftTableBootstrap2,
   * for bootstrap3 - ColumnShiftTableBootstrap3,
   * for bootstrap4 - ColumnShiftTableBootstrap4,
   * for bootstrap5 - ColumnShiftTableBootstrap5,
 
 **Tested by tox with:**
 
-* Python :3.6, 3.8
-* Django : 1.9, 1.10, 1.11, 2.0, 2.1, 3.0, 3.1, 3.2, master
-* django-tables2 : 1.5, 1.6, ..., 1.21, 2.0, 2.1, 2.2, 2.3, master
+* Python :3.6, 3.8, 3.10
+* Django : 1.9, 1.10, 1.11, 2.0, 2.1, 3.0, 3.1, 3.2, 4.0, 4.2, master
+* django-tables2 : 1.15, ..., 1.21, 2.0, 2.1, 2.2, 2.3, 2.5, master
 
 **Supported:**
 
 * Django >= 1.9
-* django-tables2 >= 1.5.0 (earlier version probably will be work but wasn't tested)
+* django-tables2 >= 1.15 (earlier version probably will work but wasn't tested)
 * **bootstrap2** / **bootstrap3** / **bootstrap4** / **bootstrap4.1.3** / **bootstrap5 beta3**
 * **JQuery**
 
 **Supported locale:**
 
 * EN        - (English)
 * PL        - (Polish)
@@ -260,14 +260,27 @@
    override method ``get_column_default_show(self)`` like that::
 
     class MyModelTable(ColumnShiftTableBootstrap5):
         def get_column_default_show(self):
             self.column_default_show = ['column1', 'column2']
             return super(MyModelTable, self).get_column_default_show()
 
+4. By default, all columns from sequence are visible, if you want exclude some colmumns and
+   block ability to manipulate then, use: ``column_excluded``
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        column_excluded = ['ex_column1', 'ex_column2']
+
+    or
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        def get_column_excluded(self):
+            self.column_excluded = ['ex_column1', 'ex_column2']
+            return super(MyModelTable, self).get_column_excluded()
+
 
 Run demo:
 ---------
 1. Download or clone project from `https://github.com/djk2/django-tables2-column-shifter`::
 
     git clone https://github.com/djk2/django-tables2-column-shifter.git
```

### Comparing `django-tables2-column-shifter-2.0.3/PKG-INFO` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,312 +1,325 @@
-Metadata-Version: 1.1
+Metadata-Version: 2.1
 Name: django-tables2-column-shifter
-Version: 2.0.3
+Version: 2.1.0
 Summary: Extension for django_tables2 can dynamically show or hide columns
 Home-page: https://github.com/djk2/django-tables2-column-shifter
 Author: Grzegorz Tężycki
 Author-email: grzegorz.tezycki@gmail.com
 License: BSD
-Description: django-tables2-column-shifter
-        ------------------------------
-        
-        
-        .. image:: https://badge.fury.io/py/django-tables2-column-shifter.svg
-            :target: https://badge.fury.io/py/django-tables2-column-shifter
-            :alt: Latest PyPI version
-        
-        
-        .. image:: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml/badge.svg?branch=master
-            :target: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml
-            :alt: GitHub Actions
-        
-        
-        .. image:: https://requires.io/github/djk2/django-tables2-column-shifter/requirements.svg?branch=master
-            :target: https://requires.io/github/djk2/django-tables2-column-shifter/requirements/?branch=master
-            :alt: Requirements Status
-        
-        
-        **About the app:**
-        Simple extension for django-tables2 to dynamically show or hide columns using jQuery.
-        Application uses web storage to store information whih columns are visible or not.
-        Using JQuery, Bootstrap3 or Bootstrap4 or Bootstrap5 and Django >=1.9.
-        
-        
-        **Warning** : - Since version 2.0 my extension works by default with bootstrap4.
-          I highly recommend to inherit explicite from tables class indicate on bootstrap version.
-          I.e if you use in your project bootstrap in version 5.
-          Your `Tables` classes should inherit from:
-          `django_tables2_column_shifter.tables.ColumnShiftTableBootstrap5`.
-        
-          Now you should inherit from:
-        
-          * for bootstrap2 - ColumnShiftTableBootstrap2,
-          * for bootstrap3 - ColumnShiftTableBootstrap3,
-          * for bootstrap4 - ColumnShiftTableBootstrap4,
-          * for bootstrap5 - ColumnShiftTableBootstrap5,
-        
-        **Tested by tox with:**
-        
-        * Python :3.6, 3.8
-        * Django : 1.9, 1.10, 1.11, 2.0, 2.1, 3.0, 3.1, 3.2, master
-        * django-tables2 : 1.5, 1.6, ..., 1.21, 2.0, 2.1, 2.2, 2.3, master
-        
-        **Supported:**
-        
-        * Django >= 1.9
-        * django-tables2 >= 1.5.0 (earlier version probably will be work but wasn't tested)
-        * **bootstrap2** / **bootstrap3** / **bootstrap4** / **bootstrap4.1.3** / **bootstrap5 beta3**
-        * **JQuery**
-        
-        **Supported locale:**
-        
-        * EN        - (English)
-        * PL        - (Polish)
-        * EL        - (Greek / Hellenic Republic)
-        * PT-BR     - (Portuguese - Brazilian)
-        
-        
-        More information about django-tables in here: https://django-tables2.readthedocs.io/
-        
-        
-        Screens:
-        ----------
-        
-        .. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr1.png
-            :alt: screen 1
-        
-        .. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr2.png
-            :alt: screen 2
-        
-        
-        How to Install:
-        ---------------
-        1. Install django-tables2-column-shifter using::
-        
-        
-                pip install django-tables2-column-shifter
-        
-            or
-        
-                pip install git+https://github.com/djk2/django-tables2-column-shifter
-        
-            or
-        
-                pip install django-tables2-column-shifter.zip
-        
-            or
-        
-                pip install django-tables2-column-shifter.tar.gz
-        
-        
-        2. Add ``django_tables2_column_shifter`` to your ``INSTALLED_APPS`` setting (after django_tables2) like this ::
-        
-            INSTALLED_APPS = [
-                ...,
-                'django_tables2',
-                'django_tables2_column_shifter',
-                ...,
-            ]
-        
-        3. Add path to js script: ``django_tables2_column_shifter.min.js`` in your base django template.
-           Script must be add after jquery.js and bootstrap.js and before </body> tag.
-           Draw attention to fact that beginning from version 4 of bootstrap,
-           the `Popper.js` is required to proper work of some of JS bootstrap scripts.
-           More about dependencies here:
-           https://getbootstrap.com/docs/4.0/getting-started/javascript/#dependencies
-        
-        
-          base.html::
-        
-            {% load static %}
-        
-            <body>
-                ...
-                ...
-                <script src="{% static "jquery.min.js" %}"></script> {# require #}
-                {# Popper is a dependency for bootstrap >= 4.0 #}
-                <script src="{% static "bootstrap/js/popper.min.js" %}"></script>
-                <script src="{% static "bootstrap/js/bootstrap.min.js" %}"></script>
-        
-                <script
-                    type="text/javascript"
-                    src="{% static "django_tables2_column_shifter/js/django_tables2_column_shifter.min.js" %}">
-                </script>
-            </body>
-        
-        
-        Usage:
-        ------
-        To use app, you must inherit your table class from ``django_tables2_column_shifter.tables.ColumnShiftTable``
-        
-          models.py - create ordinary model::
-        
-            from django.db import models
-        
-            class MyModel(models.Model):
-                first_name = models.CharField("First name", max_length=50)
-                last_name = models.CharField("Last name", max_length=50)
-        
-          tables.py - change inherit to one of: ColumnShiftTableBootstrap2,
-          ColumnShiftTableBootstrap3, ColumnShiftTableBootstrap4, ColumnShiftTableBootstrap5
-          (depends on which bootstrap version of bootstrap you are using)::
-        
-            from django_tables2_column_shifter.tables import (
-                ColumnShiftTableBootstrap2, # If you use bootstrap2
-                ColumnShiftTableBootstrap3, # If you use bootstrap3
-                ColumnShiftTableBootstrap4, # If you use bootstrap4
-                ColumnShiftTableBootstrap5, # If you use bootstrap5
-            )
-            from app.models import MyModel
-        
-            # By default you probably inherit from django_table2.Table
-            # Change inherit to ColumnShiftTableBootstrap4
-            # if you use bootstrap4
-            class MyModelTable(ColumnShiftTableBootstrap4):
-                class Meta:
-                    model = MyModel
-        
-            # or if you use bootstrap5
-            class MyModelTable(ColumnShiftTableBootstrap5):
-                class Meta:
-                    model = MyModel
-        
-        
-          views.py - In your view, nothing changes::
-        
-            from .tables import MyModelTable
-            from .models import MyModel
-        
-            def simple_list(request):
-                queryset = MyModel.objects.all()
-                table = MyModelTable(queryset)
-                return render(request, 'template.html', {'table': table})
-        
-          template.html - use default render_table tag to display table object (using bootstrap3 / bootstrap4 / bootstrap5)::
-        
-            {% extends "base.html" %}
-            {% load django_tables2 %}
-            {% render_table table %}
-        
-        
-        
-        JS API:
-        -------
-        To retrieve the invisible columns you can use the ``$.django_tables2_column_shifter_hidden()`` js API.
-        You can either pass the 0-based index of the table in the page (i.e use ``$.django_tables2_column_shifter_hidden(1)``
-        to get the hidden columns for the 2nd table in the page) or just use it without parameters to retrieve the hidden columns
-        for the first table. This API returns an array with the invisible column names.
-        
-        These columns can then be used when you want to export only the visible columns,
-        ie  when the user clicks on the export button it would append an ``&excluded_columns=col1,col2``
-        to the export button's ``href`` which would then be used by the django-tables2 ``TableExporter``
-        (http://django-tables2.readthedocs.io/en/latest/pages/export.html#excluding-columns) to exclude
-        these cols, i.e something like
-        
-            exporter = TableExport('csv', table, exclude_columns=self.request.GET.get('excluded_columns').split(',))
-        
-        
-        
-        Bootstrap2 (support for old projects):
-        --------------------------------------
-        If you use Bootstrap v2 in your project then table class has to inherit from `ColumnShiftTableBootstrap2`
-        imported from `django_tables2_column_shifter.tables`.
-        
-        Bootstrap3 (support for old projects):
-        --------------------------------------
-        If you use Bootstrap v3 in your project then table class has to inherit from `ColumnShiftTableBootstrap3`
-        imported from `django_tables2_column_shifter.tables`.
-        
-        Bootstrap4 :
-        --------------------------------------
-        If you use Bootstrap v4 in your project then table class has to inherit from `ColumnShiftTableBootstrap4`
-        imported from `django_tables2_column_shifter.tables`.
-        
-        Bootstrap5:
-        --------------------------------------
-        If you use Bootstrap v5 in your project then table class has to inherit from `ColumnShiftTableBootstrap5`
-        imported from `django_tables2_column_shifter.tables`.
-        
-        
-        
-        Warnings:
-        ----------
-        
-        - **Warning** : - If you use {% render_table %} tag with queryset (not table class instance),
-          django-tables2-column-shifter will not be work. Queryset does not have ``template`` attribute::
-        
-            {% load django_tables2 %}
-            {% render_table queryset %} {# not work #}
-        
-        
-        - **Warning** : - If you use a different template than ``django_tables2_column_shifter/bootstrap*.html``
-          to render your table, probably django-tables2-column-shifter will not be work.
-          Your custom template should inherit from ``django_tables2_column_shifter/bootstrap*.html``
-        
-        - **Warning** : - Since version 2.0 the default template is not used for Table class.
-          Moreover template ``django_tables2_column_shifter/table.html`` by default inherit from
-          ``django_tables2_column_shifter/bootstrap4.html``
-        
-        
-        
-        
-        Customizing:
-        -------------
-        1. If you use more then one instance of the same Table class, you should use a different prefix for each instance::
-        
-            tab1 = MyModelTable(queryset, prefix='tab1')
-            tab2 = MyModelTable(queryset, prefix='tab2')
-            tab3 = MyModelTable(queryset, prefix='tab3')
-        
-        2. To disable shifter mechanism - set ``False`` to ``shift_table_column`` in your table class (default value is True)::
-        
-            class MyModelTable(ColumnShiftTableBootstrap5):
-               shift_table_column = False
-               ...
-        
-        
-        3. By default, all columns from sequence are visible, if you want limit visible columns,
-           override method ``get_column_default_show(self)`` like that::
-        
-            class MyModelTable(ColumnShiftTableBootstrap5):
-                def get_column_default_show(self):
-                    self.column_default_show = ['column1', 'column2']
-                    return super(MyModelTable, self).get_column_default_show()
-        
-        
-        Run demo:
-        ---------
-        1. Download or clone project from `https://github.com/djk2/django-tables2-column-shifter`::
-        
-            git clone https://github.com/djk2/django-tables2-column-shifter.git
-        
-        2. Go to testproject directory::
-        
-            cd django-tables2-column-shifter/testproject
-        
-        3. Install requirements::
-        
-            pip install -r requirements.txt
-        
-        4. Run django developing server::
-        
-            python manage.py runserver
-        
-        
-        Links:
-        --------
-        - `Django documentation <https://docs.djangoproject.com/en/dev/>`_
-        - `django-tables2 documentation <https://django-tables2.readthedocs.io/en/latest/>`_
-        
 Keywords: django_tables2 django columns
-Platform: UNKNOWN
 Classifier: Environment :: Web Environment
 Classifier: Framework :: Django
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 2
 Classifier: Programming Language :: Python :: 2.7
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Topic :: Utilities
+License-File: LICENSE
+
+django-tables2-column-shifter
+------------------------------
+
+
+.. image:: https://badge.fury.io/py/django-tables2-column-shifter.svg
+    :target: https://badge.fury.io/py/django-tables2-column-shifter
+    :alt: Latest PyPI version
+
+
+.. image:: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml/badge.svg?branch=master
+    :target: https://github.com/djk2/django-tables2-column-shifter/actions/workflows/tests.yaml
+    :alt: GitHub Actions
+
+
+.. image:: https://requires.io/github/djk2/django-tables2-column-shifter/requirements.svg?branch=master
+    :target: https://requires.io/github/djk2/django-tables2-column-shifter/requirements/?branch=master
+    :alt: Requirements Status
+
+
+**About the app:**
+Simple extension for django-tables2 to dynamically show or hide columns using jQuery.
+Application uses web storage to store information whih columns are visible or not.
+Using JQuery, Bootstrap3 or Bootstrap4 or Bootstrap5 and Django >=1.9.
+
+
+**Warning** : - Since version 2.0 my extension works by default with bootstrap4.
+  I highly recommend to inherit explicite from tables class indicate on bootstrap version.
+  I.e if you use in your project bootstrap in version 5.
+  Your `Table` classes should inherit from:
+  `django_tables2_column_shifter.tables.ColumnShiftTableBootstrap5`.
+
+  Now you should inherit from:
+
+  * for bootstrap2 - ColumnShiftTableBootstrap2,
+  * for bootstrap3 - ColumnShiftTableBootstrap3,
+  * for bootstrap4 - ColumnShiftTableBootstrap4,
+  * for bootstrap5 - ColumnShiftTableBootstrap5,
+
+**Tested by tox with:**
+
+* Python :3.6, 3.8, 3.10
+* Django : 1.9, 1.10, 1.11, 2.0, 2.1, 3.0, 3.1, 3.2, 4.0, 4.2, master
+* django-tables2 : 1.15, ..., 1.21, 2.0, 2.1, 2.2, 2.3, 2.5, master
+
+**Supported:**
+
+* Django >= 1.9
+* django-tables2 >= 1.15 (earlier version probably will work but wasn't tested)
+* **bootstrap2** / **bootstrap3** / **bootstrap4** / **bootstrap4.1.3** / **bootstrap5 beta3**
+* **JQuery**
+
+**Supported locale:**
+
+* EN        - (English)
+* PL        - (Polish)
+* EL        - (Greek / Hellenic Republic)
+* PT-BR     - (Portuguese - Brazilian)
+
+
+More information about django-tables in here: https://django-tables2.readthedocs.io/
+
+
+Screens:
+----------
+
+.. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr1.png
+    :alt: screen 1
+
+.. image:: https://raw.githubusercontent.com/djk2/django-tables2-column-shifter/master/doc/static/scr2.png
+    :alt: screen 2
+
+
+How to Install:
+---------------
+1. Install django-tables2-column-shifter using::
+
+
+        pip install django-tables2-column-shifter
+
+    or
+
+        pip install git+https://github.com/djk2/django-tables2-column-shifter
+
+    or
+
+        pip install django-tables2-column-shifter.zip
+
+    or
+
+        pip install django-tables2-column-shifter.tar.gz
+
+
+2. Add ``django_tables2_column_shifter`` to your ``INSTALLED_APPS`` setting (after django_tables2) like this ::
+
+    INSTALLED_APPS = [
+        ...,
+        'django_tables2',
+        'django_tables2_column_shifter',
+        ...,
+    ]
+
+3. Add path to js script: ``django_tables2_column_shifter.min.js`` in your base django template.
+   Script must be add after jquery.js and bootstrap.js and before </body> tag.
+   Draw attention to fact that beginning from version 4 of bootstrap,
+   the `Popper.js` is required to proper work of some of JS bootstrap scripts.
+   More about dependencies here:
+   https://getbootstrap.com/docs/4.0/getting-started/javascript/#dependencies
+
+
+  base.html::
+
+    {% load static %}
+
+    <body>
+        ...
+        ...
+        <script src="{% static "jquery.min.js" %}"></script> {# require #}
+        {# Popper is a dependency for bootstrap >= 4.0 #}
+        <script src="{% static "bootstrap/js/popper.min.js" %}"></script>
+        <script src="{% static "bootstrap/js/bootstrap.min.js" %}"></script>
+
+        <script
+            type="text/javascript"
+            src="{% static "django_tables2_column_shifter/js/django_tables2_column_shifter.min.js" %}">
+        </script>
+    </body>
+
+
+Usage:
+------
+To use app, you must inherit your table class from ``django_tables2_column_shifter.tables.ColumnShiftTable``
+
+  models.py - create ordinary model::
+
+    from django.db import models
+
+    class MyModel(models.Model):
+        first_name = models.CharField("First name", max_length=50)
+        last_name = models.CharField("Last name", max_length=50)
+
+  tables.py - change inherit to one of: ColumnShiftTableBootstrap2,
+  ColumnShiftTableBootstrap3, ColumnShiftTableBootstrap4, ColumnShiftTableBootstrap5
+  (depends on which bootstrap version of bootstrap you are using)::
+
+    from django_tables2_column_shifter.tables import (
+        ColumnShiftTableBootstrap2, # If you use bootstrap2
+        ColumnShiftTableBootstrap3, # If you use bootstrap3
+        ColumnShiftTableBootstrap4, # If you use bootstrap4
+        ColumnShiftTableBootstrap5, # If you use bootstrap5
+    )
+    from app.models import MyModel
+
+    # By default you probably inherit from django_table2.Table
+    # Change inherit to ColumnShiftTableBootstrap4
+    # if you use bootstrap4
+    class MyModelTable(ColumnShiftTableBootstrap4):
+        class Meta:
+            model = MyModel
+
+    # or if you use bootstrap5
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        class Meta:
+            model = MyModel
+
+
+  views.py - In your view, nothing changes::
+
+    from .tables import MyModelTable
+    from .models import MyModel
+
+    def simple_list(request):
+        queryset = MyModel.objects.all()
+        table = MyModelTable(queryset)
+        return render(request, 'template.html', {'table': table})
+
+  template.html - use default render_table tag to display table object (using bootstrap3 / bootstrap4 / bootstrap5)::
+
+    {% extends "base.html" %}
+    {% load django_tables2 %}
+    {% render_table table %}
+
+
+
+JS API:
+-------
+To retrieve the invisible columns you can use the ``$.django_tables2_column_shifter_hidden()`` js API.
+You can either pass the 0-based index of the table in the page (i.e use ``$.django_tables2_column_shifter_hidden(1)``
+to get the hidden columns for the 2nd table in the page) or just use it without parameters to retrieve the hidden columns
+for the first table. This API returns an array with the invisible column names.
+
+These columns can then be used when you want to export only the visible columns,
+ie  when the user clicks on the export button it would append an ``&excluded_columns=col1,col2``
+to the export button's ``href`` which would then be used by the django-tables2 ``TableExporter``
+(http://django-tables2.readthedocs.io/en/latest/pages/export.html#excluding-columns) to exclude
+these cols, i.e something like
+
+    exporter = TableExport('csv', table, exclude_columns=self.request.GET.get('excluded_columns').split(',))
+
+
+
+Bootstrap2 (support for old projects):
+--------------------------------------
+If you use Bootstrap v2 in your project then table class has to inherit from `ColumnShiftTableBootstrap2`
+imported from `django_tables2_column_shifter.tables`.
+
+Bootstrap3 (support for old projects):
+--------------------------------------
+If you use Bootstrap v3 in your project then table class has to inherit from `ColumnShiftTableBootstrap3`
+imported from `django_tables2_column_shifter.tables`.
+
+Bootstrap4 :
+--------------------------------------
+If you use Bootstrap v4 in your project then table class has to inherit from `ColumnShiftTableBootstrap4`
+imported from `django_tables2_column_shifter.tables`.
+
+Bootstrap5:
+--------------------------------------
+If you use Bootstrap v5 in your project then table class has to inherit from `ColumnShiftTableBootstrap5`
+imported from `django_tables2_column_shifter.tables`.
+
+
+
+Warnings:
+----------
+
+- **Warning** : - If you use {% render_table %} tag with queryset (not table class instance),
+  django-tables2-column-shifter will not be work. Queryset does not have ``template`` attribute::
+
+    {% load django_tables2 %}
+    {% render_table queryset %} {# not work #}
+
+
+- **Warning** : - If you use a different template than ``django_tables2_column_shifter/bootstrap*.html``
+  to render your table, probably django-tables2-column-shifter will not be work.
+  Your custom template should inherit from ``django_tables2_column_shifter/bootstrap*.html``
+
+- **Warning** : - Since version 2.0 the default template is not used for Table class.
+  Moreover template ``django_tables2_column_shifter/table.html`` by default inherit from
+  ``django_tables2_column_shifter/bootstrap4.html``
+
+
+
+
+Customizing:
+-------------
+1. If you use more then one instance of the same Table class, you should use a different prefix for each instance::
+
+    tab1 = MyModelTable(queryset, prefix='tab1')
+    tab2 = MyModelTable(queryset, prefix='tab2')
+    tab3 = MyModelTable(queryset, prefix='tab3')
+
+2. To disable shifter mechanism - set ``False`` to ``shift_table_column`` in your table class (default value is True)::
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+       shift_table_column = False
+       ...
+
+
+3. By default, all columns from sequence are visible, if you want limit visible columns,
+   override method ``get_column_default_show(self)`` like that::
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        def get_column_default_show(self):
+            self.column_default_show = ['column1', 'column2']
+            return super(MyModelTable, self).get_column_default_show()
+
+4. By default, all columns from sequence are visible, if you want exclude some colmumns and
+   block ability to manipulate then, use: ``column_excluded``
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        column_excluded = ['ex_column1', 'ex_column2']
+
+    or
+
+    class MyModelTable(ColumnShiftTableBootstrap5):
+        def get_column_excluded(self):
+            self.column_excluded = ['ex_column1', 'ex_column2']
+            return super(MyModelTable, self).get_column_excluded()
+
+
+Run demo:
+---------
+1. Download or clone project from `https://github.com/djk2/django-tables2-column-shifter`::
+
+    git clone https://github.com/djk2/django-tables2-column-shifter.git
+
+2. Go to testproject directory::
+
+    cd django-tables2-column-shifter/testproject
+
+3. Install requirements::
+
+    pip install -r requirements.txt
+
+4. Run django developing server::
+
+    python manage.py runserver
+
+
+Links:
+--------
+- `Django documentation <https://docs.djangoproject.com/en/dev/>`_
+- `django-tables2 documentation <https://django-tables2.readthedocs.io/en/latest/>`_
```

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.po` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.mo` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.po` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.mo` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.po` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.mo` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tables.py` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tables.py`

 * *Files 10% similar despite different names*

```diff
@@ -5,14 +5,17 @@
 
     # If button for shifting columns is visible
     shift_table_column = True
 
     # Which columns are visible by default
     column_default_show = None
 
+    # List of columns to exclude from choice
+    column_excluded = None
+
     # Shifter template for tabel inherit from django_table2/bootstrap.html
     shifter_template = "django_tables2_column_shifter/table.html"
 
     # Css class for dropdown button above table
     dropdown_button_css = "btn btn-default btn-xs"
 
     def __init__(self, *args, **kwargs):
@@ -26,18 +29,21 @@
 
     def get_column_default_show(self):
         """
         Returns the columns that are visible by default
         If self.column_default_show is None then
         # default visible columns will be return from sequence
         """
-        if self.column_default_show is None:
-            return self.sequence
-        else:
-            return self.column_default_show
+        return self.column_default_show or self.sequence
+
+    def get_column_excluded(self):
+        """
+        Excluded columns are not shown on list to choice
+        """
+        return self.column_excluded or []
 
     @property
     def uniq_table_class_name(self):
         """Return unique name of table class
         using in template for container div id
         prefix in django_tables2 is always a string, can be empty or not
         """
```

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/urls.py` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/urls.py`

 * *Files 11% similar despite different names*

```diff
@@ -2,16 +2,14 @@
 
 from .views import Bootstrap2, Bootstrap3, Bootstrap4, Bootstrap5
 
 dj_version = tuple(map(int, django.__version__.split(".")[:2]))
 
 if dj_version >= (3, 1):
     from django.urls import re_path as url
-elif dj_version >= (2, 2):
-    from django.urls import url
 else:
     from django.conf.urls import url
 
 
 urlpatterns = [
     url(r'^bootstrap2/$', Bootstrap2.as_view(), name="bootstrap2"),
     url(r'^bootstrap3/$', Bootstrap3.as_view(), name="bootstrap3"),
```

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/settings.py` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/settings.py`

 * *Files 4% similar despite different names*

```diff
@@ -38,7 +38,9 @@
 ]
 
 LANGUAGE_CODE = 'en-us'
 MEDIA_URL = '/media/'
 STATIC_URL = '/static/'
 
 MIDDLEWARE = []
+
+DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
```

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/views.py` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/views.py`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/test_base.py` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/test_base.py`

 * *Files 13% similar despite different names*

```diff
@@ -1,16 +1,23 @@
 # encoding: utf-8
 from os import path
 
 import django
 import django_tables2 as tables
 from django.contrib.staticfiles import finders
-from django.test import Client, TestCase
+from django.test import Client, TestCase, RequestFactory
+from django.template import Template, Context
 
 from django_tables2_column_shifter.tests.models import Author
+from django_tables2_column_shifter.tables import (
+    ColumnShiftTableBootstrap2,
+    ColumnShiftTableBootstrap3,
+    ColumnShiftTableBootstrap4,
+    ColumnShiftTableBootstrap5,
+)
 
 if tuple(map(int, django.__version__.split(".")[:2])) >= (1, 10):
     from django.urls import reverse
 else:
     from django.core.urlresolvers import reverse
 
 
@@ -18,32 +25,36 @@
 
     CASE = [
         {
             'bootstrap_version': 'bootstrap2',
             'min_dt_version': (1, 0),
             'max_dt_version': (2, 0),
             'template_name': 'django_tables2_column_shifter/bootstrap2.html',
+            'table_clsss': ColumnShiftTableBootstrap2,
         },
         {
             'bootstrap_version': 'bootstrap3',
             'min_dt_version': (1, 0),
             'max_dt_version': (2, 0),
             'template_name': 'django_tables2_column_shifter/bootstrap3.html',
+            'table_clsss': ColumnShiftTableBootstrap3,
         },
         {
             'bootstrap_version': 'bootstrap4',
             'min_dt_version': (2, 0),
             'max_dt_version': None,
             'template_name': 'django_tables2_column_shifter/bootstrap4.html',
+            'table_clsss': ColumnShiftTableBootstrap4,
         },
         {
             'bootstrap_version': 'bootstrap5',
             'min_dt_version': (2, 0),
             'max_dt_version': None,
             'template_name': 'django_tables2_column_shifter/bootstrap5.html',
+            'table_clsss': ColumnShiftTableBootstrap5,
         },
     ]
 
     dt_version = tuple(map(int, tables.__version__.split(".")[:2]))
 
     def setUp(self):
         # Add authors to database
@@ -177,7 +188,40 @@
         ]
 
         for static in statics:
             static_path = path.join(prefix, static)
             abs_path = finders.find(static_path)
             assert abs_path is not None
             assert path.exists(abs_path) is True
+
+    def test_column_excluded(self):
+        """
+        Check that excluded columns not render in tempalte
+        """
+
+        for case in self.CASE:
+
+            if (
+                (case['min_dt_version'] and case['min_dt_version'] > self.dt_version) or
+                (case['max_dt_version'] and case['max_dt_version'] < self.dt_version)
+            ):
+                continue
+
+            class Tab(case['table_clsss']):
+                column_excluded = ["first_name", "last_name"]
+
+                class Meta:
+                    model = Author
+
+            table = Tab(Author.objects.all())
+            request = RequestFactory().get('/fake/url')
+            template = Template("""
+                {% load django_tables2 %}
+                {% render_table table %}
+            """)
+            ctx = Context({"table": table, "request": request})
+            render = template.render(ctx)
+
+            self.assertTrue('data-td-class="id"' in render)
+            self.assertTrue('data-td-class="age"' in render)
+            self.assertFalse('data-td-class="first_name"' in render)
+            self.assertFalse('data-td-class="last_name"' in render)
```

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/tests/models.py` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/models.py`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.js` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.js`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.min.js` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.min.js`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/img/loader.gif` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/loader.gif`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/static/django_tables2_column_shifter/img/check.png` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/check.png`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap5.html` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap5.html`

 * *Files 2% similar despite different names*

```diff
@@ -28,54 +28,56 @@
                     <span class="caret"></span>
                 </button>
                 <ul class="dropdown-menu"
                     style="min-width:350px; padding:5px; cursor:pointer;"
                     aria-labelledby="btn_{{ table.uniq_table_class_name }}"
                 >
                     {% for column in table.columns %}
-                        {% if column.attrs.td.class in table.get_column_default_show %}
-                            <li class="btn-shift-column"
-                                data-td-class="{{ column.attrs.td.class }}"
-                                data-state="on"
-                                {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
-                                data-table-class-container="{{ table.uniq_table_class_name }}">
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/check.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
-                                    class="ico check"
-                                />
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; display: none; opacity:0.7;"
-                                    class="ico uncheck"
-                                />
-                                {{ column.header }}
-                            </li>
-                        {% else %}
-                            <li class="btn-shift-column"
-                                data-td-class="{{ column.attrs.td.class }}"
-                                data-state="off"
-                                {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
-                                data-table-class-container="{{ table.uniq_table_class_name }}">
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/check.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; display:none; opacity:0.7;"
-                                    class="ico check"
-                                />
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
-                                    class="ico uncheck"
-                                />
-                                {{ column.header }}
-                            </li>
+                        {% if column.attrs.td.class not in table.get_column_excluded %}
+                            {% if column.attrs.td.class in table.get_column_default_show %}
+                                <li class="btn-shift-column"
+                                    data-td-class="{{ column.attrs.td.class }}"
+                                    data-state="on"
+                                    {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
+                                    data-table-class-container="{{ table.uniq_table_class_name }}">
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/check.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
+                                        class="ico check"
+                                    />
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; display: none; opacity:0.7;"
+                                        class="ico uncheck"
+                                    />
+                                    {{ column.header }}
+                                </li>
+                            {% else %}
+                                <li class="btn-shift-column"
+                                    data-td-class="{{ column.attrs.td.class }}"
+                                    data-state="off"
+                                    {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
+                                    data-table-class-container="{{ table.uniq_table_class_name }}">
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/check.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; display:none; opacity:0.7;"
+                                        class="ico check"
+                                    />
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
+                                        class="ico uncheck"
+                                    />
+                                    {{ column.header }}
+                                </li>
+                            {% endif %}
                         {% endif %}
                     {% endfor %}
                 </ul>
             </div> {# End  btn-group#}
 
             {# Loader default is show #}
             <div class="loader" style="text-align:center;" >
```

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap2.html` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap2.html`

 * *Files 2% similar despite different names*

```diff
@@ -24,54 +24,56 @@
                             opacity:0.7;"
                     />
                     {% trans "Visible columns" %}
                     <span class="caret"></span>
                 </button>
                 <ul class="dropdown-menu" style="min-width:350px; padding:5px; cursor:pointer;">
                     {% for column in table.columns %}
-                        {% if column.attrs.td.class in table.get_column_default_show %}
-                            <li class="btn-shift-column"
-                                data-td-class="{{ column.attrs.td.class }}"
-                                data-state="on"
-                                {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
-                                data-table-class-container="{{ table.uniq_table_class_name }}">
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/check.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
-                                    class="ico check"
-                                />
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; display: none; opacity:0.7;"
-                                    class="ico uncheck"
-                                />
-                                {{ column.header }}
-                            </li>
-                        {% else %}
-                            <li class="btn-shift-column"
-                                data-td-class="{{ column.attrs.td.class }}"
-                                data-state="off"
-                                {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
-                                data-table-class-container="{{ table.uniq_table_class_name }}">
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/check.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; display:none; opacity:0.7;"
-                                    class="ico check"
-                                />
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
-                                    class="ico uncheck"
-                                />
-                                {{ column.header }}
-                            </li>
+                        {% if column.attrs.td.class not in table.get_column_excluded %}
+                            {% if column.attrs.td.class in table.get_column_default_show %}
+                                <li class="btn-shift-column"
+                                    data-td-class="{{ column.attrs.td.class }}"
+                                    data-state="on"
+                                    {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
+                                    data-table-class-container="{{ table.uniq_table_class_name }}">
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/check.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
+                                        class="ico check"
+                                    />
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; display: none; opacity:0.7;"
+                                        class="ico uncheck"
+                                    />
+                                    {{ column.header }}
+                                </li>
+                            {% else %}
+                                <li class="btn-shift-column"
+                                    data-td-class="{{ column.attrs.td.class }}"
+                                    data-state="off"
+                                    {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
+                                    data-table-class-container="{{ table.uniq_table_class_name }}">
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/check.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; display:none; opacity:0.7;"
+                                        class="ico check"
+                                    />
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
+                                        class="ico uncheck"
+                                    />
+                                    {{ column.header }}
+                                </li>
+                            {% endif %}
                         {% endif %}
                     {% endfor %}
                 </ul>
             </div> {# End  btn-group#}
 
             {# Loader default is show #}
             <div class="loader" style="text-align:center;" >
```

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap4.html` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap4.html`

 * *Files 4% similar despite different names*

```diff
@@ -24,54 +24,56 @@
                             opacity:0.7;"
                     />
                     {% trans "Visible columns" %}
                     <span class="caret"></span>
                 </button>
                 <ul class="dropdown-menu" style="min-width:350px; padding:5px; cursor:pointer;">
                     {% for column in table.columns %}
-                        {% if column.attrs.td.class in table.get_column_default_show %}
-                            <li class="btn-shift-column"
-                                data-td-class="{{ column.attrs.td.class }}"
-                                data-state="on"
-                                {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
-                                data-table-class-container="{{ table.uniq_table_class_name }}">
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/check.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
-                                    class="ico check"
-                                />
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; display: none; opacity:0.7;"
-                                    class="ico uncheck"
-                                />
-                                {{ column.header }}
-                            </li>
-                        {% else %}
-                            <li class="btn-shift-column"
-                                data-td-class="{{ column.attrs.td.class }}"
-                                data-state="off"
-                                {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
-                                data-table-class-container="{{ table.uniq_table_class_name }}">
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/check.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; display:none; opacity:0.7;"
-                                    class="ico check"
-                                />
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
-                                    class="ico uncheck"
-                                />
-                                {{ column.header }}
-                            </li>
+                        {% if column.attrs.td.class not in table.get_column_excluded %}
+                            {% if column.attrs.td.class in table.get_column_default_show %}
+                                <li class="btn-shift-column"
+                                    data-td-class="{{ column.attrs.td.class }}"
+                                    data-state="on"
+                                    {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
+                                    data-table-class-container="{{ table.uniq_table_class_name }}">
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/check.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
+                                        class="ico check"
+                                    />
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; display: none; opacity:0.7;"
+                                        class="ico uncheck"
+                                    />
+                                    {{ column.header }}
+                                </li>
+                            {% else %}
+                                <li class="btn-shift-column"
+                                    data-td-class="{{ column.attrs.td.class }}"
+                                    data-state="off"
+                                    {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
+                                    data-table-class-container="{{ table.uniq_table_class_name }}">
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/check.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; display:none; opacity:0.7;"
+                                        class="ico check"
+                                    />
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
+                                        class="ico uncheck"
+                                    />
+                                    {{ column.header }}
+                                </li>
+                            {% endif %}
                         {% endif %}
                     {% endfor %}
                 </ul>
             </div> {# End  btn-group#}
 
             {# Loader default is show #}
             <div class="loader" style="text-align:center;" >
```

### Comparing `django-tables2-column-shifter-2.0.3/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap3.html` & `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap3.html`

 * *Files 2% similar despite different names*

```diff
@@ -24,54 +24,56 @@
                             opacity:0.7;"
                     />
                     {% trans "Visible columns" %}
                     <span class="caret"></span>
                 </button>
                 <ul class="dropdown-menu" style="min-width:350px; padding:5px; cursor:pointer;">
                     {% for column in table.columns %}
-                        {% if column.attrs.td.class in table.get_column_default_show %}
-                            <li class="btn-shift-column"
-                                data-td-class="{{ column.attrs.td.class }}"
-                                data-state="on"
-                                {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
-                                data-table-class-container="{{ table.uniq_table_class_name }}">
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/check.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
-                                    class="ico check"
-                                />
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; display: none; opacity:0.7;"
-                                    class="ico uncheck"
-                                />
-                                {{ column.header }}
-                            </li>
-                        {% else %}
-                            <li class="btn-shift-column"
-                                data-td-class="{{ column.attrs.td.class }}"
-                                data-state="off"
-                                {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
-                                data-table-class-container="{{ table.uniq_table_class_name }}">
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/check.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; display:none; opacity:0.7;"
-                                    class="ico check"
-                                />
-                                <img
-                                    src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
-                                    alt="loader"
-                                    style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
-                                    class="ico uncheck"
-                                />
-                                {{ column.header }}
-                            </li>
+                        {% if column.attrs.td.class not in table.get_column_excluded %}
+                            {% if column.attrs.td.class in table.get_column_default_show %}
+                                <li class="btn-shift-column"
+                                    data-td-class="{{ column.attrs.td.class }}"
+                                    data-state="on"
+                                    {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
+                                    data-table-class-container="{{ table.uniq_table_class_name }}">
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/check.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
+                                        class="ico check"
+                                    />
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; display: none; opacity:0.7;"
+                                        class="ico uncheck"
+                                    />
+                                    {{ column.header }}
+                                </li>
+                            {% else %}
+                                <li class="btn-shift-column"
+                                    data-td-class="{{ column.attrs.td.class }}"
+                                    data-state="off"
+                                    {% if not forloop.last %} style="border-bottom:1px solid #ccc;" {%endif %}
+                                    data-table-class-container="{{ table.uniq_table_class_name }}">
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/check.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; display:none; opacity:0.7;"
+                                        class="ico check"
+                                    />
+                                    <img
+                                        src="{% static "django_tables2_column_shifter/img/uncheck.png" %}"
+                                        alt="loader"
+                                        style="width:20px; height:20px; margin-right:5px; opacity:0.7;"
+                                        class="ico uncheck"
+                                    />
+                                    {{ column.header }}
+                                </li>
+                            {% endif %}
                         {% endif %}
                     {% endfor %}
                 </ul>
             </div> {# End  btn-group#}
 
             {# Loader default is show #}
             <div class="loader" style="text-align:center;" >
```

### Comparing `django-tables2-column-shifter-2.0.3/LICENSE` & `django-tables2-column-shifter-2.1.0/LICENSE`

 * *Files identical despite different names*

