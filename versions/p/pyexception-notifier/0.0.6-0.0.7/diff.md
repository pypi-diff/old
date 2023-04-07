# Comparing `tmp/pyexception-notifier-0.0.6.tar.gz` & `tmp/pyexception-notifier-0.0.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyexception-notifier-0.0.6.tar", last modified: Fri Apr  7 08:25:17 2023, max compression
+gzip compressed data, was "pyexception-notifier-0.0.7.tar", last modified: Fri Apr  7 08:27:06 2023, max compression
```

## Comparing `pyexception-notifier-0.0.6.tar` & `pyexception-notifier-0.0.7.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:25:17.873680 pyexception-notifier-0.0.6/
--rw-rw-r--   0 user      (1000) user      (1000)     1088 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.6/LICENSE.txt
--rw-rw-r--   0 user      (1000) user      (1000)      215 2023-04-07 08:25:17.873680 pyexception-notifier-0.0.6/PKG-INFO
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:25:17.873680 pyexception-notifier-0.0.6/pyexception_notifier/
--rw-rw-r--   0 user      (1000) user      (1000)       72 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.6/pyexception_notifier/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)      660 2023-04-07 08:24:41.000000 pyexception-notifier-0.0.6/pyexception_notifier/config.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:25:17.873680 pyexception-notifier-0.0.6/pyexception_notifier/exceptions/
--rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.6/pyexception_notifier/exceptions/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)      675 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.6/pyexception_notifier/exceptions/exceptions.py
--rw-rw-r--   0 user      (1000) user      (1000)     1758 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.6/pyexception_notifier/main_.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:25:17.873680 pyexception-notifier-0.0.6/pyexception_notifier/notify_sources_clients/
--rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.6/pyexception_notifier/notify_sources_clients/__init__.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:25:17.873680 pyexception-notifier-0.0.6/pyexception_notifier/notify_sources_clients/telegram/
--rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.6/pyexception_notifier/notify_sources_clients/telegram/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)      602 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.6/pyexception_notifier/notify_sources_clients/telegram/client.py
--rw-rw-r--   0 user      (1000) user      (1000)      273 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.6/pyexception_notifier/test_notifier.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:25:17.873680 pyexception-notifier-0.0.6/pyexception_notifier/utils/
--rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.6/pyexception_notifier/utils/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)      171 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.6/pyexception_notifier/utils/enums.py
--rw-rw-r--   0 user      (1000) user      (1000)      908 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.6/pyexception_notifier/utils/exception_parsers.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:25:17.873680 pyexception-notifier-0.0.6/pyexception_notifier.egg-info/
--rw-rw-r--   0 user      (1000) user      (1000)      215 2023-04-07 08:25:17.000000 pyexception-notifier-0.0.6/pyexception_notifier.egg-info/PKG-INFO
--rw-rw-r--   0 user      (1000) user      (1000)      778 2023-04-07 08:25:17.000000 pyexception-notifier-0.0.6/pyexception_notifier.egg-info/SOURCES.txt
--rw-rw-r--   0 user      (1000) user      (1000)        1 2023-04-07 08:25:17.000000 pyexception-notifier-0.0.6/pyexception_notifier.egg-info/dependency_links.txt
--rw-rw-r--   0 user      (1000) user      (1000)       70 2023-04-07 08:25:17.000000 pyexception-notifier-0.0.6/pyexception_notifier.egg-info/requires.txt
--rw-rw-r--   0 user      (1000) user      (1000)       21 2023-04-07 08:25:17.000000 pyexception-notifier-0.0.6/pyexception_notifier.egg-info/top_level.txt
--rw-rw-r--   0 user      (1000) user      (1000)       79 2023-04-07 08:25:17.873680 pyexception-notifier-0.0.6/setup.cfg
--rw-rw-r--   0 user      (1000) user      (1000)      646 2023-04-07 08:25:03.000000 pyexception-notifier-0.0.6/setup.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:27:06.241678 pyexception-notifier-0.0.7/
+-rw-rw-r--   0 user      (1000) user      (1000)     1088 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.7/LICENSE.txt
+-rw-rw-r--   0 user      (1000) user      (1000)      915 2023-04-07 08:27:06.241678 pyexception-notifier-0.0.7/PKG-INFO
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:27:06.241678 pyexception-notifier-0.0.7/pyexception_notifier/
+-rw-rw-r--   0 user      (1000) user      (1000)       72 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.7/pyexception_notifier/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      660 2023-04-07 08:24:41.000000 pyexception-notifier-0.0.7/pyexception_notifier/config.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:27:06.241678 pyexception-notifier-0.0.7/pyexception_notifier/exceptions/
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.7/pyexception_notifier/exceptions/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      675 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.7/pyexception_notifier/exceptions/exceptions.py
+-rw-rw-r--   0 user      (1000) user      (1000)     1758 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.7/pyexception_notifier/main_.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:27:06.241678 pyexception-notifier-0.0.7/pyexception_notifier/notify_sources_clients/
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.7/pyexception_notifier/notify_sources_clients/__init__.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:27:06.241678 pyexception-notifier-0.0.7/pyexception_notifier/notify_sources_clients/telegram/
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.7/pyexception_notifier/notify_sources_clients/telegram/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      602 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.7/pyexception_notifier/notify_sources_clients/telegram/client.py
+-rw-rw-r--   0 user      (1000) user      (1000)      273 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.7/pyexception_notifier/test_notifier.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:27:06.241678 pyexception-notifier-0.0.7/pyexception_notifier/utils/
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.7/pyexception_notifier/utils/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      171 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.7/pyexception_notifier/utils/enums.py
+-rw-rw-r--   0 user      (1000) user      (1000)      908 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.7/pyexception_notifier/utils/exception_parsers.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:27:06.241678 pyexception-notifier-0.0.7/pyexception_notifier.egg-info/
+-rw-rw-r--   0 user      (1000) user      (1000)      915 2023-04-07 08:27:06.000000 pyexception-notifier-0.0.7/pyexception_notifier.egg-info/PKG-INFO
+-rw-rw-r--   0 user      (1000) user      (1000)      778 2023-04-07 08:27:06.000000 pyexception-notifier-0.0.7/pyexception_notifier.egg-info/SOURCES.txt
+-rw-rw-r--   0 user      (1000) user      (1000)        1 2023-04-07 08:27:06.000000 pyexception-notifier-0.0.7/pyexception_notifier.egg-info/dependency_links.txt
+-rw-rw-r--   0 user      (1000) user      (1000)       70 2023-04-07 08:27:06.000000 pyexception-notifier-0.0.7/pyexception_notifier.egg-info/requires.txt
+-rw-rw-r--   0 user      (1000) user      (1000)       21 2023-04-07 08:27:06.000000 pyexception-notifier-0.0.7/pyexception_notifier.egg-info/top_level.txt
+-rw-rw-r--   0 user      (1000) user      (1000)       79 2023-04-07 08:27:06.241678 pyexception-notifier-0.0.7/setup.cfg
+-rw-rw-r--   0 user      (1000) user      (1000)      646 2023-04-07 08:27:03.000000 pyexception-notifier-0.0.7/setup.py
```

### Comparing `pyexception-notifier-0.0.6/LICENSE.txt` & `pyexception-notifier-0.0.7/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.6/pyexception_notifier/config.py` & `pyexception-notifier-0.0.7/pyexception_notifier/config.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.6/pyexception_notifier/exceptions/exceptions.py` & `pyexception-notifier-0.0.7/pyexception_notifier/exceptions/exceptions.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.6/pyexception_notifier/main_.py` & `pyexception-notifier-0.0.7/pyexception_notifier/main_.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.6/pyexception_notifier/notify_sources_clients/telegram/client.py` & `pyexception-notifier-0.0.7/pyexception_notifier/notify_sources_clients/telegram/client.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.6/pyexception_notifier/utils/exception_parsers.py` & `pyexception-notifier-0.0.7/pyexception_notifier/utils/exception_parsers.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.6/pyexception_notifier.egg-info/SOURCES.txt` & `pyexception-notifier-0.0.7/pyexception_notifier.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.6/setup.py` & `pyexception-notifier-0.0.7/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 else:
     long_description = ''
 
 
 setup(
     name='pyexception-notifier',
     packages=find_packages(),
-    version='0.0.6',
+    version='0.0.7',
     description='Exception notifier',
     long_description=long_description,
     long_description_content_type='text/markdown',
     author='r.islyamgali',
     license='MIT',
     install_requires=[
         "pydantic",
```

