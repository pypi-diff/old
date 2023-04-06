# Comparing `tmp/metaseg-0.1.1.tar.gz` & `tmp/metaseg-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "metaseg-0.1.1.tar", last modified: Thu Apr  6 18:50:38 2023, max compression
+gzip compressed data, was "metaseg-0.1.2.tar", last modified: Thu Apr  6 19:00:41 2023, max compression
```

## Comparing `metaseg-0.1.1.tar` & `metaseg-0.1.2.tar`

### file list

```diff
@@ -1,34 +1,34 @@
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 18:50:38.702773 metaseg-0.1.1/
--rw-r--r--   0 kadir     (1000) kadir     (1001)    11357 2023-04-06 14:30:40.000000 metaseg-0.1.1/LICENSE
--rw-r--r--   0 kadir     (1000) kadir     (1001)       24 2023-04-06 14:34:00.000000 metaseg-0.1.1/MANIFEST.in
--rw-r--r--   0 kadir     (1000) kadir     (1001)      955 2023-04-06 18:50:38.702773 metaseg-0.1.1/PKG-INFO
--rw-r--r--   0 kadir     (1000) kadir     (1001)      681 2023-04-06 18:50:22.000000 metaseg-0.1.1/README.md
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 18:50:38.699440 metaseg-0.1.1/metaseg/
--rw-r--r--   0 kadir     (1000) kadir     (1001)      492 2023-04-06 18:50:33.000000 metaseg-0.1.1/metaseg/__init__.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)    15117 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/automatic_mask_generator.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     2936 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/build_sam.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     2001 2023-04-06 18:50:33.000000 metaseg-0.1.1/metaseg/demo.py
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 18:50:38.702773 metaseg-0.1.1/metaseg/modeling/
--rw-r--r--   0 kadir     (1000) kadir     (1001)      465 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/modeling/__init__.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     1479 2023-04-06 14:34:00.000000 metaseg-0.1.1/metaseg/modeling/common.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)    14341 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/modeling/image_encoder.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     6540 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/modeling/mask_decoder.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     8596 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/modeling/prompt_encoder.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     7273 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/modeling/sam.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     8332 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/modeling/transformer.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)    11570 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/predictor.py
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 18:50:38.702773 metaseg-0.1.1/metaseg/utils/
--rw-r--r--   0 kadir     (1000) kadir     (1001)      197 2023-04-06 14:34:00.000000 metaseg-0.1.1/metaseg/utils/__init__.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)    12621 2023-04-06 14:34:00.000000 metaseg-0.1.1/metaseg/utils/amg.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     5743 2023-04-06 14:36:47.000000 metaseg-0.1.1/metaseg/utils/onnx.py
--rw-r--r--   0 kadir     (1000) kadir     (1001)     3874 2023-04-06 14:34:00.000000 metaseg-0.1.1/metaseg/utils/transforms.py
-drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 18:50:38.699440 metaseg-0.1.1/metaseg.egg-info/
--rw-r--r--   0 kadir     (1000) kadir     (1001)      955 2023-04-06 18:50:38.000000 metaseg-0.1.1/metaseg.egg-info/PKG-INFO
--rw-r--r--   0 kadir     (1000) kadir     (1001)      659 2023-04-06 18:50:38.000000 metaseg-0.1.1/metaseg.egg-info/SOURCES.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)        1 2023-04-06 18:50:38.000000 metaseg-0.1.1/metaseg.egg-info/dependency_links.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)      212 2023-04-06 18:50:38.000000 metaseg-0.1.1/metaseg.egg-info/requires.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)        8 2023-04-06 18:50:38.000000 metaseg-0.1.1/metaseg.egg-info/top_level.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)       80 2023-04-06 14:34:00.000000 metaseg-0.1.1/pyproject.toml
--rw-r--r--   0 kadir     (1000) kadir     (1001)      125 2023-04-06 14:34:00.000000 metaseg-0.1.1/requirements.txt
--rw-r--r--   0 kadir     (1000) kadir     (1001)      430 2023-04-06 18:50:38.702773 metaseg-0.1.1/setup.cfg
--rw-r--r--   0 kadir     (1000) kadir     (1001)     1529 2023-04-06 14:36:43.000000 metaseg-0.1.1/setup.py
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.839425 metaseg-0.1.2/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    11357 2023-04-06 18:52:09.000000 metaseg-0.1.2/LICENSE
+-rw-r--r--   0 kadir     (1000) kadir     (1001)       24 2023-04-06 18:52:09.000000 metaseg-0.1.2/MANIFEST.in
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1041 2023-04-06 19:00:41.839425 metaseg-0.1.2/PKG-INFO
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      767 2023-04-06 18:59:07.000000 metaseg-0.1.2/README.md
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.832759 metaseg-0.1.2/metaseg/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      492 2023-04-06 19:00:39.000000 metaseg-0.1.2/metaseg/__init__.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    15117 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/automatic_mask_generator.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     2936 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/build_sam.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1832 2023-04-06 19:00:12.000000 metaseg-0.1.2/metaseg/demo.py
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.839425 metaseg-0.1.2/metaseg/modeling/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      465 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/__init__.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1479 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/common.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    14341 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/image_encoder.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     6540 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/mask_decoder.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     8596 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/prompt_encoder.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     7273 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/sam.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     8332 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/modeling/transformer.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    11570 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/predictor.py
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.839425 metaseg-0.1.2/metaseg/utils/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      197 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/utils/__init__.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)    12621 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/utils/amg.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     5743 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/utils/onnx.py
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     3874 2023-04-06 18:52:09.000000 metaseg-0.1.2/metaseg/utils/transforms.py
+drwxr-xr-x   0 kadir     (1000) kadir     (1001)        0 2023-04-06 19:00:41.832759 metaseg-0.1.2/metaseg.egg-info/
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1041 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/PKG-INFO
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      659 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/SOURCES.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)        1 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/dependency_links.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      212 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/requires.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)        8 2023-04-06 19:00:41.000000 metaseg-0.1.2/metaseg.egg-info/top_level.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)       80 2023-04-06 18:52:09.000000 metaseg-0.1.2/pyproject.toml
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      125 2023-04-06 18:52:09.000000 metaseg-0.1.2/requirements.txt
+-rw-r--r--   0 kadir     (1000) kadir     (1001)      430 2023-04-06 19:00:41.839425 metaseg-0.1.2/setup.cfg
+-rw-r--r--   0 kadir     (1000) kadir     (1001)     1529 2023-04-06 18:52:10.000000 metaseg-0.1.2/setup.py
```

### Comparing `metaseg-0.1.1/LICENSE` & `metaseg-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/PKG-INFO` & `metaseg-0.1.2/README.md`

 * *Files 27% similar despite different names*

```diff
@@ -1,25 +1,14 @@
-Metadata-Version: 2.1
-Name: metaseg
-Version: 0.1.1
-Home-page: https://github.com/kadirnar/segment-anything-pip
-Author: kadirnar
-License: Apache-2.0
-Requires-Python: >=3.8
-Description-Content-Type: text/markdown
-Provides-Extra: all
-Provides-Extra: dev
-License-File: LICENSE
-
 <div align="center">
 <h1>
-     MetaSeg: Packaged version of the Segment Anything repository
+     MetaSeg:Packaged version of the Segment Anything repository
 </h1>
 <div>
-    <a href="https://badge.fury.io/py/meta-segment"><img src="https://badge.fury.io/py/meta-segment.svg" alt="pypi version"></a>
+    <a href="https://pepy.tech/project/metaseg"><img src="https://pepy.tech/badge/metaseg" alt="downloads"></a>
+    <a href="https://badge.fury.io/py/metaseg"><img src="https://badge.fury.io/py/metaseg.svg" alt="pypi version"></a>
 </div>
 </div>
 
 This repo is a packaged version of the [segment-anything](https://github.com/facebookresearch/segment-anything) model.
 
 
 ### Installation
@@ -27,15 +16,14 @@
 pip install metaseg
 ```
 
 ### Usage
 ```python
 from metaseg import SegAutoMaskGenerator
 
-AutoMaskGenerator(
-    model_type="default",
-    checkpoint_path="sam_vit_h_4b8939.pth",
-    image_path="image.jpg", 
-    device="cuda", # or "cpu"
-    show=True, # show the image with the mask
-)
+SegAutoMaskGenerator(
+        model_type="default", 
+        checkpoint_path="sam_vit_h_4b8939.pth",
+        image_path= "test.png",
+        device="cuda",
+        show_mask=True, 
 ```
```

#### html2text {}

```diff
@@ -1,12 +1,8 @@
-Metadata-Version: 2.1 Name: metaseg Version: 0.1.1 Home-page: https://
-github.com/kadirnar/segment-anything-pip Author: kadirnar License: Apache-2.0
-Requires-Python: >=3.8 Description-Content-Type: text/markdown Provides-Extra:
-all Provides-Extra: dev License-File: LICENSE
-  ****** MetaSeg: Packaged version of the Segment Anything repository ******
-                                [pypi_version]
+   ****** MetaSeg:Packaged version of the Segment Anything repository ******
+                          [downloads] [pypi_version]
 This repo is a packaged version of the [segment-anything](https://github.com/
 facebookresearch/segment-anything) model. ### Installation ```bash pip install
 metaseg ``` ### Usage ```python from metaseg import SegAutoMaskGenerator
-AutoMaskGenerator( model_type="default",
-checkpoint_path="sam_vit_h_4b8939.pth", image_path="image.jpg", device="cuda",
-# or "cpu" show=True, # show the image with the mask ) ```
+SegAutoMaskGenerator( model_type="default",
+checkpoint_path="sam_vit_h_4b8939.pth", image_path= "test.png", device="cuda",
+show_mask=True, ```
```

### Comparing `metaseg-0.1.1/metaseg/automatic_mask_generator.py` & `metaseg-0.1.2/metaseg/automatic_mask_generator.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/build_sam.py` & `metaseg-0.1.2/metaseg/build_sam.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/demo.py` & `metaseg-0.1.2/metaseg/demo.py`

 * *Files 21% similar despite different names*

```diff
@@ -7,16 +7,18 @@
 
 class SegAutoMaskGenerator:
     def __init__(self, model_type, checkpoint_path, image_path, device, show_mask=True):
         self.model_type = model_type
         self.checkpoint_path = checkpoint_path
         self.device = device
         self.image_path = image_path
+
         if show_mask:
             self.show_mask()
+
         if self.model is None:
             self.model = self.load_model()
 
     def load_image(self):
         image = cv2.imread(self.image_path)
         image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
         return image
@@ -53,13 +55,7 @@
     def show_mask(self):
         image, masks = self.predict()
         plt.figure(figsize=(20, 20))
         plt.imshow(image)
         self.show_anns(masks)
         plt.axis("off")
         plt.show()
-
-
-if __name__ == "__main__":
-    model = SegAutoMaskGenerator(
-        "default", "sam_vit_h_4b8939.pth", "/content/drive/MyDrive/artgan/segment/datav2.png", "cuda"
-    )
```

### Comparing `metaseg-0.1.1/metaseg/modeling/common.py` & `metaseg-0.1.2/metaseg/modeling/common.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/modeling/image_encoder.py` & `metaseg-0.1.2/metaseg/modeling/image_encoder.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/modeling/mask_decoder.py` & `metaseg-0.1.2/metaseg/modeling/mask_decoder.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/modeling/prompt_encoder.py` & `metaseg-0.1.2/metaseg/modeling/prompt_encoder.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/modeling/sam.py` & `metaseg-0.1.2/metaseg/modeling/sam.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/modeling/transformer.py` & `metaseg-0.1.2/metaseg/modeling/transformer.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/predictor.py` & `metaseg-0.1.2/metaseg/predictor.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/utils/amg.py` & `metaseg-0.1.2/metaseg/utils/amg.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/utils/onnx.py` & `metaseg-0.1.2/metaseg/utils/onnx.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg/utils/transforms.py` & `metaseg-0.1.2/metaseg/utils/transforms.py`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/metaseg.egg-info/SOURCES.txt` & `metaseg-0.1.2/metaseg.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `metaseg-0.1.1/setup.py` & `metaseg-0.1.2/setup.py`

 * *Files identical despite different names*

