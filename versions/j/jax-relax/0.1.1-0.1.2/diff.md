# Comparing `tmp/jax-relax-0.1.1.tar.gz` & `tmp/jax-relax-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/jax-relax-0.1.1.tar", last modified: Sat Feb  4 20:03:35 2023, max compression
+gzip compressed data, was "dist/jax-relax-0.1.2.tar", last modified: Thu Apr  6 20:59:29 2023, max compression
```

## Comparing `jax-relax-0.1.1.tar` & `jax-relax-0.1.2.tar`

### file list

```diff
@@ -1,39 +1,42 @@
-drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-02-04 20:03:35.000000 jax-relax-0.1.1/
--rw-r--r--   0 birk      (1000) birk      (1000)     2348 2022-12-18 21:09:02.000000 jax-relax-0.1.1/CONTRIBUTING.md
--rw-r--r--   0 birk      (1000) birk      (1000)    11357 2022-12-18 21:09:02.000000 jax-relax-0.1.1/LICENSE
--rw-r--r--   0 birk      (1000) birk      (1000)      111 2022-12-18 21:09:02.000000 jax-relax-0.1.1/MANIFEST.in
--rw-r--r--   0 birk      (1000) birk      (1000)     3062 2023-02-04 20:03:35.000000 jax-relax-0.1.1/PKG-INFO
--rw-r--r--   0 birk      (1000) birk      (1000)     2222 2023-02-04 19:44:27.000000 jax-relax-0.1.1/README.md
-drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-02-04 20:03:35.000000 jax-relax-0.1.1/jax_relax.egg-info/
--rw-r--r--   0 birk      (1000) birk      (1000)     3062 2023-02-04 20:03:35.000000 jax-relax-0.1.1/jax_relax.egg-info/PKG-INFO
--rw-r--r--   0 birk      (1000) birk      (1000)      695 2023-02-04 20:03:35.000000 jax-relax-0.1.1/jax_relax.egg-info/SOURCES.txt
--rw-r--r--   0 birk      (1000) birk      (1000)        1 2023-02-04 20:03:35.000000 jax-relax-0.1.1/jax_relax.egg-info/dependency_links.txt
--rw-r--r--   0 birk      (1000) birk      (1000)       32 2023-02-04 20:03:35.000000 jax-relax-0.1.1/jax_relax.egg-info/entry_points.txt
--rw-r--r--   0 birk      (1000) birk      (1000)        1 2022-12-19 10:47:31.000000 jax-relax-0.1.1/jax_relax.egg-info/not-zip-safe
--rw-r--r--   0 birk      (1000) birk      (1000)      143 2023-02-04 20:03:35.000000 jax-relax-0.1.1/jax_relax.egg-info/requires.txt
--rw-r--r--   0 birk      (1000) birk      (1000)        6 2023-02-04 20:03:35.000000 jax-relax-0.1.1/jax_relax.egg-info/top_level.txt
-drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-02-04 20:03:35.000000 jax-relax-0.1.1/relax/
--rw-r--r--   0 birk      (1000) birk      (1000)       21 2023-02-04 19:44:10.000000 jax-relax-0.1.1/relax/__init__.py
--rw-r--r--   0 birk      (1000) birk      (1000)     3855 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/_ckpt_manager.py
--rw-r--r--   0 birk      (1000) birk      (1000)    51997 2023-02-04 19:44:10.000000 jax-relax-0.1.1/relax/_modidx.py
-drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-02-04 20:03:35.000000 jax-relax-0.1.1/relax/data/
--rw-r--r--   0 birk      (1000) birk      (1000)      115 2023-02-04 19:44:10.000000 jax-relax-0.1.1/relax/data/__init__.py
--rw-r--r--   0 birk      (1000) birk      (1000)     7842 2023-02-04 19:44:10.000000 jax-relax-0.1.1/relax/data/loader.py
--rw-r--r--   0 birk      (1000) birk      (1000)    15164 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/data/module.py
--rw-r--r--   0 birk      (1000) birk      (1000)    13580 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/evaluate.py
--rw-r--r--   0 birk      (1000) birk      (1000)     1204 2023-01-18 19:20:24.000000 jax-relax-0.1.1/relax/import_essentials.py
--rw-r--r--   0 birk      (1000) birk      (1000)     1985 2023-02-04 19:44:10.000000 jax-relax-0.1.1/relax/logger.py
-drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-02-04 20:03:35.000000 jax-relax-0.1.1/relax/methods/
--rw-r--r--   0 birk      (1000) birk      (1000)      192 2023-02-04 19:44:10.000000 jax-relax-0.1.1/relax/methods/__init__.py
--rw-r--r--   0 birk      (1000) birk      (1000)     1903 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/methods/base.py
--rw-r--r--   0 birk      (1000) birk      (1000)    12120 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/methods/counternet.py
--rw-r--r--   0 birk      (1000) birk      (1000)     6307 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/methods/diverse.py
--rw-r--r--   0 birk      (1000) birk      (1000)     9255 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/methods/proto.py
--rw-r--r--   0 birk      (1000) birk      (1000)     3963 2023-02-04 19:44:10.000000 jax-relax-0.1.1/relax/methods/vanilla.py
--rw-r--r--   0 birk      (1000) birk      (1000)     7400 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/module.py
--rw-r--r--   0 birk      (1000) birk      (1000)     4797 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/plots.py
--rw-r--r--   0 birk      (1000) birk      (1000)     4736 2023-02-04 19:44:10.000000 jax-relax-0.1.1/relax/trainer.py
--rw-r--r--   0 birk      (1000) birk      (1000)     6761 2023-02-04 19:44:09.000000 jax-relax-0.1.1/relax/utils.py
--rw-r--r--   0 birk      (1000) birk      (1000)     1007 2023-02-04 19:44:04.000000 jax-relax-0.1.1/settings.ini
--rw-r--r--   0 birk      (1000) birk      (1000)       38 2023-02-04 20:03:35.000000 jax-relax-0.1.1/setup.cfg
--rw-r--r--   0 birk      (1000) birk      (1000)     2541 2022-12-18 21:09:02.000000 jax-relax-0.1.1/setup.py
+drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-04-06 20:59:29.000000 jax-relax-0.1.2/
+-rw-r--r--   0 birk      (1000) birk      (1000)     2348 2022-12-18 21:09:02.000000 jax-relax-0.1.2/CONTRIBUTING.md
+-rw-r--r--   0 birk      (1000) birk      (1000)    11357 2022-12-18 21:09:02.000000 jax-relax-0.1.2/LICENSE
+-rw-r--r--   0 birk      (1000) birk      (1000)      111 2022-12-18 21:09:02.000000 jax-relax-0.1.2/MANIFEST.in
+-rw-r--r--   0 birk      (1000) birk      (1000)     3128 2023-04-06 20:59:29.000000 jax-relax-0.1.2/PKG-INFO
+-rw-r--r--   0 birk      (1000) birk      (1000)     2288 2023-02-08 15:53:10.000000 jax-relax-0.1.2/README.md
+drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-04-06 20:59:29.000000 jax-relax-0.1.2/jax_relax.egg-info/
+-rw-r--r--   0 birk      (1000) birk      (1000)     3128 2023-04-06 20:59:28.000000 jax-relax-0.1.2/jax_relax.egg-info/PKG-INFO
+-rw-r--r--   0 birk      (1000) birk      (1000)      751 2023-04-06 20:59:28.000000 jax-relax-0.1.2/jax_relax.egg-info/SOURCES.txt
+-rw-r--r--   0 birk      (1000) birk      (1000)        1 2023-04-06 20:59:28.000000 jax-relax-0.1.2/jax_relax.egg-info/dependency_links.txt
+-rw-r--r--   0 birk      (1000) birk      (1000)       32 2023-04-06 20:59:28.000000 jax-relax-0.1.2/jax_relax.egg-info/entry_points.txt
+-rw-r--r--   0 birk      (1000) birk      (1000)        1 2022-12-19 10:47:31.000000 jax-relax-0.1.2/jax_relax.egg-info/not-zip-safe
+-rw-r--r--   0 birk      (1000) birk      (1000)      188 2023-04-06 20:59:28.000000 jax-relax-0.1.2/jax_relax.egg-info/requires.txt
+-rw-r--r--   0 birk      (1000) birk      (1000)        6 2023-04-06 20:59:28.000000 jax-relax-0.1.2/jax_relax.egg-info/top_level.txt
+drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-04-06 20:59:29.000000 jax-relax-0.1.2/relax/
+-rw-r--r--   0 birk      (1000) birk      (1000)       21 2023-04-06 20:59:06.000000 jax-relax-0.1.2/relax/__init__.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     3855 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/_ckpt_manager.py
+-rw-r--r--   0 birk      (1000) birk      (1000)    62848 2023-04-06 20:59:06.000000 jax-relax-0.1.2/relax/_modidx.py
+drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-04-06 20:59:29.000000 jax-relax-0.1.2/relax/data/
+-rw-r--r--   0 birk      (1000) birk      (1000)      115 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/data/__init__.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     7842 2023-04-06 14:30:59.000000 jax-relax-0.1.2/relax/data/loader.py
+-rw-r--r--   0 birk      (1000) birk      (1000)    17786 2023-04-06 14:30:59.000000 jax-relax-0.1.2/relax/data/module.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     9776 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/data/scm.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     6199 2023-04-06 14:30:59.000000 jax-relax-0.1.2/relax/docs.py
+-rw-r--r--   0 birk      (1000) birk      (1000)    15209 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/evaluate.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     1262 2023-04-06 20:59:06.000000 jax-relax-0.1.2/relax/import_essentials.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     1985 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/logger.py
+drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-04-06 20:59:29.000000 jax-relax-0.1.2/relax/methods/
+-rw-r--r--   0 birk      (1000) birk      (1000)      192 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/methods/__init__.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     1903 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/methods/base.py
+-rw-r--r--   0 birk      (1000) birk      (1000)    12118 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/methods/counternet.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     6307 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/methods/diverse.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     9255 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/methods/proto.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     7475 2023-04-06 20:59:06.000000 jax-relax-0.1.2/relax/methods/sphere.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     3963 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/methods/vanilla.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     7583 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/module.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     4797 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/plots.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     4736 2023-04-06 14:31:00.000000 jax-relax-0.1.2/relax/trainer.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     6761 2023-04-06 14:30:59.000000 jax-relax-0.1.2/relax/utils.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     1101 2023-04-06 20:59:06.000000 jax-relax-0.1.2/settings.ini
+-rw-r--r--   0 birk      (1000) birk      (1000)       38 2023-04-06 20:59:29.000000 jax-relax-0.1.2/setup.cfg
+-rw-r--r--   0 birk      (1000) birk      (1000)     2541 2022-12-18 21:09:02.000000 jax-relax-0.1.2/setup.py
```

### Comparing `jax-relax-0.1.1/CONTRIBUTING.md` & `jax-relax-0.1.2/CONTRIBUTING.md`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/LICENSE` & `jax-relax-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/PKG-INFO` & `jax-relax-0.1.2/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jax-relax
-Version: 0.1.1
+Version: 0.1.2
 Summary: Jax-based Recourse Explanation Library
 Home-page: https://github.com/birkhoffg/relax/tree/master/
 Author: BirkhoffG
 Author-email: 26811230+BirkhoffG@users.noreply.github.com
 License: Apache Software License 2.0
 Keywords: Jax,Recourse,Explanation,Interpretability,Machine Learning
 Classifier: Development Status :: 3 - Alpha
@@ -28,15 +28,15 @@
 ![Python](https://img.shields.io/pypi/pyversions/jax-relax.svg) ![CI
 status](https://github.com/BirkhoffG/ReLax/actions/workflows/test.yaml/badge.svg)
 ![Docs](https://github.com/BirkhoffG/ReLax/actions/workflows/deploy.yaml/badge.svg)
 ![pypi](https://img.shields.io/pypi/v/jax-relax.svg) ![GitHub
 License](https://img.shields.io/github/license/BirkhoffG/ReLax.svg)
 
 [**Overview**](#overview) \| [**Installation**](#installation) \|
-[**Tutorials**](tutorials/getting_started.ipynb) \|
+[**Tutorials**](https://birkhoffg.github.io/ReLax/tutorials/getting_started.html) \|
 [**Documentation**](https://birkhoffg.github.io/ReLax/) \| [**Citing
 ReLax**](#citing-relax)
 
 ## Overview
 
 `ReLax` (**Re**course Explanation **L**ibrary in J**ax**) is a library
 built on top of `jax` to generate counterfactual and recourse
@@ -73,15 +73,15 @@
 to first install this library via `pip install jax-relax`. Then, follow
 steps in the [official install
 guidelines](https://github.com/google/jax#installation) to install the
 right version for GPU or TPU.
 
 ## An Example of using `ReLax`
 
-See [Getting Started with ReLax](tutorials/getting_started.ipynb).
+See [Getting Started with ReLax](https://birkhoffg.github.io/ReLax/tutorials/getting_started.html).
 
 ## Citing `ReLax`
 
 To cite this repository:
 
 ``` latex
 @software{relax2023github,
```

### Comparing `jax-relax-0.1.1/README.md` & `jax-relax-0.1.2/README.md`

 * *Files 6% similar despite different names*

```diff
@@ -6,15 +6,15 @@
 ![Python](https://img.shields.io/pypi/pyversions/jax-relax.svg) ![CI
 status](https://github.com/BirkhoffG/ReLax/actions/workflows/test.yaml/badge.svg)
 ![Docs](https://github.com/BirkhoffG/ReLax/actions/workflows/deploy.yaml/badge.svg)
 ![pypi](https://img.shields.io/pypi/v/jax-relax.svg) ![GitHub
 License](https://img.shields.io/github/license/BirkhoffG/ReLax.svg)
 
 [**Overview**](#overview) \| [**Installation**](#installation) \|
-[**Tutorials**](tutorials/getting_started.ipynb) \|
+[**Tutorials**](https://birkhoffg.github.io/ReLax/tutorials/getting_started.html) \|
 [**Documentation**](https://birkhoffg.github.io/ReLax/) \| [**Citing
 ReLax**](#citing-relax)
 
 ## Overview
 
 `ReLax` (**Re**course Explanation **L**ibrary in J**ax**) is a library
 built on top of `jax` to generate counterfactual and recourse
@@ -51,15 +51,15 @@
 to first install this library via `pip install jax-relax`. Then, follow
 steps in the [official install
 guidelines](https://github.com/google/jax#installation) to install the
 right version for GPU or TPU.
 
 ## An Example of using `ReLax`
 
-See [Getting Started with ReLax](tutorials/getting_started.ipynb).
+See [Getting Started with ReLax](https://birkhoffg.github.io/ReLax/tutorials/getting_started.html).
 
 ## Citing `ReLax`
 
 To cite this repository:
 
 ``` latex
 @software{relax2023github,
```

### Comparing `jax-relax-0.1.1/jax_relax.egg-info/PKG-INFO` & `jax-relax-0.1.2/jax_relax.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jax-relax
-Version: 0.1.1
+Version: 0.1.2
 Summary: Jax-based Recourse Explanation Library
 Home-page: https://github.com/birkhoffg/relax/tree/master/
 Author: BirkhoffG
 Author-email: 26811230+BirkhoffG@users.noreply.github.com
 License: Apache Software License 2.0
 Keywords: Jax,Recourse,Explanation,Interpretability,Machine Learning
 Classifier: Development Status :: 3 - Alpha
@@ -28,15 +28,15 @@
 ![Python](https://img.shields.io/pypi/pyversions/jax-relax.svg) ![CI
 status](https://github.com/BirkhoffG/ReLax/actions/workflows/test.yaml/badge.svg)
 ![Docs](https://github.com/BirkhoffG/ReLax/actions/workflows/deploy.yaml/badge.svg)
 ![pypi](https://img.shields.io/pypi/v/jax-relax.svg) ![GitHub
 License](https://img.shields.io/github/license/BirkhoffG/ReLax.svg)
 
 [**Overview**](#overview) \| [**Installation**](#installation) \|
-[**Tutorials**](tutorials/getting_started.ipynb) \|
+[**Tutorials**](https://birkhoffg.github.io/ReLax/tutorials/getting_started.html) \|
 [**Documentation**](https://birkhoffg.github.io/ReLax/) \| [**Citing
 ReLax**](#citing-relax)
 
 ## Overview
 
 `ReLax` (**Re**course Explanation **L**ibrary in J**ax**) is a library
 built on top of `jax` to generate counterfactual and recourse
@@ -73,15 +73,15 @@
 to first install this library via `pip install jax-relax`. Then, follow
 steps in the [official install
 guidelines](https://github.com/google/jax#installation) to install the
 right version for GPU or TPU.
 
 ## An Example of using `ReLax`
 
-See [Getting Started with ReLax](tutorials/getting_started.ipynb).
+See [Getting Started with ReLax](https://birkhoffg.github.io/ReLax/tutorials/getting_started.html).
 
 ## Citing `ReLax`
 
 To cite this repository:
 
 ``` latex
 @software{relax2023github,
```

### Comparing `jax-relax-0.1.1/jax_relax.egg-info/SOURCES.txt` & `jax-relax-0.1.2/jax_relax.egg-info/SOURCES.txt`

 * *Files 18% similar despite different names*

```diff
@@ -10,23 +10,26 @@
 jax_relax.egg-info/entry_points.txt
 jax_relax.egg-info/not-zip-safe
 jax_relax.egg-info/requires.txt
 jax_relax.egg-info/top_level.txt
 relax/__init__.py
 relax/_ckpt_manager.py
 relax/_modidx.py
+relax/docs.py
 relax/evaluate.py
 relax/import_essentials.py
 relax/logger.py
 relax/module.py
 relax/plots.py
 relax/trainer.py
 relax/utils.py
 relax/data/__init__.py
 relax/data/loader.py
 relax/data/module.py
+relax/data/scm.py
 relax/methods/__init__.py
 relax/methods/base.py
 relax/methods/counternet.py
 relax/methods/diverse.py
 relax/methods/proto.py
+relax/methods/sphere.py
 relax/methods/vanilla.py
```

### Comparing `jax-relax-0.1.1/relax/_ckpt_manager.py` & `jax-relax-0.1.2/relax/_ckpt_manager.py`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/relax/_modidx.py` & `jax-relax-0.1.2/relax/_modidx.py`

 * *Files 10% similar despite different names*

```diff
@@ -87,14 +87,16 @@
                                    'relax.data.module.BaseDataModule.val_dataloader': ( 'data.module.html#basedatamodule.val_dataloader',
                                                                                         'relax/data/module.py'),
                                    'relax.data.module.BaseDataModule.val_dataset': ( 'data.module.html#basedatamodule.val_dataset',
                                                                                      'relax/data/module.py'),
                                    'relax.data.module.TabularDataModule': ('data.module.html#tabulardatamodule', 'relax/data/module.py'),
                                    'relax.data.module.TabularDataModule.__init__': ( 'data.module.html#tabulardatamodule.__init__',
                                                                                      'relax/data/module.py'),
+                                   'relax.data.module.TabularDataModule.__setattr__': ( 'data.module.html#tabulardatamodule.__setattr__',
+                                                                                        'relax/data/module.py'),
                                    'relax.data.module.TabularDataModule.apply_constraints': ( 'data.module.html#tabulardatamodule.apply_constraints',
                                                                                               'relax/data/module.py'),
                                    'relax.data.module.TabularDataModule.apply_regularization': ( 'data.module.html#tabulardatamodule.apply_regularization',
                                                                                                  'relax/data/module.py'),
                                    'relax.data.module.TabularDataModule.data': ( 'data.module.html#tabulardatamodule.data',
                                                                                  'relax/data/module.py'),
                                    'relax.data.module.TabularDataModule.data_name': ( 'data.module.html#tabulardatamodule.data_name',
@@ -117,54 +119,127 @@
                                                                                       'relax/data/module.py'),
                                    'relax.data.module.TabularDataModule.val_dataloader': ( 'data.module.html#tabulardatamodule.val_dataloader',
                                                                                            'relax/data/module.py'),
                                    'relax.data.module.TabularDataModule.val_dataset': ( 'data.module.html#tabulardatamodule.val_dataset',
                                                                                         'relax/data/module.py'),
                                    'relax.data.module.TabularDataModuleConfigs': ( 'data.module.html#tabulardatamoduleconfigs',
                                                                                    'relax/data/module.py'),
+                                   'relax.data.module.TabularDataModuleConfigs.Config': ( 'data.module.html#tabulardatamoduleconfigs.config',
+                                                                                          'relax/data/module.py'),
+                                   'relax.data.module.TransformerMixinType': ( 'data.module.html#transformermixintype',
+                                                                               'relax/data/module.py'),
+                                   'relax.data.module.TransformerMixinType.__get_validators__': ( 'data.module.html#transformermixintype.__get_validators__',
+                                                                                                  'relax/data/module.py'),
+                                   'relax.data.module.TransformerMixinType.__modify_schema__': ( 'data.module.html#transformermixintype.__modify_schema__',
+                                                                                                 'relax/data/module.py'),
+                                   'relax.data.module.TransformerMixinType.validate': ( 'data.module.html#transformermixintype.validate',
+                                                                                        'relax/data/module.py'),
                                    'relax.data.module._check_cols': ('data.module.html#_check_cols', 'relax/data/module.py'),
                                    'relax.data.module._init_scalar_encoder': ( 'data.module.html#_init_scalar_encoder',
                                                                                'relax/data/module.py'),
                                    'relax.data.module._inverse_transform_np': ( 'data.module.html#_inverse_transform_np',
                                                                                 'relax/data/module.py'),
                                    'relax.data.module._process_data': ('data.module.html#_process_data', 'relax/data/module.py'),
                                    'relax.data.module._supported_backends': ( 'data.module.html#_supported_backends',
                                                                               'relax/data/module.py'),
                                    'relax.data.module._transform_df': ('data.module.html#_transform_df', 'relax/data/module.py'),
                                    'relax.data.module._validate_dataname': ('data.module.html#_validate_dataname', 'relax/data/module.py'),
                                    'relax.data.module.find_imutable_idx_list': ( 'data.module.html#find_imutable_idx_list',
                                                                                  'relax/data/module.py'),
                                    'relax.data.module.load_data': ('data.module.html#load_data', 'relax/data/module.py'),
                                    'relax.data.module.sample': ('data.module.html#sample', 'relax/data/module.py')},
+            'relax.data.scm': { 'relax.data.scm.BaseDistribution': ('data.scm.html#basedistribution', 'relax/data/scm.py'),
+                                'relax.data.scm.BaseDistribution.__init__': ( 'data.scm.html#basedistribution.__init__',
+                                                                              'relax/data/scm.py'),
+                                'relax.data.scm.BaseDistribution.pdf': ('data.scm.html#basedistribution.pdf', 'relax/data/scm.py'),
+                                'relax.data.scm.BaseDistribution.sample': ('data.scm.html#basedistribution.sample', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel': ('data.scm.html#causalmodel', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.__init__': ('data.scm.html#causalmodel.__init__', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.cgm': ('data.scm.html#causalmodel.cgm', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.endogenous': ('data.scm.html#causalmodel.endogenous', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.exogenous': ('data.scm.html#causalmodel.exogenous', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.get_ancestors': ( 'data.scm.html#causalmodel.get_ancestors',
+                                                                              'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.get_children': ('data.scm.html#causalmodel.get_children', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.get_descendants': ( 'data.scm.html#causalmodel.get_descendants',
+                                                                                'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.get_non_descendants': ( 'data.scm.html#causalmodel.get_non_descendants',
+                                                                                    'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.get_parents': ('data.scm.html#causalmodel.get_parents', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.get_topological_ordering': ( 'data.scm.html#causalmodel.get_topological_ordering',
+                                                                                         'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.noise_distributions': ( 'data.scm.html#causalmodel.noise_distributions',
+                                                                                    'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.scm': ('data.scm.html#causalmodel.scm', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.scm_class': ('data.scm.html#causalmodel.scm_class', 'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.structural_equations': ( 'data.scm.html#causalmodel.structural_equations',
+                                                                                     'relax/data/scm.py'),
+                                'relax.data.scm.CausalModel.visualize': ('data.scm.html#causalmodel.visualize', 'relax/data/scm.py'),
+                                'relax.data.scm.MixtureOfGaussians': ('data.scm.html#mixtureofgaussians', 'relax/data/scm.py'),
+                                'relax.data.scm.MixtureOfGaussians.__init__': ( 'data.scm.html#mixtureofgaussians.__init__',
+                                                                                'relax/data/scm.py'),
+                                'relax.data.scm.MixtureOfGaussians.pdf': ('data.scm.html#mixtureofgaussians.pdf', 'relax/data/scm.py'),
+                                'relax.data.scm.MixtureOfGaussians.sample': ( 'data.scm.html#mixtureofgaussians.sample',
+                                                                              'relax/data/scm.py'),
+                                'relax.data.scm.Normal': ('data.scm.html#normal', 'relax/data/scm.py'),
+                                'relax.data.scm.Normal.__init__': ('data.scm.html#normal.__init__', 'relax/data/scm.py'),
+                                'relax.data.scm.Normal.pdf': ('data.scm.html#normal.pdf', 'relax/data/scm.py'),
+                                'relax.data.scm.Normal.sample': ('data.scm.html#normal.sample', 'relax/data/scm.py'),
+                                'relax.data.scm._create_synthetic_data': ('data.scm.html#_create_synthetic_data', 'relax/data/scm.py'),
+                                'relax.data.scm._get_noise_string': ('data.scm.html#_get_noise_string', 'relax/data/scm.py'),
+                                'relax.data.scm._load_scm_equations': ('data.scm.html#_load_scm_equations', 'relax/data/scm.py'),
+                                'relax.data.scm.sanity_3_lin': ('data.scm.html#sanity_3_lin', 'relax/data/scm.py')},
+            'relax.docs': { 'relax.docs.CalloutDocument': ('docs.html#calloutdocument', 'relax/docs.py'),
+                            'relax.docs.CalloutDocument.__init__': ('docs.html#calloutdocument.__init__', 'relax/docs.py'),
+                            'relax.docs.CalloutDocument._repre_mardown': ('docs.html#calloutdocument._repre_mardown', 'relax/docs.py'),
+                            'relax.docs.CustomizedMarkdownRenderer': ('docs.html#customizedmarkdownrenderer', 'relax/docs.py'),
+                            'relax.docs.CustomizedMarkdownRenderer.__init__': ( 'docs.html#customizedmarkdownrenderer.__init__',
+                                                                                'relax/docs.py'),
+                            'relax.docs.CustomizedMarkdownRenderer._check_sym': ( 'docs.html#customizedmarkdownrenderer._check_sym',
+                                                                                  'relax/docs.py'),
+                            'relax.docs.CustomizedMarkdownRenderer._repr_markdown_': ( 'docs.html#customizedmarkdownrenderer._repr_markdown_',
+                                                                                       'relax/docs.py'),
+                            'relax.docs.ParserMarkdownRenderer': ('docs.html#parsermarkdownrenderer', 'relax/docs.py'),
+                            'relax.docs.ParserMarkdownRenderer.__init__': ('docs.html#parsermarkdownrenderer.__init__', 'relax/docs.py'),
+                            'relax.docs._bold': ('docs.html#_bold', 'relax/docs.py'),
+                            'relax.docs._docment_parser': ('docs.html#_docment_parser', 'relax/docs.py'),
+                            'relax.docs._fmt_sig': ('docs.html#_fmt_sig', 'relax/docs.py'),
+                            'relax.docs._inner_list2mdlist': ('docs.html#_inner_list2mdlist', 'relax/docs.py'),
+                            'relax.docs._italic': ('docs.html#_italic', 'relax/docs.py'),
+                            'relax.docs._params_mdlist': ('docs.html#_params_mdlist', 'relax/docs.py'),
+                            'relax.docs._return_mdlist': ('docs.html#_return_mdlist', 'relax/docs.py'),
+                            'relax.docs._show_param': ('docs.html#_show_param', 'relax/docs.py'),
+                            'relax.docs._show_params_return': ('docs.html#_show_params_return', 'relax/docs.py')},
             'relax.evaluate': { 'relax.evaluate.BaseEvalMetrics': ('evaluate.html#baseevalmetrics', 'relax/evaluate.py'),
                                 'relax.evaluate.BaseEvalMetrics.__call__': ('evaluate.html#baseevalmetrics.__call__', 'relax/evaluate.py'),
+                                'relax.evaluate.BaseEvalMetrics.__init__': ('evaluate.html#baseevalmetrics.__init__', 'relax/evaluate.py'),
                                 'relax.evaluate.BaseEvalMetrics.__str__': ('evaluate.html#baseevalmetrics.__str__', 'relax/evaluate.py'),
                                 'relax.evaluate.Explanation': ('evaluate.html#explanation', 'relax/evaluate.py'),
                                 'relax.evaluate.Explanation.__post_init__': ( 'evaluate.html#explanation.__post_init__',
                                                                               'relax/evaluate.py'),
                                 'relax.evaluate.ManifoldDist': ('evaluate.html#manifolddist', 'relax/evaluate.py'),
                                 'relax.evaluate.ManifoldDist.__call__': ('evaluate.html#manifolddist.__call__', 'relax/evaluate.py'),
                                 'relax.evaluate.ManifoldDist.__init__': ('evaluate.html#manifolddist.__init__', 'relax/evaluate.py'),
-                                'relax.evaluate.ManifoldDist.__str__': ('evaluate.html#manifolddist.__str__', 'relax/evaluate.py'),
                                 'relax.evaluate.PredictiveAccuracy': ('evaluate.html#predictiveaccuracy', 'relax/evaluate.py'),
                                 'relax.evaluate.PredictiveAccuracy.__call__': ( 'evaluate.html#predictiveaccuracy.__call__',
                                                                                 'relax/evaluate.py'),
-                                'relax.evaluate.PredictiveAccuracy.__str__': ( 'evaluate.html#predictiveaccuracy.__str__',
-                                                                               'relax/evaluate.py'),
+                                'relax.evaluate.PredictiveAccuracy.__init__': ( 'evaluate.html#predictiveaccuracy.__init__',
+                                                                                'relax/evaluate.py'),
                                 'relax.evaluate.Proximity': ('evaluate.html#proximity', 'relax/evaluate.py'),
                                 'relax.evaluate.Proximity.__call__': ('evaluate.html#proximity.__call__', 'relax/evaluate.py'),
-                                'relax.evaluate.Proximity.__str__': ('evaluate.html#proximity.__str__', 'relax/evaluate.py'),
+                                'relax.evaluate.Proximity.__init__': ('evaluate.html#proximity.__init__', 'relax/evaluate.py'),
                                 'relax.evaluate.Runtime': ('evaluate.html#runtime', 'relax/evaluate.py'),
                                 'relax.evaluate.Runtime.__call__': ('evaluate.html#runtime.__call__', 'relax/evaluate.py'),
+                                'relax.evaluate.Runtime.__init__': ('evaluate.html#runtime.__init__', 'relax/evaluate.py'),
                                 'relax.evaluate.Sparsity': ('evaluate.html#sparsity', 'relax/evaluate.py'),
                                 'relax.evaluate.Sparsity.__call__': ('evaluate.html#sparsity.__call__', 'relax/evaluate.py'),
-                                'relax.evaluate.Sparsity.__str__': ('evaluate.html#sparsity.__str__', 'relax/evaluate.py'),
+                                'relax.evaluate.Sparsity.__init__': ('evaluate.html#sparsity.__init__', 'relax/evaluate.py'),
                                 'relax.evaluate.Validity': ('evaluate.html#validity', 'relax/evaluate.py'),
                                 'relax.evaluate.Validity.__call__': ('evaluate.html#validity.__call__', 'relax/evaluate.py'),
-                                'relax.evaluate.Validity.__str__': ('evaluate.html#validity.__str__', 'relax/evaluate.py'),
+                                'relax.evaluate.Validity.__init__': ('evaluate.html#validity.__init__', 'relax/evaluate.py'),
                                 'relax.evaluate._AuxPredFn': ('evaluate.html#_auxpredfn', 'relax/evaluate.py'),
                                 'relax.evaluate._AuxPredFn.__call__': ('evaluate.html#_auxpredfn.__call__', 'relax/evaluate.py'),
                                 'relax.evaluate._AuxPredFn.__init__': ('evaluate.html#_auxpredfn.__init__', 'relax/evaluate.py'),
                                 'relax.evaluate._check_aux_pred_fn_args': ('evaluate.html#_check_aux_pred_fn_args', 'relax/evaluate.py'),
                                 'relax.evaluate._check_pred_fn': ('evaluate.html#_check_pred_fn', 'relax/evaluate.py'),
                                 'relax.evaluate._compute_acc': ('evaluate.html#_compute_acc', 'relax/evaluate.py'),
                                 'relax.evaluate._compute_manifold_dist': ('evaluate.html#_compute_manifold_dist', 'relax/evaluate.py'),
@@ -176,14 +251,15 @@
                                 'relax.evaluate._train_parametric_module': ('evaluate.html#_train_parametric_module', 'relax/evaluate.py'),
                                 'relax.evaluate._validate_configs': ('evaluate.html#_validate_configs', 'relax/evaluate.py'),
                                 'relax.evaluate.benchmark_cfs': ('evaluate.html#benchmark_cfs', 'relax/evaluate.py'),
                                 'relax.evaluate.compute_so_proximity': ('evaluate.html#compute_so_proximity', 'relax/evaluate.py'),
                                 'relax.evaluate.compute_so_sparsity': ('evaluate.html#compute_so_sparsity', 'relax/evaluate.py'),
                                 'relax.evaluate.compute_so_validity': ('evaluate.html#compute_so_validity', 'relax/evaluate.py'),
                                 'relax.evaluate.evaluate_cfs': ('evaluate.html#evaluate_cfs', 'relax/evaluate.py'),
+                                'relax.evaluate.fake_explanations': ('evaluate.html#fake_explanations', 'relax/evaluate.py'),
                                 'relax.evaluate.generate_cf_explanations': ('evaluate.html#generate_cf_explanations', 'relax/evaluate.py')},
             'relax.import_essentials': {},
             'relax.logger': { 'relax.logger.TensorboardLogger': ('logger.html#tensorboardlogger', 'relax/logger.py'),
                               'relax.logger.TensorboardLogger.__init__': ('logger.html#tensorboardlogger.__init__', 'relax/logger.py'),
                               'relax.logger.TensorboardLogger.close': ('logger.html#tensorboardlogger.close', 'relax/logger.py'),
                               'relax.logger.TensorboardLogger.get_last_logs': ( 'logger.html#tensorboardlogger.get_last_logs',
                                                                                 'relax/logger.py'),
@@ -327,14 +403,27 @@
                                      'relax.methods.proto.ProtoCF.generate_cfs': ( 'methods.prototype.html#protocf.generate_cfs',
                                                                                    'relax/methods/proto.py'),
                                      'relax.methods.proto.ProtoCF.train': ( 'methods.prototype.html#protocf.train',
                                                                             'relax/methods/proto.py'),
                                      'relax.methods.proto.ProtoCFConfig': ( 'methods.prototype.html#protocfconfig',
                                                                             'relax/methods/proto.py'),
                                      'relax.methods.proto._proto_cf': ('methods.prototype.html#_proto_cf', 'relax/methods/proto.py')},
+            'relax.methods.sphere': { 'relax.methods.sphere.GSConfig': ('sphere.html#gsconfig', 'relax/methods/sphere.py'),
+                                      'relax.methods.sphere.GrowingSphere': ('sphere.html#growingsphere', 'relax/methods/sphere.py'),
+                                      'relax.methods.sphere.GrowingSphere.__init__': ( 'sphere.html#growingsphere.__init__',
+                                                                                       'relax/methods/sphere.py'),
+                                      'relax.methods.sphere.GrowingSphere.generate_cf': ( 'sphere.html#growingsphere.generate_cf',
+                                                                                          'relax/methods/sphere.py'),
+                                      'relax.methods.sphere.GrowingSphere.generate_cfs': ( 'sphere.html#growingsphere.generate_cfs',
+                                                                                           'relax/methods/sphere.py'),
+                                      'relax.methods.sphere._growing_spheres': ('sphere.html#_growing_spheres', 'relax/methods/sphere.py'),
+                                      'relax.methods.sphere.apply_immutable': ('sphere.html#apply_immutable', 'relax/methods/sphere.py'),
+                                      'relax.methods.sphere.cat_sample': ('sphere.html#cat_sample', 'relax/methods/sphere.py'),
+                                      'relax.methods.sphere.hyper_sphere_coordindates': ( 'sphere.html#hyper_sphere_coordindates',
+                                                                                          'relax/methods/sphere.py')},
             'relax.methods.vanilla': { 'relax.methods.vanilla.VanillaCF': ('methods.vanilla.html#vanillacf', 'relax/methods/vanilla.py'),
                                        'relax.methods.vanilla.VanillaCF.__init__': ( 'methods.vanilla.html#vanillacf.__init__',
                                                                                      'relax/methods/vanilla.py'),
                                        'relax.methods.vanilla.VanillaCF.generate_cf': ( 'methods.vanilla.html#vanillacf.generate_cf',
                                                                                         'relax/methods/vanilla.py'),
                                        'relax.methods.vanilla.VanillaCF.generate_cfs': ( 'methods.vanilla.html#vanillacf.generate_cfs',
                                                                                          'relax/methods/vanilla.py'),
```

### Comparing `jax-relax-0.1.1/relax/data/loader.py` & `jax-relax-0.1.2/relax/data/loader.py`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/relax/data/module.py` & `jax-relax-0.1.2/relax/data/module.py`

 * *Files 11% similar despite different names*

```diff
@@ -2,21 +2,24 @@
 
 # %% ../../nbs/01_data.module.ipynb 3
 from __future__ import annotations
 from ..import_essentials import *
 from ..utils import load_json, validate_configs, cat_normalize
 from sklearn.preprocessing import StandardScaler, MinMaxScaler, OneHotEncoder
 from sklearn.base import TransformerMixin
+from sklearn.utils.validation import check_is_fitted, NotFittedError
 from urllib.request import urlretrieve
 from .loader import Dataset, ArrayDataset, DataLoader, DataloaderBackends
+from pydantic.fields import ModelField
 
 # %% auto 0
-__all__ = ['BaseDataModule', 'find_imutable_idx_list', 'TabularDataModuleConfigs', 'TabularDataModule', 'sample', 'load_data']
+__all__ = ['BaseDataModule', 'find_imutable_idx_list', 'TransformerMixinType', 'TabularDataModuleConfigs', 'TabularDataModule',
+           'sample', 'load_data']
 
-# %% ../../nbs/01_data.module.ipynb 5
+# %% ../../nbs/01_data.module.ipynb 6
 class BaseDataModule(ABC):
     """DataModule Interface"""
 
     @property
     @abstractmethod
     def data_name(self) -> str: 
         return
@@ -78,15 +81,15 @@
         x: jnp.DeviceArray,
         cf: jnp.DeviceArray,
         hard: bool
     ):
         raise NotImplementedError
 
 
-# %% ../../nbs/01_data.module.ipynb 7
+# %% ../../nbs/01_data.module.ipynb 8
 def find_imutable_idx_list(
     imutable_col_names: List[str],
     discrete_col_names: List[str],
     continuous_col_names: List[str],
     cat_arrays: List[List[str]],
 ) -> List[int]:
     imutable_idx_list = []
@@ -99,15 +102,79 @@
     for i, (col_name, cols) in enumerate(zip(discrete_col_names, cat_arrays)):
         cat_end_idx = cat_idx + len(cols)
         if col_name in imutable_col_names:
             imutable_idx_list += list(range(cat_idx, cat_end_idx))
         cat_idx = cat_end_idx
     return imutable_idx_list
 
-# %% ../../nbs/01_data.module.ipynb 8
+# %% ../../nbs/01_data.module.ipynb 9
+class TransformerMixinType(TransformerMixin):
+    @classmethod
+    def __get_validators__(cls):
+        yield cls.validate
+
+    @classmethod
+    def validate(cls, v):
+        if not isinstance(v, TransformerMixin):
+            raise TypeError("`sklearn.base.TransformerMixin` required")
+        return v
+    
+    @classmethod
+    def __modify_schema__(
+        cls, field_schema: Dict[str, Any], field: Optional[ModelField]
+    ):
+        if field:
+            field_schema['type'] = 'TransformerMixin'
+
+
+# %% ../../nbs/01_data.module.ipynb 10
+def _supported_backends(): 
+    back = DataloaderBackends()
+    return back.supported()
+
+class TabularDataModuleConfigs(BaseParser):
+    """Configurator of `TabularDataModule`."""
+
+    data_dir: str = Field(description="The directory of dataset.")
+    data_name: str = Field(description="The name of `TabularDataModule`.")
+    continous_cols: List[str] = Field(
+        [], description="Continuous features/columns in the data."
+    )
+    discret_cols: List[str] = Field(
+        [], description="Categorical features/columns in the data."
+    )
+    imutable_cols: List[str] = Field(
+        [], description="Immutable features/columns in the data."
+    )
+    normalizer: Optional[TransformerMixinType] = Field(
+        default_factory=lambda: MinMaxScaler(),
+        description="Sklearn scalar for continuous features. Can be unfitted, fitted, or None. "
+        "If not fitted, the `TabularDataModule` will fit using the training data. If fitted, no fitting will be applied. "
+        "If `None`, no transformation will be applied. Default to `MinMaxScaler()`."
+    )
+    encoder: Optional[TransformerMixinType] = Field(
+        default_factory=lambda: OneHotEncoder(sparse=False),
+        description="Fitted encoder for categorical features. Can be unfitted, fitted, or None. "
+        "If not fitted, the `TabularDataModule` will fit using the training data. If fitted, no fitting will be applied. "
+        "If `None`, no transformation will be applied. Default to `OneHotEncoder(sparse=False)`."
+    )
+    sample_frac: Optional[float] = Field(
+        None, description="Sample fraction of the data. Default to use the entire data.", 
+        ge=0., le=1.0
+    )
+    backend: str = Field(
+        "jax", description=f"`Dataloader` backend. Currently supports: {_supported_backends()}"
+    )
+
+    class Config:
+        json_encoders = {
+            TransformerMixinType: lambda v: f"{v.__class__.__name__}()",
+        }
+
+# %% ../../nbs/01_data.module.ipynb 13
 def _check_cols(data: pd.DataFrame, configs: TabularDataModuleConfigs) -> pd.DataFrame:
     data = data.astype({
         col: float for col in configs.continous_cols
     })
     
     cols = configs.continous_cols + configs.discret_cols
     # check target columns
@@ -119,116 +186,97 @@
     for col in configs.imutable_cols:
         assert col in cols, \
             f"imutable_cols=[{col}] is not specified in `continous_cols` or `discret_cols`."
     data = data[cols + [target_col]]
     return data
 
 
-# %% ../../nbs/01_data.module.ipynb 9
+# %% ../../nbs/01_data.module.ipynb 14
 def _process_data(
     df: pd.DataFrame | None, configs: TabularDataModuleConfigs
 ) -> pd.DataFrame:
     if df is None:
         df = pd.read_csv(configs.data_dir)
     elif isinstance(df, pd.DataFrame):
         df = df
     else:
-        raise ValueError(f"{type(df).__name__} is not supported as an input type for `TabularDataModule`.")
+        raise ValueError(
+            f"{type(df).__name__} is not supported as an input type for `TabularDataModule`.")
 
     df = _check_cols(df, configs)
     return df
 
-# %% ../../nbs/01_data.module.ipynb 10
+# %% ../../nbs/01_data.module.ipynb 16
 def _transform_df(
-    transformer: TransformerMixin,
+    transformer: TransformerMixin | None,
     data: pd.DataFrame,
     cols: List[str] | None,
 ):
-    return (
-        transformer.transform(data[cols])
-            if cols else np.array([[] for _ in range(len(data))])
-    )
+    if transformer is None:
+        return data[cols].to_numpy() if cols else np.array([[] for _ in range(len(data))])
+    else:
+        return (
+            transformer.transform(data[cols])
+                if cols else np.array([[] for _ in range(len(data))])
+        )
 
-# %% ../../nbs/01_data.module.ipynb 12
+# %% ../../nbs/01_data.module.ipynb 18
 def _inverse_transform_np(
-    transformer: TransformerMixin,
-    x: jnp.DeviceArray,
+    transformer: TransformerMixin | None,
+    x: np.ndarray,
     cols: List[str] | None
 ):
     assert len(cols) <= x.shape[-1], \
         f"x.shape={x.shape} probably will not match len(cols)={len(cols)}"
+    
     if cols:
-        data = transformer.inverse_transform(x)
-        return pd.DataFrame(data=data, columns=cols)
+        data = transformer.inverse_transform(x) if transformer else x
+        df = pd.DataFrame(data=data, columns=cols)
     else:
-        return None
+        df = None
+    return df
 
 
-# %% ../../nbs/01_data.module.ipynb 15
+# %% ../../nbs/01_data.module.ipynb 20
 def _init_scalar_encoder(
     data: pd.DataFrame,
     configs: TabularDataModuleConfigs
-):  
+) -> Dict[str, TransformerMixin | None]: 
+    # The normlizer and encoder will be either None, fitted or not fitted.
+    # If the user has specified the normlizer and encoder, then we will use it.
+    # Otherwise, we will fit the normlizer and encoder.
     # fit scalar
-    if configs.normalizer:
+    if configs.normalizer is not None:
         scalar = configs.normalizer
+        try:
+            check_is_fitted(scalar)
+        except NotFittedError:
+            if configs.continous_cols:  scalar.fit(data[configs.continous_cols])
+            else:                       scalar = None
     else:
-        scalar = MinMaxScaler()
-        if configs.continous_cols:
-            scalar.fit(data[configs.continous_cols])
+        scalar = None
     
-    # fit encoder
-    if configs.encoder:
+    if configs.encoder is not None:
         encoder = configs.encoder
+        try:
+            check_is_fitted(encoder)
+        except NotFittedError:
+            if configs.discret_cols:    encoder.fit(data[configs.discret_cols])
+            else:                       encoder = None
     else:
-        encoder = OneHotEncoder(sparse=False)
-        if configs.discret_cols:
-            encoder.fit(data[configs.discret_cols])
+        encoder = None
     return dict(scalar=scalar, encoder=encoder)
 
 
-# %% ../../nbs/01_data.module.ipynb 16
-def _supported_backends(): 
-    back = DataloaderBackends()
-    return back.supported
-
-class TabularDataModuleConfigs(BaseParser):
-    """Configurator of `TabularDataModule`."""
-
-    data_dir: str = Field(description="The directory of dataset.")
-    data_name: str = Field(description="The name of `TabularDataModule`.")
-    continous_cols: List[str] = Field(
-        [], description="Continuous features/columns in the data."
-    )
-    discret_cols: List[str] = Field(
-        [], description="Categorical features/columns in the data."
-    )
-    imutable_cols: List[str] = Field(
-        [], description="Immutable features/columns in the data."
-    )
-    normalizer: Optional[Any] = Field(
-        None, description="Fitted scalar for continuous features."
-    )
-    encoder: Optional[Any] = Field(
-        None, description="Fitted encoder for categorical features."
-    )
-    sample_frac: Optional[float] = Field(
-        None, description="Sample fraction of the data. Default to use the entire data.", 
-        ge=0., le=1.0
-    )
-    backend: str = Field(
-        "jax", description=f"`Dataloader` backend. Currently supports: {_supported_backends()}"
-    )
-
-
-# %% ../../nbs/01_data.module.ipynb 20
+# %% ../../nbs/01_data.module.ipynb 22
 class TabularDataModule(BaseDataModule):
     """DataModule for tabular data"""
     cont_scalar = None # scalar for normalizing continuous features
     cat_encoder = None # encoder for encoding categorical features
+    __initialized = False
 
     def __init__(
         self, 
         data_config: dict | TabularDataModuleConfigs, # Configurator of `TabularDataModule`
         data: pd.DataFrame = None # Data in `pd.DataFrame`. If `data` is `None`, the DataModule will load data from `data_dir`.
     ):
         self._configs: TabularDataModuleConfigs = validate_configs(
@@ -244,19 +292,22 @@
         scalar_encoder_dict = _init_scalar_encoder(
             data=self._data, configs=self._configs
         )
         self.cont_scalar = scalar_encoder_dict['scalar']
         self.cat_encoder = scalar_encoder_dict['encoder']
         X, y = self.transform(self.data)
 
+        self._cat_arrays = self.cat_encoder.categories_ \
+            if self._configs.discret_cols else []
+
         self._imutable_idx_list = find_imutable_idx_list(
             imutable_col_names=self._configs.imutable_cols,
             discrete_col_names=self._configs.discret_cols,
             continuous_col_names=self._configs.continous_cols,
-            cat_arrays=self.cat_encoder.categories_,
+            cat_arrays=self._cat_arrays,
         )
         
         # prepare train & test
         train_test_tuple = train_test_split(X, y, shuffle=False)
         train_X, test_X, train_y, test_y = map(
              lambda x: x.astype(float), train_test_tuple
          )
@@ -264,14 +315,27 @@
             train_size = int(len(train_X) * self._configs.sample_frac)
             train_X, train_y = train_X[:train_size], train_y[:train_size]
         
         self._train_dataset = ArrayDataset(train_X, train_y)
         self._val_dataset = ArrayDataset(test_X, test_y)
         self._test_dataset = self.val_dataset
 
+        self.__initialized = True
+
+    def __setattr__(self, attr: str, val: Any) -> None:
+        if self.__initialized and attr in (
+            '_data', 'cat_idx', '_imutable_idx_list', '_cat_arrays',
+            '_train_dataset', '_val_dataset', '_test_dataset',
+            'cont_scalar', 'cat_encoder'
+        ):
+            raise ValueError(f'{attr} attribute should not be set after '
+                             f'{self.__class__.__name__} is initialized')
+
+        super().__setattr__(attr, val)
+
     @property
     def data_name(self) -> str: 
         return self._configs.data_name
     
     @property
     def data(self) -> pd.DataFrame:
         """Loaded data in `pd.DataFrame`."""
@@ -353,18 +417,16 @@
     def apply_constraints(
         self, 
         x: jnp.DeviceArray, # input
         cf: jnp.DeviceArray, # Unnormalized counterfactuals
         hard: bool = False # Apply hard constraints or not
     ) -> jnp.DeviceArray:
         """Apply categorical normalization and immutability constraints"""
-        cat_arrays = self.cat_encoder.categories_ \
-            if self._configs.discret_cols else []
         cf = cat_normalize(
-            cf, cat_arrays=cat_arrays, 
+            cf, cat_arrays=self._cat_arrays, 
             cat_idx=len(self._configs.continous_cols),
             hard=hard
         )
         # apply immutable constraints
         if len(self._configs.imutable_cols) > 0:
             cf = cf.at[:, self._imutable_idx_list].set(x[:, self._imutable_idx_list])
         return cf
@@ -372,32 +434,31 @@
     def apply_regularization(
         self, 
         x: jnp.DeviceArray, # Input
         cf: jnp.DeviceArray, # Unnormalized counterfactuals
     ) -> float: # Return regularization loss
         """Apply categorical constraints by adding regularization terms"""
         reg_loss = 0.
-        cat_arrays = self.cat_encoder.categories_
         cat_idx = len(self._configs.continous_cols)
 
-        for col in cat_arrays:
+        for col in self._cat_arrays:
             cat_idx_end = cat_idx + len(col)
             reg_loss += jnp.power(
                 (jnp.sum(cf[cat_idx:cat_idx_end]) - 1.0), 2
             )
         return reg_loss
 
 
-# %% ../../nbs/01_data.module.ipynb 41
+# %% ../../nbs/01_data.module.ipynb 43
 def sample(datamodule: BaseDataModule, frac: float = 1.0): 
     X, y = datamodule.train_dataset[:]
     size = int(len(X) * frac)
     return X[:size], y[:size]
 
-# %% ../../nbs/01_data.module.ipynb 46
+# %% ../../nbs/01_data.module.ipynb 47
 DEFAULT_DATA_CONFIGS = {
     'adult': {
         'data' :'assets/data/s_adult.csv',
         'conf' :'assets/configs/data_configs/adult.json',
     },
     'heloc': {
         'data': 'assets/data/s_home.csv',
@@ -405,21 +466,21 @@
     },
     'oulad': {
         'data': 'assets/data/s_student.csv',
         'conf': 'assets/configs/data_configs/student.json'
     }
 }
 
-# %% ../../nbs/01_data.module.ipynb 47
+# %% ../../nbs/01_data.module.ipynb 48
 def _validate_dataname(data_name: str):
     if data_name not in DEFAULT_DATA_CONFIGS.keys():
         raise ValueError(f'`data_name` must be one of {DEFAULT_DATA_CONFIGS.keys()}, '
             f'but got data_name={data_name}.')
 
-# %% ../../nbs/01_data.module.ipynb 48
+# %% ../../nbs/01_data.module.ipynb 49
 def load_data(
     data_name: str, # The name of data
     return_config: bool = False, # Return `data_config `or not
     data_configs: dict = None # Data configs to override default configuration
 ) -> TabularDataModule | Tuple[TabularDataModule, TabularDataModuleConfigs]: 
     """High-level util function for loading `data` and `data_config`."""
```

### Comparing `jax-relax-0.1.1/relax/evaluate.py` & `jax-relax-0.1.2/relax/evaluate.py`

 * *Files 18% similar despite different names*

```diff
@@ -6,19 +6,20 @@
 from .trainer import TrainingConfigs
 from .data import TabularDataModule
 from .utils import accuracy, proximity
 from .methods.base import BaseCFModule, BaseParametricCFModule, BasePredFnCFModule
 from .methods.counternet import CounterNet
 from copy import deepcopy
 from sklearn.neighbors import NearestNeighbors
+from fastcore.test import test_fail
 
 # %% auto 0
-__all__ = ['CFExplanationResults', 'METRICS', 'DEFAULT_METRICS', 'Explanation', 'generate_cf_explanations', 'BaseEvalMetrics',
-           'PredictiveAccuracy', 'Validity', 'Proximity', 'Sparsity', 'ManifoldDist', 'Runtime', 'compute_so_validity',
-           'compute_so_proximity', 'compute_so_sparsity', 'evaluate_cfs', 'benchmark_cfs']
+__all__ = ['CFExplanationResults', 'METRICS_CALLABLE', 'METRICS', 'DEFAULT_METRICS', 'Explanation', 'generate_cf_explanations',
+           'BaseEvalMetrics', 'PredictiveAccuracy', 'Validity', 'Proximity', 'Sparsity', 'ManifoldDist', 'Runtime',
+           'compute_so_validity', 'compute_so_proximity', 'compute_so_sparsity', 'evaluate_cfs', 'benchmark_cfs']
 
 # %% ../nbs/06_evaluate.ipynb 4
 @dataclass
 class Explanation:
     """Generated CF Explanations class."""
     cf_name: str  # cf method's name
     data_module: TabularDataModule  # data module
@@ -149,16 +150,26 @@
         pred_fn=pred_fn,
     )
 
 
 # %% ../nbs/06_evaluate.ipynb 18
 class BaseEvalMetrics(ABC):
     """Base evaluation metrics class."""
+
+    def __init__(self, name: str = None):
+        if name is None: name = type(self).__name__
+        self.name = name
+
     def __str__(self) -> str:
-        raise NotImplementedError
+        has_name = hasattr(self, 'name')
+        if not has_name:
+            raise ValidationError(
+                "EvalMetrics must have a name. Add the following as the first line in your "
+                f"__init__ method:\n\nsuper({self.__name__}, self).__init__()")
+        return self.name
 
     def __call__(self, cf_explanations: Explanation) -> Any:
         raise NotImplementedError
 
 # %% ../nbs/06_evaluate.ipynb 19
 def _compute_acc(
     input: jnp.DeviceArray, # input dim: [N, k]
@@ -168,113 +179,117 @@
     y_pred = pred_fn(input).reshape(-1, 1).round()
     label = label.reshape(-1, 1)
     return accuracy(y_pred, label).item()
 
 # %% ../nbs/06_evaluate.ipynb 20
 class PredictiveAccuracy(BaseEvalMetrics):
     """Compute the accuracy of the predict function."""
-    def __str__(self) -> str:
-        return "accuracy"
+    
+    def __init__(self, name: str = "accuracy"):
+        super().__init__(name=name)
 
     def __call__(self, cf_explanations: Explanation) -> float:
         X, y = cf_explanations.data_module.test_dataset[:]
         return _compute_acc(X, y, cf_explanations.pred_fn)
 
-# %% ../nbs/06_evaluate.ipynb 21
+# %% ../nbs/06_evaluate.ipynb 22
 def _compute_val(
     input: jnp.DeviceArray, # input dim: [N, k]
     cfs: jnp.DeviceArray, # cfs dim: [N, k]
     pred_fn: Callable[[jnp.DeviceArray], jnp.DeviceArray]
 ):
     y_pred = pred_fn(input).reshape(-1, 1).round()
     y_prime = jnp.ones_like(y_pred) - y_pred
     cf_y = pred_fn(cfs).reshape(-1, 1).round()
     return accuracy(y_prime, cf_y).item()
 
-# %% ../nbs/06_evaluate.ipynb 22
+# %% ../nbs/06_evaluate.ipynb 23
 class Validity(BaseEvalMetrics):
     """Compute fraction of input instances on which CF explanation methods output valid CF examples."""
-    def __str__(self) -> str:
-        return "validity"
+    
+    def __init__(self, name: str = "validity"):
+        super().__init__(name=name)
     
     def __call__(self, cf_explanations: Explanation) -> float:
         X, _ = cf_explanations.data_module.test_dataset[:]
         return _compute_val(
             X, cf_explanations.cfs, cf_explanations.pred_fn
         )
 
-# %% ../nbs/06_evaluate.ipynb 23
+# %% ../nbs/06_evaluate.ipynb 24
 class Proximity(BaseEvalMetrics):
     """Compute L1 norm distance between input datasets and CF examples divided by the number of features."""
-    def __str__(self) -> str:
-        return "proximity"
+    def __init__(self, name: str = "proximity"):
+        super().__init__(name=name)
     
     def __call__(self, cf_explanations: Explanation) -> float:
         X, _ = cf_explanations.data_module.test_dataset[:]
         return proximity(X, cf_explanations.cfs).item()
 
-# %% ../nbs/06_evaluate.ipynb 24
+# %% ../nbs/06_evaluate.ipynb 25
 def _compute_spar(
     input: jnp.DeviceArray,
     cfs: jnp.DeviceArray,
     cat_idx: int
 ):
     # calculate sparsity
     cat_sparsity = proximity(input[:, cat_idx:], cfs[:, cat_idx:]) / 2
     cont_sparsity = jnp.linalg.norm(
         jnp.abs(input[:, :cat_idx] - cfs[:, :cat_idx]), ord=0, axis=1
     ).mean()
     return (cont_sparsity + cat_sparsity).item()
 
 
-# %% ../nbs/06_evaluate.ipynb 25
+# %% ../nbs/06_evaluate.ipynb 26
 class Sparsity(BaseEvalMetrics):
     """Compute the number of feature changes between input datasets and CF examples."""
-    def __str__(self) -> str:
-        return "sparsity"
+
+    def __init__(self, name: str = "sparsity"):
+        super().__init__(name=name)
     
     def __call__(self, cf_explanations: Explanation) -> float:
         X, _ = cf_explanations.data_module.test_dataset[:]
         return _compute_spar(X, cf_explanations.cfs, cf_explanations.cat_idx)
 
-# %% ../nbs/06_evaluate.ipynb 26
+# %% ../nbs/06_evaluate.ipynb 27
 def _compute_manifold_dist(
     input: jnp.DeviceArray,
     cfs: jnp.DeviceArray,
     n_neighbors: int = 1,
     p: int = 2
 ):
     knn = NearestNeighbors(n_neighbors=n_neighbors, p=p)
     knn.fit(input)
     nearest_dist, nearest_points = knn.kneighbors(cfs, 1, return_distance=True)
     return jnp.mean(nearest_dist).item()
 
-# %% ../nbs/06_evaluate.ipynb 27
+# %% ../nbs/06_evaluate.ipynb 28
 class ManifoldDist(BaseEvalMetrics):
     """Compute the L1 distance to the n-nearest neighbor for all CF examples."""
-    def __init__(self, n_neighbors: int = 1, p: int = 2):
+    def __init__(self, n_neighbors: int = 1, p: int = 2, name: str = "manifold_dist"):
+        super().__init__(name=name)
         self.n_neighbors = n_neighbors
         self.p = p
-    
-    def __str__(self) -> str:
-        return "manifold_dist"
-    
+        
     def __call__(self, cf_explanations: Explanation) -> float:
         X, _ = cf_explanations.data_module.test_dataset[:]
         return _compute_manifold_dist(
             X, cf_explanations.cfs, self.n_neighbors, self.p
         )
 
-# %% ../nbs/06_evaluate.ipynb 28
+# %% ../nbs/06_evaluate.ipynb 29
 class Runtime(BaseEvalMetrics):
     """Get the running time to generate CF examples."""
+    def __init__(self, name: str = "runtime"):
+        super().__init__(name=name)
+    
     def __call__(self, cf_explanations: Explanation) -> float:
         return cf_explanations.total_time
 
-# %% ../nbs/06_evaluate.ipynb 30
+# %% ../nbs/06_evaluate.ipynb 31
 def _create_second_order_cfs(cf_results: CFExplanationResults, threshold: float = 2.0):
     X, y = cf_results.data_module.test_dataset[:]
     cfs = cf_results.cfs
     scaler = cf_results.data_module.normalizer
     cat_idx = cf_results.data_module.cat_idx
 
     # get normalized threshold = threshold / (max - min)
@@ -313,70 +328,99 @@
     cfs_hat = _create_second_order_cfs(cf_results, threshold)
     cf_results_so = deepcopy(cf_results)
     cf_results_so.cfs = cfs_hat
     compute_sparsity = Sparsity()
     return compute_sparsity(cf_results_so)
 
 
-# %% ../nbs/06_evaluate.ipynb 32
-METRICS = dict(
-    acc=PredictiveAccuracy(),
-    accuracy=PredictiveAccuracy(),
-    validity=Validity(),
-    proximity=Proximity(),
-    runtime=Runtime(),
-    manifold_dist=ManifoldDist(),
-    # validity=compute_so_validity,
-    # so_proximity=compute_so_proximity,
-    # so_sparsity=compute_so_sparsity
-)
+# %% ../nbs/06_evaluate.ipynb 33
+def fake_explanations():
+    """Generate sudo explanations for testing."""
+    from relax.data import load_data
+
+    dm = load_data("adult")
+    X, y = dm.test_dataset[:]
+    cfs = X
+    dn = dm.data_name
+    pred_fn = lambda x: jax.random.bernoulli(jax.random.PRNGKey(0), 0.5, (x.shape[0], 1)).astype(float)
+    assert y.shape == pred_fn(X).shape
+    return Explanation(
+        cf_name='sudo', data_module=dm, cfs=cfs, pred_fn=pred_fn, total_time=0.0, dataset_name=dn
+    )
+
+
+# %% ../nbs/06_evaluate.ipynb 34
+# METRICS = dict(
+#     acc=PredictiveAccuracy(),
+#     accuracy=PredictiveAccuracy(),
+#     validity=Validity(),
+#     proximity=Proximity(),
+#     runtime=Runtime(),
+#     manifold_dist=ManifoldDist(),
+#     # validity=compute_so_validity,
+#     # so_proximity=compute_so_proximity,
+#     # so_sparsity=compute_so_sparsity
+# )
+
+METRICS_CALLABLE = [
+    PredictiveAccuracy('acc'),
+    PredictiveAccuracy('accuracy'),
+    Validity(),
+    Proximity(),
+    Runtime(),
+    ManifoldDist(),
+]
+
+METRICS = { m.name: m for m in METRICS_CALLABLE }
 
 DEFAULT_METRICS = ["acc", "validity", "proximity"]
 
-# %% ../nbs/06_evaluate.ipynb 33
-def _get_metric(metric: str | callable, cf_exp: Explanation):
+# %% ../nbs/06_evaluate.ipynb 36
+def _get_metric(metric: str | BaseEvalMetrics, cf_exp: Explanation):
     if isinstance(metric, str):
-        try:
-            res = METRICS[metric](cf_exp)
-        except KeyError:
+        if metric not in METRICS.keys():
             raise ValueError(f"'{metric}' is not supported. Must be one of {METRICS.keys()}")
+        res = METRICS[metric](cf_exp)
     elif callable(metric):
+        # f(cf_exp) not supported for now
+        if not isinstance(metric, BaseEvalMetrics):
+            raise ValueError(f"metric needs to be a subclass of `BaseEvalMetrics`.")
         res = metric(cf_exp)
     else:
         raise ValueError(f"{type(metric).__name__} is not supported as a metric.")
     
     if isinstance(res, jnp.ndarray) and res.shape == (1,):
         res = res.item()
     return res
 
-# %% ../nbs/06_evaluate.ipynb 34
+# %% ../nbs/06_evaluate.ipynb 38
 def evaluate_cfs(
     cf_exp: Explanation, # CF Explanations
-    metrics: Iterable[Union[str, Callable]] = None, # A list of Metrics. Can be `str` or a subclass of `BaseEvalMetrics`
+    metrics: Iterable[Union[str, BaseEvalMetrics]] = None, # A list of Metrics. Can be `str` or a subclass of `BaseEvalMetrics`
     return_dict: bool = True, # return a dictionary or not (default: True)
     return_df: bool = False # return a pandas Dataframe or not (default: False)
 ):
     cf_name = cf_exp.cf_name
     data_name = cf_exp.data_module.data_name
     result_dict = { (data_name, cf_name): dict() }
 
     if metrics is None:
         metrics = DEFAULT_METRICS
 
     for metric in metrics:
-        result_dict[(data_name, cf_name)][metric] = _get_metric(metric, cf_exp)
+        metric_name = str(metric)
+        result_dict[(data_name, cf_name)][metric_name] = _get_metric(metric, cf_exp)
     result_df = pd.DataFrame.from_dict(result_dict, orient="index")
     
     if return_dict and return_df:
         return (result_dict, result_df)
     elif return_dict or return_df:
         return result_df if return_df else result_dict
 
-
-# %% ../nbs/06_evaluate.ipynb 35
+# %% ../nbs/06_evaluate.ipynb 40
 def benchmark_cfs(
     cf_results_list: Iterable[CFExplanationResults],
     metrics: Optional[Iterable[str]] = None,
 ):
     dfs = [
         evaluate_cfs(
             cf_exp=cf_results, metrics=metrics, return_dict=False, return_df=True
```

### Comparing `jax-relax-0.1.1/relax/import_essentials.py` & `jax-relax-0.1.2/relax/import_essentials.py`

 * *Files 9% similar despite different names*

```diff
@@ -18,17 +18,18 @@
 from tqdm import tqdm
 from pathlib import Path
 from fastcore.utils import in_jupyter
 from dataclasses import dataclass
 from abc import ABC, abstractmethod
 from pydantic import BaseModel as BaseParser, validator, ValidationError, Field
 from deprecation import deprecated
+from functools import partial
 
 # jax related
 import jax
-from jax import pmap, vmap, random, device_put, lax, jit
-import jax.numpy as jnp
+from jax import pmap, vmap, random, device_put, lax, jit, Array
+import jax.numpy as jnp, jax.random as jrand
 
 # nn related
 import haiku as hk
 import optax
 import chex
```

### Comparing `jax-relax-0.1.1/relax/logger.py` & `jax-relax-0.1.2/relax/logger.py`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/relax/methods/base.py` & `jax-relax-0.1.2/relax/methods/base.py`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/relax/methods/counternet.py` & `jax-relax-0.1.2/relax/methods/counternet.py`

 * *Files 1% similar despite different names*

```diff
@@ -54,36 +54,36 @@
         cf = MLP(self.configs.exp_sizes, self.configs.dropout_rate, name="Explainer")(
             z_exp, is_training
         )
         cf = hk.Linear(input_shape, name="Explainer")(cf)
         return y_hat, cf
 
 
-# %% ../../nbs/05d_methods.counternet.ipynb 10
+# %% ../../nbs/05d_methods.counternet.ipynb 8
 def partition_trainable_params(params: hk.Params, trainable_name: str):
     trainable_params, non_trainable_params = hk.data_structures.partition(
         lambda m, n, p: trainable_name in m, params
     )
     return trainable_params, non_trainable_params
 
 
-# %% ../../nbs/05d_methods.counternet.ipynb 11
+# %% ../../nbs/05d_methods.counternet.ipynb 9
 def project_immutable_features(x, cf: jnp.DeviceArray, imutable_idx_list: List[int]):
     cf = cf.at[:, imutable_idx_list].set(x[:, imutable_idx_list])
     return cf
 
-# %% ../../nbs/05d_methods.counternet.ipynb 12
+# %% ../../nbs/05d_methods.counternet.ipynb 10
 class CounterNetTrainingModuleConfigs(BaseParser):
     lr: float = 0.003
     lambda_1: float = 1.0
     lambda_2: float = 0.2
     lambda_3: float = 0.1
 
 
-# %% ../../nbs/05d_methods.counternet.ipynb 13
+# %% ../../nbs/05d_methods.counternet.ipynb 11
 class CounterNetTrainingModule(BaseTrainingModule):
     _data_module: TabularDataModule
 
     def __init__(self, m_configs: Dict[str, Any]):
         self.save_hyperparameters(m_configs)
         self.net = make_model(m_configs, CounterNetModel)
         self.configs = validate_configs(m_configs, CounterNetTrainingModuleConfigs)
@@ -242,15 +242,15 @@
             "val/val_loss_2": loss_2,
             "val/val_loss_3": loss_3,
             "val/val_loss": loss_1 + loss_2 + loss_3,
         }
         self.log_dict(logs)
         return logs
 
-# %% ../../nbs/05d_methods.counternet.ipynb 18
+# %% ../../nbs/05d_methods.counternet.ipynb 16
 class CounterNetConfigs(CounterNetTrainingModuleConfigs, CounterNetModelConfigs):
     """Configurator of `CounterNet`."""
 
     enc_sizes: List[int] = Field(
         [50,10], description="Sequence of layer sizes for encoder network."
     )
     dec_sizes: List[int] = Field(
@@ -273,15 +273,15 @@
         0.2, description=" $\lambda_2$ for balancing the prediction loss $\mathcal{L}_2$."
     ) 
     lambda_3: float = Field(
         0.1, description=" $\lambda_3$ for balancing the prediction loss $\mathcal{L}_3$."
     )
 
 
-# %% ../../nbs/05d_methods.counternet.ipynb 20
+# %% ../../nbs/05d_methods.counternet.ipynb 17
 class CounterNet(BaseCFModule, BaseParametricCFModule, BasePredFnCFModule):
     """API for CounterNet Explanation Module."""
     params: hk.Params = None
     module: CounterNetTrainingModule
     name: str = 'CounterNet'
 
     def __init__(
```

### Comparing `jax-relax-0.1.1/relax/methods/diverse.py` & `jax-relax-0.1.2/relax/methods/diverse.py`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/relax/methods/proto.py` & `jax-relax-0.1.2/relax/methods/proto.py`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/relax/methods/vanilla.py` & `jax-relax-0.1.2/relax/methods/vanilla.py`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/relax/module.py` & `jax-relax-0.1.2/relax/module.py`

 * *Files 3% similar despite different names*

```diff
@@ -21,64 +21,68 @@
 
     def __call__(self, *, is_training: bool):
         pass
 
 
 # %% ../nbs/03_training_module.ipynb 6
 class DenseBlock(hk.Module):
+    """A `DenseBlock` consists of a dense layer, followed by Leaky Relu and a dropout layer."""
+    
     def __init__(
         self,
         output_size: int,  # Output dimensionality.
         dropout_rate: float = 0.3,  # Dropout rate.
         name: str | None = None,  # Name of the Module
     ):
-        """A `DenseBlock` consists of a dense layer, followed by Leaky Relu and a dropout layer."""
         super().__init__(name=name)
         self.output_size = output_size
         self.dropout_rate = dropout_rate
 
     def __call__(self, x: jnp.ndarray, is_training: bool = True) -> jnp.ndarray:
         dropout_rate = self.dropout_rate if is_training else 0.0
         # he_uniform
         w_init = hk.initializers.VarianceScaling(2.0, "fan_in", "uniform")
         x = hk.Linear(self.output_size, w_init=w_init)(x)
         x = jax.nn.leaky_relu(x)
         x = hk.dropout(hk.next_rng_key(), dropout_rate, x)
         return x
 
 
-# %% ../nbs/03_training_module.ipynb 8
+# %% ../nbs/03_training_module.ipynb 7
 class MLP(hk.Module):
+    """A `MLP` consists of a list of `DenseBlock` layers."""
+    
     def __init__(
         self,
         sizes: Iterable[int],  # Sequence of layer sizes.
         dropout_rate: float = 0.3,  # Dropout rate.
         name: str | None = None,  # Name of the Module
     ):
-        """A `MLP` consists of a list of `DenseBlock` layers."""
         super().__init__(name=name)
         self.sizes = sizes
         self.dropout_rate = dropout_rate
 
     def __call__(self, x: jnp.ndarray, is_training: bool = True) -> jnp.ndarray:
         for size in self.sizes:
             x = DenseBlock(size, self.dropout_rate)(x, is_training)
         return x
 
 
-# %% ../nbs/03_training_module.ipynb 11
+# %% ../nbs/03_training_module.ipynb 9
 class PredictiveModelConfigs(BaseParser):
     """Configurator of `PredictiveModel`."""
 
     sizes: List[int]  # Sequence of layer sizes.
     dropout_rate: float = 0.3  # Dropout rate.
 
 
-# %% ../nbs/03_training_module.ipynb 12
+# %% ../nbs/03_training_module.ipynb 10
 class PredictiveModel(hk.Module):
+    """A basic predictive model for binary classification."""
+    
     def __init__(
         self,
         sizes: List[int], # Sequence of layer sizes.
         dropout_rate: float = 0.3,  # Dropout rate.
         name: Optional[str] = None,  # Name of the module.
     ):
         """A basic predictive model for binary classification."""
@@ -93,15 +97,15 @@
         )
         x = hk.Linear(1)(x)
         x = jax.nn.sigmoid(x)
         # x = sigmoid(x)
         return x
 
 
-# %% ../nbs/03_training_module.ipynb 28
+# %% ../nbs/03_training_module.ipynb 25
 class BaseTrainingModule(ABC):
     hparams: Dict[str, Any]
     logger: TensorboardLogger | None
 
     def save_hyperparameters(self, configs: Dict[str, Any]) -> Dict[str, Any]:
         self.hparams = deepcopy(configs)
         return self.hparams
@@ -141,22 +145,26 @@
         params: hk.Params,
         rng_key: random.PRNGKey,
         batch: Tuple[jnp.array, jnp.array],
     ) -> Dict[str, Any]:
         pass
 
 
-# %% ../nbs/03_training_module.ipynb 30
+# %% ../nbs/03_training_module.ipynb 27
 class PredictiveTrainingModuleConfigs(BaseParser):
+    """Configurator of `PredictiveTrainingModule`."""
+    
     lr: float = Field(description='Learning rate.')
     sizes: List[int] = Field(description='Sequence of layer sizes.')
     dropout_rate: float = Field(0.3, description='Dropout rate') 
 
-# %% ../nbs/03_training_module.ipynb 31
+# %% ../nbs/03_training_module.ipynb 28
 class PredictiveTrainingModule(BaseTrainingModule):
+    """A training module for predictive models."""
+    
     def __init__(self, m_configs: Dict | PredictiveTrainingModuleConfigs):
         self.save_hyperparameters(m_configs)
         self.configs = validate_configs(m_configs, PredictiveTrainingModuleConfigs)
         self.net = make_hk_module(
             PredictiveModel, 
             sizes=self.configs.sizes, 
             dropout_rate=self.configs.dropout_rate
```

### Comparing `jax-relax-0.1.1/relax/plots.py` & `jax-relax-0.1.2/relax/plots.py`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/relax/trainer.py` & `jax-relax-0.1.2/relax/trainer.py`

 * *Files 0% similar despite different names*

```diff
@@ -42,15 +42,15 @@
     )
 
     @property
     def PRNGSequence(self):
         return hk.PRNGSequence(self.seed)
 
 
-# %% ../nbs/04_learning.ipynb 6
+# %% ../nbs/04_learning.ipynb 5
 def train_model_with_states(
     training_module: BaseTrainingModule,
     params: hk.Params,
     opt_state: optax.OptState,
     data_module: TabularDataModule,
     t_configs: Dict[str, Any] | TrainingConfigs,
 ) -> Tuple[hk.Params, optax.OptState]:
@@ -111,15 +111,15 @@
         epoch_logs = training_module.logger.on_epoch_finished()
         ckpt_manager.update_checkpoints(params, opt_state, epoch_logs, epoch)
 
     training_module.logger.close()
     return params, opt_state
 
 
-# %% ../nbs/04_learning.ipynb 7
+# %% ../nbs/04_learning.ipynb 6
 def train_model(
     training_module: BaseTrainingModule, # Training module
     data_module: TabularDataModule, # Data module
     t_configs: Dict[str, Any] | TrainingConfigs, # Training configurator
 ) -> Tuple[hk.Params, optax.OptState]:
     """Train models."""
```

### Comparing `jax-relax-0.1.1/relax/utils.py` & `jax-relax-0.1.2/relax/utils.py`

 * *Files identical despite different names*

### Comparing `jax-relax-0.1.1/settings.ini` & `jax-relax-0.1.2/settings.ini`

 * *Files 23% similar despite different names*

```diff
@@ -4,23 +4,23 @@
 user = birkhoffg
 description = Jax-based Recourse Explanation Library
 keywords = Jax, Recourse, Explanation, Interpretability, Machine Learning
 author = BirkhoffG
 author_email = 26811230+BirkhoffG@users.noreply.github.com
 copyright = Birkhoff Guo
 branch = master
-version = 0.1.1
+version = 0.1.2
 min_python = 3.7
 audience = Developers
 language = English
 custom_sidebar = true
 license = apache2
 status = 2
-requirements = matplotlib seaborn scikit-learn pandas nbdev jupyter dm-haiku test_tube jax[cpu] tqdm optax pydantic>=1.9.0,<2 deprecation
-dev_requirements = torch>=1.7.0
+requirements = matplotlib seaborn scikit-learn>=1.0.2,<1.4.0 pandas nbdev jupyter dm-haiku test_tube jax[cpu] tqdm optax pydantic>=1.9.0,<2 deprecation networkx
+dev_requirements = torch>=1.7.0 causalgraphicalmodels
 nbs_path = nbs
 doc_path = _docs
 recursive = True
 doc_host = https://birkhoffg.github.io
 doc_baseurl = /ReLax/
 git_url = https://github.com/birkhoffg/relax/tree/master/
 lib_path = relax
@@ -30,8 +30,9 @@
 readme_nb = index.ipynb
 allowed_metadata_keys = 
 allowed_cell_metadata_keys = 
 jupyter_hooks = True
 clean_ids = True
 clear_all = False
 put_version_in_init = True
+renderer = relax.docs.CustomizedMarkdownRenderer
```

### Comparing `jax-relax-0.1.1/setup.py` & `jax-relax-0.1.2/setup.py`

 * *Files identical despite different names*

