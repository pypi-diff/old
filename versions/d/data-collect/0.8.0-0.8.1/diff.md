# Comparing `tmp/data_collect-0.8.0.tar.gz` & `tmp/data_collect-0.8.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "data_collect-0.8.0.tar", last modified: Sun Apr  2 19:50:03 2023, max compression
+gzip compressed data, was "data_collect-0.8.1.tar", last modified: Thu Apr  6 11:21:57 2023, max compression
```

## Comparing `data_collect-0.8.0.tar` & `data_collect-0.8.1.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxr-xr-x   0 jojo       (501) staff       (20)        0 2023-04-02 19:50:03.692358 data_collect-0.8.0/
--rw-r--r--   0 jojo       (501) staff       (20)      597 2023-04-02 19:50:03.692436 data_collect-0.8.0/PKG-INFO
-drwxr-xr-x   0 jojo       (501) staff       (20)        0 2023-04-02 19:50:03.690670 data_collect-0.8.0/data_collect/
--rw-r--r--   0 jojo       (501) staff       (20)        0 2023-03-23 09:10:26.000000 data_collect-0.8.0/data_collect/__init__.py
--rw-r--r--   0 jojo       (501) staff       (20)    12220 2023-04-02 17:41:36.000000 data_collect-0.8.0/data_collect/client.py
--rw-r--r--   0 jojo       (501) staff       (20)      845 2023-03-23 09:10:26.000000 data_collect-0.8.0/data_collect/constants.py
--rw-r--r--   0 jojo       (501) staff       (20)      283 2023-03-23 09:10:26.000000 data_collect-0.8.0/data_collect/correlation_id.py
-drwxr-xr-x   0 jojo       (501) staff       (20)        0 2023-04-02 19:50:03.692201 data_collect-0.8.0/data_collect/data_types/
--rw-r--r--   0 jojo       (501) staff       (20)        0 2023-03-23 09:10:26.000000 data_collect-0.8.0/data_collect/data_types/__init__.py
--rw-r--r--   0 jojo       (501) staff       (20)      544 2023-03-23 09:10:26.000000 data_collect-0.8.0/data_collect/data_types/blob.py
--rw-r--r--   0 jojo       (501) staff       (20)     3316 2023-03-29 14:36:52.000000 data_collect-0.8.0/data_collect/data_types/image.py
--rw-r--r--   0 jojo       (501) staff       (20)      394 2023-03-23 09:10:26.000000 data_collect-0.8.0/data_collect/data_types/text.py
--rw-r--r--   0 jojo       (501) staff       (20)     5164 2023-04-02 17:13:44.000000 data_collect-0.8.0/data_collect/logger.py
--rw-r--r--   0 jojo       (501) staff       (20)      179 2023-03-28 12:28:58.000000 data_collect-0.8.0/data_collect/setup.py
--rw-r--r--   0 jojo       (501) staff       (20)     1108 2023-03-23 09:10:26.000000 data_collect-0.8.0/data_collect/utils.py
-drwxr-xr-x   0 jojo       (501) staff       (20)        0 2023-04-02 19:50:03.691511 data_collect-0.8.0/data_collect.egg-info/
--rw-r--r--   0 jojo       (501) staff       (20)      597 2023-04-02 19:50:03.000000 data_collect-0.8.0/data_collect.egg-info/PKG-INFO
--rw-r--r--   0 jojo       (501) staff       (20)      537 2023-04-02 19:50:03.000000 data_collect-0.8.0/data_collect.egg-info/SOURCES.txt
--rw-r--r--   0 jojo       (501) staff       (20)        1 2023-04-02 19:50:03.000000 data_collect-0.8.0/data_collect.egg-info/dependency_links.txt
--rw-r--r--   0 jojo       (501) staff       (20)        1 2023-04-02 19:50:03.000000 data_collect-0.8.0/data_collect.egg-info/not-zip-safe
--rw-r--r--   0 jojo       (501) staff       (20)       75 2023-04-02 19:50:03.000000 data_collect-0.8.0/data_collect.egg-info/requires.txt
--rw-r--r--   0 jojo       (501) staff       (20)       13 2023-04-02 19:50:03.000000 data_collect-0.8.0/data_collect.egg-info/top_level.txt
--rw-r--r--   0 jojo       (501) staff       (20)      782 2023-04-02 19:50:03.692868 data_collect-0.8.0/setup.cfg
--rw-r--r--   0 jojo       (501) staff       (20)      179 2023-04-02 19:50:02.000000 data_collect-0.8.0/setup.py
+drwxr-xr-x   0 jojo       (501) staff       (20)        0 2023-04-06 11:21:57.704063 data_collect-0.8.1/
+-rw-r--r--   0 jojo       (501) staff       (20)      597 2023-04-06 11:21:57.704134 data_collect-0.8.1/PKG-INFO
+drwxr-xr-x   0 jojo       (501) staff       (20)        0 2023-04-06 11:21:57.702280 data_collect-0.8.1/data_collect/
+-rw-r--r--   0 jojo       (501) staff       (20)        0 2023-03-23 09:10:26.000000 data_collect-0.8.1/data_collect/__init__.py
+-rw-r--r--   0 jojo       (501) staff       (20)    12198 2023-04-06 11:20:37.000000 data_collect-0.8.1/data_collect/client.py
+-rw-r--r--   0 jojo       (501) staff       (20)     1097 2023-04-03 06:37:00.000000 data_collect-0.8.1/data_collect/constants.py
+-rw-r--r--   0 jojo       (501) staff       (20)      283 2023-03-23 09:10:26.000000 data_collect-0.8.1/data_collect/correlation_id.py
+drwxr-xr-x   0 jojo       (501) staff       (20)        0 2023-04-06 11:21:57.703910 data_collect-0.8.1/data_collect/data_types/
+-rw-r--r--   0 jojo       (501) staff       (20)        0 2023-03-23 09:10:26.000000 data_collect-0.8.1/data_collect/data_types/__init__.py
+-rw-r--r--   0 jojo       (501) staff       (20)      544 2023-03-23 09:10:26.000000 data_collect-0.8.1/data_collect/data_types/blob.py
+-rw-r--r--   0 jojo       (501) staff       (20)     3316 2023-03-29 14:36:52.000000 data_collect-0.8.1/data_collect/data_types/image.py
+-rw-r--r--   0 jojo       (501) staff       (20)      394 2023-03-23 09:10:26.000000 data_collect-0.8.1/data_collect/data_types/text.py
+-rw-r--r--   0 jojo       (501) staff       (20)     5286 2023-04-06 11:18:52.000000 data_collect-0.8.1/data_collect/logger.py
+-rw-r--r--   0 jojo       (501) staff       (20)      179 2023-03-28 12:28:58.000000 data_collect-0.8.1/data_collect/setup.py
+-rw-r--r--   0 jojo       (501) staff       (20)     1108 2023-03-23 09:10:26.000000 data_collect-0.8.1/data_collect/utils.py
+drwxr-xr-x   0 jojo       (501) staff       (20)        0 2023-04-06 11:21:57.703196 data_collect-0.8.1/data_collect.egg-info/
+-rw-r--r--   0 jojo       (501) staff       (20)      597 2023-04-06 11:21:57.000000 data_collect-0.8.1/data_collect.egg-info/PKG-INFO
+-rw-r--r--   0 jojo       (501) staff       (20)      537 2023-04-06 11:21:57.000000 data_collect-0.8.1/data_collect.egg-info/SOURCES.txt
+-rw-r--r--   0 jojo       (501) staff       (20)        1 2023-04-06 11:21:57.000000 data_collect-0.8.1/data_collect.egg-info/dependency_links.txt
+-rw-r--r--   0 jojo       (501) staff       (20)        1 2023-04-06 11:21:57.000000 data_collect-0.8.1/data_collect.egg-info/not-zip-safe
+-rw-r--r--   0 jojo       (501) staff       (20)       75 2023-04-06 11:21:57.000000 data_collect-0.8.1/data_collect.egg-info/requires.txt
+-rw-r--r--   0 jojo       (501) staff       (20)       13 2023-04-06 11:21:57.000000 data_collect-0.8.1/data_collect.egg-info/top_level.txt
+-rw-r--r--   0 jojo       (501) staff       (20)      782 2023-04-06 11:21:57.704551 data_collect-0.8.1/setup.cfg
+-rw-r--r--   0 jojo       (501) staff       (20)      179 2023-04-06 11:21:57.000000 data_collect-0.8.1/setup.py
```

### Comparing `data_collect-0.8.0/PKG-INFO` & `data_collect-0.8.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: data_collect
-Version: 0.8.0
+Version: 0.8.1
 Summary: project descriptions here
 Home-page: https://console.cloud.baidu-int.com/devops/icode/repos/baidu/themis/windmill-endpoint/tree/master
 Author: zhoubohan
 Author-email: zhoubohan@baidu.com
 License: MIT
 Platform: UNKNOWN
 Classifier: Programming Language :: Python
```

### Comparing `data_collect-0.8.0/data_collect/client.py` & `data_collect-0.8.1/data_collect/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 from pydantic import BaseModel
 
 from .constants import (
     DEFAULT_CAPTURE_LOG_DIR, DEFAULT_CAPTURE_BLOB_DIR,
     CAPTURE_LOG_DIR, CAPTURE_BLOB_DIR,
     ENABLE_CAPTURE_INPUT, ENABLE_CAPTURE_PREDICTION, ENABLE_CAPTURE_GROUND_TRUTH, DEFAULT_CAPTURE_INPUT_DESIGNATION,
     TIME_DIRECTORY_FORMAT, DEFAULT_CAPTURE_PREDICTION_DESIGNATION, CAPTURE_LOG_ROTATION, CAPTURE_LOG_RETENTION,
-    DEFAULT_CAPTURE_LOG_ROTATION, DEFAULT_CAPTURE_LOG_RETENTION,
+    DEFAULT_CAPTURE_LOG_ROTATION, DEFAULT_CAPTURE_LOG_RETENTION, CV2_IMWRITE_VALID_CONTENT_TYPE,
 )
 from .logger import LineLogger, BlobLogger, ImageLogger
 from .utils import get_model_name, NpEncoder
 from .data_types.blob import Blob as WindmillBlob
 from .data_types.image import Image as WindmillImage
 from .data_types.text import Text as WindmillText
 
@@ -111,20 +111,18 @@
         dir_name = Path(dir_name)
         dir_name.mkdir(parents=True, exist_ok=True)
         file_name = correlation_id
         if metadata.get('sub_name'):
             file_name = f'{file_name}_{metadata.get("sub_name")}'
         file_path = f"{dir_name}/{file_name}"
         # validate content type and set file extension
-        content_type = metadata.get('content_type', 'image/png')
-        if content_type not in ['image/png', 'image/jpeg', 'image/gif', 'image/jpg']:
-            raise ValueError(f"Invalid content_type '{content_type}' specified")
+        content_type = metadata.get('content_type', 'image/jpeg')
+        if content_type is not None and content_type not in CV2_IMWRITE_VALID_CONTENT_TYPE:
+            content_type = 'image/jpeg' # default content type .jpeg
         ext = mimetypes.guess_extension(content_type)
-        if ext is None:
-            ext = '.png'
         file_path += ext
         return file_path
 
     def _gen_default_message(self, correlation_id: str) -> {}:
         """
         generate default message
         :param correlation_id:
```

### Comparing `data_collect-0.8.0/data_collect/data_types/blob.py` & `data_collect-0.8.1/data_collect/data_types/blob.py`

 * *Files identical despite different names*

### Comparing `data_collect-0.8.0/data_collect/data_types/image.py` & `data_collect-0.8.1/data_collect/data_types/image.py`

 * *Files identical despite different names*

### Comparing `data_collect-0.8.0/data_collect/logger.py` & `data_collect-0.8.1/data_collect/logger.py`

 * *Files 2% similar despite different names*

```diff
@@ -22,22 +22,25 @@
         :param config
         """
         self._logger = None
         self.future_list = []
         self.submit_count = 0
         self.finish_count = 0
         self.error_count = 0
+        self.errors = []
 
     def __getattr__(self, attr):
         if attr == "submit_count":
             return self.submit_count
         elif attr == "finish_count":
             return self.finish_count
         elif attr == "error_count":
             return self.error_count
+        elif attr == "errors":
+            return self.errors
         else:
             raise AttributeError(f"{attr} not found")  # 属性不存在
 
     def log(self, correlation_id: str, **kwargs):
         raise NotImplementedError
 
     def execute(self, submit, fn, *args, **kwargs):
@@ -47,14 +50,15 @@
         """
         try:
             future = submit(fn, *args, **kwargs)
             self.future_list.append(future)
             self.submit_count += 1
         except Exception as e:
             self.error_count += 1
+            self.errors.append(e)
             raise e
 
     def wait(self):
         """
         wait
         :return:
         """
@@ -143,14 +147,15 @@
         if "PIL" in sys.modules and image.is_pillow_image():
             image.covert_to_rgb()
         elif "numpy" in sys.modules and image.is_numpy_array():
             image.covert_cv_image()
 
         cv2.imwrite(designation, image.data)
 
+
     def log(self,
             correlation_id: str,
             image: WindmillImage = None,
             designation: str = '',
             metadata: Dict = None):
 
         # 使用线程池执行器来提交cv2.write任务，并捕获异常
```

### Comparing `data_collect-0.8.0/data_collect/utils.py` & `data_collect-0.8.1/data_collect/utils.py`

 * *Files identical despite different names*

### Comparing `data_collect-0.8.0/data_collect.egg-info/PKG-INFO` & `data_collect-0.8.1/data_collect.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: data-collect
-Version: 0.8.0
+Version: 0.8.1
 Summary: project descriptions here
 Home-page: https://console.cloud.baidu-int.com/devops/icode/repos/baidu/themis/windmill-endpoint/tree/master
 Author: zhoubohan
 Author-email: zhoubohan@baidu.com
 License: MIT
 Platform: UNKNOWN
 Classifier: Programming Language :: Python
```

### Comparing `data_collect-0.8.0/data_collect.egg-info/SOURCES.txt` & `data_collect-0.8.1/data_collect.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `data_collect-0.8.0/setup.cfg` & `data_collect-0.8.1/setup.cfg`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 [metadata]
 name = data_collect
 author = zhoubohan
 author_email = zhoubohan@baidu.com
-version = 0.8.0
+version = 0.8.1
 description = project descriptions here
 long_description = file: README.md
 long_description_content_type = text/markdown
 home_page = https://console.cloud.baidu-int.com/devops/icode/repos/baidu/themis/windmill-endpoint/tree/master
 license = MIT
 classifier = 
 	Programming Language :: Python
```

