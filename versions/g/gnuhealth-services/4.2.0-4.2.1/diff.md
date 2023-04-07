# Comparing `tmp/gnuhealth_services-4.2.0.tar.gz` & `tmp/gnuhealth_services-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_services-4.2.0.tar", last modified: Sat Feb 11 21:57:43 2023, max compression
+gzip compressed data, was "gnuhealth_services-4.2.1.tar", last modified: Fri Apr  7 10:19:42 2023, max compression
```

## Comparing `gnuhealth_services-4.2.0.tar` & `gnuhealth_services-4.2.1.tar`

### file list

```diff
@@ -1,67 +1,67 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.561162 gnuhealth_services-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5737 2023-02-11 21:57:43.560879 gnuhealth_services-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1455 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.557234 gnuhealth_services-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      632 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/data/gnuhealth_commands.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      811 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/data/health_service_sequences.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1269 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/data/health_services_data.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.557301 gnuhealth_services-4.2.0/data/messages/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1410 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/data/messages/messages.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.557369 gnuhealth_services-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      442 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/doc/index.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)      739 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/exceptions.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.559970 gnuhealth_services-4.2.0/gnuhealth_services.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5737 2023-02-11 21:57:43.000000 gnuhealth_services-4.2.0/gnuhealth_services.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2180 2023-02-11 21:57:43.000000 gnuhealth_services-4.2.0/gnuhealth_services.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:43.000000 gnuhealth_services-4.2.0/gnuhealth_services.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       68 2023-02-11 21:57:43.000000 gnuhealth_services-4.2.0/gnuhealth_services.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:43.000000 gnuhealth_services-4.2.0/gnuhealth_services.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       51 2023-02-11 21:57:43.000000 gnuhealth_services-4.2.0/gnuhealth_services.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:57:43.000000 gnuhealth_services-4.2.0/gnuhealth_services.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     8976 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/health_services.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      999 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/health_services_report.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     8029 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/health_services_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.557501 gnuhealth_services-4.2.0/icons/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2088 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.0/icons/folder-documents.svg
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10595 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.0/icons/tryton-financial.svg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1503 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/invoice.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      936 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/invoice.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.558232 gnuhealth_services-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     7297 2023-02-11 12:36:12.000000 gnuhealth_services-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6808 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6808 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6548 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6741 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6861 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6740 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5414 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6374 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    11119 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/locale/zh_CN.po
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.558304 gnuhealth_services-4.2.0/report/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    66034 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/report/health_services_report.fodt
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.558422 gnuhealth_services-4.2.0/security/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6421 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/security/access_rights.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2390 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/sequences.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:57:43.561216 gnuhealth_services-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3720 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.558575 gnuhealth_services-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      235 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      600 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/tests/test_health_services.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      355 2023-02-11 12:44:33.000000 gnuhealth_services-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.559192 gnuhealth_services-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      945 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/view/gnuhealth_health_service.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      809 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/view/gnuhealth_health_service_line.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      566 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/view/gnuhealth_health_service_line_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      427 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/view/gnuhealth_health_service_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      825 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/view/gnuhealth_patient_evaluation.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      672 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/view/gnuhealth_prescription.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      444 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/view/health_service_invoice.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      798 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/view/invoice_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      508 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/view/invoice_tree.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:43.559408 gnuhealth_services-4.2.0/wizard/
--rwxr-xr-x   0 lfm       (1001) lfm       (1001)      364 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/wizard/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1159 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/wizard/create_health_service_invoice.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6572 2023-01-18 16:33:08.000000 gnuhealth_services-4.2.0/wizard/wizard_health_services.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.792858 gnuhealth_services-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5737 2023-04-07 10:19:42.792724 gnuhealth_services-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1455 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.789664 gnuhealth_services-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      632 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/data/gnuhealth_commands.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      811 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/data/health_service_sequences.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1269 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/data/health_services_data.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.789732 gnuhealth_services-4.2.1/data/messages/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1410 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/data/messages/messages.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.789801 gnuhealth_services-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      442 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/doc/index.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)      739 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/exceptions.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.792196 gnuhealth_services-4.2.1/gnuhealth_services.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5737 2023-04-07 10:19:42.000000 gnuhealth_services-4.2.1/gnuhealth_services.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2180 2023-04-07 10:19:42.000000 gnuhealth_services-4.2.1/gnuhealth_services.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:42.000000 gnuhealth_services-4.2.1/gnuhealth_services.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       68 2023-04-07 10:19:42.000000 gnuhealth_services-4.2.1/gnuhealth_services.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:42.000000 gnuhealth_services-4.2.1/gnuhealth_services.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       51 2023-04-07 10:19:42.000000 gnuhealth_services-4.2.1/gnuhealth_services.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:19:42.000000 gnuhealth_services-4.2.1/gnuhealth_services.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     8976 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/health_services.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      999 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/health_services_report.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     8029 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/health_services_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.789936 gnuhealth_services-4.2.1/icons/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2088 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.1/icons/folder-documents.svg
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10595 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.1/icons/tryton-financial.svg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1503 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/invoice.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      936 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/invoice.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.790622 gnuhealth_services-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     7297 2023-02-11 12:36:12.000000 gnuhealth_services-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6808 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6808 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6548 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6741 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6861 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6740 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5414 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6374 2022-11-28 22:17:48.000000 gnuhealth_services-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    11119 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/locale/zh_CN.po
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.790688 gnuhealth_services-4.2.1/report/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    66034 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/report/health_services_report.fodt
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.790784 gnuhealth_services-4.2.1/security/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6421 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/security/access_rights.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2390 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/sequences.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:19:42.792892 gnuhealth_services-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3720 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.790914 gnuhealth_services-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      235 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      600 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/tests/test_health_services.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      355 2023-04-07 09:37:21.000000 gnuhealth_services-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.791477 gnuhealth_services-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      945 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/view/gnuhealth_health_service.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      809 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/view/gnuhealth_health_service_line.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      566 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/view/gnuhealth_health_service_line_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      427 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/view/gnuhealth_health_service_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      825 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/view/gnuhealth_patient_evaluation.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      672 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/view/gnuhealth_prescription.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      444 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/view/health_service_invoice.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      798 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/view/invoice_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      508 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/view/invoice_tree.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:42.791678 gnuhealth_services-4.2.1/wizard/
+-rwxr-xr-x   0 lfm       (1001) wheel        (0)      364 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/wizard/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1159 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/wizard/create_health_service_invoice.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6572 2023-04-07 09:17:52.000000 gnuhealth_services-4.2.1/wizard/wizard_health_services.py
```

### Comparing `gnuhealth_services-4.2.0/COPYING` & `gnuhealth_services-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/PKG-INFO` & `gnuhealth_services-4.2.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_services
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package to manage patient health related services
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_services-4.2.0/README.rst` & `gnuhealth_services-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/__init__.py` & `gnuhealth_services-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/data/gnuhealth_commands.xml` & `gnuhealth_services-4.2.1/data/gnuhealth_commands.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/data/health_service_sequences.xml` & `gnuhealth_services-4.2.1/data/health_service_sequences.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/data/health_services_data.xml` & `gnuhealth_services-4.2.1/data/health_services_data.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/data/messages/messages.xml` & `gnuhealth_services-4.2.1/data/messages/messages.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/exceptions.py` & `gnuhealth_services-4.2.1/exceptions.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/gnuhealth_services.egg-info/PKG-INFO` & `gnuhealth_services-4.2.1/gnuhealth_services.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-services
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health package to manage patient health related services
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_services-4.2.0/gnuhealth_services.egg-info/SOURCES.txt` & `gnuhealth_services-4.2.1/gnuhealth_services.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/health_services.py` & `gnuhealth_services-4.2.1/health_services.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/health_services_report.xml` & `gnuhealth_services-4.2.1/health_services_report.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/health_services_view.xml` & `gnuhealth_services-4.2.1/health_services_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/icons/folder-documents.svg` & `gnuhealth_services-4.2.1/icons/folder-documents.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/icons/tryton-financial.svg` & `gnuhealth_services-4.2.1/icons/tryton-financial.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/invoice.py` & `gnuhealth_services-4.2.1/invoice.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/invoice.xml` & `gnuhealth_services-4.2.1/invoice.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/ar.po` & `gnuhealth_services-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/de.po` & `gnuhealth_services-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/el.po` & `gnuhealth_services-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/es.po` & `gnuhealth_services-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/fr.po` & `gnuhealth_services-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/it_IT.po` & `gnuhealth_services-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/ja_JP.po` & `gnuhealth_services-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/lo.po` & `gnuhealth_services-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/pt_BR.po` & `gnuhealth_services-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/locale/zh_CN.po` & `gnuhealth_services-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/report/health_services_report.fodt` & `gnuhealth_services-4.2.1/report/health_services_report.fodt`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/security/access_rights.xml` & `gnuhealth_services-4.2.1/security/access_rights.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/sequences.py` & `gnuhealth_services-4.2.1/sequences.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/setup.py` & `gnuhealth_services-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/tests/test_health_services.py` & `gnuhealth_services-4.2.1/tests/test_health_services.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/view/gnuhealth_health_service.xml` & `gnuhealth_services-4.2.1/view/gnuhealth_health_service.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/view/gnuhealth_health_service_line.xml` & `gnuhealth_services-4.2.1/view/gnuhealth_health_service_line.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/view/gnuhealth_health_service_line_tree.xml` & `gnuhealth_services-4.2.1/view/gnuhealth_health_service_line_tree.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/view/gnuhealth_patient_evaluation.xml` & `gnuhealth_services-4.2.1/view/gnuhealth_patient_evaluation.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/view/gnuhealth_prescription.xml` & `gnuhealth_services-4.2.1/view/gnuhealth_prescription.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/view/invoice_form.xml` & `gnuhealth_services-4.2.1/view/invoice_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/wizard/create_health_service_invoice.xml` & `gnuhealth_services-4.2.1/wizard/create_health_service_invoice.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_services-4.2.0/wizard/wizard_health_services.py` & `gnuhealth_services-4.2.1/wizard/wizard_health_services.py`

 * *Files identical despite different names*

