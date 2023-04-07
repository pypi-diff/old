# Comparing `tmp/TransLiter-0.0.1.tar.gz` & `tmp/TransLiter-0.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "TransLiter-0.0.1.tar", last modified: Fri Apr  7 03:52:19 2023, max compression
+gzip compressed data, was "TransLiter-0.0.2.tar", last modified: Fri Apr  7 03:56:32 2023, max compression
```

## Comparing `TransLiter-0.0.1.tar` & `TransLiter-0.0.2.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 hoyeolkim   (501) staff       (20)        0 2023-04-07 03:52:19.780983 TransLiter-0.0.1/
--rw-r--r--   0 hoyeolkim   (501) staff       (20)     1067 2023-04-07 00:09:21.000000 TransLiter-0.0.1/LICENSE
--rw-r--r--   0 hoyeolkim   (501) staff       (20)     1896 2023-04-07 03:52:19.780859 TransLiter-0.0.1/PKG-INFO
--rw-r--r--   0 hoyeolkim   (501) staff       (20)     1548 2023-04-07 03:11:49.000000 TransLiter-0.0.1/README.md
-drwxr-xr-x   0 hoyeolkim   (501) staff       (20)        0 2023-04-07 03:52:19.779739 TransLiter-0.0.1/TransLiter/
--rw-r--r--   0 hoyeolkim   (501) staff       (20)        0 2023-04-07 03:16:39.000000 TransLiter-0.0.1/TransLiter/__init__.py
--rw-r--r--   0 hoyeolkim   (501) staff       (20)     3264 2023-04-07 00:09:21.000000 TransLiter-0.0.1/TransLiter/jp_list.py
--rw-r--r--   0 hoyeolkim   (501) staff       (20)     1892 2023-04-07 00:09:21.000000 TransLiter-0.0.1/TransLiter/ko_jamo.py
--rw-r--r--   0 hoyeolkim   (501) staff       (20)     1051 2023-04-07 03:03:01.000000 TransLiter-0.0.1/TransLiter/transliter_jp.py
--rw-r--r--   0 hoyeolkim   (501) staff       (20)      680 2023-04-07 03:03:00.000000 TransLiter-0.0.1/TransLiter/transliter_ko.py
-drwxr-xr-x   0 hoyeolkim   (501) staff       (20)        0 2023-04-07 03:52:19.780662 TransLiter-0.0.1/TransLiter.egg-info/
--rw-r--r--   0 hoyeolkim   (501) staff       (20)     1896 2023-04-07 03:52:19.000000 TransLiter-0.0.1/TransLiter.egg-info/PKG-INFO
--rw-r--r--   0 hoyeolkim   (501) staff       (20)      351 2023-04-07 03:52:19.000000 TransLiter-0.0.1/TransLiter.egg-info/SOURCES.txt
--rw-r--r--   0 hoyeolkim   (501) staff       (20)        1 2023-04-07 03:52:19.000000 TransLiter-0.0.1/TransLiter.egg-info/dependency_links.txt
--rw-r--r--   0 hoyeolkim   (501) staff       (20)        1 2023-04-07 03:52:19.000000 TransLiter-0.0.1/TransLiter.egg-info/not-zip-safe
--rw-r--r--   0 hoyeolkim   (501) staff       (20)        9 2023-04-07 03:52:19.000000 TransLiter-0.0.1/TransLiter.egg-info/requires.txt
--rw-r--r--   0 hoyeolkim   (501) staff       (20)       11 2023-04-07 03:52:19.000000 TransLiter-0.0.1/TransLiter.egg-info/top_level.txt
--rw-r--r--   0 hoyeolkim   (501) staff       (20)       38 2023-04-07 03:52:19.781022 TransLiter-0.0.1/setup.cfg
--rw-r--r--   0 hoyeolkim   (501) staff       (20)      627 2023-04-07 03:51:57.000000 TransLiter-0.0.1/setup.py
+drwxr-xr-x   0 hoyeolkim   (501) staff       (20)        0 2023-04-07 03:56:32.014579 TransLiter-0.0.2/
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)     1067 2023-04-07 00:09:21.000000 TransLiter-0.0.2/LICENSE
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)     1896 2023-04-07 03:56:32.014455 TransLiter-0.0.2/PKG-INFO
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)     1548 2023-04-07 03:11:49.000000 TransLiter-0.0.2/README.md
+drwxr-xr-x   0 hoyeolkim   (501) staff       (20)        0 2023-04-07 03:56:32.013387 TransLiter-0.0.2/TransLiter/
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)        0 2023-04-07 03:16:39.000000 TransLiter-0.0.2/TransLiter/__init__.py
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)     3264 2023-04-07 00:09:21.000000 TransLiter-0.0.2/TransLiter/jp_list.py
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)     1892 2023-04-07 00:09:21.000000 TransLiter-0.0.2/TransLiter/ko_jamo.py
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)     1051 2023-04-07 03:03:01.000000 TransLiter-0.0.2/TransLiter/transliter_jp.py
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)      691 2023-04-07 03:56:03.000000 TransLiter-0.0.2/TransLiter/transliter_ko.py
+drwxr-xr-x   0 hoyeolkim   (501) staff       (20)        0 2023-04-07 03:56:32.014250 TransLiter-0.0.2/TransLiter.egg-info/
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)     1896 2023-04-07 03:56:31.000000 TransLiter-0.0.2/TransLiter.egg-info/PKG-INFO
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)      351 2023-04-07 03:56:31.000000 TransLiter-0.0.2/TransLiter.egg-info/SOURCES.txt
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)        1 2023-04-07 03:56:31.000000 TransLiter-0.0.2/TransLiter.egg-info/dependency_links.txt
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)        1 2023-04-07 03:52:19.000000 TransLiter-0.0.2/TransLiter.egg-info/not-zip-safe
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)        9 2023-04-07 03:56:31.000000 TransLiter-0.0.2/TransLiter.egg-info/requires.txt
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)       11 2023-04-07 03:56:31.000000 TransLiter-0.0.2/TransLiter.egg-info/top_level.txt
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)       38 2023-04-07 03:56:32.014619 TransLiter-0.0.2/setup.cfg
+-rw-r--r--   0 hoyeolkim   (501) staff       (20)      627 2023-04-07 03:55:37.000000 TransLiter-0.0.2/setup.py
```

### Comparing `TransLiter-0.0.1/LICENSE` & `TransLiter-0.0.2/LICENSE`

 * *Files identical despite different names*

### Comparing `TransLiter-0.0.1/PKG-INFO` & `TransLiter-0.0.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: TransLiter
-Version: 0.0.1
+Version: 0.0.2
 Summary: TransLiter transliterates multilingual text to English.
 Home-page: https://github.com/elibooklover/TransLiter
 Author: Hoyeol Kim
 Author-email: elibooklover@gmail.com
 License: MIT
 Platform: UNKNOWN
 Requires-Python: >=3.6
```

### Comparing `TransLiter-0.0.1/README.md` & `TransLiter-0.0.2/README.md`

 * *Files identical despite different names*

### Comparing `TransLiter-0.0.1/TransLiter/jp_list.py` & `TransLiter-0.0.2/TransLiter/jp_list.py`

 * *Files identical despite different names*

### Comparing `TransLiter-0.0.1/TransLiter/ko_jamo.py` & `TransLiter-0.0.2/TransLiter/ko_jamo.py`

 * *Files identical despite different names*

### Comparing `TransLiter-0.0.1/TransLiter/transliter_jp.py` & `TransLiter-0.0.2/TransLiter/transliter_jp.py`

 * *Files identical despite different names*

### Comparing `TransLiter-0.0.1/TransLiter/transliter_ko.py` & `TransLiter-0.0.2/TransLiter/transliter_ko.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,8 +1,8 @@
-from ko_jamo import *
+from TransLiter.ko_jamo import *
 
 def ko(text):
     text = convert(text)
     syllables = list(text)
     transliterated_syllables = []
     for syllable in syllables:
         transliterated_syllable = ''
```

### Comparing `TransLiter-0.0.1/TransLiter.egg-info/PKG-INFO` & `TransLiter-0.0.2/TransLiter.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: TransLiter
-Version: 0.0.1
+Version: 0.0.2
 Summary: TransLiter transliterates multilingual text to English.
 Home-page: https://github.com/elibooklover/TransLiter
 Author: Hoyeol Kim
 Author-email: elibooklover@gmail.com
 License: MIT
 Platform: UNKNOWN
 Requires-Python: >=3.6
```

### Comparing `TransLiter-0.0.1/setup.py` & `TransLiter-0.0.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup
 
 with open("README.md", "r", encoding="utf-8") as f:
     long_description = f.read()
 
 setup(name='TransLiter',
     python_requires='>=3.6',
-    version='0.0.1',
+    version='0.0.2',
     url='https://github.com/elibooklover/TransLiter',
     license='MIT',
     author='Hoyeol Kim',
     author_email='elibooklover@gmail.com',
     description='TransLiter transliterates multilingual text to English.',
     packages=['TransLiter', ],
     long_description=long_description,
```

