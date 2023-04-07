# Comparing `tmp/recon_lw-2.0.0.dev4638480940.tar.gz` & `tmp/recon_lw-2.0.0.dev4638710878.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/recon_lw-2.0.0.dev4638480940.tar", last modified: Fri Apr  7 13:19:54 2023, max compression
+gzip compressed data, was "dist/recon_lw-2.0.0.dev4638710878.tar", last modified: Fri Apr  7 13:57:26 2023, max compression
```

## Comparing `recon_lw-2.0.0.dev4638480940.tar` & `recon_lw-2.0.0.dev4638710878.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/
--rw-r--r--   0 runner    (1001) docker     (122)       69 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)       10 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/README.md
--rw-r--r--   0 runner    (1001) docker     (122)       76 2023-04-07 13:19:39.000000 recon_lw-2.0.0.dev4638480940/package_info.json
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw/
--rw-r--r--   0 runner    (1001) docker     (122)        5 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/recon_lw/__init__.py
--rw-r--r--   0 runner    (1001) docker     (122)    12849 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/recon_lw/recon_lw.py
--rw-r--r--   0 runner    (1001) docker     (122)    12122 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/recon_lw/recon_ob.py
-drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/
--rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (122)      287 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (122)      219 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/recon_lw.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (122)      275 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-07 13:19:54.000000 recon_lw-2.0.0.dev4638480940/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (122)     1582 2023-04-07 13:19:31.000000 recon_lw-2.0.0.dev4638480940/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/
+-rw-r--r--   0 runner    (1001) docker     (122)       69 2023-04-07 13:57:07.000000 recon_lw-2.0.0.dev4638710878/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)       10 2023-04-07 13:57:07.000000 recon_lw-2.0.0.dev4638710878/README.md
+-rw-r--r--   0 runner    (1001) docker     (122)       76 2023-04-07 13:57:14.000000 recon_lw-2.0.0.dev4638710878/package_info.json
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/recon_lw/
+-rw-r--r--   0 runner    (1001) docker     (122)        5 2023-04-07 13:57:07.000000 recon_lw-2.0.0.dev4638710878/recon_lw/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12849 2023-04-07 13:57:07.000000 recon_lw-2.0.0.dev4638710878/recon_lw/recon_lw.py
+-rw-r--r--   0 runner    (1001) docker     (122)    12172 2023-04-07 13:57:07.000000 recon_lw-2.0.0.dev4638710878/recon_lw/recon_ob.py
+drwxr-xr-x   0 runner    (1001) docker     (122)        0 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/recon_lw.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (122)      294 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/recon_lw.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (122)      287 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/recon_lw.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        1 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/recon_lw.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      219 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/recon_lw.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (122)        9 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/recon_lw.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (122)      275 2023-04-07 13:57:07.000000 recon_lw-2.0.0.dev4638710878/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (122)       38 2023-04-07 13:57:26.000000 recon_lw-2.0.0.dev4638710878/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (122)     1582 2023-04-07 13:57:07.000000 recon_lw-2.0.0.dev4638710878/setup.py
```

### Comparing `recon_lw-2.0.0.dev4638480940/recon_lw/recon_lw.py` & `recon_lw-2.0.0.dev4638710878/recon_lw/recon_lw.py`

 * *Files identical despite different names*

### Comparing `recon_lw-2.0.0.dev4638480940/recon_lw/recon_ob.py` & `recon_lw-2.0.0.dev4638710878/recon_lw/recon_ob.py`

 * *Files 0% similar despite different names*

```diff
@@ -77,14 +77,16 @@
 
     if book_id is not None:
         if book_id not in books_cache:
             books_cache[book_id] = {"ask": {}, "bid": {}, "status": "?"}
         book = books_cache[book_id]
         initial_book = copy.deepcopy(book)
         operation, parameters = update_book_rule(book, mess)
+        if operation is None:
+            return 
         initial_parameters = copy.copy(parameters)
         parameters["order_book"] = book
         result = operation(**parameters)
         if len(result) > 0:
             result["operation"] = operation.__name__
             result["operation_params"] = initial_parameters
             result["initial_book"] = initial_book
```

### Comparing `recon_lw-2.0.0.dev4638480940/setup.py` & `recon_lw-2.0.0.dev4638710878/setup.py`

 * *Files identical despite different names*

