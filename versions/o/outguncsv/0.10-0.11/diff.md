# Comparing `tmp/outguncsv-0.10.tar.gz` & `tmp/outguncsv-0.11.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "outguncsv-0.10.tar", last modified: Mon Feb 20 06:08:01 2023, max compression
+gzip compressed data, was "outguncsv-0.11.tar", last modified: Fri Apr  7 12:31:06 2023, max compression
```

## Comparing `outguncsv-0.10.tar` & `outguncsv-0.11.tar`

### file list

```diff
@@ -1,18 +1,18 @@
-drwxrwxrwx   0        0        0        0 2023-02-20 06:08:01.784763 outguncsv-0.10/
--rw-rw-rw-   0        0        0     1148 2023-02-20 06:07:44.000000 outguncsv-0.10/LICENSE.rst
--rw-rw-rw-   0        0        0       98 2023-02-20 06:07:44.000000 outguncsv-0.10/MANIFEST.in
--rw-rw-rw-   0        0        0    12384 2023-02-20 06:08:01.784763 outguncsv-0.10/PKG-INFO
--rw-rw-rw-   0        0        0    11280 2023-02-20 06:06:36.000000 outguncsv-0.10/README.md
-drwxrwxrwx   0        0        0        0 2023-02-20 06:08:01.780855 outguncsv-0.10/outguncsv/
--rw-rw-rw-   0        0        0    11280 2023-02-20 06:06:36.000000 outguncsv-0.10/outguncsv/README.MD
--rw-rw-rw-   0        0        0     6111 2023-02-20 06:04:28.000000 outguncsv-0.10/outguncsv/__init__.py
--rw-rw-rw-   0        0        0       44 2023-02-20 06:08:00.000000 outguncsv-0.10/outguncsv/requirements.txt
--rw-rw-rw-   0        0        0        2 2023-02-20 06:08:00.000000 outguncsv-0.10/outguncsv/thirdparty.json
-drwxrwxrwx   0        0        0        0 2023-02-20 06:08:01.783776 outguncsv-0.10/outguncsv.egg-info/
--rw-rw-rw-   0        0        0    12384 2023-02-20 06:08:01.000000 outguncsv-0.10/outguncsv.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      311 2023-02-20 06:08:01.000000 outguncsv-0.10/outguncsv.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-02-20 06:08:01.000000 outguncsv-0.10/outguncsv.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       42 2023-02-20 06:08:01.000000 outguncsv-0.10/outguncsv.egg-info/requires.txt
--rw-rw-rw-   0        0        0       10 2023-02-20 06:08:01.000000 outguncsv-0.10/outguncsv.egg-info/top_level.txt
--rw-rw-rw-   0        0        0      115 2023-02-20 06:08:01.784763 outguncsv-0.10/setup.cfg
--rw-rw-rw-   0        0        0     1512 2023-02-20 06:08:00.000000 outguncsv-0.10/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 12:31:06.290321 outguncsv-0.11/
+-rw-rw-rw-   0        0        0     1148 2023-04-07 12:31:03.000000 outguncsv-0.11/LICENSE.rst
+-rw-rw-rw-   0        0        0       98 2023-04-07 12:31:02.000000 outguncsv-0.11/MANIFEST.in
+-rw-rw-rw-   0        0        0    12183 2023-04-07 12:31:06.290321 outguncsv-0.11/PKG-INFO
+-rw-rw-rw-   0        0        0    11280 2023-03-27 16:24:16.000000 outguncsv-0.11/README.md
+drwxrwxrwx   0        0        0        0 2023-04-07 12:31:06.284337 outguncsv-0.11/outguncsv/
+-rw-rw-rw-   0        0        0    11280 2023-03-27 16:24:16.000000 outguncsv-0.11/outguncsv/README.MD
+-rw-rw-rw-   0        0        0     6314 2023-04-07 12:22:06.000000 outguncsv-0.11/outguncsv/__init__.py
+-rw-rw-rw-   0        0        0       44 2023-04-07 12:31:05.000000 outguncsv-0.11/outguncsv/requirements.txt
+-rw-rw-rw-   0        0        0    24125 2023-04-07 12:31:05.000000 outguncsv-0.11/outguncsv/thirdparty.json
+drwxrwxrwx   0        0        0        0 2023-04-07 12:31:06.289325 outguncsv-0.11/outguncsv.egg-info/
+-rw-rw-rw-   0        0        0    12183 2023-04-07 12:31:06.000000 outguncsv-0.11/outguncsv.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      311 2023-04-07 12:31:06.000000 outguncsv-0.11/outguncsv.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 12:31:06.000000 outguncsv-0.11/outguncsv.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       42 2023-04-07 12:31:06.000000 outguncsv-0.11/outguncsv.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       10 2023-04-07 12:31:06.000000 outguncsv-0.11/outguncsv.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0      115 2023-04-07 12:31:06.291318 outguncsv-0.11/setup.cfg
+-rw-rw-rw-   0        0        0     1351 2023-04-07 12:31:05.000000 outguncsv-0.11/setup.py
```

### Comparing `outguncsv-0.10/LICENSE.rst` & `outguncsv-0.11/LICENSE.rst`

 * *Files identical despite different names*

### Comparing `outguncsv-0.10/PKG-INFO` & `outguncsv-0.11/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,25 +1,21 @@
 Metadata-Version: 2.1
 Name: outguncsv
-Version: 0.10
+Version: 0.11
 Summary: Finds the right CSV separator and excludes bad lines in corrupt CSV files
 Home-page: https://github.com/hansalemaos/outguncsv
 Author: Johannes Fischer
 Author-email: <aulasparticularesdealemaosp@gmail.com>
 License: MIT
 Keywords: pandas,read_csv,corrupt,csv,numpy
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3 :: Only
-Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
 Classifier: Topic :: Scientific/Engineering :: Visualization
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
-Classifier: Topic :: Text Editors :: Text Processing
-Classifier: Topic :: Text Processing :: General
-Classifier: Topic :: Text Processing :: Indexing
-Classifier: Topic :: Text Processing :: Filters
 Classifier: Topic :: Utilities
 Description-Content-Type: text/markdown
 License-File: LICENSE.rst
 
 
 
 # Finds the right CSV separator and excludes bad lines
```

### Comparing `outguncsv-0.10/README.md` & `outguncsv-0.11/README.md`

 * *Files identical despite different names*

### Comparing `outguncsv-0.10/outguncsv/README.MD` & `outguncsv-0.11/outguncsv/README.MD`

 * *Files identical despite different names*

### Comparing `outguncsv-0.10/outguncsv/__init__.py` & `outguncsv-0.11/outguncsv/__init__.py`

 * *Files 2% similar despite different names*

```diff
@@ -83,20 +83,29 @@
         sora = tuple(sorted([x[1] for x in sora.items()]))[-1]
         alltoga.append((sora, key))
     pros = tuple(sorted(alltoga))[-1][1]
     return pros
 
 
 def _openfile(key):
+
     if os.path.exists(key):
-        with open(key, mode="rb") as f:
-            data = f.read()
+        try:
+            with open(key, mode="rb") as f:
+                data = f.read()
+            return data
+        except Exception as fe:
+            print(fe)
+            return data
     else:
-        with requests.get(url=key) as response:
-            data = response.content
+        try:
+            with requests.get(url=key) as response:
+                data = response.content
+        except Exception as fe:
+            pass
     return data
 
 
 def read_balky_csv_files(
     csvfiles,
     encoding="utf-8",
     sep=None,
```

### Comparing `outguncsv-0.10/outguncsv.egg-info/PKG-INFO` & `outguncsv-0.11/outguncsv.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,25 +1,21 @@
 Metadata-Version: 2.1
 Name: outguncsv
-Version: 0.10
+Version: 0.11
 Summary: Finds the right CSV separator and excludes bad lines in corrupt CSV files
 Home-page: https://github.com/hansalemaos/outguncsv
 Author: Johannes Fischer
 Author-email: <aulasparticularesdealemaosp@gmail.com>
 License: MIT
 Keywords: pandas,read_csv,corrupt,csv,numpy
 Classifier: Development Status :: 4 - Beta
 Classifier: Programming Language :: Python :: 3 :: Only
-Classifier: Programming Language :: Python :: 3.9
+Classifier: Programming Language :: Python :: 3.10
 Classifier: Topic :: Scientific/Engineering :: Visualization
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
-Classifier: Topic :: Text Editors :: Text Processing
-Classifier: Topic :: Text Processing :: General
-Classifier: Topic :: Text Processing :: Indexing
-Classifier: Topic :: Text Processing :: Filters
 Classifier: Topic :: Utilities
 Description-Content-Type: text/markdown
 License-File: LICENSE.rst
 
 
 
 # Finds the right CSV separator and excludes bad lines
```

### Comparing `outguncsv-0.10/setup.py` & `outguncsv-0.11/setup.py`

 * *Files 22% similar despite different names*

```diff
@@ -4,15 +4,15 @@
 
 #change to dict
 here = os.path.abspath(os.path.dirname(__file__))
 
 with codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)),'README.md'), encoding="utf-8") as fh:
     long_description = "\n" + fh.read()
 
-VERSION = '0.10'
+VERSION = '0.11'
 DESCRIPTION = "Finds the right CSV separator and excludes bad lines in corrupt CSV files"
 
 # Setting up
 setup(
     name="outguncsv",
     version=VERSION,
     license='MIT',
@@ -20,13 +20,13 @@
     author="Johannes Fischer",
     author_email="<aulasparticularesdealemaosp@gmail.com>",
     description=DESCRIPTION,
     long_description_content_type="text/markdown",
     long_description=long_description,
     #packages=['pandas', 'regex', 'requests', 'tolerant_isinstance'],
     keywords=['pandas', 'read_csv', 'corrupt', 'csv', 'numpy'],
-    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.9', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Text Editors :: Text Processing', 'Topic :: Text Processing :: General', 'Topic :: Text Processing :: Indexing', 'Topic :: Text Processing :: Filters', 'Topic :: Utilities'],
+    classifiers=['Development Status :: 4 - Beta', 'Programming Language :: Python :: 3 :: Only', 'Programming Language :: Python :: 3.10', 'Topic :: Scientific/Engineering :: Visualization', 'Topic :: Software Development :: Libraries :: Python Modules', 'Topic :: Utilities'],
     install_requires=['pandas', 'regex', 'requests', 'tolerant_isinstance'],
     include_package_data=True
 )
 #python setup.py sdist bdist_wheel
 #twine upload dist/*
```

