# Comparing `tmp/eqator-2.6.0.tar.gz` & `tmp/eqator-2.7.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "eqator-2.6.0.tar", last modified: Tue Oct 25 09:48:58 2022, max compression
+gzip compressed data, was "eqator-2.7.0.tar", last modified: Thu Apr  6 12:53:01 2023, max compression
```

## Comparing `eqator-2.6.0.tar` & `eqator-2.7.0.tar`

### file list

```diff
@@ -1,46 +1,46 @@
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.442805 eqator-2.6.0/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       27 2022-10-25 09:48:58.000000 eqator-2.6.0/MANIFEST.in
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     7650 2022-10-25 09:48:58.442673 eqator-2.6.0/PKG-INFO
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.438028 eqator-2.6.0/eqator/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       27 2022-08-16 10:34:10.000000 eqator-2.6.0/eqator/MANIFEST.in
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     6947 2022-10-25 09:48:15.000000 eqator-2.6.0/eqator/README.md
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-08-16 10:34:10.000000 eqator-2.6.0/eqator/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.441457 eqator-2.6.0/eqator/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      155 2022-08-16 11:00:50.000000 eqator-2.6.0/eqator/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     5075 2022-10-24 14:34:05.000000 eqator-2.6.0/eqator/__pycache__/checks.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      315 2022-09-22 15:09:50.000000 eqator-2.6.0/eqator/__pycache__/colors.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1740 2022-10-24 14:34:05.000000 eqator-2.6.0/eqator/__pycache__/constants.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2589 2022-10-24 14:32:31.000000 eqator-2.6.0/eqator/__pycache__/helpers.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     3313 2022-10-24 14:10:50.000000 eqator-2.6.0/eqator/__pycache__/main.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       87 2022-08-16 10:34:10.000000 eqator-2.6.0/eqator/apps.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     6461 2022-10-25 09:48:15.000000 eqator-2.6.0/eqator/checks.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      159 2022-09-22 15:08:59.000000 eqator-2.6.0/eqator/colors.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1635 2022-10-25 09:48:15.000000 eqator-2.6.0/eqator/constants.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2038 2022-10-25 09:48:15.000000 eqator-2.6.0/eqator/helpers.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     5062 2022-10-25 09:48:15.000000 eqator-2.6.0/eqator/main.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.441556 eqator-2.6.0/eqator/management/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-08-16 10:34:10.000000 eqator-2.6.0/eqator/management/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.441648 eqator-2.6.0/eqator/management/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      166 2022-08-16 11:00:50.000000 eqator-2.6.0/eqator/management/__pycache__/__init__.cpython-38.pyc
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.441843 eqator-2.6.0/eqator/management/commands/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-08-16 10:34:10.000000 eqator-2.6.0/eqator/management/commands/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.442056 eqator-2.6.0/eqator/management/commands/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      175 2022-08-16 11:00:50.000000 eqator-2.6.0/eqator/management/commands/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2245 2022-10-20 01:43:14.000000 eqator-2.6.0/eqator/management/commands/__pycache__/qa.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2929 2022-09-30 15:02:11.000000 eqator-2.6.0/eqator/management/commands/qa.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.442242 eqator-2.6.0/eqator/services/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-09-22 15:08:59.000000 eqator-2.6.0/eqator/services/__init__.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.442475 eqator-2.6.0/eqator/services/__pycache__/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      164 2022-09-22 15:09:50.000000 eqator-2.6.0/eqator/services/__pycache__/__init__.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      935 2022-09-22 15:09:50.000000 eqator-2.6.0/eqator/services/__pycache__/send.cpython-38.pyc
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)      592 2022-09-22 15:08:59.000000 eqator-2.6.0/eqator/services/send.py
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1342 2022-10-25 09:48:15.000000 eqator-2.6.0/eqator/setup.py
-drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2022-10-25 09:48:58.440821 eqator-2.6.0/eqator.egg-info/
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     7650 2022-10-25 09:48:58.000000 eqator-2.6.0/eqator.egg-info/PKG-INFO
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1049 2022-10-25 09:48:58.000000 eqator-2.6.0/eqator.egg-info/SOURCES.txt
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        1 2022-10-25 09:48:58.000000 eqator-2.6.0/eqator.egg-info/dependency_links.txt
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        1 2022-10-25 09:48:58.000000 eqator-2.6.0/eqator.egg-info/not-zip-safe
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       93 2022-10-25 09:48:58.000000 eqator-2.6.0/eqator.egg-info/requires.txt
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)        7 2022-10-25 09:48:58.000000 eqator-2.6.0/eqator.egg-info/top_level.txt
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)       38 2022-10-25 09:48:58.442849 eqator-2.6.0/setup.cfg
--rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1342 2022-10-25 09:48:58.000000 eqator-2.6.0/setup.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.821438 eqator-2.7.0/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       27 2023-04-06 12:53:01.000000 eqator-2.7.0/MANIFEST.in
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     7650 2023-04-06 12:53:01.821299 eqator-2.7.0/PKG-INFO
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.818907 eqator-2.7.0/eqator/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       27 2022-08-16 10:34:10.000000 eqator-2.7.0/eqator/MANIFEST.in
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     6947 2022-10-25 09:48:15.000000 eqator-2.7.0/eqator/README.md
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-08-16 10:34:10.000000 eqator-2.7.0/eqator/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.820098 eqator-2.7.0/eqator/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      155 2022-08-16 11:00:50.000000 eqator-2.7.0/eqator/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     5075 2022-10-24 14:34:05.000000 eqator-2.7.0/eqator/__pycache__/checks.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      315 2022-09-22 15:09:50.000000 eqator-2.7.0/eqator/__pycache__/colors.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1740 2022-10-24 14:34:05.000000 eqator-2.7.0/eqator/__pycache__/constants.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2589 2022-10-24 14:32:31.000000 eqator-2.7.0/eqator/__pycache__/helpers.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     3313 2022-10-24 14:10:50.000000 eqator-2.7.0/eqator/__pycache__/main.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       87 2022-08-16 10:34:10.000000 eqator-2.7.0/eqator/apps.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     6461 2022-10-25 09:48:15.000000 eqator-2.7.0/eqator/checks.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      159 2022-09-22 15:08:59.000000 eqator-2.7.0/eqator/colors.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1635 2022-10-25 09:48:15.000000 eqator-2.7.0/eqator/constants.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2038 2022-10-25 09:48:15.000000 eqator-2.7.0/eqator/helpers.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     5062 2022-10-25 09:48:15.000000 eqator-2.7.0/eqator/main.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.820198 eqator-2.7.0/eqator/management/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-08-16 10:34:10.000000 eqator-2.7.0/eqator/management/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.820276 eqator-2.7.0/eqator/management/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      166 2022-08-16 11:00:50.000000 eqator-2.7.0/eqator/management/__pycache__/__init__.cpython-38.pyc
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.820448 eqator-2.7.0/eqator/management/commands/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-08-16 10:34:10.000000 eqator-2.7.0/eqator/management/commands/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.820650 eqator-2.7.0/eqator/management/commands/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      175 2022-08-16 11:00:50.000000 eqator-2.7.0/eqator/management/commands/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2245 2022-10-20 01:43:14.000000 eqator-2.7.0/eqator/management/commands/__pycache__/qa.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     2929 2022-09-30 15:02:11.000000 eqator-2.7.0/eqator/management/commands/qa.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.820831 eqator-2.7.0/eqator/services/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        0 2022-09-22 15:08:59.000000 eqator-2.7.0/eqator/services/__init__.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.821114 eqator-2.7.0/eqator/services/__pycache__/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      164 2022-09-22 15:09:50.000000 eqator-2.7.0/eqator/services/__pycache__/__init__.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      935 2022-09-22 15:09:50.000000 eqator-2.7.0/eqator/services/__pycache__/send.cpython-38.pyc
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)      664 2023-04-06 11:01:46.000000 eqator-2.7.0/eqator/services/send.py
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1342 2023-04-06 12:51:38.000000 eqator-2.7.0/eqator/setup.py
+drwxr-xr-x   0 viktoriaresetova   (501) staff       (20)        0 2023-04-06 12:53:01.819506 eqator-2.7.0/eqator.egg-info/
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     7650 2023-04-06 12:53:01.000000 eqator-2.7.0/eqator.egg-info/PKG-INFO
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1049 2023-04-06 12:53:01.000000 eqator-2.7.0/eqator.egg-info/SOURCES.txt
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        1 2023-04-06 12:53:01.000000 eqator-2.7.0/eqator.egg-info/dependency_links.txt
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        1 2023-04-06 12:53:01.000000 eqator-2.7.0/eqator.egg-info/not-zip-safe
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       93 2023-04-06 12:53:01.000000 eqator-2.7.0/eqator.egg-info/requires.txt
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)        7 2023-04-06 12:53:01.000000 eqator-2.7.0/eqator.egg-info/top_level.txt
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)       38 2023-04-06 12:53:01.821487 eqator-2.7.0/setup.cfg
+-rw-r--r--   0 viktoriaresetova   (501) staff       (20)     1342 2023-04-06 12:53:01.000000 eqator-2.7.0/setup.py
```

### Comparing `eqator-2.6.0/PKG-INFO` & `eqator-2.7.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eqator
-Version: 2.6.0
+Version: 2.7.0
 Summary: Checking the Django project for quality
 Home-page: https://github.com/garpixcms/eqator
 Author: Garpix LTD
 Author-email: info@garpix.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Web Environment
```

### Comparing `eqator-2.6.0/eqator/README.md` & `eqator-2.7.0/eqator/README.md`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/__pycache__/checks.cpython-38.pyc` & `eqator-2.7.0/eqator/__pycache__/checks.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/__pycache__/constants.cpython-38.pyc` & `eqator-2.7.0/eqator/__pycache__/constants.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/__pycache__/helpers.cpython-38.pyc` & `eqator-2.7.0/eqator/__pycache__/helpers.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/__pycache__/main.cpython-38.pyc` & `eqator-2.7.0/eqator/__pycache__/main.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/checks.py` & `eqator-2.7.0/eqator/checks.py`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/constants.py` & `eqator-2.7.0/eqator/constants.py`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/helpers.py` & `eqator-2.7.0/eqator/helpers.py`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/main.py` & `eqator-2.7.0/eqator/main.py`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/management/commands/__pycache__/qa.cpython-38.pyc` & `eqator-2.7.0/eqator/management/commands/__pycache__/qa.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/management/commands/qa.py` & `eqator-2.7.0/eqator/management/commands/qa.py`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/services/__pycache__/send.cpython-38.pyc` & `eqator-2.7.0/eqator/services/__pycache__/send.cpython-38.pyc`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/eqator/services/send.py` & `eqator-2.7.0/eqator/services/send.py`

 * *Files 22% similar despite different names*

```diff
@@ -10,12 +10,13 @@
     def report(self, *args, **kwargs):
         url_base = self.url_base
         if url_base is None:
             raise ValueError('To send, set EQATOR_SEND_HOST')
         json_data = json.dumps({
             'data': kwargs
         }, indent=4, sort_keys=True, default=str)
-        r = requests.post(url_base, data=json_data)
+        headers = {'Content-type': 'application/json'}
+        r = requests.post(url_base, data=json_data, headers=headers)
         print_default(f'Send status - {r.status_code}\n')
 
 
 send_service = SendService()
```

### Comparing `eqator-2.6.0/eqator/setup.py` & `eqator-2.7.0/eqator/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 here = path.join(path.abspath(path.dirname(__file__)), 'eqator')
 
 with open(path.join(here, 'README.md'), encoding='utf-8') as f:
     long_description = f.read()
 
 setup(
     name='eqator',
-    version='2.6.0',
+    version='2.7.0',
     description='Checking the Django project for quality',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/garpixcms/eqator',
     author='Garpix LTD',
     author_email='info@garpix.com',
     license='MIT',
```

### Comparing `eqator-2.6.0/eqator.egg-info/PKG-INFO` & `eqator-2.7.0/eqator.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eqator
-Version: 2.6.0
+Version: 2.7.0
 Summary: Checking the Django project for quality
 Home-page: https://github.com/garpixcms/eqator
 Author: Garpix LTD
 Author-email: info@garpix.com
 License: MIT
 Classifier: Development Status :: 4 - Beta
 Classifier: Environment :: Web Environment
```

### Comparing `eqator-2.6.0/eqator.egg-info/SOURCES.txt` & `eqator-2.7.0/eqator.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `eqator-2.6.0/setup.py` & `eqator-2.7.0/setup.py`

 * *Files 8% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 here = path.join(path.abspath(path.dirname(__file__)), 'eqator')
 
 with open(path.join(here, 'README.md'), encoding='utf-8') as f:
     long_description = f.read()
 
 setup(
     name='eqator',
-    version='2.6.0',
+    version='2.7.0',
     description='Checking the Django project for quality',
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/garpixcms/eqator',
     author='Garpix LTD',
     author_email='info@garpix.com',
     license='MIT',
```

