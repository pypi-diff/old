# Comparing `tmp/foundationdb-7.2.4.tar.gz` & `tmp/foundationdb-7.2.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "foundationdb-7.2.4.tar", last modified: Sun Mar 19 20:47:01 2023, max compression
+gzip compressed data, was "foundationdb-7.2.5.tar", last modified: Mon Mar 20 01:00:18 2023, max compression
```

## Comparing `foundationdb-7.2.4.tar` & `foundationdb-7.2.5.tar`

### file list

```diff
@@ -1,15 +1,15 @@
-drwxrwxr-x   0 foundationdb_ci  (1001) foundationdb_ci  (1001)        0 2023-03-19 20:47:01.535300 foundationdb-7.2.4/
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    11665 2023-03-18 01:18:06.233257 foundationdb-7.2.4/LICENSE
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     1427 2023-03-19 20:47:01.535300 foundationdb-7.2.4/PKG-INFO
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)      245 2023-03-18 01:19:59.232848 foundationdb-7.2.4/README.rst
-drwxrwxr-x   0 foundationdb_ci  (1001) foundationdb_ci  (1001)        0 2023-03-19 20:47:01.535300 foundationdb-7.2.4/fdb/
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     4630 2023-03-18 01:19:57.096837 foundationdb-7.2.4/fdb/__init__.py
--rwxrwxr-x   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    25008 2023-03-18 01:19:57.103837 foundationdb-7.2.4/fdb/directory_impl.py
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    35672 2023-03-18 01:19:57.084837 foundationdb-7.2.4/fdb/fdboptions.py
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    62515 2023-03-18 01:19:57.108837 foundationdb-7.2.4/fdb/impl.py
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     2748 2023-03-18 01:19:57.112837 foundationdb-7.2.4/fdb/locality.py
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    30888 2023-03-18 01:19:57.123837 foundationdb-7.2.4/fdb/six.py
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     1915 2023-03-18 01:19:57.116837 foundationdb-7.2.4/fdb/subspace_impl.py
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     5700 2023-03-18 01:19:57.117837 foundationdb-7.2.4/fdb/tenant_management.py
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    20598 2023-03-18 01:19:59.223848 foundationdb-7.2.4/fdb/tuple.py
--rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     1416 2023-03-18 01:18:06.233257 foundationdb-7.2.4/setup.py
+drwxrwxr-x   0 foundationdb_ci  (1001) foundationdb_ci  (1001)        0 2023-03-20 01:00:18.271709 foundationdb-7.2.5/
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    11665 2023-03-19 20:53:18.936177 foundationdb-7.2.5/LICENSE
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     1427 2023-03-20 01:00:18.271709 foundationdb-7.2.5/PKG-INFO
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)      245 2023-03-19 20:55:10.002733 foundationdb-7.2.5/README.rst
+drwxrwxr-x   0 foundationdb_ci  (1001) foundationdb_ci  (1001)        0 2023-03-20 01:00:18.271709 foundationdb-7.2.5/fdb/
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     4630 2023-03-19 20:55:07.785722 foundationdb-7.2.5/fdb/__init__.py
+-rwxrwxr-x   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    25008 2023-03-19 20:55:07.787722 foundationdb-7.2.5/fdb/directory_impl.py
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    35672 2023-03-19 20:55:06.853718 foundationdb-7.2.5/fdb/fdboptions.py
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    62515 2023-03-19 20:55:07.791722 foundationdb-7.2.5/fdb/impl.py
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     2748 2023-03-19 20:55:07.792722 foundationdb-7.2.5/fdb/locality.py
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    30888 2023-03-19 20:55:07.795722 foundationdb-7.2.5/fdb/six.py
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     1915 2023-03-19 20:55:07.798722 foundationdb-7.2.5/fdb/subspace_impl.py
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     5700 2023-03-19 20:55:07.799722 foundationdb-7.2.5/fdb/tenant_management.py
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)    20598 2023-03-19 20:55:09.999733 foundationdb-7.2.5/fdb/tuple.py
+-rw-rw-r--   0 foundationdb_ci  (1001) foundationdb_ci  (1001)     1416 2023-03-19 20:53:18.935177 foundationdb-7.2.5/setup.py
```

### Comparing `foundationdb-7.2.4/LICENSE` & `foundationdb-7.2.5/LICENSE`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/PKG-INFO` & `foundationdb-7.2.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: foundationdb
-Version: 7.2.4
+Version: 7.2.5
 Summary: Python bindings for the FoundationDB database
 Home-page: https://www.foundationdb.org
 Author: FoundationDB
 Author-email: fdb-dist@apple.com
 License: UNKNOWN
 Description: Complete documentation of the FoundationDB Python API can be found at https://apple.github.io/foundationdb/api-python.html.
```

### Comparing `foundationdb-7.2.4/fdb/__init__.py` & `foundationdb-7.2.5/fdb/__init__.py`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/fdb/directory_impl.py` & `foundationdb-7.2.5/fdb/directory_impl.py`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/fdb/fdboptions.py` & `foundationdb-7.2.5/fdb/fdboptions.py`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/fdb/impl.py` & `foundationdb-7.2.5/fdb/impl.py`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/fdb/locality.py` & `foundationdb-7.2.5/fdb/locality.py`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/fdb/six.py` & `foundationdb-7.2.5/fdb/six.py`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/fdb/subspace_impl.py` & `foundationdb-7.2.5/fdb/subspace_impl.py`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/fdb/tenant_management.py` & `foundationdb-7.2.5/fdb/tenant_management.py`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/fdb/tuple.py` & `foundationdb-7.2.5/fdb/tuple.py`

 * *Files identical despite different names*

### Comparing `foundationdb-7.2.4/setup.py` & `foundationdb-7.2.5/setup.py`

 * *Files 7% similar despite different names*

```diff
@@ -3,15 +3,15 @@
 try:
     with open("README.rst") as f:
         long_desc = f.read()
 except:
     long_desc = ""
 
 setup(name="foundationdb",
-      version="7.2.4",
+      version="7.2.5",
       author="FoundationDB",
       author_email="fdb-dist@apple.com",
       description="Python bindings for the FoundationDB database",
       url="https://www.foundationdb.org",
       packages=['fdb'],
       package_data={'fdb': ["fdb/*.py"]},
       long_description=long_desc,
```

