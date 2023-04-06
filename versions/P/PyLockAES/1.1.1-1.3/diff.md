# Comparing `tmp/PyLockAES-1.1.1.tar.gz` & `tmp/PyLockAES-1.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "PyLockAES-1.1.1.tar", last modified: Sun Apr  2 16:11:59 2023, max compression
+gzip compressed data, was "PyLockAES-1.3.tar", last modified: Thu Apr  6 11:43:44 2023, max compression
```

## Comparing `PyLockAES-1.1.1.tar` & `PyLockAES-1.3.tar`

### file list

```diff
@@ -1,12 +1,12 @@
-drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-02 16:11:59.638204 PyLockAES-1.1.1/
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      160 2023-04-02 16:11:59.638204 PyLockAES-1.1.1/PKG-INFO
-drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-02 16:11:59.638204 PyLockAES-1.1.1/PyLockAES.egg-info/
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      160 2023-04-02 16:11:59.000000 PyLockAES-1.1.1/PyLockAES.egg-info/PKG-INFO
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      191 2023-04-02 16:11:59.000000 PyLockAES-1.1.1/PyLockAES.egg-info/SOURCES.txt
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)        1 2023-04-02 16:11:59.000000 PyLockAES-1.1.1/PyLockAES.egg-info/dependency_links.txt
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       10 2023-04-02 16:11:59.000000 PyLockAES-1.1.1/PyLockAES.egg-info/top_level.txt
-drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-02 16:11:59.638204 PyLockAES-1.1.1/pylockaes/
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1423 2023-04-02 16:08:50.000000 PyLockAES-1.1.1/pylockaes/__init__.py
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1447 2023-04-02 16:10:27.000000 PyLockAES-1.1.1/pylockaes/encrypt_decrypt.py
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       38 2023-04-02 16:11:59.638204 PyLockAES-1.1.1/setup.cfg
--rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      237 2023-04-02 16:11:56.000000 PyLockAES-1.1.1/setup.py
+drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:43:44.534780 PyLockAES-1.3/
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      158 2023-04-06 11:43:44.534780 PyLockAES-1.3/PKG-INFO
+drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:43:44.534780 PyLockAES-1.3/PyLockAES.egg-info/
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      158 2023-04-06 11:43:44.000000 PyLockAES-1.3/PyLockAES.egg-info/PKG-INFO
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      191 2023-04-06 11:43:44.000000 PyLockAES-1.3/PyLockAES.egg-info/SOURCES.txt
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)        1 2023-04-06 11:43:44.000000 PyLockAES-1.3/PyLockAES.egg-info/dependency_links.txt
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       10 2023-04-06 11:43:44.000000 PyLockAES-1.3/PyLockAES.egg-info/top_level.txt
+drwxrwxr-x   0 leonardo  (1000) leonardo  (1000)        0 2023-04-06 11:43:44.534780 PyLockAES-1.3/pylockaes/
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1423 2023-04-06 11:38:33.000000 PyLockAES-1.3/pylockaes/__init__.py
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)     1446 2023-04-06 11:38:55.000000 PyLockAES-1.3/pylockaes/encrypt_decrypt.py
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)       38 2023-04-06 11:43:44.534780 PyLockAES-1.3/setup.cfg
+-rw-rw-r--   0 leonardo  (1000) leonardo  (1000)      235 2023-04-06 11:43:41.000000 PyLockAES-1.3/setup.py
```

### Comparing `PyLockAES-1.1.1/pylockaes/__init__.py` & `PyLockAES-1.3/pylockaes/__init__.py`

 * *Files identical despite different names*

### Comparing `PyLockAES-1.1.1/pylockaes/encrypt_decrypt.py` & `PyLockAES-1.3/pylockaes/encrypt_decrypt.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -31,8 +31,8 @@
             with open(output_file, "wb") as outfile:
                 iv = infile.read(AES.block_size)
                 cipher = AES.new(self.key, AES.MODE_CBC, iv)
                 while True:
                     chunk = infile.read(64 * 1024)
                     if len(chunk) == 0:
                         break
-                    outfile.write(cipher.decrypt(chunk))
+                    outfile.write(cipher.decrypt(chunk))
```

