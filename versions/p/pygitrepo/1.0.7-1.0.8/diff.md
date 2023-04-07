# Comparing `tmp/pygitrepo-1.0.7.tar.gz` & `tmp/pygitrepo-1.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pygitrepo-1.0.7.tar", last modified: Sat Apr  2 21:58:10 2022, max compression
+gzip compressed data, was "pygitrepo-1.0.8.tar", last modified: Fri Apr  7 03:07:17 2023, max compression
```

## Comparing `pygitrepo-1.0.7.tar` & `pygitrepo-1.0.8.tar`

### file list

```diff
@@ -1,72 +1,79 @@
-drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2022-04-02 21:58:10.759482 pygitrepo-1.0.7/
--rw-r--r--   0 sanhehu    (505) staff       (20)      509 2021-12-08 02:19:08.000000 pygitrepo-1.0.7/AUTHORS.rst
--rw-r--r--   0 sanhehu    (505) staff       (20)     1119 2021-12-05 15:39:36.000000 pygitrepo-1.0.7/LICENSE.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)      341 2021-12-05 15:39:36.000000 pygitrepo-1.0.7/MANIFEST.in
--rw-r--r--   0 sanhehu    (505) staff       (20)     3816 2022-04-02 21:58:10.759342 pygitrepo-1.0.7/PKG-INFO
--rw-r--r--   0 sanhehu    (505) staff       (20)     2738 2021-12-10 02:25:55.000000 pygitrepo-1.0.7/README.rst
--rw-r--r--   0 sanhehu    (505) staff       (20)     2797 2021-12-10 02:25:49.000000 pygitrepo-1.0.7/README_cn.rst
-drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2022-04-02 21:58:10.750826 pygitrepo-1.0.7/pygitrepo/
--rw-r--r--   0 sanhehu    (505) staff       (20)     6148 2021-12-09 02:33:59.000000 pygitrepo-1.0.7/pygitrepo/.DS_Store
--rw-r--r--   0 sanhehu    (505) staff       (20)      261 2021-12-07 23:08:20.000000 pygitrepo-1.0.7/pygitrepo/__init__.py
--rw-r--r--   0 sanhehu    (505) staff       (20)      445 2021-12-08 01:36:57.000000 pygitrepo-1.0.7/pygitrepo/__init__.pyc
-drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2022-04-02 21:58:10.754566 pygitrepo-1.0.7/pygitrepo/__pycache__/
--rw-r--r--   0 sanhehu    (505) staff       (20)      435 2021-12-07 23:08:34.000000 pygitrepo-1.0.7/pygitrepo/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)      230 2022-04-02 21:16:34.000000 pygitrepo-1.0.7/pygitrepo/__pycache__/_version.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)    25432 2022-04-02 21:13:32.000000 pygitrepo-1.0.7/pygitrepo/__pycache__/actions.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     2414 2021-12-10 02:48:38.000000 pygitrepo-1.0.7/pygitrepo/__pycache__/cli.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     2092 2021-12-10 01:32:24.000000 pygitrepo-1.0.7/pygitrepo/__pycache__/color_print.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)      278 2021-12-10 00:39:17.000000 pygitrepo-1.0.7/pygitrepo/__pycache__/constants.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     5542 2021-12-10 01:13:07.000000 pygitrepo-1.0.7/pygitrepo/__pycache__/helpers.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)      939 2021-12-10 00:39:17.000000 pygitrepo-1.0.7/pygitrepo/__pycache__/operation_system.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)    22907 2022-04-02 21:09:55.000000 pygitrepo-1.0.7/pygitrepo/__pycache__/repo_config.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)       93 2022-04-02 21:14:31.000000 pygitrepo-1.0.7/pygitrepo/_version.py
--rw-r--r--   0 sanhehu    (505) staff       (20)      190 2021-12-08 01:36:57.000000 pygitrepo-1.0.7/pygitrepo/_version.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)    39332 2022-04-02 21:48:09.000000 pygitrepo-1.0.7/pygitrepo/actions.py
--rw-r--r--   0 sanhehu    (505) staff       (20)    28225 2021-12-08 02:09:27.000000 pygitrepo-1.0.7/pygitrepo/actions.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     2807 2021-12-10 02:47:39.000000 pygitrepo-1.0.7/pygitrepo/cli.py
--rw-r--r--   0 sanhehu    (505) staff       (20)     1733 2021-12-10 01:32:20.000000 pygitrepo-1.0.7/pygitrepo/color_print.py
--rw-r--r--   0 sanhehu    (505) staff       (20)     2218 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/color_print.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)      132 2021-12-10 00:28:13.000000 pygitrepo-1.0.7/pygitrepo/constants.py
--rw-r--r--   0 sanhehu    (505) staff       (20)      242 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/constants.pyc
-drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2022-04-02 21:58:10.754707 pygitrepo-1.0.7/pygitrepo/docs/
--rw-r--r--   0 sanhehu    (505) staff       (20)       43 2021-12-06 01:31:01.000000 pygitrepo-1.0.7/pygitrepo/docs/__init__.py
-drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2022-04-02 21:58:10.754950 pygitrepo-1.0.7/pygitrepo/docs/__pycache__/
--rw-r--r--   0 sanhehu    (505) staff       (20)      186 2021-12-06 01:33:28.000000 pygitrepo-1.0.7/pygitrepo/docs/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     5493 2021-12-10 01:06:08.000000 pygitrepo-1.0.7/pygitrepo/helpers.py
--rw-r--r--   0 sanhehu    (505) staff       (20)     5969 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/helpers.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     1236 2021-12-10 00:39:12.000000 pygitrepo-1.0.7/pygitrepo/operation_system.py
--rw-r--r--   0 sanhehu    (505) staff       (20)     1122 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/operation_system.pyc
-drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2022-04-02 21:58:10.757784 pygitrepo-1.0.7/pygitrepo/pkg/
--rw-r--r--   0 sanhehu    (505) staff       (20)      160 2021-12-06 01:31:01.000000 pygitrepo-1.0.7/pygitrepo/pkg/__init__.py
--rw-r--r--   0 sanhehu    (505) staff       (20)      313 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/pkg/__init__.pyc
-drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2022-04-02 21:58:10.759036 pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/
--rw-r--r--   0 sanhehu    (505) staff       (20)      306 2021-12-06 01:33:19.000000 pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)    37735 2021-12-08 01:24:53.000000 pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/configirl.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     7173 2021-12-06 02:13:41.000000 pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/fingerprint.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     2071 2021-12-06 01:33:19.000000 pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/mini_colorma.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     2252 2021-12-06 02:35:01.000000 pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/mini_six.cpython-38.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)    37429 2021-12-06 01:31:01.000000 pygitrepo-1.0.7/pygitrepo/pkg/configirl.py
--rw-r--r--   0 sanhehu    (505) staff       (20)    44629 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/pkg/configirl.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     6794 2021-12-06 01:31:01.000000 pygitrepo-1.0.7/pygitrepo/pkg/fingerprint.py
--rw-r--r--   0 sanhehu    (505) staff       (20)     8795 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/pkg/fingerprint.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     1824 2021-12-06 01:31:01.000000 pygitrepo-1.0.7/pygitrepo/pkg/mini_colorma.py
--rw-r--r--   0 sanhehu    (505) staff       (20)     2827 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/pkg/mini_colorma.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)     1940 2021-12-06 02:34:24.000000 pygitrepo-1.0.7/pygitrepo/pkg/mini_six.py
--rw-r--r--   0 sanhehu    (505) staff       (20)     3367 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/pkg/mini_six.pyc
--rw-r--r--   0 sanhehu    (505) staff       (20)    22182 2022-04-02 21:44:21.000000 pygitrepo-1.0.7/pygitrepo/repo_config.py
--rw-r--r--   0 sanhehu    (505) staff       (20)    26056 2021-12-08 01:36:58.000000 pygitrepo-1.0.7/pygitrepo/repo_config.pyc
-drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2022-04-02 21:58:10.751701 pygitrepo-1.0.7/pygitrepo.egg-info/
--rw-r--r--   0 sanhehu    (505) staff       (20)     3816 2022-04-02 21:58:10.000000 pygitrepo-1.0.7/pygitrepo.egg-info/PKG-INFO
--rw-r--r--   0 sanhehu    (505) staff       (20)     1840 2022-04-02 21:58:10.000000 pygitrepo-1.0.7/pygitrepo.egg-info/SOURCES.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)        1 2022-04-02 21:58:10.000000 pygitrepo-1.0.7/pygitrepo.egg-info/dependency_links.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)       44 2022-04-02 21:58:10.000000 pygitrepo-1.0.7/pygitrepo.egg-info/entry_points.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)      182 2022-04-02 21:58:10.000000 pygitrepo-1.0.7/pygitrepo.egg-info/requires.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)       10 2022-04-02 21:58:10.000000 pygitrepo-1.0.7/pygitrepo.egg-info/top_level.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)     3272 2022-04-02 21:49:24.000000 pygitrepo-1.0.7/release-history.rst
--rw-r--r--   0 sanhehu    (505) staff       (20)      284 2021-12-11 02:21:30.000000 pygitrepo-1.0.7/requirements-dev.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)      620 2021-12-06 01:34:39.000000 pygitrepo-1.0.7/requirements-doc.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)      254 2021-12-08 23:28:48.000000 pygitrepo-1.0.7/requirements-test.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)        0 2021-12-08 01:10:37.000000 pygitrepo-1.0.7/requirements.txt
--rw-r--r--   0 sanhehu    (505) staff       (20)       38 2022-04-02 21:58:10.759538 pygitrepo-1.0.7/setup.cfg
--rw-r--r--   0 sanhehu    (505) staff       (20)     7805 2021-12-07 23:08:26.000000 pygitrepo-1.0.7/setup.py
--rw-r--r--   0 sanhehu    (505) staff       (20)       10 2021-12-10 00:43:11.000000 pygitrepo-1.0.7/tmp.txt
+drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2023-04-07 03:07:17.964242 pygitrepo-1.0.8/
+-rw-r--r--   0 sanhehu    (505) staff       (20)      509 2021-12-08 02:19:08.000000 pygitrepo-1.0.8/AUTHORS.rst
+-rw-r--r--   0 sanhehu    (505) staff       (20)     1119 2021-12-05 15:39:36.000000 pygitrepo-1.0.8/LICENSE.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)      341 2021-12-05 15:39:36.000000 pygitrepo-1.0.8/MANIFEST.in
+-rw-r--r--   0 sanhehu    (505) staff       (20)     3814 2023-04-07 03:07:17.964094 pygitrepo-1.0.8/PKG-INFO
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2738 2021-12-10 02:25:55.000000 pygitrepo-1.0.8/README.rst
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2797 2021-12-10 02:25:49.000000 pygitrepo-1.0.8/README_cn.rst
+drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2023-04-07 03:07:17.952457 pygitrepo-1.0.8/pygitrepo/
+-rw-r--r--   0 sanhehu    (505) staff       (20)     6148 2022-05-17 21:31:44.000000 pygitrepo-1.0.8/pygitrepo/.DS_Store
+-rw-r--r--   0 sanhehu    (505) staff       (20)      261 2021-12-07 23:08:20.000000 pygitrepo-1.0.8/pygitrepo/__init__.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)      445 2021-12-08 01:36:57.000000 pygitrepo-1.0.8/pygitrepo/__init__.pyc
+drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2023-04-07 03:07:17.956306 pygitrepo-1.0.8/pygitrepo/__pycache__/
+-rw-r--r--   0 sanhehu    (505) staff       (20)      435 2021-12-07 23:08:34.000000 pygitrepo-1.0.8/pygitrepo/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)      230 2023-04-07 03:07:17.000000 pygitrepo-1.0.8/pygitrepo/__pycache__/_version.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)    25626 2022-04-02 22:03:11.000000 pygitrepo-1.0.8/pygitrepo/__pycache__/actions.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2414 2021-12-10 02:48:38.000000 pygitrepo-1.0.8/pygitrepo/__pycache__/cli.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2092 2021-12-10 01:32:24.000000 pygitrepo-1.0.8/pygitrepo/__pycache__/color_print.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)      278 2021-12-10 00:39:17.000000 pygitrepo-1.0.8/pygitrepo/__pycache__/constants.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     5542 2021-12-10 01:13:07.000000 pygitrepo-1.0.8/pygitrepo/__pycache__/helpers.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)      939 2021-12-10 00:39:17.000000 pygitrepo-1.0.8/pygitrepo/__pycache__/operation_system.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)    22991 2022-04-02 21:59:35.000000 pygitrepo-1.0.8/pygitrepo/__pycache__/repo_config.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)       93 2023-04-07 03:04:15.000000 pygitrepo-1.0.8/pygitrepo/_version.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)      190 2021-12-08 01:36:57.000000 pygitrepo-1.0.8/pygitrepo/_version.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)    39536 2023-04-07 02:58:53.000000 pygitrepo-1.0.8/pygitrepo/actions.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)    28225 2021-12-08 02:09:27.000000 pygitrepo-1.0.8/pygitrepo/actions.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2807 2021-12-10 02:47:39.000000 pygitrepo-1.0.8/pygitrepo/cli.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)     1733 2021-12-10 01:32:20.000000 pygitrepo-1.0.8/pygitrepo/color_print.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2218 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/color_print.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)      132 2021-12-10 00:28:13.000000 pygitrepo-1.0.8/pygitrepo/constants.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)      242 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/constants.pyc
+drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2023-04-07 03:07:17.956698 pygitrepo-1.0.8/pygitrepo/docs/
+-rw-r--r--   0 sanhehu    (505) staff       (20)       43 2021-12-06 01:31:01.000000 pygitrepo-1.0.8/pygitrepo/docs/__init__.py
+drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2023-04-07 03:07:17.956989 pygitrepo-1.0.8/pygitrepo/docs/__pycache__/
+-rw-r--r--   0 sanhehu    (505) staff       (20)      186 2021-12-06 01:33:28.000000 pygitrepo-1.0.8/pygitrepo/docs/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     5493 2021-12-10 01:06:08.000000 pygitrepo-1.0.8/pygitrepo/helpers.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)     5969 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/helpers.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     1236 2021-12-10 00:39:12.000000 pygitrepo-1.0.8/pygitrepo/operation_system.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)     1122 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/operation_system.pyc
+drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2023-04-07 03:07:17.960471 pygitrepo-1.0.8/pygitrepo/pkg/
+-rw-r--r--   0 sanhehu    (505) staff       (20)      160 2021-12-06 01:31:01.000000 pygitrepo-1.0.8/pygitrepo/pkg/__init__.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)      313 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/pkg/__init__.pyc
+drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2023-04-07 03:07:17.962259 pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/
+-rw-r--r--   0 sanhehu    (505) staff       (20)      306 2021-12-06 01:33:19.000000 pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)    37735 2021-12-08 01:24:53.000000 pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/configirl.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     7173 2021-12-06 02:13:41.000000 pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/fingerprint.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2071 2021-12-06 01:33:19.000000 pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/mini_colorma.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2252 2021-12-06 02:35:01.000000 pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/mini_six.cpython-38.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)    37429 2021-12-06 01:31:01.000000 pygitrepo-1.0.8/pygitrepo/pkg/configirl.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)    44629 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/pkg/configirl.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     6794 2021-12-06 01:31:01.000000 pygitrepo-1.0.8/pygitrepo/pkg/fingerprint.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)     8795 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/pkg/fingerprint.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     1824 2021-12-06 01:31:01.000000 pygitrepo-1.0.8/pygitrepo/pkg/mini_colorma.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2827 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/pkg/mini_colorma.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)     1940 2021-12-06 02:34:24.000000 pygitrepo-1.0.8/pygitrepo/pkg/mini_six.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)     3367 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/pkg/mini_six.pyc
+-rw-r--r--   0 sanhehu    (505) staff       (20)    22182 2022-04-02 21:44:21.000000 pygitrepo-1.0.8/pygitrepo/repo_config.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)    26056 2021-12-08 01:36:58.000000 pygitrepo-1.0.8/pygitrepo/repo_config.pyc
+drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2023-04-07 03:07:17.953806 pygitrepo-1.0.8/pygitrepo.egg-info/
+-rw-r--r--   0 sanhehu    (505) staff       (20)     3814 2023-04-07 03:07:17.000000 pygitrepo-1.0.8/pygitrepo.egg-info/PKG-INFO
+-rw-r--r--   0 sanhehu    (505) staff       (20)     1988 2023-04-07 03:07:17.000000 pygitrepo-1.0.8/pygitrepo.egg-info/SOURCES.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)        1 2023-04-07 03:07:17.000000 pygitrepo-1.0.8/pygitrepo.egg-info/dependency_links.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)       43 2023-04-07 03:07:17.000000 pygitrepo-1.0.8/pygitrepo.egg-info/entry_points.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)      182 2023-04-07 03:07:17.000000 pygitrepo-1.0.8/pygitrepo.egg-info/requires.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)       10 2023-04-07 03:07:17.000000 pygitrepo-1.0.8/pygitrepo.egg-info/top_level.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)     3457 2023-04-07 03:06:56.000000 pygitrepo-1.0.8/release-history.rst
+-rw-r--r--   0 sanhehu    (505) staff       (20)      284 2021-12-11 02:21:30.000000 pygitrepo-1.0.8/requirements-dev.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)      620 2021-12-06 01:34:39.000000 pygitrepo-1.0.8/requirements-doc.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)      254 2021-12-08 23:28:48.000000 pygitrepo-1.0.8/requirements-test.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)        0 2021-12-08 01:10:37.000000 pygitrepo-1.0.8/requirements.txt
+-rw-r--r--   0 sanhehu    (505) staff       (20)       38 2023-04-07 03:07:17.964290 pygitrepo-1.0.8/setup.cfg
+-rw-r--r--   0 sanhehu    (505) staff       (20)     7805 2021-12-07 23:08:26.000000 pygitrepo-1.0.8/setup.py
+drwxr-xr-x   0 sanhehu    (505) staff       (20)        0 2023-04-07 03:07:17.963811 pygitrepo-1.0.8/tests/
+-rw-r--r--   0 sanhehu    (505) staff       (20)     1875 2021-12-08 02:49:37.000000 pygitrepo-1.0.8/tests/test_actions.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2642 2021-12-06 01:31:01.000000 pygitrepo-1.0.8/tests/test_fingerprint.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)     2730 2021-12-10 00:59:16.000000 pygitrepo-1.0.8/tests/test_helpers.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)      252 2021-12-06 01:31:01.000000 pygitrepo-1.0.8/tests/test_import.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)      319 2021-12-06 01:31:01.000000 pygitrepo-1.0.8/tests/test_operation_system.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)      772 2022-04-02 21:17:49.000000 pygitrepo-1.0.8/tests/test_repo_config.py
+-rw-r--r--   0 sanhehu    (505) staff       (20)       10 2021-12-10 00:43:11.000000 pygitrepo-1.0.8/tmp.txt
```

### Comparing `pygitrepo-1.0.7/LICENSE.txt` & `pygitrepo-1.0.8/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/PKG-INFO` & `pygitrepo-1.0.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 Metadata-Version: 2.1
 Name: pygitrepo
-Version: 1.0.7
+Version: 1.0.8
 Summary: Package short description.
 Home-page: https://github.com/MacHu-GWU/
+Download-URL: https://pypi.python.org/pypi/pygitrepo/1.0.8#downloads
 Author: Sanhe Hu
 Author-email: husanhe@gmail.com
 Maintainer: Unknown
 License: MIT
-Download-URL: https://pypi.python.org/pypi/pygitrepo/1.0.7#downloads
 Platform: Windows
 Platform: MacOS
 Platform: Unix
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Natural Language :: English
@@ -104,9 +104,7 @@
     $ pip install pygitrepo
 
 To upgrade to latest version:
 
 .. code-block:: console
 
     $ pip install --upgrade pygitrepo
-
-
```

### Comparing `pygitrepo-1.0.7/README.rst` & `pygitrepo-1.0.8/README.rst`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/README_cn.rst` & `pygitrepo-1.0.8/README_cn.rst`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/.DS_Store` & `pygitrepo-1.0.8/pygitrepo/.DS_Store`

 * *Files 3% similar despite different names*

```diff
@@ -61,23 +61,23 @@
 000003c0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 000003d0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 000003e0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 000003f0: 0000 0000 0000 0000 0000 0000 0000 0000  ................
 00000400: 0000 0000 0000 0000 0000 0012 0000 000b  ................
 00000410: 005f 005f 0070 0079 0063 0061 0063 0068  ._._.p.y.c.a.c.h
 00000420: 0065 005f 005f 6c67 3153 636f 6d70 0000  .e._._lg1Scomp..
-00000430: 0000 0000 dc37 0000 000b 005f 005f 0070  .....7....._._.p
+00000430: 0000 0000 ec83 0000 000b 005f 005f 0070  ..........._._.p
 00000440: 0079 0063 0061 0063 0068 0065 005f 005f  .y.c.a.c.h.e._._
-00000450: 6d6f 4444 626c 6f62 0000 0008 cb6a 1b61  moDDblob.....j.a
-00000460: d0b0 c341 0000 000b 005f 005f 0070 0079  ...A....._._.p.y
+00000450: 6d6f 4444 626c 6f62 0000 0008 c451 c8cf  moDDblob.....Q..
+00000460: 7ffc c341 0000 000b 005f 005f 0070 0079  ...A....._._.p.y
 00000470: 0063 0061 0063 0068 0065 005f 005f 6d6f  .c.a.c.h.e._._mo
-00000480: 6444 626c 6f62 0000 0008 cb6a 1b61 d0b0  dDblob.....j.a..
+00000480: 6444 626c 6f62 0000 0008 c451 c8cf 7ffc  dDblob.....Q....
 00000490: c341 0000 000b 005f 005f 0070 0079 0063  .A....._._.p.y.c
 000004a0: 0061 0063 0068 0065 005f 005f 7068 3153  .a.c.h.e._._ph1S
-000004b0: 636f 6d70 0000 0000 0001 4000 0000 0003  comp......@.....
+000004b0: 636f 6d70 0000 0000 0001 5000 0000 0003  comp......P.....
 000004c0: 0063 006c 0069 6c67 3153 636f 6d70 0000  .c.l.ilg1Scomp..
 000004d0: 0000 0000 10a0 0000 0003 0063 006c 0069  ...........c.l.i
 000004e0: 6d6f 4444 626c 6f62 0000 0008 e1cf 19ee  moDDblob........
 000004f0: 18b0 c341 0000 0003 0063 006c 0069 6d6f  ...A.....c.l.imo
 00000500: 6444 626c 6f62 0000 0008 e1cf 19ee 18b0  dDblob..........
 00000510: c341 0000 0003 0063 006c 0069 7068 3153  .A.....c.l.iph1S
 00000520: 636f 6d70 0000 0000 0000 2000 0000 0004  comp...... .....
```

### Comparing `pygitrepo-1.0.7/pygitrepo/__pycache__/actions.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/__pycache__/actions.cpython-38.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.8, timestamp-based, .py timestamp: Sat Apr  2 21:13:26 2022 UTC, .py size: 39237 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 550d 0d0a 0000 0000 76bc 4862 4599 0000  U.......v.HbE...
+00000000: 550d 0d0a 0000 0000 17c8 4862 139a 0000  U.........Hb....
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0008 0000 0040 0000 0073 0e01 0000 6400  .....@...s....d.
 00000030: 5a00 6401 6402 6c01 6d02 5a02 6d03 5a03  Z.d.d.l.m.Z.m.Z.
 00000040: 0100 7a0c 6401 6403 6c04 5a04 5700 6e14  ..z.d.d.l.Z.W.n.
 00000050: 0400 6505 6b0a 7234 0100 0100 0100 5900  ..e.k.r4......Y.
 00000060: 6e02 5800 6401 6403 6c06 5a06 6401 6403  n.X.d.d.l.Z.d.d.
 00000070: 6c07 5a07 6401 6403 6c08 5a08 6401 6404  l.Z.d.d.l.Z.d.d.
@@ -355,1236 +355,1248 @@
 00001620: 6ce9 0000 0073 1c00 0000 0007 1601 0201  l....s..........
 00001630: 0401 0401 08fe 04ff 0406 0801 0401 0401  ................
 00001640: 0201 04fd 0605 7a13 4163 7469 6f6e 732e  ......z.Actions.
 00001650: 7069 705f 696e 7374 616c 6c7a 1d2a 2a20  pip_installz.** 
 00001660: 4469 7370 6c61 7920 7573 6566 756c 2069  Display useful i
 00001670: 6e66 6f72 6d61 7469 6f6e 6303 0000 0000  nformationc.....
 00001680: 0000 0000 0000 0004 0000 0006 0000 004b  ...............K
-00001690: 0000 0073 b800 0000 7400 6401 6a01 7402  ...s....t.d.j.t.
+00001690: 0000 0073 bc00 0000 7400 6401 6a01 7402  ...s....t.d.j.t.
 000016a0: 6a03 7402 6a04 7402 6a05 6402 8d03 8301  j.t.j.t.j.d.....
 000016b0: 0100 7406 6403 7c01 6a07 8302 0100 7406  ..t.d.|.j.....t.
 000016c0: 6404 7c01 6a08 8302 0100 7406 6405 7c01  d.|.j.....t.d.|.
 000016d0: 6a09 8302 0100 740a 725e 740b 6406 6a01  j.....t.r^t.d.j.
 000016e0: 7402 6a03 740c 7c01 6a0d 8301 6407 8d02  t.j.t.|.j...d...
-000016f0: 8301 0100 6e28 740e 7366 740f 7282 740b  ....n(t.sft.r.t.
-00001700: 6408 6a01 7402 6a03 740c 7c01 6a0d 8301  d.j.t.j.t.|.j...
-00001710: 6407 8d02 8301 0100 6e04 7410 8201 740b  d.......n.t...t.
-00001720: 6409 6a01 7402 6a03 7411 6a12 640a 8d02  d.j.t.j.t.j.d...
-00001730: 8301 0100 7406 640b 7c01 6a13 8302 0100  ....t.d.|.j.....
-00001740: 7406 640c 7c01 6a14 8302 0100 640d 5300  t.d.|.j.....d.S.
-00001750: 290e 7234 0000 007a 507b 6379 616e 7d44  ).r4...zP{cyan}D
-00001760: 6973 706c 6179 2075 7365 6675 6c20 696e  isplay useful in
-00001770: 666f 726d 6174 696f 6e2c 207b 6772 6565  formation, {gree
-00001780: 6e7d 7061 7468 2065 7869 7374 737b 6379  n}path exists{cy
-00001790: 616e 7d2c 207b 7265 647d 7061 7468 206e  an}, {red}path n
-000017a0: 6f74 2065 7869 7374 7329 0372 3600 0000  ot exists).r6...
-000017b0: 5a05 6772 6565 6eda 0372 6564 7a1d 7669  Z.green..redz.vi
-000017c0: 7274 7561 6c20 656e 7669 726f 6e6d 656e  rtual environmen
-000017d0: 7420 6469 7265 6374 6f72 797a 1b76 656e  t directoryz.ven
-000017e0: 7620 7079 7468 6f6e 2065 7865 6375 7461  v python executa
-000017f0: 626c 6520 7061 7468 7a18 7665 6e76 2070  ble pathz.venv p
-00001800: 6970 2065 7865 6375 7461 626c 6520 7061  ip executable pa
-00001810: 7468 7a25 2d20 7b63 7961 6e7d 6163 7469  thz%- {cyan}acti
-00001820: 7661 7465 2076 656e 7620 636f 6d6d 616e  vate venv comman
-00001830: 643a 207b 7061 7468 7d29 0272 3600 0000  d: {path}).r6...
-00001840: 7242 0000 007a 2c2d 207b 6379 616e 7d61  rB...z,- {cyan}a
-00001850: 6374 6976 6174 6520 7665 6e76 2063 6f6d  ctivate venv com
-00001860: 6d61 6e64 3a20 736f 7572 6365 207b 7061  mand: source {pa
-00001870: 7468 7d7a 322d 207b 6379 616e 7d64 6561  th}z2- {cyan}dea
-00001880: 6374 6976 6174 6520 7665 6e76 2063 6f6d  ctivate venv com
-00001890: 6d61 6e64 3a20 7b72 6573 6574 7d64 6561  mand: {reset}dea
-000018a0: 6374 6976 6174 65a9 0272 3600 0000 7237  ctivate..r6...r7
-000018b0: 0000 007a 1773 6974 652d 7061 636b 6167  ...z.site-packag
-000018c0: 6573 2064 6972 6563 746f 7279 7a19 7369  es directoryz.si
-000018d0: 7465 2d70 6163 6b61 6765 7336 3420 6469  te-packages64 di
-000018e0: 7265 6374 6f72 794e 2915 7219 0000 0072  rectoryN).r....r
-000018f0: 3e00 0000 7216 0000 0072 3f00 0000 5a05  >...r....r?...Z.
-00001900: 4752 4545 4eda 0352 4544 721b 0000 0072  GREEN..REDr....r
-00001910: 3800 0000 da14 7061 7468 5f76 656e 765f  8.....path_venv_
-00001920: 6269 6e5f 7079 7468 6f6e 7246 0000 0072  bin_pythonrF...r
-00001930: 0900 0000 721c 0000 0072 1d00 0000 5a16  ....r....r....Z.
-00001940: 7061 7468 5f76 656e 765f 6269 6e5f 6163  path_venv_bin_ac
-00001950: 7469 7661 7465 720a 0000 0072 0b00 0000  tivater....r....
-00001960: da13 4e6f 7449 6d70 6c65 6d65 6e74 6564  ..NotImplemented
-00001970: 4572 726f 7272 1700 0000 7240 0000 005a  Errorr....r@...Z
-00001980: 1664 6972 5f76 656e 765f 7369 7465 5f70  .dir_venv_site_p
-00001990: 6163 6b61 6765 735a 1964 6972 5f76 656e  ackagesZ.dir_ven
-000019a0: 765f 7369 7465 5f70 6163 6b61 6765 735f  v_site_packages_
-000019b0: 3634 7247 0000 0072 2000 0000 7220 0000  64rG...r ...r ..
-000019c0: 0072 2600 0000 da04 696e 666f ff00 0000  .r&.....info....
-000019d0: 7360 0000 0000 0702 0104 0104 0104 0104  s`..............
-000019e0: fd04 ff04 0702 0102 0104 fe04 0402 0102  ................
-000019f0: 0104 fe04 0402 0102 0104 fe04 0404 0102  ................
-00001a00: 0104 0104 0108 fe04 ff06 0608 0102 0104  ................
-00001a10: 0104 0108 fe04 ff06 0704 0202 0104 0104  ................
-00001a20: 0104 fe04 ff04 0602 0102 0104 fe04 0402  ................
-00001a30: 0102 0104 fe7a 0c41 6374 696f 6e73 2e69  .....z.Actions.i
-00001a40: 6e66 6f7a 332a 2a20 496e 7374 616c 6c20  nfoz3** Install 
-00001a50: 6465 7620 6465 7065 6e64 656e 6369 6573  dev dependencies
-00001a60: 2069 6e20 7265 7175 6972 656d 656e 7473   in requirements
-00001a70: 2d64 6576 2e74 7874 6303 0000 0000 0000  -dev.txtc.......
-00001a80: 0000 0000 0004 0000 0006 0000 004b 0000  .............K..
-00001a90: 0073 4200 0000 7400 6401 6a01 7402 6a03  .sB...t.d.j.t.j.
-00001aa0: 7404 6a05 6402 8d02 8301 0100 7c02 6403  t.j.d.......|.d.
-00001ab0: 6b08 7234 7406 a007 7c01 6a08 6404 6405  k.r4t...|.j.d.d.
-00001ac0: 7c01 6a09 6704 a101 0100 740a 6406 6407  |.j.g.....t.d.d.
-00001ad0: 8d01 0100 6408 5300 a909 7234 0000 007a  ....d.S...r4...z
-00001ae0: 477b 6379 616e 7d69 6e73 7461 6c6c 2064  G{cyan}install d
-00001af0: 6570 656e 6465 6e63 6965 7320 696e 207b  ependencies in {
-00001b00: 7265 7365 747d 7265 7175 6972 656d 656e  reset}requiremen
-00001b10: 7473 2d64 6576 2e74 7874 2074 6f20 7669  ts-dev.txt to vi
-00001b20: 7274 7561 6c65 6e76 7261 0000 0046 723b  rtualenvra...Fr;
-00001b30: 0000 00fa 022d 7272 0500 0000 723c 0000  .....-rr....r<..
-00001b40: 004e 290b 7219 0000 0072 3e00 0000 7216  .N).r....r>...r.
-00001b50: 0000 0072 3f00 0000 7217 0000 0072 4000  ...r?...r....r@.
-00001b60: 0000 7244 0000 0072 4500 0000 7246 0000  ..rD...rE...rF..
-00001b70: 00da 1a70 6174 685f 7265 7175 6972 656d  ...path_requirem
-00001b80: 656e 7473 5f64 6576 5f66 696c 6572 1a00  ents_dev_filer..
-00001b90: 0000 7247 0000 0072 2000 0000 7220 0000  ..rG...r ...r ..
-00001ba0: 0072 2600 0000 da07 7265 715f 6465 7639  .r&.....req_dev9
-00001bb0: 0100 0073 1c00 0000 0007 0201 0401 0401  ...s............
-00001bc0: 04fe 04ff 0406 0801 0401 0401 0201 0201  ................
-00001bd0: 04fc 0606 7a0f 4163 7469 6f6e 732e 7265  ....z.Actions.re
-00001be0: 715f 6465 767a 3049 6e73 7461 6c6c 2064  q_devz0Install d
-00001bf0: 6f63 2064 6570 656e 6465 6e63 6965 7320  oc dependencies 
-00001c00: 696e 2072 6571 7569 7265 6d65 6e74 732d  in requirements-
-00001c10: 646f 632e 7478 7463 0300 0000 0000 0000  doc.txtc........
-00001c20: 0000 0000 0400 0000 0600 0000 4b00 0000  ............K...
-00001c30: 7342 0000 0074 0064 016a 0174 026a 0374  sB...t.d.j.t.j.t
-00001c40: 046a 0564 028d 0283 0101 007c 0264 036b  .j.d.......|.d.k
-00001c50: 0872 3474 06a0 077c 016a 0864 0464 057c  .r4t...|.j.d.d.|
-00001c60: 016a 0967 04a1 0101 0074 0a64 0664 078d  .j.g.....t.d.d..
-00001c70: 0101 0064 0853 0029 0972 3400 0000 7a47  ...d.S.).r4...zG
-00001c80: 7b63 7961 6e7d 696e 7374 616c 6c20 6465  {cyan}install de
-00001c90: 7065 6e64 656e 6369 6573 2069 6e20 7b72  pendencies in {r
-00001ca0: 6573 6574 7d72 6571 7569 7265 6d65 6e74  eset}requirement
-00001cb0: 732d 646f 632e 7478 7420 746f 2076 6972  s-doc.txt to vir
-00001cc0: 7475 616c 656e 7672 6100 0000 4672 3b00  tualenvra...Fr;.
-00001cd0: 0000 7267 0000 0072 0500 0000 723c 0000  ..rg...r....r<..
-00001ce0: 004e 290b 7219 0000 0072 3e00 0000 7216  .N).r....r>...r.
-00001cf0: 0000 0072 3f00 0000 7217 0000 0072 4000  ...r?...r....r@.
-00001d00: 0000 7244 0000 0072 4500 0000 7246 0000  ..rD...rE...rF..
-00001d10: 00da 1a70 6174 685f 7265 7175 6972 656d  ...path_requirem
-00001d20: 656e 7473 5f64 6f63 5f66 696c 6572 1a00  ents_doc_filer..
-00001d30: 0000 7247 0000 0072 2000 0000 7220 0000  ..rG...r ...r ..
-00001d40: 0072 2600 0000 da07 7265 715f 646f 634f  .r&.....req_docO
-00001d50: 0100 0073 1c00 0000 0007 0201 0401 0401  ...s............
-00001d60: 04fe 04ff 0406 0801 0401 0401 0201 0201  ................
-00001d70: 04fc 0606 7a0f 4163 7469 6f6e 732e 7265  ....z.Actions.re
-00001d80: 715f 646f 637a 3149 6e73 7461 6c6c 2064  q_docz1Install d
-00001d90: 6576 2064 6570 656e 6465 6e63 6965 7320  ev dependencies 
-00001da0: 696e 2072 6571 7569 7265 6d65 6e74 732d  in requirements-
-00001db0: 7465 7374 2e74 7874 6303 0000 0000 0000  test.txtc.......
-00001dc0: 0000 0000 0004 0000 0006 0000 004b 0000  .............K..
-00001dd0: 0073 4200 0000 7400 6401 6a01 7402 6a03  .sB...t.d.j.t.j.
-00001de0: 7404 6a05 6402 8d02 8301 0100 7c02 6403  t.j.d.......|.d.
-00001df0: 6b08 7234 7406 a007 7c01 6a08 6404 6405  k.r4t...|.j.d.d.
-00001e00: 7c01 6a09 6704 a101 0100 740a 6406 6407  |.j.g.....t.d.d.
-00001e10: 8d01 0100 6408 5300 7266 0000 0029 0b72  ....d.S.rf...).r
-00001e20: 1900 0000 723e 0000 0072 1600 0000 723f  ....r>...r....r?
-00001e30: 0000 0072 1700 0000 7240 0000 0072 4400  ...r....r@...rD.
-00001e40: 0000 7245 0000 0072 4600 0000 da1b 7061  ..rE...rF.....pa
-00001e50: 7468 5f72 6571 7569 7265 6d65 6e74 735f  th_requirements_
-00001e60: 7465 7374 5f66 696c 6572 1a00 0000 7247  test_filer....rG
-00001e70: 0000 0072 2000 0000 7220 0000 0072 2600  ...r ...r ...r&.
-00001e80: 0000 da08 7265 715f 7465 7374 6501 0000  ....req_teste...
-00001e90: 731c 0000 0000 0702 0104 0104 0104 fe04  s...............
-00001ea0: ff04 0608 0104 0104 0102 0102 0104 fc06  ................
-00001eb0: 067a 1041 6374 696f 6e73 2e72 6571 5f74  .z.Actions.req_t
-00001ec0: 6573 747a 2144 6973 706c 6179 2072 6571  estz!Display req
-00001ed0: 7569 7265 6d65 6e74 7320 6669 6c65 2063  uirements file c
-00001ee0: 6f6e 7465 6e74 6303 0000 0000 0000 0000  ontentc.........
-00001ef0: 0000 0004 0000 0005 0000 004b 0000 0073  ...........K...s
-00001f00: cc00 0000 7400 6401 6a01 7402 6a03 7404  ....t.d.j.t.j.t.
-00001f10: 6a05 6402 8d02 8301 0100 7406 8300 0100  j.d.......t.....
-00001f20: 7407 a008 6403 7c01 6a09 6702 a101 0100  t...d.|.j.g.....
-00001f30: 7406 8300 0100 7400 6404 6a01 7402 6a03  t.....t.d.j.t.j.
-00001f40: 7404 6a05 6402 8d02 8301 0100 7406 8300  t.j.d.......t...
-00001f50: 0100 7407 a008 6403 7c01 6a0a 6702 a101  ..t...d.|.j.g...
-00001f60: 0100 7406 8300 0100 7400 6405 6a01 7402  ..t.....t.d.j.t.
-00001f70: 6a03 7404 6a05 6402 8d02 8301 0100 7406  j.t.j.d.......t.
-00001f80: 8300 0100 7407 a008 6403 7c01 6a0b 6702  ....t...d.|.j.g.
-00001f90: a101 0100 7406 8300 0100 7400 6406 6a01  ....t.....t.d.j.
-00001fa0: 7402 6a03 7404 6a05 6402 8d02 8301 0100  t.j.t.j.d.......
-00001fb0: 7406 8300 0100 7407 a008 6403 7c01 6a0c  t.....t...d.|.j.
-00001fc0: 6702 a101 0100 7406 8300 0100 6407 5300  g.....t.....d.S.
-00001fd0: 2908 7234 0000 007a 2d7b 6379 616e 7d64  ).r4...z-{cyan}d
-00001fe0: 6570 656e 6465 6e63 6965 7320 696e 207b  ependencies in {
-00001ff0: 7265 7365 747d 7265 7175 6972 656d 656e  reset}requiremen
-00002000: 7473 2e74 7874 7261 0000 00da 0363 6174  ts.txtra.....cat
-00002010: 7a31 7b63 7961 6e7d 6465 7065 6e64 656e  z1{cyan}dependen
-00002020: 6369 6573 2069 6e20 7b72 6573 6574 7d72  cies in {reset}r
-00002030: 6571 7569 7265 6d65 6e74 732d 6465 762e  equirements-dev.
-00002040: 7478 747a 317b 6379 616e 7d64 6570 656e  txtz1{cyan}depen
-00002050: 6465 6e63 6965 7320 696e 207b 7265 7365  dencies in {rese
-00002060: 747d 7265 7175 6972 656d 656e 7473 2d64  t}requirements-d
-00002070: 6f63 2e74 7874 7a32 7b63 7961 6e7d 6465  oc.txtz2{cyan}de
-00002080: 7065 6e64 656e 6369 6573 2069 6e20 7b72  pendencies in {r
-00002090: 6573 6574 7d72 6571 7569 7265 6d65 6e74  eset}requirement
-000020a0: 732d 7465 7374 2e74 7874 4e29 0d72 1900  s-test.txtN).r..
-000020b0: 0000 723e 0000 0072 1600 0000 723f 0000  ..r>...r....r?..
-000020c0: 0072 1700 0000 7240 0000 00da 0570 7269  .r....r@.....pri
-000020d0: 6e74 7244 0000 0072 4500 0000 5a16 7061  ntrD...rE...Z.pa
-000020e0: 7468 5f72 6571 7569 7265 6d65 6e74 735f  th_requirements_
-000020f0: 6669 6c65 7268 0000 0072 6a00 0000 726c  filerh...rj...rl
-00002100: 0000 0072 4700 0000 7220 0000 0072 2000  ...rG...r ...r .
-00002110: 0000 7226 0000 00da 0872 6571 5f69 6e66  ..r&.....req_inf
-00002120: 6f7b 0100 0073 6000 0000 0007 0201 0401  o{...s`.........
-00002130: 0401 04fe 04ff 0406 0601 0401 0201 04fe  ................
-00002140: 0604 0602 0201 0401 0401 04fe 04ff 0406  ................
-00002150: 0601 0401 0201 04fe 0604 0602 0201 0401  ................
-00002160: 0401 04fe 04ff 0406 0601 0401 0201 04fe  ................
-00002170: 0604 0602 0201 0401 0401 04fe 04ff 0406  ................
-00002180: 0601 0401 0201 04fe 0604 7a10 4163 7469  ..........z.Acti
-00002190: 6f6e 732e 7265 715f 696e 666f 7a09 7465  ons.req_infoz.te
-000021a0: 7374 2d6f 6e6c 797a 1a52 756e 2075 6e69  st-onlyz.Run uni
-000021b0: 7420 7465 7374 2077 6974 6820 7079 7465  t test with pyte
-000021c0: 7374 2e29 0272 3000 0000 722f 0000 0063  st.).r0...r/...c
-000021d0: 0300 0000 0000 0000 0000 0000 0400 0000  ................
-000021e0: 0600 0000 4b00 0000 7344 0000 0074 0064  ....K...sD...t.d
-000021f0: 016a 0174 026a 0374 046a 057c 016a 0664  .j.t.j.t.j.|.j.d
-00002200: 028d 0383 0101 007c 0264 036b 0872 3674  .......|.d.k.r6t
-00002210: 07a0 087c 016a 097c 016a 0664 0467 03a1  ...|.j.|.j.d.g..
-00002220: 0101 0074 0a64 0564 068d 0101 0064 0753  ...t.d.d.....d.S
-00002230: 0029 0872 3400 0000 7a29 7b63 7961 6e7d  .).r4...z){cyan}
-00002240: 5275 6e20 756e 6974 2074 6573 7420 696e  Run unit test in
-00002250: 207b 7265 7365 747d 7b64 6972 5f74 6573   {reset}{dir_tes
-00002260: 7473 7da9 0372 3600 0000 7237 0000 00da  ts}..r6...r7....
-00002270: 0964 6972 5f74 6573 7473 46fa 022d 7372  .dir_testsF..-sr
-00002280: 0500 0000 723c 0000 004e 290b 7219 0000  ....r<...N).r...
-00002290: 0072 3e00 0000 7216 0000 0072 3f00 0000  .r>...r....r?...
-000022a0: 7217 0000 0072 4000 0000 7272 0000 0072  r....r@...rr...r
-000022b0: 4400 0000 7245 0000 00da 1470 6174 685f  D...rE.....path_
-000022c0: 7665 6e76 5f62 696e 5f70 7974 6573 7472  venv_bin_pytestr
-000022d0: 1a00 0000 7247 0000 0072 2000 0000 7220  ....rG...r ...r 
-000022e0: 0000 0072 2600 0000 da10 7465 7374 5f70  ...r&.....test_p
-000022f0: 7974 6573 745f 6f6e 6c79 b601 0000 731c  ytest_only....s.
-00002300: 0000 0000 0802 0104 0104 0104 0104 fd04  ................
-00002310: ff04 0708 0104 0104 0104 0102 fd06 057a  ...............z
-00002320: 1841 6374 696f 6e73 2e74 6573 745f 7079  .Actions.test_py
-00002330: 7465 7374 5f6f 6e6c 79da 0474 6573 747a  test_only..testz
-00002340: 382a 2a20 5275 6e20 756e 6974 2074 6573  8** Run unit tes
-00002350: 7420 7769 7468 2070 7974 6573 742e 2053  t with pytest. S
-00002360: 7461 7274 206f 7665 722c 2072 6575 7365  tart over, reuse
-00002370: 206e 6f74 6869 6e67 2e63 0300 0000 0000   nothing.c......
-00002380: 0000 0000 0000 0400 0000 0400 0000 4b00  ..............K.
-00002390: 0000 7358 0000 007c 006a 007c 0166 0164  ..sX...|.j.|.f.d
-000023a0: 017c 0269 017c 0397 028e 0101 007c 006a  .|.i.|.......|.j
-000023b0: 017c 0166 0164 017c 0269 017c 0397 028e  .|.f.d.|.i.|....
-000023c0: 0101 007c 0264 026b 0872 3e74 027c 016a  ...|.d.k.r>t.|.j
-000023d0: 0383 0101 007c 006a 047c 0166 0164 017c  .....|.j.|.f.d.|
-000023e0: 0269 017c 0397 028e 0101 0064 0353 00a9  .i.|.......d.S..
-000023f0: 0472 3400 0000 724a 0000 0046 4e29 0572  .r4...rJ...FN).r
-00002400: 6d00 0000 725e 0000 0072 0d00 0000 7252  m...r^...r....rR
-00002410: 0000 0072 7500 0000 7247 0000 0072 2000  ...ru...rG...r .
-00002420: 0000 7220 0000 0072 2600 0000 da0b 7465  ..r ...r&.....te
-00002430: 7374 5f70 7974 6573 74cd 0100 0073 0a00  st_pytest....s..
-00002440: 0000 0008 1601 1601 0801 0a01 7a13 4163  ............z.Ac
-00002450: 7469 6f6e 732e 7465 7374 5f70 7974 6573  tions.test_pytes
-00002460: 747a 0863 6f76 2d6f 6e6c 797a 2152 756e  tz.cov-onlyz!Run
-00002470: 2063 6f64 6520 636f 7665 7261 6765 2074   code coverage t
-00002480: 6573 7420 696e 2070 7974 6573 742e 6303  est in pytest.c.
-00002490: 0000 0000 0000 0000 0000 0004 0000 000c  ................
-000024a0: 0000 004b 0000 0073 6200 0000 7400 6401  ...K...sb...t.d.
-000024b0: 6a01 7402 6a03 7404 6a05 7c01 6a06 6402  j.t.j.t.j.|.j.d.
-000024c0: 8d03 8301 0100 7c02 6403 6b08 7254 7407  ......|.d.k.rTt.
-000024d0: a008 7c01 6a09 7c01 6a06 6404 6405 a001  ..|.j.|.j.d.d...
-000024e0: 7c01 6a0a a00b a100 a101 6406 6407 6406  |.j.......d.d.d.
-000024f0: 6408 a001 7c01 6a0c a101 6708 a101 0100  d...|.j...g.....
-00002500: 740d 6409 640a 8d01 0100 640b 5300 290c  t.d.d.....d.S.).
-00002510: 7234 0000 007a 327b 6379 616e 7d52 756e  r4...z2{cyan}Run
-00002520: 2063 6f64 6520 636f 7665 7261 6765 2074   code coverage t
-00002530: 6573 7420 696e 207b 7265 7365 747d 7b64  est in {reset}{d
-00002540: 6972 5f74 6573 7473 7d72 7100 0000 4672  ir_tests}rq...Fr
-00002550: 7300 0000 7a08 2d2d 636f 763d 7b7d 7a0c  s...z.--cov={}z.
-00002560: 2d2d 636f 762d 7265 706f 7274 7a0c 7465  --cov-reportz.te
-00002570: 726d 2d6d 6973 7369 6e67 7a07 6874 6d6c  rm-missingz.html
-00002580: 3a7b 7d72 0500 0000 723c 0000 004e 290e  :{}r....r<...N).
-00002590: 7219 0000 0072 3e00 0000 7216 0000 0072  r....r>...r....r
-000025a0: 3f00 0000 7217 0000 0072 4000 0000 7272  ?...r....r@...rr
-000025b0: 0000 0072 4400 0000 7245 0000 0072 7400  ...rD...rE...rt.
-000025c0: 0000 7259 0000 0072 5a00 0000 5a11 6469  ..rY...rZ...Z.di
-000025d0: 725f 636f 7665 7261 6765 5f68 746d 6c72  r_coverage_htmlr
-000025e0: 1a00 0000 7247 0000 0072 2000 0000 7220  ....rG...r ...r 
-000025f0: 0000 0072 2600 0000 da0d 7465 7374 5f63  ...r&.....test_c
-00002600: 6f76 5f6f 6e6c 79db 0100 0073 2600 0000  ov_only....s&...
-00002610: 0008 0201 0401 0401 0401 04fd 04ff 0407  ................
-00002620: 0801 0401 0401 0401 0201 0e01 0200 0201  ................
-00002630: 0200 0afa 0608 7a15 4163 7469 6f6e 732e  ......z.Actions.
-00002640: 7465 7374 5f63 6f76 5f6f 6e6c 795a 0363  test_cov_onlyZ.c
-00002650: 6f76 7a3f 2a2a 2052 756e 2063 6f64 6520  ovz?** Run code 
-00002660: 636f 7665 7261 6765 2074 6573 7420 696e  coverage test in
-00002670: 2070 7974 6573 742e 2053 7461 7274 206f   pytest. Start o
-00002680: 7665 722c 2072 6575 7365 206e 6f74 6869  ver, reuse nothi
-00002690: 6e67 2e63 0300 0000 0000 0000 0000 0000  ng.c............
-000026a0: 0400 0000 0400 0000 4b00 0000 7362 0000  ........K...sb..
-000026b0: 007c 006a 007c 0166 0164 017c 0269 017c  .|.j.|.f.d.|.i.|
-000026c0: 0397 028e 0101 007c 006a 017c 0166 0164  .......|.j.|.f.d
-000026d0: 017c 0269 017c 0397 028e 0101 007c 0264  .|.i.|.......|.d
-000026e0: 026b 0872 4874 027c 016a 0383 0101 0074  .k.rHt.|.j.....t
-000026f0: 027c 016a 0483 0101 007c 006a 057c 0166  .|.j.....|.j.|.f
-00002700: 0164 017c 0269 017c 0397 028e 0101 0064  .d.|.i.|.......d
-00002710: 0353 0072 7700 0000 2906 726d 0000 0072  .S.rw...).rm...r
-00002720: 5e00 0000 720d 0000 0072 5200 0000 7251  ^...r....rR...rQ
-00002730: 0000 0072 7900 0000 7247 0000 0072 2000  ...ry...rG...r .
-00002740: 0000 7220 0000 0072 2600 0000 da08 7465  ..r ...r&.....te
-00002750: 7374 5f63 6f76 f501 0000 730c 0000 0000  st_cov....s.....
-00002760: 0816 0116 0108 010a 010a 017a 1041 6374  ...........z.Act
-00002770: 696f 6e73 2e74 6573 745f 636f 767a 312a  ions.test_covz1*
-00002780: 2a20 5669 6577 2063 6f64 6520 636f 7665  * View code cove
-00002790: 7261 6765 2074 6573 7420 7265 7375 6c74  rage test result
-000027a0: 2069 6e20 7765 6220 6272 6f77 7365 722e   in web browser.
-000027b0: 6303 0000 0000 0000 0000 0000 0004 0000  c...............
-000027c0: 0006 0000 004b 0000 0073 5600 0000 7400  .....K...sV...t.
-000027d0: 6401 6a01 7402 6a03 7404 6a05 7c01 6a06  d.j.t.j.t.j.|.j.
-000027e0: 6402 8d03 8301 0100 7407 6a08 a009 7c01  d.......t.j...|.
-000027f0: 6a06 a101 7330 740a 6403 8301 8201 7c02  j...s0t.d.....|.
-00002800: 6404 6b08 7248 740b a00c 740d 7c01 6a06  d.k.rHt...t.|.j.
-00002810: 6702 a101 0100 740e 6405 6406 8d01 0100  g.....t.d.d.....
-00002820: 6407 5300 2908 7234 0000 007a 4f7b 6379  d.S.).r4...zO{cy
-00002830: 616e 7d4f 7065 6e20 636f 6465 2063 6f76  an}Open code cov
-00002840: 6572 6167 6520 7465 7374 2068 746d 6c20  erage test html 
-00002850: 7265 7375 6c74 2069 6e20 7765 6220 6272  result in web br
-00002860: 6f77 7365 727b 7265 7365 747d 7b63 6f76  owser{reset}{cov
-00002870: 5f68 746d 6c5f 696e 6465 787d 2903 7236  _html_index}).r6
-00002880: 0000 0072 3700 0000 5a0e 636f 765f 6874  ...r7...Z.cov_ht
-00002890: 6d6c 5f69 6e64 6578 7a4a 636f 6465 2063  ml_indexzJcode c
-000028a0: 6f76 6572 6167 6520 7465 7374 2072 6573  overage test res
-000028b0: 756c 7473 206e 6f74 2061 7661 696c 6162  ults not availab
-000028c0: 6c65 2079 6574 2c20 796f 7520 6d61 7920  le yet, you may 
-000028d0: 7275 6e20 2770 6772 2063 6f76 2720 6669  run 'pgr cov' fi
-000028e0: 7273 7421 4672 0500 0000 723c 0000 004e  rst!Fr....r<...N
-000028f0: 290f 7219 0000 0072 3e00 0000 7216 0000  ).r....r>...r...
-00002900: 0072 3f00 0000 7217 0000 0072 4000 0000  .r?...r....r@...
-00002910: 5a18 7061 7468 5f63 6f76 6572 6167 655f  Z.path_coverage_
-00002920: 6874 6d6c 5f69 6e64 6578 7241 0000 0072  html_indexrA...r
-00002930: 4200 0000 7243 0000 00da 0a56 616c 7565  B...rC.....Value
-00002940: 4572 726f 7272 4400 0000 7245 0000 0072  ErrorrD...rE...r
-00002950: 0c00 0000 721a 0000 0072 4700 0000 7220  ....r....rG...r 
-00002960: 0000 0072 2000 0000 7226 0000 00da 0876  ...r ...r&.....v
-00002970: 6965 775f 636f 7604 0200 0073 1800 0000  iew_cov....s....
-00002980: 0007 0201 0401 0401 0401 04fd 04ff 0408  ................
-00002990: 0e01 0802 0801 1002 7a10 4163 7469 6f6e  ........z.Action
-000029a0: 732e 7669 6577 5f63 6f76 7a08 746f 782d  s.view_covz.tox-
-000029b0: 6f6e 6c79 7a22 5275 6e20 6d61 7472 6978  onlyz"Run matrix
-000029c0: 2074 6573 7420 696e 2074 6f78 2077 6974   test in tox wit
-000029d0: 6820 7079 7465 7374 6303 0000 0000 0000  h pytestc.......
-000029e0: 0000 0000 0004 0000 0006 0000 004b 0000  .............K..
-000029f0: 0073 4800 0000 7400 6401 6a01 7402 6a03  .sH...t.d.j.t.j.
-00002a00: 7404 6a05 7c01 6a06 6402 8d03 8301 0100  t.j.|.j.d.......
-00002a10: 7c02 6403 6b08 723a 7407 a008 7c01 6a09  |.d.k.r:t...|.j.
-00002a20: 6404 a001 7c01 6a0a a101 6702 a101 0100  d...|.j...g.....
-00002a30: 740b 6405 6406 8d01 0100 6407 5300 2908  t.d.d.....d.S.).
-00002a40: 7234 0000 007a 397b 6379 616e 7d52 756e  r4...z9{cyan}Run
-00002a50: 206d 6174 7269 7820 7465 7374 2077 6974   matrix test wit
-00002a60: 6820 746f 7820 7365 7474 696e 6773 2069  h tox settings i
-00002a70: 6e20 7b72 6573 6574 7d74 6f78 2e69 6e69  n {reset}tox.ini
-00002a80: 7271 0000 0046 7a0e 2d2d 776f 726b 6469  rq...Fz.--workdi
-00002a90: 7220 227b 7d22 7205 0000 0072 3c00 0000  r "{}"r....r<...
-00002aa0: 4e29 0c72 1900 0000 723e 0000 0072 1600  N).r....r>...r..
-00002ab0: 0000 723f 0000 0072 1700 0000 7240 0000  ..r?...r....r@..
-00002ac0: 0072 7200 0000 7244 0000 0072 4500 0000  .rr...rD...rE...
-00002ad0: 5a11 7061 7468 5f76 656e 765f 6269 6e5f  Z.path_venv_bin_
-00002ae0: 746f 7872 5d00 0000 721a 0000 0072 4700  toxr]...r....rG.
-00002af0: 0000 7220 0000 0072 2000 0000 7226 0000  ..r ...r ...r&..
-00002b00: 00da 0d74 6573 745f 746f 785f 6f6e 6c79  ...test_tox_only
-00002b10: 1b02 0000 731a 0000 0000 0802 0104 0104  ....s...........
-00002b20: 0104 0104 fd04 ff04 0708 0104 0104 010a  ................
-00002b30: fe06 047a 1541 6374 696f 6e73 2e74 6573  ...z.Actions.tes
-00002b40: 745f 746f 785f 6f6e 6c79 5a03 746f 787a  t_tox_onlyZ.toxz
-00002b50: 412a 2a20 5275 6e20 6d61 7472 6978 2074  A** Run matrix t
-00002b60: 6573 7420 696e 2074 6f78 2077 6974 6820  est in tox with 
-00002b70: 7079 7465 7374 2e20 5374 6172 7420 6f76  pytest. Start ov
-00002b80: 6572 2c20 7265 7573 6520 6e6f 7468 696e  er, reuse nothin
-00002b90: 672e 6303 0000 0000 0000 0000 0000 0004  g.c.............
-00002ba0: 0000 0004 0000 004b 0000 0073 5800 0000  .......K...sX...
-00002bb0: 7c00 6a00 7c01 6601 6401 7c02 6901 7c03  |.j.|.f.d.|.i.|.
-00002bc0: 9702 8e01 0100 7c00 6a01 7c01 6601 6401  ......|.j.|.f.d.
-00002bd0: 7c02 6901 7c03 9702 8e01 0100 7c02 6402  |.i.|.......|.d.
-00002be0: 6b08 723e 7402 7c01 6a03 8301 0100 7c00  k.r>t.|.j.....|.
-00002bf0: 6a04 7c01 6601 6401 7c02 6901 7c03 9702  j.|.f.d.|.i.|...
-00002c00: 8e01 0100 6403 5300 7277 0000 0029 0572  ....d.S.rw...).r
-00002c10: 6d00 0000 725e 0000 0072 0d00 0000 7254  m...r^...r....rT
-00002c20: 0000 0072 7d00 0000 7247 0000 0072 2000  ...r}...rG...r .
-00002c30: 0000 7220 0000 0072 2600 0000 da08 7465  ..r ...r&.....te
-00002c40: 7374 5f74 6f78 3102 0000 730a 0000 0000  st_tox1...s.....
-00002c50: 0816 0116 0108 010a 017a 1041 6374 696f  .........z.Actio
-00002c60: 6e73 2e74 6573 745f 746f 785a 0470 6570  ns.test_toxZ.pep
-00002c70: 387a 5041 7070 6c79 2070 6570 3820 2868  8zPApply pep8 (h
-00002c80: 7474 7073 3a2f 2f77 7777 2e70 7974 686f  ttps://www.pytho
-00002c90: 6e2e 6f72 672f 6465 762f 7065 7073 2f70  n.org/dev/peps/p
-00002ca0: 6570 2d30 3030 382f 2920 746f 2073 6f75  ep-0008/) to sou
-00002cb0: 7263 6520 636f 6465 2061 6e64 2074 6573  rce code and tes
-00002cc0: 7473 2e63 0300 0000 0000 0000 0000 0000  ts.c............
-00002cd0: 0400 0000 0600 0000 4b00 0000 7350 0000  ........K...sP..
-00002ce0: 007c 006a 007c 017c 0264 018d 0201 0074  .|.j.|.|.d.....t
-00002cf0: 0164 026a 0274 036a 0474 056a 067c 016a  .d.j.t.j.t.j.|.j
-00002d00: 0764 038d 0383 0101 007c 0264 046b 0872  .d.......|.d.k.r
-00002d10: 4274 08a0 097c 016a 0a7c 016a 0767 02a1  Bt...|.j.|.j.g..
-00002d20: 0101 0074 0b64 0564 068d 0101 0064 0753  ...t.d.d.....d.S
-00002d30: 0029 0872 3400 0000 a901 724a 0000 007a  .).r4.....rJ...z
-00002d40: 427b 6379 616e 7d72 6566 6f72 6d61 7420  B{cyan}reformat 
-00002d50: 7079 7468 6f6e 2063 6f64 6520 7374 796c  python code styl
-00002d60: 652c 2065 7865 6375 7465 207b 7265 7365  e, execute {rese
-00002d70: 747d 7b72 6566 6f72 6d61 745f 7363 7269  t}{reformat_scri
-00002d80: 7074 7d29 0372 3600 0000 7237 0000 005a  pt}).r6...r7...Z
-00002d90: 0f72 6566 6f72 6d61 745f 7363 7269 7074  .reformat_script
-00002da0: 4672 0500 0000 723c 0000 004e 290c 7269  Fr....r<...N).ri
-00002db0: 0000 0072 1900 0000 723e 0000 0072 1600  ...r....r>...r..
-00002dc0: 0000 723f 0000 0072 1700 0000 7240 0000  ..r?...r....r@..
-00002dd0: 005a 1a70 6174 685f 6669 785f 636f 6465  .Z.path_fix_code
-00002de0: 5f73 7479 6c65 5f73 6372 6970 7472 4400  _style_scriptrD.
-00002df0: 0000 7245 0000 0072 6300 0000 721a 0000  ..rE...rc...r...
-00002e00: 0072 4700 0000 7220 0000 0072 2000 0000  .rG...r ...r ...
-00002e10: 7226 0000 00da 1872 6566 6f72 6d61 745f  r&.....reformat_
-00002e20: 7065 7038 5f63 6f64 655f 7374 796c 653f  pep8_code_style?
-00002e30: 0200 0073 1c00 0000 0008 0e01 0201 0401  ...s............
-00002e40: 0401 0401 04fd 04ff 0407 0801 0401 0401  ................
-00002e50: 04fe 0604 7a20 4163 7469 6f6e 732e 7265  ....z Actions.re
-00002e60: 666f 726d 6174 5f70 6570 385f 636f 6465  format_pep8_code
-00002e70: 5f73 7479 6c65 7a26 4275 696c 6420 6c6f  _stylez&Build lo
-00002e80: 6361 6c20 646f 6375 6d65 6e74 7320 7769  cal documents wi
-00002e90: 7468 2073 7068 696e 782d 646f 632e 6303  th sphinx-doc.c.
-00002ea0: 0000 0000 0000 0000 0000 0004 0000 0006  ................
-00002eb0: 0000 004b 0000 0073 7000 0000 7400 6401  ...K...sp...t.d.
-00002ec0: 6a01 7402 6a03 7404 6a05 7c01 6a06 6402  j.t.j.t.j.|.j.d.
-00002ed0: 8d03 8301 0100 7c02 6403 6b08 7262 7c01  ......|.d.k.rb|.
-00002ee0: 6a07 7408 6a09 1700 7408 6a0a a00b 6404  j.t.j...t.j...d.
-00002ef0: 6405 a102 1700 7408 6a0a 6404 3c00 7c01  d.....t.j.d.<.|.
-00002f00: 6a0c 7408 6a0a 6406 3c00 740d a00e 6407  j.t.j.d.<.t...d.
-00002f10: 6408 7c01 6a0f 6409 6704 a101 0100 7410  d.|.j.d.g.....t.
-00002f20: 640a 640b 8d01 0100 640c 5300 290d 7234  d.d.....d.S.).r4
-00002f30: 0000 007a 2a7b 6379 616e 7d42 7569 6c64  ...z*{cyan}Build
-00002f40: 2064 6f63 2061 7420 7b72 6573 6574 7d7b   doc at {reset}{
-00002f50: 646f 635f 6275 696c 645f 6874 6d6c 7da9  doc_build_html}.
-00002f60: 0372 3600 0000 7237 0000 005a 0e64 6f63  .r6...r7...Z.doc
-00002f70: 5f62 7569 6c64 5f68 746d 6c46 da04 5041  _build_htmlF..PA
-00002f80: 5448 da00 5a0b 5649 5254 5541 4c5f 454e  TH..Z.VIRTUAL_EN
-00002f90: 56da 046d 616b 657a 022d 435a 0468 746d  V..makez.-CZ.htm
-00002fa0: 6c72 0500 0000 723c 0000 004e 2911 7219  lr....r<...N).r.
-00002fb0: 0000 0072 3e00 0000 7216 0000 0072 3f00  ...r>...r....r?.
-00002fc0: 0000 7217 0000 0072 4000 0000 da19 6469  ..r....r@.....di
-00002fd0: 725f 7370 6869 6e78 5f64 6f63 5f62 7569  r_sphinx_doc_bui
-00002fe0: 6c64 5f68 746d 6c5a 0c64 6972 5f76 656e  ld_htmlZ.dir_ven
-00002ff0: 765f 6269 6e72 4100 0000 da07 7061 7468  v_binrA.....path
-00003000: 7365 70da 0765 6e76 6972 6f6e da03 6765  sep..environ..ge
-00003010: 7472 3800 0000 7244 0000 0072 4500 0000  tr8...rD...rE...
-00003020: 5a0e 6469 725f 7370 6869 6e78 5f64 6f63  Z.dir_sphinx_doc
-00003030: 721a 0000 0072 4700 0000 7220 0000 0072  r....rG...r ...r
-00003040: 2000 0000 7226 0000 00da 0e62 7569 6c64   ...r&.....build
-00003050: 5f64 6f63 5f6f 6e6c 7956 0200 0073 2200  _doc_onlyV...s".
-00003060: 0000 0007 0201 0401 0401 0401 04fd 04ff  ................
-00003070: 0407 0802 2001 0c02 0401 0201 0200 0401  .... ...........
-00003080: 02fd 0605 7a16 4163 7469 6f6e 732e 6275  ....z.Actions.bu
-00003090: 696c 645f 646f 635f 6f6e 6c79 7a44 2a2a  ild_doc_onlyzD**
-000030a0: 2042 7569 6c64 206c 6f63 616c 2064 6f63   Build local doc
-000030b0: 756d 656e 7473 2077 6974 6820 7370 6869  uments with sphi
-000030c0: 6e78 2d64 6f63 2c20 7374 6172 7420 6f76  nx-doc, start ov
-000030d0: 6572 2c20 7265 7573 6520 6e6f 7468 696e  er, reuse nothin
-000030e0: 672e 6303 0000 0000 0000 0000 0000 0004  g.c.............
-000030f0: 0000 0006 0000 004b 0000 0073 7200 0000  .......K...sr...
-00003100: 7c00 6a00 7c01 6601 6401 7c02 6901 7c03  |.j.|.f.d.|.i.|.
-00003110: 9702 8e01 0100 7c00 6a01 7c01 6601 6401  ......|.j.|.f.d.
-00003120: 7c02 6901 7c03 9702 8e01 0100 7c02 6402  |.i.|.......|.d.
-00003130: 6b08 7258 7402 7c01 6a03 8301 0100 7402  k.rXt.|.j.....t.
-00003140: 7404 6a05 a006 7c01 6a07 7c01 6a08 a009  t.j...|.j.|.j...
-00003150: a100 a102 8301 0100 7c00 6a0a 7c01 6601  ........|.j.|.f.
-00003160: 6401 7c02 6901 7c03 9702 8e01 0100 6403  d.|.i.|.......d.
-00003170: 5300 7277 0000 0029 0b72 6b00 0000 725e  S.rw...).rk...r^
-00003180: 0000 0072 0d00 0000 7250 0000 0072 4100  ...r....rP...rA.
-00003190: 0000 7242 0000 00da 046a 6f69 6e5a 1564  ..rB.....joinZ.d
-000031a0: 6972 5f73 7068 696e 785f 646f 635f 736f  ir_sphinx_doc_so
-000031b0: 7572 6365 7259 0000 0072 5a00 0000 7289  urcerY...rZ...r.
-000031c0: 0000 0072 4700 0000 7220 0000 0072 2000  ...rG...r ...r .
-000031d0: 0000 7226 0000 00da 0962 7569 6c64 5f64  ..r&.....build_d
-000031e0: 6f63 7002 0000 7312 0000 0000 0716 0116  ocp...s.........
-000031f0: 0108 010a 0108 0104 0008 ff06 027a 1141  .............z.A
-00003200: 6374 696f 6e73 2e62 7569 6c64 5f64 6f63  ctions.build_doc
-00003210: 7a25 436c 6561 7220 7265 6365 6e74 6c79  z%Clear recently
-00003220: 2062 7569 6c74 206c 6f63 616c 2064 6f63   built local doc
-00003230: 756d 656e 7473 2e63 0300 0000 0000 0000  uments.c........
-00003240: 0000 0000 0400 0000 0600 0000 4b00 0000  ............K...
-00003250: 733a 0000 0074 0064 016a 0174 026a 0374  s:...t.d.j.t.j.t
-00003260: 046a 057c 016a 0664 028d 0383 0101 007c  .j.|.j.d.......|
-00003270: 0264 036b 0872 2c74 077c 016a 0683 0101  .d.k.r,t.|.j....
-00003280: 0074 0864 0464 058d 0101 0064 0653 0029  .t.d.d.....d.S.)
-00003290: 0772 3400 0000 7a34 7b63 7961 6e7d 436c  .r4...z4{cyan}Cl
-000032a0: 6561 6e20 7265 6365 6e74 6c79 2062 7569  ean recently bui
-000032b0: 6c74 2064 6f63 2061 7420 7b72 6573 6574  lt doc at {reset
-000032c0: 7d7b 646f 635f 6275 696c 647d 2903 7236  }{doc_build}).r6
-000032d0: 0000 0072 3700 0000 5a09 646f 635f 6275  ...r7...Z.doc_bu
-000032e0: 696c 6446 7205 0000 0072 3c00 0000 4e29  ildFr....r<...N)
-000032f0: 0972 1900 0000 723e 0000 0072 1600 0000  .r....r>...r....
-00003300: 723f 0000 0072 1700 0000 7240 0000 0072  r?...r....r@...r
-00003310: 5000 0000 720d 0000 0072 1a00 0000 7247  P...r....r....rG
-00003320: 0000 0072 2000 0000 7220 0000 0072 2600  ...r ...r ...r&.
-00003330: 0000 da09 636c 6561 6e5f 646f 637f 0200  ....clean_doc...
-00003340: 0073 1400 0000 0007 0201 0401 0401 0401  .s..............
-00003350: 04fd 04ff 0407 0801 0a01 7a11 4163 7469  ..........z.Acti
-00003360: 6f6e 732e 636c 6561 6e5f 646f 637a 272a  ons.clean_docz'*
-00003370: 2a20 5669 6577 2072 6563 656e 746c 7920  * View recently 
-00003380: 6275 696c 6420 6c6f 6361 6c20 646f 6375  build local docu
-00003390: 6d65 6e74 732e 6303 0000 0000 0000 0000  ments.c.........
-000033a0: 0000 0005 0000 0006 0000 004b 0000 0073  ...........K...s
-000033b0: 9600 0000 7400 6401 6a01 7402 6a03 7404  ....t.d.j.t.j.t.
-000033c0: 6a05 7c01 6a06 6402 8d03 8301 0100 7407  j.|.j.d.......t.
-000033d0: 6a08 a009 7407 6a08 a00a 7c01 6a06 6403  j...t.j...|.j.d.
-000033e0: a102 a101 7244 7407 6a08 a00a 7c01 6a06  ....rDt.j...|.j.
-000033f0: 6403 a102 7d04 6e2e 7407 6a08 a009 7407  d...}.n.t.j...t.
-00003400: 6a08 a00a 7c01 6a06 6404 a102 a101 726e  j...|.j.d.....rn
-00003410: 7407 6a08 a00a 7c01 6a06 6404 a102 7d04  t.j...|.j.d...}.
-00003420: 6e04 740b 8201 7c02 6405 6b08 7288 740c  n.t...|.d.k.r.t.
-00003430: a00d 740e 7c04 6702 a101 0100 740f 6406  ..t.|.g.....t.d.
-00003440: 6407 8d01 0100 6408 5300 2909 7234 0000  d.....d.S.).r4..
-00003450: 007a 407b 6379 616e 7d4f 7065 6e20 7265  .z@{cyan}Open re
-00003460: 6365 6e74 6c79 2062 7569 6c74 206c 6f63  cently built loc
-00003470: 616c 2068 746d 6c20 646f 6320 7b72 6573  al html doc {res
-00003480: 6574 7d7b 646f 635f 6275 696c 645f 6874  et}{doc_build_ht
-00003490: 6d6c 7d72 8100 0000 7a0a 696e 6465 782e  ml}r....z.index.
-000034a0: 6874 6d6c 7a0b 5245 4144 4d45 2e68 746d  htmlz.README.htm
-000034b0: 6c46 7205 0000 0072 3c00 0000 4e29 1072  lFr....r<...N).r
-000034c0: 1900 0000 723e 0000 0072 1600 0000 723f  ....r>...r....r?
-000034d0: 0000 0072 1700 0000 7240 0000 0072 8500  ...r....r@...r..
-000034e0: 0000 7241 0000 0072 4200 0000 7243 0000  ..rA...rB...rC..
-000034f0: 0072 8a00 0000 727b 0000 0072 4400 0000  .r....r{...rD...
-00003500: 7245 0000 0072 0c00 0000 721a 0000 0029  rE...r....r....)
-00003510: 0572 4800 0000 7249 0000 0072 4a00 0000  .rH...rI...rJ...
-00003520: 7222 0000 005a 1370 6174 685f 646f 635f  r"...Z.path_doc_
-00003530: 696e 6465 785f 6874 6d6c 7220 0000 0072  index_htmlr ...r
-00003540: 2000 0000 7226 0000 00da 0876 6965 775f   ...r&.....view_
-00003550: 646f 6391 0200 0073 2600 0000 0007 0201  doc....s&.......
-00003560: 0401 0401 0401 04fd 04ff 0408 0601 0eff  ................
-00003570: 0403 1201 0601 0eff 0403 1202 0402 0801  ................
-00003580: 0e02 7a10 4163 7469 6f6e 732e 7669 6577  ..z.Actions.view
-00003590: 5f64 6f63 6306 0000 0000 0000 0000 0000  _docc...........
-000035a0: 0009 0000 0008 0000 004b 0000 0073 f800  .........K...s..
-000035b0: 0000 7400 7c03 8301 0100 7401 6401 6a02  ..t.|.....t.d.j.
-000035c0: 7403 6a04 7c02 6402 8d02 8301 0100 7401  t.j.|.d.......t.
-000035d0: 6403 6a02 7403 6a04 7405 6a06 7407 7c03  d.j.t.j.t.j.t.|.
-000035e0: 6404 8d04 8301 0100 6405 6406 6407 7c03  d.......d.d.d.|.
-000035f0: 6408 6409 6706 7d07 7c04 640a 6b09 725c  d.d.g.}.|.d.k.r\
-00003600: 7c07 a008 640b 7c04 6702 a101 0100 7c05  |...d.|.g.....|.
-00003610: 640c 6b08 726e 7409 a00a 7c07 a101 0100  d.k.rnt...|.....
-00003620: 7401 640d 6a02 7403 6a04 7405 6a06 7407  t.d.j.t.j.t.j.t.
-00003630: 7c01 6a0b 7c03 640e 8d05 8301 0100 6405  |.j.|.d.......d.
-00003640: 6406 640f 7c01 6a0b 7c03 6409 6706 7d07  d.d.|.j.|.d.g.}.
-00003650: 7c04 640a 6b09 72b4 7c07 a008 640b 7c04  |.d.k.r.|...d.|.
-00003660: 6702 a101 0100 7c05 640c 6b08 72c6 7409  g.....|.d.k.r.t.
-00003670: a00a 7c07 a101 0100 740c 7c03 8301 7d08  ..|.....t.|...}.
-00003680: 7401 6410 6a02 7403 6a04 7405 6a06 7407  t.d.j.t.j.t.j.t.
-00003690: 7c02 7c08 6411 8d05 8301 0100 740d 6412  |.|.d.......t.d.
-000036a0: 6413 8d01 0100 640a 5300 2914 7aef 0a20  d.....d.S.).z.. 
-000036b0: 2020 2020 2020 2044 6570 6c6f 7920 6c6f         Deploy lo
-000036c0: 6361 6c20 6874 6d6c 2064 6f63 2074 6f20  cal html doc to 
-000036d0: 5333 2e0a 0a20 2020 2020 2020 203a 7479  S3...        :ty
-000036e0: 7065 2063 6f6e 6669 673a 2052 6570 6f43  pe config: RepoC
-000036f0: 6f6e 6669 670a 0a20 2020 2020 2020 203a  onfig..        :
-00003700: 7479 7065 2064 6f63 5f76 6572 7369 6f6e  type doc_version
-00003710: 3a20 7374 720a 2020 2020 2020 2020 3a70  : str.        :p
-00003720: 6172 616d 2064 6f63 5f76 6572 7369 6f6e  aram doc_version
-00003730: 3a20 226c 6174 6573 7422 206f 7220 2276  : "latest" or "v
-00003740: 6572 7369 6f6e 6564 220a 0a20 2020 2020  ersioned"..     
-00003750: 2020 203a 7479 7065 2073 335f 7572 695f     :type s3_uri_
-00003760: 646f 635f 6469 723a 2073 7472 0a20 2020  doc_dir: str.   
-00003770: 2020 2020 203a 7479 7065 2064 6f63 5f68       :type doc_h
-00003780: 6f73 745f 6177 735f 7072 6f66 696c 653a  ost_aws_profile:
-00003790: 2073 7472 0a20 2020 2020 2020 207a 3a7b   str.        z:{
-000037a0: 6379 616e 7d64 6570 6c6f 7920 646f 6320  cyan}deploy doc 
-000037b0: 6672 6f6d 206c 6f63 616c 2074 6f20 7333  from local to s3
-000037c0: 2061 7320 7b64 6f63 5f76 6572 7369 6f6e   as {doc_version
-000037d0: 7d20 646f 6320 2e2e 2e29 0272 3600 0000  } doc ...).r6...
-000037e0: da0b 646f 635f 7665 7273 696f 6e7a 2c7b  ..doc_versionz,{
-000037f0: 6379 616e 7d7b 7461 627d 6177 7320 7333  cyan}{tab}aws s3
-00003800: 2072 6d20 7b72 6573 6574 7d7b 7333 5f75   rm {reset}{s3_u
-00003810: 7269 5f64 6f63 5f64 6972 7d29 0472 3600  ri_doc_dir}).r6.
-00003820: 0000 7237 0000 0072 3a00 0000 da0e 7333  ..r7...r:.....s3
-00003830: 5f75 7269 5f64 6f63 5f64 6972 da03 6177  _uri_doc_dir..aw
-00003840: 73da 0273 335a 0272 6d7a 0b2d 2d72 6563  s..s3Z.rmz.--rec
-00003850: 7572 7369 7665 7a12 2d2d 6f6e 6c79 2d73  ursivez.--only-s
-00003860: 686f 772d 6572 726f 7273 4efa 092d 2d70  how-errorsN..--p
-00003870: 726f 6669 6c65 467a 4a7b 6379 616e 7d7b  rofileFzJ{cyan}{
-00003880: 7461 627d 6177 7320 7333 2073 796e 6320  tab}aws s3 sync 
-00003890: 7b72 6573 6574 7d7b 6469 725f 7370 6869  {reset}{dir_sphi
-000038a0: 6e78 5f64 6f63 5f62 7569 6c64 5f68 746d  nx_doc_build_htm
-000038b0: 6c7d 207b 7333 5f75 7269 5f64 6f63 5f64  l} {s3_uri_doc_d
-000038c0: 6972 7d29 0572 3600 0000 7237 0000 0072  ir}).r6...r7...r
-000038d0: 3a00 0000 7285 0000 0072 8f00 0000 da04  :...r....r......
-000038e0: 7379 6e63 7a3c 7b63 7961 6e7d 7b74 6162  syncz<{cyan}{tab
-000038f0: 7d76 6965 7720 7b64 6f63 5f76 6572 7369  }view {doc_versi
-00003900: 6f6e 7d20 646f 6320 6174 207b 7265 7365  on} doc at {rese
-00003910: 747d 7b73 335f 636f 6e73 6f6c 655f 7572  t}{s3_console_ur
-00003920: 6c7d 2905 7236 0000 0072 3700 0000 723a  l}).r6...r7...r:
-00003930: 0000 0072 8e00 0000 da0e 7333 5f63 6f6e  ...r......s3_con
-00003940: 736f 6c65 5f75 726c 7205 0000 0072 3c00  sole_urlr....r<.
-00003950: 0000 290e 7214 0000 0072 1900 0000 723e  ..).r....r....r>
-00003960: 0000 0072 1600 0000 723f 0000 0072 1700  ...r....r?...r..
-00003970: 0000 7240 0000 0072 1800 0000 da06 6578  ..r@...r......ex
-00003980: 7465 6e64 7244 0000 0072 4500 0000 7285  tendrD...rE...r.
-00003990: 0000 0072 1200 0000 721a 0000 0029 0972  ...r....r....).r
-000039a0: 4800 0000 7249 0000 0072 8e00 0000 728f  H...rI...r....r.
-000039b0: 0000 00da 1464 6f63 5f68 6f73 745f 6177  .....doc_host_aw
-000039c0: 735f 7072 6f66 696c 6572 4a00 0000 7222  s_profilerJ...r"
-000039d0: 0000 0072 2100 0000 7294 0000 0072 2000  ...r!...r....r .
-000039e0: 0000 7220 0000 0072 2600 0000 da11 5f64  ..r ...r&....._d
-000039f0: 6570 6c6f 795f 646f 635f 746f 5f73 33b0  eploy_doc_to_s3.
-00003a00: 0200 0073 7200 0000 0014 0802 0201 0401  ...sr...........
-00003a10: 0401 02fe 04ff 0407 0201 0401 0401 0401  ................
-00003a20: 0201 02fc 04ff 0409 0200 0200 0200 0201  ................
-00003a30: 0201 02fd 0405 0801 0e02 0801 0a02 0201  ................
-00003a40: 0401 0401 0401 0201 0401 02fb 04ff 040a  ................
-00003a50: 0200 0200 0201 0400 0201 02fd 0405 0801  ................
-00003a60: 0e02 0801 0a02 0801 0201 0401 0401 0401  ................
-00003a70: 0201 0201 02fb 04ff 040a 7a19 4163 7469  ..........z.Acti
-00003a80: 6f6e 732e 5f64 6570 6c6f 795f 646f 635f  ons._deploy_doc_
-00003a90: 746f 5f73 337a 3144 6570 6c6f 7920 6c6f  to_s3z1Deploy lo
-00003aa0: 6361 6c20 6874 6d6c 2064 6f63 2074 6f20  cal html doc to 
-00003ab0: 5333 2061 7320 7665 7273 696f 6e65 6420  S3 as versioned 
-00003ac0: 646f 6375 6d65 6e74 6303 0000 0000 0000  documentc.......
-00003ad0: 0000 0000 0004 0000 0007 0000 004b 0000  .............K..
-00003ae0: 0073 2800 0000 7c00 6a00 7c01 6601 6401  .s(...|.j.|.f.d.
-00003af0: 7c01 6a01 7c01 6a02 a003 a100 7c02 6402  |.j.|.j.....|.d.
-00003b00: 9c04 7c03 9702 8e01 0100 6403 5300 2904  ..|.......d.S.).
-00003b10: 7234 0000 005a 0976 6572 7369 6f6e 6564  r4...Z.versioned
-00003b20: a904 728e 0000 0072 8f00 0000 7296 0000  ..r....r....r...
-00003b30: 0072 4a00 0000 4e29 0472 9700 0000 5a18  .rJ...N).r....Z.
-00003b40: 7333 5f75 7269 5f64 6f63 5f64 6972 5f76  s3_uri_doc_dir_v
-00003b50: 6572 7369 6f6e 6564 da14 444f 435f 484f  ersioned..DOC_HO
-00003b60: 5354 5f41 5753 5f50 524f 4649 4c45 725a  ST_AWS_PROFILErZ
-00003b70: 0000 0072 4700 0000 7220 0000 0072 2000  ...rG...r ...r .
-00003b80: 0000 7226 0000 00da 1764 6570 6c6f 795f  ..r&.....deploy_
-00003b90: 646f 635f 746f 5f76 6572 7369 6f6e 6564  doc_to_versioned
-00003ba0: 0103 0000 7314 0000 0000 0704 0102 ff02  ....s...........
-00003bb0: 0202 0104 0108 0102 fb04 0602 fa7a 1f41  .............z.A
-00003bc0: 6374 696f 6e73 2e64 6570 6c6f 795f 646f  ctions.deploy_do
-00003bd0: 635f 746f 5f76 6572 7369 6f6e 6564 7a2e  c_to_versionedz.
-00003be0: 4465 706c 6f79 206c 6f63 616c 2068 746d  Deploy local htm
-00003bf0: 6c20 646f 6320 746f 2053 3320 6173 206c  l doc to S3 as l
-00003c00: 6174 6573 7420 646f 6375 6d65 6e74 6303  atest documentc.
-00003c10: 0000 0000 0000 0000 0000 0004 0000 0007  ................
-00003c20: 0000 004b 0000 0073 2800 0000 7c00 6a00  ...K...s(...|.j.
-00003c30: 7c01 6601 6401 7c01 6a01 7c01 6a02 a003  |.f.d.|.j.|.j...
-00003c40: a100 7c02 6402 9c04 7c03 9702 8e01 0100  ..|.d...|.......
-00003c50: 6403 5300 2904 7234 0000 005a 066c 6174  d.S.).r4...Z.lat
-00003c60: 6573 7472 9800 0000 4e29 0472 9700 0000  estr....N).r....
-00003c70: 5a15 7333 5f75 7269 5f64 6f63 5f64 6972  Z.s3_uri_doc_dir
-00003c80: 5f6c 6174 6573 7472 9900 0000 725a 0000  _latestr....rZ..
-00003c90: 0072 4700 0000 7220 0000 0072 2000 0000  .rG...r ...r ...
-00003ca0: 7226 0000 00da 1464 6570 6c6f 795f 646f  r&.....deploy_do
-00003cb0: 635f 746f 5f6c 6174 6573 7411 0300 0073  c_to_latest....s
-00003cc0: 1400 0000 0007 0401 02ff 0202 0201 0401  ................
-00003cd0: 0801 02fb 0406 02fa 7a1c 4163 7469 6f6e  ........z.Action
-00003ce0: 732e 6465 706c 6f79 5f64 6f63 5f74 6f5f  s.deploy_doc_to_
-00003cf0: 6c61 7465 7374 7a5a 4465 706c 6f79 206c  latestzZDeploy l
-00003d00: 6f63 616c 2068 746d 6c20 646f 6320 746f  ocal html doc to
-00003d10: 2053 3320 6173 2076 6572 7369 6f6e 6564   S3 as versioned
-00003d20: 2064 6f63 756d 656e 742c 2061 6e64 2061   document, and a
-00003d30: 6c73 6f20 6173 206c 6174 6573 7420 646f  lso as latest do
-00003d40: 6375 6d65 6e74 206f 7074 696f 6e61 6c6c  cument optionall
-00003d50: 792e 6303 0000 0000 0000 0000 0000 0005  y.c.............
-00003d60: 0000 0005 0000 004b 0000 0073 7e00 0000  .......K...s~...
-00003d70: 7400 6401 6a01 7402 6a03 6402 8d01 8301  t.d.j.t.j.d.....
-00003d80: 0100 7c00 6a04 7c01 6601 6403 7c02 6901  ..|.j.|.f.d.|.i.
-00003d90: 7c03 9702 8e01 0100 7400 6404 6a01 7402  |.......t.d.j.t.
-00003da0: 6a03 7405 6405 8d02 8301 0100 7406 7407  j.t.d.......t.t.
-00003db0: 6406 8301 8301 a008 a100 a009 a100 7d04  d.............}.
-00003dc0: 7c04 6407 6b06 7270 7c00 6a0a 7c01 6601  |.d.k.rp|.j.|.f.
-00003dd0: 6403 7c02 6901 7c03 9702 8e01 0100 6e0a  d.|.i.|.......n.
-00003de0: 740b 6408 6409 8d01 0100 640a 5300 290b  t.d.d.....d.S.).
-00003df0: 7234 0000 007a 257b 6379 616e 7d64 6570  r4...z%{cyan}dep
-00003e00: 6c6f 7920 646f 6320 6672 6f6d 206c 6f63  loy doc from loc
-00003e10: 616c 2074 6f20 7333 202e 2e2e 724d 0000  al to s3 ...rM..
-00003e20: 0072 4a00 0000 7a23 7b63 7961 6e7d 616c  .rJ...z#{cyan}al
-00003e30: 736f 2064 6570 6c6f 7920 6c61 7465 7374  so deploy latest
-00003e40: 2064 6f63 2028 792f 6e29 3f72 3900 0000   doc (y/n)?r9...
-00003e50: 7283 0000 0029 02da 0179 da03 7965 7372  r....)...y..yesr
-00003e60: 0500 0000 723c 0000 004e 290c 7219 0000  ....r<...N).r...
-00003e70: 0072 3e00 0000 7216 0000 0072 3f00 0000  .r>...r....r?...
-00003e80: 729a 0000 0072 1800 0000 da03 7374 7272  r....r......strr
-00003e90: 0600 0000 da05 6c6f 7765 72da 0573 7472  ......lower..str
-00003ea0: 6970 729b 0000 0072 1a00 0000 2905 7248  ipr....r....).rH
-00003eb0: 0000 0072 4900 0000 724a 0000 0072 2200  ...rI...rJ...r".
-00003ec0: 0000 5a07 656e 7465 7265 6472 2000 0000  ..Z.enteredr ...
-00003ed0: 7220 0000 0072 2600 0000 da0a 6465 706c  r ...r&.....depl
-00003ee0: 6f79 5f64 6f63 2103 0000 7318 0000 0000  oy_doc!...s.....
-00003ef0: 0712 0116 0202 0104 0104 0102 fe04 ff04  ................
-00003f00: 0614 0108 0118 027a 1241 6374 696f 6e73  .......z.Actions
-00003f10: 2e64 6570 6c6f 795f 646f 635a 0770 7562  .deploy_docZ.pub
-00003f20: 6c69 7368 7a2d 2a2a 2050 7562 6c69 7368  lishz-** Publish
-00003f30: 2074 6869 7320 5061 636b 6167 6520 746f   this Package to
-00003f40: 2068 7474 7073 3a2f 2f70 7970 692e 6f72   https://pypi.or
-00003f50: 672f 2e63 0300 0000 0000 0000 0000 0000  g/.c............
-00003f60: 0500 0000 0700 0000 4b00 0000 73de 0000  ........K...s...
-00003f70: 007c 006a 007c 0166 0164 017c 0269 017c  .|.j.|.f.d.|.i.|
-00003f80: 0397 028e 0101 007c 006a 017c 0166 0164  .......|.j.|.f.d
-00003f90: 017c 0269 017c 0397 028e 0101 0074 0264  .|.i.|.......t.d
-00003fa0: 026a 0374 046a 0574 066a 077c 016a 08a0  .j.t.j.t.j.|.j..
-00003fb0: 09a1 0064 038d 0383 0101 007c 0264 046b  ...d.......|.d.k
-00003fc0: 0872 7074 0a7c 016a 0b83 0101 0074 0a7c  .rpt.|.j.....t.|
-00003fd0: 016a 0c83 0101 0074 0a7c 016a 0d83 0101  .j.....t.|.j....
-00003fe0: 0074 0ea0 0fa1 007d 0474 0ea0 107c 016a  .t.....}.t...|.j
-00003ff0: 11a1 0101 007a 347c 0264 046b 0872 b674  .....z4|.d.k.r.t
-00004000: 12a0 137c 016a 1464 0564 0664 0764 0867  ...|.j.d.d.d.d.g
-00004010: 05a1 0101 0074 12a0 137c 016a 1564 0964  .....t...|.j.d.d
-00004020: 0a67 03a1 0101 0057 006e 0c01 0001 0001  .g.....W.n......
-00004030: 0059 006e 0258 0074 0ea0 107c 04a1 0101  .Y.n.X.t...|....
-00004040: 0074 1664 0b64 0c8d 0101 0064 0d53 0029  .t.d.d.....d.S.)
-00004050: 0e72 3400 0000 724a 0000 007a 4f7b 6379  .r4...rJ...zO{cy
-00004060: 616e 7d50 7562 6c69 7368 207b 7061 636b  an}Publish {pack
-00004070: 6167 655f 6e61 6d65 7d20 746f 207b 7265  age_name} to {re
-00004080: 7365 747d 6874 7470 733a 2f2f 7079 7069  set}https://pypi
-00004090: 2e6f 7267 2f70 726f 6a65 6374 2f7b 7061  .org/project/{pa
-000040a0: 636b 6167 655f 6e61 6d65 7d2f 2903 7236  ckage_name}/).r6
-000040b0: 0000 0072 3700 0000 7258 0000 0046 7a08  ...r7...rX...Fz.
-000040c0: 7365 7475 702e 7079 5a05 7364 6973 745a  setup.pyZ.sdistZ
-000040d0: 0b62 6469 7374 5f77 6865 656c 7a0b 2d2d  .bdist_wheelz.--
-000040e0: 756e 6976 6572 7361 6c5a 0675 706c 6f61  universalZ.uploa
-000040f0: 647a 0664 6973 742f 2a72 0500 0000 723c  dz.dist/*r....r<
-00004100: 0000 004e 2917 7269 0000 0072 5e00 0000  ...N).ri...r^...
-00004110: 7219 0000 0072 3e00 0000 7216 0000 0072  r....r>...r....r
-00004120: 3f00 0000 7217 0000 0072 4000 0000 7259  ?...r....r@...rY
-00004130: 0000 0072 5a00 0000 720d 0000 0072 4f00  ...rZ...r....rO.
-00004140: 0000 5a13 6469 725f 7079 7069 5f64 6973  ..Z.dir_pypi_dis
-00004150: 7472 6962 7574 655a 0c64 6972 5f70 7970  tributeZ.dir_pyp
-00004160: 695f 6567 6772 4100 0000 da06 6765 7463  i_eggrA.....getc
-00004170: 7764 da05 6368 6469 7272 5d00 0000 7244  wd..chdirr]...rD
-00004180: 0000 0072 4500 0000 7263 0000 005a 1370  ...rE...rc...Z.p
-00004190: 6174 685f 7665 6e76 5f62 696e 5f74 7769  ath_venv_bin_twi
-000041a0: 6e65 721a 0000 0029 0572 4800 0000 7249  ner....).rH...rI
-000041b0: 0000 0072 4a00 0000 7222 0000 00da 0363  ...rJ...r".....c
-000041c0: 7764 7220 0000 0072 2000 0000 7226 0000  wdr ...r ...r&..
-000041d0: 00da 0f70 7562 6c69 7368 5f74 6f5f 7079  ...publish_to_py
-000041e0: 7069 3703 0000 7342 0000 0000 0816 0116  pi7...sB........
-000041f0: 0102 0104 0104 0104 0108 fd04 ff04 0708  ................
-00004200: 010a 010a 010a 0208 010c 0102 0108 0104  ................
-00004210: 0104 0102 0102 0102 0102 fb06 0704 0104  ................
-00004220: 0102 0102 fd0a 0506 0106 010a 017a 1741  .............z.A
-00004230: 6374 696f 6e73 2e70 7562 6c69 7368 5f74  ctions.publish_t
-00004240: 6f5f 7079 7069 7a1d 5275 6e20 4a75 7079  o_pypiz.Run Jupy
-00004250: 7465 7220 6e6f 7465 626f 6f6b 206c 6f63  ter notebook loc
-00004260: 616c 6c79 2e63 0300 0000 0000 0000 0000  ally.c..........
-00004270: 0000 0400 0000 0400 0000 4b00 0000 732e  ..........K...s.
-00004280: 0000 0074 0064 016a 0174 026a 0364 028d  ...t.d.j.t.j.d..
-00004290: 0183 0101 007c 0264 036b 0872 2a74 04a0  .....|.d.k.r*t..
-000042a0: 057c 016a 0664 0467 02a1 0101 0064 0553  .|.j.d.g.....d.S
-000042b0: 0029 0672 3400 0000 7a1e 7b63 7961 6e7d  .).r4...z.{cyan}
-000042c0: 7275 6e20 6a75 7079 7465 7220 6e6f 7465  run jupyter note
-000042d0: 626f 6f6b 202e 2e2e 724d 0000 0046 5a08  book ...rM...FZ.
-000042e0: 6e6f 7465 626f 6f6b 4e29 0772 1900 0000  notebookN).r....
-000042f0: 723e 0000 0072 1600 0000 723f 0000 0072  r>...r....r?...r
-00004300: 4400 0000 7245 0000 005a 1570 6174 685f  D...rE...Z.path_
-00004310: 7665 6e76 5f62 696e 5f6a 7570 7974 6572  venv_bin_jupyter
-00004320: 7247 0000 0072 2000 0000 7220 0000 0072  rG...r ...r ...r
-00004330: 2600 0000 da14 7275 6e5f 6a75 7079 7465  &.....run_jupyte
-00004340: 725f 6e6f 7465 626f 6f6b 6203 0000 730c  r_notebookb...s.
-00004350: 0000 0000 0712 0108 0104 0104 0102 fe7a  ...............z
-00004360: 1c41 6374 696f 6e73 2e72 756e 5f6a 7570  .Actions.run_jup
-00004370: 7974 6572 5f6e 6f74 6562 6f6f 6b7a 2642  yter_notebookz&B
-00004380: 7569 6c64 2041 5753 204c 616d 6264 6120  uild AWS Lambda 
-00004390: 736f 7572 6365 2063 6f64 6520 7a69 7020  source code zip 
-000043a0: 6669 6c65 2e63 0300 0000 0000 0000 0000  file.c..........
-000043b0: 0000 0c00 0000 0900 0000 4b00 0000 73ec  ..........K...s.
-000043c0: 0000 0074 0064 016a 0174 026a 0374 046a  ...t.d.j.t.j.t.j
-000043d0: 057c 016a 0664 028d 0383 0101 0074 0783  .|.j.d.......t..
-000043e0: 007d 0474 08a0 097c 016a 0aa1 0144 005d  .}.t...|.j...D.]
-000043f0: 625c 037d 057d 067d 077c 05a0 0b64 03a1  b\.}.}.}.|...d..
-00004400: 0172 4271 2c7c 0744 005d 467d 087c 08a0  .rBq,|.D.]F}.|..
-00004410: 0b64 04a1 0173 467c 08a0 0b64 05a1 0172  .d...sF|...d...r
-00004420: 6071 4674 086a 0ca0 0d7c 057c 08a1 027d  `qFt.j...|.|...}
-00004430: 0974 086a 0ca0 0e7c 097c 016a 0fa1 027d  .t.j...|.|.j...}
-00004440: 0a7c 04a0 107c 097c 0a66 02a1 0101 0071  .|...|.|.f.....q
-00004450: 4671 2c7c 0264 066b 0872 de74 117c 016a  Fq,|.d.k.r.t.|.j
-00004460: 1283 0101 0074 137c 016a 0683 0101 0074  .....t.|.j.....t
-00004470: 147c 016a 0664 0783 028f 207d 0b7c 0444  .|.j.d.... }.|.D
-00004480: 005d 145c 027d 097d 0a7c 0ba0 157c 097c  .].\.}.}.|...|.|
-00004490: 0aa1 0201 0071 be57 0035 0051 0052 0058  .....q.W.5.Q.R.X
-000044a0: 0074 1664 0864 098d 0101 0064 0a53 0029  .t.d.d.....d.S.)
-000044b0: 0b72 3400 0000 7a2f 7b63 7961 6e7d 6275  .r4...z/{cyan}bu
-000044c0: 696c 6420 6c61 6d62 6461 2073 6f75 7263  ild lambda sourc
-000044d0: 6520 636f 6465 2061 7420 7b72 6573 6574  e code at {reset
-000044e0: 7d7b 7061 7468 7d72 4e00 0000 da0b 5f5f  }{path}rN.....__
-000044f0: 7079 6361 6368 655f 5f7a 042e 7079 637a  pycache__z..pycz
-00004500: 042e 7079 6f46 da01 7772 0500 0000 723c  ..pyoF..wr....r<
-00004510: 0000 004e 2917 7219 0000 0072 3e00 0000  ...N).r....r>...
-00004520: 7216 0000 0072 3f00 0000 7217 0000 0072  r....r?...r....r
-00004530: 4000 0000 da18 7061 7468 5f6c 616d 6264  @.....path_lambd
-00004540: 615f 6275 696c 645f 736f 7572 6365 da04  a_build_source..
-00004550: 6c69 7374 7241 0000 00da 0477 616c 6bda  listrA.....walk.
-00004560: 0e64 6972 5f70 7974 686f 6e5f 6c69 62da  .dir_python_lib.
-00004570: 0865 6e64 7377 6974 6872 4200 0000 728a  .endswithrB...r.
-00004580: 0000 00da 0772 656c 7061 7468 725d 0000  .....relpathr]..
-00004590: 0072 5300 0000 720e 0000 00da 1064 6972  .rS...r......dir
-000045a0: 5f6c 616d 6264 615f 6275 696c 6472 0d00  _lambda_buildr..
-000045b0: 0000 7204 0000 00da 0577 7269 7465 721a  ..r......writer.
-000045c0: 0000 0029 0c72 4800 0000 7249 0000 0072  ...).rH...rI...r
-000045d0: 4a00 0000 7222 0000 005a 0b74 6f5f 7a69  J...r"...Z.to_zi
-000045e0: 705f 6c69 7374 da07 6469 726e 616d 6572  p_list..dirnamer
-000045f0: 1e00 0000 5a0d 6261 7365 6e61 6d65 5f6c  ....Z.basename_l
-00004600: 6973 74da 0862 6173 656e 616d 65da 0b73  ist..basename..s
-00004610: 6f75 7263 655f 7061 7468 5a0c 6172 6368  ource_pathZ.arch
-00004620: 6976 655f 7061 7468 da01 6672 2000 0000  ive_path..fr ...
-00004630: 7220 0000 0072 2600 0000 da18 6275 696c  r ...r&.....buil
-00004640: 645f 6c61 6d62 6461 5f73 6f75 7263 655f  d_lambda_source_
-00004650: 636f 6465 7303 0000 7330 0000 0000 0702  codes...s0......
-00004660: 0104 0104 0104 0104 fd04 ff04 0906 0116  ................
-00004670: 020a 0102 0108 0214 0102 010e 0110 0112  ................
-00004680: 0208 010a 010a 020e 010c 0118 027a 2041  .............z A
-00004690: 6374 696f 6e73 2e62 7569 6c64 5f6c 616d  ctions.build_lam
-000046a0: 6264 615f 736f 7572 6365 5f63 6f64 6563  bda_source_codec
-000046b0: 0500 0000 0000 0000 0000 0000 0e00 0000  ................
-000046c0: 0700 0000 4b00 0000 7304 0100 0074 0064  ....K...s....t.d
-000046d0: 016a 0174 026a 0374 046a 057c 027c 0364  .j.t.j.t.j.|.|.d
-000046e0: 028d 0483 0101 007c 0264 036b 0272 2a7c  .......|.d.k.r*|
-000046f0: 016a 067d 066e 147c 0264 046b 0272 3a7c  .j.}.n.|.d.k.r:|
-00004700: 016a 077d 066e 0474 0882 0174 096a 0aa0  .j.}.n.t...t.j..
-00004710: 0b7c 03a1 0172 e674 0ca0 0d7c 03a1 017d  .|...r.t...|...}
-00004720: 0774 0e7c 0683 015c 027d 087d 0974 0f7c  .t.|...\.}.}.t.|
-00004730: 0964 05a0 017c 07a1 0167 0264 0664 078d  .d...|...g.d.d..
-00004740: 027d 0a74 107c 087c 0a83 027d 0b74 0064  .}.t.|.|...}.t.d
-00004750: 086a 0174 026a 0374 1174 046a 057c 0b64  .j.t.j.t.t.j.|.d
-00004760: 098d 0483 0101 0064 0a64 0b64 0c7c 037c  .......d.d.d.|.|
-00004770: 0b67 057d 0c7c 016a 12a0 13a1 007d 0d7c  .g.}.|.j.....}.|
-00004780: 0d64 0d6b 0972 c87c 0ca0 1464 0e7c 0d67  .d.k.r.|...d.|.g
-00004790: 02a1 0101 007c 0464 066b 0872 da74 15a0  .....|.d.k.r.t..
-000047a0: 167c 0ca1 0101 0074 1764 0f64 108d 0101  .|.....t.d.d....
-000047b0: 006e 1a74 0064 116a 0174 1174 026a 1874  .n.t.d.j.t.t.j.t
-000047c0: 026a 037c 0364 128d 0483 0101 0064 0d53  .j.|.d.......d.S
-000047d0: 0029 137a 630a 2020 2020 2020 2020 3a74  .).zc.        :t
-000047e0: 7970 6520 636f 6e66 6967 3a20 5265 706f  ype config: Repo
-000047f0: 436f 6e66 6967 0a20 2020 2020 2020 203a  Config.        :
-00004800: 7061 7261 6d20 736f 7572 6365 5f6f 725f  param source_or_
-00004810: 6c61 7965 723a 2022 736f 7572 6365 2063  layer: "source c
-00004820: 6f64 6522 206f 7220 226c 6179 6572 220a  ode" or "layer".
-00004830: 2020 2020 2020 2020 7a48 7b63 7961 6e7d          zH{cyan}
-00004840: 7570 6c6f 6164 206c 616d 6264 6120 7b73  upload lambda {s
-00004850: 6f75 7263 655f 6f72 5f6c 6179 6572 7d20  ource_or_layer} 
-00004860: 6672 6f6d 207b 7265 7365 747d 7b70 6174  from {reset}{pat
-00004870: 687d 207b 6379 616e 7d74 6f20 4157 5320  h} {cyan}to AWS 
-00004880: 5333 2904 7236 0000 0072 3700 0000 da0f  S3).r6...r7.....
-00004890: 736f 7572 6365 5f6f 725f 6c61 7965 7272  source_or_layerr
-000048a0: 4200 0000 fa0b 736f 7572 6365 2063 6f64  B.....source cod
-000048b0: 65da 056c 6179 6572 fa06 7b7d 2e7a 6970  e..layer..{}.zip
-000048c0: 46a9 02da 0570 6172 7473 da06 6973 5f64  F....parts..is_d
-000048d0: 6972 7a24 7b63 7961 6e7d 7b74 6162 7d75  irz${cyan}{tab}u
-000048e0: 706c 6f61 6420 746f 207b 7265 7365 747d  pload to {reset}
-000048f0: 7b73 335f 7572 697d 2904 7236 0000 0072  {s3_uri}).r6...r
-00004900: 3a00 0000 7237 0000 00da 0673 335f 7572  :...r7.....s3_ur
-00004910: 6972 9000 0000 7291 0000 005a 0263 704e  ir....r....Z.cpN
-00004920: 7292 0000 0072 0500 0000 723c 0000 00fa  r....r....r<....
-00004930: 217b 7265 647d 7b74 6162 7d7b 7061 7468  !{red}{tab}{path
-00004940: 7d20 7b63 7961 6e7d 6e6f 7420 666f 756e  } {cyan}not foun
-00004950: 6421 a904 723a 0000 0072 6000 0000 7236  d!..r:...r`...r6
-00004960: 0000 0072 4200 0000 2919 7219 0000 0072  ...rB...).r....r
-00004970: 3e00 0000 7216 0000 0072 3f00 0000 7217  >...r....r?...r.
-00004980: 0000 0072 4000 0000 5a29 7333 5f75 7269  ...r@...Z)s3_uri
-00004990: 5f6c 616d 6264 615f 6465 706c 6f79 5f76  _lambda_deploy_v
-000049a0: 6572 7369 6f6e 6564 5f73 6f75 7263 655f  ersioned_source_
-000049b0: 6469 72da 2873 335f 7572 695f 6c61 6d62  dir.(s3_uri_lamb
-000049c0: 6461 5f64 6570 6c6f 795f 7665 7273 696f  da_deploy_versio
-000049d0: 6e65 645f 6c61 7965 725f 6469 7272 7b00  ned_layer_dirr{.
-000049e0: 0000 7241 0000 0072 4200 0000 7243 0000  ..rA...rB...rC..
-000049f0: 0072 0700 0000 da07 6f66 5f66 696c 6572  .r......of_filer
-00004a00: 1000 0000 7213 0000 0072 0f00 0000 7218  ....r....r....r.
-00004a10: 0000 00da 1d41 5753 5f4c 414d 4244 415f  .....AWS_LAMBDA_
-00004a20: 4445 504c 4f59 5f41 5753 5f50 524f 4649  DEPLOY_AWS_PROFI
-00004a30: 4c45 725a 0000 0072 9500 0000 7244 0000  LErZ...r....rD..
-00004a40: 0072 4500 0000 721a 0000 0072 6200 0000  .rE...r....rb...
-00004a50: 290e 7248 0000 0072 4900 0000 72b6 0000  ).rH...rI...r...
-00004a60: 0072 4200 0000 724a 0000 0072 2200 0000  .rB...rJ...r"...
-00004a70: 5a22 7333 5f75 7269 5f6c 616d 6264 615f  Z"s3_uri_lambda_
-00004a80: 6465 706c 6f79 5f76 6572 7369 6f6e 6564  deploy_versioned
-00004a90: 5f64 6972 da0a 736f 7572 6365 5f6d 6435  _dir..source_md5
-00004aa0: da06 6275 636b 6574 da06 7072 6566 6978  ..bucket..prefix
-00004ab0: da03 6b65 7972 bd00 0000 7221 0000 00da  ..keyr....r!....
-00004ac0: 0b61 7773 5f70 726f 6669 6c65 7220 0000  .aws_profiler ..
-00004ad0: 0072 2000 0000 7226 0000 00da 125f 7570  .r ...r&....._up
-00004ae0: 6c6f 6164 5f6c 616d 6264 615f 7a69 709a  load_lambda_zip.
-00004af0: 0300 0073 6200 0000 000c 0201 0401 0401  ...sb...........
-00004b00: 0401 0201 02fc 04ff 0408 0801 0801 0801  ................
-00004b10: 0802 0402 0c01 0a01 0c01 0201 0c01 02fe  ................
-00004b20: 0604 0a01 0201 0401 0401 0201 0401 02fc  ................
-00004b30: 04ff 0409 0200 0200 0201 0200 02fe 0404  ................
-00004b40: 0a01 0801 0e01 0801 0a01 0c02 0201 0401  ................
-00004b50: 0201 0401 0401 02fc 04ff 7a1a 4163 7469  ..........z.Acti
-00004b60: 6f6e 732e 5f75 706c 6f61 645f 6c61 6d62  ons._upload_lamb
-00004b70: 6461 5f7a 6970 7a2d 5570 6c6f 6164 2041  da_zipz-Upload A
-00004b80: 5753 204c 616d 6264 6120 736f 7572 6365  WS Lambda source
-00004b90: 2063 6f64 6520 7a69 7020 6669 6c65 2074   code zip file t
-00004ba0: 6f20 5333 2e63 0300 0000 0000 0000 0000  o S3.c..........
-00004bb0: 0000 0400 0000 0600 0000 4b00 0000 7320  ..........K...s 
-00004bc0: 0000 007c 006a 007c 0166 0164 017c 016a  ...|.j.|.f.d.|.j
-00004bd0: 017c 0264 029c 037c 0397 028e 0101 0064  .|.d...|.......d
-00004be0: 0353 0029 0472 3400 0000 72b7 0000 00a9  .S.).r4...r.....
-00004bf0: 0372 b600 0000 7242 0000 0072 4a00 0000  .r....rB...rJ...
-00004c00: 4e29 0272 c800 0000 72a9 0000 0072 4700  N).r....r....rG.
-00004c10: 0000 7220 0000 0072 2000 0000 7226 0000  ..r ...r ...r&..
-00004c20: 00da 1975 706c 6f61 645f 6c61 6d62 6461  ...upload_lambda
-00004c30: 5f73 6f75 7263 655f 636f 6465 d903 0000  _source_code....
-00004c40: 7312 0000 0000 0704 0102 ff02 0202 0104  s...............
-00004c50: 0102 fc04 0502 fb7a 2141 6374 696f 6e73  .......z!Actions
-00004c60: 2e75 706c 6f61 645f 6c61 6d62 6461 5f73  .upload_lambda_s
-00004c70: 6f75 7263 655f 636f 6465 6301 0000 0000  ource_codec.....
-00004c80: 0000 0000 0000 0003 0000 0008 0000 0043  ...............C
-00004c90: 0000 0073 6200 0000 7400 7308 7401 7256  ...sb...t.s.t.rV
-00004ca0: 7402 6a03 a004 6401 6402 6403 6404 a104  t.j...d.d.d.d...
-00004cb0: 7402 6a03 a004 6401 6402 6405 6403 6404  t.j...d.d.d.d.d.
-00004cc0: a105 6702 7d01 7c01 4400 5d18 7d02 7402  ..g.}.|.D.].}.t.
-00004cd0: 6a03 a005 7c02 a101 7232 7c02 0200 0100  j...|...r2|.....
-00004ce0: 5300 7132 7406 6406 8301 8201 6e08 7406  S.q2t.d.....n.t.
-00004cf0: 6407 8301 8201 6408 5300 2909 7a41 0a20  d.....d.S.).zA. 
-00004d00: 2020 2020 2020 2046 696e 6420 7468 6520         Find the 
-00004d10: 6162 736f 6c75 7465 2070 6174 6820 6f66  absolute path of
-00004d20: 2074 6865 2064 6f63 6b65 7220 6578 6563   the docker exec
-00004d30: 7574 6162 6c65 0a20 2020 2020 2020 20fa  utable.        .
-00004d40: 012f 5a03 7573 72da 0362 696e 5a06 646f  ./Z.usr..binZ.do
-00004d50: 636b 6572 da05 6c6f 6361 6c7a 3857 6520  cker..localz8We 
-00004d60: 6361 6e6e 6f74 2066 696e 6420 646f 636b  cannot find dock
-00004d70: 6572 2c20 6172 6520 796f 7520 7375 7265  er, are you sure
-00004d80: 2064 6f63 6b65 7220 6973 2069 6e73 7461   docker is insta
-00004d90: 6c6c 6564 3f7a 2e57 6520 6361 6e20 6f6e  lled?z.We can on
-00004da0: 6c79 2066 696e 6420 646f 636b 6572 2062  ly find docker b
-00004db0: 696e 206f 6e20 4d61 634f 5320 6f72 204c  in on MacOS or L
-00004dc0: 696e 7578 214e 2907 720a 0000 0072 0b00  inux!N).r....r..
-00004dd0: 0000 7241 0000 0072 4200 0000 728a 0000  ..rA...rB...r...
-00004de0: 0072 4300 0000 da10 456e 7669 726f 6e6d  .rC.....Environm
-00004df0: 656e 7445 7272 6f72 2903 7248 0000 005a  entError).rH...Z
-00004e00: 096c 6f63 6174 696f 6e73 7255 0000 0072  .locationsrU...r
-00004e10: 2000 0000 7220 0000 0072 2600 0000 da0c   ...r ...r&.....
-00004e20: 5f66 696e 645f 646f 636b 6572 e803 0000  _find_docker....
-00004e30: 7312 0000 0000 0408 0210 0112 fe04 0408  s...............
-00004e40: 010c 010a 010a 027a 1441 6374 696f 6e73  .......z.Actions
-00004e50: 2e5f 6669 6e64 5f64 6f63 6b65 727a 4642  ._find_dockerzFB
-00004e60: 7569 6c64 206c 616d 6264 6120 6c61 7965  uild lambda laye
-00004e70: 7220 7573 696e 6720 6120 4157 5320 6c61  r using a AWS la
-00004e80: 6d62 6461 2072 756e 7469 6d65 2063 6f6d  mbda runtime com
-00004e90: 7061 7469 626c 6520 646f 636b 6572 2069  patible docker i
-00004ea0: 6d61 6765 2e63 0300 0000 0000 0000 0000  mage.c..........
-00004eb0: 0000 0600 0000 0a00 0000 4b00 0000 73a2  ..........K...s.
-00004ec0: 0000 007c 01a0 007c 016a 016a 02a1 0101  ...|...|.j.j....
-00004ed0: 007c 01a0 007c 016a 036a 02a1 0101 0074  .|...|.j.j.....t
-00004ee0: 0464 016a 0574 066a 0774 086a 097c 016a  .d.j.t.j.t.j.|.j
-00004ef0: 01a0 0aa1 007c 016a 0b64 028d 0483 0101  .....|.j.d......
-00004f00: 0074 0c7c 016a 0d83 0101 007c 00a0 0ea1  .t.|.j.....|....
-00004f10: 007d 0474 0f6a 10a0 117c 016a 03a0 0aa1  .}.t.j...|.j....
-00004f20: 0064 0364 04a1 037d 057c 0264 056b 0872  .d.d...}.|.d.k.r
-00004f30: 9e74 12a0 137c 0464 0664 0764 08a0 057c  .t...|.d.d.d...|
-00004f40: 016a 147c 016a 03a0 0aa1 00a1 0264 097c  .j.|.j.......d.|
-00004f50: 016a 01a0 0aa1 0064 0a7c 0567 08a1 0101  .j.....d.|.g....
-00004f60: 0064 0b53 0029 0c72 3400 0000 7a59 7b63  .d.S.).r4...zY{c
-00004f70: 7961 6e7d 6275 696c 6420 6c61 6d62 6461  yan}build lambda
-00004f80: 206c 6179 6572 2069 6e20 7b72 6573 6574   layer in {reset
-00004f90: 7d7b 646f 636b 6572 5f69 6d61 6765 7d20  }{docker_image} 
-00004fa0: 7b63 7961 6e7d 646f 636b 6572 2063 6f6e  {cyan}docker con
-00004fb0: 7461 696e 6572 2061 7420 7b72 6573 6574  tainer at {reset
-00004fc0: 7d7b 7061 7468 7d29 0472 3600 0000 7237  }{path}).r6...r7
-00004fd0: 0000 005a 0c64 6f63 6b65 725f 696d 6167  ...Z.docker_imag
-00004fe0: 6572 4200 0000 72cc 0000 007a 2463 6f6e  erB...r....z$con
-00004ff0: 7461 696e 6572 2d6f 6e6c 792d 6275 696c  tainer-only-buil
-00005000: 642d 6c61 6d62 6461 2d6c 6179 6572 2e73  d-lambda-layer.s
-00005010: 6846 da03 7275 6e7a 022d 767a 057b 7d3a  hF..runz.-vz.{}:
-00005020: 7b7d 7a04 2d2d 726d 5a04 6261 7368 4e29  {}z.--rmZ.bashN)
-00005030: 155a 1465 6e73 7572 655f 6174 7472 5f6e  .Z.ensure_attr_n
-00005040: 6f74 5f6e 6f6e 655a 1d41 5753 5f4c 414d  ot_noneZ.AWS_LAM
-00005050: 4244 415f 4255 494c 445f 444f 434b 4552  BDA_BUILD_DOCKER
-00005060: 5f49 4d41 4745 7230 0000 005a 2b41 5753  _IMAGEr0...Z+AWS
-00005070: 5f4c 414d 4244 415f 4255 494c 445f 444f  _LAMBDA_BUILD_DO
-00005080: 434b 4552 5f49 4d41 4745 5f57 4f52 4b53  CKER_IMAGE_WORKS
-00005090: 5041 4345 5f44 4952 7219 0000 0072 3e00  PACE_DIRr....r>.
-000050a0: 0000 7216 0000 0072 3f00 0000 7217 0000  ..r....r?...r...
-000050b0: 0072 4000 0000 725a 0000 00da 1770 6174  .r@...rZ.....pat
-000050c0: 685f 6c61 6d62 6461 5f62 7569 6c64 5f6c  h_lambda_build_l
-000050d0: 6179 6572 720e 0000 0072 af00 0000 72cf  ayerr....r....r.
-000050e0: 0000 0072 4100 0000 7242 0000 0072 8a00  ...rA...rB...r..
-000050f0: 0000 7244 0000 0072 4500 0000 725d 0000  ..rD...rE...r]..
-00005100: 0029 0672 4800 0000 7249 0000 0072 4a00  .).rH...rI...rJ.
-00005110: 0000 7222 0000 005a 0f70 6174 685f 6269  ..r"...Z.path_bi
-00005120: 6e5f 646f 636b 6572 5a2a 636f 6e74 6169  n_dockerZ*contai
-00005130: 6e65 725f 6f6e 6c79 5f62 7569 6c64 5f6c  ner_only_build_l
-00005140: 6264 5f6c 6179 6572 5f73 6372 6970 745f  bd_layer_script_
-00005150: 7061 7468 7220 0000 0072 2000 0000 7226  pathr ...r ...r&
-00005160: 0000 00da 1262 7569 6c64 5f6c 616d 6264  .....build_lambd
-00005170: 615f 6c61 7965 72f8 0300 0073 3e00 0000  a_layer....s>...
-00005180: 0007 0e01 0e01 0201 0401 0401 0401 0801  ................
-00005190: 04fc 04ff 0408 0a02 0801 0601 0801 0201  ................
-000051a0: 02fd 0406 0801 0401 0200 0201 0200 0401  ................
-000051b0: 0401 08fe 0204 0200 0801 0200 02f9 7a1a  ..............z.
-000051c0: 4163 7469 6f6e 732e 6275 696c 645f 6c61  Actions.build_la
-000051d0: 6d62 6461 5f6c 6179 6572 7a27 5570 6c6f  mbda_layerz'Uplo
-000051e0: 6164 2041 5753 204c 616d 6264 6120 6c61  ad AWS Lambda la
-000051f0: 7965 7220 7a69 7020 6669 6c65 2074 6f20  yer zip file to 
-00005200: 5333 2e63 0300 0000 0000 0000 0000 0000  S3.c............
-00005210: 0400 0000 0600 0000 4b00 0000 7320 0000  ........K...s ..
-00005220: 007c 006a 007c 0166 0164 017c 016a 017c  .|.j.|.f.d.|.j.|
-00005230: 0264 029c 037c 0397 028e 0101 0064 0353  .d...|.......d.S
-00005240: 0029 0472 3400 0000 72b8 0000 0072 c900  .).r4...r....r..
-00005250: 0000 4e29 0272 c800 0000 72d1 0000 0072  ..N).r....r....r
-00005260: 4700 0000 7220 0000 0072 2000 0000 7226  G...r ...r ...r&
-00005270: 0000 00da 1375 706c 6f61 645f 6c61 6d62  .....upload_lamb
-00005280: 6461 5f6c 6179 6572 1d04 0000 7312 0000  da_layer....s...
-00005290: 0000 0704 0102 ff02 0202 0104 0102 fc04  ................
-000052a0: 0502 fb7a 1b41 6374 696f 6e73 2e75 706c  ...z.Actions.upl
-000052b0: 6f61 645f 6c61 6d62 6461 5f6c 6179 6572  oad_lambda_layer
-000052c0: 7a27 4465 706c 6f79 2072 6563 656e 746c  z'Deploy recentl
-000052d0: 7920 6275 696c 7420 4157 5320 6c61 6d62  y built AWS lamb
-000052e0: 6461 206c 6179 6572 2e63 0300 0000 0000  da layer.c......
-000052f0: 0000 0000 0000 0b00 0000 0f00 0000 4b00  ..............K.
-00005300: 0000 733c 0100 0074 0064 016a 0174 026a  ..s<...t.d.j.t.j
-00005310: 0374 046a 0564 028d 0283 0101 0074 066a  .t.j.d.......t.j
-00005320: 07a0 087c 016a 09a1 0190 0172 1c74 0aa0  ...|.j.....r.t..
-00005330: 0b7c 016a 09a1 017d 0474 0c7c 016a 0d83  .|.j...}.t.|.j..
-00005340: 015c 027d 057d 0674 0e7c 0664 03a0 017c  .\.}.}.t.|.d...|
-00005350: 04a1 0167 0264 0464 058d 027d 0774 0f7c  ...g.d.d...}.t.|
-00005360: 057c 0764 068d 027d 0874 0064 076a 0174  .|.d...}.t.d.j.t
-00005370: 026a 0374 1074 046a 057c 0864 088d 0483  .j.t.t.j.|.d....
-00005380: 0101 0064 0964 0a64 0b64 0c7c 016a 1164  ...d.d.d.d.|.j.d
-00005390: 0d64 0ea0 017c 016a 11a1 0164 0f64 10a0  .d...|.j...d.d..
-000053a0: 017c 016a 12a0 13a1 007c 07a1 0264 1164  .|.j.....|...d.d
-000053b0: 12a0 017c 016a 14a0 13a1 007c 016a 15a0  ...|.j.....|.j..
-000053c0: 13a1 00a1 0267 0b7d 097c 016a 16a0 13a1  .....g.}.|.j....
-000053d0: 007d 0a7c 0a64 136b 0972 e27c 09a0 1764  .}.|.d.k.r.|...d
-000053e0: 147c 0a67 02a1 0101 007c 0264 046b 0872  .|.g.....|.d.k.r
-000053f0: f474 18a0 197c 09a1 0101 0074 0064 156a  .t...|.....t.d.j
-00005400: 0174 026a 0374 1074 046a 057c 016a 1a64  .t.j.t.t.j.|.j.d
-00005410: 168d 0483 0101 0074 1b64 1764 188d 0101  .......t.d.d....
-00005420: 006e 1c74 0064 196a 0174 1074 026a 1c74  .n.t.d.j.t.t.j.t
-00005430: 026a 037c 016a 0964 1a8d 0483 0101 0064  .j.|.j.d.......d
-00005440: 1353 0029 1b72 3400 0000 7a36 7b63 7961  .S.).r4...z6{cya
-00005450: 6e7d 6465 706c 6f79 2061 206e 6577 2076  n}deploy a new v
-00005460: 6572 7369 6f6e 206f 6620 6c61 6d62 6461  ersion of lambda
-00005470: 206c 6179 6572 2066 726f 6d20 4157 5320   layer from AWS 
-00005480: 5333 7261 0000 0072 b900 0000 4672 ba00  S3ra...r....Fr..
-00005490: 0000 2902 72c4 0000 0072 c500 0000 7a75  ..).r....r....zu
-000054a0: 7b63 7961 6e7d 7b74 6162 7d72 756e 207b  {cyan}{tab}run {
-000054b0: 7265 7365 747d 2761 7773 206c 616d 6264  reset}'aws lambd
-000054c0: 6120 7075 626c 6973 682d 6c61 7965 722d  a publish-layer-
-000054d0: 7665 7273 696f 6e27 207b 6379 616e 7d63  version' {cyan}c
-000054e0: 6f6d 6d61 6e64 2c20 7072 6576 6965 7720  ommand, preview 
-000054f0: 6c61 7965 7220 6669 6c65 2061 7420 7b72  layer file at {r
-00005500: 6573 6574 7d7b 7333 5f63 6f6e 736f 6c65  eset}{s3_console
-00005510: 5f75 726c 7d29 0472 3600 0000 723a 0000  _url}).r6...r:..
-00005520: 0072 3700 0000 7294 0000 0072 9000 0000  .r7...r....r....
-00005530: da06 6c61 6d62 6461 7a15 7075 626c 6973  ..lambdaz.publis
-00005540: 682d 6c61 7965 722d 7665 7273 696f 6e7a  h-layer-versionz
-00005550: 0c2d 2d6c 6179 6572 2d6e 616d 657a 0d2d  .--layer-namez.-
-00005560: 2d64 6573 6372 6970 7469 6f6e 7a32 6465  -descriptionz2de
-00005570: 7065 6e64 656e 6379 206c 6179 6572 2066  pendency layer f
-00005580: 6f72 2061 6c6c 2066 756e 6374 696f 6e73  or all functions
-00005590: 2069 6e20 277b 7d27 2070 726f 6a65 6374   in '{}' project
-000055a0: 7a09 2d2d 636f 6e74 656e 747a 1453 3342  z.--contentz.S3B
-000055b0: 7563 6b65 743d 7b7d 2c53 334b 6579 3d7b  ucket={},S3Key={
-000055c0: 7d7a 152d 2d63 6f6d 7061 7469 626c 652d  }z.--compatible-
-000055d0: 7275 6e74 696d 6573 7a0b 7079 7468 6f6e  runtimesz.python
-000055e0: 7b7d 2e7b 7d4e 7292 0000 007a 307b 6379  {}.{}Nr....z0{cy
-000055f0: 616e 7d7b 7461 627d 6f70 656e 207b 7265  an}{tab}open {re
-00005600: 7365 747d 7b75 726c 7d20 7b63 7961 6e7d  set}{url} {cyan}
-00005610: 746f 2076 6965 7720 6c61 7965 7229 0472  to view layer).r
-00005620: 3600 0000 723a 0000 0072 3700 0000 da03  6...r:...r7.....
-00005630: 7572 6c72 0500 0000 723c 0000 0072 be00  urlr....r<...r..
-00005640: 0000 72bf 0000 0029 1d72 1900 0000 723e  ..r....).r....r>
-00005650: 0000 0072 1600 0000 723f 0000 0072 1700  ...r....r?...r..
-00005660: 0000 7240 0000 0072 4100 0000 7242 0000  ..r@...rA...rB..
-00005670: 0072 4300 0000 72d1 0000 0072 0700 0000  .rC...r....r....
-00005680: 72c1 0000 0072 1000 0000 72c0 0000 0072  r....r....r....r
-00005690: 1300 0000 7211 0000 0072 1800 0000 5a15  ....r....r....Z.
-000056a0: 6177 735f 6c61 6d62 6461 5f6c 6179 6572  aws_lambda_layer
-000056b0: 5f6e 616d 655a 1b41 5753 5f4c 414d 4244  _nameZ.AWS_LAMBD
-000056c0: 415f 4445 504c 4f59 5f53 335f 4255 434b  A_DEPLOY_S3_BUCK
-000056d0: 4554 725a 0000 005a 1044 4556 5f50 595f  ETrZ...Z.DEV_PY_
-000056e0: 5645 525f 4d41 4a4f 525a 1044 4556 5f50  VER_MAJORZ.DEV_P
-000056f0: 595f 5645 525f 4d49 4e4f 5272 c200 0000  Y_VER_MINORr....
-00005700: 7295 0000 0072 4400 0000 7245 0000 005a  r....rD...rE...Z
-00005710: 1875 726c 5f6c 616d 6264 615f 6c61 7965  .url_lambda_laye
-00005720: 725f 636f 6e73 6f6c 6572 1a00 0000 7262  r_consoler....rb
-00005730: 0000 0029 0b72 4800 0000 7249 0000 0072  ...).rH...rI...r
-00005740: 4a00 0000 7222 0000 0072 c300 0000 72c4  J...r"...r....r.
-00005750: 0000 0072 c500 0000 72c6 0000 0072 9400  ...r....r....r..
-00005760: 0000 7221 0000 0072 c700 0000 7220 0000  ..r!...r....r ..
-00005770: 0072 2000 0000 7226 0000 00da 1364 6570  .r ...r&.....dep
-00005780: 6c6f 795f 6c61 6d62 6461 5f6c 6179 6572  loy_lambda_layer
-00005790: 2c04 0000 737c 0000 0000 0702 0104 0104  ,...s|..........
-000057a0: 0104 fe04 ff04 0610 010c 010e 0102 010c  ................
-000057b0: 0102 fe06 040c 0102 0104 0104 0102 0104  ................
-000057c0: 0102 fc04 ff04 0902 0002 0002 0102 0004  ................
-000057d0: 0102 010a 0102 0004 0108 0002 ff02 0302  ................
-000057e0: 0004 0108 0108 fe02 f804 0d0a 0108 010e  ................
-000057f0: 0108 010a 0102 0104 0104 0102 0104 0104  ................
-00005800: fc04 ff04 080c 0202 0104 0102 0104 0104  ................
-00005810: 0104 fc04 ff7a 1b41 6374 696f 6e73 2e64  .....z.Actions.d
-00005820: 6570 6c6f 795f 6c61 6d62 6461 5f6c 6179  eploy_lambda_lay
-00005830: 6572 7a10 6275 642d 6c61 6d62 6461 2d6c  erz.bud-lambda-l
-00005840: 6179 6572 7a33 2a2a 2042 7569 6c64 2c20  ayerz3** Build, 
-00005850: 7570 6c6f 6164 2061 6e64 2064 6570 6c6f  upload and deplo
-00005860: 7920 6120 6e65 7720 4157 5320 6c61 6d62  y a new AWS lamb
-00005870: 6461 206c 6179 6572 2e63 0300 0000 0000  da layer.c......
-00005880: 0000 0000 0000 0400 0000 0400 0000 4b00  ..............K.
-00005890: 0000 733e 0000 007c 006a 007c 017c 0264  ..s>...|.j.|.|.d
-000058a0: 018d 0201 007c 006a 017c 0166 0164 027c  .....|.j.|.f.d.|
-000058b0: 0269 017c 0397 028e 0101 007c 006a 027c  .i.|.......|.j.|
-000058c0: 0166 0164 027c 0269 017c 0397 028e 0101  .f.d.|.i.|......
-000058d0: 0064 0353 0029 0472 3400 0000 727f 0000  .d.S.).r4...r...
-000058e0: 0072 4a00 0000 4e29 0372 d200 0000 72d3  .rJ...N).r....r.
-000058f0: 0000 0072 d600 0000 7247 0000 0072 2000  ...r....rG...r .
-00005900: 0000 7220 0000 0072 2600 0000 da20 6275  ..r ...r&.... bu
-00005910: 696c 645f 7570 6c6f 6164 5f64 6570 6c6f  ild_upload_deplo
-00005920: 795f 6c61 6d62 6461 5f6c 6179 6572 6e04  y_lambda_layern.
-00005930: 0000 7306 0000 0000 080e 0116 017a 2841  ..s..........z(A
-00005940: 6374 696f 6e73 2e62 7569 6c64 5f75 706c  ctions.build_upl
-00005950: 6f61 645f 6465 706c 6f79 5f6c 616d 6264  oad_deploy_lambd
-00005960: 615f 6c61 7965 7263 0200 0000 0000 0000  a_layerc........
-00005970: 0000 0000 0400 0000 0500 0000 4300 0000  ............C...
-00005980: 7334 0000 007c 016a 007c 016a 0167 027d  s4...|.j.|.j.g.}
-00005990: 027c 0244 005d 1e7d 0374 026a 03a0 047c  .|.D.].}.t.j...|
-000059a0: 03a1 0173 1074 0564 01a0 067c 03a1 0183  ...s.t.d...|....
-000059b0: 0182 0171 1064 0253 0029 0372 3400 0000  ...q.d.S.).r4...
-000059c0: 7a0d 7b7d 206e 6f74 2065 7869 7374 734e  z.{} not existsN
-000059d0: 2907 5a1c 7061 7468 5f61 7773 5f63 6861  ).Z.path_aws_cha
-000059e0: 6c69 6365 5f63 6f6e 6669 675f 6a73 6f6e  lice_config_json
-000059f0: 5a17 7061 7468 5f61 7773 5f63 6861 6c69  Z.path_aws_chali
-00005a00: 6365 5f61 7070 5f70 7972 4100 0000 7242  ce_app_pyrA...rB
-00005a10: 0000 0072 4300 0000 727b 0000 0072 3e00  ...rC...r{...r>.
-00005a20: 0000 2904 7248 0000 0072 4900 0000 da05  ..).rH...rI.....
-00005a30: 6669 6c65 7372 5500 0000 7220 0000 0072  filesrU...r ...r
-00005a40: 2000 0000 7226 0000 00da 1e5f 656e 7375   ...r&....._ensu
-00005a50: 7265 5f63 6861 6c69 6365 5f6c 616d 6264  re_chalice_lambd
-00005a60: 615f 6170 705f 6469 727a 0400 0073 0c00  a_app_dirz...s..
-00005a70: 0000 0005 0401 04fe 0404 0801 0c01 7a26  ..............z&
-00005a80: 4163 7469 6f6e 732e 5f65 6e73 7572 655f  Actions._ensure_
-00005a90: 6368 616c 6963 655f 6c61 6d62 6461 5f61  chalice_lambda_a
-00005aa0: 7070 5f64 6972 7a2a 2a2a 2044 6570 6c6f  pp_dirz*** Deplo
-00005ab0: 7920 4157 5320 4c61 6d62 6461 2061 7070  y AWS Lambda app
-00005ac0: 2077 6974 6820 4157 5320 4368 616c 6963   with AWS Chalic
-00005ad0: 652e 6303 0000 0000 0000 0000 0000 0006  e.c.............
-00005ae0: 0000 0005 0000 004b 0000 0073 9600 0000  .......K...s....
-00005af0: 7400 6401 6a01 7402 6a03 7404 6a05 6402  t.d.j.t.j.t.j.d.
-00005b00: 8d02 8301 0100 7c00 a006 7c01 a101 0100  ......|...|.....
-00005b10: 7407 7c01 6a08 8301 0100 7409 7c01 6a08  t.|.j.....t.|.j.
-00005b20: 8301 0100 740a 7c01 6a0b 7c01 6a0c 8302  ....t.|.j.|.j...
-00005b30: 0100 7c01 6a0d 6403 7c01 6a0e 6404 6704  ..|.j.d.|.j.d.g.
-00005b40: 7d04 7c04 a00f 7c03 6405 1900 a101 0100  }.|...|.d.......
-00005b50: 7c01 6a10 a011 a100 7d05 7c05 6406 6b09  |.j.....}.|.d.k.
-00005b60: 7280 7c04 a00f 6407 7c05 6702 a101 0100  r.|...d.|.g.....
-00005b70: 7c02 6408 6b08 7292 7412 a013 7c04 a101  |.d.k.r.t...|...
-00005b80: 0100 6406 5300 2909 7234 0000 007a 2c7b  ..d.S.).r4...z,{
-00005b90: 6379 616e 7d44 6570 6c6f 7920 4157 5320  cyan}Deploy AWS 
-00005ba0: 4c61 6d62 6461 2061 7070 2077 6974 6820  Lambda app with 
-00005bb0: 4157 5320 4368 616c 6963 6572 6100 0000  AWS Chalicera...
-00005bc0: fa0d 2d2d 7072 6f6a 6563 742d 6469 725a  ..--project-dirZ
-00005bd0: 0664 6570 6c6f 79da 055f 6172 6773 4e72  .deploy.._argsNr
-00005be0: 9200 0000 4629 1472 1900 0000 723e 0000  ....F).r....r>..
-00005bf0: 0072 1600 0000 723f 0000 0072 1700 0000  .r....r?...r....
-00005c00: 7240 0000 0072 d900 0000 720d 0000 005a  r@...r....r....Z
-00005c10: 1664 6972 5f61 7773 5f63 6861 6c69 6365  .dir_aws_chalice
-00005c20: 5f76 656e 646f 7272 0e00 0000 7215 0000  _vendorr....r...
-00005c30: 0072 ac00 0000 5a1d 6469 725f 6177 735f  .r....Z.dir_aws_
-00005c40: 6368 616c 6963 655f 7665 6e64 6f72 5f73  chalice_vendor_s
-00005c50: 6f75 7263 65da 1570 6174 685f 7665 6e76  ource..path_venv
-00005c60: 5f62 696e 5f63 6861 6c69 6365 da0e 6469  _bin_chalice..di
-00005c70: 725f 6c61 6d62 6461 5f61 7070 7295 0000  r_lambda_appr...
-00005c80: 0072 c200 0000 725a 0000 0072 4400 0000  .r....rZ...rD...
-00005c90: 7245 0000 00a9 0672 4800 0000 7249 0000  rE.....rH...rI..
-00005ca0: 0072 4a00 0000 7222 0000 0072 2100 0000  .rJ...r"...r!...
-00005cb0: 72c7 0000 0072 2000 0000 7220 0000 0072  r....r ...r ...r
-00005cc0: 2600 0000 da0e 6368 616c 6963 655f 6465  &.....chalice_de
-00005cd0: 706c 6f79 8604 0000 7330 0000 0000 0702  ploy....s0......
-00005ce0: 0104 0104 0104 fe04 ff04 070a 030a 010a  ................
-00005cf0: 0302 0104 0104 fe04 0704 0102 0004 0102  ................
-00005d00: fd04 050e 010a 0108 010e 0208 017a 1641  .............z.A
-00005d10: 6374 696f 6e73 2e63 6861 6c69 6365 5f64  ctions.chalice_d
-00005d20: 6570 6c6f 797a 2a2a 2a20 4465 6c65 7465  eployz*** Delete
-00005d30: 2041 5753 204c 616d 6264 6120 6170 7020   AWS Lambda app 
-00005d40: 7769 7468 2041 5753 2043 6861 6c69 6365  with AWS Chalice
-00005d50: 2e63 0300 0000 0000 0000 0000 0000 0600  .c..............
-00005d60: 0000 0500 0000 4b00 0000 7374 0000 0074  ......K...st...t
-00005d70: 0064 016a 0174 026a 0374 046a 0564 028d  .d.j.t.j.t.j.d..
-00005d80: 0283 0101 007c 00a0 067c 01a1 0101 007c  .....|...|.....|
-00005d90: 016a 0764 037c 016a 0864 0467 047d 047c  .j.d.|.j.d.g.}.|
-00005da0: 04a0 097c 0364 0519 00a1 0101 007c 016a  ...|.d.......|.j
-00005db0: 0aa0 0ba1 007d 057c 0564 066b 0972 5e7c  .....}.|.d.k.r^|
-00005dc0: 04a0 0964 077c 0567 02a1 0101 007c 0264  ...d.|.g.....|.d
-00005dd0: 086b 0872 7074 0ca0 0d7c 04a1 0101 0064  .k.rpt...|.....d
-00005de0: 0653 0029 0972 3400 0000 7a2c 7b63 7961  .S.).r4...z,{cya
-00005df0: 6e7d 4465 6c65 7465 2041 5753 204c 616d  n}Delete AWS Lam
-00005e00: 6264 6120 6170 7020 7769 7468 2041 5753  bda app with AWS
-00005e10: 2043 6861 6c69 6365 7261 0000 0072 da00   Chalicera...r..
-00005e20: 0000 da06 6465 6c65 7465 72db 0000 004e  ....deleter....N
-00005e30: 7292 0000 0046 290e 7219 0000 0072 3e00  r....F).r....r>.
-00005e40: 0000 7216 0000 0072 3f00 0000 7217 0000  ..r....r?...r...
-00005e50: 0072 4000 0000 72d9 0000 0072 dc00 0000  .r@...r....r....
-00005e60: 72dd 0000 0072 9500 0000 72c2 0000 0072  r....r....r....r
-00005e70: 5a00 0000 7244 0000 0072 4500 0000 72de  Z...rD...rE...r.
-00005e80: 0000 0072 2000 0000 7220 0000 0072 2600  ...r ...r ...r&.
-00005e90: 0000 da0e 6368 616c 6963 655f 6465 6c65  ....chalice_dele
-00005ea0: 7465 ae04 0000 7324 0000 0000 0702 0104  te....s$........
-00005eb0: 0104 0104 fe04 ff04 060a 0304 0102 0004  ................
-00005ec0: 0102 fd04 050e 010a 0108 010e 0208 017a  ...............z
-00005ed0: 1641 6374 696f 6e73 2e63 6861 6c69 6365  .Actions.chalice
-00005ee0: 5f64 656c 6574 654e 2901 4629 0146 2902  _deleteN).F).F).
-00005ef0: 4646 2901 4629 0146 2901 4629 0146 2901  FF).F).F).F).F).
-00005f00: 4629 0146 2901 4629 0146 2901 4629 0146  F).F).F).F).F).F
-00005f10: 2901 4629 0146 2901 4629 0146 2901 4629  ).F).F).F).F).F)
-00005f20: 0146 2901 4629 0146 2901 4629 0146 2901  .F).F).F).F).F).
-00005f30: 4629 0146 2901 4629 0146 2901 4629 0146  F).F).F).F).F).F
-00005f40: 2901 4629 0146 2901 4629 0146 2901 4629  ).F).F).F).F).F)
-00005f50: 0146 2901 4629 0146 2901 4629 2d72 2800  .F).F).F).F)-r(.
-00005f60: 0000 da0a 5f5f 6d6f 6475 6c65 5f5f da0c  ....__module__..
-00005f70: 5f5f 7175 616c 6e61 6d65 5f5f da07 5f5f  __qualname__..__
-00005f80: 646f 635f 5f72 3200 0000 724b 0000 0072  doc__r2...rK...r
-00005f90: 4c00 0000 7256 0000 0072 5b00 0000 725e  L...rV...r[...r^
-00005fa0: 0000 0072 5f00 0000 7265 0000 0072 6900  ...r_...re...ri.
-00005fb0: 0000 726b 0000 0072 6d00 0000 7270 0000  ..rk...rm...rp..
-00005fc0: 0072 7500 0000 7278 0000 0072 7900 0000  .ru...rx...ry...
-00005fd0: 727a 0000 0072 7c00 0000 727d 0000 0072  rz...r|...r}...r
-00005fe0: 7e00 0000 7280 0000 0072 8900 0000 728b  ~...r....r....r.
-00005ff0: 0000 0072 8c00 0000 728d 0000 0072 9700  ...r....r....r..
-00006000: 0000 729a 0000 0072 9b00 0000 72a1 0000  ..r....r....r...
-00006010: 0072 a500 0000 72a6 0000 0072 b500 0000  .r....r....r....
-00006020: 72c8 0000 0072 ca00 0000 72cf 0000 0072  r....r....r....r
-00006030: d200 0000 72d3 0000 0072 d600 0000 72d7  ....r....r....r.
-00006040: 0000 0072 d900 0000 72df 0000 0072 e100  ...r....r....r..
-00006050: 0000 7220 0000 0072 2000 0000 7220 0000  ..r ...r ...r ..
-00006060: 0072 2600 0000 7233 0000 0048 0000 0073  .r&...r3...H...s
-00006070: 4401 0000 0801 040c 0201 02ff 0403 0c24  D..............$
-00006080: 0201 02ff 0403 0c17 0201 02ff 0406 0001  ................
-00006090: 00fc 0c23 0201 02ff 0403 0c13 0201 02ff  ...#............
-000060a0: 0403 0c14 0201 02ff 0403 0c13 0201 02ff  ................
-000060b0: 0403 0c37 0201 02ff 0403 0c13 0201 02ff  ...7............
-000060c0: 0403 0c13 0201 02ff 0403 0c13 0201 02ff  ................
-000060d0: 0403 0c38 0201 0201 02fe 0404 0c13 0201  ...8............
-000060e0: 0201 02fe 0404 0c0a 0201 0201 02fe 0404  ................
-000060f0: 0c16 0201 0201 02fe 0404 0c0b 0201 02ff  ................
-00006100: 0403 0c14 0201 0201 02fe 0404 0c12 0201  ................
-00006110: 0201 02fe 0404 0c0a 0201 0201 02fe 0404  ................
-00006120: 0c13 0201 02ff 0403 0c17 0201 02ff 0403  ................
-00006130: 0c0c 0201 02ff 0403 0c0f 0201 02ff 0403  ................
-00006140: 0c22 00fa 0a51 0201 02ff 0403 0c0d 0201  ."...Q..........
-00006150: 02ff 0403 0c0d 0201 02ff 0403 0c13 0201  ................
-00006160: 0201 02fe 0404 0c27 0201 02ff 0403 0c0e  .......'........
-00006170: 0201 02ff 0403 0c29 00fb 0a3f 0201 02ff  .......)...?....
-00006180: 0403 0c0c 0810 0201 02ff 0403 0c22 0201  ............."..
-00006190: 02ff 0403 0c0c 0201 02ff 0403 0c3f 0201  .............?..
-000061a0: 0201 02fe 0404 0c08 080c 0201 02ff 0403  ................
-000061b0: 0c25 0201 02ff 0403 7233 0000 0029 024e  .%......r3...).N
-000061c0: 4e29 2d72 e400 0000 5a0a 5f5f 6675 7475  N)-r....Z.__futu
-000061d0: 7265 5f5f 7202 0000 0072 0300 0000 da06  re__r....r......
-000061e0: 7479 7069 6e67 da0b 496d 706f 7274 4572  typing..ImportEr
-000061f0: 726f 7272 4100 0000 7244 0000 0072 2c00  rorrA...rD...r,.
-00006200: 0000 da07 7a69 7066 696c 6572 0400 0000  ....zipfiler....
-00006210: 5a0c 706b 672e 6d69 6e69 5f73 6978 7206  Z.pkg.mini_sixr.
-00006220: 0000 005a 0f70 6b67 2e66 696e 6765 7270  ...Z.pkg.fingerp
-00006230: 7269 6e74 7207 0000 00da 0b72 6570 6f5f  rintr......repo_
-00006240: 636f 6e66 6967 7208 0000 005a 106f 7065  configr....Z.ope
-00006250: 7261 7469 6f6e 5f73 7973 7465 6d72 0900  ration_systemr..
-00006260: 0000 720a 0000 0072 0b00 0000 720c 0000  ..r....r....r...
-00006270: 005a 0768 656c 7065 7273 720d 0000 0072  .Z.helpersr....r
-00006280: 0e00 0000 720f 0000 0072 1000 0000 7211  ....r....r....r.
-00006290: 0000 0072 1200 0000 7213 0000 0072 1400  ...r....r....r..
-000062a0: 0000 7215 0000 005a 0b63 6f6c 6f72 5f70  ..r....Z.color_p
-000062b0: 7269 6e74 7216 0000 0072 1700 0000 7218  rintr....r....r.
-000062c0: 0000 0072 1900 0000 721a 0000 0072 1b00  ...r....r....r..
-000062d0: 0000 721c 0000 0072 1d00 0000 7232 0000  ..r....r....r2..
-000062e0: 00da 066f 626a 6563 7472 3300 0000 da07  ...objectr3.....
-000062f0: 6163 7469 6f6e 7372 2000 0000 7220 0000  actionsr ...r ..
-00006300: 0072 2000 0000 7226 0000 00da 083c 6d6f  .r ...r&.....<mo
-00006310: 6475 6c65 3e03 0000 0073 3a00 0000 0405  dule>....s:.....
-00006320: 1002 0201 0c01 0e01 0602 0801 0801 0801  ................
-00006330: 0c02 0c01 0c01 0c01 1804 2c0a 2807 0001  ..........,.(...
-00006340: 00fe 0a1d 107f 007f 007f 007f 007f 007f  ................
-00006350: 007f 007f 007f 000c                      ........
+000016f0: 8301 0100 6e2c 740e 7366 740f 7286 740b  ....n,t.sft.r.t.
+00001700: 6408 6a01 7402 6a03 7410 6a11 740c 7c01  d.j.t.j.t.j.t.|.
+00001710: 6a0d 8301 6409 8d03 8301 0100 6e04 7412  j...d.......n.t.
+00001720: 8201 740b 640a 6a01 7402 6a03 7410 6a11  ..t.d.j.t.j.t.j.
+00001730: 640b 8d02 8301 0100 7406 640c 7c01 6a13  d.......t.d.|.j.
+00001740: 8302 0100 7406 640d 7c01 6a14 8302 0100  ....t.d.|.j.....
+00001750: 640e 5300 290f 7234 0000 007a 507b 6379  d.S.).r4...zP{cy
+00001760: 616e 7d44 6973 706c 6179 2075 7365 6675  an}Display usefu
+00001770: 6c20 696e 666f 726d 6174 696f 6e2c 207b  l information, {
+00001780: 6772 6565 6e7d 7061 7468 2065 7869 7374  green}path exist
+00001790: 737b 6379 616e 7d2c 207b 7265 647d 7061  s{cyan}, {red}pa
+000017a0: 7468 206e 6f74 2065 7869 7374 7329 0372  th not exists).r
+000017b0: 3600 0000 5a05 6772 6565 6eda 0372 6564  6...Z.green..red
+000017c0: 7a1d 7669 7274 7561 6c20 656e 7669 726f  z.virtual enviro
+000017d0: 6e6d 656e 7420 6469 7265 6374 6f72 797a  nment directoryz
+000017e0: 1b76 656e 7620 7079 7468 6f6e 2065 7865  .venv python exe
+000017f0: 6375 7461 626c 6520 7061 7468 7a18 7665  cutable pathz.ve
+00001800: 6e76 2070 6970 2065 7865 6375 7461 626c  nv pip executabl
+00001810: 6520 7061 7468 7a25 2d20 7b63 7961 6e7d  e pathz%- {cyan}
+00001820: 6163 7469 7661 7465 2076 656e 7620 636f  activate venv co
+00001830: 6d6d 616e 643a 207b 7061 7468 7d29 0272  mmand: {path}).r
+00001840: 3600 0000 7242 0000 007a 332d 207b 6379  6...rB...z3- {cy
+00001850: 616e 7d61 6374 6976 6174 6520 7665 6e76  an}activate venv
+00001860: 2063 6f6d 6d61 6e64 3a20 7b72 6573 6574   command: {reset
+00001870: 7d73 6f75 7263 6520 7b70 6174 687d 724e  }source {path}rN
+00001880: 0000 007a 322d 207b 6379 616e 7d64 6561  ...z2- {cyan}dea
+00001890: 6374 6976 6174 6520 7665 6e76 2063 6f6d  ctivate venv com
+000018a0: 6d61 6e64 3a20 7b72 6573 6574 7d64 6561  mand: {reset}dea
+000018b0: 6374 6976 6174 65a9 0272 3600 0000 7237  ctivate..r6...r7
+000018c0: 0000 007a 1773 6974 652d 7061 636b 6167  ...z.site-packag
+000018d0: 6573 2064 6972 6563 746f 7279 7a19 7369  es directoryz.si
+000018e0: 7465 2d70 6163 6b61 6765 7336 3420 6469  te-packages64 di
+000018f0: 7265 6374 6f72 794e 2915 7219 0000 0072  rectoryN).r....r
+00001900: 3e00 0000 7216 0000 0072 3f00 0000 5a05  >...r....r?...Z.
+00001910: 4752 4545 4eda 0352 4544 721b 0000 0072  GREEN..REDr....r
+00001920: 3800 0000 da14 7061 7468 5f76 656e 765f  8.....path_venv_
+00001930: 6269 6e5f 7079 7468 6f6e 7246 0000 0072  bin_pythonrF...r
+00001940: 0900 0000 721c 0000 0072 1d00 0000 5a16  ....r....r....Z.
+00001950: 7061 7468 5f76 656e 765f 6269 6e5f 6163  path_venv_bin_ac
+00001960: 7469 7661 7465 720a 0000 0072 0b00 0000  tivater....r....
+00001970: 7217 0000 0072 4000 0000 da13 4e6f 7449  r....r@.....NotI
+00001980: 6d70 6c65 6d65 6e74 6564 4572 726f 725a  mplementedErrorZ
+00001990: 1664 6972 5f76 656e 765f 7369 7465 5f70  .dir_venv_site_p
+000019a0: 6163 6b61 6765 735a 1964 6972 5f76 656e  ackagesZ.dir_ven
+000019b0: 765f 7369 7465 5f70 6163 6b61 6765 735f  v_site_packages_
+000019c0: 3634 7247 0000 0072 2000 0000 7220 0000  64rG...r ...r ..
+000019d0: 0072 2600 0000 da04 696e 666f ff00 0000  .r&.....info....
+000019e0: 7362 0000 0000 0702 0104 0104 0104 0104  sb..............
+000019f0: fd04 ff04 0702 0102 0104 fe04 0402 0102  ................
+00001a00: 0104 fe04 0402 0102 0104 fe04 0404 0102  ................
+00001a10: 0104 0104 0108 fe04 ff06 0608 0102 0104  ................
+00001a20: 0104 0104 0108 fd04 ff06 0804 0202 0104  ................
+00001a30: 0104 0104 fe04 ff04 0602 0102 0104 fe04  ................
+00001a40: 0402 0102 0104 fe7a 0c41 6374 696f 6e73  .......z.Actions
+00001a50: 2e69 6e66 6f7a 332a 2a20 496e 7374 616c  .infoz3** Instal
+00001a60: 6c20 6465 7620 6465 7065 6e64 656e 6369  l dev dependenci
+00001a70: 6573 2069 6e20 7265 7175 6972 656d 656e  es in requiremen
+00001a80: 7473 2d64 6576 2e74 7874 6303 0000 0000  ts-dev.txtc.....
+00001a90: 0000 0000 0000 0004 0000 0006 0000 004b  ...............K
+00001aa0: 0000 0073 4200 0000 7400 6401 6a01 7402  ...sB...t.d.j.t.
+00001ab0: 6a03 7404 6a05 6402 8d02 8301 0100 7c02  j.t.j.d.......|.
+00001ac0: 6403 6b08 7234 7406 a007 7c01 6a08 6404  d.k.r4t...|.j.d.
+00001ad0: 6405 7c01 6a09 6704 a101 0100 740a 6406  d.|.j.g.....t.d.
+00001ae0: 6407 8d01 0100 6408 5300 a909 7234 0000  d.....d.S...r4..
+00001af0: 007a 477b 6379 616e 7d69 6e73 7461 6c6c  .zG{cyan}install
+00001b00: 2064 6570 656e 6465 6e63 6965 7320 696e   dependencies in
+00001b10: 207b 7265 7365 747d 7265 7175 6972 656d   {reset}requirem
+00001b20: 656e 7473 2d64 6576 2e74 7874 2074 6f20  ents-dev.txt to 
+00001b30: 7669 7274 7561 6c65 6e76 7261 0000 0046  virtualenvra...F
+00001b40: 723b 0000 00fa 022d 7272 0500 0000 723c  r;.....-rr....r<
+00001b50: 0000 004e 290b 7219 0000 0072 3e00 0000  ...N).r....r>...
+00001b60: 7216 0000 0072 3f00 0000 7217 0000 0072  r....r?...r....r
+00001b70: 4000 0000 7244 0000 0072 4500 0000 7246  @...rD...rE...rF
+00001b80: 0000 00da 1a70 6174 685f 7265 7175 6972  .....path_requir
+00001b90: 656d 656e 7473 5f64 6576 5f66 696c 6572  ements_dev_filer
+00001ba0: 1a00 0000 7247 0000 0072 2000 0000 7220  ....rG...r ...r 
+00001bb0: 0000 0072 2600 0000 da07 7265 715f 6465  ...r&.....req_de
+00001bc0: 763a 0100 0073 1c00 0000 0007 0201 0401  v:...s..........
+00001bd0: 0401 04fe 04ff 0406 0801 0401 0401 0201  ................
+00001be0: 0201 04fc 0606 7a0f 4163 7469 6f6e 732e  ......z.Actions.
+00001bf0: 7265 715f 6465 767a 3049 6e73 7461 6c6c  req_devz0Install
+00001c00: 2064 6f63 2064 6570 656e 6465 6e63 6965   doc dependencie
+00001c10: 7320 696e 2072 6571 7569 7265 6d65 6e74  s in requirement
+00001c20: 732d 646f 632e 7478 7463 0300 0000 0000  s-doc.txtc......
+00001c30: 0000 0000 0000 0400 0000 0600 0000 4b00  ..............K.
+00001c40: 0000 7342 0000 0074 0064 016a 0174 026a  ..sB...t.d.j.t.j
+00001c50: 0374 046a 0564 028d 0283 0101 007c 0264  .t.j.d.......|.d
+00001c60: 036b 0872 3474 06a0 077c 016a 0864 0464  .k.r4t...|.j.d.d
+00001c70: 057c 016a 0967 04a1 0101 0074 0a64 0664  .|.j.g.....t.d.d
+00001c80: 078d 0101 0064 0853 0029 0972 3400 0000  .....d.S.).r4...
+00001c90: 7a47 7b63 7961 6e7d 696e 7374 616c 6c20  zG{cyan}install 
+00001ca0: 6465 7065 6e64 656e 6369 6573 2069 6e20  dependencies in 
+00001cb0: 7b72 6573 6574 7d72 6571 7569 7265 6d65  {reset}requireme
+00001cc0: 6e74 732d 646f 632e 7478 7420 746f 2076  nts-doc.txt to v
+00001cd0: 6972 7475 616c 656e 7672 6100 0000 4672  irtualenvra...Fr
+00001ce0: 3b00 0000 7267 0000 0072 0500 0000 723c  ;...rg...r....r<
+00001cf0: 0000 004e 290b 7219 0000 0072 3e00 0000  ...N).r....r>...
+00001d00: 7216 0000 0072 3f00 0000 7217 0000 0072  r....r?...r....r
+00001d10: 4000 0000 7244 0000 0072 4500 0000 7246  @...rD...rE...rF
+00001d20: 0000 00da 1a70 6174 685f 7265 7175 6972  .....path_requir
+00001d30: 656d 656e 7473 5f64 6f63 5f66 696c 6572  ements_doc_filer
+00001d40: 1a00 0000 7247 0000 0072 2000 0000 7220  ....rG...r ...r 
+00001d50: 0000 0072 2600 0000 da07 7265 715f 646f  ...r&.....req_do
+00001d60: 6350 0100 0073 1c00 0000 0007 0201 0401  cP...s..........
+00001d70: 0401 04fe 04ff 0406 0801 0401 0401 0201  ................
+00001d80: 0201 04fc 0606 7a0f 4163 7469 6f6e 732e  ......z.Actions.
+00001d90: 7265 715f 646f 637a 3149 6e73 7461 6c6c  req_docz1Install
+00001da0: 2064 6576 2064 6570 656e 6465 6e63 6965   dev dependencie
+00001db0: 7320 696e 2072 6571 7569 7265 6d65 6e74  s in requirement
+00001dc0: 732d 7465 7374 2e74 7874 6303 0000 0000  s-test.txtc.....
+00001dd0: 0000 0000 0000 0004 0000 0006 0000 004b  ...............K
+00001de0: 0000 0073 4200 0000 7400 6401 6a01 7402  ...sB...t.d.j.t.
+00001df0: 6a03 7404 6a05 6402 8d02 8301 0100 7c02  j.t.j.d.......|.
+00001e00: 6403 6b08 7234 7406 a007 7c01 6a08 6404  d.k.r4t...|.j.d.
+00001e10: 6405 7c01 6a09 6704 a101 0100 740a 6406  d.|.j.g.....t.d.
+00001e20: 6407 8d01 0100 6408 5300 7266 0000 0029  d.....d.S.rf...)
+00001e30: 0b72 1900 0000 723e 0000 0072 1600 0000  .r....r>...r....
+00001e40: 723f 0000 0072 1700 0000 7240 0000 0072  r?...r....r@...r
+00001e50: 4400 0000 7245 0000 0072 4600 0000 da1b  D...rE...rF.....
+00001e60: 7061 7468 5f72 6571 7569 7265 6d65 6e74  path_requirement
+00001e70: 735f 7465 7374 5f66 696c 6572 1a00 0000  s_test_filer....
+00001e80: 7247 0000 0072 2000 0000 7220 0000 0072  rG...r ...r ...r
+00001e90: 2600 0000 da08 7265 715f 7465 7374 6601  &.....req_testf.
+00001ea0: 0000 731c 0000 0000 0702 0104 0104 0104  ..s.............
+00001eb0: fe04 ff04 0608 0104 0104 0102 0102 0104  ................
+00001ec0: fc06 067a 1041 6374 696f 6e73 2e72 6571  ...z.Actions.req
+00001ed0: 5f74 6573 747a 2144 6973 706c 6179 2072  _testz!Display r
+00001ee0: 6571 7569 7265 6d65 6e74 7320 6669 6c65  equirements file
+00001ef0: 2063 6f6e 7465 6e74 6303 0000 0000 0000   contentc.......
+00001f00: 0000 0000 0004 0000 0005 0000 004b 0000  .............K..
+00001f10: 0073 cc00 0000 7400 6401 6a01 7402 6a03  .s....t.d.j.t.j.
+00001f20: 7404 6a05 6402 8d02 8301 0100 7406 8300  t.j.d.......t...
+00001f30: 0100 7407 a008 6403 7c01 6a09 6702 a101  ..t...d.|.j.g...
+00001f40: 0100 7406 8300 0100 7400 6404 6a01 7402  ..t.....t.d.j.t.
+00001f50: 6a03 7404 6a05 6402 8d02 8301 0100 7406  j.t.j.d.......t.
+00001f60: 8300 0100 7407 a008 6403 7c01 6a0a 6702  ....t...d.|.j.g.
+00001f70: a101 0100 7406 8300 0100 7400 6405 6a01  ....t.....t.d.j.
+00001f80: 7402 6a03 7404 6a05 6402 8d02 8301 0100  t.j.t.j.d.......
+00001f90: 7406 8300 0100 7407 a008 6403 7c01 6a0b  t.....t...d.|.j.
+00001fa0: 6702 a101 0100 7406 8300 0100 7400 6406  g.....t.....t.d.
+00001fb0: 6a01 7402 6a03 7404 6a05 6402 8d02 8301  j.t.j.t.j.d.....
+00001fc0: 0100 7406 8300 0100 7407 a008 6403 7c01  ..t.....t...d.|.
+00001fd0: 6a0c 6702 a101 0100 7406 8300 0100 6407  j.g.....t.....d.
+00001fe0: 5300 2908 7234 0000 007a 2d7b 6379 616e  S.).r4...z-{cyan
+00001ff0: 7d64 6570 656e 6465 6e63 6965 7320 696e  }dependencies in
+00002000: 207b 7265 7365 747d 7265 7175 6972 656d   {reset}requirem
+00002010: 656e 7473 2e74 7874 7261 0000 00da 0363  ents.txtra.....c
+00002020: 6174 7a31 7b63 7961 6e7d 6465 7065 6e64  atz1{cyan}depend
+00002030: 656e 6369 6573 2069 6e20 7b72 6573 6574  encies in {reset
+00002040: 7d72 6571 7569 7265 6d65 6e74 732d 6465  }requirements-de
+00002050: 762e 7478 747a 317b 6379 616e 7d64 6570  v.txtz1{cyan}dep
+00002060: 656e 6465 6e63 6965 7320 696e 207b 7265  endencies in {re
+00002070: 7365 747d 7265 7175 6972 656d 656e 7473  set}requirements
+00002080: 2d64 6f63 2e74 7874 7a32 7b63 7961 6e7d  -doc.txtz2{cyan}
+00002090: 6465 7065 6e64 656e 6369 6573 2069 6e20  dependencies in 
+000020a0: 7b72 6573 6574 7d72 6571 7569 7265 6d65  {reset}requireme
+000020b0: 6e74 732d 7465 7374 2e74 7874 4e29 0d72  nts-test.txtN).r
+000020c0: 1900 0000 723e 0000 0072 1600 0000 723f  ....r>...r....r?
+000020d0: 0000 0072 1700 0000 7240 0000 00da 0570  ...r....r@.....p
+000020e0: 7269 6e74 7244 0000 0072 4500 0000 5a16  rintrD...rE...Z.
+000020f0: 7061 7468 5f72 6571 7569 7265 6d65 6e74  path_requirement
+00002100: 735f 6669 6c65 7268 0000 0072 6a00 0000  s_filerh...rj...
+00002110: 726c 0000 0072 4700 0000 7220 0000 0072  rl...rG...r ...r
+00002120: 2000 0000 7226 0000 00da 0872 6571 5f69   ...r&.....req_i
+00002130: 6e66 6f7c 0100 0073 6000 0000 0007 0201  nfo|...s`.......
+00002140: 0401 0401 04fe 04ff 0406 0601 0401 0201  ................
+00002150: 04fe 0604 0602 0201 0401 0401 04fe 04ff  ................
+00002160: 0406 0601 0401 0201 04fe 0604 0602 0201  ................
+00002170: 0401 0401 04fe 04ff 0406 0601 0401 0201  ................
+00002180: 04fe 0604 0602 0201 0401 0401 04fe 04ff  ................
+00002190: 0406 0601 0401 0201 04fe 0604 7a10 4163  ............z.Ac
+000021a0: 7469 6f6e 732e 7265 715f 696e 666f 7a09  tions.req_infoz.
+000021b0: 7465 7374 2d6f 6e6c 797a 1a52 756e 2075  test-onlyz.Run u
+000021c0: 6e69 7420 7465 7374 2077 6974 6820 7079  nit test with py
+000021d0: 7465 7374 2e29 0272 3000 0000 722f 0000  test.).r0...r/..
+000021e0: 0063 0300 0000 0000 0000 0000 0000 0400  .c..............
+000021f0: 0000 0600 0000 4b00 0000 7344 0000 0074  ......K...sD...t
+00002200: 0064 016a 0174 026a 0374 046a 057c 016a  .d.j.t.j.t.j.|.j
+00002210: 0664 028d 0383 0101 007c 0264 036b 0872  .d.......|.d.k.r
+00002220: 3674 07a0 087c 016a 097c 016a 0664 0467  6t...|.j.|.j.d.g
+00002230: 03a1 0101 0074 0a64 0564 068d 0101 0064  .....t.d.d.....d
+00002240: 0753 0029 0872 3400 0000 7a29 7b63 7961  .S.).r4...z){cya
+00002250: 6e7d 5275 6e20 756e 6974 2074 6573 7420  n}Run unit test 
+00002260: 696e 207b 7265 7365 747d 7b64 6972 5f74  in {reset}{dir_t
+00002270: 6573 7473 7da9 0372 3600 0000 7237 0000  ests}..r6...r7..
+00002280: 00da 0964 6972 5f74 6573 7473 46fa 022d  ...dir_testsF..-
+00002290: 7372 0500 0000 723c 0000 004e 290b 7219  sr....r<...N).r.
+000022a0: 0000 0072 3e00 0000 7216 0000 0072 3f00  ...r>...r....r?.
+000022b0: 0000 7217 0000 0072 4000 0000 7272 0000  ..r....r@...rr..
+000022c0: 0072 4400 0000 7245 0000 00da 1470 6174  .rD...rE.....pat
+000022d0: 685f 7665 6e76 5f62 696e 5f70 7974 6573  h_venv_bin_pytes
+000022e0: 7472 1a00 0000 7247 0000 0072 2000 0000  tr....rG...r ...
+000022f0: 7220 0000 0072 2600 0000 da10 7465 7374  r ...r&.....test
+00002300: 5f70 7974 6573 745f 6f6e 6c79 b701 0000  _pytest_only....
+00002310: 731c 0000 0000 0802 0104 0104 0104 0104  s...............
+00002320: fd04 ff04 0708 0104 0104 0104 0102 fd06  ................
+00002330: 057a 1841 6374 696f 6e73 2e74 6573 745f  .z.Actions.test_
+00002340: 7079 7465 7374 5f6f 6e6c 79da 0474 6573  pytest_only..tes
+00002350: 747a 382a 2a20 5275 6e20 756e 6974 2074  tz8** Run unit t
+00002360: 6573 7420 7769 7468 2070 7974 6573 742e  est with pytest.
+00002370: 2053 7461 7274 206f 7665 722c 2072 6575   Start over, reu
+00002380: 7365 206e 6f74 6869 6e67 2e63 0300 0000  se nothing.c....
+00002390: 0000 0000 0000 0000 0400 0000 0400 0000  ................
+000023a0: 4b00 0000 7358 0000 007c 006a 007c 0166  K...sX...|.j.|.f
+000023b0: 0164 017c 0269 017c 0397 028e 0101 007c  .d.|.i.|.......|
+000023c0: 006a 017c 0166 0164 017c 0269 017c 0397  .j.|.f.d.|.i.|..
+000023d0: 028e 0101 007c 0264 026b 0872 3e74 027c  .....|.d.k.r>t.|
+000023e0: 016a 0383 0101 007c 006a 047c 0166 0164  .j.....|.j.|.f.d
+000023f0: 017c 0269 017c 0397 028e 0101 0064 0353  .|.i.|.......d.S
+00002400: 00a9 0472 3400 0000 724a 0000 0046 4e29  ...r4...rJ...FN)
+00002410: 0572 6d00 0000 725e 0000 0072 0d00 0000  .rm...r^...r....
+00002420: 7252 0000 0072 7500 0000 7247 0000 0072  rR...ru...rG...r
+00002430: 2000 0000 7220 0000 0072 2600 0000 da0b   ...r ...r&.....
+00002440: 7465 7374 5f70 7974 6573 74ce 0100 0073  test_pytest....s
+00002450: 0a00 0000 0008 1601 1601 0801 0a01 7a13  ..............z.
+00002460: 4163 7469 6f6e 732e 7465 7374 5f70 7974  Actions.test_pyt
+00002470: 6573 747a 0863 6f76 2d6f 6e6c 797a 2152  estz.cov-onlyz!R
+00002480: 756e 2063 6f64 6520 636f 7665 7261 6765  un code coverage
+00002490: 2074 6573 7420 696e 2070 7974 6573 742e   test in pytest.
+000024a0: 6303 0000 0000 0000 0000 0000 0004 0000  c...............
+000024b0: 000c 0000 004b 0000 0073 6200 0000 7400  .....K...sb...t.
+000024c0: 6401 6a01 7402 6a03 7404 6a05 7c01 6a06  d.j.t.j.t.j.|.j.
+000024d0: 6402 8d03 8301 0100 7c02 6403 6b08 7254  d.......|.d.k.rT
+000024e0: 7407 a008 7c01 6a09 7c01 6a06 6404 6405  t...|.j.|.j.d.d.
+000024f0: a001 7c01 6a0a a00b a100 a101 6406 6407  ..|.j.......d.d.
+00002500: 6406 6408 a001 7c01 6a0c a101 6708 a101  d.d...|.j...g...
+00002510: 0100 740d 6409 640a 8d01 0100 640b 5300  ..t.d.d.....d.S.
+00002520: 290c 7234 0000 007a 327b 6379 616e 7d52  ).r4...z2{cyan}R
+00002530: 756e 2063 6f64 6520 636f 7665 7261 6765  un code coverage
+00002540: 2074 6573 7420 696e 207b 7265 7365 747d   test in {reset}
+00002550: 7b64 6972 5f74 6573 7473 7d72 7100 0000  {dir_tests}rq...
+00002560: 4672 7300 0000 7a08 2d2d 636f 763d 7b7d  Frs...z.--cov={}
+00002570: 7a0c 2d2d 636f 762d 7265 706f 7274 7a0c  z.--cov-reportz.
+00002580: 7465 726d 2d6d 6973 7369 6e67 7a07 6874  term-missingz.ht
+00002590: 6d6c 3a7b 7d72 0500 0000 723c 0000 004e  ml:{}r....r<...N
+000025a0: 290e 7219 0000 0072 3e00 0000 7216 0000  ).r....r>...r...
+000025b0: 0072 3f00 0000 7217 0000 0072 4000 0000  .r?...r....r@...
+000025c0: 7272 0000 0072 4400 0000 7245 0000 0072  rr...rD...rE...r
+000025d0: 7400 0000 7259 0000 0072 5a00 0000 5a11  t...rY...rZ...Z.
+000025e0: 6469 725f 636f 7665 7261 6765 5f68 746d  dir_coverage_htm
+000025f0: 6c72 1a00 0000 7247 0000 0072 2000 0000  lr....rG...r ...
+00002600: 7220 0000 0072 2600 0000 da0d 7465 7374  r ...r&.....test
+00002610: 5f63 6f76 5f6f 6e6c 79dc 0100 0073 2600  _cov_only....s&.
+00002620: 0000 0008 0201 0401 0401 0401 04fd 04ff  ................
+00002630: 0407 0801 0401 0401 0401 0201 0e01 0200  ................
+00002640: 0201 0200 0afa 0608 7a15 4163 7469 6f6e  ........z.Action
+00002650: 732e 7465 7374 5f63 6f76 5f6f 6e6c 795a  s.test_cov_onlyZ
+00002660: 0363 6f76 7a3f 2a2a 2052 756e 2063 6f64  .covz?** Run cod
+00002670: 6520 636f 7665 7261 6765 2074 6573 7420  e coverage test 
+00002680: 696e 2070 7974 6573 742e 2053 7461 7274  in pytest. Start
+00002690: 206f 7665 722c 2072 6575 7365 206e 6f74   over, reuse not
+000026a0: 6869 6e67 2e63 0300 0000 0000 0000 0000  hing.c..........
+000026b0: 0000 0400 0000 0400 0000 4b00 0000 7362  ..........K...sb
+000026c0: 0000 007c 006a 007c 0166 0164 017c 0269  ...|.j.|.f.d.|.i
+000026d0: 017c 0397 028e 0101 007c 006a 017c 0166  .|.......|.j.|.f
+000026e0: 0164 017c 0269 017c 0397 028e 0101 007c  .d.|.i.|.......|
+000026f0: 0264 026b 0872 4874 027c 016a 0383 0101  .d.k.rHt.|.j....
+00002700: 0074 027c 016a 0483 0101 007c 006a 057c  .t.|.j.....|.j.|
+00002710: 0166 0164 017c 0269 017c 0397 028e 0101  .f.d.|.i.|......
+00002720: 0064 0353 0072 7700 0000 2906 726d 0000  .d.S.rw...).rm..
+00002730: 0072 5e00 0000 720d 0000 0072 5200 0000  .r^...r....rR...
+00002740: 7251 0000 0072 7900 0000 7247 0000 0072  rQ...ry...rG...r
+00002750: 2000 0000 7220 0000 0072 2600 0000 da08   ...r ...r&.....
+00002760: 7465 7374 5f63 6f76 f601 0000 730c 0000  test_cov....s...
+00002770: 0000 0816 0116 0108 010a 010a 017a 1041  .............z.A
+00002780: 6374 696f 6e73 2e74 6573 745f 636f 767a  ctions.test_covz
+00002790: 312a 2a20 5669 6577 2063 6f64 6520 636f  1** View code co
+000027a0: 7665 7261 6765 2074 6573 7420 7265 7375  verage test resu
+000027b0: 6c74 2069 6e20 7765 6220 6272 6f77 7365  lt in web browse
+000027c0: 722e 6303 0000 0000 0000 0000 0000 0004  r.c.............
+000027d0: 0000 0006 0000 004b 0000 0073 5600 0000  .......K...sV...
+000027e0: 7400 6401 6a01 7402 6a03 7404 6a05 7c01  t.d.j.t.j.t.j.|.
+000027f0: 6a06 6402 8d03 8301 0100 7407 6a08 a009  j.d.......t.j...
+00002800: 7c01 6a06 a101 7330 740a 6403 8301 8201  |.j...s0t.d.....
+00002810: 7c02 6404 6b08 7248 740b a00c 740d 7c01  |.d.k.rHt...t.|.
+00002820: 6a06 6702 a101 0100 740e 6405 6406 8d01  j.g.....t.d.d...
+00002830: 0100 6407 5300 2908 7234 0000 007a 4f7b  ..d.S.).r4...zO{
+00002840: 6379 616e 7d4f 7065 6e20 636f 6465 2063  cyan}Open code c
+00002850: 6f76 6572 6167 6520 7465 7374 2068 746d  overage test htm
+00002860: 6c20 7265 7375 6c74 2069 6e20 7765 6220  l result in web 
+00002870: 6272 6f77 7365 727b 7265 7365 747d 7b63  browser{reset}{c
+00002880: 6f76 5f68 746d 6c5f 696e 6465 787d 2903  ov_html_index}).
+00002890: 7236 0000 0072 3700 0000 5a0e 636f 765f  r6...r7...Z.cov_
+000028a0: 6874 6d6c 5f69 6e64 6578 7a4a 636f 6465  html_indexzJcode
+000028b0: 2063 6f76 6572 6167 6520 7465 7374 2072   coverage test r
+000028c0: 6573 756c 7473 206e 6f74 2061 7661 696c  esults not avail
+000028d0: 6162 6c65 2079 6574 2c20 796f 7520 6d61  able yet, you ma
+000028e0: 7920 7275 6e20 2770 6772 2063 6f76 2720  y run 'pgr cov' 
+000028f0: 6669 7273 7421 4672 0500 0000 723c 0000  first!Fr....r<..
+00002900: 004e 290f 7219 0000 0072 3e00 0000 7216  .N).r....r>...r.
+00002910: 0000 0072 3f00 0000 7217 0000 0072 4000  ...r?...r....r@.
+00002920: 0000 5a18 7061 7468 5f63 6f76 6572 6167  ..Z.path_coverag
+00002930: 655f 6874 6d6c 5f69 6e64 6578 7241 0000  e_html_indexrA..
+00002940: 0072 4200 0000 7243 0000 00da 0a56 616c  .rB...rC.....Val
+00002950: 7565 4572 726f 7272 4400 0000 7245 0000  ueErrorrD...rE..
+00002960: 0072 0c00 0000 721a 0000 0072 4700 0000  .r....r....rG...
+00002970: 7220 0000 0072 2000 0000 7226 0000 00da  r ...r ...r&....
+00002980: 0876 6965 775f 636f 7605 0200 0073 1800  .view_cov....s..
+00002990: 0000 0007 0201 0401 0401 0401 04fd 04ff  ................
+000029a0: 0408 0e01 0802 0801 1002 7a10 4163 7469  ..........z.Acti
+000029b0: 6f6e 732e 7669 6577 5f63 6f76 7a08 746f  ons.view_covz.to
+000029c0: 782d 6f6e 6c79 7a22 5275 6e20 6d61 7472  x-onlyz"Run matr
+000029d0: 6978 2074 6573 7420 696e 2074 6f78 2077  ix test in tox w
+000029e0: 6974 6820 7079 7465 7374 6303 0000 0000  ith pytestc.....
+000029f0: 0000 0000 0000 0004 0000 0006 0000 004b  ...............K
+00002a00: 0000 0073 4800 0000 7400 6401 6a01 7402  ...sH...t.d.j.t.
+00002a10: 6a03 7404 6a05 7c01 6a06 6402 8d03 8301  j.t.j.|.j.d.....
+00002a20: 0100 7c02 6403 6b08 723a 7407 a008 7c01  ..|.d.k.r:t...|.
+00002a30: 6a09 6404 a001 7c01 6a0a a101 6702 a101  j.d...|.j...g...
+00002a40: 0100 740b 6405 6406 8d01 0100 6407 5300  ..t.d.d.....d.S.
+00002a50: 2908 7234 0000 007a 397b 6379 616e 7d52  ).r4...z9{cyan}R
+00002a60: 756e 206d 6174 7269 7820 7465 7374 2077  un matrix test w
+00002a70: 6974 6820 746f 7820 7365 7474 696e 6773  ith tox settings
+00002a80: 2069 6e20 7b72 6573 6574 7d74 6f78 2e69   in {reset}tox.i
+00002a90: 6e69 7271 0000 0046 7a0e 2d2d 776f 726b  nirq...Fz.--work
+00002aa0: 6469 7220 227b 7d22 7205 0000 0072 3c00  dir "{}"r....r<.
+00002ab0: 0000 4e29 0c72 1900 0000 723e 0000 0072  ..N).r....r>...r
+00002ac0: 1600 0000 723f 0000 0072 1700 0000 7240  ....r?...r....r@
+00002ad0: 0000 0072 7200 0000 7244 0000 0072 4500  ...rr...rD...rE.
+00002ae0: 0000 5a11 7061 7468 5f76 656e 765f 6269  ..Z.path_venv_bi
+00002af0: 6e5f 746f 7872 5d00 0000 721a 0000 0072  n_toxr]...r....r
+00002b00: 4700 0000 7220 0000 0072 2000 0000 7226  G...r ...r ...r&
+00002b10: 0000 00da 0d74 6573 745f 746f 785f 6f6e  .....test_tox_on
+00002b20: 6c79 1c02 0000 731a 0000 0000 0802 0104  ly....s.........
+00002b30: 0104 0104 0104 fd04 ff04 0708 0104 0104  ................
+00002b40: 010a fe06 047a 1541 6374 696f 6e73 2e74  .....z.Actions.t
+00002b50: 6573 745f 746f 785f 6f6e 6c79 5a03 746f  est_tox_onlyZ.to
+00002b60: 787a 412a 2a20 5275 6e20 6d61 7472 6978  xzA** Run matrix
+00002b70: 2074 6573 7420 696e 2074 6f78 2077 6974   test in tox wit
+00002b80: 6820 7079 7465 7374 2e20 5374 6172 7420  h pytest. Start 
+00002b90: 6f76 6572 2c20 7265 7573 6520 6e6f 7468  over, reuse noth
+00002ba0: 696e 672e 6303 0000 0000 0000 0000 0000  ing.c...........
+00002bb0: 0004 0000 0004 0000 004b 0000 0073 5800  .........K...sX.
+00002bc0: 0000 7c00 6a00 7c01 6601 6401 7c02 6901  ..|.j.|.f.d.|.i.
+00002bd0: 7c03 9702 8e01 0100 7c00 6a01 7c01 6601  |.......|.j.|.f.
+00002be0: 6401 7c02 6901 7c03 9702 8e01 0100 7c02  d.|.i.|.......|.
+00002bf0: 6402 6b08 723e 7402 7c01 6a03 8301 0100  d.k.r>t.|.j.....
+00002c00: 7c00 6a04 7c01 6601 6401 7c02 6901 7c03  |.j.|.f.d.|.i.|.
+00002c10: 9702 8e01 0100 6403 5300 7277 0000 0029  ......d.S.rw...)
+00002c20: 0572 6d00 0000 725e 0000 0072 0d00 0000  .rm...r^...r....
+00002c30: 7254 0000 0072 7d00 0000 7247 0000 0072  rT...r}...rG...r
+00002c40: 2000 0000 7220 0000 0072 2600 0000 da08   ...r ...r&.....
+00002c50: 7465 7374 5f74 6f78 3202 0000 730a 0000  test_tox2...s...
+00002c60: 0000 0816 0116 0108 010a 017a 1041 6374  ...........z.Act
+00002c70: 696f 6e73 2e74 6573 745f 746f 785a 0470  ions.test_toxZ.p
+00002c80: 6570 387a 5041 7070 6c79 2070 6570 3820  ep8zPApply pep8 
+00002c90: 2868 7474 7073 3a2f 2f77 7777 2e70 7974  (https://www.pyt
+00002ca0: 686f 6e2e 6f72 672f 6465 762f 7065 7073  hon.org/dev/peps
+00002cb0: 2f70 6570 2d30 3030 382f 2920 746f 2073  /pep-0008/) to s
+00002cc0: 6f75 7263 6520 636f 6465 2061 6e64 2074  ource code and t
+00002cd0: 6573 7473 2e63 0300 0000 0000 0000 0000  ests.c..........
+00002ce0: 0000 0400 0000 0600 0000 4b00 0000 7350  ..........K...sP
+00002cf0: 0000 007c 006a 007c 017c 0264 018d 0201  ...|.j.|.|.d....
+00002d00: 0074 0164 026a 0274 036a 0474 056a 067c  .t.d.j.t.j.t.j.|
+00002d10: 016a 0764 038d 0383 0101 007c 0264 046b  .j.d.......|.d.k
+00002d20: 0872 4274 08a0 097c 016a 0a7c 016a 0767  .rBt...|.j.|.j.g
+00002d30: 02a1 0101 0074 0b64 0564 068d 0101 0064  .....t.d.d.....d
+00002d40: 0753 0029 0872 3400 0000 a901 724a 0000  .S.).r4.....rJ..
+00002d50: 007a 427b 6379 616e 7d72 6566 6f72 6d61  .zB{cyan}reforma
+00002d60: 7420 7079 7468 6f6e 2063 6f64 6520 7374  t python code st
+00002d70: 796c 652c 2065 7865 6375 7465 207b 7265  yle, execute {re
+00002d80: 7365 747d 7b72 6566 6f72 6d61 745f 7363  set}{reformat_sc
+00002d90: 7269 7074 7d29 0372 3600 0000 7237 0000  ript}).r6...r7..
+00002da0: 005a 0f72 6566 6f72 6d61 745f 7363 7269  .Z.reformat_scri
+00002db0: 7074 4672 0500 0000 723c 0000 004e 290c  ptFr....r<...N).
+00002dc0: 7269 0000 0072 1900 0000 723e 0000 0072  ri...r....r>...r
+00002dd0: 1600 0000 723f 0000 0072 1700 0000 7240  ....r?...r....r@
+00002de0: 0000 005a 1a70 6174 685f 6669 785f 636f  ...Z.path_fix_co
+00002df0: 6465 5f73 7479 6c65 5f73 6372 6970 7472  de_style_scriptr
+00002e00: 4400 0000 7245 0000 0072 6300 0000 721a  D...rE...rc...r.
+00002e10: 0000 0072 4700 0000 7220 0000 0072 2000  ...rG...r ...r .
+00002e20: 0000 7226 0000 00da 1872 6566 6f72 6d61  ..r&.....reforma
+00002e30: 745f 7065 7038 5f63 6f64 655f 7374 796c  t_pep8_code_styl
+00002e40: 6540 0200 0073 1c00 0000 0008 0e01 0201  e@...s..........
+00002e50: 0401 0401 0401 04fd 04ff 0407 0801 0401  ................
+00002e60: 0401 04fe 0604 7a20 4163 7469 6f6e 732e  ......z Actions.
+00002e70: 7265 666f 726d 6174 5f70 6570 385f 636f  reformat_pep8_co
+00002e80: 6465 5f73 7479 6c65 7a26 4275 696c 6420  de_stylez&Build 
+00002e90: 6c6f 6361 6c20 646f 6375 6d65 6e74 7320  local documents 
+00002ea0: 7769 7468 2073 7068 696e 782d 646f 632e  with sphinx-doc.
+00002eb0: 6303 0000 0000 0000 0000 0000 0004 0000  c...............
+00002ec0: 0006 0000 004b 0000 0073 9400 0000 7400  .....K...s....t.
+00002ed0: 6401 6a01 7402 6a03 7404 6a05 7c01 6a06  d.j.t.j.t.j.|.j.
+00002ee0: 6402 8d03 8301 0100 7c02 6403 6b08 7286  d.......|.d.k.r.
+00002ef0: 7c01 6a07 7408 6a09 1700 7408 6a0a a00b  |.j.t.j...t.j...
+00002f00: 6404 6405 a102 1700 7408 6a0a 6404 3c00  d.d.....t.j.d.<.
+00002f10: 7c01 6a0c 7408 6a0a 6406 3c00 740d 6407  |.j.t.j.d.<.t.d.
+00002f20: 8301 0100 740d 7408 6a0a 6404 1900 8301  ....t.t.j.d.....
+00002f30: 0100 740d 7408 6a0a 6406 1900 8301 0100  ..t.t.j.d.......
+00002f40: 740e a00f 6408 6409 7c01 6a10 640a 6704  t...d.d.|.j.d.g.
+00002f50: a101 0100 7411 640b 640c 8d01 0100 640d  ....t.d.d.....d.
+00002f60: 5300 290e 7234 0000 007a 2a7b 6379 616e  S.).r4...z*{cyan
+00002f70: 7d42 7569 6c64 2064 6f63 2061 7420 7b72  }Build doc at {r
+00002f80: 6573 6574 7d7b 646f 635f 6275 696c 645f  eset}{doc_build_
+00002f90: 6874 6d6c 7da9 0372 3600 0000 7237 0000  html}..r6...r7..
+00002fa0: 005a 0e64 6f63 5f62 7569 6c64 5f68 746d  .Z.doc_build_htm
+00002fb0: 6c46 da04 5041 5448 da00 5a0b 5649 5254  lF..PATH..Z.VIRT
+00002fc0: 5541 4c5f 454e 567a 503d 3d3d 3d3d 3d3d  UAL_ENVzP=======
+00002fd0: 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d  ================
+00002fe0: 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d  ================
+00002ff0: 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d  ================
+00003000: 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d 3d3d  ================
+00003010: 3d3d 3d3d 3d3d 3d3d 3dda 046d 616b 657a  =========..makez
+00003020: 022d 435a 0468 746d 6c72 0500 0000 723c  .-CZ.htmlr....r<
+00003030: 0000 004e 2912 7219 0000 0072 3e00 0000  ...N).r....r>...
+00003040: 7216 0000 0072 3f00 0000 7217 0000 0072  r....r?...r....r
+00003050: 4000 0000 da19 6469 725f 7370 6869 6e78  @.....dir_sphinx
+00003060: 5f64 6f63 5f62 7569 6c64 5f68 746d 6c5a  _doc_build_htmlZ
+00003070: 0c64 6972 5f76 656e 765f 6269 6e72 4100  .dir_venv_binrA.
+00003080: 0000 da07 7061 7468 7365 70da 0765 6e76  ....pathsep..env
+00003090: 6972 6f6e da03 6765 7472 3800 0000 726f  iron..getr8...ro
+000030a0: 0000 0072 4400 0000 7245 0000 005a 0e64  ...rD...rE...Z.d
+000030b0: 6972 5f73 7068 696e 785f 646f 6372 1a00  ir_sphinx_docr..
+000030c0: 0000 7247 0000 0072 2000 0000 7220 0000  ..rG...r ...r ..
+000030d0: 0072 2600 0000 da0e 6275 696c 645f 646f  .r&.....build_do
+000030e0: 635f 6f6e 6c79 5702 0000 7328 0000 0000  c_onlyW...s(....
+000030f0: 0702 0104 0104 0104 0104 fd04 ff04 0708  ................
+00003100: 0220 010c 0108 010e 010e 0204 0102 0102  . ..............
+00003110: 0004 0102 fd06 057a 1641 6374 696f 6e73  .......z.Actions
+00003120: 2e62 7569 6c64 5f64 6f63 5f6f 6e6c 797a  .build_doc_onlyz
+00003130: 442a 2a20 4275 696c 6420 6c6f 6361 6c20  D** Build local 
+00003140: 646f 6375 6d65 6e74 7320 7769 7468 2073  documents with s
+00003150: 7068 696e 782d 646f 632c 2073 7461 7274  phinx-doc, start
+00003160: 206f 7665 722c 2072 6575 7365 206e 6f74   over, reuse not
+00003170: 6869 6e67 2e63 0300 0000 0000 0000 0000  hing.c..........
+00003180: 0000 0400 0000 0600 0000 4b00 0000 7372  ..........K...sr
+00003190: 0000 007c 006a 007c 0166 0164 017c 0269  ...|.j.|.f.d.|.i
+000031a0: 017c 0397 028e 0101 007c 006a 017c 0166  .|.......|.j.|.f
+000031b0: 0164 017c 0269 017c 0397 028e 0101 007c  .d.|.i.|.......|
+000031c0: 0264 026b 0872 5874 027c 016a 0383 0101  .d.k.rXt.|.j....
+000031d0: 0074 0274 046a 05a0 067c 016a 077c 016a  .t.t.j...|.j.|.j
+000031e0: 08a0 09a1 00a1 0283 0101 007c 006a 0a7c  ...........|.j.|
+000031f0: 0166 0164 017c 0269 017c 0397 028e 0101  .f.d.|.i.|......
+00003200: 0064 0353 0072 7700 0000 290b 726b 0000  .d.S.rw...).rk..
+00003210: 0072 5e00 0000 720d 0000 0072 5000 0000  .r^...r....rP...
+00003220: 7241 0000 0072 4200 0000 da04 6a6f 696e  rA...rB.....join
+00003230: 5a15 6469 725f 7370 6869 6e78 5f64 6f63  Z.dir_sphinx_doc
+00003240: 5f73 6f75 7263 6572 5900 0000 725a 0000  _sourcerY...rZ..
+00003250: 0072 8900 0000 7247 0000 0072 2000 0000  .r....rG...r ...
+00003260: 7220 0000 0072 2600 0000 da09 6275 696c  r ...r&.....buil
+00003270: 645f 646f 6374 0200 0073 1200 0000 0007  d_doct...s......
+00003280: 1601 1601 0801 0a01 0801 0400 08ff 0602  ................
+00003290: 7a11 4163 7469 6f6e 732e 6275 696c 645f  z.Actions.build_
+000032a0: 646f 637a 2543 6c65 6172 2072 6563 656e  docz%Clear recen
+000032b0: 746c 7920 6275 696c 7420 6c6f 6361 6c20  tly built local 
+000032c0: 646f 6375 6d65 6e74 732e 6303 0000 0000  documents.c.....
+000032d0: 0000 0000 0000 0004 0000 0006 0000 004b  ...............K
+000032e0: 0000 0073 3a00 0000 7400 6401 6a01 7402  ...s:...t.d.j.t.
+000032f0: 6a03 7404 6a05 7c01 6a06 6402 8d03 8301  j.t.j.|.j.d.....
+00003300: 0100 7c02 6403 6b08 722c 7407 7c01 6a06  ..|.d.k.r,t.|.j.
+00003310: 8301 0100 7408 6404 6405 8d01 0100 6406  ....t.d.d.....d.
+00003320: 5300 2907 7234 0000 007a 347b 6379 616e  S.).r4...z4{cyan
+00003330: 7d43 6c65 616e 2072 6563 656e 746c 7920  }Clean recently 
+00003340: 6275 696c 7420 646f 6320 6174 207b 7265  built doc at {re
+00003350: 7365 747d 7b64 6f63 5f62 7569 6c64 7d29  set}{doc_build})
+00003360: 0372 3600 0000 7237 0000 005a 0964 6f63  .r6...r7...Z.doc
+00003370: 5f62 7569 6c64 4672 0500 0000 723c 0000  _buildFr....r<..
+00003380: 004e 2909 7219 0000 0072 3e00 0000 7216  .N).r....r>...r.
+00003390: 0000 0072 3f00 0000 7217 0000 0072 4000  ...r?...r....r@.
+000033a0: 0000 7250 0000 0072 0d00 0000 721a 0000  ..rP...r....r...
+000033b0: 0072 4700 0000 7220 0000 0072 2000 0000  .rG...r ...r ...
+000033c0: 7226 0000 00da 0963 6c65 616e 5f64 6f63  r&.....clean_doc
+000033d0: 8302 0000 7314 0000 0000 0702 0104 0104  ....s...........
+000033e0: 0104 0104 fd04 ff04 0708 010a 017a 1141  .............z.A
+000033f0: 6374 696f 6e73 2e63 6c65 616e 5f64 6f63  ctions.clean_doc
+00003400: 7a27 2a2a 2056 6965 7720 7265 6365 6e74  z'** View recent
+00003410: 6c79 2062 7569 6c64 206c 6f63 616c 2064  ly build local d
+00003420: 6f63 756d 656e 7473 2e63 0300 0000 0000  ocuments.c......
+00003430: 0000 0000 0000 0500 0000 0600 0000 4b00  ..............K.
+00003440: 0000 739a 0000 0074 0064 016a 0174 026a  ..s....t.d.j.t.j
+00003450: 0374 046a 057c 016a 0664 028d 0383 0101  .t.j.|.j.d......
+00003460: 0074 076a 08a0 0974 076a 08a0 0a7c 016a  .t.j...t.j...|.j
+00003470: 0664 03a1 02a1 0172 4474 076a 08a0 0a7c  .d.....rDt.j...|
+00003480: 016a 0664 03a1 027d 046e 3274 076a 08a0  .j.d...}.n2t.j..
+00003490: 0974 076a 08a0 0a7c 016a 0664 04a1 02a1  .t.j...|.j.d....
+000034a0: 0172 6e74 076a 08a0 0a7c 016a 0664 04a1  .rnt.j...|.j.d..
+000034b0: 027d 046e 0874 0b64 0583 0182 017c 0264  .}.n.t.d.....|.d
+000034c0: 066b 0872 8c74 0ca0 0d74 0e7c 0467 02a1  .k.r.t...t.|.g..
+000034d0: 0101 0074 0f64 0764 088d 0101 0064 0953  ...t.d.d.....d.S
+000034e0: 0029 0a72 3400 0000 7a40 7b63 7961 6e7d  .).r4...z@{cyan}
+000034f0: 4f70 656e 2072 6563 656e 746c 7920 6275  Open recently bu
+00003500: 696c 7420 6c6f 6361 6c20 6874 6d6c 2064  ilt local html d
+00003510: 6f63 207b 7265 7365 747d 7b64 6f63 5f62  oc {reset}{doc_b
+00003520: 7569 6c64 5f68 746d 6c7d 7281 0000 007a  uild_html}r....z
+00003530: 0a69 6e64 6578 2e68 746d 6c7a 0b52 4541  .index.htmlz.REA
+00003540: 444d 452e 6874 6d6c 7a29 646f 6375 6d65  DME.htmlz)docume
+00003550: 6e74 6174 696f 6e20 696e 6465 7820 6874  ntation index ht
+00003560: 6d6c 2066 696c 6520 6e6f 7420 6578 6973  ml file not exis
+00003570: 7473 2146 7205 0000 0072 3c00 0000 4e29  ts!Fr....r<...N)
+00003580: 1072 1900 0000 723e 0000 0072 1600 0000  .r....r>...r....
+00003590: 723f 0000 0072 1700 0000 7240 0000 0072  r?...r....r@...r
+000035a0: 8500 0000 7241 0000 0072 4200 0000 7243  ....rA...rB...rC
+000035b0: 0000 0072 8a00 0000 727b 0000 0072 4400  ...r....r{...rD.
+000035c0: 0000 7245 0000 0072 0c00 0000 721a 0000  ..rE...r....r...
+000035d0: 0029 0572 4800 0000 7249 0000 0072 4a00  .).rH...rI...rJ.
+000035e0: 0000 7222 0000 005a 1370 6174 685f 646f  ..r"...Z.path_do
+000035f0: 635f 696e 6465 785f 6874 6d6c 7220 0000  c_index_htmlr ..
+00003600: 0072 2000 0000 7226 0000 00da 0876 6965  .r ...r&.....vie
+00003610: 775f 646f 6395 0200 0073 2600 0000 0007  w_doc....s&.....
+00003620: 0201 0401 0401 0401 04fd 04ff 0408 0601  ................
+00003630: 0eff 0403 1201 0601 0eff 0403 1202 0802  ................
+00003640: 0801 0e02 7a10 4163 7469 6f6e 732e 7669  ....z.Actions.vi
+00003650: 6577 5f64 6f63 6306 0000 0000 0000 0000  ew_docc.........
+00003660: 0000 0009 0000 0008 0000 004b 0000 0073  ...........K...s
+00003670: f800 0000 7400 7c03 8301 0100 7401 6401  ....t.|.....t.d.
+00003680: 6a02 7403 6a04 7c02 6402 8d02 8301 0100  j.t.j.|.d.......
+00003690: 7401 6403 6a02 7403 6a04 7405 6a06 7407  t.d.j.t.j.t.j.t.
+000036a0: 7c03 6404 8d04 8301 0100 6405 6406 6407  |.d.......d.d.d.
+000036b0: 7c03 6408 6409 6706 7d07 7c04 640a 6b09  |.d.d.g.}.|.d.k.
+000036c0: 725c 7c07 a008 640b 7c04 6702 a101 0100  r\|...d.|.g.....
+000036d0: 7c05 640c 6b08 726e 7409 a00a 7c07 a101  |.d.k.rnt...|...
+000036e0: 0100 7401 640d 6a02 7403 6a04 7405 6a06  ..t.d.j.t.j.t.j.
+000036f0: 7407 7c01 6a0b 7c03 640e 8d05 8301 0100  t.|.j.|.d.......
+00003700: 6405 6406 640f 7c01 6a0b 7c03 6409 6706  d.d.d.|.j.|.d.g.
+00003710: 7d07 7c04 640a 6b09 72b4 7c07 a008 640b  }.|.d.k.r.|...d.
+00003720: 7c04 6702 a101 0100 7c05 640c 6b08 72c6  |.g.....|.d.k.r.
+00003730: 7409 a00a 7c07 a101 0100 740c 7c03 8301  t...|.....t.|...
+00003740: 7d08 7401 6410 6a02 7403 6a04 7405 6a06  }.t.d.j.t.j.t.j.
+00003750: 7407 7c02 7c08 6411 8d05 8301 0100 740d  t.|.|.d.......t.
+00003760: 6412 6413 8d01 0100 640a 5300 2914 7aef  d.d.....d.S.).z.
+00003770: 0a20 2020 2020 2020 2044 6570 6c6f 7920  .        Deploy 
+00003780: 6c6f 6361 6c20 6874 6d6c 2064 6f63 2074  local html doc t
+00003790: 6f20 5333 2e0a 0a20 2020 2020 2020 203a  o S3...        :
+000037a0: 7479 7065 2063 6f6e 6669 673a 2052 6570  type config: Rep
+000037b0: 6f43 6f6e 6669 670a 0a20 2020 2020 2020  oConfig..       
+000037c0: 203a 7479 7065 2064 6f63 5f76 6572 7369   :type doc_versi
+000037d0: 6f6e 3a20 7374 720a 2020 2020 2020 2020  on: str.        
+000037e0: 3a70 6172 616d 2064 6f63 5f76 6572 7369  :param doc_versi
+000037f0: 6f6e 3a20 226c 6174 6573 7422 206f 7220  on: "latest" or 
+00003800: 2276 6572 7369 6f6e 6564 220a 0a20 2020  "versioned"..   
+00003810: 2020 2020 203a 7479 7065 2073 335f 7572       :type s3_ur
+00003820: 695f 646f 635f 6469 723a 2073 7472 0a20  i_doc_dir: str. 
+00003830: 2020 2020 2020 203a 7479 7065 2064 6f63         :type doc
+00003840: 5f68 6f73 745f 6177 735f 7072 6f66 696c  _host_aws_profil
+00003850: 653a 2073 7472 0a20 2020 2020 2020 207a  e: str.        z
+00003860: 3a7b 6379 616e 7d64 6570 6c6f 7920 646f  :{cyan}deploy do
+00003870: 6320 6672 6f6d 206c 6f63 616c 2074 6f20  c from local to 
+00003880: 7333 2061 7320 7b64 6f63 5f76 6572 7369  s3 as {doc_versi
+00003890: 6f6e 7d20 646f 6320 2e2e 2e29 0272 3600  on} doc ...).r6.
+000038a0: 0000 da0b 646f 635f 7665 7273 696f 6e7a  ....doc_versionz
+000038b0: 2c7b 6379 616e 7d7b 7461 627d 6177 7320  ,{cyan}{tab}aws 
+000038c0: 7333 2072 6d20 7b72 6573 6574 7d7b 7333  s3 rm {reset}{s3
+000038d0: 5f75 7269 5f64 6f63 5f64 6972 7d29 0472  _uri_doc_dir}).r
+000038e0: 3600 0000 7237 0000 0072 3a00 0000 da0e  6...r7...r:.....
+000038f0: 7333 5f75 7269 5f64 6f63 5f64 6972 da03  s3_uri_doc_dir..
+00003900: 6177 73da 0273 335a 0272 6d7a 0b2d 2d72  aws..s3Z.rmz.--r
+00003910: 6563 7572 7369 7665 7a12 2d2d 6f6e 6c79  ecursivez.--only
+00003920: 2d73 686f 772d 6572 726f 7273 4efa 092d  -show-errorsN..-
+00003930: 2d70 726f 6669 6c65 467a 4a7b 6379 616e  -profileFzJ{cyan
+00003940: 7d7b 7461 627d 6177 7320 7333 2073 796e  }{tab}aws s3 syn
+00003950: 6320 7b72 6573 6574 7d7b 6469 725f 7370  c {reset}{dir_sp
+00003960: 6869 6e78 5f64 6f63 5f62 7569 6c64 5f68  hinx_doc_build_h
+00003970: 746d 6c7d 207b 7333 5f75 7269 5f64 6f63  tml} {s3_uri_doc
+00003980: 5f64 6972 7d29 0572 3600 0000 7237 0000  _dir}).r6...r7..
+00003990: 0072 3a00 0000 7285 0000 0072 8f00 0000  .r:...r....r....
+000039a0: da04 7379 6e63 7a3c 7b63 7961 6e7d 7b74  ..syncz<{cyan}{t
+000039b0: 6162 7d76 6965 7720 7b64 6f63 5f76 6572  ab}view {doc_ver
+000039c0: 7369 6f6e 7d20 646f 6320 6174 207b 7265  sion} doc at {re
+000039d0: 7365 747d 7b73 335f 636f 6e73 6f6c 655f  set}{s3_console_
+000039e0: 7572 6c7d 2905 7236 0000 0072 3700 0000  url}).r6...r7...
+000039f0: 723a 0000 0072 8e00 0000 da0e 7333 5f63  r:...r......s3_c
+00003a00: 6f6e 736f 6c65 5f75 726c 7205 0000 0072  onsole_urlr....r
+00003a10: 3c00 0000 290e 7214 0000 0072 1900 0000  <...).r....r....
+00003a20: 723e 0000 0072 1600 0000 723f 0000 0072  r>...r....r?...r
+00003a30: 1700 0000 7240 0000 0072 1800 0000 da06  ....r@...r......
+00003a40: 6578 7465 6e64 7244 0000 0072 4500 0000  extendrD...rE...
+00003a50: 7285 0000 0072 1200 0000 721a 0000 0029  r....r....r....)
+00003a60: 0972 4800 0000 7249 0000 0072 8e00 0000  .rH...rI...r....
+00003a70: 728f 0000 00da 1464 6f63 5f68 6f73 745f  r......doc_host_
+00003a80: 6177 735f 7072 6f66 696c 6572 4a00 0000  aws_profilerJ...
+00003a90: 7222 0000 0072 2100 0000 7294 0000 0072  r"...r!...r....r
+00003aa0: 2000 0000 7220 0000 0072 2600 0000 da11   ...r ...r&.....
+00003ab0: 5f64 6570 6c6f 795f 646f 635f 746f 5f73  _deploy_doc_to_s
+00003ac0: 33b4 0200 0073 7200 0000 0014 0802 0201  3....sr.........
+00003ad0: 0401 0401 02fe 04ff 0407 0201 0401 0401  ................
+00003ae0: 0401 0201 02fc 04ff 0409 0200 0200 0200  ................
+00003af0: 0201 0201 02fd 0405 0801 0e02 0801 0a02  ................
+00003b00: 0201 0401 0401 0401 0201 0401 02fb 04ff  ................
+00003b10: 040a 0200 0200 0201 0400 0201 02fd 0405  ................
+00003b20: 0801 0e02 0801 0a02 0801 0201 0401 0401  ................
+00003b30: 0401 0201 0201 02fb 04ff 040a 7a19 4163  ............z.Ac
+00003b40: 7469 6f6e 732e 5f64 6570 6c6f 795f 646f  tions._deploy_do
+00003b50: 635f 746f 5f73 337a 3144 6570 6c6f 7920  c_to_s3z1Deploy 
+00003b60: 6c6f 6361 6c20 6874 6d6c 2064 6f63 2074  local html doc t
+00003b70: 6f20 5333 2061 7320 7665 7273 696f 6e65  o S3 as versione
+00003b80: 6420 646f 6375 6d65 6e74 6303 0000 0000  d documentc.....
+00003b90: 0000 0000 0000 0004 0000 0007 0000 004b  ...............K
+00003ba0: 0000 0073 2800 0000 7c00 6a00 7c01 6601  ...s(...|.j.|.f.
+00003bb0: 6401 7c01 6a01 7c01 6a02 a003 a100 7c02  d.|.j.|.j.....|.
+00003bc0: 6402 9c04 7c03 9702 8e01 0100 6403 5300  d...|.......d.S.
+00003bd0: 2904 7234 0000 005a 0976 6572 7369 6f6e  ).r4...Z.version
+00003be0: 6564 a904 728e 0000 0072 8f00 0000 7296  ed..r....r....r.
+00003bf0: 0000 0072 4a00 0000 4e29 0472 9700 0000  ...rJ...N).r....
+00003c00: 5a18 7333 5f75 7269 5f64 6f63 5f64 6972  Z.s3_uri_doc_dir
+00003c10: 5f76 6572 7369 6f6e 6564 da14 444f 435f  _versioned..DOC_
+00003c20: 484f 5354 5f41 5753 5f50 524f 4649 4c45  HOST_AWS_PROFILE
+00003c30: 725a 0000 0072 4700 0000 7220 0000 0072  rZ...rG...r ...r
+00003c40: 2000 0000 7226 0000 00da 1764 6570 6c6f   ...r&.....deplo
+00003c50: 795f 646f 635f 746f 5f76 6572 7369 6f6e  y_doc_to_version
+00003c60: 6564 0503 0000 7314 0000 0000 0704 0102  ed....s.........
+00003c70: ff02 0202 0104 0108 0102 fb04 0602 fa7a  ...............z
+00003c80: 1f41 6374 696f 6e73 2e64 6570 6c6f 795f  .Actions.deploy_
+00003c90: 646f 635f 746f 5f76 6572 7369 6f6e 6564  doc_to_versioned
+00003ca0: 7a2e 4465 706c 6f79 206c 6f63 616c 2068  z.Deploy local h
+00003cb0: 746d 6c20 646f 6320 746f 2053 3320 6173  tml doc to S3 as
+00003cc0: 206c 6174 6573 7420 646f 6375 6d65 6e74   latest document
+00003cd0: 6303 0000 0000 0000 0000 0000 0004 0000  c...............
+00003ce0: 0007 0000 004b 0000 0073 2800 0000 7c00  .....K...s(...|.
+00003cf0: 6a00 7c01 6601 6401 7c01 6a01 7c01 6a02  j.|.f.d.|.j.|.j.
+00003d00: a003 a100 7c02 6402 9c04 7c03 9702 8e01  ....|.d...|.....
+00003d10: 0100 6403 5300 2904 7234 0000 005a 066c  ..d.S.).r4...Z.l
+00003d20: 6174 6573 7472 9800 0000 4e29 0472 9700  atestr....N).r..
+00003d30: 0000 5a15 7333 5f75 7269 5f64 6f63 5f64  ..Z.s3_uri_doc_d
+00003d40: 6972 5f6c 6174 6573 7472 9900 0000 725a  ir_latestr....rZ
+00003d50: 0000 0072 4700 0000 7220 0000 0072 2000  ...rG...r ...r .
+00003d60: 0000 7226 0000 00da 1464 6570 6c6f 795f  ..r&.....deploy_
+00003d70: 646f 635f 746f 5f6c 6174 6573 7415 0300  doc_to_latest...
+00003d80: 0073 1400 0000 0007 0401 02ff 0202 0201  .s..............
+00003d90: 0401 0801 02fb 0406 02fa 7a1c 4163 7469  ..........z.Acti
+00003da0: 6f6e 732e 6465 706c 6f79 5f64 6f63 5f74  ons.deploy_doc_t
+00003db0: 6f5f 6c61 7465 7374 7a5a 4465 706c 6f79  o_latestzZDeploy
+00003dc0: 206c 6f63 616c 2068 746d 6c20 646f 6320   local html doc 
+00003dd0: 746f 2053 3320 6173 2076 6572 7369 6f6e  to S3 as version
+00003de0: 6564 2064 6f63 756d 656e 742c 2061 6e64  ed document, and
+00003df0: 2061 6c73 6f20 6173 206c 6174 6573 7420   also as latest 
+00003e00: 646f 6375 6d65 6e74 206f 7074 696f 6e61  document optiona
+00003e10: 6c6c 792e 6303 0000 0000 0000 0000 0000  lly.c...........
+00003e20: 0005 0000 0005 0000 004b 0000 0073 7e00  .........K...s~.
+00003e30: 0000 7400 6401 6a01 7402 6a03 6402 8d01  ..t.d.j.t.j.d...
+00003e40: 8301 0100 7c00 6a04 7c01 6601 6403 7c02  ....|.j.|.f.d.|.
+00003e50: 6901 7c03 9702 8e01 0100 7400 6404 6a01  i.|.......t.d.j.
+00003e60: 7402 6a03 7405 6405 8d02 8301 0100 7406  t.j.t.d.......t.
+00003e70: 7407 6406 8301 8301 a008 a100 a009 a100  t.d.............
+00003e80: 7d04 7c04 6407 6b06 7270 7c00 6a0a 7c01  }.|.d.k.rp|.j.|.
+00003e90: 6601 6403 7c02 6901 7c03 9702 8e01 0100  f.d.|.i.|.......
+00003ea0: 6e0a 740b 6408 6409 8d01 0100 640a 5300  n.t.d.d.....d.S.
+00003eb0: 290b 7234 0000 007a 257b 6379 616e 7d64  ).r4...z%{cyan}d
+00003ec0: 6570 6c6f 7920 646f 6320 6672 6f6d 206c  eploy doc from l
+00003ed0: 6f63 616c 2074 6f20 7333 202e 2e2e 724d  ocal to s3 ...rM
+00003ee0: 0000 0072 4a00 0000 7a23 7b63 7961 6e7d  ...rJ...z#{cyan}
+00003ef0: 616c 736f 2064 6570 6c6f 7920 6c61 7465  also deploy late
+00003f00: 7374 2064 6f63 2028 792f 6e29 3f72 3900  st doc (y/n)?r9.
+00003f10: 0000 7283 0000 0029 02da 0179 da03 7965  ..r....)...y..ye
+00003f20: 7372 0500 0000 723c 0000 004e 290c 7219  sr....r<...N).r.
+00003f30: 0000 0072 3e00 0000 7216 0000 0072 3f00  ...r>...r....r?.
+00003f40: 0000 729a 0000 0072 1800 0000 da03 7374  ..r....r......st
+00003f50: 7272 0600 0000 da05 6c6f 7765 72da 0573  rr......lower..s
+00003f60: 7472 6970 729b 0000 0072 1a00 0000 2905  tripr....r....).
+00003f70: 7248 0000 0072 4900 0000 724a 0000 0072  rH...rI...rJ...r
+00003f80: 2200 0000 5a07 656e 7465 7265 6472 2000  "...Z.enteredr .
+00003f90: 0000 7220 0000 0072 2600 0000 da0a 6465  ..r ...r&.....de
+00003fa0: 706c 6f79 5f64 6f63 2503 0000 7318 0000  ploy_doc%...s...
+00003fb0: 0000 0712 0116 0202 0104 0104 0102 fe04  ................
+00003fc0: ff04 0614 0108 0118 027a 1241 6374 696f  .........z.Actio
+00003fd0: 6e73 2e64 6570 6c6f 795f 646f 635a 0770  ns.deploy_docZ.p
+00003fe0: 7562 6c69 7368 7a2d 2a2a 2050 7562 6c69  ublishz-** Publi
+00003ff0: 7368 2074 6869 7320 5061 636b 6167 6520  sh this Package 
+00004000: 746f 2068 7474 7073 3a2f 2f70 7970 692e  to https://pypi.
+00004010: 6f72 672f 2e63 0300 0000 0000 0000 0000  org/.c..........
+00004020: 0000 0500 0000 0700 0000 4b00 0000 73de  ..........K...s.
+00004030: 0000 007c 006a 007c 0166 0164 017c 0269  ...|.j.|.f.d.|.i
+00004040: 017c 0397 028e 0101 007c 006a 017c 0166  .|.......|.j.|.f
+00004050: 0164 017c 0269 017c 0397 028e 0101 0074  .d.|.i.|.......t
+00004060: 0264 026a 0374 046a 0574 066a 077c 016a  .d.j.t.j.t.j.|.j
+00004070: 08a0 09a1 0064 038d 0383 0101 007c 0264  .....d.......|.d
+00004080: 046b 0872 7074 0a7c 016a 0b83 0101 0074  .k.rpt.|.j.....t
+00004090: 0a7c 016a 0c83 0101 0074 0a7c 016a 0d83  .|.j.....t.|.j..
+000040a0: 0101 0074 0ea0 0fa1 007d 0474 0ea0 107c  ...t.....}.t...|
+000040b0: 016a 11a1 0101 007a 347c 0264 046b 0872  .j.....z4|.d.k.r
+000040c0: b674 12a0 137c 016a 1464 0564 0664 0764  .t...|.j.d.d.d.d
+000040d0: 0867 05a1 0101 0074 12a0 137c 016a 1564  .g.....t...|.j.d
+000040e0: 0964 0a67 03a1 0101 0057 006e 0c01 0001  .d.g.....W.n....
+000040f0: 0001 0059 006e 0258 0074 0ea0 107c 04a1  ...Y.n.X.t...|..
+00004100: 0101 0074 1664 0b64 0c8d 0101 0064 0d53  ...t.d.d.....d.S
+00004110: 0029 0e72 3400 0000 724a 0000 007a 4f7b  .).r4...rJ...zO{
+00004120: 6379 616e 7d50 7562 6c69 7368 207b 7061  cyan}Publish {pa
+00004130: 636b 6167 655f 6e61 6d65 7d20 746f 207b  ckage_name} to {
+00004140: 7265 7365 747d 6874 7470 733a 2f2f 7079  reset}https://py
+00004150: 7069 2e6f 7267 2f70 726f 6a65 6374 2f7b  pi.org/project/{
+00004160: 7061 636b 6167 655f 6e61 6d65 7d2f 2903  package_name}/).
+00004170: 7236 0000 0072 3700 0000 7258 0000 0046  r6...r7...rX...F
+00004180: 7a08 7365 7475 702e 7079 5a05 7364 6973  z.setup.pyZ.sdis
+00004190: 745a 0b62 6469 7374 5f77 6865 656c 7a0b  tZ.bdist_wheelz.
+000041a0: 2d2d 756e 6976 6572 7361 6c5a 0675 706c  --universalZ.upl
+000041b0: 6f61 647a 0664 6973 742f 2a72 0500 0000  oadz.dist/*r....
+000041c0: 723c 0000 004e 2917 7269 0000 0072 5e00  r<...N).ri...r^.
+000041d0: 0000 7219 0000 0072 3e00 0000 7216 0000  ..r....r>...r...
+000041e0: 0072 3f00 0000 7217 0000 0072 4000 0000  .r?...r....r@...
+000041f0: 7259 0000 0072 5a00 0000 720d 0000 0072  rY...rZ...r....r
+00004200: 4f00 0000 5a13 6469 725f 7079 7069 5f64  O...Z.dir_pypi_d
+00004210: 6973 7472 6962 7574 655a 0c64 6972 5f70  istributeZ.dir_p
+00004220: 7970 695f 6567 6772 4100 0000 da06 6765  ypi_eggrA.....ge
+00004230: 7463 7764 da05 6368 6469 7272 5d00 0000  tcwd..chdirr]...
+00004240: 7244 0000 0072 4500 0000 7263 0000 005a  rD...rE...rc...Z
+00004250: 1370 6174 685f 7665 6e76 5f62 696e 5f74  .path_venv_bin_t
+00004260: 7769 6e65 721a 0000 0029 0572 4800 0000  winer....).rH...
+00004270: 7249 0000 0072 4a00 0000 7222 0000 00da  rI...rJ...r"....
+00004280: 0363 7764 7220 0000 0072 2000 0000 7226  .cwdr ...r ...r&
+00004290: 0000 00da 0f70 7562 6c69 7368 5f74 6f5f  .....publish_to_
+000042a0: 7079 7069 3b03 0000 7342 0000 0000 0816  pypi;...sB......
+000042b0: 0116 0102 0104 0104 0104 0108 fd04 ff04  ................
+000042c0: 0708 010a 010a 010a 0208 010c 0102 0108  ................
+000042d0: 0104 0104 0102 0102 0102 0102 fb06 0704  ................
+000042e0: 0104 0102 0102 fd0a 0506 0106 010a 017a  ...............z
+000042f0: 1741 6374 696f 6e73 2e70 7562 6c69 7368  .Actions.publish
+00004300: 5f74 6f5f 7079 7069 7a1d 5275 6e20 4a75  _to_pypiz.Run Ju
+00004310: 7079 7465 7220 6e6f 7465 626f 6f6b 206c  pyter notebook l
+00004320: 6f63 616c 6c79 2e63 0300 0000 0000 0000  ocally.c........
+00004330: 0000 0000 0400 0000 0400 0000 4b00 0000  ............K...
+00004340: 732e 0000 0074 0064 016a 0174 026a 0364  s....t.d.j.t.j.d
+00004350: 028d 0183 0101 007c 0264 036b 0872 2a74  .......|.d.k.r*t
+00004360: 04a0 057c 016a 0664 0467 02a1 0101 0064  ...|.j.d.g.....d
+00004370: 0553 0029 0672 3400 0000 7a1e 7b63 7961  .S.).r4...z.{cya
+00004380: 6e7d 7275 6e20 6a75 7079 7465 7220 6e6f  n}run jupyter no
+00004390: 7465 626f 6f6b 202e 2e2e 724d 0000 0046  tebook ...rM...F
+000043a0: 5a08 6e6f 7465 626f 6f6b 4e29 0772 1900  Z.notebookN).r..
+000043b0: 0000 723e 0000 0072 1600 0000 723f 0000  ..r>...r....r?..
+000043c0: 0072 4400 0000 7245 0000 005a 1570 6174  .rD...rE...Z.pat
+000043d0: 685f 7665 6e76 5f62 696e 5f6a 7570 7974  h_venv_bin_jupyt
+000043e0: 6572 7247 0000 0072 2000 0000 7220 0000  errG...r ...r ..
+000043f0: 0072 2600 0000 da14 7275 6e5f 6a75 7079  .r&.....run_jupy
+00004400: 7465 725f 6e6f 7465 626f 6f6b 6603 0000  ter_notebookf...
+00004410: 730c 0000 0000 0712 0108 0104 0104 0102  s...............
+00004420: fe7a 1c41 6374 696f 6e73 2e72 756e 5f6a  .z.Actions.run_j
+00004430: 7570 7974 6572 5f6e 6f74 6562 6f6f 6b7a  upyter_notebookz
+00004440: 2642 7569 6c64 2041 5753 204c 616d 6264  &Build AWS Lambd
+00004450: 6120 736f 7572 6365 2063 6f64 6520 7a69  a source code zi
+00004460: 7020 6669 6c65 2e63 0300 0000 0000 0000  p file.c........
+00004470: 0000 0000 0c00 0000 0900 0000 4b00 0000  ............K...
+00004480: 73ec 0000 0074 0064 016a 0174 026a 0374  s....t.d.j.t.j.t
+00004490: 046a 057c 016a 0664 028d 0383 0101 0074  .j.|.j.d.......t
+000044a0: 0783 007d 0474 08a0 097c 016a 0aa1 0144  ...}.t...|.j...D
+000044b0: 005d 625c 037d 057d 067d 077c 05a0 0b64  .]b\.}.}.}.|...d
+000044c0: 03a1 0172 4271 2c7c 0744 005d 467d 087c  ...rBq,|.D.]F}.|
+000044d0: 08a0 0b64 04a1 0173 467c 08a0 0b64 05a1  ...d...sF|...d..
+000044e0: 0172 6071 4674 086a 0ca0 0d7c 057c 08a1  .r`qFt.j...|.|..
+000044f0: 027d 0974 086a 0ca0 0e7c 097c 016a 0fa1  .}.t.j...|.|.j..
+00004500: 027d 0a7c 04a0 107c 097c 0a66 02a1 0101  .}.|...|.|.f....
+00004510: 0071 4671 2c7c 0264 066b 0872 de74 117c  .qFq,|.d.k.r.t.|
+00004520: 016a 1283 0101 0074 137c 016a 0683 0101  .j.....t.|.j....
+00004530: 0074 147c 016a 0664 0783 028f 207d 0b7c  .t.|.j.d.... }.|
+00004540: 0444 005d 145c 027d 097d 0a7c 0ba0 157c  .D.].\.}.}.|...|
+00004550: 097c 0aa1 0201 0071 be57 0035 0051 0052  .|.....q.W.5.Q.R
+00004560: 0058 0074 1664 0864 098d 0101 0064 0a53  .X.t.d.d.....d.S
+00004570: 0029 0b72 3400 0000 7a2f 7b63 7961 6e7d  .).r4...z/{cyan}
+00004580: 6275 696c 6420 6c61 6d62 6461 2073 6f75  build lambda sou
+00004590: 7263 6520 636f 6465 2061 7420 7b72 6573  rce code at {res
+000045a0: 6574 7d7b 7061 7468 7d72 4e00 0000 da0b  et}{path}rN.....
+000045b0: 5f5f 7079 6361 6368 655f 5f7a 042e 7079  __pycache__z..py
+000045c0: 637a 042e 7079 6f46 da01 7772 0500 0000  cz..pyoF..wr....
+000045d0: 723c 0000 004e 2917 7219 0000 0072 3e00  r<...N).r....r>.
+000045e0: 0000 7216 0000 0072 3f00 0000 7217 0000  ..r....r?...r...
+000045f0: 0072 4000 0000 da18 7061 7468 5f6c 616d  .r@.....path_lam
+00004600: 6264 615f 6275 696c 645f 736f 7572 6365  bda_build_source
+00004610: da04 6c69 7374 7241 0000 00da 0477 616c  ..listrA.....wal
+00004620: 6bda 0e64 6972 5f70 7974 686f 6e5f 6c69  k..dir_python_li
+00004630: 62da 0865 6e64 7377 6974 6872 4200 0000  b..endswithrB...
+00004640: 728a 0000 00da 0772 656c 7061 7468 725d  r......relpathr]
+00004650: 0000 0072 5300 0000 720e 0000 00da 1064  ...rS...r......d
+00004660: 6972 5f6c 616d 6264 615f 6275 696c 6472  ir_lambda_buildr
+00004670: 0d00 0000 7204 0000 00da 0577 7269 7465  ....r......write
+00004680: 721a 0000 0029 0c72 4800 0000 7249 0000  r....).rH...rI..
+00004690: 0072 4a00 0000 7222 0000 005a 0b74 6f5f  .rJ...r"...Z.to_
+000046a0: 7a69 705f 6c69 7374 da07 6469 726e 616d  zip_list..dirnam
+000046b0: 6572 1e00 0000 5a0d 6261 7365 6e61 6d65  er....Z.basename
+000046c0: 5f6c 6973 74da 0862 6173 656e 616d 65da  _list..basename.
+000046d0: 0b73 6f75 7263 655f 7061 7468 5a0c 6172  .source_pathZ.ar
+000046e0: 6368 6976 655f 7061 7468 da01 6672 2000  chive_path..fr .
+000046f0: 0000 7220 0000 0072 2600 0000 da18 6275  ..r ...r&.....bu
+00004700: 696c 645f 6c61 6d62 6461 5f73 6f75 7263  ild_lambda_sourc
+00004710: 655f 636f 6465 7703 0000 7330 0000 0000  e_codew...s0....
+00004720: 0702 0104 0104 0104 0104 fd04 ff04 0906  ................
+00004730: 0116 020a 0102 0108 0214 0102 010e 0110  ................
+00004740: 0112 0208 010a 010a 020e 010c 0118 027a  ...............z
+00004750: 2041 6374 696f 6e73 2e62 7569 6c64 5f6c   Actions.build_l
+00004760: 616d 6264 615f 736f 7572 6365 5f63 6f64  ambda_source_cod
+00004770: 6563 0500 0000 0000 0000 0000 0000 0e00  ec..............
+00004780: 0000 0700 0000 4b00 0000 7304 0100 0074  ......K...s....t
+00004790: 0064 016a 0174 026a 0374 046a 057c 027c  .d.j.t.j.t.j.|.|
+000047a0: 0364 028d 0483 0101 007c 0264 036b 0272  .d.......|.d.k.r
+000047b0: 2a7c 016a 067d 066e 147c 0264 046b 0272  *|.j.}.n.|.d.k.r
+000047c0: 3a7c 016a 077d 066e 0474 0882 0174 096a  :|.j.}.n.t...t.j
+000047d0: 0aa0 0b7c 03a1 0172 e674 0ca0 0d7c 03a1  ...|...r.t...|..
+000047e0: 017d 0774 0e7c 0683 015c 027d 087d 0974  .}.t.|...\.}.}.t
+000047f0: 0f7c 0964 05a0 017c 07a1 0167 0264 0664  .|.d...|...g.d.d
+00004800: 078d 027d 0a74 107c 087c 0a83 027d 0b74  ...}.t.|.|...}.t
+00004810: 0064 086a 0174 026a 0374 1174 046a 057c  .d.j.t.j.t.t.j.|
+00004820: 0b64 098d 0483 0101 0064 0a64 0b64 0c7c  .d.......d.d.d.|
+00004830: 037c 0b67 057d 0c7c 016a 12a0 13a1 007d  .|.g.}.|.j.....}
+00004840: 0d7c 0d64 0d6b 0972 c87c 0ca0 1464 0e7c  .|.d.k.r.|...d.|
+00004850: 0d67 02a1 0101 007c 0464 066b 0872 da74  .g.....|.d.k.r.t
+00004860: 15a0 167c 0ca1 0101 0074 1764 0f64 108d  ...|.....t.d.d..
+00004870: 0101 006e 1a74 0064 116a 0174 1174 026a  ...n.t.d.j.t.t.j
+00004880: 1874 026a 037c 0364 128d 0483 0101 0064  .t.j.|.d.......d
+00004890: 0d53 0029 137a 630a 2020 2020 2020 2020  .S.).zc.        
+000048a0: 3a74 7970 6520 636f 6e66 6967 3a20 5265  :type config: Re
+000048b0: 706f 436f 6e66 6967 0a20 2020 2020 2020  poConfig.       
+000048c0: 203a 7061 7261 6d20 736f 7572 6365 5f6f   :param source_o
+000048d0: 725f 6c61 7965 723a 2022 736f 7572 6365  r_layer: "source
+000048e0: 2063 6f64 6522 206f 7220 226c 6179 6572   code" or "layer
+000048f0: 220a 2020 2020 2020 2020 7a48 7b63 7961  ".        zH{cya
+00004900: 6e7d 7570 6c6f 6164 206c 616d 6264 6120  n}upload lambda 
+00004910: 7b73 6f75 7263 655f 6f72 5f6c 6179 6572  {source_or_layer
+00004920: 7d20 6672 6f6d 207b 7265 7365 747d 7b70  } from {reset}{p
+00004930: 6174 687d 207b 6379 616e 7d74 6f20 4157  ath} {cyan}to AW
+00004940: 5320 5333 2904 7236 0000 0072 3700 0000  S S3).r6...r7...
+00004950: da0f 736f 7572 6365 5f6f 725f 6c61 7965  ..source_or_laye
+00004960: 7272 4200 0000 fa0b 736f 7572 6365 2063  rrB.....source c
+00004970: 6f64 65da 056c 6179 6572 fa06 7b7d 2e7a  ode..layer..{}.z
+00004980: 6970 46a9 02da 0570 6172 7473 da06 6973  ipF....parts..is
+00004990: 5f64 6972 7a24 7b63 7961 6e7d 7b74 6162  _dirz${cyan}{tab
+000049a0: 7d75 706c 6f61 6420 746f 207b 7265 7365  }upload to {rese
+000049b0: 747d 7b73 335f 7572 697d 2904 7236 0000  t}{s3_uri}).r6..
+000049c0: 0072 3a00 0000 7237 0000 00da 0673 335f  .r:...r7.....s3_
+000049d0: 7572 6972 9000 0000 7291 0000 005a 0263  urir....r....Z.c
+000049e0: 704e 7292 0000 0072 0500 0000 723c 0000  pNr....r....r<..
+000049f0: 00fa 217b 7265 647d 7b74 6162 7d7b 7061  ..!{red}{tab}{pa
+00004a00: 7468 7d20 7b63 7961 6e7d 6e6f 7420 666f  th} {cyan}not fo
+00004a10: 756e 6421 a904 723a 0000 0072 6000 0000  und!..r:...r`...
+00004a20: 7236 0000 0072 4200 0000 2919 7219 0000  r6...rB...).r...
+00004a30: 0072 3e00 0000 7216 0000 0072 3f00 0000  .r>...r....r?...
+00004a40: 7217 0000 0072 4000 0000 5a29 7333 5f75  r....r@...Z)s3_u
+00004a50: 7269 5f6c 616d 6264 615f 6465 706c 6f79  ri_lambda_deploy
+00004a60: 5f76 6572 7369 6f6e 6564 5f73 6f75 7263  _versioned_sourc
+00004a70: 655f 6469 72da 2873 335f 7572 695f 6c61  e_dir.(s3_uri_la
+00004a80: 6d62 6461 5f64 6570 6c6f 795f 7665 7273  mbda_deploy_vers
+00004a90: 696f 6e65 645f 6c61 7965 725f 6469 7272  ioned_layer_dirr
+00004aa0: 7b00 0000 7241 0000 0072 4200 0000 7243  {...rA...rB...rC
+00004ab0: 0000 0072 0700 0000 da07 6f66 5f66 696c  ...r......of_fil
+00004ac0: 6572 1000 0000 7213 0000 0072 0f00 0000  er....r....r....
+00004ad0: 7218 0000 00da 1d41 5753 5f4c 414d 4244  r......AWS_LAMBD
+00004ae0: 415f 4445 504c 4f59 5f41 5753 5f50 524f  A_DEPLOY_AWS_PRO
+00004af0: 4649 4c45 725a 0000 0072 9500 0000 7244  FILErZ...r....rD
+00004b00: 0000 0072 4500 0000 721a 0000 0072 6200  ...rE...r....rb.
+00004b10: 0000 290e 7248 0000 0072 4900 0000 72b6  ..).rH...rI...r.
+00004b20: 0000 0072 4200 0000 724a 0000 0072 2200  ...rB...rJ...r".
+00004b30: 0000 5a22 7333 5f75 7269 5f6c 616d 6264  ..Z"s3_uri_lambd
+00004b40: 615f 6465 706c 6f79 5f76 6572 7369 6f6e  a_deploy_version
+00004b50: 6564 5f64 6972 da0a 736f 7572 6365 5f6d  ed_dir..source_m
+00004b60: 6435 da06 6275 636b 6574 da06 7072 6566  d5..bucket..pref
+00004b70: 6978 da03 6b65 7972 bd00 0000 7221 0000  ix..keyr....r!..
+00004b80: 00da 0b61 7773 5f70 726f 6669 6c65 7220  ...aws_profiler 
+00004b90: 0000 0072 2000 0000 7226 0000 00da 125f  ...r ...r&....._
+00004ba0: 7570 6c6f 6164 5f6c 616d 6264 615f 7a69  upload_lambda_zi
+00004bb0: 709e 0300 0073 6200 0000 000c 0201 0401  p....sb.........
+00004bc0: 0401 0401 0201 02fc 04ff 0408 0801 0801  ................
+00004bd0: 0801 0802 0402 0c01 0a01 0c01 0201 0c01  ................
+00004be0: 02fe 0604 0a01 0201 0401 0401 0201 0401  ................
+00004bf0: 02fc 04ff 0409 0200 0200 0201 0200 02fe  ................
+00004c00: 0404 0a01 0801 0e01 0801 0a01 0c02 0201  ................
+00004c10: 0401 0201 0401 0401 02fc 04ff 7a1a 4163  ............z.Ac
+00004c20: 7469 6f6e 732e 5f75 706c 6f61 645f 6c61  tions._upload_la
+00004c30: 6d62 6461 5f7a 6970 7a2d 5570 6c6f 6164  mbda_zipz-Upload
+00004c40: 2041 5753 204c 616d 6264 6120 736f 7572   AWS Lambda sour
+00004c50: 6365 2063 6f64 6520 7a69 7020 6669 6c65  ce code zip file
+00004c60: 2074 6f20 5333 2e63 0300 0000 0000 0000   to S3.c........
+00004c70: 0000 0000 0400 0000 0600 0000 4b00 0000  ............K...
+00004c80: 7320 0000 007c 006a 007c 0166 0164 017c  s ...|.j.|.f.d.|
+00004c90: 016a 017c 0264 029c 037c 0397 028e 0101  .j.|.d...|......
+00004ca0: 0064 0353 0029 0472 3400 0000 72b7 0000  .d.S.).r4...r...
+00004cb0: 00a9 0372 b600 0000 7242 0000 0072 4a00  ...r....rB...rJ.
+00004cc0: 0000 4e29 0272 c800 0000 72a9 0000 0072  ..N).r....r....r
+00004cd0: 4700 0000 7220 0000 0072 2000 0000 7226  G...r ...r ...r&
+00004ce0: 0000 00da 1975 706c 6f61 645f 6c61 6d62  .....upload_lamb
+00004cf0: 6461 5f73 6f75 7263 655f 636f 6465 dd03  da_source_code..
+00004d00: 0000 7312 0000 0000 0704 0102 ff02 0202  ..s.............
+00004d10: 0104 0102 fc04 0502 fb7a 2141 6374 696f  .........z!Actio
+00004d20: 6e73 2e75 706c 6f61 645f 6c61 6d62 6461  ns.upload_lambda
+00004d30: 5f73 6f75 7263 655f 636f 6465 6301 0000  _source_codec...
+00004d40: 0000 0000 0000 0000 0003 0000 0008 0000  ................
+00004d50: 0043 0000 0073 6200 0000 7400 7308 7401  .C...sb...t.s.t.
+00004d60: 7256 7402 6a03 a004 6401 6402 6403 6404  rVt.j...d.d.d.d.
+00004d70: a104 7402 6a03 a004 6401 6402 6405 6403  ..t.j...d.d.d.d.
+00004d80: 6404 a105 6702 7d01 7c01 4400 5d18 7d02  d...g.}.|.D.].}.
+00004d90: 7402 6a03 a005 7c02 a101 7232 7c02 0200  t.j...|...r2|...
+00004da0: 0100 5300 7132 7406 6406 8301 8201 6e08  ..S.q2t.d.....n.
+00004db0: 7406 6407 8301 8201 6408 5300 2909 7a41  t.d.....d.S.).zA
+00004dc0: 0a20 2020 2020 2020 2046 696e 6420 7468  .        Find th
+00004dd0: 6520 6162 736f 6c75 7465 2070 6174 6820  e absolute path 
+00004de0: 6f66 2074 6865 2064 6f63 6b65 7220 6578  of the docker ex
+00004df0: 6563 7574 6162 6c65 0a20 2020 2020 2020  ecutable.       
+00004e00: 20fa 012f 5a03 7573 72da 0362 696e 5a06   ../Z.usr..binZ.
+00004e10: 646f 636b 6572 da05 6c6f 6361 6c7a 3857  docker..localz8W
+00004e20: 6520 6361 6e6e 6f74 2066 696e 6420 646f  e cannot find do
+00004e30: 636b 6572 2c20 6172 6520 796f 7520 7375  cker, are you su
+00004e40: 7265 2064 6f63 6b65 7220 6973 2069 6e73  re docker is ins
+00004e50: 7461 6c6c 6564 3f7a 2e57 6520 6361 6e20  talled?z.We can 
+00004e60: 6f6e 6c79 2066 696e 6420 646f 636b 6572  only find docker
+00004e70: 2062 696e 206f 6e20 4d61 634f 5320 6f72   bin on MacOS or
+00004e80: 204c 696e 7578 214e 2907 720a 0000 0072   Linux!N).r....r
+00004e90: 0b00 0000 7241 0000 0072 4200 0000 728a  ....rA...rB...r.
+00004ea0: 0000 0072 4300 0000 da10 456e 7669 726f  ...rC.....Enviro
+00004eb0: 6e6d 656e 7445 7272 6f72 2903 7248 0000  nmentError).rH..
+00004ec0: 005a 096c 6f63 6174 696f 6e73 7255 0000  .Z.locationsrU..
+00004ed0: 0072 2000 0000 7220 0000 0072 2600 0000  .r ...r ...r&...
+00004ee0: da0c 5f66 696e 645f 646f 636b 6572 ec03  .._find_docker..
+00004ef0: 0000 7312 0000 0000 0408 0210 0112 fe04  ..s.............
+00004f00: 0408 010c 010a 010a 027a 1441 6374 696f  .........z.Actio
+00004f10: 6e73 2e5f 6669 6e64 5f64 6f63 6b65 727a  ns._find_dockerz
+00004f20: 4642 7569 6c64 206c 616d 6264 6120 6c61  FBuild lambda la
+00004f30: 7965 7220 7573 696e 6720 6120 4157 5320  yer using a AWS 
+00004f40: 6c61 6d62 6461 2072 756e 7469 6d65 2063  lambda runtime c
+00004f50: 6f6d 7061 7469 626c 6520 646f 636b 6572  ompatible docker
+00004f60: 2069 6d61 6765 2e63 0300 0000 0000 0000   image.c........
+00004f70: 0000 0000 0600 0000 0a00 0000 4b00 0000  ............K...
+00004f80: 73a2 0000 007c 01a0 007c 016a 016a 02a1  s....|...|.j.j..
+00004f90: 0101 007c 01a0 007c 016a 036a 02a1 0101  ...|...|.j.j....
+00004fa0: 0074 0464 016a 0574 066a 0774 086a 097c  .t.d.j.t.j.t.j.|
+00004fb0: 016a 01a0 0aa1 007c 016a 0b64 028d 0483  .j.....|.j.d....
+00004fc0: 0101 0074 0c7c 016a 0d83 0101 007c 00a0  ...t.|.j.....|..
+00004fd0: 0ea1 007d 0474 0f6a 10a0 117c 016a 03a0  ...}.t.j...|.j..
+00004fe0: 0aa1 0064 0364 04a1 037d 057c 0264 056b  ...d.d...}.|.d.k
+00004ff0: 0872 9e74 12a0 137c 0464 0664 0764 08a0  .r.t...|.d.d.d..
+00005000: 057c 016a 147c 016a 03a0 0aa1 00a1 0264  .|.j.|.j.......d
+00005010: 097c 016a 01a0 0aa1 0064 0a7c 0567 08a1  .|.j.....d.|.g..
+00005020: 0101 0064 0b53 0029 0c72 3400 0000 7a59  ...d.S.).r4...zY
+00005030: 7b63 7961 6e7d 6275 696c 6420 6c61 6d62  {cyan}build lamb
+00005040: 6461 206c 6179 6572 2069 6e20 7b72 6573  da layer in {res
+00005050: 6574 7d7b 646f 636b 6572 5f69 6d61 6765  et}{docker_image
+00005060: 7d20 7b63 7961 6e7d 646f 636b 6572 2063  } {cyan}docker c
+00005070: 6f6e 7461 696e 6572 2061 7420 7b72 6573  ontainer at {res
+00005080: 6574 7d7b 7061 7468 7d29 0472 3600 0000  et}{path}).r6...
+00005090: 7237 0000 005a 0c64 6f63 6b65 725f 696d  r7...Z.docker_im
+000050a0: 6167 6572 4200 0000 72cc 0000 007a 2463  agerB...r....z$c
+000050b0: 6f6e 7461 696e 6572 2d6f 6e6c 792d 6275  ontainer-only-bu
+000050c0: 696c 642d 6c61 6d62 6461 2d6c 6179 6572  ild-lambda-layer
+000050d0: 2e73 6846 da03 7275 6e7a 022d 767a 057b  .shF..runz.-vz.{
+000050e0: 7d3a 7b7d 7a04 2d2d 726d 5a04 6261 7368  }:{}z.--rmZ.bash
+000050f0: 4e29 155a 1465 6e73 7572 655f 6174 7472  N).Z.ensure_attr
+00005100: 5f6e 6f74 5f6e 6f6e 655a 1d41 5753 5f4c  _not_noneZ.AWS_L
+00005110: 414d 4244 415f 4255 494c 445f 444f 434b  AMBDA_BUILD_DOCK
+00005120: 4552 5f49 4d41 4745 7230 0000 005a 2b41  ER_IMAGEr0...Z+A
+00005130: 5753 5f4c 414d 4244 415f 4255 494c 445f  WS_LAMBDA_BUILD_
+00005140: 444f 434b 4552 5f49 4d41 4745 5f57 4f52  DOCKER_IMAGE_WOR
+00005150: 4b53 5041 4345 5f44 4952 7219 0000 0072  KSPACE_DIRr....r
+00005160: 3e00 0000 7216 0000 0072 3f00 0000 7217  >...r....r?...r.
+00005170: 0000 0072 4000 0000 725a 0000 00da 1770  ...r@...rZ.....p
+00005180: 6174 685f 6c61 6d62 6461 5f62 7569 6c64  ath_lambda_build
+00005190: 5f6c 6179 6572 720e 0000 0072 af00 0000  _layerr....r....
+000051a0: 72cf 0000 0072 4100 0000 7242 0000 0072  r....rA...rB...r
+000051b0: 8a00 0000 7244 0000 0072 4500 0000 725d  ....rD...rE...r]
+000051c0: 0000 0029 0672 4800 0000 7249 0000 0072  ...).rH...rI...r
+000051d0: 4a00 0000 7222 0000 005a 0f70 6174 685f  J...r"...Z.path_
+000051e0: 6269 6e5f 646f 636b 6572 5a2a 636f 6e74  bin_dockerZ*cont
+000051f0: 6169 6e65 725f 6f6e 6c79 5f62 7569 6c64  ainer_only_build
+00005200: 5f6c 6264 5f6c 6179 6572 5f73 6372 6970  _lbd_layer_scrip
+00005210: 745f 7061 7468 7220 0000 0072 2000 0000  t_pathr ...r ...
+00005220: 7226 0000 00da 1262 7569 6c64 5f6c 616d  r&.....build_lam
+00005230: 6264 615f 6c61 7965 72fc 0300 0073 3e00  bda_layer....s>.
+00005240: 0000 0007 0e01 0e01 0201 0401 0401 0401  ................
+00005250: 0801 04fc 04ff 0408 0a02 0801 0601 0801  ................
+00005260: 0201 02fd 0406 0801 0401 0200 0201 0200  ................
+00005270: 0401 0401 08fe 0204 0200 0801 0200 02f9  ................
+00005280: 7a1a 4163 7469 6f6e 732e 6275 696c 645f  z.Actions.build_
+00005290: 6c61 6d62 6461 5f6c 6179 6572 7a27 5570  lambda_layerz'Up
+000052a0: 6c6f 6164 2041 5753 204c 616d 6264 6120  load AWS Lambda 
+000052b0: 6c61 7965 7220 7a69 7020 6669 6c65 2074  layer zip file t
+000052c0: 6f20 5333 2e63 0300 0000 0000 0000 0000  o S3.c..........
+000052d0: 0000 0400 0000 0600 0000 4b00 0000 7320  ..........K...s 
+000052e0: 0000 007c 006a 007c 0166 0164 017c 016a  ...|.j.|.f.d.|.j
+000052f0: 017c 0264 029c 037c 0397 028e 0101 0064  .|.d...|.......d
+00005300: 0353 0029 0472 3400 0000 72b8 0000 0072  .S.).r4...r....r
+00005310: c900 0000 4e29 0272 c800 0000 72d1 0000  ....N).r....r...
+00005320: 0072 4700 0000 7220 0000 0072 2000 0000  .rG...r ...r ...
+00005330: 7226 0000 00da 1375 706c 6f61 645f 6c61  r&.....upload_la
+00005340: 6d62 6461 5f6c 6179 6572 2104 0000 7312  mbda_layer!...s.
+00005350: 0000 0000 0704 0102 ff02 0202 0104 0102  ................
+00005360: fc04 0502 fb7a 1b41 6374 696f 6e73 2e75  .....z.Actions.u
+00005370: 706c 6f61 645f 6c61 6d62 6461 5f6c 6179  pload_lambda_lay
+00005380: 6572 7a27 4465 706c 6f79 2072 6563 656e  erz'Deploy recen
+00005390: 746c 7920 6275 696c 7420 4157 5320 6c61  tly built AWS la
+000053a0: 6d62 6461 206c 6179 6572 2e63 0300 0000  mbda layer.c....
+000053b0: 0000 0000 0000 0000 0b00 0000 0f00 0000  ................
+000053c0: 4b00 0000 733c 0100 0074 0064 016a 0174  K...s<...t.d.j.t
+000053d0: 026a 0374 046a 0564 028d 0283 0101 0074  .j.t.j.d.......t
+000053e0: 066a 07a0 087c 016a 09a1 0190 0172 1c74  .j...|.j.....r.t
+000053f0: 0aa0 0b7c 016a 09a1 017d 0474 0c7c 016a  ...|.j...}.t.|.j
+00005400: 0d83 015c 027d 057d 0674 0e7c 0664 03a0  ...\.}.}.t.|.d..
+00005410: 017c 04a1 0167 0264 0464 058d 027d 0774  .|...g.d.d...}.t
+00005420: 0f7c 057c 0764 068d 027d 0874 0064 076a  .|.|.d...}.t.d.j
+00005430: 0174 026a 0374 1074 046a 057c 0864 088d  .t.j.t.t.j.|.d..
+00005440: 0483 0101 0064 0964 0a64 0b64 0c7c 016a  .....d.d.d.d.|.j
+00005450: 1164 0d64 0ea0 017c 016a 11a1 0164 0f64  .d.d...|.j...d.d
+00005460: 10a0 017c 016a 12a0 13a1 007c 07a1 0264  ...|.j.....|...d
+00005470: 1164 12a0 017c 016a 14a0 13a1 007c 016a  .d...|.j.....|.j
+00005480: 15a0 13a1 00a1 0267 0b7d 097c 016a 16a0  .......g.}.|.j..
+00005490: 13a1 007d 0a7c 0a64 136b 0972 e27c 09a0  ...}.|.d.k.r.|..
+000054a0: 1764 147c 0a67 02a1 0101 007c 0264 046b  .d.|.g.....|.d.k
+000054b0: 0872 f474 18a0 197c 09a1 0101 0074 0064  .r.t...|.....t.d
+000054c0: 156a 0174 026a 0374 1074 046a 057c 016a  .j.t.j.t.t.j.|.j
+000054d0: 1a64 168d 0483 0101 0074 1b64 1764 188d  .d.......t.d.d..
+000054e0: 0101 006e 1c74 0064 196a 0174 1074 026a  ...n.t.d.j.t.t.j
+000054f0: 1c74 026a 037c 016a 0964 1a8d 0483 0101  .t.j.|.j.d......
+00005500: 0064 1353 0029 1b72 3400 0000 7a36 7b63  .d.S.).r4...z6{c
+00005510: 7961 6e7d 6465 706c 6f79 2061 206e 6577  yan}deploy a new
+00005520: 2076 6572 7369 6f6e 206f 6620 6c61 6d62   version of lamb
+00005530: 6461 206c 6179 6572 2066 726f 6d20 4157  da layer from AW
+00005540: 5320 5333 7261 0000 0072 b900 0000 4672  S S3ra...r....Fr
+00005550: ba00 0000 2902 72c4 0000 0072 c500 0000  ....).r....r....
+00005560: 7a75 7b63 7961 6e7d 7b74 6162 7d72 756e  zu{cyan}{tab}run
+00005570: 207b 7265 7365 747d 2761 7773 206c 616d   {reset}'aws lam
+00005580: 6264 6120 7075 626c 6973 682d 6c61 7965  bda publish-laye
+00005590: 722d 7665 7273 696f 6e27 207b 6379 616e  r-version' {cyan
+000055a0: 7d63 6f6d 6d61 6e64 2c20 7072 6576 6965  }command, previe
+000055b0: 7720 6c61 7965 7220 6669 6c65 2061 7420  w layer file at 
+000055c0: 7b72 6573 6574 7d7b 7333 5f63 6f6e 736f  {reset}{s3_conso
+000055d0: 6c65 5f75 726c 7d29 0472 3600 0000 723a  le_url}).r6...r:
+000055e0: 0000 0072 3700 0000 7294 0000 0072 9000  ...r7...r....r..
+000055f0: 0000 da06 6c61 6d62 6461 7a15 7075 626c  ....lambdaz.publ
+00005600: 6973 682d 6c61 7965 722d 7665 7273 696f  ish-layer-versio
+00005610: 6e7a 0c2d 2d6c 6179 6572 2d6e 616d 657a  nz.--layer-namez
+00005620: 0d2d 2d64 6573 6372 6970 7469 6f6e 7a32  .--descriptionz2
+00005630: 6465 7065 6e64 656e 6379 206c 6179 6572  dependency layer
+00005640: 2066 6f72 2061 6c6c 2066 756e 6374 696f   for all functio
+00005650: 6e73 2069 6e20 277b 7d27 2070 726f 6a65  ns in '{}' proje
+00005660: 6374 7a09 2d2d 636f 6e74 656e 747a 1453  ctz.--contentz.S
+00005670: 3342 7563 6b65 743d 7b7d 2c53 334b 6579  3Bucket={},S3Key
+00005680: 3d7b 7d7a 152d 2d63 6f6d 7061 7469 626c  ={}z.--compatibl
+00005690: 652d 7275 6e74 696d 6573 7a0b 7079 7468  e-runtimesz.pyth
+000056a0: 6f6e 7b7d 2e7b 7d4e 7292 0000 007a 307b  on{}.{}Nr....z0{
+000056b0: 6379 616e 7d7b 7461 627d 6f70 656e 207b  cyan}{tab}open {
+000056c0: 7265 7365 747d 7b75 726c 7d20 7b63 7961  reset}{url} {cya
+000056d0: 6e7d 746f 2076 6965 7720 6c61 7965 7229  n}to view layer)
+000056e0: 0472 3600 0000 723a 0000 0072 3700 0000  .r6...r:...r7...
+000056f0: da03 7572 6c72 0500 0000 723c 0000 0072  ..urlr....r<...r
+00005700: be00 0000 72bf 0000 0029 1d72 1900 0000  ....r....).r....
+00005710: 723e 0000 0072 1600 0000 723f 0000 0072  r>...r....r?...r
+00005720: 1700 0000 7240 0000 0072 4100 0000 7242  ....r@...rA...rB
+00005730: 0000 0072 4300 0000 72d1 0000 0072 0700  ...rC...r....r..
+00005740: 0000 72c1 0000 0072 1000 0000 72c0 0000  ..r....r....r...
+00005750: 0072 1300 0000 7211 0000 0072 1800 0000  .r....r....r....
+00005760: 5a15 6177 735f 6c61 6d62 6461 5f6c 6179  Z.aws_lambda_lay
+00005770: 6572 5f6e 616d 655a 1b41 5753 5f4c 414d  er_nameZ.AWS_LAM
+00005780: 4244 415f 4445 504c 4f59 5f53 335f 4255  BDA_DEPLOY_S3_BU
+00005790: 434b 4554 725a 0000 005a 1044 4556 5f50  CKETrZ...Z.DEV_P
+000057a0: 595f 5645 525f 4d41 4a4f 525a 1044 4556  Y_VER_MAJORZ.DEV
+000057b0: 5f50 595f 5645 525f 4d49 4e4f 5272 c200  _PY_VER_MINORr..
+000057c0: 0000 7295 0000 0072 4400 0000 7245 0000  ..r....rD...rE..
+000057d0: 005a 1875 726c 5f6c 616d 6264 615f 6c61  .Z.url_lambda_la
+000057e0: 7965 725f 636f 6e73 6f6c 6572 1a00 0000  yer_consoler....
+000057f0: 7262 0000 0029 0b72 4800 0000 7249 0000  rb...).rH...rI..
+00005800: 0072 4a00 0000 7222 0000 0072 c300 0000  .rJ...r"...r....
+00005810: 72c4 0000 0072 c500 0000 72c6 0000 0072  r....r....r....r
+00005820: 9400 0000 7221 0000 0072 c700 0000 7220  ....r!...r....r 
+00005830: 0000 0072 2000 0000 7226 0000 00da 1364  ...r ...r&.....d
+00005840: 6570 6c6f 795f 6c61 6d62 6461 5f6c 6179  eploy_lambda_lay
+00005850: 6572 3004 0000 737c 0000 0000 0702 0104  er0...s|........
+00005860: 0104 0104 fe04 ff04 0610 010c 010e 0102  ................
+00005870: 010c 0102 fe06 040c 0102 0104 0104 0102  ................
+00005880: 0104 0102 fc04 ff04 0902 0002 0002 0102  ................
+00005890: 0004 0102 010a 0102 0004 0108 0002 ff02  ................
+000058a0: 0302 0004 0108 0108 fe02 f804 0d0a 0108  ................
+000058b0: 010e 0108 010a 0102 0104 0104 0102 0104  ................
+000058c0: 0104 fc04 ff04 080c 0202 0104 0102 0104  ................
+000058d0: 0104 0104 fc04 ff7a 1b41 6374 696f 6e73  .......z.Actions
+000058e0: 2e64 6570 6c6f 795f 6c61 6d62 6461 5f6c  .deploy_lambda_l
+000058f0: 6179 6572 7a10 6275 642d 6c61 6d62 6461  ayerz.bud-lambda
+00005900: 2d6c 6179 6572 7a33 2a2a 2042 7569 6c64  -layerz3** Build
+00005910: 2c20 7570 6c6f 6164 2061 6e64 2064 6570  , upload and dep
+00005920: 6c6f 7920 6120 6e65 7720 4157 5320 6c61  loy a new AWS la
+00005930: 6d62 6461 206c 6179 6572 2e63 0300 0000  mbda layer.c....
+00005940: 0000 0000 0000 0000 0400 0000 0400 0000  ................
+00005950: 4b00 0000 733e 0000 007c 006a 007c 017c  K...s>...|.j.|.|
+00005960: 0264 018d 0201 007c 006a 017c 0166 0164  .d.....|.j.|.f.d
+00005970: 027c 0269 017c 0397 028e 0101 007c 006a  .|.i.|.......|.j
+00005980: 027c 0166 0164 027c 0269 017c 0397 028e  .|.f.d.|.i.|....
+00005990: 0101 0064 0353 0029 0472 3400 0000 727f  ...d.S.).r4...r.
+000059a0: 0000 0072 4a00 0000 4e29 0372 d200 0000  ...rJ...N).r....
+000059b0: 72d3 0000 0072 d600 0000 7247 0000 0072  r....r....rG...r
+000059c0: 2000 0000 7220 0000 0072 2600 0000 da20   ...r ...r&.... 
+000059d0: 6275 696c 645f 7570 6c6f 6164 5f64 6570  build_upload_dep
+000059e0: 6c6f 795f 6c61 6d62 6461 5f6c 6179 6572  loy_lambda_layer
+000059f0: 7204 0000 7306 0000 0000 080e 0116 017a  r...s..........z
+00005a00: 2841 6374 696f 6e73 2e62 7569 6c64 5f75  (Actions.build_u
+00005a10: 706c 6f61 645f 6465 706c 6f79 5f6c 616d  pload_deploy_lam
+00005a20: 6264 615f 6c61 7965 7263 0200 0000 0000  bda_layerc......
+00005a30: 0000 0000 0000 0400 0000 0500 0000 4300  ..............C.
+00005a40: 0000 7334 0000 007c 016a 007c 016a 0167  ..s4...|.j.|.j.g
+00005a50: 027d 027c 0244 005d 1e7d 0374 026a 03a0  .}.|.D.].}.t.j..
+00005a60: 047c 03a1 0173 1074 0564 01a0 067c 03a1  .|...s.t.d...|..
+00005a70: 0183 0182 0171 1064 0253 0029 0372 3400  .....q.d.S.).r4.
+00005a80: 0000 7a0d 7b7d 206e 6f74 2065 7869 7374  ..z.{} not exist
+00005a90: 734e 2907 5a1c 7061 7468 5f61 7773 5f63  sN).Z.path_aws_c
+00005aa0: 6861 6c69 6365 5f63 6f6e 6669 675f 6a73  halice_config_js
+00005ab0: 6f6e 5a17 7061 7468 5f61 7773 5f63 6861  onZ.path_aws_cha
+00005ac0: 6c69 6365 5f61 7070 5f70 7972 4100 0000  lice_app_pyrA...
+00005ad0: 7242 0000 0072 4300 0000 727b 0000 0072  rB...rC...r{...r
+00005ae0: 3e00 0000 2904 7248 0000 0072 4900 0000  >...).rH...rI...
+00005af0: da05 6669 6c65 7372 5500 0000 7220 0000  ..filesrU...r ..
+00005b00: 0072 2000 0000 7226 0000 00da 1e5f 656e  .r ...r&....._en
+00005b10: 7375 7265 5f63 6861 6c69 6365 5f6c 616d  sure_chalice_lam
+00005b20: 6264 615f 6170 705f 6469 727e 0400 0073  bda_app_dir~...s
+00005b30: 0c00 0000 0005 0401 04fe 0404 0801 0c01  ................
+00005b40: 7a26 4163 7469 6f6e 732e 5f65 6e73 7572  z&Actions._ensur
+00005b50: 655f 6368 616c 6963 655f 6c61 6d62 6461  e_chalice_lambda
+00005b60: 5f61 7070 5f64 6972 7a2a 2a2a 2044 6570  _app_dirz*** Dep
+00005b70: 6c6f 7920 4157 5320 4c61 6d62 6461 2061  loy AWS Lambda a
+00005b80: 7070 2077 6974 6820 4157 5320 4368 616c  pp with AWS Chal
+00005b90: 6963 652e 6303 0000 0000 0000 0000 0000  ice.c...........
+00005ba0: 0006 0000 0005 0000 004b 0000 0073 9600  .........K...s..
+00005bb0: 0000 7400 6401 6a01 7402 6a03 7404 6a05  ..t.d.j.t.j.t.j.
+00005bc0: 6402 8d02 8301 0100 7c00 a006 7c01 a101  d.......|...|...
+00005bd0: 0100 7407 7c01 6a08 8301 0100 7409 7c01  ..t.|.j.....t.|.
+00005be0: 6a08 8301 0100 740a 7c01 6a0b 7c01 6a0c  j.....t.|.j.|.j.
+00005bf0: 8302 0100 7c01 6a0d 6403 7c01 6a0e 6404  ....|.j.d.|.j.d.
+00005c00: 6704 7d04 7c04 a00f 7c03 6405 1900 a101  g.}.|...|.d.....
+00005c10: 0100 7c01 6a10 a011 a100 7d05 7c05 6406  ..|.j.....}.|.d.
+00005c20: 6b09 7280 7c04 a00f 6407 7c05 6702 a101  k.r.|...d.|.g...
+00005c30: 0100 7c02 6408 6b08 7292 7412 a013 7c04  ..|.d.k.r.t...|.
+00005c40: a101 0100 6406 5300 2909 7234 0000 007a  ....d.S.).r4...z
+00005c50: 2c7b 6379 616e 7d44 6570 6c6f 7920 4157  ,{cyan}Deploy AW
+00005c60: 5320 4c61 6d62 6461 2061 7070 2077 6974  S Lambda app wit
+00005c70: 6820 4157 5320 4368 616c 6963 6572 6100  h AWS Chalicera.
+00005c80: 0000 fa0d 2d2d 7072 6f6a 6563 742d 6469  ....--project-di
+00005c90: 725a 0664 6570 6c6f 79da 055f 6172 6773  rZ.deploy.._args
+00005ca0: 4e72 9200 0000 4629 1472 1900 0000 723e  Nr....F).r....r>
+00005cb0: 0000 0072 1600 0000 723f 0000 0072 1700  ...r....r?...r..
+00005cc0: 0000 7240 0000 0072 d900 0000 720d 0000  ..r@...r....r...
+00005cd0: 005a 1664 6972 5f61 7773 5f63 6861 6c69  .Z.dir_aws_chali
+00005ce0: 6365 5f76 656e 646f 7272 0e00 0000 7215  ce_vendorr....r.
+00005cf0: 0000 0072 ac00 0000 5a1d 6469 725f 6177  ...r....Z.dir_aw
+00005d00: 735f 6368 616c 6963 655f 7665 6e64 6f72  s_chalice_vendor
+00005d10: 5f73 6f75 7263 65da 1570 6174 685f 7665  _source..path_ve
+00005d20: 6e76 5f62 696e 5f63 6861 6c69 6365 da0e  nv_bin_chalice..
+00005d30: 6469 725f 6c61 6d62 6461 5f61 7070 7295  dir_lambda_appr.
+00005d40: 0000 0072 c200 0000 725a 0000 0072 4400  ...r....rZ...rD.
+00005d50: 0000 7245 0000 00a9 0672 4800 0000 7249  ..rE.....rH...rI
+00005d60: 0000 0072 4a00 0000 7222 0000 0072 2100  ...rJ...r"...r!.
+00005d70: 0000 72c7 0000 0072 2000 0000 7220 0000  ..r....r ...r ..
+00005d80: 0072 2600 0000 da0e 6368 616c 6963 655f  .r&.....chalice_
+00005d90: 6465 706c 6f79 8a04 0000 7330 0000 0000  deploy....s0....
+00005da0: 0702 0104 0104 0104 fe04 ff04 070a 030a  ................
+00005db0: 010a 0302 0104 0104 fe04 0704 0102 0004  ................
+00005dc0: 0102 fd04 050e 010a 0108 010e 0208 017a  ...............z
+00005dd0: 1641 6374 696f 6e73 2e63 6861 6c69 6365  .Actions.chalice
+00005de0: 5f64 6570 6c6f 797a 2a2a 2a20 4465 6c65  _deployz*** Dele
+00005df0: 7465 2041 5753 204c 616d 6264 6120 6170  te AWS Lambda ap
+00005e00: 7020 7769 7468 2041 5753 2043 6861 6c69  p with AWS Chali
+00005e10: 6365 2e63 0300 0000 0000 0000 0000 0000  ce.c............
+00005e20: 0600 0000 0500 0000 4b00 0000 7374 0000  ........K...st..
+00005e30: 0074 0064 016a 0174 026a 0374 046a 0564  .t.d.j.t.j.t.j.d
+00005e40: 028d 0283 0101 007c 00a0 067c 01a1 0101  .......|...|....
+00005e50: 007c 016a 0764 037c 016a 0864 0467 047d  .|.j.d.|.j.d.g.}
+00005e60: 047c 04a0 097c 0364 0519 00a1 0101 007c  .|...|.d.......|
+00005e70: 016a 0aa0 0ba1 007d 057c 0564 066b 0972  .j.....}.|.d.k.r
+00005e80: 5e7c 04a0 0964 077c 0567 02a1 0101 007c  ^|...d.|.g.....|
+00005e90: 0264 086b 0872 7074 0ca0 0d7c 04a1 0101  .d.k.rpt...|....
+00005ea0: 0064 0653 0029 0972 3400 0000 7a2c 7b63  .d.S.).r4...z,{c
+00005eb0: 7961 6e7d 4465 6c65 7465 2041 5753 204c  yan}Delete AWS L
+00005ec0: 616d 6264 6120 6170 7020 7769 7468 2041  ambda app with A
+00005ed0: 5753 2043 6861 6c69 6365 7261 0000 0072  WS Chalicera...r
+00005ee0: da00 0000 da06 6465 6c65 7465 72db 0000  ......deleter...
+00005ef0: 004e 7292 0000 0046 290e 7219 0000 0072  .Nr....F).r....r
+00005f00: 3e00 0000 7216 0000 0072 3f00 0000 7217  >...r....r?...r.
+00005f10: 0000 0072 4000 0000 72d9 0000 0072 dc00  ...r@...r....r..
+00005f20: 0000 72dd 0000 0072 9500 0000 72c2 0000  ..r....r....r...
+00005f30: 0072 5a00 0000 7244 0000 0072 4500 0000  .rZ...rD...rE...
+00005f40: 72de 0000 0072 2000 0000 7220 0000 0072  r....r ...r ...r
+00005f50: 2600 0000 da0e 6368 616c 6963 655f 6465  &.....chalice_de
+00005f60: 6c65 7465 b204 0000 7324 0000 0000 0702  lete....s$......
+00005f70: 0104 0104 0104 fe04 ff04 060a 0304 0102  ................
+00005f80: 0004 0102 fd04 050e 010a 0108 010e 0208  ................
+00005f90: 017a 1641 6374 696f 6e73 2e63 6861 6c69  .z.Actions.chali
+00005fa0: 6365 5f64 656c 6574 654e 2901 4629 0146  ce_deleteN).F).F
+00005fb0: 2902 4646 2901 4629 0146 2901 4629 0146  ).FF).F).F).F).F
+00005fc0: 2901 4629 0146 2901 4629 0146 2901 4629  ).F).F).F).F).F)
+00005fd0: 0146 2901 4629 0146 2901 4629 0146 2901  .F).F).F).F).F).
+00005fe0: 4629 0146 2901 4629 0146 2901 4629 0146  F).F).F).F).F).F
+00005ff0: 2901 4629 0146 2901 4629 0146 2901 4629  ).F).F).F).F).F)
+00006000: 0146 2901 4629 0146 2901 4629 0146 2901  .F).F).F).F).F).
+00006010: 4629 0146 2901 4629 0146 2901 4629 2d72  F).F).F).F).F)-r
+00006020: 2800 0000 da0a 5f5f 6d6f 6475 6c65 5f5f  (.....__module__
+00006030: da0c 5f5f 7175 616c 6e61 6d65 5f5f da07  ..__qualname__..
+00006040: 5f5f 646f 635f 5f72 3200 0000 724b 0000  __doc__r2...rK..
+00006050: 0072 4c00 0000 7256 0000 0072 5b00 0000  .rL...rV...r[...
+00006060: 725e 0000 0072 5f00 0000 7265 0000 0072  r^...r_...re...r
+00006070: 6900 0000 726b 0000 0072 6d00 0000 7270  i...rk...rm...rp
+00006080: 0000 0072 7500 0000 7278 0000 0072 7900  ...ru...rx...ry.
+00006090: 0000 727a 0000 0072 7c00 0000 727d 0000  ..rz...r|...r}..
+000060a0: 0072 7e00 0000 7280 0000 0072 8900 0000  .r~...r....r....
+000060b0: 728b 0000 0072 8c00 0000 728d 0000 0072  r....r....r....r
+000060c0: 9700 0000 729a 0000 0072 9b00 0000 72a1  ....r....r....r.
+000060d0: 0000 0072 a500 0000 72a6 0000 0072 b500  ...r....r....r..
+000060e0: 0000 72c8 0000 0072 ca00 0000 72cf 0000  ..r....r....r...
+000060f0: 0072 d200 0000 72d3 0000 0072 d600 0000  .r....r....r....
+00006100: 72d7 0000 0072 d900 0000 72df 0000 0072  r....r....r....r
+00006110: e100 0000 7220 0000 0072 2000 0000 7220  ....r ...r ...r 
+00006120: 0000 0072 2600 0000 7233 0000 0048 0000  ...r&...r3...H..
+00006130: 0073 4401 0000 0801 040c 0201 02ff 0403  .sD.............
+00006140: 0c24 0201 02ff 0403 0c17 0201 02ff 0406  .$..............
+00006150: 0001 00fc 0c23 0201 02ff 0403 0c13 0201  .....#..........
+00006160: 02ff 0403 0c14 0201 02ff 0403 0c13 0201  ................
+00006170: 02ff 0403 0c38 0201 02ff 0403 0c13 0201  .....8..........
+00006180: 02ff 0403 0c13 0201 02ff 0403 0c13 0201  ................
+00006190: 02ff 0403 0c38 0201 0201 02fe 0404 0c13  .....8..........
+000061a0: 0201 0201 02fe 0404 0c0a 0201 0201 02fe  ................
+000061b0: 0404 0c16 0201 0201 02fe 0404 0c0b 0201  ................
+000061c0: 02ff 0403 0c14 0201 0201 02fe 0404 0c12  ................
+000061d0: 0201 0201 02fe 0404 0c0a 0201 0201 02fe  ................
+000061e0: 0404 0c13 0201 02ff 0403 0c1a 0201 02ff  ................
+000061f0: 0403 0c0c 0201 02ff 0403 0c0f 0201 02ff  ................
+00006200: 0403 0c22 00fa 0a51 0201 02ff 0403 0c0d  ..."...Q........
+00006210: 0201 02ff 0403 0c0d 0201 02ff 0403 0c13  ................
+00006220: 0201 0201 02fe 0404 0c27 0201 02ff 0403  .........'......
+00006230: 0c0e 0201 02ff 0403 0c29 00fb 0a3f 0201  .........)...?..
+00006240: 02ff 0403 0c0c 0810 0201 02ff 0403 0c22  ..............."
+00006250: 0201 02ff 0403 0c0c 0201 02ff 0403 0c3f  ...............?
+00006260: 0201 0201 02fe 0404 0c08 080c 0201 02ff  ................
+00006270: 0403 0c25 0201 02ff 0403 7233 0000 0029  ...%......r3...)
+00006280: 024e 4e29 2d72 e400 0000 5a0a 5f5f 6675  .NN)-r....Z.__fu
+00006290: 7475 7265 5f5f 7202 0000 0072 0300 0000  ture__r....r....
+000062a0: da06 7479 7069 6e67 da0b 496d 706f 7274  ..typing..Import
+000062b0: 4572 726f 7272 4100 0000 7244 0000 0072  ErrorrA...rD...r
+000062c0: 2c00 0000 da07 7a69 7066 696c 6572 0400  ,.....zipfiler..
+000062d0: 0000 5a0c 706b 672e 6d69 6e69 5f73 6978  ..Z.pkg.mini_six
+000062e0: 7206 0000 005a 0f70 6b67 2e66 696e 6765  r....Z.pkg.finge
+000062f0: 7270 7269 6e74 7207 0000 00da 0b72 6570  rprintr......rep
+00006300: 6f5f 636f 6e66 6967 7208 0000 005a 106f  o_configr....Z.o
+00006310: 7065 7261 7469 6f6e 5f73 7973 7465 6d72  peration_systemr
+00006320: 0900 0000 720a 0000 0072 0b00 0000 720c  ....r....r....r.
+00006330: 0000 005a 0768 656c 7065 7273 720d 0000  ...Z.helpersr...
+00006340: 0072 0e00 0000 720f 0000 0072 1000 0000  .r....r....r....
+00006350: 7211 0000 0072 1200 0000 7213 0000 0072  r....r....r....r
+00006360: 1400 0000 7215 0000 005a 0b63 6f6c 6f72  ....r....Z.color
+00006370: 5f70 7269 6e74 7216 0000 0072 1700 0000  _printr....r....
+00006380: 7218 0000 0072 1900 0000 721a 0000 0072  r....r....r....r
+00006390: 1b00 0000 721c 0000 0072 1d00 0000 7232  ....r....r....r2
+000063a0: 0000 00da 066f 626a 6563 7472 3300 0000  .....objectr3...
+000063b0: da07 6163 7469 6f6e 7372 2000 0000 7220  ..actionsr ...r 
+000063c0: 0000 0072 2000 0000 7226 0000 00da 083c  ...r ...r&.....<
+000063d0: 6d6f 6475 6c65 3e03 0000 0073 3a00 0000  module>....s:...
+000063e0: 0405 1002 0201 0c01 0e01 0602 0801 0801  ................
+000063f0: 0801 0c02 0c01 0c01 0c01 1804 2c0a 2807  ............,.(.
+00006400: 0001 00fe 0a1d 107f 007f 007f 007f 007f  ................
+00006410: 007f 007f 007f 007f 0010                 ..........
```

### Comparing `pygitrepo-1.0.7/pygitrepo/__pycache__/cli.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/__pycache__/cli.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/__pycache__/color_print.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/__pycache__/color_print.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/__pycache__/helpers.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/__pycache__/helpers.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/__pycache__/operation_system.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/__pycache__/operation_system.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/__pycache__/repo_config.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/__pycache__/repo_config.cpython-38.pyc`

 * *Format-specific differences are supported for Python .pyc files but no file-specific differences were detected; falling back to a binary diff. file(1) reports: Byte-compiled Python module for CPython 3.8, timestamp-based, .py timestamp: Sat Apr  2 21:08:28 2022 UTC, .py size: 22053 bytes*

 * *Could not decompile bytecode: bad marshal data (unknown type code)*

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-00000000: 550d 0d0a 0000 0000 4cbb 4862 2556 0000  U.......L.Hb%V..
+00000000: 550d 0d0a 0000 0000 b5c3 4862 a656 0000  U.........Hb.V..
 00000010: e300 0000 0000 0000 0000 0000 0000 0000  ................
 00000020: 0006 0000 0040 0000 0073 b800 0000 6400  .....@...s....d.
 00000030: 6401 6c00 5a00 6400 6401 6c01 5a01 6400  d.l.Z.d.d.l.Z.d.
 00000040: 6401 6c02 5a02 6402 6403 6c03 6d04 5a04  d.l.Z.d.d.l.m.Z.
 00000050: 6d05 5a05 6d06 5a06 0100 6402 6404 6c07  m.Z.m.Z...d.d.l.
 00000060: 6d08 5a08 0100 6402 6405 6c09 6d0a 5a0a  m.Z...d.d.l.m.Z.
 00000070: 6d0b 5a0b 6d0c 5a0c 0100 6402 6406 6c0d  m.Z.m.Z...d.d.l.
@@ -903,530 +903,535 @@
 00003860: 6401 a102 5300 2902 4eda 0370 6970 729b  d...S.).N..pipr.
 00003870: 0000 0072 2200 0000 7215 0000 0072 1500  ...r"...r....r..
 00003880: 0000 7216 0000 00da 1170 6174 685f 7665  ..r......path_ve
 00003890: 6e76 5f62 696e 5f70 6970 e301 0000 7302  nv_bin_pip....s.
 000038a0: 0000 0000 027a 1c52 6570 6f43 6f6e 6669  .....z.RepoConfi
 000038b0: 672e 7061 7468 5f76 656e 765f 6269 6e5f  g.path_venv_bin_
 000038c0: 7069 7063 0100 0000 0000 0000 0000 0000  pipc............
-000038d0: 0100 0000 0400 0000 4300 0000 7310 0000  ........C...s...
-000038e0: 0074 006a 01a0 027c 006a 0364 01a1 0253  .t.j...|.j.d...S
-000038f0: 0029 024e 5a08 6163 7469 7661 7465 729b  .).NZ.activater.
-00003900: 0000 0072 2200 0000 7215 0000 0072 1500  ...r"...r....r..
-00003910: 0000 7216 0000 00da 1670 6174 685f 7665  ..r......path_ve
-00003920: 6e76 5f62 696e 5f61 6374 6976 6174 65e7  nv_bin_activate.
-00003930: 0100 0073 0200 0000 0002 7a21 5265 706f  ...s......z!Repo
-00003940: 436f 6e66 6967 2e70 6174 685f 7665 6e76  Config.path_venv
-00003950: 5f62 696e 5f61 6374 6976 6174 6563 0100  _bin_activatec..
-00003960: 0000 0000 0000 0000 0000 0100 0000 0400  ................
-00003970: 0000 4300 0000 7310 0000 0074 006a 01a0  ..C...s....t.j..
-00003980: 027c 006a 0364 01a1 0253 0029 024e 5a06  .|.j.d...S.).NZ.
-00003990: 7079 7465 7374 729b 0000 0072 2200 0000  pytestr....r"...
-000039a0: 7215 0000 0072 1500 0000 7216 0000 00da  r....r....r.....
-000039b0: 1470 6174 685f 7665 6e76 5f62 696e 5f70  .path_venv_bin_p
-000039c0: 7974 6573 74eb 0100 0073 0200 0000 0002  ytest....s......
-000039d0: 7a1f 5265 706f 436f 6e66 6967 2e70 6174  z.RepoConfig.pat
-000039e0: 685f 7665 6e76 5f62 696e 5f70 7974 6573  h_venv_bin_pytes
-000039f0: 7463 0100 0000 0000 0000 0000 0000 0100  tc..............
-00003a00: 0000 0400 0000 4300 0000 7310 0000 0074  ......C...s....t
-00003a10: 006a 01a0 027c 006a 0364 01a1 0253 0029  .j...|.j.d...S.)
-00003a20: 024e 7a11 7370 6869 6e78 2d71 7569 636b  .Nz.sphinx-quick
-00003a30: 7374 6172 7472 9b00 0000 7222 0000 0072  startr....r"...r
-00003a40: 1500 0000 7215 0000 0072 1600 0000 da1f  ....r....r......
-00003a50: 7061 7468 5f76 656e 765f 6269 6e5f 7370  path_venv_bin_sp
-00003a60: 6869 6e78 5f71 7569 636b 7374 6172 74ef  hinx_quickstart.
-00003a70: 0100 0073 0200 0000 0002 7a2a 5265 706f  ...s......z*Repo
-00003a80: 436f 6e66 6967 2e70 6174 685f 7665 6e76  Config.path_venv
-00003a90: 5f62 696e 5f73 7068 696e 785f 7175 6963  _bin_sphinx_quic
-00003aa0: 6b73 7461 7274 6301 0000 0000 0000 0000  kstartc.........
-00003ab0: 0000 0001 0000 0004 0000 0043 0000 0073  ...........C...s
-00003ac0: 1000 0000 7400 6a01 a002 7c00 6a03 6401  ....t.j...|.j.d.
-00003ad0: a102 5300 2902 4e5a 0574 7769 6e65 729b  ..S.).NZ.twiner.
-00003ae0: 0000 0072 2200 0000 7215 0000 0072 1500  ...r"...r....r..
-00003af0: 0000 7216 0000 00da 1370 6174 685f 7665  ..r......path_ve
-00003b00: 6e76 5f62 696e 5f74 7769 6e65 f301 0000  nv_bin_twine....
-00003b10: 7302 0000 0000 027a 1e52 6570 6f43 6f6e  s......z.RepoCon
-00003b20: 6669 672e 7061 7468 5f76 656e 765f 6269  fig.path_venv_bi
-00003b30: 6e5f 7477 696e 6563 0100 0000 0000 0000  n_twinec........
-00003b40: 0000 0000 0100 0000 0400 0000 4300 0000  ............C...
-00003b50: 7310 0000 0074 006a 01a0 027c 006a 0364  s....t.j...|.j.d
-00003b60: 01a1 0253 0029 024e da03 746f 7872 9b00  ...S.).N..toxr..
-00003b70: 0000 7222 0000 0072 1500 0000 7215 0000  ..r"...r....r...
-00003b80: 0072 1600 0000 da11 7061 7468 5f76 656e  .r......path_ven
-00003b90: 765f 6269 6e5f 746f 78f7 0100 0073 0200  v_bin_tox....s..
-00003ba0: 0000 0002 7a1c 5265 706f 436f 6e66 6967  ....z.RepoConfig
-00003bb0: 2e70 6174 685f 7665 6e76 5f62 696e 5f74  .path_venv_bin_t
-00003bc0: 6f78 6301 0000 0000 0000 0000 0000 0001  oxc.............
-00003bd0: 0000 0004 0000 0043 0000 0073 1000 0000  .......C...s....
-00003be0: 7400 6a01 a002 7c00 6a03 6401 a102 5300  t.j...|.j.d...S.
-00003bf0: 2902 4e5a 076a 7570 7974 6572 729b 0000  ).NZ.jupyterr...
-00003c00: 0072 2200 0000 7215 0000 0072 1500 0000  .r"...r....r....
-00003c10: 7216 0000 00da 1570 6174 685f 7665 6e76  r......path_venv
-00003c20: 5f62 696e 5f6a 7570 7974 6572 fb01 0000  _bin_jupyter....
-00003c30: 7302 0000 0000 027a 2052 6570 6f43 6f6e  s......z RepoCon
-00003c40: 6669 672e 7061 7468 5f76 656e 765f 6269  fig.path_venv_bi
-00003c50: 6e5f 6a75 7079 7465 7263 0100 0000 0000  n_jupyterc......
-00003c60: 0000 0000 0000 0100 0000 0400 0000 4300  ..............C.
-00003c70: 0000 7310 0000 0074 006a 01a0 027c 006a  ..s....t.j...|.j
-00003c80: 0364 01a1 0253 0029 024e 5a07 616e 7369  .d...S.).NZ.ansi
-00003c90: 626c 6572 9b00 0000 7222 0000 0072 1500  bler....r"...r..
-00003ca0: 0000 7215 0000 0072 1600 0000 da15 7061  ..r....r......pa
-00003cb0: 7468 5f76 656e 765f 6269 6e5f 616e 7369  th_venv_bin_ansi
-00003cc0: 626c 65ff 0100 0073 0200 0000 0002 7a20  ble....s......z 
-00003cd0: 5265 706f 436f 6e66 6967 2e70 6174 685f  RepoConfig.path_
-00003ce0: 7665 6e76 5f62 696e 5f61 6e73 6962 6c65  venv_bin_ansible
-00003cf0: 6301 0000 0000 0000 0000 0000 0001 0000  c...............
-00003d00: 0004 0000 0043 0000 0073 1000 0000 7400  .....C...s....t.
-00003d10: 6a01 a002 7c00 6a03 6401 a102 5300 2902  j...|.j.d...S.).
-00003d20: 4eda 0361 7773 729b 0000 0072 2200 0000  N..awsr....r"...
-00003d30: 7215 0000 0072 1500 0000 7216 0000 00da  r....r....r.....
-00003d40: 1170 6174 685f 7665 6e76 5f62 696e 5f61  .path_venv_bin_a
-00003d50: 7773 0302 0000 7302 0000 0000 027a 1c52  ws....s......z.R
-00003d60: 6570 6f43 6f6e 6669 672e 7061 7468 5f76  epoConfig.path_v
-00003d70: 656e 765f 6269 6e5f 6177 7363 0100 0000  env_bin_awsc....
-00003d80: 0000 0000 0000 0000 0100 0000 0400 0000  ................
-00003d90: 4300 0000 7310 0000 0074 006a 01a0 027c  C...s....t.j...|
-00003da0: 006a 0364 01a1 0253 0029 024e 5a07 6368  .j.d...S.).NZ.ch
-00003db0: 616c 6963 6572 9b00 0000 7222 0000 0072  alicer....r"...r
-00003dc0: 1500 0000 7215 0000 0072 1600 0000 da15  ....r....r......
-00003dd0: 7061 7468 5f76 656e 765f 6269 6e5f 6368  path_venv_bin_ch
-00003de0: 616c 6963 6507 0200 0073 0200 0000 0002  alice....s......
-00003df0: 7a20 5265 706f 436f 6e66 6967 2e70 6174  z RepoConfig.pat
-00003e00: 685f 7665 6e76 5f62 696e 5f63 6861 6c69  h_venv_bin_chali
-00003e10: 6365 6301 0000 0000 0000 0000 0000 0001  cec.............
-00003e20: 0000 0004 0000 0043 0000 0073 1000 0000  .......C...s....
-00003e30: 7400 6a01 a002 7c00 6a03 6401 a102 5300  t.j...|.j.d...S.
-00003e40: 2902 4e5a 0566 6c61 736b 729b 0000 0072  ).NZ.flaskr....r
-00003e50: 2200 0000 7215 0000 0072 1500 0000 7216  "...r....r....r.
-00003e60: 0000 00da 1370 6174 685f 7665 6e76 5f62  .....path_venv_b
-00003e70: 696e 5f66 6c61 736b 0b02 0000 7302 0000  in_flask....s...
-00003e80: 0000 027a 1e52 6570 6f43 6f6e 6669 672e  ...z.RepoConfig.
-00003e90: 7061 7468 5f76 656e 765f 6269 6e5f 666c  path_venv_bin_fl
-00003ea0: 6173 6b63 0100 0000 0000 0000 0000 0000  askc............
-00003eb0: 0100 0000 0400 0000 4300 0000 7310 0000  ........C...s...
-00003ec0: 0074 006a 01a0 027c 006a 0364 01a1 0253  .t.j...|.j.d...S
-00003ed0: 0029 024e 5a09 636f 6e66 6967 6972 6c72  .).NZ.configirlr
-00003ee0: 9b00 0000 7222 0000 0072 1500 0000 7215  ....r"...r....r.
-00003ef0: 0000 0072 1600 0000 da17 7061 7468 5f76  ...r......path_v
-00003f00: 656e 765f 6269 6e5f 636f 6e66 6967 6972  env_bin_configir
-00003f10: 6c0f 0200 0073 0200 0000 0002 7a22 5265  l....s......z"Re
-00003f20: 706f 436f 6e66 6967 2e70 6174 685f 7665  poConfig.path_ve
-00003f30: 6e76 5f62 696e 5f63 6f6e 6669 6769 726c  nv_bin_configirl
-00003f40: 6301 0000 0000 0000 0000 0000 0002 0000  c...............
-00003f50: 0002 0000 0043 0000 0073 1e00 0000 7c00  .....C...s....|.
-00003f60: 6a00 a001 a100 7d01 7c01 6400 6b08 7216  j.....}.|.d.k.r.
-00003f70: 6401 5300 7c01 5300 6400 5300 a902 4eda  d.S.|.S.d.S...N.
-00003f80: 0029 0272 2e00 0000 720f 0000 0029 0272  .).r....r....).r
-00003f90: 1200 0000 da14 646f 635f 686f 7374 5f61  ......doc_host_a
-00003fa0: 7773 5f70 726f 6669 6c65 7215 0000 0072  ws_profiler....r
-00003fb0: 1500 0000 7216 0000 00da 1c61 7773 5f63  ....r......aws_c
-00003fc0: 6c69 5f70 726f 6669 6c65 5f61 7267 5f64  li_profile_arg_d
-00003fd0: 6f63 5f68 6f73 7414 0200 0073 0800 0000  oc_host....s....
-00003fe0: 0002 0a01 0801 0402 7a27 5265 706f 436f  ........z'RepoCo
-00003ff0: 6e66 6967 2e61 7773 5f63 6c69 5f70 726f  nfig.aws_cli_pro
-00004000: 6669 6c65 5f61 7267 5f64 6f63 5f68 6f73  file_arg_doc_hos
-00004010: 7463 0100 0000 0000 0000 0000 0000 0200  tc..............
-00004020: 0000 0200 0000 4300 0000 731e 0000 007c  ......C...s....|
-00004030: 006a 00a0 01a1 007d 017c 0164 006b 0872  .j.....}.|.d.k.r
-00004040: 1664 0153 007c 0153 0064 0053 0072 ac00  .d.S.|.S.d.S.r..
-00004050: 0000 2902 7234 0000 0072 0f00 0000 2902  ..).r4...r....).
-00004060: 7212 0000 005a 1d61 7773 5f6c 616d 6264  r....Z.aws_lambd
-00004070: 615f 6465 706c 6f79 5f61 7773 5f70 726f  a_deploy_aws_pro
-00004080: 6669 6c65 7215 0000 0072 1500 0000 7216  filer....r....r.
-00004090: 0000 00da 2161 7773 5f63 6c69 5f70 726f  ....!aws_cli_pro
-000040a0: 6669 6c65 5f61 7267 5f6c 616d 6264 615f  file_arg_lambda_
-000040b0: 6465 706c 6f79 1c02 0000 7308 0000 0000  deploy....s.....
-000040c0: 020a 0108 0104 027a 2c52 6570 6f43 6f6e  .......z,RepoCon
-000040d0: 6669 672e 6177 735f 636c 695f 7072 6f66  fig.aws_cli_prof
-000040e0: 696c 655f 6172 675f 6c61 6d62 6461 5f64  ile_arg_lambda_d
-000040f0: 6570 6c6f 7963 0100 0000 0000 0000 0000  eployc..........
-00004100: 0000 0100 0000 0400 0000 4300 0000 7310  ..........C...s.
-00004110: 0000 0074 006a 01a0 027c 006a 0364 01a1  ...t.j...|.j.d..
-00004120: 0253 0029 024e da06 6c61 6d62 6461 2904  .S.).N..lambda).
-00004130: 7239 0000 0072 3c00 0000 723e 0000 0072  r9...r<...r>...r
-00004140: 6500 0000 7222 0000 0072 1500 0000 7215  e...r"...r....r.
-00004150: 0000 0072 1600 0000 da10 6469 725f 6c61  ...r......dir_la
-00004160: 6d62 6461 5f62 7569 6c64 2802 0000 7302  mbda_build(...s.
-00004170: 0000 0000 027a 1b52 6570 6f43 6f6e 6669  .....z.RepoConfi
-00004180: 672e 6469 725f 6c61 6d62 6461 5f62 7569  g.dir_lambda_bui
-00004190: 6c64 6301 0000 0000 0000 0000 0000 0001  ldc.............
-000041a0: 0000 0004 0000 0043 0000 0073 1000 0000  .......C...s....
-000041b0: 7400 6a01 a002 7c00 6a03 6401 a102 5300  t.j...|.j.d...S.
-000041c0: 2902 4e7a 0a73 6f75 7263 652e 7a69 70a9  ).Nz.source.zip.
-000041d0: 0472 3900 0000 723c 0000 0072 3e00 0000  .r9...r<...r>...
-000041e0: 72b2 0000 0072 2200 0000 7215 0000 0072  r....r"...r....r
-000041f0: 1500 0000 7216 0000 00da 1870 6174 685f  ....r......path_
-00004200: 6c61 6d62 6461 5f62 7569 6c64 5f73 6f75  lambda_build_sou
-00004210: 7263 652c 0200 0073 0200 0000 0002 7a23  rce,...s......z#
-00004220: 5265 706f 436f 6e66 6967 2e70 6174 685f  RepoConfig.path_
-00004230: 6c61 6d62 6461 5f62 7569 6c64 5f73 6f75  lambda_build_sou
-00004240: 7263 6563 0100 0000 0000 0000 0000 0000  rcec............
-00004250: 0100 0000 0400 0000 4300 0000 7310 0000  ........C...s...
-00004260: 0074 006a 01a0 027c 006a 0364 01a1 0253  .t.j...|.j.d...S
-00004270: 0029 024e 7a09 6c61 7965 722e 7a69 7072  .).Nz.layer.zipr
-00004280: b300 0000 7222 0000 0072 1500 0000 7215  ....r"...r....r.
-00004290: 0000 0072 1600 0000 da17 7061 7468 5f6c  ...r......path_l
-000042a0: 616d 6264 615f 6275 696c 645f 6c61 7965  ambda_build_laye
-000042b0: 7230 0200 0073 0200 0000 0002 7a22 5265  r0...s......z"Re
-000042c0: 706f 436f 6e66 6967 2e70 6174 685f 6c61  poConfig.path_la
-000042d0: 6d62 6461 5f62 7569 6c64 5f6c 6179 6572  mbda_build_layer
-000042e0: 6301 0000 0000 0000 0000 0000 0001 0000  c...............
-000042f0: 0004 0000 0043 0000 0073 1000 0000 7400  .....C...s....t.
-00004300: 6a01 a002 7c00 6a03 6401 a102 5300 2902  j...|.j.d...S.).
-00004310: 4e7a 0e64 6570 6c6f 792d 706b 672e 7a69  Nz.deploy-pkg.zi
-00004320: 7072 b300 0000 7222 0000 0072 1500 0000  pr....r"...r....
-00004330: 7215 0000 0072 1600 0000 da20 7061 7468  r....r..... path
-00004340: 5f6c 616d 6264 615f 6275 696c 645f 6465  _lambda_build_de
-00004350: 706c 6f79 5f70 6163 6b61 6765 3402 0000  ploy_package4...
-00004360: 7302 0000 0000 027a 2b52 6570 6f43 6f6e  s......z+RepoCon
-00004370: 6669 672e 7061 7468 5f6c 616d 6264 615f  fig.path_lambda_
-00004380: 6275 696c 645f 6465 706c 6f79 5f70 6163  build_deploy_pac
-00004390: 6b61 6765 6301 0000 0000 0000 0000 0000  kagec...........
-000043a0: 0001 0000 0004 0000 0043 0000 0073 1600  .........C...s..
-000043b0: 0000 7400 6401 7c00 6a01 a002 a100 6702  ..t.d.|.j.....g.
-000043c0: 6402 6403 8d02 5300 2904 7a2d 0a20 2020  d.d...S.).z-.   
-000043d0: 2020 2020 2065 7861 6d70 6c65 3a20 6c61       example: la
-000043e0: 6d62 6461 2f6d 795f 7061 636b 6167 652f  mbda/my_package/
-000043f0: 0a20 2020 2020 2020 2072 b100 0000 54a9  .        r....T.
-00004400: 02da 0570 6172 7473 da06 6973 5f64 6972  ...parts..is_dir
-00004410: 2903 7208 0000 0072 2100 0000 720f 0000  ).r....r!...r...
-00004420: 0072 2200 0000 7215 0000 0072 1500 0000  .r"...r....r....
-00004430: 7216 0000 00da 1873 335f 6b65 795f 6c61  r......s3_key_la
-00004440: 6d62 6461 5f64 6570 6c6f 795f 6469 7239  mbda_deploy_dir9
-00004450: 0200 0073 0c00 0000 0005 0202 0201 08fe  ...s............
-00004460: 0204 02fb 7a23 5265 706f 436f 6e66 6967  ....z#RepoConfig
-00004470: 2e73 335f 6b65 795f 6c61 6d62 6461 5f64  .s3_key_lambda_d
-00004480: 6570 6c6f 795f 6469 7263 0100 0000 0000  eploy_dirc......
-00004490: 0000 0000 0000 0100 0000 0400 0000 4300  ..............C.
-000044a0: 0000 7314 0000 0074 007c 006a 017c 006a  ..s....t.|.j.|.j
-000044b0: 0267 0264 0164 028d 0253 0029 037a 330a  .g.d.d...S.).z3.
-000044c0: 2020 2020 2020 2020 6578 616d 706c 653a          example:
-000044d0: 206c 616d 6264 612f 6d79 5f70 6163 6b61   lambda/my_packa
-000044e0: 6765 2f30 2e30 2e31 2f0a 2020 2020 2020  ge/0.0.1/.      
-000044f0: 2020 5472 b700 0000 2903 7208 0000 0072    Tr....).r....r
-00004500: ba00 0000 725f 0000 0072 2200 0000 7215  ....r_...r"...r.
-00004510: 0000 0072 1500 0000 7216 0000 00da 2273  ...r....r....."s
-00004520: 335f 6b65 795f 6c61 6d62 6461 5f64 6570  3_key_lambda_dep
-00004530: 6c6f 795f 7665 7273 696f 6e65 645f 6469  loy_versioned_di
-00004540: 7246 0200 0073 0c00 0000 0005 0202 0401  rF...s..........
-00004550: 04fe 0204 02fb 7a2d 5265 706f 436f 6e66  ......z-RepoConf
-00004560: 6967 2e73 335f 6b65 795f 6c61 6d62 6461  ig.s3_key_lambda
-00004570: 5f64 6570 6c6f 795f 7665 7273 696f 6e65  _deploy_versione
-00004580: 645f 6469 7263 0100 0000 0000 0000 0000  d_dirc..........
-00004590: 0000 0100 0000 0400 0000 4300 0000 731c  ..........C...s.
-000045a0: 0000 007c 00a0 00a1 0001 0074 017c 006a  ...|.......t.|.j
-000045b0: 02a0 03a1 007c 006a 0464 018d 0253 0029  .....|.j.d...S.)
-000045c0: 027a 3f0a 2020 2020 2020 2020 6578 616d  .z?.        exam
-000045d0: 706c 653a 2073 333a 2f2f 6275 636b 6574  ple: s3://bucket
-000045e0: 2f6c 616d 6264 612f 6d79 5f70 6163 6b61  /lambda/my_packa
-000045f0: 6765 2f30 2e30 2e31 2f0a 2020 2020 2020  ge/0.0.1/.      
-00004600: 2020 a902 7281 0000 00da 036b 6579 2905    ..r......key).
-00004610: 7233 0000 0072 0700 0000 7231 0000 0072  r3...r....r1...r
-00004620: 0f00 0000 72bb 0000 0072 2200 0000 7215  ....r....r"...r.
-00004630: 0000 0072 1500 0000 7216 0000 00da 2273  ...r....r....."s
-00004640: 335f 7572 695f 6c61 6d62 6461 5f64 6570  3_uri_lambda_dep
-00004650: 6c6f 795f 7665 7273 696f 6e65 645f 6469  loy_versioned_di
-00004660: 7253 0200 0073 0a00 0000 0005 0801 0201  rS...s..........
-00004670: 0801 04fe 7a2d 5265 706f 436f 6e66 6967  ....z-RepoConfig
-00004680: 2e73 335f 7572 695f 6c61 6d62 6461 5f64  .s3_uri_lambda_d
-00004690: 6570 6c6f 795f 7665 7273 696f 6e65 645f  eploy_versioned_
-000046a0: 6469 7263 0100 0000 0000 0000 0000 0000  dirc............
-000046b0: 0100 0000 0400 0000 4300 0000 7312 0000  ........C...s...
-000046c0: 0074 007c 006a 0164 0167 0264 0264 038d  .t.|.j.d.g.d.d..
-000046d0: 0253 0029 047a 3a0a 2020 2020 2020 2020  .S.).z:.        
-000046e0: 6578 616d 706c 653a 206c 616d 6264 612f  example: lambda/
-000046f0: 6d79 5f70 6163 6b61 6765 2f30 2e30 2e31  my_package/0.0.1
-00004700: 2f73 6f75 7263 652f 0a20 2020 2020 2020  /source/.       
-00004710: 2072 7600 0000 5472 b700 0000 a902 7208   rv...Tr......r.
-00004720: 0000 0072 bb00 0000 7222 0000 0072 1500  ...r....r"...r..
-00004730: 0000 7215 0000 0072 1600 0000 da29 7333  ..r....r.....)s3
-00004740: 5f6b 6579 5f6c 616d 6264 615f 6465 706c  _key_lambda_depl
-00004750: 6f79 5f76 6572 7369 6f6e 6564 5f73 6f75  oy_versioned_sou
-00004760: 7263 655f 6469 725f 0200 0073 0c00 0000  rce_dir_...s....
-00004770: 0005 0202 0401 02fe 0204 02fb 7a34 5265  ............z4Re
-00004780: 706f 436f 6e66 6967 2e73 335f 6b65 795f  poConfig.s3_key_
-00004790: 6c61 6d62 6461 5f64 6570 6c6f 795f 7665  lambda_deploy_ve
-000047a0: 7273 696f 6e65 645f 736f 7572 6365 5f64  rsioned_source_d
-000047b0: 6972 6301 0000 0000 0000 0000 0000 0001  irc.............
-000047c0: 0000 0004 0000 0043 0000 0073 1c00 0000  .......C...s....
-000047d0: 7c00 a000 a100 0100 7401 7c00 6a02 a003  |.......t.|.j...
-000047e0: a100 7c00 6a04 6401 8d02 5300 2902 7a46  ..|.j.d...S.).zF
-000047f0: 0a20 2020 2020 2020 2065 7861 6d70 6c65  .        example
-00004800: 3a20 7333 3a2f 2f62 7563 6b65 742f 6c61  : s3://bucket/la
-00004810: 6d62 6461 2f6d 795f 7061 636b 6167 652f  mbda/my_package/
-00004820: 302e 302e 312f 736f 7572 6365 2f0a 2020  0.0.1/source/.  
-00004830: 2020 2020 2020 72bc 0000 0029 0572 3300        r....).r3.
-00004840: 0000 7207 0000 0072 3100 0000 720f 0000  ..r....r1...r...
-00004850: 0072 c000 0000 7222 0000 0072 1500 0000  .r....r"...r....
-00004860: 7215 0000 0072 1600 0000 da29 7333 5f75  r....r.....)s3_u
-00004870: 7269 5f6c 616d 6264 615f 6465 706c 6f79  ri_lambda_deploy
-00004880: 5f76 6572 7369 6f6e 6564 5f73 6f75 7263  _versioned_sourc
-00004890: 655f 6469 726c 0200 0073 0a00 0000 0005  e_dirl...s......
-000048a0: 0801 0201 0801 04fe 7a34 5265 706f 436f  ........z4RepoCo
-000048b0: 6e66 6967 2e73 335f 7572 695f 6c61 6d62  nfig.s3_uri_lamb
-000048c0: 6461 5f64 6570 6c6f 795f 7665 7273 696f  da_deploy_versio
-000048d0: 6e65 645f 736f 7572 6365 5f64 6972 6301  ned_source_dirc.
-000048e0: 0000 0000 0000 0000 0000 0001 0000 0004  ................
-000048f0: 0000 0043 0000 0073 1200 0000 7400 7c00  ...C...s....t.|.
-00004900: 6a01 6401 6702 6402 6403 8d02 5300 2904  j.d.g.d.d...S.).
-00004910: 7a39 0a20 2020 2020 2020 2065 7861 6d70  z9.        examp
-00004920: 6c65 3a20 6c61 6d62 6461 2f6d 795f 7061  le: lambda/my_pa
-00004930: 636b 6167 652f 302e 302e 312f 6c61 7965  ckage/0.0.1/laye
-00004940: 722f 0a20 2020 2020 2020 20da 056c 6179  r/.        ..lay
-00004950: 6572 5472 b700 0000 72bf 0000 0072 2200  erTr....r....r".
-00004960: 0000 7215 0000 0072 1500 0000 7216 0000  ..r....r....r...
-00004970: 00da 2873 335f 6b65 795f 6c61 6d62 6461  ..(s3_key_lambda
-00004980: 5f64 6570 6c6f 795f 7665 7273 696f 6e65  _deploy_versione
-00004990: 645f 6c61 7965 725f 6469 7278 0200 0073  d_layer_dirx...s
-000049a0: 0c00 0000 0005 0202 0401 02fe 0204 02fb  ................
-000049b0: 7a33 5265 706f 436f 6e66 6967 2e73 335f  z3RepoConfig.s3_
-000049c0: 6b65 795f 6c61 6d62 6461 5f64 6570 6c6f  key_lambda_deplo
-000049d0: 795f 7665 7273 696f 6e65 645f 6c61 7965  y_versioned_laye
-000049e0: 725f 6469 7263 0100 0000 0000 0000 0000  r_dirc..........
-000049f0: 0000 0100 0000 0400 0000 4300 0000 731c  ..........C...s.
-00004a00: 0000 007c 00a0 00a1 0001 0074 017c 006a  ...|.......t.|.j
-00004a10: 02a0 03a1 007c 006a 0464 018d 0253 0029  .....|.j.d...S.)
-00004a20: 027a 450a 2020 2020 2020 2020 6578 616d  .zE.        exam
-00004a30: 706c 653a 2073 333a 2f2f 6275 636b 6574  ple: s3://bucket
-00004a40: 2f6c 616d 6264 612f 6d79 5f70 6163 6b61  /lambda/my_packa
-00004a50: 6765 2f30 2e30 2e31 2f6c 6179 6572 2f0a  ge/0.0.1/layer/.
-00004a60: 2020 2020 2020 2020 72bc 0000 0029 0572          r....).r
-00004a70: 3300 0000 7207 0000 0072 3100 0000 720f  3...r....r1...r.
-00004a80: 0000 0072 c300 0000 7222 0000 0072 1500  ...r....r"...r..
-00004a90: 0000 7215 0000 0072 1600 0000 da28 7333  ..r....r.....(s3
-00004aa0: 5f75 7269 5f6c 616d 6264 615f 6465 706c  _uri_lambda_depl
-00004ab0: 6f79 5f76 6572 7369 6f6e 6564 5f6c 6179  oy_versioned_lay
-00004ac0: 6572 5f64 6972 8502 0000 730a 0000 0000  er_dir....s.....
-00004ad0: 0508 0102 0108 0104 fe7a 3352 6570 6f43  .........z3RepoC
-00004ae0: 6f6e 6669 672e 7333 5f75 7269 5f6c 616d  onfig.s3_uri_lam
-00004af0: 6264 615f 6465 706c 6f79 5f76 6572 7369  bda_deploy_versi
-00004b00: 6f6e 6564 5f6c 6179 6572 5f64 6972 6301  oned_layer_dirc.
-00004b10: 0000 0000 0000 0000 0000 0001 0000 0004  ................
-00004b20: 0000 0043 0000 0073 1200 0000 7400 7c00  ...C...s....t.|.
-00004b30: 6a01 6401 6702 6402 6403 8d02 5300 2904  j.d.g.d.d...S.).
-00004b40: 7a3e 0a20 2020 2020 2020 2065 7861 6d70  z>.        examp
-00004b50: 6c65 3a20 6c61 6d62 6461 2f6d 795f 7061  le: lambda/my_pa
-00004b60: 636b 6167 652f 302e 302e 312f 6465 706c  ckage/0.0.1/depl
-00004b70: 6f79 2d70 6b67 2f0a 2020 2020 2020 2020  oy-pkg/.        
-00004b80: 7a0a 6465 706c 6f79 2d70 6b67 5472 b700  z.deploy-pkgTr..
-00004b90: 0000 72bf 0000 0072 2200 0000 7215 0000  ..r....r"...r...
-00004ba0: 0072 1500 0000 7216 0000 00da 2d73 335f  .r....r.....-s3_
-00004bb0: 6b65 795f 6c61 6d62 6461 5f64 6570 6c6f  key_lambda_deplo
-00004bc0: 795f 7665 7273 696f 6e65 645f 6465 706c  y_versioned_depl
-00004bd0: 6f79 5f70 6b67 5f64 6972 9102 0000 730c  oy_pkg_dir....s.
-00004be0: 0000 0000 0502 0204 0102 fe02 0402 fb7a  ...............z
-00004bf0: 3852 6570 6f43 6f6e 6669 672e 7333 5f6b  8RepoConfig.s3_k
-00004c00: 6579 5f6c 616d 6264 615f 6465 706c 6f79  ey_lambda_deploy
-00004c10: 5f76 6572 7369 6f6e 6564 5f64 6570 6c6f  _versioned_deplo
-00004c20: 795f 706b 675f 6469 7263 0100 0000 0000  y_pkg_dirc......
-00004c30: 0000 0000 0000 0100 0000 0400 0000 4300  ..............C.
-00004c40: 0000 731c 0000 007c 00a0 00a1 0001 0074  ..s....|.......t
-00004c50: 017c 006a 02a0 03a1 007c 006a 0464 018d  .|.j.....|.j.d..
-00004c60: 0253 0029 027a 4a0a 2020 2020 2020 2020  .S.).zJ.        
-00004c70: 6578 616d 706c 653a 2073 333a 2f2f 6275  example: s3://bu
-00004c80: 636b 6574 2f6c 616d 6264 612f 6d79 5f70  cket/lambda/my_p
-00004c90: 6163 6b61 6765 2f30 2e30 2e31 2f64 6570  ackage/0.0.1/dep
-00004ca0: 6c6f 792d 706b 672f 0a20 2020 2020 2020  loy-pkg/.       
-00004cb0: 2072 bc00 0000 2905 7233 0000 0072 0700   r....).r3...r..
-00004cc0: 0000 7231 0000 0072 0f00 0000 72c5 0000  ..r1...r....r...
-00004cd0: 0072 2200 0000 7215 0000 0072 1500 0000  .r"...r....r....
-00004ce0: 7216 0000 00da 2d73 335f 7572 695f 6c61  r.....-s3_uri_la
-00004cf0: 6d62 6461 5f64 6570 6c6f 795f 7665 7273  mbda_deploy_vers
-00004d00: 696f 6e65 645f 6465 706c 6f79 5f70 6b67  ioned_deploy_pkg
-00004d10: 5f64 6972 9e02 0000 730a 0000 0000 0508  _dir....s.......
-00004d20: 0102 0108 0104 fe7a 3852 6570 6f43 6f6e  .......z8RepoCon
-00004d30: 6669 672e 7333 5f75 7269 5f6c 616d 6264  fig.s3_uri_lambd
-00004d40: 615f 6465 706c 6f79 5f76 6572 7369 6f6e  a_deploy_version
-00004d50: 6564 5f64 6570 6c6f 795f 706b 675f 6469  ed_deploy_pkg_di
-00004d60: 7263 0100 0000 0000 0000 0000 0000 0100  rc..............
-00004d70: 0000 0200 0000 4300 0000 730a 0000 007c  ......C...s....|
-00004d80: 006a 00a0 01a1 0053 0072 1f00 0000 7220  .j.....S.r....r 
-00004d90: 0000 0072 2200 0000 7215 0000 0072 1500  ...r"...r....r..
-00004da0: 0000 7216 0000 00da 1561 7773 5f6c 616d  ..r......aws_lam
-00004db0: 6264 615f 6c61 7965 725f 6e61 6d65 a902  bda_layer_name..
-00004dc0: 0000 7302 0000 0000 027a 2052 6570 6f43  ..s......z RepoC
-00004dd0: 6f6e 6669 672e 6177 735f 6c61 6d62 6461  onfig.aws_lambda
-00004de0: 5f6c 6179 6572 5f6e 616d 6563 0100 0000  _layer_namec....
-00004df0: 0000 0000 0000 0000 0100 0000 0300 0000  ................
-00004e00: 4300 0000 730e 0000 0064 016a 007c 006a  C...s....d.j.|.j
-00004e10: 0164 028d 0153 0029 034e 7a40 6874 7470  .d...S.).Nz@http
-00004e20: 733a 2f2f 636f 6e73 6f6c 652e 6177 732e  s://console.aws.
-00004e30: 616d 617a 6f6e 2e63 6f6d 2f6c 616d 6264  amazon.com/lambd
-00004e40: 612f 686f 6d65 3f23 2f6c 6179 6572 732f  a/home?#/layers/
-00004e50: 7b6c 6179 6572 5f6e 616d 657d 2901 5a0a  {layer_name}).Z.
-00004e60: 6c61 7965 725f 6e61 6d65 2902 7211 0000  layer_name).r...
-00004e70: 0072 c700 0000 7222 0000 0072 1500 0000  .r....r"...r....
-00004e80: 7215 0000 0072 1600 0000 da18 7572 6c5f  r....r......url_
-00004e90: 6c61 6d62 6461 5f6c 6179 6572 5f63 6f6e  lambda_layer_con
-00004ea0: 736f 6c65 ad02 0000 7306 0000 0000 0204  sole....s.......
-00004eb0: 0104 ff7a 2352 6570 6f43 6f6e 6669 672e  ...z#RepoConfig.
-00004ec0: 7572 6c5f 6c61 6d62 6461 5f6c 6179 6572  url_lambda_layer
-00004ed0: 5f63 6f6e 736f 6c65 6301 0000 0000 0000  _consolec.......
-00004ee0: 0000 0000 0001 0000 0004 0000 0043 0000  .............C..
-00004ef0: 0073 1000 0000 7400 6a01 a002 7c00 6a03  .s....t.j...|.j.
-00004f00: 6401 a102 5300 2902 7a39 0a20 2020 2020  d...S.).z9.     
-00004f10: 2020 2065 7861 6d70 6c65 3a20 247b 6469     example: ${di
-00004f20: 725f 7072 6f6a 6563 745f 726f 6f74 7d2f  r_project_root}/
-00004f30: 6c61 6d62 6461 5f61 7070 0a20 2020 2020  lambda_app.     
-00004f40: 2020 205a 0a6c 616d 6264 615f 6170 7072     Z.lambda_appr
-00004f50: 5700 0000 7222 0000 0072 1500 0000 7215  W...r"...r....r.
-00004f60: 0000 0072 1600 0000 da0e 6469 725f 6c61  ...r......dir_la
-00004f70: 6d62 6461 5f61 7070 b502 0000 7302 0000  mbda_app....s...
-00004f80: 0000 057a 1952 6570 6f43 6f6e 6669 672e  ...z.RepoConfig.
-00004f90: 6469 725f 6c61 6d62 6461 5f61 7070 6301  dir_lambda_appc.
-00004fa0: 0000 0000 0000 0000 0000 0001 0000 0004  ................
-00004fb0: 0000 0043 0000 0073 1000 0000 7400 6a01  ...C...s....t.j.
-00004fc0: a002 7c00 6a03 6401 a102 5300 2902 7a42  ..|.j.d...S.).zB
-00004fd0: 0a20 2020 2020 2020 2065 7861 6d70 6c65  .        example
-00004fe0: 3a20 247b 6469 725f 7072 6f6a 6563 745f  : ${dir_project_
-00004ff0: 726f 6f74 7d2f 6c61 6d62 6461 5f61 7070  root}/lambda_app
-00005000: 2f2e 6368 616c 6963 650a 2020 2020 2020  /.chalice.      
-00005010: 2020 7a08 2e63 6861 6c69 6365 a904 7239    z..chalice..r9
-00005020: 0000 0072 3c00 0000 723e 0000 0072 c900  ...r<...r>...r..
-00005030: 0000 7222 0000 0072 1500 0000 7215 0000  ..r"...r....r...
-00005040: 0072 1600 0000 da0f 6469 725f 6177 735f  .r......dir_aws_
-00005050: 6368 616c 6963 65bc 0200 0073 0200 0000  chalice....s....
-00005060: 0005 7a1a 5265 706f 436f 6e66 6967 2e64  ..z.RepoConfig.d
-00005070: 6972 5f61 7773 5f63 6861 6c69 6365 6301  ir_aws_chalicec.
-00005080: 0000 0000 0000 0000 0000 0001 0000 0004  ................
-00005090: 0000 0043 0000 0073 1000 0000 7400 6a01  ...C...s....t.j.
-000050a0: a002 7c00 6a03 6401 a102 5300 2902 7a4e  ..|.j.d...S.).zN
-000050b0: 0a20 2020 2020 2020 2065 7861 6d70 6c65  .        example
-000050c0: 3a20 247b 6469 725f 7072 6f6a 6563 745f  : ${dir_project_
-000050d0: 726f 6f74 7d2f 6c61 6d62 6461 5f61 7070  root}/lambda_app
-000050e0: 2f2e 6368 616c 6963 652f 636f 6e66 6967  /.chalice/config
-000050f0: 2e6a 736f 6e0a 2020 2020 2020 2020 7a0b  .json.        z.
-00005100: 636f 6e66 6967 2e6a 736f 6ea9 0472 3900  config.json..r9.
-00005110: 0000 723c 0000 0072 3e00 0000 72cb 0000  ..r<...r>...r...
-00005120: 0072 2200 0000 7215 0000 0072 1500 0000  .r"...r....r....
-00005130: 7216 0000 00da 1c70 6174 685f 6177 735f  r......path_aws_
-00005140: 6368 616c 6963 655f 636f 6e66 6967 5f6a  chalice_config_j
-00005150: 736f 6ec3 0200 0073 0200 0000 0005 7a27  son....s......z'
-00005160: 5265 706f 436f 6e66 6967 2e70 6174 685f  RepoConfig.path_
-00005170: 6177 735f 6368 616c 6963 655f 636f 6e66  aws_chalice_conf
-00005180: 6967 5f6a 736f 6e63 0100 0000 0000 0000  ig_jsonc........
-00005190: 0000 0000 0100 0000 0400 0000 4300 0000  ............C...
-000051a0: 7310 0000 0074 006a 01a0 027c 006a 0364  s....t.j...|.j.d
-000051b0: 01a1 0253 0029 027a 400a 2020 2020 2020  ...S.).z@.      
-000051c0: 2020 6578 616d 706c 653a 2024 7b64 6972    example: ${dir
-000051d0: 5f70 726f 6a65 6374 5f72 6f6f 747d 2f6c  _project_root}/l
-000051e0: 616d 6264 615f 6170 702f 6170 702e 7079  ambda_app/app.py
-000051f0: 0a20 2020 2020 2020 207a 0661 7070 2e70  .        z.app.p
-00005200: 7972 ca00 0000 7222 0000 0072 1500 0000  yr....r"...r....
-00005210: 7215 0000 0072 1600 0000 da17 7061 7468  r....r......path
-00005220: 5f61 7773 5f63 6861 6c69 6365 5f61 7070  _aws_chalice_app
-00005230: 5f70 79ca 0200 0073 0200 0000 0005 7a22  _py....s......z"
-00005240: 5265 706f 436f 6e66 6967 2e70 6174 685f  RepoConfig.path_
-00005250: 6177 735f 6368 616c 6963 655f 6170 705f  aws_chalice_app_
-00005260: 7079 6301 0000 0000 0000 0000 0000 0001  pyc.............
-00005270: 0000 0004 0000 0043 0000 0073 1000 0000  .......C...s....
-00005280: 7400 6a01 a002 7c00 6a03 6401 a102 5300  t.j...|.j.d...S.
-00005290: 2902 7a40 0a20 2020 2020 2020 2065 7861  ).z@.        exa
-000052a0: 6d70 6c65 3a20 247b 6469 725f 7072 6f6a  mple: ${dir_proj
-000052b0: 6563 745f 726f 6f74 7d2f 6c61 6d62 6461  ect_root}/lambda
-000052c0: 5f61 7070 2f76 656e 646f 720a 2020 2020  _app/vendor.    
-000052d0: 2020 2020 5a06 7665 6e64 6f72 72ca 0000      Z.vendorr...
-000052e0: 0072 2200 0000 7215 0000 0072 1500 0000  .r"...r....r....
-000052f0: 7216 0000 00da 1664 6972 5f61 7773 5f63  r......dir_aws_c
-00005300: 6861 6c69 6365 5f76 656e 646f 72d1 0200  halice_vendor...
-00005310: 0073 0200 0000 0005 7a21 5265 706f 436f  .s......z!RepoCo
-00005320: 6e66 6967 2e64 6972 5f61 7773 5f63 6861  nfig.dir_aws_cha
-00005330: 6c69 6365 5f76 656e 646f 7263 0100 0000  lice_vendorc....
-00005340: 0000 0000 0000 0000 0100 0000 0500 0000  ................
-00005350: 4300 0000 7316 0000 0074 006a 01a0 027c  C...s....t.j...|
-00005360: 006a 037c 006a 04a0 05a1 00a1 0253 0029  .j.|.j.......S.)
-00005370: 017a 500a 2020 2020 2020 2020 6578 616d  .zP.        exam
-00005380: 706c 653a 2024 7b64 6972 5f70 726f 6a65  ple: ${dir_proje
-00005390: 6374 5f72 6f6f 747d 2f6c 616d 6264 615f  ct_root}/lambda_
-000053a0: 6170 702f 7665 6e64 6f72 2f24 7b70 6163  app/vendor/${pac
-000053b0: 6b61 6765 5f6e 616d 657d 0a20 2020 2020  kage_name}.     
-000053c0: 2020 2029 0672 3900 0000 723c 0000 0072     ).r9...r<...r
-000053d0: 3e00 0000 72cf 0000 0072 2100 0000 720f  >...r....r!...r.
-000053e0: 0000 0072 2200 0000 7215 0000 0072 1500  ...r"...r....r..
-000053f0: 0000 7216 0000 00da 1d64 6972 5f61 7773  ..r......dir_aws
-00005400: 5f63 6861 6c69 6365 5f76 656e 646f 725f  _chalice_vendor_
-00005410: 736f 7572 6365 d802 0000 7308 0000 0000  source....s.....
-00005420: 0506 0104 0108 fe7a 2852 6570 6f43 6f6e  .......z(RepoCon
-00005430: 6669 672e 6469 725f 6177 735f 6368 616c  fig.dir_aws_chal
-00005440: 6963 655f 7665 6e64 6f72 5f73 6f75 7263  ice_vendor_sourc
-00005450: 6563 0100 0000 0000 0000 0000 0000 0100  ec..............
-00005460: 0000 0400 0000 4300 0000 7310 0000 0074  ......C...s....t
-00005470: 006a 01a0 027c 006a 0364 01a1 0253 0029  .j...|.j.d...S.)
-00005480: 027a 4b0a 2020 2020 2020 2020 6578 616d  .zK.        exam
-00005490: 706c 653a 2024 7b64 6972 5f70 726f 6a65  ple: ${dir_proje
-000054a0: 6374 5f72 6f6f 747d 2f6c 616d 6264 615f  ct_root}/lambda_
-000054b0: 6170 702f 2e63 6861 6c69 6365 2f64 6570  app/.chalice/dep
-000054c0: 6c6f 7965 640a 2020 2020 2020 2020 5a08  loyed.        Z.
-000054d0: 6465 706c 6f79 6564 72cc 0000 0072 2200  deployedr....r".
-000054e0: 0000 7215 0000 0072 1500 0000 7216 0000  ..r....r....r...
-000054f0: 00da 1864 6972 5f61 7773 5f63 6861 6c69  ...dir_aws_chali
-00005500: 6365 5f64 6570 6c6f 7965 64e2 0200 0073  ce_deployed....s
-00005510: 0200 0000 0005 7a23 5265 706f 436f 6e66  ......z#RepoConf
-00005520: 6967 2e64 6972 5f61 7773 5f63 6861 6c69  ig.dir_aws_chali
-00005530: 6365 5f64 6570 6c6f 7965 644e 2961 7218  ce_deployedN)ar.
-00005540: 0000 0072 1900 0000 721a 0000 0072 1b00  ...r....r....r..
-00005550: 0000 7205 0000 0072 4100 0000 da06 6765  ..r....rA.....ge
-00005560: 7474 6572 723b 0000 0072 4000 0000 7246  tterr;...r@...rF
-00005570: 0000 0072 5000 0000 728b 0000 0072 5300  ...rP...r....rS.
-00005580: 0000 7255 0000 0072 5400 0000 722b 0000  ..rU...rT...r+..
-00005590: 0072 5600 0000 7258 0000 0072 5900 0000  .rV...rX...rY...
-000055a0: 725a 0000 0072 5f00 0000 7260 0000 0072  rZ...r_...r`...r
-000055b0: 6100 0000 7262 0000 0072 6300 0000 7265  a...rb...rc...re
-000055c0: 0000 0072 6700 0000 7268 0000 0072 6900  ...rg...rh...ri.
-000055d0: 0000 726a 0000 0072 6b00 0000 726c 0000  ..rj...rk...rl..
-000055e0: 0072 6d00 0000 726e 0000 0072 6f00 0000  .rm...rn...ro...
-000055f0: 7270 0000 0072 7100 0000 7273 0000 0072  rp...rq...rs...r
-00005600: 7400 0000 7275 0000 0072 7800 0000 7279  t...ru...rx...ry
-00005610: 0000 0072 7a00 0000 727c 0000 0072 7d00  ...rz...r|...r}.
-00005620: 0000 727e 0000 0072 7f00 0000 7283 0000  ..r~...r....r...
-00005630: 0072 8700 0000 7288 0000 0072 8900 0000  .r....r....r....
-00005640: 728c 0000 0072 8d00 0000 728f 0000 0072  r....r....r....r
-00005650: 9000 0000 7295 0000 0072 9600 0000 7297  ....r....r....r.
-00005660: 0000 0072 9800 0000 729a 0000 0072 9c00  ...r....r....r..
-00005670: 0000 729e 0000 0072 9f00 0000 72a0 0000  ..r....r....r...
-00005680: 0072 a100 0000 72a2 0000 0072 a400 0000  .r....r....r....
-00005690: 72a5 0000 0072 a600 0000 72a8 0000 0072  r....r....r....r
-000056a0: a900 0000 72aa 0000 0072 ab00 0000 72af  ....r....r....r.
-000056b0: 0000 0072 b000 0000 72b2 0000 0072 b400  ...r....r....r..
-000056c0: 0000 72b5 0000 0072 b600 0000 72ba 0000  ..r....r....r...
-000056d0: 0072 bb00 0000 72be 0000 0072 c000 0000  .r....r....r....
-000056e0: 72c1 0000 0072 c300 0000 72c4 0000 0072  r....r....r....r
-000056f0: c500 0000 72c6 0000 0072 c700 0000 72c8  ....r....r....r.
-00005700: 0000 0072 c900 0000 72cb 0000 0072 cd00  ...r....r....r..
-00005710: 0000 72ce 0000 0072 cf00 0000 72d0 0000  ..r....r....r...
-00005720: 0072 d100 0000 7215 0000 0072 1500 0000  .r....r....r....
-00005730: 7215 0000 0072 1600 0000 7237 0000 0066  r....r....r7...f
-00005740: 0000 0073 5e01 0000 0805 0403 0a0f 0401  ...s^...........
-00005750: 0a03 080c 0814 080e 0a0a 0401 0a05 0a02  ................
-00005760: 0401 0a03 0201 0a03 0201 0a03 0201 0a03  ................
-00005770: 0201 0a03 0201 0a08 0201 0a03 0201 0a03  ................
-00005780: 0201 0a03 0201 0a03 0201 0a03 0201 0a03  ................
-00005790: 0201 0a06 0201 0a04 0201 0a03 0201 0a03  ................
-000057a0: 0201 0a03 0201 0a03 0201 0a03 0201 0a03  ................
-000057b0: 0201 0a03 0201 0a03 0201 0a03 0201 0a04  ................
-000057c0: 0201 0a03 0201 0a03 0201 0a03 0201 0a03  ................
+000038d0: 0100 0000 0400 0000 4300 0000 7330 0000  ........C...s0..
+000038e0: 0074 0072 1474 016a 02a0 037c 006a 0464  .t.r.t.j...|.j.d
+000038f0: 01a1 0253 0074 0573 1c74 0672 2c74 016a  ...S.t.s.t.r,t.j
+00003900: 02a0 037c 006a 0464 02a1 0253 0064 0053  ...|.j.d...S.d.S
+00003910: 0029 034e 7a0c 6163 7469 7661 7465 2e62  .).Nz.activate.b
+00003920: 6174 5a08 6163 7469 7661 7465 2907 720a  atZ.activate).r.
+00003930: 0000 0072 3900 0000 723c 0000 0072 3e00  ...r9...r<...r>.
+00003940: 0000 729a 0000 0072 0b00 0000 720c 0000  ..r....r....r...
+00003950: 0072 2200 0000 7215 0000 0072 1500 0000  .r"...r....r....
+00003960: 7216 0000 00da 1670 6174 685f 7665 6e76  r......path_venv
+00003970: 5f62 696e 5f61 6374 6976 6174 65e7 0100  _bin_activate...
+00003980: 0073 0800 0000 0002 0401 1001 0801 7a21  .s............z!
+00003990: 5265 706f 436f 6e66 6967 2e70 6174 685f  RepoConfig.path_
+000039a0: 7665 6e76 5f62 696e 5f61 6374 6976 6174  venv_bin_activat
+000039b0: 6563 0100 0000 0000 0000 0000 0000 0100  ec..............
+000039c0: 0000 0400 0000 4300 0000 7310 0000 0074  ......C...s....t
+000039d0: 006a 01a0 027c 006a 0364 01a1 0253 0029  .j...|.j.d...S.)
+000039e0: 024e 5a06 7079 7465 7374 729b 0000 0072  .NZ.pytestr....r
+000039f0: 2200 0000 7215 0000 0072 1500 0000 7216  "...r....r....r.
+00003a00: 0000 00da 1470 6174 685f 7665 6e76 5f62  .....path_venv_b
+00003a10: 696e 5f70 7974 6573 74ee 0100 0073 0200  in_pytest....s..
+00003a20: 0000 0002 7a1f 5265 706f 436f 6e66 6967  ....z.RepoConfig
+00003a30: 2e70 6174 685f 7665 6e76 5f62 696e 5f70  .path_venv_bin_p
+00003a40: 7974 6573 7463 0100 0000 0000 0000 0000  ytestc..........
+00003a50: 0000 0100 0000 0400 0000 4300 0000 7310  ..........C...s.
+00003a60: 0000 0074 006a 01a0 027c 006a 0364 01a1  ...t.j...|.j.d..
+00003a70: 0253 0029 024e 7a11 7370 6869 6e78 2d71  .S.).Nz.sphinx-q
+00003a80: 7569 636b 7374 6172 7472 9b00 0000 7222  uickstartr....r"
+00003a90: 0000 0072 1500 0000 7215 0000 0072 1600  ...r....r....r..
+00003aa0: 0000 da1f 7061 7468 5f76 656e 765f 6269  ....path_venv_bi
+00003ab0: 6e5f 7370 6869 6e78 5f71 7569 636b 7374  n_sphinx_quickst
+00003ac0: 6172 74f2 0100 0073 0200 0000 0002 7a2a  art....s......z*
+00003ad0: 5265 706f 436f 6e66 6967 2e70 6174 685f  RepoConfig.path_
+00003ae0: 7665 6e76 5f62 696e 5f73 7068 696e 785f  venv_bin_sphinx_
+00003af0: 7175 6963 6b73 7461 7274 6301 0000 0000  quickstartc.....
+00003b00: 0000 0000 0000 0001 0000 0004 0000 0043  ...............C
+00003b10: 0000 0073 1000 0000 7400 6a01 a002 7c00  ...s....t.j...|.
+00003b20: 6a03 6401 a102 5300 2902 4e5a 0574 7769  j.d...S.).NZ.twi
+00003b30: 6e65 729b 0000 0072 2200 0000 7215 0000  ner....r"...r...
+00003b40: 0072 1500 0000 7216 0000 00da 1370 6174  .r....r......pat
+00003b50: 685f 7665 6e76 5f62 696e 5f74 7769 6e65  h_venv_bin_twine
+00003b60: f601 0000 7302 0000 0000 027a 1e52 6570  ....s......z.Rep
+00003b70: 6f43 6f6e 6669 672e 7061 7468 5f76 656e  oConfig.path_ven
+00003b80: 765f 6269 6e5f 7477 696e 6563 0100 0000  v_bin_twinec....
+00003b90: 0000 0000 0000 0000 0100 0000 0400 0000  ................
+00003ba0: 4300 0000 7310 0000 0074 006a 01a0 027c  C...s....t.j...|
+00003bb0: 006a 0364 01a1 0253 0029 024e da03 746f  .j.d...S.).N..to
+00003bc0: 7872 9b00 0000 7222 0000 0072 1500 0000  xr....r"...r....
+00003bd0: 7215 0000 0072 1600 0000 da11 7061 7468  r....r......path
+00003be0: 5f76 656e 765f 6269 6e5f 746f 78fa 0100  _venv_bin_tox...
+00003bf0: 0073 0200 0000 0002 7a1c 5265 706f 436f  .s......z.RepoCo
+00003c00: 6e66 6967 2e70 6174 685f 7665 6e76 5f62  nfig.path_venv_b
+00003c10: 696e 5f74 6f78 6301 0000 0000 0000 0000  in_toxc.........
+00003c20: 0000 0001 0000 0004 0000 0043 0000 0073  ...........C...s
+00003c30: 1000 0000 7400 6a01 a002 7c00 6a03 6401  ....t.j...|.j.d.
+00003c40: a102 5300 2902 4e5a 076a 7570 7974 6572  ..S.).NZ.jupyter
+00003c50: 729b 0000 0072 2200 0000 7215 0000 0072  r....r"...r....r
+00003c60: 1500 0000 7216 0000 00da 1570 6174 685f  ....r......path_
+00003c70: 7665 6e76 5f62 696e 5f6a 7570 7974 6572  venv_bin_jupyter
+00003c80: fe01 0000 7302 0000 0000 027a 2052 6570  ....s......z Rep
+00003c90: 6f43 6f6e 6669 672e 7061 7468 5f76 656e  oConfig.path_ven
+00003ca0: 765f 6269 6e5f 6a75 7079 7465 7263 0100  v_bin_jupyterc..
+00003cb0: 0000 0000 0000 0000 0000 0100 0000 0400  ................
+00003cc0: 0000 4300 0000 7310 0000 0074 006a 01a0  ..C...s....t.j..
+00003cd0: 027c 006a 0364 01a1 0253 0029 024e 5a07  .|.j.d...S.).NZ.
+00003ce0: 616e 7369 626c 6572 9b00 0000 7222 0000  ansibler....r"..
+00003cf0: 0072 1500 0000 7215 0000 0072 1600 0000  .r....r....r....
+00003d00: da15 7061 7468 5f76 656e 765f 6269 6e5f  ..path_venv_bin_
+00003d10: 616e 7369 626c 6502 0200 0073 0200 0000  ansible....s....
+00003d20: 0002 7a20 5265 706f 436f 6e66 6967 2e70  ..z RepoConfig.p
+00003d30: 6174 685f 7665 6e76 5f62 696e 5f61 6e73  ath_venv_bin_ans
+00003d40: 6962 6c65 6301 0000 0000 0000 0000 0000  iblec...........
+00003d50: 0001 0000 0004 0000 0043 0000 0073 1000  .........C...s..
+00003d60: 0000 7400 6a01 a002 7c00 6a03 6401 a102  ..t.j...|.j.d...
+00003d70: 5300 2902 4eda 0361 7773 729b 0000 0072  S.).N..awsr....r
+00003d80: 2200 0000 7215 0000 0072 1500 0000 7216  "...r....r....r.
+00003d90: 0000 00da 1170 6174 685f 7665 6e76 5f62  .....path_venv_b
+00003da0: 696e 5f61 7773 0602 0000 7302 0000 0000  in_aws....s.....
+00003db0: 027a 1c52 6570 6f43 6f6e 6669 672e 7061  .z.RepoConfig.pa
+00003dc0: 7468 5f76 656e 765f 6269 6e5f 6177 7363  th_venv_bin_awsc
+00003dd0: 0100 0000 0000 0000 0000 0000 0100 0000  ................
+00003de0: 0400 0000 4300 0000 7310 0000 0074 006a  ....C...s....t.j
+00003df0: 01a0 027c 006a 0364 01a1 0253 0029 024e  ...|.j.d...S.).N
+00003e00: 5a07 6368 616c 6963 6572 9b00 0000 7222  Z.chalicer....r"
+00003e10: 0000 0072 1500 0000 7215 0000 0072 1600  ...r....r....r..
+00003e20: 0000 da15 7061 7468 5f76 656e 765f 6269  ....path_venv_bi
+00003e30: 6e5f 6368 616c 6963 650a 0200 0073 0200  n_chalice....s..
+00003e40: 0000 0002 7a20 5265 706f 436f 6e66 6967  ....z RepoConfig
+00003e50: 2e70 6174 685f 7665 6e76 5f62 696e 5f63  .path_venv_bin_c
+00003e60: 6861 6c69 6365 6301 0000 0000 0000 0000  halicec.........
+00003e70: 0000 0001 0000 0004 0000 0043 0000 0073  ...........C...s
+00003e80: 1000 0000 7400 6a01 a002 7c00 6a03 6401  ....t.j...|.j.d.
+00003e90: a102 5300 2902 4e5a 0566 6c61 736b 729b  ..S.).NZ.flaskr.
+00003ea0: 0000 0072 2200 0000 7215 0000 0072 1500  ...r"...r....r..
+00003eb0: 0000 7216 0000 00da 1370 6174 685f 7665  ..r......path_ve
+00003ec0: 6e76 5f62 696e 5f66 6c61 736b 0e02 0000  nv_bin_flask....
+00003ed0: 7302 0000 0000 027a 1e52 6570 6f43 6f6e  s......z.RepoCon
+00003ee0: 6669 672e 7061 7468 5f76 656e 765f 6269  fig.path_venv_bi
+00003ef0: 6e5f 666c 6173 6b63 0100 0000 0000 0000  n_flaskc........
+00003f00: 0000 0000 0100 0000 0400 0000 4300 0000  ............C...
+00003f10: 7310 0000 0074 006a 01a0 027c 006a 0364  s....t.j...|.j.d
+00003f20: 01a1 0253 0029 024e 5a09 636f 6e66 6967  ...S.).NZ.config
+00003f30: 6972 6c72 9b00 0000 7222 0000 0072 1500  irlr....r"...r..
+00003f40: 0000 7215 0000 0072 1600 0000 da17 7061  ..r....r......pa
+00003f50: 7468 5f76 656e 765f 6269 6e5f 636f 6e66  th_venv_bin_conf
+00003f60: 6967 6972 6c12 0200 0073 0200 0000 0002  igirl....s......
+00003f70: 7a22 5265 706f 436f 6e66 6967 2e70 6174  z"RepoConfig.pat
+00003f80: 685f 7665 6e76 5f62 696e 5f63 6f6e 6669  h_venv_bin_confi
+00003f90: 6769 726c 6301 0000 0000 0000 0000 0000  girlc...........
+00003fa0: 0002 0000 0002 0000 0043 0000 0073 1e00  .........C...s..
+00003fb0: 0000 7c00 6a00 a001 a100 7d01 7c01 6400  ..|.j.....}.|.d.
+00003fc0: 6b08 7216 6401 5300 7c01 5300 6400 5300  k.r.d.S.|.S.d.S.
+00003fd0: a902 4eda 0029 0272 2e00 0000 720f 0000  ..N..).r....r...
+00003fe0: 0029 0272 1200 0000 da14 646f 635f 686f  .).r......doc_ho
+00003ff0: 7374 5f61 7773 5f70 726f 6669 6c65 7215  st_aws_profiler.
+00004000: 0000 0072 1500 0000 7216 0000 00da 1c61  ...r....r......a
+00004010: 7773 5f63 6c69 5f70 726f 6669 6c65 5f61  ws_cli_profile_a
+00004020: 7267 5f64 6f63 5f68 6f73 7417 0200 0073  rg_doc_host....s
+00004030: 0800 0000 0002 0a01 0801 0402 7a27 5265  ............z'Re
+00004040: 706f 436f 6e66 6967 2e61 7773 5f63 6c69  poConfig.aws_cli
+00004050: 5f70 726f 6669 6c65 5f61 7267 5f64 6f63  _profile_arg_doc
+00004060: 5f68 6f73 7463 0100 0000 0000 0000 0000  _hostc..........
+00004070: 0000 0200 0000 0200 0000 4300 0000 731e  ..........C...s.
+00004080: 0000 007c 006a 00a0 01a1 007d 017c 0164  ...|.j.....}.|.d
+00004090: 006b 0872 1664 0153 007c 0153 0064 0053  .k.r.d.S.|.S.d.S
+000040a0: 0072 ac00 0000 2902 7234 0000 0072 0f00  .r....).r4...r..
+000040b0: 0000 2902 7212 0000 005a 1d61 7773 5f6c  ..).r....Z.aws_l
+000040c0: 616d 6264 615f 6465 706c 6f79 5f61 7773  ambda_deploy_aws
+000040d0: 5f70 726f 6669 6c65 7215 0000 0072 1500  _profiler....r..
+000040e0: 0000 7216 0000 00da 2161 7773 5f63 6c69  ..r.....!aws_cli
+000040f0: 5f70 726f 6669 6c65 5f61 7267 5f6c 616d  _profile_arg_lam
+00004100: 6264 615f 6465 706c 6f79 1f02 0000 7308  bda_deploy....s.
+00004110: 0000 0000 020a 0108 0104 027a 2c52 6570  ...........z,Rep
+00004120: 6f43 6f6e 6669 672e 6177 735f 636c 695f  oConfig.aws_cli_
+00004130: 7072 6f66 696c 655f 6172 675f 6c61 6d62  profile_arg_lamb
+00004140: 6461 5f64 6570 6c6f 7963 0100 0000 0000  da_deployc......
+00004150: 0000 0000 0000 0100 0000 0400 0000 4300  ..............C.
+00004160: 0000 7310 0000 0074 006a 01a0 027c 006a  ..s....t.j...|.j
+00004170: 0364 01a1 0253 0029 024e da06 6c61 6d62  .d...S.).N..lamb
+00004180: 6461 2904 7239 0000 0072 3c00 0000 723e  da).r9...r<...r>
+00004190: 0000 0072 6500 0000 7222 0000 0072 1500  ...re...r"...r..
+000041a0: 0000 7215 0000 0072 1600 0000 da10 6469  ..r....r......di
+000041b0: 725f 6c61 6d62 6461 5f62 7569 6c64 2b02  r_lambda_build+.
+000041c0: 0000 7302 0000 0000 027a 1b52 6570 6f43  ..s......z.RepoC
+000041d0: 6f6e 6669 672e 6469 725f 6c61 6d62 6461  onfig.dir_lambda
+000041e0: 5f62 7569 6c64 6301 0000 0000 0000 0000  _buildc.........
+000041f0: 0000 0001 0000 0004 0000 0043 0000 0073  ...........C...s
+00004200: 1000 0000 7400 6a01 a002 7c00 6a03 6401  ....t.j...|.j.d.
+00004210: a102 5300 2902 4e7a 0a73 6f75 7263 652e  ..S.).Nz.source.
+00004220: 7a69 70a9 0472 3900 0000 723c 0000 0072  zip..r9...r<...r
+00004230: 3e00 0000 72b2 0000 0072 2200 0000 7215  >...r....r"...r.
+00004240: 0000 0072 1500 0000 7216 0000 00da 1870  ...r....r......p
+00004250: 6174 685f 6c61 6d62 6461 5f62 7569 6c64  ath_lambda_build
+00004260: 5f73 6f75 7263 652f 0200 0073 0200 0000  _source/...s....
+00004270: 0002 7a23 5265 706f 436f 6e66 6967 2e70  ..z#RepoConfig.p
+00004280: 6174 685f 6c61 6d62 6461 5f62 7569 6c64  ath_lambda_build
+00004290: 5f73 6f75 7263 6563 0100 0000 0000 0000  _sourcec........
+000042a0: 0000 0000 0100 0000 0400 0000 4300 0000  ............C...
+000042b0: 7310 0000 0074 006a 01a0 027c 006a 0364  s....t.j...|.j.d
+000042c0: 01a1 0253 0029 024e 7a09 6c61 7965 722e  ...S.).Nz.layer.
+000042d0: 7a69 7072 b300 0000 7222 0000 0072 1500  zipr....r"...r..
+000042e0: 0000 7215 0000 0072 1600 0000 da17 7061  ..r....r......pa
+000042f0: 7468 5f6c 616d 6264 615f 6275 696c 645f  th_lambda_build_
+00004300: 6c61 7965 7233 0200 0073 0200 0000 0002  layer3...s......
+00004310: 7a22 5265 706f 436f 6e66 6967 2e70 6174  z"RepoConfig.pat
+00004320: 685f 6c61 6d62 6461 5f62 7569 6c64 5f6c  h_lambda_build_l
+00004330: 6179 6572 6301 0000 0000 0000 0000 0000  ayerc...........
+00004340: 0001 0000 0004 0000 0043 0000 0073 1000  .........C...s..
+00004350: 0000 7400 6a01 a002 7c00 6a03 6401 a102  ..t.j...|.j.d...
+00004360: 5300 2902 4e7a 0e64 6570 6c6f 792d 706b  S.).Nz.deploy-pk
+00004370: 672e 7a69 7072 b300 0000 7222 0000 0072  g.zipr....r"...r
+00004380: 1500 0000 7215 0000 0072 1600 0000 da20  ....r....r..... 
+00004390: 7061 7468 5f6c 616d 6264 615f 6275 696c  path_lambda_buil
+000043a0: 645f 6465 706c 6f79 5f70 6163 6b61 6765  d_deploy_package
+000043b0: 3702 0000 7302 0000 0000 027a 2b52 6570  7...s......z+Rep
+000043c0: 6f43 6f6e 6669 672e 7061 7468 5f6c 616d  oConfig.path_lam
+000043d0: 6264 615f 6275 696c 645f 6465 706c 6f79  bda_build_deploy
+000043e0: 5f70 6163 6b61 6765 6301 0000 0000 0000  _packagec.......
+000043f0: 0000 0000 0001 0000 0004 0000 0043 0000  .............C..
+00004400: 0073 1600 0000 7400 6401 7c00 6a01 a002  .s....t.d.|.j...
+00004410: a100 6702 6402 6403 8d02 5300 2904 7a2d  ..g.d.d...S.).z-
+00004420: 0a20 2020 2020 2020 2065 7861 6d70 6c65  .        example
+00004430: 3a20 6c61 6d62 6461 2f6d 795f 7061 636b  : lambda/my_pack
+00004440: 6167 652f 0a20 2020 2020 2020 2072 b100  age/.        r..
+00004450: 0000 54a9 02da 0570 6172 7473 da06 6973  ..T....parts..is
+00004460: 5f64 6972 2903 7208 0000 0072 2100 0000  _dir).r....r!...
+00004470: 720f 0000 0072 2200 0000 7215 0000 0072  r....r"...r....r
+00004480: 1500 0000 7216 0000 00da 1873 335f 6b65  ....r......s3_ke
+00004490: 795f 6c61 6d62 6461 5f64 6570 6c6f 795f  y_lambda_deploy_
+000044a0: 6469 723c 0200 0073 0c00 0000 0005 0202  dir<...s........
+000044b0: 0201 08fe 0204 02fb 7a23 5265 706f 436f  ........z#RepoCo
+000044c0: 6e66 6967 2e73 335f 6b65 795f 6c61 6d62  nfig.s3_key_lamb
+000044d0: 6461 5f64 6570 6c6f 795f 6469 7263 0100  da_deploy_dirc..
+000044e0: 0000 0000 0000 0000 0000 0100 0000 0400  ................
+000044f0: 0000 4300 0000 7314 0000 0074 007c 006a  ..C...s....t.|.j
+00004500: 017c 006a 0267 0264 0164 028d 0253 0029  .|.j.g.d.d...S.)
+00004510: 037a 330a 2020 2020 2020 2020 6578 616d  .z3.        exam
+00004520: 706c 653a 206c 616d 6264 612f 6d79 5f70  ple: lambda/my_p
+00004530: 6163 6b61 6765 2f30 2e30 2e31 2f0a 2020  ackage/0.0.1/.  
+00004540: 2020 2020 2020 5472 b700 0000 2903 7208        Tr....).r.
+00004550: 0000 0072 ba00 0000 725f 0000 0072 2200  ...r....r_...r".
+00004560: 0000 7215 0000 0072 1500 0000 7216 0000  ..r....r....r...
+00004570: 00da 2273 335f 6b65 795f 6c61 6d62 6461  .."s3_key_lambda
+00004580: 5f64 6570 6c6f 795f 7665 7273 696f 6e65  _deploy_versione
+00004590: 645f 6469 7249 0200 0073 0c00 0000 0005  d_dirI...s......
+000045a0: 0202 0401 04fe 0204 02fb 7a2d 5265 706f  ..........z-Repo
+000045b0: 436f 6e66 6967 2e73 335f 6b65 795f 6c61  Config.s3_key_la
+000045c0: 6d62 6461 5f64 6570 6c6f 795f 7665 7273  mbda_deploy_vers
+000045d0: 696f 6e65 645f 6469 7263 0100 0000 0000  ioned_dirc......
+000045e0: 0000 0000 0000 0100 0000 0400 0000 4300  ..............C.
+000045f0: 0000 731c 0000 007c 00a0 00a1 0001 0074  ..s....|.......t
+00004600: 017c 006a 02a0 03a1 007c 006a 0464 018d  .|.j.....|.j.d..
+00004610: 0253 0029 027a 3f0a 2020 2020 2020 2020  .S.).z?.        
+00004620: 6578 616d 706c 653a 2073 333a 2f2f 6275  example: s3://bu
+00004630: 636b 6574 2f6c 616d 6264 612f 6d79 5f70  cket/lambda/my_p
+00004640: 6163 6b61 6765 2f30 2e30 2e31 2f0a 2020  ackage/0.0.1/.  
+00004650: 2020 2020 2020 a902 7281 0000 00da 036b        ..r......k
+00004660: 6579 2905 7233 0000 0072 0700 0000 7231  ey).r3...r....r1
+00004670: 0000 0072 0f00 0000 72bb 0000 0072 2200  ...r....r....r".
+00004680: 0000 7215 0000 0072 1500 0000 7216 0000  ..r....r....r...
+00004690: 00da 2273 335f 7572 695f 6c61 6d62 6461  .."s3_uri_lambda
+000046a0: 5f64 6570 6c6f 795f 7665 7273 696f 6e65  _deploy_versione
+000046b0: 645f 6469 7256 0200 0073 0a00 0000 0005  d_dirV...s......
+000046c0: 0801 0201 0801 04fe 7a2d 5265 706f 436f  ........z-RepoCo
+000046d0: 6e66 6967 2e73 335f 7572 695f 6c61 6d62  nfig.s3_uri_lamb
+000046e0: 6461 5f64 6570 6c6f 795f 7665 7273 696f  da_deploy_versio
+000046f0: 6e65 645f 6469 7263 0100 0000 0000 0000  ned_dirc........
+00004700: 0000 0000 0100 0000 0400 0000 4300 0000  ............C...
+00004710: 7312 0000 0074 007c 006a 0164 0167 0264  s....t.|.j.d.g.d
+00004720: 0264 038d 0253 0029 047a 3a0a 2020 2020  .d...S.).z:.    
+00004730: 2020 2020 6578 616d 706c 653a 206c 616d      example: lam
+00004740: 6264 612f 6d79 5f70 6163 6b61 6765 2f30  bda/my_package/0
+00004750: 2e30 2e31 2f73 6f75 7263 652f 0a20 2020  .0.1/source/.   
+00004760: 2020 2020 2072 7600 0000 5472 b700 0000       rv...Tr....
+00004770: a902 7208 0000 0072 bb00 0000 7222 0000  ..r....r....r"..
+00004780: 0072 1500 0000 7215 0000 0072 1600 0000  .r....r....r....
+00004790: da29 7333 5f6b 6579 5f6c 616d 6264 615f  .)s3_key_lambda_
+000047a0: 6465 706c 6f79 5f76 6572 7369 6f6e 6564  deploy_versioned
+000047b0: 5f73 6f75 7263 655f 6469 7262 0200 0073  _source_dirb...s
+000047c0: 0c00 0000 0005 0202 0401 02fe 0204 02fb  ................
+000047d0: 7a34 5265 706f 436f 6e66 6967 2e73 335f  z4RepoConfig.s3_
+000047e0: 6b65 795f 6c61 6d62 6461 5f64 6570 6c6f  key_lambda_deplo
+000047f0: 795f 7665 7273 696f 6e65 645f 736f 7572  y_versioned_sour
+00004800: 6365 5f64 6972 6301 0000 0000 0000 0000  ce_dirc.........
+00004810: 0000 0001 0000 0004 0000 0043 0000 0073  ...........C...s
+00004820: 1c00 0000 7c00 a000 a100 0100 7401 7c00  ....|.......t.|.
+00004830: 6a02 a003 a100 7c00 6a04 6401 8d02 5300  j.....|.j.d...S.
+00004840: 2902 7a46 0a20 2020 2020 2020 2065 7861  ).zF.        exa
+00004850: 6d70 6c65 3a20 7333 3a2f 2f62 7563 6b65  mple: s3://bucke
+00004860: 742f 6c61 6d62 6461 2f6d 795f 7061 636b  t/lambda/my_pack
+00004870: 6167 652f 302e 302e 312f 736f 7572 6365  age/0.0.1/source
+00004880: 2f0a 2020 2020 2020 2020 72bc 0000 0029  /.        r....)
+00004890: 0572 3300 0000 7207 0000 0072 3100 0000  .r3...r....r1...
+000048a0: 720f 0000 0072 c000 0000 7222 0000 0072  r....r....r"...r
+000048b0: 1500 0000 7215 0000 0072 1600 0000 da29  ....r....r.....)
+000048c0: 7333 5f75 7269 5f6c 616d 6264 615f 6465  s3_uri_lambda_de
+000048d0: 706c 6f79 5f76 6572 7369 6f6e 6564 5f73  ploy_versioned_s
+000048e0: 6f75 7263 655f 6469 726f 0200 0073 0a00  ource_diro...s..
+000048f0: 0000 0005 0801 0201 0801 04fe 7a34 5265  ............z4Re
+00004900: 706f 436f 6e66 6967 2e73 335f 7572 695f  poConfig.s3_uri_
+00004910: 6c61 6d62 6461 5f64 6570 6c6f 795f 7665  lambda_deploy_ve
+00004920: 7273 696f 6e65 645f 736f 7572 6365 5f64  rsioned_source_d
+00004930: 6972 6301 0000 0000 0000 0000 0000 0001  irc.............
+00004940: 0000 0004 0000 0043 0000 0073 1200 0000  .......C...s....
+00004950: 7400 7c00 6a01 6401 6702 6402 6403 8d02  t.|.j.d.g.d.d...
+00004960: 5300 2904 7a39 0a20 2020 2020 2020 2065  S.).z9.        e
+00004970: 7861 6d70 6c65 3a20 6c61 6d62 6461 2f6d  xample: lambda/m
+00004980: 795f 7061 636b 6167 652f 302e 302e 312f  y_package/0.0.1/
+00004990: 6c61 7965 722f 0a20 2020 2020 2020 20da  layer/.        .
+000049a0: 056c 6179 6572 5472 b700 0000 72bf 0000  .layerTr....r...
+000049b0: 0072 2200 0000 7215 0000 0072 1500 0000  .r"...r....r....
+000049c0: 7216 0000 00da 2873 335f 6b65 795f 6c61  r.....(s3_key_la
+000049d0: 6d62 6461 5f64 6570 6c6f 795f 7665 7273  mbda_deploy_vers
+000049e0: 696f 6e65 645f 6c61 7965 725f 6469 727b  ioned_layer_dir{
+000049f0: 0200 0073 0c00 0000 0005 0202 0401 02fe  ...s............
+00004a00: 0204 02fb 7a33 5265 706f 436f 6e66 6967  ....z3RepoConfig
+00004a10: 2e73 335f 6b65 795f 6c61 6d62 6461 5f64  .s3_key_lambda_d
+00004a20: 6570 6c6f 795f 7665 7273 696f 6e65 645f  eploy_versioned_
+00004a30: 6c61 7965 725f 6469 7263 0100 0000 0000  layer_dirc......
+00004a40: 0000 0000 0000 0100 0000 0400 0000 4300  ..............C.
+00004a50: 0000 731c 0000 007c 00a0 00a1 0001 0074  ..s....|.......t
+00004a60: 017c 006a 02a0 03a1 007c 006a 0464 018d  .|.j.....|.j.d..
+00004a70: 0253 0029 027a 450a 2020 2020 2020 2020  .S.).zE.        
+00004a80: 6578 616d 706c 653a 2073 333a 2f2f 6275  example: s3://bu
+00004a90: 636b 6574 2f6c 616d 6264 612f 6d79 5f70  cket/lambda/my_p
+00004aa0: 6163 6b61 6765 2f30 2e30 2e31 2f6c 6179  ackage/0.0.1/lay
+00004ab0: 6572 2f0a 2020 2020 2020 2020 72bc 0000  er/.        r...
+00004ac0: 0029 0572 3300 0000 7207 0000 0072 3100  .).r3...r....r1.
+00004ad0: 0000 720f 0000 0072 c300 0000 7222 0000  ..r....r....r"..
+00004ae0: 0072 1500 0000 7215 0000 0072 1600 0000  .r....r....r....
+00004af0: da28 7333 5f75 7269 5f6c 616d 6264 615f  .(s3_uri_lambda_
+00004b00: 6465 706c 6f79 5f76 6572 7369 6f6e 6564  deploy_versioned
+00004b10: 5f6c 6179 6572 5f64 6972 8802 0000 730a  _layer_dir....s.
+00004b20: 0000 0000 0508 0102 0108 0104 fe7a 3352  .............z3R
+00004b30: 6570 6f43 6f6e 6669 672e 7333 5f75 7269  epoConfig.s3_uri
+00004b40: 5f6c 616d 6264 615f 6465 706c 6f79 5f76  _lambda_deploy_v
+00004b50: 6572 7369 6f6e 6564 5f6c 6179 6572 5f64  ersioned_layer_d
+00004b60: 6972 6301 0000 0000 0000 0000 0000 0001  irc.............
+00004b70: 0000 0004 0000 0043 0000 0073 1200 0000  .......C...s....
+00004b80: 7400 7c00 6a01 6401 6702 6402 6403 8d02  t.|.j.d.g.d.d...
+00004b90: 5300 2904 7a3e 0a20 2020 2020 2020 2065  S.).z>.        e
+00004ba0: 7861 6d70 6c65 3a20 6c61 6d62 6461 2f6d  xample: lambda/m
+00004bb0: 795f 7061 636b 6167 652f 302e 302e 312f  y_package/0.0.1/
+00004bc0: 6465 706c 6f79 2d70 6b67 2f0a 2020 2020  deploy-pkg/.    
+00004bd0: 2020 2020 7a0a 6465 706c 6f79 2d70 6b67      z.deploy-pkg
+00004be0: 5472 b700 0000 72bf 0000 0072 2200 0000  Tr....r....r"...
+00004bf0: 7215 0000 0072 1500 0000 7216 0000 00da  r....r....r.....
+00004c00: 2d73 335f 6b65 795f 6c61 6d62 6461 5f64  -s3_key_lambda_d
+00004c10: 6570 6c6f 795f 7665 7273 696f 6e65 645f  eploy_versioned_
+00004c20: 6465 706c 6f79 5f70 6b67 5f64 6972 9402  deploy_pkg_dir..
+00004c30: 0000 730c 0000 0000 0502 0204 0102 fe02  ..s.............
+00004c40: 0402 fb7a 3852 6570 6f43 6f6e 6669 672e  ...z8RepoConfig.
+00004c50: 7333 5f6b 6579 5f6c 616d 6264 615f 6465  s3_key_lambda_de
+00004c60: 706c 6f79 5f76 6572 7369 6f6e 6564 5f64  ploy_versioned_d
+00004c70: 6570 6c6f 795f 706b 675f 6469 7263 0100  eploy_pkg_dirc..
+00004c80: 0000 0000 0000 0000 0000 0100 0000 0400  ................
+00004c90: 0000 4300 0000 731c 0000 007c 00a0 00a1  ..C...s....|....
+00004ca0: 0001 0074 017c 006a 02a0 03a1 007c 006a  ...t.|.j.....|.j
+00004cb0: 0464 018d 0253 0029 027a 4a0a 2020 2020  .d...S.).zJ.    
+00004cc0: 2020 2020 6578 616d 706c 653a 2073 333a      example: s3:
+00004cd0: 2f2f 6275 636b 6574 2f6c 616d 6264 612f  //bucket/lambda/
+00004ce0: 6d79 5f70 6163 6b61 6765 2f30 2e30 2e31  my_package/0.0.1
+00004cf0: 2f64 6570 6c6f 792d 706b 672f 0a20 2020  /deploy-pkg/.   
+00004d00: 2020 2020 2072 bc00 0000 2905 7233 0000       r....).r3..
+00004d10: 0072 0700 0000 7231 0000 0072 0f00 0000  .r....r1...r....
+00004d20: 72c5 0000 0072 2200 0000 7215 0000 0072  r....r"...r....r
+00004d30: 1500 0000 7216 0000 00da 2d73 335f 7572  ....r.....-s3_ur
+00004d40: 695f 6c61 6d62 6461 5f64 6570 6c6f 795f  i_lambda_deploy_
+00004d50: 7665 7273 696f 6e65 645f 6465 706c 6f79  versioned_deploy
+00004d60: 5f70 6b67 5f64 6972 a102 0000 730a 0000  _pkg_dir....s...
+00004d70: 0000 0508 0102 0108 0104 fe7a 3852 6570  ...........z8Rep
+00004d80: 6f43 6f6e 6669 672e 7333 5f75 7269 5f6c  oConfig.s3_uri_l
+00004d90: 616d 6264 615f 6465 706c 6f79 5f76 6572  ambda_deploy_ver
+00004da0: 7369 6f6e 6564 5f64 6570 6c6f 795f 706b  sioned_deploy_pk
+00004db0: 675f 6469 7263 0100 0000 0000 0000 0000  g_dirc..........
+00004dc0: 0000 0100 0000 0200 0000 4300 0000 730a  ..........C...s.
+00004dd0: 0000 007c 006a 00a0 01a1 0053 0072 1f00  ...|.j.....S.r..
+00004de0: 0000 7220 0000 0072 2200 0000 7215 0000  ..r ...r"...r...
+00004df0: 0072 1500 0000 7216 0000 00da 1561 7773  .r....r......aws
+00004e00: 5f6c 616d 6264 615f 6c61 7965 725f 6e61  _lambda_layer_na
+00004e10: 6d65 ac02 0000 7302 0000 0000 027a 2052  me....s......z R
+00004e20: 6570 6f43 6f6e 6669 672e 6177 735f 6c61  epoConfig.aws_la
+00004e30: 6d62 6461 5f6c 6179 6572 5f6e 616d 6563  mbda_layer_namec
+00004e40: 0100 0000 0000 0000 0000 0000 0100 0000  ................
+00004e50: 0300 0000 4300 0000 730e 0000 0064 016a  ....C...s....d.j
+00004e60: 007c 006a 0164 028d 0153 0029 034e 7a40  .|.j.d...S.).Nz@
+00004e70: 6874 7470 733a 2f2f 636f 6e73 6f6c 652e  https://console.
+00004e80: 6177 732e 616d 617a 6f6e 2e63 6f6d 2f6c  aws.amazon.com/l
+00004e90: 616d 6264 612f 686f 6d65 3f23 2f6c 6179  ambda/home?#/lay
+00004ea0: 6572 732f 7b6c 6179 6572 5f6e 616d 657d  ers/{layer_name}
+00004eb0: 2901 5a0a 6c61 7965 725f 6e61 6d65 2902  ).Z.layer_name).
+00004ec0: 7211 0000 0072 c700 0000 7222 0000 0072  r....r....r"...r
+00004ed0: 1500 0000 7215 0000 0072 1600 0000 da18  ....r....r......
+00004ee0: 7572 6c5f 6c61 6d62 6461 5f6c 6179 6572  url_lambda_layer
+00004ef0: 5f63 6f6e 736f 6c65 b002 0000 7306 0000  _console....s...
+00004f00: 0000 0204 0104 ff7a 2352 6570 6f43 6f6e  .......z#RepoCon
+00004f10: 6669 672e 7572 6c5f 6c61 6d62 6461 5f6c  fig.url_lambda_l
+00004f20: 6179 6572 5f63 6f6e 736f 6c65 6301 0000  ayer_consolec...
+00004f30: 0000 0000 0000 0000 0001 0000 0004 0000  ................
+00004f40: 0043 0000 0073 1000 0000 7400 6a01 a002  .C...s....t.j...
+00004f50: 7c00 6a03 6401 a102 5300 2902 7a39 0a20  |.j.d...S.).z9. 
+00004f60: 2020 2020 2020 2065 7861 6d70 6c65 3a20         example: 
+00004f70: 247b 6469 725f 7072 6f6a 6563 745f 726f  ${dir_project_ro
+00004f80: 6f74 7d2f 6c61 6d62 6461 5f61 7070 0a20  ot}/lambda_app. 
+00004f90: 2020 2020 2020 205a 0a6c 616d 6264 615f         Z.lambda_
+00004fa0: 6170 7072 5700 0000 7222 0000 0072 1500  apprW...r"...r..
+00004fb0: 0000 7215 0000 0072 1600 0000 da0e 6469  ..r....r......di
+00004fc0: 725f 6c61 6d62 6461 5f61 7070 b802 0000  r_lambda_app....
+00004fd0: 7302 0000 0000 057a 1952 6570 6f43 6f6e  s......z.RepoCon
+00004fe0: 6669 672e 6469 725f 6c61 6d62 6461 5f61  fig.dir_lambda_a
+00004ff0: 7070 6301 0000 0000 0000 0000 0000 0001  ppc.............
+00005000: 0000 0004 0000 0043 0000 0073 1000 0000  .......C...s....
+00005010: 7400 6a01 a002 7c00 6a03 6401 a102 5300  t.j...|.j.d...S.
+00005020: 2902 7a42 0a20 2020 2020 2020 2065 7861  ).zB.        exa
+00005030: 6d70 6c65 3a20 247b 6469 725f 7072 6f6a  mple: ${dir_proj
+00005040: 6563 745f 726f 6f74 7d2f 6c61 6d62 6461  ect_root}/lambda
+00005050: 5f61 7070 2f2e 6368 616c 6963 650a 2020  _app/.chalice.  
+00005060: 2020 2020 2020 7a08 2e63 6861 6c69 6365        z..chalice
+00005070: a904 7239 0000 0072 3c00 0000 723e 0000  ..r9...r<...r>..
+00005080: 0072 c900 0000 7222 0000 0072 1500 0000  .r....r"...r....
+00005090: 7215 0000 0072 1600 0000 da0f 6469 725f  r....r......dir_
+000050a0: 6177 735f 6368 616c 6963 65bf 0200 0073  aws_chalice....s
+000050b0: 0200 0000 0005 7a1a 5265 706f 436f 6e66  ......z.RepoConf
+000050c0: 6967 2e64 6972 5f61 7773 5f63 6861 6c69  ig.dir_aws_chali
+000050d0: 6365 6301 0000 0000 0000 0000 0000 0001  cec.............
+000050e0: 0000 0004 0000 0043 0000 0073 1000 0000  .......C...s....
+000050f0: 7400 6a01 a002 7c00 6a03 6401 a102 5300  t.j...|.j.d...S.
+00005100: 2902 7a4e 0a20 2020 2020 2020 2065 7861  ).zN.        exa
+00005110: 6d70 6c65 3a20 247b 6469 725f 7072 6f6a  mple: ${dir_proj
+00005120: 6563 745f 726f 6f74 7d2f 6c61 6d62 6461  ect_root}/lambda
+00005130: 5f61 7070 2f2e 6368 616c 6963 652f 636f  _app/.chalice/co
+00005140: 6e66 6967 2e6a 736f 6e0a 2020 2020 2020  nfig.json.      
+00005150: 2020 7a0b 636f 6e66 6967 2e6a 736f 6ea9    z.config.json.
+00005160: 0472 3900 0000 723c 0000 0072 3e00 0000  .r9...r<...r>...
+00005170: 72cb 0000 0072 2200 0000 7215 0000 0072  r....r"...r....r
+00005180: 1500 0000 7216 0000 00da 1c70 6174 685f  ....r......path_
+00005190: 6177 735f 6368 616c 6963 655f 636f 6e66  aws_chalice_conf
+000051a0: 6967 5f6a 736f 6ec6 0200 0073 0200 0000  ig_json....s....
+000051b0: 0005 7a27 5265 706f 436f 6e66 6967 2e70  ..z'RepoConfig.p
+000051c0: 6174 685f 6177 735f 6368 616c 6963 655f  ath_aws_chalice_
+000051d0: 636f 6e66 6967 5f6a 736f 6e63 0100 0000  config_jsonc....
+000051e0: 0000 0000 0000 0000 0100 0000 0400 0000  ................
+000051f0: 4300 0000 7310 0000 0074 006a 01a0 027c  C...s....t.j...|
+00005200: 006a 0364 01a1 0253 0029 027a 400a 2020  .j.d...S.).z@.  
+00005210: 2020 2020 2020 6578 616d 706c 653a 2024        example: $
+00005220: 7b64 6972 5f70 726f 6a65 6374 5f72 6f6f  {dir_project_roo
+00005230: 747d 2f6c 616d 6264 615f 6170 702f 6170  t}/lambda_app/ap
+00005240: 702e 7079 0a20 2020 2020 2020 207a 0661  p.py.        z.a
+00005250: 7070 2e70 7972 ca00 0000 7222 0000 0072  pp.pyr....r"...r
+00005260: 1500 0000 7215 0000 0072 1600 0000 da17  ....r....r......
+00005270: 7061 7468 5f61 7773 5f63 6861 6c69 6365  path_aws_chalice
+00005280: 5f61 7070 5f70 79cd 0200 0073 0200 0000  _app_py....s....
+00005290: 0005 7a22 5265 706f 436f 6e66 6967 2e70  ..z"RepoConfig.p
+000052a0: 6174 685f 6177 735f 6368 616c 6963 655f  ath_aws_chalice_
+000052b0: 6170 705f 7079 6301 0000 0000 0000 0000  app_pyc.........
+000052c0: 0000 0001 0000 0004 0000 0043 0000 0073  ...........C...s
+000052d0: 1000 0000 7400 6a01 a002 7c00 6a03 6401  ....t.j...|.j.d.
+000052e0: a102 5300 2902 7a40 0a20 2020 2020 2020  ..S.).z@.       
+000052f0: 2065 7861 6d70 6c65 3a20 247b 6469 725f   example: ${dir_
+00005300: 7072 6f6a 6563 745f 726f 6f74 7d2f 6c61  project_root}/la
+00005310: 6d62 6461 5f61 7070 2f76 656e 646f 720a  mbda_app/vendor.
+00005320: 2020 2020 2020 2020 5a06 7665 6e64 6f72          Z.vendor
+00005330: 72ca 0000 0072 2200 0000 7215 0000 0072  r....r"...r....r
+00005340: 1500 0000 7216 0000 00da 1664 6972 5f61  ....r......dir_a
+00005350: 7773 5f63 6861 6c69 6365 5f76 656e 646f  ws_chalice_vendo
+00005360: 72d4 0200 0073 0200 0000 0005 7a21 5265  r....s......z!Re
+00005370: 706f 436f 6e66 6967 2e64 6972 5f61 7773  poConfig.dir_aws
+00005380: 5f63 6861 6c69 6365 5f76 656e 646f 7263  _chalice_vendorc
+00005390: 0100 0000 0000 0000 0000 0000 0100 0000  ................
+000053a0: 0500 0000 4300 0000 7316 0000 0074 006a  ....C...s....t.j
+000053b0: 01a0 027c 006a 037c 006a 04a0 05a1 00a1  ...|.j.|.j......
+000053c0: 0253 0029 017a 500a 2020 2020 2020 2020  .S.).zP.        
+000053d0: 6578 616d 706c 653a 2024 7b64 6972 5f70  example: ${dir_p
+000053e0: 726f 6a65 6374 5f72 6f6f 747d 2f6c 616d  roject_root}/lam
+000053f0: 6264 615f 6170 702f 7665 6e64 6f72 2f24  bda_app/vendor/$
+00005400: 7b70 6163 6b61 6765 5f6e 616d 657d 0a20  {package_name}. 
+00005410: 2020 2020 2020 2029 0672 3900 0000 723c         ).r9...r<
+00005420: 0000 0072 3e00 0000 72cf 0000 0072 2100  ...r>...r....r!.
+00005430: 0000 720f 0000 0072 2200 0000 7215 0000  ..r....r"...r...
+00005440: 0072 1500 0000 7216 0000 00da 1d64 6972  .r....r......dir
+00005450: 5f61 7773 5f63 6861 6c69 6365 5f76 656e  _aws_chalice_ven
+00005460: 646f 725f 736f 7572 6365 db02 0000 7308  dor_source....s.
+00005470: 0000 0000 0506 0104 0108 fe7a 2852 6570  ...........z(Rep
+00005480: 6f43 6f6e 6669 672e 6469 725f 6177 735f  oConfig.dir_aws_
+00005490: 6368 616c 6963 655f 7665 6e64 6f72 5f73  chalice_vendor_s
+000054a0: 6f75 7263 6563 0100 0000 0000 0000 0000  ourcec..........
+000054b0: 0000 0100 0000 0400 0000 4300 0000 7310  ..........C...s.
+000054c0: 0000 0074 006a 01a0 027c 006a 0364 01a1  ...t.j...|.j.d..
+000054d0: 0253 0029 027a 4b0a 2020 2020 2020 2020  .S.).zK.        
+000054e0: 6578 616d 706c 653a 2024 7b64 6972 5f70  example: ${dir_p
+000054f0: 726f 6a65 6374 5f72 6f6f 747d 2f6c 616d  roject_root}/lam
+00005500: 6264 615f 6170 702f 2e63 6861 6c69 6365  bda_app/.chalice
+00005510: 2f64 6570 6c6f 7965 640a 2020 2020 2020  /deployed.      
+00005520: 2020 5a08 6465 706c 6f79 6564 72cc 0000    Z.deployedr...
+00005530: 0072 2200 0000 7215 0000 0072 1500 0000  .r"...r....r....
+00005540: 7216 0000 00da 1864 6972 5f61 7773 5f63  r......dir_aws_c
+00005550: 6861 6c69 6365 5f64 6570 6c6f 7965 64e5  halice_deployed.
+00005560: 0200 0073 0200 0000 0005 7a23 5265 706f  ...s......z#Repo
+00005570: 436f 6e66 6967 2e64 6972 5f61 7773 5f63  Config.dir_aws_c
+00005580: 6861 6c69 6365 5f64 6570 6c6f 7965 644e  halice_deployedN
+00005590: 2961 7218 0000 0072 1900 0000 721a 0000  )ar....r....r...
+000055a0: 0072 1b00 0000 7205 0000 0072 4100 0000  .r....r....rA...
+000055b0: da06 6765 7474 6572 723b 0000 0072 4000  ..getterr;...r@.
+000055c0: 0000 7246 0000 0072 5000 0000 728b 0000  ..rF...rP...r...
+000055d0: 0072 5300 0000 7255 0000 0072 5400 0000  .rS...rU...rT...
+000055e0: 722b 0000 0072 5600 0000 7258 0000 0072  r+...rV...rX...r
+000055f0: 5900 0000 725a 0000 0072 5f00 0000 7260  Y...rZ...r_...r`
+00005600: 0000 0072 6100 0000 7262 0000 0072 6300  ...ra...rb...rc.
+00005610: 0000 7265 0000 0072 6700 0000 7268 0000  ..re...rg...rh..
+00005620: 0072 6900 0000 726a 0000 0072 6b00 0000  .ri...rj...rk...
+00005630: 726c 0000 0072 6d00 0000 726e 0000 0072  rl...rm...rn...r
+00005640: 6f00 0000 7270 0000 0072 7100 0000 7273  o...rp...rq...rs
+00005650: 0000 0072 7400 0000 7275 0000 0072 7800  ...rt...ru...rx.
+00005660: 0000 7279 0000 0072 7a00 0000 727c 0000  ..ry...rz...r|..
+00005670: 0072 7d00 0000 727e 0000 0072 7f00 0000  .r}...r~...r....
+00005680: 7283 0000 0072 8700 0000 7288 0000 0072  r....r....r....r
+00005690: 8900 0000 728c 0000 0072 8d00 0000 728f  ....r....r....r.
+000056a0: 0000 0072 9000 0000 7295 0000 0072 9600  ...r....r....r..
+000056b0: 0000 7297 0000 0072 9800 0000 729a 0000  ..r....r....r...
+000056c0: 0072 9c00 0000 729e 0000 0072 9f00 0000  .r....r....r....
+000056d0: 72a0 0000 0072 a100 0000 72a2 0000 0072  r....r....r....r
+000056e0: a400 0000 72a5 0000 0072 a600 0000 72a8  ....r....r....r.
+000056f0: 0000 0072 a900 0000 72aa 0000 0072 ab00  ...r....r....r..
+00005700: 0000 72af 0000 0072 b000 0000 72b2 0000  ..r....r....r...
+00005710: 0072 b400 0000 72b5 0000 0072 b600 0000  .r....r....r....
+00005720: 72ba 0000 0072 bb00 0000 72be 0000 0072  r....r....r....r
+00005730: c000 0000 72c1 0000 0072 c300 0000 72c4  ....r....r....r.
+00005740: 0000 0072 c500 0000 72c6 0000 0072 c700  ...r....r....r..
+00005750: 0000 72c8 0000 0072 c900 0000 72cb 0000  ..r....r....r...
+00005760: 0072 cd00 0000 72ce 0000 0072 cf00 0000  .r....r....r....
+00005770: 72d0 0000 0072 d100 0000 7215 0000 0072  r....r....r....r
+00005780: 1500 0000 7215 0000 0072 1600 0000 7237  ....r....r....r7
+00005790: 0000 0066 0000 0073 5e01 0000 0805 0403  ...f...s^.......
+000057a0: 0a0f 0401 0a03 080c 0814 080e 0a0a 0401  ................
+000057b0: 0a05 0a02 0401 0a03 0201 0a03 0201 0a03  ................
+000057c0: 0201 0a03 0201 0a03 0201 0a08 0201 0a03  ................
 000057d0: 0201 0a03 0201 0a03 0201 0a03 0201 0a03  ................
-000057e0: 0201 0a09 0201 0a0a 0201 0a06 0201 0a08  ................
-000057f0: 0201 0a19 0201 0a03 0201 0a0f 0201 0a07  ................
-00005800: 0201 0a10 0201 0a0f 0201 0a06 0201 0a07  ................
-00005810: 0201 0a08 0201 0a03 0201 0a03 0201 0a03  ................
+000057e0: 0201 0a03 0201 0a06 0201 0a04 0201 0a03  ................
+000057f0: 0201 0a03 0201 0a03 0201 0a03 0201 0a03  ................
+00005800: 0201 0a03 0201 0a03 0201 0a03 0201 0a03  ................
+00005810: 0201 0a04 0201 0a03 0201 0a03 0201 0a03  ................
 00005820: 0201 0a03 0201 0a03 0201 0a03 0201 0a03  ................
-00005830: 0201 0a03 0201 0a03 0201 0a03 0201 0a03  ................
-00005840: 0201 0a03 0201 0a04 0201 0a07 0201 0a0b  ................
-00005850: 0201 0a03 0201 0a03 0201 0a03 0201 0a04  ................
-00005860: 0201 0a0c 0201 0a0c 0201 0a0b 0201 0a0c  ................
-00005870: 0201 0a0b 0201 0a0c 0201 0a0b 0201 0a0c  ................
-00005880: 0201 0a0a 0201 0a03 0201 0a07 0201 0a06  ................
-00005890: 0201 0a06 0201 0a06 0201 0a06 0201 0a06  ................
-000058a0: 0201 0a09 0201 7237 0000 0029 1672 3900  ......r7...).r9.
-000058b0: 0000 725c 0000 0072 4b00 0000 5a0d 706b  ..r\...rK...Z.pk
-000058c0: 672e 636f 6e66 6967 6972 6c72 0300 0000  g.configirlr....
-000058d0: 7204 0000 0072 0500 0000 72ad 0000 0072  r....r....r....r
-000058e0: 0600 0000 da07 6865 6c70 6572 7372 0700  ......helpersr..
-000058f0: 0000 7208 0000 0072 0900 0000 da10 6f70  ..r....r......op
-00005900: 6572 6174 696f 6e5f 7379 7374 656d 720a  eration_systemr.
-00005910: 0000 0072 0b00 0000 720c 0000 0072 0d00  ...r....r....r..
-00005920: 0000 721c 0000 0072 2c00 0000 7230 0000  ..r....r,...r0..
-00005930: 0072 3700 0000 7215 0000 0072 1500 0000  .r7...r....r....
-00005940: 7215 0000 0072 1600 0000 da08 3c6d 6f64  r....r......<mod
-00005950: 756c 653e 0300 0000 731e 0000 0008 0108  ule>....s.......
-00005960: 0108 0114 010c 0114 0514 0510 1210 1710  ................
-00005970: 1810 130a 0102 0102 0102 fd              ...........
+00005830: 0201 0a03 0201 0a09 0201 0a0a 0201 0a06  ................
+00005840: 0201 0a08 0201 0a19 0201 0a03 0201 0a0f  ................
+00005850: 0201 0a07 0201 0a10 0201 0a0f 0201 0a06  ................
+00005860: 0201 0a07 0201 0a08 0201 0a03 0201 0a03  ................
+00005870: 0201 0a06 0201 0a03 0201 0a03 0201 0a03  ................
+00005880: 0201 0a03 0201 0a03 0201 0a03 0201 0a03  ................
+00005890: 0201 0a03 0201 0a03 0201 0a04 0201 0a07  ................
+000058a0: 0201 0a0b 0201 0a03 0201 0a03 0201 0a03  ................
+000058b0: 0201 0a04 0201 0a0c 0201 0a0c 0201 0a0b  ................
+000058c0: 0201 0a0c 0201 0a0b 0201 0a0c 0201 0a0b  ................
+000058d0: 0201 0a0c 0201 0a0a 0201 0a03 0201 0a07  ................
+000058e0: 0201 0a06 0201 0a06 0201 0a06 0201 0a06  ................
+000058f0: 0201 0a06 0201 0a09 0201 7237 0000 0029  ..........r7...)
+00005900: 1672 3900 0000 725c 0000 0072 4b00 0000  .r9...r\...rK...
+00005910: 5a0d 706b 672e 636f 6e66 6967 6972 6c72  Z.pkg.configirlr
+00005920: 0300 0000 7204 0000 0072 0500 0000 72ad  ....r....r....r.
+00005930: 0000 0072 0600 0000 da07 6865 6c70 6572  ...r......helper
+00005940: 7372 0700 0000 7208 0000 0072 0900 0000  sr....r....r....
+00005950: da10 6f70 6572 6174 696f 6e5f 7379 7374  ..operation_syst
+00005960: 656d 720a 0000 0072 0b00 0000 720c 0000  emr....r....r...
+00005970: 0072 0d00 0000 721c 0000 0072 2c00 0000  .r....r....r,...
+00005980: 7230 0000 0072 3700 0000 7215 0000 0072  r0...r7...r....r
+00005990: 1500 0000 7215 0000 0072 1600 0000 da08  ....r....r......
+000059a0: 3c6d 6f64 756c 653e 0300 0000 731e 0000  <module>....s...
+000059b0: 0008 0108 0108 0114 010c 0114 0514 0510  ................
+000059c0: 1210 1710 1810 130a 0102 0102 0102 fd    ...............
```

### Comparing `pygitrepo-1.0.7/pygitrepo/actions.py` & `pygitrepo-1.0.8/pygitrepo/actions.py`

 * *Files 1% similar despite different names*

```diff
@@ -448,19 +448,22 @@
             "{cyan}Run unit test in {reset}{dir_tests}".format(
                 cyan=Fore.CYAN,
                 reset=Style.RESET_ALL,
                 dir_tests=config.dir_tests,
             )
         )
         if _dry_run is False:
+            cwd = os.getcwd()
+            os.chdir(config.dir_project_root)
             subprocess.call([
                 config.path_venv_bin_pytest,
                 config.dir_tests,
                 "-s",
             ])
+            os.chdir(cwd)
         pgr_print_done(indent=1)
 
     @subcommand(
         name="test",
         help="** Run unit test with pytest. Start over, reuse nothing.",
     )
     def test_pytest(self, config, _dry_run=False, **kwargs):  # pragma: no cover
@@ -485,22 +488,25 @@
             "{cyan}Run code coverage test in {reset}{dir_tests}".format(
                 cyan=Fore.CYAN,
                 reset=Style.RESET_ALL,
                 dir_tests=config.dir_tests,
             )
         )
         if _dry_run is False:
+            cwd = os.getcwd()
+            os.chdir(config.dir_project_root)
             subprocess.call([
                 config.path_venv_bin_pytest,
                 config.dir_tests,
                 "-s",
                 "--cov={}".format(config.PACKAGE_NAME.get_value()),
                 "--cov-report", "term-missing",
                 "--cov-report", "html:{}".format(config.dir_coverage_html),
             ])
+            os.chdir(cwd)
         pgr_print_done(indent=1)
 
     @subcommand(
         name="cov",
         help="** Run code coverage test in pytest. Start over, reuse nothing.",
     )
     def test_cov(self, config, _dry_run=False, **kwargs):  # pragma: no cover
```

### Comparing `pygitrepo-1.0.7/pygitrepo/actions.pyc` & `pygitrepo-1.0.8/pygitrepo/actions.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/cli.py` & `pygitrepo-1.0.8/pygitrepo/cli.py`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/color_print.py` & `pygitrepo-1.0.8/pygitrepo/color_print.py`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/color_print.pyc` & `pygitrepo-1.0.8/pygitrepo/color_print.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/helpers.py` & `pygitrepo-1.0.8/pygitrepo/helpers.py`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/helpers.pyc` & `pygitrepo-1.0.8/pygitrepo/helpers.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/operation_system.py` & `pygitrepo-1.0.8/pygitrepo/operation_system.py`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/operation_system.pyc` & `pygitrepo-1.0.8/pygitrepo/operation_system.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/configirl.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/configirl.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/fingerprint.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/fingerprint.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/mini_colorma.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/mini_colorma.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/__pycache__/mini_six.cpython-38.pyc` & `pygitrepo-1.0.8/pygitrepo/pkg/__pycache__/mini_six.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/configirl.py` & `pygitrepo-1.0.8/pygitrepo/pkg/configirl.py`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/configirl.pyc` & `pygitrepo-1.0.8/pygitrepo/pkg/configirl.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/fingerprint.py` & `pygitrepo-1.0.8/pygitrepo/pkg/fingerprint.py`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/fingerprint.pyc` & `pygitrepo-1.0.8/pygitrepo/pkg/fingerprint.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/mini_colorma.py` & `pygitrepo-1.0.8/pygitrepo/pkg/mini_colorma.py`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/mini_colorma.pyc` & `pygitrepo-1.0.8/pygitrepo/pkg/mini_colorma.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/mini_six.py` & `pygitrepo-1.0.8/pygitrepo/pkg/mini_six.py`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/pkg/mini_six.pyc` & `pygitrepo-1.0.8/pygitrepo/pkg/mini_six.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/repo_config.py` & `pygitrepo-1.0.8/pygitrepo/repo_config.py`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo/repo_config.pyc` & `pygitrepo-1.0.8/pygitrepo/repo_config.pyc`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/pygitrepo.egg-info/PKG-INFO` & `pygitrepo-1.0.8/pygitrepo.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,17 +1,17 @@
 Metadata-Version: 2.1
 Name: pygitrepo
-Version: 1.0.7
+Version: 1.0.8
 Summary: Package short description.
 Home-page: https://github.com/MacHu-GWU/
+Download-URL: https://pypi.python.org/pypi/pygitrepo/1.0.8#downloads
 Author: Sanhe Hu
 Author-email: husanhe@gmail.com
 Maintainer: Unknown
 License: MIT
-Download-URL: https://pypi.python.org/pypi/pygitrepo/1.0.7#downloads
 Platform: Windows
 Platform: MacOS
 Platform: Unix
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Natural Language :: English
@@ -104,9 +104,7 @@
     $ pip install pygitrepo
 
 To upgrade to latest version:
 
 .. code-block:: console
 
     $ pip install --upgrade pygitrepo
-
-
```

### Comparing `pygitrepo-1.0.7/pygitrepo.egg-info/SOURCES.txt` & `pygitrepo-1.0.8/pygitrepo.egg-info/SOURCES.txt`

 * *Files 19% similar despite different names*

```diff
@@ -55,8 +55,14 @@
 pygitrepo/pkg/mini_colorma.pyc
 pygitrepo/pkg/mini_six.py
 pygitrepo/pkg/mini_six.pyc
 pygitrepo/pkg/__pycache__/__init__.cpython-38.pyc
 pygitrepo/pkg/__pycache__/configirl.cpython-38.pyc
 pygitrepo/pkg/__pycache__/fingerprint.cpython-38.pyc
 pygitrepo/pkg/__pycache__/mini_colorma.cpython-38.pyc
-pygitrepo/pkg/__pycache__/mini_six.cpython-38.pyc
+pygitrepo/pkg/__pycache__/mini_six.cpython-38.pyc
+tests/test_actions.py
+tests/test_fingerprint.py
+tests/test_helpers.py
+tests/test_import.py
+tests/test_operation_system.py
+tests/test_repo_config.py
```

### Comparing `pygitrepo-1.0.7/release-history.rst` & `pygitrepo-1.0.8/release-history.rst`

 * *Files 4% similar despite different names*

```diff
@@ -1,24 +1,31 @@
 .. _release_history:
 
 Release and Version History
 ==============================================================================
 
 
-1.0.8 (TODO)
+1.0.9 (TODO)
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 **Features and Improvements**
 
 **Minor Improvements**
 
 **Bugfixes**
 
 **Miscellaneous**
 
 
+1.0.8 (2023-04-06)
+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+**Bugfixes**
+
+- fix a bug that the unit test is not running in the project root dir.
+
+
 1.0.7 (2022-04-02)
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 **Features and Improvements**
 
 - use ``coverage html`` for report, drop ``coverage annotate`` support.
 
 **Bugfixes**
```

### Comparing `pygitrepo-1.0.7/requirements-doc.txt` & `pygitrepo-1.0.8/requirements-doc.txt`

 * *Files identical despite different names*

### Comparing `pygitrepo-1.0.7/setup.py` & `pygitrepo-1.0.8/setup.py`

 * *Files identical despite different names*

