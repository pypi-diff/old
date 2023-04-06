# Comparing `tmp/gradient-accumulator-0.3.1.tar.gz` & `tmp/gradient-accumulator-0.3.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/gradient-accumulator-0.3.1.tar", last modified: Sun Jan 29 22:29:18 2023, max compression
+gzip compressed data, was "dist/gradient-accumulator-0.3.2.tar", last modified: Thu Apr  6 21:50:02 2023, max compression
```

## Comparing `gradient-accumulator-0.3.1.tar` & `gradient-accumulator-0.3.2.tar`

### file list

```diff
@@ -1,29 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/
--rw-r--r--   0 runner    (1001) docker     (116)    11008 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)     8590 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/README.md
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/gradient_accumulator/
--rw-r--r--   0 runner    (1001) docker     (116)      104 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/gradient_accumulator/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)    11154 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/gradient_accumulator/accumulators.py
--rw-r--r--   0 runner    (1001) docker     (116)     1882 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/gradient_accumulator/agc.py
--rw-r--r--   0 runner    (1001) docker     (116)      752 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/gradient_accumulator/layers.py
--rw-r--r--   0 runner    (1001) docker     (116)     3192 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/gradient_accumulator/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/gradient_accumulator.egg-info/
--rw-r--r--   0 runner    (1001) docker     (116)    11008 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/gradient_accumulator.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (116)      735 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/gradient_accumulator.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (116)        1 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/gradient_accumulator.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (116)       29 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/gradient_accumulator.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (116)       27 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/gradient_accumulator.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (116)       79 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (116)     1171 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (116)        0 2023-01-29 22:29:18.000000 gradient-accumulator-0.3.1/tests/
--rw-r--r--   0 runner    (1001) docker     (116)        0 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (116)     2713 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_adaptive_gradient_clipping.py
--rw-r--r--   0 runner    (1001) docker     (116)     3323 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_expected_result.py
--rw-r--r--   0 runner    (1001) docker     (116)     2699 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_mixed_precision.py
--rw-r--r--   0 runner    (1001) docker     (116)     3041 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_multi_gpu.py
--rw-r--r--   0 runner    (1001) docker     (116)     4493 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_multi_gpu_benchmark.py
--rw-r--r--   0 runner    (1001) docker     (116)     4332 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_multitask.py
--rw-r--r--   0 runner    (1001) docker     (116)     2536 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_optimizer_distribute.py
--rw-r--r--   0 runner    (1001) docker     (116)     3959 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_optimizer_invariance.py
--rw-r--r--   0 runner    (1001) docker     (116)     4021 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_optimizer_wrapper.py
--rw-r--r--   0 runner    (1001) docker     (116)     1911 2023-01-29 22:28:35.000000 gradient-accumulator-0.3.1/tests/test_train_mnist.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/
+-rw-r--r--   0 runner    (1001) docker     (122)    15309 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)    12093 2023-04-06 21:49:17.000000 gradient-accumulator-0.3.2/README.md
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/gradient_accumulator/
+-rw-r--r--   0 runner    (1001) docker     (122)      104 2023-04-06 21:49:17.000000 gradient-accumulator-0.3.2/gradient_accumulator/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    10916 2023-04-06 21:49:17.000000 gradient-accumulator-0.3.2/gradient_accumulator/accumulators.py
+-rw-r--r--   0 runner    (1001) docker     (122)     1882 2023-04-06 21:49:17.000000 gradient-accumulator-0.3.2/gradient_accumulator/agc.py
+-rw-r--r--   0 runner    (1001) docker     (122)     2949 2023-04-06 21:49:17.000000 gradient-accumulator-0.3.2/gradient_accumulator/layers.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/gradient_accumulator.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)    15309 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/gradient_accumulator.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      376 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/gradient_accumulator.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/gradient_accumulator.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       11 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/gradient_accumulator.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       21 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/gradient_accumulator.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       79 2023-04-06 21:50:02.000000 gradient-accumulator-0.3.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1255 2023-04-06 21:49:17.000000 gradient-accumulator-0.3.2/setup.py
```

### Comparing `gradient-accumulator-0.3.1/PKG-INFO` & `gradient-accumulator-0.3.2/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,30 +1,32 @@
 Metadata-Version: 2.1
 Name: gradient-accumulator
-Version: 0.3.1
+Version: 0.3.2
 Summary: Package for gradient accumulation in TensorFlow
 Home-page: https://github.com/andreped/GradientAccumulator
 Author: André Pedersen and David Bouget
 Author-email: andrped94@gmail.com
 License: UNKNOWN
 Description: <div align="center">
         <h1 align="center">GradientAccumulator</h1>
         <h3 align="center">Seemless gradient accumulation for TensorFlow 2</h3>
         
         [![Pip Downloads](https://img.shields.io/pypi/dm/gradient-accumulator?label=pip%20downloads&logo=python)](https://pypi.org/project/gradient-accumulator/)
         [![PyPI version](https://badge.fury.io/py/gradient-accumulator.svg)](https://badge.fury.io/py/gradient-accumulator)
         [![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
-        [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7581815.svg)](https://doi.org/10.5281/zenodo.7581815)
+        [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7582309.svg)](https://doi.org/10.5281/zenodo.7582309)
         [![CI](https://github.com/andreped/GradientAccumulator/workflows/CI/badge.svg)](https://github.com/andreped/GradientAccumulator/actions)
+        [![codecov](https://codecov.io/gh/andreped/GradientAccumulator/branch/main/graph/badge.svg?token=MWLK71V750)](https://codecov.io/gh/andreped/GradientAccumulator)
         
         **GradientAccumulator** was developed by SINTEF Health due to the lack of an easy-to-use method for gradient accumulation in TensorFlow 2.
         
-        The package is available on PyPI and is compatible with and have been tested against TF >= 2.3 and Python >= 3.6 (tested with 3.6-3.10), and works cross-platform (Ubuntu, Windows, macOS).
+        The package is available on PyPI and is compatible with and have been tested against `TF 2.2-2.12` and `Python 3.6-3.12`, and works cross-platform (Ubuntu, Windows, macOS).
         </div>
         
+        
         ## What?
         Gradient accumulation (GA) enables reduced GPU memory consumption through dividing a batch into smaller reduced batches, and performing gradient computation either in a distributing setting across multiple GPUs or sequentially on the same GPU. When the full batch is processed, the gradients are the _accumulated_ to produce the full batch gradient.
         
         <p align="center">
         <img src="assets/grad_accum.png" width="50%">
         </p>
         
@@ -33,15 +35,15 @@
         In TensorFlow 2, there did not exist a plug-and-play method to use gradient accumulation with any custom pipeline. Hence, we have implemented two generic TF2-compatible approaches:
         
         | Method | Usage |
         | - | - |
         | `GradientAccumulateModel` | `model = GradientAccumulateModel(accum_steps=4, inputs=model.input, outputs=model.output)` |
         | `GradientAccumulateOptimizer` | `opt = GradientAccumulateOptimizer(accum_steps=4, optimizer=tf.keras.optimizers.SGD(1e-2))` |
         
-        Both approaches control how frequently the weigths are updated, but in their own way. Approach (1) is for single-GPU only, whereas (2) supports both single-GPU and distributed training (multi-GPU).
+        Both approaches control how frequently the weigths are updated, but in their own way. Approach (1) is for single-GPU only, whereas (2) supports both single-GPU and distributed training (multi-GPU). However, note that (2) is not yet working as intended. Hence, use (1) for most applications.
         
         Our implementations enable theoretically **infinitely large batch size**, with **identical memory consumption** as for a regular mini batch. If a single GPU is used, this comes at the cost of increased training runtime. Multiple GPUs could be used to increase runtime performance.
         
         As batch normalization is not natively compatible with GA, support for adaptive gradient clipping has been added as an alternative. We have also added support for mixed precision and both GPU and TPU support.
         
         
         ## Install
@@ -63,15 +65,15 @@
         
         model = Model(...)
         model = GradientAccumulateModel(accum_steps=4, inputs=model.input, outputs=model.output)
         ```
         
         Then simply use the `model` as you normally would!
         
-        <details open>
+        <details>
         <summary>
         
         #### Mixed precision</summary>
         
         There has also been added experimental support for mixed precision:
         ```
         from tensorflow.keras import mixed_precision
@@ -89,27 +91,64 @@
         mixed_precision.set_global_policy('mixed_bfloat16')
         ```
         
         There is also an example of how to use gradient accumulation with mixed precision [here](https://github.com/andreped/GradientAccumulator/blob/main/tests/test_mixed_precision.py#L58).
         </details>
         
         
-        <details open>
+        <details>
         <summary>
         
         #### Distributed training with multiple GPUs</summary>
         In order to use multiple GPUs, you will have to use the Optimizer wrapper:
         ```
         opt = GradientAccumulateOptimizer(accum_steps=4, optimizer=tf.keras.optimizers.SGD(1e-2))
         ```
         
         Just remember to wrap the optimizer within the `tf.distribute.MirroredStrategy`. For an example, see [here](https://github.com/andreped/GradientAccumulator/blob/main/tests/test_optimizer_distribute.py).
         
+        **DISCLAIMER: The GradientAccumulateOptimizer is a VERY experimental feature. It is not reaching the same results as GradientAccumulateModel with a single GPU, and does not work (yet) with multiple GPUs. Hence, I would recommend using GradientAccumulateModel with a single GPU in its current state.**
+        
+        </details>
+        
+        
+        <details>
+        <summary>
+        
+        #### HuggingFace :hugs:</summary>
+        Note that HuggingFace provides a variety of different pretrained models. However, it was observed that when loading these models into TensorFlow, the computational graph may not be set up correctly, such that the `model.input` and `model.output` exist.
+        
+        To fix this, we basically wrap the model into a new `tf.keras.Model`, but define the inputs and outputs ourselves:
+        ```
+        from gradient_accumulator import GradientAccumulateModel
+        from tensorflow.keras.layers import Input
+        from tensorflow.keras.models import Model
+        from transformers import TFx
+        
+        #load your model checkpoint
+        HF_model = TFx.from_pretrained(checkpoint)
+        
+        # define model inputs and outputs -> for different models, different inputs/outputs need to be defined
+        input_ids = tf.keras.Input(shape=(None,), dtype='int32', name="input_ids")
+        attention_mask = tf.keras.Input(shape=(None,), dtype='int32', name="attention_mask")
+        model_input={'input_ids': input_ids, 'attention_mask': attention_mask}
+        
+        #create a new Model which has model.input and model.output properties
+        new_model = Model(inputs=model_input, outputs=HF_model(model_input))
+        
+        #create the GA model
+        model = GradientAccumulateModel(accum_steps=4, inputs=new_model.input, outputs=new_model.output)
+        ```
+          
+        For more details, see [this](https://github.com/andreped/GradientAccumulator/blob/main/notebooks/GA_for_HuggingFace_TF_models.ipynb) jupyter notebook.
+        
         </details>
         
+        
+        
         <details>
         <summary>
         
         #### Adaptive gradient clipping</summary>
         
         There has also been added support for adaptive gradient clipping, based on [this](https://github.com/sayakpaul/Adaptive-Gradient-Clipping) implementation:
         ```
@@ -121,15 +160,15 @@
         
         
         <details>
         <summary>
         
         #### Model format</summary>
         
-        It is recommended to use the SavedModel format when using this implementation. That is because the HDF5 format is only compatible with `TF <= 2.6` when using the model wrapper. However, if you are using older TF versions, both formats work out-of-the-box. The SavedModel format works fine for all versions of TF 2.x
+        It is recommended to use the SavedModel format when using this implementation. That is because the HDF5 format is only compatible with `TF <= 2.6` when using the model wrapper. However, if you are using older TF versions, both formats work out-of-the-box. The SavedModel format works fine for all versions of TF 2.x.
         </details>
         
         
         <details>
         <summary>
         
         #### macOS compatibility</summary>
@@ -149,16 +188,64 @@
         For TF 1, I suggest using the AccumOptimizer implementation in the [H2G-Net repository](https://github.com/andreped/H2G-Net/blob/main/src/utils/accum_optimizers.py#L139) instead, which wraps the optimizer instead of overloading the train_step of the Model itself (new feature in TF2).
         </details>
         
         
         <details>
         <summary>
         
+        #### TF >= 2.11 legacy option</summary>
+        Note that for TensorFlow >= 2.11, there has been some major changes to the Optimizer class. Our current implementation is not compatible with the new one. Based on which TensorFlow version you have, our `GradientAccumulateOptimizer` dynamically chooses which Optimizer to use.
+        
+        However, you will need to choose a legacy optimizer to use with the Optimizer wrapper, like so:
+        ```
+        import tensorflow as tf
+        from gradient_accumulator import GradientAccumulateOptimizer
+        
+        opt = tf.keras.optimizers.legacy.SGD(learning_rate=1e-2)
+        opt = GradientAccumulateOptimizer(optimizer=opt, accum_steps=4)
+        ```
+        </details>
+        
+        
+        <details>
+        <summary>
+        
         #### PyTorch</summary>
         For PyTorch, I would recommend using [accelerate](https://pypi.org/project/accelerate/). HuggingFace :hugs: has a great tutorial on how to use it [here](https://huggingface.co/docs/accelerate/usage_guides/gradient_accumulation).
+        
+        However, if you wish to use native PyTorch and you are implementing your own training loop, you could do something like this:
+        ```
+        # batch accumulation parameter
+        accum_iter = 4
+        
+        # loop through enumaretad batches
+        for batch_idx, (inputs, labels) in enumerate(data_loader):
+        
+            # extract inputs and labels
+            inputs = inputs.to(device)
+            labels = labels.to(device)
+        
+            # passes and weights update
+            with torch.set_grad_enabled(True):
+                
+                # forward pass 
+                preds = model(inputs)
+                loss  = criterion(preds, labels)
+        
+                # scale loss prior to accumulation
+                loss = loss / accum_iter
+        
+                # backward pass
+                loss.backward()
+        
+                # weights update and reset gradients
+                if ((batch_idx + 1) % accum_iter == 0) or (batch_idx + 1 == len(data_loader)):
+                    optimizer.step()
+                    optimizer.zero_grad()
+        ```
         </details>
         
         
         <details>
         <summary>
         
         #### Troubleshooting</summary>
@@ -184,32 +271,34 @@
         The optimizer wrapper is derived from [the implementation by @fsx950223 and @stefan-falk](https://github.com/tensorflow/addons/pull/2525).
         
           
         ## How to cite?
         If you used this package or found the project relevant in your research, please, considering including the following citation:
         
         ```
-        @software{andre_pedersen_2023_7581815,
+        @software{andre_pedersen_2023_7582309,
           author       = {André Pedersen and David Bouget},
-          title        = {andreped/GradientAccumulator: v0.3.0},
+          title        = {andreped/GradientAccumulator: v0.3.1},
           month        = jan,
           year         = 2023,
           publisher    = {Zenodo},
-          version      = {v0.3.0},
-          doi          = {10.5281/zenodo.7581815},
-          url          = {https://doi.org/10.5281/zenodo.7581815}
+          version      = {v0.3.1},
+          doi          = {10.5281/zenodo.7582309},
+          url          = {https://doi.org/10.5281/zenodo.7582309}
         }
         ```
         
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3.12
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
```

### Comparing `gradient-accumulator-0.3.1/README.md` & `gradient-accumulator-0.3.2/README.md`

 * *Files 24% similar despite different names*

```diff
@@ -1,22 +1,24 @@
 <div align="center">
 <h1 align="center">GradientAccumulator</h1>
 <h3 align="center">Seemless gradient accumulation for TensorFlow 2</h3>
 
 [![Pip Downloads](https://img.shields.io/pypi/dm/gradient-accumulator?label=pip%20downloads&logo=python)](https://pypi.org/project/gradient-accumulator/)
 [![PyPI version](https://badge.fury.io/py/gradient-accumulator.svg)](https://badge.fury.io/py/gradient-accumulator)
 [![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
-[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7581815.svg)](https://doi.org/10.5281/zenodo.7581815)
+[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7582309.svg)](https://doi.org/10.5281/zenodo.7582309)
 [![CI](https://github.com/andreped/GradientAccumulator/workflows/CI/badge.svg)](https://github.com/andreped/GradientAccumulator/actions)
+[![codecov](https://codecov.io/gh/andreped/GradientAccumulator/branch/main/graph/badge.svg?token=MWLK71V750)](https://codecov.io/gh/andreped/GradientAccumulator)
 
 **GradientAccumulator** was developed by SINTEF Health due to the lack of an easy-to-use method for gradient accumulation in TensorFlow 2.
 
-The package is available on PyPI and is compatible with and have been tested against TF >= 2.3 and Python >= 3.6 (tested with 3.6-3.10), and works cross-platform (Ubuntu, Windows, macOS).
+The package is available on PyPI and is compatible with and have been tested against `TF 2.2-2.12` and `Python 3.6-3.12`, and works cross-platform (Ubuntu, Windows, macOS).
 </div>
 
+
 ## What?
 Gradient accumulation (GA) enables reduced GPU memory consumption through dividing a batch into smaller reduced batches, and performing gradient computation either in a distributing setting across multiple GPUs or sequentially on the same GPU. When the full batch is processed, the gradients are the _accumulated_ to produce the full batch gradient.
 
 <p align="center">
 <img src="assets/grad_accum.png" width="50%">
 </p>
 
@@ -25,15 +27,15 @@
 In TensorFlow 2, there did not exist a plug-and-play method to use gradient accumulation with any custom pipeline. Hence, we have implemented two generic TF2-compatible approaches:
 
 | Method | Usage |
 | - | - |
 | `GradientAccumulateModel` | `model = GradientAccumulateModel(accum_steps=4, inputs=model.input, outputs=model.output)` |
 | `GradientAccumulateOptimizer` | `opt = GradientAccumulateOptimizer(accum_steps=4, optimizer=tf.keras.optimizers.SGD(1e-2))` |
 
-Both approaches control how frequently the weigths are updated, but in their own way. Approach (1) is for single-GPU only, whereas (2) supports both single-GPU and distributed training (multi-GPU).
+Both approaches control how frequently the weigths are updated, but in their own way. Approach (1) is for single-GPU only, whereas (2) supports both single-GPU and distributed training (multi-GPU). However, note that (2) is not yet working as intended. Hence, use (1) for most applications.
 
 Our implementations enable theoretically **infinitely large batch size**, with **identical memory consumption** as for a regular mini batch. If a single GPU is used, this comes at the cost of increased training runtime. Multiple GPUs could be used to increase runtime performance.
 
 As batch normalization is not natively compatible with GA, support for adaptive gradient clipping has been added as an alternative. We have also added support for mixed precision and both GPU and TPU support.
 
 
 ## Install
@@ -55,15 +57,15 @@
 
 model = Model(...)
 model = GradientAccumulateModel(accum_steps=4, inputs=model.input, outputs=model.output)
 ```
 
 Then simply use the `model` as you normally would!
 
-<details open>
+<details>
 <summary>
 
 #### Mixed precision</summary>
 
 There has also been added experimental support for mixed precision:
 ```
 from tensorflow.keras import mixed_precision
@@ -81,27 +83,64 @@
 mixed_precision.set_global_policy('mixed_bfloat16')
 ```
 
 There is also an example of how to use gradient accumulation with mixed precision [here](https://github.com/andreped/GradientAccumulator/blob/main/tests/test_mixed_precision.py#L58).
 </details>
 
 
-<details open>
+<details>
 <summary>
 
 #### Distributed training with multiple GPUs</summary>
 In order to use multiple GPUs, you will have to use the Optimizer wrapper:
 ```
 opt = GradientAccumulateOptimizer(accum_steps=4, optimizer=tf.keras.optimizers.SGD(1e-2))
 ```
 
 Just remember to wrap the optimizer within the `tf.distribute.MirroredStrategy`. For an example, see [here](https://github.com/andreped/GradientAccumulator/blob/main/tests/test_optimizer_distribute.py).
 
+**DISCLAIMER: The GradientAccumulateOptimizer is a VERY experimental feature. It is not reaching the same results as GradientAccumulateModel with a single GPU, and does not work (yet) with multiple GPUs. Hence, I would recommend using GradientAccumulateModel with a single GPU in its current state.**
+
+</details>
+
+
+<details>
+<summary>
+
+#### HuggingFace :hugs:</summary>
+Note that HuggingFace provides a variety of different pretrained models. However, it was observed that when loading these models into TensorFlow, the computational graph may not be set up correctly, such that the `model.input` and `model.output` exist.
+
+To fix this, we basically wrap the model into a new `tf.keras.Model`, but define the inputs and outputs ourselves:
+```
+from gradient_accumulator import GradientAccumulateModel
+from tensorflow.keras.layers import Input
+from tensorflow.keras.models import Model
+from transformers import TFx
+
+#load your model checkpoint
+HF_model = TFx.from_pretrained(checkpoint)
+
+# define model inputs and outputs -> for different models, different inputs/outputs need to be defined
+input_ids = tf.keras.Input(shape=(None,), dtype='int32', name="input_ids")
+attention_mask = tf.keras.Input(shape=(None,), dtype='int32', name="attention_mask")
+model_input={'input_ids': input_ids, 'attention_mask': attention_mask}
+
+#create a new Model which has model.input and model.output properties
+new_model = Model(inputs=model_input, outputs=HF_model(model_input))
+
+#create the GA model
+model = GradientAccumulateModel(accum_steps=4, inputs=new_model.input, outputs=new_model.output)
+```
+  
+For more details, see [this](https://github.com/andreped/GradientAccumulator/blob/main/notebooks/GA_for_HuggingFace_TF_models.ipynb) jupyter notebook.
+
 </details>
 
+
+
 <details>
 <summary>
 
 #### Adaptive gradient clipping</summary>
 
 There has also been added support for adaptive gradient clipping, based on [this](https://github.com/sayakpaul/Adaptive-Gradient-Clipping) implementation:
 ```
@@ -113,15 +152,15 @@
 
 
 <details>
 <summary>
 
 #### Model format</summary>
 
-It is recommended to use the SavedModel format when using this implementation. That is because the HDF5 format is only compatible with `TF <= 2.6` when using the model wrapper. However, if you are using older TF versions, both formats work out-of-the-box. The SavedModel format works fine for all versions of TF 2.x
+It is recommended to use the SavedModel format when using this implementation. That is because the HDF5 format is only compatible with `TF <= 2.6` when using the model wrapper. However, if you are using older TF versions, both formats work out-of-the-box. The SavedModel format works fine for all versions of TF 2.x.
 </details>
 
 
 <details>
 <summary>
 
 #### macOS compatibility</summary>
@@ -141,16 +180,64 @@
 For TF 1, I suggest using the AccumOptimizer implementation in the [H2G-Net repository](https://github.com/andreped/H2G-Net/blob/main/src/utils/accum_optimizers.py#L139) instead, which wraps the optimizer instead of overloading the train_step of the Model itself (new feature in TF2).
 </details>
 
 
 <details>
 <summary>
 
+#### TF >= 2.11 legacy option</summary>
+Note that for TensorFlow >= 2.11, there has been some major changes to the Optimizer class. Our current implementation is not compatible with the new one. Based on which TensorFlow version you have, our `GradientAccumulateOptimizer` dynamically chooses which Optimizer to use.
+
+However, you will need to choose a legacy optimizer to use with the Optimizer wrapper, like so:
+```
+import tensorflow as tf
+from gradient_accumulator import GradientAccumulateOptimizer
+
+opt = tf.keras.optimizers.legacy.SGD(learning_rate=1e-2)
+opt = GradientAccumulateOptimizer(optimizer=opt, accum_steps=4)
+```
+</details>
+
+
+<details>
+<summary>
+
 #### PyTorch</summary>
 For PyTorch, I would recommend using [accelerate](https://pypi.org/project/accelerate/). HuggingFace :hugs: has a great tutorial on how to use it [here](https://huggingface.co/docs/accelerate/usage_guides/gradient_accumulation).
+
+However, if you wish to use native PyTorch and you are implementing your own training loop, you could do something like this:
+```
+# batch accumulation parameter
+accum_iter = 4
+
+# loop through enumaretad batches
+for batch_idx, (inputs, labels) in enumerate(data_loader):
+
+    # extract inputs and labels
+    inputs = inputs.to(device)
+    labels = labels.to(device)
+
+    # passes and weights update
+    with torch.set_grad_enabled(True):
+        
+        # forward pass 
+        preds = model(inputs)
+        loss  = criterion(preds, labels)
+
+        # scale loss prior to accumulation
+        loss = loss / accum_iter
+
+        # backward pass
+        loss.backward()
+
+        # weights update and reset gradients
+        if ((batch_idx + 1) % accum_iter == 0) or (batch_idx + 1 == len(data_loader)):
+            optimizer.step()
+            optimizer.zero_grad()
+```
 </details>
 
 
 <details>
 <summary>
 
 #### Troubleshooting</summary>
@@ -176,18 +263,18 @@
 The optimizer wrapper is derived from [the implementation by @fsx950223 and @stefan-falk](https://github.com/tensorflow/addons/pull/2525).
 
   
 ## How to cite?
 If you used this package or found the project relevant in your research, please, considering including the following citation:
 
 ```
-@software{andre_pedersen_2023_7581815,
+@software{andre_pedersen_2023_7582309,
   author       = {André Pedersen and David Bouget},
-  title        = {andreped/GradientAccumulator: v0.3.0},
+  title        = {andreped/GradientAccumulator: v0.3.1},
   month        = jan,
   year         = 2023,
   publisher    = {Zenodo},
-  version      = {v0.3.0},
-  doi          = {10.5281/zenodo.7581815},
-  url          = {https://doi.org/10.5281/zenodo.7581815}
+  version      = {v0.3.1},
+  doi          = {10.5281/zenodo.7582309},
+  url          = {https://doi.org/10.5281/zenodo.7582309}
 }
 ```
```

### Comparing `gradient-accumulator-0.3.1/gradient_accumulator/accumulators.py` & `gradient-accumulator-0.3.2/gradient_accumulator/accumulators.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,11 +1,17 @@
 import tensorflow as tf
 from . import agc
-from tensorflow_addons.utils import types
-from typeguard import typechecked
+#from tensorflow_addons.utils import types
+#from typeguard import typechecked
+
+
+# need to dynamically handle which Optimizer class to use dependent on tf version
+opt = tf.keras.optimizers.Optimizer
+if int(tf.version.VERSION.split(".")[1]) > 10:
+    opt = tf.keras.optimizers.legacy.Optimizer
 
 
 # https://stackoverflow.com/a/66524901
 # https://keras.io/guides/customizing_what_happens_in_fit/
 @tf.keras.utils.register_keras_serializable()  # adding this avoids needing to use custom_objects when loading model
 class GradientAccumulateModel(tf.keras.Model):
     def __init__(self, accum_steps=1, mixed_precision=False, use_agc=False, clip_factor=0.01, eps=1e-3, *args, **kwargs):
@@ -104,25 +110,17 @@
             ) for i, v in enumerate(self.trainable_variables)
         ]
 
 
 # Implementation was derived from:
 # https://github.com/fsx950223/addons/blob/67c1e8ea19e82c3f2a5706674dd81f15ab5002a2/tensorflow_addons/optimizers/gradient_accumulator.py
 @tf.keras.utils.register_keras_serializable()
-class GradientAccumulateOptimizer(tf.keras.optimizers.Optimizer):
+class GradientAccumulateOptimizer(opt):
     """Optimizer wrapper for gradient accumulation."""
-    @typechecked
-    def __init__(
-        self,
-        optimizer,  # : types.Optimizer,  # having this results in TypeError -> expected OptimizerV2 or str, got dict instead
-        accum_steps: types.TensorLike = 4,
-        reduction: str = "MEAN",
-        name: str = "GradientAccumulateOptimizer",
-        **kwargs,
-    ):
+    def __init__(self, optimizer="SGD", accum_steps=1, reduction: str = "MEAN", name: str = "GradientAccumulateOptimizer", **kwargs):
         r"""Construct a new GradientAccumulateOptimizer optimizer.
 
         Args:
             optimizer: str or `tf.keras.optimizers.Optimizer` that will be
                 used to compute and apply gradients.
             accum_steps: int > 0. Update gradient in every accumulation steps.
             reduction: str. Which gradient reduction method to use. Defaults to 'SUM'.
@@ -131,23 +129,21 @@
             **kwargs: keyword arguments. Allowed to be {`clipnorm`,
                 `clipvalue`, `lr`, `decay`}. `clipnorm` is clip gradients by
                 norm; `clipvalue` is clip gradients by value, `decay` is
                 included for backward compatibility to allow time inverse
                 decay of learning rate. `lr` is included for backward
                 compatibility, recommended to use `learning_rate` instead.
         """
-        self.optimizer = optimizer
-        self._optimizer = tf.keras.optimizers.get(optimizer)
+        self.optimizer = tf.keras.optimizers.get(optimizer)
+        self.accum_steps = accum_steps
         self.reduction = reduction
-        self._gradients = []
-        self._accum_steps = accum_steps
         super().__init__(name, **kwargs)
 
     def _create_slots(self, var_list):
-        self._optimizer._create_slots(var_list=var_list)
+        self.optimizer._create_slots(var_list=var_list)
         for var in var_list:
             self.add_slot(var, "ga")
 
         self._gradients = [self.get_slot(var, "ga") for var in var_list]
 
     @property
     def gradients(self):
@@ -158,77 +154,77 @@
             )
         return list(
             gradient.read_value() if gradient is not None else gradient
             for gradient in self._gradients
         )
 
     def apply_gradients(self, grads_and_vars, name=None, **kwargs):
-        self._optimizer._iterations = self.iterations
+        self.optimizer._iterations = self.iterations
         return super().apply_gradients(grads_and_vars, name, **kwargs)
 
     @tf.function
     def _resource_apply_dense(self, grad, var, apply_state=None):
         accum_gradient = self.get_slot(var, "ga")
 
         if accum_gradient is not None and grad is not None:
             if self.reduction == "MEAN":
-                grad /= tf.cast(self._accum_steps, grad.dtype)
+                grad /= tf.cast(self.accum_steps, grad.dtype)
 
             accum_gradient.assign_add(
                 grad, use_locking=self._use_locking, read_value=False
             )
 
         def _apply():
-            if "apply_state" in self._optimizer._dense_apply_args:
-                train_op = self._optimizer._resource_apply_dense(
+            if "apply_state" in self.optimizer._dense_apply_args:
+                train_op = self.optimizer._resource_apply_dense(
                     accum_gradient.read_value(), var, apply_state=apply_state
                 )
             else:
-                train_op = self._optimizer._resource_apply_dense(
+                train_op = self.optimizer._resource_apply_dense(
                     accum_gradient.read_value(), var
                 )
             reset_op = accum_gradient.assign(
                         tf.zeros_like(accum_gradient),
                         use_locking=self._use_locking,
                         read_value=False,
                     )
             return tf.group(train_op, reset_op)
 
         apply_op = tf.cond(
-            (self.iterations + 1) % self._accum_steps == 0, _apply, lambda: tf.no_op()
+            (self.iterations + 1) % self.accum_steps == 0, _apply, lambda: tf.no_op()
         )
         return apply_op
 
     @tf.function
-    def _resource_apply_sparse(self, grad: types.TensorLike, var, indices, apply_state):
+    def _resource_apply_sparse(self, grad, var, indices, apply_state):
         accum_gradient = self.get_slot(var, "ga")
         if accum_gradient is not None and grad is not None:
             self._resource_scatter_add(accum_gradient, indices, grad)
 
         def _apply():
-            if "apply_state" in self._optimizer._sparse_apply_args:
-                train_op = self._optimizer._resource_apply_sparse(
+            if "apply_state" in self.optimizer._sparse_apply_args:
+                train_op = self.optimizer._resource_apply_sparse(
                     accum_gradient.sparse_read(indices),
                     var,
                     indices,
                     apply_state=apply_state,
                 )
             else:
-                train_op = self._optimizer._resource_apply_sparse(
+                train_op = self.optimizer._resource_apply_sparse(
                     accum_gradient.sparse_read(indices), var, indices
                 )
             reset_op = accum_gradient.assign(
                         tf.zeros_like(accum_gradient),
                         use_locking=self._use_locking,
                         read_value=False,
                     )
             return tf.group(train_op, reset_op)
 
         apply_op = tf.cond(
-            (self.iterations + 1) % self._accum_steps == 0, _apply, lambda: tf.no_op()  # tf.no_op: Does nothing - placeholder
+            (self.iterations + 1) % self.accum_steps == 0, _apply, lambda: tf.no_op()  # tf.no_op: Does nothing - placeholder
         )
         return apply_op
 
     def reset(self):
         """Resets the accumulated gradients on the current replica."""
         assign_ops = []
         if not self._gradients:
@@ -243,29 +239,22 @@
                         read_value=False,
                     )
                 )
 
         return tf.group(assign_ops)
 
     @property
-    def lr(self):
-        return self._optimizer._get_hyper("learning_rate")
-
-    @lr.setter
-    def lr(self, lr):
-        self._optimizer._set_hyper("learning_rate", lr)
-
-    @property
     def learning_rate(self):
-        return self._optimizer._get_hyper("learning_rate")
+        return self.optimizer._get_hyper("learning_rate")
 
     @learning_rate.setter
     def learning_rate(self, learning_rate):
-        self._optimizer._set_hyper("learning_rate", learning_rate)
+        self.optimizer._set_hyper("learning_rate", learning_rate)
 
     def get_config(self):
-        config = super(GradientAccumulateOptimizer, self).get_config()
-        config.update({
-            "optimizer": self.optimizer,
-            "accum_steps": self._accum_steps,
-            "reduction": self.reduction})
-        return config
+        config = {
+            "optimizer": tf.keras.optimizers.get(self.optimizer),
+            "accum_steps": self.accum_steps,
+            "reduction": self.reduction,
+        }
+        base_config = super().get_config()
+        return dict(list(base_config.items()) + list(config.items()))
```

### Comparing `gradient-accumulator-0.3.1/gradient_accumulator/agc.py` & `gradient-accumulator-0.3.2/gradient_accumulator/agc.py`

 * *Files identical despite different names*

### Comparing `gradient-accumulator-0.3.1/gradient_accumulator.egg-info/PKG-INFO` & `gradient-accumulator-0.3.2/gradient_accumulator.egg-info/PKG-INFO`

 * *Files 17% similar despite different names*

```diff
@@ -1,30 +1,32 @@
 Metadata-Version: 2.1
 Name: gradient-accumulator
-Version: 0.3.1
+Version: 0.3.2
 Summary: Package for gradient accumulation in TensorFlow
 Home-page: https://github.com/andreped/GradientAccumulator
 Author: André Pedersen and David Bouget
 Author-email: andrped94@gmail.com
 License: UNKNOWN
 Description: <div align="center">
         <h1 align="center">GradientAccumulator</h1>
         <h3 align="center">Seemless gradient accumulation for TensorFlow 2</h3>
         
         [![Pip Downloads](https://img.shields.io/pypi/dm/gradient-accumulator?label=pip%20downloads&logo=python)](https://pypi.org/project/gradient-accumulator/)
         [![PyPI version](https://badge.fury.io/py/gradient-accumulator.svg)](https://badge.fury.io/py/gradient-accumulator)
         [![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
-        [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7581815.svg)](https://doi.org/10.5281/zenodo.7581815)
+        [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7582309.svg)](https://doi.org/10.5281/zenodo.7582309)
         [![CI](https://github.com/andreped/GradientAccumulator/workflows/CI/badge.svg)](https://github.com/andreped/GradientAccumulator/actions)
+        [![codecov](https://codecov.io/gh/andreped/GradientAccumulator/branch/main/graph/badge.svg?token=MWLK71V750)](https://codecov.io/gh/andreped/GradientAccumulator)
         
         **GradientAccumulator** was developed by SINTEF Health due to the lack of an easy-to-use method for gradient accumulation in TensorFlow 2.
         
-        The package is available on PyPI and is compatible with and have been tested against TF >= 2.3 and Python >= 3.6 (tested with 3.6-3.10), and works cross-platform (Ubuntu, Windows, macOS).
+        The package is available on PyPI and is compatible with and have been tested against `TF 2.2-2.12` and `Python 3.6-3.12`, and works cross-platform (Ubuntu, Windows, macOS).
         </div>
         
+        
         ## What?
         Gradient accumulation (GA) enables reduced GPU memory consumption through dividing a batch into smaller reduced batches, and performing gradient computation either in a distributing setting across multiple GPUs or sequentially on the same GPU. When the full batch is processed, the gradients are the _accumulated_ to produce the full batch gradient.
         
         <p align="center">
         <img src="assets/grad_accum.png" width="50%">
         </p>
         
@@ -33,15 +35,15 @@
         In TensorFlow 2, there did not exist a plug-and-play method to use gradient accumulation with any custom pipeline. Hence, we have implemented two generic TF2-compatible approaches:
         
         | Method | Usage |
         | - | - |
         | `GradientAccumulateModel` | `model = GradientAccumulateModel(accum_steps=4, inputs=model.input, outputs=model.output)` |
         | `GradientAccumulateOptimizer` | `opt = GradientAccumulateOptimizer(accum_steps=4, optimizer=tf.keras.optimizers.SGD(1e-2))` |
         
-        Both approaches control how frequently the weigths are updated, but in their own way. Approach (1) is for single-GPU only, whereas (2) supports both single-GPU and distributed training (multi-GPU).
+        Both approaches control how frequently the weigths are updated, but in their own way. Approach (1) is for single-GPU only, whereas (2) supports both single-GPU and distributed training (multi-GPU). However, note that (2) is not yet working as intended. Hence, use (1) for most applications.
         
         Our implementations enable theoretically **infinitely large batch size**, with **identical memory consumption** as for a regular mini batch. If a single GPU is used, this comes at the cost of increased training runtime. Multiple GPUs could be used to increase runtime performance.
         
         As batch normalization is not natively compatible with GA, support for adaptive gradient clipping has been added as an alternative. We have also added support for mixed precision and both GPU and TPU support.
         
         
         ## Install
@@ -63,15 +65,15 @@
         
         model = Model(...)
         model = GradientAccumulateModel(accum_steps=4, inputs=model.input, outputs=model.output)
         ```
         
         Then simply use the `model` as you normally would!
         
-        <details open>
+        <details>
         <summary>
         
         #### Mixed precision</summary>
         
         There has also been added experimental support for mixed precision:
         ```
         from tensorflow.keras import mixed_precision
@@ -89,27 +91,64 @@
         mixed_precision.set_global_policy('mixed_bfloat16')
         ```
         
         There is also an example of how to use gradient accumulation with mixed precision [here](https://github.com/andreped/GradientAccumulator/blob/main/tests/test_mixed_precision.py#L58).
         </details>
         
         
-        <details open>
+        <details>
         <summary>
         
         #### Distributed training with multiple GPUs</summary>
         In order to use multiple GPUs, you will have to use the Optimizer wrapper:
         ```
         opt = GradientAccumulateOptimizer(accum_steps=4, optimizer=tf.keras.optimizers.SGD(1e-2))
         ```
         
         Just remember to wrap the optimizer within the `tf.distribute.MirroredStrategy`. For an example, see [here](https://github.com/andreped/GradientAccumulator/blob/main/tests/test_optimizer_distribute.py).
         
+        **DISCLAIMER: The GradientAccumulateOptimizer is a VERY experimental feature. It is not reaching the same results as GradientAccumulateModel with a single GPU, and does not work (yet) with multiple GPUs. Hence, I would recommend using GradientAccumulateModel with a single GPU in its current state.**
+        
+        </details>
+        
+        
+        <details>
+        <summary>
+        
+        #### HuggingFace :hugs:</summary>
+        Note that HuggingFace provides a variety of different pretrained models. However, it was observed that when loading these models into TensorFlow, the computational graph may not be set up correctly, such that the `model.input` and `model.output` exist.
+        
+        To fix this, we basically wrap the model into a new `tf.keras.Model`, but define the inputs and outputs ourselves:
+        ```
+        from gradient_accumulator import GradientAccumulateModel
+        from tensorflow.keras.layers import Input
+        from tensorflow.keras.models import Model
+        from transformers import TFx
+        
+        #load your model checkpoint
+        HF_model = TFx.from_pretrained(checkpoint)
+        
+        # define model inputs and outputs -> for different models, different inputs/outputs need to be defined
+        input_ids = tf.keras.Input(shape=(None,), dtype='int32', name="input_ids")
+        attention_mask = tf.keras.Input(shape=(None,), dtype='int32', name="attention_mask")
+        model_input={'input_ids': input_ids, 'attention_mask': attention_mask}
+        
+        #create a new Model which has model.input and model.output properties
+        new_model = Model(inputs=model_input, outputs=HF_model(model_input))
+        
+        #create the GA model
+        model = GradientAccumulateModel(accum_steps=4, inputs=new_model.input, outputs=new_model.output)
+        ```
+          
+        For more details, see [this](https://github.com/andreped/GradientAccumulator/blob/main/notebooks/GA_for_HuggingFace_TF_models.ipynb) jupyter notebook.
+        
         </details>
         
+        
+        
         <details>
         <summary>
         
         #### Adaptive gradient clipping</summary>
         
         There has also been added support for adaptive gradient clipping, based on [this](https://github.com/sayakpaul/Adaptive-Gradient-Clipping) implementation:
         ```
@@ -121,15 +160,15 @@
         
         
         <details>
         <summary>
         
         #### Model format</summary>
         
-        It is recommended to use the SavedModel format when using this implementation. That is because the HDF5 format is only compatible with `TF <= 2.6` when using the model wrapper. However, if you are using older TF versions, both formats work out-of-the-box. The SavedModel format works fine for all versions of TF 2.x
+        It is recommended to use the SavedModel format when using this implementation. That is because the HDF5 format is only compatible with `TF <= 2.6` when using the model wrapper. However, if you are using older TF versions, both formats work out-of-the-box. The SavedModel format works fine for all versions of TF 2.x.
         </details>
         
         
         <details>
         <summary>
         
         #### macOS compatibility</summary>
@@ -149,16 +188,64 @@
         For TF 1, I suggest using the AccumOptimizer implementation in the [H2G-Net repository](https://github.com/andreped/H2G-Net/blob/main/src/utils/accum_optimizers.py#L139) instead, which wraps the optimizer instead of overloading the train_step of the Model itself (new feature in TF2).
         </details>
         
         
         <details>
         <summary>
         
+        #### TF >= 2.11 legacy option</summary>
+        Note that for TensorFlow >= 2.11, there has been some major changes to the Optimizer class. Our current implementation is not compatible with the new one. Based on which TensorFlow version you have, our `GradientAccumulateOptimizer` dynamically chooses which Optimizer to use.
+        
+        However, you will need to choose a legacy optimizer to use with the Optimizer wrapper, like so:
+        ```
+        import tensorflow as tf
+        from gradient_accumulator import GradientAccumulateOptimizer
+        
+        opt = tf.keras.optimizers.legacy.SGD(learning_rate=1e-2)
+        opt = GradientAccumulateOptimizer(optimizer=opt, accum_steps=4)
+        ```
+        </details>
+        
+        
+        <details>
+        <summary>
+        
         #### PyTorch</summary>
         For PyTorch, I would recommend using [accelerate](https://pypi.org/project/accelerate/). HuggingFace :hugs: has a great tutorial on how to use it [here](https://huggingface.co/docs/accelerate/usage_guides/gradient_accumulation).
+        
+        However, if you wish to use native PyTorch and you are implementing your own training loop, you could do something like this:
+        ```
+        # batch accumulation parameter
+        accum_iter = 4
+        
+        # loop through enumaretad batches
+        for batch_idx, (inputs, labels) in enumerate(data_loader):
+        
+            # extract inputs and labels
+            inputs = inputs.to(device)
+            labels = labels.to(device)
+        
+            # passes and weights update
+            with torch.set_grad_enabled(True):
+                
+                # forward pass 
+                preds = model(inputs)
+                loss  = criterion(preds, labels)
+        
+                # scale loss prior to accumulation
+                loss = loss / accum_iter
+        
+                # backward pass
+                loss.backward()
+        
+                # weights update and reset gradients
+                if ((batch_idx + 1) % accum_iter == 0) or (batch_idx + 1 == len(data_loader)):
+                    optimizer.step()
+                    optimizer.zero_grad()
+        ```
         </details>
         
         
         <details>
         <summary>
         
         #### Troubleshooting</summary>
@@ -184,32 +271,34 @@
         The optimizer wrapper is derived from [the implementation by @fsx950223 and @stefan-falk](https://github.com/tensorflow/addons/pull/2525).
         
           
         ## How to cite?
         If you used this package or found the project relevant in your research, please, considering including the following citation:
         
         ```
-        @software{andre_pedersen_2023_7581815,
+        @software{andre_pedersen_2023_7582309,
           author       = {André Pedersen and David Bouget},
-          title        = {andreped/GradientAccumulator: v0.3.0},
+          title        = {andreped/GradientAccumulator: v0.3.1},
           month        = jan,
           year         = 2023,
           publisher    = {Zenodo},
-          version      = {v0.3.0},
-          doi          = {10.5281/zenodo.7581815},
-          url          = {https://doi.org/10.5281/zenodo.7581815}
+          version      = {v0.3.1},
+          doi          = {10.5281/zenodo.7582309},
+          url          = {https://doi.org/10.5281/zenodo.7582309}
         }
         ```
         
 Platform: UNKNOWN
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
 Classifier: Topic :: Scientific/Engineering :: Artificial Intelligence
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Programming Language :: Python :: 3.10
+Classifier: Programming Language :: Python :: 3.11
+Classifier: Programming Language :: Python :: 3.12
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Requires-Python: >=3.6
 Description-Content-Type: text/markdown
```

### Comparing `gradient-accumulator-0.3.1/setup.py` & `gradient-accumulator-0.3.2/setup.py`

 * *Files 15% similar despite different names*

```diff
@@ -1,33 +1,34 @@
 import setuptools
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="gradient-accumulator",
-    version="0.3.1",
+    version="0.3.2",
     author="André Pedersen and David Bouget",
     author_email="andrped94@gmail.com",
     description="Package for gradient accumulation in TensorFlow",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/andreped/GradientAccumulator",
-    packages=setuptools.find_packages(exclude=('tests')),
+    packages=setuptools.find_packages(exclude=('tests', 'notebooks')),
     install_requires=[
-        "tensorflow",
-        "tensorflow-addons"
+        "tensorflow"
     ],
     classifiers=[
         "Development Status :: 4 - Beta",
         "Intended Audience :: Developers",
         "Topic :: Scientific/Engineering :: Artificial Intelligence",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: 3.8",
         "Programming Language :: Python :: 3.9",
         "Programming Language :: Python :: 3.10",
+        "Programming Language :: Python :: 3.11",
+        "Programming Language :: Python :: 3.12",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent"
     ],
     python_requires=">=3.6",
 )
```

