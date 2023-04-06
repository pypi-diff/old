# Comparing `tmp/huggingface_hub-0.9.0rc3.tar.gz` & `tmp/huggingface_hub-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "huggingface_hub-0.9.0rc3.tar", last modified: Tue Aug 23 07:15:19 2022, max compression
+gzip compressed data, was "huggingface_hub-0.9.1.tar", last modified: Thu Aug 25 15:37:04 2022, max compression
```

## Comparing `huggingface_hub-0.9.0rc3.tar` & `huggingface_hub-0.9.1.tar`

### file list

```diff
@@ -1,49 +1,49 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-23 07:15:19.335722 huggingface_hub-0.9.0rc3/
--rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)     3891 2022-08-23 07:15:19.335722 huggingface_hub-0.9.0rc3/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     2839 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/README.md
--rw-r--r--   0 runner    (1001) docker     (121)       96 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)      834 2022-08-23 07:15:19.335722 huggingface_hub-0.9.0rc3/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2415 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-23 07:15:19.331722 huggingface_hub-0.9.0rc3/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-23 07:15:19.335722 huggingface_hub-0.9.0rc3/src/huggingface_hub/
--rw-r--r--   0 runner    (1001) docker     (121)     6566 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    15132 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/_commit_api.py
--rw-r--r--   0 runner    (1001) docker     (121)     8252 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/_snapshot_download.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-23 07:15:19.335722 huggingface_hub-0.9.0rc3/src/huggingface_hub/commands/
--rw-r--r--   0 runner    (1001) docker     (121)      922 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/commands/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     1334 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/commands/huggingface_cli.py
--rw-r--r--   0 runner    (1001) docker     (121)     7406 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/commands/lfs.py
--rw-r--r--   0 runner    (1001) docker     (121)    12304 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/commands/user.py
--rw-r--r--   0 runner    (1001) docker     (121)    11146 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/community.py
--rw-r--r--   0 runner    (1001) docker     (121)     2771 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/constants.py
--rw-r--r--   0 runner    (1001) docker     (121)    16184 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/fastai_utils.py
--rw-r--r--   0 runner    (1001) docker     (121)    49343 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/file_download.py
--rw-r--r--   0 runner    (1001) docker     (121)   124559 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/hf_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    19615 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/hub_mixin.py
--rw-r--r--   0 runner    (1001) docker     (121)     5513 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/inference_api.py
--rw-r--r--   0 runner    (1001) docker     (121)    24058 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/keras_mixin.py
--rw-r--r--   0 runner    (1001) docker     (121)    16215 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/lfs.py
--rw-r--r--   0 runner    (1001) docker     (121)    16519 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/repocard.py
--rw-r--r--   0 runner    (1001) docker     (121)     2319 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/repocard_types.py
--rw-r--r--   0 runner    (1001) docker     (121)    55356 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/repository.py
--rw-r--r--   0 runner    (1001) docker     (121)      473 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/snapshot_download.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-23 07:15:19.335722 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/
--rw-r--r--   0 runner    (1001) docker     (121)     1083 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     2635 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_datetime.py
--rw-r--r--   0 runner    (1001) docker     (121)     3543 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_deprecation.py
--rw-r--r--   0 runner    (1001) docker     (121)     6183 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_errors.py
--rw-r--r--   0 runner    (1001) docker     (121)      394 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_fixes.py
--rw-r--r--   0 runner    (1001) docker     (121)     4415 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_paths.py
--rw-r--r--   0 runner    (1001) docker     (121)     1952 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_subprocess.py
--rw-r--r--   0 runner    (1001) docker     (121)    12726 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/endpoint_helpers.py
--rw-r--r--   0 runner    (1001) docker     (121)     4880 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/logging.py
--rw-r--r--   0 runner    (1001) docker     (121)     1214 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/sha.py
--rw-r--r--   0 runner    (1001) docker     (121)     4088 2022-08-23 07:15:09.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/tqdm.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-23 07:15:19.335722 huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     3891 2022-08-23 07:15:19.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1447 2022-08-23 07:15:19.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-23 07:15:19.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)       83 2022-08-23 07:15:19.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (121)      532 2022-08-23 07:15:19.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)       16 2022-08-23 07:15:19.000000 huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 15:37:04.460654 huggingface_hub-0.9.1/
+-rw-r--r--   0 runner    (1001) docker     (121)    11357 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)     3888 2022-08-25 15:37:04.460654 huggingface_hub-0.9.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     2839 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (121)       96 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (121)      834 2022-08-25 15:37:04.460654 huggingface_hub-0.9.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2415 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 15:37:04.452654 huggingface_hub-0.9.1/src/
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 15:37:04.456654 huggingface_hub-0.9.1/src/huggingface_hub/
+-rw-r--r--   0 runner    (1001) docker     (121)     6562 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    15132 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/_commit_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)     8252 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/_snapshot_download.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 15:37:04.456654 huggingface_hub-0.9.1/src/huggingface_hub/commands/
+-rw-r--r--   0 runner    (1001) docker     (121)      922 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/commands/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1334 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/commands/huggingface_cli.py
+-rw-r--r--   0 runner    (1001) docker     (121)     7406 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/commands/lfs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12304 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/commands/user.py
+-rw-r--r--   0 runner    (1001) docker     (121)    11146 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/community.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2771 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/constants.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16184 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/fastai_utils.py
+-rw-r--r--   0 runner    (1001) docker     (121)    49343 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/file_download.py
+-rw-r--r--   0 runner    (1001) docker     (121)   124559 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/hf_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    19615 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/hub_mixin.py
+-rw-r--r--   0 runner    (1001) docker     (121)     5513 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/inference_api.py
+-rw-r--r--   0 runner    (1001) docker     (121)    24058 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/keras_mixin.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16215 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/lfs.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16519 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/repocard.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2319 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/repocard_types.py
+-rw-r--r--   0 runner    (1001) docker     (121)    55356 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/repository.py
+-rw-r--r--   0 runner    (1001) docker     (121)      473 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/snapshot_download.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 15:37:04.456654 huggingface_hub-0.9.1/src/huggingface_hub/utils/
+-rw-r--r--   0 runner    (1001) docker     (121)     1083 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2635 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/_datetime.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3543 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/_deprecation.py
+-rw-r--r--   0 runner    (1001) docker     (121)     6854 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/_errors.py
+-rw-r--r--   0 runner    (1001) docker     (121)      394 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/_fixes.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4415 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/_paths.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1952 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/_subprocess.py
+-rw-r--r--   0 runner    (1001) docker     (121)    12726 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/endpoint_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4880 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/logging.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1214 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/sha.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4088 2022-08-25 15:36:59.000000 huggingface_hub-0.9.1/src/huggingface_hub/utils/tqdm.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-08-25 15:37:04.456654 huggingface_hub-0.9.1/src/huggingface_hub.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     3888 2022-08-25 15:37:04.000000 huggingface_hub-0.9.1/src/huggingface_hub.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     1447 2022-08-25 15:37:04.000000 huggingface_hub-0.9.1/src/huggingface_hub.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-08-25 15:37:04.000000 huggingface_hub-0.9.1/src/huggingface_hub.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       83 2022-08-25 15:37:04.000000 huggingface_hub-0.9.1/src/huggingface_hub.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      532 2022-08-25 15:37:04.000000 huggingface_hub-0.9.1/src/huggingface_hub.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)       16 2022-08-25 15:37:04.000000 huggingface_hub-0.9.1/src/huggingface_hub.egg-info/top_level.txt
```

### Comparing `huggingface_hub-0.9.0rc3/LICENSE` & `huggingface_hub-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/PKG-INFO` & `huggingface_hub-0.9.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: huggingface_hub
-Version: 0.9.0rc3
+Version: 0.9.1
 Summary: Client library to download and publish models, datasets and other repos on the huggingface.co hub
 Home-page: https://github.com/huggingface/huggingface_hub
 Author: Hugging Face, Inc.
 Author-email: julien@huggingface.co
 License: Apache
 Keywords: model-hub machine-learning models natural-language-processing deep-learning pytorch pretrained-models
 Platform: UNKNOWN
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: huggingface_hub Version: 0.9.0rc3 Summary: Client
+Metadata-Version: 2.1 Name: huggingface_hub Version: 0.9.1 Summary: Client
 library to download and publish models, datasets and other repos on the
 huggingface.co hub Home-page: https://github.com/huggingface/huggingface_hub
 Author: Hugging Face, Inc. Author-email: julien@huggingface.co License: Apache
 Keywords: model-hub machine-learning models natural-language-processing deep-
 learning pytorch pretrained-models Platform: UNKNOWN Classifier: Intended
 Audience :: Developers Classifier: Intended Audience :: Education Classifier:
 Intended Audience :: Science/Research Classifier: License :: OSI Approved ::
```

### Comparing `huggingface_hub-0.9.0rc3/README.md` & `huggingface_hub-0.9.1/README.md`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/setup.cfg` & `huggingface_hub-0.9.1/setup.cfg`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/setup.py` & `huggingface_hub-0.9.1/setup.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/__init__.py` & `huggingface_hub-0.9.1/src/huggingface_hub/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -112,15 +112,15 @@
             __getattr__(attr)
 
     return __getattr__, __dir__, list(__all__)
 
 
 # ************
 
-__version__ = "0.9.0.rc3"
+__version__ = "0.9.1"
 
 
 __getattr__, __dir__, __all__ = _attach(
     __name__,
     submodules=[],
     submod_attrs={
         "commands.user": ["notebook_login"],
```

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/_commit_api.py` & `huggingface_hub-0.9.1/src/huggingface_hub/_commit_api.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/_snapshot_download.py` & `huggingface_hub-0.9.1/src/huggingface_hub/_snapshot_download.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/commands/__init__.py` & `huggingface_hub-0.9.1/src/huggingface_hub/commands/__init__.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/commands/huggingface_cli.py` & `huggingface_hub-0.9.1/src/huggingface_hub/commands/huggingface_cli.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/commands/lfs.py` & `huggingface_hub-0.9.1/src/huggingface_hub/commands/lfs.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/commands/user.py` & `huggingface_hub-0.9.1/src/huggingface_hub/commands/user.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/community.py` & `huggingface_hub-0.9.1/src/huggingface_hub/community.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/constants.py` & `huggingface_hub-0.9.1/src/huggingface_hub/constants.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/fastai_utils.py` & `huggingface_hub-0.9.1/src/huggingface_hub/fastai_utils.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/file_download.py` & `huggingface_hub-0.9.1/src/huggingface_hub/file_download.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/hf_api.py` & `huggingface_hub-0.9.1/src/huggingface_hub/hf_api.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/hub_mixin.py` & `huggingface_hub-0.9.1/src/huggingface_hub/hub_mixin.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/inference_api.py` & `huggingface_hub-0.9.1/src/huggingface_hub/inference_api.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/keras_mixin.py` & `huggingface_hub-0.9.1/src/huggingface_hub/keras_mixin.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/lfs.py` & `huggingface_hub-0.9.1/src/huggingface_hub/lfs.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/repocard.py` & `huggingface_hub-0.9.1/src/huggingface_hub/repocard.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/repocard_types.py` & `huggingface_hub-0.9.1/src/huggingface_hub/repocard_types.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/repository.py` & `huggingface_hub-0.9.1/src/huggingface_hub/repository.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/__init__.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/__init__.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_datetime.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/_datetime.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_deprecation.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/_deprecation.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_errors.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/_errors.py`

 * *Files 6% similar despite different names*

```diff
@@ -8,15 +8,15 @@
     Raised when trying to access a hf.co URL with an invalid repository name, or
     with a private repo name the user does not have access to.
 
     Example:
 
     ```py
     >>> from huggingface_hub import model_info
-    >>> model_info("<non_existant_repository>")
+    >>> model_info("<non_existent_repository>")
     huggingface_hub.utils._errors.RepositoryNotFoundError: 404 Client Error: Repository Not Found for url: <url>
     ```
     """
 
     def __init__(self, message, response):
         super().__init__(message, response=response)
 
@@ -26,15 +26,15 @@
     Raised when trying to access a hf.co URL with a valid repository but an invalid
     revision.
 
     Example:
 
     ```py
     >>> from huggingface_hub import hf_hub_download
-    >>> hf_hub_download('bert-base-cased', 'config.json', revision='<non-existant-revision>')
+    >>> hf_hub_download('bert-base-cased', 'config.json', revision='<non-existent-revision>')
     huggingface_hub.utils._errors.RevisionNotFoundError: 404 Client Error: Revision Not Found for url: <url>
     ```
     """
 
     def __init__(self, message, response):
         super().__init__(message, response=response)
 
@@ -44,15 +44,15 @@
     Raised when trying to access a hf.co URL with a valid repository and revision
     but an invalid filename.
 
     Example:
 
     ```py
     >>> from huggingface_hub import hf_hub_download
-    >>> hf_hub_download('bert-base-cased', '<non-existant-file>')
+    >>> hf_hub_download('bert-base-cased', '<non-existent-file>')
     huggingface_hub.utils._errors.EntryNotFoundError: 404 Client Error: Entry Not Found for url: <url>
     ```
     """
 
     def __init__(self, message, response):
         super().__init__(message, response=response)
 
@@ -97,14 +97,34 @@
 
 
 def _add_request_id_to_error_args(e, request_id):
     if request_id is not None and len(e.args) > 0 and isinstance(e.args[0], str):
         e.args = (e.args[0] + f" (Request ID: {request_id})",) + e.args[1:]
 
 
+def _add_server_message_to_error_args(e: HTTPError, response: Response):
+    """
+    If the server response raises an HTTPError, we try to decode the response body and
+    find an error message. If the server returned one, it is added to the HTTPError
+    message.
+    """
+    try:
+        server_message = response.json().get("error", None)
+    except JSONDecodeError:
+        return
+
+    if (
+        server_message is not None
+        and len(server_message) > 0
+        and len(e.args) > 0
+        and isinstance(e.args[0], str)
+    ):
+        e.args = (e.args[0] + "\n\n" + str(server_message),) + e.args[1:]
+
+
 def _raise_for_status(response):
     """
     Internal version of `response.raise_for_status()` that will refine a
     potential HTTPError.
     """
     request_id = response.headers.get("X-Request-Id")
     try:
@@ -140,14 +160,15 @@
                 f"{response.status_code} Client Error: Repository Not Found for url:"
                 f" {response.url}. If the repo is private, make sure you are"
                 " authenticated."
             )
             e = RepositoryNotFoundError(message, response)
 
         _add_request_id_to_error_args(e, request_id)
+        _add_server_message_to_error_args(e, response)
 
         raise e
 
 
 def _raise_with_request_id(request):
     request_id = request.headers.get("X-Request-Id")
     try:
```

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_paths.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/_paths.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/_subprocess.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/_subprocess.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/endpoint_helpers.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/endpoint_helpers.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/logging.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/logging.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/sha.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/sha.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub/utils/tqdm.py` & `huggingface_hub-0.9.1/src/huggingface_hub/utils/tqdm.py`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/PKG-INFO` & `huggingface_hub-0.9.1/src/huggingface_hub.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: huggingface-hub
-Version: 0.9.0rc3
+Version: 0.9.1
 Summary: Client library to download and publish models, datasets and other repos on the huggingface.co hub
 Home-page: https://github.com/huggingface/huggingface_hub
 Author: Hugging Face, Inc.
 Author-email: julien@huggingface.co
 License: Apache
 Keywords: model-hub machine-learning models natural-language-processing deep-learning pytorch pretrained-models
 Platform: UNKNOWN
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: huggingface-hub Version: 0.9.0rc3 Summary: Client
+Metadata-Version: 2.1 Name: huggingface-hub Version: 0.9.1 Summary: Client
 library to download and publish models, datasets and other repos on the
 huggingface.co hub Home-page: https://github.com/huggingface/huggingface_hub
 Author: Hugging Face, Inc. Author-email: julien@huggingface.co License: Apache
 Keywords: model-hub machine-learning models natural-language-processing deep-
 learning pytorch pretrained-models Platform: UNKNOWN Classifier: Intended
 Audience :: Developers Classifier: Intended Audience :: Education Classifier:
 Intended Audience :: Science/Research Classifier: License :: OSI Approved ::
```

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/SOURCES.txt` & `huggingface_hub-0.9.1/src/huggingface_hub.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `huggingface_hub-0.9.0rc3/src/huggingface_hub.egg-info/requires.txt` & `huggingface_hub-0.9.1/src/huggingface_hub.egg-info/requires.txt`

 * *Files identical despite different names*

