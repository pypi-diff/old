# Comparing `tmp/ScribePy-0.1.1.tar.gz` & `tmp/ScribePy-0.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "ScribePy-0.1.1.tar", last modified: Thu Apr  6 14:52:48 2023, max compression
+gzip compressed data, was "ScribePy-0.1.2.tar", last modified: Thu Apr  6 15:09:17 2023, max compression
```

## Comparing `ScribePy-0.1.1.tar` & `ScribePy-0.1.2.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:52:48.987203 ScribePy-0.1.1/
--rw-r--r--   0 fcarva844   (501) staff       (20)    11357 2023-04-06 13:47:41.000000 ScribePy-0.1.1/LICENSE
--rw-r--r--   0 fcarva844   (501) staff       (20)    15824 2023-04-06 14:52:48.986548 ScribePy-0.1.1/PKG-INFO
--rw-r--r--   0 fcarva844   (501) staff       (20)     1996 2023-04-06 14:12:48.000000 ScribePy-0.1.1/README.md
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:52:48.981059 ScribePy-0.1.1/ScribePy.egg-info/
--rw-r--r--   0 fcarva844   (501) staff       (20)    15824 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/PKG-INFO
--rw-r--r--   0 fcarva844   (501) staff       (20)      283 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/SOURCES.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)        1 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/dependency_links.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)       32 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/requires.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)        9 2023-04-06 14:52:48.000000 ScribePy-0.1.1/ScribePy.egg-info/top_level.txt
--rw-r--r--   0 fcarva844   (501) staff       (20)      868 2023-04-06 14:52:35.000000 ScribePy-0.1.1/pyproject.toml
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:52:48.982951 ScribePy-0.1.1/scribepy/
--rw-r--r--   0 fcarva844   (501) staff       (20)       24 2023-04-06 13:59:46.000000 ScribePy-0.1.1/scribepy/__init__.py
--rw-r--r--   0 fcarva844   (501) staff       (20)      894 2023-04-06 13:59:36.000000 ScribePy-0.1.1/scribepy/scribepy.py
--rw-r--r--   0 fcarva844   (501) staff       (20)      445 2023-04-06 13:59:17.000000 ScribePy-0.1.1/scribepy/utils.py
--rw-r--r--   0 fcarva844   (501) staff       (20)       38 2023-04-06 14:52:48.987319 ScribePy-0.1.1/setup.cfg
--rw-r--r--   0 fcarva844   (501) staff       (20)     1038 2023-04-06 14:44:00.000000 ScribePy-0.1.1/setup.py
-drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 14:52:48.984925 ScribePy-0.1.1/tests/
--rw-r--r--   0 fcarva844   (501) staff       (20)      359 2023-04-06 14:21:22.000000 ScribePy-0.1.1/tests/test_scribepy.py
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 15:09:17.151427 ScribePy-0.1.2/
+-rw-r--r--   0 fcarva844   (501) staff       (20)    11357 2023-04-06 13:47:41.000000 ScribePy-0.1.2/LICENSE
+-rw-r--r--   0 fcarva844   (501) staff       (20)    15824 2023-04-06 15:09:17.150941 ScribePy-0.1.2/PKG-INFO
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1996 2023-04-06 14:12:48.000000 ScribePy-0.1.2/README.md
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 15:09:17.141541 ScribePy-0.1.2/ScribePy.egg-info/
+-rw-r--r--   0 fcarva844   (501) staff       (20)    15824 2023-04-06 15:09:17.000000 ScribePy-0.1.2/ScribePy.egg-info/PKG-INFO
+-rw-r--r--   0 fcarva844   (501) staff       (20)      283 2023-04-06 15:09:17.000000 ScribePy-0.1.2/ScribePy.egg-info/SOURCES.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)        1 2023-04-06 15:09:17.000000 ScribePy-0.1.2/ScribePy.egg-info/dependency_links.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)       32 2023-04-06 15:09:17.000000 ScribePy-0.1.2/ScribePy.egg-info/requires.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)        9 2023-04-06 15:09:17.000000 ScribePy-0.1.2/ScribePy.egg-info/top_level.txt
+-rw-r--r--   0 fcarva844   (501) staff       (20)      868 2023-04-06 15:08:57.000000 ScribePy-0.1.2/pyproject.toml
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 15:09:17.146223 ScribePy-0.1.2/scribepy/
+-rw-r--r--   0 fcarva844   (501) staff       (20)       24 2023-04-06 13:59:46.000000 ScribePy-0.1.2/scribepy/__init__.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)      894 2023-04-06 15:02:56.000000 ScribePy-0.1.2/scribepy/scribepy.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)      445 2023-04-06 13:59:17.000000 ScribePy-0.1.2/scribepy/utils.py
+-rw-r--r--   0 fcarva844   (501) staff       (20)       38 2023-04-06 15:09:17.151628 ScribePy-0.1.2/setup.cfg
+-rw-r--r--   0 fcarva844   (501) staff       (20)     1038 2023-04-06 15:08:52.000000 ScribePy-0.1.2/setup.py
+drwxr-xr-x   0 fcarva844   (501) staff       (20)        0 2023-04-06 15:09:17.148203 ScribePy-0.1.2/tests/
+-rw-r--r--   0 fcarva844   (501) staff       (20)      359 2023-04-06 15:06:43.000000 ScribePy-0.1.2/tests/test_scribepy.py
```

### Comparing `ScribePy-0.1.1/LICENSE` & `ScribePy-0.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `ScribePy-0.1.1/PKG-INFO` & `ScribePy-0.1.2/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ScribePy
-Version: 0.1.1
+Version: 0.1.2
 Summary: Python library for generating documentation
 Home-page: https://github.com/hipnologo/ScribePy
 Author: Fabio Carvalho
 Author-email: Fabio Carvalho <hipnologo@gmail.com>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
```

### Comparing `ScribePy-0.1.1/README.md` & `ScribePy-0.1.2/README.md`

 * *Files identical despite different names*

### Comparing `ScribePy-0.1.1/ScribePy.egg-info/PKG-INFO` & `ScribePy-0.1.2/ScribePy.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ScribePy
-Version: 0.1.1
+Version: 0.1.2
 Summary: Python library for generating documentation
 Home-page: https://github.com/hipnologo/ScribePy
 Author: Fabio Carvalho
 Author-email: Fabio Carvalho <hipnologo@gmail.com>
 License:                                  Apache License
                                    Version 2.0, January 2004
                                 http://www.apache.org/licenses/
```

### Comparing `ScribePy-0.1.1/pyproject.toml` & `ScribePy-0.1.2/pyproject.toml`

 * *Files 11% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "ScribePy"
-version = "0.1.1"
+version = "0.1.2"
 description = "Python library for generating documentation"
 authors = [
   { name="Fabio Carvalho", email="hipnologo@gmail.com" },
 ]
 readme = "README.md"
 keywords = ["documentation", "python"]
 classifiers = [
```

### Comparing `ScribePy-0.1.1/scribepy/scribepy.py` & `ScribePy-0.1.2/scribepy/scribepy.py`

 * *Files 23% similar despite different names*

```diff
@@ -11,15 +11,15 @@
     """
     lexer = get_lexer_by_name('python', stripall=True)
     formatter = html.HtmlFormatter()
     highlighted_code = highlight(source_code, lexer, formatter)
     markdown_code = markdown(highlighted_code, extensions=['markdown.extensions.tables'])
     return markdown_code
 
-class scribepy:
+class ScribePy:
     """
     A class for generating documentation from Python source code.
     """
     def __init__(self, source_code):
         self.source_code = source_code
 
     def generate_html_docs(self):
```

### Comparing `ScribePy-0.1.1/setup.py` & `ScribePy-0.1.2/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setup(
     name='ScribePy',
-    version='0.1.1',
+    version='0.1.2',
     description='Python library for generating documentation',
     long_description=long_description,
     long_description_content_type="text/markdown",
     url='https://github.com/hipnologo/ScribePy',
     author='Fabio Carvalho',
     author_email='hipnologo@gmail.com',
     license='Apache License, Version 2.0',
```

