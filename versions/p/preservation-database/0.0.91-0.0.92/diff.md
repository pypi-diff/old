# Comparing `tmp/preservation-database-0.0.91.tar.gz` & `tmp/preservation-database-0.0.92.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "preservation-database-0.0.91.tar", last modified: Thu Apr  6 15:40:50 2023, max compression
+gzip compressed data, was "preservation-database-0.0.92.tar", last modified: Thu Apr  6 15:47:24 2023, max compression
```

## Comparing `preservation-database-0.0.91.tar` & `preservation-database-0.0.92.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:40:50.228283 preservation-database-0.0.91/
--rw-rw-r--   0 martin    (1000) martin    (1000)      129 2023-02-06 17:29:02.000000 preservation-database-0.0.91/MANIFEST.in
--rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 15:40:50.228283 preservation-database-0.0.91/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)     4701 2023-04-06 15:40:45.000000 preservation-database-0.0.91/README.md
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:40:50.228283 preservation-database-0.0.91/preservation_database.egg-info/
--rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 15:40:50.000000 preservation-database-0.0.91/preservation_database.egg-info/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)      691 2023-04-06 15:40:50.000000 preservation-database-0.0.91/preservation_database.egg-info/SOURCES.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-04-06 15:40:50.000000 preservation-database-0.0.91/preservation_database.egg-info/dependency_links.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)      208 2023-04-06 15:40:50.000000 preservation-database-0.0.91/preservation_database.egg-info/requires.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)       21 2023-04-06 15:40:50.000000 preservation-database-0.0.91/preservation_database.egg-info/top_level.txt
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:40:50.228283 preservation-database-0.0.91/preservationdatabase/
--rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:14:23.000000 preservation-database-0.0.91/preservationdatabase/__init__.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    15336 2023-04-06 14:03:38.000000 preservation-database-0.0.91/preservationdatabase/cli.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      660 2023-03-01 11:09:55.000000 preservation-database-0.0.91/preservationdatabase/constants.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     1597 2023-03-05 12:44:30.000000 preservation-database-0.0.91/preservationdatabase/environment.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     3450 2023-02-19 18:38:37.000000 preservation-database-0.0.91/preservationdatabase/example_settings.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    34121 2023-04-06 15:40:37.000000 preservation-database-0.0.91/preservationdatabase/exporter.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    42928 2023-04-06 14:20:58.000000 preservation-database-0.0.91/preservationdatabase/models.py
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:40:50.228283 preservation-database-0.0.91/preservationdatabase/test_data/
--rw-rw-r--   0 martin    (1000) martin    (1000)      888 2023-02-06 10:17:59.000000 preservation-database-0.0.91/preservationdatabase/test_data/tests.jsonl
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:40:50.228283 preservation-database-0.0.91/preservationdatabase/tests/
--rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:20:11.000000 preservation-database-0.0.91/preservationdatabase/tests/__init__.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     2072 2023-02-06 10:15:46.000000 preservation-database-0.0.91/preservationdatabase/tests/test_archives.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      767 2023-02-19 18:38:37.000000 preservation-database-0.0.91/preservationdatabase/urls.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    20636 2023-04-06 13:59:40.000000 preservation-database-0.0.91/preservationdatabase/utils.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     1238 2023-04-06 15:40:43.000000 preservation-database-0.0.91/pyproject.toml
--rw-rw-r--   0 martin    (1000) martin    (1000)     1143 2023-04-06 15:40:50.232283 preservation-database-0.0.91/setup.cfg
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:47:24.881266 preservation-database-0.0.92/
+-rw-rw-r--   0 martin    (1000) martin    (1000)      129 2023-02-06 17:29:02.000000 preservation-database-0.0.92/MANIFEST.in
+-rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 15:47:24.881266 preservation-database-0.0.92/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)     4701 2023-04-06 15:47:20.000000 preservation-database-0.0.92/README.md
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:47:24.881266 preservation-database-0.0.92/preservation_database.egg-info/
+-rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 15:47:24.000000 preservation-database-0.0.92/preservation_database.egg-info/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)      691 2023-04-06 15:47:24.000000 preservation-database-0.0.92/preservation_database.egg-info/SOURCES.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-04-06 15:47:24.000000 preservation-database-0.0.92/preservation_database.egg-info/dependency_links.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)      208 2023-04-06 15:47:24.000000 preservation-database-0.0.92/preservation_database.egg-info/requires.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)       21 2023-04-06 15:47:24.000000 preservation-database-0.0.92/preservation_database.egg-info/top_level.txt
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:47:24.881266 preservation-database-0.0.92/preservationdatabase/
+-rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:14:23.000000 preservation-database-0.0.92/preservationdatabase/__init__.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    15336 2023-04-06 15:46:52.000000 preservation-database-0.0.92/preservationdatabase/cli.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)      660 2023-03-01 11:09:55.000000 preservation-database-0.0.92/preservationdatabase/constants.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1597 2023-03-05 12:44:30.000000 preservation-database-0.0.92/preservationdatabase/environment.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     3450 2023-02-19 18:38:37.000000 preservation-database-0.0.92/preservationdatabase/example_settings.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    34125 2023-04-06 15:45:45.000000 preservation-database-0.0.92/preservationdatabase/exporter.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    42928 2023-04-06 14:20:58.000000 preservation-database-0.0.92/preservationdatabase/models.py
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:47:24.881266 preservation-database-0.0.92/preservationdatabase/test_data/
+-rw-rw-r--   0 martin    (1000) martin    (1000)      888 2023-02-06 10:17:59.000000 preservation-database-0.0.92/preservationdatabase/test_data/tests.jsonl
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 15:47:24.881266 preservation-database-0.0.92/preservationdatabase/tests/
+-rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:20:11.000000 preservation-database-0.0.92/preservationdatabase/tests/__init__.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     2072 2023-02-06 10:15:46.000000 preservation-database-0.0.92/preservationdatabase/tests/test_archives.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)      767 2023-02-19 18:38:37.000000 preservation-database-0.0.92/preservationdatabase/urls.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    20636 2023-04-06 13:59:40.000000 preservation-database-0.0.92/preservationdatabase/utils.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1238 2023-04-06 15:45:45.000000 preservation-database-0.0.92/pyproject.toml
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1143 2023-04-06 15:47:24.881266 preservation-database-0.0.92/setup.cfg
```

### Comparing `preservation-database-0.0.91/PKG-INFO` & `preservation-database-0.0.92/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: preservation-database
-Version: 0.0.91
+Version: 0.0.92
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
-Metadata-Version: 2.1 Name: preservation-database Version: 0.0.91 Summary: A
+Metadata-Version: 2.1 Name: preservation-database Version: 0.0.92 Summary: A
 database builder for digital preservation information. Home-page: https://
 gitlab.com/crossref/labs/preservationDatabase Author: Martin Paul Eve Author-
 email: meve@crossref.org Maintainer-email: Martin Paul Eve
 crossref.org> Project-URL: homepage, https://labs.crossref.org Project-URL:
 documentation, https://labs.crossref.org Project-URL: repository, https://
 gitlab.com/crossref/labs/preservationDatabase Project-URL: changelog, https://
 gitlab.com/crossref/labs/preservation-data/-/blob/main/CHANGELOG.md Keywords:
```

### Comparing `preservation-database-0.0.91/README.md` & `preservation-database-0.0.92/README.md`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/preservation_database.egg-info/PKG-INFO` & `preservation-database-0.0.92/preservation_database.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: preservation-database
-Version: 0.0.91
+Version: 0.0.92
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
-Metadata-Version: 2.1 Name: preservation-database Version: 0.0.91 Summary: A
+Metadata-Version: 2.1 Name: preservation-database Version: 0.0.92 Summary: A
 database builder for digital preservation information. Home-page: https://
 gitlab.com/crossref/labs/preservationDatabase Author: Martin Paul Eve Author-
 email: meve@crossref.org Maintainer-email: Martin Paul Eve
 crossref.org> Project-URL: homepage, https://labs.crossref.org Project-URL:
 documentation, https://labs.crossref.org Project-URL: repository, https://
 gitlab.com/crossref/labs/preservationDatabase Project-URL: changelog, https://
 gitlab.com/crossref/labs/preservation-data/-/blob/main/CHANGELOG.md Keywords:
```

### Comparing `preservation-database-0.0.91/preservation_database.egg-info/SOURCES.txt` & `preservation-database-0.0.92/preservation_database.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/preservationdatabase/cli.py` & `preservation-database-0.0.92/preservationdatabase/cli.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -289,25 +289,25 @@
 @click.argument("member_id")
 @transaction.atomic()
 def member_report(member_id):
     """Process the member"""
 
     import exporter
 
-    exporter.member_reports()
+    exporter.member_report(member_id)
 
 
 @click.command()
 @transaction.atomic()
 def member_reports():
     """Process all members"""
 
     import exporter
 
-    exporter.member_report(member_id)
+    exporter.member_reports()
 
 
 @click.command()
 @click.argument("member_id")
 @transaction.atomic()
 def process_member(member_id):
     """Process a member"""
```

### Comparing `preservation-database-0.0.91/preservationdatabase/constants.py` & `preservation-database-0.0.92/preservationdatabase/constants.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/preservationdatabase/environment.py` & `preservation-database-0.0.92/preservationdatabase/environment.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/preservationdatabase/example_settings.py` & `preservation-database-0.0.92/preservationdatabase/example_settings.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/preservationdatabase/exporter.py` & `preservation-database-0.0.92/preservationdatabase/exporter.py`

 * *Files 0% similar despite different names*

```diff
@@ -605,15 +605,15 @@
 
     import botocore
 
     for sample in samples:
         sample = json.loads(sample)["data-point"]
 
         if "type" in sample and sample["type"] == "journal-article":
-            print(f"Appending {sample['DOI']}")
+            # print(f"Appending {sample['DOI']}")
 
             md5_doi = hashlib.md5(sample["DOI"].lower().encode()).hexdigest()
 
             try:
                 annotation = get_annotation(
                     s3client=s3client,
                     member_id=member_id,
@@ -633,15 +633,15 @@
                 if not preserved:
                     unpreserved_samples.append(annotation)
 
                 overall_samples.append(annotation)
 
             except Exception as e:
                 print(e)
-                print(f"This DOI was excluded: {sample['DOI']}")
+                # print(f"This DOI was excluded: {sample['DOI']}")
 
     key = f"{REPORT_PATH}/members/{member_id}/preservation-report.json"
     unpreserved_key = f"{REPORT_PATH}/members/{member_id}/unpreserved.json"
 
     push_json_to_s3(
         s3=s3,
         json_obj=unpreserved_samples,
```

### Comparing `preservation-database-0.0.91/preservationdatabase/models.py` & `preservation-database-0.0.92/preservationdatabase/models.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/preservationdatabase/test_data/tests.jsonl` & `preservation-database-0.0.92/preservationdatabase/test_data/tests.jsonl`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/preservationdatabase/tests/test_archives.py` & `preservation-database-0.0.92/preservationdatabase/tests/test_archives.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/preservationdatabase/urls.py` & `preservation-database-0.0.92/preservationdatabase/urls.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/preservationdatabase/utils.py` & `preservation-database-0.0.92/preservationdatabase/utils.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.91/pyproject.toml` & `preservation-database-0.0.92/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "preservation-database"
-version = "0.0.91"
+version = "0.0.92"
 description = "A database builder for digital preservation information."
 readme = "README.md"
 requires-python = ">=3.8"
 license = {file = "LICENSE.md"}
 keywords = ["digital preservation", "academic"]
 authors = [
   {email = "meve@crossref.org"},
```

### Comparing `preservation-database-0.0.91/setup.cfg` & `preservation-database-0.0.92/setup.cfg`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = preservation-database
-version = 0.0.91
+version = 0.0.92
 description = A database builder for digital preservation information.
 url = https://gitlab.com/crossref/labs/preservationDatabase
 author = Martin Paul Eve
 author_email = martin@eve.gd
 license = MIT
 classifiers = 
 	Environment :: Web Environment
```

