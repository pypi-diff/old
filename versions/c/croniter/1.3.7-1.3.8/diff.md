# Comparing `tmp/croniter-1.3.7.tar.gz` & `tmp/croniter-1.3.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "croniter-1.3.7.tar", last modified: Tue Sep  6 16:47:21 2022, max compression
+gzip compressed data, was "croniter-1.3.8.tar", last modified: Tue Nov 22 08:07:19 2022, max compression
```

## Comparing `croniter-1.3.7.tar` & `croniter-1.3.8.tar`

### file list

```diff
@@ -1,32 +1,31 @@
-drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-09-06 16:47:21.874700 croniter-1.3.7/
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      136 2022-09-06 16:47:21.000000 croniter-1.3.7/MANIFEST.in
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    22848 2022-09-06 16:47:21.874700 croniter-1.3.7/PKG-INFO
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    11054 2022-09-06 16:47:21.000000 croniter-1.3.7/README.rst
-drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-09-06 16:47:21.874700 croniter-1.3.7/docs/
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    10554 2022-09-06 16:47:21.000000 croniter-1.3.7/docs/CHANGES.rst
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     1064 2022-09-06 16:47:21.000000 croniter-1.3.7/docs/LICENSE
-drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-09-06 16:47:21.874700 croniter-1.3.7/requirements/
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)       21 2022-09-06 16:47:21.000000 croniter-1.3.7/requirements/base.txt
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)       44 2022-09-06 16:47:21.000000 croniter-1.3.7/requirements/release.txt
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      109 2022-09-06 16:47:21.000000 croniter-1.3.7/requirements/test.txt
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      324 2022-09-06 16:47:21.874700 croniter-1.3.7/setup.cfg
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     2027 2022-09-06 16:47:21.000000 croniter-1.3.7/setup.py
-drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-09-06 16:47:21.874700 croniter-1.3.7/src/
-drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-09-06 16:47:21.874700 croniter-1.3.7/src/croniter/
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      380 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter/__init__.py
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    35173 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter/croniter.py
-drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-09-06 16:47:21.874700 croniter-1.3.7/src/croniter/tests/
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)        0 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter/tests/__init__.py
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      282 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter/tests/base.py
--rwxrwxr-x   0 kiorky    (1000) kiorky    (1000)    55865 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter/tests/test_croniter.py
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     6646 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter/tests/test_croniter_hash.py
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     1705 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter/tests/test_croniter_random.py
--rwxrwxr-x   0 kiorky    (1000) kiorky    (1000)     6786 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter/tests/test_croniter_range.py
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     5715 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter/tests/test_speed.py
-drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-09-06 16:47:21.874700 croniter-1.3.7/src/croniter.egg-info/
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    22848 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter.egg-info/PKG-INFO
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      630 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter.egg-info/SOURCES.txt
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)        1 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter.egg-info/dependency_links.txt
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)       16 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter.egg-info/requires.txt
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)        9 2022-09-06 16:47:21.000000 croniter-1.3.7/src/croniter.egg-info/top_level.txt
--rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      601 2022-09-06 16:47:21.000000 croniter-1.3.7/tox.ini
+drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-11-22 08:07:19.349861 croniter-1.3.8/
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    10665 2022-11-22 08:07:19.000000 croniter-1.3.8/CHANGELOG.rst
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     1064 2022-11-22 08:07:19.000000 croniter-1.3.8/LICENSE
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      136 2022-11-22 08:07:19.000000 croniter-1.3.8/MANIFEST.in
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    23032 2022-11-22 08:07:19.349861 croniter-1.3.8/PKG-INFO
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    11054 2022-11-22 08:07:19.000000 croniter-1.3.8/README.rst
+drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-11-22 08:07:19.349861 croniter-1.3.8/requirements/
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)       21 2022-11-22 08:07:19.000000 croniter-1.3.8/requirements/base.txt
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)       44 2022-11-22 08:07:19.000000 croniter-1.3.8/requirements/release.txt
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      109 2022-11-22 08:07:19.000000 croniter-1.3.8/requirements/test.txt
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      324 2022-11-22 08:07:19.349861 croniter-1.3.8/setup.cfg
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     2071 2022-11-22 08:07:19.000000 croniter-1.3.8/setup.py
+drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-11-22 08:07:19.349861 croniter-1.3.8/src/
+drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-11-22 08:07:19.349861 croniter-1.3.8/src/croniter/
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      380 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter/__init__.py
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    35173 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter/croniter.py
+drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-11-22 08:07:19.349861 croniter-1.3.8/src/croniter/tests/
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)        0 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter/tests/__init__.py
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      282 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter/tests/base.py
+-rwxrwxr-x   0 kiorky    (1000) kiorky    (1000)    55865 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter/tests/test_croniter.py
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     6646 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter/tests/test_croniter_hash.py
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     1705 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter/tests/test_croniter_random.py
+-rwxrwxr-x   0 kiorky    (1000) kiorky    (1000)     6786 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter/tests/test_croniter_range.py
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)     5715 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter/tests/test_speed.py
+drwxrwxr-x   0 kiorky    (1000) kiorky    (1000)        0 2022-11-22 08:07:19.349861 croniter-1.3.8/src/croniter.egg-info/
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)    23032 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter.egg-info/PKG-INFO
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      622 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter.egg-info/SOURCES.txt
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)        1 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter.egg-info/dependency_links.txt
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)       16 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter.egg-info/requires.txt
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)        9 2022-11-22 08:07:19.000000 croniter-1.3.8/src/croniter.egg-info/top_level.txt
+-rw-rw-r--   0 kiorky    (1000) kiorky    (1000)      619 2022-11-22 08:07:19.000000 croniter-1.3.8/tox.ini
```

### Comparing `croniter-1.3.7/PKG-INFO` & `croniter-1.3.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: croniter
-Version: 1.3.7
+Version: 1.3.8
 Summary: croniter provides iteration for datetime object with cron like format
 Home-page: http://github.com/kiorky/croniter
 Author: Matsumoto Taichi, kiorky
 Author-email: taichino@gmail.com, kiorky@cryptelium.net
 License: MIT License
 Keywords: datetime,iterator,cron
 Platform: UNKNOWN
@@ -20,16 +20,18 @@
 Classifier: Programming Language :: Python :: 3.4
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Requires-Python: >=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*
+License-File: LICENSE
 
 Introduction
 ============
 
 .. contents::
 
 
@@ -317,14 +319,20 @@
     - Ryan Finnie (rfinnie)
 
 
 
 Changelog
 ==============
 
+1.3.8 (2022-11-22)
+------------------
+
+- Add Python 3.11 support and move docs files to main folder [rafsaf]
+
+
 1.3.7 (2022-09-06)
 ------------------
 
 - fix tests
 - Fix croniter_range infinite loop  [Shachar Snapiri <ssnapiri@paloaltonetworks.com>]
```

### Comparing `croniter-1.3.7/README.rst` & `croniter-1.3.8/README.rst`

 * *Files identical despite different names*

### Comparing `croniter-1.3.7/docs/CHANGES.rst` & `croniter-1.3.8/CHANGELOG.rst`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,16 @@
 Changelog
 ==============
 
+1.3.8 (2022-11-22)
+------------------
+
+- Add Python 3.11 support and move docs files to main folder [rafsaf]
+
+
 1.3.7 (2022-09-06)
 ------------------
 
 - fix tests
 - Fix croniter_range infinite loop  [Shachar Snapiri <ssnapiri@paloaltonetworks.com>]
```

### Comparing `croniter-1.3.7/docs/LICENSE` & `croniter-1.3.8/LICENSE`

 * *Files identical despite different names*

### Comparing `croniter-1.3.7/setup.py` & `croniter-1.3.8/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -14,21 +14,21 @@
     for a in read('requirements/base.txt').splitlines()
     if a.strip() and not a.startswith(('#', '-'))
 ]
 
 long_description = "\n\n".join(
     [
         read('README.rst'),
-        read('docs', 'CHANGES.rst'),
+        read('CHANGELOG.rst'),
     ]
 )
 
 setup(
     name='croniter',
-    version='1.3.7',
+    version='1.3.8',
     py_modules=['croniter', ],
     description=(
         'croniter provides iteration for datetime '
         'object with cron like format'
     ),
     long_description=long_description,
     author="Matsumoto Taichi, kiorky",
@@ -51,13 +51,14 @@
         "Programming Language :: Python :: 3.4",
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11",
         "Topic :: Software Development :: Libraries :: Python Modules"],
     packages=find_packages('src', exclude=['tests*', '*.tests*']),
     package_dir={'': 'src'},
     include_package_data=True,
     exclude_package_data={'croniter': ['tests/*']},
 )
```

### Comparing `croniter-1.3.7/src/croniter/croniter.py` & `croniter-1.3.8/src/croniter/croniter.py`

 * *Files identical despite different names*

### Comparing `croniter-1.3.7/src/croniter/tests/test_croniter.py` & `croniter-1.3.8/src/croniter/tests/test_croniter.py`

 * *Files identical despite different names*

### Comparing `croniter-1.3.7/src/croniter/tests/test_croniter_hash.py` & `croniter-1.3.8/src/croniter/tests/test_croniter_hash.py`

 * *Files identical despite different names*

### Comparing `croniter-1.3.7/src/croniter/tests/test_croniter_random.py` & `croniter-1.3.8/src/croniter/tests/test_croniter_random.py`

 * *Files identical despite different names*

### Comparing `croniter-1.3.7/src/croniter/tests/test_croniter_range.py` & `croniter-1.3.8/src/croniter/tests/test_croniter_range.py`

 * *Files identical despite different names*

### Comparing `croniter-1.3.7/src/croniter/tests/test_speed.py` & `croniter-1.3.8/src/croniter/tests/test_speed.py`

 * *Files identical despite different names*

### Comparing `croniter-1.3.7/src/croniter.egg-info/PKG-INFO` & `croniter-1.3.8/src/croniter.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: croniter
-Version: 1.3.7
+Version: 1.3.8
 Summary: croniter provides iteration for datetime object with cron like format
 Home-page: http://github.com/kiorky/croniter
 Author: Matsumoto Taichi, kiorky
 Author-email: taichino@gmail.com, kiorky@cryptelium.net
 License: MIT License
 Keywords: datetime,iterator,cron
 Platform: UNKNOWN
@@ -20,16 +20,18 @@
 Classifier: Programming Language :: Python :: 3.4
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Requires-Python: >=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*
+License-File: LICENSE
 
 Introduction
 ============
 
 .. contents::
 
 
@@ -317,14 +319,20 @@
     - Ryan Finnie (rfinnie)
 
 
 
 Changelog
 ==============
 
+1.3.8 (2022-11-22)
+------------------
+
+- Add Python 3.11 support and move docs files to main folder [rafsaf]
+
+
 1.3.7 (2022-09-06)
 ------------------
 
 - fix tests
 - Fix croniter_range infinite loop  [Shachar Snapiri <ssnapiri@paloaltonetworks.com>]
```

### Comparing `croniter-1.3.7/src/croniter.egg-info/SOURCES.txt` & `croniter-1.3.8/src/croniter.egg-info/SOURCES.txt`

 * *Files 7% similar despite different names*

```diff
@@ -1,14 +1,14 @@
+CHANGELOG.rst
+LICENSE
 MANIFEST.in
 README.rst
 setup.cfg
 setup.py
 tox.ini
-docs/CHANGES.rst
-docs/LICENSE
 requirements/base.txt
 requirements/release.txt
 requirements/test.txt
 src/croniter/__init__.py
 src/croniter/croniter.py
 src/croniter.egg-info/PKG-INFO
 src/croniter.egg-info/SOURCES.txt
```

### Comparing `croniter-1.3.7/tox.ini` & `croniter-1.3.8/tox.ini`

 * *Files 22% similar despite different names*

```diff
@@ -1,21 +1,21 @@
 [tox]
 minversion = 2.3
 envlist =
-    {py26,py27,py34,py35,py36,py37,py38,py39,py310}-std
+    {py26,py27,py34,py35,py36,py37,py38,py39,py310,py311}-std
     py27-coverage
 skipsdist = true
 
 [testenv]
 usedevelop = true
 deps =
     -r{toxinidir}/requirements/test.txt
 whitelist_externals = /bin/sh
 setenv =
     COVERAGE_FILE={envdir}/coverage_report
 changedir = src
 commands =
-    {py26,py27,py34,py35,py36,py37,py38,py39,py310}-std: py.test -v .
-    {py27,py34,py35,py36,py37,py38,py39,py310}-std: flake8 croniter/croniter.py
+    {py26,py27,py34,py35,py36,py37,py38,py39,py310,py311}-std: py.test -v .
+    {py27,py34,py35,py36,py37,py38,py39,py310,py311}-std: flake8 croniter/croniter.py
     py27-coverage: coverage erase
     py27-coverage: sh -c 'cd .. && coverage run $(which py.test) -v src'
     py27-coverage: coverage report
```

