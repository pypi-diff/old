# Comparing `tmp/generate_score-0.0.1.tar.gz` & `tmp/generate_score-0.0.2.tar.gz`

## Comparing `generate_score-0.0.1.tar` & `generate_score-0.0.2.tar`

### file list

```diff
@@ -1,41 +1,16 @@
--rw-r--r--   0        0        0      553 2020-02-02 00:00:00.000000 generate_score-0.0.1/updatePackage.txt
--rw-r--r--   0        0        0     1249 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/addFractions.py
--rw-r--r--   0        0        0     1534 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/clock.py
--rw-r--r--   0        0        0      946 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/division.py
--rw-r--r--   0        0        0      517 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/ex1.py
--rw-r--r--   0        0        0    12667 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/generateSheets_Example1.py
--rw-r--r--   0        0        0     2376 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/graph.py
--rw-r--r--   0        0        0      137 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/scoreAnswers.py
--rw-r--r--   0        0        0     2408 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/userfunctions.py
--rw-r--r--   0        0        0      284 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/userfunctions11.py
--rw-r--r--   0        0        0     1275 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/userfunctions2.py
--rw-r--r--   0        0        0      288 2020-02-02 00:00:00.000000 generate_score-0.0.1/Examples/출석부.csv
--rw-r--r--   0        0        0     9274 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex1-1.png
--rw-r--r--   0        0        0    40429 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex1-2.png
--rw-r--r--   0        0        0    51221 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex1-3.png
--rw-r--r--   0        0        0    42174 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex2-1.png
--rw-r--r--   0        0        0    51242 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex2-2.png
--rw-r--r--   0        0        0    63682 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex2-3.png
--rw-r--r--   0        0        0    61703 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex2-4.png
--rw-r--r--   0        0        0    59325 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex2-5.png
--rw-r--r--   0        0        0    65983 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex2-6.png
--rw-r--r--   0        0        0    43457 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex2-7.png
--rw-r--r--   0        0        0    52191 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/ex2-7b.png
--rw-r--r--   0        0        0    62187 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/example1-1.png
--rw-r--r--   0        0        0    63145 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/example1-2.png
--rw-r--r--   0        0        0    41639 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/example1-3.png
--rw-r--r--   0        0        0    55764 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/example1-4.png
--rw-r--r--   0        0        0    70568 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/example1-5.png
--rw-r--r--   0        0        0    47874 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/example1-6.png
--rw-r--r--   0        0        0     2130 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/question.png
--rw-r--r--   0        0        0     2258 2020-02-02 00:00:00.000000 generate_score-0.0.1/img/save.png
--rw-r--r--   0        0        0      161 2020-02-02 00:00:00.000000 generate_score-0.0.1/src/__init__.py
--rw-r--r--   0        0        0     2284 2020-02-02 00:00:00.000000 generate_score-0.0.1/src/_common.py
--rw-r--r--   0        0        0     9263 2020-02-02 00:00:00.000000 generate_score-0.0.1/src/_generateEm.py
--rw-r--r--   0        0        0    17850 2020-02-02 00:00:00.000000 generate_score-0.0.1/src/_generateMakeHTMLs.py
--rw-r--r--   0        0        0     9951 2020-02-02 00:00:00.000000 generate_score-0.0.1/src/_scoreEm.py
--rw-r--r--   0        0        0    14836 2020-02-02 00:00:00.000000 generate_score-0.0.1/src/makeChoices.py
--rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 generate_score-0.0.1/LICENSE.txt
--rw-r--r--   0        0        0     2580 2020-02-02 00:00:00.000000 generate_score-0.0.1/README.md
--rw-r--r--   0        0        0      829 2020-02-02 00:00:00.000000 generate_score-0.0.1/pyproject.toml
--rw-r--r--   0        0        0     3300 2020-02-02 00:00:00.000000 generate_score-0.0.1/PKG-INFO
+-rw-r--r--   0        0        0      167 2020-02-02 00:00:00.000000 generate_score-0.0.2/Embedding Images in HTMLs.url
+-rw-r--r--   0        0        0      158 2020-02-02 00:00:00.000000 generate_score-0.0.2/Packaging.url
+-rw-r--r--   0        0        0        0 2020-02-02 00:00:00.000000 generate_score-0.0.2/certutil -encode mypicture.png mypicture.txt.txt
+-rw-r--r--   0        0        0     2029 2020-02-02 00:00:00.000000 generate_score-0.0.2/up8c18p01.png
+-rw-r--r--   0        0        0     2850 2020-02-02 00:00:00.000000 generate_score-0.0.2/up8c18p01.txt
+-rw-r--r--   0        0        0      564 2020-02-02 00:00:00.000000 generate_score-0.0.2/updatePackage.txt
+-rw-r--r--   0        0        0      161 2020-02-02 00:00:00.000000 generate_score-0.0.2/src/generate_score/__init__.py
+-rw-r--r--   0        0        0     2284 2020-02-02 00:00:00.000000 generate_score-0.0.2/src/generate_score/_common.py
+-rw-r--r--   0        0        0     9263 2020-02-02 00:00:00.000000 generate_score-0.0.2/src/generate_score/_generateEm.py
+-rw-r--r--   0        0        0    17850 2020-02-02 00:00:00.000000 generate_score-0.0.2/src/generate_score/_generateMakeHTMLs.py
+-rw-r--r--   0        0        0     9951 2020-02-02 00:00:00.000000 generate_score-0.0.2/src/generate_score/_scoreEm.py
+-rw-r--r--   0        0        0    14836 2020-02-02 00:00:00.000000 generate_score-0.0.2/src/generate_score/makeChoices.py
+-rw-r--r--   0        0        0     1091 2020-02-02 00:00:00.000000 generate_score-0.0.2/LICENSE.txt
+-rw-r--r--   0        0        0     2343 2020-02-02 00:00:00.000000 generate_score-0.0.2/README.md
+-rw-r--r--   0        0        0      829 2020-02-02 00:00:00.000000 generate_score-0.0.2/pyproject.toml
+-rw-r--r--   0        0        0     3063 2020-02-02 00:00:00.000000 generate_score-0.0.2/PKG-INFO
```

### Comparing `generate_score-0.0.1/updatePackage.txt` & `generate_score-0.0.2/updatePackage.txt`

 * *Files 20% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 동일한 버전은 허락하지 않는다.
 
 1. pyroject에서 버전을 바꾼다. 
 
 2. dist에 들어있던 예전 파일들은 모두 삭제
 
-3. 명령 프롬프트를 열고 해당 디렉토리으로 이동한다. D:\GitHub\generate_score>
+3. 명령 프롬프트를 열고 해당 디렉토리으로 이동한다. D:\gram\Desktop\PyPI_generate_score>
 
 	필요하면,   py -m pip install --upgrade build
 
 4. py -m build
 ---> "Successfully built generatenscore-1.0.0.tar.gz and generatenscore-1.0.0-py3-none-any.whl" 확인하고
 폴더 disk에 파일 2 개 생성 확인.
```

### Comparing `generate_score-0.0.1/src/_common.py` & `generate_score-0.0.2/src/generate_score/_common.py`

 * *Files identical despite different names*

### Comparing `generate_score-0.0.1/src/_generateEm.py` & `generate_score-0.0.2/src/generate_score/_generateEm.py`

 * *Files identical despite different names*

### Comparing `generate_score-0.0.1/src/_generateMakeHTMLs.py` & `generate_score-0.0.2/src/generate_score/_generateMakeHTMLs.py`

 * *Files identical despite different names*

### Comparing `generate_score-0.0.1/src/_scoreEm.py` & `generate_score-0.0.2/src/generate_score/_scoreEm.py`

 * *Files identical despite different names*

### Comparing `generate_score-0.0.1/src/makeChoices.py` & `generate_score-0.0.2/src/generate_score/makeChoices.py`

 * *Files identical despite different names*

### Comparing `generate_score-0.0.1/LICENSE.txt` & `generate_score-0.0.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `generate_score-0.0.1/README.md` & `generate_score-0.0.2/README.md`

 * *Files 20% similar despite different names*

```diff
@@ -1,18 +1,17 @@
 # generate_score
-Python package to generate question sheets in HTML files and to score students answer text files
 
 <strong>What is it?</strong>
 
 generateNscore is a Python package that provides as many personalized question sheets in HTML files as you want. It aims to be one of fundamental teaching tools.
 
 <strong>Help</strong>
 <ul>
 <li><a href="https://github.com/generateNscore/generate_score/wiki">Documentation</a></li>
-<li><a href="https://github.com/generateNscore/generate_score/blob/main/Changelog.md">Changelog</a></li></ul>
+</ul>
 
 <strong>Features</strong>
 <ul>
 <li>Generates as many personalized question sheets in HTML files as one wants with a few strings of text.</li>
 <li>The amount of random personalization is under total control of users.</li>
 <li>Each HTML file with a name corresponding to the identification number.</li>
 <li>Multi-choice as well as short, default, questions can be made.</li>
@@ -28,22 +27,23 @@
 <li>The source code is currently hosted on GitHub at: <a href="https://github.com/generateNscore/generate_score">https://github.com/generateNscore/generate_score</a></li>
 <br>
 
 <pre lang=sh>pip install generate_score</pre>
 
 </ul>
 
+<strong>Dependencies</strong>
 <ul><li>None</li></ul>
 
 <strong>Example shots</strong>
 <li>A short-answer question</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-3.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-3.png">
 <li>A multiple-choice question</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-6.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-6.png">
 <li>A multiple-choice question with a figure</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-2.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-2.png">
 <li>A question with multiple-choice figures</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-1.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-1.png">
 <li>A question with equation and with multiple-choices</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-4.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-4.png">
 <li>A question with equation and with multiple-choice figures</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-5.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-5.png">
```

#### html2text {}

```diff
@@ -1,13 +1,11 @@
-# generate_score Python package to generate question sheets in HTML files and
-to score students answer text files What is it? generateNscore is a Python
-package that provides as many personalized question sheets in HTML files as you
-want. It aims to be one of fundamental teaching tools. Help
+# generate_score What is it? generateNscore is a Python package that provides
+as many personalized question sheets in HTML files as you want. It aims to be
+one of fundamental teaching tools. Help
     * Documentation
-    * Changelog
 Features
     * Generates as many personalized question sheets in HTML files as one wants
       with a few strings of text.
     * The amount of random personalization is under total control of users.
     * Each HTML file with a name corresponding to the identification number.
     * Multi-choice as well as short, default, questions can be made.
     * A figure, although a pre-made image can be used, can be varied as well as
@@ -20,21 +18,22 @@
     * Scoring all different answers in text files submitted can be done in a
       second.
 Where to get it
     * The source code is currently hosted on GitHub at: https://github.com/
       generateNscore/generate_score
     *
       pip install generate_score
+Dependencies
     * None
 Example shots
 A short-answer question
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-3.png]
+[https://generateNscore.github.io/generate_score/img/example1-3.png]
 A multiple-choice question
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-6.png]
+[https://generateNscore.github.io/generate_score/img/example1-6.png]
 A multiple-choice question with a figure
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-2.png]
+[https://generateNscore.github.io/generate_score/img/example1-2.png]
 A question with multiple-choice figures
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-1.png]
+[https://generateNscore.github.io/generate_score/img/example1-1.png]
 A question with equation and with multiple-choices
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-4.png]
+[https://generateNscore.github.io/generate_score/img/example1-4.png]
 A question with equation and with multiple-choice figures
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-5.png]
+[https://generateNscore.github.io/generate_score/img/example1-5.png]
```

### Comparing `generate_score-0.0.1/pyproject.toml` & `generate_score-0.0.2/pyproject.toml`

 * *Files 14% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "generate_score"
-version = "0.0.1"
+version = "0.0.2"
 authors = [
   { name="Sukmock Lee", email="smlee@inha.ac.kr" },
 ]
 description = "A package to generate question sheets in HTML files and to score answers in text files"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `generate_score-0.0.1/PKG-INFO` & `generate_score-0.0.2/PKG-INFO`

 * *Files 13% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: generate_score
-Version: 0.0.1
+Version: 0.0.2
 Summary: A package to generate question sheets in HTML files and to score answers in text files
 Project-URL: Homepage, https://github.com/generateNscore/generate_score
 Project-URL: Bug Tracker, https://github.com/generateNscore/generate_score/issues
 Author-email: Sukmock Lee <smlee@inha.ac.kr>
 License-File: LICENSE.txt
 Classifier: Development Status :: 3 - Alpha
 Classifier: Intended Audience :: Education
@@ -13,24 +13,23 @@
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
 Classifier: Topic :: Education :: Testing
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
 
 # generate_score
-Python package to generate question sheets in HTML files and to score students answer text files
 
 <strong>What is it?</strong>
 
 generateNscore is a Python package that provides as many personalized question sheets in HTML files as you want. It aims to be one of fundamental teaching tools.
 
 <strong>Help</strong>
 <ul>
 <li><a href="https://github.com/generateNscore/generate_score/wiki">Documentation</a></li>
-<li><a href="https://github.com/generateNscore/generate_score/blob/main/Changelog.md">Changelog</a></li></ul>
+</ul>
 
 <strong>Features</strong>
 <ul>
 <li>Generates as many personalized question sheets in HTML files as one wants with a few strings of text.</li>
 <li>The amount of random personalization is under total control of users.</li>
 <li>Each HTML file with a name corresponding to the identification number.</li>
 <li>Multi-choice as well as short, default, questions can be made.</li>
@@ -46,22 +45,23 @@
 <li>The source code is currently hosted on GitHub at: <a href="https://github.com/generateNscore/generate_score">https://github.com/generateNscore/generate_score</a></li>
 <br>
 
 <pre lang=sh>pip install generate_score</pre>
 
 </ul>
 
+<strong>Dependencies</strong>
 <ul><li>None</li></ul>
 
 <strong>Example shots</strong>
 <li>A short-answer question</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-3.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-3.png">
 <li>A multiple-choice question</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-6.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-6.png">
 <li>A multiple-choice question with a figure</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-2.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-2.png">
 <li>A question with multiple-choice figures</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-1.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-1.png">
 <li>A question with equation and with multiple-choices</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-4.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-4.png">
 <li>A question with equation and with multiple-choice figures</li>
-<img src="https://github.com/generateNscore/generate_score/blob/main/img/example1-5.png">
+<img src="https://generateNscore.github.io/generate_score/img/example1-5.png">
```

#### html2text {}

```diff
@@ -1,24 +1,22 @@
-Metadata-Version: 2.1 Name: generate_score Version: 0.0.1 Summary: A package to
+Metadata-Version: 2.1 Name: generate_score Version: 0.0.2 Summary: A package to
 generate question sheets in HTML files and to score answers in text files
 Project-URL: Homepage, https://github.com/generateNscore/generate_score
 Project-URL: Bug Tracker, https://github.com/generateNscore/generate_score/
 issues Author-email: Sukmock Lee
 inha.ac.kr> License-File: LICENSE.txt Classifier: Development Status :: 3 -
 Alpha Classifier: Intended Audience :: Education Classifier: Intended Audience
 :: End Users/Desktop Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: OS Independent Classifier: Programming Language
 :: Python :: 3 Classifier: Topic :: Education :: Testing Requires-Python: >=3.7
-Description-Content-Type: text/markdown # generate_score Python package to
-generate question sheets in HTML files and to score students answer text files
-What is it? generateNscore is a Python package that provides as many
-personalized question sheets in HTML files as you want. It aims to be one of
-fundamental teaching tools. Help
+Description-Content-Type: text/markdown # generate_score What is it?
+generateNscore is a Python package that provides as many personalized question
+sheets in HTML files as you want. It aims to be one of fundamental teaching
+tools. Help
     * Documentation
-    * Changelog
 Features
     * Generates as many personalized question sheets in HTML files as one wants
       with a few strings of text.
     * The amount of random personalization is under total control of users.
     * Each HTML file with a name corresponding to the identification number.
     * Multi-choice as well as short, default, questions can be made.
     * A figure, although a pre-made image can be used, can be varied as well as
@@ -31,21 +29,22 @@
     * Scoring all different answers in text files submitted can be done in a
       second.
 Where to get it
     * The source code is currently hosted on GitHub at: https://github.com/
       generateNscore/generate_score
     *
       pip install generate_score
+Dependencies
     * None
 Example shots
 A short-answer question
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-3.png]
+[https://generateNscore.github.io/generate_score/img/example1-3.png]
 A multiple-choice question
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-6.png]
+[https://generateNscore.github.io/generate_score/img/example1-6.png]
 A multiple-choice question with a figure
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-2.png]
+[https://generateNscore.github.io/generate_score/img/example1-2.png]
 A question with multiple-choice figures
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-1.png]
+[https://generateNscore.github.io/generate_score/img/example1-1.png]
 A question with equation and with multiple-choices
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-4.png]
+[https://generateNscore.github.io/generate_score/img/example1-4.png]
 A question with equation and with multiple-choice figures
-[https://github.com/generateNscore/generate_score/blob/main/img/example1-5.png]
+[https://generateNscore.github.io/generate_score/img/example1-5.png]
```

