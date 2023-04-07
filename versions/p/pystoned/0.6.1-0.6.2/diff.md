# Comparing `tmp/pystoned-0.6.1.tar.gz` & `tmp/pystoned-0.6.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pystoned-0.6.1.tar", last modified: Sun Feb 26 18:27:45 2023, max compression
+gzip compressed data, was "pystoned-0.6.2.tar", last modified: Fri Apr  7 08:23:46 2023, max compression
```

## Comparing `pystoned-0.6.1.tar` & `pystoned-0.6.2.tar`

### file list

```diff
@@ -1,55 +1,55 @@
-drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-02-26 18:27:45.687528 pystoned-0.6.1/
--rw-r--r--   0 dais2     (1000) dais2     (1000)    35149 2021-10-05 07:06:23.000000 pystoned-0.6.1/LICENSE
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     2976 2023-02-26 18:27:45.687528 pystoned-0.6.1/PKG-INFO
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     2288 2023-01-28 14:01:26.000000 pystoned-0.6.1/README.md
-drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-02-26 18:27:45.683528 pystoned-0.6.1/pystoned/
--rw-r--r--   0 dais2     (1000) dais2     (1000)    13169 2023-02-25 14:32:21.000000 pystoned-0.6.1/pystoned/CNLS.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)     8579 2023-02-25 12:37:20.000000 pystoned-0.6.1/pystoned/CNLSDDF.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)     9784 2023-02-25 14:32:53.000000 pystoned-0.6.1/pystoned/CNLSG.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)    15726 2023-02-25 14:33:03.000000 pystoned-0.6.1/pystoned/CQER.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)     8122 2023-02-25 12:37:20.000000 pystoned-0.6.1/pystoned/CQERDDF.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)    21380 2023-02-25 14:32:38.000000 pystoned-0.6.1/pystoned/CQERG.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     6598 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/CSVR.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)    18111 2023-01-28 13:37:04.000000 pystoned-0.6.1/pystoned/DEA.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)     5964 2023-01-28 13:48:38.000000 pystoned-0.6.1/pystoned/FDH.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     4816 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/ICNLS.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     2861 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/ICQER.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     9456 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/StoNED.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)      800 2023-01-31 11:34:44.000000 pystoned-0.6.1/pystoned/__init__.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     1473 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/constant.py
-drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-02-26 18:27:45.683528 pystoned-0.6.1/pystoned/data/
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     1429 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/data/41Firm.csv
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     7609 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/data/abatementCost.csv
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     3082 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/data/electricityFirms.csv
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    33693 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/data/riceProduction.csv
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     4733 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/dataset.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)     1649 2023-01-31 11:32:21.000000 pystoned-0.6.1/pystoned/pCNLS.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)     3447 2023-01-30 18:44:28.000000 pystoned-0.6.1/pystoned/pCQER.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)     2956 2023-01-30 18:44:10.000000 pystoned-0.6.1/pystoned/pICQER.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     4548 2023-02-26 18:24:25.000000 pystoned-0.6.1/pystoned/plot.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     8256 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/sCQER.py
-drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-02-26 18:27:45.687528 pystoned-0.6.1/pystoned/utils/
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    11736 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/utils/CNLSG1.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    14915 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/utils/CNLSG2.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    12161 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/utils/CNLSZG1.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    15358 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/utils/CNLSZG2.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    13742 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/utils/CQERG1.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    16930 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/utils/CQERG2.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    14286 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/utils/CQERZG1.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    17619 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/utils/CQERZG2.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)      240 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/utils/__init__.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)     1121 2023-02-25 14:26:26.000000 pystoned-0.6.1/pystoned/utils/interpolation.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)      960 2023-02-25 12:37:20.000000 pystoned-0.6.1/pystoned/utils/sweet.py
--rw-r--r--   0 dais2     (1000) dais2     (1000)     8892 2023-02-25 12:37:20.000000 pystoned-0.6.1/pystoned/utils/tools.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    12977 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/wCNLS.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    15753 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/wCQER.py
--rw-rw-r--   0 dais2     (1000) dais2     (1000)    14927 2023-01-28 13:53:33.000000 pystoned-0.6.1/pystoned/weakCNLS.py
-drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-02-26 18:27:45.683528 pystoned-0.6.1/pystoned.egg-info/
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     2976 2023-02-26 18:27:45.000000 pystoned-0.6.1/pystoned.egg-info/PKG-INFO
--rw-rw-r--   0 dais2     (1000) dais2     (1000)     1075 2023-02-26 18:27:45.000000 pystoned-0.6.1/pystoned.egg-info/SOURCES.txt
--rw-rw-r--   0 dais2     (1000) dais2     (1000)        1 2023-02-26 18:27:45.000000 pystoned-0.6.1/pystoned.egg-info/dependency_links.txt
--rw-rw-r--   0 dais2     (1000) dais2     (1000)        1 2023-02-26 18:27:45.000000 pystoned-0.6.1/pystoned.egg-info/not-zip-safe
--rw-rw-r--   0 dais2     (1000) dais2     (1000)       86 2023-02-26 18:27:45.000000 pystoned-0.6.1/pystoned.egg-info/requires.txt
--rw-rw-r--   0 dais2     (1000) dais2     (1000)        9 2023-02-26 18:27:45.000000 pystoned-0.6.1/pystoned.egg-info/top_level.txt
--rw-rw-r--   0 dais2     (1000) dais2     (1000)       38 2023-02-26 18:27:45.687528 pystoned-0.6.1/setup.cfg
--rw-r--r--   0 dais2     (1000) dais2     (1000)     1345 2023-02-26 18:24:17.000000 pystoned-0.6.1/setup.py
+drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-04-07 08:23:46.205601 pystoned-0.6.2/
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    35149 2021-10-05 07:06:23.000000 pystoned-0.6.2/LICENSE
+-rw-rw-r--   0 dais2     (1000) dais2     (1000)     2976 2023-04-07 08:23:46.205601 pystoned-0.6.2/PKG-INFO
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     2288 2023-01-28 14:01:26.000000 pystoned-0.6.2/README.md
+drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-04-07 08:23:46.201601 pystoned-0.6.2/pystoned/
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    13169 2023-02-25 14:32:21.000000 pystoned-0.6.2/pystoned/CNLS.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     8579 2023-04-07 08:10:12.000000 pystoned-0.6.2/pystoned/CNLSDDF.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     9784 2023-02-25 14:32:53.000000 pystoned-0.6.2/pystoned/CNLSG.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    15726 2023-02-25 14:33:03.000000 pystoned-0.6.2/pystoned/CQER.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     8122 2023-04-07 08:10:02.000000 pystoned-0.6.2/pystoned/CQERDDF.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    21380 2023-02-25 14:32:38.000000 pystoned-0.6.2/pystoned/CQERG.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     6613 2023-04-07 08:10:07.000000 pystoned-0.6.2/pystoned/CSVR.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    18111 2023-04-07 08:09:53.000000 pystoned-0.6.2/pystoned/DEA.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     5964 2023-04-07 08:09:49.000000 pystoned-0.6.2/pystoned/FDH.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     4816 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/ICNLS.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     2861 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/ICQER.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     9456 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/StoNED.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)      800 2023-01-31 11:34:44.000000 pystoned-0.6.2/pystoned/__init__.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     1473 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/constant.py
+drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-04-07 08:23:46.201601 pystoned-0.6.2/pystoned/data/
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     1429 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/data/41Firm.csv
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     7609 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/data/abatementCost.csv
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     3082 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/data/electricityFirms.csv
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    33693 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/data/riceProduction.csv
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     4733 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/dataset.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     1649 2023-01-31 11:32:21.000000 pystoned-0.6.2/pystoned/pCNLS.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     3447 2023-01-30 18:44:28.000000 pystoned-0.6.2/pystoned/pCQER.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     2956 2023-01-30 18:44:10.000000 pystoned-0.6.2/pystoned/pICQER.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     4548 2023-02-26 18:24:25.000000 pystoned-0.6.2/pystoned/plot.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     8256 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/sCQER.py
+drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-04-07 08:23:46.205601 pystoned-0.6.2/pystoned/utils/
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    11736 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/utils/CNLSG1.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    14915 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/utils/CNLSG2.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    12161 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/utils/CNLSZG1.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    15358 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/utils/CNLSZG2.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    13742 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/utils/CQERG1.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    16930 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/utils/CQERG2.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    14286 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/utils/CQERZG1.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    17619 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/utils/CQERZG2.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)      240 2023-01-28 13:53:33.000000 pystoned-0.6.2/pystoned/utils/__init__.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     1121 2023-02-25 14:26:26.000000 pystoned-0.6.2/pystoned/utils/interpolation.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)      960 2023-02-25 12:37:20.000000 pystoned-0.6.2/pystoned/utils/sweet.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     8684 2023-03-04 07:54:35.000000 pystoned-0.6.2/pystoned/utils/tools.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     1647 2023-04-07 08:10:46.000000 pystoned-0.6.2/pystoned/wCNLS.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     3342 2023-04-07 08:10:49.000000 pystoned-0.6.2/pystoned/wCQER.py
+-rw-r--r--   0 dais2     (1000) dais2     (1000)    14942 2023-04-07 08:10:52.000000 pystoned-0.6.2/pystoned/weakCNLS.py
+drwxrwxr-x   0 dais2     (1000) dais2     (1000)        0 2023-04-07 08:23:46.201601 pystoned-0.6.2/pystoned.egg-info/
+-rw-rw-r--   0 dais2     (1000) dais2     (1000)     2976 2023-04-07 08:23:46.000000 pystoned-0.6.2/pystoned.egg-info/PKG-INFO
+-rw-rw-r--   0 dais2     (1000) dais2     (1000)     1075 2023-04-07 08:23:46.000000 pystoned-0.6.2/pystoned.egg-info/SOURCES.txt
+-rw-rw-r--   0 dais2     (1000) dais2     (1000)        1 2023-04-07 08:23:46.000000 pystoned-0.6.2/pystoned.egg-info/dependency_links.txt
+-rw-rw-r--   0 dais2     (1000) dais2     (1000)        1 2023-04-07 08:23:46.000000 pystoned-0.6.2/pystoned.egg-info/not-zip-safe
+-rw-rw-r--   0 dais2     (1000) dais2     (1000)       86 2023-04-07 08:23:46.000000 pystoned-0.6.2/pystoned.egg-info/requires.txt
+-rw-rw-r--   0 dais2     (1000) dais2     (1000)        9 2023-04-07 08:23:46.000000 pystoned-0.6.2/pystoned.egg-info/top_level.txt
+-rw-rw-r--   0 dais2     (1000) dais2     (1000)       38 2023-04-07 08:23:46.205601 pystoned-0.6.2/setup.cfg
+-rw-r--r--   0 dais2     (1000) dais2     (1000)     1345 2023-04-07 08:16:40.000000 pystoned-0.6.2/setup.py
```

### Comparing `pystoned-0.6.1/LICENSE` & `pystoned-0.6.2/LICENSE`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/PKG-INFO` & `pystoned-0.6.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pystoned
-Version: 0.6.1
+Version: 0.6.2
 Summary: A Python Package for Convex Regression and Frontier Estimation
 Home-page: https://github.com/ds2010/pyStoNED
 Download-URL: https://pypi.org/project/pystoned/
 Author: Sheng Dai, Yu-Hsueh Fang, Chia-Yen Lee, Timo Kuosmanen
 Author-email: sheng.dai@utu.fi
 License: GPLv3
 Keywords: StoNED,CNLS,CER,CQR,Z-variables,CNLSG
```

### Comparing `pystoned-0.6.1/README.md` & `pystoned-0.6.2/README.md`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/CNLS.py` & `pystoned-0.6.2/pystoned/CNLS.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/CNLSDDF.py` & `pystoned-0.6.2/pystoned/CNLSDDF.py`

 * *Files 3% similar despite different names*

```diff
@@ -31,23 +31,23 @@
         self.rts = RTS_VRS
     
         self.__model__ = ConcreteModel()
 
         # Initialize the sets
         self.__model__.I = Set(initialize=range(len(self.y)))
         self.__model__.J = Set(initialize=range(len(self.x[0])))
-        self.__model__.K = Set(initialize=range(len(self.y[0])))
+        self.__model__.Q = Set(initialize=range(len(self.y[0])))
 
         # Initialize the variables
         self.__model__.alpha = Var(self.__model__.I, doc='alpha')
         self.__model__.beta = Var(
             self.__model__.I, self.__model__.J, bounds=(0.0, None), doc='beta')
         self.__model__.epsilon = Var(self.__model__.I, doc='residuals')
         self.__model__.gamma = Var(
-            self.__model__.I, self.__model__.K, bounds=(0.0, None), doc='gamma')
+            self.__model__.I, self.__model__.Q, bounds=(0.0, None), doc='gamma')
 
         if type(self.b) != type(None):
             self.__model__.L = Set(initialize=range(len(self.b[0])))
             self.__model__.delta = Var(
                 self.__model__.I, self.__model__.L, bounds=(0.0, None), doc='delta')
 
         # Setup the objective function and constraints
@@ -80,42 +80,42 @@
         self.problem_status, self.optimization_status = tools.optimize_model(
             self.__model__, email, CET_ADDI, solver)
 
     def __regression_rule(self):
         """Return the proper regression constraint"""
         if type(self.b) == type(None):
             def regression_rule(model, i):
-                return sum(model.gamma[i, k] * self.y[i][k] for k in model.K) \
+                return sum(model.gamma[i, q] * self.y[i][q] for q in model.Q) \
                     == model.alpha[i] \
                     + sum(model.beta[i, j] * self.x[i][j] for j in model.J) \
                     - model.epsilon[i]
 
             return regression_rule
 
         def regression_rule(model, i):
-            return sum(model.gamma[i, k] * self.y[i][k] for k in model.K) \
+            return sum(model.gamma[i, q] * self.y[i][q] for q in model.Q) \
                 == model.alpha[i] \
                 + sum(model.beta[i, j] * self.x[i][j] for j in model.J) \
                 + sum(model.delta[i, l] * self.b[i][l] for l in model.L) \
                 - model.epsilon[i]
 
         return regression_rule
 
     def __translation_property(self):
         """Return the proper translation property"""
         if type(self.b) == type(None):
             def translation_rule(model, i):
                 return sum(model.beta[i, j] * self.gx[j] for j in model.J) \
-                    + sum(model.gamma[i, k] * self.gy[k] for k in model.K) == 1
+                    + sum(model.gamma[i, q] * self.gy[q] for q in model.Q) == 1
 
             return translation_rule
 
         def translation_rule(model, i):
             return sum(model.beta[i, j] * self.gx[j] for j in model.J) \
-                + sum(model.gamma[i, k] * self.gy[k] for k in model.K) \
+                + sum(model.gamma[i, q] * self.gy[q] for q in model.Q) \
                 + sum(model.delta[i, l] * self.gb[l] for l in model.L) == 1
 
         return translation_rule
 
     def __afriat_rule(self):
         """Return the proper afriat inequality constraint"""
         if self.fun == FUN_PROD:
@@ -126,33 +126,33 @@
         if type(self.b) == type(None):
             def afriat_rule(model, i, h):
                 if i == h:
                     return Constraint.Skip
                 return __operator(model.alpha[i]
                                   + sum(model.beta[i, j] * self.x[i][j]
                                         for j in model.J)
-                                  - sum(model.gamma[i, k] * self.y[i][k]
-                                        for k in model.K),
+                                  - sum(model.gamma[i, q] * self.y[i][q]
+                                        for q in model.Q),
                                   model.alpha[h]
                                   + sum(model.beta[h, j] * self.x[i][j]
                                         for j in model.J)
-                                  - sum(model.gamma[h, k] * self.y[i][k] for k in model.K))
+                                  - sum(model.gamma[h, q] * self.y[i][q] for q in model.Q))
 
             return afriat_rule
 
         def afriat_rule(model, i, h):
             if i == h:
                 return Constraint.Skip
             return __operator(model.epsilon[i],
                               model.alpha[h]
                               + sum(model.beta[h, j] * self.x[i][j]
                                     for j in model.J)
                               + sum(model.delta[h, l] * self.b[i][l]
                                     for l in model.L)
-                              - sum(model.gamma[h, k] * self.y[i][k] for k in model.K))
+                              - sum(model.gamma[h, q] * self.y[i][q] for q in model.Q))
 
         return afriat_rule
 
     def display_gamma(self):
         """Display gamma value"""
         tools.assert_optimized(self.optimization_status)
         self.__model__.gamma.display()
```

### Comparing `pystoned-0.6.1/pystoned/CNLSG.py` & `pystoned-0.6.2/pystoned/CNLSG.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/CQER.py` & `pystoned-0.6.2/pystoned/CQER.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/CQERDDF.py` & `pystoned-0.6.2/pystoned/CQERDDF.py`

 * *Files 2% similar despite different names*

```diff
@@ -29,22 +29,22 @@
         self.fun = fun
         self.rts = RTS_VRS
         self.__model__ = ConcreteModel()
 
         # Initialize the sets
         self.__model__.I = Set(initialize=range(len(self.y)))
         self.__model__.J = Set(initialize=range(len(self.x[0])))
-        self.__model__.K = Set(initialize=range(len(self.y[0])))
+        self.__model__.Q = Set(initialize=range(len(self.y[0])))
 
         # Initialize the variables
         self.__model__.alpha = Var(self.__model__.I, doc='alpha')
         self.__model__.beta = Var(
             self.__model__.I, self.__model__.J, bounds=(0.0, None), doc='beta')
         self.__model__.gamma = Var(
-            self.__model__.I, self.__model__.K, bounds=(0.0, None), doc='gamma')
+            self.__model__.I, self.__model__.Q, bounds=(0.0, None), doc='gamma')
 
         self.__model__.epsilon = Var(self.__model__.I, doc='residuals')
         self.__model__.epsilon_plus = Var(
             self.__model__.I, bounds=(0.0, None), doc='positive error term')
         self.__model__.epsilon_minus = Var(
             self.__model__.I, bounds=(0.0, None), doc='negative error term')
 
@@ -78,23 +78,23 @@
         self.optimization_status = 0
         self.problem_status = 0
 
     def __regression_rule(self):
         """Return the proper regression constraint"""
         if type(self.b) == type(None):
             def regression_rule(model, i):
-                return sum(model.gamma[i, k] * self.y[i][k] for k in model.K) \
+                return sum(model.gamma[i, q] * self.y[i][q] for q in model.Q) \
                     == model.alpha[i] \
                     + sum(model.beta[i, j] * self.x[i][j] for j in model.J) \
                     + model.epsilon[i]
 
             return regression_rule
 
         def regression_rule(model, i):
-            return sum(model.gamma[i, k] * self.y[i][k] for k in model.K) \
+            return sum(model.gamma[i, q] * self.y[i][q] for q in model.Q) \
                 == model.alpha[i] \
                 + sum(model.beta[i, j] * self.x[i][j] for j in model.J) \
                 + sum(model.delta[i, l] * self.b[i][l] for l in model.L) \
                 + model.epsilon[i]
 
         return regression_rule
 
@@ -108,39 +108,39 @@
         if type(self.b) == type(None):
             def afriat_rule(model, i, h):
                 if i == h:
                     return Constraint.Skip
                 return __operator(model.alpha[i]
                                   + sum(model.beta[i, j] * self.x[i][j]
                                         for j in model.J)
-                                  - sum(model.gamma[i, k] * self.y[i][k]
-                                        for k in model.K),
+                                  - sum(model.gamma[i, q] * self.y[i][q]
+                                        for q in model.Q),
                                   model.alpha[h]
                                   + sum(model.beta[h, j] * self.x[i][j]
                                         for j in model.J)
-                                  - sum(model.gamma[h, k] * self.y[i][k] for k in model.K))
+                                  - sum(model.gamma[h, q] * self.y[i][q] for q in model.Q))
 
             return afriat_rule
 
         def afriat_rule(model, i, h):
             if i == h:
                 return Constraint.Skip
             return __operator(model.alpha[i]
                               + sum(model.beta[i, j] * self.x[i][j]
                                     for j in model.J)
                               + sum(model.delta[i, l] * self.b[i][l]
                                     for l in model.L)
-                              - sum(model.gamma[i, k] * self.y[i][k]
-                                    for k in model.K),
+                              - sum(model.gamma[i, q] * self.y[i][q]
+                                    for q in model.Q),
                               model.alpha[h]
                               + sum(model.beta[h, j] * self.x[i][j]
                                     for j in model.J)
                               + sum(model.delta[h, l] * self.b[i][l]
                                     for l in model.L)
-                              - sum(model.gamma[h, k] * self.y[i][k] for k in model.K))
+                              - sum(model.gamma[h, q] * self.y[i][q] for q in model.Q))
 
         return afriat_rule
 
 
 class CERDDF(CQRDDF):
     """Convex expectile regression with DDF formulation
     """
```

### Comparing `pystoned-0.6.1/pystoned/CQERG.py` & `pystoned-0.6.2/pystoned/CQERG.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/CSVR.py` & `pystoned-0.6.2/pystoned/CSVR.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # import dependencies
 from pyomo.environ import ConcreteModel, Set, Var, Objective, minimize, Constraint
 from pyomo.core.expr.numvalue import NumericValue
 import numpy as np
 import pandas as pd
 
 from .constant import CET_ADDI, FUN_PROD, FUN_COST, OPT_DEFAULT, OPT_LOCAL
-from .utils import tools
+from .utils import tools, interpolation
 
 
 class CSVR:
     """Convex Support Vector Regression (CSVR)
     """
 
     def __init__(self, y, x, fun=FUN_PROD, epsilon=0.01, C=2):
```

### Comparing `pystoned-0.6.1/pystoned/DEA.py` & `pystoned-0.6.2/pystoned/DEA.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/FDH.py` & `pystoned-0.6.2/pystoned/FDH.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/ICNLS.py` & `pystoned-0.6.2/pystoned/ICNLS.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/ICQER.py` & `pystoned-0.6.2/pystoned/ICQER.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/StoNED.py` & `pystoned-0.6.2/pystoned/StoNED.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/__init__.py` & `pystoned-0.6.2/pystoned/__init__.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/constant.py` & `pystoned-0.6.2/pystoned/constant.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/data/41Firm.csv` & `pystoned-0.6.2/pystoned/data/41Firm.csv`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/data/abatementCost.csv` & `pystoned-0.6.2/pystoned/data/abatementCost.csv`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/data/electricityFirms.csv` & `pystoned-0.6.2/pystoned/data/electricityFirms.csv`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/data/riceProduction.csv` & `pystoned-0.6.2/pystoned/data/riceProduction.csv`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/dataset.py` & `pystoned-0.6.2/pystoned/dataset.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/pCNLS.py` & `pystoned-0.6.2/pystoned/pCNLS.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/pCQER.py` & `pystoned-0.6.2/pystoned/pCQER.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/pICQER.py` & `pystoned-0.6.2/pystoned/pICQER.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/plot.py` & `pystoned-0.6.2/pystoned/plot.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/sCQER.py` & `pystoned-0.6.2/pystoned/sCQER.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/CNLSG1.py` & `pystoned-0.6.2/pystoned/utils/CNLSG1.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/CNLSG2.py` & `pystoned-0.6.2/pystoned/utils/CNLSG2.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/CNLSZG1.py` & `pystoned-0.6.2/pystoned/utils/CNLSZG1.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/CNLSZG2.py` & `pystoned-0.6.2/pystoned/utils/CNLSZG2.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/CQERG1.py` & `pystoned-0.6.2/pystoned/utils/CQERG1.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/CQERG2.py` & `pystoned-0.6.2/pystoned/utils/CQERG2.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/CQERZG1.py` & `pystoned-0.6.2/pystoned/utils/CQERZG1.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/CQERZG2.py` & `pystoned-0.6.2/pystoned/utils/CQERZG2.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/interpolation.py` & `pystoned-0.6.2/pystoned/utils/interpolation.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/sweet.py` & `pystoned-0.6.2/pystoned/utils/sweet.py`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/pystoned/utils/tools.py` & `pystoned-0.6.2/pystoned/utils/tools.py`

 * *Files 2% similar despite different names*

```diff
@@ -263,36 +263,30 @@
         if y_shape[0] != z_shape[0]:
             raise ValueError(
                 "Number of DMUs must be the same in y and z.")
 
     return y, x, b, z
 
 
-def assert_valid_basic_data_weight(y, x, w, z=None):
+def assert_valid_mupltiple_x_y_data(y, x, z=None):
     y = trans_list(y)
     x = trans_list(x)
-    w = trans_list(w)
 
-    y = to_1d_list(y)
+    y = to_2d_list(y)
     x = to_2d_list(x)
-    w = to_1d_list(w)
 
     y_shape = np.asarray(y).shape
     x_shape = np.asarray(x).shape
 
-    if len(y_shape) == 2 and y_shape[1] != 1:
-        raise ValueError(
-            "The multidimensional output data is supported by direciontal based models.")
-
     if y_shape[0] != x_shape[0]:
         raise ValueError(
             "Number of DMUs must be the same in x and y.")
-
+    
     if type(z) != type(None):
         z = trans_list(z)
         z = to_2d_list(z)
         z_shape = np.asarray(z).shape
         if y_shape[0] != z_shape[0]:
             raise ValueError(
                 "Number of DMUs must be the same in y and z.")
-
-    return y, x, w, z
+        
+    return y, x, z
```

### Comparing `pystoned-0.6.1/pystoned/weakCNLS.py` & `pystoned-0.6.2/pystoned/weakCNLS.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 # import dependencies
 from pyomo.environ import ConcreteModel, Set, Var, Objective, minimize, Constraint, log
 from pyomo.core.expr.numvalue import NumericValue
 import numpy as np
 import pandas as pd
 
 from .constant import CET_ADDI, CET_MULT, FUN_PROD, FUN_COST, OPT_DEFAULT, RTS_CRS, RTS_VRS, OPT_LOCAL
-from .utils import tools
+from .utils import tools, interpolation
 
 
 class weakCNLS:
     """Convex Nonparametric Least Square with weak disposability (weakCNLS)
     """
 
     def __init__(self, y, x, b, z=None, cet=CET_ADDI, fun=FUN_PROD, rts=RTS_VRS):
```

### Comparing `pystoned-0.6.1/pystoned.egg-info/PKG-INFO` & `pystoned-0.6.2/pystoned.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pystoned
-Version: 0.6.1
+Version: 0.6.2
 Summary: A Python Package for Convex Regression and Frontier Estimation
 Home-page: https://github.com/ds2010/pyStoNED
 Download-URL: https://pypi.org/project/pystoned/
 Author: Sheng Dai, Yu-Hsueh Fang, Chia-Yen Lee, Timo Kuosmanen
 Author-email: sheng.dai@utu.fi
 License: GPLv3
 Keywords: StoNED,CNLS,CER,CQR,Z-variables,CNLSG
```

### Comparing `pystoned-0.6.1/pystoned.egg-info/SOURCES.txt` & `pystoned-0.6.2/pystoned.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pystoned-0.6.1/setup.py` & `pystoned-0.6.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open('README.md') as readme_file:
     README = readme_file.read()
 
 setup_args = dict(
     name='pystoned',
-    version='0.6.1',
+    version='0.6.2',
     description='A Python Package for Convex Regression and Frontier Estimation',
     long_description_content_type="text/markdown",
     long_description=README,
     license='GPLv3',
     packages=find_packages(),
     author='Sheng Dai, Yu-Hsueh Fang, Chia-Yen Lee, Timo Kuosmanen',
     author_email='sheng.dai@utu.fi',
```

