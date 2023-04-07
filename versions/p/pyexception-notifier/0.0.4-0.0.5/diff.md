# Comparing `tmp/pyexception-notifier-0.0.4.tar.gz` & `tmp/pyexception-notifier-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pyexception-notifier-0.0.4.tar", last modified: Fri Apr  7 08:18:03 2023, max compression
+gzip compressed data, was "pyexception-notifier-0.0.5.tar", last modified: Fri Apr  7 08:19:11 2023, max compression
```

## Comparing `pyexception-notifier-0.0.4.tar` & `pyexception-notifier-0.0.5.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:18:03.005685 pyexception-notifier-0.0.4/
--rw-rw-r--   0 user      (1000) user      (1000)     1088 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.4/LICENSE.txt
--rw-rw-r--   0 user      (1000) user      (1000)      262 2023-04-07 08:18:03.005685 pyexception-notifier-0.0.4/PKG-INFO
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:18:03.005685 pyexception-notifier-0.0.4/pyexception_notifier/
--rw-rw-r--   0 user      (1000) user      (1000)       72 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.4/pyexception_notifier/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)      717 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.4/pyexception_notifier/config.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:18:03.005685 pyexception-notifier-0.0.4/pyexception_notifier/exceptions/
--rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.4/pyexception_notifier/exceptions/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)      675 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.4/pyexception_notifier/exceptions/exceptions.py
--rw-rw-r--   0 user      (1000) user      (1000)     1758 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.4/pyexception_notifier/main_.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:18:03.005685 pyexception-notifier-0.0.4/pyexception_notifier/notify_sources_clients/
--rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.4/pyexception_notifier/notify_sources_clients/__init__.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:18:03.005685 pyexception-notifier-0.0.4/pyexception_notifier/notify_sources_clients/telegram/
--rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.4/pyexception_notifier/notify_sources_clients/telegram/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)      602 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.4/pyexception_notifier/notify_sources_clients/telegram/client.py
--rw-rw-r--   0 user      (1000) user      (1000)      273 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.4/pyexception_notifier/test_notifier.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:18:03.005685 pyexception-notifier-0.0.4/pyexception_notifier/utils/
--rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.4/pyexception_notifier/utils/__init__.py
--rw-rw-r--   0 user      (1000) user      (1000)      171 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.4/pyexception_notifier/utils/enums.py
--rw-rw-r--   0 user      (1000) user      (1000)      908 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.4/pyexception_notifier/utils/exception_parsers.py
-drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:18:03.005685 pyexception-notifier-0.0.4/pyexception_notifier.egg-info/
--rw-rw-r--   0 user      (1000) user      (1000)      262 2023-04-07 08:18:02.000000 pyexception-notifier-0.0.4/pyexception_notifier.egg-info/PKG-INFO
--rw-rw-r--   0 user      (1000) user      (1000)      778 2023-04-07 08:18:02.000000 pyexception-notifier-0.0.4/pyexception_notifier.egg-info/SOURCES.txt
--rw-rw-r--   0 user      (1000) user      (1000)        1 2023-04-07 08:18:02.000000 pyexception-notifier-0.0.4/pyexception_notifier.egg-info/dependency_links.txt
--rw-rw-r--   0 user      (1000) user      (1000)       70 2023-04-07 08:18:02.000000 pyexception-notifier-0.0.4/pyexception_notifier.egg-info/requires.txt
--rw-rw-r--   0 user      (1000) user      (1000)       21 2023-04-07 08:18:02.000000 pyexception-notifier-0.0.4/pyexception_notifier.egg-info/top_level.txt
--rw-rw-r--   0 user      (1000) user      (1000)       79 2023-04-07 08:18:03.005685 pyexception-notifier-0.0.4/setup.cfg
--rw-rw-r--   0 user      (1000) user      (1000)      646 2023-04-07 08:17:45.000000 pyexception-notifier-0.0.4/setup.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:19:11.197684 pyexception-notifier-0.0.5/
+-rw-rw-r--   0 user      (1000) user      (1000)     1088 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.5/LICENSE.txt
+-rw-rw-r--   0 user      (1000) user      (1000)      954 2023-04-07 08:19:11.197684 pyexception-notifier-0.0.5/PKG-INFO
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:19:11.197684 pyexception-notifier-0.0.5/pyexception_notifier/
+-rw-rw-r--   0 user      (1000) user      (1000)       72 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.5/pyexception_notifier/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      717 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.5/pyexception_notifier/config.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:19:11.197684 pyexception-notifier-0.0.5/pyexception_notifier/exceptions/
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.5/pyexception_notifier/exceptions/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      675 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.5/pyexception_notifier/exceptions/exceptions.py
+-rw-rw-r--   0 user      (1000) user      (1000)     1758 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.5/pyexception_notifier/main_.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:19:11.197684 pyexception-notifier-0.0.5/pyexception_notifier/notify_sources_clients/
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.5/pyexception_notifier/notify_sources_clients/__init__.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:19:11.197684 pyexception-notifier-0.0.5/pyexception_notifier/notify_sources_clients/telegram/
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.5/pyexception_notifier/notify_sources_clients/telegram/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      602 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.5/pyexception_notifier/notify_sources_clients/telegram/client.py
+-rw-rw-r--   0 user      (1000) user      (1000)      273 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.5/pyexception_notifier/test_notifier.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:19:11.197684 pyexception-notifier-0.0.5/pyexception_notifier/utils/
+-rw-rw-r--   0 user      (1000) user      (1000)        0 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.5/pyexception_notifier/utils/__init__.py
+-rw-rw-r--   0 user      (1000) user      (1000)      171 2023-04-06 08:06:17.000000 pyexception-notifier-0.0.5/pyexception_notifier/utils/enums.py
+-rw-rw-r--   0 user      (1000) user      (1000)      908 2023-04-07 06:12:35.000000 pyexception-notifier-0.0.5/pyexception_notifier/utils/exception_parsers.py
+drwxrwxr-x   0 user      (1000) user      (1000)        0 2023-04-07 08:19:11.197684 pyexception-notifier-0.0.5/pyexception_notifier.egg-info/
+-rw-rw-r--   0 user      (1000) user      (1000)      954 2023-04-07 08:19:11.000000 pyexception-notifier-0.0.5/pyexception_notifier.egg-info/PKG-INFO
+-rw-rw-r--   0 user      (1000) user      (1000)      778 2023-04-07 08:19:11.000000 pyexception-notifier-0.0.5/pyexception_notifier.egg-info/SOURCES.txt
+-rw-rw-r--   0 user      (1000) user      (1000)        1 2023-04-07 08:19:11.000000 pyexception-notifier-0.0.5/pyexception_notifier.egg-info/dependency_links.txt
+-rw-rw-r--   0 user      (1000) user      (1000)       70 2023-04-07 08:19:11.000000 pyexception-notifier-0.0.5/pyexception_notifier.egg-info/requires.txt
+-rw-rw-r--   0 user      (1000) user      (1000)       21 2023-04-07 08:19:11.000000 pyexception-notifier-0.0.5/pyexception_notifier.egg-info/top_level.txt
+-rw-rw-r--   0 user      (1000) user      (1000)       79 2023-04-07 08:19:11.197684 pyexception-notifier-0.0.5/setup.cfg
+-rw-rw-r--   0 user      (1000) user      (1000)      646 2023-04-07 08:19:04.000000 pyexception-notifier-0.0.5/setup.py
```

### Comparing `pyexception-notifier-0.0.4/LICENSE.txt` & `pyexception-notifier-0.0.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.4/pyexception_notifier/config.py` & `pyexception-notifier-0.0.5/pyexception_notifier/config.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.4/pyexception_notifier/exceptions/exceptions.py` & `pyexception-notifier-0.0.5/pyexception_notifier/exceptions/exceptions.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.4/pyexception_notifier/main_.py` & `pyexception-notifier-0.0.5/pyexception_notifier/main_.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.4/pyexception_notifier/notify_sources_clients/telegram/client.py` & `pyexception-notifier-0.0.5/pyexception_notifier/notify_sources_clients/telegram/client.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.4/pyexception_notifier/utils/exception_parsers.py` & `pyexception-notifier-0.0.5/pyexception_notifier/utils/exception_parsers.py`

 * *Files identical despite different names*

### Comparing `pyexception-notifier-0.0.4/pyexception_notifier.egg-info/SOURCES.txt` & `pyexception-notifier-0.0.5/pyexception_notifier.egg-info/SOURCES.txt`

 * *Files identical despite different names*

