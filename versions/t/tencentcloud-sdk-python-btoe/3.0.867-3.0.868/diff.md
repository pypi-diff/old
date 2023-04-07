# Comparing `tmp/tencentcloud-sdk-python-btoe-3.0.867.tar.gz` & `tmp/tencentcloud-sdk-python-btoe-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-btoe-3.0.867.tar", last modified: Wed Apr  5 16:22:58 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-btoe-3.0.868.tar", last modified: Fri Apr  7 00:21:54 2023, max compression
```

## Comparing `tencentcloud-sdk-python-btoe-3.0.867.tar` & `tencentcloud-sdk-python-btoe-3.0.868.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/
--rw-r--r--   0 root         (0) root         (0)     1008 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud_sdk_python_btoe.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud_sdk_python_btoe.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      618 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud_sdk_python_btoe.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1664 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud_sdk_python_btoe.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud_sdk_python_btoe.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210514/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210514/__init__.py
--rw-r--r--   0 root         (0) root         (0)    14610 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210514/btoe_client.py
--rw-r--r--   0 root         (0) root         (0)     3235 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210514/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)    26668 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210514/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210303/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210303/__init__.py
--rw-r--r--   0 root         (0) root         (0)    14636 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210303/btoe_client.py
--rw-r--r--   0 root         (0) root         (0)     3211 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210303/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)    28282 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210303/models.py
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/__init__.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1664 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      740 2023-04-05 16:22:58.000000 tencentcloud-sdk-python-btoe-3.0.867/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1664 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210303/
+-rw-r--r--   0 root         (0) root         (0)    28282 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210303/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210303/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    14636 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210303/btoe_client.py
+-rw-r--r--   0 root         (0) root         (0)     3211 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210303/errorcodes.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210514/
+-rw-r--r--   0 root         (0) root         (0)    26668 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210514/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210514/__init__.py
+-rw-r--r--   0 root         (0) root         (0)    14610 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210514/btoe_client.py
+-rw-r--r--   0 root         (0) root         (0)     3235 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210514/errorcodes.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      740 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud_sdk_python_btoe.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1664 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud_sdk_python_btoe.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud_sdk_python_btoe.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud_sdk_python_btoe.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      618 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/tencentcloud_sdk_python_btoe.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)     1008 2023-04-07 00:21:53.000000 tencentcloud-sdk-python-btoe-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 00:21:54.000000 tencentcloud-sdk-python-btoe-3.0.868/setup.cfg
```

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/setup.py` & `tencentcloud-sdk-python-btoe-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/tencentcloud_sdk_python_btoe.egg-info/SOURCES.txt` & `tencentcloud-sdk-python-btoe-3.0.868/tencentcloud_sdk_python_btoe.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/tencentcloud_sdk_python_btoe.egg-info/PKG-INFO` & `tencentcloud-sdk-python-btoe-3.0.868/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-btoe
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Btoe SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210514/btoe_client.py` & `tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210514/btoe_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210514/errorcodes.py` & `tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210514/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210514/models.py` & `tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210514/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210303/btoe_client.py` & `tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210303/btoe_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210303/errorcodes.py` & `tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210303/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/btoe/v20210303/models.py` & `tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/btoe/v20210303/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/tencentcloud/__init__.py` & `tencentcloud-sdk-python-btoe-3.0.868/tencentcloud/__init__.py`

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

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/PKG-INFO` & `tencentcloud-sdk-python-btoe-3.0.868/tencentcloud_sdk_python_btoe.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-btoe
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Btoe SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-btoe-3.0.867/README.rst` & `tencentcloud-sdk-python-btoe-3.0.868/README.rst`

 * *Files identical despite different names*

