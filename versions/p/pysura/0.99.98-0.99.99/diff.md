# Comparing `tmp/pysura-0.99.98.tar.gz` & `tmp/pysura-0.99.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pysura-0.99.98.tar", last modified: Fri Apr  7 06:53:37 2023, max compression
+gzip compressed data, was "pysura-0.99.99.tar", last modified: Fri Apr  7 07:02:47 2023, max compression
```

## Comparing `pysura-0.99.98.tar` & `pysura-0.99.99.tar`

### file list

```diff
@@ -1,110 +1,110 @@
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.862068 pysura-0.99.98/
--rw-r--r--   0 thegoodz   (501) staff       (20)     1069 2023-03-20 10:07:23.000000 pysura-0.99.98/LICENSE.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)    11717 2023-04-07 06:53:37.862167 pysura-0.99.98/PKG-INFO
--rw-r--r--   0 thegoodz   (501) staff       (20)    10980 2023-04-05 22:05:09.000000 pysura-0.99.98/README.rst
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.840721 pysura-0.99.98/pysura/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 15:46:21.000000 pysura-0.99.98/pysura/__init__.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.842104 pysura-0.99.98/pysura/cli/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-22 06:05:11.000000 pysura-0.99.98/pysura/cli/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      771 2023-04-02 23:46:54.000000 pysura-0.99.98/pysura/cli/app.py
--rw-r--r--   0 thegoodz   (501) staff       (20)   159954 2023-04-07 06:52:31.000000 pysura-0.99.98/pysura/cli/google_root.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.843320 pysura-0.99.98/pysura/faster_api/
--rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-03-31 02:57:53.000000 pysura-0.99.98/pysura/faster_api/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      157 2023-04-01 13:36:35.000000 pysura-0.99.98/pysura/faster_api/enums.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1040 2023-04-02 22:11:13.000000 pysura-0.99.98/pysura/faster_api/models.py
--rw-r--r--   0 thegoodz   (501) staff       (20)    11936 2023-04-07 01:41:12.000000 pysura-0.99.98/pysura/faster_api/security.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.839688 pysura-0.99.98/pysura/library_data/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.844062 pysura-0.99.98/pysura/library_data/pysura_auth/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-26 12:15:47.000000 pysura-0.99.98/pysura/library_data/pysura_auth/.gcloudignore
--rw-r--r--   0 thegoodz   (501) staff       (20)     3056 2023-04-01 19:05:04.000000 pysura-0.99.98/pysura/library_data/pysura_auth/main.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      958 2023-03-27 11:41:24.000000 pysura-0.99.98/pysura/library_data/pysura_auth/requirements.txt
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.844656 pysura-0.99.98/pysura/library_data/pysura_frontend/
--rw-r--r--   0 thegoodz   (501) staff       (20)      691 2023-04-04 01:50:17.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/build.yaml
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.844993 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.846982 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/
--rw-r--r--   0 thegoodz   (501) staff       (20)     1075 2023-03-31 06:17:27.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/app_color.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2531 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/app_route.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2453 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/app_text_style.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1632 2023-03-31 06:19:26.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/app_theme.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      213 2023-04-04 16:39:17.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/constants.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      412 2023-03-31 06:21:23.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/date_util.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     3988 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/popups.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1285 2023-04-04 04:19:48.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/utils.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.847935 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/controllers/
--rw-r--r--   0 thegoodz   (501) staff       (20)     2400 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1000 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/controllers/data_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1980 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      452 2023-03-31 07:01:52.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/controllers/theme_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.850495 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/
--rw-r--r--   0 thegoodz   (501) staff       (20)     1034 2023-04-04 03:45:32.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql
--rw-r--r--   0 thegoodz   (501) staff       (20)    71391 2023-04-04 02:34:58.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)    43063 2023-04-04 01:21:17.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql
--rw-r--r--   0 thegoodz   (501) staff       (20)   368298 2023-04-04 02:34:58.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      646 2023-04-04 02:16:17.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/user.graphql
--rw-r--r--   0 thegoodz   (501) staff       (20)    63297 2023-04-04 02:34:58.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/user.graphql.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1966 2023-04-05 15:18:37.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/main.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.839165 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.851331 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/auth/
--rw-r--r--   0 thegoodz   (501) staff       (20)     5781 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2441 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.852058 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.852542 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/action/
--rw-r--r--   0 thegoodz   (501) staff       (20)     9580 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     4908 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.853092 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/home/
--rw-r--r--   0 thegoodz   (501) staff       (20)     7574 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     5621 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1162 2023-03-31 15:44:39.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      744 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      964 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/main_page_middleware.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.853542 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/settings/
--rw-r--r--   0 thegoodz   (501) staff       (20)     5506 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2298 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.854028 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/misc/
--rw-r--r--   0 thegoodz   (501) staff       (20)      350 2023-03-31 07:37:44.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/misc/error_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      378 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/misc/loading_page.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.854439 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/misc/splash/
--rw-r--r--   0 thegoodz   (501) staff       (20)      883 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      658 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.855448 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/widgets/
--rw-r--r--   0 thegoodz   (501) staff       (20)      888 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1530 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1156 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1007 2023-04-04 16:09:45.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2021 2023-04-05 15:14:39.000000 pysura-0.99.98/pysura/library_data/pysura_frontend/pubspec.yaml
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.857331 pysura-0.99.98/pysura/library_data/pysura_microservice/
--rw-r--r--   0 thegoodz   (501) staff       (20)      596 2023-03-30 01:08:14.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/Dockerfile
--rw-r--r--   0 thegoodz   (501) staff       (20)       30 2023-03-30 05:47:17.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/README.md
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.858190 pysura-0.99.98/pysura/library_data/pysura_microservice/actions/
--rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 22:32:31.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/actions/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1842 2023-04-03 22:19:14.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/actions/action_template.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     5939 2023-04-07 02:34:29.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/actions/action_upload_file.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1452 2023-04-02 23:37:34.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/app.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      754 2023-04-06 00:25:39.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/app_secrets.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.858559 pysura-0.99.98/pysura/library_data/pysura_microservice/crons/
--rw-r--r--   0 thegoodz   (501) staff       (20)       18 2023-03-30 01:13:17.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/crons/__init__.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.859069 pysura-0.99.98/pysura/library_data/pysura_microservice/events/
--rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 01:13:17.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/events/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     2013 2023-04-03 22:19:14.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/events/event_update_user_role.py
--rw-r--r--   0 thegoodz   (501) staff       (20)    10748 2023-04-06 01:14:19.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/pysura_metadata.json
--rw-r--r--   0 thegoodz   (501) staff       (20)     1231 2023-04-07 02:46:07.000000 pysura-0.99.98/pysura/library_data/pysura_microservice/requirements.txt
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.859840 pysura-0.99.98/pysura/library_data/pysura_ssr/
--rw-r--r--   0 thegoodz   (501) staff       (20)       52 2023-04-05 20:24:54.000000 pysura-0.99.98/pysura/library_data/pysura_ssr/.firebaserc
--rw-r--r--   0 thegoodz   (501) staff       (20)      239 2023-04-05 20:25:13.000000 pysura-0.99.98/pysura/library_data/pysura_ssr/firebase.json
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.860729 pysura-0.99.98/pysura/playground/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-04-01 13:54:32.000000 pysura-0.99.98/pysura/playground/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1796 2023-03-31 03:54:29.000000 pysura-0.99.98/pysura/playground/tmp.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     2386 2023-03-31 03:14:29.000000 pysura-0.99.98/pysura/playground/tmp2.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.861649 pysura-0.99.98/pysura/pysura_types/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 16:42:48.000000 pysura-0.99.98/pysura/pysura_types/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)    20772 2023-04-06 00:22:51.000000 pysura-0.99.98/pysura/pysura_types/google_pysura_env.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     6647 2023-04-05 18:30:55.000000 pysura-0.99.98/pysura/pysura_types/root_cmd.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 06:53:37.841598 pysura-0.99.98/pysura.egg-info/
--rw-r--r--   0 thegoodz   (501) staff       (20)    11717 2023-04-07 06:53:37.000000 pysura-0.99.98/pysura.egg-info/PKG-INFO
--rw-r--r--   0 thegoodz   (501) staff       (20)     4300 2023-04-07 06:53:37.000000 pysura-0.99.98/pysura.egg-info/SOURCES.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-04-07 06:53:37.000000 pysura-0.99.98/pysura.egg-info/dependency_links.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)       46 2023-04-07 06:53:37.000000 pysura-0.99.98/pysura.egg-info/entry_points.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)       63 2023-04-07 06:53:37.000000 pysura-0.99.98/pysura.egg-info/requires.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)        7 2023-04-07 06:53:37.000000 pysura-0.99.98/pysura.egg-info/top_level.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)      106 2023-04-07 06:53:37.862590 pysura-0.99.98/setup.cfg
--rw-r--r--   0 thegoodz   (501) staff       (20)     5467 2023-04-07 06:53:21.000000 pysura-0.99.98/setup.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.973083 pysura-0.99.99/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1069 2023-03-20 10:07:23.000000 pysura-0.99.99/LICENSE.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)    11717 2023-04-07 07:02:47.973206 pysura-0.99.99/PKG-INFO
+-rw-r--r--   0 thegoodz   (501) staff       (20)    10980 2023-04-05 22:05:09.000000 pysura-0.99.99/README.rst
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.951514 pysura-0.99.99/pysura/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 15:46:21.000000 pysura-0.99.99/pysura/__init__.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.953126 pysura-0.99.99/pysura/cli/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-22 06:05:11.000000 pysura-0.99.99/pysura/cli/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      771 2023-04-02 23:46:54.000000 pysura-0.99.99/pysura/cli/app.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)   160028 2023-04-07 07:00:50.000000 pysura-0.99.99/pysura/cli/google_root.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.954483 pysura-0.99.99/pysura/faster_api/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-03-31 02:57:53.000000 pysura-0.99.99/pysura/faster_api/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      157 2023-04-01 13:36:35.000000 pysura-0.99.99/pysura/faster_api/enums.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1040 2023-04-02 22:11:13.000000 pysura-0.99.99/pysura/faster_api/models.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)    11936 2023-04-07 01:41:12.000000 pysura-0.99.99/pysura/faster_api/security.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.950479 pysura-0.99.99/pysura/library_data/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.955279 pysura-0.99.99/pysura/library_data/pysura_auth/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-26 12:15:47.000000 pysura-0.99.99/pysura/library_data/pysura_auth/.gcloudignore
+-rw-r--r--   0 thegoodz   (501) staff       (20)     3056 2023-04-01 19:05:04.000000 pysura-0.99.99/pysura/library_data/pysura_auth/main.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      958 2023-03-27 11:41:24.000000 pysura-0.99.99/pysura/library_data/pysura_auth/requirements.txt
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.955964 pysura-0.99.99/pysura/library_data/pysura_frontend/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      691 2023-04-04 01:50:17.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/build.yaml
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.956385 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.958734 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1075 2023-03-31 06:17:27.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/app_color.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2531 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/app_route.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2453 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/app_text_style.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1632 2023-03-31 06:19:26.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/app_theme.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      213 2023-04-04 16:39:17.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/constants.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      412 2023-03-31 06:21:23.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/date_util.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     3988 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/popups.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1285 2023-04-04 04:19:48.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/utils.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.959618 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/controllers/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2400 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1000 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/controllers/data_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1980 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      452 2023-03-31 07:01:52.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/controllers/theme_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.962066 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1034 2023-04-04 03:45:32.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql
+-rw-r--r--   0 thegoodz   (501) staff       (20)    71391 2023-04-04 02:34:58.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)    43063 2023-04-04 01:21:17.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql
+-rw-r--r--   0 thegoodz   (501) staff       (20)   368298 2023-04-04 02:34:58.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      646 2023-04-04 02:16:17.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/user.graphql
+-rw-r--r--   0 thegoodz   (501) staff       (20)    63297 2023-04-04 02:34:58.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/user.graphql.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1966 2023-04-05 15:18:37.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/main.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.949955 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.962972 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/auth/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5781 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2441 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.963608 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.964164 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/action/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     9580 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     4908 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.964669 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/home/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     7574 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5621 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1162 2023-03-31 15:44:39.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      744 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      964 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/main_page_middleware.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.965080 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/settings/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5506 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2298 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.965507 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/misc/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      350 2023-03-31 07:37:44.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/misc/error_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      378 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/misc/loading_page.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.965944 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/misc/splash/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      883 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      658 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.966858 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/widgets/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      888 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1530 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1156 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1007 2023-04-04 16:09:45.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2021 2023-04-05 15:14:39.000000 pysura-0.99.99/pysura/library_data/pysura_frontend/pubspec.yaml
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.968762 pysura-0.99.99/pysura/library_data/pysura_microservice/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      596 2023-03-30 01:08:14.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/Dockerfile
+-rw-r--r--   0 thegoodz   (501) staff       (20)       30 2023-03-30 05:47:17.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/README.md
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.969544 pysura-0.99.99/pysura/library_data/pysura_microservice/actions/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 22:32:31.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/actions/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1842 2023-04-03 22:19:14.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/actions/action_template.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5939 2023-04-07 02:34:29.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/actions/action_upload_file.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1452 2023-04-02 23:37:34.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/app.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      754 2023-04-06 00:25:39.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/app_secrets.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.969887 pysura-0.99.99/pysura/library_data/pysura_microservice/crons/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       18 2023-03-30 01:13:17.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/crons/__init__.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.970331 pysura-0.99.99/pysura/library_data/pysura_microservice/events/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 01:13:17.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/events/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2013 2023-04-03 22:19:14.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/events/event_update_user_role.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)    10748 2023-04-06 01:14:19.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/pysura_metadata.json
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1231 2023-04-07 02:46:07.000000 pysura-0.99.99/pysura/library_data/pysura_microservice/requirements.txt
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.970999 pysura-0.99.99/pysura/library_data/pysura_ssr/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       52 2023-04-05 20:24:54.000000 pysura-0.99.99/pysura/library_data/pysura_ssr/.firebaserc
+-rw-r--r--   0 thegoodz   (501) staff       (20)      239 2023-04-05 20:25:13.000000 pysura-0.99.99/pysura/library_data/pysura_ssr/firebase.json
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.971831 pysura-0.99.99/pysura/playground/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-04-01 13:54:32.000000 pysura-0.99.99/pysura/playground/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1796 2023-03-31 03:54:29.000000 pysura-0.99.99/pysura/playground/tmp.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2386 2023-03-31 03:14:29.000000 pysura-0.99.99/pysura/playground/tmp2.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.972765 pysura-0.99.99/pysura/pysura_types/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 16:42:48.000000 pysura-0.99.99/pysura/pysura_types/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)    20772 2023-04-06 00:22:51.000000 pysura-0.99.99/pysura/pysura_types/google_pysura_env.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     6647 2023-04-05 18:30:55.000000 pysura-0.99.99/pysura/pysura_types/root_cmd.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 07:02:47.952530 pysura-0.99.99/pysura.egg-info/
+-rw-r--r--   0 thegoodz   (501) staff       (20)    11717 2023-04-07 07:02:47.000000 pysura-0.99.99/pysura.egg-info/PKG-INFO
+-rw-r--r--   0 thegoodz   (501) staff       (20)     4300 2023-04-07 07:02:47.000000 pysura-0.99.99/pysura.egg-info/SOURCES.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-04-07 07:02:47.000000 pysura-0.99.99/pysura.egg-info/dependency_links.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)       46 2023-04-07 07:02:47.000000 pysura-0.99.99/pysura.egg-info/entry_points.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)       63 2023-04-07 07:02:47.000000 pysura-0.99.99/pysura.egg-info/requires.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)        7 2023-04-07 07:02:47.000000 pysura-0.99.99/pysura.egg-info/top_level.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)      106 2023-04-07 07:02:47.973641 pysura-0.99.99/setup.cfg
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5467 2023-04-07 07:02:23.000000 pysura-0.99.99/setup.py
```

### Comparing `pysura-0.99.98/LICENSE.txt` & `pysura-0.99.99/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/PKG-INFO` & `pysura-0.99.99/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pysura
-Version: 0.99.98
+Version: 0.99.99
 Summary: A useful tool that provides commands to help ease the installation process of Hasura, and manage its actions, events, and scheduled jobs with baked in phone Auth and a Flutter frontend.
 Home-page: https://github.com/tristengoodz/pysura
 Author: Tristen Harr
 Author-email: tristen@thegoodzapp.com
 Keywords: hasura,graphql,postgresql,google-cloud,python,pysura,backend,backend-in-a-box
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

### Comparing `pysura-0.99.98/README.rst` & `pysura-0.99.99/README.rst`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/cli/app.py` & `pysura-0.99.99/pysura/cli/app.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/cli/google_root.py` & `pysura-0.99.99/pysura/cli/google_root.py`

 * *Files 0% similar despite different names*

```diff
@@ -3090,15 +3090,16 @@
         data = {
             "opts": ["-O", "-x", "--schema-only", "--schema=public", "--clean", "--if-exists"],
             "clean_output": True,
             "source": "default"
         }
         response = requests.post(path, headers=headers, json=data)
         create_sql = response.text
-
+        with open("create.sql", "w") as f:
+            f.write(create_sql)
         env = self.get_env()
         if env.database is None:
             self.log("No database set.", level=logging.ERROR)
             return
         if env.database_credentials is None:
             self.log("No database credentials set.", level=logging.ERROR)
             return
```

### Comparing `pysura-0.99.98/pysura/faster_api/models.py` & `pysura-0.99.99/pysura/faster_api/models.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/faster_api/security.py` & `pysura-0.99.99/pysura/faster_api/security.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_auth/main.py` & `pysura-0.99.99/pysura/library_data/pysura_auth/main.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_auth/requirements.txt` & `pysura-0.99.99/pysura/library_data/pysura_auth/requirements.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/build.yaml` & `pysura-0.99.99/pysura/library_data/pysura_frontend/build.yaml`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/app_color.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/app_color.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/app_route.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/app_route.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/app_text_style.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/app_text_style.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/app_theme.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/app_theme.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/popups.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/popups.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/common/utils.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/common/utils.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/controllers/data_controller.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/controllers/data_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/user.graphql` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/user.graphql`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/graphql/user.graphql.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/graphql/user.graphql.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/main.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/main.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page_controller.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page_controller.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/main_page_middleware.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/main_page_middleware.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page_controller.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page_controller.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart` & `pysura-0.99.99/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_frontend/pubspec.yaml` & `pysura-0.99.99/pysura/library_data/pysura_frontend/pubspec.yaml`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_microservice/Dockerfile` & `pysura-0.99.99/pysura/library_data/pysura_microservice/Dockerfile`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_microservice/actions/action_template.py` & `pysura-0.99.99/pysura/library_data/pysura_microservice/actions/action_template.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_microservice/actions/action_upload_file.py` & `pysura-0.99.99/pysura/library_data/pysura_microservice/actions/action_upload_file.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_microservice/app.py` & `pysura-0.99.99/pysura/library_data/pysura_microservice/app.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_microservice/app_secrets.py` & `pysura-0.99.99/pysura/library_data/pysura_microservice/app_secrets.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_microservice/events/event_update_user_role.py` & `pysura-0.99.99/pysura/library_data/pysura_microservice/events/event_update_user_role.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_microservice/pysura_metadata.json` & `pysura-0.99.99/pysura/library_data/pysura_microservice/pysura_metadata.json`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/library_data/pysura_microservice/requirements.txt` & `pysura-0.99.99/pysura/library_data/pysura_microservice/requirements.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/playground/tmp.py` & `pysura-0.99.99/pysura/playground/tmp.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/playground/tmp2.py` & `pysura-0.99.99/pysura/playground/tmp2.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/pysura_types/google_pysura_env.py` & `pysura-0.99.99/pysura/pysura_types/google_pysura_env.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura/pysura_types/root_cmd.py` & `pysura-0.99.99/pysura/pysura_types/root_cmd.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/pysura.egg-info/PKG-INFO` & `pysura-0.99.99/pysura.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pysura
-Version: 0.99.98
+Version: 0.99.99
 Summary: A useful tool that provides commands to help ease the installation process of Hasura, and manage its actions, events, and scheduled jobs with baked in phone Auth and a Flutter frontend.
 Home-page: https://github.com/tristengoodz/pysura
 Author: Tristen Harr
 Author-email: tristen@thegoodzapp.com
 Keywords: hasura,graphql,postgresql,google-cloud,python,pysura,backend,backend-in-a-box
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

### Comparing `pysura-0.99.98/pysura.egg-info/SOURCES.txt` & `pysura-0.99.99/pysura.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.98/setup.py` & `pysura-0.99.99/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name="pysura",
-    version="0.99.98",
+    version="0.99.99",
     packages=find_packages(),
     entry_points={
         "console_scripts": [
             "pysura=pysura.cli.app:cli"
         ]
     },
     package_dir={"pysura": "pysura"},
```

