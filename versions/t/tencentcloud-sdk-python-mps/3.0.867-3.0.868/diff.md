# Comparing `tmp/tencentcloud-sdk-python-mps-3.0.867.tar.gz` & `tmp/tencentcloud-sdk-python-mps-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-mps-3.0.867.tar", last modified: Wed Apr  5 16:44:19 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-mps-3.0.868.tar", last modified: Fri Apr  7 00:45:55 2023, max compression
```

## Comparing `tencentcloud-sdk-python-mps-3.0.867.tar` & `tencentcloud-sdk-python-mps-3.0.868.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/
--rw-r--r--   0 root         (0) root         (0)     1006 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud/
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/v20190612/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/v20190612/__init__.py
--rw-r--r--   0 root         (0) root         (0)    89755 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/v20190612/mps_client.py
--rw-r--r--   0 root         (0) root         (0)    13373 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/v20190612/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)   781435 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/v20190612/models.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/__init__.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      737 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud_sdk_python_mps.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud_sdk_python_mps.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      445 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud_sdk_python_mps.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud_sdk_python_mps.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 16:44:19.000000 tencentcloud-sdk-python-mps-3.0.867/tencentcloud_sdk_python_mps.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud/
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/v20190612/
+-rw-r--r--   0 root         (0) root         (0)    89755 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/v20190612/mps_client.py
+-rw-r--r--   0 root         (0) root         (0)   797827 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/v20190612/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/v20190612/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    13373 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/v20190612/errorcodes.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud_sdk_python_mps.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud_sdk_python_mps.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud_sdk_python_mps.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud_sdk_python_mps.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      445 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/tencentcloud_sdk_python_mps.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)      737 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/README.rst
+-rw-r--r--   0 root         (0) root         (0)     1006 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 00:45:55.000000 tencentcloud-sdk-python-mps-3.0.868/setup.cfg
```

### Comparing `tencentcloud-sdk-python-mps-3.0.867/setup.py` & `tencentcloud-sdk-python-mps-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mps-3.0.867/tencentcloud/__init__.py` & `tencentcloud-sdk-python-mps-3.0.868/tencentcloud/__init__.py`

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

### Comparing `tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/v20190612/mps_client.py` & `tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/v20190612/mps_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/v20190612/errorcodes.py` & `tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/v20190612/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mps-3.0.867/tencentcloud/mps/v20190612/models.py` & `tencentcloud-sdk-python-mps-3.0.868/tencentcloud/mps/v20190612/models.py`

 * *Files 2% similar despite different names*

```diff
@@ -211,18 +211,21 @@
 <li>action-AIAnalysis: 分析</li>
 <li>action-AIRecognition：识别</li>
 <li>action-aiReview：审核</li>
 <li>action-animated-graphics：转动图</li>
 <li>action-image-sprite：雪碧图</li>
 <li>action-snapshotByTimeOffset: 时间点截图</li>
 <li>action-adaptive-substream：自适应码流</li>
+注意：此字段可能返回 null，表示取不到有效值。
         :type ActivityType: str
         :param ReardriveIndex: 后驱节点索引数组
+注意：此字段可能返回 null，表示取不到有效值。
         :type ReardriveIndex: list of int
         :param ActivityPara: 原子任务参数
+注意：此字段可能返回 null，表示取不到有效值。
         :type ActivityPara: :class:`tencentcloud.mps.v20190612.models.ActivityPara`
         """
         self.ActivityType = None
         self.ReardriveIndex = None
         self.ActivityPara = None
 
 
@@ -666,20 +669,24 @@
         :type CoverTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskCoverResult`
         :param TagTask: 视频内容分析智能标签任务的查询结果，当任务类型为 Tag 时有效。
 注意：此字段可能返回 null，表示取不到有效值。
         :type TagTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskTagResult`
         :param FrameTagTask: 视频内容分析智能按帧标签任务的查询结果，当任务类型为 FrameTag 时有效。
 注意：此字段可能返回 null，表示取不到有效值。
         :type FrameTagTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskFrameTagResult`
+        :param HighlightTask: 视频内容分析集锦任务的查询结果，当任务类型为 Highlight时有效。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type HighlightTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskHighlightResult`
         """
         self.Type = None
         self.ClassificationTask = None
         self.CoverTask = None
         self.TagTask = None
         self.FrameTagTask = None
+        self.HighlightTask = None
 
 
     def _deserialize(self, params):
         self.Type = params.get("Type")
         if params.get("ClassificationTask") is not None:
             self.ClassificationTask = AiAnalysisTaskClassificationResult()
             self.ClassificationTask._deserialize(params.get("ClassificationTask"))
@@ -688,14 +695,17 @@
             self.CoverTask._deserialize(params.get("CoverTask"))
         if params.get("TagTask") is not None:
             self.TagTask = AiAnalysisTaskTagResult()
             self.TagTask._deserialize(params.get("TagTask"))
         if params.get("FrameTagTask") is not None:
             self.FrameTagTask = AiAnalysisTaskFrameTagResult()
             self.FrameTagTask._deserialize(params.get("FrameTagTask"))
+        if params.get("HighlightTask") is not None:
+            self.HighlightTask = AiAnalysisTaskHighlightResult()
+            self.HighlightTask._deserialize(params.get("HighlightTask"))
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -1009,14 +1019,118 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class AiAnalysisTaskHighlightInput(AbstractModel):
+    """智能精彩片段任务输入类型
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Definition: 视频智能精彩片段模板 ID。
+        :type Definition: int
+        """
+        self.Definition = None
+
+
+    def _deserialize(self, params):
+        self.Definition = params.get("Definition")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class AiAnalysisTaskHighlightOutput(AbstractModel):
+    """智能精彩片段结果信息
+
+    """
+
+    def __init__(self):
+        r"""
+        :param HighlightSet: 视频智能精彩片段列表。
+        :type HighlightSet: list of MediaAiAnalysisHighlightItem
+        :param OutputStorage: 精彩片段的存储位置。
+        :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
+        """
+        self.HighlightSet = None
+        self.OutputStorage = None
+
+
+    def _deserialize(self, params):
+        if params.get("HighlightSet") is not None:
+            self.HighlightSet = []
+            for item in params.get("HighlightSet"):
+                obj = MediaAiAnalysisHighlightItem()
+                obj._deserialize(item)
+                self.HighlightSet.append(obj)
+        if params.get("OutputStorage") is not None:
+            self.OutputStorage = TaskOutputStorage()
+            self.OutputStorage._deserialize(params.get("OutputStorage"))
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class AiAnalysisTaskHighlightResult(AbstractModel):
+    """智能精彩片段结果类型
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
+        :type Status: str
+        :param ErrCode: 错误码，0：成功，其他值：失败。
+        :type ErrCode: int
+        :param Message: 错误信息。
+        :type Message: str
+        :param Input: 智能精彩片段任务输入。
+        :type Input: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskHighlightInput`
+        :param Output: 智能精彩片段任务输出。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Output: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskHighlightOutput`
+        """
+        self.Status = None
+        self.ErrCode = None
+        self.Message = None
+        self.Input = None
+        self.Output = None
+
+
+    def _deserialize(self, params):
+        self.Status = params.get("Status")
+        self.ErrCode = params.get("ErrCode")
+        self.Message = params.get("Message")
+        if params.get("Input") is not None:
+            self.Input = AiAnalysisTaskHighlightInput()
+            self.Input._deserialize(params.get("Input"))
+        if params.get("Output") is not None:
+            self.Output = AiAnalysisTaskHighlightOutput()
+            self.Output._deserialize(params.get("Output"))
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class AiAnalysisTaskInput(AbstractModel):
     """AI 视频智能分析输入参数类型
 
     """
 
     def __init__(self):
         r"""
@@ -1277,14 +1391,44 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class AiQualityControlTaskInput(AbstractModel):
+    """视频质检输入参数类型
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Definition: 视频质检模板 ID 。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Definition: int
+        :param ChannelExtPara: 渠道扩展参数json序列化字符串。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ChannelExtPara: str
+        """
+        self.Definition = None
+        self.ChannelExtPara = None
+
+
+    def _deserialize(self, params):
+        self.Definition = params.get("Definition")
+        self.ChannelExtPara = params.get("ChannelExtPara")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class AiRecognitionResult(AbstractModel):
     """智能识别结果。
 
     """
 
     def __init__(self):
         r"""
@@ -4246,29 +4390,29 @@
 class AwsS3FileUploadTrigger(AbstractModel):
     """AWS S3 文件是上传触发器。
 
     """
 
     def __init__(self):
         r"""
-        :param S3Bucket: 工作流绑定的 AWS S3 存储桶。
+        :param S3Bucket: 绑定的 AWS S3 存储桶。
         :type S3Bucket: str
-        :param S3Region: 工作流绑定的桶所在 AWS 区域。
+        :param S3Region: 绑定的桶所在 AWS 区域。
         :type S3Region: str
-        :param Dir: 工作流绑定的输入路径目录，必须为绝对路径，即以 `/` 开头和结尾。如`/movie/201907/`，不填代表根目录`/`。	
+        :param Dir: 绑定的输入路径目录，必须为绝对路径，即以 `/` 开头和结尾。如`/movie/201907/`，不填代表根目录`/`。	
         :type Dir: str
-        :param Formats: 工作流允许触发的文件格式列表，如 ["mp4", "flv", "mov"]。不填代表所有格式的文件都可以触发工作流。	
+        :param Formats: 允许触发的文件格式列表，如 ["mp4", "flv", "mov"]。不填代表所有格式的文件都可以触发工作流。	
         :type Formats: list of str
-        :param S3SecretId: 工作流绑定的 AWS S3 存储桶的秘钥ID。
+        :param S3SecretId: 绑定的 AWS S3 存储桶的秘钥ID。
 注意：此字段可能返回 null，表示取不到有效值。
         :type S3SecretId: str
-        :param S3SecretKey: 工作流绑定的 AWS S3 存储桶的秘钥Key。
+        :param S3SecretKey: 绑定的 AWS S3 存储桶的秘钥Key。
 注意：此字段可能返回 null，表示取不到有效值。
         :type S3SecretKey: str
-        :param AwsSQS: 工作流绑定的 AWS S3 存储桶对应的 SQS事件队列。
+        :param AwsSQS: 绑定的 AWS S3 存储桶对应的 SQS事件队列。
 注意：队列和桶需要在同一区域。
 注意：此字段可能返回 null，表示取不到有效值。
         :type AwsSQS: :class:`tencentcloud.mps.v20190612.models.AwsSQS`
         """
         self.S3Bucket = None
         self.S3Region = None
         self.Dir = None
@@ -5869,21 +6013,22 @@
 
     """
 
     def __init__(self):
         r"""
         :param ScheduleName: 编排名称，最多128字符。同一个用户该名称唯一。
         :type ScheduleName: str
-        :param Trigger: 编排绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。
+        :param Trigger: 编排绑定的触发规则，当上传视频命中该规则到该对象时即触发编排。
         :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
         :param Activities: 编排任务列表。
         :type Activities: list of Activity
         :param OutputStorage: 媒体处理的文件输出存储位置。不填则继承 Trigger 中的存储位置。
         :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
-        :param OutputDir: 媒体处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致。
+        :param OutputDir: 媒体处理生成的文件输出的目标目录，必选以 / 开头和结尾，如`/movie/201907/`。
+如果不填，表示与触发文件所在的目录一致。
         :type OutputDir: str
         :param TaskNotifyConfig: 任务的事件通知配置，不填代表不获取事件通知。
         :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
         """
         self.ScheduleName = None
         self.Trigger = None
         self.Activities = None
@@ -6403,15 +6548,16 @@
         r"""
         :param WorkflowName: 工作流名称，最多128字符。同一个用户该名称唯一。
         :type WorkflowName: str
         :param Trigger: 工作流绑定的触发规则，当上传视频命中该规则到该对象时即触发工作流。
         :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
         :param OutputStorage: 媒体处理的文件输出存储位置。不填则继承 Trigger 中的存储位置。
         :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
-        :param OutputDir: 媒体处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与触发文件所在的目录一致。
+        :param OutputDir: 媒体处理生成的文件输出的目标目录，必选以 / 开头和结尾，如`/movie/201907/`。
+如果不填，表示与触发文件所在的目录一致。
         :type OutputDir: str
         :param MediaProcessTask: 媒体处理类型任务参数。
         :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
         :param AiContentReviewTask: 视频内容审核类型任务参数。
         :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
         :param AiAnalysisTask: 视频内容分析类型任务参数。
         :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
@@ -8649,32 +8795,39 @@
 
     """
 
     def __init__(self):
         r"""
         :param ScheduleIds: 编排 ID 过滤条件，数组长度限制：100。
         :type ScheduleIds: list of int
+        :param TriggerType: 编排触发类型，可选值：
+<li>CosFileUpload： 腾讯云 COS 文件上传触发</li>
+<li>AwsS3FileUpload：Aws S3 文件上传触发。</li>
+不填或者为空表示全部。
+        :type TriggerType: str
         :param Status: 状态，取值范围：
 <li>Enabled：已启用，</li>
 <li>Disabled：已禁用。</li>
-不填此参数，则不区分工作流状态。
+不填此参数，则不区编排状态。
         :type Status: str
         :param Offset: 分页偏移量，默认值：0。
         :type Offset: int
         :param Limit: 返回记录条数，默认值：10，最大值：100。
         :type Limit: int
         """
         self.ScheduleIds = None
+        self.TriggerType = None
         self.Status = None
         self.Offset = None
         self.Limit = None
 
 
     def _deserialize(self, params):
         self.ScheduleIds = params.get("ScheduleIds")
+        self.TriggerType = params.get("TriggerType")
         self.Status = params.get("Status")
         self.Offset = params.get("Offset")
         self.Limit = params.get("Limit")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
@@ -11269,14 +11422,46 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class HighlightSegmentItem(AbstractModel):
+    """智能精彩集锦片段列表。
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Confidence: 置信度。
+        :type Confidence: float
+        :param StartTimeOffset: 片段起始时间偏移。
+        :type StartTimeOffset: float
+        :param EndTimeOffset: 片段结束时间偏移。
+        :type EndTimeOffset: float
+        """
+        self.Confidence = None
+        self.StartTimeOffset = None
+        self.EndTimeOffset = None
+
+
+    def _deserialize(self, params):
+        self.Confidence = params.get("Confidence")
+        self.StartTimeOffset = params.get("StartTimeOffset")
+        self.EndTimeOffset = params.get("EndTimeOffset")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class ImageQualityEnhanceConfig(AbstractModel):
     """综合增强配置
 
     """
 
     def __init__(self):
         r"""
@@ -12612,14 +12797,59 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class MediaAiAnalysisHighlightItem(AbstractModel):
+    """智能精彩片段信息
+
+    """
+
+    def __init__(self):
+        r"""
+        :param HighlightPath: 智能精彩集锦地址。
+        :type HighlightPath: str
+        :param CovImgPath: 智能精彩集锦封面地址。
+        :type CovImgPath: str
+        :param Confidence: 智能精彩集锦的可信度，取值范围是 0 到 100。
+        :type Confidence: float
+        :param Duration: 智能精彩集锦持续时间。
+        :type Duration: float
+        :param SegmentSet: 智能精彩集锦子片段列表。
+        :type SegmentSet: list of HighlightSegmentItem
+        """
+        self.HighlightPath = None
+        self.CovImgPath = None
+        self.Confidence = None
+        self.Duration = None
+        self.SegmentSet = None
+
+
+    def _deserialize(self, params):
+        self.HighlightPath = params.get("HighlightPath")
+        self.CovImgPath = params.get("CovImgPath")
+        self.Confidence = params.get("Confidence")
+        self.Duration = params.get("Duration")
+        if params.get("SegmentSet") is not None:
+            self.SegmentSet = []
+            for item in params.get("SegmentSet"):
+                obj = HighlightSegmentItem()
+                obj._deserialize(item)
+                self.SegmentSet.append(obj)
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class MediaAiAnalysisTagItem(AbstractModel):
     """智能标签结果信息
 
     """
 
     def __init__(self):
         r"""
@@ -14704,15 +14934,15 @@
         :param Trigger: 编排绑定的触发规则。
         :type Trigger: :class:`tencentcloud.mps.v20190612.models.WorkflowTrigger`
         :param Activities: 编排任务列表。
 注意：内部不允许部分更新，如果需要更新需全量提交编排任务列表。
         :type Activities: list of Activity
         :param OutputStorage: 媒体处理的文件输出存储位置。
         :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
-        :param OutputDir: 媒体处理生成的文件输出的目标目录。
+        :param OutputDir: 媒体处理生成的文件输出的目标目录，必选以 / 开头和结尾。
 注意：如果设置为空，则表示取消老配置的OutputDir值。
         :type OutputDir: str
         :param TaskNotifyConfig: 任务的事件通知配置。
         :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
         """
         self.ScheduleId = None
         self.ScheduleName = None
@@ -16431,87 +16661,94 @@
 
     def __init__(self):
         r"""
         :param InputInfo: 媒体处理的文件输入信息。
         :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
         :param OutputStorage: 媒体处理输出文件的目标存储。不填则继承 InputInfo 中的存储位置。
         :type OutputStorage: :class:`tencentcloud.mps.v20190612.models.TaskOutputStorage`
-        :param OutputDir: 媒体处理生成的文件输出的目标目录，如`/movie/201907/`。如果不填，表示与 InputInfo 中文件所在的目录一致。
+        :param OutputDir: 媒体处理生成的文件输出的目标目录，必选以 / 开头和结尾，如`/movie/201907/`。
+如果不填，表示与 InputInfo 中文件所在的目录一致。
         :type OutputDir: str
+        :param ScheduleId: 编排ID。
+注意1：对于OutputStorage、OutputDir参数：
+<li>当服务编排中子任务节点配置了OutputStorage、OutputDir时，该子任务节点中配置的输出作为子任务的输出。</li>
+<li>当服务编排中子任务节点没有配置OutputStorage、OutputDir时，若创建任务接口（ProcessMedia）有输出，将覆盖原有编排的默认输出。</li>
+注意2：对于TaskNotifyConfig参数，若创建任务接口（ProcessMedia）有设置，将覆盖原有编排的默认回调。
+
+注意3：编排的 Trigger 只是用来自动化触发场景，在手动发起的请求中已经配置的 Trigger 无意义。
+        :type ScheduleId: int
         :param MediaProcessTask: 媒体处理类型任务参数。
         :type MediaProcessTask: :class:`tencentcloud.mps.v20190612.models.MediaProcessTaskInput`
         :param AiContentReviewTask: 视频内容审核类型任务参数。
         :type AiContentReviewTask: :class:`tencentcloud.mps.v20190612.models.AiContentReviewTaskInput`
         :param AiAnalysisTask: 视频内容分析类型任务参数。
         :type AiAnalysisTask: :class:`tencentcloud.mps.v20190612.models.AiAnalysisTaskInput`
         :param AiRecognitionTask: 视频内容识别类型任务参数。
         :type AiRecognitionTask: :class:`tencentcloud.mps.v20190612.models.AiRecognitionTaskInput`
+        :param AiQualityControlTask: 视频质检类型任务参数。
+        :type AiQualityControlTask: :class:`tencentcloud.mps.v20190612.models.AiQualityControlTaskInput`
         :param TaskNotifyConfig: 任务的事件通知信息，不填代表不获取事件通知。
         :type TaskNotifyConfig: :class:`tencentcloud.mps.v20190612.models.TaskNotifyConfig`
         :param TasksPriority: 任务流的优先级，数值越大优先级越高，取值范围是-10到 10，不填代表0。
         :type TasksPriority: int
         :param SessionId: 用于去重的识别码，如果三天内曾有过相同的识别码的请求，则本次的请求会返回错误。最长 50 个字符，不带或者带空字符串表示不做去重。
         :type SessionId: str
         :param SessionContext: 来源上下文，用于透传用户请求信息，任务流状态变更回调将返回该字段值，最长 1000 个字符。
         :type SessionContext: str
-        :param ScheduleId: 编排ID。
-注意1：对于OutputStorage、OutputDir参数：
-<li>当服务编排中子任务节点配置了OutputStorage、OutputDir时，该子任务节点中配置的输出作为子任务的输出。</li>
-<li>当服务编排中子任务节点没有配置OutputStorage、OutputDir时，若创建任务接口（ProcessMedia）有输出，将覆盖原有编排的默认输出。</li>
-注意2：对于TaskNotifyConfig参数，若创建任务接口（ProcessMedia）有设置，将覆盖原有编排的默认回调。
-
-注意3：编排的 Trigger 只是用来自动化触发场景，在手动发起的请求中已经配置的 Trigger 无意义。
-        :type ScheduleId: int
         :param TaskType: 任务类型，默认Online
 <li> Online：实时任务</li>
 <li> Offline：闲时任务，不保证实效性，默认3天内处理完</li>
         :type TaskType: str
         """
         self.InputInfo = None
         self.OutputStorage = None
         self.OutputDir = None
+        self.ScheduleId = None
         self.MediaProcessTask = None
         self.AiContentReviewTask = None
         self.AiAnalysisTask = None
         self.AiRecognitionTask = None
+        self.AiQualityControlTask = None
         self.TaskNotifyConfig = None
         self.TasksPriority = None
         self.SessionId = None
         self.SessionContext = None
-        self.ScheduleId = None
         self.TaskType = None
 
 
     def _deserialize(self, params):
         if params.get("InputInfo") is not None:
             self.InputInfo = MediaInputInfo()
             self.InputInfo._deserialize(params.get("InputInfo"))
         if params.get("OutputStorage") is not None:
             self.OutputStorage = TaskOutputStorage()
             self.OutputStorage._deserialize(params.get("OutputStorage"))
         self.OutputDir = params.get("OutputDir")
+        self.ScheduleId = params.get("ScheduleId")
         if params.get("MediaProcessTask") is not None:
             self.MediaProcessTask = MediaProcessTaskInput()
             self.MediaProcessTask._deserialize(params.get("MediaProcessTask"))
         if params.get("AiContentReviewTask") is not None:
             self.AiContentReviewTask = AiContentReviewTaskInput()
             self.AiContentReviewTask._deserialize(params.get("AiContentReviewTask"))
         if params.get("AiAnalysisTask") is not None:
             self.AiAnalysisTask = AiAnalysisTaskInput()
             self.AiAnalysisTask._deserialize(params.get("AiAnalysisTask"))
         if params.get("AiRecognitionTask") is not None:
             self.AiRecognitionTask = AiRecognitionTaskInput()
             self.AiRecognitionTask._deserialize(params.get("AiRecognitionTask"))
+        if params.get("AiQualityControlTask") is not None:
+            self.AiQualityControlTask = AiQualityControlTaskInput()
+            self.AiQualityControlTask._deserialize(params.get("AiQualityControlTask"))
         if params.get("TaskNotifyConfig") is not None:
             self.TaskNotifyConfig = TaskNotifyConfig()
             self.TaskNotifyConfig._deserialize(params.get("TaskNotifyConfig"))
         self.TasksPriority = params.get("TasksPriority")
         self.SessionId = params.get("SessionId")
         self.SessionContext = params.get("SessionContext")
-        self.ScheduleId = params.get("ScheduleId")
         self.TaskType = params.get("TaskType")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
@@ -16737,14 +16974,146 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class QualityControlData(AbstractModel):
+    """质检结果输出。
+
+    """
+
+    def __init__(self):
+        r"""
+        :param NoAudio: 为true时表示视频无音频轨。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type NoAudio: bool
+        :param NoVideo: 为true时表示视频无视频轨。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type NoVideo: bool
+        :param QualityEvaluationScore: 视频无参考质量打分，百分制。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type QualityEvaluationScore: int
+        :param QualityControlResultSet: 质检检出异常项。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type QualityControlResultSet: list of QualityControlResult
+        """
+        self.NoAudio = None
+        self.NoVideo = None
+        self.QualityEvaluationScore = None
+        self.QualityControlResultSet = None
+
+
+    def _deserialize(self, params):
+        self.NoAudio = params.get("NoAudio")
+        self.NoVideo = params.get("NoVideo")
+        self.QualityEvaluationScore = params.get("QualityEvaluationScore")
+        if params.get("QualityControlResultSet") is not None:
+            self.QualityControlResultSet = []
+            for item in params.get("QualityControlResultSet"):
+                obj = QualityControlResult()
+                obj._deserialize(item)
+                self.QualityControlResultSet.append(obj)
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class QualityControlItem(AbstractModel):
+    """质检结果项
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Confidence: 置信度，取值范围是 0 到 100。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Confidence: int
+        :param StartTimeOffset: 出现的起始时间戳，秒。
+        :type StartTimeOffset: float
+        :param EndTimeOffset: 出现的结束时间戳，秒。
+        :type EndTimeOffset: float
+        :param AreaCoordSet: 区域坐标(px)，即左上角坐标、右下角坐标。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type AreaCoordSet: list of int
+        """
+        self.Confidence = None
+        self.StartTimeOffset = None
+        self.EndTimeOffset = None
+        self.AreaCoordSet = None
+
+
+    def _deserialize(self, params):
+        self.Confidence = params.get("Confidence")
+        self.StartTimeOffset = params.get("StartTimeOffset")
+        self.EndTimeOffset = params.get("EndTimeOffset")
+        self.AreaCoordSet = params.get("AreaCoordSet")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class QualityControlResult(AbstractModel):
+    """质检异常项。
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Type: 异常类型，取值范围：
+Jitter：抖动，
+Blur：模糊，
+LowLighting：低光照，
+HighLighting：过曝，
+CrashScreen：花屏，
+BlackWhiteEdge：黑白边，
+SolidColorScreen：纯色屏，
+Noise：噪点，
+Mosaic：马赛克，
+QRCode：二维码，
+AppletCode：小程序码，
+BarCode：条形码，
+LowVoice：低音，
+HighVoice：爆音，
+NoVoice：静音，
+LowEvaluation：无参考打分低于阈值。
+        :type Type: str
+        :param QualityControlItems: 质检结果项。
+        :type QualityControlItems: list of QualityControlItem
+        """
+        self.Type = None
+        self.QualityControlItems = None
+
+
+    def _deserialize(self, params):
+        self.Type = params.get("Type")
+        if params.get("QualityControlItems") is not None:
+            self.QualityControlItems = []
+            for item in params.get("QualityControlItems"):
+                obj = QualityControlItem()
+                obj._deserialize(item)
+                self.QualityControlItems.append(obj)
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class RTMPAddressDestination(AbstractModel):
     """RTMP转推的目标地址信息。
 
     """
 
     def __init__(self):
         r"""
@@ -17562,14 +17931,63 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class ScheduleQualityControlTaskResult(AbstractModel):
+    """质检任务结果类型
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Status: 任务状态，有 PROCESSING，SUCCESS 和 FAIL 三种。
+        :type Status: str
+        :param ErrCodeExt: 错误码，空字符串表示成功，其他值表示失败，取值请参考 [媒体处理类错误码](https://cloud.tencent.com/document/product/862/50369#.E8.A7.86.E9.A2.91.E5.A4.84.E7.90.86.E7.B1.BB.E9.94.99.E8.AF.AF.E7.A0.81) 列表。
+        :type ErrCodeExt: str
+        :param ErrCode: 错误码，0 表示成功，其他值表示失败（该字段已不推荐使用，建议使用新的错误码字段 ErrCodeExt）。
+        :type ErrCode: int
+        :param Message: 错误信息。
+        :type Message: str
+        :param Input: 质检任务的输入。
+        :type Input: :class:`tencentcloud.mps.v20190612.models.AiQualityControlTaskInput`
+        :param Output: 质检任务的输出。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Output: :class:`tencentcloud.mps.v20190612.models.QualityControlData`
+        """
+        self.Status = None
+        self.ErrCodeExt = None
+        self.ErrCode = None
+        self.Message = None
+        self.Input = None
+        self.Output = None
+
+
+    def _deserialize(self, params):
+        self.Status = params.get("Status")
+        self.ErrCodeExt = params.get("ErrCodeExt")
+        self.ErrCode = params.get("ErrCode")
+        self.Message = params.get("Message")
+        if params.get("Input") is not None:
+            self.Input = AiQualityControlTaskInput()
+            self.Input._deserialize(params.get("Input"))
+        if params.get("Output") is not None:
+            self.Output = QualityControlData()
+            self.Output._deserialize(params.get("Output"))
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class ScheduleRecognitionTaskResult(AbstractModel):
     """编排视频识别任务结果类型
 
     """
 
     def __init__(self):
         r"""
@@ -17679,34 +18097,42 @@
         r"""
         :param TaskId: 编排任务 ID。
         :type TaskId: str
         :param Status: 任务流状态，取值：
 <li>PROCESSING：处理中；</li>
 <li>FINISH：已完成。</li>
         :type Status: str
+        :param ErrCode: 源异常时返回非0错误码，返回0 时请使用各个具体任务的 ErrCode。
+        :type ErrCode: int
+        :param Message: 源异常时返回对应异常Message，否则请使用各个具体任务的 Message。
+        :type Message: str
         :param InputInfo: 媒体处理的目标文件信息。
 注意：此字段可能返回 null，表示取不到有效值。
         :type InputInfo: :class:`tencentcloud.mps.v20190612.models.MediaInputInfo`
         :param MetaData: 原始视频的元信息。
 注意：此字段可能返回 null，表示取不到有效值。
         :type MetaData: :class:`tencentcloud.mps.v20190612.models.MediaMetaData`
         :param ActivityResultSet: 编排任务输出。
 注意：此字段可能返回 null，表示取不到有效值。
         :type ActivityResultSet: list of ActivityResult
         """
         self.TaskId = None
         self.Status = None
+        self.ErrCode = None
+        self.Message = None
         self.InputInfo = None
         self.MetaData = None
         self.ActivityResultSet = None
 
 
     def _deserialize(self, params):
         self.TaskId = params.get("TaskId")
         self.Status = params.get("Status")
+        self.ErrCode = params.get("ErrCode")
+        self.Message = params.get("Message")
         if params.get("InputInfo") is not None:
             self.InputInfo = MediaInputInfo()
             self.InputInfo._deserialize(params.get("InputInfo"))
         if params.get("MetaData") is not None:
             self.MetaData = MediaMetaData()
             self.MetaData._deserialize(params.get("MetaData"))
         if params.get("ActivityResultSet") is not None:
@@ -20036,25 +20462,29 @@
         :type MediaProcessResultSet: list of MediaProcessTaskResult
         :param AiContentReviewResultSet: 视频内容审核任务的执行状态与结果。
         :type AiContentReviewResultSet: list of AiContentReviewResult
         :param AiAnalysisResultSet: 视频内容分析任务的执行状态与结果。
         :type AiAnalysisResultSet: list of AiAnalysisResult
         :param AiRecognitionResultSet: 视频内容识别任务的执行状态与结果。
         :type AiRecognitionResultSet: list of AiRecognitionResult
+        :param AiQualityControlTaskResult: 视频质检任务的执行状态与结果。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type AiQualityControlTaskResult: :class:`tencentcloud.mps.v20190612.models.ScheduleQualityControlTaskResult`
         """
         self.TaskId = None
         self.Status = None
         self.ErrCode = None
         self.Message = None
         self.InputInfo = None
         self.MetaData = None
         self.MediaProcessResultSet = None
         self.AiContentReviewResultSet = None
         self.AiAnalysisResultSet = None
         self.AiRecognitionResultSet = None
+        self.AiQualityControlTaskResult = None
 
 
     def _deserialize(self, params):
         self.TaskId = params.get("TaskId")
         self.Status = params.get("Status")
         self.ErrCode = params.get("ErrCode")
         self.Message = params.get("Message")
@@ -20084,14 +20514,17 @@
                 self.AiAnalysisResultSet.append(obj)
         if params.get("AiRecognitionResultSet") is not None:
             self.AiRecognitionResultSet = []
             for item in params.get("AiRecognitionResultSet"):
                 obj = AiRecognitionResult()
                 obj._deserialize(item)
                 self.AiRecognitionResultSet.append(obj)
+        if params.get("AiQualityControlTaskResult") is not None:
+            self.AiQualityControlTaskResult = ScheduleQualityControlTaskResult()
+            self.AiQualityControlTaskResult._deserialize(params.get("AiQualityControlTaskResult"))
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
```

### Comparing `tencentcloud-sdk-python-mps-3.0.867/PKG-INFO` & `tencentcloud-sdk-python-mps-3.0.868/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-mps
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Mps SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-mps-3.0.867/README.rst` & `tencentcloud-sdk-python-mps-3.0.868/README.rst`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mps-3.0.867/tencentcloud_sdk_python_mps.egg-info/PKG-INFO` & `tencentcloud-sdk-python-mps-3.0.868/tencentcloud_sdk_python_mps.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-mps
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Mps SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

