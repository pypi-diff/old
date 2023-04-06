# Comparing `tmp/misc_utils_aath-0.2.tar.gz` & `tmp/misc_utils_aath-0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "misc_utils_aath-0.2.tar", last modified: Thu Apr  6 23:07:46 2023, max compression
+gzip compressed data, was "misc_utils_aath-0.3.tar", last modified: Thu Apr  6 23:10:47 2023, max compression
```

## Comparing `misc_utils_aath-0.2.tar` & `misc_utils_aath-0.3.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxrwxr-x   0 saandeepaath  (1001) saandeepaath  (1001)        0 2023-04-06 23:07:46.645073 misc_utils_aath-0.2/
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      106 2023-04-06 23:07:46.645073 misc_utils_aath-0.2/PKG-INFO
-drwxrwxr-x   0 saandeepaath  (1001) saandeepaath  (1001)        0 2023-04-06 23:07:46.645073 misc_utils_aath-0.2/misc_utils_aath/
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      211 2023-04-06 23:07:21.000000 misc_utils_aath-0.2/misc_utils_aath/__init__.py
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)     4602 2023-04-06 23:07:20.000000 misc_utils_aath-0.2/misc_utils_aath/misc.py
-drwxrwxr-x   0 saandeepaath  (1001) saandeepaath  (1001)        0 2023-04-06 23:07:46.645073 misc_utils_aath-0.2/misc_utils_aath.egg-info/
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      106 2023-04-06 23:07:46.000000 misc_utils_aath-0.2/misc_utils_aath.egg-info/PKG-INFO
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      254 2023-04-06 23:07:46.000000 misc_utils_aath-0.2/misc_utils_aath.egg-info/SOURCES.txt
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)        1 2023-04-06 23:07:46.000000 misc_utils_aath-0.2/misc_utils_aath.egg-info/dependency_links.txt
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      132 2023-04-06 23:07:46.000000 misc_utils_aath-0.2/misc_utils_aath.egg-info/requires.txt
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)       16 2023-04-06 23:07:46.000000 misc_utils_aath-0.2/misc_utils_aath.egg-info/top_level.txt
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)       38 2023-04-06 23:07:46.645073 misc_utils_aath-0.2/setup.cfg
--rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      465 2023-04-06 23:07:44.000000 misc_utils_aath-0.2/setup.py
+drwxrwxr-x   0 saandeepaath  (1001) saandeepaath  (1001)        0 2023-04-06 23:10:47.564104 misc_utils_aath-0.3/
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      106 2023-04-06 23:10:47.564104 misc_utils_aath-0.3/PKG-INFO
+drwxrwxr-x   0 saandeepaath  (1001) saandeepaath  (1001)        0 2023-04-06 23:10:47.564104 misc_utils_aath-0.3/misc_utils_aath/
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      211 2023-04-06 23:07:21.000000 misc_utils_aath-0.3/misc_utils_aath/__init__.py
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)     4867 2023-04-06 23:10:14.000000 misc_utils_aath-0.3/misc_utils_aath/misc.py
+drwxrwxr-x   0 saandeepaath  (1001) saandeepaath  (1001)        0 2023-04-06 23:10:47.564104 misc_utils_aath-0.3/misc_utils_aath.egg-info/
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      106 2023-04-06 23:10:47.000000 misc_utils_aath-0.3/misc_utils_aath.egg-info/PKG-INFO
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      254 2023-04-06 23:10:47.000000 misc_utils_aath-0.3/misc_utils_aath.egg-info/SOURCES.txt
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)        1 2023-04-06 23:10:47.000000 misc_utils_aath-0.3/misc_utils_aath.egg-info/dependency_links.txt
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      146 2023-04-06 23:10:47.000000 misc_utils_aath-0.3/misc_utils_aath.egg-info/requires.txt
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)       16 2023-04-06 23:10:47.000000 misc_utils_aath-0.3/misc_utils_aath.egg-info/top_level.txt
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)       38 2023-04-06 23:10:47.564104 misc_utils_aath-0.3/setup.cfg
+-rw-rw-r--   0 saandeepaath  (1001) saandeepaath  (1001)      463 2023-04-06 23:10:45.000000 misc_utils_aath-0.3/setup.py
```

### Comparing `misc_utils_aath-0.2/misc_utils_aath/misc.py` & `misc_utils_aath-0.3/misc_utils_aath/misc.py`

 * *Files 12% similar despite different names*

```diff
@@ -7,14 +7,15 @@
 
 from sklearn.metrics import accuracy_score, f1_score, matthews_corrcoef, confusion_matrix
 
 import av
 import cv2
 import random 
 import numpy as np
+import torch 
 from umap import UMAP
 import pandas as pd
 import regex
 import plotly.express as px
 
 def match_files(mtc_str, fl_id):
   match_flg = 0
@@ -102,14 +103,24 @@
     os.mkdir(path)
 
 def read_json(path):
   with open(path, 'r') as fp:
     json_file = json.load(fp)
   return json_file
 
+
+def seed_everything(seed):
+  random.seed(seed)
+  os.environ['PYTHONHASHSEED'] = str(seed)
+  np.random.seed(seed)
+  torch.manual_seed(seed)
+  torch.cuda.manual_seed(seed)
+  torch.cuda.manual_seed_all(seed)
+  torch.backends.cudnn.deterministic = True
+
 def get_args():
   parser = argparse.ArgumentParser(description="Vision Transformers")
   parser.add_argument('--config', type=str, default='default', help='configuration to load')
   args = parser.parse_args()
   return args
 
 def get_metrics(y_true, y_pred):
```

