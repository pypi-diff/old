# Comparing `tmp/image-trimmer-0.0.7.tar.gz` & `tmp/image-trimmer-0.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "image-trimmer-0.0.7.tar", last modified: Fri Apr  7 09:53:14 2023, max compression
+gzip compressed data, was "image-trimmer-0.0.8.tar", last modified: Fri Apr  7 09:54:49 2023, max compression
```

## Comparing `image-trimmer-0.0.7.tar` & `image-trimmer-0.0.8.tar`

### file list

```diff
@@ -1,14 +1,14 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 09:53:14.488046 image-trimmer-0.0.7/
--rw-rw-rw-   0        0        0      851 2023-04-07 09:53:14.487546 image-trimmer-0.0.7/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-07 09:53:14.472546 image-trimmer-0.0.7/image_trimmer/
--rw-rw-rw-   0        0        0        0 2023-04-07 07:37:37.000000 image-trimmer-0.0.7/image_trimmer/__init__.py
--rw-rw-rw-   0        0        0     3431 2023-04-07 09:53:03.000000 image-trimmer-0.0.7/image_trimmer/image_trimmer.py
-drwxrwxrwx   0        0        0        0 2023-04-07 09:53:14.486546 image-trimmer-0.0.7/image_trimmer.egg-info/
--rw-rw-rw-   0        0        0      851 2023-04-07 09:53:14.000000 image-trimmer-0.0.7/image_trimmer.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      289 2023-04-07 09:53:14.000000 image-trimmer-0.0.7/image_trimmer.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 09:53:14.000000 image-trimmer-0.0.7/image_trimmer.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       67 2023-04-07 09:53:14.000000 image-trimmer-0.0.7/image_trimmer.egg-info/entry_points.txt
--rw-rw-rw-   0        0        0       26 2023-04-07 09:53:14.000000 image-trimmer-0.0.7/image_trimmer.egg-info/requires.txt
--rw-rw-rw-   0        0        0       14 2023-04-07 09:53:14.000000 image-trimmer-0.0.7/image_trimmer.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-07 09:53:14.488545 image-trimmer-0.0.7/setup.cfg
--rw-rw-rw-   0        0        0      830 2023-04-07 09:53:10.000000 image-trimmer-0.0.7/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:54:49.461815 image-trimmer-0.0.8/
+-rw-rw-rw-   0        0        0      851 2023-04-07 09:54:49.461315 image-trimmer-0.0.8/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-07 09:54:49.446315 image-trimmer-0.0.8/image_trimmer/
+-rw-rw-rw-   0        0        0        0 2023-04-07 07:37:37.000000 image-trimmer-0.0.8/image_trimmer/__init__.py
+-rw-rw-rw-   0        0        0     3435 2023-04-07 09:54:42.000000 image-trimmer-0.0.8/image_trimmer/image_trimmer.py
+drwxrwxrwx   0        0        0        0 2023-04-07 09:54:49.459816 image-trimmer-0.0.8/image_trimmer.egg-info/
+-rw-rw-rw-   0        0        0      851 2023-04-07 09:54:49.000000 image-trimmer-0.0.8/image_trimmer.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      289 2023-04-07 09:54:49.000000 image-trimmer-0.0.8/image_trimmer.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 09:54:49.000000 image-trimmer-0.0.8/image_trimmer.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       67 2023-04-07 09:54:49.000000 image-trimmer-0.0.8/image_trimmer.egg-info/entry_points.txt
+-rw-rw-rw-   0        0        0       26 2023-04-07 09:54:49.000000 image-trimmer-0.0.8/image_trimmer.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       14 2023-04-07 09:54:49.000000 image-trimmer-0.0.8/image_trimmer.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 09:54:49.461815 image-trimmer-0.0.8/setup.cfg
+-rw-rw-rw-   0        0        0      830 2023-04-07 09:54:46.000000 image-trimmer-0.0.8/setup.py
```

### Comparing `image-trimmer-0.0.7/PKG-INFO` & `image-trimmer-0.0.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: image-trimmer
-Version: 0.0.7
+Version: 0.0.8
 Summary: A tool to crop images and extract text using OCR
 Home-page: https://github.com/jaytrairat/python-image-trimmer
 Author: jaytrairat
 Author-email: jaytrairat@outlook.com
 Classifier: Programming Language :: Python :: 3
 Description-Content-Type: text/markdown
```

### Comparing `image-trimmer-0.0.7/image_trimmer/image_trimmer.py` & `image-trimmer-0.0.8/image_trimmer/image_trimmer.py`

 * *Files 2% similar despite different names*

```diff
@@ -29,16 +29,16 @@
     return cropped_image, text
 
 
 def crop_images(input_folder, output_folder, template_name):
     name_list = []
     # Define the crop templates
     templates = {
-        "scb": {"x": 40, "y": 166, "width": 580, "height": 70},
-        "kbank": {"x": 0, "y": 135, "width": 745, "height": 75},
+        "scb": {"x": 270, "y": 570, "width": 420, "height": 135},
+        "kbank": {"x": 10, "y": 385, "width": 500, "height": 140},
     }
 
     # Check if the template exists
     if template_name not in templates:
         print(f"Error: template '{template_name}' not found, only supports: scb, kbank")
         return
```

### Comparing `image-trimmer-0.0.7/image_trimmer.egg-info/PKG-INFO` & `image-trimmer-0.0.8/image_trimmer.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: image-trimmer
-Version: 0.0.7
+Version: 0.0.8
 Summary: A tool to crop images and extract text using OCR
 Home-page: https://github.com/jaytrairat/python-image-trimmer
 Author: jaytrairat
 Author-email: jaytrairat@outlook.com
 Classifier: Programming Language :: Python :: 3
 Description-Content-Type: text/markdown
```

### Comparing `image-trimmer-0.0.7/setup.py` & `image-trimmer-0.0.8/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r", encoding="utf-8") as readme_file:
     readme = readme_file.read()
 
 setup(
     name="image-trimmer",
-    version="0.0.7",
+    version="0.0.8",
     packages=find_packages(),
     include_package_data=True,
     install_requires=[
         "pytesseract",
         "Pillow",
         "pyyaml",
     ],
```

