# Comparing `tmp/jmcomic-1.5.0.tar.gz` & `tmp/jmcomic-1.5.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "/home/runner/work/JMComic-Crawler-Python/JMComic-Crawler-Python/dist/.tmp-8lmu8dc7/jmcomic-1.5.0.tar", last modified: Fri Apr  7 10:08:21 2023, max compression
+gzip compressed data, was "/home/runner/work/JMComic-Crawler-Python/JMComic-Crawler-Python/dist/.tmp-hn88r5vv/jmcomic-1.5.1.tar", last modified: Fri Apr  7 10:21:21 2023, max compression
```

## Comparing `jmcomic-1.5.0.tar` & `jmcomic-1.5.1.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:08:21.000000 jmcomic-1.5.0/
--rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-04-07 10:08:03.000000 jmcomic-1.5.0/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     3712 2023-04-07 10:08:21.000000 jmcomic-1.5.0/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2867 2023-04-07 10:08:03.000000 jmcomic-1.5.0/README.md
--rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 10:08:21.000000 jmcomic-1.5.0/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-07 10:08:03.000000 jmcomic-1.5.0/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:08:21.000000 jmcomic-1.5.0/src/jmcomic/
--rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     5129 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/api.py
--rw-r--r--   0 runner    (1001) docker     (123)     6971 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_client.py
--rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_config.py
--rw-r--r--   0 runner    (1001) docker     (123)     9480 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_entity.py
--rw-r--r--   0 runner    (1001) docker     (123)    17129 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_option.py
--rw-r--r--   0 runner    (1001) docker     (123)     8537 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_service.py
--rw-r--r--   0 runner    (1001) docker     (123)    10136 2023-04-07 10:08:03.000000 jmcomic-1.5.0/src/jmcomic/jm_toolkit.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:08:21.000000 jmcomic-1.5.0/src/jmcomic.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3712 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      395 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-07 10:08:20.000000 jmcomic-1.5.0/src/jmcomic.egg-info/top_level.txt
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:21:21.000000 jmcomic-1.5.1/
+-rw-r--r--   0 runner    (1001) docker     (123)     1064 2023-04-07 10:21:12.000000 jmcomic-1.5.1/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     3712 2023-04-07 10:21:21.000000 jmcomic-1.5.1/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2867 2023-04-07 10:21:12.000000 jmcomic-1.5.1/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 10:21:21.000000 jmcomic-1.5.1/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1510 2023-04-07 10:21:12.000000 jmcomic-1.5.1/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:21:21.000000 jmcomic-1.5.1/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:21:21.000000 jmcomic-1.5.1/src/jmcomic/
+-rw-r--r--   0 runner    (1001) docker     (123)      172 2023-04-07 10:21:12.000000 jmcomic-1.5.1/src/jmcomic/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5129 2023-04-07 10:21:12.000000 jmcomic-1.5.1/src/jmcomic/api.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6971 2023-04-07 10:21:12.000000 jmcomic-1.5.1/src/jmcomic/jm_client.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3345 2023-04-07 10:21:12.000000 jmcomic-1.5.1/src/jmcomic/jm_config.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9480 2023-04-07 10:21:12.000000 jmcomic-1.5.1/src/jmcomic/jm_entity.py
+-rw-r--r--   0 runner    (1001) docker     (123)    17135 2023-04-07 10:21:12.000000 jmcomic-1.5.1/src/jmcomic/jm_option.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8537 2023-04-07 10:21:12.000000 jmcomic-1.5.1/src/jmcomic/jm_service.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10136 2023-04-07 10:21:12.000000 jmcomic-1.5.1/src/jmcomic/jm_toolkit.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 10:21:21.000000 jmcomic-1.5.1/src/jmcomic.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3712 2023-04-07 10:21:21.000000 jmcomic-1.5.1/src/jmcomic.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      395 2023-04-07 10:21:21.000000 jmcomic-1.5.1/src/jmcomic.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 10:21:21.000000 jmcomic-1.5.1/src/jmcomic.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       32 2023-04-07 10:21:21.000000 jmcomic-1.5.1/src/jmcomic.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        8 2023-04-07 10:21:21.000000 jmcomic-1.5.1/src/jmcomic.egg-info/top_level.txt
```

### Comparing `jmcomic-1.5.0/LICENSE` & `jmcomic-1.5.1/LICENSE`

 * *Files identical despite different names*

### Comparing `jmcomic-1.5.0/PKG-INFO` & `jmcomic-1.5.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jmcomic
-Version: 1.5.0
+Version: 1.5.1
 Summary: Python API For JMComic (禁漫天堂)
 Home-page: https://github.com/hect0x7/JMComic-Crawler-Python
 Author: hect0x7
 Author-email: 93357912+hect0x7@users.noreply.github.com
 Keywords: python,jmcomic,18comic,禁漫天堂,NSFW
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

### Comparing `jmcomic-1.5.0/README.md` & `jmcomic-1.5.1/README.md`

 * *Files identical despite different names*

### Comparing `jmcomic-1.5.0/setup.py` & `jmcomic-1.5.1/setup.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.5.0/src/jmcomic/api.py` & `jmcomic-1.5.1/src/jmcomic/api.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.5.0/src/jmcomic/jm_client.py` & `jmcomic-1.5.1/src/jmcomic/jm_client.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.5.0/src/jmcomic/jm_config.py` & `jmcomic-1.5.1/src/jmcomic/jm_config.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.5.0/src/jmcomic/jm_entity.py` & `jmcomic-1.5.1/src/jmcomic/jm_entity.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.5.0/src/jmcomic/jm_option.py` & `jmcomic-1.5.1/src/jmcomic/jm_option.py`

 * *Files 1% similar despite different names*

```diff
@@ -399,15 +399,15 @@
             self.client_config[key] = domain
             return domain
 
         def handle_headers(key='headers'):
             headers = meta_data.get(key, None)
             if headers is None or (not isinstance(headers, dict)) or len(headers) == 0:
                 # 未配置headers，使用默认headers
-                headers = JmModuleConfig.headers()
+                headers = JmModuleConfig.headers(domain)
 
             meta_data[key] = headers
 
         def handle_postman():
             nonlocal postman
             postman = postman_clazz(meta_data)
```

### Comparing `jmcomic-1.5.0/src/jmcomic/jm_service.py` & `jmcomic-1.5.1/src/jmcomic/jm_service.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.5.0/src/jmcomic/jm_toolkit.py` & `jmcomic-1.5.1/src/jmcomic/jm_toolkit.py`

 * *Files identical despite different names*

### Comparing `jmcomic-1.5.0/src/jmcomic.egg-info/PKG-INFO` & `jmcomic-1.5.1/src/jmcomic.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: jmcomic
-Version: 1.5.0
+Version: 1.5.1
 Summary: Python API For JMComic (禁漫天堂)
 Home-page: https://github.com/hect0x7/JMComic-Crawler-Python
 Author: hect0x7
 Author-email: 93357912+hect0x7@users.noreply.github.com
 Keywords: python,jmcomic,18comic,禁漫天堂,NSFW
 Classifier: Development Status :: 4 - Beta
 Classifier: Intended Audience :: Developers
```

