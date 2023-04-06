# Comparing `tmp/badsecrets-0.1.284.tar.gz` & `tmp/badsecrets-0.1.287.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "badsecrets-0.1.284.tar", max compression
+gzip compressed data, was "badsecrets-0.1.287.tar", max compression
```

## Comparing `badsecrets-0.1.284.tar` & `badsecrets-0.1.287.tar`

### file list

```diff
@@ -1,35 +1,35 @@
--rw-r--r--   0        0        0    35149 2023-04-06 04:49:11.142422 badsecrets-0.1.284/LICENSE
--rw-r--r--   0        0        0    25791 2023-04-06 04:49:11.142422 badsecrets-0.1.284/README.md
--rw-r--r--   0        0        0      711 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/__init__.py
--rw-r--r--   0        0        0     4485 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/base.py
--rw-r--r--   0        0        0      233 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/errors.py
--rw-r--r--   0        0        0     3570 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/helpers.py
--rw-r--r--   0        0        0        0 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/__init__.py
--rw-r--r--   0        0        0     5865 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/aspnet_viewstate.py
--rw-r--r--   0        0        0     1032 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/django_signedcookies.py
--rw-r--r--   0        0        0     2076 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/express_signedcookies.py
--rw-r--r--   0        0        0      856 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/flask_signedcookies.py
--rw-r--r--   0        0        0     3363 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/generic_jwt.py
--rw-r--r--   0        0        0    13573 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/jsf_viewstate.py
--rw-r--r--   0        0        0     1325 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/peoplesoft_pstoken.py
--rw-r--r--   0        0        0     3058 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/rails_secretkeybase.py
--rw-r--r--   0        0        0     2098 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/symfony_signedurl.py
--rw-r--r--   0        0        0     4943 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/telerik_encryptionkey.py
--rw-r--r--   0        0        0     2961 2023-04-06 04:49:11.142422 badsecrets-0.1.284/badsecrets/modules/telerik_hashkey.py
--rw-r--r--   0        0        0   654111 2023-04-06 04:49:11.150422 badsecrets-0.1.284/badsecrets/resources/aspnet_machinekeys.txt
--rw-r--r--   0        0        0    31178 2023-04-06 04:49:11.150422 badsecrets-0.1.284/badsecrets/resources/django_secret_keys.txt
--rw-r--r--   0        0        0    40993 2023-04-06 04:49:11.150422 badsecrets-0.1.284/badsecrets/resources/express_session_secrets.txt
--rw-r--r--   0        0        0  1777603 2023-04-06 04:49:11.170422 badsecrets-0.1.284/badsecrets/resources/flask_secret_keys.txt
--rw-r--r--   0        0        0       87 2023-04-06 04:49:11.170422 badsecrets-0.1.284/badsecrets/resources/jsf_viewstate_passwords.txt
--rw-r--r--   0        0        0     1257 2023-04-06 04:49:11.170422 badsecrets-0.1.284/badsecrets/resources/jsf_viewstate_passwords_b64.txt
--rw-r--r--   0        0        0     7785 2023-04-06 04:49:11.170422 badsecrets-0.1.284/badsecrets/resources/jwt_rsakeys_private.txt
--rw-r--r--   0        0        0     2122 2023-04-06 04:49:11.170422 badsecrets-0.1.284/badsecrets/resources/jwt_rsakeys_public.txt
--rw-r--r--   0        0        0   113170 2023-04-06 04:49:11.174422 badsecrets-0.1.284/badsecrets/resources/jwt_secrets.txt
--rw-r--r--   0        0        0       78 2023-04-06 04:49:11.174422 badsecrets-0.1.284/badsecrets/resources/peoplesoft_passwords.txt
--rw-r--r--   0        0        0     6184 2023-04-06 04:49:11.174422 badsecrets-0.1.284/badsecrets/resources/rails_secret_key_base.txt
--rw-r--r--   0        0        0     3009 2023-04-06 04:49:11.174422 badsecrets-0.1.284/badsecrets/resources/symfony_appsecret.txt
--rw-r--r--   0        0        0    18037 2023-04-06 04:49:11.174422 badsecrets-0.1.284/badsecrets/resources/telerik_encryption_keys.txt
--rw-r--r--   0        0        0    17990 2023-04-06 04:49:11.174422 badsecrets-0.1.284/badsecrets/resources/telerik_hash_keys.txt
--rw-r--r--   0        0        0    76516 2023-04-06 04:49:11.174422 badsecrets-0.1.284/badsecrets/resources/top_10000_passwords.txt
--rw-r--r--   0        0        0      872 2023-04-06 04:49:33.238804 badsecrets-0.1.284/pyproject.toml
--rw-r--r--   0        0        0    26604 1970-01-01 00:00:00.000000 badsecrets-0.1.284/PKG-INFO
+-rw-r--r--   0        0        0    35149 2023-04-06 18:41:42.102580 badsecrets-0.1.287/LICENSE
+-rw-r--r--   0        0        0    25791 2023-04-06 18:41:42.102580 badsecrets-0.1.287/README.md
+-rw-r--r--   0        0        0      711 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/__init__.py
+-rw-r--r--   0        0        0     4485 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/base.py
+-rw-r--r--   0        0        0      233 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/errors.py
+-rw-r--r--   0        0        0     3570 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/helpers.py
+-rw-r--r--   0        0        0        0 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/__init__.py
+-rw-r--r--   0        0        0     5865 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/aspnet_viewstate.py
+-rw-r--r--   0        0        0     1032 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/django_signedcookies.py
+-rw-r--r--   0        0        0     2079 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/express_signedcookies.py
+-rw-r--r--   0        0        0      856 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/flask_signedcookies.py
+-rw-r--r--   0        0        0     3363 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/generic_jwt.py
+-rw-r--r--   0        0        0    13573 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/jsf_viewstate.py
+-rw-r--r--   0        0        0     1325 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/peoplesoft_pstoken.py
+-rw-r--r--   0        0        0     3058 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/rails_secretkeybase.py
+-rw-r--r--   0        0        0     2098 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/symfony_signedurl.py
+-rw-r--r--   0        0        0     4943 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/telerik_encryptionkey.py
+-rw-r--r--   0        0        0     2961 2023-04-06 18:41:42.102580 badsecrets-0.1.287/badsecrets/modules/telerik_hashkey.py
+-rw-r--r--   0        0        0   654111 2023-04-06 18:41:42.110580 badsecrets-0.1.287/badsecrets/resources/aspnet_machinekeys.txt
+-rw-r--r--   0        0        0    31178 2023-04-06 18:41:42.110580 badsecrets-0.1.287/badsecrets/resources/django_secret_keys.txt
+-rw-r--r--   0        0        0    40993 2023-04-06 18:41:42.110580 badsecrets-0.1.287/badsecrets/resources/express_session_secrets.txt
+-rw-r--r--   0        0        0  1777603 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/flask_secret_keys.txt
+-rw-r--r--   0        0        0       87 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/jsf_viewstate_passwords.txt
+-rw-r--r--   0        0        0     1257 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/jsf_viewstate_passwords_b64.txt
+-rw-r--r--   0        0        0     7785 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/jwt_rsakeys_private.txt
+-rw-r--r--   0        0        0     2122 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/jwt_rsakeys_public.txt
+-rw-r--r--   0        0        0   113170 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/jwt_secrets.txt
+-rw-r--r--   0        0        0       78 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/peoplesoft_passwords.txt
+-rw-r--r--   0        0        0     6184 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/rails_secret_key_base.txt
+-rw-r--r--   0        0        0     3009 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/symfony_appsecret.txt
+-rw-r--r--   0        0        0    18037 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/telerik_encryption_keys.txt
+-rw-r--r--   0        0        0    17990 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/telerik_hash_keys.txt
+-rw-r--r--   0        0        0    76516 2023-04-06 18:41:42.126580 badsecrets-0.1.287/badsecrets/resources/top_10000_passwords.txt
+-rw-r--r--   0        0        0      872 2023-04-06 18:42:02.790735 badsecrets-0.1.287/pyproject.toml
+-rw-r--r--   0        0        0    26604 1970-01-01 00:00:00.000000 badsecrets-0.1.287/PKG-INFO
```

### Comparing `badsecrets-0.1.284/LICENSE` & `badsecrets-0.1.287/LICENSE`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/README.md` & `badsecrets-0.1.287/README.md`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/__init__.py` & `badsecrets-0.1.287/badsecrets/__init__.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/base.py` & `badsecrets-0.1.287/badsecrets/base.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/helpers.py` & `badsecrets-0.1.287/badsecrets/helpers.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/aspnet_viewstate.py` & `badsecrets-0.1.287/badsecrets/modules/aspnet_viewstate.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/django_signedcookies.py` & `badsecrets-0.1.287/badsecrets/modules/django_signedcookies.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/express_signedcookies.py` & `badsecrets-0.1.287/badsecrets/modules/express_signedcookies.py`

 * *Files 1% similar despite different names*

```diff
@@ -13,15 +13,15 @@
 
 def no_padding_urlsafe_base64_encode(enc):
     return base64.urlsafe_b64encode(enc).decode().rstrip("=").replace("-", "+").replace("_", "/")
 
 
 class ExpressSignedCookies(BadsecretsBase):
     identify_regex = re.compile(r"^s%3[Aa][^\.]+\.[a-zA-Z0-9%]{20,90}$")
-    description = {"Product": "Express.js Signed Cookie", "Secret": "Express SESSION_SECRET"}
+    description = {"Product": "Express.js Signed Cookie", "Secret": "Express.js SESSION_SECRET"}
 
     def carve_regex(self):
         return re.compile(r"(s%3[Aa][^\.]+\.[a-zA-Z0-9%]{20,90})")
 
     def expressHMAC(self, payload, secret, hash_algorithm):
         return no_padding_urlsafe_base64_encode(hmac.HMAC(secret.encode(), payload.encode(), hash_algorithm).digest())
```

### Comparing `badsecrets-0.1.284/badsecrets/modules/flask_signedcookies.py` & `badsecrets-0.1.287/badsecrets/modules/flask_signedcookies.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/generic_jwt.py` & `badsecrets-0.1.287/badsecrets/modules/generic_jwt.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/jsf_viewstate.py` & `badsecrets-0.1.287/badsecrets/modules/jsf_viewstate.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/peoplesoft_pstoken.py` & `badsecrets-0.1.287/badsecrets/modules/peoplesoft_pstoken.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/rails_secretkeybase.py` & `badsecrets-0.1.287/badsecrets/modules/rails_secretkeybase.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/symfony_signedurl.py` & `badsecrets-0.1.287/badsecrets/modules/symfony_signedurl.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/telerik_encryptionkey.py` & `badsecrets-0.1.287/badsecrets/modules/telerik_encryptionkey.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/modules/telerik_hashkey.py` & `badsecrets-0.1.287/badsecrets/modules/telerik_hashkey.py`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/aspnet_machinekeys.txt` & `badsecrets-0.1.287/badsecrets/resources/aspnet_machinekeys.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/django_secret_keys.txt` & `badsecrets-0.1.287/badsecrets/resources/django_secret_keys.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/express_session_secrets.txt` & `badsecrets-0.1.287/badsecrets/resources/express_session_secrets.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/flask_secret_keys.txt` & `badsecrets-0.1.287/badsecrets/resources/flask_secret_keys.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/jsf_viewstate_passwords_b64.txt` & `badsecrets-0.1.287/badsecrets/resources/jsf_viewstate_passwords_b64.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/jwt_rsakeys_private.txt` & `badsecrets-0.1.287/badsecrets/resources/jwt_rsakeys_private.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/jwt_rsakeys_public.txt` & `badsecrets-0.1.287/badsecrets/resources/jwt_rsakeys_public.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/jwt_secrets.txt` & `badsecrets-0.1.287/badsecrets/resources/jwt_secrets.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/rails_secret_key_base.txt` & `badsecrets-0.1.287/badsecrets/resources/rails_secret_key_base.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/symfony_appsecret.txt` & `badsecrets-0.1.287/badsecrets/resources/symfony_appsecret.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/telerik_encryption_keys.txt` & `badsecrets-0.1.287/badsecrets/resources/telerik_encryption_keys.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/telerik_hash_keys.txt` & `badsecrets-0.1.287/badsecrets/resources/telerik_hash_keys.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/badsecrets/resources/top_10000_passwords.txt` & `badsecrets-0.1.287/badsecrets/resources/top_10000_passwords.txt`

 * *Files identical despite different names*

### Comparing `badsecrets-0.1.284/pyproject.toml` & `badsecrets-0.1.287/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "badsecrets"
-version = "v0.1.284"
+version = "v0.1.287"
 description = "About"
 authors = ["A library for detecting known or weak secrets on across many platforms"]
 license = "GPL-3.0"
 readme = "README.md"
 
 [tool.poetry.dev-dependencies]
 requests-mock = "^1.10.0"
```

### Comparing `badsecrets-0.1.284/PKG-INFO` & `badsecrets-0.1.287/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: badsecrets
-Version: 0.1.284
+Version: 0.1.287
 Summary: About
 License: GPL-3.0
 Author: A library for detecting known or weak secrets on across many platforms
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: GNU General Public License v3 (GPLv3)
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.9
```

