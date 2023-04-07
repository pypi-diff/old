# Comparing `tmp/biobrary-0.0.6.3.tar.gz` & `tmp/biobrary-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/fanghl/fanghl_dirtree/works/github/biobrary/dist/tmp90jqk4b1/biobrary-0.0.6.3.tar", last modified: Tue Dec 28 12:50:09 2021, max compression
+gzip compressed data, was "biobrary-0.1.1.tar", last modified: Fri Apr  7 12:46:29 2023, max compression
```

## Comparing `biobrary-0.0.6.3.tar` & `biobrary-0.1.1.tar`

### file list

```diff
@@ -1,20 +1,27 @@
-drwxrwxr-x   0 fanghl    (1000) fanghl    (1000)        0 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)     1070 2021-10-14 11:11:21.000000 biobrary-0.0.6.3/LICENSE
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)     1184 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/PKG-INFO
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)      845 2021-12-25 10:53:41.000000 biobrary-0.0.6.3/README.md
-drwxrwxr-x   0 fanghl    (1000) fanghl    (1000)        0 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/biobrary/
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)    10708 2021-12-28 12:47:29.000000 biobrary-0.0.6.3/biobrary/CircleNode.py
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)      213 2021-10-15 07:12:55.000000 biobrary-0.0.6.3/biobrary/__init__.py
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)      324 2021-10-15 07:12:55.000000 biobrary-0.0.6.3/biobrary/amino_acids_mw.py
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)     1051 2021-10-15 07:12:55.000000 biobrary-0.0.6.3/biobrary/biocodon.py
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)    19985 2021-10-15 07:12:55.000000 biobrary-0.0.6.3/biobrary/bioparser.py
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)    14178 2021-10-15 07:12:55.000000 biobrary-0.0.6.3/biobrary/score_matrix.py
-drwxrwxr-x   0 fanghl    (1000) fanghl    (1000)        0 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/biobrary.egg-info/
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)     1184 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/biobrary.egg-info/PKG-INFO
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)      349 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/biobrary.egg-info/SOURCES.txt
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)        1 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/biobrary.egg-info/dependency_links.txt
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)       26 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/biobrary.egg-info/requires.txt
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)        9 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/biobrary.egg-info/top_level.txt
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)       48 2021-10-15 07:12:55.000000 biobrary-0.0.6.3/pyproject.toml
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)      449 2021-12-28 12:50:09.000000 biobrary-0.0.6.3/setup.cfg
--rw-rw-r--   0 fanghl    (1000) fanghl    (1000)       39 2021-10-15 07:12:55.000000 biobrary-0.0.6.3/setup.py
+drwxr-xr-x   0 fanghl    (1000) fanghl    (1000)        0 2023-04-07 12:46:28.998445 biobrary-0.1.1/
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)     1070 2023-04-07 06:30:35.000000 biobrary-0.1.1/LICENSE
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)     1354 2023-04-07 12:46:28.998445 biobrary-0.1.1/PKG-INFO
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)      942 2023-04-07 06:30:35.000000 biobrary-0.1.1/README.md
+drwxr-xr-x   0 fanghl    (1000) fanghl    (1000)        0 2023-04-07 12:46:28.996445 biobrary-0.1.1/biobrary/
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)      140 2023-04-07 07:16:13.000000 biobrary-0.1.1/biobrary/__init__.py
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)      324 2023-04-07 06:30:35.000000 biobrary-0.1.1/biobrary/amino_acids_mw.py
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)     1051 2023-04-07 06:30:35.000000 biobrary-0.1.1/biobrary/biocodon.py
+drwxr-xr-x   0 fanghl    (1000) fanghl    (1000)        0 2023-04-07 12:46:28.997445 biobrary-0.1.1/biobrary/bioparse/
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)      104 2023-04-07 07:04:13.000000 biobrary-0.1.1/biobrary/bioparse/__init__.py
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)    12457 2023-04-07 07:03:30.000000 biobrary-0.1.1/biobrary/bioparse/blast_parse.py
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)     1438 2023-04-07 06:41:04.000000 biobrary-0.1.1/biobrary/bioparse/fasta_parse.py
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)       27 2023-04-07 07:02:32.000000 biobrary-0.1.1/biobrary/bioparse/gbk_parse.py
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)     2261 2023-04-07 07:01:51.000000 biobrary-0.1.1/biobrary/bioparse/gff_parse.py
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)    14178 2023-04-07 06:30:35.000000 biobrary-0.1.1/biobrary/score_matrix.py
+drwxr-xr-x   0 fanghl    (1000) fanghl    (1000)        0 2023-04-07 12:46:28.998445 biobrary-0.1.1/biobrary/tree/
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)    10708 2023-04-07 06:30:35.000000 biobrary-0.1.1/biobrary/tree/CircleNode.py
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)        0 2023-04-07 07:13:44.000000 biobrary-0.1.1/biobrary/tree/__init__.py
+drwxr-xr-x   0 fanghl    (1000) fanghl    (1000)        0 2023-04-07 12:46:28.997445 biobrary-0.1.1/biobrary.egg-info/
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)     1354 2023-04-07 12:46:28.000000 biobrary-0.1.1/biobrary.egg-info/PKG-INFO
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)      516 2023-04-07 12:46:28.000000 biobrary-0.1.1/biobrary.egg-info/SOURCES.txt
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)        1 2023-04-07 12:46:28.000000 biobrary-0.1.1/biobrary.egg-info/dependency_links.txt
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)       38 2023-04-07 12:46:28.000000 biobrary-0.1.1/biobrary.egg-info/requires.txt
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)        9 2023-04-07 12:46:28.000000 biobrary-0.1.1/biobrary.egg-info/top_level.txt
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)      551 2023-04-07 12:44:00.000000 biobrary-0.1.1/pyproject.toml
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)      235 2023-04-07 12:46:28.999445 biobrary-0.1.1/setup.cfg
+-rw-r--r--   0 fanghl    (1000) fanghl    (1000)       68 2023-04-07 08:42:11.000000 biobrary-0.1.1/setup.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `biobrary-0.0.6.3/LICENSE` & `biobrary-0.1.1/LICENSE`

 * *Files identical despite different names*

### Comparing `biobrary-0.0.6.3/PKG-INFO` & `biobrary-0.1.1/README.md`

 * *Files 15% similar despite different names*

```diff
@@ -1,25 +1,17 @@
-Metadata-Version: 2.1
-Name: biobrary
-Version: 0.0.6.3
-Summary: A library for biological computing works
-Home-page: https://github.com/benjaminfang/biobrary
-Author: Benjamin Fang
-Author-email: benjaminfang.ol@outlook.com
-License: MIT
-Platform: UNKNOWN
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-License-File: LICENSE
-
 # Biobrary
 
 ## Introduction
 Biobrary is a python library, which contain data and methods for biological computation.
 
+## Requirement  
+* ete3
+    pyqt5 is needed by ete3. you maybe need install it manually.
+ 
+
 ## Install  
 * using pip  
 `pip install biobrary --user`
 
 * manally install  
 `git clone https://github.com/benjaminfang/biobrary.git`  
 `cd biobrary`  
@@ -53,9 +45,8 @@
 * amino_acids_mw  
 
 
 
 * CircleNode  
     class for phylogenic tree traverse and operations. And divide tree to circle node according
     to phylogenic distance.
-
-
+
```

### Comparing `biobrary-0.0.6.3/biobrary/CircleNode.py` & `biobrary-0.1.1/biobrary/tree/CircleNode.py`

 * *Files identical despite different names*

### Comparing `biobrary-0.0.6.3/biobrary/biocodon.py` & `biobrary-0.1.1/biobrary/biocodon.py`

 * *Files identical despite different names*

### Comparing `biobrary-0.0.6.3/biobrary/score_matrix.py` & `biobrary-0.1.1/biobrary/score_matrix.py`

 * *Files identical despite different names*

### Comparing `biobrary-0.0.6.3/biobrary.egg-info/PKG-INFO` & `biobrary-0.1.1/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,25 +1,30 @@
 Metadata-Version: 2.1
 Name: biobrary
-Version: 0.0.6.3
+Version: 0.1.1
 Summary: A library for biological computing works
-Home-page: https://github.com/benjaminfang/biobrary
-Author: Benjamin Fang
-Author-email: benjaminfang.ol@outlook.com
-License: MIT
-Platform: UNKNOWN
-Requires-Python: >=3.7
+Author-email: Benjamin Fang <benjaminfang.ol@outlook.com>
+License: MIT License
+Project-URL: Homepage, https://github.com/benjaminfang/biobrary
+Keywords: biobrary,bioparse,tree
+Classifier: Programming Language :: Python :: 3
+Requires-Python: >=3.6
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # Biobrary
 
 ## Introduction
 Biobrary is a python library, which contain data and methods for biological computation.
 
+## Requirement  
+* ete3
+    pyqt5 is needed by ete3. you maybe need install it manually.
+ 
+
 ## Install  
 * using pip  
 `pip install biobrary --user`
 
 * manally install  
 `git clone https://github.com/benjaminfang/biobrary.git`  
 `cd biobrary`  
@@ -53,9 +58,8 @@
 * amino_acids_mw  
 
 
 
 * CircleNode  
     class for phylogenic tree traverse and operations. And divide tree to circle node according
     to phylogenic distance.
-
-
+
```

