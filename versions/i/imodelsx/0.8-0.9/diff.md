# Comparing `tmp/imodelsx-0.8.tar.gz` & `tmp/imodelsx-0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "imodelsx-0.8.tar", last modified: Wed Feb  1 01:22:02 2023, max compression
+gzip compressed data, was "imodelsx-0.9.tar", last modified: Fri Feb  3 17:27:40 2023, max compression
```

## Comparing `imodelsx-0.8.tar` & `imodelsx-0.9.tar`

### file list

```diff
@@ -1,34 +1,35 @@
-drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-01 01:22:02.568938 imodelsx-0.8/
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     8193 2023-02-01 01:22:02.568938 imodelsx-0.8/PKG-INFO
-drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-01 01:22:02.568938 imodelsx-0.8/imodelsx/
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)      237 2023-01-31 05:36:51.000000 imodelsx-0.8/imodelsx/__init__.py
-drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-01 01:22:02.568938 imodelsx-0.8/imodelsx/d3/
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2022-10-04 21:38:29.000000 imodelsx-0.8/imodelsx/d3/__init__.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     4313 2022-10-31 04:22:01.000000 imodelsx-0.8/imodelsx/d3/d3.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     7246 2022-10-04 22:03:12.000000 imodelsx-0.8/imodelsx/d3/step1_get_extreme.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     7194 2022-10-04 22:27:59.000000 imodelsx-0.8/imodelsx/d3/step2_proposer.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     8982 2022-10-04 22:12:36.000000 imodelsx-0.8/imodelsx/d3/step3_verifier.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     4009 2023-02-01 00:47:38.000000 imodelsx-0.8/imodelsx/data.py
-drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-01 01:22:02.568938 imodelsx-0.8/imodelsx/embgam/
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2022-10-04 23:40:44.000000 imodelsx-0.8/imodelsx/embgam/__init__.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     4927 2023-01-31 05:38:49.000000 imodelsx-0.8/imodelsx/embgam/embed.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    11088 2023-01-31 05:36:04.000000 imodelsx-0.8/imodelsx/embgam/embgam.py
-drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-01 01:22:02.568938 imodelsx-0.8/imodelsx/iprompt/
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)      195 2022-10-15 16:18:36.000000 imodelsx-0.8/imodelsx/iprompt/__init__.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    26467 2023-01-24 22:08:17.000000 imodelsx-0.8/imodelsx/iprompt/api.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     9661 2022-10-15 16:18:36.000000 imodelsx-0.8/imodelsx/iprompt/autoprompt.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)      461 2022-10-21 19:39:19.000000 imodelsx-0.8/imodelsx/iprompt/data.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     2371 2022-10-15 16:18:36.000000 imodelsx-0.8/imodelsx/iprompt/gumbel.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    13745 2022-12-16 22:11:36.000000 imodelsx-0.8/imodelsx/iprompt/hotflip.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    17577 2023-01-24 22:08:17.000000 imodelsx-0.8/imodelsx/iprompt/ipromptx.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     1751 2022-10-15 16:18:36.000000 imodelsx-0.8/imodelsx/iprompt/prompt_tune.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    22909 2022-12-16 20:18:05.000000 imodelsx-0.8/imodelsx/iprompt/utils.py
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     2707 2023-01-31 05:46:12.000000 imodelsx-0.8/imodelsx/util.py
-drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-01 01:22:02.568938 imodelsx-0.8/imodelsx.egg-info/
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     8193 2023-02-01 01:22:02.000000 imodelsx-0.8/imodelsx.egg-info/PKG-INFO
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)      687 2023-02-01 01:22:02.000000 imodelsx-0.8/imodelsx.egg-info/SOURCES.txt
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        1 2023-02-01 01:22:02.000000 imodelsx-0.8/imodelsx.egg-info/dependency_links.txt
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)       94 2023-02-01 01:22:02.000000 imodelsx-0.8/imodelsx.egg-info/requires.txt
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        9 2023-02-01 01:22:02.000000 imodelsx-0.8/imodelsx.egg-info/top_level.txt
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)       38 2023-02-01 01:22:02.568938 imodelsx-0.8/setup.cfg
--rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     1080 2023-02-01 01:21:25.000000 imodelsx-0.8/setup.py
+drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-03 17:27:40.506288 imodelsx-0.9/
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     8193 2023-02-03 17:27:40.506288 imodelsx-0.9/PKG-INFO
+drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-03 17:27:40.506288 imodelsx-0.9/imodelsx/
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)      237 2023-01-31 05:36:51.000000 imodelsx-0.9/imodelsx/__init__.py
+drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-03 17:27:40.506288 imodelsx-0.9/imodelsx/d3/
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2022-10-04 21:38:29.000000 imodelsx-0.9/imodelsx/d3/__init__.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     4313 2022-10-31 04:22:01.000000 imodelsx-0.9/imodelsx/d3/d3.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     7246 2022-10-04 22:03:12.000000 imodelsx-0.9/imodelsx/d3/step1_get_extreme.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     7194 2022-10-04 22:27:59.000000 imodelsx-0.9/imodelsx/d3/step2_proposer.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     8982 2022-10-04 22:12:36.000000 imodelsx-0.9/imodelsx/d3/step3_verifier.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     4934 2023-02-02 05:59:06.000000 imodelsx-0.9/imodelsx/data.py
+drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-03 17:27:40.506288 imodelsx-0.9/imodelsx/embgam/
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2022-10-04 23:40:44.000000 imodelsx-0.9/imodelsx/embgam/__init__.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     4927 2023-01-31 05:38:49.000000 imodelsx-0.9/imodelsx/embgam/embed.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    11088 2023-01-31 05:36:04.000000 imodelsx-0.9/imodelsx/embgam/embgam.py
+drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-03 17:27:40.506288 imodelsx-0.9/imodelsx/iprompt/
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)      195 2022-10-15 16:18:36.000000 imodelsx-0.9/imodelsx/iprompt/__init__.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    26467 2023-01-24 22:08:17.000000 imodelsx-0.9/imodelsx/iprompt/api.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     9661 2022-10-15 16:18:36.000000 imodelsx-0.9/imodelsx/iprompt/autoprompt.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)      461 2022-10-21 19:39:19.000000 imodelsx-0.9/imodelsx/iprompt/data.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     2371 2022-10-15 16:18:36.000000 imodelsx-0.9/imodelsx/iprompt/gumbel.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    13745 2022-12-16 22:11:36.000000 imodelsx-0.9/imodelsx/iprompt/hotflip.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    17577 2023-01-24 22:08:17.000000 imodelsx-0.9/imodelsx/iprompt/ipromptx.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     1751 2022-10-15 16:18:36.000000 imodelsx-0.9/imodelsx/iprompt/prompt_tune.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)    22909 2022-12-16 20:18:05.000000 imodelsx-0.9/imodelsx/iprompt/utils.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     5654 2023-02-02 06:39:15.000000 imodelsx-0.9/imodelsx/submit_utils.py
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     2707 2023-01-31 05:46:12.000000 imodelsx-0.9/imodelsx/util.py
+drwxr-xr-x   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        0 2023-02-03 17:27:40.506288 imodelsx-0.9/imodelsx.egg-info/
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     8193 2023-02-03 17:27:40.000000 imodelsx-0.9/imodelsx.egg-info/PKG-INFO
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)      712 2023-02-03 17:27:40.000000 imodelsx-0.9/imodelsx.egg-info/SOURCES.txt
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        1 2023-02-03 17:27:40.000000 imodelsx-0.9/imodelsx.egg-info/dependency_links.txt
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)       94 2023-02-03 17:27:40.000000 imodelsx-0.9/imodelsx.egg-info/requires.txt
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)        9 2023-02-03 17:27:40.000000 imodelsx-0.9/imodelsx.egg-info/top_level.txt
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)       38 2023-02-03 17:27:40.506288 imodelsx-0.9/setup.cfg
+-rw-r--r--   0 REDMOND.chansingh (560039895) REDMOND.domain users (500000513)     1080 2023-02-03 17:27:13.000000 imodelsx-0.9/setup.py
```

### Comparing `imodelsx-0.8/PKG-INFO` & `imodelsx-0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: imodelsx
-Version: 0.8
+Version: 0.9
 Summary: Library to explain a dataset in natural language.
 Home-page: https://github.com/csinva/imodelsX
 Author: Chandan Singh, John X. Morris, Armin Askari
 Author-email: chansingh@microsoft.com
 License: UNKNOWN
 Description: <p align="center">  <img src="https://csinva.io/emb-gam/embgam_gif.gif" width="18%"> 
         <img align="center" width=40% src="https://csinva.io/imodelsX/imodelsx_logo.svg?sanitize=True&kill_cache=1"> </img>	<img src="https://csinva.io/emb-gam/embgam_gif.gif" width="18%"></p>
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: imodelsx Version: 0.8 Summary: Library to explain a
+Metadata-Version: 2.1 Name: imodelsx Version: 0.9 Summary: Library to explain a
 dataset in natural language. Home-page: https://github.com/csinva/imodelsX
 Author: Chandan Singh, John X. Morris, Armin Askari Author-email:
 chansingh@microsoft.com License: UNKNOWN Description:
     [https://csinva.io/emb-gam/embgam_gif.gif] [https://csinva.io/imodelsX/
    imodelsx_logo.svg?sanitize=True&kill_cache=1] [https://csinva.io/emb-gam/
                                 embgam_gif.gif]
                Library to explain a dataset in natural language.
```

### Comparing `imodelsx-0.8/imodelsx/d3/d3.py` & `imodelsx-0.9/imodelsx/d3/d3.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/d3/step1_get_extreme.py` & `imodelsx-0.9/imodelsx/d3/step1_get_extreme.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/d3/step2_proposer.py` & `imodelsx-0.9/imodelsx/d3/step2_proposer.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/d3/step3_verifier.py` & `imodelsx-0.9/imodelsx/d3/step3_verifier.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/data.py` & `imodelsx-0.9/imodelsx/data.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,30 +1,38 @@
 import datasets
 import numpy as np
 from sklearn.model_selection import train_test_split
 from sklearn.feature_extraction.text import CountVectorizer
 
 
 def load_huggingface_dataset(
-    dataset_name: str, subsample_frac: float = 1.0,
-    binary_classification: bool = False
+    dataset_name: str,
+    subsample_frac: float = 1.0,
+    binary_classification: bool = False,
+    return_lists: bool = False,
 ):
     """Load text dataset from huggingface (with train/validation splits) + return the relevant dataset key
     Params
     ------
+    subsample_frac: float
+        Only use this fraction of the training data
     binary_classification: bool
         Whether to convert a multiclass task into a binary one
         Unless this function is modified, will take the class number with the lowest to indexes
+    return_lists: bool
+        Whether to return pre-split lists rather than HF dataset
 
-    Some examples       |    n_train     |    n_classes
+    Some examples       |    n_train     |    n_classes |
     rotten_tomatoes     |    ~9k         |    2
     sst2                |    ~68k        |    2
+    imdb                |    ~25k        |    2         | note: these are relatively long
     tweet_eval          |    ~10k        |    2
     financial_phrasebank|    ~2.3k       |    3
     emotion             |    ~18k        |    6
+    ag_news             |    ~120k       |    4
     """
     # load dset
     if dataset_name == 'tweet_eval':
         dset = datasets.load_dataset('tweet_eval', 'hate')
     elif dataset_name == 'financial_phrasebank':
         train = datasets.load_dataset('financial_phrasebank', 'sentences_75agree',
                                       revision='main', split='train')
@@ -39,16 +47,18 @@
     # process dset
     dataset_key_text = 'text'
     if dataset_name == 'sst2':
         dataset_key_text = 'sentence'
     elif dataset_name == 'financial_phrasebank':
         dataset_key_text = 'sentence'
     elif dataset_name == 'imdb':
-        del dset['unsupervised']
         dset['validation'] = dset['test']
+    elif dataset_name == 'ag_news':
+        dset['validation'] = dset['test']
+
 
     # subsample data
     if subsample_frac > 0:
         n = len(dset['train'])
         dset['train'] = dset['train'].select(np.random.choice(
             range(n), replace=False,
             size=int(n * subsample_frac)
@@ -62,42 +72,55 @@
                 2: 0, # positive
             }
         elif dataset_name == 'emotion':
             labels_to_keep_remap = {
                 0: 0, # sadness
                 1: 1, # joy
             }
+        elif dataset_name == 'ag_news':
+            labels_to_keep_remap = {
+                # 1 was "world" and 4 was "sci/tech"
+                2: 0, # 2 was "sports"
+                3: 1, # 3 was "business"
+            }
         else:
             labels_to_keep_keys = np.sort(np.unique(dset['train']['label']))[:2]
             labels_to_keep_remap = {
                 labels_to_keep_keys[i]: i for i in range(2)
             }
         
         # filter dset labels to only keep these labels
         dset['train'] = dset['train'].filter(lambda ex: ex["label"] in labels_to_keep_remap)
         dset['validation'] = dset['validation'].filter(lambda ex: ex["label"] in labels_to_keep_remap)
 
         # map these labels to 0/1
         dset['train'] = dset['train'].map(lambda ex: {'label': labels_to_keep_remap[ex['label']]})
         dset['validation'] = dset['validation'].map(lambda ex: {'label': labels_to_keep_remap[ex['label']]})
     
-    return dset, dataset_key_text
+    if return_lists:
+        X_train_text= dset['train'][dataset_key_text]
+        y_train = np.array(dset['train']['label'])
+        X_test_text = dset['validation'][dataset_key_text]
+        y_test = np.array(dset['validation']['label'])
+        return X_train_text, X_test_text, y_train, y_test
+    else:
+        return dset, dataset_key_text
 
 
 def convert_text_data_to_counts_array(dset, dataset_key_text):
     v = CountVectorizer()
     X_train = v.fit_transform(dset['train'][dataset_key_text])
     y_train = dset['train']['label']
     X_test = v.transform(dset['validation'][dataset_key_text])
     y_test = dset['validation']['label']
     feature_names = v.get_feature_names_out().tolist()
     return X_train, X_test, y_train, y_test, feature_names
 
 if __name__ == '__main__':
-    dset, k = load_huggingface_dataset('emotion', 1, binary_classification=False)
+    dset, k = load_huggingface_dataset('ag_news', 1, binary_classification=False)
     print(dset)
     print(dset['train'])
     print(np.unique(dset['train']['label']))
 
-    dset, k = load_huggingface_dataset('emotion', 1, binary_classification=True)
+    dset, k = load_huggingface_dataset('ag_news', 1, binary_classification=True)
     print(dset)
     print(np.unique(dset['train']['label']))
```

### Comparing `imodelsx-0.8/imodelsx/embgam/embed.py` & `imodelsx-0.9/imodelsx/embgam/embed.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/embgam/embgam.py` & `imodelsx-0.9/imodelsx/embgam/embgam.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/iprompt/api.py` & `imodelsx-0.9/imodelsx/iprompt/api.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/iprompt/autoprompt.py` & `imodelsx-0.9/imodelsx/iprompt/autoprompt.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/iprompt/gumbel.py` & `imodelsx-0.9/imodelsx/iprompt/gumbel.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/iprompt/hotflip.py` & `imodelsx-0.9/imodelsx/iprompt/hotflip.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/iprompt/ipromptx.py` & `imodelsx-0.9/imodelsx/iprompt/ipromptx.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/iprompt/prompt_tune.py` & `imodelsx-0.9/imodelsx/iprompt/prompt_tune.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/iprompt/utils.py` & `imodelsx-0.9/imodelsx/iprompt/utils.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx/util.py` & `imodelsx-0.9/imodelsx/util.py`

 * *Files identical despite different names*

### Comparing `imodelsx-0.8/imodelsx.egg-info/PKG-INFO` & `imodelsx-0.9/imodelsx.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: imodelsx
-Version: 0.8
+Version: 0.9
 Summary: Library to explain a dataset in natural language.
 Home-page: https://github.com/csinva/imodelsX
 Author: Chandan Singh, John X. Morris, Armin Askari
 Author-email: chansingh@microsoft.com
 License: UNKNOWN
 Description: <p align="center">  <img src="https://csinva.io/emb-gam/embgam_gif.gif" width="18%"> 
         <img align="center" width=40% src="https://csinva.io/imodelsX/imodelsx_logo.svg?sanitize=True&kill_cache=1"> </img>	<img src="https://csinva.io/emb-gam/embgam_gif.gif" width="18%"></p>
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: imodelsx Version: 0.8 Summary: Library to explain a
+Metadata-Version: 2.1 Name: imodelsx Version: 0.9 Summary: Library to explain a
 dataset in natural language. Home-page: https://github.com/csinva/imodelsX
 Author: Chandan Singh, John X. Morris, Armin Askari Author-email:
 chansingh@microsoft.com License: UNKNOWN Description:
     [https://csinva.io/emb-gam/embgam_gif.gif] [https://csinva.io/imodelsX/
    imodelsx_logo.svg?sanitize=True&kill_cache=1] [https://csinva.io/emb-gam/
                                 embgam_gif.gif]
                Library to explain a dataset in natural language.
```

### Comparing `imodelsx-0.8/imodelsx.egg-info/SOURCES.txt` & `imodelsx-0.9/imodelsx.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,11 @@
 setup.py
 imodelsx/__init__.py
 imodelsx/data.py
+imodelsx/submit_utils.py
 imodelsx/util.py
 imodelsx.egg-info/PKG-INFO
 imodelsx.egg-info/SOURCES.txt
 imodelsx.egg-info/dependency_links.txt
 imodelsx.egg-info/requires.txt
 imodelsx.egg-info/top_level.txt
 imodelsx/d3/__init__.py
```

### Comparing `imodelsx-0.8/setup.py` & `imodelsx-0.9/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -17,15 +17,15 @@
     'torch',
     'tqdm',
     'transformers[torch] >= 4.23.1',
 ]
 
 setuptools.setup(
     name="imodelsx",
-    version="0.08",
+    version="0.09",
     author="Chandan Singh, John X. Morris, Armin Askari",
     author_email="chansingh@microsoft.com",
     description="Library to explain a dataset in natural language.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/csinva/imodelsX",
     packages=setuptools.find_packages(
```

