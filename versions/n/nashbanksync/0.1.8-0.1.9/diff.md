# Comparing `tmp/nashbanksync-0.1.8.tar.gz` & `tmp/nashbanksync-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "nashbanksync-0.1.8.tar", last modified: Wed Jan 18 08:30:33 2023, max compression
+gzip compressed data, was "dist\nashbanksync-0.1.9.tar", last modified: Wed Jan 18 20:04:09 2023, max compression
```

## Comparing `nashbanksync-0.1.8.tar` & `nashbanksync-0.1.9.tar`

### file list

```diff
@@ -1,51 +1,51 @@
-drwxrwxrwx   0        0        0        0 2023-01-18 08:30:33.045491 nashbanksync-0.1.8/
--rw-rw-rw-   0        0        0    35821 2022-01-28 09:49:37.000000 nashbanksync-0.1.8/LICENSE
--rw-rw-rw-   0        0        0      910 2023-01-18 08:30:33.045491 nashbanksync-0.1.8/PKG-INFO
--rw-rw-rw-   0        0        0      314 2022-01-28 09:49:37.000000 nashbanksync-0.1.8/README.md
-drwxrwxrwx   0        0        0        0 2023-01-18 08:30:32.998152 nashbanksync-0.1.8/bank_sync/
-drwxrwxrwx   0        0        0        0 2023-01-18 08:30:32.998152 nashbanksync-0.1.8/bank_sync/APIs/
--rw-rw-rw-   0        0        0       13 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/APIs/__init__.py
--rw-rw-rw-   0        0        0     7516 2023-01-16 12:29:39.000000 nashbanksync-0.1.8/bank_sync/APIs/api_format.py
-drwxrwxrwx   0        0        0        0 2023-01-18 08:30:32.998152 nashbanksync-0.1.8/bank_sync/APIs/utils/
--rw-rw-rw-   0        0        0       14 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/APIs/utils/__init__.py
--rw-rw-rw-   0        0        0     1023 2023-01-09 06:43:57.000000 nashbanksync-0.1.8/bank_sync/APIs/utils/generate_code.py
-drwxrwxrwx   0        0        0        0 2023-01-18 08:30:32.998152 nashbanksync-0.1.8/bank_sync/Nash/
--rw-rw-rw-   0        0        0       13 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/Nash/__init__.py
--rw-rw-rw-   0        0        0     1456 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/Nash/nash.py
-drwxrwxrwx   0        0        0        0 2023-01-18 08:30:33.013788 nashbanksync-0.1.8/bank_sync/Resources/
--rw-rw-rw-   0        0        0        0 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/Resources/__init__.py
--rw-rw-rw-   0        0        0    25461 2023-01-13 10:01:49.000000 nashbanksync-0.1.8/bank_sync/Resources/accounts.py
--rw-rw-rw-   0        0        0    13110 2023-01-16 10:50:05.000000 nashbanksync-0.1.8/bank_sync/Resources/banks.py
--rw-rw-rw-   0        0        0    13483 2023-01-09 06:43:57.000000 nashbanksync-0.1.8/bank_sync/Resources/operations.py
--rw-rw-rw-   0        0        0    45030 2023-01-12 14:03:40.000000 nashbanksync-0.1.8/bank_sync/Resources/payments.py
--rw-rw-rw-   0        0        0    39264 2023-01-18 08:27:00.000000 nashbanksync-0.1.8/bank_sync/Resources/resource.py
--rw-rw-rw-   0        0        0        0 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/__init__.py
--rw-rw-rw-   0        0        0      306 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/admin.py
--rw-rw-rw-   0        0        0      155 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/apps.py
-drwxrwxrwx   0        0        0        0 2023-01-18 08:30:33.023847 nashbanksync-0.1.8/bank_sync/middlewares/
--rw-rw-rw-   0        0        0        0 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/middlewares/__init__.py
--rw-rw-rw-   0        0        0     2643 2022-12-09 06:49:18.000000 nashbanksync-0.1.8/bank_sync/middlewares/logs.py
-drwxrwxrwx   0        0        0        0 2023-01-18 08:30:33.029854 nashbanksync-0.1.8/bank_sync/migrations/
--rw-rw-rw-   0        0        0     1017 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/migrations/0001_initial.py
--rw-rw-rw-   0        0        0      415 2022-07-14 12:15:29.000000 nashbanksync-0.1.8/bank_sync/migrations/0002_alter_callbacks_reference.py
--rw-rw-rw-   0        0        0      990 2022-11-08 13:16:02.000000 nashbanksync-0.1.8/bank_sync/migrations/0003_requestlogs.py
--rw-rw-rw-   0        0        0      400 2022-11-08 13:47:51.000000 nashbanksync-0.1.8/bank_sync/migrations/0004_requestlogs_error.py
--rw-rw-rw-   0        0        0      419 2022-11-08 13:50:25.000000 nashbanksync-0.1.8/bank_sync/migrations/0005_alter_requestlogs_error.py
--rw-rw-rw-   0        0        0      470 2022-11-09 07:52:10.000000 nashbanksync-0.1.8/bank_sync/migrations/0006_requestlogs_log_time.py
--rw-rw-rw-   0        0        0      728 2022-11-09 08:32:51.000000 nashbanksync-0.1.8/bank_sync/migrations/0007_responselogs.py
--rw-rw-rw-   0        0        0      425 2022-11-09 08:51:19.000000 nashbanksync-0.1.8/bank_sync/migrations/0008_responselogs_ip.py
--rw-rw-rw-   0        0        0      416 2022-11-09 08:57:45.000000 nashbanksync-0.1.8/bank_sync/migrations/0009_responselogs_error.py
--rw-rw-rw-   0        0        0     1560 2022-11-17 11:06:01.000000 nashbanksync-0.1.8/bank_sync/migrations/0010_auto_20221117_1406.py
--rw-rw-rw-   0        0        0      943 2022-11-18 09:28:08.000000 nashbanksync-0.1.8/bank_sync/migrations/0011_ipndata.py
--rw-rw-rw-   0        0        0      414 2022-11-18 11:32:50.000000 nashbanksync-0.1.8/bank_sync/migrations/0012_alter_ipn_account_number.py
--rw-rw-rw-   0        0        0      495 2022-11-18 12:15:10.000000 nashbanksync-0.1.8/bank_sync/migrations/0013_alter_ipndata_ipn.py
--rw-rw-rw-   0        0        0        0 2022-11-18 12:37:16.000000 nashbanksync-0.1.8/bank_sync/migrations/__init__.py
--rw-rw-rw-   0        0        0     4256 2023-01-09 06:43:57.000000 nashbanksync-0.1.8/bank_sync/models.py
--rw-rw-rw-   0        0        0     1010 2023-01-11 11:06:16.000000 nashbanksync-0.1.8/bank_sync/tests.py
-drwxrwxrwx   0        0        0        0 2023-01-18 08:30:33.045491 nashbanksync-0.1.8/nashbanksync.egg-info/
--rw-rw-rw-   0        0        0      910 2023-01-18 08:30:32.000000 nashbanksync-0.1.8/nashbanksync.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0     1337 2023-01-18 08:30:32.000000 nashbanksync-0.1.8/nashbanksync.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-01-18 08:30:32.000000 nashbanksync-0.1.8/nashbanksync.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       10 2023-01-18 08:30:32.000000 nashbanksync-0.1.8/nashbanksync.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-01-18 08:30:33.045491 nashbanksync-0.1.8/setup.cfg
--rw-rw-rw-   0        0        0      769 2023-01-18 08:27:08.000000 nashbanksync-0.1.8/setup.py
+drwxrwxrwx   0        0        0        0 2023-01-18 20:04:09.245108 nashbanksync-0.1.9/
+-rw-rw-rw-   0        0        0    35821 2022-08-31 12:58:39.000000 nashbanksync-0.1.9/LICENSE
+-rw-rw-rw-   0        0        0      871 2023-01-18 20:04:09.244103 nashbanksync-0.1.9/PKG-INFO
+-rw-rw-rw-   0        0        0      314 2022-08-31 12:58:39.000000 nashbanksync-0.1.9/README.md
+drwxrwxrwx   0        0        0        0 2023-01-18 20:04:09.191954 nashbanksync-0.1.9/bank_sync/
+drwxrwxrwx   0        0        0        0 2023-01-18 20:04:09.193954 nashbanksync-0.1.9/bank_sync/APIs/
+-rw-rw-rw-   0        0        0       13 2022-08-31 12:58:40.000000 nashbanksync-0.1.9/bank_sync/APIs/__init__.py
+-rw-rw-rw-   0        0        0     7516 2023-01-16 16:36:50.000000 nashbanksync-0.1.9/bank_sync/APIs/api_format.py
+drwxrwxrwx   0        0        0        0 2023-01-18 20:04:09.197059 nashbanksync-0.1.9/bank_sync/APIs/utils/
+-rw-rw-rw-   0        0        0       14 2022-08-31 12:58:40.000000 nashbanksync-0.1.9/bank_sync/APIs/utils/__init__.py
+-rw-rw-rw-   0        0        0     1023 2023-01-08 19:43:19.000000 nashbanksync-0.1.9/bank_sync/APIs/utils/generate_code.py
+drwxrwxrwx   0        0        0        0 2023-01-18 20:04:09.200058 nashbanksync-0.1.9/bank_sync/Nash/
+-rw-rw-rw-   0        0        0       13 2022-08-31 12:58:40.000000 nashbanksync-0.1.9/bank_sync/Nash/__init__.py
+-rw-rw-rw-   0        0        0     1456 2022-08-31 12:58:40.000000 nashbanksync-0.1.9/bank_sync/Nash/nash.py
+drwxrwxrwx   0        0        0        0 2023-01-18 20:04:09.208772 nashbanksync-0.1.9/bank_sync/Resources/
+-rw-rw-rw-   0        0        0        0 2022-08-31 12:58:40.000000 nashbanksync-0.1.9/bank_sync/Resources/__init__.py
+-rw-rw-rw-   0        0        0    28300 2023-01-18 19:57:42.000000 nashbanksync-0.1.9/bank_sync/Resources/accounts.py
+-rw-rw-rw-   0        0        0    13110 2023-01-16 16:36:50.000000 nashbanksync-0.1.9/bank_sync/Resources/banks.py
+-rw-rw-rw-   0        0        0    13483 2023-01-07 22:05:26.000000 nashbanksync-0.1.9/bank_sync/Resources/operations.py
+-rw-rw-rw-   0        0        0    45030 2023-01-12 18:34:03.000000 nashbanksync-0.1.9/bank_sync/Resources/payments.py
+-rw-rw-rw-   0        0        0    39264 2023-01-18 18:14:57.000000 nashbanksync-0.1.9/bank_sync/Resources/resource.py
+-rw-rw-rw-   0        0        0        0 2022-08-31 12:58:40.000000 nashbanksync-0.1.9/bank_sync/__init__.py
+-rw-rw-rw-   0        0        0      306 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/admin.py
+-rw-rw-rw-   0        0        0      155 2022-08-31 12:58:40.000000 nashbanksync-0.1.9/bank_sync/apps.py
+drwxrwxrwx   0        0        0        0 2023-01-18 20:04:09.211771 nashbanksync-0.1.9/bank_sync/middlewares/
+-rw-rw-rw-   0        0        0        0 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/middlewares/__init__.py
+-rw-rw-rw-   0        0        0     2643 2022-12-08 16:31:16.000000 nashbanksync-0.1.9/bank_sync/middlewares/logs.py
+drwxrwxrwx   0        0        0        0 2023-01-18 20:04:09.231770 nashbanksync-0.1.9/bank_sync/migrations/
+-rw-rw-rw-   0        0        0     1017 2022-08-31 12:58:40.000000 nashbanksync-0.1.9/bank_sync/migrations/0001_initial.py
+-rw-rw-rw-   0        0        0      415 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0002_alter_callbacks_reference.py
+-rw-rw-rw-   0        0        0      990 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0003_requestlogs.py
+-rw-rw-rw-   0        0        0      400 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0004_requestlogs_error.py
+-rw-rw-rw-   0        0        0      419 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0005_alter_requestlogs_error.py
+-rw-rw-rw-   0        0        0      470 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0006_requestlogs_log_time.py
+-rw-rw-rw-   0        0        0      728 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0007_responselogs.py
+-rw-rw-rw-   0        0        0      425 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0008_responselogs_ip.py
+-rw-rw-rw-   0        0        0      416 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0009_responselogs_error.py
+-rw-rw-rw-   0        0        0     1560 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0010_auto_20221117_1406.py
+-rw-rw-rw-   0        0        0      943 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0011_ipndata.py
+-rw-rw-rw-   0        0        0      414 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0012_alter_ipn_account_number.py
+-rw-rw-rw-   0        0        0      495 2022-11-24 16:31:07.000000 nashbanksync-0.1.9/bank_sync/migrations/0013_alter_ipndata_ipn.py
+-rw-rw-rw-   0        0        0        0 2022-08-31 12:58:40.000000 nashbanksync-0.1.9/bank_sync/migrations/__init__.py
+-rw-rw-rw-   0        0        0     4256 2023-01-08 19:40:25.000000 nashbanksync-0.1.9/bank_sync/models.py
+-rw-rw-rw-   0        0        0     1010 2023-01-12 18:34:03.000000 nashbanksync-0.1.9/bank_sync/tests.py
+drwxrwxrwx   0        0        0        0 2023-01-18 20:04:09.241770 nashbanksync-0.1.9/nashbanksync.egg-info/
+-rw-rw-rw-   0        0        0      871 2023-01-18 20:04:09.000000 nashbanksync-0.1.9/nashbanksync.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0     1337 2023-01-18 20:04:09.000000 nashbanksync-0.1.9/nashbanksync.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-01-18 20:04:09.000000 nashbanksync-0.1.9/nashbanksync.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       10 2023-01-18 20:04:09.000000 nashbanksync-0.1.9/nashbanksync.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-01-18 20:04:09.245108 nashbanksync-0.1.9/setup.cfg
+-rw-rw-rw-   0        0        0      769 2023-01-18 20:03:46.000000 nashbanksync-0.1.9/setup.py
```

### Comparing `nashbanksync-0.1.8/LICENSE` & `nashbanksync-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/PKG-INFO` & `nashbanksync-0.1.9/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,16 +1,14 @@
 Metadata-Version: 2.1
 Name: nashbanksync
-Version: 0.1.8
+Version: 0.1.9
 Summary: Python library for connecting to the Nash Banks Framework
 Home-page: https://github.com/NashInc/NashSync.git
 Author: Dansol Obondo
 Author-email: dansol@nashafrica.co
-License: UNKNOWN
-Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 License-File: LICENSE
@@ -25,8 +23,7 @@
     pip install nashbanksync
 ```
 2.	View get started documentation:
 ```bash
     https://nashbanksuite.readme.io/v1.2.0/docs
 ```
 3.	Start Coding
-
```

### Comparing `nashbanksync-0.1.8/bank_sync/APIs/api_format.py` & `nashbanksync-0.1.9/bank_sync/APIs/api_format.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/APIs/utils/generate_code.py` & `nashbanksync-0.1.9/bank_sync/APIs/utils/generate_code.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/Nash/nash.py` & `nashbanksync-0.1.9/bank_sync/Nash/nash.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/Resources/accounts.py` & `nashbanksync-0.1.9/bank_sync/Resources/accounts.py`

 * *Files 12% similar despite different names*

```diff
@@ -13,14 +13,31 @@
 
 
 class Accounts(Resource):
 
     urls = {}
     bank_sync_call_back = {}
 
+    full_statement_transaction_dict = {
+        "currency_code": "",
+        "date": "",
+        "description": "",
+        "transaction_id": "",
+        "reference": "",
+        "value_date": "",
+        "posted_date": "",
+        "service_point": "",
+        "running_cleared_balance": "",
+        "debit_limit": 0,
+        "limit_expiry_date": "",
+        "serial": "",
+        "amount": "",
+        "type": "",
+    }
+
     try:
         bank_sync_call_back = getattr(
             settings, 'BANK_SYNC_CALL_BACK_URLS', bank_sync_call_back)
     except Exception as e:
         pass
 
     def set_bank_id(self, bank_id):
@@ -209,27 +226,30 @@
                     "amount": round(float(payload.get("amount", 0)), 2),
                 })
 
         data.update(payload.get("additional_properties", {}))
 
         return data
 
+    def get_full_statement_transaction_dict(self):
+        return self.full_statement_transaction_dict
+
     def response(self):
 
         data = {}
 
         response_data = super().response()
 
         if super().get_operation() == super().BALANCE:
 
             data.update({
                 "message": "",
                 "code": -111111,
                 "balance": 0,
-                "balance_time":"",
+                "balance_time": "",
                 "account_type": "",
                 "cleared_balance": "",
                 "booked_balance": "",
                 "blocked_balance": "",
                 "arrears_amount": "",
                 "branch_name": "",
                 "branch_code": "",
@@ -241,15 +261,15 @@
 
             if super().get_bank_id() == super().COOP:
 
                 data["message"] = response_data.get("MessageDescription", "")
                 data["code"] = int(response_data.get("MessageCode", -111111))
                 data["balance"] = response_data.get("AvailableBalance", "")
                 data["balance_time"] = response_data.get("MessageDateTime", "")
-                
+
                 data["account_type"] = response_data.get("ProductName", "")
                 data["cleared_balance"] = response_data.get(
                     "ClearedBalance", "")
                 data["booked_balance"] = response_data.get("BookedBalance", "")
                 data["blocked_balance"] = response_data.get(
                     "BlockedBalance", "")
                 data["arrears_amount"] = response_data.get("ArrearsAmount", "")
@@ -280,14 +300,15 @@
             elif super().get_bank_id() == super().UBA:
 
                 data["message"] = ''
                 data["code"] = int(float(response_data.get("sendTransactionResponse", {}).get(
                     "return", {}).get("C24TRANRES", {}).get("ACTION_CODE", "-111111")))
                 data["balance"] = float(response_data.get("sendTransactionResponse", {}).get(
                     "return", {}).get("C24TRANRES", {}).get("AVAILABLE_BALANCE", -1))
+                data["balance_time"] = datetime.strptime(f'{response_data.get("sendTransactionResponse", {}).get("return", {}).get("C24TRANRES", {}).get("TRAN_DATE_TIME",)}', '%Y%d%m%H%M%S').strftime('%Y-%m-%d %H:%M:%S')
                 if data["code"]:
                     data["message"] = "Transaction Failed"
                 else:
                     data["message"] = "Success"
 
         elif super().get_operation() == super().MINI_STATEMENT or super().get_operation() == super().ACCOUNT_TRANSACTIONS:
 
@@ -372,45 +393,58 @@
                     data["message"] = response_data.get(
                         "content", {}).get("account_description", "")
                     data["code"] = 0
                     data["account_name"] = response_data.get(
                         "content", {}).get("customer_name", "")
 
         elif super().get_operation() == super().FULL_STATEMENT:
+            transaction = self.get_full_statement_transaction_dict()
 
             if super().get_bank_id() == super().COOP:
 
                 data["message"] = response_data.get("MessageDescription", "")
                 data["code"] = response_data.get("MessageCode", "-111111")
-                data["statement_time"] = response_data.get("MessageDateTime", "")
+                data["statement_time"] = response_data.get(
+                    "MessageDateTime", "")
+                data["statement_reference"] = response_data.get(
+                    "MessageReference", "")
                 data["transactions"] = []
 
                 transactions = response_data.get("Transactions", [])
 
                 for i in range(len(transactions)):
-                    transaction = {
-                        "currency_code": "KES",
-                        "date": transactions[i].get("TransactionDate", ""),
-                        "description": transactions[i].get("Narration", ""),
-                    }
+
+                    transaction.update(
+                        {
+                            "currency_code": "KES",
+                            "date": transactions[i].get("TransactionDate", ""),
+                            "description": transactions[i].get("Narration", ""),
+                            "transaction_id": transactions[i].get("TransactionID", ""),
+                            "value_date": transactions[i].get("ValueDate", ""),
+                            "service_point": transactions[i].get("ServicePoint", ""),
+                            "running_cleared_balance": transactions[i].get("RunningClearedBalance", ""),
+                            "debit_limit": float(transactions[i].get("DebitLimit", -1)),
+                            "limit_expiry_date": transactions[i].get("LimitExpiryDate", ""),
+                        }
+                    )
 
                     if transactions[i].get("TransactionType", "") == "D":
                         transaction["amount"] = transactions[i].get(
                             "DebitAmount", "")
                         transaction["type"] = "Debit"
 
                     elif transactions[i].get("TransactionType", "") == "C":
                         transaction["amount"] = transactions[i].get(
                             "CreditAmount", "")
                         transaction["type"] = "Credit"
 
                     transaction["reference"] = transactions[i].get(
                         "TransactionReference", "")
                     transaction["running_balance"] = transactions[i].get(
-                        "RunningClearedBalance", "")
+                        "RunningBookBalance", "")
 
                     data["transactions"].append(transaction)
 
             elif super().get_bank_id() == super().EQUITY:
 
                 try:
                     if isinstance(response_data, str):
@@ -418,68 +452,86 @@
                         response_data = json.loads(response_data)
                 except Exception as e:
                     data['error'] = e
 
                 if isinstance(response_data, dict):
                     data["message"] = response_data.get("message", "")
                     data["code"] = f'{response_data.get("code", -111111)}'
-                    data["statement_time"] = response_data.get("response_time", "")
+                    data["statement_time"] = response_data.get(
+                        "response_time", "")
+                    data["statement_reference"] = ""
                     data["transactions"] = []
 
                     transactions = response_data.get(
                         "data", {}).get("transactions", [])
 
                     for i in range(len(transactions)):
 
-                        transaction = {
+                        transaction.update({
                             "currency_code": response_data.get("data", {}).get("currency", "KES"),
                             "date": datetime.fromisoformat(
                                 transactions[i].get(
-                                    "postedDateTime", "") + '+00:00'
+                                    "date", "") + '+00:00'
                             ).strftime('%Y-%m-%d %H:%M:%S'),
                             "description": transactions[i].get("description", ""),
                             "amount":  f'{transactions[i].get("amount", "")}',
                             "type":  transactions[i].get("type", ""),
+                            "serial":  transactions[i].get("serial", ""),
                             "reference":  transactions[i].get("reference", ""),
-                            "running_balance":  f'{transactions[i].get("runningBalance", {}).get("amount", "")}'
-                        }
+                            "running_balance":  f'{transactions[i].get("runningBalance", {}).get("amount", "")}',
+                            "posted_date": datetime.fromisoformat(
+                                transactions[i].get(
+                                    "postedDateTime", "") + '+00:00'
+                            ).strftime('%Y-%m-%d %H:%M:%S'),
+                        })
 
                         data["transactions"].append(transaction)
                 else:
                     data['response'] = response_data
 
             # If bank_id is UBA
             elif super().get_bank_id() == super().UBA:
 
                 data["message"] = ''
                 data["code"] = int(float(response_data.get("sendTransactionResponse", {}).get(
                     "return", {}).get("C24TRANRES", {}).get("ACTION_CODE", "-111111")))
+                data["statement_reference"] = f'{response_data.get("sendTransactionResponse", {}).get("return", {}).get("C24TRANRES", {}).get("STAN", "")}'
                 if data["code"]:
                     data["message"] = "Transaction Failed"
                 else:
                     data["message"] = "Success"
                 data["transactions"] = []
 
                 transactions = response_data.get("sendTransactionResponse", {}).get("return", {}).get(
                     "C24TRANRES", {}).get("TRANS_INFO", {}).get("TRAN", {}).get("element", [])
 
                 for i in range(len(transactions)):
-                    transaction = {
-                        "date": datetime.strptime(f'{transactions[i].get("DATE_POSTED", None)}', '%Y%d%m%H%M%S').strftime('%Y-%m-%d %H:%M:%S'),
+                    transaction.update({
+                        "currency_code": response_data.get("sendTransactionResponse", {}).get(
+                            "return", {}).get("C24TRANRES", {}).get("BALANCE_CURRENCY", "NGN"),
+                        "date": datetime.strptime(f'{transactions[i].get("TRAN_DATE", None)}', '%Y%d%m').strftime('%Y-%m-%d'),
+
                         "description": transactions[i].get("NARRATION", ""),
                         "amount": transactions[i].get("TRAN_AMT", -1),
-                        "reference": transactions[i].get("TRAN_ID", ""),
                         "running_balance": transactions[i].get("BALANCE", -1),
-                    }
+
+                        "transaction_id": transactions[i].get("TRAN_ID", ""),
+                        "serial": f'{transactions[i].get("TRAN_SNUM", "")}',
+                        "value_date": datetime.strptime(f'{transactions[i].get("VALUE_DATE", None)}', '%Y%d%m').strftime('%Y-%m-%d'),
+                        "posted_date": datetime.strptime(f'{transactions[i].get("DATE_POSTED", None)}', '%Y%d%m%H%M%S').strftime('%Y-%m-%d %H:%M:%S'),
+                    })
 
                     if transactions[i].get("PART_TRAN_TYPE", "") == "D":
                         transaction["type"] = "Debit"
                     elif transactions[i].get("PART_TRAN_TYPE", "") == "C":
                         transaction["type"] = "Credit"
 
+                    if transactions[i].get("REF_NUM", {}).get("@null", "true") == "true":
+                        transaction["reference"] = ""
+
                     data["transactions"].append(transaction)
 
         elif super().get_operation() == super().PDF_TO_JSON or super().get_operation() == super().GET_JSON_PDF:
             data = self.standardize_pdf_to_json(response_data=response_data)
 
         elif super().get_operation() == super().FOREX_RATE:
```

### Comparing `nashbanksync-0.1.8/bank_sync/Resources/banks.py` & `nashbanksync-0.1.9/bank_sync/Resources/banks.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/Resources/operations.py` & `nashbanksync-0.1.9/bank_sync/Resources/operations.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/Resources/payments.py` & `nashbanksync-0.1.9/bank_sync/Resources/payments.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/Resources/resource.py` & `nashbanksync-0.1.9/bank_sync/Resources/resource.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/middlewares/logs.py` & `nashbanksync-0.1.9/bank_sync/middlewares/logs.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/migrations/0001_initial.py` & `nashbanksync-0.1.9/bank_sync/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/migrations/0003_requestlogs.py` & `nashbanksync-0.1.9/bank_sync/migrations/0003_requestlogs.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/migrations/0007_responselogs.py` & `nashbanksync-0.1.9/bank_sync/migrations/0007_responselogs.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/migrations/0010_auto_20221117_1406.py` & `nashbanksync-0.1.9/bank_sync/migrations/0010_auto_20221117_1406.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/migrations/0011_ipndata.py` & `nashbanksync-0.1.9/bank_sync/migrations/0011_ipndata.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/models.py` & `nashbanksync-0.1.9/bank_sync/models.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/bank_sync/tests.py` & `nashbanksync-0.1.9/bank_sync/tests.py`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/nashbanksync.egg-info/PKG-INFO` & `nashbanksync-0.1.9/nashbanksync.egg-info/PKG-INFO`

 * *Files 7% similar despite different names*

```diff
@@ -1,16 +1,14 @@
 Metadata-Version: 2.1
 Name: nashbanksync
-Version: 0.1.8
+Version: 0.1.9
 Summary: Python library for connecting to the Nash Banks Framework
 Home-page: https://github.com/NashInc/NashSync.git
 Author: Dansol Obondo
 Author-email: dansol@nashafrica.co
-License: UNKNOWN
-Platform: UNKNOWN
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Description-Content-Type: text/markdown
 License-File: LICENSE
@@ -25,8 +23,7 @@
     pip install nashbanksync
 ```
 2.	View get started documentation:
 ```bash
     https://nashbanksuite.readme.io/v1.2.0/docs
 ```
 3.	Start Coding
-
```

### Comparing `nashbanksync-0.1.8/nashbanksync.egg-info/SOURCES.txt` & `nashbanksync-0.1.9/nashbanksync.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `nashbanksync-0.1.8/setup.py` & `nashbanksync-0.1.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="nashbanksync",
-    version="0.1.8",
+    version="0.1.9",
     author="Dansol Obondo",
     author_email="dansol@nashafrica.co",
     description='Python library for connecting to the Nash Banks Framework',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/NashInc/NashSync.git",
     packages=setuptools.find_packages(),
```

