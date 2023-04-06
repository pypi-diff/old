# Comparing `tmp/phynder-0.1.0.tar.gz` & `tmp/phynder-0.1.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "phynder-0.1.0.tar", max compression
+gzip compressed data, was "phynder-0.1.1.tar", max compression
```

## Comparing `phynder-0.1.0.tar` & `phynder-0.1.1.tar`

### file list

```diff
@@ -1,8 +1,8 @@
--rw-r--r--   0        0        0        0 2023-04-04 19:35:02.316549 phynder-0.1.0/README.md
--rw-r--r--   0        0        0      255 2023-04-05 21:21:40.627932 phynder-0.1.0/file_finder/cli.py
--rw-r--r--   0        0        0      297 2023-04-05 21:21:40.630478 phynder-0.1.0/file_finder/constants.py
--rw-r--r--   0        0        0      392 2023-03-31 17:12:48.001630 phynder-0.1.0/file_finder/exceptions.py
--rw-r--r--   0        0        0     4996 2023-04-05 21:21:40.633232 phynder-0.1.0/file_finder/finder.py
--rw-r--r--   0        0        0     3740 2023-04-05 21:21:40.635514 phynder-0.1.0/file_finder/utils.py
--rw-r--r--   0        0        0      374 2023-04-05 21:43:47.382122 phynder-0.1.0/pyproject.toml
--rw-r--r--   0        0        0      481 1970-01-01 00:00:00.000000 phynder-0.1.0/PKG-INFO
+-rw-r--r--   0        0        0      144 2023-04-06 20:30:44.811944 phynder-0.1.1/README.md
+-rw-r--r--   0        0        0      255 2023-04-05 21:21:40.627932 phynder-0.1.1/file_finder/cli.py
+-rw-r--r--   0        0        0      297 2023-04-05 21:21:40.630478 phynder-0.1.1/file_finder/constants.py
+-rw-r--r--   0        0        0      392 2023-03-31 17:12:48.001630 phynder-0.1.1/file_finder/exceptions.py
+-rw-r--r--   0        0        0     4996 2023-04-05 21:21:40.633232 phynder-0.1.1/file_finder/finder.py
+-rw-r--r--   0        0        0     3898 2023-04-06 20:32:00.066098 phynder-0.1.1/file_finder/utils.py
+-rw-r--r--   0        0        0      374 2023-04-06 20:30:44.816079 phynder-0.1.1/pyproject.toml
+-rw-r--r--   0        0        0      625 1970-01-01 00:00:00.000000 phynder-0.1.1/PKG-INFO
```

### Comparing `phynder-0.1.0/file_finder/finder.py` & `phynder-0.1.1/file_finder/finder.py`

 * *Files identical despite different names*

### Comparing `phynder-0.1.0/file_finder/utils.py` & `phynder-0.1.1/file_finder/utils.py`

 * *Files 3% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 from datetime import datetime
 from file_finder.exceptions import InvalidInputError
+import platform
 
 def get_folders(path):
     """
     Obtém todos os subdiretorios no diretório pesquisado.
     :param path: Um objeto Path() que representa o diretório
     :return: uma lista de objetos Path() em que cada elemento
     será um diretorio que existe em `path`
@@ -81,15 +82,22 @@
     """
     files_details = []
 
     for file in files:
         stat = file.stat()
         details = [
             file.name,
-            timestamp_to_string(stat.st_birthtime),
+            timestamp_to_string(get_created_timestamp(stat)),
             timestamp_to_string(stat.st_mtime),
             file.absolute()
         ]
 
         files_details.append(details)
 
     return files_details
+
+
+def get_created_timestamp(stat):
+    if platform.system() == "Darwin":
+        return stat.st_birthtime
+
+    return stat.st_ctime
```

