# Comparing `tmp/pyxk-0.4.6.tar.gz` & `tmp/pyxk-0.4.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyxk-0.4.6.tar", last modified: Thu Apr  6 16:04:35 2023, max compression
+gzip compressed data, was "pyxk-0.4.7.tar", last modified: Fri Apr  7 09:10:58 2023, max compression
```

## Comparing `pyxk-0.4.6.tar` & `pyxk-0.4.7.tar`

### file list

```diff
@@ -1,32 +1,33 @@
-drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-06 16:04:35.103993 pyxk-0.4.6/
--rw-rw----   0 root         (0) everybody  (9997)     1079 2022-09-01 11:31:05.000000 pyxk-0.4.6/LICENSE
--rw-rw----   0 root         (0) everybody  (9997)      343 2023-04-06 16:04:35.103993 pyxk-0.4.6/PKG-INFO
--rw-rw----   0 root         (0) everybody  (9997)        4 2023-03-31 15:33:16.000000 pyxk-0.4.6/README.md
-drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-06 16:04:35.103993 pyxk-0.4.6/pyxk/
--rw-rw----   0 root         (0) everybody  (9997)      568 2023-04-06 16:01:42.000000 pyxk-0.4.6/pyxk/__init__.py
-drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-06 16:04:35.103993 pyxk-0.4.6/pyxk/aes/
--rw-rw----   0 root         (0) everybody  (9997)       79 2023-02-24 04:10:40.000000 pyxk-0.4.6/pyxk/aes/__init__.py
--rw-rw----   0 root         (0) everybody  (9997)     3639 2023-04-06 15:25:24.000000 pyxk-0.4.6/pyxk/aes/_fmtdata.py
--rw-rw----   0 root         (0) everybody  (9997)     4701 2023-04-06 15:27:39.000000 pyxk-0.4.6/pyxk/aes/cryptor.py
--rw-rw----   0 root         (0) everybody  (9997)      954 2023-03-15 06:04:12.000000 pyxk-0.4.6/pyxk/lazy_loader.py
-drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-06 16:04:35.103993 pyxk-0.4.6/pyxk/m3u8/
--rw-rw----   0 root         (0) everybody  (9997)       82 2023-03-16 14:08:36.000000 pyxk-0.4.6/pyxk/m3u8/__init__.py
--rw-rw----   0 root         (0) everybody  (9997)     8292 2023-03-16 12:13:38.000000 pyxk-0.4.6/pyxk/m3u8/_download.py
--rw-rw----   0 root         (0) everybody  (9997)     3199 2023-03-16 16:35:49.000000 pyxk-0.4.6/pyxk/m3u8/_entry_point.py
--rw-rw----   0 root         (0) everybody  (9997)     7791 2023-03-16 16:35:32.000000 pyxk-0.4.6/pyxk/m3u8/_m3u8.py
--rw-rw----   0 root         (0) everybody  (9997)     4504 2023-03-17 04:00:18.000000 pyxk-0.4.6/pyxk/m3u8/_parser.py
-drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-06 16:04:35.103993 pyxk-0.4.6/pyxk/requests/
--rw-rw----   0 root         (0) everybody  (9997)      235 2023-04-06 15:53:39.000000 pyxk-0.4.6/pyxk/requests/__init__.py
--rw-rw----   0 root         (0) everybody  (9997)     5648 2023-04-06 15:32:32.000000 pyxk-0.4.6/pyxk/requests/_entry_point.py
--rw-rw----   0 root         (0) everybody  (9997)     7514 2023-03-31 10:17:41.000000 pyxk-0.4.6/pyxk/requests/api.py
--rw-rw----   0 root         (0) everybody  (9997)    21859 2023-04-06 15:20:21.000000 pyxk-0.4.6/pyxk/requests/sessions.py
--rw-rw----   0 root         (0) everybody  (9997)    12202 2023-04-06 16:00:37.000000 pyxk-0.4.6/pyxk/utils.py
-drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-06 16:04:35.103993 pyxk-0.4.6/pyxk.egg-info/
--rw-rw----   0 root         (0) everybody  (9997)      343 2023-04-06 16:04:34.000000 pyxk-0.4.6/pyxk.egg-info/PKG-INFO
--rw-rw----   0 root         (0) everybody  (9997)      523 2023-04-06 16:04:35.000000 pyxk-0.4.6/pyxk.egg-info/SOURCES.txt
--rw-rw----   0 root         (0) everybody  (9997)        1 2023-04-06 16:04:34.000000 pyxk-0.4.6/pyxk.egg-info/dependency_links.txt
--rw-rw----   0 root         (0) everybody  (9997)       91 2023-04-06 16:04:34.000000 pyxk-0.4.6/pyxk.egg-info/entry_points.txt
--rw-rw----   0 root         (0) everybody  (9997)       55 2023-04-06 16:04:34.000000 pyxk-0.4.6/pyxk.egg-info/requires.txt
--rw-rw----   0 root         (0) everybody  (9997)        5 2023-04-06 16:04:34.000000 pyxk-0.4.6/pyxk.egg-info/top_level.txt
--rw-rw----   0 root         (0) everybody  (9997)       38 2023-04-06 16:04:35.103993 pyxk-0.4.6/setup.cfg
--rw-rw----   0 root         (0) everybody  (9997)      916 2023-04-06 16:03:44.000000 pyxk-0.4.6/setup.py
+drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-07 09:10:58.026980 pyxk-0.4.7/
+-rw-rw----   0 root         (0) everybody  (9997)     1079 2022-09-01 11:31:05.000000 pyxk-0.4.7/LICENSE
+-rw-rw----   0 root         (0) everybody  (9997)      343 2023-04-07 09:10:58.026980 pyxk-0.4.7/PKG-INFO
+-rw-rw----   0 root         (0) everybody  (9997)        4 2023-03-31 15:33:16.000000 pyxk-0.4.7/README.md
+drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-07 09:10:58.026980 pyxk-0.4.7/pyxk/
+-rw-rw----   0 root         (0) everybody  (9997)      612 2023-04-07 05:35:36.000000 pyxk-0.4.7/pyxk/__init__.py
+drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-07 09:10:58.026980 pyxk-0.4.7/pyxk/aes/
+-rw-rw----   0 root         (0) everybody  (9997)       79 2023-02-24 04:10:40.000000 pyxk-0.4.7/pyxk/aes/__init__.py
+-rw-rw----   0 root         (0) everybody  (9997)     3639 2023-04-06 15:25:24.000000 pyxk-0.4.7/pyxk/aes/_fmtdata.py
+-rw-rw----   0 root         (0) everybody  (9997)     4701 2023-04-06 15:27:39.000000 pyxk-0.4.7/pyxk/aes/cryptor.py
+-rw-rw----   0 root         (0) everybody  (9997)     6946 2023-04-07 09:09:24.000000 pyxk-0.4.7/pyxk/async_session.py
+-rw-rw----   0 root         (0) everybody  (9997)      954 2023-03-15 06:04:12.000000 pyxk-0.4.7/pyxk/lazy_loader.py
+drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-07 09:10:58.026980 pyxk-0.4.7/pyxk/m3u8/
+-rw-rw----   0 root         (0) everybody  (9997)       82 2023-03-16 14:08:36.000000 pyxk-0.4.7/pyxk/m3u8/__init__.py
+-rw-rw----   0 root         (0) everybody  (9997)     8292 2023-03-16 12:13:38.000000 pyxk-0.4.7/pyxk/m3u8/_download.py
+-rw-rw----   0 root         (0) everybody  (9997)     3199 2023-03-16 16:35:49.000000 pyxk-0.4.7/pyxk/m3u8/_entry_point.py
+-rw-rw----   0 root         (0) everybody  (9997)     7791 2023-03-16 16:35:32.000000 pyxk-0.4.7/pyxk/m3u8/_m3u8.py
+-rw-rw----   0 root         (0) everybody  (9997)     4504 2023-03-17 04:00:18.000000 pyxk-0.4.7/pyxk/m3u8/_parser.py
+drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-07 09:10:58.026980 pyxk-0.4.7/pyxk/requests/
+-rw-rw----   0 root         (0) everybody  (9997)      235 2023-04-06 15:53:39.000000 pyxk-0.4.7/pyxk/requests/__init__.py
+-rw-rw----   0 root         (0) everybody  (9997)     5598 2023-04-06 16:07:00.000000 pyxk-0.4.7/pyxk/requests/_entry_point.py
+-rw-rw----   0 root         (0) everybody  (9997)     7514 2023-03-31 10:17:41.000000 pyxk-0.4.7/pyxk/requests/api.py
+-rw-rw----   0 root         (0) everybody  (9997)    21859 2023-04-06 15:20:21.000000 pyxk-0.4.7/pyxk/requests/sessions.py
+-rw-rw----   0 root         (0) everybody  (9997)    12202 2023-04-06 16:00:37.000000 pyxk-0.4.7/pyxk/utils.py
+drwxrwx---   0 root         (0) everybody  (9997)        0 2023-04-07 09:10:58.026980 pyxk-0.4.7/pyxk.egg-info/
+-rw-rw----   0 root         (0) everybody  (9997)      343 2023-04-07 09:10:57.000000 pyxk-0.4.7/pyxk.egg-info/PKG-INFO
+-rw-rw----   0 root         (0) everybody  (9997)      545 2023-04-07 09:10:57.000000 pyxk-0.4.7/pyxk.egg-info/SOURCES.txt
+-rw-rw----   0 root         (0) everybody  (9997)        1 2023-04-07 09:10:57.000000 pyxk-0.4.7/pyxk.egg-info/dependency_links.txt
+-rw-rw----   0 root         (0) everybody  (9997)       91 2023-04-07 09:10:57.000000 pyxk-0.4.7/pyxk.egg-info/entry_points.txt
+-rw-rw----   0 root         (0) everybody  (9997)       55 2023-04-07 09:10:57.000000 pyxk-0.4.7/pyxk.egg-info/requires.txt
+-rw-rw----   0 root         (0) everybody  (9997)        5 2023-04-07 09:10:57.000000 pyxk-0.4.7/pyxk.egg-info/top_level.txt
+-rw-rw----   0 root         (0) everybody  (9997)       38 2023-04-07 09:10:58.026980 pyxk-0.4.7/setup.cfg
+-rw-rw----   0 root         (0) everybody  (9997)      916 2023-04-07 09:10:10.000000 pyxk-0.4.7/setup.py
```

### Comparing `pyxk-0.4.6/LICENSE` & `pyxk-0.4.7/LICENSE`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/__init__.py` & `pyxk-0.4.7/pyxk/__init__.py`

 * *Files 7% similar despite different names*

```diff
@@ -27,7 +27,8 @@
     post,
     put,
     request,
     wget,
     Session,
 )
 from pyxk.lazy_loader import LazyLoader
+from pyxk.async_session import AsyncSession
```

### Comparing `pyxk-0.4.6/pyxk/aes/_fmtdata.py` & `pyxk-0.4.7/pyxk/aes/_fmtdata.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/aes/cryptor.py` & `pyxk-0.4.7/pyxk/aes/cryptor.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/lazy_loader.py` & `pyxk-0.4.7/pyxk/lazy_loader.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/m3u8/_download.py` & `pyxk-0.4.7/pyxk/m3u8/_download.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/m3u8/_entry_point.py` & `pyxk-0.4.7/pyxk/m3u8/_entry_point.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/m3u8/_m3u8.py` & `pyxk-0.4.7/pyxk/m3u8/_m3u8.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/m3u8/_parser.py` & `pyxk-0.4.7/pyxk/m3u8/_parser.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/requests/_entry_point.py` & `pyxk-0.4.7/pyxk/requests/_entry_point.py`

 * *Files 2% similar despite different names*

```diff
@@ -243,17 +243,16 @@
             padding=1,
             border_style="bright_blue"
         )
         console.print(renders)
 
     if not no_show_content and not output and threads==1:
         response.encoding = response.apparent_encoding
-        console = rich_console.Console()
         for chunk in response.iter_lines():
             try:
                 chunk = chunk.decode(response.encoding)
             except (
                 UnicodeDecodeError,
                 AttributeError
             ):
-                raise
-            console.print(chunk, end="")
+                pass
+            print(chunk, end="")
```

### Comparing `pyxk-0.4.6/pyxk/requests/api.py` & `pyxk-0.4.7/pyxk/requests/api.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/requests/sessions.py` & `pyxk-0.4.7/pyxk/requests/sessions.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk/utils.py` & `pyxk-0.4.7/pyxk/utils.py`

 * *Files identical despite different names*

### Comparing `pyxk-0.4.6/pyxk.egg-info/SOURCES.txt` & `pyxk-0.4.7/pyxk.egg-info/SOURCES.txt`

 * *Files 8% similar despite different names*

```diff
@@ -1,11 +1,12 @@
 LICENSE
 README.md
 setup.py
 pyxk/__init__.py
+pyxk/async_session.py
 pyxk/lazy_loader.py
 pyxk/utils.py
 pyxk.egg-info/PKG-INFO
 pyxk.egg-info/SOURCES.txt
 pyxk.egg-info/dependency_links.txt
 pyxk.egg-info/entry_points.txt
 pyxk.egg-info/requires.txt
```

### Comparing `pyxk-0.4.6/setup.py` & `pyxk-0.4.7/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 
 with open("README.md", "r", encoding="utf-8") as fh:
     long_description = fh.read()
 
 setuptools.setup(
     name="pyxk",
-    version="0.4.6",
+    version="0.4.7",
     author="xiek",
     install_requires=[
         "requests",
         "pycryptodome",
         "rich",
         "m3u8",
         "aiohttp",
```

