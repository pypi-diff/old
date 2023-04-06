# Comparing `tmp/tradingpattern-0.0.2.tar.gz` & `tmp/tradingpattern-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "tradingpattern-0.0.2.tar", max compression
+gzip compressed data, was "tradingpattern-0.0.5.tar", max compression
```

## Comparing `tradingpattern-0.0.2.tar` & `tradingpattern-0.0.5.tar`

### file list

```diff
@@ -1,7 +1,7 @@
--rw-r--r--   0        0        0     1415 2023-04-04 12:56:27.810000 tradingpattern-0.0.2/LICENSE.md
--rw-r--r--   0        0        0     3718 2023-04-04 12:56:27.810000 tradingpattern-0.0.2/README.md
--rw-r--r--   0        0        0      655 2023-04-05 16:33:47.740000 tradingpattern-0.0.2/pyproject.toml
--rw-r--r--   0        0        0        0 2023-04-04 12:56:27.810000 tradingpattern-0.0.2/tradingpatterns/__init__.py
--rw-r--r--   0        0        0     1328 2023-04-04 12:56:27.810000 tradingpattern-0.0.2/tradingpatterns/hard_data.py
--rw-r--r--   0        0        0    10359 2023-04-04 12:56:27.810000 tradingpattern-0.0.2/tradingpatterns/tradingpatterns.py
--rw-r--r--   0        0        0     4414 1970-01-01 00:00:00.000000 tradingpattern-0.0.2/PKG-INFO
+-rw-r--r--   0        0        0     1415 2023-04-06 08:05:16.253889 tradingpattern-0.0.5/LICENSE.md
+-rw-r--r--   0        0        0     3718 2023-04-06 08:05:16.257890 tradingpattern-0.0.5/README.md
+-rw-r--r--   0        0        0      655 2023-04-06 08:05:30.490060 tradingpattern-0.0.5/pyproject.toml
+-rw-r--r--   0        0        0        0 2023-04-06 08:05:16.257890 tradingpattern-0.0.5/tradingpatterns/__init__.py
+-rw-r--r--   0        0        0     1328 2023-04-06 08:05:16.257890 tradingpattern-0.0.5/tradingpatterns/hard_data.py
+-rw-r--r--   0        0        0    10359 2023-04-06 08:05:16.257890 tradingpattern-0.0.5/tradingpatterns/tradingpatterns.py
+-rw-r--r--   0        0        0     4414 1970-01-01 00:00:00.000000 tradingpattern-0.0.5/PKG-INFO
```

### Comparing `tradingpattern-0.0.2/LICENSE.md` & `tradingpattern-0.0.5/LICENSE.md`

 * *Files identical despite different names*

### Comparing `tradingpattern-0.0.2/README.md` & `tradingpattern-0.0.5/README.md`

 * *Files identical despite different names*

### Comparing `tradingpattern-0.0.2/pyproject.toml` & `tradingpattern-0.0.5/pyproject.toml`

 * *Files 15% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "tradingpattern"
-version = "0.0.2"
+version = "0.0.5"
 repository = "https://github.com/white07S/TradingPatternScanner"
 description = "Trading Pattern Scanner Identifies complex patterns like head and shoulder, wedge and many more."
 authors = ["Preetam Sharma"]
 license = "CC BY-NC-SA 4.0"
 readme = "README.md"
 packages = [
     { include = "tradingpatterns" }
```

### Comparing `tradingpattern-0.0.2/tradingpatterns/hard_data.py` & `tradingpattern-0.0.5/tradingpatterns/hard_data.py`

 * *Files identical despite different names*

### Comparing `tradingpattern-0.0.2/tradingpatterns/tradingpatterns.py` & `tradingpattern-0.0.5/tradingpatterns/tradingpatterns.py`

 * *Files identical despite different names*

### Comparing `tradingpattern-0.0.2/PKG-INFO` & `tradingpattern-0.0.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tradingpattern
-Version: 0.0.2
+Version: 0.0.5
 Summary: Trading Pattern Scanner Identifies complex patterns like head and shoulder, wedge and many more.
 Home-page: https://github.com/white07S/TradingPatternScanner
 License: CC BY-NC-SA 4.0
 Author: Preetam Sharma
 Requires-Python: >=3.10,<4.0
 Classifier: License :: Other/Proprietary License
 Classifier: Programming Language :: Python :: 3
```

