# Comparing `tmp/mdocfile-0.0.7.tar.gz` & `tmp/mdocfile-0.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mdocfile-0.0.7.tar", last modified: Sat Dec  3 14:37:40 2022, max compression
+gzip compressed data, was "mdocfile-0.0.8.tar", last modified: Thu Apr  6 11:15:39 2023, max compression
```

## Comparing `mdocfile-0.0.7.tar` & `mdocfile-0.0.8.tar`

### file list

```diff
@@ -1,41 +1,42 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 14:37:40.834853 mdocfile-0.0.7/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 14:37:40.830853 mdocfile-0.0.7/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 14:37:40.834853 mdocfile-0.0.7/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)      856 2022-12-03 14:37:31.000000 mdocfile-0.0.7/.github/workflows/build-and-deploy-docs.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1828 2022-12-03 14:37:31.000000 mdocfile-0.0.7/.github/workflows/test_and_deploy.yml
--rw-r--r--   0 runner    (1001) docker     (123)      173 2022-12-03 14:37:31.000000 mdocfile-0.0.7/.github_changelog_generator
--rw-r--r--   0 runner    (1001) docker     (123)     1197 2022-12-03 14:37:31.000000 mdocfile-0.0.7/.gitignore
--rw-r--r--   0 runner    (1001) docker     (123)     1011 2022-12-03 14:37:31.000000 mdocfile-0.0.7/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1513 2022-12-03 14:37:31.000000 mdocfile-0.0.7/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      195 2022-12-03 14:37:31.000000 mdocfile-0.0.7/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1843 2022-12-03 14:37:40.838853 mdocfile-0.0.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1134 2022-12-03 14:37:31.000000 mdocfile-0.0.7/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 14:37:40.834853 mdocfile-0.0.7/docs/
--rw-r--r--   0 runner    (1001) docker     (123)     1133 2022-12-03 14:37:31.000000 mdocfile-0.0.7/docs/index.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 14:37:40.834853 mdocfile-0.0.7/mdocfile/
--rw-r--r--   0 runner    (1001) docker     (123)       28 2022-12-03 14:37:31.000000 mdocfile-0.0.7/mdocfile/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      176 2022-12-03 14:37:40.000000 mdocfile-0.0.7/mdocfile/_version.py
--rw-r--r--   0 runner    (1001) docker     (123)      931 2022-12-03 14:37:31.000000 mdocfile-0.0.7/mdocfile/functions.py
--rw-r--r--   0 runner    (1001) docker     (123)     1436 2022-12-03 14:37:31.000000 mdocfile-0.0.7/mdocfile/global_data.py
--rw-r--r--   0 runner    (1001) docker     (123)     1366 2022-12-03 14:37:31.000000 mdocfile-0.0.7/mdocfile/mdoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     3369 2022-12-03 14:37:31.000000 mdocfile-0.0.7/mdocfile/section_data.py
--rw-r--r--   0 runner    (1001) docker     (123)      740 2022-12-03 14:37:31.000000 mdocfile-0.0.7/mdocfile/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 14:37:40.834853 mdocfile-0.0.7/mdocfile.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1843 2022-12-03 14:37:40.000000 mdocfile-0.0.7/mdocfile.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      709 2022-12-03 14:37:40.000000 mdocfile-0.0.7/mdocfile.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-03 14:37:40.000000 mdocfile-0.0.7/mdocfile.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2022-12-03 14:37:40.000000 mdocfile-0.0.7/mdocfile.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)      148 2022-12-03 14:37:40.000000 mdocfile-0.0.7/mdocfile.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2022-12-03 14:37:40.000000 mdocfile-0.0.7/mdocfile.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)     1048 2022-12-03 14:37:31.000000 mdocfile-0.0.7/mkdocs.yml
--rw-r--r--   0 runner    (1001) docker     (123)     1528 2022-12-03 14:37:40.838853 mdocfile-0.0.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)       90 2022-12-03 14:37:31.000000 mdocfile-0.0.7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 14:37:40.834853 mdocfile-0.0.7/tests/
--rw-r--r--   0 runner    (1001) docker     (123)      150 2022-12-03 14:37:31.000000 mdocfile-0.0.7/tests/conftest.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2022-12-03 14:37:40.834853 mdocfile-0.0.7/tests/test_data/
--rw-r--r--   0 runner    (1001) docker     (123)    20443 2022-12-03 14:37:31.000000 mdocfile-0.0.7/tests/test_data/TS_01.mrc.mdoc
--rw-r--r--   0 runner    (1001) docker     (123)      243 2022-12-03 14:37:31.000000 mdocfile-0.0.7/tests/test_functions.py
--rw-r--r--   0 runner    (1001) docker     (123)      460 2022-12-03 14:37:31.000000 mdocfile-0.0.7/tests/test_global_data.py
--rw-r--r--   0 runner    (1001) docker     (123)      713 2022-12-03 14:37:31.000000 mdocfile-0.0.7/tests/test_mdoc.py
--rw-r--r--   0 runner    (1001) docker     (123)     1642 2022-12-03 14:37:31.000000 mdocfile-0.0.7/tests/test_section_data.py
--rw-r--r--   0 runner    (1001) docker     (123)      495 2022-12-03 14:37:31.000000 mdocfile-0.0.7/tox.ini
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:15:39.603387 mdocfile-0.0.8/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:15:39.599387 mdocfile-0.0.8/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:15:39.599387 mdocfile-0.0.8/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)      856 2023-04-06 11:15:25.000000 mdocfile-0.0.8/.github/workflows/build-and-deploy-docs.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1828 2023-04-06 11:15:25.000000 mdocfile-0.0.8/.github/workflows/test_and_deploy.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      173 2023-04-06 11:15:25.000000 mdocfile-0.0.8/.github_changelog_generator
+-rw-r--r--   0 runner    (1001) docker     (123)     1197 2023-04-06 11:15:25.000000 mdocfile-0.0.8/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)     1011 2023-04-06 11:15:25.000000 mdocfile-0.0.8/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1513 2023-04-06 11:15:25.000000 mdocfile-0.0.8/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      195 2023-04-06 11:15:25.000000 mdocfile-0.0.8/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1841 2023-04-06 11:15:39.603387 mdocfile-0.0.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1132 2023-04-06 11:15:25.000000 mdocfile-0.0.8/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:15:39.599387 mdocfile-0.0.8/docs/
+-rw-r--r--   0 runner    (1001) docker     (123)     1133 2023-04-06 11:15:25.000000 mdocfile-0.0.8/docs/index.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:15:39.603387 mdocfile-0.0.8/mdocfile/
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-06 11:15:25.000000 mdocfile-0.0.8/mdocfile/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      160 2023-04-06 11:15:39.000000 mdocfile-0.0.8/mdocfile/_version.py
+-rw-r--r--   0 runner    (1001) docker     (123)      931 2023-04-06 11:15:25.000000 mdocfile-0.0.8/mdocfile/functions.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1436 2023-04-06 11:15:25.000000 mdocfile-0.0.8/mdocfile/global_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1362 2023-04-06 11:15:25.000000 mdocfile-0.0.8/mdocfile/mdoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3505 2023-04-06 11:15:25.000000 mdocfile-0.0.8/mdocfile/section_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      938 2023-04-06 11:15:25.000000 mdocfile-0.0.8/mdocfile/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:15:39.603387 mdocfile-0.0.8/mdocfile.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1841 2023-04-06 11:15:39.000000 mdocfile-0.0.8/mdocfile.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      748 2023-04-06 11:15:39.000000 mdocfile-0.0.8/mdocfile.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:15:39.000000 mdocfile-0.0.8/mdocfile.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:15:39.000000 mdocfile-0.0.8/mdocfile.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)      148 2023-04-06 11:15:39.000000 mdocfile-0.0.8/mdocfile.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 11:15:39.000000 mdocfile-0.0.8/mdocfile.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)     1048 2023-04-06 11:15:25.000000 mdocfile-0.0.8/mkdocs.yml
+-rw-r--r--   0 runner    (1001) docker     (123)     1528 2023-04-06 11:15:39.603387 mdocfile-0.0.8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)       90 2023-04-06 11:15:25.000000 mdocfile-0.0.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:15:39.603387 mdocfile-0.0.8/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)      277 2023-04-06 11:15:25.000000 mdocfile-0.0.8/tests/conftest.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:15:39.603387 mdocfile-0.0.8/tests/test_data/
+-rw-r--r--   0 runner    (1001) docker     (123)    43777 2023-04-06 11:15:25.000000 mdocfile-0.0.8/tests/test_data/montage_section.mdoc
+-rw-r--r--   0 runner    (1001) docker     (123)    20443 2023-04-06 11:15:25.000000 mdocfile-0.0.8/tests/test_data/tilt_series.mdoc
+-rw-r--r--   0 runner    (1001) docker     (123)      428 2023-04-06 11:15:25.000000 mdocfile-0.0.8/tests/test_functions.py
+-rw-r--r--   0 runner    (1001) docker     (123)      460 2023-04-06 11:15:25.000000 mdocfile-0.0.8/tests/test_global_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      713 2023-04-06 11:15:25.000000 mdocfile-0.0.8/tests/test_mdoc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1642 2023-04-06 11:15:25.000000 mdocfile-0.0.8/tests/test_section_data.py
+-rw-r--r--   0 runner    (1001) docker     (123)      495 2023-04-06 11:15:25.000000 mdocfile-0.0.8/tox.ini
```

### Comparing `mdocfile-0.0.7/.github/workflows/build-and-deploy-docs.yml` & `mdocfile-0.0.8/.github/workflows/build-and-deploy-docs.yml`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/.github/workflows/test_and_deploy.yml` & `mdocfile-0.0.8/.github/workflows/test_and_deploy.yml`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/.gitignore` & `mdocfile-0.0.8/.gitignore`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/.pre-commit-config.yaml` & `mdocfile-0.0.8/.pre-commit-config.yaml`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/LICENSE` & `mdocfile-0.0.8/LICENSE`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/PKG-INFO` & `mdocfile-0.0.8/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mdocfile
-Version: 0.0.7
+Version: 0.0.8
 Summary: parse serialEM mdoc files in Python
 Home-page: https://github.com/alisterburt/mdocfile
 Author: Alister Burt
 Author-email: alisterburt@gmail.com
 License: BSD license
 Project-URL: Source Code, https://github.com/alisterburt/mdocfile
 Classifier: Development Status :: 2 - Pre-Alpha
@@ -24,20 +24,18 @@
 [![License](https://img.shields.io/pypi/l/mdocfile.svg?color=green)](https://github.com/alisterburt/mdocfile/raw/main/LICENSE)
 [![PyPI](https://img.shields.io/pypi/v/mdocfile.svg?color=green)](https://pypi.org/project/mdocfile)
 [![Python Version](https://img.shields.io/pypi/pyversions/mdocfile.svg?color=green)](https://python.org)
 [![CI](https://github.com/alisterburt/mdocfile/actions/workflows/ci.yml/badge.svg)](https://github.com/alisterburt/mdocfile/actions/workflows/ci.yml)
 [![codecov](https://codecov.io/gh/alisterburt/mdocfile/branch/main/graph/badge.svg)](https://codecov.io/gh/alisterburt/mdocfile)
 
 <p align="center" width="100%">
-    <img width="70%" src="https://user-images.githubusercontent.
-com/7307488/205445941-8db4ad0e-648a-446e-812d-bd1b81ec19b8.png"> 
+    <img width="70%" src="https://user-images.githubusercontent.com/7307488/205445941-8db4ad0e-648a-446e-812d-bd1b81ec19b8.png"> 
 </p>
 
-*mdocfile* is Python package for working with [SerialEM](https://bio3d.colorado.
-edu/SerialEM/) mdoc files.
+*mdocfile* is Python package for working with [SerialEM](https://bio3d.colorado.edu/SerialEM/) mdoc files.
 
 ---
 
 # Quickstart
 
 `mdocfile.read()` will return the contents of an mdoc file as a pandas 
 dataframe.
```

### Comparing `mdocfile-0.0.7/README.md` & `mdocfile-0.0.8/docs/index.md`

 * *Files 1% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-# mdocfile
+# Overview
 
 [![License](https://img.shields.io/pypi/l/mdocfile.svg?color=green)](https://github.com/alisterburt/mdocfile/raw/main/LICENSE)
 [![PyPI](https://img.shields.io/pypi/v/mdocfile.svg?color=green)](https://pypi.org/project/mdocfile)
 [![Python Version](https://img.shields.io/pypi/pyversions/mdocfile.svg?color=green)](https://python.org)
 [![CI](https://github.com/alisterburt/mdocfile/actions/workflows/ci.yml/badge.svg)](https://github.com/alisterburt/mdocfile/actions/workflows/ci.yml)
 [![codecov](https://codecov.io/gh/alisterburt/mdocfile/branch/main/graph/badge.svg)](https://codecov.io/gh/alisterburt/mdocfile)
 
@@ -29,8 +29,8 @@
 
 # Installation
 
 pip:
 
 ```shell
 pip install mdocfile
-```
+```
```

### Comparing `mdocfile-0.0.7/docs/index.md` & `mdocfile-0.0.8/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -1,22 +1,20 @@
-# Overview
+# mdocfile
 
 [![License](https://img.shields.io/pypi/l/mdocfile.svg?color=green)](https://github.com/alisterburt/mdocfile/raw/main/LICENSE)
 [![PyPI](https://img.shields.io/pypi/v/mdocfile.svg?color=green)](https://pypi.org/project/mdocfile)
 [![Python Version](https://img.shields.io/pypi/pyversions/mdocfile.svg?color=green)](https://python.org)
 [![CI](https://github.com/alisterburt/mdocfile/actions/workflows/ci.yml/badge.svg)](https://github.com/alisterburt/mdocfile/actions/workflows/ci.yml)
 [![codecov](https://codecov.io/gh/alisterburt/mdocfile/branch/main/graph/badge.svg)](https://codecov.io/gh/alisterburt/mdocfile)
 
 <p align="center" width="100%">
-    <img width="70%" src="https://user-images.githubusercontent.
-com/7307488/205445941-8db4ad0e-648a-446e-812d-bd1b81ec19b8.png"> 
+    <img width="70%" src="https://user-images.githubusercontent.com/7307488/205445941-8db4ad0e-648a-446e-812d-bd1b81ec19b8.png"> 
 </p>
 
-*mdocfile* is Python package for working with [SerialEM](https://bio3d.colorado.
-edu/SerialEM/) mdoc files.
+*mdocfile* is Python package for working with [SerialEM](https://bio3d.colorado.edu/SerialEM/) mdoc files.
 
 ---
 
 # Quickstart
 
 `mdocfile.read()` will return the contents of an mdoc file as a pandas 
 dataframe.
@@ -29,8 +27,8 @@
 
 # Installation
 
 pip:
 
 ```shell
 pip install mdocfile
-```
+```
```

### Comparing `mdocfile-0.0.7/mdocfile/functions.py` & `mdocfile-0.0.8/mdocfile/functions.py`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/mdocfile/global_data.py` & `mdocfile-0.0.8/mdocfile/global_data.py`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/mdocfile/mdoc.py` & `mdocfile-0.0.8/mdocfile/mdoc.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,37 +1,37 @@
 from typing import List
 
 from pydantic import BaseModel
 from .global_data import MdocGlobalData
 from .section_data import MdocSectionData
-from .utils import find_z_value_entries, find_title_entries
+from .utils import find_section_entries, find_title_entries
 
 
 class Mdoc(BaseModel):
     titles: List[str]
     global_data: MdocGlobalData
     section_data: List[MdocSectionData]
 
     @classmethod
     def from_file(cls, filename: str):
         with open(filename) as file:
             lines = [line.strip() for line in file.readlines()]
-        split_idxs = find_z_value_entries(lines)
+        split_idxs = find_section_entries(lines)
         split_idxs.append(len(lines))
 
         header_lines = lines[0:split_idxs[0]]
         title_idxs = find_title_entries(header_lines)
 
         titles = [header_lines[idx] for idx in title_idxs]
         global_data = MdocGlobalData.from_lines(header_lines)
         section_data = [
             MdocSectionData.from_lines(lines[start_idx:end_idx])
             for start_idx, end_idx
             in zip(split_idxs, split_idxs[1:])
-            ]
+        ]
         return cls(titles=titles, global_data=global_data, section_data=section_data)
 
     def to_string(self):
         """
         Generate the string representation of the Mdoc data
         """
         return '\n\n'.join([
```

### Comparing `mdocfile-0.0.7/mdocfile/section_data.py` & `mdocfile-0.0.8/mdocfile/section_data.py`

 * *Files 18% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 
 class MdocSectionData(BaseModel):
     """Data model for section data in a SerialEM mdoc file.
 
     https://bio3d.colorado.edu/SerialEM/hlp/html/about_formats.htm
     """
     ZValue: Optional[int]
+    MontSection: Optional[int]
     TiltAngle: Optional[float]
     PieceCoordinates: Optional[Tuple[float, float, int]]
     StagePosition: Tuple[float, float]
     StageZ: Optional[float]
     Magnification: Optional[float]
     CameraLength: Optional[float]
     MagIndex: Optional[int]
@@ -33,19 +34,19 @@
     CameraIndex: Optional[int]
     DividedBy2: Optional[bool]
     LowDoseConSet: Optional[int]
     MinMaxMean: Optional[Tuple[float, float, float]]
     PriorRecordDose: Optional[float]
     XedgeDxy: Optional[Tuple[float, float]]
     YedgeDxy: Optional[Tuple[float, float]]
-    XedgeDxyVS: Optional[Tuple[float, float]]
-    YedgeDxyVS: Optional[Tuple[float, float]]
+    XedgeDxyVS: Optional[Union[Tuple[float, float], Tuple[float, float, float]]]
+    YedgeDxyVS: Optional[Union[Tuple[float, float], Tuple[float, float, float]]]
     StageOffsets: Optional[Tuple[float, float]]
     AlignedPieceCoords: Optional[Tuple[float, float]]
-    AlignedPieceCoordsVS: Optional[Tuple[float, float]]
+    AlignedPieceCoordsVS: Optional[Union[Tuple[float, float], Tuple[float, float, float]]]
     SubFramePath: Optional[Path]
     NumSubFrames: Optional[int]
     FrameDosesAndNumbers: Optional[Sequence[Tuple[float, int]]]
     DateTime: Optional[str]
     NavigatorLabel: Optional[str]
     FilterSlitAndLoss: Optional[Tuple[float, float]]
     ChannelName: Optional[str]
@@ -58,15 +59,15 @@
         'SuperMontCoords',
         'ImageShift',
         'MinMaxMean',
         'StagePosition',
         'XedgeDxy',
         'YedgeDxy',
         'XedgeDxyVS',
-        'XedgeDxyVS',
+        'YedgeDxyVS',
         'StageOffsets',
         'AlignedPieceCoords',
         'AlignedPieceCoordsVS',
         'FrameDosesAndNumbers',
         'FilterSlitAndLoss',
         'MultiShotHoleAndPosition',
         pre=True)
```

### Comparing `mdocfile-0.0.7/mdocfile/utils.py` & `mdocfile-0.0.8/mdocfile/utils.py`

 * *Files 26% similar despite different names*

```diff
@@ -4,22 +4,26 @@
 camel_to_snake_regex = re.compile(r'(?<!^)(?=[A-Z])')
 
 
 def camel_to_snake(word: str) -> str:
     return camel_to_snake_regex.sub('_', word).lower()
 
 
-def find_z_value_entries(lines: List[str]) -> List[int]:
-    """Find the strings which contains a z-value entry.
-    """
-    z_value_idxs = []
-    for idx, line in enumerate(lines):
-        if line.startswith('[ZValue ='):
-            z_value_idxs.append(idx)
-    return z_value_idxs
+def find_section_entries(lines: List[str]) -> List[int]:
+    """Find the strings which contains a z-value or montage section entry."""
+    section_idx = [
+        idx
+        for idx, line
+        in enumerate(lines)
+        if line.startswith('[ZValue =') or line.startswith('[MontSection =')
+    ]
+    # for idx, line in enumerate(lines):
+    #     if line.startswith('[ZValue =') or line.startswith('[MontSection ='):
+    #         section_idx.append(idx)
+    return section_idx
 
 
 def find_title_entries(lines: List[str]) -> List[int]:
     """Find mdoc title entries in a list of strings"""
     title_idxs = []
     for idx, line in enumerate(lines):
         if line.startswith('[T ='):
```

### Comparing `mdocfile-0.0.7/mdocfile.egg-info/PKG-INFO` & `mdocfile-0.0.8/mdocfile.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mdocfile
-Version: 0.0.7
+Version: 0.0.8
 Summary: parse serialEM mdoc files in Python
 Home-page: https://github.com/alisterburt/mdocfile
 Author: Alister Burt
 Author-email: alisterburt@gmail.com
 License: BSD license
 Project-URL: Source Code, https://github.com/alisterburt/mdocfile
 Classifier: Development Status :: 2 - Pre-Alpha
@@ -24,20 +24,18 @@
 [![License](https://img.shields.io/pypi/l/mdocfile.svg?color=green)](https://github.com/alisterburt/mdocfile/raw/main/LICENSE)
 [![PyPI](https://img.shields.io/pypi/v/mdocfile.svg?color=green)](https://pypi.org/project/mdocfile)
 [![Python Version](https://img.shields.io/pypi/pyversions/mdocfile.svg?color=green)](https://python.org)
 [![CI](https://github.com/alisterburt/mdocfile/actions/workflows/ci.yml/badge.svg)](https://github.com/alisterburt/mdocfile/actions/workflows/ci.yml)
 [![codecov](https://codecov.io/gh/alisterburt/mdocfile/branch/main/graph/badge.svg)](https://codecov.io/gh/alisterburt/mdocfile)
 
 <p align="center" width="100%">
-    <img width="70%" src="https://user-images.githubusercontent.
-com/7307488/205445941-8db4ad0e-648a-446e-812d-bd1b81ec19b8.png"> 
+    <img width="70%" src="https://user-images.githubusercontent.com/7307488/205445941-8db4ad0e-648a-446e-812d-bd1b81ec19b8.png"> 
 </p>
 
-*mdocfile* is Python package for working with [SerialEM](https://bio3d.colorado.
-edu/SerialEM/) mdoc files.
+*mdocfile* is Python package for working with [SerialEM](https://bio3d.colorado.edu/SerialEM/) mdoc files.
 
 ---
 
 # Quickstart
 
 `mdocfile.read()` will return the contents of an mdoc file as a pandas 
 dataframe.
```

### Comparing `mdocfile-0.0.7/mdocfile.egg-info/SOURCES.txt` & `mdocfile-0.0.8/mdocfile.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -25,8 +25,9 @@
 mdocfile.egg-info/requires.txt
 mdocfile.egg-info/top_level.txt
 tests/conftest.py
 tests/test_functions.py
 tests/test_global_data.py
 tests/test_mdoc.py
 tests/test_section_data.py
-tests/test_data/TS_01.mrc.mdoc
+tests/test_data/montage_section.mdoc
+tests/test_data/tilt_series.mdoc
```

### Comparing `mdocfile-0.0.7/mkdocs.yml` & `mdocfile-0.0.8/mkdocs.yml`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/setup.cfg` & `mdocfile-0.0.8/setup.cfg`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/tests/test_data/TS_01.mrc.mdoc` & `mdocfile-0.0.8/tests/test_data/tilt_series.mdoc`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/tests/test_mdoc.py` & `mdocfile-0.0.8/tests/test_mdoc.py`

 * *Files identical despite different names*

### Comparing `mdocfile-0.0.7/tests/test_section_data.py` & `mdocfile-0.0.8/tests/test_section_data.py`

 * *Files identical despite different names*

