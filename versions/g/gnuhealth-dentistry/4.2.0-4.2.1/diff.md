# Comparing `tmp/gnuhealth_dentistry-4.2.0.tar.gz` & `tmp/gnuhealth_dentistry-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_dentistry-4.2.0.tar", last modified: Sat Feb 11 21:55:23 2023, max compression
+gzip compressed data, was "gnuhealth_dentistry-4.2.1.tar", last modified: Fri Apr  7 10:17:26 2023, max compression
```

## Comparing `gnuhealth_dentistry-4.2.0.tar` & `gnuhealth_dentistry-4.2.1.tar`

### file list

```diff
@@ -1,55 +1,55 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.007084 gnuhealth_dentistry-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:47.000000 gnuhealth_dentistry-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5760 2023-02-11 21:55:23.006936 gnuhealth_dentistry-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1854 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.004149 gnuhealth_dentistry-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3075 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/data/dentistry_procedures.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.004215 gnuhealth_dentistry-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      251 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.006786 gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5760 2023-02-11 21:55:22.000000 gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1343 2023-02-11 21:55:22.000000 gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:22.000000 gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       70 2023-02-11 21:55:22.000000 gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:22.000000 gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       45 2023-02-11 21:55:22.000000 gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:55:22.000000 gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)    11242 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/health_dentistry.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1889 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/health_dentistry_report.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5720 2023-01-18 16:33:08.000000 gnuhealth_dentistry-4.2.0/health_dentistry_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.004547 gnuhealth_dentistry-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)   102069 2022-11-28 22:17:47.000000 gnuhealth_dentistry-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)   103478 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    94857 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/locale/zh_CN.po
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.005042 gnuhealth_dentistry-4.2.0/report/
--rwxr-xr-x   0 lfm       (1001) lfm       (1001)     1104 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/report/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)    50888 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/report/odontogram_report.fodt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6614 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/report/odontogram_report.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)    33930 2022-11-28 22:17:47.000000 gnuhealth_dentistry-4.2.0/report/odontogram_template.png
--rw-r--r--   0 lfm       (1001) lfm       (1001)    59631 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/report/procedures_report.fodt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2693 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/report/procedures_report.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.005109 gnuhealth_dentistry-4.2.0/security/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     7601 2023-01-18 16:33:08.000000 gnuhealth_dentistry-4.2.0/security/access_rights.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:55:23.007123 gnuhealth_dentistry-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3724 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.005257 gnuhealth_dentistry-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      379 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      604 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/tests/test_health_dentistry.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      244 2023-02-11 12:44:33.000000 gnuhealth_dentistry-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.005898 gnuhealth_dentistry-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      471 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_procedure_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      422 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_procedure_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1361 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_treatment_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      933 2023-01-18 16:33:08.000000 gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_treatment_procedure_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      608 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_treatment_procedure_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      528 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_treatment_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2612 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/view/gnuhealth_patient_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5093 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/view/load_procedure_start_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35823 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/view/set_odontogram_start_form.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:23.006302 gnuhealth_dentistry-4.2.0/wizard/
--rwxr-xr-x   0 lfm       (1001) lfm       (1001)     1106 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/wizard/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6383 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/wizard/load_procedure.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1020 2023-01-18 16:33:08.000000 gnuhealth_dentistry-4.2.0/wizard/load_procedure.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)    22790 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/wizard/patient_set_odontogram.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1015 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.0/wizard/patient_set_odontogram.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.609196 gnuhealth_dentistry-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:47.000000 gnuhealth_dentistry-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5760 2023-04-07 10:17:26.609018 gnuhealth_dentistry-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1854 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.606294 gnuhealth_dentistry-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3075 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/data/dentistry_procedures.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.606364 gnuhealth_dentistry-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      251 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.608886 gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5760 2023-04-07 10:17:26.000000 gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1343 2023-04-07 10:17:26.000000 gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:26.000000 gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       70 2023-04-07 10:17:26.000000 gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:26.000000 gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       45 2023-04-07 10:17:26.000000 gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:17:26.000000 gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)    11242 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/health_dentistry.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1889 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/health_dentistry_report.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5720 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/health_dentistry_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.606662 gnuhealth_dentistry-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)   102069 2022-11-28 22:17:47.000000 gnuhealth_dentistry-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)   103478 2023-01-18 16:33:07.000000 gnuhealth_dentistry-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    94857 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/locale/zh_CN.po
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.607186 gnuhealth_dentistry-4.2.1/report/
+-rwxr-xr-x   0 lfm       (1001) wheel        (0)     1104 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/report/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)    50888 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/report/odontogram_report.fodt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6614 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/report/odontogram_report.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)    33930 2022-11-28 22:17:47.000000 gnuhealth_dentistry-4.2.1/report/odontogram_template.png
+-rw-r--r--   0 lfm       (1001) wheel        (0)    59631 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/report/procedures_report.fodt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2693 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/report/procedures_report.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.607254 gnuhealth_dentistry-4.2.1/security/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     7601 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/security/access_rights.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:17:26.609229 gnuhealth_dentistry-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3724 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.607394 gnuhealth_dentistry-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      379 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      604 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/tests/test_health_dentistry.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      244 2023-04-07 09:37:21.000000 gnuhealth_dentistry-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.608040 gnuhealth_dentistry-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      471 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_procedure_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      422 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_procedure_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1361 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_treatment_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      933 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_treatment_procedure_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      608 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_treatment_procedure_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      528 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_treatment_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2612 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/view/gnuhealth_patient_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5093 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/view/load_procedure_start_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35823 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/view/set_odontogram_start_form.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:26.608432 gnuhealth_dentistry-4.2.1/wizard/
+-rwxr-xr-x   0 lfm       (1001) wheel        (0)     1106 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/wizard/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6383 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/wizard/load_procedure.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1020 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/wizard/load_procedure.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)    22790 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/wizard/patient_set_odontogram.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1015 2023-04-07 09:17:52.000000 gnuhealth_dentistry-4.2.1/wizard/patient_set_odontogram.xml
```

### Comparing `gnuhealth_dentistry-4.2.0/COPYING` & `gnuhealth_dentistry-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/PKG-INFO` & `gnuhealth_dentistry-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_dentistry
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health: Dentistry Package
 Home-page: https://www.gnuhealth_dentistry.org
 Download-URL: http://ftp.gnu.org/gnu/health_dentistry/
 Author: GNU Solidario
 Author-email: health_dentistry@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_dentistry-4.2.0/README.rst` & `gnuhealth_dentistry-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/__init__.py` & `gnuhealth_dentistry-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/data/dentistry_procedures.xml` & `gnuhealth_dentistry-4.2.1/data/dentistry_procedures.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/PKG-INFO` & `gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-dentistry
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health: Dentistry Package
 Home-page: https://www.gnuhealth_dentistry.org
 Download-URL: http://ftp.gnu.org/gnu/health_dentistry/
 Author: GNU Solidario
 Author-email: health_dentistry@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_dentistry-4.2.0/gnuhealth_dentistry.egg-info/SOURCES.txt` & `gnuhealth_dentistry-4.2.1/gnuhealth_dentistry.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/health_dentistry.py` & `gnuhealth_dentistry-4.2.1/health_dentistry.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/health_dentistry_report.xml` & `gnuhealth_dentistry-4.2.1/health_dentistry_report.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/health_dentistry_view.xml` & `gnuhealth_dentistry-4.2.1/health_dentistry_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/locale/es.po` & `gnuhealth_dentistry-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/locale/fr.po` & `gnuhealth_dentistry-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/locale/zh_CN.po` & `gnuhealth_dentistry-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/report/__init__.py` & `gnuhealth_dentistry-4.2.1/report/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/report/odontogram_report.fodt` & `gnuhealth_dentistry-4.2.1/report/odontogram_report.fodt`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/report/odontogram_report.py` & `gnuhealth_dentistry-4.2.1/report/odontogram_report.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/report/odontogram_template.png` & `gnuhealth_dentistry-4.2.1/report/odontogram_template.png`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/report/procedures_report.fodt` & `gnuhealth_dentistry-4.2.1/report/procedures_report.fodt`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/report/procedures_report.py` & `gnuhealth_dentistry-4.2.1/report/procedures_report.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/security/access_rights.xml` & `gnuhealth_dentistry-4.2.1/security/access_rights.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/setup.py` & `gnuhealth_dentistry-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/tests/test_health_dentistry.py` & `gnuhealth_dentistry-4.2.1/tests/test_health_dentistry.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_treatment_form.xml` & `gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_treatment_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_treatment_procedure_form.xml` & `gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_treatment_procedure_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_treatment_procedure_tree.xml` & `gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_treatment_procedure_tree.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/view/gnuhealth_dentistry_treatment_tree.xml` & `gnuhealth_dentistry-4.2.1/view/gnuhealth_dentistry_treatment_tree.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/view/gnuhealth_patient_form.xml` & `gnuhealth_dentistry-4.2.1/view/gnuhealth_patient_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/view/load_procedure_start_form.xml` & `gnuhealth_dentistry-4.2.1/view/load_procedure_start_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/view/set_odontogram_start_form.xml` & `gnuhealth_dentistry-4.2.1/view/set_odontogram_start_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/wizard/__init__.py` & `gnuhealth_dentistry-4.2.1/wizard/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/wizard/load_procedure.py` & `gnuhealth_dentistry-4.2.1/wizard/load_procedure.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/wizard/load_procedure.xml` & `gnuhealth_dentistry-4.2.1/wizard/load_procedure.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/wizard/patient_set_odontogram.py` & `gnuhealth_dentistry-4.2.1/wizard/patient_set_odontogram.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_dentistry-4.2.0/wizard/patient_set_odontogram.xml` & `gnuhealth_dentistry-4.2.1/wizard/patient_set_odontogram.xml`

 * *Files identical despite different names*

