# Comparing `tmp/tasknet-1.8.0.tar.gz` & `tmp/tasknet-1.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tasknet-1.8.0.tar", last modified: Wed Nov 16 13:08:47 2022, max compression
+gzip compressed data, was "tasknet-1.9.0.tar", last modified: Wed Nov 16 13:19:41 2022, max compression
```

## Comparing `tasknet-1.8.0.tar` & `tasknet-1.9.0.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:08:47.768337 tasknet-1.8.0/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:08:47.764337 tasknet-1.8.0/.github/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:08:47.768337 tasknet-1.8.0/.github/scripts/
--rw-r--r--   0 runner    (1001) docker     (122)     1328 2022-11-16 13:08:39.000000 tasknet-1.8.0/.github/scripts/release.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:08:47.768337 tasknet-1.8.0/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (122)      431 2022-11-16 13:08:39.000000 tasknet-1.8.0/.github/workflows/python-publish.yml
--rw-r--r--   0 runner    (1001) docker     (122)      319 2022-11-16 13:08:39.000000 tasknet-1.8.0/.github/workflows/release.yml
--rwxr-xr-x   0 runner    (1001) docker     (122)      234 2022-11-16 13:08:39.000000 tasknet-1.8.0/CITATION.cff
--rwxr-xr-x   0 runner    (1001) docker     (122)    11357 2022-11-16 13:08:39.000000 tasknet-1.8.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (122)     3181 2022-11-16 13:08:47.768337 tasknet-1.8.0/PKG-INFO
--rwxr-xr-x   0 runner    (1001) docker     (122)     2792 2022-11-16 13:08:39.000000 tasknet-1.8.0/README.md
--rwxr-xr-x   0 runner    (1001) docker     (122)    17116 2022-11-16 13:08:39.000000 tasknet-1.8.0/Tasknet_multitask_transformer_training.ipynb
--rwxr-xr-x   0 runner    (1001) docker     (122)      137 2022-11-16 13:08:39.000000 tasknet-1.8.0/pyproject.toml
--rwxr-xr-x   0 runner    (1001) docker     (122)      589 2022-11-16 13:08:47.768337 tasknet-1.8.0/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:08:47.764337 tasknet-1.8.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:08:47.768337 tasknet-1.8.0/src/tasknet/
--rwxr-xr-x   0 runner    (1001) docker     (122)       64 2022-11-16 13:08:39.000000 tasknet-1.8.0/src/tasknet/__init__.py
--rwxr-xr-x   0 runner    (1001) docker     (122)    11849 2022-11-16 13:08:39.000000 tasknet-1.8.0/src/tasknet/models.py
--rwxr-xr-x   0 runner    (1001) docker     (122)     8531 2022-11-16 13:08:39.000000 tasknet-1.8.0/src/tasknet/tasks.py
--rwxr-xr-x   0 runner    (1001) docker     (122)      449 2022-11-16 13:08:39.000000 tasknet-1.8.0/src/tasknet/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:08:47.768337 tasknet-1.8.0/src/tasknet.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)     3181 2022-11-16 13:08:47.000000 tasknet-1.8.0/src/tasknet.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)      456 2022-11-16 13:08:47.000000 tasknet-1.8.0/src/tasknet.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2022-11-16 13:08:47.000000 tasknet-1.8.0/src/tasknet.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)       70 2022-11-16 13:08:47.000000 tasknet-1.8.0/src/tasknet.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)        8 2022-11-16 13:08:47.000000 tasknet-1.8.0/src/tasknet.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:19:41.875036 tasknet-1.9.0/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:19:41.871036 tasknet-1.9.0/.github/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:19:41.875036 tasknet-1.9.0/.github/scripts/
+-rw-r--r--   0 runner    (1001) docker     (122)     1328 2022-11-16 13:19:31.000000 tasknet-1.9.0/.github/scripts/release.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:19:41.875036 tasknet-1.9.0/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (122)      431 2022-11-16 13:19:31.000000 tasknet-1.9.0/.github/workflows/python-publish.yml
+-rw-r--r--   0 runner    (1001) docker     (122)      319 2022-11-16 13:19:31.000000 tasknet-1.9.0/.github/workflows/release.yml
+-rwxr-xr-x   0 runner    (1001) docker     (122)      234 2022-11-16 13:19:31.000000 tasknet-1.9.0/CITATION.cff
+-rwxr-xr-x   0 runner    (1001) docker     (122)    11357 2022-11-16 13:19:31.000000 tasknet-1.9.0/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (122)     3181 2022-11-16 13:19:41.875036 tasknet-1.9.0/PKG-INFO
+-rwxr-xr-x   0 runner    (1001) docker     (122)     2792 2022-11-16 13:19:31.000000 tasknet-1.9.0/README.md
+-rwxr-xr-x   0 runner    (1001) docker     (122)    17116 2022-11-16 13:19:31.000000 tasknet-1.9.0/Tasknet_multitask_transformer_training.ipynb
+-rwxr-xr-x   0 runner    (1001) docker     (122)      137 2022-11-16 13:19:31.000000 tasknet-1.9.0/pyproject.toml
+-rwxr-xr-x   0 runner    (1001) docker     (122)      589 2022-11-16 13:19:41.875036 tasknet-1.9.0/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:19:41.875036 tasknet-1.9.0/src/
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:19:41.875036 tasknet-1.9.0/src/tasknet/
+-rwxr-xr-x   0 runner    (1001) docker     (122)       64 2022-11-16 13:19:31.000000 tasknet-1.9.0/src/tasknet/__init__.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)    11849 2022-11-16 13:19:31.000000 tasknet-1.9.0/src/tasknet/models.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)     8530 2022-11-16 13:19:31.000000 tasknet-1.9.0/src/tasknet/tasks.py
+-rwxr-xr-x   0 runner    (1001) docker     (122)      449 2022-11-16 13:19:31.000000 tasknet-1.9.0/src/tasknet/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2022-11-16 13:19:41.875036 tasknet-1.9.0/src/tasknet.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)     3181 2022-11-16 13:19:41.000000 tasknet-1.9.0/src/tasknet.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      456 2022-11-16 13:19:41.000000 tasknet-1.9.0/src/tasknet.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2022-11-16 13:19:41.000000 tasknet-1.9.0/src/tasknet.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       70 2022-11-16 13:19:41.000000 tasknet-1.9.0/src/tasknet.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        8 2022-11-16 13:19:41.000000 tasknet-1.9.0/src/tasknet.egg-info/top_level.txt
```

### Comparing `tasknet-1.8.0/.github/scripts/release.py` & `tasknet-1.9.0/.github/scripts/release.py`

 * *Files identical despite different names*

### Comparing `tasknet-1.8.0/LICENSE` & `tasknet-1.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `tasknet-1.8.0/PKG-INFO` & `tasknet-1.9.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tasknet
-Version: 1.8.0
+Version: 1.9.0
 Summary: Seamless integration of tasks with huggingface models
 Home-page: https://github.com/sileod/tasknet/
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Intended Audience :: Developers
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
```

### Comparing `tasknet-1.8.0/README.md` & `tasknet-1.9.0/README.md`

 * *Files identical despite different names*

### Comparing `tasknet-1.8.0/Tasknet_multitask_transformer_training.ipynb` & `tasknet-1.9.0/Tasknet_multitask_transformer_training.ipynb`

 * *Files identical despite different names*

### Comparing `tasknet-1.8.0/setup.cfg` & `tasknet-1.9.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `tasknet-1.8.0/src/tasknet/models.py` & `tasknet-1.9.0/src/tasknet/models.py`

 * *Files identical despite different names*

### Comparing `tasknet-1.8.0/src/tasknet/tasks.py` & `tasknet-1.9.0/src/tasknet/tasks.py`

 * *Files 0% similar despite different names*

```diff
@@ -11,15 +11,15 @@
 import funcy as fc
 import evaluate
 from dataclasses import dataclass, field
 import re
 from transformers.tokenization_utils_base import PreTrainedTokenizerBase
 
 load_dataset = lazy_func(datasets.load_dataset)
-_= = None
+_ = None
 
 def get_name(dataset):
     try:
         s = str(dataset.cache_files.values())
         return re.search(r"/datasets/(.*?)/default/", s).group(1).split("___")[-1]
     except:
         return ""
```

### Comparing `tasknet-1.8.0/src/tasknet.egg-info/PKG-INFO` & `tasknet-1.9.0/src/tasknet.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tasknet
-Version: 1.8.0
+Version: 1.9.0
 Summary: Seamless integration of tasks with huggingface models
 Home-page: https://github.com/sileod/tasknet/
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Intended Audience :: Developers
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
```

