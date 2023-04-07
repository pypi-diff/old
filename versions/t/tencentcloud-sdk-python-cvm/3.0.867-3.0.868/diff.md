# Comparing `tmp/tencentcloud-sdk-python-cvm-3.0.867.tar.gz` & `tmp/tencentcloud-sdk-python-cvm-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-cvm-3.0.867.tar", last modified: Wed Apr  5 16:26:48 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-cvm-3.0.868.tar", last modified: Fri Apr  7 00:25:50 2023, max compression
```

## Comparing `tencentcloud-sdk-python-cvm-3.0.867.tar` & `tencentcloud-sdk-python-cvm-3.0.868.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/
--rw-r--r--   0 root         (0) root         (0)     1006 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud_sdk_python_cvm.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud_sdk_python_cvm.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      445 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud_sdk_python_cvm.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud_sdk_python_cvm.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud_sdk_python_cvm.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/v20170312/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/v20170312/__init__.py
--rw-r--r--   0 root         (0) root         (0)    42551 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/v20170312/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)   119282 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/v20170312/cvm_client.py
--rw-r--r--   0 root         (0) root         (0)   429343 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/v20170312/models.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      737 2023-04-05 16:26:48.000000 tencentcloud-sdk-python-cvm-3.0.867/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/v20170312/
+-rw-r--r--   0 root         (0) root         (0)   119282 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/v20170312/cvm_client.py
+-rw-r--r--   0 root         (0) root         (0)   429343 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/v20170312/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/v20170312/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    42551 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/v20170312/errorcodes.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      737 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/README.rst
+-rw-r--r--   0 root         (0) root         (0)     1006 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/setup.cfg
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud_sdk_python_cvm.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud_sdk_python_cvm.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud_sdk_python_cvm.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud_sdk_python_cvm.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      445 2023-04-07 00:25:50.000000 tencentcloud-sdk-python-cvm-3.0.868/tencentcloud_sdk_python_cvm.egg-info/SOURCES.txt
```

### Comparing `tencentcloud-sdk-python-cvm-3.0.867/setup.py` & `tencentcloud-sdk-python-cvm-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cvm-3.0.867/tencentcloud_sdk_python_cvm.egg-info/PKG-INFO` & `tencentcloud-sdk-python-cvm-3.0.868/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-cvm
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Cvm SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/__init__.py` & `tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/__init__.py`

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

### Comparing `tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/v20170312/errorcodes.py` & `tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/v20170312/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/v20170312/cvm_client.py` & `tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/v20170312/cvm_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cvm-3.0.867/tencentcloud/cvm/v20170312/models.py` & `tencentcloud-sdk-python-cvm-3.0.868/tencentcloud/cvm/v20170312/models.py`

 * *Files 0% similar despite different names*

```diff
@@ -116,15 +116,15 @@
 class ActionTimer(AbstractModel):
     """定时任务
 
     """
 
     def __init__(self):
         r"""
-        :param TimerAction: 定时器名称，目前仅支持销毁一个值：TerminateInstances。
+        :param TimerAction: 定时器动作，目前仅支持销毁一个值：TerminateInstances。
 注意：此字段可能返回 null，表示取不到有效值。
         :type TimerAction: str
         :param ActionTime: 执行时间，按照ISO8601标准表示，并且使用UTC时间。格式为 YYYY-MM-DDThh:mm:ssZ。例如 2018-05-29T11:26:40Z，执行时间必须大于当前时间5分钟。
 注意：此字段可能返回 null，表示取不到有效值。
         :type ActionTime: str
         :param Externals: 扩展数据
 注意：此字段可能返回 null，表示取不到有效值。
```

### Comparing `tencentcloud-sdk-python-cvm-3.0.867/PKG-INFO` & `tencentcloud-sdk-python-cvm-3.0.868/tencentcloud_sdk_python_cvm.egg-info/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-cvm
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Cvm SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-cvm-3.0.867/README.rst` & `tencentcloud-sdk-python-cvm-3.0.868/README.rst`

 * *Files identical despite different names*

