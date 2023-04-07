# Comparing `tmp/tencentcloud-sdk-python-scf-3.0.867.tar.gz` & `tmp/tencentcloud-sdk-python-scf-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-scf-3.0.867.tar", last modified: Wed Apr  5 16:46:58 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-scf-3.0.868.tar", last modified: Fri Apr  7 00:48:19 2023, max compression
```

## Comparing `tencentcloud-sdk-python-scf-3.0.867.tar` & `tencentcloud-sdk-python-scf-3.0.868.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/
--rw-r--r--   0 root         (0) root         (0)     1006 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/v20180416/
--rw-r--r--   0 root         (0) root         (0)    42711 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/v20180416/scf_client.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/v20180416/__init__.py
--rw-r--r--   0 root         (0) root         (0)    31630 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/v20180416/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)   190551 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/v20180416/models.py
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud/__init__.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      737 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud_sdk_python_scf.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud_sdk_python_scf.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      445 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud_sdk_python_scf.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud_sdk_python_scf.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 16:46:58.000000 tencentcloud-sdk-python-scf-3.0.867/tencentcloud_sdk_python_scf.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud/
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/v20180416/
+-rw-r--r--   0 root         (0) root         (0)    42711 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/v20180416/scf_client.py
+-rw-r--r--   0 root         (0) root         (0)   190551 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/v20180416/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/v20180416/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    31630 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/v20180416/errorcodes.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      737 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud_sdk_python_scf.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud_sdk_python_scf.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud_sdk_python_scf.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud_sdk_python_scf.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      445 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/tencentcloud_sdk_python_scf.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)     1006 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 00:48:19.000000 tencentcloud-sdk-python-scf-3.0.868/setup.cfg
```

### Comparing `tencentcloud-sdk-python-scf-3.0.867/setup.py` & `tencentcloud-sdk-python-scf-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/v20180416/scf_client.py` & `tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/v20180416/scf_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/v20180416/errorcodes.py` & `tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/v20180416/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-scf-3.0.867/tencentcloud/scf/v20180416/models.py` & `tencentcloud-sdk-python-scf-3.0.868/tencentcloud/scf/v20180416/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-scf-3.0.867/tencentcloud/__init__.py` & `tencentcloud-sdk-python-scf-3.0.868/tencentcloud/__init__.py`

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

### Comparing `tencentcloud-sdk-python-scf-3.0.867/PKG-INFO` & `tencentcloud-sdk-python-scf-3.0.868/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-scf
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Scf SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-scf-3.0.867/README.rst` & `tencentcloud-sdk-python-scf-3.0.868/README.rst`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-scf-3.0.867/tencentcloud_sdk_python_scf.egg-info/PKG-INFO` & `tencentcloud-sdk-python-scf-3.0.868/tencentcloud_sdk_python_scf.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-scf
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Scf SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

