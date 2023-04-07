# Comparing `tmp/generatenscore-1.0.7.tar.gz` & `tmp/generatenscore-1.0.8.tar.gz`

## Comparing `generatenscore-1.0.7.tar` & `generatenscore-1.0.8.tar`

### file list

```diff
@@ -1,16 +1,16 @@
--rw-r--r--   0        0        0      167 2020-02-02 00:00:00.000000 generatenscore-1.0.7/Embedding Images in HTMLs.url
--rw-r--r--   0        0        0      158 2020-02-02 00:00:00.000000 generatenscore-1.0.7/Packaging.url
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 generatenscore-1.0.7/certutil -encode mypicture.png mypicture.txt.txt
--rw-r--r--   0        0        0     2029 2020-02-02 00:00:00.000000 generatenscore-1.0.7/up8c18p01.png
--rw-r--r--   0        0        0     2850 2020-02-02 00:00:00.000000 generatenscore-1.0.7/up8c18p01.txt
--rw-r--r--   0        0        0      564 2020-02-02 00:00:00.000000 generatenscore-1.0.7/updatePackage.txt
--rw-r--r--   0        0        0      161 2020-02-02 00:00:00.000000 generatenscore-1.0.7/src/generateNscore/__init__.py
--rw-r--r--   0        0        0     2284 2020-02-02 00:00:00.000000 generatenscore-1.0.7/src/generateNscore/_common.py
--rw-r--r--   0        0        0     9263 2020-02-02 00:00:00.000000 generatenscore-1.0.7/src/generateNscore/_generateEm.py
--rw-r--r--   0        0        0    17850 2020-02-02 00:00:00.000000 generatenscore-1.0.7/src/generateNscore/_generateMakeHTMLs.py
--rw-r--r--   0        0        0     9951 2020-02-02 00:00:00.000000 generatenscore-1.0.7/src/generateNscore/_scoreEm.py
--rw-r--r--   0        0        0    14836 2020-02-02 00:00:00.000000 generatenscore-1.0.7/src/generateNscore/makeChoices.py
--rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 generatenscore-1.0.7/LICENSE.txt
--rw-r--r--   0        0        0     2502 2020-02-02 00:00:00.000000 generatenscore-1.0.7/README.md
--rw-r--r--   0        0        0      789 2020-02-02 00:00:00.000000 generatenscore-1.0.7/pyproject.toml
--rw-r--r--   0        0        0     3178 2020-02-02 00:00:00.000000 generatenscore-1.0.7/PKG-INFO
+-rw-r--r--   0        0        0      167 2020-02-02 00:00:00.000000 generatenscore-1.0.8/Embedding Images in HTMLs.url
+-rw-r--r--   0        0        0      158 2020-02-02 00:00:00.000000 generatenscore-1.0.8/Packaging.url
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 generatenscore-1.0.8/certutil -encode mypicture.png mypicture.txt.txt
+-rw-r--r--   0        0        0     2029 2020-02-02 00:00:00.000000 generatenscore-1.0.8/up8c18p01.png
+-rw-r--r--   0        0        0     2850 2020-02-02 00:00:00.000000 generatenscore-1.0.8/up8c18p01.txt
+-rw-r--r--   0        0        0      564 2020-02-02 00:00:00.000000 generatenscore-1.0.8/updatePackage.txt
+-rw-r--r--   0        0        0      161 2020-02-02 00:00:00.000000 generatenscore-1.0.8/src/generateNscore/__init__.py
+-rw-r--r--   0        0        0     2284 2020-02-02 00:00:00.000000 generatenscore-1.0.8/src/generateNscore/_common.py
+-rw-r--r--   0        0        0     9263 2020-02-02 00:00:00.000000 generatenscore-1.0.8/src/generateNscore/_generateEm.py
+-rw-r--r--   0        0        0    17850 2020-02-02 00:00:00.000000 generatenscore-1.0.8/src/generateNscore/_generateMakeHTMLs.py
+-rw-r--r--   0        0        0     9951 2020-02-02 00:00:00.000000 generatenscore-1.0.8/src/generateNscore/_scoreEm.py
+-rw-r--r--   0        0        0    14836 2020-02-02 00:00:00.000000 generatenscore-1.0.8/src/generateNscore/makeChoices.py
+-rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 generatenscore-1.0.8/LICENSE.txt
+-rw-r--r--   0        0        0     2502 2020-02-02 00:00:00.000000 generatenscore-1.0.8/README.md
+-rw-r--r--   0        0        0      829 2020-02-02 00:00:00.000000 generatenscore-1.0.8/pyproject.toml
+-rw-r--r--   0        0        0     3222 2020-02-02 00:00:00.000000 generatenscore-1.0.8/PKG-INFO
```

### Comparing `generatenscore-1.0.7/up8c18p01.png` & `generatenscore-1.0.8/up8c18p01.png`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/up8c18p01.txt` & `generatenscore-1.0.8/up8c18p01.txt`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/updatePackage.txt` & `generatenscore-1.0.8/updatePackage.txt`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/src/generateNscore/_common.py` & `generatenscore-1.0.8/src/generateNscore/_common.py`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/src/generateNscore/_generateEm.py` & `generatenscore-1.0.8/src/generateNscore/_generateEm.py`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/src/generateNscore/_generateMakeHTMLs.py` & `generatenscore-1.0.8/src/generateNscore/_generateMakeHTMLs.py`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/src/generateNscore/_scoreEm.py` & `generatenscore-1.0.8/src/generateNscore/_scoreEm.py`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/src/generateNscore/makeChoices.py` & `generatenscore-1.0.8/src/generateNscore/makeChoices.py`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/LICENSE.txt` & `generatenscore-1.0.8/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/README.md` & `generatenscore-1.0.8/README.md`

 * *Files identical despite different names*

### Comparing `generatenscore-1.0.7/pyproject.toml` & `generatenscore-1.0.8/pyproject.toml`

 * *Files 16% similar despite different names*

```diff
@@ -1,25 +1,26 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "generateNscore"
-version = "1.0.7"
+version = "1.0.8"
 authors = [
   { name="Sukmock Lee", email="smlee@inha.ac.kr" },
 ]
 description = "A package to generate question sheets in HTML files and to score answers in text files"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
     "Topic :: Education :: Testing",
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
     "Intended Audience :: Education",
-    "Intended Audience :: End Users/Desktop"
+    "Intended Audience :: End Users/Desktop",
+    "Development Status :: 3 - Alpha"
 ]
 
 [project.urls]
 "Homepage" = "https://github.com/generateNscore/generateNscore"
 "Bug Tracker" = "https://github.com/generateNscore/generateNscore/issues"
```

### Comparing `generatenscore-1.0.7/PKG-INFO` & `generatenscore-1.0.8/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,15 +1,16 @@
 Metadata-Version: 2.1
 Name: generateNscore
-Version: 1.0.7
+Version: 1.0.8
 Summary: A package to generate question sheets in HTML files and to score answers in text files
 Project-URL: Homepage, https://github.com/generateNscore/generateNscore
 Project-URL: Bug Tracker, https://github.com/generateNscore/generateNscore/issues
 Author-email: Sukmock Lee <smlee@inha.ac.kr>
 License-File: LICENSE.txt
+Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Education
 Classifier: Intended Audience :: End Users/Desktop
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: Topic :: Education :: Testing
 Requires-Python: >=3.7
```

#### html2text {}

```diff
@@ -1,20 +1,21 @@
-Metadata-Version: 2.1 Name: generateNscore Version: 1.0.7 Summary: A package to
+Metadata-Version: 2.1 Name: generateNscore Version: 1.0.8 Summary: A package to
 generate question sheets in HTML files and to score answers in text files
 Project-URL: Homepage, https://github.com/generateNscore/generateNscore
 Project-URL: Bug Tracker, https://github.com/generateNscore/generateNscore/
 issues Author-email: Sukmock Lee
-inha.ac.kr> License-File: LICENSE.txt Classifier: Intended Audience ::
-Education Classifier: Intended Audience :: End Users/Desktop Classifier:
-License :: OSI Approved :: MIT License Classifier: Operating System :: OS
-Independent Classifier: Programming Language :: Python :: 3 Classifier: Topic
-:: Education :: Testing Requires-Python: >=3.7 Description-Content-Type: text/
-markdown # generateNscore What is it? generateNscore is a Python package that
-provides as many personalized question sheets in HTML files as you want. It
-aims to be one of fundamental teaching tools. Help
+inha.ac.kr> License-File: LICENSE.txt Classifier: Development Status :: 3 -
+Alpha Classifier: Intended Audience :: Education Classifier: Intended Audience
+:: End Users/Desktop Classifier: License :: OSI Approved :: MIT License
+Classifier: Operating System :: OS Independent Classifier: Programming Language
+:: Python :: 3 Classifier: Topic :: Education :: Testing Requires-Python: >=3.7
+Description-Content-Type: text/markdown # generateNscore What is it?
+generateNscore is a Python package that provides as many personalized question
+sheets in HTML files as you want. It aims to be one of fundamental teaching
+tools. Help
     * Documentation
     * Changelog
 Features
     * Generates as many personalized question sheets in HTML files as one wants
       with a few strings of text.
     * The amount of random personalization is under total control of users.
     * Each HTML file with a name corresponding to the identification number.
```

