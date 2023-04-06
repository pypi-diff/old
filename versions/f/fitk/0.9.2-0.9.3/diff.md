# Comparing `tmp/fitk-0.9.2.tar.gz` & `tmp/fitk-0.9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fitk-0.9.2.tar", max compression
+gzip compressed data, was "fitk-0.9.3.tar", max compression
```

## Comparing `fitk-0.9.2.tar` & `fitk-0.9.3.tar`

### file list

```diff
@@ -1,21 +1,16 @@
--rw-r--r--   0        0        0     1066 2023-03-10 08:59:21.296744 fitk-0.9.2/LICENSE
--rw-r--r--   0        0        0     1694 2023-03-24 14:09:28.855309 fitk-0.9.2/README.md
--rw-r--r--   0        0        0        6 2023-04-06 08:58:30.286223 fitk-0.9.2/fitk/VERSION.txt
--rw-r--r--   0        0        0    15324 2023-04-06 08:52:04.275308 fitk-0.9.2/fitk/__init__.py
--rw-r--r--   0        0        0    22326 2023-04-06 08:52:04.275308 fitk-0.9.2/fitk/derivatives.py
--rw-r--r--   0        0        0   173975 2022-04-02 10:14:59.572788 fitk-0.9.2/fitk/fitk/fisher_matrix.html
--rw-r--r--   0        0        0    54615 2022-04-02 10:14:59.600788 fitk-0.9.2/fitk/fitk/fisher_plotter.html
--rw-r--r--   0        0        0    27182 2022-04-02 10:14:59.612788 fitk-0.9.2/fitk/fitk/fisher_utils.html
--rw-r--r--   0        0        0     8650 2022-04-02 10:14:59.520788 fitk-0.9.2/fitk/fitk/index.html
--rw-r--r--   0        0        0    82161 2023-04-06 08:52:04.275308 fitk-0.9.2/fitk/graphics.py
--rw-r--r--   0        0        0     3511 2023-04-06 08:58:01.942301 fitk-0.9.2/fitk/interfaces/__init__.py
--rw-r--r--   0        0        0     8587 2023-04-06 08:58:01.942301 fitk-0.9.2/fitk/interfaces/classy_interfaces.py
--rw-r--r--   0        0        0     8646 2023-03-25 13:01:58.103976 fitk-0.9.2/fitk/interfaces/classy_interfaces.py.orig
--rw-r--r--   0        0        0    20069 2023-04-06 08:52:04.279308 fitk-0.9.2/fitk/interfaces/coffe_interfaces.py
--rw-r--r--   0        0        0     5159 2023-04-06 08:52:04.279308 fitk-0.9.2/fitk/interfaces/misc_interfaces.py
--rw-r--r--   0        0        0     9254 2023-04-06 08:52:04.279308 fitk-0.9.2/fitk/operations.py
--rw-r--r--   0        0        0    73698 2023-04-06 08:52:04.279308 fitk-0.9.2/fitk/tensors.py
--rw-r--r--   0        0        0     9912 2023-04-06 08:52:04.279308 fitk-0.9.2/fitk/utilities.py
--rw-r--r--   0        0        0     1166 2023-04-06 08:58:30.654222 fitk-0.9.2/pyproject.toml
--rw-r--r--   0        0        0     2743 1970-01-01 00:00:00.000000 fitk-0.9.2/setup.py
--rw-r--r--   0        0        0     2795 1970-01-01 00:00:00.000000 fitk-0.9.2/PKG-INFO
+-rw-r--r--   0        0        0     1066 2023-03-10 08:59:21.296744 fitk-0.9.3/LICENSE
+-rw-r--r--   0        0        0     1694 2023-03-24 14:09:28.855309 fitk-0.9.3/README.md
+-rw-r--r--   0        0        0        6 2023-04-06 09:02:27.185568 fitk-0.9.3/fitk/VERSION.txt
+-rw-r--r--   0        0        0    15324 2023-04-06 08:52:04.275308 fitk-0.9.3/fitk/__init__.py
+-rw-r--r--   0        0        0    22326 2023-04-06 08:52:04.275308 fitk-0.9.3/fitk/derivatives.py
+-rw-r--r--   0        0        0    82161 2023-04-06 08:52:04.275308 fitk-0.9.3/fitk/graphics.py
+-rw-r--r--   0        0        0     3511 2023-04-06 08:58:01.942301 fitk-0.9.3/fitk/interfaces/__init__.py
+-rw-r--r--   0        0        0     8587 2023-04-06 08:58:01.942301 fitk-0.9.3/fitk/interfaces/classy_interfaces.py
+-rw-r--r--   0        0        0    20069 2023-04-06 08:52:04.279308 fitk-0.9.3/fitk/interfaces/coffe_interfaces.py
+-rw-r--r--   0        0        0     5159 2023-04-06 08:52:04.279308 fitk-0.9.3/fitk/interfaces/misc_interfaces.py
+-rw-r--r--   0        0        0     9254 2023-04-06 08:52:04.279308 fitk-0.9.3/fitk/operations.py
+-rw-r--r--   0        0        0    73698 2023-04-06 08:52:04.279308 fitk-0.9.3/fitk/tensors.py
+-rw-r--r--   0        0        0     9912 2023-04-06 08:52:04.279308 fitk-0.9.3/fitk/utilities.py
+-rw-r--r--   0        0        0     1166 2023-04-06 09:02:27.505567 fitk-0.9.3/pyproject.toml
+-rw-r--r--   0        0        0     2723 1970-01-01 00:00:00.000000 fitk-0.9.3/setup.py
+-rw-r--r--   0        0        0     2795 1970-01-01 00:00:00.000000 fitk-0.9.3/PKG-INFO
```

### Comparing `fitk-0.9.2/LICENSE` & `fitk-0.9.3/LICENSE`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/README.md` & `fitk-0.9.3/README.md`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/__init__.py` & `fitk-0.9.3/fitk/__init__.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/derivatives.py` & `fitk-0.9.3/fitk/derivatives.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/graphics.py` & `fitk-0.9.3/fitk/graphics.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/interfaces/__init__.py` & `fitk-0.9.3/fitk/interfaces/__init__.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/interfaces/classy_interfaces.py` & `fitk-0.9.3/fitk/interfaces/classy_interfaces.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/interfaces/coffe_interfaces.py` & `fitk-0.9.3/fitk/interfaces/coffe_interfaces.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/interfaces/misc_interfaces.py` & `fitk-0.9.3/fitk/interfaces/misc_interfaces.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/operations.py` & `fitk-0.9.3/fitk/operations.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/tensors.py` & `fitk-0.9.3/fitk/tensors.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/fitk/utilities.py` & `fitk-0.9.3/fitk/utilities.py`

 * *Files identical despite different names*

### Comparing `fitk-0.9.2/pyproject.toml` & `fitk-0.9.3/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "fitk"
-version = "0.9.2"
+version = "0.9.3"
 description = "The Fisher Information ToolKit"
 authors = ["JCGoran <goran.jelic-cizmek@unige.ch>"]
 license = "MIT"
 readme = "README.md"
 
 [tool.poetry.dependencies]
 python = ">=3.7,<4"
```

### Comparing `fitk-0.9.2/setup.py` & `fitk-0.9.3/setup.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # -*- coding: utf-8 -*-
 from setuptools import setup
 
 packages = \
 ['fitk', 'fitk.interfaces']
 
 package_data = \
-{'': ['*'], 'fitk': ['fitk/*']}
+{'': ['*']}
 
 install_requires = \
 ['sympy']
 
 extras_require = \
 {':python_version < "3.11"': ['matplotlib>=3.5,<4.0'],
  ':python_version == "3.7"': ['numpy==1.21.6', 'scipy==1.7.3'],
@@ -17,15 +17,15 @@
  ':python_version >= "3.8"': ['numpy>1.22', 'scipy>1.7.3'],
  'classy': ['classy'],
  'coffe': ['coffe'],
  'interfaces': ['coffe', 'classy']}
 
 setup_kwargs = {
     'name': 'fitk',
-    'version': '0.9.2',
+    'version': '0.9.3',
     'description': 'The Fisher Information ToolKit',
     'long_description': "## FITK - the Fisher Information ToolKit\n[![codecov](https://codecov.io/gh/JCGoran/fitk/branch/master/graph/badge.svg?token=NX9WRX89SI)](https://codecov.io/gh/JCGoran/fitk)\n[![CircleCI](https://dl.circleci.com/status-badge/img/gh/JCGoran/fitk/tree/master.svg?style=shield&circle-token=5cc8653735b0092318b9790720101eaa4c568c10)](https://dl.circleci.com/status-badge/redirect/gh/JCGoran/fitk/tree/master)\n[![python - versions](https://img.shields.io/pypi/pyversions/fitk)](https://pypi.org/project/fitk/)\n[![CodeFactor](https://www.codefactor.io/repository/github/jcgoran/fitk/badge)](https://www.codefactor.io/repository/github/jcgoran/fitk)\n\nFitk is a Python package for computing, manipulating, and plotting of Fisher information matrices.\n\n### Installation\n\nThe best way to install the stable version is via `pip`:\n\n```plaintext\npip install fitk\n```\n\nNote that on some systems you may have to replace `pip` by `python3 -m pip` or similar for the installation.\nFurthermore, if you only wish to install the package for the current user (or don't have root privileges), you should supply the `--user` flag to the above command.\n\nAlternatively, if you want to install the latest development version:\n\n```plaintext\npip install git+https://github.com/JCGoran/fitk\n```\n\n### Usage\n\nFor various examples on how to use FITK, as well as the latest API, please refer to [the main docs](https://jcgoran.github.io/fitk/).\n\n### Issues\n\nIf you encounter any bugs running the code, or have a suggestion for new functionality, please open up a new issue [on GitHub](https://github.com/JCGoran/fitk/issues/).\n\n### Contributing\n\nSee [CONTRIBUTING.md](CONTRIBUTING.md).\n\n### License\n\nSee [LICENSE](LICENSE) file.\n",
     'author': 'JCGoran',
     'author_email': 'goran.jelic-cizmek@unige.ch',
     'maintainer': 'None',
     'maintainer_email': 'None',
     'url': 'None',
```

### Comparing `fitk-0.9.2/PKG-INFO` & `fitk-0.9.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: fitk
-Version: 0.9.2
+Version: 0.9.3
 Summary: The Fisher Information ToolKit
 License: MIT
 Author: JCGoran
 Author-email: goran.jelic-cizmek@unige.ch
 Requires-Python: >=3.7,<4
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

