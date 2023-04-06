# Comparing `tmp/bitcode-1.6.0.tar.gz` & `tmp/bitcode-1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bitcode-1.6.0.tar", max compression
+gzip compressed data, was "bitcode-1.7.tar", max compression
```

## Comparing `bitcode-1.6.0.tar` & `bitcode-1.7.tar`

### file list

```diff
@@ -1,5 +1,5 @@
--rw-r--r--   0        0        0      435 2023-04-05 21:04:07.802166 bitcode-1.6.0/README.md
--rw-r--r--   0        0        0       29 2023-04-05 21:04:07.795499 bitcode-1.6.0/bitcode/__init__.py
--rw-r--r--   0        0        0      790 2023-04-05 21:04:07.802166 bitcode-1.6.0/bitcode/console.py
--rw-r--r--   0        0        0      353 2023-04-05 21:04:07.802166 bitcode-1.6.0/pyproject.toml
--rw-r--r--   0        0        0     1153 1970-01-01 00:00:00.000000 bitcode-1.6.0/PKG-INFO
+-rw-r--r--   0        0        0      435 2023-04-06 09:44:07.091846 bitcode-1.7/README.md
+-rw-r--r--   0        0        0       29 2023-04-06 09:44:07.088513 bitcode-1.7/bitcode/__init__.py
+-rw-r--r--   0        0        0      791 2023-04-06 09:44:07.091846 bitcode-1.7/bitcode/console.py
+-rw-r--r--   0        0        0      351 2023-04-06 09:44:07.095179 bitcode-1.7/pyproject.toml
+-rw-r--r--   0        0        0     1151 1970-01-01 00:00:00.000000 bitcode-1.7/PKG-INFO
```

### Comparing `bitcode-1.6.0/bitcode/console.py` & `bitcode-1.7/bitcode/console.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -29,8 +29,8 @@
 		return return_type(input())
 	except:
 		error = TypeError(f"console.prompt: cannot convert user input to {return_type}")
 	if error:
 		raise error
 
 def get_width():
-	return os.get_terminal_size().columns
+	return os.get_terminal_size().columns
```

### Comparing `bitcode-1.6.0/PKG-INFO` & `bitcode-1.7/PKG-INFO`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bitcode
-Version: 1.6.0
+Version: 1.7
 Summary: Bitcode - the ultimate library for everything Python
 Home-page: http://123web.uk/bitpy
 Author: Dylan Rogers
 Author-email: opendylan@proton.me
 Requires-Python: >=3,<4
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.4
```

