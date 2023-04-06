# Comparing `tmp/potato-annotation-1.2.0.8.tar.gz` & `tmp/potato-annotation-1.2.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "potato-annotation-1.2.0.8.tar", last modified: Wed Mar 22 20:26:26 2023, max compression
+gzip compressed data, was "potato-annotation-1.2.0.9.tar", last modified: Thu Mar 23 03:12:32 2023, max compression
```

## Comparing `potato-annotation-1.2.0.8.tar` & `potato-annotation-1.2.0.9.tar`

### file list

```diff
@@ -1,78 +1,78 @@
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.507542 potato-annotation-1.2.0.8/
--rw-r--r--   0 pedropei   (504) staff       (20)     5748 2023-03-12 13:48:10.000000 potato-annotation-1.2.0.8/LICENSE
--rw-r--r--   0 pedropei   (504) staff       (20)      288 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/MANIFEST.in
--rw-r--r--   0 pedropei   (504) staff       (20)    11828 2023-03-22 20:26:26.507295 potato-annotation-1.2.0.8/PKG-INFO
--rw-r--r--   0 pedropei   (504) staff       (20)    11563 2023-03-21 20:53:43.000000 potato-annotation-1.2.0.8/README.md
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.490295 potato-annotation-1.2.0.8/potato/
--rw-r--r--   0 pedropei   (504) staff       (20)       42 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/__init__.py
--rw-r--r--   0 pedropei   (504) staff       (20)     1931 2023-02-09 19:03:46.000000 potato-annotation-1.2.0.8/potato/agreement.py
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.491090 potato-annotation-1.2.0.8/potato/base_html/
--rw-r--r--   0 pedropei   (504) staff       (20)    24046 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/base_html/base_template.html
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.491538 potato-annotation-1.2.0.8/potato/base_html/examples/
--rw-r--r--   0 pedropei   (504) staff       (20)      608 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/base_html/examples/fixed_keybinding_layout.html
--rw-r--r--   0 pedropei   (504) staff       (20)      628 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/base_html/examples/kwargs_example.html
--rw-r--r--   0 pedropei   (504) staff       (20)      447 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/base_html/examples/plain_layout.html
--rw-r--r--   0 pedropei   (504) staff       (20)     7918 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/base_html/header.html
--rw-r--r--   0 pedropei   (504) staff       (20)     2661 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/base_html/home.html
--rw-r--r--   0 pedropei   (504) staff       (20)      147 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/cli.py
--rw-r--r--   0 pedropei   (504) staff       (20)     6707 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/create_task_cli.py
--rw-r--r--   0 pedropei   (504) staff       (20)   102521 2023-03-22 01:21:58.000000 potato-annotation-1.2.0.8/potato/flask_server.py
--rw-r--r--   0 pedropei   (504) staff       (20)     3073 2022-12-19 17:15:12.000000 potato-annotation-1.2.0.8/potato/remove_users_from_queue.py
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.492445 potato-annotation-1.2.0.8/potato/server_utils/
--rw-r--r--   0 pedropei   (504) staff       (20)        0 2023-02-20 00:09:39.000000 potato-annotation-1.2.0.8/potato/server_utils/__init__.py
--rw-r--r--   0 pedropei   (504) staff       (20)     1183 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/server_utils/arg_utils.py
--rw-r--r--   0 pedropei   (504) staff       (20)     2377 2023-03-21 01:46:33.000000 potato-annotation-1.2.0.8/potato/server_utils/cli_utlis.py
--rw-r--r--   0 pedropei   (504) staff       (20)     3476 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.8/potato/server_utils/config_module.py
--rw-r--r--   0 pedropei   (504) staff       (20)    21654 2023-03-22 20:12:13.000000 potato-annotation-1.2.0.8/potato/server_utils/front_end.py
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.498286 potato-annotation-1.2.0.8/potato/server_utils/schemas/
--rw-r--r--   0 pedropei   (504) staff       (20)      411 2023-03-12 05:08:35.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/__init__.py
--rw-r--r--   0 pedropei   (504) staff       (20)     4196 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/likert.py
--rw-r--r--   0 pedropei   (504) staff       (20)     3892 2023-02-13 13:58:08.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/multirate.py
--rw-r--r--   0 pedropei   (504) staff       (20)     6363 2023-03-20 02:22:32.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/multiselect.py
--rw-r--r--   0 pedropei   (504) staff       (20)     3235 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/number.py
--rw-r--r--   0 pedropei   (504) staff       (20)      254 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/pure_display.py
--rw-r--r--   0 pedropei   (504) staff       (20)     6093 2023-03-20 02:22:38.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/radio.py
--rw-r--r--   0 pedropei   (504) staff       (20)     2927 2023-03-21 01:40:54.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/select.py
--rw-r--r--   0 pedropei   (504) staff       (20)     8849 2023-03-12 05:08:35.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/span.py
--rw-r--r--   0 pedropei   (504) staff       (20)     4784 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/server_utils/schemas/textbox.py
--rw-r--r--   0 pedropei   (504) staff       (20)     4264 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/setup_multilingual_config.py
--rw-r--r--   0 pedropei   (504) staff       (20)     4195 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/setup_multitask_config.py
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.501200 potato-annotation-1.2.0.8/potato/static/
--rw-r--r--   0 pedropei   (504) staff       (20)    51143 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/bootstrap.js
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.501341 potato-annotation-1.2.0.8/potato/static/fonts/
--rw-r--r--   0 pedropei   (504) staff       (20)    77160 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/fonts/fontawesome-webfont.woff2
--rw-r--r--   0 pedropei   (504) staff       (20)     1906 2023-02-14 16:23:59.000000 potato-annotation-1.2.0.8/potato/static/function.js
--rw-r--r--   0 pedropei   (504) staff       (20)     3798 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/img-01.webp
--rw-r--r--   0 pedropei   (504) staff       (20)    86659 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/jquery-3.js
--rw-r--r--   0 pedropei   (504) staff       (20)      875 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/main.js
--rw-r--r--   0 pedropei   (504) staff       (20)    34239 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/popper.js
--rw-r--r--   0 pedropei   (504) staff       (20)    66664 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/select2.js
--rw-r--r--   0 pedropei   (504) staff       (20)    18387 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/sha256.js
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.504496 potato-annotation-1.2.0.8/potato/static/styles/
--rw-r--r--   0 pedropei   (504) staff       (20)    17502 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/styles/animate.css
--rw-r--r--   0 pedropei   (504) staff       (20)   124962 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/styles/bootstrap.css
--rw-r--r--   0 pedropei   (504) staff       (20)    31000 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/styles/font-awesome.css
--rw-r--r--   0 pedropei   (504) staff       (20)    19686 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/styles/hamburgers.css
--rw-r--r--   0 pedropei   (504) staff       (20)     6702 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/styles/main.css
--rw-r--r--   0 pedropei   (504) staff       (20)    15196 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/styles/select2.css
--rw-r--r--   0 pedropei   (504) staff       (20)      771 2023-02-16 02:45:18.000000 potato-annotation-1.2.0.8/potato/static/styles/style.css
--rw-r--r--   0 pedropei   (504) staff       (20)    70790 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/styles/util.css
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.505101 potato-annotation-1.2.0.8/potato/static/survey_assets/
--rw-r--r--   0 pedropei   (504) staff       (20)    11223 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/survey_assets/country_dropdown_list.html
--rw-r--r--   0 pedropei   (504) staff       (20)     1834 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/survey_assets/ethnicity_dropdown_list.html
--rw-r--r--   0 pedropei   (504) staff       (20)     1376 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/survey_assets/religion_dropdown_list.html
--rw-r--r--   0 pedropei   (504) staff       (20)     5640 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/static/tilt.js
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.506227 potato-annotation-1.2.0.8/potato/templates/
--rwxr-xr-x   0 pedropei   (504) staff       (20)      184 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/templates/congrats.html
--rwxr-xr-x   0 pedropei   (504) staff       (20)      150 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/templates/error.html
--rwxr-xr-x   0 pedropei   (504) staff       (20)    15973 2022-12-20 21:24:49.000000 potato-annotation-1.2.0.8/potato/templates/home.html
--rwxr-xr-x   0 pedropei   (504) staff       (20)    15934 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/templates/id_login_home.html
--rwxr-xr-x   0 pedropei   (504) staff       (20)     5395 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.8/potato/templates/signup.html
-drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-22 20:26:26.507079 potato-annotation-1.2.0.8/potato_annotation.egg-info/
--rw-r--r--   0 pedropei   (504) staff       (20)    11828 2023-03-22 20:26:26.000000 potato-annotation-1.2.0.8/potato_annotation.egg-info/PKG-INFO
--rw-r--r--   0 pedropei   (504) staff       (20)     2103 2023-03-22 20:26:26.000000 potato-annotation-1.2.0.8/potato_annotation.egg-info/SOURCES.txt
--rw-r--r--   0 pedropei   (504) staff       (20)        1 2023-03-22 20:26:26.000000 potato-annotation-1.2.0.8/potato_annotation.egg-info/dependency_links.txt
--rw-r--r--   0 pedropei   (504) staff       (20)       45 2023-03-22 20:26:26.000000 potato-annotation-1.2.0.8/potato_annotation.egg-info/entry_points.txt
--rw-r--r--   0 pedropei   (504) staff       (20)        7 2023-03-22 20:26:26.000000 potato-annotation-1.2.0.8/potato_annotation.egg-info/top_level.txt
--rw-r--r--   0 pedropei   (504) staff       (20)       38 2023-03-22 20:26:26.507583 potato-annotation-1.2.0.8/setup.cfg
--rw-r--r--   0 pedropei   (504) staff       (20)      593 2023-03-22 20:23:54.000000 potato-annotation-1.2.0.8/setup.py
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.393208 potato-annotation-1.2.0.9/
+-rw-r--r--   0 pedropei   (504) staff       (20)     5748 2023-03-12 13:48:10.000000 potato-annotation-1.2.0.9/LICENSE
+-rw-r--r--   0 pedropei   (504) staff       (20)      288 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/MANIFEST.in
+-rw-r--r--   0 pedropei   (504) staff       (20)    11828 2023-03-23 03:12:32.392945 potato-annotation-1.2.0.9/PKG-INFO
+-rw-r--r--   0 pedropei   (504) staff       (20)    11563 2023-03-21 20:53:43.000000 potato-annotation-1.2.0.9/README.md
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.373037 potato-annotation-1.2.0.9/potato/
+-rw-r--r--   0 pedropei   (504) staff       (20)       42 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/__init__.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     1931 2023-02-09 19:03:46.000000 potato-annotation-1.2.0.9/potato/agreement.py
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.373900 potato-annotation-1.2.0.9/potato/base_html/
+-rw-r--r--   0 pedropei   (504) staff       (20)    24046 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/base_html/base_template.html
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.374573 potato-annotation-1.2.0.9/potato/base_html/examples/
+-rw-r--r--   0 pedropei   (504) staff       (20)      608 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/base_html/examples/fixed_keybinding_layout.html
+-rw-r--r--   0 pedropei   (504) staff       (20)      628 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/base_html/examples/kwargs_example.html
+-rw-r--r--   0 pedropei   (504) staff       (20)      447 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/base_html/examples/plain_layout.html
+-rw-r--r--   0 pedropei   (504) staff       (20)     7918 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/base_html/header.html
+-rw-r--r--   0 pedropei   (504) staff       (20)     2661 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/base_html/home.html
+-rw-r--r--   0 pedropei   (504) staff       (20)      147 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/cli.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     6707 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/create_task_cli.py
+-rw-r--r--   0 pedropei   (504) staff       (20)   102521 2023-03-22 01:21:58.000000 potato-annotation-1.2.0.9/potato/flask_server.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     3073 2022-12-19 17:15:12.000000 potato-annotation-1.2.0.9/potato/remove_users_from_queue.py
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.375813 potato-annotation-1.2.0.9/potato/server_utils/
+-rw-r--r--   0 pedropei   (504) staff       (20)        0 2023-02-20 00:09:39.000000 potato-annotation-1.2.0.9/potato/server_utils/__init__.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     1183 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/server_utils/arg_utils.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     2377 2023-03-21 01:46:33.000000 potato-annotation-1.2.0.9/potato/server_utils/cli_utlis.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     3476 2023-03-21 01:11:11.000000 potato-annotation-1.2.0.9/potato/server_utils/config_module.py
+-rw-r--r--   0 pedropei   (504) staff       (20)    21654 2023-03-22 20:12:13.000000 potato-annotation-1.2.0.9/potato/server_utils/front_end.py
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.378998 potato-annotation-1.2.0.9/potato/server_utils/schemas/
+-rw-r--r--   0 pedropei   (504) staff       (20)      411 2023-03-12 05:08:35.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/__init__.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     4196 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/likert.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     3892 2023-02-13 13:58:08.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/multirate.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     6363 2023-03-20 02:22:32.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/multiselect.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     3235 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/number.py
+-rw-r--r--   0 pedropei   (504) staff       (20)      254 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/pure_display.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     6093 2023-03-20 02:22:38.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/radio.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     2927 2023-03-21 01:40:54.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/select.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     9876 2023-03-23 03:00:55.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/span.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     4784 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/server_utils/schemas/textbox.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     4264 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/setup_multilingual_config.py
+-rw-r--r--   0 pedropei   (504) staff       (20)     4195 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/setup_multitask_config.py
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.383259 potato-annotation-1.2.0.9/potato/static/
+-rw-r--r--   0 pedropei   (504) staff       (20)    51143 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/bootstrap.js
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.384198 potato-annotation-1.2.0.9/potato/static/fonts/
+-rw-r--r--   0 pedropei   (504) staff       (20)    77160 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/fonts/fontawesome-webfont.woff2
+-rw-r--r--   0 pedropei   (504) staff       (20)     1906 2023-02-14 16:23:59.000000 potato-annotation-1.2.0.9/potato/static/function.js
+-rw-r--r--   0 pedropei   (504) staff       (20)     3798 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/img-01.webp
+-rw-r--r--   0 pedropei   (504) staff       (20)    86659 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/jquery-3.js
+-rw-r--r--   0 pedropei   (504) staff       (20)      875 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/main.js
+-rw-r--r--   0 pedropei   (504) staff       (20)    34239 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/popper.js
+-rw-r--r--   0 pedropei   (504) staff       (20)    66664 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/select2.js
+-rw-r--r--   0 pedropei   (504) staff       (20)    18387 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/sha256.js
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.388239 potato-annotation-1.2.0.9/potato/static/styles/
+-rw-r--r--   0 pedropei   (504) staff       (20)    17502 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/styles/animate.css
+-rw-r--r--   0 pedropei   (504) staff       (20)   124962 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/styles/bootstrap.css
+-rw-r--r--   0 pedropei   (504) staff       (20)    31000 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/styles/font-awesome.css
+-rw-r--r--   0 pedropei   (504) staff       (20)    19686 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/styles/hamburgers.css
+-rw-r--r--   0 pedropei   (504) staff       (20)     6702 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/styles/main.css
+-rw-r--r--   0 pedropei   (504) staff       (20)    15196 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/styles/select2.css
+-rw-r--r--   0 pedropei   (504) staff       (20)      771 2023-02-16 02:45:18.000000 potato-annotation-1.2.0.9/potato/static/styles/style.css
+-rw-r--r--   0 pedropei   (504) staff       (20)    70790 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/styles/util.css
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.389361 potato-annotation-1.2.0.9/potato/static/survey_assets/
+-rw-r--r--   0 pedropei   (504) staff       (20)    11223 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/survey_assets/country_dropdown_list.html
+-rw-r--r--   0 pedropei   (504) staff       (20)     1834 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/survey_assets/ethnicity_dropdown_list.html
+-rw-r--r--   0 pedropei   (504) staff       (20)     1376 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/survey_assets/religion_dropdown_list.html
+-rw-r--r--   0 pedropei   (504) staff       (20)     5640 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/static/tilt.js
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.391174 potato-annotation-1.2.0.9/potato/templates/
+-rwxr-xr-x   0 pedropei   (504) staff       (20)      184 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/templates/congrats.html
+-rwxr-xr-x   0 pedropei   (504) staff       (20)      150 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/templates/error.html
+-rwxr-xr-x   0 pedropei   (504) staff       (20)    15973 2022-12-20 21:24:49.000000 potato-annotation-1.2.0.9/potato/templates/home.html
+-rwxr-xr-x   0 pedropei   (504) staff       (20)    15934 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/templates/id_login_home.html
+-rwxr-xr-x   0 pedropei   (504) staff       (20)     5395 2022-12-08 05:48:04.000000 potato-annotation-1.2.0.9/potato/templates/signup.html
+drwxr-xr-x   0 pedropei   (504) staff       (20)        0 2023-03-23 03:12:32.392463 potato-annotation-1.2.0.9/potato_annotation.egg-info/
+-rw-r--r--   0 pedropei   (504) staff       (20)    11828 2023-03-23 03:12:32.000000 potato-annotation-1.2.0.9/potato_annotation.egg-info/PKG-INFO
+-rw-r--r--   0 pedropei   (504) staff       (20)     2103 2023-03-23 03:12:32.000000 potato-annotation-1.2.0.9/potato_annotation.egg-info/SOURCES.txt
+-rw-r--r--   0 pedropei   (504) staff       (20)        1 2023-03-23 03:12:32.000000 potato-annotation-1.2.0.9/potato_annotation.egg-info/dependency_links.txt
+-rw-r--r--   0 pedropei   (504) staff       (20)       45 2023-03-23 03:12:32.000000 potato-annotation-1.2.0.9/potato_annotation.egg-info/entry_points.txt
+-rw-r--r--   0 pedropei   (504) staff       (20)        7 2023-03-23 03:12:32.000000 potato-annotation-1.2.0.9/potato_annotation.egg-info/top_level.txt
+-rw-r--r--   0 pedropei   (504) staff       (20)       38 2023-03-23 03:12:32.393255 potato-annotation-1.2.0.9/setup.cfg
+-rw-r--r--   0 pedropei   (504) staff       (20)      593 2023-03-23 03:12:25.000000 potato-annotation-1.2.0.9/setup.py
```

### Comparing `potato-annotation-1.2.0.8/LICENSE` & `potato-annotation-1.2.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/PKG-INFO` & `potato-annotation-1.2.0.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: potato-annotation
-Version: 1.2.0.8
+Version: 1.2.0.9
 Summary: Potato text annotation tool
 Home-page: https://github.com/davidjurgens/potato
 Author: Jiaxin Pei
 Author-email: pedropei@umich.edu
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `potato-annotation-1.2.0.8/README.md` & `potato-annotation-1.2.0.9/README.md`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/agreement.py` & `potato-annotation-1.2.0.9/potato/agreement.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/base_html/base_template.html` & `potato-annotation-1.2.0.9/potato/base_html/base_template.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/base_html/examples/fixed_keybinding_layout.html` & `potato-annotation-1.2.0.9/potato/base_html/examples/fixed_keybinding_layout.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/base_html/examples/kwargs_example.html` & `potato-annotation-1.2.0.9/potato/base_html/examples/kwargs_example.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/base_html/header.html` & `potato-annotation-1.2.0.9/potato/base_html/header.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/base_html/home.html` & `potato-annotation-1.2.0.9/potato/base_html/home.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/create_task_cli.py` & `potato-annotation-1.2.0.9/potato/create_task_cli.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/flask_server.py` & `potato-annotation-1.2.0.9/potato/flask_server.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/remove_users_from_queue.py` & `potato-annotation-1.2.0.9/potato/remove_users_from_queue.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/arg_utils.py` & `potato-annotation-1.2.0.9/potato/server_utils/arg_utils.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/cli_utlis.py` & `potato-annotation-1.2.0.9/potato/server_utils/cli_utlis.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/config_module.py` & `potato-annotation-1.2.0.9/potato/server_utils/config_module.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/front_end.py` & `potato-annotation-1.2.0.9/potato/server_utils/front_end.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/schemas/likert.py` & `potato-annotation-1.2.0.9/potato/server_utils/schemas/likert.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/schemas/multirate.py` & `potato-annotation-1.2.0.9/potato/server_utils/schemas/multirate.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/schemas/multiselect.py` & `potato-annotation-1.2.0.9/potato/server_utils/schemas/multiselect.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/schemas/number.py` & `potato-annotation-1.2.0.9/potato/server_utils/schemas/number.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/schemas/radio.py` & `potato-annotation-1.2.0.9/potato/server_utils/schemas/radio.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/schemas/select.py` & `potato-annotation-1.2.0.9/potato/server_utils/schemas/select.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/schemas/span.py` & `potato-annotation-1.2.0.9/potato/server_utils/schemas/span.py`

 * *Files 9% similar despite different names*

```diff
@@ -250,9 +250,35 @@
             br_label=br_label,
             is_checked=is_checked,
             name_with_span=name_with_span,
             bg_color=span_color.replace(")", ",0.25)"),
             span_color=span_color,
         )
 
+    # allow annotators to choose bad_text label
+    bad_text_schematic = ""
+    if "label_content" in annotation_scheme.get("bad_text_label", {}):
+        name = annotation_scheme["name"] + ":::" + "bad_text"
+        bad_text_schematic = (
+            (
+                    ' <input class="{class_name}" type="checkbox" id="{id}" name="{name}" value="{value}" onclick="onlyOne(this)" validation="{validation}">'
+                    + ' {line_break} <label for="{label_for}" {label_args}>{label_text}</label>'
+            )
+        ).format(
+            class_name=annotation_scheme["name"],
+            id=name,
+            name=name,
+            value=0,
+            validation=validation,
+            line_break="",
+            label_for=name,
+            label_args="",
+            label_text=annotation_scheme["bad_text_label"]["label_content"],
+        )
+        key_bindings.append(
+            (0, class_name + ": " + annotation_scheme["bad_text_label"]["label_content"])
+        )
+
+    schematic += bad_text_schematic
+
     schematic += "  </fieldset>\n</form>\n"
     return schematic, key_bindings
```

### Comparing `potato-annotation-1.2.0.8/potato/server_utils/schemas/textbox.py` & `potato-annotation-1.2.0.9/potato/server_utils/schemas/textbox.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/setup_multilingual_config.py` & `potato-annotation-1.2.0.9/potato/setup_multilingual_config.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/setup_multitask_config.py` & `potato-annotation-1.2.0.9/potato/setup_multitask_config.py`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/bootstrap.js` & `potato-annotation-1.2.0.9/potato/static/bootstrap.js`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/fonts/fontawesome-webfont.woff2` & `potato-annotation-1.2.0.9/potato/static/fonts/fontawesome-webfont.woff2`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/function.js` & `potato-annotation-1.2.0.9/potato/static/function.js`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/img-01.webp` & `potato-annotation-1.2.0.9/potato/static/img-01.webp`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/jquery-3.js` & `potato-annotation-1.2.0.9/potato/static/jquery-3.js`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/main.js` & `potato-annotation-1.2.0.9/potato/static/main.js`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/popper.js` & `potato-annotation-1.2.0.9/potato/static/popper.js`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/select2.js` & `potato-annotation-1.2.0.9/potato/static/select2.js`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/sha256.js` & `potato-annotation-1.2.0.9/potato/static/sha256.js`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/styles/animate.css` & `potato-annotation-1.2.0.9/potato/static/styles/animate.css`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/styles/bootstrap.css` & `potato-annotation-1.2.0.9/potato/static/styles/bootstrap.css`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/styles/font-awesome.css` & `potato-annotation-1.2.0.9/potato/static/styles/font-awesome.css`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/styles/hamburgers.css` & `potato-annotation-1.2.0.9/potato/static/styles/hamburgers.css`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/styles/main.css` & `potato-annotation-1.2.0.9/potato/static/styles/main.css`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/styles/select2.css` & `potato-annotation-1.2.0.9/potato/static/styles/select2.css`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/styles/style.css` & `potato-annotation-1.2.0.9/potato/static/styles/style.css`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/styles/util.css` & `potato-annotation-1.2.0.9/potato/static/styles/util.css`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/survey_assets/country_dropdown_list.html` & `potato-annotation-1.2.0.9/potato/static/survey_assets/country_dropdown_list.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/survey_assets/ethnicity_dropdown_list.html` & `potato-annotation-1.2.0.9/potato/static/survey_assets/ethnicity_dropdown_list.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/survey_assets/religion_dropdown_list.html` & `potato-annotation-1.2.0.9/potato/static/survey_assets/religion_dropdown_list.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/static/tilt.js` & `potato-annotation-1.2.0.9/potato/static/tilt.js`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/templates/home.html` & `potato-annotation-1.2.0.9/potato/templates/home.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/templates/id_login_home.html` & `potato-annotation-1.2.0.9/potato/templates/id_login_home.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato/templates/signup.html` & `potato-annotation-1.2.0.9/potato/templates/signup.html`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/potato_annotation.egg-info/PKG-INFO` & `potato-annotation-1.2.0.9/potato_annotation.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: potato-annotation
-Version: 1.2.0.8
+Version: 1.2.0.9
 Summary: Potato text annotation tool
 Home-page: https://github.com/davidjurgens/potato
 Author: Jiaxin Pei
 Author-email: pedropei@umich.edu
 Description-Content-Type: text/markdown
 License-File: LICENSE
```

### Comparing `potato-annotation-1.2.0.8/potato_annotation.egg-info/SOURCES.txt` & `potato-annotation-1.2.0.9/potato_annotation.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `potato-annotation-1.2.0.8/setup.py` & `potato-annotation-1.2.0.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 with open("README.md", "r") as fh:
     long_description = fh.read()
 setup(
     name='potato-annotation',
-    version='1.2.0.8',
+    version='1.2.0.9',
     packages=find_packages(),
     entry_points={
         'console_scripts': [
             'potato = potato.cli:potato',
         ],
     },
     url="https://github.com/davidjurgens/potato",
```

