# Comparing `tmp/django-minke-1.2.3.dev0.tar.gz` & `tmp/django-minke-1.3.0.dev0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/django-minke-1.2.3.dev0.tar", last modified: Mon Dec  6 10:37:34 2021, max compression
+gzip compressed data, was "django-minke-1.3.0.dev0.tar", last modified: Thu Apr  6 12:04:07 2023, max compression
```

## Comparing `django-minke-1.2.3.dev0.tar` & `django-minke-1.3.0.dev0.tar`

### file list

```diff
@@ -1,79 +1,83 @@
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/
--rw-r--r--   0 thomas    (1000) thomas    (1000)      124 2020-01-04 18:58:05.000000 django-minke-1.2.3.dev0/MANIFEST.in
--rw-rw-r--   0 thomas    (1000) thomas    (1000)     5572 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/PKG-INFO
--rw-r--r--   0 thomas    (1000) thomas    (1000)     3686 2020-09-03 05:45:05.000000 django-minke-1.2.3.dev0/README.rst
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/django_minke.egg-info/
--rw-r--r--   0 thomas    (1000) thomas    (1000)     5572 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/django_minke.egg-info/PKG-INFO
--rw-r--r--   0 thomas    (1000) thomas    (1000)     1832 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/django_minke.egg-info/SOURCES.txt
--rw-r--r--   0 thomas    (1000) thomas    (1000)        1 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/django_minke.egg-info/dependency_links.txt
--rw-r--r--   0 thomas    (1000) thomas    (1000)       81 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/django_minke.egg-info/requires.txt
--rw-r--r--   0 thomas    (1000) thomas    (1000)        6 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/django_minke.egg-info/top_level.txt
--rw-r--r--   0 thomas    (1000) thomas    (1000)        1 2020-01-04 19:00:53.000000 django-minke-1.2.3.dev0/django_minke.egg-info/zip-safe
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/
--rw-r--r--   0 thomas    (1000) thomas    (1000)       94 2021-12-06 10:33:51.000000 django-minke-1.2.3.dev0/minke/__init__.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)    17448 2021-04-21 10:49:52.000000 django-minke-1.2.3.dev0/minke/admin.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      110 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/apps.py
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/contrib/
--rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/__init__.py
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/contrib/commands/
--rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/commands/__init__.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      968 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/commands/admin.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)       91 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/commands/apps.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      129 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/commands/forms.py
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/contrib/commands/migrations/
--rw-r--r--   0 thomas    (1000) thomas    (1000)     2608 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/commands/migrations/0001_initial.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/commands/migrations/__init__.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     4470 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/commands/models.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     2641 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/commands/sessions.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)       60 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/contrib/commands/tests.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     3937 2020-09-08 19:41:54.000000 django-minke-1.2.3.dev0/minke/engine.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      936 2021-10-28 12:20:43.000000 django-minke-1.2.3.dev0/minke/exceptions.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)    10237 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/fabrictools.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     2091 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/filters.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     1874 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/forms.py
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/management/
--rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/management/__init__.py
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/management/commands/
--rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/management/commands/__init__.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     2917 2020-09-08 19:24:30.000000 django-minke-1.2.3.dev0/minke/management/commands/minkeadm.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     8119 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/management/commands/minkerun.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     3611 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/messages.py
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/migrations/
--rw-r--r--   0 thomas    (1000) thomas    (1000)      970 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/migrations/0001_initial.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      396 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/migrations/0002_auto_20180619_1703.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     6144 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/migrations/0003_auto_20190326_1648.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)    11470 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/migrations/0004_auto_20190703_1319.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      591 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/migrations/0005_auto_20190810_1412.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      458 2020-01-08 12:33:36.000000 django-minke-1.2.3.dev0/minke/migrations/0006_auto_20200108_1333.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/migrations/__init__.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)    23247 2020-09-08 20:14:37.000000 django-minke-1.2.3.dev0/minke/models.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      589 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/serializers.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)    23376 2021-11-02 14:21:06.000000 django-minke-1.2.3.dev0/minke/sessions.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      934 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/settings.py
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/static/
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/static/minke/
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/static/minke/css/
--rw-r--r--   0 thomas    (1000) thomas    (1000)     3037 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/static/minke/css/minke.css
--rw-r--r--   0 thomas    (1000) thomas    (1000)       88 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/static/minke/css/minke_form.css
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/static/minke/js/
--rw-r--r--   0 thomas    (1000) thomas    (1000)     5516 2021-04-22 12:31:18.000000 django-minke-1.2.3.dev0/minke/static/minke/js/minke.js
--rw-r--r--   0 thomas    (1000) thomas    (1000)     4291 2021-10-28 12:20:52.000000 django-minke-1.2.3.dev0/minke/tasks.py
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/templates/
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/templates/minke/
--rw-r--r--   0 thomas    (1000) thomas    (1000)      403 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templates/minke/change_form.html
--rw-r--r--   0 thomas    (1000) thomas    (1000)      882 2020-03-07 14:50:57.000000 django-minke-1.2.3.dev0/minke/templates/minke/change_list.html
--rw-r--r--   0 thomas    (1000) thomas    (1000)     2088 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templates/minke/change_list_results.html
--rw-r--r--   0 thomas    (1000) thomas    (1000)      154 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templates/minke/message_toggle.html
--rw-r--r--   0 thomas    (1000) thomas    (1000)     1140 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templates/minke/minke_form.html
--rw-r--r--   0 thomas    (1000) thomas    (1000)     1357 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templates/minke/session.html
--rw-r--r--   0 thomas    (1000) thomas    (1000)      717 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templates/minke/session_select.html
--rw-r--r--   0 thomas    (1000) thomas    (1000)      405 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templates/minke/session_summary.html
--rw-r--r--   0 thomas    (1000) thomas    (1000)      817 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templates/minke/session_switch.html
-drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/minke/templatetags/
--rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templatetags/__init__.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     1866 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/templatetags/minke.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)      811 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/urls.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     1757 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/utils.py
--rw-r--r--   0 thomas    (1000) thomas    (1000)     2611 2020-01-04 19:00:54.000000 django-minke-1.2.3.dev0/minke/views.py
--rw-rw-r--   0 thomas    (1000) thomas    (1000)       38 2021-12-06 10:37:34.000000 django-minke-1.2.3.dev0/setup.cfg
--rw-r--r--   0 thomas    (1000) thomas    (1000)     2012 2020-09-02 22:35:23.000000 django-minke-1.2.3.dev0/setup.py
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.308431 django-minke-1.3.0.dev0/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     1527 2020-01-04 18:58:05.000000 django-minke-1.3.0.dev0/LICENCE
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      124 2020-01-04 18:58:05.000000 django-minke-1.3.0.dev0/MANIFEST.in
+-rw-rw-r--   0 thomas    (1000) thomas    (1000)     4906 2023-04-06 12:04:07.308431 django-minke-1.3.0.dev0/PKG-INFO
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     3686 2020-09-03 05:45:05.000000 django-minke-1.3.0.dev0/README.rst
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.292430 django-minke-1.3.0.dev0/django_minke.egg-info/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     4906 2023-04-06 12:04:07.000000 django-minke-1.3.0.dev0/django_minke.egg-info/PKG-INFO
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     1986 2023-04-06 12:04:07.000000 django-minke-1.3.0.dev0/django_minke.egg-info/SOURCES.txt
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        1 2023-04-06 12:04:07.000000 django-minke-1.3.0.dev0/django_minke.egg-info/dependency_links.txt
+-rw-r--r--   0 thomas    (1000) thomas    (1000)       88 2023-04-06 12:04:07.000000 django-minke-1.3.0.dev0/django_minke.egg-info/requires.txt
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        6 2023-04-06 12:04:07.000000 django-minke-1.3.0.dev0/django_minke.egg-info/top_level.txt
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        1 2020-01-04 19:00:53.000000 django-minke-1.3.0.dev0/django_minke.egg-info/zip-safe
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.296431 django-minke-1.3.0.dev0/minke/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)       94 2023-04-06 11:59:08.000000 django-minke-1.3.0.dev0/minke/__init__.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)    16763 2023-04-06 12:02:28.000000 django-minke-1.3.0.dev0/minke/admin.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      110 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/apps.py
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.296431 django-minke-1.3.0.dev0/minke/contrib/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/__init__.py
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.300431 django-minke-1.3.0.dev0/minke/contrib/commands/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/commands/__init__.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      968 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/commands/admin.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)       91 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/commands/apps.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      129 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/commands/forms.py
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.300431 django-minke-1.3.0.dev0/minke/contrib/commands/migrations/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     2608 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/commands/migrations/0001_initial.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/commands/migrations/__init__.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     4470 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/commands/models.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     2641 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/commands/sessions.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)       60 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/contrib/commands/tests.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     3792 2023-04-06 08:05:57.000000 django-minke-1.3.0.dev0/minke/engine.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      936 2021-10-28 12:20:43.000000 django-minke-1.3.0.dev0/minke/exceptions.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     5254 2023-04-06 08:09:00.000000 django-minke-1.3.0.dev0/minke/fabrictools.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     2091 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/filters.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     1874 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/forms.py
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.300431 django-minke-1.3.0.dev0/minke/management/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/management/__init__.py
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.300431 django-minke-1.3.0.dev0/minke/management/commands/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/management/commands/__init__.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     2917 2020-09-08 19:24:30.000000 django-minke-1.3.0.dev0/minke/management/commands/minkeadm.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     8129 2023-04-05 17:46:32.000000 django-minke-1.3.0.dev0/minke/management/commands/minkerun.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     3611 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/messages.py
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.304431 django-minke-1.3.0.dev0/minke/migrations/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      970 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/migrations/0001_initial.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      396 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/migrations/0002_auto_20180619_1703.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     6144 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/migrations/0003_auto_20190326_1648.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)    11470 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/migrations/0004_auto_20190703_1319.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      591 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/migrations/0005_auto_20190810_1412.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      458 2020-01-08 12:33:36.000000 django-minke-1.3.0.dev0/minke/migrations/0006_auto_20200108_1333.py
+-rw-rw-r--   0 thomas    (1000) thomas    (1000)      600 2023-04-04 14:46:20.000000 django-minke-1.3.0.dev0/minke/migrations/0007_auto_20230404_1646.py
+-rw-rw-r--   0 thomas    (1000) thomas    (1000)      964 2023-04-05 19:53:08.000000 django-minke-1.3.0.dev0/minke/migrations/0008_auto_20230405_2153.py
+-rw-rw-r--   0 thomas    (1000) thomas    (1000)      339 2023-04-05 19:57:08.000000 django-minke-1.3.0.dev0/minke/migrations/0009_remove_minkesession_session_data.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/migrations/__init__.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)    23285 2023-04-06 12:02:28.000000 django-minke-1.3.0.dev0/minke/models.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      589 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/serializers.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)    23375 2023-04-06 12:02:28.000000 django-minke-1.3.0.dev0/minke/sessions.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      383 2023-04-05 17:29:28.000000 django-minke-1.3.0.dev0/minke/settings.py
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.288431 django-minke-1.3.0.dev0/minke/static/
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.288431 django-minke-1.3.0.dev0/minke/static/minke/
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.304431 django-minke-1.3.0.dev0/minke/static/minke/css/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     3037 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/static/minke/css/minke.css
+-rw-r--r--   0 thomas    (1000) thomas    (1000)       88 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/static/minke/css/minke_form.css
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.304431 django-minke-1.3.0.dev0/minke/static/minke/js/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     5534 2023-04-04 14:36:52.000000 django-minke-1.3.0.dev0/minke/static/minke/js/minke.js
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     3577 2023-04-06 08:13:20.000000 django-minke-1.3.0.dev0/minke/tasks.py
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.288431 django-minke-1.3.0.dev0/minke/templates/
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.304431 django-minke-1.3.0.dev0/minke/templates/minke/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      403 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templates/minke/change_form.html
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      882 2020-03-07 14:50:57.000000 django-minke-1.3.0.dev0/minke/templates/minke/change_list.html
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     2088 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templates/minke/change_list_results.html
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      154 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templates/minke/message_toggle.html
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     1140 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templates/minke/minke_form.html
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     1357 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templates/minke/session.html
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      717 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templates/minke/session_select.html
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      405 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templates/minke/session_summary.html
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      817 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templates/minke/session_switch.html
+drwxrwxr-x   0 thomas    (1000) thomas    (1000)        0 2023-04-06 12:04:07.308431 django-minke-1.3.0.dev0/minke/templatetags/
+-rw-r--r--   0 thomas    (1000) thomas    (1000)        0 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templatetags/__init__.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     1866 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/templatetags/minke.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)      811 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/urls.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     2496 2023-04-06 11:19:05.000000 django-minke-1.3.0.dev0/minke/utils.py
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     2611 2020-01-04 19:00:54.000000 django-minke-1.3.0.dev0/minke/views.py
+-rw-rw-r--   0 thomas    (1000) thomas    (1000)       38 2023-04-06 12:04:07.308431 django-minke-1.3.0.dev0/setup.cfg
+-rw-r--r--   0 thomas    (1000) thomas    (1000)     2030 2023-04-05 17:50:16.000000 django-minke-1.3.0.dev0/setup.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `django-minke-1.2.3.dev0/PKG-INFO` & `django-minke-1.3.0.dev0/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,98 +1,14 @@
-Metadata-Version: 1.1
+Metadata-Version: 2.1
 Name: django-minke
-Version: 1.2.3.dev0
+Version: 1.3.0.dev0
 Summary: Django- and fabric-based building toolkit for remote-control- and configuration-management-systems.
-Home-page: UNKNOWN
 Author: Thomas Leichtfuß
 Author-email: thomas.leichtfuss@posteo.de
 License: BSD License
-Description: ================
-        Welcome to Minke
-        ================
-        
-        .. image:: https://travis-ci.com/thomst/django-minke.svg?branch=master
-           :target: https://travis-ci.com/thomst/django-minke
-        
-        .. image:: https://coveralls.io/repos/github/thomst/django-minke/badge.svg
-           :target: https://coveralls.io/github/thomst/django-minke
-        
-        .. image:: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue
-           :target: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue
-           :alt: python: 3.4, 3.5, 3.6, 3.7, 3.8
-        
-        .. image:: https://img.shields.io/badge/django-1.11%20%7C%202.0%20%7C%202.1%20%7C%202.2-orange
-           :target: https://img.shields.io/badge/django-1.11%20%7C%202.0%20%7C%202.1%20%7C%202.2-orange
-           :alt: django: 1.11, 2.0, 2.1, 2.2
-        
-        Links
-        =====
-        * Minke on github: https://github.com/thomst/django-minke
-        * Minke on Read the Docs: https://django-minke.readthedocs.io
-        * Getting started: https://django-minke.readthedocs.io/en/latest/docs/gettingstarted.html
-        
-        A framework for remote-control- and configuration-management-systems
-        ====================================================================
-        Minke is a framework that combines the full power of djangos admin-interface
-        with the reliability and configurability of fabric2. A pure open-source- and
-        pure python-solution to realize the most different szenarios concerning remote-
-        control and configuration-managment.
-        
-        Imagine you just need to setup some managment-commands for a handful of servers -
-        you can do that with minke. Imagine you have lots of servers with different
-        setups that you need to group and address seperatly - you can do that with
-        minke. Imagine you have servers with multiple subsystems installed on each of them
-        and you not just want to manage those systems but also to track configurations,
-        version-numbers, installed extensions or modules and to filter for all of those
-        values within your backend - you can do that with minke.
-        
-        Features
-        --------
-        * full integration with django's admin-site
-        * parrallel session-execution through celery
-        * realtime monitoring of executed remote-sessions
-        * command-line-api using django's management-commands
-        * session- and command-history
-        
-        Concept
-        -------
-        The main idea of minke is to define an arbitrary data-structure that represents
-        your server- and subsystem-landscape as django-models. And then be able to
-        run specific remote-tasks for those models right out of their changelist-sites.
-        Now those tasks could be anything about remote-control and system-managment, but
-        also fetching relevant data to update your django-data-structure itself.
-        
-        To make this possible there are three main elements:
-        
-        * hosts,
-        * minke-models,
-        * and sessions.
-        
-        Hosts
-        .....
-        A Host is a django-model that is basically the database-representation of a
-        specific ssh-config. It holds every information needed by fabric to connect
-        to the remote-system.
-        
-        Minke-Models
-        ............
-        Minke-models now are all those models that you want to run remote-sessions with.
-        This could be the data-representation of a server, but also of web-applications
-        running on this server, and even something like installed extensions, patches,
-        backups and everything else you want to track and manage in your minke-app.
-        
-        Sessions
-        ........
-        A session-class defines the code to be executed for minke-models. Sessions are
-        similar fabric-tasks. Within a session you have access to a connection-object
-        (as implemented by fabric) as well as to the minke-model-object you are working
-        with. So a session could be as simple as running a single shell-command on the
-        remote-machine, up to complex management-routines including manipulating the
-        data of the minke-model-object itself.
-        
 Platform: OS Independent
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Framework :: Django
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: System Administrators
 Classifier: License :: OSI Approved :: BSD License
@@ -104,7 +20,91 @@
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Topic :: Internet :: WWW/HTTP :: Dynamic Content
 Classifier: Topic :: Software Development
 Classifier: Topic :: Software Development :: Libraries :: Application Frameworks
 Classifier: Topic :: System :: Networking :: Monitoring
 Classifier: Topic :: System :: Systems Administration
+License-File: LICENCE
+
+================
+Welcome to Minke
+================
+
+.. image:: https://travis-ci.com/thomst/django-minke.svg?branch=master
+   :target: https://travis-ci.com/thomst/django-minke
+
+.. image:: https://coveralls.io/repos/github/thomst/django-minke/badge.svg
+   :target: https://coveralls.io/github/thomst/django-minke
+
+.. image:: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue
+   :target: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue
+   :alt: python: 3.4, 3.5, 3.6, 3.7, 3.8
+
+.. image:: https://img.shields.io/badge/django-1.11%20%7C%202.0%20%7C%202.1%20%7C%202.2-orange
+   :target: https://img.shields.io/badge/django-1.11%20%7C%202.0%20%7C%202.1%20%7C%202.2-orange
+   :alt: django: 1.11, 2.0, 2.1, 2.2
+
+Links
+=====
+* Minke on github: https://github.com/thomst/django-minke
+* Minke on Read the Docs: https://django-minke.readthedocs.io
+* Getting started: https://django-minke.readthedocs.io/en/latest/docs/gettingstarted.html
+
+A framework for remote-control- and configuration-management-systems
+====================================================================
+Minke is a framework that combines the full power of djangos admin-interface
+with the reliability and configurability of fabric2. A pure open-source- and
+pure python-solution to realize the most different szenarios concerning remote-
+control and configuration-managment.
+
+Imagine you just need to setup some managment-commands for a handful of servers -
+you can do that with minke. Imagine you have lots of servers with different
+setups that you need to group and address seperatly - you can do that with
+minke. Imagine you have servers with multiple subsystems installed on each of them
+and you not just want to manage those systems but also to track configurations,
+version-numbers, installed extensions or modules and to filter for all of those
+values within your backend - you can do that with minke.
+
+Features
+--------
+* full integration with django's admin-site
+* parrallel session-execution through celery
+* realtime monitoring of executed remote-sessions
+* command-line-api using django's management-commands
+* session- and command-history
+
+Concept
+-------
+The main idea of minke is to define an arbitrary data-structure that represents
+your server- and subsystem-landscape as django-models. And then be able to
+run specific remote-tasks for those models right out of their changelist-sites.
+Now those tasks could be anything about remote-control and system-managment, but
+also fetching relevant data to update your django-data-structure itself.
+
+To make this possible there are three main elements:
+
+* hosts,
+* minke-models,
+* and sessions.
+
+Hosts
+.....
+A Host is a django-model that is basically the database-representation of a
+specific ssh-config. It holds every information needed by fabric to connect
+to the remote-system.
+
+Minke-Models
+............
+Minke-models now are all those models that you want to run remote-sessions with.
+This could be the data-representation of a server, but also of web-applications
+running on this server, and even something like installed extensions, patches,
+backups and everything else you want to track and manage in your minke-app.
+
+Sessions
+........
+A session-class defines the code to be executed for minke-models. Sessions are
+similar fabric-tasks. Within a session you have access to a connection-object
+(as implemented by fabric) as well as to the minke-model-object you are working
+with. So a session could be as simple as running a single shell-command on the
+remote-machine, up to complex management-routines including manipulating the
+data of the minke-model-object itself.
```

### Comparing `django-minke-1.2.3.dev0/README.rst` & `django-minke-1.3.0.dev0/README.rst`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/django_minke.egg-info/PKG-INFO` & `django-minke-1.3.0.dev0/django_minke.egg-info/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,98 +1,14 @@
-Metadata-Version: 1.1
+Metadata-Version: 2.1
 Name: django-minke
-Version: 1.2.3.dev0
+Version: 1.3.0.dev0
 Summary: Django- and fabric-based building toolkit for remote-control- and configuration-management-systems.
-Home-page: UNKNOWN
 Author: Thomas Leichtfuß
 Author-email: thomas.leichtfuss@posteo.de
 License: BSD License
-Description: ================
-        Welcome to Minke
-        ================
-        
-        .. image:: https://travis-ci.com/thomst/django-minke.svg?branch=master
-           :target: https://travis-ci.com/thomst/django-minke
-        
-        .. image:: https://coveralls.io/repos/github/thomst/django-minke/badge.svg
-           :target: https://coveralls.io/github/thomst/django-minke
-        
-        .. image:: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue
-           :target: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue
-           :alt: python: 3.4, 3.5, 3.6, 3.7, 3.8
-        
-        .. image:: https://img.shields.io/badge/django-1.11%20%7C%202.0%20%7C%202.1%20%7C%202.2-orange
-           :target: https://img.shields.io/badge/django-1.11%20%7C%202.0%20%7C%202.1%20%7C%202.2-orange
-           :alt: django: 1.11, 2.0, 2.1, 2.2
-        
-        Links
-        =====
-        * Minke on github: https://github.com/thomst/django-minke
-        * Minke on Read the Docs: https://django-minke.readthedocs.io
-        * Getting started: https://django-minke.readthedocs.io/en/latest/docs/gettingstarted.html
-        
-        A framework for remote-control- and configuration-management-systems
-        ====================================================================
-        Minke is a framework that combines the full power of djangos admin-interface
-        with the reliability and configurability of fabric2. A pure open-source- and
-        pure python-solution to realize the most different szenarios concerning remote-
-        control and configuration-managment.
-        
-        Imagine you just need to setup some managment-commands for a handful of servers -
-        you can do that with minke. Imagine you have lots of servers with different
-        setups that you need to group and address seperatly - you can do that with
-        minke. Imagine you have servers with multiple subsystems installed on each of them
-        and you not just want to manage those systems but also to track configurations,
-        version-numbers, installed extensions or modules and to filter for all of those
-        values within your backend - you can do that with minke.
-        
-        Features
-        --------
-        * full integration with django's admin-site
-        * parrallel session-execution through celery
-        * realtime monitoring of executed remote-sessions
-        * command-line-api using django's management-commands
-        * session- and command-history
-        
-        Concept
-        -------
-        The main idea of minke is to define an arbitrary data-structure that represents
-        your server- and subsystem-landscape as django-models. And then be able to
-        run specific remote-tasks for those models right out of their changelist-sites.
-        Now those tasks could be anything about remote-control and system-managment, but
-        also fetching relevant data to update your django-data-structure itself.
-        
-        To make this possible there are three main elements:
-        
-        * hosts,
-        * minke-models,
-        * and sessions.
-        
-        Hosts
-        .....
-        A Host is a django-model that is basically the database-representation of a
-        specific ssh-config. It holds every information needed by fabric to connect
-        to the remote-system.
-        
-        Minke-Models
-        ............
-        Minke-models now are all those models that you want to run remote-sessions with.
-        This could be the data-representation of a server, but also of web-applications
-        running on this server, and even something like installed extensions, patches,
-        backups and everything else you want to track and manage in your minke-app.
-        
-        Sessions
-        ........
-        A session-class defines the code to be executed for minke-models. Sessions are
-        similar fabric-tasks. Within a session you have access to a connection-object
-        (as implemented by fabric) as well as to the minke-model-object you are working
-        with. So a session could be as simple as running a single shell-command on the
-        remote-machine, up to complex management-routines including manipulating the
-        data of the minke-model-object itself.
-        
 Platform: OS Independent
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Framework :: Django
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: System Administrators
 Classifier: License :: OSI Approved :: BSD License
@@ -104,7 +20,91 @@
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Topic :: Internet :: WWW/HTTP :: Dynamic Content
 Classifier: Topic :: Software Development
 Classifier: Topic :: Software Development :: Libraries :: Application Frameworks
 Classifier: Topic :: System :: Networking :: Monitoring
 Classifier: Topic :: System :: Systems Administration
+License-File: LICENCE
+
+================
+Welcome to Minke
+================
+
+.. image:: https://travis-ci.com/thomst/django-minke.svg?branch=master
+   :target: https://travis-ci.com/thomst/django-minke
+
+.. image:: https://coveralls.io/repos/github/thomst/django-minke/badge.svg
+   :target: https://coveralls.io/github/thomst/django-minke
+
+.. image:: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue
+   :target: https://img.shields.io/badge/python-3.4%20%7C%203.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue
+   :alt: python: 3.4, 3.5, 3.6, 3.7, 3.8
+
+.. image:: https://img.shields.io/badge/django-1.11%20%7C%202.0%20%7C%202.1%20%7C%202.2-orange
+   :target: https://img.shields.io/badge/django-1.11%20%7C%202.0%20%7C%202.1%20%7C%202.2-orange
+   :alt: django: 1.11, 2.0, 2.1, 2.2
+
+Links
+=====
+* Minke on github: https://github.com/thomst/django-minke
+* Minke on Read the Docs: https://django-minke.readthedocs.io
+* Getting started: https://django-minke.readthedocs.io/en/latest/docs/gettingstarted.html
+
+A framework for remote-control- and configuration-management-systems
+====================================================================
+Minke is a framework that combines the full power of djangos admin-interface
+with the reliability and configurability of fabric2. A pure open-source- and
+pure python-solution to realize the most different szenarios concerning remote-
+control and configuration-managment.
+
+Imagine you just need to setup some managment-commands for a handful of servers -
+you can do that with minke. Imagine you have lots of servers with different
+setups that you need to group and address seperatly - you can do that with
+minke. Imagine you have servers with multiple subsystems installed on each of them
+and you not just want to manage those systems but also to track configurations,
+version-numbers, installed extensions or modules and to filter for all of those
+values within your backend - you can do that with minke.
+
+Features
+--------
+* full integration with django's admin-site
+* parrallel session-execution through celery
+* realtime monitoring of executed remote-sessions
+* command-line-api using django's management-commands
+* session- and command-history
+
+Concept
+-------
+The main idea of minke is to define an arbitrary data-structure that represents
+your server- and subsystem-landscape as django-models. And then be able to
+run specific remote-tasks for those models right out of their changelist-sites.
+Now those tasks could be anything about remote-control and system-managment, but
+also fetching relevant data to update your django-data-structure itself.
+
+To make this possible there are three main elements:
+
+* hosts,
+* minke-models,
+* and sessions.
+
+Hosts
+.....
+A Host is a django-model that is basically the database-representation of a
+specific ssh-config. It holds every information needed by fabric to connect
+to the remote-system.
+
+Minke-Models
+............
+Minke-models now are all those models that you want to run remote-sessions with.
+This could be the data-representation of a server, but also of web-applications
+running on this server, and even something like installed extensions, patches,
+backups and everything else you want to track and manage in your minke-app.
+
+Sessions
+........
+A session-class defines the code to be executed for minke-models. Sessions are
+similar fabric-tasks. Within a session you have access to a connection-object
+(as implemented by fabric) as well as to the minke-model-object you are working
+with. So a session could be as simple as running a single shell-command on the
+remote-machine, up to complex management-routines including manipulating the
+data of the minke-model-object itself.
```

### Comparing `django-minke-1.2.3.dev0/django_minke.egg-info/SOURCES.txt` & `django-minke-1.3.0.dev0/django_minke.egg-info/SOURCES.txt`

 * *Files 7% similar despite different names*

```diff
@@ -1,7 +1,8 @@
+LICENCE
 MANIFEST.in
 README.rst
 setup.py
 django_minke.egg-info/PKG-INFO
 django_minke.egg-info/SOURCES.txt
 django_minke.egg-info/dependency_links.txt
 django_minke.egg-info/requires.txt
@@ -40,14 +41,17 @@
 minke/management/commands/minkerun.py
 minke/migrations/0001_initial.py
 minke/migrations/0002_auto_20180619_1703.py
 minke/migrations/0003_auto_20190326_1648.py
 minke/migrations/0004_auto_20190703_1319.py
 minke/migrations/0005_auto_20190810_1412.py
 minke/migrations/0006_auto_20200108_1333.py
+minke/migrations/0007_auto_20230404_1646.py
+minke/migrations/0008_auto_20230405_2153.py
+minke/migrations/0009_remove_minkesession_session_data.py
 minke/migrations/__init__.py
 minke/static/minke/css/minke.css
 minke/static/minke/css/minke_form.css
 minke/static/minke/js/minke.js
 minke/templates/minke/change_form.html
 minke/templates/minke/change_list.html
 minke/templates/minke/change_list_results.html
```

### Comparing `django-minke-1.2.3.dev0/minke/admin.py` & `django-minke-1.3.0.dev0/minke/admin.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,11 @@
 # -*- coding: utf-8 -*-
 from pydoc import locate
 from collections import OrderedDict
 
-from django import forms
 from django.contrib.admin.options import IncorrectLookupParameters
 from django.contrib.admin.views.main import ChangeList
 from django.contrib.admin.filters import RelatedOnlyFieldListFilter
 from django.contrib.admin import helpers
 from django.contrib import messages
 from django.contrib import admin
 from django.utils.text import Truncator
@@ -90,15 +89,14 @@
         }),
         (_('Session'), {
             'fields': (
                 'session_name',
                 'session_verbose_name',
                 'session_status',
                 'session_description',
-                'session_data',
             ),
             'classes': ('extrapretty', 'wide')
         }),
         (_('Processing'), {
             'fields': (
                 'proc_status',
                 'pid',
@@ -110,17 +108,17 @@
             'classes': ('extrapretty', 'wide')
         }),
     )
     readonly_fields = fieldsets[0][1]['fields'] + fieldsets[1][1]['fields'] + fieldsets[2][1]['fields']
 
     def minkeobj_view(self, obj):
         opts = obj.minkeobj._meta
-        lookup = "admin:{}_{}_change".format(opts.app_label, opts.model_name)
+        lookup = f"admin:{opts.app_label}_{opts.model_name}_change"
         href = reverse(lookup, args=(obj.minkeobj.id,))
-        return mark_safe('<a href="{}">{}</a>'.format(href, obj.minkeobj))
+        return mark_safe(f'<a href="{href}">{obj.minkeobj}</a>')
     minkeobj_view.short_description = 'Minke-object'
     minkeobj_view.admin_order_field = 'minkeobj_id'
 
     def changelist_view(self, request, extra_context=None):
         display_messages = bool(int(request.GET.get('display_messages', 0)))
         display_commands = bool(int(request.GET.get('display_commands', 0)))
         extra_context = extra_context or dict()
@@ -239,19 +237,18 @@
         choices, extra_attrs = self.get_session_options(request)
         form.fields['session'].choices = choices
         form.fields['session'].widget.extra_attrs = extra_attrs
         return form
 
     def run_sessions(self, request, session_cls, queryset, force_confirm=False):
         confirm = force_confirm or session_cls.confirm
-        fabric_config = None
-        session_data = dict()
         session_form_cls = session_cls.get_form()
         fabric_form_cls = None
         render_params = dict()
+        runtime_data = dict()
 
         # import fabric-form if needed...
         if settings.MINKE_FABRIC_FORM:
             fabric_form_cls = locate(settings.MINKE_FABRIC_FORM)
             if not fabric_form_cls:
                 msg = '{} could not be loaded'.format(settings.MINKE_FABRIC_FORM)
                 raise InvalidMinkeSetup(msg)
@@ -288,39 +285,38 @@
                 render_params['minke_form'] = minke_form
                 render_params['objects'] = queryset
                 render_params['object_list'] = confirm
                 return TemplateResponse(request, 'minke/minke_form.html', render_params)
 
             else:
                 # collect form-data
-                if fabric_form_cls: fabric_config = fabric_form.cleaned_data
-                if session_form_cls: session_data = session_form.cleaned_data
+                if fabric_form_cls:
+                    runtime_data.update(fabric_form.cleaned_data)
+                if session_form_cls:
+                    runtime_data.update(session_form.cleaned_data)
 
         # lets rock...
-        engine.process(session_cls, queryset, session_data, request.user,
-                       fabric_config=fabric_config)
+        engine.process(session_cls, queryset, request.user, runtime_data)
 
     def changelist_view(self, request, extra_context=None):
         """
         Extend the modeladmin-changelist_view by session-processing.
         """
         extra_context = extra_context or dict()
         extra_context['display_session_select'] = extra_context.get('display_session_select', True)
         extra_context['display_session_info'] = extra_context.get('display_session_info', True)
         extra_context['display_session_proc_info'] = extra_context.get('display_session_proc_info', True)
         extra_context['display_messages'] = extra_context.get('display_messages', True)
         extra_context['display_commands'] = extra_context.get('display_commands', False)
 
-        # We perform one registry-reload per request. GET- and POST-request
-        # will need it alike.
+        # We perform one registry-reload per request. GET- and POST-request will need it alike.
         REGISTRY.reload()
 
         # Does this request has something to do with sessions at all?
-        if ('run_sessions' not in request.POST
-        and 'clear_sessions' not in request.POST):
+        if not 'run_sessions' in request.POST and not 'clear_sessions' in request.POST:
             return super().changelist_view(request, extra_context)
 
         # setup
         force_confirm = False
         selected = request.POST.getlist(helpers.ACTION_CHECKBOX_NAME)
         select_across = bool(int(request.POST.get('select_across', 0)))
         redirect_url = request.get_full_path()
@@ -372,49 +368,27 @@
                 redirect_url += delimiter + 'all='
 
             # run_sessions might want to render a minke- or session-form
             response = self.run_sessions(request, session_cls, queryset, force_confirm)
             return response or HttpResponseRedirect(redirect_url)
 
 
-def get_ssh_options():
-    choices = ((None, '---------'),)
-    choices += tuple(((k, k) for k in settings.MINKE_HOST_CONFIG.keys()))
-    return choices
-
-
-class HostAdminForm(forms.ModelForm):
-    class Meta:
-        model = Host
-        exclude = tuple()
-        widgets = dict(config=forms.Select(choices=get_ssh_options()))
-
-
-class HostGroupAdminForm(forms.ModelForm):
-    class Meta:
-        model = HostGroup
-        exclude = tuple()
-        widgets = dict(config=forms.Select(choices=get_ssh_options()))
-
-
 @admin.register(Host)
 class HostAdmin(MinkeAdmin):
     model = Host
-    form = HostAdminForm
     list_display = ('name', 'verbose_name', 'username', 'hostname', 'port', 'disabled')
     list_editable = ('disabled',)
     search_fields = ('name', 'hostname')
     ordering = ('name',)
-    list_filter = (StatusFilter, 'disabled')
+    list_filter = (StatusFilter, 'disabled', 'groups')
 
 
 @admin.register(HostGroup)
 class HostGroupAdmin(admin.ModelAdmin):
     model = HostGroup
-    form = HostGroupAdminForm
     list_display = ('name',)
     search_fields = ('name',)
     ordering = ('name',)
 
 
 class CommandResultAdmin(admin.ModelAdmin):
     model = CommandResult
```

### Comparing `django-minke-1.2.3.dev0/minke/contrib/commands/admin.py` & `django-minke-1.3.0.dev0/minke/contrib/commands/admin.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/contrib/commands/migrations/0001_initial.py` & `django-minke-1.3.0.dev0/minke/contrib/commands/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/contrib/commands/models.py` & `django-minke-1.3.0.dev0/minke/contrib/commands/models.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/contrib/commands/sessions.py` & `django-minke-1.3.0.dev0/minke/contrib/commands/sessions.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/engine.py` & `django-minke-1.3.0.dev0/minke/engine.py`

 * *Files 4% similar despite different names*

```diff
@@ -6,64 +6,62 @@
 from .messages import Message
 from .messages import ExceptionMessage
 from .models import MinkeSession
 from .tasks import process_session
 from .tasks import cleanup
 
 
-def process(session_cls, queryset, session_data, user,
-            fabric_config=None, wait=False, console=False):
+def process(session_cls, queryset, user, runtime_data=None, wait=False, console=False):
     """
     Initiate and run celery-tasks.
     """
     # TODO: Add a MinkeSession lock. To lock the host should be optional.
     MinkeSession.objects.clear_currents(user, queryset)
     hosts = queryset.get_hosts()
     lock = hosts.filter(disabled=False).get_lock()
 
     # group sessions by hosts
     session_groups = dict()
     for minkeobj in queryset.select_related_hosts():
         host = minkeobj.get_host()
 
         session = MinkeSession()
-        session.init(user, minkeobj, session_cls, session_data)
+        session.init(user, minkeobj, session_cls)
 
         # Skip disabled or locked hosts...
         if host.disabled:
-            msg = '{}: Host is disabled.'.format(minkeobj)
+            msg = f'{minkeobj}: Host is disabled.'
             session.messages.add(Message(msg, 'error'), bulk=False)
             session.cancel()
-            if console: session.prnt()
+            if console:
+                session.prnt()
         elif host.lock and host.lock != lock:
-            msg = '{}: Host is locked.'.format(minkeobj)
+            msg = f'{minkeobj}: Host is locked.'
             session.messages.add(Message(msg, 'error'), bulk=False)
             session.cancel()
-            if console: session.prnt()
+            if console:
+                session.prnt()
 
         # otherwise group sessions by hosts...
         else:
             if host not in session_groups:
                 session_groups[host] = list()
             session_groups[host].append(session)
 
     # Stop here if no valid hosts are left...
-    if not session_groups: return
-
-    # merge fabric-config and invoke-config
-    config = session_cls.invoke_config.copy()
-    config.update(fabric_config or dict())
+    if not session_groups:
+        return
 
 
     # run celery-tasks...
     results = list()
     for host, sessions in session_groups.items():
 
         # get process_session_signatures for all sessions
-        signatures = [process_session.si(host.id, s.id, config) for s in sessions]
+        signatures = [process_session.si(host.id, s.id, runtime_data) for s in sessions]
 
         # To support parrallel execution per host we wrap the signatures in a group.
         # NOTE: Since we append the cleanup-task the construct is essentially the
         # same as a chord which is not supported by all result-backends (s. celery-docs).
         if session_cls.parrallel_per_host:
             signatures = [group(*signatures)]
```

### Comparing `django-minke-1.2.3.dev0/minke/exceptions.py` & `django-minke-1.3.0.dev0/minke/exceptions.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/filters.py` & `django-minke-1.3.0.dev0/minke/filters.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/forms.py` & `django-minke-1.3.0.dev0/minke/forms.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/management/commands/minkeadm.py` & `django-minke-1.3.0.dev0/minke/management/commands/minkeadm.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/management/commands/minkerun.py` & `django-minke-1.3.0.dev0/minke/management/commands/minkerun.py`

 * *Files 2% similar despite different names*

```diff
@@ -154,16 +154,17 @@
             changelist = modeladmin.get_changelist_instance(request)
         except (IncorrectLookupParameters, FieldError):
             msg = 'Invalid url-query: {}'.format(url_query)
             raise CommandError(msg)
         return changelist.get_queryset(request)
 
     def get_form_data(self, options, session_cls):
-        form_cls = session_cls.form
-        if not session_cls.form: return dict()
+        form_cls = session_cls.get_form()
+        if not form_cls:
+            return dict()
 
         # form-data passed via command-line?
         form_data = options['form_data']
         if form_data:
             try:
                 form_data = eval('dict({})'.format(form_data))
                 form = form_cls(form_data)
@@ -227,8 +228,8 @@
             form_data = self.get_form_data(options, session_cls)
         except CommandError as err:
             self.print_usage_and_quit(err)
 
         if options['list_items']:
             for obj in queryset: print(obj)
         else:
-            process(session_cls, queryset, form_data, user, console=True)
+            process(session_cls, queryset, user, form_data, console=True)
```

### Comparing `django-minke-1.2.3.dev0/minke/messages.py` & `django-minke-1.3.0.dev0/minke/messages.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/migrations/0001_initial.py` & `django-minke-1.3.0.dev0/minke/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/migrations/0003_auto_20190326_1648.py` & `django-minke-1.3.0.dev0/minke/migrations/0003_auto_20190326_1648.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/migrations/0004_auto_20190703_1319.py` & `django-minke-1.3.0.dev0/minke/migrations/0004_auto_20190703_1319.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/migrations/0005_auto_20190810_1412.py` & `django-minke-1.3.0.dev0/minke/migrations/0005_auto_20190810_1412.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/models.py` & `django-minke-1.3.0.dev0/minke/models.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,28 +1,29 @@
 # -*- coding: utf-8 -*-
 
-import re, os, signal, datetime
+import re
+import os
+import signal
+import datetime
 from time import time
-from collections import OrderedDict
-
 from fabric2.runners import Result
-from celery.task.control import revoke
 
 from django.db import models
 from django.db import transaction
 from django.contrib.auth.models import User
 from django.contrib.contenttypes.fields import GenericForeignKey
 from django.contrib.contenttypes.fields import GenericRelation
 from django.contrib.contenttypes.models import ContentType
 from django.core.exceptions import FieldError
 from django.utils.translation import gettext
 from django.utils.translation import gettext_lazy as _
 
 from .exceptions import InvalidMinkeSetup
 from .utils import JSONField
+from .utils import valid_yaml_configuration
 
 
 class MinkeSessionQuerySet(models.QuerySet):
     """
     Working with current sessions.
     Which are those that are rendered within the changelist.
     """
@@ -93,18 +94,14 @@
         blank=True, null=True, max_length=128,
         verbose_name=_("Session's description"),
         help_text=_('Doc-string of the session-class.'))
     session_status = models.CharField(
         max_length=128, choices=SESSION_CHOICES,
         verbose_name=_("Session-status"),
         help_text=_('Mostly set by the session-code itself.'))
-    session_data = JSONField(
-        blank=True, null=True,
-        verbose_name=_("Session's extra-data"),
-        help_text=_('Data coming from a session-form.'))
 
     # the minkeobj to work on
     minkeobj_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
     minkeobj_id = models.PositiveIntegerField()
     minkeobj = GenericForeignKey('minkeobj_type', 'minkeobj_id')
 
     # execution-data of the session
@@ -135,27 +132,26 @@
     created_time = models.DateTimeField(
         auto_now_add=True,
         verbose_name=_("Created-time"),
         help_text=_('Time the session has been initiated.'))
     current = models.BooleanField(default=True)
 
     def __str__(self):
-        return '{} on {}'.format(self.session_name, self.minkeobj)
+        return f'{self.session_name} on {self.minkeobj}'
 
-    def init(self, user, minkeobj, session_cls, session_data):
+    def init(self, user, minkeobj, session_cls):
         """
         Initialize a session. Setup the session-attributes and save it.
         """
         self.proc_status = 'initialized'
         self.user = user
         self.minkeobj = minkeobj
         self.session_name = session_cls.__name__
         self.session_verbose_name = session_cls.verbose_name
         self.session_description = session_cls.__doc__
-        self.session_data = session_data
         self.save()
 
     @transaction.atomic
     def start(self):
         """
         Start a session. Update proc_status, start_time and pid.
         Since the cancel-method is called asynchrouniously to the whole session-
@@ -437,40 +433,45 @@
 
     class Meta:
         ordering = ('session_id', 'created_time')
         verbose_name = _('Message')
         verbose_name_plural = _('Messages')
 
 
-# FIXME: Make the config attribute a yaml data field.
 class HostGroup(models.Model):
     """
     A Group of hosts. (Not sure if this is practical.)
     """
     name = models.CharField(
         max_length=128, unique=True,
         verbose_name=_('Group-Name'),
         help_text=_('Unique group-name.'))
     comment = models.TextField(
         blank=True, null=True,
         verbose_name=_('Comment'),
         help_text=_('Something about the group.'))
-    config = models.CharField(
-        max_length=255, blank=True, null=True,
-        verbose_name=_('Fabric-/Invoke-config'),
-        help_text=_('Use config as specified in MINKE_HOST_CONFIG.'))
+    config = models.TextField(
+        blank=True,
+        validators=[valid_yaml_configuration],
+        verbose_name=_('Fabric and invoke configuration'),
+        help_text=_('A yaml formatted fabric/invoke configuration.')
+        )
 
     class Meta:
         ordering = ['name']
         verbose_name = _('Host-Group')
         verbose_name_plural = _('Host-Groups')
 
     def __str__(self):
         return self.name
 
+    def save(self, *args, **kwargs):
+        self.full_clean()
+        return super().save(*args, **kwargs)
+
 
 class HostQuerySet(models.QuerySet):
     """
     Besides the get_lock-method this is an imitation of the minkemodel-queryset-api.
     """
     def get_lock(self):
         """
@@ -497,15 +498,14 @@
     def select_related_hosts(self):
         """
         Return itself (minkemodel-api).
         """
         return self
 
 
-# FIXME: Make the config attribute a yaml data field.
 class Host(models.Model):
     """
     This model is mainly a ssh-config.
     Each host represents an unique ssh-connection.
     It also imitates the minkemodel-api to normalize the way the engine
     runs sessions on them.
     """
@@ -533,22 +533,27 @@
         blank=True, null=True,
         verbose_name=_('Port number.'),
         help_text=_('Port number to connect on the remote host.'))
     comment = models.TextField(
         blank=True, null=True,
         verbose_name=_('Comment'),
         help_text=_('Something about the host.'))
-    group = models.ForeignKey(HostGroup,
-        blank=True, null=True, on_delete=models.SET_NULL,
+    groups = models.ManyToManyField(
+        HostGroup,
+        blank=True,
+        related_name="hosts",
         verbose_name=_('Hostgroup'),
-        help_text=_('The group this host belongs to.'))
-    config = models.CharField(
-        max_length=255, blank=True, null=True,
-        verbose_name=_('Fabric-/Invoke-config'),
-        help_text=_('Use config as specified in MINKE_HOST_CONFIG.'))
+        help_text=_('Hostgroups this host belongs to.')
+        )
+    config = models.TextField(
+        blank=True,
+        validators=[valid_yaml_configuration],
+        verbose_name=_('Fabric and invoke configuration'),
+        help_text=_('A yaml formatted fabric/invoke configuration.')
+        )
     disabled = models.BooleanField(
         default=False,
         verbose_name=_('Disabled'),
         help_text=_('Disabled hosts won\'t be accessed by minke.'))
     lock = models.CharField(
         max_length=20, blank=True, null=True,
         verbose_name=_('Lock'),
@@ -578,14 +583,18 @@
         ordering = ['name']
         verbose_name = _('Host')
         verbose_name_plural = _('Hosts')
 
     def __str__(self):
         return self.name
 
+    def save(self, *args, **kwargs):
+        self.full_clean()
+        return super().save(*args, **kwargs)
+
 
 class MinkeQuerySet(models.QuerySet):
     """
     A queryset-api to work with related hosts.
     This api is mainly used by the engine-module.
     """
     def get_hosts(self):
@@ -650,14 +659,15 @@
             lookup = '__'.join(lookup_list[1:])
         return lookup
 
     def get_host(self):
         """
         Return the related host-instance.
         """
+        # return self.__class__.objects.filter(pk__in=self.pk).get_hosts()[0]
         host = self
         for attr in self.HOST_LOOKUP.split('__'):
             host = getattr(host, attr, None)
         if not isinstance(host, Host):
             msg = "Invalid host-lookup: {}".format(self.HOST_LOOKUP)
             raise InvalidMinkeSetup(msg)
         else:
```

### Comparing `django-minke-1.2.3.dev0/minke/serializers.py` & `django-minke-1.3.0.dev0/minke/serializers.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/sessions.py` & `django-minke-1.3.0.dev0/minke/sessions.py`

 * *Files 0% similar despite different names*

```diff
@@ -363,15 +363,15 @@
 
     @property
     def data(self):
         """
         Refers to :attr:`.models.MinkeSession.session_data`.
         This model-field holds all the data that comes from :attr:`.form`.
         """
-        return self._db.session_data
+        return self._c.session_data
 
     def stop(self, *arg, **kwargs):
         """Interrupt the session's processing.
 
         This method could be called twice. The first time it will initiate a
         soft interruption which means a current remote-process won't be
         interrupted. The session will be stopped subsequently.
```

### Comparing `django-minke-1.2.3.dev0/minke/static/minke/css/minke.css` & `django-minke-1.3.0.dev0/minke/static/minke/css/minke.css`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/static/minke/js/minke.js` & `django-minke-1.3.0.dev0/minke/static/minke/js/minke.js`

 * *Files 2% similar despite different names*

#### js-beautify {}

```diff
@@ -140,17 +140,19 @@
     $(document).ready(function() {
 
         // initiate message-toggles
         $('div.session_select a.message-toggle').click(toggleAllMessageLists);
         $('tr.session a.message-toggle').click(toggleMessageList);
 
         // initialize session-objects...
-        $('tr.session.initialized,tr.session.running,tr.session.stopping').each(function(i, e) {
-            sessions[$(e).data('id')] = new Session(e)
-        });
+        $('tr.session.initialized,tr.session.running,tr.session.stopping').each(
+            function(i, e) {
+                sessions[$(e).data('id')] = new Session(e)
+            }
+        );
 
         // do we work with sessions?
         if (!$.isEmptyObject(sessions)) {
 
             // setup header-csrf-token - to get it work with django-rest-framework
             $.ajaxSetup({
                 headers: {
```

### Comparing `django-minke-1.2.3.dev0/minke/tasks.py` & `django-minke-1.3.0.dev0/minke/tasks.py`

 * *Files 19% similar despite different names*

```diff
@@ -14,66 +14,46 @@
 
 from . import settings
 from .models import Host
 from .models import MinkeSession
 from .exceptions import SessionError
 from .sessions import REGISTRY
 from .messages import ExceptionMessage
-from .settings import MINKE_HOST_CONFIG
-from .settings import MINKE_FABRIC_CONFIG
+from .fabrictools import FabricConfig
 
 
 logger = logging.getLogger(__name__)
 
 
 class SessionProcessor:
     """
     Process sessions.
     """
-    def __init__(self, host_id, session_id, session_config):
-        host = Host.objects.select_related('group').get(pk=host_id)
+    def __init__(self, host_id, session_id, runtime_data):
+        minke_session = MinkeSession.objects.get(pk=session_id)
+        REGISTRY.reload(minke_session.session_name)
+        session_cls = REGISTRY[minke_session.session_name]
+        host = Host.objects.get(pk=host_id)
         hostname = host.hostname or host.name
-        config = MINKE_FABRIC_CONFIG.clone()
-        self.host = host
-
-        # At first try to load the hostgroup- and host-config...
-        for obj in (host.group, host):
-            if not obj or not obj.config: continue
-            if obj.config in MINKE_HOST_CONFIG:
-                config.load_snakeconfig(MINKE_HOST_CONFIG[obj.config])
-            else:
-                msg = 'Invalid MINKE_HOST_CONFIG for {}'.format(obj)
-                logger.warning(msg)
-
-        # At least load the session-config...
-        config.load_snakeconfig(session_config or dict())
-
-        # Initialize the connection...
+        config = FabricConfig(host, session_cls, runtime_data)
         self.con = Connection(hostname, host.username, host.port, config=config)
-
-        # Initialize the session...
-        self.minke_session = MinkeSession.objects.get(pk=session_id)
-        REGISTRY.reload(self.minke_session.session_name)
-        session_cls = REGISTRY[self.minke_session.session_name]
-        self.session = session_cls(self.con, self.minke_session)
+        self.session = session_cls(self.con, minke_session)
 
     def run(self):
+        """
+        Run the task.
+        """
         try:
             started = self.session.start()
-            if not started: return
+            if not started:
+                return
 
             try:
                 self.session.process()
 
-            # Since task-interruption could happen all along between
-            # session.start() and session.end() we handle it in the outer
-            # try-construct.
-            except KeyboardInterrupt:
-                raise
-
             # A SessionError might be raised by from the process method of a
             # session itself. It is a convenient way to end a session with an
             # error status.
             except SessionError as exc:
                 self.session.set_status('error')
                 for msg in exc.args:
                     self.session.add_msg(msg, 'error')
@@ -99,29 +79,30 @@
                 else:
                     # TODO: relegate to the log.
                     self.session.add_msg('An error occurred.', 'error')
 
             else:
                 self.session.end()
 
-        # task-interruption
+        # Since task-interruption could happen all along between session.start()
+        # and session.end() we handle it in the outer try-construct.
         except KeyboardInterrupt:
             self.session.end()
 
         # at least close the ssh-connection
         finally:
             self.con.close()
 
 
 @shared_task(bind=True)
-def process_session(task, host_id, session_id, config):
+def process_session(task, host_id, session_id, runtime_data):
     """
     Task for session-processing.
     """
-    processor = SessionProcessor(host_id, session_id, config)
+    processor = SessionProcessor(host_id, session_id, runtime_data)
     signal.signal(signal.SIGUSR1, processor.session.stop)
     processor.run()
 
 @shared_task
 def cleanup(host_id):
     """
     Task to release the host's lock.
```

### Comparing `django-minke-1.2.3.dev0/minke/templates/minke/change_list.html` & `django-minke-1.3.0.dev0/minke/templates/minke/change_list.html`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/templates/minke/change_list_results.html` & `django-minke-1.3.0.dev0/minke/templates/minke/change_list_results.html`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/templates/minke/minke_form.html` & `django-minke-1.3.0.dev0/minke/templates/minke/minke_form.html`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/templates/minke/session.html` & `django-minke-1.3.0.dev0/minke/templates/minke/session.html`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/templates/minke/session_select.html` & `django-minke-1.3.0.dev0/minke/templates/minke/session_select.html`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/templates/minke/session_switch.html` & `django-minke-1.3.0.dev0/minke/templates/minke/session_switch.html`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/templatetags/minke.py` & `django-minke-1.3.0.dev0/minke/templatetags/minke.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/urls.py` & `django-minke-1.3.0.dev0/minke/urls.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/minke/views.py` & `django-minke-1.3.0.dev0/minke/views.py`

 * *Files identical despite different names*

### Comparing `django-minke-1.2.3.dev0/setup.py` & `django-minke-1.3.0.dev0/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -32,14 +32,15 @@
     packages=find_packages(exclude=["tests"]),
     include_package_data=True,
     install_requires=[
         "Django>=1.11,<3.0",
         "fabric2>=2.4.0",
         "celery>=4.2.2,<5.0.0",
         "djangorestframework>=3.9.2",
+        "pyyaml",
     ],
     classifiers=[
         dev_status,
         "Framework :: Django",
         "Environment :: Web Environment",
         "Intended Audience :: Developers",
         "Intended Audience :: System Administrators",
```

