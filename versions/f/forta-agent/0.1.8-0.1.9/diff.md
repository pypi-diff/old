# Comparing `tmp/forta_agent-0.1.8.tar.gz` & `tmp/forta_agent-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "forta_agent-0.1.8.tar", last modified: Thu Jan 12 04:07:33 2023, max compression
+gzip compressed data, was "forta_agent-0.1.9.tar", last modified: Wed Jan 18 13:03:17 2023, max compression
```

## Comparing `forta_agent-0.1.8.tar` & `forta_agent-0.1.9.tar`

### file list

```diff
@@ -1,31 +1,35 @@
-drwxr-xr-x   0 haseebrabbani   (501) staff       (20)        0 2023-01-12 04:07:33.273868 forta_agent-0.1.8/
--rw-r--r--   0 haseebrabbani   (501) staff       (20)     1073 2021-09-03 16:10:14.000000 forta_agent-0.1.8/LICENSE
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      585 2023-01-12 04:07:33.273971 forta_agent-0.1.8/PKG-INFO
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      110 2021-09-03 19:42:46.000000 forta_agent-0.1.8/README.md
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      103 2021-09-03 16:10:14.000000 forta_agent-0.1.8/pyproject.toml
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      646 2023-01-12 04:07:33.274490 forta_agent-0.1.8/setup.cfg
--rw-r--r--   0 haseebrabbani   (501) staff       (20)       69 2022-11-29 16:58:32.000000 forta_agent-0.1.8/setup.py
-drwxr-xr-x   0 haseebrabbani   (501) staff       (20)        0 2023-01-12 04:07:33.266517 forta_agent-0.1.8/src/
-drwxr-xr-x   0 haseebrabbani   (501) staff       (20)        0 2023-01-12 04:07:33.272600 forta_agent-0.1.8/src/forta_agent/
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      726 2023-01-05 14:10:22.000000 forta_agent-0.1.8/src/forta_agent/__init__.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)     3515 2023-01-05 14:10:22.000000 forta_agent-0.1.8/src/forta_agent/alert.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      825 2023-01-05 14:10:22.000000 forta_agent-0.1.8/src/forta_agent/alert_event.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      896 2023-01-05 14:10:22.000000 forta_agent-0.1.8/src/forta_agent/alert_test.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)     1296 2021-09-03 19:20:26.000000 forta_agent-0.1.8/src/forta_agent/block.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      758 2021-11-02 17:23:16.000000 forta_agent-0.1.8/src/forta_agent/block_event.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)       81 2021-09-03 16:10:14.000000 forta_agent-0.1.8/src/forta_agent/event_type.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)     1442 2023-01-05 14:10:22.000000 forta_agent-0.1.8/src/forta_agent/finding.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)     3927 2023-01-05 14:10:22.000000 forta_agent-0.1.8/src/forta_agent/forta_graphql.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      772 2023-01-05 14:10:22.000000 forta_agent-0.1.8/src/forta_agent/label.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      223 2022-03-23 10:25:46.000000 forta_agent-0.1.8/src/forta_agent/network.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)     2142 2021-11-01 12:51:25.000000 forta_agent-0.1.8/src/forta_agent/receipt.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)     1531 2021-10-01 23:15:36.000000 forta_agent-0.1.8/src/forta_agent/trace.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      550 2021-09-03 23:05:46.000000 forta_agent-0.1.8/src/forta_agent/transaction.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)     4768 2023-01-12 03:58:13.000000 forta_agent-0.1.8/src/forta_agent/transaction_event.py
--rw-r--r--   0 haseebrabbani   (501) staff       (20)     8315 2022-11-24 11:09:38.000000 forta_agent-0.1.8/src/forta_agent/utils.py
-drwxr-xr-x   0 haseebrabbani   (501) staff       (20)        0 2023-01-12 04:07:33.273709 forta_agent-0.1.8/src/forta_agent.egg-info/
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      585 2023-01-12 04:07:33.000000 forta_agent-0.1.8/src/forta_agent.egg-info/PKG-INFO
--rw-r--r--   0 haseebrabbani   (501) staff       (20)      702 2023-01-12 04:07:33.000000 forta_agent-0.1.8/src/forta_agent.egg-info/SOURCES.txt
--rw-r--r--   0 haseebrabbani   (501) staff       (20)        1 2023-01-12 04:07:33.000000 forta_agent-0.1.8/src/forta_agent.egg-info/dependency_links.txt
--rw-r--r--   0 haseebrabbani   (501) staff       (20)       35 2023-01-12 04:07:33.000000 forta_agent-0.1.8/src/forta_agent.egg-info/requires.txt
--rw-r--r--   0 haseebrabbani   (501) staff       (20)       12 2023-01-12 04:07:33.000000 forta_agent-0.1.8/src/forta_agent.egg-info/top_level.txt
+drwxr-xr-x   0 haseebrabbani   (501) staff       (20)        0 2023-01-18 13:03:17.080227 forta_agent-0.1.9/
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     1073 2021-09-03 16:10:14.000000 forta_agent-0.1.9/LICENSE
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      585 2023-01-18 13:03:17.080328 forta_agent-0.1.9/PKG-INFO
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      110 2021-09-03 19:42:46.000000 forta_agent-0.1.9/README.md
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      103 2021-09-03 16:10:14.000000 forta_agent-0.1.9/pyproject.toml
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)       34 2022-11-24 11:09:38.000000 forta_agent-0.1.9/pytest.ini
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)       63 2023-01-18 12:46:13.000000 forta_agent-0.1.9/requirements.txt
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      646 2023-01-18 13:03:17.080868 forta_agent-0.1.9/setup.cfg
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)       69 2022-11-29 16:58:32.000000 forta_agent-0.1.9/setup.py
+drwxr-xr-x   0 haseebrabbani   (501) staff       (20)        0 2023-01-18 13:03:17.074097 forta_agent-0.1.9/src/
+drwxr-xr-x   0 haseebrabbani   (501) staff       (20)        0 2023-01-18 13:03:17.079221 forta_agent-0.1.9/src/forta_agent/
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      752 2023-01-18 12:46:13.000000 forta_agent-0.1.9/src/forta_agent/__init__.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     3515 2023-01-05 14:10:22.000000 forta_agent-0.1.9/src/forta_agent/alert.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      825 2023-01-05 14:10:22.000000 forta_agent-0.1.9/src/forta_agent/alert_event.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      896 2023-01-05 14:10:22.000000 forta_agent-0.1.9/src/forta_agent/alert_test.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     1296 2021-09-03 19:20:26.000000 forta_agent-0.1.9/src/forta_agent/block.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      758 2021-11-02 17:23:16.000000 forta_agent-0.1.9/src/forta_agent/block_event.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)       81 2021-09-03 16:10:14.000000 forta_agent-0.1.9/src/forta_agent/event_type.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     1442 2023-01-05 14:10:22.000000 forta_agent-0.1.9/src/forta_agent/finding.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     3927 2023-01-05 14:10:22.000000 forta_agent-0.1.9/src/forta_agent/forta_graphql.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     4068 2023-01-18 12:46:13.000000 forta_agent-0.1.9/src/forta_agent/jwt.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     1353 2023-01-18 12:46:13.000000 forta_agent-0.1.9/src/forta_agent/jwt_test.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      820 2023-01-16 15:27:47.000000 forta_agent-0.1.9/src/forta_agent/label.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      223 2022-03-23 10:25:46.000000 forta_agent-0.1.9/src/forta_agent/network.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     2142 2021-11-01 12:51:25.000000 forta_agent-0.1.9/src/forta_agent/receipt.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     1531 2021-10-01 23:15:36.000000 forta_agent-0.1.9/src/forta_agent/trace.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      550 2021-09-03 23:05:46.000000 forta_agent-0.1.9/src/forta_agent/transaction.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     4768 2023-01-12 03:58:13.000000 forta_agent-0.1.9/src/forta_agent/transaction_event.py
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)     4637 2023-01-18 12:46:13.000000 forta_agent-0.1.9/src/forta_agent/utils.py
+drwxr-xr-x   0 haseebrabbani   (501) staff       (20)        0 2023-01-18 13:03:17.080066 forta_agent-0.1.9/src/forta_agent.egg-info/
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      585 2023-01-18 13:03:17.000000 forta_agent-0.1.9/src/forta_agent.egg-info/PKG-INFO
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)      781 2023-01-18 13:03:17.000000 forta_agent-0.1.9/src/forta_agent.egg-info/SOURCES.txt
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)        1 2023-01-18 13:03:17.000000 forta_agent-0.1.9/src/forta_agent.egg-info/dependency_links.txt
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)       35 2023-01-18 13:03:17.000000 forta_agent-0.1.9/src/forta_agent.egg-info/requires.txt
+-rw-r--r--   0 haseebrabbani   (501) staff       (20)       12 2023-01-18 13:03:17.000000 forta_agent-0.1.9/src/forta_agent.egg-info/top_level.txt
```

### Comparing `forta_agent-0.1.8/LICENSE` & `forta_agent-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/PKG-INFO` & `forta_agent-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: forta_agent
-Version: 0.1.8
+Version: 0.1.9
 Summary: Forta Agent Python SDK
 Home-page: https://forta.org/
 Project-URL: Source, https://github.com/forta-network/forta-agent-sdk
 Project-URL: Documentation, https://docs.forta.network/
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `forta_agent-0.1.8/setup.cfg` & `forta_agent-0.1.9/setup.cfg`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = forta_agent
-version = 0.1.8
+version = 0.1.9
 description = Forta Agent Python SDK
 url = https://forta.org/
 project_urls = 
 	Source = https://github.com/forta-network/forta-agent-sdk
 	Documentation =  https://docs.forta.network/
 long_description = file: README.md
 long_description_content_type = text/markdown
```

### Comparing `forta_agent-0.1.8/src/forta_agent/__init__.py` & `forta_agent-0.1.9/src/forta_agent/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -5,11 +5,12 @@
 from .alert_event import AlertEvent
 from .block import Block
 from .transaction import Transaction
 from .receipt import Receipt, Log
 from .trace import Trace, TraceAction, TraceResult
 from .event_type import EventType
 from .network import Network
-from .utils import get_json_rpc_url, create_block_event, create_transaction_event, create_alert_event, get_web3_provider, keccak256, get_transaction_receipt, get_alerts, fetch_jwt, decode_jwt, verify_jwt
+from .utils import get_json_rpc_url, create_block_event, create_transaction_event, create_alert_event, get_web3_provider, keccak256, get_transaction_receipt, get_alerts
+from .jwt import fetch_jwt, decode_jwt, verify_jwt, MOCK_JWT
 from web3 import Web3
 
 web3Provider = Web3(Web3.HTTPProvider(get_json_rpc_url()))
```

### Comparing `forta_agent-0.1.8/src/forta_agent/alert.py` & `forta_agent-0.1.9/src/forta_agent/alert.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/alert_event.py` & `forta_agent-0.1.9/src/forta_agent/alert_event.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/alert_test.py` & `forta_agent-0.1.9/src/forta_agent/alert_test.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/block.py` & `forta_agent-0.1.9/src/forta_agent/block.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/block_event.py` & `forta_agent-0.1.9/src/forta_agent/block_event.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/finding.py` & `forta_agent-0.1.9/src/forta_agent/finding.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/forta_graphql.py` & `forta_agent-0.1.9/src/forta_agent/forta_graphql.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/label.py` & `forta_agent-0.1.9/src/forta_agent/label.py`

 * *Files 22% similar despite different names*

```diff
@@ -15,13 +15,14 @@
         assert_enum_value_in_dict(dict, 'entity_type', EntityType)
         assert_non_empty_string_in_dict(dict, 'entity')
         assert_non_empty_string_in_dict(dict, 'label')
         self.entity = dict['entity']
         self.confidence = dict['confidence']
         self.entity_type = dict['entity_type']
         self.label = dict['label']
+        self.remove = dict.get('remove', False)
 
     def toDict(self):
         d = dict(self.__dict__, **{
             'entityType': self.entity_type,
         })
         return {k: v for k, v in d.items() if v is not None}
```

### Comparing `forta_agent-0.1.8/src/forta_agent/receipt.py` & `forta_agent-0.1.9/src/forta_agent/receipt.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/trace.py` & `forta_agent-0.1.9/src/forta_agent/trace.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/transaction.py` & `forta_agent-0.1.9/src/forta_agent/transaction.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent/transaction_event.py` & `forta_agent-0.1.9/src/forta_agent/transaction_event.py`

 * *Files identical despite different names*

### Comparing `forta_agent-0.1.8/src/forta_agent.egg-info/PKG-INFO` & `forta_agent-0.1.9/src/forta_agent.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: forta-agent
-Version: 0.1.8
+Version: 0.1.9
 Summary: Forta Agent Python SDK
 Home-page: https://forta.org/
 Project-URL: Source, https://github.com/forta-network/forta-agent-sdk
 Project-URL: Documentation, https://docs.forta.network/
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
```

### Comparing `forta_agent-0.1.8/src/forta_agent.egg-info/SOURCES.txt` & `forta_agent-0.1.9/src/forta_agent.egg-info/SOURCES.txt`

 * *Files 12% similar despite different names*

```diff
@@ -1,21 +1,25 @@
 LICENSE
 README.md
 pyproject.toml
+pytest.ini
+requirements.txt
 setup.cfg
 setup.py
 src/forta_agent/__init__.py
 src/forta_agent/alert.py
 src/forta_agent/alert_event.py
 src/forta_agent/alert_test.py
 src/forta_agent/block.py
 src/forta_agent/block_event.py
 src/forta_agent/event_type.py
 src/forta_agent/finding.py
 src/forta_agent/forta_graphql.py
+src/forta_agent/jwt.py
+src/forta_agent/jwt_test.py
 src/forta_agent/label.py
 src/forta_agent/network.py
 src/forta_agent/receipt.py
 src/forta_agent/trace.py
 src/forta_agent/transaction.py
 src/forta_agent/transaction_event.py
 src/forta_agent/utils.py
```

