# Comparing `tmp/telebirr-0.1.8.tar.gz` & `tmp/telebirr-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "telebirr-0.1.8.tar", last modified: Fri Apr  7 09:26:17 2023, max compression
+gzip compressed data, was "telebirr-0.1.9.tar", last modified: Fri Apr  7 09:30:20 2023, max compression
```

## Comparing `telebirr-0.1.8.tar` & `telebirr-0.1.9.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:26:17.031142 telebirr-0.1.8/
--rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 09:26:17.031142 telebirr-0.1.8/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-04-07 09:26:06.000000 telebirr-0.1.8/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 09:26:17.031142 telebirr-0.1.8/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1099 2023-04-07 09:26:06.000000 telebirr-0.1.8/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:26:17.027142 telebirr-0.1.8/telebirr/
--rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-07 09:26:06.000000 telebirr-0.1.8/telebirr/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     9042 2023-04-07 09:26:06.000000 telebirr-0.1.8/telebirr/telebirr.py
--rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-04-07 09:26:06.000000 telebirr-0.1.8/telebirr/utils.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:26:17.031142 telebirr-0.1.8/telebirr.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      237 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 09:26:17.000000 telebirr-0.1.8/telebirr.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:30:20.333988 telebirr-0.1.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 09:30:20.333988 telebirr-0.1.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     5455 2023-04-07 09:30:10.000000 telebirr-0.1.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 09:30:20.333988 telebirr-0.1.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1099 2023-04-07 09:30:10.000000 telebirr-0.1.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:30:20.333988 telebirr-0.1.9/telebirr/
+-rw-r--r--   0 runner    (1001) docker     (123)       31 2023-04-07 09:30:10.000000 telebirr-0.1.9/telebirr/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9035 2023-04-07 09:30:10.000000 telebirr-0.1.9/telebirr/telebirr.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2348 2023-04-07 09:30:10.000000 telebirr-0.1.9/telebirr/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 09:30:20.333988 telebirr-0.1.9/telebirr.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     5976 2023-04-07 09:30:20.000000 telebirr-0.1.9/telebirr.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      237 2023-04-07 09:30:20.000000 telebirr-0.1.9/telebirr.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 09:30:20.000000 telebirr-0.1.9/telebirr.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       35 2023-04-07 09:30:20.000000 telebirr-0.1.9/telebirr.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        9 2023-04-07 09:30:20.000000 telebirr-0.1.9/telebirr.egg-info/top_level.txt
```

### Comparing `telebirr-0.1.8/PKG-INFO` & `telebirr-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: telebirr
-Version: 0.1.8
+Version: 0.1.9
 Summary: Telebirr integration
 Author: Eba Alemayehu
 Author-email: <ebaalemayhu3@gmail.com>
 Keywords: python,telebirr,payment,ethiopia,ethio telecom
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

### Comparing `telebirr-0.1.8/README.md` & `telebirr-0.1.9/README.md`

 * *Files identical despite different names*

### Comparing `telebirr-0.1.8/setup.py` & `telebirr-0.1.9/setup.py`

 * *Files 10% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 import os
 
 here = os.path.abspath(os.path.dirname(__file__))
 
 with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
     long_description = "\n" + fh.read()
 
-VERSION = '0.1.8'
+VERSION = '0.1.9'
 DESCRIPTION = 'Telebirr integration'
 LONG_DESCRIPTION = 'This package is a helper package with telebirr integration.'
 
 # Setting up
 setup(
     name="telebirr",
     version=VERSION,
```

### Comparing `telebirr-0.1.8/telebirr/telebirr.py` & `telebirr-0.1.9/telebirr/telebirr.py`

 * *Files 0% similar despite different names*

```diff
@@ -181,15 +181,15 @@
             "nonce_str": nonce_str,
             "prepay_id": response.get('biz_content').get('prepay_id'),
             "timestamp": timestamp,
             "sign_type": SIGN_TYPE
         }
         pay_signature = utils.sign(payload, self.private_key)
         payload["sign"] = pay_signature
-        return response, signed_payload
+        return response, payload
 
     def queryOrder(self, nonce_str, sign, merch_order_id, version="1.0", method="payment.queryorder", sign_type="SHA256WithRSA"):
         fabric_token = self.apply_fabric_token()
 
         response = requests.post(
             url=self.url,
             headers={
```

### Comparing `telebirr-0.1.8/telebirr/utils.py` & `telebirr-0.1.9/telebirr/utils.py`

 * *Files identical despite different names*

### Comparing `telebirr-0.1.8/telebirr.egg-info/PKG-INFO` & `telebirr-0.1.9/telebirr.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: telebirr
-Version: 0.1.8
+Version: 0.1.9
 Summary: Telebirr integration
 Author: Eba Alemayehu
 Author-email: <ebaalemayhu3@gmail.com>
 Keywords: python,telebirr,payment,ethiopia,ethio telecom
 Classifier: Development Status :: 1 - Planning
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3
```

