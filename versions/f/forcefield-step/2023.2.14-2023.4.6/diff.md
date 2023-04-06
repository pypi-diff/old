# Comparing `tmp/forcefield_step-2023.2.14.tar.gz` & `tmp/forcefield_step-2023.4.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "forcefield_step-2023.2.14.tar", last modified: Tue Feb 14 14:28:23 2023, max compression
+gzip compressed data, was "forcefield_step-2023.4.6.tar", last modified: Thu Apr  6 15:40:42 2023, max compression
```

## Comparing `forcefield_step-2023.2.14.tar` & `forcefield_step-2023.4.6.tar`

### file list

```diff
@@ -1,59 +1,60 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.572760 forcefield_step-2023.2.14/
--rw-r--r--   0 runner    (1001) docker     (123)      126 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/AUTHORS.rst
--rw-r--r--   0 runner    (1001) docker     (123)     3315 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/CONTRIBUTING.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1044 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/HISTORY.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1509 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      303 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     4162 2023-02-14 14:28:23.572760 forcefield_step-2023.2.14/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2261 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.564760 forcefield_step-2023.2.14/docs/
--rw-r--r--   0 runner    (1001) docker     (123)     6798 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/Makefile
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.564760 forcefield_step-2023.2.14/docs/_static/
--rw-r--r--   0 runner    (1001) docker     (123)    20790 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/_static/SEAMM inverted.png
--rw-r--r--   0 runner    (1001) docker     (123)    17802 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/_static/SEAMM logo.png
--rw-r--r--   0 runner    (1001) docker     (123)    79373 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/_static/molssi_main_logo.png
--rw-r--r--   0 runner    (1001) docker     (123)    68255 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/_static/molssi_main_logo_inverted_white.png
--rw-r--r--   0 runner    (1001) docker     (123)    63967 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/_static/molssi_square.png
--rw-r--r--   0 runner    (1001) docker     (123)    32355 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/_static/nsf.png
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.564760 forcefield_step-2023.2.14/docs/api/
--rw-r--r--   0 runner    (1001) docker     (123)      182 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/api/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/authors.rst
--rwxr-xr-x   0 runner    (1001) docker     (123)     9604 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/conf.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.568760 forcefield_step-2023.2.14/docs/developer_guide/
--rw-r--r--   0 runner    (1001) docker     (123)       36 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/developer_guide/contributing.rst
--rw-r--r--   0 runner    (1001) docker     (123)      234 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/developer_guide/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1212 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/developer_guide/installation.rst
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/developer_guide/readme.rst
--rw-r--r--   0 runner    (1001) docker     (123)       92 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/developer_guide/usage.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.568760 forcefield_step-2023.2.14/docs/getting_started/
--rw-r--r--   0 runner    (1001) docker     (123)     1035 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/getting_started/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/history.rst
--rw-r--r--   0 runner    (1001) docker     (123)     1301 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/index.rst
--rw-r--r--   0 runner    (1001) docker     (123)     6477 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/make.bat
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.568760 forcefield_step-2023.2.14/docs/user_guide/
--rw-r--r--   0 runner    (1001) docker     (123)      240 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/docs/user_guide/index.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.572760 forcefield_step-2023.2.14/forcefield_step/
--rw-r--r--   0 runner    (1001) docker     (123)      722 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/forcefield_step/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      501 2023-02-14 14:28:23.572760 forcefield_step-2023.2.14/forcefield_step/_version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.568760 forcefield_step-2023.2.14/forcefield_step/data/
--rw-r--r--   0 runner    (1001) docker     (123)     7938 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/forcefield_step/data/nacl_water.frc
--rw-r--r--   0 runner    (1001) docker     (123)   474898 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/forcefield_step/data/oplsaa.frc
--rw-r--r--   0 runner    (1001) docker     (123)   361764 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/forcefield_step/data/pcff2018.frc
--rw-r--r--   0 runner    (1001) docker     (123)     9974 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/forcefield_step/forcefield.py
--rw-r--r--   0 runner    (1001) docker     (123)     2888 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/forcefield_step/forcefield_parameters.py
--rw-r--r--   0 runner    (1001) docker     (123)     1208 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/forcefield_step/forcefield_step.py
--rw-r--r--   0 runner    (1001) docker     (123)     3955 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/forcefield_step/tk_forcefield.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.568760 forcefield_step-2023.2.14/forcefield_step.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     4162 2023-02-14 14:28:23.000000 forcefield_step-2023.2.14/forcefield_step.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1252 2023-02-14 14:28:23.000000 forcefield_step-2023.2.14/forcefield_step.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-14 14:28:23.000000 forcefield_step-2023.2.14/forcefield_step.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      130 2023-02-14 14:28:23.000000 forcefield_step-2023.2.14/forcefield_step.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       30 2023-02-14 14:28:23.000000 forcefield_step-2023.2.14/forcefield_step.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-02-14 14:28:23.000000 forcefield_step-2023.2.14/forcefield_step.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)      375 2023-02-14 14:28:23.572760 forcefield_step-2023.2.14/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     2907 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-14 14:28:23.572760 forcefield_step-2023.2.14/tests/
--rw-r--r--   0 runner    (1001) docker     (123)       70 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1465 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/tests/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)      592 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/tests/test_forcefield_step.py
--rw-r--r--   0 runner    (1001) docker     (123)   153001 2023-02-14 14:28:03.000000 forcefield_step-2023.2.14/tests/test_oplsaa_assignment.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.384149 forcefield_step-2023.4.6/
+-rw-r--r--   0 runner    (1001) docker     (123)      126 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/AUTHORS.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     3315 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/CONTRIBUTING.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1167 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/HISTORY.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1509 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      303 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     4284 2023-04-06 15:40:42.384149 forcefield_step-2023.4.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2261 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.376150 forcefield_step-2023.4.6/docs/
+-rw-r--r--   0 runner    (1001) docker     (123)     6798 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/Makefile
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.376150 forcefield_step-2023.4.6/docs/_static/
+-rw-r--r--   0 runner    (1001) docker     (123)    20790 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/_static/SEAMM inverted.png
+-rw-r--r--   0 runner    (1001) docker     (123)    17802 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/_static/SEAMM logo.png
+-rw-r--r--   0 runner    (1001) docker     (123)    79373 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/_static/molssi_main_logo.png
+-rw-r--r--   0 runner    (1001) docker     (123)    68255 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/_static/molssi_main_logo_inverted_white.png
+-rw-r--r--   0 runner    (1001) docker     (123)    63967 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/_static/molssi_square.png
+-rw-r--r--   0 runner    (1001) docker     (123)    32355 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/_static/nsf.png
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.376150 forcefield_step-2023.4.6/docs/api/
+-rw-r--r--   0 runner    (1001) docker     (123)      182 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/api/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/authors.rst
+-rwxr-xr-x   0 runner    (1001) docker     (123)     9604 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/conf.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.376150 forcefield_step-2023.4.6/docs/developer_guide/
+-rw-r--r--   0 runner    (1001) docker     (123)       36 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/developer_guide/contributing.rst
+-rw-r--r--   0 runner    (1001) docker     (123)      234 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/developer_guide/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1212 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/developer_guide/installation.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/developer_guide/readme.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       92 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/developer_guide/usage.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.376150 forcefield_step-2023.4.6/docs/getting_started/
+-rw-r--r--   0 runner    (1001) docker     (123)     1035 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/getting_started/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/history.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     1301 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/index.rst
+-rw-r--r--   0 runner    (1001) docker     (123)     6477 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/make.bat
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.376150 forcefield_step-2023.4.6/docs/user_guide/
+-rw-r--r--   0 runner    (1001) docker     (123)      240 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/docs/user_guide/index.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.384149 forcefield_step-2023.4.6/forcefield_step/
+-rw-r--r--   0 runner    (1001) docker     (123)      722 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/forcefield_step/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      500 2023-04-06 15:40:42.384149 forcefield_step-2023.4.6/forcefield_step/_version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.380149 forcefield_step-2023.4.6/forcefield_step/data/
+-rw-r--r--   0 runner    (1001) docker     (123)     3443 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/forcefield_step/data/lithium_battery.frc
+-rw-r--r--   0 runner    (1001) docker     (123)     7938 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/forcefield_step/data/nacl_water.frc
+-rw-r--r--   0 runner    (1001) docker     (123)   474898 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/forcefield_step/data/oplsaa.frc
+-rw-r--r--   0 runner    (1001) docker     (123)   361764 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/forcefield_step/data/pcff2018.frc
+-rw-r--r--   0 runner    (1001) docker     (123)     9974 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/forcefield_step/forcefield.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2888 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/forcefield_step/forcefield_parameters.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1208 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/forcefield_step/forcefield_step.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3955 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/forcefield_step/tk_forcefield.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.380149 forcefield_step-2023.4.6/forcefield_step.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     4284 2023-04-06 15:40:42.000000 forcefield_step-2023.4.6/forcefield_step.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1293 2023-04-06 15:40:42.000000 forcefield_step-2023.4.6/forcefield_step.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 15:40:42.000000 forcefield_step-2023.4.6/forcefield_step.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      130 2023-04-06 15:40:42.000000 forcefield_step-2023.4.6/forcefield_step.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       30 2023-04-06 15:40:42.000000 forcefield_step-2023.4.6/forcefield_step.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-06 15:40:42.000000 forcefield_step-2023.4.6/forcefield_step.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      375 2023-04-06 15:40:42.384149 forcefield_step-2023.4.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     2907 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 15:40:42.384149 forcefield_step-2023.4.6/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)       70 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1465 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/tests/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)      592 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/tests/test_forcefield_step.py
+-rw-r--r--   0 runner    (1001) docker     (123)   153001 2023-04-06 15:40:18.000000 forcefield_step-2023.4.6/tests/test_oplsaa_assignment.py
```

### Comparing `forcefield_step-2023.2.14/CONTRIBUTING.rst` & `forcefield_step-2023.4.6/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/HISTORY.rst` & `forcefield_step-2023.4.6/HISTORY.rst`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,14 @@
 =======
 History
 =======
 
+2023.4.6 -- Added Lithium battery forcefield
+  * An initial set of parameters for cathode materials, specifically LiCoO2.
+
 2023.2.13 -- Added OPLS-AA forcefield
   * Added parameters for OPLS-AA along with some extra parameters for ionic liquids
     * PF6-
     * ethylene carbonate (EC) and fluoronated EC (FEC)
   * Added atom-typing templates for most of OPLS-AA. Still missing a few and amino
     acids and DNA not yet tested.
   * Added extensive, almost-complete testing, for OPLS-AA
```

### Comparing `forcefield_step-2023.2.14/LICENSE` & `forcefield_step-2023.4.6/LICENSE`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/PKG-INFO` & `forcefield_step-2023.4.6/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: forcefield_step
-Version: 2023.2.14
+Version: 2023.4.6
 Summary: A SEAMM plug-in for setting up a forcefield or EAM potentials for subsequent simulations.
 Home-page: https://github.com/molssi-seam/forcefield_step
 Author: Paul Saxe
 Author-email: psaxe@molssi.org
 License: BSD-3-Clause
 Keywords: SEAMM,plug-in,flowchart,forcefield,EAM,OpenKIM
 Platform: Linux
@@ -83,14 +83,17 @@
 .. _`National Science Foundation`: https://www.nsf.gov
 
 
 =======
 History
 =======
 
+2023.4.6 -- Added Lithium battery forcefield
+  * An initial set of parameters for cathode materials, specifically LiCoO2.
+
 2023.2.13 -- Added OPLS-AA forcefield
   * Added parameters for OPLS-AA along with some extra parameters for ionic liquids
     * PF6-
     * ethylene carbonate (EC) and fluoronated EC (FEC)
   * Added atom-typing templates for most of OPLS-AA. Still missing a few and amino
     acids and DNA not yet tested.
   * Added extensive, almost-complete testing, for OPLS-AA
```

### Comparing `forcefield_step-2023.2.14/README.rst` & `forcefield_step-2023.4.6/README.rst`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/Makefile` & `forcefield_step-2023.4.6/docs/Makefile`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/_static/SEAMM inverted.png` & `forcefield_step-2023.4.6/docs/_static/SEAMM inverted.png`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/_static/SEAMM logo.png` & `forcefield_step-2023.4.6/docs/_static/SEAMM logo.png`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/_static/molssi_main_logo.png` & `forcefield_step-2023.4.6/docs/_static/molssi_main_logo.png`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/_static/molssi_main_logo_inverted_white.png` & `forcefield_step-2023.4.6/docs/_static/molssi_main_logo_inverted_white.png`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/_static/molssi_square.png` & `forcefield_step-2023.4.6/docs/_static/molssi_square.png`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/_static/nsf.png` & `forcefield_step-2023.4.6/docs/_static/nsf.png`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/conf.py` & `forcefield_step-2023.4.6/docs/conf.py`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/developer_guide/installation.rst` & `forcefield_step-2023.4.6/docs/developer_guide/installation.rst`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/getting_started/index.rst` & `forcefield_step-2023.4.6/docs/getting_started/index.rst`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/index.rst` & `forcefield_step-2023.4.6/docs/index.rst`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/docs/make.bat` & `forcefield_step-2023.4.6/docs/make.bat`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/forcefield_step/__init__.py` & `forcefield_step-2023.4.6/forcefield_step/__init__.py`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/forcefield_step/data/nacl_water.frc` & `forcefield_step-2023.4.6/forcefield_step/data/nacl_water.frc`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/forcefield_step/data/oplsaa.frc` & `forcefield_step-2023.4.6/forcefield_step/data/oplsaa.frc`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/forcefield_step/data/pcff2018.frc` & `forcefield_step-2023.4.6/forcefield_step/data/pcff2018.frc`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/forcefield_step/forcefield.py` & `forcefield_step-2023.4.6/forcefield_step/forcefield.py`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/forcefield_step/forcefield_parameters.py` & `forcefield_step-2023.4.6/forcefield_step/forcefield_parameters.py`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/forcefield_step/forcefield_step.py` & `forcefield_step-2023.4.6/forcefield_step/forcefield_step.py`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/forcefield_step/tk_forcefield.py` & `forcefield_step-2023.4.6/forcefield_step/tk_forcefield.py`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/forcefield_step.egg-info/PKG-INFO` & `forcefield_step-2023.4.6/forcefield_step.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: forcefield-step
-Version: 2023.2.14
+Version: 2023.4.6
 Summary: A SEAMM plug-in for setting up a forcefield or EAM potentials for subsequent simulations.
 Home-page: https://github.com/molssi-seam/forcefield_step
 Author: Paul Saxe
 Author-email: psaxe@molssi.org
 License: BSD-3-Clause
 Keywords: SEAMM,plug-in,flowchart,forcefield,EAM,OpenKIM
 Platform: Linux
@@ -83,14 +83,17 @@
 .. _`National Science Foundation`: https://www.nsf.gov
 
 
 =======
 History
 =======
 
+2023.4.6 -- Added Lithium battery forcefield
+  * An initial set of parameters for cathode materials, specifically LiCoO2.
+
 2023.2.13 -- Added OPLS-AA forcefield
   * Added parameters for OPLS-AA along with some extra parameters for ionic liquids
     * PF6-
     * ethylene carbonate (EC) and fluoronated EC (FEC)
   * Added atom-typing templates for most of OPLS-AA. Still missing a few and amino
     acids and DNA not yet tested.
   * Added extensive, almost-complete testing, for OPLS-AA
```

### Comparing `forcefield_step-2023.2.14/forcefield_step.egg-info/SOURCES.txt` & `forcefield_step-2023.4.6/forcefield_step.egg-info/SOURCES.txt`

 * *Files 5% similar despite different names*

```diff
@@ -34,14 +34,15 @@
 forcefield_step/tk_forcefield.py
 forcefield_step.egg-info/PKG-INFO
 forcefield_step.egg-info/SOURCES.txt
 forcefield_step.egg-info/dependency_links.txt
 forcefield_step.egg-info/entry_points.txt
 forcefield_step.egg-info/requires.txt
 forcefield_step.egg-info/top_level.txt
+forcefield_step/data/lithium_battery.frc
 forcefield_step/data/nacl_water.frc
 forcefield_step/data/oplsaa.frc
 forcefield_step/data/pcff2018.frc
 tests/__init__.py
 tests/conftest.py
 tests/test_forcefield_step.py
 tests/test_oplsaa_assignment.py
```

### Comparing `forcefield_step-2023.2.14/setup.py` & `forcefield_step-2023.4.6/setup.py`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/tests/conftest.py` & `forcefield_step-2023.4.6/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/tests/test_forcefield_step.py` & `forcefield_step-2023.4.6/tests/test_forcefield_step.py`

 * *Files identical despite different names*

### Comparing `forcefield_step-2023.2.14/tests/test_oplsaa_assignment.py` & `forcefield_step-2023.4.6/tests/test_oplsaa_assignment.py`

 * *Files identical despite different names*

