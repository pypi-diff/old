# Comparing `tmp/tencentcloud-sdk-python-teo-3.0.866.tar.gz` & `tmp/tencentcloud-sdk-python-teo-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-teo-3.0.866.tar", last modified: Tue Apr  4 17:18:17 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-teo-3.0.868.tar", last modified: Fri Apr  7 01:01:25 2023, max compression
```

## Comparing `tencentcloud-sdk-python-teo-3.0.866.tar` & `tencentcloud-sdk-python-teo-3.0.868.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/
--rw-r--r--   0 root         (0) root         (0)     1006 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220901/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220901/__init__.py
--rw-r--r--   0 root         (0) root         (0)    81864 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220901/teo_client.py
--rw-r--r--   0 root         (0) root         (0)    20753 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220901/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)   495667 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220901/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220106/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220106/__init__.py
--rw-r--r--   0 root         (0) root         (0)    87643 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220106/teo_client.py
--rw-r--r--   0 root         (0) root         (0)     7631 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220106/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)   468214 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220106/models.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/__init__.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      737 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud_sdk_python_teo.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud_sdk_python_teo.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      603 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud_sdk_python_teo.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud_sdk_python_teo.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-04 17:18:17.000000 tencentcloud-sdk-python-teo-3.0.866/tencentcloud_sdk_python_teo.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220106/
+-rw-r--r--   0 root         (0) root         (0)   468214 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220106/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220106/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     7631 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220106/errorcodes.py
+-rw-r--r--   0 root         (0) root         (0)    87643 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220106/teo_client.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220901/
+-rw-r--r--   0 root         (0) root         (0)   504485 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220901/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220901/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    20753 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220901/errorcodes.py
+-rw-r--r--   0 root         (0) root         (0)    81864 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220901/teo_client.py
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      737 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud_sdk_python_teo.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud_sdk_python_teo.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud_sdk_python_teo.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud_sdk_python_teo.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      603 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/tencentcloud_sdk_python_teo.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)     1006 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 01:01:25.000000 tencentcloud-sdk-python-teo-3.0.868/setup.cfg
```

### Comparing `tencentcloud-sdk-python-teo-3.0.866/setup.py` & `tencentcloud-sdk-python-teo-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-teo-3.0.866/tencentcloud/__init__.py` & `tencentcloud-sdk-python-teo-3.0.868/tencentcloud/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -10,8 +10,8 @@
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS,
 # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 # See the License for the specific language governing permissions and
 # limitations under the License.
 
 
-__version__ = '3.0.866'
+__version__ = '3.0.868'
```

### Comparing `tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220901/teo_client.py` & `tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220901/teo_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220901/errorcodes.py` & `tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220901/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220901/models.py` & `tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220901/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -443,14 +443,231 @@
             if name in memeber_set:
                 memeber_set.remove(name)
         if len(memeber_set) > 0:
             warnings.warn("%s fileds are useless." % ",".join(memeber_set))
         
 
 
+class AlgDetectJS(AbstractModel):
+    """Bot主动特征识别客户端行为校验。
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Name: 操作名称。
+        :type Name: str
+        :param WorkLevel: 工作量证明 (proof_Of-Work)校验强度，默认low，取值有：
+<li>low：低；</li>
+<li>middle：中；</li>
+<li>high：高。</li>
+        :type WorkLevel: str
+        :param ExecuteMode: 执行方式，js延迟执行的时间。单位为ms，默认500，取值：0～1000。
+        :type ExecuteMode: int
+        :param InvalidStatTime: 客户端末启用JS（末完成检测）统计周期。单位为秒，默认10，取值：5～3600。
+        :type InvalidStatTime: int
+        :param InvalidThreshold: 客户端末启用JS（末完成检测）触发阈值。单位为次，默认300，取值：1～100000000。
+        :type InvalidThreshold: int
+        :param AlgDetectResults: Bot主动特征识别客户端行为校验结果。
+        :type AlgDetectResults: list of AlgDetectResult
+        """
+        self.Name = None
+        self.WorkLevel = None
+        self.ExecuteMode = None
+        self.InvalidStatTime = None
+        self.InvalidThreshold = None
+        self.AlgDetectResults = None
+
+
+    def _deserialize(self, params):
+        self.Name = params.get("Name")
+        self.WorkLevel = params.get("WorkLevel")
+        self.ExecuteMode = params.get("ExecuteMode")
+        self.InvalidStatTime = params.get("InvalidStatTime")
+        self.InvalidThreshold = params.get("InvalidThreshold")
+        if params.get("AlgDetectResults") is not None:
+            self.AlgDetectResults = []
+            for item in params.get("AlgDetectResults"):
+                obj = AlgDetectResult()
+                obj._deserialize(item)
+                self.AlgDetectResults.append(obj)
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class AlgDetectResult(AbstractModel):
+    """Bot主动特征识别校验结果。
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Result: 校验结果，取值有：
+<li>invalid：不合法Cookie；</li>
+<li>cookie_empty：末携带Cookie或Cookie己过期；</li>
+<li>js_empty：客户端末启用JS（末完成检测）；</li>
+<li>low：会话速率和周期特征校验低风险；</li>
+<li>middle：会话速率和周期特征校验中风险；</li>
+<li>high：会话速率和周期特征校验高风险；</li>
+<li>timeout：检测超时时长；</li>
+<li>not_browser：不合法浏览器；</li>
+<li>is_bot：Bot客户端。</li>
+        :type Result: str
+        :param Action: 处罚动作，取值有：
+<li>drop：拦截；</li>
+<li>monitor：观察；</li>
+<li>silence：静默；</li>
+<li>shortdelay：（短时间）等待后响应；</li>
+<li>longdelay：（长时间）等待后响应。</li>
+        :type Action: str
+        """
+        self.Result = None
+        self.Action = None
+
+
+    def _deserialize(self, params):
+        self.Result = params.get("Result")
+        self.Action = params.get("Action")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class AlgDetectRule(AbstractModel):
+    """Bot主动特征识别规则。
+
+    """
+
+    def __init__(self):
+        r"""
+        :param RuleID: 规则id。
+        :type RuleID: int
+        :param RuleName: 规则名。
+        :type RuleName: str
+        :param Switch: 规则开关。
+        :type Switch: str
+        :param AlgConditions: 自定义规则。
+        :type AlgConditions: list of AclCondition
+        :param AlgDetectSession: Cookie校验和会话行为分析。
+注意：此字段可能返回 null，表示取不到有效值。
+        :type AlgDetectSession: :class:`tencentcloud.teo.v20220901.models.AlgDetectSession`
+        :param AlgDetectJS: 客户端行为校验。
+        :type AlgDetectJS: list of AlgDetectJS
+        :param UpdateTime: 更新时间。仅出参使用。
+        :type UpdateTime: str
+        """
+        self.RuleID = None
+        self.RuleName = None
+        self.Switch = None
+        self.AlgConditions = None
+        self.AlgDetectSession = None
+        self.AlgDetectJS = None
+        self.UpdateTime = None
+
+
+    def _deserialize(self, params):
+        self.RuleID = params.get("RuleID")
+        self.RuleName = params.get("RuleName")
+        self.Switch = params.get("Switch")
+        if params.get("AlgConditions") is not None:
+            self.AlgConditions = []
+            for item in params.get("AlgConditions"):
+                obj = AclCondition()
+                obj._deserialize(item)
+                self.AlgConditions.append(obj)
+        if params.get("AlgDetectSession") is not None:
+            self.AlgDetectSession = AlgDetectSession()
+            self.AlgDetectSession._deserialize(params.get("AlgDetectSession"))
+        if params.get("AlgDetectJS") is not None:
+            self.AlgDetectJS = []
+            for item in params.get("AlgDetectJS"):
+                obj = AlgDetectJS()
+                obj._deserialize(item)
+                self.AlgDetectJS.append(obj)
+        self.UpdateTime = params.get("UpdateTime")
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
+class AlgDetectSession(AbstractModel):
+    """Cookie校验与会话跟踪。
+
+    """
+
+    def __init__(self):
+        r"""
+        :param Name: 操作名称。
+        :type Name: str
+        :param DetectMode: 校验方式，默认update_detect，取值有：
+<li>detect：仅校验；</li>
+<li>update_detect：更新Cookie并校验。</li>
+        :type DetectMode: str
+        :param SessionAnalyzeSwitch: 会话速率和周期特征校验开关，默认off，取值有：
+<li>off：关闭；</li>
+<li>on：打开。</li>
+        :type SessionAnalyzeSwitch: str
+        :param InvalidStatTime: 校验结果为未携带Cookie或Cookie已过期的统计周期。单位为秒，默认10，取值：5～3600。
+        :type InvalidStatTime: int
+        :param InvalidThreshold: 校验结果为未携带Cookie或Cookie已过期的触发阈值。单位为次，默认300，取值：1～100000000。
+        :type InvalidThreshold: int
+        :param AlgDetectResults: Cookie校验校验结果。
+        :type AlgDetectResults: list of AlgDetectResult
+        :param SessionBehaviors: 会话速率和周期特征校验结果。
+        :type SessionBehaviors: list of AlgDetectResult
+        """
+        self.Name = None
+        self.DetectMode = None
+        self.SessionAnalyzeSwitch = None
+        self.InvalidStatTime = None
+        self.InvalidThreshold = None
+        self.AlgDetectResults = None
+        self.SessionBehaviors = None
+
+
+    def _deserialize(self, params):
+        self.Name = params.get("Name")
+        self.DetectMode = params.get("DetectMode")
+        self.SessionAnalyzeSwitch = params.get("SessionAnalyzeSwitch")
+        self.InvalidStatTime = params.get("InvalidStatTime")
+        self.InvalidThreshold = params.get("InvalidThreshold")
+        if params.get("AlgDetectResults") is not None:
+            self.AlgDetectResults = []
+            for item in params.get("AlgDetectResults"):
+                obj = AlgDetectResult()
+                obj._deserialize(item)
+                self.AlgDetectResults.append(obj)
+        if params.get("SessionBehaviors") is not None:
+            self.SessionBehaviors = []
+            for item in params.get("SessionBehaviors"):
+                obj = AlgDetectResult()
+                obj._deserialize(item)
+                self.SessionBehaviors.append(obj)
+        memeber_set = set(params.keys())
+        for name, value in vars(self).items():
+            if name in memeber_set:
+                memeber_set.remove(name)
+        if len(memeber_set) > 0:
+            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
+        
+
+
 class AliasDomain(AbstractModel):
     """别称域名信息。
 
     """
 
     def __init__(self):
         r"""
@@ -790,23 +1007,26 @@
         :param BotPortraitRule: 用户画像规则。如果为null，默认使用历史配置。
         :type BotPortraitRule: :class:`tencentcloud.teo.v20220901.models.BotPortraitRule`
         :param IntelligenceRule: Bot智能分析。如果为null，默认使用历史配置。
 注意：此字段可能返回 null，表示取不到有效值。
         :type IntelligenceRule: :class:`tencentcloud.teo.v20220901.models.IntelligenceRule`
         :param BotUserRules: Bot自定义规则。如果为null，默认使用历史配置。
         :type BotUserRules: list of BotUserRule
+        :param AlgDetectRule: Bot主动特征识别规则。
+        :type AlgDetectRule: list of AlgDetectRule
         :param Customizes: Bot托管定制策略，入参可不填，仅出参使用。
 注意：此字段可能返回 null，表示取不到有效值。
         :type Customizes: list of BotUserRule
         """
         self.Switch = None
         self.BotManagedRule = None
         self.BotPortraitRule = None
         self.IntelligenceRule = None
         self.BotUserRules = None
+        self.AlgDetectRule = None
         self.Customizes = None
 
 
     def _deserialize(self, params):
         self.Switch = params.get("Switch")
         if params.get("BotManagedRule") is not None:
             self.BotManagedRule = BotManagedRule()
@@ -819,14 +1039,20 @@
             self.IntelligenceRule._deserialize(params.get("IntelligenceRule"))
         if params.get("BotUserRules") is not None:
             self.BotUserRules = []
             for item in params.get("BotUserRules"):
                 obj = BotUserRule()
                 obj._deserialize(item)
                 self.BotUserRules.append(obj)
+        if params.get("AlgDetectRule") is not None:
+            self.AlgDetectRule = []
+            for item in params.get("AlgDetectRule"):
+                obj = AlgDetectRule()
+                obj._deserialize(item)
+                self.AlgDetectRule.append(obj)
         if params.get("Customizes") is not None:
             self.Customizes = []
             for item in params.get("Customizes"):
                 obj = BotUserRule()
                 obj._deserialize(item)
                 self.Customizes.append(obj)
         memeber_set = set(params.keys())
```

### Comparing `tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220106/teo_client.py` & `tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220106/teo_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220106/errorcodes.py` & `tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220106/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-teo-3.0.866/tencentcloud/teo/v20220106/models.py` & `tencentcloud-sdk-python-teo-3.0.868/tencentcloud/teo/v20220106/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-teo-3.0.866/PKG-INFO` & `tencentcloud-sdk-python-teo-3.0.868/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-teo
-Version: 3.0.866
+Version: 3.0.868
 Summary: Tencent Cloud Teo SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-teo-3.0.866/README.rst` & `tencentcloud-sdk-python-teo-3.0.868/README.rst`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-teo-3.0.866/tencentcloud_sdk_python_teo.egg-info/SOURCES.txt` & `tencentcloud-sdk-python-teo-3.0.868/tencentcloud_sdk_python_teo.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-teo-3.0.866/tencentcloud_sdk_python_teo.egg-info/PKG-INFO` & `tencentcloud-sdk-python-teo-3.0.868/tencentcloud_sdk_python_teo.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-teo
-Version: 3.0.866
+Version: 3.0.868
 Summary: Tencent Cloud Teo SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

