# Comparing `tmp/metaseg-0.1.2.tar.gz` & `tmp/metaseg-0.1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "metaseg-0.1.2.tar", last modified: Thu Apr  6 19:00:41 2023, max compression
+gzip compressed data, was "metaseg-0.1.3.tar", last modified: Fri Apr  7 13:29:34 2023, max compression
```

## Comparing `metaseg-0.1.2.tar` & `metaseg-0.1.3.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.839425 metaseg-0.1.2/
--rw-r--r--   0 kadir     (1000) kadir     (1001)    11357 2023-04-06 18:52:09.000000 metaseg-0.1.2/LICENSE
--rw-r--r--   0 kadir     (1000) kadir     (1001)       24 2023-04-06 18:52:09.000000 metaseg-0.1.2/MANIFEST.in
--rw-r--r--   0 kadir     (1000) kadir     (1001)     1041 2023-04-06 19:00:41.839425 metaseg-0.1.2/PKG-INFO
--rw-r--r--   0 kadir     (1000) kadir     (1001)      767 2023-04-06 18:59:07.000000 metaseg-0.1.2/README.md
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.832759 metaseg-0.1.2/metaseg/
--rw-r--r--   0 kadir     (1000) kadir     (1001)      492 2023-04-06 19:00:39.000000 metaseg-0.1.2/metaseg/__init__.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)    15117 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/automatic_mask_generator.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     2936 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/build_sam.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     1832 2023-04-06 19:00:12.000000 metaseg-0.1.2/metaseg/demo.py
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.839425 metaseg-0.1.2/metaseg/modeling/
--rw-r--r--   0 kadir     (1000) kadir     (1001)      465 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/__init__.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     1479 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/common.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)    14341 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/image_encoder.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     6540 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/mask_decoder.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     8596 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/prompt_encoder.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     7273 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/sam.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     8332 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/transformer.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)    11570 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/predictor.py
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.839425 metaseg-0.1.2/metaseg/utils/
--rw-r--r--   0 kadir     (1000) kadir     (1001)      197 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/utils/__init__.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)    12621 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/utils/amg.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     5743 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/utils/onnx.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     3874 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/utils/transforms.py
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.832759 metaseg-0.1.2/metaseg.egg-info/
--rw-r--r--   0 kadir     (1000) kadir     (1001)     1041 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/PKG-INFO
--rw-r--r--   0 kadir     (1000) kadir     (1001)      659 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/SOURCES.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)        1 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/dependency_links.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)      212 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/requires.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)        8 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/top_level.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)       80 2023-04-06 18:52:09.000000 metaseg-0.1.2/pyproject.toml
--rw-r--r--   0 kadir     (1000) kadir     (1001)      125 2023-04-06 18:52:09.000000 metaseg-0.1.2/requirements.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)      430 2023-04-06 19:00:41.839425 metaseg-0.1.2/setup.cfg
--rw-r--r--   0 kadir     (1000) kadir     (1001)     1529 2023-04-06 18:52:10.000000 metaseg-0.1.2/setup.py
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-07 13:29:34.264477 metaseg-0.1.3/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    11357 2023-04-06 18:52:09.000000 metaseg-0.1.3/LICENSE
+-rw-r--r--   0 kadir     (1000) kadir     (1001)       24 2023-04-06 18:52:09.000000 metaseg-0.1.3/MANIFEST.in
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1066 2023-04-07 13:29:34.264477 metaseg-0.1.3/PKG-INFO
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      792 2023-04-07 13:27:02.000000 metaseg-0.1.3/README.md
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-07 13:29:34.257811 metaseg-0.1.3/metaseg/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      492 2023-04-07 13:29:03.000000 metaseg-0.1.3/metaseg/__init__.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    15117 2023-04-07 13:09:43.000000 metaseg-0.1.3/metaseg/automatic_mask_generator.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     2936 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/build_sam.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1839 2023-04-07 13:29:29.000000 metaseg-0.1.3/metaseg/demo.py
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-07 13:29:34.261144 metaseg-0.1.3/metaseg/modeling/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      465 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/modeling/__init__.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1479 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/modeling/common.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    14341 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/modeling/image_encoder.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     6540 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/modeling/mask_decoder.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     8596 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/modeling/prompt_encoder.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     7273 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/modeling/sam.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     8332 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/modeling/transformer.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    11570 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/predictor.py
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-07 13:29:34.264477 metaseg-0.1.3/metaseg/utils/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      197 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/utils/__init__.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    12621 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/utils/amg.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     5743 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/utils/onnx.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     3874 2023-04-06 18:52:09.000000 metaseg-0.1.3/metaseg/utils/transforms.py
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-07 13:29:34.261144 metaseg-0.1.3/metaseg.egg-info/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1066 2023-04-07 13:29:34.000000 metaseg-0.1.3/metaseg.egg-info/PKG-INFO
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      659 2023-04-07 13:29:34.000000 metaseg-0.1.3/metaseg.egg-info/SOURCES.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)        1 2023-04-07 13:29:34.000000 metaseg-0.1.3/metaseg.egg-info/dependency_links.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      212 2023-04-07 13:29:34.000000 metaseg-0.1.3/metaseg.egg-info/requires.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)        8 2023-04-07 13:29:34.000000 metaseg-0.1.3/metaseg.egg-info/top_level.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)       80 2023-04-06 18:52:09.000000 metaseg-0.1.3/pyproject.toml
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      125 2023-04-06 18:52:09.000000 metaseg-0.1.3/requirements.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      430 2023-04-07 13:29:34.264477 metaseg-0.1.3/setup.cfg
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1529 2023-04-06 18:52:10.000000 metaseg-0.1.3/setup.py
```

### Comparing `metaseg-0.1.2/LICENSE` & `metaseg-0.1.3/LICENSE`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/PKG-INFO` & `metaseg-0.1.3/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,27 +1,28 @@
 Metadata-Version: 2.1
 Name: metaseg
-Version: 0.1.2
+Version: 0.1.3
 Home-page: https://github.com/kadirnar/segment-anything-pip
 Author: kadirnar
 License: Apache-2.0
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 Provides-Extra: all
 Provides-Extra: dev
 License-File: LICENSE
 
 <div align="center">
-<h1>
-     MetaSeg:Packaged version of the Segment Anything repository
-</h1>
+<h2>
+     MetaSeg: Packaged version of the Segment Anything repository
+</h2>
 <div>
-    <a href="https://pepy.tech/project/metaseg"><img src="https://pepy.tech/badge/metaseg" alt="downloads"></a>
-    <a href="https://badge.fury.io/py/metaseg"><img src="https://badge.fury.io/py/metaseg.svg" alt="pypi version"></a>
+    <img width="1000" alt="teaser" src="https://github.com/kadirnar/segment-anything-pip/releases/download/v0.1.2/metaseg_demo.png">
 </div>
+    <a href="https://badge.fury.io/py/metaseg"><img src="https://badge.fury.io/py/metaseg.svg" alt="pypi version"></a>
+
 </div>
 
 This repo is a packaged version of the [segment-anything](https://github.com/facebookresearch/segment-anything) model.
 
 
 ### Installation
 ```bash
@@ -34,8 +35,9 @@
 
 SegAutoMaskGenerator(
         model_type="default", 
         checkpoint_path="sam_vit_h_4b8939.pth",
         image_path= "test.png",
         device="cuda",
         show_mask=True, 
+)
 ```
```

#### html2text {}

```diff
@@ -1,12 +1,13 @@
-Metadata-Version: 2.1 Name: metaseg Version: 0.1.2 Home-page: https://
+Metadata-Version: 2.1 Name: metaseg Version: 0.1.3 Home-page: https://
 github.com/kadirnar/segment-anything-pip Author: kadirnar License: Apache-2.0
 Requires-Python: >=3.8 Description-Content-Type: text/markdown Provides-Extra:
 all Provides-Extra: dev License-File: LICENSE
-   ****** MetaSeg:Packaged version of the Segment Anything repository ******
-                          [downloads] [pypi_version]
+   ***** MetaSeg: Packaged version of the Segment Anything repository *****
+                                   [teaser]
+                                [pypi_version]
 This repo is a packaged version of the [segment-anything](https://github.com/
 facebookresearch/segment-anything) model. ### Installation ```bash pip install
 metaseg ``` ### Usage ```python from metaseg import SegAutoMaskGenerator
 SegAutoMaskGenerator( model_type="default",
 checkpoint_path="sam_vit_h_4b8939.pth", image_path= "test.png", device="cuda",
-show_mask=True, ```
+show_mask=True, ) ```
```

### Comparing `metaseg-0.1.2/README.md` & `metaseg-0.1.3/README.md`

 * *Files 13% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 <div align="center">
-<h1>
-     MetaSeg:Packaged version of the Segment Anything repository
-</h1>
+<h2>
+     MetaSeg: Packaged version of the Segment Anything repository
+</h2>
 <div>
-    <a href="https://pepy.tech/project/metaseg"><img src="https://pepy.tech/badge/metaseg" alt="downloads"></a>
-    <a href="https://badge.fury.io/py/metaseg"><img src="https://badge.fury.io/py/metaseg.svg" alt="pypi version"></a>
+    <img width="1000" alt="teaser" src="https://github.com/kadirnar/segment-anything-pip/releases/download/v0.1.2/metaseg_demo.png">
 </div>
+    <a href="https://badge.fury.io/py/metaseg"><img src="https://badge.fury.io/py/metaseg.svg" alt="pypi version"></a>
+
 </div>
 
 This repo is a packaged version of the [segment-anything](https://github.com/facebookresearch/segment-anything) model.
 
 
 ### Installation
 ```bash
@@ -22,8 +23,9 @@
 
 SegAutoMaskGenerator(
         model_type="default", 
         checkpoint_path="sam_vit_h_4b8939.pth",
         image_path= "test.png",
         device="cuda",
         show_mask=True, 
+)
 ```
```

#### html2text {}

```diff
@@ -1,8 +1,9 @@
-   ****** MetaSeg:Packaged version of the Segment Anything repository ******
-                          [downloads] [pypi_version]
+   ***** MetaSeg: Packaged version of the Segment Anything repository *****
+                                   [teaser]
+                                [pypi_version]
 This repo is a packaged version of the [segment-anything](https://github.com/
 facebookresearch/segment-anything) model. ### Installation ```bash pip install
 metaseg ``` ### Usage ```python from metaseg import SegAutoMaskGenerator
 SegAutoMaskGenerator( model_type="default",
 checkpoint_path="sam_vit_h_4b8939.pth", image_path= "test.png", device="cuda",
-show_mask=True, ```
+show_mask=True, ) ```
```

### Comparing `metaseg-0.1.2/metaseg/automatic_mask_generator.py` & `metaseg-0.1.3/metaseg/automatic_mask_generator.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/build_sam.py` & `metaseg-0.1.3/metaseg/build_sam.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/demo.py` & `metaseg-0.1.3/metaseg/demo.py`

 * *Files 18% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 import cv2
+import gradio as gr
 import matplotlib.pyplot as plt
 import numpy as np
 
 from metaseg import SamAutomaticMaskGenerator, sam_model_registry
 
 
 class SegAutoMaskGenerator:
@@ -22,40 +23,40 @@
         image = cv2.imread(self.image_path)
         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
         return image
 
     def load_model(self):
         model = sam_model_registry[self.model_type](checkpoint=self.checkpoint_path)
         model.to(device=self.device)
+        self.model = model
+
         return model
 
+    def predict(self):
+        model = self.load_model()
+        image = self.load_image()
+        mask_generator = SamAutomaticMaskGenerator(model)
+        masks = mask_generator.generate(image)
+
+        return image, masks
+
     def show_anns(self, anns):
         if len(anns) == 0:
             return
         sorted_anns = sorted(anns, key=(lambda x: x["area"]), reverse=True)
         ax = plt.gca()
         ax.set_autoscale_on(False)
-        polygons = []
-        color = []
         for ann in sorted_anns:
             m = ann["segmentation"]
             img = np.ones((m.shape[0], m.shape[1], 3))
             color_mask = np.random.random((1, 3)).tolist()[0]
             for i in range(3):
                 img[:, :, i] = color_mask[i]
             ax.imshow(np.dstack((img, m * 0.35)))
 
-    def predict(self):
-        model = self.load_model()
-        image = self.load_image()
-        mask_generator = SamAutomaticMaskGenerator(model)
-        masks = mask_generator.generate(image)
-
-        return image, masks
-
     def show_mask(self):
         image, masks = self.predict()
         plt.figure(figsize=(20, 20))
         plt.imshow(image)
         self.show_anns(masks)
         plt.axis("off")
         plt.show()
```

### Comparing `metaseg-0.1.2/metaseg/modeling/common.py` & `metaseg-0.1.3/metaseg/modeling/common.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/modeling/image_encoder.py` & `metaseg-0.1.3/metaseg/modeling/image_encoder.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/modeling/mask_decoder.py` & `metaseg-0.1.3/metaseg/modeling/mask_decoder.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/modeling/prompt_encoder.py` & `metaseg-0.1.3/metaseg/modeling/prompt_encoder.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/modeling/sam.py` & `metaseg-0.1.3/metaseg/modeling/sam.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/modeling/transformer.py` & `metaseg-0.1.3/metaseg/modeling/transformer.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/predictor.py` & `metaseg-0.1.3/metaseg/predictor.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/utils/amg.py` & `metaseg-0.1.3/metaseg/utils/amg.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/utils/onnx.py` & `metaseg-0.1.3/metaseg/utils/onnx.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg/utils/transforms.py` & `metaseg-0.1.3/metaseg/utils/transforms.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/metaseg.egg-info/PKG-INFO` & `metaseg-0.1.3/metaseg.egg-info/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,27 +1,28 @@
 Metadata-Version: 2.1
 Name: metaseg
-Version: 0.1.2
+Version: 0.1.3
 Home-page: https://github.com/kadirnar/segment-anything-pip
 Author: kadirnar
 License: Apache-2.0
 Requires-Python: >=3.8
 Description-Content-Type: text/markdown
 Provides-Extra: all
 Provides-Extra: dev
 License-File: LICENSE
 
 <div align="center">
-<h1>
-     MetaSeg:Packaged version of the Segment Anything repository
-</h1>
+<h2>
+     MetaSeg: Packaged version of the Segment Anything repository
+</h2>
 <div>
-    <a href="https://pepy.tech/project/metaseg"><img src="https://pepy.tech/badge/metaseg" alt="downloads"></a>
-    <a href="https://badge.fury.io/py/metaseg"><img src="https://badge.fury.io/py/metaseg.svg" alt="pypi version"></a>
+    <img width="1000" alt="teaser" src="https://github.com/kadirnar/segment-anything-pip/releases/download/v0.1.2/metaseg_demo.png">
 </div>
+    <a href="https://badge.fury.io/py/metaseg"><img src="https://badge.fury.io/py/metaseg.svg" alt="pypi version"></a>
+
 </div>
 
 This repo is a packaged version of the [segment-anything](https://github.com/facebookresearch/segment-anything) model.
 
 
 ### Installation
 ```bash
@@ -34,8 +35,9 @@
 
 SegAutoMaskGenerator(
         model_type="default", 
         checkpoint_path="sam_vit_h_4b8939.pth",
         image_path= "test.png",
         device="cuda",
         show_mask=True, 
+)
 ```
```

#### html2text {}

```diff
@@ -1,12 +1,13 @@
-Metadata-Version: 2.1 Name: metaseg Version: 0.1.2 Home-page: https://
+Metadata-Version: 2.1 Name: metaseg Version: 0.1.3 Home-page: https://
 github.com/kadirnar/segment-anything-pip Author: kadirnar License: Apache-2.0
 Requires-Python: >=3.8 Description-Content-Type: text/markdown Provides-Extra:
 all Provides-Extra: dev License-File: LICENSE
-   ****** MetaSeg:Packaged version of the Segment Anything repository ******
-                          [downloads] [pypi_version]
+   ***** MetaSeg: Packaged version of the Segment Anything repository *****
+                                   [teaser]
+                                [pypi_version]
 This repo is a packaged version of the [segment-anything](https://github.com/
 facebookresearch/segment-anything) model. ### Installation ```bash pip install
 metaseg ``` ### Usage ```python from metaseg import SegAutoMaskGenerator
 SegAutoMaskGenerator( model_type="default",
 checkpoint_path="sam_vit_h_4b8939.pth", image_path= "test.png", device="cuda",
-show_mask=True, ```
+show_mask=True, ) ```
```

### Comparing `metaseg-0.1.2/metaseg.egg-info/SOURCES.txt` & `metaseg-0.1.3/metaseg.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.2/setup.py` & `metaseg-0.1.3/setup.py`

 * *Files identical despite different names*

