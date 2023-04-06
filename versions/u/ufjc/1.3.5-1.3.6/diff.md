# Comparing `tmp/ufjc-1.3.5.tar.gz` & `tmp/ufjc-1.3.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ufjc-1.3.5.tar", last modified: Thu Oct 13 20:44:39 2022, max compression
+gzip compressed data, was "ufjc-1.3.6.tar", last modified: Thu Apr  6 21:30:47 2023, max compression
```

## Comparing `ufjc-1.3.5.tar` & `ufjc-1.3.6.tar`

### file list

```diff
@@ -1,32 +1,32 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 20:44:39.037937 ufjc-1.3.5/
--rw-r--r--   0 runner    (1001) docker     (121)     1663 2022-10-13 20:44:30.000000 ufjc-1.3.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     4853 2022-10-13 20:44:39.037937 ufjc-1.3.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     3673 2022-10-13 20:44:30.000000 ufjc-1.3.5/README.rst
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-10-13 20:44:39.037937 ufjc-1.3.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2298 2022-10-13 20:44:30.000000 ufjc-1.3.5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 20:44:39.037937 ufjc-1.3.5/ufjc/
--rw-r--r--   0 runner    (1001) docker     (121)       68 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    21360 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/core.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 20:44:39.037937 ufjc-1.3.5/ufjc/examples/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/examples/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      427 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/examples/__main__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4466 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/examples/approaches.py
--rw-r--r--   0 runner    (1001) docker     (121)     6537 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/examples/asymptotics.py
--rw-r--r--   0 runner    (1001) docker     (121)     5220 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/examples/error.py
--rw-r--r--   0 runner    (1001) docker     (121)    11563 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/isometric.py
--rw-r--r--   0 runner    (1001) docker     (121)    16805 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/isotensional.py
--rw-r--r--   0 runner    (1001) docker     (121)    13717 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/monte_carlo.py
--rw-r--r--   0 runner    (1001) docker     (121)    26991 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/potential.py
--rw-r--r--   0 runner    (1001) docker     (121)     7978 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/swfjc.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 20:44:39.037937 ufjc-1.3.5/ufjc/tests/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      352 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/tests/__main__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1474 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/tests/test_examples.py
--rw-r--r--   0 runner    (1001) docker     (121)     1096 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/tests/test_style.py
--rw-r--r--   0 runner    (1001) docker     (121)     8992 2022-10-13 20:44:30.000000 ufjc-1.3.5/ufjc/utility.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-10-13 20:44:39.037937 ufjc-1.3.5/ufjc.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     4853 2022-10-13 20:44:38.000000 ufjc-1.3.5/ufjc.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      534 2022-10-13 20:44:39.000000 ufjc-1.3.5/ufjc.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-10-13 20:44:38.000000 ufjc-1.3.5/ufjc.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      268 2022-10-13 20:44:38.000000 ufjc-1.3.5/ufjc.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        5 2022-10-13 20:44:38.000000 ufjc-1.3.5/ufjc.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:30:47.385484 ufjc-1.3.6/
+-rw-r--r--   0 runner    (1001) docker     (122)     1541 2023-04-06 21:30:37.000000 ufjc-1.3.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)     5423 2023-04-06 21:30:47.385484 ufjc-1.3.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)     4243 2023-04-06 21:30:37.000000 ufjc-1.3.6/README.rst
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-06 21:30:47.385484 ufjc-1.3.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     2298 2023-04-06 21:30:37.000000 ufjc-1.3.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:30:47.385484 ufjc-1.3.6/ufjc/
+-rw-r--r--   0 runner    (1001) docker     (122)       68 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    21360 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/core.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:30:47.385484 ufjc-1.3.6/ufjc/examples/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/examples/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      427 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/examples/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     4466 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/examples/approaches.py
+-rw-r--r--   0 runner    (1001) docker     (122)     6537 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/examples/asymptotics.py
+-rw-r--r--   0 runner    (1001) docker     (122)     5220 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/examples/error.py
+-rw-r--r--   0 runner    (1001) docker     (122)    11563 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/isometric.py
+-rw-r--r--   0 runner    (1001) docker     (122)    16805 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/isotensional.py
+-rw-r--r--   0 runner    (1001) docker     (122)    13717 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/monte_carlo.py
+-rw-r--r--   0 runner    (1001) docker     (122)    26991 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/potential.py
+-rw-r--r--   0 runner    (1001) docker     (122)     7978 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/swfjc.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:30:47.385484 ufjc-1.3.6/ufjc/tests/
+-rw-r--r--   0 runner    (1001) docker     (122)        0 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)      352 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/tests/__main__.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1474 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/tests/test_examples.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1096 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/tests/test_style.py
+-rw-r--r--   0 runner    (1001) docker     (122)     8992 2023-04-06 21:30:37.000000 ufjc-1.3.6/ufjc/utility.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:30:47.385484 ufjc-1.3.6/ufjc.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     5423 2023-04-06 21:30:47.000000 ufjc-1.3.6/ufjc.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      534 2023-04-06 21:30:47.000000 ufjc-1.3.6/ufjc.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 21:30:47.000000 ufjc-1.3.6/ufjc.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      268 2023-04-06 21:30:47.000000 ufjc-1.3.6/ufjc.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        5 2023-04-06 21:30:47.000000 ufjc-1.3.6/ufjc.egg-info/top_level.txt
```

### Comparing `ufjc-1.3.5/LICENSE` & `ufjc-1.3.6/LICENSE`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 BSD 3-Clause License
 
-Copyright 2022 National Technology & Engineering Solutions of Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software.
+Copyright 2022 National Technology & Engineering Solutions of Sandia, LLC.
 
 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:
 
 1. Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.
```

### Comparing `ufjc-1.3.5/PKG-INFO` & `ufjc-1.3.6/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ufjc
-Version: 1.3.5
+Version: 1.3.6
 Summary: The Python package for the uFJC single-chain model.
 Home-page: https://sandialabs.github.io/uFJC
 Author: Michael R. Buche, Scott J. Grutzik
 Author-email: mrbuche@sandia.gov, sjgrutz@sandia.gov
 License: BSD-3-Clause
 Project-URL: Anaconda, https://anaconda.org/mrbuche/ufjc
 Project-URL: Documentation, https://ufjc.readthedocs.io
@@ -27,15 +27,19 @@
 Provides-Extra: all
 License-File: LICENSE
 
 ####
 uFJC
 ####
 
-|build| |docs| |codecov| |coveralls| |pyversions| |pypi| |conda| |docker| |license| |zenodo|
+****************************************************************************************************************
+THIS PACKAGE IS DEPRECATED. PLEASE USE THE `POLYMERS MODELING LIBRARY <https://sandialabs.github.io/Polymers>`_.
+****************************************************************************************************************
+
+|build| |docs| |codecov| |coveralls| |codefactor| |pyversions| |pypi| |conda| |docker| |license| |zenodo|
 
 The Python package for the uFJC single-chain model.
 
 ************
 Installation
 ************
 
@@ -90,25 +94,28 @@
 *********
 
 Copyright 2022 National Technology & Engineering Solutions of Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software.
 
 ..
     Badges ========================================================================
 
+.. |build| image:: https://img.shields.io/github/actions/workflow/status/sandialabs/ufjc/main.yml?branch=main&label=GitHub&logo=github
+    :target: https://github.com/sandialabs/ufjc
+
 .. |docs| image:: https://img.shields.io/readthedocs/ufjc?logo=readthedocs&label=Read%20the%20Docs
     :target: https://ufjc.readthedocs.io/en/latest/
 
-.. |build| image:: https://img.shields.io/github/workflow/status/sandialabs/ufjc/main?label=GitHub&logo=github
-    :target: https://github.com/sandialabs/ufjc
+.. |codecov| image:: https://img.shields.io/codecov/c/github/sandialabs/ufjc?label=Codecov&logo=codecov
+    :target: https://codecov.io/gh/sandialabs/ufjc
 
 .. |coveralls| image:: https://img.shields.io/coveralls/github/sandialabs/ufjc?logo=coveralls&label=Coveralls
     :target: https://coveralls.io/github/sandialabs/ufjc?branch=main
 
-.. |codecov| image:: https://img.shields.io/codecov/c/github/sandialabs/ufjc?label=Codecov&logo=codecov
-    :target: https://codecov.io/gh/sandialabs/ufjc
+.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/sandialabs/ufjc?label=Codefactor&logo=codefactor
+   :target: https://www.codefactor.io/repository/github/sandialabs/ufjc
 
 .. |pyversions| image:: https://img.shields.io/pypi/pyversions/ufjc.svg?logo=python&logoColor=FBE072&color=4B8BBE&label=Python
     :target: https://pypi.org/project/ufjc/
 
 .. |pypi| image:: https://img.shields.io/pypi/v/ufjc?logo=pypi&logoColor=FBE072&label=PyPI&color=4B8BBE
     :target: https://pypi.org/project/ufjc/
```

### Comparing `ufjc-1.3.5/README.rst` & `ufjc-1.3.6/README.rst`

 * *Files 10% similar despite different names*

```diff
@@ -1,12 +1,16 @@
 ####
 uFJC
 ####
 
-|build| |docs| |codecov| |coveralls| |pyversions| |pypi| |conda| |docker| |license| |zenodo|
+****************************************************************************************************************
+THIS PACKAGE IS DEPRECATED. PLEASE USE THE `POLYMERS MODELING LIBRARY <https://sandialabs.github.io/Polymers>`_.
+****************************************************************************************************************
+
+|build| |docs| |codecov| |coveralls| |codefactor| |pyversions| |pypi| |conda| |docker| |license| |zenodo|
 
 The Python package for the uFJC single-chain model.
 
 ************
 Installation
 ************
 
@@ -61,25 +65,28 @@
 *********
 
 Copyright 2022 National Technology & Engineering Solutions of Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software.
 
 ..
     Badges ========================================================================
 
+.. |build| image:: https://img.shields.io/github/actions/workflow/status/sandialabs/ufjc/main.yml?branch=main&label=GitHub&logo=github
+    :target: https://github.com/sandialabs/ufjc
+
 .. |docs| image:: https://img.shields.io/readthedocs/ufjc?logo=readthedocs&label=Read%20the%20Docs
     :target: https://ufjc.readthedocs.io/en/latest/
 
-.. |build| image:: https://img.shields.io/github/workflow/status/sandialabs/ufjc/main?label=GitHub&logo=github
-    :target: https://github.com/sandialabs/ufjc
+.. |codecov| image:: https://img.shields.io/codecov/c/github/sandialabs/ufjc?label=Codecov&logo=codecov
+    :target: https://codecov.io/gh/sandialabs/ufjc
 
 .. |coveralls| image:: https://img.shields.io/coveralls/github/sandialabs/ufjc?logo=coveralls&label=Coveralls
     :target: https://coveralls.io/github/sandialabs/ufjc?branch=main
 
-.. |codecov| image:: https://img.shields.io/codecov/c/github/sandialabs/ufjc?label=Codecov&logo=codecov
-    :target: https://codecov.io/gh/sandialabs/ufjc
+.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/sandialabs/ufjc?label=Codefactor&logo=codefactor
+   :target: https://www.codefactor.io/repository/github/sandialabs/ufjc
 
 .. |pyversions| image:: https://img.shields.io/pypi/pyversions/ufjc.svg?logo=python&logoColor=FBE072&color=4B8BBE&label=Python
     :target: https://pypi.org/project/ufjc/
 
 .. |pypi| image:: https://img.shields.io/pypi/v/ufjc?logo=pypi&logoColor=FBE072&label=PyPI&color=4B8BBE
     :target: https://pypi.org/project/ufjc/
```

### Comparing `ufjc-1.3.5/setup.py` & `ufjc-1.3.6/setup.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/core.py` & `ufjc-1.3.6/ufjc/core.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/examples/approaches.py` & `ufjc-1.3.6/ufjc/examples/approaches.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/examples/asymptotics.py` & `ufjc-1.3.6/ufjc/examples/asymptotics.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/examples/error.py` & `ufjc-1.3.6/ufjc/examples/error.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/isometric.py` & `ufjc-1.3.6/ufjc/isometric.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/isotensional.py` & `ufjc-1.3.6/ufjc/isotensional.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/monte_carlo.py` & `ufjc-1.3.6/ufjc/monte_carlo.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/potential.py` & `ufjc-1.3.6/ufjc/potential.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/swfjc.py` & `ufjc-1.3.6/ufjc/swfjc.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/tests/test_examples.py` & `ufjc-1.3.6/ufjc/tests/test_examples.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/tests/test_style.py` & `ufjc-1.3.6/ufjc/tests/test_style.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc/utility.py` & `ufjc-1.3.6/ufjc/utility.py`

 * *Files identical despite different names*

### Comparing `ufjc-1.3.5/ufjc.egg-info/PKG-INFO` & `ufjc-1.3.6/ufjc.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ufjc
-Version: 1.3.5
+Version: 1.3.6
 Summary: The Python package for the uFJC single-chain model.
 Home-page: https://sandialabs.github.io/uFJC
 Author: Michael R. Buche, Scott J. Grutzik
 Author-email: mrbuche@sandia.gov, sjgrutz@sandia.gov
 License: BSD-3-Clause
 Project-URL: Anaconda, https://anaconda.org/mrbuche/ufjc
 Project-URL: Documentation, https://ufjc.readthedocs.io
@@ -27,15 +27,19 @@
 Provides-Extra: all
 License-File: LICENSE
 
 ####
 uFJC
 ####
 
-|build| |docs| |codecov| |coveralls| |pyversions| |pypi| |conda| |docker| |license| |zenodo|
+****************************************************************************************************************
+THIS PACKAGE IS DEPRECATED. PLEASE USE THE `POLYMERS MODELING LIBRARY <https://sandialabs.github.io/Polymers>`_.
+****************************************************************************************************************
+
+|build| |docs| |codecov| |coveralls| |codefactor| |pyversions| |pypi| |conda| |docker| |license| |zenodo|
 
 The Python package for the uFJC single-chain model.
 
 ************
 Installation
 ************
 
@@ -90,25 +94,28 @@
 *********
 
 Copyright 2022 National Technology & Engineering Solutions of Sandia, LLC (NTESS). Under the terms of Contract DE-NA0003525 with NTESS, the U.S. Government retains certain rights in this software.
 
 ..
     Badges ========================================================================
 
+.. |build| image:: https://img.shields.io/github/actions/workflow/status/sandialabs/ufjc/main.yml?branch=main&label=GitHub&logo=github
+    :target: https://github.com/sandialabs/ufjc
+
 .. |docs| image:: https://img.shields.io/readthedocs/ufjc?logo=readthedocs&label=Read%20the%20Docs
     :target: https://ufjc.readthedocs.io/en/latest/
 
-.. |build| image:: https://img.shields.io/github/workflow/status/sandialabs/ufjc/main?label=GitHub&logo=github
-    :target: https://github.com/sandialabs/ufjc
+.. |codecov| image:: https://img.shields.io/codecov/c/github/sandialabs/ufjc?label=Codecov&logo=codecov
+    :target: https://codecov.io/gh/sandialabs/ufjc
 
 .. |coveralls| image:: https://img.shields.io/coveralls/github/sandialabs/ufjc?logo=coveralls&label=Coveralls
     :target: https://coveralls.io/github/sandialabs/ufjc?branch=main
 
-.. |codecov| image:: https://img.shields.io/codecov/c/github/sandialabs/ufjc?label=Codecov&logo=codecov
-    :target: https://codecov.io/gh/sandialabs/ufjc
+.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/sandialabs/ufjc?label=Codefactor&logo=codefactor
+   :target: https://www.codefactor.io/repository/github/sandialabs/ufjc
 
 .. |pyversions| image:: https://img.shields.io/pypi/pyversions/ufjc.svg?logo=python&logoColor=FBE072&color=4B8BBE&label=Python
     :target: https://pypi.org/project/ufjc/
 
 .. |pypi| image:: https://img.shields.io/pypi/v/ufjc?logo=pypi&logoColor=FBE072&label=PyPI&color=4B8BBE
     :target: https://pypi.org/project/ufjc/
```

### Comparing `ufjc-1.3.5/ufjc.egg-info/SOURCES.txt` & `ufjc-1.3.6/ufjc.egg-info/SOURCES.txt`

 * *Files identical despite different names*

