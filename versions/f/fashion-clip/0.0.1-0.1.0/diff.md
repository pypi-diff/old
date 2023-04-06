# Comparing `tmp/fashion-clip-0.0.1.tar.gz` & `tmp/fashion-clip-0.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "fashion-clip-0.0.1.tar", last modified: Thu Apr  6 20:01:33 2023, max compression
+gzip compressed data, was "fashion-clip-0.1.0.tar", last modified: Thu Apr  6 20:13:59 2023, max compression
```

## Comparing `fashion-clip-0.0.1.tar` & `fashion-clip-0.1.0.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxr-x   0 vinid     (1000) vinid     (1000)        0 2023-04-06 20:01:33.647521 fashion-clip-0.0.1/
--rw-rw-r--   0 vinid     (1000) vinid     (1000)      276 2023-04-06 20:01:33.647521 fashion-clip-0.0.1/PKG-INFO
--rw-rw-r--   0 vinid     (1000) vinid     (1000)     9233 2023-04-04 01:09:03.000000 fashion-clip-0.0.1/README.md
-drwxrwxr-x   0 vinid     (1000) vinid     (1000)        0 2023-04-06 20:01:33.647521 fashion-clip-0.0.1/fashion_clip/
--rw-rw-r--   0 vinid     (1000) vinid     (1000)        0 2023-03-03 05:22:25.000000 fashion-clip-0.0.1/fashion_clip/__init__.py
--rw-rw-r--   0 vinid     (1000) vinid     (1000)     2608 2023-03-03 05:22:25.000000 fashion-clip-0.0.1/fashion_clip/attention_map.py
--rw-rw-r--   0 vinid     (1000) vinid     (1000)    14220 2023-04-04 01:12:21.000000 fashion-clip-0.0.1/fashion_clip/fashion_clip.py
--rw-rw-r--   0 vinid     (1000) vinid     (1000)     3579 2023-03-03 05:22:25.000000 fashion-clip-0.0.1/fashion_clip/s3_client.py
--rw-rw-r--   0 vinid     (1000) vinid     (1000)     6047 2023-03-03 05:22:25.000000 fashion-clip-0.0.1/fashion_clip/utils.py
-drwxrwxr-x   0 vinid     (1000) vinid     (1000)        0 2023-04-06 20:01:33.647521 fashion-clip-0.0.1/fashion_clip.egg-info/
--rw-rw-r--   0 vinid     (1000) vinid     (1000)      276 2023-04-06 20:01:33.000000 fashion-clip-0.0.1/fashion_clip.egg-info/PKG-INFO
--rw-rw-r--   0 vinid     (1000) vinid     (1000)      374 2023-04-06 20:01:33.000000 fashion-clip-0.0.1/fashion_clip.egg-info/SOURCES.txt
--rw-rw-r--   0 vinid     (1000) vinid     (1000)        1 2023-04-06 20:01:33.000000 fashion-clip-0.0.1/fashion_clip.egg-info/dependency_links.txt
--rw-rw-r--   0 vinid     (1000) vinid     (1000)        1 2023-04-06 20:01:33.000000 fashion-clip-0.0.1/fashion_clip.egg-info/not-zip-safe
--rw-rw-r--   0 vinid     (1000) vinid     (1000)      325 2023-04-06 20:01:33.000000 fashion-clip-0.0.1/fashion_clip.egg-info/requires.txt
--rw-rw-r--   0 vinid     (1000) vinid     (1000)       13 2023-04-06 20:01:33.000000 fashion-clip-0.0.1/fashion_clip.egg-info/top_level.txt
--rw-rw-r--   0 vinid     (1000) vinid     (1000)      107 2023-04-06 20:01:33.647521 fashion-clip-0.0.1/setup.cfg
--rw-rw-r--   0 vinid     (1000) vinid     (1000)      462 2023-03-03 05:22:25.000000 fashion-clip-0.0.1/setup.py
+drwxrwxr-x   0 vinid     (1000) vinid     (1000)        0 2023-04-06 20:13:59.377570 fashion-clip-0.1.0/
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)     9546 2023-04-06 20:13:59.377570 fashion-clip-0.1.0/PKG-INFO
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)     9233 2023-04-04 01:09:03.000000 fashion-clip-0.1.0/README.md
+drwxrwxr-x   0 vinid     (1000) vinid     (1000)        0 2023-04-06 20:13:59.377570 fashion-clip-0.1.0/fashion_clip/
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)        0 2023-03-03 05:22:25.000000 fashion-clip-0.1.0/fashion_clip/__init__.py
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)     2608 2023-03-03 05:22:25.000000 fashion-clip-0.1.0/fashion_clip/attention_map.py
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)    14220 2023-04-04 01:12:21.000000 fashion-clip-0.1.0/fashion_clip/fashion_clip.py
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)     3579 2023-03-03 05:22:25.000000 fashion-clip-0.1.0/fashion_clip/s3_client.py
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)     6047 2023-03-03 05:22:25.000000 fashion-clip-0.1.0/fashion_clip/utils.py
+drwxrwxr-x   0 vinid     (1000) vinid     (1000)        0 2023-04-06 20:13:59.377570 fashion-clip-0.1.0/fashion_clip.egg-info/
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)     9546 2023-04-06 20:13:59.000000 fashion-clip-0.1.0/fashion_clip.egg-info/PKG-INFO
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)      374 2023-04-06 20:13:59.000000 fashion-clip-0.1.0/fashion_clip.egg-info/SOURCES.txt
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)        1 2023-04-06 20:13:59.000000 fashion-clip-0.1.0/fashion_clip.egg-info/dependency_links.txt
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)        1 2023-04-06 20:01:33.000000 fashion-clip-0.1.0/fashion_clip.egg-info/not-zip-safe
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)      325 2023-04-06 20:13:59.000000 fashion-clip-0.1.0/fashion_clip.egg-info/requires.txt
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)       13 2023-04-06 20:13:59.000000 fashion-clip-0.1.0/fashion_clip.egg-info/top_level.txt
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)      107 2023-04-06 20:13:59.377570 fashion-clip-0.1.0/setup.cfg
+-rw-rw-r--   0 vinid     (1000) vinid     (1000)      641 2023-04-06 20:13:53.000000 fashion-clip-0.1.0/setup.py
```

### Comparing `fashion-clip-0.0.1/README.md` & `fashion-clip-0.1.0/README.md`

 * *Files identical despite different names*

### Comparing `fashion-clip-0.0.1/fashion_clip/attention_map.py` & `fashion-clip-0.1.0/fashion_clip/attention_map.py`

 * *Files identical despite different names*

### Comparing `fashion-clip-0.0.1/fashion_clip/fashion_clip.py` & `fashion-clip-0.1.0/fashion_clip/fashion_clip.py`

 * *Files identical despite different names*

### Comparing `fashion-clip-0.0.1/fashion_clip/s3_client.py` & `fashion-clip-0.1.0/fashion_clip/s3_client.py`

 * *Files identical despite different names*

### Comparing `fashion-clip-0.0.1/fashion_clip/utils.py` & `fashion-clip-0.1.0/fashion_clip/utils.py`

 * *Files identical despite different names*

