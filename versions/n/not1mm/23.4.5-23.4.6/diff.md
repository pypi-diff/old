# Comparing `tmp/not1mm-23.4.5.tar.gz` & `tmp/not1mm-23.4.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "not1mm-23.4.5.tar", last modified: Wed Apr  5 15:55:27 2023, max compression
+gzip compressed data, was "not1mm-23.4.6.tar", last modified: Thu Apr  6 17:36:34 2023, max compression
```

## Comparing `not1mm-23.4.5.tar` & `not1mm-23.4.6.tar`

### file list

```diff
@@ -1,78 +1,80 @@
-drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-05 15:55:27.721260 not1mm-23.4.5/
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    35149 2022-05-05 15:15:13.000000 not1mm-23.4.5/LICENSE
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    11831 2023-04-05 15:55:27.721260 not1mm-23.4.5/PKG-INFO
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    11082 2023-04-05 15:34:14.000000 not1mm-23.4.5/README.md
-drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-05 15:55:27.706261 not1mm-23.4.5/not1mm/
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)        0 2022-11-03 15:04:39.000000 not1mm-23.4.5/not1mm/__init__.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    61519 2023-04-05 14:37:43.000000 not1mm-23.4.5/not1mm/__main__.py
-drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-05 15:55:27.715261 not1mm-23.4.5/not1mm/data/
--rw-rw-rw-   0 mbridak   (1000) mbridak   (1000)    16590 2023-02-15 20:52:35.000000 not1mm-23.4.5/not1mm/data/Combinear.qss
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)   203952 2023-01-27 16:44:51.000000 not1mm-23.4.5/not1mm/data/JetBrainsMono-Regular.ttf
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)   542666 2023-02-14 19:22:02.000000 not1mm-23.4.5/not1mm/data/MASTER.SCP
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      387 2023-03-15 16:56:38.000000 not1mm-23.4.5/not1mm/data/check.png
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    89307 2023-03-07 17:30:38.000000 not1mm-23.4.5/not1mm/data/contests.sql
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)  4534539 2023-02-21 19:49:24.000000 not1mm-23.4.5/not1mm/data/cty.json
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      487 2023-03-21 14:20:18.000000 not1mm-23.4.5/not1mm/data/cwmacros.txt
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    19280 2023-03-20 20:22:09.000000 not1mm-23.4.5/not1mm/data/editcontact.ui
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2273 2023-02-21 14:39:24.000000 not1mm-23.4.5/not1mm/data/editmacro.ui
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      474 2023-02-10 02:42:18.000000 not1mm-23.4.5/not1mm/data/greendot.png
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      205 2023-02-09 20:47:40.000000 not1mm-23.4.5/not1mm/data/k6gte-not1mm.desktop
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     4010 2023-02-09 20:45:38.000000 not1mm-23.4.5/not1mm/data/k6gte.not1mm-128.png
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1108 2023-02-09 20:45:03.000000 not1mm-23.4.5/not1mm/data/k6gte.not1mm-32.png
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2152 2023-02-09 20:45:22.000000 not1mm-23.4.5/not1mm/data/k6gte.not1mm-64.png
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      970 2023-03-23 20:14:51.000000 not1mm-23.4.5/not1mm/data/logwindow.ui
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    37714 2023-03-31 15:58:57.000000 not1mm-23.4.5/not1mm/data/main.ui
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    16002 2023-04-03 20:06:41.000000 not1mm-23.4.5/not1mm/data/new_contest.ui
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2018 2023-02-12 17:56:36.000000 not1mm-23.4.5/not1mm/data/opon.ui
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1600 2023-04-03 14:20:44.000000 not1mm-23.4.5/not1mm/data/pickcontest.ui
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      565 2023-02-10 02:42:40.000000 not1mm-23.4.5/not1mm/data/reddot.png
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    35558 2023-03-24 21:02:25.000000 not1mm-23.4.5/not1mm/data/settings.ui
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     4554 2023-02-26 02:19:03.000000 not1mm-23.4.5/not1mm/data/use_qrz_dialog.ui
-drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-05 15:55:27.717261 not1mm-23.4.5/not1mm/lib/
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)        0 2022-11-03 15:04:39.000000 not1mm-23.4.5/not1mm/lib/__init__.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    10342 2023-04-04 19:55:47.000000 not1mm-23.4.5/not1mm/lib/cat_interface.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1772 2023-03-17 21:26:43.000000 not1mm-23.4.5/not1mm/lib/cwinterface.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    25757 2023-04-05 14:32:16.000000 not1mm-23.4.5/not1mm/lib/database.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      357 2023-03-20 13:17:21.000000 not1mm-23.4.5/not1mm/lib/edit_contact.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      559 2023-03-06 17:59:31.000000 not1mm-23.4.5/not1mm/lib/edit_macro.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      363 2023-03-06 18:02:53.000000 not1mm-23.4.5/not1mm/lib/edit_opon.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      734 2023-03-31 15:55:44.000000 not1mm-23.4.5/not1mm/lib/edit_station.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     8841 2023-03-31 16:35:24.000000 not1mm-23.4.5/not1mm/lib/ham_utility.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    13916 2023-03-07 18:49:31.000000 not1mm-23.4.5/not1mm/lib/lookup.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1954 2023-03-17 17:01:08.000000 not1mm-23.4.5/not1mm/lib/multicast.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     4434 2023-03-17 16:20:37.000000 not1mm-23.4.5/not1mm/lib/n1mm.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      354 2023-03-28 20:21:24.000000 not1mm-23.4.5/not1mm/lib/new_contest.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      350 2023-03-06 18:07:06.000000 not1mm-23.4.5/not1mm/lib/qrz_dialog.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      363 2023-03-31 21:22:27.000000 not1mm-23.4.5/not1mm/lib/select_contest.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)       46 2023-04-05 15:35:33.000000 not1mm-23.4.5/not1mm/lib/version.py
--rwxr-xr-x   0 mbridak   (1000) mbridak   (1000)    26394 2023-04-04 23:00:38.000000 not1mm-23.4.5/not1mm/logwindow.py
-drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-05 15:55:27.720260 not1mm-23.4.5/not1mm/plugins/
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)        0 2023-02-20 21:20:03.000000 not1mm-23.4.5/not1mm/plugins/__init__.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2456 2023-03-28 17:33:53.000000 not1mm-23.4.5/not1mm/plugins/arrl_dx_cw.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2459 2023-03-28 17:34:18.000000 not1mm-23.4.5/not1mm/plugins/arrl_dx_phone.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    12679 2023-04-05 15:51:09.000000 not1mm-23.4.5/not1mm/plugins/arrl_field_day.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2464 2023-03-28 17:34:12.000000 not1mm-23.4.5/not1mm/plugins/arrl_rtty_ru.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2465 2023-03-28 17:34:06.000000 not1mm-23.4.5/not1mm/plugins/arrl_ss_cw.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2468 2023-03-28 17:33:59.000000 not1mm-23.4.5/not1mm/plugins/arrl_ss_phone.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    14651 2023-04-02 16:44:37.000000 not1mm-23.4.5/not1mm/plugins/cq_wpx_cw.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    14659 2023-04-03 15:09:21.000000 not1mm-23.4.5/not1mm/plugins/cq_wpx_rtty.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    14655 2023-04-03 15:09:18.000000 not1mm-23.4.5/not1mm/plugins/cq_wpx_ssb.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2153 2023-03-28 17:33:25.000000 not1mm-23.4.5/not1mm/plugins/cqww_dx_cw.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2157 2023-03-28 17:33:25.000000 not1mm-23.4.5/not1mm/plugins/cqww_dx_ssb.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     7177 2023-04-04 14:52:27.000000 not1mm-23.4.5/not1mm/plugins/general_logging.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2725 2023-03-28 17:33:25.000000 not1mm-23.4.5/not1mm/plugins/winter_field_day.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     3906 2023-03-07 21:13:08.000000 not1mm-23.4.5/not1mm/test.py
-drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-05 15:55:27.720260 not1mm-23.4.5/not1mm/testing/
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2297 2023-03-29 19:50:12.000000 not1mm-23.4.5/not1mm/testing/test.py
-drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-05 15:55:27.707261 not1mm-23.4.5/not1mm.egg-info/
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)    11831 2023-04-05 15:55:27.000000 not1mm-23.4.5/not1mm.egg-info/PKG-INFO
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1749 2023-04-05 15:55:27.000000 not1mm-23.4.5/not1mm.egg-info/SOURCES.txt
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)        1 2023-04-05 15:55:27.000000 not1mm-23.4.5/not1mm.egg-info/dependency_links.txt
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)       47 2023-04-05 15:55:27.000000 not1mm-23.4.5/not1mm.egg-info/entry_points.txt
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)       42 2023-04-05 15:55:27.000000 not1mm-23.4.5/not1mm.egg-info/requires.txt
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)       33 2023-04-05 15:55:27.000000 not1mm-23.4.5/not1mm.egg-info/top_level.txt
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1148 2023-04-05 15:35:29.000000 not1mm-23.4.5/pyproject.toml
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)       38 2023-04-05 15:55:27.721260 not1mm-23.4.5/setup.cfg
-drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-05 15:55:27.720260 not1mm-23.4.5/testing/
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2248 2023-03-07 22:04:42.000000 not1mm-23.4.5/testing/test.py
--rw-r--r--   0 mbridak   (1000) mbridak   (1000)      861 2023-03-29 19:39:25.000000 not1mm-23.4.5/testing/text2.py
+drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-06 17:36:34.554216 not1mm-23.4.6/
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    35149 2022-05-05 15:15:13.000000 not1mm-23.4.6/LICENSE
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    12200 2023-04-06 17:36:34.553217 not1mm-23.4.6/PKG-INFO
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    11451 2023-04-06 17:30:46.000000 not1mm-23.4.6/README.md
+drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-06 17:36:34.534217 not1mm-23.4.6/not1mm/
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)        0 2022-11-03 15:04:39.000000 not1mm-23.4.6/not1mm/__init__.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    61666 2023-04-06 16:51:30.000000 not1mm-23.4.6/not1mm/__main__.py
+drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-06 17:36:34.546217 not1mm-23.4.6/not1mm/data/
+-rw-rw-rw-   0 mbridak   (1000) mbridak   (1000)    16590 2023-02-15 20:52:35.000000 not1mm-23.4.6/not1mm/data/Combinear.qss
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)   203952 2023-01-27 16:44:51.000000 not1mm-23.4.6/not1mm/data/JetBrainsMono-Regular.ttf
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)   542666 2023-02-14 19:22:02.000000 not1mm-23.4.6/not1mm/data/MASTER.SCP
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      387 2023-03-15 16:56:38.000000 not1mm-23.4.6/not1mm/data/check.png
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    89307 2023-03-07 17:30:38.000000 not1mm-23.4.6/not1mm/data/contests.sql
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)  4534539 2023-02-21 19:49:24.000000 not1mm-23.4.6/not1mm/data/cty.json
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      487 2023-03-21 14:20:18.000000 not1mm-23.4.6/not1mm/data/cwmacros.txt
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    19280 2023-03-20 20:22:09.000000 not1mm-23.4.6/not1mm/data/editcontact.ui
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2273 2023-02-21 14:39:24.000000 not1mm-23.4.6/not1mm/data/editmacro.ui
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      474 2023-02-10 02:42:18.000000 not1mm-23.4.6/not1mm/data/greendot.png
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      205 2023-02-09 20:47:40.000000 not1mm-23.4.6/not1mm/data/k6gte-not1mm.desktop
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     4010 2023-02-09 20:45:38.000000 not1mm-23.4.6/not1mm/data/k6gte.not1mm-128.png
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1108 2023-02-09 20:45:03.000000 not1mm-23.4.6/not1mm/data/k6gte.not1mm-32.png
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2152 2023-02-09 20:45:22.000000 not1mm-23.4.6/not1mm/data/k6gte.not1mm-64.png
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      970 2023-03-23 20:14:51.000000 not1mm-23.4.6/not1mm/data/logwindow.ui
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    37714 2023-04-05 21:11:39.000000 not1mm-23.4.6/not1mm/data/main.ui
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    16209 2023-04-06 14:33:00.000000 not1mm-23.4.6/not1mm/data/new_contest.ui
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2018 2023-02-12 17:56:36.000000 not1mm-23.4.6/not1mm/data/opon.ui
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1600 2023-04-03 14:20:44.000000 not1mm-23.4.6/not1mm/data/pickcontest.ui
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      565 2023-02-10 02:42:40.000000 not1mm-23.4.6/not1mm/data/reddot.png
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    35558 2023-03-24 21:02:25.000000 not1mm-23.4.6/not1mm/data/settings.ui
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     4554 2023-02-26 02:19:03.000000 not1mm-23.4.6/not1mm/data/use_qrz_dialog.ui
+drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-06 17:36:34.550217 not1mm-23.4.6/not1mm/lib/
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)        0 2022-11-03 15:04:39.000000 not1mm-23.4.6/not1mm/lib/__init__.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    10342 2023-04-04 19:55:47.000000 not1mm-23.4.6/not1mm/lib/cat_interface.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1772 2023-03-17 21:26:43.000000 not1mm-23.4.6/not1mm/lib/cwinterface.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    27632 2023-04-06 16:34:21.000000 not1mm-23.4.6/not1mm/lib/database.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      357 2023-03-20 13:17:21.000000 not1mm-23.4.6/not1mm/lib/edit_contact.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      559 2023-03-06 17:59:31.000000 not1mm-23.4.6/not1mm/lib/edit_macro.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      363 2023-03-06 18:02:53.000000 not1mm-23.4.6/not1mm/lib/edit_opon.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      734 2023-03-31 15:55:44.000000 not1mm-23.4.6/not1mm/lib/edit_station.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     8760 2023-04-05 20:29:02.000000 not1mm-23.4.6/not1mm/lib/ham_utility.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    13916 2023-03-07 18:49:31.000000 not1mm-23.4.6/not1mm/lib/lookup.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1954 2023-03-17 17:01:08.000000 not1mm-23.4.6/not1mm/lib/multicast.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     4434 2023-03-17 16:20:37.000000 not1mm-23.4.6/not1mm/lib/n1mm.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      354 2023-03-28 20:21:24.000000 not1mm-23.4.6/not1mm/lib/new_contest.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      350 2023-03-06 18:07:06.000000 not1mm-23.4.6/not1mm/lib/qrz_dialog.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      363 2023-03-31 21:22:27.000000 not1mm-23.4.6/not1mm/lib/select_contest.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)       46 2023-04-06 17:13:12.000000 not1mm-23.4.6/not1mm/lib/version.py
+-rwxr-xr-x   0 mbridak   (1000) mbridak   (1000)    28034 2023-04-05 21:31:54.000000 not1mm-23.4.6/not1mm/logwindow.py
+drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-06 17:36:34.553217 not1mm-23.4.6/not1mm/plugins/
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)        0 2023-02-20 21:20:03.000000 not1mm-23.4.6/not1mm/plugins/__init__.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2456 2023-03-28 17:33:53.000000 not1mm-23.4.6/not1mm/plugins/arrl_dx_cw.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2459 2023-03-28 17:34:18.000000 not1mm-23.4.6/not1mm/plugins/arrl_dx_phone.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    12593 2023-04-05 21:08:37.000000 not1mm-23.4.6/not1mm/plugins/arrl_field_day.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2464 2023-03-28 17:34:12.000000 not1mm-23.4.6/not1mm/plugins/arrl_rtty_ru.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2465 2023-03-28 17:34:06.000000 not1mm-23.4.6/not1mm/plugins/arrl_ss_cw.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2468 2023-03-28 17:33:59.000000 not1mm-23.4.6/not1mm/plugins/arrl_ss_phone.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    14651 2023-04-02 16:44:37.000000 not1mm-23.4.6/not1mm/plugins/cq_wpx_cw.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    14659 2023-04-03 15:09:21.000000 not1mm-23.4.6/not1mm/plugins/cq_wpx_rtty.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    14655 2023-04-03 15:09:18.000000 not1mm-23.4.6/not1mm/plugins/cq_wpx_ssb.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2153 2023-03-28 17:33:25.000000 not1mm-23.4.6/not1mm/plugins/cqww_dx_cw.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2157 2023-03-28 17:33:25.000000 not1mm-23.4.6/not1mm/plugins/cqww_dx_ssb.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     7177 2023-04-04 14:52:27.000000 not1mm-23.4.6/not1mm/plugins/general_logging.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    13549 2023-04-06 16:32:50.000000 not1mm-23.4.6/not1mm/plugins/jidx_cw.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    13550 2023-04-06 16:31:42.000000 not1mm-23.4.6/not1mm/plugins/jidx_ph.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2725 2023-03-28 17:33:25.000000 not1mm-23.4.6/not1mm/plugins/winter_field_day.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     3906 2023-03-07 21:13:08.000000 not1mm-23.4.6/not1mm/test.py
+drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-06 17:36:34.553217 not1mm-23.4.6/not1mm/testing/
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2297 2023-03-29 19:50:12.000000 not1mm-23.4.6/not1mm/testing/test.py
+drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-06 17:36:34.535217 not1mm-23.4.6/not1mm.egg-info/
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)    12200 2023-04-06 17:36:34.000000 not1mm-23.4.6/not1mm.egg-info/PKG-INFO
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1801 2023-04-06 17:36:34.000000 not1mm-23.4.6/not1mm.egg-info/SOURCES.txt
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)        1 2023-04-06 17:36:34.000000 not1mm-23.4.6/not1mm.egg-info/dependency_links.txt
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)       47 2023-04-06 17:36:34.000000 not1mm-23.4.6/not1mm.egg-info/entry_points.txt
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)       42 2023-04-06 17:36:34.000000 not1mm-23.4.6/not1mm.egg-info/requires.txt
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)       33 2023-04-06 17:36:34.000000 not1mm-23.4.6/not1mm.egg-info/top_level.txt
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     1148 2023-04-06 17:13:25.000000 not1mm-23.4.6/pyproject.toml
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)       38 2023-04-06 17:36:34.554216 not1mm-23.4.6/setup.cfg
+drwxr-xr-x   0 mbridak   (1000) mbridak   (1000)        0 2023-04-06 17:36:34.553217 not1mm-23.4.6/testing/
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)     2248 2023-03-07 22:04:42.000000 not1mm-23.4.6/testing/test.py
+-rw-r--r--   0 mbridak   (1000) mbridak   (1000)      861 2023-03-29 19:39:25.000000 not1mm-23.4.6/testing/text2.py
```

### Comparing `not1mm-23.4.5/LICENSE` & `not1mm-23.4.6/LICENSE`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/PKG-INFO` & `not1mm-23.4.6/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: not1mm
-Version: 23.4.5
+Version: 23.4.6
 Summary: NOT1MM Logger
 Author-email: Michael Bridak <michael.bridak@gmail.com>
 Project-URL: Homepage, https://github.com/mbridak/not1mm
 Project-URL: Bug Tracker, https://github.com/mbridak/not1mm/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: Development Status :: 1 - Planning
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
@@ -52,36 +52,37 @@
   - [CAT](#cat)
 
 ## What and why is Not1MM
 
 Not1MM's interface is a blantent ripoff of N1MM.
 It is NOT N1MM and any problem you have with this software should in no way reflect on their software.
 
-If you use Windows(tm) you should run their, or some other, program.
+If you use Windows(tm) you should run away from this and use someother program.
 
 I personally don't. While it may be possible to get N1MM working under Wine, I haven't checked, I'd rather not have to jump thru the hoops.
 
 **Currently this exists for my own personal amusement**.
 Something to do in my free time.
 While I'm not watching TV, Right vs Left political 'News' programs, mind numbing 'Reality' TV etc...
 
 ## What it is not
 
-Working.
+Fully working.
 
-The current state is "**Not Working**". I literally just dragged some widgets out on a Qt Designer window, and wrote a couple stubs to display the interface. Next to nothing is working or useful.
+The current state is "**ALPHA**". I've used it for CQ WPX SSB, and was able to work about 40 contacts and submit a cabrillo at the end. I'll add contests as/if I work them.
 
 ## What it probably never will be
 
-Feature complete.
+Feature complete. I'm only one guy, and I'm not what you'd consider to be a contester. So new contests will be sparse.
 
 ![main screen](https://github.com/mbridak/not1mm/raw/master/pic/main.png)
 
 ## Changes of note
 
+- [23-4-6] Added JIDX contest. Added {SNT} and {SENTNR} CW macros.
 - [23-4-5] Fixed crash caused by lists not being lists. Filled out some existing code stubs in the Field Day plugin. Fixed log window not showing current contest Q's.  
 - [23-4-4] Current OP defaults to Station call if OPON not used. Text formatting of Station settings. Removed STX and SRX strings from General Logging ADIF. DB now operates on current contest Nr. Hide/Show band-mode frames.
 - [23-4-3] Added dialog to select from defined contests in the active database. Force Station settings then new contest dialog on new DB creation. Add Greneral Logging contest type. Added other Cabrillo tags.
 
 <details>
 
 <summary>March 2023</summary>
@@ -195,14 +196,21 @@
 The your choices will be remembered when you relaunch the program.
 
 ## Editing function key macros
 
 You can edit the CW macros by right clicking on the buttons and filling out the dialog.
 ![Edit Macro](https://github.com/mbridak/not1mm/raw/master/pic/edit_macro.png)
 
+You can include a limited set of substitution instructions.
+
+- {MYCALL} Sends the station call.
+- {HISCALL} Send what's in the callsign field.
+- {SNT} Sends 5nn
+- {SENTNR} Sends whats in the SentNR field. 
+
 ## cty.dat and QRZ lookups for distance and bearing
 
 When a callsign is entered, a look up is first done in a cty.dat file to determin the country of origin, geographic center, cq zone and ITU region. Great circle calculations are done to determin the heading and distance from your gridsquare to the grographic center. This information then displayed at the bottom left.
 
 ![snapshot of heading and distance](https://github.com/mbridak/not1mm/raw/master/pic/heading_distance.png)
 
 After this, a request is made to QRZ for the gridsquare of the callsign. If there is a response the information is recalculated and displayed. You'll know is this has happened, since the gridsquare will replace the word "Regional".
```

### Comparing `not1mm-23.4.5/README.md` & `not1mm-23.4.6/README.md`

 * *Files 4% similar despite different names*

```diff
@@ -33,36 +33,37 @@
   - [CAT](#cat)
 
 ## What and why is Not1MM
 
 Not1MM's interface is a blantent ripoff of N1MM.
 It is NOT N1MM and any problem you have with this software should in no way reflect on their software.
 
-If you use Windows(tm) you should run their, or some other, program.
+If you use Windows(tm) you should run away from this and use someother program.
 
 I personally don't. While it may be possible to get N1MM working under Wine, I haven't checked, I'd rather not have to jump thru the hoops.
 
 **Currently this exists for my own personal amusement**.
 Something to do in my free time.
 While I'm not watching TV, Right vs Left political 'News' programs, mind numbing 'Reality' TV etc...
 
 ## What it is not
 
-Working.
+Fully working.
 
-The current state is "**Not Working**". I literally just dragged some widgets out on a Qt Designer window, and wrote a couple stubs to display the interface. Next to nothing is working or useful.
+The current state is "**ALPHA**". I've used it for CQ WPX SSB, and was able to work about 40 contacts and submit a cabrillo at the end. I'll add contests as/if I work them.
 
 ## What it probably never will be
 
-Feature complete.
+Feature complete. I'm only one guy, and I'm not what you'd consider to be a contester. So new contests will be sparse.
 
 ![main screen](https://github.com/mbridak/not1mm/raw/master/pic/main.png)
 
 ## Changes of note
 
+- [23-4-6] Added JIDX contest. Added {SNT} and {SENTNR} CW macros.
 - [23-4-5] Fixed crash caused by lists not being lists. Filled out some existing code stubs in the Field Day plugin. Fixed log window not showing current contest Q's.  
 - [23-4-4] Current OP defaults to Station call if OPON not used. Text formatting of Station settings. Removed STX and SRX strings from General Logging ADIF. DB now operates on current contest Nr. Hide/Show band-mode frames.
 - [23-4-3] Added dialog to select from defined contests in the active database. Force Station settings then new contest dialog on new DB creation. Add Greneral Logging contest type. Added other Cabrillo tags.
 
 <details>
 
 <summary>March 2023</summary>
@@ -176,14 +177,21 @@
 The your choices will be remembered when you relaunch the program.
 
 ## Editing function key macros
 
 You can edit the CW macros by right clicking on the buttons and filling out the dialog.
 ![Edit Macro](https://github.com/mbridak/not1mm/raw/master/pic/edit_macro.png)
 
+You can include a limited set of substitution instructions.
+
+- {MYCALL} Sends the station call.
+- {HISCALL} Send what's in the callsign field.
+- {SNT} Sends 5nn
+- {SENTNR} Sends whats in the SentNR field. 
+
 ## cty.dat and QRZ lookups for distance and bearing
 
 When a callsign is entered, a look up is first done in a cty.dat file to determin the country of origin, geographic center, cq zone and ITU region. Great circle calculations are done to determin the heading and distance from your gridsquare to the grographic center. This information then displayed at the bottom left.
 
 ![snapshot of heading and distance](https://github.com/mbridak/not1mm/raw/master/pic/heading_distance.png)
 
 After this, a request is made to QRZ for the gridsquare of the callsign. If there is a response the information is recalculated and displayed. You'll know is this has happened, since the gridsquare will replace the word "Regional".
```

### Comparing `not1mm-23.4.5/not1mm/__main__.py` & `not1mm-23.4.6/not1mm/__main__.py`

 * *Files 1% similar despite different names*

```diff
@@ -997,14 +997,16 @@
         self.edit_macro(self.F12)
 
     def process_macro(self, macro: str) -> str:
         """Process CW macro substitutions"""
         macro = macro.upper()
         macro = macro.replace("{MYCALL}", self.station.get("Call"))
         macro = macro.replace("{HISCALL}", self.callsign.text())
+        macro = macro.replace("{SNT}", self.sent.text().replace("9", "n"))  # FIXME
+        macro = macro.replace("{SENTNR}", self.other_1.text())
         return macro
 
     def sendf1(self):
         """stub"""
         logger.debug("F1 Clicked")
         if self.cw:
             # if self.preference.get("send_n1mm_packets"):
```

### Comparing `not1mm-23.4.5/not1mm/data/Combinear.qss` & `not1mm-23.4.6/not1mm/data/Combinear.qss`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/JetBrainsMono-Regular.ttf` & `not1mm-23.4.6/not1mm/data/JetBrainsMono-Regular.ttf`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/MASTER.SCP` & `not1mm-23.4.6/not1mm/data/MASTER.SCP`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/contests.sql` & `not1mm-23.4.6/not1mm/data/contests.sql`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/cty.json` & `not1mm-23.4.6/not1mm/data/cty.json`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/editcontact.ui` & `not1mm-23.4.6/not1mm/data/editcontact.ui`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/editmacro.ui` & `not1mm-23.4.6/not1mm/data/editmacro.ui`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/k6gte.not1mm-128.png` & `not1mm-23.4.6/not1mm/data/k6gte.not1mm-128.png`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/k6gte.not1mm-32.png` & `not1mm-23.4.6/not1mm/data/k6gte.not1mm-32.png`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/k6gte.not1mm-64.png` & `not1mm-23.4.6/not1mm/data/k6gte.not1mm-64.png`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/logwindow.ui` & `not1mm-23.4.6/not1mm/data/logwindow.ui`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/main.ui` & `not1mm-23.4.6/not1mm/data/main.ui`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/new_contest.ui` & `not1mm-23.4.6/not1mm/data/new_contest.ui`

 * *Files 1% similar despite different names*

#### Comparing `not1mm-23.4.5/not1mm/data/new_contest.ui` & `not1mm-23.4.6/not1mm/data/new_contest.ui`

```diff
@@ -175,24 +175,34 @@
           <item>
             <property name="text">
               <string>CQ WPX SSB</string>
             </property>
           </item>
           <item>
             <property name="text">
+              <string>JIDX CW</string>
+            </property>
+          </item>
+          <item>
+            <property name="text">
+              <string>JIDX PH</string>
+            </property>
+          </item>
+          <item>
+            <property name="text">
               <string>Winter Field Day</string>
             </property>
           </item>
         </widget>
       </item>
       <item row="2" column="2">
         <widget class="QDateTimeEdit" name="dateTimeEdit">
           <property name="time">
             <time>
-              <hour>16</hour>
+              <hour>0</hour>
               <minute>0</minute>
               <second>0</second>
             </time>
           </property>
           <property name="maximumDateTime">
             <datetime>
               <hour>7</hour>
```

### Comparing `not1mm-23.4.5/not1mm/data/opon.ui` & `not1mm-23.4.6/not1mm/data/opon.ui`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/pickcontest.ui` & `not1mm-23.4.6/not1mm/data/pickcontest.ui`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/reddot.png` & `not1mm-23.4.6/not1mm/data/reddot.png`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/settings.ui` & `not1mm-23.4.6/not1mm/data/settings.ui`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/data/use_qrz_dialog.ui` & `not1mm-23.4.6/not1mm/data/use_qrz_dialog.ui`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/lib/cat_interface.py` & `not1mm-23.4.6/not1mm/lib/cat_interface.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/lib/cwinterface.py` & `not1mm-23.4.6/not1mm/lib/cwinterface.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/lib/database.py` & `not1mm-23.4.6/not1mm/lib/database.py`

 * *Files 2% similar despite different names*

```diff
@@ -323,22 +323,22 @@
                 cursor = conn.cursor()
                 cursor.execute("select count(*) + 1 as count from ContestInstance;")
                 return cursor.fetchone()
         except sqlite3.OperationalError as exception:
             logger.debug("%s", exception)
             return {}
 
-    def fetch_contest_by_id(self, ContestNR: str) -> dict:
+    def fetch_contest_by_id(self, contest_nr: str) -> dict:
         """returns a dict of ContestInstance"""
         try:
             with sqlite3.connect(self.database) as conn:
                 conn.row_factory = self.row_factory
                 cursor = conn.cursor()
                 cursor.execute(
-                    f"select * from ContestInstance where ContestNR='{ContestNR}';"
+                    f"select * from ContestInstance where ContestNR='{contest_nr}';"
                 )
                 return cursor.fetchone()
         except sqlite3.OperationalError as exception:
             logger.debug("%s", exception)
             return {}
 
     def add_contest(self, contest: dict) -> None:
@@ -481,22 +481,70 @@
                 cursor = conn.cursor()
                 cursor.execute(f"select * from dxlog where ID='{uuid}';")
                 return cursor.fetchone()
         except sqlite3.OperationalError as exception:
             logger.debug("%s", exception)
             return {}
 
+    def fetch_nr_count(self) -> dict:
+        """
+        returns dict with count of unique NR.
+        {nr_count: count}
+        """
+        try:
+            with sqlite3.connect(self.database) as conn:
+                conn.row_factory = self.row_factory
+                cursor = conn.cursor()
+                cursor.execute(
+                    f"select count(DISTINCT NR) as nr_count from dxlog where ContestNR = {self.current_contest};"
+                )
+                return cursor.fetchone()
+        except sqlite3.OperationalError as exception:
+            logger.debug("%s", exception)
+            return {}
+
+    def fetch_nr_exists(self, number) -> dict:
+        """returns a dict key of nr_count"""
+        try:
+            with sqlite3.connect(self.database) as conn:
+                conn.row_factory = self.row_factory
+                cursor = conn.cursor()
+                cursor.execute(
+                    f"select count(*) as nr_count from dxlog where NR = '{number}' and ContestNR = {self.current_contest};"
+                )
+                return cursor.fetchone()
+        except sqlite3.OperationalError as exception:
+            logger.debug("%s", exception)
+            return {}
+
+    def fetch_nr_exists_before_me(self, number, time_stamp) -> dict:
+        """returns a dict key of nr_count"""
+        try:
+            with sqlite3.connect(self.database) as conn:
+                conn.row_factory = self.row_factory
+                cursor = conn.cursor()
+                cursor.execute(
+                    f"select count(*) as nr_count from dxlog where  TS < '{time_stamp}' and NR = '{number}' and ContestNR = {self.current_contest};"
+                )
+                return cursor.fetchone()
+        except sqlite3.OperationalError as exception:
+            logger.debug("%s", exception)
+            return {}
+
     def fetch_wpx_count(self) -> dict:
-        """returns a list of dicts with last contact in the database."""
+        """
+        returns dict with count of unique WPXPrefix.
+        {wpx_count: count}
+        """
         try:
             with sqlite3.connect(self.database) as conn:
                 conn.row_factory = self.row_factory
                 cursor = conn.cursor()
                 cursor.execute(
-                    f"select count(DISTINCT WPXPrefix) as wpx_count from dxlog and ContestNR = {self.current_contest};"
+                    f"select count(DISTINCT WPXPrefix) as wpx_count from dxlog where ContestNR = {self.current_contest};"
                 )
                 return cursor.fetchone()
         except sqlite3.OperationalError as exception:
             logger.debug("%s", exception)
             return {}
 
     def fetch_wpx_exists(self, wpx) -> dict:
```

### Comparing `not1mm-23.4.5/not1mm/lib/edit_macro.py` & `not1mm-23.4.6/not1mm/lib/edit_macro.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/lib/edit_station.py` & `not1mm-23.4.6/not1mm/lib/edit_station.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/lib/ham_utility.py` & `not1mm-23.4.6/not1mm/lib/ham_utility.py`

 * *Files 1% similar despite different names*

```diff
@@ -100,25 +100,24 @@
             return "6"
         if 148000000 > frequency > 144000000:
             return "2"
         if 225000000 > frequency > 222000000:
             return "222"
         if 450000000 > frequency > 420000000:
             return "432"
-    else:
-        return "0"
+    return "0"
 
 
 def get_logged_band(freq: str) -> str:
     """
     Convert a (string) frequency into a (string) band.
     Returns a (string) band.
     Returns a "0" if frequency is out of band.
     """
-    # logger.info("getband: %s %s", type(freq), freq)
+
     if freq.isnumeric():
         frequency = int(float(freq))
         if 2000000 > frequency > 1800000:
             return "1.8"
         if 4000000 > frequency > 3500000:
             return "3.5"
         if 5406000 > frequency > 5330000:
@@ -141,16 +140,15 @@
             return "50"
         if 148000000 > frequency > 144000000:
             return "144"
         if 225000000 > frequency > 222000000:
             return "222"
         if 450000000 > frequency > 420000000:
             return "430"
-    else:
-        return "0"
+    return "0"
 
 
 def fakefreq(band, mode):
     """
     If unable to obtain a frequency from the rig,
     This will return a sane value for a frequency mainly for the cabrillo and adif log.
     Takes a band and mode as input and returns freq in khz.
```

### Comparing `not1mm-23.4.5/not1mm/lib/lookup.py` & `not1mm-23.4.6/not1mm/lib/lookup.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/lib/multicast.py` & `not1mm-23.4.6/not1mm/lib/multicast.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/lib/n1mm.py` & `not1mm-23.4.6/not1mm/lib/n1mm.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/logwindow.py` & `not1mm-23.4.6/not1mm/logwindow.py`

 * *Files 2% similar despite different names*

```diff
@@ -72,16 +72,16 @@
         self.database.current_contest = self.pref.get("contest", 0)
         self.contact = self.database.empty_contact
         data_path = WORKING_PATH + "/data/logwindow.ui"
         uic.loadUi(data_path, self)
         self.setWindowTitle(
             f"Log Display - {self.pref.get('current_database', 'ham.db')}"
         )
-        self.generalLog.setColumnCount(14)
-        self.focusedLog.setColumnCount(14)
+        self.generalLog.setColumnCount(16)
+        self.focusedLog.setColumnCount(16)
         icon_path = WORKING_PATH + "/data/"
         self.checkmark = QtGui.QPixmap(icon_path + "check.png")
         self.checkicon = QtGui.QIcon()
         self.checkicon.addPixmap(self.checkmark)
         self.generalLog.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
         self.generalLog.customContextMenuRequested.connect(self.edit_contact_selected)
         self.generalLog.setHorizontalHeaderItem(
@@ -90,36 +90,43 @@
         self.generalLog.verticalHeader().setVisible(False)
         self.generalLog.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Call"))
         self.generalLog.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Freq"))
         self.generalLog.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Snt"))
         self.generalLog.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("Rcv"))
         self.generalLog.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("SentNr"))
         self.generalLog.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem("RcvNr"))
-        self.generalLog.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem("WPX"))
-        self.generalLog.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem("M1"))
-        self.generalLog.setHorizontalHeaderItem(9, QtWidgets.QTableWidgetItem("ZN"))
-        self.generalLog.setHorizontalHeaderItem(10, QtWidgets.QTableWidgetItem("M2"))
-        self.generalLog.setHorizontalHeaderItem(11, QtWidgets.QTableWidgetItem("PFX"))
-        self.generalLog.setHorizontalHeaderItem(12, QtWidgets.QTableWidgetItem("PTS"))
-        self.generalLog.setHorizontalHeaderItem(13, QtWidgets.QTableWidgetItem("UUID"))
+
+        self.generalLog.setHorizontalHeaderItem(
+            7, QtWidgets.QTableWidgetItem("Exchange1")
+        )
+        self.generalLog.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem("Sect"))
+
+        self.generalLog.setHorizontalHeaderItem(9, QtWidgets.QTableWidgetItem("WPX"))
+        self.generalLog.setHorizontalHeaderItem(10, QtWidgets.QTableWidgetItem("M1"))
+        self.generalLog.setHorizontalHeaderItem(11, QtWidgets.QTableWidgetItem("ZN"))
+        self.generalLog.setHorizontalHeaderItem(12, QtWidgets.QTableWidgetItem("M2"))
+        self.generalLog.setHorizontalHeaderItem(13, QtWidgets.QTableWidgetItem("PFX"))
+        self.generalLog.setHorizontalHeaderItem(14, QtWidgets.QTableWidgetItem("PTS"))
+        self.generalLog.setHorizontalHeaderItem(15, QtWidgets.QTableWidgetItem("UUID"))
         self.generalLog.setColumnWidth(0, 200)
         self.generalLog.setColumnWidth(3, 50)
         self.generalLog.setColumnWidth(4, 50)
         self.generalLog.setColumnWidth(5, 75)
         self.generalLog.setColumnWidth(6, 75)
-        self.generalLog.setColumnWidth(7, 50)
-        self.generalLog.setColumnWidth(8, 50)
+
         self.generalLog.setColumnWidth(9, 50)
-        self.generalLog.setColumnWidth(12, 50)
+        self.generalLog.setColumnWidth(10, 50)
+        self.generalLog.setColumnWidth(11, 50)
+        self.generalLog.setColumnWidth(14, 50)
         self.generalLog.cellDoubleClicked.connect(self.double_clicked)
         self.generalLog.cellChanged.connect(self.cell_changed)
-        self.generalLog.setColumnHidden(9, True)
-        self.generalLog.setColumnHidden(10, True)
-        self.generalLog.setColumnHidden(11, True)
-        self.generalLog.setColumnHidden(13, True)
+        # self.generalLog.setColumnHidden(11, True)
+        # self.generalLog.setColumnHidden(12, True)
+        # self.generalLog.setColumnHidden(13, True)
+        self.generalLog.setColumnHidden(15, True)
 
         self.focusedLog.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
         self.focusedLog.customContextMenuRequested.connect(
             self.edit_focused_contact_selected
         )
         self.focusedLog.setHorizontalHeaderItem(
             0, QtWidgets.QTableWidgetItem("YYYY-MM-DD HH:MM:SS")
@@ -127,36 +134,43 @@
         self.focusedLog.verticalHeader().setVisible(False)
         self.focusedLog.setHorizontalHeaderItem(1, QtWidgets.QTableWidgetItem("Call"))
         self.focusedLog.setHorizontalHeaderItem(2, QtWidgets.QTableWidgetItem("Freq"))
         self.focusedLog.setHorizontalHeaderItem(3, QtWidgets.QTableWidgetItem("Snt"))
         self.focusedLog.setHorizontalHeaderItem(4, QtWidgets.QTableWidgetItem("Rcv"))
         self.focusedLog.setHorizontalHeaderItem(5, QtWidgets.QTableWidgetItem("SentNr"))
         self.focusedLog.setHorizontalHeaderItem(6, QtWidgets.QTableWidgetItem("RcvNr"))
-        self.focusedLog.setHorizontalHeaderItem(7, QtWidgets.QTableWidgetItem("WPX"))
-        self.focusedLog.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem("M1"))
-        self.focusedLog.setHorizontalHeaderItem(9, QtWidgets.QTableWidgetItem("ZN"))
-        self.focusedLog.setHorizontalHeaderItem(10, QtWidgets.QTableWidgetItem("M2"))
-        self.focusedLog.setHorizontalHeaderItem(11, QtWidgets.QTableWidgetItem("PFX"))
-        self.focusedLog.setHorizontalHeaderItem(12, QtWidgets.QTableWidgetItem("PTS"))
-        self.focusedLog.setHorizontalHeaderItem(13, QtWidgets.QTableWidgetItem("UUID"))
+
+        self.generalLog.setHorizontalHeaderItem(
+            7, QtWidgets.QTableWidgetItem("Exchange1")
+        )
+        self.generalLog.setHorizontalHeaderItem(8, QtWidgets.QTableWidgetItem("Sect"))
+
+        self.focusedLog.setHorizontalHeaderItem(9, QtWidgets.QTableWidgetItem("WPX"))
+        self.focusedLog.setHorizontalHeaderItem(10, QtWidgets.QTableWidgetItem("M1"))
+        self.focusedLog.setHorizontalHeaderItem(11, QtWidgets.QTableWidgetItem("ZN"))
+        self.focusedLog.setHorizontalHeaderItem(12, QtWidgets.QTableWidgetItem("M2"))
+        self.focusedLog.setHorizontalHeaderItem(13, QtWidgets.QTableWidgetItem("PFX"))
+        self.focusedLog.setHorizontalHeaderItem(14, QtWidgets.QTableWidgetItem("PTS"))
+        self.focusedLog.setHorizontalHeaderItem(15, QtWidgets.QTableWidgetItem("UUID"))
         self.focusedLog.setColumnWidth(0, 200)
         self.focusedLog.setColumnWidth(3, 50)
         self.focusedLog.setColumnWidth(4, 50)
         self.focusedLog.setColumnWidth(5, 75)
         self.focusedLog.setColumnWidth(6, 75)
-        self.focusedLog.setColumnWidth(7, 50)
-        self.focusedLog.setColumnWidth(8, 50)
+
         self.focusedLog.setColumnWidth(9, 50)
-        self.focusedLog.setColumnWidth(12, 50)
+        self.focusedLog.setColumnWidth(10, 50)
+        self.focusedLog.setColumnWidth(11, 50)
+        self.focusedLog.setColumnWidth(14, 50)
         # self.focusedLog.cellDoubleClicked.connect(self.double_clicked)
         # self.focusedLog.cellChanged.connect(self.cell_changed)
-        self.focusedLog.setColumnHidden(9, True)
-        self.focusedLog.setColumnHidden(10, True)
-        self.focusedLog.setColumnHidden(11, True)
-        self.focusedLog.setColumnHidden(13, True)
+        # self.focusedLog.setColumnHidden(11, True)
+        # self.focusedLog.setColumnHidden(12, True)
+        # self.focusedLog.setColumnHidden(13, True)
+        self.focusedLog.setColumnHidden(15, True)
         self.get_log()
         self.multicast_interface = Multicast(
             MULTICAST_GROUP, MULTICAST_PORT, INTERFACE_IP
         )
 
         if self._udpwatch is None:
             self._udpwatch = threading.Thread(
@@ -212,41 +226,43 @@
             "TS": self.generalLog.item(row, 0).text(),
             "Call": self.generalLog.item(row, 1).text().upper(),
             "Freq": self.generalLog.item(row, 2).text(),
             "SNT": self.generalLog.item(row, 3).text(),
             "RCV": self.generalLog.item(row, 4).text(),
             "SentNr": self.generalLog.item(row, 5).text(),
             "NR": self.generalLog.item(row, 6).text(),
-            "WPXPrefix": self.generalLog.item(row, 7).text(),
-            "IsMultiplier1": self.generalLog.item(row, 8).text(),
-            "ZN": self.generalLog.item(row, 9).text(),
-            "IsMultiplier2": self.generalLog.item(row, 10).text().upper(),
-            "CountryPrefix": self.generalLog.item(row, 11).text(),
-            "Points": self.generalLog.item(row, 12).text(),
-            "ID": self.generalLog.item(row, 13).text(),
+            "Exchange1": self.generalLog.item(row, 7).text(),
+            "Sect": self.generalLog.item(row, 8).text(),
+            "WPXPrefix": self.generalLog.item(row, 9).text(),
+            "IsMultiplier1": self.generalLog.item(row, 10).text(),
+            "ZN": self.generalLog.item(row, 11).text(),
+            "IsMultiplier2": self.generalLog.item(row, 12).text().upper(),
+            "CountryPrefix": self.generalLog.item(row, 13).text(),
+            "Points": self.generalLog.item(row, 14).text(),
+            "ID": self.generalLog.item(row, 15).text(),
         }
         self.database.change_contact(db_record)
         self.get_log()
         self.generalLog.scrollToItem(self.generalLog.item(row, column))
 
     def dummy(self):
         """the dummy"""
 
     def edit_focused_contact_selected(self, clicked_cell):
         """Show edit contact dialog"""
         logger.debug("Opening EditContact dialog")
         item = self.focusedLog.itemAt(clicked_cell)
-        uuid = self.focusedLog.item(item.row(), 13).text()
+        uuid = self.focusedLog.item(item.row(), 15).text()
         self.edit_contact(uuid)
 
     def edit_contact_selected(self, clicked_cell):
         """Show edit contact dialog"""
         logger.debug("Opening EditContact dialog")
         item = self.generalLog.itemAt(clicked_cell)
-        uuid = self.generalLog.item(item.row(), 13).text()
+        uuid = self.generalLog.item(item.row(), 15).text()
         self.edit_contact(uuid)
 
     def edit_contact(self, uuid):
         """Show edit contact dialog"""
         logger.debug("Edit: %s", uuid)
         self.edit_contact_dialog = EditContact(WORKING_PATH)
         self.edit_contact_dialog.accepted.connect(self.save_edited_contact)
@@ -352,14 +368,32 @@
         self.database.delete_contact(self.contact.get("ID", ""))
         self.edit_contact_dialog.close()
         self.get_log()
         self.show_like_calls(self.contact.get("Call", ""))
 
     def get_log(self):
         """Get Log, Show it."""
+
+        """
+            The horizontal flags are:
+
+            Constant	Value	Description
+            Qt::AlignLeft	0x0001	Aligns with the left edge.
+            Qt::AlignRight	0x0002	Aligns with the right edge.
+            Qt::AlignHCenter	0x0004	Centers horizontally in the available space.
+            Qt::AlignJustify	0x0008	Justifies the text in the available space.
+            
+            The vertical flags are:
+
+            Constant	Value	Description
+            Qt::AlignTop	0x0020	Aligns with the top.
+            Qt::AlignBottom	0x0040	Aligns with the bottom.
+            Qt::AlignVCenter	0x0080	Centers vertically in the available space.
+            Qt::AlignBaseline	0x0100	Aligns with the baseline.
+        """
         self.generalLog.cellChanged.connect(self.dummy)
         self.table_loading = True
         current_log = self.database.fetch_all_contacts_asc()
         self.generalLog.setRowCount(0)
         for log_item in current_log:
             number_of_rows = self.generalLog.rowCount()
             self.generalLog.insertRow(number_of_rows)
@@ -399,50 +433,60 @@
                 number_of_rows,
                 6,
                 QtWidgets.QTableWidgetItem(str(log_item.get("NR", ""))),
             )
             self.generalLog.setItem(
                 number_of_rows,
                 7,
+                QtWidgets.QTableWidgetItem(str(log_item.get("Exchange1", ""))),
+            )
+            self.generalLog.setItem(
+                number_of_rows,
+                8,
+                QtWidgets.QTableWidgetItem(str(log_item.get("Sect", ""))),
+            )
+            self.generalLog.setItem(
+                number_of_rows,
+                9,
                 QtWidgets.QTableWidgetItem(str(log_item.get("WPXPrefix", ""))),
             )
             item = QtWidgets.QTableWidgetItem()
             if log_item.get("IsMultiplier1", False):
                 item.setIcon(self.checkicon)
             self.generalLog.setItem(
                 number_of_rows,
-                8,
+                10,
                 item,
             )
             self.generalLog.setItem(
                 number_of_rows,
-                9,
+                11,
                 QtWidgets.QTableWidgetItem(str(log_item.get("ZN", ""))),
             )
             item = QtWidgets.QTableWidgetItem()
             if log_item.get("IsMultiplier2", False):
                 item.setIcon(self.checkicon)
             self.generalLog.setItem(
                 number_of_rows,
-                10,
+                12,
                 item,
             )
             self.generalLog.setItem(
                 number_of_rows,
-                11,
+                13,
                 QtWidgets.QTableWidgetItem(str(log_item.get("CountryPrefix", ""))),
             )
             self.generalLog.setItem(
                 number_of_rows,
-                12,
+                14,
                 QtWidgets.QTableWidgetItem(str(log_item.get("Points", ""))),
             )
             self.generalLog.setItem(
                 number_of_rows,
-                13,
+                15,
                 QtWidgets.QTableWidgetItem(str(log_item.get("ID", ""))),
             )
         self.table_loading = False
         self.generalLog.cellChanged.connect(self.cell_changed)
 
     # def testing(self, a):
     #     """ignore"""
```

### Comparing `not1mm-23.4.5/not1mm/plugins/arrl_dx_cw.py` & `not1mm-23.4.6/not1mm/plugins/arrl_dx_cw.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/arrl_dx_phone.py` & `not1mm-23.4.6/not1mm/plugins/arrl_dx_phone.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/arrl_field_day.py` & `not1mm-23.4.6/not1mm/plugins/arrl_field_day.py`

 * *Files 2% similar despite different names*

```diff
@@ -38,16 +38,16 @@
     label = self.field4.findChild(QtWidgets.QLabel)
     label.setText("Section")
 
 
 def set_tab_next(self):
     """Set TAB Advances"""
     self.tab_next = {
-        self.callsign: self.field1.findChild(QtWidgets.QLineEdit),
-        self.field1.findChild(QtWidgets.QLineEdit): self.field2.findChild(
+        self.callsign: self.field3.findChild(QtWidgets.QLineEdit),
+        self.field1.findChild(QtWidgets.QLineEdit): self.field3.findChild(
             QtWidgets.QLineEdit
         ),
         self.field2.findChild(QtWidgets.QLineEdit): self.field3.findChild(
             QtWidgets.QLineEdit
         ),
         self.field3.findChild(QtWidgets.QLineEdit): self.field4.findChild(
             QtWidgets.QLineEdit
@@ -57,32 +57,28 @@
 
 
 def set_tab_prev(self):
     """Set TAB Advances"""
     self.tab_prev = {
         self.callsign: self.field4.findChild(QtWidgets.QLineEdit),
         self.field1.findChild(QtWidgets.QLineEdit): self.callsign,
-        self.field2.findChild(QtWidgets.QLineEdit): self.field1.findChild(
-            QtWidgets.QLineEdit
-        ),
-        self.field3.findChild(QtWidgets.QLineEdit): self.field2.findChild(
-            QtWidgets.QLineEdit
-        ),
+        self.field2.findChild(QtWidgets.QLineEdit): self.callsign,
+        self.field3.findChild(QtWidgets.QLineEdit): self.callsign,
         self.field4.findChild(QtWidgets.QLineEdit): self.field3.findChild(
             QtWidgets.QLineEdit
         ),
     }
 
 
 def set_contact_vars(self):
     """Contest Specific"""
     self.contact["SNT"] = self.sent.text()
     self.contact["RCV"] = self.receive.text()
-    self.contact["Exchange1"] = self.other_1.text()
-    self.contact["Sect"] = self.other_2.text()
+    self.contact["Exchange1"] = self.other_1.text().upper()
+    self.contact["Sect"] = self.other_2.text().upper()
 
 
 def prefill(self):
     """Fill SentNR"""
 
 
 def points(self):
```

### Comparing `not1mm-23.4.5/not1mm/plugins/arrl_rtty_ru.py` & `not1mm-23.4.6/not1mm/plugins/arrl_rtty_ru.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/arrl_ss_cw.py` & `not1mm-23.4.6/not1mm/plugins/arrl_ss_cw.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/arrl_ss_phone.py` & `not1mm-23.4.6/not1mm/plugins/arrl_ss_phone.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/cq_wpx_cw.py` & `not1mm-23.4.6/not1mm/plugins/cq_wpx_cw.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/cq_wpx_rtty.py` & `not1mm-23.4.6/not1mm/plugins/cq_wpx_rtty.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/cq_wpx_ssb.py` & `not1mm-23.4.6/not1mm/plugins/cq_wpx_ssb.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/cqww_dx_cw.py` & `not1mm-23.4.6/not1mm/plugins/cqww_dx_cw.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/cqww_dx_ssb.py` & `not1mm-23.4.6/not1mm/plugins/cqww_dx_ssb.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/general_logging.py` & `not1mm-23.4.6/not1mm/plugins/general_logging.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/plugins/winter_field_day.py` & `not1mm-23.4.6/not1mm/plugins/winter_field_day.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/test.py` & `not1mm-23.4.6/not1mm/test.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm/testing/test.py` & `not1mm-23.4.6/not1mm/testing/test.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/not1mm.egg-info/PKG-INFO` & `not1mm-23.4.6/not1mm.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: not1mm
-Version: 23.4.5
+Version: 23.4.6
 Summary: NOT1MM Logger
 Author-email: Michael Bridak <michael.bridak@gmail.com>
 Project-URL: Homepage, https://github.com/mbridak/not1mm
 Project-URL: Bug Tracker, https://github.com/mbridak/not1mm/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: Development Status :: 1 - Planning
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
@@ -52,36 +52,37 @@
   - [CAT](#cat)
 
 ## What and why is Not1MM
 
 Not1MM's interface is a blantent ripoff of N1MM.
 It is NOT N1MM and any problem you have with this software should in no way reflect on their software.
 
-If you use Windows(tm) you should run their, or some other, program.
+If you use Windows(tm) you should run away from this and use someother program.
 
 I personally don't. While it may be possible to get N1MM working under Wine, I haven't checked, I'd rather not have to jump thru the hoops.
 
 **Currently this exists for my own personal amusement**.
 Something to do in my free time.
 While I'm not watching TV, Right vs Left political 'News' programs, mind numbing 'Reality' TV etc...
 
 ## What it is not
 
-Working.
+Fully working.
 
-The current state is "**Not Working**". I literally just dragged some widgets out on a Qt Designer window, and wrote a couple stubs to display the interface. Next to nothing is working or useful.
+The current state is "**ALPHA**". I've used it for CQ WPX SSB, and was able to work about 40 contacts and submit a cabrillo at the end. I'll add contests as/if I work them.
 
 ## What it probably never will be
 
-Feature complete.
+Feature complete. I'm only one guy, and I'm not what you'd consider to be a contester. So new contests will be sparse.
 
 ![main screen](https://github.com/mbridak/not1mm/raw/master/pic/main.png)
 
 ## Changes of note
 
+- [23-4-6] Added JIDX contest. Added {SNT} and {SENTNR} CW macros.
 - [23-4-5] Fixed crash caused by lists not being lists. Filled out some existing code stubs in the Field Day plugin. Fixed log window not showing current contest Q's.  
 - [23-4-4] Current OP defaults to Station call if OPON not used. Text formatting of Station settings. Removed STX and SRX strings from General Logging ADIF. DB now operates on current contest Nr. Hide/Show band-mode frames.
 - [23-4-3] Added dialog to select from defined contests in the active database. Force Station settings then new contest dialog on new DB creation. Add Greneral Logging contest type. Added other Cabrillo tags.
 
 <details>
 
 <summary>March 2023</summary>
@@ -195,14 +196,21 @@
 The your choices will be remembered when you relaunch the program.
 
 ## Editing function key macros
 
 You can edit the CW macros by right clicking on the buttons and filling out the dialog.
 ![Edit Macro](https://github.com/mbridak/not1mm/raw/master/pic/edit_macro.png)
 
+You can include a limited set of substitution instructions.
+
+- {MYCALL} Sends the station call.
+- {HISCALL} Send what's in the callsign field.
+- {SNT} Sends 5nn
+- {SENTNR} Sends whats in the SentNR field. 
+
 ## cty.dat and QRZ lookups for distance and bearing
 
 When a callsign is entered, a look up is first done in a cty.dat file to determin the country of origin, geographic center, cq zone and ITU region. Great circle calculations are done to determin the heading and distance from your gridsquare to the grographic center. This information then displayed at the bottom left.
 
 ![snapshot of heading and distance](https://github.com/mbridak/not1mm/raw/master/pic/heading_distance.png)
 
 After this, a request is made to QRZ for the gridsquare of the callsign. If there is a response the information is recalculated and displayed. You'll know is this has happened, since the gridsquare will replace the word "Regional".
```

### Comparing `not1mm-23.4.5/not1mm.egg-info/SOURCES.txt` & `not1mm-23.4.6/not1mm.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -58,11 +58,13 @@
 not1mm/plugins/arrl_ss_phone.py
 not1mm/plugins/cq_wpx_cw.py
 not1mm/plugins/cq_wpx_rtty.py
 not1mm/plugins/cq_wpx_ssb.py
 not1mm/plugins/cqww_dx_cw.py
 not1mm/plugins/cqww_dx_ssb.py
 not1mm/plugins/general_logging.py
+not1mm/plugins/jidx_cw.py
+not1mm/plugins/jidx_ph.py
 not1mm/plugins/winter_field_day.py
 not1mm/testing/test.py
 testing/test.py
 testing/text2.py
```

### Comparing `not1mm-23.4.5/pyproject.toml` & `not1mm-23.4.6/pyproject.toml`

 * *Files 9% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "not1mm" 
-version = "23.4.5"
+version = "23.4.6"
 description = "NOT1MM Logger"
 readme = "README.md"
 requires-python = ">=3.9"
 authors = [
   { name="Michael Bridak", email="michael.bridak@gmail.com" },
 ]
 dependencies = [
```

### Comparing `not1mm-23.4.5/testing/test.py` & `not1mm-23.4.6/testing/test.py`

 * *Files identical despite different names*

### Comparing `not1mm-23.4.5/testing/text2.py` & `not1mm-23.4.6/testing/text2.py`

 * *Files identical despite different names*

