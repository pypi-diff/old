# Comparing `tmp/gnuhealth_calendar-4.2.0.tar.gz` & `tmp/gnuhealth_calendar-4.2.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "gnuhealth_calendar-4.2.0.tar", last modified: Sat Feb 11 21:55:08 2023, max compression
+gzip compressed data, was "gnuhealth_calendar-4.2.1.tar", last modified: Fri Apr  7 10:17:11 2023, max compression
```

## Comparing `gnuhealth_calendar-4.2.0.tar` & `gnuhealth_calendar-4.2.1.tar`

### file list

```diff
@@ -1,51 +1,51 @@
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.211636 gnuhealth_calendar-4.2.0/
--rw-r--r--   0 lfm       (1001) lfm       (1001)    35147 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.0/COPYING
--rw-r--r--   0 lfm       (1001) lfm       (1001)       54 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.0/MANIFEST.in
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5716 2023-02-11 21:55:08.211495 gnuhealth_calendar-4.2.0/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4826 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/README.rst
--rwxr-xr-x   0 lfm       (1001) lfm       (1001)     1163 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/__init__.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.208101 gnuhealth_calendar-4.2.0/data/
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.209118 gnuhealth_calendar-4.2.0/data/messages/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1242 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/data/messages/messages.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.209183 gnuhealth_calendar-4.2.0/doc/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      500 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/doc/index.rst
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1062 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/exceptions.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.211049 gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5716 2023-02-11 21:55:08.000000 gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/PKG-INFO
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1434 2023-02-11 21:55:08.000000 gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/SOURCES.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:08.000000 gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/dependency_links.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)       68 2023-02-11 21:55:08.000000 gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/entry_points.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        1 2023-02-11 21:55:08.000000 gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/not-zip-safe
--rw-r--r--   0 lfm       (1001) lfm       (1001)       35 2023-02-11 21:55:08.000000 gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/requires.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)        8 2023-02-11 21:55:08.000000 gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/top_level.txt
--rw-r--r--   0 lfm       (1001) lfm       (1001)     7710 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/health_calendar.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3077 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/health_calendar_view.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.209313 gnuhealth_calendar-4.2.0/icons/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4859 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.0/icons/calendar_icon.svg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     5225 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.0/icons/execute_icon.svg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.209971 gnuhealth_calendar-4.2.0/locale/
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4686 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/locale/ar.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4225 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/locale/de.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4822 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/locale/el.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4333 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.0/locale/es.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4384 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/locale/fr.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4307 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/locale/it_IT.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4456 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.0/locale/ja_JP.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3342 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/locale/lo.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4311 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/locale/pt_BR.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)     4511 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/locale/zh_CN.po
--rw-r--r--   0 lfm       (1001) lfm       (1001)       38 2023-02-11 21:55:08.211671 gnuhealth_calendar-4.2.0/setup.cfg
--rw-r--r--   0 lfm       (1001) lfm       (1001)     3343 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/setup.py
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.210099 gnuhealth_calendar-4.2.0/tests/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      827 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/tests/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1192 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/tests/test_health_calendar.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)      164 2023-02-11 12:44:33.000000 gnuhealth_calendar-4.2.0/tryton.cfg
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.210353 gnuhealth_calendar-4.2.0/view/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      356 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/view/gnuhealth_appointment_calendar.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      612 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/view/gnuhealth_calendar_appointment.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)      558 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/view/gnuhealth_calendar_user.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1292 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/view/gnuhealth_create_appointment_start_form.xml
-drwxr-xr-x   0 lfm       (1001) lfm       (1001)        0 2023-02-11 21:55:08.210545 gnuhealth_calendar-4.2.0/wizard/
--rw-r--r--   0 lfm       (1001) lfm       (1001)      893 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/wizard/__init__.py
--rw-r--r--   0 lfm       (1001) lfm       (1001)     1000 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/wizard/health_calendar_wizard.xml
--rw-r--r--   0 lfm       (1001) lfm       (1001)     6990 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.0/wizard/wizard_health_calendar.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.560776 gnuhealth_calendar-4.2.1/
+-rw-r--r--   0 lfm       (1001) wheel        (0)    35147 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.1/COPYING
+-rw-r--r--   0 lfm       (1001) wheel        (0)       54 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.1/MANIFEST.in
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5716 2023-04-07 10:17:11.560645 gnuhealth_calendar-4.2.1/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4826 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/README.rst
+-rwxr-xr-x   0 lfm       (1001) wheel        (0)     1163 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/__init__.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.557242 gnuhealth_calendar-4.2.1/data/
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.558404 gnuhealth_calendar-4.2.1/data/messages/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1242 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/data/messages/messages.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.558469 gnuhealth_calendar-4.2.1/doc/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      500 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/doc/index.rst
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1062 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/exceptions.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.560238 gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5716 2023-04-07 10:17:11.000000 gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/PKG-INFO
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1434 2023-04-07 10:17:11.000000 gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/SOURCES.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:11.000000 gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/dependency_links.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)       68 2023-04-07 10:17:11.000000 gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/entry_points.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        1 2023-04-07 10:17:11.000000 gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/not-zip-safe
+-rw-r--r--   0 lfm       (1001) wheel        (0)       35 2023-04-07 10:17:11.000000 gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/requires.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)        8 2023-04-07 10:17:11.000000 gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/top_level.txt
+-rw-r--r--   0 lfm       (1001) wheel        (0)     7710 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/health_calendar.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3077 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/health_calendar_view.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.558595 gnuhealth_calendar-4.2.1/icons/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4859 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.1/icons/calendar_icon.svg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     5225 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.1/icons/execute_icon.svg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.559232 gnuhealth_calendar-4.2.1/locale/
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4686 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/locale/ar.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4225 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/locale/de.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4822 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/locale/el.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4333 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.1/locale/es.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4384 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/locale/fr.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4307 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/locale/it_IT.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4456 2022-11-28 22:17:47.000000 gnuhealth_calendar-4.2.1/locale/ja_JP.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3342 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/locale/lo.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4311 2023-01-18 16:33:07.000000 gnuhealth_calendar-4.2.1/locale/pt_BR.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)     4511 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/locale/zh_CN.po
+-rw-r--r--   0 lfm       (1001) wheel        (0)       38 2023-04-07 10:17:11.560808 gnuhealth_calendar-4.2.1/setup.cfg
+-rw-r--r--   0 lfm       (1001) wheel        (0)     3343 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/setup.py
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.559355 gnuhealth_calendar-4.2.1/tests/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      827 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/tests/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1192 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/tests/test_health_calendar.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)      164 2023-04-07 09:37:21.000000 gnuhealth_calendar-4.2.1/tryton.cfg
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.559603 gnuhealth_calendar-4.2.1/view/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      356 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/view/gnuhealth_appointment_calendar.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      612 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/view/gnuhealth_calendar_appointment.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)      558 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/view/gnuhealth_calendar_user.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1292 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/view/gnuhealth_create_appointment_start_form.xml
+drwxr-xr-x   0 lfm       (1001) wheel        (0)        0 2023-04-07 10:17:11.559786 gnuhealth_calendar-4.2.1/wizard/
+-rw-r--r--   0 lfm       (1001) wheel        (0)      893 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/wizard/__init__.py
+-rw-r--r--   0 lfm       (1001) wheel        (0)     1000 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/wizard/health_calendar_wizard.xml
+-rw-r--r--   0 lfm       (1001) wheel        (0)     6990 2023-04-07 09:17:52.000000 gnuhealth_calendar-4.2.1/wizard/wizard_health_calendar.py
```

### Comparing `gnuhealth_calendar-4.2.0/COPYING` & `gnuhealth_calendar-4.2.1/COPYING`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/PKG-INFO` & `gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: gnuhealth_calendar
-Version: 4.2.0
+Name: gnuhealth-calendar
+Version: 4.2.1
 Summary: GNU Health Calendar with Caldav support
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_calendar-4.2.0/README.rst` & `gnuhealth_calendar-4.2.1/README.rst`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/__init__.py` & `gnuhealth_calendar-4.2.1/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/data/messages/messages.xml` & `gnuhealth_calendar-4.2.1/data/messages/messages.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/exceptions.py` & `gnuhealth_calendar-4.2.1/exceptions.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/PKG-INFO` & `gnuhealth_calendar-4.2.1/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
-Name: gnuhealth-calendar
-Version: 4.2.0
+Name: gnuhealth_calendar
+Version: 4.2.1
 Summary: GNU Health Calendar with Caldav support
 Home-page: https://www.gnuhealth.org
 Download-URL: http://ftp.gnu.org/gnu/health/
 Author: GNU Solidario
 Author-email: health@gnusolidario.org
 License: GPL-3
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `gnuhealth_calendar-4.2.0/gnuhealth_calendar.egg-info/SOURCES.txt` & `gnuhealth_calendar-4.2.1/gnuhealth_calendar.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/health_calendar.py` & `gnuhealth_calendar-4.2.1/health_calendar.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/health_calendar_view.xml` & `gnuhealth_calendar-4.2.1/health_calendar_view.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/icons/calendar_icon.svg` & `gnuhealth_calendar-4.2.1/icons/calendar_icon.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/icons/execute_icon.svg` & `gnuhealth_calendar-4.2.1/icons/execute_icon.svg`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/ar.po` & `gnuhealth_calendar-4.2.1/locale/ar.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/de.po` & `gnuhealth_calendar-4.2.1/locale/de.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/el.po` & `gnuhealth_calendar-4.2.1/locale/el.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/es.po` & `gnuhealth_calendar-4.2.1/locale/es.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/fr.po` & `gnuhealth_calendar-4.2.1/locale/fr.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/it_IT.po` & `gnuhealth_calendar-4.2.1/locale/it_IT.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/ja_JP.po` & `gnuhealth_calendar-4.2.1/locale/ja_JP.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/lo.po` & `gnuhealth_calendar-4.2.1/locale/lo.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/pt_BR.po` & `gnuhealth_calendar-4.2.1/locale/pt_BR.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/locale/zh_CN.po` & `gnuhealth_calendar-4.2.1/locale/zh_CN.po`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/setup.py` & `gnuhealth_calendar-4.2.1/setup.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/tests/__init__.py` & `gnuhealth_calendar-4.2.1/tests/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/tests/test_health_calendar.py` & `gnuhealth_calendar-4.2.1/tests/test_health_calendar.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/view/gnuhealth_calendar_appointment.xml` & `gnuhealth_calendar-4.2.1/view/gnuhealth_calendar_appointment.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/view/gnuhealth_calendar_user.xml` & `gnuhealth_calendar-4.2.1/view/gnuhealth_calendar_user.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/view/gnuhealth_create_appointment_start_form.xml` & `gnuhealth_calendar-4.2.1/view/gnuhealth_create_appointment_start_form.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/wizard/__init__.py` & `gnuhealth_calendar-4.2.1/wizard/__init__.py`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/wizard/health_calendar_wizard.xml` & `gnuhealth_calendar-4.2.1/wizard/health_calendar_wizard.xml`

 * *Files identical despite different names*

### Comparing `gnuhealth_calendar-4.2.0/wizard/wizard_health_calendar.py` & `gnuhealth_calendar-4.2.1/wizard/wizard_health_calendar.py`

 * *Files identical despite different names*

