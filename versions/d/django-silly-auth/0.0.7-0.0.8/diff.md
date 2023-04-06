# Comparing `tmp/django-silly-auth-0.0.7.tar.gz` & `tmp/django-silly-auth-0.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "django-silly-auth-0.0.7.tar", last modified: Wed Apr  5 04:46:51 2023, max compression
+gzip compressed data, was "django-silly-auth-0.0.8.tar", last modified: Thu Apr  6 17:28:35 2023, max compression
```

## Comparing `django-silly-auth-0.0.7.tar` & `django-silly-auth-0.0.8.tar`

### file list

```diff
@@ -1,56 +1,57 @@
-drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:46:51.751623 django-silly-auth-0.0.7/
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     1072 2023-03-30 21:48:27.000000 django-silly-auth-0.0.7/LICENSE.md
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     1924 2023-04-05 04:46:51.751623 django-silly-auth-0.0.7/PKG-INFO
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     1314 2023-04-05 04:43:28.000000 django-silly-auth-0.0.7/README.md
-drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:46:51.743623 django-silly-auth-0.0.7/django_silly_auth/
--rw-rw-r--   0 byoso     (1000) byoso     (1000)       22 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/__init__.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     4625 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/config.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)       41 2023-04-03 08:45:56.000000 django-silly-auth-0.0.7/django_silly_auth/exceptions.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     5495 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/forms.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     2394 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/mixins.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     3637 2023-04-03 20:54:16.000000 django-silly-auth-0.0.7/django_silly_auth/serializers.py
-drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:46:51.743623 django-silly-auth-0.0.7/django_silly_auth/templates/
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      146 2023-04-04 20:59:42.000000 django-silly-auth-0.0.7/django_silly_auth/templates/helpers.py
-drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:46:51.743623 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/
--rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-03 16:52:09.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/__init__.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      512 2023-04-04 22:34:28.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/_base.html
-drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:46:51.747623 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/_test/
--rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/_test/__init__.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     3052 2023-04-05 04:17:33.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/_test/_base.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      175 2023-04-04 22:34:28.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/_test/_test.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      274 2023-04-04 20:59:42.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/_test/_users.html
-drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:46:51.747623 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/
--rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/__init__.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      515 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/account.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      528 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/change_email.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      539 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/change_username.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      328 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/index.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      713 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/login.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      512 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/request_password_reset.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      740 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/reset_password.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     1048 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/signin.html
-drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:46:51.747623 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/emails/
--rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-03 16:51:56.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/emails/__init__.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      243 2023-04-03 10:13:02.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/emails/confirm_email.txt
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      238 2023-03-31 12:20:50.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/emails/request_password_reset.txt
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      621 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/new_email_confirm.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      417 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/new_email_confirmed_done.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      884 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/reset_password.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      427 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/reset_password_done.html
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     4483 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/urls.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     3093 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/utils.py
-drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:46:51.747623 django-silly-auth-0.0.7/django_silly_auth/views/
--rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-03 13:29:53.000000 django-silly-auth-0.0.7/django_silly_auth/views/__init__.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     1651 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/views/api_custom_login.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)      260 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/views/api_views.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     6013 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/views/api_views_if_drf.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     9224 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/views/classics.py
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     4700 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/django_silly_auth/views/views.py
-drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:46:51.743623 django-silly-auth-0.0.7/django_silly_auth.egg-info/
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     1924 2023-04-05 04:46:51.000000 django-silly-auth-0.0.7/django_silly_auth.egg-info/PKG-INFO
--rw-rw-r--   0 byoso     (1000) byoso     (1000)     2078 2023-04-05 04:46:51.000000 django-silly-auth-0.0.7/django_silly_auth.egg-info/SOURCES.txt
--rw-rw-r--   0 byoso     (1000) byoso     (1000)        1 2023-04-05 04:46:51.000000 django-silly-auth-0.0.7/django_silly_auth.egg-info/dependency_links.txt
--rw-rw-r--   0 byoso     (1000) byoso     (1000)       13 2023-04-05 04:46:51.000000 django-silly-auth-0.0.7/django_silly_auth.egg-info/requires.txt
--rw-rw-r--   0 byoso     (1000) byoso     (1000)       18 2023-04-05 04:46:51.000000 django-silly-auth-0.0.7/django_silly_auth.egg-info/top_level.txt
--rw-rw-r--   0 byoso     (1000) byoso     (1000)       38 2023-04-05 04:46:51.751623 django-silly-auth-0.0.7/setup.cfg
--rwxrwxr-x   0 byoso     (1000) byoso     (1000)     1896 2023-04-05 04:15:11.000000 django-silly-auth-0.0.7/setup.py
+drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-06 17:28:35.336551 django-silly-auth-0.0.8/
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     1072 2023-03-30 21:48:27.000000 django-silly-auth-0.0.8/LICENSE.md
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     1925 2023-04-06 17:28:35.336551 django-silly-auth-0.0.8/PKG-INFO
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     1315 2023-04-06 13:29:54.000000 django-silly-auth-0.0.8/README.md
+drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-06 17:28:35.320550 django-silly-auth-0.0.8/django_silly_auth/
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)       22 2023-04-06 17:10:40.000000 django-silly-auth-0.0.8/django_silly_auth/__init__.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     4752 2023-04-06 17:20:18.000000 django-silly-auth-0.0.8/django_silly_auth/config.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)       41 2023-04-03 08:45:56.000000 django-silly-auth-0.0.8/django_silly_auth/exceptions.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     5589 2023-04-06 17:19:45.000000 django-silly-auth-0.0.8/django_silly_auth/forms.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     2394 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/mixins.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     3637 2023-04-03 20:54:16.000000 django-silly-auth-0.0.8/django_silly_auth/serializers.py
+drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-06 17:28:35.324550 django-silly-auth-0.0.8/django_silly_auth/templates/
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      234 2023-04-06 17:10:17.000000 django-silly-auth-0.0.8/django_silly_auth/templates/helpers.py
+drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-06 17:28:35.324550 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-03 16:52:09.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/__init__.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      512 2023-04-04 22:34:28.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/_base.html
+drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-06 17:28:35.328550 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/_test/
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/_test/__init__.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     4187 2023-04-06 17:17:07.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/_test/_base.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      175 2023-04-04 22:34:28.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/_test/_test.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      274 2023-04-04 20:59:42.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/_test/_users.html
+drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-06 17:28:35.332550 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/__init__.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      515 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/account.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      528 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/change_email.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      539 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/change_username.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      328 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/index.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     1045 2023-04-06 16:37:59.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/login.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      512 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/request_password_reset.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      527 2023-04-06 16:37:59.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/request_resend_account_confirmation_email.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      800 2023-04-06 16:37:59.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/reset_password.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     1094 2023-04-06 13:29:54.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/signup.html
+drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-06 17:28:35.332550 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/emails/
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-03 16:51:56.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/emails/__init__.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      243 2023-04-03 10:13:02.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/emails/confirm_email.txt
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      238 2023-03-31 12:20:50.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/emails/request_password_reset.txt
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      621 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/new_email_confirm.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      411 2023-04-06 16:37:59.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/new_email_confirmed_done.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      884 2023-04-05 15:24:47.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/reset_password.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      427 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/reset_password_done.html
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     4723 2023-04-06 17:14:51.000000 django-silly-auth-0.0.8/django_silly_auth/urls.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     3046 2023-04-06 16:37:59.000000 django-silly-auth-0.0.8/django_silly_auth/utils.py
+drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-06 17:28:35.336551 django-silly-auth-0.0.8/django_silly_auth/views/
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)        0 2023-04-03 13:29:53.000000 django-silly-auth-0.0.8/django_silly_auth/views/__init__.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     1651 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/views/api_custom_login.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)      260 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/views/api_views.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     6013 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/views/api_views_if_drf.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)    12404 2023-04-06 17:19:20.000000 django-silly-auth-0.0.8/django_silly_auth/views/classics.py
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     4700 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/django_silly_auth/views/views.py
+drwxrwxr-x   0 byoso     (1000) byoso     (1000)        0 2023-04-06 17:28:35.324550 django-silly-auth-0.0.8/django_silly_auth.egg-info/
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     1925 2023-04-06 17:28:35.000000 django-silly-auth-0.0.8/django_silly_auth.egg-info/PKG-INFO
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)     2172 2023-04-06 17:28:35.000000 django-silly-auth-0.0.8/django_silly_auth.egg-info/SOURCES.txt
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)        1 2023-04-06 17:28:35.000000 django-silly-auth-0.0.8/django_silly_auth.egg-info/dependency_links.txt
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)       13 2023-04-06 17:28:35.000000 django-silly-auth-0.0.8/django_silly_auth.egg-info/requires.txt
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)       18 2023-04-06 17:28:35.000000 django-silly-auth-0.0.8/django_silly_auth.egg-info/top_level.txt
+-rw-rw-r--   0 byoso     (1000) byoso     (1000)       38 2023-04-06 17:28:35.336551 django-silly-auth-0.0.8/setup.cfg
+-rwxrwxr-x   0 byoso     (1000) byoso     (1000)     1896 2023-04-05 04:15:11.000000 django-silly-auth-0.0.8/setup.py
```

### Comparing `django-silly-auth-0.0.7/LICENSE.md` & `django-silly-auth-0.0.8/LICENSE.md`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/PKG-INFO` & `django-silly-auth-0.0.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-silly-auth
-Version: 0.0.7
+Version: 0.0.8
 Summary: Authentication package for Django and DRF
 Home-page: https://github.com/byoso/django_silly_auth
 Author: Vincent Fabre
 Author-email: peigne.plume@gmail.com
 License: MIT
 Keywords: django auth drf jwt
 Platform: UNKNOWN
@@ -43,7 +43,8 @@
 
 - ## [SILLY_AUTH settings explained](https://github.com/byoso/django_silly_auth/wiki/SILLY_AUTH-settings-explained)
 
 - ## [API Endpoints](https://github.com/byoso/django_silly_auth/wiki/API-endpoints)
 
 - ## [Classic Django](https://github.com/byoso/django_silly_auth/wiki/Classic-Django)
 
+
```

### Comparing `django-silly-auth-0.0.7/README.md` & `django-silly-auth-0.0.8/README.md`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -22,8 +22,8 @@
 
 - ## [Configure emails](https://github.com/byoso/django_silly_auth/wiki/Configure-the-emails-of-the-site)
 
 - ## [SILLY_AUTH settings explained](https://github.com/byoso/django_silly_auth/wiki/SILLY_AUTH-settings-explained)
 
 - ## [API Endpoints](https://github.com/byoso/django_silly_auth/wiki/API-endpoints)
 
-- ## [Classic Django](https://github.com/byoso/django_silly_auth/wiki/Classic-Django)
+- ## [Classic Django](https://github.com/byoso/django_silly_auth/wiki/Classic-Django)
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth/config.py` & `django-silly-auth-0.0.8/django_silly_auth/config.py`

 * *Files 5% similar despite different names*

```diff
@@ -61,22 +61,23 @@
     "CONFIRM_NEW_EMAIL_HOOK_ENDPOINT": "confirm_new_email/<token>/",  # default is a classic view
     "NEW_EMAIL_CONFIRM_TEMPLATE": dsa_template_path("silly_auth/new_email_confirm.html"),  # if new email hook activated
     "NEW_EMAIL_CONFIRMED_DONE_TEMPLATE": dsa_template_path("silly_auth/new_email_confirmed_done.html"),  # if new email hook activated
 
     # FULL_CLASSIC templates, if you use FULL_CLASSIC == True, change this to your own templates
     "USE_CLASSIC_INDEX": True,  # if False, your url route must have the name='classic_index'
     "CLASSIC_INDEX": dsa_template_path("silly_auth/classic/index.html"),
-    "USE_CLASSIC_ACCOUNT": True, # if False, your url route must have the name='classic_account'
+    "USE_CLASSIC_ACCOUNT": True,  # if False, your url route must have the name='classic_account'
     "CLASSIC_ACCOUNT": dsa_template_path("silly_auth/classic/account.html"),
-    "CLASSIC_SIGNIN": dsa_template_path("silly_auth/classic/signin.html"),
+    "CLASSIC_SIGNUP": dsa_template_path("silly_auth/classic/signup.html"),
     "CLASSIC_LOGIN": dsa_template_path("silly_auth/classic/login.html"),
     "CLASSIC_CHANGE_EMAIL": dsa_template_path("silly_auth/classic/change_email.html"),
     "CLASSIC_CHANGE_USERNAME": dsa_template_path("silly_auth/classic/change_username.html"),
     "CLASSIC_REQUEST_PASSWORD_RESET": dsa_template_path("silly_auth/classic/request_password_reset.html"),
     "CLASSIC_RESET_PASSWORD": dsa_template_path("silly_auth/classic/reset_password.html"),
+    "CLASSIC_REQUEST_RESEND_ACCOUNT_CONFIRMATION_EMAIL": "silly_auth/classic/request_resend_account_confirmation_email.html",
 
 
 }
 
 # Overwrite SILLY_AUTH_SETTINGS with datas from  settings.SILLY_AUTH
 try:
     for key in settings.SILLY_AUTH:
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth/forms.py` & `django-silly-auth-0.0.8/django_silly_auth/forms.py`

 * *Files 1% similar despite different names*

```diff
@@ -61,15 +61,15 @@
         else:
             user = User.objects.filter(username=credential)
         if not user or not user[0].is_confirmed:
             raise ValidationError(_(f"user '{credential}' unknown or unconfirmed"))
         return credential
 
 
-class SignInForm(forms.Form):
+class SignUpForm(forms.Form):
     username = forms.CharField(
         label=_("Username"),
         validators=[MinLengthValidator(4), MaxLengthValidator(64)],
         max_length=64,
     )
     email = forms.EmailField(
         label=_("Email"),
@@ -107,15 +107,15 @@
         email = self.cleaned_data['email']
         user = User.objects.filter(email=email)
         if user:
             raise ValidationError(_(f"'{email}' already used."))
         return email
 
 
-class RequestPasswordResetForm(forms.Form):
+class CredentialForm(forms.Form):
     credential = forms.CharField(
         label=_("Email or username"),
         validators=[])
 
     def clean_credential(self):
         credential = self.cleaned_data['credential']
         if "@" in credential:
@@ -135,14 +135,18 @@
     )
     password2 = forms.CharField(
         label=_("Confirm password"),
         max_length=64, widget=forms.PasswordInput,
         validators=[validate_password]
     )
 
+    def clean_password(self):
+        password = self.cleaned_data['password']
+        return password
+
     def clean_password2(self):
         password = self.cleaned_data['password']
         password2 = self.cleaned_data['password2']
         if password != password2:
             raise ValidationError(_("different than password"))
         return password2
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth/mixins.py` & `django-silly-auth-0.0.8/django_silly_auth/mixins.py`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/serializers.py` & `django-silly-auth-0.0.8/django_silly_auth/serializers.py`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/_base.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/_base.html`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/account.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/account.html`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/change_email.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/change_email.html`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/change_username.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/change_username.html`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/login.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/login.html`

 * *Files 21% similar despite different names*

```diff
@@ -1,30 +1,47 @@
 {% extends base_template %}
 
 {% block content %}
 <h1 class="h2 subtitle">Login</h1>
 <form method="post">
-    {% csrf_token %}
+  {% csrf_token %}
 
-<p>
-    {{ form.credential.label }} <br>
-    {{ form.credential }} <br>
-    {% for error in form.errors.credential %}
-    <span style="color: red;">{{ error }}</span>
-    {% endfor %}
-</p>
-<p>
-    {{ form.password.label }} <br>
-    {{ form.password }} <br>
-    {% for error in form.errors.password %}
-    <span style="color: red;">{{ error }}</span>
-    {% endfor %}
-    <br>
-    <a href="{% url 'classic_request_password_reset' %}">Forgot your password ?</a>
-</p>
+  <p>
+      {{ form.credential.label }} <br>
+      {{ form.credential }} <br>
+      <ul>
+        {% for error in form.errors.credential %}
+        <li style="color: red;">{{ error }}</li>
+        {% endfor %}
+
+      </ul>
+  </p>
+  <p>
+      {{ form.password.label }} <br>
+      {{ form.password }} <br>
+      <ul>
+        {% for error in form.errors.password %}
+        <li style="color: red;">{{ error }}</li>
+        {% endfor %}
+      </ul>
+      <br>
+  </p>
+
+  <ul>
+    <li>
+      <a href="{% url 'classic_request_password_reset' %}">I forgot my password.</a>
+    </li>
+    <li>
+      <p>
+        <a href="{% url 'classic_request_resend_confirmation_email' %}">
+          My account exists but is unconfirmed, please send me the confirmation email again.
+        </a>
+      </p>
 
+    </li>
+  </ul>
 
-    <input type="submit" class="button is-success m-2 btn btn-success" value="log in">
+  <input type="submit" class="button is-success m-2 btn btn-success" value="log in">
 </form>
 
 
 {% endblock content %}
```

#### html2text {}

```diff
@@ -1,12 +1,19 @@
 {% extends base_template %} {% block content %}
 ****** Login ******
 {% csrf_token %}
 {{ form.credential.label }}
 {{ form.credential }}
-{% for error in form.errors.credential %} {{ error }} {% endfor %}
+    * {% for error in form.errors.credential %}
+    * {{ error }}
+    * {% endfor %}
 {{ form.password.label }}
 {{ form.password }}
-{% for error in form.errors.password %} {{ error }} {% endfor %}
-Forgot_your_password_?
+    * {% for error in form.errors.password %}
+    * {{ error }}
+    * {% endfor %}
+
+    * I_forgot_my_password.
+    * My_account_exists_but_is_unconfirmed,_please_send_me_the_confirmation
+      email_again.
 [log in]
 {% endblock content %}
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/request_password_reset.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/request_password_reset.html`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/reset_password.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/reset_password.html`

 * *Files 11% similar despite different names*

```diff
@@ -9,25 +9,31 @@
 
 <form method="post">
     {% csrf_token %}
 
     <p>
         {{ form.password.label }} <br>
         {{ form.password }} <br>
-        {% for error in form.errors.password %}
-        <span style="color: red;">{{ error }}</span>
-        {% endfor %}
+        <ul>
+          {% for error in form.errors.password %}
+          <li style="color: red;">{{ error }}</li>
+          {% endfor %}
+
+        </ul>
 
     </p>
     <p>
         {{ form.password2.label }} <br>
         {{ form.password2 }} <br>
-        {% for error in form.errors.password2 %}
-        <span style="color: red;">{{ error }}</span>
-        {% endfor %}
+        <ul>
+          {% for error in form.errors.password2 %}
+          <li style="color: red;">{{ error }}</li>
+          {% endfor %}
+
+        </ul>
 
     </p>
     <p>
         <input type="submit" class="button is-success m-2 btn btn-success"value="confirm">
     </p>
 
 </form>
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/classic/signin.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/classic/signup.html`

 * *Files 7% similar despite different names*

```diff
@@ -31,14 +31,14 @@
     <p>
         {{ form.password2.label }} <br>
         {{ form.password2 }} <br>
         {% for error in form.errors.password2 %}
         <span style="color: red;">{{ error }}</span>
         {% endfor %}
     </p>
-        <input type="submit" value="Sign In">
+        <input type="submit" class="button is-success m-2 btn btn-success" value="Sign In">
 
 
 </form>
 
 
 {% endblock content %}
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/new_email_confirm.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/new_email_confirm.html`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/templates/silly_auth/reset_password.html` & `django-silly-auth-0.0.8/django_silly_auth/templates/silly_auth/reset_password.html`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/urls.py` & `django-silly-auth-0.0.8/django_silly_auth/urls.py`

 * *Files 6% similar despite different names*

```diff
@@ -11,19 +11,20 @@
     print("=== login_with_auth_token FROM django_silly_auth.api_custom_login")
 
 print("=== IMPORT django_silly_auth.urls")
 
 User = get_user_model()
 
 
-# Signal interceptor to make sure that superusers are always confirmed
+# Signal interceptor to make sure that superusers are always active
 @receiver(pre_save, sender=User)
-def superuser_is_always_confirmed(sender, instance, **kwargs):
+def new_superuser_is_always_active(sender, instance, **kwargs):
     if instance.is_superuser and not instance.is_confirmed:
         instance.is_confirmed = True
+        instance.is_active = True
 
 
 urlpatterns = [
 ]
 # for testing
 if conf["TEST_TEMPLATES"]:
     urlpatterns += [
@@ -107,18 +108,23 @@
         )
     ]
 
 if conf["FULL_CLASSIC"]:
     urlpatterns += [
         path('classic_login/', classics.login_view, name='classic_login'),
         path('classic_logout/', classics.logout_view, name='classic_logout'),
-        path('classic_signin/', classics.signin_view, name='classic_signin'),
+        path('classic_signup/', classics.signup_view, name='classic_signup'),
         path('classic_request_password_reset/', classics.request_password_reset, name='classic_request_password_reset'),
         path('classic_reset_password/<token>', classics.reset_password, name='classic_reset_password'),
         path('classic_change_username/', classics.change_username, name='classic_change_username'),
         path('classic_change_email/', classics.change_email, name='classic_change_email'),
         path('classic_confirm_email/<token>', classics.confirm_email, name='classic_confirm_email'),
+        path(
+            'classic_request_resend_confirmation_email/',
+            classics.request_resend_account_confirmation_email,
+            name='classic_request_resend_confirmation_email'
+        ),
     ]
     if conf["USE_CLASSIC_INDEX"]:
         urlpatterns += [path('', classics.index, name='classic_index'),]
     if conf["USE_CLASSIC_ACCOUNT"]:
         urlpatterns += [path('classic_account/', classics.account, name='classic_account'),]
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth/utils.py` & `django-silly-auth-0.0.8/django_silly_auth/utils.py`

 * *Files 21% similar despite different names*

```diff
@@ -6,90 +6,95 @@
 from django.utils.translation import gettext_lazy as _
 
 from smtplib import SMTPServerDisconnected
 
 from django_silly_auth.config import SILLY_AUTH_SETTINGS as conf
 from django_silly_auth.views.views import reset_password
 
-# email address to send emails from
-EMAIL_HOST_USER = settings.EMAIL_HOST_USER
-validity_time = conf["EMAIL_VALID_TIME"]
-email_confirm_account_template = conf["EMAIL_CONFIRM_ACCOUNT_TEMPLATE"]
-email_reset_password_template = conf["EMAIL_RESET_PASSWORD_TEMPLATE"]
-site_name = conf["SITE_NAME"]
-terminal_print = conf["EMAIL_TERMINAL_PRINT"]
-# print_warnings = conf["PRINT_WARNINGS"]
-reset_password_endpoint = conf["RESET_PASSWORD_ENDPOINT"]
-
 
 def send_password_reset_email(request, user):
-    token = user.get_jwt_token(expires_in=validity_time)
+    token = user.get_jwt_token(expires_in=conf["EMAIL_VALID_TIME"])
     domain = request.build_absolute_uri('/')[:-1]
     if conf["FULL_CLASSIC"]:
         link = domain + reverse('classic_reset_password', args=[token])
     else:
         link = domain + reverse(reset_password, args=[token])
     context = {
         'user': user,
         'link': link,
-        'site_name': site_name
+        'site_name': conf["SITE_NAME"]
     }
 
-    msg_text = get_template(email_reset_password_template)
-    if terminal_print:
-        print("from ", EMAIL_HOST_USER)
+    msg_text = get_template(conf["EMAIL_RESET_PASSWORD_TEMPLATE"])
+    if conf["EMAIL_TERMINAL_PRINT"]:
+        print("from ", settings.EMAIL_HOST_USER)
         print(msg_text.render(context))
 
     send_mail(
         'Password reset request',
         msg_text.render(context),
-        EMAIL_HOST_USER,
+        settings.EMAIL_HOST_USER,
         [user.email],
         fail_silently=False,
     )
 
 
 def send_confirm_email(request, user, new_email=False):
-    token = user.get_jwt_token(expires_in=validity_time)
+    token = user.get_jwt_token(expires_in=conf["EMAIL_VALID_TIME"])
     domain = request.build_absolute_uri('/')[:-1]
     if new_email:
         if conf["FULL_CLASSIC"]:
-            link = domain + reverse('classic_confirm_new_email', args=[token])
+            link = domain + reverse('classic_confirm_email', args=[token])
         link = domain + reverse('confirm_new_email', args=[token])
     else:
         if conf["FULL_CLASSIC"]:
             link = domain + reverse('classic_confirm_email', args=[token])
         else:
             link = domain + reverse('confirm_email', args=[token])
     context = {
         'user': user,
         'link': link,
-        'site_name': site_name,
+        'site_name': conf["SITE_NAME"],
     }
 
-    msg_text = get_template(email_confirm_account_template)
+    msg_text = get_template(conf["EMAIL_CONFIRM_ACCOUNT_TEMPLATE"])
 
-    if terminal_print:
-        print("from ", EMAIL_HOST_USER)
+    if conf["EMAIL_TERMINAL_PRINT"]:
+        print("from ", settings.EMAIL_HOST_USER)
         print(msg_text.render(context))
 
     if new_email:
         email = user.new_email
     else:
         email = user.email
 
     send_mail(
         'Confirm your new email',
         msg_text.render(context),
-        EMAIL_HOST_USER,
+        settings.EMAIL_HOST_USER,
         [email],
         fail_silently=False,
     )
 
 
+def send_generic_email(
+        subject,
+        message,
+        host=settings.EMAIL_HOST_USER,
+        to=None,  # list() of emails
+        fail_silently=False
+        ):
+    send_mail(
+        subject,
+        message,
+        host,
+        to,
+        fail_silently,
+    )
+
 class Color:
     """
     Color class for terminal output
     """
     end = "\x1b[0m"
     info = "\x1b[0;30;36m"
     success = "\x1b[0;30;32m"
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth/views/api_custom_login.py` & `django-silly-auth-0.0.8/django_silly_auth/views/api_custom_login.py`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/views/api_views_if_drf.py` & `django-silly-auth-0.0.8/django_silly_auth/views/api_views_if_drf.py`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth/views/classics.py` & `django-silly-auth-0.0.8/django_silly_auth/views/classics.py`

 * *Files 18% similar despite different names*

```diff
@@ -8,16 +8,16 @@
 from django.utils.translation import gettext_lazy as _
 
 from django_silly_auth.config import SILLY_AUTH_SETTINGS as conf
 from django_silly_auth.forms import NewPasswordForm, NewEmailConfirmForm
 from django_silly_auth.templates.helpers import dsa_template_path
 from django_silly_auth.forms import (
     LoginForm,
-    SignInForm,
-    RequestPasswordResetForm,
+    SignUpForm,
+    CredentialForm,
     ResetPasswordForm,
     ChangeUsernameForm,
     ChangeEmailForm,
 )
 from django_silly_auth.utils import (
     send_password_reset_email,
     send_confirm_email,
@@ -45,22 +45,22 @@
             if "@" in credential:
                 username = User.objects.get(email=credential).username
                 user = authenticate(
                     request, username=username, password=password)
             else:
                 user = authenticate(
                     request, username=credential, password=password)
-            if user is not None:
+            if user is not None and user.is_confirmed:
                 login(request, user)
                 return redirect('classic_index')
             else:
                 messages.add_message(
                     request, messages.ERROR,
-                    message=_("Access denied: wrong password"),
-                    extra_tags="danger"),
+                    message=_("Wrong credentials or unconfirmed account"),
+                    extra_tags="warning"),
         else:
             context = {
                 "form": form,
                 "base_template": conf["BASE_TEMPLATE"],
                 "title": conf["TEMPLATES_TITLE"],
             }
             return render(request, conf["CLASSIC_LOGIN"], context)
@@ -84,115 +84,144 @@
     context = {
         "base_template": conf["BASE_TEMPLATE"],
         "title": conf["TEMPLATES_TITLE"],
     }
     return render(request, conf["CLASSIC_ACCOUNT"], context)
 
 
-def signin_view(request):
+def signup_view(request):
     if request.method == 'POST':
-        form = SignInForm(request.POST)
+        form = SignUpForm(request.POST)
         if form.is_valid():
             username = form.cleaned_data['username']
             email = form.cleaned_data['email']
             password = form.cleaned_data['password']
-            user = User(username=username, email=email, is_active=False)
+            user = User(username=username, email=email, is_active=True)
             user.set_password(password)
             user.save()
-            send_password_reset_email(request, user)
+            send_confirm_email(request, user)
+            messages.add_message(
+                request, messages.INFO,
+                message=(_(
+                    f"Please check your email '{user.email}' "
+                    "to confirm your account"
+                    )),
+                extra_tags="info"
+            )
             return redirect('classic_login')
         else:
             context = {
                 "form": form,
                 "base_template": conf["BASE_TEMPLATE"],
                 "title": conf["TEMPLATES_TITLE"],
             }
-            return render(request, conf["CLASSIC_SIGNIN"], context)
+            return render(request, conf["CLASSIC_SIGNUP"], context)
 
-    form = SignInForm()
+    form = SignUpForm()
     context = {
         "form": form,
         "base_template": conf["BASE_TEMPLATE"],
         "title": conf["TEMPLATES_TITLE"],
     }
-    return render(request, conf["CLASSIC_SIGNIN"], context)
+    return render(request, conf["CLASSIC_SIGNUP"], context)
 
 
 def request_password_reset(request):
     if request.method == "POST":
-        form = RequestPasswordResetForm(request.POST)
+        form = CredentialForm(request.POST)
         if form.is_valid():
             credential = form.cleaned_data['credential']
             if "@" in credential:
                 user = User.objects.get(email=credential)
             else:
                 user = User.objects.get(username=credential)
-
             # user existence is checked by the form validation #
-            send_password_reset_email(request, user)
+            if user.is_active:
+                send_password_reset_email(request, user)
 
-            messages.add_message(
-                request, messages.INFO,
-                message=(_(
-                    f"Please check your email '{user.email}' "
-                    "to reset your password"
-                    )),
-                extra_tags="info"
-            )
+                messages.add_message(
+                    request, messages.INFO,
+                    message=(_(
+                        "Please check your inbox "
+                        "to reset your password"
+                        )),
+                    extra_tags="info"
+                )
+            else:
+                messages.add_message(
+                    request, messages.INFO,
+                    message=(_(
+                        "Your account is not active anymore, please contact the administrator, "
+                        "no email has been sent"
+                        )),
+                    extra_tags="info"
+                )
         else:
             context = {
                 "form": form,
                 "base_template": conf["BASE_TEMPLATE"],
                 "title": conf["TEMPLATES_TITLE"],
             }
             return render(
                 request,
                 conf["CLASSIC_REQUEST_PASSWORD_RESET"],
                 context
                 )
-    form = RequestPasswordResetForm()
+    form = CredentialForm()
     if request.user.is_authenticated:
-        form = RequestPasswordResetForm(initial={'credential': request.user.email})
+        form = CredentialForm(initial={'credential': request.user.email})
     context = {
         "form": form,
         "base_template": conf["BASE_TEMPLATE"],
         "title": conf["TEMPLATES_TITLE"],
     }
     return render(request, conf["CLASSIC_REQUEST_PASSWORD_RESET"], context)
 
 
 def reset_password(request, token):
+    """Receive the token from the confirmation email and reset the password"""
     user = User.verify_jwt_token(token)
     if user is None:
-        return HttpResponse(_("Token invalid or expired"))
+        messages.add_message(
+            request, messages.INFO,
+            message=(_(
+                "Invalid or expired token"
+                )),
+            extra_tags="danger"
+        )
+        return redirect('classic_index')
 
     if request.method == 'POST':
         form = ResetPasswordForm(request.POST)
         if form.is_valid():
             user.set_password(form.cleaned_data['password'])
-            user.is_active = True
-            user.is_confirmed = True
             user.save()
-            login(request, user)
             messages.add_message(
                 request, messages.SUCCESS,
-                message=_("Your password have been reset"),
+                message=_("Your password have been reset, please login"),
                 extra_tags="success"
             )
-            return redirect('classic_account')
+            return redirect('classic_index')
         else:
             context = {
                 'form': form,
                 "base_template": conf["BASE_TEMPLATE"],
                 "title": conf["TEMPLATES_TITLE"],
             }
             return render(request, conf["CLASSIC_RESET_PASSWORD"], context)
+
     form = ResetPasswordForm()
+    login(request, user)
+    messages.add_message(
+        request, messages.SUCCESS,
+        message=_("Your have been logged in by email confirmation, please reset your password."),
+        extra_tags="warning"
+    )
+
     context = {
-        'user': user,
         'form': form,
         "base_template": conf["BASE_TEMPLATE"],
         "title": conf["TEMPLATES_TITLE"],
     }
     return render(request, conf["CLASSIC_RESET_PASSWORD"], context)
 
 
@@ -235,26 +264,27 @@
 @login_required
 def change_email(request):
     if request.method == 'POST':
         form = ChangeEmailForm(request.POST)
         if form.is_valid():
             email = form.cleaned_data['email']
             user = request.user
-            user.unconfirmed_email = email
+            user.new_email = email
             user.save()
-            send_confirm_email(request, user)
+            send_confirm_email(request, user, new_email=True)
 
             messages.add_message(
                 request, messages.INFO,
                 message=(_(
-                    "Please check your email to"
-                    f" confirm your address '{email}'"
+                    "Please check your inbox to"
+                    f" confirm your new address '{email}'"
                     )),
                 extra_tags="info"
             )
+            return redirect("classic_account")
         else:
             context = {
                 'form': form,
                 "base_template": conf["BASE_TEMPLATE"],
                 "title": conf["TEMPLATES_TITLE"],
             }
             return render(request, conf["CLASSIC_CHANGE_EMAIL"], context)
@@ -266,20 +296,86 @@
         "title": conf["TEMPLATES_TITLE"],
     }
     return render(request, conf["CLASSIC_CHANGE_EMAIL"], context)
 
 
 def confirm_email(request, token):
     user = User.verify_jwt_token(token)
-    if user is not None:
-        user.email = user.new_email
-        user.new_email = None
+    if user is None:
+        messages.add_message(
+            request, messages.INFO,
+            message=(_(
+                "Invalid or expired token"
+                )),
+            extra_tags="danger"
+        )
+        return redirect('classic_index')
+    if user is not None and user.is_active:
+        if user.new_email:
+            user.email = user.new_email
+            user.new_email = None
         user.is_confirmed = True
         user.save()
-        login(request, user)
         messages.add_message(
             request, messages.SUCCESS,
-            message=_(f"Your new email have been confirmed: '{user.email}'"),
+            message=_("Your new email have been confirmed"),
             extra_tags="success"
         )
 
-        return redirect("classic_account")
+        return redirect("classic_index")
+
+
+def request_resend_account_confirmation_email(request):
+    if request.method == 'POST':
+        form = CredentialForm(request.POST)
+        if form.is_valid():
+            credential = form.cleaned_data['credential']
+            if "@" in credential:
+                user = User.objects.get(email=credential)
+            else:
+                user = User.objects.get(username=credential)
+
+            # user existence is checked by the form validation #
+
+            if user.is_confirmed:
+                messages.add_message(
+                    request, messages.INFO,
+                    message=(_(
+                        "Your account is already confirmed, "
+                        "no email has been sent."
+                        )),
+                    extra_tags="info"
+                )
+                return redirect("classic_login")
+
+            send_confirm_email(request, user)
+
+            messages.add_message(
+                request, messages.INFO,
+                message=(_(
+                    "Please check your inbox "
+                    "to confirm your account"
+                    )),
+                extra_tags="info"
+            )
+        else:
+            context = {
+                "form": form,
+                "base_template": conf["BASE_TEMPLATE"],
+                "title": conf["TEMPLATES_TITLE"],
+            }
+            return render(
+                request,
+                conf["CLASSIC_REQUEST_RESEND_ACCOUNT_CONFIRMATION_EMAIL"],
+                context
+                )
+    form = CredentialForm()
+    context = {
+        "form": form,
+        "base_template": conf["BASE_TEMPLATE"],
+        "title": conf["TEMPLATES_TITLE"],
+    }
+    return render(
+        request,
+        conf["CLASSIC_REQUEST_RESEND_ACCOUNT_CONFIRMATION_EMAIL"],
+        context
+        )
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth/views/views.py` & `django-silly-auth-0.0.8/django_silly_auth/views/views.py`

 * *Files identical despite different names*

### Comparing `django-silly-auth-0.0.7/django_silly_auth.egg-info/PKG-INFO` & `django-silly-auth-0.0.8/django_silly_auth.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: django-silly-auth
-Version: 0.0.7
+Version: 0.0.8
 Summary: Authentication package for Django and DRF
 Home-page: https://github.com/byoso/django_silly_auth
 Author: Vincent Fabre
 Author-email: peigne.plume@gmail.com
 License: MIT
 Keywords: django auth drf jwt
 Platform: UNKNOWN
@@ -43,7 +43,8 @@
 
 - ## [SILLY_AUTH settings explained](https://github.com/byoso/django_silly_auth/wiki/SILLY_AUTH-settings-explained)
 
 - ## [API Endpoints](https://github.com/byoso/django_silly_auth/wiki/API-endpoints)
 
 - ## [Classic Django](https://github.com/byoso/django_silly_auth/wiki/Classic-Django)
 
+
```

### Comparing `django-silly-auth-0.0.7/django_silly_auth.egg-info/SOURCES.txt` & `django-silly-auth-0.0.8/django_silly_auth.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -28,16 +28,17 @@
 django_silly_auth/templates/silly_auth/classic/__init__.py
 django_silly_auth/templates/silly_auth/classic/account.html
 django_silly_auth/templates/silly_auth/classic/change_email.html
 django_silly_auth/templates/silly_auth/classic/change_username.html
 django_silly_auth/templates/silly_auth/classic/index.html
 django_silly_auth/templates/silly_auth/classic/login.html
 django_silly_auth/templates/silly_auth/classic/request_password_reset.html
+django_silly_auth/templates/silly_auth/classic/request_resend_account_confirmation_email.html
 django_silly_auth/templates/silly_auth/classic/reset_password.html
-django_silly_auth/templates/silly_auth/classic/signin.html
+django_silly_auth/templates/silly_auth/classic/signup.html
 django_silly_auth/templates/silly_auth/emails/__init__.py
 django_silly_auth/templates/silly_auth/emails/confirm_email.txt
 django_silly_auth/templates/silly_auth/emails/request_password_reset.txt
 django_silly_auth/views/__init__.py
 django_silly_auth/views/api_custom_login.py
 django_silly_auth/views/api_views.py
 django_silly_auth/views/api_views_if_drf.py
```

### Comparing `django-silly-auth-0.0.7/setup.py` & `django-silly-auth-0.0.8/setup.py`

 * *Files identical despite different names*

