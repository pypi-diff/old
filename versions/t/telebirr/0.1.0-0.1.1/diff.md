# Comparing `tmp/telebirr-0.1.0.tar.gz` & `tmp/telebirr-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "telebirr-0.1.0.tar", last modified: Tue Mar 28 07:10:49 2023, max compression
+gzip compressed data, was "telebirr-0.1.1.tar", last modified: Thu Apr  6 10:59:47 2023, max compression
```

## Comparing `telebirr-0.1.0.tar` & `telebirr-0.1.1.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 07:10:49.281477 telebirr-0.1.0/
--rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-03-28 07:10:49.281477 telebirr-0.1.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-03-28 07:10:37.000000 telebirr-0.1.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-03-28 07:10:49.281477 telebirr-0.1.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1099 2023-03-28 07:10:37.000000 telebirr-0.1.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 07:10:49.281477 telebirr-0.1.0/telebirr/
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-03-28 07:10:37.000000 telebirr-0.1.0/telebirr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7541 2023-03-28 07:10:37.000000 telebirr-0.1.0/telebirr/telebirr.py
--rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-03-28 07:10:37.000000 telebirr-0.1.0/telebirr/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-28 07:10:49.281477 telebirr-0.1.0/telebirr.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-03-28 07:10:49.000000 telebirr-0.1.0/telebirr.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      237 2023-03-28 07:10:49.000000 telebirr-0.1.0/telebirr.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-28 07:10:49.000000 telebirr-0.1.0/telebirr.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-03-28 07:10:49.000000 telebirr-0.1.0/telebirr.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-03-28 07:10:49.000000 telebirr-0.1.0/telebirr.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:59:47.009749 telebirr-0.1.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-06 10:59:47.009749 telebirr-0.1.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-04-06 10:59:37.000000 telebirr-0.1.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 10:59:47.009749 telebirr-0.1.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1099 2023-04-06 10:59:37.000000 telebirr-0.1.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:59:47.009749 telebirr-0.1.1/telebirr/
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-06 10:59:37.000000 telebirr-0.1.1/telebirr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8548 2023-04-06 10:59:37.000000 telebirr-0.1.1/telebirr/telebirr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-04-06 10:59:37.000000 telebirr-0.1.1/telebirr/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:59:47.009749 telebirr-0.1.1/telebirr.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      237 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/top_level.txt
```

### Comparing `telebirr-0.1.0/PKG-INFO` & `telebirr-0.1.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: telebirr
-Version: 0.1.0
+Version: 0.1.1
 Summary: Telebirr integration
 Author: Eba Alemayehu
 Author-email: <ebaalemayhu3@gmail.com>
 Keywords: python,telebirr,payment,ethiopia,ethio telecom
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `telebirr-0.1.0/README.md` & `telebirr-0.1.1/README.md`

 * *Files identical despite different names*

### Comparing `telebirr-0.1.0/setup.py` & `telebirr-0.1.1/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 import os
 
 here = os.path.abspath(os.path.dirname(__file__))
 
 with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
     long_description = "\n" + fh.read()
 
-VERSION = '0.1.0'
+VERSION = '0.1.1'
 DESCRIPTION = 'Telebirr integration'
 LONG_DESCRIPTION = 'This package is a helper package with telebirr integration.'
 
 # Setting up
 setup(
     name="telebirr",
     version=VERSION,
```

### Comparing `telebirr-0.1.0/telebirr/telebirr.py` & `telebirr-0.1.1/telebirr/telebirr.py`

 * *Files 4% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-import datetime, json, requests, base64, hashlib, re, time
+import datetime, json, requests, base64, hashlib, re, time, uuid
 from Crypto.PublicKey import RSA
 from Crypto.Cipher import PKCS1_v1_5
 
 from cryptography.hazmat.primitives import hashes
 from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
 from cryptography.hazmat.backends import default_backend
 from cryptography.hazmat.primitives.serialization import load_der_public_key
@@ -99,14 +99,45 @@
         self.url = url
 
 
     def apply_fabric_token(self):
         response = requests.post(url=self.url+"/apiaccess/payment/gateway/payment/v1/token", headers={"X-App-key": self.app_key}, json={"appSecret": self.app_secret}, verify=False)
         return json.loads(response.content)
 
+    def auth(self, token):
+        fabric_token = self.apply_fabric_token()
+        url = self.url + "/apiaccess/payment/gateway/payment/v1/auth/authToken"
+
+        payload = {
+            "timestamp": "{}".format(int(time.time())),
+            "method": "payment.authtoken",
+            "nonce_str": str(uuid.uuid4().hex),
+            "biz_content": {
+                access_token: token,
+                trade_type: "InApp",
+                appid: self.merchant_id,
+                resource_type: "OpenId",
+            },
+            "version": "1.0",
+            "sign_type": "SHA256WithRSA",
+        }
+        signature = utils.sign(payload, self.private_key)
+        payload['sign'] = signature
+
+        response = requests.post(
+            url=url,
+            headers={
+                "X-App-key": self.app_key,
+                "Authorization": fabric_token.get("token")
+            },
+            json=payload,
+            verify=False
+        )
+        return json.loads(response.content)
+
     def request_create_order(self, nonce_str, amount, notify_url, redirect_url, merch_order_id, timeout_express, title, business_type, payee_identifier_type):
         fabric_token = self.apply_fabric_token()
         url = self.url+"/apiaccess/payment/gateway/payment/v1/merchant/preOrder"
 
         payload = {
                 "nonce_str": nonce_str,
                 "biz_content": {
```

### Comparing `telebirr-0.1.0/telebirr/utils.py` & `telebirr-0.1.1/telebirr/utils.py`

 * *Files identical despite different names*

### Comparing `telebirr-0.1.0/telebirr.egg-info/PKG-INFO` & `telebirr-0.1.1/telebirr.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: telebirr
-Version: 0.1.0
+Version: 0.1.1
 Summary: Telebirr integration
 Author: Eba Alemayehu
 Author-email: <ebaalemayhu3@gmail.com>
 Keywords: python,telebirr,payment,ethiopia,ethio telecom
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

