# Comparing `tmp/lavacli-1.6.tar.gz` & `tmp/lavacli-1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "lavacli-1.6.tar", last modified: Fri Feb 24 15:34:01 2023, max compression
+gzip compressed data, was "lavacli-1.7.tar", last modified: Fri Apr  7 12:41:44 2023, max compression
```

## Comparing `lavacli-1.6.tar` & `lavacli-1.7.tar`

### file list

```diff
@@ -1,61 +1,65 @@
-drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-02-24 15:34:01.022431 lavacli-1.6/
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)      105 2018-07-13 09:52:07.000000 lavacli-1.6/.coveragerc
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     2506 2023-02-24 11:28:26.000000 lavacli-1.6/.gitlab-ci.yml
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    34520 2018-01-18 08:05:38.000000 lavacli-1.6/LICENSE
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)      141 2019-03-13 08:49:12.000000 lavacli-1.6/MANIFEST.in
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1150 2023-02-24 15:34:01.022431 lavacli-1.6/PKG-INFO
-drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-02-24 15:34:01.018430 lavacli-1.6/doc/
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)      604 2018-04-13 14:07:49.000000 lavacli-1.6/doc/Makefile
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     5259 2023-02-24 10:40:23.000000 lavacli-1.6/doc/conf.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     2335 2020-09-09 08:32:09.000000 lavacli-1.6/doc/configuration.rst
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)      379 2019-11-27 05:33:22.000000 lavacli-1.6/doc/index.rst
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)      721 2019-04-24 15:25:09.000000 lavacli-1.6/doc/install.rst
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     4624 2022-05-10 09:55:41.000000 lavacli-1.6/doc/usage.rst
-drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-02-24 15:34:01.018430 lavacli-1.6/lavacli/
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1344 2023-02-24 15:32:23.000000 lavacli-1.6/lavacli/__about__.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     9025 2023-02-24 15:05:54.000000 lavacli-1.6/lavacli/__init__.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)      851 2023-02-24 10:40:23.000000 lavacli-1.6/lavacli/__main__.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)      111 2022-03-31 04:08:12.000000 lavacli-1.6/lavacli/colors.py
-drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-02-24 15:34:01.022431 lavacli-1.6/lavacli/commands/
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)        0 2022-05-09 15:46:10.000000 lavacli-1.6/lavacli/commands/__init__.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     4001 2023-02-24 10:40:23.000000 lavacli-1.6/lavacli/commands/aliases.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    11793 2023-02-24 10:40:23.000000 lavacli-1.6/lavacli/commands/device_types.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    15460 2023-02-24 11:14:44.000000 lavacli-1.6/lavacli/commands/devices.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    10914 2023-02-24 15:03:12.000000 lavacli-1.6/lavacli/commands/events.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     4156 2023-02-24 10:40:23.000000 lavacli-1.6/lavacli/commands/identities.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    24817 2023-02-24 10:44:52.000000 lavacli-1.6/lavacli/commands/jobs.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    23878 2023-02-24 11:14:44.000000 lavacli-1.6/lavacli/commands/lab.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     3217 2023-02-24 10:40:23.000000 lavacli-1.6/lavacli/commands/results.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     9679 2023-02-24 11:14:44.000000 lavacli-1.6/lavacli/commands/system.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     3689 2023-02-24 10:40:23.000000 lavacli-1.6/lavacli/commands/tags.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     4119 2023-02-24 11:14:44.000000 lavacli-1.6/lavacli/commands/utils.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    13681 2023-02-24 11:14:44.000000 lavacli-1.6/lavacli/commands/workers.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1761 2023-02-24 10:44:52.000000 lavacli-1.6/lavacli/utils.py
-drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-02-24 15:34:01.022431 lavacli-1.6/lavacli.egg-info/
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1150 2023-02-24 15:34:00.000000 lavacli-1.6/lavacli.egg-info/PKG-INFO
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1151 2023-02-24 15:34:00.000000 lavacli-1.6/lavacli.egg-info/SOURCES.txt
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)        1 2023-02-24 15:34:00.000000 lavacli-1.6/lavacli.egg-info/dependency_links.txt
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)       41 2023-02-24 15:34:00.000000 lavacli-1.6/lavacli.egg-info/entry_points.txt
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)       42 2023-02-24 15:34:00.000000 lavacli-1.6/lavacli.egg-info/requires.txt
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)        8 2023-02-24 15:34:00.000000 lavacli-1.6/lavacli.egg-info/top_level.txt
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)        1 2023-02-24 15:33:30.000000 lavacli-1.6/lavacli.egg-info/zip-safe
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)       37 2020-11-02 09:35:16.000000 lavacli-1.6/requirements.txt
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)       38 2023-02-24 15:34:01.022431 lavacli-1.6/setup.cfg
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     2424 2023-02-24 10:40:23.000000 lavacli-1.6/setup.py
-drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-02-24 15:34:01.022431 lavacli-1.6/share/
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)      838 2018-04-13 12:29:55.000000 lavacli-1.6/share/lavacli.yaml
-drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-02-24 15:34:01.022431 lavacli-1.6/tests/
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)        0 2022-12-05 17:35:49.000000 lavacli-1.6/tests/__init__.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1800 2023-02-24 11:14:44.000000 lavacli-1.6/tests/conftest.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     8982 2023-02-24 10:40:23.000000 lavacli-1.6/tests/test_aliases.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    21634 2023-02-24 10:40:23.000000 lavacli-1.6/tests/test_device_types.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    39737 2023-02-24 11:14:44.000000 lavacli-1.6/tests/test_devices.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    26771 2023-02-24 10:40:23.000000 lavacli-1.6/tests/test_events.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1324 2023-02-24 10:40:23.000000 lavacli-1.6/tests/test_helpers.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     7446 2023-02-24 11:14:44.000000 lavacli-1.6/tests/test_identities.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    65588 2023-02-24 10:40:23.000000 lavacli-1.6/tests/test_jobs.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1615 2023-02-24 11:14:44.000000 lavacli-1.6/tests/test_lavacli.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    11619 2023-02-24 10:40:23.000000 lavacli-1.6/tests/test_results.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    25696 2023-02-24 10:40:23.000000 lavacli-1.6/tests/test_system.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)     6550 2023-02-24 10:40:23.000000 lavacli-1.6/tests/test_tags.py
--rw-r--r--   0 ivoire    (1000) ivoire    (1000)    26696 2023-02-24 11:14:44.000000 lavacli-1.6/tests/test_workers.py
+drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-04-07 12:41:44.641114 lavacli-1.7/
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)      105 2018-07-13 09:52:07.000000 lavacli-1.7/.coveragerc
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     2506 2023-03-17 09:18:40.000000 lavacli-1.7/.gitlab-ci.yml
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    34520 2018-01-18 08:05:38.000000 lavacli-1.7/LICENSE
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)      141 2019-03-13 08:49:12.000000 lavacli-1.7/MANIFEST.in
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1150 2023-04-07 12:41:44.641114 lavacli-1.7/PKG-INFO
+drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-04-07 12:41:44.637114 lavacli-1.7/doc/
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)      604 2018-04-13 14:07:49.000000 lavacli-1.7/doc/Makefile
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     5259 2023-02-24 10:40:23.000000 lavacli-1.7/doc/conf.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     2335 2020-09-09 08:32:09.000000 lavacli-1.7/doc/configuration.rst
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)      379 2019-11-27 05:33:22.000000 lavacli-1.7/doc/index.rst
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)      721 2019-04-24 15:25:09.000000 lavacli-1.7/doc/install.rst
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     4624 2022-05-10 09:55:41.000000 lavacli-1.7/doc/usage.rst
+drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-04-07 12:41:44.641114 lavacli-1.7/lavacli/
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1344 2023-04-07 12:35:31.000000 lavacli-1.7/lavacli/__about__.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     9098 2023-04-07 07:01:47.000000 lavacli-1.7/lavacli/__init__.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)      851 2023-02-24 10:40:23.000000 lavacli-1.7/lavacli/__main__.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)      111 2022-03-31 04:08:12.000000 lavacli-1.7/lavacli/colors.py
+drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-04-07 12:41:44.641114 lavacli-1.7/lavacli/commands/
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)        0 2022-05-09 15:46:10.000000 lavacli-1.7/lavacli/commands/__init__.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     4001 2023-02-24 10:40:23.000000 lavacli-1.7/lavacli/commands/aliases.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    13999 2023-04-07 12:33:18.000000 lavacli-1.7/lavacli/commands/device_types.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    15547 2023-04-07 07:01:47.000000 lavacli-1.7/lavacli/commands/devices.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     9742 2023-03-17 09:10:17.000000 lavacli-1.7/lavacli/commands/events.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     5767 2023-04-07 12:33:18.000000 lavacli-1.7/lavacli/commands/groups.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     4156 2023-02-24 10:40:23.000000 lavacli-1.7/lavacli/commands/identities.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    23030 2023-04-07 07:01:47.000000 lavacli-1.7/lavacli/commands/jobs.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    33394 2023-04-07 12:33:18.000000 lavacli-1.7/lavacli/commands/lab.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     3217 2023-02-24 10:40:23.000000 lavacli-1.7/lavacli/commands/results.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     9213 2023-03-17 09:10:17.000000 lavacli-1.7/lavacli/commands/system.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     3689 2023-02-24 10:40:23.000000 lavacli-1.7/lavacli/commands/tags.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    11204 2023-04-07 12:33:18.000000 lavacli-1.7/lavacli/commands/users.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     4119 2023-04-07 07:01:44.000000 lavacli-1.7/lavacli/commands/utils.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    12997 2023-04-07 07:01:47.000000 lavacli-1.7/lavacli/commands/workers.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1808 2023-03-21 10:08:31.000000 lavacli-1.7/lavacli/utils.py
+drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-04-07 12:41:44.641114 lavacli-1.7/lavacli.egg-info/
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1150 2023-04-07 12:41:44.000000 lavacli-1.7/lavacli.egg-info/PKG-INFO
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1242 2023-04-07 12:41:44.000000 lavacli-1.7/lavacli.egg-info/SOURCES.txt
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)        1 2023-04-07 12:41:44.000000 lavacli-1.7/lavacli.egg-info/dependency_links.txt
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)       41 2023-04-07 12:41:44.000000 lavacli-1.7/lavacli.egg-info/entry_points.txt
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)       36 2023-04-07 12:41:44.000000 lavacli-1.7/lavacli.egg-info/requires.txt
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)        8 2023-04-07 12:41:44.000000 lavacli-1.7/lavacli.egg-info/top_level.txt
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)        1 2023-04-07 12:41:44.000000 lavacli-1.7/lavacli.egg-info/zip-safe
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)       36 2023-03-17 09:09:30.000000 lavacli-1.7/requirements.txt
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)       38 2023-04-07 12:41:44.641114 lavacli-1.7/setup.cfg
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     2417 2023-03-17 09:10:17.000000 lavacli-1.7/setup.py
+drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-04-07 12:41:44.641114 lavacli-1.7/share/
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)      838 2018-04-13 12:29:55.000000 lavacli-1.7/share/lavacli.yaml
+drwxr-xr-x   0 ivoire    (1000) ivoire    (1000)        0 2023-04-07 12:41:44.641114 lavacli-1.7/tests/
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)        0 2023-04-07 07:02:55.000000 lavacli-1.7/tests/__init__.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1806 2023-04-07 07:02:55.000000 lavacli-1.7/tests/conftest.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     8982 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_aliases.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    20063 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_device_types.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    32637 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_devices.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    24515 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_events.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1324 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_helpers.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     7504 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_identities.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    58342 2023-04-07 12:33:40.000000 lavacli-1.7/tests/test_jobs.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    76698 2023-04-07 12:33:18.000000 lavacli-1.7/tests/test_lab.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     1615 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_lavacli.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    11619 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_results.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    25702 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_system.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     6550 2023-04-07 07:02:55.000000 lavacli-1.7/tests/test_tags.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)     4743 2023-04-07 12:33:18.000000 lavacli-1.7/tests/test_users.py
+-rw-r--r--   0 ivoire    (1000) ivoire    (1000)    24888 2023-04-07 12:33:53.000000 lavacli-1.7/tests/test_workers.py
```

### Comparing `lavacli-1.6/.gitlab-ci.yml` & `lavacli-1.7/.gitlab-ci.yml`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/LICENSE` & `lavacli-1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/PKG-INFO` & `lavacli-1.7/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lavacli
-Version: 1.6
+Version: 1.7
 Summary: LAVA XML-RPC command line interface
 Home-page: https://git.lavasoftware.org/lava/lavacli
 Author: Rémi Duraffort
 Author-email: remi.duraffort@linaro.org
 License: AGPLv3+
 Project-URL: Bug Tracker, https://git.lavasoftware.org/lava/lavacli/issues/
 Project-URL: Documentation, https://docs.lavasoftware.org/lavacli/
@@ -18,9 +18,9 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Topic :: Communications
 Classifier: Topic :: Software Development :: Testing
 Classifier: Topic :: System :: Networking
-Requires-Python: >=3.4
+Requires-Python: >=3.7
 License-File: LICENSE
```

### Comparing `lavacli-1.6/doc/Makefile` & `lavacli-1.7/doc/Makefile`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/doc/conf.py` & `lavacli-1.7/doc/conf.py`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/doc/configuration.rst` & `lavacli-1.7/doc/configuration.rst`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/doc/install.rst` & `lavacli-1.7/doc/install.rst`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/doc/usage.rst` & `lavacli-1.7/doc/usage.rst`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/lavacli/__about__.py` & `lavacli-1.7/lavacli/__about__.py`

 * *Files 8% similar despite different names*

```diff
@@ -38,8 +38,8 @@
 
 
 __author__ = "Rémi Duraffort"
 __author_email__ = "remi.duraffort@linaro.org"
 __description__ = "LAVA XML-RPC command line interface"
 __license__ = "AGPLv3+"
 __url__ = "https://git.lavasoftware.org/lava/lavacli"
-__version__ = "1.6"
+__version__ = "1.7"
```

### Comparing `lavacli-1.6/lavacli/__init__.py` & `lavacli-1.7/lavacli/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -31,20 +31,22 @@
 
 from .__about__ import __version__
 from .commands import (
     aliases,
     device_types,
     devices,
     events,
+    groups,
     identities,
     jobs,
     lab,
     results,
     system,
     tags,
+    users,
     utils,
     workers,
 )
 from .utils import VERSION_LATEST, exc2str, parse_version, safe_yaml
 
 
 class RequestsTransport(xmlrpc.client.Transport):
@@ -182,20 +184,22 @@
 def main():
     # List of known commands
     commands = {
         "aliases": aliases,
         "devices": devices,
         "device-types": device_types,
         "events": events,
+        "groups": groups,
         "identities": identities,
         "jobs": jobs,
         "lab": lab,
         "results": results,
         "system": system,
         "tags": tags,
+        "users": users,
         "utils": utils,
         "workers": workers,
     }
 
     # Parsing is made of two phases as arguments depends on the API version of
     # the remote server.
     # 1/ Parse the common arguments
```

### Comparing `lavacli-1.6/lavacli/__main__.py` & `lavacli-1.7/lavacli/__main__.py`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/lavacli/commands/aliases.py` & `lavacli-1.7/lavacli/commands/aliases.py`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/lavacli/commands/device_types.py` & `lavacli-1.7/lavacli/commands/device_types.py`

 * *Files 10% similar despite different names*

```diff
@@ -93,33 +93,32 @@
         dest="output_format",
         default=None,
         action="store_const",
         const="yaml",
         help="print as yaml",
     )
 
-    if version >= (2018, 4):
-        # "heath-check"
-        dt_hc = sub.add_parser("health-check", help="device-type health-check")
-        dt_sub = dt_hc.add_subparsers(dest="sub_sub_sub_command", help="Sub commands")
-        dt_sub.required = True
-        if version >= (2022, 4):
-            dt_delete = dt_sub.add_parser(
-                "delete", help="delete the device-type health-check"
-            )
-            dt_delete.add_argument("name", help="name of the device-type")
-
-        dt_get = dt_sub.add_parser("get", help="get the device-type health-check")
-        dt_get.add_argument("name", help="name of the device-type")
-
-        dt_set = dt_sub.add_parser("set", help="set the device-type health-check")
-        dt_set.add_argument("name", help="name of the device-type")
-        dt_set.add_argument(
-            "definition", type=argparse.FileType("r"), help="health-check definition"
+    # "heath-check"
+    dt_hc = sub.add_parser("health-check", help="device-type health-check")
+    dt_sub = dt_hc.add_subparsers(dest="sub_sub_sub_command", help="Sub commands")
+    dt_sub.required = True
+    if version >= (2022, 4):
+        dt_delete = dt_sub.add_parser(
+            "delete", help="delete the device-type health-check"
         )
+        dt_delete.add_argument("name", help="name of the device-type")
+
+    dt_get = dt_sub.add_parser("get", help="get the device-type health-check")
+    dt_get.add_argument("name", help="name of the device-type")
+
+    dt_set = dt_sub.add_parser("set", help="set the device-type health-check")
+    dt_set.add_argument("name", help="name of the device-type")
+    dt_set.add_argument(
+        "definition", type=argparse.FileType("r"), help="health-check definition"
+    )
 
     # "list"
     dt_list = sub.add_parser("list", help="list available device-types")
     dt_list.add_argument(
         "--all",
         "-a",
         dest="show_all",
@@ -141,14 +140,52 @@
         dest="output_format",
         default=None,
         action="store_const",
         const="yaml",
         help="print as yaml",
     )
 
+    # "perms"
+    if version >= (2023, 3):
+        dt_perms = sub.add_parser("perms", help="permissions")
+        perms_sub = dt_perms.add_subparsers(
+            dest="sub_sub_sub_command", help="Sub commands"
+        )
+        perms_sub.required = True
+
+        perms_add = perms_sub.add_parser("add", help="add permissions")
+        perms_add.add_argument("name", help="name of the device-type")
+        perms_add.add_argument("group", help="group")
+        perms_add.add_argument("permission", help="permission")
+
+        perms_delete = perms_sub.add_parser("delete", help="delete permissions")
+        perms_delete.add_argument("name", help="name of the device-type")
+        perms_delete.add_argument("group", help="group")
+        perms_delete.add_argument("permission", help="permission")
+
+        perms_list = perms_sub.add_parser("list", help="list permissions")
+        perms_list.add_argument("name", help="name of the device-type")
+        out_format = perms_list.add_mutually_exclusive_group()
+        out_format.add_argument(
+            "--json",
+            dest="output_format",
+            default=None,
+            action="store_const",
+            const="json",
+            help="print as json",
+        )
+        out_format.add_argument(
+            "--yaml",
+            dest="output_format",
+            default=None,
+            action="store_const",
+            const="yaml",
+            help="print as yaml",
+        )
+
     # "show"
     dt_show = sub.add_parser("show", help="show device-type details")
     dt_show.add_argument("name", help="name of the device-type")
     out_format = dt_show.add_mutually_exclusive_group()
     out_format.add_argument(
         "--json",
         dest="output_format",
@@ -306,14 +343,36 @@
     else:
         print("Device-Types:")
         for dt in device_types:
             print(f"* {dt['name']} ({dt['devices']})")
     return 0
 
 
+def handle_perms(proxy, options, _):
+    if options.sub_sub_sub_command == "add":
+        proxy.scheduler.device_types.perms_add(
+            options.name, options.group, options.permission
+        )
+    elif options.sub_sub_sub_command == "delete":
+        proxy.scheduler.device_types.perms_delete(
+            options.name, options.group, options.permission
+        )
+    elif options.sub_sub_sub_command == "list":
+        perms = proxy.scheduler.device_types.perms_list(options.name)
+        if options.output_format == "json":
+            print(json.dumps(perms))
+        elif options.output_format == "yaml":
+            safe_yaml.dump(perms, sys.stdout)
+        else:
+            print("Permissions:")
+            for perm in perms:
+                print("* %s %s" % (perm["group"], perm["name"]))
+    return 0
+
+
 def handle_show(proxy, options, config):
     dt = proxy.scheduler.device_types.show(options.name)
 
     if options.output_format == "json":
         print(json.dumps(dt))
     elif options.output_format == "yaml":
         safe_yaml.dump(dt, sys.stdout)
@@ -356,12 +415,13 @@
 
 def handle(proxy, options, config):
     handlers = {
         "add": handle_add,
         "aliases": handle_aliases,
         "health-check": handle_hc,
         "list": handle_list,
+        "perms": handle_perms,
         "show": handle_show,
         "template": handle_template,
         "update": handle_update,
     }
     return handlers[options.sub_sub_command](proxy, options, config)
```

### Comparing `lavacli-1.6/lavacli/commands/devices.py` & `lavacli-1.7/lavacli/commands/devices.py`

 * *Files 12% similar despite different names*

```diff
@@ -37,34 +37,20 @@
     devices_add.add_argument("--worker", required=True, help="worker name")
     devices_add.add_argument("--description", default=None, help="device description")
 
     owner = devices_add.add_mutually_exclusive_group()
     owner.add_argument("--user", default=None, help="device owner")
     owner.add_argument("--group", default=None, help="device group owner")
 
-    if version >= (2018, 1):
-        devices_add.add_argument(
-            "--health",
-            default=None,
-            choices=["GOOD", "UNKNOWN", "LOOPING", "BAD", "MAINTENANCE", "RETIRED"],
-            help="device health",
-        )
-    else:
-        devices_add.add_argument(
-            "--status",
-            default=None,
-            choices=["OFFLINE", "IDLE", "RUNNING", "OFFLINING", "RETIRED", "RESERVED"],
-            help="device status",
-        )
-        devices_add.add_argument(
-            "--health",
-            default=None,
-            choices=["UNKNOWN", "PASS", "FAIL", "LOOPING"],
-            help="device health status",
-        )
+    devices_add.add_argument(
+        "--health",
+        default=None,
+        choices=["GOOD", "UNKNOWN", "LOOPING", "BAD", "MAINTENANCE", "RETIRED"],
+        help="device health",
+    )
 
     devices_add.add_argument(
         "--private",
         action="store_true",
         default=False,
         help="private device [default=public]",
     )
@@ -124,31 +110,66 @@
         default=None,
         action="store_const",
         const="yaml",
         help="print as yaml",
     )
 
     # "maintenance"
-    if version >= (2018, 1):
-        devices_maintenance = sub.add_parser(
-            "maintenance", help="maintenance the device"
-        )
-        devices_maintenance.add_argument("name", help="device name")
-        devices_maintenance.add_argument(
-            "--force",
-            default=False,
-            action="store_true",
-            help="force device maintenance by canceling running job",
-        )
-        devices_maintenance.add_argument(
-            "--no-wait",
-            dest="wait",
-            default=True,
-            action="store_false",
-            help="do not wait for the device to be idle",
+    devices_maintenance = sub.add_parser("maintenance", help="maintenance the device")
+    devices_maintenance.add_argument("name", help="device name")
+    devices_maintenance.add_argument(
+        "--force",
+        default=False,
+        action="store_true",
+        help="force device maintenance by canceling running job",
+    )
+    devices_maintenance.add_argument(
+        "--no-wait",
+        dest="wait",
+        default=True,
+        action="store_false",
+        help="do not wait for the device to be idle",
+    )
+
+    # "perms"
+    if version >= (2023, 3):
+        devices_perms = sub.add_parser("perms", help="permissions")
+        perms_sub = devices_perms.add_subparsers(
+            dest="sub_sub_sub_command", help="Sub commands"
+        )
+        perms_sub.required = True
+
+        perms_add = perms_sub.add_parser("add", help="add permissions")
+        perms_add.add_argument("name", help="name of the device")
+        perms_add.add_argument("group", help="group")
+        perms_add.add_argument("permission", help="permission")
+
+        perms_delete = perms_sub.add_parser("delete", help="delete permissions")
+        perms_delete.add_argument("name", help="name of the device")
+        perms_delete.add_argument("group", help="group")
+        perms_delete.add_argument("permission", help="permission")
+
+        perms_list = perms_sub.add_parser("list", help="list permissions")
+        perms_list.add_argument("name", help="name of the device")
+        out_format = perms_list.add_mutually_exclusive_group()
+        out_format.add_argument(
+            "--json",
+            dest="output_format",
+            default=None,
+            action="store_const",
+            const="json",
+            help="print as json",
+        )
+        out_format.add_argument(
+            "--yaml",
+            dest="output_format",
+            default=None,
+            action="store_const",
+            const="yaml",
+            help="print as yaml",
         )
 
     # "show"
     devices_show = sub.add_parser("show", help="show device details")
     devices_show.add_argument("name", help="device name")
     out_format = devices_show.add_mutually_exclusive_group()
     out_format.add_argument(
@@ -209,34 +230,20 @@
         "--description", default=None, help="device description"
     )
 
     owner = devices_update.add_mutually_exclusive_group()
     owner.add_argument("--user", default=None, help="device owner")
     owner.add_argument("--group", default=None, help="device group owner")
 
-    if version >= (2018, 1):
-        devices_update.add_argument(
-            "--health",
-            default=None,
-            choices=["GOOD", "UNKNOWN", "LOOPING", "BAD", "MAINTENANCE", "RETIRED"],
-            help="device health",
-        )
-    else:
-        devices_update.add_argument(
-            "--status",
-            default=None,
-            choices=["OFFLINE", "IDLE", "RUNNING", "OFFLINING", "RETIRED", "RESERVED"],
-            help="device status",
-        )
-        devices_update.add_argument(
-            "--health",
-            default=None,
-            choices=["UNKNOWN", "PASS", "FAIL", "LOOPING"],
-            help="device health status",
-        )
+    devices_update.add_argument(
+        "--health",
+        default=None,
+        choices=["GOOD", "UNKNOWN", "LOOPING", "BAD", "MAINTENANCE", "RETIRED"],
+        help="device health",
+    )
 
     display = devices_update.add_mutually_exclusive_group()
     display.add_argument(
         "--public", default=None, action="store_true", help="make the device public"
     )
     display.add_argument(
         "--private", dest="public", action="store_false", help="make the device private"
@@ -244,37 +251,24 @@
 
 
 def help_string():
     return "manage devices"
 
 
 def handle_add(proxy, options, config):
-    if config["version"] >= (2018, 1):
-        proxy.scheduler.devices.add(
-            options.name,
-            options.type,
-            options.worker,
-            options.user,
-            options.group,
-            not options.private,
-            options.health,
-            options.description,
-        )
-    else:
-        proxy.scheduler.devices.add(
-            options.name,
-            options.type,
-            options.worker,
-            options.user,
-            options.group,
-            not options.private,
-            options.status,
-            options.health,
-            options.description,
-        )
+    proxy.scheduler.devices.add(
+        options.name,
+        options.type,
+        options.worker,
+        options.user,
+        options.group,
+        not options.private,
+        options.health,
+        options.description,
+    )
     return 0
 
 
 def _lookups(value, fields):
     try:
         for key in fields:
             if isinstance(value, list):
@@ -344,29 +338,23 @@
     if options.output_format == "json":
         print(json.dumps(devices))
     elif options.output_format == "yaml":
         safe_yaml.dump(devices, sys.stdout)
     else:
         print("Devices:")
         for device in devices:
-            if config["version"] >= (2018, 1):
-                print(
-                    "* %s (%s): %s,%s"
-                    % (
-                        device["hostname"],
-                        device["type"],
-                        device["state"],
-                        device["health"],
-                    )
-                )
-            else:
-                print(
-                    "* %s (%s): %s"
-                    % (device["hostname"], device["type"], device["status"])
+            print(
+                "* %s (%s): %s,%s"
+                % (
+                    device["hostname"],
+                    device["type"],
+                    device["state"],
+                    device["health"],
                 )
+            )
     return 0
 
 
 def handle_maintenance(proxy, options, _):
     proxy.scheduler.devices.update(
         options.name, None, None, None, None, "MAINTENANCE", None
     )
@@ -383,29 +371,48 @@
             and proxy.scheduler.jobs.show(current_job)["state"] != "Finished"
         ):
             print("--> waiting")
             time.sleep(5)
     return 0
 
 
+def handle_perms(proxy, options, _):
+    if options.sub_sub_sub_command == "add":
+        proxy.scheduler.devices.perms_add(
+            options.name, options.group, options.permission
+        )
+    elif options.sub_sub_sub_command == "delete":
+        proxy.scheduler.devices.perms_delete(
+            options.name, options.group, options.permission
+        )
+    elif options.sub_sub_sub_command == "list":
+        perms = proxy.scheduler.devices.perms_list(options.name)
+        if options.output_format == "json":
+            print(json.dumps(perms))
+        elif options.output_format == "yaml":
+            safe_yaml.dump(perms, sys.stdout)
+        else:
+            print("Permissions:")
+            for perm in perms:
+                print("* %s %s" % (perm["group"], perm["name"]))
+    return 0
+
+
 def handle_show(proxy, options, config):
     device = proxy.scheduler.devices.show(options.name)
 
     if options.output_format == "json":
         print(json.dumps(device))
     elif options.output_format == "yaml":
         safe_yaml.dump(device, sys.stdout)
     else:
         print("name        : %s" % device["hostname"])
         print("device-type : %s" % device["device_type"])
-        if config["version"] >= (2018, 1):
-            print("state       : %s" % device["state"])
-            print("health      : %s" % device["health"])
-        else:
-            print("status      : %s" % device["status"])
+        print("state       : %s" % device["state"])
+        print("health      : %s" % device["health"])
         if config["version"] < (2019, 9):
             print("user        : %s" % device["user"])
             print("group       : %s" % device["group"])
         print("health job  : %s" % device["health_job"])
         print("description : %s" % device["description"])
         if config["version"] < (2019, 9):
             print("public      : %s" % device["public"])
@@ -432,42 +439,31 @@
             print("Tags:")
             for tag in tags:
                 print("* %s" % tag)
     return 0
 
 
 def handle_update(proxy, options, config):
-    if config["version"] >= (2018, 1):
-        proxy.scheduler.devices.update(
-            options.name,
-            options.worker,
-            options.user,
-            options.group,
-            options.public,
-            options.health,
-            options.description,
-        )
-    else:
-        proxy.scheduler.devices.update(
-            options.name,
-            options.worker,
-            options.user,
-            options.group,
-            options.public,
-            options.status,
-            options.health,
-            options.description,
-        )
+    proxy.scheduler.devices.update(
+        options.name,
+        options.worker,
+        options.user,
+        options.group,
+        options.public,
+        options.health,
+        options.description,
+    )
     return 0
 
 
 def handle(proxy, options, config):
     handlers = {
         "add": handle_add,
         "dict": handle_dict,
         "list": handle_list,
         "maintenance": handle_maintenance,
+        "perms": handle_perms,
         "show": handle_show,
         "tags": handle_tags,
         "update": handle_update,
     }
     return handlers[options.sub_sub_command](proxy, options, config)
```

### Comparing `lavacli-1.6/lavacli/commands/events.py` & `lavacli-1.7/lavacli/commands/events.py`

 * *Files 26% similar despite different names*

```diff
@@ -18,16 +18,14 @@
 
 import asyncio
 import json
 import sys
 from urllib.parse import urlparse
 
 import aiohttp
-import zmq
-from zmq.utils.strtypes import b, u
 
 from lavacli.__about__ import __version__
 
 
 def configure_parser(parser, version):
     sub = parser.add_subparsers(dest="sub_sub_command", help="Sub commands")
     sub.required = True
@@ -39,70 +37,69 @@
         action="append",
         default=None,
         choices=["device", "event", "testjob", "worker"],
         help="filter by topic type",
     )
 
     # "wait"
-    if version >= (2018, 1):
-        wait_parser = sub.add_parser("wait", help="wait for a specific event")
-        obj_parser = wait_parser.add_subparsers(dest="object", help="object to wait")
-        obj_parser.required = True
-
-        # "wait device"
-        device_parser = obj_parser.add_parser("device")
-        device_parser.add_argument("name", type=str, help="name of the device")
-        device_parser.add_argument(
-            "--state",
-            default=None,
-            choices=["IDLE", "RESERVED", "RUNNING"],
-            help="device state",
-        )
-        device_parser.add_argument(
-            "--health",
-            default=None,
-            choices=["GOOD", "UNKNOWN", "LOOPING", "BAD", "MAINTENANCE", "RETIRED"],
-            help="device health",
-        )
+    wait_parser = sub.add_parser("wait", help="wait for a specific event")
+    obj_parser = wait_parser.add_subparsers(dest="object", help="object to wait")
+    obj_parser.required = True
+
+    # "wait device"
+    device_parser = obj_parser.add_parser("device")
+    device_parser.add_argument("name", type=str, help="name of the device")
+    device_parser.add_argument(
+        "--state",
+        default=None,
+        choices=["IDLE", "RESERVED", "RUNNING"],
+        help="device state",
+    )
+    device_parser.add_argument(
+        "--health",
+        default=None,
+        choices=["GOOD", "UNKNOWN", "LOOPING", "BAD", "MAINTENANCE", "RETIRED"],
+        help="device health",
+    )
 
-        # "wait job"
-        testjob_parser = obj_parser.add_parser("job")
-        testjob_parser.add_argument("job_id", help="job id")
-        testjob_parser.add_argument(
-            "--state",
-            default=None,
-            choices=[
-                "SUBMITTED",
-                "SCHEDULING",
-                "SCHEDULED",
-                "RUNNING",
-                "CANCELING",
-                "FINISHED",
-            ],
-            help="job state",
-        )
-        testjob_parser.add_argument(
-            "--health",
-            default=None,
-            choices=["UNKNOWN", "COMPLETE", "INCOMPLETE", "CANCELED"],
-            help="job health",
-        )
+    # "wait job"
+    testjob_parser = obj_parser.add_parser("job")
+    testjob_parser.add_argument("job_id", help="job id")
+    testjob_parser.add_argument(
+        "--state",
+        default=None,
+        choices=[
+            "SUBMITTED",
+            "SCHEDULING",
+            "SCHEDULED",
+            "RUNNING",
+            "CANCELING",
+            "FINISHED",
+        ],
+        help="job state",
+    )
+    testjob_parser.add_argument(
+        "--health",
+        default=None,
+        choices=["UNKNOWN", "COMPLETE", "INCOMPLETE", "CANCELED"],
+        help="job health",
+    )
 
-        # "wait worker"
-        worker_parser = obj_parser.add_parser("worker")
-        worker_parser.add_argument("name", type=str, help="worker name")
-        worker_parser.add_argument(
-            "--state", default=None, choices=["ONLINE", "OFFLINE"], help="worker state"
-        )
-        worker_parser.add_argument(
-            "--health",
-            default=None,
-            choices=["ACTIVE", "MAINTENANCE", "RETIRED"],
-            help="worker health",
-        )
+    # "wait worker"
+    worker_parser = obj_parser.add_parser("worker")
+    worker_parser.add_argument("name", type=str, help="worker name")
+    worker_parser.add_argument(
+        "--state", default=None, choices=["ONLINE", "OFFLINE"], help="worker state"
+    )
+    worker_parser.add_argument(
+        "--health",
+        default=None,
+        choices=["ACTIVE", "MAINTENANCE", "RETIRED"],
+        help="worker health",
+    )
 
 
 def help_string():
     return "listen to events"
 
 
 def _get_zmq_url(proxy, options, config):
@@ -128,186 +125,167 @@
     topic_end = topic.split(".")[-1]
 
     # filter by topic_end
     if options.filter and topic_end not in options.filter:
         return
 
     if topic_end == "device":
-        if config["version"] >= (2018, 1):
-            msg = f"[{data['device']}] <{data['device_type']}> state={data['state']} health={data['health']}"
-        else:
-            msg = f"[{data['device']}] <{data['device_type']}> {data['status']}"
+        msg = f"[{data['device']}] <{data['device_type']}> state={data['state']} health={data['health']}"
         if "job" in data:
             msg += " for %s" % data["job"]
     elif topic_end == "testjob":
-        if config["version"] >= (2018, 1):
-            msg = f"[{data['job']}] <{data.get('device', '??')}> state={data['state']} health={data['health']} ({data['description']})"
-        else:
-            msg = f"[{data['job']}] <{data.get('device', '??')}> {data['status']} ({data['description']})"
+        msg = f"[{data['job']}] <{data.get('device', '??')}> state={data['state']} health={data['health']} ({data['description']})"
     elif topic_end == "worker":
         msg = f"[{data['hostname']}] state={data['state']} health={data['health']}"
     elif topic_end == "event":
         msg = f"[{data['job']}] message={data['message']}"
 
     if sys.stdout.isatty():
         print(
             f"\033[1;30m{dt}\033[0m \033[1;37m{topic}\033[0m \033[32m{username}\033[0m - {msg}"
         )
     else:
         print(f"{dt} {topic} {username} - {msg}")
 
 
-def handle_listen(proxy, options, config):
-    if config["version"] < (2020, 9):
-        # Try to find the socket url
-        url = _get_zmq_url(proxy, options, config)
-        if url is None:
-            print("Unable to find the socket url", file=sys.stderr)
-            return 1
-
-        context = zmq.Context()
-        sock = context.socket(zmq.SUB)
-        sock.setsockopt(zmq.SUBSCRIBE, b"")
-        # Set the sock proxy (if needed)
-        socks = config.get("events", {}).get("socks_proxy")
-        if socks is not None:
-            print(f"Listening to {url} (socks {socks})")
-            sock.setsockopt(zmq.SOCKS_PROXY, b(socks))
-        else:
-            print("Listening to %s" % url)
-
-        try:
-            sock.connect(url)
-        except zmq.error.ZMQError as exc:
-            print("Unable to connect: %s" % exc, file=sys.stderr)
-            return 1
-
-        while True:
-            msg = sock.recv_multipart()
-            try:
-                (topic, _, dt, username, data) = (u(m) for m in msg)
-            except ValueError:
-                print("Invalid message: %s" % msg, file=sys.stderr)
-                continue
-            print_event(options, config, topic, dt, username, data)
-
-    else:
-
-        async def handler():
-            HEADERS = {"User-Agent": "lavacli v%s" % __version__}
-            url = urlparse(options.uri)
-            scheme = url.scheme
-            path = url.path
-            if path.endswith("/RPC2/"):
-                path = path[:-5]
-            elif path.endswith("/RPC2"):
-                path = path[:-4]
-            if not path.endswith("/"):
-                path = path + "/"
-
-            ws_url = ws_url_redacted = f"{scheme}://{url.netloc}{path}ws/"
-            if "@" in url.netloc:
-                ws_url_redacted = f"{scheme}://<USERNAME>:<TOKEN>@{url.netloc.split('@')[-1]}{path}ws/"
-
-            try:
-                while True:
-                    try:
-                        async with aiohttp.ClientSession(headers=HEADERS) as session:
-                            print("Connecting to %s" % ws_url_redacted)
-                            async with session.ws_connect(ws_url, heartbeat=30) as ws:
-                                async for msg in ws:
-                                    if msg.type == aiohttp.WSMsgType.TEXT:
-                                        try:
-                                            data = json.loads(msg.data)
-                                            if "error" in data:
-                                                raise aiohttp.ClientError(data["error"])
-                                            (topic, _, dt, username, data) = data
-                                        except ValueError:
-                                            print(
-                                                "Invalid message: %s" % msg,
-                                                file=sys.stderr,
-                                            )
-                                            continue
-                                        print_event(
-                                            options, config, topic, dt, username, data
-                                        )
-                    except aiohttp.ClientError as exc:
-                        print("Connection issue: %s" % str(exc), file=sys.stderr)
-                        await asyncio.sleep(1)
-            except Exception as exc:
-                print(exc, file=sys.stderr)
+def loop_zmq_events(proxy, options, config, func):
+    import zmq  # pylint: disable=import-outside-toplevel
+    from zmq.utils.strtypes import b, u  # pylint: disable=import-outside-toplevel
 
-        asyncio.run(handler())
-    return 0
-
-
-def handle_wait(proxy, options, config):
     # Try to find the socket url
     url = _get_zmq_url(proxy, options, config)
     if url is None:
         print("Unable to find the socket url", file=sys.stderr)
         return 1
 
     context = zmq.Context()
     sock = context.socket(zmq.SUB)
-    # Filter by topic (if needed)
-    sock.setsockopt(zmq.SUBSCRIBE, b(config.get("events", {}).get("topic", "")))
-
+    sock.setsockopt(zmq.SUBSCRIBE, b"")
     # Set the sock proxy (if needed)
     socks = config.get("events", {}).get("socks_proxy")
     if socks is not None:
         print(f"Listening to {url} (socks {socks})")
         sock.setsockopt(zmq.SOCKS_PROXY, b(socks))
     else:
-        print(f"Listening to {url}")
+        print("Listening to %s" % url)
 
     try:
         sock.connect(url)
     except zmq.error.ZMQError as exc:
         print("Unable to connect: %s" % exc, file=sys.stderr)
         return 1
 
-    # "job" is called "testjob" in the events
-    object_topic = options.object
-    if object_topic == "job":
-        object_topic = "testjob"
-
-    # Wait for events
     while True:
         msg = sock.recv_multipart()
         try:
-            (topic, _uuid, _dt, _username, data) = (u(m) for m in msg)
+            (topic, _, dt, username, data) = (u(m) for m in msg)
         except ValueError:
             print("Invalid message: %s" % msg, file=sys.stderr)
             continue
+        if func(options, config, topic, dt, username, data):
+            break
+
+
+def loop_ws_events(proxy, options, config, func):
+    async def handler():
+        HEADERS = {"User-Agent": "lavacli v%s" % __version__}
+        url = urlparse(options.uri)
+        scheme = url.scheme
+        path = url.path
+        if path.endswith("/RPC2/"):
+            path = path[:-5]
+        elif path.endswith("/RPC2"):
+            path = path[:-4]
+        if not path.endswith("/"):
+            path = path + "/"
+
+        ws_url = ws_url_redacted = f"{scheme}://{url.netloc}{path}ws/"
+        if "@" in url.netloc:
+            ws_url_redacted = (
+                f"{scheme}://<USERNAME>:<TOKEN>@{url.netloc.split('@')[-1]}{path}ws/"
+            )
+
+        try:
+            while True:
+                try:
+                    async with aiohttp.ClientSession(headers=HEADERS) as session:
+                        print("Connecting to %s" % ws_url_redacted)
+                        async with session.ws_connect(ws_url, heartbeat=30) as ws:
+                            async for msg in ws:
+                                if msg.type == aiohttp.WSMsgType.TEXT:
+                                    try:
+                                        data = json.loads(msg.data)
+                                        if "error" in data:
+                                            raise aiohttp.ClientError(data["error"])
+                                        (topic, _, dt, username, data) = data
+                                    except ValueError:
+                                        print(
+                                            "Invalid message: %s" % msg,
+                                            file=sys.stderr,
+                                        )
+                                        continue
+                                    if func(options, config, topic, dt, username, data):
+                                        return 0
+                            print("Connection closed")
+                            await asyncio.sleep(1)
+                except aiohttp.ClientError as exc:
+                    print("Connection issue: %s" % str(exc), file=sys.stderr)
+                    await asyncio.sleep(1)
+        except Exception as exc:
+            print(exc, file=sys.stderr)
+
+    asyncio.run(handler())
+
+
+def handle_listen(proxy, options, config):
+    if config["version"] < (2020, 9):
+        loop_zmq_events(proxy, options, config, print_event)
+    else:
+        loop_ws_events(proxy, options, config, print_event)
+    return 0
+
+
+def handle_wait(proxy, options, config):
+    def wait(options, config, topic, dt, username, data):
+        # "job" is called "testjob" in the events
+        object_topic = options.object
+        if object_topic == "job":
+            object_topic = "testjob"
+
         data = json.loads(data)
 
         # Filter by object
         obj = topic.split(".")[-1]
         if obj != object_topic:
-            continue
+            return False
 
         if object_topic == "device":
             if data.get("device") != options.name:
-                continue
+                return False
         elif object_topic == "testjob":
             if data.get("job") != options.job_id:
-                continue
+                return False
         else:
             if data.get("hostname") != options.name:
-                continue
+                return False
 
         # Filter by state
         if options.state is not None:
             if data.get("state") != options.state.capitalize():
-                continue
+                return False
         # Filter by health
         if options.health is not None:
             if data.get("health") != options.health.capitalize():
-                continue
+                return False
+
+        return True
 
-        return 0
+    if config["version"] < (2020, 9):
+        loop_zmq_events(proxy, options, config, wait)
+    else:
+        loop_ws_events(proxy, options, config, wait)
+    return 0
 
 
 def handle(proxy, options, config):
     handlers = {"listen": handle_listen, "wait": handle_wait}
     return handlers[options.sub_sub_command](proxy, options, config)
```

### Comparing `lavacli-1.6/lavacli/commands/identities.py` & `lavacli-1.7/lavacli/commands/identities.py`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/lavacli/commands/jobs.py` & `lavacli-1.7/lavacli/commands/jobs.py`

 * *Files 4% similar despite different names*

```diff
@@ -53,63 +53,60 @@
     sub = parser.add_subparsers(dest="sub_sub_command", help="Sub commands")
     sub.required = True
 
     # "cancel"
     jobs_cancel = sub.add_parser("cancel", help="cancel a job")
     jobs_cancel.add_argument("job_id", nargs="+", help="job id")
 
-    if version >= (2018, 4):
-        # "config"
-        jobs_config = sub.add_parser("config", help="job configuration")
-        jobs_config.add_argument("job_id", help="job id")
-        jobs_config.add_argument(
-            "--dest", default=".", help="save files into this directory"
-        )
+    # "config"
+    jobs_config = sub.add_parser("config", help="job configuration")
+    jobs_config.add_argument("job_id", help="job id")
+    jobs_config.add_argument(
+        "--dest", default=".", help="save files into this directory"
+    )
 
     # "definition"
     jobs_definition = sub.add_parser("definition", help="job definition")
     jobs_definition.add_argument("job_id", help="job id")
 
     # "list"
     jobs_list = sub.add_parser("list", help="list jobs")
-    if version >= (2018, 4):
-        jobs_list.add_argument(
-            "--state",
-            type=str,
-            default=None,
-            choices=[
-                "SUBMITTED",
-                "SCHEDULING",
-                "SCHEDULED",
-                "RUNNING",
-                "CANCELING",
-                "FINISHED",
-            ],
-            help="filter jobs by state",
-        )
-        jobs_list.add_argument(
-            "--health",
-            type=str,
-            default=None,
-            choices=["UNKNOWN", "COMPLETE", "INCOMPLETE", "CANCELED"],
-            help="filter jobs by health",
-        )
-    if version >= (2018, 10):
-        jobs_list.add_argument(
-            "--since",
-            type=int,
-            default=0,
-            help="Filter by jobs which completed in the last N minutes.",
-        )
-        jobs_list.add_argument(
-            "--verbose",
-            dest="verbose",
-            action="store_true",
-            help="If verbose is True, add extra keys, including error_type.",
-        )
+    jobs_list.add_argument(
+        "--state",
+        type=str,
+        default=None,
+        choices=[
+            "SUBMITTED",
+            "SCHEDULING",
+            "SCHEDULED",
+            "RUNNING",
+            "CANCELING",
+            "FINISHED",
+        ],
+        help="filter jobs by state",
+    )
+    jobs_list.add_argument(
+        "--health",
+        type=str,
+        default=None,
+        choices=["UNKNOWN", "COMPLETE", "INCOMPLETE", "CANCELED"],
+        help="filter jobs by health",
+    )
+    jobs_list.add_argument(
+        "--since",
+        type=int,
+        default=0,
+        help="Filter by jobs which completed in the last N minutes.",
+    )
+    jobs_list.add_argument(
+        "--verbose",
+        dest="verbose",
+        action="store_true",
+        help="If verbose is True, add extra keys, including error_type.",
+    )
     jobs_list.add_argument(
         "--start", type=int, default=0, help="skip the N first jobs [default=0]"
     )
     jobs_list.add_argument(
         "--limit", type=int, default=25, help="limit to N jobs [default=25]"
     )
     out_format = jobs_list.add_mutually_exclusive_group()
@@ -138,42 +135,39 @@
         default=False,
         action="store_true",
         help="do not keep polling until the end of the job",
     )
     configure_log_options(jobs_logs)
 
     # "queue"
-    if version >= (2019, 1):
-        jobs_queue = sub.add_parser("queue", help="job queue")
-        jobs_queue.add_argument(
-            "device_types", nargs="*", help="filter by device-types"
-        )
-        out_format = jobs_queue.add_mutually_exclusive_group()
-        out_format.add_argument(
-            "--json",
-            dest="output_format",
-            default=None,
-            action="store_const",
-            const="json",
-            help="print as json",
-        )
-        out_format.add_argument(
-            "--yaml",
-            dest="output_format",
-            action="store_const",
-            const="yaml",
-            default=None,
-            help="print as yaml",
-        )
-        jobs_queue.add_argument(
-            "--start", type=int, default=0, help="skip the N first jobs [default=0]"
-        )
-        jobs_queue.add_argument(
-            "--limit", type=int, default=25, help="limit to N jobs [default=25]"
-        )
+    jobs_queue = sub.add_parser("queue", help="job queue")
+    jobs_queue.add_argument("device_types", nargs="*", help="filter by device-types")
+    out_format = jobs_queue.add_mutually_exclusive_group()
+    out_format.add_argument(
+        "--json",
+        dest="output_format",
+        default=None,
+        action="store_const",
+        const="json",
+        help="print as json",
+    )
+    out_format.add_argument(
+        "--yaml",
+        dest="output_format",
+        action="store_const",
+        const="yaml",
+        default=None,
+        help="print as yaml",
+    )
+    jobs_queue.add_argument(
+        "--start", type=int, default=0, help="skip the N first jobs [default=0]"
+    )
+    jobs_queue.add_argument(
+        "--limit", type=int, default=25, help="limit to N jobs [default=25]"
+    )
 
     # "resubmit"
     jobs_resubmit = sub.add_parser("resubmit", help="resubmit a job")
     jobs_resubmit.add_argument("job_id", help="job id")
     jobs_resubmit.add_argument(
         "--url",
         action="store_true",
@@ -269,30 +263,29 @@
         jobs_validate.add_argument(
             "definition", type=argparse.FileType("r"), help="job definition"
         )
         jobs_validate.add_argument(
             "--strict", action="store_true", default=False, help="check in strict mode"
         )
 
-    if version >= (2018, 1):
-        # "wait"
-        jobs_wait = sub.add_parser("wait", help="wait for the job to finish")
-        jobs_wait.add_argument("job_id", help="job id")
-        jobs_wait.add_argument(
-            "--polling",
-            default=5,
-            type=int,
-            help="polling interval in seconds [default=5s]",
-        )
-        jobs_wait.add_argument(
-            "--timeout",
-            default=0,
-            type=int,
-            help="Maximum time to wait in seconds, 0 to disable [default=0s]",
-        )
+    # "wait"
+    jobs_wait = sub.add_parser("wait", help="wait for the job to finish")
+    jobs_wait.add_argument("job_id", help="job id")
+    jobs_wait.add_argument(
+        "--polling",
+        default=5,
+        type=int,
+        help="polling interval in seconds [default=5s]",
+    )
+    jobs_wait.add_argument(
+        "--timeout",
+        default=0,
+        type=int,
+        help="Maximum time to wait in seconds, 0 to disable [default=0s]",
+    )
 
 
 def help_string():
     return "manage jobs"
 
 
 def handle_cancel(proxy, options, _):
@@ -338,38 +331,31 @@
 
 def handle_definition(proxy, options, _):
     print(proxy.scheduler.jobs.definition(options.job_id))
     return 0
 
 
 def handle_list(proxy, options, config):
-    if config["version"] >= (2018, 10):
-        jobs = proxy.scheduler.jobs.list(
-            options.state,
-            options.health,
-            options.start,
-            options.limit,
-            options.since,
-            options.verbose,
-        )
-    elif config["version"] >= (2018, 4):
-        jobs = proxy.scheduler.jobs.list(
-            options.state, options.health, options.start, options.limit
-        )
-    else:
-        jobs = proxy.scheduler.jobs.list(options.start, options.limit)
+    jobs = proxy.scheduler.jobs.list(
+        options.state,
+        options.health,
+        options.start,
+        options.limit,
+        options.since,
+        options.verbose,
+    )
 
     if options.output_format == "json":
         print(json.dumps(jobs))
     elif options.output_format == "yaml":
         safe_yaml.dump(jobs, sys.stdout)
     else:
         print(f"Jobs (from {1 + options.start} to {options.start + options.limit}):")
         for job in jobs:
-            if config["version"] >= (2018, 10) and options.verbose:
+            if options.verbose:
                 if job["error_type"]:
                     print(
                         "* %s: %s,%s [%s] (%s) - %s %s <%s> <%s> %s: %s"
                         % (
                             job["id"],
                             job["state"],
                             job["health"],
@@ -395,37 +381,26 @@
                             job["device_type"],
                             job["actual_device"],
                             job["start_time"],
                             job["end_time"],
                         )
                     )
 
-            elif config["version"] >= (2018, 1):
+            else:
                 print(
                     "* %s: %s,%s [%s] (%s) - %s"
                     % (
                         job["id"],
                         job["state"],
                         job["health"],
                         job["submitter"],
                         job["description"],
                         job["device_type"],
                     )
                 )
-            else:
-                print(
-                    "* %s: %s [%s] (%s) - %s"
-                    % (
-                        job["id"],
-                        job["status"],
-                        job["submitter"],
-                        job["description"],
-                        job["device_type"],
-                    )
-                )
     return 0
 
 
 if sys.stdout.isatty():
     COLORS = {
         "exception": "\033[1;31m",
         "error": "\033[1;31m",
@@ -493,24 +468,16 @@
                 + COLORS[level]
                 + msg
                 + COLORS["end"]
             )
 
 
 def _download_logs(proxy, version, job_id, start, end):
-    if version >= (2018, 6):
-        (finished, data) = proxy.scheduler.jobs.logs(job_id, start, end)
-        logs = safe_yaml.load(str(data))
-    else:
-        (finished, data) = proxy.scheduler.jobs.logs(job_id, start)
-        logs = safe_yaml.load(str(data))
-        if end is not None and len(logs) >= end - start:
-            if end < start:
-                end = start
-            logs = logs[: end - start]
+    (finished, data) = proxy.scheduler.jobs.logs(job_id, start, end)
+    logs = safe_yaml.load(str(data))
     return (finished, logs)
 
 
 def handle_logs(proxy, options, config):
     # Loop
     lines = options.start
     while True:
@@ -664,35 +631,32 @@
     return 0
 
 
 def handle_show(proxy, options, config):
     job = proxy.scheduler.jobs.show(options.job_id)
 
     if options.output_format == "json":
-        job["submit_time"] = job["submit_time"].value if job["submit_time"] else None
-        job["start_time"] = job["start_time"].value if job["start_time"] else None
-        job["end_time"] = job["end_time"].value if job["end_time"] else None
+        job["submit_time"] = job["submit_time"].value or None
+        job["start_time"] = job["start_time"].value or None
+        job["end_time"] = job["end_time"].value or None
         print(json.dumps(job))
     elif options.output_format == "yaml":
-        job["submit_time"] = job["submit_time"].value if job["submit_time"] else None
-        job["start_time"] = job["start_time"].value if job["start_time"] else None
-        job["end_time"] = job["end_time"].value if job["end_time"] else None
+        job["submit_time"] = job["submit_time"].value or None
+        job["start_time"] = job["start_time"].value or None
+        job["end_time"] = job["end_time"].value or None
         safe_yaml.dump(job, sys.stdout)
     else:
         print("id          : %s" % job["id"])
         print("description : %s" % job["description"])
         print("submitter   : %s" % job["submitter"])
         print("device-type : %s" % job["device_type"])
         print("device      : %s" % job["device"])
         print("health-check: %s" % job["health_check"])
-        if config["version"] >= (2018, 1):
-            print("state       : %s" % job["state"])
-            print("Health      : %s" % job["health"])
-        else:
-            print("status      : %s" % job["status"])
+        print("state       : %s" % job["state"])
+        print("Health      : %s" % job["health"])
         if job.get("failure_comment"):
             print("failure     : %s" % job["failure_comment"])
         print("pipeline    : %s" % job["pipeline"])
         print("tags        : %s" % str(job["tags"]))
         print("visibility  : %s" % job["visibility"])
         print("submit time : %s" % job["submit_time"])
         print("start time  : %s" % job["start_time"])
```

### Comparing `lavacli-1.6/lavacli/commands/lab.py` & `lavacli-1.7/lavacli/commands/lab.py`

 * *Files 19% similar despite different names*

```diff
@@ -61,23 +61,26 @@
 @dataclass
 class Device(Base):
     hostname: str
     device_type: str
     worker: str
     description: str = None
     tags: Set[str] = field(default_factory=set)
+    # TODO: add permissions
 
     def __post_init__(self):
         self.tags = set(self.tags)
 
     def diff(self, data: Dict[str, Any]) -> List[str]:
         data = data.copy()
         data["tags"] = set(data["tags"])
-        if data["description"] in ["", None]:
-            data["description"] = self.description
+        if data["description"] is None:
+            data["description"] = ""
+        if self.description is None:
+            self.description = ""
         return super().diff(data)
 
     def dump(self):
         defaults = {f.name: f.default for f in fields(self) if f.default != MISSING}
         data = {}
         for k, v in asdict(self).items():
             if k in defaults and v == defaults[k]:
@@ -113,23 +116,26 @@
     name: str
     description: str = ""
     health_disabled: str = False
     health_denominator: str = "hours"
     health_frequency: int = 24
     aliases: Set[str] = field(default_factory=set)
     display: bool = True
+    # TODO: add permissions
 
     def __post_init__(self):
         self.aliases = set(self.aliases)
 
     def diff(self, data: Dict[str, Any]) -> List[str]:
         data = data.copy()
         data["aliases"] = set(data["aliases"])
-        if data["description"] in ["", None]:
-            data["description"] = self.description
+        if data["description"] is None:
+            data["description"] = ""
+        if self.description is None:
+            self.description = ""
         return super().diff(data)
 
     def dump(self):
         defaults = {f.name: f.default for f in fields(self) if f.default != MISSING}
         data = {}
         for k, v in asdict(self).items():
             if k in defaults and v == defaults[k]:
@@ -167,24 +173,109 @@
     def set_template(self, base, text):
         (base / "device-types").mkdir(parents=True, exist_ok=True)
         (base / "device-types" / f"{self.name}.jinja2").write_text(
             text, encoding="utf-8"
         )
 
 
+@dataclass(frozen=True, order=True)
+class Permission:
+    app: str
+    model: str
+    codename: str
+
+    @classmethod
+    def from_str(cls, s):
+        app, model, codename = s.split(".")
+        return cls(app=app, model=model, codename=codename)
+
+    def dump(self):
+        return str(self)
+
+    def __repr__(self):
+        return f"{self.app}.{self.model}.{self.codename}"
+
+
+@dataclass
+class Group(Base):
+    name: str
+    permissions: Set[Permission] = field(default_factory=set)
+
+    def __post_init__(self):
+        self.permissions = set([Permission.from_str(p) for p in self.permissions])
+
+    def dump(self):
+        defaults = {f.name: f.default for f in fields(self) if f.default != MISSING}
+        data = {}
+        for k, v in asdict(self).items():
+            if k in defaults and v == defaults[k]:
+                continue
+            data[k] = v
+
+        if not data["permissions"]:
+            del data["permissions"]
+        else:
+            data["permissions"] = [p.dump() for p in sorted(data["permissions"])]
+        del data["name"]
+        return data if data else None
+
+
+@dataclass
+class User(Base):
+    username: str
+    last_name: str = ""
+    first_name: str = ""
+    email: str = ""
+    is_superuser: bool = False
+    is_staff: bool = False
+    is_active: bool = True
+    groups: Set[str] = field(default_factory=set)
+    permissions: Set[Permission] = field(default_factory=set)
+
+    def __post_init__(self):
+        self.groups = set(self.groups)
+        self.permissions = set([Permission.from_str(p) for p in self.permissions])
+
+    def diff(self, data: Dict[str, Any]) -> List[str]:
+        data = data.copy()
+        data["groups"] = set(data["groups"])
+        return super().diff(data)
+
+    def dump(self):
+        defaults = {f.name: f.default for f in fields(self) if f.default != MISSING}
+        data = {}
+        for k, v in asdict(self).items():
+            if k in defaults and v == defaults[k]:
+                continue
+            data[k] = v
+
+        if not data["groups"]:
+            del data["groups"]
+        else:
+            data["groups"] = sorted(data["groups"])
+        if not data["permissions"]:
+            del data["permissions"]
+        else:
+            data["permissions"] = [p.dump() for p in sorted(data["permissions"])]
+        del data["username"]
+        return data if data else None
+
+
 @dataclass
 class Worker(Base):
     hostname: str
     description: str = ""
     job_limit: int = 0
 
     def diff(self, data: Dict[str, Any]) -> List[str]:
         data = data.copy()
-        if data["description"] in ["", None]:
-            data["description"] = self.description
+        if data["description"] is None:
+            data["description"] = ""
+        if self.description is None:
+            self.description = ""
         return super().diff(data)
 
     def dump(self):
         defaults = {f.name: f.default for f in fields(self) if f.default != MISSING}
         data = {}
         for k, v in asdict(self).items():
             if k in defaults and v == defaults[k]:
@@ -233,31 +324,43 @@
         )
 
 
 @dataclass
 class Config:
     device_types: Dict[str, DeviceType]
     devices: Dict[str, Device]
+    groups: Dict[str, Group]
+    users: Dict[str, User]
     workers: Dict[str, Worker]
 
     def __post_init__(self):
         self.devices = {n: Device(hostname=n, **d) for n, d in self.devices.items()}
         self.device_types = {
             n: DeviceType(name=n, **(dt if dt is not None else {}))
             for n, dt in self.device_types.items()
         }
+        self.groups = {
+            n: Group(name=n, **(grp if grp is not None else {}))
+            for n, grp in self.groups.items()
+        }
+        self.users = {
+            n: User(username=n, **(user if user is not None else {}))
+            for n, user in self.users.items()
+        }
         self.workers = {
             h: Worker(hostname=h, **(w if w is not None else {}))
             for h, w in self.workers.items()
         }
 
     def dump(self):
         return {
             "device_types": {k: self.device_types[k].dump() for k in self.device_types},
             "devices": {k: self.devices[k].dump() for k in self.devices},
+            "groups": {k: self.groups[k].dump() for k in self.groups},
+            "users": {k: self.users[k].dump() for k in self.users},
             "workers": {k: self.workers[k].dump() for k in self.workers},
         }
 
 
 def configure_parser(parser, version):
     sub = parser.add_subparsers(dest="sub_sub_command", help="Sub commands")
     sub.required = True
@@ -288,59 +391,176 @@
 
 def help_string():
     return "manage lab configuration"
 
 
 def handle_apply(proxy, options, config):
     if not options.resources:
-        options.resources = ["devices", "device-types", "workers"]
+        options.resources = ["devices", "device-types", "groups", "users", "workers"]
 
     lab = Config(**ruamel.yaml.safe_load(options.config.read_text(encoding="utf-8")))
     base = (options.config / ".." / options.config.stem).resolve()
 
+    print(f"{colors.cyan}> groups{colors.reset}")
+    if "groups" not in options.resources:
+        print(f"  {colors.yellow}-> SKIP{colors.reset}")
+    elif config["version"] >= (2023, 3):
+        groups = proxy.auth.groups.list()
+        for group in lab.groups.values():
+            if group.name in groups:
+                print(f"  {colors.green}* {group.name}{colors.reset}")
+            else:
+                print(f"  {colors.yellow}* {group.name}{colors.reset}")
+                if not options.dry_run:
+                    proxy.auth.groups.add(group.name)
+
+            data = proxy.auth.groups.show(group.name)
+            data["permissions"] = set(
+                [Permission.from_str(p) for p in data["permissions"]]
+            )
+            diff = group.diff(data)
+            if "permissions" in diff:
+                print(f"    {colors.yellow}-> permissions{colors.reset}")
+                missing = group.permissions.difference(set(data["permissions"]))
+                for perm in missing:
+                    print(f"      {colors.green}+ {perm}{colors.reset}")
+                    if not options.dry_run:
+                        proxy.auth.groups.perms.add(
+                            group.name, perm.app, perm.model, perm.codename
+                        )
+                missing = set(data["permissions"]).difference(group.permissions)
+                for perm in missing:
+                    print(f"      {colors.red}- {perm}{colors.reset}")
+                    if not options.dry_run:
+                        proxy.auth.groups.perms.delete(
+                            group.name, perm.app, perm.model, perm.codename
+                        )
+
+    print(f"{colors.cyan}> users{colors.reset}")
+    if "users" not in options.resources:
+        print(f"  {colors.yellow}-> SKIP{colors.reset}")
+    elif config["version"] >= (2023, 3):
+        users = [user["username"] for user in proxy.auth.users.list()]
+        for user in lab.users.values():
+            if user.username in users:
+                print(f"  {colors.green}* {user.username}{colors.reset}")
+            else:
+                print(f"  {colors.yellow}* {user.username}{colors.reset}")
+                if not options.dry_run:
+                    proxy.auth.users.add(
+                        user.username,
+                        user.first_name or None,
+                        user.last_name or None,
+                        user.email or None,
+                        user.is_active,
+                        user.is_staff,
+                        user.is_superuser,
+                    )
+
+            data = proxy.auth.users.show(user.username)
+            data["permissions"] = set(
+                [Permission.from_str(p) for p in data["permissions"]]
+            )
+            diff = user.diff(data)
+            for name in (n for n in diff if n not in ["groups", "permissions"]):
+                print(
+                    f"    {colors.yellow}-> {name}: '{data[name]}' => '{getattr(user, name)}'{colors.reset}"
+                )
+
+            if diff:
+                if not options.dry_run:
+                    proxy.auth.users.update(
+                        user.username,
+                        user.first_name if "first_name" in diff else None,
+                        user.last_name if "last_name" in diff else None,
+                        user.email if "email" in diff else None,
+                        user.is_active if "is_active" in diff else None,
+                        user.is_staff if "is_staff" in diff else None,
+                        user.is_superuser if "is_superuser" in diff else None,
+                    )
+                if "groups" in diff:
+                    print(f"    {colors.yellow}-> groups{colors.reset}")
+                    missing = user.groups.difference(set(data["groups"]))
+                    for grp in missing:
+                        print(f"      {colors.green}+ {grp}{colors.reset}")
+                        if not options.dry_run:
+                            proxy.auth.users.groups.add(user.username, grp)
+                    missing = set(data["groups"]).difference(user.groups)
+                    for grp in missing:
+                        print(f"      {colors.red}- {grp}{colors.reset}")
+                        if not options.dry_run:
+                            proxy.auth.users.groups.delete(user.username, grp)
+
+                if "permissions" in diff:
+                    print(f"    {colors.yellow}-> permissions{colors.reset}")
+                    missing = user.permissions.difference(set(data["permissions"]))
+                    for perm in missing:
+                        print(f"      {colors.green}+ {perm}{colors.reset}")
+                        if not options.dry_run:
+                            proxy.auth.users.perms.add(
+                                user.username, perm.app, perm.model, perm.codename
+                            )
+                    missing = set(data["permissions"]).difference(user.permissions)
+                    for perm in missing:
+                        print(f"      {colors.red}- {perm}{colors.reset}")
+                        if not options.dry_run:
+                            proxy.auth.users.perms.delete(
+                                user.username, perm.app, perm.model, perm.codename
+                            )
+
     print(f"{colors.cyan}> device-types{colors.reset}")
     if "device-types" not in options.resources:
         print(f"  {colors.yellow}-> SKIP{colors.reset}")
     else:
         device_types = [dt["name"] for dt in proxy.scheduler.device_types.list(False)]
         for dt in lab.device_types.values():
             if dt.name in device_types:
                 print(f"  {colors.green}* {dt.name}{colors.reset}")
             else:
                 print(f"  {colors.yellow}* {dt.name}{colors.reset}")
-                raise NotImplementedError("Unable to create the device-type")
+                if not options.dry_run:
+                    proxy.scheduler.device_types.add(
+                        dt.name,
+                        dt.description or None,
+                        dt.display or True,
+                        # owners_only is deprecated.
+                        None,
+                        dt.health_frequency or 24,
+                        dt.health_denominator or "hours",
+                    )
             data = proxy.scheduler.device_types.show(dt.name)
             diff = dt.diff(data)
-            for name in (n for n in diff if n != "aliases"):
-                print(
-                    f"    {colors.yellow}-> {name}: '{data[name]}' => '{getattr(dt, name)}'{colors.reset}"
-                )
-            if diff:
+            dt_diff = [n for n in diff if n != "aliases"]
+            if dt_diff:
+                for name in dt_diff:
+                    print(
+                        f"    {colors.yellow}-> {name}: '{data[name]}' => '{getattr(dt, name)}'{colors.reset}"
+                    )
                 if not options.dry_run:
                     proxy.scheduler.device_types.update(
                         dt.name,
                         dt.description if "description" in diff else None,
                         dt.display if "display" in diff else None,
                         None,
                         dt.health_frequency if "health_frequency" in diff else None,
                         dt.health_denominator if "health_denominator" in diff else None,
                         dt.health_disabled if "health_disabled" in diff else None,
                     )
-                if "aliases" in diff:
-                    print(f"    {colors.yellow}-> aliases{colors.reset}")
-                    missing = dt.aliases.difference(set(data["aliases"]))
-                    for alias in missing:
-                        print(f"      {colors.green}+ {alias}{colors.reset}")
-                        if not options.dry_run:
-                            proxy.scheduler.device_types.aliases.add(dt.name, alias)
-                    missing = set(data["aliases"]).difference(dt.aliases)
-                    for alias in missing:
-                        print(f"      {colors.red}- {alias}{colors.reset}")
-                        if not options.dry_run:
-                            proxy.scheduler.device_types.aliases.delete(dt.name, alias)
+            if "aliases" in diff:
+                print(f"    {colors.yellow}-> aliases{colors.reset}")
+                missing = dt.aliases.difference(set(data["aliases"]))
+                for alias in missing:
+                    print(f"      {colors.green}+ {alias}{colors.reset}")
+                    if not options.dry_run:
+                        proxy.scheduler.device_types.aliases.add(dt.name, alias)
+                missing = set(data["aliases"]).difference(dt.aliases)
+                for alias in missing:
+                    print(f"      {colors.red}- {alias}{colors.reset}")
+                    if not options.dry_run:
+                        proxy.scheduler.device_types.aliases.delete(dt.name, alias)
 
             try:
                 hc = str(proxy.scheduler.device_types.get_health_check(dt.name))
             except xmlrpc.client.Fault as exc:
                 if exc.faultCode != 404:
                     raise
                 hc = None
@@ -459,42 +679,43 @@
                         None,
                         None,
                         None,
                         device.description,
                     )
             data = proxy.scheduler.devices.show(device.hostname)
             diff = device.diff(data)
-            for name in (n for n in diff if n != "tags"):
-                print(
-                    f"    {colors.yellow}-> {name}: '{data[name]}' => '{getattr(device, name)}'{colors.reset}"
-                )
-            if diff:
+            device_diff = [n for n in diff if n != "tags"]
+            if device_diff:
+                for name in device_diff:
+                    print(
+                        f"    {colors.yellow}-> {name}: '{data[name]}' => '{getattr(device, name)}'{colors.reset}"
+                    )
                 if not options.dry_run:
                     proxy.scheduler.devices.update(
                         device.hostname,
                         device.worker if "worker" in diff else None,
                         None,
                         None,
                         None,
                         None,
                         device.description if "description" in diff else None,
                         device.device_type if "device_type" in diff else None,
                     )
-                if "tags" in diff:
-                    print(f"    {colors.yellow}-> tags{colors.reset}")
-                    missing = device.tags.difference(set(data["tags"]))
-                    for tag in missing:
-                        print(f"      {colors.green}+ {tag}{colors.reset}")
-                        if not options.dry_run:
-                            proxy.scheduler.devices.tags.add(device.hostname, tag)
-                    missing = set(data["tags"]).difference(device.tags)
-                    for tag in missing:
-                        print(f"      {colors.red}- {tag}{colors.reset}")
-                        if not options.dry_run:
-                            proxy.scheduler.devices.tags.delete(device.hostname, tag)
+            if "tags" in diff:
+                print(f"    {colors.yellow}-> tags{colors.reset}")
+                missing = device.tags.difference(set(data["tags"]))
+                for tag in missing:
+                    print(f"      {colors.green}+ {tag}{colors.reset}")
+                    if not options.dry_run:
+                        proxy.scheduler.devices.tags.add(device.hostname, tag)
+                missing = set(data["tags"]).difference(device.tags)
+                for tag in missing:
+                    print(f"      {colors.red}- {tag}{colors.reset}")
+                    if not options.dry_run:
+                        proxy.scheduler.devices.tags.delete(device.hostname, tag)
 
             try:
                 ddict = str(proxy.scheduler.devices.get_dictionary(device.hostname))
             except xmlrpc.client.Fault as exc:
                 if exc.faultCode != 404:
                     raise
                 ddict = None
@@ -503,19 +724,38 @@
                 print(f"    {colors.yellow}-> dictionary{colors.reset}")
                 print_file_diff(ddict, device.get_dict(base))
                 if not options.dry_run:
                     proxy.scheduler.devices.set_dictionary(
                         device.hostname, device.get_dict(base)
                     )
 
+    return 0
+
 
 def handle_import(proxy, options, config):
-    lab = Config({}, {}, {})
+    lab = Config({}, {}, {}, {}, {})
     base = (options.config / ".." / options.config.stem).resolve()
 
+    if config["version"] >= (2023, 3):
+        print(f"{colors.cyan}> groups{colors.reset}")
+        groups = [grp for grp in proxy.auth.groups.list()]
+        for grp in groups:
+            print(f"  {colors.green}* {grp}{colors.reset}")
+            data = proxy.auth.groups.show(grp)
+            lab.groups[grp] = Group.new(
+                name=data["name"], permissions=data["permissions"]
+            )
+
+        print(f"{colors.cyan}> users{colors.reset}")
+        users = [user["username"] for user in proxy.auth.users.list()]
+        for user in users:
+            print(f"  {colors.green}* {user}{colors.reset}")
+            data = proxy.auth.users.show(user)
+            lab.users[user] = User.new(**data)
+
     print(f"{colors.cyan}> device-types{colors.reset}")
     device_types = [dt["name"] for dt in proxy.scheduler.device_types.list(False)]
     for dt in device_types:
         print(f"  {colors.green}* {dt}{colors.reset}")
         data = proxy.scheduler.device_types.show(dt)
         lab.device_types[dt] = DeviceType.new(**data)
```

### Comparing `lavacli-1.6/lavacli/commands/results.py` & `lavacli-1.7/lavacli/commands/results.py`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/lavacli/commands/system.py` & `lavacli-1.7/lavacli/commands/system.py`

 * *Files 5% similar despite different names*

```diff
@@ -26,16 +26,15 @@
 
 
 def configure_parser(parser, version):
     sub = parser.add_subparsers(dest="sub_sub_command", help="Sub commands")
     sub.required = True
 
     # "active"
-    if version >= (2017, 12):
-        sub.add_parser("active", help="activate the system")
+    sub.add_parser("active", help="activate the system")
 
     #  "api"
     sub.add_parser("api", help="print server API version")
 
     # "certificate"
     if version >= (2020, 4):
         sub.add_parser("certificate")
@@ -50,27 +49,26 @@
         help="do a full export, including retired devices",
     )
 
     # "import"
     # sub.add_parser("import", help="import server configuration")
 
     # "maintenance"
-    if version >= (2017, 12):
-        sys_maintenance = sub.add_parser("maintenance", help="maintenance the system")
-        sys_maintenance.add_argument(
-            "--force",
-            default=False,
-            action="store_true",
-            help="force maintenance by canceling jobs",
-        )
-        sys_maintenance.add_argument(
-            "--exclude",
-            default=None,
-            help="comma separated list of workers to keep untouched",
-        )
+    sys_maintenance = sub.add_parser("maintenance", help="maintenance the system")
+    sys_maintenance.add_argument(
+        "--force",
+        default=False,
+        action="store_true",
+        help="force maintenance by canceling jobs",
+    )
+    sys_maintenance.add_argument(
+        "--exclude",
+        default=None,
+        help="comma separated list of workers to keep untouched",
+    )
 
     # "methods"
     sys_methods = sub.add_parser("methods", help="list methods")
     sys_sub = sys_methods.add_subparsers(
         dest="sub_sub_sub_command", help="Sub commands"
     )
     sys_sub.required = True
@@ -128,32 +126,22 @@
         tags.append(tag)
 
     print("Listing workers")
     workers = []
     for worker in proxy.scheduler.workers.list():
         print("* %s" % worker)
         w = proxy.scheduler.workers.show(worker)
-        if config["version"] >= (2017, 12):
-            workers.append(
-                {
-                    "hostname": w["hostname"],
-                    "description": w["description"],
-                    "state": w["state"],
-                    "health": w["health"],
-                }
-            )
-        else:
-            workers.append(
-                {
-                    "hostname": w["hostname"],
-                    "description": w["description"],
-                    "master": w["master"],
-                    "hidden": w["hidden"],
-                }
-            )
+        workers.append(
+            {
+                "hostname": w["hostname"],
+                "description": w["description"],
+                "state": w["state"],
+                "health": w["health"],
+            }
+        )
 
     print("Listing device-types")
     (dest / "device-types").mkdir(mode=0o755)
     device_types = []
     for device_type in proxy.scheduler.device_types.list():
         print("* %s" % device_type["name"])
         dt = proxy.scheduler.device_types.show(device_type["name"])
```

### Comparing `lavacli-1.6/lavacli/commands/tags.py` & `lavacli-1.7/lavacli/commands/tags.py`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/lavacli/commands/utils.py` & `lavacli-1.7/lavacli/commands/utils.py`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/lavacli/commands/workers.py` & `lavacli-1.7/lavacli/commands/workers.py`

 * *Files 4% similar despite different names*

```diff
@@ -126,14 +126,21 @@
         env_dut_set.add_argument("name", type=str, help="worker name")
         env_dut_set.add_argument(
             "env", type=argparse.FileType("r"), help="environment file"
         )
 
     # "list"
     workers_list = sub.add_parser("list", help="list workers")
+    workers_list.add_argument(
+        "--all",
+        "-a",
+        action="store_true",
+        default=False,
+        help="list every workers, including retired",
+    )
     out_format = workers_list.add_mutually_exclusive_group()
     out_format.add_argument(
         "--json",
         dest="output_format",
         default=None,
         action="store_const",
         const="json",
@@ -188,38 +195,21 @@
 
     # "update"
     update_parser = sub.add_parser("update", help="update worker properties")
     update_parser.add_argument("name", type=str, help="worker name")
     update_parser.add_argument(
         "--description", type=str, default=None, help="worker description"
     )
-    if version >= (2017, 12):
-        update_parser.add_argument(
-            "--health",
-            type=str,
-            default=None,
-            choices=["ACTIVE", "MAINTENANCE", "RETIRED"],
-            help="worker health",
-        )
-    else:
-        display = update_parser.add_mutually_exclusive_group()
-        display.add_argument(
-            "--disable",
-            action="store_false",
-            default=None,
-            dest="display",
-            help="disable the worker",
-        )
-        display.add_argument(
-            "--enable",
-            action="store_true",
-            default=None,
-            dest="display",
-            help="enable the worker",
-        )
+    update_parser.add_argument(
+        "--health",
+        type=str,
+        default=None,
+        choices=["ACTIVE", "MAINTENANCE", "RETIRED"],
+        help="worker health",
+    )
     if version >= (2020, 1):
         update_parser.add_argument(
             "--job-limit", type=positive_integer, default=None, help="job limit"
         )
 
 
 def help_string():
@@ -285,16 +275,19 @@
         ret = proxy.scheduler.workers.set_env_dut(options.name, env)
         if not ret:
             print("Unable to store worker dut environment", file=sys.stderr)
             return 1
     return 0
 
 
-def handle_list(proxy, options, _):
-    workers = proxy.scheduler.workers.list()
+def handle_list(proxy, options, config):
+    if config["version"] >= (2023, 3):
+        workers = proxy.scheduler.workers.list(options.all)
+    else:
+        workers = proxy.scheduler.workers.list()
     if options.output_format == "json":
         print(json.dumps(workers))
     elif options.output_format == "yaml":
         safe_yaml.dump(workers, sys.stdout)
     else:
         print("Workers:")
         for worker in workers:
@@ -335,27 +328,18 @@
     elif options.output_format == "yaml":
         if "last_ping" in worker:
             worker["last_ping"] = worker["last_ping"].value
         safe_yaml.dump(worker, sys.stdout)
     else:
         print("hostname    : %s" % worker["hostname"])
         print("description : %s" % worker["description"])
-
-        if config["version"] >= (2017, 12):
-            print("state       : %s" % worker["state"])
-            print("health      : %s" % worker["health"])
-        else:
-            print("master      : %s" % worker["master"])
-            print("hidden      : %s" % worker["hidden"])
-
-        if config["version"] >= (2018, 1):
-            print("devices     : %s" % ", ".join(worker["devices"]))
-            print("last ping   : %s" % worker["last_ping"])
-        else:
-            print("devices     : %d" % worker["devices"])
+        print("state       : %s" % worker["state"])
+        print("health      : %s" % worker["health"])
+        print("devices     : %s" % ", ".join(worker["devices"]))
+        print("last ping   : %s" % worker["last_ping"])
 
         if config["version"] >= (2020, 1):
             print("job limit   : %d" % worker["job_limit"])
 
         if config["version"] >= (2020, 6):
             print("version     : %s" % worker["version"])
 
@@ -365,21 +349,17 @@
 
 
 def handle_update(proxy, options, config):
     if config["version"] >= (2020, 1):
         proxy.scheduler.workers.update(
             options.name, options.description, options.health, options.job_limit
         )
-    elif config["version"] >= (2017, 12):
-        proxy.scheduler.workers.update(
-            options.name, options.description, options.health
-        )
     else:
         proxy.scheduler.workers.update(
-            options.name, options.description, not options.display
+            options.name, options.description, options.health
         )
     return 0
 
 
 def handle(proxy, options, config):
     handlers = {
         "add": handle_add,
```

### Comparing `lavacli-1.6/lavacli/utils.py` & `lavacli-1.7/lavacli/utils.py`

 * *Files 9% similar despite different names*

```diff
@@ -45,14 +45,16 @@
     res = m.groupdict()
     return (int(res["major"]), int(res["minor"]))
 
 
 def exc2str(exc, url):
     if isinstance(exc, xmlrpc.client.ProtocolError):
         msg = exc.errmsg
+        if url is None:
+            return msg
         p = urlparse(url)
         if "@" in p.netloc:
             uri = f"{p.scheme}://<USERNAME>:<TOKEN>@{p.netloc.split('@')[-1]}{p.path}"
         else:
             uri = f"{p.scheme}://{p.netloc}{p.path}"
         return msg.replace(url, uri)
     return str(exc)
```

### Comparing `lavacli-1.6/lavacli.egg-info/PKG-INFO` & `lavacli-1.7/lavacli.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: lavacli
-Version: 1.6
+Version: 1.7
 Summary: LAVA XML-RPC command line interface
 Home-page: https://git.lavasoftware.org/lava/lavacli
 Author: Rémi Duraffort
 Author-email: remi.duraffort@linaro.org
 License: AGPLv3+
 Project-URL: Bug Tracker, https://git.lavasoftware.org/lava/lavacli/issues/
 Project-URL: Documentation, https://docs.lavasoftware.org/lavacli/
@@ -18,9 +18,9 @@
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Topic :: Communications
 Classifier: Topic :: Software Development :: Testing
 Classifier: Topic :: System :: Networking
-Requires-Python: >=3.4
+Requires-Python: >=3.7
 License-File: LICENSE
```

### Comparing `lavacli-1.6/lavacli.egg-info/SOURCES.txt` & `lavacli-1.7/lavacli.egg-info/SOURCES.txt`

 * *Files 3% similar despite different names*

```diff
@@ -23,30 +23,34 @@
 lavacli.egg-info/top_level.txt
 lavacli.egg-info/zip-safe
 lavacli/commands/__init__.py
 lavacli/commands/aliases.py
 lavacli/commands/device_types.py
 lavacli/commands/devices.py
 lavacli/commands/events.py
+lavacli/commands/groups.py
 lavacli/commands/identities.py
 lavacli/commands/jobs.py
 lavacli/commands/lab.py
 lavacli/commands/results.py
 lavacli/commands/system.py
 lavacli/commands/tags.py
+lavacli/commands/users.py
 lavacli/commands/utils.py
 lavacli/commands/workers.py
 share/lavacli.yaml
 tests/__init__.py
 tests/conftest.py
 tests/test_aliases.py
 tests/test_device_types.py
 tests/test_devices.py
 tests/test_events.py
 tests/test_helpers.py
 tests/test_identities.py
 tests/test_jobs.py
+tests/test_lab.py
 tests/test_lavacli.py
 tests/test_results.py
 tests/test_system.py
 tests/test_tags.py
+tests/test_users.py
 tests/test_workers.py
```

### Comparing `lavacli-1.6/setup.py` & `lavacli-1.7/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -34,15 +34,15 @@
     license=metadata["__license__"],
     url=metadata["__url__"],
     project_urls={
         "Bug Tracker": "https://git.lavasoftware.org/lava/lavacli/issues/",
         "Documentation": "https://docs.lavasoftware.org/lavacli/",
         "Source Code": "https://git.lavasoftware.org/lava/lavacli/",
     },
-    python_requires=">=3.4",
+    python_requires=">=3.7",
     classifiers=[
         "Development Status :: 5 - Production/Stable",
         "Environment :: Console",
         "Intended Audience :: Developers",
         "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
         "Operating System :: POSIX :: Linux",
         "Programming Language :: Python :: 3.7",
@@ -52,12 +52,12 @@
         "Programming Language :: Python :: 3 :: Only",
         "Topic :: Communications",
         "Topic :: Software Development :: Testing",
         "Topic :: System :: Networking",
     ],
     packages=["lavacli", "lavacli.commands"],
     entry_points={"console_scripts": ["lavacli = lavacli:main"]},
-    install_requires=["aiohttp", "jinja2", "pyzmq", "requests", "ruamel.yaml"],
-    setup_requires=["pytest-runner"],
-    tests_require=["pytest"],
+    install_requires=["aiohttp", "jinja2", "requests", "ruamel.yaml"],
+    setup_requires=[],
+    tests_require=["pytest", "pytest-runner"],
     zip_safe=True,
 )
```

### Comparing `lavacli-1.6/share/lavacli.yaml` & `lavacli-1.7/share/lavacli.yaml`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/tests/conftest.py` & `lavacli-1.7/tests/conftest.py`

 * *Files 22% similar despite different names*

```diff
@@ -43,12 +43,12 @@
                 self.request.append(attr)
                 return self
 
         return RecordingProxy
 
 
 @pytest.fixture
-def setup(monkeypatch, tmpdir):
-    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmpdir))
-    with (tmpdir / "lavacli.yaml").open("w") as f_conf:
+def setup(monkeypatch, tmp_path):
+    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
+    with (tmp_path / "lavacli.yaml").open("w") as f_conf:
         safe_yaml.dump({"default": {"uri": "https://lava.example.com/RPC2"}}, f_conf)
     monkeypatch.setattr(xmlrpc.client, "ServerProxy", RecordingProxyFactory(None))
```

### Comparing `lavacli-1.6/tests/test_aliases.py` & `lavacli-1.7/tests/test_aliases.py`

 * *Files 0% similar despite different names*

```diff
@@ -56,15 +56,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_aliases_delete(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "aliases", "delete", "new_alias"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -75,30 +75,30 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_aliases_list_empty(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "aliases", "list"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "scheduler.aliases.list", "args": (), "ret": []},
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Aliases:\n"  # nosec
 
 
 def test_aliases_list(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "aliases", "list"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -111,15 +111,15 @@
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "Aliases:\n* first-alias\n* second-alias\n"
     )
 
 
 def test_aliases_list_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "aliases", "list", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -130,15 +130,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == '["first-alias", "second-alias"]\n'  # nosec
 
 
 def test_aliases_list_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "aliases", "list", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -216,15 +216,15 @@
     assert json.loads(capsys.readouterr()[0]) == {  # nosec
         "name": "my_alias",
         "device_types": ["qemu", "kvm"],
     }
 
 
 def test_aliases_show_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "aliases", "show", "kvm", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
```

### Comparing `lavacli-1.6/tests/test_device_types.py` & `lavacli-1.7/tests/test_device_types.py`

 * *Files 4% similar despite different names*

```diff
@@ -16,21 +16,19 @@
 # You should have received a copy of the GNU Affero General Public License
 # along with lavacli.  If not, see <http://www.gnu.org/licenses/>
 
 import json
 import sys
 import xmlrpc.client
 
-import pytest
-
 from lavacli import main
 
 
 def test_dt_add(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "device-types", "add", "mydt"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -41,15 +39,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_add_1(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "device-types",
             "add",
@@ -77,15 +75,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_aliases_add(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "aliases", "add", "mydt", "myalias"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -98,15 +96,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_aliases_delete(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "aliases", "delete", "mydt", "myalias"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -119,15 +117,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_aliases_list(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "aliases", "list", "mydt"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -142,15 +140,15 @@
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "Aliases:\n* first alias\n* second alias\n"
     )
 
 
 def test_dt_aliases_list_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "aliases", "list", "mydt", "--json"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -163,15 +161,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == '["first alias", "second alias"]\n'  # nosec
 
 
 def test_dt_aliases_list_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "aliases", "list", "mydt", "--yaml"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -184,15 +182,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "[first alias, second alias]\n"  # nosec
 
 
 def test_dt_aliases_list_empty(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "aliases", "list", "mydt"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -204,15 +202,15 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Aliases:\n"  # nosec
 
 
-def test_dt_hc_delete(setup, monkeypatch, capsys, tmpdir):
+def test_dt_hc_delete(setup, monkeypatch, capsys, tmp_path):
     version = "2022.4"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "device-types",
@@ -233,62 +231,16 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
-def test_dt_hc_get_before_2018_4(setup, monkeypatch, capsys):
-    version = "2018.2"
-    monkeypatch.setattr(
-        sys, "argv", ["lavacli", "device-types", "health-check", "get", "mydt"]
-    )
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {"request": None, "args": (), "ret": []},
-        ],
-    )
-    with pytest.raises(SystemExit):
-        main()
-    assert (  # nosec
-        capsys.readouterr()[1]
-        == """usage: lavacli device-types [-h] {add,aliases,list,show,template,update} ...
-lavacli device-types: error: argument sub_sub_command: invalid choice: 'health-check' (choose from 'add', 'aliases', 'list', 'show', 'template', 'update')
-"""
-    )
-
-
-def test_dt_hc_set_before_2018_4(setup, monkeypatch, capsys):
-    version = "2018.2"
-    monkeypatch.setattr(
-        sys, "argv", ["lavacli", "device-types", "health-check", "set", "mydt"]
-    )
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {"request": None, "args": (), "ret": []},
-        ],
-    )
-    with pytest.raises(SystemExit):
-        main()
-    assert (  # nosec
-        capsys.readouterr()[1]
-        == """usage: lavacli device-types [-h] {add,aliases,list,show,template,update} ...
-lavacli device-types: error: argument sub_sub_command: invalid choice: 'health-check' (choose from 'add', 'aliases', 'list', 'show', 'template', 'update')
-"""
-    )
-
-
-def test_dt_hc_get_after_2018_4(setup, monkeypatch, capsys):
-    version = "2018.4"
+def test_dt_hc_get_after_2019_1(setup, monkeypatch, capsys):
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "health-check", "get", "mydt"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -300,28 +252,28 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "definition.yaml\n"  # nosec
 
 
-def test_dt_hc_set_after_2018_4(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "hc.yaml").open("w") as f_hc:
+def test_dt_hc_set_after_2019_1(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "hc.yaml").open("w") as f_hc:
         f_hc.write("definition")
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "device-types",
             "health-check",
             "set",
             "mydt",
-            str(tmpdir / "hc.yaml"),
+            str(tmp_path / "hc.yaml"),
         ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -333,15 +285,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_list(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "device-types", "list"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -355,15 +307,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Device-Types:\n* bbb (0)\n* qemu (3)\n"  # nosec
 
 
 def test_dt_list_all(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "device-types", "list", "--all"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -377,15 +329,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Device-Types:\n* bbb (0)\n* qemu (3)\n"  # nosec
 
 
 def test_dt_list_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "device-types", "list", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -402,15 +354,15 @@
     assert json.loads(capsys.readouterr()[0]) == [  # nosec
         {"name": "bbb", "devices": 0, "installed": True, "template": True},
         {"name": "qemu", "devices": 3, "installed": True, "template": True},
     ]
 
 
 def test_dt_list_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "device-types", "list", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -429,15 +381,15 @@
         == """- {devices: 0, installed: true, name: bbb, template: true}
 - {devices: 3, installed: true, name: qemu, template: true}
 """
     )
 
 
 def test_dt_show(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "device-types", "show", "qemu"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -466,15 +418,15 @@
 aliases         : ['kvm']
 devices         : ['qemu01', 'qemu02']
 """
     )
 
 
 def test_dt_show_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "show", "qemu", "--json"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -503,15 +455,15 @@
         "health_disabled": False,
         "aliases": ["kvm"],
         "devices": ["qemu01", "qemu02"],
     }
 
 
 def test_dt_show_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "show", "qemu", "--yaml"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -541,15 +493,15 @@
 health_disabled: false
 name: qemu
 owners_only: false
 """
     )
 
 
-def test_dt_template_delete(setup, monkeypatch, capsys, tmpdir):
+def test_dt_template_delete(setup, monkeypatch, capsys, tmp_path):
     version = "2022.4"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "device-types",
@@ -571,15 +523,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_template_get(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "template", "get", "bbb"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -591,28 +543,28 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "template content\n"  # nosec
 
 
-def test_dt_template_set(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "template.jinja2").open("w") as f_hc:
+def test_dt_template_set(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "template.jinja2").open("w") as f_hc:
         f_hc.write("template definition")
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "device-types",
             "template",
             "set",
             "bbb",
-            str(tmpdir / "template.jinja2"),
+            str(tmp_path / "template.jinja2"),
         ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -624,15 +576,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_update(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "device-types", "update", "bbb", "--description", "hello"],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
@@ -647,15 +599,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_update_1(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "device-types", "update", "bbb", "--hide"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -668,15 +620,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_update_2(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "device-types",
             "update",
@@ -699,15 +651,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_dt_update_3(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "device-types",
             "update",
```

### Comparing `lavacli-1.6/tests/test_devices.py` & `lavacli-1.7/tests/test_devices.py`

 * *Files 9% similar despite different names*

```diff
@@ -20,148 +20,16 @@
 import sys
 import time
 import xmlrpc.client
 
 from lavacli import main
 
 
-def test_devices_add_before_2018_1(setup, monkeypatch, capsys):
-    version = "2017.12"
-    monkeypatch.setattr(
-        sys,
-        "argv",
-        [
-            "lavacli",
-            "devices",
-            "add",
-            "qemu01",
-            "--type",
-            "qemu",
-            "--worker",
-            "worker01",
-        ],
-    )
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.devices.add",
-                "args": (
-                    "qemu01",
-                    "qemu",
-                    "worker01",
-                    None,
-                    None,
-                    True,
-                    None,
-                    None,
-                    None,
-                ),
-                "ret": None,
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert capsys.readouterr()[0] == ""  # nosec
-
-
-def test_devices_add_1_before_2018_1(setup, monkeypatch, capsys):
-    version = "2017.12"
-    monkeypatch.setattr(
-        sys,
-        "argv",
-        [
-            "lavacli",
-            "devices",
-            "add",
-            "qemu01",
-            "--type",
-            "qemu",
-            "--worker",
-            "worker01",
-            "--status",
-            "IDLE",
-            "--health",
-            "PASS",
-        ],
-    )
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.devices.add",
-                "args": (
-                    "qemu01",
-                    "qemu",
-                    "worker01",
-                    None,
-                    None,
-                    True,
-                    "IDLE",
-                    "PASS",
-                    None,
-                ),
-                "ret": None,
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert capsys.readouterr()[0] == ""  # nosec
-
-
-def test_devices_add_2_before_2018_1(setup, monkeypatch, capsys):
-    version = "2017.12"
-    monkeypatch.setattr(
-        sys,
-        "argv",
-        [
-            "lavacli",
-            "devices",
-            "add",
-            "qemu01",
-            "--type",
-            "qemu",
-            "--worker",
-            "worker01",
-            "--user",
-            "self",
-        ],
-    )
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.devices.add",
-                "args": (
-                    "qemu01",
-                    "qemu",
-                    "worker01",
-                    "self",
-                    None,
-                    True,
-                    None,
-                    None,
-                    None,
-                ),
-                "ret": None,
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert capsys.readouterr()[0] == ""  # nosec
-
-
-def test_devices_add_after_2018_1(setup, monkeypatch, capsys):
-    version = "2018.4"
+def test_devices_add(setup, monkeypatch, capsys):
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "devices",
             "add",
@@ -184,16 +52,16 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
-def test_devices_add_1_after_2018_1(setup, monkeypatch, capsys):
-    version = "2018.4"
+def test_devices_add_1(setup, monkeypatch, capsys):
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "devices",
             "add",
@@ -218,16 +86,16 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
-def test_devices_add_2_after_2018_1(setup, monkeypatch, capsys):
-    version = "2018.4"
+def test_devices_add_2(setup, monkeypatch, capsys):
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "devices",
             "add",
@@ -272,15 +140,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_devices_dict_get(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "dict", "get", "qemu01"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -291,15 +159,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "yaml_dict\n"  # nosec
 
 
 def test_devices_dict_get_render_field(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "devices", "dict", "get", "--render", "qemu01", "hello.0.world"],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
@@ -314,15 +182,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "as usual\n"  # nosec
 
 
 def test_devices_dict_get_render_field_out_of_range(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "devices", "dict", "get", "--render", "qemu01", "hello.2.world"],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
@@ -337,15 +205,15 @@
         ],
     )
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "list index out of range (2 vs 2)\n"  # nosec
 
 
 def test_devices_dict_get_render_field_missing(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "devices", "dict", "get", "--render", "qemu01", "hello.0.worl"],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
@@ -362,15 +230,15 @@
     assert main() == 1  # nosec
     assert (  # nosec
         capsys.readouterr()[1] == "Unknown key 'worl' for '{'world': 'as usual'}'\n"
     )
 
 
 def test_devices_dict_get_render_field_missing_1(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "devices", "dict", "get", "--render", "qemu01", "hello.0.world.0"],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
@@ -387,15 +255,15 @@
     assert main() == 1  # nosec
     assert (  # nosec
         capsys.readouterr()[1] == "Unable to lookup inside 'as usual' for '0'\n"
     )
 
 
 def test_devices_dict_get_render_field_missing_2(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "devices",
             "dict",
@@ -420,15 +288,15 @@
     assert main() == 1  # nosec
     assert (  # nosec
         capsys.readouterr()[1] == "Unable to lookup inside 'as usual' for 'missing'\n"
     )
 
 
 def test_devices_dict_get_jinja2_field(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "devices", "dict", "get", "qemu01", "hello"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -441,15 +309,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "bla\n"  # nosec
 
 
 def test_devices_dict_get_jinja2_field_2(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "devices", "dict", "get", "qemu01", "hello.0.bla"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -462,15 +330,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "something\n"  # nosec
 
 
 def test_devices_dict_get_jinja2_field_missing(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "devices", "dict", "get", "qemu01", "world"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -482,22 +350,22 @@
             },
         ],
     )
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Unknown field 'world'\n"  # nosec
 
 
-def test_devices_dict_set(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "dict.jinja2").open("w") as f_conf:
+def test_devices_dict_set(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "dict.jinja2").open("w") as f_conf:
         f_conf.write("{% set exclusive = True %}")
     monkeypatch.setattr(
         sys,
         "argv",
-        ["lavacli", "devices", "dict", "set", "qemu01", str(tmpdir / "dict.jinja2")],
+        ["lavacli", "devices", "dict", "set", "qemu01", str(tmp_path / "dict.jinja2")],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -507,22 +375,22 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
-def test_devices_dict_set_error(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "dict.jinja2").open("w") as f_conf:
+def test_devices_dict_set_error(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "dict.jinja2").open("w") as f_conf:
         f_conf.write("{% set exclusive = True %}")
     monkeypatch.setattr(
         sys,
         "argv",
-        ["lavacli", "devices", "dict", "set", "qemu01", str(tmpdir / "dict.jinja2")],
+        ["lavacli", "devices", "dict", "set", "qemu01", str(tmp_path / "dict.jinja2")],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -533,15 +401,15 @@
         ],
     )
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Unable to set the configuration\n"  # nosec
 
 
 def test_devices_list(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "list"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -584,15 +452,15 @@
 * qemu02 (qemu): Running,Good
 * bbb01 (bbb): Idle,Maintenance
 """
     )
 
 
 def test_devices_list_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "list", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -653,15 +521,15 @@
             "current_job": None,
             "pipeline": True,
         },
     ]
 
 
 def test_devices_list_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "list", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -705,64 +573,16 @@
   type: qemu}
 - {current_job: null, health: Maintenance, hostname: bbb01, pipeline: true, state: Idle,
   type: bbb}
 """
     )
 
 
-def test_devices_list_before_2018_1(setup, monkeypatch, capsys, tmpdir):
-    version = "2017.12"
-    monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "list"])
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.devices.list",
-                "args": (False,),
-                "ret": [
-                    {
-                        "hostname": "qemu01",
-                        "type": "qemu",
-                        "status": "Idle",
-                        "current_job": None,
-                        "pipeline": True,
-                    },
-                    {
-                        "hostname": "qemu02",
-                        "type": "qemu",
-                        "status": "Running",
-                        "current_job": 1234,
-                        "pipeline": True,
-                    },
-                    {
-                        "hostname": "bbb01",
-                        "type": "bbb",
-                        "status": "Maintenance",
-                        "current_job": None,
-                        "pipeline": True,
-                    },
-                ],
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert (  # nosec
-        capsys.readouterr()[0]
-        == """Devices:
-* qemu01 (qemu): Idle
-* qemu02 (qemu): Running
-* bbb01 (bbb): Maintenance
-"""
-    )
-
-
 def test_devices_maintenance(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 5  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "maintenance", "qemu01"])
@@ -841,15 +661,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "-> waiting for job 1234\n--> waiting\n"  # nosec
 
 
 def test_devices_maintenance_force(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "devices", "maintenance", "qemu01", "--force"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
@@ -905,15 +725,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "-> waiting for job 1234\n--> canceling\n"  # nosec
 
 
 def test_devices_maintenance_without_current_job(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "devices", "maintenance", "qemu01", "--force"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -946,15 +766,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_devices_show(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "show", "qemu01"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -997,15 +817,15 @@
 current job : None
 tags        : ['a', 'b']
 """
     )
 
 
 def test_devices_show_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "show", "qemu01", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -1046,15 +866,15 @@
         "group": "group01",
         "current_job": None,
         "tags": ["a", "b"],
     }
 
 
 def test_devices_show_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "show", "qemu01", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -1096,65 +916,16 @@
 tags: [a, b]
 user: null
 worker: worker01
 """
     )
 
 
-def test_devices_show_before_2018_1(setup, monkeypatch, capsys):
-    version = "2017.12"
-    monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "show", "qemu01"])
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.devices.show",
-                "args": ("qemu01",),
-                "ret": {
-                    "hostname": "qemu01",
-                    "device_type": "qemu",
-                    "status": "Idle",
-                    "health_job": True,
-                    "description": None,
-                    "public": True,
-                    "pipeline": True,
-                    "has_device_dict": True,
-                    "worker": "worker01",
-                    "user": None,
-                    "group": "group01",
-                    "current_job": None,
-                    "tags": ["a", "b"],
-                },
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert (  # nosec
-        capsys.readouterr()[0]
-        == """name        : qemu01
-device-type : qemu
-status      : Idle
-user        : None
-group       : group01
-health job  : True
-description : None
-public      : True
-pipeline    : True
-device-dict : True
-worker      : worker01
-current job : None
-tags        : ['a', 'b']
-"""
-    )
-
-
 def test_devices_tags_add(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "devices", "tags", "add", "qemu01", "hdd"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -1167,15 +938,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_devices_tags_delete(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "devices", "tags", "delete", "qemu01", "hdd"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -1188,15 +959,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_devices_tags_list(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "devices", "tags", "list", "qemu01"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -1207,15 +978,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Tags:\n* hdd\n* virt\n"  # nosec
 
 
 def test_devices_tags_list_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "devices", "tags", "list", "--json", "qemu01"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -1228,15 +999,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == '["hdd", "virt"]\n'  # nosec
 
 
 def test_devices_tags_list_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "devices", "tags", "list", "--yaml", "qemu01"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -1249,15 +1020,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "[hdd, virt]\n"  # nosec
 
 
 def test_devices_update(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "devices",
             "update",
@@ -1278,50 +1049,7 @@
                 "args": ("qemu01", "worker01", None, None, None, "UNKNOWN", None),
                 "ret": None,
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
-
-
-def test_devices_update_before_2018_1(setup, monkeypatch, capsys):
-    version = "2017.12"
-    monkeypatch.setattr(
-        sys,
-        "argv",
-        [
-            "lavacli",
-            "devices",
-            "update",
-            "qemu01",
-            "--worker",
-            "worker01",
-            "--status",
-            "IDLE",
-            "--health",
-            "UNKNOWN",
-        ],
-    )
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.devices.update",
-                "args": (
-                    "qemu01",
-                    "worker01",
-                    None,
-                    None,
-                    None,
-                    "IDLE",
-                    "UNKNOWN",
-                    None,
-                ),
-                "ret": None,
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert capsys.readouterr()[0] == ""  # nosec
```

### Comparing `lavacli-1.6/tests/test_events.py` & `lavacli-1.7/tests/test_events.py`

 * *Files 14% similar despite different names*

```diff
@@ -42,16 +42,16 @@
 
 class DummyContext:
     def socket(self, sock_type):
         assert sock_type == zmq.SUB  # nosec
         return DummySocket()
 
 
-def test_events_listen(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_listen(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "events", "listen"])
     monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
     DummySocket.data = [
         (
             "v.l.o.device",
             "uuid",
@@ -140,87 +140,16 @@
     )
     assert (  # nosec
         readouterr[1]
         == "Invalid message: invalid message\nUnknown error: pop from empty list\n"
     )
 
 
-def test_events_listen_before_2018_1(setup, monkeypatch, capsys, tmpdir):
-    version = "2017.12"
-    monkeypatch.setattr(sys, "argv", ["lavacli", "events", "listen"])
-    monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
-    monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
-    DummySocket.data = [
-        (
-            "v.l.o.device",
-            "uuid",
-            "2018-01-29",
-            "lava-health",
-            json.dumps({"device": "bbb-01", "device_type": "bbb", "status": "Idle"}),
-        ),
-        (
-            "v.l.o.device",
-            "uuid",
-            "2018-01-29",
-            "lava-health",
-            json.dumps(
-                {
-                    "device": "bbb-01",
-                    "device_type": "bbb",
-                    "status": "Running",
-                    "job": "1234",
-                }
-            ),
-        ),
-        (
-            "v.l.o.testjob",
-            "uuid",
-            "2018-01-30",
-            "lava-health",
-            json.dumps(
-                {
-                    "job": "1234",
-                    "device": "bbb-01",
-                    "status": "Running",
-                    "description": "a nice job",
-                }
-            ),
-        ),
-        ("invalid message"),
-    ]
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.get_publisher_event_socket",
-                "args": (),
-                "ret": "tcp://*:5500",
-            },
-        ],
-    )
-    assert main() == 1  # nosec
-    readouterr = capsys.readouterr()
-    assert (  # nosec
-        readouterr[0]
-        == """Listening to tcp://lava.example.com:5500
-\033[1;30m2018-01-29\033[0m \033[1;37mv.l.o.device\033[0m \033[32mlava-health\033[0m - [bbb-01] <bbb> Idle
-\033[1;30m2018-01-29\033[0m \033[1;37mv.l.o.device\033[0m \033[32mlava-health\033[0m - [bbb-01] <bbb> Running for 1234
-\033[1;30m2018-01-30\033[0m \033[1;37mv.l.o.testjob\033[0m \033[32mlava-health\033[0m - [1234] <bbb-01> Running (a nice job)
-"""
-    )
-    assert (  # nosec
-        readouterr[1]
-        == "Invalid message: invalid message\nUnknown error: pop from empty list\n"
-    )
-
-
-def test_events_listen_config(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_listen_config(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "--uri",
             "https://admin:12345@localhost:456/RPC2",
@@ -245,37 +174,37 @@
     )
     assert main() == 1  # nosec
     readouterr = capsys.readouterr()
     assert readouterr[0] == "Listening to tcp://localhost:5501\n"  # nosec
     assert readouterr[1] == "Unknown error: pop from empty list\n"  # nosec
 
 
-def test_events_listen_config_2(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_listen_config_2(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "events", "listen"])
     monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
     monkeypatch.setattr(DummySocket, "url", "tcp://localhost:789")
-    with (tmpdir / "lavacli.yaml").open("w") as f_conf:
+    with (tmp_path / "lavacli.yaml").open("w") as f_conf:
         f_conf.write(
             "default:\n  username: admin\n  token: 12345\n  uri: https://localhost:456/RPC2\n  events:\n    uri: tcp://localhost:789\n"
         )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [{"request": "system.version", "args": (), "ret": version}],
     )
     assert main() == 1  # nosec
     readouterr = capsys.readouterr()
     assert readouterr[0] == "Listening to tcp://localhost:789\n"  # nosec
     assert readouterr[1] == "Unknown error: pop from empty list\n"  # nosec
 
 
-def test_events_listen_filter(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_listen_filter(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "events", "listen", "--filter", "device"]
     )
     monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
     DummySocket.data = [
         (
@@ -363,16 +292,16 @@
     )
     assert (  # nosec
         readouterr[1]
         == "Invalid message: invalid message\nUnknown error: pop from empty list\n"
     )
 
 
-def test_events_listen_filter_2(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_listen_filter_2(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "events", "listen", "--filter", "device", "--filter", "worker"],
     )
     monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
@@ -463,16 +392,16 @@
     )
     assert (  # nosec
         readouterr[1]
         == "Invalid message: invalid message\nUnknown error: pop from empty list\n"
     )
 
 
-def test_events_wait_device(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_wait_device(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "events", "wait", "device", "bbb-02"])
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
     DummySocket.data = [
         (
             "v.l.o.device",
             "uuid",
             "2018-01-29",
@@ -532,16 +461,16 @@
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "Listening to tcp://lava.example.com:5500\n"
     )
     assert DummySocket.data == []  # nosec
 
 
-def test_events_wait_device_state(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_wait_device_state(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "events", "wait", "device", "bbb-01", "--state", "RUNNING"],
     )
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
     DummySocket.data = [
@@ -605,16 +534,16 @@
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "Listening to tcp://lava.example.com:5500\n"
     )
     assert DummySocket.data == []  # nosec
 
 
-def test_events_wait_device_health(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_wait_device_health(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "events", "wait", "device", "bbb-01", "--health", "MAINTENANCE"],
     )
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
     DummySocket.data = [
@@ -662,16 +591,16 @@
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "Listening to tcp://lava.example.com:5500\n"
     )
     assert DummySocket.data == []  # nosec
 
 
-def test_events_wait_job(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_wait_job(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "events", "wait", "job", "1234"])
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
     DummySocket.data = [
         (
             "v.l.o.device",
             "uuid",
             "2018-01-29",
@@ -731,16 +660,16 @@
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "Listening to tcp://lava.example.com:5500\n"
     )
     assert DummySocket.data == []  # nosec
 
 
-def test_events_wait_worker(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_wait_worker(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "events", "wait", "worker", "worker-01"]
     )
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
     DummySocket.data = [
         (
             "v.l.o.device",
@@ -820,16 +749,16 @@
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "Listening to tcp://lava.example.com:5500\n"
     )
     assert DummySocket.data == []  # nosec
 
 
-def test_events_wait_worker_invalid_message(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_events_wait_worker_invalid_message(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "events", "wait", "worker", "worker-01"]
     )
     monkeypatch.setattr(zmq, "Context", lambda: DummyContext())
     DummySocket.data = [
         (
             "v.l.o.device",
```

### Comparing `lavacli-1.6/tests/test_helpers.py` & `lavacli-1.7/tests/test_helpers.py`

 * *Files 3% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 
 from lavacli.utils import VERSION_LATEST, parse_version
 
 
 def test_parse_version():
     assert parse_version("2018.5.post1-2~bpo9+1.1debian9.1") == (2018, 5)  # nosec
     assert parse_version("2018.5.post1-1+stretch") == (2018, 5)  # nosec
-    assert parse_version("2018.4-1-1") == (2018, 4)  # nosec
-    assert parse_version("2018.4.post2-1+stretch") == (2018, 4)  # nosec
+    assert parse_version("2019.1-1-1") == (2019, 1)  # nosec
+    assert parse_version("2019.1.post2-1+stretch") == (2019, 1)  # nosec
     assert parse_version("2019.01.post2-1+stretch") == (2019, 1)  # nosec
 
 
 def test_parse_version_errors():
     assert parse_version(1) == VERSION_LATEST  # nosec
     assert parse_version("201812") == VERSION_LATEST  # nosec
```

### Comparing `lavacli-1.6/tests/test_identities.py` & `lavacli-1.7/tests/test_identities.py`

 * *Files 18% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 
 import sys
 
 from lavacli import main
 from lavacli.utils import safe_yaml
 
 
-def test_identities_add(setup, monkeypatch, capsys, tmpdir):
+def test_identities_add(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "identities",
             "add",
@@ -34,22 +34,22 @@
             "--uri",
             "https://validation.linaro.org/RPC2",
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
-    with (tmpdir / "lavacli.yaml").open() as f_in:
+    with (tmp_path / "lavacli.yaml").open() as f_in:
         data = safe_yaml.load(f_in)
         assert set(data.keys()) == {"default", "v.l.o"}  # nosec
         assert data["default"] == {"uri": "https://lava.example.com/RPC2"}  # nosec
         assert data["v.l.o"] == {"uri": "https://validation.linaro.org/RPC2"}  # nosec
 
 
-def test_identities_add_1(setup, monkeypatch, capsys, tmpdir):
+def test_identities_add_1(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "identities",
             "add",
@@ -63,136 +63,136 @@
             "--token",
             "12345",
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
-    with (tmpdir / "lavacli.yaml").open() as f_in:
+    with (tmp_path / "lavacli.yaml").open() as f_in:
         data = safe_yaml.load(f_in)
         assert set(data.keys()) == {"default", "v.l.o"}  # nosec
         assert data["default"] == {"uri": "https://lava.example.com/RPC2"}  # nosec
         assert data["v.l.o"] == {  # nosec
             "uri": "https://validation.linaro.org/RPC2",
             "proxy": "http://proxy:3128",
             "username": "admin",
             "token": "12345",
         }
 
 
-def test_identities_add_empty_config(setup, monkeypatch, capsys, tmpdir):
+def test_identities_add_empty_config(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "identities",
             "add",
             "v.l.o",
             "--uri",
             "https://validation.linaro.org/RPC2",
         ],
     )
-    (tmpdir / "lavacli.yaml").remove()
+    (tmp_path / "lavacli.yaml").unlink()
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
-    with (tmpdir / "lavacli.yaml").open() as f_in:
+    with (tmp_path / "lavacli.yaml").open() as f_in:
         data = safe_yaml.load(f_in)
         assert set(data.keys()) == {"v.l.o"}  # nosec
         assert data["v.l.o"] == {"uri": "https://validation.linaro.org/RPC2"}  # nosec
 
 
-def test_identities_delete(setup, monkeypatch, capsys, tmpdir):
+def test_identities_delete(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "delete", "v.l.o"])
-    with (tmpdir / "lavacli.yaml").open("w") as f_conf:
+    with (tmp_path / "lavacli.yaml").open("w") as f_conf:
         f_conf.write(
             "default:\n  uri: https://lava.example.com/RPC2\nv.l.o:\n  uri: https://validation.linaro.org/RPC"
         )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
-    with (tmpdir / "lavacli.yaml").open() as f_in:
+    with (tmp_path / "lavacli.yaml").open() as f_in:
         data = safe_yaml.load(f_in)
         assert list(data.keys()) == ["default"]  # nosec
         assert data["default"] == {"uri": "https://lava.example.com/RPC2"}  # nosec
 
 
-def test_identities_delete_empty_config(setup, monkeypatch, capsys, tmpdir):
+def test_identities_delete_empty_config(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "delete", "v.l.o"])
-    (tmpdir / "lavacli.yaml").remove()
+    (tmp_path / "lavacli.yaml").unlink()
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Unknown identity 'v.l.o'\n"  # nosec
-    assert not (tmpdir / "lavacli.yaml").exists()  # nosec
+    assert not (tmp_path / "lavacli.yaml").exists()  # nosec
 
 
-def test_identities_delete_missing_key(setup, monkeypatch, capsys, tmpdir):
+def test_identities_delete_missing_key(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "delete", "v.l.o"])
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Unknown identity 'v.l.o'\n"  # nosec
 
-    with (tmpdir / "lavacli.yaml").open() as f_in:
+    with (tmp_path / "lavacli.yaml").open() as f_in:
         data = safe_yaml.load(f_in)
         assert list(data.keys()) == ["default"]  # nosec
         assert data["default"] == {"uri": "https://lava.example.com/RPC2"}  # nosec
 
 
-def test_identities_list(setup, monkeypatch, capsys, tmpdir):
+def test_identities_list(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "list"])
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Identities:\n* default\n"  # nosec
 
-    with (tmpdir / "lavacli.yaml").open() as f_in:
+    with (tmp_path / "lavacli.yaml").open() as f_in:
         data = safe_yaml.load(f_in)
         assert list(data.keys()) == ["default"]  # nosec
         assert data["default"] == {"uri": "https://lava.example.com/RPC2"}  # nosec
 
 
-def test_identities_list_1(setup, monkeypatch, capsys, tmpdir):
+def test_identities_list_1(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "list"])
-    with (tmpdir / "lavacli.yaml").open("w") as f_conf:
+    with (tmp_path / "lavacli.yaml").open("w") as f_conf:
         f_conf.write(
             "default:\n  uri: https://lava.example.com/RPC2\nv.l.o:\n  uri: https://validation.linaro.org/RPC2"
         )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Identities:\n* default\n* v.l.o\n"  # nosec
 
-    with (tmpdir / "lavacli.yaml").open() as f_in:
+    with (tmp_path / "lavacli.yaml").open() as f_in:
         data = safe_yaml.load(f_in)
         assert set(data.keys()) == {"default", "v.l.o"}  # nosec
         assert data["default"] == {"uri": "https://lava.example.com/RPC2"}  # nosec
         assert data["v.l.o"] == {"uri": "https://validation.linaro.org/RPC2"}  # nosec
 
 
-def test_identities_list_2(setup, monkeypatch, capsys, tmpdir):
+def test_identities_list_2(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "list"])
-    (tmpdir / "lavacli.yaml").remove()
+    (tmp_path / "lavacli.yaml").unlink()
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Identities:\n"  # nosec
-    assert not (tmpdir / "lavacli.yaml").exists()  # nosec
+    assert not (tmp_path / "lavacli.yaml").exists()  # nosec
 
 
-def test_identities_show(setup, monkeypatch, capsys, tmpdir):
+def test_identities_show(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "show", "default"])
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "uri: https://lava.example.com/RPC2\n"  # nosec
 
 
-def test_identities_show_missing(setup, monkeypatch, capsys, tmpdir):
+def test_identities_show_missing(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "show", "missing"])
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Unknown identity 'missing'\n"  # nosec
 
 
-def test_identities_show_no_config(setup, monkeypatch, capsys, tmpdir):
+def test_identities_show_no_config(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "show", "default"])
-    (tmpdir / "lavacli.yaml").remove()
+    (tmp_path / "lavacli.yaml").unlink()
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Unknown identity 'default'\n"  # nosec
 
 
-def test_identities_show_invalid_config(setup, monkeypatch, capsys, tmpdir):
+def test_identities_show_invalid_config(setup, monkeypatch, capsys, tmp_path):
     monkeypatch.setattr(sys, "argv", ["lavacli", "identities", "show", "default"])
-    with (tmpdir / "lavacli.yaml").open("w") as f_conf:
+    with (tmp_path / "lavacli.yaml").open("w") as f_conf:
         f_conf.write("hello")
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Invalid configuration file\n"  # nosec
```

### Comparing `lavacli-1.6/tests/test_jobs.py` & `lavacli-1.7/tests/test_jobs.py`

 * *Files 3% similar despite different names*

```diff
@@ -22,32 +22,32 @@
 import xmlrpc.client
 
 from lavacli import main
 from lavacli.utils import safe_yaml
 
 
 def test_jobs_cancel(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "cancel", "1234"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "scheduler.jobs.cancel", "args": ("1234",), "ret": None},
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
-def test_jobs_config(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_jobs_config(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     monkeypatch.setattr(
-        sys, "argv", ["lavacli", "jobs", "config", "1234", "--dest", str(tmpdir)]
+        sys, "argv", ["lavacli", "jobs", "config", "1234", "--dest", str(tmp_path)]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -55,28 +55,28 @@
                 "args": ("1234",),
                 "ret": ["definition", "device", "dispatcher", "env", "env.dut"],
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
-    with (tmpdir / "definition.yaml").open() as f_in:
+    with (tmp_path / "definition.yaml").open() as f_in:
         assert f_in.read() == "definition"  # nosec
-    with (tmpdir / "device.yaml").open() as f_in:
+    with (tmp_path / "device.yaml").open() as f_in:
         assert f_in.read() == "device"  # nosec
-    with (tmpdir / "dispatcher.yaml").open() as f_in:
+    with (tmp_path / "dispatcher.yaml").open() as f_in:
         assert f_in.read() == "dispatcher"  # nosec
-    with (tmpdir / "env.yaml").open() as f_in:
+    with (tmp_path / "env.yaml").open() as f_in:
         assert f_in.read() == "env"  # nosec
-    with (tmpdir / "env.dut.yaml").open() as f_in:
+    with (tmp_path / "env.dut.yaml").open() as f_in:
         assert f_in.read() == "env.dut"  # nosec
 
 
 def test_jobs_definition(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "definition", "1234"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -86,189 +86,16 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "definition\n"  # nosec
 
 
-def test_jobs_list_before_2018_1(setup, monkeypatch, capsys):
-    version = "2017.12"
-    monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "list"])
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.jobs.list",
-                "args": (0, 25),
-                "ret": [
-                    {
-                        "id": "16",
-                        "description": "hello",
-                        "device_type": "bbb",
-                        "status": "Complete",
-                        "submitter": "lava",
-                    },
-                    {
-                        "id": "15",
-                        "description": "world",
-                        "device_type": "qemu",
-                        "status": "Incomplete",
-                        "submitter": "lab",
-                    },
-                    {
-                        "id": "14",
-                        "description": "health",
-                        "device_type": "docker",
-                        "status": "Canceled",
-                        "submitter": "lava-health",
-                    },
-                    {
-                        "id": "12",
-                        "description": "something",
-                        "device_type": "",
-                        "status": "Running",
-                        "submitter": "admin",
-                    },
-                ],
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert (  # nosec
-        capsys.readouterr()[0]
-        == """Jobs (from 1 to 25):
-* 16: Complete [lava] (hello) - bbb
-* 15: Incomplete [lab] (world) - qemu
-* 14: Canceled [lava-health] (health) - docker
-* 12: Running [admin] (something) - \n"""
-    )
-
-
-def test_jobs_list_before_2018_4(setup, monkeypatch, capsys):
-    version = "2018.2"
-    monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "list"])
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.jobs.list",
-                "args": (0, 25),
-                "ret": [
-                    {
-                        "id": "16",
-                        "description": "hello",
-                        "device_type": "bbb",
-                        "health": "Complete",
-                        "state": "Runished",
-                        "submitter": "lava",
-                    },
-                    {
-                        "id": "15",
-                        "description": "world",
-                        "device_type": "qemu",
-                        "health": "Incomplete",
-                        "state": "Finished",
-                        "submitter": "lab",
-                    },
-                    {
-                        "id": "14",
-                        "description": "health",
-                        "device_type": "docker",
-                        "health": "Canceled",
-                        "state": "Finished",
-                        "submitter": "lava-health",
-                    },
-                    {
-                        "id": "12",
-                        "description": "something",
-                        "device_type": "",
-                        "health": "Unknown",
-                        "state": "Running",
-                        "submitter": "admin",
-                    },
-                ],
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert (  # nosec
-        capsys.readouterr()[0]
-        == """Jobs (from 1 to 25):
-* 16: Runished,Complete [lava] (hello) - bbb
-* 15: Finished,Incomplete [lab] (world) - qemu
-* 14: Finished,Canceled [lava-health] (health) - docker
-* 12: Running,Unknown [admin] (something) - \n"""
-    )
-
-
-def test_jobs_list_before_2018_10(setup, monkeypatch, capsys):
-    version = "2018.4"
-    monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "list"])
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.jobs.list",
-                "args": (None, None, 0, 25),
-                "ret": [
-                    {
-                        "id": "16",
-                        "description": "hello",
-                        "device_type": "bbb",
-                        "health": "Complete",
-                        "state": "Rinished",
-                        "submitter": "lava",
-                    },
-                    {
-                        "id": "15",
-                        "description": "world",
-                        "device_type": "qemu",
-                        "health": "Incomplete",
-                        "state": "Finished",
-                        "submitter": "lab",
-                    },
-                    {
-                        "id": "14",
-                        "description": "health",
-                        "device_type": "docker",
-                        "health": "Canceled",
-                        "state": "Finished",
-                        "submitter": "lava-health",
-                    },
-                    {
-                        "id": "12",
-                        "description": "something",
-                        "device_type": "",
-                        "health": "Unknown",
-                        "state": "Running",
-                        "submitter": "admin",
-                    },
-                ],
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert (  # nosec
-        capsys.readouterr()[0]
-        == """Jobs (from 1 to 25):
-* 16: Rinished,Complete [lava] (hello) - bbb
-* 15: Finished,Incomplete [lab] (world) - qemu
-* 14: Finished,Canceled [lava-health] (health) - docker
-* 12: Running,Unknown [admin] (something) - \n"""
-    )
-
-
 def test_jobs_list(setup, monkeypatch, capsys):
-    version = "2018.10"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "list"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -301,15 +128,15 @@
         == """Jobs (from 1 to 25):
 * 16: Rinished,Complete [lava] (hello) - bbb
 * 12: Running,Unknown [admin] (something) - \n"""
     )
 
 
 def test_jobs_list_since_verbose(setup, monkeypatch, capsys):
-    version = "2018.10"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "jobs", "list", "--verbose", "--since", "5"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -354,15 +181,15 @@
         == """Jobs (from 1 to 25):
 * 16: Rinished,Complete [lava] (hello) - bbb bbb-01 <12> <13>
 * 12: Running,Unknown [admin] (something) - docker docker-01 <45> <46> something is wrong: job error\n"""
     )
 
 
 def test_jobs_list_json(setup, monkeypatch, capsys):
-    version = "2018.10"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "list", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -439,15 +266,15 @@
             "state": "Running",
             "submitter": "admin",
         },
     ]
 
 
 def test_jobs_list_yaml(setup, monkeypatch, capsys):
-    version = "2018.10"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "list", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -502,15 +329,15 @@
 - {description: something, device_type: '', health: Unknown, id: '12', state: Running,
   submitter: admin}
 """
     )
 
 
 def test_jobs_list_filtering(setup, monkeypatch, capsys):
-    version = "2018.10"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "list", "--state", "RUNNING"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -521,15 +348,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Jobs (from 1 to 25):\n"  # nosec
 
 
 def test_jobs_list_filtering2(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "jobs",
             "list",
@@ -544,49 +371,49 @@
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
                 "request": "scheduler.jobs.list",
-                "args": (None, "CANCELED", 45, 56),
+                "args": (None, "CANCELED", 45, 56, 0, False),
                 "ret": [],
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Jobs (from 46 to 101):\n"  # nosec
 
 
 # TODO: test with 2018.6 and also --start/--end
 def test_jobs_logs(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 5  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "logs", "1234"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 0),
+                "args": ("1234", 0, None),
                 "ret": (
                     False,
-                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2018.4-1"}',
+                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2019.1-1"}',
                 ),
             },
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 1),
+                "args": ("1234", 1, None),
                 "ret": (
                     True,
                     """- {"dt": "2018-04-23T12:07:02.572789", "lvl": "results", "msg": {"case": "validate", "definition": "lava", "result": "pass"}}
 - {"dt": "2018-04-23T12:07:02.573414", "lvl": "debug", "msg": "start: 1.1 download-retry (timeout 00:02:00) [common]"}""",
                 ),
             },
             {
@@ -612,30 +439,30 @@
             },
         ],
     )
     assert main() == 0  # nosec
     lines = capsys.readouterr()[0].split("\n")
     assert (  # nosec
         lines[0]
-        == "2018-04-23T12:07:02 lava-dispatcher, installed at version: 2018.4-1"
+        == "2018-04-23T12:07:02 lava-dispatcher, installed at version: 2019.1-1"
     )
     assert lines[1][:20] == "2018-04-23T12:07:02 "  # nosec
     assert safe_yaml.load(lines[1][20:]) == {  # nosec
         "case": "validate",
         "definition": "lava",
         "result": "pass",
     }
     assert (  # nosec
         lines[2]
         == "2018-04-23T12:07:02 start: 1.1 download-retry (timeout 00:02:00) [common]"
     )
 
 
 def test_jobs_logs_failure_comment_and_polling(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 10  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(
@@ -644,23 +471,23 @@
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 0),
+                "args": ("1234", 0, None),
                 "ret": (
                     False,
-                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2018.4-1"}',
+                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2019.1-1"}',
                 ),
             },
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 1),
+                "args": ("1234", 1, None),
                 "ret": (
                     True,
                     """- {"dt": "2018-04-23T12:07:02.572789", "lvl": "results", "msg": {"case": "validate", "definition": "lava", "result": "pass"}}
 - {"dt": "2018-04-23T12:07:02.573414", "lvl": "debug", "msg": "start: 1.1 download-retry (timeout 00:02:00) [common]"}""",
                 ),
             },
             {
@@ -686,15 +513,15 @@
             },
         ],
     )
     assert main() == 0  # nosec
     lines = capsys.readouterr()[0].split("\n")
     assert (  # nosec
         lines[0]
-        == "2018-04-23T12:07:02 lava-dispatcher, installed at version: 2018.4-1"
+        == "2018-04-23T12:07:02 lava-dispatcher, installed at version: 2019.1-1"
     )
     assert lines[1][:20] == "2018-04-23T12:07:02 "  # nosec
     assert safe_yaml.load(lines[1][20:]) == {  # nosec
         "case": "validate",
         "definition": "lava",
         "result": "pass",
     }
@@ -704,15 +531,15 @@
     )
     assert lines[3].endswith(  # nosec
         "lavacli] Failure comment: A small issue was found"
     )
 
 
 def test_jobs_logs_filtering(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 5  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(
@@ -721,23 +548,23 @@
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 0),
+                "args": ("1234", 0, None),
                 "ret": (
                     False,
-                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2018.4-1"}',
+                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2019.1-1"}',
                 ),
             },
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 1),
+                "args": ("1234", 1, None),
                 "ret": (
                     True,
                     """- {"dt": "2018-04-23T12:07:02.572789", "lvl": "results", "msg": {"case": "validate", "definition": "lava", "result": "pass"}}
 - {"dt": "2018-04-23T12:07:02.573414", "lvl": "debug", "msg": "start: 1.1 download-retry (timeout 00:02:00) [common]"}""",
                 ),
             },
             {
@@ -762,45 +589,45 @@
                 },
             },
         ],
     )
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0]
-        == """2018-04-23T12:07:02 lava-dispatcher, installed at version: 2018.4-1
+        == """2018-04-23T12:07:02 lava-dispatcher, installed at version: 2019.1-1
 2018-04-23T12:07:02 start: 1.1 download-retry (timeout 00:02:00) [common]
 """
     )
 
 
 def test_jobs_logs_raw(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 5  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "logs", "1234", "--raw"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 0),
+                "args": ("1234", 0, None),
                 "ret": (
                     False,
-                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2018.4-1"}',
+                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2019.1-1"}',
                 ),
             },
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 1),
+                "args": ("1234", 1, None),
                 "ret": (
                     True,
                     """- {"dt": "2018-04-23T12:07:02.572789", "lvl": "results", "msg": {"case": "validate", "definition": "lava", "result": "pass"}}
 - {"dt": "2018-04-23T12:07:02.573414", "lvl": "debug", "msg": "start: 1.1 download-retry (timeout 00:02:00) [common]"}""",
                 ),
             },
             {
@@ -825,23 +652,23 @@
                 },
             },
         ],
     )
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0]
-        == """- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2018.4-1"}
+        == """- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2019.1-1"}
 - {"dt": "2018-04-23T12:07:02.572789", "lvl": "results", "msg": {"case": "validate", "definition": "lava", "result": "pass"}}
 - {"dt": "2018-04-23T12:07:02.573414", "lvl": "debug", "msg": "start: 1.1 download-retry (timeout 00:02:00) [common]"}
 """
     )
 
 
 def test_jobs_logs_raw_filter(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 5  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(
@@ -852,23 +679,23 @@
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 0),
+                "args": ("1234", 0, None),
                 "ret": (
                     False,
-                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2018.4-1"}',
+                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2019.1-1"}',
                 ),
             },
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 1),
+                "args": ("1234", 1, None),
                 "ret": (
                     True,
                     """- {"dt": "2018-04-23T12:07:02.572789", "lvl": "results", "msg": {"case": "validate", "definition": "lava", "result": "pass"}}
 - {"dt": "2018-04-23T12:07:02.573414", "lvl": "debug", "msg": "start: 1.1 download-retry (timeout 00:02:00) [common]"}""",
                 ),
             },
             {
@@ -1068,30 +895,30 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Jobs (from 2 to 4):\n"  # nosec
 
 
 def test_jobs_resubmit(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "resubmit", "1234"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "scheduler.jobs.resubmit", "args": ("1234",), "ret": 1234},
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "1234\n"  # nosec
 
 
 def test_jobs_resubmit_url(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "--uri",
             "https://localhost:8000/RPC2",
@@ -1112,15 +939,15 @@
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "https://localhost:8000/scheduler/job/1234\n"
     )
 
 
 def test_jobs_resubmit_mutlinode(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "resubmit", "1234"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -1131,15 +958,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "1234\n1235\n"  # nosec
 
 
 def test_jobs_resubmit_mutlinode_url(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "--uri",
             "https://example.com/RPC2",
@@ -1165,15 +992,15 @@
     assert (  # nosec
         capsys.readouterr()[0]
         == "https://example.com/scheduler/job/1234\nhttps://example.com/scheduler/job/1345\n"
     )
 
 
 def test_jobs_resubmit_follow(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 5  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(
@@ -1185,23 +1012,23 @@
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "scheduler.jobs.resubmit", "args": ("1234",), "ret": 1234},
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 0),
+                "args": ("1234", 0, None),
                 "ret": (
                     False,
-                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2018.4-1"}',
+                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2019.1-1"}',
                 ),
             },
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("1234", 1),
+                "args": ("1234", 1, None),
                 "ret": (
                     True,
                     """- {"dt": "2018-04-23T12:07:02.572789", "lvl": "results", "msg": {"case": "validate", "definition": "lava", "result": "pass"}}
 - {"dt": "2018-04-23T12:07:02.573414", "lvl": "debug", "msg": "start: 1.1 download-retry (timeout 00:02:00) [common]"}""",
                 ),
             },
             {
@@ -1228,56 +1055,56 @@
         ],
     )
     assert main() == 0  # nosec
     lines = capsys.readouterr()[0].split("\n")
     assert lines[0].endswith("[lavacli] Job 1234 submitted")  # nosec
     assert (  # nosec
         lines[1]
-        == "2018-04-23T12:07:02 lava-dispatcher, installed at version: 2018.4-1"
+        == "2018-04-23T12:07:02 lava-dispatcher, installed at version: 2019.1-1"
     )
     assert (  # nosec
         lines[2]
         == "2018-04-23T12:07:02 start: 1.1 download-retry (timeout 00:02:00) [common]"
     )
 
 
-def test_jobs_run(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
+def test_jobs_run(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 5  # nosec
 
-    with (tmpdir / "job.yaml").open("w") as f_out:
+    with (tmp_path / "job.yaml").open("w") as f_out:
         f_out.write("job definition")
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(
-        sys, "argv", ["lavacli", "jobs", "run", str(tmpdir / "job.yaml")]
+        sys, "argv", ["lavacli", "jobs", "run", str(tmp_path / "job.yaml")]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
                 "request": "scheduler.jobs.submit",
                 "args": ("job definition",),
                 "ret": "4567",
             },
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("4567", 0),
+                "args": ("4567", 0, None),
                 "ret": (
                     False,
-                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2018.4-1"}',
+                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2019.1-1"}',
                 ),
             },
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("4567", 1),
+                "args": ("4567", 1, None),
                 "ret": (
                     True,
                     """- {"dt": "2018-04-23T12:07:02.572789", "lvl": "results", "msg": {"case": "validate", "definition": "lava", "result": "pass"}}
 - {"dt": "2018-04-23T12:07:02.573414", "lvl": "debug", "msg": "start: 1.1 download-retry (timeout 00:02:00) [common]"}""",
                 ),
             },
             {
@@ -1304,81 +1131,30 @@
         ],
     )
     assert main() == 0  # nosec
     lines = capsys.readouterr()[0].split("\n")
     assert lines[0].endswith("[lavacli] Job 4567 submitted")  # nosec
     assert (  # nosec
         lines[1]
-        == "2018-04-23T12:07:02 lava-dispatcher, installed at version: 2018.4-1"
+        == "2018-04-23T12:07:02 lava-dispatcher, installed at version: 2019.1-1"
     )
     assert lines[2][:20] == "2018-04-23T12:07:02 "  # nosec
     assert safe_yaml.load(lines[2][20:]) == {  # nosec
         "case": "validate",
         "definition": "lava",
         "result": "pass",
     }
     assert (  # nosec
         lines[3]
         == "2018-04-23T12:07:02 start: 1.1 download-retry (timeout 00:02:00) [common]"
     )
 
 
-def test_jobs_show_before_2018_1(setup, monkeypatch, capsys):
-    version = "2017.12"
-    now = xmlrpc.client.DateTime("20180128T01:01:01")
-    monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "show", "789"])
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.jobs.show",
-                "args": ("789",),
-                "ret": {
-                    "id": "789",
-                    "description": "desc",
-                    "device": "qemu01",
-                    "device_type": "qemu",
-                    "health_check": False,
-                    "pipeline": True,
-                    "status": "Complete",
-                    "submitter": "lava-admin",
-                    "submit_time": now,
-                    "start_time": now,
-                    "end_time": now,
-                    "tags": [],
-                    "visibility": "Publicly visible",
-                    "failure_comment": None,
-                },
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert (  # nosec
-        capsys.readouterr()[0]
-        == """id          : 789
-description : desc
-submitter   : lava-admin
-device-type : qemu
-device      : qemu01
-health-check: False
-status      : Complete
-pipeline    : True
-tags        : []
-visibility  : Publicly visible
-submit time : 20180128T01:01:01
-start time  : 20180128T01:01:01
-end time    : 20180128T01:01:01
-"""
-    )
-
-
 def test_jobs_show(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "show", "789"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -1423,15 +1199,15 @@
 start time  : 20180128T01:01:01
 end time    : 20180128T01:01:01
 """
     )
 
 
 def test_jobs_show_failure_comment(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "show", "789"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -1477,15 +1253,15 @@
 start time  : 20180128T01:01:01
 end time    : 20180128T01:01:01
 """
     )
 
 
 def test_jobs_show_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "show", "789", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -1529,15 +1305,15 @@
         "tags": [],
         "visibility": "Publicly visible",
         "failure_comment": None,
     }
 
 
 def test_jobs_show_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "show", "789", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -1582,20 +1358,20 @@
 submitter: lava-admin
 tags: []
 visibility: Publicly visible
 """
     )
 
 
-def test_jobs_submit(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "job.yaml").open("w") as f_out:
+def test_jobs_submit(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "job.yaml").open("w") as f_out:
         f_out.write("job definition as yaml")
     monkeypatch.setattr(
-        sys, "argv", ["lavacli", "jobs", "submit", str(tmpdir / "job.yaml")]
+        sys, "argv", ["lavacli", "jobs", "submit", str(tmp_path / "job.yaml")]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -1605,28 +1381,28 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "5689\n"  # nosec
 
 
-def test_jobs_submit_url(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "job.yaml").open("w") as f_out:
+def test_jobs_submit_url(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "job.yaml").open("w") as f_out:
         f_out.write("job definition as yaml")
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "--uri",
             "https://localhost:8000/RPC2",
             "jobs",
             "submit",
-            str(tmpdir / "job.yaml"),
+            str(tmp_path / "job.yaml"),
             "--url",
         ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -1640,20 +1416,20 @@
     )
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "https://localhost:8000/scheduler/job/5689\n"
     )
 
 
-def test_jobs_submit_url_identity_default(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "job.yaml").open("w") as f_out:
+def test_jobs_submit_url_identity_default(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "job.yaml").open("w") as f_out:
         f_out.write("job definition as yaml")
     monkeypatch.setattr(
-        sys, "argv", ["lavacli", "jobs", "submit", str(tmpdir / "job.yaml"), "--url"]
+        sys, "argv", ["lavacli", "jobs", "submit", str(tmp_path / "job.yaml"), "--url"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -1665,30 +1441,38 @@
     )
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "https://lava.example.com/scheduler/job/5689\n"
     )
 
 
-def test_jobs_submit_url_identity_admin(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "job.yaml").open("w") as f_out:
+def test_jobs_submit_url_identity_admin(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "job.yaml").open("w") as f_out:
         f_out.write("job definition as yaml")
-    with (tmpdir / "lavacli.yaml").open("w") as f_conf:
+    with (tmp_path / "lavacli.yaml").open("w") as f_conf:
         safe_yaml.dump(
             {
                 "default": {"uri": "https://lava.example.com/RPC2"},
                 "admin": {"uri": "https://localhost:8001/RPC2"},
             },
             f_conf,
         )
     monkeypatch.setattr(
         sys,
         "argv",
-        ["lavacli", "-i", "admin", "jobs", "submit", str(tmpdir / "job.yaml"), "--url"],
+        [
+            "lavacli",
+            "-i",
+            "admin",
+            "jobs",
+            "submit",
+            str(tmp_path / "job.yaml"),
+            "--url",
+        ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -1700,32 +1484,32 @@
     )
     assert main() == 0  # nosec
     assert (  # nosec
         capsys.readouterr()[0] == "https://localhost:8001/scheduler/job/5689\n"
     )
 
 
-def test_jobs_submit_multiple(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "job1.yaml").open("w") as f_out:
+def test_jobs_submit_multiple(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "job1.yaml").open("w") as f_out:
         f_out.write("first job definition as yaml")
-    with (tmpdir / "job2.yaml").open("w") as f_out:
+    with (tmp_path / "job2.yaml").open("w") as f_out:
         f_out.write("second job definition as yaml")
-    with (tmpdir / "job3.yaml").open("w") as f_out:
+    with (tmp_path / "job3.yaml").open("w") as f_out:
         f_out.write("third job definition as yaml")
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "jobs",
             "submit",
-            str(tmpdir / "job1.yaml"),
-            str(tmpdir / "job2.yaml"),
-            str(tmpdir / "job3.yaml"),
+            str(tmp_path / "job1.yaml"),
+            str(tmp_path / "job2.yaml"),
+            str(tmp_path / "job3.yaml"),
         ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -1746,20 +1530,20 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "5689\n5690\n5691\n5692\n"  # nosec
 
 
-def test_jobs_submit_multinode(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "job.yaml").open("w") as f_out:
+def test_jobs_submit_multinode(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "job.yaml").open("w") as f_out:
         f_out.write("job definition as yaml")
     monkeypatch.setattr(
-        sys, "argv", ["lavacli", "jobs", "submit", str(tmpdir / "job.yaml")]
+        sys, "argv", ["lavacli", "jobs", "submit", str(tmp_path / "job.yaml")]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -1769,28 +1553,28 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "5689\n5698\n"  # nosec
 
 
-def test_jobs_submit_multinode_url(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "job.yaml").open("w") as f_out:
+def test_jobs_submit_multinode_url(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "job.yaml").open("w") as f_out:
         f_out.write("job definition as yaml")
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "--uri",
             "https://localhost:8000/RPC2",
             "jobs",
             "submit",
-            str(tmpdir / "job.yaml"),
+            str(tmp_path / "job.yaml"),
             "--url",
         ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -1806,15 +1590,15 @@
     assert (  # nosec
         capsys.readouterr()[0]
         == "https://localhost:8000/scheduler/job/5689\nhttps://localhost:8000/scheduler/job/5698\n"
     )
 
 
 def test_jobs_wait(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     now = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 5  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(sys, "argv", ["lavacli", "jobs", "wait", "1234"])
@@ -1910,38 +1694,40 @@
         ],
     )
 
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "Submitted\nRunning.\n"  # nosec
 
 
-def test_jobs_submit_follow(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "job.yaml").open("w") as f_out:
+def test_jobs_submit_follow(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "job.yaml").open("w") as f_out:
         f_out.write("job definition as yaml")
     monkeypatch.setattr(
-        sys, "argv", ["lavacli", "jobs", "submit", "--follow", str(tmpdir / "job.yaml")]
+        sys,
+        "argv",
+        ["lavacli", "jobs", "submit", "--follow", str(tmp_path / "job.yaml")],
     )
     now = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
                 "request": "scheduler.jobs.submit",
                 "args": ("job definition as yaml",),
                 "ret": 5689,
             },
             {
                 "request": "scheduler.jobs.logs",
-                "args": ("5689", 0),
+                "args": ("5689", 0, None),
                 "ret": (
                     True,
-                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2018.4-1"}',
+                    '- {"dt": "2018-04-23T12:07:02.569264", "lvl": "info", "msg": "lava-dispatcher, installed at version: 2019.1-1"}',
                 ),
             },
             {
                 "request": "scheduler.jobs.show",
                 "args": ("5689",),
                 "ret": {
                     "id": "5689",
@@ -1960,8 +1746,8 @@
                     "visibility": "Publicly visible",
                     "failure_comment": None,
                 },
             },
         ],
     )
     assert main() == 0  # nosec
-    assert "lava-dispatcher, installed at version: 2018.4" in capsys.readouterr()[0]
+    assert "lava-dispatcher, installed at version: 2019.1" in capsys.readouterr()[0]
```

### Comparing `lavacli-1.6/tests/test_lavacli.py` & `lavacli-1.7/tests/test_lavacli.py`

 * *Files identical despite different names*

### Comparing `lavacli-1.6/tests/test_results.py` & `lavacli-1.7/tests/test_results.py`

 * *Files 3% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 import sys
 import xmlrpc.client
 
 from lavacli import main
 
 
 def test_results_job(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -45,15 +45,15 @@
 * lava.validate [pass]
 * lava.job [fail]
 """
     )
 
 
 def test_results_job_isatty(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234"])
     monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -72,15 +72,15 @@
 * lava.boot [skip]
 * lava.job [\033[1;31mfail\033[0m]
 """
     )
 
 
 def test_results_job_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -94,15 +94,15 @@
     assert json.loads(capsys.readouterr()[0]) == [  # nosec
         {"name": "validate", "result": "pass", "suite": "lava"},
         {"name": "job", "result": "fail", "suite": "lava"},
     ]
 
 
 def test_results_job_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -118,15 +118,15 @@
         == """- {name: validate, result: pass, suite: lava}
 - {name: job, result: fail, suite: lava}
 """
     )
 
 
 def test_results_suite(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "lava"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -143,15 +143,15 @@
 * lava.validate [pass]
 * lava.job [fail]
 """
     )
 
 
 def test_results_suite_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "lava", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -165,15 +165,15 @@
     assert json.loads(capsys.readouterr()[0]) == [  # nosec
         {"name": "validate", "result": "pass", "suite": "lava"},
         {"name": "job", "result": "fail", "suite": "lava"},
     ]
 
 
 def test_results_suite_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "lava", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -189,15 +189,15 @@
         == """- {name: validate, result: pass, suite: lava}
 - {name: job, result: fail, suite: lava}
 """
     )
 
 
 def test_results_case(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "lava", "validate"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -208,15 +208,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "pass\n"  # nosec
 
 
 def test_results_case_isatty_pass(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "lava", "validate"])
     monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -228,15 +228,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "\033[1;32mpass\033[0m\n"  # nosec
 
 
 def test_results_case_isatty_fail(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "lava", "validate"])
     monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -248,15 +248,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "\033[1;31mfail\033[0m\n"  # nosec
 
 
 def test_results_case_isatty_skip(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "lava", "validate"])
     monkeypatch.setattr(sys.stdout, "isatty", lambda: True)
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -268,15 +268,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "skip\n"  # nosec
 
 
 def test_results_case_1(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "results", "1234", "lava", "validate"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -287,15 +287,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "pass\nfail\n"  # nosec
 
 
 def test_results_case_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "results", "1234", "lava", "validate", "--json"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -310,15 +310,15 @@
     assert main() == 0  # nosec
     assert json.loads(capsys.readouterr()[0]) == [  # nosec
         {"name": "validate", "result": "pass", "suite": "lava"}
     ]
 
 
 def test_results_case_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "results", "1234", "lava", "validate", "--yaml"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
```

### Comparing `lavacli-1.6/tests/test_system.py` & `lavacli-1.7/tests/test_system.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 import time
 import xmlrpc.client
 
 from lavacli import main
 
 
 def test_system_active(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "system", "active"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -55,39 +55,39 @@
 * worker01
 * worker02
 """
     )
 
 
 def test_system_api(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "system", "api"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "system.api_version", "args": (), "ret": 2},
         ],
     )
 
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "2\n"  # nosec
 
 
-def test_system_export(setup, monkeypatch, capsys, tmpdir):
+def test_system_export(setup, monkeypatch, capsys, tmp_path):
     last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(
-        sys, "argv", ["lavacli", "system", "export", str(tmpdir / "export")]
+        sys, "argv", ["lavacli", "system", "export", str(tmp_path / "export")]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
-            {"request": "system.version", "args": (), "ret": "2018.6"},
+            {"request": "system.version", "args": (), "ret": "2019.1"},
             {
                 "request": "scheduler.aliases.list",
                 "args": (),
                 "ret": ["alias01", "alias02"],
             },
             {
                 "request": "scheduler.aliases.show",
@@ -252,15 +252,15 @@
                 "args": ("bbb-01",),
                 "ret": "bbb-01 device dict",
             },
         ],
     )
     assert main() == 0  # nosec
     lines = capsys.readouterr()[0].split("\n")
-    assert lines[0] == "Export to %s" % str(tmpdir / "export")  # nosec
+    assert lines[0] == "Export to %s" % str(tmp_path / "export")  # nosec
     assert (  # nosec
         "\n".join(lines[1:])
         == """Listing aliases
 * alias01
 * alias02
 Listing tags
 * hdd
@@ -286,15 +286,15 @@
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(sys, "argv", ["lavacli", "system", "maintenance"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
-            {"request": "system.version", "args": (), "ret": "2018.6"},
+            {"request": "system.version", "args": (), "ret": "2019.1"},
             {
                 "request": "scheduler.workers.list",
                 "args": (),
                 "ret": ["worker01", "worker02"],
             },
             {
                 "request": "scheduler.workers.update",
@@ -428,15 +428,15 @@
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "system", "maintenance", "--exclude", "worker01"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
-            {"request": "system.version", "args": (), "ret": "2018.6"},
+            {"request": "system.version", "args": (), "ret": "2019.1"},
             {
                 "request": "scheduler.workers.list",
                 "args": (),
                 "ret": ["worker01", "worker02"],
             },
             {
                 "request": "scheduler.workers.update",
@@ -551,15 +551,15 @@
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(sys, "argv", ["lavacli", "system", "maintenance", "--force"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
-            {"request": "system.version", "args": (), "ret": "2018.6"},
+            {"request": "system.version", "args": (), "ret": "2019.1"},
             {
                 "request": "scheduler.workers.list",
                 "args": (),
                 "ret": ["worker01", "worker02"],
             },
             {
                 "request": "scheduler.workers.update",
@@ -667,15 +667,15 @@
 
 def test_system_methods_list(setup, monkeypatch, capsys):
     monkeypatch.setattr(sys, "argv", ["lavacli", "system", "methods", "list"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
-            {"request": "system.version", "args": (), "ret": "2018.6"},
+            {"request": "system.version", "args": (), "ret": "2019.1"},
             {
                 "request": "system.listMethods",
                 "args": (),
                 "ret": [
                     "scheduler.job_details",
                     "scheduler.job_health",
                     "scheduler.job_list_status",
@@ -694,15 +694,15 @@
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "system", "methods", "help", "system.version"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
-            {"request": "system.version", "args": (), "ret": "2018.6"},
+            {"request": "system.version", "args": (), "ret": "2019.1"},
             {
                 "request": "system.methodHelp",
                 "args": ("system.version",),
                 "ret": """Name
 ----
 `system.version` ()
 
@@ -748,46 +748,46 @@
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "system", "methods", "signature", "system.version"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
-            {"request": "system.version", "args": (), "ret": "2018.6"},
+            {"request": "system.version", "args": (), "ret": "2019.1"},
             {
                 "request": "system.methodSignature",
                 "args": ("system.version",),
                 "ret": "undef",
             },
         ],
     )
 
     assert main() == 0  # nosec
 
     assert capsys.readouterr()[0] == "undef\n"  # nosec
 
 
 def test_system_version(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "system", "version"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "system.version", "args": (), "ret": version},
         ],
     )
 
     assert main() == 0  # nosec
-    assert capsys.readouterr()[0] == "2018.4\n"  # nosec
+    assert capsys.readouterr()[0] == "2019.1\n"  # nosec
 
 
 def test_system_whoami(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "system", "whoami"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "system.whoami", "args": (), "ret": "lava-admin"},
@@ -795,15 +795,15 @@
     )
 
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "lava-admin\n"  # nosec
 
 
 def test_system_whoami_anonymous(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "system", "whoami"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "system.whoami", "args": (), "ret": None},
```

### Comparing `lavacli-1.6/tests/test_tags.py` & `lavacli-1.7/tests/test_tags.py`

 * *Files 8% similar despite different names*

```diff
@@ -20,45 +20,45 @@
 import sys
 import xmlrpc.client
 
 from lavacli import main
 
 
 def test_tags_add(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "tags", "add", "hdd"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "scheduler.tags.add", "args": ("hdd", None), "ret": None},
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_tags_delete(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "tags", "delete", "hdd"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {"request": "scheduler.tags.delete", "args": ("hdd",), "ret": None},
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_tags_list(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "tags", "list"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -78,15 +78,15 @@
 * hdd (drive attached)
 * tag1
 """
     )
 
 
 def test_tags_list_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "tags", "list", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -103,15 +103,15 @@
     assert json.loads(capsys.readouterr()[0]) == [  # nosec
         {"name": "hdd", "description": "drive attached"},
         {"name": "tag1", "description": None},
     ]
 
 
 def test_tags_list_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "tags", "list", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -130,15 +130,15 @@
         == """- {description: drive attached, name: hdd}
 - {description: null, name: tag1}
 """
     )
 
 
 def test_tags_show(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "tags", "show", "hdd"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -161,15 +161,15 @@
 * aemu01
 * bbb-01
 """
     )
 
 
 def test_tags_show_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "tags", "show", "--json", "hdd"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -188,15 +188,15 @@
         "name": "hdd",
         "description": "drive attached",
         "devices": ["aemu01", "bbb-01"],
     }
 
 
 def test_tags_show_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "tags", "show", "--yaml", "hdd"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
```

### Comparing `lavacli-1.6/tests/test_workers.py` & `lavacli-1.7/tests/test_workers.py`

 * *Files 6% similar despite different names*

```diff
@@ -21,15 +21,15 @@
 import time
 import xmlrpc.client
 
 from lavacli import main
 
 
 def test_workers_add(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "workers", "add", "worker01"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -40,15 +40,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_workers_add_1(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "workers",
             "add",
@@ -70,15 +70,15 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
-def test_workers_config_delete(setup, monkeypatch, capsys, tmpdir):
+def test_workers_config_delete(setup, monkeypatch, capsys, tmp_path):
     version = "2022.4"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "workers",
@@ -100,15 +100,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_workers_config_get(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "workers", "config", "get", "worker01"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
@@ -120,28 +120,28 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "config content\n"  # nosec
 
 
-def test_workers_config_set(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "config.yaml").open("w") as f_conf:
+def test_workers_config_set(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "config.yaml").open("w") as f_conf:
         f_conf.write("config content")
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "workers",
             "config",
             "set",
             "worker01",
-            str(tmpdir / "config.yaml"),
+            str(tmp_path / "config.yaml"),
         ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -152,28 +152,28 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
-def test_workers_config_set_error(setup, monkeypatch, capsys, tmpdir):
-    version = "2018.4"
-    with (tmpdir / "config.yaml").open("w") as f_conf:
+def test_workers_config_set_error(setup, monkeypatch, capsys, tmp_path):
+    version = "2019.1"
+    with (tmp_path / "config.yaml").open("w") as f_conf:
         f_conf.write("config content")
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "workers",
             "config",
             "set",
             "worker01",
-            str(tmpdir / "config.yaml"),
+            str(tmp_path / "config.yaml"),
         ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -184,15 +184,15 @@
             },
         ],
     )
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Unable to store worker configuration\n"  # nosec
 
 
-def test_workers_env_delete(setup, monkeypatch, capsys, tmpdir):
+def test_workers_env_delete(setup, monkeypatch, capsys, tmp_path):
     version = "2022.4"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "workers", "env", "delete", "worker01"],
     )
     monkeypatch.setattr(
@@ -226,22 +226,22 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "env content\n"  # nosec
 
 
-def test_workers_env_set(setup, monkeypatch, capsys, tmpdir):
+def test_workers_env_set(setup, monkeypatch, capsys, tmp_path):
     version = "2019.6"
-    with (tmpdir / "env.yaml").open("w") as f_conf:
+    with (tmp_path / "env.yaml").open("w") as f_conf:
         f_conf.write("env content")
     monkeypatch.setattr(
         sys,
         "argv",
-        ["lavacli", "workers", "env", "set", "worker01", str(tmpdir / "env.yaml")],
+        ["lavacli", "workers", "env", "set", "worker01", str(tmp_path / "env.yaml")],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -251,22 +251,22 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
-def test_workers_env_set_error(setup, monkeypatch, capsys, tmpdir):
+def test_workers_env_set_error(setup, monkeypatch, capsys, tmp_path):
     version = "2019.6"
-    with (tmpdir / "env.yaml").open("w") as f_conf:
+    with (tmp_path / "env.yaml").open("w") as f_conf:
         f_conf.write("env content")
     monkeypatch.setattr(
         sys,
         "argv",
-        ["lavacli", "workers", "env", "set", "worker01", str(tmpdir / "env.yaml")],
+        ["lavacli", "workers", "env", "set", "worker01", str(tmp_path / "env.yaml")],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -276,15 +276,15 @@
             },
         ],
     )
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Unable to store worker environment\n"  # nosec
 
 
-def test_workers_env_dut_delete(setup, monkeypatch, capsys, tmpdir):
+def test_workers_env_dut_delete(setup, monkeypatch, capsys, tmp_path):
     version = "2022.4"
     monkeypatch.setattr(
         sys,
         "argv",
         ["lavacli", "workers", "env-dut", "delete", "worker01"],
     )
     monkeypatch.setattr(
@@ -320,22 +320,29 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "env-dut content\n"  # nosec
 
 
-def test_workers_env_dut_set(setup, monkeypatch, capsys, tmpdir):
+def test_workers_env_dut_set(setup, monkeypatch, capsys, tmp_path):
     version = "2022.4"
-    with (tmpdir / "env.yaml").open("w") as f_conf:
+    with (tmp_path / "env.yaml").open("w") as f_conf:
         f_conf.write("env-dut content")
     monkeypatch.setattr(
         sys,
         "argv",
-        ["lavacli", "workers", "env-dut", "set", "worker01", str(tmpdir / "env.yaml")],
+        [
+            "lavacli",
+            "workers",
+            "env-dut",
+            "set",
+            "worker01",
+            str(tmp_path / "env.yaml"),
+        ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -345,22 +352,29 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
-def test_workers_env_dut_set_error(setup, monkeypatch, capsys, tmpdir):
+def test_workers_env_dut_set_error(setup, monkeypatch, capsys, tmp_path):
     version = "2022.4"
-    with (tmpdir / "env.yaml").open("w") as f_conf:
+    with (tmp_path / "env.yaml").open("w") as f_conf:
         f_conf.write("env-dut content")
     monkeypatch.setattr(
         sys,
         "argv",
-        ["lavacli", "workers", "env-dut", "set", "worker01", str(tmpdir / "env.yaml")],
+        [
+            "lavacli",
+            "workers",
+            "env-dut",
+            "set",
+            "worker01",
+            str(tmp_path / "env.yaml"),
+        ],
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -370,16 +384,41 @@
             },
         ],
     )
     assert main() == 1  # nosec
     assert capsys.readouterr()[1] == "Unable to store worker dut environment\n"  # nosec
 
 
+def test_workers_list_exclude_retired(setup, monkeypatch, capsys):
+    version = "2023.3"
+    monkeypatch.setattr(sys, "argv", ["lavacli", "workers", "list"])
+    monkeypatch.setattr(
+        xmlrpc.client.ServerProxy,
+        "data",
+        [
+            {"request": "system.version", "args": (), "ret": version},
+            {
+                "request": "scheduler.workers.list",
+                "args": (False,),
+                "ret": ["worker01", "worker02"],
+            },
+        ],
+    )
+    assert main() == 0  # nosec
+    assert (  # nosec
+        capsys.readouterr()[0]
+        == """Workers:
+* worker01
+* worker02
+"""
+    )
+
+
 def test_workers_list(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "workers", "list"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -396,15 +435,15 @@
 * worker01
 * worker02
 """
     )
 
 
 def test_workers_list_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "workers", "list", "--json"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -415,15 +454,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == '["worker01", "worker02"]\n'  # nosec
 
 
 def test_workers_list_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(sys, "argv", ["lavacli", "workers", "list", "--yaml"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
             {
@@ -434,15 +473,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "[worker01, worker02]\n"  # nosec
 
 
 def test_workers_maintenance(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
 
     def sleep(duration):
         assert duration == 5  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(sys, "argv", ["lavacli", "workers", "maintenance", "worker01"])
@@ -543,15 +582,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "-> waiting for job 1234\n--> waiting\n"  # nosec
 
 
 def test_workers_maintenance_nowait(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
 
     def sleep(duration):
         assert duration == 5  # nosec
 
     monkeypatch.setattr(time, "sleep", sleep)
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "workers", "maintenance", "worker01", "--no-wait"]
@@ -569,15 +608,15 @@
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == ""  # nosec
 
 
 def test_workers_maintenance_force(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "workers", "maintenance", "worker01", "--force"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
@@ -646,86 +685,16 @@
             },
         ],
     )
     assert main() == 0  # nosec
     assert capsys.readouterr()[0] == "-> waiting for job 1234\n--> canceling\n"  # nosec
 
 
-def test_workers_show_before_2017_12(setup, monkeypatch, capsys):
-    version = "2017.11"
-    last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
-    monkeypatch.setattr(sys, "argv", ["lavacli", "workers", "show", "worker01"])
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.workers.show",
-                "args": ("worker01",),
-                "ret": {
-                    "hostname": "worker01",
-                    "description": None,
-                    "master": False,
-                    "hidden": False,
-                    "devices": 2,
-                    "last_ping": last_ping,
-                },
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert (  # nosec
-        capsys.readouterr()[0]
-        == """hostname    : worker01
-description : None
-master      : False
-hidden      : False
-devices     : 2
-"""
-    )
-
-
-def test_workers_show_before_2018_1(setup, monkeypatch, capsys):
-    version = "2017.12"
-    last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
-    monkeypatch.setattr(sys, "argv", ["lavacli", "workers", "show", "worker01"])
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.workers.show",
-                "args": ("worker01",),
-                "ret": {
-                    "hostname": "worker01",
-                    "description": None,
-                    "state": "Idle",
-                    "health": "Active",
-                    "devices": 2,
-                    "last_ping": last_ping,
-                },
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert (  # nosec
-        capsys.readouterr()[0]
-        == """hostname    : worker01
-description : None
-state       : Idle
-health      : Active
-devices     : 2
-"""
-    )
-
-
 def test_workers_show(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(sys, "argv", ["lavacli", "workers", "show", "worker01"])
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
         [
             {"request": "system.version", "args": (), "ret": version},
@@ -753,15 +722,15 @@
 devices     : qemu01, bbb-01
 last ping   : 20180128T01:01:01
 """
     )
 
 
 def test_workers_show_json(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "workers", "show", "worker01", "--json"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
@@ -789,15 +758,15 @@
         "health": "Active",
         "devices": ["qemu01", "bbb-01"],
         "last_ping": "20180128T01:01:01",
     }
 
 
 def test_workers_show_yaml(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     last_ping = xmlrpc.client.DateTime("20180128T01:01:01")
     monkeypatch.setattr(
         sys, "argv", ["lavacli", "workers", "show", "worker01", "--yaml"]
     )
     monkeypatch.setattr(
         xmlrpc.client.ServerProxy,
         "data",
@@ -826,37 +795,16 @@
 hostname: worker01
 last_ping: 20180128T01:01:01
 state: Idle
 """
     )
 
 
-def test_workers_update_before_2017_12(setup, monkeypatch, capsys):
-    version = "2017.11"
-    monkeypatch.setattr(
-        sys, "argv", ["lavacli", "workers", "update", "worker01", "--disable"]
-    )
-    monkeypatch.setattr(
-        xmlrpc.client.ServerProxy,
-        "data",
-        [
-            {"request": "system.version", "args": (), "ret": version},
-            {
-                "request": "scheduler.workers.update",
-                "args": ("worker01", None, True),
-                "ret": None,
-            },
-        ],
-    )
-    assert main() == 0  # nosec
-    assert capsys.readouterr()[0] == ""  # nosec
-
-
 def test_workers_update(setup, monkeypatch, capsys):
-    version = "2018.4"
+    version = "2019.1"
     monkeypatch.setattr(
         sys,
         "argv",
         [
             "lavacli",
             "workers",
             "update",
```

