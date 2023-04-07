# Comparing `tmp/gnuhealth_genetics-4.2.0.tar.gz` & `tmp/gnuhealth_genetics-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_genetics-4.2.0.tar", last modified: Sat Feb 11 21:55:37 2023, max compression
+gzip compressed data, was "gnuhealth_genetics-4.2.1.tar", last modified: Fri Apr  7 10:17:40 2023, max compression
```

## Comparing `gnuhealth_genetics-4.2.0.tar` & `gnuhealth_genetics-4.2.1.tar`

### file list

```diff
@@ -1,56 +1,56 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:37.507656 gnuhealth_genetics-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       60 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)      879 2023-02-11 21:55:37.507429 gnuhealth_genetics-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1219 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:37.498351 gnuhealth_genetics-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)  1956831 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/data/disease_genes.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2056 2023-01-18 16:33:07.000000 gnuhealth_genetics-4.2.0/data/gnuhealth_commands.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:37.498422 gnuhealth_genetics-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      461 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:37.506456 gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      879 2023-02-11 21:55:37.000000 gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1984 2023-02-11 21:55:37.000000 gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:37.000000 gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       68 2023-02-11 21:55:37.000000 gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:37.000000 gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       17 2023-02-11 21:55:37.000000 gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:55:37.000000 gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)    14474 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/health_genetics.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     9920 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/health_genetics_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:37.498526 gnuhealth_genetics-4.2.0/icons/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    11113 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.0/icons/dna.svg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:37.502050 gnuhealth_genetics-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)   489259 2023-02-11 12:36:12.000000 gnuhealth_genetics-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   487980 2023-01-18 16:33:07.000000 gnuhealth_genetics-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   505203 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   489130 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   560961 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   489823 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   490154 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   489818 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   489959 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   609810 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/locale/zh_CN.po
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:37.502561 gnuhealth_genetics-4.2.0/security/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5585 2023-01-18 16:33:07.000000 gnuhealth_genetics-4.2.0/security/access_rights.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:55:37.507712 gnuhealth_genetics-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3554 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:37.502846 gnuhealth_genetics-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      235 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      598 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/tests/test_health_genetics.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      170 2023-02-11 12:44:33.000000 gnuhealth_genetics-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:37.505561 gnuhealth_genetics-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      802 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_disease_gene.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      394 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_disease_gene_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      420 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_family_diseases.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      360 2023-01-18 16:33:07.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_family_diseases_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      474 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_gene_variant.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      493 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_gene_variant_phenotype.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      406 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_gene_variant_phenotype_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      351 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_gene_variant_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      883 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_genetic_risk.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      557 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_genetic_risk_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      490 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_patient.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1025 2023-01-18 16:33:07.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_protein_disease.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      395 2023-01-18 16:33:08.000000 gnuhealth_genetics-4.2.0/view/gnuhealth_protein_disease_tree.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:40.043649 gnuhealth_genetics-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       60 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)      879 2023-04-07 10:17:40.043507 gnuhealth_genetics-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1219 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:40.037967 gnuhealth_genetics-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)  1956831 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/data/disease_genes.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2056 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/data/gnuhealth_commands.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:40.038041 gnuhealth_genetics-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      461 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:40.042919 gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      879 2023-04-07 10:17:39.000000 gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1984 2023-04-07 10:17:40.000000 gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:39.000000 gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       68 2023-04-07 10:17:39.000000 gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:39.000000 gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       17 2023-04-07 10:17:39.000000 gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:17:39.000000 gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)    14474 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/health_genetics.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     9920 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/health_genetics_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:40.038114 gnuhealth_genetics-4.2.1/icons/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    11113 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.1/icons/dna.svg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:40.040997 gnuhealth_genetics-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)   489259 2023-02-11 12:36:12.000000 gnuhealth_genetics-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   487980 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   505203 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   489130 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   560961 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   489823 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   490154 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   489818 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   489959 2022-11-28 22:17:47.000000 gnuhealth_genetics-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   609810 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/locale/zh_CN.po
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:40.041329 gnuhealth_genetics-4.2.1/security/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5585 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/security/access_rights.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:17:40.043691 gnuhealth_genetics-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3554 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:40.041476 gnuhealth_genetics-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      235 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      598 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/tests/test_health_genetics.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      170 2023-04-07 09:37:21.000000 gnuhealth_genetics-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:40.042377 gnuhealth_genetics-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      802 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_disease_gene.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      394 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_disease_gene_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      420 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_family_diseases.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      360 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_family_diseases_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      474 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_gene_variant.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      493 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_gene_variant_phenotype.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      406 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_gene_variant_phenotype_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      351 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_gene_variant_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      883 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_genetic_risk.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      557 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_genetic_risk_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      490 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_patient.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1025 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_protein_disease.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      395 2023-04-07 09:17:52.000000 gnuhealth_genetics-4.2.1/view/gnuhealth_protein_disease_tree.xml
```

### Comparing `gnuhealth_genetics-4.2.0/COPYING` & `gnuhealth_genetics-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/PKG-INFO` & `gnuhealth_genetics-4.2.1/PKG-INFO`

 * *Files 14% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_genetics
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Genetics Module
 Home-page: https://www.gnuhealth.org/
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_genetics-4.2.0/README.rst` & `gnuhealth_genetics-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/__init__.py` & `gnuhealth_genetics-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/data/disease_genes.xml` & `gnuhealth_genetics-4.2.1/data/disease_genes.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/data/gnuhealth_commands.xml` & `gnuhealth_genetics-4.2.1/data/gnuhealth_commands.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/PKG-INFO` & `gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-genetics
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Genetics Module
 Home-page: https://www.gnuhealth.org/
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_genetics-4.2.0/gnuhealth_genetics.egg-info/SOURCES.txt` & `gnuhealth_genetics-4.2.1/gnuhealth_genetics.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/health_genetics.py` & `gnuhealth_genetics-4.2.1/health_genetics.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/health_genetics_view.xml` & `gnuhealth_genetics-4.2.1/health_genetics_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/icons/dna.svg` & `gnuhealth_genetics-4.2.1/icons/dna.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/ar.po` & `gnuhealth_genetics-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/de.po` & `gnuhealth_genetics-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/el.po` & `gnuhealth_genetics-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/es.po` & `gnuhealth_genetics-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/fr.po` & `gnuhealth_genetics-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/it_IT.po` & `gnuhealth_genetics-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/ja_JP.po` & `gnuhealth_genetics-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/lo.po` & `gnuhealth_genetics-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/pt_BR.po` & `gnuhealth_genetics-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/locale/zh_CN.po` & `gnuhealth_genetics-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/security/access_rights.xml` & `gnuhealth_genetics-4.2.1/security/access_rights.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/setup.py` & `gnuhealth_genetics-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/tests/test_health_genetics.py` & `gnuhealth_genetics-4.2.1/tests/test_health_genetics.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/view/gnuhealth_disease_gene.xml` & `gnuhealth_genetics-4.2.1/view/gnuhealth_disease_gene.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/view/gnuhealth_genetic_risk.xml` & `gnuhealth_genetics-4.2.1/view/gnuhealth_genetic_risk.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/view/gnuhealth_genetic_risk_tree.xml` & `gnuhealth_genetics-4.2.1/view/gnuhealth_genetic_risk_tree.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_genetics-4.2.0/view/gnuhealth_protein_disease.xml` & `gnuhealth_genetics-4.2.1/view/gnuhealth_protein_disease.xml`

 * *Files identical despite different names*

