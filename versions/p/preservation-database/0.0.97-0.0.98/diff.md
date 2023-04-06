# Comparing `tmp/preservation-database-0.0.97.tar.gz` & `tmp/preservation-database-0.0.98.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "preservation-database-0.0.97.tar", last modified: Thu Apr  6 16:05:03 2023, max compression
+gzip compressed data, was "preservation-database-0.0.98.tar", last modified: Thu Apr  6 16:11:43 2023, max compression
```

## Comparing `preservation-database-0.0.97.tar` & `preservation-database-0.0.98.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:05:03.883018 preservation-database-0.0.97/
--rw-rw-r--   0 martin    (1000) martin    (1000)      129 2023-02-06 17:29:02.000000 preservation-database-0.0.97/MANIFEST.in
--rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 16:05:03.883018 preservation-database-0.0.97/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)     4701 2023-04-06 16:04:59.000000 preservation-database-0.0.97/README.md
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:05:03.883018 preservation-database-0.0.97/preservation_database.egg-info/
--rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 16:05:03.000000 preservation-database-0.0.97/preservation_database.egg-info/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)      691 2023-04-06 16:05:03.000000 preservation-database-0.0.97/preservation_database.egg-info/SOURCES.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-04-06 16:05:03.000000 preservation-database-0.0.97/preservation_database.egg-info/dependency_links.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)      208 2023-04-06 16:05:03.000000 preservation-database-0.0.97/preservation_database.egg-info/requires.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)       21 2023-04-06 16:05:03.000000 preservation-database-0.0.97/preservation_database.egg-info/top_level.txt
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:05:03.883018 preservation-database-0.0.97/preservationdatabase/
--rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:14:23.000000 preservation-database-0.0.97/preservationdatabase/__init__.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    15336 2023-04-06 15:46:52.000000 preservation-database-0.0.97/preservationdatabase/cli.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      660 2023-03-01 11:09:55.000000 preservation-database-0.0.97/preservationdatabase/constants.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     1597 2023-03-05 12:44:30.000000 preservation-database-0.0.97/preservationdatabase/environment.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     3450 2023-02-19 18:38:37.000000 preservation-database-0.0.97/preservationdatabase/example_settings.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    34494 2023-04-06 16:04:56.000000 preservation-database-0.0.97/preservationdatabase/exporter.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    42928 2023-04-06 14:20:58.000000 preservation-database-0.0.97/preservationdatabase/models.py
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:05:03.883018 preservation-database-0.0.97/preservationdatabase/test_data/
--rw-rw-r--   0 martin    (1000) martin    (1000)      888 2023-02-06 10:17:59.000000 preservation-database-0.0.97/preservationdatabase/test_data/tests.jsonl
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:05:03.883018 preservation-database-0.0.97/preservationdatabase/tests/
--rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:20:11.000000 preservation-database-0.0.97/preservationdatabase/tests/__init__.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     2072 2023-02-06 10:15:46.000000 preservation-database-0.0.97/preservationdatabase/tests/test_archives.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      767 2023-02-19 18:38:37.000000 preservation-database-0.0.97/preservationdatabase/urls.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    20636 2023-04-06 13:59:40.000000 preservation-database-0.0.97/preservationdatabase/utils.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     1238 2023-04-06 16:04:56.000000 preservation-database-0.0.97/pyproject.toml
--rw-rw-r--   0 martin    (1000) martin    (1000)     1143 2023-04-06 16:05:03.883018 preservation-database-0.0.97/setup.cfg
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/
+-rw-rw-r--   0 martin    (1000) martin    (1000)      129 2023-02-06 17:29:02.000000 preservation-database-0.0.98/MANIFEST.in
+-rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 16:11:43.704483 preservation-database-0.0.98/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)     4701 2023-04-06 16:11:39.000000 preservation-database-0.0.98/README.md
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/preservation_database.egg-info/
+-rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)      691 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/SOURCES.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/dependency_links.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)      208 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/requires.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)       21 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/top_level.txt
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/preservationdatabase/
+-rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:14:23.000000 preservation-database-0.0.98/preservationdatabase/__init__.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    15336 2023-04-06 15:46:52.000000 preservation-database-0.0.98/preservationdatabase/cli.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)      660 2023-03-01 11:09:55.000000 preservation-database-0.0.98/preservationdatabase/constants.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1597 2023-03-05 12:44:30.000000 preservation-database-0.0.98/preservationdatabase/environment.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     3450 2023-02-19 18:38:37.000000 preservation-database-0.0.98/preservationdatabase/example_settings.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    34670 2023-04-06 16:11:32.000000 preservation-database-0.0.98/preservationdatabase/exporter.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    42928 2023-04-06 14:20:58.000000 preservation-database-0.0.98/preservationdatabase/models.py
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/preservationdatabase/test_data/
+-rw-rw-r--   0 martin    (1000) martin    (1000)      888 2023-02-06 10:17:59.000000 preservation-database-0.0.98/preservationdatabase/test_data/tests.jsonl
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/preservationdatabase/tests/
+-rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:20:11.000000 preservation-database-0.0.98/preservationdatabase/tests/__init__.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     2072 2023-02-06 10:15:46.000000 preservation-database-0.0.98/preservationdatabase/tests/test_archives.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)      767 2023-02-19 18:38:37.000000 preservation-database-0.0.98/preservationdatabase/urls.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    20636 2023-04-06 13:59:40.000000 preservation-database-0.0.98/preservationdatabase/utils.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1238 2023-04-06 16:11:37.000000 preservation-database-0.0.98/pyproject.toml
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1143 2023-04-06 16:11:43.704483 preservation-database-0.0.98/setup.cfg
```

### Comparing `preservation-database-0.0.97/PKG-INFO` & `preservation-database-0.0.98/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: preservation-database
-Version: 0.0.97
+Version: 0.0.98
 Summary: A database builder for digital preservation information.
 Home-page: https://gitlab.com/crossref/labs/preservationDatabase
 Author: Martin Paul Eve
 Author-email: meve@crossref.org
 Maintainer-email: Martin Paul Eve <meve@crossref.org>
 Project-URL: homepage, https://labs.crossref.org
 Project-URL: documentation, https://labs.crossref.org
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: preservation-database Version: 0.0.97 Summary: A
+Metadata-Version: 2.1 Name: preservation-database Version: 0.0.98 Summary: A
 database builder for digital preservation information. Home-page: https://
 gitlab.com/crossref/labs/preservationDatabase Author: Martin Paul Eve Author-
 email: meve@crossref.org Maintainer-email: Martin Paul Eve
 crossref.org> Project-URL: homepage, https://labs.crossref.org Project-URL:
 documentation, https://labs.crossref.org Project-URL: repository, https://
 gitlab.com/crossref/labs/preservationDatabase Project-URL: changelog, https://
 gitlab.com/crossref/labs/preservation-data/-/blob/main/CHANGELOG.md Keywords:
```

### Comparing `preservation-database-0.0.97/README.md` & `preservation-database-0.0.98/README.md`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservation_database.egg-info/PKG-INFO` & `preservation-database-0.0.98/preservation_database.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: preservation-database
-Version: 0.0.97
+Version: 0.0.98
 Summary: A database builder for digital preservation information.
 Home-page: https://gitlab.com/crossref/labs/preservationDatabase
 Author: Martin Paul Eve
 Author-email: meve@crossref.org
 Maintainer-email: Martin Paul Eve <meve@crossref.org>
 Project-URL: homepage, https://labs.crossref.org
 Project-URL: documentation, https://labs.crossref.org
```

#### html2text {}

```diff
@@ -1,8 +1,8 @@
-Metadata-Version: 2.1 Name: preservation-database Version: 0.0.97 Summary: A
+Metadata-Version: 2.1 Name: preservation-database Version: 0.0.98 Summary: A
 database builder for digital preservation information. Home-page: https://
 gitlab.com/crossref/labs/preservationDatabase Author: Martin Paul Eve Author-
 email: meve@crossref.org Maintainer-email: Martin Paul Eve
 crossref.org> Project-URL: homepage, https://labs.crossref.org Project-URL:
 documentation, https://labs.crossref.org Project-URL: repository, https://
 gitlab.com/crossref/labs/preservationDatabase Project-URL: changelog, https://
 gitlab.com/crossref/labs/preservation-data/-/blob/main/CHANGELOG.md Keywords:
```

### Comparing `preservation-database-0.0.97/preservation_database.egg-info/SOURCES.txt` & `preservation-database-0.0.98/preservation_database.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservationdatabase/cli.py` & `preservation-database-0.0.98/preservationdatabase/cli.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservationdatabase/constants.py` & `preservation-database-0.0.98/preservationdatabase/constants.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservationdatabase/environment.py` & `preservation-database-0.0.98/preservationdatabase/environment.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservationdatabase/example_settings.py` & `preservation-database-0.0.98/preservationdatabase/example_settings.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservationdatabase/exporter.py` & `preservation-database-0.0.98/preservationdatabase/exporter.py`

 * *Files 1% similar despite different names*

```diff
@@ -133,20 +133,27 @@
     )
     issn = result["ISSN"] if "ISSN" in result else None
     volume = result["volume"] if "volume" in result else None
 
     # not in sampling framework (yet)
     no = None
 
+    year = None
+    # "published": {"date-parts": [[2005, 12, 30]]}}}
+
+    if "published" in result:
+        year = result["published"]["date-parts"][0][0]
+
     return show_preservation(
         container_title=container_title,
         issn=issn,
         volume=volume,
         no=no,
         doi=result,
+        year=year,
     )
 
 
 def score(
     one_archive, two_archives, three_archives, sample_count, verbose=False
 ):
     score = "Unclassified"
```

### Comparing `preservation-database-0.0.97/preservationdatabase/models.py` & `preservation-database-0.0.98/preservationdatabase/models.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservationdatabase/test_data/tests.jsonl` & `preservation-database-0.0.98/preservationdatabase/test_data/tests.jsonl`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservationdatabase/tests/test_archives.py` & `preservation-database-0.0.98/preservationdatabase/tests/test_archives.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservationdatabase/urls.py` & `preservation-database-0.0.98/preservationdatabase/urls.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/preservationdatabase/utils.py` & `preservation-database-0.0.98/preservationdatabase/utils.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.97/pyproject.toml` & `preservation-database-0.0.98/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "preservation-database"
-version = "0.0.97"
+version = "0.0.98"
 description = "A database builder for digital preservation information."
 readme = "README.md"
 requires-python = ">=3.8"
 license = {file = "LICENSE.md"}
 keywords = ["digital preservation", "academic"]
 authors = [
   {email = "meve@crossref.org"},
```

### Comparing `preservation-database-0.0.97/setup.cfg` & `preservation-database-0.0.98/setup.cfg`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = preservation-database
-version = 0.0.97
+version = 0.0.98
 description = A database builder for digital preservation information.
 url = https://gitlab.com/crossref/labs/preservationDatabase
 author = Martin Paul Eve
 author_email = martin@eve.gd
 license = MIT
 classifiers = 
 	Environment :: Web Environment
```

