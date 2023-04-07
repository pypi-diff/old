# Comparing `tmp/tencentcloud-sdk-python-cms-3.0.867.tar.gz` & `tmp/tencentcloud-sdk-python-cms-3.0.868.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/tencentcloud-sdk-python-cms-3.0.867.tar", last modified: Wed Apr  5 16:26:21 2023, max compression
+gzip compressed data, was "dist/tencentcloud-sdk-python-cms-3.0.868.tar", last modified: Fri Apr  7 00:25:22 2023, max compression
```

## Comparing `tencentcloud-sdk-python-cms-3.0.867.tar` & `tencentcloud-sdk-python-cms-3.0.868.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud_sdk_python_cms.egg-info/
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud_sdk_python_cms.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      445 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud_sdk_python_cms.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud_sdk_python_cms.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)       13 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud_sdk_python_cms.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)     1006 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud/
--rw-r--r--   0 root         (0) root         (0)      630 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/v20190321/
--rw-r--r--   0 root         (0) root         (0)     9932 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/v20190321/cms_client.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/v20190321/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3664 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/v20190321/errorcodes.py
--rw-r--r--   0 root         (0) root         (0)    63975 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/v20190321/models.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/__init__.py
--rw-r--r--   0 root         (0) root         (0)       88 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     1659 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      737 2023-04-05 16:26:21.000000 tencentcloud-sdk-python-cms-3.0.867/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/PKG-INFO
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud/
+-rw-r--r--   0 root         (0) root         (0)      630 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/v20190321/
+-rw-r--r--   0 root         (0) root         (0)    63975 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/v20190321/models.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/v20190321/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3664 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/v20190321/errorcodes.py
+-rw-r--r--   0 root         (0) root         (0)     9932 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/v20190321/cms_client.py
+-rw-r--r--   0 root         (0) root         (0)      737 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud_sdk_python_cms.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1659 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud_sdk_python_cms.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud_sdk_python_cms.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       13 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud_sdk_python_cms.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      445 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/tencentcloud_sdk_python_cms.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)     1006 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/setup.py
+-rw-r--r--   0 root         (0) root         (0)       88 2023-04-07 00:25:22.000000 tencentcloud-sdk-python-cms-3.0.868/setup.cfg
```

### Comparing `tencentcloud-sdk-python-cms-3.0.867/tencentcloud_sdk_python_cms.egg-info/PKG-INFO` & `tencentcloud-sdk-python-cms-3.0.868/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-cms
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Cms SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-cms-3.0.867/setup.py` & `tencentcloud-sdk-python-cms-3.0.868/setup.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cms-3.0.867/tencentcloud/__init__.py` & `tencentcloud-sdk-python-cms-3.0.868/tencentcloud/__init__.py`

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

### Comparing `tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/v20190321/cms_client.py` & `tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/v20190321/cms_client.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/v20190321/errorcodes.py` & `tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/v20190321/errorcodes.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cms-3.0.867/tencentcloud/cms/v20190321/models.py` & `tencentcloud-sdk-python-cms-3.0.868/tencentcloud/cms/v20190321/models.py`

 * *Files identical despite different names*

### Comparing `tencentcloud-sdk-python-cms-3.0.867/PKG-INFO` & `tencentcloud-sdk-python-cms-3.0.868/tencentcloud_sdk_python_cms.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: tencentcloud-sdk-python-cms
-Version: 3.0.867
+Version: 3.0.868
 Summary: Tencent Cloud Cms SDK for Python
 Home-page: https://github.com/TencentCloud/tencentcloud-sdk-python
 Author: Tencent Cloud
 Author-email: tencentcloudapi@tencent.com
 License: Apache License 2.0
 Description: ============================
         Tencent Cloud SDK for Python
```

### Comparing `tencentcloud-sdk-python-cms-3.0.867/README.rst` & `tencentcloud-sdk-python-cms-3.0.868/README.rst`

 * *Files identical despite different names*

