# Comparing `tmp/django-comment-system-2.9.0.tar.gz` & `tmp/django-comment-system-2.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-comment-system-2.9.0.tar", last modified: Thu Apr  6 20:58:43 2023, max compression
+gzip compressed data, was "django-comment-system-2.9.1.tar", last modified: Fri Apr  7 10:53:45 2023, max compression
```

## Comparing `django-comment-system-2.9.0.tar` & `django-comment-system-2.9.1.tar`

### file list

```diff
@@ -1,104 +1,105 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      404 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3314 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    15470 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     2659 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/VERSION
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/
--rw-r--r--   0 runner    (1001) docker     (123)      898 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     6063 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/admin.py
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/apps.py
--rw-r--r--   0 runner    (1001) docker     (123)      181 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/forms.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/locale/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/locale/fa/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/django.mo
--rw-r--r--   0 runner    (1001) docker     (123)     3498 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/django.po
--rw-r--r--   0 runner    (1001) docker     (123)     1244 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/managers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/migrations/
--rw-r--r--   0 runner    (1001) docker     (123)     5259 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/migrations/0001_initial.py
--rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/migrations/0002_config.py
--rw-r--r--   0 runner    (1001) docker     (123)      980 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/migrations/0003_comment_content_main_comment_status_edited_and_more.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/migrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      513 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/mixins.py
--rw-r--r--   0 runner    (1001) docker     (123)     5572 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      442 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/static/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/static/comment/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/static/comment/css/
--rw-r--r--   0 runner    (1001) docker     (123)    40199 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/css/style.css
--rw-r--r--   0 runner    (1001) docker     (123)    32347 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/css/style.min.css
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/static/comment/font/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/static/comment/font/Vazir/
--rw-r--r--   0 runner    (1001) docker     (123)    50568 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Black.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51020 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Bold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51120 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraBold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51268 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraLight.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51180 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Light.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51128 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Medium.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    50684 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Regular.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51032 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-SemiBold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    50796 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Thin.woff2
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/
--rw-r--r--   0 runner    (1001) docker     (123)    49100 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Black.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49868 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Bold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49628 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49816 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49712 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Light.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49784 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Medium.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49044 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Regular.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49608 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49556 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Thin.woff2
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/static/comment/img/
--rw-r--r--   0 runner    (1001) docker     (123)     3602 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/img/profile.png
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/static/comment/js/
--rw-r--r--   0 runner    (1001) docker     (123)     7034 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/js/comment.js
--rw-r--r--   0 runner    (1001) docker     (123)     4323 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/js/comment.min.js
--rw-r--r--   0 runner    (1001) docker     (123)    89574 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/js/jquery.min.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/static/comment/tailwindcss/
--rw-r--r--   0 runner    (1001) docker     (123)     4764 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/tailwindcss/style.css
--rw-r--r--   0 runner    (1001) docker     (123)     7389 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/tailwindcss/tailwind.config.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/templates/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/templates/comment/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templates/comment/comment/
--rw-r--r--   0 runner    (1001) docker     (123)     7862 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comment_body.html
--rw-r--r--   0 runner    (1001) docker     (123)      595 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comment_counter.html
--rw-r--r--   0 runner    (1001) docker     (123)     2161 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comment_list.html
--rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comment_reactions.html
--rw-r--r--   0 runner    (1001) docker     (123)      765 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comments.html
--rw-r--r--   0 runner    (1001) docker     (123)      411 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/object_info.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templates/comment/forms/
--rw-r--r--   0 runner    (1001) docker     (123)     2463 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_create.html
--rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_delete.html
--rw-r--r--   0 runner    (1001) docker     (123)     2654 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_edit.html
--rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_reply.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templates/comment/icons/
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_arrow_backward.html
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_arrow_forward.html
--rw-r--r--   0 runner    (1001) docker     (123)      629 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_delete.html
--rw-r--r--   0 runner    (1001) docker     (123)      205 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_dots.html
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_down.html
--rw-r--r--   0 runner    (1001) docker     (123)      672 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_edit.html
--rw-r--r--   0 runner    (1001) docker     (123)      447 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_eye.html
--rw-r--r--   0 runner    (1001) docker     (123)     1163 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_eye_off.html
--rw-r--r--   0 runner    (1001) docker     (123)      280 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_pen.html
--rw-r--r--   0 runner    (1001) docker     (123)      706 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_pin.html
--rw-r--r--   0 runner    (1001) docker     (123)      264 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_up.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templates/comment/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/IMPORTS.html
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/SCRIPTS.html
--rw-r--r--   0 runner    (1001) docker     (123)     2340 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_empty.html
--rw-r--r--   0 runner    (1001) docker     (123)     1564 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_loader.html
--rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_pagination.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templatetags/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templatetags/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2507 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templatetags/comment_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/tests.py
--rw-r--r--   0 runner    (1001) docker     (123)      511 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     6423 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/django_comment_system.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3369 2023-04-06 20:58:43.000000 django-comment-system-2.9.0/django_comment_system.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      890 2023-04-06 20:58:43.559306 django-comment-system-2.9.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       36 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.677509 django-comment-system-2.9.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      404 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3314 2023-04-07 10:53:45.677509 django-comment-system-2.9.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    15470 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     2659 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/VERSION
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.665508 django-comment-system-2.9.1/comment/
+-rw-r--r--   0 runner    (1001) docker     (123)      898 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6063 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/admin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/apps.py
+-rw-r--r--   0 runner    (1001) docker     (123)      181 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/forms.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.661508 django-comment-system-2.9.1/comment/locale/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.661508 django-comment-system-2.9.1/comment/locale/fa/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.665508 django-comment-system-2.9.1/comment/locale/fa/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/locale/fa/LC_MESSAGES/django.mo
+-rw-r--r--   0 runner    (1001) docker     (123)     3498 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/locale/fa/LC_MESSAGES/django.po
+-rw-r--r--   0 runner    (1001) docker     (123)     1244 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/managers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.665508 django-comment-system-2.9.1/comment/migrations/
+-rw-r--r--   0 runner    (1001) docker     (123)     5259 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/migrations/0001_initial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/migrations/0002_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      980 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/migrations/0003_comment_content_main_comment_status_edited_and_more.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/migrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      513 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/mixins.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5572 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      442 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.661508 django-comment-system-2.9.1/comment/static/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.661508 django-comment-system-2.9.1/comment/static/comment/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.665508 django-comment-system-2.9.1/comment/static/comment/css/
+-rw-r--r--   0 runner    (1001) docker     (123)    41131 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/css/style.css
+-rw-r--r--   0 runner    (1001) docker     (123)    32950 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/css/style.min.css
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.661508 django-comment-system-2.9.1/comment/static/comment/font/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.669509 django-comment-system-2.9.1/comment/static/comment/font/Vazir/
+-rw-r--r--   0 runner    (1001) docker     (123)    50568 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Black.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51020 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Bold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51120 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-ExtraBold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51268 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-ExtraLight.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51180 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Light.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51128 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Medium.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    50684 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Regular.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51032 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-SemiBold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    50796 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Thin.woff2
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.669509 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/
+-rw-r--r--   0 runner    (1001) docker     (123)    49100 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Black.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49868 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Bold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49628 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49816 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49712 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Light.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49784 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Medium.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49044 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Regular.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49608 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49556 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Thin.woff2
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.669509 django-comment-system-2.9.1/comment/static/comment/img/
+-rw-r--r--   0 runner    (1001) docker     (123)     3602 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/img/profile.png
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.673509 django-comment-system-2.9.1/comment/static/comment/js/
+-rw-r--r--   0 runner    (1001) docker     (123)     7347 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/js/comment.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4521 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/js/comment.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)    89574 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/js/jquery.min.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.673509 django-comment-system-2.9.1/comment/static/comment/tailwindcss/
+-rw-r--r--   0 runner    (1001) docker     (123)     4764 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/tailwindcss/style.css
+-rw-r--r--   0 runner    (1001) docker     (123)     7389 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/static/comment/tailwindcss/tailwind.config.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.661508 django-comment-system-2.9.1/comment/templates/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.661508 django-comment-system-2.9.1/comment/templates/comment/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.673509 django-comment-system-2.9.1/comment/templates/comment/comment/
+-rw-r--r--   0 runner    (1001) docker     (123)     7862 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/comment/comment_body.html
+-rw-r--r--   0 runner    (1001) docker     (123)      595 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/comment/comment_counter.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2161 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/comment/comment_list.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/comment/comment_reactions.html
+-rw-r--r--   0 runner    (1001) docker     (123)      806 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/comment/comments.html
+-rw-r--r--   0 runner    (1001) docker     (123)      411 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/comment/object_info.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.673509 django-comment-system-2.9.1/comment/templates/comment/forms/
+-rw-r--r--   0 runner    (1001) docker     (123)     2493 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/forms/comment_form_create.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/forms/comment_form_delete.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2684 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/forms/comment_form_edit.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2685 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/forms/comment_form_reply.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.677509 django-comment-system-2.9.1/comment/templates/comment/icons/
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_arrow_backward.html
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_arrow_forward.html
+-rw-r--r--   0 runner    (1001) docker     (123)      629 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_delete.html
+-rw-r--r--   0 runner    (1001) docker     (123)      205 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_dots.html
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_down.html
+-rw-r--r--   0 runner    (1001) docker     (123)      672 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_edit.html
+-rw-r--r--   0 runner    (1001) docker     (123)      447 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_eye.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1163 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_eye_off.html
+-rw-r--r--   0 runner    (1001) docker     (123)      280 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_pen.html
+-rw-r--r--   0 runner    (1001) docker     (123)      706 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_pin.html
+-rw-r--r--   0 runner    (1001) docker     (123)      264 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/icons/icon_up.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.677509 django-comment-system-2.9.1/comment/templates/comment/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/utils/IMPORTS.html
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/utils/SCRIPTS.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2340 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/utils/comment_list_empty.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1564 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/utils/comment_list_loader.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/utils/comment_list_pagination.html
+-rw-r--r--   0 runner    (1001) docker     (123)      525 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templates/comment/utils/toast.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.677509 django-comment-system-2.9.1/comment/templatetags/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templatetags/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2507 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/templatetags/comment_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/tests.py
+-rw-r--r--   0 runner    (1001) docker     (123)      511 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6423 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/comment/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:53:45.677509 django-comment-system-2.9.1/django_comment_system.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3412 2023-04-07 10:53:45.000000 django-comment-system-2.9.1/django_comment_system.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      890 2023-04-07 10:53:45.677509 django-comment-system-2.9.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       36 2023-04-07 10:53:42.000000 django-comment-system-2.9.1/setup.py
```

### Comparing `django-comment-system-2.9.0/LICENSE` & `django-comment-system-2.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/PKG-INFO` & `django-comment-system-2.9.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-comment-system
-Version: 2.9.0
+Version: 2.9.1
 Summary: Django Comment System, It can be associated with any given model.
 Home-page: https://github.com/mahyar-amiri/django-comment-system
 Author: Mahyar Amiri
 Author-email: mmaahhyyaarr@gmail.com
 License: MIT
 Project-URL: Documentation, https://github.com/mahyar-amiri/django-comment-system/README.md
 Project-URL: Source Code, https://github.com/mahyar-amiri/django-comment-system
```

### Comparing `django-comment-system-2.9.0/README.md` & `django-comment-system-2.9.1/README.md`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/README.rst` & `django-comment-system-2.9.1/README.rst`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/__init__.py` & `django-comment-system-2.9.1/comment/__init__.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/admin.py` & `django-comment-system-2.9.1/comment/admin.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/django.mo` & `django-comment-system-2.9.1/comment/locale/fa/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/django.po` & `django-comment-system-2.9.1/comment/locale/fa/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/managers.py` & `django-comment-system-2.9.1/comment/managers.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/migrations/0001_initial.py` & `django-comment-system-2.9.1/comment/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/migrations/0002_config.py` & `django-comment-system-2.9.1/comment/migrations/0002_config.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/migrations/0003_comment_content_main_comment_status_edited_and_more.py` & `django-comment-system-2.9.1/comment/migrations/0003_comment_content_main_comment_status_edited_and_more.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/mixins.py` & `django-comment-system-2.9.1/comment/mixins.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/models.py` & `django-comment-system-2.9.1/comment/models.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/css/style.css` & `django-comment-system-2.9.1/comment/static/comment/css/style.css`

 * *Files 1% similar despite different names*

```diff
@@ -548,14 +548,18 @@
 .inset-0 {
   top: 0px;
   right: 0px;
   bottom: 0px;
   left: 0px;
 }
 
+.bottom-0 {
+  bottom: 0px;
+}
+
 .z-10 {
   z-index: 10;
 }
 
 .m-4 {
   margin: 1rem;
 }
@@ -586,14 +590,18 @@
   margin-bottom: 0.5rem;
 }
 
 .mb-16 {
   margin-bottom: 4rem;
 }
 
+.ml-auto {
+  margin-left: auto;
+}
+
 .box-border {
   box-sizing: border-box;
 }
 
 .block {
   display: block;
 }
@@ -646,14 +654,18 @@
   height: 1rem;
 }
 
 .h-5 {
   height: 1.25rem;
 }
 
+.h-8 {
+  height: 2rem;
+}
+
 .min-h-\[124px\] {
   min-height: 124px;
 }
 
 .min-h-full {
   min-height: 100%;
 }
@@ -1045,14 +1057,19 @@
   background-color: rgb(0 0 0 / var(--tw-bg-opacity));
 }
 
 .bg-page-bg-light {
   background-color: transparent;
 }
 
+.bg-gray-800 {
+  --tw-bg-opacity: 1;
+  background-color: rgb(31 41 55 / var(--tw-bg-opacity));
+}
+
 .bg-opacity-70 {
   --tw-bg-opacity: 0.7;
 }
 
 .fill-icon-pin-light {
   fill: #6b7280;
 }
@@ -1207,33 +1224,37 @@
   font-weight: 700;
 }
 
 .font-medium {
   font-weight: 500;
 }
 
-.leading-6 {
-  line-height: 1.5rem;
+.font-normal {
+  font-weight: 400;
 }
 
-.text-black {
-  --tw-text-opacity: 1;
-  color: rgb(0 0 0 / var(--tw-text-opacity));
+.leading-6 {
+  line-height: 1.5rem;
 }
 
 .text-comment-name-text-light {
   --tw-text-opacity: 1;
   color: rgb(0 0 0 / var(--tw-text-opacity));
 }
 
 .text-comment-time-text-light {
   --tw-text-opacity: 1;
   color: rgb(107 114 128 / var(--tw-text-opacity));
 }
 
+.text-black {
+  --tw-text-opacity: 1;
+  color: rgb(0 0 0 / var(--tw-text-opacity));
+}
+
 .text-comment-read-more-light {
   --tw-text-opacity: 1;
   color: rgb(29 78 216 / var(--tw-text-opacity));
 }
 
 .text-reply-text-light {
   --tw-text-opacity: 1;
@@ -1311,14 +1332,24 @@
 }
 
 .text-page-text-light {
   --tw-text-opacity: 1;
   color: rgb(156 163 175 / var(--tw-text-opacity));
 }
 
+.text-gray-300 {
+  --tw-text-opacity: 1;
+  color: rgb(209 213 219 / var(--tw-text-opacity));
+}
+
+.text-gray-400 {
+  --tw-text-opacity: 1;
+  color: rgb(156 163 175 / var(--tw-text-opacity));
+}
+
 .shadow-md {
   --tw-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
   --tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);
   box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
 }
 
 .shadow-xl {
@@ -1329,14 +1360,20 @@
 
 .shadow-sm {
   --tw-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);
   --tw-shadow-colored: 0 1px 2px 0 var(--tw-shadow-color);
   box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
 }
 
+.shadow {
+  --tw-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
+  --tw-shadow-colored: 0 1px 3px 0 var(--tw-shadow-color), 0 1px 2px -1px var(--tw-shadow-color);
+  box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
+}
+
 .outline-0 {
   outline-width: 0px;
 }
 
 .blur {
   --tw-blur: blur(8px);
   filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
@@ -1670,23 +1707,33 @@
 }
 
 .hover\:bg-page-bg-hover-light:hover {
   --tw-bg-opacity: 1;
   background-color: rgb(156 163 175 / var(--tw-bg-opacity));
 }
 
+.hover\:bg-gray-700:hover {
+  --tw-bg-opacity: 1;
+  background-color: rgb(55 65 81 / var(--tw-bg-opacity));
+}
+
 .hover\:fill-icon-pagination-hover-light:hover {
   fill: #374151;
 }
 
 .hover\:text-page-text-hover-light:hover {
   --tw-text-opacity: 1;
   color: rgb(255 255 255 / var(--tw-text-opacity));
 }
 
+.hover\:text-white:hover {
+  --tw-text-opacity: 1;
+  color: rgb(255 255 255 / var(--tw-text-opacity));
+}
+
 .group:hover .group-hover\:inline {
   display: inline;
 }
 
 .group:hover .group-hover\:scale-150 {
   --tw-scale-x: 1.5;
   --tw-scale-y: 1.5;
```

### Comparing `django-comment-system-2.9.0/comment/static/comment/css/style.min.css` & `django-comment-system-2.9.1/comment/static/comment/css/style.min.css`

 * *Files 14% similar despite different names*

```diff
@@ -1 +1 @@
- *, ::before, ::after {box-sizing: border-box;border-width: 0;border-style: solid;border-color: #e5e7eb;}::before, ::after {--tw-content: '';}html {line-height: 1.5;-webkit-text-size-adjust: 100%;-moz-tab-size: 4;-o-tab-size: 4;tab-size: 4;font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-feature-settings: normal;}body {margin: 0;line-height: inherit;}hr {height: 0;color: inherit;border-top-width: 1px;}abbr:where([title]) {-webkit-text-decoration: underline dotted;text-decoration: underline dotted;}h1, h2, h3, h4, h5, h6 {font-size: inherit;font-weight: inherit;}a {color: inherit;text-decoration: inherit;}b, strong {font-weight: bolder;}code, kbd, samp, pre {font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;font-size: 1em;}small {font-size: 80%;}sub, sup {font-size: 75%;line-height: 0;position: relative;vertical-align: baseline;}sub {bottom: -0.25em;}sup {top: -0.5em;}table {text-indent: 0;border-color: inherit;border-collapse: collapse;}button, input, optgroup, select, textarea {font-family: inherit;font-size: 100%;font-weight: inherit;line-height: inherit;color: inherit;margin: 0;padding: 0;}button, select {text-transform: none;}button, [type='button'], [type='reset'], [type='submit'] {-webkit-appearance: button;background-color: transparent;background-image: none;}:-moz-focusring {outline: auto;}:-moz-ui-invalid {box-shadow: none;}progress {vertical-align: baseline;}::-webkit-inner-spin-button, ::-webkit-outer-spin-button {height: auto;}[type='search'] {-webkit-appearance: textfield;outline-offset: -2px;}::-webkit-search-decoration {-webkit-appearance: none;}::-webkit-file-upload-button {-webkit-appearance: button;font: inherit;}summary {display: list-item;}blockquote, dl, dd, h1, h2, h3, h4, h5, h6, hr, figure, p, pre {margin: 0;}fieldset {margin: 0;padding: 0;}legend {padding: 0;}ol, ul, menu {list-style: none;margin: 0;padding: 0;}textarea {resize: vertical;}input::-moz-placeholder, textarea::-moz-placeholder {opacity: 1;color: #9ca3af;}input::placeholder, textarea::placeholder {opacity: 1;color: #9ca3af;}button, [role="button"] {cursor: pointer;}:disabled {cursor: default;}img, svg, video, canvas, audio, iframe, embed, object {display: block;vertical-align: middle;}img, video {max-width: 100%;height: auto;}[hidden] {display: none;}*, ::before, ::after {--tw-border-spacing-x: 0;--tw-border-spacing-y: 0;--tw-translate-x: 0;--tw-translate-y: 0;--tw-rotate: 0;--tw-skew-x: 0;--tw-skew-y: 0;--tw-scale-x: 1;--tw-scale-y: 1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness: proximity;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width: 0px;--tw-ring-offset-color: #fff;--tw-ring-color: rgb(59 130 246 / 0.5);--tw-ring-offset-shadow: 0 0 #0000;--tw-ring-shadow: 0 0 #0000;--tw-shadow: 0 0 #0000;--tw-shadow-colored: 0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;}::backdrop {--tw-border-spacing-x: 0;--tw-border-spacing-y: 0;--tw-translate-x: 0;--tw-translate-y: 0;--tw-rotate: 0;--tw-skew-x: 0;--tw-skew-y: 0;--tw-scale-x: 1;--tw-scale-y: 1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness: proximity;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width: 0px;--tw-ring-offset-color: #fff;--tw-ring-color: rgb(59 130 246 / 0.5);--tw-ring-offset-shadow: 0 0 #0000;--tw-ring-shadow: 0 0 #0000;--tw-shadow: 0 0 #0000;--tw-shadow-colored: 0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;}.sr-only {position: absolute;width: 1px;height: 1px;padding: 0;margin: -1px;overflow: hidden;clip: rect(0, 0, 0, 0);white-space: nowrap;border-width: 0;}.visible {visibility: visible;}.static {position: static;}.fixed {position: fixed;}.absolute {position: absolute;}.relative {position: relative;}.inset-0 {top: 0px;right: 0px;bottom: 0px;left: 0px;}.z-10 {z-index: 10;}.m-4 {margin: 1rem;}.mx-1 {margin-left: 0.25rem;margin-right: 0.25rem;}.my-4 {margin-top: 1rem;margin-bottom: 1rem;}.mt-2 {margin-top: 0.5rem;}.mb-4 {margin-bottom: 1rem;}.mt-3 {margin-top: 0.75rem;}.mb-2 {margin-bottom: 0.5rem;}.mb-16 {margin-bottom: 4rem;}.box-border {box-sizing: border-box;}.block {display: block;}.inline-block {display: inline-block;}.inline {display: inline;}.flex {display: flex;}.inline-flex {display: inline-flex;}.table {display: table;}.grid {display: grid;}.contents {display: contents;}.hidden {display: none;}.h-12 {height: 3rem;}.h-3 {height: 0.75rem;}.h-6 {height: 1.5rem;}.h-4 {height: 1rem;}.h-5 {height: 1.25rem;}.min-h-\[124px\] {min-height: 124px;}.min-h-full {min-height: 100%;}.min-h-\[66px\] {min-height: 66px;}.min-h-\[56px\] {min-height: 56px;}.w-12 {width: 3rem;}.w-3 {width: 0.75rem;}.w-6 {width: 1.5rem;}.w-full {width: 100%;}.w-8 {width: 2rem;}.w-72 {width: 18rem;}.w-24 {width: 6rem;}.w-64 {width: 16rem;}.w-36 {width: 9rem;}.w-16 {width: 4rem;}.w-5 {width: 1.25rem;}.origin-bottom {transform-origin: bottom;}.translate-x-16 {--tw-translate-x: 4rem;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.-translate-y-16 {--tw-translate-y: -4rem;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.-rotate-3 {--tw-rotate: -3deg;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.rotate-3 {--tw-rotate: 3deg;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.scale-90 {--tw-scale-x: .9;--tw-scale-y: .9;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.transform {transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}@keyframes pulse {50% {opacity: .5;}}.animate-pulse {animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;}@keyframes pulse {50% {opacity: .5;}}.animate-\[pulse_500ms_linear_infinite\] {animation: pulse 500ms linear infinite;}.cursor-pointer {cursor: pointer;}.cursor-default {cursor: default;}.resize-y {resize: vertical;}.resize {resize: both;}.flex-row-reverse {flex-direction: row-reverse;}.flex-col {flex-direction: column;}.place-content-center {place-content: center;}.content-center {align-content: center;}.items-end {align-items: flex-end;}.items-center {align-items: center;}.justify-end {justify-content: flex-end;}.justify-center {justify-content: center;}.justify-between {justify-content: space-between;}.space-x-3 > :not([hidden]) ~ :not([hidden]) {--tw-space-x-reverse: 0;margin-right: calc(0.75rem * var(--tw-space-x-reverse));margin-left: calc(0.75rem * calc(1 - var(--tw-space-x-reverse)));}.space-x-2 > :not([hidden]) ~ :not([hidden]) {--tw-space-x-reverse: 0;margin-right: calc(0.5rem * var(--tw-space-x-reverse));margin-left: calc(0.5rem * calc(1 - var(--tw-space-x-reverse)));}.space-y-2 > :not([hidden]) ~ :not([hidden]) {--tw-space-y-reverse: 0;margin-top: calc(0.5rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom: calc(0.5rem * var(--tw-space-y-reverse));}.place-self-center {place-self: center;}.self-center {align-self: center;}.overflow-hidden {overflow: hidden;}.overflow-y-auto {overflow-y: auto;}.whitespace-pre-wrap {white-space: pre-wrap;}.rounded-full {border-radius: 9999px;}.rounded-md {border-radius: 0.375rem;}.rounded-lg {border-radius: 0.5rem;}.border-2 {border-width: 2px;}.border {border-width: 1px;}.border-b-4 {border-bottom-width: 4px;}.border-none {border-style: none;}.border-section-primary-light {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-section-secondary-light {--tw-border-opacity: 1;border-color: rgb(0 0 0 / var(--tw-border-opacity));}.border-comment-parent-border-light {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-reply-border-light {--tw-border-opacity: 1;border-color: rgb(75 85 99 / var(--tw-border-opacity));}.border-comment-child-border-light {--tw-border-opacity: 1;border-color: rgb(165 180 252 / var(--tw-border-opacity));}.border-react-selected-border-light {--tw-border-opacity: 1;border-color: rgb(191 219 254 / var(--tw-border-opacity));}.border-react-default-border-light {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-transparent {border-color: transparent;}.border-gray-300 {--tw-border-opacity: 1;border-color: rgb(209 213 219 / var(--tw-border-opacity));}.border-textarea-bg-light {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-gray-200 {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-textarea-border-empty-light {--tw-border-opacity: 1;border-color: rgb(248 113 113 / var(--tw-border-opacity));}.bg-background-light {--tw-bg-opacity: 1;background-color: rgb(248 250 252 / var(--tw-bg-opacity));}.bg-comment-option-bg-light {--tw-bg-opacity: 1;background-color: rgb(243 244 246 / var(--tw-bg-opacity));}.bg-section-number-bg-light {--tw-bg-opacity: 1;background-color: rgb(229 231 235 / var(--tw-bg-opacity));}.bg-comment-parent-bg-light {--tw-bg-opacity: 1;background-color: rgb(248 250 252 / var(--tw-bg-opacity));}.bg-comment-child-bg-light {--tw-bg-opacity: 1;background-color: rgb(248 250 252 / var(--tw-bg-opacity));}.bg-react-selected-bg-light {--tw-bg-opacity: 1;background-color: rgb(219 234 254 / var(--tw-bg-opacity));}.bg-react-default-bg-light {--tw-bg-opacity: 1;background-color: rgb(243 244 246 / var(--tw-bg-opacity));}.bg-textarea-bg-light {--tw-bg-opacity: 1;background-color: rgb(229 231 235 / var(--tw-bg-opacity));}.bg-transparent {background-color: transparent;}.bg-btn-send-bg-light {--tw-bg-opacity: 1;background-color: rgb(0 0 0 / var(--tw-bg-opacity));}.bg-gray-500 {--tw-bg-opacity: 1;background-color: rgb(107 114 128 / var(--tw-bg-opacity));}.bg-delete-from-bg-light {--tw-bg-opacity: 1;background-color: rgb(255 255 255 / var(--tw-bg-opacity));}.bg-btn-delete-bg-light {--tw-bg-opacity: 1;background-color: rgb(220 38 38 / var(--tw-bg-opacity));}.bg-btn-cancel-bg-light {--tw-bg-opacity: 1;background-color: rgb(107 114 128 / var(--tw-bg-opacity));}.bg-btn-edit-bg-light {--tw-bg-opacity: 1;background-color: rgb(22 163 74 / var(--tw-bg-opacity));}.bg-btn-reply-bg-light {--tw-bg-opacity: 1;background-color: rgb(37 99 235 / var(--tw-bg-opacity));}.bg-slate-50 {--tw-bg-opacity: 1;background-color: rgb(248 250 252 / var(--tw-bg-opacity));}.bg-gray-300 {--tw-bg-opacity: 1;background-color: rgb(209 213 219 / var(--tw-bg-opacity));}.bg-gray-200 {--tw-bg-opacity: 1;background-color: rgb(229 231 235 / var(--tw-bg-opacity));}.bg-slate-100 {--tw-bg-opacity: 1;background-color: rgb(241 245 249 / var(--tw-bg-opacity));}.bg-page-current-bg-light {--tw-bg-opacity: 1;background-color: rgb(0 0 0 / var(--tw-bg-opacity));}.bg-page-bg-light {background-color: transparent;}.bg-opacity-70 {--tw-bg-opacity: 0.7;}.fill-icon-pin-light {fill: #6b7280;}.fill-icon-dots-light {fill: #6b7280;}.fill-icon-edit-light {fill: #16a34a;}.fill-icon-delete-light {fill: #ef4444;}.fill-none {fill: none;}.fill-icon-spoiler-option-light {fill: #111827;}.fill-icon-spoiler-light {fill: #6b7280;}.fill-gray-300 {fill: #d1d5db;}.stroke-icon-spoiler-light {stroke: #6b7280;}.p-4 {padding: 1rem;}.p-2 {padding: 0.5rem;}.p-1 {padding: 0.25rem;}.p-1\.5 {padding: 0.375rem;}.px-1 {padding-left: 0.25rem;padding-right: 0.25rem;}.px-2 {padding-left: 0.5rem;padding-right: 0.5rem;}.py-2 {padding-top: 0.5rem;padding-bottom: 0.5rem;}.px-6 {padding-left: 1.5rem;padding-right: 1.5rem;}.px-4 {padding-left: 1rem;padding-right: 1rem;}.py-3 {padding-top: 0.75rem;padding-bottom: 0.75rem;}.pb-2 {padding-bottom: 0.5rem;}.pt-5 {padding-top: 1.25rem;}.pb-4 {padding-bottom: 1rem;}.pt-1 {padding-top: 0.25rem;}.pt-4 {padding-top: 1rem;}.pt-3 {padding-top: 0.75rem;}.text-center {text-align: center;}.text-justify {text-align: justify;}.align-middle {vertical-align: middle;}.font-default-fd {font-family: Vazirmatn FD, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;}.font-default {font-family: Vazirmatn, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;}.text-lg {font-size: 1.125rem;line-height: 1.75rem;}.text-sm {font-size: 0.875rem;line-height: 1.25rem;}.text-base {font-size: 1rem;line-height: 1.5rem;}.text-xl {font-size: 1.25rem;line-height: 1.75rem;}.font-semibold {font-weight: 600;}.font-bold {font-weight: 700;}.font-medium {font-weight: 500;}.leading-6 {line-height: 1.5rem;}.text-black {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-comment-name-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-comment-time-text-light {--tw-text-opacity: 1;color: rgb(107 114 128 / var(--tw-text-opacity));}.text-comment-read-more-light {--tw-text-opacity: 1;color: rgb(29 78 216 / var(--tw-text-opacity));}.text-reply-text-light {--tw-text-opacity: 1;color: rgb(29 78 216 / var(--tw-text-opacity));}.text-section-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-section-number-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-react-count-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-textarea-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-btn-send-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-btn-login-text-light {--tw-text-opacity: 1;color: rgb(29 78 216 / var(--tw-text-opacity));}.text-delete-from-text-light {--tw-text-opacity: 1;color: rgb(17 24 39 / var(--tw-text-opacity));}.text-delete-from-subtext-light {--tw-text-opacity: 1;color: rgb(107 114 128 / var(--tw-text-opacity));}.text-btn-delete-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-btn-cancel-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-btn-edit-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-btn-reply-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-text-dark {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-page-current-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-page-text-light {--tw-text-opacity: 1;color: rgb(156 163 175 / var(--tw-text-opacity));}.shadow-md {--tw-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);--tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);}.shadow-xl {--tw-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);--tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color);box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);}.shadow-sm {--tw-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);--tw-shadow-colored: 0 1px 2px 0 var(--tw-shadow-color);box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);}.outline-0 {outline-width: 0px;}.blur {--tw-blur: blur(8px);filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);}.filter {filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);}.transition-transform {transition-property: transform;transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);transition-duration: 150ms;}.transition-opacity {transition-property: opacity;transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);transition-duration: 150ms;}.transition-all {transition-property: all;transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);transition-duration: 150ms;}.duration-200 {transition-duration: 200ms;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Thin.woff2') format('woff2');font-weight: 100;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-ExtraLight.woff2') format('woff2');font-weight: 200;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Light.woff2') format('woff2');font-weight: 300;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Regular.woff2') format('woff2');font-weight: 400;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Medium.woff2') format('woff2');font-weight: 500;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-SemiBold.woff2') format('woff2');font-weight: 600;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Bold.woff2') format('woff2');font-weight: 700;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-ExtraBold.woff2') format('woff2');font-weight: 800;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Black.woff2') format('woff2');font-weight: 900;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Thin.woff2') format('woff2');font-weight: 100;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2') format('woff2');font-weight: 200;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Light.woff2') format('woff2');font-weight: 300;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Regular.woff2') format('woff2');font-weight: 400;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Medium.woff2') format('woff2');font-weight: 500;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2') format('woff2');font-weight: 600;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Bold.woff2') format('woff2');font-weight: 700;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2') format('woff2');font-weight: 800;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Black.woff2') format('woff2');font-weight: 900;font-style: normal;font-display: swap;}  :root {--scrollbarprimary: #e5e7eb;--scrollbarsecondary: #9ca3af;}  [data-mode=dark] {--scrollbarprimary: #475569;--scrollbarsecondary: #9ca3af;}  textarea {scrollbar-width: thin;scrollbar-color: var(--scrollbarsecondary) var(--scrollbarprimary);}  textarea::-webkit-scrollbar {width: 10px;}  textarea::-webkit-scrollbar-track {background: var(--scrollbarprimary);border-radius: 5px;}  textarea::-webkit-scrollbar-thumb {background-color: var(--scrollbarsecondary);border-radius: 5px;border: 3px solid var(--scrollbarprimary);}  textarea::-webkit-resizer {border-width: 5px;border-style: solid;}  [dir=ltr] textarea::-webkit-resizer {border-color: var(--scrollbarprimary) var(--scrollbarsecondary) var(--scrollbarsecondary) var(--scrollbarprimary);}  [dir=rtl] textarea::-webkit-resizer {border-color: var(--scrollbarprimary) var(--scrollbarprimary) var(--scrollbarsecondary) var(--scrollbarsecondary);}  .selection\:bg-textarea-text-selection-light *::-moz-selection {--tw-bg-opacity: 1;background-color: rgb(199 210 254 / var(--tw-bg-opacity));}  .selection\:bg-textarea-text-selection-light *::selection {--tw-bg-opacity: 1;background-color: rgb(199 210 254 / var(--tw-bg-opacity));}  .selection\:bg-textarea-text-selection-light::-moz-selection {--tw-bg-opacity: 1;background-color: rgb(199 210 254 / var(--tw-bg-opacity));}  .selection\:bg-textarea-text-selection-light::selection {--tw-bg-opacity: 1;background-color: rgb(199 210 254 / var(--tw-bg-opacity));}  .placeholder\:text-textarea-text-placeholder-light::-moz-placeholder {--tw-text-opacity: 1;color: rgb(107 114 128 / var(--tw-text-opacity));}  .placeholder\:text-textarea-text-placeholder-light::placeholder {--tw-text-opacity: 1;color: rgb(107 114 128 / var(--tw-text-opacity));}  .hover\:bg-page-bg-hover-light:hover {--tw-bg-opacity: 1;background-color: rgb(156 163 175 / var(--tw-bg-opacity));}  .hover\:fill-icon-pagination-hover-light:hover {fill: #374151;}  .hover\:text-page-text-hover-light:hover {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}  .group:hover .group-hover\:inline {display: inline;}  .group:hover .group-hover\:scale-150 {--tw-scale-x: 1.5;--tw-scale-y: 1.5;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}  .peer:checked ~ .peer-checked\:block {display: block;}  .peer:checked ~ .peer-checked\:hidden {display: none;}  [dir="ltr"] .ltr\:ml-2 {margin-left: 0.5rem;}  [dir="ltr"] .ltr\:mr-1 {margin-right: 0.25rem;}  [dir="ltr"] .ltr\:mr-0 {margin-right: 0px;}  [dir="ltr"] .ltr\:mr-4 {margin-right: 1rem;}  [dir="ltr"] .ltr\:mr-2 {margin-right: 0.5rem;}  [dir="ltr"] .ltr\:ml-1 {margin-left: 0.25rem;}  [dir="ltr"] .ltr\:space-x-reverse > :not([hidden]) ~ :not([hidden]) {--tw-space-x-reverse: 1;}  [dir="ltr"] .ltr\:border-l-2 {border-left-width: 2px;}  [dir="ltr"] .ltr\:pl-4 {padding-left: 1rem;}  [dir="ltr"] .ltr\:pr-1 {padding-right: 0.25rem;}  [dir="ltr"] .ltr\:pr-4 {padding-right: 1rem;}  [dir="ltr"] .ltr\:pl-1 {padding-left: 0.25rem;}  [dir="ltr"] .ltr\:text-left {text-align: left;}  [dir="rtl"] .rtl\:mr-2 {margin-right: 0.5rem;}  [dir="rtl"] .rtl\:ml-1 {margin-left: 0.25rem;}  [dir="rtl"] .rtl\:ml-0 {margin-left: 0px;}  [dir="rtl"] .rtl\:ml-4 {margin-left: 1rem;}  [dir="rtl"] .rtl\:ml-2 {margin-left: 0.5rem;}  [dir="rtl"] .rtl\:mr-1 {margin-right: 0.25rem;}  [dir="rtl"] .rtl\:scale-x-\[-1\] {--tw-scale-x: -1;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}  [dir="rtl"] .rtl\:border-r-2 {border-right-width: 2px;}  [dir="rtl"] .rtl\:pr-4 {padding-right: 1rem;}  [dir="rtl"] .rtl\:pl-1 {padding-left: 0.25rem;}  [dir="rtl"] .rtl\:pl-4 {padding-left: 1rem;}  [dir="rtl"] .rtl\:pr-1 {padding-right: 0.25rem;}  [dir="rtl"] .rtl\:text-right {text-align: right;}  [data-mode="dark"] .dark\:border-section-primary-dark {--tw-border-opacity: 1;border-color: rgb(55 65 81 / var(--tw-border-opacity));}  [data-mode="dark"] .dark\:border-section-secondary-dark {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}  [data-mode="dark"] .dark\:border-comment-parent-border-dark {--tw-border-opacity: 1;border-color: rgb(75 85 99 / var(--tw-border-opacity));}  [data-mode="dark"] .dark\:border-reply-border-dark {--tw-border-opacity: 1;border-color: rgb(75 85 99 / var(--tw-border-opacity));}  [data-mode="dark"] .dark\:border-comment-child-border-dark {--tw-border-opacity: 1;border-color: rgb(165 180 252 / var(--tw-border-opacity));}  [data-mode="dark"] .dark\:border-react-selected-border-dark {--tw-border-opacity: 1;border-color: rgb(30 41 59 / var(--tw-border-opacity));}  [data-mode="dark"] .dark\:border-react-default-border-dark {--tw-border-opacity: 1;border-color: rgb(107 114 128 / var(--tw-border-opacity));}  [data-mode="dark"] .dark\:border-textarea-bg-dark {--tw-border-opacity: 1;border-color: rgb(71 85 105 / var(--tw-border-opacity));}  [data-mode="dark"] .dark\:border-textarea-border-empty-dark {--tw-border-opacity: 1;border-color: rgb(248 113 113 / var(--tw-border-opacity));}  [data-mode="dark"] .dark\:bg-background-dark {--tw-bg-opacity: 1;background-color: rgb(30 41 59 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-comment-option-bg-dark {--tw-bg-opacity: 1;background-color: rgb(71 85 105 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-comment-parent-bg-dark {--tw-bg-opacity: 1;background-color: rgb(30 41 59 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-comment-child-bg-dark {--tw-bg-opacity: 1;background-color: rgb(30 41 59 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-react-selected-bg-dark {--tw-bg-opacity: 1;background-color: rgb(100 116 139 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-react-default-bg-dark {--tw-bg-opacity: 1;background-color: rgb(51 65 85 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-textarea-bg-dark {--tw-bg-opacity: 1;background-color: rgb(71 85 105 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-btn-send-bg-dark {--tw-bg-opacity: 1;background-color: rgb(226 232 240 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-delete-from-bg-dark {--tw-bg-opacity: 1;background-color: rgb(71 85 105 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-btn-delete-bg-dark {--tw-bg-opacity: 1;background-color: rgb(239 68 68 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-btn-cancel-bg-dark {--tw-bg-opacity: 1;background-color: rgb(226 232 240 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-btn-edit-bg-dark {--tw-bg-opacity: 1;background-color: rgb(22 163 74 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-btn-reply-bg-dark {--tw-bg-opacity: 1;background-color: rgb(37 99 235 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-page-current-bg-dark {--tw-bg-opacity: 1;background-color: rgb(71 85 105 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:bg-page-bg-dark {background-color: transparent;}  [data-mode="dark"] .dark\:fill-icon-pin-dark {fill: #d1d5db;}  [data-mode="dark"] .dark\:fill-icon-dots-dark {fill: #e5e7eb;}  [data-mode="dark"] .dark\:fill-icon-edit-dark {fill: #4ade80;}  [data-mode="dark"] .dark\:fill-icon-delete-dark {fill: #f87171;}  [data-mode="dark"] .dark\:fill-icon-spoiler-option-dark {fill: #e5e7eb;}  [data-mode="dark"] .dark\:fill-icon-spoiler-dark {fill: #e5e7eb;}  [data-mode="dark"] .dark\:fill-icon-pagination-dark {fill: #9ca3af;}  [data-mode="dark"] .dark\:stroke-icon-spoiler-dark {stroke: #e5e7eb;}  [data-mode="dark"] .dark\:font-semibold {font-weight: 600;}  [data-mode="dark"] .dark\:text-comment-name-text-dark {--tw-text-opacity: 1;color: rgb(243 244 246 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-comment-time-text-dark {--tw-text-opacity: 1;color: rgb(209 213 219 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-white {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-comment-read-more-dark {--tw-text-opacity: 1;color: rgb(147 197 253 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-reply-text-dark {--tw-text-opacity: 1;color: rgb(147 197 253 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-section-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-react-count-text-dark {--tw-text-opacity: 1;color: rgb(243 244 246 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-textarea-text-dark {--tw-text-opacity: 1;color: rgb(243 244 246 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-btn-send-text-dark {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-btn-login-text-dark {--tw-text-opacity: 1;color: rgb(96 165 250 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-delete-from-text-dark {--tw-text-opacity: 1;color: rgb(243 244 246 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-delete-from-subtext-dark {--tw-text-opacity: 1;color: rgb(209 213 219 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-btn-delete-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-btn-cancel-text-dark {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-btn-edit-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-btn-reply-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-page-current-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:text-page-text-dark {--tw-text-opacity: 1;color: rgb(156 163 175 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:placeholder\:text-textarea-text-placeholder-dark::-moz-placeholder {--tw-text-opacity: 1;color: rgb(148 163 184 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:placeholder\:text-textarea-text-placeholder-dark::placeholder {--tw-text-opacity: 1;color: rgb(148 163 184 / var(--tw-text-opacity));}  [data-mode="dark"] .dark\:hover\:bg-page-bg-hover-dark:hover {--tw-bg-opacity: 1;background-color: rgb(51 65 85 / var(--tw-bg-opacity));}  [data-mode="dark"] .dark\:hover\:fill-icon-pagination-hover-dark:hover {fill: #6b7280;}  [data-mode="dark"] .dark\:hover\:text-page-text-hover-dark:hover {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}@media (min-width: 640px) {.sm\:my-8 {margin-top: 2rem;margin-bottom: 2rem;}  .sm\:mt-0 {margin-top: 0px;}  .sm\:flex {display: flex;}  .sm\:w-full {width: 100%;}  .sm\:w-auto {width: auto;}  .sm\:max-w-lg {max-width: 32rem;}  .sm\:flex-row-reverse {flex-direction: row-reverse;}  .sm\:items-start {align-items: flex-start;}  .sm\:items-center {align-items: center;}  .sm\:p-0 {padding: 0px;}  .sm\:p-6 {padding: 1.5rem;}  .sm\:px-6 {padding-left: 1.5rem;padding-right: 1.5rem;}  .sm\:pb-4 {padding-bottom: 1rem;}  .sm\:text-sm {font-size: 0.875rem;line-height: 1.25rem;}  [dir="ltr"] .sm\:ltr\:ml-4 {margin-left: 1rem;}  [dir="ltr"] .sm\:ltr\:ml-3 {margin-left: 0.75rem;}  [dir="ltr"] .ltr\:sm\:text-left {text-align: left;}  [dir="rtl"] .sm\:rtl\:mr-4 {margin-right: 1rem;}  [dir="rtl"] .sm\:rtl\:mr-3 {margin-right: 0.75rem;}  [dir="rtl"] .rtl\:sm\:text-right {text-align: right;}}
+ *, ::before, ::after {box-sizing: border-box;border-width: 0;border-style: solid;border-color: #e5e7eb;}::before, ::after {--tw-content: '';}html {line-height: 1.5;-webkit-text-size-adjust: 100%;-moz-tab-size: 4;-o-tab-size: 4;tab-size: 4;font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";font-feature-settings: normal;}body {margin: 0;line-height: inherit;}hr {height: 0;color: inherit;border-top-width: 1px;}abbr:where([title]) {-webkit-text-decoration: underline dotted;text-decoration: underline dotted;}h1, h2, h3, h4, h5, h6 {font-size: inherit;font-weight: inherit;}a {color: inherit;text-decoration: inherit;}b, strong {font-weight: bolder;}code, kbd, samp, pre {font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;font-size: 1em;}small {font-size: 80%;}sub, sup {font-size: 75%;line-height: 0;position: relative;vertical-align: baseline;}sub {bottom: -0.25em;}sup {top: -0.5em;}table {text-indent: 0;border-color: inherit;border-collapse: collapse;}button, input, optgroup, select, textarea {font-family: inherit;font-size: 100%;font-weight: inherit;line-height: inherit;color: inherit;margin: 0;padding: 0;}button, select {text-transform: none;}button, [type='button'], [type='reset'], [type='submit'] {-webkit-appearance: button;background-color: transparent;background-image: none;}:-moz-focusring {outline: auto;}:-moz-ui-invalid {box-shadow: none;}progress {vertical-align: baseline;}::-webkit-inner-spin-button, ::-webkit-outer-spin-button {height: auto;}[type='search'] {-webkit-appearance: textfield;outline-offset: -2px;}::-webkit-search-decoration {-webkit-appearance: none;}::-webkit-file-upload-button {-webkit-appearance: button;font: inherit;}summary {display: list-item;}blockquote, dl, dd, h1, h2, h3, h4, h5, h6, hr, figure, p, pre {margin: 0;}fieldset {margin: 0;padding: 0;}legend {padding: 0;}ol, ul, menu {list-style: none;margin: 0;padding: 0;}textarea {resize: vertical;}input::-moz-placeholder, textarea::-moz-placeholder {opacity: 1;color: #9ca3af;}input::placeholder, textarea::placeholder {opacity: 1;color: #9ca3af;}button, [role="button"] {cursor: pointer;}:disabled {cursor: default;}img, svg, video, canvas, audio, iframe, embed, object {display: block;vertical-align: middle;}img, video {max-width: 100%;height: auto;}[hidden] {display: none;}*, ::before, ::after {--tw-border-spacing-x: 0;--tw-border-spacing-y: 0;--tw-translate-x: 0;--tw-translate-y: 0;--tw-rotate: 0;--tw-skew-x: 0;--tw-skew-y: 0;--tw-scale-x: 1;--tw-scale-y: 1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness: proximity;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width: 0px;--tw-ring-offset-color: #fff;--tw-ring-color: rgb(59 130 246 / 0.5);--tw-ring-offset-shadow: 0 0 #0000;--tw-ring-shadow: 0 0 #0000;--tw-shadow: 0 0 #0000;--tw-shadow-colored: 0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;}::backdrop {--tw-border-spacing-x: 0;--tw-border-spacing-y: 0;--tw-translate-x: 0;--tw-translate-y: 0;--tw-rotate: 0;--tw-skew-x: 0;--tw-skew-y: 0;--tw-scale-x: 1;--tw-scale-y: 1;--tw-pan-x: ;--tw-pan-y: ;--tw-pinch-zoom: ;--tw-scroll-snap-strictness: proximity;--tw-ordinal: ;--tw-slashed-zero: ;--tw-numeric-figure: ;--tw-numeric-spacing: ;--tw-numeric-fraction: ;--tw-ring-inset: ;--tw-ring-offset-width: 0px;--tw-ring-offset-color: #fff;--tw-ring-color: rgb(59 130 246 / 0.5);--tw-ring-offset-shadow: 0 0 #0000;--tw-ring-shadow: 0 0 #0000;--tw-shadow: 0 0 #0000;--tw-shadow-colored: 0 0 #0000;--tw-blur: ;--tw-brightness: ;--tw-contrast: ;--tw-grayscale: ;--tw-hue-rotate: ;--tw-invert: ;--tw-saturate: ;--tw-sepia: ;--tw-drop-shadow: ;--tw-backdrop-blur: ;--tw-backdrop-brightness: ;--tw-backdrop-contrast: ;--tw-backdrop-grayscale: ;--tw-backdrop-hue-rotate: ;--tw-backdrop-invert: ;--tw-backdrop-opacity: ;--tw-backdrop-saturate: ;--tw-backdrop-sepia: ;}.sr-only {position: absolute;width: 1px;height: 1px;padding: 0;margin: -1px;overflow: hidden;clip: rect(0, 0, 0, 0);white-space: nowrap;border-width: 0;}.visible {visibility: visible;}.static {position: static;}.fixed {position: fixed;}.absolute {position: absolute;}.relative {position: relative;}.inset-0 {top: 0px;right: 0px;bottom: 0px;left: 0px;}.bottom-0 {bottom: 0px;}.z-10 {z-index: 10;}.m-4 {margin: 1rem;}.mx-1 {margin-left: 0.25rem;margin-right: 0.25rem;}.my-4 {margin-top: 1rem;margin-bottom: 1rem;}.mt-2 {margin-top: 0.5rem;}.mb-4 {margin-bottom: 1rem;}.mt-3 {margin-top: 0.75rem;}.mb-2 {margin-bottom: 0.5rem;}.mb-16 {margin-bottom: 4rem;}.ml-auto {margin-left: auto;}.box-border {box-sizing: border-box;}.block {display: block;}.inline-block {display: inline-block;}.inline {display: inline;}.flex {display: flex;}.inline-flex {display: inline-flex;}.table {display: table;}.grid {display: grid;}.contents {display: contents;}.hidden {display: none;}.h-12 {height: 3rem;}.h-3 {height: 0.75rem;}.h-6 {height: 1.5rem;}.h-4 {height: 1rem;}.h-5 {height: 1.25rem;}.h-8 {height: 2rem;}.min-h-\[124px\] {min-height: 124px;}.min-h-full {min-height: 100%;}.min-h-\[66px\] {min-height: 66px;}.min-h-\[56px\] {min-height: 56px;}.w-12 {width: 3rem;}.w-3 {width: 0.75rem;}.w-6 {width: 1.5rem;}.w-full {width: 100%;}.w-8 {width: 2rem;}.w-72 {width: 18rem;}.w-24 {width: 6rem;}.w-64 {width: 16rem;}.w-36 {width: 9rem;}.w-16 {width: 4rem;}.w-5 {width: 1.25rem;}.origin-bottom {transform-origin: bottom;}.translate-x-16 {--tw-translate-x: 4rem;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.-translate-y-16 {--tw-translate-y: -4rem;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.-rotate-3 {--tw-rotate: -3deg;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.rotate-3 {--tw-rotate: 3deg;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.scale-90 {--tw-scale-x: .9;--tw-scale-y: .9;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.transform {transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}@keyframes pulse {50% {opacity: .5;}}.animate-pulse {animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;}@keyframes pulse {50% {opacity: .5;}}.animate-\[pulse_500ms_linear_infinite\] {animation: pulse 500ms linear infinite;}.cursor-pointer {cursor: pointer;}.cursor-default {cursor: default;}.resize-y {resize: vertical;}.resize {resize: both;}.flex-row-reverse {flex-direction: row-reverse;}.flex-col {flex-direction: column;}.place-content-center {place-content: center;}.content-center {align-content: center;}.items-end {align-items: flex-end;}.items-center {align-items: center;}.justify-end {justify-content: flex-end;}.justify-center {justify-content: center;}.justify-between {justify-content: space-between;}.space-x-3 > :not([hidden]) ~ :not([hidden]) {--tw-space-x-reverse: 0;margin-right: calc(0.75rem * var(--tw-space-x-reverse));margin-left: calc(0.75rem * calc(1 - var(--tw-space-x-reverse)));}.space-x-2 > :not([hidden]) ~ :not([hidden]) {--tw-space-x-reverse: 0;margin-right: calc(0.5rem * var(--tw-space-x-reverse));margin-left: calc(0.5rem * calc(1 - var(--tw-space-x-reverse)));}.space-y-2 > :not([hidden]) ~ :not([hidden]) {--tw-space-y-reverse: 0;margin-top: calc(0.5rem * calc(1 - var(--tw-space-y-reverse)));margin-bottom: calc(0.5rem * var(--tw-space-y-reverse));}.place-self-center {place-self: center;}.self-center {align-self: center;}.overflow-hidden {overflow: hidden;}.overflow-y-auto {overflow-y: auto;}.whitespace-pre-wrap {white-space: pre-wrap;}.rounded-full {border-radius: 9999px;}.rounded-md {border-radius: 0.375rem;}.rounded-lg {border-radius: 0.5rem;}.border-2 {border-width: 2px;}.border {border-width: 1px;}.border-b-4 {border-bottom-width: 4px;}.border-none {border-style: none;}.border-section-primary-light {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-section-secondary-light {--tw-border-opacity: 1;border-color: rgb(0 0 0 / var(--tw-border-opacity));}.border-comment-parent-border-light {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-reply-border-light {--tw-border-opacity: 1;border-color: rgb(75 85 99 / var(--tw-border-opacity));}.border-comment-child-border-light {--tw-border-opacity: 1;border-color: rgb(165 180 252 / var(--tw-border-opacity));}.border-react-selected-border-light {--tw-border-opacity: 1;border-color: rgb(191 219 254 / var(--tw-border-opacity));}.border-react-default-border-light {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-transparent {border-color: transparent;}.border-gray-300 {--tw-border-opacity: 1;border-color: rgb(209 213 219 / var(--tw-border-opacity));}.border-textarea-bg-light {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-gray-200 {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}.border-textarea-border-empty-light {--tw-border-opacity: 1;border-color: rgb(248 113 113 / var(--tw-border-opacity));}.bg-background-light {--tw-bg-opacity: 1;background-color: rgb(248 250 252 / var(--tw-bg-opacity));}.bg-comment-option-bg-light {--tw-bg-opacity: 1;background-color: rgb(243 244 246 / var(--tw-bg-opacity));}.bg-section-number-bg-light {--tw-bg-opacity: 1;background-color: rgb(229 231 235 / var(--tw-bg-opacity));}.bg-comment-parent-bg-light {--tw-bg-opacity: 1;background-color: rgb(248 250 252 / var(--tw-bg-opacity));}.bg-comment-child-bg-light {--tw-bg-opacity: 1;background-color: rgb(248 250 252 / var(--tw-bg-opacity));}.bg-react-selected-bg-light {--tw-bg-opacity: 1;background-color: rgb(219 234 254 / var(--tw-bg-opacity));}.bg-react-default-bg-light {--tw-bg-opacity: 1;background-color: rgb(243 244 246 / var(--tw-bg-opacity));}.bg-textarea-bg-light {--tw-bg-opacity: 1;background-color: rgb(229 231 235 / var(--tw-bg-opacity));}.bg-transparent {background-color: transparent;}.bg-btn-send-bg-light {--tw-bg-opacity: 1;background-color: rgb(0 0 0 / var(--tw-bg-opacity));}.bg-gray-500 {--tw-bg-opacity: 1;background-color: rgb(107 114 128 / var(--tw-bg-opacity));}.bg-delete-from-bg-light {--tw-bg-opacity: 1;background-color: rgb(255 255 255 / var(--tw-bg-opacity));}.bg-btn-delete-bg-light {--tw-bg-opacity: 1;background-color: rgb(220 38 38 / var(--tw-bg-opacity));}.bg-btn-cancel-bg-light {--tw-bg-opacity: 1;background-color: rgb(107 114 128 / var(--tw-bg-opacity));}.bg-btn-edit-bg-light {--tw-bg-opacity: 1;background-color: rgb(22 163 74 / var(--tw-bg-opacity));}.bg-btn-reply-bg-light {--tw-bg-opacity: 1;background-color: rgb(37 99 235 / var(--tw-bg-opacity));}.bg-slate-50 {--tw-bg-opacity: 1;background-color: rgb(248 250 252 / var(--tw-bg-opacity));}.bg-gray-300 {--tw-bg-opacity: 1;background-color: rgb(209 213 219 / var(--tw-bg-opacity));}.bg-gray-200 {--tw-bg-opacity: 1;background-color: rgb(229 231 235 / var(--tw-bg-opacity));}.bg-slate-100 {--tw-bg-opacity: 1;background-color: rgb(241 245 249 / var(--tw-bg-opacity));}.bg-page-current-bg-light {--tw-bg-opacity: 1;background-color: rgb(0 0 0 / var(--tw-bg-opacity));}.bg-page-bg-light {background-color: transparent;}.bg-gray-800 {--tw-bg-opacity: 1;background-color: rgb(31 41 55 / var(--tw-bg-opacity));}.bg-opacity-70 {--tw-bg-opacity: 0.7;}.fill-icon-pin-light {fill: #6b7280;}.fill-icon-dots-light {fill: #6b7280;}.fill-icon-edit-light {fill: #16a34a;}.fill-icon-delete-light {fill: #ef4444;}.fill-none {fill: none;}.fill-icon-spoiler-option-light {fill: #111827;}.fill-icon-spoiler-light {fill: #6b7280;}.fill-gray-300 {fill: #d1d5db;}.stroke-icon-spoiler-light {stroke: #6b7280;}.p-4 {padding: 1rem;}.p-2 {padding: 0.5rem;}.p-1 {padding: 0.25rem;}.p-1\.5 {padding: 0.375rem;}.px-1 {padding-left: 0.25rem;padding-right: 0.25rem;}.px-2 {padding-left: 0.5rem;padding-right: 0.5rem;}.py-2 {padding-top: 0.5rem;padding-bottom: 0.5rem;}.px-6 {padding-left: 1.5rem;padding-right: 1.5rem;}.px-4 {padding-left: 1rem;padding-right: 1rem;}.py-3 {padding-top: 0.75rem;padding-bottom: 0.75rem;}.pb-2 {padding-bottom: 0.5rem;}.pt-5 {padding-top: 1.25rem;}.pb-4 {padding-bottom: 1rem;}.pt-1 {padding-top: 0.25rem;}.pt-4 {padding-top: 1rem;}.pt-3 {padding-top: 0.75rem;}.text-center {text-align: center;}.text-justify {text-align: justify;}.align-middle {vertical-align: middle;}.font-default-fd {font-family: Vazirmatn FD, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;}.font-default {font-family: Vazirmatn, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, Noto Color Emoji;}.text-lg {font-size: 1.125rem;line-height: 1.75rem;}.text-sm {font-size: 0.875rem;line-height: 1.25rem;}.text-base {font-size: 1rem;line-height: 1.5rem;}.text-xl {font-size: 1.25rem;line-height: 1.75rem;}.font-semibold {font-weight: 600;}.font-bold {font-weight: 700;}.font-medium {font-weight: 500;}.font-normal {font-weight: 400;}.leading-6 {line-height: 1.5rem;}.text-comment-name-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-comment-time-text-light {--tw-text-opacity: 1;color: rgb(107 114 128 / var(--tw-text-opacity));}.text-black {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-comment-read-more-light {--tw-text-opacity: 1;color: rgb(29 78 216 / var(--tw-text-opacity));}.text-reply-text-light {--tw-text-opacity: 1;color: rgb(29 78 216 / var(--tw-text-opacity));}.text-section-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-section-number-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-react-count-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-textarea-text-light {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-btn-send-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-btn-login-text-light {--tw-text-opacity: 1;color: rgb(29 78 216 / var(--tw-text-opacity));}.text-delete-from-text-light {--tw-text-opacity: 1;color: rgb(17 24 39 / var(--tw-text-opacity));}.text-delete-from-subtext-light {--tw-text-opacity: 1;color: rgb(107 114 128 / var(--tw-text-opacity));}.text-btn-delete-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-btn-cancel-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-btn-edit-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-btn-reply-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-text-dark {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}.text-page-current-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.text-page-text-light {--tw-text-opacity: 1;color: rgb(156 163 175 / var(--tw-text-opacity));}.text-gray-300 {--tw-text-opacity: 1;color: rgb(209 213 219 / var(--tw-text-opacity));}.text-gray-400 {--tw-text-opacity: 1;color: rgb(156 163 175 / var(--tw-text-opacity));}.shadow-md {--tw-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);--tw-shadow-colored: 0 4px 6px -1px var(--tw-shadow-color), 0 2px 4px -2px var(--tw-shadow-color);box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);}.shadow-xl {--tw-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);--tw-shadow-colored: 0 20px 25px -5px var(--tw-shadow-color), 0 8px 10px -6px var(--tw-shadow-color);box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);}.shadow-sm {--tw-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);--tw-shadow-colored: 0 1px 2px 0 var(--tw-shadow-color);box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);}.shadow {--tw-shadow: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);--tw-shadow-colored: 0 1px 3px 0 var(--tw-shadow-color), 0 1px 2px -1px var(--tw-shadow-color);box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);}.outline-0 {outline-width: 0px;}.blur {--tw-blur: blur(8px);filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);}.filter {filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);}.transition-transform {transition-property: transform;transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);transition-duration: 150ms;}.transition-opacity {transition-property: opacity;transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);transition-duration: 150ms;}.transition-all {transition-property: all;transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);transition-duration: 150ms;}.duration-200 {transition-duration: 200ms;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Thin.woff2') format('woff2');font-weight: 100;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-ExtraLight.woff2') format('woff2');font-weight: 200;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Light.woff2') format('woff2');font-weight: 300;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Regular.woff2') format('woff2');font-weight: 400;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Medium.woff2') format('woff2');font-weight: 500;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-SemiBold.woff2') format('woff2');font-weight: 600;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Bold.woff2') format('woff2');font-weight: 700;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-ExtraBold.woff2') format('woff2');font-weight: 800;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn;src: url('../font/Vazir/Vazirmatn-Black.woff2') format('woff2');font-weight: 900;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Thin.woff2') format('woff2');font-weight: 100;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2') format('woff2');font-weight: 200;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Light.woff2') format('woff2');font-weight: 300;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Regular.woff2') format('woff2');font-weight: 400;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Medium.woff2') format('woff2');font-weight: 500;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2') format('woff2');font-weight: 600;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Bold.woff2') format('woff2');font-weight: 700;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2') format('woff2');font-weight: 800;font-style: normal;font-display: swap;}@font-face {font-family: Vazirmatn FD;src: url('../font/Vazir-FD/Vazirmatn-FD-Black.woff2') format('woff2');font-weight: 900;font-style: normal;font-display: swap;}:root {--scrollbarprimary: #e5e7eb;--scrollbarsecondary: #9ca3af;}[data-mode=dark] {--scrollbarprimary: #475569;--scrollbarsecondary: #9ca3af;}textarea {scrollbar-width: thin;scrollbar-color: var(--scrollbarsecondary) var(--scrollbarprimary);}textarea::-webkit-scrollbar {width: 10px;}textarea::-webkit-scrollbar-track {background: var(--scrollbarprimary);border-radius: 5px;}textarea::-webkit-scrollbar-thumb {background-color: var(--scrollbarsecondary);border-radius: 5px;border: 3px solid var(--scrollbarprimary);}textarea::-webkit-resizer {border-width: 5px;border-style: solid;}[dir=ltr] textarea::-webkit-resizer {border-color: var(--scrollbarprimary) var(--scrollbarsecondary) var(--scrollbarsecondary) var(--scrollbarprimary);}[dir=rtl] textarea::-webkit-resizer {border-color: var(--scrollbarprimary) var(--scrollbarprimary) var(--scrollbarsecondary) var(--scrollbarsecondary);}.selection\:bg-textarea-text-selection-light *::-moz-selection {--tw-bg-opacity: 1;background-color: rgb(199 210 254 / var(--tw-bg-opacity));}.selection\:bg-textarea-text-selection-light *::selection {--tw-bg-opacity: 1;background-color: rgb(199 210 254 / var(--tw-bg-opacity));}.selection\:bg-textarea-text-selection-light::-moz-selection {--tw-bg-opacity: 1;background-color: rgb(199 210 254 / var(--tw-bg-opacity));}.selection\:bg-textarea-text-selection-light::selection {--tw-bg-opacity: 1;background-color: rgb(199 210 254 / var(--tw-bg-opacity));}.placeholder\:text-textarea-text-placeholder-light::-moz-placeholder {--tw-text-opacity: 1;color: rgb(107 114 128 / var(--tw-text-opacity));}.placeholder\:text-textarea-text-placeholder-light::placeholder {--tw-text-opacity: 1;color: rgb(107 114 128 / var(--tw-text-opacity));}.hover\:bg-page-bg-hover-light:hover {--tw-bg-opacity: 1;background-color: rgb(156 163 175 / var(--tw-bg-opacity));}.hover\:bg-gray-700:hover {--tw-bg-opacity: 1;background-color: rgb(55 65 81 / var(--tw-bg-opacity));}.hover\:fill-icon-pagination-hover-light:hover {fill: #374151;}.hover\:text-page-text-hover-light:hover {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.hover\:text-white:hover {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}.group:hover .group-hover\:inline {display: inline;}.group:hover .group-hover\:scale-150 {--tw-scale-x: 1.5;--tw-scale-y: 1.5;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}.peer:checked ~ .peer-checked\:block {display: block;}.peer:checked ~ .peer-checked\:hidden {display: none;}[dir="ltr"] .ltr\:ml-2 {margin-left: 0.5rem;}[dir="ltr"] .ltr\:mr-1 {margin-right: 0.25rem;}[dir="ltr"] .ltr\:mr-0 {margin-right: 0px;}[dir="ltr"] .ltr\:mr-4 {margin-right: 1rem;}[dir="ltr"] .ltr\:mr-2 {margin-right: 0.5rem;}[dir="ltr"] .ltr\:ml-1 {margin-left: 0.25rem;}[dir="ltr"] .ltr\:space-x-reverse > :not([hidden]) ~ :not([hidden]) {--tw-space-x-reverse: 1;}[dir="ltr"] .ltr\:border-l-2 {border-left-width: 2px;}[dir="ltr"] .ltr\:pl-4 {padding-left: 1rem;}[dir="ltr"] .ltr\:pr-1 {padding-right: 0.25rem;}[dir="ltr"] .ltr\:pr-4 {padding-right: 1rem;}[dir="ltr"] .ltr\:pl-1 {padding-left: 0.25rem;}[dir="ltr"] .ltr\:text-left {text-align: left;}[dir="rtl"] .rtl\:mr-2 {margin-right: 0.5rem;}[dir="rtl"] .rtl\:ml-1 {margin-left: 0.25rem;}[dir="rtl"] .rtl\:ml-0 {margin-left: 0px;}[dir="rtl"] .rtl\:ml-4 {margin-left: 1rem;}[dir="rtl"] .rtl\:ml-2 {margin-left: 0.5rem;}[dir="rtl"] .rtl\:mr-1 {margin-right: 0.25rem;}[dir="rtl"] .rtl\:scale-x-\[-1\] {--tw-scale-x: -1;transform: translate(var(--tw-translate-x), var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y));}[dir="rtl"] .rtl\:border-r-2 {border-right-width: 2px;}[dir="rtl"] .rtl\:pr-4 {padding-right: 1rem;}[dir="rtl"] .rtl\:pl-1 {padding-left: 0.25rem;}[dir="rtl"] .rtl\:pl-4 {padding-left: 1rem;}[dir="rtl"] .rtl\:pr-1 {padding-right: 0.25rem;}[dir="rtl"] .rtl\:text-right {text-align: right;}[data-mode="dark"] .dark\:border-section-primary-dark {--tw-border-opacity: 1;border-color: rgb(55 65 81 / var(--tw-border-opacity));}[data-mode="dark"] .dark\:border-section-secondary-dark {--tw-border-opacity: 1;border-color: rgb(229 231 235 / var(--tw-border-opacity));}[data-mode="dark"] .dark\:border-comment-parent-border-dark {--tw-border-opacity: 1;border-color: rgb(75 85 99 / var(--tw-border-opacity));}[data-mode="dark"] .dark\:border-reply-border-dark {--tw-border-opacity: 1;border-color: rgb(75 85 99 / var(--tw-border-opacity));}[data-mode="dark"] .dark\:border-comment-child-border-dark {--tw-border-opacity: 1;border-color: rgb(165 180 252 / var(--tw-border-opacity));}[data-mode="dark"] .dark\:border-react-selected-border-dark {--tw-border-opacity: 1;border-color: rgb(30 41 59 / var(--tw-border-opacity));}[data-mode="dark"] .dark\:border-react-default-border-dark {--tw-border-opacity: 1;border-color: rgb(107 114 128 / var(--tw-border-opacity));}[data-mode="dark"] .dark\:border-textarea-bg-dark {--tw-border-opacity: 1;border-color: rgb(71 85 105 / var(--tw-border-opacity));}[data-mode="dark"] .dark\:border-textarea-border-empty-dark {--tw-border-opacity: 1;border-color: rgb(248 113 113 / var(--tw-border-opacity));}[data-mode="dark"] .dark\:bg-background-dark {--tw-bg-opacity: 1;background-color: rgb(30 41 59 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-comment-option-bg-dark {--tw-bg-opacity: 1;background-color: rgb(71 85 105 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-comment-parent-bg-dark {--tw-bg-opacity: 1;background-color: rgb(30 41 59 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-comment-child-bg-dark {--tw-bg-opacity: 1;background-color: rgb(30 41 59 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-react-selected-bg-dark {--tw-bg-opacity: 1;background-color: rgb(100 116 139 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-react-default-bg-dark {--tw-bg-opacity: 1;background-color: rgb(51 65 85 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-textarea-bg-dark {--tw-bg-opacity: 1;background-color: rgb(71 85 105 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-btn-send-bg-dark {--tw-bg-opacity: 1;background-color: rgb(226 232 240 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-delete-from-bg-dark {--tw-bg-opacity: 1;background-color: rgb(71 85 105 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-btn-delete-bg-dark {--tw-bg-opacity: 1;background-color: rgb(239 68 68 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-btn-cancel-bg-dark {--tw-bg-opacity: 1;background-color: rgb(226 232 240 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-btn-edit-bg-dark {--tw-bg-opacity: 1;background-color: rgb(22 163 74 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-btn-reply-bg-dark {--tw-bg-opacity: 1;background-color: rgb(37 99 235 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-page-current-bg-dark {--tw-bg-opacity: 1;background-color: rgb(71 85 105 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:bg-page-bg-dark {background-color: transparent;}[data-mode="dark"] .dark\:fill-icon-pin-dark {fill: #d1d5db;}[data-mode="dark"] .dark\:fill-icon-dots-dark {fill: #e5e7eb;}[data-mode="dark"] .dark\:fill-icon-edit-dark {fill: #4ade80;}[data-mode="dark"] .dark\:fill-icon-delete-dark {fill: #f87171;}[data-mode="dark"] .dark\:fill-icon-spoiler-option-dark {fill: #e5e7eb;}[data-mode="dark"] .dark\:fill-icon-spoiler-dark {fill: #e5e7eb;}[data-mode="dark"] .dark\:fill-icon-pagination-dark {fill: #9ca3af;}[data-mode="dark"] .dark\:stroke-icon-spoiler-dark {stroke: #e5e7eb;}[data-mode="dark"] .dark\:font-semibold {font-weight: 600;}[data-mode="dark"] .dark\:text-comment-name-text-dark {--tw-text-opacity: 1;color: rgb(243 244 246 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-comment-time-text-dark {--tw-text-opacity: 1;color: rgb(209 213 219 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-white {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-comment-read-more-dark {--tw-text-opacity: 1;color: rgb(147 197 253 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-reply-text-dark {--tw-text-opacity: 1;color: rgb(147 197 253 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-section-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-react-count-text-dark {--tw-text-opacity: 1;color: rgb(243 244 246 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-textarea-text-dark {--tw-text-opacity: 1;color: rgb(243 244 246 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-btn-send-text-dark {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-btn-login-text-dark {--tw-text-opacity: 1;color: rgb(96 165 250 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-delete-from-text-dark {--tw-text-opacity: 1;color: rgb(243 244 246 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-delete-from-subtext-dark {--tw-text-opacity: 1;color: rgb(209 213 219 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-btn-delete-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-btn-cancel-text-dark {--tw-text-opacity: 1;color: rgb(0 0 0 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-btn-edit-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-btn-reply-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-text-light {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-page-current-text-dark {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:text-page-text-dark {--tw-text-opacity: 1;color: rgb(156 163 175 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:placeholder\:text-textarea-text-placeholder-dark::-moz-placeholder {--tw-text-opacity: 1;color: rgb(148 163 184 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:placeholder\:text-textarea-text-placeholder-dark::placeholder {--tw-text-opacity: 1;color: rgb(148 163 184 / var(--tw-text-opacity));}[data-mode="dark"] .dark\:hover\:bg-page-bg-hover-dark:hover {--tw-bg-opacity: 1;background-color: rgb(51 65 85 / var(--tw-bg-opacity));}[data-mode="dark"] .dark\:hover\:fill-icon-pagination-hover-dark:hover {fill: #6b7280;}[data-mode="dark"] .dark\:hover\:text-page-text-hover-dark:hover {--tw-text-opacity: 1;color: rgb(255 255 255 / var(--tw-text-opacity));}@media (min-width: 640px) {.sm\:my-8 {margin-top: 2rem;margin-bottom: 2rem;}.sm\:mt-0 {margin-top: 0px;}.sm\:flex {display: flex;}.sm\:w-full {width: 100%;}.sm\:w-auto {width: auto;}.sm\:max-w-lg {max-width: 32rem;}.sm\:flex-row-reverse {flex-direction: row-reverse;}.sm\:items-start {align-items: flex-start;}.sm\:items-center {align-items: center;}.sm\:p-0 {padding: 0px;}.sm\:p-6 {padding: 1.5rem;}.sm\:px-6 {padding-left: 1.5rem;padding-right: 1.5rem;}.sm\:pb-4 {padding-bottom: 1rem;}.sm\:text-sm {font-size: 0.875rem;line-height: 1.25rem;}[dir="ltr"] .sm\:ltr\:ml-4 {margin-left: 1rem;}[dir="ltr"] .sm\:ltr\:ml-3 {margin-left: 0.75rem;}[dir="ltr"] .ltr\:sm\:text-left {text-align: left;}[dir="rtl"] .sm\:rtl\:mr-4 {margin-right: 1rem;}[dir="rtl"] .sm\:rtl\:mr-3 {margin-right: 0.75rem;}[dir="rtl"] .rtl\:sm\:text-right {text-align: right;}}
```

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Black.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Black.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Bold.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Bold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraBold.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-ExtraBold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraLight.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-ExtraLight.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Light.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Light.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Medium.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Medium.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Regular.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Regular.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-SemiBold.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-SemiBold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Thin.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir/Vazirmatn-Thin.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Black.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Black.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Bold.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Bold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Light.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Light.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Medium.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Medium.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Regular.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Regular.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Thin.woff2` & `django-comment-system-2.9.1/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Thin.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/img/profile.png` & `django-comment-system-2.9.1/comment/static/comment/img/profile.png`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/js/comment.js` & `django-comment-system-2.9.1/comment/static/comment/js/comment.js`

 * *Files 5% similar despite different names*

#### js-beautify {}

```diff
@@ -65,15 +65,15 @@
     }
 }
 
 function ResetDeleteCommentForm() {
     $(`#comment-modal`).html('');
 }
 
-function CreateComment(form_id) {
+function CreateComment(form_id, status_check) {
     let form = $(`#${form_id}`);
     let method = form.prop('method');
     let action = form.prop('action');
     let formData = {
         //OBJECT INPUTS
         app_name: $("#form-comment-create [name='app_name']").val(),
         model_name: $("#form-comment-create [name='model_name']").val(),
@@ -90,14 +90,17 @@
         url: action,
         headers: {
             "X-Requested-With": "XMLHttpRequest",
             "X-CSRFToken": getCookie("csrftoken"),
         },
         data: formData,
         success: function() {
+            if (status_check) {
+                document.getElementById('toast').classList.remove('hidden');
+            }
             if (formData.parent_id) {
                 let page = $(`#form-comment-reply-${formData.parent_id} [name='page']`).val();
                 LoadCommentList(page);
             } else {
                 ResetCreateCommentForm();
                 LoadCommentList();
             }
@@ -116,15 +119,15 @@
     if (textarea.val().trim() === '') {
         textarea.removeClass('border-textarea-bg-light dark:border-textarea-bg-dark').addClass('border-textarea-border-empty-light dark:border-textarea-border-empty-dark');
     } else {
         textarea.removeClass('border-textarea-border-empty-light dark:border-textarea-border-empty-dark animate-[pulse_500ms_linear_infinite]').addClass('border-textarea-bg-light dark:border-textarea-bg-dark');
     }
 }
 
-function EditComment(form_id, settings_slug) {
+function EditComment(form_id, settings_slug, status_check) {
     let form = $(`#${form_id}`);
     let method = form.prop('method');
     let action = form.prop('action');
     let formData = {
         //FORM INPUTS
         content: $(`#${form_id} [name='content']`).val(),
         is_spoiler: $(`#${form_id} [name='is_spoiler']`).is(':checked'),
@@ -136,17 +139,18 @@
         url: action,
         headers: {
             "X-Requested-With": "XMLHttpRequest",
             "X-CSRFToken": getCookie("csrftoken"),
         },
         data: formData,
         success: function(data) {
-            if (data.urlhash) {
-                LoadComment(data.urlhash, settings_slug);
+            if (status_check) {
+                document.getElementById('toast').classList.remove('hidden');
             }
+            LoadComment(data.urlhash, settings_slug);
         },
         error: function() {
             let textarea = $(`#${form_id} textarea`);
             if (textarea.val().trim() === '') {
                 textarea.removeClass('border-textarea-bg-light dark:border-textarea-bg-dark').addClass('animate-[pulse_500ms_linear_infinite] border-textarea-border-empty-light dark:border-textarea-border-empty-dark');
             } else {
                 alert('ERROR in Creating Comment!')
@@ -193,12 +197,16 @@
         },
         success: function() {
             LoadCommentReactions(urlhash);
         }
     });
 }
 
+function CloseToast() {
+    document.getElementById('toast').classList.add('hidden');
+}
+
 $(document).ready(function() {
     // setTimeout(function () {
     LoadCommentList(undefined, true);
     // }, 100);
 });
```

### Comparing `django-comment-system-2.9.0/comment/static/comment/js/comment.min.js` & `django-comment-system-2.9.1/comment/static/comment/js/comment.min.js`

 * *Files 4% similar despite different names*

#### js-beautify {}

```diff
@@ -45,72 +45,72 @@
     a.find("textarea").val(t).removeClass("animate-[pulse_500ms_linear_infinite] border-textarea-border-empty-light dark:border-textarea-border-empty-dark").addClass("border-textarea-bg-light dark:border-textarea-bg-dark"), "True" === o ? a.find("[name='is_spoiler']").prop("checked", !0) : a.find("[name='is_spoiler']").prop("checked", !1)
 }
 
 function ResetDeleteCommentForm() {
     $("#comment-modal").html("")
 }
 
-function CreateComment(e) {
-    let t = $(`#${e}`),
-        o = t.prop("method"),
-        a = t.prop("action"),
-        r = {
+function CreateComment(e, t) {
+    let o = $(`#${e}`),
+        a = o.prop("method"),
+        r = o.prop("action"),
+        n = {
             app_name: $("#form-comment-create [name='app_name']").val(),
             model_name: $("#form-comment-create [name='model_name']").val(),
             content_type: $("#form-comment-create [name='content_type']").val(),
             object_id: $("#form-comment-create [name='object_id']").val(),
             settings_slug: $("#form-comment-create [name='settings_slug']").val(),
             content: $(`#${e} [name='content']`).val(),
             is_spoiler: $(`#${e} [name='is_spoiler']`).is(":checked"),
             parent_id: $(`#${e} [name='parent_id']`).val()
         };
     $.ajax({
-        type: o,
-        url: a,
+        type: a,
+        url: r,
         headers: {
             "X-Requested-With": "XMLHttpRequest",
             "X-CSRFToken": getCookie("csrftoken")
         },
-        data: r,
+        data: n,
         success: function() {
-            if (r.parent_id) {
-                LoadCommentList($(`#form-comment-reply-${r.parent_id} [name='page']`).val())
+            if (t && document.getElementById("toast").classList.remove("hidden"), n.parent_id) {
+                LoadCommentList($(`#form-comment-reply-${n.parent_id} [name='page']`).val())
             } else ResetCreateCommentForm(), LoadCommentList()
         },
         error: function() {
             "" !== $(`#${e} textarea`).val().trim() && alert("ERROR in Creating Comment!")
         }
     })
 }
 
 function CheckEditTextarea(e) {
     let t = $(`#${e} textarea`);
     "" === t.val().trim() ? t.removeClass("border-textarea-bg-light dark:border-textarea-bg-dark").addClass("border-textarea-border-empty-light dark:border-textarea-border-empty-dark") : t.removeClass("border-textarea-border-empty-light dark:border-textarea-border-empty-dark animate-[pulse_500ms_linear_infinite]").addClass("border-textarea-bg-light dark:border-textarea-bg-dark")
 }
 
-function EditComment(e, t) {
-    let o = $(`#${e}`),
-        a = o.prop("method"),
-        r = o.prop("action"),
-        n = {
+function EditComment(e, t, o) {
+    let a = $(`#${e}`),
+        r = a.prop("method"),
+        n = a.prop("action"),
+        m = {
             content: $(`#${e} [name='content']`).val(),
             is_spoiler: $(`#${e} [name='is_spoiler']`).is(":checked"),
             urlhash: e.replace("form-comment-edit-", ""),
             settings_slug: t
         };
     $.ajax({
-        type: a,
-        url: r,
+        type: r,
+        url: n,
         headers: {
             "X-Requested-With": "XMLHttpRequest",
             "X-CSRFToken": getCookie("csrftoken")
         },
-        data: n,
+        data: m,
         success: function(e) {
-            e.urlhash && LoadComment(e.urlhash, t)
+            o && document.getElementById("toast").classList.remove("hidden"), LoadComment(e.urlhash, t)
         },
         error: function() {
             let t = $(`#${e} textarea`);
             "" === t.val().trim() ? t.removeClass("border-textarea-bg-light dark:border-textarea-bg-dark").addClass("animate-[pulse_500ms_linear_infinite] border-textarea-border-empty-light dark:border-textarea-border-empty-dark") : alert("ERROR in Creating Comment!")
         }
     })
 }
@@ -151,10 +151,14 @@
             "X-CSRFToken": getCookie("csrftoken")
         },
         success: function() {
             LoadCommentReactions(e)
         }
     })
 }
+
+function CloseToast() {
+    document.getElementById("toast").classList.add("hidden")
+}
 $(document).ready((function() {
     LoadCommentList(void 0, !0)
 }));
```

### Comparing `django-comment-system-2.9.0/comment/static/comment/js/jquery.min.js` & `django-comment-system-2.9.1/comment/static/comment/js/jquery.min.js`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/tailwindcss/style.css` & `django-comment-system-2.9.1/comment/static/comment/tailwindcss/style.css`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/static/comment/tailwindcss/tailwind.config.js` & `django-comment-system-2.9.1/comment/static/comment/tailwindcss/tailwind.config.js`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/comment/comment_body.html` & `django-comment-system-2.9.1/comment/templates/comment/comment/comment_body.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/comment/comment_counter.html` & `django-comment-system-2.9.1/comment/templates/comment/comment/comment_counter.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/comment/comment_list.html` & `django-comment-system-2.9.1/comment/templates/comment/comment/comment_list.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/comment/comment_reactions.html` & `django-comment-system-2.9.1/comment/templates/comment/comment/comment_reactions.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/comment/comments.html` & `django-comment-system-2.9.1/comment/templates/comment/comment/comments.html`

 * *Files 9% similar despite different names*

```diff
@@ -17,8 +17,9 @@
         {# COMMENTS LIST #}
         <div id="comment-list">
             {% include 'comment/utils/comment_list_loader.html' %}
         </div>
 
     </div>
 </div>
+{% include 'comment/utils/toast.html' %}
 {% include 'comment/utils/SCRIPTS.html' %}
```

### Comparing `django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_create.html` & `django-comment-system-2.9.1/comment/templates/comment/forms/comment_form_create.html`

 * *Files 2% similar despite different names*

```diff
@@ -18,15 +18,15 @@
                         <input type="checkbox" name="is_spoiler" id="id_is_spoiler" class="peer sr-only"/>
                         {#ICON EYE#}
                         <span class="block cursor-pointer peer-checked:hidden">{% include 'comment/icons/icon_eye.html' with class='inline-block w-8 fill-none stroke-icon-spoiler-light dark:stroke-icon-spoiler-dark' %}</span>
                         {#ICON EYE OFF#}
                         <span class="hidden cursor-pointer peer-checked:block">{% include 'comment/icons/icon_eye_off.html' with class='inline-block w-8 fill-icon-spoiler-light dark:fill-icon-spoiler-dark' %}</span>
                     </label>
                 {% endif %}
-                <button type="button" onclick="CreateComment('form-comment-create')" class="rounded-lg border-none bg-btn-send-bg-light dark:bg-btn-send-bg-dark py-2 px-6 text-xl text-btn-send-text-light dark:text-btn-send-text-dark dark:font-semibold outline-0 shadow-md">{% trans 'Send' context 'form-button' %}</button>
+                <button type="button" onclick="CreateComment('form-comment-create','{{ settings.status_check }}')" class="rounded-lg border-none bg-btn-send-bg-light dark:bg-btn-send-bg-dark py-2 px-6 text-xl text-btn-send-text-light dark:text-btn-send-text-dark dark:font-semibold outline-0 shadow-md">{% trans 'Send' context 'form-button' %}</button>
             </div>
         {% else %}
             <div><a href="{% get_settings 'LOGIN_URL' %}" class="font-bold text-btn-login-text-light dark:text-btn-login-text-dark">{% trans 'Login to comment' context 'login-required' %}</a></div>
         {% endif %}
     </div>
 
 </form>
```

### Comparing `django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_delete.html` & `django-comment-system-2.9.1/comment/templates/comment/forms/comment_form_delete.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_edit.html` & `django-comment-system-2.9.1/comment/templates/comment/forms/comment_form_edit.html`

 * *Files 1% similar despite different names*

```diff
@@ -12,11 +12,11 @@
                     {#ICON EYE#}
                     <span class="block cursor-pointer peer-checked:hidden">{% include 'comment/icons/icon_eye.html' with class='inline-block w-8 fill-none stroke-icon-spoiler-light dark:stroke-icon-spoiler-dark' %}</span>
                     {#ICON EYE OFF#}
                     <span class="hidden cursor-pointer peer-checked:block">{% include 'comment/icons/icon_eye_off.html' with class='inline-block w-8 fill-icon-spoiler-light dark:fill-icon-spoiler-dark' %}</span>
                 </label>
             {% endif %}
             <label for="toggle-edit-{{ comment.urlhash }}" onclick="ResetEditCommentForm('form-comment-edit-{{ comment.urlhash }}','{{ comment.content_main }}','{{ comment.is_spoiler }}')" class="inline cursor-pointer rounded-lg border-none bg-btn-cancel-bg-light dark:bg-btn-cancel-bg-dark py-2 px-6 text-xl text-btn-cancel-text-light dark:text-btn-cancel-text-dark outline-0 shadow-md ltr:mr-2 rtl:ml-2">{% trans 'Cancel' context 'form-button' %}</label>
-            <button type="button" onclick="EditComment('form-comment-edit-{{ comment.urlhash }}','{{ settings.slug }}')" class="rounded-lg border-none bg-btn-edit-bg-light dark:bg-btn-edit-bg-dark py-2 px-6 text-xl text-btn-edit-text-light dark:text-btn-edit-text-dark outline-0 shadow-md">{% trans 'Edit' context 'form-button' %}</button>
+            <button type="button" onclick="EditComment('form-comment-edit-{{ comment.urlhash }}','{{ settings.slug }}','{{ settings.status_check }}')" class="rounded-lg border-none bg-btn-edit-bg-light dark:bg-btn-edit-bg-dark py-2 px-6 text-xl text-btn-edit-text-light dark:text-btn-edit-text-dark outline-0 shadow-md">{% trans 'Edit' context 'form-button' %}</button>
         </div>
     </div>
 </form>
```

### Comparing `django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_reply.html` & `django-comment-system-2.9.1/comment/templates/comment/forms/comment_form_reply.html`

 * *Files 2% similar despite different names*

```diff
@@ -22,15 +22,15 @@
                         <input type="checkbox" name="is_spoiler" id="id_is_spoiler" class="peer sr-only"/>
                         {#ICON EYE#}
                         <span class="block cursor-pointer peer-checked:hidden">{% include 'comment/icons/icon_eye.html' with class='inline-block w-8 fill-none stroke-icon-spoiler-light dark:stroke-icon-spoiler-dark' %}</span>
                         {#ICON EYE OFF#}
                         <span class="hidden cursor-pointer peer-checked:block">{% include 'comment/icons/icon_eye_off.html' with class='inline-block w-8 fill-icon-spoiler-light dark:fill-icon-spoiler-dark' %}</span>
                     </label>
                 {% endif %}
-                <button type="button" onclick="CreateComment('form-comment-reply-{{ comment.urlhash }}')" class="rounded-lg border-none py-2 px-6 text-xl outline-0 shadow-md bg-btn-reply-bg-light dark:bg-btn-reply-bg-dark text-btn-reply-text-light dark:text-btn-reply-text-dark">{% trans 'Reply' context 'form-button' %}</button>
+                <button type="button" onclick="CreateComment('form-comment-reply-{{ comment.urlhash }}','{{ settings.status_check }}')" class="rounded-lg border-none py-2 px-6 text-xl outline-0 shadow-md bg-btn-reply-bg-light dark:bg-btn-reply-bg-dark text-btn-reply-text-light dark:text-btn-reply-text-dark">{% trans 'Reply' context 'form-button' %}</button>
             </div>
         {% else %}
             <div><a href="{% get_settings 'LOGIN_URL' %}" class="font-bold text-btn-login-text-light dark:text-btn-login-text-dark">{% trans 'Login to reply' context 'login-required' %}</a></div>
         {% endif %}
     </div>
 
 </form>
```

### Comparing `django-comment-system-2.9.0/comment/templates/comment/icons/icon_delete.html` & `django-comment-system-2.9.1/comment/templates/comment/icons/icon_delete.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/icons/icon_edit.html` & `django-comment-system-2.9.1/comment/templates/comment/icons/icon_edit.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/icons/icon_eye_off.html` & `django-comment-system-2.9.1/comment/templates/comment/icons/icon_eye_off.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/icons/icon_pin.html` & `django-comment-system-2.9.1/comment/templates/comment/icons/icon_pin.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/utils/IMPORTS.html` & `django-comment-system-2.9.1/comment/templates/comment/utils/IMPORTS.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_empty.html` & `django-comment-system-2.9.1/comment/templates/comment/utils/comment_list_empty.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_loader.html` & `django-comment-system-2.9.1/comment/templates/comment/utils/comment_list_loader.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_pagination.html` & `django-comment-system-2.9.1/comment/templates/comment/utils/comment_list_pagination.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/templatetags/comment_tags.py` & `django-comment-system-2.9.1/comment/templatetags/comment_tags.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/comment/views.py` & `django-comment-system-2.9.1/comment/views.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.9.0/django_comment_system.egg-info/SOURCES.txt` & `django-comment-system-2.9.1/django_comment_system.egg-info/SOURCES.txt`

 * *Files 4% similar despite different names*

```diff
@@ -71,9 +71,10 @@
 comment/templates/comment/icons/icon_pin.html
 comment/templates/comment/icons/icon_up.html
 comment/templates/comment/utils/IMPORTS.html
 comment/templates/comment/utils/SCRIPTS.html
 comment/templates/comment/utils/comment_list_empty.html
 comment/templates/comment/utils/comment_list_loader.html
 comment/templates/comment/utils/comment_list_pagination.html
+comment/templates/comment/utils/toast.html
 comment/templatetags/__init__.py
 comment/templatetags/comment_tags.py
```

### Comparing `django-comment-system-2.9.0/setup.cfg` & `django-comment-system-2.9.1/setup.cfg`

 * *Files identical despite different names*

