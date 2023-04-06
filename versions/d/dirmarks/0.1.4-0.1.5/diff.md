# Comparing `tmp/dirmarks-0.1.4.tar.gz` & `tmp/dirmarks-0.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dirmarks-0.1.4.tar", max compression
+gzip compressed data, was "dirmarks-0.1.5.tar", max compression
```

## Comparing `dirmarks-0.1.4.tar` & `dirmarks-0.1.5.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     1070 2023-04-06 16:22:22.890575 dirmarks-0.1.4/LICENSE
--rw-r--r--   0        0        0     2419 2023-04-06 16:27:00.205868 dirmarks-0.1.4/README.md
--rw-r--r--   0        0        0       88 2023-04-06 16:22:22.895649 dirmarks-0.1.4/dirmarks/__init__.py
--rw-r--r--   0        0        0      671 2023-04-06 17:18:28.779427 dirmarks-0.1.4/dirmarks/data/dirmarks.function
--rwxr-xr-x   0        0        0     4926 2023-04-06 17:23:30.564651 dirmarks-0.1.4/dirmarks/main.py
--rw-r--r--   0        0        0      364 2023-04-06 17:23:43.419897 dirmarks-0.1.4/pyproject.toml
--rw-r--r--   0        0        0     2895 1970-01-01 00:00:00.000000 dirmarks-0.1.4/PKG-INFO
+-rw-r--r--   0        0        0     1070 2023-04-06 16:22:22.890575 dirmarks-0.1.5/LICENSE
+-rw-r--r--   0        0        0     2419 2023-04-06 16:27:00.205868 dirmarks-0.1.5/README.md
+-rw-r--r--   0        0        0       88 2023-04-06 16:22:22.895649 dirmarks-0.1.5/dirmarks/__init__.py
+-rw-r--r--   0        0        0      671 2023-04-06 17:18:28.779427 dirmarks-0.1.5/dirmarks/data/dirmarks.function
+-rwxr-xr-x   0        0        0     4960 2023-04-06 17:26:03.567768 dirmarks-0.1.5/dirmarks/main.py
+-rw-r--r--   0        0        0      364 2023-04-06 17:27:28.814353 dirmarks-0.1.5/pyproject.toml
+-rw-r--r--   0        0        0     2895 1970-01-01 00:00:00.000000 dirmarks-0.1.5/PKG-INFO
```

### Comparing `dirmarks-0.1.4/LICENSE` & `dirmarks-0.1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `dirmarks-0.1.4/README.md` & `dirmarks-0.1.5/README.md`

 * *Files identical despite different names*

### Comparing `dirmarks-0.1.4/dirmarks/data/dirmarks.function` & `dirmarks-0.1.5/dirmarks/data/dirmarks.function`

 * *Files identical despite different names*

### Comparing `dirmarks-0.1.4/dirmarks/main.py` & `dirmarks-0.1.5/dirmarks/main.py`

 * *Files 0% similar despite different names*

```diff
@@ -115,15 +115,16 @@
 dir -d <name>|[0-9]+ ------ delete mark
 dir -u <name> <path> ------ update mark
 dir -m <name> ------------- add mark for PWD
 dir -p <name> ------------- prints mark
 """)
     elif command == "--shell":
         with open(os.path.join(f"{DATA_PATH}","dirmarks.function"), "r") as fb:
-            print(fb.readlines())
+            for line in fb.readlines():
+                print(line)
     elif command == "--mark":
         shortname, path = sys.argv[2], os.path.abspath(".")
         Marks().add_mark(shortname, path)
     elif command == "--add":
         shortname, path = sys.argv[2], sys.argv[3]
         Marks().add_mark(shortname, path)
     elif command == "--delete":
```

### Comparing `dirmarks-0.1.4/PKG-INFO` & `dirmarks-0.1.5/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dirmarks
-Version: 0.1.4
+Version: 0.1.5
 Summary: Bookmarks for the filesystem
 License: MIT
 Author: Meir Michanie
 Author-email: meirm@riunx.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

