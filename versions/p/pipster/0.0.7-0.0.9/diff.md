# Comparing `tmp/pipster-0.0.7.tar.gz` & `tmp/pipster-0.0.9.tar.gz`

## Comparing `pipster-0.0.7.tar` & `pipster-0.0.9.tar`

### file list

```diff
@@ -1,26 +1,26 @@
--rw-r--r--   0        0        0      125 2020-02-02 00:00:00.000000 pipster-0.0.7/.git_archival.txt
--rw-r--r--   0        0        0       32 2020-02-02 00:00:00.000000 pipster-0.0.7/.gitattributes
--rw-r--r--   0        0        0     2476 2020-02-02 00:00:00.000000 pipster-0.0.7/.github/workflows/test_build_publish.yml
--rw-r--r--   0        0        0    17896 2020-02-02 00:00:00.000000 pipster-0.0.7/images/pipster_138x250.jpg
--rw-r--r--   0        0        0    23684 2020-02-02 00:00:00.000000 pipster-0.0.7/images/pipster_166x300.jpg
--rw-r--r--   0        0        0    44659 2020-02-02 00:00:00.000000 pipster-0.0.7/images/pipster_250x453.jpg
--rw-r--r--   0        0        0    59147 2020-02-02 00:00:00.000000 pipster-0.0.7/images/pipster_300x544.jpg
--rw-r--r--   0        0        0    56840 2020-02-02 00:00:00.000000 pipster-0.0.7/images/pipster_orig.png
--rwxr-xr-x   0        0        0      179 2020-02-02 00:00:00.000000 pipster-0.0.7/scripts/pre-commit
--rw-r--r--   0        0        0      180 2020-02-02 00:00:00.000000 pipster-0.0.7/src/pipster/__init__.py
--rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 pipster-0.0.7/src/pipster/_version.py
--rw-r--r--   0        0        0     3938 2020-02-02 00:00:00.000000 pipster-0.0.7/src/pipster/autoinstall.py
--rw-r--r--   0        0        0     9402 2020-02-02 00:00:00.000000 pipster-0.0.7/src/pipster/install.py
--rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 pipster-0.0.7/tests/data/constraints.txt
--rw-r--r--   0        0        0      372 2020-02-02 00:00:00.000000 pipster-0.0.7/tests/data/imports.py
--rw-r--r--   0        0        0       27 2020-02-02 00:00:00.000000 pipster-0.0.7/tests/data/other-requirements.txt
--rw-r--r--   0        0        0      843 2020-02-02 00:00:00.000000 pipster-0.0.7/tests/data/requirements.txt
--rw-r--r--   0        0        0     1842 2020-02-02 00:00:00.000000 pipster-0.0.7/tests/data/packages/simplewheel-1.0-py2.py3-none-any.whl
--rw-r--r--   0        0        0     1835 2020-02-02 00:00:00.000000 pipster-0.0.7/tests/data/packages/simplewheel-2.0-py2.py3-none-any.whl
--rw-r--r--   0        0        0      305 2020-02-02 00:00:00.000000 pipster-0.0.7/tests/functional/test_autoinstall.py
--rw-r--r--   0        0        0     8653 2020-02-02 00:00:00.000000 pipster-0.0.7/tests/functional/test_install.py
--rw-r--r--   0        0        0       67 2020-02-02 00:00:00.000000 pipster-0.0.7/.gitignore
--rw-r--r--   0        0        0     1097 2020-02-02 00:00:00.000000 pipster-0.0.7/LICENSE
--rw-r--r--   0        0        0     3096 2020-02-02 00:00:00.000000 pipster-0.0.7/README.md
--rw-r--r--   0        0        0     1353 2020-02-02 00:00:00.000000 pipster-0.0.7/pyproject.toml
--rw-r--r--   0        0        0     5514 2020-02-02 00:00:00.000000 pipster-0.0.7/PKG-INFO
+-rw-r--r--   0        0        0      125 2020-02-02 00:00:00.000000 pipster-0.0.9/.git_archival.txt
+-rw-r--r--   0        0        0       32 2020-02-02 00:00:00.000000 pipster-0.0.9/.gitattributes
+-rw-r--r--   0        0        0     2476 2020-02-02 00:00:00.000000 pipster-0.0.9/.github/workflows/test_build_publish.yml
+-rw-r--r--   0        0        0    17896 2020-02-02 00:00:00.000000 pipster-0.0.9/images/pipster_138x250.jpg
+-rw-r--r--   0        0        0    23684 2020-02-02 00:00:00.000000 pipster-0.0.9/images/pipster_166x300.jpg
+-rw-r--r--   0        0        0    44659 2020-02-02 00:00:00.000000 pipster-0.0.9/images/pipster_250x453.jpg
+-rw-r--r--   0        0        0    59147 2020-02-02 00:00:00.000000 pipster-0.0.9/images/pipster_300x544.jpg
+-rw-r--r--   0        0        0    56840 2020-02-02 00:00:00.000000 pipster-0.0.9/images/pipster_orig.png
+-rwxr-xr-x   0        0        0      179 2020-02-02 00:00:00.000000 pipster-0.0.9/scripts/pre-commit
+-rw-r--r--   0        0        0      180 2020-02-02 00:00:00.000000 pipster-0.0.9/src/pipster/__init__.py
+-rw-r--r--   0        0        0       52 2020-02-02 00:00:00.000000 pipster-0.0.9/src/pipster/_version.py
+-rw-r--r--   0        0        0     3938 2020-02-02 00:00:00.000000 pipster-0.0.9/src/pipster/autoinstall.py
+-rw-r--r--   0        0        0     9402 2020-02-02 00:00:00.000000 pipster-0.0.9/src/pipster/install.py
+-rw-r--r--   0        0        0       17 2020-02-02 00:00:00.000000 pipster-0.0.9/tests/data/constraints.txt
+-rw-r--r--   0        0        0      372 2020-02-02 00:00:00.000000 pipster-0.0.9/tests/data/imports.py
+-rw-r--r--   0        0        0       27 2020-02-02 00:00:00.000000 pipster-0.0.9/tests/data/other-requirements.txt
+-rw-r--r--   0        0        0      843 2020-02-02 00:00:00.000000 pipster-0.0.9/tests/data/requirements.txt
+-rw-r--r--   0        0        0     1842 2020-02-02 00:00:00.000000 pipster-0.0.9/tests/data/packages/simplewheel-1.0-py2.py3-none-any.whl
+-rw-r--r--   0        0        0     1835 2020-02-02 00:00:00.000000 pipster-0.0.9/tests/data/packages/simplewheel-2.0-py2.py3-none-any.whl
+-rw-r--r--   0        0        0      305 2020-02-02 00:00:00.000000 pipster-0.0.9/tests/functional/test_autoinstall.py
+-rw-r--r--   0        0        0     8653 2020-02-02 00:00:00.000000 pipster-0.0.9/tests/functional/test_install.py
+-rw-r--r--   0        0        0       67 2020-02-02 00:00:00.000000 pipster-0.0.9/.gitignore
+-rw-r--r--   0        0        0     1097 2020-02-02 00:00:00.000000 pipster-0.0.9/LICENSE
+-rw-r--r--   0        0        0     3092 2020-02-02 00:00:00.000000 pipster-0.0.9/README.md
+-rw-r--r--   0        0        0     1353 2020-02-02 00:00:00.000000 pipster-0.0.9/pyproject.toml
+-rw-r--r--   0        0        0     5510 2020-02-02 00:00:00.000000 pipster-0.0.9/PKG-INFO
```

### Comparing `pipster-0.0.7/.github/workflows/test_build_publish.yml` & `pipster-0.0.9/.github/workflows/test_build_publish.yml`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/images/pipster_138x250.jpg` & `pipster-0.0.9/images/pipster_138x250.jpg`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/images/pipster_166x300.jpg` & `pipster-0.0.9/images/pipster_166x300.jpg`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/images/pipster_250x453.jpg` & `pipster-0.0.9/images/pipster_250x453.jpg`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/images/pipster_300x544.jpg` & `pipster-0.0.9/images/pipster_300x544.jpg`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/images/pipster_orig.png` & `pipster-0.0.9/images/pipster_orig.png`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/src/pipster/autoinstall.py` & `pipster-0.0.9/src/pipster/autoinstall.py`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/src/pipster/install.py` & `pipster-0.0.9/src/pipster/install.py`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/tests/data/requirements.txt` & `pipster-0.0.9/tests/data/requirements.txt`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/tests/data/packages/simplewheel-1.0-py2.py3-none-any.whl` & `pipster-0.0.9/tests/data/packages/simplewheel-1.0-py2.py3-none-any.whl`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/tests/data/packages/simplewheel-2.0-py2.py3-none-any.whl` & `pipster-0.0.9/tests/data/packages/simplewheel-2.0-py2.py3-none-any.whl`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/tests/functional/test_install.py` & `pipster-0.0.9/tests/functional/test_install.py`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/LICENSE` & `pipster-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/README.md` & `pipster-0.0.9/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,11 +1,9 @@
 # pipster
 
-> 
-
 <div align="center">
     <img src="https://raw.githubusercontent.com/reynoldsnlp/pipster/main/images/pipster_138x250.jpg" alt="Pipster logo" width="138">
 <br/>
 <br/>
 
 | | |
 | --- | --- |
```

### Comparing `pipster-0.0.7/pyproject.toml` & `pipster-0.0.9/pyproject.toml`

 * *Files identical despite different names*

### Comparing `pipster-0.0.7/PKG-INFO` & `pipster-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pipster
-Version: 0.0.7
+Version: 0.0.9
 Summary: pip install from inside your scripts
 Project-URL: Homepage, https://github.com/reynoldsnlp/pipster
 Project-URL: Bug Tracker, https://github.com/reynoldsnlp/pipster/issues
 Author-email: Robert Reynolds <robert_reynolds@byu.edu>
 License: Copyright (c) 2018-2019 The pipster developers (see pyproject.toml file)
         
         Permission is hereby granted, free of charge, to any person obtaining
@@ -46,16 +46,14 @@
 Provides-Extra: test
 Requires-Dist: pytest-cov>=4.0; extra == 'test'
 Requires-Dist: pytest>=6.0; extra == 'test'
 Description-Content-Type: text/markdown
 
 # pipster
 
-> 
-
 <div align="center">
     <img src="https://raw.githubusercontent.com/reynoldsnlp/pipster/main/images/pipster_138x250.jpg" alt="Pipster logo" width="138">
 <br/>
 <br/>
 
 | | |
 | --- | --- |
```

