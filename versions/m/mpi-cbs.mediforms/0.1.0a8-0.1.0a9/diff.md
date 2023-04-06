# Comparing `tmp/mpi-cbs.mediforms-0.1.0a8.tar.gz` & `tmp/mpi-cbs.mediforms-0.1.0a9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "mpi-cbs.mediforms-0.1.0a8.tar", last modified: Thu Mar 30 10:27:02 2023, max compression
+gzip compressed data, was "mpi-cbs.mediforms-0.1.0a9.tar", last modified: Thu Mar 30 10:30:14 2023, max compression
```

## Comparing `mpi-cbs.mediforms-0.1.0a8.tar` & `mpi-cbs.mediforms-0.1.0a9.tar`

### file list

```diff
@@ -1,77 +1,77 @@
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.759906 mpi-cbs.mediforms-0.1.0a8/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)       65 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/MANIFEST.in
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      972 2023-03-30 10:27:02.759906 mpi-cbs.mediforms-0.1.0a8/PKG-INFO
--rw-rw-r--   0 lotus     (1000) lotus     (1000)       12 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/README.md
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.751906 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.755905 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      166 2023-03-30 10:26:38.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/__init__.py
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     1996 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/admin.py
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      189 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/apps.py
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     8166 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/forms.py
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.751906 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.751906 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/de/
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.755905 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/de/LC_MESSAGES/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     8039 2023-03-30 10:22:11.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/de/LC_MESSAGES/django.mo
--rw-rw-r--   0 lotus     (1000) lotus     (1000)   126361 2023-03-30 10:22:09.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/de/LC_MESSAGES/django.po
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.751906 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/en/
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.755905 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/en/LC_MESSAGES/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)   141359 2023-03-30 10:22:11.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/en/LC_MESSAGES/django.mo
--rw-rw-r--   0 lotus     (1000) lotus     (1000)   188265 2023-03-30 10:22:09.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/en/LC_MESSAGES/django.po
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.755905 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/migrations/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)    48474 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/migrations/0001_initial.py
--rw-rw-r--   0 lotus     (1000) lotus     (1000)        0 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/migrations/__init__.py
--rw-rw-r--   0 lotus     (1000) lotus     (1000)    11480 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/models.py
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.751906 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.755905 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      723 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/base.html
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.755905 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     8773 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/data_storage_and_usage_consent_mrt.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     2444 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/data_storage_and_usage_consent_mrtbegleitung.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3929 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrt.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3848 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrt7tptx.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3313 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrtbegleitung.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3832 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrtconnectom.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     4067 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_tms.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     7787 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrt.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)    19683 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrt7tptx.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     7095 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrtbegleitung.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)    13735 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrtconnectom.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)    13558 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_tms.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     2068 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/iup.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      317 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/index.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      230 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/login.html
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.759906 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      738 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/base.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      218 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/data_storage_and_usage_consent_mrt.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      228 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/data_storage_and_usage_consent_mrtbegleitung.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3669 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/data_storage_consent.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      257 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/exploration_consent.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     5230 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      939 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_complete.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     5369 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_mrt.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     4926 2023-03-30 09:57:15.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_mrt7tptx.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     4795 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_mrtbegleitung.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3772 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_mrtconnectom.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     4912 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_tms.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      254 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/information_text.html
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.759906 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3655 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/mrt.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3647 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/mrt7tptx.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3618 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/mrtbegleitung.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3660 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/mrtconnectom.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      332 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/pdf.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     4009 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/tms.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      636 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/token_list.html
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.759906 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/widgets/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      367 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/widgets/radio_select.html
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     1960 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/urls.py
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     7502 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/views.py
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      123 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/widgets.py
-drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:27:02.751906 mpi-cbs.mediforms-0.1.0a8/mpi_cbs.mediforms.egg-info/
--rw-rw-r--   0 lotus     (1000) lotus     (1000)      972 2023-03-30 10:27:02.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs.mediforms.egg-info/PKG-INFO
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     3241 2023-03-30 10:27:02.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs.mediforms.egg-info/SOURCES.txt
--rw-rw-r--   0 lotus     (1000) lotus     (1000)        1 2023-03-30 10:27:02.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs.mediforms.egg-info/dependency_links.txt
--rw-rw-r--   0 lotus     (1000) lotus     (1000)       87 2023-03-30 10:27:02.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs.mediforms.egg-info/requires.txt
--rw-rw-r--   0 lotus     (1000) lotus     (1000)        8 2023-03-30 10:27:02.000000 mpi-cbs.mediforms-0.1.0a8/mpi_cbs.mediforms.egg-info/top_level.txt
--rw-rw-r--   0 lotus     (1000) lotus     (1000)       38 2023-03-30 10:27:02.759906 mpi-cbs.mediforms-0.1.0a8/setup.cfg
--rw-rw-r--   0 lotus     (1000) lotus     (1000)     1513 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a8/setup.py
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.316664 mpi-cbs.mediforms-0.1.0a9/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)       65 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/MANIFEST.in
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      972 2023-03-30 10:30:14.316664 mpi-cbs.mediforms-0.1.0a9/PKG-INFO
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)       12 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/README.md
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.308664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.308664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      166 2023-03-30 10:29:44.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/__init__.py
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     1996 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/admin.py
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      189 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/apps.py
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     8166 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/forms.py
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.308664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.308664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/de/
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.308664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/de/LC_MESSAGES/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     8039 2023-03-30 10:29:00.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/de/LC_MESSAGES/django.mo
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)   126361 2023-03-30 10:28:47.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/de/LC_MESSAGES/django.po
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.308664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/en/
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.308664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/en/LC_MESSAGES/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)   141696 2023-03-30 10:29:00.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/en/LC_MESSAGES/django.mo
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)   188425 2023-03-30 10:28:48.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/en/LC_MESSAGES/django.po
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.312664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/migrations/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)    48474 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/migrations/0001_initial.py
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)        0 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/migrations/__init__.py
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)    11480 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/models.py
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.308664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.312664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      723 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/base.html
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.312664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     8773 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/data_storage_and_usage_consent_mrt.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     2444 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/data_storage_and_usage_consent_mrtbegleitung.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3929 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrt.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3848 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrt7tptx.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3313 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrtbegleitung.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3832 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrtconnectom.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     4067 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_tms.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     7787 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrt.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)    19683 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrt7tptx.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     7095 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrtbegleitung.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)    13735 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrtconnectom.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)    13558 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_tms.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     2068 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/iup.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      317 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/index.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      230 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/login.html
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.312664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      738 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/base.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      218 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/data_storage_and_usage_consent_mrt.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      228 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/data_storage_and_usage_consent_mrtbegleitung.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3669 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/data_storage_consent.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      257 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/exploration_consent.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     5230 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      939 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_complete.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     5369 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_mrt.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     4926 2023-03-30 09:57:15.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_mrt7tptx.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     4795 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_mrtbegleitung.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3772 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_mrtconnectom.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     4912 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_tms.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      254 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/information_text.html
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.316664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3655 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/mrt.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3647 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/mrt7tptx.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3618 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/mrtbegleitung.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3660 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/mrtconnectom.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      332 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/pdf.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     4009 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/tms.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      636 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/token_list.html
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.316664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/widgets/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      367 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/widgets/radio_select.html
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     1960 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/urls.py
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     7502 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/views.py
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      123 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/widgets.py
+drwxrwxr-x   0 lotus     (1000) lotus     (1000)        0 2023-03-30 10:30:14.308664 mpi-cbs.mediforms-0.1.0a9/mpi_cbs.mediforms.egg-info/
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)      972 2023-03-30 10:30:14.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs.mediforms.egg-info/PKG-INFO
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     3241 2023-03-30 10:30:14.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs.mediforms.egg-info/SOURCES.txt
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)        1 2023-03-30 10:30:14.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs.mediforms.egg-info/dependency_links.txt
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)       87 2023-03-30 10:30:14.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs.mediforms.egg-info/requires.txt
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)        8 2023-03-30 10:30:14.000000 mpi-cbs.mediforms-0.1.0a9/mpi_cbs.mediforms.egg-info/top_level.txt
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)       38 2023-03-30 10:30:14.316664 mpi-cbs.mediforms-0.1.0a9/setup.cfg
+-rw-rw-r--   0 lotus     (1000) lotus     (1000)     1513 2023-03-30 08:47:05.000000 mpi-cbs.mediforms-0.1.0a9/setup.py
```

### Comparing `mpi-cbs.mediforms-0.1.0a8/PKG-INFO` & `mpi-cbs.mediforms-0.1.0a9/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mpi-cbs.mediforms
-Version: 0.1.0a8
+Version: 0.1.0a9
 Summary: UNKNOWN
 Home-page: https://bitbucket.org/huscy/mediforms
 Author: Stefan Bunde
 Author-email: stefanbunde+git@posteo.de
 License: AGPLv3+
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/admin.py` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/admin.py`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/forms.py` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/forms.py`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/de/LC_MESSAGES/django.mo` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/de/LC_MESSAGES/django.mo`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/de/LC_MESSAGES/django.po` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/de/LC_MESSAGES/django.po`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/en/LC_MESSAGES/django.mo` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/en/LC_MESSAGES/django.mo`

 * *Files 1% similar despite different names*

#### msgunfmt {}

```diff
@@ -1805,14 +1805,23 @@
 msgid ""
 "Magnetresonanz-Untersuchung bei 7 Tesla unter Verwendung paralleler "
 "Sendetechniken (pTx)"
 msgstr ""
 "Magnetic Resonance Imaging Study at 7 Tesla using parallel transmission "
 "techniques"
 
+msgid ""
+"Magnetresonanz-Untersuchung bei 7 Tesla unter Verwendung paralleler "
+"Sendetechniken (pTx) am Max-Planck-Institut für Kognitions- und "
+"Neurowissenschaften (MPI CBS)"
+msgstr ""
+"Magnetic Resonance Examination at 7 Tesla using parallel transmission "
+"techniques at the Max Planck Institute for Human Cognitive and Brain "
+"Sciences (MPI CBS)"
+
 msgid "Magnetresonanz-Untersuchung für Begleitpersonen"
 msgstr "Magnetic Resonance Examination for accompanying persons"
 
 msgid ""
 "Magnetresonanz-Untersuchung für Begleitpersonen am Max-Planck-Institut für "
 "Kognitions- und Neurowissenschaften (MPI CBS)"
 msgstr ""
```

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/locale/en/LC_MESSAGES/django.po` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/locale/en/LC_MESSAGES/django.po`

 * *Files 0% similar despite different names*

```diff
@@ -3266,14 +3266,15 @@
 
 #: mpi_cbs/mediforms/templates/mediforms/pages/form_mrt7tptx.html:7
 msgid ""
 "Magnetresonanz-Untersuchung bei 7 Tesla unter Verwendung paralleler "
 "Sendetechniken (pTx) am Max-Planck-Institut für Kognitions- und "
 "Neurowissenschaften (MPI CBS)"
 msgstr ""
+"Magnetic Resonance Examination at 7 Tesla using parallel transmission techniques at the Max Planck Institute for Human Cognitive and Brain Sciences (MPI CBS)"
 
 #: mpi_cbs/mediforms/templates/mediforms/pages/form_mrt7tptx.html:19
 msgid ""
 "<b>Einwilligungserklärung zur Magnetresonanz-Untersuchung bei 7 Tesla pTx</"
 "b> und <b>Erklärung zur Speicherung und Nutzung von Daten</b> (Dauer: 4 "
 "Minuten)."
 msgstr ""
```

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/migrations/0001_initial.py` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/migrations/0001_initial.py`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/models.py` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/models.py`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/base.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/base.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/data_storage_and_usage_consent_mrt.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/data_storage_and_usage_consent_mrt.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/data_storage_and_usage_consent_mrtbegleitung.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/data_storage_and_usage_consent_mrtbegleitung.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrt.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrt.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrt7tptx.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrt7tptx.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrtbegleitung.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrtbegleitung.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrtconnectom.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_mrtconnectom.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_tms.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/exploration_consent_tms.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrt.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrt.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrt7tptx.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrt7tptx.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrtbegleitung.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrtbegleitung.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrtconnectom.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_mrtconnectom.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/information_text_tms.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/information_text_tms.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/includes/iup.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/includes/iup.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/base.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/base.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/data_storage_consent.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/data_storage_consent.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_complete.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_complete.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_mrt.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_mrt.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_mrt7tptx.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_mrt7tptx.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_mrtbegleitung.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_mrtbegleitung.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_mrtconnectom.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_mrtconnectom.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pages/form_tms.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pages/form_tms.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/mrt.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/mrt.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/mrt7tptx.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/mrt7tptx.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/mrtbegleitung.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/mrtbegleitung.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/mrtconnectom.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/mrtconnectom.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/pdfs/tms.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/pdfs/tms.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/templates/mediforms/token_list.html` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/templates/mediforms/token_list.html`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/urls.py` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/urls.py`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs/mediforms/views.py` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs/mediforms/views.py`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs.mediforms.egg-info/PKG-INFO` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs.mediforms.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: mpi-cbs.mediforms
-Version: 0.1.0a8
+Version: 0.1.0a9
 Summary: UNKNOWN
 Home-page: https://bitbucket.org/huscy/mediforms
 Author: Stefan Bunde
 Author-email: stefanbunde+git@posteo.de
 License: AGPLv3+
 Platform: UNKNOWN
 Classifier: Development Status :: 5 - Production/Stable
```

### Comparing `mpi-cbs.mediforms-0.1.0a8/mpi_cbs.mediforms.egg-info/SOURCES.txt` & `mpi-cbs.mediforms-0.1.0a9/mpi_cbs.mediforms.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `mpi-cbs.mediforms-0.1.0a8/setup.py` & `mpi-cbs.mediforms-0.1.0a9/setup.py`

 * *Files identical despite different names*

