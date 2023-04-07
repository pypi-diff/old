# Comparing `tmp/md2pdf-0.5.tar.gz` & `tmp/md2pdf-0.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/md2pdf-0.5.tar", last modified: Thu Jan 21 20:23:32 2021, max compression
+gzip compressed data, was "md2pdf-0.6.tar", last modified: Fri Apr  7 14:33:47 2023, max compression
```

## Comparing `md2pdf-0.5.tar` & `md2pdf-0.6.tar`

### file list

```diff
@@ -1,26 +1,26 @@
-drwxr-xr-x   0 maupetit  (1000) fun       (5000)        0 2021-01-21 20:23:32.239445 md2pdf-0.5/
--rw-r--r--   0 maupetit  (1000) fun       (5000)     1064 2021-01-21 19:55:29.000000 md2pdf-0.5/LICENSE
--rw-r--r--   0 maupetit  (1000) fun       (5000)      148 2021-01-21 19:55:29.000000 md2pdf-0.5/MANIFEST.in
--rw-r--r--   0 maupetit  (1000) fun       (5000)     1155 2021-01-21 20:23:32.239445 md2pdf-0.5/PKG-INFO
--rw-r--r--   0 maupetit  (1000) fun       (5000)     3467 2021-01-21 19:55:29.000000 md2pdf-0.5/README.md
-drwxr-xr-x   0 maupetit  (1000) fun       (5000)        0 2021-01-21 20:23:32.239445 md2pdf-0.5/md2pdf/
--rw-r--r--   0 maupetit  (1000) fun       (5000)      210 2021-01-21 19:58:56.000000 md2pdf-0.5/md2pdf/__init__.py
--rw-r--r--   0 maupetit  (1000) fun       (5000)     1380 2021-01-21 19:55:29.000000 md2pdf-0.5/md2pdf/core.py
--rw-r--r--   0 maupetit  (1000) fun       (5000)       69 2021-01-21 19:55:29.000000 md2pdf-0.5/md2pdf/exceptions.py
-drwxr-xr-x   0 maupetit  (1000) fun       (5000)        0 2021-01-21 20:23:32.239445 md2pdf-0.5/md2pdf.egg-info/
--rw-r--r--   0 maupetit  (1000) fun       (5000)     1155 2021-01-21 20:23:32.000000 md2pdf-0.5/md2pdf.egg-info/PKG-INFO
--rw-r--r--   0 maupetit  (1000) fun       (5000)      378 2021-01-21 20:23:32.000000 md2pdf-0.5/md2pdf.egg-info/SOURCES.txt
--rw-r--r--   0 maupetit  (1000) fun       (5000)        1 2021-01-21 20:23:32.000000 md2pdf-0.5/md2pdf.egg-info/dependency_links.txt
--rw-r--r--   0 maupetit  (1000) fun       (5000)       28 2021-01-21 20:23:32.000000 md2pdf-0.5/md2pdf.egg-info/requires.txt
--rw-r--r--   0 maupetit  (1000) fun       (5000)       13 2021-01-21 20:23:32.000000 md2pdf-0.5/md2pdf.egg-info/top_level.txt
--rw-r--r--   0 maupetit  (1000) fun       (5000)       96 2021-01-21 19:55:29.000000 md2pdf-0.5/requirements-dev.txt
--rw-r--r--   0 maupetit  (1000) fun       (5000)       28 2021-01-21 19:55:29.000000 md2pdf-0.5/requirements.txt
-drwxr-xr-x   0 maupetit  (1000) fun       (5000)        0 2021-01-21 20:23:32.239445 md2pdf-0.5/scripts/
--rwxr-xr-x   0 maupetit  (1000) fun       (5000)      787 2021-01-21 19:55:29.000000 md2pdf-0.5/scripts/md2pdf
--rw-r--r--   0 maupetit  (1000) fun       (5000)      247 2021-01-21 20:23:32.239445 md2pdf-0.5/setup.cfg
--rw-r--r--   0 maupetit  (1000) fun       (5000)     2256 2021-01-21 19:55:29.000000 md2pdf-0.5/setup.py
-drwxr-xr-x   0 maupetit  (1000) fun       (5000)        0 2021-01-21 20:23:32.239445 md2pdf-0.5/tests/
--rw-r--r--   0 maupetit  (1000) fun       (5000)        0 2021-01-21 19:55:29.000000 md2pdf-0.5/tests/__init__.py
--rw-r--r--   0 maupetit  (1000) fun       (5000)      164 2021-01-21 19:55:29.000000 md2pdf-0.5/tests/defaults.py
--rw-r--r--   0 maupetit  (1000) fun       (5000)     1866 2021-01-21 19:55:29.000000 md2pdf-0.5/tests/test_cli.py
--rw-r--r--   0 maupetit  (1000) fun       (5000)      617 2021-01-21 19:55:29.000000 md2pdf-0.5/tests/test_core.py
+drwxr-xr-x   0 maupetit  (1000) fun       (5000)        0 2023-04-07 14:33:47.295627 md2pdf-0.6/
+-rw-r--r--   0 maupetit  (1000) fun       (5000)     1064 2021-01-21 19:55:29.000000 md2pdf-0.6/LICENSE
+-rw-r--r--   0 maupetit  (1000) fun       (5000)      148 2021-01-21 19:55:29.000000 md2pdf-0.6/MANIFEST.in
+-rw-r--r--   0 maupetit  (1000) fun       (5000)     1166 2023-04-07 14:33:47.295627 md2pdf-0.6/PKG-INFO
+-rw-r--r--   0 maupetit  (1000) fun       (5000)     3467 2021-01-21 19:55:29.000000 md2pdf-0.6/README.md
+drwxr-xr-x   0 maupetit  (1000) fun       (5000)        0 2023-04-07 14:33:47.295627 md2pdf-0.6/md2pdf/
+-rw-r--r--   0 maupetit  (1000) fun       (5000)      210 2023-04-07 14:25:24.000000 md2pdf-0.6/md2pdf/__init__.py
+-rwxr-xr-x   0 maupetit  (1000) fun       (5000)      787 2023-04-07 14:17:27.000000 md2pdf-0.6/md2pdf/__main__.py
+-rw-r--r--   0 maupetit  (1000) fun       (5000)     1393 2023-04-07 14:17:27.000000 md2pdf-0.6/md2pdf/core.py
+-rw-r--r--   0 maupetit  (1000) fun       (5000)       69 2021-01-21 19:55:29.000000 md2pdf-0.6/md2pdf/exceptions.py
+drwxr-xr-x   0 maupetit  (1000) fun       (5000)        0 2023-04-07 14:33:47.295627 md2pdf-0.6/md2pdf.egg-info/
+-rw-r--r--   0 maupetit  (1000) fun       (5000)     1166 2023-04-07 14:33:47.000000 md2pdf-0.6/md2pdf.egg-info/PKG-INFO
+-rw-r--r--   0 maupetit  (1000) fun       (5000)      415 2023-04-07 14:33:47.000000 md2pdf-0.6/md2pdf.egg-info/SOURCES.txt
+-rw-r--r--   0 maupetit  (1000) fun       (5000)        1 2023-04-07 14:33:47.000000 md2pdf-0.6/md2pdf.egg-info/dependency_links.txt
+-rw-r--r--   0 maupetit  (1000) fun       (5000)       49 2023-04-07 14:33:47.000000 md2pdf-0.6/md2pdf.egg-info/entry_points.txt
+-rw-r--r--   0 maupetit  (1000) fun       (5000)       28 2023-04-07 14:33:47.000000 md2pdf-0.6/md2pdf.egg-info/requires.txt
+-rw-r--r--   0 maupetit  (1000) fun       (5000)       13 2023-04-07 14:33:47.000000 md2pdf-0.6/md2pdf.egg-info/top_level.txt
+-rw-r--r--   0 maupetit  (1000) fun       (5000)       96 2021-01-21 19:55:29.000000 md2pdf-0.6/requirements-dev.txt
+-rw-r--r--   0 maupetit  (1000) fun       (5000)       28 2021-01-21 19:55:29.000000 md2pdf-0.6/requirements.txt
+-rw-r--r--   0 maupetit  (1000) fun       (5000)      319 2023-04-07 14:33:47.295627 md2pdf-0.6/setup.cfg
+-rw-r--r--   0 maupetit  (1000) fun       (5000)     2222 2023-04-07 14:17:27.000000 md2pdf-0.6/setup.py
+drwxr-xr-x   0 maupetit  (1000) fun       (5000)        0 2023-04-07 14:33:47.295627 md2pdf-0.6/tests/
+-rw-r--r--   0 maupetit  (1000) fun       (5000)        0 2021-01-21 19:55:29.000000 md2pdf-0.6/tests/__init__.py
+-rw-r--r--   0 maupetit  (1000) fun       (5000)      164 2021-01-21 19:55:29.000000 md2pdf-0.6/tests/defaults.py
+-rw-r--r--   0 maupetit  (1000) fun       (5000)     1866 2021-01-21 19:55:29.000000 md2pdf-0.6/tests/test_cli.py
+-rw-r--r--   0 maupetit  (1000) fun       (5000)      617 2021-01-21 19:55:29.000000 md2pdf-0.6/tests/test_core.py
```

### Comparing `md2pdf-0.5/LICENSE` & `md2pdf-0.6/LICENSE`

 * *Files identical despite different names*

### Comparing `md2pdf-0.5/PKG-INFO` & `md2pdf-0.6/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,16 +1,15 @@
-Metadata-Version: 1.1
+Metadata-Version: 2.1
 Name: md2pdf
-Version: 0.5
+Version: 0.6
 Summary: md2pdf, a Markdown to PDF conversion tool
 Home-page: UNKNOWN
 Author: Julien Maupetit
 Author-email: julien@maupetit.net
 License: MIT
-Description: UNKNOWN
 Keywords: markdown converter css pdf
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Customer Service
 Classifier: Intended Audience :: End Users/Desktop
 Classifier: Intended Audience :: Information Technology
 Classifier: Intended Audience :: Science/Research
@@ -24,7 +23,11 @@
 Classifier: Programming Language :: Python :: 2.7
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.4
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Topic :: Office/Business
 Classifier: Topic :: Utilities
+License-File: LICENSE
+
+UNKNOWN
+
```

### Comparing `md2pdf-0.5/README.md` & `md2pdf-0.6/README.md`

 * *Files identical despite different names*

### Comparing `md2pdf-0.5/md2pdf/core.py` & `md2pdf-0.6/md2pdf/core.py`

 * *Files 4% similar despite different names*

```diff
@@ -24,15 +24,15 @@
 
     Raises:
         ValidationError: if md_content and md_file_path are empty.
     """
 
     # Convert markdown to html
     raw_html = ''
-    extras = ['cuddled-lists', 'tables']
+    extras = ['cuddled-lists', 'tables', 'footnotes']
     if md_file_path:
         raw_html = markdown_path(md_file_path, extras=extras)
     elif md_content:
         raw_html = markdown(md_content, extras=extras)
 
     if not len(raw_html):
         raise ValidationError('Input markdown seems empty')
```

### Comparing `md2pdf-0.5/md2pdf.egg-info/PKG-INFO` & `md2pdf-0.6/md2pdf.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,16 +1,15 @@
-Metadata-Version: 1.1
+Metadata-Version: 2.1
 Name: md2pdf
-Version: 0.5
+Version: 0.6
 Summary: md2pdf, a Markdown to PDF conversion tool
 Home-page: UNKNOWN
 Author: Julien Maupetit
 Author-email: julien@maupetit.net
 License: MIT
-Description: UNKNOWN
 Keywords: markdown converter css pdf
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Intended Audience :: Customer Service
 Classifier: Intended Audience :: End Users/Desktop
 Classifier: Intended Audience :: Information Technology
 Classifier: Intended Audience :: Science/Research
@@ -24,7 +23,11 @@
 Classifier: Programming Language :: Python :: 2.7
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.4
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Topic :: Office/Business
 Classifier: Topic :: Utilities
+License-File: LICENSE
+
+UNKNOWN
+
```

### Comparing `md2pdf-0.5/scripts/md2pdf` & `md2pdf-0.6/md2pdf/__main__.py`

 * *Files identical despite different names*

### Comparing `md2pdf-0.5/setup.py` & `md2pdf-0.6/setup.py`

 * *Files 2% similar despite different names*

```diff
@@ -32,15 +32,14 @@
         return list(packages)
 
 
 setup(
     name='md2pdf',
     version=md2pdf.__version__,
     packages=find_packages(),
-    scripts=['scripts/md2pdf', ],
     install_requires=parse_requirements('requirements.txt'),
     setup_requires=['pytest-runner', ],
     tests_require=parse_requirements('requirements-dev.txt'),
     author='Julien Maupetit',
     author_email='julien@maupetit.net',
     description='md2pdf, a Markdown to PDF conversion tool',
     license='MIT',
```

### Comparing `md2pdf-0.5/tests/test_cli.py` & `md2pdf-0.6/tests/test_cli.py`

 * *Files identical despite different names*

### Comparing `md2pdf-0.5/tests/test_core.py` & `md2pdf-0.6/tests/test_core.py`

 * *Files identical despite different names*

