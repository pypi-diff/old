# Comparing `tmp/eboekhouden_python-0.1.6.tar.gz` & `tmp/eboekhouden_python-0.1.7.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "eboekhouden_python-0.1.6.tar", max compression
+gzip compressed data, was "eboekhouden_python-0.1.7.tar", max compression
```

## Comparing `eboekhouden_python-0.1.6.tar` & `eboekhouden_python-0.1.7.tar`

### file list

```diff
@@ -1,18 +1,18 @@
--rw-r--r--   0        0        0     1071 2023-04-03 11:53:59.399776 eboekhouden_python-0.1.6/LICENSE
--rw-r--r--   0        0        0     1200 2023-04-03 11:41:12.021970 eboekhouden_python-0.1.6/README.md
--rw-r--r--   0        0        0      266 2023-04-05 20:13:02.774431 eboekhouden_python-0.1.6/eboekhouden_python/__init__.py
--rw-r--r--   0        0        0      385 2023-04-03 16:59:55.203583 eboekhouden_python-0.1.6/eboekhouden_python/constants/__init__.py
--rw-r--r--   0        0        0      247 2023-04-03 16:59:40.940120 eboekhouden_python-0.1.6/eboekhouden_python/constants/bedrijf_particulier.py
--rw-r--r--   0        0        0     1964 2023-04-03 14:17:12.994123 eboekhouden_python-0.1.6/eboekhouden_python/constants/btw_code.py
--rw-r--r--   0        0        0      272 2023-04-03 13:40:19.527704 eboekhouden_python-0.1.6/eboekhouden_python/constants/in_ex_btw.py
--rw-r--r--   0        0        0      623 2023-04-05 19:46:16.173697 eboekhouden_python-0.1.6/eboekhouden_python/constants/mutatie_soort.py
--rw-r--r--   0        0        0      235 2023-04-03 14:17:30.188459 eboekhouden_python-0.1.6/eboekhouden_python/constants/string_enum.py
--rw-r--r--   0        0        0     5180 2023-04-03 20:02:13.785039 eboekhouden_python-0.1.6/eboekhouden_python/eboekhouden_client.py
--rw-r--r--   0        0        0      302 2023-04-03 17:02:41.185239 eboekhouden_python-0.1.6/eboekhouden_python/models/__init__.py
--rw-r--r--   0        0        0     4432 2023-04-05 20:07:24.969738 eboekhouden_python-0.1.6/eboekhouden_python/models/mutatie.py
--rw-r--r--   0        0        0     1361 2023-04-03 17:08:37.346890 eboekhouden_python-0.1.6/eboekhouden_python/models/mutatie_filter.py
--rw-r--r--   0        0        0     2397 2023-04-04 06:03:35.645610 eboekhouden_python-0.1.6/eboekhouden_python/models/mutatie_regel.py
--rw-r--r--   0        0        0     4568 2023-04-04 06:03:35.668723 eboekhouden_python-0.1.6/eboekhouden_python/models/relatie.py
--rw-r--r--   0        0        0      735 2023-04-03 19:45:53.253119 eboekhouden_python-0.1.6/eboekhouden_python/models/relatie_filter.py
--rw-r--r--   0        0        0      954 2023-04-05 20:12:53.935996 eboekhouden_python-0.1.6/pyproject.toml
--rw-r--r--   0        0        0     2006 1970-01-01 00:00:00.000000 eboekhouden_python-0.1.6/PKG-INFO
+-rw-r--r--   0        0        0     1071 2023-04-03 11:53:59.399776 eboekhouden_python-0.1.7/LICENSE
+-rw-r--r--   0        0        0     1200 2023-04-03 11:41:12.021970 eboekhouden_python-0.1.7/README.md
+-rw-r--r--   0        0        0      153 2023-04-06 13:25:08.895807 eboekhouden_python-0.1.7/eboekhouden_python/__init__.py
+-rw-r--r--   0        0        0      399 2023-04-06 13:05:26.446485 eboekhouden_python-0.1.7/eboekhouden_python/constants/__init__.py
+-rw-r--r--   0        0        0      247 2023-04-03 16:59:40.940120 eboekhouden_python-0.1.7/eboekhouden_python/constants/bedrijf_particulier.py
+-rw-r--r--   0        0        0     1964 2023-04-03 14:17:12.994123 eboekhouden_python-0.1.7/eboekhouden_python/constants/btw_code.py
+-rw-r--r--   0        0        0      272 2023-04-03 13:40:19.527704 eboekhouden_python-0.1.7/eboekhouden_python/constants/in_ex_btw.py
+-rw-r--r--   0        0        0      623 2023-04-05 19:46:16.173697 eboekhouden_python-0.1.7/eboekhouden_python/constants/mutatie_soort.py
+-rw-r--r--   0        0        0      235 2023-04-03 14:17:30.188459 eboekhouden_python-0.1.7/eboekhouden_python/constants/string_enum.py
+-rw-r--r--   0        0        0     5180 2023-04-03 20:02:13.785039 eboekhouden_python-0.1.7/eboekhouden_python/eboekhouden_client.py
+-rw-r--r--   0        0        0      312 2023-04-06 13:05:08.348133 eboekhouden_python-0.1.7/eboekhouden_python/models/__init__.py
+-rw-r--r--   0        0        0     4432 2023-04-05 20:07:24.969738 eboekhouden_python-0.1.7/eboekhouden_python/models/mutatie.py
+-rw-r--r--   0        0        0     1361 2023-04-03 17:08:37.346890 eboekhouden_python-0.1.7/eboekhouden_python/models/mutatie_filter.py
+-rw-r--r--   0        0        0     2397 2023-04-04 06:03:35.645610 eboekhouden_python-0.1.7/eboekhouden_python/models/mutatie_regel.py
+-rw-r--r--   0        0        0     4568 2023-04-04 06:03:35.668723 eboekhouden_python-0.1.7/eboekhouden_python/models/relatie.py
+-rw-r--r--   0        0        0      735 2023-04-03 19:45:53.253119 eboekhouden_python-0.1.7/eboekhouden_python/models/relatie_filter.py
+-rw-r--r--   0        0        0      954 2023-04-06 13:23:21.997172 eboekhouden_python-0.1.7/pyproject.toml
+-rw-r--r--   0        0        0     2006 1970-01-01 00:00:00.000000 eboekhouden_python-0.1.7/PKG-INFO
```

### Comparing `eboekhouden_python-0.1.6/LICENSE` & `eboekhouden_python-0.1.7/LICENSE`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/README.md` & `eboekhouden_python-0.1.7/README.md`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/eboekhouden_python/constants/btw_code.py` & `eboekhouden_python-0.1.7/eboekhouden_python/constants/btw_code.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/eboekhouden_python/constants/mutatie_soort.py` & `eboekhouden_python-0.1.7/eboekhouden_python/constants/mutatie_soort.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/eboekhouden_python/eboekhouden_client.py` & `eboekhouden_python-0.1.7/eboekhouden_python/eboekhouden_client.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/eboekhouden_python/models/mutatie.py` & `eboekhouden_python-0.1.7/eboekhouden_python/models/mutatie.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/eboekhouden_python/models/mutatie_filter.py` & `eboekhouden_python-0.1.7/eboekhouden_python/models/mutatie_filter.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/eboekhouden_python/models/mutatie_regel.py` & `eboekhouden_python-0.1.7/eboekhouden_python/models/mutatie_regel.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/eboekhouden_python/models/relatie.py` & `eboekhouden_python-0.1.7/eboekhouden_python/models/relatie.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/eboekhouden_python/models/relatie_filter.py` & `eboekhouden_python-0.1.7/eboekhouden_python/models/relatie_filter.py`

 * *Files identical despite different names*

### Comparing `eboekhouden_python-0.1.6/pyproject.toml` & `eboekhouden_python-0.1.7/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "eboekhouden-python"
-version = "0.1.6"
+version = "0.1.7"
 description = "This is a simple API client for the E-boekhouden.nl API. It is written in Python and uses the ZEEP library."
 authors = ["Dennis Bakhuis <pypi@bakhuis.nu>"]
 readme = "README.md"
 packages = [{include = "eboekhouden_python"}]
 license = "MIT"
 homepage = "https://github.com/dennisbakhuis/eboekhouden-python"
 repository = "https://github.com/dennisbakhuis/eboekhouden-python"
```

### Comparing `eboekhouden_python-0.1.6/PKG-INFO` & `eboekhouden_python-0.1.7/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: eboekhouden-python
-Version: 0.1.6
+Version: 0.1.7
 Summary: This is a simple API client for the E-boekhouden.nl API. It is written in Python and uses the ZEEP library.
 Home-page: https://github.com/dennisbakhuis/eboekhouden-python
 License: MIT
 Keywords: e-boekhouden,eboekhouden,api,zeep,soap,client,python
 Author: Dennis Bakhuis
 Author-email: pypi@bakhuis.nu
 Requires-Python: >=3.9,<4.0
```

