# Comparing `tmp/vaspvis-1.2.6.tar.gz` & `tmp/vaspvis-1.2.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "vaspvis-1.2.6.tar", last modified: Wed Apr  5 15:25:47 2023, max compression
+gzip compressed data, was "vaspvis-1.2.7.tar", last modified: Thu Apr  6 19:50:13 2023, max compression
```

## Comparing `vaspvis-1.2.6.tar` & `vaspvis-1.2.7.tar`

### file list

```diff
@@ -1,58 +1,58 @@
-drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-05 15:25:47.044004 vaspvis-1.2.6/
--rw-rw-r--   0 dd        (1000) dd        (1000)     1056 2023-01-26 14:32:30.000000 vaspvis-1.2.6/LICENSE.txt
--rw-rw-r--   0 dd        (1000) dd        (1000)       72 2023-01-26 14:32:30.000000 vaspvis-1.2.6/MANIFEST.in
--rw-rw-r--   0 dd        (1000) dd        (1000)    11478 2023-04-05 15:25:47.044004 vaspvis-1.2.6/PKG-INFO
--rw-rw-r--   0 dd        (1000) dd        (1000)    11176 2023-01-26 14:32:30.000000 vaspvis-1.2.6/README.md
--rw-rw-r--   0 dd        (1000) dd        (1000)     6277 2023-01-26 14:32:30.000000 vaspvis-1.2.6/example.py
-drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-05 15:25:47.036004 vaspvis-1.2.6/img/
--rw-rw-r--   0 dd        (1000) dd        (1000)   342587 2023-01-26 14:32:30.000000 vaspvis-1.2.6/img/band_atom_orbitals.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   348428 2023-01-26 14:32:30.000000 vaspvis-1.2.6/img/band_atom_spd.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   308011 2023-01-26 14:32:30.000000 vaspvis-1.2.6/img/band_atoms.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   462542 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_dos_atom_orbitals.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   454083 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_dos_atoms.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   394736 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_dos_element_orbitals.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   439321 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_dos_element_spd.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   450754 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_dos_elements.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   590551 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_dos_orbitals.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   243066 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_dos_plain.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   516200 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_dos_spd.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   278341 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_element_orbital.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   310041 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_element_spd.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   306319 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_elements.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   426076 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_orbital.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   174622 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_plain.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   359336 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/band_spd.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   137295 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/dos_atom_orbitals.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   157059 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/dos_atom_spd.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   163001 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/dos_atoms.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   124882 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/dos_element_orbitals.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   141064 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/dos_element_spd.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   161570 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/dos_elements.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   179699 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/dos_orbitals.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   101917 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/dos_plain.png
--rw-rw-r--   0 dd        (1000) dd        (1000)   170210 2023-01-26 14:32:31.000000 vaspvis-1.2.6/img/dos_spd.png
--rw-rw-r--   0 dd        (1000) dd        (1000)       38 2023-04-05 15:25:47.044004 vaspvis-1.2.6/setup.cfg
--rw-rw-r--   0 dd        (1000) dd        (1000)      788 2023-04-05 15:25:42.000000 vaspvis-1.2.6/setup.py
-drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-05 15:25:47.040004 vaspvis-1.2.6/vaspvis/
--rw-rw-r--   0 dd        (1000) dd        (1000)      175 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/__init__.py
--rw-rw-r--   0 dd        (1000) dd        (1000)   107676 2023-02-28 20:42:29.000000 vaspvis-1.2.6/vaspvis/band.py
--rw-rw-r--   0 dd        (1000) dd        (1000)     6233 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/charge.py
--rw-rw-r--   0 dd        (1000) dd        (1000)    80193 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/dos.py
-drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-05 15:25:47.044004 vaspvis-1.2.6/vaspvis/passivator_utils/
--rw-rw-r--   0 dd        (1000) dd        (1000)      136 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/passivator_utils/__init__.py
--rw-rw-r--   0 dd        (1000) dd        (1000)    11117 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/passivator_utils/passivator_utils.py
--rw-rw-r--   0 dd        (1000) dd        (1000)   347297 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/standard.py
--rw-rw-r--   0 dd        (1000) dd        (1000)    18075 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/stm.py
-drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-05 15:25:47.044004 vaspvis-1.2.6/vaspvis/unfold/
--rw-rw-r--   0 dd        (1000) dd        (1000)       22 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/unfold/__init__.py
--rw-rw-r--   0 dd        (1000) dd        (1000)     6062 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/unfold/convert.py
--rw-rw-r--   0 dd        (1000) dd        (1000)    19556 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/unfold/unfold.py
--rw-rw-r--   0 dd        (1000) dd        (1000)     1774 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/unfold/vasp_constant.py
--rw-rw-r--   0 dd        (1000) dd        (1000)    48732 2023-04-05 15:24:57.000000 vaspvis-1.2.6/vaspvis/unfold/vaspwfc.py
--rw-rw-r--   0 dd        (1000) dd        (1000)    38651 2023-01-26 14:32:31.000000 vaspvis-1.2.6/vaspvis/utils.py
-drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-05 15:25:47.044004 vaspvis-1.2.6/vaspvis.egg-info/
--rw-rw-r--   0 dd        (1000) dd        (1000)    11478 2023-04-05 15:25:46.000000 vaspvis-1.2.6/vaspvis.egg-info/PKG-INFO
--rw-rw-r--   0 dd        (1000) dd        (1000)     1154 2023-04-05 15:25:46.000000 vaspvis-1.2.6/vaspvis.egg-info/SOURCES.txt
--rw-rw-r--   0 dd        (1000) dd        (1000)        1 2023-04-05 15:25:46.000000 vaspvis-1.2.6/vaspvis.egg-info/dependency_links.txt
--rw-rw-r--   0 dd        (1000) dd        (1000)       82 2023-04-05 15:25:46.000000 vaspvis-1.2.6/vaspvis.egg-info/requires.txt
--rw-rw-r--   0 dd        (1000) dd        (1000)        8 2023-04-05 15:25:46.000000 vaspvis-1.2.6/vaspvis.egg-info/top_level.txt
+drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-06 19:50:13.318025 vaspvis-1.2.7/
+-rw-rw-r--   0 dd        (1000) dd        (1000)     1056 2023-01-26 14:32:30.000000 vaspvis-1.2.7/LICENSE.txt
+-rw-rw-r--   0 dd        (1000) dd        (1000)       72 2023-01-26 14:32:30.000000 vaspvis-1.2.7/MANIFEST.in
+-rw-rw-r--   0 dd        (1000) dd        (1000)    11478 2023-04-06 19:50:13.318025 vaspvis-1.2.7/PKG-INFO
+-rw-rw-r--   0 dd        (1000) dd        (1000)    11176 2023-01-26 14:32:30.000000 vaspvis-1.2.7/README.md
+-rw-rw-r--   0 dd        (1000) dd        (1000)     6277 2023-01-26 14:32:30.000000 vaspvis-1.2.7/example.py
+drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-06 19:50:13.314025 vaspvis-1.2.7/img/
+-rw-rw-r--   0 dd        (1000) dd        (1000)   342587 2023-01-26 14:32:30.000000 vaspvis-1.2.7/img/band_atom_orbitals.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   348428 2023-01-26 14:32:30.000000 vaspvis-1.2.7/img/band_atom_spd.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   308011 2023-01-26 14:32:30.000000 vaspvis-1.2.7/img/band_atoms.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   462542 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_dos_atom_orbitals.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   454083 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_dos_atoms.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   394736 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_dos_element_orbitals.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   439321 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_dos_element_spd.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   450754 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_dos_elements.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   590551 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_dos_orbitals.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   243066 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_dos_plain.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   516200 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_dos_spd.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   278341 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_element_orbital.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   310041 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_element_spd.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   306319 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_elements.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   426076 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_orbital.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   174622 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_plain.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   359336 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/band_spd.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   137295 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/dos_atom_orbitals.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   157059 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/dos_atom_spd.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   163001 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/dos_atoms.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   124882 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/dos_element_orbitals.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   141064 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/dos_element_spd.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   161570 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/dos_elements.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   179699 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/dos_orbitals.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   101917 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/dos_plain.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)   170210 2023-01-26 14:32:31.000000 vaspvis-1.2.7/img/dos_spd.png
+-rw-rw-r--   0 dd        (1000) dd        (1000)       38 2023-04-06 19:50:13.318025 vaspvis-1.2.7/setup.cfg
+-rw-rw-r--   0 dd        (1000) dd        (1000)      788 2023-04-06 19:50:09.000000 vaspvis-1.2.7/setup.py
+drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-06 19:50:13.314025 vaspvis-1.2.7/vaspvis/
+-rw-rw-r--   0 dd        (1000) dd        (1000)      175 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/__init__.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)   107676 2023-02-28 20:42:29.000000 vaspvis-1.2.7/vaspvis/band.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)     6233 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/charge.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)    80193 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/dos.py
+drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-06 19:50:13.318025 vaspvis-1.2.7/vaspvis/passivator_utils/
+-rw-rw-r--   0 dd        (1000) dd        (1000)      136 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/passivator_utils/__init__.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)    11117 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/passivator_utils/passivator_utils.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)   347297 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/standard.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)    18075 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/stm.py
+drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-06 19:50:13.318025 vaspvis-1.2.7/vaspvis/unfold/
+-rw-rw-r--   0 dd        (1000) dd        (1000)       22 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/unfold/__init__.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)     6062 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/unfold/convert.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)    19858 2023-04-06 19:48:51.000000 vaspvis-1.2.7/vaspvis/unfold/unfold.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)     1774 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/unfold/vasp_constant.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)    48732 2023-04-05 15:24:57.000000 vaspvis-1.2.7/vaspvis/unfold/vaspwfc.py
+-rw-rw-r--   0 dd        (1000) dd        (1000)    38651 2023-01-26 14:32:31.000000 vaspvis-1.2.7/vaspvis/utils.py
+drwxrwxr-x   0 dd        (1000) dd        (1000)        0 2023-04-06 19:50:13.314025 vaspvis-1.2.7/vaspvis.egg-info/
+-rw-rw-r--   0 dd        (1000) dd        (1000)    11478 2023-04-06 19:50:13.000000 vaspvis-1.2.7/vaspvis.egg-info/PKG-INFO
+-rw-rw-r--   0 dd        (1000) dd        (1000)     1154 2023-04-06 19:50:13.000000 vaspvis-1.2.7/vaspvis.egg-info/SOURCES.txt
+-rw-rw-r--   0 dd        (1000) dd        (1000)        1 2023-04-06 19:50:13.000000 vaspvis-1.2.7/vaspvis.egg-info/dependency_links.txt
+-rw-rw-r--   0 dd        (1000) dd        (1000)       82 2023-04-06 19:50:13.000000 vaspvis-1.2.7/vaspvis.egg-info/requires.txt
+-rw-rw-r--   0 dd        (1000) dd        (1000)        8 2023-04-06 19:50:13.000000 vaspvis-1.2.7/vaspvis.egg-info/top_level.txt
```

### Comparing `vaspvis-1.2.6/LICENSE.txt` & `vaspvis-1.2.7/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/PKG-INFO` & `vaspvis-1.2.7/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vaspvis
-Version: 1.2.6
+Version: 1.2.7
 Summary: A highly flexible and customizable library for visualizing electronic structure data from VASP calculations
 Home-page: https://github.com/DerekDardzinski/vaspvis
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 # vaspvis
```

### Comparing `vaspvis-1.2.6/README.md` & `vaspvis-1.2.7/README.md`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/example.py` & `vaspvis-1.2.7/example.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_atom_orbitals.png` & `vaspvis-1.2.7/img/band_atom_orbitals.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_atom_spd.png` & `vaspvis-1.2.7/img/band_atom_spd.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_atoms.png` & `vaspvis-1.2.7/img/band_atoms.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_dos_atom_orbitals.png` & `vaspvis-1.2.7/img/band_dos_atom_orbitals.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_dos_atoms.png` & `vaspvis-1.2.7/img/band_dos_atoms.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_dos_element_orbitals.png` & `vaspvis-1.2.7/img/band_dos_element_orbitals.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_dos_element_spd.png` & `vaspvis-1.2.7/img/band_dos_element_spd.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_dos_elements.png` & `vaspvis-1.2.7/img/band_dos_elements.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_dos_orbitals.png` & `vaspvis-1.2.7/img/band_dos_orbitals.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_dos_plain.png` & `vaspvis-1.2.7/img/band_dos_plain.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_dos_spd.png` & `vaspvis-1.2.7/img/band_dos_spd.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_element_orbital.png` & `vaspvis-1.2.7/img/band_element_orbital.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_element_spd.png` & `vaspvis-1.2.7/img/band_element_spd.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_elements.png` & `vaspvis-1.2.7/img/band_elements.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_orbital.png` & `vaspvis-1.2.7/img/band_orbital.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_plain.png` & `vaspvis-1.2.7/img/band_plain.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/band_spd.png` & `vaspvis-1.2.7/img/band_spd.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/dos_atom_orbitals.png` & `vaspvis-1.2.7/img/dos_atom_orbitals.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/dos_atom_spd.png` & `vaspvis-1.2.7/img/dos_atom_spd.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/dos_atoms.png` & `vaspvis-1.2.7/img/dos_atoms.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/dos_element_orbitals.png` & `vaspvis-1.2.7/img/dos_element_orbitals.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/dos_element_spd.png` & `vaspvis-1.2.7/img/dos_element_spd.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/dos_elements.png` & `vaspvis-1.2.7/img/dos_elements.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/dos_orbitals.png` & `vaspvis-1.2.7/img/dos_orbitals.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/dos_plain.png` & `vaspvis-1.2.7/img/dos_plain.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/img/dos_spd.png` & `vaspvis-1.2.7/img/dos_spd.png`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/setup.py` & `vaspvis-1.2.7/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open("./README.md", "r") as fh:
     long_description = fh.read()
 
 setup(
     name="vaspvis",
-    version="1.2.6",
+    version="1.2.7",
     description="A highly flexible and customizable library for visualizing electronic structure data from VASP calculations",
     long_description=long_description,
     long_description_content_type="text/markdown",
     packages=find_packages(),
     install_requires=[
         "pymatgen",
         "matplotlib",
```

### Comparing `vaspvis-1.2.6/vaspvis/band.py` & `vaspvis-1.2.7/vaspvis/band.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis/charge.py` & `vaspvis-1.2.7/vaspvis/charge.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis/dos.py` & `vaspvis-1.2.7/vaspvis/dos.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis/passivator_utils/passivator_utils.py` & `vaspvis-1.2.7/vaspvis/passivator_utils/passivator_utils.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis/standard.py` & `vaspvis-1.2.7/vaspvis/standard.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis/stm.py` & `vaspvis-1.2.7/vaspvis/stm.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis/unfold/convert.py` & `vaspvis-1.2.7/vaspvis/unfold/convert.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis/unfold/unfold.py` & `vaspvis-1.2.7/vaspvis/unfold/unfold.py`

 * *Files 14% similar despite different names*

```diff
@@ -1,131 +1,149 @@
 #!/usr/bin/env python
-# -*- coding: utf-8 -*-   
+# -*- coding: utf-8 -*-
 
 ############################################################
 import numpy as np
 import multiprocessing
 from .vaspwfc import vaspwfc
 
 ############################################################
 
+
 def find_K_from_k(k, M):
-    '''
+    """
     Get the K vector of the supercell onto which the k vector of the primitive
     cell folds. The unfoliding vector G, which satisfy the following equation,
     is also returned.
 
         k = K + G
 
     where G is a reciprocal space vector of supercell
-    '''
+    """
 
     M = np.array(M)
     Kc = np.dot(k, M.T)
-    G = np.array(
-            np.round(Kc), dtype=int)
+    G = np.array(np.round(Kc), dtype=int)
     KG = Kc - np.round(Kc)
 
     return KG, G
 
+
 def LorentzSmearing(x, x0, sigma=0.02):
-    '''
+    """
     Simulate the Delta function by a Lorentzian shape function
-        
+
         \Delta(x) = \lim_{\sigma\to 0}  Lorentzian
-    '''
+    """
+
+    return 1.0 / np.pi * sigma**2 / ((x - x0) ** 2 + sigma**2)
 
-    return 1./ np.pi * sigma**2 / ((x - x0)**2 + sigma**2)
 
 def GaussianSmearing(x, x0, sigma=0.02):
-    '''
+    """
     Simulate the Delta function by a Lorentzian shape function
-        
+
         \Delta(x) = \lim_{\sigma\to 0} Gaussian
-    '''
+    """
+
+    return (
+        1.0
+        / (np.sqrt(2 * np.pi) * sigma)
+        * np.exp(-((x - x0) ** 2) / (2 * sigma**2))
+    )
 
-    return 1. / (np.sqrt(2*np.pi) * sigma) * np.exp(-(x - x0)**2 / (2*sigma**2))
 
 def removeDuplicateKpoints(kpoints):
-    '''
+    """
     remove duplicate kpoints in the list.
-    '''
-    kpoints = np.array(
-            sorted(kpoints, key=lambda x: (x[0], x[1], x[2]))
-            )
+    """
+    kpoints = np.array(sorted(kpoints, key=lambda x: (x[0], x[1], x[2])))
     kdiff = np.diff(kpoints, axis=0)
-    match = np.abs(np.linalg.norm(kdiff, axis=1)) > 1E-5
+    match = np.abs(np.linalg.norm(kdiff, axis=1)) > 1e-5
 
     return kpoints[np.r_[True, match]]
 
-def save2VaspKPOINTS(kpoints, output='KPOINTS'):
-    '''
+
+def save2VaspKPOINTS(kpoints, output="KPOINTS"):
+    """
     save to VASP KPOINTS file
-    '''
+    """
     kpoints = np.array(kpoints)
-    nkpts   = kpoints.shape[0]
+    nkpts = kpoints.shape[0]
 
-    with open(output, 'w') as vaspkpt:
-        vaspkpt.write('kpoints generated by PYVASPWFC\n')
-        vaspkpt.write('%d\n' % nkpts)
-        vaspkpt.write('Rec\n')
+    with open(output, "w") as vaspkpt:
+        vaspkpt.write("kpoints generated by PYVASPWFC\n")
+        vaspkpt.write("%d\n" % nkpts)
+        vaspkpt.write("Rec\n")
         for ik in range(nkpts):
-            line = '  %12.8f %12.8f %12.8f 1.0\n' % (kpoints[ik,0], kpoints[ik,1], kpoints[ik,2])
+            line = "  %12.8f %12.8f %12.8f 1.0\n" % (
+                kpoints[ik, 0],
+                kpoints[ik, 1],
+                kpoints[ik, 2],
+            )
             vaspkpt.write(line)
 
+
 def make_kpath(kbound, nseg=40):
-    '''
-    make a list of kpoints defining the path between the given kpoints. 
-    '''
+    """
+    make a list of kpoints defining the path between the given kpoints.
+    """
     kbound = np.array(kbound, dtype=float)
-    kdist  = np.diff(kbound, axis=0)
+    kdist = np.diff(kbound, axis=0)
 
     # kpath = []
     # for ii in range(len(kdist)):
     #     for nk in range(nseg):
     #         kpt = kbound[ii] + kdist[ii] / nseg * nk
     #         kpath.append(kpt)
 
-    kpath = [kbound[ii] + kdist[ii] / nseg * nk
-             for ii in range(len(kdist))
-             for nk in range(nseg)]
+    kpath = [
+        kbound[ii] + kdist[ii] / nseg * nk
+        for ii in range(len(kdist))
+        for nk in range(nseg)
+    ]
     kpath.append(kbound[-1])
     return kpath
 
-def EBS_scatter(kpts, cell, spectral_weight,
-                eref=0.0,
-                nseg=None, save='ebs_s.png',
-                kpath_label=[],
-                factor=20, figsize=(3.0, 4.0),
-                ylim=(-3, 3), show=True,
-                color='b'):
-    '''
+
+def EBS_scatter(
+    kpts,
+    cell,
+    spectral_weight,
+    eref=0.0,
+    nseg=None,
+    save="ebs_s.png",
+    kpath_label=[],
+    factor=20,
+    figsize=(3.0, 4.0),
+    ylim=(-3, 3),
+    show=True,
+    color="b",
+):
+    """
     plot the effective band structure with scatter, the size of the scatter
     indicates the spectral weight.
     The plotting function utilizes Matplotlib package.
 
     inputs:
         kpts: the kpoints vectors in fractional coordinates.
         cell: the primitive cell basis
         spectral_weight: self-explanatory
-    '''
+    """
 
     import matplotlib as mpl
-    mpl.use('agg')
+
+    mpl.use("agg")
     import matplotlib.pyplot as plt
 
-    mpl.rcParams['axes.unicode_minus'] = False
+    mpl.rcParams["axes.unicode_minus"] = False
 
     nspin = spectral_weight.shape[0]
     kpt_c = np.dot(kpts, np.linalg.inv(cell).T)
-    kdist = np.r_[0, np.cumsum(
-                            np.linalg.norm(
-                                np.diff(kpt_c, axis=0),
-                                axis=1
-                            ))]
+    kdist = np.r_[0, np.cumsum(np.linalg.norm(np.diff(kpt_c, axis=0), axis=1))]
     nk = kdist.size
     nb = spectral_weight.shape[2]
     x0 = np.ones(nb)
 
     fig = plt.figure()
     fig.set_size_inches(figsize)
     if nspin == 1:
@@ -134,247 +152,265 @@
     else:
         axes = [plt.subplot(121), plt.subplot(122)]
         fig.set_size_inches((figsize[0] * 2, figsize[1]))
 
     for ispin in range(nspin):
         ax = axes[ispin]
         for ik in range(nk):
-            ax.scatter(kdist[ik] * x0,
-                       spectral_weight[ispin,ik,:,0] - eref,
-                       s=spectral_weight[ispin,ik,:,1] * factor,
-                       lw=0.0,
-                       #  color=color
-                       )
+            ax.scatter(
+                kdist[ik] * x0,
+                spectral_weight[ispin, ik, :, 0] - eref,
+                s=spectral_weight[ispin, ik, :, 1] * factor,
+                lw=0.0,
+                #  color=color
+            )
 
         ax.set_xlim(0, kdist.max())
         ax.set_ylim(*ylim)
-        ax.set_ylabel('Energy [eV]', labelpad=5)
+        ax.set_ylabel("Energy [eV]", labelpad=5)
 
         if nseg:
             for kb in kdist[::nseg]:
-                ax.axvline(x=kb, lw=0.5, color='k', ls=':', alpha=0.8)
+                ax.axvline(x=kb, lw=0.5, color="k", ls=":", alpha=0.8)
 
             if kpath_label:
                 ax.set_xticks(np.r_[kdist[::nseg], kdist[-1]])
                 kname = [x.upper() for x in kpath_label]
                 for ii in range(len(kname)):
-                    if kname[ii] == 'G':
-                        kname[ii] = r'$\mathrm{\mathsf{\Gamma}}$'
+                    if kname[ii] == "G":
+                        kname[ii] = r"$\mathrm{\mathsf{\Gamma}}$"
                     else:
-                        kname[ii] = r'$\mathrm{\mathsf{%s}}$' % kname[ii]
+                        kname[ii] = r"$\mathrm{\mathsf{%s}}$" % kname[ii]
                 ax.set_xticklabels(kname)
 
     plt.tight_layout(pad=0.2)
     plt.savefig(save, dpi=360)
-    if show: plt.show()
+    if show:
+        plt.show()
 
-def EBS_cmaps(kpts, cell, E0, spectral_function,
-              eref=0.0, nseg=None,
-              kpath_label=[],
-              save='ebs_c.png',
-              figsize=(3.0, 4.0),
-              ylim=(-3, 3), show=True,
-              cmap='jet'):
-    '''
+
+def EBS_cmaps(
+    kpts,
+    cell,
+    E0,
+    spectral_function,
+    eref=0.0,
+    nseg=None,
+    kpath_label=[],
+    save="ebs_c.png",
+    figsize=(3.0, 4.0),
+    ylim=(-3, 3),
+    show=True,
+    cmap="jet",
+):
+    """
     plot the effective band structure with colormaps.  The plotting function
     utilizes Matplotlib package.
 
     inputs:
         kpts: the kpoints vectors in fractional coordinates.
         cell: the primitive cell basis
         spectral_weight: self-explanatory
-    '''
+    """
 
     import matplotlib as mpl
-    mpl.use('agg')
+
+    mpl.use("agg")
     import matplotlib.pyplot as plt
 
-    mpl.rcParams['axes.unicode_minus'] = False
+    mpl.rcParams["axes.unicode_minus"] = False
 
     nspin = spectral_function.shape[0]
     kpt_c = np.dot(kpts, np.linalg.inv(cell).T)
-    kdist = np.r_[0, np.cumsum(
-                            np.linalg.norm(
-                                np.diff(kpt_c, axis=0),
-                                axis=1
-                            ))]
+    kdist = np.r_[0, np.cumsum(np.linalg.norm(np.diff(kpt_c, axis=0), axis=1))]
     nk = kdist.size
     xmin, xmax = kdist.min(), kdist.max()
     # ymin, ymax = E0.min() - eref, E0.max() - eref
 
     fig = plt.figure()
     if nspin == 1:
         axes = [plt.subplot(111)]
         fig.set_size_inches(figsize)
     else:
         axes = [plt.subplot(121), plt.subplot(122)]
         fig.set_size_inches((figsize[0] * 2, figsize[1]))
 
-    # ax.imshow(spectral_function, extent=(xmin, xmax, ymin, ymax), 
+    # ax.imshow(spectral_function, extent=(xmin, xmax, ymin, ymax),
     #           origin='lower', aspect='auto', cmap=cmap)
     X, Y = np.meshgrid(kdist, E0 - eref)
     for ispin in range(nspin):
         ax = axes[ispin]
         ax.contourf(X, Y, spectral_function[ispin], cmap=cmap)
 
         ax.set_xlim(xmin, xmax)
         ax.set_ylim(*ylim)
-        ax.set_ylabel('Energy [eV]', labelpad=5)
+        ax.set_ylabel("Energy [eV]", labelpad=5)
 
         if nseg:
             for kb in kdist[::nseg]:
-                ax.axvline(x=kb, lw=0.5, color='k', ls=':', alpha=0.8)
+                ax.axvline(x=kb, lw=0.5, color="k", ls=":", alpha=0.8)
 
             if kpath_label:
                 ax.set_xticks(np.r_[kdist[::nseg], kdist[-1]])
                 kname = [x.upper() for x in kpath_label]
                 for ii in range(len(kname)):
-                    if kname[ii] == 'G':
-                        kname[ii] = r'$\mathrm{\mathsf{\Gamma}}$'
+                    if kname[ii] == "G":
+                        kname[ii] = r"$\mathrm{\mathsf{\Gamma}}$"
                     else:
-                        kname[ii] = r'$\mathrm{\mathsf{%s}}$' % kname[ii]
+                        kname[ii] = r"$\mathrm{\mathsf{%s}}$" % kname[ii]
                 ax.set_xticklabels(kname)
 
     plt.tight_layout(pad=0.2)
     plt.savefig(save, dpi=360)
-    if show: plt.show()
+    if show:
+        plt.show()
+
+
 ############################################################
 
-class unfold():
-    '''
+
+class unfold:
+    """
     Unfold the band structure from Supercell calculation into a primitive cell and
     obtain the effective band structure (EBS).
-    
+
     REF:
     "Extracting E versus k effective band structure from supercell
      calculations on alloys and impurities"
     Phys. Rev. B 85, 085201 (2012)
-    '''
+    """
 
-    def __init__(self, M=None, wavecar='WAVECAR', gamma=False, lsorbit=False,
-                 gamma_half='x'):
-        '''
+    def __init__(
+        self,
+        M=None,
+        wavecar="WAVECAR",
+        gamma=False,
+        lsorbit=False,
+        gamma_half="x",
+    ):
+        """
         Initialization.
 
-        M is the transformation matrix between supercell and primitive cell: 
+        M is the transformation matrix between supercell and primitive cell:
 
-            M = np.dot(A, np.linalg.inv(a))     
+            M = np.dot(A, np.linalg.inv(a))
 
         In real space, the basis vectors of Supercell (A) and those of the
         primitive cell (a) satisfy:
 
             A = np.dot(M, a);      a = np.dot(np.linalg.inv(M), A)
 
         Whereas in reciprocal space
 
-            b = np.dot(M.T, B);    B = np.dot(np.linalg.inv(M).T, b)    
+            b = np.dot(M.T, B);    B = np.dot(np.linalg.inv(M).T, b)
 
         wavecar is the location of VASP WAVECAR file that contains the
         wavefunction information of a supercell calculation.
-        '''
+        """
 
         # Whether the WAVECAR is a gamma-only version
         self._lgam = gamma
         self._lsoc = lsorbit
 
         self.M = np.array(M, dtype=float)
-        assert self.M.shape == (3,3), 'Shape of the tranformation matrix must be (3,3)'
-
-        self.wfc = vaspwfc(wavecar, lsorbit=self._lsoc, lgamma=self._lgam,
-                           gamma_half=gamma_half)
+        assert self.M.shape == (
+            3,
+            3,
+        ), "Shape of the tranformation matrix must be (3,3)"
+
+        self.wfc = vaspwfc(
+            wavecar,
+            lsorbit=self._lsoc,
+            lgamma=self._lgam,
+            gamma_half=gamma_half,
+        )
         # all the K-point vectors
         self.kvecs = self.wfc._kvecs
         # all the KS energies
         self.bands = self.wfc._bands
         #  print(self.bands[0][15])
 
         # G-vectors within the cutoff sphere, let's just do it once for all.
         # self.allGvecs = np.array([self.wfc.gvectors(ikpt=kpt+1)
         #                           for kpt in range(self.wfc._nkpts)], dtype=int)
 
         # spectral weight for all the kpoints
         self.SW = None
 
-    def get_ovlap_G(self, ikpt=1, epsilon=1E-5):
-        '''
+    def get_ovlap_G(self, ikpt=1, epsilon=1e-5):
+        """
         Get subset of the reciprocal space vectors of the supercell,
         specifically the ones that match the reciprocal space vectors of the
         primitive cell.
-        '''
+        """
 
-        assert 1 <= ikpt <= self.wfc._nkpts, 'Invalid K-point index!'
+        assert 1 <= ikpt <= self.wfc._nkpts, "Invalid K-point index!"
 
         # Reciprocal space vectors of the supercell in fractional unit
         Gvecs = self.wfc.gvectors(ikpt=ikpt)
         # Gvecs = self.allGvecs[ikpt - 1]
 
         if self._lgam:
             nplw = Gvecs.shape[0]
-            tmp  = np.zeros((nplw * 2 - 1, 3), dtype=int)
+            tmp = np.zeros((nplw * 2 - 1, 3), dtype=int)
             # the gvectors of Gamma version only contains half the number of a
-            # normal version. 
-            tmp[:nplw,...] = Gvecs
-            tmp[nplw:,...] = -Gvecs[1:,...]            # G' = -G
+            # normal version.
+            tmp[:nplw, ...] = Gvecs
+            tmp[nplw:, ...] = -Gvecs[1:, ...]  # G' = -G
 
             Gvecs = tmp
 
         # Shape of Gvecs: (nplws, 3)
         # iGvecs = np.arange(Gvecs.shape[0], dtype=int)
 
         # Reciprocal space vectors of the primitive cell
         gvecs = np.dot(Gvecs, np.linalg.inv(self.M).T)
         # Deviation from the perfect sites
         gd = gvecs - np.round(gvecs)
         # match = np.linalg.norm(gd, axis=1) < epsilon
-        match = np.alltrue(
-                    np.abs(gd) < epsilon, axis=1
-                )
+        match = np.alltrue(np.abs(gd) < epsilon, axis=1)
 
         # return Gvecs[match], iGvecs[match]
         return Gvecs[match], Gvecs
 
     def find_K_index(self, K0):
-        '''
+        """
         Find the index of K0.
-        '''
+        """
 
         for ii in range(self.wfc._nkpts):
-            if np.alltrue(
-                    np.abs(self.wfc._kvecs[ii] - K0) < 1E-5
-               ):
+            if np.alltrue(np.abs(self.wfc._kvecs[ii] - K0) < 1e-5):
                 return ii + 1
         # the for-else
         else:
             raise ValueError(
-                    'Cannot find the corresponding K-points in WAVECAR!' 
-                    )
+                "Cannot find the corresponding K-points in WAVECAR!"
+            )
 
     def k2K_map(self, kpath):
-        '''
+        """
         Find the map from primitive-cell k-points to supercell k-points.
-        '''
+        """
 
         return [
-            self.find_K_index(
-                find_K_from_k(k, self.M)[0]
-            ) - 1 for k in kpath
+            self.find_K_index(find_K_from_k(k, self.M)[0]) - 1 for k in kpath
         ]
 
     def spectral_weight_k(self, k0, whichspin=1):
-        '''
+        """
         Spectral weight for a given k:
 
             P_{Km}(k) = \sum_n |<Km | kn>|^2
 
         which is equivalent to
 
             P_{Km}(k) = \sum_{G} |C_{Km}(G + k - K)|^2
 
         where {G} is a subset of the reciprocal space vectors of the supercell.
-        '''
+        """
 
         #  print('Processing k-point %8.4f %8.4f %8.4f' % (k0[0], k0[1], k0[2]))
 
         # find the K0 onto which k0 folds
         # k0 = G0 + K0
         K0, G0 = find_K_from_k(k0, self.M)
         # find index of K0
@@ -383,18 +419,18 @@
         # get the overlap G-vectors
         Gvalid, Gall = self.get_ovlap_G(ikpt=ikpt)
         # Gnew = Gvalid + k0 - K0
         Goffset = Gvalid + G0[np.newaxis, :]
 
         # Index of the Gvalid in 3D grid
         GallIndex = Gall % self.wfc._ngrid[np.newaxis, :]
-        GoffsetIndex   = Goffset % self.wfc._ngrid[np.newaxis, :]
+        GoffsetIndex = Goffset % self.wfc._ngrid[np.newaxis, :]
 
         # 3d grid for planewave coefficients
-        wfc_k_3D = np.zeros(self.wfc._ngrid, dtype=np.complex)
+        wfc_k_3D = np.zeros(self.wfc._ngrid, dtype=np.complex128)
 
         # if self._lsoc:
         #     # the weights and corresponding energies
         #     P_Km = np.zeros((2, self.wfc._nbands), dtype=float)
         #     E_Km = np.zeros((2, self.wfc._nbands), dtype=float)
         # else:
         #     # the weights and corresponding energies
@@ -408,53 +444,75 @@
         for nb in range(self.wfc._nbands):
             # initialize the array to zero, which is unnecessary since the
             # GallIndex is the same for the same K-point
             # wfc_k_3D[:,:,:] = 0.0
 
             if self._lsoc:
                 # pad the coefficients to 3D grid
-                band_coeff = self.wfc.readBandCoeff(ispin=whichspin, ikpt=ikpt,
-                                                    iband=nb + 1, norm=True)
+                band_coeff = self.wfc.readBandCoeff(
+                    ispin=whichspin, ikpt=ikpt, iband=nb + 1, norm=True
+                )
                 nplw = band_coeff.shape[0] // 2
                 band_spinor_coeff = [band_coeff[:nplw], band_coeff[nplw:]]
 
                 # energy
-                E_Km[nb] = self.bands[whichspin-1,ikpt-1,nb]
+                E_Km[nb] = self.bands[whichspin - 1, ikpt - 1, nb]
                 for Ispinor in range(2):
                     # band = band_spinor_coeff[Ispinor]
                     # band /= np.linalg.norm(band)
-                    wfc_k_3D[GallIndex[:,0], GallIndex[:,1], GallIndex[:,2]] = band_spinor_coeff[Ispinor]
-
-                    # spectral weight 
-                    P_Km[nb] += np.linalg.norm(
-                                wfc_k_3D[GoffsetIndex[:,0], GoffsetIndex[:,1], GoffsetIndex[:,2]]
-                            )**2
+                    wfc_k_3D[
+                        GallIndex[:, 0], GallIndex[:, 1], GallIndex[:, 2]
+                    ] = band_spinor_coeff[Ispinor]
+
+                    # spectral weight
+                    P_Km[nb] += (
+                        np.linalg.norm(
+                            wfc_k_3D[
+                                GoffsetIndex[:, 0],
+                                GoffsetIndex[:, 1],
+                                GoffsetIndex[:, 2],
+                            ]
+                        )
+                        ** 2
+                    )
             else:
                 # pad the coefficients to 3D grid
-                band_coeff = self.wfc.readBandCoeff(ispin=whichspin, ikpt=ikpt, iband=nb + 1, norm=True)
+                band_coeff = self.wfc.readBandCoeff(
+                    ispin=whichspin, ikpt=ikpt, iband=nb + 1, norm=True
+                )
                 if self._lgam:
                     nplw = band_coeff.size
-                    tmp  = np.zeros((nplw * 2 - 1), dtype=band_coeff.dtype)
+                    tmp = np.zeros((nplw * 2 - 1), dtype=band_coeff.dtype)
                     # for Gamma version, the coefficients corresponding to G \ne 0
                     # is multiplied by a factor of sqrt(2)
-                    band_coeff[1:] /= np.sqrt(2.)
+                    band_coeff[1:] /= np.sqrt(2.0)
                     tmp[:nplw] = band_coeff
                     tmp[nplw:] = band_coeff[1:].conj()
                     band_coeff = tmp
 
-                wfc_k_3D[GallIndex[:,0], GallIndex[:,1], GallIndex[:,2]] = band_coeff
+                wfc_k_3D[
+                    GallIndex[:, 0], GallIndex[:, 1], GallIndex[:, 2]
+                ] = band_coeff
                 # energy
-                E_Km[nb] = self.bands[whichspin-1,ikpt-1,nb]
-                # spectral weight 
-                P_Km[nb] = np.linalg.norm(
-                            wfc_k_3D[GoffsetIndex[:,0], GoffsetIndex[:,1], GoffsetIndex[:,2]]
-                        )**2
-
+                E_Km[nb] = self.bands[whichspin - 1, ikpt - 1, nb]
+                # spectral weight
+                P_Km[nb] = (
+                    np.linalg.norm(
+                        wfc_k_3D[
+                            GoffsetIndex[:, 0],
+                            GoffsetIndex[:, 1],
+                            GoffsetIndex[:, 2],
+                        ]
+                    )
+                    ** 2
+                )
 
-        return np.array((E_Km, P_Km, ikpt-1 * np.ones(len(E_Km))), dtype=float).T
+        return np.array(
+            (E_Km, P_Km, ikpt - 1 * np.ones(len(E_Km))), dtype=float
+        ).T
 
     # def spectral_weight(self, kpoints, nproc=None):
     #     '''
     #     Calculate the spectral weight for a list of kpoints in the primitive BZ.
     #     Here, we use "multiprocessing" package to parallel over the kpoints.
     #     '''
     #
@@ -472,120 +530,136 @@
     #
     #     self.SW = np.array([res.get() for res in results], dtype=float)
     #
     #     pool.close()
     #     pool.join()
     #
     #     return self.SW
-        
+
     def spectral_weight(self, kpoints):
-        '''
+        """
         Calculate the spectral weight for a list of kpoints in the primitive BZ.
-        '''
+        """
 
         NKPTS = len(kpoints)
 
         # self.SW = np.array([self.spectral_weight_k(kpoints[ik])
         #                     for ik in range(NKPTS)], dtype=float)
         sw = []
         for ispin in range(self.wfc._nspin):
             if self.wfc._nspin == 2:
                 print("#" * 60)
                 print("Spin component: %d" % ispin)
                 print("#" * 60)
-            sw.append([self.spectral_weight_k(kpoints[ik], whichspin=ispin+1)
-                       for ik in range(NKPTS)])
+            sw.append(
+                [
+                    self.spectral_weight_k(kpoints[ik], whichspin=ispin + 1)
+                    for ik in range(NKPTS)
+                ]
+            )
 
         self.SW = np.array(sw)
 
         # For noncollinear calculation, nspin = 1.
         # if self._lsoc:
         #     # self.SW = np.swapaxes(self.SW, 0, 1)
         #     self.SW = np.array([self.SW[0,:,:,0,:], self.SW[0,:,:,1,]])
 
         return self.SW
 
     def spectral_function(self, nedos=4000, sigma=0.02):
-        '''
+        """
         Generate the spectral function
 
             A(k_i, E) = \sum_m P_{Km}(k_i)\Delta(E - Em)
 
         Where the \Delta function can be approximated by Lorentzian or Gaussian
         function.
-        '''
+        """
 
-        assert self.SW is not None, 'Spectral weight must be calculated first!'
+        assert self.SW is not None, "Spectral weight must be calculated first!"
 
         # NS = 2 if self._lsoc else self.wfc._nspin
         # For noncollinear calculation, nspin = 1.
         NS = self.wfc._nspin
         # Number of kpoints
         nk = self.SW.shape[1]
         # spectral function
         SF = np.zeros((NS, nedos, nk), dtype=float)
 
-        emin = self.SW[:,:,:,0].min()
-        emax = self.SW[:,:,:,0].max()
+        emin = self.SW[:, :, :, 0].min()
+        emax = self.SW[:, :, :, 0].max()
         e0 = np.linspace(emin - 5 * sigma, emax + 5 * sigma, nedos)
 
         for ispin in range(NS):
             for ii in range(nk):
-                E_Km = self.SW[ispin,ii,:,0]
-                P_Km = self.SW[ispin,ii,:,1]
+                E_Km = self.SW[ispin, ii, :, 0]
+                P_Km = self.SW[ispin, ii, :, 1]
 
-                SF[ispin,:,ii] = np.sum(
-                            LorentzSmearing(
-                                e0[:,np.newaxis], E_Km[np.newaxis,:],
-                                sigma=sigma
-                            ) * P_Km[np.newaxis,:], axis=1
-                        )
+                SF[ispin, :, ii] = np.sum(
+                    LorentzSmearing(
+                        e0[:, np.newaxis], E_Km[np.newaxis, :], sigma=sigma
+                    )
+                    * P_Km[np.newaxis, :],
+                    axis=1,
+                )
         return e0, SF
 
+
 ############################################################
 
-if __name__ == '__main__':
-    M = [[3.0, 0.0, 0.0],
-         [0.0, 3.0, 0.0],
-         [0.0, 0.0, 1.0]]
-
-    kpts = [[0.0, 0.5, 0.0],
-            [0.0, 0.0, 0.0],
-            [1./3, 1./3, 0.0],
-            [0.0, 0.5, 0.0]]
+if __name__ == "__main__":
+    M = [[3.0, 0.0, 0.0], [0.0, 3.0, 0.0], [0.0, 0.0, 1.0]]
+
+    kpts = [
+        [0.0, 0.5, 0.0],
+        [0.0, 0.0, 0.0],
+        [1.0 / 3, 1.0 / 3, 0.0],
+        [0.0, 0.5, 0.0],
+    ]
 
     kpath = make_kpath(kpts, nseg=30)
 
     K_in_sup = []
     for kk in kpath:
         kg, g = find_K_from_k(kk, M)
         K_in_sup.append(kg)
     reducedK = removeDuplicateKpoints(K_in_sup)
     save2VaspKPOINTS(reducedK)
 
     import os
+
     # from ase.io import read, write
     #
     # pos = read('POSCAR.p', format='vasp')
     # cell = pos.cell
-    cell = [[ 3.1850, 0.0000000000000000,  0.0],
-            [-1.5925, 2.7582909110534373,  0.0],
-            [ 0.0000, 0.0000000000000000, 35.0]]
-
-    if os.path.isfile('spectral_function.npy'):
-        sw = np.load('spectral_weight.npy')
-        sf = np.load('spectral_function.npy')
-        e0 = np.load('energy.npy')
+    cell = [
+        [3.1850, 0.0000000000000000, 0.0],
+        [-1.5925, 2.7582909110534373, 0.0],
+        [0.0000, 0.0000000000000000, 35.0],
+    ]
+
+    if os.path.isfile("spectral_function.npy"):
+        sw = np.load("spectral_weight.npy")
+        sf = np.load("spectral_function.npy")
+        e0 = np.load("energy.npy")
     else:
-        fwave = unfold(M=M, wavecar='WAVECAR')
+        fwave = unfold(M=M, wavecar="WAVECAR")
         sw = fwave.spectral_weight(kpath)
         e0, sf = fwave.spectral_function(nedos=4000)
-        np.save('spectral_weight.npy', sw)
-        np.save('spectral_function.npy', sf)
-        np.save('energy.npy', e0)
-
-    EBS_scatter(kpath, cell, sw, nseg=30, eref=-4.01,
-            ylim=(-3, 4), show=False,
-            factor=5)
-    EBS_cmaps(kpath, cell, e0, sf, nseg=30, eref=-4.01,
-            show=False,
-            ylim=(-3, 4))
+        np.save("spectral_weight.npy", sw)
+        np.save("spectral_function.npy", sf)
+        np.save("energy.npy", e0)
+
+    EBS_scatter(
+        kpath,
+        cell,
+        sw,
+        nseg=30,
+        eref=-4.01,
+        ylim=(-3, 4),
+        show=False,
+        factor=5,
+    )
+    EBS_cmaps(
+        kpath, cell, e0, sf, nseg=30, eref=-4.01, show=False, ylim=(-3, 4)
+    )
```

### Comparing `vaspvis-1.2.6/vaspvis/unfold/vasp_constant.py` & `vaspvis-1.2.7/vaspvis/unfold/vasp_constant.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis/unfold/vaspwfc.py` & `vaspvis-1.2.7/vaspvis/unfold/vaspwfc.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis/utils.py` & `vaspvis-1.2.7/vaspvis/utils.py`

 * *Files identical despite different names*

### Comparing `vaspvis-1.2.6/vaspvis.egg-info/PKG-INFO` & `vaspvis-1.2.7/vaspvis.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: vaspvis
-Version: 1.2.6
+Version: 1.2.7
 Summary: A highly flexible and customizable library for visualizing electronic structure data from VASP calculations
 Home-page: https://github.com/DerekDardzinski/vaspvis
 License: MIT
 Description-Content-Type: text/markdown
 License-File: LICENSE.txt
 
 # vaspvis
```

### Comparing `vaspvis-1.2.6/vaspvis.egg-info/SOURCES.txt` & `vaspvis-1.2.7/vaspvis.egg-info/SOURCES.txt`

 * *Files identical despite different names*

