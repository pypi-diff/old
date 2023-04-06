# Comparing `tmp/gget-0.3.8.tar.gz` & `tmp/gget-0.3.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gget-0.3.8.tar", last modified: Fri Aug 12 19:30:39 2022, max compression
+gzip compressed data, was "gget-0.3.9.tar", last modified: Thu Aug 25 08:36:56 2022, max compression
```

## Comparing `gget-0.3.8.tar` & `gget-0.3.9.tar`

### file list

```diff
@@ -1,50 +1,50 @@
-drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-12 19:30:39.656979 gget-0.3.8/
--rw-r--r--   0 lauraluebbert   (501) staff       (20)     1341 2022-08-12 19:29:53.000000 gget-0.3.8/LICENSE
--rw-r--r--   0 lauraluebbert   (501) staff       (20)       70 2022-08-12 19:29:53.000000 gget-0.3.8/MANIFEST.in
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    35795 2022-08-12 19:30:39.657232 gget-0.3.8/PKG-INFO
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    34954 2022-08-12 19:29:53.000000 gget-0.3.8/README.md
-drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-12 19:30:39.624772 gget-0.3.8/gget/
--rw-r--r--   0 lauraluebbert   (501) staff       (20)      645 2022-08-12 19:29:53.000000 gget-0.3.8/gget/__init__.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)       31 2022-08-12 19:29:53.000000 gget-0.3.8/gget/__main__.py
-drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-12 19:30:39.614459 gget-0.3.8/gget/bins/
-drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-12 19:30:39.633221 gget-0.3.8/gget/bins/Darwin/
--rwxr-xr-x   0 lauraluebbert   (501) staff       (20)  1096232 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/Darwin/jackhmmer
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    35149 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/Darwin/license.txt
--rwxr-xr-x   0 lauraluebbert   (501) staff       (20)  1024744 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/Darwin/muscle
-drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-12 19:30:39.645779 gget-0.3.8/gget/bins/Linux/
--rwxr-xr-x   0 lauraluebbert   (501) staff       (20)   897984 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/Linux/jackhmmer
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    35149 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/Linux/license.txt
--rwxr-xr-x   0 lauraluebbert   (501) staff       (20)   859512 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/Linux/muscle
-drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-12 19:30:39.651035 gget-0.3.8/gget/bins/Windows/
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    35149 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/Windows/license.txt
--rw-r--r--   0 lauraluebbert   (501) staff       (20)   832512 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/Windows/muscle.win64.exe
-drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-12 19:30:39.656400 gget-0.3.8/gget/bins/alphafold/
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    11358 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/alphafold/LICENSE
--rw-r--r--   0 lauraluebbert   (501) staff       (20)     1129 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/alphafold/NOTICE
--rw-r--r--   0 lauraluebbert   (501) staff       (20)     9119 2022-08-12 19:29:53.000000 gget-0.3.8/gget/bins/alphafold/stereo_chemical_props.txt
--rw-r--r--   0 lauraluebbert   (501) staff       (20)     2968 2022-08-12 19:29:53.000000 gget-0.3.8/gget/compile.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)      947 2022-08-12 19:29:53.000000 gget-0.3.8/gget/constants.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    29106 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_alphafold.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)     7708 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_archs4.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    14808 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_blast.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)     9050 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_blat.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    12149 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_enrichr.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    21382 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_info.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)     6557 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_muscle.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    18000 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_ref.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    10803 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_search.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    16330 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_seq.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    13735 2022-08-12 19:29:53.000000 gget-0.3.8/gget/gget_setup.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    50149 2022-08-12 19:29:53.000000 gget-0.3.8/gget/main.py
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    20233 2022-08-12 19:29:53.000000 gget-0.3.8/gget/utils.py
-drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-12 19:30:39.626908 gget-0.3.8/gget.egg-info/
--rw-r--r--   0 lauraluebbert   (501) staff       (20)    35795 2022-08-12 19:30:38.000000 gget-0.3.8/gget.egg-info/PKG-INFO
--rw-r--r--   0 lauraluebbert   (501) staff       (20)      892 2022-08-12 19:30:39.000000 gget-0.3.8/gget.egg-info/SOURCES.txt
--rw-r--r--   0 lauraluebbert   (501) staff       (20)        1 2022-08-12 19:30:38.000000 gget-0.3.8/gget.egg-info/dependency_links.txt
--rw-r--r--   0 lauraluebbert   (501) staff       (20)       40 2022-08-12 19:30:39.000000 gget-0.3.8/gget.egg-info/entry_points.txt
--rw-r--r--   0 lauraluebbert   (501) staff       (20)        1 2022-08-12 19:30:38.000000 gget-0.3.8/gget.egg-info/not-zip-safe
--rw-r--r--   0 lauraluebbert   (501) staff       (20)      157 2022-08-12 19:30:39.000000 gget-0.3.8/gget.egg-info/requires.txt
--rw-r--r--   0 lauraluebbert   (501) staff       (20)        5 2022-08-12 19:30:39.000000 gget-0.3.8/gget.egg-info/top_level.txt
--rw-r--r--   0 lauraluebbert   (501) staff       (20)      157 2022-08-12 19:29:53.000000 gget-0.3.8/requirements.txt
--rw-r--r--   0 lauraluebbert   (501) staff       (20)      107 2022-08-12 19:30:39.657809 gget-0.3.8/setup.cfg
--rw-r--r--   0 lauraluebbert   (501) staff       (20)     1442 2022-08-12 19:29:53.000000 gget-0.3.8/setup.py
+drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-25 08:36:56.059022 gget-0.3.9/
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)     1341 2022-08-12 19:29:53.000000 gget-0.3.9/LICENSE
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)       70 2022-08-12 19:29:53.000000 gget-0.3.9/MANIFEST.in
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    35717 2022-08-25 08:36:56.059401 gget-0.3.9/PKG-INFO
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    34896 2022-08-19 19:08:20.000000 gget-0.3.9/README.md
+drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-25 08:36:56.022679 gget-0.3.9/gget/
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)      645 2022-08-25 08:19:32.000000 gget-0.3.9/gget/__init__.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)       31 2022-08-12 19:29:53.000000 gget-0.3.9/gget/__main__.py
+drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-25 08:36:56.006678 gget-0.3.9/gget/bins/
+drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-25 08:36:56.032810 gget-0.3.9/gget/bins/Darwin/
+-rwxr-xr-x   0 lauraluebbert   (501) staff       (20)  1096232 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/Darwin/jackhmmer
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    35149 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/Darwin/license.txt
+-rwxr-xr-x   0 lauraluebbert   (501) staff       (20)  1024744 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/Darwin/muscle
+drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-25 08:36:56.046215 gget-0.3.9/gget/bins/Linux/
+-rwxr-xr-x   0 lauraluebbert   (501) staff       (20)   897984 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/Linux/jackhmmer
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    35149 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/Linux/license.txt
+-rwxr-xr-x   0 lauraluebbert   (501) staff       (20)   859512 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/Linux/muscle
+drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-25 08:36:56.051973 gget-0.3.9/gget/bins/Windows/
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    35149 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/Windows/license.txt
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)   832512 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/Windows/muscle.win64.exe
+drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-25 08:36:56.058223 gget-0.3.9/gget/bins/alphafold/
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    11358 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/alphafold/LICENSE
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)     1129 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/alphafold/NOTICE
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)     9119 2022-08-12 19:29:53.000000 gget-0.3.9/gget/bins/alphafold/stereo_chemical_props.txt
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)     2968 2022-08-12 19:29:53.000000 gget-0.3.9/gget/compile.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)      947 2022-08-12 19:29:53.000000 gget-0.3.9/gget/constants.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    29716 2022-08-25 08:18:57.000000 gget-0.3.9/gget/gget_alphafold.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)     7708 2022-08-12 19:29:53.000000 gget-0.3.9/gget/gget_archs4.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    14808 2022-08-12 19:29:53.000000 gget-0.3.9/gget/gget_blast.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)     9050 2022-08-12 19:29:53.000000 gget-0.3.9/gget/gget_blat.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    12149 2022-08-12 19:29:53.000000 gget-0.3.9/gget/gget_enrichr.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    21382 2022-08-12 19:29:53.000000 gget-0.3.9/gget/gget_info.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)     6557 2022-08-12 19:29:53.000000 gget-0.3.9/gget/gget_muscle.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    18000 2022-08-12 19:29:53.000000 gget-0.3.9/gget/gget_ref.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    10803 2022-08-12 19:29:53.000000 gget-0.3.9/gget/gget_search.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    16317 2022-08-15 19:25:12.000000 gget-0.3.9/gget/gget_seq.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    13899 2022-08-25 08:19:11.000000 gget-0.3.9/gget/gget_setup.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    50149 2022-08-12 19:29:53.000000 gget-0.3.9/gget/main.py
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    20233 2022-08-12 19:29:53.000000 gget-0.3.9/gget/utils.py
+drwxr-xr-x   0 lauraluebbert   (501) staff       (20)        0 2022-08-25 08:36:56.025852 gget-0.3.9/gget.egg-info/
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)    35717 2022-08-25 08:36:55.000000 gget-0.3.9/gget.egg-info/PKG-INFO
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)      892 2022-08-25 08:36:55.000000 gget-0.3.9/gget.egg-info/SOURCES.txt
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)        1 2022-08-25 08:36:55.000000 gget-0.3.9/gget.egg-info/dependency_links.txt
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)       40 2022-08-25 08:36:55.000000 gget-0.3.9/gget.egg-info/entry_points.txt
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)        1 2022-08-25 08:36:55.000000 gget-0.3.9/gget.egg-info/not-zip-safe
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)      157 2022-08-25 08:36:55.000000 gget-0.3.9/gget.egg-info/requires.txt
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)        5 2022-08-25 08:36:55.000000 gget-0.3.9/gget.egg-info/top_level.txt
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)      157 2022-08-12 19:29:53.000000 gget-0.3.9/requirements.txt
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)      107 2022-08-25 08:36:56.060363 gget-0.3.9/setup.cfg
+-rw-r--r--   0 lauraluebbert   (501) staff       (20)     1442 2022-08-12 19:29:53.000000 gget-0.3.9/setup.py
```

### Comparing `gget-0.3.8/LICENSE` & `gget-0.3.9/LICENSE`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/PKG-INFO` & `gget-0.3.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,35 +1,34 @@
 Metadata-Version: 2.1
 Name: gget
-Version: 0.3.8
+Version: 0.3.9
 Summary: Efficient querying of genomic databases directly into programming environments.
 Home-page: https://github.com/pachterlab/gget
 Author: Laura Luebbert
 Author-email: lauraluebbert@caltech.edu
 Maintainer: Laura Luebbert
 Maintainer-email: lauraluebbert@caltech.edu
 License: BSD-2
 Keywords: gget
-Platform: UNKNOWN
 Classifier: Environment :: Console
 Classifier: Framework :: Jupyter
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Topic :: Scientific/Engineering :: Bio-Informatics
 Classifier: Topic :: Utilities
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 
 # gget
 [![pypi version](https://img.shields.io/pypi/v/gget)](https://pypi.org/project/gget)
+[![image](https://anaconda.org/bioconda/gget/badges/version.svg)](https://anaconda.org/bioconda/gget)
 [![Downloads](https://pepy.tech/badge/gget)](https://pepy.tech/project/gget)
-[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/gget/README.html)
 [![license](https://img.shields.io/pypi/l/gget)](LICENSE)
 ![status](https://github.com/pachterlab/gget/workflows/CI/badge.svg)
 ![Code Coverage](https://img.shields.io/badge/Coverage-83%25-green.svg)  
 
 ## ✨ Version ≥ 0.3.0: [`gget alphafold`](#gget-alphafold-) 
 
 ## ✨ What's new in version ≥ 0.2.0
@@ -759,9 +758,7 @@
   
   And, if applicable:  
   Evans, R. et al. Protein complex prediction with AlphaFold-Multimer. bioRxiv 2021.10.04.463034; https://doi.org/10.1101/2021.10.04.463034
   
 ___
 # Disclaimer  
 `gget` is only as accurate as the databases/servers/APIs it queries from. The accuracy or reliability of the data is not guaranteed or warranted in any way and the providers disclaim liability of any kind whatsoever, including, without limitation, liability for quality, performance, merchantability and fitness for a particular purpose arising out of the use, or inability to use the data.
-
-
```

### Comparing `gget-0.3.8/README.md` & `gget-0.3.9/gget.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,34 @@
+Metadata-Version: 2.1
+Name: gget
+Version: 0.3.9
+Summary: Efficient querying of genomic databases directly into programming environments.
+Home-page: https://github.com/pachterlab/gget
+Author: Laura Luebbert
+Author-email: lauraluebbert@caltech.edu
+Maintainer: Laura Luebbert
+Maintainer-email: lauraluebbert@caltech.edu
+License: BSD-2
+Keywords: gget
+Classifier: Environment :: Console
+Classifier: Framework :: Jupyter
+Classifier: Intended Audience :: Science/Research
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Classifier: Programming Language :: Python :: 3.7
+Classifier: Programming Language :: Python :: 3.8
+Classifier: Topic :: Scientific/Engineering :: Bio-Informatics
+Classifier: Topic :: Utilities
+Requires-Python: >=3.6
+Description-Content-Type: text/markdown
+
 # gget
 [![pypi version](https://img.shields.io/pypi/v/gget)](https://pypi.org/project/gget)
+[![image](https://anaconda.org/bioconda/gget/badges/version.svg)](https://anaconda.org/bioconda/gget)
 [![Downloads](https://pepy.tech/badge/gget)](https://pepy.tech/project/gget)
-[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/gget/README.html)
 [![license](https://img.shields.io/pypi/l/gget)](LICENSE)
 ![status](https://github.com/pachterlab/gget/workflows/CI/badge.svg)
 ![Code Coverage](https://img.shields.io/badge/Coverage-83%25-green.svg)  
 
 ## ✨ Version ≥ 0.3.0: [`gget alphafold`](#gget-alphafold-) 
 
 ## ✨ What's new in version ≥ 0.2.0
```

### Comparing `gget-0.3.8/gget/__init__.py` & `gget-0.3.9/gget/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,10 +15,10 @@
     format="%(asctime)s %(levelname)s %(message)s",
     level=logging.INFO,
     datefmt="%c",
 )
 # Mute numexpr threads info
 logging.getLogger("numexpr").setLevel(logging.WARNING)
 
-__version__ = "0.3.8"
+__version__ = "0.3.9"
 __author__ = "Laura Luebbert"
 __email__ = "lauraluebbert@caltech.edu"
```

### Comparing `gget-0.3.8/gget/bins/Darwin/jackhmmer` & `gget-0.3.9/gget/bins/Darwin/jackhmmer`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/Darwin/license.txt` & `gget-0.3.9/gget/bins/Darwin/license.txt`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/Darwin/muscle` & `gget-0.3.9/gget/bins/Darwin/muscle`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/Linux/jackhmmer` & `gget-0.3.9/gget/bins/Linux/jackhmmer`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/Linux/license.txt` & `gget-0.3.9/gget/bins/Linux/license.txt`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/Linux/muscle` & `gget-0.3.9/gget/bins/Linux/muscle`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/Windows/license.txt` & `gget-0.3.9/gget/bins/Windows/license.txt`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/Windows/muscle.win64.exe` & `gget-0.3.9/gget/bins/Windows/muscle.win64.exe`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/alphafold/LICENSE` & `gget-0.3.9/gget/bins/alphafold/LICENSE`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/alphafold/NOTICE` & `gget-0.3.9/gget/bins/alphafold/NOTICE`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/bins/alphafold/stereo_chemical_props.txt` & `gget-0.3.9/gget/bins/alphafold/stereo_chemical_props.txt`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/compile.py` & `gget-0.3.9/gget/compile.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/constants.py` & `gget-0.3.9/gget/constants.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/gget_alphafold.py` & `gget-0.3.9/gget/gget_alphafold.py`

 * *Files 6% similar despite different names*

```diff
@@ -227,16 +227,17 @@
     ## Check if third-party dependencies are installed
     # Check if openmm is installed
     try:
         import simtk.openmm as openmm
     except ImportError:
         logging.error(
             """
-        Please install third-party dependency openmm v7.5.1 by running the following command from the command line:
-        'conda install -c conda-forge openmm=7.5.1'
+        Please install AlphaFold third-party dependency openmm v7.5.1 by running the following command from the command line: 
+        'conda install -qy conda==4.13.0 && conda install -qy -c conda-forge openmm=7.5.1' 
+        (Recommendation: Follow with 'conda update -qy conda' to update conda to the latest version afterwards.)
         """
         )
         return
 
     # Check if AlphaFold is installed
     try:
         import alphafold as AlphaFold
@@ -296,26 +297,34 @@
     from alphafold.common import protein
 
     try:
         from alphafold.relax import utils
     except ModuleNotFoundError as e:
         if "openmm" in str(e):
             logging.error(
-                "Dependency openmm v7.5.1 not installed succesfully. Try running 'conda install -c conda-forge openmm=7.5.1' from the command line."
+                """
+                Dependency openmm v7.5.1 not installed succesfully. 
+                Try running 'conda install -qy conda==4.13.0 && conda install -qy -c conda-forge openmm=7.5.1' from the command line.
+                (Recommendation: Follow with 'conda update -qy conda' to update conda to the latest version afterwards.)
+                """
             )
             return
 
     if relax:
         # Import AlphaFold relax package
         try:
             from alphafold.relax import relax as run_relax
         except ModuleNotFoundError as e:
             if "openmm" in str(e):
                 logging.error(
-                    "Dependency openmm v7.5.1 not installed succesfully. Try running 'conda install -c conda-forge openmm=7.5.1' from the command line."
+                    """
+                    Dependency openmm v7.5.1 not installed succesfully. 
+                    Try running 'conda install -qy conda==4.13.0 && conda install -qy -c conda-forge openmm=7.5.1' from the command line.
+                    (Recommendation: Follow with 'conda update -qy conda' to update conda to the latest version afterwards.)
+                    """
                 )
                 return
 
     ## Move stereo_chemical_props.txt from gget bins to Alphafold package so it can be found
     # logging.info("Locate files containing stereochemical properties.")
     ALPHAFOLD_PATH = os.path.abspath(os.path.dirname(AlphaFold.__file__))
     os.makedirs(os.path.join(ALPHAFOLD_PATH, "common/"), exist_ok=True)
```

### Comparing `gget-0.3.8/gget/gget_archs4.py` & `gget-0.3.9/gget/gget_archs4.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/gget_blast.py` & `gget-0.3.9/gget/gget_blast.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/gget_blat.py` & `gget-0.3.9/gget/gget_blat.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/gget_enrichr.py` & `gget-0.3.9/gget/gget_enrichr.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/gget_info.py` & `gget-0.3.9/gget/gget_info.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/gget_muscle.py` & `gget-0.3.9/gget/gget_muscle.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/gget_ref.py` & `gget-0.3.9/gget/gget_ref.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/gget_search.py` & `gget-0.3.9/gget/gget_search.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/gget_seq.py` & `gget-0.3.9/gget/gget_seq.py`

 * *Files 1% similar despite different names*

```diff
@@ -117,27 +117,26 @@
 
                     logging.info(
                         f"Requesting nucleotide sequence of {ensembl_ID} from Ensembl."
                     )
 
                 except RuntimeError:
                     logging.error(
-                        f"ID {ensembl_ID} not found. "
-                        "Please double-check spelling/arguments and try again."
+                        f"ID {ensembl_ID} not found. Please double-check spelling/arguments and try again."
                     )
 
             # If isoforms true, fetch sequences of isoforms instead
             if isoforms == True:
                 # Get ID type (gene, transcript, ...) using gget info
                 info_df = info(ensembl_ID, verbose=False)
 
                 # Check if Ensembl ID was found
                 if isinstance(info_df, type(None)):
                     logging.warning(
-                        f"ID '{ensembl_ID}' not found. Please double-check spelling/arguments."
+                        f"ID '{ensembl_ID}' not found. Please double-check spelling/arguments and try again."
                     )
                     continue
 
                 ens_ID_type = info_df.loc[ensembl_ID]["object_type"]
 
                 # If the ID is a gene, get the IDs of all its transcripts
                 if ens_ID_type == "Gene":
```

### Comparing `gget-0.3.8/gget/gget_setup.py` & `gget-0.3.9/gget/gget_setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -98,16 +98,17 @@
                 raise ImportError()
 
             logging.info(f"openmm v{openmm.__version__} already installed.")
 
         except ImportError:
             logging.error(
                 """
-        Please install third-party dependency openmm v7.5.1 by running the following command from the command line:
-        'conda install -c conda-forge openmm=7.5.1'
+        Please install AlphaFold third-party dependency openmm v7.5.1 by running the following command from the command line: 
+        'conda install -qy conda==4.13.0 && conda install -qy -c conda-forge openmm=7.5.1' 
+        (Recommendation: Follow with 'conda update -qy conda' to update conda to the latest version afterwards.)
         """
             )
             return
 
         ## Install Alphafold if not already installed
         logging.info("Installing AlphaFold from source (requires pip and git).")
         # Install AlphaFold and apply OpenMM patch.
```

### Comparing `gget-0.3.8/gget/main.py` & `gget-0.3.9/gget/main.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget/utils.py` & `gget-0.3.9/gget/utils.py`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/gget.egg-info/PKG-INFO` & `gget-0.3.9/README.md`

 * *Files 2% similar despite different names*

```diff
@@ -1,35 +1,11 @@
-Metadata-Version: 2.1
-Name: gget
-Version: 0.3.8
-Summary: Efficient querying of genomic databases directly into programming environments.
-Home-page: https://github.com/pachterlab/gget
-Author: Laura Luebbert
-Author-email: lauraluebbert@caltech.edu
-Maintainer: Laura Luebbert
-Maintainer-email: lauraluebbert@caltech.edu
-License: BSD-2
-Keywords: gget
-Platform: UNKNOWN
-Classifier: Environment :: Console
-Classifier: Framework :: Jupyter
-Classifier: Intended Audience :: Science/Research
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: OS Independent
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Topic :: Scientific/Engineering :: Bio-Informatics
-Classifier: Topic :: Utilities
-Requires-Python: >=3.6
-Description-Content-Type: text/markdown
-
 # gget
 [![pypi version](https://img.shields.io/pypi/v/gget)](https://pypi.org/project/gget)
+[![image](https://anaconda.org/bioconda/gget/badges/version.svg)](https://anaconda.org/bioconda/gget)
 [![Downloads](https://pepy.tech/badge/gget)](https://pepy.tech/project/gget)
-[![install with bioconda](https://img.shields.io/badge/install%20with-bioconda-brightgreen.svg?style=flat)](http://bioconda.github.io/recipes/gget/README.html)
 [![license](https://img.shields.io/pypi/l/gget)](LICENSE)
 ![status](https://github.com/pachterlab/gget/workflows/CI/badge.svg)
 ![Code Coverage](https://img.shields.io/badge/Coverage-83%25-green.svg)  
 
 ## ✨ Version ≥ 0.3.0: [`gget alphafold`](#gget-alphafold-) 
 
 ## ✨ What's new in version ≥ 0.2.0
@@ -759,9 +735,7 @@
   
   And, if applicable:  
   Evans, R. et al. Protein complex prediction with AlphaFold-Multimer. bioRxiv 2021.10.04.463034; https://doi.org/10.1101/2021.10.04.463034
   
 ___
 # Disclaimer  
 `gget` is only as accurate as the databases/servers/APIs it queries from. The accuracy or reliability of the data is not guaranteed or warranted in any way and the providers disclaim liability of any kind whatsoever, including, without limitation, liability for quality, performance, merchantability and fitness for a particular purpose arising out of the use, or inability to use the data.
-
-
```

### Comparing `gget-0.3.8/gget.egg-info/SOURCES.txt` & `gget-0.3.9/gget.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gget-0.3.8/setup.py` & `gget-0.3.9/setup.py`

 * *Files identical despite different names*

