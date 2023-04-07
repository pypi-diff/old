# Comparing `tmp/gnuhealth_genetics_uniprot-4.2.0.tar.gz` & `tmp/gnuhealth_genetics_uniprot-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_genetics_uniprot-4.2.0.tar", last modified: Sat Feb 11 21:55:42 2023, max compression
+gzip compressed data, was "gnuhealth_genetics_uniprot-4.2.1.tar", last modified: Fri Apr  7 10:17:45 2023, max compression
```

## Comparing `gnuhealth_genetics_uniprot-4.2.0.tar` & `gnuhealth_genetics_uniprot-4.2.1.tar`

### file list

```diff
@@ -1,36 +1,36 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:42.358464 gnuhealth_genetics_uniprot-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       60 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)      920 2023-02-11 21:55:42.358282 gnuhealth_genetics_uniprot-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      786 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:42.346679 gnuhealth_genetics_uniprot-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)   392196 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/data/disease_genes_uniprot.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)  6378586 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/data/gene_variants.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)  3777680 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/data/protein_diseases.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)  6737901 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/data/variant_phenotypes.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:42.354796 gnuhealth_genetics_uniprot-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      779 2023-01-18 16:33:07.000000 gnuhealth_genetics_uniprot-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:42.357990 gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      920 2023-02-11 21:55:42.000000 gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)      973 2023-02-11 21:55:42.000000 gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:42.000000 gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       76 2023-02-11 21:55:42.000000 gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:42.000000 gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       26 2023-02-11 21:55:42.000000 gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:55:42.000000 gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/top_level.txt
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:42.356990 gnuhealth_genetics_uniprot-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)   527151 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   526801 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   527199 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   542274 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   526801 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   526801 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   526801 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   672125 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:55:42.358511 gnuhealth_genetics_uniprot-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3689 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:42.357394 gnuhealth_genetics_uniprot-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      243 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      627 2023-01-18 16:33:08.000000 gnuhealth_genetics_uniprot-4.2.0/tests/test_health_genetics_uniprot.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      183 2023-02-11 12:44:33.000000 gnuhealth_genetics_uniprot-4.2.0/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:45.843873 gnuhealth_genetics_uniprot-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       60 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)      920 2023-04-07 10:17:45.843709 gnuhealth_genetics_uniprot-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      786 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:45.837309 gnuhealth_genetics_uniprot-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)   392196 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/data/disease_genes_uniprot.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)  6378586 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/data/gene_variants.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)  3777680 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/data/protein_diseases.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)  6737901 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/data/variant_phenotypes.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:45.840182 gnuhealth_genetics_uniprot-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      779 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:45.843411 gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      920 2023-04-07 10:17:45.000000 gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)      973 2023-04-07 10:17:45.000000 gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:45.000000 gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       76 2023-04-07 10:17:45.000000 gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:45.000000 gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       26 2023-04-07 10:17:45.000000 gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:17:45.000000 gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/top_level.txt
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:45.842328 gnuhealth_genetics_uniprot-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)   527151 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   526801 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   527199 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   542274 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   526801 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   526801 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   526801 2022-11-28 22:17:47.000000 gnuhealth_genetics_uniprot-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   672125 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:17:45.843912 gnuhealth_genetics_uniprot-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3689 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:45.842803 gnuhealth_genetics_uniprot-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      243 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      627 2023-04-07 09:17:52.000000 gnuhealth_genetics_uniprot-4.2.1/tests/test_health_genetics_uniprot.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      183 2023-04-07 09:37:21.000000 gnuhealth_genetics_uniprot-4.2.1/tryton.cfg
```

### Comparing `gnuhealth_genetics_uniprot-4.2.0/COPYING` & `gnuhealth_genetics_uniprot-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/PKG-INFO` & `gnuhealth_genetics_uniprot-4.2.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_genetics_uniprot
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Genetics UniProt Human Natural Variants Database
 Home-page: https://www.gnuhealth.org/
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_genetics_uniprot-4.2.0/README.rst` & `gnuhealth_genetics_uniprot-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/__init__.py` & `gnuhealth_genetics_uniprot-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/data/disease_genes_uniprot.xml` & `gnuhealth_genetics_uniprot-4.2.1/data/disease_genes_uniprot.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/data/gene_variants.xml` & `gnuhealth_genetics_uniprot-4.2.1/data/gene_variants.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/data/protein_diseases.xml` & `gnuhealth_genetics_uniprot-4.2.1/data/protein_diseases.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/data/variant_phenotypes.xml` & `gnuhealth_genetics_uniprot-4.2.1/data/variant_phenotypes.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/doc/index.rst` & `gnuhealth_genetics_uniprot-4.2.1/doc/index.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/PKG-INFO` & `gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-genetics-uniprot
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Genetics UniProt Human Natural Variants Database
 Home-page: https://www.gnuhealth.org/
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_genetics_uniprot-4.2.0/gnuhealth_genetics_uniprot.egg-info/SOURCES.txt` & `gnuhealth_genetics_uniprot-4.2.1/gnuhealth_genetics_uniprot.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/locale/de.po` & `gnuhealth_genetics_uniprot-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/locale/el.po` & `gnuhealth_genetics_uniprot-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/locale/es.po` & `gnuhealth_genetics_uniprot-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/locale/fr.po` & `gnuhealth_genetics_uniprot-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/locale/it_IT.po` & `gnuhealth_genetics_uniprot-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/locale/ja_JP.po` & `gnuhealth_genetics_uniprot-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/locale/lo.po` & `gnuhealth_genetics_uniprot-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/locale/zh_CN.po` & `gnuhealth_genetics_uniprot-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/setup.py` & `gnuhealth_genetics_uniprot-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics_uniprot-4.2.0/tests/test_health_genetics_uniprot.py` & `gnuhealth_genetics_uniprot-4.2.1/tests/test_health_genetics_uniprot.py`

 * *Files identical despite different names*

