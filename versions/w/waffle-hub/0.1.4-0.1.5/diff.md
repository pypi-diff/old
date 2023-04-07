# Comparing `tmp/waffle_hub-0.1.4.tar.gz` & `tmp/waffle_hub-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "waffle_hub-0.1.4.tar", last modified: Fri Apr  7 00:36:39 2023, max compression
+gzip compressed data, was "waffle_hub-0.1.5.tar", last modified: Fri Apr  7 03:37:16 2023, max compression
```

## Comparing `waffle_hub-0.1.4.tar` & `waffle_hub-0.1.5.tar`

### file list

```diff
@@ -1,44 +1,44 @@
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)    35149 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/LICENSE
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      138 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/MANIFEST.in
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     1966 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/PKG-INFO
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      885 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/README.md
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      213 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/requirements.txt
--rw-rw-r--   0 lhj       (1002) lhj       (1003)       38 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/setup.cfg
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     2643 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/setup.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/tests/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     5470 2023-04-07 00:35:34.000000 waffle_hub-0.1.4/tests/test_hub.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     2500 2023-04-07 00:35:47.000000 waffle_hub-0.1.4/waffle_hub/__init__.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/__init__.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/adapter/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/__init__.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)       63 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/__init__.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      129 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     2573 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/data_cfg.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     1865 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/model_cfg.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     8535 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/tx_model_hub.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/adapter/ultralytics/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)       74 2023-03-28 04:35:11.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/ultralytics/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)    10566 2023-04-07 00:35:34.000000 waffle_hub-0.1.4/waffle_hub/hub/adapter/ultralytics/ultralytics_hub.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)    22021 2023-04-05 07:21:49.000000 waffle_hub-0.1.4/waffle_hub/hub/base_hub.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/hub/model/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/hub/model/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     5026 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/waffle_hub/hub/model/wrapper.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     1247 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/run.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/schemas/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/schemas/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      679 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/schemas/configs.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub/utils/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.4/waffle_hub/utils/__init__.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     5252 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/waffle_hub/utils/callback.py
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     5030 2023-04-03 23:38:22.000000 waffle_hub-0.1.4/waffle_hub/utils/image.py
-drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 00:36:39.731414 waffle_hub-0.1.4/waffle_hub.egg-info/
--rw-rw-r--   0 lhj       (1002) lhj       (1003)     1966 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/PKG-INFO
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      932 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/SOURCES.txt
--rw-rw-r--   0 lhj       (1002) lhj       (1003)        1 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/dependency_links.txt
--rw-rw-r--   0 lhj       (1002) lhj       (1003)      172 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/requires.txt
--rw-rw-r--   0 lhj       (1002) lhj       (1003)       11 2023-04-07 00:36:39.000000 waffle_hub-0.1.4/waffle_hub.egg-info/top_level.txt
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.645641 waffle_hub-0.1.5/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)    35149 2023-03-20 23:40:26.000000 waffle_hub-0.1.5/LICENSE
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      138 2023-03-20 23:40:26.000000 waffle_hub-0.1.5/MANIFEST.in
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     1966 2023-04-07 03:37:16.645641 waffle_hub-0.1.5/PKG-INFO
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      885 2023-04-03 23:38:22.000000 waffle_hub-0.1.5/README.md
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      213 2023-04-03 23:38:22.000000 waffle_hub-0.1.5/requirements.txt
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)       38 2023-04-07 03:37:16.645641 waffle_hub-0.1.5/setup.cfg
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     2643 2023-04-03 23:38:22.000000 waffle_hub-0.1.5/setup.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/tests/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     5470 2023-04-07 00:35:34.000000 waffle_hub-0.1.5/tests/test_hub.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/waffle_hub/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     2500 2023-04-07 03:36:43.000000 waffle_hub-0.1.5/waffle_hub/__init__.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/waffle_hub/hub/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-28 04:35:11.000000 waffle_hub-0.1.5/waffle_hub/hub/__init__.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/waffle_hub/hub/adapter/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-28 04:35:11.000000 waffle_hub-0.1.5/waffle_hub/hub/adapter/__init__.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)       63 2023-03-28 04:35:11.000000 waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/__init__.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/configs/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      129 2023-03-28 04:35:11.000000 waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/configs/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     2573 2023-03-28 04:35:11.000000 waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/configs/data_cfg.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     1865 2023-03-28 04:35:11.000000 waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/configs/model_cfg.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     8535 2023-04-03 23:38:22.000000 waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/tx_model_hub.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/waffle_hub/hub/adapter/ultralytics/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)       74 2023-03-28 04:35:11.000000 waffle_hub-0.1.5/waffle_hub/hub/adapter/ultralytics/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)    10566 2023-04-07 00:35:34.000000 waffle_hub-0.1.5/waffle_hub/hub/adapter/ultralytics/ultralytics_hub.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)    22096 2023-04-07 03:36:43.000000 waffle_hub-0.1.5/waffle_hub/hub/base_hub.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/waffle_hub/hub/model/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.5/waffle_hub/hub/model/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     5026 2023-04-03 23:38:22.000000 waffle_hub-0.1.5/waffle_hub/hub/model/wrapper.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     1247 2023-03-20 23:40:26.000000 waffle_hub-0.1.5/waffle_hub/run.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/waffle_hub/schemas/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.5/waffle_hub/schemas/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      679 2023-03-20 23:40:26.000000 waffle_hub-0.1.5/waffle_hub/schemas/configs.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.645641 waffle_hub-0.1.5/waffle_hub/utils/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        0 2023-03-20 23:40:26.000000 waffle_hub-0.1.5/waffle_hub/utils/__init__.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     5252 2023-04-03 23:38:22.000000 waffle_hub-0.1.5/waffle_hub/utils/callback.py
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     5030 2023-04-03 23:38:22.000000 waffle_hub-0.1.5/waffle_hub/utils/image.py
+drwxrwxr-x   0 lhj       (1002) lhj       (1003)        0 2023-04-07 03:37:16.641641 waffle_hub-0.1.5/waffle_hub.egg-info/
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)     1966 2023-04-07 03:37:16.000000 waffle_hub-0.1.5/waffle_hub.egg-info/PKG-INFO
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      932 2023-04-07 03:37:16.000000 waffle_hub-0.1.5/waffle_hub.egg-info/SOURCES.txt
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)        1 2023-04-07 03:37:16.000000 waffle_hub-0.1.5/waffle_hub.egg-info/dependency_links.txt
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)      172 2023-04-07 03:37:16.000000 waffle_hub-0.1.5/waffle_hub.egg-info/requires.txt
+-rw-rw-r--   0 lhj       (1002) lhj       (1003)       11 2023-04-07 03:37:16.000000 waffle_hub-0.1.5/waffle_hub.egg-info/top_level.txt
```

### Comparing `waffle_hub-0.1.4/LICENSE` & `waffle_hub-0.1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/PKG-INFO` & `waffle_hub-0.1.5/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: waffle_hub
-Version: 0.1.4
+Version: 0.1.5
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
-Metadata-Version: 2.1 Name: waffle_hub Version: 0.1.4 Summary: Waffle hub Home-
+Metadata-Version: 2.1 Name: waffle_hub Version: 0.1.5 Summary: Waffle hub Home-
 page: https://github.com/snuailab/waffle_hub Author: SNUAILAB Author-email:
 huijae.lee@snuailab.ai License: GPL-3.0 Project-URL: Bug Reports, https://
 github.com/snuailab/waffle_hub/issues Project-URL: Source, https://github.com/
 snuailab/waffle_hub Keywords: machine-learning,deep-
 learning,vision,ML,DL,AI,YOLO,Ultralytics,SNUAILAB Classifier: Development
 Status :: 3 - Alpha Classifier: Intended Audience :: Developers Classifier:
 Intended Audience :: Science/Research Classifier: License :: OSI Approved ::
```

### Comparing `waffle_hub-0.1.4/README.md` & `waffle_hub-0.1.5/README.md`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/setup.py` & `waffle_hub-0.1.5/setup.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/tests/test_hub.py` & `waffle_hub-0.1.5/tests/test_hub.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub/__init__.py` & `waffle_hub-0.1.5/waffle_hub/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-__version__ = "0.1.4"
+__version__ = "0.1.5"
 
 import importlib
 import warnings
 from collections import OrderedDict
 
 from tabulate import tabulate
```

### Comparing `waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/data_cfg.py` & `waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/configs/data_cfg.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/configs/model_cfg.py` & `waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/configs/model_cfg.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub/hub/adapter/tx_model/tx_model_hub.py` & `waffle_hub-0.1.5/waffle_hub/hub/adapter/tx_model/tx_model_hub.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub/hub/adapter/ultralytics/ultralytics_hub.py` & `waffle_hub-0.1.5/waffle_hub/hub/adapter/ultralytics/ultralytics_hub.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub/hub/base_hub.py` & `waffle_hub-0.1.5/waffle_hub/hub/base_hub.py`

 * *Files 1% similar despite different names*

```diff
@@ -167,25 +167,27 @@
 
         Raises:
             FileNotFoundError: if hub is not exist in root_dir
 
         Returns:
             Hub: Hub instance
         """
-        model_config_file = (
-            Path(root_dir if root_dir else BaseHub.DEFAULT_ROOT_DIR)
-            / name
-            / BaseHub.MODEL_CONFIG_FILE
-        )
+        root_dir = Path(root_dir if root_dir else BaseHub.DEFAULT_ROOT_DIR)
+        model_config_file = root_dir / name / BaseHub.MODEL_CONFIG_FILE
         if not model_config_file.exists():
             raise FileNotFoundError(
                 f"Model[{name}] does not exists. {model_config_file}"
             )
         model_config = io.load_yaml(model_config_file)
-        return cls(**model_config)
+        return cls(
+            **{
+                **model_config,
+                "root_dir": root_dir,
+            }
+        )
 
     @classmethod
     def from_model_config(
         cls, name: str, model_config_file: str, root_dir: str = None
     ) -> "BaseHub":
         """Create new Hub with model config.
```

### Comparing `waffle_hub-0.1.4/waffle_hub/hub/model/wrapper.py` & `waffle_hub-0.1.5/waffle_hub/hub/model/wrapper.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub/run.py` & `waffle_hub-0.1.5/waffle_hub/run.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub/schemas/configs.py` & `waffle_hub-0.1.5/waffle_hub/schemas/configs.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub/utils/callback.py` & `waffle_hub-0.1.5/waffle_hub/utils/callback.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub/utils/image.py` & `waffle_hub-0.1.5/waffle_hub/utils/image.py`

 * *Files identical despite different names*

### Comparing `waffle_hub-0.1.4/waffle_hub.egg-info/PKG-INFO` & `waffle_hub-0.1.5/waffle_hub.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: waffle-hub
-Version: 0.1.4
+Version: 0.1.5
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
-Metadata-Version: 2.1 Name: waffle-hub Version: 0.1.4 Summary: Waffle hub Home-
+Metadata-Version: 2.1 Name: waffle-hub Version: 0.1.5 Summary: Waffle hub Home-
 page: https://github.com/snuailab/waffle_hub Author: SNUAILAB Author-email:
 huijae.lee@snuailab.ai License: GPL-3.0 Project-URL: Bug Reports, https://
 github.com/snuailab/waffle_hub/issues Project-URL: Source, https://github.com/
 snuailab/waffle_hub Keywords: machine-learning,deep-
 learning,vision,ML,DL,AI,YOLO,Ultralytics,SNUAILAB Classifier: Development
 Status :: 3 - Alpha Classifier: Intended Audience :: Developers Classifier:
 Intended Audience :: Science/Research Classifier: License :: OSI Approved ::
```

### Comparing `waffle_hub-0.1.4/waffle_hub.egg-info/SOURCES.txt` & `waffle_hub-0.1.5/waffle_hub.egg-info/SOURCES.txt`

 * *Files identical despite different names*

