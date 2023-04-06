# Comparing `tmp/PyLockAES-1.2.tar.gz` & `tmp/PyLockAES-1.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "PyLockAES-1.2.tar", last modified: Thu Apr  6 11:03:09 2023, max compression
+gzip compressed data, was "PyLockAES-1.2.1.tar", last modified: Thu Apr  6 11:07:48 2023, max compression
```

## Comparing `PyLockAES-1.2.tar` & `PyLockAES-1.2.1.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:03:09.505445 PyLockAES-1.2/
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      158 2023-04-06 11:03:09.505445 PyLockAES-1.2/PKG-INFO
-drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:03:09.505445 PyLockAES-1.2/PyLockAES.egg-info/
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      158 2023-04-06 11:03:09.000000 PyLockAES-1.2/PyLockAES.egg-info/PKG-INFO
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      191 2023-04-06 11:03:09.000000 PyLockAES-1.2/PyLockAES.egg-info/SOURCES.txt
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)        1 2023-04-06 11:03:09.000000 PyLockAES-1.2/PyLockAES.egg-info/dependency_links.txt
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       10 2023-04-06 11:03:09.000000 PyLockAES-1.2/PyLockAES.egg-info/top_level.txt
-drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:03:09.505445 PyLockAES-1.2/pylockaes/
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1651 2023-04-06 11:02:03.000000 PyLockAES-1.2/pylockaes/__init__.py
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1650 2023-04-06 11:02:03.000000 PyLockAES-1.2/pylockaes/encrypt_decrypt.py
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       38 2023-04-06 11:03:09.505445 PyLockAES-1.2/setup.cfg
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      235 2023-04-06 11:02:03.000000 PyLockAES-1.2/setup.py
+drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:07:48.559723 PyLockAES-1.2.1/
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      160 2023-04-06 11:07:48.559723 PyLockAES-1.2.1/PKG-INFO
+drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:07:48.559723 PyLockAES-1.2.1/PyLockAES.egg-info/
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      160 2023-04-06 11:07:48.000000 PyLockAES-1.2.1/PyLockAES.egg-info/PKG-INFO
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      191 2023-04-06 11:07:48.000000 PyLockAES-1.2.1/PyLockAES.egg-info/SOURCES.txt
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)        1 2023-04-06 11:07:48.000000 PyLockAES-1.2.1/PyLockAES.egg-info/dependency_links.txt
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       10 2023-04-06 11:07:48.000000 PyLockAES-1.2.1/PyLockAES.egg-info/top_level.txt
+drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:07:48.559723 PyLockAES-1.2.1/pylockaes/
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1491 2023-04-06 11:07:40.000000 PyLockAES-1.2.1/pylockaes/__init__.py
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1491 2023-04-06 11:07:40.000000 PyLockAES-1.2.1/pylockaes/encrypt_decrypt.py
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       38 2023-04-06 11:07:48.559723 PyLockAES-1.2.1/setup.cfg
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      237 2023-04-06 11:07:40.000000 PyLockAES-1.2.1/setup.py
```

### Comparing `PyLockAES-1.2/pylockaes/__init__.py` & `PyLockAES-1.2.1/pylockaes/__init__.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,24 +1,17 @@
 from Crypto.Cipher import AES
 import os
 import string
 import random
 
-
 class AESEncryption:
     def __init__(self, password):
-        self.key = self.generate_key(password)
+        self.key = self.password(len(password))
         self.iv = os.urandom(AES.block_size)
 
-    @staticmethod
-    def generate_key(password):
-        key = password.encode("utf-8")
-        key += b'\0' * (AES.block_size - len(key) % AES.block_size)
-        return key
-
     def encrypt_file(self, input_file, output_file):
         with open(input_file, "rb") as infile:
             with open(output_file, "wb") as outfile:
                 cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
                 outfile.write(self.iv)
                 while True:
                     chunk = infile.read(64 * 1024)
@@ -35,11 +28,11 @@
                 cipher = AES.new(self.key, AES.MODE_CBC, iv)
                 while True:
                     chunk = infile.read(64 * 1024)
                     if len(chunk) == 0:
                         break
                     outfile.write(cipher.decrypt(chunk))
 
+    @staticmethod
     def password(length):
         alphabet = string.ascii_letters + string.digits + string.punctuation
         return ''.join(random.choice(alphabet) for i in range(length))
-
```

### Comparing `PyLockAES-1.2/pylockaes/encrypt_decrypt.py` & `PyLockAES-1.2.1/pylockaes/encrypt_decrypt.py`

 * *Files 12% similar despite different names*

```diff
@@ -1,24 +1,17 @@
 from Crypto.Cipher import AES
 import os
 import string
 import random
 
-
 class AESEncryption:
     def __init__(self, password):
-        self.key = self.generate_key(password)
+        self.key = self.password(len(password))
         self.iv = os.urandom(AES.block_size)
 
-    @staticmethod
-    def generate_key(password):
-        key = password.encode("utf-8")
-        key += b'\0' * (AES.block_size - len(key) % AES.block_size)
-        return key
-
     def encrypt_file(self, input_file, output_file):
         with open(input_file, "rb") as infile:
             with open(output_file, "wb") as outfile:
                 cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
                 outfile.write(self.iv)
                 while True:
                     chunk = infile.read(64 * 1024)
@@ -35,10 +28,11 @@
                 cipher = AES.new(self.key, AES.MODE_CBC, iv)
                 while True:
                     chunk = infile.read(64 * 1024)
                     if len(chunk) == 0:
                         break
                     outfile.write(cipher.decrypt(chunk))
 
+    @staticmethod
     def password(length):
         alphabet = string.ascii_letters + string.digits + string.punctuation
         return ''.join(random.choice(alphabet) for i in range(length))
```

