# Comparing `tmp/pytorch_nlp_pipeline-0.1.8.tar.gz` & `tmp/pytorch_nlp_pipeline-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pytorch_nlp_pipeline-0.1.8.tar", last modified: Tue Mar 21 18:28:54 2023, max compression
+gzip compressed data, was "pytorch_nlp_pipeline-0.1.9.tar", last modified: Tue Mar 21 23:08:51 2023, max compression
```

## Comparing `pytorch_nlp_pipeline-0.1.8.tar` & `pytorch_nlp_pipeline-0.1.9.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 18:28:54.930725 pytorch_nlp_pipeline-0.1.8/
--rw-r--r--   0 M255032    (505) staff       (20)     1061 2023-03-01 23:53:28.000000 pytorch_nlp_pipeline-0.1.8/LICENSE.txt
--rw-r--r--   0 M255032    (505) staff       (20)      291 2023-03-21 18:28:54.930934 pytorch_nlp_pipeline-0.1.8/PKG-INFO
--rw-r--r--   0 M255032    (505) staff       (20)       47 2023-03-01 23:53:28.000000 pytorch_nlp_pipeline-0.1.8/README.md
-drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 18:28:54.889807 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/
--rw-r--r--   0 M255032    (505) staff       (20)        0 2023-02-13 16:55:40.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/__init__.py
--rw-r--r--   0 M255032    (505) staff       (20)    19057 2023-03-21 18:25:51.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/classification.py
-drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 18:28:54.925375 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/dataset/
--rw-r--r--   0 M255032    (505) staff       (20)     1000 2023-03-21 18:26:31.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/dataset/__init__.py
--rw-r--r--   0 M255032    (505) staff       (20)     3052 2023-03-11 04:31:16.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/dataset/core.py
--rw-r--r--   0 M255032    (505) staff       (20)     1984 2023-03-11 04:36:02.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/dataset/utils.py
-drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 18:28:54.928998 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/model/
--rw-r--r--   0 M255032    (505) staff       (20)     4127 2023-03-21 18:26:14.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/model/__init__.py
--rw-r--r--   0 M255032    (505) staff       (20)     4911 2023-03-14 18:03:12.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/utils.py
-drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 18:28:54.910746 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline.egg-info/
--rw-r--r--   0 M255032    (505) staff       (20)      291 2023-03-21 18:28:54.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline.egg-info/PKG-INFO
--rw-r--r--   0 M255032    (505) staff       (20)      516 2023-03-21 18:28:54.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline.egg-info/SOURCES.txt
--rw-r--r--   0 M255032    (505) staff       (20)        1 2023-03-21 18:28:54.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline.egg-info/dependency_links.txt
--rw-r--r--   0 M255032    (505) staff       (20)       87 2023-03-21 18:28:54.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline.egg-info/requires.txt
--rw-r--r--   0 M255032    (505) staff       (20)       21 2023-03-21 18:28:54.000000 pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline.egg-info/top_level.txt
--rw-r--r--   0 M255032    (505) staff       (20)       79 2023-03-21 18:28:54.936833 pytorch_nlp_pipeline-0.1.8/setup.cfg
--rw-r--r--   0 M255032    (505) staff       (20)      817 2023-03-21 18:26:03.000000 pytorch_nlp_pipeline-0.1.8/setup.py
+drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 23:08:51.450609 pytorch_nlp_pipeline-0.1.9/
+-rw-r--r--   0 M255032    (505) staff       (20)     1061 2023-03-01 23:53:28.000000 pytorch_nlp_pipeline-0.1.9/LICENSE.txt
+-rw-r--r--   0 M255032    (505) staff       (20)      291 2023-03-21 23:08:51.450851 pytorch_nlp_pipeline-0.1.9/PKG-INFO
+-rw-r--r--   0 M255032    (505) staff       (20)       47 2023-03-01 23:53:28.000000 pytorch_nlp_pipeline-0.1.9/README.md
+drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 23:08:51.387761 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/
+-rw-r--r--   0 M255032    (505) staff       (20)        0 2023-02-13 16:55:40.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/__init__.py
+-rw-r--r--   0 M255032    (505) staff       (20)    19057 2023-03-21 18:25:51.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/classification.py
+drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 23:08:51.430145 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/dataset/
+-rw-r--r--   0 M255032    (505) staff       (20)     1000 2023-03-21 18:26:31.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/dataset/__init__.py
+-rw-r--r--   0 M255032    (505) staff       (20)     3039 2023-03-21 23:07:05.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/dataset/core.py
+-rw-r--r--   0 M255032    (505) staff       (20)     1971 2023-03-21 23:07:14.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/dataset/utils.py
+drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 23:08:51.447211 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/model/
+-rw-r--r--   0 M255032    (505) staff       (20)     4127 2023-03-21 18:26:14.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/model/__init__.py
+-rw-r--r--   0 M255032    (505) staff       (20)     5128 2023-03-21 23:06:25.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/utils.py
+drwxr-xr-x   0 M255032    (505) staff       (20)        0 2023-03-21 23:08:51.411168 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline.egg-info/
+-rw-r--r--   0 M255032    (505) staff       (20)      291 2023-03-21 23:08:50.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline.egg-info/PKG-INFO
+-rw-r--r--   0 M255032    (505) staff       (20)      516 2023-03-21 23:08:50.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline.egg-info/SOURCES.txt
+-rw-r--r--   0 M255032    (505) staff       (20)        1 2023-03-21 23:08:50.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline.egg-info/dependency_links.txt
+-rw-r--r--   0 M255032    (505) staff       (20)       87 2023-03-21 23:08:50.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline.egg-info/requires.txt
+-rw-r--r--   0 M255032    (505) staff       (20)       21 2023-03-21 23:08:50.000000 pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline.egg-info/top_level.txt
+-rw-r--r--   0 M255032    (505) staff       (20)       79 2023-03-21 23:08:51.462651 pytorch_nlp_pipeline-0.1.9/setup.cfg
+-rw-r--r--   0 M255032    (505) staff       (20)      817 2023-03-21 23:07:53.000000 pytorch_nlp_pipeline-0.1.9/setup.py
```

### Comparing `pytorch_nlp_pipeline-0.1.8/LICENSE.txt` & `pytorch_nlp_pipeline-0.1.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/classification.py` & `pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/classification.py`

 * *Files identical despite different names*

### Comparing `pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/dataset/__init__.py` & `pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/dataset/__init__.py`

 * *Files identical despite different names*

### Comparing `pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/dataset/core.py` & `pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/dataset/core.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 import torch
 from torch.utils.data import Dataset, DataLoader
 import logging
 
-WORKER = '[bold]DATAMODULE[/bold]'
+WORKER = 'DataModule'
 
 class TorchDataset(Dataset):
     """
     Build torch dataset
     
     Input:
         texts:
```

### Comparing `pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/dataset/utils.py` & `pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/dataset/utils.py`

 * *Files 7% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from sklearn.model_selection import train_test_split
 import logging
 import pandas as pd
 
-WORKER = '[bold]DATAMODULE[/bold]'
+WORKER = 'DataModule'
 
 def split_data_w_sample(df: pd.DataFrame, 
                         label_col: str, 
                         random_seed: int, 
                         stratify_col: str,
                         test_size = 0.1,
                         sample = None):
```

### Comparing `pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/model/__init__.py` & `pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/model/__init__.py`

 * *Files identical despite different names*

### Comparing `pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline/utils.py` & `pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline/utils.py`

 * *Files 6% similar despite different names*

```diff
@@ -40,17 +40,21 @@
 
     if not os.path.isdir(save_path_final):
         os.mkdir(save_path_final) # create directory for model if not exist
     
     # save torch model TODO
     if save_mode is None:
         torch.save(model.state_dict(), os.path.join(save_path_final, model_id + '-' + 'model.bin'))  # save model
+
+        if type(model) == torch.nn.DataParallel:
+            torch.save(model.module.state_dict(), os.path.join(save_path_final, model_id + '-' + 'model.bin'))
+        else:
+            torch.save(model.state_dict(), os.path.join(save_path_final, model_id + '-' + 'model.bin'))
     elif save_mode == 'body-only':
         # only save embedding part
-        #TODO might need debug - might need to create the dir
         if type(model) == torch.nn.DataParallel:
             model.module.pretrained.save_pretrained(save_path_final)
         else:
             model.pretrained.save_pretrained(save_path_final)
     elif save_mode == 'head-only':
         # only save head
         if type(model) == torch.nn.DataParallel:
```

### Comparing `pytorch_nlp_pipeline-0.1.8/pytorch_nlp_pipeline.egg-info/SOURCES.txt` & `pytorch_nlp_pipeline-0.1.9/pytorch_nlp_pipeline.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pytorch_nlp_pipeline-0.1.8/setup.py` & `pytorch_nlp_pipeline-0.1.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 from setuptools import setup, find_packages
 
 
-VERSION = '0.1.8' 
+VERSION = '0.1.9' 
 DESCRIPTION = 'abstracted ML pipelines based on pytorch'
 LONG_DESCRIPTION = 'abstracted ML pipelines based on pytorch - mainly for text classification'
 
 # Setting up
 setup(
        # the name must match the folder name 'verysimplemodule'
         name="pytorch_nlp_pipeline",
```

