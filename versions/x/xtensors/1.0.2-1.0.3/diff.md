# Comparing `tmp/xtensors-1.0.2.tar.gz` & `tmp/xtensors-1.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "xtensors-1.0.2.tar", last modified: Fri Dec 23 05:45:05 2022, max compression
+gzip compressed data, was "xtensors-1.0.3.tar", last modified: Fri Apr  7 04:45:03 2023, max compression
```

## Comparing `xtensors-1.0.2.tar` & `xtensors-1.0.3.tar`

### file list

```diff
@@ -1,60 +1,60 @@
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.139929 xtensors-1.0.2/
--rw-rw-r--   0 michael   (1000) michael   (1000)     1070 2022-12-09 02:26:31.000000 xtensors-1.0.2/LICENSE
--rw-rw-r--   0 michael   (1000) michael   (1000)      781 2022-12-23 05:45:05.139929 xtensors-1.0.2/PKG-INFO
--rw-rw-r--   0 michael   (1000) michael   (1000)      283 2022-12-09 02:26:31.000000 xtensors-1.0.2/README.rst
--rw-rw-r--   0 michael   (1000) michael   (1000)      102 2022-12-09 02:26:31.000000 xtensors-1.0.2/pyproject.toml
--rw-rw-r--   0 michael   (1000) michael   (1000)      673 2022-12-23 05:45:05.139929 xtensors-1.0.2/setup.cfg
--rw-rw-r--   0 michael   (1000) michael   (1000)       39 2022-12-09 02:26:31.000000 xtensors-1.0.2/setup.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.135929 xtensors-1.0.2/src/
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.135929 xtensors-1.0.2/src/xtensors/
--rw-rw-r--   0 michael   (1000) michael   (1000)      221 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/__init__.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.135929 xtensors-1.0.2/src/xtensors/base/
--rw-rw-r--   0 michael   (1000) michael   (1000)     1127 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/base/__init__.py
--rw-r--r--   0 michael   (1000) michael   (1000)     2854 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/base/_arg.py
--rw-r--r--   0 michael   (1000) michael   (1000)     2543 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/base/_args.py
--rw-r--r--   0 michael   (1000) michael   (1000)     2967 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/base/_binary_op.py
--rw-r--r--   0 michael   (1000) michael   (1000)     3237 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/base/_coords.py
--rw-r--r--   0 michael   (1000) michael   (1000)      825 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/base/_misc.py
--rw-rw-r--   0 michael   (1000) michael   (1000)     3156 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/base/_reduc.py
--rw-rw-r--   0 michael   (1000) michael   (1000)      607 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/base/_reduc_2to1.py
--rw-r--r--   0 michael   (1000) michael   (1000)     1855 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/base/_ufuncs.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.135929 xtensors-1.0.2/src/xtensors/functionals/
--rw-rw-r--   0 michael   (1000) michael   (1000)      149 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/functionals/__init__.py
--rw-rw-r--   0 michael   (1000) michael   (1000)      853 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/functionals/base.py
--rw-rw-r--   0 michael   (1000) michael   (1000)     2755 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/functionals/reductions.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.135929 xtensors-1.0.2/src/xtensors/learn/
--rw-r--r--   0 michael   (1000) michael   (1000)       60 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/learn/__init__.py
--rw-r--r--   0 michael   (1000) michael   (1000)     1115 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/learn/confmat.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.135929 xtensors-1.0.2/src/xtensors/numpy/
--rw-r--r--   0 michael   (1000) michael   (1000)      176 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/numpy/__init__.py
--rw-r--r--   0 michael   (1000) michael   (1000)      941 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/numpy/_args.py
--rw-r--r--   0 michael   (1000) michael   (1000)     2360 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/numpy/_np.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.135929 xtensors-1.0.2/src/xtensors/tensor/
--rw-r--r--   0 michael   (1000) michael   (1000)      227 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/__init__.py
--rw-r--r--   0 michael   (1000) michael   (1000)    11303 2022-12-23 05:44:38.000000 xtensors-1.0.2/src/xtensors/tensor/_base.py
--rw-r--r--   0 michael   (1000) michael   (1000)     2365 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/_decors.py
--rw-r--r--   0 michael   (1000) michael   (1000)     1563 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/_slice.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.139929 xtensors-1.0.2/src/xtensors/tensor/basic_utils/
--rw-r--r--   0 michael   (1000) michael   (1000)      451 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/basic_utils/__init__.py
--rw-r--r--   0 michael   (1000) michael   (1000)     5981 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/basic_utils/_axes.py
--rw-r--r--   0 michael   (1000) michael   (1000)      754 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/basic_utils/_base.py
--rw-r--r--   0 michael   (1000) michael   (1000)     1765 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/basic_utils/_coords.py
--rw-r--r--   0 michael   (1000) michael   (1000)     4111 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/basic_utils/_dims.py
--rw-r--r--   0 michael   (1000) michael   (1000)     2244 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/basic_utils/_generalize.py
--rw-r--r--   0 michael   (1000) michael   (1000)     1093 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/basic_utils/_misc.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.139929 xtensors-1.0.2/src/xtensors/tensor/broadcast/
--rw-r--r--   0 michael   (1000) michael   (1000)     3002 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/broadcast/__init__.py
--rw-r--r--   0 michael   (1000) michael   (1000)     4475 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/broadcast/_broadcast.py
--rw-r--r--   0 michael   (1000) michael   (1000)     3409 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/broadcast/_dimcast.py
--rw-r--r--   0 michael   (1000) michael   (1000)     6454 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/broadcast/_template.py
--rw-r--r--   0 michael   (1000) michael   (1000)     1739 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/broadcast/_types.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.139929 xtensors-1.0.2/src/xtensors/tensor/typing/
--rw-r--r--   0 michael   (1000) michael   (1000)      320 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/typing/__init__.py
--rw-r--r--   0 michael   (1000) michael   (1000)     1880 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/tensor/typing/_typing.py
--rw-r--r--   0 michael   (1000) michael   (1000)       73 2022-12-09 02:26:32.000000 xtensors-1.0.2/src/xtensors/version.py
-drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2022-12-23 05:45:05.135929 xtensors-1.0.2/src/xtensors.egg-info/
--rw-rw-r--   0 michael   (1000) michael   (1000)      781 2022-12-23 05:45:05.000000 xtensors-1.0.2/src/xtensors.egg-info/PKG-INFO
--rw-rw-r--   0 michael   (1000) michael   (1000)     1504 2022-12-23 05:45:05.000000 xtensors-1.0.2/src/xtensors.egg-info/SOURCES.txt
--rw-rw-r--   0 michael   (1000) michael   (1000)        1 2022-12-23 05:45:05.000000 xtensors-1.0.2/src/xtensors.egg-info/dependency_links.txt
--rw-rw-r--   0 michael   (1000) michael   (1000)       23 2022-12-23 05:45:05.000000 xtensors-1.0.2/src/xtensors.egg-info/requires.txt
--rw-rw-r--   0 michael   (1000) michael   (1000)        9 2022-12-23 05:45:05.000000 xtensors-1.0.2/src/xtensors.egg-info/top_level.txt
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/
+-rw-rw-r--   0 michael   (1000) michael   (1000)     1070 2022-12-09 02:26:31.000000 xtensors-1.0.3/LICENSE
+-rw-rw-r--   0 michael   (1000) michael   (1000)      781 2023-04-07 04:45:03.758641 xtensors-1.0.3/PKG-INFO
+-rw-rw-r--   0 michael   (1000) michael   (1000)      283 2022-12-09 02:26:31.000000 xtensors-1.0.3/README.rst
+-rw-rw-r--   0 michael   (1000) michael   (1000)      102 2022-12-09 02:26:31.000000 xtensors-1.0.3/pyproject.toml
+-rw-rw-r--   0 michael   (1000) michael   (1000)      673 2023-04-07 04:45:03.758641 xtensors-1.0.3/setup.cfg
+-rw-rw-r--   0 michael   (1000) michael   (1000)       39 2022-12-09 02:26:31.000000 xtensors-1.0.3/setup.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.754641 xtensors-1.0.3/src/
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors/
+-rw-rw-r--   0 michael   (1000) michael   (1000)      221 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/__init__.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors/base/
+-rw-rw-r--   0 michael   (1000) michael   (1000)     1127 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/base/__init__.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     2854 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/base/_arg.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     2543 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/base/_args.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     2967 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/base/_binary_op.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     3237 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/base/_coords.py
+-rw-r--r--   0 michael   (1000) michael   (1000)      825 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/base/_misc.py
+-rw-rw-r--   0 michael   (1000) michael   (1000)     3156 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/base/_reduc.py
+-rw-rw-r--   0 michael   (1000) michael   (1000)      607 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/base/_reduc_2to1.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     1855 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/base/_ufuncs.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors/functionals/
+-rw-rw-r--   0 michael   (1000) michael   (1000)      149 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/functionals/__init__.py
+-rw-rw-r--   0 michael   (1000) michael   (1000)      853 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/functionals/base.py
+-rw-rw-r--   0 michael   (1000) michael   (1000)     2755 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/functionals/reductions.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors/learn/
+-rw-r--r--   0 michael   (1000) michael   (1000)       60 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/learn/__init__.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     1137 2023-04-07 04:44:08.000000 xtensors-1.0.3/src/xtensors/learn/confmat.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors/numpy/
+-rw-r--r--   0 michael   (1000) michael   (1000)      176 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/numpy/__init__.py
+-rw-r--r--   0 michael   (1000) michael   (1000)      941 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/numpy/_args.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     2637 2023-04-07 04:43:13.000000 xtensors-1.0.3/src/xtensors/numpy/_np.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors/tensor/
+-rw-r--r--   0 michael   (1000) michael   (1000)      227 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/__init__.py
+-rw-r--r--   0 michael   (1000) michael   (1000)    11303 2022-12-23 05:44:38.000000 xtensors-1.0.3/src/xtensors/tensor/_base.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     2365 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/_decors.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     1563 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/_slice.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors/tensor/basic_utils/
+-rw-r--r--   0 michael   (1000) michael   (1000)      451 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/basic_utils/__init__.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     5981 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/basic_utils/_axes.py
+-rw-r--r--   0 michael   (1000) michael   (1000)      754 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/basic_utils/_base.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     1765 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/basic_utils/_coords.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     4111 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/basic_utils/_dims.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     2244 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/basic_utils/_generalize.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     1093 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/basic_utils/_misc.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors/tensor/broadcast/
+-rw-r--r--   0 michael   (1000) michael   (1000)     3002 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/broadcast/__init__.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     4475 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/broadcast/_broadcast.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     3409 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/broadcast/_dimcast.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     6454 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/broadcast/_template.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     1739 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/broadcast/_types.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors/tensor/typing/
+-rw-r--r--   0 michael   (1000) michael   (1000)      320 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/typing/__init__.py
+-rw-r--r--   0 michael   (1000) michael   (1000)     1880 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/tensor/typing/_typing.py
+-rw-r--r--   0 michael   (1000) michael   (1000)       73 2022-12-09 02:26:32.000000 xtensors-1.0.3/src/xtensors/version.py
+drwxrwxr-x   0 michael   (1000) michael   (1000)        0 2023-04-07 04:45:03.758641 xtensors-1.0.3/src/xtensors.egg-info/
+-rw-rw-r--   0 michael   (1000) michael   (1000)      781 2023-04-07 04:45:03.000000 xtensors-1.0.3/src/xtensors.egg-info/PKG-INFO
+-rw-rw-r--   0 michael   (1000) michael   (1000)     1504 2023-04-07 04:45:03.000000 xtensors-1.0.3/src/xtensors.egg-info/SOURCES.txt
+-rw-rw-r--   0 michael   (1000) michael   (1000)        1 2023-04-07 04:45:03.000000 xtensors-1.0.3/src/xtensors.egg-info/dependency_links.txt
+-rw-rw-r--   0 michael   (1000) michael   (1000)       23 2023-04-07 04:45:03.000000 xtensors-1.0.3/src/xtensors.egg-info/requires.txt
+-rw-rw-r--   0 michael   (1000) michael   (1000)        9 2023-04-07 04:45:03.000000 xtensors-1.0.3/src/xtensors.egg-info/top_level.txt
```

### Comparing `xtensors-1.0.2/LICENSE` & `xtensors-1.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/PKG-INFO` & `xtensors-1.0.3/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: xtensors
-Version: 1.0.2
+Version: 1.0.3
 Summary: ND named tensor utilities
 Home-page: https://github.com/michael-960/xtensor
 Author: Michael Wang
 Author-email: mike.wang96029@gmail.com
 Project-URL: Bug Tracker, https://github.com/michael-960/xtensor/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `xtensors-1.0.2/setup.cfg` & `xtensors-1.0.3/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = xtensors
-version = 1.0.2
+version = 1.0.3
 author = Michael Wang
 author_email = mike.wang96029@gmail.com
 description = ND named tensor utilities
 long_description = file: README.rst
 long_description_content_type = text/x-rst
 url = https://github.com/michael-960/xtensor
 project_urls =
```

### Comparing `xtensors-1.0.2/src/xtensors/base/__init__.py` & `xtensors-1.0.3/src/xtensors/base/__init__.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/base/_arg.py` & `xtensors-1.0.3/src/xtensors/base/_arg.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/base/_args.py` & `xtensors-1.0.3/src/xtensors/base/_args.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/base/_binary_op.py` & `xtensors-1.0.3/src/xtensors/base/_binary_op.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/base/_coords.py` & `xtensors-1.0.3/src/xtensors/base/_coords.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/base/_misc.py` & `xtensors-1.0.3/src/xtensors/base/_misc.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/base/_reduc.py` & `xtensors-1.0.3/src/xtensors/base/_reduc.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/base/_reduc_2to1.py` & `xtensors-1.0.3/src/xtensors/base/_reduc_2to1.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/base/_ufuncs.py` & `xtensors-1.0.3/src/xtensors/base/_ufuncs.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/functionals/base.py` & `xtensors-1.0.3/src/xtensors/functionals/base.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/functionals/reductions.py` & `xtensors-1.0.3/src/xtensors/functionals/reductions.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/learn/confmat.py` & `xtensors-1.0.3/src/xtensors/learn/confmat.py`

 * *Files 13% similar despite different names*

```diff
@@ -5,15 +5,15 @@
 
 def confusion_matrix(truth: np.ndarray, pred: np.ndarray, /, *, n_classes: int) -> np.ndarray:
     '''
         X: (*, M)
         Y: (*, M)
     '''
     z = truth* n_classes + pred
-    cmat = xtnp.bincount(z, N=n_classes**2)
+    cmat = xtnp.bincount(z, N=n_classes**2, ignore_negative=True)
     return cmat.reshape(*cmat.shape[:-1], n_classes, n_classes)
 
 
 def get_confmat_function(target_dim: str, truth_dim: str, pred_dim: str, n_classes: int):
     @xtt.generalize_at_0
     @xtt.generalize_at_1
     def wrapped_confmat(truth: xtt.XTensor, pred: xtt.XTensor) -> xtt.XTensor:
```

### Comparing `xtensors-1.0.2/src/xtensors/numpy/_args.py` & `xtensors-1.0.3/src/xtensors/numpy/_args.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/numpy/_np.py` & `xtensors-1.0.3/src/xtensors/numpy/_np.py`

 * *Files 15% similar despite different names*

```diff
@@ -65,35 +65,44 @@
         _indices.append(indices % l)
         indices //= l
 
     return np.array(_indices[::-1]).transpose(*[i+1 for i in range(len(indices.shape))], 0)
         
 
 
-def bincount(x: NDArray[np.int_], N: int|None=None) -> NDArray[np.int_]:
-    '''
+def bincount(
+    x: NDArray[np.int_], N: int|None=None, *,
+    ignore_negative: bool = False    
+) -> NDArray[np.int_]:
+    """
         x: (*, M)
         return: (*, N)
-    '''
+
+        count the number of occurrences along the last axis of x
+
+        N: number of bins
+
+        ignore_negative: whether to ignore negative numbers
+    """
 
     if N is None:
         N = np.max(x) + 1
 
     shape = x.shape[:-1]
 
     # (D, M)
     _x = flatten(x, [a for a in range(len(x.shape))][:-1], position='left')
 
     D = _x.shape[0]
     index = np.arange(D).reshape(D, 1)
 
-
     N = cast(int, N)
 
-    y = np.bincount((index*N + _x).reshape(-1), minlength=N*D).reshape(*shape, N)
+    stats = (index*N + _x).reshape(-1)
 
-    return y
+    if ignore_negative:
+        stats = stats[np.where(stats >= 0)]
 
+    y = np.bincount(stats, minlength=N*D).reshape(*shape, N)
 
+    return y
 
-    
-
```

### Comparing `xtensors-1.0.2/src/xtensors/tensor/_base.py` & `xtensors-1.0.3/src/xtensors/tensor/_base.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/_decors.py` & `xtensors-1.0.3/src/xtensors/tensor/_decors.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/_slice.py` & `xtensors-1.0.3/src/xtensors/tensor/_slice.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/basic_utils/_axes.py` & `xtensors-1.0.3/src/xtensors/tensor/basic_utils/_axes.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/basic_utils/_base.py` & `xtensors-1.0.3/src/xtensors/tensor/basic_utils/_base.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/basic_utils/_coords.py` & `xtensors-1.0.3/src/xtensors/tensor/basic_utils/_coords.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/basic_utils/_dims.py` & `xtensors-1.0.3/src/xtensors/tensor/basic_utils/_dims.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/basic_utils/_generalize.py` & `xtensors-1.0.3/src/xtensors/tensor/basic_utils/_generalize.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/basic_utils/_misc.py` & `xtensors-1.0.3/src/xtensors/tensor/basic_utils/_misc.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/broadcast/__init__.py` & `xtensors-1.0.3/src/xtensors/tensor/broadcast/__init__.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/broadcast/_broadcast.py` & `xtensors-1.0.3/src/xtensors/tensor/broadcast/_broadcast.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/broadcast/_dimcast.py` & `xtensors-1.0.3/src/xtensors/tensor/broadcast/_dimcast.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/broadcast/_template.py` & `xtensors-1.0.3/src/xtensors/tensor/broadcast/_template.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/broadcast/_types.py` & `xtensors-1.0.3/src/xtensors/tensor/broadcast/_types.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors/tensor/typing/_typing.py` & `xtensors-1.0.3/src/xtensors/tensor/typing/_typing.py`

 * *Files identical despite different names*

### Comparing `xtensors-1.0.2/src/xtensors.egg-info/PKG-INFO` & `xtensors-1.0.3/src/xtensors.egg-info/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: xtensors
-Version: 1.0.2
+Version: 1.0.3
 Summary: ND named tensor utilities
 Home-page: https://github.com/michael-960/xtensor
 Author: Michael Wang
 Author-email: mike.wang96029@gmail.com
 Project-URL: Bug Tracker, https://github.com/michael-960/xtensor/issues
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
```

### Comparing `xtensors-1.0.2/src/xtensors.egg-info/SOURCES.txt` & `xtensors-1.0.3/src/xtensors.egg-info/SOURCES.txt`

 * *Files identical despite different names*

