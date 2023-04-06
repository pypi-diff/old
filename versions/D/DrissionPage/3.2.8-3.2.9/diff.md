# Comparing `tmp/DrissionPage-3.2.8.tar.gz` & `tmp/DrissionPage-3.2.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "DrissionPage-3.2.8.tar", last modified: Fri Mar  3 11:49:54 2023, max compression
+gzip compressed data, was "DrissionPage-3.2.9.tar", last modified: Fri Mar  3 12:11:11 2023, max compression
```

## Comparing `DrissionPage-3.2.8.tar` & `DrissionPage-3.2.9.tar`

### file list

```diff
@@ -1,83 +1,83 @@
-drwxrwxrwx   0        0        0        0 2023-03-03 11:49:54.437867 DrissionPage-3.2.8/
-drwxrwxrwx   0        0        0        0 2023-03-03 11:49:54.080362 DrissionPage-3.2.8/DrissionPage/
--rw-rw-rw-   0        0        0      566 2023-03-01 05:59:36.000000 DrissionPage-3.2.8/DrissionPage/__init__.py
--rw-rw-rw-   0        0        0    10143 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/action_chains.py
--rw-rw-rw-   0        0        0     2473 2023-02-22 08:26:16.000000 DrissionPage-3.2.8/DrissionPage/action_chains.pyi
--rw-rw-rw-   0        0        0    13143 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/base.py
--rw-rw-rw-   0        0        0     5724 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/base.pyi
--rw-rw-rw-   0        0        0    44335 2023-03-03 11:48:34.000000 DrissionPage-3.2.8/DrissionPage/chromium_base.py
--rw-rw-rw-   0        0        0     9098 2023-03-03 10:25:51.000000 DrissionPage-3.2.8/DrissionPage/chromium_base.pyi
--rw-rw-rw-   0        0        0     8004 2023-03-03 08:42:49.000000 DrissionPage-3.2.8/DrissionPage/chromium_driver.py
--rw-rw-rw-   0        0        0     1468 2023-03-03 06:41:59.000000 DrissionPage-3.2.8/DrissionPage/chromium_driver.pyi
--rw-rw-rw-   0        0        0    82312 2023-03-03 07:15:04.000000 DrissionPage-3.2.8/DrissionPage/chromium_element.py
--rw-rw-rw-   0        0        0    17584 2023-03-03 06:43:23.000000 DrissionPage-3.2.8/DrissionPage/chromium_element.pyi
--rw-rw-rw-   0        0        0    21974 2023-02-22 00:43:45.000000 DrissionPage-3.2.8/DrissionPage/chromium_frame.py
--rw-rw-rw-   0        0        0     5735 2023-02-20 06:49:35.000000 DrissionPage-3.2.8/DrissionPage/chromium_frame.pyi
--rw-rw-rw-   0        0        0    28813 2023-03-02 11:51:28.000000 DrissionPage-3.2.8/DrissionPage/chromium_page.py
--rw-rw-rw-   0        0        0     6610 2023-03-03 06:41:59.000000 DrissionPage-3.2.8/DrissionPage/chromium_page.pyi
--rw-rw-rw-   0        0        0    15056 2023-02-27 00:44:34.000000 DrissionPage-3.2.8/DrissionPage/chromium_tab.py
--rw-rw-rw-   0        0        0     5827 2023-02-27 00:44:34.000000 DrissionPage-3.2.8/DrissionPage/chromium_tab.pyi
--rw-rw-rw-   0        0        0      292 2023-03-01 05:59:36.000000 DrissionPage-3.2.8/DrissionPage/common.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:49:54.182788 DrissionPage-3.2.8/DrissionPage/commons/
--rw-rw-rw-   0        0        0     7427 2023-03-03 03:54:39.000000 DrissionPage-3.2.8/DrissionPage/commons/browser.py
--rw-rw-rw-   0        0        0      483 2023-02-16 02:46:25.000000 DrissionPage-3.2.8/DrissionPage/commons/browser.pyi
--rw-rw-rw-   0        0        0      257 2023-03-01 05:52:20.000000 DrissionPage-3.2.8/DrissionPage/commons/by.py
--rw-rw-rw-   0        0        0      960 2023-02-22 07:06:52.000000 DrissionPage-3.2.8/DrissionPage/commons/cli.py
--rw-rw-rw-   0        0        0      847 2023-02-23 00:46:59.000000 DrissionPage-3.2.8/DrissionPage/commons/constants.py
--rw-rw-rw-   0        0        0    21028 2023-02-21 00:47:33.000000 DrissionPage-3.2.8/DrissionPage/commons/keys.py
--rw-rw-rw-   0        0        0     8277 2023-03-01 05:58:00.000000 DrissionPage-3.2.8/DrissionPage/commons/locator.py
--rw-rw-rw-   0        0        0      284 2023-02-16 02:46:25.000000 DrissionPage-3.2.8/DrissionPage/commons/locator.pyi
--rw-rw-rw-   0        0        0     4241 2023-02-16 02:46:25.000000 DrissionPage-3.2.8/DrissionPage/commons/tools.py
--rw-rw-rw-   0        0        0      672 2023-03-03 10:44:59.000000 DrissionPage-3.2.8/DrissionPage/commons/tools.pyi
--rw-rw-rw-   0        0        0     8547 2023-02-17 11:39:17.000000 DrissionPage-3.2.8/DrissionPage/commons/web.py
--rw-rw-rw-   0        0        0     1001 2023-02-16 02:46:25.000000 DrissionPage-3.2.8/DrissionPage/commons/web.pyi
-drwxrwxrwx   0        0        0        0 2023-03-03 11:49:54.271153 DrissionPage-3.2.8/DrissionPage/configs/
--rw-rw-rw-   0        0        0    14212 2023-03-03 03:55:14.000000 DrissionPage-3.2.8/DrissionPage/configs/chromium_options.py
--rw-rw-rw-   0        0        0     3399 2023-03-03 06:41:59.000000 DrissionPage-3.2.8/DrissionPage/configs/chromium_options.pyi
--rw-rw-rw-   0        0        0      868 2023-02-28 01:03:31.000000 DrissionPage-3.2.8/DrissionPage/configs/configs.ini
--rw-rw-rw-   0        0        0    12628 2023-02-16 02:36:13.000000 DrissionPage-3.2.8/DrissionPage/configs/driver_options.py
--rw-rw-rw-   0        0        0     2909 2023-02-16 02:36:13.000000 DrissionPage-3.2.8/DrissionPage/configs/driver_options.pyi
--rw-rw-rw-   0        0        0     3901 2023-02-17 00:54:09.000000 DrissionPage-3.2.8/DrissionPage/configs/options_manage.py
--rw-rw-rw-   0        0        0      871 2023-02-16 02:36:13.000000 DrissionPage-3.2.8/DrissionPage/configs/options_manage.pyi
--rw-rw-rw-   0        0        0    13050 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/configs/session_options.py
--rw-rw-rw-   0        0        0     3486 2023-03-03 06:41:59.000000 DrissionPage-3.2.8/DrissionPage/configs/session_options.pyi
--rw-rw-rw-   0        0        0    13080 2023-02-27 00:44:34.000000 DrissionPage-3.2.8/DrissionPage/easy_set.py
--rw-rw-rw-   0        0        0     2351 2023-02-20 06:54:30.000000 DrissionPage-3.2.8/DrissionPage/easy_set.pyi
--rw-rw-rw-   0        0        0     1153 2023-03-03 01:01:50.000000 DrissionPage-3.2.8/DrissionPage/errors.py
-drwxrwxrwx   0        0        0        0 2023-03-03 11:49:54.425967 DrissionPage-3.2.8/DrissionPage/mixpage/
--rw-rw-rw-   0        0        0    11360 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/mixpage/base.py
--rw-rw-rw-   0        0        0     5075 2023-02-17 00:54:09.000000 DrissionPage-3.2.8/DrissionPage/mixpage/base.pyi
--rw-rw-rw-   0        0        0    16193 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/mixpage/drission.py
--rw-rw-rw-   0        0        0     2832 2023-02-17 00:54:09.000000 DrissionPage-3.2.8/DrissionPage/mixpage/drission.pyi
--rw-rw-rw-   0        0        0    52349 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/mixpage/driver_element.py
--rw-rw-rw-   0        0        0    10683 2023-02-17 00:54:09.000000 DrissionPage-3.2.8/DrissionPage/mixpage/driver_element.pyi
--rw-rw-rw-   0        0        0    23350 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/mixpage/driver_page.py
--rw-rw-rw-   0        0        0     6178 2023-02-17 00:54:09.000000 DrissionPage-3.2.8/DrissionPage/mixpage/driver_page.pyi
--rw-rw-rw-   0        0        0    14069 2023-02-17 00:54:09.000000 DrissionPage-3.2.8/DrissionPage/mixpage/mix_page.py
--rw-rw-rw-   0        0        0     5661 2023-02-17 00:54:09.000000 DrissionPage-3.2.8/DrissionPage/mixpage/mix_page.pyi
--rw-rw-rw-   0        0        0    14845 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/mixpage/session_element.py
--rw-rw-rw-   0        0        0     3826 2023-02-17 00:54:09.000000 DrissionPage-3.2.8/DrissionPage/mixpage/session_element.pyi
--rw-rw-rw-   0        0        0    19675 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/mixpage/session_page.py
--rw-rw-rw-   0        0        0     7715 2023-03-03 06:41:59.000000 DrissionPage-3.2.8/DrissionPage/mixpage/session_page.pyi
--rw-rw-rw-   0        0        0     9199 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/mixpage/shadow_root_element.py
--rw-rw-rw-   0        0        0     2791 2023-02-17 00:54:09.000000 DrissionPage-3.2.8/DrissionPage/mixpage/shadow_root_element.pyi
--rw-rw-rw-   0        0        0    14995 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/session_element.py
--rw-rw-rw-   0        0        0     4185 2023-02-23 02:47:18.000000 DrissionPage-3.2.8/DrissionPage/session_element.pyi
--rw-rw-rw-   0        0        0    19077 2023-02-24 06:53:35.000000 DrissionPage-3.2.8/DrissionPage/session_page.py
--rw-rw-rw-   0        0        0     7632 2023-03-03 06:41:59.000000 DrissionPage-3.2.8/DrissionPage/session_page.pyi
--rw-rw-rw-   0        0        0    22789 2023-03-03 10:18:39.000000 DrissionPage-3.2.8/DrissionPage/web_page.py
--rw-rw-rw-   0        0        0     7074 2023-02-27 00:44:34.000000 DrissionPage-3.2.8/DrissionPage/web_page.pyi
-drwxrwxrwx   0        0        0        0 2023-03-03 11:49:54.096962 DrissionPage-3.2.8/DrissionPage.egg-info/
--rw-rw-rw-   0        0        0     5810 2023-03-03 11:49:53.000000 DrissionPage-3.2.8/DrissionPage.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     2379 2023-03-03 11:49:53.000000 DrissionPage-3.2.8/DrissionPage.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-03-03 11:49:53.000000 DrissionPage-3.2.8/DrissionPage.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       53 2023-03-03 11:49:53.000000 DrissionPage-3.2.8/DrissionPage.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0        2 2023-02-23 09:40:29.000000 DrissionPage-3.2.8/DrissionPage.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       85 2023-03-03 11:49:53.000000 DrissionPage-3.2.8/DrissionPage.egg-info/requires.txt
--rw-rw-rw-   0        0        0       13 2023-03-03 11:49:53.000000 DrissionPage-3.2.8/DrissionPage.egg-info/top_level.txt
--rw-rw-rw-   0        0        0     1534 2020-04-26 07:01:29.000000 DrissionPage-3.2.8/LICENSE
--rw-rw-rw-   0        0        0      127 2023-01-28 00:34:32.000000 DrissionPage-3.2.8/MANIFEST.in
--rw-rw-rw-   0        0        0     5810 2023-03-03 11:49:54.436376 DrissionPage-3.2.8/PKG-INFO
--rw-rw-rw-   0        0        0     5246 2023-02-23 06:00:34.000000 DrissionPage-3.2.8/README.md
--rw-rw-rw-   0        0        0       42 2023-03-03 11:49:54.437867 DrissionPage-3.2.8/setup.cfg
--rw-rw-rw-   0        0        0     1219 2023-03-03 07:44:34.000000 DrissionPage-3.2.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-03 12:11:11.174975 DrissionPage-3.2.9/
+drwxrwxrwx   0        0        0        0 2023-03-03 12:11:10.760544 DrissionPage-3.2.9/DrissionPage/
+-rw-rw-rw-   0        0        0      566 2023-03-01 05:59:36.000000 DrissionPage-3.2.9/DrissionPage/__init__.py
+-rw-rw-rw-   0        0        0    10143 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/action_chains.py
+-rw-rw-rw-   0        0        0     2473 2023-02-22 08:26:16.000000 DrissionPage-3.2.9/DrissionPage/action_chains.pyi
+-rw-rw-rw-   0        0        0    13143 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/base.py
+-rw-rw-rw-   0        0        0     5724 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/base.pyi
+-rw-rw-rw-   0        0        0    44298 2023-03-03 12:10:56.000000 DrissionPage-3.2.9/DrissionPage/chromium_base.py
+-rw-rw-rw-   0        0        0     9099 2023-03-03 12:03:57.000000 DrissionPage-3.2.9/DrissionPage/chromium_base.pyi
+-rw-rw-rw-   0        0        0     8004 2023-03-03 08:42:49.000000 DrissionPage-3.2.9/DrissionPage/chromium_driver.py
+-rw-rw-rw-   0        0        0     1468 2023-03-03 06:41:59.000000 DrissionPage-3.2.9/DrissionPage/chromium_driver.pyi
+-rw-rw-rw-   0        0        0    82312 2023-03-03 07:15:04.000000 DrissionPage-3.2.9/DrissionPage/chromium_element.py
+-rw-rw-rw-   0        0        0    17584 2023-03-03 06:43:23.000000 DrissionPage-3.2.9/DrissionPage/chromium_element.pyi
+-rw-rw-rw-   0        0        0    21974 2023-02-22 00:43:45.000000 DrissionPage-3.2.9/DrissionPage/chromium_frame.py
+-rw-rw-rw-   0        0        0     5735 2023-02-20 06:49:35.000000 DrissionPage-3.2.9/DrissionPage/chromium_frame.pyi
+-rw-rw-rw-   0        0        0    28813 2023-03-02 11:51:28.000000 DrissionPage-3.2.9/DrissionPage/chromium_page.py
+-rw-rw-rw-   0        0        0     6610 2023-03-03 06:41:59.000000 DrissionPage-3.2.9/DrissionPage/chromium_page.pyi
+-rw-rw-rw-   0        0        0    15056 2023-02-27 00:44:34.000000 DrissionPage-3.2.9/DrissionPage/chromium_tab.py
+-rw-rw-rw-   0        0        0     5827 2023-02-27 00:44:34.000000 DrissionPage-3.2.9/DrissionPage/chromium_tab.pyi
+-rw-rw-rw-   0        0        0      292 2023-03-01 05:59:36.000000 DrissionPage-3.2.9/DrissionPage/common.py
+drwxrwxrwx   0        0        0        0 2023-03-03 12:11:10.894224 DrissionPage-3.2.9/DrissionPage/commons/
+-rw-rw-rw-   0        0        0     7427 2023-03-03 03:54:39.000000 DrissionPage-3.2.9/DrissionPage/commons/browser.py
+-rw-rw-rw-   0        0        0      483 2023-02-16 02:46:25.000000 DrissionPage-3.2.9/DrissionPage/commons/browser.pyi
+-rw-rw-rw-   0        0        0      257 2023-03-01 05:52:20.000000 DrissionPage-3.2.9/DrissionPage/commons/by.py
+-rw-rw-rw-   0        0        0      960 2023-02-22 07:06:52.000000 DrissionPage-3.2.9/DrissionPage/commons/cli.py
+-rw-rw-rw-   0        0        0      847 2023-02-23 00:46:59.000000 DrissionPage-3.2.9/DrissionPage/commons/constants.py
+-rw-rw-rw-   0        0        0    21028 2023-02-21 00:47:33.000000 DrissionPage-3.2.9/DrissionPage/commons/keys.py
+-rw-rw-rw-   0        0        0     8277 2023-03-01 05:58:00.000000 DrissionPage-3.2.9/DrissionPage/commons/locator.py
+-rw-rw-rw-   0        0        0      284 2023-02-16 02:46:25.000000 DrissionPage-3.2.9/DrissionPage/commons/locator.pyi
+-rw-rw-rw-   0        0        0     4241 2023-02-16 02:46:25.000000 DrissionPage-3.2.9/DrissionPage/commons/tools.py
+-rw-rw-rw-   0        0        0      672 2023-03-03 10:44:59.000000 DrissionPage-3.2.9/DrissionPage/commons/tools.pyi
+-rw-rw-rw-   0        0        0     8547 2023-02-17 11:39:17.000000 DrissionPage-3.2.9/DrissionPage/commons/web.py
+-rw-rw-rw-   0        0        0     1001 2023-02-16 02:46:25.000000 DrissionPage-3.2.9/DrissionPage/commons/web.pyi
+drwxrwxrwx   0        0        0        0 2023-03-03 12:11:10.985230 DrissionPage-3.2.9/DrissionPage/configs/
+-rw-rw-rw-   0        0        0    14212 2023-03-03 03:55:14.000000 DrissionPage-3.2.9/DrissionPage/configs/chromium_options.py
+-rw-rw-rw-   0        0        0     3399 2023-03-03 06:41:59.000000 DrissionPage-3.2.9/DrissionPage/configs/chromium_options.pyi
+-rw-rw-rw-   0        0        0      868 2023-02-28 01:03:31.000000 DrissionPage-3.2.9/DrissionPage/configs/configs.ini
+-rw-rw-rw-   0        0        0    12628 2023-02-16 02:36:13.000000 DrissionPage-3.2.9/DrissionPage/configs/driver_options.py
+-rw-rw-rw-   0        0        0     2909 2023-02-16 02:36:13.000000 DrissionPage-3.2.9/DrissionPage/configs/driver_options.pyi
+-rw-rw-rw-   0        0        0     3901 2023-02-17 00:54:09.000000 DrissionPage-3.2.9/DrissionPage/configs/options_manage.py
+-rw-rw-rw-   0        0        0      871 2023-02-16 02:36:13.000000 DrissionPage-3.2.9/DrissionPage/configs/options_manage.pyi
+-rw-rw-rw-   0        0        0    13050 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/configs/session_options.py
+-rw-rw-rw-   0        0        0     3486 2023-03-03 06:41:59.000000 DrissionPage-3.2.9/DrissionPage/configs/session_options.pyi
+-rw-rw-rw-   0        0        0    13080 2023-02-27 00:44:34.000000 DrissionPage-3.2.9/DrissionPage/easy_set.py
+-rw-rw-rw-   0        0        0     2351 2023-02-20 06:54:30.000000 DrissionPage-3.2.9/DrissionPage/easy_set.pyi
+-rw-rw-rw-   0        0        0     1153 2023-03-03 01:01:50.000000 DrissionPage-3.2.9/DrissionPage/errors.py
+drwxrwxrwx   0        0        0        0 2023-03-03 12:11:11.164174 DrissionPage-3.2.9/DrissionPage/mixpage/
+-rw-rw-rw-   0        0        0    11360 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/mixpage/base.py
+-rw-rw-rw-   0        0        0     5075 2023-02-17 00:54:09.000000 DrissionPage-3.2.9/DrissionPage/mixpage/base.pyi
+-rw-rw-rw-   0        0        0    16193 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/mixpage/drission.py
+-rw-rw-rw-   0        0        0     2832 2023-02-17 00:54:09.000000 DrissionPage-3.2.9/DrissionPage/mixpage/drission.pyi
+-rw-rw-rw-   0        0        0    52349 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/mixpage/driver_element.py
+-rw-rw-rw-   0        0        0    10683 2023-02-17 00:54:09.000000 DrissionPage-3.2.9/DrissionPage/mixpage/driver_element.pyi
+-rw-rw-rw-   0        0        0    23350 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/mixpage/driver_page.py
+-rw-rw-rw-   0        0        0     6178 2023-02-17 00:54:09.000000 DrissionPage-3.2.9/DrissionPage/mixpage/driver_page.pyi
+-rw-rw-rw-   0        0        0    14069 2023-02-17 00:54:09.000000 DrissionPage-3.2.9/DrissionPage/mixpage/mix_page.py
+-rw-rw-rw-   0        0        0     5661 2023-02-17 00:54:09.000000 DrissionPage-3.2.9/DrissionPage/mixpage/mix_page.pyi
+-rw-rw-rw-   0        0        0    14845 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/mixpage/session_element.py
+-rw-rw-rw-   0        0        0     3826 2023-02-17 00:54:09.000000 DrissionPage-3.2.9/DrissionPage/mixpage/session_element.pyi
+-rw-rw-rw-   0        0        0    19675 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/mixpage/session_page.py
+-rw-rw-rw-   0        0        0     7715 2023-03-03 06:41:59.000000 DrissionPage-3.2.9/DrissionPage/mixpage/session_page.pyi
+-rw-rw-rw-   0        0        0     9199 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/mixpage/shadow_root_element.py
+-rw-rw-rw-   0        0        0     2791 2023-02-17 00:54:09.000000 DrissionPage-3.2.9/DrissionPage/mixpage/shadow_root_element.pyi
+-rw-rw-rw-   0        0        0    14995 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/session_element.py
+-rw-rw-rw-   0        0        0     4185 2023-02-23 02:47:18.000000 DrissionPage-3.2.9/DrissionPage/session_element.pyi
+-rw-rw-rw-   0        0        0    19077 2023-02-24 06:53:35.000000 DrissionPage-3.2.9/DrissionPage/session_page.py
+-rw-rw-rw-   0        0        0     7632 2023-03-03 06:41:59.000000 DrissionPage-3.2.9/DrissionPage/session_page.pyi
+-rw-rw-rw-   0        0        0    22789 2023-03-03 10:18:39.000000 DrissionPage-3.2.9/DrissionPage/web_page.py
+-rw-rw-rw-   0        0        0     7074 2023-02-27 00:44:34.000000 DrissionPage-3.2.9/DrissionPage/web_page.pyi
+drwxrwxrwx   0        0        0        0 2023-03-03 12:11:10.797754 DrissionPage-3.2.9/DrissionPage.egg-info/
+-rw-rw-rw-   0        0        0     5810 2023-03-03 12:11:09.000000 DrissionPage-3.2.9/DrissionPage.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     2379 2023-03-03 12:11:09.000000 DrissionPage-3.2.9/DrissionPage.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-03 12:11:09.000000 DrissionPage-3.2.9/DrissionPage.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       53 2023-03-03 12:11:09.000000 DrissionPage-3.2.9/DrissionPage.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0        2 2023-02-23 09:40:29.000000 DrissionPage-3.2.9/DrissionPage.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       85 2023-03-03 12:11:09.000000 DrissionPage-3.2.9/DrissionPage.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       13 2023-03-03 12:11:09.000000 DrissionPage-3.2.9/DrissionPage.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0     1534 2020-04-26 07:01:29.000000 DrissionPage-3.2.9/LICENSE
+-rw-rw-rw-   0        0        0      127 2023-01-28 00:34:32.000000 DrissionPage-3.2.9/MANIFEST.in
+-rw-rw-rw-   0        0        0     5810 2023-03-03 12:11:11.174005 DrissionPage-3.2.9/PKG-INFO
+-rw-rw-rw-   0        0        0     5246 2023-02-23 06:00:34.000000 DrissionPage-3.2.9/README.md
+-rw-rw-rw-   0        0        0       42 2023-03-03 12:11:11.174975 DrissionPage-3.2.9/setup.cfg
+-rw-rw-rw-   0        0        0     1219 2023-03-03 12:02:30.000000 DrissionPage-3.2.9/setup.py
```

### Comparing `DrissionPage-3.2.8/DrissionPage/__init__.py` & `DrissionPage-3.2.9/DrissionPage/__init__.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/action_chains.py` & `DrissionPage-3.2.9/DrissionPage/action_chains.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/action_chains.pyi` & `DrissionPage-3.2.9/DrissionPage/action_chains.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/base.py` & `DrissionPage-3.2.9/DrissionPage/base.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/base.pyi` & `DrissionPage-3.2.9/DrissionPage/base.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_base.py` & `DrissionPage-3.2.9/DrissionPage/chromium_base.py`

 * *Files 0% similar despite different names*

```diff
@@ -824,33 +824,31 @@
         :param save_path: 录屏保存位置
         :param quality: 录屏质量
         :return: None
         """
         self.set(save_path, quality)
         if self._path is None:
             raise ValueError('save_path必须设置。')
-        if not self._path.isascii():
-            raise TypeError('仅支持英文路径。')
         clean_folder(self._path)
         self._page.driver.Page.screencastFrame = self._onScreencastFrame
         self._page.run_cdp('Page.startScreencast', everyNthFrame=1, quality=self._quality)
 
-    def stop(self, to_mp4=True, video_name=None):
+    def stop(self, to_mp4=False, video_name=None):
         """停止录屏
         :param to_mp4: 是否合并成MP4格式
         :param video_name: 视频文件名，为None时以当前时间名命
         :return: 文件路径
         """
         self._page.driver.Page.screencastFrame = None
         self._page.run_cdp('Page.stopScreencast')
         if not to_mp4:
             return str(Path(self._path).absolute())
 
-        if not str(video_name).isascii():
-            raise TypeError('仅支持英文文件名。')
+        if not str(video_name).isascii() or not str(self._path).isascii():
+            raise TypeError('转换成视频仅支持英文路径和文件名。')
 
         try:
             from cv2 import VideoWriter, imread
             from numpy import fromfile, uint8
         except ModuleNotFoundError:
             raise ModuleNotFoundError('请先安装cv2，pip install opencv-python')
```

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_base.pyi` & `DrissionPage-3.2.9/DrissionPage/chromium_base.pyi`

 * *Files 0% similar despite different names*

```diff
@@ -201,15 +201,15 @@
     def __init__(self, page: ChromiumBase):
         self._page: ChromiumBase = ...
         self._path: str = ...
         self._quality: int = ...
 
     def start(self, save_path: Union[str, Path] = None, quality: int = None) -> None: ...
 
-    def stop(self, to_mp4: bool = True, video_name: str = None) -> str: ...
+    def stop(self, to_mp4: bool = False, video_name: str = None) -> str: ...
 
     def set(self, save_path: Union[str, Path] = None, quality: int = None) -> None: ...
 
     def _onScreencastFrame(self, **kwargs) -> None: ...
 
 
 class ChromiumBaseWaiter(object):
```

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_driver.py` & `DrissionPage-3.2.9/DrissionPage/chromium_driver.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_driver.pyi` & `DrissionPage-3.2.9/DrissionPage/chromium_driver.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_element.py` & `DrissionPage-3.2.9/DrissionPage/chromium_element.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_element.pyi` & `DrissionPage-3.2.9/DrissionPage/chromium_element.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_frame.py` & `DrissionPage-3.2.9/DrissionPage/chromium_frame.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_frame.pyi` & `DrissionPage-3.2.9/DrissionPage/chromium_frame.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_page.py` & `DrissionPage-3.2.9/DrissionPage/chromium_page.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_page.pyi` & `DrissionPage-3.2.9/DrissionPage/chromium_page.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_tab.py` & `DrissionPage-3.2.9/DrissionPage/chromium_tab.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/chromium_tab.pyi` & `DrissionPage-3.2.9/DrissionPage/chromium_tab.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/commons/browser.py` & `DrissionPage-3.2.9/DrissionPage/commons/browser.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/commons/cli.py` & `DrissionPage-3.2.9/DrissionPage/commons/cli.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/commons/constants.py` & `DrissionPage-3.2.9/DrissionPage/commons/constants.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/commons/keys.py` & `DrissionPage-3.2.9/DrissionPage/commons/keys.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/commons/locator.py` & `DrissionPage-3.2.9/DrissionPage/commons/locator.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/commons/tools.py` & `DrissionPage-3.2.9/DrissionPage/commons/tools.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/commons/tools.pyi` & `DrissionPage-3.2.9/DrissionPage/commons/tools.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/commons/web.py` & `DrissionPage-3.2.9/DrissionPage/commons/web.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/commons/web.pyi` & `DrissionPage-3.2.9/DrissionPage/commons/web.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/configs/chromium_options.py` & `DrissionPage-3.2.9/DrissionPage/configs/chromium_options.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/configs/chromium_options.pyi` & `DrissionPage-3.2.9/DrissionPage/configs/chromium_options.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/configs/configs.ini` & `DrissionPage-3.2.9/DrissionPage/configs/configs.ini`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/configs/driver_options.py` & `DrissionPage-3.2.9/DrissionPage/configs/driver_options.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/configs/driver_options.pyi` & `DrissionPage-3.2.9/DrissionPage/configs/driver_options.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/configs/options_manage.py` & `DrissionPage-3.2.9/DrissionPage/configs/options_manage.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/configs/options_manage.pyi` & `DrissionPage-3.2.9/DrissionPage/configs/options_manage.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/configs/session_options.py` & `DrissionPage-3.2.9/DrissionPage/configs/session_options.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/configs/session_options.pyi` & `DrissionPage-3.2.9/DrissionPage/configs/session_options.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/easy_set.py` & `DrissionPage-3.2.9/DrissionPage/easy_set.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/easy_set.pyi` & `DrissionPage-3.2.9/DrissionPage/easy_set.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/errors.py` & `DrissionPage-3.2.9/DrissionPage/errors.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/base.py` & `DrissionPage-3.2.9/DrissionPage/mixpage/base.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/base.pyi` & `DrissionPage-3.2.9/DrissionPage/mixpage/base.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/drission.py` & `DrissionPage-3.2.9/DrissionPage/mixpage/drission.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/drission.pyi` & `DrissionPage-3.2.9/DrissionPage/mixpage/drission.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/driver_element.py` & `DrissionPage-3.2.9/DrissionPage/mixpage/driver_element.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/driver_element.pyi` & `DrissionPage-3.2.9/DrissionPage/mixpage/driver_element.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/driver_page.py` & `DrissionPage-3.2.9/DrissionPage/mixpage/driver_page.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/driver_page.pyi` & `DrissionPage-3.2.9/DrissionPage/mixpage/driver_page.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/mix_page.py` & `DrissionPage-3.2.9/DrissionPage/mixpage/mix_page.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/mix_page.pyi` & `DrissionPage-3.2.9/DrissionPage/mixpage/mix_page.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/session_element.py` & `DrissionPage-3.2.9/DrissionPage/mixpage/session_element.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/session_element.pyi` & `DrissionPage-3.2.9/DrissionPage/mixpage/session_element.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/session_page.py` & `DrissionPage-3.2.9/DrissionPage/mixpage/session_page.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/session_page.pyi` & `DrissionPage-3.2.9/DrissionPage/mixpage/session_page.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/shadow_root_element.py` & `DrissionPage-3.2.9/DrissionPage/mixpage/shadow_root_element.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/mixpage/shadow_root_element.pyi` & `DrissionPage-3.2.9/DrissionPage/mixpage/shadow_root_element.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/session_element.py` & `DrissionPage-3.2.9/DrissionPage/session_element.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/session_element.pyi` & `DrissionPage-3.2.9/DrissionPage/session_element.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/session_page.py` & `DrissionPage-3.2.9/DrissionPage/session_page.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/session_page.pyi` & `DrissionPage-3.2.9/DrissionPage/session_page.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/web_page.py` & `DrissionPage-3.2.9/DrissionPage/web_page.py`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage/web_page.pyi` & `DrissionPage-3.2.9/DrissionPage/web_page.pyi`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/DrissionPage.egg-info/PKG-INFO` & `DrissionPage-3.2.9/DrissionPage.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: DrissionPage
-Version: 3.2.8
+Version: 3.2.9
 Summary: Python based web automation tool. It can control the browser and send and receive data packets.
 Home-page: https://gitee.com/g1879/DrissionPage
 Author: g1879
 Author-email: g1879@qq.com
 License: BSD
 Keywords: DrissionPage
 Classifier: Programming Language :: Python :: 3.6
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: DrissionPage Version: 3.2.8 Summary: Python based
+Metadata-Version: 2.1 Name: DrissionPage Version: 3.2.9 Summary: Python based
 web automation tool. It can control the browser and send and receive data
 packets. Home-page: https://gitee.com/g1879/DrissionPage Author: g1879 Author-
 email: g1879@qq.com License: BSD Keywords: DrissionPage Classifier: Programming
 Language :: Python :: 3.6 Classifier: Development Status :: 4 - Beta
 Classifier: Topic :: Utilities Classifier: License :: OSI Approved :: BSD
 License Requires-Python: >=3.6 Description-Content-Type: text/markdown License-
 File: LICENSE # â¨ï¸ æ¦è¿° DrissionPage æ¯ä¸ä¸ªåºäº python
```

### Comparing `DrissionPage-3.2.8/DrissionPage.egg-info/SOURCES.txt` & `DrissionPage-3.2.9/DrissionPage.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/LICENSE` & `DrissionPage-3.2.9/LICENSE`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/PKG-INFO` & `DrissionPage-3.2.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: DrissionPage
-Version: 3.2.8
+Version: 3.2.9
 Summary: Python based web automation tool. It can control the browser and send and receive data packets.
 Home-page: https://gitee.com/g1879/DrissionPage
 Author: g1879
 Author-email: g1879@qq.com
 License: BSD
 Keywords: DrissionPage
 Classifier: Programming Language :: Python :: 3.6
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: DrissionPage Version: 3.2.8 Summary: Python based
+Metadata-Version: 2.1 Name: DrissionPage Version: 3.2.9 Summary: Python based
 web automation tool. It can control the browser and send and receive data
 packets. Home-page: https://gitee.com/g1879/DrissionPage Author: g1879 Author-
 email: g1879@qq.com License: BSD Keywords: DrissionPage Classifier: Programming
 Language :: Python :: 3.6 Classifier: Development Status :: 4 - Beta
 Classifier: Topic :: Utilities Classifier: License :: OSI Approved :: BSD
 License Requires-Python: >=3.6 Description-Content-Type: text/markdown License-
 File: LICENSE # â¨ï¸ æ¦è¿° DrissionPage æ¯ä¸ä¸ªåºäº python
```

### Comparing `DrissionPage-3.2.8/README.md` & `DrissionPage-3.2.9/README.md`

 * *Files identical despite different names*

### Comparing `DrissionPage-3.2.8/setup.py` & `DrissionPage-3.2.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r", encoding='utf-8') as fh:
     long_description = fh.read()
 
 setup(
     name="DrissionPage",
-    version="3.2.8",
+    version="3.2.9",
     author="g1879",
     author_email="g1879@qq.com",
     description="Python based web automation tool. It can control the browser and send and receive data packets.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license="BSD",
     keywords="DrissionPage",
```

