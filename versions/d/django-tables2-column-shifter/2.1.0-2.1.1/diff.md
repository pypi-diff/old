# Comparing `tmp/django-tables2-column-shifter-2.1.0.tar.gz` & `tmp/django-tables2-column-shifter-2.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-tables2-column-shifter-2.1.0.tar", last modified: Thu Apr  6 14:28:37 2023, max compression
+gzip compressed data, was "django-tables2-column-shifter-2.1.1.tar", last modified: Fri Apr  7 07:21:28 2023, max compression
```

## Comparing `django-tables2-column-shifter-2.1.0.tar` & `django-tables2-column-shifter-2.1.1.tar`

### file list

```diff
@@ -1,56 +1,56 @@
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     2571 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/CHANGELOG.rst
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1570 2016-11-21 08:42:29.000000 django-tables2-column-shifter-2.1.0/LICENSE
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      231 2016-11-22 15:42:55.000000 django-tables2-column-shifter-2.1.0/MANIFEST.in
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)    11320 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/PKG-INFO
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)    10470 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/README.rst
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       68 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/__init__.py
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      607 2018-04-23 09:25:33.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.mo
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      992 2018-04-23 09:25:33.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.po
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      713 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.mo
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1142 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.po
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      600 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.mo
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1021 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.po
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      573 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/check.png
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      274 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/cols.png
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      847 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/loader.gif
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      349 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/uncheck.png
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     6504 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.js
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1687 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.min.js
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     3130 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tables.py
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     4886 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap2.html
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     4886 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap3.html
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     4887 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap4.html
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     5070 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap5.html
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       62 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/table.html
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/
--rw-r--r--   0 grzegorz  (1000) grzegorz  (1000)        0 2016-11-24 07:27:10.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/__init__.py
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      755 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/models.py
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1093 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/settings.py
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      409 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/tables.py
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     9169 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/test_base.py
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      550 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/urls.py
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     2302 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/views.py
-drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-06 14:28:37.319159 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)    11320 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/PKG-INFO
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     2126 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/SOURCES.txt
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)        1 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/dependency_links.txt
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)        1 2017-05-24 17:24:45.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/not-zip-safe
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       34 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/requires.txt
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       30 2023-04-06 14:28:37.000000 django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/top_level.txt
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      374 2023-04-06 14:28:37.323159 django-tables2-column-shifter-2.1.0/setup.cfg
--rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1331 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.0/setup.py
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     2762 2023-04-07 07:17:07.000000 django-tables2-column-shifter-2.1.1/CHANGELOG.rst
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1570 2016-11-21 08:42:29.000000 django-tables2-column-shifter-2.1.1/LICENSE
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      231 2016-11-22 15:42:55.000000 django-tables2-column-shifter-2.1.1/MANIFEST.in
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)    11615 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/PKG-INFO
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)    10765 2023-04-07 07:17:07.000000 django-tables2-column-shifter-2.1.1/README.rst
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       68 2023-04-07 07:17:07.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/__init__.py
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.342609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.342609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/el/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/el/LC_MESSAGES/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      607 2018-04-23 09:25:33.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.mo
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      992 2018-04-23 09:25:33.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.po
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.342609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pl/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pl/LC_MESSAGES/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      713 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.mo
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1142 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.po
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.342609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pt_BR/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      600 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.mo
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1021 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.po
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.342609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.342609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/img/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      573 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/img/check.png
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      274 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/img/cols.png
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      847 2016-11-24 07:27:09.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/img/loader.gif
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      349 2017-02-19 14:03:25.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/img/uncheck.png
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/js/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     6596 2023-04-07 07:17:07.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.js
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1647 2023-04-07 07:17:07.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.min.js
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     3130 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tables.py
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.342609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     4886 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap2.html
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     4886 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap3.html
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     4887 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap4.html
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     5070 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap5.html
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       62 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/table.html
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/
+-rw-r--r--   0 grzegorz  (1000) grzegorz  (1000)        0 2016-11-24 07:27:10.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/__init__.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      755 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/models.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1093 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/settings.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      409 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/tables.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     9169 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/test_base.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      550 2023-04-06 14:26:04.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/urls.py
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     2302 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/views.py
+drwxrwxr-x   0 grzegorz  (1000) grzegorz  (1000)        0 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter.egg-info/
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)    11615 2023-04-07 07:21:28.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter.egg-info/PKG-INFO
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     2126 2023-04-07 07:21:28.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter.egg-info/SOURCES.txt
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)        1 2023-04-07 07:21:28.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter.egg-info/dependency_links.txt
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)        1 2023-04-07 07:21:28.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter.egg-info/not-zip-safe
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       34 2023-04-07 07:21:28.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter.egg-info/requires.txt
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)       30 2023-04-07 07:21:28.000000 django-tables2-column-shifter-2.1.1/django_tables2_column_shifter.egg-info/top_level.txt
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)      374 2023-04-07 07:21:28.346609 django-tables2-column-shifter-2.1.1/setup.cfg
+-rw-rw-r--   0 grzegorz  (1000) grzegorz  (1000)     1331 2023-04-06 12:10:58.000000 django-tables2-column-shifter-2.1.1/setup.py
```

### Comparing `django-tables2-column-shifter-2.1.0/CHANGELOG.rst` & `django-tables2-column-shifter-2.1.1/CHANGELOG.rst`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,16 @@
 CHANGELOG
 ===========
 
+v. 2.1.1
+--------
+
+    * Add the ``$.django_tables2_column_shifter_init`` api to initialize the column shifter
+      for tables that are added to the DOM after the page has loaded (@spapas)
+
 v. 2.1.0
 --------
 
     * Add possibility to exclude columns from shifting via `column_excluded`
     * Support for Python 3.10
     * Support for Django 4.0
     * Support for Django 4.2
```

### Comparing `django-tables2-column-shifter-2.1.0/LICENSE` & `django-tables2-column-shifter-2.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/PKG-INFO` & `django-tables2-column-shifter-2.1.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-tables2-column-shifter
-Version: 2.1.0
+Version: 2.1.1
 Summary: Extension for django_tables2 can dynamically show or hide columns
 Home-page: https://github.com/djk2/django-tables2-column-shifter
 Author: Grzegorz Tężycki
 Author-email: grzegorz.tezycki@gmail.com
 License: BSD
 Keywords: django_tables2 django columns
 Classifier: Environment :: Web Environment
@@ -201,14 +201,19 @@
     {% load django_tables2 %}
     {% render_table table %}
 
 
 
 JS API:
 -------
+
+This library is initialized automatically on the page ready event. In case you are using a framework
+like htmx, unpoly or turbo that does not trigger the ready event, you can initialize it manually by calling
+``$.django_tables2_column_shifter_init()`` on your framework's initialize callback.
+
 To retrieve the invisible columns you can use the ``$.django_tables2_column_shifter_hidden()`` js API.
 You can either pass the 0-based index of the table in the page (i.e use ``$.django_tables2_column_shifter_hidden(1)``
 to get the hidden columns for the 2nd table in the page) or just use it without parameters to retrieve the hidden columns
 for the first table. This API returns an array with the invisible column names.
 
 These columns can then be used when you want to export only the visible columns,
 ie  when the user clicks on the export button it would append an ``&excluded_columns=col1,col2``
```

### Comparing `django-tables2-column-shifter-2.1.0/README.rst` & `django-tables2-column-shifter-2.1.1/README.rst`

 * *Files 1% similar despite different names*

```diff
@@ -179,14 +179,19 @@
     {% load django_tables2 %}
     {% render_table table %}
 
 
 
 JS API:
 -------
+
+This library is initialized automatically on the page ready event. In case you are using a framework
+like htmx, unpoly or turbo that does not trigger the ready event, you can initialize it manually by calling
+``$.django_tables2_column_shifter_init()`` on your framework's initialize callback.
+
 To retrieve the invisible columns you can use the ``$.django_tables2_column_shifter_hidden()`` js API.
 You can either pass the 0-based index of the table in the page (i.e use ``$.django_tables2_column_shifter_hidden(1)``
 to get the hidden columns for the 2nd table in the page) or just use it without parameters to retrieve the hidden columns
 for the first table. This API returns an array with the invisible column names.
 
 These columns can then be used when you want to export only the visible columns,
 ie  when the user clicks on the export button it would append an ``&excluded_columns=col1,col2``
```

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.mo` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.po` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/el/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.mo` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.po` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pl/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.mo` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.po` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/locale/pt_BR/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/check.png` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/img/check.png`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/img/loader.gif` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/img/loader.gif`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.js` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.js`

 * *Files 5% similar despite different names*

#### js-beautify {}

```diff
@@ -1,10 +1,12 @@
 // Author: Grzegorz Tężycki
 
-$(document).ready(function() {
+
+// API function for initializing column shifter tables
+$.django_tables2_column_shifter_init = function() {
 
     // In web storage is saved structure like that:
     // localStorage['django_tables2_column_shifter'] = {
     //     'table_class_container1' : {
     //         'id' : 'on',
     //         'col1' : 'off',
     //         'col2' : 'on',
@@ -181,23 +183,26 @@
     });
 
     // Load saved states for all tables
     load_state_for_all_containters();
 
     // show or hide columns based on data from web storage
     shift_columns();
+}
+
 
-    // Add API method for retrieving non-visible cols for table
-    // Pass the 0-based index of the table or leave the parameter 
-    // empty to return the hidden cols for the 1st table found
-    $.django_tables2_column_shifter_hidden = function(idx) {
-        if (idx == undefined) {
-            idx = 0;
-        }
-        return $('.table-container').eq(idx).find('.btn-shift-column').filter(function(z) {
-            return $(this).data('state') == 'off'
-        }).map(function(z) {
-            return $(this).data('td-class')
-        }).toArray();
+// Add API method for retrieving non-visible cols for table
+// Pass the 0-based index of the table or leave the parameter
+// empty to return the hidden cols for the 1st table found
+$.django_tables2_column_shifter_hidden = function(idx) {
+    if (idx == undefined) {
+        idx = 0;
     }
+    return $('.table-container').eq(idx).find('.btn-shift-column').filter(function(z) {
+        return $(this).data('state') == 'off'
+    }).map(function(z) {
+        return $(this).data('td-class')
+    }).toArray();
+}
 
-});
+// Initialize column shifter on page ready event
+$(document).ready($.django_tables2_column_shifter_init);
```

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.min.js` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/static/django_tables2_column_shifter/js/django_tables2_column_shifter.min.js`

 * *Files 8% similar despite different names*

#### js-beautify {}

```diff
@@ -1,74 +1,49 @@
-$(document).ready(function() {
-    var t = "django_tables2_column_shifter",
-        n = function() {
-            var n = localStorage.getItem(t);
-            return n = null === n ? {} : JSON.parse(n)
-        },
-        a = function(n) {
-            var a = JSON.stringify(n);
-            localStorage.setItem(t, a)
-        },
-        i = function(t) {
-            var i = t.data("table-class-container"),
-                o = $("#" + i),
-                c = t.data("state"),
-                e = t.data("td-class"),
-                s = n(),
-                f = o.attr("id");
-            f in s ? data = s[f] : (data = {}, s[f] = data), data[e] = c, a(s)
-        },
-        o = function(t) {
-            var a = n(),
-                i = t.attr("id"),
-                o = {};
-            i in a && (o = a[i], t.find(".btn-shift-column").each(function() {
-                var t = $(this),
-                    n = t.data("td-class");
-                if (n in o) {
-                    var a = o[n];
-                    f(t, a)
-                }
-            }))
-        },
-        c = function(t) {
-            t.find(".loader").hide(), t.find(".table-wrapper").show()
-        },
-        e = function() {
-            $(".column-shifter-container").each(function() {
-                $table_class_container = $(this), o($table_class_container), c($table_class_container)
-            })
-        };
+$.django_tables2_column_shifter_init = function() {
+    function o() {
+        var t = localStorage.getItem(c);
+        return t = null === t ? {} : JSON.parse(t)
+    }
+
+    function i(t) {
+        var n = t.data("table-class-container"),
+            a = $("#" + n),
+            i = t.data("state"),
+            n = t.data("td-class"),
+            t = o();
+        (a = a.attr("id")) in t ? data = t[a] : (data = {}, t[a] = data), data[n] = i,
+            function(t) {
+                t = JSON.stringify(t);
+                localStorage.setItem(c, t)
+            }(t)
+    }
+    var c = "django_tables2_column_shifter";
     shift_column = function(t) {
         var n = t.data("state"),
             a = t.data("td-class"),
-            i = t.data("table-class-container"),
-            o = $("#" + i),
-            c = o.find("table"),
-            e = c.find("." + a);
-        "on" === n ? e.show() : e.hide()
+            t = t.data("table-class-container"),
+            a = $("#" + t).find("table").find("." + a);
+        "on" === n ? a.show() : a.hide()
     }, shift_columns = function() {
-        var t, n = $(".btn-shift-column"),
-            a = n.length;
-        for (t = 0; a > t; t++) shift_column($(n[t]))
+        for (var t = $(".btn-shift-column"), n = t.length, a = 0; a < n; a++) shift_column($(t[a]))
+    };
+    var e = function(t, n) {
+        t.data("state", n), t = t, "on" === n ? (t.find("img.uncheck").hide(), t.find("img.check").show()) : (t.find("img.check").hide(), t.find("img.uncheck").show())
     };
-    var s = function(t, n) {
-            "on" === n ? (t.find("img.uncheck").hide(), t.find("img.check").show()) : (t.find("img.check").hide(), t.find("img.uncheck").show())
-        },
-        f = function(t, n) {
-            t.data("state", n), s(t, n)
-        },
-        r = function(t) {
-            var n = t.data("state");
-            n = "on" === n ? "off" : "on", f(t, n)
-        };
     $(".btn-shift-column").on("click", function(t) {
-        var n = $(this);
-        t.stopPropagation(), r(n), shift_column(n), i(n)
-    }), e(), shift_columns(), $.django_tables2_column_shifter_hidden = function(t) {
-        return void 0 == t && (t = 0), $(".table-container").eq(t).find(".btn-shift-column").filter(function() {
-            return "off" == $(this).data("state")
-        }).map(function() {
-            return $(this).data("td-class")
-        }).toArray()
-    }
-});
+        var n, a = $(this);
+        t.stopPropagation(), t = (n = a).data("state"), e(n, t = "on" === t ? "off" : "on"), shift_column(a), i(a)
+    }), $(".column-shifter-container").each(function() {
+        var a, t, n, i;
+        $table_class_container = $(this), i = $table_class_container, t = o(), (n = i.attr("id")) in t && (a = t[n], i.find(".btn-shift-column").each(function() {
+            var t = $(this),
+                n = t.data("td-class");
+            n in a && (n = a[n], e(t, n))
+        })), (i = $table_class_container).find(".loader").hide(), i.find(".table-wrapper").show()
+    }), shift_columns()
+}, $.django_tables2_column_shifter_hidden = function(t) {
+    return null == t && (t = 0), $(".table-container").eq(t).find(".btn-shift-column").filter(function(t) {
+        return "off" == $(this).data("state")
+    }).map(function(t) {
+        return $(this).data("td-class")
+    }).toArray()
+}, $(document).ready($.django_tables2_column_shifter_init);
```

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tables.py` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tables.py`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap2.html` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap2.html`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap3.html` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap3.html`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap4.html` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap4.html`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap5.html` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/templates/django_tables2_column_shifter/bootstrap5.html`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/models.py` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/models.py`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/settings.py` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/settings.py`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/test_base.py` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/test_base.py`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/urls.py` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/urls.py`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter/tests/views.py` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter/tests/views.py`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/PKG-INFO` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-tables2-column-shifter
-Version: 2.1.0
+Version: 2.1.1
 Summary: Extension for django_tables2 can dynamically show or hide columns
 Home-page: https://github.com/djk2/django-tables2-column-shifter
 Author: Grzegorz Tężycki
 Author-email: grzegorz.tezycki@gmail.com
 License: BSD
 Keywords: django_tables2 django columns
 Classifier: Environment :: Web Environment
@@ -201,14 +201,19 @@
     {% load django_tables2 %}
     {% render_table table %}
 
 
 
 JS API:
 -------
+
+This library is initialized automatically on the page ready event. In case you are using a framework
+like htmx, unpoly or turbo that does not trigger the ready event, you can initialize it manually by calling
+``$.django_tables2_column_shifter_init()`` on your framework's initialize callback.
+
 To retrieve the invisible columns you can use the ``$.django_tables2_column_shifter_hidden()`` js API.
 You can either pass the 0-based index of the table in the page (i.e use ``$.django_tables2_column_shifter_hidden(1)``
 to get the hidden columns for the 2nd table in the page) or just use it without parameters to retrieve the hidden columns
 for the first table. This API returns an array with the invisible column names.
 
 These columns can then be used when you want to export only the visible columns,
 ie  when the user clicks on the export button it would append an ``&excluded_columns=col1,col2``
```

### Comparing `django-tables2-column-shifter-2.1.0/django_tables2_column_shifter.egg-info/SOURCES.txt` & `django-tables2-column-shifter-2.1.1/django_tables2_column_shifter.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `django-tables2-column-shifter-2.1.0/setup.py` & `django-tables2-column-shifter-2.1.1/setup.py`

 * *Files identical despite different names*

