# Comparing `tmp/mlserver-alibi-explain-1.3.0.dev4.tar.gz` & `tmp/mlserver-alibi-explain-1.3.0rc1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mlserver-alibi-explain-1.3.0.dev4.tar", last modified: Wed Mar 22 09:49:14 2023, max compression
+gzip compressed data, was "mlserver-alibi-explain-1.3.0rc1.tar", last modified: Thu Apr  6 13:36:33 2023, max compression
```

## Comparing `mlserver-alibi-explain-1.3.0.dev4.tar` & `mlserver-alibi-explain-1.3.0rc1.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:49:14.202095 mlserver-alibi-explain-1.3.0.dev4/
--rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      643 2023-03-22 09:49:14.202095 mlserver-alibi-explain-1.3.0.dev4/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      233 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:49:14.198095 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/
--rw-r--r--   0 runner    (1001) docker     (123)       76 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2778 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/alibi_dependency_reference.py
--rw-r--r--   0 runner    (1001) docker     (123)     5296 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/common.py
--rw-r--r--   0 runner    (1001) docker     (123)      462 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/errors.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:49:14.198095 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/explainers/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/explainers/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     4309 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/explainers/black_box_runtime.py
--rw-r--r--   0 runner    (1001) docker     (123)     1010 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/explainers/integrated_gradients.py
--rw-r--r--   0 runner    (1001) docker     (123)     1777 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/explainers/white_box_runtime.py
--rw-r--r--   0 runner    (1001) docker     (123)     7903 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/runtime.py
--rw-r--r--   0 runner    (1001) docker     (123)       27 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-22 09:49:14.198095 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      643 2023-03-22 09:49:14.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      691 2023-03-22 09:49:14.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-22 09:49:14.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       39 2023-03-22 09:49:14.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       23 2023-03-22 09:49:14.000000 mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-22 09:49:14.202095 mlserver-alibi-explain-1.3.0.dev4/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1175 2023-03-22 09:48:43.000000 mlserver-alibi-explain-1.3.0.dev4/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:36:33.895706 mlserver-alibi-explain-1.3.0rc1/
+-rw-r--r--   0 runner    (1001) docker     (123)    11354 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      641 2023-04-06 13:36:33.895706 mlserver-alibi-explain-1.3.0rc1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      233 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:36:33.891706 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/
+-rw-r--r--   0 runner    (1001) docker     (123)       76 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2778 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/alibi_dependency_reference.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5296 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/common.py
+-rw-r--r--   0 runner    (1001) docker     (123)      462 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/errors.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:36:33.895706 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/explainers/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/explainers/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4277 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/explainers/black_box_runtime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1010 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/explainers/integrated_gradients.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1745 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/explainers/white_box_runtime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5934 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/runtime.py
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 13:36:33.891706 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      641 2023-04-06 13:36:33.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      691 2023-04-06 13:36:33.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 13:36:33.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       39 2023-04-06 13:36:33.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       23 2023-04-06 13:36:33.000000 mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 13:36:33.895706 mlserver-alibi-explain-1.3.0rc1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1175 2023-04-06 13:35:49.000000 mlserver-alibi-explain-1.3.0rc1/setup.py
```

### Comparing `mlserver-alibi-explain-1.3.0.dev4/LICENSE` & `mlserver-alibi-explain-1.3.0rc1/LICENSE`

 * *Files identical despite different names*

### Comparing `mlserver-alibi-explain-1.3.0.dev4/PKG-INFO` & `mlserver-alibi-explain-1.3.0rc1/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver-alibi-explain
-Version: 1.3.0.dev4
+Version: 1.3.0rc1
 Summary: Alibi-Explain runtime for MLServer
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # Alibi-Explain runtime for MLServer
```

### Comparing `mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/alibi_dependency_reference.py` & `mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/alibi_dependency_reference.py`

 * *Files identical despite different names*

### Comparing `mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/common.py` & `mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/common.py`

 * *Files identical despite different names*

### Comparing `mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/explainers/black_box_runtime.py` & `mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/explainers/black_box_runtime.py`

 * *Files 2% similar despite different names*

```diff
@@ -45,16 +45,15 @@
         if self.alibi_explain_settings.init_parameters is not None:
             init_parameters = self.alibi_explain_settings.init_parameters
             init_parameters["predictor"] = self._infer_impl
             self._model = self._explainer_class(**init_parameters)  # type: ignore
         else:
             self._model = await self._load_from_uri(self._infer_impl)
 
-        self.ready = True
-        return self.ready
+        return True
 
     def _explain_impl(self, input_data: Any, explain_parameters: Dict) -> Explanation:
         if not self.alibi_explain_settings.explainer_batch:
             # if we get a list of strings, we can only explain the first elem and there
             # is no way of just sending a plain string in v2, it has to be in a list
             # as the encoding is List[str] with content_type "BYTES"
             # we also assume that the explain data will contain a batch dimension,
```

### Comparing `mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/explainers/integrated_gradients.py` & `mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/explainers/integrated_gradients.py`

 * *Files identical despite different names*

### Comparing `mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/explainers/white_box_runtime.py` & `mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/explainers/white_box_runtime.py`

 * *Files 9% similar despite different names*

```diff
@@ -35,12 +35,11 @@
             init_parameters = self.alibi_explain_settings.init_parameters
             # white box explainers requires access to the inference model
             init_parameters["model"] = self._inference_model
             self._model = self._explainer_class(**init_parameters)  # type: ignore
         else:
             self._model = await self._load_from_uri(self._inference_model)
 
-        self.ready = True
-        return self.ready
+        return True
 
     async def _get_inference_model(self) -> Any:
         raise NotImplementedError
```

### Comparing `mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain/runtime.py` & `mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain/runtime.py`

 * *Files 24% similar despite different names*

```diff
@@ -1,41 +1,34 @@
-import json
 import asyncio
-import numpy as np
 import functools
+import json
+from concurrent.futures import ThreadPoolExecutor
+from typing import Any, Optional, Dict
 
-from typing import Any, Optional, List, Dict
-
+import numpy as np
 import pandas as pd
 from alibi.api.interfaces import Explanation, Explainer
 from alibi.saving import load_explainer
-from concurrent.futures import ThreadPoolExecutor
 
 from mlserver.codecs import (
     NumpyRequestCodec,
-    InputCodecLike,
     StringCodec,
-    RequestCodecLike,
 )
 from mlserver.errors import ModelParametersMissing
 from mlserver.handlers import custom_handler
 from mlserver.model import MLModel
 from mlserver.rest.responses import Response
 from mlserver.settings import ModelSettings, ModelParameters
 from mlserver.types import (
     InferenceRequest,
     InferenceResponse,
-    RequestInput,
-    MetadataModelResponse,
     Parameters,
-    MetadataTensor,
     ResponseOutput,
 )
 from mlserver.utils import get_model_uri
-
 from mlserver_alibi_explain.alibi_dependency_reference import (
     get_mlmodel_class_as_str,
     get_alibi_class_as_str,
 )
 from mlserver_alibi_explain.common import (
     AlibiExplainSettings,
     import_and_get_class,
@@ -53,14 +46,15 @@
     def __init__(
         self, settings: ModelSettings, explainer_settings: AlibiExplainSettings
     ):
         self.alibi_explain_settings = explainer_settings
         self._executor = ThreadPoolExecutor()
         super().__init__(settings)
 
+    @custom_handler(rest_path="/explain")
     async def explain_v1_output(self, request: InferenceRequest) -> Response:
         """
         A custom endpoint to return explanation results in plain json format (no v2
         encoding) to keep backward compatibility of legacy downstream users.
 
         This does not work with multi-model serving as no reference to the model exists
         in the endpoint.
@@ -144,90 +138,25 @@
         return await loop.run_in_executor(self._executor, load_call)
 
     def _explain_impl(self, input_data: Any, explain_parameters: Dict) -> Explanation:
         """Actual explain to be implemented by subclasses"""
         raise NotImplementedError
 
 
-class AlibiExplainRuntime(MLModel):
+class AlibiExplainRuntime:
     """Wrapper / Factory class for specific alibi explain runtimes"""
 
-    def __init__(self, settings: ModelSettings):
+    def __new__(cls, settings: ModelSettings):
         # TODO: we probably want to validate the enum more sanely here
         # we do not want to construct a specific alibi settings here because
         # it might be dependent on type
         # although at the moment we only have one `AlibiExplainSettings`
         assert settings.parameters is not None
         assert EXPLAINER_TYPE_TAG in settings.parameters.extra  # type: ignore
 
         explainer_type = settings.parameters.extra[EXPLAINER_TYPE_TAG]  # type: ignore
 
         rt_class = import_and_get_class(get_mlmodel_class_as_str(explainer_type))
 
         alibi_class = import_and_get_class(get_alibi_class_as_str(explainer_type))
 
-        self._rt = rt_class(settings, alibi_class)
-
-    @property
-    def name(self) -> str:
-        return self._rt.name
-
-    @property
-    def version(self) -> Optional[str]:
-        return self._rt.version
-
-    @property
-    def settings(self) -> ModelSettings:
-        return self._rt.settings
-
-    @property
-    def inputs(self) -> Optional[List[MetadataTensor]]:
-        return self._rt.inputs
-
-    @inputs.setter
-    def inputs(self, value: List[MetadataTensor]):
-        self._rt.inputs = value
-
-    @property
-    def outputs(self) -> Optional[List[MetadataTensor]]:
-        return self._rt.outputs
-
-    @outputs.setter
-    def outputs(self, value: List[MetadataTensor]):
-        self._rt.outputs = value
-
-    @property  # type: ignore
-    def ready(self) -> bool:  # type: ignore
-        return self._rt.ready
-
-    @ready.setter
-    def ready(self, value: bool):
-        self._rt.ready = value
-
-    def decode(
-        self,
-        request_input: RequestInput,
-        default_codec: Optional[InputCodecLike] = None,
-    ) -> Any:
-        return self._rt.decode(request_input, default_codec)
-
-    def decode_request(
-        self,
-        inference_request: InferenceRequest,
-        default_codec: Optional[RequestCodecLike] = None,
-    ) -> Any:
-        return self._rt.decode_request(inference_request, default_codec)
-
-    async def metadata(self) -> MetadataModelResponse:
-        return await self._rt.metadata()
-
-    async def load(self) -> bool:
-        return await self._rt.load()
-
-    async def predict(self, payload: InferenceRequest) -> InferenceResponse:
-        return await self._rt.predict(payload)
-
-    # we add _explain_v1_output here to enable the registration and routing of custom
-    # endpoint to `_rt.explain_v1_output`
-    @custom_handler(rest_path="/explain")
-    async def _explain_v1_output(self, request: InferenceRequest) -> Response:
-        return await self._rt.explain_v1_output(request)
+        return rt_class(settings, alibi_class)
```

### Comparing `mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain.egg-info/PKG-INFO` & `mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mlserver-alibi-explain
-Version: 1.3.0.dev4
+Version: 1.3.0rc1
 Summary: Alibi-Explain runtime for MLServer
 Home-page: https://github.com/SeldonIO/MLServer.git
 Author: Seldon Technologies Ltd.
 Author-email: hello@seldon.io
 License: Apache 2.0
 Description: # Alibi-Explain runtime for MLServer
```

### Comparing `mlserver-alibi-explain-1.3.0.dev4/mlserver_alibi_explain.egg-info/SOURCES.txt` & `mlserver-alibi-explain-1.3.0rc1/mlserver_alibi_explain.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mlserver-alibi-explain-1.3.0.dev4/setup.py` & `mlserver-alibi-explain-1.3.0rc1/setup.py`

 * *Files identical despite different names*

