# Comparing `tmp/django-chatapp-1.3.tar.gz` & `tmp/django-chatapp-1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-chatapp-1.3.tar", last modified: Mon Mar 13 09:04:36 2023, max compression
+gzip compressed data, was "django-chatapp-1.4.tar", last modified: Sat Mar 25 06:33:04 2023, max compression
```

## Comparing `django-chatapp-1.3.tar` & `django-chatapp-1.4.tar`

### file list

```diff
@@ -1,69 +1,69 @@
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.936966 django-chatapp-1.3/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     1070 2023-03-05 14:24:31.000000 django-chatapp-1.3/LICENSE
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      106 2023-03-06 09:57:28.000000 django-chatapp-1.3/MANIFEST.in
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     5103 2023-03-13 09:04:36.936966 django-chatapp-1.3/PKG-INFO
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     4290 2023-03-13 09:02:24.000000 django-chatapp-1.3/README.md
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.932966 django-chatapp-1.3/chatapp/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)        0 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/__init__.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     2361 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/admin.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      259 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/apps.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    12810 2023-03-06 10:35:22.000000 django-chatapp-1.3/chatapp/consumers.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     6272 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/jalali.py
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.932966 django-chatapp-1.3/chatapp/migrations/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     6775 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/migrations/0001_initial.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)        0 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/migrations/__init__.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     6035 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/models.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      157 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/routing.py
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.928966 django-chatapp-1.3/chatapp/static/
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.928966 django-chatapp-1.3/chatapp/static/django_chat_app/
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.932966 django-chatapp-1.3/chatapp/static/django_chat_app/css/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    19698 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/css/custom.css
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    29636 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/css/custom.scss
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    23886 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/css/supporter.css
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    37001 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/css/supporter.scss
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.932966 django-chatapp-1.3/chatapp/static/django_chat_app/font/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    98892 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/font/vazir-medium.ttf
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    54120 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/font/vazir-medium.woff
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.936966 django-chatapp-1.3/chatapp/static/django_chat_app/img/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      788 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/chat-room.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      448 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/close.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      255 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/copy.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      373 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/delete.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      228 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/double-check.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      316 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/edit.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     1007 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/emoji.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     1679 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/game.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      370 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/gotodown.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     1468 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/loader.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     1844 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/o.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      154 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/plus.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      298 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/reply.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      149 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/report.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      516 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/send.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      205 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/single-check.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     1279 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/supporter.png
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     1494 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/img/x.png
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.936966 django-chatapp-1.3/chatapp/static/django_chat_app/js/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    40934 2023-03-13 08:49:53.000000 django-chatapp-1.3/chatapp/static/django_chat_app/js/client.js
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    32492 2023-03-13 08:50:03.000000 django-chatapp-1.3/chatapp/static/django_chat_app/js/supporter.js
--rw-rw-r--   0 peaka     (1000) peaka     (1000)   569433 2023-03-01 10:57:47.000000 django-chatapp-1.3/chatapp/static/django_chat_app/js/vue3.js
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.936966 django-chatapp-1.3/chatapp/templates/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    22820 2023-03-06 10:34:47.000000 django-chatapp-1.3/chatapp/templates/client.html
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    27765 2023-03-06 10:34:22.000000 django-chatapp-1.3/chatapp/templates/supporter.html
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.936966 django-chatapp-1.3/chatapp/templatetags/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)        0 2023-03-06 07:49:27.000000 django-chatapp-1.3/chatapp/templatetags/__init__.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      137 2023-03-06 08:24:43.000000 django-chatapp-1.3/chatapp/templatetags/chatapp.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)       60 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/tests.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      813 2023-03-13 08:51:11.000000 django-chatapp-1.3/chatapp/urls.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     4333 2023-03-05 08:52:29.000000 django-chatapp-1.3/chatapp/utils.py
--rw-rw-r--   0 peaka     (1000) peaka     (1000)    17732 2023-03-13 08:51:35.000000 django-chatapp-1.3/chatapp/views.py
-drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-13 09:04:36.936966 django-chatapp-1.3/django_chatapp.egg-info/
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     5103 2023-03-13 09:04:36.000000 django-chatapp-1.3/django_chatapp.egg-info/PKG-INFO
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     1936 2023-03-13 09:04:36.000000 django-chatapp-1.3/django_chatapp.egg-info/SOURCES.txt
--rw-rw-r--   0 peaka     (1000) peaka     (1000)        1 2023-03-13 09:04:36.000000 django-chatapp-1.3/django_chatapp.egg-info/dependency_links.txt
--rw-rw-r--   0 peaka     (1000) peaka     (1000)        1 2023-03-13 09:04:36.000000 django-chatapp-1.3/django_chatapp.egg-info/not-zip-safe
--rw-rw-r--   0 peaka     (1000) peaka     (1000)       23 2023-03-13 09:04:36.000000 django-chatapp-1.3/django_chatapp.egg-info/requires.txt
--rw-rw-r--   0 peaka     (1000) peaka     (1000)        8 2023-03-13 09:04:36.000000 django-chatapp-1.3/django_chatapp.egg-info/top_level.txt
--rw-rw-r--   0 peaka     (1000) peaka     (1000)      109 2023-03-05 09:04:49.000000 django-chatapp-1.3/pyproject.toml
--rw-rw-r--   0 peaka     (1000) peaka     (1000)       76 2023-03-13 09:04:36.940966 django-chatapp-1.3/setup.cfg
--rw-rw-r--   0 peaka     (1000) peaka     (1000)     1263 2023-03-13 09:02:41.000000 django-chatapp-1.3/setup.py
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.076357 django-chatapp-1.4/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1070 2023-03-17 22:50:48.000000 django-chatapp-1.4/LICENSE
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      106 2023-03-17 22:51:02.000000 django-chatapp-1.4/MANIFEST.in
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     8917 2023-03-25 06:33:04.076357 django-chatapp-1.4/PKG-INFO
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     8068 2023-03-23 13:30:14.000000 django-chatapp-1.4/README.md
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.040357 django-chatapp-1.4/chatapp/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)        0 2023-03-01 10:57:47.000000 django-chatapp-1.4/chatapp/__init__.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     2236 2023-03-23 10:07:11.000000 django-chatapp-1.4/chatapp/admin.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      259 2023-03-05 08:42:23.000000 django-chatapp-1.4/chatapp/apps.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    13872 2023-03-23 10:07:24.000000 django-chatapp-1.4/chatapp/consumers.py
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.040357 django-chatapp-1.4/chatapp/migrations/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     6775 2023-03-23 10:04:47.000000 django-chatapp-1.4/chatapp/migrations/0001_initial.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)        0 2023-03-23 10:04:47.000000 django-chatapp-1.4/chatapp/migrations/__init__.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     5473 2023-03-23 10:07:52.000000 django-chatapp-1.4/chatapp/models.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      157 2023-03-01 10:57:47.000000 django-chatapp-1.4/chatapp/routing.py
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.028357 django-chatapp-1.4/chatapp/static/
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.028357 django-chatapp-1.4/chatapp/static/django_chatapp/
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.044357 django-chatapp-1.4/chatapp/static/django_chatapp/css/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    20083 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/css/client.css
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    30564 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/css/client.scss
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    25431 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/css/supporter.css
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    39095 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/css/supporter.scss
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.048357 django-chatapp-1.4/chatapp/static/django_chatapp/font/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    98892 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/font/vazir-medium.ttf
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    54120 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/font/vazir-medium.woff
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.060357 django-chatapp-1.4/chatapp/static/django_chatapp/img/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      788 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/chat-room.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      448 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/close.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      255 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/copy.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      373 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/delete.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      228 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/double-check.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      316 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/edit.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1007 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/emoji.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1679 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/game.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      370 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/gotodown.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1468 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/loader.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1844 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/o.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      154 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/plus.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      298 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/reply.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      149 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/report.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      516 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/send.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      205 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/single-check.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1279 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/supporter.png
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1494 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/img/x.png
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.064357 django-chatapp-1.4/chatapp/static/django_chatapp/js/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    51465 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/js/client.js
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    45766 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/js/supporter.js
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    69516 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/js/vue-i18n.js
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)   167908 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/js/vue3.js
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.064357 django-chatapp-1.4/chatapp/static/django_chatapp/song/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    10911 2023-03-23 10:03:55.000000 django-chatapp-1.4/chatapp/static/django_chatapp/song/send.mp3
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.068357 django-chatapp-1.4/chatapp/templates/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    19454 2023-03-23 10:06:07.000000 django-chatapp-1.4/chatapp/templates/client.html
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    26334 2023-03-23 10:06:07.000000 django-chatapp-1.4/chatapp/templates/supporter.html
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.068357 django-chatapp-1.4/chatapp/templatetags/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)        0 2023-03-05 09:17:19.000000 django-chatapp-1.4/chatapp/templatetags/__init__.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)      137 2023-03-17 19:52:40.000000 django-chatapp-1.4/chatapp/templatetags/chatapp.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1158 2023-03-23 10:08:20.000000 django-chatapp-1.4/chatapp/urls.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     2861 2023-03-23 10:08:34.000000 django-chatapp-1.4/chatapp/utils.py
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)    16052 2023-03-23 10:08:53.000000 django-chatapp-1.4/chatapp/views.py
+drwxrwxr-x   0 peaka     (1000) peaka     (1000)        0 2023-03-25 06:33:04.072357 django-chatapp-1.4/django_chatapp.egg-info/
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     8917 2023-03-25 06:33:03.000000 django-chatapp-1.4/django_chatapp.egg-info/PKG-INFO
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1948 2023-03-25 06:33:03.000000 django-chatapp-1.4/django_chatapp.egg-info/SOURCES.txt
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)        1 2023-03-25 06:33:03.000000 django-chatapp-1.4/django_chatapp.egg-info/dependency_links.txt
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)        1 2023-03-25 06:33:03.000000 django-chatapp-1.4/django_chatapp.egg-info/not-zip-safe
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)       23 2023-03-25 06:33:03.000000 django-chatapp-1.4/django_chatapp.egg-info/requires.txt
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)        8 2023-03-25 06:33:03.000000 django-chatapp-1.4/django_chatapp.egg-info/top_level.txt
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)       76 2023-03-25 06:33:04.076357 django-chatapp-1.4/setup.cfg
+-rw-rw-r--   0 peaka     (1000) peaka     (1000)     1299 2023-03-23 13:34:16.000000 django-chatapp-1.4/setup.py
```

### Comparing `django-chatapp-1.3/LICENSE` & `django-chatapp-1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/admin.py` & `django-chatapp-1.4/chatapp/admin.py`

 * *Files 7% similar despite different names*

```diff
@@ -35,40 +35,38 @@
         report_numbers=0
     )
 
 
 # write admin models
 class SupporterModel_Admin(admin.ModelAdmin):
     list_display = ['user', 'supporter_uid', 'full_name', 'is_active']
-    search_field = ['supporter_uid', 'fullname']
+    search_field = ['supporter_uid']
     ordering = ['-id']
 
     
 class ChatModel_Admin(admin.ModelAdmin):
     list_display = ['id', 'client', 'supporter', 'sender', 'is_seen']
-    search_field = ['supporter']
     ordering = ['-id']
 
     
 class UserChatModel_Admin(admin.ModelAdmin):
-    list_display = ['user_chat_uid', 'j_created', 'is_blocked']
-    search_field = ['user_chat_uid', 'email', 'phone', 'is_blocked']
+    list_display = ['user_chat_uid', 'have_supporter', 'created', 'is_blocked']
+    search_field = ['user_chat_uid']
     ordering = ['-id']
     actions = [del_users_more_30d, del_users_isblocked, unblock_users]
 
     
 class ReadyChatModel_Admin(admin.ModelAdmin):
     list_display = ['subject', 'supporter', 'is_public']
-    search_field = ['subject', 'supporter', 'is_public']
+    search_field = ['subject']
     ordering = ['-id']
     
 
 class ReportUserModel_Admin(admin.ModelAdmin):
-    list_display = ['user', 'item', 'j_created']
-    search_field = ['user', 'item']
+    list_display = ['user', 'item', 'created']
     ordering = ['-id']
 
 
 admin.site.register(SupporterModel, SupporterModel_Admin)
 admin.site.register(ChatModel, ChatModel_Admin)
 admin.site.register(UserChatModel, UserChatModel_Admin)
 admin.site.register(ReadyChatModel, ReadyChatModel_Admin)
```

### Comparing `django-chatapp-1.3/chatapp/consumers.py` & `django-chatapp-1.4/chatapp/consumers.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,34 +1,35 @@
 import json
 from channels.generic.websocket import WebsocketConsumer
 from asgiref.sync import async_to_sync
-from django.utils import timezone
-# from channels.db import database_sync_to_async
+from .utils import get_hour_min
 from .models import (
     SupporterModel, 
     UserChatModel,
     ChatModel
 )
 
 
-# url: /ws/<str:type>/chat/<str:username>/
+# route: /ws/<str:type>/chat/<str:username>/
 class ChatConsumer(WebsocketConsumer):
     
     def connect(self):
+
         self.user_id = self.scope['url_route']['kwargs']['username']
         self.type = self.scope['url_route']['kwargs']['type']
-        self.user = ''
+        self.user = None
 
         if self.type == 'supporter':
 
             self.group_name1 = f'chat_supporter_{self.user_id}'
             self.group_name2 = 'unread_msg_board'
 
             if SupporterModel.objects.filter(supporter_uid=self.user_id, is_active=True).exists():
                 self.user = SupporterModel.objects.get(supporter_uid=self.user_id, is_active=True)
+
                 async_to_sync(self.channel_layer.group_add)(
                     self.group_name1,
                     self.channel_name
                 )
                 async_to_sync(self.channel_layer.group_add)(
                     self.group_name2,
                     self.channel_name
@@ -36,138 +37,144 @@
                 self.accept()
 
         elif self.type == 'client':
 
             self.group_name = f"chat_client_{self.user_id}"
 
             if UserChatModel.objects.filter(user_chat_uid=self.user_id, is_blocked=False).exists():
+
                 self.user = UserChatModel.objects.get(user_chat_uid=self.user_id, is_blocked=False)
                 async_to_sync(self.channel_layer.group_add)(
                     self.group_name,
                     self.channel_name
                 )
                 self.accept()
 
+
     def disconnect(self, close_code):
+
         if self.type == 'client':
             async_to_sync(self.channel_layer.group_discard)(
                 self.group_name,
                 self.channel_name
             )
+
         elif self.type == 'supporter':
             async_to_sync(self.channel_layer.group_discard)(
                 self.group_name1,
                 self.channel_name
             )
             async_to_sync(self.channel_layer.group_discard)(
                 self.group_name2,
                 self.channel_name
             )
 
+
     def receive(self, text_data=None, bytes_data=None):
-        if text_data:
+
+        if text_data and not bytes_data:
 
             text_data_json = json.loads(text_data)
             # print(self.type.upper(), text_data_json)
 
             # send delete message to client
             if self.type == 'supporter' and text_data_json.get('_type_request') == 'del':
+
                 chat = ChatModel.objects.get(
                     id=text_data_json.get('id'),
                     sender='supporter'
                 )
                 chat.is_deleted = True
                 chat.save()
 
                 user_group_name = f"chat_client_{text_data_json['client_id']}" 
                 async_to_sync(self.channel_layer.group_send)(
-                    user_group_name,
-                    {
+                    user_group_name, {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
 
             
             # send delete message to supporter
             if self.type == 'client' and text_data_json.get('_type_request') == 'del':
+
                 chat = ChatModel.objects.get(
                     id=text_data_json.get('id'),
                     sender='client'
                 )
                 chat.is_deleted = True
                 chat.save()
 
                 async_to_sync(self.channel_layer.group_send)(
-                    'unread_msg_board',
-                    {
+                    'unread_msg_board', {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
 
             
             # send edit message to client
             if self.type == 'supporter' and text_data_json.get('_type_request') == 'edit':
+
                 chat = ChatModel.objects.get(
                     id=text_data_json.get('reply_id'),
                     sender='supporter'
                 )
                 chat.old_msg = chat.msg
                 chat.msg = text_data_json.get('text')
                 chat.is_edited = True
                 chat.save()
 
                 user_group_name = f"chat_client_{text_data_json['client_id']}" 
                 async_to_sync(self.channel_layer.group_send)(
-                    user_group_name,
-                    {
+                    user_group_name, {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
 
             
             # send edit message to supporter
             if self.type == 'client' and text_data_json.get('_type_request') == 'edit':
+
                 chat = ChatModel.objects.get(
                     id=text_data_json.get('reply_id'),
                     sender='client'
                 )
                 chat.old_msg = chat.msg
                 chat.msg = text_data_json.get('text')
                 chat.is_edited = True
                 chat.save()
 
                 async_to_sync(self.channel_layer.group_send)(
-                    'unread_msg_board',
-                    {
+                    'unread_msg_board', {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
 
             
             # send status to client
             if self.type == 'supporter' and text_data_json.get('_type_request') == 'status':
+
                 user_group_name = f"chat_client_{text_data_json['client_id']}" 
                 async_to_sync(self.channel_layer.group_send)(
-                    user_group_name,
-                    {
+                    user_group_name, {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
 
             
             # send status to supporter (unread msgs board)
             elif self.type == 'client' and text_data_json.get('_type_request') == 'status': 
+
                 async_to_sync(self.channel_layer.group_send)(
-                    'unread_msg_board',
-                    {
+                    'unread_msg_board', {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
 
             
             # seen message of client in supporter panel
@@ -178,39 +185,42 @@
                     client = UserChatModel.objects.get(user_chat_uid=text_data_json.get('client_id'))
 
                     ChatModel.objects.filter(
                         sender='client',
                         client=client,
                         supporter=self.user,
                         is_seen=False
-                    ).update(is_seen=True)
+                    ).update(
+                        is_seen=True
+                    )
 
                     user_group_name = f"chat_client_{client.user_chat_uid}" 
                     async_to_sync(self.channel_layer.group_send)(
-                        user_group_name,
-                        {
+                        user_group_name, {
                             'type': 'send_msg',
                             'message': text_data
                         }
                     )
 
                 
             # seen message of supporter in client
             elif self.type == 'client' and text_data_json.get('_type_request') == 'seen':
+
                 if text_data_json.get('message_sender') == 'supporter':
 
                     ChatModel.objects.filter(
                         sender='supporter',
                         client=self.user,
                         is_seen=False
-                    ).update(is_seen=True)
+                    ).update(
+                        is_seen=True
+                    )
 
                     async_to_sync(self.channel_layer.group_send)(
-                        'unread_msg_board',
-                        {
+                        'unread_msg_board', {
                             'type': 'send_msg',
                             'message': text_data
                         }
                     )
 
 
             # send msg from supporter to client
@@ -232,43 +242,47 @@
                     chat_obj.reply = ChatModel.objects.get(id=text_data_json['reply_id'])
 
                 if not user_client.have_supporter:
                     user_client.have_supporter = self.user
                     user_client.save()
 
                 if ChatModel.objects.filter(client=user_client, supporter=None).exists():
-                    ChatModel.objects.filter(client=user_client, supporter=None).update(supporter=self.user)
+                    ChatModel.objects.filter(
+                        client=user_client, 
+                        supporter=None
+                    ).update(
+                        supporter=self.user
+                    )
 
                 chat_obj.save()
 
-                # update id-created-isseen-reply-ownername of message
-                text_data_json['owner_name'] = f'{self.user.user.first_name} {self.user.user.last_name}' if self.user.user.first_name else 'supporter'
+                owner_name_str = f'{self.user.user.first_name} {self.user.user.last_name}' if self.user.user.first_name else 'supporter'
+                text_data_json['owner_name'] = owner_name_str
                 text_data_json['id'] = chat_obj.id
-                text_data_json['created'] = f'{timezone.localtime(chat_obj.created).hour}:{timezone.localtime(chat_obj.created).minute}'
+                text_data_json['created'] = get_hour_min(chat_obj.created)
                 text_data_json['is_seen'] = chat_obj.is_seen
                 if chat_obj.reply:
                     text_data_json['reply_title'] = chat_obj.reply.sender
                     text_data_json['reply_msg'] = chat_obj.reply.msg
                     text_data_json['reply_id'] = chat_obj.reply.id
                 text_data = json.dumps(text_data_json)
 
                 # send msg to client
                 user_group_name_1 = f'chat_client_{chat_obj.client.user_chat_uid}' 
                 async_to_sync(self.channel_layer.group_send)(
-                    user_group_name_1,
-                    {
+                    user_group_name_1, {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
+
                 # Echo msg supporter
                 user_group_name_2 = 'unread_msg_board'
                 async_to_sync(self.channel_layer.group_send)(
-                    user_group_name_2,
-                    {
+                    user_group_name_2, {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
 
             
             # send msg from client to supporter
@@ -279,51 +293,78 @@
                     sender=text_data_json['sender_type'],
                     msg=text_data_json['text']
                 )
 
                 if self.user.have_supporter:
                     chat_obj.supporter = self.user.have_supporter
 
+                if len(text_data_json.get('supporter_uid')) > 1 and not chat_obj.supporter:
+                    try:
+                        supporter_found = SupporterModel.objects.get(supporter_uid=text_data_json.get('supporter_uid'))
+                        chat_obj.supporter = supporter_found
+                    except:
+                        pass
+
                 if text_data_json['reply_id']:
-                    chat_obj.reply = ChatModel.objects.get(id=text_data_json['reply_id'])
+                    chat_obj.reply = ChatModel.objects.get(
+                        id=text_data_json['reply_id']
+                    )
                 
                 chat_obj.save()
 
-                # update id-created-isseen-reply-ownername of message
                 text_data_json['owner_name'] = f'{self.user.first_name} {self.user.last_name}'
                 text_data_json['id'] = chat_obj.id
-                text_data_json['created'] = f'{timezone.localtime(chat_obj.created).hour}:{timezone.localtime(chat_obj.created).minute}'
+                text_data_json['created'] = get_hour_min(chat_obj.created)
                 text_data_json['is_seen'] = chat_obj.is_seen
                 if chat_obj.reply:
                     text_data_json['reply_title'] = chat_obj.reply.sender
                     text_data_json['reply_msg'] = chat_obj.reply.msg
                     text_data_json['reply_id'] = chat_obj.reply.id
-                if self.user.have_supporter:
+                if len(text_data_json.get('supporter_uid')) > 1 or self.user.have_supporter:
                     text_data_json['client_have_supporter'] = 'yes'
-                elif not self.user.have_supporter:
+                else:
                     text_data_json['client_have_supporter'] = 'no'
                 text_data = json.dumps(text_data_json)
 
                 # send msg to unread msgs board
                 user_group_name_1 = "unread_msg_board"    
                 async_to_sync(self.channel_layer.group_send)(
-                    user_group_name_1,
-                    {
+                    user_group_name_1, {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
                 # Echo msg client
                 user_group_name_2 = f"chat_client_{self.user_id}"    
                 async_to_sync(self.channel_layer.group_send)(
-                    user_group_name_2,
-                    {
+                    user_group_name_2, {
+                        'type': 'send_msg',
+                        'message': text_data
+                    }
+                )
+
+            # send supporterID to client
+            elif self.type == 'supporter' and text_data_json.get('_type_request') == 'set_supporter_for_client':
+
+                try:
+                    supporter_found = SupporterModel.objects.get(supporter_uid=text_data_json.get('supporter_id'))
+                    client_found = UserChatModel.objects.get(user_chat_uid=text_data_json.get('client_id'))
+                    client_found.have_supporter = supporter_found
+                    client_found.save()
+                except:
+                    pass
+
+                # Echo msg client
+                user_group_name = f"chat_client_{text_data_json.get('client_id')}"    
+                async_to_sync(self.channel_layer.group_send)(
+                    user_group_name, {
                         'type': 'send_msg',
                         'message': text_data
                     }
                 )
 
     
+
     def send_msg(self, event):
         message = event['message']
         self.send(text_data=message)
```

### Comparing `django-chatapp-1.3/chatapp/migrations/0001_initial.py` & `django-chatapp-1.4/chatapp/migrations/0001_initial.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# Generated by Django 4.1.2 on 2023-03-05 08:43
+# Generated by Django 4.1.7 on 2023-03-23 09:21
 
 import chatapp.utils
 from django.conf import settings
 from django.db import migrations, models
 import django.db.models.deletion
```

### Comparing `django-chatapp-1.3/chatapp/models.py` & `django-chatapp-1.4/chatapp/models.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,12 +1,11 @@
-from random import choices
 from django.db import models
 from django.contrib.auth.models import User
 from django.utils.translation import gettext_lazy as _
-from .utils import jalali_convertor, unique_username
+from .utils import unique_username
 
 
 class SupporterModel(models.Model):
     """ for creating a list of supporter for your website """
 
     supporter_uid = models.CharField(default=unique_username, max_length=255, editable=False, unique=True, verbose_name=_('آیدی پشتیبان'))
     user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('کاربر'))
@@ -16,23 +15,23 @@
     
     class Meta:
         ordering = ['-id']
         verbose_name = _('پشتیبان')
         verbose_name_plural = _('پشتیبان ها')
     
     def __str__(self):
-        return str(self.supporter_uid)
-
-    def j_created(self):
-        return jalali_convertor(time=self.created, number=True)
-    j_created.short_description = _('تاریخ ثبت رکورد')
+        try:
+            return f'{self.full_name} ({str(self.supporter_uid)})'
+        except:
+            return f'{str(self.supporter_uid)}'
 
 
 class ChatModel(models.Model):
     """ this is a message data between client and supporter """
+    
     CLIENT_SUPPORTER = (('supporter', _('پشتیبان')), ('client', _('کاربر')))
 
     reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('پاسخ'))
     client = models.ForeignKey('UserChatModel', on_delete=models.CASCADE, verbose_name=_('کاربر'))
     supporter = models.ForeignKey(SupporterModel, blank=True, null=True, on_delete=models.CASCADE, verbose_name=_('پشتیبان'))
     sender = models.CharField(max_length=255, choices=CLIENT_SUPPORTER, verbose_name=_('ارسال کننده'))
     msg = models.TextField(verbose_name=_('متن پیام'))
@@ -46,18 +45,14 @@
         ordering = ['-id']
         verbose_name = _('چت کاربر و پشتیبان')
         verbose_name_plural = _('چت های کاربر و پشتیبان')
     
     def __str__(self):
         return str(self.id)
 
-    def j_created(self):
-        return jalali_convertor(time=self.created, number=True)
-    j_created.short_description = _('تاریخ ثبت رکورد')
-
 
 class UserChatModel(models.Model):
     """ create a flag for user for chat to supporter """
 
     user_chat_uid = models.CharField(default=unique_username, max_length=255, editable=False, unique=True, verbose_name=_('آیدی چت کاربر'))
     have_supporter = models.ForeignKey(SupporterModel, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('آیا پشتیبان دارد؟'))
     first_name = models.CharField(max_length=255, verbose_name=_('نام'))
@@ -72,18 +67,14 @@
         ordering = ['-id']
         verbose_name = _('اطلاعات کاربر')
         verbose_name_plural = _('اطلاعات کاربران')
     
     def __str__(self):
         return str(self.user_chat_uid)
 
-    def j_created(self):
-        return jalali_convertor(time=self.created, number=True)
-    j_created.short_description = _('تاریخ ثبت رکورد')
-
 
 class ReadyChatModel(models.Model):
     """ list of ready chat component for all of supporters """
 
     subject = models.CharField(max_length=255, verbose_name=_('عنوان'))
     content = models.TextField(verbose_name=_('محتوا'))
     supporter = models.ForeignKey(SupporterModel, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('پشتیبان'))
@@ -111,11 +102,8 @@
     class Meta:
         ordering = ['-id']
         verbose_name = _('گزارش کاربر')
         verbose_name_plural = _('گزارش کاربران')
     
     def __str__(self):
         return self.user.user_chat_uid
-
-    def j_created(self):
-        return jalali_convertor(time=self.created, number=True)
-    j_created.short_description = _('تاریخ ثبت رکورد')
+
```

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/css/custom.css` & `django-chatapp-1.4/chatapp/static/django_chatapp/css/client.css`

 * *Files 1% similar despite different names*

```diff
@@ -1 +1 @@
-@font-face{font-family:"vazir";src:url("../font/vazir-medium.ttf"),url("../font/vazir-medium.woff")}.font-vazir{font-family:vazir !important}.msg__body::-webkit-scrollbar{background-color:rgba(0,0,0,0);width:5px}.msg__body::-webkit-scrollbar-thumb{border-radius:5px;background-color:#d1d1d1}.d-none{display:none !important}.chatapp__show{opacity:1 !important}.chatapp__hide{opacity:0 !important}section.chatapp{box-sizing:border-box;z-index:9999 !important;font-family:vazir !important;scroll-behavior:smooth !important;direction:rtl !important}section.chatapp .chatapp__btn{position:fixed;right:14px;bottom:14px;cursor:pointer;padding:7px 10px;border-radius:10px;background-color:#2391eb}section.chatapp .chatapp__btn+div{position:relative}section.chatapp .chatapp__btn img{height:40px;width:40px}section.chatapp .chatapp__btn div#alert_msg_ctx{position:absolute;top:13px;left:14px;height:19px;width:22px;border-radius:2px;background-color:#fff;animation:blink 2s alternate infinite;-webkit-animation:blink 2s alternate infinite}section.chatapp .chatapp__msg{position:fixed !important;right:14px;border-radius:10px;bottom:87px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);transition:all .5s ease}section.chatapp .chatapp__msg .msg__header{background-color:#2391eb;border-radius:10px 10px 0 0}section.chatapp .chatapp__msg .msg__header .msg__wrapper{border-radius:10px 10px 0 0;padding:10px;background:linear-gradient(258deg, rgba(0, 0, 0, 0.3) 0%, rgba(84, 141, 177, 0) 100%) rgba(0,0,0,0);display:flex;justify-content:space-between;width:375px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info{display:flex}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info img{height:45px;width:45px;border-radius:50%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div{display:flex;flex-direction:column;color:#fff;margin:0 10px;position:relative}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(1){font-size:20px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(2){font-size:9pt;position:absolute;right:0;bottom:0px;display:flex}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options button{background-color:rgba(0,0,0,0);border:none;color:#fff;outline:none;cursor:pointer;font-size:20px;margin-top:8px;transition:all .3s}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options button.bottom__msgbox img{height:22px !important;width:22px !important;margin-bottom:2px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options button.close__msgbox img{height:26px !important;width:26px !important}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options .loader_spinner{height:11px;width:11px;border-radius:50%;border:3px solid #fff;-webkit-animation:spinner 1s linear infinite;animation:spinner 1s linear infinite;transition:all .3s;pointer-events:none;margin-top:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options .loader_spinner--white{border-top:3px solid #2391eb}section.chatapp .chatapp__msg .msgdel__right{float:right !important}section.chatapp .chatapp__msg .msgdel__left{float:left !important}section.chatapp .chatapp__msg .msg__body{background-color:#fff;padding:10px 15px;overflow-y:auto;-webkit-overflow-scrolling:touch;height:320px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .deleted_msg{background-color:#d1d1d1 !important;color:#fff !important;padding:3px 4px;font-size:13px;border-radius:5px;margin-bottom:5px;width:175px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .deleted_msg img{height:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper{width:100%;height:auto;position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar{position:absolute;top:-13px;padding:5px;background-color:#000;z-index:5;list-style:none;color:#d1d1d1;width:100px;font-size:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li{cursor:pointer;padding:3px 5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li img{height:13px;margin-bottom:-4px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li:hover{color:#fff}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar--right{right:0 !important;left:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar--left{left:0 !important;right:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper:hover .reply_one_msg{opacity:1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg{padding:7px 10px;margin-bottom:5px;max-width:240px;min-width:100px;text-align:right;color:#fff;position:relative;transition:background-color .3s linear;z-index:2}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p{margin:0px !important;word-break:break-word}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied{padding:3px 5px;border-right:2px solid #fff;margin-bottom:7px !important;border-radius:4px 0 0 4px;display:flex;flex-direction:column;cursor:pointer}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied span{font-size:9pt}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied--right{background-color:#39a2f9}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied--left{background-color:#c5c5c5}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info{margin-top:5px;margin-bottom:-5px;display:flex;flex-direction:row;justify-content:flex-start}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__clock{font-size:9pt}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__edited{font-size:9pt;padding:0 7px;margin-top:-3px !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__status img{height:14px;width:16px;margin-left:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left{float:left;border-radius:12px;background-color:#d1d1d1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left::after{content:"";position:absolute;bottom:9px;left:-8px;width:0;height:0;border-top:8px solid rgba(0,0,0,0);border-bottom:0px solid rgba(0,0,0,0);border-right:8px solid #d1d1d1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left div.msg__info__clock{padding-bottom:4px !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__right{float:right;border-radius:12px;background-color:#2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__right::after{content:"";position:absolute;bottom:9px;right:-8px;width:0;height:0;border-top:8px solid rgba(0,0,0,0);border-bottom:0px solid rgba(0,0,0,0);border-left:8px solid #2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg{color:#d1d1d1;font-size:10pt;opacity:0;line-height:11px;z-index:1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg--right{transform:translate(-5px, 7px)}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg--left{text-align:left;transform:translate(5px, 7px)}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg span{cursor:pointer;transition:all .2s;margin:0 !important;padding:4px 0}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg span:hover{color:#9e9e9e}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .clearfix{clear:both}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #restart__game{border:none;outline:none;font-family:vazir;padding:5px 15px;border-radius:5px;cursor:pointer;background-color:#ececec;margin-bottom:15px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #restart__game:active{transform:translateY(-1px)}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #score__game{display:flex;justify-content:center;margin-bottom:20px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #score__game div{margin:0 15px;display:flex}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #score__game div span:nth-child(1){color:#d1d1d1;padding-left:3px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper{width:208px;margin:auto;position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper #bg__glass{background-color:rgba(0,0,0,0);position:absolute;inset:0;cursor:not-allowed !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn{display:flex;background-color:#2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .btn_game{padding:0px;height:65px;width:68px;border:none;outline:none;background-color:#fff;display:flex;justify-content:center;align-items:center}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .btn_game img{height:50%;height:50%}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .m2px_l{margin-left:2px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .m2px_b{margin-bottom:2px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .disable_btn{cursor:not-allowed !important;pointer-events:none}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #game_alert_msg{color:#fff;padding:8px 7px;border-radius:7px;max-width:1100px;margin:20px auto;background-color:#2391eb;font-size:11pt;text-align:center}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .game_alert_msg_win{background-color:#d1d1d1 !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .game_alert_msg_lose{background-color:#2391eb !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form{width:250px;margin:20px auto;border-radius:8px;box-shadow:0 0 13px 3px rgba(0,0,0,.1)}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form .chatform__header{border-radius:8px 8px 0px 0px;background-color:#2391eb;padding:8px;color:#fff;font-size:9pt;text-align:start;margin-bottom:10px}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form{padding:1rem}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol{position:relative;margin-bottom:23px}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol input{font-family:vazir;width:92%;padding:7px;font-size:13pt;color:#2391eb;border:1px solid #d1d1d1;border-radius:5px;outline:none;background:#fff !important;transition:all .3s linear}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol input:focus{border-color:#858585}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol input:focus~label{color:#858585}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol label{position:absolute;pointer-events:none;top:-15px;right:10px;color:#d1d1d1;font-size:13px;padding:0 7px;background-color:#fff;transition:all .3s linear}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form .mbnone__chatapp{margin-bottom:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form .chatapp_button{width:100%;display:flex;justify-content:end;margin-top:13px}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form .chatapp_button button{font-family:vazir;border:none;outline:none;padding:5px 25px;cursor:pointer;border-radius:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .btn_last_msg{position:absolute;left:20px;bottom:60px;z-index:9999}section.chatapp .chatapp__msg .msg__body .body__wrapper .btn_last_msg button{cursor:pointer;outline:none;border:none;border-radius:50%;background-color:rgba(0,0,0,.3);position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .btn_last_msg button img{height:35px;width:35px;padding:5px 3px;padding-top:8px}section.chatapp .chatapp__msg .msg__body .body__wrapper .btn_last_msg button div.unreadmsg_counter{position:absolute;right:-2px;top:-2px;padding:3px 7px;background-color:#2391eb;border-radius:50%;font-size:10pt;color:#fff}section.chatapp .chatapp__msg .body__inputs{padding:8px 10px;padding-top:4px !important}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper{background-color:#ececec;border-radius:25px;display:flex;position:relative}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper input{flex:auto;font-family:vazir !important;outline:none;border:none;background-color:#ececec;padding:10px 15px;border-radius:25px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper{position:absolute;bottom:44px;border-radius:7px;right:0px;background-color:#ececec;padding:5px 10px;z-index:9999;width:70%;display:flex;justify-content:space-between}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper div{order:1;display:flex;flex-direction:column}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper div p{margin:0;color:#5e5e5e;font-size:9pt;padding:0 5px;border-right:2px solid #fff;height:20px;overflow:hidden}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper button.close_replybar{order:2;background-color:rgba(0,0,0,0) !important;color:#5e5e5e;border:none;outline:none;font-size:20px;cursor:pointer;padding:0 10px 10px 0;height:100%}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper button.close_replybar:hover{color:#000}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper{position:absolute;bottom:44px;border-radius:7px;right:0px;background-color:#ececec;padding:5px 10px;z-index:9999;width:70%;height:100px;overflow-y:scroll;display:flex;justify-content:space-between}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper div.emoji_box{order:1;display:flex;flex-direction:row;flex-wrap:wrap}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper div.emoji_box div.emoji_item{flex:1;cursor:pointer;padding:3px;max-width:25px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_game{outline:none;background-color:rgba(0,0,0,0);border:none;margin-right:3px;padding:6px 10px;cursor:pointer}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_game img{height:26px;width:28px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_emoji{outline:none;background-color:rgba(0,0,0,0);border:none;margin-right:3px;padding:6px 2px;cursor:pointer}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_emoji img{height:26px;width:28px;margin-bottom:-4px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button[type=submit]{outline:none;background-color:#2391eb;border:none;margin-right:3px;border-radius:25px;padding:6px 20px;cursor:pointer}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button[type=submit] img{height:20px;width:21px}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn{text-align:center;padding:4px;cursor:pointer;transition:all .3s}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn:hover{color:#2391eb}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn .new_msg_shower{background-color:#2391eb;color:#fff;width:56px;font-size:12px;border-radius:5px;padding:4px;display:flex;align-items:center;justify-content:center;float:left;margin-bottom:10px}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn .new_msg_shower img{height:20px;margin-bottom:-5px}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn .new_msg_shower div{flex:1}section.chatapp__ltr{direction:ltr !important}section.chatapp__ltr .chatapp__btn{left:14px;right:unset !important}section.chatapp__ltr .chatapp__msg{left:14px;right:unset !important;border-radius:10px;bottom:87px;box-shadow:0 0 13px 3px rgba(0,0,0,.1)}section.chatapp__ltr .msg__info__status img{margin-right:5px;margin-left:unset !important}section.chatapp__ltr .msg__header .msg__wrapper .header__info div span:nth-child(2){right:unset !important;left:0}section.chatapp__ltr .chatapp__msg .body__inputs form div button{margin-right:unset !important;margin-left:3px}section.chatapp__ltr .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol label{right:unset !important;left:10px}section.chatapp__ltr .m2px_l{margin-left:unset !important;margin-right:2px}section.chatapp__ltr .msg__body .body__wrapper .msg{text-align:left !important}section.chatapp__ltr .msg__body .body__wrapper .msg p.msg__replied{border-right:unset !important;border-left:2px solid #fff;border-radius:0 4px 4px 0 !important}section.chatapp__ltr .chatapp__msg .msg__header .msg__wrapper{background:linear-gradient(258deg, rgba(84, 141, 177, 0) 0%, rgba(0, 0, 0, 0.3) 100%) rgba(0,0,0,0) !important}section.chatapp__ltr .body__inputs .btn_last_msg{left:unset !important;right:15px}section.chatapp__ltr .body__inputs form div.forminput_wrapper .reply_msg_wrapper{left:0px;right:unset !important}section.chatapp__ltr .body__inputs form div.forminput_wrapper .reply_msg_wrapper div p{border-left:2px solid #fff !important;border-right:unset !important}section.chatapp__ltr .body__inputs form div.forminput_wrapper .emoji_wrapper{left:0px;right:unset !important}section.chatapp__ltr .reply_one_msg--right{float:right !important}@-webkit-keyframes blink{from{opacity:0}to{opacity:1}}@keyframes blink{from{opacity:0}to{opacity:1}}@-webkit-keyframes spinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}@keyframes spinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}@media screen and (min-width: 1001px){.chatapp__msg .msg__header .msg__wrapper{width:375px !important}}@media screen and (max-width: 1000px){.chatapp__msg .msg__header .msg__wrapper{width:280px !important}.chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(1){font-size:12pt !important}.chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(2){font-size:9pt !important}}
+@font-face{font-family:"vazir";src:url("../font/vazir-medium.ttf"),url("../font/vazir-medium.woff")}.font-vazir{font-family:vazir !important}.msg__body::-webkit-scrollbar{background-color:rgba(0,0,0,0);width:5px}.msg__body::-webkit-scrollbar-thumb{border-radius:5px;background-color:#d1d1d1}.d-none{display:none !important}.chatapp__show{opacity:1 !important}.chatapp__hide{opacity:0 !important}section.chatapp{box-sizing:border-box;z-index:9999 !important;font-family:vazir !important;scroll-behavior:smooth !important;direction:rtl !important}section.chatapp .chatapp__btn{position:fixed;right:14px;bottom:14px;cursor:pointer;padding:7px 10px;border-radius:10px;background-color:#2391eb}section.chatapp .chatapp__btn+div{position:relative}section.chatapp .chatapp__btn img{height:40px;width:40px}section.chatapp .chatapp__btn div#alert_msg_ctx{position:absolute;top:13px;left:14px;height:19px;width:22px;border-radius:2px;background-color:#fff;animation:blink 2s alternate infinite;-webkit-animation:blink 2s alternate infinite}section.chatapp .chatapp__msg{position:fixed !important;right:14px;border-radius:10px;bottom:87px;box-shadow:0 5px 13px 3px rgba(0,0,0,.1);transition:all .5s ease;background-color:#fff}section.chatapp .chatapp__msg::after{content:"";height:0;width:0;position:absolute;bottom:-9px;right:22px;border-left:10px solid rgba(0,0,0,0);border-right:10px solid rgba(0,0,0,0);border-top:10px solid #fff}section.chatapp .chatapp__msg .msg__header{background-color:#2391eb;border-radius:10px 10px 0 0}section.chatapp .chatapp__msg .msg__header .msg__wrapper{border-radius:10px 10px 0 0;padding:10px;background:linear-gradient(258deg, rgba(0, 0, 0, 0.3) 0%, rgba(84, 141, 177, 0) 100%) rgba(0,0,0,0);display:flex;justify-content:space-between;width:375px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info{display:flex}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info img{height:45px;width:45px;border-radius:50%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div{display:flex;flex-direction:column;color:#fff;margin:0 10px;position:relative;min-width:140px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(1){font-size:20px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(2){font-size:9pt;position:absolute;right:0;bottom:0px;display:flex}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options button{background-color:rgba(0,0,0,0);border:none;color:#fff;outline:none;cursor:pointer;font-size:20px;margin-top:8px;transition:all .3s}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options button.bottom__msgbox img{height:22px !important;width:22px !important;margin-bottom:2px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options button.close__msgbox img{height:26px !important;width:26px !important}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options .loader_spinner{height:11px;width:11px;border-radius:50%;border:3px solid #fff;animation:spinner 1s linear infinite;transition:all .3s;pointer-events:none;margin-top:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__options .loader_spinner--white{border-top:3px solid #2391eb}section.chatapp .chatapp__msg .msgdel__right{float:right !important}section.chatapp .chatapp__msg .msgdel__left{float:left !important}section.chatapp .chatapp__msg .msg__body{background-color:#fff;padding:10px 15px;overflow-y:auto;-webkit-overflow-scrolling:touch;height:320px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .deleted_msg{background-color:#d1d1d1 !important;color:#fff !important;padding:3px 4px;font-size:13px;border-radius:5px;margin-bottom:5px;width:175px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .deleted_msg img{height:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper{width:100%;height:auto;position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar{position:absolute;top:-13px;padding:5px;background-color:#000;z-index:5;list-style:none;color:#d1d1d1;width:100px;font-size:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li{cursor:pointer;padding:3px 5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li img{height:13px;margin-bottom:-4px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li:hover{color:#fff}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar--right{right:0 !important;left:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar--left{left:0 !important;right:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper:hover .reply_one_msg{opacity:1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg{padding:7px 10px;margin-bottom:5px;max-width:240px;min-width:100px;text-align:right;color:#fff;position:relative;transition:background-color .3s linear;z-index:2}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p{margin:0px !important;word-break:break-word}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied{padding:3px 5px;border-right:2px solid #fff;margin-bottom:7px !important;border-radius:4px 0 0 4px;display:flex;flex-direction:column;cursor:pointer}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied span{font-size:9pt}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied--right{background-color:#39a2f9}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied--left{background-color:#c5c5c5}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info{margin-top:5px;margin-bottom:-5px;display:flex;flex-direction:row;justify-content:flex-start}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__clock{font-size:9pt}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__edited{font-size:9pt;padding:0 7px;margin-top:-3px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__status img{height:14px;width:16px;margin-left:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left{float:left;border-radius:12px;background-color:#d1d1d1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left::after{content:"";position:absolute;bottom:9px;left:-8px;width:0;height:0;border-top:8px solid rgba(0,0,0,0);border-bottom:0px solid rgba(0,0,0,0);border-right:8px solid #d1d1d1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left div.msg__info__clock{padding-bottom:4px !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__right{float:right;border-radius:12px;background-color:#2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__right::after{content:"";position:absolute;bottom:9px;right:-8px;width:0;height:0;border-top:8px solid rgba(0,0,0,0);border-bottom:0px solid rgba(0,0,0,0);border-left:8px solid #2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg{color:#d1d1d1;font-size:10pt;opacity:0;line-height:11px;z-index:1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg--right{transform:translate(-5px, 7px)}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg--left{text-align:left;transform:translate(5px, 7px)}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg span{cursor:pointer;transition:all .2s;margin:0 !important;padding:4px 0}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg span:hover{color:#9e9e9e}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .clearfix{clear:both}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #restart__game{border:none;outline:none;font-family:vazir;padding:5px 15px;border-radius:5px;cursor:pointer;background-color:#ececec;margin-bottom:15px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #restart__game:active{transform:translateY(-1px)}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #score__game{display:flex;justify-content:center;margin-bottom:20px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #score__game div{margin:0 15px;display:flex}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #score__game div span:nth-child(1){color:#d1d1d1;padding-left:3px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper{width:208px;margin:auto;position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper #bg__glass{background-color:rgba(0,0,0,0);position:absolute;inset:0;cursor:not-allowed !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn{display:flex;background-color:#2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .btn_game{padding:0px;height:65px;width:68px;border:none;outline:none;background-color:#fff;display:flex;justify-content:center;align-items:center}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .btn_game img{height:50%;height:50%}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .m2px_l{margin-left:2px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .m2px_b{margin-bottom:2px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .btns__wrapper__btn .disable_btn{cursor:not-allowed !important;pointer-events:none}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game #game_alert_msg{color:#fff;padding:8px 7px;border-radius:7px;max-width:1100px;margin:20px auto;background-color:#2391eb;font-size:11pt;text-align:center}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .game_alert_msg_win{background-color:#d1d1d1 !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .tictoctoe__game .game_alert_msg_lose{background-color:#2391eb !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form{width:250px;margin:20px auto;border-radius:8px;box-shadow:0 0 13px 3px rgba(0,0,0,.1)}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form .chatform__header{border-radius:8px 8px 0px 0px;background-color:#2391eb;padding:8px;color:#fff;font-size:9pt;text-align:start;margin-bottom:10px}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form{padding:1rem}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol{position:relative;margin-bottom:23px}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol input{font-family:vazir;width:92%;padding:7px;font-size:13pt;color:#2391eb;border:1px solid #d1d1d1;border-radius:5px;outline:none;background:#fff !important;transition:all .3s linear}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol input:focus{border-color:#858585}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol input:focus~label{color:#858585}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol label{position:absolute;pointer-events:none;top:-15px;right:10px;color:#d1d1d1;font-size:13px;padding:0 7px;background-color:#fff;transition:all .3s linear}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol p.form_error{color:red;font-size:12px;margin:0px;margin-top:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form .mbnone__chatapp{margin-bottom:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form .chatapp_button{width:100%;display:flex;justify-content:end;margin-top:13px}section.chatapp .chatapp__msg .msg__body .body__wrapper .chatapp__form form .chatapp_button button{font-family:vazir;border:none;outline:none;padding:5px 25px;cursor:pointer;border-radius:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .btn_last_msg{position:absolute;left:20px;bottom:60px;z-index:9999}section.chatapp .chatapp__msg .msg__body .body__wrapper .btn_last_msg button{cursor:pointer;outline:none;border:none;border-radius:50%;background-color:rgba(0,0,0,.3);position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .btn_last_msg button img{height:35px;width:35px;padding:5px 3px;padding-top:8px}section.chatapp .chatapp__msg .msg__body .body__wrapper .btn_last_msg button div.unreadmsg_counter{position:absolute;right:-2px;top:-2px;padding:3px 7px;background-color:#2391eb;border-radius:50%;font-size:10pt;color:#fff}section.chatapp .chatapp__msg .body__inputs{padding:0px 10px;padding-top:4px !important;background-color:#fff;border-radius:0 0 10px 10px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper{background-color:#ececec;border-radius:25px;display:flex;position:relative}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper input{flex:auto;font-family:vazir !important;outline:none;border:none;background-color:#ececec;padding:10px 15px;border-radius:25px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper{position:absolute;bottom:44px;border-radius:7px;right:0px;background-color:#ececec;padding:5px 10px;z-index:9999;width:70%;display:flex;justify-content:space-between}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper div{order:1;display:flex;flex-direction:column}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper div p{margin:0;color:#5e5e5e;font-size:9pt;padding:0 5px;border-right:2px solid #fff;height:20px;overflow:hidden}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper button.close_replybar{order:2;background-color:rgba(0,0,0,0) !important;color:#5e5e5e;border:none;outline:none;font-size:20px;cursor:pointer;padding:0 10px 10px 0;height:100%}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper button.close_replybar:hover{color:#000}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper{position:absolute;bottom:44px;border-radius:7px;right:0px;background-color:#ececec;padding:5px 10px;z-index:9999;width:70%;height:100px;overflow-y:scroll;display:flex;justify-content:space-between}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper div.emoji_box{order:1;display:flex;flex-direction:row;flex-wrap:wrap}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper div.emoji_box div.emoji_item{flex:1;cursor:pointer;font-size:18px;padding:4px;max-width:25px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_game{outline:none;background-color:rgba(0,0,0,0);border:none;margin-right:3px;padding:6px 10px;cursor:pointer}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_game img{height:26px;width:28px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_emoji{outline:none;background-color:rgba(0,0,0,0);border:none;margin-right:3px;padding:6px 2px;cursor:pointer}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_emoji img{height:26px;width:28px;margin-bottom:-4px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button[type=submit]{outline:none;background-color:#2391eb;border:none;margin-right:3px;border-radius:25px;padding:6px 20px;cursor:pointer}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button[type=submit] img{height:20px;width:21px}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn{text-align:center;padding:4px;cursor:pointer;transition:all .3s}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn:hover{color:#2391eb}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn .new_msg_shower{background-color:#2391eb;color:#fff;width:56px;font-size:12px;border-radius:5px;padding:4px;display:flex;align-items:center;justify-content:center;float:left;margin-bottom:10px}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn .new_msg_shower img{height:20px;margin-bottom:-5px}section.chatapp .chatapp__msg .body__inputs .goback_chat_btn .new_msg_shower div{flex:1}section.chatapp__ltr{direction:ltr !important}section.chatapp__ltr .chatapp__btn{left:14px;right:unset !important}section.chatapp__ltr .chatapp__msg{left:14px;right:unset !important;border-radius:10px;bottom:87px;box-shadow:0 0 13px 3px rgba(0,0,0,.1)}section.chatapp__ltr .chatapp__msg::after{right:unset !important;left:22px}section.chatapp__ltr .msg__info__status img{margin-right:5px;margin-left:unset !important}section.chatapp__ltr .msg__header .msg__wrapper .header__info div span:nth-child(2){right:unset !important;left:0}section.chatapp__ltr .chatapp__msg .body__inputs form div button{margin-right:unset !important;margin-left:3px}section.chatapp__ltr .chatapp__msg .msg__body .body__wrapper .chatapp__form form div.chatapp_formcontrol label{right:unset !important;left:10px}section.chatapp__ltr .m2px_l{margin-left:unset !important;margin-right:2px}section.chatapp__ltr .msg__body .body__wrapper .msg{text-align:left !important}section.chatapp__ltr .msg__body .body__wrapper .msg p.msg__replied{border-right:unset !important;border-left:2px solid #fff;border-radius:0 4px 4px 0 !important}section.chatapp__ltr .chatapp__msg .msg__header .msg__wrapper{background:linear-gradient(258deg, rgba(84, 141, 177, 0) 0%, rgba(0, 0, 0, 0.3) 100%) rgba(0,0,0,0) !important}section.chatapp__ltr .body__inputs .btn_last_msg{left:unset !important;right:15px}section.chatapp__ltr .body__inputs form div.forminput_wrapper .reply_msg_wrapper{left:0px;right:unset !important}section.chatapp__ltr .body__inputs form div.forminput_wrapper .reply_msg_wrapper div p{border-left:2px solid #fff !important;border-right:unset !important}section.chatapp__ltr .body__inputs form div.forminput_wrapper .emoji_wrapper{left:0px;right:unset !important}section.chatapp__ltr .reply_one_msg--right{float:right !important}section.chatapp__ltr .body__wrapper .msg div.msg__info__edited{margin-top:unset !important}@keyframes blink{from{opacity:0}to{opacity:1}}@keyframes spinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}@media screen and (min-width: 1001px){.chatapp__msg .msg__header .msg__wrapper{width:375px !important}}@media screen and (max-width: 1000px){.chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(1){font-size:12pt !important}.chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(2){font-size:9pt !important}}
```

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/css/custom.scss` & `django-chatapp-1.4/chatapp/static/django_chatapp/css/client.scss`

 * *Files 1% similar despite different names*

```diff
@@ -63,16 +63,29 @@
     }
 
     .chatapp__msg {
         position: fixed !important;
         right: 14px;
         border-radius: 10px;
         bottom: 87px;
-        box-shadow: $boxshadow;
+        box-shadow: 0 5px 13px 3px rgba(0, 0, 0, 0.1);
         transition: all 0.5s ease;
+        background-color: white;
+
+        &::after {
+            content: '';
+            height: 0;
+            width: 0;
+            position: absolute;
+            bottom: -9px;
+            right: 22px;
+            border-left: 10px solid rgba(0,0,0,0);
+            border-right: 10px solid rgba(0,0,0,0);
+            border-top: 10px solid white;
+        }
 
         .msg__header {
             background-color: $primary;
             border-radius: 10px 10px 0 0;
 
             .msg__wrapper {
                 border-radius: 10px 10px 0 0;
@@ -92,14 +105,15 @@
                     }
                     div {
                         display: flex;
                         flex-direction: column;
                         color: $white;
                         margin: 0 10px;
                         position: relative;
+                        min-width: 140px;
     
                         span:nth-child(1) {
                             font-size: 20px;
                         }
                         span:nth-child(2) {
                             font-size: 9pt;
                             position: absolute;
@@ -265,15 +279,15 @@
         
                                 &__clock {
                                     font-size: 9pt;
                                 }
                                 &__edited {
                                     font-size: 9pt;
                                     padding: 0 7px;
-                                    margin-top: -3px !important;
+                                    margin-top: -3px;
                                 }
                                 &__status {
                                     img {
                                         height: 14px;
                                         width: 16px;
                                         margin-left: 5px;
                                     }
@@ -484,14 +498,20 @@
                                 right: 10px;
                                 color: $secondry;
                                 font-size: 13px;
                                 padding: 0 7px;
                                 background-color: white;
                                 transition: all 0.3s linear;
                             }
+                            p.form_error {
+                                color: red;
+                                font-size: 12px;
+                                margin: 0px;
+                                margin-top: 5px;
+                            }
                         }
                         .mbnone__chatapp {margin-bottom: unset !important;}
                         .chatapp_button {
                             width: 100%;
                             display: flex;
                             justify-content: end;
                             margin-top: 13px;
@@ -540,16 +560,18 @@
                         }
                     }
 
                 }
             }
         }
         .body__inputs {
-            padding: 8px 10px;
+            padding: 0px 10px;
             padding-top: 4px !important;
+            background-color: white;
+            border-radius: 0 0 10px 10px;
 
             form {
                 div.forminput_wrapper {
                     background-color: #ececec;
                     border-radius: 25px;
                     display: flex;
                     position: relative;
@@ -627,15 +649,16 @@
                             display: flex;
                             flex-direction: row;
                             flex-wrap: wrap;
                             
                             div.emoji_item {
                                 flex: 1;
                                 cursor: pointer;
-                                padding: 3px;
+                                font-size: 18px;
+                                padding: 4px;
                                 max-width: 25px;
                             }
                         }
                     }
 
                     button.show_game {
                         outline: none;
@@ -727,14 +750,19 @@
     }
     .chatapp__msg {
         left: 14px;
         right: unset !important;
         border-radius: 10px;
         bottom: 87px;
         box-shadow: $boxshadow;
+
+        &::after {
+            right: unset !important;
+            left: 22px;
+        }
     }
     .msg__info__status img {
         margin-right: 5px;
         margin-left: unset !important;
     }
     .msg__header .msg__wrapper .header__info div span:nth-child(2) {
         right: unset !important;
@@ -782,14 +810,17 @@
     .body__inputs form div.forminput_wrapper .emoji_wrapper {
         left: 0px;
         right: unset !important;
     }
     .reply_one_msg--right {
         float: right !important;
     }
+    .body__wrapper .msg div.msg__info__edited {
+        margin-top: unset !important;
+    }
 }
 
 /* *** ANIMATIONS *** */
 @keyframes blink {
     from {opacity: 0;}
     to {opacity: 1;}
 }
@@ -806,17 +837,14 @@
 /* *** Media queries *** */
 @media screen and (min-width: 1001px) {
     .chatapp__msg .msg__header .msg__wrapper {
         width: 375px !important;
     }
 }
 @media screen and (max-width: 1000px) {
-    .chatapp__msg .msg__header .msg__wrapper {
-        width: 280px !important;
-    }
     .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(1) {
         font-size: 12pt !important;
     }
     .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(2) {
         font-size: 9pt !important;
     }
 }
```

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/css/supporter.css` & `django-chatapp-1.4/chatapp/static/django_chatapp/css/supporter.css`

 * *Files 2% similar despite different names*

```diff
@@ -1 +1 @@
-@font-face{font-family:"vazir";src:url("../font/vazir-medium.ttf"),url("../font/vazir-medium.woff")}.font-vazir{font-family:vazir !important}::-webkit-scrollbar{background-color:rgba(0,0,0,0);width:5px}::-webkit-scrollbar-thumb{border-radius:5px;background-color:#d1d1d1}.d-none{display:none !important}.chatapp__show{opacity:1 !important}.chatapp__hide{opacity:0 !important}body{background-color:#f9f9f9}section.chatapp{box-sizing:border-box;font-family:vazir !important;scroll-behavior:smooth !important;direction:rtl !important}section.chatapp .alert_box{background-color:#2391eb;color:#fff;font-size:14px;padding:1px 15px;border-radius:7px;min-width:300px;position:absolute;top:20px;right:20px;z-index:1000}section.chatapp .chatapp__msg{max-width:900px;margin:4rem auto;border-radius:10px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);height:calc(100vh - 8rem);transition:all .5s ease}section.chatapp .chatapp__msg .msg__header{background-color:#2391eb;border-radius:10px 10px 0 0}section.chatapp .chatapp__msg .msg__header .msg__wrapper{border-radius:10px 10px 0 0;padding:10px;background:linear-gradient(258deg, rgba(0, 0, 0, 0.3) 0%, rgba(84, 141, 177, 0) 100%) rgba(0,0,0,0);display:flex;justify-content:space-between}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info{display:flex}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info img{height:45px;width:45px;border-radius:50%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div{display:flex;flex-direction:column;color:#fff;margin:0 10px;position:relative}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(1){font-size:20px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(2){font-size:9pt;position:absolute;right:0;bottom:0px;display:flex;width:150px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option{display:flex;align-items:center}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns{position:relative}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns button.btns_base{outline:none;border:none;cursor:pointer;background-color:rgba(0,0,0,0);margin:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns button.btns_base img{height:20px;width:20px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section{position:absolute;top:57px;left:-2px;border-radius:7px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);background-color:#fff;padding:7px;z-index:10000;width:200px;height:207px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form{padding:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol{position:relative;margin-bottom:5px;width:100%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol textarea,section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol select{font-family:vazir;padding:7px;font-size:11px;color:#2391eb;border:1px solid #d1d1d1;border-radius:5px;outline:none;background:#fff !important;transition:all .3s linear;resize:none;width:100%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol textarea:focus,section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol select:focus{border-color:#858585}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol textarea:focus~label,section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol select:focus~label{color:#858585}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol textarea{height:90px;width:92%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol label{position:absolute;pointer-events:none;top:-10px;right:10px;color:#d1d1d1;font-size:11px;padding:0 7px;background-color:#fff;transition:all .3s linear}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form .chatapp_button{width:100%;display:flex;justify-content:end;margin-top:13px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form .chatapp_button button{font-family:vazir;border:none;outline:none;padding:5px 25px;cursor:pointer;border-radius:5px;font-size:11px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section{position:absolute;top:57px;left:-2px;border-radius:7px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);background-color:#fff;padding:7px;z-index:10000;width:200px;height:224px;overflow-y:auto}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes{overflow-y:auto;display:flex;flex-direction:column}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item{margin-bottom:5px;background-color:#f2f2f2;padding:5px;border-radius:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item p{font-size:10pt;color:#7e7e7e;margin:0px !important;word-break:break-word;padding:4px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs{display:flex;justify-content:space-between;align-items:center}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs>button{outline:none;border:none;cursor:pointer;padding:3px 7px;background-color:#d1d1d1;border-radius:5px;margin:2px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs>button img{height:15px;width:15px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs .wrapper_2btn_msgs{display:flex}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs .wrapper_2btn_msgs button{margin:2px;outline:none;border:none;cursor:pointer;padding:2px 7px;background-color:#d1d1d1;border-radius:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs .wrapper_2btn_msgs button img{height:17px;width:15px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section{position:absolute;top:67px;left:-34px;background-color:#fff;border-radius:7px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);padding:7px;z-index:10000;width:200px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section .wrapper_close_btn{margin-bottom:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section .wrapper_close_btn button.close_box{outline:none;border:none;cursor:pointer;padding:2px 7px;border-radius:50%;background-color:#ff5151;color:#fff;font-size:16px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section form input{width:90%;font-family:vazir !important;outline:none;border:none;background-color:#ececec;padding:7px 10px;border-radius:5px;margin-bottom:8px;font-size:13px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section form textarea{width:90%;resize:none;font-family:vazir !important;outline:none;border:none;background-color:#ececec;padding:7px 10px;border-radius:5px;font-size:13px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section form button{outline:none;font-family:vazir !important;background-color:#2391eb;color:#fff;border:none;border-radius:5px;padding:4px 10px;float:left;cursor:pointer}section.chatapp .chatapp__msg .msg__tabbar{width:100%;display:flex;justify-content:space-around}section.chatapp .chatapp__msg .msg__tabbar .tab_item{width:100%;padding:10px 0;text-align:center;font-size:12px;color:#000;background-color:#f2f2f2;border-left:1px solid #ccc;cursor:pointer}section.chatapp .chatapp__msg .msg__tabbar .tab_item.tab_active{background-color:#e3e3e3}section.chatapp .chatapp__msg .msgdel__right{float:right !important}section.chatapp .chatapp__msg .msgdel__left{float:left !important}section.chatapp .chatapp__msg .msg__body{background-color:#fff;padding:10px 15px;overflow-y:auto;-webkit-overflow-scrolling:touch;height:calc(100vh - 9.3rem - 120px);position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_buttons p{line-height:1rem}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_buttons p:hover a{color:#000;cursor:pointer}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_buttons p a{color:#d1d1d1;font-size:14px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output{margin:26px auto;padding:10px;border-radius:6px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);max-width:80%;border-radius:7px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form{padding:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol{position:relative;margin-bottom:5px;width:100%}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol textarea,section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol input{font-family:vazir;padding:7px;font-size:11px;color:#2391eb;border:1px solid #d1d1d1;border-radius:5px;outline:none;background:#fff !important;transition:all .3s linear;resize:none}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol textarea:focus,section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol input:focus{border-color:#858585}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol textarea:focus~label,section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol input:focus~label{color:#858585}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol textarea{height:90px;width:300px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol label{position:absolute;pointer-events:none;top:-10px;right:10px;color:#d1d1d1;font-size:11px;padding:0 7px;background-color:#fff;transition:all .3s linear}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form .chatapp_button{width:100%;display:flex;justify-content:end;margin-top:13px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form .chatapp_button button{font-family:vazir;border:none;outline:none;padding:5px 25px;cursor:pointer;border-radius:5px;font-size:11px}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box{cursor:pointer;display:flex;justify-content:space-between;align-items:center;padding:10px;margin-bottom:10px;background-color:#f2f2f2}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box .user_date_div div:nth-child(1){font-size:12pt;transition:all .3s}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box .user_date_div div:nth-child(2){font-size:9pt;color:#d1d1d1;text-align:center}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box .unreadmsg_counter{padding:5px 10px;background-color:#2391eb;border-radius:50%;color:#fff;height:100%;font-size:9pt;transition:all .3s}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box:hover{border-right:1px solid #2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box:hover .user_date_div div:nth-child(1){padding-right:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .msg_item_active .user_date_div div:nth-child(1){font-weight:900 !important;color:#fff !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .deleted_msg{background-color:#d1d1d1 !important;color:#fff !important;padding:3px 4px;font-size:13px;border-radius:5px;margin-bottom:5px;width:175px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .deleted_msg img{height:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper{width:100%;height:auto;position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar{position:absolute;top:-13px;padding:5px;background-color:#000;z-index:5;list-style:none;color:#d1d1d1;width:100px;font-size:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li{cursor:pointer;padding:3px 5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li img{height:13px;margin-bottom:-4px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li:hover{color:#fff}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar--right{right:0 !important;left:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar--left{left:0 !important;right:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper:hover .reply_one_msg{opacity:1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg{padding:7px 10px;margin-bottom:5px;max-width:500px;min-width:100px;text-align:right;color:#fff;position:relative;transition:background-color .3s linear;z-index:2}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p{margin:0px !important;word-break:break-word}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied{padding:3px 5px;border-right:2px solid #fff;margin-bottom:7px !important;border-radius:4px 0 0 4px;display:flex;flex-direction:column;cursor:pointer}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied span{font-size:9pt}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied--right{background-color:#39a2f9}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied--left{background-color:#c5c5c5}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info{margin-top:5px;margin-bottom:-5px;display:flex;flex-direction:row;justify-content:flex-start}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__clock{font-size:9pt;margin-top:2px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__edited{font-size:9pt;padding:0 7px;margin-top:0px !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__status img{height:14px;width:16px;margin-left:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left{float:left;border-radius:12px;background-color:#d1d1d1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left::after{content:"";position:absolute;bottom:9px;left:-8px;width:0;height:0;border-top:8px solid rgba(0,0,0,0);border-bottom:0px solid rgba(0,0,0,0);border-right:8px solid #d1d1d1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left div.msg__info__clock{padding-bottom:4px !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__right{float:right;border-radius:12px;background-color:#2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__right::after{content:"";position:absolute;bottom:9px;right:-8px;width:0;height:0;border-top:8px solid rgba(0,0,0,0);border-bottom:0px solid rgba(0,0,0,0);border-left:8px solid #2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg{color:#d1d1d1;font-size:10pt;opacity:0;line-height:11px;z-index:1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg--right{position:absolute;left:-67px;top:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg--left{text-align:left;position:absolute;right:-67px;top:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg span{cursor:pointer;transition:all .2s;margin:0 !important;padding:4px 0}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg span:hover{color:#9e9e9e}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .clearfix{clear:both}section.chatapp .chatapp__msg .body__inputs{padding:8px 10px;border-radius:0 0 10px 10px;padding-top:4px !important;background-color:#fff;position:relative}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper{background-color:#ececec;border-radius:25px;display:flex;position:relative}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper input{flex:auto;font-family:vazir !important;outline:none;border:none;background-color:#ececec;padding:10px 15px;border-radius:25px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper{position:absolute;bottom:44px;border-radius:7px;right:0px;background-color:#ececec;padding:5px 10px;z-index:9999;width:70%;display:flex;justify-content:space-between}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper div{order:1;display:flex;flex-direction:column}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper div p{margin:0;color:#5e5e5e;font-size:9pt;padding:0 5px;border-right:2px solid #fff;height:20px;overflow:hidden}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper button.close_replybar{order:2;color:#5e5e5e;border:none;outline:none;background-color:rgba(0,0,0,0) !important;font-size:20px;cursor:pointer;padding:0 10px 10px 0;height:100%}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper button.close_replybar:hover{color:#000}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper{position:absolute;bottom:44px;border-radius:7px;right:0px;background-color:#ececec;padding:5px 10px;z-index:9999;width:70%;height:100px;overflow-y:scroll;display:flex;justify-content:space-between}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper div.emoji_box{order:1;display:flex;flex-direction:row;flex-wrap:wrap}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper div.emoji_box div.emoji_item{flex:1;cursor:pointer;padding:3px;max-width:25px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_emoji{outline:none;background-color:rgba(0,0,0,0);border:none;padding:6px 2px;cursor:pointer;margin:0 13px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_emoji img{height:26px;width:28px;margin-bottom:-4px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.submit_msg_client{outline:none;background-color:#2391eb;border:none;margin-right:3px;border-radius:25px;padding:6px 20px;cursor:pointer}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.submit_msg_client img{height:20px;width:21px}section.chatapp .chatapp__msg .body__inputs .btn_last_msg{position:absolute;left:15px;bottom:60px;z-index:9999}section.chatapp .chatapp__msg .body__inputs .btn_last_msg button{cursor:pointer;outline:none;border:none;border-radius:50%;background-color:rgba(0,0,0,.3);position:relative}section.chatapp .chatapp__msg .body__inputs .btn_last_msg button img{height:35px;width:35px;padding:5px 3px;padding-top:8px}section.chatapp .chatapp__msg .body__inputs .btn_last_msg button div.unreadmsg_counter{position:absolute;right:-2px;top:-2px;padding:3px 7px;background-color:#2391eb;border-radius:50%;font-size:10pt;color:#fff}section.chatapp__ltr{direction:ltr !important}section.chatapp__ltr .chatapp__msg{left:14px;right:unset !important;border-radius:10px;bottom:87px;box-shadow:0 0 13px 3px rgba(0,0,0,.1)}section.chatapp__ltr .msg__info__status img{margin-right:5px;margin-left:unset !important}section.chatapp__ltr .msg__header .msg__wrapper .header__info div span:nth-child(2){right:unset !important;left:0}section.chatapp__ltr .chatapp__msg .body__inputs form div button{margin-right:unset !important;margin-left:3px}section.chatapp__ltr .m2px_l{margin-left:unset !important;margin-right:2px}section.chatapp__ltr .msg__body .body__wrapper .msg{text-align:left !important}section.chatapp__ltr .msg__body .body__wrapper .msg p.msg__replied{border-right:unset !important;border-left:2px solid #fff;border-radius:0 4px 4px 0 !important}section.chatapp__ltr .chatapp__msg .msg__header .msg__wrapper{background:linear-gradient(258deg, rgba(84, 141, 177, 0) 0%, rgba(0, 0, 0, 0.3) 100%) rgba(0,0,0,0) !important}section.chatapp__ltr .body__inputs .btn_last_msg{left:unset !important;right:15px}section.chatapp__ltr .body__inputs form div.forminput_wrapper .reply_msg_wrapper{left:0px;right:unset !important}section.chatapp__ltr .body__inputs form div.forminput_wrapper .reply_msg_wrapper div p{border-left:2px solid #fff !important;border-right:unset !important}section.chatapp__ltr .reply_one_msg--right{float:right !important}section.chatapp__ltr .header__option .copybox_section{left:unset !important;right:-2px}section.chatapp__ltr .header__option .addbox_section{left:unset !important;right:-34px}section.chatapp__ltr .body__inputs form div.forminput_wrapper .emoji_wrapper{left:0px;right:unset !important}section.chatapp__ltr .reportbox_section{right:-2px;left:unset !important}@media screen and (max-width: 1000px){.all__msg__wrapper .msg{max-width:300px !important}}@-webkit-keyframes spinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}@keyframes spinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
+@font-face{font-family:"vazir";src:url("../font/vazir-medium.ttf"),url("../font/vazir-medium.woff")}.font-vazir{font-family:vazir !important}::-webkit-scrollbar{background-color:rgba(0,0,0,0);width:5px}::-webkit-scrollbar-thumb{border-radius:5px;background-color:#d1d1d1}.d-none{display:none !important}.chatapp__show{opacity:1 !important}.chatapp__hide{opacity:0 !important}body{background-color:#f9f9f9}section.chatapp{box-sizing:border-box;font-family:vazir !important;scroll-behavior:smooth !important;direction:rtl !important}section.chatapp .alert_box{background-color:#2391eb;color:#fff;font-size:14px;padding:1px 15px;border-radius:7px;min-width:300px;position:absolute;top:20px;right:20px;z-index:1000}section.chatapp .chatapp__msg{max-width:900px;margin:4rem auto;border-radius:10px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);height:calc(100vh - 8rem);transition:all .5s ease}section.chatapp .chatapp__msg .msg__header{background-color:#2391eb;border-radius:10px 10px 0 0}section.chatapp .chatapp__msg .msg__header .msg__wrapper{border-radius:10px 10px 0 0;padding:10px;background:linear-gradient(258deg, rgba(0, 0, 0, 0.3) 0%, rgba(84, 141, 177, 0) 100%) rgba(0,0,0,0);display:flex;justify-content:space-between}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info{display:flex}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info img{height:45px;width:45px;border-radius:50%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div{display:flex;flex-direction:column;color:#fff;margin:0 10px;position:relative}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(1){font-size:20px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__info div span:nth-child(2){font-size:9pt;position:absolute;right:0;bottom:0px;display:flex;width:150px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option{display:flex;align-items:center}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns{position:relative}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns button.btns_base{outline:none;border:none;cursor:pointer;background-color:rgba(0,0,0,0);margin:5px;color:#fff}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns button.btns_base img{height:20px;width:20px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section{position:absolute;top:57px;left:-2px;border-radius:7px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);background-color:#fff;padding:7px;z-index:10000;width:200px;height:207px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form{padding:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol{position:relative;margin-bottom:5px;width:100%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol textarea,section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol select{font-family:vazir;padding:7px;font-size:11px;color:#2391eb;border:1px solid #d1d1d1;border-radius:5px;outline:none;background:#fff !important;transition:all .3s linear;resize:none;width:100%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol textarea:focus,section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol select:focus{border-color:#858585}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol textarea:focus~label,section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol select:focus~label{color:#858585}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol textarea{height:90px;width:92%}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form div.chatapp_formcontrol label{position:absolute;pointer-events:none;top:-10px;right:10px;color:#d1d1d1;font-size:11px;padding:0 7px;background-color:#fff;transition:all .3s linear}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form .chatapp_button{width:100%;display:flex;justify-content:end;margin-top:13px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .reportbox_section form .chatapp_button button{font-family:vazir;border:none;outline:none;padding:5px 25px;cursor:pointer;border-radius:5px;font-size:11px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section{position:absolute;top:57px;left:-2px;border-radius:7px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);background-color:#fff;padding:7px;z-index:10000;width:200px;height:224px;overflow-y:auto}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes{overflow-y:auto;display:flex;flex-direction:column}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item{margin-bottom:5px;background-color:#f2f2f2;padding:5px;border-radius:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item p{font-size:10pt;color:#7e7e7e;margin:0px !important;word-break:break-word;padding:4px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs{display:flex;justify-content:space-between;align-items:center}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs>button{outline:none;border:none;cursor:pointer;padding:3px 7px;background-color:#d1d1d1;border-radius:5px;margin:2px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs>button img{height:15px;width:15px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs .wrapper_2btn_msgs{display:flex}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs .wrapper_2btn_msgs button{margin:2px;outline:none;border:none;cursor:pointer;padding:2px 7px;background-color:#d1d1d1;border-radius:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .copybox_section .wrapper_boxes .msg_item .wrapper_btns_msgs .wrapper_2btn_msgs button img{height:17px;width:15px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section{position:absolute;top:67px;left:-34px;background-color:#fff;border-radius:7px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);padding:7px;z-index:10000;width:200px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section .wrapper_close_btn{margin-bottom:5px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section .wrapper_close_btn button.close_box{outline:none;border:none;cursor:pointer;padding:2px 7px;border-radius:50%;background-color:#ff5151;color:#fff;font-size:16px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section form input{width:90%;font-family:vazir !important;outline:none;border:none;background-color:#ececec;padding:7px 10px;border-radius:5px;margin-bottom:8px;font-size:13px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section form textarea{width:90%;resize:none;font-family:vazir !important;outline:none;border:none;background-color:#ececec;padding:7px 10px;border-radius:5px;font-size:13px}section.chatapp .chatapp__msg .msg__header .msg__wrapper .header__option .wrapper_btns .addbox_section form button{outline:none;font-family:vazir !important;background-color:#2391eb;color:#fff;border:none;border-radius:5px;padding:4px 10px;float:left;cursor:pointer}section.chatapp .chatapp__msg .msg__tabbar{width:100%;display:flex;justify-content:space-around}section.chatapp .chatapp__msg .msg__tabbar .tab_item{width:100%;padding:10px 0;text-align:center;font-size:12px;color:#000;background-color:#f2f2f2;border-left:1px solid #ccc;cursor:pointer}section.chatapp .chatapp__msg .msg__tabbar .tab_item span{padding:1px 10px;background-color:#2391eb;border-radius:50%;font-size:7pt;color:#fff}section.chatapp .chatapp__msg .msg__tabbar .tab_item.tab_active{background-color:#e3e3e3}section.chatapp .chatapp__msg .msgdel__right{float:right !important}section.chatapp .chatapp__msg .msgdel__left{float:left !important}section.chatapp .chatapp__msg .msg__body{background-color:#fff;padding:10px 15px;padding-top:20px;overflow-y:auto;-webkit-overflow-scrolling:touch;height:calc(100vh - 9.3rem - 160px);position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_buttons{margin:auto;max-width:70%}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_buttons p{line-height:6px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_buttons p a{color:#d1d1d1;font-size:14px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output{margin:26px auto;padding:10px;border-radius:6px;box-shadow:0 0 13px 3px rgba(0,0,0,.1);max-width:70%;border-radius:7px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form{padding:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol{position:relative;margin-bottom:5px;width:100%}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol textarea,section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol input{font-family:vazir;padding:7px;font-size:11px;color:#2391eb;border:1px solid #d1d1d1;border-radius:5px;outline:none;background:#fff !important;transition:all .3s linear;resize:none}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol textarea:focus,section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol input:focus{border-color:#858585}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol textarea:focus~label,section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol input:focus~label{color:#858585}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol textarea{height:90px;max-width:92%;min-width:70%}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form div.chatapp_formcontrol label{position:absolute;pointer-events:none;top:-10px;right:10px;color:#d1d1d1;font-size:11px;padding:0 7px;background-color:#fff;transition:all .3s linear}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form .chatapp_button{width:100%;display:flex;justify-content:end;margin-top:13px}section.chatapp .chatapp__msg .msg__body .body__wrapper .tab_menu_links .wrapper_output form .chatapp_button button{font-family:vazir;border:none;outline:none;padding:5px 25px;cursor:pointer;border-radius:5px;font-size:11px}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .border_red{border-right:1px solid red}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .border_green{border-right:1px solid #00e100}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box{cursor:pointer;display:flex;justify-content:space-between;align-items:center;padding:10px;max-width:70%;margin-left:auto;margin-right:auto;margin-bottom:10px;background-color:#fff;box-shadow:0 0 12px 0px rgba(0,0,0,.1);transition:all .3s ease}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box .no__data{color:#bfbfbf;font-size:15px;padding:6px}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box .user_date_div{direction:ltr !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box .user_date_div div:nth-child(1){font-size:12pt;transition:all .3s;text-align:end}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box .user_date_div div:nth-child(2){font-size:9pt;color:#d1d1d1;text-align:end}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box .unreadmsg_counter{padding:5px 16px;background-color:#2391eb;border-radius:50%;color:#fff;height:100%;font-size:9pt;transition:all .3s;margin-left:10px}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .chat__box:hover{transform:translateY(-1px)}section.chatapp .chatapp__msg .msg__body .body__wrapper .wrapper__chatboxes .msg_item_active .user_date_div div:nth-child(1){font-weight:900 !important;color:#fff !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .deleted_msg{background-color:#d1d1d1 !important;color:#fff !important;padding:3px 4px;font-size:13px;border-radius:5px;margin-bottom:5px;width:175px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .deleted_msg img{height:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper{width:100%;height:auto;position:relative}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar{position:absolute;top:-13px;padding:5px;background-color:#000;z-index:5;list-style:none;color:#d1d1d1;width:100px;font-size:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li{cursor:pointer;padding:3px 5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li img{height:13px;margin-bottom:-4px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar li:hover{color:#fff}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar--right{right:0 !important;left:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper ul.msg-menu-bar--left{left:0 !important;right:unset !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper:hover .reply_one_msg{opacity:1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg{padding:7px 10px;margin-bottom:5px;max-width:500px;min-width:100px;text-align:right;color:#fff;position:relative;transition:background-color .3s linear;z-index:2}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p{margin:0px !important;word-break:break-word}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied{padding:3px 5px;border-right:2px solid #fff;margin-bottom:7px !important;border-radius:4px 0 0 4px;display:flex;flex-direction:column;cursor:pointer}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied span{font-size:9pt}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied--right{background-color:#39a2f9}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg p.msg__replied--left{background-color:#c5c5c5}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info{margin-top:5px;margin-bottom:-5px;display:flex;flex-direction:row;justify-content:flex-start}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__clock{font-size:9pt;margin-top:2px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__edited{font-size:9pt;padding:0 7px;margin-top:0px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg div.msg__info__status img{height:14px;width:16px;margin-left:5px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left{float:left;border-radius:12px;background-color:#d1d1d1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left::after{content:"";position:absolute;bottom:9px;left:-8px;width:0;height:0;border-top:8px solid rgba(0,0,0,0);border-bottom:0px solid rgba(0,0,0,0);border-right:8px solid #d1d1d1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__left div.msg__info__clock{padding-bottom:4px !important}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__right{float:right;border-radius:12px;background-color:#2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .msg__right::after{content:"";position:absolute;bottom:9px;right:-8px;width:0;height:0;border-top:8px solid rgba(0,0,0,0);border-bottom:0px solid rgba(0,0,0,0);border-left:8px solid #2391eb}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg{color:#d1d1d1;font-size:10pt;opacity:0;line-height:11px;z-index:1}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg--right{position:absolute;left:-67px;top:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg--left{text-align:left;position:absolute;right:-67px;top:12px}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg span{cursor:pointer;transition:all .2s;margin:0 !important;padding:4px 0}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper div.one_msg_wrapper .reply_one_msg span:hover{color:#9e9e9e}section.chatapp .chatapp__msg .msg__body .body__wrapper .all__msg__wrapper .clearfix{clear:both}section.chatapp .chatapp__msg .body__inputs{padding:8px 10px;border-radius:0 0 10px 10px;padding-top:4px !important;background-color:#fff;position:relative}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper{background-color:#ececec;border-radius:25px;display:flex;position:relative}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper input{flex:auto;font-family:vazir !important;outline:none;border:none;background-color:#ececec;padding:10px 15px;border-radius:25px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper{position:absolute;bottom:44px;border-radius:7px;right:0px;background-color:#ececec;padding:5px 10px;z-index:9999;width:70%;display:flex;justify-content:space-between}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper div{order:1;display:flex;flex-direction:column}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper div p{margin:0;color:#5e5e5e;font-size:9pt;padding:0 5px;border-right:2px solid #fff;height:20px;overflow:hidden}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper button.close_replybar{order:2;color:#5e5e5e;border:none;outline:none;background-color:rgba(0,0,0,0) !important;font-size:20px;cursor:pointer;padding:0 10px 10px 0;height:100%}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .reply_msg_wrapper button.close_replybar:hover{color:#000}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper{position:absolute;bottom:44px;border-radius:7px;right:0px;background-color:#ececec;padding:5px 10px;z-index:9999;width:70%;height:100px;overflow-y:scroll;display:flex;justify-content:space-between}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper div.emoji_box{order:1;display:flex;flex-direction:row;flex-wrap:wrap}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper .emoji_wrapper div.emoji_box div.emoji_item{flex:1;cursor:pointer;font-size:18px;padding:4px;max-width:25px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_emoji{outline:none;background-color:rgba(0,0,0,0);border:none;padding:6px 2px;cursor:pointer;margin:0 13px !important}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.show_emoji img{height:26px;width:28px;margin-bottom:-4px}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.submit_msg_client{outline:none;background-color:#2391eb;border:none;margin-right:3px;border-radius:25px;padding:6px 20px;cursor:pointer}section.chatapp .chatapp__msg .body__inputs form div.forminput_wrapper button.submit_msg_client img{height:20px;width:21px}section.chatapp .chatapp__msg .body__inputs .btn_last_msg{position:absolute;left:15px;bottom:60px;z-index:9999}section.chatapp .chatapp__msg .body__inputs .btn_last_msg button{cursor:pointer;outline:none;border:none;border-radius:50%;background-color:rgba(0,0,0,.3);position:relative}section.chatapp .chatapp__msg .body__inputs .btn_last_msg button img{height:35px;width:35px;padding:5px 3px;padding-top:8px}section.chatapp .chatapp__msg .body__inputs .btn_last_msg button div.unreadmsg_counter{position:absolute;right:-2px;top:-2px;padding:3px 7px;background-color:#2391eb;border-radius:50%;font-size:10pt;color:#fff}section.chatapp__ltr{direction:ltr !important}section.chatapp__ltr .chatapp__msg{left:14px;right:unset !important;border-radius:10px;bottom:87px;box-shadow:0 0 13px 3px rgba(0,0,0,.1)}section.chatapp__ltr .msg__info__status img{margin-right:5px;margin-left:unset !important}section.chatapp__ltr .msg__header .msg__wrapper .header__info div span:nth-child(2){right:unset !important;left:0}section.chatapp__ltr .chatapp__msg .body__inputs form div button{margin-right:unset !important;margin-left:3px}section.chatapp__ltr .m2px_l{margin-left:unset !important;margin-right:2px}section.chatapp__ltr .msg__body .body__wrapper .msg{text-align:left !important}section.chatapp__ltr .msg__body .body__wrapper .msg p.msg__replied{border-right:unset !important;border-left:2px solid #fff;border-radius:0 4px 4px 0 !important}section.chatapp__ltr .chatapp__msg .msg__header .msg__wrapper{background:linear-gradient(258deg, rgba(84, 141, 177, 0) 0%, rgba(0, 0, 0, 0.3) 100%) rgba(0,0,0,0) !important}section.chatapp__ltr .body__inputs .btn_last_msg{left:unset !important;right:15px}section.chatapp__ltr .body__inputs form div.forminput_wrapper .reply_msg_wrapper{left:0px;right:unset !important}section.chatapp__ltr .body__inputs form div.forminput_wrapper .reply_msg_wrapper div p{border-left:2px solid #fff !important;border-right:unset !important}section.chatapp__ltr .reply_one_msg--right{float:right !important}section.chatapp__ltr .header__option .copybox_section{left:unset !important;right:-2px}section.chatapp__ltr .header__option .addbox_section{left:unset !important;right:-34px}section.chatapp__ltr .body__inputs form div.forminput_wrapper .emoji_wrapper{left:0px;right:unset !important}section.chatapp__ltr .reportbox_section{right:-2px;left:unset !important}section.chatapp__ltr .body__wrapper .msg div.msg__info__edited{margin-top:3px !important}section.chatapp__ltr .wrapper_output form .chatapp_formcontrol label{right:unset !important;left:10px}section.chatapp__ltr .reportbox_section form .chatapp_formcontrol label{right:unset !important;left:10px}section.chatapp__ltr .border_red{border-right:unset !important;border-left:1px solid red}section.chatapp__ltr .border_green{border-right:unset !important;border-left:1px solid #00e100}section.chatapp__ltr .chat__box .user_date_div div:nth-child(1),section.chatapp__ltr .chat__box .user_date_div div:nth-child(2){text-align:start !important}@media screen and (max-width: 1000px){body{margin:0;padding:0}.msg__header{border-radius:0 !important}.msg__wrapper{border-radius:0 !important}.all__msg__wrapper .msg{max-width:300px !important}.chatapp__msg{max-width:unset !important;margin:unset !important;border-radius:unset !important;box-shadow:unset !important;height:100vh !important}.msg__body{height:calc(100vh - 9.3rem - 70px) !important}}@keyframes spinner{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}
```

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/css/supporter.scss` & `django-chatapp-1.4/chatapp/static/django_chatapp/css/supporter.scss`

 * *Files 3% similar despite different names*

```diff
@@ -104,14 +104,15 @@
 
                         button.btns_base {
                             outline: none;
                             border: none;
                             cursor: pointer;
                             background-color: transparent;
                             margin: 5px;
+                            color: white;
 
                             img {
                                 height: 20px;
                                 width: 20px;
                             }
                         }
 
@@ -341,14 +342,22 @@
                 padding: 10px 0;
                 text-align: center;
                 font-size: 12px;
                 color: #000;
                 background-color: #f2f2f2;
                 border-left: 1px solid #ccc;
                 cursor: pointer;
+
+                span {
+                    padding: 1px 10px;
+                    background-color: $primary;
+                    border-radius: 50%;
+                    font-size: 7pt;
+                    color: $white;
+                }
             }
             .tab_item.tab_active {
                 background-color: #e3e3e3;
             }
         }
 
         .msgdel__right {
@@ -357,47 +366,43 @@
         .msgdel__left {
             float: left !important;
         }
 
         .msg__body {
             background-color: $white;
             padding: 10px 15px;
+            padding-top: 20px;
             overflow-y: auto;
             -webkit-overflow-scrolling: touch;
-            height: calc(100vh - 9.3rem - 120px);
+            height: calc(100vh - 9.3rem - 160px);
             position: relative;
 
             .body__wrapper {
 
                 .tab_menu_links {
 
                     .wrapper_buttons {
-                    
-                        p {
-                            line-height: 1rem;
+                        margin: auto;
+                        max-width: 70%;
 
-                            &:hover {
-                                a {
-                                    color: black;
-                                    cursor: pointer;
-                                }
-                            }
+                        p {
+                            line-height: 6px;
 
                             a {
                                 color: $secondry;
                                 font-size: 14px;
                             }
                         }
                     }
                     .wrapper_output {
                         margin: 26px auto;
                         padding: 10px;
                         border-radius: 6px;
                         box-shadow: 0 0 13px 3px rgba(0,0,0,.1);
-                        max-width: 80%;
+                        max-width: 70%;
                         border-radius: 7px;
 
                         form {
                             padding: 5px; 
     
                             div.chatapp_formcontrol {
                                 position: relative;
@@ -421,15 +426,16 @@
                                     }
                                     &:focus ~ label {
                                         color: darken($secondry, 30%);
                                     }
                                 }
                                 textarea {
                                     height: 90px;
-                                    width: 300px;
+                                    max-width: 92%;
+                                    min-width: 70%;
                                 }
                                 label {
                                     position: absolute;
                                     pointer-events: none;
                                     top: -10px;
                                     right: 10px;
                                     color: $secondry;
@@ -456,51 +462,69 @@
                                 }
                             }
                         }
                     }
                 }
 
                 .wrapper__chatboxes {
+
+                    .border_red {
+                        border-right: 1px solid red;
+                    }
+                    .border_green {
+                        border-right: 1px solid #00e100;
+                    }
                 
                     .chat__box {
                         cursor: pointer;
                         display: flex;
                         justify-content: space-between;
                         align-items: center;
                         padding: 10px;
+                        max-width: 70%;
+                        margin-left: auto;
+                        margin-right: auto;
                         margin-bottom: 10px;
-                        background-color: #f2f2f2;
+                        background-color: white;
+                        box-shadow: 0 0 12px 0px rgba(0, 0, 0, 0.1);
+                        transition: all .3s ease;
+
+                        .no__data {
+                            color: #bfbfbf;
+                            font-size: 15px;
+                            padding: 6px;
+                        }
         
                         .user_date_div {
+                            direction: ltr !important;
+
                             div:nth-child(1) {
                                 font-size: 12pt;
                                 transition: all 0.3s;
+                                text-align: end;
                             }
                             div:nth-child(2) {
                                 font-size: 9pt;
                                 color: #d1d1d1;
-                                text-align: center;
+                                text-align: end;
                             }
                         }
                         .unreadmsg_counter {
-                            padding: 5px 10px;
+                            padding: 5px 16px;
                             background-color: $primary;
                             border-radius: 50%;
                             color: white;
                             height: 100%;
                             font-size: 9pt;
                             transition: all 0.3s;
+                            margin-left: 10px;
                         }
     
                         &:hover {
-                            border-right: 1px solid $primary;
-
-                            .user_date_div div:nth-child(1) {
-                                padding-right: 5px;
-                            }
+                            transform: translateY(-1px);
                         }
                     }
                     .msg_item_active {
                         .user_date_div div:nth-child(1) {
                             font-weight: 900 !important;
                             color: $white !important;
                         }
@@ -612,15 +636,15 @@
                                 &__clock {
                                     font-size: 9pt;
                                     margin-top: 2px;
                                 }
                                 &__edited {
                                     font-size: 9pt;
                                     padding: 0 7px;
-                                    margin-top: 0px !important;
+                                    margin-top: 0px;
                                 }
                                 &__status {
                                     img {
                                         height: 14px;
                                         width: 16px;
                                         margin-left: 5px;
                                     }
@@ -788,27 +812,28 @@
                             display: flex;
                             flex-direction: row;
                             flex-wrap: wrap;
                             
                             div.emoji_item {
                                 flex: 1;
                                 cursor: pointer;
-                                padding: 3px;
+                                font-size: 18px;
+                                padding: 4px;
                                 max-width: 25px;
                             }
                         }
                     }
 
                     button.show_emoji {
                         outline: none;
                         background-color: transparent;
                         border: none;
                         padding: 6px 2px;
                         cursor: pointer;
-                        margin: 0 13px;
+                        margin: 0 13px !important;
 
                         img {
                             height: 26px;
                             width: 28px;
                             margin-bottom: -4px;
                         }
                     }
@@ -935,21 +960,63 @@
         left: 0px;
         right: unset !important;
     }
     .reportbox_section {
         right: -2px;
         left: unset !important;
     }
+    .body__wrapper .msg div.msg__info__edited {
+        margin-top: 3px !important;
+    }
+    .wrapper_output form .chatapp_formcontrol label {
+        right: unset !important;
+        left: 10px;
+    }
+    .reportbox_section form .chatapp_formcontrol label {
+        right: unset !important;
+        left: 10px;
+    }
+    .border_red {
+        border-right: unset !important;
+        border-left: 1px solid red; 
+    }
+    .border_green {
+        border-right: unset !important;
+        border-left: 1px solid #00e100; 
+    }
+    .chat__box .user_date_div div:nth-child(1), .chat__box .user_date_div div:nth-child(2) {
+        text-align: start !important;
+    }
 }
 
 /* *** MEDIA QUERIES *** */
 @media screen and (max-width: 1000px) {
+    body {
+        margin: 0;
+        padding: 0;
+    }
+    .msg__header {
+        border-radius: 0 !important;
+    }
+    .msg__wrapper {
+        border-radius: 0 !important;
+    }
     .all__msg__wrapper .msg {
         max-width: 300px !important;
     }
+    .chatapp__msg {
+        max-width: unset !important;
+        margin: unset !important;
+        border-radius: unset !important;
+        box-shadow: unset !important;
+        height: 100vh !important;
+    }
+    .msg__body {
+        height: calc(100vh - 9.3rem - 70px) !important;
+    }
 }
 /* *** ANIMATIONS *** */
 @keyframes spinner {
     0% { 
         transform: rotate(0deg)
     }
     100% {
```

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/font/vazir-medium.ttf` & `django-chatapp-1.4/chatapp/static/django_chatapp/font/vazir-medium.ttf`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/font/vazir-medium.woff` & `django-chatapp-1.4/chatapp/static/django_chatapp/font/vazir-medium.woff`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/img/chat-room.png` & `django-chatapp-1.4/chatapp/static/django_chatapp/img/chat-room.png`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/img/emoji.png` & `django-chatapp-1.4/chatapp/static/django_chatapp/img/emoji.png`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/img/game.png` & `django-chatapp-1.4/chatapp/static/django_chatapp/img/game.png`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/img/loader.png` & `django-chatapp-1.4/chatapp/static/django_chatapp/img/loader.png`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/img/o.png` & `django-chatapp-1.4/chatapp/static/django_chatapp/img/o.png`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/img/send.png` & `django-chatapp-1.4/chatapp/static/django_chatapp/img/send.png`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/img/supporter.png` & `django-chatapp-1.4/chatapp/static/django_chatapp/img/supporter.png`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/static/django_chat_app/img/x.png` & `django-chatapp-1.4/chatapp/static/django_chatapp/img/x.png`

 * *Files identical despite different names*

### Comparing `django-chatapp-1.3/chatapp/templates/client.html` & `django-chatapp-1.4/chatapp/templates/client.html`

 * *Files 20% similar despite different names*

```diff
@@ -1,34 +1,35 @@
 {% load static %}
 
-<link rel="stylesheet" href="{% static 'django_chat_app/css/custom.css' %}">
+<link rel="stylesheet" href="{% static 'django_chatapp/css/client.css' %}">
 
 <section class="chatapp" id="chatapp">
 
-    <span id="sound_sendmsg" class="d-none">{% static 'django_chat_app/media/send.mp3' %}</span>
+    <span id="sound_sendmsg" class="d-none">{% static 'django_chatapp/song/send.mp3' %}</span>
+    <span id="chat_locale" class="d-none"></span>
 
     <div class="chatapp__btn" @click="open_close_box">
         <div>
-            <img src="{% static 'django_chat_app/img/chat-room.png' %}" alt="Django Chat Application!">
+            <img src="{% static 'django_chatapp/img/chat-room.png' %}" alt="Django Chat Application!">
             <div id="alert_msg_ctx" :class="counter_new_msg > 0 ? '' : 'd-none'"></div>
         </div>
     </div>
 
     <div class="chatapp__msg d-none chatapp__hide">
         <div class="msg__header">
             <div class="msg__wrapper">
                 <div class="header__info">
-                    <img src="{% static 'django_chat_app/img/supporter.png' %}" alt="">
+                    <img src="{% static 'django_chatapp/img/supporter.png' %}" alt="supporter image">
                     <div>
                         <span></span>
-                        <span>[[ receiver_status == 'online' ? 'آنلاین' : 'آخرین بازدید به تازگی' ]]</span>
+                        <span>[[ receiver_status == 'online' ? $t('online') : $t('last seen recently') ]]</span>
                     </div>
                 </div>
                 <div class="header__options">
-                    <button class="close__msgbox" id="close__msgbox" @click="open_close_box"><img src="{% static 'django_chat_app/img/close.png' %}" alt="close chat application"></button>
+                    <button class="close__msgbox" id="close__msgbox" @click="open_close_box"><img src="{% static 'django_chatapp/img/close.png' %}" alt="close chat application"></button>
                     <button class="close__msgbox d-none" id="loader_spinner"><div class="loader_spinner loader_spinner--white"></div></button>
                 </div>
             </div>
         </div>
 
         <div class="msg__body">        
             <div class="body__wrapper">
@@ -37,82 +38,82 @@
                 <div class="all__msg__wrapper d-none">
 
                     <template v-if="message_list.length == 0">
                         <div class="one_msg_wrapper">
 
                             <div class="msg msg__left">
                                 <p class="msg__content">
-                                    با عرض سلام، پشتیبان تا لحظاتی دیگر آنلاین خواهد شد. لطفا صبور باشید.
+                                    [[ $t('Hello, the supporter will be online in a few moments. please await.') ]]
                                 </p>
                                 <div class="msg__info">
                                 </div>
                             </div>
                         </div>
                     </template>
 
                     <template v-else v-for="msg_item in message_list" :key="msg_item.id">
                         <div v-if="!msg_item.is_deleted" class="one_msg_wrapper">
 
                             <ul :id="`msg-menu-bar-${msg_item.id}`" class="msg-menu-bar d-none" :class="msg_item.sender_type == 'client' ? 'msg-menu-bar--left' : 'msg-menu-bar--right'">
-                                <li @click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)"><img src="{% static 'django_chat_app/img/reply.png' %}" alt=""> پاسخ دادن</li>
-                                <li @click="copy_ready_msg(msg_item.text)"><img src="{% static 'django_chat_app/img/copy.png' %}" alt=""> کپی متن</li>
-                                <li v-if="edit_user_msg && msg_item.sender_type == 'client' && !msg_item.is_edited" @click="edit_message(`chatapp_msg_${msg_item.id}`, msg_item.id)"><img src="{% static 'django_chat_app/img/edit.png' %}" alt=""> ویرایش پیام</li>
-                                <li v-if="delete_user_msg && msg_item.sender_type == 'client'" @click="delete_message(msg_item.id)"><img src="{% static 'django_chat_app/img/delete.png' %}" alt=""> حذف پیام</li>
+                                <li @click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)"><img src="{% static 'django_chatapp/img/reply.png' %}" alt="reply"> [[ $t('Reply') ]]</li>
+                                <li @click="copy_ready_msg(msg_item.text)"><img src="{% static 'django_chatapp/img/copy.png' %}" alt="copy"> [[ $t('Copy') ]]</li>
+                                <li v-if="edit_user_msg && msg_item.sender_type == 'client' && !msg_item.is_edited" @click="edit_message(`chatapp_msg_${msg_item.id}`, msg_item.id)"><img src="{% static 'django_chatapp/img/edit.png' %}" alt="edit"> [[ $t('Edit') ]]</li>
+                                <li v-if="delete_user_msg && msg_item.sender_type == 'client'" @click="delete_message(msg_item.id)"><img src="{% static 'django_chatapp/img/delete.png' %}" alt="remove"> [[ $t('Remove') ]]</li>
                             </ul>
 
                             <div class="msg" :class="msg_item.sender_type == 'client' ? 'msg__right' : 'msg__left'" :id="'chatapp_msg_' + msg_item.id">
                                 <p v-if="msg_item.reply_title" class="msg__replied" :class="msg_item.sender_type == 'client' ? 'msg__replied--right' : 'msg__replied--left'" @click="msg_replied(`chatapp_msg_${msg_item.reply_id}`)">
-                                    <span>[[ msg_item.reply_title == 'client' ? 'شما' : 'پشتیبان' ]]</span>
+                                    <span>[[ msg_item.reply_title == 'client' ? $('You') : $t('Supporter') ]]</span>
                                     <span v-if="!msg_item.reply_is_deleted">[[ msg_item.reply_msg ]]</span>
-                                    <span v-else>این پیام حذف شده است</span>
+                                    <span v-else>[[ $t('This message has been deleted.') ]]</span>
                                 </p>
                                 <p class="msg__content">
                                     [[ msg_item.text ]]
                                 </p>
                                 <div class="msg__info">
                                     <div class="msg__info__status" v-if="msg_item.sender_type == 'client'">
-                                        <img v-if="msg_item.is_seen" src="{% static 'django_chat_app/img/double-check.png' %}" alt="double check status">
-                                        <img v-else src="{% static 'django_chat_app/img/single-check.png' %}" alt="single check status">
+                                        <img v-if="msg_item.is_seen" src="{% static 'django_chatapp/img/double-check.png' %}" alt="double check status">
+                                        <img v-else src="{% static 'django_chatapp/img/single-check.png' %}" alt="single check status">
                                     </div>
                                     <div class="msg__info__clock">[[ msg_item.created ]]</div>
-                                    <div class="msg__info__edited" v-if="msg_item.is_edited">ویرایش شده</div>
+                                    <div class="msg__info__edited" v-if="msg_item.is_edited">[[ $t('edited') ]]</div>
                                 </div>
                             </div>
                             <div class="reply_one_msg" :class="msg_item.sender_type == 'client' ? 'reply_one_msg--right' : 'reply_one_msg--left'">
-                                <span @click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)">پاسخ دادن</span>
+                                <span @click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)">[[ $t('reply') ]]</span>
                                 <br><br>
-                                <span class="toggle_mneubar" @click="show_menu_bar(`msg-menu-bar-${msg_item.id}`)">بیشتر</span>
+                                <span class="toggle_mneubar" @click="show_menu_bar(`msg-menu-bar-${msg_item.id}`)">[[ $t('more') ]]</span>
                             </div>
                         </div>
                         <div v-if="msg_item.is_deleted && show_deleted_msg">
                             <div class="msg__content deleted_msg"  :class="msg_item.sender_type == 'client' ? 'msgdel__right' : 'msgdel__left'">
-                                <img src="{% static 'django_chat_app/img/delete.png' %}" alt=""> این پیام حذف شده است.
+                                <img src="{% static 'django_chatapp/img/delete.png' %}" alt="delete"> [[ $t('This message has been deleted.') ]]
                             </div>
                         </div>
                         <div class="clearfix"></div>
                     </template>
 
                 </div>
                 <!-- - messages wrapper -->
 
                 <!-- + tictoctoe game -->
                 <div class="tictoctoe__game d-none">
                     
-                    <button id="restart__game">شروع دوباره</button>
+                    <button id="restart__game">[[ $t('Play again') ]]</button>
                     <div id="score__game">
-                        <div><span>شما:</span><span>0</span></div>
-                        <div><span>کامپیوتر:</span><span>0</span></div>
+                        <div><span>[[ $t('You') ]]:</span><span>0</span></div>
+                        <div><span>[[ $t('Computer') ]]:</span><span>0</span></div>
                     </div>
                     <p id="game_alert_msg" class="d-none"></p>
                                     
                     <div class="btns__wrapper">
 
                         <div id="bg__glass" class="d-none"></div>
-                        <img src="{% static 'django_chat_app/img/o.png' %}" id="oimage_game" class="d-none" alt="this image is dnone because js handle image src">
-                        <img src="{% static 'django_chat_app/img/x.png' %}" id="ximage_game" class="d-none" alt="this image is dnone because js handle image src">
+                        <img src="{% static 'django_chatapp/img/o.png' %}" id="oimage_game" class="d-none" alt="this image is dnone because js handle image src">
+                        <img src="{% static 'django_chatapp/img/x.png' %}" id="ximage_game" class="d-none" alt="this image is dnone because js handle image src">
 
                         <div class="btns__wrapper__btn">
                             <div class="btn_game m2px_b m2px_l" id="btn11"></div>
                             <div class="btn_game m2px_b m2px_l" id="btn12"></div>
                             <div class="btn_game m2px_b" id="btn13"></div>
                         </div>
                         <div class="btns__wrapper__btn">
@@ -128,62 +129,66 @@
                     </div>
                 </div>
                 <!-- - tictoctoe game -->
 
                 <!-- + login form -->
                 <div class="chatapp__form d-none">
                     <div class="chatform__header">
-                        <p>جهت پشتیبانی و راهنمایی بهتر، لطفا مشخصات خود را بصورت صحیح وارد نمایید.</p>
+                        <p>[[ $t('For better support and guidance, please enter your details correctly.') ]]</p>
                     </div>
 
                     <form novalidate @submit.prevent="chatapp_submitform">
                         <div class="chatapp_formcontrol">
                             <input type="text" id="chatapp__fname" autocomplete="off">
-                            <label for="chatapp__fname">نام</label>
+                            <label for="chatapp__fname">[[ $t('First Name') ]]</label>
+                            <p class="form_error" v-if="form_errors.fname != ''">[[ form_errors.fname ]]</p>
                         </div>
                         <div class="chatapp_formcontrol">
                             <input type="text" id="chatapp__lname" autocomplete="off">
-                            <label for="chatapp__lname">نام خانوادگی</label>
+                            <label for="chatapp__lname">[[ $t('Last Name') ]]</label>
+                            <p class="form_error" v-if="form_errors.lname != ''">[[ form_errors.lname ]]</p>
                         </div>
                         <div class="chatapp_formcontrol chatapp_control_email d-none">
                             <input type="email" id="chatapp__email" autocomplete="off">
-                            <label for="chatapp__email">ایمیل</label>
+                            <label for="chatapp__email">[[ $t('E-mail') ]]</label>
+                            <p class="form_error" v-if="form_errors.phone_email != ''">[[ form_errors.phone_email ]]</p>
                         </div>
                         <div class="chatapp_formcontrol chatapp_control_phone mbnone__chat-app d-none">
                             <input type="number" id="chatapp__phone" autocomplete="off">
-                            <label for="chatapp__phone">شماره تماس</label>
+                            <label for="chatapp__phone">[[ $t('Phone') ]]</label>
+                            <p class="form_error" v-if="form_errors.phone_email != ''">[[ form_errors.phone_email ]]</p>
                         </div>
 
                         <div class="chatapp_button">
-                            <button id="chatapp_submitform" type="submit">ارسال</button>
+                            <button id="chatapp_submitform" type="submit">[[ $t('Send') ]]</button>
                         </div>
                     </form>
                 </div>
                 <!-- - login form -->
 
                 <div class="btn_last_msg d-none">
                     <button @click="go_to_bottom_of_box">
-                        <img src="{% static 'django_chat_app/img/gotodown.png' %}" alt="go to last msg img">
+                        <img src="{% static 'django_chatapp/img/gotodown.png' %}" alt="go to last msg img">
                         <div class="unreadmsg_counter"></div>
                     </button>
                 </div>
 
             </div>
         </div>
 
         <div class="body__inputs">
             <form novalidate class="d-none" @submit.prevent="sned_msg_socket">
                 <div class="forminput_wrapper">
                     
-                    <input type="text" v-model="msg_input" id="text-chatinput" autocomplete="off" placeholder="پیام خود را وارد کنید:">
+                    <input type="text" v-model="msg_input" id="text-chatinput" autocomplete="off" :placeholder="$t('Enter your message:')">
                     <button class="show_emoji" type="button" @click="show_emojibar">
-                        <img src="{% static 'django_chat_app/img/emoji.png' %}" alt="toggle emojis">
+                        <img src="{% static 'django_chatapp/img/emoji.png' %}" alt="toggle emojis">
                     </button>
                     <button class="show_game" type="button" @click="show_game_btn">
-                        <img src="{% static 'django_chat_app/img/game.png' %}" alt="let's go to game">
+                        <img src="{% static 'django_chatapp/img/game.png' %}" alt="let's go to game">
                     </button>
 
                     <div class="reply_msg_wrapper d-none">
                         <button class="close_replybar" type="button" @click="close_replybar">&times;</button>
                         <div>
                             <p class="reply__writer"></p>
                             <p class="reply__content"></p>
@@ -195,119 +200,83 @@
                         <div class="emoji_box">
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F600;')">&#x1F600;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F601;')">&#x1F601;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F602;')">&#x1F602;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F603;')">&#x1F603;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F604;')">&#x1F604;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F605;')">&#x1F605;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F606;')">&#x1F606;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F607;')">&#x1F607;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F608;')">&#x1F608;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F609;')">&#x1F609;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F60A;')">&#x1F60A;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F60B;')">&#x1F60B;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F60C;')">&#x1F60C;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F60D;')">&#x1F60D;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F60E;')">&#x1F60E;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F60F;')">&#x1F60F;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F610;')">&#x1F610;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F611;')">&#x1F611;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F612;')">&#x1F612;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F613;')">&#x1F613;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F614;')">&#x1F614;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F615;')">&#x1F615;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F616;')">&#x1F616;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F617;')">&#x1F617;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F618;')">&#x1F618;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F619;')">&#x1F619;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F61A;')">&#x1F61A;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F61B;')">&#x1F61B;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F61C;')">&#x1F61C;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F61D;')">&#x1F61D;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F61E;')">&#x1F61E;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F61F;')">&#x1F61F;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F620;')">&#x1F620;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F621;')">&#x1F621;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F622;')">&#x1F622;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F623;')">&#x1F623;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F624;')">&#x1F624;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F625;')">&#x1F625;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F626;')">&#x1F626;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F627;')">&#x1F627;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F628;')">&#x1F628;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F629;')">&#x1F629;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F62A;')">&#x1F62A;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F62B;')">&#x1F62B;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F62C;')">&#x1F62C;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F62D;')">&#x1F62D;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F62E;')">&#x1F62E;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F62F;')">&#x1F62F;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F630;')">&#x1F630;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F631;')">&#x1F631;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F632;')">&#x1F632;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F633;')">&#x1F633;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F634;')">&#x1F634;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F635;')">&#x1F635;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F636;')">&#x1F636;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F637;')">&#x1F637;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F641;')">&#x1F641;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F642;')">&#x1F642;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F643;')">&#x1F643;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F644;')">&#x1F644;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F910;')">&#x1F910;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F911;')">&#x1F911;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F912;')">&#x1F912;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F913;')">&#x1F913;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F914;')">&#x1F914;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F915;')">&#x1F915;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F917;')">&#x1F917;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F918;')">&#x1F918;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F919;')">&#x1F919;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F91A;')">&#x1F91A;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F91B;')">&#x1F91B;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F91C;')">&#x1F91C;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F91D;')">&#x1F91D;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F91E;')">&#x1F91E;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F91F;')">&#x1F91F;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F920;')">&#x1F920;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F921;')">&#x1F921;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F922;')">&#x1F922;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F923;')">&#x1F923;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F924;')">&#x1F924;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F925;')">&#x1F925;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F926;')">&#x1F926;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F927;')">&#x1F927;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F928;')">&#x1F928;</div>
                             <div class="emoji_item" @click="add_emoji_toinput('&#x1F929;')">&#x1F929;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F92A;')">&#x1F92A;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F92B;')">&#x1F92B;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F92C;')">&#x1F92C;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F92D;')">&#x1F92D;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F92E;')">&#x1F92E;</div>
-                            <div class="emoji_item" @click="add_emoji_toinput('&#x1F92F;')">&#x1F92F;</div>
                         </div>
                     </div>
 
                     <button type="submit">
-                        <img src="{% static 'django_chat_app/img/send.png' %}" alt="send image">
+                        <img src="{% static 'django_chatapp/img/send.png' %}" alt="send image">
                     </button>
                 </div>
             </form>
             <div class="goback_chat_btn d-none" @click="goback_chat_btn">
 
-                <div>بازگشت به صفحه‌ی چت</div>
+                <div>[[ $t('Return to Chat') ]]</div>
 
                 <div v-if="counter_new_msg > 0">
                     <div class="new_msg_shower">
-                        <div><img src="{% static 'django_chat_app/img/chat-room' %}.png" alt=""></div>
+                        <div><img src="{% static 'django_chatapp/img/chat-room' %}.png" alt="chat room image"></div>
                         <div>[[ counter_new_msg ]]</div>
                     </div>
                 </div>
 
             </div>
         </div>
     </div>
 </section>
 
-
-<script type="text/javascript" src="{% static 'django_chat_app/js/vue3.js' %}"></script>
-<script type="text/javascript" src="{% static 'django_chat_app/js/client.js' %}"></script>
+<script type="text/javascript" src="{% static 'django_chatapp/js/vue3.js' %}"></script>
+<script type="text/javascript" src="{% static 'django_chatapp/js/vue-i18n.js' %}"></script>
+<script type="text/javascript" src="{% static 'django_chatapp/js/client.js' %}"></script>
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `django-chatapp-1.3/chatapp/templates/supporter.html` & `django-chatapp-1.4/chatapp/templates/supporter.html`

 * *Files 24% similar despite different names*

```diff
@@ -1,90 +1,99 @@
-{% load static %}
+{% load static i18n %}
 <!DOCTYPE html>
 <html lang="fa">
 <head>
 
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <meta http-equiv="X-UA-Compatible" content="ie=edge">
 
-    <title>صفحه‌ی پشتیبان</title>
+    <title>{% translate 'صفحه‌ی پشتیبان' %}</title>
 
     <!-- External files2 -->
-    <link rel="stylesheet" href="{% static 'django_chat_app/css/supporter.css' %}">
+    <link rel="stylesheet" href="{% static 'django_chatapp/css/supporter.css' %}">
 
 </head>
 <body>
 
     <section class="chatapp" id="chatapp">
 
         <div class="alert_box" v-if="alert">
             <p>[[ alert ]]</p>
         </div>
 
-        <span id="sound_sendmsg" class="d-none">{% static 'django_chat_app/media/send.mp3' %}</span>
+        <span id="sound_sendmsg" class="d-none">{% static 'django_chatapp/song/send.mp3' %}</span>
 
         <p class="d-none" id="supporter_uid">{{ supporter_uid }}</p>
 
         <div class="chatapp__msg">
 
             <!-- + header -->
             <div class="msg__header">
                 <div class="msg__wrapper">
 
                     <div class="header__info">
-                        <img src="{% static 'django_chat_app/img/supporter.png' %}" alt="">
+                        <img src="{% static 'django_chatapp/img/supporter.png' %}" alt="supporter image">
                         <div>
-                            <span v-if="client_id" :title="client_id.slice(0,5) + '***' + client_id.slice(31)">[[ client_name ]]</span>
-                            <span v-if="client_id">[[ receiver_status == 'online' ? 'آنلاین' : 'آخرین بازدید به تازگی' ]]</span>
-                            <span v-else>به پنل پشتیبان خوش آمدید.</span>
+                            <span v-if="client_id" :title="client_id.slice(0,3) + '****' + client_id.slice(7,11)">[[ client_name.slice(0,35) ]]</span>
+                            <span v-if="client_id">[[ receiver_status == 'online' ? $t('online') : $t('last seen recently') ]]</span>
+                            <span v-else>[[ $t('WelCome to Supporter Panel') ]]</span>
                         </div>
                     </div>
 
                     <div class="header__option">
                         <div class="wrapper_btns">
-                            <button class="btns_base" v-if="client_id" @click="open_report_box"><img src="{% static 'django_chat_app/img/report.png' %}" alt="report user"></button>
-                            <button class="btns_base" v-if="client_id" @click="openclose_copyreadymsg"><img src="{% static 'django_chat_app/img/copy.png' %}" alt="copy msg box"></button>
-                            <button class="btns_base" v-if="client_id" @click="reset_close_chat_box"><img src="{% static 'django_chat_app/img/close.png' %}" alt="close chat box"></button>
+
+                            <button class="btns_base" v-if="!client_id && $i18n.locale != 'en'" @click="change_lang('en')">En</button>
+                            <button class="btns_base" v-if="!client_id && $i18n.locale != 'fa'" @click="change_lang('fa')">Fa</button>
+                            <button class="btns_base" v-if="!client_id && $i18n.locale != 'ar'" @click="change_lang('ar')">Ar</button>
+                            <button class="btns_base" v-if="!client_id && $i18n.locale != 'ru'" @click="change_lang('ru')">Ru</button>
+                            
+                            <button class="btns_base" v-if="client_id" @click="open_report_box"><img src="{% static 'django_chatapp/img/report.png' %}" alt="report user"></button>
+                            <button class="btns_base" v-if="client_id" @click="openclose_copyreadymsg"><img src="{% static 'django_chatapp/img/copy.png' %}" alt="copy msg box"></button>
+                            <button class="btns_base" v-if="client_id" @click="reset_close_chat_box"><img src="{% static 'django_chatapp/img/close.png' %}" alt="close chat box"></button>
                             
                             <div class="reportbox_section" v-if="which_toggle_popup == 'report'">
 
                                 <form @submit.prevent="send_report">
                                     <div class="chatapp_formcontrol" style="margin-bottom: 17px !important;">
                                         <select v-model="report_item">
-                                            <option value="badterms">استفاده از کلمات نامناسب</option>
-                                            <option value="others">دلایل دیگر</option>
+                                            <option value="badterms">[[ $t('Using inappropriate words') ]]</option>
+                                            <option value="others">[[ $t('Others') ]]</option>
                                         </select>
                                     </div>
     
                                     <div class="chatapp_formcontrol">
-                                        <label>متن گزارش</label>
+                                        <label>[[ $t('Report Content') ]]</label>
                                         <textarea v-model="report_cause"></textarea>
                                     </div>
     
                                     <div class="chatapp_button">
-                                        <button type="button" @click="send_report">ثبت گزارش</button>
+                                        <button type="button" @click="send_report">[[ $t('Send') ]]</button>
                                     </div>
                                 </form>
                             </div>
 
                             <div class="copybox_section" v-if="which_toggle_popup == 'copybox'">
 
                                 <div class="wrapper_boxes">
 
-                                    <div class="msg_item" v-for="ready_msg in ready_msgs" :key="ready_msg.id">
+                                    <div class="msg_item" v-for="ready_msg in ready_msgs" v-if="ready_msgs" :key="ready_msg.id">
                                         <p :title="ready_msg.content">[[ ready_msg.subject ]]</p>
                                         <div class="wrapper_btns_msgs">
-                                            <button v-if="ready_msg.supporter__supporter_uid == supporter_uid && !ready_msg.is_public" @click="delete_ready_msg(ready_msg.id)"><img src="{% static 'django_chat_app/img/delete.png' %}" alt="delete ready msg item"></button>
+                                            <button v-if="ready_msg.supporter__supporter_uid == supporter_uid && !ready_msg.is_public" @click="delete_ready_msg(ready_msg.id)"><img src="{% static 'django_chatapp/img/delete.png' %}" alt="delete ready msg item"></button>
                                             <div class="wrapper_2btn_msgs">
-                                                <button @click="msg_input+=ready_msg.content" v-if="client_id"><img src="{% static 'django_chat_app/img/plus.png' %}" alt="add to input"></button>
-                                                <button @click="copy_ready_msg(ready_msg.content)"><img src="{% static 'django_chat_app/img/copy.png' %}" alt="copy to clipboard"></button>
+                                                <button @click="msg_input+=ready_msg.content" v-if="client_id"><img src="{% static 'django_chatapp/img/plus.png' %}" alt="add to input"></button>
+                                                <button @click="copy_ready_msg(ready_msg.content)"><img src="{% static 'django_chatapp/img/copy.png' %}" alt="copy to clipboard"></button>
                                             </div>
                                         </div>
                                     </div>
+                                    <div class="msg_item" v-if="ready_msgs.length == 0">
+                                        <p>[[ $t('There are no ready messages.') ]]</p>
+                                    </div>
 
                                 </div>
                             </div>
 
                         </div>
 
 
@@ -92,145 +101,174 @@
 
                 </div>
             </div>
             <!-- - header -->
 
             <!-- + tabbar -->
             <div class="msg__tabbar">
-                <div class="tab_item" :class="tab_id_active == 'menu' ? 'tab_active' : ''" @click="open_tab_data('menu')">صفحه‌ی اصلی</div>
-                <div class="tab_item" :class="tab_id_active == 'yourunreads' ? 'tab_active' : ''" @click="open_tab_data('yourunreads')">پیام‌های ناخوانده‌ی شما</div>
-                <div class="tab_item" :class="tab_id_active == 'unreads' ? 'tab_active' : ''" @click="open_tab_data('unreads')">سایر پیام‌های ناخوانده</div>
-                <div class="tab_item" :class="tab_id_active == 'allpages' ? 'tab_active' : ''" @click="open_tab_data('allpages')">کاربران</div>
+                <div class="tab_item" :class="tab_id_active == 'menu' ? 'tab_active' : ''" @click="open_tab_data('menu')">
+                    [[ $t('Home') ]]
+                </div>
+                <div class="tab_item" :class="tab_id_active == 'yourunreads' ? 'tab_active' : ''" @click="open_tab_data('yourunreads')">
+                    [[ $t('Your unread Messages') ]] <span v-if="this_supporter_counter_tab > 0">[[ this_supporter_counter_tab ]]</span>
+                </div>
+                <div class="tab_item" :class="tab_id_active == 'unreads' ? 'tab_active' : ''" @click="open_tab_data('unreads')">
+                    [[ $t('Other unread Messages') ]] <span v-if="no_supoorter_counter_tab > 0">[[ no_supoorter_counter_tab ]]</span>
+                </div>
+                <div class="tab_item" :class="tab_id_active == 'allpages' ? 'tab_active' : ''" @click="open_tab_data('allpages')">
+                    [[ $t('All Users') ]]
+                </div>
             </div>
             <!-- - tabbar -->
 
             <!-- + body -->
             <div class="msg__body">        
                 <div class="body__wrapper">
 
                     <div v-if="tab_id_active=='menu'" class="tab_menu_links">
                         
                         <!-- links -->
                         <div class="wrapper_buttons">
-                            <p><a @click="menu_active_tab = 'addnewmsg'">نوشتن پیام آماده</a></p>
+                            <p><a>[[ $t('Register a Ready Message') ]]</a></p>
                         </div>
 
                         <!-- outputs -->
-                        <div class="wrapper_output" v-if="menu_active_tab">
+                        <div class="wrapper_output">
 
-                            <form novalidate @submit.prevent="submit_new_readymsg" v-if="menu_active_tab == 'addnewmsg'">
+                            <form novalidate @submit.prevent="submit_new_readymsg">
                                 
                                 <div class="chatapp_formcontrol" style="margin-bottom: 17px !important; margin-top: 7px;">
-                                    <label>عنوان متن</label>
+                                    <label>[[ $t('Subject') ]]</label>
                                     <input type="text" id="subject-chatinput" v-model="new_readymsg_subject" autocomplete="off" autofocus>
                                 </div>
                                 <div class="chatapp_formcontrol">
-                                    <label>محتوای متن</label>
+                                    <label>[[ $t('Content') ]]</label>
                                     <textarea id="content-chatinput" rows="4" v-model="new_readymsg_content" autocomplete="off"></textarea>
                                 </div>
                                 <div class="chatapp_button">
-                                    <button type="submit">ذخیره</button>
+                                    <button type="submit">[[ $t('Save') ]]</button>
                                 </div>
                             </form>
 
                         </div>
 
                     </div>
 
                     <div v-if="tab_id_active=='yourunreads'" :class="tab_data_is_show == false ? 'd-none' : ''">
                         
                         <!-- list pages -->
                         <div class="wrapper__chatboxes">
-                            <template v-for="(msg, index) in unreads_thissupporter" :key="msg">
-                                <div class="chat__box" :class="'page1_item_' + index" @click="show_user_chat_page(msg.owner_id, msg.owner_name, `page1_item_${index}`, 'thissupporter', index)">
+                            <template v-if="unreads_thissupporter.length != 0" v-for="(msg, index) in unreads_thissupporter" :key="msg">
+                                <div class="chat__box" :class="['page1_item_' + index,  msg.status == 'online' ? 'border_green' : 'border_red']" @click="show_user_chat_page(msg.owner_id, msg.owner_name, `page1_item_${index}`, 'thissupporter', index)">
                                     <div class="user_date_div">
-                                        <div>[[ msg.owner_name ]]</div>
-                                        <div>[[ msg.owner_id.slice(0,3) ]]****[[ msg.owner_id.slice(7) ]] [[ msg.status == 'online' ? ' - آنلاین' : ' - اخیرا' ]]</div>
+                                        <div :title="msg.owner_id.slice(0,3) + '****' + msg.owner_id.slice(7,11)">[[ msg.owner_name.slice(0,25) ]]</div>
+                                        <div>[[ msg.status == 'online' ? $t('online') : $t('last seen recently') ]]</div>
                                     </div>
                                     <div class="unreadmsg_counter">[[ msg.counter ]]</div>
                                 </div>
                             </template>
+                            <template v-else>
+                                <div class="chat__box">
+                                    <div class="user_date_div no__data">
+                                        <div>[[ $t('There are no unread messages for you') ]]</div>
+                                    </div>
+                                </div>
+                            </template>
                         </div>
 
                     </div>
 
                     <div v-if="tab_id_active=='unreads'" :class="tab_data_is_show == false ? 'd-none' : ''">
 
                         <!-- list pages -->
                         <div class="wrapper__chatboxes">
-                            <template v-for="(msg, index) in unreads_nosupoorter" :key="msg">
-                                <div class="chat__box" :class="'page2_item_' + index" @click="show_user_chat_page(msg.owner_id, msg.owner_name, `page2_item_${index}`, 'nosupoorter', index)">
+                            <template v-if="unreads_nosupoorter.length != 0" v-for="(msg, index) in unreads_nosupoorter" :key="msg">
+                                <div class="chat__box" :class="['page2_item_' + index, msg.status == 'online' ? 'border_green' : 'border_red']" @click="show_user_chat_page(msg.owner_id, msg.owner_name, `page2_item_${index}`, 'nosupoorter', index)">
                                     <div class="user_date_div">
-                                        <div>[[ msg.owner_name ]]</div>
-                                        <div>[[ msg.owner_id.slice(0,3) ]]****[[ msg.owner_id.slice(7) ]] [[ msg.status == 'online' ? ' - آنلاین' : ' - اخیرا' ]]</div>
+                                        <div :title="msg.owner_id.slice(0,3) + '****' + msg.owner_id.slice(7,11)">[[ msg.owner_name.slice(0,25)]]</div>
+                                        <div>[[ msg.status == 'online' ? $t('online') : $t('last seen recently') ]]</div>
                                     </div>
                                     <div class="unreadmsg_counter">[[ msg.counter ]]</div>
                                 </div>
                             </template>
+                            <template v-else>
+                                <div class="chat__box">
+                                    <div class="user_date_div no__data">
+                                        <div>[[ $t('There are no unread messages') ]]</div>
+                                    </div>
+                                </div>
+                            </template>
                         </div>
 
                     </div>
                     
                     <div v-if="tab_id_active=='allpages'" :class="tab_data_is_show == false ? 'd-none' : ''">
 
                         <!-- list pages -->
                         <div class="wrapper__chatboxes">
-                            <template v-for="(chat, index) in chat_to_all" :key="chat">
+                            <template v-if="chat_to_all.length != 0" v-for="(chat, index) in chat_to_all" :key="chat">
                                 <div class="chat__box" :class="'page3_item_' + index" @click="show_user_chat_page(chat.user_chat_uid, `${chat.first_name} ${chat.last_name}`, `page3_item_${index}`, 'anyone', index)">
                                     <div class="user_date_div">
-                                        <div>[[ chat.first_name ]] [[ chat.last_name ]]</div>
-                                        <div>[[ chat.user_chat_uid.slice(0,3) ]]****[[ chat.user_chat_uid.slice(7) ]]</div>
+                                        <div>[[ (chat.first_name + chat.last_name).slice(0,25) ]]</div>
+                                        <div>[[ chat.user_chat_uid.slice(0,3) ]]****[[ chat.user_chat_uid.slice(7,11) ]]</div>
+                                    </div>
+                                </div>
+                            </template>
+                            <template v-else>
+                                <div class="chat__box">
+                                    <div class="user_date_div no__data">
+                                        <div>[[ $t('There are no Users') ]]</div>
                                     </div>
                                 </div>
                             </template>
                         </div>
 
                     </div>
 
                     <!-- + messages wrapper -->
                     <div class="all__msg__wrapper" :class="show_msg_container == true ? '' : 'd-none'">
 
                         <template v-for="msg_item in message_list" :key="msg_item.id">
                             <div v-if="!msg_item.is_deleted" class="one_msg_wrapper">
 
                                 <ul :id="`msg-menu-bar-${msg_item.id}`" class="msg-menu-bar d-none" :class="msg_item.sender_type == 'supporter' ? 'msg-menu-bar--left' : 'msg-menu-bar--right'">
-                                    <li @click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)"><img src="{% static 'django_chat_app/img/reply.png' %}" alt=""> پاسخ دادن</li>
-                                    <li @click="copy_ready_msg(msg_item.text)"><img src="{% static 'django_chat_app/img/copy.png' %}" alt=""> کپی متن</li>
-                                    <li v-if="edit_user_msg && msg_item.sender_type == 'supporter' && !msg_item.is_edited" @click="edit_message(`chatapp_msg_${msg_item.id}`, msg_item.id)"><img src="{% static 'django_chat_app/img/edit.png' %}" alt=""> ویرایش پیام</li>
-                                    <li v-if="delete_user_msg && msg_item.sender_type == 'supporter'" @click="delete_message(msg_item.id)"><img src="{% static 'django_chat_app/img/delete.png' %}" alt=""> حذف پیام</li>
+                                    <li @click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)"><img src="{% static 'django_chatapp/img/reply.png' %}" alt="reply"> [[ $t('Reply') ]]</li>
+                                    <li @click="copy_ready_msg(msg_item.text)"><img src="{% static 'django_chatapp/img/copy.png' %}" alt="copy"> [[ $t('Copy') ]]</li>
+                                    <li v-if="edit_user_msg && msg_item.sender_type == 'supporter' && !msg_item.is_edited" @click="edit_message(`chatapp_msg_${msg_item.id}`, msg_item.id)"><img src="{% static 'django_chatapp/img/edit.png' %}" alt="edit"> [[ $t('Edit') ]]</li>
+                                    <li v-if="delete_user_msg && msg_item.sender_type == 'supporter'" @click="delete_message(msg_item.id)"><img src="{% static 'django_chatapp/img/delete.png' %}" alt="delete"> [[ $t('Remove') ]]</li>
                                 </ul>
 
                                 <div class="msg" :class="msg_item.sender_type == 'supporter' ? 'msg__right' : 'msg__left'" :id="'chatapp_msg_' + msg_item.id">
                                     <p v-if="msg_item.reply_title" class="msg__replied" :class="msg_item.sender_type == 'supporter' ? 'msg__replied--right' : 'msg__replied--left'" @click="msg_replied(`chatapp_msg_${msg_item.reply_id}`)">
-                                        <span>[[ msg_item.reply_title == 'supporter' ? 'شما' : 'کاربر' ]]</span>
+                                        <span>[[ msg_item.reply_title == 'supporter' ? $t('You') : $t('Client') ]]</span>
                                         <span v-if="!msg_item.reply_is_deleted">[[ msg_item.reply_msg ]]</span>
-                                        <span v-else>این پیام حذف شده است</span>
+                                        <span v-else>[[ $t('This message has been deleted.') ]]</span>
                                     </p>
                                     
                                     <p class="msg__content">
                                         [[ msg_item.text ]]
                                     </p>
                                     <div class="msg__info">
                                         <div class="msg__info__status" v-if="msg_item.sender_type == 'supporter'">
-                                            <img v-if="msg_item.is_seen" src="{% static 'django_chat_app/img/double-check.png' %}" alt="double check status">
-                                            <img v-else src="{% static 'django_chat_app/img/single-check.png' %}" alt="single check status">
+                                            <img v-if="msg_item.is_seen" src="{% static 'django_chatapp/img/double-check.png' %}" alt="double check status">
+                                            <img v-else src="{% static 'django_chatapp/img/single-check.png' %}" alt="single check status">
                                         </div>
                                         <div class="msg__info__clock">[[ msg_item.created ]]</div>
-                                        <div class="msg__info__edited" v-if="msg_item.is_edited">ویرایش شده</div>
+                                        <div class="msg__info__edited" v-if="msg_item.is_edited">[[ $t('edited') ]]</div>
                                     </div>
                                     <div class="reply_one_msg" :class="msg_item.sender_type == 'supporter' ? 'reply_one_msg--right' : 'reply_one_msg--left'">
-                                        <span @click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)">پاسخ دادن</span>
+                                        <span @click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)">[[ $t('reply') ]]</span>
                                         <br><br>
-                                        <span class="toggle_mneubar" @click="show_menu_bar(`msg-menu-bar-${msg_item.id}`)">بیشتر</span>
+                                        <span class="toggle_mneubar" @click="show_menu_bar(`msg-menu-bar-${msg_item.id}`)">[[ $t('more') ]]</span>
                                     </div>
                                 </div>
                             </div>
                             <div v-if="msg_item.is_deleted && show_deleted_msg">
                                 <div class="msg__content deleted_msg"  :class="msg_item.sender_type == 'supporter' ? 'msgdel__right' : 'msgdel__left'">
-                                    <img src="{% static 'django_chat_app/img/delete.png' %}" alt=""> این پیام حذف شده است.
+                                    <img src="{% static 'django_chatapp/img/delete.png' %}" alt="delete"> [[ $t('This message has been deleted.') ]]
                                 </div>
                             </div>
                             <div class="clearfix"></div>
                         </template>
 
                     </div>
                     <!-- - messages wrapper -->
@@ -240,17 +278,17 @@
             <!-- - body -->
 
             <!-- + send msg -->
             <div class="body__inputs d-none">
                 <form novalidate @submit.prevent="sned_msg_socket">
                     <div class="forminput_wrapper">
 
-                        <input type="text" v-model="msg_input" id="text-chatinput" autocomplete="off" placeholder="پیام خود را وارد کنید:">
+                        <input type="text" v-model="msg_input" id="text-chatinput" autocomplete="off" :placeholder="$t('Enter your message:')">
                         <button class="show_emoji" type="button" @click="show_emojibar">
-                            <img src="{% static 'django_chat_app/img/emoji.png' %}" alt="toggle emojis">
+                            <img src="{% static 'django_chatapp/img/emoji.png' %}" alt="toggle emojis">
                         </button>
 
                         <div class="reply_msg_wrapper d-none">
                             <button class="close_replybar" type="button" @click="close_replybar">&times;</button>
                             <div>
                                 <p class="reply__writer"></p>
                                 <p class="reply__content"></p>
@@ -262,120 +300,85 @@
                             <div class="emoji_box">
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F600;')">&#x1F600;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F601;')">&#x1F601;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F602;')">&#x1F602;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F603;')">&#x1F603;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F604;')">&#x1F604;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F605;')">&#x1F605;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F606;')">&#x1F606;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F607;')">&#x1F607;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F608;')">&#x1F608;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F609;')">&#x1F609;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F60A;')">&#x1F60A;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F60B;')">&#x1F60B;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F60C;')">&#x1F60C;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F60D;')">&#x1F60D;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F60E;')">&#x1F60E;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F60F;')">&#x1F60F;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F610;')">&#x1F610;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F611;')">&#x1F611;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F612;')">&#x1F612;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F613;')">&#x1F613;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F614;')">&#x1F614;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F615;')">&#x1F615;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F616;')">&#x1F616;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F617;')">&#x1F617;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F618;')">&#x1F618;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F619;')">&#x1F619;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F61A;')">&#x1F61A;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F61B;')">&#x1F61B;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F61C;')">&#x1F61C;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F61D;')">&#x1F61D;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F61E;')">&#x1F61E;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F61F;')">&#x1F61F;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F620;')">&#x1F620;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F621;')">&#x1F621;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F622;')">&#x1F622;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F623;')">&#x1F623;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F624;')">&#x1F624;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F625;')">&#x1F625;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F626;')">&#x1F626;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F627;')">&#x1F627;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F628;')">&#x1F628;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F629;')">&#x1F629;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F62A;')">&#x1F62A;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F62B;')">&#x1F62B;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F62C;')">&#x1F62C;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F62D;')">&#x1F62D;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F62E;')">&#x1F62E;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F62F;')">&#x1F62F;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F630;')">&#x1F630;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F631;')">&#x1F631;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F632;')">&#x1F632;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F633;')">&#x1F633;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F634;')">&#x1F634;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F635;')">&#x1F635;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F636;')">&#x1F636;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F637;')">&#x1F637;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F641;')">&#x1F641;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F642;')">&#x1F642;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F643;')">&#x1F643;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F644;')">&#x1F644;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F910;')">&#x1F910;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F911;')">&#x1F911;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F912;')">&#x1F912;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F913;')">&#x1F913;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F914;')">&#x1F914;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F915;')">&#x1F915;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F917;')">&#x1F917;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F918;')">&#x1F918;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F919;')">&#x1F919;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F91A;')">&#x1F91A;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F91B;')">&#x1F91B;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F91C;')">&#x1F91C;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F91D;')">&#x1F91D;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F91E;')">&#x1F91E;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F91F;')">&#x1F91F;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F920;')">&#x1F920;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F921;')">&#x1F921;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F922;')">&#x1F922;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F923;')">&#x1F923;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F924;')">&#x1F924;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F925;')">&#x1F925;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F926;')">&#x1F926;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F927;')">&#x1F927;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F928;')">&#x1F928;</div>
                                 <div class="emoji_item" @click="add_emoji_toinput('&#x1F929;')">&#x1F929;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F92A;')">&#x1F92A;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F92B;')">&#x1F92B;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F92C;')">&#x1F92C;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F92D;')">&#x1F92D;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F92E;')">&#x1F92E;</div>
-                                <div class="emoji_item" @click="add_emoji_toinput('&#x1F92F;')">&#x1F92F;</div>
                             </div>
                         </div>
 
                         <button type="submit" class="submit_msg_client">
-                            <img src="{% static 'django_chat_app/img/send.png' %}" alt="send image">
+                            <img src="{% static 'django_chatapp/img/send.png' %}" alt="send image">
                         </button>
                     </div>
                 </form>
 
                 <div class="btn_last_msg d-none" @click="go_to_bottom_of_box">
                     <button @click="go_to_bottom_of_box">
-                        <img src="{% static 'django_chat_app/img/gotodown.png' %}" alt="go to last msg img">
+                        <img src="{% static 'django_chatapp/img/gotodown.png' %}" alt="go to last msg img">
                         <div class="unreadmsg_counter d-none"></div>
                     </button>
                 </div>
 
             </div>
             <!-- - send msg -->
 
         </div>
 
     </section>
 
-    <script type="text/javascript" src="{% static 'django_chat_app/js/vue3.js' %}"></script>
-    <script type="text/javascript" src="{% static 'django_chat_app/js/supporter.js' %}"></script>
+    <script type="text/javascript" src="{% static 'django_chatapp/js/vue3.js' %}"></script>
+    <script type="text/javascript" src="{% static 'django_chatapp/js/vue-i18n.js' %}"></script>
+    <script type="text/javascript" src="{% static 'django_chatapp/js/supporter.js' %}"></script>
 
 </body>
 </html>
```

#### html2text {}

```diff
@@ -1,186 +1,165 @@
-{% load static %}
+{% load static i18n %}
 
 
 
 [[ alert ]]
-{% static 'django_chat_app/media/send.mp3' %}
+{% static 'django_chatapp/song/send.mp3' %}
 {{ supporter_uid }}
-title="client_id.slice(0,5) + '***' + client_id.slice(31)">[[ client_name ]] [
-[ receiver_status == 'online' ? 'Ø¢ÙÙØ§ÛÙ' : 'Ø¢Ø®Ø±ÛÙ Ø¨Ø§Ø²Ø¯ÛØ¯ Ø¨Ù
-ØªØ§Ø²Ú¯Û' ]] Ø¨Ù Ù¾ÙÙ Ù¾Ø´ØªÛØ¨Ø§Ù Ø®ÙØ´ Ø¢ÙØ¯ÛØ¯.
+[supporter image]
+title="client_id.slice(0,3) + '****' + client_id.slice(7,11)">[
+[ client_name.slice(0,35) ]] [[ receiver_status == 'online' ? $t('online') : $t
+('last seen recently') ]] [[ $t('WelCome to Supporter Panel') ]]
+click="change_lang('en')">En
+click="change_lang('fa')">Fa
+click="change_lang('ar')">Ar
+click="change_lang('ru')">Ru
 click="open_report_box">[report user]
 click="openclose_copyreadymsg">[copy msg box]
 click="reset_close_chat_box">[close chat box]
 submit.prevent="send_report">
-[One of: Ø§Ø³ØªÙØ§Ø¯Ù Ø§Ø² Ú©ÙÙØ§Øª ÙØ§ÙÙØ§Ø³Ø¨/Ø¯ÙØ§ÛÙ Ø¯ÛÚ¯Ø±]
-click="send_report">Ø«Ø¨Øª Ú¯Ø²Ø§Ø±Ø´
+[One of: [[ $t('Using inappropriate words') ]]/[[ $t('Others') ]]]
+click="send_report">[[ $t('Send') ]]
 key="ready_msg.id">
 title="ready_msg.content">[[ ready_msg.subject ]]
 click="delete_ready_msg(ready_msg.id)">[delete ready msg item]
 click="msg_input+=ready_msg.content" v-if="client_id">[add to input]
 click="copy_ready_msg(ready_msg.content)">[copy to clipboard]
+[[ $t('There are no ready messages.') ]]
 
 class="tab_id_active == 'menu' ? 'tab_active' : ''" @click="open_tab_data
-('menu')">ØµÙØ­ÙâÛ Ø§ØµÙÛ
+('menu')"> [[ $t('Home') ]]
 class="tab_id_active == 'yourunreads' ? 'tab_active' : ''"
-@click="open_tab_data('yourunreads')">Ù¾ÛØ§ÙâÙØ§Û ÙØ§Ø®ÙØ§ÙØ¯ÙâÛ
-Ø´ÙØ§
+@click="open_tab_data('yourunreads')"> [[ $t('Your unread Messages') ]] [
+[ this_supporter_counter_tab ]]
 class="tab_id_active == 'unreads' ? 'tab_active' : ''" @click="open_tab_data
-('unreads')">Ø³Ø§ÛØ± Ù¾ÛØ§ÙâÙØ§Û ÙØ§Ø®ÙØ§ÙØ¯Ù
+('unreads')"> [[ $t('Other unread Messages') ]] [[ no_supoorter_counter_tab ]]
 class="tab_id_active == 'allpages' ? 'tab_active' : ''" @click="open_tab_data
-('allpages')">Ú©Ø§Ø±Ø¨Ø±Ø§Ù
+('allpages')"> [[ $t('All Users') ]]
 
-click="menu_active_tab = 'addnewmsg'">ÙÙØ´ØªÙ Ù¾ÛØ§Ù Ø¢ÙØ§Ø¯Ù
-submit.prevent="submit_new_readymsg" v-if="menu_active_tab == 'addnewmsg'">
-Ø¹ÙÙØ§Ù ÙØªÙ [                    ]
-Ø°Ø®ÛØ±Ù
+[[ $t('Register a Ready Message') ]]
+submit.prevent="submit_new_readymsg">
+[[ $t('Subject') ]] [                    ]
+[[ $t('Save') ]]
 class="tab_data_is_show == false ? 'd-none' : ''">
 key="msg">
-class="'page1_item_' + index" @click="show_user_chat_page(msg.owner_id,
-msg.owner_name, `page1_item_${index}`, 'thissupporter', index)">
-[[ msg.owner_name ]]
-[[ msg.owner_id.slice(0,3) ]]****[[ msg.owner_id.slice(7) ]] [[ msg.status ==
-'online' ? ' - Ø¢ÙÙØ§ÛÙ' : ' - Ø§Ø®ÛØ±Ø§' ]]
+class="['page1_item_' + index, msg.status == 'online' ? 'border_green' :
+'border_red']" @click="show_user_chat_page(msg.owner_id, msg.owner_name,
+`page1_item_${index}`, 'thissupporter', index)">
+title="msg.owner_id.slice(0,3) + '****' + msg.owner_id.slice(7,11)">[
+[ msg.owner_name.slice(0,25) ]]
+[[ msg.status == 'online' ? $t('online') : $t('last seen recently') ]]
 [[ msg.counter ]]
+
+[[ $t('There are no unread messages for you') ]]
 class="tab_data_is_show == false ? 'd-none' : ''">
 key="msg">
-class="'page2_item_' + index" @click="show_user_chat_page(msg.owner_id,
-msg.owner_name, `page2_item_${index}`, 'nosupoorter', index)">
-[[ msg.owner_name ]]
-[[ msg.owner_id.slice(0,3) ]]****[[ msg.owner_id.slice(7) ]] [[ msg.status ==
-'online' ? ' - Ø¢ÙÙØ§ÛÙ' : ' - Ø§Ø®ÛØ±Ø§' ]]
+class="['page2_item_' + index, msg.status == 'online' ? 'border_green' :
+'border_red']" @click="show_user_chat_page(msg.owner_id, msg.owner_name,
+`page2_item_${index}`, 'nosupoorter', index)">
+title="msg.owner_id.slice(0,3) + '****' + msg.owner_id.slice(7,11)">[
+[ msg.owner_name.slice(0,25)]]
+[[ msg.status == 'online' ? $t('online') : $t('last seen recently') ]]
 [[ msg.counter ]]
+
+[[ $t('There are no unread messages') ]]
 class="tab_data_is_show == false ? 'd-none' : ''">
 key="chat">
 class="'page3_item_' + index" @click="show_user_chat_page(chat.user_chat_uid,
 `${chat.first_name} ${chat.last_name}`, `page3_item_${index}`, 'anyone',
 index)">
-[[ chat.first_name ]] [[ chat.last_name ]]
-[[ chat.user_chat_uid.slice(0,3) ]]****[[ chat.user_chat_uid.slice(7) ]]
+[[ (chat.first_name + chat.last_name).slice(0,25) ]]
+[[ chat.user_chat_uid.slice(0,3) ]]****[[ chat.user_chat_uid.slice(7,11) ]]
+
+[[ $t('There are no Users') ]]
 
 class="show_msg_container == true ? '' : 'd-none'">
 key="msg_item.id">
 id="`msg-menu-bar-${msg_item.id}`" class="msg-menu-bar d-none" :
 class="msg_item.sender_type == 'supporter' ? 'msg-menu-bar--left' : 'msg-menu-
 bar--right'">
-click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)"> Ù¾Ø§Ø³Ø® Ø¯Ø§Ø¯Ù
-click="copy_ready_msg(msg_item.text)"> Ú©Ù¾Û ÙØªÙ
-click="edit_message(`chatapp_msg_${msg_item.id}`, msg_item.id)"> ÙÛØ±Ø§ÛØ´
-Ù¾ÛØ§Ù
-click="delete_message(msg_item.id)"> Ø­Ø°Ù Ù¾ÛØ§Ù
+click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)">[reply] [[ $t
+('Reply') ]]
+click="copy_ready_msg(msg_item.text)">[copy] [[ $t('Copy') ]]
+click="edit_message(`chatapp_msg_${msg_item.id}`, msg_item.id)">[edit] [[ $t
+('Edit') ]]
+click="delete_message(msg_item.id)">[delete] [[ $t('Remove') ]]
 class="msg_item.sender_type == 'supporter' ? 'msg__right' : 'msg__left'" :
 id="'chatapp_msg_' + msg_item.id">
 class="msg_item.sender_type == 'supporter' ? 'msg__replied--right' :
 'msg__replied--left'" @click="msg_replied(`chatapp_msg_${msg_item.reply_id}`)">
-[[ msg_item.reply_title == 'supporter' ? 'Ø´ÙØ§' : 'Ú©Ø§Ø±Ø¨Ø±' ]] [
-[ msg_item.reply_msg ]] Ø§ÛÙ Ù¾ÛØ§Ù Ø­Ø°Ù Ø´Ø¯Ù Ø§Ø³Øª
+[[ msg_item.reply_title == 'supporter' ? $t('You') : $t('Client') ]] [
+[ msg_item.reply_msg ]] [[ $t('This message has been deleted.') ]]
 [[ msg_item.text ]]
 [double check status] [single check status]
 [[ msg_item.created ]]
-ÙÛØ±Ø§ÛØ´ Ø´Ø¯Ù
+[[ $t('edited') ]]
 class="msg_item.sender_type == 'supporter' ? 'reply_one_msg--right' :
 'reply_one_msg--left'">
-click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)">Ù¾Ø§Ø³Ø® Ø¯Ø§Ø¯Ù
+click="reply_msg(`chatapp_msg_${msg_item.id}`, msg_item.id)">[[ $t('reply') ]]
 
-click="show_menu_bar(`msg-menu-bar-${msg_item.id}`)">Ø¨ÛØ´ØªØ±
+click="show_menu_bar(`msg-menu-bar-${msg_item.id}`)">[[ $t('more') ]]
 class="msg_item.sender_type == 'supporter' ? 'msgdel__right' : 'msgdel__left'">
-Ø§ÛÙ Ù¾ÛØ§Ù Ø­Ø°Ù Ø´Ø¯Ù Ø§Ø³Øª.
+[delete] [[ $t('This message has been deleted.') ]]
 
 submit.prevent="sned_msg_socket">
-[                    ]
+placeholder="$t('Enter your message:')">
 click="show_emojibar"> [toggle emojis]
 click="close_replybar">×
 click="add_emoji_toinput('&#x1F600;')">&#x1F600;
 click="add_emoji_toinput('&#x1F601;')">&#x1F601;
 click="add_emoji_toinput('&#x1F602;')">&#x1F602;
 click="add_emoji_toinput('&#x1F603;')">&#x1F603;
 click="add_emoji_toinput('&#x1F604;')">&#x1F604;
 click="add_emoji_toinput('&#x1F605;')">&#x1F605;
-click="add_emoji_toinput('&#x1F606;')">&#x1F606;
 click="add_emoji_toinput('&#x1F607;')">&#x1F607;
-click="add_emoji_toinput('&#x1F608;')">&#x1F608;
-click="add_emoji_toinput('&#x1F609;')">&#x1F609;
-click="add_emoji_toinput('&#x1F60A;')">&#x1F60A;
 click="add_emoji_toinput('&#x1F60B;')">&#x1F60B;
 click="add_emoji_toinput('&#x1F60C;')">&#x1F60C;
 click="add_emoji_toinput('&#x1F60D;')">&#x1F60D;
 click="add_emoji_toinput('&#x1F60E;')">&#x1F60E;
 click="add_emoji_toinput('&#x1F60F;')">&#x1F60F;
 click="add_emoji_toinput('&#x1F610;')">&#x1F610;
 click="add_emoji_toinput('&#x1F611;')">&#x1F611;
 click="add_emoji_toinput('&#x1F612;')">&#x1F612;
 click="add_emoji_toinput('&#x1F613;')">&#x1F613;
-click="add_emoji_toinput('&#x1F614;')">&#x1F614;
-click="add_emoji_toinput('&#x1F615;')">&#x1F615;
-click="add_emoji_toinput('&#x1F616;')">&#x1F616;
-click="add_emoji_toinput('&#x1F617;')">&#x1F617;
 click="add_emoji_toinput('&#x1F618;')">&#x1F618;
-click="add_emoji_toinput('&#x1F619;')">&#x1F619;
-click="add_emoji_toinput('&#x1F61A;')">&#x1F61A;
-click="add_emoji_toinput('&#x1F61B;')">&#x1F61B;
 click="add_emoji_toinput('&#x1F61C;')">&#x1F61C;
-click="add_emoji_toinput('&#x1F61D;')">&#x1F61D;
-click="add_emoji_toinput('&#x1F61E;')">&#x1F61E;
-click="add_emoji_toinput('&#x1F61F;')">&#x1F61F;
-click="add_emoji_toinput('&#x1F620;')">&#x1F620;
 click="add_emoji_toinput('&#x1F621;')">&#x1F621;
 click="add_emoji_toinput('&#x1F622;')">&#x1F622;
-click="add_emoji_toinput('&#x1F623;')">&#x1F623;
 click="add_emoji_toinput('&#x1F624;')">&#x1F624;
 click="add_emoji_toinput('&#x1F625;')">&#x1F625;
-click="add_emoji_toinput('&#x1F626;')">&#x1F626;
 click="add_emoji_toinput('&#x1F627;')">&#x1F627;
 click="add_emoji_toinput('&#x1F628;')">&#x1F628;
 click="add_emoji_toinput('&#x1F629;')">&#x1F629;
 click="add_emoji_toinput('&#x1F62A;')">&#x1F62A;
-click="add_emoji_toinput('&#x1F62B;')">&#x1F62B;
 click="add_emoji_toinput('&#x1F62C;')">&#x1F62C;
 click="add_emoji_toinput('&#x1F62D;')">&#x1F62D;
 click="add_emoji_toinput('&#x1F62E;')">&#x1F62E;
-click="add_emoji_toinput('&#x1F62F;')">&#x1F62F;
 click="add_emoji_toinput('&#x1F630;')">&#x1F630;
 click="add_emoji_toinput('&#x1F631;')">&#x1F631;
 click="add_emoji_toinput('&#x1F632;')">&#x1F632;
 click="add_emoji_toinput('&#x1F633;')">&#x1F633;
 click="add_emoji_toinput('&#x1F634;')">&#x1F634;
-click="add_emoji_toinput('&#x1F635;')">&#x1F635;
 click="add_emoji_toinput('&#x1F636;')">&#x1F636;
 click="add_emoji_toinput('&#x1F637;')">&#x1F637;
 click="add_emoji_toinput('&#x1F641;')">&#x1F641;
 click="add_emoji_toinput('&#x1F642;')">&#x1F642;
 click="add_emoji_toinput('&#x1F643;')">&#x1F643;
 click="add_emoji_toinput('&#x1F644;')">&#x1F644;
 click="add_emoji_toinput('&#x1F910;')">&#x1F910;
 click="add_emoji_toinput('&#x1F911;')">&#x1F911;
 click="add_emoji_toinput('&#x1F912;')">&#x1F912;
 click="add_emoji_toinput('&#x1F913;')">&#x1F913;
 click="add_emoji_toinput('&#x1F914;')">&#x1F914;
 click="add_emoji_toinput('&#x1F915;')">&#x1F915;
 click="add_emoji_toinput('&#x1F917;')">&#x1F917;
-click="add_emoji_toinput('&#x1F918;')">&#x1F918;
-click="add_emoji_toinput('&#x1F919;')">&#x1F919;
 click="add_emoji_toinput('&#x1F91A;')">&#x1F91A;
-click="add_emoji_toinput('&#x1F91B;')">&#x1F91B;
-click="add_emoji_toinput('&#x1F91C;')">&#x1F91C;
 click="add_emoji_toinput('&#x1F91D;')">&#x1F91D;
 click="add_emoji_toinput('&#x1F91E;')">&#x1F91E;
 click="add_emoji_toinput('&#x1F91F;')">&#x1F91F;
-click="add_emoji_toinput('&#x1F920;')">&#x1F920;
-click="add_emoji_toinput('&#x1F921;')">&#x1F921;
-click="add_emoji_toinput('&#x1F922;')">&#x1F922;
 click="add_emoji_toinput('&#x1F923;')">&#x1F923;
-click="add_emoji_toinput('&#x1F924;')">&#x1F924;
-click="add_emoji_toinput('&#x1F925;')">&#x1F925;
 click="add_emoji_toinput('&#x1F926;')">&#x1F926;
-click="add_emoji_toinput('&#x1F927;')">&#x1F927;
 click="add_emoji_toinput('&#x1F928;')">&#x1F928;
 click="add_emoji_toinput('&#x1F929;')">&#x1F929;
-click="add_emoji_toinput('&#x1F92A;')">&#x1F92A;
-click="add_emoji_toinput('&#x1F92B;')">&#x1F92B;
-click="add_emoji_toinput('&#x1F92C;')">&#x1F92C;
-click="add_emoji_toinput('&#x1F92D;')">&#x1F92D;
-click="add_emoji_toinput('&#x1F92E;')">&#x1F92E;
-click="add_emoji_toinput('&#x1F92F;')">&#x1F92F;
  [send image]
 click="go_to_bottom_of_box">
 click="go_to_bottom_of_box"> [go to last msg img]
```

### Comparing `django-chatapp-1.3/chatapp/views.py` & `django-chatapp-1.4/chatapp/views.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,141 +1,126 @@
+from django.db.models import Q
 from django.conf import settings
 from django.contrib.auth.decorators import login_required
 from django.views.decorators.csrf import csrf_exempt
 from django.http import JsonResponse, HttpResponse
-from django.utils import timezone
-from django.shortcuts import render
+from django.shortcuts import render, get_object_or_404, redirect
+from .utils import get_hour_min, get_settings
 from .models import (
     SupporterModel,
     UserChatModel,
     ChatModel,
     ReadyChatModel,
     ReportUserModel
 )
 
 
-# url: / 
-def home(request):
-    return render(request, 'test.html')
+def ready_message_list(supporter) -> list:
+    """ get list of ready message of a supporter """
+
+    lookup = Q(supporter=supporter) | Q(is_public=True)
+    ready_chats = ReadyChatModel.objects.filter(lookup).all()
+
+    msgs_list = list(ready_chats.values(
+        'id', 'subject', 'content', 'supporter__supporter_uid', 'is_public'
+    ))
+    return msgs_list
+
+
+# url: /django-chatapp/chat/supporter/login-required/
+def loginrequired_page(request):
+    """ go to supporter login page OR show h3 html tag """
+
+    try:
+        login_url = settings.CHATAPP_SUPPORTER_LOGIN_URL
+        return redirect(login_url)
+    except:
+        login_url = None
+        return HttpResponse('<h3>Login Required.</h3>')
 
 
 # url: /django-chatapp/auth/check/userid/
 @csrf_exempt
 def check_userid(request):
+    """ 
+    - send chat settings
+    - check userID and send messages to her chat app 
+    - seen messages of supporter via this user 
+    """
+
     if request.method == 'POST':
 
         userid = request.POST.get('user_id')
         
         # send 10 msg from db to client
-        if userid and UserChatModel.objects.filter(user_chat_uid=userid, is_blocked=False).exists():
-
-            setting_dict = {}
-            
-            try:
-                setting_dict['dir'] = settings.CHATAPP_DIR
-            except:
-                setting_dict['dir'] = 'rtl'
-            
-            try:
-                setting_dict['title'] = settings.CHATAPP_TITLE
-            except:
-                setting_dict['title'] = 'وبسایت تستی'
-            
-            try:
-                setting_dict['subtitle'] = settings.CHATAPP_SUBTITLE
-            except:
-                setting_dict['subtitle'] = 'لطفا کوشا باشید.'
-            
-            try:
-                setting_dict['game'] = settings.CHATAPP_GAME
-            except:
-                setting_dict['game'] = True
-            
-            try:
-                setting_dict['auth_fields'] = settings.CHATAPP_AUTHFIELDS
-            except:
-                setting_dict['auth_fields'] = 'email'
+        if userid and UserChatModel.objects.filter(
+            user_chat_uid=userid, 
+            is_blocked=False
+        ).exists():
             
             try:
-                setting_dict['max_report_number'] = settings.CHATAPP_MAX_REPORT_NUMBER
+                msg_counter = settings.CHATAPP_MESSAGES_COUNT
             except:
-                setting_dict['max_report_number'] = 2
-            
-            try:
-                setting_dict['edit_user_msg'] = settings.CHATAPP_EDIT_USER_MESSAGE
-            except:
-                setting_dict['edit_user_msg'] = True
-            
-            try:
-                setting_dict['edit_supporter_msg'] = settings.CHATAPP_EDIT_SUPPORTER_MESSAGE
-            except:
-                setting_dict['edit_supporter_msg'] = True
-            
-            try:
-                setting_dict['delete_user_msg'] = settings.CHATAPP_DELETE_USER_MESSAGE
-            except:
-                setting_dict['delete_user_msg'] = True
-            
-            try:
-                setting_dict['delete_supporter_msg'] = settings.CHATAPP_DELETE_SUPPORTER_MESSAGE
-            except:
-                setting_dict['delete_supporter_msg'] = True
-            
-            try:
-                setting_dict['show_deleted_msg'] = settings.CHATAPP_SHOW_DELETED_MESSAGE
-            except:
-                setting_dict['show_deleted_msg'] = True
-
-            client = UserChatModel.objects.get(user_chat_uid=userid, is_blocked=False)
+                msg_counter = 30
 
-            chats = ChatModel.objects.filter(client=client).all()[:15]
+            client = UserChatModel.objects.get(
+                user_chat_uid=userid, 
+                is_blocked=False
+            )
+            chats = ChatModel.objects.filter(client=client).all()[:msg_counter]
             chats_arr = []
 
             for item in chats:
-
                 obj = {
                     'id': item.id,
                     'owner_id': item.supporter.supporter_uid if item.sender == 'supporter' else item.client.user_chat_uid,
                     'owner_name': 'supporter' if item.sender == 'supporter' else f'{item.client.first_name} {item.client.last_name}',
                     'sender_type': item.sender,
                     'reply_id': item.reply.id if item.reply else '',
                     'reply_title': item.reply.sender if item.reply else '',
                     'reply_msg': item.reply.msg if item.reply else '',
                     'reply_is_deleted': True if item.reply and item.reply.is_deleted else False,
                     'is_seen': item.is_seen,
                     'is_edited': item.is_edited,
                     'is_deleted': item.is_deleted,
-                    'created': f'{timezone.localtime(item.created).hour}:{timezone.localtime(item.created).minute}',
+                    'created': get_hour_min(item.created),
                     'text': item.msg
                 }
                 chats_arr.append(obj)
 
             # update the unread messages
             ChatModel.objects.filter(
                 sender='supporter',
                 is_seen=False,
                 client=client
             ).update(is_seen=True)
 
             chats_arr.reverse()
 
-            return JsonResponse({'data': chats_arr, 'setting': setting_dict, 'status': 200})
+            return JsonResponse({
+                'data': chats_arr, 
+                'setting': get_settings(), 
+                'status': 200
+            })
+        
         return JsonResponse({'status': 401})
     return JsonResponse({'status': 400})
 
 
 # url: /django-chatapp/auth/create/userid/
 @csrf_exempt
 def create_userid(request):
-    if request.method == 'POST':
+    """ create a user with fname, lname, email or phone. this is client login from! """
 
+    if request.method == 'POST':
         fname = request.POST.get('fname')
         lname = request.POST.get('lname')
-        email = ''
-        phone = ''
+        email = str()
+        phone = str()
+
         if request.POST.get('email'):
             email = request.POST.get('email')
         elif request.POST.get('phone'):
             phone = request.POST.get('phone')
 
         user_chat_model = UserChatModel(
             first_name=fname,
@@ -145,111 +130,72 @@
         if email:
             user_chat_model.email = email
         elif phone:
             user_chat_model.phone = phone
 
         user_chat_model.save()
 
-        return JsonResponse({'data': user_chat_model.user_chat_uid, 'status': 200})
+        return JsonResponse({
+            'data': user_chat_model.user_chat_uid, 
+            'status': 200
+        })
+    
     return JsonResponse({'status': 400})
 
 
 # url: /django-chatapp/chat/setting/
 @csrf_exempt
 def setting_chat(request):
-    if request.method == 'POST':
-
-        setting_dict = {}
-
-        try:
-            setting_dict['dir'] = settings.CHATAPP_DIR
-        except:
-            setting_dict['dir'] = 'rtl'
-
-        try:
-            setting_dict['title'] = settings.CHATAPP_TITLE
-        except:
-            setting_dict['title'] = 'وبسایت تستی'
-        
-        try:
-            setting_dict['subtitle'] = settings.CHATAPP_SUBTITLE
-        except:
-            setting_dict['subtitle'] = 'لطفا کوشا باشید.'
-        
-        try:
-            setting_dict['game'] = settings.CHATAPP_GAME
-        except:
-            setting_dict['game'] = True
-        
-        try:
-            setting_dict['auth_fields'] = settings.CHATAPP_AUTHFIELDS
-        except:
-            setting_dict['auth_fields'] = 'email'
-        
-        try:
-            setting_dict['max_report_number'] = settings.CHATAPP_MAX_REPORT_NUMBER
-        except:
-            setting_dict['max_report_number'] = 2
-        
-        try:
-            setting_dict['edit_user_msg'] = settings.CHATAPP_EDIT_USER_MESSAGE
-        except:
-            setting_dict['edit_user_msg'] = True
-        
-        try:
-            setting_dict['edit_supporter_msg'] = settings.CHATAPP_EDIT_SUPPORTER_MESSAGE
-        except:
-            setting_dict['edit_supporter_msg'] = True
-        
-        try:
-            setting_dict['delete_user_msg'] = settings.CHATAPP_DELETE_USER_MESSAGE
-        except:
-            setting_dict['delete_user_msg'] = True
-        
-        try:
-            setting_dict['delete_supporter_msg'] = settings.CHATAPP_DELETE_SUPPORTER_MESSAGE
-        except:
-            setting_dict['delete_supporter_msg'] = True
-        
-        try:
-            setting_dict['show_deleted_msg'] = settings.CHATAPP_SHOW_DELETED_MESSAGE
-        except:
-            setting_dict['show_deleted_msg'] = True
-
-
-        return JsonResponse({'data': setting_dict, 'status': 200})
+    """ send chat settings """
 
+    if request.method == 'POST':
+        return JsonResponse({
+            'data': get_settings(), 
+            'status': 200
+        })
+    
     return JsonResponse({'status': 400})
 
 
 # url: /django-chatapp/chat/supporter/
-@login_required
+@login_required(login_url='chatapp:login-required')
 def supporter_homepage(request):
+    """ check supporter in db and show panel """
 
-    if SupporterModel.objects.filter(user__username=request.user.username, is_active=True).exists():
-        
-        supporter_uid = SupporterModel.objects.get(user=request.user, is_active=True)
-
+    try:
+        supporter_uid = SupporterModel.objects.get(
+            user=request.user, 
+            is_active=True
+        )
         return render(request, 'supporter.html', {
             'supporter_uid': supporter_uid.supporter_uid
         })
-    return HttpResponse('You are not a supporter!')
-    
+    except:
+        return HttpResponse('<h3>You are not a supporter!</h3>')
+
 
 # url: /django-chatapp/chat/supporter/unreads/
-@login_required
+@login_required(login_url='chatapp:login-required')
 @csrf_exempt
 def supporter_unreads(request):
+    """ 
+    send unread messages for this supporter
+    send unread messages that do not have supporter
+    send all clients 
+    """
     
     if request.method == 'POST':
 
         supporter_uid = request.POST.get('supporter_uid')
         
-        if not SupporterModel.objects.filter(supporter_uid=supporter_uid, is_active=True).exists():
-            return HttpResponse('You are not a supporter!')
+        if not supporter_uid or not SupporterModel.objects.filter(
+            supporter_uid=supporter_uid, 
+            is_active=True
+        ).exists():
+            return HttpResponse('<h3>You are not a supporter!</h3>')
         
         chats__nosupporter = ChatModel.objects.filter(
             sender='client',
             is_seen=False,
             supporter=None
         ).order_by('id')
 
@@ -272,15 +218,15 @@
                 'reply_id': item.reply.id if item.reply else '',
                 'reply_title': item.reply.sender if item.reply else '',
                 'reply_is_deleted': True if item.reply and item.reply.is_deleted else False,
                 'reply_msg': item.reply.msg if item.reply else '',
                 'is_seen': item.is_seen,
                 'is_edited': item.is_edited,
                 'is_deleted': item.is_deleted,
-                'created': f'{timezone.localtime(item.created).hour}:{timezone.localtime(item.created).minute}',
+                'created': get_hour_min(item.created),
                 'text': item.msg
             }
             unreads_nosupoorter.append(obj)
 
         for item in chats__thissupporter:
 
             obj = {
@@ -291,66 +237,77 @@
                 'reply_id': item.reply.id if item.reply else '',
                 'reply_title': item.reply.sender if item.reply else '',
                 'reply_is_deleted': True if item.reply and item.reply.is_deleted else False,
                 'reply_msg': item.reply.msg if item.reply else '',
                 'is_seen': item.is_seen,
                 'is_edited': item.is_edited,
                 'is_deleted': item.is_deleted,
-                'created': f'{timezone.localtime(item.created).hour}:{timezone.localtime(item.created).minute}',
+                'created': get_hour_min(item.created),
                 'text': item.msg
             }
             unreads_thissupporter.append(obj)
 
         chat_to_all = list(
             UserChatModel.objects.filter(
-                is_blocked=False #TODO add filter: return users who actived just in 30 days ago
+                is_blocked=False
             ).values(
                 'user_chat_uid', 'first_name', 'last_name'
             )
         )
 
         return JsonResponse({
             'unreads_nosupoorter': unreads_nosupoorter, 
             'unreads_thissupporter': unreads_thissupporter, 
             'chat_to_all': chat_to_all,
             'status': 200
         })
+
     return JsonResponse({'status': 400})
 
 
 # url: /django-chatapp/chat/supporter/read-all/
-@login_required
+@login_required(login_url='chatapp:login-required')
 @csrf_exempt
 def supporter_read_all(request):
+    """ 
+    send chats between client and supporter
+    set supporter for client
+    seen messages of client for this supporter
+    """
+
     if request.method == 'POST':
 
         supporter_uid = request.POST.get('supporter_uid')
         client_id= request.POST.get('client_id')
         msg_type= request.POST.get('msg_type')
         
-        if not client_id or not msg_type or not SupporterModel.objects.filter(supporter_uid=supporter_uid, is_active=True).exists():
-            return HttpResponse('You are not a supporter!')
+        if not client_id or not msg_type or not SupporterModel.objects.filter(
+            supporter_uid=supporter_uid, 
+            is_active=True
+        ).exists():
+            return HttpResponse('<h3>You are not a supporter!</h3>')
         
         supporter = SupporterModel.objects.get(user=request.user, is_active=True)
         client = UserChatModel.objects.get(user_chat_uid=client_id, is_blocked=False)
         
         if msg_type == 'thissupporter':
 
             # update the unread messages
             ChatModel.objects.filter(
                 sender='client',
                 is_seen=False,
                 supporter=supporter,
                 client=client
-            ).update(is_seen=True)
-    
+            ).update(
+                is_seen=True
+            )
     
         elif msg_type == 'nosupoorter':
 
-            # add supporter to client
+            # add supporter for this client
             UserChatModel.objects.filter(
                 user_chat_uid=client_id,
                 have_supporter=None
             ).update(
                 have_supporter=supporter
             )
 
@@ -361,18 +318,23 @@
                 client=client,
                 supporter=None
             ).update(
                 supporter=supporter,
                 is_seen=True
             )
 
+        try:
+            msg_counter = settings.CHATAPP_MESSAGES_COUNT
+        except:
+            msg_counter = 30
+
         chats = ChatModel.objects.filter(
             supporter=supporter,
             client=client
-        ).all()[:15]
+        ).all()[:msg_counter]
         chats_arr = []
 
         for item in chats:
 
             obj = {
                 'id': item.id,
                 'owner_id': item.supporter.supporter_uid if item.sender == 'supporter' else item.client.user_chat_uid,
@@ -381,115 +343,151 @@
                 'reply_id': item.reply.id if item.reply else '',
                 'reply_title': item.reply.sender if item.reply else '',
                 'reply_is_deleted': True if item.reply and item.reply.is_deleted else False,
                 'reply_msg': item.reply.msg if item.reply else '',
                 'is_seen': item.is_seen,
                 'is_edited': item.is_edited,
                 'is_deleted': item.is_deleted,
-                'created': f'{timezone.localtime(item.created).hour}:{timezone.localtime(item.created).minute}',
+                'created': get_hour_min(item.created),
                 'text': item.msg
             }
             chats_arr.append(obj)
         
         chats_arr.reverse()
 
-        return JsonResponse({'data': chats_arr, 'status': 200})
+        return JsonResponse({
+            'data': chats_arr, 
+            'status': 200
+        })
     
     return JsonResponse({'status': 400})
 
 
 # url: /django-chatapp/chat/supporter/report/
-@login_required
+@login_required(login_url='chatapp:login-required')
 @csrf_exempt
 def report_user(request):
+    """ report a client via supporter """
+
     if request.method == 'POST':
+
         supporter_uid = request.POST.get('supporter_uid')
         client_id = request.POST.get('client_id')
         report_cause = request.POST.get('report_cause')
         report_item = request.POST.get('report_item')
-
+    
         if supporter_uid and client_id and report_cause and report_item:
-            if UserChatModel.objects.filter(user_chat_uid=client_id).exists():
-                user = UserChatModel.objects.get(user_chat_uid=client_id)
 
-                ReportUserModel.objects.create(
-                    supporter=SupporterModel.objects.get(supporter_uid=supporter_uid),
-                    user=user,
-                    item=report_item,
-                    desc=report_cause
-                )
+            user = get_object_or_404(UserChatModel, user_chat_uid=client_id)
+            supporter = get_object_or_404(SupporterModel, supporter_uid=supporter_uid, is_active=True)
 
-                user.report_numbers = user.report_numbers + 1
-                user.save()
+            ReportUserModel.objects.create(
+                supporter=supporter,
+                user=user,
+                item=report_item,
+                desc=report_cause
+            )
 
-                if user.report_numbers == settings.CHATAPP_MAX_REPORT_NUMBER:
-                    user.is_blocked = True
-                    user.save()
-                    return JsonResponse({'status': 200, 'is_blocked': True})
-                return JsonResponse({'status': 200, 'is_blocked': False})
+            user.report_numbers = user.report_numbers + 1
+            user.save()
+
+            try:
+                max_report_num = settings.CHATAPP_MAX_REPORT_NUMBER
+            except:
+                max_report_num = 2
+
+            if user.report_numbers == int(max_report_num):
+                user.is_blocked = True
+                user.save()
+                return JsonResponse({
+                    'status': 200, 
+                    'is_blocked': True
+                })
+            
+            return JsonResponse({'status': 200, 'is_blocked': False})
+        
         return JsonResponse({'status': 400}) 
     return JsonResponse({'status': 400}) 
                 
 
 # url: /django-chatapp/chat/supporter/ready-msg/get/
-@login_required
+@login_required(login_url='chatapp:login-required')
 @csrf_exempt
 def get_ready_msg(request):
-    if request.method == 'POST':
+    """ send list of ready message to supporter panel """
 
-        supporter_uid = request.POST.get('supporter_uid')
+    if request.method == 'POST':
         
-        if not SupporterModel.objects.filter(supporter_uid=supporter_uid, is_active=True).exists():
-            return HttpResponse('You are not a supporter!')
+        try:
+            supporter_uid = request.POST.get('supporter_uid')
+            supporter = SupporterModel.objects.get(supporter_uid=supporter_uid, is_active=True)
+        except:
+            return HttpResponse('<h3>You are not a supporter!</h3>')
 
-        ready_chats = ReadyChatModel.objects.all()
-        ready_chats_obj = list(ready_chats.values(
-            'id', 'subject', 'content', 'supporter__supporter_uid', 'is_public'
-        ))
-        return JsonResponse({'data': ready_chats_obj, 'status': 200})
+        return JsonResponse({
+            'data': ready_message_list(supporter=supporter), 
+            'status': 200
+        })
     return JsonResponse({'status': 400}) 
 
             
 # url: /django-chatapp/chat/supporter/ready-msg/del/
-@login_required
+@login_required(login_url='chatapp:login-required')
 @csrf_exempt
 def delete_ready_msg(request):
+    """ 
+    delete ready message of supporter and 
+    send list of ready message to supporter panel 
+    """
+
     if request.method == 'POST':
 
-        supporter_uid = request.POST.get('supporter_uid')
-        
-        if not SupporterModel.objects.filter(supporter_uid=supporter_uid, is_active=True).exists():
-            return HttpResponse('You are not a supporter!')
+        try:
+            supporter_uid = request.POST.get('supporter_uid')
+            supporter = SupporterModel.objects.get(supporter_uid=supporter_uid, is_active=True)
+        except:
+            return HttpResponse('<h3>You are not a supporter!</h3>')
 
-        # delete msg
+        # delete ready message of supporter
         ReadyChatModel.objects.get(
-            id=request.POST.get('msgID')
+            id=request.POST.get('msgID'),
+            supporter=supporter
         ).delete()
 
-        ready_chats = ReadyChatModel.objects.all()
-        ready_chats_obj = list(ready_chats.values(
-            'id', 'subject', 'content', 'supporter__supporter_uid', 'is_public'
-        ))
-        return JsonResponse({'data': ready_chats_obj, 'status': 200})
+        return JsonResponse({
+            'data': ready_message_list(supporter=supporter), 
+            'status': 200
+        })
     return JsonResponse({'status': 400}) 
 
 
 # url: /django-chatapp/chat/supporter/ready-msg/create/
-@login_required
+@login_required(login_url='chatapp:login-required')
 @csrf_exempt
 def create_ready_msg(request):
-    if request.method == 'POST':
+    """ 
+    create a ready message via supporter and 
+    send list of ready message to supporter panel 
+    """
 
-        supporter_uid = request.POST.get('supporter_uid')
-        
-        if not SupporterModel.objects.filter(supporter_uid=supporter_uid, is_active=True).exists():
-            return HttpResponse('You are not a supporter!')
+    if request.method == 'POST':
 
-        new_msg = ReadyChatModel.objects.create(
-            subject=request.POST.get('subject'),
-            content=request.POST.get('content'),
-            supporter=SupporterModel.objects.get(supporter_uid=supporter_uid)
+        try:
+            subject = request.POST.get('subject')
+            content = request.POST.get('content')
+            supporter_uid = request.POST.get('supporter_uid')
+            supporter = SupporterModel.objects.get(supporter_uid=supporter_uid, is_active=True)
+        except:
+            return HttpResponse('<h3>You are not a supporter!</h3>')
+
+        ReadyChatModel.objects.create(
+            subject=subject,
+            content=content,
+            supporter=supporter
         )
-        all_msg = ReadyChatModel.objects.all().values('id', 'subject', 'content', 'supporter__supporter_uid', 'is_public')
 
-        return JsonResponse({'data': list(all_msg), 'status': 200})
-    return JsonResponse({'status': 400}) 
+        return JsonResponse({
+            'data': ready_message_list(supporter=supporter), 
+            'status': 200
+        })
+    return JsonResponse({'status': 400}) 
+
```

#### encoding

```diff
@@ -1 +1 @@
-utf-8
+us-ascii
```

### Comparing `django-chatapp-1.3/django_chatapp.egg-info/SOURCES.txt` & `django-chatapp-1.4/django_chatapp.egg-info/SOURCES.txt`

 * *Files 17% similar despite different names*

```diff
@@ -1,53 +1,52 @@
 LICENSE
 MANIFEST.in
 README.md
-pyproject.toml
 setup.cfg
 setup.py
 chatapp/__init__.py
 chatapp/admin.py
 chatapp/apps.py
 chatapp/consumers.py
-chatapp/jalali.py
 chatapp/models.py
 chatapp/routing.py
-chatapp/tests.py
 chatapp/urls.py
 chatapp/utils.py
 chatapp/views.py
 chatapp/migrations/0001_initial.py
 chatapp/migrations/__init__.py
-chatapp/static/django_chat_app/css/custom.css
-chatapp/static/django_chat_app/css/custom.scss
-chatapp/static/django_chat_app/css/supporter.css
-chatapp/static/django_chat_app/css/supporter.scss
-chatapp/static/django_chat_app/font/vazir-medium.ttf
-chatapp/static/django_chat_app/font/vazir-medium.woff
-chatapp/static/django_chat_app/img/chat-room.png
-chatapp/static/django_chat_app/img/close.png
-chatapp/static/django_chat_app/img/copy.png
-chatapp/static/django_chat_app/img/delete.png
-chatapp/static/django_chat_app/img/double-check.png
-chatapp/static/django_chat_app/img/edit.png
-chatapp/static/django_chat_app/img/emoji.png
-chatapp/static/django_chat_app/img/game.png
-chatapp/static/django_chat_app/img/gotodown.png
-chatapp/static/django_chat_app/img/loader.png
-chatapp/static/django_chat_app/img/o.png
-chatapp/static/django_chat_app/img/plus.png
-chatapp/static/django_chat_app/img/reply.png
-chatapp/static/django_chat_app/img/report.png
-chatapp/static/django_chat_app/img/send.png
-chatapp/static/django_chat_app/img/single-check.png
-chatapp/static/django_chat_app/img/supporter.png
-chatapp/static/django_chat_app/img/x.png
-chatapp/static/django_chat_app/js/client.js
-chatapp/static/django_chat_app/js/supporter.js
-chatapp/static/django_chat_app/js/vue3.js
+chatapp/static/django_chatapp/css/client.css
+chatapp/static/django_chatapp/css/client.scss
+chatapp/static/django_chatapp/css/supporter.css
+chatapp/static/django_chatapp/css/supporter.scss
+chatapp/static/django_chatapp/font/vazir-medium.ttf
+chatapp/static/django_chatapp/font/vazir-medium.woff
+chatapp/static/django_chatapp/img/chat-room.png
+chatapp/static/django_chatapp/img/close.png
+chatapp/static/django_chatapp/img/copy.png
+chatapp/static/django_chatapp/img/delete.png
+chatapp/static/django_chatapp/img/double-check.png
+chatapp/static/django_chatapp/img/edit.png
+chatapp/static/django_chatapp/img/emoji.png
+chatapp/static/django_chatapp/img/game.png
+chatapp/static/django_chatapp/img/gotodown.png
+chatapp/static/django_chatapp/img/loader.png
+chatapp/static/django_chatapp/img/o.png
+chatapp/static/django_chatapp/img/plus.png
+chatapp/static/django_chatapp/img/reply.png
+chatapp/static/django_chatapp/img/report.png
+chatapp/static/django_chatapp/img/send.png
+chatapp/static/django_chatapp/img/single-check.png
+chatapp/static/django_chatapp/img/supporter.png
+chatapp/static/django_chatapp/img/x.png
+chatapp/static/django_chatapp/js/client.js
+chatapp/static/django_chatapp/js/supporter.js
+chatapp/static/django_chatapp/js/vue-i18n.js
+chatapp/static/django_chatapp/js/vue3.js
+chatapp/static/django_chatapp/song/send.mp3
 chatapp/templates/client.html
 chatapp/templates/supporter.html
 chatapp/templatetags/__init__.py
 chatapp/templatetags/chatapp.py
 django_chatapp.egg-info/PKG-INFO
 django_chatapp.egg-info/SOURCES.txt
 django_chatapp.egg-info/dependency_links.txt
```

### Comparing `django-chatapp-1.3/setup.py` & `django-chatapp-1.4/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -5,26 +5,26 @@
 
 def read_me(filename):
     return codecs.open(filename, encoding='utf-8').read()
 
 
 setup(
     name='django-chatapp',
-    version='1.3',
+    version='1.4',
     python_requires='>=3',
     packages=find_packages(),
     include_package_data=True,
     description=(
-        'A complete chat application in your Django project.'
+        'A flexible Chat Application for open source software society.'
     ),
     url='https://github.com/saeedrezaghazanfari/django-chat-app',
-    download_url='https://pypi.org/project/django-chatapp/1.3/',
+    download_url='https://pypi.org/project/django-chatapp/1.4/',
     author='SaeedReza Ghazanfari',
     author_email='saeedreza.gh.1397@gmail.com',
-    keywords="django chat app",
+    keywords="django chat websocket channels asgi vuejs",
     license='MIT',
     platforms=['any'],
     install_requires=[
         "django",
         "channels",
         "daphne",
     ],
```

