# Comparing `tmp/waffle_hub-0.1.3.tar.gz` & `tmp/waffle_hub-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "waffle_hub-0.1.3.tar", last modified: Wed Apr  5 07:22:10 2023, max compression
+gzip compressed data, was "waffle_hub-0.1.4.tar", last modified: Fri Apr  7 00:36:39 2023, max compression
```

## Comparing `waffle_hub-0.1.3.tar` & `waffle_hub-0.1.4.tar`

### file list

```diff
@@ -1,44 +1,44 @@
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)    35149 2023-03-20 23:40:26.000000 waffle_hub-0.1.3/LICENSE
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      138 2023-03-20 23:40:26.000000 waffle_hub-0.1.3/MANIFEST.in
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     1966 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/PKG-INFO
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      885 2023-04-03 23:38:22.000000 waffle_hub-0.1.3/README.md
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      213 2023-04-03 23:38:22.000000 waffle_hub-0.1.3/requirements.txt
--rw-rw-r--   0 lhj       (1002) lhj       (1003)       38 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/setup.cfg
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     2643 2023-04-03 23:38:22.000000 waffle_hub-0.1.3/setup.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/tests/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     5448 2023-04-05 07:21:49.000000 waffle_hub-0.1.3/tests/test_hub.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     2500 2023-04-05 07:21:49.000000 waffle_hub-0.1.3/waffle_hub/__init__.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub/hub/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-28 04:35:11.000000 waffle_hub-0.1.3/waffle_hub/hub/__init__.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub/hub/adapter/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-28 04:35:11.000000 waffle_hub-0.1.3/waffle_hub/hub/adapter/__init__.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)       63 2023-03-28 04:35:11.000000 waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/__init__.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/configs/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      129 2023-03-28 04:35:11.000000 waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/configs/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     2573 2023-03-28 04:35:11.000000 waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/configs/data_cfg.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     1865 2023-03-28 04:35:11.000000 waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/configs/model_cfg.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     8535 2023-04-03 23:38:22.000000 waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/tx_model_hub.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub/hub/adapter/ultralytics/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)       74 2023-03-28 04:35:11.000000 waffle_hub-0.1.3/waffle_hub/hub/adapter/ultralytics/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)    10278 2023-04-03 23:38:22.000000 waffle_hub-0.1.3/waffle_hub/hub/adapter/ultralytics/ultralytics_hub.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)    22021 2023-04-05 07:21:49.000000 waffle_hub-0.1.3/waffle_hub/hub/base_hub.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub/hub/model/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.3/waffle_hub/hub/model/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     5026 2023-04-03 23:38:22.000000 waffle_hub-0.1.3/waffle_hub/hub/model/wrapper.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     1247 2023-03-20 23:40:26.000000 waffle_hub-0.1.3/waffle_hub/run.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub/schemas/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.3/waffle_hub/schemas/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      679 2023-03-20 23:40:26.000000 waffle_hub-0.1.3/waffle_hub/schemas/configs.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub/utils/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.3/waffle_hub/utils/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     5252 2023-04-03 23:38:22.000000 waffle_hub-0.1.3/waffle_hub/utils/callback.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     5030 2023-04-03 23:38:22.000000 waffle_hub-0.1.3/waffle_hub/utils/image.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-05 07:22:10.225662 waffle_hub-0.1.3/waffle_hub.egg-info/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     1966 2023-04-05 07:22:10.000000 waffle_hub-0.1.3/waffle_hub.egg-info/PKG-INFO
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      932 2023-04-05 07:22:10.000000 waffle_hub-0.1.3/waffle_hub.egg-info/SOURCES.txt
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        1 2023-04-05 07:22:10.000000 waffle_hub-0.1.3/waffle_hub.egg-info/dependency_links.txt
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      172 2023-04-05 07:22:10.000000 waffle_hub-0.1.3/waffle_hub.egg-info/requires.txt
--rw-rw-r--   0 lhj       (1002) lhj       (1003)       11 2023-04-05 07:22:10.000000 waffle_hub-0.1.3/waffle_hub.egg-info/top_level.txt
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)    35149 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/LICENSE
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      138 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/MANIFEST.in
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     1966 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/PKG-INFO
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      885 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/README.md
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      213 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/requirements.txt
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)       38 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/setup.cfg
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     2643 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/setup.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/tests/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     5470 2023-04-07 00:35:34.000000 waffle_hub-0.1.4/tests/test_hub.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     2500 2023-04-07 00:35:47.000000 waffle_hub-0.1.4/waffle_hub/__init__.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/__init__.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/adapter/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/__init__.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)       63 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/__init__.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      129 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     2573 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/data_cfg.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     1865 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/model_cfg.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     8535 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/tx_model_hub.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/adapter/ultralytics/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)       74 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/ultralytics/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)    10566 2023-04-07 00:35:34.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/ultralytics/ultralytics_hub.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)    22021 2023-04-05 07:21:49.000000 waffle_hub-0.1.4/waffle_hub/hub/base_hub.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/model/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/hub/model/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     5026 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/waffle_hub/hub/model/wrapper.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     1247 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/run.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/schemas/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/schemas/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      679 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/schemas/configs.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/utils/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/utils/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     5252 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/waffle_hub/utils/callback.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     5030 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/waffle_hub/utils/image.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub.egg-info/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     1966 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/PKG-INFO
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      932 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/SOURCES.txt
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        1 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/dependency_links.txt
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      172 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/requires.txt
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)       11 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/top_level.txt
```

### Comparing `waffle_hub-0.1.3/LICENSE` & `waffle_hub-0.1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/PKG-INFO` & `waffle_hub-0.1.4/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: waffle_hub
-Version: 0.1.3
+Version: 0.1.4
 Summary: Waffle hub
 Home-page: https://github.com/snuailab/waffle_hub
 Author: SNUAILAB
 Author-email: huijae.lee@snuailab.ai
 License: GPL-3.0
 Project-URL: Bug Reports, https://github.com/snuailab/waffle_hub/issues
 Project-URL: Source, https://github.com/snuailab/waffle_hub
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: waffle_hub Version: 0.1.3 Summary: Waffle hub Home-
+Metadata-Version: 2.1 Name: waffle_hub Version: 0.1.4 Summary: Waffle hub Home-
 page: https://github.com/snuailab/waffle_hub Author: SNUAILAB Author-email:
 huijae.lee@snuailab.ai License: GPL-3.0 Project-URL: Bug Reports, https://
 github.com/snuailab/waffle_hub/issues Project-URL: Source, https://github.com/
 snuailab/waffle_hub Keywords: machine-learning,deep-
 learning,vision,ML,DL,AI,YOLO,Ultralytics,SNUAILAB Classifier: Development
 Status :: 3 - Alpha Classifier: Intended Audience :: Developers Classifier:
 Intended Audience :: Science/Research Classifier: License :: OSI Approved ::
```

### Comparing `waffle_hub-0.1.3/README.md` & `waffle_hub-0.1.4/README.md`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/setup.py` & `waffle_hub-0.1.4/setup.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/tests/test_hub.py` & `waffle_hub-0.1.4/tests/test_hub.py`

 * *Files 2% similar despite different names*

```diff
@@ -11,20 +11,20 @@
     InferenceCallback,
     TrainCallback,
 )
 
 
 @pytest.fixture
 def dummy_dataset(tmpdir: Path):
-    url = "https://github.com/snuailab/waffle_utils/raw/main/mnist.zip"
+    url = "https://raw.githubusercontent.com/snuailab/assets/main/waffle/sample_dataset/mnist.zip"
 
     dummy_zip_file = tmpdir / "mnist.zip"
     dummy_extract_dir = tmpdir / "extract"
-    dummy_coco_root_dir = tmpdir / "extract/raw"
-    dummy_coco_file = tmpdir / "extract/exports/coco.json"
+    dummy_coco_root_dir = tmpdir / "extract/images"
+    dummy_coco_file = tmpdir / "extract/coco.json"
 
     network.get_file_from_url(url, dummy_zip_file, create_directory=True)
     io.unzip(dummy_zip_file, dummy_extract_dir, create_directory=True)
 
     ds = Dataset.from_coco(
         "mnist", dummy_coco_file, Path(dummy_coco_root_dir), root_dir=tmpdir
     )
```

### Comparing `waffle_hub-0.1.3/waffle_hub/__init__.py` & `waffle_hub-0.1.4/waffle_hub/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-__version__ = "0.1.3"
+__version__ = "0.1.4"
 
 import importlib
 import warnings
 from collections import OrderedDict
 
 from tabulate import tabulate
```

### Comparing `waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/configs/data_cfg.py` & `waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/data_cfg.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/configs/model_cfg.py` & `waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/model_cfg.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/waffle_hub/hub/adapter/tx_model/tx_model_hub.py` & `waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/tx_model_hub.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/waffle_hub/hub/adapter/ultralytics/ultralytics_hub.py` & `waffle_hub-0.1.4/waffle_hub/hub/adapter/ultralytics/ultralytics_hub.py`

 * *Files 5% similar despite different names*

```diff
@@ -185,15 +185,15 @@
 
         with open(csv_path) as f:
             lines = f.readlines()
 
         header = lines[0].strip().split(",")
         metrics = []
         for line in lines[1:]:
-            values = line.strip().split(",")[1:]
+            values = line.strip().split(",")
             metric = []
             for i, value in enumerate(values):
                 metric.append(
                     {
                         "tag": header[i].strip(),
                         "value": float(value),
                     }
@@ -215,14 +215,24 @@
                     raise FileNotFoundError(
                         f"Ambiguous data file. Detected files: {yaml_files}"
                     )
                 ctx.dataset_path = Path(yaml_files[0]).absolute()
             else:
                 ctx.dataset_path = ctx.dataset_path.absolute()
         elif self.backend_task_name == "classify":
+
+            from torchvision.datasets.folder import ImageFolder
+
+            def find_classes(_, directory: str):
+                return directory, {
+                    v["name"]: i for i, v in enumerate(self.classes)
+                }
+
+            ImageFolder.find_classes = find_classes
+
             if not ctx.dataset_path.is_dir():
                 raise ValueError(
                     f"Classification dataset should be directory. Not {ctx.dataset_path}"
                 )
             ctx.dataset_path = ctx.dataset_path.absolute()
         ctx.dataset_path = str(ctx.dataset_path)
```

### Comparing `waffle_hub-0.1.3/waffle_hub/hub/base_hub.py` & `waffle_hub-0.1.4/waffle_hub/hub/base_hub.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/waffle_hub/hub/model/wrapper.py` & `waffle_hub-0.1.4/waffle_hub/hub/model/wrapper.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/waffle_hub/run.py` & `waffle_hub-0.1.4/waffle_hub/run.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/waffle_hub/schemas/configs.py` & `waffle_hub-0.1.4/waffle_hub/schemas/configs.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/waffle_hub/utils/callback.py` & `waffle_hub-0.1.4/waffle_hub/utils/callback.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/waffle_hub/utils/image.py` & `waffle_hub-0.1.4/waffle_hub/utils/image.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.3/waffle_hub.egg-info/PKG-INFO` & `waffle_hub-0.1.4/waffle_hub.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: waffle-hub
-Version: 0.1.3
+Version: 0.1.4
 Summary: Waffle hub
 Home-page: https://github.com/snuailab/waffle_hub
 Author: SNUAILAB
 Author-email: huijae.lee@snuailab.ai
 License: GPL-3.0
 Project-URL: Bug Reports, https://github.com/snuailab/waffle_hub/issues
 Project-URL: Source, https://github.com/snuailab/waffle_hub
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: waffle-hub Version: 0.1.3 Summary: Waffle hub Home-
+Metadata-Version: 2.1 Name: waffle-hub Version: 0.1.4 Summary: Waffle hub Home-
 page: https://github.com/snuailab/waffle_hub Author: SNUAILAB Author-email:
 huijae.lee@snuailab.ai License: GPL-3.0 Project-URL: Bug Reports, https://
 github.com/snuailab/waffle_hub/issues Project-URL: Source, https://github.com/
 snuailab/waffle_hub Keywords: machine-learning,deep-
 learning,vision,ML,DL,AI,YOLO,Ultralytics,SNUAILAB Classifier: Development
 Status :: 3 - Alpha Classifier: Intended Audience :: Developers Classifier:
 Intended Audience :: Science/Research Classifier: License :: OSI Approved ::
```

### Comparing `waffle_hub-0.1.3/waffle_hub.egg-info/SOURCES.txt` & `waffle_hub-0.1.4/waffle_hub.egg-info/SOURCES.txt`

 * *Files identical despite different names*

