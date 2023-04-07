# Comparing `tmp/czthry-0.0.7.tar.gz` & `tmp/czthry-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "czthry-0.0.7.tar", last modified: Tue Sep  6 07:27:14 2022, max compression
+gzip compressed data, was "czthry-0.0.9.tar", last modified: Tue Sep  6 07:31:31 2022, max compression
```

## Comparing `czthry-0.0.7.tar` & `czthry-0.0.9.tar`

### file list

```diff
@@ -1,17 +1,17 @@
-drwxr-xr-x   0 abc        (501) staff       (20)        0 2022-09-06 07:27:14.279928 czthry-0.0.7/
--rw-r--r--   0 abc        (501) staff       (20)     1073 2022-09-06 07:06:07.000000 czthry-0.0.7/LICENSE
--rw-r--r--   0 abc        (501) staff       (20)     1868 2022-09-06 07:27:14.279705 czthry-0.0.7/PKG-INFO
--rw-r--r--   0 abc        (501) staff       (20)      170 2022-09-06 07:06:07.000000 czthry-0.0.7/README.md
--rw-r--r--   0 abc        (501) staff       (20)      572 2022-09-06 07:24:25.000000 czthry-0.0.7/pyproject.toml
--rw-r--r--   0 abc        (501) staff       (20)       38 2022-09-06 07:27:14.280005 czthry-0.0.7/setup.cfg
-drwxr-xr-x   0 abc        (501) staff       (20)        0 2022-09-06 07:27:14.277144 czthry-0.0.7/src/
-drwxr-xr-x   0 abc        (501) staff       (20)        0 2022-09-06 07:27:14.278488 czthry-0.0.7/src/czthry/
--rw-r--r--   0 abc        (501) staff       (20)        0 2022-09-06 07:06:07.000000 czthry-0.0.7/src/czthry/__init__.py
--rw-r--r--   0 abc        (501) staff       (20)     1894 2022-09-06 07:06:07.000000 czthry-0.0.7/src/czthry/alog.py
--rw-r--r--   0 abc        (501) staff       (20)     5375 2022-09-06 07:06:07.000000 czthry-0.0.7/src/czthry/dbmanager.py
--rw-r--r--   0 abc        (501) staff       (20)     7604 2022-09-06 07:24:12.000000 czthry-0.0.7/src/czthry/util.py
-drwxr-xr-x   0 abc        (501) staff       (20)        0 2022-09-06 07:27:14.279385 czthry-0.0.7/src/czthry.egg-info/
--rw-r--r--   0 abc        (501) staff       (20)     1868 2022-09-06 07:27:14.000000 czthry-0.0.7/src/czthry.egg-info/PKG-INFO
--rw-r--r--   0 abc        (501) staff       (20)      253 2022-09-06 07:27:14.000000 czthry-0.0.7/src/czthry.egg-info/SOURCES.txt
--rw-r--r--   0 abc        (501) staff       (20)        1 2022-09-06 07:27:14.000000 czthry-0.0.7/src/czthry.egg-info/dependency_links.txt
--rw-r--r--   0 abc        (501) staff       (20)        7 2022-09-06 07:27:14.000000 czthry-0.0.7/src/czthry.egg-info/top_level.txt
+drwxr-xr-x   0 abc        (501) staff       (20)        0 2022-09-06 07:31:31.780522 czthry-0.0.9/
+-rw-r--r--   0 abc        (501) staff       (20)     1073 2022-09-06 07:06:07.000000 czthry-0.0.9/LICENSE
+-rw-r--r--   0 abc        (501) staff       (20)     1868 2022-09-06 07:31:31.780305 czthry-0.0.9/PKG-INFO
+-rw-r--r--   0 abc        (501) staff       (20)      170 2022-09-06 07:06:07.000000 czthry-0.0.9/README.md
+-rw-r--r--   0 abc        (501) staff       (20)      572 2022-09-06 07:31:04.000000 czthry-0.0.9/pyproject.toml
+-rw-r--r--   0 abc        (501) staff       (20)       38 2022-09-06 07:31:31.780590 czthry-0.0.9/setup.cfg
+drwxr-xr-x   0 abc        (501) staff       (20)        0 2022-09-06 07:31:31.776919 czthry-0.0.9/src/
+drwxr-xr-x   0 abc        (501) staff       (20)        0 2022-09-06 07:31:31.778859 czthry-0.0.9/src/czthry/
+-rw-r--r--   0 abc        (501) staff       (20)        0 2022-09-06 07:06:07.000000 czthry-0.0.9/src/czthry/__init__.py
+-rw-r--r--   0 abc        (501) staff       (20)     1894 2022-09-06 07:06:07.000000 czthry-0.0.9/src/czthry/alog.py
+-rw-r--r--   0 abc        (501) staff       (20)     5375 2022-09-06 07:06:07.000000 czthry-0.0.9/src/czthry/dbmanager.py
+-rw-r--r--   0 abc        (501) staff       (20)     7596 2022-09-06 07:28:53.000000 czthry-0.0.9/src/czthry/util.py
+drwxr-xr-x   0 abc        (501) staff       (20)        0 2022-09-06 07:31:31.780007 czthry-0.0.9/src/czthry.egg-info/
+-rw-r--r--   0 abc        (501) staff       (20)     1868 2022-09-06 07:31:31.000000 czthry-0.0.9/src/czthry.egg-info/PKG-INFO
+-rw-r--r--   0 abc        (501) staff       (20)      253 2022-09-06 07:31:31.000000 czthry-0.0.9/src/czthry.egg-info/SOURCES.txt
+-rw-r--r--   0 abc        (501) staff       (20)        1 2022-09-06 07:31:31.000000 czthry-0.0.9/src/czthry.egg-info/dependency_links.txt
+-rw-r--r--   0 abc        (501) staff       (20)        7 2022-09-06 07:31:31.000000 czthry-0.0.9/src/czthry.egg-info/top_level.txt
```

### Comparing `czthry-0.0.7/LICENSE` & `czthry-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `czthry-0.0.7/PKG-INFO` & `czthry-0.0.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: czthry
-Version: 0.0.7
+Version: 0.0.9
 Summary: A small example package
 Author-email: thr <22227124@qq.com>
 License: Copyright (c) 2018 The Python Packaging Authority
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
         of this software and associated documentation files (the "Software"), to deal
         in the Software without restriction, including without limitation the rights
```

### Comparing `czthry-0.0.7/pyproject.toml` & `czthry-0.0.9/pyproject.toml`

 * *Files 19% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools>=61.0"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "czthry"
-version = "0.0.7"
+version = "0.0.9"
 authors = [
   { name="thr", email="22227124@qq.com" },
 ]
 description = "A small example package"
 readme = "README.md"
 license = { file="LICENSE" }
 requires-python = ">=3.7"
```

### Comparing `czthry-0.0.7/src/czthry/alog.py` & `czthry-0.0.9/src/czthry/alog.py`

 * *Files identical despite different names*

### Comparing `czthry-0.0.7/src/czthry/dbmanager.py` & `czthry-0.0.9/src/czthry/dbmanager.py`

 * *Files identical despite different names*

### Comparing `czthry-0.0.7/src/czthry/util.py` & `czthry-0.0.9/src/czthry/util.py`

 * *Files 0% similar despite different names*

```diff
@@ -19,17 +19,17 @@
     return fmt.format(date)
 
 
 def reg_find(exp, text):
     result = re.search(exp, text)
     if not result:
         return None
-    ret = list(result.groups())
+    ret = result.groups()
     if not ret:
-        ret = [result.group()]
+        ret = result.group()
     return ret
 
 
 def excludeFiles(files, exc=None):
     if exc is None:
         exc = ['.DS_Store', '__pycache__']
     arr = []
```

### Comparing `czthry-0.0.7/src/czthry.egg-info/PKG-INFO` & `czthry-0.0.9/src/czthry.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: czthry
-Version: 0.0.7
+Version: 0.0.9
 Summary: A small example package
 Author-email: thr <22227124@qq.com>
 License: Copyright (c) 2018 The Python Packaging Authority
         
         Permission is hereby granted, free of charge, to any person obtaining a copy
         of this software and associated documentation files (the "Software"), to deal
         in the Software without restriction, including without limitation the rights
```

