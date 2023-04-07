# Comparing `tmp/aliyun-python-sdk-eventbridge-1.0.5.tar.gz` & `tmp/aliyun-python-sdk-eventbridge-1.0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/aliyun-python-sdk-eventbridge-1.0.5.tar", last modified: Tue Mar 21 08:18:11 2023, max compression
+gzip compressed data, was "dist/aliyun-python-sdk-eventbridge-1.0.6.tar", last modified: Fri Apr  7 03:43:53 2023, max compression
```

## Comparing `aliyun-python-sdk-eventbridge-1.0.5.tar` & `aliyun-python-sdk-eventbridge-1.0.6.tar`

### file list

```diff
@@ -1,61 +1,61 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/
--rw-r--r--   0 root         (0) root         (0)      575 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/LICENSE
--rw-r--r--   0 root         (0) root         (0)       40 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1577 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      543 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/README.rst
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyun_python_sdk_eventbridge.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1577 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyun_python_sdk_eventbridge.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     3223 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyun_python_sdk_eventbridge.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyun_python_sdk_eventbridge.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       31 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyun_python_sdk_eventbridge.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       21 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyun_python_sdk_eventbridge.egg-info/top_level.txt
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/
--rw-r--r--   0 root         (0) root         (0)       21 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/
--rw-r--r--   0 root         (0) root         (0)     2221 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateApiDestinationRequest.py
--rw-r--r--   0 root         (0) root         (0)     1906 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateConnectionRequest.py
--rw-r--r--   0 root         (0) root         (0)     1406 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateEventBusRequest.py
--rw-r--r--   0 root         (0) root         (0)     3018 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateEventSourceRequest.py
--rw-r--r--   0 root         (0) root         (0)     2218 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateEventStreamingRequest.py
--rw-r--r--   0 root         (0) root         (0)     2178 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateRuleRequest.py
--rw-r--r--   0 root         (0) root         (0)     1241 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateServiceLinkedRoleForProductRequest.py
--rw-r--r--   0 root         (0) root         (0)     1581 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateTargetsRequest.py
--rw-r--r--   0 root         (0) root         (0)     1454 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteApiDestinationRequest.py
--rw-r--r--   0 root         (0) root         (0)     1225 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteConnectionRequest.py
--rw-r--r--   0 root         (0) root         (0)     1209 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteEventBusRequest.py
--rw-r--r--   0 root         (0) root         (0)     1232 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteEventSourceRequest.py
--rw-r--r--   0 root         (0) root         (0)     1256 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteEventStreamingRequest.py
--rw-r--r--   0 root         (0) root         (0)     1380 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteRuleRequest.py
--rw-r--r--   0 root         (0) root         (0)     1593 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteTargetsRequest.py
--rw-r--r--   0 root         (0) root         (0)     1382 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DisableRuleRequest.py
--rw-r--r--   0 root         (0) root         (0)     1380 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/EnableRuleRequest.py
--rw-r--r--   0 root         (0) root         (0)     1448 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetApiDestinationRequest.py
--rw-r--r--   0 root         (0) root         (0)     1219 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetConnectionRequest.py
--rw-r--r--   0 root         (0) root         (0)     1203 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetEventBusRequest.py
--rw-r--r--   0 root         (0) root         (0)     1250 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetEventStreamingRequest.py
--rw-r--r--   0 root         (0) root         (0)     1374 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetRuleRequest.py
--rw-r--r--   0 root         (0) root         (0)     1038 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListAliyunOfficialEventSourcesRequest.py
--rw-r--r--   0 root         (0) root         (0)     2057 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListApiDestinationsRequest.py
--rw-r--r--   0 root         (0) root         (0)     1628 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListConnectionsRequest.py
--rw-r--r--   0 root         (0) root         (0)     1545 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListEventBusesRequest.py
--rw-r--r--   0 root         (0) root         (0)     1546 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListEventStreamingsRequest.py
--rw-r--r--   0 root         (0) root         (0)     1762 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListRulesRequest.py
--rw-r--r--   0 root         (0) root         (0)     1032 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListUserDefinedEventSourcesRequest.py
--rw-r--r--   0 root         (0) root         (0)     1254 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/PauseEventStreamingRequest.py
--rw-r--r--   0 root         (0) root         (0)     1575 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/PutTargetsRequest.py
--rw-r--r--   0 root         (0) root         (0)     1374 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/QueryEventRequest.py
--rw-r--r--   0 root         (0) root         (0)     1386 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/QueryEventTracesRequest.py
--rw-r--r--   0 root         (0) root         (0)     1601 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/QueryTracedEventByEventIdRequest.py
--rw-r--r--   0 root         (0) root         (0)     2492 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/QueryTracedEventsRequest.py
--rw-r--r--   0 root         (0) root         (0)     1254 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/StartEventStreamingRequest.py
--rw-r--r--   0 root         (0) root         (0)     2123 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateApiDestinationRequest.py
--rw-r--r--   0 root         (0) root         (0)     1906 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateConnectionRequest.py
--rw-r--r--   0 root         (0) root         (0)     1406 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateEventBusRequest.py
--rw-r--r--   0 root         (0) root         (0)     3018 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateEventSourceRequest.py
--rw-r--r--   0 root         (0) root         (0)     2218 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateEventStreamingRequest.py
--rw-r--r--   0 root         (0) root         (0)     1953 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateRuleRequest.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/__init__.py
--rw-r--r--   0 root         (0) root         (0)      102 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/setup.cfg
--rw-r--r--   0 root         (0) root         (0)     2492 2023-03-21 08:18:11.000000 aliyun-python-sdk-eventbridge-1.0.5/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/
+-rw-r--r--   0 root         (0) root         (0)      575 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/LICENSE
+-rw-r--r--   0 root         (0) root         (0)       40 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1577 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      543 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/README.rst
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyun_python_sdk_eventbridge.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1577 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyun_python_sdk_eventbridge.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     3223 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyun_python_sdk_eventbridge.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyun_python_sdk_eventbridge.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       31 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyun_python_sdk_eventbridge.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       21 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyun_python_sdk_eventbridge.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/
+-rw-r--r--   0 root         (0) root         (0)       21 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/
+-rw-r--r--   0 root         (0) root         (0)     1926 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateApiDestinationRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1906 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateConnectionRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1406 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateEventBusRequest.py
+-rw-r--r--   0 root         (0) root         (0)     3018 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateEventSourceRequest.py
+-rw-r--r--   0 root         (0) root         (0)     2218 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateEventStreamingRequest.py
+-rw-r--r--   0 root         (0) root         (0)     2178 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateRuleRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1241 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateServiceLinkedRoleForProductRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1581 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateTargetsRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1257 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteApiDestinationRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1225 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteConnectionRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1209 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteEventBusRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1232 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteEventSourceRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1256 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteEventStreamingRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1380 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteRuleRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1593 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteTargetsRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1382 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DisableRuleRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1380 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/EnableRuleRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1251 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetApiDestinationRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1219 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetConnectionRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1203 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetEventBusRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1250 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetEventStreamingRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1374 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetRuleRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1038 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListAliyunOfficialEventSourcesRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1878 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListApiDestinationsRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1628 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListConnectionsRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1545 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListEventBusesRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1546 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListEventStreamingsRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1762 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListRulesRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1032 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListUserDefinedEventSourcesRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1254 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/PauseEventStreamingRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1575 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/PutTargetsRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1374 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/QueryEventRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1386 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/QueryEventTracesRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1601 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/QueryTracedEventByEventIdRequest.py
+-rw-r--r--   0 root         (0) root         (0)     2492 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/QueryTracedEventsRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1254 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/StartEventStreamingRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1926 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateApiDestinationRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1906 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateConnectionRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1406 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateEventBusRequest.py
+-rw-r--r--   0 root         (0) root         (0)     3018 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateEventSourceRequest.py
+-rw-r--r--   0 root         (0) root         (0)     2218 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateEventStreamingRequest.py
+-rw-r--r--   0 root         (0) root         (0)     1953 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateRuleRequest.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      102 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)     2492 2023-04-07 03:43:53.000000 aliyun-python-sdk-eventbridge-1.0.6/setup.py
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/LICENSE` & `aliyun-python-sdk-eventbridge-1.0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/PKG-INFO` & `aliyun-python-sdk-eventbridge-1.0.6/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: aliyun-python-sdk-eventbridge
-Version: 1.0.5
+Version: 1.0.6
 Summary: The eventbridge module of Aliyun Python sdk.
 Home-page: http://develop.aliyun.com/sdk/python
 Author: Aliyun
 Author-email: aliyun-developers-efficiency@list.alibaba-inc.com
 License: Apache
 Description: =============================================================
         aliyun-python-sdk-eventbridge
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/README.rst` & `aliyun-python-sdk-eventbridge-1.0.6/README.rst`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyun_python_sdk_eventbridge.egg-info/PKG-INFO` & `aliyun-python-sdk-eventbridge-1.0.6/aliyun_python_sdk_eventbridge.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: aliyun-python-sdk-eventbridge
-Version: 1.0.5
+Version: 1.0.6
 Summary: The eventbridge module of Aliyun Python sdk.
 Home-page: http://develop.aliyun.com/sdk/python
 Author: Aliyun
 Author-email: aliyun-developers-efficiency@list.alibaba-inc.com
 License: Apache
 Description: =============================================================
         aliyun-python-sdk-eventbridge
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyun_python_sdk_eventbridge.egg-info/SOURCES.txt` & `aliyun-python-sdk-eventbridge-1.0.6/aliyun_python_sdk_eventbridge.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateApiDestinationRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateApiDestinationRequest.py`

 * *Files 14% similar despite different names*

```diff
@@ -42,12 +42,7 @@
 	def set_HttpApiParameters(self, HttpApiParameters):  # Struct
 		self.add_query_param("HttpApiParameters", json.dumps(HttpApiParameters))
 	def get_ApiDestinationName(self): # String
 		return self.get_query_params().get('ApiDestinationName')
 
 	def set_ApiDestinationName(self, ApiDestinationName):  # String
 		self.add_query_param('ApiDestinationName', ApiDestinationName)
-	def get_InvocationRateLimitPerSecond(self): # Long
-		return self.get_query_params().get('InvocationRateLimitPerSecond')
-
-	def set_InvocationRateLimitPerSecond(self, InvocationRateLimitPerSecond):  # Long
-		self.add_query_param('InvocationRateLimitPerSecond', InvocationRateLimitPerSecond)
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateConnectionRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateConnectionRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateEventBusRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateEventBusRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateEventSourceRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateEventSourceRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateEventStreamingRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateEventStreamingRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateRuleRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateRuleRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateServiceLinkedRoleForProductRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateServiceLinkedRoleForProductRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/CreateTargetsRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/CreateTargetsRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteApiDestinationRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteApiDestinationRequest.py`

 * *Files 10% similar despite different names*

```diff
@@ -21,17 +21,12 @@
 
 class DeleteApiDestinationRequest(RpcRequest):
 
 	def __init__(self):
 		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'DeleteApiDestination')
 		self.set_method('POST')
 
-	def get_ClientToken(self): # String
-		return self.get_query_params().get('ClientToken')
-
-	def set_ClientToken(self, ClientToken):  # String
-		self.add_query_param('ClientToken', ClientToken)
 	def get_ApiDestinationName(self): # String
 		return self.get_query_params().get('ApiDestinationName')
 
 	def set_ApiDestinationName(self, ApiDestinationName):  # String
 		self.add_query_param('ApiDestinationName', ApiDestinationName)
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteConnectionRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteConnectionRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteEventBusRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteEventBusRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteEventSourceRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteEventSourceRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteEventStreamingRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteEventStreamingRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteRuleRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteRuleRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DeleteTargetsRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DeleteTargetsRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/DisableRuleRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/DisableRuleRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/EnableRuleRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/EnableRuleRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetApiDestinationRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetApiDestinationRequest.py`

 * *Files 14% similar despite different names*

```diff
@@ -21,17 +21,12 @@
 
 class GetApiDestinationRequest(RpcRequest):
 
 	def __init__(self):
 		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'GetApiDestination')
 		self.set_method('POST')
 
-	def get_ClientToken(self): # String
-		return self.get_query_params().get('ClientToken')
-
-	def set_ClientToken(self, ClientToken):  # String
-		self.add_query_param('ClientToken', ClientToken)
 	def get_ApiDestinationName(self): # String
 		return self.get_query_params().get('ApiDestinationName')
 
 	def set_ApiDestinationName(self, ApiDestinationName):  # String
 		self.add_query_param('ApiDestinationName', ApiDestinationName)
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetConnectionRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetConnectionRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetEventBusRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetEventBusRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetEventStreamingRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetEventStreamingRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/GetRuleRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/GetRuleRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListAliyunOfficialEventSourcesRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListAliyunOfficialEventSourcesRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListApiDestinationsRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListEventStreamingsRequest.py`

 * *Files 17% similar despite different names*

```diff
@@ -15,38 +15,28 @@
 # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 # KIND, either express or implied.  See the License for the
 # specific language governing permissions and limitations
 # under the License.
 
 from aliyunsdkcore.request import RpcRequest
 
-class ListApiDestinationsRequest(RpcRequest):
+class ListEventStreamingsRequest(RpcRequest):
 
 	def __init__(self):
-		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'ListApiDestinations')
+		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'ListEventStreamings')
 		self.set_method('POST')
 
-	def get_ClientToken(self): # String
-		return self.get_query_params().get('ClientToken')
-
-	def set_ClientToken(self, ClientToken):  # String
-		self.add_query_param('ClientToken', ClientToken)
-	def get_Description(self): # String
-		return self.get_query_params().get('Description')
-
-	def set_Description(self, Description):  # String
-		self.add_query_param('Description', Description)
 	def get_NextToken(self): # String
-		return self.get_query_params().get('NextToken')
+		return self.get_body_params().get('NextToken')
 
 	def set_NextToken(self, NextToken):  # String
-		self.add_query_param('NextToken', NextToken)
-	def get_MaxResults(self): # Long
-		return self.get_query_params().get('MaxResults')
-
-	def set_MaxResults(self, MaxResults):  # Long
-		self.add_query_param('MaxResults', MaxResults)
-	def get_ApiDestinationNamePrefix(self): # String
-		return self.get_query_params().get('ApiDestinationNamePrefix')
+		self.add_body_params('NextToken', NextToken)
+	def get_Limit(self): # Long
+		return self.get_body_params().get('Limit')
+
+	def set_Limit(self, Limit):  # Long
+		self.add_body_params('Limit', Limit)
+	def get_NamePrefix(self): # String
+		return self.get_body_params().get('NamePrefix')
 
-	def set_ApiDestinationNamePrefix(self, ApiDestinationNamePrefix):  # String
-		self.add_query_param('ApiDestinationNamePrefix', ApiDestinationNamePrefix)
+	def set_NamePrefix(self, NamePrefix):  # String
+		self.add_body_params('NamePrefix', NamePrefix)
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListConnectionsRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListConnectionsRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListEventBusesRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListEventBusesRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListEventStreamingsRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListRulesRequest.py`

 * *Files 18% similar despite different names*

```diff
@@ -15,28 +15,33 @@
 # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 # KIND, either express or implied.  See the License for the
 # specific language governing permissions and limitations
 # under the License.
 
 from aliyunsdkcore.request import RpcRequest
 
-class ListEventStreamingsRequest(RpcRequest):
+class ListRulesRequest(RpcRequest):
 
 	def __init__(self):
-		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'ListEventStreamings')
+		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'ListRules')
 		self.set_method('POST')
 
+	def get_RuleNamePrefix(self): # String
+		return self.get_query_params().get('RuleNamePrefix')
+
+	def set_RuleNamePrefix(self, RuleNamePrefix):  # String
+		self.add_query_param('RuleNamePrefix', RuleNamePrefix)
+	def get_EventBusName(self): # String
+		return self.get_query_params().get('EventBusName')
+
+	def set_EventBusName(self, EventBusName):  # String
+		self.add_query_param('EventBusName', EventBusName)
 	def get_NextToken(self): # String
-		return self.get_body_params().get('NextToken')
+		return self.get_query_params().get('NextToken')
 
 	def set_NextToken(self, NextToken):  # String
-		self.add_body_params('NextToken', NextToken)
-	def get_Limit(self): # Long
-		return self.get_body_params().get('Limit')
-
-	def set_Limit(self, Limit):  # Long
-		self.add_body_params('Limit', Limit)
-	def get_NamePrefix(self): # String
-		return self.get_body_params().get('NamePrefix')
+		self.add_query_param('NextToken', NextToken)
+	def get_Limit(self): # Integer
+		return self.get_query_params().get('Limit')
 
-	def set_NamePrefix(self, NamePrefix):  # String
-		self.add_body_params('NamePrefix', NamePrefix)
+	def set_Limit(self, Limit):  # Integer
+		self.add_query_param('Limit', Limit)
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListRulesRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/PutTargetsRequest.py`

 * *Files 21% similar despite different names*

```diff
@@ -14,34 +14,30 @@
 # software distributed under the License is distributed on an
 # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 # KIND, either express or implied.  See the License for the
 # specific language governing permissions and limitations
 # under the License.
 
 from aliyunsdkcore.request import RpcRequest
+import json
 
-class ListRulesRequest(RpcRequest):
+class PutTargetsRequest(RpcRequest):
 
 	def __init__(self):
-		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'ListRules')
+		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'PutTargets')
 		self.set_method('POST')
 
-	def get_RuleNamePrefix(self): # String
-		return self.get_query_params().get('RuleNamePrefix')
+	def get_RuleName(self): # String
+		return self.get_query_params().get('RuleName')
 
-	def set_RuleNamePrefix(self, RuleNamePrefix):  # String
-		self.add_query_param('RuleNamePrefix', RuleNamePrefix)
+	def set_RuleName(self, RuleName):  # String
+		self.add_query_param('RuleName', RuleName)
 	def get_EventBusName(self): # String
 		return self.get_query_params().get('EventBusName')
 
 	def set_EventBusName(self, EventBusName):  # String
 		self.add_query_param('EventBusName', EventBusName)
-	def get_NextToken(self): # String
-		return self.get_query_params().get('NextToken')
+	def get_Targets(self): # Array
+		return self.get_query_params().get('Targets')
 
-	def set_NextToken(self, NextToken):  # String
-		self.add_query_param('NextToken', NextToken)
-	def get_Limit(self): # Integer
-		return self.get_query_params().get('Limit')
-
-	def set_Limit(self, Limit):  # Integer
-		self.add_query_param('Limit', Limit)
+	def set_Targets(self, Targets):  # Array
+		self.add_query_param("Targets", json.dumps(Targets))
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/ListUserDefinedEventSourcesRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/ListUserDefinedEventSourcesRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/PauseEventStreamingRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/PauseEventStreamingRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/PutTargetsRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateEventStreamingRequest.py`

 * *Files 19% similar despite different names*

```diff
@@ -16,28 +16,43 @@
 # KIND, either express or implied.  See the License for the
 # specific language governing permissions and limitations
 # under the License.
 
 from aliyunsdkcore.request import RpcRequest
 import json
 
-class PutTargetsRequest(RpcRequest):
+class UpdateEventStreamingRequest(RpcRequest):
 
 	def __init__(self):
-		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'PutTargets')
+		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'UpdateEventStreaming')
 		self.set_method('POST')
 
-	def get_RuleName(self): # String
-		return self.get_query_params().get('RuleName')
+	def get_Sink(self): # Struct
+		return self.get_body_params().get('Sink')
 
-	def set_RuleName(self, RuleName):  # String
-		self.add_query_param('RuleName', RuleName)
-	def get_EventBusName(self): # String
-		return self.get_query_params().get('EventBusName')
-
-	def set_EventBusName(self, EventBusName):  # String
-		self.add_query_param('EventBusName', EventBusName)
-	def get_Targets(self): # Array
-		return self.get_query_params().get('Targets')
+	def set_Sink(self, Sink):  # Struct
+		self.add_body_params("Sink", json.dumps(Sink))
+	def get_Description(self): # String
+		return self.get_body_params().get('Description')
 
-	def set_Targets(self, Targets):  # Array
-		self.add_query_param("Targets", json.dumps(Targets))
+	def set_Description(self, Description):  # String
+		self.add_body_params('Description', Description)
+	def get_FilterPattern(self): # String
+		return self.get_body_params().get('FilterPattern')
+
+	def set_FilterPattern(self, FilterPattern):  # String
+		self.add_body_params('FilterPattern', FilterPattern)
+	def get_Source(self): # Struct
+		return self.get_body_params().get('Source')
+
+	def set_Source(self, Source):  # Struct
+		self.add_body_params("Source", json.dumps(Source))
+	def get_RunOptions(self): # Struct
+		return self.get_body_params().get('RunOptions')
+
+	def set_RunOptions(self, RunOptions):  # Struct
+		self.add_body_params("RunOptions", json.dumps(RunOptions))
+	def get_EventStreamingName(self): # String
+		return self.get_body_params().get('EventStreamingName')
+
+	def set_EventStreamingName(self, EventStreamingName):  # String
+		self.add_body_params('EventStreamingName', EventStreamingName)
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/QueryEventRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/QueryEventRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/QueryEventTracesRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/QueryEventTracesRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/QueryTracedEventByEventIdRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/QueryTracedEventByEventIdRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/QueryTracedEventsRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/QueryTracedEventsRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/StartEventStreamingRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/StartEventStreamingRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateApiDestinationRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateRuleRequest.py`

 * *Files 22% similar despite different names*

```diff
@@ -14,40 +14,39 @@
 # software distributed under the License is distributed on an
 # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 # KIND, either express or implied.  See the License for the
 # specific language governing permissions and limitations
 # under the License.
 
 from aliyunsdkcore.request import RpcRequest
-import json
 
-class UpdateApiDestinationRequest(RpcRequest):
+class UpdateRuleRequest(RpcRequest):
 
 	def __init__(self):
-		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'UpdateApiDestination')
+		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'UpdateRule')
 		self.set_method('POST')
 
-	def get_ClientToken(self): # String
-		return self.get_query_params().get('ClientToken')
-
-	def set_ClientToken(self, ClientToken):  # String
-		self.add_query_param('ClientToken', ClientToken)
 	def get_Description(self): # String
 		return self.get_query_params().get('Description')
 
 	def set_Description(self, Description):  # String
 		self.add_query_param('Description', Description)
-	def get_ApiDestinationName(self): # String
-		return self.get_query_params().get('ApiDestinationName')
+	def get_RuleName(self): # String
+		return self.get_query_params().get('RuleName')
 
-	def set_ApiDestinationName(self, ApiDestinationName):  # String
-		self.add_query_param('ApiDestinationName', ApiDestinationName)
-	def get_ConnectionName(self): # String
-		return self.get_query_params().get('ConnectionName')
-
-	def set_ConnectionName(self, ConnectionName):  # String
-		self.add_query_param('ConnectionName', ConnectionName)
-	def get_HttpApiParameters(self): # Struct
-		return self.get_query_params().get('HttpApiParameters')
+	def set_RuleName(self, RuleName):  # String
+		self.add_query_param('RuleName', RuleName)
+	def get_EventBusName(self): # String
+		return self.get_query_params().get('EventBusName')
+
+	def set_EventBusName(self, EventBusName):  # String
+		self.add_query_param('EventBusName', EventBusName)
+	def get_FilterPattern(self): # String
+		return self.get_query_params().get('FilterPattern')
+
+	def set_FilterPattern(self, FilterPattern):  # String
+		self.add_query_param('FilterPattern', FilterPattern)
+	def get_Status(self): # String
+		return self.get_query_params().get('Status')
 
-	def set_HttpApiParameters(self, HttpApiParameters):  # Struct
-		self.add_query_param("HttpApiParameters", json.dumps(HttpApiParameters))
+	def set_Status(self, Status):  # String
+		self.add_query_param('Status', Status)
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateConnectionRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateConnectionRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateEventBusRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateEventBusRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateEventSourceRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateEventSourceRequest.py`

 * *Files identical despite different names*

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/aliyunsdkeventbridge/request/v20200401/UpdateEventStreamingRequest.py` & `aliyun-python-sdk-eventbridge-1.0.6/aliyunsdkeventbridge/request/v20200401/UpdateApiDestinationRequest.py`

 * *Files 20% similar despite different names*

```diff
@@ -16,43 +16,33 @@
 # KIND, either express or implied.  See the License for the
 # specific language governing permissions and limitations
 # under the License.
 
 from aliyunsdkcore.request import RpcRequest
 import json
 
-class UpdateEventStreamingRequest(RpcRequest):
+class UpdateApiDestinationRequest(RpcRequest):
 
 	def __init__(self):
-		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'UpdateEventStreaming')
+		RpcRequest.__init__(self, 'eventbridge', '2020-04-01', 'UpdateApiDestination')
 		self.set_method('POST')
 
-	def get_Sink(self): # Struct
-		return self.get_body_params().get('Sink')
-
-	def set_Sink(self, Sink):  # Struct
-		self.add_body_params("Sink", json.dumps(Sink))
 	def get_Description(self): # String
-		return self.get_body_params().get('Description')
+		return self.get_query_params().get('Description')
 
 	def set_Description(self, Description):  # String
-		self.add_body_params('Description', Description)
-	def get_FilterPattern(self): # String
-		return self.get_body_params().get('FilterPattern')
-
-	def set_FilterPattern(self, FilterPattern):  # String
-		self.add_body_params('FilterPattern', FilterPattern)
-	def get_Source(self): # Struct
-		return self.get_body_params().get('Source')
-
-	def set_Source(self, Source):  # Struct
-		self.add_body_params("Source", json.dumps(Source))
-	def get_RunOptions(self): # Struct
-		return self.get_body_params().get('RunOptions')
-
-	def set_RunOptions(self, RunOptions):  # Struct
-		self.add_body_params("RunOptions", json.dumps(RunOptions))
-	def get_EventStreamingName(self): # String
-		return self.get_body_params().get('EventStreamingName')
+		self.add_query_param('Description', Description)
+	def get_ApiDestinationName(self): # String
+		return self.get_query_params().get('ApiDestinationName')
+
+	def set_ApiDestinationName(self, ApiDestinationName):  # String
+		self.add_query_param('ApiDestinationName', ApiDestinationName)
+	def get_ConnectionName(self): # String
+		return self.get_query_params().get('ConnectionName')
+
+	def set_ConnectionName(self, ConnectionName):  # String
+		self.add_query_param('ConnectionName', ConnectionName)
+	def get_HttpApiParameters(self): # Struct
+		return self.get_query_params().get('HttpApiParameters')
 
-	def set_EventStreamingName(self, EventStreamingName):  # String
-		self.add_body_params('EventStreamingName', EventStreamingName)
+	def set_HttpApiParameters(self, HttpApiParameters):  # Struct
+		self.add_query_param("HttpApiParameters", json.dumps(HttpApiParameters))
```

### Comparing `aliyun-python-sdk-eventbridge-1.0.5/setup.py` & `aliyun-python-sdk-eventbridge-1.0.6/setup.py`

 * *Files identical despite different names*

