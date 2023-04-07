# Comparing `tmp/tencentcloud-sdk-python-vod-3.0.867.tar.gz` & `tmp/tencentcloud-sdk-python-vod-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-vod-3.0.867.tar", last modified: Wed Apr  5 17:00:14 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-vod-3.0.868.tar", last modified: Fri Apr  7 01:05:03 2023, max compression
```

## Comparing `tencentcloud-sdk-python-vod-3.0.867.tar` & `tencentcloud-sdk-python-vod-3.0.868.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/
--rw-r--r--   0 root         (0) root         (0)     1006 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/v20180717/
--rw-r--r--   0 root         (0) root         (0)   172361 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/v20180717/vod_client.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/v20180717/__init__.py
--rw-r--r--   0 root         (0) root         (0)    25016 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/v20180717/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)  1167656 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/v20180717/models.py
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud/__init__.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      737 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud_sdk_python_vod.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud_sdk_python_vod.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      445 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud_sdk_python_vod.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud_sdk_python_vod.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 17:00:14.000000 tencentcloud-sdk-python-vod-3.0.867/tencentcloud_sdk_python_vod.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud/
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/v20180717/
+-rw-r--r--   0 root         (0) root         (0)   172410 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/v20180717/vod_client.py
+-rw-r--r--   0 root         (0) root         (0)  1169017 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/v20180717/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/v20180717/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    25016 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/v20180717/errorcodes.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud_sdk_python_vod.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud_sdk_python_vod.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud_sdk_python_vod.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud_sdk_python_vod.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      445 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/tencentcloud_sdk_python_vod.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)      737 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/README.rst
+-rw-r--r--   0 root         (0) root         (0)     1006 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 01:05:03.000000 tencentcloud-sdk-python-vod-3.0.868/setup.cfg
```

### Comparing `tencentcloud-sdk-python-vod-3.0.867/setup.py` & `tencentcloud-sdk-python-vod-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/v20180717/vod_client.py` & `tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/v20180717/vod_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -318,15 +318,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def CreateImageProcessingTemplate(self, request):
-        """创建一个用户自定义的图片处理模板，数量上限：16。最多支持三次操作，例如：裁剪-缩略-裁剪。
+        """创建一个用户自定义的图片处理模板，数量上限：16。最多支持十次操作，例如：裁剪-缩略-裁剪-模糊-缩略-裁剪-缩略-裁剪-模糊-缩略。
 
         :param request: Request instance for CreateImageProcessingTemplate.
         :type request: :class:`tencentcloud.vod.v20180717.models.CreateImageProcessingTemplateRequest`
         :rtype: :class:`tencentcloud.vod.v20180717.models.CreateImageProcessingTemplateResponse`
 
         """
         try:
@@ -410,15 +410,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def CreateRebuildMediaTemplate(self, request):
-        """创建音画质重生模版。
+        """创建音画质重生模板。
 
         :param request: Request instance for CreateRebuildMediaTemplate.
         :type request: :class:`tencentcloud.vod.v20180717.models.CreateRebuildMediaTemplateRequest`
         :rtype: :class:`tencentcloud.vod.v20180717.models.CreateRebuildMediaTemplateResponse`
 
         """
         try:
@@ -975,15 +975,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def DeleteRebuildMediaTemplate(self, request):
-        """删除音画质重生模版。
+        """删除音画质重生模板。
 
         :param request: Request instance for DeleteRebuildMediaTemplate.
         :type request: :class:`tencentcloud.vod.v20180717.models.DeleteRebuildMediaTemplateRequest`
         :rtype: :class:`tencentcloud.vod.v20180717.models.DeleteRebuildMediaTemplateResponse`
 
         """
         try:
@@ -1936,15 +1936,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def DescribeRebuildMediaTemplates(self, request):
-        """获取音画质重生模版列表。
+        """获取音画质重生模板列表。
 
         :param request: Request instance for DescribeRebuildMediaTemplates.
         :type request: :class:`tencentcloud.vod.v20180717.models.DescribeRebuildMediaTemplatesRequest`
         :rtype: :class:`tencentcloud.vod.v20180717.models.DescribeRebuildMediaTemplatesResponse`
 
         """
         try:
@@ -2837,15 +2837,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def ModifyRebuildMediaTemplate(self, request):
-        """修改音画质重生模版。
+        """修改音画质重生模板。
 
         :param request: Request instance for ModifyRebuildMediaTemplate.
         :type request: :class:`tencentcloud.vod.v20180717.models.ModifyRebuildMediaTemplateRequest`
         :rtype: :class:`tencentcloud.vod.v20180717.models.ModifyRebuildMediaTemplateResponse`
 
         """
         try:
@@ -3381,15 +3381,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def RebuildMediaByTemplate(self, request):
-        """使用模版发起音画质重生。
+        """使用模板发起音画质重生。
 
         :param request: Request instance for RebuildMediaByTemplate.
         :type request: :class:`tencentcloud.vod.v20180717.models.RebuildMediaByTemplateRequest`
         :rtype: :class:`tencentcloud.vod.v20180717.models.RebuildMediaByTemplateResponse`
 
         """
         try:
```

### Comparing `tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/v20180717/errorcodes.py` & `tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/v20180717/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-vod-3.0.867/tencentcloud/vod/v20180717/models.py` & `tencentcloud-sdk-python-vod-3.0.868/tencentcloud/vod/v20180717/models.py`

 * *Files 1% similar despite different names*

```diff
@@ -6705,15 +6705,15 @@
     """CreateImageProcessingTemplate请求参数结构体
 
     """
 
     def __init__(self):
         r"""
         :param Operations: 图片处理操作数组，操作将以其在数组中的顺序执行。
-<li>长度限制：3。</li>
+<li>长度限制：10。</li>
         :type Operations: list of ImageOperation
         :param SubAppId: <b>点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。</b>
         :type SubAppId: int
         :param Name: 图片处理模板名称，长度限制：64 个字符。
         :type Name: str
         :param Comment: 模板描述信息，长度限制：256 个字符。
         :type Comment: str
@@ -7100,17 +7100,17 @@
 
     def __init__(self):
         r"""
         :param Container: 输出文件封装格式，可选值：mp4、flv、hls。
         :type Container: str
         :param SubAppId: <b>点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。</b>
         :type SubAppId: int
-        :param Name: 音画质重生模版名称。
+        :param Name: 音画质重生模板名称。
         :type Name: str
-        :param Comment: 模版描述。
+        :param Comment: 模板描述。
         :type Comment: str
         :param RebuildVideoInfo: 音画质重生视频控制控制信息。
         :type RebuildVideoInfo: :class:`tencentcloud.vod.v20180717.models.RebuildVideoInfo`
         :param RebuildAudioInfo: 音画质重生音频控制控制信息。
         :type RebuildAudioInfo: :class:`tencentcloud.vod.v20180717.models.RebuildAudioInfo`
         :param TargetVideoInfo: 输出目标视频控制信息。
         :type TargetVideoInfo: :class:`tencentcloud.vod.v20180717.models.RebuildMediaTargetVideoStream`
@@ -7170,15 +7170,15 @@
 class CreateRebuildMediaTemplateResponse(AbstractModel):
     """CreateRebuildMediaTemplate返回参数结构体
 
     """
 
     def __init__(self):
         r"""
-        :param Definition: 音画质重生模版 ID。
+        :param Definition: 音画质重生模板 ID。
         :type Definition: int
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
         self.Definition = None
         self.RequestId = None
 
@@ -8630,15 +8630,15 @@
 class DeleteRebuildMediaTemplateRequest(AbstractModel):
     """DeleteRebuildMediaTemplate请求参数结构体
 
     """
 
     def __init__(self):
         r"""
-        :param Definition: 音画质重生模版号。
+        :param Definition: 音画质重生模板号。
         :type Definition: int
         :param SubAppId: <b>点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。</b>
         :type SubAppId: int
         """
         self.Definition = None
         self.SubAppId = None
 
@@ -11128,15 +11128,15 @@
 class DescribeRebuildMediaTemplatesRequest(AbstractModel):
     """DescribeRebuildMediaTemplates请求参数结构体
 
     """
 
     def __init__(self):
         r"""
-        :param Definitions: 音画质重生模版列表。
+        :param Definitions: 音画质重生模板列表。
         :type Definitions: list of int
         :param SubAppId: <b>点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。</b>
         :type SubAppId: int
         :param Type: 模板类型过滤条件，可选值：
 <li>Preset：系统预置模板；</li>
 <li>Custom：用户自定义模板。</li>
         :type Type: str
@@ -14256,14 +14256,47 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class ImageBlur(AbstractModel):
+    """图片模糊处理。
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Type: 图片模糊的操作类型。可选模式有：
+<li>Gaussian : 高斯模糊。</li>
+        :type Type: str
+        :param Radius: 模糊半径，取值范围为1 - 50。当 Type 取值为 Gaussian 时此字段有效。
+        :type Radius: int
+        :param Sigma: 正态分布的标准差，必须大于0。当 Type 取值为 Gaussian 时此字段有效。
+        :type Sigma: int
+        """
+        self.Type = None
+        self.Radius = None
+        self.Sigma = None
+
+
+    def _deserialize(self, params):
+        self.Type = params.get("Type")
+        self.Radius = params.get("Radius")
+        self.Sigma = params.get("Sigma")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class ImageCenterCut(AbstractModel):
     """图片中心裁剪处理。
 
     """
 
     def __init__(self):
         r"""
@@ -14334,28 +14367,34 @@
 <li>Scale : 图片缩略处理。</li>
 <li>CenterCut : 图片裁剪处理。</li>
         :type Type: str
         :param Scale: 图片缩略处理，仅当 Type 为 Scale 时有效。
         :type Scale: :class:`tencentcloud.vod.v20180717.models.ImageScale`
         :param CenterCut: 图片裁剪处理，仅当 Type 为 CenterCut 时有效。
         :type CenterCut: :class:`tencentcloud.vod.v20180717.models.ImageCenterCut`
+        :param Blur: 图片模糊处理，仅当 Type 为 Blur 时有效。
+        :type Blur: :class:`tencentcloud.vod.v20180717.models.ImageBlur`
         """
         self.Type = None
         self.Scale = None
         self.CenterCut = None
+        self.Blur = None
 
 
     def _deserialize(self, params):
         self.Type = params.get("Type")
         if params.get("Scale") is not None:
             self.Scale = ImageScale()
             self.Scale._deserialize(params.get("Scale"))
         if params.get("CenterCut") is not None:
             self.CenterCut = ImageCenterCut()
             self.CenterCut._deserialize(params.get("CenterCut"))
+        if params.get("Blur") is not None:
+            self.Blur = ImageBlur()
+            self.Blur._deserialize(params.get("Blur"))
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -18636,21 +18675,21 @@
 class ModifyRebuildMediaTemplateRequest(AbstractModel):
     """ModifyRebuildMediaTemplate请求参数结构体
 
     """
 
     def __init__(self):
         r"""
-        :param Definition: 音画质重生模版号。
+        :param Definition: 音画质重生模板号。
         :type Definition: int
         :param SubAppId: <b>点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。</b>
         :type SubAppId: str
-        :param Name: 音画质重生模版名称。
+        :param Name: 音画质重生模板名称。
         :type Name: str
-        :param Comment: 音画质重生模版描述。
+        :param Comment: 音画质重生模板描述。
         :type Comment: str
         :param RebuildVideoInfo: 音画质重生视频控制信息。
         :type RebuildVideoInfo: :class:`tencentcloud.vod.v20180717.models.RebuildVideoInfo`
         :param RebuildAudioInfo: 音画质重生音频控制信息。
         :type RebuildAudioInfo: :class:`tencentcloud.vod.v20180717.models.RebuildAudioInfo`
         :param TargetVideoInfo: 输出目标视频控制信息。
         :type TargetVideoInfo: :class:`tencentcloud.vod.v20180717.models.RebuildMediaTargetVideoStream`
@@ -22054,15 +22093,15 @@
 
     """
 
     def __init__(self):
         r"""
         :param FileId: 媒体文件 ID。
         :type FileId: str
-        :param Definition: 音画质重生模版 ID。
+        :param Definition: 音画质重生模板 ID。
         :type Definition: int
         :param SubAppId: <b>点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。</b>
         :type SubAppId: str
         :param StartTimeOffset: 起始偏移时间，单位：秒，不填表示从视频开始截取。
         :type StartTimeOffset: float
         :param EndTimeOffset: 结束偏移时间，单位：秒，不填表示截取到视频末尾。
         :type EndTimeOffset: float
@@ -22759,29 +22798,29 @@
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
 class RebuildMediaTemplate(AbstractModel):
-    """音画质重生模版详情。
+    """音画质重生模板详情。
 
     """
 
     def __init__(self):
         r"""
-        :param Definition: 音画质重生模版号。
+        :param Definition: 音画质重生模板号。
         :type Definition: int
         :param Type: 模板类型，可选值：
 <li>Preset：系统预置模板；</li>
 <li>Custom：用户自定义模板。</li>
         :type Type: str
-        :param Name: 音画质重生模版名称。
+        :param Name: 音画质重生模板名称。
         :type Name: str
-        :param Comment: 音画质重生模版描述。
+        :param Comment: 音画质重生模板描述。
         :type Comment: str
         :param RebuildVideoInfo: 音画质重生视频控制信息。
 注意：此字段可能返回 null，表示取不到有效值。
         :type RebuildVideoInfo: :class:`tencentcloud.vod.v20180717.models.RebuildVideoInfo`
         :param RebuildAudioInfo: 音画质重生音频控制信息。
 注意：此字段可能返回 null，表示取不到有效值。
         :type RebuildAudioInfo: :class:`tencentcloud.vod.v20180717.models.RebuildAudioInfo`
```

### Comparing `tencentcloud-sdk-python-vod-3.0.867/tencentcloud/__init__.py` & `tencentcloud-sdk-python-vod-3.0.868/tencentcloud/__init__.py`

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

### Comparing `tencentcloud-sdk-python-vod-3.0.867/PKG-INFO` & `tencentcloud-sdk-python-vod-3.0.868/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-vod
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Vod SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-vod-3.0.867/README.rst` & `tencentcloud-sdk-python-vod-3.0.868/README.rst`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-vod-3.0.867/tencentcloud_sdk_python_vod.egg-info/PKG-INFO` & `tencentcloud-sdk-python-vod-3.0.868/tencentcloud_sdk_python_vod.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-vod
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Vod SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

