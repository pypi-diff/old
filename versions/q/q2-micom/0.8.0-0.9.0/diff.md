# Comparing `tmp/q2-micom-0.8.0.tar.gz` & `tmp/q2-micom-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/q2-micom-0.8.0.tar", last modified: Tue May 12 02:02:09 2020, max compression
+gzip compressed data, was "dist/q2-micom-0.9.0.tar", last modified: Tue Aug 18 00:03:40 2020, max compression
```

## Comparing `q2-micom-0.8.0.tar` & `q2-micom-0.9.0.tar`

### file list

```diff
@@ -1,41 +1,41 @@
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-05-12 02:02:09.000000 q2-micom-0.8.0/
--rw-r--r--   0 runner    (1001) docker     (116)     1620 2020-05-12 02:02:00.000000 q2-micom-0.8.0/setup.py
--rw-r--r--   0 runner    (1001) docker     (116)      774 2020-05-12 02:02:09.000000 q2-micom-0.8.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (116)     4240 2020-05-12 02:02:09.000000 q2-micom-0.8.0/PKG-INFO
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom.egg-info/
--rw-r--r--   0 runner    (1001) docker     (116)      918 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (116)        1 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (116)        9 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (116)        1 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (116)      184 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (116)     4240 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)       58 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom.egg-info/entry_points.txt
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom/
--rw-r--r--   0 runner    (1001) docker     (116)     2389 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/_build.py
--rw-r--r--   0 runner    (1001) docker     (116)      930 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/_tradeoff.py
--rw-r--r--   0 runner    (1001) docker     (116)      685 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/_db.py
--rw-r--r--   0 runner    (1001) docker     (116)    14608 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/plugin_setup.py
--rw-r--r--   0 runner    (1001) docker     (116)     4911 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/_formats_and_types.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom/assets/
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom/assets/templates/
--rw-r--r--   0 runner    (1001) docker     (116)     2838 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/assets/templates/sample_heatmap.html
--rw-r--r--   0 runner    (1001) docker     (116)     6205 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/assets/templates/tests.html
--rw-r--r--   0 runner    (1001) docker     (116)     3277 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/assets/templates/growth.html
--rw-r--r--   0 runner    (1001) docker     (116)     5014 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/assets/templates/tradeoff.html
--rw-r--r--   0 runner    (1001) docker     (116)     3163 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/assets/templates/umap.html
--rw-r--r--   0 runner    (1001) docker     (116)     1341 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     2815 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/_transform.py
--rw-r--r--   0 runner    (1001) docker     (116)     3901 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/citations.bib
--rw-r--r--   0 runner    (1001) docker     (116)      774 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/_medium.py
--rw-r--r--   0 runner    (1001) docker     (116)     1602 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/_viz.py
--rw-r--r--   0 runner    (1001) docker     (116)      923 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/_growth.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-05-12 02:02:09.000000 q2-micom-0.8.0/q2_micom/tests/
--rw-r--r--   0 runner    (1001) docker     (116)     1065 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/tests/test_growth.py
--rw-r--r--   0 runner    (1001) docker     (116)     1022 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/tests/test_tradeoff.py
--rw-r--r--   0 runner    (1001) docker     (116)     1823 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/tests/test_viz.py
--rw-r--r--   0 runner    (1001) docker     (116)      939 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/tests/test_build.py
--rw-r--r--   0 runner    (1001) docker     (116)     1354 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/tests/test_db.py
--rw-r--r--   0 runner    (1001) docker     (116)      714 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/tests/test_medium.py
--rw-r--r--   0 runner    (1001) docker     (116)        0 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/tests/test_plugin.py
--rw-r--r--   0 runner    (1001) docker     (116)      140 2020-05-12 02:02:00.000000 q2-micom-0.8.0/q2_micom/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     2662 2020-05-12 02:02:00.000000 q2-micom-0.8.0/README.md
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-08-18 00:03:40.000000 q2-micom-0.9.0/
+-rw-r--r--   0 runner    (1001) docker     (116)     4240 2020-08-18 00:03:40.000000 q2-micom-0.9.0/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)     2662 2020-08-18 00:03:31.000000 q2-micom-0.9.0/README.md
+-rw-r--r--   0 runner    (1001) docker     (116)      774 2020-08-18 00:03:40.000000 q2-micom-0.9.0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (116)        1 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (116)      918 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (116)     4240 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (116)        9 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (116)        1 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (116)       58 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (116)      184 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (116)     1620 2020-08-18 00:03:31.000000 q2-micom-0.9.0/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom/
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom/tests/
+-rw-r--r--   0 runner    (1001) docker     (116)      714 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/tests/test_medium.py
+-rw-r--r--   0 runner    (1001) docker     (116)      939 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/tests/test_build.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1065 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/tests/test_growth.py
+-rw-r--r--   0 runner    (1001) docker     (116)        0 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/tests/test_plugin.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1823 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/tests/test_viz.py
+-rw-r--r--   0 runner    (1001) docker     (116)      140 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1354 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/tests/test_db.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1022 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/tests/test_tradeoff.py
+-rw-r--r--   0 runner    (1001) docker     (116)      930 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/_tradeoff.py
+-rw-r--r--   0 runner    (1001) docker     (116)     3901 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/citations.bib
+-rw-r--r--   0 runner    (1001) docker     (116)     1602 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/_viz.py
+-rw-r--r--   0 runner    (1001) docker     (116)      923 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/_growth.py
+-rw-r--r--   0 runner    (1001) docker     (116)     1341 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (116)     2815 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/_transform.py
+-rw-r--r--   0 runner    (1001) docker     (116)     4911 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/_formats_and_types.py
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom/assets/
+drwxr-xr-x   0 runner    (1001) docker     (116)        0 2020-08-18 00:03:40.000000 q2-micom-0.9.0/q2_micom/assets/templates/
+-rw-r--r--   0 runner    (1001) docker     (116)     5014 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/assets/templates/tradeoff.html
+-rw-r--r--   0 runner    (1001) docker     (116)     2838 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/assets/templates/sample_heatmap.html
+-rw-r--r--   0 runner    (1001) docker     (116)     3163 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/assets/templates/umap.html
+-rw-r--r--   0 runner    (1001) docker     (116)     6205 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/assets/templates/tests.html
+-rw-r--r--   0 runner    (1001) docker     (116)     3277 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/assets/templates/growth.html
+-rw-r--r--   0 runner    (1001) docker     (116)      774 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/_medium.py
+-rw-r--r--   0 runner    (1001) docker     (116)      685 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/_db.py
+-rw-r--r--   0 runner    (1001) docker     (116)     2389 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/_build.py
+-rw-r--r--   0 runner    (1001) docker     (116)    14608 2020-08-18 00:03:31.000000 q2-micom-0.9.0/q2_micom/plugin_setup.py
```

### Comparing `q2-micom-0.8.0/setup.py` & `q2-micom-0.9.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 from setuptools import setup, find_packages
 
 with open('README.md') as f:
     long_description = f.read()
 
 setup(
     name="q2-micom",
-    version="0.8.0",
+    version="0.9.0",
     packages=find_packages(),
     package_data={"q2_micom": ["citations.bib", "assets/templates/*.html"]},
     author="Christian Diener",
     author_email="cdiener@isbscience.org",
     description="Plugin for metabolic modeling of microbial communities.",
     long_description=long_description,
     long_description_content_type='text/markdown',
```

### Comparing `q2-micom-0.8.0/setup.cfg` & `q2-micom-0.9.0/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,9 +1,9 @@
 [bumpversion]
-current_version = 0.8.0
+current_version = 0.9.0
 commit = True
 tag = True
 
 [bumpversion:file:setup.py]
 search = version="{current_version}"
 replace = version="{new_version}"
```

### Comparing `q2-micom-0.8.0/PKG-INFO` & `q2-micom-0.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: q2-micom
-Version: 0.8.0
+Version: 0.9.0
 Summary: Plugin for metabolic modeling of microbial communities.
 Home-page: https://github.com/micom-dev/q2-micom
 Author: Christian Diener
 Author-email: cdiener@isbscience.org
 License: Apache License 2.0
 Description: <img src="docs/assets/logo.png" width="75%">
         
@@ -110,9 +110,9 @@
 Classifier: Topic :: Scientific/Engineering :: Bio-Informatics
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
-Provides-Extra: dev
 Provides-Extra: test
+Provides-Extra: dev
```

### Comparing `q2-micom-0.8.0/q2_micom.egg-info/SOURCES.txt` & `q2-micom-0.9.0/q2_micom.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom.egg-info/PKG-INFO` & `q2-micom-0.9.0/q2_micom.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: q2-micom
-Version: 0.8.0
+Version: 0.9.0
 Summary: Plugin for metabolic modeling of microbial communities.
 Home-page: https://github.com/micom-dev/q2-micom
 Author: Christian Diener
 Author-email: cdiener@isbscience.org
 License: Apache License 2.0
 Description: <img src="docs/assets/logo.png" width="75%">
         
@@ -110,9 +110,9 @@
 Classifier: Topic :: Scientific/Engineering :: Bio-Informatics
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
-Provides-Extra: dev
 Provides-Extra: test
+Provides-Extra: dev
```

### Comparing `q2-micom-0.8.0/q2_micom/_build.py` & `q2-micom-0.9.0/q2_micom/_build.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/_tradeoff.py` & `q2-micom-0.9.0/q2_micom/_tradeoff.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/_db.py` & `q2-micom-0.9.0/q2_micom/_db.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/plugin_setup.py` & `q2-micom-0.9.0/q2_micom/plugin_setup.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/_formats_and_types.py` & `q2-micom-0.9.0/q2_micom/_formats_and_types.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/assets/templates/sample_heatmap.html` & `q2-micom-0.9.0/q2_micom/assets/templates/sample_heatmap.html`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/assets/templates/tests.html` & `q2-micom-0.9.0/q2_micom/assets/templates/tests.html`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/assets/templates/growth.html` & `q2-micom-0.9.0/q2_micom/assets/templates/growth.html`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/assets/templates/tradeoff.html` & `q2-micom-0.9.0/q2_micom/assets/templates/tradeoff.html`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/assets/templates/umap.html` & `q2-micom-0.9.0/q2_micom/assets/templates/umap.html`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/__init__.py` & `q2-micom-0.9.0/q2_micom/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -10,15 +10,15 @@
     plot_growth,
     exchanges_per_sample,
     exchanges_per_taxon,
     plot_tradeoff,
     fit_phenotype,
 )
 
-__version__ = "0.8.0"
+__version__ = "0.9.0"
 
 
 def read_results(path):
     """Read the results from a MICOM simulation.
 
     Parameters:
     -----------
```

### Comparing `q2-micom-0.8.0/q2_micom/_transform.py` & `q2-micom-0.9.0/q2_micom/_transform.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/citations.bib` & `q2-micom-0.9.0/q2_micom/citations.bib`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/_medium.py` & `q2-micom-0.9.0/q2_micom/_medium.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/_viz.py` & `q2-micom-0.9.0/q2_micom/_viz.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/_growth.py` & `q2-micom-0.9.0/q2_micom/_growth.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/tests/test_growth.py` & `q2-micom-0.9.0/q2_micom/tests/test_growth.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/tests/test_tradeoff.py` & `q2-micom-0.9.0/q2_micom/tests/test_tradeoff.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/tests/test_viz.py` & `q2-micom-0.9.0/q2_micom/tests/test_viz.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/tests/test_build.py` & `q2-micom-0.9.0/q2_micom/tests/test_build.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/tests/test_db.py` & `q2-micom-0.9.0/q2_micom/tests/test_db.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/q2_micom/tests/test_medium.py` & `q2-micom-0.9.0/q2_micom/tests/test_medium.py`

 * *Files identical despite different names*

### Comparing `q2-micom-0.8.0/README.md` & `q2-micom-0.9.0/README.md`

 * *Files identical despite different names*

