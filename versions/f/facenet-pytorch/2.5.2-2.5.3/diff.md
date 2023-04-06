# Comparing `tmp/facenet-pytorch-2.5.2.tar.gz` & `tmp/facenet-pytorch-2.5.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/facenet-pytorch-2.5.2.tar", last modified: Wed Mar 10 00:59:59 2021, max compression
+gzip compressed data, was "facenet-pytorch-2.5.3.tar", last modified: Thu Apr  6 17:17:37 2023, max compression
```

## Comparing `facenet-pytorch-2.5.2.tar` & `facenet-pytorch-2.5.3.tar`

### file list

```diff
@@ -1,25 +1,26 @@
-drwxrwxr-x   0 tim       (6009) tim       (6009)        0 2021-03-10 00:59:59.000000 facenet-pytorch-2.5.2/
--rw-rw-r--   0 tim       (6009) tim       (6009)    14898 2021-03-10 00:59:59.000000 facenet-pytorch-2.5.2/PKG-INFO
--rw-rw-r--   0 tim       (6009) tim       (6009)    12439 2021-03-10 00:48:16.000000 facenet-pytorch-2.5.2/README.md
--rw-rw-r--   0 tim       (6009) tim       (6009)      393 2020-08-20 20:21:17.000000 facenet-pytorch-2.5.2/__init__.py
-drwxrwxr-x   0 tim       (6009) tim       (6009)        0 2021-03-10 00:59:59.000000 facenet-pytorch-2.5.2/data/
--rw-rw-r--   0 tim       (6009) tim       (6009)  1559269 2020-02-09 00:55:16.000000 facenet-pytorch-2.5.2/data/onet.pt
--rw-rw-r--   0 tim       (6009) tim       (6009)    28570 2020-02-09 00:55:16.000000 facenet-pytorch-2.5.2/data/pnet.pt
--rw-rw-r--   0 tim       (6009) tim       (6009)   403147 2020-02-09 00:55:16.000000 facenet-pytorch-2.5.2/data/rnet.pt
-drwxrwxr-x   0 tim       (6009) tim       (6009)        0 2021-03-10 00:59:59.000000 facenet-pytorch-2.5.2/facenet_pytorch.egg-info/
--rw-rw-r--   0 tim       (6009) tim       (6009)    14898 2021-03-10 00:59:58.000000 facenet-pytorch-2.5.2/facenet_pytorch.egg-info/PKG-INFO
--rw-rw-r--   0 tim       (6009) tim       (6009)      452 2021-03-10 00:59:59.000000 facenet-pytorch-2.5.2/facenet_pytorch.egg-info/SOURCES.txt
--rw-rw-r--   0 tim       (6009) tim       (6009)        1 2021-03-10 00:59:58.000000 facenet-pytorch-2.5.2/facenet_pytorch.egg-info/dependency_links.txt
--rw-rw-r--   0 tim       (6009) tim       (6009)       34 2021-03-10 00:59:58.000000 facenet-pytorch-2.5.2/facenet_pytorch.egg-info/requires.txt
--rw-rw-r--   0 tim       (6009) tim       (6009)       16 2021-03-10 00:59:58.000000 facenet-pytorch-2.5.2/facenet_pytorch.egg-info/top_level.txt
-drwxrwxr-x   0 tim       (6009) tim       (6009)        0 2021-03-10 00:59:59.000000 facenet-pytorch-2.5.2/models/
--rw-rw-r--   0 tim       (6009) tim       (6009)    11054 2020-08-20 20:21:17.000000 facenet-pytorch-2.5.2/models/inception_resnet_v1.py
--rw-rw-r--   0 tim       (6009) tim       (6009)    21105 2021-03-10 00:48:16.000000 facenet-pytorch-2.5.2/models/mtcnn.py
-drwxrwxr-x   0 tim       (6009) tim       (6009)        0 2021-03-10 00:59:59.000000 facenet-pytorch-2.5.2/models/utils/
--rw-rw-r--   0 tim       (6009) tim       (6009)    12230 2021-03-10 00:48:16.000000 facenet-pytorch-2.5.2/models/utils/detect_face.py
--rw-rw-r--   0 tim       (6009) tim       (6009)     3720 2020-08-20 20:21:17.000000 facenet-pytorch-2.5.2/models/utils/download.py
--rw-rw-r--   0 tim       (6009) tim       (6009)    16090 2019-07-03 19:56:50.000000 facenet-pytorch-2.5.2/models/utils/tensorflow2pytorch.py
--rw-rw-r--   0 tim       (6009) tim       (6009)     5128 2019-11-03 00:56:22.000000 facenet-pytorch-2.5.2/models/utils/training.py
--rw-rw-r--   0 tim       (6009) tim       (6009)       38 2021-03-10 00:59:59.000000 facenet-pytorch-2.5.2/setup.cfg
--rw-rw-r--   0 tim       (6009) tim       (6009)     1202 2021-03-10 00:51:35.000000 facenet-pytorch-2.5.2/setup.py
--rw-rw-r--   0 tim       (6009) tim       (6009)       25 2019-09-19 16:50:05.000000 facenet-pytorch-2.5.2/test.py
+drwxr-xr-x   0 timesler (23197709) amazon     (100)        0 2023-04-06 17:17:37.017434 facenet-pytorch-2.5.3/
+-rw-r--r--   0 timesler (23197709) amazon     (100)     1070 2023-04-03 18:18:51.000000 facenet-pytorch-2.5.3/LICENSE.md
+-rw-r--r--   0 timesler (23197709) amazon     (100)    13013 2023-04-06 17:17:37.017434 facenet-pytorch-2.5.3/PKG-INFO
+-rw-r--r--   0 timesler (23197709) amazon     (100)    12569 2023-04-06 17:01:01.000000 facenet-pytorch-2.5.3/README.md
+-rw-r--r--   0 timesler (23197709) amazon     (100)      393 2023-04-03 18:18:51.000000 facenet-pytorch-2.5.3/__init__.py
+drwxr-xr-x   0 timesler (23197709) amazon     (100)        0 2023-04-06 17:17:37.013434 facenet-pytorch-2.5.3/data/
+-rw-r--r--   0 timesler (23197709) amazon     (100)  1559269 2023-04-03 18:18:51.000000 facenet-pytorch-2.5.3/data/onet.pt
+-rw-r--r--   0 timesler (23197709) amazon     (100)    28570 2023-04-03 18:18:51.000000 facenet-pytorch-2.5.3/data/pnet.pt
+-rw-r--r--   0 timesler (23197709) amazon     (100)   403147 2023-04-03 18:18:51.000000 facenet-pytorch-2.5.3/data/rnet.pt
+drwxr-xr-x   0 timesler (23197709) amazon     (100)        0 2023-04-06 17:17:37.017434 facenet-pytorch-2.5.3/facenet_pytorch.egg-info/
+-rw-r--r--   0 timesler (23197709) amazon     (100)    13013 2023-04-06 17:17:37.000000 facenet-pytorch-2.5.3/facenet_pytorch.egg-info/PKG-INFO
+-rw-r--r--   0 timesler (23197709) amazon     (100)      463 2023-04-06 17:17:37.000000 facenet-pytorch-2.5.3/facenet_pytorch.egg-info/SOURCES.txt
+-rw-r--r--   0 timesler (23197709) amazon     (100)        1 2023-04-06 17:17:37.000000 facenet-pytorch-2.5.3/facenet_pytorch.egg-info/dependency_links.txt
+-rw-r--r--   0 timesler (23197709) amazon     (100)       34 2023-04-06 17:17:37.000000 facenet-pytorch-2.5.3/facenet_pytorch.egg-info/requires.txt
+-rw-r--r--   0 timesler (23197709) amazon     (100)       16 2023-04-06 17:17:37.000000 facenet-pytorch-2.5.3/facenet_pytorch.egg-info/top_level.txt
+drwxr-xr-x   0 timesler (23197709) amazon     (100)        0 2023-04-06 17:17:37.013434 facenet-pytorch-2.5.3/models/
+-rw-r--r--   0 timesler (23197709) amazon     (100)    11054 2023-04-03 18:18:51.000000 facenet-pytorch-2.5.3/models/inception_resnet_v1.py
+-rw-r--r--   0 timesler (23197709) amazon     (100)    21148 2023-04-06 17:07:54.000000 facenet-pytorch-2.5.3/models/mtcnn.py
+drwxr-xr-x   0 timesler (23197709) amazon     (100)        0 2023-04-06 17:17:37.017434 facenet-pytorch-2.5.3/models/utils/
+-rw-r--r--   0 timesler (23197709) amazon     (100)    12258 2023-04-06 17:07:54.000000 facenet-pytorch-2.5.3/models/utils/detect_face.py
+-rw-r--r--   0 timesler (23197709) amazon     (100)     3720 2023-04-03 18:18:51.000000 facenet-pytorch-2.5.3/models/utils/download.py
+-rw-r--r--   0 timesler (23197709) amazon     (100)    16090 2023-04-03 18:18:51.000000 facenet-pytorch-2.5.3/models/utils/tensorflow2pytorch.py
+-rw-r--r--   0 timesler (23197709) amazon     (100)     5128 2023-04-03 18:18:51.000000 facenet-pytorch-2.5.3/models/utils/training.py
+-rw-r--r--   0 timesler (23197709) amazon     (100)       38 2023-04-06 17:17:37.017434 facenet-pytorch-2.5.3/setup.cfg
+-rw-r--r--   0 timesler (23197709) amazon     (100)     1202 2023-04-06 17:17:21.000000 facenet-pytorch-2.5.3/setup.py
+-rw-r--r--   0 timesler (23197709) amazon     (100)       26 2023-04-03 18:56:15.000000 facenet-pytorch-2.5.3/test.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `facenet-pytorch-2.5.2/PKG-INFO` & `facenet-pytorch-2.5.3/README.md`

 * *Files 23% similar despite different names*

```diff
@@ -1,263 +1,246 @@
-Metadata-Version: 2.1
-Name: facenet-pytorch
-Version: 2.5.2
-Summary: Pretrained Pytorch face detection and recognition models
-Home-page: https://github.com/timesler/facenet-pytorch
-Author: Tim Esler
-Author-email: tim.esler@gmail.com
-License: UNKNOWN
-Description: [![](data/facenet-pytorch-banner.png)](https://xscode.com/timesler/facenet-pytorch)
-        [![Foo](https://xscode.com/assets/promo-banner.svg)](https://xscode.com/timesler/facenet-pytorch)
-        
-        # Face Recognition Using Pytorch 
-        [![Downloads](https://pepy.tech/badge/facenet-pytorch)](https://pepy.tech/project/facenet-pytorch)
-        
-        [![Code Coverage](https://img.shields.io/codecov/c/github/timesler/facenet-pytorch.svg)](https://codecov.io/gh/timesler/facenet-pytorch)
-        
-        | Python | 3.7 | 3.6 | 3.5 |
-        | :---: | :---: | :---: | :---: |
-        | Status | [![Build Status](https://travis-ci.com/timesler/facenet-pytorch.svg?branch=master)](https://travis-ci.com/timesler/facenet-pytorch) | [![Build Status](https://travis-ci.com/timesler/facenet-pytorch.svg?branch=master)](https://travis-ci.com/timesler/facenet-pytorch) | [![Build Status](https://travis-ci.com/timesler/facenet-pytorch.svg?branch=master)](https://travis-ci.com/timesler/facenet-pytorch) |
-        
-        [![xscode](https://img.shields.io/badge/Available%20on-xs%3Acode-blue?style=?style=plastic&logo=appveyor&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF////////VXz1bAAAAAJ0Uk5T/wDltzBKAAAAlUlEQVR42uzXSwqAMAwE0Mn9L+3Ggtgkk35QwcnSJo9S+yGwM9DCooCbgn4YrJ4CIPUcQF7/XSBbx2TEz4sAZ2q1RAECBAiYBlCtvwN+KiYAlG7UDGj59MViT9hOwEqAhYCtAsUZvL6I6W8c2wcbd+LIWSCHSTeSAAECngN4xxIDSK9f4B9t377Wd7H5Nt7/Xz8eAgwAvesLRjYYPuUAAAAASUVORK5CYII=)](https://xscode.com/timesler/facenet-pytorch)
-        
-        This is a repository for Inception Resnet (V1) models in pytorch, pretrained on VGGFace2 and CASIA-Webface.
-        
-        Pytorch model weights were initialized using parameters ported from David Sandberg's [tensorflow facenet repo](https://github.com/davidsandberg/facenet).
-        
-        Also included in this repo is an efficient pytorch implementation of MTCNN for face detection prior to inference. These models are also pretrained. To our knowledge, this is the fastest MTCNN implementation available.
-        
-        ## Table of contents
-        
-        * [Table of contents](#table-of-contents)
-        * [Quick start](#quick-start)
-        * [Pretrained models](#pretrained-models)
-        * [Example notebooks](#example-notebooks)
-          + [*Complete detection and recognition pipeline*](#complete-detection-and-recognition-pipeline)
-          + [*Face tracking in video streams*](#face-tracking-in-video-streams)
-          + [*Finetuning pretrained models with new data*](#finetuning-pretrained-models-with-new-data)
-          + [*Guide to MTCNN in facenet-pytorch*](#guide-to-mtcnn-in-facenet-pytorch)
-          + [*Performance comparison of face detection packages*](#performance-comparison-of-face-detection-packages)
-          + [*The FastMTCNN algorithm*](#the-fastmtcnn-algorithm)
-        * [Running with docker](#running-with-docker)
-        * [Use this repo in your own git project](#use-this-repo-in-your-own-git-project)
-        * [Conversion of parameters from Tensorflow to Pytorch](#conversion-of-parameters-from-tensorflow-to-pytorch)
-        * [References](#references)
-        
-        ## Quick start
-        
-        1. Install:
-            
-            ```bash
-            # With pip:
-            pip install facenet-pytorch
-            
-            # or clone this repo, removing the '-' to allow python imports:
-            git clone https://github.com/timesler/facenet-pytorch.git facenet_pytorch
-            
-            # or use a docker container (see https://github.com/timesler/docker-jupyter-dl-gpu):
-            docker run -it --rm timesler/jupyter-dl-gpu pip install facenet-pytorch && ipython
-            ```
-            
-        1. In python, import facenet-pytorch and instantiate models:
-            
-            ```python
-            from facenet_pytorch import MTCNN, InceptionResnetV1
-            
-            # If required, create a face detection pipeline using MTCNN:
-            mtcnn = MTCNN(image_size=<image_size>, margin=<margin>)
-            
-            # Create an inception resnet (in eval mode):
-            resnet = InceptionResnetV1(pretrained='vggface2').eval()
-            ```
-            
-        1. Process an image:
-            
-            ```python
-            from PIL import Image
-            
-            img = Image.open(<image path>)
-        
-            # Get cropped and prewhitened image tensor
-            img_cropped = mtcnn(img, save_path=<optional save path>)
-        
-            # Calculate embedding (unsqueeze to add batch dimension)
-            img_embedding = resnet(img_cropped.unsqueeze(0))
-        
-            # Or, if using for VGGFace2 classification
-            resnet.classify = True
-            img_probs = resnet(img_cropped.unsqueeze(0))
-            ```
-        
-        See `help(MTCNN)` and `help(InceptionResnetV1)` for usage and implementation details.
-        
-        ## Pretrained models
-        
-        See: [models/inception_resnet_v1.py](models/inception_resnet_v1.py)
-        
-        The following models have been ported to pytorch (with links to download pytorch state_dict's):
-        
-        |Model name|LFW accuracy (as listed [here](https://github.com/davidsandberg/facenet))|Training dataset|
-        | :- | :-: | -: |
-        |[20180408-102900](https://drive.google.com/uc?export=download&id=12DYdlLesBl3Kk51EtJsyPS8qA7fErWDX) (111MB)|0.9905|CASIA-Webface|
-        |[20180402-114759](https://drive.google.com/uc?export=download&id=1TDZVEBudGaEd5POR5X4ZsMvdsh1h68T1) (107MB)|0.9965|VGGFace2|
-        
-        There is no need to manually download the pretrained state_dict's; they are downloaded automatically on model instantiation and cached for future use in the torch cache. To use an Inception Resnet (V1) model for facial recognition/identification in pytorch, use:
-        
-        ```python
-        from facenet_pytorch import InceptionResnetV1
-        
-        # For a model pretrained on VGGFace2
-        model = InceptionResnetV1(pretrained='vggface2').eval()
-        
-        # For a model pretrained on CASIA-Webface
-        model = InceptionResnetV1(pretrained='casia-webface').eval()
-        
-        # For an untrained model with 100 classes
-        model = InceptionResnetV1(num_classes=100).eval()
-        
-        # For an untrained 1001-class classifier
-        model = InceptionResnetV1(classify=True, num_classes=1001).eval()
-        ```
-        
-        Both pretrained models were trained on 160x160 px images, so will perform best if applied to images resized to this shape. For best results, images should also be cropped to the face using MTCNN (see below).
-        
-        By default, the above models will return 512-dimensional embeddings of images. To enable classification instead, either pass `classify=True` to the model constructor, or you can set the object attribute afterwards with `model.classify = True`. For VGGFace2, the pretrained model will output logit vectors of length 8631, and for CASIA-Webface logit vectors of length 10575.
-        
-        ## Example notebooks
-        
-        ### *Complete detection and recognition pipeline*
-        
-        Face recognition can be easily applied to raw images by first detecting faces using MTCNN before calculating embedding or probabilities using an Inception Resnet model. The example code at [examples/infer.ipynb](examples/infer.ipynb) provides a complete example pipeline utilizing datasets, dataloaders, and optional GPU processing.
-        
-        ### *Face tracking in video streams*
-        
-        MTCNN can be used to build a face tracking system (using the `MTCNN.detect()` method). A full face tracking example can be found at [examples/face_tracking.ipynb](examples/face_tracking.ipynb).
-        
-        ![](examples/tracked.gif)
-        
-        ### *Finetuning pretrained models with new data*
-        
-        In most situations, the best way to implement face recognition is to use the pretrained models directly, with either a clustering algorithm or a simple distance metrics to determine the identity of a face. However, if finetuning is required (i.e., if you want to select identity based on the model's output logits), an example can be found at [examples/finetune.ipynb](examples/finetune.ipynb).
-        
-        ### *Guide to MTCNN in facenet-pytorch*
-        
-        This guide demonstrates the functionality of the MTCNN module. Topics covered are:
-        
-        * Basic usage
-        * Image normalization
-        * Face margins
-        * Multiple faces in a single image
-        * Batched detection
-        * Bounding boxes and facial landmarks
-        * Saving face datasets
-        
-        See the [notebook on kaggle](https://www.kaggle.com/timesler/guide-to-mtcnn-in-facenet-pytorch).
-        
-        ### *Performance comparison of face detection packages*
-        
-        This notebook demonstrates the use of three face detection packages:
-        
-        1. facenet-pytorch
-        1. mtcnn
-        1. dlib
-        
-        Each package is tested for its speed in detecting the faces in a set of 300 images (all frames from one video), with GPU support enabled. Performance is based on Kaggle's P100 notebook kernel. Results are summarized below.
-        
-        |Package|FPS (1080x1920)|FPS (720x1280)|FPS (540x960)|
-        |---|---|---|---|
-        |facenet-pytorch|12.97|20.32|25.50|
-        |facenet-pytorch (non-batched)|9.75|14.81|19.68|
-        |dlib|3.80|8.39|14.53|
-        |mtcnn|3.04|5.70|8.23|
-        
-        ![](examples/performance-comparison.png)
-        
-        See the [notebook on kaggle](https://www.kaggle.com/timesler/comparison-of-face-detection-packages).
-        
-        ### *The FastMTCNN algorithm*
-        
-        This algorithm demonstrates how to achieve extremely efficient face detection specifically in videos, by taking advantage of similarities between adjacent frames.
-        
-        See the [notebook on kaggle](https://www.kaggle.com/timesler/fast-mtcnn-detector-55-fps-at-full-resolution).
-        
-        ## Running with docker
-        
-        The package and any of the example notebooks can be run with docker (or nvidia-docker) using:
-        
-        ```bash
-        docker run --rm -p 8888:8888
-            -v ./facenet-pytorch:/home/jovyan timesler/jupyter-dl-gpu \
-            -v <path to data>:/home/jovyan/data
-            pip install facenet-pytorch && jupyter lab 
-        ```
-        
-        Navigate to the examples/ directory and run any of the ipython notebooks.
-        
-        See [timesler/jupyter-dl-gpu](https://github.com/timesler/docker-jupyter-dl-gpu) for docker container details.
-        
-        ## Use this repo in your own git project
-        
-        To use this code in your own git repo, I recommend first adding this repo as a submodule. Note that the dash ('-') in the repo name should be removed when cloning as a submodule as it will break python when importing:
-        
-        `git submodule add https://github.com/timesler/facenet-pytorch.git facenet_pytorch`
-        
-        Alternatively, the code can be installed as a package using pip:
-        
-        `pip install facenet-pytorch`
-        
-        ## Conversion of parameters from Tensorflow to Pytorch
-        
-        See: [models/utils/tensorflow2pytorch.py](models/tensorflow2pytorch.py)
-        
-        Note that this functionality is not needed to use the models in this repo, which depend only on the saved pytorch `state_dict`'s. 
-        
-        Following instantiation of the pytorch model, each layer's weights were loaded from equivalent layers in the pretrained tensorflow models from [davidsandberg/facenet](https://github.com/davidsandberg/facenet).
-        
-        The equivalence of the outputs from the original tensorflow models and the pytorch-ported models have been tested and are identical:
-        
-        ---
-        
-        `>>> compare_model_outputs(mdl, sess, torch.randn(5, 160, 160, 3).detach())`
-        
-        ```
-        Passing test data through TF model
-        
-        tensor([[-0.0142,  0.0615,  0.0057,  ...,  0.0497,  0.0375, -0.0838],
-                [-0.0139,  0.0611,  0.0054,  ...,  0.0472,  0.0343, -0.0850],
-                [-0.0238,  0.0619,  0.0124,  ...,  0.0598,  0.0334, -0.0852],
-                [-0.0089,  0.0548,  0.0032,  ...,  0.0506,  0.0337, -0.0881],
-                [-0.0173,  0.0630, -0.0042,  ...,  0.0487,  0.0295, -0.0791]])
-        
-        Passing test data through PT model
-        
-        tensor([[-0.0142,  0.0615,  0.0057,  ...,  0.0497,  0.0375, -0.0838],
-                [-0.0139,  0.0611,  0.0054,  ...,  0.0472,  0.0343, -0.0850],
-                [-0.0238,  0.0619,  0.0124,  ...,  0.0598,  0.0334, -0.0852],
-                [-0.0089,  0.0548,  0.0032,  ...,  0.0506,  0.0337, -0.0881],
-                [-0.0173,  0.0630, -0.0042,  ...,  0.0487,  0.0295, -0.0791]],
-               grad_fn=<DivBackward0>)
-        
-        Distance 1.2874517096861382e-06
-        ```
-        
-        ---
-        
-        In order to re-run the conversion of tensorflow parameters into the pytorch model, ensure you clone this repo _with submodules_, as the davidsandberg/facenet repo is included as a submodule and parts of it are required for the conversion.
-        
-        ## References
-        
-        1. David Sandberg's facenet repo: [https://github.com/davidsandberg/facenet](https://github.com/davidsandberg/facenet)
-        
-        1. F. Schroff, D. Kalenichenko, J. Philbin. _FaceNet: A Unified Embedding for Face Recognition and Clustering_, arXiv:1503.03832, 2015. [PDF](https://arxiv.org/pdf/1503.03832)
-        
-        1. Q. Cao, L. Shen, W. Xie, O. M. Parkhi, A. Zisserman. _VGGFace2: A dataset for recognising face across pose and age_, International Conference on Automatic Face and Gesture Recognition, 2018. [PDF](http://www.robots.ox.ac.uk/~vgg/publications/2018/Cao18/cao18.pdf)
-        
-        1. D. Yi, Z. Lei, S. Liao and S. Z. Li. _CASIAWebface: Learning Face Representation from Scratch_, arXiv:1411.7923, 2014. [PDF](https://arxiv.org/pdf/1411.7923)
-        
-        1. K. Zhang, Z. Zhang, Z. Li and Y. Qiao. _Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks_, IEEE Signal Processing Letters, 2016. [PDF](https://kpzhang93.github.io/MTCNN_face_detection_alignment/paper/spl.pdf)
-        
-Platform: UNKNOWN
-Classifier: Programming Language :: Python :: 3
-Classifier: License :: OSI Approved :: MIT License
-Classifier: Operating System :: OS Independent
-Description-Content-Type: text/markdown
+# Face Recognition Using Pytorch 
+[![Downloads](https://pepy.tech/badge/facenet-pytorch)](https://pepy.tech/project/facenet-pytorch)
+
+[![Code Coverage](https://img.shields.io/codecov/c/github/timesler/facenet-pytorch.svg)](https://codecov.io/gh/timesler/facenet-pytorch)
+
+| Python | 3.10 | 3.9 | 3.8 |
+| :---: | :---: | :---: | :---: |
+| Status | [![Build Status](https://github.com/timesler/facenet-pytorch/actions/workflows/python-3.10.yml/badge.svg?branch=master)](https://github.com/timesler/facenet-pytorch/actions?query=workflow%3A%22Python+3.10%22+branch%3Amaster) | [![Build Status](https://github.com/timesler/facenet-pytorch/actions/workflows/python-3.9.yml/badge.svg?branch=master)](https://github.com/timesler/facenet-pytorch/actions?query=workflow%3A%22Python+3.9%22+branch%3Amaster) | [![Build Status](https://github.com/timesler/facenet-pytorch/actions/workflows/python-3.8.yml/badge.svg?branch=master)](https://github.com/timesler/facenet-pytorch/actions?query=workflow%3A%22Python+3.8%22+branch%3Amaster) |
+
+[![xscode](https://img.shields.io/badge/Available%20on-xs%3Acode-blue?style=?style=plastic&logo=appveyor&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF////////VXz1bAAAAAJ0Uk5T/wDltzBKAAAAlUlEQVR42uzXSwqAMAwE0Mn9L+3Ggtgkk35QwcnSJo9S+yGwM9DCooCbgn4YrJ4CIPUcQF7/XSBbx2TEz4sAZ2q1RAECBAiYBlCtvwN+KiYAlG7UDGj59MViT9hOwEqAhYCtAsUZvL6I6W8c2wcbd+LIWSCHSTeSAAECngN4xxIDSK9f4B9t377Wd7H5Nt7/Xz8eAgwAvesLRjYYPuUAAAAASUVORK5CYII=)](https://xscode.com/timesler/facenet-pytorch)
+
+This is a repository for Inception Resnet (V1) models in pytorch, pretrained on VGGFace2 and CASIA-Webface.
+
+Pytorch model weights were initialized using parameters ported from David Sandberg's [tensorflow facenet repo](https://github.com/davidsandberg/facenet).
+
+Also included in this repo is an efficient pytorch implementation of MTCNN for face detection prior to inference. These models are also pretrained. To our knowledge, this is the fastest MTCNN implementation available.
+
+## Table of contents
+
+* [Table of contents](#table-of-contents)
+* [Quick start](#quick-start)
+* [Pretrained models](#pretrained-models)
+* [Example notebooks](#example-notebooks)
+  + [*Complete detection and recognition pipeline*](#complete-detection-and-recognition-pipeline)
+  + [*Face tracking in video streams*](#face-tracking-in-video-streams)
+  + [*Finetuning pretrained models with new data*](#finetuning-pretrained-models-with-new-data)
+  + [*Guide to MTCNN in facenet-pytorch*](#guide-to-mtcnn-in-facenet-pytorch)
+  + [*Performance comparison of face detection packages*](#performance-comparison-of-face-detection-packages)
+  + [*The FastMTCNN algorithm*](#the-fastmtcnn-algorithm)
+* [Running with docker](#running-with-docker)
+* [Use this repo in your own git project](#use-this-repo-in-your-own-git-project)
+* [Conversion of parameters from Tensorflow to Pytorch](#conversion-of-parameters-from-tensorflow-to-pytorch)
+* [References](#references)
+
+## Quick start
+
+1. Install:
+    
+    ```bash
+    # With pip:
+    pip install facenet-pytorch
+    
+    # or clone this repo, removing the '-' to allow python imports:
+    git clone https://github.com/timesler/facenet-pytorch.git facenet_pytorch
+    
+    # or use a docker container (see https://github.com/timesler/docker-jupyter-dl-gpu):
+    docker run -it --rm timesler/jupyter-dl-gpu pip install facenet-pytorch && ipython
+    ```
+    
+1. In python, import facenet-pytorch and instantiate models:
+    
+    ```python
+    from facenet_pytorch import MTCNN, InceptionResnetV1
+    
+    # If required, create a face detection pipeline using MTCNN:
+    mtcnn = MTCNN(image_size=<image_size>, margin=<margin>)
+    
+    # Create an inception resnet (in eval mode):
+    resnet = InceptionResnetV1(pretrained='vggface2').eval()
+    ```
+    
+1. Process an image:
+    
+    ```python
+    from PIL import Image
+    
+    img = Image.open(<image path>)
+
+    # Get cropped and prewhitened image tensor
+    img_cropped = mtcnn(img, save_path=<optional save path>)
+
+    # Calculate embedding (unsqueeze to add batch dimension)
+    img_embedding = resnet(img_cropped.unsqueeze(0))
+
+    # Or, if using for VGGFace2 classification
+    resnet.classify = True
+    img_probs = resnet(img_cropped.unsqueeze(0))
+    ```
+
+See `help(MTCNN)` and `help(InceptionResnetV1)` for usage and implementation details.
+
+## Pretrained models
+
+See: [models/inception_resnet_v1.py](models/inception_resnet_v1.py)
+
+The following models have been ported to pytorch (with links to download pytorch state_dict's):
+
+|Model name|LFW accuracy (as listed [here](https://github.com/davidsandberg/facenet))|Training dataset|
+| :- | :-: | -: |
+|[20180408-102900](https://github.com/timesler/facenet-pytorch/releases/download/v2.2.9/20180408-102900-casia-webface.pt) (111MB)|0.9905|CASIA-Webface|
+|[20180402-114759](https://github.com/timesler/facenet-pytorch/releases/download/v2.2.9/20180402-114759-vggface2.pt) (107MB)|0.9965|VGGFace2|
+
+There is no need to manually download the pretrained state_dict's; they are downloaded automatically on model instantiation and cached for future use in the torch cache. To use an Inception Resnet (V1) model for facial recognition/identification in pytorch, use:
+
+```python
+from facenet_pytorch import InceptionResnetV1
+
+# For a model pretrained on VGGFace2
+model = InceptionResnetV1(pretrained='vggface2').eval()
+
+# For a model pretrained on CASIA-Webface
+model = InceptionResnetV1(pretrained='casia-webface').eval()
+
+# For an untrained model with 100 classes
+model = InceptionResnetV1(num_classes=100).eval()
+
+# For an untrained 1001-class classifier
+model = InceptionResnetV1(classify=True, num_classes=1001).eval()
+```
+
+Both pretrained models were trained on 160x160 px images, so will perform best if applied to images resized to this shape. For best results, images should also be cropped to the face using MTCNN (see below).
+
+By default, the above models will return 512-dimensional embeddings of images. To enable classification instead, either pass `classify=True` to the model constructor, or you can set the object attribute afterwards with `model.classify = True`. For VGGFace2, the pretrained model will output logit vectors of length 8631, and for CASIA-Webface logit vectors of length 10575.
+
+## Example notebooks
+
+### *Complete detection and recognition pipeline*
+
+Face recognition can be easily applied to raw images by first detecting faces using MTCNN before calculating embedding or probabilities using an Inception Resnet model. The example code at [examples/infer.ipynb](examples/infer.ipynb) provides a complete example pipeline utilizing datasets, dataloaders, and optional GPU processing.
+
+### *Face tracking in video streams*
+
+MTCNN can be used to build a face tracking system (using the `MTCNN.detect()` method). A full face tracking example can be found at [examples/face_tracking.ipynb](examples/face_tracking.ipynb).
+
+![](examples/tracked.gif)
+
+### *Finetuning pretrained models with new data*
+
+In most situations, the best way to implement face recognition is to use the pretrained models directly, with either a clustering algorithm or a simple distance metrics to determine the identity of a face. However, if finetuning is required (i.e., if you want to select identity based on the model's output logits), an example can be found at [examples/finetune.ipynb](examples/finetune.ipynb).
+
+### *Guide to MTCNN in facenet-pytorch*
+
+This guide demonstrates the functionality of the MTCNN module. Topics covered are:
+
+* Basic usage
+* Image normalization
+* Face margins
+* Multiple faces in a single image
+* Batched detection
+* Bounding boxes and facial landmarks
+* Saving face datasets
+
+See the [notebook on kaggle](https://www.kaggle.com/timesler/guide-to-mtcnn-in-facenet-pytorch).
+
+### *Performance comparison of face detection packages*
+
+This notebook demonstrates the use of three face detection packages:
+
+1. facenet-pytorch
+1. mtcnn
+1. dlib
+
+Each package is tested for its speed in detecting the faces in a set of 300 images (all frames from one video), with GPU support enabled. Performance is based on Kaggle's P100 notebook kernel. Results are summarized below.
+
+|Package|FPS (1080x1920)|FPS (720x1280)|FPS (540x960)|
+|---|---|---|---|
+|facenet-pytorch|12.97|20.32|25.50|
+|facenet-pytorch (non-batched)|9.75|14.81|19.68|
+|dlib|3.80|8.39|14.53|
+|mtcnn|3.04|5.70|8.23|
+
+![](examples/performance-comparison.png)
+
+See the [notebook on kaggle](https://www.kaggle.com/timesler/comparison-of-face-detection-packages).
+
+### *The FastMTCNN algorithm*
+
+This algorithm demonstrates how to achieve extremely efficient face detection specifically in videos, by taking advantage of similarities between adjacent frames.
+
+See the [notebook on kaggle](https://www.kaggle.com/timesler/fast-mtcnn-detector-55-fps-at-full-resolution).
+
+## Running with docker
+
+The package and any of the example notebooks can be run with docker (or nvidia-docker) using:
+
+```bash
+docker run --rm -p 8888:8888
+    -v ./facenet-pytorch:/home/jovyan timesler/jupyter-dl-gpu \
+    -v <path to data>:/home/jovyan/data
+    pip install facenet-pytorch && jupyter lab 
+```
+
+Navigate to the examples/ directory and run any of the ipython notebooks.
+
+See [timesler/jupyter-dl-gpu](https://github.com/timesler/docker-jupyter-dl-gpu) for docker container details.
+
+## Use this repo in your own git project
+
+To use this code in your own git repo, I recommend first adding this repo as a submodule. Note that the dash ('-') in the repo name should be removed when cloning as a submodule as it will break python when importing:
+
+`git submodule add https://github.com/timesler/facenet-pytorch.git facenet_pytorch`
+
+Alternatively, the code can be installed as a package using pip:
+
+`pip install facenet-pytorch`
+
+## Conversion of parameters from Tensorflow to Pytorch
+
+See: [models/utils/tensorflow2pytorch.py](models/tensorflow2pytorch.py)
+
+Note that this functionality is not needed to use the models in this repo, which depend only on the saved pytorch `state_dict`'s. 
+
+Following instantiation of the pytorch model, each layer's weights were loaded from equivalent layers in the pretrained tensorflow models from [davidsandberg/facenet](https://github.com/davidsandberg/facenet).
+
+The equivalence of the outputs from the original tensorflow models and the pytorch-ported models have been tested and are identical:
+
+---
+
+`>>> compare_model_outputs(mdl, sess, torch.randn(5, 160, 160, 3).detach())`
+
+```
+Passing test data through TF model
+
+tensor([[-0.0142,  0.0615,  0.0057,  ...,  0.0497,  0.0375, -0.0838],
+        [-0.0139,  0.0611,  0.0054,  ...,  0.0472,  0.0343, -0.0850],
+        [-0.0238,  0.0619,  0.0124,  ...,  0.0598,  0.0334, -0.0852],
+        [-0.0089,  0.0548,  0.0032,  ...,  0.0506,  0.0337, -0.0881],
+        [-0.0173,  0.0630, -0.0042,  ...,  0.0487,  0.0295, -0.0791]])
+
+Passing test data through PT model
+
+tensor([[-0.0142,  0.0615,  0.0057,  ...,  0.0497,  0.0375, -0.0838],
+        [-0.0139,  0.0611,  0.0054,  ...,  0.0472,  0.0343, -0.0850],
+        [-0.0238,  0.0619,  0.0124,  ...,  0.0598,  0.0334, -0.0852],
+        [-0.0089,  0.0548,  0.0032,  ...,  0.0506,  0.0337, -0.0881],
+        [-0.0173,  0.0630, -0.0042,  ...,  0.0487,  0.0295, -0.0791]],
+       grad_fn=<DivBackward0>)
+
+Distance 1.2874517096861382e-06
+```
+
+---
+
+In order to re-run the conversion of tensorflow parameters into the pytorch model, ensure you clone this repo _with submodules_, as the davidsandberg/facenet repo is included as a submodule and parts of it are required for the conversion.
+
+## References
+
+1. David Sandberg's facenet repo: [https://github.com/davidsandberg/facenet](https://github.com/davidsandberg/facenet)
+
+1. F. Schroff, D. Kalenichenko, J. Philbin. _FaceNet: A Unified Embedding for Face Recognition and Clustering_, arXiv:1503.03832, 2015. [PDF](https://arxiv.org/pdf/1503.03832)
+
+1. Q. Cao, L. Shen, W. Xie, O. M. Parkhi, A. Zisserman. _VGGFace2: A dataset for recognising face across pose and age_, International Conference on Automatic Face and Gesture Recognition, 2018. [PDF](http://www.robots.ox.ac.uk/~vgg/publications/2018/Cao18/cao18.pdf)
+
+1. D. Yi, Z. Lei, S. Liao and S. Z. Li. _CASIAWebface: Learning Face Representation from Scratch_, arXiv:1411.7923, 2014. [PDF](https://arxiv.org/pdf/1411.7923)
+
+1. K. Zhang, Z. Zhang, Z. Li and Y. Qiao. _Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks_, IEEE Signal Processing Letters, 2016. [PDF](https://kpzhang93.github.io/MTCNN_face_detection_alignment/paper/spl.pdf)
```

### Comparing `facenet-pytorch-2.5.2/README.md` & `facenet-pytorch-2.5.3/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,18 +1,28 @@
-[![](data/facenet-pytorch-banner.png)](https://xscode.com/timesler/facenet-pytorch)
-[![Foo](https://xscode.com/assets/promo-banner.svg)](https://xscode.com/timesler/facenet-pytorch)
+Metadata-Version: 2.1
+Name: facenet-pytorch
+Version: 2.5.3
+Summary: Pretrained Pytorch face detection and recognition models
+Home-page: https://github.com/timesler/facenet-pytorch
+Author: Tim Esler
+Author-email: tim.esler@gmail.com
+Classifier: Programming Language :: Python :: 3
+Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent
+Description-Content-Type: text/markdown
+License-File: LICENSE.md
 
 # Face Recognition Using Pytorch 
 [![Downloads](https://pepy.tech/badge/facenet-pytorch)](https://pepy.tech/project/facenet-pytorch)
 
 [![Code Coverage](https://img.shields.io/codecov/c/github/timesler/facenet-pytorch.svg)](https://codecov.io/gh/timesler/facenet-pytorch)
 
-| Python | 3.7 | 3.6 | 3.5 |
+| Python | 3.10 | 3.9 | 3.8 |
 | :---: | :---: | :---: | :---: |
-| Status | [![Build Status](https://travis-ci.com/timesler/facenet-pytorch.svg?branch=master)](https://travis-ci.com/timesler/facenet-pytorch) | [![Build Status](https://travis-ci.com/timesler/facenet-pytorch.svg?branch=master)](https://travis-ci.com/timesler/facenet-pytorch) | [![Build Status](https://travis-ci.com/timesler/facenet-pytorch.svg?branch=master)](https://travis-ci.com/timesler/facenet-pytorch) |
+| Status | [![Build Status](https://github.com/timesler/facenet-pytorch/actions/workflows/python-3.10.yml/badge.svg?branch=master)](https://github.com/timesler/facenet-pytorch/actions?query=workflow%3A%22Python+3.10%22+branch%3Amaster) | [![Build Status](https://github.com/timesler/facenet-pytorch/actions/workflows/python-3.9.yml/badge.svg?branch=master)](https://github.com/timesler/facenet-pytorch/actions?query=workflow%3A%22Python+3.9%22+branch%3Amaster) | [![Build Status](https://github.com/timesler/facenet-pytorch/actions/workflows/python-3.8.yml/badge.svg?branch=master)](https://github.com/timesler/facenet-pytorch/actions?query=workflow%3A%22Python+3.8%22+branch%3Amaster) |
 
 [![xscode](https://img.shields.io/badge/Available%20on-xs%3Acode-blue?style=?style=plastic&logo=appveyor&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF////////VXz1bAAAAAJ0Uk5T/wDltzBKAAAAlUlEQVR42uzXSwqAMAwE0Mn9L+3Ggtgkk35QwcnSJo9S+yGwM9DCooCbgn4YrJ4CIPUcQF7/XSBbx2TEz4sAZ2q1RAECBAiYBlCtvwN+KiYAlG7UDGj59MViT9hOwEqAhYCtAsUZvL6I6W8c2wcbd+LIWSCHSTeSAAECngN4xxIDSK9f4B9t377Wd7H5Nt7/Xz8eAgwAvesLRjYYPuUAAAAASUVORK5CYII=)](https://xscode.com/timesler/facenet-pytorch)
 
 This is a repository for Inception Resnet (V1) models in pytorch, pretrained on VGGFace2 and CASIA-Webface.
 
 Pytorch model weights were initialized using parameters ported from David Sandberg's [tensorflow facenet repo](https://github.com/davidsandberg/facenet).
 
@@ -86,16 +96,16 @@
 
 See: [models/inception_resnet_v1.py](models/inception_resnet_v1.py)
 
 The following models have been ported to pytorch (with links to download pytorch state_dict's):
 
 |Model name|LFW accuracy (as listed [here](https://github.com/davidsandberg/facenet))|Training dataset|
 | :- | :-: | -: |
-|[20180408-102900](https://drive.google.com/uc?export=download&id=12DYdlLesBl3Kk51EtJsyPS8qA7fErWDX) (111MB)|0.9905|CASIA-Webface|
-|[20180402-114759](https://drive.google.com/uc?export=download&id=1TDZVEBudGaEd5POR5X4ZsMvdsh1h68T1) (107MB)|0.9965|VGGFace2|
+|[20180408-102900](https://github.com/timesler/facenet-pytorch/releases/download/v2.2.9/20180408-102900-casia-webface.pt) (111MB)|0.9905|CASIA-Webface|
+|[20180402-114759](https://github.com/timesler/facenet-pytorch/releases/download/v2.2.9/20180402-114759-vggface2.pt) (107MB)|0.9965|VGGFace2|
 
 There is no need to manually download the pretrained state_dict's; they are downloaded automatically on model instantiation and cached for future use in the torch cache. To use an Inception Resnet (V1) model for facial recognition/identification in pytorch, use:
 
 ```python
 from facenet_pytorch import InceptionResnetV1
 
 # For a model pretrained on VGGFace2
```

### Comparing `facenet-pytorch-2.5.2/data/onet.pt` & `facenet-pytorch-2.5.3/data/onet.pt`

 * *Files identical despite different names*

### Comparing `facenet-pytorch-2.5.2/data/pnet.pt` & `facenet-pytorch-2.5.3/data/pnet.pt`

 * *Files identical despite different names*

### Comparing `facenet-pytorch-2.5.2/data/rnet.pt` & `facenet-pytorch-2.5.3/data/rnet.pt`

 * *Files identical despite different names*

### Comparing `facenet-pytorch-2.5.2/facenet_pytorch.egg-info/PKG-INFO` & `facenet-pytorch-2.5.3/facenet_pytorch.egg-info/PKG-INFO`

 * *Files 24% similar despite different names*

```diff
@@ -1,263 +1,259 @@
 Metadata-Version: 2.1
 Name: facenet-pytorch
-Version: 2.5.2
+Version: 2.5.3
 Summary: Pretrained Pytorch face detection and recognition models
 Home-page: https://github.com/timesler/facenet-pytorch
 Author: Tim Esler
 Author-email: tim.esler@gmail.com
-License: UNKNOWN
-Description: [![](data/facenet-pytorch-banner.png)](https://xscode.com/timesler/facenet-pytorch)
-        [![Foo](https://xscode.com/assets/promo-banner.svg)](https://xscode.com/timesler/facenet-pytorch)
-        
-        # Face Recognition Using Pytorch 
-        [![Downloads](https://pepy.tech/badge/facenet-pytorch)](https://pepy.tech/project/facenet-pytorch)
-        
-        [![Code Coverage](https://img.shields.io/codecov/c/github/timesler/facenet-pytorch.svg)](https://codecov.io/gh/timesler/facenet-pytorch)
-        
-        | Python | 3.7 | 3.6 | 3.5 |
-        | :---: | :---: | :---: | :---: |
-        | Status | [![Build Status](https://travis-ci.com/timesler/facenet-pytorch.svg?branch=master)](https://travis-ci.com/timesler/facenet-pytorch) | [![Build Status](https://travis-ci.com/timesler/facenet-pytorch.svg?branch=master)](https://travis-ci.com/timesler/facenet-pytorch) | [![Build Status](https://travis-ci.com/timesler/facenet-pytorch.svg?branch=master)](https://travis-ci.com/timesler/facenet-pytorch) |
-        
-        [![xscode](https://img.shields.io/badge/Available%20on-xs%3Acode-blue?style=?style=plastic&logo=appveyor&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF////////VXz1bAAAAAJ0Uk5T/wDltzBKAAAAlUlEQVR42uzXSwqAMAwE0Mn9L+3Ggtgkk35QwcnSJo9S+yGwM9DCooCbgn4YrJ4CIPUcQF7/XSBbx2TEz4sAZ2q1RAECBAiYBlCtvwN+KiYAlG7UDGj59MViT9hOwEqAhYCtAsUZvL6I6W8c2wcbd+LIWSCHSTeSAAECngN4xxIDSK9f4B9t377Wd7H5Nt7/Xz8eAgwAvesLRjYYPuUAAAAASUVORK5CYII=)](https://xscode.com/timesler/facenet-pytorch)
-        
-        This is a repository for Inception Resnet (V1) models in pytorch, pretrained on VGGFace2 and CASIA-Webface.
-        
-        Pytorch model weights were initialized using parameters ported from David Sandberg's [tensorflow facenet repo](https://github.com/davidsandberg/facenet).
-        
-        Also included in this repo is an efficient pytorch implementation of MTCNN for face detection prior to inference. These models are also pretrained. To our knowledge, this is the fastest MTCNN implementation available.
-        
-        ## Table of contents
-        
-        * [Table of contents](#table-of-contents)
-        * [Quick start](#quick-start)
-        * [Pretrained models](#pretrained-models)
-        * [Example notebooks](#example-notebooks)
-          + [*Complete detection and recognition pipeline*](#complete-detection-and-recognition-pipeline)
-          + [*Face tracking in video streams*](#face-tracking-in-video-streams)
-          + [*Finetuning pretrained models with new data*](#finetuning-pretrained-models-with-new-data)
-          + [*Guide to MTCNN in facenet-pytorch*](#guide-to-mtcnn-in-facenet-pytorch)
-          + [*Performance comparison of face detection packages*](#performance-comparison-of-face-detection-packages)
-          + [*The FastMTCNN algorithm*](#the-fastmtcnn-algorithm)
-        * [Running with docker](#running-with-docker)
-        * [Use this repo in your own git project](#use-this-repo-in-your-own-git-project)
-        * [Conversion of parameters from Tensorflow to Pytorch](#conversion-of-parameters-from-tensorflow-to-pytorch)
-        * [References](#references)
-        
-        ## Quick start
-        
-        1. Install:
-            
-            ```bash
-            # With pip:
-            pip install facenet-pytorch
-            
-            # or clone this repo, removing the '-' to allow python imports:
-            git clone https://github.com/timesler/facenet-pytorch.git facenet_pytorch
-            
-            # or use a docker container (see https://github.com/timesler/docker-jupyter-dl-gpu):
-            docker run -it --rm timesler/jupyter-dl-gpu pip install facenet-pytorch && ipython
-            ```
-            
-        1. In python, import facenet-pytorch and instantiate models:
-            
-            ```python
-            from facenet_pytorch import MTCNN, InceptionResnetV1
-            
-            # If required, create a face detection pipeline using MTCNN:
-            mtcnn = MTCNN(image_size=<image_size>, margin=<margin>)
-            
-            # Create an inception resnet (in eval mode):
-            resnet = InceptionResnetV1(pretrained='vggface2').eval()
-            ```
-            
-        1. Process an image:
-            
-            ```python
-            from PIL import Image
-            
-            img = Image.open(<image path>)
-        
-            # Get cropped and prewhitened image tensor
-            img_cropped = mtcnn(img, save_path=<optional save path>)
-        
-            # Calculate embedding (unsqueeze to add batch dimension)
-            img_embedding = resnet(img_cropped.unsqueeze(0))
-        
-            # Or, if using for VGGFace2 classification
-            resnet.classify = True
-            img_probs = resnet(img_cropped.unsqueeze(0))
-            ```
-        
-        See `help(MTCNN)` and `help(InceptionResnetV1)` for usage and implementation details.
-        
-        ## Pretrained models
-        
-        See: [models/inception_resnet_v1.py](models/inception_resnet_v1.py)
-        
-        The following models have been ported to pytorch (with links to download pytorch state_dict's):
-        
-        |Model name|LFW accuracy (as listed [here](https://github.com/davidsandberg/facenet))|Training dataset|
-        | :- | :-: | -: |
-        |[20180408-102900](https://drive.google.com/uc?export=download&id=12DYdlLesBl3Kk51EtJsyPS8qA7fErWDX) (111MB)|0.9905|CASIA-Webface|
-        |[20180402-114759](https://drive.google.com/uc?export=download&id=1TDZVEBudGaEd5POR5X4ZsMvdsh1h68T1) (107MB)|0.9965|VGGFace2|
-        
-        There is no need to manually download the pretrained state_dict's; they are downloaded automatically on model instantiation and cached for future use in the torch cache. To use an Inception Resnet (V1) model for facial recognition/identification in pytorch, use:
-        
-        ```python
-        from facenet_pytorch import InceptionResnetV1
-        
-        # For a model pretrained on VGGFace2
-        model = InceptionResnetV1(pretrained='vggface2').eval()
-        
-        # For a model pretrained on CASIA-Webface
-        model = InceptionResnetV1(pretrained='casia-webface').eval()
-        
-        # For an untrained model with 100 classes
-        model = InceptionResnetV1(num_classes=100).eval()
-        
-        # For an untrained 1001-class classifier
-        model = InceptionResnetV1(classify=True, num_classes=1001).eval()
-        ```
-        
-        Both pretrained models were trained on 160x160 px images, so will perform best if applied to images resized to this shape. For best results, images should also be cropped to the face using MTCNN (see below).
-        
-        By default, the above models will return 512-dimensional embeddings of images. To enable classification instead, either pass `classify=True` to the model constructor, or you can set the object attribute afterwards with `model.classify = True`. For VGGFace2, the pretrained model will output logit vectors of length 8631, and for CASIA-Webface logit vectors of length 10575.
-        
-        ## Example notebooks
-        
-        ### *Complete detection and recognition pipeline*
-        
-        Face recognition can be easily applied to raw images by first detecting faces using MTCNN before calculating embedding or probabilities using an Inception Resnet model. The example code at [examples/infer.ipynb](examples/infer.ipynb) provides a complete example pipeline utilizing datasets, dataloaders, and optional GPU processing.
-        
-        ### *Face tracking in video streams*
-        
-        MTCNN can be used to build a face tracking system (using the `MTCNN.detect()` method). A full face tracking example can be found at [examples/face_tracking.ipynb](examples/face_tracking.ipynb).
-        
-        ![](examples/tracked.gif)
-        
-        ### *Finetuning pretrained models with new data*
-        
-        In most situations, the best way to implement face recognition is to use the pretrained models directly, with either a clustering algorithm or a simple distance metrics to determine the identity of a face. However, if finetuning is required (i.e., if you want to select identity based on the model's output logits), an example can be found at [examples/finetune.ipynb](examples/finetune.ipynb).
-        
-        ### *Guide to MTCNN in facenet-pytorch*
-        
-        This guide demonstrates the functionality of the MTCNN module. Topics covered are:
-        
-        * Basic usage
-        * Image normalization
-        * Face margins
-        * Multiple faces in a single image
-        * Batched detection
-        * Bounding boxes and facial landmarks
-        * Saving face datasets
-        
-        See the [notebook on kaggle](https://www.kaggle.com/timesler/guide-to-mtcnn-in-facenet-pytorch).
-        
-        ### *Performance comparison of face detection packages*
-        
-        This notebook demonstrates the use of three face detection packages:
-        
-        1. facenet-pytorch
-        1. mtcnn
-        1. dlib
-        
-        Each package is tested for its speed in detecting the faces in a set of 300 images (all frames from one video), with GPU support enabled. Performance is based on Kaggle's P100 notebook kernel. Results are summarized below.
-        
-        |Package|FPS (1080x1920)|FPS (720x1280)|FPS (540x960)|
-        |---|---|---|---|
-        |facenet-pytorch|12.97|20.32|25.50|
-        |facenet-pytorch (non-batched)|9.75|14.81|19.68|
-        |dlib|3.80|8.39|14.53|
-        |mtcnn|3.04|5.70|8.23|
-        
-        ![](examples/performance-comparison.png)
-        
-        See the [notebook on kaggle](https://www.kaggle.com/timesler/comparison-of-face-detection-packages).
-        
-        ### *The FastMTCNN algorithm*
-        
-        This algorithm demonstrates how to achieve extremely efficient face detection specifically in videos, by taking advantage of similarities between adjacent frames.
-        
-        See the [notebook on kaggle](https://www.kaggle.com/timesler/fast-mtcnn-detector-55-fps-at-full-resolution).
-        
-        ## Running with docker
-        
-        The package and any of the example notebooks can be run with docker (or nvidia-docker) using:
-        
-        ```bash
-        docker run --rm -p 8888:8888
-            -v ./facenet-pytorch:/home/jovyan timesler/jupyter-dl-gpu \
-            -v <path to data>:/home/jovyan/data
-            pip install facenet-pytorch && jupyter lab 
-        ```
-        
-        Navigate to the examples/ directory and run any of the ipython notebooks.
-        
-        See [timesler/jupyter-dl-gpu](https://github.com/timesler/docker-jupyter-dl-gpu) for docker container details.
-        
-        ## Use this repo in your own git project
-        
-        To use this code in your own git repo, I recommend first adding this repo as a submodule. Note that the dash ('-') in the repo name should be removed when cloning as a submodule as it will break python when importing:
-        
-        `git submodule add https://github.com/timesler/facenet-pytorch.git facenet_pytorch`
-        
-        Alternatively, the code can be installed as a package using pip:
-        
-        `pip install facenet-pytorch`
-        
-        ## Conversion of parameters from Tensorflow to Pytorch
-        
-        See: [models/utils/tensorflow2pytorch.py](models/tensorflow2pytorch.py)
-        
-        Note that this functionality is not needed to use the models in this repo, which depend only on the saved pytorch `state_dict`'s. 
-        
-        Following instantiation of the pytorch model, each layer's weights were loaded from equivalent layers in the pretrained tensorflow models from [davidsandberg/facenet](https://github.com/davidsandberg/facenet).
-        
-        The equivalence of the outputs from the original tensorflow models and the pytorch-ported models have been tested and are identical:
-        
-        ---
-        
-        `>>> compare_model_outputs(mdl, sess, torch.randn(5, 160, 160, 3).detach())`
-        
-        ```
-        Passing test data through TF model
-        
-        tensor([[-0.0142,  0.0615,  0.0057,  ...,  0.0497,  0.0375, -0.0838],
-                [-0.0139,  0.0611,  0.0054,  ...,  0.0472,  0.0343, -0.0850],
-                [-0.0238,  0.0619,  0.0124,  ...,  0.0598,  0.0334, -0.0852],
-                [-0.0089,  0.0548,  0.0032,  ...,  0.0506,  0.0337, -0.0881],
-                [-0.0173,  0.0630, -0.0042,  ...,  0.0487,  0.0295, -0.0791]])
-        
-        Passing test data through PT model
-        
-        tensor([[-0.0142,  0.0615,  0.0057,  ...,  0.0497,  0.0375, -0.0838],
-                [-0.0139,  0.0611,  0.0054,  ...,  0.0472,  0.0343, -0.0850],
-                [-0.0238,  0.0619,  0.0124,  ...,  0.0598,  0.0334, -0.0852],
-                [-0.0089,  0.0548,  0.0032,  ...,  0.0506,  0.0337, -0.0881],
-                [-0.0173,  0.0630, -0.0042,  ...,  0.0487,  0.0295, -0.0791]],
-               grad_fn=<DivBackward0>)
-        
-        Distance 1.2874517096861382e-06
-        ```
-        
-        ---
-        
-        In order to re-run the conversion of tensorflow parameters into the pytorch model, ensure you clone this repo _with submodules_, as the davidsandberg/facenet repo is included as a submodule and parts of it are required for the conversion.
-        
-        ## References
-        
-        1. David Sandberg's facenet repo: [https://github.com/davidsandberg/facenet](https://github.com/davidsandberg/facenet)
-        
-        1. F. Schroff, D. Kalenichenko, J. Philbin. _FaceNet: A Unified Embedding for Face Recognition and Clustering_, arXiv:1503.03832, 2015. [PDF](https://arxiv.org/pdf/1503.03832)
-        
-        1. Q. Cao, L. Shen, W. Xie, O. M. Parkhi, A. Zisserman. _VGGFace2: A dataset for recognising face across pose and age_, International Conference on Automatic Face and Gesture Recognition, 2018. [PDF](http://www.robots.ox.ac.uk/~vgg/publications/2018/Cao18/cao18.pdf)
-        
-        1. D. Yi, Z. Lei, S. Liao and S. Z. Li. _CASIAWebface: Learning Face Representation from Scratch_, arXiv:1411.7923, 2014. [PDF](https://arxiv.org/pdf/1411.7923)
-        
-        1. K. Zhang, Z. Zhang, Z. Li and Y. Qiao. _Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks_, IEEE Signal Processing Letters, 2016. [PDF](https://kpzhang93.github.io/MTCNN_face_detection_alignment/paper/spl.pdf)
-        
-Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
+License-File: LICENSE.md
+
+# Face Recognition Using Pytorch 
+[![Downloads](https://pepy.tech/badge/facenet-pytorch)](https://pepy.tech/project/facenet-pytorch)
+
+[![Code Coverage](https://img.shields.io/codecov/c/github/timesler/facenet-pytorch.svg)](https://codecov.io/gh/timesler/facenet-pytorch)
+
+| Python | 3.10 | 3.9 | 3.8 |
+| :---: | :---: | :---: | :---: |
+| Status | [![Build Status](https://github.com/timesler/facenet-pytorch/actions/workflows/python-3.10.yml/badge.svg?branch=master)](https://github.com/timesler/facenet-pytorch/actions?query=workflow%3A%22Python+3.10%22+branch%3Amaster) | [![Build Status](https://github.com/timesler/facenet-pytorch/actions/workflows/python-3.9.yml/badge.svg?branch=master)](https://github.com/timesler/facenet-pytorch/actions?query=workflow%3A%22Python+3.9%22+branch%3Amaster) | [![Build Status](https://github.com/timesler/facenet-pytorch/actions/workflows/python-3.8.yml/badge.svg?branch=master)](https://github.com/timesler/facenet-pytorch/actions?query=workflow%3A%22Python+3.8%22+branch%3Amaster) |
+
+[![xscode](https://img.shields.io/badge/Available%20on-xs%3Acode-blue?style=?style=plastic&logo=appveyor&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAMAAACdt4HsAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF////////VXz1bAAAAAJ0Uk5T/wDltzBKAAAAlUlEQVR42uzXSwqAMAwE0Mn9L+3Ggtgkk35QwcnSJo9S+yGwM9DCooCbgn4YrJ4CIPUcQF7/XSBbx2TEz4sAZ2q1RAECBAiYBlCtvwN+KiYAlG7UDGj59MViT9hOwEqAhYCtAsUZvL6I6W8c2wcbd+LIWSCHSTeSAAECngN4xxIDSK9f4B9t377Wd7H5Nt7/Xz8eAgwAvesLRjYYPuUAAAAASUVORK5CYII=)](https://xscode.com/timesler/facenet-pytorch)
+
+This is a repository for Inception Resnet (V1) models in pytorch, pretrained on VGGFace2 and CASIA-Webface.
+
+Pytorch model weights were initialized using parameters ported from David Sandberg's [tensorflow facenet repo](https://github.com/davidsandberg/facenet).
+
+Also included in this repo is an efficient pytorch implementation of MTCNN for face detection prior to inference. These models are also pretrained. To our knowledge, this is the fastest MTCNN implementation available.
+
+## Table of contents
+
+* [Table of contents](#table-of-contents)
+* [Quick start](#quick-start)
+* [Pretrained models](#pretrained-models)
+* [Example notebooks](#example-notebooks)
+  + [*Complete detection and recognition pipeline*](#complete-detection-and-recognition-pipeline)
+  + [*Face tracking in video streams*](#face-tracking-in-video-streams)
+  + [*Finetuning pretrained models with new data*](#finetuning-pretrained-models-with-new-data)
+  + [*Guide to MTCNN in facenet-pytorch*](#guide-to-mtcnn-in-facenet-pytorch)
+  + [*Performance comparison of face detection packages*](#performance-comparison-of-face-detection-packages)
+  + [*The FastMTCNN algorithm*](#the-fastmtcnn-algorithm)
+* [Running with docker](#running-with-docker)
+* [Use this repo in your own git project](#use-this-repo-in-your-own-git-project)
+* [Conversion of parameters from Tensorflow to Pytorch](#conversion-of-parameters-from-tensorflow-to-pytorch)
+* [References](#references)
+
+## Quick start
+
+1. Install:
+    
+    ```bash
+    # With pip:
+    pip install facenet-pytorch
+    
+    # or clone this repo, removing the '-' to allow python imports:
+    git clone https://github.com/timesler/facenet-pytorch.git facenet_pytorch
+    
+    # or use a docker container (see https://github.com/timesler/docker-jupyter-dl-gpu):
+    docker run -it --rm timesler/jupyter-dl-gpu pip install facenet-pytorch && ipython
+    ```
+    
+1. In python, import facenet-pytorch and instantiate models:
+    
+    ```python
+    from facenet_pytorch import MTCNN, InceptionResnetV1
+    
+    # If required, create a face detection pipeline using MTCNN:
+    mtcnn = MTCNN(image_size=<image_size>, margin=<margin>)
+    
+    # Create an inception resnet (in eval mode):
+    resnet = InceptionResnetV1(pretrained='vggface2').eval()
+    ```
+    
+1. Process an image:
+    
+    ```python
+    from PIL import Image
+    
+    img = Image.open(<image path>)
+
+    # Get cropped and prewhitened image tensor
+    img_cropped = mtcnn(img, save_path=<optional save path>)
+
+    # Calculate embedding (unsqueeze to add batch dimension)
+    img_embedding = resnet(img_cropped.unsqueeze(0))
+
+    # Or, if using for VGGFace2 classification
+    resnet.classify = True
+    img_probs = resnet(img_cropped.unsqueeze(0))
+    ```
+
+See `help(MTCNN)` and `help(InceptionResnetV1)` for usage and implementation details.
+
+## Pretrained models
+
+See: [models/inception_resnet_v1.py](models/inception_resnet_v1.py)
+
+The following models have been ported to pytorch (with links to download pytorch state_dict's):
+
+|Model name|LFW accuracy (as listed [here](https://github.com/davidsandberg/facenet))|Training dataset|
+| :- | :-: | -: |
+|[20180408-102900](https://github.com/timesler/facenet-pytorch/releases/download/v2.2.9/20180408-102900-casia-webface.pt) (111MB)|0.9905|CASIA-Webface|
+|[20180402-114759](https://github.com/timesler/facenet-pytorch/releases/download/v2.2.9/20180402-114759-vggface2.pt) (107MB)|0.9965|VGGFace2|
+
+There is no need to manually download the pretrained state_dict's; they are downloaded automatically on model instantiation and cached for future use in the torch cache. To use an Inception Resnet (V1) model for facial recognition/identification in pytorch, use:
+
+```python
+from facenet_pytorch import InceptionResnetV1
+
+# For a model pretrained on VGGFace2
+model = InceptionResnetV1(pretrained='vggface2').eval()
+
+# For a model pretrained on CASIA-Webface
+model = InceptionResnetV1(pretrained='casia-webface').eval()
+
+# For an untrained model with 100 classes
+model = InceptionResnetV1(num_classes=100).eval()
+
+# For an untrained 1001-class classifier
+model = InceptionResnetV1(classify=True, num_classes=1001).eval()
+```
+
+Both pretrained models were trained on 160x160 px images, so will perform best if applied to images resized to this shape. For best results, images should also be cropped to the face using MTCNN (see below).
+
+By default, the above models will return 512-dimensional embeddings of images. To enable classification instead, either pass `classify=True` to the model constructor, or you can set the object attribute afterwards with `model.classify = True`. For VGGFace2, the pretrained model will output logit vectors of length 8631, and for CASIA-Webface logit vectors of length 10575.
+
+## Example notebooks
+
+### *Complete detection and recognition pipeline*
+
+Face recognition can be easily applied to raw images by first detecting faces using MTCNN before calculating embedding or probabilities using an Inception Resnet model. The example code at [examples/infer.ipynb](examples/infer.ipynb) provides a complete example pipeline utilizing datasets, dataloaders, and optional GPU processing.
+
+### *Face tracking in video streams*
+
+MTCNN can be used to build a face tracking system (using the `MTCNN.detect()` method). A full face tracking example can be found at [examples/face_tracking.ipynb](examples/face_tracking.ipynb).
+
+![](examples/tracked.gif)
+
+### *Finetuning pretrained models with new data*
+
+In most situations, the best way to implement face recognition is to use the pretrained models directly, with either a clustering algorithm or a simple distance metrics to determine the identity of a face. However, if finetuning is required (i.e., if you want to select identity based on the model's output logits), an example can be found at [examples/finetune.ipynb](examples/finetune.ipynb).
+
+### *Guide to MTCNN in facenet-pytorch*
+
+This guide demonstrates the functionality of the MTCNN module. Topics covered are:
+
+* Basic usage
+* Image normalization
+* Face margins
+* Multiple faces in a single image
+* Batched detection
+* Bounding boxes and facial landmarks
+* Saving face datasets
+
+See the [notebook on kaggle](https://www.kaggle.com/timesler/guide-to-mtcnn-in-facenet-pytorch).
+
+### *Performance comparison of face detection packages*
+
+This notebook demonstrates the use of three face detection packages:
+
+1. facenet-pytorch
+1. mtcnn
+1. dlib
+
+Each package is tested for its speed in detecting the faces in a set of 300 images (all frames from one video), with GPU support enabled. Performance is based on Kaggle's P100 notebook kernel. Results are summarized below.
+
+|Package|FPS (1080x1920)|FPS (720x1280)|FPS (540x960)|
+|---|---|---|---|
+|facenet-pytorch|12.97|20.32|25.50|
+|facenet-pytorch (non-batched)|9.75|14.81|19.68|
+|dlib|3.80|8.39|14.53|
+|mtcnn|3.04|5.70|8.23|
+
+![](examples/performance-comparison.png)
+
+See the [notebook on kaggle](https://www.kaggle.com/timesler/comparison-of-face-detection-packages).
+
+### *The FastMTCNN algorithm*
+
+This algorithm demonstrates how to achieve extremely efficient face detection specifically in videos, by taking advantage of similarities between adjacent frames.
+
+See the [notebook on kaggle](https://www.kaggle.com/timesler/fast-mtcnn-detector-55-fps-at-full-resolution).
+
+## Running with docker
+
+The package and any of the example notebooks can be run with docker (or nvidia-docker) using:
+
+```bash
+docker run --rm -p 8888:8888
+    -v ./facenet-pytorch:/home/jovyan timesler/jupyter-dl-gpu \
+    -v <path to data>:/home/jovyan/data
+    pip install facenet-pytorch && jupyter lab 
+```
+
+Navigate to the examples/ directory and run any of the ipython notebooks.
+
+See [timesler/jupyter-dl-gpu](https://github.com/timesler/docker-jupyter-dl-gpu) for docker container details.
+
+## Use this repo in your own git project
+
+To use this code in your own git repo, I recommend first adding this repo as a submodule. Note that the dash ('-') in the repo name should be removed when cloning as a submodule as it will break python when importing:
+
+`git submodule add https://github.com/timesler/facenet-pytorch.git facenet_pytorch`
+
+Alternatively, the code can be installed as a package using pip:
+
+`pip install facenet-pytorch`
+
+## Conversion of parameters from Tensorflow to Pytorch
+
+See: [models/utils/tensorflow2pytorch.py](models/tensorflow2pytorch.py)
+
+Note that this functionality is not needed to use the models in this repo, which depend only on the saved pytorch `state_dict`'s. 
+
+Following instantiation of the pytorch model, each layer's weights were loaded from equivalent layers in the pretrained tensorflow models from [davidsandberg/facenet](https://github.com/davidsandberg/facenet).
+
+The equivalence of the outputs from the original tensorflow models and the pytorch-ported models have been tested and are identical:
+
+---
+
+`>>> compare_model_outputs(mdl, sess, torch.randn(5, 160, 160, 3).detach())`
+
+```
+Passing test data through TF model
+
+tensor([[-0.0142,  0.0615,  0.0057,  ...,  0.0497,  0.0375, -0.0838],
+        [-0.0139,  0.0611,  0.0054,  ...,  0.0472,  0.0343, -0.0850],
+        [-0.0238,  0.0619,  0.0124,  ...,  0.0598,  0.0334, -0.0852],
+        [-0.0089,  0.0548,  0.0032,  ...,  0.0506,  0.0337, -0.0881],
+        [-0.0173,  0.0630, -0.0042,  ...,  0.0487,  0.0295, -0.0791]])
+
+Passing test data through PT model
+
+tensor([[-0.0142,  0.0615,  0.0057,  ...,  0.0497,  0.0375, -0.0838],
+        [-0.0139,  0.0611,  0.0054,  ...,  0.0472,  0.0343, -0.0850],
+        [-0.0238,  0.0619,  0.0124,  ...,  0.0598,  0.0334, -0.0852],
+        [-0.0089,  0.0548,  0.0032,  ...,  0.0506,  0.0337, -0.0881],
+        [-0.0173,  0.0630, -0.0042,  ...,  0.0487,  0.0295, -0.0791]],
+       grad_fn=<DivBackward0>)
+
+Distance 1.2874517096861382e-06
+```
+
+---
+
+In order to re-run the conversion of tensorflow parameters into the pytorch model, ensure you clone this repo _with submodules_, as the davidsandberg/facenet repo is included as a submodule and parts of it are required for the conversion.
+
+## References
+
+1. David Sandberg's facenet repo: [https://github.com/davidsandberg/facenet](https://github.com/davidsandberg/facenet)
+
+1. F. Schroff, D. Kalenichenko, J. Philbin. _FaceNet: A Unified Embedding for Face Recognition and Clustering_, arXiv:1503.03832, 2015. [PDF](https://arxiv.org/pdf/1503.03832)
+
+1. Q. Cao, L. Shen, W. Xie, O. M. Parkhi, A. Zisserman. _VGGFace2: A dataset for recognising face across pose and age_, International Conference on Automatic Face and Gesture Recognition, 2018. [PDF](http://www.robots.ox.ac.uk/~vgg/publications/2018/Cao18/cao18.pdf)
+
+1. D. Yi, Z. Lei, S. Liao and S. Z. Li. _CASIAWebface: Learning Face Representation from Scratch_, arXiv:1411.7923, 2014. [PDF](https://arxiv.org/pdf/1411.7923)
+
+1. K. Zhang, Z. Zhang, Z. Li and Y. Qiao. _Joint Face Detection and Alignment Using Multitask Cascaded Convolutional Networks_, IEEE Signal Processing Letters, 2016. [PDF](https://kpzhang93.github.io/MTCNN_face_detection_alignment/paper/spl.pdf)
```

### Comparing `facenet-pytorch-2.5.2/models/inception_resnet_v1.py` & `facenet-pytorch-2.5.3/models/inception_resnet_v1.py`

 * *Files identical despite different names*

### Comparing `facenet-pytorch-2.5.2/models/mtcnn.py` & `facenet-pytorch-2.5.3/models/mtcnn.py`

 * *Files 1% similar despite different names*

```diff
@@ -179,15 +179,15 @@
         select_largest {bool} -- If True, if multiple faces are detected, the largest is returned.
             If False, the face with the highest detection probability is returned.
             (default: {True})
         selection_method {string} -- Which heuristic to use for selection. Default None. If
             specified, will override select_largest:
                     "probability": highest probability selected
                     "largest": largest box selected
-                    "largest_over_theshold": largest box over a certain probability selected
+                    "largest_over_threshold": largest box over a certain probability selected
                     "center_weighted_size": box size minus weighted squared offset from image center
                 (default: {None})
         keep_all {bool} -- If True, all detected faces are returned, in the order dictated by the
             select_largest parameter. If a save_path is specified, the first face is saved to that
             path and the remaining faces are saved to <save_path>1, <save_path>2 etc.
             (default: {False})
         device {torch.device} -- The device on which to run neural net passes. Image tensors and
@@ -332,17 +332,17 @@
                 boxes.append(box[:, :4])
                 probs.append(box[:, 4])
                 points.append(point)
             else:
                 boxes.append(box[:, :4])
                 probs.append(box[:, 4])
                 points.append(point)
-        boxes = np.array(boxes)
-        probs = np.array(probs)
-        points = np.array(points)
+        boxes = np.array(boxes, dtype=object)
+        probs = np.array(probs, dtype=object)
+        points = np.array(points, dtype=object)
 
         if (
             not isinstance(img, (list, tuple)) and 
             not (isinstance(img, np.ndarray) and len(img.shape) == 4) and
             not (isinstance(img, torch.Tensor) and len(img.shape) == 4)
         ):
             boxes = boxes[0]
```

### Comparing `facenet-pytorch-2.5.2/models/utils/detect_face.py` & `facenet-pytorch-2.5.3/models/utils/detect_face.py`

 * *Files 1% similar despite different names*

```diff
@@ -176,15 +176,15 @@
     batch_boxes = []
     batch_points = []
     for b_i in range(batch_size):
         b_i_inds = np.where(image_inds == b_i)
         batch_boxes.append(boxes[b_i_inds].copy())
         batch_points.append(points[b_i_inds].copy())
 
-    batch_boxes, batch_points = np.array(batch_boxes), np.array(batch_points)
+    batch_boxes, batch_points = np.array(batch_boxes, dtype=object), np.array(batch_points, dtype=object)
 
     return batch_boxes, batch_points
 
 
 def bbreg(boundingbox, reg):
     if reg.shape[1] == 1:
         reg = torch.reshape(reg, (reg.shape[2], reg.shape[3]))
@@ -243,15 +243,15 @@
         xx2 = np.minimum(x2[i], x2[idx]).copy()
         yy2 = np.minimum(y2[i], y2[idx]).copy()
 
         w = np.maximum(0.0, xx2 - xx1 + 1).copy()
         h = np.maximum(0.0, yy2 - yy1 + 1).copy()
 
         inter = w * h
-        if method is "Min":
+        if method == 'Min':
             o = inter / np.minimum(area[i], area[idx])
         else:
             o = inter / (area[i] + area[idx] - inter)
         I = I[np.where(o <= threshold)]
 
     pick = pick[:counter].copy()
     return pick
```

### Comparing `facenet-pytorch-2.5.2/models/utils/download.py` & `facenet-pytorch-2.5.3/models/utils/download.py`

 * *Files identical despite different names*

### Comparing `facenet-pytorch-2.5.2/models/utils/tensorflow2pytorch.py` & `facenet-pytorch-2.5.3/models/utils/tensorflow2pytorch.py`

 * *Files identical despite different names*

### Comparing `facenet-pytorch-2.5.2/models/utils/training.py` & `facenet-pytorch-2.5.3/models/utils/training.py`

 * *Files identical despite different names*

### Comparing `facenet-pytorch-2.5.2/setup.py` & `facenet-pytorch-2.5.3/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,11 @@
 import setuptools, os
 
 PACKAGE_NAME = 'facenet-pytorch'
-VERSION = '2.5.2'
+VERSION = '2.5.3'
 AUTHOR = 'Tim Esler'
 EMAIL = 'tim.esler@gmail.com'
 DESCRIPTION = 'Pretrained Pytorch face detection and recognition models'
 GITHUB_URL = 'https://github.com/timesler/facenet-pytorch'
 
 parent_dir = os.path.dirname(os.path.realpath(__file__))
 import_name = os.path.basename(parent_dir)
```

