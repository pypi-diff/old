# Comparing `tmp/invesytoolbox-0.0.8.tar.gz` & `tmp/invesytoolbox-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/invesytoolbox-0.0.8.tar", last modified: Fri Jul 29 09:55:02 2022, max compression
+gzip compressed data, was "dist/invesytoolbox-0.0.9.tar", last modified: Fri Jul 29 11:01:19 2022, max compression
```

## Comparing `invesytoolbox-0.0.8.tar` & `invesytoolbox-0.0.9.tar`

### file list

```diff
@@ -1,31 +1,31 @@
-drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 09:55:02.435956 invesytoolbox-0.0.8/
--rw-r--r--   0 georg      (502) staff       (20)     1050 2022-04-20 10:44:14.000000 invesytoolbox-0.0.8/LICENSE.txt
--rw-r--r--   0 georg      (502) staff       (20)     7162 2022-07-29 09:55:02.436165 invesytoolbox-0.0.8/PKG-INFO
--rw-r--r--   0 georg      (502) staff       (20)     5682 2022-07-06 08:00:06.000000 invesytoolbox-0.0.8/README.md
--rw-r--r--   0 georg      (502) staff       (20)      906 2022-07-29 09:55:02.436890 invesytoolbox-0.0.8/setup.cfg
--rw-r--r--   0 georg      (502) staff       (20)       69 2022-06-08 20:27:46.000000 invesytoolbox-0.0.8/setup.py
-drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 09:55:02.417945 invesytoolbox-0.0.8/src/
-drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 09:55:02.426912 invesytoolbox-0.0.8/src/invesytoolbox/
--rw-r--r--   0 georg      (502) staff       (20)      333 2022-07-07 07:39:27.000000 invesytoolbox-0.0.8/src/invesytoolbox/__init__.py
--rw-r--r--   0 georg      (502) staff       (20)     8292 2022-07-07 08:05:50.000000 invesytoolbox-0.0.8/src/invesytoolbox/itb_data.py
--rw-r--r--   0 georg      (502) staff       (20)    11333 2022-07-16 10:36:00.000000 invesytoolbox-0.0.8/src/invesytoolbox/itb_date_time.py
--rw-r--r--   0 georg      (502) staff       (20)     3558 2022-07-28 21:11:21.000000 invesytoolbox-0.0.8/src/invesytoolbox/itb_email_phone.py
--rw-r--r--   0 georg      (502) staff       (20)    11339 2022-07-28 18:54:20.000000 invesytoolbox-0.0.8/src/invesytoolbox/itb_locales.py
--rw-r--r--   0 georg      (502) staff       (20)     1125 2022-07-07 07:22:11.000000 invesytoolbox-0.0.8/src/invesytoolbox/itb_restricted_python.py
--rw-r--r--   0 georg      (502) staff       (20)     3241 2022-07-07 07:20:38.000000 invesytoolbox-0.0.8/src/invesytoolbox/itb_security.py
--rw-r--r--   0 georg      (502) staff       (20)     7457 2022-07-28 21:22:02.000000 invesytoolbox-0.0.8/src/invesytoolbox/itb_text_name.py
--rw-r--r--   0 georg      (502) staff       (20)     1388 2022-07-29 08:52:25.000000 invesytoolbox-0.0.8/src/invesytoolbox/itb_www.py
-drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 09:55:02.430211 invesytoolbox-0.0.8/src/invesytoolbox.egg-info/
--rw-r--r--   0 georg      (502) staff       (20)     7162 2022-07-29 09:55:01.000000 invesytoolbox-0.0.8/src/invesytoolbox.egg-info/PKG-INFO
--rw-r--r--   0 georg      (502) staff       (20)      729 2022-07-29 09:55:02.000000 invesytoolbox-0.0.8/src/invesytoolbox.egg-info/SOURCES.txt
--rw-r--r--   0 georg      (502) staff       (20)        1 2022-07-29 09:55:01.000000 invesytoolbox-0.0.8/src/invesytoolbox.egg-info/dependency_links.txt
--rw-r--r--   0 georg      (502) staff       (20)       96 2022-07-29 09:55:02.000000 invesytoolbox-0.0.8/src/invesytoolbox.egg-info/requires.txt
--rw-r--r--   0 georg      (502) staff       (20)       20 2022-07-29 09:55:02.000000 invesytoolbox-0.0.8/src/invesytoolbox.egg-info/top_level.txt
-drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 09:55:02.435366 invesytoolbox-0.0.8/src/tests/
--rw-r--r--   0 georg      (502) staff       (20)        1 2022-06-09 11:45:01.000000 invesytoolbox-0.0.8/src/tests/__init__.py
--rwxr--r--   0 georg      (502) staff       (20)     5059 2022-07-07 08:04:19.000000 invesytoolbox-0.0.8/src/tests/test_data.py
--rwxr--r--   0 georg      (502) staff       (20)    11394 2022-07-07 08:00:45.000000 invesytoolbox-0.0.8/src/tests/test_date_time.py
--rwxr--r--   0 georg      (502) staff       (20)     1239 2022-07-28 21:11:36.000000 invesytoolbox-0.0.8/src/tests/test_email_phone.py
--rwxr--r--   0 georg      (502) staff       (20)     3541 2022-07-07 08:04:05.000000 invesytoolbox-0.0.8/src/tests/test_locales.py
--rwxr--r--   0 georg      (502) staff       (20)     3723 2022-07-28 21:03:32.000000 invesytoolbox-0.0.8/src/tests/test_text_name.py
--rwxr--r--   0 georg      (502) staff       (20)     2893 2022-07-29 09:00:25.000000 invesytoolbox-0.0.8/src/tests/test_www.py
+drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 11:01:19.110808 invesytoolbox-0.0.9/
+-rw-r--r--   0 georg      (502) staff       (20)     1050 2022-04-20 10:44:14.000000 invesytoolbox-0.0.9/LICENSE.txt
+-rw-r--r--   0 georg      (502) staff       (20)     7254 2022-07-29 11:01:19.111101 invesytoolbox-0.0.9/PKG-INFO
+-rw-r--r--   0 georg      (502) staff       (20)     5682 2022-07-06 08:00:06.000000 invesytoolbox-0.0.9/README.md
+-rw-r--r--   0 georg      (502) staff       (20)      906 2022-07-29 11:01:19.111987 invesytoolbox-0.0.9/setup.cfg
+-rw-r--r--   0 georg      (502) staff       (20)       69 2022-06-08 20:27:46.000000 invesytoolbox-0.0.9/setup.py
+drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 11:01:19.091531 invesytoolbox-0.0.9/src/
+drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 11:01:19.099936 invesytoolbox-0.0.9/src/invesytoolbox/
+-rw-r--r--   0 georg      (502) staff       (20)      333 2022-07-07 07:39:27.000000 invesytoolbox-0.0.9/src/invesytoolbox/__init__.py
+-rw-r--r--   0 georg      (502) staff       (20)     8292 2022-07-07 08:05:50.000000 invesytoolbox-0.0.9/src/invesytoolbox/itb_data.py
+-rw-r--r--   0 georg      (502) staff       (20)    11333 2022-07-16 10:36:00.000000 invesytoolbox-0.0.9/src/invesytoolbox/itb_date_time.py
+-rw-r--r--   0 georg      (502) staff       (20)     3558 2022-07-28 21:11:21.000000 invesytoolbox-0.0.9/src/invesytoolbox/itb_email_phone.py
+-rw-r--r--   0 georg      (502) staff       (20)    11339 2022-07-28 18:54:20.000000 invesytoolbox-0.0.9/src/invesytoolbox/itb_locales.py
+-rw-r--r--   0 georg      (502) staff       (20)     1125 2022-07-07 07:22:11.000000 invesytoolbox-0.0.9/src/invesytoolbox/itb_restricted_python.py
+-rw-r--r--   0 georg      (502) staff       (20)     3241 2022-07-07 07:20:38.000000 invesytoolbox-0.0.9/src/invesytoolbox/itb_security.py
+-rw-r--r--   0 georg      (502) staff       (20)     7457 2022-07-28 21:22:02.000000 invesytoolbox-0.0.9/src/invesytoolbox/itb_text_name.py
+-rw-r--r--   0 georg      (502) staff       (20)     1697 2022-07-29 10:51:22.000000 invesytoolbox-0.0.9/src/invesytoolbox/itb_www.py
+drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 11:01:19.103497 invesytoolbox-0.0.9/src/invesytoolbox.egg-info/
+-rw-r--r--   0 georg      (502) staff       (20)     7254 2022-07-29 11:01:18.000000 invesytoolbox-0.0.9/src/invesytoolbox.egg-info/PKG-INFO
+-rw-r--r--   0 georg      (502) staff       (20)      729 2022-07-29 11:01:19.000000 invesytoolbox-0.0.9/src/invesytoolbox.egg-info/SOURCES.txt
+-rw-r--r--   0 georg      (502) staff       (20)        1 2022-07-29 11:01:18.000000 invesytoolbox-0.0.9/src/invesytoolbox.egg-info/dependency_links.txt
+-rw-r--r--   0 georg      (502) staff       (20)       96 2022-07-29 11:01:18.000000 invesytoolbox-0.0.9/src/invesytoolbox.egg-info/requires.txt
+-rw-r--r--   0 georg      (502) staff       (20)       20 2022-07-29 11:01:18.000000 invesytoolbox-0.0.9/src/invesytoolbox.egg-info/top_level.txt
+drwxr-xr-x   0 georg      (502) staff       (20)        0 2022-07-29 11:01:19.109939 invesytoolbox-0.0.9/src/tests/
+-rw-r--r--   0 georg      (502) staff       (20)        1 2022-06-09 11:45:01.000000 invesytoolbox-0.0.9/src/tests/__init__.py
+-rwxr--r--   0 georg      (502) staff       (20)     5059 2022-07-07 08:04:19.000000 invesytoolbox-0.0.9/src/tests/test_data.py
+-rwxr--r--   0 georg      (502) staff       (20)    11394 2022-07-07 08:00:45.000000 invesytoolbox-0.0.9/src/tests/test_date_time.py
+-rwxr--r--   0 georg      (502) staff       (20)     1239 2022-07-28 21:11:36.000000 invesytoolbox-0.0.9/src/tests/test_email_phone.py
+-rwxr--r--   0 georg      (502) staff       (20)     3541 2022-07-07 08:04:05.000000 invesytoolbox-0.0.9/src/tests/test_locales.py
+-rwxr--r--   0 georg      (502) staff       (20)     3723 2022-07-28 21:03:32.000000 invesytoolbox-0.0.9/src/tests/test_text_name.py
+-rwxr--r--   0 georg      (502) staff       (20)     2974 2022-07-29 10:38:02.000000 invesytoolbox-0.0.9/src/tests/test_www.py
```

### Comparing `invesytoolbox-0.0.8/LICENSE.txt` & `invesytoolbox-0.0.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/PKG-INFO` & `invesytoolbox-0.0.9/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: invesytoolbox
-Version: 0.0.8
+Version: 0.0.9
 Summary: Tools for Python scripts or terminal
 Home-page: https://gitlab.com/Rastaf/invesytoolbox
 Author: Georg Pfolz
 Author-email: georg.pfolz@invesy.at
 License: MIT License
 Project-URL: Bug Tracker, https://gitlab.com/Rastaf/invesytoolbox/-/issues
 Platform: UNKNOWN
@@ -133,14 +133,17 @@
 	ü --> ue
 	ß --> ss
 	```
 
 - **sort_word_list**: Sort a list of words using map\_special\_chars.
 
 # History
+## 0.0.9
+*change\_query\_string* respects Zope parameter converters (like `paramname:int`)
+
 ## 0.0.8
 * New submodule www
    * *change\_query\_string*
 
 ## 0.0.7
 * shorter submodule names (no _tools suffix)
 * *is_holiday* works without argument
```

### Comparing `invesytoolbox-0.0.8/README.md` & `invesytoolbox-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/setup.cfg` & `invesytoolbox-0.0.9/setup.cfg`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = invesytoolbox
-version = 0.0.8
+version = 0.0.9
 author = Georg Pfolz
 author_email = georg.pfolz@invesy.at
 description = Tools for Python scripts or terminal
 long_description = file: README.md,HISTORY.md
 long_description_content_type = text/markdown
 license = MIT License
 license_files = LICENSE.txt
```

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox/itb_data.py` & `invesytoolbox-0.0.9/src/invesytoolbox/itb_data.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox/itb_date_time.py` & `invesytoolbox-0.0.9/src/invesytoolbox/itb_date_time.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox/itb_email_phone.py` & `invesytoolbox-0.0.9/src/invesytoolbox/itb_email_phone.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox/itb_locales.py` & `invesytoolbox-0.0.9/src/invesytoolbox/itb_locales.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox/itb_restricted_python.py` & `invesytoolbox-0.0.9/src/invesytoolbox/itb_restricted_python.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox/itb_security.py` & `invesytoolbox-0.0.9/src/invesytoolbox/itb_security.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox/itb_text_name.py` & `invesytoolbox-0.0.9/src/invesytoolbox/itb_text_name.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox/itb_www.py` & `invesytoolbox-0.0.9/src/invesytoolbox/itb_www.py`

 * *Files 17% similar despite different names*

```diff
@@ -2,14 +2,28 @@
 """
 ===============
 www_tools
 ===============
 """
 import urllib.parse
 
+zope_data_types = {
+    'boolean',
+    'int',
+    'long',
+    'float',
+    'string',
+    'text',
+    'list',
+    'tuple',
+    'tokens',
+    'lines',
+    ':ignore_empty'
+}
+
 def change_query_string(
     url: str = None,
     query_string: str = None,
     params: dict = None,
     delete_remaining: bool = False,
     returning='auto'
 ):
@@ -39,14 +53,17 @@
 
     if delete_remaining:
         query = params
     else:
         query.update(params)
 
     new_query_string = urllib.parse.urlencode(query)
+    if '%3A' in new_query_string:
+        for typ in zope_data_types:
+            new_query_string = new_query_string.replace(f'%3A{typ}', f':{typ}')
 
     if returning == 'query_string':
         return new_query_string
 
     if returning == 'url':
-        new_url = url_parts._replace(query=urllib.parse.urlencode(query)).geturl()
+        new_url = url_parts._replace(query=new_query_string).geturl()
         return new_url
```

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox.egg-info/PKG-INFO` & `invesytoolbox-0.0.9/src/invesytoolbox.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: invesytoolbox
-Version: 0.0.8
+Version: 0.0.9
 Summary: Tools for Python scripts or terminal
 Home-page: https://gitlab.com/Rastaf/invesytoolbox
 Author: Georg Pfolz
 Author-email: georg.pfolz@invesy.at
 License: MIT License
 Project-URL: Bug Tracker, https://gitlab.com/Rastaf/invesytoolbox/-/issues
 Platform: UNKNOWN
@@ -133,14 +133,17 @@
 	ü --> ue
 	ß --> ss
 	```
 
 - **sort_word_list**: Sort a list of words using map\_special\_chars.
 
 # History
+## 0.0.9
+*change\_query\_string* respects Zope parameter converters (like `paramname:int`)
+
 ## 0.0.8
 * New submodule www
    * *change\_query\_string*
 
 ## 0.0.7
 * shorter submodule names (no _tools suffix)
 * *is_holiday* works without argument
```

### Comparing `invesytoolbox-0.0.8/src/invesytoolbox.egg-info/SOURCES.txt` & `invesytoolbox-0.0.9/src/invesytoolbox.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/tests/test_data.py` & `invesytoolbox-0.0.9/src/tests/test_data.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/tests/test_date_time.py` & `invesytoolbox-0.0.9/src/tests/test_date_time.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/tests/test_email_phone.py` & `invesytoolbox-0.0.9/src/tests/test_email_phone.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/tests/test_locales.py` & `invesytoolbox-0.0.9/src/tests/test_locales.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/tests/test_text_name.py` & `invesytoolbox-0.0.9/src/tests/test_text_name.py`

 * *Files identical despite different names*

### Comparing `invesytoolbox-0.0.8/src/tests/test_www.py` & `invesytoolbox-0.0.9/src/tests/test_www.py`

 * *Files 13% similar despite different names*

```diff
@@ -16,19 +16,20 @@
 change_query_string_data = [
     {
         'url': 'http://qawebsite.com/search?q=question&x=irgendwas',
         'query': 'q=question&x=irgendwas',
         'params': {
             'lang':'en',
             'tag':'python',
-            'q': 'frage'},
-        'new_url': 'http://qawebsite.com/search?q=frage&x=irgendwas&lang=en&tag=python',
-        'new_query': 'q=frage&x=irgendwas&lang=en&tag=python',
-        'new_url_fresh': 'http://qawebsite.com/search?lang=en&tag=python&q=frage',
-        'new_query_fresh': 'lang=en&tag=python&q=frage'
+            'q': 'frage',
+            'nummer:int': 4},
+        'new_url': 'http://qawebsite.com/search?q=frage&x=irgendwas&lang=en&tag=python&nummer:int=4',
+        'new_query': 'q=frage&x=irgendwas&lang=en&tag=python&nummer:int=4',
+        'new_url_fresh': 'http://qawebsite.com/search?lang=en&tag=python&q=frage&nummer:int=4',
+        'new_query_fresh': 'lang=en&tag=python&q=frage&nummer:int=4'
     }
 ]
 
 class TestTextName(unittest.TestCase):
     def test_change_query_string(self):
         for datum in change_query_string_data:
             new_url = change_query_string(
```

