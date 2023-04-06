# Comparing `tmp/zest.releaser-8.0.0a1.tar.gz` & `tmp/zest.releaser-8.0.0a2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "zest.releaser-8.0.0a1.tar", last modified: Wed Feb  8 22:32:02 2023, max compression
+gzip compressed data, was "zest.releaser-8.0.0a2.tar", last modified: Thu Apr  6 15:46:36 2023, max compression
```

## Comparing `zest.releaser-8.0.0a1.tar` & `zest.releaser-8.0.0a2.tar`

### file list

```diff
@@ -1,89 +1,88 @@
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-02-08 22:32:02.790995 zest.releaser-8.0.0a1/
--rw-r--r--   0 maurits    (501) staff       (20)     2444 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/CHANGES.rst
--rw-r--r--   0 maurits    (501) staff       (20)     1288 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/CONTRIBUTING.rst
--rw-r--r--   0 maurits    (501) staff       (20)      938 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/CREDITS.rst
--rw-r--r--   0 maurits    (501) staff       (20)    17987 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/LICENSE.GPL
--rw-r--r--   0 maurits    (501) staff       (20)      756 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/LICENSE.rst
--rw-r--r--   0 maurits    (501) staff       (20)      149 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/MANIFEST.in
--rw-r--r--   0 maurits    (501) staff       (20)    13262 2023-02-08 22:32:02.791122 zest.releaser-8.0.0a1/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)     8496 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/README.rst
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-02-08 22:32:02.766895 zest.releaser-8.0.0a1/doc/
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-02-08 22:32:02.774679 zest.releaser-8.0.0a1/doc/source/
--rw-r--r--   0 maurits    (501) staff       (20)     1804 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/assumptions.rst
--rw-r--r--   0 maurits    (501) staff       (20)    50612 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/changelog.rst
--rw-r--r--   0 maurits    (501) staff       (20)     6911 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/conf.py
--rw-r--r--   0 maurits    (501) staff       (20)       32 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/credits.rst
--rw-r--r--   0 maurits    (501) staff       (20)     3355 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/developing.rst
--rw-r--r--   0 maurits    (501) staff       (20)     7705 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/entrypoints.rst
--rw-r--r--   0 maurits    (501) staff       (20)     1265 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/further_reading.rst
--rw-r--r--   0 maurits    (501) staff       (20)      837 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/index.rst
--rw-r--r--   0 maurits    (501) staff       (20)     6754 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/options.rst
--rw-r--r--   0 maurits    (501) staff       (20)       30 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/overview.rst
--rw-r--r--   0 maurits    (501) staff       (20)     1165 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/project.rst
--rw-r--r--   0 maurits    (501) staff       (20)     9536 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/uploading.rst
--rw-r--r--   0 maurits    (501) staff       (20)     3360 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/doc/source/versions.rst
--rw-r--r--   0 maurits    (501) staff       (20)     3204 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/pyproject.toml
--rw-r--r--   0 maurits    (501) staff       (20)      340 2023-02-08 22:32:02.791761 zest.releaser-8.0.0a1/setup.cfg
--rw-r--r--   0 maurits    (501) staff       (20)      191 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/setup.py
--rw-r--r--   0 maurits    (501) staff       (20)      229 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/tox.ini
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-02-08 22:32:02.774965 zest.releaser-8.0.0a1/zest/
--rw-r--r--   0 maurits    (501) staff       (20)      245 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-02-08 22:32:02.782147 zest.releaser-8.0.0a1/zest/releaser/
--rw-r--r--   0 maurits    (501) staff       (20)      398 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     3063 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/addchangelogentry.py
--rw-r--r--   0 maurits    (501) staff       (20)    18151 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/baserelease.py
--rw-r--r--   0 maurits    (501) staff       (20)     6267 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/bumpversion.py
--rw-r--r--   0 maurits    (501) staff       (20)     1241 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/choose.py
--rw-r--r--   0 maurits    (501) staff       (20)      962 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/fullrelease.py
--rw-r--r--   0 maurits    (501) staff       (20)     4159 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/git.py
--rw-r--r--   0 maurits    (501) staff       (20)      831 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/lasttagdiff.py
--rw-r--r--   0 maurits    (501) staff       (20)      833 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/lasttaglog.py
--rw-r--r--   0 maurits    (501) staff       (20)     2309 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/longtest.py
--rw-r--r--   0 maurits    (501) staff       (20)     5132 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/postrelease.py
--rw-r--r--   0 maurits    (501) staff       (20)     2146 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/preparedocs.py
--rw-r--r--   0 maurits    (501) staff       (20)     4533 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/prerelease.py
--rw-r--r--   0 maurits    (501) staff       (20)    24621 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/pypi.py
--rw-r--r--   0 maurits    (501) staff       (20)    12986 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/release.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-02-08 22:32:02.790814 zest.releaser-8.0.0a1/zest/releaser/tests/
--rw-r--r--   0 maurits    (501) staff       (20)       10 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     3657 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/addchangelogentry.txt
--rw-r--r--   0 maurits    (501) staff       (20)     4318 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/baserelease.txt
--rw-r--r--   0 maurits    (501) staff       (20)     4598 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/bumpversion.txt
--rw-r--r--   0 maurits    (501) staff       (20)     1199 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/choose.txt
--rw-r--r--   0 maurits    (501) staff       (20)      121 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/cmd_error.py
--rw-r--r--   0 maurits    (501) staff       (20)    20480 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/example.tar
--rw-r--r--   0 maurits    (501) staff       (20)     3166 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/fullrelease.txt
--rw-r--r--   0 maurits    (501) staff       (20)     4126 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/functional-git.txt
--rw-r--r--   0 maurits    (501) staff       (20)     4200 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/functional-with-hooks.txt
--rw-r--r--   0 maurits    (501) staff       (20)     4322 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/functional.py
--rw-r--r--   0 maurits    (501) staff       (20)     5670 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/git.txt
--rw-r--r--   0 maurits    (501) staff       (20)     9742 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/postrelease.txt
--rw-r--r--   0 maurits    (501) staff       (20)     1891 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/preparedocs.txt
--rw-r--r--   0 maurits    (501) staff       (20)     1172 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/prerelease.txt
--rw-r--r--   0 maurits    (501) staff       (20)    12926 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypi.txt
--rw-r--r--   0 maurits    (501) staff       (20)      203 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypirc_both.txt
--rw-r--r--   0 maurits    (501) staff       (20)      341 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypirc_new.txt
--rw-r--r--   0 maurits    (501) staff       (20)      109 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypirc_no_input.txt
--rw-r--r--   0 maurits    (501) staff       (20)      107 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypirc_no_release.txt
--rw-r--r--   0 maurits    (501) staff       (20)      123 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypirc_old.txt
--rw-r--r--   0 maurits    (501) staff       (20)       37 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypirc_simple.txt
--rw-r--r--   0 maurits    (501) staff       (20)      137 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypirc_universal_create.txt
--rw-r--r--   0 maurits    (501) staff       (20)      155 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypirc_universal_nocreate.txt
--rw-r--r--   0 maurits    (501) staff       (20)      127 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pypirc_yes_release.txt
--rw-r--r--   0 maurits    (501) staff       (20)     4240 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pyproject-toml.txt
--rw-r--r--   0 maurits    (501) staff       (20)      400 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/pyproject.toml
--rw-r--r--   0 maurits    (501) staff       (20)     3118 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/release.txt
--rw-r--r--   0 maurits    (501) staff       (20)     2791 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/test_setup.py
--rw-r--r--   0 maurits    (501) staff       (20)    22286 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/utils.txt
--rw-r--r--   0 maurits    (501) staff       (20)     9600 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/tests/vcs.txt
--rw-r--r--   0 maurits    (501) staff       (20)    32025 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/utils.py
--rw-r--r--   0 maurits    (501) staff       (20)    17236 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest/releaser/vcs.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-02-08 22:32:02.777261 zest.releaser-8.0.0a1/zest.releaser.egg-info/
--rw-r--r--   0 maurits    (501) staff       (20)    13262 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest.releaser.egg-info/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)     2349 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest.releaser.egg-info/SOURCES.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest.releaser.egg-info/dependency_links.txt
--rw-r--r--   0 maurits    (501) staff       (20)      951 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest.releaser.egg-info/entry_points.txt
--rw-r--r--   0 maurits    (501) staff       (20)        5 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest.releaser.egg-info/namespace_packages.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest.releaser.egg-info/not-zip-safe
--rw-r--r--   0 maurits    (501) staff       (20)      185 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest.releaser.egg-info/requires.txt
--rw-r--r--   0 maurits    (501) staff       (20)        5 2023-02-08 22:32:02.000000 zest.releaser-8.0.0a1/zest.releaser.egg-info/top_level.txt
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 15:46:36.353483 zest.releaser-8.0.0a2/
+-rw-r--r--   0 maurits    (501) staff       (20)     3034 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/CHANGES.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     1288 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/CONTRIBUTING.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      938 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/CREDITS.rst
+-rw-r--r--   0 maurits    (501) staff       (20)    17987 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/LICENSE.GPL
+-rw-r--r--   0 maurits    (501) staff       (20)      756 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/LICENSE.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      149 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/MANIFEST.in
+-rw-r--r--   0 maurits    (501) staff       (20)    13852 2023-04-06 15:46:36.353715 zest.releaser-8.0.0a2/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)     8496 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/README.rst
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 15:46:36.317024 zest.releaser-8.0.0a2/doc/
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 15:46:36.328550 zest.releaser-8.0.0a2/doc/source/
+-rw-r--r--   0 maurits    (501) staff       (20)     1804 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/assumptions.rst
+-rw-r--r--   0 maurits    (501) staff       (20)    50612 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/changelog.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     6911 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/conf.py
+-rw-r--r--   0 maurits    (501) staff       (20)       32 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/credits.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     3355 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/developing.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     7705 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/entrypoints.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     1265 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/further_reading.rst
+-rw-r--r--   0 maurits    (501) staff       (20)      837 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/index.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     6754 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/options.rst
+-rw-r--r--   0 maurits    (501) staff       (20)       30 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/overview.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     1165 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/project.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     9536 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/uploading.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     3360 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/doc/source/versions.rst
+-rw-r--r--   0 maurits    (501) staff       (20)     3204 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/pyproject.toml
+-rw-r--r--   0 maurits    (501) staff       (20)      340 2023-04-06 15:46:36.354517 zest.releaser-8.0.0a2/setup.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)      191 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/setup.py
+-rw-r--r--   0 maurits    (501) staff       (20)      229 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/tox.ini
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 15:46:36.328976 zest.releaser-8.0.0a2/zest/
+-rw-r--r--   0 maurits    (501) staff       (20)      245 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 15:46:36.340119 zest.releaser-8.0.0a2/zest/releaser/
+-rw-r--r--   0 maurits    (501) staff       (20)      398 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3063 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/addchangelogentry.py
+-rw-r--r--   0 maurits    (501) staff       (20)    18151 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/baserelease.py
+-rw-r--r--   0 maurits    (501) staff       (20)     6267 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/bumpversion.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1241 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/choose.py
+-rw-r--r--   0 maurits    (501) staff       (20)      962 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/fullrelease.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4159 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/git.py
+-rw-r--r--   0 maurits    (501) staff       (20)      831 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/lasttagdiff.py
+-rw-r--r--   0 maurits    (501) staff       (20)      833 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/lasttaglog.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2309 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/longtest.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5132 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/postrelease.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2146 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/preparedocs.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4533 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/prerelease.py
+-rw-r--r--   0 maurits    (501) staff       (20)    24132 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/pypi.py
+-rw-r--r--   0 maurits    (501) staff       (20)    12986 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/release.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 15:46:36.353155 zest.releaser-8.0.0a2/zest/releaser/tests/
+-rw-r--r--   0 maurits    (501) staff       (20)       10 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3657 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/addchangelogentry.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     4318 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/baserelease.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     4598 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/bumpversion.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1199 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/choose.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      121 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/cmd_error.py
+-rw-r--r--   0 maurits    (501) staff       (20)    20480 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/example.tar
+-rw-r--r--   0 maurits    (501) staff       (20)     3166 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/fullrelease.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     4124 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/functional-git.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     4200 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/functional-with-hooks.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     4336 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/functional.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5662 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/git.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     9742 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/postrelease.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1891 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/preparedocs.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1172 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/prerelease.txt
+-rw-r--r--   0 maurits    (501) staff       (20)    12003 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pypi.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      203 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pypirc_both.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      341 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pypirc_new.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      109 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pypirc_no_input.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      107 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pypirc_no_release.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      123 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pypirc_old.txt
+-rw-r--r--   0 maurits    (501) staff       (20)       37 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pypirc_simple.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      155 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pypirc_universal_nocreate.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      127 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pypirc_yes_release.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     4236 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pyproject-toml.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      400 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/pyproject.toml
+-rw-r--r--   0 maurits    (501) staff       (20)     3118 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/release.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     2791 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/test_setup.py
+-rw-r--r--   0 maurits    (501) staff       (20)    22286 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/utils.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     9600 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/tests/vcs.txt
+-rw-r--r--   0 maurits    (501) staff       (20)    32636 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/utils.py
+-rw-r--r--   0 maurits    (501) staff       (20)    17236 2023-04-06 15:46:35.000000 zest.releaser-8.0.0a2/zest/releaser/vcs.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 15:46:36.332499 zest.releaser-8.0.0a2/zest.releaser.egg-info/
+-rw-r--r--   0 maurits    (501) staff       (20)    13852 2023-04-06 15:46:36.000000 zest.releaser-8.0.0a2/zest.releaser.egg-info/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)     2301 2023-04-06 15:46:36.000000 zest.releaser-8.0.0a2/zest.releaser.egg-info/SOURCES.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 15:46:36.000000 zest.releaser-8.0.0a2/zest.releaser.egg-info/dependency_links.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      951 2023-04-06 15:46:36.000000 zest.releaser-8.0.0a2/zest.releaser.egg-info/entry_points.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        5 2023-04-06 15:46:36.000000 zest.releaser-8.0.0a2/zest.releaser.egg-info/namespace_packages.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 15:46:36.000000 zest.releaser-8.0.0a2/zest.releaser.egg-info/not-zip-safe
+-rw-r--r--   0 maurits    (501) staff       (20)      185 2023-04-06 15:46:36.000000 zest.releaser-8.0.0a2/zest.releaser.egg-info/requires.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        5 2023-04-06 15:46:36.000000 zest.releaser-8.0.0a2/zest.releaser.egg-info/top_level.txt
```

### Comparing `zest.releaser-8.0.0a1/CHANGES.rst` & `zest.releaser-8.0.0a2/CHANGES.rst`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,25 @@
 Changelog for zest.releaser
 ===========================
 
+8.0.0a2 (2023-04-06)
+--------------------
+
+- Always create wheels, except when you explicitly switch this off in the config:
+  ``[zest.releaser] create-wheel = no``.
+  If the ``wheel`` package is not available, we still do not create wheels.
+  Fixes `issue 406 <https://github.com/zestsoftware/zest.releaser/issues/406>`_.
+  [maurits]
+
+- Do not fail when tag versions cannot be parsed.
+  This can happen in ``lasttaglog``, ``lasttagdiff``, and ``bumpversion``, with ``setuptools`` 66 or higher.
+  Fixes `issue 408 <https://github.com/zestsoftware/zest.releaser/issues/408>`_.
+  [maurits]
+
+
 8.0.0a1 (2023-02-08)
 --------------------
 
 - Drop support for Python 3.6.  [maurits]
 
 - Support reading and writing the version in ``pyproject.toml``.
   See `issue 295 <https://github.com/zestsoftware/zest.releaser/issues/295>`_,
```

### Comparing `zest.releaser-8.0.0a1/CONTRIBUTING.rst` & `zest.releaser-8.0.0a2/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/CREDITS.rst` & `zest.releaser-8.0.0a2/CREDITS.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/LICENSE.GPL` & `zest.releaser-8.0.0a2/LICENSE.GPL`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/LICENSE.rst` & `zest.releaser-8.0.0a2/LICENSE.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/PKG-INFO` & `zest.releaser-8.0.0a2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: zest.releaser
-Version: 8.0.0a1
+Version: 8.0.0a2
 Summary: Software releasing made easy and repeatable
 Author-email: Reinout van Rees <reinout@vanrees.org>, Maurits van Rees <maurits@vanrees.org>
 License: GPL
 Project-URL: documentation, https://zestreleaser.readthedocs.io
 Project-URL: repository, https://github.com/zestsoftware/zest.releaser/
 Project-URL: changelog, https://github.com/zestsoftware/zest.releaser/blob/master/CHANGES.rst
 Keywords: releasing,packaging,pypi
@@ -248,14 +248,29 @@
 
 * `Mateusz Legięcki <https://github.com/Behoston>`_ added a dockerfile for
   much easier testing.
 
 Changelog for zest.releaser
 ===========================
 
+8.0.0a2 (2023-04-06)
+--------------------
+
+- Always create wheels, except when you explicitly switch this off in the config:
+  ``[zest.releaser] create-wheel = no``.
+  If the ``wheel`` package is not available, we still do not create wheels.
+  Fixes `issue 406 <https://github.com/zestsoftware/zest.releaser/issues/406>`_.
+  [maurits]
+
+- Do not fail when tag versions cannot be parsed.
+  This can happen in ``lasttaglog``, ``lasttagdiff``, and ``bumpversion``, with ``setuptools`` 66 or higher.
+  Fixes `issue 408 <https://github.com/zestsoftware/zest.releaser/issues/408>`_.
+  [maurits]
+
+
 8.0.0a1 (2023-02-08)
 --------------------
 
 - Drop support for Python 3.6.  [maurits]
 
 - Support reading and writing the version in ``pyproject.toml``.
   See `issue 295 <https://github.com/zestsoftware/zest.releaser/issues/295>`_,
```

### Comparing `zest.releaser-8.0.0a1/README.rst` & `zest.releaser-8.0.0a2/README.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/assumptions.rst` & `zest.releaser-8.0.0a2/doc/source/assumptions.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/changelog.rst` & `zest.releaser-8.0.0a2/doc/source/changelog.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/conf.py` & `zest.releaser-8.0.0a2/doc/source/conf.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/developing.rst` & `zest.releaser-8.0.0a2/doc/source/developing.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/entrypoints.rst` & `zest.releaser-8.0.0a2/doc/source/entrypoints.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/further_reading.rst` & `zest.releaser-8.0.0a2/doc/source/further_reading.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/index.rst` & `zest.releaser-8.0.0a2/doc/source/index.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/options.rst` & `zest.releaser-8.0.0a2/doc/source/options.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/project.rst` & `zest.releaser-8.0.0a2/doc/source/project.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/uploading.rst` & `zest.releaser-8.0.0a2/doc/source/uploading.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/doc/source/versions.rst` & `zest.releaser-8.0.0a2/doc/source/versions.rst`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/pyproject.toml` & `zest.releaser-8.0.0a2/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 [build-system]
 # See https://snarky.ca/what-the-heck-is-pyproject-toml/
 requires = ["setuptools", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "zest.releaser"
-version = "8.0.0a1"
+version = "8.0.0a2"
 description = "Software releasing made easy and repeatable"
 license = {text = "GPL"}
 authors = [
     {name = "Reinout van Rees", email = "reinout@vanrees.org"},
     {name = "Maurits van Rees", email = "maurits@vanrees.org"},
 ]
 dependencies = [
```

### Comparing `zest.releaser-8.0.0a1/zest/releaser/addchangelogentry.py` & `zest.releaser-8.0.0a2/zest/releaser/addchangelogentry.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/baserelease.py` & `zest.releaser-8.0.0a2/zest/releaser/baserelease.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/bumpversion.py` & `zest.releaser-8.0.0a2/zest/releaser/bumpversion.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/choose.py` & `zest.releaser-8.0.0a2/zest/releaser/choose.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/fullrelease.py` & `zest.releaser-8.0.0a2/zest/releaser/fullrelease.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/git.py` & `zest.releaser-8.0.0a2/zest/releaser/git.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/lasttagdiff.py` & `zest.releaser-8.0.0a2/zest/releaser/lasttagdiff.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/lasttaglog.py` & `zest.releaser-8.0.0a2/zest/releaser/lasttaglog.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/longtest.py` & `zest.releaser-8.0.0a2/zest/releaser/longtest.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/postrelease.py` & `zest.releaser-8.0.0a2/zest/releaser/postrelease.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/preparedocs.py` & `zest.releaser-8.0.0a2/zest/releaser/preparedocs.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/prerelease.py` & `zest.releaser-8.0.0a2/zest/releaser/prerelease.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/pypi.py` & `zest.releaser-8.0.0a2/zest/releaser/pypi.py`

 * *Files 2% similar despite different names*

```diff
@@ -402,44 +402,33 @@
         except (NoSectionError, NoOptionError, ValueError):
             return default
         return result
 
     def create_wheel(self):
         """Should we create a Python wheel for this package?
 
-        Either in your ~/.pypirc or in a setup.cfg in a specific
-        package, add this when you want to create a Python wheel, next
-        to a standard sdist:
+        This is next to the standard source distribution that we always create
+        when releasing a Python package.
 
-        [zest.releaser]
-        create-wheel = yes
-
-        If there is no setting for ``create-wheel``, then if there is a
-        ``[bdist_wheel]`` section, it is treated as if
-        ``create-wheel`` was true.  We used to look at the value of
-        the ``universal`` option, but that no longer matters.
-        This will still create a wheel:
+        Changed in version 8.0.0a2: we ALWAYS create a wheel,
+        unless this is explicitly switched off.
+        The `wheel` package must be installed though, which is in our
+        'recommended' extra.
 
-        [bdist_wheel]
-        universal = 0
+        To switch this OFF, either in your ~/.pypirc or in a setup.cfg in
+        a specific package, add this:
 
-        See https://github.com/zestsoftware/zest.releaser/issues/315
+        [zest.releaser]
+        create-wheel = no
         """
         if not USE_WHEEL:
             # If the wheel package is not available, we obviously
             # cannot create wheels.
             return False
-        create_setting = self._get_boolean("zest.releaser", "create-wheel", None)
-        if create_setting is not None:
-            # User specified this setting, it overrides
-            # inferring from bdist_wheel
-            return create_setting
-        # No zest.releaser setting, are they asking for a universal wheel?
-        # Then they want wheels in general.
-        return self.config.has_section("bdist_wheel")
+        return self._get_boolean("zest.releaser", "create-wheel", True)
 
     def register_package(self):
         """Should we try to register this package with a package server?
 
         For the standard Python Package Index (PyPI), registering a
         package is no longer needed: this is done automatically when
         uploading a distribution for a package.  In fact, trying to
```

### Comparing `zest.releaser-8.0.0a1/zest/releaser/release.py` & `zest.releaser-8.0.0a2/zest/releaser/release.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/addchangelogentry.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/addchangelogentry.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/baserelease.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/baserelease.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/bumpversion.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/bumpversion.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/choose.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/choose.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/example.tar` & `zest.releaser-8.0.0a2/zest/releaser/tests/example.tar`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/fullrelease.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/fullrelease.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/functional-git.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/functional-git.txt`

 * *Files 2% similar despite different names*

```diff
@@ -146,9 +146,9 @@
     >>> githead('setup.py')
     from setuptools import setup, find_packages
     version = '0.2.dev0'
 
 And there are no uncommitted changes:
 
     >>> print(execute_command(["git", "status"]))
-    On branch master
+    On branch main
     nothing to commit, working directory clean
```

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/functional-with-hooks.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/functional-with-hooks.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/functional.py` & `zest.releaser-8.0.0a2/zest/releaser/tests/functional.py`

 * *Files 1% similar despite different names*

```diff
@@ -67,15 +67,15 @@
         tf.extractall(path=test.tempdir)
     sourcedir = os.path.join(test.tempdir, "tha.example")
 
     # Git initialization
     gitsourcedir = os.path.join(test.tempdir, "tha.example-git")
     shutil.copytree(sourcedir, gitsourcedir)
     os.chdir(gitsourcedir)
-    execute_command(["git", "init"])
+    execute_command(["git", "init", "-b", "main"])
     # Configure local git.
     execute_command(["git", "config", "--local", "user.name", "Temp user"])
     execute_command(["git", "config", "--local", "user.email", "temp@example.com"])
     execute_command(["git", "config", "--local", "commit.gpgsign", "false"])
     execute_command(["git", "config", "--local", "tag.gpgsign", "false"])
     execute_command(["git", "add", "."])
     execute_command(["git", "commit", "-a", "-m", "init" "-n"])
```

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/git.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/git.txt`

 * *Files 3% similar despite different names*

```diff
@@ -53,15 +53,15 @@
 Commit it:
 
     >>> cmd = checkout.cmd_commit('small tweak')
     >>> cmd
     ['git', 'commit', '-a', '-m', 'small tweak', '-n']
 
 In some cases we get this output:
-``[master ...] small tweak``
+``[main ...] small tweak``
 and in other this:
 ``Created commit ...: small tweak``
 
     >>> print('dummy %s' % execute_command(cmd))
     dummy...small tweak
      1 file changed, 2 insertions(+)
 
@@ -185,22 +185,22 @@
 
     >>> with open(os.path.join(temp, 'setup.py')) as f:
     ...     print(f.read())
     from setuptools import setup, find_packages
     ...
     a = 2
 
-Change back to the source directory and return to the master branch.
+Change back to the source directory and return to the main branch.
 
     >>> os.chdir(gitsourcedir)
-    >>> cmd = [['git', 'checkout', 'master'],
+    >>> cmd = [['git', 'checkout', 'main'],
     ... ['git', 'submodule', 'update', '--init', '--recursive']]
     >>> print(execute_commands(cmd))
     RED Previous HEAD position was ... small tweak
-    RED Switched to branch 'master'
+    RED Switched to branch 'main'
 
 Pushing changes
 ---------------
 
 For git, committing isn't enough. We need to push changes to the server:
 
     >>> checkout.push_commands()
```

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/postrelease.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/postrelease.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/preparedocs.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/preparedocs.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/prerelease.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/prerelease.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/pypi.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/pypi.txt`

 * *Files 13% similar despite different names*

```diff
@@ -153,61 +153,35 @@
 
 
 Creating a wheel
 ----------------
 
 When the ``wheel`` package is installed, we could create shiny new
 Python wheels, next to the standard old-style source distributions.
-This seems good, but not for every package.  So you have to explicitly
-turn it on.
+In 2023 this seems good for most packages, so since version 8.0.0a2 this is by default true.
 
 If the package is installed, we set a constant:
 
     >>> from zest.releaser.pypi import USE_WHEEL
     >>> USE_WHEEL
     True
 
 We try to read a [zest.releaser] section, either in pypirc or
 setup.cfg and check for a ``create-wheel`` option.  In this case we
 explicitly disable checking for a setup.cfg, because when running the
 tests with ``tox`` the current directory is the base directory of
 zest.releaser, which now contains a setup.cfg.
 
-We can ask for the result like this, which by default is False:
+We can ask for the result like this, which by default is True:
 
     >>> pypiconfig = pypi.PypiConfig(config_filename=pypirc_both, use_setup_cfg=False)
     >>> pypiconfig.create_wheel()
-    False
-
-We have a pypirc for this where we implicitly set it to False:
-
-    >>> pypirc_no_release = pkg_resources.resource_filename(
-    ...     'zest.releaser.tests', 'pypirc_no_release.txt')
-    >>> pypiconfig = pypi.PypiConfig(config_filename=pypirc_no_release, use_setup_cfg=False)
-    >>> pypiconfig.create_wheel()
-    False
-
-We can also specify to always create it:
-
-    >>> pypirc_yes_release = pkg_resources.resource_filename(
-    ...     'zest.releaser.tests', 'pypirc_yes_release.txt')
-    >>> pypiconfig = pypi.PypiConfig(config_filename=pypirc_yes_release, use_setup_cfg=False)
-    >>> pypiconfig.create_wheel()
-    True
-
-Asking for universal wheels is the same as explicitly asking to create
-wheels:
-
-    >>> pypirc_yes_release = pkg_resources.resource_filename(
-    ...     'zest.releaser.tests', 'pypirc_universal_create.txt')
-    >>> pypiconfig = pypi.PypiConfig(config_filename=pypirc_yes_release, use_setup_cfg=False)
-    >>> pypiconfig.create_wheel()
     True
 
-But a negative setting overrides universal wheels:
+We can also specify to not create the wheel, even when (universal) wheels could be created:
 
     >>> pypirc_yes_release = pkg_resources.resource_filename(
     ...     'zest.releaser.tests', 'pypirc_universal_nocreate.txt')
     >>> pypiconfig = pypi.PypiConfig(config_filename=pypirc_yes_release, use_setup_cfg=False)
     >>> pypiconfig.create_wheel()
     False
```

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/pyproject-toml.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/pyproject-toml.txt`

 * *Files 1% similar despite different names*

```diff
@@ -20,15 +20,15 @@
     >>> _ = execute_command(["git", "rm", "setup.cfg", "setup.py"])
     >>> pyproject_file = os.path.join(os.path.dirname(tests.__file__), "pyproject.toml")
     >>> shutil.copy(pyproject_file, os.path.curdir)
     './pyproject.toml'
     >>> _ = execute_command(["git", "add", "pyproject.toml"])
     >>> _ = execute_command(["git", "commit", "-m", "Move to pyproject.toml"])
     >>> print(execute_command(["git", "status"]))
-    On branch master
+    On branch main
     nothing to commit, working directory clean
 
 The version is at 0.1.dev0:
 
     >>> githead('pyproject.toml')
     [project]
     name = "tha.example"
@@ -136,9 +136,9 @@
     version = "0.2.dev0"
     description = "Example package"
     keywords = ["example"]
 
 And there are no uncommitted changes:
 
     >>> print(execute_command(["git", "status"]))
-    On branch master
+    On branch main
     nothing to commit, working directory clean
```

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/release.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/release.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/test_setup.py` & `zest.releaser-8.0.0a2/zest/releaser/tests/test_setup.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/utils.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/utils.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/tests/vcs.txt` & `zest.releaser-8.0.0a2/zest/releaser/tests/vcs.txt`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest/releaser/utils.py` & `zest.releaser-8.0.0a2/zest/releaser/utils.py`

 * *Files 2% similar despite different names*

```diff
@@ -845,27 +845,41 @@
 
     # Mostly nicked from zest.stabilizer.
 
     # We seek a tag that's the same or less than the version as determined
     # by setuptools' version parsing. A direct match is obviously
     # right. The 'less' approach handles development eggs that have
     # already been switched back to development.
-    available_tags.reverse()
-    found = available_tags[0]
+    # Note: if parsing the current version fails, there is nothing we can do:
+    # there is no sane way of knowing which version is smaller than an unparsable
+    # version, so we just break hard.
     parsed_version = parse_version(version)
+    found = parsed_found = None
     for tag in available_tags:
-        parsed_tag = parse_version(tag)
-        parsed_found = parse_version(found)
+        try:
+            parsed_tag = parse_version(tag)
+        except Exception:
+            # I don't want to import this specific exception,
+            # because it sounds unstable:
+            # pkg_resources.extern.packaging.version.InvalidVersion
+            logger.debug("Could not parse version: %s", tag)
+            continue
         if parsed_tag == parsed_version:
             found = tag
             logger.debug("Found exact match: %s", found)
             break
-        if parsed_tag >= parsed_found and parsed_tag < parsed_version:
-            logger.debug("Found possible lower match: %s", tag)
-            found = tag
+        if parsed_tag >= parsed_version:
+            # too new tag, not interesting
+            continue
+        if found is not None and parsed_tag <= parsed_found:
+            # we already have a better match
+            continue
+        logger.debug("Found possible lower match: %s", tag)
+        found = tag
+        parsed_found = parsed_tag
     return found
 
 
 def sanity_check(vcs):
     """Do sanity check before making changes
 
     Check that we are not on a tag and/or do not have local changes.
```

### Comparing `zest.releaser-8.0.0a1/zest/releaser/vcs.py` & `zest.releaser-8.0.0a2/zest/releaser/vcs.py`

 * *Files identical despite different names*

### Comparing `zest.releaser-8.0.0a1/zest.releaser.egg-info/PKG-INFO` & `zest.releaser-8.0.0a2/zest.releaser.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: zest.releaser
-Version: 8.0.0a1
+Version: 8.0.0a2
 Summary: Software releasing made easy and repeatable
 Author-email: Reinout van Rees <reinout@vanrees.org>, Maurits van Rees <maurits@vanrees.org>
 License: GPL
 Project-URL: documentation, https://zestreleaser.readthedocs.io
 Project-URL: repository, https://github.com/zestsoftware/zest.releaser/
 Project-URL: changelog, https://github.com/zestsoftware/zest.releaser/blob/master/CHANGES.rst
 Keywords: releasing,packaging,pypi
@@ -248,14 +248,29 @@
 
 * `Mateusz Legięcki <https://github.com/Behoston>`_ added a dockerfile for
   much easier testing.
 
 Changelog for zest.releaser
 ===========================
 
+8.0.0a2 (2023-04-06)
+--------------------
+
+- Always create wheels, except when you explicitly switch this off in the config:
+  ``[zest.releaser] create-wheel = no``.
+  If the ``wheel`` package is not available, we still do not create wheels.
+  Fixes `issue 406 <https://github.com/zestsoftware/zest.releaser/issues/406>`_.
+  [maurits]
+
+- Do not fail when tag versions cannot be parsed.
+  This can happen in ``lasttaglog``, ``lasttagdiff``, and ``bumpversion``, with ``setuptools`` 66 or higher.
+  Fixes `issue 408 <https://github.com/zestsoftware/zest.releaser/issues/408>`_.
+  [maurits]
+
+
 8.0.0a1 (2023-02-08)
 --------------------
 
 - Drop support for Python 3.6.  [maurits]
 
 - Support reading and writing the version in ``pyproject.toml``.
   See `issue 295 <https://github.com/zestsoftware/zest.releaser/issues/295>`_,
```

### Comparing `zest.releaser-8.0.0a1/zest.releaser.egg-info/SOURCES.txt` & `zest.releaser-8.0.0a2/zest.releaser.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -66,15 +66,14 @@
 zest/releaser/tests/pypi.txt
 zest/releaser/tests/pypirc_both.txt
 zest/releaser/tests/pypirc_new.txt
 zest/releaser/tests/pypirc_no_input.txt
 zest/releaser/tests/pypirc_no_release.txt
 zest/releaser/tests/pypirc_old.txt
 zest/releaser/tests/pypirc_simple.txt
-zest/releaser/tests/pypirc_universal_create.txt
 zest/releaser/tests/pypirc_universal_nocreate.txt
 zest/releaser/tests/pypirc_yes_release.txt
 zest/releaser/tests/pyproject-toml.txt
 zest/releaser/tests/pyproject.toml
 zest/releaser/tests/release.txt
 zest/releaser/tests/test_setup.py
 zest/releaser/tests/utils.txt
```

### Comparing `zest.releaser-8.0.0a1/zest.releaser.egg-info/entry_points.txt` & `zest.releaser-8.0.0a2/zest.releaser.egg-info/entry_points.txt`

 * *Files identical despite different names*

