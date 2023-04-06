# Comparing `tmp/toolformer-pytorch-0.0.7.tar.gz` & `tmp/toolformer-pytorch-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "toolformer-pytorch-0.0.7.tar", last modified: Thu Apr  6 20:51:07 2023, max compression
+gzip compressed data, was "toolformer-pytorch-0.0.9.tar", last modified: Thu Apr  6 20:57:16 2023, max compression
```

## Comparing `toolformer-pytorch-0.0.7.tar` & `toolformer-pytorch-0.0.9.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:51:07.543386 toolformer-pytorch-0.0.7/
--rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-04-06 20:50:57.000000 toolformer-pytorch-0.0.7/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-06 20:51:07.543386 toolformer-pytorch-0.0.7/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3690 2023-04-06 20:50:57.000000 toolformer-pytorch-0.0.7/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 20:51:07.543386 toolformer-pytorch-0.0.7/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)      868 2023-04-06 20:50:57.000000 toolformer-pytorch-0.0.7/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:51:07.543386 toolformer-pytorch-0.0.7/toolformer_pytorch/
--rw-r--r--   0 runner    (1001) docker     (123)      204 2023-04-06 20:50:57.000000 toolformer-pytorch-0.0.7/toolformer_pytorch/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5592 2023-04-06 20:50:57.000000 toolformer-pytorch-0.0.7/toolformer_pytorch/palm.py
--rw-r--r--   0 runner    (1001) docker     (123)     4529 2023-04-06 20:50:57.000000 toolformer-pytorch-0.0.7/toolformer_pytorch/prompts.py
--rw-r--r--   0 runner    (1001) docker     (123)    14761 2023-04-06 20:50:57.000000 toolformer-pytorch-0.0.7/toolformer_pytorch/toolformer_pytorch.py
--rw-r--r--   0 runner    (1001) docker     (123)     6917 2023-04-06 20:50:57.000000 toolformer-pytorch-0.0.7/toolformer_pytorch/tools.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:51:07.543386 toolformer-pytorch-0.0.7/toolformer_pytorch.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-06 20:51:07.000000 toolformer-pytorch-0.0.7/toolformer_pytorch.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      392 2023-04-06 20:51:07.000000 toolformer-pytorch-0.0.7/toolformer_pytorch.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 20:51:07.000000 toolformer-pytorch-0.0.7/toolformer_pytorch.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-06 20:51:07.000000 toolformer-pytorch-0.0.7/toolformer_pytorch.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 20:51:07.000000 toolformer-pytorch-0.0.7/toolformer_pytorch.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:57:16.986621 toolformer-pytorch-0.0.9/
+-rw-r--r--   0 runner    (1001) docker     (123)     1066 2023-04-06 20:57:05.000000 toolformer-pytorch-0.0.9/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-06 20:57:16.986621 toolformer-pytorch-0.0.9/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3690 2023-04-06 20:57:05.000000 toolformer-pytorch-0.0.9/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-06 20:57:16.986621 toolformer-pytorch-0.0.9/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      868 2023-04-06 20:57:05.000000 toolformer-pytorch-0.0.9/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:57:16.986621 toolformer-pytorch-0.0.9/toolformer_pytorch/
+-rw-r--r--   0 runner    (1001) docker     (123)      204 2023-04-06 20:57:05.000000 toolformer-pytorch-0.0.9/toolformer_pytorch/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5592 2023-04-06 20:57:05.000000 toolformer-pytorch-0.0.9/toolformer_pytorch/palm.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4529 2023-04-06 20:57:05.000000 toolformer-pytorch-0.0.9/toolformer_pytorch/prompts.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14953 2023-04-06 20:57:05.000000 toolformer-pytorch-0.0.9/toolformer_pytorch/toolformer_pytorch.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6917 2023-04-06 20:57:05.000000 toolformer-pytorch-0.0.9/toolformer_pytorch/tools.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 20:57:16.986621 toolformer-pytorch-0.0.9/toolformer_pytorch.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)      639 2023-04-06 20:57:16.000000 toolformer-pytorch-0.0.9/toolformer_pytorch.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      392 2023-04-06 20:57:16.000000 toolformer-pytorch-0.0.9/toolformer_pytorch.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 20:57:16.000000 toolformer-pytorch-0.0.9/toolformer_pytorch.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       37 2023-04-06 20:57:16.000000 toolformer-pytorch-0.0.9/toolformer_pytorch.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-04-06 20:57:16.000000 toolformer-pytorch-0.0.9/toolformer_pytorch.egg-info/top_level.txt
```

### Comparing `toolformer-pytorch-0.0.7/LICENSE` & `toolformer-pytorch-0.0.9/LICENSE`

 * *Files identical despite different names*

### Comparing `toolformer-pytorch-0.0.7/PKG-INFO` & `toolformer-pytorch-0.0.9/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: toolformer-pytorch
-Version: 0.0.7
+Version: 0.0.9
 Summary: Toolformer - Pytorch
 Home-page: https://github.com/lucidrains/toolformer-pytorch
 Author: Phil Wang
 Author-email: lucidrains@gmail.com
 License: MIT
 Keywords: artificial intelligence,deep learning,transformers,attention mechanism,automated-tool-use
 Classifier: Development Status :: 4 - Beta
```

### Comparing `toolformer-pytorch-0.0.7/README.md` & `toolformer-pytorch-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `toolformer-pytorch-0.0.7/setup.py` & `toolformer-pytorch-0.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from setuptools import setup, find_packages
 
 setup(
   name = 'toolformer-pytorch',
   packages = find_packages(exclude=[]),
-  version = '0.0.7',
+  version = '0.0.9',
   license='MIT',
   description = 'Toolformer - Pytorch',
   author = 'Phil Wang',
   author_email = 'lucidrains@gmail.com',
   long_description_content_type = 'text/markdown',
   url = 'https://github.com/lucidrains/toolformer-pytorch',
   keywords = [
```

### Comparing `toolformer-pytorch-0.0.7/toolformer_pytorch/palm.py` & `toolformer-pytorch-0.0.9/toolformer_pytorch/palm.py`

 * *Files identical despite different names*

### Comparing `toolformer-pytorch-0.0.7/toolformer_pytorch/prompts.py` & `toolformer-pytorch-0.0.9/toolformer_pytorch/prompts.py`

 * *Files identical despite different names*

### Comparing `toolformer-pytorch-0.0.7/toolformer_pytorch/toolformer_pytorch.py` & `toolformer-pytorch-0.0.9/toolformer_pytorch/toolformer_pytorch.py`

 * *Files 2% similar despite different names*

```diff
@@ -78,44 +78,50 @@
         return float(s)
 
     return None
 
 @beartype
 def replace_fn(
     registry: dict[str, Callable],
-    m,
+    matches,
     delimiter = '→'
 ):
-    orig_text = m.group(0)
+    orig_text = matches.group(0)
 
-    function_name = m.group(1)
+    function_name = matches.group(1)
 
     # unable to find function in registry
 
     if function_name not in registry:
         return orig_text
 
     fn = registry[function_name]
 
-    params = m.group(2).split(',')
+    params = matches.group(2).split(',')
     params = list(map(lambda s: s.strip(), params))
+    params = list(filter(len, params))
     params = list(map(parse_param, params))
 
     # if any of the parameters are not parseable, return
 
     if any([(not exists(p)) for p in params]):
         return orig_text
 
     # just return original text if there is some error with the function
 
     try:
         out = fn(*params)
     except:
         return orig_text
 
+    # the api calling function can also arrest the process, by returning None
+
+    if not exists(out):
+        return orig_text
+
     # return original text with the output delimiter and the stringified output
 
     return f'{orig_text[:-1]} {delimiter} {str(out)}]'
 
 # main function, which takes a registry of functions, the text in question, and makes all the appropriate api calls and append the output
 
 def invoke_tools(
```

### Comparing `toolformer-pytorch-0.0.7/toolformer_pytorch/tools.py` & `toolformer-pytorch-0.0.9/toolformer_pytorch/tools.py`

 * *Files identical despite different names*

### Comparing `toolformer-pytorch-0.0.7/toolformer_pytorch.egg-info/PKG-INFO` & `toolformer-pytorch-0.0.9/toolformer_pytorch.egg-info/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: toolformer-pytorch
-Version: 0.0.7
+Version: 0.0.9
 Summary: Toolformer - Pytorch
 Home-page: https://github.com/lucidrains/toolformer-pytorch
 Author: Phil Wang
 Author-email: lucidrains@gmail.com
 License: MIT
 Keywords: artificial intelligence,deep learning,transformers,attention mechanism,automated-tool-use
 Classifier: Development Status :: 4 - Beta
```

