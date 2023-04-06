# Comparing `tmp/directory_constants-9.2.0-py3-none-any.whl.zip` & `tmp/directory_constants-9.3.0-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,18 +1,18 @@
-Zip file size: 24050 bytes, number of entries: 16
--rw-r--r--  2.0 unx        0 b- defN 18-Nov-16 15:57 directory_constants/__init__.py
--rw-r--r--  2.0 unx        0 b- defN 18-Nov-16 15:57 directory_constants/constants/__init__.py
--rw-r--r--  2.0 unx    10989 b- defN 18-Nov-16 15:57 directory_constants/constants/choices.py
--rw-r--r--  2.0 unx     3067 b- defN 18-Nov-16 15:57 directory_constants/constants/cms.py
--rw-r--r--  2.0 unx     3876 b- defN 18-Nov-16 15:57 directory_constants/constants/exred_articles.py
--rw-r--r--  2.0 unx     9324 b- defN 18-Nov-16 15:57 directory_constants/constants/exred_sector_names.py
--rw-r--r--  2.0 unx     3784 b- defN 18-Nov-16 15:57 directory_constants/constants/sectors.py
--rw-r--r--  2.0 unx     1775 b- defN 18-Nov-16 15:57 directory_constants/constants/urls.py
--rw-r--r--  2.0 unx    46051 b- defN 18-Nov-16 15:57 directory_constants/fixtures/country.json
--rw-r--r--  2.0 unx        0 b- defN 18-Nov-16 15:57 directory_constants/templatetags/__init__.py
--rw-r--r--  2.0 unx     1400 b- defN 18-Nov-16 15:57 directory_constants/templatetags/constants_tags.py
--rw-r--r--  2.0 unx     1091 b- defN 18-Nov-16 15:57 directory_constants-9.2.0.dist-info/LICENSE
--rw-r--r--  2.0 unx     2483 b- defN 18-Nov-16 15:57 directory_constants-9.2.0.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 18-Nov-16 15:57 directory_constants-9.2.0.dist-info/WHEEL
--rw-r--r--  2.0 unx       20 b- defN 18-Nov-16 15:57 directory_constants-9.2.0.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1524 b- defN 18-Nov-16 15:57 directory_constants-9.2.0.dist-info/RECORD
-16 files, 85476 bytes uncompressed, 21458 bytes compressed:  74.9%
+Zip file size: 24060 bytes, number of entries: 16
+-rw-r--r--  2.0 unx        0 b- defN 18-Nov-19 12:16 directory_constants/__init__.py
+-rw-r--r--  2.0 unx        0 b- defN 18-Nov-19 12:16 directory_constants/constants/__init__.py
+-rw-r--r--  2.0 unx    10989 b- defN 18-Nov-19 12:16 directory_constants/constants/choices.py
+-rw-r--r--  2.0 unx     3174 b- defN 18-Nov-19 12:16 directory_constants/constants/cms.py
+-rw-r--r--  2.0 unx     3876 b- defN 18-Nov-19 12:16 directory_constants/constants/exred_articles.py
+-rw-r--r--  2.0 unx     9324 b- defN 18-Nov-19 12:16 directory_constants/constants/exred_sector_names.py
+-rw-r--r--  2.0 unx     3784 b- defN 18-Nov-19 12:16 directory_constants/constants/sectors.py
+-rw-r--r--  2.0 unx     1775 b- defN 18-Nov-19 12:16 directory_constants/constants/urls.py
+-rw-r--r--  2.0 unx    46051 b- defN 18-Nov-19 12:16 directory_constants/fixtures/country.json
+-rw-r--r--  2.0 unx        0 b- defN 18-Nov-19 12:16 directory_constants/templatetags/__init__.py
+-rw-r--r--  2.0 unx     1400 b- defN 18-Nov-19 12:16 directory_constants/templatetags/constants_tags.py
+-rw-r--r--  2.0 unx     1091 b- defN 18-Nov-19 12:17 directory_constants-9.3.0.dist-info/LICENSE
+-rw-r--r--  2.0 unx     2491 b- defN 18-Nov-19 12:17 directory_constants-9.3.0.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 18-Nov-19 12:17 directory_constants-9.3.0.dist-info/WHEEL
+-rw-r--r--  2.0 unx       20 b- defN 18-Nov-19 12:17 directory_constants-9.3.0.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1524 b- defN 18-Nov-19 12:17 directory_constants-9.3.0.dist-info/RECORD
+16 files, 85591 bytes uncompressed, 21468 bytes compressed:  74.9%
```

## zipnote {}

```diff
@@ -27,23 +27,23 @@
 
 Filename: directory_constants/templatetags/__init__.py
 Comment: 
 
 Filename: directory_constants/templatetags/constants_tags.py
 Comment: 
 
-Filename: directory_constants-9.2.0.dist-info/LICENSE
+Filename: directory_constants-9.3.0.dist-info/LICENSE
 Comment: 
 
-Filename: directory_constants-9.2.0.dist-info/METADATA
+Filename: directory_constants-9.3.0.dist-info/METADATA
 Comment: 
 
-Filename: directory_constants-9.2.0.dist-info/WHEEL
+Filename: directory_constants-9.3.0.dist-info/WHEEL
 Comment: 
 
-Filename: directory_constants-9.2.0.dist-info/top_level.txt
+Filename: directory_constants-9.3.0.dist-info/top_level.txt
 Comment: 
 
-Filename: directory_constants-9.2.0.dist-info/RECORD
+Filename: directory_constants-9.3.0.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## directory_constants/constants/cms.py

```diff
@@ -58,14 +58,17 @@
 )
 EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_FEEDBACK_SLUG = (
     'contact-feedback-success-form'
 )
 EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_FIND_COMPANIES_SLUG = (
     'contact-find-companies-success-form'
 )
+EXPORT_READINESS_CONTACT_US_FORM_SUCCESS_INTERNATIONAL_SLUG = (
+    'contact-international-success-form'
+)
 # Find A Supplier
 FIND_A_SUPPLIER_INDUSTRY_LANDING_SLUG = 'industries-landing-page'
 FIND_A_SUPPLIER_LANDING_SLUG = 'landing-page'
 FIND_A_SUPPLIER_INDUSTRY_CONTACT_SLUG = 'industry-contact'
 
 
 # CMS page types
```

## Comparing `directory_constants-9.2.0.dist-info/LICENSE` & `directory_constants-9.3.0.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `directory_constants-9.2.0.dist-info/METADATA` & `directory_constants-9.3.0.dist-info/METADATA`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: directory-constants
-Version: 9.2.0
+Version: 9.3.0
 Summary: Constant values shared between Directory apps.
 Home-page: https://github.com/uktrade/directory-constants
 Author: Department for International Trade
 License: MIT
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: Environment :: Web Environment
@@ -15,22 +15,22 @@
 Classifier: Natural Language :: English
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
 Description-Content-Type: text/markdown
 Requires-Dist: django (<2.0a1,>=1.9)
 Provides-Extra: test
-Requires-Dist: pytest (==3.0.2); extra == 'test'
-Requires-Dist: pytest-cov (==2.3.1); extra == 'test'
-Requires-Dist: pytest-django (==3.0.0); extra == 'test'
-Requires-Dist: flake8 (==3.0.4); extra == 'test'
-Requires-Dist: twine (<2.0.0,>=1.11.0); extra == 'test'
-Requires-Dist: wheel (<1.0.0,>=0.31.0); extra == 'test'
-Requires-Dist: freezegun (==0.3.8); extra == 'test'
-Requires-Dist: setuptools (<39.0.0,>=38.6.0); extra == 'test'
+Requires-Dist: pytest (==3.0.2) ; extra == 'test'
+Requires-Dist: pytest-cov (==2.3.1) ; extra == 'test'
+Requires-Dist: pytest-django (==3.0.0) ; extra == 'test'
+Requires-Dist: flake8 (==3.0.4) ; extra == 'test'
+Requires-Dist: twine (<2.0.0,>=1.11.0) ; extra == 'test'
+Requires-Dist: wheel (<1.0.0,>=0.31.0) ; extra == 'test'
+Requires-Dist: freezegun (==0.3.8) ; extra == 'test'
+Requires-Dist: setuptools (<39.0.0,>=38.6.0) ; extra == 'test'
 
 # directory-constants
 
 [![circle-ci-image]][circle-ci]
 [![codecov-image]][codecov]
 [![pypi-image]][pypi]
 ---
```

## Comparing `directory_constants-9.2.0.dist-info/RECORD` & `directory_constants-9.3.0.dist-info/RECORD`

 * *Files 13% similar despite different names*

```diff
@@ -1,16 +1,16 @@
 directory_constants/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 directory_constants/constants/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 directory_constants/constants/choices.py,sha256=OYq78Z87_ckYbWSsDozrvlKXNIolW6kjf1JPbDxl5kM,10989
-directory_constants/constants/cms.py,sha256=sdSLWcea8ZLc7s_HEj-5ugRzejyoU3XMuBqlVkAOW4Y,3067
+directory_constants/constants/cms.py,sha256=1cEghyWTUvDMadKcrchN8G3r6cPJDK1KSNN6FNMhLMM,3174
 directory_constants/constants/exred_articles.py,sha256=fXFTMSG6V4oo46cQUTClFMiJAH3WjuKfp6DyY5bCpyI,3876
 directory_constants/constants/exred_sector_names.py,sha256=r0DJ9itsCgNxZM1A6tJX4mfGhMM1A-Oa9JTR9w3-SaM,9324
 directory_constants/constants/sectors.py,sha256=6DyHjI0vMlBMknw94Ti_7LbSP3jv02m-P9xYxZke5zA,3784
 directory_constants/constants/urls.py,sha256=_yH4Yvd5wkgGBMepYbYNuqViCWuAYxmc2yxz6ZDHBec,1775
 directory_constants/fixtures/country.json,sha256=mLX-DJvJkm7NMy-lf6zCbEn_scdQnBL54WP0l4ggKLc,46051
 directory_constants/templatetags/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
 directory_constants/templatetags/constants_tags.py,sha256=ecLyKdxuZxou5VVsxbNlR7Vs1RWKqrHiewd-7uwa1oM,1400
-directory_constants-9.2.0.dist-info/LICENSE,sha256=y-ArErAQz98OorLek2xntwEp9bo3ZcqfQMtAIcjBdvQ,1091
-directory_constants-9.2.0.dist-info/METADATA,sha256=e5x_bs2ck8T3j4_Y3qF_MO3xYlAywJGhFE0PmDJjs4A,2483
-directory_constants-9.2.0.dist-info/WHEEL,sha256=MYFsq5fFBwF_oyJgrOoFmYYB1K6Sw7MxY-0897ZLbdM,92
-directory_constants-9.2.0.dist-info/top_level.txt,sha256=jbajnKJfYlDfIfI9EBcNzVQHrrsxDFyzWOmdxhsSl9U,20
-directory_constants-9.2.0.dist-info/RECORD,,
+directory_constants-9.3.0.dist-info/LICENSE,sha256=y-ArErAQz98OorLek2xntwEp9bo3ZcqfQMtAIcjBdvQ,1091
+directory_constants-9.3.0.dist-info/METADATA,sha256=vkIH8TrUzMIEvwejCf24UcIsHkM33Qp5QXdLjyD_vq0,2491
+directory_constants-9.3.0.dist-info/WHEEL,sha256=_NOXIqFgOaYmlm9RJLPQZ13BJuEIrp5jx5ptRD5uh3Y,92
+directory_constants-9.3.0.dist-info/top_level.txt,sha256=jbajnKJfYlDfIfI9EBcNzVQHrrsxDFyzWOmdxhsSl9U,20
+directory_constants-9.3.0.dist-info/RECORD,,
```

