# Comparing `tmp/jax-dataloader-0.0.2.tar.gz` & `tmp/jax-dataloader-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/jax-dataloader-0.0.2.tar", last modified: Mon Mar  6 01:04:58 2023, max compression
+gzip compressed data, was "dist/jax-dataloader-0.0.3.tar", last modified: Fri Apr  7 00:16:48 2023, max compression
```

## Comparing `jax-dataloader-0.0.2.tar` & `jax-dataloader-0.0.3.tar`

### file list

```diff
@@ -1,20 +1,24 @@
-drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/
--rw-rw-r--   0 birk      (1000) birk      (1000)    11337 2022-09-05 16:31:43.000000 jax-dataloader-0.0.2/LICENSE
--rw-rw-r--   0 birk      (1000) birk      (1000)      111 2022-09-05 16:31:43.000000 jax-dataloader-0.0.2/MANIFEST.in
--rw-r--r--   0 birk      (1000) birk      (1000)     5072 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/PKG-INFO
--rw-r--r--   0 birk      (1000) birk      (1000)     4260 2023-03-06 00:56:44.000000 jax-dataloader-0.0.2/README.md
-drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/jax_dataloader/
--rw-r--r--   0 birk      (1000) birk      (1000)       44 2023-03-06 00:57:00.000000 jax-dataloader-0.0.2/jax_dataloader/__init__.py
--rw-r--r--   0 birk      (1000) birk      (1000)    10832 2023-03-06 00:57:00.000000 jax-dataloader-0.0.2/jax_dataloader/_modidx.py
--rw-r--r--   0 birk      (1000) birk      (1000)    13117 2023-03-06 00:57:00.000000 jax-dataloader-0.0.2/jax_dataloader/core.py
-drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/jax_dataloader.egg-info/
--rw-r--r--   0 birk      (1000) birk      (1000)     5072 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/jax_dataloader.egg-info/PKG-INFO
--rw-r--r--   0 birk      (1000) birk      (1000)      394 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/jax_dataloader.egg-info/SOURCES.txt
--rw-r--r--   0 birk      (1000) birk      (1000)        1 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/jax_dataloader.egg-info/dependency_links.txt
--rw-r--r--   0 birk      (1000) birk      (1000)       50 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/jax_dataloader.egg-info/entry_points.txt
--rw-r--r--   0 birk      (1000) birk      (1000)        1 2023-01-12 03:15:10.000000 jax-dataloader-0.0.2/jax_dataloader.egg-info/not-zip-safe
--rw-r--r--   0 birk      (1000) birk      (1000)       92 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/jax_dataloader.egg-info/requires.txt
--rw-r--r--   0 birk      (1000) birk      (1000)       15 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/jax_dataloader.egg-info/top_level.txt
--rw-r--r--   0 birk      (1000) birk      (1000)      973 2023-03-06 00:57:41.000000 jax-dataloader-0.0.2/settings.ini
--rw-r--r--   0 birk      (1000) birk      (1000)       38 2023-03-06 01:04:58.000000 jax-dataloader-0.0.2/setup.cfg
--rw-rw-r--   0 birk      (1000) birk      (1000)     2541 2022-09-05 16:31:43.000000 jax-dataloader-0.0.2/setup.py
+drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/
+-rw-rw-r--   0 birk      (1000) birk      (1000)    11337 2022-09-05 16:31:43.000000 jax-dataloader-0.0.3/LICENSE
+-rw-rw-r--   0 birk      (1000) birk      (1000)      111 2022-09-05 16:31:43.000000 jax-dataloader-0.0.3/MANIFEST.in
+-rw-r--r--   0 birk      (1000) birk      (1000)     6169 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/PKG-INFO
+-rw-r--r--   0 birk      (1000) birk      (1000)     5372 2023-04-05 20:47:16.000000 jax-dataloader-0.0.3/README.md
+drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/jax_dataloader/
+-rw-r--r--   0 birk      (1000) birk      (1000)      112 2023-04-07 00:15:43.000000 jax-dataloader-0.0.3/jax_dataloader/__init__.py
+-rw-r--r--   0 birk      (1000) birk      (1000)    15604 2023-04-07 00:15:43.000000 jax-dataloader-0.0.3/jax_dataloader/_modidx.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     5077 2023-04-07 00:15:43.000000 jax-dataloader-0.0.3/jax_dataloader/core.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     2910 2023-04-07 00:15:43.000000 jax-dataloader-0.0.3/jax_dataloader/datasets.py
+-rw-r--r--   0 birk      (1000) birk      (1000)      758 2023-04-06 01:20:29.000000 jax-dataloader-0.0.3/jax_dataloader/imports.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     6464 2023-04-07 00:15:43.000000 jax-dataloader-0.0.3/jax_dataloader/loaders.py
+-rw-r--r--   0 birk      (1000) birk      (1000)     3317 2023-04-07 00:15:43.000000 jax-dataloader-0.0.3/jax_dataloader/utils.py
+drwxr-xr-x   0 birk      (1000) birk      (1000)        0 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/jax_dataloader.egg-info/
+-rw-r--r--   0 birk      (1000) birk      (1000)     6169 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/jax_dataloader.egg-info/PKG-INFO
+-rw-r--r--   0 birk      (1000) birk      (1000)      497 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/jax_dataloader.egg-info/SOURCES.txt
+-rw-r--r--   0 birk      (1000) birk      (1000)        1 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/jax_dataloader.egg-info/dependency_links.txt
+-rw-r--r--   0 birk      (1000) birk      (1000)       50 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/jax_dataloader.egg-info/entry_points.txt
+-rw-r--r--   0 birk      (1000) birk      (1000)        1 2023-01-12 03:15:10.000000 jax-dataloader-0.0.3/jax_dataloader.egg-info/not-zip-safe
+-rw-r--r--   0 birk      (1000) birk      (1000)      284 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/jax_dataloader.egg-info/requires.txt
+-rw-r--r--   0 birk      (1000) birk      (1000)       15 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/jax_dataloader.egg-info/top_level.txt
+-rw-r--r--   0 birk      (1000) birk      (1000)     1101 2023-04-07 00:15:43.000000 jax-dataloader-0.0.3/settings.ini
+-rw-r--r--   0 birk      (1000) birk      (1000)       38 2023-04-07 00:16:47.000000 jax-dataloader-0.0.3/setup.cfg
+-rw-r--r--   0 birk      (1000) birk      (1000)     3133 2023-04-07 00:15:31.000000 jax-dataloader-0.0.3/setup.py
```

### Comparing `jax-dataloader-0.0.2/LICENSE` & `jax-dataloader-0.0.3/LICENSE`

 * *Files identical despite different names*

### Comparing `jax-dataloader-0.0.2/PKG-INFO` & `jax-dataloader-0.0.3/README.md`

 * *Files 16% similar despite different names*

```diff
@@ -1,156 +1,174 @@
-Metadata-Version: 2.1
-Name: jax-dataloader
-Version: 0.0.2
-Summary: Dataloader for jax
-Home-page: https://github.com/birkhoffg/jax-dataloader
-Author: BirkhoffG
-Author-email: 26811230+BirkhoffG@users.noreply.github.com
-License: Apache Software License 2.0
-Keywords: python jax dataloader pytorch datasets huggingface
-Classifier: Development Status :: 4 - Beta
-Classifier: Intended Audience :: Developers
-Classifier: Natural Language :: English
-Classifier: Programming Language :: Python :: 3.7
-Classifier: Programming Language :: Python :: 3.8
-Classifier: Programming Language :: Python :: 3.9
-Classifier: Programming Language :: Python :: 3.10
-Classifier: License :: OSI Approved :: Apache Software License
-Requires-Python: >=3.7
-Description-Content-Type: text/markdown
-Provides-Extra: dev
-License-File: LICENSE
-
-Jax-Dataloader
-================
-
-<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->
-
-![Python](https://img.shields.io/pypi/pyversions/jax-dataloader.svg)
-![CI
-status](https://github.com/BirkhoffG/jax-dataloader/actions/workflows/test.yaml/badge.svg)
-![Docs](https://github.com/BirkhoffG/jax-dataloader/actions/workflows/deploy.yaml/badge.svg)
-![pypi](https://img.shields.io/pypi/v/jax-dataloader.svg) ![GitHub
-License](https://img.shields.io/github/license/BirkhoffG/jax-dataloader.svg)
-
-## Overview
-
-`jax_dataloader` provides a high-level *pytorch-like* dataloader API for
-`jax`. It supports
-
-- **downloading and pre-processing datasets** via [huggingface
-  datasets](https://github.com/huggingface/datasets), [pytorch
-  Dataset](https://pytorch.org/docs/stable/data.html#torch.utils.data.Dataset),
-  and tensorflow dataset (forthcoming)
-
-- **iteratively loading batches** via (vanillla) [jax
-  dataloader](https://birkhoffg.github.io/jax-dataloader/core.html#jax-dataloader),
-  [pytorch
-  dataloader](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader),
-  tensorflow (forthcoming), and merlin (forthcoming).
-
-A minimum `jax_dataloader` example:
-
-``` python
-import jax_dataloader as jdl
-
-dataloader = jdl.DataLoader(
-    dataset, # Can be a jdl.Dataset or pytorch or huggingface dataset
-    backend='jax', # Use 'jax' for loading data (also supports `pytorch`)
-)
-
-batch = next(iter(dataloader)) # iterate next batch
-```
-
-## Installation
-
-The latest `jax_dataloader` release can directly be installed from PyPI:
-
-``` sh
-pip install jax_dataloader
-```
-
-or install directly from the repository:
-
-``` sh
-pip install git+https://github.com/BirkhoffG/jax-dataloader.git
-```
-
-<div>
-
-> **Note**
->
-> We will only install `jax`-related dependencies. If you wish to use
-> integration of `pytorch` or huggingface `datasets`, you should try to
-> manually install them, or run `pip install jax_dataloader[dev]` for
-> installing all the dependencies.
-
-</div>
-
-## Usage
-
-[`jax_dataloader.core.DataLoader`](https://birkhoffg.github.io/jax-dataloader/core.html#dataloader)
-follows similar API as the pytorch dataloader.
-
-- The `dataset` argument takes
-  [`jax_dataloader.core.Dataset`](https://birkhoffg.github.io/jax-dataloader/core.html#dataset)
-  or `torch.utils.data.Dataset` or (the huggingface) `datasets.Dataset`
-  as an input from which to load the data.
-- The `backend` argument takes `"jax"` or`"pytorch"` as an input, which
-  specifies which backend dataloader to use batches.
-
-``` python
-import jax_dataloader as jdl
-import jax.numpy as jnp
-```
-
-### Using [`ArrayDataset`](https://birkhoffg.github.io/jax-dataloader/core.html#arraydataset)
-
-The
-[`jax_dataloader.core.ArrayDataset`](https://birkhoffg.github.io/jax-dataloader/core.html#arraydataset)
-is an easy way to wrap multiple `jax.numpy.array` into one Dataset. For
-example, we can create an
-[`ArrayDataset`](https://birkhoffg.github.io/jax-dataloader/core.html#arraydataset)
-as follows:
-
-``` python
-# Create features `X` and labels `y`
-X = jnp.arange(100).reshape(10, 10)
-y = jnp.arange(10)
-# Create an `ArrayDataset`
-arr_ds = jdl.ArrayDataset(X, y)
-```
-
-This `arr_ds` can be loaded by both `"jax"` and `"pytorch"` dataloaders.
-
-``` python
-# Create a `DataLoader` from the `ArrayDataset` via jax backend
-dataloader = jdl.DataLoader(arr_ds, 'jax', batch_size=5, shuffle=True)
-# Or we can use the pytorch backend
-dataloader = jdl.DataLoader(arr_ds, 'pytorch', batch_size=5, shuffle=True)
-```
-
-### Using Huggingface Datasets
-
-The huggingface [datasets](https://github.com/huggingface/datasets) is a
-morden library for downloading, pre-processing, and sharing datasets.
-`jax_dataloader` supports directly passing the huggingface datasets.
-
-``` python
-from datasets import load_dataset
-```
-
-For example, We load the `"squad"` dataset from `datasets`:
-
-``` python
-hf_ds = load_dataset("squad")
-```
-
-This `hf_ds` can be loaded via `"jax"` and `"pytorch"` dataloaders.
-
-``` python
-# Create a `DataLoader` from the `datasets.Dataset` via jax backend
-# TODO: This is currently not working
-dataloader = jdl.DataLoader(hf_ds['train'], 'jax', batch_size=5, shuffle=True)
-# Or we can use the pytorch backend
-dataloader = jdl.DataLoader(hf_ds['train'], 'pytorch', batch_size=5, shuffle=True)
-```
+Jax-Dataloader
+================
+
+<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->
+
+![Python](https://img.shields.io/pypi/pyversions/jax-dataloader.svg)
+![CI
+status](https://github.com/BirkhoffG/jax-dataloader/actions/workflows/test.yaml/badge.svg)
+![Docs](https://github.com/BirkhoffG/jax-dataloader/actions/workflows/deploy.yaml/badge.svg)
+![pypi](https://img.shields.io/pypi/v/jax-dataloader.svg) ![GitHub
+License](https://img.shields.io/github/license/BirkhoffG/jax-dataloader.svg)
+
+## Overview
+
+`jax_dataloader` provides a high-level *pytorch-like* dataloader API for
+`jax`. It supports
+
+- **downloading and pre-processing datasets** via [huggingface
+  datasets](https://github.com/huggingface/datasets), [pytorch
+  Dataset](https://pytorch.org/docs/stable/data.html#torch.utils.data.Dataset),
+  and tensorflow dataset (forthcoming)
+
+- **iteratively loading batches** via (vanillla) [jax
+  dataloader](https://birkhoffg.github.io/jax-dataloader/core.html#jax-dataloader),
+  [pytorch
+  dataloader](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader),
+  tensorflow (forthcoming), and merlin (forthcoming).
+
+A minimum `jax_dataloader` example:
+
+``` python
+import jax_dataloader as jdl
+
+dataloader = jdl.DataLoader(
+    dataset, # Can be a jdl.Dataset or pytorch or huggingface dataset
+    backend='jax', # Use 'jax' for loading data (also supports `pytorch`)
+)
+
+batch = next(iter(dataloader)) # iterate next batch
+```
+
+## Installation
+
+The latest `jax_dataloader` release can directly be installed from PyPI:
+
+``` sh
+pip install jax_dataloader
+```
+
+or install directly from the repository:
+
+``` sh
+pip install git+https://github.com/BirkhoffG/jax-dataloader.git
+```
+
+<div>
+
+> **Note**
+>
+> We will only install `jax`-related dependencies. If you wish to use
+> integration of `pytorch` or huggingface `datasets`, you should try to
+> manually install them, or run `pip install jax_dataloader[dev]` for
+> installing all the dependencies.
+
+</div>
+
+## Usage
+
+[`jax_dataloader.core.DataLoader`](https://birkhoffg.github.io/jax-dataloader/core.html#dataloader)
+follows similar API as the pytorch dataloader.
+
+- The `dataset` argument takes `jax_dataloader.core.Dataset` or
+  `torch.utils.data.Dataset` or (the huggingface) `datasets.Dataset` as
+  an input from which to load the data.
+- The `backend` argument takes `"jax"` or`"pytorch"` as an input, which
+  specifies which backend dataloader to use batches.
+
+``` python
+import jax_dataloader as jdl
+import jax.numpy as jnp
+```
+
+### Using [`ArrayDataset`](https://birkhoffg.github.io/jax-dataloader/dataset.html#arraydataset)
+
+The `jax_dataloader.core.ArrayDataset` is an easy way to wrap multiple
+`jax.numpy.array` into one Dataset. For example, we can create an
+[`ArrayDataset`](https://birkhoffg.github.io/jax-dataloader/dataset.html#arraydataset)
+as follows:
+
+``` python
+# Create features `X` and labels `y`
+X = jnp.arange(100).reshape(10, 10)
+y = jnp.arange(10)
+# Create an `ArrayDataset`
+arr_ds = jdl.ArrayDataset(X, y)
+```
+
+This `arr_ds` can be loaded by both `"jax"` and `"pytorch"` dataloaders.
+
+``` python
+# Create a `DataLoader` from the `ArrayDataset` via jax backend
+dataloader = jdl.DataLoader(arr_ds, 'jax', batch_size=5, shuffle=True)
+# Or we can use the pytorch backend
+dataloader = jdl.DataLoader(arr_ds, 'pytorch', batch_size=5, shuffle=True)
+```
+
+### Using Pytorch Datasets
+
+The [pytorch Dataset](https://pytorch.org/docs/stable/data.html) and its
+ecosystems (e.g.,
+[torchvision](https://pytorch.org/vision/stable/index.html),
+[torchtext](https://pytorch.org/text/stable/index.html),
+[torchaudio](https://pytorch.org/audio/stable/index.html)) supports many
+built-in datasets. `jax_dataloader` supports directly passing the
+pytorch Dataset.
+
+<div>
+
+> **Note**
+>
+> Unfortuantely, the [pytorch
+> Dataset](https://pytorch.org/docs/stable/data.html) can only work with
+> `backend=pytorch`. See the belowing example.
+
+</div>
+
+``` python
+from torchvision.datasets import MNIST
+import numpy as np
+```
+
+We load the MNIST dataset from `torchvision`. The `ToNumpy` object
+transforms images to `numpy.array`.
+
+``` python
+class ToNumpy(object):
+  def __call__(self, pic):
+    return np.array(pic, dtype=float)
+```
+
+``` python
+pt_ds = MNIST('/tmp/mnist/', download=True, transform=ToNumpy(), train=False)
+```
+
+This `pt_ds` can **only** be loaded via `"pytorch"` dataloaders.
+
+``` python
+dataloader = jdl.DataLoader(pt_ds, 'pytorch', batch_size=5, shuffle=True)
+```
+
+### Using Huggingface Datasets
+
+The huggingface [datasets](https://github.com/huggingface/datasets) is a
+morden library for downloading, pre-processing, and sharing datasets.
+`jax_dataloader` supports directly passing the huggingface datasets.
+
+``` python
+from datasets import load_dataset
+```
+
+For example, We load the `"squad"` dataset from `datasets`:
+
+``` python
+hf_ds = load_dataset("squad")
+```
+
+This `hf_ds` can be loaded via `"jax"` and `"pytorch"` dataloaders.
+
+``` python
+# Create a `DataLoader` from the `datasets.Dataset` via jax backend
+dataloader = jdl.DataLoader(hf_ds['train'], 'jax', batch_size=5, shuffle=True)
+# Or we can use the pytorch backend
+dataloader = jdl.DataLoader(hf_ds['train'], 'pytorch', batch_size=5, shuffle=True)
+```
```

### Comparing `jax-dataloader-0.0.2/settings.ini` & `jax-dataloader-0.0.3/settings.ini`

 * *Files 22% similar despite different names*

```diff
@@ -1,36 +1,39 @@
 [DEFAULT]
 repo = jax-dataloader
 lib_name = jax-dataloader
-version = 0.0.2
+version = 0.0.3
 min_python = 3.7
 license = apache2
 doc_path = _docs
 lib_path = jax_dataloader
 nbs_path = nbs
 recursive = True
-tst_flags = notest
+tst_flags = notest torch tf hf
 put_version_in_init = True
 branch = master
 custom_sidebar = False
 doc_host = https://birkhoffg.github.io
 doc_baseurl = /jax-dataloader
 git_url = https://github.com/birkhoffg/jax-dataloader
 title = Jax-Dataloader
 audience = Developers
 author = BirkhoffG
 author_email = 26811230+BirkhoffG@users.noreply.github.com
 copyright = 2023 onwards, BirkhoffG
 description = Dataloader for jax
-keywords = python jax dataloader pytorch datasets huggingface
+keywords = python jax dataloader pytorch tensorflow datasets huggingface
 language = English
 status = 3
 user = birkhoffg
 requirements = jax[cpu]
-dev_requirements = scikit-learn pandas nbdev jupyter dm-haiku optax torch torchvision datasets
+dev_requirements = scikit-learn pandas nbdev jupyter dm-haiku optax
+torch_requirements = torch torchvision
+tensorflow_requirements = tensorflow tensorflow-datasets
+huggingface_requirements = datasets
 black_formatting = False
 readme_nb = index.ipynb
 allowed_metadata_keys = 
 allowed_cell_metadata_keys = 
 jupyter_hooks = True
 clean_ids = True
 clear_all = False
```

