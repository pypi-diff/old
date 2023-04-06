# Comparing `tmp/mdai-0.9.0.tar.gz` & `tmp/mdai-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/mdai-0.9.0.tar", last modified: Fri Nov 19 21:01:33 2021, max compression
+gzip compressed data, was "dist/mdai-0.9.1.tar", last modified: Tue Jan 11 17:18:36 2022, max compression
```

## Comparing `mdai-0.9.0.tar` & `mdai-0.9.1.tar`

### file list

```diff
@@ -1,29 +1,29 @@
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-11-19 21:01:33.000000 mdai-0.9.0/
--rw-r--r--   0 circleci  (3434) circleci  (3434)    10756 2021-11-19 21:00:59.000000 mdai-0.9.0/LICENSE
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5604 2021-11-19 21:01:33.000000 mdai-0.9.0/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4541 2021-11-19 21:00:59.000000 mdai-0.9.0/README.md
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-11-19 21:01:33.000000 mdai-0.9.0/mdai/
--rwxr-xr-x   0 circleci  (3434) circleci  (3434)      331 2021-11-19 21:00:59.000000 mdai-0.9.0/mdai/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    24933 2021-11-19 21:00:59.000000 mdai-0.9.0/mdai/client.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    13523 2021-11-19 21:00:59.000000 mdai-0.9.0/mdai/preprocess.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-11-19 21:01:33.000000 mdai-0.9.0/mdai/utils/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-11-19 21:00:59.000000 mdai-0.9.0/mdai/utils/__init__.py
--rwxr-xr-x   0 circleci  (3434) circleci  (3434)    14143 2021-11-19 21:00:59.000000 mdai-0.9.0/mdai/utils/common_utils.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     2524 2021-11-19 21:00:59.000000 mdai-0.9.0/mdai/utils/keras_utils.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     4203 2021-11-19 21:00:59.000000 mdai-0.9.0/mdai/utils/tensorflow_utils.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     6704 2021-11-19 21:00:59.000000 mdai-0.9.0/mdai/utils/transforms.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)    12397 2021-11-19 21:00:59.000000 mdai-0.9.0/mdai/visualize.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-11-19 21:01:33.000000 mdai-0.9.0/mdai.egg-info/
--rw-r--r--   0 circleci  (3434) circleci  (3434)     5604 2021-11-19 21:01:33.000000 mdai-0.9.0/mdai.egg-info/PKG-INFO
--rw-r--r--   0 circleci  (3434) circleci  (3434)      466 2021-11-19 21:01:33.000000 mdai-0.9.0/mdai.egg-info/SOURCES.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2021-11-19 21:01:33.000000 mdai-0.9.0/mdai.egg-info/dependency_links.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)      115 2021-11-19 21:01:33.000000 mdai-0.9.0/mdai.egg-info/requires.txt
--rw-r--r--   0 circleci  (3434) circleci  (3434)       11 2021-11-19 21:01:33.000000 mdai-0.9.0/mdai.egg-info/top_level.txt
--rwxr-xr-x   0 circleci  (3434) circleci  (3434)      585 2021-11-19 21:00:59.000000 mdai-0.9.0/pyproject.toml
--rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2021-11-19 21:01:33.000000 mdai-0.9.0/setup.cfg
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1604 2021-11-19 21:00:59.000000 mdai-0.9.0/setup.py
-drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2021-11-19 21:01:33.000000 mdai-0.9.0/tests/
--rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2021-11-19 21:00:59.000000 mdai-0.9.0/tests/__init__.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1207 2021-11-19 21:00:59.000000 mdai-0.9.0/tests/conftest.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1761 2021-11-19 21:00:59.000000 mdai-0.9.0/tests/test_preprocess.py
--rw-r--r--   0 circleci  (3434) circleci  (3434)     1213 2021-11-19 21:00:59.000000 mdai-0.9.0/tests/test_visualize.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-01-11 17:18:36.000000 mdai-0.9.1/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    10756 2022-01-11 17:18:07.000000 mdai-0.9.1/LICENSE
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5604 2022-01-11 17:18:36.000000 mdai-0.9.1/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4541 2022-01-11 17:18:07.000000 mdai-0.9.1/README.md
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-01-11 17:18:36.000000 mdai-0.9.1/mdai/
+-rwxr-xr-x   0 circleci  (3434) circleci  (3434)      331 2022-01-11 17:18:07.000000 mdai-0.9.1/mdai/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    24933 2022-01-11 17:18:07.000000 mdai-0.9.1/mdai/client.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    13632 2022-01-11 17:18:07.000000 mdai-0.9.1/mdai/preprocess.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-01-11 17:18:36.000000 mdai-0.9.1/mdai/utils/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2022-01-11 17:18:07.000000 mdai-0.9.1/mdai/utils/__init__.py
+-rwxr-xr-x   0 circleci  (3434) circleci  (3434)    14633 2022-01-11 17:18:07.000000 mdai-0.9.1/mdai/utils/common_utils.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     2524 2022-01-11 17:18:07.000000 mdai-0.9.1/mdai/utils/keras_utils.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     4203 2022-01-11 17:18:07.000000 mdai-0.9.1/mdai/utils/tensorflow_utils.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5395 2022-01-11 17:18:07.000000 mdai-0.9.1/mdai/utils/transforms.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)    12397 2022-01-11 17:18:07.000000 mdai-0.9.1/mdai/visualize.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-01-11 17:18:36.000000 mdai-0.9.1/mdai.egg-info/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     5604 2022-01-11 17:18:35.000000 mdai-0.9.1/mdai.egg-info/PKG-INFO
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      466 2022-01-11 17:18:35.000000 mdai-0.9.1/mdai.egg-info/SOURCES.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        1 2022-01-11 17:18:35.000000 mdai-0.9.1/mdai.egg-info/dependency_links.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)      115 2022-01-11 17:18:35.000000 mdai-0.9.1/mdai.egg-info/requires.txt
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       11 2022-01-11 17:18:35.000000 mdai-0.9.1/mdai.egg-info/top_level.txt
+-rwxr-xr-x   0 circleci  (3434) circleci  (3434)      585 2022-01-11 17:18:07.000000 mdai-0.9.1/pyproject.toml
+-rw-r--r--   0 circleci  (3434) circleci  (3434)       38 2022-01-11 17:18:36.000000 mdai-0.9.1/setup.cfg
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1604 2022-01-11 17:18:07.000000 mdai-0.9.1/setup.py
+drwxr-xr-x   0 circleci  (3434) circleci  (3434)        0 2022-01-11 17:18:36.000000 mdai-0.9.1/tests/
+-rw-r--r--   0 circleci  (3434) circleci  (3434)        0 2022-01-11 17:18:07.000000 mdai-0.9.1/tests/__init__.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1207 2022-01-11 17:18:07.000000 mdai-0.9.1/tests/conftest.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1761 2022-01-11 17:18:07.000000 mdai-0.9.1/tests/test_preprocess.py
+-rw-r--r--   0 circleci  (3434) circleci  (3434)     1213 2022-01-11 17:18:07.000000 mdai-0.9.1/tests/test_visualize.py
```

### Comparing `mdai-0.9.0/LICENSE` & `mdai-0.9.1/LICENSE`

 * *Files 0% similar despite different names*

```diff
@@ -171,15 +171,15 @@
       of any other Contributor, and only if You agree to indemnify,
       defend, and hold each Contributor harmless for any liability
       incurred by, or claims asserted against, such Contributor by reason
       of your accepting any such warranty or additional liability.
 
    END OF TERMS AND CONDITIONS
 
-   Copyright 2020 MD.ai, Inc.
+   Copyright 2022 MD.ai, Inc.
 
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
 
        http://www.apache.org/licenses/LICENSE-2.0
```

### Comparing `mdai-0.9.0/PKG-INFO` & `mdai-0.9.1/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: mdai
-Version: 0.9.0
+Version: 0.9.1
 Summary: MD.ai Python client library
 Home-page: https://github.com/mdai/mdai-client-py
 Author: MD.ai
 Author-email: github@md.ai
 License: Apache-2.0
-Download-URL: https://github.com/mdai/mdai-client-py/tarball/0.9.0
+Download-URL: https://github.com/mdai/mdai-client-py/tarball/0.9.1
 Platform: UNKNOWN
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Education
 Classifier: Intended Audience :: Healthcare Industry
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: Apache Software License
@@ -92,10 +92,10 @@
 
 You can also run the notebook with powerful GPUs on the Google Cloud Platform. In this case, you need to authenticate to the Google Cloug Platform, create a private virtual machine instance running a Google's Deep Learning image, and import the lessons. See instructions below.
 
 [GCP Deep Learnings Images How To](running_on_gcp.md)
 
 ---
 
-&copy; 2020 MD.ai, Inc.
+&copy; 2022 MD.ai, Inc.
```

### Comparing `mdai-0.9.0/README.md` & `mdai-0.9.1/README.md`

 * *Files 0% similar despite different names*

```diff
@@ -66,8 +66,8 @@
 
 You can also run the notebook with powerful GPUs on the Google Cloud Platform. In this case, you need to authenticate to the Google Cloug Platform, create a private virtual machine instance running a Google's Deep Learning image, and import the lessons. See instructions below.
 
 [GCP Deep Learnings Images How To](running_on_gcp.md)
 
 ---
 
-&copy; 2020 MD.ai, Inc.
+&copy; 2022 MD.ai, Inc.
```

### Comparing `mdai-0.9.0/mdai/client.py` & `mdai-0.9.1/mdai/client.py`

 * *Files identical despite different names*

### Comparing `mdai-0.9.0/mdai/preprocess.py` & `mdai-0.9.1/mdai/preprocess.py`

 * *Files 1% similar despite different names*

```diff
@@ -221,14 +221,16 @@
         if self.classes_dict is None:
             raise Exception("Use `Project.set_labels_dict()` to set labels.")
 
         label_ids = self.classes_dict.keys()
 
         # filter annotations by label ids
         ann_filtered = self.get_annotations(label_ids)
+        if not ann_filtered:
+            raise Exception(f"No annotations exist for dataset '{self.name}'.")
 
         self.imgs_anns_dict = self._associate_images_and_annotations(ann_filtered)
 
     def get_annotations(self, label_ids=None, verbose=False):
         """Returns annotations, filtered by label ids.
 
         Args:
```

### Comparing `mdai-0.9.0/mdai/utils/common_utils.py` & `mdai-0.9.1/mdai/utils/common_utils.py`

 * *Files 5% similar despite different names*

```diff
@@ -40,29 +40,41 @@
     valid_image_ids = image_ids_list[split_index:]
 
     def filter_by_ids(ids, imgs_anns_dict):
         return {x: imgs_anns_dict[x] for x in ids}
 
     train_dataset = copy.deepcopy(dataset)
     train_dataset.id = dataset.id + "-TRAIN"
+    train_dataset.name = dataset.name + "-TRAIN"
 
     valid_dataset = copy.deepcopy(dataset)
     valid_dataset.id = dataset.id + "-VALID"
+    valid_dataset.name = dataset.name + "-VALID"
 
     imgs_anns_dict = dataset.imgs_anns_dict
 
     train_imgs_anns_dict = filter_by_ids(train_image_ids, imgs_anns_dict)
     valid_imgs_anns_dict = filter_by_ids(valid_image_ids, imgs_anns_dict)
 
     train_dataset.image_ids = train_image_ids
     valid_dataset.image_ids = valid_image_ids
 
     train_dataset.imgs_anns_dict = train_imgs_anns_dict
     valid_dataset.imgs_anns_dict = valid_imgs_anns_dict
 
+    all_train_annotations = []
+    for _, annotations in train_dataset.imgs_anns_dict.items():
+        all_train_annotations += annotations
+    train_dataset.all_annotations = all_train_annotations
+
+    all_val_annotations = []
+    for _, annotations in valid_dataset.imgs_anns_dict.items():
+        all_val_annotations += annotations
+    valid_dataset.all_annotations = all_val_annotations
+
     print(
         "Num of instances for training set: %d, validation set: %d"
         % (len(train_image_ids), len(valid_image_ids))
     )
     return train_dataset, valid_dataset
```

### Comparing `mdai-0.9.0/mdai/utils/keras_utils.py` & `mdai-0.9.1/mdai/utils/keras_utils.py`

 * *Files identical despite different names*

### Comparing `mdai-0.9.0/mdai/utils/tensorflow_utils.py` & `mdai-0.9.1/mdai/utils/tensorflow_utils.py`

 * *Files identical despite different names*

### Comparing `mdai-0.9.0/mdai/utils/transforms.py` & `mdai-0.9.1/mdai/utils/transforms.py`

 * *Files 16% similar despite different names*

```diff
@@ -3,48 +3,14 @@
 import numpy as np
 import dicom2nifti
 import pydicom
 
 DEFAULT_IMAGE_SIZE = (512.0, 512.0)
 
 
-def sort_dicoms(dicoms):
-    """
-    Sort the dicoms based on the image position patient.
-    Find most significant axis to use during sorting. The original way of sorting
-    (first x than y than z) does not work in certain border situations where for
-    exampe the X will only slightly change causing the values to remain equal on
-    multiple slices messing up the sorting completely.
-
-    @dicoms: list of dicoms
-    """
-
-    dicom_input_sorted_x = sorted(dicoms, key=lambda x: (x.ImagePositionPatient[0]))
-    dicom_input_sorted_y = sorted(dicoms, key=lambda x: (x.ImagePositionPatient[1]))
-    dicom_input_sorted_z = sorted(dicoms, key=lambda x: (x.ImagePositionPatient[2]))
-    diff_x = abs(
-        dicom_input_sorted_x[-1].ImagePositionPatient[0]
-        - dicom_input_sorted_x[0].ImagePositionPatient[0]
-    )
-    diff_y = abs(
-        dicom_input_sorted_y[-1].ImagePositionPatient[1]
-        - dicom_input_sorted_y[0].ImagePositionPatient[1]
-    )
-    diff_z = abs(
-        dicom_input_sorted_z[-1].ImagePositionPatient[2]
-        - dicom_input_sorted_z[0].ImagePositionPatient[2]
-    )
-    if diff_x >= diff_y and diff_x >= diff_z:
-        return dicom_input_sorted_x
-    if diff_y >= diff_x and diff_y >= diff_z:
-        return dicom_input_sorted_y
-    if diff_z >= diff_x and diff_z >= diff_y:
-        return dicom_input_sorted_z
-
-
 def apply_slope_intercept(dicom_file):
     """
     Applies rescale slope and rescale intercept transformation.
     """
     array = dicom_file.pixel_array.copy()
 
     scale_slope = 1
@@ -129,15 +95,15 @@
     Saves nifti in directory provided with filename as SeriesInstanceUID.nii.gz
     Returns a sorted list of dicom files based on image position patient.
     """
     output_file = os.path.join(tempdir, dicom_files[0].SeriesInstanceUID + ".nii.gz")
     nifti_file = dicom2nifti.convert_dicom.dicom_array_to_nifti(
         dicom_files, output_file=output_file, reorient_nifti=True,
     )
-    return sort_dicoms(dicom_files)
+    return dicom2nifti.common.sort_dicoms(dicom_files)
 
 
 def convert_dicom_to_8bit(dicom_file, imsize=None, width=None, level=None, keep_padding=True):
     """
     Given a DICOM file, window specifications, and image size,
     return the image as a Numpy array scaled to [0,255] of the specified size.
     """
@@ -192,15 +158,15 @@
 
 
 def stack_slices(dicom_files):
     """
     Stacks the +-1 slice to each slice in a dicom series.
     Returns the list of stacked images and sorted list of dicom files.
     """
-    dicom_files = sort_dicoms(dicom_files)
+    dicom_files = dicom2nifti.common.sort_dicoms(dicom_files)
     dicom_images = [load_dicom_array(i) for i in dicom_files]
 
     stacked_images = []
     for i, file in enumerate(dicom_images):
         if i == 0:
             img = np.stack([dicom_images[i], dicom_images[i], dicom_images[i + 1]], axis=-1)
             stacked_images.append(img)
```

### Comparing `mdai-0.9.0/mdai/visualize.py` & `mdai-0.9.1/mdai/visualize.py`

 * *Files identical despite different names*

### Comparing `mdai-0.9.0/mdai.egg-info/PKG-INFO` & `mdai-0.9.1/mdai.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 Metadata-Version: 2.1
 Name: mdai
-Version: 0.9.0
+Version: 0.9.1
 Summary: MD.ai Python client library
 Home-page: https://github.com/mdai/mdai-client-py
 Author: MD.ai
 Author-email: github@md.ai
 License: Apache-2.0
-Download-URL: https://github.com/mdai/mdai-client-py/tarball/0.9.0
+Download-URL: https://github.com/mdai/mdai-client-py/tarball/0.9.1
 Platform: UNKNOWN
 Classifier: Development Status :: 2 - Pre-Alpha
 Classifier: Intended Audience :: Developers
 Classifier: Intended Audience :: Education
 Classifier: Intended Audience :: Healthcare Industry
 Classifier: Intended Audience :: Science/Research
 Classifier: License :: OSI Approved :: Apache Software License
@@ -92,10 +92,10 @@
 
 You can also run the notebook with powerful GPUs on the Google Cloud Platform. In this case, you need to authenticate to the Google Cloug Platform, create a private virtual machine instance running a Google's Deep Learning image, and import the lessons. See instructions below.
 
 [GCP Deep Learnings Images How To](running_on_gcp.md)
 
 ---
 
-&copy; 2020 MD.ai, Inc.
+&copy; 2022 MD.ai, Inc.
```

### Comparing `mdai-0.9.0/pyproject.toml` & `mdai-0.9.1/pyproject.toml`

 * *Files identical despite different names*

### Comparing `mdai-0.9.0/setup.py` & `mdai-0.9.1/setup.py`

 * *Files identical despite different names*

### Comparing `mdai-0.9.0/tests/conftest.py` & `mdai-0.9.1/tests/conftest.py`

 * *Files identical despite different names*

### Comparing `mdai-0.9.0/tests/test_preprocess.py` & `mdai-0.9.1/tests/test_preprocess.py`

 * *Files identical despite different names*

### Comparing `mdai-0.9.0/tests/test_visualize.py` & `mdai-0.9.1/tests/test_visualize.py`

 * *Files identical despite different names*

