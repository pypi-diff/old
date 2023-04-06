# Comparing `tmp/rickled-0.3.1.tar.gz` & `tmp/rickled-0.3.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist\rickled-0.3.1.tar", last modified: Sun Apr  2 21:26:56 2023, max compression
+gzip compressed data, was "dist\rickled-0.3.2.tar", last modified: Thu Apr  6 22:05:10 2023, max compression
```

## Comparing `rickled-0.3.1.tar` & `rickled-0.3.2.tar`

### file list

```diff
@@ -1,24 +1,24 @@
-drwxrwxrwx   0        0        0        0 2023-04-02 21:26:56.000000 rickled-0.3.1/
--rw-rw-rw-   0        0        0    11357 2021-12-06 14:18:08.000000 rickled-0.3.1/LICENSE
--rw-rw-rw-   0        0        0     6448 2023-04-02 21:26:56.000000 rickled-0.3.1/PKG-INFO
--rw-rw-rw-   0        0        0     7051 2022-08-15 15:51:56.000000 rickled-0.3.1/README.md
-drwxrwxrwx   0        0        0        0 2023-04-02 21:26:56.000000 rickled-0.3.1/rickled/
--rw-rw-rw-   0        0        0    50013 2023-04-02 21:25:40.000000 rickled-0.3.1/rickled/__init__.py
--rw-rw-rw-   0        0        0       48 2023-04-02 21:26:55.000000 rickled-0.3.1/rickled/__version__.py
-drwxrwxrwx   0        0        0        0 2023-04-02 21:26:56.000000 rickled-0.3.1/rickled.egg-info/
--rw-rw-rw-   0        0        0     6448 2023-04-02 21:26:55.000000 rickled-0.3.1/rickled.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      420 2023-04-02 21:26:55.000000 rickled-0.3.1/rickled.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-02 21:26:55.000000 rickled-0.3.1/rickled.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2023-04-02 21:26:55.000000 rickled-0.3.1/rickled.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0       16 2023-04-02 21:26:55.000000 rickled-0.3.1/rickled.egg-info/requires.txt
--rw-rw-rw-   0        0        0       14 2023-04-02 21:26:55.000000 rickled-0.3.1/rickled.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       95 2023-04-02 21:26:56.000000 rickled-0.3.1/setup.cfg
--rw-rw-rw-   0        0        0     2010 2023-02-15 17:06:58.000000 rickled-0.3.1/setup.py
-drwxrwxrwx   0        0        0        0 2023-04-02 21:26:56.000000 rickled-0.3.1/tests/
-drwxrwxrwx   0        0        0        0 2023-04-02 21:26:56.000000 rickled-0.3.1/tests/integration/
--rw-rw-rw-   0        0        0        0 2021-12-06 14:18:08.000000 rickled-0.3.1/tests/integration/__init__.py
-drwxrwxrwx   0        0        0        0 2023-04-02 21:26:56.000000 rickled-0.3.1/tests/unittest/
--rw-rw-rw-   0        0        0        0 2022-03-13 15:27:46.000000 rickled-0.3.1/tests/unittest/__init__.py
--rw-rw-rw-   0        0        0     6898 2023-04-02 21:25:40.000000 rickled-0.3.1/tests/unittest/test_advanced.py
--rw-rw-rw-   0        0        0     1717 2023-01-18 22:01:25.000000 rickled-0.3.1/tests/unittest/test_object_rickler.py
--rw-rw-rw-   0        0        0    10648 2023-04-02 21:25:40.000000 rickled-0.3.1/tests/unittest/test_rickle.py
+drwxrwxrwx   0        0        0        0 2023-04-06 22:05:10.000000 rickled-0.3.2/
+-rw-rw-rw-   0        0        0    11357 2021-12-06 14:18:08.000000 rickled-0.3.2/LICENSE
+-rw-rw-rw-   0        0        0     6448 2023-04-06 22:05:10.000000 rickled-0.3.2/PKG-INFO
+-rw-rw-rw-   0        0        0     7051 2022-08-15 15:51:56.000000 rickled-0.3.2/README.md
+drwxrwxrwx   0        0        0        0 2023-04-06 22:05:10.000000 rickled-0.3.2/rickled/
+-rw-rw-rw-   0        0        0    50289 2023-04-06 21:36:35.000000 rickled-0.3.2/rickled/__init__.py
+-rw-rw-rw-   0        0        0       48 2023-04-06 22:05:09.000000 rickled-0.3.2/rickled/__version__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 22:05:10.000000 rickled-0.3.2/rickled.egg-info/
+-rw-rw-rw-   0        0        0     6448 2023-04-06 22:05:10.000000 rickled-0.3.2/rickled.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      420 2023-04-06 22:05:10.000000 rickled-0.3.2/rickled.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 22:05:10.000000 rickled-0.3.2/rickled.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2023-04-06 22:05:10.000000 rickled-0.3.2/rickled.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0       16 2023-04-06 22:05:10.000000 rickled-0.3.2/rickled.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       14 2023-04-06 22:05:10.000000 rickled-0.3.2/rickled.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       95 2023-04-06 22:05:10.000000 rickled-0.3.2/setup.cfg
+-rw-rw-rw-   0        0        0     2010 2023-02-15 17:06:58.000000 rickled-0.3.2/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 22:05:10.000000 rickled-0.3.2/tests/
+drwxrwxrwx   0        0        0        0 2023-04-06 22:05:10.000000 rickled-0.3.2/tests/integration/
+-rw-rw-rw-   0        0        0        0 2021-12-06 14:18:08.000000 rickled-0.3.2/tests/integration/__init__.py
+drwxrwxrwx   0        0        0        0 2023-04-06 22:05:10.000000 rickled-0.3.2/tests/unittest/
+-rw-rw-rw-   0        0        0        0 2022-03-13 15:27:46.000000 rickled-0.3.2/tests/unittest/__init__.py
+-rw-rw-rw-   0        0        0     7819 2023-04-06 21:55:53.000000 rickled-0.3.2/tests/unittest/test_advanced.py
+-rw-rw-rw-   0        0        0     1717 2023-01-18 22:01:25.000000 rickled-0.3.2/tests/unittest/test_object_rickler.py
+-rw-rw-rw-   0        0        0    10648 2023-04-02 21:25:40.000000 rickled-0.3.2/tests/unittest/test_rickle.py
```

### Comparing `rickled-0.3.1/LICENSE` & `rickled-0.3.2/LICENSE`

 * *Files identical despite different names*

### Comparing `rickled-0.3.1/PKG-INFO` & `rickled-0.3.2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rickled
-Version: 0.3.1
+Version: 0.3.2
 Summary: Tools for pickling Python objects in completely different way
 Home-page: https://github.com/Zipfian-Science/rickled
 Author: Zipfian Science
 Author-email: about@zipfian.science
 License: Apache 2.0
 Download-URL: https://github.com/Zipfian-Science/rickled/archive/v_01.tar.gz
 Keywords: Pickle,Python
@@ -153,12 +153,12 @@
 
 >> config.BASIC.callable_lambda()
 'hell world!'
 ```
 
 ## Release
 
-- Date: 2023-04-02
-- Version: 0.3.1
+- Date: 2023-04-07
+- Version: 0.3.2
```

### Comparing `rickled-0.3.1/README.md` & `rickled-0.3.2/README.md`

 * *Files identical despite different names*

### Comparing `rickled-0.3.1/rickled/__init__.py` & `rickled-0.3.2/rickled/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -811,15 +811,20 @@
         """
         d = dict()
         for key, value in self.__dict__.items():
             if self.__eval_name(key):
                 continue
             if serialised and key in self.__meta_info.keys():
                 d[key] = self.__meta_info[key]
-            elif key in self.__meta_info.keys() and self.__meta_info[key]['type'] in ['function', 'lambda', 'class_definition']:
+            elif key in self.__meta_info.keys() and \
+                    self.__meta_info[key]['type'] in ['function', 'lambda', 'class_definition']:
+                d[key] = self.__meta_info[key]
+            elif key in self.__meta_info.keys() and \
+                    self.__meta_info[key]['type'] in ['from_file', 'html_page', 'api_json'] and \
+                    self.__meta_info[key]['hot_load']:
                 d[key] = self.__meta_info[key]
             elif isinstance(value, BaseRickle):
                 d[key] = value.dict(serialised=serialised)
             elif isinstance(value, list):
                 new_list = list()
                 for element in value:
                     if isinstance(element, BaseRickle):
```

### Comparing `rickled-0.3.1/rickled.egg-info/PKG-INFO` & `rickled-0.3.2/rickled.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rickled
-Version: 0.3.1
+Version: 0.3.2
 Summary: Tools for pickling Python objects in completely different way
 Home-page: https://github.com/Zipfian-Science/rickled
 Author: Zipfian Science
 Author-email: about@zipfian.science
 License: Apache 2.0
 Download-URL: https://github.com/Zipfian-Science/rickled/archive/v_01.tar.gz
 Keywords: Pickle,Python
@@ -153,12 +153,12 @@
 
 >> config.BASIC.callable_lambda()
 'hell world!'
 ```
 
 ## Release
 
-- Date: 2023-04-02
-- Version: 0.3.1
+- Date: 2023-04-07
+- Version: 0.3.2
```

### Comparing `rickled-0.3.1/setup.py` & `rickled-0.3.2/setup.py`

 * *Files identical despite different names*

### Comparing `rickled-0.3.1/tests/unittest/test_advanced.py` & `rickled-0.3.2/tests/unittest/test_advanced.py`

 * *Files 5% similar despite different names*

```diff
@@ -205,27 +205,36 @@
 
         r = Rickle(s)
 
         observed = r.random_joke()
 
         self.assertTrue(isinstance(observed, Rickle))
 
+        d = r.dict()
+
+        self.assertTrue(isinstance(d['random_joke'], dict))
+
         s = """
 random_joke:
   type: api_json
   url: https://official-joke-api.appspot.com/random_joke
   expected_http_status: 200
   load_as_rick: true
   deep: true
         """
 
         r = Rickle(s)
 
         self.assertTrue(isinstance(r.random_joke, Rickle))
 
+
+        d = r.dict()
+
+        self.assertTrue(isinstance(d['random_joke'], dict))
+
     def test_hot_load_html(self):
 
         s = """
 page:
     type: html_page
     url: https://zipfian.science
     expected_http_status: 200
@@ -234,14 +243,18 @@
 
         r = Rickle(s)
 
         observed = r.page()
 
         self.assertTrue(isinstance(observed, str))
 
+        d = r.dict()
+
+        self.assertTrue(isinstance(d['page'], dict))
+
         s = """
 page:
     type: html_page
     url: https://zipfian.science
     expected_http_status: 200
         """
 
@@ -257,30 +270,67 @@
                         'hot_load' : False
                     }
 
         actual_meta = r.meta('page')
 
         self.assertDictEqual(expected_meta, actual_meta)
 
+        d = r.dict()
+
+        self.assertTrue(isinstance(d['page'], str))
+
     def test_hot_load_file(self):
         s = """
 another_rick:
    type: from_file
    file_path: './tests/placebos/test_config.json'
    hot_load: true
         """
 
         r = Rickle(s)
 
         observed = r.another_rick()
 
         self.assertTrue(isinstance(observed, str))
 
+        d = r.dict()
+
+        self.assertTrue(isinstance(d['another_rick'], dict))
+
         s = """
 another_rick:
    type: from_file
    file_path: './tests/placebos/test_config.json'
         """
 
         r = Rickle(s)
 
-        self.assertTrue(isinstance(r.another_rick, str))
+        self.assertTrue(isinstance(r.another_rick, str))
+
+        d = r.dict()
+
+        self.assertTrue(isinstance(d['another_rick'], str))
+
+    def test_serialise_list(self):
+
+        s = """
+BASICS:
+    text: test
+    dictionary:
+        one: value
+        two: value
+    number: 2
+    list:
+        - one
+        - two
+        - four
+        - name: John
+          age: 20
+        """
+
+        r = Rickle(s, deep=True)
+
+        self.assertTrue(isinstance(r.BASICS.list[-1], Rickle))
+
+        d = r.dict()
+
+        self.assertTrue(isinstance(d['BASICS']['list'][-1], dict))
```

### Comparing `rickled-0.3.1/tests/unittest/test_object_rickler.py` & `rickled-0.3.2/tests/unittest/test_object_rickler.py`

 * *Files identical despite different names*

### Comparing `rickled-0.3.1/tests/unittest/test_rickle.py` & `rickled-0.3.2/tests/unittest/test_rickle.py`

 * *Files identical despite different names*

