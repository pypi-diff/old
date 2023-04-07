# Comparing `tmp/bioat-0.1.5.0.tar.gz` & `tmp/bioat-0.1.5.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "bioat-0.1.5.0.tar", max compression
+gzip compressed data, was "bioat-0.1.5.1.tar", max compression
```

## Comparing `bioat-0.1.5.0.tar` & `bioat-0.1.5.1.tar`

### file list

```diff
@@ -1,22 +1,22 @@
--rw-r--r--   0        0        0     1080 2022-10-12 10:28:48.000000 bioat-0.1.5.0/LICENSE
--rw-r--r--   0        0        0     1215 2023-03-31 15:29:35.600902 bioat-0.1.5.0/README.md
--rw-r--r--   0        0        0     1044 2023-04-07 08:01:46.846952 bioat-0.1.5.0/pyproject.toml
--rw-r--r--   0        0        0      471 2023-04-01 11:15:49.201131 bioat-0.1.5.0/src/bioat/__init__.py
--rw-r--r--   0        0        0      508 2023-04-02 12:41:49.000000 bioat-0.1.5.0/src/bioat/about.py
--rw-r--r--   0        0        0    13130 2023-03-31 17:13:33.632897 bioat-0.1.5.0/src/bioat/bam.py
--rw-r--r--   0        0        0     1413 2023-04-06 11:55:25.000000 bioat-0.1.5.0/src/bioat/cli.py
--rw-r--r--   0        0        0       63 2022-10-12 10:34:44.000000 bioat-0.1.5.0/src/bioat/exceptions.py
--rw-r--r--   0        0        0    11016 2023-03-13 04:00:08.114588 bioat-0.1.5.0/src/bioat/fastx.py
--rw-r--r--   0        0        0      818 2023-03-13 04:16:15.365909 bioat-0.1.5.0/src/bioat/genome.py
--rw-r--r--   0        0        0     5529 2023-04-06 10:53:27.000000 bioat-0.1.5.0/src/bioat/hic.py
--rw-r--r--   0        0        0        0 2023-04-01 12:21:31.028419 bioat-0.1.5.0/src/bioat/lib/__init__.py
--rw-r--r--   0        0        0      854 2023-04-01 13:16:24.000000 bioat-0.1.5.0/src/bioat/lib/_dev_tools.py
--rw-r--r--   0        0        0     2285 2023-04-06 10:50:24.000000 bioat-0.1.5.0/src/bioat/lib/libcolor.py
--rw-r--r--   0        0        0     7917 2023-04-06 10:50:04.000000 bioat-0.1.5.0/src/bioat/lib/libcrispr.py
--rw-r--r--   0        0        0     1128 2023-03-26 11:49:26.175731 bioat-0.1.5.0/src/bioat/logger.py
--rw-r--r--   0        0        0      685 2023-03-13 15:37:04.537990 bioat-0.1.5.0/src/bioat/mgi.py
--rw-r--r--   0        0        0     5629 2023-03-12 14:27:33.279607 bioat-0.1.5.0/src/bioat/system.py
--rw-r--r--   0        0        0     3245 2023-04-07 08:00:16.234706 bioat-0.1.5.0/src/bioat/table.py
--rw-r--r--   0        0        0    23903 2023-04-06 13:09:33.000000 bioat-0.1.5.0/src/bioat/targeted_deep_sequencing.py
--rw-r--r--   0        0        0      536 2023-04-06 12:41:33.000000 bioat-0.1.5.0/src/bioat/version.py
--rw-r--r--   0        0        0     2207 1970-01-01 00:00:00.000000 bioat-0.1.5.0/PKG-INFO
+-rw-r--r--   0        0        0     1080 2022-10-12 10:28:48.000000 bioat-0.1.5.1/LICENSE
+-rw-r--r--   0        0        0     1215 2023-03-31 15:29:35.600902 bioat-0.1.5.1/README.md
+-rw-r--r--   0        0        0     1044 2023-04-07 08:13:22.521088 bioat-0.1.5.1/pyproject.toml
+-rw-r--r--   0        0        0      471 2023-04-01 11:15:49.201131 bioat-0.1.5.1/src/bioat/__init__.py
+-rw-r--r--   0        0        0      508 2023-04-02 12:41:49.000000 bioat-0.1.5.1/src/bioat/about.py
+-rw-r--r--   0        0        0    13130 2023-03-31 17:13:33.632897 bioat-0.1.5.1/src/bioat/bam.py
+-rw-r--r--   0        0        0     1413 2023-04-06 11:55:25.000000 bioat-0.1.5.1/src/bioat/cli.py
+-rw-r--r--   0        0        0       63 2022-10-12 10:34:44.000000 bioat-0.1.5.1/src/bioat/exceptions.py
+-rw-r--r--   0        0        0    11016 2023-03-13 04:00:08.114588 bioat-0.1.5.1/src/bioat/fastx.py
+-rw-r--r--   0        0        0      818 2023-03-13 04:16:15.365909 bioat-0.1.5.1/src/bioat/genome.py
+-rw-r--r--   0        0        0     5529 2023-04-06 10:53:27.000000 bioat-0.1.5.1/src/bioat/hic.py
+-rw-r--r--   0        0        0        0 2023-04-01 12:21:31.028419 bioat-0.1.5.1/src/bioat/lib/__init__.py
+-rw-r--r--   0        0        0      854 2023-04-01 13:16:24.000000 bioat-0.1.5.1/src/bioat/lib/_dev_tools.py
+-rw-r--r--   0        0        0     2285 2023-04-06 10:50:24.000000 bioat-0.1.5.1/src/bioat/lib/libcolor.py
+-rw-r--r--   0        0        0     7917 2023-04-06 10:50:04.000000 bioat-0.1.5.1/src/bioat/lib/libcrispr.py
+-rw-r--r--   0        0        0     1128 2023-03-26 11:49:26.175731 bioat-0.1.5.1/src/bioat/logger.py
+-rw-r--r--   0        0        0      685 2023-03-13 15:37:04.537990 bioat-0.1.5.1/src/bioat/mgi.py
+-rw-r--r--   0        0        0     5629 2023-03-12 14:27:33.279607 bioat-0.1.5.1/src/bioat/system.py
+-rw-r--r--   0        0        0     3245 2023-04-07 08:00:16.234706 bioat-0.1.5.1/src/bioat/table.py
+-rw-r--r--   0        0        0    23903 2023-04-06 13:09:33.000000 bioat-0.1.5.1/src/bioat/targeted_deep_sequencing.py
+-rw-r--r--   0        0        0      384 2023-04-07 08:13:27.906137 bioat-0.1.5.1/src/bioat/version.py
+-rw-r--r--   0        0        0     2207 1970-01-01 00:00:00.000000 bioat-0.1.5.1/PKG-INFO
```

### Comparing `bioat-0.1.5.0/LICENSE` & `bioat-0.1.5.1/LICENSE`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/README.md` & `bioat-0.1.5.1/README.md`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/pyproject.toml` & `bioat-0.1.5.1/pyproject.toml`

 * *Files 8% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [tool.poetry]
 name = "bioat"
-version = "0.1.5.0"
+version = "0.1.5.1"
 description = "Bioinformatic toolkit with python (It's still under development!)"
 license = "MIT"
 authors = ["Herman Zhao <hermanzhaozzzz@gmail.com>"]
 repository = "https://github.com/hermanzhaozzzz/BioinformaticAnalysisTools"
 homepage = "https://github.com/hermanzhaozzzz/BioinformaticAnalysisTools"
 # README file(s) are used as the package description
 readme = "README.md"
```

### Comparing `bioat-0.1.5.0/src/bioat/bam.py` & `bioat-0.1.5.1/src/bioat/bam.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/cli.py` & `bioat-0.1.5.1/src/bioat/cli.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/fastx.py` & `bioat-0.1.5.1/src/bioat/fastx.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/genome.py` & `bioat-0.1.5.1/src/bioat/genome.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/hic.py` & `bioat-0.1.5.1/src/bioat/hic.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/lib/_dev_tools.py` & `bioat-0.1.5.1/src/bioat/lib/_dev_tools.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/lib/libcolor.py` & `bioat-0.1.5.1/src/bioat/lib/libcolor.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/lib/libcrispr.py` & `bioat-0.1.5.1/src/bioat/lib/libcrispr.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/logger.py` & `bioat-0.1.5.1/src/bioat/logger.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/mgi.py` & `bioat-0.1.5.1/src/bioat/mgi.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/system.py` & `bioat-0.1.5.1/src/bioat/system.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/table.py` & `bioat-0.1.5.1/src/bioat/table.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/src/bioat/targeted_deep_sequencing.py` & `bioat-0.1.5.1/src/bioat/targeted_deep_sequencing.py`

 * *Files identical despite different names*

### Comparing `bioat-0.1.5.0/PKG-INFO` & `bioat-0.1.5.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: bioat
-Version: 0.1.5.0
+Version: 0.1.5.1
 Summary: Bioinformatic toolkit with python (It's still under development!)
 Home-page: https://github.com/hermanzhaozzzz/BioinformaticAnalysisTools
 License: MIT
 Author: Herman Zhao
 Author-email: hermanzhaozzzz@gmail.com
 Requires-Python: >=3.9.6,<4.0.0
 Classifier: License :: OSI Approved :: MIT License
```

