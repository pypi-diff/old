# Comparing `tmp/telebirr-0.1.1.tar.gz` & `tmp/telebirr-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "telebirr-0.1.1.tar", last modified: Thu Apr  6 10:59:47 2023, max compression
+gzip compressed data, was "telebirr-0.1.2.tar", last modified: Fri Apr  7 07:29:11 2023, max compression
```

## Comparing `telebirr-0.1.1.tar` & `telebirr-0.1.2.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:59:47.009749 telebirr-0.1.1/
--rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-06 10:59:47.009749 telebirr-0.1.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-04-06 10:59:37.000000 telebirr-0.1.1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 10:59:47.009749 telebirr-0.1.1/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1099 2023-04-06 10:59:37.000000 telebirr-0.1.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:59:47.009749 telebirr-0.1.1/telebirr/
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-06 10:59:37.000000 telebirr-0.1.1/telebirr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     8548 2023-04-06 10:59:37.000000 telebirr-0.1.1/telebirr/telebirr.py
--rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-04-06 10:59:37.000000 telebirr-0.1.1/telebirr/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 10:59:47.009749 telebirr-0.1.1/telebirr.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      237 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-06 10:59:47.000000 telebirr-0.1.1/telebirr.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:29:11.813419 telebirr-0.1.2/
+-rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 07:29:11.809419 telebirr-0.1.2/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-04-07 07:28:59.000000 telebirr-0.1.2/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 07:29:11.813419 telebirr-0.1.2/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1099 2023-04-07 07:28:59.000000 telebirr-0.1.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:29:11.809419 telebirr-0.1.2/telebirr/
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-07 07:28:59.000000 telebirr-0.1.2/telebirr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9060 2023-04-07 07:28:59.000000 telebirr-0.1.2/telebirr/telebirr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-04-07 07:28:59.000000 telebirr-0.1.2/telebirr/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 07:29:11.809419 telebirr-0.1.2/telebirr.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 07:29:11.000000 telebirr-0.1.2/telebirr.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      237 2023-04-07 07:29:11.000000 telebirr-0.1.2/telebirr.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 07:29:11.000000 telebirr-0.1.2/telebirr.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 07:29:11.000000 telebirr-0.1.2/telebirr.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 07:29:11.000000 telebirr-0.1.2/telebirr.egg-info/top_level.txt
```

### Comparing `telebirr-0.1.1/PKG-INFO` & `telebirr-0.1.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: telebirr
-Version: 0.1.1
+Version: 0.1.2
 Summary: Telebirr integration
 Author: Eba Alemayehu
 Author-email: <ebaalemayhu3@gmail.com>
 Keywords: python,telebirr,payment,ethiopia,ethio telecom
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `telebirr-0.1.1/README.md` & `telebirr-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `telebirr-0.1.1/setup.py` & `telebirr-0.1.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 import os
 
 here = os.path.abspath(os.path.dirname(__file__))
 
 with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
     long_description = "\n" + fh.read()
 
-VERSION = '0.1.1'
+VERSION = '0.1.2'
 DESCRIPTION = 'Telebirr integration'
 LONG_DESCRIPTION = 'This package is a helper package with telebirr integration.'
 
 # Setting up
 setup(
     name="telebirr",
     version=VERSION,
```

### Comparing `telebirr-0.1.1/telebirr/telebirr.py` & `telebirr-0.1.2/telebirr/telebirr.py`

 * *Files 3% similar despite different names*

```diff
@@ -169,15 +169,25 @@
             headers={
                 "X-App-key": self.app_key,
                 "Authorization": fabric_token.get("token")
             },
             json=payload,
             verify=False
         )
-        return json.loads(response.content)
+        payload = {
+                "appid": settings.TELEBIRR_SUPPER_APP_MERCHANT_ID,
+                "merch_code": payment_order.id,
+                "nonce_str": payment_order_request.request_id,
+                "prepay_id": order_response.get('biz_content').get('prepay_id'),
+                "timestamp": timestamp,
+                "sign_type": order_response.get('sign_type')
+            }
+        pay_signature = utils.sign(payload, self.private_key)
+        payload["sign"] = pay_signature
+        return json.loads(response.content), signed_payload
 
     def queryOrder(self, nonce_str, sign, merch_order_id, version="1.0", method="payment.queryorder", sign_type="SHA256WithRSA"):
         fabric_token = self.apply_fabric_token()
 
         response = requests.post(
             url=self.url,
             headers={
```

### Comparing `telebirr-0.1.1/telebirr/utils.py` & `telebirr-0.1.2/telebirr/utils.py`

 * *Files identical despite different names*

### Comparing `telebirr-0.1.1/telebirr.egg-info/PKG-INFO` & `telebirr-0.1.2/telebirr.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: telebirr
-Version: 0.1.1
+Version: 0.1.2
 Summary: Telebirr integration
 Author: Eba Alemayehu
 Author-email: <ebaalemayhu3@gmail.com>
 Keywords: python,telebirr,payment,ethiopia,ethio telecom
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

