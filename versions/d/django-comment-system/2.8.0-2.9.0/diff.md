# Comparing `tmp/django-comment-system-2.8.0.tar.gz` & `tmp/django-comment-system-2.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-comment-system-2.8.0.tar", last modified: Thu Apr  6 05:11:39 2023, max compression
+gzip compressed data, was "django-comment-system-2.9.0.tar", last modified: Thu Apr  6 20:58:43 2023, max compression
```

## Comparing `django-comment-system-2.8.0.tar` & `django-comment-system-2.9.0.tar`

### file list

```diff
@@ -1,104 +1,104 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.826503 django-comment-system-2.8.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      404 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3314 2023-04-06 05:11:39.826503 django-comment-system-2.8.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)    15276 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)     2659 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/README.rst
--rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/VERSION
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.810503 django-comment-system-2.8.0/comment/
--rw-r--r--   0 runner    (1001) docker     (123)      898 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4872 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/admin.py
--rw-r--r--   0 runner    (1001) docker     (123)      146 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/apps.py
--rw-r--r--   0 runner    (1001) docker     (123)      181 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/forms.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.806503 django-comment-system-2.8.0/comment/locale/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.806503 django-comment-system-2.8.0/comment/locale/fa/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.810503 django-comment-system-2.8.0/comment/locale/fa/LC_MESSAGES/
--rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/locale/fa/LC_MESSAGES/django.mo
--rw-r--r--   0 runner    (1001) docker     (123)     3498 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/locale/fa/LC_MESSAGES/django.po
--rw-r--r--   0 runner    (1001) docker     (123)     1244 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/managers.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.810503 django-comment-system-2.8.0/comment/migrations/
--rw-r--r--   0 runner    (1001) docker     (123)     5259 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/migrations/0001_initial.py
--rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/migrations/0002_config.py
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/migrations/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      513 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/mixins.py
--rw-r--r--   0 runner    (1001) docker     (123)     5054 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/models.py
--rw-r--r--   0 runner    (1001) docker     (123)      442 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/settings.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.806503 django-comment-system-2.8.0/comment/static/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.806503 django-comment-system-2.8.0/comment/static/comment/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.814503 django-comment-system-2.8.0/comment/static/comment/css/
--rw-r--r--   0 runner    (1001) docker     (123)    40199 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/css/style.css
--rw-r--r--   0 runner    (1001) docker     (123)    32347 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/css/style.min.css
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.806503 django-comment-system-2.8.0/comment/static/comment/font/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.814503 django-comment-system-2.8.0/comment/static/comment/font/Vazir/
--rw-r--r--   0 runner    (1001) docker     (123)    50568 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Black.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51020 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Bold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51120 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraBold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51268 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraLight.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51180 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Light.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51128 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Medium.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    50684 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Regular.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    51032 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-SemiBold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    50796 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Thin.woff2
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.818503 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/
--rw-r--r--   0 runner    (1001) docker     (123)    49100 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Black.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49868 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Bold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49628 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49816 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49712 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Light.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49784 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Medium.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49044 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Regular.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49608 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2
--rw-r--r--   0 runner    (1001) docker     (123)    49556 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Thin.woff2
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.818503 django-comment-system-2.8.0/comment/static/comment/img/
--rw-r--r--   0 runner    (1001) docker     (123)     3602 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/img/profile.png
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.818503 django-comment-system-2.8.0/comment/static/comment/js/
--rw-r--r--   0 runner    (1001) docker     (123)     7734 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/js/comment-no-jquery-no-tested.js
--rw-r--r--   0 runner    (1001) docker     (123)     6996 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/js/comment.js
--rw-r--r--   0 runner    (1001) docker     (123)     4307 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/js/comment.min.js
--rw-r--r--   0 runner    (1001) docker     (123)    89574 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/js/jquery.min.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.818503 django-comment-system-2.8.0/comment/static/comment/tailwindcss/
--rw-r--r--   0 runner    (1001) docker     (123)     4764 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/tailwindcss/style.css
--rw-r--r--   0 runner    (1001) docker     (123)     7389 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/static/comment/tailwindcss/tailwind.config.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.806503 django-comment-system-2.8.0/comment/templates/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.806503 django-comment-system-2.8.0/comment/templates/comment/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.822503 django-comment-system-2.8.0/comment/templates/comment/comment/
--rw-r--r--   0 runner    (1001) docker     (123)     7842 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/comment/comment_body.html
--rw-r--r--   0 runner    (1001) docker     (123)      595 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/comment/comment_counter.html
--rw-r--r--   0 runner    (1001) docker     (123)     2161 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/comment/comment_list.html
--rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/comment/comment_reactions.html
--rw-r--r--   0 runner    (1001) docker     (123)      765 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/comment/comments.html
--rw-r--r--   0 runner    (1001) docker     (123)      411 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/comment/object_info.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.822503 django-comment-system-2.8.0/comment/templates/comment/forms/
--rw-r--r--   0 runner    (1001) docker     (123)     2463 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/forms/comment_form_create.html
--rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/forms/comment_form_delete.html
--rw-r--r--   0 runner    (1001) docker     (123)     2644 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/forms/comment_form_edit.html
--rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/forms/comment_form_reply.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.822503 django-comment-system-2.8.0/comment/templates/comment/icons/
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_arrow_backward.html
--rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_arrow_forward.html
--rw-r--r--   0 runner    (1001) docker     (123)      629 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_delete.html
--rw-r--r--   0 runner    (1001) docker     (123)      205 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_dots.html
--rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_down.html
--rw-r--r--   0 runner    (1001) docker     (123)      672 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_edit.html
--rw-r--r--   0 runner    (1001) docker     (123)      447 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_eye.html
--rw-r--r--   0 runner    (1001) docker     (123)     1163 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_eye_off.html
--rw-r--r--   0 runner    (1001) docker     (123)      280 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_pen.html
--rw-r--r--   0 runner    (1001) docker     (123)      706 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_pin.html
--rw-r--r--   0 runner    (1001) docker     (123)      264 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/icons/icon_up.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.822503 django-comment-system-2.8.0/comment/templates/comment/utils/
--rw-r--r--   0 runner    (1001) docker     (123)      551 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/utils/IMPORTS.html
--rw-r--r--   0 runner    (1001) docker     (123)       82 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/utils/SCRIPTS.html
--rw-r--r--   0 runner    (1001) docker     (123)     2340 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/utils/comment_list_empty.html
--rw-r--r--   0 runner    (1001) docker     (123)     1564 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/utils/comment_list_loader.html
--rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templates/comment/utils/comment_list_pagination.html
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.826503 django-comment-system-2.8.0/comment/templatetags/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templatetags/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2507 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/templatetags/comment_tags.py
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/tests.py
--rw-r--r--   0 runner    (1001) docker     (123)      511 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/urls.py
--rw-r--r--   0 runner    (1001) docker     (123)     5953 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/comment/views.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 05:11:39.826503 django-comment-system-2.8.0/django_comment_system.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3347 2023-04-06 05:11:39.000000 django-comment-system-2.8.0/django_comment_system.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      890 2023-04-06 05:11:39.826503 django-comment-system-2.8.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       36 2023-04-06 05:11:34.000000 django-comment-system-2.8.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/
+-rw-r--r--   0 runner    (1001) docker     (123)     1068 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      404 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3314 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)    15470 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)     2659 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/README.rst
+-rw-r--r--   0 runner    (1001) docker     (123)        5 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/VERSION
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/
+-rw-r--r--   0 runner    (1001) docker     (123)      898 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6063 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/admin.py
+-rw-r--r--   0 runner    (1001) docker     (123)      146 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/apps.py
+-rw-r--r--   0 runner    (1001) docker     (123)      181 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/forms.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/locale/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/locale/fa/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/
+-rw-r--r--   0 runner    (1001) docker     (123)     1732 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/django.mo
+-rw-r--r--   0 runner    (1001) docker     (123)     3498 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/django.po
+-rw-r--r--   0 runner    (1001) docker     (123)     1244 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/managers.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/migrations/
+-rw-r--r--   0 runner    (1001) docker     (123)     5259 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/migrations/0001_initial.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1467 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/migrations/0002_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)      980 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/migrations/0003_comment_content_main_comment_status_edited_and_more.py
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/migrations/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      513 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/mixins.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5572 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/models.py
+-rw-r--r--   0 runner    (1001) docker     (123)      442 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/settings.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/static/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/static/comment/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/static/comment/css/
+-rw-r--r--   0 runner    (1001) docker     (123)    40199 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/css/style.css
+-rw-r--r--   0 runner    (1001) docker     (123)    32347 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/css/style.min.css
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/static/comment/font/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/static/comment/font/Vazir/
+-rw-r--r--   0 runner    (1001) docker     (123)    50568 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Black.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51020 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Bold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51120 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraBold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51268 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraLight.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51180 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Light.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51128 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Medium.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    50684 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Regular.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    51032 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-SemiBold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    50796 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Thin.woff2
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/
+-rw-r--r--   0 runner    (1001) docker     (123)    49100 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Black.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49868 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Bold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49628 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49816 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49712 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Light.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49784 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Medium.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49044 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Regular.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49608 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2
+-rw-r--r--   0 runner    (1001) docker     (123)    49556 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Thin.woff2
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.551305 django-comment-system-2.9.0/comment/static/comment/img/
+-rw-r--r--   0 runner    (1001) docker     (123)     3602 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/img/profile.png
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/static/comment/js/
+-rw-r--r--   0 runner    (1001) docker     (123)     7034 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/js/comment.js
+-rw-r--r--   0 runner    (1001) docker     (123)     4323 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/js/comment.min.js
+-rw-r--r--   0 runner    (1001) docker     (123)    89574 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/js/jquery.min.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/static/comment/tailwindcss/
+-rw-r--r--   0 runner    (1001) docker     (123)     4764 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/tailwindcss/style.css
+-rw-r--r--   0 runner    (1001) docker     (123)     7389 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/static/comment/tailwindcss/tailwind.config.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/templates/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.547305 django-comment-system-2.9.0/comment/templates/comment/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templates/comment/comment/
+-rw-r--r--   0 runner    (1001) docker     (123)     7862 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comment_body.html
+-rw-r--r--   0 runner    (1001) docker     (123)      595 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comment_counter.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2161 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comment_list.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comment_reactions.html
+-rw-r--r--   0 runner    (1001) docker     (123)      765 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/comments.html
+-rw-r--r--   0 runner    (1001) docker     (123)      411 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/comment/object_info.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templates/comment/forms/
+-rw-r--r--   0 runner    (1001) docker     (123)     2463 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_create.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2630 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_delete.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2654 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_edit.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2655 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_reply.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templates/comment/icons/
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_arrow_backward.html
+-rw-r--r--   0 runner    (1001) docker     (123)      275 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_arrow_forward.html
+-rw-r--r--   0 runner    (1001) docker     (123)      629 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_delete.html
+-rw-r--r--   0 runner    (1001) docker     (123)      205 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_dots.html
+-rw-r--r--   0 runner    (1001) docker     (123)      229 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_down.html
+-rw-r--r--   0 runner    (1001) docker     (123)      672 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_edit.html
+-rw-r--r--   0 runner    (1001) docker     (123)      447 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_eye.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1163 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_eye_off.html
+-rw-r--r--   0 runner    (1001) docker     (123)      280 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_pen.html
+-rw-r--r--   0 runner    (1001) docker     (123)      706 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_pin.html
+-rw-r--r--   0 runner    (1001) docker     (123)      264 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/icons/icon_up.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templates/comment/utils/
+-rw-r--r--   0 runner    (1001) docker     (123)      551 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/IMPORTS.html
+-rw-r--r--   0 runner    (1001) docker     (123)       82 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/SCRIPTS.html
+-rw-r--r--   0 runner    (1001) docker     (123)     2340 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_empty.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1564 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_loader.html
+-rw-r--r--   0 runner    (1001) docker     (123)     1896 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_pagination.html
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/comment/templatetags/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templatetags/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2507 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/templatetags/comment_tags.py
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/tests.py
+-rw-r--r--   0 runner    (1001) docker     (123)      511 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/urls.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6423 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/comment/views.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:58:43.555305 django-comment-system-2.9.0/django_comment_system.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3369 2023-04-06 20:58:43.000000 django-comment-system-2.9.0/django_comment_system.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      890 2023-04-06 20:58:43.559306 django-comment-system-2.9.0/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       36 2023-04-06 20:58:40.000000 django-comment-system-2.9.0/setup.py
```

### Comparing `django-comment-system-2.8.0/LICENSE` & `django-comment-system-2.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/PKG-INFO` & `django-comment-system-2.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-comment-system
-Version: 2.8.0
+Version: 2.9.0
 Summary: Django Comment System, It can be associated with any given model.
 Home-page: https://github.com/mahyar-amiri/django-comment-system
 Author: Mahyar Amiri
 Author-email: mmaahhyyaarr@gmail.com
 License: MIT
 Project-URL: Documentation, https://github.com/mahyar-amiri/django-comment-system/README.md
 Project-URL: Source Code, https://github.com/mahyar-amiri/django-comment-system
```

### Comparing `django-comment-system-2.8.0/README.md` & `django-comment-system-2.9.0/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -136,27 +136,31 @@
     # if None, comments will be shown without profile image
     # you should set this value as profile image field name
     # for example our abstract user profile picture field is profile_image
     # <img src="{{ user.profile_image.url }}" /> so we set PROFILE_IMAGE_FIELD = 'profile.image'
     # see link blew to create abstract user model
     # https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#substituting-a-custom-user-model
     'PROFILE_IMAGE_FIELD': None,
-    # default profile image static path
-    'PROFILE_IMAGE_DEFAULT': 'img/profile.png'
 }
 ```
 
 ### Config Settings
 
 This settings can be configured in admin panel. Set your config in `CommentSettings` model.
 
 ```python
+# image file for default profile image, it null the image will not be shown
+DEFAULT_PROFILE_IMAGE
+
 # the comments need to be set as a(Accepted) to be shown in the comments list.
 # if True, comment status will be set as d(Delivered) otherwise it will be set as a(Accepted).
 STATUS_CHECK = False
+# the comments need to be set as a(Accepted) to be edited.
+# if True, comment status will be set as d(Delivered) otherwise it will be set as a(Accepted).
+STATUS_EDITED_CHECK = False
 
 # activate spoiler comment mode
 ALLOW_SPOILER = True
 # let users reply to a comment
 ALLOW_REPLY = True
 # let users edit their comment
 ALLOW_EDIT = True
```

### Comparing `django-comment-system-2.8.0/README.rst` & `django-comment-system-2.9.0/README.rst`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/__init__.py` & `django-comment-system-2.9.0/comment/__init__.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/admin.py` & `django-comment-system-2.9.0/comment/admin.py`

 * *Files 24% similar despite different names*

```diff
@@ -35,20 +35,20 @@
             if self.value() == 'updated':
                 return queryset.filter_updated()
             elif self.value() == 'not_updated':
                 return queryset.filter_not_updated()
 
 
 class CommentAdmin(admin.ModelAdmin):
-    list_display = ('__str__', 'user', 'is_spoiler', 'is_pinned', 'is_updated', 'status', 'content_object', 'posted')
+    list_display = ('__str__', 'content', 'user', 'is_spoiler', 'is_pinned', 'is_updated', 'status', 'status_edited', 'content_object', 'posted', 'updated')
     ordering = ('-is_pinned', '-posted',)
     search_fields = ('content',)
-    list_filter = ('is_spoiler', 'is_pinned', ListFilterByUpdated, 'status', ListFilterByParent)
-    readonly_fields = ('user', 'content', 'parent', 'content_type', 'content_object', 'object_id', 'urlhash', 'posted', 'is_spoiler', 'is_pinned', 'status')
-    actions = ['accept_comment', 'reject_comment', 'pin_comment', 'unpin_comment', 'set_spoiler_comment', 'unset_spoiler_comment']
+    list_filter = ('is_spoiler', 'is_pinned', ListFilterByUpdated, 'status', 'status_edited', ListFilterByParent)
+    readonly_fields = ('user', 'content_main', 'content', 'parent', 'content_type', 'content_object', 'object_id', 'urlhash', 'posted', 'is_spoiler', 'is_pinned', 'status', 'status_edited')
+    actions = ['accept_comment', 'reject_comment', 'accept_edited_comment', 'reject_edited_comment', 'pin_comment', 'unpin_comment', 'set_spoiler_comment', 'unset_spoiler_comment']
 
     def accept_comment(self, request, queryset):
         accepted = queryset.update(status='a')
         self.message_user(request,
                           ngettext(f'{accepted} comment accepted.',
                                    f'{accepted} comments accepted.', accepted),
                           messages.SUCCESS)
@@ -60,14 +60,38 @@
         self.message_user(request,
                           ngettext(f'{rejected} comment rejected.',
                                    f'{rejected} comments rejected.', rejected),
                           messages.WARNING)
 
     reject_comment.short_description = 'Reject selected comments'
 
+    def accept_edited_comment(self, request, queryset):
+        for comment in queryset:
+            comment.content_main = comment.content
+            comment.save()
+        edited = queryset.update(status_edited='a')
+        self.message_user(request,
+                          ngettext(f'{edited} comment edited.',
+                                   f'{edited} comments edited.', edited),
+                          messages.SUCCESS)
+
+    accept_edited_comment.short_description = 'Accept edit for selected comments'
+
+    def reject_edited_comment(self, request, queryset):
+        for comment in queryset:
+            comment.content = comment.content_main
+            comment.save()
+        edited = queryset.update(status_edited='r')
+        self.message_user(request,
+                          ngettext(f'{edited} comment did not edit.',
+                                   f'{edited} comments did not edit.', edited),
+                          messages.WARNING)
+
+    reject_edited_comment.short_description = 'Reject edit for selected comments'
+
     def pin_comment(self, request, queryset):
         pinned = queryset.update(is_pinned=True)
         self.message_user(request,
                           ngettext(f'{pinned} comment pinned.',
                                    f'{pinned} comments pinned.', pinned),
                           messages.SUCCESS)
```

### Comparing `django-comment-system-2.8.0/comment/locale/fa/LC_MESSAGES/django.mo` & `django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/locale/fa/LC_MESSAGES/django.po` & `django-comment-system-2.9.0/comment/locale/fa/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/managers.py` & `django-comment-system-2.9.0/comment/managers.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/migrations/0001_initial.py` & `django-comment-system-2.9.0/comment/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/migrations/0002_config.py` & `django-comment-system-2.9.0/comment/migrations/0002_config.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/mixins.py` & `django-comment-system-2.9.0/comment/mixins.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/models.py` & `django-comment-system-2.9.0/comment/models.py`

 * *Files 8% similar despite different names*

```diff
@@ -12,14 +12,15 @@
 class CommentSettings(models.Model):
     name = models.CharField(max_length=30)
     slug = models.SlugField(primary_key=True, help_text='This value will be used in render_comments tag')
 
     default_profile_image = models.ImageField(upload_to='comment_default_profile_images', null=True, blank=True)
     content_words_count = models.PositiveSmallIntegerField(default=40, help_text='More than this value will have Read More button in comment content')
     status_check = models.BooleanField(default=False, help_text='If True, comment status will be set as d(Delivered) otherwise it will be set as a(Accepted).')
+    status_edited_check = models.BooleanField(default=False, help_text='If True, comment status_edited will be set as d(Delivered) otherwise it will be set as a(Accepted) when a comment is edited.')
     allow_spoiler = models.BooleanField(default=True)
     allow_reply = models.BooleanField(default=True)
     allow_edit = models.BooleanField(default=True)
     allow_delete = models.BooleanField(default=True)
     allow_reaction = models.BooleanField(default=True, help_text='First, create a react emoji in React models')
     reaction_type = models.CharField(max_length=6, choices=(('emoji', 'Emoji'), ('source', 'Source')), default='emoji', help_text='Add source in React model')
     per_page = models.PositiveSmallIntegerField(default=10, help_text='Set 0 if you don\'t want pagination (All comments will be shown at once)')
@@ -34,20 +35,23 @@
 
     def __str__(self):
         return f'{self.name} - [{self.slug}]'
 
 
 class Comment(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
-    content = models.TextField()
+    content_main = models.TextField()
+    content = models.TextField()  # edited content will store here
     parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', null=True, blank=True)
     is_spoiler = models.BooleanField(default=False)
     is_pinned = models.BooleanField(default=False)
     STATUS_CHOICES = (('d', 'Delivered'), ('a', 'Accepted'), ('r', 'Rejected'))
     status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
+    STATUS_EDITED_CHOICES = (('n', 'None'), ('d', 'Delivered'), ('a', 'Accepted'), ('r', 'Rejected'))
+    status_edited = models.CharField(max_length=1, choices=STATUS_EDITED_CHOICES, default='n')
     urlhash = models.CharField(max_length=50, unique=True, editable=False)
     posted = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)
 
     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
     object_id = models.PositiveIntegerField()
     content_object = GenericForeignKey('content_type', 'object_id')
@@ -55,30 +59,30 @@
     objects = CommentQuerySet.as_manager()
 
     class Meta:
         ordering = ('-is_pinned', '-posted')
 
     def __str__(self):
         if not self.parent:
-            return f'{self.content[:20]}'
+            return f'{self.content_main[:20]}'
         else:
-            return f'[RE] ({self.parent.content[:10]}) : {self.content[:15]}'
+            return f'[RE] ({self.parent.content_main[:10]}) : {self.content_main[:15]}'
 
     def set_unique_urlhash(self):
         if not self.urlhash:
             self.urlhash = self.__class__.objects.generate_urlhash()
             while self.__class__.objects.filter(urlhash=self.urlhash).exists():
                 self.urlhash = self.__class__.objects.generate_urlhash()
 
     def save(self, *args, **kwargs):
         self.set_unique_urlhash()
         super(Comment, self).save(*args, **kwargs)
 
     def is_updated(self):
-        return True if self.updated.timestamp() > self.posted.timestamp() else False
+        return True if self.updated.timestamp() > self.posted.timestamp() and self.status_edited != 'n' else False
 
     is_updated.boolean = True
 
     @property
     def is_parent(self):
         return self.parent is None
 
@@ -102,8 +106,8 @@
 
     objects = ReactionQuerySet.as_manager()
 
     class Meta:
         unique_together = ['user', 'comment']
 
     def __str__(self):
-        return f'{self.user} <{self.react.slug}> ({self.comment.content[:20]})'
+        return f'{self.user} <{self.react.slug}> ({self.comment.content_main[:20]})'
```

### Comparing `django-comment-system-2.8.0/comment/static/comment/css/style.css` & `django-comment-system-2.9.0/comment/static/comment/css/style.css`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/css/style.min.css` & `django-comment-system-2.9.0/comment/static/comment/css/style.min.css`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Black.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Black.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Bold.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Bold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraBold.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraBold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraLight.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-ExtraLight.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Light.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Light.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Medium.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Medium.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Regular.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Regular.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-SemiBold.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-SemiBold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir/Vazirmatn-Thin.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir/Vazirmatn-Thin.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Black.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Black.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Bold.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Bold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraBold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Light.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Light.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Medium.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Medium.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Regular.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Regular.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Thin.woff2` & `django-comment-system-2.9.0/comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Thin.woff2`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/img/profile.png` & `django-comment-system-2.9.0/comment/static/comment/img/profile.png`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/js/comment.js` & `django-comment-system-2.9.0/comment/static/comment/js/comment.js`

 * *Files 1% similar despite different names*

#### js-beautify {}

```diff
@@ -125,14 +125,15 @@
     let method = form.prop('method');
     let action = form.prop('action');
     let formData = {
         //FORM INPUTS
         content: $(`#${form_id} [name='content']`).val(),
         is_spoiler: $(`#${form_id} [name='is_spoiler']`).is(':checked'),
         urlhash: form_id.replace('form-comment-edit-', ''),
+        settings_slug: settings_slug,
     };
     $.ajax({
         type: method,
         url: action,
         headers: {
             "X-Requested-With": "XMLHttpRequest",
             "X-CSRFToken": getCookie("csrftoken"),
```

### Comparing `django-comment-system-2.8.0/comment/static/comment/js/comment.min.js` & `django-comment-system-2.9.0/comment/static/comment/js/comment.min.js`

 * *Files 0% similar despite different names*

#### js-beautify {}

```diff
@@ -90,15 +90,16 @@
 function EditComment(e, t) {
     let o = $(`#${e}`),
         a = o.prop("method"),
         r = o.prop("action"),
         n = {
             content: $(`#${e} [name='content']`).val(),
             is_spoiler: $(`#${e} [name='is_spoiler']`).is(":checked"),
-            urlhash: e.replace("form-comment-edit-", "")
+            urlhash: e.replace("form-comment-edit-", ""),
+            settings_slug: t
         };
     $.ajax({
         type: a,
         url: r,
         headers: {
             "X-Requested-With": "XMLHttpRequest",
             "X-CSRFToken": getCookie("csrftoken")
```

### Comparing `django-comment-system-2.8.0/comment/static/comment/js/jquery.min.js` & `django-comment-system-2.9.0/comment/static/comment/js/jquery.min.js`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/tailwindcss/style.css` & `django-comment-system-2.9.0/comment/static/comment/tailwindcss/style.css`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/static/comment/tailwindcss/tailwind.config.js` & `django-comment-system-2.9.0/comment/static/comment/tailwindcss/tailwind.config.js`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/comment/comment_body.html` & `django-comment-system-2.9.0/comment/templates/comment/comment/comment_body.html`

 * *Files 2% similar despite different names*

```diff
@@ -65,22 +65,22 @@
 
 {#COMMENT SECTION#}
 <div class="mt-2 {% if comment.is_spoiler and not comment.user == request.user %}hidden peer-checked:block{% endif %}">
     {#COMMENT CONTENT#}
     {% if settings.allow_edit %}<input type="checkbox" class="peer sr-only" id="toggle-edit-{{ comment.urlhash }}">{% endif %}
     <div class="p-2 text-justify block peer-checked:hidden">
         {#CONTENT#}
-        {% if comment.content|wordcount > settings.content_words_count %}
+        {% if comment.content_main|wordcount > settings.content_words_count %}
             <input type="checkbox" class="peer sr-only" id="toggle-more-{{ comment.urlhash }}">
-            <div class="whitespace-pre-wrap text-black dark:text-white inline-block peer-checked:hidden {% if LANGUAGE_CODE == 'fa-ir' %}font-default-fd{% else %}font-default{% endif %}">{{ comment.content|truncatewords:settings.content_words_count }}</div>
-            <div class="whitespace-pre-wrap text-black dark:text-white hidden peer-checked:block {% if LANGUAGE_CODE == 'fa-ir' %}font-default-fd{% else %}font-default{% endif %}">{{ comment.content }}</div>
+            <div class="whitespace-pre-wrap text-black dark:text-white inline-block peer-checked:hidden {% if LANGUAGE_CODE == 'fa-ir' %}font-default-fd{% else %}font-default{% endif %}">{{ comment.content_main|truncatewords:settings.content_words_count }}</div>
+            <div class="whitespace-pre-wrap text-black dark:text-white hidden peer-checked:block {% if LANGUAGE_CODE == 'fa-ir' %}font-default-fd{% else %}font-default{% endif %}">{{ comment.content_main }}</div>
             <label for="toggle-more-{{ comment.urlhash }}" class="inline peer-checked:hidden cursor-pointer text-comment-read-more-light dark:text-comment-read-more-dark">{% trans 'Read More' %} {% include 'comment/icons/icon_down.html' with class='w-6 inline-block' %}</label>
             <label for="toggle-more-{{ comment.urlhash }}" class="hidden peer-checked:block cursor-pointer text-comment-read-more-light dark:text-comment-read-more-dark">{% trans 'Read Less' %} {% include 'comment/icons/icon_up.html' with class='w-6 inline-block' %}</label>
         {% else %}
-            <div class="whitespace-pre-wrap text-black dark:text-white {% if LANGUAGE_CODE == 'fa-ir' %}font-default-fd{% else %}font-default{% endif %}">{{ comment.content }}</div>
+            <div class="whitespace-pre-wrap text-black dark:text-white {% if LANGUAGE_CODE == 'fa-ir' %}font-default-fd{% else %}font-default{% endif %}">{{ comment.content_main }}</div>
         {% endif %}
     </div>
     <div class="text-justify hidden peer-checked:block">
         {% if request.user.is_authenticated and comment.user == request.user and settings.allow_edit %}
             {% include 'comment/forms/comment_form_edit.html' with comment=comment settings=settings %}
         {% endif %}
     </div>
```

### Comparing `django-comment-system-2.8.0/comment/templates/comment/comment/comment_counter.html` & `django-comment-system-2.9.0/comment/templates/comment/comment/comment_counter.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/comment/comment_list.html` & `django-comment-system-2.9.0/comment/templates/comment/comment/comment_list.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/comment/comment_reactions.html` & `django-comment-system-2.9.0/comment/templates/comment/comment/comment_reactions.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/comment/comments.html` & `django-comment-system-2.9.0/comment/templates/comment/comment/comments.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/forms/comment_form_create.html` & `django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_create.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/forms/comment_form_delete.html` & `django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_delete.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/forms/comment_form_edit.html` & `django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_edit.html`

 * *Files 6% similar despite different names*

```diff
@@ -1,22 +1,22 @@
 {% load i18n %}
 
 <form id="form-comment-edit-{{ comment.urlhash }}" method="post" action="{% url 'comment:update' pk=comment.pk %}">{% csrf_token %}
     <div class="block rounded-lg bg-textarea-bg-light dark:bg-textarea-bg-dark pb-4 pt-1 ltr:pr-4 rtl:pl-4 ltr:pl-1 rtl:pr-1">
-        <textarea name="content" oninput="CheckEditTextarea('form-comment-edit-{{ comment.urlhash }}')" spellcheck="false" class="p-1 rounded-md block w-full border-2 resize-y bg-transparent box-border text-base mb-2 outline-0 min-h-[66px] text-textarea-text-light dark:text-textarea-text-dark border-textarea-bg-light dark:border-textarea-bg-dark selection:bg-textarea-text-selection-light dark:selection:bg-text-selection-dark placeholder:text-textarea-text-placeholder-light dark:placeholder:text-textarea-text-placeholder-dark {% if LANGUAGE_CODE == 'fa-ir' %}font-default-fd{% else %}font-default{% endif %}">{{ comment.content }}</textarea>
+        <textarea name="content" oninput="CheckEditTextarea('form-comment-edit-{{ comment.urlhash }}')" spellcheck="false" class="p-1 rounded-md block w-full border-2 resize-y bg-transparent box-border text-base mb-2 outline-0 min-h-[66px] text-textarea-text-light dark:text-textarea-text-dark border-textarea-bg-light dark:border-textarea-bg-dark selection:bg-textarea-text-selection-light dark:selection:bg-text-selection-dark placeholder:text-textarea-text-placeholder-light dark:placeholder:text-textarea-text-placeholder-dark {% if LANGUAGE_CODE == 'fa-ir' %}font-default-fd{% else %}font-default{% endif %}">{{ comment.content_main }}</textarea>
 
         <div class="flex justify-end">
             {#ALLOW_SPOILER#}
             {% if settings.allow_spoiler %}
                 <label class="ltr:mr-4 rtl:ml-4 grid content-center">
                     <input type="checkbox" name="is_spoiler" id="id_is_spoiler" class="peer sr-only" {% if comment.is_spoiler %}checked="checked"{% endif %}/>
                     {#ICON EYE#}
                     <span class="block cursor-pointer peer-checked:hidden">{% include 'comment/icons/icon_eye.html' with class='inline-block w-8 fill-none stroke-icon-spoiler-light dark:stroke-icon-spoiler-dark' %}</span>
                     {#ICON EYE OFF#}
                     <span class="hidden cursor-pointer peer-checked:block">{% include 'comment/icons/icon_eye_off.html' with class='inline-block w-8 fill-icon-spoiler-light dark:fill-icon-spoiler-dark' %}</span>
                 </label>
             {% endif %}
-            <label for="toggle-edit-{{ comment.urlhash }}" onclick="ResetEditCommentForm('form-comment-edit-{{ comment.urlhash }}','{{ comment.content }}','{{ comment.is_spoiler }}')" class="inline cursor-pointer rounded-lg border-none bg-btn-cancel-bg-light dark:bg-btn-cancel-bg-dark py-2 px-6 text-xl text-btn-cancel-text-light dark:text-btn-cancel-text-dark outline-0 shadow-md ltr:mr-2 rtl:ml-2">{% trans 'Cancel' context 'form-button' %}</label>
+            <label for="toggle-edit-{{ comment.urlhash }}" onclick="ResetEditCommentForm('form-comment-edit-{{ comment.urlhash }}','{{ comment.content_main }}','{{ comment.is_spoiler }}')" class="inline cursor-pointer rounded-lg border-none bg-btn-cancel-bg-light dark:bg-btn-cancel-bg-dark py-2 px-6 text-xl text-btn-cancel-text-light dark:text-btn-cancel-text-dark outline-0 shadow-md ltr:mr-2 rtl:ml-2">{% trans 'Cancel' context 'form-button' %}</label>
             <button type="button" onclick="EditComment('form-comment-edit-{{ comment.urlhash }}','{{ settings.slug }}')" class="rounded-lg border-none bg-btn-edit-bg-light dark:bg-btn-edit-bg-dark py-2 px-6 text-xl text-btn-edit-text-light dark:text-btn-edit-text-dark outline-0 shadow-md">{% trans 'Edit' context 'form-button' %}</button>
         </div>
     </div>
 </form>
```

### Comparing `django-comment-system-2.8.0/comment/templates/comment/forms/comment_form_reply.html` & `django-comment-system-2.9.0/comment/templates/comment/forms/comment_form_reply.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/icons/icon_delete.html` & `django-comment-system-2.9.0/comment/templates/comment/icons/icon_delete.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/icons/icon_edit.html` & `django-comment-system-2.9.0/comment/templates/comment/icons/icon_edit.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/icons/icon_eye_off.html` & `django-comment-system-2.9.0/comment/templates/comment/icons/icon_eye_off.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/icons/icon_pin.html` & `django-comment-system-2.9.0/comment/templates/comment/icons/icon_pin.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/utils/IMPORTS.html` & `django-comment-system-2.9.0/comment/templates/comment/utils/IMPORTS.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/utils/comment_list_empty.html` & `django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_empty.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/utils/comment_list_loader.html` & `django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_loader.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templates/comment/utils/comment_list_pagination.html` & `django-comment-system-2.9.0/comment/templates/comment/utils/comment_list_pagination.html`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/templatetags/comment_tags.py` & `django-comment-system-2.9.0/comment/templatetags/comment_tags.py`

 * *Files identical despite different names*

### Comparing `django-comment-system-2.8.0/comment/views.py` & `django-comment-system-2.9.0/comment/views.py`

 * *Files 9% similar despite different names*

```diff
@@ -66,14 +66,15 @@
 class CommentCreate(CommentMixin, CreateView):
     def post(self, request, *args, **kwargs):
         form = CommentForm(data=request.POST)
         if form.is_valid():
             comment = form.save(commit=False)
 
             comment.user = request.user
+            comment.content_main = comment.content
             app_name = request.POST.get('app_name', None)
             model_name = request.POST.get('model_name', None)
             object_id = request.POST.get('object_id', None)
             parent_id = request.POST.get('parent_id', None)
             settings_slug = request.POST.get('settings_slug', None)
             comment_settings = CommentSettings.objects.get(slug=settings_slug)
             time_posted = timezone.now()
@@ -99,14 +100,26 @@
 class CommentUpdate(CommentMixin, UpdateView):
     model = Comment
     form_class = CommentForm
     success_url = '/'
 
     def form_valid(self, form):
         super().form_valid(form)
+
+        settings_slug = self.request.POST.get('settings_slug', None)
+        comment_settings = CommentSettings.objects.get(slug=settings_slug)
+
+        if comment_settings.status_edited_check:
+            self.object.status_edited = 'd'
+            self.object.save()
+        else:
+            self.object.status_edited = 'a'
+            self.object.content_main = self.object.content
+            self.object.save()
+
         return JsonResponse({'urlhash': self.object.urlhash}, status=200)
 
     def form_invalid(self, form):
         super().form_invalid(form)
         return HttpResponseBadRequest()
```

### Comparing `django-comment-system-2.8.0/django_comment_system.egg-info/SOURCES.txt` & `django-comment-system-2.9.0/django_comment_system.egg-info/SOURCES.txt`

 * *Files 2% similar despite different names*

```diff
@@ -17,14 +17,15 @@
 comment/tests.py
 comment/urls.py
 comment/views.py
 comment/locale/fa/LC_MESSAGES/django.mo
 comment/locale/fa/LC_MESSAGES/django.po
 comment/migrations/0001_initial.py
 comment/migrations/0002_config.py
+comment/migrations/0003_comment_content_main_comment_status_edited_and_more.py
 comment/migrations/__init__.py
 comment/static/comment/css/style.css
 comment/static/comment/css/style.min.css
 comment/static/comment/font/Vazir/Vazirmatn-Black.woff2
 comment/static/comment/font/Vazir/Vazirmatn-Bold.woff2
 comment/static/comment/font/Vazir/Vazirmatn-ExtraBold.woff2
 comment/static/comment/font/Vazir/Vazirmatn-ExtraLight.woff2
@@ -39,15 +40,14 @@
 comment/static/comment/font/Vazir-FD/Vazirmatn-FD-ExtraLight.woff2
 comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Light.woff2
 comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Medium.woff2
 comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Regular.woff2
 comment/static/comment/font/Vazir-FD/Vazirmatn-FD-SemiBold.woff2
 comment/static/comment/font/Vazir-FD/Vazirmatn-FD-Thin.woff2
 comment/static/comment/img/profile.png
-comment/static/comment/js/comment-no-jquery-no-tested.js
 comment/static/comment/js/comment.js
 comment/static/comment/js/comment.min.js
 comment/static/comment/js/jquery.min.js
 comment/static/comment/tailwindcss/style.css
 comment/static/comment/tailwindcss/tailwind.config.js
 comment/templates/comment/comment/comment_body.html
 comment/templates/comment/comment/comment_counter.html
```

### Comparing `django-comment-system-2.8.0/setup.cfg` & `django-comment-system-2.9.0/setup.cfg`

 * *Files identical despite different names*

