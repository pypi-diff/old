# Comparing `tmp/alibabacloud_ga20191120-1.0.8.tar.gz` & `tmp/alibabacloud_ga20191120-1.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/alibabacloud_ga20191120-1.0.8.tar", last modified: Mon Dec 20 03:05:27 2021, max compression
+gzip compressed data, was "dist/alibabacloud_ga20191120-1.0.9.tar", last modified: Thu Jan  6 08:45:34 2022, max compression
```

## Comparing `alibabacloud_ga20191120-1.0.8.tar` & `alibabacloud_ga20191120-1.0.9.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/
--rw-r--r--   0 root         (0) root         (0)      707 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/ChangeLog.md
--rw-r--r--   0 root         (0) root         (0)      600 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/LICENSE
--rw-r--r--   0 root         (0) root         (0)       29 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     2339 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1019 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/README-CN.md
--rw-r--r--   0 root         (0) root         (0)     1104 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120/
--rw-r--r--   0 root         (0) root         (0)       21 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120/__init__.py
--rw-r--r--   0 root         (0) root         (0)   238702 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120/client.py
--rw-r--r--   0 root         (0) root         (0)   503775 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2339 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      412 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      156 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       24 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       73 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2622 2021-12-20 03:05:27.000000 alibabacloud_ga20191120-1.0.8/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/
+-rw-r--r--   0 root         (0) root         (0)      867 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/ChangeLog.md
+-rw-r--r--   0 root         (0) root         (0)      600 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       29 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     2339 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1019 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/README-CN.md
+-rw-r--r--   0 root         (0) root         (0)     1104 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120/
+-rw-r--r--   0 root         (0) root         (0)       21 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   319472 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120/client.py
+-rw-r--r--   0 root         (0) root         (0)   544926 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2339 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      412 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      156 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       24 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       73 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2622 2022-01-06 08:45:34.000000 alibabacloud_ga20191120-1.0.9/setup.py
```

### Comparing `alibabacloud_ga20191120-1.0.8/ChangeLog.md` & `alibabacloud_ga20191120-1.0.9/ChangeLog.md`

 * *Files 10% similar despite different names*

```diff
@@ -1,7 +1,12 @@
+2021-12-20 Version: 1.0.8
+- Update createBasicAccelerator Api.
+- Add UpdateAcceleratorAutoRenewAttribute Api.
+- Add DescribeAcceleratorAutoRenewAttribute Api.
+
 2021-11-30 Version: 1.0.7
 - Update createBasicAccelerator Api.
 - Add UpdateAcceleratorAutoRenewAttribute Api.
 - Add DescribeAcceleratorAutoRenewAttribute Api.
 
 2021-11-24 Version: 1.0.6
 - Update createAccelerator Api.
```

### Comparing `alibabacloud_ga20191120-1.0.8/LICENSE` & `alibabacloud_ga20191120-1.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `alibabacloud_ga20191120-1.0.8/PKG-INFO` & `alibabacloud_ga20191120-1.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud_ga20191120
-Version: 1.0.8
+Version: 1.0.9
 Summary: Alibaba Cloud Global Acceleration (20191120) SDK Library for Python
 Home-page: https://github.com/aliyun/alibabacloud-python-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_ga20191120-1.0.8/README-CN.md` & `alibabacloud_ga20191120-1.0.9/README-CN.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_ga20191120-1.0.8/README.md` & `alibabacloud_ga20191120-1.0.9/README.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120/models.py` & `alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120/models.py`

 * *Files 2% similar despite different names*

```diff
@@ -1403,14 +1403,154 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = CreateAclResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class CreateApplicationMonitorRequest(TeaModel):
+    def __init__(
+        self,
+        accelerator_id: str = None,
+        address: str = None,
+        client_token: str = None,
+        detect_threshold: int = None,
+        listener_id: str = None,
+        options_json: str = None,
+        region_id: str = None,
+        task_name: str = None,
+    ):
+        self.accelerator_id = accelerator_id
+        self.address = address
+        self.client_token = client_token
+        self.detect_threshold = detect_threshold
+        self.listener_id = listener_id
+        self.options_json = options_json
+        self.region_id = region_id
+        self.task_name = task_name
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.accelerator_id is not None:
+            result['AcceleratorId'] = self.accelerator_id
+        if self.address is not None:
+            result['Address'] = self.address
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.detect_threshold is not None:
+            result['DetectThreshold'] = self.detect_threshold
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.options_json is not None:
+            result['OptionsJson'] = self.options_json
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_name is not None:
+            result['TaskName'] = self.task_name
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('AcceleratorId') is not None:
+            self.accelerator_id = m.get('AcceleratorId')
+        if m.get('Address') is not None:
+            self.address = m.get('Address')
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('DetectThreshold') is not None:
+            self.detect_threshold = m.get('DetectThreshold')
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('OptionsJson') is not None:
+            self.options_json = m.get('OptionsJson')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskName') is not None:
+            self.task_name = m.get('TaskName')
+        return self
+
+
+class CreateApplicationMonitorResponseBody(TeaModel):
+    def __init__(
+        self,
+        request_id: str = None,
+        task_id: str = None,
+    ):
+        # Id of the request
+        self.request_id = request_id
+        self.task_id = task_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class CreateApplicationMonitorResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: CreateApplicationMonitorResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = CreateApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class CreateBandwidthPackageRequest(TeaModel):
     def __init__(
         self,
         auto_pay: bool = None,
         auto_use_coupon: str = None,
         bandwidth: int = None,
         bandwidth_type: str = None,
@@ -3917,14 +4057,117 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = DeleteAclResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class DeleteApplicationMonitorRequest(TeaModel):
+    def __init__(
+        self,
+        client_token: str = None,
+        region_id: str = None,
+        task_id: str = None,
+    ):
+        self.client_token = client_token
+        self.region_id = region_id
+        self.task_id = task_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class DeleteApplicationMonitorResponseBody(TeaModel):
+    def __init__(
+        self,
+        request_id: str = None,
+    ):
+        self.request_id = request_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class DeleteApplicationMonitorResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: DeleteApplicationMonitorResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = DeleteApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class DeleteBandwidthPackageRequest(TeaModel):
     def __init__(
         self,
         bandwidth_package_id: str = None,
         client_token: str = None,
         region_id: str = None,
     ):
@@ -5519,14 +5762,224 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = DescribeAcceleratorAutoRenewAttributeResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class DescribeApplicationMonitorRequest(TeaModel):
+    def __init__(
+        self,
+        client_token: str = None,
+        region_id: str = None,
+        task_id: str = None,
+    ):
+        self.client_token = client_token
+        self.region_id = region_id
+        self.task_id = task_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class DescribeApplicationMonitorResponseBodyIspCityList(TeaModel):
+    def __init__(
+        self,
+        city: str = None,
+        city_name: str = None,
+        isp: str = None,
+        isp_name: str = None,
+    ):
+        self.city = city
+        self.city_name = city_name
+        self.isp = isp
+        self.isp_name = isp_name
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.city is not None:
+            result['City'] = self.city
+        if self.city_name is not None:
+            result['CityName'] = self.city_name
+        if self.isp is not None:
+            result['Isp'] = self.isp
+        if self.isp_name is not None:
+            result['IspName'] = self.isp_name
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('City') is not None:
+            self.city = m.get('City')
+        if m.get('CityName') is not None:
+            self.city_name = m.get('CityName')
+        if m.get('Isp') is not None:
+            self.isp = m.get('Isp')
+        if m.get('IspName') is not None:
+            self.isp_name = m.get('IspName')
+        return self
+
+
+class DescribeApplicationMonitorResponseBody(TeaModel):
+    def __init__(
+        self,
+        accelerator_id: str = None,
+        address: str = None,
+        detect_threshold: str = None,
+        isp_city_list: List[DescribeApplicationMonitorResponseBodyIspCityList] = None,
+        listener_id: str = None,
+        options_json: str = None,
+        region_id: str = None,
+        request_id: str = None,
+        task_id: str = None,
+        task_name: str = None,
+    ):
+        self.accelerator_id = accelerator_id
+        self.address = address
+        self.detect_threshold = detect_threshold
+        self.isp_city_list = isp_city_list
+        self.listener_id = listener_id
+        self.options_json = options_json
+        self.region_id = region_id
+        self.request_id = request_id
+        self.task_id = task_id
+        self.task_name = task_name
+
+    def validate(self):
+        if self.isp_city_list:
+            for k in self.isp_city_list:
+                if k:
+                    k.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.accelerator_id is not None:
+            result['AcceleratorId'] = self.accelerator_id
+        if self.address is not None:
+            result['Address'] = self.address
+        if self.detect_threshold is not None:
+            result['DetectThreshold'] = self.detect_threshold
+        result['IspCityList'] = []
+        if self.isp_city_list is not None:
+            for k in self.isp_city_list:
+                result['IspCityList'].append(k.to_map() if k else None)
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.options_json is not None:
+            result['OptionsJson'] = self.options_json
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        if self.task_name is not None:
+            result['TaskName'] = self.task_name
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('AcceleratorId') is not None:
+            self.accelerator_id = m.get('AcceleratorId')
+        if m.get('Address') is not None:
+            self.address = m.get('Address')
+        if m.get('DetectThreshold') is not None:
+            self.detect_threshold = m.get('DetectThreshold')
+        self.isp_city_list = []
+        if m.get('IspCityList') is not None:
+            for k in m.get('IspCityList'):
+                temp_model = DescribeApplicationMonitorResponseBodyIspCityList()
+                self.isp_city_list.append(temp_model.from_map(k))
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('OptionsJson') is not None:
+            self.options_json = m.get('OptionsJson')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        if m.get('TaskName') is not None:
+            self.task_name = m.get('TaskName')
+        return self
+
+
+class DescribeApplicationMonitorResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: DescribeApplicationMonitorResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = DescribeApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class DescribeBandwidthPackageRequest(TeaModel):
     def __init__(
         self,
         bandwidth_package_id: str = None,
         region_id: str = None,
     ):
         self.bandwidth_package_id = bandwidth_package_id
@@ -6988,14 +7441,220 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = DetachLogStoreFromEndpointGroupResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class DetectApplicationMonitorRequest(TeaModel):
+    def __init__(
+        self,
+        client_token: str = None,
+        region_id: str = None,
+        task_id: str = None,
+    ):
+        self.client_token = client_token
+        self.region_id = region_id
+        self.task_id = task_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class DetectApplicationMonitorResponseBody(TeaModel):
+    def __init__(
+        self,
+        request_id: str = None,
+    ):
+        self.request_id = request_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class DetectApplicationMonitorResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: DetectApplicationMonitorResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = DetectApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
+class DisableApplicationMonitorRequest(TeaModel):
+    def __init__(
+        self,
+        client_token: str = None,
+        region_id: str = None,
+        task_id: str = None,
+    ):
+        self.client_token = client_token
+        self.region_id = region_id
+        self.task_id = task_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class DisableApplicationMonitorResponseBody(TeaModel):
+    def __init__(
+        self,
+        request_id: str = None,
+    ):
+        self.request_id = request_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class DisableApplicationMonitorResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: DisableApplicationMonitorResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = DisableApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class DissociateAclsFromListenerRequest(TeaModel):
     def __init__(
         self,
         acl_ids: List[str] = None,
         client_token: str = None,
         dry_run: bool = None,
         listener_id: str = None,
@@ -7232,14 +7891,117 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = DissociateAdditionalCertificatesFromListenerResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class EnableApplicationMonitorRequest(TeaModel):
+    def __init__(
+        self,
+        client_token: str = None,
+        region_id: str = None,
+        task_id: str = None,
+    ):
+        self.client_token = client_token
+        self.region_id = region_id
+        self.task_id = task_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class EnableApplicationMonitorResponseBody(TeaModel):
+    def __init__(
+        self,
+        request_id: str = None,
+    ):
+        self.request_id = request_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class EnableApplicationMonitorResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: EnableApplicationMonitorResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = EnableApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class GetAclRequest(TeaModel):
     def __init__(
         self,
         acl_id: str = None,
         region_id: str = None,
     ):
         self.acl_id = acl_id
@@ -9157,14 +9919,440 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = ListAclsResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class ListApplicationMonitorRequest(TeaModel):
+    def __init__(
+        self,
+        page_number: int = None,
+        page_size: int = None,
+        region_id: str = None,
+        search_value: str = None,
+    ):
+        self.page_number = page_number
+        self.page_size = page_size
+        self.region_id = region_id
+        self.search_value = search_value
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.page_number is not None:
+            result['PageNumber'] = self.page_number
+        if self.page_size is not None:
+            result['PageSize'] = self.page_size
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.search_value is not None:
+            result['SearchValue'] = self.search_value
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('PageNumber') is not None:
+            self.page_number = m.get('PageNumber')
+        if m.get('PageSize') is not None:
+            self.page_size = m.get('PageSize')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('SearchValue') is not None:
+            self.search_value = m.get('SearchValue')
+        return self
+
+
+class ListApplicationMonitorResponseBodyApplicationMonitors(TeaModel):
+    def __init__(
+        self,
+        accelerator_id: str = None,
+        address: str = None,
+        detect_threshold: int = None,
+        listener_id: str = None,
+        options_json: str = None,
+        state: str = None,
+        task_id: str = None,
+        task_name: str = None,
+    ):
+        self.accelerator_id = accelerator_id
+        self.address = address
+        self.detect_threshold = detect_threshold
+        self.listener_id = listener_id
+        self.options_json = options_json
+        self.state = state
+        self.task_id = task_id
+        self.task_name = task_name
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.accelerator_id is not None:
+            result['AcceleratorId'] = self.accelerator_id
+        if self.address is not None:
+            result['Address'] = self.address
+        if self.detect_threshold is not None:
+            result['DetectThreshold'] = self.detect_threshold
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.options_json is not None:
+            result['OptionsJson'] = self.options_json
+        if self.state is not None:
+            result['State'] = self.state
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        if self.task_name is not None:
+            result['TaskName'] = self.task_name
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('AcceleratorId') is not None:
+            self.accelerator_id = m.get('AcceleratorId')
+        if m.get('Address') is not None:
+            self.address = m.get('Address')
+        if m.get('DetectThreshold') is not None:
+            self.detect_threshold = m.get('DetectThreshold')
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('OptionsJson') is not None:
+            self.options_json = m.get('OptionsJson')
+        if m.get('State') is not None:
+            self.state = m.get('State')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        if m.get('TaskName') is not None:
+            self.task_name = m.get('TaskName')
+        return self
+
+
+class ListApplicationMonitorResponseBody(TeaModel):
+    def __init__(
+        self,
+        application_monitors: List[ListApplicationMonitorResponseBodyApplicationMonitors] = None,
+        page_number: int = None,
+        page_size: int = None,
+        request_id: str = None,
+        total_count: int = None,
+    ):
+        self.application_monitors = application_monitors
+        self.page_number = page_number
+        self.page_size = page_size
+        self.request_id = request_id
+        self.total_count = total_count
+
+    def validate(self):
+        if self.application_monitors:
+            for k in self.application_monitors:
+                if k:
+                    k.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        result['ApplicationMonitors'] = []
+        if self.application_monitors is not None:
+            for k in self.application_monitors:
+                result['ApplicationMonitors'].append(k.to_map() if k else None)
+        if self.page_number is not None:
+            result['PageNumber'] = self.page_number
+        if self.page_size is not None:
+            result['PageSize'] = self.page_size
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        if self.total_count is not None:
+            result['TotalCount'] = self.total_count
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        self.application_monitors = []
+        if m.get('ApplicationMonitors') is not None:
+            for k in m.get('ApplicationMonitors'):
+                temp_model = ListApplicationMonitorResponseBodyApplicationMonitors()
+                self.application_monitors.append(temp_model.from_map(k))
+        if m.get('PageNumber') is not None:
+            self.page_number = m.get('PageNumber')
+        if m.get('PageSize') is not None:
+            self.page_size = m.get('PageSize')
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        if m.get('TotalCount') is not None:
+            self.total_count = m.get('TotalCount')
+        return self
+
+
+class ListApplicationMonitorResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: ListApplicationMonitorResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = ListApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
+class ListApplicationMonitorDetectResultRequest(TeaModel):
+    def __init__(
+        self,
+        begin_time: int = None,
+        end_time: int = None,
+        page_number: int = None,
+        page_size: int = None,
+        region_id: str = None,
+        task_id: str = None,
+    ):
+        self.begin_time = begin_time
+        self.end_time = end_time
+        self.page_number = page_number
+        self.page_size = page_size
+        self.region_id = region_id
+        self.task_id = task_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.begin_time is not None:
+            result['BeginTime'] = self.begin_time
+        if self.end_time is not None:
+            result['EndTime'] = self.end_time
+        if self.page_number is not None:
+            result['PageNumber'] = self.page_number
+        if self.page_size is not None:
+            result['PageSize'] = self.page_size
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('BeginTime') is not None:
+            self.begin_time = m.get('BeginTime')
+        if m.get('EndTime') is not None:
+            self.end_time = m.get('EndTime')
+        if m.get('PageNumber') is not None:
+            self.page_number = m.get('PageNumber')
+        if m.get('PageSize') is not None:
+            self.page_size = m.get('PageSize')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList(TeaModel):
+    def __init__(
+        self,
+        accelerator_id: str = None,
+        detail: str = None,
+        diag_status: str = None,
+        listener_id: str = None,
+        port: str = None,
+        protocol: str = None,
+        task_id: str = None,
+    ):
+        self.accelerator_id = accelerator_id
+        self.detail = detail
+        self.diag_status = diag_status
+        self.listener_id = listener_id
+        self.port = port
+        self.protocol = protocol
+        self.task_id = task_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.accelerator_id is not None:
+            result['AcceleratorId'] = self.accelerator_id
+        if self.detail is not None:
+            result['Detail'] = self.detail
+        if self.diag_status is not None:
+            result['DiagStatus'] = self.diag_status
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.port is not None:
+            result['Port'] = self.port
+        if self.protocol is not None:
+            result['Protocol'] = self.protocol
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('AcceleratorId') is not None:
+            self.accelerator_id = m.get('AcceleratorId')
+        if m.get('Detail') is not None:
+            self.detail = m.get('Detail')
+        if m.get('DiagStatus') is not None:
+            self.diag_status = m.get('DiagStatus')
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('Port') is not None:
+            self.port = m.get('Port')
+        if m.get('Protocol') is not None:
+            self.protocol = m.get('Protocol')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        return self
+
+
+class ListApplicationMonitorDetectResultResponseBody(TeaModel):
+    def __init__(
+        self,
+        application_monitor_detect_result_list: List[ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList] = None,
+        page_number: int = None,
+        page_size: int = None,
+        request_id: str = None,
+        total_count: int = None,
+    ):
+        self.application_monitor_detect_result_list = application_monitor_detect_result_list
+        self.page_number = page_number
+        self.page_size = page_size
+        self.request_id = request_id
+        self.total_count = total_count
+
+    def validate(self):
+        if self.application_monitor_detect_result_list:
+            for k in self.application_monitor_detect_result_list:
+                if k:
+                    k.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        result['ApplicationMonitorDetectResultList'] = []
+        if self.application_monitor_detect_result_list is not None:
+            for k in self.application_monitor_detect_result_list:
+                result['ApplicationMonitorDetectResultList'].append(k.to_map() if k else None)
+        if self.page_number is not None:
+            result['PageNumber'] = self.page_number
+        if self.page_size is not None:
+            result['PageSize'] = self.page_size
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        if self.total_count is not None:
+            result['TotalCount'] = self.total_count
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        self.application_monitor_detect_result_list = []
+        if m.get('ApplicationMonitorDetectResultList') is not None:
+            for k in m.get('ApplicationMonitorDetectResultList'):
+                temp_model = ListApplicationMonitorDetectResultResponseBodyApplicationMonitorDetectResultList()
+                self.application_monitor_detect_result_list.append(temp_model.from_map(k))
+        if m.get('PageNumber') is not None:
+            self.page_number = m.get('PageNumber')
+        if m.get('PageSize') is not None:
+            self.page_size = m.get('PageSize')
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        if m.get('TotalCount') is not None:
+            self.total_count = m.get('TotalCount')
+        return self
+
+
+class ListApplicationMonitorDetectResultResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: ListApplicationMonitorDetectResultResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = ListApplicationMonitorDetectResultResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class ListAvailableAccelerateAreasRequest(TeaModel):
     def __init__(
         self,
         accelerator_id: str = None,
         region_id: str = None,
     ):
         self.accelerator_id = accelerator_id
@@ -13230,14 +14418,147 @@
             self.headers = m.get('headers')
         if m.get('body') is not None:
             temp_model = UpdateAclAttributeResponseBody()
             self.body = temp_model.from_map(m['body'])
         return self
 
 
+class UpdateApplicationMonitorRequest(TeaModel):
+    def __init__(
+        self,
+        address: str = None,
+        client_token: str = None,
+        detect_threshold: int = None,
+        listener_id: str = None,
+        options_json: str = None,
+        region_id: str = None,
+        task_id: str = None,
+        task_name: str = None,
+    ):
+        self.address = address
+        self.client_token = client_token
+        self.detect_threshold = detect_threshold
+        self.listener_id = listener_id
+        self.options_json = options_json
+        self.region_id = region_id
+        self.task_id = task_id
+        self.task_name = task_name
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.address is not None:
+            result['Address'] = self.address
+        if self.client_token is not None:
+            result['ClientToken'] = self.client_token
+        if self.detect_threshold is not None:
+            result['DetectThreshold'] = self.detect_threshold
+        if self.listener_id is not None:
+            result['ListenerId'] = self.listener_id
+        if self.options_json is not None:
+            result['OptionsJson'] = self.options_json
+        if self.region_id is not None:
+            result['RegionId'] = self.region_id
+        if self.task_id is not None:
+            result['TaskId'] = self.task_id
+        if self.task_name is not None:
+            result['TaskName'] = self.task_name
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('Address') is not None:
+            self.address = m.get('Address')
+        if m.get('ClientToken') is not None:
+            self.client_token = m.get('ClientToken')
+        if m.get('DetectThreshold') is not None:
+            self.detect_threshold = m.get('DetectThreshold')
+        if m.get('ListenerId') is not None:
+            self.listener_id = m.get('ListenerId')
+        if m.get('OptionsJson') is not None:
+            self.options_json = m.get('OptionsJson')
+        if m.get('RegionId') is not None:
+            self.region_id = m.get('RegionId')
+        if m.get('TaskId') is not None:
+            self.task_id = m.get('TaskId')
+        if m.get('TaskName') is not None:
+            self.task_name = m.get('TaskName')
+        return self
+
+
+class UpdateApplicationMonitorResponseBody(TeaModel):
+    def __init__(
+        self,
+        request_id: str = None,
+    ):
+        self.request_id = request_id
+
+    def validate(self):
+        pass
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.request_id is not None:
+            result['RequestId'] = self.request_id
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('RequestId') is not None:
+            self.request_id = m.get('RequestId')
+        return self
+
+
+class UpdateApplicationMonitorResponse(TeaModel):
+    def __init__(
+        self,
+        headers: Dict[str, str] = None,
+        body: UpdateApplicationMonitorResponseBody = None,
+    ):
+        self.headers = headers
+        self.body = body
+
+    def validate(self):
+        self.validate_required(self.headers, 'headers')
+        self.validate_required(self.body, 'body')
+        if self.body:
+            self.body.validate()
+
+    def to_map(self):
+        _map = super().to_map()
+        if _map is not None:
+            return _map
+
+        result = dict()
+        if self.headers is not None:
+            result['headers'] = self.headers
+        if self.body is not None:
+            result['body'] = self.body.to_map()
+        return result
+
+    def from_map(self, m: dict = None):
+        m = m or dict()
+        if m.get('headers') is not None:
+            self.headers = m.get('headers')
+        if m.get('body') is not None:
+            temp_model = UpdateApplicationMonitorResponseBody()
+            self.body = temp_model.from_map(m['body'])
+        return self
+
+
 class UpdateBandwidthPackageRequest(TeaModel):
     def __init__(
         self,
         auto_pay: bool = None,
         auto_use_coupon: bool = None,
         bandwidth: int = None,
         bandwidth_package_id: str = None,
```

### Comparing `alibabacloud_ga20191120-1.0.8/alibabacloud_ga20191120.egg-info/PKG-INFO` & `alibabacloud_ga20191120-1.0.9/alibabacloud_ga20191120.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud-ga20191120
-Version: 1.0.8
+Version: 1.0.9
 Summary: Alibaba Cloud Global Acceleration (20191120) SDK Library for Python
 Home-page: https://github.com/aliyun/alibabacloud-python-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_ga20191120-1.0.8/setup.py` & `alibabacloud_ga20191120-1.0.9/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -20,29 +20,29 @@
 
 import os
 from setuptools import setup, find_packages
 
 """
 setup module for alibabacloud_ga20191120.
 
-Created on 20/12/2021
+Created on 06/01/2022
 
 @author: Alibaba Cloud SDK
 """
 
 PACKAGE = "alibabacloud_ga20191120"
 NAME = "alibabacloud_ga20191120" or "alibabacloud-package"
 DESCRIPTION = "Alibaba Cloud Global Acceleration (20191120) SDK Library for Python"
 AUTHOR = "Alibaba Cloud SDK"
 AUTHOR_EMAIL = "sdk-team@alibabacloud.com"
 URL = "https://github.com/aliyun/alibabacloud-python-sdk"
 VERSION = __import__(PACKAGE).__version__
 REQUIRES = [
     "alibabacloud_tea_util>=0.3.5, <1.0.0",
-    "alibabacloud_tea_openapi>=0.3.0, <1.0.0",
+    "alibabacloud_tea_openapi>=0.3.1, <1.0.0",
     "alibabacloud_openapi_util>=0.1.6, <1.0.0",
     "alibabacloud_endpoint_util>=0.0.3, <1.0.0"
 ]
 
 LONG_DESCRIPTION = ''
 if os.path.exists('./README.md'):
     with open("README.md", encoding='utf-8') as fp:
```

