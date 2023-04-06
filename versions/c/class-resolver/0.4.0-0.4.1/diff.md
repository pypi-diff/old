# Comparing `tmp/class_resolver-0.4.0.tar.gz` & `tmp/class_resolver-0.4.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "class_resolver-0.4.0.tar", last modified: Wed Feb  8 22:23:04 2023, max compression
+gzip compressed data, was "class_resolver-0.4.1.tar", last modified: Thu Apr  6 14:49:55 2023, max compression
```

## Comparing `class_resolver-0.4.0.tar` & `class_resolver-0.4.1.tar`

### file list

```diff
@@ -1,60 +1,87 @@
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.978435 class_resolver-0.4.0/
--rw-r--r--   0 cthoyt     (501) staff       (20)     1076 2022-03-13 12:44:09.000000 class_resolver-0.4.0/LICENSE
--rw-r--r--   0 cthoyt     (501) staff       (20)      346 2022-03-13 12:44:09.000000 class_resolver-0.4.0/MANIFEST.in
--rw-r--r--   0 cthoyt     (501) staff       (20)    12737 2023-02-08 22:23:04.978592 class_resolver-0.4.0/PKG-INFO
--rw-r--r--   0 cthoyt     (501) staff       (20)    11262 2022-03-13 12:44:09.000000 class_resolver-0.4.0/README.md
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.954751 class_resolver-0.4.0/docs/
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.961462 class_resolver-0.4.0/docs/source/
--rw-r--r--   0 cthoyt     (501) staff       (20)     7021 2023-02-08 22:23:03.000000 class_resolver-0.4.0/docs/source/conf.py
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.962983 class_resolver-0.4.0/docs/source/contrib/
--rw-r--r--   0 cthoyt     (501) staff       (20)      176 2022-03-13 12:44:09.000000 class_resolver-0.4.0/docs/source/contrib/index.rst
--rw-r--r--   0 cthoyt     (501) staff       (20)       71 2022-03-13 12:44:09.000000 class_resolver-0.4.0/docs/source/contrib/numpy.rst
--rw-r--r--   0 cthoyt     (501) staff       (20)       74 2022-03-13 12:44:09.000000 class_resolver-0.4.0/docs/source/contrib/optuna.rst
--rw-r--r--   0 cthoyt     (501) staff       (20)       75 2022-03-13 12:44:09.000000 class_resolver-0.4.0/docs/source/contrib/torch.rst
--rw-r--r--   0 cthoyt     (501) staff       (20)      331 2022-03-13 12:44:09.000000 class_resolver-0.4.0/docs/source/index.rst
--rw-r--r--   0 cthoyt     (501) staff       (20)      539 2022-03-13 12:44:09.000000 class_resolver-0.4.0/docs/source/installation.rst
--rw-r--r--   0 cthoyt     (501) staff       (20)       67 2022-03-13 12:44:09.000000 class_resolver-0.4.0/docs/source/usage.rst
--rw-r--r--   0 cthoyt     (501) staff       (20)      358 2022-03-13 12:44:09.000000 class_resolver-0.4.0/pyproject.toml
--rw-r--r--   0 cthoyt     (501) staff       (20)     2610 2023-02-08 22:23:04.979613 class_resolver-0.4.0/setup.cfg
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.955618 class_resolver-0.4.0/src/
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.965758 class_resolver-0.4.0/src/class_resolver/
--rw-r--r--   0 cthoyt     (501) staff       (20)     2972 2023-02-07 22:09:28.000000 class_resolver-0.4.0/src/class_resolver/__init__.py
--rw-r--r--   0 cthoyt     (501) staff       (20)    13813 2022-03-13 12:44:09.000000 class_resolver-0.4.0/src/class_resolver/api.py
--rw-r--r--   0 cthoyt     (501) staff       (20)     9508 2022-04-13 12:48:56.000000 class_resolver-0.4.0/src/class_resolver/base.py
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.969925 class_resolver-0.4.0/src/class_resolver/contrib/
--rw-r--r--   0 cthoyt     (501) staff       (20)      325 2022-06-01 14:29:58.000000 class_resolver-0.4.0/src/class_resolver/contrib/__init__.py
--rw-r--r--   0 cthoyt     (501) staff       (20)     1176 2022-03-13 12:44:09.000000 class_resolver-0.4.0/src/class_resolver/contrib/numpy.py
--rw-r--r--   0 cthoyt     (501) staff       (20)     2322 2022-03-13 12:44:09.000000 class_resolver-0.4.0/src/class_resolver/contrib/optuna.py
--rw-r--r--   0 cthoyt     (501) staff       (20)     7162 2022-03-13 12:44:09.000000 class_resolver-0.4.0/src/class_resolver/contrib/torch.py
--rw-r--r--   0 cthoyt     (501) staff       (20)     1549 2022-03-13 12:44:09.000000 class_resolver-0.4.0/src/class_resolver/func.py
--rw-r--r--   0 cthoyt     (501) staff       (20)        0 2022-03-13 12:44:09.000000 class_resolver-0.4.0/src/class_resolver/py.typed
--rw-r--r--   0 cthoyt     (501) staff       (20)     6070 2023-02-08 22:15:11.000000 class_resolver-0.4.0/src/class_resolver/utils.py
--rw-r--r--   0 cthoyt     (501) staff       (20)      127 2023-02-08 22:23:03.000000 class_resolver-0.4.0/src/class_resolver/version.py
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.968249 class_resolver-0.4.0/src/class_resolver.egg-info/
--rw-r--r--   0 cthoyt     (501) staff       (20)    12737 2023-02-08 22:23:04.000000 class_resolver-0.4.0/src/class_resolver.egg-info/PKG-INFO
--rw-r--r--   0 cthoyt     (501) staff       (20)     1358 2023-02-08 22:23:04.000000 class_resolver-0.4.0/src/class_resolver.egg-info/SOURCES.txt
--rw-r--r--   0 cthoyt     (501) staff       (20)        1 2023-02-08 22:23:04.000000 class_resolver-0.4.0/src/class_resolver.egg-info/dependency_links.txt
--rw-r--r--   0 cthoyt     (501) staff       (20)      129 2023-02-08 22:23:04.000000 class_resolver-0.4.0/src/class_resolver.egg-info/entry_points.txt
--rw-r--r--   0 cthoyt     (501) staff       (20)        1 2022-03-13 12:44:53.000000 class_resolver-0.4.0/src/class_resolver.egg-info/not-zip-safe
--rw-r--r--   0 cthoyt     (501) staff       (20)      242 2023-02-08 22:23:04.000000 class_resolver-0.4.0/src/class_resolver.egg-info/requires.txt
--rw-r--r--   0 cthoyt     (501) staff       (20)       15 2023-02-08 22:23:04.000000 class_resolver-0.4.0/src/class_resolver.egg-info/top_level.txt
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.973295 class_resolver-0.4.0/tests/
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.974653 class_resolver-0.4.0/tests/.pytest_cache/
--rw-r--r--   0 cthoyt     (501) staff       (20)       37 2023-02-07 21:00:24.000000 class_resolver-0.4.0/tests/.pytest_cache/.gitignore
--rw-r--r--   0 cthoyt     (501) staff       (20)      191 2023-02-07 21:00:24.000000 class_resolver-0.4.0/tests/.pytest_cache/CACHEDIR.TAG
--rw-r--r--   0 cthoyt     (501) staff       (20)      302 2023-02-07 21:00:24.000000 class_resolver-0.4.0/tests/.pytest_cache/README.md
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.956826 class_resolver-0.4.0/tests/.pytest_cache/v/
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.976174 class_resolver-0.4.0/tests/.pytest_cache/v/cache/
--rw-r--r--   0 cthoyt     (501) staff       (20)       56 2023-02-07 21:57:34.000000 class_resolver-0.4.0/tests/.pytest_cache/v/cache/lastfailed
--rw-r--r--   0 cthoyt     (501) staff       (20)     2882 2023-02-07 22:09:36.000000 class_resolver-0.4.0/tests/.pytest_cache/v/cache/nodeids
--rw-r--r--   0 cthoyt     (501) staff       (20)        2 2023-02-07 22:09:36.000000 class_resolver-0.4.0/tests/.pytest_cache/v/cache/stepwise
--rw-r--r--   0 cthoyt     (501) staff       (20)       64 2022-03-13 12:44:09.000000 class_resolver-0.4.0/tests/__init__.py
--rw-r--r--   0 cthoyt     (501) staff       (20)      130 2022-03-13 12:44:09.000000 class_resolver-0.4.0/tests/_private_extras.py
--rw-r--r--   0 cthoyt     (501) staff       (20)    15845 2023-02-07 22:09:55.000000 class_resolver-0.4.0/tests/test_api.py
-drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-02-08 22:23:04.977985 class_resolver-0.4.0/tests/test_contrib/
--rw-r--r--   0 cthoyt     (501) staff       (20)       58 2022-03-13 12:44:09.000000 class_resolver-0.4.0/tests/test_contrib/__init__.py
--rw-r--r--   0 cthoyt     (501) staff       (20)      755 2023-02-07 21:52:07.000000 class_resolver-0.4.0/tests/test_contrib/test_numpy.py
--rw-r--r--   0 cthoyt     (501) staff       (20)     1212 2022-03-13 12:44:09.000000 class_resolver-0.4.0/tests/test_contrib/test_optuna.py
--rw-r--r--   0 cthoyt     (501) staff       (20)     2969 2022-03-13 12:44:09.000000 class_resolver-0.4.0/tests/test_contrib/test_torch.py
--rw-r--r--   0 cthoyt     (501) staff       (20)     3983 2022-03-13 12:44:09.000000 class_resolver-0.4.0/tests/test_function_resolver.py
--rw-r--r--   0 cthoyt     (501) staff       (20)     3725 2023-02-08 22:15:11.000000 class_resolver-0.4.0/tests/test_utils.py
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.224177 class_resolver-0.4.1/
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1076 2022-03-13 12:44:09.000000 class_resolver-0.4.1/LICENSE
+-rw-r--r--   0 cthoyt     (501) staff       (20)      346 2022-03-13 12:44:09.000000 class_resolver-0.4.1/MANIFEST.in
+-rw-r--r--   0 cthoyt     (501) staff       (20)    12793 2023-04-06 14:49:55.224339 class_resolver-0.4.1/PKG-INFO
+-rw-r--r--   0 cthoyt     (501) staff       (20)    11262 2022-03-13 12:44:09.000000 class_resolver-0.4.1/README.md
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.183683 class_resolver-0.4.1/docs/
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.189849 class_resolver-0.4.1/docs/source/
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.197236 class_resolver-0.4.1/docs/source/api/
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1110 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.BaseResolver.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1690 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.ClassResolver.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1174 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.FunctionResolver.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)      118 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.KeywordArgumentError.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)      109 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.RegistrationError.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)      130 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.RegistrationNameConflict.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)      139 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.RegistrationSynonymConflict.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1570 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.Resolver.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)      124 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.UnexpectedKeywordError.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)       78 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.get_cls.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)       99 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.get_subclasses.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)      105 2023-02-19 21:04:38.000000 class_resolver-0.4.1/docs/source/api/class_resolver.normalize_string.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)     7164 2023-04-06 14:49:54.000000 class_resolver-0.4.1/docs/source/conf.py
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.200292 class_resolver-0.4.1/docs/source/contrib/
+-rw-r--r--   0 cthoyt     (501) staff       (20)      187 2023-02-21 22:29:06.000000 class_resolver-0.4.1/docs/source/contrib/index.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)       71 2023-02-08 22:33:04.000000 class_resolver-0.4.1/docs/source/contrib/numpy.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)       74 2022-03-13 12:44:09.000000 class_resolver-0.4.1/docs/source/contrib/optuna.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)       87 2023-02-21 22:29:06.000000 class_resolver-0.4.1/docs/source/contrib/sklearn.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)       75 2022-03-13 12:44:09.000000 class_resolver-0.4.1/docs/source/contrib/torch.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)      331 2022-03-13 12:44:09.000000 class_resolver-0.4.1/docs/source/index.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)      539 2022-03-13 12:44:09.000000 class_resolver-0.4.1/docs/source/installation.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)       67 2023-02-08 22:33:04.000000 class_resolver-0.4.1/docs/source/usage.rst
+-rw-r--r--   0 cthoyt     (501) staff       (20)      358 2022-03-13 12:44:09.000000 class_resolver-0.4.1/pyproject.toml
+-rw-r--r--   0 cthoyt     (501) staff       (20)     2692 2023-04-06 14:49:55.225375 class_resolver-0.4.1/setup.cfg
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.184608 class_resolver-0.4.1/src/
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.204177 class_resolver-0.4.1/src/class_resolver/
+-rw-r--r--   0 cthoyt     (501) staff       (20)     2972 2023-02-08 22:33:04.000000 class_resolver-0.4.1/src/class_resolver/__init__.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)    13813 2023-02-19 20:43:34.000000 class_resolver-0.4.1/src/class_resolver/api.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)    11254 2023-02-21 22:29:06.000000 class_resolver-0.4.1/src/class_resolver/base.py
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.210233 class_resolver-0.4.1/src/class_resolver/contrib/
+-rw-r--r--   0 cthoyt     (501) staff       (20)      325 2023-02-19 20:53:52.000000 class_resolver-0.4.1/src/class_resolver/contrib/__init__.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1176 2023-02-08 22:33:04.000000 class_resolver-0.4.1/src/class_resolver/contrib/numpy.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     2322 2022-03-13 12:44:09.000000 class_resolver-0.4.1/src/class_resolver/contrib/optuna.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     2199 2023-02-21 22:29:06.000000 class_resolver-0.4.1/src/class_resolver/contrib/sklearn.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     7332 2023-04-06 14:49:37.000000 class_resolver-0.4.1/src/class_resolver/contrib/torch.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     2258 2023-02-21 22:29:06.000000 class_resolver-0.4.1/src/class_resolver/contrib/torch_geometric.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1549 2023-02-19 20:43:34.000000 class_resolver-0.4.1/src/class_resolver/func.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)        0 2022-03-13 12:44:09.000000 class_resolver-0.4.1/src/class_resolver/py.typed
+-rw-r--r--   0 cthoyt     (501) staff       (20)     6070 2023-02-08 22:33:04.000000 class_resolver-0.4.1/src/class_resolver/utils.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)      127 2023-04-06 14:49:54.000000 class_resolver-0.4.1/src/class_resolver/version.py
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.207172 class_resolver-0.4.1/src/class_resolver.egg-info/
+-rw-r--r--   0 cthoyt     (501) staff       (20)    12793 2023-04-06 14:49:55.000000 class_resolver-0.4.1/src/class_resolver.egg-info/PKG-INFO
+-rw-r--r--   0 cthoyt     (501) staff       (20)     2464 2023-04-06 14:49:55.000000 class_resolver-0.4.1/src/class_resolver.egg-info/SOURCES.txt
+-rw-r--r--   0 cthoyt     (501) staff       (20)        1 2023-04-06 14:49:55.000000 class_resolver-0.4.1/src/class_resolver.egg-info/dependency_links.txt
+-rw-r--r--   0 cthoyt     (501) staff       (20)      129 2023-04-06 14:49:55.000000 class_resolver-0.4.1/src/class_resolver.egg-info/entry_points.txt
+-rw-r--r--   0 cthoyt     (501) staff       (20)        1 2022-03-13 12:44:53.000000 class_resolver-0.4.1/src/class_resolver.egg-info/not-zip-safe
+-rw-r--r--   0 cthoyt     (501) staff       (20)      320 2023-04-06 14:49:55.000000 class_resolver-0.4.1/src/class_resolver.egg-info/requires.txt
+-rw-r--r--   0 cthoyt     (501) staff       (20)       15 2023-04-06 14:49:55.000000 class_resolver-0.4.1/src/class_resolver.egg-info/top_level.txt
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.213497 class_resolver-0.4.1/tests/
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.215560 class_resolver-0.4.1/tests/.pytest_cache/
+-rw-r--r--   0 cthoyt     (501) staff       (20)       37 2023-02-07 21:00:24.000000 class_resolver-0.4.1/tests/.pytest_cache/.gitignore
+-rw-r--r--   0 cthoyt     (501) staff       (20)      191 2023-02-07 21:00:24.000000 class_resolver-0.4.1/tests/.pytest_cache/CACHEDIR.TAG
+-rw-r--r--   0 cthoyt     (501) staff       (20)      302 2023-02-07 21:00:24.000000 class_resolver-0.4.1/tests/.pytest_cache/README.md
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.185402 class_resolver-0.4.1/tests/.pytest_cache/v/
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.217396 class_resolver-0.4.1/tests/.pytest_cache/v/cache/
+-rw-r--r--   0 cthoyt     (501) staff       (20)      111 2023-02-19 20:02:44.000000 class_resolver-0.4.1/tests/.pytest_cache/v/cache/lastfailed
+-rw-r--r--   0 cthoyt     (501) staff       (20)     3848 2023-02-21 22:57:19.000000 class_resolver-0.4.1/tests/.pytest_cache/v/cache/nodeids
+-rw-r--r--   0 cthoyt     (501) staff       (20)        2 2023-02-21 22:57:19.000000 class_resolver-0.4.1/tests/.pytest_cache/v/cache/stepwise
+-rw-r--r--   0 cthoyt     (501) staff       (20)       64 2022-03-13 12:44:09.000000 class_resolver-0.4.1/tests/__init__.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)      130 2022-03-13 12:44:09.000000 class_resolver-0.4.1/tests/_private_extras.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)    17352 2023-02-21 22:29:06.000000 class_resolver-0.4.1/tests/test_api.py
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.220164 class_resolver-0.4.1/tests/test_contrib/
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.221867 class_resolver-0.4.1/tests/test_contrib/.pytest_cache/
+-rw-r--r--   0 cthoyt     (501) staff       (20)       37 2023-02-19 19:18:56.000000 class_resolver-0.4.1/tests/test_contrib/.pytest_cache/.gitignore
+-rw-r--r--   0 cthoyt     (501) staff       (20)      191 2023-02-19 19:18:56.000000 class_resolver-0.4.1/tests/test_contrib/.pytest_cache/CACHEDIR.TAG
+-rw-r--r--   0 cthoyt     (501) staff       (20)      302 2023-02-19 19:18:56.000000 class_resolver-0.4.1/tests/test_contrib/.pytest_cache/README.md
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.185998 class_resolver-0.4.1/tests/test_contrib/.pytest_cache/v/
+drwxr-xr-x   0 cthoyt     (501) staff       (20)        0 2023-04-06 14:49:55.223651 class_resolver-0.4.1/tests/test_contrib/.pytest_cache/v/cache/
+-rw-r--r--   0 cthoyt     (501) staff       (20)       37 2023-02-19 20:56:24.000000 class_resolver-0.4.1/tests/test_contrib/.pytest_cache/v/cache/lastfailed
+-rw-r--r--   0 cthoyt     (501) staff       (20)      173 2023-02-19 20:59:32.000000 class_resolver-0.4.1/tests/test_contrib/.pytest_cache/v/cache/nodeids
+-rw-r--r--   0 cthoyt     (501) staff       (20)        2 2023-02-19 20:59:32.000000 class_resolver-0.4.1/tests/test_contrib/.pytest_cache/v/cache/stepwise
+-rw-r--r--   0 cthoyt     (501) staff       (20)       58 2022-03-13 12:44:09.000000 class_resolver-0.4.1/tests/test_contrib/__init__.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)      755 2023-02-08 22:33:04.000000 class_resolver-0.4.1/tests/test_contrib/test_numpy.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1212 2022-03-13 12:44:09.000000 class_resolver-0.4.1/tests/test_contrib/test_optuna.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1421 2023-02-21 22:29:06.000000 class_resolver-0.4.1/tests/test_contrib/test_sklearn.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     2969 2022-03-13 12:44:09.000000 class_resolver-0.4.1/tests/test_contrib/test_torch.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     1365 2023-02-21 22:29:06.000000 class_resolver-0.4.1/tests/test_contrib/test_torch_geometric.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     3983 2023-02-19 20:43:34.000000 class_resolver-0.4.1/tests/test_function_resolver.py
+-rw-r--r--   0 cthoyt     (501) staff       (20)     3725 2023-02-08 22:33:04.000000 class_resolver-0.4.1/tests/test_utils.py
```

### Comparing `class_resolver-0.4.0/LICENSE` & `class_resolver-0.4.1/LICENSE`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/PKG-INFO` & `class_resolver-0.4.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: class_resolver
-Version: 0.4.0
+Version: 0.4.1
 Summary: Lookup and instantiate classes with style.
 Home-page: https://github.com/cthoyt/class-resolver
 Download-URL: https://github.com/cthoyt/class-resolver/releases
 Author: Charles Tapley Hoyt
 Author-email: cthoyt@gmail.com
 Maintainer: Charles Tapley Hoyt
 Maintainer-email: cthoyt@gmail.com
@@ -31,16 +31,18 @@
 Description-Content-Type: text/markdown
 Provides-Extra: click
 Provides-Extra: docs
 Provides-Extra: tests
 Provides-Extra: docdata
 Provides-Extra: ray
 Provides-Extra: torch
+Provides-Extra: torch-geometric
 Provides-Extra: optuna
 Provides-Extra: numpy
+Provides-Extra: sklearn
 License-File: LICENSE
 
 <!--
 <p align="center">
   <img src="docs/source/logo.png" height="150">
 </p>
 -->
```

### Comparing `class_resolver-0.4.0/README.md` & `class_resolver-0.4.1/README.md`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/docs/source/conf.py` & `class_resolver-0.4.1/docs/source/conf.py`

 * *Files 2% similar despite different names*

```diff
@@ -28,15 +28,15 @@
 # -- Project information -----------------------------------------------------
 
 project = 'class_resolver'
 copyright = f'{date.today().year}, Charles Tapley Hoyt'
 author = 'Charles Tapley Hoyt'
 
 # The full version, including alpha/beta/rc tags.
-release = '0.4.0'
+release = '0.4.1'
 
 # The short X.Y version.
 parsed_version = re.match(
     '(?P<major>\d+)\.(?P<minor>\d+)\.(?P<patch>\d+)(?:-(?P<release>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+(?P<build>[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?',
     release,
 )
 version = parsed_version.expand('\g<major>.\g<minor>.\g<patch>')
@@ -226,12 +226,14 @@
 
 # -- Options for intersphinx extension ---------------------------------------
 
 # Example configuration for intersphinx: refer to the Python standard library.
 intersphinx_mapping = {
     'https://docs.python.org/3/': None,
     'torch': ('https://pytorch.org/docs/stable', None),
+    'torch_geometric': ('https://pytorch-geometric.readthedocs.io/en/latest', None),
     'numpy': ('https://numpy.org/doc/stable', None),
     'optuna': ('https://optuna.readthedocs.io/en/latest', None),
+    'sklearn': ('https://scikit-learn.org/stable', None),
 }
 
 autoclass_content = 'both'
```

### Comparing `class_resolver-0.4.0/docs/source/installation.rst` & `class_resolver-0.4.1/docs/source/installation.rst`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/setup.cfg` & `class_resolver-0.4.1/setup.cfg`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = class_resolver
-version = 0.4.0
+version = 0.4.1
 description = Lookup and instantiate classes with style.
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/cthoyt/class-resolver
 download_url = https://github.com/cthoyt/class-resolver/releases
 project_urls = 
 	Bug Tracker = https://github.com/cthoyt/class-resolver/issues
@@ -60,18 +60,24 @@
 	pytest
 docdata = 
 	docdata
 ray = 
 	ray[tune]<2.0.0; python_version < "3.9"
 torch = 
 	torch
+torch-geometric = 
+	torch
+	torch-sparse
+	torch-geometric
 optuna = 
 	optuna
 numpy = 
 	numpy
+sklearn = 
+	scikit-learn
 
 [options.entry_points]
 class_resolver_demo = 
 	add = operator:add
 	sub = operator:sub
 	mul = operator:mul
 	expected_failure = operator:nope_this_is_not_real
```

### Comparing `class_resolver-0.4.0/src/class_resolver/__init__.py` & `class_resolver-0.4.1/src/class_resolver/__init__.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/src/class_resolver/api.py` & `class_resolver-0.4.1/src/class_resolver/api.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/src/class_resolver/base.py` & `class_resolver-0.4.1/src/class_resolver/base.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,19 +1,32 @@
 # -*- coding: utf-8 -*-
 
 """A base resolver."""
 
 import logging
 from abc import ABC, abstractmethod
-from typing import Collection, Dict, Generic, Iterable, Iterator, Mapping, Optional, Set
+from typing import (
+    TYPE_CHECKING,
+    Collection,
+    Dict,
+    Generic,
+    Iterable,
+    Iterator,
+    Mapping,
+    Optional,
+    Set,
+)
 
 from pkg_resources import iter_entry_points
 
 from .utils import Hint, OptionalKwargs, X, Y, make_callback, normalize_string
 
+if TYPE_CHECKING:
+    import optuna
+
 __all__ = [
     "BaseResolver",
     "RegistrationError",
     "RegistrationNameConflict",
     "RegistrationSynonymConflict",
 ]
 
@@ -257,7 +270,45 @@
         return elements
 
     @classmethod
     def from_entrypoint(cls, group: str, **kwargs) -> "BaseResolver":
         """Make a resolver from the elements registered at the given entrypoint."""
         elements = cls._from_entrypoint(group)
         return cls(elements, **kwargs)
+
+    def optuna_lookup(self, trial: "optuna.Trial", name: str) -> X:
+        """Suggest an element from this resolver for hyper-parameter optimization in Optuna.
+
+        :param trial: A trial object from :mod:`optuna`. Note that this object shouldn't be constructed
+            by the developer, and should only get constructed inside the optuna framework when
+            using :meth:`optuna.Study.optimize`.
+        :param name: The name of the `param` within an optuna study.
+        :returns: An element chosen by optuna, then run through :func:`lookup`.
+
+        In the following example, Optuna is used to determine the best classification
+        algorithm from scikit-learn when applied to the famous iris dataset.
+
+        .. code-block::
+
+            import optuna
+            from sklearn import datasets
+            from sklearn.model_selection import train_test_split
+
+            from class_resolver.contrib.sklearn import classifier_resolver
+
+
+            def objective(trial: optuna.Trial) -> float:
+                x, y = datasets.load_iris(return_X_y=True)
+                x_train, x_test, y_train, y_test = train_test_split(
+                    x, y, test_size=0.33, random_state=42,
+                )
+                clf_cls = classifier_resolver.optuna_lookup(trial, "model")
+                clf = clf_cls()
+                clf.fit(x_train, y_train)
+                return clf.score(x_test, y_test)
+
+
+            study = optuna.create_study(direction="maximize")
+            study.optimize(objective, n_trials=100)
+        """
+        key = trial.suggest_categorical(name, sorted(self.lookup_dict))
+        return self.lookup(key)
```

### Comparing `class_resolver-0.4.0/src/class_resolver/contrib/numpy.py` & `class_resolver-0.4.1/src/class_resolver/contrib/numpy.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/src/class_resolver/contrib/optuna.py` & `class_resolver-0.4.1/src/class_resolver/contrib/optuna.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/src/class_resolver/contrib/torch.py` & `class_resolver-0.4.1/src/class_resolver/contrib/torch.py`

 * *Files 2% similar despite different names*

```diff
@@ -7,15 +7,22 @@
 """  # noqa:D205,D400
 
 import torch
 from torch import nn
 from torch.nn import init
 from torch.nn.modules import activation
 from torch.optim import Adam, Optimizer
-from torch.optim.lr_scheduler import ExponentialLR, ReduceLROnPlateau, _LRScheduler
+from torch.optim.lr_scheduler import ExponentialLR, ReduceLROnPlateau
+
+try:
+    # torch >= 2.0
+    from torch.optim.lr_scheduler import LRScheduler
+except ImportError:
+    # torch < 2.0
+    from torch.optim.lr_scheduler import _LRScheduler as LRScheduler
 
 from ..api import ClassResolver
 from ..func import FunctionResolver
 
 __all__ = [
     "optimizer_resolver",
     "activation_resolver",
@@ -152,15 +159,15 @@
             x = F.relu(x)
             x = self.layer_2(x)
             x = F.relu(x)
             return x
 """
 
 lr_scheduler_resolver = ClassResolver.from_subclasses(
-    _LRScheduler,
+    LRScheduler,
     default=ExponentialLR,
     suffix="LR",
 )
 """A resolver for learning rate schedulers.
 
 Borrowing from the PyTorch documentation's example on `how to adjust the learning
 rate <https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate>`_,
```

### Comparing `class_resolver-0.4.0/src/class_resolver/func.py` & `class_resolver-0.4.1/src/class_resolver/func.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/src/class_resolver/utils.py` & `class_resolver-0.4.1/src/class_resolver/utils.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/src/class_resolver.egg-info/PKG-INFO` & `class_resolver-0.4.1/src/class_resolver.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: class-resolver
-Version: 0.4.0
+Version: 0.4.1
 Summary: Lookup and instantiate classes with style.
 Home-page: https://github.com/cthoyt/class-resolver
 Download-URL: https://github.com/cthoyt/class-resolver/releases
 Author: Charles Tapley Hoyt
 Author-email: cthoyt@gmail.com
 Maintainer: Charles Tapley Hoyt
 Maintainer-email: cthoyt@gmail.com
@@ -31,16 +31,18 @@
 Description-Content-Type: text/markdown
 Provides-Extra: click
 Provides-Extra: docs
 Provides-Extra: tests
 Provides-Extra: docdata
 Provides-Extra: ray
 Provides-Extra: torch
+Provides-Extra: torch-geometric
 Provides-Extra: optuna
 Provides-Extra: numpy
+Provides-Extra: sklearn
 License-File: LICENSE
 
 <!--
 <p align="center">
   <img src="docs/source/logo.png" height="150">
 </p>
 -->
```

### Comparing `class_resolver-0.4.0/src/class_resolver.egg-info/SOURCES.txt` & `class_resolver-0.4.1/src/class_resolver.egg-info/SOURCES.txt`

 * *Files 22% similar despite different names*

```diff
@@ -3,17 +3,30 @@
 README.md
 pyproject.toml
 setup.cfg
 docs/source/conf.py
 docs/source/index.rst
 docs/source/installation.rst
 docs/source/usage.rst
+docs/source/api/class_resolver.BaseResolver.rst
+docs/source/api/class_resolver.ClassResolver.rst
+docs/source/api/class_resolver.FunctionResolver.rst
+docs/source/api/class_resolver.KeywordArgumentError.rst
+docs/source/api/class_resolver.RegistrationError.rst
+docs/source/api/class_resolver.RegistrationNameConflict.rst
+docs/source/api/class_resolver.RegistrationSynonymConflict.rst
+docs/source/api/class_resolver.Resolver.rst
+docs/source/api/class_resolver.UnexpectedKeywordError.rst
+docs/source/api/class_resolver.get_cls.rst
+docs/source/api/class_resolver.get_subclasses.rst
+docs/source/api/class_resolver.normalize_string.rst
 docs/source/contrib/index.rst
 docs/source/contrib/numpy.rst
 docs/source/contrib/optuna.rst
+docs/source/contrib/sklearn.rst
 docs/source/contrib/torch.rst
 src/class_resolver/__init__.py
 src/class_resolver/api.py
 src/class_resolver/base.py
 src/class_resolver/func.py
 src/class_resolver/py.typed
 src/class_resolver/utils.py
@@ -24,23 +37,33 @@
 src/class_resolver.egg-info/entry_points.txt
 src/class_resolver.egg-info/not-zip-safe
 src/class_resolver.egg-info/requires.txt
 src/class_resolver.egg-info/top_level.txt
 src/class_resolver/contrib/__init__.py
 src/class_resolver/contrib/numpy.py
 src/class_resolver/contrib/optuna.py
+src/class_resolver/contrib/sklearn.py
 src/class_resolver/contrib/torch.py
+src/class_resolver/contrib/torch_geometric.py
 tests/__init__.py
 tests/_private_extras.py
 tests/test_api.py
 tests/test_function_resolver.py
 tests/test_utils.py
 tests/.pytest_cache/.gitignore
 tests/.pytest_cache/CACHEDIR.TAG
 tests/.pytest_cache/README.md
 tests/.pytest_cache/v/cache/lastfailed
 tests/.pytest_cache/v/cache/nodeids
 tests/.pytest_cache/v/cache/stepwise
 tests/test_contrib/__init__.py
 tests/test_contrib/test_numpy.py
 tests/test_contrib/test_optuna.py
-tests/test_contrib/test_torch.py
+tests/test_contrib/test_sklearn.py
+tests/test_contrib/test_torch.py
+tests/test_contrib/test_torch_geometric.py
+tests/test_contrib/.pytest_cache/.gitignore
+tests/test_contrib/.pytest_cache/CACHEDIR.TAG
+tests/test_contrib/.pytest_cache/README.md
+tests/test_contrib/.pytest_cache/v/cache/lastfailed
+tests/test_contrib/.pytest_cache/v/cache/nodeids
+tests/test_contrib/.pytest_cache/v/cache/stepwise
```

### Comparing `class_resolver-0.4.0/tests/.pytest_cache/v/cache/nodeids` & `class_resolver-0.4.1/tests/.pytest_cache/v/cache/nodeids`

 * *Files 18% similar despite different names*

#### Pretty-printed

 * *Similarity: 0.78125%*

 * *Differences: {'insert': "[(19, 'test_api.py::TestResolver::test_optuna_suggest'), (27, "*

 * *           "'test_api.py::TestResolver::test_subresolver'), (34, "*

 * *           "'test_contrib/test_sklearn.py::TestSklearn::test_classifier_resolver'), (40, "*

 * *           "'test_contrib/test_torch_geometric.py::TestTorch::test_aggregation'), (41, "*

 * *           "'test_contrib/test_torch_geometric.py::TestTorch::test_message_passing'), (52, "*

 * *           "'test_function_resolver.py::TestFunctionResolver::test_subresolver'), (53, "*

 * *        […]*

```diff
@@ -14,39 +14,53 @@
     "test_api.py::TestResolver::test_make",
     "test_api.py::TestResolver::test_make_from_kwargs",
     "test_api.py::TestResolver::test_make_many",
     "test_api.py::TestResolver::test_make_safe",
     "test_api.py::TestResolver::test_missing_kwarg",
     "test_api.py::TestResolver::test_no_arguments",
     "test_api.py::TestResolver::test_normalize",
+    "test_api.py::TestResolver::test_optuna_suggest",
     "test_api.py::TestResolver::test_passthrough",
     "test_api.py::TestResolver::test_registration_empty_synonym_failure",
     "test_api.py::TestResolver::test_registration_name_failure",
     "test_api.py::TestResolver::test_registration_synonym",
     "test_api.py::TestResolver::test_registration_synonym_failure",
     "test_api.py::TestResolver::test_required_click_option",
     "test_api.py::TestResolver::test_signature",
+    "test_api.py::TestResolver::test_subresolver",
     "test_api.py::TestResolver::test_unexpected_error",
     "test_api.py::TestResolver::test_variant_generation",
     "test_api.py::TestResolver::test_version",
     "test_contrib/test_numpy.py::TestNumpy::test_activation",
     "test_contrib/test_optuna.py::TestTorch::test_pruner",
     "test_contrib/test_optuna.py::TestTorch::test_sampler",
+    "test_contrib/test_sklearn.py::TestSklearn::test_classifier_resolver",
     "test_contrib/test_torch.py::TestTorch::test_activation",
     "test_contrib/test_torch.py::TestTorch::test_initializer",
     "test_contrib/test_torch.py::TestTorch::test_lr",
     "test_contrib/test_torch.py::TestTorch::test_margin_activation",
     "test_contrib/test_torch.py::TestTorch::test_optimizer",
+    "test_contrib/test_torch_geometric.py::TestTorch::test_aggregation",
+    "test_contrib/test_torch_geometric.py::TestTorch::test_message_passing",
     "test_function_resolver.py::TestFunctionResolver::test_contents",
     "test_function_resolver.py::TestFunctionResolver::test_default_lookup",
     "test_function_resolver.py::TestFunctionResolver::test_entrypoints",
     "test_function_resolver.py::TestFunctionResolver::test_late_entrypoints",
     "test_function_resolver.py::TestFunctionResolver::test_lookup",
     "test_function_resolver.py::TestFunctionResolver::test_make",
     "test_function_resolver.py::TestFunctionResolver::test_make_safe",
     "test_function_resolver.py::TestFunctionResolver::test_passthrough",
     "test_function_resolver.py::TestFunctionResolver::test_registration_failure",
     "test_function_resolver.py::TestFunctionResolver::test_registration_synonym",
+    "test_function_resolver.py::TestFunctionResolver::test_subresolver",
+    "test_metaresolver.py::TestMetaResolver::test_annotation_extended_origin_mismatch",
+    "test_metaresolver.py::TestMetaResolver::test_annotation_extended_origin_mismatch_2",
+    "test_metaresolver.py::TestMetaResolver::test_annotation_invalid_origin",
+    "test_metaresolver.py::TestMetaResolver::test_annotation_mismatch",
+    "test_metaresolver.py::TestMetaResolver::test_annotation_resolver_mismatch",
+    "test_metaresolver.py::TestMetaResolver::test_argument_checker",
+    "test_metaresolver.py::TestMetaResolver::test_is_hint",
     "test_utils.py::TestUtilities::test_get_subclasses",
+    "test_utils.py::TestUtilities::test_is_private",
     "test_utils.py::TestUtilities::test_normalize_with_defaults",
     "test_utils.py::TestUtilities::test_same_module"
 ]
```

### Comparing `class_resolver-0.4.0/tests/test_api.py` & `class_resolver-0.4.1/tests/test_api.py`

 * *Files 9% similar despite different names*

```diff
@@ -8,26 +8,37 @@
 
 import click
 from click.testing import CliRunner, Result
 from docdata import parse_docdata
 
 from class_resolver import (
     VERSION,
+    ClassResolver,
     KeywordArgumentError,
     RegistrationNameConflict,
     RegistrationSynonymConflict,
     Resolver,
     UnexpectedKeywordError,
 )
 
 try:
     import ray.tune as tune
 except ImportError:
     tune = None
 
+try:
+    import optuna
+except ImportError:
+    optuna = None
+
+try:
+    import sklearn
+except ImportError:
+    sklearn = None
+
 
 class Base:
     """A base class."""
 
     def __init__(self, name: str):
         """Initialize the class."""
         self.name = name
@@ -238,14 +249,49 @@
             tune.suggest.variant_generator.generate_variants(search_space), 2
         ):
             config = {k[0]: v for k, v in spec[0].items()}
             query = config.pop("query")
             instance = self.resolver.make(query=query, pos_kwargs=config)
             self.assertIsInstance(instance, Base)
 
+    @unittest.skipIf(optuna is None, "optuna is not installed")
+    @unittest.skipIf(sklearn is None, "sklearn is not installed")
+    def test_optuna_suggest(self):
+        """Test suggesting categorical for optuna."""
+        import optuna
+        from sklearn import datasets
+        from sklearn.base import BaseEstimator
+        from sklearn.ensemble import RandomForestClassifier
+        from sklearn.linear_model import LogisticRegression
+        from sklearn.model_selection import train_test_split
+
+        resolver = ClassResolver(
+            [
+                LogisticRegression,
+                RandomForestClassifier,
+            ],
+            base=BaseEstimator,
+            base_as_suffix=False,
+            default=LogisticRegression,
+        )
+
+        def objective(trial: optuna.Trial) -> float:
+            """Calculate the classification accuracy for the iris dataset."""
+            x, y = datasets.load_iris(return_X_y=True)
+            x_train, x_test, y_train, y_test = train_test_split(
+                x, y, test_size=0.33, random_state=42
+            )
+            clf_cls = resolver.optuna_lookup(trial, "model")
+            clf = clf_cls()
+            clf.fit(x_train, y_train)
+            return clf.score(x_test, y_test)
+
+        study = optuna.create_study(direction="maximize")
+        study.optimize(objective, n_trials=100)
+
     def test_bad_click_option(self):
         """Test failure to get a click option."""
         with self.assertRaises(ValueError):
             self.resolver.get_option("--opt")  # no default given
 
     def test_required_click_option(self):
         """Test non-failure to get a required click option without default."""
```

### Comparing `class_resolver-0.4.0/tests/test_contrib/test_numpy.py` & `class_resolver-0.4.1/tests/test_contrib/test_numpy.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/tests/test_contrib/test_optuna.py` & `class_resolver-0.4.1/tests/test_contrib/test_optuna.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/tests/test_contrib/test_torch.py` & `class_resolver-0.4.1/tests/test_contrib/test_torch.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/tests/test_function_resolver.py` & `class_resolver-0.4.1/tests/test_function_resolver.py`

 * *Files identical despite different names*

### Comparing `class_resolver-0.4.0/tests/test_utils.py` & `class_resolver-0.4.1/tests/test_utils.py`

 * *Files identical despite different names*

