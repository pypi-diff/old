# Comparing `tmp/binarystream-0.1.0.tar.gz` & `tmp/binarystream-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "binarystream-0.1.0.tar", max compression
+gzip compressed data, was "binarystream-0.1.2.tar", max compression
```

## Comparing `binarystream-0.1.0.tar` & `binarystream-0.1.2.tar`

### file list

```diff
@@ -1,6 +1,6 @@
--rw-r--r--   0        0        0     2655 2023-04-06 14:45:47.729526 binarystream-0.1.0/BinaryStream/BinaryStream.py
--rw-r--r--   0        0        0       61 2023-04-06 14:47:33.313526 binarystream-0.1.0/BinaryStream/__init__.py
--rw-r--r--   0        0        0    10280 2023-04-06 18:49:50.820496 binarystream-0.1.0/LICENSE
--rw-r--r--   0        0        0       16 2023-04-06 18:49:50.900496 binarystream-0.1.0/README.md
--rw-r--r--   0        0        0      377 2023-04-06 19:05:36.548496 binarystream-0.1.0/pyproject.toml
--rw-r--r--   0        0        0      615 1970-01-01 00:00:00.000000 binarystream-0.1.0/PKG-INFO
+-rw-r--r--   0        0        0     2351 2023-04-06 22:56:03.020397 binarystream-0.1.2/BinaryStream/BinaryStream.py
+-rw-r--r--   0        0        0       61 2023-04-06 22:26:34.600397 binarystream-0.1.2/BinaryStream/__init__.py
+-rw-r--r--   0        0        0    10280 2023-04-06 18:49:50.820496 binarystream-0.1.2/LICENSE
+-rw-r--r--   0        0        0       16 2023-04-06 18:49:50.900496 binarystream-0.1.2/README.md
+-rw-r--r--   0        0        0      377 2023-04-06 22:56:03.036397 binarystream-0.1.2/pyproject.toml
+-rw-r--r--   0        0        0      615 1970-01-01 00:00:00.000000 binarystream-0.1.2/PKG-INFO
```

### Comparing `binarystream-0.1.0/LICENSE` & `binarystream-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `binarystream-0.1.0/PKG-INFO` & `binarystream-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: binarystream
-Version: 0.1.0
+Version: 0.1.2
 Summary: BinaryStream libary for python (support only big-endian stream)
 License: Apache-2.0
 Author: TheMade4
 Requires-Python: >=3.7,<4.0
 Classifier: License :: OSI Approved :: Apache Software License
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.7
```

