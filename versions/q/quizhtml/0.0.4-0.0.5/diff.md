# Comparing `tmp/quizhtml-0.0.4.tar.gz` & `tmp/quizhtml-0.0.5.tar.gz`

## Comparing `quizhtml-0.0.4.tar` & `quizhtml-0.0.5.tar`

### file list

```diff
@@ -1,16 +1,19 @@
--rw-r--r--   0        0        0      167 2020-02-02 00:00:00.000000 quizhtml-0.0.4/Embedding Images in HTMLs.url
--rw-r--r--   0        0        0      158 2020-02-02 00:00:00.000000 quizhtml-0.0.4/Packaging.url
--rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 quizhtml-0.0.4/certutil -encode mypicture.png mypicture.txt.txt
--rw-r--r--   0        0        0     2029 2020-02-02 00:00:00.000000 quizhtml-0.0.4/up8c18p01.png
--rw-r--r--   0        0        0     2850 2020-02-02 00:00:00.000000 quizhtml-0.0.4/up8c18p01.txt
--rw-r--r--   0        0        0      564 2020-02-02 00:00:00.000000 quizhtml-0.0.4/updatePackage.txt
--rw-r--r--   0        0        0      161 2020-02-02 00:00:00.000000 quizhtml-0.0.4/src/quizhtml/__init__.py
--rw-r--r--   0        0        0     2284 2020-02-02 00:00:00.000000 quizhtml-0.0.4/src/quizhtml/_common.py
--rw-r--r--   0        0        0     9263 2020-02-02 00:00:00.000000 quizhtml-0.0.4/src/quizhtml/_generateEm.py
--rw-r--r--   0        0        0    17850 2020-02-02 00:00:00.000000 quizhtml-0.0.4/src/quizhtml/_generateMakeHTMLs.py
--rw-r--r--   0        0        0     9951 2020-02-02 00:00:00.000000 quizhtml-0.0.4/src/quizhtml/_scoreEm.py
--rw-r--r--   0        0        0    14836 2020-02-02 00:00:00.000000 quizhtml-0.0.4/src/quizhtml/makeChoices.py
--rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 quizhtml-0.0.4/LICENSE.txt
--rw-r--r--   0        0        0     2277 2020-02-02 00:00:00.000000 quizhtml-0.0.4/README.md
--rw-r--r--   0        0        0      874 2020-02-02 00:00:00.000000 quizhtml-0.0.4/pyproject.toml
--rw-r--r--   0        0        0     3042 2020-02-02 00:00:00.000000 quizhtml-0.0.4/PKG-INFO
+-rw-r--r--   0        0        0      167 2020-02-02 00:00:00.000000 quizhtml-0.0.5/Embedding Images in HTMLs.url
+-rw-r--r--   0        0        0      158 2020-02-02 00:00:00.000000 quizhtml-0.0.5/Packaging.url
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 quizhtml-0.0.5/certutil -encode mypicture.png mypicture.txt.txt
+-rw-r--r--   0        0        0     2029 2020-02-02 00:00:00.000000 quizhtml-0.0.5/up8c18p01.png
+-rw-r--r--   0        0        0     2850 2020-02-02 00:00:00.000000 quizhtml-0.0.5/up8c18p01.txt
+-rw-r--r--   0        0        0      564 2020-02-02 00:00:00.000000 quizhtml-0.0.5/updatePackage.txt
+-rw-r--r--   0        0        0     7612 2020-02-02 00:00:00.000000 quizhtml-0.0.5/src/yyy.py
+-rw-r--r--   0        0        0    10901 2020-02-02 00:00:00.000000 quizhtml-0.0.5/src/checkups1/checkups1/checkups10.html
+-rw-r--r--   0        0        0      334 2020-02-02 00:00:00.000000 quizhtml-0.0.5/src/checkups1/checkups1/index.html
+-rw-r--r--   0        0        0      161 2020-02-02 00:00:00.000000 quizhtml-0.0.5/src/quizhtml/__init__.py
+-rw-r--r--   0        0        0     2284 2020-02-02 00:00:00.000000 quizhtml-0.0.5/src/quizhtml/_common.py
+-rw-r--r--   0        0        0     9263 2020-02-02 00:00:00.000000 quizhtml-0.0.5/src/quizhtml/_generateEm.py
+-rw-r--r--   0        0        0    17850 2020-02-02 00:00:00.000000 quizhtml-0.0.5/src/quizhtml/_generateMakeHTMLs.py
+-rw-r--r--   0        0        0     9951 2020-02-02 00:00:00.000000 quizhtml-0.0.5/src/quizhtml/_scoreEm.py
+-rw-r--r--   0        0        0    14836 2020-02-02 00:00:00.000000 quizhtml-0.0.5/src/quizhtml/makeChoices.py
+-rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 quizhtml-0.0.5/LICENSE.txt
+-rw-r--r--   0        0        0     2277 2020-02-02 00:00:00.000000 quizhtml-0.0.5/README.md
+-rw-r--r--   0        0        0      874 2020-02-02 00:00:00.000000 quizhtml-0.0.5/pyproject.toml
+-rw-r--r--   0        0        0     3042 2020-02-02 00:00:00.000000 quizhtml-0.0.5/PKG-INFO
```

### Comparing `quizhtml-0.0.4/up8c18p01.png` & `quizhtml-0.0.5/up8c18p01.png`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/up8c18p01.txt` & `quizhtml-0.0.5/up8c18p01.txt`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/updatePackage.txt` & `quizhtml-0.0.5/updatePackage.txt`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/src/quizhtml/_common.py` & `quizhtml-0.0.5/src/quizhtml/_common.py`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/src/quizhtml/_generateEm.py` & `quizhtml-0.0.5/src/quizhtml/_generateEm.py`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/src/quizhtml/_generateMakeHTMLs.py` & `quizhtml-0.0.5/src/quizhtml/_generateMakeHTMLs.py`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/src/quizhtml/_scoreEm.py` & `quizhtml-0.0.5/src/quizhtml/_scoreEm.py`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/src/quizhtml/makeChoices.py` & `quizhtml-0.0.5/src/quizhtml/makeChoices.py`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/LICENSE.txt` & `quizhtml-0.0.5/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/README.md` & `quizhtml-0.0.5/README.md`

 * *Files identical despite different names*

### Comparing `quizhtml-0.0.4/pyproject.toml` & `quizhtml-0.0.5/pyproject.toml`

 * *Files 13% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "quizhtml"
-version = "0.0.4"
+version = "0.0.5"
 authors = [
   { name="Sukmock Lee", email="smlee@inha.ac.kr" },
 ]
 description = "A package that generates question papers as HTML files to be distributed over the network and grades the answers in text files submitted by students."
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `quizhtml-0.0.4/PKG-INFO` & `quizhtml-0.0.5/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: quizhtml
-Version: 0.0.4
+Version: 0.0.5
 Summary: A package that generates question papers as HTML files to be distributed over the network and grades the answers in text files submitted by students.
 Project-URL: Homepage, https://github.com/generateNscore/quizhtml
 Project-URL: Bug Tracker, https://github.com/generateNscore/quizhtml/issues
 Author-email: Sukmock Lee <smlee@inha.ac.kr>
 License-File: LICENSE.txt
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Education
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: quizhtml Version: 0.0.4 Summary: A package that
+Metadata-Version: 2.1 Name: quizhtml Version: 0.0.5 Summary: A package that
 generates question papers as HTML files to be distributed over the network and
 grades the answers in text files submitted by students. Project-URL: Homepage,
 https://github.com/generateNscore/quizhtml Project-URL: Bug Tracker, https://
 github.com/generateNscore/quizhtml/issues Author-email: Sukmock Lee
 inha.ac.kr> License-File: LICENSE.txt Classifier: Development Status :: 3 -
 Alpha Classifier: Intended Audience :: Education Classifier: Intended Audience
 :: End Users/Desktop Classifier: License :: OSI Approved :: MIT License
```

