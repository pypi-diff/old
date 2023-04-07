# Comparing `tmp/monai_nvflare-0.2.1rc2-py3-none-any.whl.zip` & `tmp/monai_nvflare-0.2.2-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,12 +1,12 @@
-Zip file size: 11508 bytes, number of entries: 10
--rw-rw-r--  2.0 unx      847 b- defN 22-Oct-17 19:36 monai_nvflare/__init__.py
--rw-rw-r--  2.0 unx    10191 b- defN 22-Oct-14 15:54 monai_nvflare/client_algo_executor.py
--rw-rw-r--  2.0 unx     7385 b- defN 22-Oct-21 16:48 monai_nvflare/client_algo_statistics.py
--rw-rw-r--  2.0 unx     4839 b- defN 22-Sep-22 20:41 monai_nvflare/monai_bundle_persistor.py
--rw-rw-r--  2.0 unx     2150 b- defN 22-Oct-17 19:36 monai_nvflare/monai_data_stats_persistor.py
--rw-rw-r--  2.0 unx      724 b- defN 22-Oct-17 19:36 monai_nvflare/utils.py
--rw-rw-r--  2.0 unx     1969 b- defN 22-Oct-21 17:01 monai_nvflare-0.2.1rc2.dist-info/METADATA
--rw-rw-r--  2.0 unx       92 b- defN 22-Oct-21 17:01 monai_nvflare-0.2.1rc2.dist-info/WHEEL
--rw-rw-r--  2.0 unx       14 b- defN 22-Oct-21 17:01 monai_nvflare-0.2.1rc2.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      880 b- defN 22-Oct-21 17:01 monai_nvflare-0.2.1rc2.dist-info/RECORD
-10 files, 29091 bytes uncompressed, 9988 bytes compressed:  65.7%
+Zip file size: 11734 bytes, number of entries: 10
+-rw-rw-r--  2.0 unx      842 b- defN 23-Apr-05 22:42 monai_nvflare/__init__.py
+-rw-rw-r--  2.0 unx    10186 b- defN 23-Apr-05 22:42 monai_nvflare/client_algo_executor.py
+-rw-rw-r--  2.0 unx     7394 b- defN 23-Apr-05 22:42 monai_nvflare/client_algo_statistics.py
+-rw-rw-r--  2.0 unx     5077 b- defN 23-Apr-05 22:42 monai_nvflare/monai_bundle_persistor.py
+-rw-rw-r--  2.0 unx     2145 b- defN 23-Apr-05 22:42 monai_nvflare/monai_data_stats_persistor.py
+-rw-rw-r--  2.0 unx      747 b- defN 23-Apr-05 22:42 monai_nvflare/utils.py
+-rw-rw-r--  2.0 unx     2407 b- defN 23-Apr-07 02:03 monai_nvflare-0.2.2.dist-info/METADATA
+-rw-rw-r--  2.0 unx       92 b- defN 23-Apr-07 02:03 monai_nvflare-0.2.2.dist-info/WHEEL
+-rw-rw-r--  2.0 unx       14 b- defN 23-Apr-07 02:03 monai_nvflare-0.2.2.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx      868 b- defN 23-Apr-07 02:03 monai_nvflare-0.2.2.dist-info/RECORD
+10 files, 29772 bytes uncompressed, 10238 bytes compressed:  65.6%
```

## zipnote {}

```diff
@@ -12,20 +12,20 @@
 
 Filename: monai_nvflare/monai_data_stats_persistor.py
 Comment: 
 
 Filename: monai_nvflare/utils.py
 Comment: 
 
-Filename: monai_nvflare-0.2.1rc2.dist-info/METADATA
+Filename: monai_nvflare-0.2.2.dist-info/METADATA
 Comment: 
 
-Filename: monai_nvflare-0.2.1rc2.dist-info/WHEEL
+Filename: monai_nvflare-0.2.2.dist-info/WHEEL
 Comment: 
 
-Filename: monai_nvflare-0.2.1rc2.dist-info/top_level.txt
+Filename: monai_nvflare-0.2.2.dist-info/top_level.txt
 Comment: 
 
-Filename: monai_nvflare-0.2.1rc2.dist-info/RECORD
+Filename: monai_nvflare-0.2.2.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## monai_nvflare/__init__.py

```diff
@@ -1,8 +1,8 @@
-# Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
+# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
```

## monai_nvflare/client_algo_executor.py

```diff
@@ -1,8 +1,8 @@
-# Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
+# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
```

## monai_nvflare/client_algo_statistics.py

```diff
@@ -1,8 +1,8 @@
-# Copyright (c) 2022, NVIDIA CORPORATION.
+# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
@@ -42,15 +42,15 @@
         self.histograms = None
         self.fl_ctx = None
 
         self.req_num_of_bins = None
         self.req_bin_ranges = None
         self.feature_names = None
 
-    def initialize(self, parts: dict, fl_ctx: FLContext):
+    def initialize(self, fl_ctx: FLContext):
         self.fl_ctx = fl_ctx
         self.client_name = fl_ctx.get_identity_name()
         engine = fl_ctx.get_engine()
         self.client_algo_stats = engine.get_component(self.client_algo_stats_id)
         if not isinstance(self.client_algo_stats, ClientAlgoStats):
             raise TypeError(f"client_stats must be client_stats type. Got: {type(self.client_algo_stats)}")
         self.client_algo_stats.initialize(
```

## monai_nvflare/monai_bundle_persistor.py

```diff
@@ -1,8 +1,8 @@
-# Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
+# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
@@ -19,27 +19,28 @@
 from monai.fl.client.monai_algo import check_bundle_config
 from monai.fl.utils.constants import RequiredBundleKeys
 
 from nvflare.apis.event_type import EventType
 from nvflare.apis.fl_constant import FLContextKey
 from nvflare.apis.fl_context import FLContext
 from nvflare.app_common.app_constant import DefaultCheckpointFileName
-from nvflare.app_common.pt.pt_file_model_persistor import PTFileModelPersistor
+from nvflare.app_opt.pt.file_model_persistor import PTFileModelPersistor
 
 
 class MonaiBundlePersistor(PTFileModelPersistor):
     def __init__(
         self,
         bundle_root: str,
         config_train_filename: str = "configs/train.json",
         network_def_key: str = "network_def",
         exclude_vars=None,
         global_model_file_name=DefaultCheckpointFileName.GLOBAL_MODEL,
         best_global_model_file_name=DefaultCheckpointFileName.BEST_GLOBAL_MODEL,
         source_ckpt_filename=None,
+        filter_id: str = None,
     ):
         """Persist pytorch-based from MONAI bundle configuration.
 
         Args:
             bundle_root (str): path of bundle.
             config_train_filename (str, optional): bundle training config path relative to bundle_root;
                 defaults to "configs/train.json".
@@ -48,24 +49,26 @@
                 Defaults to None.
             global_model_file_name (str, optional): file name for saving global model.
                 Defaults to DefaultCheckpointFileName.GLOBAL_MODEL.
             best_global_model_file_name (str, optional): file name for saving best global model.
                 Defaults to DefaultCheckpointFileName.BEST_GLOBAL_MODEL.
             source_ckpt_filename (str, optional): file name for source model checkpoint file relative to `bundle_root`.
                 Defaults to None.
-
+            filter_id: Optional string that defines a filter component that is applied to prepare the model to be saved,
+                e.g. for serialization of custom Python objects.
         Raises:
             ValueError: when source_ckpt_filename does not exist
         """
         super().__init__(
             model=None,  # will be set in handle_event
             exclude_vars=exclude_vars,
             global_model_file_name=global_model_file_name,
             best_global_model_file_name=best_global_model_file_name,
             source_ckpt_file_full_name=None,  # will be set in _parse_config
+            filter_id=filter_id,
         )
 
         self.bundle_root = bundle_root
         self.config_train_filename = config_train_filename
         self.network_def_key = network_def_key
         self.source_ckpt_filename = source_ckpt_filename
```

## monai_nvflare/monai_data_stats_persistor.py

```diff
@@ -1,8 +1,8 @@
-# Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
+# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
```

## monai_nvflare/utils.py

```diff
@@ -1,19 +1,20 @@
-# Copyright (c) 2022, NVIDIA CORPORATION.
+# Copyright (c) 2022, NVIDIA CORPORATION.  All rights reserved.
 #
 # Licensed under the Apache License, Version 2.0 (the "License");
 # you may not use this file except in compliance with the License.
 # You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
+
 import json
 
 
 def convert_dict_keys(src_dict):
     """Convert dictionary to simple types"""
     return json.loads(json.dumps(src_dict))
```

## Comparing `monai_nvflare-0.2.1rc2.dist-info/METADATA` & `monai_nvflare-0.2.2.dist-info/METADATA`

 * *Files 9% similar despite different names*

```diff
@@ -1,20 +1,21 @@
 Metadata-Version: 2.1
 Name: monai-nvflare
-Version: 0.2.1rc2
+Version: 0.2.2
 Summary: MONAI NVIDIA FLARE integration
 Home-page: https://github.com/NVIDIA/NVFlare
-Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
+Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Operating System :: POSIX :: Linux
-Requires-Python: >=3.7,<3.9
+Requires-Python: >=3.8,<3.11
 Description-Content-Type: text/markdown
-Requires-Dist: monai (>=1.0.1rc4)
-Requires-Dist: nvflare (>=2.2.1rc9)
+Requires-Dist: monai (>=1.1.0)
+Requires-Dist: nvflare (>=2.3.0)
 
 # MONAI Integration
 
 ## Objective
 Integration with [MONAI](https://monai.io/)'s federated learning capabilities.
 
 Add `ClientAlgoExecutor` class to allow using MONAI's `ClientAlgo` class in federated scenarios.
@@ -28,23 +29,31 @@
 n/a
 
 ## Background
 MONAI allows the definition of AI models using the "[bundle](https://docs.monai.io/en/latest/bundle.html)" concept. 
 It allows for easy experimentation and sharing of models that have been developed using MONAI.
 Using the bundle configurations, we can use MONAI's `MonaiAlgo` (the implementation of `ClientAlgo`) to execute a bundle model in a federated scenario using NVFlare.
 
+![Federated Learning Module in MONAI (https://docs.monai.io/en/stable/modules.html#federated-learning)](https://docs.monai.io/en/stable/_images/federated.svg)
+
 ## Description
 NVFlare executes the `ClientAlgo` class using the `ClientAlgoExecutor` class provided with this package.
 
 ### Examples
 
-For an example of using [NVIDIA FLARE](https://nvflare.readthedocs.io/en/main/index.html) to train a medical image analysis model using federated averaging ([FedAvg]([FedAvg](https://arxiv.org/abs/1602.05629))) and [MONAI Bundle](https://docs.monai.io/en/latest/mb_specification.html), see the [examples/spleen_ct_segmentation](./examples/spleen_ct_segmentation).
+For an example of using [NVIDIA FLARE](https://nvflare.readthedocs.io/en/main/index.html) to train
+a medical image analysis model using federated averaging ([FedAvg](https://arxiv.org/abs/1602.05629))
+and [MONAI Bundle](https://docs.monai.io/en/latest/mb_specification.html),
+see the [examples](./examples/README.md).
 
 ## Requirements
 
+We recommend following the instructions for setting up a [virtual environment](../../examples/README.md#set-up-a-virtual-environment),
+and using it in [JupyterLab](../../examples/README.md#set-up-jupyterlab-for-notebooks) for running the notebooks the MONAI integration examples.
+
 Install MONAI-NVFlare integration from [PyPI](https://pypi.org/):
 ```
 pip install monai_nvflare
 ```
 
 (Optional) Install MONAI-NVFlare integration from source:
 ```
```

