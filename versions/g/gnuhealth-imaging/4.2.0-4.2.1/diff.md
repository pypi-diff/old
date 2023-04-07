# Comparing `tmp/gnuhealth_imaging-4.2.0.tar.gz` & `tmp/gnuhealth_imaging-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_imaging-4.2.0.tar", last modified: Sat Feb 11 21:56:33 2023, max compression
+gzip compressed data, was "gnuhealth_imaging-4.2.1.tar", last modified: Fri Apr  7 10:18:33 2023, max compression
```

## Comparing `gnuhealth_imaging-4.2.0.tar` & `gnuhealth_imaging-4.2.1.tar`

### file list

```diff
@@ -1,61 +1,61 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.160918 gnuhealth_imaging-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5724 2023-02-11 21:56:33.160748 gnuhealth_imaging-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/README.rst
--rwxr-xr-x   0 lfm       (1001) lfm       (1001)     1485 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.157555 gnuhealth_imaging-4.2.0/data/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      643 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/data/gnuhealth_commands.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1312 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/data/health_imaging_sequences.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5211 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/data/imaging_data.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.157626 gnuhealth_imaging-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      312 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.160177 gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5724 2023-02-11 21:56:33.000000 gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1941 2023-02-11 21:56:33.000000 gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:33.000000 gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       66 2023-02-11 21:56:33.000000 gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:56:33.000000 gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       17 2023-02-11 21:56:33.000000 gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:56:33.000000 gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     7926 2023-01-24 11:03:05.000000 gnuhealth_imaging-4.2.0/health_imaging.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      990 2023-01-24 10:35:21.000000 gnuhealth_imaging-4.2.0/health_imaging_report.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10231 2023-01-24 20:00:02.000000 gnuhealth_imaging-4.2.0/health_imaging_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.157763 gnuhealth_imaging-4.2.0/icons/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5225 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.0/icons/execute_icon.svg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     7169 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.0/icons/imaging_icon.svg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.158475 gnuhealth_imaging-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    11328 2023-02-11 12:36:12.000000 gnuhealth_imaging-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10777 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    12370 2022-11-28 22:17:47.000000 gnuhealth_imaging-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10799 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10591 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10489 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    11466 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     8914 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     9760 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10183 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/locale/zh_CN.po
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.158543 gnuhealth_imaging-4.2.0/report/
--rw-r--r--   0 lfm       (1001) lfm       (1001)   141531 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/report/imaging_study_report.fodt
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.158685 gnuhealth_imaging-4.2.0/security/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    10196 2023-01-23 19:10:14.000000 gnuhealth_imaging-4.2.0/security/access_rights.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3776 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/sequences.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:56:33.160959 gnuhealth_imaging-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3651 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.158819 gnuhealth_imaging-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      234 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      596 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/tests/test_health_imaging.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      233 2023-02-11 12:44:33.000000 gnuhealth_imaging-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.159450 gnuhealth_imaging-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      599 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/view/imaging_test_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1024 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/view/imaging_test_request_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      506 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/view/imaging_test_request_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1065 2023-02-01 13:11:33.000000 gnuhealth_imaging-4.2.0/view/imaging_test_result_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      464 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/view/imaging_test_result_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      394 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/view/imaging_test_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      335 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/view/imaging_test_type_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      285 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/view/imaging_test_type_tree.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      577 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/view/patient_imaging_test_request_start_form.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:56:33.159589 gnuhealth_imaging-4.2.0/wizard/
--rwxr-xr-x   0 lfm       (1001) lfm       (1001)      363 2023-01-18 16:33:08.000000 gnuhealth_imaging-4.2.0/wizard/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4920 2023-01-24 10:51:41.000000 gnuhealth_imaging-4.2.0/wizard/wizard_health_imaging.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.665198 gnuhealth_imaging-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5724 2023-04-07 10:18:33.665062 gnuhealth_imaging-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/README.rst
+-rwxr-xr-x   0 lfm       (1001) wheel        (0)     1485 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.662155 gnuhealth_imaging-4.2.1/data/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      643 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/data/gnuhealth_commands.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1312 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/data/health_imaging_sequences.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5211 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/data/imaging_data.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.662221 gnuhealth_imaging-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      312 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.664547 gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5724 2023-04-07 10:18:33.000000 gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1941 2023-04-07 10:18:33.000000 gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:18:33.000000 gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       66 2023-04-07 10:18:33.000000 gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:18:33.000000 gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       17 2023-04-07 10:18:33.000000 gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:18:33.000000 gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     7926 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/health_imaging.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      990 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/health_imaging_report.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10231 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/health_imaging_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.662345 gnuhealth_imaging-4.2.1/icons/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5225 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.1/icons/execute_icon.svg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     7169 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.1/icons/imaging_icon.svg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.662993 gnuhealth_imaging-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    11328 2023-02-11 12:36:12.000000 gnuhealth_imaging-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10777 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    12370 2022-11-28 22:17:47.000000 gnuhealth_imaging-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10799 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10591 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10489 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    11466 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     8914 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     9760 2022-11-28 22:17:48.000000 gnuhealth_imaging-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10183 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/locale/zh_CN.po
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.663074 gnuhealth_imaging-4.2.1/report/
+-rw-r--r--   0 lfm       (1001) wheel        (0)   151092 2023-04-07 09:20:43.000000 gnuhealth_imaging-4.2.1/report/imaging_study_report.fodt
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.663212 gnuhealth_imaging-4.2.1/security/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    10196 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/security/access_rights.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3776 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/sequences.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:18:33.665233 gnuhealth_imaging-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3651 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.663343 gnuhealth_imaging-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      234 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      596 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/tests/test_health_imaging.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      233 2023-04-07 09:37:21.000000 gnuhealth_imaging-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.663919 gnuhealth_imaging-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      599 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/view/imaging_test_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1024 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/view/imaging_test_request_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      506 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/view/imaging_test_request_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1065 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/view/imaging_test_result_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      464 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/view/imaging_test_result_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      394 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/view/imaging_test_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      335 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/view/imaging_test_type_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      285 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/view/imaging_test_type_tree.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      577 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/view/patient_imaging_test_request_start_form.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:18:33.664047 gnuhealth_imaging-4.2.1/wizard/
+-rwxr-xr-x   0 lfm       (1001) wheel        (0)      363 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/wizard/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4920 2023-04-07 09:17:52.000000 gnuhealth_imaging-4.2.1/wizard/wizard_health_imaging.py
```

### Comparing `gnuhealth_imaging-4.2.0/COPYING` & `gnuhealth_imaging-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/PKG-INFO` & `gnuhealth_imaging-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_imaging
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Diagnostic Imaging management package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_imaging-4.2.0/README.rst` & `gnuhealth_imaging-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/__init__.py` & `gnuhealth_imaging-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/data/gnuhealth_commands.xml` & `gnuhealth_imaging-4.2.1/data/gnuhealth_commands.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/data/health_imaging_sequences.xml` & `gnuhealth_imaging-4.2.1/data/health_imaging_sequences.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/data/imaging_data.xml` & `gnuhealth_imaging-4.2.1/data/imaging_data.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/PKG-INFO` & `gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-imaging
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health Diagnostic Imaging management package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_imaging-4.2.0/gnuhealth_imaging.egg-info/SOURCES.txt` & `gnuhealth_imaging-4.2.1/gnuhealth_imaging.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/health_imaging.py` & `gnuhealth_imaging-4.2.1/health_imaging.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/health_imaging_report.xml` & `gnuhealth_imaging-4.2.1/health_imaging_report.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/health_imaging_view.xml` & `gnuhealth_imaging-4.2.1/health_imaging_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/icons/execute_icon.svg` & `gnuhealth_imaging-4.2.1/icons/execute_icon.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/icons/imaging_icon.svg` & `gnuhealth_imaging-4.2.1/icons/imaging_icon.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/ar.po` & `gnuhealth_imaging-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/de.po` & `gnuhealth_imaging-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/el.po` & `gnuhealth_imaging-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/es.po` & `gnuhealth_imaging-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/fr.po` & `gnuhealth_imaging-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/it_IT.po` & `gnuhealth_imaging-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/ja_JP.po` & `gnuhealth_imaging-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/lo.po` & `gnuhealth_imaging-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/pt_BR.po` & `gnuhealth_imaging-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/locale/zh_CN.po` & `gnuhealth_imaging-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/report/imaging_study_report.fodt` & `gnuhealth_imaging-4.2.1/report/imaging_study_report.fodt`

 * *Files 2% similar despite different names*

#### Comparing `gnuhealth_imaging-4.2.0/report/imaging_study_report.fodt` & `gnuhealth_imaging-4.2.1/report/imaging_study_report.fodt`

```diff
@@ -1,35 +1,35 @@
 <?xml version="1.0" encoding="utf-8"?>
 <office:document xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" office:version="1.3" office:mimetype="application/vnd.oasis.opendocument.text">
   <office:meta>
     <meta:initial-creator>lfm</meta:initial-creator>
     <meta:creation-date>2011-06-15T19:12:18</meta:creation-date>
-    <dc:date>2023-01-15T20:12:48.488565049</dc:date>
-    <meta:editing-duration>P11DT14H1M50S</meta:editing-duration>
-    <meta:editing-cycles>453</meta:editing-cycles>
-    <meta:generator>LibreOffice/7.4.2.3$FreeBSD_X86_64 LibreOffice_project/40$Build-3</meta:generator>
-    <meta:document-statistic meta:table-count="3" meta:image-count="0" meta:object-count="0" meta:page-count="1" meta:paragraph-count="40" meta:word-count="90" meta:character-count="1195" meta:non-whitespace-character-count="1136"/>
+    <dc:date>2023-04-06T19:13:46.706099882</dc:date>
+    <meta:editing-duration>P12DT15H54M19S</meta:editing-duration>
+    <meta:editing-cycles>486</meta:editing-cycles>
+    <meta:generator>LibreOffice/7.4.4.2$FreeBSD_X86_64 LibreOffice_project/40$Build-2</meta:generator>
+    <meta:document-statistic meta:table-count="3" meta:image-count="0" meta:object-count="0" meta:page-count="1" meta:paragraph-count="37" meta:word-count="105" meta:character-count="1389" meta:non-whitespace-character-count="1311"/>
   </office:meta>
   <office:settings>
     <config:config-item-set config:name="ooo:view-settings">
-      <config:config-item config:name="ViewAreaTop" config:type="long">6676</config:config-item>
+      <config:config-item config:name="ViewAreaTop" config:type="long">0</config:config-item>
       <config:config-item config:name="ViewAreaLeft" config:type="long">0</config:config-item>
-      <config:config-item config:name="ViewAreaWidth" config:type="long">23047</config:config-item>
-      <config:config-item config:name="ViewAreaHeight" config:type="long">10003</config:config-item>
+      <config:config-item config:name="ViewAreaWidth" config:type="long">27201</config:config-item>
+      <config:config-item config:name="ViewAreaHeight" config:type="long">8389</config:config-item>
       <config:config-item config:name="ShowRedlineChanges" config:type="boolean">true</config:config-item>
       <config:config-item config:name="InBrowseMode" config:type="boolean">false</config:config-item>
       <config:config-item-map-indexed config:name="Views">
         <config:config-item-map-entry>
           <config:config-item config:name="ViewId" config:type="string">view2</config:config-item>
-          <config:config-item config:name="ViewLeft" config:type="long">3561</config:config-item>
-          <config:config-item config:name="ViewTop" config:type="long">13637</config:config-item>
+          <config:config-item config:name="ViewLeft" config:type="long">18870</config:config-item>
+          <config:config-item config:name="ViewTop" config:type="long">7740</config:config-item>
           <config:config-item config:name="VisibleLeft" config:type="long">0</config:config-item>
-          <config:config-item config:name="VisibleTop" config:type="long">6676</config:config-item>
-          <config:config-item config:name="VisibleRight" config:type="long">23045</config:config-item>
-          <config:config-item config:name="VisibleBottom" config:type="long">16678</config:config-item>
+          <config:config-item config:name="VisibleTop" config:type="long">0</config:config-item>
+          <config:config-item config:name="VisibleRight" config:type="long">27199</config:config-item>
+          <config:config-item config:name="VisibleBottom" config:type="long">8387</config:config-item>
           <config:config-item config:name="ZoomType" config:type="short">0</config:config-item>
           <config:config-item config:name="ViewLayoutColumns" config:type="short">1</config:config-item>
           <config:config-item config:name="ViewLayoutBookMode" config:type="boolean">false</config:config-item>
           <config:config-item config:name="ZoomFactor" config:type="short">200</config:config-item>
           <config:config-item config:name="IsSelectedFrame" config:type="boolean">false</config:config-item>
           <config:config-item config:name="KeepRatio" config:type="boolean">false</config:config-item>
           <config:config-item config:name="HideWhitespace" config:type="boolean">false</config:config-item>
@@ -52,15 +52,15 @@
       <config:config-item config:name="TabsRelativeToIndent" config:type="boolean">true</config:config-item>
       <config:config-item config:name="RedlineProtectionKey" config:type="base64Binary"/>
       <config:config-item config:name="PrintTextPlaceholder" config:type="boolean">false</config:config-item>
       <config:config-item config:name="PrintControls" config:type="boolean">true</config:config-item>
       <config:config-item config:name="SaveThumbnail" config:type="boolean">true</config:config-item>
       <config:config-item config:name="EmbedFonts" config:type="boolean">false</config:config-item>
       <config:config-item config:name="AutoFirstLineIndentDisregardLineSpace" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="Rsid" config:type="int">13938163</config:config-item>
+      <config:config-item config:name="Rsid" config:type="int">14336304</config:config-item>
       <config:config-item config:name="GutterAtTop" config:type="boolean">false</config:config-item>
       <config:config-item config:name="AddFrameOffsets" config:type="boolean">false</config:config-item>
       <config:config-item config:name="FrameAutowidthWithMorePara" config:type="boolean">false</config:config-item>
       <config:config-item config:name="MathBaselineAlignment" config:type="boolean">false</config:config-item>
       <config:config-item config:name="ProtectBookmarks" config:type="boolean">false</config:config-item>
       <config:config-item config:name="IgnoreTabsAndBlanksForLineCalculation" config:type="boolean">false</config:config-item>
       <config:config-item config:name="ContinuousEndnotes" config:type="boolean">false</config:config-item>
@@ -363,65 +363,69 @@
       </style:table-cell-properties>
     </style:style>
     <style:style style:name="Tabla1.C2" style:family="table-cell">
       <style:table-cell-properties fo:background-color="#eeeeee" fo:padding="0.0382in" fo:border-left="0.05pt solid #000000" fo:border-right="0.05pt solid #000000" fo:border-top="none" fo:border-bottom="0.05pt solid #000000">
         <style:background-image/>
       </style:table-cell-properties>
     </style:style>
+    <style:style style:name="Tabla1.3" style:family="table-row">
+      <style:table-row-properties style:min-row-height="0.6493in"/>
+    </style:style>
     <style:style style:name="Table1" style:family="table">
       <style:table-properties style:width="6.6354in" table:align="right"/>
     </style:style>
     <style:style style:name="Table1.A" style:family="table-column">
       <style:table-column-properties style:column-width="6.6354in"/>
     </style:style>
     <style:style style:name="Table1.A1" style:family="table-cell">
       <style:table-cell-properties fo:padding="0.0382in" fo:border="0.05pt solid #000000"/>
     </style:style>
-    <style:style style:name="Table2" style:family="table">
+    <style:style style:name="Tabla2" style:family="table">
       <style:table-properties style:width="6.6757in" table:align="right"/>
     </style:style>
-    <style:style style:name="Table2.A" style:family="table-column">
+    <style:style style:name="Tabla2.A" style:family="table-column">
       <style:table-column-properties style:column-width="3.2139in"/>
     </style:style>
-    <style:style style:name="Table2.B" style:family="table-column">
+    <style:style style:name="Tabla2.B" style:family="table-column">
       <style:table-column-properties style:column-width="3.4618in"/>
     </style:style>
-    <style:style style:name="Table2.1" style:family="table-row">
+    <style:style style:name="Tabla2.1" style:family="table-row">
       <style:table-row-properties style:min-row-height="0.3493in"/>
     </style:style>
-    <style:style style:name="Table2.A1" style:family="table-cell">
+    <style:style style:name="Tabla2.A1" style:family="table-cell">
       <style:table-cell-properties fo:padding="0.0382in" fo:border-left="0.5pt solid #000000" fo:border-right="none" fo:border-top="0.5pt solid #000000" fo:border-bottom="0.5pt solid #000000"/>
     </style:style>
-    <style:style style:name="Table2.B1" style:family="table-cell">
+    <style:style style:name="Tabla2.B1" style:family="table-cell">
       <style:table-cell-properties style:vertical-align="middle" fo:padding="0.0382in" fo:border-left="none" fo:border-right="0.5pt solid #000000" fo:border-top="0.5pt solid #000000" fo:border-bottom="0.5pt solid #000000"/>
     </style:style>
     <style:style style:name="P1" style:family="paragraph" style:parent-style-name="Header">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
-      <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
+      <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
     <style:style style:name="P2" style:family="paragraph" style:parent-style-name="Header">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" officeooo:paragraph-rsid="001b7e2b" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
     <style:style style:name="P3" style:family="paragraph" style:parent-style-name="Footer">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" officeooo:paragraph-rsid="001b7e2b" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
     <style:style style:name="P4" style:family="paragraph" style:parent-style-name="Header">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
-      <style:text-properties style:font-name="FreeSans" fo:font-size="12pt" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
+      <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
-    <style:style style:name="P5" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:text-properties style:font-name="FreeSans" fo:font-size="12pt" officeooo:rsid="00bcd6d3" officeooo:paragraph-rsid="00bcd6d3" fo:background-color="#dddddd" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
+    <style:style style:name="P5" style:family="paragraph" style:parent-style-name="Header">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
     <style:style style:name="P6" style:family="paragraph" style:parent-style-name="Header">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" officeooo:paragraph-rsid="0019dc12" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
     <style:style style:name="P7" style:family="paragraph" style:parent-style-name="Header">
-      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" officeooo:paragraph-rsid="0019dc12" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
     <style:style style:name="P8" style:family="paragraph" style:parent-style-name="Header">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
     <style:style style:name="P9" style:family="paragraph" style:parent-style-name="Footer">
@@ -433,628 +437,676 @@
     </style:style>
     <style:style style:name="P11" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" fo:font-style="normal" officeooo:rsid="00c47104" officeooo:paragraph-rsid="00c47104" fo:background-color="#dddddd" style:font-size-asian="9pt" style:font-style-asian="normal" style:font-size-complex="9pt" style:font-style-complex="normal"/>
     </style:style>
     <style:style style:name="P12" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" fo:font-style="normal" style:font-size-asian="9pt" style:font-style-asian="normal" style:font-size-complex="9pt" style:font-style-complex="normal"/>
     </style:style>
-    <style:style style:name="P13" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P13" style:family="paragraph" style:parent-style-name="Header">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties style:font-name="FreeSans" fo:font-size="12pt" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
+    </style:style>
+    <style:style style:name="P14" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:text-properties style:font-name="FreeSans" fo:font-size="12pt" officeooo:rsid="00bcd6d3" officeooo:paragraph-rsid="00bcd6d3" fo:background-color="#dddddd" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
+    </style:style>
+    <style:style style:name="P15" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="FreeSans"/>
     </style:style>
-    <style:style style:name="P14" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P16" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P15" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P17" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" officeooo:paragraph-rsid="00c5a6fa" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P16" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P18" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" officeooo:paragraph-rsid="00c47104" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P17" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P19" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P18" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P20" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" officeooo:rsid="00a0e670" officeooo:paragraph-rsid="00a0e670" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P19" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P21" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" officeooo:rsid="00a0e670" officeooo:paragraph-rsid="00a0e670" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P20" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P22" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" officeooo:rsid="00a1cdd8" officeooo:paragraph-rsid="00a1cdd8" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P21" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P23" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" fo:font-style="italic" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" officeooo:paragraph-rsid="00c47104" fo:background-color="#dddddd" style:font-size-asian="10pt" style:font-style-asian="italic" style:font-size-complex="10pt" style:font-style-complex="italic"/>
     </style:style>
-    <style:style style:name="P22" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P24" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" fo:font-style="italic" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" officeooo:paragraph-rsid="00c2734f" fo:background-color="#dddddd" style:font-size-asian="10pt" style:font-style-asian="italic" style:font-size-complex="10pt" style:font-style-complex="italic"/>
     </style:style>
-    <style:style style:name="P23" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P25" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="00a1cdd8" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P24" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P26" style:family="paragraph" style:parent-style-name="Standard">
+      <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P27" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="FreeSans" fo:font-size="8pt" fo:font-style="normal" style:font-size-asian="8pt" style:font-style-asian="normal" style:font-size-complex="8pt" style:font-style-complex="normal"/>
     </style:style>
-    <style:style style:name="P25" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P28" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="FreeSans" fo:font-size="8pt" style:font-size-asian="8pt" style:font-size-complex="8pt"/>
     </style:style>
-    <style:style style:name="P26" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P29" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties style:font-name="FreeSans" fo:font-size="8pt" style:font-size-asian="8pt" style:font-size-complex="8pt"/>
     </style:style>
-    <style:style style:name="P27" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P30" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="FreeSans" fo:font-weight="bold" officeooo:paragraph-rsid="00b41c6c" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P28" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P31" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="00a5f256"/>
     </style:style>
-    <style:style style:name="P29" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P32" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="00a5f256"/>
     </style:style>
-    <style:style style:name="P30" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P33" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="FreeSans" fo:font-size="11pt" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00a5f256" style:font-size-asian="11pt" style:font-weight-asian="bold" style:font-size-complex="11pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P31" style:family="paragraph" style:parent-style-name="Heading_20_1">
+    <style:style style:name="P34" style:family="paragraph" style:parent-style-name="Heading_20_1">
       <style:text-properties style:font-name="FreeSans"/>
     </style:style>
-    <style:style style:name="P32" style:family="paragraph" style:parent-style-name="Heading_20_1">
+    <style:style style:name="P35" style:family="paragraph" style:parent-style-name="Heading_20_1">
       <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="009f72f6"/>
     </style:style>
-    <style:style style:name="P33" style:family="paragraph" style:parent-style-name="Heading_20_1">
+    <style:style style:name="P36" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="009f72f6"/>
+    </style:style>
+    <style:style style:name="P37" style:family="paragraph" style:parent-style-name="Heading_20_1">
       <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="00c2734f"/>
     </style:style>
-    <style:style style:name="P34" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P38" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties style:font-name="FreeSans"/>
     </style:style>
-    <style:style style:name="P35" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P39" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="00b6b21a"/>
     </style:style>
-    <style:style style:name="P36" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P40" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="00bcd6d3"/>
     </style:style>
-    <style:style style:name="P37" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P41" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="0085d769"/>
     </style:style>
-    <style:style style:name="P38" style:family="paragraph" style:parent-style-name="Header">
+    <style:style style:name="P42" style:family="paragraph" style:parent-style-name="Preformatted_20_Text" style:master-page-name="">
+      <loext:graphic-properties draw:fill="none"/>
+      <style:paragraph-properties fo:margin-left="0.25in" fo:margin-right="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:contextual-spacing="false" fo:text-indent="0in" style:auto-text-indent="false" style:page-number="auto" fo:background-color="transparent"/>
+      <style:text-properties style:font-name="FreeSans" officeooo:rsid="00d4adf3" officeooo:paragraph-rsid="00d4adf3"/>
+    </style:style>
+    <style:style style:name="P43" style:family="paragraph" style:parent-style-name="Standard" style:master-page-name="">
+      <loext:graphic-properties draw:fill="none"/>
+      <style:paragraph-properties fo:margin-left="0.25in" fo:margin-right="0in" fo:text-indent="0in" style:auto-text-indent="false" style:page-number="auto" fo:background-color="transparent"/>
+      <style:text-properties style:font-name="FreeSans"/>
+    </style:style>
+    <style:style style:name="P44" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="00d4adf3"/>
+    </style:style>
+    <style:style style:name="P45" style:family="paragraph" style:parent-style-name="Header">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" officeooo:paragraph-rsid="001b7e2b" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
-    <style:style style:name="P39" style:family="paragraph" style:parent-style-name="Footer">
+    <style:style style:name="P46" style:family="paragraph" style:parent-style-name="Footer">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" officeooo:paragraph-rsid="001b7e2b" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
-    <style:style style:name="P40" style:family="paragraph" style:parent-style-name="Header">
+    <style:style style:name="P47" style:family="paragraph" style:parent-style-name="Header">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
-    <style:style style:name="P41" style:family="paragraph" style:parent-style-name="Footer">
+    <style:style style:name="P48" style:family="paragraph" style:parent-style-name="Footer">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
-    <style:style style:name="P42" style:family="paragraph" style:parent-style-name="Header">
+    <style:style style:name="P49" style:family="paragraph" style:parent-style-name="Header">
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" officeooo:paragraph-rsid="0019dc12" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
-    <style:style style:name="P43" style:family="paragraph" style:parent-style-name="Header">
+    <style:style style:name="P50" style:family="paragraph" style:parent-style-name="Header">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" officeooo:paragraph-rsid="0019dc12" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
-    <style:style style:name="P44" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P51" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
     </style:style>
-    <style:style style:name="P45" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P52" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" fo:font-style="normal" style:font-size-asian="9pt" style:font-style-asian="normal" style:font-size-complex="9pt" style:font-style-complex="normal"/>
     </style:style>
-    <style:style style:name="P46" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P53" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="Cantarell" fo:font-size="9pt" fo:font-style="normal" officeooo:rsid="00c47104" officeooo:paragraph-rsid="00c47104" fo:background-color="#dddddd" style:font-size-asian="9pt" style:font-style-asian="normal" style:font-size-complex="9pt" style:font-style-complex="normal"/>
     </style:style>
-    <style:style style:name="P47" style:family="paragraph" style:parent-style-name="Header">
+    <style:style style:name="P54" style:family="paragraph" style:parent-style-name="Header">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="12pt" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
     </style:style>
-    <style:style style:name="P48" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P55" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties style:font-name="Cantarell" fo:font-size="12pt" officeooo:rsid="00bcd6d3" officeooo:paragraph-rsid="00bcd6d3" fo:background-color="#dddddd" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
     </style:style>
-    <style:style style:name="P49" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P56" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="Cantarell"/>
     </style:style>
-    <style:style style:name="P50" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P57" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P51" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P58" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" officeooo:paragraph-rsid="00c47104" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P52" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P59" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" officeooo:paragraph-rsid="00c5a6fa" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P53" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P60" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P54" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P61" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" officeooo:rsid="00a0e670" officeooo:paragraph-rsid="00a0e670" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P55" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P62" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" officeooo:rsid="00a0e670" officeooo:paragraph-rsid="00a0e670" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P56" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P63" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" officeooo:rsid="00a1cdd8" officeooo:paragraph-rsid="00a1cdd8" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P57" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P64" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" fo:font-style="italic" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" officeooo:paragraph-rsid="00c47104" fo:background-color="#dddddd" style:font-size-asian="10pt" style:font-style-asian="italic" style:font-size-complex="10pt" style:font-style-complex="italic"/>
     </style:style>
-    <style:style style:name="P58" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P65" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" fo:font-style="italic" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" officeooo:paragraph-rsid="00c2734f" fo:background-color="#dddddd" style:font-size-asian="10pt" style:font-style-asian="italic" style:font-size-complex="10pt" style:font-style-complex="italic"/>
     </style:style>
-    <style:style style:name="P59" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P66" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="00a1cdd8" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P60" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P67" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="Cantarell" fo:font-size="8pt" fo:font-style="normal" style:font-size-asian="8pt" style:font-style-asian="normal" style:font-size-complex="8pt" style:font-style-complex="normal"/>
     </style:style>
-    <style:style style:name="P61" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P68" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="Cantarell" fo:font-size="8pt" style:font-size-asian="8pt" style:font-size-complex="8pt"/>
     </style:style>
-    <style:style style:name="P62" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P69" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="Cantarell" fo:font-weight="bold" officeooo:paragraph-rsid="00b41c6c" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P63" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P70" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="Cantarell" officeooo:paragraph-rsid="00a5f256"/>
     </style:style>
-    <style:style style:name="P64" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P71" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties style:font-name="Cantarell" fo:font-size="11pt" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00a5f256" style:font-size-asian="11pt" style:font-weight-asian="bold" style:font-size-complex="11pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P65" style:family="paragraph" style:parent-style-name="Heading_20_1">
+    <style:style style:name="P72" style:family="paragraph" style:parent-style-name="Heading_20_1">
       <style:text-properties style:font-name="Cantarell"/>
     </style:style>
-    <style:style style:name="P66" style:family="paragraph" style:parent-style-name="Heading_20_1">
+    <style:style style:name="P73" style:family="paragraph" style:parent-style-name="Heading_20_1">
       <style:text-properties style:font-name="Cantarell" officeooo:paragraph-rsid="009f72f6"/>
     </style:style>
-    <style:style style:name="P67" style:family="paragraph" style:parent-style-name="Heading_20_1">
+    <style:style style:name="P74" style:family="paragraph" style:parent-style-name="Heading_20_1">
       <style:text-properties style:font-name="Cantarell" officeooo:paragraph-rsid="00c2734f"/>
     </style:style>
-    <style:style style:name="P68" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P75" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P69" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P76" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="005aec69" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P70" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P77" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="00319676" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P71" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P78" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="0034cf71" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P72" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P79" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="007e34e9" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P73" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P80" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P74" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P81" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="003b0313" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P75" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P82" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="0055ce37" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P76" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P83" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="00c9e1e0" officeooo:paragraph-rsid="00c9e1e0" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P77" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P84" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P78" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P85" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009b7863" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P79" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P86" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009b7863" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P80" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P87" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P81" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P88" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P82" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P89" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="0055ce37" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P83" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P90" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="008396ac" officeooo:paragraph-rsid="0083ca92" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P84" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P91" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P85" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P92" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="00af421a" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P86" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P93" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P87" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P94" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="00947e9e" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P88" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P95" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P89" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P96" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="00a0e670" officeooo:paragraph-rsid="00a0e670" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P90" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P97" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="00a0e670" officeooo:paragraph-rsid="00b96abd" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P91" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P98" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00af421a" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P92" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P99" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P93" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P100" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P94" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P101" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00ab8446" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P95" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P102" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00b6b21a" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P96" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P103" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00b6b21a" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P97" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P104" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P98" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P105" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P99" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P106" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00c6da79" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P100" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P107" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00b07167" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P101" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P108" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P102" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P109" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00af421a" fo:background-color="#dddddd" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P103" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P110" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="12pt" fo:font-weight="bold" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P104" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P111" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="8pt" fo:font-weight="bold" officeooo:paragraph-rsid="00b41c6c" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P105" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P112" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="8pt" fo:font-weight="bold" officeooo:rsid="001db513" officeooo:paragraph-rsid="00ab8446" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P106" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P113" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="8pt" fo:font-weight="bold" officeooo:rsid="001db513" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P107" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P114" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="8pt" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00a5f256" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P108" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P115" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="9pt" fo:font-weight="normal" style:font-size-asian="9pt" style:font-weight-asian="normal" style:font-size-complex="9pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P109" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P116" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P110" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P117" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="005aec69" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P111" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P118" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="007e34e9" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P112" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P119" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="00319676" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P113" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P120" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="0034cf71" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P114" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P121" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P115" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P122" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="003b0313" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P116" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P123" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="0055ce37" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P117" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P124" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="00d669c4" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P125" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="00c9e1e0" officeooo:paragraph-rsid="00c9e1e0" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P118" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P126" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009b7863" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P119" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P127" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009b7863" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P120" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P128" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P121" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P129" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="00d4adf3" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P130" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P131" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P122" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P132" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P123" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P133" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="0055ce37" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P124" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P134" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="008396ac" officeooo:paragraph-rsid="0083ca92" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P125" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P135" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P126" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P136" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="00af421a" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P127" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P137" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P128" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P138" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="00947e9e" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P129" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P139" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P130" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P140" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="00a0e670" officeooo:paragraph-rsid="00a0e670" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P131" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P141" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="00a0e670" officeooo:paragraph-rsid="00b96abd" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P132" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P142" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="00d4adf3" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P143" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P144" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="none" fo:font-weight="bold" officeooo:rsid="00d4adf3" officeooo:paragraph-rsid="00d80030" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P145" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="none" fo:font-weight="bold" officeooo:paragraph-rsid="005aec69" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P146" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="none" fo:font-weight="bold" officeooo:paragraph-rsid="007e34e9" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P147" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="none" fo:font-weight="bold" officeooo:paragraph-rsid="00319676" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P148" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="none" fo:font-weight="bold" officeooo:paragraph-rsid="00d669c4" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P149" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="none" fo:font-weight="bold" officeooo:rsid="00c9e1e0" officeooo:paragraph-rsid="00c9e1e0" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P150" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="none" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P151" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="none" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P152" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="bold" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009b7863" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P153" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00af421a" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P133" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P154" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P134" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P155" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P135" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P156" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00ab8446" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P136" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P157" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00b6b21a" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P137" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P158" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00b6b21a" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P138" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P159" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="bold" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P139" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P160" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00af421a" fo:background-color="#dddddd" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P140" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P161" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P141" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P162" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00c6da79" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P142" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P163" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00b07167" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P143" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P164" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-style="normal" fo:font-weight="normal" officeooo:rsid="00af421a" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-size-complex="12pt" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P144" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P165" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="12pt" fo:font-weight="bold" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="12pt" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P145" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P166" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="bold" officeooo:paragraph-rsid="00b41c6c" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P146" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P167" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="bold" officeooo:rsid="001db513" officeooo:paragraph-rsid="00ab8446" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P147" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P168" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="bold" officeooo:rsid="001db513" officeooo:paragraph-rsid="00bcd6d3" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P148" style:family="paragraph" style:parent-style-name="Text_20_body">
+    <style:style style:name="P169" style:family="paragraph" style:parent-style-name="Text_20_body">
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="bold" officeooo:rsid="008396ac" officeooo:paragraph-rsid="00a5f256" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P149" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P170" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P171" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P172" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P173" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="9pt" fo:font-weight="normal" style:font-size-asian="9pt" style:font-weight-asian="normal" style:font-size-complex="9pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P150" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P174" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell"/>
     </style:style>
-    <style:style style:name="P151" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P175" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell"/>
     </style:style>
-    <style:style style:name="P152" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P176" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P153" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P177" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="9pt" fo:font-weight="normal" officeooo:paragraph-rsid="009b7863" style:font-size-asian="9pt" style:font-weight-asian="normal" style:font-size-complex="9pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P154" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P178" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="9pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009b7863" style:font-size-asian="9pt" style:font-weight-asian="normal" style:font-size-complex="9pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P155" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P179" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="0095e6ef" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P156" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P180" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009cff63" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P157" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P181" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans"/>
     </style:style>
-    <style:style style:name="P158" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P182" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans"/>
     </style:style>
-    <style:style style:name="P159" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P183" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="9pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009b7863" style:font-size-asian="9pt" style:font-weight-asian="normal" style:font-size-complex="9pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P160" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P184" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="9pt" fo:font-weight="normal" officeooo:paragraph-rsid="009b7863" style:font-size-asian="9pt" style:font-weight-asian="normal" style:font-size-complex="9pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P161" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P185" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="9pt" style:text-underline-style="none" fo:font-weight="normal" officeooo:paragraph-rsid="009b7863" style:font-size-asian="9pt" style:font-weight-asian="normal" style:font-size-complex="9pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P186" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="0095e6ef" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P162" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P187" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009cff63" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P163" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P188" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P189" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="00d669c4" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P190" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="00d4adf3" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P191" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P164" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P192" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" style:text-underline-style="none" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P193" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#ff0000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P165" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P194" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties fo:color="#ff0000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P166" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P195" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties fo:color="#ff0000" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="009f72f6" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P167" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P196" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#ff0000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P168" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P197" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties fo:color="#ff0000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P169" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P198" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties fo:color="#ff0000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="009f72f6" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P170" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P199" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:text-properties fo:color="#ff0000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="P200" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties officeooo:paragraph-rsid="0085d769"/>
     </style:style>
-    <style:style style:name="P171" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P201" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties fo:font-size="8pt" style:font-size-asian="8pt" style:font-size-complex="8pt"/>
     </style:style>
-    <style:style style:name="P172" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P202" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties officeooo:paragraph-rsid="00a5f256"/>
     </style:style>
-    <style:style style:name="P173" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P203" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties officeooo:paragraph-rsid="00b6b21a"/>
     </style:style>
-    <style:style style:name="P174" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
+    <style:style style:name="P204" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
       <style:text-properties officeooo:paragraph-rsid="00bcd6d3"/>
     </style:style>
-    <style:style style:name="P175" style:family="paragraph" style:parent-style-name="Header">
-      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
-      <style:text-properties style:font-name="FreeSans" fo:font-size="9pt" officeooo:paragraph-rsid="00166ab1" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
-    </style:style>
-    <style:style style:name="P176" style:family="paragraph" style:parent-style-name="Preformatted_20_Text">
-      <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="0085d769"/>
-    </style:style>
-    <style:style style:name="P177" style:family="paragraph" style:parent-style-name="Preformatted_20_Text" style:master-page-name="">
-      <loext:graphic-properties draw:fill="none"/>
-      <style:paragraph-properties fo:margin-left="0.25in" fo:margin-right="0in" fo:margin-top="0in" fo:margin-bottom="0in" style:contextual-spacing="false" fo:text-indent="0in" style:auto-text-indent="false" style:page-number="auto" fo:background-color="transparent"/>
-      <style:text-properties style:font-name="FreeSans" officeooo:rsid="00d4adf3" officeooo:paragraph-rsid="00d4adf3"/>
-    </style:style>
-    <style:style style:name="P178" style:family="paragraph" style:parent-style-name="Standard">
-      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="00d4adf3" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
-    </style:style>
-    <style:style style:name="P179" style:family="paragraph" style:parent-style-name="Standard">
-      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P180" style:family="paragraph" style:parent-style-name="Standard">
-      <style:text-properties style:font-name="FreeSans"/>
-    </style:style>
-    <style:style style:name="P181" style:family="paragraph" style:parent-style-name="Standard" style:master-page-name="">
-      <loext:graphic-properties draw:fill="none"/>
-      <style:paragraph-properties fo:margin-left="0.25in" fo:margin-right="0in" fo:text-indent="0in" style:auto-text-indent="false" style:page-number="auto" fo:background-color="transparent"/>
-      <style:text-properties style:font-name="FreeSans"/>
-    </style:style>
-    <style:style style:name="P182" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="009f72f6"/>
-    </style:style>
-    <style:style style:name="P183" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:text-properties style:font-name="FreeSans" officeooo:paragraph-rsid="00d4adf3"/>
-    </style:style>
-    <style:style style:name="P184" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
-    </style:style>
-    <style:style style:name="P185" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="00d4adf3" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P186" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="009f72f6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P187" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P188" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:text-properties fo:color="#000000" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P189" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="009cff63" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P190" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P191" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="00d4adf3" officeooo:paragraph-rsid="00d4adf3" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P192" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="9pt" fo:font-weight="normal" officeooo:paragraph-rsid="009b7863" style:font-size-asian="9pt" style:font-weight-asian="normal" style:font-size-complex="9pt" style:font-weight-complex="normal"/>
-    </style:style>
     <style:style style:name="T1" style:family="text">
       <style:text-properties fo:color="#000000" loext:opacity="100%"/>
     </style:style>
     <style:style style:name="T2" style:family="text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal"/>
     </style:style>
     <style:style style:name="T3" style:family="text">
@@ -1096,91 +1148,130 @@
     <style:style style:name="T15" style:family="text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" officeooo:rsid="00d4adf3"/>
     </style:style>
     <style:style style:name="T16" style:family="text">
       <style:text-properties fo:color="#000000" loext:opacity="100%" officeooo:rsid="0091e790"/>
     </style:style>
     <style:style style:name="T17" style:family="text">
-      <style:text-properties fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" officeooo:rsid="00d669c4"/>
     </style:style>
     <style:style style:name="T18" style:family="text">
-      <style:text-properties fo:font-weight="bold" officeooo:rsid="00892188" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" officeooo:rsid="0091e790"/>
     </style:style>
     <style:style style:name="T19" style:family="text">
-      <style:text-properties fo:font-weight="bold" officeooo:rsid="0095e6ef" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
+      <style:text-properties fo:color="#000000" loext:opacity="100%" style:text-underline-style="none" officeooo:rsid="0091e790"/>
     </style:style>
     <style:style style:name="T20" style:family="text">
-      <style:text-properties fo:font-weight="bold" officeooo:rsid="008396ac" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
+      <style:text-properties fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T21" style:family="text">
-      <style:text-properties fo:font-weight="bold" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
+      <style:text-properties fo:font-weight="bold" officeooo:rsid="00892188" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T22" style:family="text">
-      <style:text-properties fo:font-weight="bold" officeooo:rsid="00892188" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
+      <style:text-properties fo:font-weight="bold" officeooo:rsid="0095e6ef" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T23" style:family="text">
-      <style:text-properties fo:font-weight="bold" officeooo:rsid="00c6da79" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
+      <style:text-properties fo:font-weight="bold" officeooo:rsid="008396ac" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T24" style:family="text">
-      <style:text-properties fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal"/>
+      <style:text-properties fo:font-weight="bold" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T25" style:family="text">
-      <style:text-properties fo:font-weight="normal" officeooo:rsid="005aec69" style:font-weight-asian="normal" style:font-weight-complex="normal"/>
+      <style:text-properties fo:font-weight="bold" officeooo:rsid="00892188" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T26" style:family="text">
-      <style:text-properties fo:font-size="12pt" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
+      <style:text-properties fo:font-weight="bold" officeooo:rsid="00c6da79" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T27" style:family="text">
-      <style:text-properties fo:font-size="12pt" fo:font-weight="bold" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-size-asian="12pt" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-weight-complex="bold"/>
+      <style:text-properties fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal"/>
     </style:style>
     <style:style style:name="T28" style:family="text">
-      <style:text-properties fo:font-size="12pt" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
+      <style:text-properties fo:font-weight="normal" officeooo:rsid="005aec69" style:font-weight-asian="normal" style:font-weight-complex="normal"/>
     </style:style>
     <style:style style:name="T29" style:family="text">
-      <style:text-properties fo:font-size="12pt" officeooo:rsid="00c2734f" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
+      <style:text-properties fo:font-weight="normal" officeooo:rsid="0091e790" style:font-weight-asian="normal" style:font-weight-complex="normal"/>
     </style:style>
     <style:style style:name="T30" style:family="text">
-      <style:text-properties officeooo:rsid="00a1cdd8" fo:background-color="#dddddd" loext:char-shading-value="0"/>
+      <style:text-properties fo:font-weight="normal" officeooo:rsid="00d669c4" style:font-weight-asian="normal" style:font-weight-complex="normal"/>
     </style:style>
     <style:style style:name="T31" style:family="text">
-      <style:text-properties fo:font-size="8pt" fo:font-weight="bold" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
+      <style:text-properties fo:font-size="12pt" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
     </style:style>
     <style:style style:name="T32" style:family="text">
-      <style:text-properties fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
+      <style:text-properties fo:font-size="12pt" fo:font-weight="bold" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-size-asian="12pt" style:font-weight-asian="bold" style:font-size-complex="12pt" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T33" style:family="text">
-      <style:text-properties fo:color="#ff0000" loext:opacity="100%"/>
+      <style:text-properties fo:font-size="12pt" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
     </style:style>
     <style:style style:name="T34" style:family="text">
-      <style:text-properties fo:color="#ff0000" loext:opacity="100%" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
+      <style:text-properties fo:font-size="12pt" officeooo:rsid="00c2734f" fo:background-color="#dddddd" loext:char-shading-value="0" style:font-size-asian="12pt" style:font-size-complex="12pt"/>
     </style:style>
     <style:style style:name="T35" style:family="text">
-      <style:text-properties fo:font-size="9pt" officeooo:rsid="009d4bd6" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
+      <style:text-properties officeooo:rsid="00a1cdd8" fo:background-color="#dddddd" loext:char-shading-value="0"/>
     </style:style>
     <style:style style:name="T36" style:family="text">
-      <style:text-properties fo:font-size="9pt" officeooo:rsid="0091e790" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
+      <style:text-properties fo:font-size="8pt" fo:font-weight="bold" style:font-size-asian="8pt" style:font-weight-asian="bold" style:font-size-complex="8pt" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T37" style:family="text">
-      <style:text-properties fo:font-size="9pt" fo:font-weight="bold" officeooo:rsid="0091e790" style:font-size-asian="9pt" style:font-weight-asian="bold" style:font-size-complex="9pt" style:font-weight-complex="bold"/>
+      <style:text-properties fo:font-size="8pt" fo:font-weight="normal" officeooo:rsid="0091e790" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
     </style:style>
     <style:style style:name="T38" style:family="text">
-      <style:text-properties fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+      <style:text-properties fo:font-size="8pt" style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color" fo:font-weight="normal" officeooo:rsid="0091e790" style:font-size-asian="8pt" style:font-weight-asian="normal" style:font-size-complex="8pt" style:font-weight-complex="normal"/>
     </style:style>
     <style:style style:name="T39" style:family="text">
-      <style:text-properties fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+      <style:text-properties fo:font-size="8pt" officeooo:rsid="0091e790" style:font-size-asian="8pt" style:font-size-complex="8pt"/>
     </style:style>
     <style:style style:name="T40" style:family="text">
-      <style:text-properties fo:font-style="italic" style:font-style-asian="italic" style:font-style-complex="italic"/>
+      <style:text-properties fo:color="#ff0000" loext:opacity="100%"/>
     </style:style>
     <style:style style:name="T41" style:family="text">
-      <style:text-properties fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal"/>
+      <style:text-properties fo:color="#ff0000" loext:opacity="100%" fo:font-size="10pt" fo:font-weight="normal" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
     <style:style style:name="T42" style:family="text">
+      <style:text-properties fo:font-size="9pt" officeooo:rsid="009d4bd6" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
+    </style:style>
+    <style:style style:name="T43" style:family="text">
+      <style:text-properties fo:font-size="9pt" officeooo:rsid="0091e790" style:font-size-asian="9pt" style:font-size-complex="9pt"/>
+    </style:style>
+    <style:style style:name="T44" style:family="text">
+      <style:text-properties fo:font-size="9pt" fo:font-weight="bold" officeooo:rsid="0091e790" style:font-size-asian="9pt" style:font-weight-asian="bold" style:font-size-complex="9pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="T45" style:family="text">
+      <style:text-properties fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="T46" style:family="text">
+      <style:text-properties fo:font-size="10pt" fo:font-weight="bold" officeooo:rsid="00d4adf3" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="T47" style:family="text">
+      <style:text-properties fo:font-style="italic" style:font-style-asian="italic" style:font-style-complex="italic"/>
+    </style:style>
+    <style:style style:name="T48" style:family="text">
+      <style:text-properties fo:font-style="normal" style:font-style-asian="normal" style:font-style-complex="normal"/>
+    </style:style>
+    <style:style style:name="T49" style:family="text">
       <style:text-properties fo:font-style="normal" fo:font-weight="normal" style:font-style-asian="normal" style:font-weight-asian="normal" style:font-style-complex="normal" style:font-weight-complex="normal"/>
     </style:style>
+    <style:style style:name="T50" style:family="text">
+      <style:text-properties officeooo:rsid="00d669c4"/>
+    </style:style>
+    <style:style style:name="T51" style:family="text">
+      <style:text-properties fo:color="#000080" loext:opacity="100%" fo:font-weight="normal" style:font-weight-asian="normal" style:font-weight-complex="normal"/>
+    </style:style>
+    <style:style style:name="T52" style:family="text">
+      <style:text-properties style:text-underline-style="solid" style:text-underline-width="auto" style:text-underline-color="font-color"/>
+    </style:style>
+    <style:style style:name="T53" style:family="text">
+      <style:text-properties style:text-underline-style="none"/>
+    </style:style>
+    <style:style style:name="T54" style:family="text">
+      <style:text-properties style:text-underline-style="none" fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="T55" style:family="text">
+      <style:text-properties officeooo:rsid="0091e790"/>
+    </style:style>
     <style:style style:name="fr1" style:family="graphic" style:parent-style-name="Frame">
       <style:graphic-properties style:print-content="true" style:protect="none" style:wrap="none" style:vertical-pos="middle" style:vertical-rel="baseline" style:horizontal-pos="center" style:horizontal-rel="paragraph" fo:background-color="transparent" draw:fill="none" draw:fill-color="#ffffff" fo:padding="0in" fo:border="none" style:shadow="none" draw:shadow-opacity="100%" draw:wrap-influence-on-position="once-concurrent" loext:allow-overlap="true">
         <style:columns fo:column-count="1" fo:column-gap="0in"/>
       </style:graphic-properties>
     </style:style>
     <style:page-layout style:name="pm1">
       <style:page-layout-properties fo:page-width="8.5in" fo:page-height="11in" style:num-format="1" style:print-orientation="portrait" fo:margin-top="0.7874in" fo:margin-bottom="0.7874in" fo:margin-left="0.7874in" fo:margin-right="0.7874in" style:writing-mode="lr-tb" style:layout-grid-color="#c0c0c0" style:layout-grid-lines="44" style:layout-grid-base-height="0.2165in" style:layout-grid-ruby-height="0in" style:layout-grid-mode="none" style:layout-grid-ruby-below="false" style:layout-grid-print="true" style:layout-grid-display="true" style:footnote-max-height="0in" loext:margin-gutter="0in">
@@ -1227,76 +1318,72 @@
       <text:sequence-decls>
         <text:sequence-decl text:display-outline-level="0" text:name="Illustration"/>
         <text:sequence-decl text:display-outline-level="0" text:name="Table"/>
         <text:sequence-decl text:display-outline-level="0" text:name="Text"/>
         <text:sequence-decl text:display-outline-level="0" text:name="Drawing"/>
         <text:sequence-decl text:display-outline-level="0" text:name="Figure"/>
       </text:sequence-decls>
-      <text:p text:style-name="P13">
+      <text:p text:style-name="P15">
         <text:placeholder text:placeholder-type="text">&lt;for each=&quot;interpretation in records&quot;&gt;</text:placeholder>
       </text:p>
       <table:table table:name="Tabla1" table:style-name="Tabla1">
         <table:table-column table:style-name="Tabla1.A"/>
         <table:table-column table:style-name="Tabla1.B"/>
         <table:table-column table:style-name="Tabla1.C"/>
         <table:table-row>
           <table:table-cell table:style-name="Tabla1.A1" table:number-columns-spanned="3" office:value-type="string">
-            <text:p text:style-name="P128">
-              <text:span text:style-name="T18">
+            <text:p text:style-name="P138">
+              <text:span text:style-name="T21">
                 <text:s/>
               </text:span>
-              <text:span text:style-name="T35">D</text:span>
-              <text:span text:style-name="T36">ate:</text:span>
-              <text:span text:style-name="T37">
+              <text:span text:style-name="T42">D</text:span>
+              <text:span text:style-name="T43">ate:</text:span>
+              <text:span text:style-name="T44">
                 <text:placeholder text:placeholder-type="text">&lt;format_date(interpretation.date, user.language)&gt;</text:placeholder>
               </text:span>
             </text:p>
-            <text:p text:style-name="P162">
+            <text:p text:style-name="P189">
               <text:span text:style-name="T15">Study ID</text:span>
               <text:span text:style-name="T12">:</text:span>
               <text:span text:style-name="T1">
                 <text:placeholder text:placeholder-type="text">&lt;interpretation.number&gt;</text:placeholder>
               </text:span>
             </text:p>
-            <text:p text:style-name="P191">
+            <text:p text:style-name="P190">
               <text:span text:style-name="T1">Order</text:span>
               :
-              <text:span text:style-name="T16">
+              <text:span text:style-name="T19">
                 <text:placeholder text:placeholder-type="text">&lt;interpretation.order or ''&gt;</text:placeholder>
               </text:span>
             </text:p>
-            <text:p text:style-name="P179">
-              <text:span text:style-name="T16">
-                <text:placeholder text:placeholder-type="text">&lt;if test=&quot;interpretation.request.doctor&quot;&gt;</text:placeholder>
-              </text:span>
+            <text:p text:style-name="P172">
+              <text:placeholder text:placeholder-type="text">&lt;if test=&quot;interpretation.request and interpretation.request.doctor&quot;&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P191">
+            <text:p text:style-name="P190">
               <text:span text:style-name="T16">R</text:span>
               <text:span text:style-name="T1">equested by:</text:span>
               <text:span text:style-name="T16">
                 <text:placeholder text:placeholder-type="text">&lt;interpretation.request.doctor.rec_name&gt;</text:placeholder>
               </text:span>
             </text:p>
-            <text:p text:style-name="P179">
-              <text:span text:style-name="T16">
-                <text:placeholder text:placeholder-type="text">&lt;/if&gt;</text:placeholder>
-              </text:span>
+            <text:p text:style-name="P172">
+              <text:placeholder text:placeholder-type="text">&lt;/if&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P190">
+            <text:p text:style-name="P188">
               <text:span text:style-name="T15">Evaluated</text:span>
               <text:span text:style-name="T13">
                 <text:s/>
                 by
               </text:span>
               <text:span text:style-name="T1">:</text:span>
               <text:span text:style-name="T1">
                 <text:placeholder text:placeholder-type="text">&lt;interpretation.doctor.rec_name&gt;</text:placeholder>
               </text:span>
             </text:p>
-            <text:p text:style-name="P157">
+            <text:p text:style-name="P181">
               <text:span text:style-name="T10">Print Date:</text:span>
               <text:span text:style-name="T11">
                 <text:placeholder text:placeholder-type="text">&lt;format_date(datetime.date.today(), user.language)&gt;</text:placeholder>
               </text:span>
               <text:span text:style-name="T11">,</text:span>
               <text:span text:style-name="T11">
                 <text:placeholder text:placeholder-type="text">&lt;datetime.datetime.now().strftime('%H:%M:%S')&gt;</text:placeholder>
@@ -1304,165 +1391,144 @@
             </text:p>
           </table:table-cell>
           <table:covered-table-cell/>
           <table:covered-table-cell/>
         </table:table-row>
         <table:table-row>
           <table:table-cell table:style-name="Tabla1.A2" office:value-type="string">
-            <text:p text:style-name="P122">
-              <text:span text:style-name="T17">Patient</text:span>
+            <text:p text:style-name="P151">
+              <text:span text:style-name="T20">Patient</text:span>
               :
-              <text:span text:style-name="T17">
-                <text:placeholder text:placeholder-type="text">&lt;interpretation.patient.rec_name&gt;</text:placeholder>
+              <text:span text:style-name="T20">
+                <text:placeholder text:placeholder-type="text">&lt;interpretation.patient.rec_name if interpretation.patient else ''&gt;</text:placeholder>
               </text:span>
             </text:p>
-            <text:p text:style-name="P160">
+            <text:p text:style-name="P185">
               <text:span text:style-name="T9">PUID</text:span>
               <text:span text:style-name="T7">:</text:span>
               <text:span text:style-name="T1"/>
               <text:span text:style-name="T1">
-                <text:placeholder text:placeholder-type="text">&lt;interpretation.patient.name.ref&gt;</text:placeholder>
+                <text:placeholder text:placeholder-type="text">&lt;interpretation.patient.name.ref if interpretation.patient else ''&gt;</text:placeholder>
               </text:span>
             </text:p>
-            <text:p text:style-name="P119"/>
+            <text:p text:style-name="P152"/>
           </table:table-cell>
           <table:table-cell table:style-name="Tabla1.A2" office:value-type="string">
-            <text:p text:style-name="P110">
-              <text:placeholder text:placeholder-type="text">&lt;if test=&quot;interpretation.patient.dob&quot;&gt;</text:placeholder>
-              <text:span text:style-name="T24">
+            <text:p text:style-name="P145">
+              <text:placeholder text:placeholder-type="text">&lt;if test=&quot;interpretation.patient and interpretation.patient.dob&quot;&gt;</text:placeholder>
+              <text:span text:style-name="T27">
                 <text:s text:c="4"/>
               </text:span>
             </text:p>
-            <text:p text:style-name="P111">
-              <text:span text:style-name="T25">DoB:</text:span>
+            <text:p text:style-name="P146">
+              <text:span text:style-name="T28">DoB:</text:span>
               <text:placeholder text:placeholder-type="text">&lt;format_date(interpretation.patient.name.dob, user.language)&gt;</text:placeholder>
-              <text:span text:style-name="T24">
+              <text:span text:style-name="T27">
                 <text:s text:c="2"/>
               </text:span>
             </text:p>
-            <text:p text:style-name="P117">
+            <text:p text:style-name="P149">
               <text:placeholder text:placeholder-type="text">&lt;interpretation.computed_age&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P112">
+            <text:p text:style-name="P147">
               <text:placeholder text:placeholder-type="text">&lt;/if&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P127"/>
+            <text:p text:style-name="P150"/>
           </table:table-cell>
           <table:table-cell table:style-name="Tabla1.C2" office:value-type="string">
-            <text:p text:style-name="P163">
-              <text:placeholder text:placeholder-type="text">&lt;if test=&quot;interpretation.patient.name.gender == 'f'&quot;&gt;</text:placeholder>
+            <text:p text:style-name="P192">
+              <text:placeholder text:placeholder-type="text">&lt;if test=&quot;interpretation.patient&quot;&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P114">
-              Sex:
-              <text:span text:style-name="T42">Female</text:span>
+            <text:p text:style-name="P148">
+              <text:span text:style-name="T30">Gender</text:span>
+              <text:span text:style-name="T27">:</text:span>
+              <text:placeholder text:placeholder-type="text">&lt;interpretation.patient.name.gender_str&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P163">
-              <text:placeholder text:placeholder-type="text">&lt;/if&gt;</text:placeholder>
-            </text:p>
-            <text:p text:style-name="P163">
-              <text:placeholder text:placeholder-type="text">&lt;if test=&quot;interpretation.patient.name.gender == 'm'&quot;&gt;</text:placeholder>
-            </text:p>
-            <text:p text:style-name="P114">
-              Sex:
-              <text:span text:style-name="T24">Male</text:span>
-            </text:p>
-            <text:p text:style-name="P163">
+            <text:p text:style-name="P192">
               <text:placeholder text:placeholder-type="text">&lt;/if&gt;</text:placeholder>
             </text:p>
           </table:table-cell>
         </table:table-row>
-        <table:table-row>
+        <table:table-row table:style-name="Tabla1.3">
           <table:table-cell table:style-name="Tabla1.A2" office:value-type="string">
-            <text:p text:style-name="P185">
-              <text:span text:style-name="T17">Study</text:span>
-              :
-              <text:placeholder text:placeholder-type="text">&lt;interpretation.requested_test.rec_name&gt;</text:placeholder>
+            <text:p text:style-name="P142">
+              <text:span text:style-name="T54">Study</text:span>
+              <text:span text:style-name="T53">:</text:span>
+              <text:span text:style-name="T55">
+                <text:placeholder text:placeholder-type="text">&lt;interpretation.requested_test.rec_name if interpretation.requested_test else ''&gt;</text:placeholder>
+              </text:span>
             </text:p>
           </table:table-cell>
           <table:table-cell table:style-name="Tabla1.C2" table:number-columns-spanned="2" office:value-type="string">
-            <text:p text:style-name="P178">
+            <text:p text:style-name="P144">
               Context:
-              <text:span text:style-name="T32">
-                <text:placeholder text:placeholder-type="text">&lt;interpretation.request.context.rec_name&gt;</text:placeholder>
+              <text:span text:style-name="T29">
+                <text:placeholder text:placeholder-type="text">&lt;interpretation.request.context.rec_name if interpretation.request and interpretation.request.context else ''&gt;</text:placeholder>
               </text:span>
             </text:p>
           </table:table-cell>
           <table:covered-table-cell/>
         </table:table-row>
       </table:table>
-      <text:p text:style-name="P13">
-        <text:span text:style-name="T38"/>
-      </text:p>
-      <text:p text:style-name="P181">
-        <text:span text:style-name="T39">Interpretation</text:span>
-        <text:span text:style-name="T38">:</text:span>
+      <text:p text:style-name="P26"/>
+      <text:p text:style-name="P43">
+        <text:span text:style-name="T46">Interpretation</text:span>
+        <text:span text:style-name="T45">:</text:span>
       </text:p>
       <table:table table:name="Table1" table:style-name="Table1">
         <table:table-column table:style-name="Table1.A"/>
         <table:table-row>
           <table:table-cell table:style-name="Table1.A1" office:value-type="string">
-            <text:p text:style-name="P182">
-              <text:span text:style-name="T34">
-                <text:placeholder text:placeholder-type="text">&lt;for each=&quot;line in (interpretation.comment or &quot;&quot;).split('\n')&quot;&gt;</text:placeholder>
-              </text:span>
+            <text:p text:style-name="P197">
+              <text:placeholder text:placeholder-type="text">&lt;for each=&quot;line in (interpretation.comment or &quot;&quot;).split('\n')&quot;&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P129">
+            <text:p text:style-name="P139">
               <text:placeholder text:placeholder-type="text">&lt;line&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P129">
+            <text:p text:style-name="P139">
               <text:placeholder text:placeholder-type="text">&lt;/for&gt;</text:placeholder>
             </text:p>
           </table:table-cell>
         </table:table-row>
       </table:table>
-      <text:p text:style-name="P37"/>
-      <text:p text:style-name="P177">Resources:</text:p>
-      <text:p text:style-name="P183">
-        <text:span text:style-name="T34">
-          <text:placeholder text:placeholder-type="text">&lt;for each=&quot;image in interpretation.images&quot;&gt;</text:placeholder>
-        </text:span>
+      <text:p text:style-name="P41"/>
+      <text:p text:style-name="P42">Resources:</text:p>
+      <text:p text:style-name="P199">
+        <text:placeholder text:placeholder-type="text">&lt;for each=&quot;image in interpretation.images&quot;&gt;</text:placeholder>
       </text:p>
-      <table:table table:name="Table2" table:style-name="Table2">
-        <table:table-column table:style-name="Table2.A"/>
-        <table:table-column table:style-name="Table2.B"/>
-        <table:table-row table:style-name="Table2.1">
-          <table:table-cell table:style-name="Table2.A1" office:value-type="string">
-            <text:p text:style-name="P184">
+      <table:table table:name="Tabla2" table:style-name="Tabla2">
+        <table:table-column table:style-name="Tabla2.A"/>
+        <table:table-column table:style-name="Tabla2.B"/>
+        <table:table-row table:style-name="Tabla2.1">
+          <table:table-cell table:style-name="Tabla2.A1" office:value-type="string">
+            <text:p text:style-name="P130">
               <draw:frame draw:style-name="fr1" draw:name="image: (image.data, 'image/png','5cm','5cm')" text:anchor-type="as-char" svg:width="0.6791in" svg:height="0.178in" draw:z-index="0">
                 <draw:text-box>
                   <text:p text:style-name="Frame_20_contents"/>
                 </draw:text-box>
               </draw:frame>
             </text:p>
           </table:table-cell>
-          <table:table-cell table:style-name="Table2.B1" office:value-type="string">
-            <text:p text:style-name="P183">
-              <text:span text:style-name="T34">
-                <text:placeholder text:placeholder-type="text">&lt;for each=&quot;line in (image.description or &quot;&quot;).split('\n')&quot;&gt;</text:placeholder>
-              </text:span>
+          <table:table-cell table:style-name="Tabla2.B1" office:value-type="string">
+            <text:p text:style-name="P199">
+              <text:placeholder text:placeholder-type="text">&lt;for each=&quot;line in (image.description or &quot;&quot;).split('\n')&quot;&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P188">
+            <text:p text:style-name="P171">
               <text:placeholder text:placeholder-type="text">&lt;line&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P187">
+            <text:p text:style-name="P143">
               <text:placeholder text:placeholder-type="text">&lt;/for&gt;</text:placeholder>
             </text:p>
           </table:table-cell>
         </table:table-row>
       </table:table>
-      <text:p text:style-name="P187">
-        <text:span text:style-name="T33">
-          <text:placeholder text:placeholder-type="text">&lt;/for&gt;</text:placeholder>
-        </text:span>
-      </text:p>
-      <text:p text:style-name="P183">
-        <text:span text:style-name="T34"/>
-      </text:p>
-      <text:p text:style-name="P183">
-        <text:span text:style-name="T34"/>
+      <text:p text:style-name="P199">
+        <text:placeholder text:placeholder-type="text">&lt;/for&gt;</text:placeholder>
       </text:p>
-      <text:p text:style-name="P37">
+      <text:p text:style-name="P199"/>
+      <text:p text:style-name="P199"/>
+      <text:p text:style-name="P41">
         <text:placeholder text:placeholder-type="text">&lt;/for&gt;</text:placeholder>
       </text:p>
     </office:text>
   </office:body>
 </office:document>
```

### Comparing `gnuhealth_imaging-4.2.0/security/access_rights.xml` & `gnuhealth_imaging-4.2.1/security/access_rights.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/sequences.py` & `gnuhealth_imaging-4.2.1/sequences.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/setup.py` & `gnuhealth_imaging-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/tests/test_health_imaging.py` & `gnuhealth_imaging-4.2.1/tests/test_health_imaging.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/view/imaging_test_form.xml` & `gnuhealth_imaging-4.2.1/view/imaging_test_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/view/imaging_test_request_form.xml` & `gnuhealth_imaging-4.2.1/view/imaging_test_request_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/view/imaging_test_result_form.xml` & `gnuhealth_imaging-4.2.1/view/imaging_test_result_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/view/patient_imaging_test_request_start_form.xml` & `gnuhealth_imaging-4.2.1/view/patient_imaging_test_request_start_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_imaging-4.2.0/wizard/wizard_health_imaging.py` & `gnuhealth_imaging-4.2.1/wizard/wizard_health_imaging.py`

 * *Files identical despite different names*

