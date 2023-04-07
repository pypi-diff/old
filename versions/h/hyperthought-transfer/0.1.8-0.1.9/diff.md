# Comparing `tmp/hyperthought-transfer-0.1.8.tar.gz` & `tmp/hyperthought-transfer-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "C:\Users\Jason\Documents\repos\hyperthought-transfer\dist\tmpj8wxhaam\hyperthought-transfer-0.1.8.tar", last modified: Wed Jan 11 04:00:37 2023, max compression
+gzip compressed data, was "C:\Users\Jason\Documents\repos\hyperthought-transfer\dist\tmpljs6z5h9\hyperthought-transfer-0.1.9.tar", last modified: Wed Jan 11 06:03:11 2023, max compression
```

## Comparing `hyperthought-transfer-0.1.8.tar` & `hyperthought-transfer-0.1.9.tar`

### file list

```diff
@@ -1,53 +1,53 @@
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/
--rw-rw-rw-   0        0        0      632 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/.coveragerc
--rw-rw-rw-   0        0        0      661 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.8/.gitignore
--rw-rw-rw-   0        0        0      514 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.8/.readthedocs.yml
--rw-rw-rw-   0        0        0       84 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/AUTHORS.rst
--rw-rw-rw-   0        0        0      141 2022-05-17 15:55:48.000000 hyperthought-transfer-0.1.8/CHANGELOG.rst
--rw-rw-rw-   0        0        0    14388 2022-12-27 15:26:41.000000 hyperthought-transfer-0.1.8/CONTRIBUTING.rst
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/docs/
--rw-rw-rw-   0        0        0       43 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/authors.rst
--rw-rw-rw-   0        0        0       45 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/changelog.rst
--rw-rw-rw-   0        0        0    10090 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/conf.py
--rw-rw-rw-   0        0        0       34 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/contributing.rst
--rw-rw-rw-   0        0        0     2430 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/index.rst
--rw-rw-rw-   0        0        0       74 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/license.rst
--rw-rw-rw-   0        0        0     1183 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/Makefile
--rw-rw-rw-   0        0        0       41 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/readme.rst
--rw-rw-rw-   0        0        0      238 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/requirements.txt
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/docs/_static/
--rw-rw-rw-   0        0        0       19 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/docs/_static/.gitignore
--rw-rw-rw-   0        0        0     1100 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/LICENSE.txt
--rw-rw-rw-   0        0        0       74 2023-01-09 12:22:58.000000 hyperthought-transfer-0.1.8/MANIFEST.in
--rw-rw-rw-   0        0        0     2766 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/PKG-INFO
--rw-rw-rw-   0        0        0     2198 2022-05-17 15:55:48.000000 hyperthought-transfer-0.1.8/README.rst
--rw-rw-rw-   0        0        0     1335 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/setup.cfg
--rw-rw-rw-   0        0        0     1025 2023-01-11 04:00:09.000000 hyperthought-transfer-0.1.8/setup.py
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/antivirus/
--rw-rw-rw-   0        0        0     2359 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/antivirus/base.py
--rw-rw-rw-   0        0        0     2893 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/antivirus/_mcafee.py
--rw-rw-rw-   0        0        0     2957 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/antivirus/__init__.py
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/
--rw-rw-rw-   0        0        0     1635 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/connect.py
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/template/
--rw-rw-rw-   0        0        0     1581 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/template/create.py
--rw-rw-rw-   0        0        0   102400 2023-01-09 12:22:58.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/template/template.db
--rw-rw-rw-   0        0        0       22 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/template/__init__.py
--rw-rw-rw-   0        0        0    34890 2023-01-11 03:59:52.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/__init__.py
--rw-rw-rw-   0        0        0     2046 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/utils.py
--rw-rw-rw-   0        0        0    24384 2023-01-11 03:59:52.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/__init__.py
--rw-rw-rw-   0        0        0      645 2022-10-24 14:27:48.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer/__init__.py
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer.egg-info/
--rw-rw-rw-   0        0        0        1 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        2 2022-05-16 11:27:09.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer.egg-info/not-zip-safe
--rw-rw-rw-   0        0        0     2766 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0       86 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer.egg-info/requires.txt
--rw-rw-rw-   0        0        0     1228 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0       22 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/src/hyperthought_transfer.egg-info/top_level.txt
-drwxrwxrwx   0        0        0        0 2023-01-11 04:00:37.000000 hyperthought-transfer-0.1.8/tests/
--rw-rw-rw-   0        0        0      299 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/tests/conftest.py
--rw-rw-rw-   0        0        0      622 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/tests/test_skeleton.py
--rw-rw-rw-   0        0        0     2659 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.8/tox.ini
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/
+-rw-rw-rw-   0        0        0      632 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/.coveragerc
+-rw-rw-rw-   0        0        0      661 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.9/.gitignore
+-rw-rw-rw-   0        0        0      514 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.9/.readthedocs.yml
+-rw-rw-rw-   0        0        0       84 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/AUTHORS.rst
+-rw-rw-rw-   0        0        0      141 2022-05-17 15:55:48.000000 hyperthought-transfer-0.1.9/CHANGELOG.rst
+-rw-rw-rw-   0        0        0    14388 2022-12-27 15:26:41.000000 hyperthought-transfer-0.1.9/CONTRIBUTING.rst
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/docs/
+-rw-rw-rw-   0        0        0       43 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/authors.rst
+-rw-rw-rw-   0        0        0       45 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/changelog.rst
+-rw-rw-rw-   0        0        0    10090 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/conf.py
+-rw-rw-rw-   0        0        0       34 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/contributing.rst
+-rw-rw-rw-   0        0        0     2430 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/index.rst
+-rw-rw-rw-   0        0        0       74 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/license.rst
+-rw-rw-rw-   0        0        0     1183 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/Makefile
+-rw-rw-rw-   0        0        0       41 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/readme.rst
+-rw-rw-rw-   0        0        0      238 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/requirements.txt
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/docs/_static/
+-rw-rw-rw-   0        0        0       19 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/docs/_static/.gitignore
+-rw-rw-rw-   0        0        0     1100 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/LICENSE.txt
+-rw-rw-rw-   0        0        0       74 2023-01-09 12:22:58.000000 hyperthought-transfer-0.1.9/MANIFEST.in
+-rw-rw-rw-   0        0        0     2766 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/PKG-INFO
+-rw-rw-rw-   0        0        0     2198 2022-05-17 15:55:48.000000 hyperthought-transfer-0.1.9/README.rst
+-rw-rw-rw-   0        0        0     1335 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/setup.cfg
+-rw-rw-rw-   0        0        0     1025 2023-01-11 06:02:52.000000 hyperthought-transfer-0.1.9/setup.py
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/antivirus/
+-rw-rw-rw-   0        0        0     2359 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/antivirus/base.py
+-rw-rw-rw-   0        0        0     2893 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/antivirus/_mcafee.py
+-rw-rw-rw-   0        0        0     2957 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/antivirus/__init__.py
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/
+-rw-rw-rw-   0        0        0     1635 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/connect.py
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/template/
+-rw-rw-rw-   0        0        0     1581 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/template/create.py
+-rw-rw-rw-   0        0        0   102400 2023-01-09 12:22:58.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/template/template.db
+-rw-rw-rw-   0        0        0       22 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/template/__init__.py
+-rw-rw-rw-   0        0        0    35266 2023-01-11 06:01:36.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/__init__.py
+-rw-rw-rw-   0        0        0     2046 2023-01-03 12:02:08.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/utils.py
+-rw-rw-rw-   0        0        0    24543 2023-01-11 06:00:20.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/__init__.py
+-rw-rw-rw-   0        0        0      645 2022-10-24 14:27:48.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer/__init__.py
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer.egg-info/
+-rw-rw-rw-   0        0        0        1 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        2 2022-05-16 11:27:09.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer.egg-info/not-zip-safe
+-rw-rw-rw-   0        0        0     2766 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0       86 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer.egg-info/requires.txt
+-rw-rw-rw-   0        0        0     1228 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0       22 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/src/hyperthought_transfer.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-01-11 06:03:11.000000 hyperthought-transfer-0.1.9/tests/
+-rw-rw-rw-   0        0        0      299 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/tests/conftest.py
+-rw-rw-rw-   0        0        0      622 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/tests/test_skeleton.py
+-rw-rw-rw-   0        0        0     2659 2022-04-26 15:06:17.000000 hyperthought-transfer-0.1.9/tox.ini
```

### Comparing `hyperthought-transfer-0.1.8/.coveragerc` & `hyperthought-transfer-0.1.9/.coveragerc`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/.gitignore` & `hyperthought-transfer-0.1.9/.gitignore`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/.readthedocs.yml` & `hyperthought-transfer-0.1.9/.readthedocs.yml`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/CONTRIBUTING.rst` & `hyperthought-transfer-0.1.9/CONTRIBUTING.rst`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/docs/conf.py` & `hyperthought-transfer-0.1.9/docs/conf.py`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/docs/index.rst` & `hyperthought-transfer-0.1.9/docs/index.rst`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/docs/Makefile` & `hyperthought-transfer-0.1.9/docs/Makefile`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/LICENSE.txt` & `hyperthought-transfer-0.1.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/PKG-INFO` & `hyperthought-transfer-0.1.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hyperthought-transfer
-Version: 0.1.8
+Version: 0.1.9
 Summary: Package used to upload files to and download files from the HyperThought® content management system.
 Home-page: https://github.com/pyscaffold/pyscaffold/
 Author: Jason Thiese
 Author-email: jthiese@ues.com
 License: MIT
 Project-URL: Documentation, https://pyscaffold.org/
 Platform: any
```

### Comparing `hyperthought-transfer-0.1.8/README.rst` & `hyperthought-transfer-0.1.9/README.rst`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/setup.cfg` & `hyperthought-transfer-0.1.9/setup.cfg`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/setup.py` & `hyperthought-transfer-0.1.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -8,15 +8,15 @@
 """
 from setuptools import setup, find_packages
 
 
 if __name__ == "__main__":
     try:
         setup(
-            version="0.1.8",
+            version="0.1.9",
             use_scm_version={
                 "version_scheme": "no-guess-dev",
                 "local-scheme": "no-local-version",
             },
             packages=find_packages(where="src"),
             package_dir={"": "src"},
             include_package_data=True,
```

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/antivirus/base.py` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/antivirus/base.py`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/antivirus/_mcafee.py` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/antivirus/_mcafee.py`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/antivirus/__init__.py` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/antivirus/__init__.py`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/connect.py` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/connect.py`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/template/create.py` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/template/create.py`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/template/template.db` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/template/template.db`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/database/__init__.py` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/database/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -233,14 +233,26 @@
         cursor = self.connection.cursor()
         sql = "DELETE FROM File WHERE id = :id"
         cursor.execute(sql, {"id": file_id})
 
         if commit:
             self.connection.commit()
 
+    def get_total_size(self) -> int:
+        """Get the sum of file sizes for all files in the manifest."""
+        sql = """
+        SELECT SUM(size) AS total_bytes
+        FROM File
+        WHERE size IS NOT NULL
+        """
+        cursor = self.connection.cursor()
+        cursor.execute(sql)
+        row = cursor.fetchone()
+        return row["total_bytes"]
+
     def create_parser(
         self,
         file_id: int,
         parser_class: str,
         metadata_id: int,
         commit: bool = True,
     ) -> Optional[int]:
```

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/utils.py` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/utils.py`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/manifest/__init__.py` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/manifest/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -630,14 +630,18 @@
         if use_pool:
             self._compute_file_info_with_pool(n_processes=n_processes)
         else:
             self._compute_file_info_without_pool()
 
         self._file_info_computed = True
 
+    def get_total_size(self) -> int:
+        """Get the sum of file sizes for all files in the manifest."""
+        return self.database.get_total_size()
+
     def close(self, compute_file_info: bool = True) -> None:
         """
         Close the manifest (database).
 
         Parameters
         ----------
         compute_file_info : bool
```

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer/__init__.py` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer/__init__.py`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer.egg-info/PKG-INFO` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hyperthought-transfer
-Version: 0.1.8
+Version: 0.1.9
 Summary: Package used to upload files to and download files from the HyperThought® content management system.
 Home-page: https://github.com/pyscaffold/pyscaffold/
 Author: Jason Thiese
 Author-email: jthiese@ues.com
 License: MIT
 Project-URL: Documentation, https://pyscaffold.org/
 Platform: any
```

### Comparing `hyperthought-transfer-0.1.8/src/hyperthought_transfer.egg-info/SOURCES.txt` & `hyperthought-transfer-0.1.9/src/hyperthought_transfer.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/tests/test_skeleton.py` & `hyperthought-transfer-0.1.9/tests/test_skeleton.py`

 * *Files identical despite different names*

### Comparing `hyperthought-transfer-0.1.8/tox.ini` & `hyperthought-transfer-0.1.9/tox.ini`

 * *Files identical despite different names*

