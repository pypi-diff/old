# Comparing `tmp/tencentcloud-sdk-python-tione-3.0.867.tar.gz` & `tmp/tencentcloud-sdk-python-tione-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-tione-3.0.867.tar", last modified: Wed Apr  5 16:55:08 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-tione-3.0.868.tar", last modified: Fri Apr  7 01:03:05 2023, max compression
```

## Comparing `tencentcloud-sdk-python-tione-3.0.867.tar` & `tencentcloud-sdk-python-tione-3.0.868.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/
--rw-r--r--   0 root         (0) root         (0)     1010 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20211111/
--rw-r--r--   0 root         (0) root         (0)    51024 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20211111/tione_client.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20211111/__init__.py
--rw-r--r--   0 root         (0) root         (0)    10624 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20211111/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)   327221 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20211111/models.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20191022/
--rw-r--r--   0 root         (0) root         (0)    22010 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20191022/tione_client.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20191022/__init__.py
--rw-r--r--   0 root         (0) root         (0)     4465 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20191022/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)    91250 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20191022/models.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/setup.cfg
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud_sdk_python_tione.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud_sdk_python_tione.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      633 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud_sdk_python_tione.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1669 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud_sdk_python_tione.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/tencentcloud_sdk_python_tione.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     1669 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      743 2023-04-05 16:55:08.000000 tencentcloud-sdk-python-tione-3.0.867/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1669 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20191022/
+-rw-r--r--   0 root         (0) root         (0)    22010 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20191022/tione_client.py
+-rw-r--r--   0 root         (0) root         (0)    91250 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20191022/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20191022/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     4465 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20191022/errorcodes.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20211111/
+-rw-r--r--   0 root         (0) root         (0)    51024 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20211111/tione_client.py
+-rw-r--r--   0 root         (0) root         (0)   329804 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20211111/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20211111/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    10624 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20211111/errorcodes.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud_sdk_python_tione.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1669 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud_sdk_python_tione.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud_sdk_python_tione.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud_sdk_python_tione.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      633 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/tencentcloud_sdk_python_tione.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)      743 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/README.rst
+-rw-r--r--   0 root         (0) root         (0)     1010 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 01:03:05.000000 tencentcloud-sdk-python-tione-3.0.868/setup.cfg
```

### Comparing `tencentcloud-sdk-python-tione-3.0.867/setup.py` & `tencentcloud-sdk-python-tione-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-tione-3.0.867/tencentcloud/__init__.py` & `tencentcloud-sdk-python-tione-3.0.868/tencentcloud/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -10,8 +10,8 @@
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 
-__version__ = '3.0.867'
+__version__ = '3.0.868'
```

### Comparing `tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20211111/tione_client.py` & `tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20211111/tione_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20211111/errorcodes.py` & `tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20211111/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20211111/models.py` & `tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20211111/models.py`

 * *Files 2% similar despite different names*

```diff
@@ -119,38 +119,42 @@
         :type AccEngineVersion: str
         :param ModelInputPath: 模型输入cos路径
         :type ModelInputPath: :class:`tencentcloud.tione.v20211111.models.CosPathInfo`
         :param ModelName: 模型名称
         :type ModelName: str
         :param ModelSignature: SavedModel保存时配置的签名
         :type ModelSignature: str
+        :param FrameworkVersion: 加速引擎对应的框架版本
+        :type FrameworkVersion: str
         """
         self.ModelId = None
         self.ModelVersion = None
         self.ModelSource = None
         self.ModelFormat = None
         self.TensorInfos = None
         self.AccEngineVersion = None
         self.ModelInputPath = None
         self.ModelName = None
         self.ModelSignature = None
+        self.FrameworkVersion = None
 
 
     def _deserialize(self, params):
         self.ModelId = params.get("ModelId")
         self.ModelVersion = params.get("ModelVersion")
         self.ModelSource = params.get("ModelSource")
         self.ModelFormat = params.get("ModelFormat")
         self.TensorInfos = params.get("TensorInfos")
         self.AccEngineVersion = params.get("AccEngineVersion")
         if params.get("ModelInputPath") is not None:
             self.ModelInputPath = CosPathInfo()
             self.ModelInputPath._deserialize(params.get("ModelInputPath"))
         self.ModelName = params.get("ModelName")
         self.ModelSignature = params.get("ModelSignature")
+        self.FrameworkVersion = params.get("FrameworkVersion")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -4334,19 +4338,19 @@
 
     """
 
     def __init__(self):
         r"""
         :param Filters: 过滤器
 Filter.Name: 枚举值:
-    keyword (模型名称)
-    TrainingModelId (模型ID)
-    ModelVersionType (模型版本类型) 其值Filter.Values支持: NORMAL(通用) ACCELERATE (加速)
-    TrainingModelSource (模型来源)  其值Filter.Values支持： JOB/COS
-    ModelFormat（模型格式）其值Filter.Values支持：
+keyword (模型名称)
+TrainingModelId (模型ID)
+ModelVersionType (模型版本类型) 其值Filter.Values支持: NORMAL(通用) ACCELERATE (加速)
+TrainingModelSource (模型来源) 其值Filter.Values支持： JOB/COS
+ModelFormat（模型格式）其值Filter.Values支持：
 PYTORCH/TORCH_SCRIPT/DETECTRON2/SAVED_MODEL/FROZEN_GRAPH/PMML/MMDETECTION/ONNX/HUGGING_FACE
 Filter.Values: 当长度为1时，支持模糊查询; 不为1时，精确查询
 每次请求的Filters的上限为10，Filter.Values的上限为100
 Filter.Fuzzy取值：true/false，是否支持模糊匹配
         :type Filters: list of Filter
         :param OrderField: 排序字段，默认CreateTime
         :type OrderField: str
@@ -4354,21 +4358,24 @@
         :type Order: str
         :param Offset: 偏移量
         :type Offset: int
         :param Limit: 返回结果数量
         :type Limit: int
         :param TagFilters: 标签过滤
         :type TagFilters: list of TagFilter
+        :param WithModelVersions: 是否同时返回模型版本列表
+        :type WithModelVersions: bool
         """
         self.Filters = None
         self.OrderField = None
         self.Order = None
         self.Offset = None
         self.Limit = None
         self.TagFilters = None
+        self.WithModelVersions = None
 
 
     def _deserialize(self, params):
         if params.get("Filters") is not None:
             self.Filters = []
             for item in params.get("Filters"):
                 obj = Filter()
@@ -4380,14 +4387,15 @@
         self.Limit = params.get("Limit")
         if params.get("TagFilters") is not None:
             self.TagFilters = []
             for item in params.get("TagFilters"):
                 obj = TagFilter()
                 obj._deserialize(item)
                 self.TagFilters.append(obj)
+        self.WithModelVersions = params.get("WithModelVersions")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -4662,24 +4670,29 @@
         :type Version: str
         :param Image: 运行镜像
 注意：此字段可能返回 null，表示取不到有效值。
         :type Image: str
         :param IsSupportIntEightQuantization: 是否支持int8量化
 注意：此字段可能返回 null，表示取不到有效值。
         :type IsSupportIntEightQuantization: bool
+        :param FrameworkVersion: 框架版本
+注意：此字段可能返回 null，表示取不到有效值。
+        :type FrameworkVersion: str
         """
         self.Version = None
         self.Image = None
         self.IsSupportIntEightQuantization = None
+        self.FrameworkVersion = None
 
 
     def _deserialize(self, params):
         self.Version = params.get("Version")
         self.Image = params.get("Image")
         self.IsSupportIntEightQuantization = params.get("IsSupportIntEightQuantization")
+        self.FrameworkVersion = params.get("FrameworkVersion")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -5623,14 +5636,17 @@
         :type IsSaved: bool
         :param ModelSignature: SAVED_MODEL保存时配置的签名
 注意：此字段可能返回 null，表示取不到有效值。
         :type ModelSignature: str
         :param QATModel: 是否是QAT模型
 注意：此字段可能返回 null，表示取不到有效值。
         :type QATModel: bool
+        :param FrameworkVersion: 加速引擎对应的框架版本
+注意：此字段可能返回 null，表示取不到有效值。
+        :type FrameworkVersion: str
         """
         self.ModelAccTaskId = None
         self.ModelAccTaskName = None
         self.ModelId = None
         self.ModelName = None
         self.ModelVersion = None
         self.ModelSource = None
@@ -5652,14 +5668,15 @@
         self.TensorInfos = None
         self.HyperParameter = None
         self.AccEngineVersion = None
         self.Tags = None
         self.IsSaved = None
         self.ModelSignature = None
         self.QATModel = None
+        self.FrameworkVersion = None
 
 
     def _deserialize(self, params):
         self.ModelAccTaskId = params.get("ModelAccTaskId")
         self.ModelAccTaskName = params.get("ModelAccTaskName")
         self.ModelId = params.get("ModelId")
         self.ModelName = params.get("ModelName")
@@ -5699,14 +5716,15 @@
             for item in params.get("Tags"):
                 obj = Tag()
                 obj._deserialize(item)
                 self.Tags.append(obj)
         self.IsSaved = params.get("IsSaved")
         self.ModelSignature = params.get("ModelSignature")
         self.QATModel = params.get("QATModel")
+        self.FrameworkVersion = params.get("FrameworkVersion")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -6207,34 +6225,44 @@
         :type IP: str
         :param CreateTime: pod的创建时间
 注意：此字段可能返回 null，表示取不到有效值。
         :type CreateTime: str
         :param Containers: 容器列表
 注意：此字段可能返回 null，表示取不到有效值。
         :type Containers: :class:`tencentcloud.tione.v20211111.models.Container`
+        :param ContainerInfos: 容器列表
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ContainerInfos: list of Container
         """
         self.Name = None
         self.Uid = None
         self.ChargeType = None
         self.Phase = None
         self.IP = None
         self.CreateTime = None
         self.Containers = None
+        self.ContainerInfos = None
 
 
     def _deserialize(self, params):
         self.Name = params.get("Name")
         self.Uid = params.get("Uid")
         self.ChargeType = params.get("ChargeType")
         self.Phase = params.get("Phase")
         self.IP = params.get("IP")
         self.CreateTime = params.get("CreateTime")
         if params.get("Containers") is not None:
             self.Containers = Container()
             self.Containers._deserialize(params.get("Containers"))
+        if params.get("ContainerInfos") is not None:
+            self.ContainerInfos = []
+            for item in params.get("ContainerInfos"):
+                obj = Container()
+                obj._deserialize(item)
+                self.ContainerInfos.append(obj)
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -6573,14 +6601,16 @@
         :type HyperParameter: :class:`tencentcloud.tione.v20211111.models.HyperParameter`
         :param AccEngineVersion: 加速引擎版本
         :type AccEngineVersion: str
         :param Tags: 标签
         :type Tags: list of Tag
         :param ModelSignature: SavedModel保存时配置的签名
         :type ModelSignature: str
+        :param FrameworkVersion: 加速引擎对应的框架版本
+        :type FrameworkVersion: str
         """
         self.ModelAccTaskId = None
         self.ModelAccTaskName = None
         self.ModelSource = None
         self.AlgorithmFramework = None
         self.ModelId = None
         self.ModelName = None
@@ -6593,14 +6623,15 @@
         self.ModelFormat = None
         self.TensorInfos = None
         self.GPUType = None
         self.HyperParameter = None
         self.AccEngineVersion = None
         self.Tags = None
         self.ModelSignature = None
+        self.FrameworkVersion = None
 
 
     def _deserialize(self, params):
         self.ModelAccTaskId = params.get("ModelAccTaskId")
         self.ModelAccTaskName = params.get("ModelAccTaskName")
         self.ModelSource = params.get("ModelSource")
         self.AlgorithmFramework = params.get("AlgorithmFramework")
@@ -6631,14 +6662,15 @@
         if params.get("Tags") is not None:
             self.Tags = []
             for item in params.get("Tags"):
                 obj = Tag()
                 obj._deserialize(item)
                 self.Tags.append(obj)
         self.ModelSignature = params.get("ModelSignature")
+        self.FrameworkVersion = params.get("FrameworkVersion")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -7292,14 +7324,17 @@
         :type OldHybridBillingPrepaidReplicas: int
         :param ModelHotUpdateEnable: 是否开启模型的热更新。默认不开启
 注意：此字段可能返回 null，表示取不到有效值。
         :type ModelHotUpdateEnable: bool
         :param Pods: Pod列表信息
 注意：此字段可能返回 null，表示取不到有效值。
         :type Pods: :class:`tencentcloud.tione.v20211111.models.Pod`
+        :param PodInfos: Pod列表信息
+注意：此字段可能返回 null，表示取不到有效值。
+        :type PodInfos: list of Pod
         """
         self.Replicas = None
         self.ImageInfo = None
         self.Env = None
         self.Resources = None
         self.InstanceType = None
         self.ModelInfo = None
@@ -7312,14 +7347,15 @@
         self.PodList = None
         self.ResourceTotal = None
         self.OldReplicas = None
         self.HybridBillingPrepaidReplicas = None
         self.OldHybridBillingPrepaidReplicas = None
         self.ModelHotUpdateEnable = None
         self.Pods = None
+        self.PodInfos = None
 
 
     def _deserialize(self, params):
         self.Replicas = params.get("Replicas")
         if params.get("ImageInfo") is not None:
             self.ImageInfo = ImageInfo()
             self.ImageInfo._deserialize(params.get("ImageInfo"))
@@ -7355,14 +7391,20 @@
         self.OldReplicas = params.get("OldReplicas")
         self.HybridBillingPrepaidReplicas = params.get("HybridBillingPrepaidReplicas")
         self.OldHybridBillingPrepaidReplicas = params.get("OldHybridBillingPrepaidReplicas")
         self.ModelHotUpdateEnable = params.get("ModelHotUpdateEnable")
         if params.get("Pods") is not None:
             self.Pods = Pod()
             self.Pods._deserialize(params.get("Pods"))
+        if params.get("PodInfos") is not None:
+            self.PodInfos = []
+            for item in params.get("PodInfos"):
+                obj = Pod()
+                obj._deserialize(item)
+                self.PodInfos.append(obj)
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -8142,31 +8184,41 @@
         :type TrainingModelName: str
         :param Tags: 标签
 注意：此字段可能返回 null，表示取不到有效值。
         :type Tags: list of Tag
         :param CreateTime: 模型创建时间
 注意：此字段可能返回 null，表示取不到有效值。
         :type CreateTime: str
+        :param TrainingModelVersions: 模型版本列表。默认不返回，仅在指定请求参数开启时返回。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type TrainingModelVersions: list of TrainingModelVersionDTO
         """
         self.TrainingModelId = None
         self.TrainingModelName = None
         self.Tags = None
         self.CreateTime = None
+        self.TrainingModelVersions = None
 
 
     def _deserialize(self, params):
         self.TrainingModelId = params.get("TrainingModelId")
         self.TrainingModelName = params.get("TrainingModelName")
         if params.get("Tags") is not None:
             self.Tags = []
             for item in params.get("Tags"):
                 obj = Tag()
                 obj._deserialize(item)
                 self.Tags.append(obj)
         self.CreateTime = params.get("CreateTime")
+        if params.get("TrainingModelVersions") is not None:
+            self.TrainingModelVersions = []
+            for item in params.get("TrainingModelVersions"):
+                obj = TrainingModelVersionDTO()
+                obj._deserialize(item)
+                self.TrainingModelVersions.append(obj)
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
```

### Comparing `tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20191022/tione_client.py` & `tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20191022/tione_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20191022/errorcodes.py` & `tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20191022/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-tione-3.0.867/tencentcloud/tione/v20191022/models.py` & `tencentcloud-sdk-python-tione-3.0.868/tencentcloud/tione/v20191022/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-tione-3.0.867/tencentcloud_sdk_python_tione.egg-info/SOURCES.txt` & `tencentcloud-sdk-python-tione-3.0.868/tencentcloud_sdk_python_tione.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-tione-3.0.867/tencentcloud_sdk_python_tione.egg-info/PKG-INFO` & `tencentcloud-sdk-python-tione-3.0.868/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-tione
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Tione SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-tione-3.0.867/PKG-INFO` & `tencentcloud-sdk-python-tione-3.0.868/tencentcloud_sdk_python_tione.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-tione
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Tione SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-tione-3.0.867/README.rst` & `tencentcloud-sdk-python-tione-3.0.868/README.rst`

 * *Files identical despite different names*

