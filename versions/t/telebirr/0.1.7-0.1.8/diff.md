# Comparing `tmp/telebirr-0.1.7.tar.gz` & `tmp/telebirr-0.1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "telebirr-0.1.7.tar", last modified: Fri Apr  7 09:22:50 2023, max compression
+gzip compressed data, was "telebirr-0.1.8.tar", last modified: Fri Apr  7 09:26:17 2023, max compression
```

## Comparing `telebirr-0.1.7.tar` & `telebirr-0.1.8.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:22:50.529872 telebirr-0.1.7/
--rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 09:22:50.529872 telebirr-0.1.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-04-07 09:22:34.000000 telebirr-0.1.7/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 09:22:50.529872 telebirr-0.1.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1099 2023-04-07 09:22:34.000000 telebirr-0.1.7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:22:50.525872 telebirr-0.1.7/telebirr/
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-07 09:22:34.000000 telebirr-0.1.7/telebirr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9012 2023-04-07 09:22:34.000000 telebirr-0.1.7/telebirr/telebirr.py
--rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-04-07 09:22:34.000000 telebirr-0.1.7/telebirr/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:22:50.529872 telebirr-0.1.7/telebirr.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 09:22:50.000000 telebirr-0.1.7/telebirr.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      237 2023-04-07 09:22:50.000000 telebirr-0.1.7/telebirr.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 09:22:50.000000 telebirr-0.1.7/telebirr.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 09:22:50.000000 telebirr-0.1.7/telebirr.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 09:22:50.000000 telebirr-0.1.7/telebirr.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:26:17.031142 telebirr-0.1.8/
+-rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 09:26:17.031142 telebirr-0.1.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-04-07 09:26:06.000000 telebirr-0.1.8/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 09:26:17.031142 telebirr-0.1.8/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1099 2023-04-07 09:26:06.000000 telebirr-0.1.8/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:26:17.027142 telebirr-0.1.8/telebirr/
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-07 09:26:06.000000 telebirr-0.1.8/telebirr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9042 2023-04-07 09:26:06.000000 telebirr-0.1.8/telebirr/telebirr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-04-07 09:26:06.000000 telebirr-0.1.8/telebirr/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:26:17.031142 telebirr-0.1.8/telebirr.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      237 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/top_level.txt
```

### Comparing `telebirr-0.1.7/PKG-INFO` & `telebirr-0.1.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: telebirr
-Version: 0.1.7
+Version: 0.1.8
 Summary: Telebirr integration
 Author: Eba Alemayehu
 Author-email: <ebaalemayhu3@gmail.com>
 Keywords: python,telebirr,payment,ethiopia,ethio telecom
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `telebirr-0.1.7/README.md` & `telebirr-0.1.8/README.md`

 * *Files identical despite different names*

### Comparing `telebirr-0.1.7/setup.py` & `telebirr-0.1.8/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 import os
 
 here = os.path.abspath(os.path.dirname(__file__))
 
 with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
     long_description = "\n" + fh.read()
 
-VERSION = '0.1.7'
+VERSION = '0.1.8'
 DESCRIPTION = 'Telebirr integration'
 LONG_DESCRIPTION = 'This package is a helper package with telebirr integration.'
 
 # Setting up
 setup(
     name="telebirr",
     version=VERSION,
```

### Comparing `telebirr-0.1.7/telebirr/telebirr.py` & `telebirr-0.1.8/telebirr/telebirr.py`

 * *Files 1% similar despite different names*

```diff
@@ -134,14 +134,15 @@
         )
         return json.loads(response.content)
 
     def request_create_order(self, nonce_str, amount, notify_url, redirect_url, merch_order_id, timeout_express, title, business_type, payee_identifier_type):
         fabric_token = self.apply_fabric_token()
         url = self.url+"/apiaccess/payment/gateway/payment/v1/merchant/preOrder"
         SIGN_TYPE = "SHA256WithRSA"
+        timestamp = "{}".format(int(time.time()))
         payload = {
                 "nonce_str": nonce_str,
                 "biz_content": {
                      "notify_url": notify_url,
                      "redirect_url": redirect_url,
                      "trans_currency": "ETB",
                      "total_amount": amount,
@@ -155,15 +156,15 @@
                      "payee_identifier": self.short_code,
                      "payee_identifier_type": payee_identifier_type,
                      "payee_type": "5000"
                  },
                  "method": "payment.preorder",
                  "version": "1.0",
                  "sign_type": SIGN_TYPE,
-                 "timestamp": "{}".format(int(time.time()))
+                 "timestamp": timestamp
             }
         signature = utils.sign(payload, self.private_key)
         payload['sign'] = signature
         print(payload)
         response = requests.post(
             url= url,
             headers={
```

### Comparing `telebirr-0.1.7/telebirr/utils.py` & `telebirr-0.1.8/telebirr/utils.py`

 * *Files identical despite different names*

### Comparing `telebirr-0.1.7/telebirr.egg-info/PKG-INFO` & `telebirr-0.1.8/telebirr.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: telebirr
-Version: 0.1.7
+Version: 0.1.8
 Summary: Telebirr integration
 Author: Eba Alemayehu
 Author-email: <ebaalemayhu3@gmail.com>
 Keywords: python,telebirr,payment,ethiopia,ethio telecom
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

