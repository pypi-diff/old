# Comparing `tmp/pheno-utils-0.0.4.tar.gz` & `tmp/pheno-utils-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pheno-utils-0.0.4.tar", last modified: Wed Mar 29 12:17:27 2023, max compression
+gzip compressed data, was "pheno-utils-0.0.5.tar", last modified: Thu Apr  6 20:38:38 2023, max compression
```

## Comparing `pheno-utils-0.0.4.tar` & `pheno-utils-0.0.5.tar`

### file list

```diff
@@ -1,55 +1,25 @@
-drwxr-xr-x   0 jovyan    (1000) users      (100)        0 2023-03-29 12:17:27.181182 pheno-utils-0.0.4/
--rw-r--r--   0 jovyan    (1000) users      (100)     6148 2023-03-25 22:23:15.000000 pheno-utils-0.0.4/.DS_Store
-drwxr-xr-x   0 jovyan    (1000) users      (100)        0 2023-03-29 12:17:26.742459 pheno-utils-0.0.4/.github/
-drwxr-xr-x   0 jovyan    (1000) users      (100)        0 2023-03-29 12:17:26.839704 pheno-utils-0.0.4/.github/workflows/
--rw-rw-r--   0 jovyan    (1000) users      (100)      242 2023-01-20 02:50:04.000000 pheno-utils-0.0.4/.github/workflows/deploy.yaml
--rw-rw-r--   0 jovyan    (1000) users      (100)      148 2023-01-20 02:50:04.000000 pheno-utils-0.0.4/.github/workflows/test.yaml
--rw-r--r--   0 jovyan    (1000) users      (100)     1799 2023-03-25 22:15:20.000000 pheno-utils-0.0.4/.gitignore
--rw-r--r--   0 jovyan    (1000) users      (100)    11357 2023-03-25 22:15:20.000000 pheno-utils-0.0.4/LICENSE
--rw-rw-r--   0 jovyan    (1000) users      (100)      111 2023-01-20 02:50:04.000000 pheno-utils-0.0.4/MANIFEST.in
--rw-r--r--   0 jovyan    (1000) users      (100)     1230 2023-03-29 12:17:27.177694 pheno-utils-0.0.4/PKG-INFO
--rw-r--r--   0 jovyan    (1000) users      (100)      446 2023-03-28 08:09:50.000000 pheno-utils-0.0.4/README.md
-drwxr-xr-x   0 jovyan    (1000) users      (100)        0 2023-03-29 12:17:26.922811 pheno-utils-0.0.4/_proc/
--rw-r--r--   0 jovyan    (1000) users      (100)       10 2023-03-27 17:48:07.000000 pheno-utils-0.0.4/_proc/.gitignore
--rw-r--r--   0 jovyan    (1000) users      (100)     6002 2023-03-27 17:47:52.000000 pheno-utils-0.0.4/_proc/00_config.ipynb
--rw-r--r--   0 jovyan    (1000) users      (100)    25765 2023-03-27 17:47:58.000000 pheno-utils-0.0.4/_proc/01_basic_plots.ipynb
--rw-r--r--   0 jovyan    (1000) users      (100)     3379 2023-03-28 08:09:26.000000 pheno-utils-0.0.4/_proc/02_blandaltman_plots.ipynb
--rw-r--r--   0 jovyan    (1000) users      (100)    13722 2023-03-27 17:47:59.000000 pheno-utils-0.0.4/_proc/03_age_reference_plots.ipynb
--rw-r--r--   0 jovyan    (1000) users      (100)     4668 2023-03-27 17:47:57.000000 pheno-utils-0.0.4/_proc/04_date_plots.ipynb
-drwxr-xr-x   0 jovyan    (1000) users      (100)        0 2023-03-29 12:17:26.946376 pheno-utils-0.0.4/_proc/_docs/
--rw-r--r--   0 jovyan    (1000) users      (100)      229 2023-03-28 08:09:52.000000 pheno-utils-0.0.4/_proc/_docs/index.html
--rw-r--r--   0 jovyan    (1000) users      (100)       60 2023-03-28 08:09:52.000000 pheno-utils-0.0.4/_proc/_docs/robots.txt
--rw-r--r--   0 jovyan    (1000) users      (100)      110 2023-03-28 08:09:52.000000 pheno-utils-0.0.4/_proc/_docs/sitemap.xml
--rw-r--r--   0 jovyan    (1000) users      (100)      290 2023-03-25 22:16:51.000000 pheno-utils-0.0.4/_proc/_quarto.yml
--rw-r--r--   0 jovyan    (1000) users      (100)     2889 2023-03-27 17:47:57.000000 pheno-utils-0.0.4/_proc/index.ipynb
--rw-r--r--   0 jovyan    (1000) users      (100)      247 2023-03-28 08:09:13.000000 pheno-utils-0.0.4/_proc/nbdev.yml
--rw-rw-r--   0 jovyan    (1000) users      (100)      600 2023-01-20 02:50:04.000000 pheno-utils-0.0.4/_proc/styles.css
-drwxr-xr-x   0 jovyan    (1000) users      (100)        0 2023-03-29 12:17:27.046796 pheno-utils-0.0.4/nbs/
--rw-rw-r--   0 jovyan    (1000) users      (100)     6368 2023-03-27 17:19:15.000000 pheno-utils-0.0.4/nbs/00_config.ipynb
--rw-rw-r--   0 jovyan    (1000) users      (100)    27309 2023-03-29 12:02:36.000000 pheno-utils-0.0.4/nbs/01_basic_plots.ipynb
--rw-rw-r--   0 jovyan    (1000) users      (100)    63630 2023-03-29 12:02:40.000000 pheno-utils-0.0.4/nbs/02_blandaltman_plots.ipynb
--rw-rw-r--   0 jovyan    (1000) users      (100)   402152 2023-03-29 12:01:35.000000 pheno-utils-0.0.4/nbs/03_age_reference_plots.ipynb
--rw-r--r--   0 jovyan    (1000) users      (100)   274686 2023-03-29 12:14:08.000000 pheno-utils-0.0.4/nbs/04_date_plots.ipynb
--rw-r--r--   0 jovyan    (1000) users      (100)      290 2023-03-25 22:16:51.000000 pheno-utils-0.0.4/nbs/_quarto.yml
--rw-rw-r--   0 jovyan    (1000) users      (100)     2797 2023-03-27 17:45:22.000000 pheno-utils-0.0.4/nbs/index.ipynb
--rw-r--r--   0 jovyan    (1000) users      (100)      247 2023-03-29 12:14:49.000000 pheno-utils-0.0.4/nbs/nbdev.yml
--rw-rw-r--   0 jovyan    (1000) users      (100)      600 2023-01-20 02:50:04.000000 pheno-utils-0.0.4/nbs/styles.css
-drwxr-xr-x   0 jovyan    (1000) users      (100)        0 2023-03-29 12:17:27.108741 pheno-utils-0.0.4/pheno_utils/
--rw-r--r--   0 jovyan    (1000) users      (100)       22 2023-03-29 12:14:30.000000 pheno-utils-0.0.4/pheno_utils/__init__.py
--rw-r--r--   0 jovyan    (1000) users      (100)     5308 2023-03-29 12:14:30.000000 pheno-utils-0.0.4/pheno_utils/_modidx.py
--rw-r--r--   0 jovyan    (1000) users      (100)    16964 2023-03-29 12:14:30.000000 pheno-utils-0.0.4/pheno_utils/age_reference_plots.py
--rw-r--r--   0 jovyan    (1000) users      (100)     2333 2023-03-29 12:14:30.000000 pheno-utils-0.0.4/pheno_utils/basic_plots.py
--rw-r--r--   0 jovyan    (1000) users      (100)     2518 2023-03-29 12:14:30.000000 pheno-utils-0.0.4/pheno_utils/blandaltman_plots.py
--rw-r--r--   0 jovyan    (1000) users      (100)     1442 2023-03-29 12:14:30.000000 pheno-utils-0.0.4/pheno_utils/config.py
--rw-r--r--   0 jovyan    (1000) users      (100)     2825 2023-03-29 12:14:30.000000 pheno-utils-0.0.4/pheno_utils/dates_plots.py
-drwxr-xr-x   0 jovyan    (1000) users      (100)        0 2023-03-29 12:17:27.169822 pheno-utils-0.0.4/pheno_utils.egg-info/
--rw-r--r--   0 jovyan    (1000) users      (100)     1230 2023-03-29 12:17:26.000000 pheno-utils-0.0.4/pheno_utils.egg-info/PKG-INFO
--rw-r--r--   0 jovyan    (1000) users      (100)     1060 2023-03-29 12:17:26.000000 pheno-utils-0.0.4/pheno_utils.egg-info/SOURCES.txt
--rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-03-29 12:17:26.000000 pheno-utils-0.0.4/pheno_utils.egg-info/dependency_links.txt
--rw-r--r--   0 jovyan    (1000) users      (100)       44 2023-03-29 12:17:26.000000 pheno-utils-0.0.4/pheno_utils.egg-info/entry_points.txt
--rw-r--r--   0 jovyan    (1000) users      (100)        1 2023-03-25 22:29:41.000000 pheno-utils-0.0.4/pheno_utils.egg-info/not-zip-safe
--rw-r--r--   0 jovyan    (1000) users      (100)       87 2023-03-29 12:17:26.000000 pheno-utils-0.0.4/pheno_utils.egg-info/requires.txt
--rw-r--r--   0 jovyan    (1000) users      (100)       12 2023-03-29 12:17:26.000000 pheno-utils-0.0.4/pheno_utils.egg-info/top_level.txt
--rw-r--r--   0 jovyan    (1000) users      (100)     1028 2023-03-29 12:14:19.000000 pheno-utils-0.0.4/settings.ini
--rw-r--r--   0 jovyan    (1000) users      (100)       38 2023-03-29 12:17:27.182652 pheno-utils-0.0.4/setup.cfg
--rw-rw-r--   0 jovyan    (1000) users      (100)     2560 2023-01-20 02:50:04.000000 pheno-utils-0.0.4/setup.py
+drwxr-xr-x   0 alondmnt   (501) staff       (20)        0 2023-04-06 20:38:38.322388 pheno-utils-0.0.5/
+-rw-r--r--   0 alondmnt   (501) staff       (20)    11357 2023-04-06 20:07:34.000000 pheno-utils-0.0.5/LICENSE
+-rw-r--r--   0 alondmnt   (501) staff       (20)      111 2023-04-06 20:07:42.000000 pheno-utils-0.0.5/MANIFEST.in
+-rw-r--r--   0 alondmnt   (501) staff       (20)     1479 2023-04-06 20:38:38.321987 pheno-utils-0.0.5/PKG-INFO
+-rw-r--r--   0 alondmnt   (501) staff       (20)      446 2023-04-06 20:07:47.000000 pheno-utils-0.0.5/README.md
+drwxr-xr-x   0 alondmnt   (501) staff       (20)        0 2023-04-06 20:38:38.318053 pheno-utils-0.0.5/pheno_utils/
+-rw-r--r--   0 alondmnt   (501) staff       (20)       22 2023-04-06 20:09:00.000000 pheno-utils-0.0.5/pheno_utils/__init__.py
+-rw-r--r--   0 alondmnt   (501) staff       (20)     8743 2023-04-06 20:10:17.000000 pheno-utils-0.0.5/pheno_utils/_modidx.py
+-rw-r--r--   0 alondmnt   (501) staff       (20)    16963 2023-04-06 20:09:00.000000 pheno-utils-0.0.5/pheno_utils/age_reference_plots.py
+-rw-r--r--   0 alondmnt   (501) staff       (20)     2333 2023-04-06 20:09:00.000000 pheno-utils-0.0.5/pheno_utils/basic_plots.py
+-rw-r--r--   0 alondmnt   (501) staff       (20)     2517 2023-04-06 20:09:00.000000 pheno-utils-0.0.5/pheno_utils/blandaltman_plots.py
+-rw-r--r--   0 alondmnt   (501) staff       (20)     2740 2023-04-06 20:09:00.000000 pheno-utils-0.0.5/pheno_utils/config.py
+-rw-r--r--   0 alondmnt   (501) staff       (20)    11460 2023-04-06 20:09:00.000000 pheno-utils-0.0.5/pheno_utils/data_loader.py
+-rw-r--r--   0 alondmnt   (501) staff       (20)     2825 2023-04-06 20:09:00.000000 pheno-utils-0.0.5/pheno_utils/dates_plots.py
+drwxr-xr-x   0 alondmnt   (501) staff       (20)        0 2023-04-06 20:38:38.321334 pheno-utils-0.0.5/pheno_utils.egg-info/
+-rw-r--r--   0 alondmnt   (501) staff       (20)     1479 2023-04-06 20:38:38.000000 pheno-utils-0.0.5/pheno_utils.egg-info/PKG-INFO
+-rw-r--r--   0 alondmnt   (501) staff       (20)      515 2023-04-06 20:38:38.000000 pheno-utils-0.0.5/pheno_utils.egg-info/SOURCES.txt
+-rw-r--r--   0 alondmnt   (501) staff       (20)        1 2023-04-06 20:38:38.000000 pheno-utils-0.0.5/pheno_utils.egg-info/dependency_links.txt
+-rw-r--r--   0 alondmnt   (501) staff       (20)       65 2023-04-06 20:38:38.000000 pheno-utils-0.0.5/pheno_utils.egg-info/entry_points.txt
+-rw-r--r--   0 alondmnt   (501) staff       (20)        1 2023-04-06 08:56:36.000000 pheno-utils-0.0.5/pheno_utils.egg-info/not-zip-safe
+-rw-r--r--   0 alondmnt   (501) staff       (20)       99 2023-04-06 20:38:38.000000 pheno-utils-0.0.5/pheno_utils.egg-info/requires.txt
+-rw-r--r--   0 alondmnt   (501) staff       (20)       12 2023-04-06 20:38:38.000000 pheno-utils-0.0.5/pheno_utils.egg-info/top_level.txt
+-rw-r--r--   0 alondmnt   (501) staff       (20)     1040 2023-04-06 20:15:47.000000 pheno-utils-0.0.5/settings.ini
+-rw-r--r--   0 alondmnt   (501) staff       (20)       38 2023-04-06 20:38:38.322530 pheno-utils-0.0.5/setup.cfg
+-rw-r--r--   0 alondmnt   (501) staff       (20)     2560 2023-04-06 20:07:57.000000 pheno-utils-0.0.5/setup.py
```

### Comparing `pheno-utils-0.0.4/LICENSE` & `pheno-utils-0.0.5/LICENSE`

 * *Files identical despite different names*

### Comparing `pheno-utils-0.0.4/PKG-INFO` & `pheno-utils-0.0.5/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,52 +1,52 @@
 Metadata-Version: 2.1
 Name: pheno-utils
-Version: 0.0.4
+Version: 0.0.5
 Summary: Pheno data utils - viz, loaders, mergers
 Home-page: https://github.com/hrossman/pheno-utils
 Author: hrossman
 Author-email: hagairossman@gmail.com
 License: Apache Software License 2.0
+Description: pheno-utils
+        ================
+        
+        <!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->
+        
+        Viz functions, loaders, mergers.
+        
+        WORK IN PROGRESS
+        
+        ## Install
+        
+        ``` sh
+        pip install pheno_utils
+        ```
+        
+        ## How to use
+        
+        Examples:
+        
+        ``` python
+        data = generate_synthetic_data(n=1000)
+        hist_ecdf_plots(data=data, col="val1")
+        ```
+        
+            NameError: name 'hist_ecdf_plots' is not defined
+        
+        ``` python
+        age_refplots = GenderAgeRefPlot(data, "val1")
+        age_refplots.plot()
+        ```
+        
 Keywords: nbdev jupyter notebook python
+Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 Provides-Extra: dev
-License-File: LICENSE
-
-pheno-utils
-================
-
-<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->
-
-Viz functions, loaders, mergers.
-
-WORK IN PROGRESS
-
-## Install
-
-``` sh
-pip install pheno_utils
-```
-
-## How to use
-
-Examples:
-
-``` python
-data = generate_synthetic_data(n=1000)
-hist_ecdf_plots(data=data, col="val1")
-```
-
-    NameError: name 'hist_ecdf_plots' is not defined
-
-``` python
-age_refplots = GenderAgeRefPlot(data, "val1")
-age_refplots.plot()
-```
```

### Comparing `pheno-utils-0.0.4/pheno_utils/age_reference_plots.py` & `pheno-utils-0.0.5/pheno_utils/age_reference_plots.py`

 * *Files 0% similar despite different names*

```diff
@@ -309,15 +309,14 @@
         
         self.plot_scatter()
         self.plot_percentiles()
         self.plot_ornaments()
         self.plot_agehist()
         self.plot_valhist()
 
-
 # %% ../nbs/03_age_reference_plots.ipynb 7
 class GenderAgeRefPlot(AgeRefPlot):
     def __init__(
         self, 
         data: pd.DataFrame,
         val_col: str,
         age_col: str = "age_at_research_stage",
```

### Comparing `pheno-utils-0.0.4/pheno_utils/basic_plots.py` & `pheno-utils-0.0.5/pheno_utils/basic_plots.py`

 * *Files identical despite different names*

### Comparing `pheno-utils-0.0.4/pheno_utils/blandaltman_plots.py` & `pheno-utils-0.0.5/pheno_utils/blandaltman_plots.py`

 * *Files 0% similar despite different names*

```diff
@@ -67,8 +67,7 @@
     ax.set_xlabel(f"Mean of {m1.name} and {m2.name}")
     ax.set_ylabel(f"{m1.name} - {m2.name}")
 
     ax = axes[2]
     blandAltman(m1, m2, ax=ax, percentage=True)
     ax.set_xlabel(f"Mean of {m1.name} and {m2.name}")
     ax.set_ylabel(f"Percentage ({m1.name} - {m2.name})")
-
```

### Comparing `pheno-utils-0.0.4/pheno_utils/dates_plots.py` & `pheno-utils-0.0.5/pheno_utils/dates_plots.py`

 * *Files identical despite different names*

### Comparing `pheno-utils-0.0.4/pheno_utils.egg-info/PKG-INFO` & `pheno-utils-0.0.5/pheno_utils.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,52 +1,52 @@
 Metadata-Version: 2.1
 Name: pheno-utils
-Version: 0.0.4
+Version: 0.0.5
 Summary: Pheno data utils - viz, loaders, mergers
 Home-page: https://github.com/hrossman/pheno-utils
 Author: hrossman
 Author-email: hagairossman@gmail.com
 License: Apache Software License 2.0
+Description: pheno-utils
+        ================
+        
+        <!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->
+        
+        Viz functions, loaders, mergers.
+        
+        WORK IN PROGRESS
+        
+        ## Install
+        
+        ``` sh
+        pip install pheno_utils
+        ```
+        
+        ## How to use
+        
+        Examples:
+        
+        ``` python
+        data = generate_synthetic_data(n=1000)
+        hist_ecdf_plots(data=data, col="val1")
+        ```
+        
+            NameError: name 'hist_ecdf_plots' is not defined
+        
+        ``` python
+        age_refplots = GenderAgeRefPlot(data, "val1")
+        age_refplots.plot()
+        ```
+        
 Keywords: nbdev jupyter notebook python
+Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Natural Language :: English
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
 Classifier: License :: OSI Approved :: Apache Software License
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 Provides-Extra: dev
-License-File: LICENSE
-
-pheno-utils
-================
-
-<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->
-
-Viz functions, loaders, mergers.
-
-WORK IN PROGRESS
-
-## Install
-
-``` sh
-pip install pheno_utils
-```
-
-## How to use
-
-Examples:
-
-``` python
-data = generate_synthetic_data(n=1000)
-hist_ecdf_plots(data=data, col="val1")
-```
-
-    NameError: name 'hist_ecdf_plots' is not defined
-
-``` python
-age_refplots = GenderAgeRefPlot(data, "val1")
-age_refplots.plot()
-```
```

### Comparing `pheno-utils-0.0.4/settings.ini` & `pheno-utils-0.0.5/settings.ini`

 * *Files 3% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 [DEFAULT]
 # All sections below are required unless otherwise specified.
 # See https://github.com/fastai/nbdev/blob/master/settings.ini for examples.
 
 ### Python library ###
 repo = pheno-utils
 lib_name = %(repo)s
-version = 0.0.4
+version = 0.0.5
 min_python = 3.7
 license = apache2
 black_formatting = False
 
 ### nbdev ###
 doc_path = _docs
 lib_path = pheno_utils
@@ -34,10 +34,10 @@
 description = Pheno data utils - viz, loaders, mergers
 keywords = nbdev jupyter notebook python
 language = English
 status = 3
 user = hrossman
 
 ### Optional ###
-requirements = fastcore numpy scipy pandas matplotlib seaborn scikit-learn pyCompare tsmoothie
+requirements = fastcore numpy scipy pandas fastparquet matplotlib seaborn scikit-learn pyCompare tsmoothie
 # dev_requirements = 
 # console_scripts =
```

### Comparing `pheno-utils-0.0.4/setup.py` & `pheno-utils-0.0.5/setup.py`

 * *Files identical despite different names*

