# Comparing `tmp/rpaframework_pdf-7.1.4.tar.gz` & `tmp/rpaframework_pdf-7.1.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "rpaframework_pdf-7.1.4.tar", max compression
+gzip compressed data, was "rpaframework_pdf-7.1.5.tar", max compression
```

## Comparing `rpaframework_pdf-7.1.4.tar` & `rpaframework_pdf-7.1.5.tar`

### file list

```diff
@@ -1,15 +1,15 @@
--rw-r--r--   0        0        0    11358 2021-09-09 09:55:26.451320 rpaframework_pdf-7.1.4/LICENSE
--rw-r--r--   0        0        0      187 2021-09-09 09:55:26.451408 rpaframework_pdf-7.1.4/README.rst
--rw-r--r--   0        0        0    59021 2023-04-05 08:31:51.897271 rpaframework_pdf-7.1.4/RPA_PDF.libspec
--rw-r--r--   0        0        0     1920 2023-04-05 08:26:32.484729 rpaframework_pdf-7.1.4/pyproject.toml
--rw-r--r--   0        0        0     4047 2023-03-31 12:08:05.029080 rpaframework_pdf-7.1.4/src/RPA/PDF/__init__.py
--rw-r--r--   0        0        0   316100 2022-09-09 11:28:10.260100 rpaframework_pdf-7.1.4/src/RPA/PDF/assets/Inter-Bold.ttf
--rw-r--r--   0        0        0   265920 2022-09-09 11:28:10.261375 rpaframework_pdf-7.1.4/src/RPA/PDF/assets/Inter-BoldItalic.ttf
--rw-r--r--   0        0        0   263548 2022-09-09 11:28:10.263934 rpaframework_pdf-7.1.4/src/RPA/PDF/assets/Inter-Italic.ttf
--rw-r--r--   0        0        0   309828 2022-09-09 11:28:10.265438 rpaframework_pdf-7.1.4/src/RPA/PDF/assets/Inter-Regular.ttf
--rw-r--r--   0        0        0      258 2023-02-03 14:24:02.149967 rpaframework_pdf-7.1.4/src/RPA/PDF/keywords/__init__.py
--rw-r--r--   0        0        0      789 2022-09-09 11:28:10.265897 rpaframework_pdf-7.1.4/src/RPA/PDF/keywords/context.py
--rw-r--r--   0        0        0    44846 2023-03-31 12:08:05.029474 rpaframework_pdf-7.1.4/src/RPA/PDF/keywords/document.py
--rw-r--r--   0        0        0    16873 2023-02-03 14:24:02.150961 rpaframework_pdf-7.1.4/src/RPA/PDF/keywords/finder.py
--rw-r--r--   0        0        0    32447 2023-03-15 11:45:26.906753 rpaframework_pdf-7.1.4/src/RPA/PDF/keywords/model.py
--rw-r--r--   0        0        0     1794 1970-01-01 00:00:00.000000 rpaframework_pdf-7.1.4/PKG-INFO
+-rw-r--r--   0        0        0    11358 2021-09-09 09:55:26.451320 rpaframework_pdf-7.1.5/LICENSE
+-rw-r--r--   0        0        0      187 2021-09-09 09:55:26.451408 rpaframework_pdf-7.1.5/README.rst
+-rw-r--r--   0        0        0    59021 2023-04-07 09:38:15.855855 rpaframework_pdf-7.1.5/RPA_PDF.libspec
+-rw-r--r--   0        0        0     1920 2023-04-07 09:37:40.112345 rpaframework_pdf-7.1.5/pyproject.toml
+-rw-r--r--   0        0        0     4047 2023-03-31 12:08:05.029080 rpaframework_pdf-7.1.5/src/RPA/PDF/__init__.py
+-rw-r--r--   0        0        0   316100 2022-09-09 11:28:10.260100 rpaframework_pdf-7.1.5/src/RPA/PDF/assets/Inter-Bold.ttf
+-rw-r--r--   0        0        0   265920 2022-09-09 11:28:10.261375 rpaframework_pdf-7.1.5/src/RPA/PDF/assets/Inter-BoldItalic.ttf
+-rw-r--r--   0        0        0   263548 2022-09-09 11:28:10.263934 rpaframework_pdf-7.1.5/src/RPA/PDF/assets/Inter-Italic.ttf
+-rw-r--r--   0        0        0   309828 2022-09-09 11:28:10.265438 rpaframework_pdf-7.1.5/src/RPA/PDF/assets/Inter-Regular.ttf
+-rw-r--r--   0        0        0      258 2023-02-03 14:24:02.149967 rpaframework_pdf-7.1.5/src/RPA/PDF/keywords/__init__.py
+-rw-r--r--   0        0        0      789 2022-09-09 11:28:10.265897 rpaframework_pdf-7.1.5/src/RPA/PDF/keywords/context.py
+-rw-r--r--   0        0        0    44846 2023-03-31 12:08:05.029474 rpaframework_pdf-7.1.5/src/RPA/PDF/keywords/document.py
+-rw-r--r--   0        0        0    16873 2023-02-03 14:24:02.150961 rpaframework_pdf-7.1.5/src/RPA/PDF/keywords/finder.py
+-rw-r--r--   0        0        0    32447 2023-03-15 11:45:26.906753 rpaframework_pdf-7.1.5/src/RPA/PDF/keywords/model.py
+-rw-r--r--   0        0        0     1794 1970-01-01 00:00:00.000000 rpaframework_pdf-7.1.5/PKG-INFO
```

### Comparing `rpaframework_pdf-7.1.4/LICENSE` & `rpaframework_pdf-7.1.5/LICENSE`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/RPA_PDF.libspec` & `rpaframework_pdf-7.1.5/RPA_PDF.libspec`

 * *Files 0% similar despite different names*

#### Comparing `rpaframework_pdf-7.1.4/RPA_PDF.libspec` & `rpaframework_pdf-7.1.5/RPA_PDF.libspec`

```diff
@@ -1,9 +1,9 @@
 <?xml version="1.0" encoding="utf-8"?>
-<keywordspec name="RPA.PDF" type="LIBRARY" format="REST" scope="GLOBAL" generated="2023-04-05T08:31:51Z" specversion="4" source="./RPA/PDF/__init__.py" lineno="11">
+<keywordspec name="RPA.PDF" type="LIBRARY" format="REST" scope="GLOBAL" generated="2023-04-07T09:38:15Z" specversion="4" source="./RPA/PDF/__init__.py" lineno="11">
   <version/>
   <doc>`PDF` is a library for managing PDF documents.
 
 It can be used to extract text from PDFs, add watermarks to pages, and
 decrypt/encrypt documents.
 
 Merging and splitting PDFs is supported by ``Add Files To PDF`` keyword. Read
```

### Comparing `rpaframework_pdf-7.1.4/pyproject.toml` & `rpaframework_pdf-7.1.5/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "rpaframework-pdf"
-version = "7.1.4"
+version = "7.1.5"
 description = "PDF library of RPA Framework"
 authors = ["RPA Framework <rpafw@robocorp.com>"]
 license = "Apache-2.0"
 readme = "README.rst"
 
 homepage = "https://rpaframework.org/"
 documentation = "https://rpaframework.org/"
@@ -31,16 +31,16 @@
 
 [tool.poetry.dependencies]
 python = "^3.7"
 rpaframework-core = "^11.0.0"
 robotframework = ">=4.0.0,!=4.0.1,<6.0.0"
 robotframework-pythonlibcore = "^4.0.0"
 "pdfminer.six" = "20221105"
-pypdf = "^3.2.0"
-fpdf2 = "^2.6.0"
+pypdf = "^3.7.0"
+fpdf2 = "^2.7.3"
 
 [tool.poetry.group.dev.dependencies]
 black = "^22.3.0"
 flake8 = "^3.7.9"
 pylint = "^2.4.4"
 pytest = "^7.2.0"
 mock = "^5.0.0"
```

### Comparing `rpaframework_pdf-7.1.4/src/RPA/PDF/__init__.py` & `rpaframework_pdf-7.1.5/src/RPA/PDF/__init__.py`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/src/RPA/PDF/assets/Inter-Bold.ttf` & `rpaframework_pdf-7.1.5/src/RPA/PDF/assets/Inter-Bold.ttf`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/src/RPA/PDF/assets/Inter-BoldItalic.ttf` & `rpaframework_pdf-7.1.5/src/RPA/PDF/assets/Inter-BoldItalic.ttf`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/src/RPA/PDF/assets/Inter-Italic.ttf` & `rpaframework_pdf-7.1.5/src/RPA/PDF/assets/Inter-Italic.ttf`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/src/RPA/PDF/assets/Inter-Regular.ttf` & `rpaframework_pdf-7.1.5/src/RPA/PDF/assets/Inter-Regular.ttf`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/src/RPA/PDF/keywords/context.py` & `rpaframework_pdf-7.1.5/src/RPA/PDF/keywords/context.py`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/src/RPA/PDF/keywords/document.py` & `rpaframework_pdf-7.1.5/src/RPA/PDF/keywords/document.py`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/src/RPA/PDF/keywords/finder.py` & `rpaframework_pdf-7.1.5/src/RPA/PDF/keywords/finder.py`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/src/RPA/PDF/keywords/model.py` & `rpaframework_pdf-7.1.5/src/RPA/PDF/keywords/model.py`

 * *Files identical despite different names*

### Comparing `rpaframework_pdf-7.1.4/PKG-INFO` & `rpaframework_pdf-7.1.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: rpaframework-pdf
-Version: 7.1.4
+Version: 7.1.5
 Summary: PDF library of RPA Framework
 Home-page: https://rpaframework.org/
 License: Apache-2.0
 Keywords: robotframework,rpa,automation,pdf
 Author: RPA Framework
 Author-email: rpafw@robocorp.com
 Requires-Python: >=3.7,<4.0
@@ -21,17 +21,17 @@
 Classifier: Programming Language :: Python :: 3.10
 Classifier: Programming Language :: Python :: 3.11
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Classifier: Topic :: Software Development :: Libraries
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
-Requires-Dist: fpdf2 (>=2.6.0,<3.0.0)
+Requires-Dist: fpdf2 (>=2.7.3,<3.0.0)
 Requires-Dist: pdfminer.six (==20221105)
-Requires-Dist: pypdf (>=3.2.0,<4.0.0)
+Requires-Dist: pypdf (>=3.7.0,<4.0.0)
 Requires-Dist: robotframework (>=4.0.0,!=4.0.1,<6.0.0)
 Requires-Dist: robotframework-pythonlibcore (>=4.0.0,<5.0.0)
 Requires-Dist: rpaframework-core (>=11.0.0,<12.0.0)
 Project-URL: Documentation, https://rpaframework.org/
 Project-URL: Repository, https://github.com/robocorp/rpaframework
 Description-Content-Type: text/x-rst
```

