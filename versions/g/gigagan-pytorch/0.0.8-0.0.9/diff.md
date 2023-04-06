# Comparing `tmp/gigagan-pytorch-0.0.8.tar.gz` & `tmp/gigagan-pytorch-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gigagan-pytorch-0.0.8.tar", last modified: Tue Apr  4 20:05:03 2023, max compression
+gzip compressed data, was "gigagan-pytorch-0.0.9.tar", last modified: Tue Apr  4 20:08:13 2023, max compression
```

## Comparing `gigagan-pytorch-0.0.8.tar` & `gigagan-pytorch-0.0.9.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 20:05:03.855801 gigagan-pytorch-0.0.8/
--rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-04-04 20:04:48.000000 gigagan-pytorch-0.0.8/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      612 2023-04-04 20:05:03.855801 gigagan-pytorch-0.0.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2757 2023-04-04 20:04:48.000000 gigagan-pytorch-0.0.8/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 20:05:03.851801 gigagan-pytorch-0.0.8/gigagan_pytorch/
--rw-r--r--   0 runner    (1001) docker     (123)      117 2023-04-04 20:04:48.000000 gigagan-pytorch-0.0.8/gigagan_pytorch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    38186 2023-04-04 20:04:48.000000 gigagan-pytorch-0.0.8/gigagan_pytorch/gigagan_pytorch.py
--rw-r--r--   0 runner    (1001) docker     (123)     4262 2023-04-04 20:04:48.000000 gigagan-pytorch-0.0.8/gigagan_pytorch/open_clip.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 20:05:03.855801 gigagan-pytorch-0.0.8/gigagan_pytorch.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      612 2023-04-04 20:05:03.000000 gigagan-pytorch-0.0.8/gigagan_pytorch.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      312 2023-04-04 20:05:03.000000 gigagan-pytorch-0.0.8/gigagan_pytorch.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 20:05:03.000000 gigagan-pytorch-0.0.8/gigagan_pytorch.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-04 20:05:03.000000 gigagan-pytorch-0.0.8/gigagan_pytorch.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-04 20:05:03.000000 gigagan-pytorch-0.0.8/gigagan_pytorch.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-04 20:05:03.855801 gigagan-pytorch-0.0.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      890 2023-04-04 20:04:48.000000 gigagan-pytorch-0.0.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 20:08:13.908714 gigagan-pytorch-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-04-04 20:07:59.000000 gigagan-pytorch-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      612 2023-04-04 20:08:13.908714 gigagan-pytorch-0.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2757 2023-04-04 20:07:59.000000 gigagan-pytorch-0.0.9/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 20:08:13.908714 gigagan-pytorch-0.0.9/gigagan_pytorch/
+-rw-r--r--   0 runner    (1001) docker     (123)      117 2023-04-04 20:07:59.000000 gigagan-pytorch-0.0.9/gigagan_pytorch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    38254 2023-04-04 20:07:59.000000 gigagan-pytorch-0.0.9/gigagan_pytorch/gigagan_pytorch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4262 2023-04-04 20:07:59.000000 gigagan-pytorch-0.0.9/gigagan_pytorch/open_clip.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-04 20:08:13.908714 gigagan-pytorch-0.0.9/gigagan_pytorch.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      612 2023-04-04 20:08:13.000000 gigagan-pytorch-0.0.9/gigagan_pytorch.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      312 2023-04-04 20:08:13.000000 gigagan-pytorch-0.0.9/gigagan_pytorch.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-04 20:08:13.000000 gigagan-pytorch-0.0.9/gigagan_pytorch.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       85 2023-04-04 20:08:13.000000 gigagan-pytorch-0.0.9/gigagan_pytorch.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       16 2023-04-04 20:08:13.000000 gigagan-pytorch-0.0.9/gigagan_pytorch.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-04 20:08:13.908714 gigagan-pytorch-0.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      890 2023-04-04 20:07:59.000000 gigagan-pytorch-0.0.9/setup.py
```

### Comparing `gigagan-pytorch-0.0.8/LICENSE` & `gigagan-pytorch-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `gigagan-pytorch-0.0.8/PKG-INFO` & `gigagan-pytorch-0.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gigagan-pytorch
-Version: 0.0.8
+Version: 0.0.9
 Summary: GigaGAN - Pytorch
 Home-page: https://github.com/lucidrains/ETSformer-pytorch
 Author: Phil Wang
 Author-email: lucidrains@gmail.com
 License: MIT
 Keywords: artificial intelligence,deep learning,generative adversarial networks
 Classifier: Development Status :: 4 - Beta
```

### Comparing `gigagan-pytorch-0.0.8/README.md` & `gigagan-pytorch-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `gigagan-pytorch-0.0.8/gigagan_pytorch/gigagan_pytorch.py` & `gigagan-pytorch-0.0.9/gigagan_pytorch/gigagan_pytorch.py`

 * *Files 0% similar despite different names*

```diff
@@ -1076,14 +1076,15 @@
 
         assert max(multiscale_input_resolutions) > max(multiscale_output_resolutions)
         assert min(multiscale_input_resolutions) > min(multiscale_output_resolutions)
 
         self.multiscale_output_resolutions = multiscale_output_resolutions
 
         assert all([*map(is_power_of_two, aux_recon_resolutions)])
+        assert len(aux_recon_resolutions) == len(aux_recon_patches)
         self.aux_recon_resolutions_to_patches = {resolution: patches for resolution, patches in zip(aux_recon_resolutions, aux_recon_patches)}
 
         self.resize_mode = resize_mode
 
         num_layers = int(log2(image_size) - 1)
         self.num_layers = num_layers
```

### Comparing `gigagan-pytorch-0.0.8/gigagan_pytorch/open_clip.py` & `gigagan-pytorch-0.0.9/gigagan_pytorch/open_clip.py`

 * *Files identical despite different names*

### Comparing `gigagan-pytorch-0.0.8/gigagan_pytorch.egg-info/PKG-INFO` & `gigagan-pytorch-0.0.9/gigagan_pytorch.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gigagan-pytorch
-Version: 0.0.8
+Version: 0.0.9
 Summary: GigaGAN - Pytorch
 Home-page: https://github.com/lucidrains/ETSformer-pytorch
 Author: Phil Wang
 Author-email: lucidrains@gmail.com
 License: MIT
 Keywords: artificial intelligence,deep learning,generative adversarial networks
 Classifier: Development Status :: 4 - Beta
```

### Comparing `gigagan-pytorch-0.0.8/setup.py` & `gigagan-pytorch-0.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 
 setup(
   name = 'gigagan-pytorch',
   packages = find_packages(exclude=[]),
-  version = '0.0.8',
+  version = '0.0.9',
   license='MIT',
   description = 'GigaGAN - Pytorch',
   author = 'Phil Wang',
   author_email = 'lucidrains@gmail.com',
   long_description_content_type = 'text/markdown',
   url = 'https://github.com/lucidrains/ETSformer-pytorch',
   keywords = [
```

