# Comparing `tmp/pysura-0.99.8.tar.gz` & `tmp/pysura-0.99.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pysura-0.99.8.tar", last modified: Fri Mar 31 00:56:42 2023, max compression
+gzip compressed data, was "pysura-0.99.9.tar", last modified: Fri Mar 31 01:04:39 2023, max compression
```

## Comparing `pysura-0.99.8.tar` & `pysura-0.99.9.tar`

### file list

```diff
@@ -1,75 +1,75 @@
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.868902 pysura-0.99.8/
--rw-r--r--   0 thegoodz   (501) staff       (20)     1069 2023-03-20 10:07:23.000000 pysura-0.99.8/LICENSE.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)     9127 2023-03-31 00:56:42.869060 pysura-0.99.8/PKG-INFO
--rw-r--r--   0 thegoodz   (501) staff       (20)     8354 2023-03-30 07:12:08.000000 pysura-0.99.8/README.rst
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.814872 pysura-0.99.8/pysura/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 15:46:21.000000 pysura-0.99.8/pysura/__init__.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.816116 pysura-0.99.8/pysura/cli/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-22 06:05:11.000000 pysura-0.99.8/pysura/cli/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      675 2023-03-26 09:40:52.000000 pysura-0.99.8/pysura/cli/app.py
--rw-r--r--   0 thegoodz   (501) staff       (20)    98197 2023-03-31 00:55:32.000000 pysura-0.99.8/pysura/cli/google_root.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.855521 pysura-0.99.8/pysura/faster_api/
--rw-r--r--   0 thegoodz   (501) staff       (20)       25 2023-03-23 14:15:46.000000 pysura-0.99.8/pysura/faster_api/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      206 2023-03-30 05:06:41.000000 pysura-0.99.8/pysura/faster_api/enums.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     5914 2023-03-30 21:39:40.000000 pysura-0.99.8/pysura/faster_api/security.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      148 2023-03-24 15:28:42.000000 pysura-0.99.8/pysura/faster_api/test_class.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.810824 pysura-0.99.8/pysura/library_data/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.856181 pysura-0.99.8/pysura/library_data/pysura_auth/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-26 12:15:47.000000 pysura-0.99.8/pysura/library_data/pysura_auth/.gcloudignore
--rw-r--r--   0 thegoodz   (501) staff       (20)     2646 2023-03-30 06:54:45.000000 pysura-0.99.8/pysura/library_data/pysura_auth/main.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      958 2023-03-27 11:41:24.000000 pysura-0.99.8/pysura/library_data/pysura_auth/requirements.txt
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.856524 pysura-0.99.8/pysura/library_data/pysura_frontend/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.856973 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.858438 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/common/
--rw-r--r--   0 thegoodz   (501) staff       (20)      373 2023-03-27 17:25:23.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/common/constants.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      393 2023-03-27 16:40:53.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/common/date_util.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     3130 2023-03-27 16:46:35.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/common/popups.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2025 2023-03-27 16:50:56.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/common/styles.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      729 2023-03-27 16:42:08.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/common/utils.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.859033 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/controllers/
--rw-r--r--   0 thegoodz   (501) staff       (20)     1560 2023-03-27 16:42:36.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1969 2023-03-27 16:46:35.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2516 2023-03-29 21:00:46.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/main.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.810695 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.860913 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/auth/
--rw-r--r--   0 thegoodz   (501) staff       (20)     5158 2023-03-27 16:43:52.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2047 2023-03-27 16:44:22.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.861639 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/main/
--rw-r--r--   0 thegoodz   (501) staff       (20)      882 2023-03-27 23:17:43.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      718 2023-03-27 23:17:17.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.862316 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/misc/
--rw-r--r--   0 thegoodz   (501) staff       (20)      338 2023-03-27 16:50:56.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/misc/error_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      301 2023-03-27 16:50:56.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/misc/loading_page.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.863803 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/widgets/
--rw-r--r--   0 thegoodz   (501) staff       (20)      708 2023-03-27 16:50:56.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1536 2023-03-27 16:50:56.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1393 2023-03-27 16:51:23.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1466 2023-03-27 16:51:50.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1954 2023-03-29 21:12:03.000000 pysura-0.99.8/pysura/library_data/pysura_frontend/pubspec.yaml
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.866438 pysura-0.99.8/pysura/library_data/pysura_microservice/
--rw-r--r--   0 thegoodz   (501) staff       (20)      596 2023-03-30 01:08:14.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/Dockerfile
--rw-r--r--   0 thegoodz   (501) staff       (20)       30 2023-03-30 05:47:17.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/README.md
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.867198 pysura-0.99.8/pysura/library_data/pysura_microservice/actions/
--rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 22:32:31.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/actions/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1689 2023-03-30 17:37:02.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/actions/action_template.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      746 2023-03-30 21:11:23.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/app.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1050 2023-03-30 21:37:32.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/app_secrets.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.867589 pysura-0.99.8/pysura/library_data/pysura_microservice/crons/
--rw-r--r--   0 thegoodz   (501) staff       (20)       18 2023-03-30 01:13:17.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/crons/__init__.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.867836 pysura-0.99.8/pysura/library_data/pysura_microservice/events/
--rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 01:13:17.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/events/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     5947 2023-03-30 17:37:02.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/pysura_metadata.json
--rw-r--r--   0 thegoodz   (501) staff       (20)     1165 2023-03-30 01:13:17.000000 pysura-0.99.8/pysura/library_data/pysura_microservice/requirements.txt
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.868615 pysura-0.99.8/pysura/pysura_types/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 16:42:48.000000 pysura-0.99.8/pysura/pysura_types/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)    19300 2023-03-30 18:35:44.000000 pysura-0.99.8/pysura/pysura_types/google_pysura_env.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     5588 2023-03-31 00:37:53.000000 pysura-0.99.8/pysura/pysura_types/root_cmd.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 00:56:42.815615 pysura-0.99.8/pysura.egg-info/
--rw-r--r--   0 thegoodz   (501) staff       (20)     9127 2023-03-31 00:56:42.000000 pysura-0.99.8/pysura.egg-info/PKG-INFO
--rw-r--r--   0 thegoodz   (501) staff       (20)     2492 2023-03-31 00:56:42.000000 pysura-0.99.8/pysura.egg-info/SOURCES.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-03-31 00:56:42.000000 pysura-0.99.8/pysura.egg-info/dependency_links.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)       47 2023-03-31 00:56:42.000000 pysura-0.99.8/pysura.egg-info/entry_points.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)      153 2023-03-31 00:56:42.000000 pysura-0.99.8/pysura.egg-info/requires.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)        7 2023-03-31 00:56:42.000000 pysura-0.99.8/pysura.egg-info/top_level.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)      106 2023-03-31 00:56:42.870442 pysura-0.99.8/setup.cfg
--rw-r--r--   0 thegoodz   (501) staff       (20)     3675 2023-03-31 00:55:32.000000 pysura-0.99.8/setup.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.098084 pysura-0.99.9/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1069 2023-03-20 10:07:23.000000 pysura-0.99.9/LICENSE.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)     9127 2023-03-31 01:04:39.098186 pysura-0.99.9/PKG-INFO
+-rw-r--r--   0 thegoodz   (501) staff       (20)     8354 2023-03-30 07:12:08.000000 pysura-0.99.9/README.rst
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.085116 pysura-0.99.9/pysura/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 15:46:21.000000 pysura-0.99.9/pysura/__init__.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.086513 pysura-0.99.9/pysura/cli/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-22 06:05:11.000000 pysura-0.99.9/pysura/cli/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      675 2023-03-26 09:40:52.000000 pysura-0.99.9/pysura/cli/app.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)    98193 2023-03-31 01:02:09.000000 pysura-0.99.9/pysura/cli/google_root.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.087841 pysura-0.99.9/pysura/faster_api/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       25 2023-03-23 14:15:46.000000 pysura-0.99.9/pysura/faster_api/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      206 2023-03-30 05:06:41.000000 pysura-0.99.9/pysura/faster_api/enums.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5914 2023-03-30 21:39:40.000000 pysura-0.99.9/pysura/faster_api/security.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      148 2023-03-24 15:28:42.000000 pysura-0.99.9/pysura/faster_api/test_class.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.082157 pysura-0.99.9/pysura/library_data/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.088559 pysura-0.99.9/pysura/library_data/pysura_auth/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-26 12:15:47.000000 pysura-0.99.9/pysura/library_data/pysura_auth/.gcloudignore
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2646 2023-03-30 06:54:45.000000 pysura-0.99.9/pysura/library_data/pysura_auth/main.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      958 2023-03-27 11:41:24.000000 pysura-0.99.9/pysura/library_data/pysura_auth/requirements.txt
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.088798 pysura-0.99.9/pysura/library_data/pysura_frontend/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.089170 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.090834 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/common/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      373 2023-03-27 17:25:23.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/common/constants.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      393 2023-03-27 16:40:53.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/common/date_util.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     3130 2023-03-27 16:46:35.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/common/popups.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2025 2023-03-27 16:50:56.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/common/styles.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      729 2023-03-27 16:42:08.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/common/utils.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.091573 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/controllers/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1560 2023-03-27 16:42:36.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1969 2023-03-27 16:46:35.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2516 2023-03-29 21:00:46.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/main.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.082026 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.092079 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/auth/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5158 2023-03-27 16:43:52.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2047 2023-03-27 16:44:22.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.092678 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/main/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      882 2023-03-27 23:17:43.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      718 2023-03-27 23:17:17.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.093184 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/misc/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      338 2023-03-27 16:50:56.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/misc/error_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      301 2023-03-27 16:50:56.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/misc/loading_page.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.094390 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/widgets/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      708 2023-03-27 16:50:56.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1536 2023-03-27 16:50:56.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1393 2023-03-27 16:51:23.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1466 2023-03-27 16:51:50.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1954 2023-03-29 21:12:03.000000 pysura-0.99.9/pysura/library_data/pysura_frontend/pubspec.yaml
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.096315 pysura-0.99.9/pysura/library_data/pysura_microservice/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      596 2023-03-30 01:08:14.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/Dockerfile
+-rw-r--r--   0 thegoodz   (501) staff       (20)       30 2023-03-30 05:47:17.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/README.md
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.096781 pysura-0.99.9/pysura/library_data/pysura_microservice/actions/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 22:32:31.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/actions/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1689 2023-03-30 17:37:02.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/actions/action_template.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      746 2023-03-30 21:11:23.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/app.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1050 2023-03-30 21:37:32.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/app_secrets.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.097095 pysura-0.99.9/pysura/library_data/pysura_microservice/crons/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       18 2023-03-30 01:13:17.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/crons/__init__.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.097283 pysura-0.99.9/pysura/library_data/pysura_microservice/events/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 01:13:17.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/events/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5947 2023-03-30 17:37:02.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/pysura_metadata.json
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1165 2023-03-30 01:13:17.000000 pysura-0.99.9/pysura/library_data/pysura_microservice/requirements.txt
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.097972 pysura-0.99.9/pysura/pysura_types/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 16:42:48.000000 pysura-0.99.9/pysura/pysura_types/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)    19300 2023-03-30 18:35:44.000000 pysura-0.99.9/pysura/pysura_types/google_pysura_env.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5720 2023-03-31 01:03:50.000000 pysura-0.99.9/pysura/pysura_types/root_cmd.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-03-31 01:04:39.085984 pysura-0.99.9/pysura.egg-info/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     9127 2023-03-31 01:04:39.000000 pysura-0.99.9/pysura.egg-info/PKG-INFO
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2492 2023-03-31 01:04:39.000000 pysura-0.99.9/pysura.egg-info/SOURCES.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-03-31 01:04:39.000000 pysura-0.99.9/pysura.egg-info/dependency_links.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)       47 2023-03-31 01:04:39.000000 pysura-0.99.9/pysura.egg-info/entry_points.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)      153 2023-03-31 01:04:39.000000 pysura-0.99.9/pysura.egg-info/requires.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)        7 2023-03-31 01:04:39.000000 pysura-0.99.9/pysura.egg-info/top_level.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)      106 2023-03-31 01:04:39.099183 pysura-0.99.9/setup.cfg
+-rw-r--r--   0 thegoodz   (501) staff       (20)     3675 2023-03-31 01:04:14.000000 pysura-0.99.9/setup.py
```

### Comparing `pysura-0.99.8/LICENSE.txt` & `pysura-0.99.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/PKG-INFO` & `pysura-0.99.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pysura
-Version: 0.99.8
+Version: 0.99.9
 Summary: A useful tool that provides commands to help ease the installation process of Hasura, and manage its actions, events, and scheduled jobs with baked in phone Auth and a Flutter frontend.
 Home-page: https://github.com/tristengoodz/pysura
 Author: Tristen Harr
 Author-email: tristen@thegoodzapp.com
 License: UNKNOWN
 Keywords: hasura,graphql,postgresql,google-cloud,python,pysura,backend,backend-in-a-box
 Platform: UNKNOWN
```

### Comparing `pysura-0.99.8/README.rst` & `pysura-0.99.9/README.rst`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/cli/app.py` & `pysura-0.99.9/pysura/cli/app.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/cli/google_root.py` & `pysura-0.99.9/pysura/cli/google_root.py`

 * *Files 0% similar despite different names*

```diff
@@ -1458,15 +1458,15 @@
           "type": "RS256",
           "jwk_url": "https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com",
           "audience": "PROJECT_ID",
           "issuer": "https://securetoken.google.com/PROJECT_ID"
         }""".replace("PROJECT_ID", env.project.name.split("/")[-1])))
         env.hasura.HASURA_GRAPHQL_JWT_SECRET = jwt_config
         self.set_env(env)
-        self.do_gcloud_deploy_hasura(None)
+        self.do_gcloud_deploy_hasura()
 
     def do_attach_firebase(self, _):
         env = self.get_env()
         cmd_str = f"firebase projects:addfirebase  {env.project.name.split('/')[-1]}"
         self.log(cmd_str, level=logging.DEBUG)
         os.system(cmd_str)
         cmd_str = f"firebase login --interactive"
@@ -2010,15 +2010,15 @@
         for action_data in hasura_metadata.get("actions", []):
             if action_data.get("name") in included_actions:
                 new_hasura_metadata["actions"].append(action_data)
                 action_names.append(action_data.get("name"))
 
         init_str = ""
         for action_name in action_names:
-            init_str += f"from {action_name} import {action_name}_router\n"
+            init_str += f"from actions.{action_name} import {action_name}_router\n"
 
         init_str += f"\naction_routers = [\n"
         for action_name in action_names:
             init_str += f"    {action_name}_router,\n"
         init_str += "]\n"
         with open("actions/__init__.py", "w") as f:
             f.write(init_str)
@@ -2157,15 +2157,15 @@
                             break
                     if append_flag:
                         env.hasura.microservice_urls.append(microservice_url)
             new_services.append(service_data)
         env.services = new_services
         os.chdir("../..")
         self.set_env(env)
-        self.do_gcloud_deploy_hasura(None)
+        self.do_gcloud_deploy_hasura()
         with open("hasura_metadata.json", "r") as f:
             metadata = json.load(f)
         new_metadata = {}
         new_actions = []
         new_objects = []
         new_input_objects = []
         for key, value in metadata.items():
@@ -2233,14 +2233,14 @@
                 self.do_gcloud_create_vpc_peering(peering_id=hasura_project_name)
             if env.firewalls is None:
                 self.do_gcloud_create_firewall(firewall_id=hasura_project_name)
             if env.database_credential is None:
                 self.do_gcloud_create_database(database_id=hasura_project_name)
             if env.connector is None:
                 self.do_gcloud_create_serverless_connector(connector_id=hasura_project_name)
-            self.do_gcloud_deploy_hasura(None)
+            self.do_gcloud_deploy_hasura()
             self.do_gcloud_create_auth_service_account(None)
             env = self.get_env()
             self.do_enable_database_local(database_id=env.database.name.split("/")[-1])
             self.do_create_default_user_table(None)
             self.do_attach_firebase(None)
             self.do_deploy_microservice(microservice_name="default")
```

### Comparing `pysura-0.99.8/pysura/faster_api/security.py` & `pysura-0.99.9/pysura/faster_api/security.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_auth/main.py` & `pysura-0.99.9/pysura/library_data/pysura_auth/main.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_auth/requirements.txt` & `pysura-0.99.9/pysura/library_data/pysura_auth/requirements.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/common/popups.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/common/popups.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/common/styles.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/common/styles.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/common/utils.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/common/utils.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/main.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/main.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart` & `pysura-0.99.9/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_frontend/pubspec.yaml` & `pysura-0.99.9/pysura/library_data/pysura_frontend/pubspec.yaml`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_microservice/Dockerfile` & `pysura-0.99.9/pysura/library_data/pysura_microservice/Dockerfile`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_microservice/actions/action_template.py` & `pysura-0.99.9/pysura/library_data/pysura_microservice/actions/action_template.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_microservice/app.py` & `pysura-0.99.9/pysura/library_data/pysura_microservice/app.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_microservice/app_secrets.py` & `pysura-0.99.9/pysura/library_data/pysura_microservice/app_secrets.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_microservice/pysura_metadata.json` & `pysura-0.99.9/pysura/library_data/pysura_microservice/pysura_metadata.json`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/library_data/pysura_microservice/requirements.txt` & `pysura-0.99.9/pysura/library_data/pysura_microservice/requirements.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/pysura_types/google_pysura_env.py` & `pysura-0.99.9/pysura/pysura_types/google_pysura_env.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/pysura/pysura_types/root_cmd.py` & `pysura-0.99.9/pysura/pysura_types/root_cmd.py`

 * *Files 3% similar despite different names*

```diff
@@ -13,28 +13,31 @@
 import os
 import json
 
 
 class RootCmd(Cmd):
 
     def setup_logging(self):
+        if not os.path.exists("logs"):
+            os.mkdir("logs")
+        log_path = os.path.join(os.getcwd(), "logs")
         log_levels = {
             'debug': logging.DEBUG,
             'info': logging.INFO,
             'warning': logging.WARNING,
             'error': logging.ERROR,
             'critical': logging.CRITICAL
         }
 
         root_logger = logging.getLogger()
         if not root_logger.hasHandlers():
             root_logger.setLevel(logging.DEBUG)
 
             for level_name, level in log_levels.items():
-                log_file_handler = logging.FileHandler(f'{level_name}.log', mode='a')
+                log_file_handler = logging.FileHandler(f'{log_path}/{level_name}.log', mode='a')
                 log_file_handler.setLevel(level)
                 log_file_formatter = logging.Formatter(fmt="%(asctime)s %(levelname)-5s %(message)s",
                                                        datefmt="%Y-%m-%d %I:%H:%M")
                 log_file_handler.setFormatter(log_file_formatter)
                 root_logger.addHandler(log_file_handler)
 
             root_handler = logging.StreamHandler(sys.stdout)
```

### Comparing `pysura-0.99.8/pysura.egg-info/PKG-INFO` & `pysura-0.99.9/pysura.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pysura
-Version: 0.99.8
+Version: 0.99.9
 Summary: A useful tool that provides commands to help ease the installation process of Hasura, and manage its actions, events, and scheduled jobs with baked in phone Auth and a Flutter frontend.
 Home-page: https://github.com/tristengoodz/pysura
 Author: Tristen Harr
 Author-email: tristen@thegoodzapp.com
 License: UNKNOWN
 Keywords: hasura,graphql,postgresql,google-cloud,python,pysura,backend,backend-in-a-box
 Platform: UNKNOWN
```

### Comparing `pysura-0.99.8/pysura.egg-info/SOURCES.txt` & `pysura-0.99.9/pysura.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.8/setup.py` & `pysura-0.99.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name="pysura",
-    version="0.99.8",
+    version="0.99.9",
     packages=find_packages(),
     entry_points={
         "console_scripts": [
             "pysura=pysura.cli.app:cli"
         ]
     },
     package_dir={"pysura": "pysura"},
```

