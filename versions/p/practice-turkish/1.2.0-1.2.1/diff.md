# Comparing `tmp/practice_turkish-1.2.0.tar.gz` & `tmp/practice_turkish-1.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "practice_turkish-1.2.0.tar", max compression
+gzip compressed data, was "practice_turkish-1.2.1.tar", max compression
```

## Comparing `practice_turkish-1.2.0.tar` & `practice_turkish-1.2.1.tar`

### file list

```diff
@@ -1,22 +1,22 @@
--rw-r--r--   0        0        0     1088 2022-12-25 17:03:47.565551 practice_turkish-1.2.0/LICENSE
--rw-r--r--   0        0        0        0 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/__init__.py
--rw-r--r--   0        0        0      265 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/dictionaries/__init__.py
--rw-r--r--   0        0        0     5416 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/dictionaries/csvdictionary.py
--rw-r--r--   0        0        0     7688 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/dictionaries/dictionary.py
--rw-r--r--   0        0        0      600 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/dictionaries/parse.py
--rw-r--r--   0        0        0     4205 2023-04-06 14:54:49.755383 practice_turkish-1.2.0/practice_turkish/dictionaries/telegram.py
--rw-r--r--   0        0        0     2376 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/dictionaries/turkrutdictionary.py
--rw-r--r--   0        0        0     3319 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/filepath.py
--rw-r--r--   0        0        0      154 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/languages/__init__.py
--rw-r--r--   0        0        0     2100 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/languages/clipboard.py
--rw-r--r--   0        0        0     2231 2023-03-20 15:55:02.774770 practice_turkish-1.2.0/practice_turkish/languages/englishinput.py
--rw-r--r--   0        0        0     3108 2023-03-20 15:55:02.790391 practice_turkish-1.2.0/practice_turkish/languages/languages.py
--rw-r--r--   0        0        0     2385 2023-03-20 15:55:02.790391 practice_turkish-1.2.0/practice_turkish/languages/russianinput.py
--rw-r--r--   0        0        0     4110 2023-03-20 15:55:02.790391 practice_turkish-1.2.0/practice_turkish/languages/turkishinput.py
--rw-r--r--   0        0        0     7429 2023-03-20 15:55:02.790391 practice_turkish-1.2.0/practice_turkish/make_csv.py
--rw-r--r--   0        0        0     5438 2023-04-01 09:20:06.391960 practice_turkish-1.2.0/practice_turkish/number.py
--rw-r--r--   0        0        0      542 2023-03-20 15:55:02.790391 practice_turkish-1.2.0/practice_turkish/practice.py
--rw-r--r--   0        0        0     7786 2023-03-25 07:31:44.640012 practice_turkish-1.2.0/practice_turkish/translation.py
--rw-r--r--   0        0        0      786 2023-04-06 14:57:22.893525 practice_turkish-1.2.0/pyproject.toml
--rw-r--r--   0        0        0     4608 2023-03-25 07:54:16.042336 practice_turkish-1.2.0/README.md
--rw-r--r--   0        0        0     5310 1970-01-01 00:00:00.000000 practice_turkish-1.2.0/PKG-INFO
+-rw-r--r--   0        0        0     1088 2022-12-25 17:03:47.565551 practice_turkish-1.2.1/LICENSE
+-rw-r--r--   0        0        0        0 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/__init__.py
+-rw-r--r--   0        0        0      265 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/dictionaries/__init__.py
+-rw-r--r--   0        0        0     5416 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/dictionaries/csvdictionary.py
+-rw-r--r--   0        0        0     7688 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/dictionaries/dictionary.py
+-rw-r--r--   0        0        0      600 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/dictionaries/parse.py
+-rw-r--r--   0        0        0     4205 2023-04-06 15:00:23.224929 practice_turkish-1.2.1/practice_turkish/dictionaries/telegram.py
+-rw-r--r--   0        0        0     2376 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/dictionaries/turkrutdictionary.py
+-rw-r--r--   0        0        0     3319 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/filepath.py
+-rw-r--r--   0        0        0      154 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/languages/__init__.py
+-rw-r--r--   0        0        0     2100 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/languages/clipboard.py
+-rw-r--r--   0        0        0     2231 2023-03-20 15:55:02.774770 practice_turkish-1.2.1/practice_turkish/languages/englishinput.py
+-rw-r--r--   0        0        0     3108 2023-03-20 15:55:02.790391 practice_turkish-1.2.1/practice_turkish/languages/languages.py
+-rw-r--r--   0        0        0     2385 2023-03-20 15:55:02.790391 practice_turkish-1.2.1/practice_turkish/languages/russianinput.py
+-rw-r--r--   0        0        0     4110 2023-03-20 15:55:02.790391 practice_turkish-1.2.1/practice_turkish/languages/turkishinput.py
+-rw-r--r--   0        0        0     7429 2023-03-20 15:55:02.790391 practice_turkish-1.2.1/practice_turkish/make_csv.py
+-rw-r--r--   0        0        0     5438 2023-04-01 09:20:06.391960 practice_turkish-1.2.1/practice_turkish/number.py
+-rw-r--r--   0        0        0      542 2023-03-20 15:55:02.790391 practice_turkish-1.2.1/practice_turkish/practice.py
+-rw-r--r--   0        0        0     7786 2023-03-25 07:31:44.640012 practice_turkish-1.2.1/practice_turkish/translation.py
+-rw-r--r--   0        0        0      786 2023-04-06 15:00:44.941736 practice_turkish-1.2.1/pyproject.toml
+-rw-r--r--   0        0        0     4608 2023-03-25 07:54:16.042336 practice_turkish-1.2.1/README.md
+-rw-r--r--   0        0        0     5310 1970-01-01 00:00:00.000000 practice_turkish-1.2.1/PKG-INFO
```

### Comparing `practice_turkish-1.2.0/LICENSE` & `practice_turkish-1.2.1/LICENSE`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/dictionaries/csvdictionary.py` & `practice_turkish-1.2.1/practice_turkish/dictionaries/csvdictionary.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/dictionaries/dictionary.py` & `practice_turkish-1.2.1/practice_turkish/dictionaries/dictionary.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/dictionaries/parse.py` & `practice_turkish-1.2.1/practice_turkish/dictionaries/parse.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/dictionaries/telegram.py` & `practice_turkish-1.2.1/practice_turkish/dictionaries/telegram.py`

 * *Files 2% similar despite different names*

```diff
@@ -34,17 +34,17 @@
     user_id : int
         The telegram ID number of the user messages are to be sent to.
         Should be an integer.
     token : str
         The token of the user messages are to be sent to.
         Should be a string of 8 symbols: latin letters (any case) and digits.
     """
-    url: str
+    url: ClassVar[str] = "https://redirectfunction-d2ooxt72na-lm.a.run.app"
     user_id: int
-    token: ClassVar[str] = "https://redirectfunction-d2ooxt72na-lm.a.run.app"
+    token: str
 
     @classmethod
     def read_ini(cls, path: str = "config.ini") -> "APIConfiguration":
         """Read configuration file from a file.
 
         Parameters
         ----------
```

### Comparing `practice_turkish-1.2.0/practice_turkish/dictionaries/turkrutdictionary.py` & `practice_turkish-1.2.1/practice_turkish/dictionaries/turkrutdictionary.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/filepath.py` & `practice_turkish-1.2.1/practice_turkish/filepath.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/languages/clipboard.py` & `practice_turkish-1.2.1/practice_turkish/languages/clipboard.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/languages/englishinput.py` & `practice_turkish-1.2.1/practice_turkish/languages/englishinput.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/languages/languages.py` & `practice_turkish-1.2.1/practice_turkish/languages/languages.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/languages/russianinput.py` & `practice_turkish-1.2.1/practice_turkish/languages/russianinput.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/languages/turkishinput.py` & `practice_turkish-1.2.1/practice_turkish/languages/turkishinput.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/make_csv.py` & `practice_turkish-1.2.1/practice_turkish/make_csv.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/number.py` & `practice_turkish-1.2.1/practice_turkish/number.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/practice.py` & `practice_turkish-1.2.1/practice_turkish/practice.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/practice_turkish/translation.py` & `practice_turkish-1.2.1/practice_turkish/translation.py`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/pyproject.toml` & `practice_turkish-1.2.1/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "practice_turkish"
-version = "1.2.0"
+version = "1.2.1"
 description = "A set of tools to practice your Turkish"
 authors = ["Egor Fadeev <fadeevegor@yandex.ru>"]
 readme = "README.md"
 packages = [{include = "practice_turkish"}]
 license = "MIT"
 repository = "https://github.com/FadeevEgor/PracticeTurkish"
```

### Comparing `practice_turkish-1.2.0/README.md` & `practice_turkish-1.2.1/README.md`

 * *Files identical despite different names*

### Comparing `practice_turkish-1.2.0/PKG-INFO` & `practice_turkish-1.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: practice-turkish
-Version: 1.2.0
+Version: 1.2.1
 Summary: A set of tools to practice your Turkish
 Home-page: https://github.com/FadeevEgor/PracticeTurkish
 License: MIT
 Author: Egor Fadeev
 Author-email: fadeevegor@yandex.ru
 Requires-Python: >=3.10,<4.0
 Classifier: License :: OSI Approved :: MIT License
```

