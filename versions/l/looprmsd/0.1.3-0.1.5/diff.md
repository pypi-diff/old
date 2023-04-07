# Comparing `tmp/looprmsd-0.1.3.tar.gz` & `tmp/looprmsd-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "looprmsd-0.1.3.tar", last modified: Fri Apr  7 02:48:36 2023, max compression
+gzip compressed data, was "looprmsd-0.1.5.tar", last modified: Fri Apr  7 05:19:46 2023, max compression
```

## Comparing `looprmsd-0.1.3.tar` & `looprmsd-0.1.5.tar`

### file list

```diff
@@ -1,13 +1,18 @@
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:48:36.710279 looprmsd-0.1.3/
--rw-r--r--   0 jeffrey   (1014) galux      (500)       11 2023-04-05 08:26:23.000000 looprmsd-0.1.3/LICENCE
--rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:48:36.710279 looprmsd-0.1.3/PKG-INFO
--rw-r--r--   0 jeffrey   (1014) galux      (500)     1019 2023-04-07 01:55:16.000000 looprmsd-0.1.3/README.md
--rwxr-xr-x   0 jeffrey   (1014) galux      (500)     5187 2023-04-07 01:48:50.000000 looprmsd-0.1.3/loop_rmsd_antibody.py
-drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 02:48:36.710279 looprmsd-0.1.3/looprmsd.egg-info/
--rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/PKG-INFO
--rw-r--r--   0 jeffrey   (1014) galux      (500)      207 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/SOURCES.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)        1 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/dependency_links.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)       16 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/requires.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)       19 2023-04-07 02:48:36.000000 looprmsd-0.1.3/looprmsd.egg-info/top_level.txt
--rw-r--r--   0 jeffrey   (1014) galux      (500)       38 2023-04-07 02:48:36.710279 looprmsd-0.1.3/setup.cfg
--rw-r--r--   0 jeffrey   (1014) galux      (500)      411 2023-04-07 02:48:20.000000 looprmsd-0.1.3/setup.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:19:46.769284 looprmsd-0.1.5/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       11 2023-04-05 08:26:23.000000 looprmsd-0.1.5/LICENCE
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 05:19:46.769284 looprmsd-0.1.5/PKG-INFO
+-rw-r--r--   0 jeffrey   (1014) galux      (500)     1057 2023-04-07 04:54:48.000000 looprmsd-0.1.5/README.md
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:19:46.677288 looprmsd-0.1.5/looprmsd/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        0 2023-04-07 04:50:27.000000 looprmsd-0.1.5/looprmsd/__init__.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:19:46.729286 looprmsd-0.1.5/looprmsd/dat/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)   704545 2023-04-05 08:43:17.000000 looprmsd-0.1.5/looprmsd/dat/1bj1.pdb
+-rw-r--r--   0 jeffrey   (1014) galux      (500)   283302 2023-04-05 08:42:28.000000 looprmsd-0.1.5/looprmsd/dat/1bj1_HL_H3_pred.pdb
+-rwxr-xr-x   0 jeffrey   (1014) galux      (500)     5189 2023-04-07 04:38:51.000000 looprmsd-0.1.5/looprmsd/loop_rmsd_antibody.py
+drwxr-xr-x   0 jeffrey   (1014) galux      (500)        0 2023-04-07 05:19:46.677288 looprmsd-0.1.5/looprmsd.egg-info/
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      222 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/PKG-INFO
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      292 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/SOURCES.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        1 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/dependency_links.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        6 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/requires.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)        9 2023-04-07 05:19:46.000000 looprmsd-0.1.5/looprmsd.egg-info/top_level.txt
+-rw-r--r--   0 jeffrey   (1014) galux      (500)       38 2023-04-07 05:19:46.769284 looprmsd-0.1.5/setup.cfg
+-rw-r--r--   0 jeffrey   (1014) galux      (500)      429 2023-04-07 05:05:22.000000 looprmsd-0.1.5/setup.py
```

### Comparing `looprmsd-0.1.3/README.md` & `looprmsd-0.1.5/README.md`

 * *Files 12% similar despite different names*

```diff
@@ -18,21 +18,21 @@
 numpy
 ```
 
 ## Example
 
 1. Loop region 지정해주면 RMSD 구해줌.
 ```
-from looprmsd import pdb_rmsd
+from looprmsd.loop_rmsd_antibody import pdb_rmsd
 rmsd = pdb_rmsd(model_pdb, ref_pdb, 'H', 'H', loop_region='H3')  #0.5385195760350145
 ```
 
 2. Seq 주면 RMSD 구해줌.
 ```
-from looprmsd import pdb_rmsd
+from looprmsd.loop_rmsd_antibody import pdb_rmsd
 rmsd = pdb_rmsd(model_pdb, ref_pdb, 'H', 'H', loop_seq='YPHYYGSSHWYFDV')  #0.5385195760350145
 ```
 
 ## Detail
 1. Use Carbon Alpha only in RMSD calculation
 2. Superposition is done by +-2 residue from given loop.
```

### Comparing `looprmsd-0.1.3/loop_rmsd_antibody.py` & `looprmsd-0.1.5/looprmsd/loop_rmsd_antibody.py`

 * *Files 0% similar despite different names*

```diff
@@ -132,10 +132,10 @@
 
     return rmsd
 
 
 if __name__ == "__main__":
     model_pdb = 'dat/1bj1_HL_H3_pred.pdb'
     ref_pdb = 'dat/1bj1.pdb'
-    rmsd = pdb_rmsd(model_pdb, ref_pdb, 'H', 'H', loop_region='H3')  #0.5385195760350145
+    # rmsd = pdb_rmsd(model_pdb, ref_pdb, 'H', 'H', loop_region='H3')  #0.5385195760350145
     rmsd = pdb_rmsd(model_pdb, ref_pdb, 'H', 'H', loop_seq='YPHYYGSSHWYFDV')  #0.5385195760350145
     print(rmsd)
```

