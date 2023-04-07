# Comparing `tmp/sugarcoat-sdk-1.7.0.tar.gz` & `tmp/sugarcoat-sdk-1.8.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "sugarcoat-sdk-1.7.0.tar", last modified: Wed Apr  5 17:40:02 2023, max compression
+gzip compressed data, was "sugarcoat-sdk-1.8.0.tar", last modified: Fri Apr  7 07:16:31 2023, max compression
```

## Comparing `sugarcoat-sdk-1.7.0.tar` & `sugarcoat-sdk-1.8.0.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 jonny      (501) staff       (20)        0 2023-04-05 17:40:02.453035 sugarcoat-sdk-1.7.0/
--rw-r--r--   0 jonny      (501) staff       (20)     4579 2023-04-05 17:40:02.452899 sugarcoat-sdk-1.7.0/PKG-INFO
--rw-r--r--   0 jonny      (501) staff       (20)     4224 2021-07-03 18:30:30.000000 sugarcoat-sdk-1.7.0/README.md
--rw-r--r--   0 jonny      (501) staff       (20)       38 2023-04-05 17:40:02.453075 sugarcoat-sdk-1.7.0/setup.cfg
--rw-r--r--   0 jonny      (501) staff       (20)      539 2023-04-05 17:37:49.000000 sugarcoat-sdk-1.7.0/setup.py
-drwxr-xr-x   0 jonny      (501) staff       (20)        0 2023-04-05 17:40:02.451784 sugarcoat-sdk-1.7.0/sugarcoat/
--rw-r--r--   0 jonny      (501) staff       (20)        0 2020-06-26 15:18:09.000000 sugarcoat-sdk-1.7.0/sugarcoat/__init__.py
--rw-r--r--   0 jonny      (501) staff       (20)       42 2021-07-03 18:30:30.000000 sugarcoat-sdk-1.7.0/sugarcoat/defaults.py
--rw-r--r--   0 jonny      (501) staff       (20)     2277 2021-07-03 18:30:30.000000 sugarcoat-sdk-1.7.0/sugarcoat/endpoints.py
--rw-r--r--   0 jonny      (501) staff       (20)      663 2020-06-26 15:18:09.000000 sugarcoat-sdk-1.7.0/sugarcoat/request.py
--rw-r--r--   0 jonny      (501) staff       (20)     1972 2023-04-05 17:37:24.000000 sugarcoat-sdk-1.7.0/sugarcoat/sugarcoat.py
-drwxr-xr-x   0 jonny      (501) staff       (20)        0 2023-04-05 17:40:02.452310 sugarcoat-sdk-1.7.0/sugarcoat_sdk.egg-info/
--rw-r--r--   0 jonny      (501) staff       (20)     4579 2023-04-05 17:40:02.000000 sugarcoat-sdk-1.7.0/sugarcoat_sdk.egg-info/PKG-INFO
--rw-r--r--   0 jonny      (501) staff       (20)      326 2023-04-05 17:40:02.000000 sugarcoat-sdk-1.7.0/sugarcoat_sdk.egg-info/SOURCES.txt
--rw-r--r--   0 jonny      (501) staff       (20)        1 2023-04-05 17:40:02.000000 sugarcoat-sdk-1.7.0/sugarcoat_sdk.egg-info/dependency_links.txt
--rw-r--r--   0 jonny      (501) staff       (20)       16 2023-04-05 17:40:02.000000 sugarcoat-sdk-1.7.0/sugarcoat_sdk.egg-info/top_level.txt
-drwxr-xr-x   0 jonny      (501) staff       (20)        0 2023-04-05 17:40:02.452728 sugarcoat-sdk-1.7.0/tests/
--rw-r--r--   0 jonny      (501) staff       (20)        0 2020-06-26 15:18:09.000000 sugarcoat-sdk-1.7.0/tests/__init__.py
--rw-r--r--   0 jonny      (501) staff       (20)      146 2020-06-26 15:18:09.000000 sugarcoat-sdk-1.7.0/tests/support.py
--rw-r--r--   0 jonny      (501) staff       (20)     2722 2021-07-03 18:30:30.000000 sugarcoat-sdk-1.7.0/tests/unit.py
+drwxr-xr-x   0 jonny      (501) staff       (20)        0 2023-04-07 07:16:31.827264 sugarcoat-sdk-1.8.0/
+-rw-r--r--   0 jonny      (501) staff       (20)     4579 2023-04-07 07:16:31.827125 sugarcoat-sdk-1.8.0/PKG-INFO
+-rw-r--r--   0 jonny      (501) staff       (20)     4224 2021-07-03 18:30:30.000000 sugarcoat-sdk-1.8.0/README.md
+-rw-r--r--   0 jonny      (501) staff       (20)       38 2023-04-07 07:16:31.827304 sugarcoat-sdk-1.8.0/setup.cfg
+-rw-r--r--   0 jonny      (501) staff       (20)      539 2023-04-07 07:16:19.000000 sugarcoat-sdk-1.8.0/setup.py
+drwxr-xr-x   0 jonny      (501) staff       (20)        0 2023-04-07 07:16:31.826055 sugarcoat-sdk-1.8.0/sugarcoat/
+-rw-r--r--   0 jonny      (501) staff       (20)        0 2020-06-26 15:18:09.000000 sugarcoat-sdk-1.8.0/sugarcoat/__init__.py
+-rw-r--r--   0 jonny      (501) staff       (20)       42 2021-07-03 18:30:30.000000 sugarcoat-sdk-1.8.0/sugarcoat/defaults.py
+-rw-r--r--   0 jonny      (501) staff       (20)     2277 2021-07-03 18:30:30.000000 sugarcoat-sdk-1.8.0/sugarcoat/endpoints.py
+-rw-r--r--   0 jonny      (501) staff       (20)      663 2020-06-26 15:18:09.000000 sugarcoat-sdk-1.8.0/sugarcoat/request.py
+-rw-r--r--   0 jonny      (501) staff       (20)     2013 2023-04-07 07:15:31.000000 sugarcoat-sdk-1.8.0/sugarcoat/sugarcoat.py
+drwxr-xr-x   0 jonny      (501) staff       (20)        0 2023-04-07 07:16:31.826521 sugarcoat-sdk-1.8.0/sugarcoat_sdk.egg-info/
+-rw-r--r--   0 jonny      (501) staff       (20)     4579 2023-04-07 07:16:31.000000 sugarcoat-sdk-1.8.0/sugarcoat_sdk.egg-info/PKG-INFO
+-rw-r--r--   0 jonny      (501) staff       (20)      326 2023-04-07 07:16:31.000000 sugarcoat-sdk-1.8.0/sugarcoat_sdk.egg-info/SOURCES.txt
+-rw-r--r--   0 jonny      (501) staff       (20)        1 2023-04-07 07:16:31.000000 sugarcoat-sdk-1.8.0/sugarcoat_sdk.egg-info/dependency_links.txt
+-rw-r--r--   0 jonny      (501) staff       (20)       16 2023-04-07 07:16:31.000000 sugarcoat-sdk-1.8.0/sugarcoat_sdk.egg-info/top_level.txt
+drwxr-xr-x   0 jonny      (501) staff       (20)        0 2023-04-07 07:16:31.826921 sugarcoat-sdk-1.8.0/tests/
+-rw-r--r--   0 jonny      (501) staff       (20)        0 2020-06-26 15:18:09.000000 sugarcoat-sdk-1.8.0/tests/__init__.py
+-rw-r--r--   0 jonny      (501) staff       (20)      146 2020-06-26 15:18:09.000000 sugarcoat-sdk-1.8.0/tests/support.py
+-rw-r--r--   0 jonny      (501) staff       (20)     2722 2021-07-03 18:30:30.000000 sugarcoat-sdk-1.8.0/tests/unit.py
```

### Comparing `sugarcoat-sdk-1.7.0/PKG-INFO` & `sugarcoat-sdk-1.8.0/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sugarcoat-sdk
-Version: 1.7.0
+Version: 1.8.0
 Summary: An SDK for the Sugarcoat API
 Home-page: https://gitlab.com/sugarcoat/sugarcoat-python-sdk
 Author: Jonathan Butler
 Author-email: jonybutler@gmail.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Description-Content-Type: text/markdown
```

### Comparing `sugarcoat-sdk-1.7.0/README.md` & `sugarcoat-sdk-1.8.0/README.md`

 * *Files identical despite different names*

### Comparing `sugarcoat-sdk-1.7.0/setup.py` & `sugarcoat-sdk-1.8.0/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 import setuptools
 
 with open("README.md", "r") as fh:
 	long_description = fh.read()
 
 setuptools.setup(
 	name="sugarcoat-sdk",
-	version="1.7.0",
+	version="1.8.0",
 	author="Jonathan Butler",
 	author_email="jonybutler@gmail.com",
 	description="An SDK for the Sugarcoat API",
 	long_description=long_description,
 	long_description_content_type="text/markdown",
 	url="https://gitlab.com/sugarcoat/sugarcoat-python-sdk",
 	packages=setuptools.find_packages(),
```

### Comparing `sugarcoat-sdk-1.7.0/sugarcoat/endpoints.py` & `sugarcoat-sdk-1.8.0/sugarcoat/endpoints.py`

 * *Files identical despite different names*

### Comparing `sugarcoat-sdk-1.7.0/sugarcoat/request.py` & `sugarcoat-sdk-1.8.0/sugarcoat/request.py`

 * *Files identical despite different names*

### Comparing `sugarcoat-sdk-1.7.0/sugarcoat/sugarcoat.py` & `sugarcoat-sdk-1.8.0/sugarcoat/sugarcoat.py`

 * *Files 10% similar despite different names*

```diff
@@ -5,14 +5,15 @@
 
 class Sugarcoat:
 	endpoints = {
 		"Store": "stores",
 		"Product": "products",
 		"Basket": "baskets",
 		"Categories": "categories",
+		"CategoryOptions": "category-options",
 		"ProductTypes": "product-types",
 		"User": "users",
 		"Customer": "customers",
 		"Order": "orders",
 		"SearchProducts": "search/products",
 		"DiscountCodes": "discount_codes",
 		"ProductGroups": "product-groups",
```

### Comparing `sugarcoat-sdk-1.7.0/sugarcoat_sdk.egg-info/PKG-INFO` & `sugarcoat-sdk-1.8.0/sugarcoat_sdk.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: sugarcoat-sdk
-Version: 1.7.0
+Version: 1.8.0
 Summary: An SDK for the Sugarcoat API
 Home-page: https://gitlab.com/sugarcoat/sugarcoat-python-sdk
 Author: Jonathan Butler
 Author-email: jonybutler@gmail.com
 Classifier: Programming Language :: Python :: 3
 Classifier: License :: OSI Approved :: MIT License
 Description-Content-Type: text/markdown
```

### Comparing `sugarcoat-sdk-1.7.0/tests/unit.py` & `sugarcoat-sdk-1.8.0/tests/unit.py`

 * *Files identical despite different names*

