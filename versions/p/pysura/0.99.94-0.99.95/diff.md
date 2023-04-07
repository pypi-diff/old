# Comparing `tmp/pysura-0.99.94.tar.gz` & `tmp/pysura-0.99.95.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pysura-0.99.94.tar", last modified: Fri Apr  7 03:13:10 2023, max compression
+gzip compressed data, was "pysura-0.99.95.tar", last modified: Fri Apr  7 03:51:09 2023, max compression
```

## Comparing `pysura-0.99.94.tar` & `pysura-0.99.95.tar`

### file list

```diff
@@ -1,110 +1,110 @@
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.189808 pysura-0.99.94/
--rw-r--r--   0 thegoodz   (501) staff       (20)     1069 2023-03-20 10:07:23.000000 pysura-0.99.94/LICENSE.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)    11717 2023-04-07 03:13:10.189895 pysura-0.99.94/PKG-INFO
--rw-r--r--   0 thegoodz   (501) staff       (20)    10980 2023-04-05 22:05:09.000000 pysura-0.99.94/README.rst
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.169838 pysura-0.99.94/pysura/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 15:46:21.000000 pysura-0.99.94/pysura/__init__.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.171213 pysura-0.99.94/pysura/cli/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-22 06:05:11.000000 pysura-0.99.94/pysura/cli/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      771 2023-04-02 23:46:54.000000 pysura-0.99.94/pysura/cli/app.py
--rw-r--r--   0 thegoodz   (501) staff       (20)   158061 2023-04-07 01:16:17.000000 pysura-0.99.94/pysura/cli/google_root.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.173062 pysura-0.99.94/pysura/faster_api/
--rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-03-31 02:57:53.000000 pysura-0.99.94/pysura/faster_api/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      157 2023-04-01 13:36:35.000000 pysura-0.99.94/pysura/faster_api/enums.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1040 2023-04-02 22:11:13.000000 pysura-0.99.94/pysura/faster_api/models.py
--rw-r--r--   0 thegoodz   (501) staff       (20)    11936 2023-04-07 01:41:12.000000 pysura-0.99.94/pysura/faster_api/security.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.168767 pysura-0.99.94/pysura/library_data/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.173736 pysura-0.99.94/pysura/library_data/pysura_auth/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-26 12:15:47.000000 pysura-0.99.94/pysura/library_data/pysura_auth/.gcloudignore
--rw-r--r--   0 thegoodz   (501) staff       (20)     3056 2023-04-01 19:05:04.000000 pysura-0.99.94/pysura/library_data/pysura_auth/main.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      958 2023-03-27 11:41:24.000000 pysura-0.99.94/pysura/library_data/pysura_auth/requirements.txt
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.174267 pysura-0.99.94/pysura/library_data/pysura_frontend/
--rw-r--r--   0 thegoodz   (501) staff       (20)      691 2023-04-04 01:50:17.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/build.yaml
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.174516 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.176728 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/
--rw-r--r--   0 thegoodz   (501) staff       (20)     1075 2023-03-31 06:17:27.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/app_color.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2531 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/app_route.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2453 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/app_text_style.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1632 2023-03-31 06:19:26.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/app_theme.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      213 2023-04-04 16:39:17.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/constants.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      412 2023-03-31 06:21:23.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/date_util.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     3988 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/popups.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1285 2023-04-04 04:19:48.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/utils.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.177552 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/controllers/
--rw-r--r--   0 thegoodz   (501) staff       (20)     2400 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1000 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/controllers/data_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1980 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      452 2023-03-31 07:01:52.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/controllers/theme_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.179974 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/
--rw-r--r--   0 thegoodz   (501) staff       (20)     1034 2023-04-04 03:45:32.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql
--rw-r--r--   0 thegoodz   (501) staff       (20)    71391 2023-04-04 02:34:58.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)    43063 2023-04-04 01:21:17.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql
--rw-r--r--   0 thegoodz   (501) staff       (20)   368298 2023-04-04 02:34:58.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      646 2023-04-04 02:16:17.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/user.graphql
--rw-r--r--   0 thegoodz   (501) staff       (20)    63297 2023-04-04 02:34:58.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/user.graphql.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1966 2023-04-05 15:18:37.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/main.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.168232 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.180719 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/auth/
--rw-r--r--   0 thegoodz   (501) staff       (20)     5781 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2441 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.181414 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.181887 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/action/
--rw-r--r--   0 thegoodz   (501) staff       (20)     9580 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     4908 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.182421 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/home/
--rw-r--r--   0 thegoodz   (501) staff       (20)     7574 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     5621 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1162 2023-03-31 15:44:39.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      744 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      964 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/main_page_middleware.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.182844 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/settings/
--rw-r--r--   0 thegoodz   (501) staff       (20)     5506 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2298 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.183302 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/misc/
--rw-r--r--   0 thegoodz   (501) staff       (20)      350 2023-03-31 07:37:44.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/misc/error_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      378 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/misc/loading_page.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.183643 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/misc/splash/
--rw-r--r--   0 thegoodz   (501) staff       (20)      883 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)      658 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page_controller.dart
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.184356 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/widgets/
--rw-r--r--   0 thegoodz   (501) staff       (20)      888 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1530 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1156 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     1007 2023-04-04 16:09:45.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart
--rw-r--r--   0 thegoodz   (501) staff       (20)     2021 2023-04-05 15:14:39.000000 pysura-0.99.94/pysura/library_data/pysura_frontend/pubspec.yaml
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.185920 pysura-0.99.94/pysura/library_data/pysura_microservice/
--rw-r--r--   0 thegoodz   (501) staff       (20)      596 2023-03-30 01:08:14.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/Dockerfile
--rw-r--r--   0 thegoodz   (501) staff       (20)       30 2023-03-30 05:47:17.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/README.md
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.186711 pysura-0.99.94/pysura/library_data/pysura_microservice/actions/
--rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 22:32:31.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/actions/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1842 2023-04-03 22:19:14.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/actions/action_template.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     5939 2023-04-07 02:34:29.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/actions/action_upload_file.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1452 2023-04-02 23:37:34.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/app.py
--rw-r--r--   0 thegoodz   (501) staff       (20)      754 2023-04-06 00:25:39.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/app_secrets.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.187039 pysura-0.99.94/pysura/library_data/pysura_microservice/crons/
--rw-r--r--   0 thegoodz   (501) staff       (20)       18 2023-03-30 01:13:17.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/crons/__init__.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.187574 pysura-0.99.94/pysura/library_data/pysura_microservice/events/
--rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 01:13:17.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/events/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     2013 2023-04-03 22:19:14.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/events/event_update_user_role.py
--rw-r--r--   0 thegoodz   (501) staff       (20)    10748 2023-04-06 01:14:19.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/pysura_metadata.json
--rw-r--r--   0 thegoodz   (501) staff       (20)     1231 2023-04-07 02:46:07.000000 pysura-0.99.94/pysura/library_data/pysura_microservice/requirements.txt
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.188147 pysura-0.99.94/pysura/library_data/pysura_ssr/
--rw-r--r--   0 thegoodz   (501) staff       (20)       52 2023-04-05 20:24:54.000000 pysura-0.99.94/pysura/library_data/pysura_ssr/.firebaserc
--rw-r--r--   0 thegoodz   (501) staff       (20)      239 2023-04-05 20:25:13.000000 pysura-0.99.94/pysura/library_data/pysura_ssr/firebase.json
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.188781 pysura-0.99.94/pysura/playground/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-04-01 13:54:32.000000 pysura-0.99.94/pysura/playground/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     1796 2023-03-31 03:54:29.000000 pysura-0.99.94/pysura/playground/tmp.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     2386 2023-03-31 03:14:29.000000 pysura-0.99.94/pysura/playground/tmp2.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.189566 pysura-0.99.94/pysura/pysura_types/
--rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 16:42:48.000000 pysura-0.99.94/pysura/pysura_types/__init__.py
--rw-r--r--   0 thegoodz   (501) staff       (20)    20772 2023-04-06 00:22:51.000000 pysura-0.99.94/pysura/pysura_types/google_pysura_env.py
--rw-r--r--   0 thegoodz   (501) staff       (20)     6647 2023-04-05 18:30:55.000000 pysura-0.99.94/pysura/pysura_types/root_cmd.py
-drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:13:10.170670 pysura-0.99.94/pysura.egg-info/
--rw-r--r--   0 thegoodz   (501) staff       (20)    11717 2023-04-07 03:13:10.000000 pysura-0.99.94/pysura.egg-info/PKG-INFO
--rw-r--r--   0 thegoodz   (501) staff       (20)     4300 2023-04-07 03:13:10.000000 pysura-0.99.94/pysura.egg-info/SOURCES.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-04-07 03:13:10.000000 pysura-0.99.94/pysura.egg-info/dependency_links.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)       46 2023-04-07 03:13:10.000000 pysura-0.99.94/pysura.egg-info/entry_points.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)       63 2023-04-07 03:13:10.000000 pysura-0.99.94/pysura.egg-info/requires.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)        7 2023-04-07 03:13:10.000000 pysura-0.99.94/pysura.egg-info/top_level.txt
--rw-r--r--   0 thegoodz   (501) staff       (20)      106 2023-04-07 03:13:10.190325 pysura-0.99.94/setup.cfg
--rw-r--r--   0 thegoodz   (501) staff       (20)     5467 2023-04-07 03:12:37.000000 pysura-0.99.94/setup.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.132585 pysura-0.99.95/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1069 2023-03-20 10:07:23.000000 pysura-0.99.95/LICENSE.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)    11717 2023-04-07 03:51:09.132687 pysura-0.99.95/PKG-INFO
+-rw-r--r--   0 thegoodz   (501) staff       (20)    10980 2023-04-05 22:05:09.000000 pysura-0.99.95/README.rst
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.111792 pysura-0.99.95/pysura/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 15:46:21.000000 pysura-0.99.95/pysura/__init__.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.113139 pysura-0.99.95/pysura/cli/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-22 06:05:11.000000 pysura-0.99.95/pysura/cli/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      771 2023-04-02 23:46:54.000000 pysura-0.99.95/pysura/cli/app.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)   158952 2023-04-07 03:50:20.000000 pysura-0.99.95/pysura/cli/google_root.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.115051 pysura-0.99.95/pysura/faster_api/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-03-31 02:57:53.000000 pysura-0.99.95/pysura/faster_api/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      157 2023-04-01 13:36:35.000000 pysura-0.99.95/pysura/faster_api/enums.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1040 2023-04-02 22:11:13.000000 pysura-0.99.95/pysura/faster_api/models.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)    11936 2023-04-07 01:41:12.000000 pysura-0.99.95/pysura/faster_api/security.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.110545 pysura-0.99.95/pysura/library_data/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.115733 pysura-0.99.95/pysura/library_data/pysura_auth/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-26 12:15:47.000000 pysura-0.99.95/pysura/library_data/pysura_auth/.gcloudignore
+-rw-r--r--   0 thegoodz   (501) staff       (20)     3056 2023-04-01 19:05:04.000000 pysura-0.99.95/pysura/library_data/pysura_auth/main.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      958 2023-03-27 11:41:24.000000 pysura-0.99.95/pysura/library_data/pysura_auth/requirements.txt
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.116256 pysura-0.99.95/pysura/library_data/pysura_frontend/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      691 2023-04-04 01:50:17.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/build.yaml
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.116587 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.118561 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1075 2023-03-31 06:17:27.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/app_color.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2531 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/app_route.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2453 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/app_text_style.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1632 2023-03-31 06:19:26.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/app_theme.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      213 2023-04-04 16:39:17.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/constants.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      412 2023-03-31 06:21:23.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/date_util.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     3988 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/popups.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1285 2023-04-04 04:19:48.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/utils.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.119344 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/controllers/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2400 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1000 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/controllers/data_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1980 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      452 2023-03-31 07:01:52.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/controllers/theme_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.121828 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1034 2023-04-04 03:45:32.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql
+-rw-r--r--   0 thegoodz   (501) staff       (20)    71391 2023-04-04 02:34:58.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)    43063 2023-04-04 01:21:17.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql
+-rw-r--r--   0 thegoodz   (501) staff       (20)   368298 2023-04-04 02:34:58.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      646 2023-04-04 02:16:17.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/user.graphql
+-rw-r--r--   0 thegoodz   (501) staff       (20)    63297 2023-04-04 02:34:58.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/user.graphql.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1966 2023-04-05 15:18:37.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/main.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.110005 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.122618 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/auth/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5781 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2441 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.123222 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.123688 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/action/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     9580 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     4908 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.124167 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/home/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     7574 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5621 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1162 2023-03-31 15:44:39.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      744 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      964 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/main_page_middleware.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.124594 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/settings/
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5506 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2298 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.125055 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/misc/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      350 2023-03-31 07:37:44.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/misc/error_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      378 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/misc/loading_page.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.125404 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/misc/splash/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      883 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)      658 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page_controller.dart
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.126220 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/widgets/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      888 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1530 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1156 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1007 2023-04-04 16:09:45.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2021 2023-04-05 15:14:39.000000 pysura-0.99.95/pysura/library_data/pysura_frontend/pubspec.yaml
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.127976 pysura-0.99.95/pysura/library_data/pysura_microservice/
+-rw-r--r--   0 thegoodz   (501) staff       (20)      596 2023-03-30 01:08:14.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/Dockerfile
+-rw-r--r--   0 thegoodz   (501) staff       (20)       30 2023-03-30 05:47:17.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/README.md
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.128745 pysura-0.99.95/pysura/library_data/pysura_microservice/actions/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 22:32:31.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/actions/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1842 2023-04-03 22:19:14.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/actions/action_template.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5939 2023-04-07 02:34:29.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/actions/action_upload_file.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1452 2023-04-02 23:37:34.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/app.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)      754 2023-04-06 00:25:39.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/app_secrets.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.129107 pysura-0.99.95/pysura/library_data/pysura_microservice/crons/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       18 2023-03-30 01:13:17.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/crons/__init__.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.129636 pysura-0.99.95/pysura/library_data/pysura_microservice/events/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       19 2023-03-30 01:13:17.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/events/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2013 2023-04-03 22:19:14.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/events/event_update_user_role.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)    10748 2023-04-06 01:14:19.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/pysura_metadata.json
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1231 2023-04-07 02:46:07.000000 pysura-0.99.95/pysura/library_data/pysura_microservice/requirements.txt
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.130297 pysura-0.99.95/pysura/library_data/pysura_ssr/
+-rw-r--r--   0 thegoodz   (501) staff       (20)       52 2023-04-05 20:24:54.000000 pysura-0.99.95/pysura/library_data/pysura_ssr/.firebaserc
+-rw-r--r--   0 thegoodz   (501) staff       (20)      239 2023-04-05 20:25:13.000000 pysura-0.99.95/pysura/library_data/pysura_ssr/firebase.json
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.131372 pysura-0.99.95/pysura/playground/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-04-01 13:54:32.000000 pysura-0.99.95/pysura/playground/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     1796 2023-03-31 03:54:29.000000 pysura-0.99.95/pysura/playground/tmp.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     2386 2023-03-31 03:14:29.000000 pysura-0.99.95/pysura/playground/tmp2.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.132284 pysura-0.99.95/pysura/pysura_types/
+-rw-r--r--   0 thegoodz   (501) staff       (20)        0 2023-03-23 16:42:48.000000 pysura-0.99.95/pysura/pysura_types/__init__.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)    20772 2023-04-06 00:22:51.000000 pysura-0.99.95/pysura/pysura_types/google_pysura_env.py
+-rw-r--r--   0 thegoodz   (501) staff       (20)     6647 2023-04-05 18:30:55.000000 pysura-0.99.95/pysura/pysura_types/root_cmd.py
+drwxr-xr-x   0 thegoodz   (501) staff       (20)        0 2023-04-07 03:51:09.112588 pysura-0.99.95/pysura.egg-info/
+-rw-r--r--   0 thegoodz   (501) staff       (20)    11717 2023-04-07 03:51:09.000000 pysura-0.99.95/pysura.egg-info/PKG-INFO
+-rw-r--r--   0 thegoodz   (501) staff       (20)     4300 2023-04-07 03:51:09.000000 pysura-0.99.95/pysura.egg-info/SOURCES.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)        1 2023-04-07 03:51:09.000000 pysura-0.99.95/pysura.egg-info/dependency_links.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)       46 2023-04-07 03:51:09.000000 pysura-0.99.95/pysura.egg-info/entry_points.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)       63 2023-04-07 03:51:09.000000 pysura-0.99.95/pysura.egg-info/requires.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)        7 2023-04-07 03:51:09.000000 pysura-0.99.95/pysura.egg-info/top_level.txt
+-rw-r--r--   0 thegoodz   (501) staff       (20)      106 2023-04-07 03:51:09.133108 pysura-0.99.95/setup.cfg
+-rw-r--r--   0 thegoodz   (501) staff       (20)     5467 2023-04-07 03:50:31.000000 pysura-0.99.95/setup.py
```

### Comparing `pysura-0.99.94/LICENSE.txt` & `pysura-0.99.95/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/PKG-INFO` & `pysura-0.99.95/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pysura
-Version: 0.99.94
+Version: 0.99.95
 Summary: A useful tool that provides commands to help ease the installation process of Hasura, and manage its actions, events, and scheduled jobs with baked in phone Auth and a Flutter frontend.
 Home-page: https://github.com/tristengoodz/pysura
 Author: Tristen Harr
 Author-email: tristen@thegoodzapp.com
 Keywords: hasura,graphql,postgresql,google-cloud,python,pysura,backend,backend-in-a-box
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

### Comparing `pysura-0.99.94/README.rst` & `pysura-0.99.95/README.rst`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/cli/app.py` & `pysura-0.99.95/pysura/cli/app.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/cli/google_root.py` & `pysura-0.99.95/pysura/cli/google_root.py`

 * *Files 1% similar despite different names*

```diff
@@ -3153,14 +3153,85 @@
         self.log(deploy_command, level=logging.DEBUG)
         with open("deploy.txt", "w") as f:
             f.write(deploy_command)
         os.system(deploy_command)
         os.chdir("../..")
         self.set_env(env)
 
+    def do_print_pysura(self, _):
+        env = self.get_env()
+        self.log(f"Pysura App is ready to run!, open the folder named {env.flutter_app_name} in Android Studio!",
+                 level=logging.INFO)
+        assert env.hasura is not None
+        assert env.hasura_metadata is not None
+        if env.hasura.microservice_urls is not None:
+            num_services = len(env.hasura.microservice_urls)
+        else:
+            num_services = 0
+        log_str = f"""
+        Pysura Project Setup Complete!
+
+        The default microservice can be found at:
+        {env.default_microservice_url}/docs
+
+        """
+        actions = [action for action in env.hasura_metadata.actions if
+                   action.definition.handler == "{{HASURA_MICROSERVICE_URL}}"]
+        if len(actions) > 0:
+            log_str += f"""The default microservice has {len(actions)} actions:\n"""
+            for action in actions:
+                log_str += f"""\t{action.name}\n"""
+
+        log_str += f"""\nYou have {num_services} additional microservice(s) deployed."""
+        if num_services > 0:
+            log_str += "\n\tMicroservice URLs:\n"
+
+        for microservice_url in env.hasura.microservice_urls:
+            actions = [action for action in env.hasura_metadata.actions if
+                       action.definition.handler == microservice_url.url_wrapper]
+            log_str += f"""\t{microservice_url.url}\n"""
+            if len(actions) > 0:
+                log_str += f"""\t\t{len(actions)} action(s):\n"""
+                for action in actions:
+                    log_str += f"""\t\t\t{action.name}\n"""
+
+        log_str += f"""
+
+        Your Hasura instance can be found at:
+        {env.hasura_service.status.address.url}/console
+
+        Your Hasura Admin Secret is:
+        {env.hasura.HASURA_GRAPHQL_ADMIN_SECRET}
+
+        The event secret for the all attached microservices is:
+        {env.hasura.HASURA_EVENT_SECRET}
+
+        You can find authorization tokens for your microservice by running your flutter application and logging in, navigate to
+        the settings tab, and click the "Copy GraphQL Token" button and a bearer token will be copied to your clipboard.
+        The bearer token will have the role of the user that is logged in.
+
+        You can find your web application here:
+        https://{env.project.name.split('/')[-1]}.web.app/
+
+
+        """
+
+        test_phone_numbers = env.test_phone_numbers
+        if isinstance(test_phone_numbers, list):
+            for test_phone_number in test_phone_numbers:
+                if test_phone_number.role == "admin":
+                    log_str += f"\nAdmin Phone Number: {test_phone_number.phone_number}\t" \
+                               f"Code: {test_phone_number.code}\n"
+                elif test_phone_number.role == "user":
+                    log_str += f"\nUser Phone Number: {test_phone_number.phone_number}\t" \
+                               f"Code: {test_phone_number.code}\n"
+
+        log_str += "\n\nTo see these credentials again, run print_pysura\n"
+        self.log(log_str, level=logging.INFO)
+
     def do_setup_pysura(self, recurse=0):
         """
         Setups up a Pysura project
         """
         if recurse == "":
             recurse = 0
         else:
@@ -3395,64 +3466,9 @@
                 code=user_code,
                 uid=user_id
             )
             test_phone_numbers.append(user_number)
         if isinstance(test_phone_numbers, list) and len(test_phone_numbers) > 0:
             env.test_phone_numbers = test_phone_numbers
             self.set_env(env)
-        self.log(f"Pysura App is ready to run!, open the folder named {env.flutter_app_name} in Android Studio!",
-                 level=logging.INFO)
-        assert env.hasura is not None
-        assert env.hasura_metadata is not None
-        if env.hasura.microservice_urls is not None:
-            num_services = len(env.hasura.microservice_urls)
-        else:
-            num_services = 0
-        log_str = f"""
-Pysura Project Setup Complete!
-
-The default microservice can be found at:
-{env.default_microservice_url}/docs
 
-"""
-        actions = [action for action in env.hasura_metadata.actions if
-                   action.definition.handler == "{{HASURA_MICROSERVICE_URL}}"]
-        if len(actions) > 0:
-            log_str += f"""The default microservice has {len(actions)} actions:\n"""
-            for action in actions:
-                log_str += f"""\t{action.name}\n"""
-
-        log_str += f"""\nYou have {num_services} additional microservice(s) deployed."""
-        if num_services > 0:
-            log_str += "\n\tMicroservice URLs:\n"
-
-        for microservice_url in env.hasura.microservice_urls:
-            actions = [action for action in env.hasura_metadata.actions if
-                       action.definition.handler == microservice_url.url_wrapper]
-            log_str += f"""\t{microservice_url.url}\n"""
-            if len(actions) > 0:
-                log_str += f"""\t\t{len(actions)} action(s):\n"""
-                for action in actions:
-                    log_str += f"""\t\t\t{action.name}\n"""
-
-        log_str += f"""
-
-Your Hasura instance can be found at:
-{env.hasura_service.status.address.url}/console
-
-Your Hasura Admin Secret is:
-{env.hasura.HASURA_GRAPHQL_ADMIN_SECRET}
-
-The event secret for the all attached microservices is:
-{env.hasura.HASURA_EVENT_SECRET}
-
-You can find authorization tokens for your microservice by running your flutter application and logging in, navigate to
-the settings tab, and click the "Copy GraphQL Token" button and a bearer token will be copied to your clipboard.
-The bearer token will have the role of the user that is logged in.
-
-You can find your web application here:
-https://{env.project.name.split('/')[-1]}.web.app/
-
-
-"""
-
-        self.log(log_str, level=logging.INFO)
+        self.do_print_pysura(None)
```

### Comparing `pysura-0.99.94/pysura/faster_api/models.py` & `pysura-0.99.95/pysura/faster_api/models.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/faster_api/security.py` & `pysura-0.99.95/pysura/faster_api/security.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_auth/main.py` & `pysura-0.99.95/pysura/library_data/pysura_auth/main.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_auth/requirements.txt` & `pysura-0.99.95/pysura/library_data/pysura_auth/requirements.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/build.yaml` & `pysura-0.99.95/pysura/library_data/pysura_frontend/build.yaml`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/app_color.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/app_color.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/app_route.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/app_route.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/app_text_style.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/app_text_style.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/app_theme.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/app_theme.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/popups.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/popups.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/common/utils.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/common/utils.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/controllers/auth_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/controllers/data_controller.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/controllers/data_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/controllers/graphql_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/actions.graphql.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/schema.graphql.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/user.graphql` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/user.graphql`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/graphql/user.graphql.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/graphql/user.graphql.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/main.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/main.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/auth/login_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/auth/login_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page_controller.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/action/action_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page_controller.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/home/home_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/main_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/main_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/main_page_middleware.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/main_page_middleware.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page_controller.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/main/settings/settings_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page_controller.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/pages/misc/splash/splash_page_controller.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/widgets/graphql_provider_widget.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/widgets/phone_number_field.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/widgets/primary_button.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart` & `pysura-0.99.95/pysura/library_data/pysura_frontend/lib/widgets/secondary_button.dart`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_frontend/pubspec.yaml` & `pysura-0.99.95/pysura/library_data/pysura_frontend/pubspec.yaml`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_microservice/Dockerfile` & `pysura-0.99.95/pysura/library_data/pysura_microservice/Dockerfile`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_microservice/actions/action_template.py` & `pysura-0.99.95/pysura/library_data/pysura_microservice/actions/action_template.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_microservice/actions/action_upload_file.py` & `pysura-0.99.95/pysura/library_data/pysura_microservice/actions/action_upload_file.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_microservice/app.py` & `pysura-0.99.95/pysura/library_data/pysura_microservice/app.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_microservice/app_secrets.py` & `pysura-0.99.95/pysura/library_data/pysura_microservice/app_secrets.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_microservice/events/event_update_user_role.py` & `pysura-0.99.95/pysura/library_data/pysura_microservice/events/event_update_user_role.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_microservice/pysura_metadata.json` & `pysura-0.99.95/pysura/library_data/pysura_microservice/pysura_metadata.json`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/library_data/pysura_microservice/requirements.txt` & `pysura-0.99.95/pysura/library_data/pysura_microservice/requirements.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/playground/tmp.py` & `pysura-0.99.95/pysura/playground/tmp.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/playground/tmp2.py` & `pysura-0.99.95/pysura/playground/tmp2.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/pysura_types/google_pysura_env.py` & `pysura-0.99.95/pysura/pysura_types/google_pysura_env.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura/pysura_types/root_cmd.py` & `pysura-0.99.95/pysura/pysura_types/root_cmd.py`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/pysura.egg-info/PKG-INFO` & `pysura-0.99.95/pysura.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pysura
-Version: 0.99.94
+Version: 0.99.95
 Summary: A useful tool that provides commands to help ease the installation process of Hasura, and manage its actions, events, and scheduled jobs with baked in phone Auth and a Flutter frontend.
 Home-page: https://github.com/tristengoodz/pysura
 Author: Tristen Harr
 Author-email: tristen@thegoodzapp.com
 Keywords: hasura,graphql,postgresql,google-cloud,python,pysura,backend,backend-in-a-box
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

### Comparing `pysura-0.99.94/pysura.egg-info/SOURCES.txt` & `pysura-0.99.95/pysura.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pysura-0.99.94/setup.py` & `pysura-0.99.95/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import setup, find_packages
 
 setup(
     name="pysura",
-    version="0.99.94",
+    version="0.99.95",
     packages=find_packages(),
     entry_points={
         "console_scripts": [
             "pysura=pysura.cli.app:cli"
         ]
     },
     package_dir={"pysura": "pysura"},
```

