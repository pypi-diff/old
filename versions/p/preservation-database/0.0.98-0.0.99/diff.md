# Comparing `tmp/preservation-database-0.0.98.tar.gz` & `tmp/preservation-database-0.0.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "preservation-database-0.0.98.tar", last modified: Thu Apr  6 16:11:43 2023, max compression
+gzip compressed data, was "preservation-database-0.0.99.tar", last modified: Thu Apr  6 16:21:46 2023, max compression
```

## Comparing `preservation-database-0.0.98.tar` & `preservation-database-0.0.99.tar`

### file list

```diff
@@ -1,27 +1,27 @@
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/
--rw-rw-r--   0 martin    (1000) martin    (1000)      129 2023-02-06 17:29:02.000000 preservation-database-0.0.98/MANIFEST.in
--rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 16:11:43.704483 preservation-database-0.0.98/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)     4701 2023-04-06 16:11:39.000000 preservation-database-0.0.98/README.md
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/preservation_database.egg-info/
--rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/PKG-INFO
--rw-rw-r--   0 martin    (1000) martin    (1000)      691 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/SOURCES.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/dependency_links.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)      208 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/requires.txt
--rw-rw-r--   0 martin    (1000) martin    (1000)       21 2023-04-06 16:11:43.000000 preservation-database-0.0.98/preservation_database.egg-info/top_level.txt
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/preservationdatabase/
--rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:14:23.000000 preservation-database-0.0.98/preservationdatabase/__init__.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    15336 2023-04-06 15:46:52.000000 preservation-database-0.0.98/preservationdatabase/cli.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      660 2023-03-01 11:09:55.000000 preservation-database-0.0.98/preservationdatabase/constants.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     1597 2023-03-05 12:44:30.000000 preservation-database-0.0.98/preservationdatabase/environment.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     3450 2023-02-19 18:38:37.000000 preservation-database-0.0.98/preservationdatabase/example_settings.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    34670 2023-04-06 16:11:32.000000 preservation-database-0.0.98/preservationdatabase/exporter.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    42928 2023-04-06 14:20:58.000000 preservation-database-0.0.98/preservationdatabase/models.py
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/preservationdatabase/test_data/
--rw-rw-r--   0 martin    (1000) martin    (1000)      888 2023-02-06 10:17:59.000000 preservation-database-0.0.98/preservationdatabase/test_data/tests.jsonl
-drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:11:43.704483 preservation-database-0.0.98/preservationdatabase/tests/
--rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:20:11.000000 preservation-database-0.0.98/preservationdatabase/tests/__init__.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     2072 2023-02-06 10:15:46.000000 preservation-database-0.0.98/preservationdatabase/tests/test_archives.py
--rw-rw-r--   0 martin    (1000) martin    (1000)      767 2023-02-19 18:38:37.000000 preservation-database-0.0.98/preservationdatabase/urls.py
--rw-rw-r--   0 martin    (1000) martin    (1000)    20636 2023-04-06 13:59:40.000000 preservation-database-0.0.98/preservationdatabase/utils.py
--rw-rw-r--   0 martin    (1000) martin    (1000)     1238 2023-04-06 16:11:37.000000 preservation-database-0.0.98/pyproject.toml
--rw-rw-r--   0 martin    (1000) martin    (1000)     1143 2023-04-06 16:11:43.704483 preservation-database-0.0.98/setup.cfg
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:21:46.792799 preservation-database-0.0.99/
+-rw-rw-r--   0 martin    (1000) martin    (1000)      129 2023-02-06 17:29:02.000000 preservation-database-0.0.99/MANIFEST.in
+-rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 16:21:46.792799 preservation-database-0.0.99/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)     4701 2023-04-06 16:21:42.000000 preservation-database-0.0.99/README.md
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:21:46.792799 preservation-database-0.0.99/preservation_database.egg-info/
+-rw-rw-r--   0 martin    (1000) martin    (1000)     5481 2023-04-06 16:21:46.000000 preservation-database-0.0.99/preservation_database.egg-info/PKG-INFO
+-rw-rw-r--   0 martin    (1000) martin    (1000)      691 2023-04-06 16:21:46.000000 preservation-database-0.0.99/preservation_database.egg-info/SOURCES.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)        1 2023-04-06 16:21:46.000000 preservation-database-0.0.99/preservation_database.egg-info/dependency_links.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)      208 2023-04-06 16:21:46.000000 preservation-database-0.0.99/preservation_database.egg-info/requires.txt
+-rw-rw-r--   0 martin    (1000) martin    (1000)       21 2023-04-06 16:21:46.000000 preservation-database-0.0.99/preservation_database.egg-info/top_level.txt
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:21:46.792799 preservation-database-0.0.99/preservationdatabase/
+-rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:14:23.000000 preservation-database-0.0.99/preservationdatabase/__init__.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    15336 2023-04-06 15:46:52.000000 preservation-database-0.0.99/preservationdatabase/cli.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)      660 2023-03-01 11:09:55.000000 preservation-database-0.0.99/preservationdatabase/constants.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1597 2023-03-05 12:44:30.000000 preservation-database-0.0.99/preservationdatabase/environment.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     3450 2023-02-19 18:38:37.000000 preservation-database-0.0.99/preservationdatabase/example_settings.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    35165 2023-04-06 16:21:20.000000 preservation-database-0.0.99/preservationdatabase/exporter.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    42928 2023-04-06 14:20:58.000000 preservation-database-0.0.99/preservationdatabase/models.py
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:21:46.792799 preservation-database-0.0.99/preservationdatabase/test_data/
+-rw-rw-r--   0 martin    (1000) martin    (1000)      888 2023-02-06 10:17:59.000000 preservation-database-0.0.99/preservationdatabase/test_data/tests.jsonl
+drwxrwxr-x   0 martin    (1000) martin    (1000)        0 2023-04-06 16:21:46.792799 preservation-database-0.0.99/preservationdatabase/tests/
+-rw-rw-r--   0 martin    (1000) martin    (1000)        0 2023-02-06 09:20:11.000000 preservation-database-0.0.99/preservationdatabase/tests/__init__.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     2072 2023-02-06 10:15:46.000000 preservation-database-0.0.99/preservationdatabase/tests/test_archives.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)      767 2023-02-19 18:38:37.000000 preservation-database-0.0.99/preservationdatabase/urls.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)    20645 2023-04-06 16:16:36.000000 preservation-database-0.0.99/preservationdatabase/utils.py
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1238 2023-04-06 16:21:38.000000 preservation-database-0.0.99/pyproject.toml
+-rw-rw-r--   0 martin    (1000) martin    (1000)     1143 2023-04-06 16:21:46.792799 preservation-database-0.0.99/setup.cfg
```

### Comparing `preservation-database-0.0.98/PKG-INFO` & `preservation-database-0.0.99/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: preservation-database
-Version: 0.0.98
+Version: 0.0.99
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
-Metadata-Version: 2.1 Name: preservation-database Version: 0.0.98 Summary: A
+Metadata-Version: 2.1 Name: preservation-database Version: 0.0.99 Summary: A
 database builder for digital preservation information. Home-page: https://
 gitlab.com/crossref/labs/preservationDatabase Author: Martin Paul Eve Author-
 email: meve@crossref.org Maintainer-email: Martin Paul Eve
 crossref.org> Project-URL: homepage, https://labs.crossref.org Project-URL:
 documentation, https://labs.crossref.org Project-URL: repository, https://
 gitlab.com/crossref/labs/preservationDatabase Project-URL: changelog, https://
 gitlab.com/crossref/labs/preservation-data/-/blob/main/CHANGELOG.md Keywords:
```

### Comparing `preservation-database-0.0.98/README.md` & `preservation-database-0.0.99/README.md`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservation_database.egg-info/PKG-INFO` & `preservation-database-0.0.99/preservation_database.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: preservation-database
-Version: 0.0.98
+Version: 0.0.99
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
-Metadata-Version: 2.1 Name: preservation-database Version: 0.0.98 Summary: A
+Metadata-Version: 2.1 Name: preservation-database Version: 0.0.99 Summary: A
 database builder for digital preservation information. Home-page: https://
 gitlab.com/crossref/labs/preservationDatabase Author: Martin Paul Eve Author-
 email: meve@crossref.org Maintainer-email: Martin Paul Eve
 crossref.org> Project-URL: homepage, https://labs.crossref.org Project-URL:
 documentation, https://labs.crossref.org Project-URL: repository, https://
 gitlab.com/crossref/labs/preservationDatabase Project-URL: changelog, https://
 gitlab.com/crossref/labs/preservation-data/-/blob/main/CHANGELOG.md Keywords:
```

### Comparing `preservation-database-0.0.98/preservation_database.egg-info/SOURCES.txt` & `preservation-database-0.0.99/preservation_database.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservationdatabase/cli.py` & `preservation-database-0.0.99/preservationdatabase/cli.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservationdatabase/constants.py` & `preservation-database-0.0.99/preservationdatabase/constants.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservationdatabase/environment.py` & `preservation-database-0.0.99/preservationdatabase/environment.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservationdatabase/example_settings.py` & `preservation-database-0.0.99/preservationdatabase/example_settings.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservationdatabase/exporter.py` & `preservation-database-0.0.99/preservationdatabase/exporter.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 import hashlib
 import json
 import logging
 import os
 import sys
 from collections import defaultdict, OrderedDict
-from datetime import date
+from datetime import date, datetime
 from typing import DefaultDict, Any
 
 from caseconverter import kebabcase
 
 SAMPLES_BUCKET = "samples.research.crossref.org"
 SAMPLES_PATH = "members-works/2023-03-05/samples/"
 
@@ -335,14 +335,20 @@
                 # increment the correct counters for overall stats
                 if archive_count == 1:
                     one_archive += 1
                 elif archive_count == 2:
                     two_archives += 1
                 elif archive_count > 2:
                     three_archives += 1
+            else:
+                overall_status["excluded-current-year"] += 1
+                if verbose:
+                    logging.info(
+                        f"{result['DOI']} is excluded as is too recent"
+                    )
         else:
             # this is an excluded sample item
             if "type" in result and result["type"] != "journal-article":
                 overall_status["excluded-non-journal"] += 1
                 if verbose:
                     logging.info(
                         f"{result['DOI']} is excluded as it is not a journal "
@@ -623,44 +629,50 @@
 
     import botocore
 
     for sample in samples:
         sample = json.loads(sample)["data-point"]
 
         if "type" in sample and sample["type"] == "journal-article":
-            # print(f"Appending {sample['DOI']}")
+            year = None
 
-            md5_doi = hashlib.md5(sample["DOI"].lower().encode()).hexdigest()
+            if "published" in sample:
+                year = sample["published"]["date-parts"][0][0]
 
-            try:
-                annotation = get_annotation(
-                    s3client=s3client,
-                    member_id=member_id,
-                    annotation_name="preservation.json",
-                    annotations_bucket=ANNOTATION_BUCKET,
-                    annotations_path=ANNOTATION_PATH,
-                    path=f"works/{md5_doi}",
-                    use_member_id=False,
-                )
+            if year != datetime.now().year:
+                md5_doi = hashlib.md5(
+                    sample["DOI"].lower().encode()
+                ).hexdigest()
+
+                try:
+                    annotation = get_annotation(
+                        s3client=s3client,
+                        member_id=member_id,
+                        annotation_name="preservation.json",
+                        annotations_bucket=ANNOTATION_BUCKET,
+                        annotations_path=ANNOTATION_PATH,
+                        path=f"works/{md5_doi}",
+                        use_member_id=False,
+                    )
 
-                preserved = any(
-                    v.startswith("preserved")
-                    for v in annotation.values()
-                    if isinstance(v, str)
-                )
+                    preserved = any(
+                        v.startswith("preserved")
+                        for v in annotation.values()
+                        if isinstance(v, str)
+                    )
 
-                if not preserved:
-                    unpreserved_samples.append(annotation)
+                    if not preserved:
+                        unpreserved_samples.append(annotation)
 
-                overall_samples.append(annotation)
+                    overall_samples.append(annotation)
 
-            except Exception as e:
-                ...
-                # print(e)
-                # print(f"This DOI was excluded: {sample['DOI']}")
+                except Exception as e:
+                    ...
+                    # print(e)
+                    # print(f"This DOI was excluded: {sample['DOI']}")
 
     key = f"{REPORT_PATH}/members/{member_id}/preservation-report.json"
     unpreserved_key = f"{REPORT_PATH}/members/{member_id}/unpreserved.json"
 
     push_json_to_s3(
         s3=s3,
         json_obj=unpreserved_samples,
```

### Comparing `preservation-database-0.0.98/preservationdatabase/models.py` & `preservation-database-0.0.99/preservationdatabase/models.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservationdatabase/test_data/tests.jsonl` & `preservation-database-0.0.99/preservationdatabase/test_data/tests.jsonl`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservationdatabase/tests/test_archives.py` & `preservation-database-0.0.99/preservationdatabase/tests/test_archives.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservationdatabase/urls.py` & `preservation-database-0.0.99/preservationdatabase/urls.py`

 * *Files identical despite different names*

### Comparing `preservation-database-0.0.98/preservationdatabase/utils.py` & `preservation-database-0.0.99/preservationdatabase/utils.py`

 * *Files 0% similar despite different names*

```diff
@@ -154,25 +154,25 @@
         doi["container-title"] if "container-title" in doi else None
     )
     issns = set(doi["ISSN"]) if "ISSN" in doi else None
 
     volume = doi["volume"] if "volume" in doi else None
     no = doi["issue"] if "issue" in doi else None
 
-    logging.info(
-        f'Checking {doi["DOI"]}: {container_title} '
-        f"({issns}) v{volume} n{no}"
-    )
-
     year = None
     # "published": {"date-parts": [[2005, 12, 30]]}}}
 
     if "published" in doi:
         year = doi["published"]["date-parts"][0][0]
 
+    logging.info(
+        f'Checking {doi["DOI"]}: {container_title} '
+        f"({issns}) v{volume} n{no} ({year})"
+    )
+
     preserves, doi_echo = show_preservation(
         container_title,
         issns,
         volume,
         no,
         doi,
         archive,
```

### Comparing `preservation-database-0.0.98/pyproject.toml` & `preservation-database-0.0.99/pyproject.toml`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [project]
 name = "preservation-database"
-version = "0.0.98"
+version = "0.0.99"
 description = "A database builder for digital preservation information."
 readme = "README.md"
 requires-python = ">=3.8"
 license = {file = "LICENSE.md"}
 keywords = ["digital preservation", "academic"]
 authors = [
   {email = "meve@crossref.org"},
```

### Comparing `preservation-database-0.0.98/setup.cfg` & `preservation-database-0.0.99/setup.cfg`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = preservation-database
-version = 0.0.98
+version = 0.0.99
 description = A database builder for digital preservation information.
 url = https://gitlab.com/crossref/labs/preservationDatabase
 author = Martin Paul Eve
 author_email = martin@eve.gd
 license = MIT
 classifiers = 
 	Environment :: Web Environment
```

