# Comparing `tmp/gnuhealth_qrcodes-4.2.0.tar.gz` & `tmp/gnuhealth_qrcodes-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_qrcodes-4.2.0.tar", last modified: Sat Feb 11 21:57:34 2023, max compression
+gzip compressed data, was "gnuhealth_qrcodes-4.2.1.tar", last modified: Fri Apr  7 10:19:35 2023, max compression
```

## Comparing `gnuhealth_qrcodes-4.2.0.tar` & `gnuhealth_qrcodes-4.2.1.tar`

### file list

```diff
@@ -1,47 +1,47 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:34.286413 gnuhealth_qrcodes-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5734 2023-02-11 21:57:34.286246 gnuhealth_qrcodes-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/README.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1062 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:34.283759 gnuhealth_qrcodes-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      346 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/doc/index.rst
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:34.285741 gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5734 2023-02-11 21:57:34.000000 gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1333 2023-02-11 21:57:34.000000 gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:34.000000 gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       66 2023-02-11 21:57:34.000000 gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:57:34.000000 gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       66 2023-02-11 21:57:34.000000 gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:57:34.000000 gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6429 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/health_qrcodes.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3592 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/health_qrcodes_report.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1419 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/health_qrcodes_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:34.284403 gnuhealth_qrcodes-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      803 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)      748 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)      792 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)      790 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)      775 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)      749 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     2151 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)      366 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)      764 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3509 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/locale/zh_CN.po
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:34.284816 gnuhealth_qrcodes-4.2.0/report/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    62204 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/report/appointment_qrcode.fodt
--rw-r--r--   0 lfm       (1001) lfm       (1001)    44451 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/report/barcode39.fodt
--rw-r--r--   0 lfm       (1001) lfm       (1001)    52343 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/report/labtest_qrcode.fodt
--rw-r--r--   0 lfm       (1001) lfm       (1001)    51397 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/report/newborn_card.fodt
--rw-r--r--   0 lfm       (1001) lfm       (1001)    53669 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/report/patient_card.fodt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:57:34.286449 gnuhealth_qrcodes-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3607 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:34.284966 gnuhealth_qrcodes-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      234 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      597 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/tests/test_health_qrcodes.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      143 2023-02-11 12:44:33.000000 gnuhealth_qrcodes-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:57:34.285221 gnuhealth_qrcodes-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      454 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/view/gnuhealth_appointment.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      462 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/view/gnuhealth_patient_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      533 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/view/lab_form.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      444 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.0/view/newborn_form.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:35.406663 gnuhealth_qrcodes-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5734 2023-04-07 10:19:35.406520 gnuhealth_qrcodes-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/README.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1062 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:35.404030 gnuhealth_qrcodes-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      346 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/doc/index.rst
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:35.406039 gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5734 2023-04-07 10:19:35.000000 gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1333 2023-04-07 10:19:35.000000 gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:35.000000 gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       66 2023-04-07 10:19:35.000000 gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:19:35.000000 gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       66 2023-04-07 10:19:35.000000 gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:19:35.000000 gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6438 2023-04-07 09:20:43.000000 gnuhealth_qrcodes-4.2.1/health_qrcodes.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3592 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/health_qrcodes_report.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1419 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/health_qrcodes_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:35.404697 gnuhealth_qrcodes-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      803 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)      748 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)      792 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)      790 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)      775 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)      749 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     2151 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)      366 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)      764 2022-11-28 22:17:48.000000 gnuhealth_qrcodes-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3509 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/locale/zh_CN.po
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:35.405129 gnuhealth_qrcodes-4.2.1/report/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    62204 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/report/appointment_qrcode.fodt
+-rw-r--r--   0 lfm       (1001) wheel        (0)    44451 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/report/barcode39.fodt
+-rw-r--r--   0 lfm       (1001) wheel        (0)    52343 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/report/labtest_qrcode.fodt
+-rw-r--r--   0 lfm       (1001) wheel        (0)    51397 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/report/newborn_card.fodt
+-rw-r--r--   0 lfm       (1001) wheel        (0)    55205 2023-04-07 09:20:43.000000 gnuhealth_qrcodes-4.2.1/report/patient_card.fodt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:19:35.406701 gnuhealth_qrcodes-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3607 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:35.405292 gnuhealth_qrcodes-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      234 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      597 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/tests/test_health_qrcodes.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      143 2023-04-07 09:37:21.000000 gnuhealth_qrcodes-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:19:35.405563 gnuhealth_qrcodes-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      454 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/view/gnuhealth_appointment.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      462 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/view/gnuhealth_patient_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      533 2023-01-18 16:33:08.000000 gnuhealth_qrcodes-4.2.1/view/lab_form.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      444 2023-04-07 09:17:52.000000 gnuhealth_qrcodes-4.2.1/view/newborn_form.xml
```

### Comparing `gnuhealth_qrcodes-4.2.0/COPYING` & `gnuhealth_qrcodes-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/PKG-INFO` & `gnuhealth_qrcodes-4.2.1/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth_qrcodes
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health support for Quick Response - QR Codes-  package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_qrcodes-4.2.0/README.rst` & `gnuhealth_qrcodes-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/__init__.py` & `gnuhealth_qrcodes-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/PKG-INFO` & `gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: gnuhealth-qrcodes
-Version: 4.2.0
+Version: 4.2.1
 Summary: GNU Health support for Quick Response - QR Codes-  package
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_qrcodes-4.2.0/gnuhealth_qrcodes.egg-info/SOURCES.txt` & `gnuhealth_qrcodes-4.2.1/gnuhealth_qrcodes.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/health_qrcodes.py` & `gnuhealth_qrcodes-4.2.1/health_qrcodes.py`

 * *Files 1% similar despite different names*

```diff
@@ -30,15 +30,15 @@
 
     def make_qrcode(self, name):
         # Create the QR code
 
         patient_puid = self.puid or ''
         patient_blood_type = self.blood_type or ''
         patient_rh = self.rh or ''
-        patient_gender = self.gender or ''
+        patient_gender = self.name.gender_str or ''
         patient_dob = ''
 
         if (self.dob):
             patient_dob = str(self.dob)
 
         qr_string = f'{patient_puid}\n' \
             f'Name: {self.name.rec_name}\n' \
```

### Comparing `gnuhealth_qrcodes-4.2.0/health_qrcodes_report.xml` & `gnuhealth_qrcodes-4.2.1/health_qrcodes_report.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/health_qrcodes_view.xml` & `gnuhealth_qrcodes-4.2.1/health_qrcodes_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/locale/ar.po` & `gnuhealth_qrcodes-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/locale/de.po` & `gnuhealth_qrcodes-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/locale/el.po` & `gnuhealth_qrcodes-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/locale/es.po` & `gnuhealth_qrcodes-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/locale/fr.po` & `gnuhealth_qrcodes-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/locale/it_IT.po` & `gnuhealth_qrcodes-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/locale/ja_JP.po` & `gnuhealth_qrcodes-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/locale/pt_BR.po` & `gnuhealth_qrcodes-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/locale/zh_CN.po` & `gnuhealth_qrcodes-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/report/appointment_qrcode.fodt` & `gnuhealth_qrcodes-4.2.1/report/appointment_qrcode.fodt`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/report/barcode39.fodt` & `gnuhealth_qrcodes-4.2.1/report/barcode39.fodt`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/report/labtest_qrcode.fodt` & `gnuhealth_qrcodes-4.2.1/report/labtest_qrcode.fodt`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/report/newborn_card.fodt` & `gnuhealth_qrcodes-4.2.1/report/newborn_card.fodt`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/report/patient_card.fodt` & `gnuhealth_qrcodes-4.2.1/report/patient_card.fodt`

 * *Files 3% similar despite different names*

#### Comparing `gnuhealth_qrcodes-4.2.0/report/patient_card.fodt` & `gnuhealth_qrcodes-4.2.1/report/patient_card.fodt`

```diff
@@ -1,188 +1,197 @@
 <?xml version="1.0" encoding="utf-8"?>
-<office:document xmlns:officeooo="http://openoffice.org/2009/office" xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rpt="http://openoffice.org/2005/report" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:xforms="http://www.w3.org/2002/xforms" office:version="1.3" office:mimetype="application/vnd.oasis.opendocument.text">
+<office:document xmlns:css3t="http://www.w3.org/TR/css3-text/" xmlns:grddl="http://www.w3.org/2003/g/data-view#" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xforms="http://www.w3.org/2002/xforms" xmlns:dom="http://www.w3.org/2001/xml-events" xmlns:script="urn:oasis:names:tc:opendocument:xmlns:script:1.0" xmlns:form="urn:oasis:names:tc:opendocument:xmlns:form:1.0" xmlns:math="http://www.w3.org/1998/Math/MathML" xmlns:meta="urn:oasis:names:tc:opendocument:xmlns:meta:1.0" xmlns:loext="urn:org:documentfoundation:names:experimental:office:xmlns:loext:1.0" xmlns:field="urn:openoffice:names:experimental:ooo-ms-interop:xmlns:field:1.0" xmlns:number="urn:oasis:names:tc:opendocument:xmlns:datastyle:1.0" xmlns:officeooo="http://openoffice.org/2009/office" xmlns:table="urn:oasis:names:tc:opendocument:xmlns:table:1.0" xmlns:chart="urn:oasis:names:tc:opendocument:xmlns:chart:1.0" xmlns:formx="urn:openoffice:names:experimental:ooxml-odf-interop:xmlns:form:1.0" xmlns:svg="urn:oasis:names:tc:opendocument:xmlns:svg-compatible:1.0" xmlns:rpt="http://openoffice.org/2005/report" xmlns:dr3d="urn:oasis:names:tc:opendocument:xmlns:dr3d:1.0" xmlns:tableooo="http://openoffice.org/2009/table" xmlns:draw="urn:oasis:names:tc:opendocument:xmlns:drawing:1.0" xmlns:of="urn:oasis:names:tc:opendocument:xmlns:of:1.2" xmlns:text="urn:oasis:names:tc:opendocument:xmlns:text:1.0" xmlns:style="urn:oasis:names:tc:opendocument:xmlns:style:1.0" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:calcext="urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0" xmlns:oooc="http://openoffice.org/2004/calc" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:drawooo="http://openoffice.org/2010/draw" xmlns:ooow="http://openoffice.org/2004/writer" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0" xmlns:fo="urn:oasis:names:tc:opendocument:xmlns:xsl-fo-compatible:1.0" xmlns:ooo="http://openoffice.org/2004/office" xmlns:office="urn:oasis:names:tc:opendocument:xmlns:office:1.0" office:version="1.3" office:mimetype="application/vnd.oasis.opendocument.text">
   <office:meta>
-    <meta:generator>LibreOffice/7.1.8.1$Linux_X86_64 LibreOffice_project/10$Build-1</meta:generator>
+    <meta:generator>LibreOffice/7.4.4.2$FreeBSD_X86_64 LibreOffice_project/40$Build-2</meta:generator>
     <meta:creation-date>2008-06-07T15:26:29</meta:creation-date>
     <dc:date>2008-08-27T16:57:45</dc:date>
     <meta:editing-cycles>1</meta:editing-cycles>
     <meta:editing-duration>PT0S</meta:editing-duration>
-    <meta:document-statistic meta:table-count="1" meta:image-count="0" meta:object-count="0" meta:page-count="1" meta:paragraph-count="12" meta:word-count="25" meta:character-count="247" meta:non-whitespace-character-count="231"/>
+    <meta:document-statistic meta:table-count="1" meta:image-count="0" meta:object-count="0" meta:page-count="1" meta:paragraph-count="12" meta:word-count="25" meta:character-count="256" meta:non-whitespace-character-count="240"/>
     <meta:user-defined meta:name="Info 1"/>
     <meta:user-defined meta:name="Info 2"/>
     <meta:user-defined meta:name="Info 3"/>
     <meta:user-defined meta:name="Info 4"/>
   </office:meta>
   <office:settings>
     <config:config-item-set config:name="ooo:view-settings">
-      <config:config-item config:name="ViewAreaTop" config:type="long">0</config:config-item>
+      <config:config-item config:name="ViewAreaTop" config:type="long">9525</config:config-item>
       <config:config-item config:name="ViewAreaLeft" config:type="long">0</config:config-item>
-      <config:config-item config:name="ViewAreaWidth" config:type="long">29390</config:config-item>
-      <config:config-item config:name="ViewAreaHeight" config:type="long">15252</config:config-item>
+      <config:config-item config:name="ViewAreaWidth" config:type="long">38858</config:config-item>
+      <config:config-item config:name="ViewAreaHeight" config:type="long">11984</config:config-item>
       <config:config-item config:name="ShowRedlineChanges" config:type="boolean">true</config:config-item>
       <config:config-item config:name="InBrowseMode" config:type="boolean">false</config:config-item>
       <config:config-item-map-indexed config:name="Views">
         <config:config-item-map-entry>
           <config:config-item config:name="ViewId" config:type="string">view2</config:config-item>
-          <config:config-item config:name="ViewLeft" config:type="long">7096</config:config-item>
-          <config:config-item config:name="ViewTop" config:type="long">12305</config:config-item>
+          <config:config-item config:name="ViewLeft" config:type="long">18175</config:config-item>
+          <config:config-item config:name="ViewTop" config:type="long">11755</config:config-item>
           <config:config-item config:name="VisibleLeft" config:type="long">0</config:config-item>
-          <config:config-item config:name="VisibleTop" config:type="long">0</config:config-item>
-          <config:config-item config:name="VisibleRight" config:type="long">29388</config:config-item>
-          <config:config-item config:name="VisibleBottom" config:type="long">15251</config:config-item>
+          <config:config-item config:name="VisibleTop" config:type="long">9525</config:config-item>
+          <config:config-item config:name="VisibleRight" config:type="long">38857</config:config-item>
+          <config:config-item config:name="VisibleBottom" config:type="long">21507</config:config-item>
           <config:config-item config:name="ZoomType" config:type="short">0</config:config-item>
           <config:config-item config:name="ViewLayoutColumns" config:type="short">1</config:config-item>
           <config:config-item config:name="ViewLayoutBookMode" config:type="boolean">false</config:config-item>
           <config:config-item config:name="ZoomFactor" config:type="short">140</config:config-item>
           <config:config-item config:name="IsSelectedFrame" config:type="boolean">false</config:config-item>
+          <config:config-item config:name="KeepRatio" config:type="boolean">false</config:config-item>
+          <config:config-item config:name="HideWhitespace" config:type="boolean">false</config:config-item>
           <config:config-item config:name="AnchoredTextOverflowLegacy" config:type="boolean">false</config:config-item>
         </config:config-item-map-entry>
       </config:config-item-map-indexed>
     </config:config-item-set>
     <config:config-item-set config:name="ooo:configuration-settings">
-      <config:config-item config:name="PrintProspect" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrintReversed" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrintSingleJobs" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrintLeftPages" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="PrintTables" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="PrintControls" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="PrintPageBackground" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="PrintDrawings" config:type="boolean">true</config:config-item>
       <config:config-item config:name="PrintBlackFonts" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintReversed" config:type="boolean">false</config:config-item>
       <config:config-item config:name="PrintAnnotationMode" config:type="short">0</config:config-item>
+      <config:config-item config:name="PrintGraphics" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="PrintTables" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="WordLikeWrapForAsCharFlys" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="NoNumberingShowFollowBy" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintProspect" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintHiddenText" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintRightPages" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="PrintFaxName" config:type="string"/>
+      <config:config-item config:name="TabsRelativeToIndent" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="RedlineProtectionKey" config:type="base64Binary"/>
       <config:config-item config:name="PrintTextPlaceholder" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="ProtectFields" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintControls" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="SaveThumbnail" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="EmbedFonts" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="AutoFirstLineIndentDisregardLineSpace" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="Rsid" config:type="int">4232260</config:config-item>
+      <config:config-item config:name="GutterAtTop" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="AddFrameOffsets" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="FrameAutowidthWithMorePara" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="MathBaselineAlignment" config:type="boolean">false</config:config-item>
       <config:config-item config:name="ProtectBookmarks" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="IgnoreTabsAndBlanksForLineCalculation" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="ContinuousEndnotes" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="FieldAutoUpdate" config:type="boolean">true</config:config-item>
       <config:config-item config:name="EmptyDbFieldHidesPara" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="DisableOffPagePositioning" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="SubtractFlysAnchoredAtFlys" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="PropLineSpacingShrinksFirstLine" config:type="boolean">false</config:config-item>
       <config:config-item config:name="ApplyParagraphMarkFormatToNumbering" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="TreatSingleColumnBreakAsPageBreak" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="EmbedSystemFonts" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="EmbedComplexScriptFonts" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="AddParaTableSpacing" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="TabOverSpacing" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintEmptyPages" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="AddParaLineSpacingToTableCells" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="TabOverMargin" config:type="boolean">false</config:config-item>
       <config:config-item config:name="EmbedAsianScriptFonts" config:type="boolean">true</config:config-item>
       <config:config-item config:name="EmbedLatinScriptFonts" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="DisableOffPagePositioning" config:type="boolean">false</config:config-item>
       <config:config-item config:name="EmbedOnlyUsedFonts" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="ContinuousEndnotes" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="EmbedFonts" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="ImagePreferredDPI" config:type="int">0</config:config-item>
+      <config:config-item config:name="MsWordCompMinLineHeightByFly" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="SurroundTextWrapSmall" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="BackgroundParaOverDrawings" config:type="boolean">false</config:config-item>
       <config:config-item config:name="ClippedPictures" config:type="boolean">false</config:config-item>
       <config:config-item config:name="FloattableNomargins" config:type="boolean">false</config:config-item>
       <config:config-item config:name="UnbreakableNumberings" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="EmbedSystemFonts" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="TabOverflow" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="SmallCapsPercentage66" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="CollapseEmptyCellPara" config:type="boolean">true</config:config-item>
       <config:config-item config:name="HeaderSpacingBelowLastPara" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="AllowPrintJobCancel" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="UseOldPrinterMetrics" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="TabOverMargin" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="TabsRelativeToIndent" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="UseOldNumbering" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="InvertBorderSpacing" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrintPaperFromSetup" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="UpdateFromTemplate" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="RsidRoot" config:type="int">1589586</config:config-item>
+      <config:config-item config:name="PrinterSetup" config:type="base64Binary"/>
+      <config:config-item config:name="CurrentDatabaseCommand" config:type="string"/>
+      <config:config-item config:name="AlignTabStopPosition" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="ClipAsCharacterAnchoredWriterFlyFrames" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="DoNotCaptureDrawObjsOnPage" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="SaveGlobalDocumentLinks" config:type="boolean">false</config:config-item>
       <config:config-item config:name="CurrentDatabaseCommandType" config:type="int">0</config:config-item>
+      <config:config-item config:name="LoadReadonly" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="DoNotResetParaAttrsForNumFont" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="StylesNoDefault" config:type="boolean">false</config:config-item>
       <config:config-item config:name="LinkUpdateMode" config:type="short">1</config:config-item>
-      <config:config-item config:name="AddParaSpacingToTableCells" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="FrameAutowidthWithMorePara" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="CurrentDatabaseCommand" config:type="string"/>
-      <config:config-item config:name="PrinterIndependentLayout" config:type="string">high-resolution</config:config-item>
-      <config:config-item config:name="ApplyUserData" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrintFaxName" config:type="string"/>
+      <config:config-item config:name="DoNotJustifyLinesWithManualBreak" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PropLineSpacingShrinksFirstLine" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintDrawings" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="PrintSingleJobs" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="ConsiderTextWrapOnObjPos" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="TabAtLeftIndentForParagraphsInList" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="ProtectFields" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="UnxForceZeroExtLeading" config:type="boolean">false</config:config-item>
       <config:config-item config:name="CurrentDatabaseDataSource" config:type="string"/>
-      <config:config-item config:name="ClipAsCharacterAnchoredWriterFlyFrames" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="IsKernAsianPunctuation" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="SaveThumbnail" config:type="boolean">true</config:config-item>
       <config:config-item config:name="UseFormerTextWrapping" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="AddExternalLeading" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="AddParaTableSpacing" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="StylesNoDefault" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="ChartAutoUpdate" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="PrinterSetup" config:type="base64Binary"/>
-      <config:config-item config:name="AddParaTableSpacingAtStart" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="Rsid" config:type="int">4217949</config:config-item>
+      <config:config-item config:name="PrintPaperFromSetup" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintLeftPages" config:type="boolean">true</config:config-item>
       <config:config-item config:name="EmbeddedDatabaseName" config:type="string"/>
-      <config:config-item config:name="FieldAutoUpdate" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="OutlineLevelYieldsNumbering" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="AlignTabStopPosition" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="CharacterCompressionType" config:type="short">0</config:config-item>
-      <config:config-item config:name="PrinterName" config:type="string"/>
-      <config:config-item config:name="SaveGlobalDocumentLinks" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrinterPaperFromSetup" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="ProtectForm" config:type="boolean">false</config:config-item>
       <config:config-item config:name="UseFormerLineSpacing" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="AddParaLineSpacingToTableCells" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="UseFormerObjectPositioning" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrintGraphics" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="SurroundTextWrapSmall" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="ConsiderTextWrapOnObjPos" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="MsWordCompTrailingBlanks" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="TabAtLeftIndentForParagraphsInList" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrintRightPages" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="IgnoreFirstLineIndentInNumbering" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="RedlineProtectionKey" config:type="base64Binary"/>
-      <config:config-item config:name="DoNotJustifyLinesWithManualBreak" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrintProspectRTL" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="PrintEmptyPages" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="DoNotResetParaAttrsForNumFont" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="AddFrameOffsets" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="IgnoreTabsAndBlanksForLineCalculation" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="LoadReadonly" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="DoNotCaptureDrawObjsOnPage" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="AllowPrintJobCancel" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="SubtractFlysAnchoredAtFlys" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="AddParaSpacingToTableCells" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="AddExternalLeading" config:type="boolean">true</config:config-item>
       <config:config-item config:name="AddVerticalFrameOffsets" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="UnxForceZeroExtLeading" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="TreatSingleColumnBreakAsPageBreak" config:type="boolean">false</config:config-item>
       <config:config-item config:name="IsLabelDocument" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="MsWordCompTrailingBlanks" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrinterPaperFromSetup" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="IgnoreFirstLineIndentInNumbering" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintPageBackground" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="OutlineLevelYieldsNumbering" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrinterName" config:type="string"/>
+      <config:config-item config:name="IsKernAsianPunctuation" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrinterIndependentLayout" config:type="string">high-resolution</config:config-item>
       <config:config-item config:name="TableRowKeep" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="RsidRoot" config:type="int">1589586</config:config-item>
-      <config:config-item config:name="PrintHiddenText" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="ProtectForm" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="MsWordCompMinLineHeightByFly" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="BackgroundParaOverDrawings" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="UpdateFromTemplate" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="FootnoteInColumnToPageEnd" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="EmbedComplexScriptFonts" config:type="boolean">true</config:config-item>
+      <config:config-item config:name="UseOldPrinterMetrics" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="InvertBorderSpacing" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="PrintProspectRTL" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="ApplyUserData" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="AddParaTableSpacingAtStart" config:type="boolean">true</config:config-item>
       <config:config-item config:name="SaveVersionOnClose" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="MathBaselineAlignment" config:type="boolean">false</config:config-item>
-      <config:config-item config:name="SmallCapsPercentage66" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="CollapseEmptyCellPara" config:type="boolean">true</config:config-item>
-      <config:config-item config:name="TabOverflow" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="CharacterCompressionType" config:type="short">0</config:config-item>
+      <config:config-item config:name="UseOldNumbering" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="UseFormerObjectPositioning" config:type="boolean">false</config:config-item>
+      <config:config-item config:name="ChartAutoUpdate" config:type="boolean">true</config:config-item>
     </config:config-item-set>
   </office:settings>
   <office:scripts>
     <office:script script:language="ooo:Basic">
       <ooo:libraries xmlns:ooo="http://openoffice.org/2004/office" xmlns:xlink="http://www.w3.org/1999/xlink"/>
     </office:script>
   </office:scripts>
   <office:font-face-decls>
-    <style:font-face style:name="StarSymbol" svg:font-family="StarSymbol"/>
     <style:font-face style:name="Cantarell" svg:font-family="Cantarell" style:font-pitch="variable"/>
-    <style:font-face style:name="Liberation Serif1" svg:font-family="'Liberation Serif'" style:font-adornments="Bold" style:font-family-generic="roman" style:font-pitch="variable"/>
-    <style:font-face style:name="Liberation Serif" svg:font-family="'Liberation Serif'" style:font-adornments="Regular" style:font-family-generic="roman" style:font-pitch="variable"/>
-    <style:font-face style:name="Nimbus Roman No9 L" svg:font-family="'Nimbus Roman No9 L'" style:font-family-generic="roman" style:font-pitch="variable"/>
+    <style:font-face style:name="DejaVu Sans" svg:font-family="'DejaVu Sans'" style:font-family-generic="system" style:font-pitch="variable"/>
     <style:font-face style:name="FreeSans" svg:font-family="FreeSans" style:font-family-generic="swiss" style:font-pitch="variable"/>
     <style:font-face style:name="Liberation Sans" svg:font-family="'Liberation Sans'" style:font-adornments="Regular" style:font-family-generic="swiss" style:font-pitch="variable"/>
-    <style:font-face style:name="DejaVu Sans" svg:font-family="'DejaVu Sans'" style:font-family-generic="system" style:font-pitch="variable"/>
+    <style:font-face style:name="Liberation Serif" svg:font-family="'Liberation Serif'" style:font-adornments="Bold" style:font-family-generic="roman" style:font-pitch="variable"/>
+    <style:font-face style:name="Liberation Serif1" svg:font-family="'Liberation Serif'" style:font-adornments="Regular" style:font-family-generic="roman" style:font-pitch="variable"/>
+    <style:font-face style:name="Nimbus Roman No9 L" svg:font-family="'Nimbus Roman No9 L'" style:font-family-generic="roman" style:font-pitch="variable"/>
+    <style:font-face style:name="StarSymbol" svg:font-family="StarSymbol"/>
   </office:font-face-decls>
   <office:styles>
     <style:default-style style:family="graphic">
       <style:graphic-properties svg:stroke-color="#3465a4" draw:fill-color="#729fcf" fo:wrap-option="no-wrap" draw:shadow-offset-x="0.1181in" draw:shadow-offset-y="0.1181in" draw:start-line-spacing-horizontal="0.1114in" draw:start-line-spacing-vertical="0.1114in" draw:end-line-spacing-horizontal="0.1114in" draw:end-line-spacing-vertical="0.1114in" style:flow-with-text="false"/>
-      <style:paragraph-properties style:text-autospace="ideograph-alpha" style:line-break="strict" style:writing-mode="lr-tb" style:font-independent-line-spacing="false">
+      <style:paragraph-properties style:text-autospace="ideograph-alpha" style:line-break="strict" style:font-independent-line-spacing="false">
         <style:tab-stops/>
       </style:paragraph-properties>
-      <style:text-properties style:use-window-font-color="true" loext:opacity="0%" style:font-name="Nimbus Roman No9 L" fo:font-size="12pt" fo:language="en" fo:country="US" style:letter-kerning="true" style:font-name-asian="DejaVu Sans" style:font-size-asian="10.5pt" style:language-asian="zh" style:country-asian="CN" style:font-name-complex="DejaVu Sans" style:font-size-complex="12pt" style:language-complex="hi" style:country-complex="IN"/>
+      <style:text-properties style:use-window-font-color="true" loext:opacity="0%" loext:color-lum-mod="100%" loext:color-lum-off="0%" style:font-name="Nimbus Roman No9 L" fo:font-size="12pt" fo:language="en" fo:country="US" style:letter-kerning="true" style:font-name-asian="DejaVu Sans" style:font-size-asian="10.5pt" style:language-asian="zh" style:country-asian="CN" style:font-name-complex="DejaVu Sans" style:font-size-complex="12pt" style:language-complex="hi" style:country-complex="IN"/>
     </style:default-style>
     <style:default-style style:family="paragraph">
       <style:paragraph-properties fo:orphans="2" fo:widows="2" fo:hyphenation-ladder-count="no-limit" style:text-autospace="ideograph-alpha" style:punctuation-wrap="hanging" style:line-break="strict" style:tab-stop-distance="0.4925in" style:writing-mode="page"/>
-      <style:text-properties style:use-window-font-color="true" loext:opacity="0%" style:font-name="Nimbus Roman No9 L" fo:font-size="12pt" fo:language="en" fo:country="US" style:letter-kerning="true" style:font-name-asian="DejaVu Sans" style:font-size-asian="10.5pt" style:language-asian="zh" style:country-asian="CN" style:font-name-complex="DejaVu Sans" style:font-size-complex="12pt" style:language-complex="hi" style:country-complex="IN" fo:hyphenate="false" fo:hyphenation-remain-char-count="2" fo:hyphenation-push-char-count="2" loext:hyphenation-no-caps="false"/>
+      <style:text-properties style:use-window-font-color="true" loext:opacity="0%" style:font-name="Nimbus Roman No9 L" fo:font-size="12pt" fo:language="en" fo:country="US" style:letter-kerning="true" style:font-name-asian="DejaVu Sans" style:font-size-asian="10.5pt" style:language-asian="zh" style:country-asian="CN" style:font-name-complex="DejaVu Sans" style:font-size-complex="12pt" style:language-complex="hi" style:country-complex="IN" fo:hyphenate="false" fo:hyphenation-remain-char-count="2" fo:hyphenation-push-char-count="2" loext:hyphenation-no-caps="false" loext:hyphenation-no-last-word="false" loext:hyphenation-word-char-count="5" loext:hyphenation-zone="no-limit"/>
     </style:default-style>
     <style:default-style style:family="table">
       <style:table-properties table:border-model="collapsing"/>
     </style:default-style>
     <style:default-style style:family="table-row">
       <style:table-row-properties fo:keep-together="auto"/>
     </style:default-style>
     <style:style style:name="Standard" style:family="paragraph" style:class="text">
       <style:text-properties style:font-name="Liberation Sans" fo:font-family="'Liberation Sans'" style:font-style-name="Regular" style:font-family-generic="swiss" style:font-pitch="variable" style:font-size-asian="10.5pt"/>
     </style:style>
     <style:style style:name="Heading" style:family="paragraph" style:parent-style-name="Standard" style:next-style-name="Text_20_body" style:class="text">
       <style:paragraph-properties fo:margin-top="0.1665in" fo:margin-bottom="0.0835in" style:contextual-spacing="false" fo:keep-with-next="always"/>
-      <style:text-properties style:font-name="Liberation Serif" fo:font-family="'Liberation Serif'" style:font-style-name="Regular" style:font-family-generic="roman" style:font-pitch="variable" fo:font-size="16pt" style:font-name-asian="DejaVu Sans" style:font-family-asian="'DejaVu Sans'" style:font-family-generic-asian="system" style:font-pitch-asian="variable" style:font-size-asian="14pt" style:font-name-complex="DejaVu Sans" style:font-family-complex="'DejaVu Sans'" style:font-family-generic-complex="system" style:font-pitch-complex="variable" style:font-size-complex="14pt"/>
+      <style:text-properties style:font-name="Liberation Serif1" fo:font-family="'Liberation Serif'" style:font-style-name="Regular" style:font-family-generic="roman" style:font-pitch="variable" fo:font-size="16pt" style:font-name-asian="DejaVu Sans" style:font-family-asian="'DejaVu Sans'" style:font-family-generic-asian="system" style:font-pitch-asian="variable" style:font-size-asian="14pt" style:font-name-complex="DejaVu Sans" style:font-family-complex="'DejaVu Sans'" style:font-family-generic-complex="system" style:font-pitch-complex="variable" style:font-size-complex="14pt"/>
     </style:style>
     <style:style style:name="Text_20_body" style:display-name="Text body" style:family="paragraph" style:parent-style-name="Standard" style:class="text">
       <style:paragraph-properties fo:margin-top="0in" fo:margin-bottom="0.0835in" style:contextual-spacing="false"/>
       <style:text-properties style:font-name="Liberation Sans" fo:font-family="'Liberation Sans'" style:font-style-name="Regular" style:font-family-generic="swiss" style:font-pitch="variable" style:font-size-asian="10.5pt"/>
     </style:style>
     <style:style style:name="List" style:family="paragraph" style:parent-style-name="Text_20_body" style:class="list">
       <style:text-properties style:font-size-asian="12pt"/>
@@ -200,15 +209,15 @@
     </style:style>
     <style:style style:name="Table_20_Contents" style:display-name="Table Contents" style:family="paragraph" style:parent-style-name="Standard" style:class="extra">
       <style:paragraph-properties text:number-lines="false" text:line-number="0"/>
       <style:text-properties style:font-size-asian="10.5pt"/>
     </style:style>
     <style:style style:name="Table_20_Heading" style:display-name="Table Heading" style:family="paragraph" style:parent-style-name="Table_20_Contents" style:class="extra">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false" text:number-lines="false" text:line-number="0"/>
-      <style:text-properties style:font-name="Liberation Serif1" fo:font-family="'Liberation Serif'" style:font-style-name="Bold" style:font-family-generic="roman" style:font-pitch="variable" fo:font-weight="bold" style:font-size-asian="10.5pt" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
+      <style:text-properties style:font-name="Liberation Serif" fo:font-family="'Liberation Serif'" style:font-style-name="Bold" style:font-family-generic="roman" style:font-pitch="variable" fo:font-weight="bold" style:font-size-asian="10.5pt" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="Header_20_and_20_Footer" style:display-name="Header and Footer" style:family="paragraph" style:parent-style-name="Standard" style:class="extra">
       <style:paragraph-properties text:number-lines="false" text:line-number="0">
         <style:tab-stops>
           <style:tab-stop style:position="3.3465in" style:type="center"/>
           <style:tab-stop style:position="6.6929in" style:type="right"/>
         </style:tab-stops>
@@ -281,42 +290,42 @@
     <style:style style:name="OLE" style:family="graphic">
       <style:graphic-properties text:anchor-type="paragraph" svg:x="0in" svg:y="0in" style:wrap="dynamic" style:number-wrapped-paragraphs="no-limit" style:wrap-contour="false" style:vertical-pos="top" style:vertical-rel="paragraph" style:horizontal-pos="center" style:horizontal-rel="paragraph"/>
     </style:style>
     <style:style style:name="Frame" style:family="graphic">
       <style:graphic-properties text:anchor-type="paragraph" svg:x="0in" svg:y="0in" fo:margin-left="0.0791in" fo:margin-right="0.0791in" fo:margin-top="0.0791in" fo:margin-bottom="0.0791in" style:wrap="parallel" style:number-wrapped-paragraphs="no-limit" style:wrap-contour="false" style:vertical-pos="top" style:vertical-rel="paragraph-content" style:horizontal-pos="center" style:horizontal-rel="paragraph-content" fo:padding="0.0591in" fo:border="0.06pt solid #000000"/>
     </style:style>
     <text:outline-style style:name="Outline">
-      <text:outline-level-style text:level="1" style:num-format="">
+      <text:outline-level-style text:level="1" loext:num-list-format="%1%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
-      <text:outline-level-style text:level="2" style:num-format="">
+      <text:outline-level-style text:level="2" loext:num-list-format="%2%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
-      <text:outline-level-style text:level="3" style:num-format="">
+      <text:outline-level-style text:level="3" loext:num-list-format="%3%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
-      <text:outline-level-style text:level="4" style:num-format="">
+      <text:outline-level-style text:level="4" loext:num-list-format="%4%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
-      <text:outline-level-style text:level="5" style:num-format="">
+      <text:outline-level-style text:level="5" loext:num-list-format="%5%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
-      <text:outline-level-style text:level="6" style:num-format="">
+      <text:outline-level-style text:level="6" loext:num-list-format="%6%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
-      <text:outline-level-style text:level="7" style:num-format="">
+      <text:outline-level-style text:level="7" loext:num-list-format="%7%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
-      <text:outline-level-style text:level="8" style:num-format="">
+      <text:outline-level-style text:level="8" loext:num-list-format="%8%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
-      <text:outline-level-style text:level="9" style:num-format="">
+      <text:outline-level-style text:level="9" loext:num-list-format="%9%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
-      <text:outline-level-style text:level="10" style:num-format="">
+      <text:outline-level-style text:level="10" loext:num-list-format="%10%" style:num-format="">
         <style:list-level-properties text:min-label-distance="0.15in"/>
       </text:outline-level-style>
     </text:outline-style>
     <text:notes-configuration text:note-class="footnote" style:num-format="1" text:start-value="0" text:footnotes-position="page" text:start-numbering-at="document"/>
     <text:notes-configuration text:note-class="endnote" style:num-format="i" text:start-value="0"/>
     <text:linenumbering-configuration text:number-lines="false" text:offset="0.1965in" style:num-format="1" text:number-position="left" text:increment="5"/>
   </office:styles>
@@ -357,104 +366,104 @@
     </style:style>
     <style:style style:name="P1" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
     </style:style>
     <style:style style:name="P2" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="Cantarell"/>
     </style:style>
-    <style:style style:name="P3" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P3" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P4" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
+      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="002b9d98" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P5" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
+      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="002ae9ba" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    </style:style>
+    <style:style style:name="P6" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
+    </style:style>
+    <style:style style:name="P7" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
+    </style:style>
+    <style:style style:name="P8" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:line-height="150%"/>
+      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" officeooo:paragraph-rsid="002771e8" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
+    </style:style>
+    <style:style style:name="P9" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P4" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P10" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:line-height="150%"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" officeooo:paragraph-rsid="00238dc6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P5" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P11" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:line-height="150%" fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="6pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" officeooo:paragraph-rsid="00359bff" style:font-size-asian="6pt" style:font-weight-asian="normal" style:font-size-complex="6pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P6" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P12" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="6pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" officeooo:paragraph-rsid="00359bff" style:font-size-asian="6pt" style:font-weight-asian="normal" style:font-size-complex="6pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P7" style:family="paragraph" style:parent-style-name="Frame_20_contents">
-      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
-    </style:style>
-    <style:style style:name="P8" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#dc2300" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="13pt" fo:font-weight="bold" style:font-size-asian="13pt" style:font-weight-asian="bold" style:font-size-complex="13pt" style:font-weight-complex="bold"/>
+    <style:style style:name="P13" style:family="paragraph" style:parent-style-name="Standard">
+      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="6pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" officeooo:paragraph-rsid="00359bff" style:font-size-asian="6pt" style:font-weight-asian="normal" style:font-size-complex="6pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P9" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    <style:style style:name="P14" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:line-height="150%" fo:text-align="start" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="6pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" officeooo:paragraph-rsid="00359bff" style:font-size-asian="6pt" style:font-weight-asian="normal" style:font-size-complex="6pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P10" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
-      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="002b9d98" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    <style:style style:name="P15" style:family="paragraph" style:parent-style-name="Standard">
+      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P11" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
-      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="002ae9ba" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
+    <style:style style:name="P16" style:family="paragraph" style:parent-style-name="Standard">
+      <style:paragraph-properties fo:line-height="150%"/>
+      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" officeooo:paragraph-rsid="00238dc6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
     </style:style>
-    <style:style style:name="P12" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
+    <style:style style:name="P17" style:family="paragraph" style:parent-style-name="Frame_20_contents">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
     </style:style>
-    <style:style style:name="P13" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
-      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
+    <style:style style:name="P18" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#dc2300" loext:opacity="100%" style:font-name="Cantarell" fo:font-size="13pt" fo:font-weight="bold" style:font-size-asian="13pt" style:font-weight-asian="bold" style:font-size-complex="13pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P14" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:line-height="150%"/>
-      <style:text-properties style:font-name="Cantarell" fo:font-size="10pt" officeooo:paragraph-rsid="002771e8" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
+    <style:style style:name="P19" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
+      <style:text-properties fo:color="#dc2300" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="13pt" fo:font-weight="bold" style:font-size-asian="13pt" style:font-weight-asian="bold" style:font-size-complex="13pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P15" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P20" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P16" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P21" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="center" style:justify-single-word="false"/>
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="002ae9ba" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P17" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P22" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="bold" officeooo:paragraph-rsid="002b9d98" style:font-size-asian="10pt" style:font-weight-asian="bold" style:font-size-complex="10pt" style:font-weight-complex="bold"/>
     </style:style>
-    <style:style style:name="P18" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P23" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P19" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P24" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:line-height="150%"/>
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" officeooo:paragraph-rsid="002771e8" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P20" style:family="paragraph" style:parent-style-name="Table_20_Contents">
+    <style:style style:name="P25" style:family="paragraph" style:parent-style-name="Table_20_Contents">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties style:font-name="FreeSans" fo:font-size="10pt" style:font-size-asian="10pt" style:font-size-complex="10pt"/>
     </style:style>
-    <style:style style:name="P21" style:family="paragraph" style:parent-style-name="Table_20_Contents">
-      <style:paragraph-properties fo:text-align="end" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#dc2300" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="13pt" fo:font-weight="bold" style:font-size-asian="13pt" style:font-weight-asian="bold" style:font-size-complex="13pt" style:font-weight-complex="bold"/>
-    </style:style>
-    <style:style style:name="P22" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P26" style:family="paragraph" style:parent-style-name="Standard">
       <style:text-properties style:font-name="FreeSans"/>
     </style:style>
-    <style:style style:name="P23" style:family="paragraph" style:parent-style-name="Standard">
+    <style:style style:name="P27" style:family="paragraph" style:parent-style-name="Standard">
       <style:paragraph-properties fo:text-align="start" style:justify-single-word="false"/>
       <style:text-properties style:font-name="FreeSans"/>
     </style:style>
-    <style:style style:name="P24" style:family="paragraph" style:parent-style-name="Standard">
-      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="6pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" officeooo:paragraph-rsid="00359bff" style:font-size-asian="6pt" style:font-weight-asian="normal" style:font-size-complex="6pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P25" style:family="paragraph" style:parent-style-name="Standard">
-      <style:paragraph-properties fo:line-height="150%" fo:text-align="start" style:justify-single-word="false"/>
-      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="6pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" officeooo:paragraph-rsid="00359bff" style:font-size-asian="6pt" style:font-weight-asian="normal" style:font-size-complex="6pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P26" style:family="paragraph" style:parent-style-name="Standard">
-      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
-    </style:style>
-    <style:style style:name="P27" style:family="paragraph" style:parent-style-name="Standard">
-      <style:paragraph-properties fo:line-height="150%"/>
-      <style:text-properties fo:color="#000080" loext:opacity="100%" style:font-name="FreeSans" fo:font-size="10pt" fo:font-weight="normal" officeooo:rsid="0003fe3b" officeooo:paragraph-rsid="00238dc6" style:font-size-asian="10pt" style:font-weight-asian="normal" style:font-size-complex="10pt" style:font-weight-complex="normal"/>
-    </style:style>
     <style:style style:name="T1" style:family="text">
       <style:text-properties fo:font-weight="bold" style:font-weight-asian="bold" style:font-weight-complex="bold"/>
     </style:style>
     <style:style style:name="T2" style:family="text">
       <style:text-properties officeooo:rsid="002ae9ba"/>
     </style:style>
     <style:style style:name="T3" style:family="text">
@@ -477,27 +486,30 @@
     </style:style>
     <style:style style:name="fr2" style:family="graphic" style:parent-style-name="Frame">
       <style:graphic-properties style:print-content="true" style:protect="none" style:wrap="none" style:vertical-pos="from-top" style:vertical-rel="paragraph" style:horizontal-pos="from-left" style:horizontal-rel="paragraph" fo:background-color="transparent" draw:fill="none" draw:fill-color="#ffffff" fo:padding="0in" fo:border="none" style:shadow="none" draw:shadow-opacity="100%">
         <style:columns fo:column-count="1" fo:column-gap="0in"/>
       </style:graphic-properties>
     </style:style>
     <style:page-layout style:name="pm1">
-      <style:page-layout-properties fo:page-width="8.5in" fo:page-height="11in" style:num-format="1" style:print-orientation="portrait" fo:margin-top="0.7874in" fo:margin-bottom="0.7874in" fo:margin-left="0.7874in" fo:margin-right="0.7874in" style:writing-mode="lr-tb" style:layout-grid-color="#c0c0c0" style:layout-grid-lines="44" style:layout-grid-base-height="0.2165in" style:layout-grid-ruby-height="0in" style:layout-grid-mode="none" style:layout-grid-ruby-below="false" style:layout-grid-print="true" style:layout-grid-display="true" style:footnote-max-height="0in">
+      <style:page-layout-properties fo:page-width="8.5in" fo:page-height="11in" style:num-format="1" style:print-orientation="portrait" fo:margin-top="0.7874in" fo:margin-bottom="0.7874in" fo:margin-left="0.7874in" fo:margin-right="0.7874in" style:writing-mode="lr-tb" style:layout-grid-color="#c0c0c0" style:layout-grid-lines="44" style:layout-grid-base-height="0.2165in" style:layout-grid-ruby-height="0in" style:layout-grid-mode="none" style:layout-grid-ruby-below="false" style:layout-grid-print="true" style:layout-grid-display="true" style:footnote-max-height="0in" loext:margin-gutter="0in">
         <style:footnote-sep style:width="0.0071in" style:distance-before-sep="0.0398in" style:distance-after-sep="0.0398in" style:line-style="none" style:adjustment="left" style:rel-width="25%" style:color="#000000"/>
       </style:page-layout-properties>
       <style:header-style>
         <style:header-footer-properties fo:min-height="0in" fo:margin-left="0in" fo:margin-right="0in" fo:margin-bottom="0.1965in"/>
       </style:header-style>
       <style:footer-style>
         <style:header-footer-properties fo:min-height="0in" fo:margin-left="0in" fo:margin-right="0in" fo:margin-top="0.1965in"/>
       </style:footer-style>
     </style:page-layout>
+    <style:style style:name="dp1" style:family="drawing-page">
+      <style:drawing-page-properties draw:background-size="full"/>
+    </style:style>
   </office:automatic-styles>
   <office:master-styles>
-    <style:master-page style:name="Standard" style:page-layout-name="pm1">
+    <style:master-page style:name="Standard" style:page-layout-name="pm1" draw:style-name="dp1">
       <style:header>
         <text:p text:style-name="Standard"/>
       </style:header>
       <style:footer>
         <text:p text:style-name="Standard"/>
       </style:footer>
     </style:master-page>
@@ -508,101 +520,101 @@
       <text:sequence-decls>
         <text:sequence-decl text:display-outline-level="0" text:name="Illustration"/>
         <text:sequence-decl text:display-outline-level="0" text:name="Table"/>
         <text:sequence-decl text:display-outline-level="0" text:name="Text"/>
         <text:sequence-decl text:display-outline-level="0" text:name="Drawing"/>
         <text:sequence-decl text:display-outline-level="0" text:name="Figure"/>
       </text:sequence-decls>
-      <text:p text:style-name="P22"/>
-      <text:p text:style-name="P22"/>
-      <text:p text:style-name="P22">
+      <text:p text:style-name="P26"/>
+      <text:p text:style-name="P26"/>
+      <text:p text:style-name="P26">
         <text:placeholder text:placeholder-type="text">&lt;for each=&quot;patient in records&quot;&gt;</text:placeholder>
       </text:p>
       <table:table table:name="Tabla1" table:style-name="Tabla1">
         <table:table-column table:style-name="Tabla1.A"/>
         <table:table-column table:style-name="Tabla1.B"/>
         <table:table-column table:style-name="Tabla1.C"/>
         <table:table-row table:style-name="Tabla1.1">
           <table:table-cell table:style-name="Tabla1.A1" office:value-type="string">
-            <text:p text:style-name="P24">
+            <text:p text:style-name="P13">
               <text:placeholder text:placeholder-type="text">&lt;if test=&quot;patient.photo&quot;&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P24">
+            <text:p text:style-name="P13">
               <draw:frame draw:style-name="fr2" draw:name="image: (patient.photo, 'image/png','3cm','3cm')" text:anchor-type="paragraph" svg:x="0.0646in" svg:y="0.2102in" svg:width="0.6791in" svg:height="0.178in" draw:z-index="0">
                 <draw:text-box>
                   <text:p text:style-name="Frame_20_contents"/>
                 </draw:text-box>
               </draw:frame>
             </text:p>
-            <text:p text:style-name="P24"/>
-            <text:p text:style-name="P24"/>
-            <text:p text:style-name="P25"/>
-            <text:p text:style-name="P25">
+            <text:p text:style-name="P13"/>
+            <text:p text:style-name="P13"/>
+            <text:p text:style-name="P14"/>
+            <text:p text:style-name="P14">
               <text:placeholder text:placeholder-type="text">&lt;/if&gt;</text:placeholder>
             </text:p>
           </table:table-cell>
           <table:table-cell table:style-name="Tabla1.B1" office:value-type="string">
-            <text:p text:style-name="P15"/>
-            <text:p text:style-name="P18">
+            <text:p text:style-name="P20"/>
+            <text:p text:style-name="P23">
               <text:span text:style-name="T1">Name</text:span>
               :
               <text:placeholder text:placeholder-type="text">&lt;patient.rec_name&gt;</text:placeholder>
               <text:s/>
             </text:p>
-            <text:p text:style-name="P18"/>
-            <text:p text:style-name="P26">
+            <text:p text:style-name="P23"/>
+            <text:p text:style-name="P15">
               <text:placeholder text:placeholder-type="text">&lt;if test=&quot;patient.dob&quot;&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P19">
+            <text:p text:style-name="P24">
               <text:span text:style-name="T5">DoB:</text:span>
               <text:span text:style-name="T7"/>
               <text:span text:style-name="T6">
                 <text:placeholder text:placeholder-type="text">&lt;format_date(patient.dob, user.language)&gt;</text:placeholder>
               </text:span>
             </text:p>
-            <text:p text:style-name="P27">
+            <text:p text:style-name="P16">
               <text:placeholder text:placeholder-type="text">&lt;/if&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P22"/>
-            <text:p text:style-name="P18">
+            <text:p text:style-name="P26"/>
+            <text:p text:style-name="P23">
               <text:span text:style-name="T4">Blood Type</text:span>
               <text:span text:style-name="T3">:</text:span>
               <text:placeholder text:placeholder-type="text">&lt;patient.blood_type&gt;</text:placeholder>
               <text:s/>
               <text:placeholder text:placeholder-type="text">&lt;patient.rh&gt;</text:placeholder>
             </text:p>
-            <text:p text:style-name="P20">
+            <text:p text:style-name="P25">
               <text:s/>
             </text:p>
           </table:table-cell>
           <table:table-cell table:style-name="Tabla1.C1" office:value-type="string">
-            <text:p text:style-name="P21">
+            <text:p text:style-name="P19">
               <draw:frame draw:style-name="fr1" draw:name="image: (patient.qr, 'image/png','3cm','3cm')" text:anchor-type="paragraph" svg:x="0.0992in" svg:y="0.0717in" svg:width="0.7874in" draw:z-index="1">
                 <draw:text-box fo:min-height="0.1965in">
-                  <text:p text:style-name="P7"/>
+                  <text:p text:style-name="P17"/>
                 </draw:text-box>
               </draw:frame>
             </text:p>
-            <text:p text:style-name="P21"/>
+            <text:p text:style-name="P19"/>
           </table:table-cell>
         </table:table-row>
-        <table:table-row table:style-name="TableLine94743752995328">
+        <table:table-row>
           <table:table-cell table:style-name="Tabla1.A2" office:value-type="string">
-            <text:p text:style-name="P16">
+            <text:p text:style-name="P21">
               <text:span text:style-name="T2">ID</text:span>
               <text:placeholder text:placeholder-type="text">&lt;patient.puid&gt;</text:placeholder>
             </text:p>
           </table:table-cell>
           <table:table-cell table:style-name="Tabla1.B2" table:number-columns-spanned="2" office:value-type="string">
-            <text:p text:style-name="P17">
-              <text:placeholder text:placeholder-type="text">&lt;patient.gender&gt;</text:placeholder>
+            <text:p text:style-name="P22">
+              <text:placeholder text:placeholder-type="text">&lt;patient.name.gender_str&gt;</text:placeholder>
             </text:p>
           </table:table-cell>
           <table:covered-table-cell/>
         </table:table-row>
       </table:table>
-      <text:p text:style-name="P23">
+      <text:p text:style-name="P27">
         <text:placeholder text:placeholder-type="text">&lt;/for&gt;</text:placeholder>
       </text:p>
     </office:text>
   </office:body>
 </office:document>
```

### Comparing `gnuhealth_qrcodes-4.2.0/setup.py` & `gnuhealth_qrcodes-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/tests/test_health_qrcodes.py` & `gnuhealth_qrcodes-4.2.1/tests/test_health_qrcodes.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_qrcodes-4.2.0/view/lab_form.xml` & `gnuhealth_qrcodes-4.2.1/view/lab_form.xml`

 * *Files identical despite different names*

