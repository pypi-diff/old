# Comparing `tmp/razorback-0.4.3a2.tar.gz` & `tmp/razorback-0.4.3a3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "razorback-0.4.3a2.tar", last modified: Wed Mar 29 12:53:30 2023, max compression
+gzip compressed data, was "razorback-0.4.3a3.tar", last modified: Thu Apr  6 16:16:31 2023, max compression
```

## Comparing `razorback-0.4.3a2.tar` & `razorback-0.4.3a3.tar`

### file list

```diff
@@ -1,68 +1,68 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.130845 razorback-0.4.3a2/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.122845 razorback-0.4.3a2/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.122845 razorback-0.4.3a2/.github/ISSUE_TEMPLATE/
--rw-r--r--   0 runner    (1001) docker     (123)      748 2023-03-29 12:53:00.000000 razorback-0.4.3a2/.github/ISSUE_TEMPLATE/bug_report.md
--rw-r--r--   0 runner    (1001) docker     (123)      595 2023-03-29 12:53:00.000000 razorback-0.4.3a2/.github/ISSUE_TEMPLATE/feature_request.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.126845 razorback-0.4.3a2/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)     1626 2023-03-29 12:53:00.000000 razorback-0.4.3a2/.github/workflows/continuous-integration.yml
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-29 12:53:00.000000 razorback-0.4.3a2/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)      131 2023-03-29 12:53:00.000000 razorback-0.4.3a2/.gitmodules
--rw-r--r--   0 runner    (1001) docker     (123)       69 2023-03-29 12:53:00.000000 razorback-0.4.3a2/AUTHORS
--rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-03-29 12:53:00.000000 razorback-0.4.3a2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1714 2023-03-29 12:53:30.130845 razorback-0.4.3a2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1128 2023-03-29 12:53:00.000000 razorback-0.4.3a2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.126845 razorback-0.4.3a2/docs/
--rw-r--r--   0 runner    (1001) docker     (123)      769 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/Makefile
--rw-r--r--   0 runner    (1001) docker     (123)      781 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/make.bat
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.126845 razorback-0.4.3a2/docs/source/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.126845 razorback-0.4.3a2/docs/source/_static/
--rw-r--r--   0 runner    (1001) docker     (123)     2769 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/_static/copybutton.js
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.126845 razorback-0.4.3a2/docs/source/_templates/
--rw-r--r--   0 runner    (1001) docker     (123)      133 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/_templates/layout.html
--rw-r--r--   0 runner    (1001) docker     (123)      347 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/citation.rst
--rw-r--r--   0 runner    (1001) docker     (123)    10544 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/conf.py
--rw-r--r--   0 runner    (1001) docker     (123)      482 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1208 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/install.rst
--rw-r--r--   0 runner    (1001) docker     (123)      528 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/overview.rst
--rw-r--r--   0 runner    (1001) docker     (123)       39 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/quickstart.rst
--rw-r--r--   0 runner    (1001) docker     (123)     2881 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/script.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.126845 razorback-0.4.3a2/docs/source/tutorials/
--rw-r--r--   0 runner    (1001) docker     (123)    32849 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/tutorials/handling-time-series.ipynb
--rw-r--r--   0 runner    (1001) docker     (123)      148 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/tutorials/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)   130585 2023-03-29 12:53:00.000000 razorback-0.4.3a2/docs/source/tutorials/survey-study.ipynb
--rw-r--r--   0 runner    (1001) docker     (123)     1145 2023-03-29 12:53:00.000000 razorback-0.4.3a2/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)      191 2023-03-29 12:53:00.000000 razorback-0.4.3a2/readthedocs.yml
--rw-r--r--   0 runner    (1001) docker     (123)       69 2023-03-29 12:53:00.000000 razorback-0.4.3a2/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-29 12:53:30.130845 razorback-0.4.3a2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-29 12:53:00.000000 razorback-0.4.3a2/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.122845 razorback-0.4.3a2/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.126845 razorback-0.4.3a2/src/razorback/
--rw-r--r--   0 runner    (1001) docker     (123)      508 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      162 2023-03-29 12:53:30.000000 razorback-0.4.3a2/src/razorback/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)     4565 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/calibrations.py
--rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/cli.py
--rw-r--r--   0 runner    (1001) docker     (123)     1196 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/data.py
--rw-r--r--   0 runner    (1001) docker     (123)      153 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/errors.py
--rw-r--r--   0 runner    (1001) docker     (123)     5339 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/fourier_transform.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.126845 razorback-0.4.3a2/src/razorback/io/
--rw-r--r--   0 runner    (1001) docker     (123)      235 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/io/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4676 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/io/ats.py
--rw-r--r--   0 runner    (1001) docker     (123)     5362 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/io/binary_file_array.py
--rw-r--r--   0 runner    (1001) docker     (123)     8202 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/mestimator.py
--rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/prefilters.py
--rw-r--r--   0 runner    (1001) docker     (123)    34897 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/signalset.py
--rw-r--r--   0 runner    (1001) docker     (123)    16655 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/utils.py
--rw-r--r--   0 runner    (1001) docker     (123)     5489 2023-03-29 12:53:00.000000 razorback-0.4.3a2/src/razorback/weights.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.126845 razorback-0.4.3a2/src/razorback.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1714 2023-03-29 12:53:30.000000 razorback-0.4.3a2/src/razorback.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1392 2023-03-29 12:53:30.000000 razorback-0.4.3a2/src/razorback.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-29 12:53:30.000000 razorback-0.4.3a2/src/razorback.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       42 2023-03-29 12:53:30.000000 razorback-0.4.3a2/src/razorback.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-03-29 12:53:30.000000 razorback-0.4.3a2/src/razorback.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       10 2023-03-29 12:53:30.000000 razorback-0.4.3a2/src/razorback.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-29 12:53:30.130845 razorback-0.4.3a2/tests/
--rw-r--r--   0 runner    (1001) docker     (123)     2724 2023-03-29 12:53:00.000000 razorback-0.4.3a2/tests/test_impedance.py
--rw-r--r--   0 runner    (1001) docker     (123)     1144 2023-03-29 12:53:00.000000 razorback-0.4.3a2/tests/test_inventory.doctest
--rw-r--r--   0 runner    (1001) docker     (123)    13414 2023-03-29 12:53:00.000000 razorback-0.4.3a2/tests/test_merge_consecutive_runs.py
--rw-r--r--   0 runner    (1001) docker     (123)     2985 2023-03-29 12:53:00.000000 razorback-0.4.3a2/tests/test_signalset.doctest
--rw-r--r--   0 runner    (1001) docker     (123)      956 2023-03-29 12:53:00.000000 razorback-0.4.3a2/tests/test_tags_from_path.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.859325 razorback-0.4.3a3/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.847325 razorback-0.4.3a3/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.851325 razorback-0.4.3a3/.github/ISSUE_TEMPLATE/
+-rw-r--r--   0 runner    (1001) docker     (123)      748 2023-04-06 16:15:52.000000 razorback-0.4.3a3/.github/ISSUE_TEMPLATE/bug_report.md
+-rw-r--r--   0 runner    (1001) docker     (123)      595 2023-04-06 16:15:52.000000 razorback-0.4.3a3/.github/ISSUE_TEMPLATE/feature_request.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.851325 razorback-0.4.3a3/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     1626 2023-04-06 16:15:52.000000 razorback-0.4.3a3/.github/workflows/continuous-integration.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-04-06 16:15:52.000000 razorback-0.4.3a3/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      131 2023-04-06 16:15:52.000000 razorback-0.4.3a3/.gitmodules
+-rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-06 16:15:52.000000 razorback-0.4.3a3/AUTHORS
+-rw-r--r--   0 runner    (1001) docker     (123)    35149 2023-04-06 16:15:52.000000 razorback-0.4.3a3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1714 2023-04-06 16:16:31.859325 razorback-0.4.3a3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1128 2023-04-06 16:15:52.000000 razorback-0.4.3a3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.851325 razorback-0.4.3a3/docs/
+-rw-r--r--   0 runner    (1001) docker     (123)      769 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/Makefile
+-rw-r--r--   0 runner    (1001) docker     (123)      781 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/make.bat
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.855325 razorback-0.4.3a3/docs/source/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.855325 razorback-0.4.3a3/docs/source/_static/
+-rw-r--r--   0 runner    (1001) docker     (123)     2769 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/_static/copybutton.js
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.855325 razorback-0.4.3a3/docs/source/_templates/
+-rw-r--r--   0 runner    (1001) docker     (123)      133 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/_templates/layout.html
+-rw-r--r--   0 runner    (1001) docker     (123)      347 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/citation.rst
+-rw-r--r--   0 runner    (1001) docker     (123)    10544 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/conf.py
+-rw-r--r--   0 runner    (1001) docker     (123)      482 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1208 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/install.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      528 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/overview.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       39 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/quickstart.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     2881 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/script.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.855325 razorback-0.4.3a3/docs/source/tutorials/
+-rw-r--r--   0 runner    (1001) docker     (123)    32849 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/tutorials/handling-time-series.ipynb
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/tutorials/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)   130585 2023-04-06 16:15:52.000000 razorback-0.4.3a3/docs/source/tutorials/survey-study.ipynb
+-rw-r--r--   0 runner    (1001) docker     (123)     1145 2023-04-06 16:15:52.000000 razorback-0.4.3a3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      191 2023-04-06 16:15:52.000000 razorback-0.4.3a3/readthedocs.yml
+-rw-r--r--   0 runner    (1001) docker     (123)       69 2023-04-06 16:15:52.000000 razorback-0.4.3a3/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 16:16:31.859325 razorback-0.4.3a3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 16:15:52.000000 razorback-0.4.3a3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.847325 razorback-0.4.3a3/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.855325 razorback-0.4.3a3/src/razorback/
+-rw-r--r--   0 runner    (1001) docker     (123)      508 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      162 2023-04-06 16:16:31.000000 razorback-0.4.3a3/src/razorback/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4565 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/calibrations.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1937 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/cli.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1196 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      153 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/errors.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5339 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/fourier_transform.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.859325 razorback-0.4.3a3/src/razorback/io/
+-rw-r--r--   0 runner    (1001) docker     (123)      235 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/io/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4676 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/io/ats.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5362 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/io/binary_file_array.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8202 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/mestimator.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1514 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/prefilters.py
+-rw-r--r--   0 runner    (1001) docker     (123)    34897 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/signalset.py
+-rw-r--r--   0 runner    (1001) docker     (123)    16792 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/utils.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5489 2023-04-06 16:15:52.000000 razorback-0.4.3a3/src/razorback/weights.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.859325 razorback-0.4.3a3/src/razorback.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1714 2023-04-06 16:16:31.000000 razorback-0.4.3a3/src/razorback.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1392 2023-04-06 16:16:31.000000 razorback-0.4.3a3/src/razorback.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 16:16:31.000000 razorback-0.4.3a3/src/razorback.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       42 2023-04-06 16:16:31.000000 razorback-0.4.3a3/src/razorback.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-04-06 16:16:31.000000 razorback-0.4.3a3/src/razorback.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       10 2023-04-06 16:16:31.000000 razorback-0.4.3a3/src/razorback.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 16:16:31.859325 razorback-0.4.3a3/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)     2724 2023-04-06 16:15:52.000000 razorback-0.4.3a3/tests/test_impedance.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1144 2023-04-06 16:15:52.000000 razorback-0.4.3a3/tests/test_inventory.doctest
+-rw-r--r--   0 runner    (1001) docker     (123)    13414 2023-04-06 16:15:52.000000 razorback-0.4.3a3/tests/test_merge_consecutive_runs.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2985 2023-04-06 16:15:52.000000 razorback-0.4.3a3/tests/test_signalset.doctest
+-rw-r--r--   0 runner    (1001) docker     (123)      956 2023-04-06 16:15:52.000000 razorback-0.4.3a3/tests/test_tags_from_path.py
```

### Comparing `razorback-0.4.3a2/.github/ISSUE_TEMPLATE/bug_report.md` & `razorback-0.4.3a3/.github/ISSUE_TEMPLATE/bug_report.md`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/.github/ISSUE_TEMPLATE/feature_request.md` & `razorback-0.4.3a3/.github/ISSUE_TEMPLATE/feature_request.md`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/.github/workflows/continuous-integration.yml` & `razorback-0.4.3a3/.github/workflows/continuous-integration.yml`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/LICENSE` & `razorback-0.4.3a3/LICENSE`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/PKG-INFO` & `razorback-0.4.3a3/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: razorback
-Version: 0.4.3a2
+Version: 0.4.3a3
 Summary: Robust estimation of linear response functions
 Author-email: Farid Smai <f.smai@brgm.fr>
 License: GNU GPLv3 License
 Project-URL: Homepage, https://github.com/BRGM/razorback
 Project-URL: Documentation, https://razorback.readthedocs.io
 Project-URL: Source, https://github.com/BRGM/razorback
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

### Comparing `razorback-0.4.3a2/README.md` & `razorback-0.4.3a3/README.md`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/docs/Makefile` & `razorback-0.4.3a3/docs/Makefile`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/docs/make.bat` & `razorback-0.4.3a3/docs/make.bat`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/docs/source/_static/copybutton.js` & `razorback-0.4.3a3/docs/source/_static/copybutton.js`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/docs/source/conf.py` & `razorback-0.4.3a3/docs/source/conf.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/docs/source/install.rst` & `razorback-0.4.3a3/docs/source/install.rst`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/docs/source/overview.rst` & `razorback-0.4.3a3/docs/source/overview.rst`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/docs/source/script.rst` & `razorback-0.4.3a3/docs/source/script.rst`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/docs/source/tutorials/handling-time-series.ipynb` & `razorback-0.4.3a3/docs/source/tutorials/handling-time-series.ipynb`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/docs/source/tutorials/survey-study.ipynb` & `razorback-0.4.3a3/docs/source/tutorials/survey-study.ipynb`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/pyproject.toml` & `razorback-0.4.3a3/pyproject.toml`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/calibrations.py` & `razorback-0.4.3a3/src/razorback/calibrations.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/cli.py` & `razorback-0.4.3a3/src/razorback/cli.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/data.py` & `razorback-0.4.3a3/src/razorback/data.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/fourier_transform.py` & `razorback-0.4.3a3/src/razorback/fourier_transform.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/io/ats.py` & `razorback-0.4.3a3/src/razorback/io/ats.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/io/binary_file_array.py` & `razorback-0.4.3a3/src/razorback/io/binary_file_array.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/mestimator.py` & `razorback-0.4.3a3/src/razorback/mestimator.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/prefilters.py` & `razorback-0.4.3a3/src/razorback/prefilters.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/signalset.py` & `razorback-0.4.3a3/src/razorback/signalset.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback/utils.py` & `razorback-0.4.3a3/src/razorback/utils.py`

 * *Files 1% similar despite different names*

```diff
@@ -58,14 +58,15 @@
     transfer_mag: complex
 
 
 def impedance_mass_proc(
     inventory, remote_names,
     l_freq, l_interval,
     impedance_opts,
+    combines_remotes=True,
 ):
     """ massive processing with multiple remote
     all combination of remote
 
     TODO: doc
 
     inventory: Inventory
@@ -75,17 +76,20 @@
             others -> remotes
 
     remote_names: list of str
         tag names for the remotes magn
 
     """
 
-    remote_combination = list(itertools.product(*[
-        (None, e) for e in range(len(remote_names))
-    ]))
+    if combines_remotes:
+        remote_combination = list(itertools.product(*[
+            (None, e) for e in range(len(remote_names))
+        ]))
+    else:
+        remote_combination = [tuple(range(len(remote_names)))]
 
     ptl_z, ptl_ivt, ptl_err, ptl_T = [], [], [], []
     l_rcomb = []
     for k, rindices in enumerate(remote_combination):
 
         remote_tags = [remote_names[e] for e in rindices if e is not None]
         options = dict(impedance_opts)
```

### Comparing `razorback-0.4.3a2/src/razorback/weights.py` & `razorback-0.4.3a3/src/razorback/weights.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/src/razorback.egg-info/PKG-INFO` & `razorback-0.4.3a3/src/razorback.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: razorback
-Version: 0.4.3a2
+Version: 0.4.3a3
 Summary: Robust estimation of linear response functions
 Author-email: Farid Smai <f.smai@brgm.fr>
 License: GNU GPLv3 License
 Project-URL: Homepage, https://github.com/BRGM/razorback
 Project-URL: Documentation, https://razorback.readthedocs.io
 Project-URL: Source, https://github.com/BRGM/razorback
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
```

### Comparing `razorback-0.4.3a2/src/razorback.egg-info/SOURCES.txt` & `razorback-0.4.3a3/src/razorback.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/tests/test_impedance.py` & `razorback-0.4.3a3/tests/test_impedance.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/tests/test_inventory.doctest` & `razorback-0.4.3a3/tests/test_inventory.doctest`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/tests/test_merge_consecutive_runs.py` & `razorback-0.4.3a3/tests/test_merge_consecutive_runs.py`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/tests/test_signalset.doctest` & `razorback-0.4.3a3/tests/test_signalset.doctest`

 * *Files identical despite different names*

### Comparing `razorback-0.4.3a2/tests/test_tags_from_path.py` & `razorback-0.4.3a3/tests/test_tags_from_path.py`

 * *Files identical despite different names*

