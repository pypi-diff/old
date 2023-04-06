# Comparing `tmp/dirmarks-0.1.3.tar.gz` & `tmp/dirmarks-0.1.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dirmarks-0.1.3.tar", max compression
+gzip compressed data, was "dirmarks-0.1.4.tar", max compression
```

## Comparing `dirmarks-0.1.3.tar` & `dirmarks-0.1.4.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     1070 2023-04-06 16:22:22.890575 dirmarks-0.1.3/LICENSE
--rw-r--r--   0        0        0     2419 2023-04-06 16:27:00.205868 dirmarks-0.1.3/README.md
--rw-r--r--   0        0        0       88 2023-04-06 16:22:22.895649 dirmarks-0.1.3/dirmarks/__init__.py
--rw-r--r--   0        0        0      671 2023-04-06 17:18:28.779427 dirmarks-0.1.3/dirmarks/data/dirmarks.function
--rwxr-xr-x   0        0        0     4921 2023-04-06 16:22:22.896269 dirmarks-0.1.3/dirmarks/main.py
--rw-r--r--   0        0        0      364 2023-04-06 17:18:46.786468 dirmarks-0.1.3/pyproject.toml
--rw-r--r--   0        0        0     2895 1970-01-01 00:00:00.000000 dirmarks-0.1.3/PKG-INFO
+-rw-r--r--   0        0        0     1070 2023-04-06 16:22:22.890575 dirmarks-0.1.4/LICENSE
+-rw-r--r--   0        0        0     2419 2023-04-06 16:27:00.205868 dirmarks-0.1.4/README.md
+-rw-r--r--   0        0        0       88 2023-04-06 16:22:22.895649 dirmarks-0.1.4/dirmarks/__init__.py
+-rw-r--r--   0        0        0      671 2023-04-06 17:18:28.779427 dirmarks-0.1.4/dirmarks/data/dirmarks.function
+-rwxr-xr-x   0        0        0     4926 2023-04-06 17:23:30.564651 dirmarks-0.1.4/dirmarks/main.py
+-rw-r--r--   0        0        0      364 2023-04-06 17:23:43.419897 dirmarks-0.1.4/pyproject.toml
+-rw-r--r--   0        0        0     2895 1970-01-01 00:00:00.000000 dirmarks-0.1.4/PKG-INFO
```

### Comparing `dirmarks-0.1.3/LICENSE` & `dirmarks-0.1.4/LICENSE`

 * *Files identical despite different names*

### Comparing `dirmarks-0.1.3/README.md` & `dirmarks-0.1.4/README.md`

 * *Files identical despite different names*

### Comparing `dirmarks-0.1.3/dirmarks/data/dirmarks.function` & `dirmarks-0.1.4/dirmarks/data/dirmarks.function`

 * *Files identical despite different names*

### Comparing `dirmarks-0.1.3/dirmarks/main.py` & `dirmarks-0.1.4/dirmarks/main.py`

 * *Files 0% similar despite different names*

```diff
@@ -114,15 +114,15 @@
 dir -a <name> <path> ------ add new mark
 dir -d <name>|[0-9]+ ------ delete mark
 dir -u <name> <path> ------ update mark
 dir -m <name> ------------- add mark for PWD
 dir -p <name> ------------- prints mark
 """)
     elif command == "--shell":
-        with open(os.join(f"{DATA_PATH}","dirmarks.function"), "r") as fb:
+        with open(os.path.join(f"{DATA_PATH}","dirmarks.function"), "r") as fb:
             print(fb.readlines())
     elif command == "--mark":
         shortname, path = sys.argv[2], os.path.abspath(".")
         Marks().add_mark(shortname, path)
     elif command == "--add":
         shortname, path = sys.argv[2], sys.argv[3]
         Marks().add_mark(shortname, path)
```

### Comparing `dirmarks-0.1.3/PKG-INFO` & `dirmarks-0.1.4/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dirmarks
-Version: 0.1.3
+Version: 0.1.4
 Summary: Bookmarks for the filesystem
 License: MIT
 Author: Meir Michanie
 Author-email: meirm@riunx.com
 Requires-Python: >=3.9,<4.0
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Programming Language :: Python :: 3
```

