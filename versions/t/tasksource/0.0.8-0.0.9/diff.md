# Comparing `tmp/tasksource-0.0.8.tar.gz` & `tmp/tasksource-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tasksource-0.0.8.tar", last modified: Fri Jan 13 22:18:03 2023, max compression
+gzip compressed data, was "tasksource-0.0.9.tar", last modified: Fri Jan 13 22:25:20 2023, max compression
```

## Comparing `tasksource-0.0.8.tar` & `tasksource-0.0.9.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:18:03.215441 tasksource-0.0.8/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:18:03.211441 tasksource-0.0.8/.github/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:18:03.211441 tasksource-0.0.8/.github/scripts/
--rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-01-13 22:17:55.000000 tasksource-0.0.8/.github/scripts/release.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:18:03.211441 tasksource-0.0.8/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (123)      431 2023-01-13 22:17:55.000000 tasksource-0.0.8/.github/workflows/python-publish.yml
--rw-r--r--   0 runner    (1001) docker     (123)      319 2023-01-13 22:17:55.000000 tasksource-0.0.8/.github/workflows/release.yml
--rwxr-xr-x   0 runner    (1001) docker     (123)      702 2023-01-13 22:17:55.000000 tasksource-0.0.8/.gitignore
--rwxr-xr-x   0 runner    (1001) docker     (123)    11357 2023-01-13 22:17:55.000000 tasksource-0.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3394 2023-01-13 22:18:03.215441 tasksource-0.0.8/PKG-INFO
--rwxr-xr-x   0 runner    (1001) docker     (123)     3007 2023-01-13 22:17:55.000000 tasksource-0.0.8/README.md
--rwxr-xr-x   0 runner    (1001) docker     (123)      137 2023-01-13 22:17:55.000000 tasksource-0.0.8/pyproject.toml
--rwxr-xr-x   0 runner    (1001) docker     (123)      574 2023-01-13 22:18:03.215441 tasksource-0.0.8/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:18:03.211441 tasksource-0.0.8/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:18:03.211441 tasksource-0.0.8/src/tasksource/
--rwxr-xr-x   0 runner    (1001) docker     (123)       69 2023-01-13 22:17:55.000000 tasksource-0.0.8/src/tasksource/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3003 2023-01-13 22:17:55.000000 tasksource-0.0.8/src/tasksource/access.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:18:03.215441 tasksource-0.0.8/src/tasksource/metadata/
--rw-r--r--   0 runner    (1001) docker     (123)     1585 2023-01-13 22:17:55.000000 tasksource-0.0.8/src/tasksource/metadata/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3612 2023-01-13 22:17:55.000000 tasksource-0.0.8/src/tasksource/metadata/bigbench_groups.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     2721 2023-01-13 22:17:55.000000 tasksource-0.0.8/src/tasksource/metadata/blimp_groups.py
--rw-r--r--   0 runner    (1001) docker     (123)    25139 2023-01-13 22:17:55.000000 tasksource-0.0.8/src/tasksource/metadata/popularity.py
--rwxr-xr-x   0 runner    (1001) docker     (123)     7620 2023-01-13 22:17:55.000000 tasksource-0.0.8/src/tasksource/preprocess.py
--rwxr-xr-x   0 runner    (1001) docker     (123)    29884 2023-01-13 22:17:55.000000 tasksource-0.0.8/src/tasksource/tasks.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:18:03.211441 tasksource-0.0.8/src/tasksource.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3394 2023-01-13 22:18:03.000000 tasksource-0.0.8/src/tasksource.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      607 2023-01-13 22:18:03.000000 tasksource-0.0.8/src/tasksource.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 22:18:03.000000 tasksource-0.0.8/src/tasksource.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       57 2023-01-13 22:18:03.000000 tasksource-0.0.8/src/tasksource.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       11 2023-01-13 22:18:03.000000 tasksource-0.0.8/src/tasksource.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)   127818 2023-01-13 22:17:55.000000 tasksource-0.0.8/tasks.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:25:20.242703 tasksource-0.0.9/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:25:20.238703 tasksource-0.0.9/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:25:20.238703 tasksource-0.0.9/.github/scripts/
+-rw-r--r--   0 runner    (1001) docker     (123)     1328 2023-01-13 22:25:12.000000 tasksource-0.0.9/.github/scripts/release.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:25:20.238703 tasksource-0.0.9/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)      431 2023-01-13 22:25:12.000000 tasksource-0.0.9/.github/workflows/python-publish.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      319 2023-01-13 22:25:12.000000 tasksource-0.0.9/.github/workflows/release.yml
+-rwxr-xr-x   0 runner    (1001) docker     (123)      702 2023-01-13 22:25:12.000000 tasksource-0.0.9/.gitignore
+-rwxr-xr-x   0 runner    (1001) docker     (123)    11357 2023-01-13 22:25:12.000000 tasksource-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3394 2023-01-13 22:25:20.242703 tasksource-0.0.9/PKG-INFO
+-rwxr-xr-x   0 runner    (1001) docker     (123)     3007 2023-01-13 22:25:12.000000 tasksource-0.0.9/README.md
+-rwxr-xr-x   0 runner    (1001) docker     (123)      137 2023-01-13 22:25:12.000000 tasksource-0.0.9/pyproject.toml
+-rwxr-xr-x   0 runner    (1001) docker     (123)      574 2023-01-13 22:25:20.242703 tasksource-0.0.9/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:25:20.238703 tasksource-0.0.9/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:25:20.238703 tasksource-0.0.9/src/tasksource/
+-rwxr-xr-x   0 runner    (1001) docker     (123)       69 2023-01-13 22:25:12.000000 tasksource-0.0.9/src/tasksource/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3003 2023-01-13 22:25:12.000000 tasksource-0.0.9/src/tasksource/access.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:25:20.242703 tasksource-0.0.9/src/tasksource/metadata/
+-rw-r--r--   0 runner    (1001) docker     (123)     1585 2023-01-13 22:25:12.000000 tasksource-0.0.9/src/tasksource/metadata/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3612 2023-01-13 22:25:12.000000 tasksource-0.0.9/src/tasksource/metadata/bigbench_groups.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     2721 2023-01-13 22:25:12.000000 tasksource-0.0.9/src/tasksource/metadata/blimp_groups.py
+-rw-r--r--   0 runner    (1001) docker     (123)    25139 2023-01-13 22:25:12.000000 tasksource-0.0.9/src/tasksource/metadata/popularity.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)     7619 2023-01-13 22:25:12.000000 tasksource-0.0.9/src/tasksource/preprocess.py
+-rwxr-xr-x   0 runner    (1001) docker     (123)    29884 2023-01-13 22:25:12.000000 tasksource-0.0.9/src/tasksource/tasks.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-13 22:25:20.242703 tasksource-0.0.9/src/tasksource.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3394 2023-01-13 22:25:20.000000 tasksource-0.0.9/src/tasksource.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      607 2023-01-13 22:25:20.000000 tasksource-0.0.9/src/tasksource.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-13 22:25:20.000000 tasksource-0.0.9/src/tasksource.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       57 2023-01-13 22:25:20.000000 tasksource-0.0.9/src/tasksource.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-01-13 22:25:20.000000 tasksource-0.0.9/src/tasksource.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)   127818 2023-01-13 22:25:12.000000 tasksource-0.0.9/tasks.md
```

### Comparing `tasksource-0.0.8/.github/scripts/release.py` & `tasksource-0.0.9/.github/scripts/release.py`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/.gitignore` & `tasksource-0.0.9/.gitignore`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/LICENSE` & `tasksource-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/PKG-INFO` & `tasksource-0.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tasksource
-Version: 0.0.8
+Version: 0.0.9
 Summary: Preprocessings to prepare datasets for a task
 Home-page: https://github.com/sileod/tasksource/
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Intended Audience :: Developers
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
```

### Comparing `tasksource-0.0.8/README.md` & `tasksource-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/setup.cfg` & `tasksource-0.0.9/setup.cfg`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/src/tasksource/access.py` & `tasksource-0.0.9/src/tasksource/access.py`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/src/tasksource/metadata/__init__.py` & `tasksource-0.0.9/src/tasksource/metadata/__init__.py`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/src/tasksource/metadata/bigbench_groups.py` & `tasksource-0.0.9/src/tasksource/metadata/bigbench_groups.py`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/src/tasksource/metadata/blimp_groups.py` & `tasksource-0.0.9/src/tasksource/metadata/blimp_groups.py`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/src/tasksource/metadata/popularity.py` & `tasksource-0.0.9/src/tasksource/metadata/popularity.py`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/src/tasksource/preprocess.py` & `tasksource-0.0.9/src/tasksource/preprocess.py`

 * *Files 1% similar despite different names*

```diff
@@ -205,15 +205,15 @@
     
     if 'validation' in dataset and 'test' not in dataset:
         validation_test = dataset['validation'].train_test_split(0.5, seed=0)
         dataset['validation'] = validation_test['train']
         dataset['test']=validation_test['test']
 
     if 'test' in dataset and 'validation' not in dataset:
-        validation_test = dataset['test'].train_test_split(0.5, sseed=0)
+        validation_test = dataset['test'].train_test_split(0.5, seed=0)
         dataset['validation'] = validation_test['train']
         dataset['test']=validation_test['test']
 
     if 'validation' not in dataset and 'test' not in dataset:
         train_val_test = dataset["train"].train_test_split(train_size=0.85, seed=0)
         val_test = train_val_test["test"].train_test_split(0.5, seed=0)
         dataset["train"] = train_val_test["train"]
```

### Comparing `tasksource-0.0.8/src/tasksource/tasks.py` & `tasksource-0.0.9/src/tasksource/tasks.py`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/src/tasksource.egg-info/PKG-INFO` & `tasksource-0.0.9/src/tasksource.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tasksource
-Version: 0.0.8
+Version: 0.0.9
 Summary: Preprocessings to prepare datasets for a task
 Home-page: https://github.com/sileod/tasksource/
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: BSD License
 Classifier: Intended Audience :: Developers
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
```

### Comparing `tasksource-0.0.8/src/tasksource.egg-info/SOURCES.txt` & `tasksource-0.0.9/src/tasksource.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tasksource-0.0.8/tasks.md` & `tasksource-0.0.9/tasks.md`

 * *Files identical despite different names*

