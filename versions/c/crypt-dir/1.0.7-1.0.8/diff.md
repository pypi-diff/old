# Comparing `tmp/crypt-dir-1.0.7.tar.gz` & `tmp/crypt-dir-1.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "crypt-dir-1.0.7.tar", last modified: Fri Mar 31 14:40:29 2023, max compression
+gzip compressed data, was "crypt-dir-1.0.8.tar", last modified: Fri Mar 31 15:19:03 2023, max compression
```

## Comparing `crypt-dir-1.0.7.tar` & `crypt-dir-1.0.8.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 khanh      (501) staff       (20)        0 2023-03-31 14:40:29.702054 crypt-dir-1.0.7/
--rw-r--r--   0 khanh      (501) staff       (20)     1069 2023-03-31 12:34:48.000000 crypt-dir-1.0.7/LICENSE
--rw-r--r--   0 khanh      (501) staff       (20)     3556 2023-03-31 14:40:29.701897 crypt-dir-1.0.7/PKG-INFO
--rw-r--r--   0 khanh      (501) staff       (20)     3311 2023-03-31 14:19:49.000000 crypt-dir-1.0.7/README.md
-drwxr-xr-x   0 khanh      (501) staff       (20)        0 2023-03-31 14:40:29.700675 crypt-dir-1.0.7/crypt_dir/
--rw-r--r--   0 khanh      (501) staff       (20)       88 2023-03-31 12:34:48.000000 crypt-dir-1.0.7/crypt_dir/__init__.py
--rw-r--r--   0 khanh      (501) staff       (20)     2579 2023-03-31 14:08:30.000000 crypt-dir-1.0.7/crypt_dir/crypt.py
--rw-r--r--   0 khanh      (501) staff       (20)     6017 2023-03-31 14:08:30.000000 crypt-dir-1.0.7/crypt_dir/crypt_dir.py
--rw-r--r--   0 khanh      (501) staff       (20)     3618 2023-03-31 14:38:51.000000 crypt-dir-1.0.7/crypt_dir/crypt_file.py
--rw-r--r--   0 khanh      (501) staff       (20)      552 2023-03-31 14:38:51.000000 crypt-dir-1.0.7/crypt_dir/sig.py
--rw-r--r--   0 khanh      (501) staff       (20)      467 2023-03-31 14:02:04.000000 crypt-dir-1.0.7/crypt_dir/util.py
-drwxr-xr-x   0 khanh      (501) staff       (20)        0 2023-03-31 14:40:29.701683 crypt-dir-1.0.7/crypt_dir.egg-info/
--rw-r--r--   0 khanh      (501) staff       (20)     3556 2023-03-31 14:40:29.000000 crypt-dir-1.0.7/crypt_dir.egg-info/PKG-INFO
--rw-r--r--   0 khanh      (501) staff       (20)      313 2023-03-31 14:40:29.000000 crypt-dir-1.0.7/crypt_dir.egg-info/SOURCES.txt
--rw-r--r--   0 khanh      (501) staff       (20)        1 2023-03-31 14:40:29.000000 crypt-dir-1.0.7/crypt_dir.egg-info/dependency_links.txt
--rw-r--r--   0 khanh      (501) staff       (20)       22 2023-03-31 14:40:29.000000 crypt-dir-1.0.7/crypt_dir.egg-info/requires.txt
--rw-r--r--   0 khanh      (501) staff       (20)       10 2023-03-31 14:40:29.000000 crypt-dir-1.0.7/crypt_dir.egg-info/top_level.txt
--rw-r--r--   0 khanh      (501) staff       (20)       38 2023-03-31 14:40:29.702097 crypt-dir-1.0.7/setup.cfg
--rw-r--r--   0 khanh      (501) staff       (20)      565 2023-03-31 14:38:51.000000 crypt-dir-1.0.7/setup.py
+drwxr-xr-x   0 khanh      (501) staff       (20)        0 2023-03-31 15:19:03.977844 crypt-dir-1.0.8/
+-rw-r--r--   0 khanh      (501) staff       (20)     1069 2023-03-31 12:34:48.000000 crypt-dir-1.0.8/LICENSE
+-rw-r--r--   0 khanh      (501) staff       (20)     3556 2023-03-31 15:19:03.977693 crypt-dir-1.0.8/PKG-INFO
+-rw-r--r--   0 khanh      (501) staff       (20)     3311 2023-03-31 14:19:49.000000 crypt-dir-1.0.8/README.md
+drwxr-xr-x   0 khanh      (501) staff       (20)        0 2023-03-31 15:19:03.976663 crypt-dir-1.0.8/crypt_dir/
+-rw-r--r--   0 khanh      (501) staff       (20)       88 2023-03-31 12:34:48.000000 crypt-dir-1.0.8/crypt_dir/__init__.py
+-rw-r--r--   0 khanh      (501) staff       (20)     2579 2023-03-31 14:08:30.000000 crypt-dir-1.0.8/crypt_dir/crypt.py
+-rw-r--r--   0 khanh      (501) staff       (20)     6017 2023-03-31 14:08:30.000000 crypt-dir-1.0.8/crypt_dir/crypt_dir.py
+-rw-r--r--   0 khanh      (501) staff       (20)     3618 2023-03-31 14:38:51.000000 crypt-dir-1.0.8/crypt_dir/crypt_file.py
+-rw-r--r--   0 khanh      (501) staff       (20)      824 2023-03-31 14:44:06.000000 crypt-dir-1.0.8/crypt_dir/sig.py
+-rw-r--r--   0 khanh      (501) staff       (20)      467 2023-03-31 14:02:04.000000 crypt-dir-1.0.8/crypt_dir/util.py
+drwxr-xr-x   0 khanh      (501) staff       (20)        0 2023-03-31 15:19:03.977522 crypt-dir-1.0.8/crypt_dir.egg-info/
+-rw-r--r--   0 khanh      (501) staff       (20)     3556 2023-03-31 15:19:03.000000 crypt-dir-1.0.8/crypt_dir.egg-info/PKG-INFO
+-rw-r--r--   0 khanh      (501) staff       (20)      313 2023-03-31 15:19:03.000000 crypt-dir-1.0.8/crypt_dir.egg-info/SOURCES.txt
+-rw-r--r--   0 khanh      (501) staff       (20)        1 2023-03-31 15:19:03.000000 crypt-dir-1.0.8/crypt_dir.egg-info/dependency_links.txt
+-rw-r--r--   0 khanh      (501) staff       (20)       20 2023-03-31 15:19:03.000000 crypt-dir-1.0.8/crypt_dir.egg-info/requires.txt
+-rw-r--r--   0 khanh      (501) staff       (20)       10 2023-03-31 15:19:03.000000 crypt-dir-1.0.8/crypt_dir.egg-info/top_level.txt
+-rw-r--r--   0 khanh      (501) staff       (20)       38 2023-03-31 15:19:03.977891 crypt-dir-1.0.8/setup.cfg
+-rw-r--r--   0 khanh      (501) staff       (20)      563 2023-03-31 15:18:33.000000 crypt-dir-1.0.8/setup.py
```

### Comparing `crypt-dir-1.0.7/LICENSE` & `crypt-dir-1.0.8/LICENSE`

 * *Files identical despite different names*

### Comparing `crypt-dir-1.0.7/PKG-INFO` & `crypt-dir-1.0.8/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: crypt-dir
-Version: 1.0.7
+Version: 1.0.8
 Home-page: https://github.com/khanh-nguyen-code/crypt-dir
 Author: Nguyen Ngoc Khanh
 Author-email: khanh.nguyen.contact@gmail.com
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # CRYPT_DIR
```

### Comparing `crypt-dir-1.0.7/README.md` & `crypt-dir-1.0.8/README.md`

 * *Files identical despite different names*

### Comparing `crypt-dir-1.0.7/crypt_dir/crypt.py` & `crypt-dir-1.0.8/crypt_dir/crypt.py`

 * *Files identical despite different names*

### Comparing `crypt-dir-1.0.7/crypt_dir/crypt_dir.py` & `crypt-dir-1.0.8/crypt_dir/crypt_dir.py`

 * *Files identical despite different names*

### Comparing `crypt-dir-1.0.7/crypt_dir/crypt_file.py` & `crypt-dir-1.0.8/crypt_dir/crypt_file.py`

 * *Files identical despite different names*

### Comparing `crypt-dir-1.0.7/crypt_dir/sig.py` & `crypt-dir-1.0.8/crypt_dir/sig.py`

 * *Files 24% similar despite different names*

```diff
@@ -18,7 +18,18 @@
     return uint64_to_bytes(mtime)
 
 
 def set_file_signature(path: str, sig: bytes):
     mtime = bytes_to_uint64(sig)
     atime = mtime
     os.utime(path=path, ns=(atime, mtime))
+
+
+"""
+Alternative implementation of file signature using hash
+
+FILE_SIGNATURE_SIZE = HASH_SIZE
+def get_file_signature(path: str) -> bytes:
+    return sha1_hash(open(path, "rb"))
+def set_file_signature(path: str, sig: bytes):
+    assert sig == get_file_signature(path)
+"""
```

### Comparing `crypt-dir-1.0.7/crypt_dir.egg-info/PKG-INFO` & `crypt-dir-1.0.8/crypt_dir.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: crypt-dir
-Version: 1.0.7
+Version: 1.0.8
 Home-page: https://github.com/khanh-nguyen-code/crypt-dir
 Author: Nguyen Ngoc Khanh
 Author-email: khanh.nguyen.contact@gmail.com
 Description-Content-Type: text/markdown
 License-File: LICENSE
 
 # CRYPT_DIR
```

### Comparing `crypt-dir-1.0.7/setup.py` & `crypt-dir-1.0.8/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 import setuptools
 
 if __name__ == "__main__":
     with open("README.md") as f:
         long_description = f.read()
     setuptools.setup(
         name="crypt-dir",
-        version="1.0.7",
+        version="1.0.8",
         author="Nguyen Ngoc Khanh",
         author_email="khanh.nguyen.contact@gmail.com",
         long_description=long_description,
         long_description_content_type="text/markdown",
         url="https://github.com/khanh-nguyen-code/crypt-dir",
         packages=setuptools.find_packages(),
         install_requires=[
-            "pycryptodomex==3.15.0",
+            "pycryptodomex==3.17",
         ],
     )
```

