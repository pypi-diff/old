# Comparing `tmp/looprmsd-0.1.5.tar.gz` & `tmp/looprmsd-0.1.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "looprmsd-0.1.5.tar", last modified: Fri Apr  7 05:19:46 2023, max compression
+gzip compressed data, was "looprmsd-0.1.6.tar", last modified: Fri Apr  7 05:45:02 2023, max compression
```

## Comparing `looprmsd-0.1.5.tar` & `looprmsd-0.1.6.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:19:46.769284 looprmsd-0.1.5/
--rw-r--r--   0 jeffrey   (1014) galux      (500)       11 2023-04-05 08:26:23.000000 looprmsd-0.1.5/LICENCE
--rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 05:19:46.769284 looprmsd-0.1.5/PKG-INFO
--rw-r--r--   0 jeffrey   (1014) galux      (500)     1057 2023-04-07 04:54:48.000000 looprmsd-0.1.5/README.md
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:19:46.677288 looprmsd-0.1.5/looprmsd/
--rw-r--r--   0 jeffrey   (1014) galux      (500)        0 2023-04-07 04:50:27.000000 looprmsd-0.1.5/looprmsd/__init__.py
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:19:46.729286 looprmsd-0.1.5/looprmsd/dat/
--rw-r--r--   0 jeffrey   (1014) galux      (500)   704545 2023-04-05 08:43:17.000000 looprmsd-0.1.5/looprmsd/dat/1bj1.pdb
--rw-r--r--   0 jeffrey   (1014) galux      (500)   283302 2023-04-05 08:42:28.000000 looprmsd-0.1.5/looprmsd/dat/1bj1_HL_H3_pred.pdb
--rwxr-xr-x   0 jeffrey   (1014) galux      (500)     5189 2023-04-07 04:38:51.000000 looprmsd-0.1.5/looprmsd/loop_rmsd_antibody.py
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:19:46.677288 looprmsd-0.1.5/looprmsd.egg-info/
--rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/PKG-INFO
--rw-r--r--   0 jeffrey   (1014) galux      (500)      292 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/SOURCES.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)        1 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/dependency_links.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)        6 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/requires.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)        9 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/top_level.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)       38 2023-04-07 05:19:46.769284 looprmsd-0.1.5/setup.cfg
--rw-r--r--   0 jeffrey   (1014) galux      (500)      429 2023-04-07 05:05:22.000000 looprmsd-0.1.5/setup.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:45:02.298862 looprmsd-0.1.6/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       11 2023-04-05 08:26:23.000000 looprmsd-0.1.6/LICENCE
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      271 2023-04-07 05:45:02.298862 looprmsd-0.1.6/PKG-INFO
+-rw-r--r--   0 jeffrey   (1014) galux      (500)     1048 2023-04-07 05:42:44.000000 looprmsd-0.1.6/README.md
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:45:02.298862 looprmsd-0.1.6/looprmsd/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        0 2023-04-07 04:50:27.000000 looprmsd-0.1.6/looprmsd/__init__.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:45:02.298862 looprmsd-0.1.6/looprmsd/dat/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)   704545 2023-04-05 08:43:17.000000 looprmsd-0.1.6/looprmsd/dat/1bj1.pdb
+-rw-r--r--   0 jeffrey   (1014) galux      (500)   283302 2023-04-05 08:42:28.000000 looprmsd-0.1.6/looprmsd/dat/1bj1_HL_H3_pred.pdb
+-rwxr-xr-x   0 jeffrey   (1014) galux      (500)     5189 2023-04-07 05:42:47.000000 looprmsd-0.1.6/looprmsd/loop_rmsd_antibody.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:45:02.298862 looprmsd-0.1.6/looprmsd.egg-info/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      271 2023-04-07 05:45:02.000000 looprmsd-0.1.6/looprmsd.egg-info/PKG-INFO
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      292 2023-04-07 05:45:02.000000 looprmsd-0.1.6/looprmsd.egg-info/SOURCES.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        1 2023-04-07 05:45:02.000000 looprmsd-0.1.6/looprmsd.egg-info/dependency_links.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        6 2023-04-07 05:45:02.000000 looprmsd-0.1.6/looprmsd.egg-info/requires.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        9 2023-04-07 05:45:02.000000 looprmsd-0.1.6/looprmsd.egg-info/top_level.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       38 2023-04-07 05:45:02.298862 looprmsd-0.1.6/setup.cfg
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      477 2023-04-07 05:43:33.000000 looprmsd-0.1.6/setup.py
```

### Comparing `looprmsd-0.1.5/README.md` & `looprmsd-0.1.6/README.md`

 * *Files 16% similar despite different names*

```diff
@@ -1,25 +1,25 @@
 ## Description
 PDB 2개랑 loop_region 지정해주면 RMSD 구해주는 라이브러리
 
 Input PDB 가 chothia numbering 이 아니면 anarci 로 chothia numbering 으로 변환해 RMSD 계산.
 현재는 항체에 대해서만 RMSD 구해줌. (H1-H3, L1-L3)
 
-H1: 26-35
-H2: 50-65
+H1: 26-32
+H2: 52-56
 H3: 95-102
 L1: 24-34
 L2: 50-56
 L3: 89-97
 
-## Requirements
+## Install
+
 ```bash
-anarci  # conda install anarci
-biopython
-numpy
+conda install anarci
+pip install looprmsd
 ```
 
 ## Example
 
 1. Loop region 지정해주면 RMSD 구해줌.
 ```
 from looprmsd.loop_rmsd_antibody import pdb_rmsd
```

### Comparing `looprmsd-0.1.5/looprmsd/dat/1bj1.pdb` & `looprmsd-0.1.6/looprmsd/dat/1bj1.pdb`

 * *Files identical despite different names*

### Comparing `looprmsd-0.1.5/looprmsd/dat/1bj1_HL_H3_pred.pdb` & `looprmsd-0.1.6/looprmsd/dat/1bj1_HL_H3_pred.pdb`

 * *Files identical despite different names*

### Comparing `looprmsd-0.1.5/looprmsd/loop_rmsd_antibody.py` & `looprmsd-0.1.6/looprmsd/loop_rmsd_antibody.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 import os
 import numpy as np
 from Bio.PDB import Superimposer, PDBParser, PDBIO, PPBuilder
 from Bio.Data import SCOPData
 from anarci import run_anarci
 
 REGION_TO_RANGE={
-    'H1': (26,35),
-    'H2': (50,65),
+    'H1': (26,32),
+    'H2': (52,56),
     'H3': (95,102),
     'L1': (24,34),
     'L2': (50,56),
     'L3': (89,97),
 }
 
 def calculate_rotation_matrix(x, y):
```

