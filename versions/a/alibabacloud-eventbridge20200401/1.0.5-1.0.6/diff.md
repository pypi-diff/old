# Comparing `tmp/alibabacloud_eventbridge20200401-1.0.5.tar.gz` & `tmp/alibabacloud_eventbridge20200401-1.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/alibabacloud_eventbridge20200401-1.0.5.tar", last modified: Wed Mar 22 05:42:01 2023, max compression
+gzip compressed data, was "dist/alibabacloud_eventbridge20200401-1.0.6.tar", last modified: Fri Apr  7 03:45:29 2023, max compression
```

## Comparing `alibabacloud_eventbridge20200401-1.0.5.tar` & `alibabacloud_eventbridge20200401-1.0.6.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/
--rw-r--r--   0 root         (0) root         (0)      256 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/ChangeLog.md
--rw-r--r--   0 root         (0) root         (0)      600 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/LICENSE
--rw-r--r--   0 root         (0) root         (0)       29 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     2376 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1046 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/README-CN.md
--rw-r--r--   0 root         (0) root         (0)     1131 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401/
--rw-r--r--   0 root         (0) root         (0)       21 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401/__init__.py
--rw-r--r--   0 root         (0) root         (0)   146485 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401/client.py
--rw-r--r--   0 root         (0) root         (0)   740307 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401/models.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2376 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      484 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      156 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       33 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)       73 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2650 2023-03-22 05:42:01.000000 alibabacloud_eventbridge20200401-1.0.5/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/
+-rw-r--r--   0 root         (0) root         (0)      304 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/ChangeLog.md
+-rw-r--r--   0 root         (0) root         (0)      600 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       29 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     2376 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1046 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/README-CN.md
+-rw-r--r--   0 root         (0) root         (0)     1131 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401/
+-rw-r--r--   0 root         (0) root         (0)       21 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   145253 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401/client.py
+-rw-r--r--   0 root         (0) root         (0)   729553 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401/models.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2376 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      484 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      156 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       33 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)       73 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2650 2023-04-07 03:45:29.000000 alibabacloud_eventbridge20200401-1.0.6/setup.py
```

### Comparing `alibabacloud_eventbridge20200401-1.0.5/LICENSE` & `alibabacloud_eventbridge20200401-1.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `alibabacloud_eventbridge20200401-1.0.5/PKG-INFO` & `alibabacloud_eventbridge20200401-1.0.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud_eventbridge20200401
-Version: 1.0.5
+Version: 1.0.6
 Summary: Alibaba Cloud eventbridge (20200401) SDK Library for Python
 Home-page: https://github.com/aliyun/alibabacloud-python-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_eventbridge20200401-1.0.5/README-CN.md` & `alibabacloud_eventbridge20200401-1.0.6/README-CN.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_eventbridge20200401-1.0.5/README.md` & `alibabacloud_eventbridge20200401-1.0.6/README.md`

 * *Files identical despite different names*

### Comparing `alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401/client.py` & `alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401/client.py`

 * *Files 1% similar despite different names*

```diff
@@ -56,16 +56,14 @@
             query['ApiDestinationName'] = request.api_destination_name
         if not UtilClient.is_unset(request.connection_name):
             query['ConnectionName'] = request.connection_name
         if not UtilClient.is_unset(request.description):
             query['Description'] = request.description
         if not UtilClient.is_unset(request.http_api_parameters_shrink):
             query['HttpApiParameters'] = request.http_api_parameters_shrink
-        if not UtilClient.is_unset(request.invocation_rate_limit_per_second):
-            query['InvocationRateLimitPerSecond'] = request.invocation_rate_limit_per_second
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateApiDestination',
             version='2020-04-01',
             protocol='HTTPS',
@@ -96,16 +94,14 @@
             query['ApiDestinationName'] = request.api_destination_name
         if not UtilClient.is_unset(request.connection_name):
             query['ConnectionName'] = request.connection_name
         if not UtilClient.is_unset(request.description):
             query['Description'] = request.description
         if not UtilClient.is_unset(request.http_api_parameters_shrink):
             query['HttpApiParameters'] = request.http_api_parameters_shrink
-        if not UtilClient.is_unset(request.invocation_rate_limit_per_second):
-            query['InvocationRateLimitPerSecond'] = request.invocation_rate_limit_per_second
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='CreateApiDestination',
             version='2020-04-01',
             protocol='HTTPS',
@@ -790,16 +786,14 @@
         request: eventbridge_20200401_models.DeleteApiDestinationRequest,
         runtime: util_models.RuntimeOptions,
     ) -> eventbridge_20200401_models.DeleteApiDestinationResponse:
         UtilClient.validate_model(request)
         query = {}
         if not UtilClient.is_unset(request.api_destination_name):
             query['ApiDestinationName'] = request.api_destination_name
-        if not UtilClient.is_unset(request.client_token):
-            query['ClientToken'] = request.client_token
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteApiDestination',
             version='2020-04-01',
             protocol='HTTPS',
@@ -820,16 +814,14 @@
         request: eventbridge_20200401_models.DeleteApiDestinationRequest,
         runtime: util_models.RuntimeOptions,
     ) -> eventbridge_20200401_models.DeleteApiDestinationResponse:
         UtilClient.validate_model(request)
         query = {}
         if not UtilClient.is_unset(request.api_destination_name):
             query['ApiDestinationName'] = request.api_destination_name
-        if not UtilClient.is_unset(request.client_token):
-            query['ClientToken'] = request.client_token
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='DeleteApiDestination',
             version='2020-04-01',
             protocol='HTTPS',
@@ -1452,16 +1444,14 @@
         request: eventbridge_20200401_models.GetApiDestinationRequest,
         runtime: util_models.RuntimeOptions,
     ) -> eventbridge_20200401_models.GetApiDestinationResponse:
         UtilClient.validate_model(request)
         query = {}
         if not UtilClient.is_unset(request.api_destination_name):
             query['ApiDestinationName'] = request.api_destination_name
-        if not UtilClient.is_unset(request.client_token):
-            query['ClientToken'] = request.client_token
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='GetApiDestination',
             version='2020-04-01',
             protocol='HTTPS',
@@ -1482,16 +1472,14 @@
         request: eventbridge_20200401_models.GetApiDestinationRequest,
         runtime: util_models.RuntimeOptions,
     ) -> eventbridge_20200401_models.GetApiDestinationResponse:
         UtilClient.validate_model(request)
         query = {}
         if not UtilClient.is_unset(request.api_destination_name):
             query['ApiDestinationName'] = request.api_destination_name
-        if not UtilClient.is_unset(request.client_token):
-            query['ClientToken'] = request.client_token
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
         params = open_api_models.Params(
             action='GetApiDestination',
             version='2020-04-01',
             protocol='HTTPS',
@@ -1860,18 +1848,16 @@
         request: eventbridge_20200401_models.ListApiDestinationsRequest,
         runtime: util_models.RuntimeOptions,
     ) -> eventbridge_20200401_models.ListApiDestinationsResponse:
         UtilClient.validate_model(request)
         query = {}
         if not UtilClient.is_unset(request.api_destination_name_prefix):
             query['ApiDestinationNamePrefix'] = request.api_destination_name_prefix
-        if not UtilClient.is_unset(request.client_token):
-            query['ClientToken'] = request.client_token
-        if not UtilClient.is_unset(request.description):
-            query['Description'] = request.description
+        if not UtilClient.is_unset(request.connection_name):
+            query['ConnectionName'] = request.connection_name
         if not UtilClient.is_unset(request.max_results):
             query['MaxResults'] = request.max_results
         if not UtilClient.is_unset(request.next_token):
             query['NextToken'] = request.next_token
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
@@ -1896,18 +1882,16 @@
         request: eventbridge_20200401_models.ListApiDestinationsRequest,
         runtime: util_models.RuntimeOptions,
     ) -> eventbridge_20200401_models.ListApiDestinationsResponse:
         UtilClient.validate_model(request)
         query = {}
         if not UtilClient.is_unset(request.api_destination_name_prefix):
             query['ApiDestinationNamePrefix'] = request.api_destination_name_prefix
-        if not UtilClient.is_unset(request.client_token):
-            query['ClientToken'] = request.client_token
-        if not UtilClient.is_unset(request.description):
-            query['Description'] = request.description
+        if not UtilClient.is_unset(request.connection_name):
+            query['ConnectionName'] = request.connection_name
         if not UtilClient.is_unset(request.max_results):
             query['MaxResults'] = request.max_results
         if not UtilClient.is_unset(request.next_token):
             query['NextToken'] = request.next_token
         req = open_api_models.OpenApiRequest(
             query=OpenApiUtilClient.query(query)
         )
@@ -2866,16 +2850,14 @@
         request = eventbridge_20200401_models.UpdateApiDestinationShrinkRequest()
         OpenApiUtilClient.convert(tmp_req, request)
         if not UtilClient.is_unset(tmp_req.http_api_parameters):
             request.http_api_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
         query = {}
         if not UtilClient.is_unset(request.api_destination_name):
             query['ApiDestinationName'] = request.api_destination_name
-        if not UtilClient.is_unset(request.client_token):
-            query['ClientToken'] = request.client_token
         if not UtilClient.is_unset(request.connection_name):
             query['ConnectionName'] = request.connection_name
         if not UtilClient.is_unset(request.description):
             query['Description'] = request.description
         if not UtilClient.is_unset(request.http_api_parameters_shrink):
             query['HttpApiParameters'] = request.http_api_parameters_shrink
         req = open_api_models.OpenApiRequest(
@@ -2906,16 +2888,14 @@
         request = eventbridge_20200401_models.UpdateApiDestinationShrinkRequest()
         OpenApiUtilClient.convert(tmp_req, request)
         if not UtilClient.is_unset(tmp_req.http_api_parameters):
             request.http_api_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.http_api_parameters, 'HttpApiParameters', 'json')
         query = {}
         if not UtilClient.is_unset(request.api_destination_name):
             query['ApiDestinationName'] = request.api_destination_name
-        if not UtilClient.is_unset(request.client_token):
-            query['ClientToken'] = request.client_token
         if not UtilClient.is_unset(request.connection_name):
             query['ConnectionName'] = request.connection_name
         if not UtilClient.is_unset(request.description):
             query['Description'] = request.description
         if not UtilClient.is_unset(request.http_api_parameters_shrink):
             query['HttpApiParameters'] = request.http_api_parameters_shrink
         req = open_api_models.OpenApiRequest(
```

### Comparing `alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401/models.py` & `alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401/models.py`

 * *Files 1% similar despite different names*

```diff
@@ -40,21 +40,19 @@
 class CreateApiDestinationRequest(TeaModel):
     def __init__(
         self,
         api_destination_name: str = None,
         connection_name: str = None,
         description: str = None,
         http_api_parameters: CreateApiDestinationRequestHttpApiParameters = None,
-        invocation_rate_limit_per_second: int = None,
     ):
         self.api_destination_name = api_destination_name
         self.connection_name = connection_name
         self.description = description
         self.http_api_parameters = http_api_parameters
-        self.invocation_rate_limit_per_second = invocation_rate_limit_per_second
 
     def validate(self):
         if self.http_api_parameters:
             self.http_api_parameters.validate()
 
     def to_map(self):
         _map = super().to_map()
@@ -66,48 +64,42 @@
             result['ApiDestinationName'] = self.api_destination_name
         if self.connection_name is not None:
             result['ConnectionName'] = self.connection_name
         if self.description is not None:
             result['Description'] = self.description
         if self.http_api_parameters is not None:
             result['HttpApiParameters'] = self.http_api_parameters.to_map()
-        if self.invocation_rate_limit_per_second is not None:
-            result['InvocationRateLimitPerSecond'] = self.invocation_rate_limit_per_second
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('ApiDestinationName') is not None:
             self.api_destination_name = m.get('ApiDestinationName')
         if m.get('ConnectionName') is not None:
             self.connection_name = m.get('ConnectionName')
         if m.get('Description') is not None:
             self.description = m.get('Description')
         if m.get('HttpApiParameters') is not None:
             temp_model = CreateApiDestinationRequestHttpApiParameters()
             self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
-        if m.get('InvocationRateLimitPerSecond') is not None:
-            self.invocation_rate_limit_per_second = m.get('InvocationRateLimitPerSecond')
         return self
 
 
 class CreateApiDestinationShrinkRequest(TeaModel):
     def __init__(
         self,
         api_destination_name: str = None,
         connection_name: str = None,
         description: str = None,
         http_api_parameters_shrink: str = None,
-        invocation_rate_limit_per_second: int = None,
     ):
         self.api_destination_name = api_destination_name
         self.connection_name = connection_name
         self.description = description
         self.http_api_parameters_shrink = http_api_parameters_shrink
-        self.invocation_rate_limit_per_second = invocation_rate_limit_per_second
 
     def validate(self):
         pass
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
@@ -118,30 +110,26 @@
             result['ApiDestinationName'] = self.api_destination_name
         if self.connection_name is not None:
             result['ConnectionName'] = self.connection_name
         if self.description is not None:
             result['Description'] = self.description
         if self.http_api_parameters_shrink is not None:
             result['HttpApiParameters'] = self.http_api_parameters_shrink
-        if self.invocation_rate_limit_per_second is not None:
-            result['InvocationRateLimitPerSecond'] = self.invocation_rate_limit_per_second
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('ApiDestinationName') is not None:
             self.api_destination_name = m.get('ApiDestinationName')
         if m.get('ConnectionName') is not None:
             self.connection_name = m.get('ConnectionName')
         if m.get('Description') is not None:
             self.description = m.get('Description')
         if m.get('HttpApiParameters') is not None:
             self.http_api_parameters_shrink = m.get('HttpApiParameters')
-        if m.get('InvocationRateLimitPerSecond') is not None:
-            self.invocation_rate_limit_per_second = m.get('InvocationRateLimitPerSecond')
         return self
 
 
 class CreateApiDestinationResponseBodyDate(TeaModel):
     def __init__(
         self,
         api_destination_name: str = None,
@@ -321,178 +309,14 @@
         if m.get('Password') is not None:
             self.password = m.get('Password')
         if m.get('Username') is not None:
             self.username = m.get('Username')
         return self
 
 
-class CreateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters(TeaModel):
-    def __init__(
-        self,
-        key: str = None,
-        value: str = None,
-    ):
-        self.key = key
-        self.value = value
-
-    def validate(self):
-        pass
-
-    def to_map(self):
-        _map = super().to_map()
-        if _map is not None:
-            return _map
-
-        result = dict()
-        if self.key is not None:
-            result['Key'] = self.key
-        if self.value is not None:
-            result['Value'] = self.value
-        return result
-
-    def from_map(self, m: dict = None):
-        m = m or dict()
-        if m.get('Key') is not None:
-            self.key = m.get('Key')
-        if m.get('Value') is not None:
-            self.value = m.get('Value')
-        return self
-
-
-class CreateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters(TeaModel):
-    def __init__(
-        self,
-        key: str = None,
-        value: str = None,
-    ):
-        self.key = key
-        self.value = value
-
-    def validate(self):
-        pass
-
-    def to_map(self):
-        _map = super().to_map()
-        if _map is not None:
-            return _map
-
-        result = dict()
-        if self.key is not None:
-            result['Key'] = self.key
-        if self.value is not None:
-            result['Value'] = self.value
-        return result
-
-    def from_map(self, m: dict = None):
-        m = m or dict()
-        if m.get('Key') is not None:
-            self.key = m.get('Key')
-        if m.get('Value') is not None:
-            self.value = m.get('Value')
-        return self
-
-
-class CreateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters(TeaModel):
-    def __init__(
-        self,
-        key: str = None,
-        value: str = None,
-    ):
-        self.key = key
-        self.value = value
-
-    def validate(self):
-        pass
-
-    def to_map(self):
-        _map = super().to_map()
-        if _map is not None:
-            return _map
-
-        result = dict()
-        if self.key is not None:
-            result['Key'] = self.key
-        if self.value is not None:
-            result['Value'] = self.value
-        return result
-
-    def from_map(self, m: dict = None):
-        m = m or dict()
-        if m.get('Key') is not None:
-            self.key = m.get('Key')
-        if m.get('Value') is not None:
-            self.value = m.get('Value')
-        return self
-
-
-class CreateConnectionRequestAuthParametersInvocationHttpParameters(TeaModel):
-    def __init__(
-        self,
-        body_parameters: List[CreateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters] = None,
-        header_parameters: List[CreateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters] = None,
-        query_string_parameters: List[CreateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters] = None,
-    ):
-        self.body_parameters = body_parameters
-        self.header_parameters = header_parameters
-        self.query_string_parameters = query_string_parameters
-
-    def validate(self):
-        if self.body_parameters:
-            for k in self.body_parameters:
-                if k:
-                    k.validate()
-        if self.header_parameters:
-            for k in self.header_parameters:
-                if k:
-                    k.validate()
-        if self.query_string_parameters:
-            for k in self.query_string_parameters:
-                if k:
-                    k.validate()
-
-    def to_map(self):
-        _map = super().to_map()
-        if _map is not None:
-            return _map
-
-        result = dict()
-        result['BodyParameters'] = []
-        if self.body_parameters is not None:
-            for k in self.body_parameters:
-                result['BodyParameters'].append(k.to_map() if k else None)
-        result['HeaderParameters'] = []
-        if self.header_parameters is not None:
-            for k in self.header_parameters:
-                result['HeaderParameters'].append(k.to_map() if k else None)
-        result['QueryStringParameters'] = []
-        if self.query_string_parameters is not None:
-            for k in self.query_string_parameters:
-                result['QueryStringParameters'].append(k.to_map() if k else None)
-        return result
-
-    def from_map(self, m: dict = None):
-        m = m or dict()
-        self.body_parameters = []
-        if m.get('BodyParameters') is not None:
-            for k in m.get('BodyParameters'):
-                temp_model = CreateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters()
-                self.body_parameters.append(temp_model.from_map(k))
-        self.header_parameters = []
-        if m.get('HeaderParameters') is not None:
-            for k in m.get('HeaderParameters'):
-                temp_model = CreateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters()
-                self.header_parameters.append(temp_model.from_map(k))
-        self.query_string_parameters = []
-        if m.get('QueryStringParameters') is not None:
-            for k in m.get('QueryStringParameters'):
-                temp_model = CreateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters()
-                self.query_string_parameters.append(temp_model.from_map(k))
-        return self
-
-
 class CreateConnectionRequestAuthParametersOAuthParametersClientParameters(TeaModel):
     def __init__(
         self,
         client_id: str = None,
         client_secret: str = None,
     ):
         self.client_id = client_id
@@ -756,30 +580,26 @@
 
 class CreateConnectionRequestAuthParameters(TeaModel):
     def __init__(
         self,
         api_key_auth_parameters: CreateConnectionRequestAuthParametersApiKeyAuthParameters = None,
         authorization_type: str = None,
         basic_auth_parameters: CreateConnectionRequestAuthParametersBasicAuthParameters = None,
-        invocation_http_parameters: CreateConnectionRequestAuthParametersInvocationHttpParameters = None,
         oauth_parameters: CreateConnectionRequestAuthParametersOAuthParameters = None,
     ):
         self.api_key_auth_parameters = api_key_auth_parameters
         self.authorization_type = authorization_type
         self.basic_auth_parameters = basic_auth_parameters
-        self.invocation_http_parameters = invocation_http_parameters
         self.oauth_parameters = oauth_parameters
 
     def validate(self):
         if self.api_key_auth_parameters:
             self.api_key_auth_parameters.validate()
         if self.basic_auth_parameters:
             self.basic_auth_parameters.validate()
-        if self.invocation_http_parameters:
-            self.invocation_http_parameters.validate()
         if self.oauth_parameters:
             self.oauth_parameters.validate()
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
@@ -787,33 +607,28 @@
         result = dict()
         if self.api_key_auth_parameters is not None:
             result['ApiKeyAuthParameters'] = self.api_key_auth_parameters.to_map()
         if self.authorization_type is not None:
             result['AuthorizationType'] = self.authorization_type
         if self.basic_auth_parameters is not None:
             result['BasicAuthParameters'] = self.basic_auth_parameters.to_map()
-        if self.invocation_http_parameters is not None:
-            result['InvocationHttpParameters'] = self.invocation_http_parameters.to_map()
         if self.oauth_parameters is not None:
             result['OAuthParameters'] = self.oauth_parameters.to_map()
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('ApiKeyAuthParameters') is not None:
             temp_model = CreateConnectionRequestAuthParametersApiKeyAuthParameters()
             self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
         if m.get('AuthorizationType') is not None:
             self.authorization_type = m.get('AuthorizationType')
         if m.get('BasicAuthParameters') is not None:
             temp_model = CreateConnectionRequestAuthParametersBasicAuthParameters()
             self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
-        if m.get('InvocationHttpParameters') is not None:
-            temp_model = CreateConnectionRequestAuthParametersInvocationHttpParameters()
-            self.invocation_http_parameters = temp_model.from_map(m['InvocationHttpParameters'])
         if m.get('OAuthParameters') is not None:
             temp_model = CreateConnectionRequestAuthParametersOAuthParameters()
             self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
         return self
 
 
 class CreateConnectionRequestNetworkParameters(TeaModel):
@@ -1367,22 +1182,32 @@
 
 
 class CreateEventSourceRequestSourceRocketMQParameters(TeaModel):
     def __init__(
         self,
         group_id: str = None,
         instance_id: str = None,
+        instance_network: str = None,
+        instance_security_group_id: str = None,
+        instance_type: str = None,
+        instance_vswitch_ids: str = None,
+        instance_vpc_id: str = None,
         offset: str = None,
         region_id: str = None,
         tag: str = None,
         timestamp: float = None,
         topic: str = None,
     ):
         self.group_id = group_id
         self.instance_id = instance_id
+        self.instance_network = instance_network
+        self.instance_security_group_id = instance_security_group_id
+        self.instance_type = instance_type
+        self.instance_vswitch_ids = instance_vswitch_ids
+        self.instance_vpc_id = instance_vpc_id
         self.offset = offset
         self.region_id = region_id
         self.tag = tag
         self.timestamp = timestamp
         self.topic = topic
 
     def validate(self):
@@ -1391,35 +1216,55 @@
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
         if self.group_id is not None:
-            result['GroupId'] = self.group_id
+            result['GroupID'] = self.group_id
         if self.instance_id is not None:
             result['InstanceId'] = self.instance_id
+        if self.instance_network is not None:
+            result['InstanceNetwork'] = self.instance_network
+        if self.instance_security_group_id is not None:
+            result['InstanceSecurityGroupId'] = self.instance_security_group_id
+        if self.instance_type is not None:
+            result['InstanceType'] = self.instance_type
+        if self.instance_vswitch_ids is not None:
+            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
+        if self.instance_vpc_id is not None:
+            result['InstanceVpcId'] = self.instance_vpc_id
         if self.offset is not None:
             result['Offset'] = self.offset
         if self.region_id is not None:
             result['RegionId'] = self.region_id
         if self.tag is not None:
             result['Tag'] = self.tag
         if self.timestamp is not None:
             result['Timestamp'] = self.timestamp
         if self.topic is not None:
             result['Topic'] = self.topic
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
-        if m.get('GroupId') is not None:
-            self.group_id = m.get('GroupId')
+        if m.get('GroupID') is not None:
+            self.group_id = m.get('GroupID')
         if m.get('InstanceId') is not None:
             self.instance_id = m.get('InstanceId')
+        if m.get('InstanceNetwork') is not None:
+            self.instance_network = m.get('InstanceNetwork')
+        if m.get('InstanceSecurityGroupId') is not None:
+            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
+        if m.get('InstanceType') is not None:
+            self.instance_type = m.get('InstanceType')
+        if m.get('InstanceVSwitchIds') is not None:
+            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
+        if m.get('InstanceVpcId') is not None:
+            self.instance_vpc_id = m.get('InstanceVpcId')
         if m.get('Offset') is not None:
             self.offset = m.get('Offset')
         if m.get('RegionId') is not None:
             self.region_id = m.get('RegionId')
         if m.get('Tag') is not None:
             self.tag = m.get('Tag')
         if m.get('Timestamp') is not None:
@@ -6101,40 +5946,34 @@
         return self
 
 
 class DeleteApiDestinationRequest(TeaModel):
     def __init__(
         self,
         api_destination_name: str = None,
-        client_token: str = None,
     ):
         self.api_destination_name = api_destination_name
-        self.client_token = client_token
 
     def validate(self):
         pass
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
         if self.api_destination_name is not None:
             result['ApiDestinationName'] = self.api_destination_name
-        if self.client_token is not None:
-            result['ClientToken'] = self.client_token
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('ApiDestinationName') is not None:
             self.api_destination_name = m.get('ApiDestinationName')
-        if m.get('ClientToken') is not None:
-            self.client_token = m.get('ClientToken')
         return self
 
 
 class DeleteApiDestinationResponseBody(TeaModel):
     def __init__(
         self,
         code: str = None,
@@ -7297,40 +7136,34 @@
         return self
 
 
 class GetApiDestinationRequest(TeaModel):
     def __init__(
         self,
         api_destination_name: str = None,
-        client_token: str = None,
     ):
         self.api_destination_name = api_destination_name
-        self.client_token = client_token
 
     def validate(self):
         pass
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
         if self.api_destination_name is not None:
             result['ApiDestinationName'] = self.api_destination_name
-        if self.client_token is not None:
-            result['ClientToken'] = self.client_token
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('ApiDestinationName') is not None:
             self.api_destination_name = m.get('ApiDestinationName')
-        if m.get('ClientToken') is not None:
-            self.client_token = m.get('ClientToken')
         return self
 
 
 class GetApiDestinationResponseBodyDataHttpApiParameters(TeaModel):
     def __init__(
         self,
         endpoint: str = None,
@@ -8135,23 +7968,21 @@
             self.vswitche_id = m.get('VswitcheId')
         return self
 
 
 class GetConnectionResponseBodyDataConnections(TeaModel):
     def __init__(
         self,
-        api_destination_name: str = None,
         auth_parameters: GetConnectionResponseBodyDataConnectionsAuthParameters = None,
         connection_name: str = None,
         description: str = None,
         gmt_create: int = None,
         id: int = None,
         network_parameters: GetConnectionResponseBodyDataConnectionsNetworkParameters = None,
     ):
-        self.api_destination_name = api_destination_name
         self.auth_parameters = auth_parameters
         self.connection_name = connection_name
         self.description = description
         self.gmt_create = gmt_create
         self.id = id
         self.network_parameters = network_parameters
 
@@ -8163,16 +7994,14 @@
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
-        if self.api_destination_name is not None:
-            result['ApiDestinationName'] = self.api_destination_name
         if self.auth_parameters is not None:
             result['AuthParameters'] = self.auth_parameters.to_map()
         if self.connection_name is not None:
             result['ConnectionName'] = self.connection_name
         if self.description is not None:
             result['Description'] = self.description
         if self.gmt_create is not None:
@@ -8181,16 +8010,14 @@
             result['Id'] = self.id
         if self.network_parameters is not None:
             result['NetworkParameters'] = self.network_parameters.to_map()
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
-        if m.get('ApiDestinationName') is not None:
-            self.api_destination_name = m.get('ApiDestinationName')
         if m.get('AuthParameters') is not None:
             temp_model = GetConnectionResponseBodyDataConnectionsAuthParameters()
             self.auth_parameters = temp_model.from_map(m['AuthParameters'])
         if m.get('ConnectionName') is not None:
             self.connection_name = m.get('ConnectionName')
         if m.get('Description') is not None:
             self.description = m.get('Description')
@@ -11504,23 +11331,25 @@
     def __init__(
         self,
         arn: str = None,
         ctime: float = None,
         description: str = None,
         event_bus_name: str = None,
         event_types: List[ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes] = None,
+        full_name: str = None,
         name: str = None,
         status: str = None,
         type: str = None,
     ):
         self.arn = arn
         self.ctime = ctime
         self.description = description
         self.event_bus_name = event_bus_name
         self.event_types = event_types
+        self.full_name = full_name
         self.name = name
         self.status = status
         self.type = type
 
     def validate(self):
         if self.event_types:
             for k in self.event_types:
@@ -11541,14 +11370,16 @@
             result['Description'] = self.description
         if self.event_bus_name is not None:
             result['EventBusName'] = self.event_bus_name
         result['EventTypes'] = []
         if self.event_types is not None:
             for k in self.event_types:
                 result['EventTypes'].append(k.to_map() if k else None)
+        if self.full_name is not None:
+            result['FullName'] = self.full_name
         if self.name is not None:
             result['Name'] = self.name
         if self.status is not None:
             result['Status'] = self.status
         if self.type is not None:
             result['Type'] = self.type
         return result
@@ -11564,14 +11395,16 @@
         if m.get('EventBusName') is not None:
             self.event_bus_name = m.get('EventBusName')
         self.event_types = []
         if m.get('EventTypes') is not None:
             for k in m.get('EventTypes'):
                 temp_model = ListAliyunOfficialEventSourcesResponseBodyDataEventSourceListEventTypes()
                 self.event_types.append(temp_model.from_map(k))
+        if m.get('FullName') is not None:
+            self.full_name = m.get('FullName')
         if m.get('Name') is not None:
             self.name = m.get('Name')
         if m.get('Status') is not None:
             self.status = m.get('Status')
         if m.get('Type') is not None:
             self.type = m.get('Type')
         return self
@@ -11709,54 +11542,48 @@
         return self
 
 
 class ListApiDestinationsRequest(TeaModel):
     def __init__(
         self,
         api_destination_name_prefix: str = None,
-        client_token: str = None,
-        description: str = None,
+        connection_name: str = None,
         max_results: int = None,
         next_token: str = None,
     ):
         self.api_destination_name_prefix = api_destination_name_prefix
-        self.client_token = client_token
-        self.description = description
+        self.connection_name = connection_name
         self.max_results = max_results
         self.next_token = next_token
 
     def validate(self):
         pass
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
         if self.api_destination_name_prefix is not None:
             result['ApiDestinationNamePrefix'] = self.api_destination_name_prefix
-        if self.client_token is not None:
-            result['ClientToken'] = self.client_token
-        if self.description is not None:
-            result['Description'] = self.description
+        if self.connection_name is not None:
+            result['ConnectionName'] = self.connection_name
         if self.max_results is not None:
             result['MaxResults'] = self.max_results
         if self.next_token is not None:
             result['NextToken'] = self.next_token
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('ApiDestinationNamePrefix') is not None:
             self.api_destination_name_prefix = m.get('ApiDestinationNamePrefix')
-        if m.get('ClientToken') is not None:
-            self.client_token = m.get('ClientToken')
-        if m.get('Description') is not None:
-            self.description = m.get('Description')
+        if m.get('ConnectionName') is not None:
+            self.connection_name = m.get('ConnectionName')
         if m.get('MaxResults') is not None:
             self.max_results = m.get('MaxResults')
         if m.get('NextToken') is not None:
             self.next_token = m.get('NextToken')
         return self
 
 
@@ -11846,16 +11673,22 @@
         return self
 
 
 class ListApiDestinationsResponseBodyData(TeaModel):
     def __init__(
         self,
         api_destinations: List[ListApiDestinationsResponseBodyDataApiDestinations] = None,
+        max_results: float = None,
+        next_token: str = None,
+        total: float = None,
     ):
         self.api_destinations = api_destinations
+        self.max_results = max_results
+        self.next_token = next_token
+        self.total = total
 
     def validate(self):
         if self.api_destinations:
             for k in self.api_destinations:
                 if k:
                     k.validate()
 
@@ -11865,23 +11698,35 @@
             return _map
 
         result = dict()
         result['ApiDestinations'] = []
         if self.api_destinations is not None:
             for k in self.api_destinations:
                 result['ApiDestinations'].append(k.to_map() if k else None)
+        if self.max_results is not None:
+            result['MaxResults'] = self.max_results
+        if self.next_token is not None:
+            result['NextToken'] = self.next_token
+        if self.total is not None:
+            result['Total'] = self.total
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         self.api_destinations = []
         if m.get('ApiDestinations') is not None:
             for k in m.get('ApiDestinations'):
                 temp_model = ListApiDestinationsResponseBodyDataApiDestinations()
                 self.api_destinations.append(temp_model.from_map(k))
+        if m.get('MaxResults') is not None:
+            self.max_results = m.get('MaxResults')
+        if m.get('NextToken') is not None:
+            self.next_token = m.get('NextToken')
+        if m.get('Total') is not None:
+            self.total = m.get('Total')
         return self
 
 
 class ListApiDestinationsResponseBody(TeaModel):
     def __init__(
         self,
         code: str = None,
@@ -12612,23 +12457,21 @@
             self.vswitche_id = m.get('VswitcheId')
         return self
 
 
 class ListConnectionsResponseBodyDataConnections(TeaModel):
     def __init__(
         self,
-        api_destination_name: str = None,
         auth_parameters: ListConnectionsResponseBodyDataConnectionsAuthParameters = None,
         connection_name: str = None,
         description: str = None,
         gmt_create: int = None,
         id: int = None,
         network_parameters: ListConnectionsResponseBodyDataConnectionsNetworkParameters = None,
     ):
-        self.api_destination_name = api_destination_name
         self.auth_parameters = auth_parameters
         self.connection_name = connection_name
         self.description = description
         self.gmt_create = gmt_create
         self.id = id
         self.network_parameters = network_parameters
 
@@ -12640,16 +12483,14 @@
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
-        if self.api_destination_name is not None:
-            result['ApiDestinationName'] = self.api_destination_name
         if self.auth_parameters is not None:
             result['AuthParameters'] = self.auth_parameters.to_map()
         if self.connection_name is not None:
             result['ConnectionName'] = self.connection_name
         if self.description is not None:
             result['Description'] = self.description
         if self.gmt_create is not None:
@@ -12658,16 +12499,14 @@
             result['Id'] = self.id
         if self.network_parameters is not None:
             result['NetworkParameters'] = self.network_parameters.to_map()
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
-        if m.get('ApiDestinationName') is not None:
-            self.api_destination_name = m.get('ApiDestinationName')
         if m.get('AuthParameters') is not None:
             temp_model = ListConnectionsResponseBodyDataConnectionsAuthParameters()
             self.auth_parameters = temp_model.from_map(m['AuthParameters'])
         if m.get('ConnectionName') is not None:
             self.connection_name = m.get('ConnectionName')
         if m.get('Description') is not None:
             self.description = m.get('Description')
@@ -18042,21 +17881,19 @@
         return self
 
 
 class UpdateApiDestinationRequest(TeaModel):
     def __init__(
         self,
         api_destination_name: str = None,
-        client_token: str = None,
         connection_name: str = None,
         description: str = None,
         http_api_parameters: UpdateApiDestinationRequestHttpApiParameters = None,
     ):
         self.api_destination_name = api_destination_name
-        self.client_token = client_token
         self.connection_name = connection_name
         self.description = description
         self.http_api_parameters = http_api_parameters
 
     def validate(self):
         if self.http_api_parameters:
             self.http_api_parameters.validate()
@@ -18065,51 +17902,45 @@
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
         if self.api_destination_name is not None:
             result['ApiDestinationName'] = self.api_destination_name
-        if self.client_token is not None:
-            result['ClientToken'] = self.client_token
         if self.connection_name is not None:
             result['ConnectionName'] = self.connection_name
         if self.description is not None:
             result['Description'] = self.description
         if self.http_api_parameters is not None:
             result['HttpApiParameters'] = self.http_api_parameters.to_map()
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('ApiDestinationName') is not None:
             self.api_destination_name = m.get('ApiDestinationName')
-        if m.get('ClientToken') is not None:
-            self.client_token = m.get('ClientToken')
         if m.get('ConnectionName') is not None:
             self.connection_name = m.get('ConnectionName')
         if m.get('Description') is not None:
             self.description = m.get('Description')
         if m.get('HttpApiParameters') is not None:
             temp_model = UpdateApiDestinationRequestHttpApiParameters()
             self.http_api_parameters = temp_model.from_map(m['HttpApiParameters'])
         return self
 
 
 class UpdateApiDestinationShrinkRequest(TeaModel):
     def __init__(
         self,
         api_destination_name: str = None,
-        client_token: str = None,
         connection_name: str = None,
         description: str = None,
         http_api_parameters_shrink: str = None,
     ):
         self.api_destination_name = api_destination_name
-        self.client_token = client_token
         self.connection_name = connection_name
         self.description = description
         self.http_api_parameters_shrink = http_api_parameters_shrink
 
     def validate(self):
         pass
 
@@ -18117,30 +17948,26 @@
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
         if self.api_destination_name is not None:
             result['ApiDestinationName'] = self.api_destination_name
-        if self.client_token is not None:
-            result['ClientToken'] = self.client_token
         if self.connection_name is not None:
             result['ConnectionName'] = self.connection_name
         if self.description is not None:
             result['Description'] = self.description
         if self.http_api_parameters_shrink is not None:
             result['HttpApiParameters'] = self.http_api_parameters_shrink
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('ApiDestinationName') is not None:
             self.api_destination_name = m.get('ApiDestinationName')
-        if m.get('ClientToken') is not None:
-            self.client_token = m.get('ClientToken')
         if m.get('ConnectionName') is not None:
             self.connection_name = m.get('ConnectionName')
         if m.get('Description') is not None:
             self.description = m.get('Description')
         if m.get('HttpApiParameters') is not None:
             self.http_api_parameters_shrink = m.get('HttpApiParameters')
         return self
@@ -18298,178 +18125,14 @@
         if m.get('Password') is not None:
             self.password = m.get('Password')
         if m.get('Username') is not None:
             self.username = m.get('Username')
         return self
 
 
-class UpdateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters(TeaModel):
-    def __init__(
-        self,
-        key: str = None,
-        value: str = None,
-    ):
-        self.key = key
-        self.value = value
-
-    def validate(self):
-        pass
-
-    def to_map(self):
-        _map = super().to_map()
-        if _map is not None:
-            return _map
-
-        result = dict()
-        if self.key is not None:
-            result['Key'] = self.key
-        if self.value is not None:
-            result['Value'] = self.value
-        return result
-
-    def from_map(self, m: dict = None):
-        m = m or dict()
-        if m.get('Key') is not None:
-            self.key = m.get('Key')
-        if m.get('Value') is not None:
-            self.value = m.get('Value')
-        return self
-
-
-class UpdateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters(TeaModel):
-    def __init__(
-        self,
-        key: str = None,
-        value: str = None,
-    ):
-        self.key = key
-        self.value = value
-
-    def validate(self):
-        pass
-
-    def to_map(self):
-        _map = super().to_map()
-        if _map is not None:
-            return _map
-
-        result = dict()
-        if self.key is not None:
-            result['Key'] = self.key
-        if self.value is not None:
-            result['Value'] = self.value
-        return result
-
-    def from_map(self, m: dict = None):
-        m = m or dict()
-        if m.get('Key') is not None:
-            self.key = m.get('Key')
-        if m.get('Value') is not None:
-            self.value = m.get('Value')
-        return self
-
-
-class UpdateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters(TeaModel):
-    def __init__(
-        self,
-        key: str = None,
-        value: str = None,
-    ):
-        self.key = key
-        self.value = value
-
-    def validate(self):
-        pass
-
-    def to_map(self):
-        _map = super().to_map()
-        if _map is not None:
-            return _map
-
-        result = dict()
-        if self.key is not None:
-            result['Key'] = self.key
-        if self.value is not None:
-            result['Value'] = self.value
-        return result
-
-    def from_map(self, m: dict = None):
-        m = m or dict()
-        if m.get('Key') is not None:
-            self.key = m.get('Key')
-        if m.get('Value') is not None:
-            self.value = m.get('Value')
-        return self
-
-
-class UpdateConnectionRequestAuthParametersInvocationHttpParameters(TeaModel):
-    def __init__(
-        self,
-        body_parameters: List[UpdateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters] = None,
-        header_parameters: List[UpdateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters] = None,
-        query_string_parameters: List[UpdateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters] = None,
-    ):
-        self.body_parameters = body_parameters
-        self.header_parameters = header_parameters
-        self.query_string_parameters = query_string_parameters
-
-    def validate(self):
-        if self.body_parameters:
-            for k in self.body_parameters:
-                if k:
-                    k.validate()
-        if self.header_parameters:
-            for k in self.header_parameters:
-                if k:
-                    k.validate()
-        if self.query_string_parameters:
-            for k in self.query_string_parameters:
-                if k:
-                    k.validate()
-
-    def to_map(self):
-        _map = super().to_map()
-        if _map is not None:
-            return _map
-
-        result = dict()
-        result['BodyParameters'] = []
-        if self.body_parameters is not None:
-            for k in self.body_parameters:
-                result['BodyParameters'].append(k.to_map() if k else None)
-        result['HeaderParameters'] = []
-        if self.header_parameters is not None:
-            for k in self.header_parameters:
-                result['HeaderParameters'].append(k.to_map() if k else None)
-        result['QueryStringParameters'] = []
-        if self.query_string_parameters is not None:
-            for k in self.query_string_parameters:
-                result['QueryStringParameters'].append(k.to_map() if k else None)
-        return result
-
-    def from_map(self, m: dict = None):
-        m = m or dict()
-        self.body_parameters = []
-        if m.get('BodyParameters') is not None:
-            for k in m.get('BodyParameters'):
-                temp_model = UpdateConnectionRequestAuthParametersInvocationHttpParametersBodyParameters()
-                self.body_parameters.append(temp_model.from_map(k))
-        self.header_parameters = []
-        if m.get('HeaderParameters') is not None:
-            for k in m.get('HeaderParameters'):
-                temp_model = UpdateConnectionRequestAuthParametersInvocationHttpParametersHeaderParameters()
-                self.header_parameters.append(temp_model.from_map(k))
-        self.query_string_parameters = []
-        if m.get('QueryStringParameters') is not None:
-            for k in m.get('QueryStringParameters'):
-                temp_model = UpdateConnectionRequestAuthParametersInvocationHttpParametersQueryStringParameters()
-                self.query_string_parameters.append(temp_model.from_map(k))
-        return self
-
-
 class UpdateConnectionRequestAuthParametersOAuthParametersClientParameters(TeaModel):
     def __init__(
         self,
         client_id: str = None,
         client_secret: str = None,
     ):
         self.client_id = client_id
@@ -18733,30 +18396,26 @@
 
 class UpdateConnectionRequestAuthParameters(TeaModel):
     def __init__(
         self,
         api_key_auth_parameters: UpdateConnectionRequestAuthParametersApiKeyAuthParameters = None,
         authorization_type: str = None,
         basic_auth_parameters: UpdateConnectionRequestAuthParametersBasicAuthParameters = None,
-        invocation_http_parameters: UpdateConnectionRequestAuthParametersInvocationHttpParameters = None,
         oauth_parameters: UpdateConnectionRequestAuthParametersOAuthParameters = None,
     ):
         self.api_key_auth_parameters = api_key_auth_parameters
         self.authorization_type = authorization_type
         self.basic_auth_parameters = basic_auth_parameters
-        self.invocation_http_parameters = invocation_http_parameters
         self.oauth_parameters = oauth_parameters
 
     def validate(self):
         if self.api_key_auth_parameters:
             self.api_key_auth_parameters.validate()
         if self.basic_auth_parameters:
             self.basic_auth_parameters.validate()
-        if self.invocation_http_parameters:
-            self.invocation_http_parameters.validate()
         if self.oauth_parameters:
             self.oauth_parameters.validate()
 
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
@@ -18764,33 +18423,28 @@
         result = dict()
         if self.api_key_auth_parameters is not None:
             result['ApiKeyAuthParameters'] = self.api_key_auth_parameters.to_map()
         if self.authorization_type is not None:
             result['AuthorizationType'] = self.authorization_type
         if self.basic_auth_parameters is not None:
             result['BasicAuthParameters'] = self.basic_auth_parameters.to_map()
-        if self.invocation_http_parameters is not None:
-            result['InvocationHttpParameters'] = self.invocation_http_parameters.to_map()
         if self.oauth_parameters is not None:
             result['OAuthParameters'] = self.oauth_parameters.to_map()
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
         if m.get('ApiKeyAuthParameters') is not None:
             temp_model = UpdateConnectionRequestAuthParametersApiKeyAuthParameters()
             self.api_key_auth_parameters = temp_model.from_map(m['ApiKeyAuthParameters'])
         if m.get('AuthorizationType') is not None:
             self.authorization_type = m.get('AuthorizationType')
         if m.get('BasicAuthParameters') is not None:
             temp_model = UpdateConnectionRequestAuthParametersBasicAuthParameters()
             self.basic_auth_parameters = temp_model.from_map(m['BasicAuthParameters'])
-        if m.get('InvocationHttpParameters') is not None:
-            temp_model = UpdateConnectionRequestAuthParametersInvocationHttpParameters()
-            self.invocation_http_parameters = temp_model.from_map(m['InvocationHttpParameters'])
         if m.get('OAuthParameters') is not None:
             temp_model = UpdateConnectionRequestAuthParametersOAuthParameters()
             self.oauth_parameters = temp_model.from_map(m['OAuthParameters'])
         return self
 
 
 class UpdateConnectionRequestNetworkParameters(TeaModel):
@@ -19274,22 +18928,32 @@
 
 
 class UpdateEventSourceRequestSourceRocketMQParameters(TeaModel):
     def __init__(
         self,
         group_id: str = None,
         instance_id: str = None,
+        instance_network: str = None,
+        instance_security_group_id: str = None,
+        instance_type: str = None,
+        instance_vswitch_ids: str = None,
+        instance_vpc_id: str = None,
         offset: str = None,
         region_id: str = None,
         tag: str = None,
         timestamp: float = None,
         topic: str = None,
     ):
         self.group_id = group_id
         self.instance_id = instance_id
+        self.instance_network = instance_network
+        self.instance_security_group_id = instance_security_group_id
+        self.instance_type = instance_type
+        self.instance_vswitch_ids = instance_vswitch_ids
+        self.instance_vpc_id = instance_vpc_id
         self.offset = offset
         self.region_id = region_id
         self.tag = tag
         self.timestamp = timestamp
         self.topic = topic
 
     def validate(self):
@@ -19298,35 +18962,55 @@
     def to_map(self):
         _map = super().to_map()
         if _map is not None:
             return _map
 
         result = dict()
         if self.group_id is not None:
-            result['GroupId'] = self.group_id
+            result['GroupID'] = self.group_id
         if self.instance_id is not None:
             result['InstanceId'] = self.instance_id
+        if self.instance_network is not None:
+            result['InstanceNetwork'] = self.instance_network
+        if self.instance_security_group_id is not None:
+            result['InstanceSecurityGroupId'] = self.instance_security_group_id
+        if self.instance_type is not None:
+            result['InstanceType'] = self.instance_type
+        if self.instance_vswitch_ids is not None:
+            result['InstanceVSwitchIds'] = self.instance_vswitch_ids
+        if self.instance_vpc_id is not None:
+            result['InstanceVpcId'] = self.instance_vpc_id
         if self.offset is not None:
             result['Offset'] = self.offset
         if self.region_id is not None:
             result['RegionId'] = self.region_id
         if self.tag is not None:
             result['Tag'] = self.tag
         if self.timestamp is not None:
             result['Timestamp'] = self.timestamp
         if self.topic is not None:
             result['Topic'] = self.topic
         return result
 
     def from_map(self, m: dict = None):
         m = m or dict()
-        if m.get('GroupId') is not None:
-            self.group_id = m.get('GroupId')
+        if m.get('GroupID') is not None:
+            self.group_id = m.get('GroupID')
         if m.get('InstanceId') is not None:
             self.instance_id = m.get('InstanceId')
+        if m.get('InstanceNetwork') is not None:
+            self.instance_network = m.get('InstanceNetwork')
+        if m.get('InstanceSecurityGroupId') is not None:
+            self.instance_security_group_id = m.get('InstanceSecurityGroupId')
+        if m.get('InstanceType') is not None:
+            self.instance_type = m.get('InstanceType')
+        if m.get('InstanceVSwitchIds') is not None:
+            self.instance_vswitch_ids = m.get('InstanceVSwitchIds')
+        if m.get('InstanceVpcId') is not None:
+            self.instance_vpc_id = m.get('InstanceVpcId')
         if m.get('Offset') is not None:
             self.offset = m.get('Offset')
         if m.get('RegionId') is not None:
             self.region_id = m.get('RegionId')
         if m.get('Tag') is not None:
             self.tag = m.get('Tag')
         if m.get('Timestamp') is not None:
```

### Comparing `alibabacloud_eventbridge20200401-1.0.5/alibabacloud_eventbridge20200401.egg-info/PKG-INFO` & `alibabacloud_eventbridge20200401-1.0.6/alibabacloud_eventbridge20200401.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: alibabacloud-eventbridge20200401
-Version: 1.0.5
+Version: 1.0.6
 Summary: Alibaba Cloud eventbridge (20200401) SDK Library for Python
 Home-page: https://github.com/aliyun/alibabacloud-python-sdk
 Author: Alibaba Cloud SDK
 Author-email: sdk-team@alibabacloud.com
 License: Apache License 2.0
 Description: English | [简体中文](README-CN.md)
         ![](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)
```

### Comparing `alibabacloud_eventbridge20200401-1.0.5/setup.py` & `alibabacloud_eventbridge20200401-1.0.6/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -20,15 +20,15 @@
 
 import os
 from setuptools import setup, find_packages
 
 """
 setup module for alibabacloud_eventbridge20200401.
 
-Created on 22/03/2023
+Created on 07/04/2023
 
 @author: Alibaba Cloud SDK
 """
 
 PACKAGE = "alibabacloud_eventbridge20200401"
 NAME = "alibabacloud_eventbridge20200401" or "alibabacloud-package"
 DESCRIPTION = "Alibaba Cloud eventbridge (20200401) SDK Library for Python"
```

