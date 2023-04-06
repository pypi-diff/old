# Comparing `tmp/spanishconjugator-2.3.998.tar.gz` & `tmp/spanishconjugator-2.3.999.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "spanishconjugator-2.3.998.tar", last modified: Thu Jan 13 17:35:42 2022, max compression
+gzip compressed data, was "spanishconjugator-2.3.999.tar", last modified: Thu Jan 13 20:28:54 2022, max compression
```

## Comparing `spanishconjugator-2.3.998.tar` & `spanishconjugator-2.3.999.tar`

### file list

```diff
@@ -1,50 +1,50 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.641233 spanishconjugator-2.3.998/
--rw-r--r--   0 runner    (1001) docker     (121)     1067 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/LICENSE.txt
--rw-r--r--   0 runner    (1001) docker     (121)       43 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     5945 2022-01-13 17:35:42.641233 spanishconjugator-2.3.998/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     5202 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/README.md
--rw-r--r--   0 runner    (1001) docker     (121)      129 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)       38 2022-01-13 17:35:42.641233 spanishconjugator-2.3.998/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     1275 2022-01-13 17:35:41.000000 spanishconjugator-2.3.998/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.633233 spanishconjugator-2.3.998/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.637233 spanishconjugator-2.3.998/src/spanishconjugator/
--rw-r--r--   0 runner    (1001) docker     (121)     9871 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/SpanishConjugator.py
--rw-r--r--   0 runner    (1001) docker     (121)      102 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.637233 spanishconjugator-2.3.998/src/spanishconjugator/irregulars/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/irregulars/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    16727 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/irregulars/irregular_dict.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.637233 spanishconjugator-2.3.998/src/spanishconjugator/tenses/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.637233 spanishconjugator-2.3.998/src/spanishconjugator/tenses/conditional/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/conditional/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1842 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/conditional/perfect.py
--rw-r--r--   0 runner    (1001) docker     (121)     3655 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/conditional/simple_conditional.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.637233 spanishconjugator-2.3.998/src/spanishconjugator/tenses/imperative/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/imperative/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2015 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/imperative/affirmative.py
--rw-r--r--   0 runner    (1001) docker     (121)     2021 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/imperative/negative.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.637233 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     3338 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/future.py
--rw-r--r--   0 runner    (1001) docker     (121)     1834 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/future_perfect.py
--rw-r--r--   0 runner    (1001) docker     (121)     4100 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/imperfect.py
--rw-r--r--   0 runner    (1001) docker     (121)     1827 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/past_anterior.py
--rw-r--r--   0 runner    (1001) docker     (121)     4325 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/past_perfect.py
--rw-r--r--   0 runner    (1001) docker     (121)     4640 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/present.py
--rw-r--r--   0 runner    (1001) docker     (121)     4342 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/present_perfect.py
--rw-r--r--   0 runner    (1001) docker     (121)     4086 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/preterite.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.637233 spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/
--rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1692 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/future.py
--rw-r--r--   0 runner    (1001) docker     (121)     1851 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/future_perfect.py
--rw-r--r--   0 runner    (1001) docker     (121)     1696 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/imperfect.py
--rw-r--r--   0 runner    (1001) docker     (121)     1699 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/imperfect_se.py
--rw-r--r--   0 runner    (1001) docker     (121)     1847 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/pluperfect.py
--rw-r--r--   0 runner    (1001) docker     (121)     2302 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/present.py
--rw-r--r--   0 runner    (1001) docker     (121)     1816 2022-01-13 17:35:24.000000 spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/present_perfect.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 17:35:42.637233 spanishconjugator-2.3.998/src/spanishconjugator.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     5945 2022-01-13 17:35:42.000000 spanishconjugator-2.3.998/src/spanishconjugator.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1754 2022-01-13 17:35:42.000000 spanishconjugator-2.3.998/src/spanishconjugator.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-13 17:35:42.000000 spanishconjugator-2.3.998/src/spanishconjugator.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       35 2022-01-13 17:35:42.000000 spanishconjugator-2.3.998/src/spanishconjugator.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       18 2022-01-13 17:35:42.000000 spanishconjugator-2.3.998/src/spanishconjugator.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.510031 spanishconjugator-2.3.999/
+-rw-r--r--   0 runner    (1001) docker     (121)     1067 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/LICENSE.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       43 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     5945 2022-01-13 20:28:54.510031 spanishconjugator-2.3.999/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     5202 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)      129 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       38 2022-01-13 20:28:54.510031 spanishconjugator-2.3.999/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     1275 2022-01-13 20:28:53.000000 spanishconjugator-2.3.999/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.498031 spanishconjugator-2.3.999/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.502031 spanishconjugator-2.3.999/src/spanishconjugator/
+-rw-r--r--   0 runner    (1001) docker     (121)     9871 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/SpanishConjugator.py
+-rw-r--r--   0 runner    (1001) docker     (121)      102 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.506031 spanishconjugator-2.3.999/src/spanishconjugator/irregulars/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/irregulars/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16727 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/irregulars/irregular_dict.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.506031 spanishconjugator-2.3.999/src/spanishconjugator/tenses/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.506031 spanishconjugator-2.3.999/src/spanishconjugator/tenses/conditional/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/conditional/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1842 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/conditional/perfect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3655 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/conditional/simple_conditional.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.506031 spanishconjugator-2.3.999/src/spanishconjugator/tenses/imperative/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/imperative/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2015 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/imperative/affirmative.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2021 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/imperative/negative.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.506031 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3338 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/future.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1834 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/future_perfect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4100 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/imperfect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1827 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/past_anterior.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4325 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/past_perfect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4640 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/present.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4342 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/present_perfect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4086 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/preterite.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.510031 spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/
+-rw-r--r--   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1692 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/future.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1851 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/future_perfect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1696 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/imperfect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1699 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/imperfect_se.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1847 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/pluperfect.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2302 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/present.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1816 2022-01-13 20:28:43.000000 spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/present_perfect.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-01-13 20:28:54.506031 spanishconjugator-2.3.999/src/spanishconjugator.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     5945 2022-01-13 20:28:54.000000 spanishconjugator-2.3.999/src/spanishconjugator.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1754 2022-01-13 20:28:54.000000 spanishconjugator-2.3.999/src/spanishconjugator.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-01-13 20:28:54.000000 spanishconjugator-2.3.999/src/spanishconjugator.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       35 2022-01-13 20:28:54.000000 spanishconjugator-2.3.999/src/spanishconjugator.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       18 2022-01-13 20:28:54.000000 spanishconjugator-2.3.999/src/spanishconjugator.egg-info/top_level.txt
```

### Comparing `spanishconjugator-2.3.998/LICENSE.txt` & `spanishconjugator-2.3.999/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/PKG-INFO` & `spanishconjugator-2.3.999/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: spanishconjugator
-Version: 2.3.998
+Version: 2.3.999
 Summary: A python library to conjugate spanish words with parameters tense, mood and pronoun
 Home-page: https://github.com/Benedict-Carling/spanish-conjugator
 Author: Benedict Carling
 Author-email: bencarling1@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `spanishconjugator-2.3.998/README.md` & `spanishconjugator-2.3.999/README.md`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/setup.py` & `spanishconjugator-2.3.999/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setup(
     name="spanishconjugator",
-    version="2.3.998",
+    version="2.3.999",
     description="A python library to conjugate spanish words with parameters tense, mood and pronoun",
     packages=[
         "spanishconjugator",
         "spanishconjugator.tenses",
         "spanishconjugator.tenses.conditional",
         "spanishconjugator.tenses.indicative",
         "spanishconjugator.tenses.imperative",
```

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/SpanishConjugator.py` & `spanishconjugator-2.3.999/src/spanishconjugator/SpanishConjugator.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/irregulars/irregular_dict.py` & `spanishconjugator-2.3.999/src/spanishconjugator/irregulars/irregular_dict.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/conditional/perfect.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/conditional/perfect.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/conditional/simple_conditional.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/conditional/simple_conditional.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/imperative/affirmative.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/imperative/affirmative.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/imperative/negative.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/imperative/negative.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/future.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/future.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/future_perfect.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/future_perfect.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/imperfect.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/imperfect.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/past_anterior.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/past_anterior.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/past_perfect.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/past_perfect.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/present.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/present.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/present_perfect.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/present_perfect.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/indicative/preterite.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/indicative/preterite.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/future.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/future.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/future_perfect.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/future_perfect.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/imperfect.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/imperfect.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/imperfect_se.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/imperfect_se.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/pluperfect.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/pluperfect.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/present.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/present.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator/tenses/subjunctive/present_perfect.py` & `spanishconjugator-2.3.999/src/spanishconjugator/tenses/subjunctive/present_perfect.py`

 * *Files identical despite different names*

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator.egg-info/PKG-INFO` & `spanishconjugator-2.3.999/src/spanishconjugator.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: spanishconjugator
-Version: 2.3.998
+Version: 2.3.999
 Summary: A python library to conjugate spanish words with parameters tense, mood and pronoun
 Home-page: https://github.com/Benedict-Carling/spanish-conjugator
 Author: Benedict Carling
 Author-email: bencarling1@gmail.com
 License: UNKNOWN
 Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
```

### Comparing `spanishconjugator-2.3.998/src/spanishconjugator.egg-info/SOURCES.txt` & `spanishconjugator-2.3.999/src/spanishconjugator.egg-info/SOURCES.txt`

 * *Files identical despite different names*

