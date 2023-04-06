# Comparing `tmp/gladier-tools-0.4.2.tar.gz` & `tmp/gladier-tools-0.4.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gladier-tools-0.4.2.tar", last modified: Mon Mar  6 23:10:56 2023, max compression
+gzip compressed data, was "gladier-tools-0.4.3.tar", last modified: Thu Apr  6 18:58:48 2023, max compression
```

## Comparing `gladier-tools-0.4.2.tar` & `gladier-tools-0.4.3.tar`

### file list

```diff
@@ -1,47 +1,49 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:56.436726 gladier-tools-0.4.2/
--rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       60 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1962 2023-03-06 23:10:56.436726 gladier-tools-0.4.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1189 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/README.rst
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:56.432726 gladier-tools-0.4.2/gladier_tools/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:56.432726 gladier-tools-0.4.2/gladier_tools/globus/
--rw-r--r--   0 runner    (1001) docker     (123)       55 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/globus/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2682 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/globus/transfer.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:56.436726 gladier-tools-0.4.2/gladier_tools/posix/
--rw-r--r--   0 runner    (1001) docker     (123)      441 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/posix/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     2656 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/posix/asymmetric_decrypt.py
--rw-r--r--   0 runner    (1001) docker     (123)     2055 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/posix/asymmetric_encrypt.py
--rw-r--r--   0 runner    (1001) docker     (123)     2457 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/posix/decrypt.py
--rw-r--r--   0 runner    (1001) docker     (123)     2141 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/posix/encrypt.py
--rw-r--r--   0 runner    (1001) docker     (123)     1312 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/posix/https_download_file.py
--rw-r--r--   0 runner    (1001) docker     (123)     4780 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/posix/shell_cmd.py
--rw-r--r--   0 runner    (1001) docker     (123)     1346 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/posix/tar.py
--rw-r--r--   0 runner    (1001) docker     (123)     2088 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/posix/untar.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:56.436726 gladier-tools-0.4.2/gladier_tools/publish/
--rw-r--r--   0 runner    (1001) docker     (123)       52 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/publish/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7224 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/publish/publish.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:56.436726 gladier-tools-0.4.2/gladier_tools/tests/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:56.436726 gladier-tools-0.4.2/gladier_tools/tests/posix/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/posix/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)      510 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/posix/conftest.py
--rw-r--r--   0 runner    (1001) docker     (123)     1975 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/posix/test_decrypt.py
--rw-r--r--   0 runner    (1001) docker     (123)     1802 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/posix/test_encrypt.py
--rw-r--r--   0 runner    (1001) docker     (123)      738 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/posix/test_gladier_tools.py
--rw-r--r--   0 runner    (1001) docker     (123)     3134 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/posix/test_shell_cmd.py
--rw-r--r--   0 runner    (1001) docker     (123)      926 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/posix/test_tar.py
--rw-r--r--   0 runner    (1001) docker     (123)     1015 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/posix/test_untar.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:56.436726 gladier-tools-0.4.2/gladier_tools/tests/publish/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/publish/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     1703 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/tests/publish/test_publish.py
--rw-r--r--   0 runner    (1001) docker     (123)       22 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/gladier_tools/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-06 23:10:56.432726 gladier-tools-0.4.2/gladier_tools.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1962 2023-03-06 23:10:56.000000 gladier-tools-0.4.2/gladier_tools.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     1190 2023-03-06 23:10:56.000000 gladier-tools-0.4.2/gladier_tools.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-06 23:10:56.000000 gladier-tools-0.4.2/gladier_tools.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-06 23:10:56.000000 gladier-tools-0.4.2/gladier_tools.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       14 2023-03-06 23:10:56.000000 gladier-tools-0.4.2/gladier_tools.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)       15 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (123)       88 2023-03-06 23:10:56.436726 gladier-tools-0.4.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-03-06 23:10:47.000000 gladier-tools-0.4.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:48.862953 gladier-tools-0.4.3/
+-rw-r--r--   0 runner    (1001) docker     (123)     1071 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       60 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1962 2023-04-06 18:58:48.862953 gladier-tools-0.4.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1189 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/README.rst
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:48.858952 gladier-tools-0.4.3/gladier_tools/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:48.858952 gladier-tools-0.4.3/gladier_tools/globus/
+-rw-r--r--   0 runner    (1001) docker     (123)       55 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/globus/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2682 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/globus/transfer.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:48.858952 gladier-tools-0.4.3/gladier_tools/posix/
+-rw-r--r--   0 runner    (1001) docker     (123)      441 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/posix/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2656 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/posix/asymmetric_decrypt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2055 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/posix/asymmetric_encrypt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2457 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/posix/decrypt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2141 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/posix/encrypt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1312 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/posix/https_download_file.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4780 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/posix/shell_cmd.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1346 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/posix/tar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     2088 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/posix/untar.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:48.858952 gladier-tools-0.4.3/gladier_tools/publish/
+-rw-r--r--   0 runner    (1001) docker     (123)       98 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/publish/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7224 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/publish/publish.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17420 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/publish/publishv2.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:48.862953 gladier-tools-0.4.3/gladier_tools/tests/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:48.862953 gladier-tools-0.4.3/gladier_tools/tests/posix/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/posix/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)      510 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/posix/conftest.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1975 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/posix/test_decrypt.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1802 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/posix/test_encrypt.py
+-rw-r--r--   0 runner    (1001) docker     (123)      738 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/posix/test_gladier_tools.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3134 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/posix/test_shell_cmd.py
+-rw-r--r--   0 runner    (1001) docker     (123)      926 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/posix/test_tar.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1015 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/posix/test_untar.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:48.862953 gladier-tools-0.4.3/gladier_tools/tests/publish/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/publish/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1703 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/publish/test_publish.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9718 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/tests/publish/test_publishv2.py
+-rw-r--r--   0 runner    (1001) docker     (123)       22 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/gladier_tools/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 18:58:48.858952 gladier-tools-0.4.3/gladier_tools.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1962 2023-04-06 18:58:48.000000 gladier-tools-0.4.3/gladier_tools.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1271 2023-04-06 18:58:48.000000 gladier-tools-0.4.3/gladier_tools.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 18:58:48.000000 gladier-tools-0.4.3/gladier_tools.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 18:58:48.000000 gladier-tools-0.4.3/gladier_tools.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       14 2023-04-06 18:58:48.000000 gladier-tools-0.4.3/gladier_tools.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       15 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       88 2023-04-06 18:58:48.862953 gladier-tools-0.4.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1448 2023-04-06 18:58:36.000000 gladier-tools-0.4.3/setup.py
```

### Comparing `gladier-tools-0.4.2/LICENSE` & `gladier-tools-0.4.3/LICENSE`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/PKG-INFO` & `gladier-tools-0.4.3/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gladier-tools
-Version: 0.4.2
+Version: 0.4.3
 Summary: A set of reusable Gladier Tools
 Home-page: https://github.com/globus-gladier/gladier-tools
 Maintainer: The Gladier Team
 Maintainer-email: 
 License: Apache 2.0
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
```

### Comparing `gladier-tools-0.4.2/README.rst` & `gladier-tools-0.4.3/README.rst`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/globus/transfer.py` & `gladier-tools-0.4.3/gladier_tools/globus/transfer.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/posix/asymmetric_decrypt.py` & `gladier-tools-0.4.3/gladier_tools/posix/asymmetric_decrypt.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/posix/asymmetric_encrypt.py` & `gladier-tools-0.4.3/gladier_tools/posix/asymmetric_encrypt.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/posix/decrypt.py` & `gladier-tools-0.4.3/gladier_tools/posix/decrypt.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/posix/encrypt.py` & `gladier-tools-0.4.3/gladier_tools/posix/encrypt.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/posix/https_download_file.py` & `gladier-tools-0.4.3/gladier_tools/posix/https_download_file.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/posix/shell_cmd.py` & `gladier-tools-0.4.3/gladier_tools/posix/shell_cmd.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/posix/tar.py` & `gladier-tools-0.4.3/gladier_tools/posix/tar.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/posix/untar.py` & `gladier-tools-0.4.3/gladier_tools/posix/untar.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/publish/publish.py` & `gladier-tools-0.4.3/gladier_tools/publish/publish.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/tests/posix/test_decrypt.py` & `gladier-tools-0.4.3/gladier_tools/tests/posix/test_decrypt.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/tests/posix/test_encrypt.py` & `gladier-tools-0.4.3/gladier_tools/tests/posix/test_encrypt.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/tests/posix/test_gladier_tools.py` & `gladier-tools-0.4.3/gladier_tools/tests/posix/test_gladier_tools.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/tests/posix/test_shell_cmd.py` & `gladier-tools-0.4.3/gladier_tools/tests/posix/test_shell_cmd.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/tests/posix/test_tar.py` & `gladier-tools-0.4.3/gladier_tools/tests/posix/test_tar.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/tests/posix/test_untar.py` & `gladier-tools-0.4.3/gladier_tools/tests/posix/test_untar.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools/tests/publish/test_publish.py` & `gladier-tools-0.4.3/gladier_tools/tests/publish/test_publish.py`

 * *Files identical despite different names*

### Comparing `gladier-tools-0.4.2/gladier_tools.egg-info/PKG-INFO` & `gladier-tools-0.4.3/gladier_tools.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gladier-tools
-Version: 0.4.2
+Version: 0.4.3
 Summary: A set of reusable Gladier Tools
 Home-page: https://github.com/globus-gladier/gladier-tools
 Maintainer: The Gladier Team
 Maintainer-email: 
 License: Apache 2.0
 Classifier: Intended Audience :: Science/Research
 Classifier: Intended Audience :: Developers
```

### Comparing `gladier-tools-0.4.2/gladier_tools.egg-info/SOURCES.txt` & `gladier-tools-0.4.3/gladier_tools.egg-info/SOURCES.txt`

 * *Files 10% similar despite different names*

```diff
@@ -20,18 +20,20 @@
 gladier_tools/posix/encrypt.py
 gladier_tools/posix/https_download_file.py
 gladier_tools/posix/shell_cmd.py
 gladier_tools/posix/tar.py
 gladier_tools/posix/untar.py
 gladier_tools/publish/__init__.py
 gladier_tools/publish/publish.py
+gladier_tools/publish/publishv2.py
 gladier_tools/tests/__init__.py
 gladier_tools/tests/posix/__init__.py
 gladier_tools/tests/posix/conftest.py
 gladier_tools/tests/posix/test_decrypt.py
 gladier_tools/tests/posix/test_encrypt.py
 gladier_tools/tests/posix/test_gladier_tools.py
 gladier_tools/tests/posix/test_shell_cmd.py
 gladier_tools/tests/posix/test_tar.py
 gladier_tools/tests/posix/test_untar.py
 gladier_tools/tests/publish/__init__.py
-gladier_tools/tests/publish/test_publish.py
+gladier_tools/tests/publish/test_publish.py
+gladier_tools/tests/publish/test_publishv2.py
```

### Comparing `gladier-tools-0.4.2/setup.py` & `gladier-tools-0.4.3/setup.py`

 * *Files identical despite different names*

