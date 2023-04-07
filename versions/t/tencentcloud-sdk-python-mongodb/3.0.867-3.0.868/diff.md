# Comparing `tmp/tencentcloud-sdk-python-mongodb-3.0.867.tar.gz` & `tmp/tencentcloud-sdk-python-mongodb-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-mongodb-3.0.867.tar", last modified: Wed Apr  5 16:44:04 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-mongodb-3.0.868.tar", last modified: Fri Apr  7 00:45:40 2023, max compression
```

## Comparing `tencentcloud-sdk-python-mongodb-3.0.867.tar` & `tencentcloud-sdk-python-mongodb-3.0.868.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/
--rw-r--r--   0 root         (0) root         (0)     1014 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20190725/
--rw-r--r--   0 root         (0) root         (0)    35382 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20190725/mongodb_client.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20190725/__init__.py
--rw-r--r--   0 root         (0) root         (0)     7304 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20190725/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)   146222 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20190725/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20180408/
--rw-r--r--   0 root         (0) root         (0)    13571 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20180408/mongodb_client.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20180408/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3903 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20180408/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)    46677 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20180408/models.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/__init__.py
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/__init__.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1679 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      749 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud_sdk_python_mongodb.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud_sdk_python_mongodb.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      663 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud_sdk_python_mongodb.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1679 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud_sdk_python_mongodb.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 16:44:04.000000 tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud_sdk_python_mongodb.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1679 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20180408/
+-rw-r--r--   0 root         (0) root         (0)    46677 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20180408/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20180408/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    13571 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20180408/mongodb_client.py
+-rw-r--r--   0 root         (0) root         (0)     3903 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20180408/errorcodes.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20190725/
+-rw-r--r--   0 root         (0) root         (0)   146939 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20190725/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20190725/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    35460 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20190725/mongodb_client.py
+-rw-r--r--   0 root         (0) root         (0)     7304 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20190725/errorcodes.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud_sdk_python_mongodb.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1679 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud_sdk_python_mongodb.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud_sdk_python_mongodb.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud_sdk_python_mongodb.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      663 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud_sdk_python_mongodb.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)      749 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/README.rst
+-rw-r--r--   0 root         (0) root         (0)     1014 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 00:45:40.000000 tencentcloud-sdk-python-mongodb-3.0.868/setup.cfg
```

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/setup.py` & `tencentcloud-sdk-python-mongodb-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20190725/mongodb_client.py` & `tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20190725/mongodb_client.py`

 * *Files 1% similar despite different names*

```diff
@@ -345,15 +345,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def DescribeDBInstances(self, request):
-        """本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目ID、实例ID、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。
+        """本接口（DescribeDBInstances）用于查询云数据库实例列表，支持通过项目ID、实例ID、实例状态等过滤条件来筛选主实例、灾备实例和只读实例信息列表。
 
         :param request: Request instance for DescribeDBInstances.
         :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesRequest`
         :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesResponse`
 
         """
         try:
@@ -391,15 +391,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def DescribeSecurityGroup(self, request):
-        """查询实例绑定的安全组
+        """本就口（DescribeSecurityGroup）用于查询实例绑定的安全组。
 
         :param request: Request instance for DescribeSecurityGroup.
         :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSecurityGroupRequest`
         :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSecurityGroupResponse`
 
         """
         try:
@@ -644,15 +644,15 @@
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
     def ModifyDBInstanceSecurityGroup(self, request):
-        """修改实例绑定的安全组
+        """本接口（ModifyDBInstanceSecurityGroup）用于修改实例绑定的安全组
 
         :param request: Request instance for ModifyDBInstanceSecurityGroup.
         :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSecurityGroupRequest`
         :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSecurityGroupResponse`
 
         """
         try:
```

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20190725/errorcodes.py` & `tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20190725/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20190725/models.py` & `tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20190725/models.py`

 * *Files 1% similar despite different names*

```diff
@@ -1489,41 +1489,47 @@
 class DescribeDBInstancesRequest(AbstractModel):
     """DescribeDBInstances请求参数结构体
 
     """
 
     def __init__(self):
         r"""
-        :param InstanceIds: 实例ID列表，格式如：cmgo-p8vnipr5。与云数据库控制台页面中显示的实例ID相同。
+        :param InstanceIds: 实例ID列表。例如：cmgo-p8vn****。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表复制实例 ID。
         :type InstanceIds: list of str
         :param InstanceType: 实例类型。取值范围如下：<ul><li>0：所有实例。</li><li>1：正式实例。</li><li>2：临时实例。</li><li>3：只读实例。</li><li>-1：正式实例、只读、灾备实例。</li></ul>
         :type InstanceType: int
         :param ClusterType: 集群类型，取值范围如下：<ul><li>0：副本集实例。</li><li>1：分片实例。</li><li>-1：所有实例。</li></ul>
         :type ClusterType: int
         :param Status: 实例状态，取值范围如下所示：<ul><li>0：待初始化。</li><li>1：流程执行中。</li><li>2：实例有效。</li><li>-2：已隔离（包年包月实例）。</li><li>-3：已隔离（按量计费实例）。</li></ul>
         :type Status: list of int
-        :param VpcId: 私有网络的ID，基础网络则不传该参数。
+        :param VpcId: 私有网络的 ID。
+- 基础网络则无需配置该参数。
+- 请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表中，单击私有网络名称，在**私有网络**页面获取其 ID。
         :type VpcId: str
-        :param SubnetId: 私有网络的子网ID，基础网络则不传该参数。入参设置该参数的同时，必须设置相应的VpcId。
+        :param SubnetId: 私有网络的子网ID。
+- 基础网络则无需配置该参数。
+- 请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)在实例列表中，单击私有网络名称，在**私有网络**页面获取其子网 ID。
         :type SubnetId: str
         :param PayMode: 付费类型，取值范围如下：<ul><li>0：查询按量计费实例。</li><li>1：查询包年包月实例。</li><li>-1：查询按量计费与包年包月实例。</li></ul>
         :type PayMode: int
         :param Limit: 单次请求返回的数量。默认值为20，取值范围为[1,100]。
         :type Limit: int
         :param Offset: 偏移量，默认值为0。
         :type Offset: int
-        :param OrderBy: 返回结果集排序的字段，目前支持："ProjectId"、"InstanceName"、"CreateTime"，默认为升序排序。
+        :param OrderBy: 配置返回结果排序依据的字段。目前支持依据"ProjectId"、"InstanceName"、"CreateTime"排序。
         :type OrderBy: str
-        :param OrderByType: 返回结果集排序方式，目前支持："ASC"或者"DESC"。
+        :param OrderByType: 配置返回结果的排序方式。
+- ASC：升序。
+- DESC：降序。
         :type OrderByType: str
-        :param ProjectIds: 项目 ID。
+        :param ProjectIds: 项目 ID。请登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)，在右上角的账户信息下拉菜单中，选择项目管理查询项目。
         :type ProjectIds: list of int non-negative
-        :param SearchKey: 搜索关键词，支持实例ID、实例名称、完整IP。
+        :param SearchKey: 配置查询搜索的关键词。支持配置为实例ID、实例名称或者内网 IP 地址。
         :type SearchKey: str
-        :param Tags: Tag信息。
+        :param Tags: 标签信息，包含标签键与标签值。
         :type Tags: list of TagInfo
         """
         self.InstanceIds = None
         self.InstanceType = None
         self.ClusterType = None
         self.Status = None
         self.VpcId = None
@@ -1681,15 +1687,15 @@
 class DescribeSecurityGroupRequest(AbstractModel):
     """DescribeSecurityGroup请求参数结构体
 
     """
 
     def __init__(self):
         r"""
-        :param InstanceId: 实例ID，格式如：cmgo-p8vnipr5。
+        :param InstanceId: 实例 ID。例如：cmgo-p8vn****。
         :type InstanceId: str
         """
         self.InstanceId = None
 
 
     def _deserialize(self, params):
         self.InstanceId = params.get("InstanceId")
@@ -1705,15 +1711,15 @@
 class DescribeSecurityGroupResponse(AbstractModel):
     """DescribeSecurityGroup返回参数结构体
 
     """
 
     def __init__(self):
         r"""
-        :param Groups: 实例绑定的安全组
+        :param Groups: 实例绑定的安全组信息。
         :type Groups: list of SecurityGroup
         :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
         :type RequestId: str
         """
         self.Groups = None
         self.RequestId = None
 
@@ -2848,17 +2854,17 @@
 class ModifyDBInstanceSecurityGroupRequest(AbstractModel):
     """ModifyDBInstanceSecurityGroup请求参数结构体
 
     """
 
     def __init__(self):
         r"""
-        :param InstanceId: 实例ID
+        :param InstanceId: 实例 ID。例如：cmgo-7pje****。
         :type InstanceId: str
-        :param SecurityGroupIds: 目标安全组id
+        :param SecurityGroupIds: 目标安全组 ID。请通过接口[DescribeSecurityGroup](https://cloud.tencent.com/document/product/240/55675)查看具体的安全组 ID。
         :type SecurityGroupIds: list of str
         """
         self.InstanceId = None
         self.SecurityGroupIds = None
 
 
     def _deserialize(self, params):
```

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20180408/mongodb_client.py` & `tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20180408/mongodb_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20180408/errorcodes.py` & `tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20180408/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/mongodb/v20180408/models.py` & `tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/mongodb/v20180408/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud/__init__.py` & `tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud/__init__.py`

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

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/PKG-INFO` & `tencentcloud-sdk-python-mongodb-3.0.868/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-mongodb
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Mongodb SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/README.rst` & `tencentcloud-sdk-python-mongodb-3.0.868/README.rst`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud_sdk_python_mongodb.egg-info/SOURCES.txt` & `tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud_sdk_python_mongodb.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-mongodb-3.0.867/tencentcloud_sdk_python_mongodb.egg-info/PKG-INFO` & `tencentcloud-sdk-python-mongodb-3.0.868/tencentcloud_sdk_python_mongodb.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-mongodb
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Mongodb SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

