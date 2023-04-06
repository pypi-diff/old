# Comparing `tmp/sprint2-0.0.14.tar.gz` & `tmp/sprint2-0.0.15.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sprint2-0.0.14.tar", last modified: Thu Apr  6 17:42:09 2023, max compression
+gzip compressed data, was "sprint2-0.0.15.tar", last modified: Thu Apr  6 17:45:21 2023, max compression
```

## Comparing `sprint2-0.0.14.tar` & `sprint2-0.0.15.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:42:14.245825 sprint2-0.0.14/
-drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:42:14.090839 sprint2-0.0.14/MaskAGref/
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     6734 2023-04-06 17:42:00.000000 sprint2-0.0.14/MaskAGref/MaskAGref.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)       24 2023-04-06 17:42:00.000000 sprint2-0.0.14/MaskAGref/__init__.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)      621 2023-04-06 17:42:14.243825 sprint2-0.0.14/PKG-INFO
-drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:42:14.144834 sprint2-0.0.14/getDsRNA/
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     1919 2023-04-06 17:41:56.000000 sprint2-0.0.14/getDsRNA/__init__.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     9507 2023-04-06 17:41:55.000000 sprint2-0.0.14/getDsRNA/step1_transcript_blat.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     9760 2023-04-06 17:41:55.000000 sprint2-0.0.14/getDsRNA/step2_transcript_dspair.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     3162 2023-04-06 17:41:55.000000 sprint2-0.0.14/getDsRNA/step3_bedtools_sorted_rmLC.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     6742 2023-04-06 17:41:55.000000 sprint2-0.0.14/getDsRNA/step4_combine_by_chr.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     5750 2023-04-06 17:41:56.000000 sprint2-0.0.14/getDsRNA/step5_merge_dsRNA.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     2408 2023-04-06 17:41:56.000000 sprint2-0.0.14/getDsRNA/step6_dsRNA.py
-drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:42:14.200829 sprint2-0.0.14/getRES/
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     2034 2023-04-06 17:41:58.000000 sprint2-0.0.14/getRES/__init__.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)    45388 2023-04-06 17:41:58.000000 sprint2-0.0.14/getRES/step1_SNVcalling.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)    20538 2023-04-06 17:41:58.000000 sprint2-0.0.14/getRES/step2_annotation_based.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)    19408 2023-04-06 17:41:58.000000 sprint2-0.0.14/getRES/step3_dsRNA_based.py
--rw-rw-r--   0 xyx       (1003) xyx       (1003)       38 2023-04-06 17:42:14.247825 sprint2-0.0.14/setup.cfg
--rw-rw-r--   0 xyx       (1003) xyx       (1003)     1096 2023-04-06 17:42:03.000000 sprint2-0.0.14/setup.py
-drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:42:14.236826 sprint2-0.0.14/sprint2.egg-info/
--rw-rw-r--   0 xyx       (1003) xyx       (1003)      621 2023-04-06 17:42:13.000000 sprint2-0.0.14/sprint2.egg-info/PKG-INFO
--rw-rw-r--   0 xyx       (1003) xyx       (1003)      565 2023-04-06 17:42:13.000000 sprint2-0.0.14/sprint2.egg-info/SOURCES.txt
--rw-rw-r--   0 xyx       (1003) xyx       (1003)        1 2023-04-06 17:42:13.000000 sprint2-0.0.14/sprint2.egg-info/dependency_links.txt
--rw-rw-r--   0 xyx       (1003) xyx       (1003)       90 2023-04-06 17:42:13.000000 sprint2-0.0.14/sprint2.egg-info/entry_points.txt
--rw-rw-r--   0 xyx       (1003) xyx       (1003)        9 2023-04-06 17:42:13.000000 sprint2-0.0.14/sprint2.egg-info/requires.txt
--rw-rw-r--   0 xyx       (1003) xyx       (1003)       26 2023-04-06 17:42:13.000000 sprint2-0.0.14/sprint2.egg-info/top_level.txt
+drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:45:26.719216 sprint2-0.0.15/
+drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:45:26.591228 sprint2-0.0.15/MaskAGref/
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     6734 2023-04-06 17:45:12.000000 sprint2-0.0.15/MaskAGref/MaskAGref.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)       24 2023-04-06 17:45:12.000000 sprint2-0.0.15/MaskAGref/__init__.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)      621 2023-04-06 17:45:26.716217 sprint2-0.0.15/PKG-INFO
+drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:45:26.638224 sprint2-0.0.15/getDsRNA/
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     1919 2023-04-06 17:45:16.000000 sprint2-0.0.15/getDsRNA/__init__.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     9507 2023-04-06 17:45:16.000000 sprint2-0.0.15/getDsRNA/step1_transcript_blat.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     9760 2023-04-06 17:45:16.000000 sprint2-0.0.15/getDsRNA/step2_transcript_dspair.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     3162 2023-04-06 17:45:16.000000 sprint2-0.0.15/getDsRNA/step3_bedtools_sorted_rmLC.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     6742 2023-04-06 17:45:16.000000 sprint2-0.0.15/getDsRNA/step4_combine_by_chr.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     5750 2023-04-06 17:45:16.000000 sprint2-0.0.15/getDsRNA/step5_merge_dsRNA.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     2408 2023-04-06 17:45:16.000000 sprint2-0.0.15/getDsRNA/step6_dsRNA.py
+drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:45:26.668221 sprint2-0.0.15/getRES/
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     2034 2023-04-06 17:45:14.000000 sprint2-0.0.15/getRES/__init__.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)    45388 2023-04-06 17:45:14.000000 sprint2-0.0.15/getRES/step1_SNVcalling.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)    20538 2023-04-06 17:45:14.000000 sprint2-0.0.15/getRES/step2_annotation_based.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)    19408 2023-04-06 17:45:14.000000 sprint2-0.0.15/getRES/step3_dsRNA_based.py
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)       38 2023-04-06 17:45:26.720216 sprint2-0.0.15/setup.cfg
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)     1096 2023-04-06 17:45:09.000000 sprint2-0.0.15/setup.py
+drwxrwxr-x   0 xyx       (1003) xyx       (1003)        0 2023-04-06 17:45:26.708217 sprint2-0.0.15/sprint2.egg-info/
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)      621 2023-04-06 17:45:26.000000 sprint2-0.0.15/sprint2.egg-info/PKG-INFO
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)      565 2023-04-06 17:45:26.000000 sprint2-0.0.15/sprint2.egg-info/SOURCES.txt
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)        1 2023-04-06 17:45:26.000000 sprint2-0.0.15/sprint2.egg-info/dependency_links.txt
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)       90 2023-04-06 17:45:26.000000 sprint2-0.0.15/sprint2.egg-info/entry_points.txt
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)        9 2023-04-06 17:45:26.000000 sprint2-0.0.15/sprint2.egg-info/requires.txt
+-rw-rw-r--   0 xyx       (1003) xyx       (1003)       26 2023-04-06 17:45:26.000000 sprint2-0.0.15/sprint2.egg-info/top_level.txt
```

### Comparing `sprint2-0.0.14/MaskAGref/MaskAGref.py` & `sprint2-0.0.15/MaskAGref/MaskAGref.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/PKG-INFO` & `sprint2-0.0.15/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sprint2
-Version: 0.0.14
+Version: 0.0.15
 Summary: SPRINT-2.0: An enhanced tool to identify RNA editing sites
 Home-page: https://github.com/xieyunxiao/SPRINT2
 Author: Feng Zhang, Yunxiao Xie
 Author-email: 20210700107@fudan.edu.cn
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `sprint2-0.0.14/getDsRNA/__init__.py` & `sprint2-0.0.15/getDsRNA/__init__.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/getDsRNA/step1_transcript_blat.py` & `sprint2-0.0.15/getDsRNA/step1_transcript_blat.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/getDsRNA/step2_transcript_dspair.py` & `sprint2-0.0.15/getDsRNA/step2_transcript_dspair.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/getDsRNA/step3_bedtools_sorted_rmLC.py` & `sprint2-0.0.15/getDsRNA/step3_bedtools_sorted_rmLC.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/getDsRNA/step4_combine_by_chr.py` & `sprint2-0.0.15/getDsRNA/step4_combine_by_chr.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/getDsRNA/step5_merge_dsRNA.py` & `sprint2-0.0.15/getDsRNA/step5_merge_dsRNA.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/getDsRNA/step6_dsRNA.py` & `sprint2-0.0.15/getDsRNA/step6_dsRNA.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/getRES/__init__.py` & `sprint2-0.0.15/getRES/__init__.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/getRES/step1_SNVcalling.py` & `sprint2-0.0.15/getRES/step1_SNVcalling.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/getRES/step2_annotation_based.py` & `sprint2-0.0.15/getRES/step2_annotation_based.py`

 * *Files 0% similar despite different names*

```diff
@@ -442,22 +442,22 @@
     try:
         args = parser.parse_args(args.split())
 
     except argparse.ArgumentError as e:
         print(e)
         exit(1)
 
-    global ori_tmp,tmp
+    global ori_tmp,tmp,repeat
     ori_tmp=str(args.snv)+"/"
     tmp=str(args.output)+"/"
     repeat=str(args.repeat)
 
     global cluster_distance,cluster_size_alu_ad1,cluster_size_alu_ad2,cluster_size_nalurp,cluster_size_nrp
     global cluster_size_rg,cluster_size_hp,cluster_size_alu_hp,cluster_size_nalurp_hp,cluster_size_nrp_hp
-    global strand_specify,var_limit,poly_limit,rm_multi,repeat
+    global strand_specify,var_limit,poly_limit,rm_multi
     cluster_distance=200
     cluster_size_alu_ad1 = 3
     cluster_size_alu_ad2 = 2
     cluster_size_nalurp = 5
     cluster_size_nrp = 7
     cluster_size_rg = 5
     cluster_size_hp = 5
```

### Comparing `sprint2-0.0.14/getRES/step3_dsRNA_based.py` & `sprint2-0.0.15/getRES/step3_dsRNA_based.py`

 * *Files identical despite different names*

### Comparing `sprint2-0.0.14/setup.py` & `sprint2-0.0.15/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 # To use a consistent encoding
 from codecs import open
 from os import path
 
 
 setup(
     name='sprint2',
-    version='0.0.14',
+    version='0.0.15',
     packages=find_packages(),
     install_requires=[
         'argparse',
     ],
     entry_points={
         'console_scripts': [
             'MaskAGref=MaskAGref:main',
```

### Comparing `sprint2-0.0.14/sprint2.egg-info/PKG-INFO` & `sprint2-0.0.15/sprint2.egg-info/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sprint2
-Version: 0.0.14
+Version: 0.0.15
 Summary: SPRINT-2.0: An enhanced tool to identify RNA editing sites
 Home-page: https://github.com/xieyunxiao/SPRINT2
 Author: Feng Zhang, Yunxiao Xie
 Author-email: 20210700107@fudan.edu.cn
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `sprint2-0.0.14/sprint2.egg-info/SOURCES.txt` & `sprint2-0.0.15/sprint2.egg-info/SOURCES.txt`

 * *Files identical despite different names*

