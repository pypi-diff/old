# Comparing `tmp/coba-6.4.1.tar.gz` & `tmp/coba-6.4.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\coba-6.4.1.tar", last modified: Sat Apr  1 21:51:51 2023, max compression
+gzip compressed data, was "dist\coba-6.4.2.tar", last modified: Thu Apr  6 14:58:16 2023, max compression
```

## Comparing `coba-6.4.1.tar` & `coba-6.4.2.tar`

### file list

```diff
@@ -1,73 +1,73 @@
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/
--rw-rw-rw-   0        0        0       40 2021-11-14 20:00:02.000000 coba-6.4.1/AUTHORS
--rw-rw-rw-   0        0        0     1593 2021-11-14 20:00:02.000000 coba-6.4.1/LICENSE
--rw-rw-rw-   0        0        0     7956 2023-04-01 21:51:51.000000 coba-6.4.1/PKG-INFO
--rw-rw-rw-   0        0        0     7336 2023-02-22 16:34:05.000000 coba-6.4.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/coba/
--rw-rw-rw-   0        0        0     1996 2023-02-22 16:34:05.000000 coba-6.4.1/coba/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/coba/backports/
--rw-rw-rw-   0        0        0      222 2022-11-27 17:52:42.000000 coba-6.4.1/coba/backports/__init__.py
--rw-rw-rw-   0        0        0      473 2022-04-27 16:17:38.000000 coba-6.4.1/coba/backports/metadata.py
--rw-rw-rw-   0        0        0      143 2022-11-27 17:52:42.000000 coba-6.4.1/coba/backports/typing.py
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/coba/contexts/
--rw-rw-rw-   0        0        0      994 2022-10-09 15:45:49.000000 coba-6.4.1/coba/contexts/__init__.py
--rw-rw-rw-   0        0        0     9727 2023-02-22 16:34:05.000000 coba-6.4.1/coba/contexts/cachers.py
--rw-rw-rw-   0        0        0     9263 2023-03-15 01:44:54.000000 coba-6.4.1/coba/contexts/core.py
--rw-rw-rw-   0        0        0     8881 2023-02-22 16:34:05.000000 coba-6.4.1/coba/contexts/loggers.py
--rw-rw-rw-   0        0        0    15634 2022-12-02 22:43:08.000000 coba-6.4.1/coba/encodings.py
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/coba/environments/
--rw-rw-rw-   0        0        0     2286 2023-02-22 15:59:12.000000 coba-6.4.1/coba/environments/__init__.py
--rw-rw-rw-   0        0        0    21561 2023-03-12 01:08:17.000000 coba-6.4.1/coba/environments/core.py
--rw-rw-rw-   0        0        0    44618 2023-03-15 01:38:26.000000 coba-6.4.1/coba/environments/filters.py
--rw-rw-rw-   0        0        0    14316 2023-02-22 16:34:05.000000 coba-6.4.1/coba/environments/openml.py
--rw-rw-rw-   0        0        0     8220 2023-03-11 23:39:33.000000 coba-6.4.1/coba/environments/primitives.py
--rw-rw-rw-   0        0        0     2598 2023-02-22 16:34:05.000000 coba-6.4.1/coba/environments/serialized.py
--rw-rw-rw-   0        0        0    10122 2023-02-22 16:34:56.000000 coba-6.4.1/coba/environments/supervised.py
--rw-rw-rw-   0        0        0    24193 2023-02-22 15:59:12.000000 coba-6.4.1/coba/environments/synthetics.py
--rw-rw-rw-   0        0        0     6076 2023-02-22 15:59:12.000000 coba-6.4.1/coba/environments/templates.py
--rw-rw-rw-   0        0        0     1126 2022-04-27 16:17:38.000000 coba-6.4.1/coba/exceptions.py
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/coba/experiments/
--rw-rw-rw-   0        0        0      859 2023-01-14 22:42:57.000000 coba-6.4.1/coba/experiments/__init__.py
--rw-rw-rw-   0        0        0     9523 2023-03-15 01:34:27.000000 coba-6.4.1/coba/experiments/core.py
--rw-rw-rw-   0        0        0     9216 2023-03-23 06:41:59.000000 coba-6.4.1/coba/experiments/process.py
--rw-rw-rw-   0        0        0    53044 2023-03-01 23:34:22.000000 coba-6.4.1/coba/experiments/results.py
--rw-rw-rw-   0        0        0    25294 2023-03-15 01:58:08.000000 coba-6.4.1/coba/experiments/tasks.py
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/coba/learners/
--rw-rw-rw-   0        0        0     1120 2023-02-22 16:34:05.000000 coba-6.4.1/coba/learners/__init__.py
--rw-rw-rw-   0        0        0     6453 2023-03-15 01:04:42.000000 coba-6.4.1/coba/learners/bandit.py
--rw-rw-rw-   0        0        0     7801 2023-02-22 16:34:05.000000 coba-6.4.1/coba/learners/corral.py
--rw-rw-rw-   0        0        0     4771 2023-02-22 16:34:05.000000 coba-6.4.1/coba/learners/linucb.py
--rw-rw-rw-   0        0        0    14794 2023-03-01 23:52:04.000000 coba-6.4.1/coba/learners/primitives.py
--rw-rw-rw-   0        0        0    30352 2023-03-15 02:33:32.000000 coba-6.4.1/coba/learners/vowpal.py
--rw-rw-rw-   0        0        0     4277 2023-03-15 01:43:39.000000 coba-6.4.1/coba/multiprocessing.py
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/coba/pipes/
--rw-rw-rw-   0        0        0     2394 2023-02-22 16:34:05.000000 coba-6.4.1/coba/pipes/__init__.py
--rw-rw-rw-   0        0        0     1902 2023-02-22 16:34:05.000000 coba-6.4.1/coba/pipes/core.py
--rw-rw-rw-   0        0        0    15360 2023-02-25 19:41:52.000000 coba-6.4.1/coba/pipes/filters.py
--rw-rw-rw-   0        0        0    14945 2023-03-01 23:34:22.000000 coba-6.4.1/coba/pipes/multiprocessing.py
--rw-rw-rw-   0        0        0     6622 2023-02-22 16:34:05.000000 coba-6.4.1/coba/pipes/primitives.py
--rw-rw-rw-   0        0        0    13017 2023-02-22 16:00:21.000000 coba-6.4.1/coba/pipes/readers.py
--rw-rw-rw-   0        0        0    18680 2023-02-22 16:34:05.000000 coba-6.4.1/coba/pipes/rows.py
--rw-rw-rw-   0        0        0     3734 2023-03-01 23:34:22.000000 coba-6.4.1/coba/pipes/sinks.py
--rw-rw-rw-   0        0        0     6154 2023-03-01 23:34:22.000000 coba-6.4.1/coba/pipes/sources.py
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/coba/primitives/
--rw-rw-rw-   0        0        0      870 2023-03-11 21:43:20.000000 coba-6.4.1/coba/primitives/__init__.py
--rw-rw-rw-   0        0        0      930 2022-12-13 14:59:41.000000 coba-6.4.1/coba/primitives/feedbacks.py
--rw-rw-rw-   0        0        0     6432 2023-03-11 21:54:59.000000 coba-6.4.1/coba/primitives/rewards.py
--rw-rw-rw-   0        0        0     4425 2023-02-22 16:34:05.000000 coba-6.4.1/coba/primitives/rows.py
--rw-rw-rw-   0        0        0      234 2022-12-13 01:57:20.000000 coba-6.4.1/coba/primitives/semantic.py
--rw-rw-rw-   0        0        0      556 2023-02-22 16:34:05.000000 coba-6.4.1/coba/primitives/types.py
--rw-rw-rw-   0        0        0    10887 2023-03-12 00:39:45.000000 coba-6.4.1/coba/random.py
--rw-rw-rw-   0        0        0     1405 2023-02-22 15:59:12.000000 coba-6.4.1/coba/register.py
--rw-rw-rw-   0        0        0    10657 2022-05-30 19:08:09.000000 coba-6.4.1/coba/registry.py
--rw-rw-rw-   0        0        0     7199 2023-03-01 23:34:22.000000 coba-6.4.1/coba/statistics.py
--rw-rw-rw-   0        0        0     4504 2023-01-14 22:42:57.000000 coba-6.4.1/coba/utilities.py
-drwxrwxrwx   0        0        0        0 2023-04-01 21:51:51.000000 coba-6.4.1/coba.egg-info/
--rw-rw-rw-   0        0        0     7956 2023-04-01 21:51:51.000000 coba-6.4.1/coba.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1466 2023-04-01 21:51:51.000000 coba-6.4.1/coba.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-01 21:51:51.000000 coba-6.4.1/coba.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       37 2023-04-01 21:51:51.000000 coba-6.4.1/coba.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       91 2023-04-01 21:51:51.000000 coba-6.4.1/coba.egg-info/requires.txt
--rw-rw-rw-   0        0        0        5 2023-04-01 21:51:51.000000 coba-6.4.1/coba.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-01 21:51:51.000000 coba-6.4.1/setup.cfg
--rw-rw-rw-   0        0        0     1289 2023-04-01 21:48:36.000000 coba-6.4.1/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/
+-rw-rw-rw-   0        0        0       40 2021-11-14 20:00:02.000000 coba-6.4.2/AUTHORS
+-rw-rw-rw-   0        0        0     1593 2021-11-14 20:00:02.000000 coba-6.4.2/LICENSE
+-rw-rw-rw-   0        0        0     7956 2023-04-06 14:58:16.000000 coba-6.4.2/PKG-INFO
+-rw-rw-rw-   0        0        0     7336 2023-02-22 16:34:05.000000 coba-6.4.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/coba/
+-rw-rw-rw-   0        0        0     1996 2023-02-22 16:34:05.000000 coba-6.4.2/coba/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/coba/backports/
+-rw-rw-rw-   0        0        0      222 2022-11-27 17:52:42.000000 coba-6.4.2/coba/backports/__init__.py
+-rw-rw-rw-   0        0        0      473 2022-04-27 16:17:38.000000 coba-6.4.2/coba/backports/metadata.py
+-rw-rw-rw-   0        0        0      143 2022-11-27 17:52:42.000000 coba-6.4.2/coba/backports/typing.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/coba/contexts/
+-rw-rw-rw-   0        0        0     1035 2023-04-05 17:51:59.000000 coba-6.4.2/coba/contexts/__init__.py
+-rw-rw-rw-   0        0        0     9727 2023-02-22 16:34:05.000000 coba-6.4.2/coba/contexts/cachers.py
+-rw-rw-rw-   0        0        0     9263 2023-03-15 01:44:54.000000 coba-6.4.2/coba/contexts/core.py
+-rw-rw-rw-   0        0        0     9715 2023-04-05 18:41:31.000000 coba-6.4.2/coba/contexts/loggers.py
+-rw-rw-rw-   0        0        0    15634 2022-12-02 22:43:08.000000 coba-6.4.2/coba/encodings.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/coba/environments/
+-rw-rw-rw-   0        0        0     2286 2023-02-22 15:59:12.000000 coba-6.4.2/coba/environments/__init__.py
+-rw-rw-rw-   0        0        0    21561 2023-04-05 17:27:30.000000 coba-6.4.2/coba/environments/core.py
+-rw-rw-rw-   0        0        0    44618 2023-03-15 01:38:26.000000 coba-6.4.2/coba/environments/filters.py
+-rw-rw-rw-   0        0        0    14316 2023-02-22 16:34:05.000000 coba-6.4.2/coba/environments/openml.py
+-rw-rw-rw-   0        0        0     8220 2023-03-11 23:39:33.000000 coba-6.4.2/coba/environments/primitives.py
+-rw-rw-rw-   0        0        0     2598 2023-02-22 16:34:05.000000 coba-6.4.2/coba/environments/serialized.py
+-rw-rw-rw-   0        0        0    10122 2023-02-22 16:34:56.000000 coba-6.4.2/coba/environments/supervised.py
+-rw-rw-rw-   0        0        0    24193 2023-02-22 15:59:12.000000 coba-6.4.2/coba/environments/synthetics.py
+-rw-rw-rw-   0        0        0     6179 2023-04-05 19:12:23.000000 coba-6.4.2/coba/environments/templates.py
+-rw-rw-rw-   0        0        0     1126 2022-04-27 16:17:38.000000 coba-6.4.2/coba/exceptions.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/coba/experiments/
+-rw-rw-rw-   0        0        0      859 2023-01-14 22:42:57.000000 coba-6.4.2/coba/experiments/__init__.py
+-rw-rw-rw-   0        0        0     9404 2023-04-05 18:43:13.000000 coba-6.4.2/coba/experiments/core.py
+-rw-rw-rw-   0        0        0     9302 2023-04-05 19:38:54.000000 coba-6.4.2/coba/experiments/process.py
+-rw-rw-rw-   0        0        0    52988 2023-04-05 18:54:33.000000 coba-6.4.2/coba/experiments/results.py
+-rw-rw-rw-   0        0        0    25294 2023-03-15 01:58:08.000000 coba-6.4.2/coba/experiments/tasks.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/coba/learners/
+-rw-rw-rw-   0        0        0     1120 2023-02-22 16:34:05.000000 coba-6.4.2/coba/learners/__init__.py
+-rw-rw-rw-   0        0        0     6453 2023-03-15 01:04:42.000000 coba-6.4.2/coba/learners/bandit.py
+-rw-rw-rw-   0        0        0     7801 2023-02-22 16:34:05.000000 coba-6.4.2/coba/learners/corral.py
+-rw-rw-rw-   0        0        0     4757 2023-04-05 18:54:39.000000 coba-6.4.2/coba/learners/linucb.py
+-rw-rw-rw-   0        0        0    14794 2023-03-01 23:52:04.000000 coba-6.4.2/coba/learners/primitives.py
+-rw-rw-rw-   0        0        0    30352 2023-03-15 02:33:32.000000 coba-6.4.2/coba/learners/vowpal.py
+-rw-rw-rw-   0        0        0     4277 2023-03-15 01:43:39.000000 coba-6.4.2/coba/multiprocessing.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/coba/pipes/
+-rw-rw-rw-   0        0        0     2394 2023-02-22 16:34:05.000000 coba-6.4.2/coba/pipes/__init__.py
+-rw-rw-rw-   0        0        0     1902 2023-02-22 16:34:05.000000 coba-6.4.2/coba/pipes/core.py
+-rw-rw-rw-   0        0        0    15360 2023-02-25 19:41:52.000000 coba-6.4.2/coba/pipes/filters.py
+-rw-rw-rw-   0        0        0    14945 2023-03-01 23:34:22.000000 coba-6.4.2/coba/pipes/multiprocessing.py
+-rw-rw-rw-   0        0        0     6622 2023-02-22 16:34:05.000000 coba-6.4.2/coba/pipes/primitives.py
+-rw-rw-rw-   0        0        0    13017 2023-02-22 16:00:21.000000 coba-6.4.2/coba/pipes/readers.py
+-rw-rw-rw-   0        0        0    18680 2023-02-22 16:34:05.000000 coba-6.4.2/coba/pipes/rows.py
+-rw-rw-rw-   0        0        0     3734 2023-03-01 23:34:22.000000 coba-6.4.2/coba/pipes/sinks.py
+-rw-rw-rw-   0        0        0     6154 2023-03-01 23:34:22.000000 coba-6.4.2/coba/pipes/sources.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/coba/primitives/
+-rw-rw-rw-   0        0        0      870 2023-03-11 21:43:20.000000 coba-6.4.2/coba/primitives/__init__.py
+-rw-rw-rw-   0        0        0      930 2022-12-13 14:59:41.000000 coba-6.4.2/coba/primitives/feedbacks.py
+-rw-rw-rw-   0        0        0     6432 2023-03-11 21:54:59.000000 coba-6.4.2/coba/primitives/rewards.py
+-rw-rw-rw-   0        0        0     4425 2023-02-22 16:34:05.000000 coba-6.4.2/coba/primitives/rows.py
+-rw-rw-rw-   0        0        0      234 2022-12-13 01:57:20.000000 coba-6.4.2/coba/primitives/semantic.py
+-rw-rw-rw-   0        0        0      556 2023-02-22 16:34:05.000000 coba-6.4.2/coba/primitives/types.py
+-rw-rw-rw-   0        0        0    10887 2023-03-12 00:39:45.000000 coba-6.4.2/coba/random.py
+-rw-rw-rw-   0        0        0     1405 2023-02-22 15:59:12.000000 coba-6.4.2/coba/register.py
+-rw-rw-rw-   0        0        0    10657 2022-05-30 19:08:09.000000 coba-6.4.2/coba/registry.py
+-rw-rw-rw-   0        0        0     7199 2023-03-01 23:34:22.000000 coba-6.4.2/coba/statistics.py
+-rw-rw-rw-   0        0        0     4504 2023-01-14 22:42:57.000000 coba-6.4.2/coba/utilities.py
+drwxrwxrwx   0        0        0        0 2023-04-06 14:58:16.000000 coba-6.4.2/coba.egg-info/
+-rw-rw-rw-   0        0        0     7956 2023-04-06 14:58:16.000000 coba-6.4.2/coba.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1466 2023-04-06 14:58:16.000000 coba-6.4.2/coba.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 14:58:16.000000 coba-6.4.2/coba.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       37 2023-04-06 14:58:16.000000 coba-6.4.2/coba.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       91 2023-04-06 14:58:16.000000 coba-6.4.2/coba.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        5 2023-04-06 14:58:16.000000 coba-6.4.2/coba.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 14:58:16.000000 coba-6.4.2/setup.cfg
+-rw-rw-rw-   0        0        0     1273 2023-04-06 14:28:50.000000 coba-6.4.2/setup.py
```

### Comparing `coba-6.4.1/LICENSE` & `coba-6.4.2/LICENSE`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/PKG-INFO` & `coba-6.4.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: coba
-Version: 6.4.1
+Version: 6.4.2
 Summary: A contextual bandit research package.
 Home-page: https://github.com/VowpalWabbit/coba
 Author: Mark Rucker
 Author-email: rucker.mark@gmail.com
 License: BSD 3-Clause License
 Platform: UNKNOWN
 Classifier: Intended Audience :: Science/Research
```

### Comparing `coba-6.4.1/README.md` & `coba-6.4.2/README.md`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/__init__.py` & `coba-6.4.2/coba/__init__.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/contexts/__init__.py` & `coba-6.4.2/coba/contexts/__init__.py`

 * *Files 14% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 This module should not be confused with the idea of "context" within Contextual Bandit problems.
 This is simply context relevant to framework functions at various scopes. For developers who have
 experience with other frameworks these are similar in kind to ThreadContext, DbContext, or ServerContext.
 """
 
 from coba.contexts.cachers import Cacher, NullCacher, MemoryCacher, DiskCacher, ConcurrentCacher
-from coba.contexts.loggers import Logger, NullLogger, BasicLogger, IndentLogger, ExceptLog, NameLog, StampLog, DecoratedLogger
+from coba.contexts.loggers import Logger, NullLogger, BasicLogger, IndentLogger, ExceptionLogger, ExceptLog, NameLog, StampLog, DecoratedLogger
 from coba.contexts.core    import CobaContext, ExperimentConfig
 
 __all__ =[
     'CobaContext',
     'ExperimentConfig',
     'NullCacher',
     'MemoryCacher',
@@ -20,9 +20,10 @@
     'NullLogger',
     'BasicLogger',
     'IndentLogger',
     'ExceptLog',
     'NameLog',
     'StampLog',
     'DecoratedLogger',
+    'ExceptionLogger',
     'Logger'
 ]
```

### Comparing `coba-6.4.1/coba/contexts/cachers.py` & `coba-6.4.2/coba/contexts/cachers.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/contexts/core.py` & `coba-6.4.2/coba/contexts/core.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/contexts/loggers.py` & `coba-6.4.2/coba/contexts/loggers.py`

 * *Files 9% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 import time
 import traceback
 
 from abc import abstractmethod, ABC
 from multiprocessing import current_process
-from contextlib import contextmanager
+from contextlib import contextmanager, nullcontext
 from datetime import datetime
 from typing import ContextManager, Iterator, Sequence, Union
+from copy import copy
 
 from coba.pipes import Pipes, Filter, Sink, NullSink, ConsoleSink, Identity
 from coba.exceptions import CobaException
 
 class Logger(ABC):
     """The interface for a logger."""
 
@@ -47,34 +48,35 @@
             A ContextManager that indicates when to stop timing.
         """
         ...
 
 class NullLogger(Logger):
     """A logger which writes nothing."""
 
-    def __init__(self) -> None:
-        self._sink = NullSink()
+    def __init__(self, sink: Sink[str] = NullSink()) -> None:
+        """Instantiate a NullLogger.
 
-    @contextmanager
-    def _context(self) -> 'Iterator[Logger]':
-        yield self
+        Args:
+            sink: The sink to write to (by default null).
+        """
+        self._sink = sink
 
     @property
     def sink(self) -> Sink[str]:
         return self._sink
 
     @sink.setter
     def sink(self, sink: Sink[str]):
         self._sink = sink
 
     def log(self, message: Union[str,Exception]) -> 'ContextManager[Logger]':
-        return self._context()
+        return nullcontext(self)
 
     def time(self, message: str) -> 'ContextManager[Logger]':
-        return self._context()
+        return nullcontext(self)
 
 class BasicLogger(Logger):
     """A Logger with flat hierarchy and separate begin/end messages."""
 
     def __init__(self, sink: Sink[str] = ConsoleSink()):
         """Instantiate a BasicLogger.
 
@@ -203,49 +205,76 @@
             self._sink.write(self._level_message(message))
 
         return self._indent_context()
 
     def time(self, message: str) -> 'ContextManager[Logger]':
         return self._time_context(message)
 
+class ExceptionLogger(Logger):
+    """A Logger that only logs exceptions."""
+
+    def __init__(self, sink: Sink[str] = ConsoleSink()):
+        """Instantiate an ExceptionLogger.
+
+        Args:
+            sink: The sink to write the logs to (by default console).
+        """
+        self._sink = sink
+        self._filter = ExceptLog()
+
+    @property
+    def sink(self) -> Sink[str]:
+        return self._sink
+
+    @sink.setter
+    def sink(self, sink: Sink[str]):
+        self._sink = sink
+
+    def log(self, message: Union[str,Exception]) -> 'ContextManager[Logger]':
+        if isinstance(message,Exception):
+            self._sink.write(self._filter.filter(message))
+        return nullcontext(self)
+
+    def time(self, message: str) -> 'ContextManager[Logger]':
+        return nullcontext(self)
+
 class DecoratedLogger(Logger):
     """A Logger which decorates a base logger."""
 
     def __init__(self, pre_decorators: Sequence[Filter], logger: Logger, post_decorators: Sequence[Filter]):
         """Instantiate DecoratedLogger.
 
         Args:
             pre_decorators: A sequence of decorators to be applied before the base logger.
             logger: The base logger we are decorating.
             post_decorators: A sequence of decorators to be applied after the base logger.
         """
 
-        self._pre_decorator        = Pipes.join(*pre_decorators) if pre_decorators else Identity()
-        self._post_decorators      = post_decorators
-        self._original_logger      = logger
-        self._original_sink        = self._original_logger.sink
-        self._original_logger.sink = Pipes.join(*post_decorators, self._original_sink)
+        self._pre_decorator    = Pipes.join(*pre_decorators) if pre_decorators else Identity()
+        self._post_decorators  = post_decorators
+        self._original_logger  = logger
+        self._copy_logger      = copy(logger)
+        self._copy_logger.sink = Pipes.join(*post_decorators, logger.sink)
 
     @property
     def sink(self) -> Sink[str]:
-        return self._original_sink
+        return self._original_logger.sink
 
     @sink.setter
     def sink(self, sink: Sink[str]):
-        self._original_sink = sink
-        self._original_logger.sink   = Pipes.join(*self._post_decorators, sink)
+        self._original_logger.sink = sink
+        self._copy_logger.sink     = Pipes.join(*self._post_decorators, sink)
 
     def log(self, message: Union[str,Exception]) -> 'ContextManager[Logger]':
-        return self._original_logger.log(self._pre_decorator.filter(message))
+        return self._copy_logger.log(self._pre_decorator.filter(message))
 
     def time(self, message: str) -> 'ContextManager[Logger]':
-        return self._original_logger.time(self._pre_decorator.filter(message))
+        return self._copy_logger.time(self._pre_decorator.filter(message))
 
     def undecorate(self) -> Logger:
-        self._original_logger.sink = self._original_sink
         return self._original_logger
 
 class NameLog(Filter[str,str]):
     """A log decorator that names the process writing the log."""
 
     def filter(self, log: str) -> str:
         return f"pid-{current_process().pid:<6} -- {log}"
```

### Comparing `coba-6.4.1/coba/encodings.py` & `coba-6.4.2/coba/encodings.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/environments/__init__.py` & `coba-6.4.2/coba/environments/__init__.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/environments/core.py` & `coba-6.4.2/coba/environments/core.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/environments/filters.py` & `coba-6.4.2/coba/environments/filters.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/environments/openml.py` & `coba-6.4.2/coba/environments/openml.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/environments/primitives.py` & `coba-6.4.2/coba/environments/primitives.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/environments/serialized.py` & `coba-6.4.2/coba/environments/serialized.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/environments/supervised.py` & `coba-6.4.2/coba/environments/supervised.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/environments/synthetics.py` & `coba-6.4.2/coba/environments/synthetics.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/environments/templates.py` & `coba-6.4.2/coba/environments/templates.py`

 * *Files 2% similar despite different names*

```diff
@@ -101,14 +101,17 @@
 
         missing = set(self._missing(recipes))
         if missing: raise CobaException(f"The following variables were not defined: [{','.join(missing)}]")
 
         environments = []
         for recipe in recipes:
             environments.extend(self._make(recipe))
+        
+        environments = sorted(environments, key= lambda env: env.params.get("shuffle",0))
+
         return environments
     
     def _make(self, item:Union[str,list,dict] ) -> Sequence[Any]:
         
         result = item
 
         if isinstance(item, str):
```

### Comparing `coba-6.4.1/coba/exceptions.py` & `coba-6.4.2/coba/exceptions.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/experiments/__init__.py` & `coba-6.4.2/coba/experiments/__init__.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/experiments/core.py` & `coba-6.4.2/coba/experiments/core.py`

 * *Files 2% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from itertools import product
 from typing import Sequence, Optional, Union, overload, Tuple
 
 from coba.pipes import Pipes
 from coba.learners import Learner
 from coba.environments import Environment
 from coba.multiprocessing import CobaMultiprocessor
-from coba.contexts import CobaContext, ExceptLog, StampLog, NameLog, DecoratedLogger, NullLogger
+from coba.contexts import CobaContext, ExceptLog, StampLog, NameLog, DecoratedLogger, ExceptionLogger
 from coba.exceptions import CobaException
 
 from coba.experiments.process import CreateWorkItems,  RemoveFinished, ChunkByChunk, MaxChunkSize, ProcessWorkItems
 from coba.experiments.tasks   import EnvironmentTask, EvaluationTask, LearnerTask
 from coba.experiments.tasks   import SimpleLearnerInfo, SimpleEnvironmentInfo, SimpleEvaluation
 from coba.experiments.results import Result, TransactionIO
 
@@ -132,20 +132,20 @@
             seed: The seed that will determine all randomness within the experiment.
         """
         mp, mc, mt = (processes or self.processes), self.maxchunksperchild, self.maxtasksperchunk
 
         CobaContext.store['experiment_seed'] = seed
         is_multiproc = mp > 1 or mc != 0
 
-        if quiet: 
-            old_logger = CobaContext.logger
-            CobaContext.logger = NullLogger()
+        old_logger = CobaContext.logger
 
-        #Add name so that we know which process-id the logs came from in addition to the time of the log
-        CobaContext.logger = DecoratedLogger([ExceptLog()], CobaContext.logger, [NameLog(),StampLog()] if is_multiproc else [StampLog()])
+        if quiet:
+            CobaContext.logger = DecoratedLogger([], ExceptionLogger(CobaContext.logger.sink), [NameLog(),StampLog()] if is_multiproc else [StampLog()])
+        else:
+            CobaContext.logger = DecoratedLogger([ExceptLog()], CobaContext.logger, [NameLog(),StampLog()] if is_multiproc else [StampLog()])
 
         if result_file and Path(result_file).exists():
             CobaContext.logger.log("Restoring existing experiment logs...")
             restored = Result.from_file(result_file)
         else:
             restored = None
 
@@ -169,18 +169,15 @@
 
         except KeyboardInterrupt: # pragma: no cover
             CobaContext.logger.log("Experiment execution was manually aborted via Ctrl-C")
 
         except Exception as ex: # pragma: no cover
             CobaContext.logger.log(ex)
 
-        if isinstance(CobaContext.logger, DecoratedLogger):
-            CobaContext.logger = CobaContext.logger.undecorate()
-
-        if quiet: CobaContext.logger = old_logger
+        CobaContext.logger = old_logger
         del CobaContext.store['experiment_seed']
 
         return sink.read()
 
     def evaluate(self, result_file:str = None) -> Result:
         """Evaluate the experiment and return the results (this is a backwards compatible proxy for the run method).
```

### Comparing `coba-6.4.1/coba/experiments/process.py` & `coba-6.4.2/coba/experiments/process.py`

 * *Files 1% similar despite different names*

```diff
@@ -191,14 +191,15 @@
                                 empty_envs.add(item.env_id)
                                 continue
 
                             with CobaContext.logger.time(f"Evaluating Learner {item.lrn_id} on Environment {item.env_id}..."):
                                 lrn = item.lrn if not item.copy else deepcopy(item.lrn)
                                 row = list(item.task.process(lrn, finalizer.filter(interactions)))
                                 yield ["T3", (item.env_id, item.lrn_id), row]
+                                if hasattr(lrn,'finish') and item.copy: lrn.finish()
 
                     except Exception as e:
                         CobaContext.logger.log(e)
 
     # def _cache_ids(self, item: WorkItem) -> Tuple[int,...]:
         #I'm not sure this is necessary and it makes sorting by env-ids difficult which 
         #isn't necessary but is nice to have when you're running experiments on a single
```

### Comparing `coba-6.4.1/coba/experiments/results.py` & `coba-6.4.2/coba/experiments/results.py`

 * *Files 0% similar despite different names*

```diff
@@ -18,15 +18,15 @@
 from coba.utilities import PackageChecker
 from coba.pipes import Pipes, Sink, Source, JsonEncode, JsonDecode, DiskSource, DiskSink, IterableSource, ListSink, Foreach
 
 def exponential_moving_average(values:Sequence[float], span:int=None) -> Iterable[float]:
     #exponential moving average identical to Pandas df.ewm(span=span).mean()
     alpha = 2/(1+span)
     cumwindow  = list(accumulate(values          , lambda a,v: v + (1-alpha)*a))
-    cumdivisor = list(accumulate([1.]*len(values), lambda a,v: v + (1-alpha)*a)) #type: ignore
+    cumdivisor = list(accumulate([1.]*len(values), lambda a,v: v + (1-alpha)*a))
     return map(truediv, cumwindow, cumdivisor)
 
 def moving_average(values:Sequence[float], span:int=None) -> Iterable[float]:
 
     if span == 1:
         return values
 
@@ -360,15 +360,15 @@
 
         return Table(self, keep)
 
     def to_pandas(self) -> Any:
         """Turn the Table into a Pandas data frame."""
 
         PackageChecker.pandas("Table.to_pandas")
-        import pandas as pd #type: ignore
+        import pandas as pd
         return pd.DataFrame(self.row_values(), columns=self.col_names)
 
     def to_dicts(self) -> Sequence[Mapping[str,Any]]:
         """Turn the Table into a sequence of tuples."""
         return [dict(zip(self.col_names,row)) for row in self]
 
     def __iter__(self) -> Iterator[Sequence[Any]]:
@@ -597,15 +597,15 @@
         out: Union[None,Literal['screen'],str]
     ) -> None:
 
         xlim = xlim or [None,None]
         ylim = ylim or [None,None]
 
         PackageChecker.matplotlib('Result.plot_learners')
-        import matplotlib.pyplot as plt #type: ignore
+        import matplotlib.pyplot as plt
 
         color_cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']
 
         ax: plt.Axes
 
         bad_xlim  = xlim and xlim[0] is not None and xlim[1] is not None and xlim[0] >= xlim[1]
         bad_ylim  = ylim and ylim[0] is not None and ylim[1] is not None and ylim[0] >= ylim[1]
@@ -683,15 +683,15 @@
                 scale = 0.65
                 box1 = ax.get_position()
                 ax.set_position([box1.x0, box1.y0 + box1.height * (1-scale), box1.width, box1.height * scale])
             else:
                 ax.get_legend().remove()
 
             if any_label:
-                ax.legend(*ax.get_legend_handles_labels(), loc='upper left', bbox_to_anchor=(-.01, -.25), ncol=1, fontsize='medium') #type: ignore
+                ax.legend(*ax.get_legend_handles_labels(), loc='upper left', bbox_to_anchor=(-.01, -.25), ncol=1, fontsize='medium')
 
             if not xticks:
                 plt.xticks([])
 
             if not yticks:
                 plt.yticks([])
```

### Comparing `coba-6.4.1/coba/experiments/tasks.py` & `coba-6.4.2/coba/experiments/tasks.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/learners/__init__.py` & `coba-6.4.2/coba/learners/__init__.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/learners/bandit.py` & `coba-6.4.2/coba/learners/bandit.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/learners/corral.py` & `coba-6.4.2/coba/learners/corral.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/learners/linucb.py` & `coba-6.4.2/coba/learners/linucb.py`

 * *Files 1% similar despite different names*

```diff
@@ -53,15 +53,15 @@
 
     @property
     def params(self) -> Dict[str, Any]:
         return {'family': 'LinUCB', 'alpha': self._alpha, 'features': self._X}
 
     def predict(self, context: Context, actions: Actions) -> PMF:
 
-        import numpy as np #type: ignore
+        import numpy as np
 
         if isinstance(actions[0], dict) or isinstance(context, dict):
             raise CobaException("Sparse data cannot be handled by this implementation at this time.")
 
         if not context:
             self._X_encoder = InteractionsEncoder(list(set(filter(None,[ f.replace('x','') if isinstance(f,str) else f for f in self._X ]))))
```

### Comparing `coba-6.4.1/coba/learners/primitives.py` & `coba-6.4.2/coba/learners/primitives.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/learners/vowpal.py` & `coba-6.4.2/coba/learners/vowpal.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/multiprocessing.py` & `coba-6.4.2/coba/multiprocessing.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/pipes/__init__.py` & `coba-6.4.2/coba/pipes/__init__.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/pipes/core.py` & `coba-6.4.2/coba/pipes/core.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/pipes/filters.py` & `coba-6.4.2/coba/pipes/filters.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/pipes/multiprocessing.py` & `coba-6.4.2/coba/pipes/multiprocessing.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/pipes/primitives.py` & `coba-6.4.2/coba/pipes/primitives.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/pipes/readers.py` & `coba-6.4.2/coba/pipes/readers.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/pipes/rows.py` & `coba-6.4.2/coba/pipes/rows.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/pipes/sinks.py` & `coba-6.4.2/coba/pipes/sinks.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/pipes/sources.py` & `coba-6.4.2/coba/pipes/sources.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/primitives/__init__.py` & `coba-6.4.2/coba/primitives/__init__.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/primitives/feedbacks.py` & `coba-6.4.2/coba/primitives/feedbacks.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/primitives/rewards.py` & `coba-6.4.2/coba/primitives/rewards.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/primitives/rows.py` & `coba-6.4.2/coba/primitives/rows.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/primitives/types.py` & `coba-6.4.2/coba/primitives/types.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/random.py` & `coba-6.4.2/coba/random.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/register.py` & `coba-6.4.2/coba/register.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/registry.py` & `coba-6.4.2/coba/registry.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/statistics.py` & `coba-6.4.2/coba/statistics.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba/utilities.py` & `coba-6.4.2/coba/utilities.py`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/coba.egg-info/PKG-INFO` & `coba-6.4.2/coba.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: coba
-Version: 6.4.1
+Version: 6.4.2
 Summary: A contextual bandit research package.
 Home-page: https://github.com/VowpalWabbit/coba
 Author: Mark Rucker
 Author-email: rucker.mark@gmail.com
 License: BSD 3-Clause License
 Platform: UNKNOWN
 Classifier: Intended Audience :: Science/Research
```

### Comparing `coba-6.4.1/coba.egg-info/SOURCES.txt` & `coba-6.4.2/coba.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `coba-6.4.1/setup.py` & `coba-6.4.2/setup.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,13 +1,12 @@
-# type: ignore
 import setuptools
 
 MAJOR               = 6
 MINOR               = 4
-MICRO               = 1
+MICRO               = 2
 VERSION             = f"{MAJOR}.{MINOR}.{MICRO}"
 
 with open("README.md", "r") as f:
     long_description = f.read()
 
 setuptools.setup(
     name="coba",
```

