# Comparing `tmp/tencentcloud-sdk-python-cwp-3.0.867.tar.gz` & `tmp/tencentcloud-sdk-python-cwp-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-cwp-3.0.867.tar", last modified: Wed Apr  5 16:26:54 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-cwp-3.0.868.tar", last modified: Fri Apr  7 00:25:57 2023, max compression
```

## Comparing `tencentcloud-sdk-python-cwp-3.0.867.tar` & `tencentcloud-sdk-python-cwp-3.0.868.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/
--rw-r--r--   0 root         (0) root         (0)     1006 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/v20180228/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/v20180228/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3900 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/v20180228/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)   858991 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/v20180228/models.py
--rw-r--r--   0 root         (0) root         (0)   243143 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/v20180228/cwp_client.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      737 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud_sdk_python_cwp.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud_sdk_python_cwp.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      445 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud_sdk_python_cwp.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud_sdk_python_cwp.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 16:26:54.000000 tencentcloud-sdk-python-cwp-3.0.867/tencentcloud_sdk_python_cwp.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/v20180228/
+-rw-r--r--   0 root         (0) root         (0)   891318 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/v20180228/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/v20180228/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   249576 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/v20180228/cwp_client.py
+-rw-r--r--   0 root         (0) root         (0)     3900 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/v20180228/errorcodes.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      737 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud_sdk_python_cwp.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud_sdk_python_cwp.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud_sdk_python_cwp.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud_sdk_python_cwp.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      445 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/tencentcloud_sdk_python_cwp.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)     1006 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 00:25:57.000000 tencentcloud-sdk-python-cwp-3.0.868/setup.cfg
```

### Comparing `tencentcloud-sdk-python-cwp-3.0.867/setup.py` & `tencentcloud-sdk-python-cwp-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/__init__.py` & `tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/__init__.py`

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

### Comparing `tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/v20180228/errorcodes.py` & `tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/v20180228/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/v20180228/models.py` & `tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/v20180228/models.py`

 * *Files 1% similar despite different names*

```diff
@@ -42,14 +42,42 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class AlarmInfo(AbstractModel):
+    """节点关联的告警信息
+
+    """
+
+    def __init__(self):
+        r"""
+        :param AlarmId: 该节点关联的告警，告警的table_name+id（t1:id1,t2:id2,...)
+        :type AlarmId: str
+        :param Status: 告警事件表状态，当该节点为告警点时生效
+        :type Status: int
+        """
+        self.AlarmId = None
+        self.Status = None
+
+
+    def _deserialize(self, params):
+        self.AlarmId = params.get("AlarmId")
+        self.Status = params.get("Status")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class AssetAppBaseInfo(AbstractModel):
     """资源管理进程基本信息
 
     """
 
     def __init__(self):
         r"""
@@ -4583,14 +4611,17 @@
         :type InstanceId: str
         :param DataStatus: 0：待处理，1：忽略，5：已处理，6：加入白名单
 注意：此字段可能返回 null，表示取不到有效值。
         :type DataStatus: int
         :param MachineExtraInfo: 附加信息
 注意：此字段可能返回 null，表示取不到有效值。
         :type MachineExtraInfo: :class:`tencentcloud.cwp.v20180228.models.MachineExtraInfo`
+        :param Location: 地理位置中文名
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Location: str
         """
         self.Id = None
         self.Uuid = None
         self.MachineIp = None
         self.MachineName = None
         self.UserName = None
         self.SrcIp = None
@@ -4606,14 +4637,15 @@
         self.IsProVersion = None
         self.Protocol = None
         self.Port = None
         self.ModifyTime = None
         self.InstanceId = None
         self.DataStatus = None
         self.MachineExtraInfo = None
+        self.Location = None
 
 
     def _deserialize(self, params):
         self.Id = params.get("Id")
         self.Uuid = params.get("Uuid")
         self.MachineIp = params.get("MachineIp")
         self.MachineName = params.get("MachineName")
@@ -4633,14 +4665,15 @@
         self.Port = params.get("Port")
         self.ModifyTime = params.get("ModifyTime")
         self.InstanceId = params.get("InstanceId")
         self.DataStatus = params.get("DataStatus")
         if params.get("MachineExtraInfo") is not None:
             self.MachineExtraInfo = MachineExtraInfo()
             self.MachineExtraInfo._deserialize(params.get("MachineExtraInfo"))
+        self.Location = params.get("Location")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -6548,14 +6581,127 @@
             for item in params.get("AccountStatistics"):
                 obj = AccountStatistics()
                 obj._deserialize(item)
                 self.AccountStatistics.append(obj)
         self.RequestId = params.get("RequestId")
 
 
+class DescribeAlarmIncidentNodesRequest(AbstractModel):
+    """DescribeAlarmIncidentNodes请求参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Uuid: 机器uuid
+        :type Uuid: str
+        :param AlarmVid: 告警vid
+        :type AlarmVid: str
+        :param AlarmTime: 告警时间
+        :type AlarmTime: int
+        """
+        self.Uuid = None
+        self.AlarmVid = None
+        self.AlarmTime = None
+
+
+    def _deserialize(self, params):
+        self.Uuid = params.get("Uuid")
+        self.AlarmVid = params.get("AlarmVid")
+        self.AlarmTime = params.get("AlarmTime")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class DescribeAlarmIncidentNodesResponse(AbstractModel):
+    """DescribeAlarmIncidentNodes返回参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param IncidentNodes: 告警点所在事件的所有节点信息,可能包含多事件
+注意：此字段可能返回 null，表示取不到有效值。
+        :type IncidentNodes: list of IncidentVertexInfo
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.IncidentNodes = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("IncidentNodes") is not None:
+            self.IncidentNodes = []
+            for item in params.get("IncidentNodes"):
+                obj = IncidentVertexInfo()
+                obj._deserialize(item)
+                self.IncidentNodes.append(obj)
+        self.RequestId = params.get("RequestId")
+
+
+class DescribeAlarmVertexIdRequest(AbstractModel):
+    """DescribeAlarmVertexId请求参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Uuid: 机器uuid
+        :type Uuid: str
+        :param StartTime: 开始时间戳
+        :type StartTime: int
+        :param EndTime: 结束时间戳
+        :type EndTime: int
+        """
+        self.Uuid = None
+        self.StartTime = None
+        self.EndTime = None
+
+
+    def _deserialize(self, params):
+        self.Uuid = params.get("Uuid")
+        self.StartTime = params.get("StartTime")
+        self.EndTime = params.get("EndTime")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class DescribeAlarmVertexIdResponse(AbstractModel):
+    """DescribeAlarmVertexId返回参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param AlarmVertexIds: 告警点id列表
+注意：此字段可能返回 null，表示取不到有效值。
+        :type AlarmVertexIds: list of str
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.AlarmVertexIds = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.AlarmVertexIds = params.get("AlarmVertexIds")
+        self.RequestId = params.get("RequestId")
+
+
 class DescribeAssetAppListRequest(AbstractModel):
     """DescribeAssetAppList请求参数结构体
 
     """
 
     def __init__(self):
         r"""
@@ -12060,14 +12206,67 @@
                 obj._deserialize(item)
                 self.List.append(obj)
         self.TotalCount = params.get("TotalCount")
         self.ExistsRisk = params.get("ExistsRisk")
         self.RequestId = params.get("RequestId")
 
 
+class DescribeEventByTableRequest(AbstractModel):
+    """DescribeEventByTable请求参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param TableName: 事件表名
+        :type TableName: str
+        :param Ids: 事件表id号
+        :type Ids: list of int
+        """
+        self.TableName = None
+        self.Ids = None
+
+
+    def _deserialize(self, params):
+        self.TableName = params.get("TableName")
+        self.Ids = params.get("Ids")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class DescribeEventByTableResponse(AbstractModel):
+    """DescribeEventByTable返回参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Type: 告警类型，爆破bruteattack，高危命令bash，恶意文件malware，恶意请求risk_dns，本地提权privilege_escalation，反弹shell reverse_shell，内存马java_shell
+        :type Type: str
+        :param Value: 事件内容的json编码字符串，字段结构对齐事件表
+        :type Value: str
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.Type = None
+        self.Value = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        self.Type = params.get("Type")
+        self.Value = params.get("Value")
+        self.RequestId = params.get("RequestId")
+
+
 class DescribeExpertServiceListRequest(AbstractModel):
     """DescribeExpertServiceList请求参数结构体
 
     """
 
     def __init__(self):
         r"""
@@ -14463,14 +14662,62 @@
         self.NonlocalLoginNum = params.get("NonlocalLoginNum")
         self.BruteAttackSuccessNum = params.get("BruteAttackSuccessNum")
         self.VulNum = params.get("VulNum")
         self.BaseLineNum = params.get("BaseLineNum")
         self.RequestId = params.get("RequestId")
 
 
+class DescribePrivilegeEventInfoRequest(AbstractModel):
+    """DescribePrivilegeEventInfo请求参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Id: 事件id
+        :type Id: int
+        """
+        self.Id = None
+
+
+    def _deserialize(self, params):
+        self.Id = params.get("Id")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class DescribePrivilegeEventInfoResponse(AbstractModel):
+    """DescribePrivilegeEventInfo返回参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param PrivilegeEventInfo: 本地提权详情
+注意：此字段可能返回 null，表示取不到有效值。
+        :type PrivilegeEventInfo: :class:`tencentcloud.cwp.v20180228.models.PrivilegeEventInfo`
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.PrivilegeEventInfo = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("PrivilegeEventInfo") is not None:
+            self.PrivilegeEventInfo = PrivilegeEventInfo()
+            self.PrivilegeEventInfo._deserialize(params.get("PrivilegeEventInfo"))
+        self.RequestId = params.get("RequestId")
+
+
 class DescribePrivilegeEventsRequest(AbstractModel):
     """DescribePrivilegeEvents请求参数结构体
 
     """
 
     def __init__(self):
         r"""
@@ -14987,14 +15234,62 @@
             for item in params.get("List"):
                 obj = ProtectNetInfo()
                 obj._deserialize(item)
                 self.List.append(obj)
         self.RequestId = params.get("RequestId")
 
 
+class DescribeReverseShellEventInfoRequest(AbstractModel):
+    """DescribeReverseShellEventInfo请求参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Id: 事件id
+        :type Id: int
+        """
+        self.Id = None
+
+
+    def _deserialize(self, params):
+        self.Id = params.get("Id")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class DescribeReverseShellEventInfoResponse(AbstractModel):
+    """DescribeReverseShellEventInfo返回参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param ReverseShellEventInfo: 反弹shell详情信息
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ReverseShellEventInfo: :class:`tencentcloud.cwp.v20180228.models.ReverseShellEventInfo`
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.ReverseShellEventInfo = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("ReverseShellEventInfo") is not None:
+            self.ReverseShellEventInfo = ReverseShellEventInfo()
+            self.ReverseShellEventInfo._deserialize(params.get("ReverseShellEventInfo"))
+        self.RequestId = params.get("RequestId")
+
+
 class DescribeReverseShellEventsRequest(AbstractModel):
     """DescribeReverseShellEvents请求参数结构体
 
     """
 
     def __init__(self):
         r"""
@@ -15131,14 +15426,62 @@
                 obj = ReverseShellRule()
                 obj._deserialize(item)
                 self.List.append(obj)
         self.TotalCount = params.get("TotalCount")
         self.RequestId = params.get("RequestId")
 
 
+class DescribeRiskDnsEventInfoRequest(AbstractModel):
+    """DescribeRiskDnsEventInfo请求参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Id: 恶意请求事件Id
+        :type Id: int
+        """
+        self.Id = None
+
+
+    def _deserialize(self, params):
+        self.Id = params.get("Id")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class DescribeRiskDnsEventInfoResponse(AbstractModel):
+    """DescribeRiskDnsEventInfo返回参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Info: 恶意请求事件详情
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Info: :class:`tencentcloud.cwp.v20180228.models.RiskDnsEvent`
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.Info = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("Info") is not None:
+            self.Info = RiskDnsEvent()
+            self.Info._deserialize(params.get("Info"))
+        self.RequestId = params.get("RequestId")
+
+
 class DescribeRiskDnsEventListRequest(AbstractModel):
     """DescribeRiskDnsEventList请求参数结构体
 
     """
 
     def __init__(self):
         r"""
@@ -16802,14 +17145,73 @@
         self.BasicVersionNum = params.get("BasicVersionNum")
         self.ProVersionNum = params.get("ProVersionNum")
         self.UltimateVersionNum = params.get("UltimateVersionNum")
         self.GeneralVersionNum = params.get("GeneralVersionNum")
         self.RequestId = params.get("RequestId")
 
 
+class DescribeVertexDetailRequest(AbstractModel):
+    """DescribeVertexDetail请求参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param VertexIds: 点id列表
+        :type VertexIds: list of str
+        :param IncidentId: 事件id
+        :type IncidentId: str
+        :param TableName: 事件所在表名
+        :type TableName: str
+        """
+        self.VertexIds = None
+        self.IncidentId = None
+        self.TableName = None
+
+
+    def _deserialize(self, params):
+        self.VertexIds = params.get("VertexIds")
+        self.IncidentId = params.get("IncidentId")
+        self.TableName = params.get("TableName")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class DescribeVertexDetailResponse(AbstractModel):
+    """DescribeVertexDetail返回参数结构体
+
+    """
+
+    def __init__(self):
+        r"""
+        :param VertexDetails: 指定点列表的属性信息
+注意：此字段可能返回 null，表示取不到有效值。
+        :type VertexDetails: list of VertexDetail
+        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
+        :type RequestId: str
+        """
+        self.VertexDetails = None
+        self.RequestId = None
+
+
+    def _deserialize(self, params):
+        if params.get("VertexDetails") is not None:
+            self.VertexDetails = []
+            for item in params.get("VertexDetails"):
+                obj = VertexDetail()
+                obj._deserialize(item)
+                self.VertexDetails.append(obj)
+        self.RequestId = params.get("RequestId")
+
+
 class DescribeVulCountByDatesRequest(AbstractModel):
     """DescribeVulCountByDates请求参数结构体
 
     """
 
     def __init__(self):
         r"""
@@ -20121,14 +20523,17 @@
 ABROAD - 海外IP；
 XTI - 威胁情报
 注意：此字段可能返回 null，表示取不到有效值。
         :type Desc: str
         :param MachineExtraInfo: 附加信息
 注意：此字段可能返回 null，表示取不到有效值。
         :type MachineExtraInfo: :class:`tencentcloud.cwp.v20180228.models.MachineExtraInfo`
+        :param Port: 请求目的端口
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Port: int
         """
         self.Id = None
         self.Uuid = None
         self.MachineIp = None
         self.MachineName = None
         self.UserName = None
         self.SrcIp = None
@@ -20143,14 +20548,15 @@
         self.IsRiskTime = None
         self.IsRiskSrcIp = None
         self.RiskLevel = None
         self.Location = None
         self.Quuid = None
         self.Desc = None
         self.MachineExtraInfo = None
+        self.Port = None
 
 
     def _deserialize(self, params):
         self.Id = params.get("Id")
         self.Uuid = params.get("Uuid")
         self.MachineIp = params.get("MachineIp")
         self.MachineName = params.get("MachineName")
@@ -20169,14 +20575,15 @@
         self.RiskLevel = params.get("RiskLevel")
         self.Location = params.get("Location")
         self.Quuid = params.get("Quuid")
         self.Desc = params.get("Desc")
         if params.get("MachineExtraInfo") is not None:
             self.MachineExtraInfo = MachineExtraInfo()
             self.MachineExtraInfo._deserialize(params.get("MachineExtraInfo"))
+        self.Port = params.get("Port")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -20364,14 +20771,59 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class IncidentVertexInfo(AbstractModel):
+    """事件点信息
+
+    """
+
+    def __init__(self):
+        r"""
+        :param IncidentId: 事件id
+注意：此字段可能返回 null，表示取不到有效值。
+        :type IncidentId: str
+        :param TableName: 事件所在表名
+注意：此字段可能返回 null，表示取不到有效值。
+        :type TableName: str
+        :param Vertex: 节点信息列表，数组项中包含节点详细信息
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Vertex: list of VertexInfo
+        :param VertexCount: 节点总个数
+注意：此字段可能返回 null，表示取不到有效值。
+        :type VertexCount: int
+        """
+        self.IncidentId = None
+        self.TableName = None
+        self.Vertex = None
+        self.VertexCount = None
+
+
+    def _deserialize(self, params):
+        self.IncidentId = params.get("IncidentId")
+        self.TableName = params.get("TableName")
+        if params.get("Vertex") is not None:
+            self.Vertex = []
+            for item in params.get("Vertex"):
+                obj = VertexInfo()
+                obj._deserialize(item)
+                self.Vertex.append(obj)
+        self.VertexCount = params.get("VertexCount")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class Item(AbstractModel):
     """项
 
     """
 
     def __init__(self):
         r"""
@@ -22635,14 +23087,17 @@
         :param CreateTime: 发生时间
         :type CreateTime: str
         :param MachineName: 机器名
         :type MachineName: str
         :param MachineExtraInfo: 附加信息
 注意：此字段可能返回 null，表示取不到有效值。
         :type MachineExtraInfo: :class:`tencentcloud.cwp.v20180228.models.MachineExtraInfo`
+        :param Pid: 进程id
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Pid: int
         """
         self.Id = None
         self.Uuid = None
         self.Quuid = None
         self.Hostip = None
         self.ProcessName = None
         self.FullPath = None
@@ -22655,14 +23110,15 @@
         self.ParentProcGroup = None
         self.ParentProcPath = None
         self.ProcTree = None
         self.Status = None
         self.CreateTime = None
         self.MachineName = None
         self.MachineExtraInfo = None
+        self.Pid = None
 
 
     def _deserialize(self, params):
         self.Id = params.get("Id")
         self.Uuid = params.get("Uuid")
         self.Quuid = params.get("Quuid")
         self.Hostip = params.get("Hostip")
@@ -22679,14 +23135,139 @@
         self.ProcTree = params.get("ProcTree")
         self.Status = params.get("Status")
         self.CreateTime = params.get("CreateTime")
         self.MachineName = params.get("MachineName")
         if params.get("MachineExtraInfo") is not None:
             self.MachineExtraInfo = MachineExtraInfo()
             self.MachineExtraInfo._deserialize(params.get("MachineExtraInfo"))
+        self.Pid = params.get("Pid")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class PrivilegeEventInfo(AbstractModel):
+    """本地提权数据
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Id: 数据ID
+        :type Id: int
+        :param Uuid: 云镜ID
+        :type Uuid: str
+        :param Quuid: 主机ID
+        :type Quuid: str
+        :param HostIp: 主机内网IP
+        :type HostIp: str
+        :param ProcessName: 进程名
+        :type ProcessName: str
+        :param FullPath: 进程路径
+        :type FullPath: str
+        :param CmdLine: 执行命令
+        :type CmdLine: str
+        :param UserName: 用户名
+        :type UserName: str
+        :param UserGroup: 用户组
+        :type UserGroup: str
+        :param ProcFilePrivilege: 进程文件权限
+        :type ProcFilePrivilege: str
+        :param ParentProcName: 父进程名
+        :type ParentProcName: str
+        :param ParentProcUser: 父进程用户名
+        :type ParentProcUser: str
+        :param ParentProcGroup: 父进程用户组
+        :type ParentProcGroup: str
+        :param ParentProcPath: 父进程路径
+        :type ParentProcPath: str
+        :param PsTree: 进程树 json  pid:进程id，exe:文件路径 ，account:进程所属用组和用户 ,cmdline:执行命令，ssh_service: SSH服务ip, ssh_soure:登录源
+        :type PsTree: str
+        :param Status: 处理状态：0-待处理 2-白名单 3-已处理 4-已忽略
+        :type Status: int
+        :param CreateTime: 发生时间
+        :type CreateTime: str
+        :param MachineName: 机器名
+        :type MachineName: str
+        :param SuggestScheme: 建议方案
+        :type SuggestScheme: str
+        :param HarmDescribe: 危害描述信息
+        :type HarmDescribe: str
+        :param Tags: 标签
+        :type Tags: list of str
+        :param References: 参考链接
+        :type References: list of str
+        :param MachineWanIp: 主机外网ip
+        :type MachineWanIp: str
+        :param NewCaps: 权限列表|隔开
+        :type NewCaps: str
+        :param MachineStatus: 主机在线状态 OFFLINE  ONLINE
+        :type MachineStatus: str
+        :param ModifyTime: 处理时间
+        :type ModifyTime: str
+        """
+        self.Id = None
+        self.Uuid = None
+        self.Quuid = None
+        self.HostIp = None
+        self.ProcessName = None
+        self.FullPath = None
+        self.CmdLine = None
+        self.UserName = None
+        self.UserGroup = None
+        self.ProcFilePrivilege = None
+        self.ParentProcName = None
+        self.ParentProcUser = None
+        self.ParentProcGroup = None
+        self.ParentProcPath = None
+        self.PsTree = None
+        self.Status = None
+        self.CreateTime = None
+        self.MachineName = None
+        self.SuggestScheme = None
+        self.HarmDescribe = None
+        self.Tags = None
+        self.References = None
+        self.MachineWanIp = None
+        self.NewCaps = None
+        self.MachineStatus = None
+        self.ModifyTime = None
+
+
+    def _deserialize(self, params):
+        self.Id = params.get("Id")
+        self.Uuid = params.get("Uuid")
+        self.Quuid = params.get("Quuid")
+        self.HostIp = params.get("HostIp")
+        self.ProcessName = params.get("ProcessName")
+        self.FullPath = params.get("FullPath")
+        self.CmdLine = params.get("CmdLine")
+        self.UserName = params.get("UserName")
+        self.UserGroup = params.get("UserGroup")
+        self.ProcFilePrivilege = params.get("ProcFilePrivilege")
+        self.ParentProcName = params.get("ParentProcName")
+        self.ParentProcUser = params.get("ParentProcUser")
+        self.ParentProcGroup = params.get("ParentProcGroup")
+        self.ParentProcPath = params.get("ParentProcPath")
+        self.PsTree = params.get("PsTree")
+        self.Status = params.get("Status")
+        self.CreateTime = params.get("CreateTime")
+        self.MachineName = params.get("MachineName")
+        self.SuggestScheme = params.get("SuggestScheme")
+        self.HarmDescribe = params.get("HarmDescribe")
+        self.Tags = params.get("Tags")
+        self.References = params.get("References")
+        self.MachineWanIp = params.get("MachineWanIp")
+        self.NewCaps = params.get("NewCaps")
+        self.MachineStatus = params.get("MachineStatus")
+        self.ModifyTime = params.get("ModifyTime")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -23362,14 +23943,17 @@
         :param ProcTree: 进程树
         :type ProcTree: str
         :param DetectBy: 检测方法
         :type DetectBy: int
         :param MachineExtraInfo:  主机额外信息
 注意：此字段可能返回 null，表示取不到有效值。
         :type MachineExtraInfo: :class:`tencentcloud.cwp.v20180228.models.MachineExtraInfo`
+        :param Pid: 进程id
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Pid: int
         """
         self.Id = None
         self.Uuid = None
         self.Quuid = None
         self.Hostip = None
         self.DstIp = None
         self.DstPort = None
@@ -23384,14 +23968,15 @@
         self.ParentProcPath = None
         self.Status = None
         self.CreateTime = None
         self.MachineName = None
         self.ProcTree = None
         self.DetectBy = None
         self.MachineExtraInfo = None
+        self.Pid = None
 
 
     def _deserialize(self, params):
         self.Id = params.get("Id")
         self.Uuid = params.get("Uuid")
         self.Quuid = params.get("Quuid")
         self.Hostip = params.get("Hostip")
@@ -23410,14 +23995,144 @@
         self.CreateTime = params.get("CreateTime")
         self.MachineName = params.get("MachineName")
         self.ProcTree = params.get("ProcTree")
         self.DetectBy = params.get("DetectBy")
         if params.get("MachineExtraInfo") is not None:
             self.MachineExtraInfo = MachineExtraInfo()
             self.MachineExtraInfo._deserialize(params.get("MachineExtraInfo"))
+        self.Pid = params.get("Pid")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class ReverseShellEventInfo(AbstractModel):
+    """反弹Shell数据详情
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Id: ID 主键
+        :type Id: int
+        :param Uuid: 云镜UUID
+        :type Uuid: str
+        :param Quuid: 主机ID
+        :type Quuid: str
+        :param HostIp: 主机内网IP
+        :type HostIp: str
+        :param DstIp: 目标IP
+        :type DstIp: str
+        :param DstPort: 目标端口
+        :type DstPort: int
+        :param ProcessName: 进程名
+        :type ProcessName: str
+        :param FullPath: 进程路径
+        :type FullPath: str
+        :param CmdLine: 命令详情
+        :type CmdLine: str
+        :param UserName: 执行用户
+        :type UserName: str
+        :param UserGroup: 执行用户组
+        :type UserGroup: str
+        :param ParentProcName: 父进程名
+        :type ParentProcName: str
+        :param ParentProcUser: 父进程用户
+        :type ParentProcUser: str
+        :param ParentProcGroup: 父进程用户组
+        :type ParentProcGroup: str
+        :param ParentProcPath: 父进程路径
+        :type ParentProcPath: str
+        :param Status: 处理状态：0-待处理 2-白名单 3-已处理 4-已忽略
+        :type Status: int
+        :param CreateTime: 产生时间
+        :type CreateTime: str
+        :param MachineName: 主机名
+        :type MachineName: str
+        :param DetectBy: 检测方法
+        :type DetectBy: int
+        :param PsTree: 进程树 json  pid:进程id，exe:文件路径 ，account:进程所属用组和用户 ,cmdline:执行命令，ssh_service: SSH服务ip, ssh_soure:登录源
+注意：此字段可能返回 null，表示取不到有效值。
+        :type PsTree: str
+        :param SuggestScheme: 建议方案
+        :type SuggestScheme: str
+        :param HarmDescribe: 描述
+        :type HarmDescribe: str
+        :param Tags: 标签
+        :type Tags: list of str
+        :param References: 参考链接
+        :type References: list of str
+        :param MachineWanIp: 主机外网ip
+        :type MachineWanIp: str
+        :param MachineStatus: 主机在线状态 OFFLINE  ONLINE
+        :type MachineStatus: str
+        :param ModifyTime: 处理时间
+        :type ModifyTime: str
+        """
+        self.Id = None
+        self.Uuid = None
+        self.Quuid = None
+        self.HostIp = None
+        self.DstIp = None
+        self.DstPort = None
+        self.ProcessName = None
+        self.FullPath = None
+        self.CmdLine = None
+        self.UserName = None
+        self.UserGroup = None
+        self.ParentProcName = None
+        self.ParentProcUser = None
+        self.ParentProcGroup = None
+        self.ParentProcPath = None
+        self.Status = None
+        self.CreateTime = None
+        self.MachineName = None
+        self.DetectBy = None
+        self.PsTree = None
+        self.SuggestScheme = None
+        self.HarmDescribe = None
+        self.Tags = None
+        self.References = None
+        self.MachineWanIp = None
+        self.MachineStatus = None
+        self.ModifyTime = None
+
+
+    def _deserialize(self, params):
+        self.Id = params.get("Id")
+        self.Uuid = params.get("Uuid")
+        self.Quuid = params.get("Quuid")
+        self.HostIp = params.get("HostIp")
+        self.DstIp = params.get("DstIp")
+        self.DstPort = params.get("DstPort")
+        self.ProcessName = params.get("ProcessName")
+        self.FullPath = params.get("FullPath")
+        self.CmdLine = params.get("CmdLine")
+        self.UserName = params.get("UserName")
+        self.UserGroup = params.get("UserGroup")
+        self.ParentProcName = params.get("ParentProcName")
+        self.ParentProcUser = params.get("ParentProcUser")
+        self.ParentProcGroup = params.get("ParentProcGroup")
+        self.ParentProcPath = params.get("ParentProcPath")
+        self.Status = params.get("Status")
+        self.CreateTime = params.get("CreateTime")
+        self.MachineName = params.get("MachineName")
+        self.DetectBy = params.get("DetectBy")
+        self.PsTree = params.get("PsTree")
+        self.SuggestScheme = params.get("SuggestScheme")
+        self.HarmDescribe = params.get("HarmDescribe")
+        self.Tags = params.get("Tags")
+        self.References = params.get("References")
+        self.MachineWanIp = params.get("MachineWanIp")
+        self.MachineStatus = params.get("MachineStatus")
+        self.ModifyTime = params.get("ModifyTime")
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
@@ -25108,14 +25823,218 @@
         memeber_set = set(params.keys())
         for name, value in vars(self).items():
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
+
+
+class VertexDetail(AbstractModel):
+    """点详细信息
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Type: 该节点类型，进程:1；网络:2；文件:3；ssh:4
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Type: int
+        :param Time: 各节点类型用到的时间，2022-11-29 00:00:00 格式
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Time: str
+        :param AlarmInfo: 告警信息
+注意：此字段可能返回 null，表示取不到有效值。
+        :type AlarmInfo: list of AlarmInfo
+        :param ProcName: 进程名，当该节点为进程时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ProcName: str
+        :param CmdLine: 命令行，当该节点为进程时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type CmdLine: str
+        :param Pid: 进程id，当该节点为进程时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Pid: str
+        :param FileMd5: 文件md5，当该节点为文件时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type FileMd5: str
+        :param FileContent: 文件写入内容，当该节点为文件时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type FileContent: str
+        :param FilePath: 文件路径，当该节点为文件时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type FilePath: str
+        :param FileCreateTime: 文件创建时间，当该节点为文件时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type FileCreateTime: str
+        :param Address: 请求目的地址，当该节点为网络时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type Address: str
+        :param DstPort: 目标端口，当该节点为网络时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type DstPort: int
+        :param SrcIP: 登录源ip，当该节点为ssh时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type SrcIP: str
+        :param User: 登录用户名用户组，当该节点为ssh时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type User: str
+        :param VulName: 漏洞名称，当该节点为漏洞时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type VulName: str
+        :param VulTime: 漏洞利用时间，当该节点为漏洞时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type VulTime: str
+        :param HttpContent: http请求内容，当该节点为漏洞时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type HttpContent: str
+        :param VulSrcIP: 漏洞利用者来源ip，当该节点为漏洞时生效
+注意：此字段可能返回 null，表示取不到有效值。
+        :type VulSrcIP: str
+        :param VertexId: 点id
+注意：此字段可能返回 null，表示取不到有效值。
+        :type VertexId: str
+        """
+        self.Type = None
+        self.Time = None
+        self.AlarmInfo = None
+        self.ProcName = None
+        self.CmdLine = None
+        self.Pid = None
+        self.FileMd5 = None
+        self.FileContent = None
+        self.FilePath = None
+        self.FileCreateTime = None
+        self.Address = None
+        self.DstPort = None
+        self.SrcIP = None
+        self.User = None
+        self.VulName = None
+        self.VulTime = None
+        self.HttpContent = None
+        self.VulSrcIP = None
+        self.VertexId = None
+
+
+    def _deserialize(self, params):
+        self.Type = params.get("Type")
+        self.Time = params.get("Time")
+        if params.get("AlarmInfo") is not None:
+            self.AlarmInfo = []
+            for item in params.get("AlarmInfo"):
+                obj = AlarmInfo()
+                obj._deserialize(item)
+                self.AlarmInfo.append(obj)
+        self.ProcName = params.get("ProcName")
+        self.CmdLine = params.get("CmdLine")
+        self.Pid = params.get("Pid")
+        self.FileMd5 = params.get("FileMd5")
+        self.FileContent = params.get("FileContent")
+        self.FilePath = params.get("FilePath")
+        self.FileCreateTime = params.get("FileCreateTime")
+        self.Address = params.get("Address")
+        self.DstPort = params.get("DstPort")
+        self.SrcIP = params.get("SrcIP")
+        self.User = params.get("User")
+        self.VulName = params.get("VulName")
+        self.VulTime = params.get("VulTime")
+        self.HttpContent = params.get("HttpContent")
+        self.VulSrcIP = params.get("VulSrcIP")
+        self.VertexId = params.get("VertexId")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class VertexInfo(AbstractModel):
+    """攻击溯源节点信息
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Type: 该结点类型，进程:1；网络:2；文件:3；ssh:4；
+        :type Type: int
+        :param Vid: 该节点包含的vid
+        :type Vid: str
+        :param ParentVid: 该节点的父节点vid
+        :type ParentVid: str
+        :param IsLeaf: 是否叶子
+        :type IsLeaf: bool
+        :param ProcNamePrefix: 进程名，当Type=1时使用
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ProcNamePrefix: str
+        :param ProcNameMd5: 进程名md5，当Type=1时使用
+注意：此字段可能返回 null，表示取不到有效值。
+        :type ProcNameMd5: str
+        :param CmdLinePrefix: 命令行，当Type=1时使用
+注意：此字段可能返回 null，表示取不到有效值。
+        :type CmdLinePrefix: str
+        :param CmdLineMd5: 命令行md5，当Type=1时使用
+注意：此字段可能返回 null，表示取不到有效值。
+        :type CmdLineMd5: str
+        :param FilePathPrefix: 文件路径，当Type=3时使用
+注意：此字段可能返回 null，表示取不到有效值。
+        :type FilePathPrefix: str
+        :param AddressPrefix: 请求目的地址，当Type=2时使用
+注意：此字段可能返回 null，表示取不到有效值。
+        :type AddressPrefix: str
+        :param IsWeDetect: 是否漏洞节点
+        :type IsWeDetect: bool
+        :param IsAlarm: 是否告警节点
+        :type IsAlarm: bool
+        :param FilePathMd5: 文件路径md5，当Type=3时使用
+注意：此字段可能返回 null，表示取不到有效值。
+        :type FilePathMd5: str
+        :param AddressMd5: 请求目的地址md5，当Type=2时使用
+注意：此字段可能返回 null，表示取不到有效值。
+        :type AddressMd5: str
+        """
+        self.Type = None
+        self.Vid = None
+        self.ParentVid = None
+        self.IsLeaf = None
+        self.ProcNamePrefix = None
+        self.ProcNameMd5 = None
+        self.CmdLinePrefix = None
+        self.CmdLineMd5 = None
+        self.FilePathPrefix = None
+        self.AddressPrefix = None
+        self.IsWeDetect = None
+        self.IsAlarm = None
+        self.FilePathMd5 = None
+        self.AddressMd5 = None
+
+
+    def _deserialize(self, params):
+        self.Type = params.get("Type")
+        self.Vid = params.get("Vid")
+        self.ParentVid = params.get("ParentVid")
+        self.IsLeaf = params.get("IsLeaf")
+        self.ProcNamePrefix = params.get("ProcNamePrefix")
+        self.ProcNameMd5 = params.get("ProcNameMd5")
+        self.CmdLinePrefix = params.get("CmdLinePrefix")
+        self.CmdLineMd5 = params.get("CmdLineMd5")
+        self.FilePathPrefix = params.get("FilePathPrefix")
+        self.AddressPrefix = params.get("AddressPrefix")
+        self.IsWeDetect = params.get("IsWeDetect")
+        self.IsAlarm = params.get("IsAlarm")
+        self.FilePathMd5 = params.get("FilePathMd5")
+        self.AddressMd5 = params.get("AddressMd5")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
 
 
 class VulDetailInfo(AbstractModel):
     """漏洞详细信息
 
     """
```

### Comparing `tencentcloud-sdk-python-cwp-3.0.867/tencentcloud/cwp/v20180228/cwp_client.py` & `tencentcloud-sdk-python-cwp-3.0.868/tencentcloud/cwp/v20180228/cwp_client.py`

 * *Files 0% similar despite different names*

```diff
@@ -876,14 +876,60 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def DescribeAlarmIncidentNodes(self, request):
+        """获取告警点所在事件的所有节点信息
+
+        :param request: Request instance for DescribeAlarmIncidentNodes.
+        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmIncidentNodesRequest`
+        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmIncidentNodesResponse`
+
+        """
+        try:
+            params = request._serialize()
+            headers = request.headers
+            body = self.call("DescribeAlarmIncidentNodes", params, headers=headers)
+            response = json.loads(body)
+            model = models.DescribeAlarmIncidentNodesResponse()
+            model._deserialize(response["Response"])
+            return model
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
+    def DescribeAlarmVertexId(self, request):
+        """查询告警点id列表
+
+        :param request: Request instance for DescribeAlarmVertexId.
+        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmVertexIdRequest`
+        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAlarmVertexIdResponse`
+
+        """
+        try:
+            params = request._serialize()
+            headers = request.headers
+            body = self.call("DescribeAlarmVertexId", params, headers=headers)
+            response = json.loads(body)
+            model = models.DescribeAlarmVertexIdResponse()
+            model._deserialize(response["Response"])
+            return model
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DescribeAssetAppList(self, request):
         """查询应用列表
 
         :param request: Request instance for DescribeAssetAppList.
         :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppListRequest`
         :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeAssetAppListResponse`
 
@@ -2624,14 +2670,37 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def DescribeEventByTable(self, request):
+        """根据事件表名和id查询告警事件详情
+
+        :param request: Request instance for DescribeEventByTable.
+        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeEventByTableRequest`
+        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeEventByTableResponse`
+
+        """
+        try:
+            params = request._serialize()
+            headers = request.headers
+            body = self.call("DescribeEventByTable", params, headers=headers)
+            response = json.loads(body)
+            model = models.DescribeEventByTableResponse()
+            model._deserialize(response["Response"])
+            return model
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DescribeExpertServiceList(self, request):
         """专家服务-安全管家列表
 
         :param request: Request instance for DescribeExpertServiceList.
         :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceListRequest`
         :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeExpertServiceListResponse`
 
@@ -3406,14 +3475,37 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def DescribePrivilegeEventInfo(self, request):
+        """本地提权信息详情
+
+        :param request: Request instance for DescribePrivilegeEventInfo.
+        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventInfoRequest`
+        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventInfoResponse`
+
+        """
+        try:
+            params = request._serialize()
+            headers = request.headers
+            body = self.call("DescribePrivilegeEventInfo", params, headers=headers)
+            response = json.loads(body)
+            model = models.DescribePrivilegeEventInfoResponse()
+            model._deserialize(response["Response"])
+            return model
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DescribePrivilegeEvents(self, request):
         """获取本地提权事件列表
 
         :param request: Request instance for DescribePrivilegeEvents.
         :type request: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventsRequest`
         :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribePrivilegeEventsResponse`
 
@@ -3590,14 +3682,37 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def DescribeReverseShellEventInfo(self, request):
+        """反弹shell信息详情
+
+        :param request: Request instance for DescribeReverseShellEventInfo.
+        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventInfoRequest`
+        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventInfoResponse`
+
+        """
+        try:
+            params = request._serialize()
+            headers = request.headers
+            body = self.call("DescribeReverseShellEventInfo", params, headers=headers)
+            response = json.loads(body)
+            model = models.DescribeReverseShellEventInfoResponse()
+            model._deserialize(response["Response"])
+            return model
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DescribeReverseShellEvents(self, request):
         """获取反弹Shell列表
 
         :param request: Request instance for DescribeReverseShellEvents.
         :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsRequest`
         :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeReverseShellEventsResponse`
 
@@ -3636,14 +3751,37 @@
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
 
 
+    def DescribeRiskDnsEventInfo(self, request):
+        """查询恶意请求事件详情
+
+        :param request: Request instance for DescribeRiskDnsEventInfo.
+        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventInfoRequest`
+        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventInfoResponse`
+
+        """
+        try:
+            params = request._serialize()
+            headers = request.headers
+            body = self.call("DescribeRiskDnsEventInfo", params, headers=headers)
+            response = json.loads(body)
+            model = models.DescribeRiskDnsEventInfoResponse()
+            model._deserialize(response["Response"])
+            return model
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
+
+
     def DescribeRiskDnsEventList(self, request):
         """获取恶意请求事件列表
 
         :param request: Request instance for DescribeRiskDnsEventList.
         :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventListRequest`
         :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeRiskDnsEventListResponse`
 
@@ -4186,14 +4324,37 @@
             model._deserialize(response["Response"])
             return model
         except Exception as e:
             if isinstance(e, TencentCloudSDKException):
                 raise
             else:
                 raise TencentCloudSDKException(e.message, e.message)
+
+
+    def DescribeVertexDetail(self, request):
+        """获取指定点属性信息
+
+        :param request: Request instance for DescribeVertexDetail.
+        :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVertexDetailRequest`
+        :rtype: :class:`tencentcloud.cwp.v20180228.models.DescribeVertexDetailResponse`
+
+        """
+        try:
+            params = request._serialize()
+            headers = request.headers
+            body = self.call("DescribeVertexDetail", params, headers=headers)
+            response = json.loads(body)
+            model = models.DescribeVertexDetailResponse()
+            model._deserialize(response["Response"])
+            return model
+        except Exception as e:
+            if isinstance(e, TencentCloudSDKException):
+                raise
+            else:
+                raise TencentCloudSDKException(e.message, e.message)
 
 
     def DescribeVulCountByDates(self, request):
         """漏洞管理模块，获取近日指定类型的漏洞数量和主机数量
 
         :param request: Request instance for DescribeVulCountByDates.
         :type request: :class:`tencentcloud.cwp.v20180228.models.DescribeVulCountByDatesRequest`
```

### Comparing `tencentcloud-sdk-python-cwp-3.0.867/PKG-INFO` & `tencentcloud-sdk-python-cwp-3.0.868/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-cwp
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Cwp SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-cwp-3.0.867/README.rst` & `tencentcloud-sdk-python-cwp-3.0.868/README.rst`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cwp-3.0.867/tencentcloud_sdk_python_cwp.egg-info/PKG-INFO` & `tencentcloud-sdk-python-cwp-3.0.868/tencentcloud_sdk_python_cwp.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-cwp
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Cwp SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

