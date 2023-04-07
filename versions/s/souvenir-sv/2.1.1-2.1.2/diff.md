# Comparing `tmp/souvenir-sv-2.1.1.tar.gz` & `tmp/souvenir-sv-2.1.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "souvenir-sv-2.1.1.tar", last modified: Thu Apr  6 00:48:44 2023, max compression
+gzip compressed data, was "souvenir-sv-2.1.2.tar", last modified: Fri Apr  7 04:37:54 2023, max compression
```

## Comparing `souvenir-sv-2.1.1.tar` & `souvenir-sv-2.1.2.tar`

### file list

```diff
@@ -1,13 +1,13 @@
--rw-r--r--   0        0        0      153 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/.deepsource.toml
--rw-r--r--   0        0        0     1228 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/.github/workflows/publish.yml
--rw-r--r--   0        0        0     1831 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/.gitignore
--rw-r--r--   0        0        0    35149 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/LICENSE
--rw-r--r--   0        0        0     3159 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/README.md
--rw-r--r--   0        0        0      705 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/pyproject.toml
--rw-r--r--   0        0        0     2490 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/requirements.txt
--rw-r--r--   0        0        0       84 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/souvenir/__init__.py
--rw-r--r--   0        0        0     2685 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/souvenir/image.py
--rw-r--r--   0        0        0     2710 2023-04-06 00:48:41.283159 souvenir-sv-2.1.1/souvenir/zipcode.py
--rw-r--r--   0        0        0        0 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/tests/__init__.py
--rw-r--r--   0        0        0     2085 2023-04-06 00:48:36.338947 souvenir-sv-2.1.1/tests/souvenir_modules.py
--rw-r--r--   0        0        0     3668 1970-01-01 00:00:00.000000 souvenir-sv-2.1.1/PKG-INFO
+-rw-r--r--   0        0        0      153 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/.deepsource.toml
+-rw-r--r--   0        0        0     1228 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/.github/workflows/publish.yml
+-rw-r--r--   0        0        0     1831 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/.gitignore
+-rw-r--r--   0        0        0    35149 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/LICENSE
+-rw-r--r--   0        0        0     3159 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/README.md
+-rw-r--r--   0        0        0      730 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/pyproject.toml
+-rw-r--r--   0        0        0     2490 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/requirements.txt
+-rw-r--r--   0        0        0       84 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/souvenir/__init__.py
+-rw-r--r--   0        0        0     2685 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/souvenir/image.py
+-rw-r--r--   0        0        0     2710 2023-04-07 04:37:51.734784 souvenir-sv-2.1.2/souvenir/zipcode.py
+-rw-r--r--   0        0        0        0 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/tests/__init__.py
+-rw-r--r--   0        0        0     2085 2023-04-07 04:37:47.502626 souvenir-sv-2.1.2/tests/souvenir_modules.py
+-rw-r--r--   0        0        0     3705 1970-01-01 00:00:00.000000 souvenir-sv-2.1.2/PKG-INFO
```

### Comparing `souvenir-sv-2.1.1/.github/workflows/publish.yml` & `souvenir-sv-2.1.2/.github/workflows/publish.yml`

 * *Files identical despite different names*

### Comparing `souvenir-sv-2.1.1/.gitignore` & `souvenir-sv-2.1.2/.gitignore`

 * *Files identical despite different names*

### Comparing `souvenir-sv-2.1.1/LICENSE` & `souvenir-sv-2.1.2/LICENSE`

 * *Files identical despite different names*

### Comparing `souvenir-sv-2.1.1/README.md` & `souvenir-sv-2.1.2/README.md`

 * *Files identical despite different names*

### Comparing `souvenir-sv-2.1.1/pyproject.toml` & `souvenir-sv-2.1.2/pyproject.toml`

 * *Files 3% similar despite different names*

```diff
@@ -11,15 +11,16 @@
 license = {file = "LICENSE"}
 classifiers = ["License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"]
 # execution dependencies
 dependencies = [
 "requests == 2.28.1",
 "beautifulsoup4 == 4.11.1",
 "bing-image-urls==0.1.5",
-"google-search-results==2.4.1"
+"google-search-results==2.4.1",
+"requests-cache==1.0.1"
 ]
 dynamic = ["version", "description"]
 
 # defines module import
 [tool.flit.module]
 name = "souvenir"
```

### Comparing `souvenir-sv-2.1.1/requirements.txt` & `souvenir-sv-2.1.2/requirements.txt`

 * *Files identical despite different names*

### Comparing `souvenir-sv-2.1.1/souvenir/image.py` & `souvenir-sv-2.1.2/souvenir/image.py`

 * *Files identical despite different names*

### Comparing `souvenir-sv-2.1.1/souvenir/zipcode.py` & `souvenir-sv-2.1.2/souvenir/zipcode.py`

 * *Files identical despite different names*

### Comparing `souvenir-sv-2.1.1/tests/souvenir_modules.py` & `souvenir-sv-2.1.2/tests/souvenir_modules.py`

 * *Files identical despite different names*

### Comparing `souvenir-sv-2.1.1/PKG-INFO` & `souvenir-sv-2.1.2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,18 +1,19 @@
 Metadata-Version: 2.1
 Name: souvenir-sv
-Version: 2.1.1
+Version: 2.1.2
 Summary: A package to get zipcodes from El Salvador departments
 Author-email: standoge <stanlydoge@gmail.com>
 Description-Content-Type: text/markdown
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Requires-Dist: requests == 2.28.1
 Requires-Dist: beautifulsoup4 == 4.11.1
 Requires-Dist: bing-image-urls==0.1.5
 Requires-Dist: google-search-results==2.4.1
+Requires-Dist: requests-cache==1.0.1
 Project-URL: Home, https://github.com/standoge/souvenir-sv
 
 [![publish](https://github.com/standoge/souvenir-sv/actions/workflows/publish.yml/badge.svg)](https://github.com/standoge/souvenir-sv/actions/workflows/publish.yml)
 
 # El Salvador souvenir
 
 This Python package scrapes [this web](https://www.listasal.info/articulos/codigo-postal-el-salvador.shtml) to get zip codes by municipality. It uses `Requests` with `BeautifulSoup` to extract that information, which is then returned as a dictionary or JSON.
```

