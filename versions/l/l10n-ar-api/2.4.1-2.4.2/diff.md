# Comparing `tmp/l10n_ar_api-2.4.1.tar.gz` & `tmp/l10n_ar_api-2.4.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "l10n_ar_api-2.4.1.tar", last modified: Wed Apr  5 17:23:42 2023, max compression
+gzip compressed data, was "l10n_ar_api-2.4.2.tar", last modified: Thu Apr  6 19:32:19 2023, max compression
```

## Comparing `l10n_ar_api-2.4.1.tar` & `l10n_ar_api-2.4.2.tar`

### file list

```diff
@@ -1,86 +1,86 @@
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.471553 l10n_ar_api-2.4.1/
--rw-r--r--   0 lbaldi     (501) staff       (20)      729 2023-04-05 17:23:42.471297 l10n_ar_api-2.4.1/PKG-INFO
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     1327 2022-08-03 14:18:42.000000 l10n_ar_api-2.4.1/README.md
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.439152 l10n_ar_api-2.4.1/l10n_ar_api/
--rwxr-xr-x   0 lbaldi     (501) staff       (20)      206 2019-05-16 12:24:14.000000 l10n_ar_api-2.4.1/l10n_ar_api/__init__.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.443036 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/
--rwxr-xr-x   0 lbaldi     (501) staff       (20)      188 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/__init__.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     1324 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/config.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.444118 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/ws_sr_padron/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)       27 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/ws_sr_padron/__init__.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     1764 2021-06-11 14:11:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/ws_sr_padron/ws_sr_padron.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.447050 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsaa/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)       66 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsaa/__init__.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)     1830 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsaa/certificate.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     4964 2022-05-04 18:30:12.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsaa/tokens.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)      944 2019-05-16 20:39:48.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsaa/wsaa.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.449184 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsbfe/
--rw-r--r--   0 lbaldi     (501) staff       (20)       62 2019-05-16 12:21:51.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsbfe/__init__.py
--rw-r--r--   0 lbaldi     (501) staff       (20)      218 2019-05-16 12:21:51.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsbfe/error.py
--rw-r--r--   0 lbaldi     (501) staff       (20)     3749 2021-01-25 20:28:10.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsbfe/invoice.py
--rw-r--r--   0 lbaldi     (501) staff       (20)    11123 2021-01-25 20:28:10.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsbfe/wsbfe.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.450928 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsct/
--rwxr-xr-x   0 lbaldi     (501) staff       (20)       60 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsct/__init__.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)      296 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsct/error.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     5025 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsct/invoice.py
--rw-r--r--   0 lbaldi     (501) staff       (20)    17475 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsct/wsct.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.453905 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfe/
--rwxr-xr-x   0 lbaldi     (501) staff       (20)       88 2021-01-28 18:46:39.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfe/__init__.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      248 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfe/error.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     4499 2021-05-05 19:00:39.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfe/invoice.py
--rw-r--r--   0 lbaldi     (501) staff       (20)      879 2021-02-19 18:45:11.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfe/qr_generator.py
--rw-r--r--   0 lbaldi     (501) staff       (20)    14310 2021-05-05 19:00:39.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfe/wsfe.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.456433 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfex/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)       62 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfex/__init__.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      222 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfex/error.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     4326 2022-08-02 17:19:38.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfex/invoice.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)    11372 2022-08-03 14:18:42.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfex/wsfex.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.457961 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wstesimbrefiscal/
--rwxr-xr-x   0 lbaldi     (501) staff       (20)       50 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wstesimbrefiscal/__init__.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)      282 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wstesimbrefiscal/error.py
--rw-r--r--   0 lbaldi     (501) staff       (20)     5574 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wstesimbrefiscal/wstesimbrefiscal.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.459312 l10n_ar_api-2.4.1/l10n_ar_api/anmat_webservices/
--rw-r--r--   0 lbaldi     (501) staff       (20)       41 2019-05-16 12:24:14.000000 l10n_ar_api-2.4.1/l10n_ar_api/anmat_webservices/__init__.py
--rw-r--r--   0 lbaldi     (501) staff       (20)     4923 2019-05-16 12:24:14.000000 l10n_ar_api-2.4.1/l10n_ar_api/anmat_webservices/anmat.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)      199 2019-05-16 12:24:14.000000 l10n_ar_api-2.4.1/l10n_ar_api/anmat_webservices/config.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.460793 l10n_ar_api-2.4.1/l10n_ar_api/arba_webservices/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      939 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/arba_webservices/__init__.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      252 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/arba_webservices/config.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     1979 2019-06-27 13:49:55.000000 l10n_ar_api-2.4.1/l10n_ar_api/arba_webservices/iibb.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.462509 l10n_ar_api-2.4.1/l10n_ar_api/documents/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      101 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/documents/__init__.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      597 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/documents/invoice.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      611 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/documents/tax.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.463973 l10n_ar_api-2.4.1/l10n_ar_api/documents/tests/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)       85 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/documents/tests/__init__.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)     1568 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/documents/tests/test_gross_income.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)     2377 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/documents/tests/test_profit.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      246 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/documents/tests/test_tribute.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     3530 2023-04-05 17:23:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/documents/tribute.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.465583 l10n_ar_api-2.4.1/l10n_ar_api/padron/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)       46 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/padron/__init__.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)    10346 2021-05-05 19:00:39.000000 l10n_ar_api-2.4.1/l10n_ar_api/padron/banks.py
--rw-r--r--   0 lbaldi     (501) staff       (20)       60 2019-05-16 12:21:51.000000 l10n_ar_api-2.4.1/l10n_ar_api/padron/config.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)      712 2022-09-26 14:13:58.000000 l10n_ar_api-2.4.1/l10n_ar_api/padron/contributor.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.466879 l10n_ar_api-2.4.1/l10n_ar_api/padron/test/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)       57 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/padron/test/__init__.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      836 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/padron/test/test_banks.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      899 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/padron/test/test_contributors.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.468011 l10n_ar_api-2.4.1/l10n_ar_api/presentations/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)       59 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/presentations/__init__.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)     2253 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/presentations/presentation.py
--rwxr-xr-x   0 lbaldi     (501) staff       (20)   138717 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.1/l10n_ar_api/presentations/presentation_line.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.470775 l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/
--rwxr-xr-x   0 lbaldi     (501) staff       (20)      209 2020-04-07 13:00:21.000000 l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/__init__.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)     8316 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/test_purchases_sales_presentation.py
--rwxrwxrwx   0 lbaldi     (501) staff       (20)     9156 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/test_purchases_sales_presentation_line.py
--rw-r--r--   0 lbaldi     (501) staff       (20)     7411 2020-04-07 13:00:21.000000 l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/test_purchases_sales_vat_digital_book.py
--rw-r--r--   0 lbaldi     (501) staff       (20)     8082 2020-04-07 13:00:21.000000 l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/test_purchases_sales_vat_digital_book_line.py
-drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-05 17:23:42.442118 l10n_ar_api-2.4.1/l10n_ar_api.egg-info/
--rwxrwxrwx   0 lbaldi     (501) staff       (20)      729 2023-04-05 17:23:42.000000 l10n_ar_api-2.4.1/l10n_ar_api.egg-info/PKG-INFO
--rwxrwxrwx   0 lbaldi     (501) staff       (20)     2776 2023-04-05 17:23:42.000000 l10n_ar_api-2.4.1/l10n_ar_api.egg-info/SOURCES.txt
--rwxrwxrwx   0 lbaldi     (501) staff       (20)        1 2023-04-05 17:23:42.000000 l10n_ar_api-2.4.1/l10n_ar_api.egg-info/dependency_links.txt
--rwxrwxrwx   0 lbaldi     (501) staff       (20)       77 2023-04-05 17:23:42.000000 l10n_ar_api-2.4.1/l10n_ar_api.egg-info/requires.txt
--rwxrwxrwx   0 lbaldi     (501) staff       (20)       12 2023-04-05 17:23:42.000000 l10n_ar_api-2.4.1/l10n_ar_api.egg-info/top_level.txt
--rw-r--r--   0 lbaldi     (501) staff       (20)       38 2023-04-05 17:23:42.471636 l10n_ar_api-2.4.1/setup.cfg
--rwxr-xr-x   0 lbaldi     (501) staff       (20)     1278 2023-04-05 17:23:07.000000 l10n_ar_api-2.4.1/setup.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.784621 l10n_ar_api-2.4.2/
+-rw-r--r--   0 lbaldi     (501) staff       (20)      729 2023-04-06 19:32:19.784312 l10n_ar_api-2.4.2/PKG-INFO
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     1327 2022-08-03 14:18:42.000000 l10n_ar_api-2.4.2/README.md
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.738034 l10n_ar_api-2.4.2/l10n_ar_api/
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)      206 2019-05-16 12:24:14.000000 l10n_ar_api-2.4.2/l10n_ar_api/__init__.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.741072 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)      188 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/__init__.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     1324 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/config.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.742208 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/ws_sr_padron/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)       27 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/ws_sr_padron/__init__.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     1764 2021-06-11 14:11:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/ws_sr_padron/ws_sr_padron.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.744959 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsaa/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)       66 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsaa/__init__.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)     1830 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsaa/certificate.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     4964 2022-05-04 18:30:12.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsaa/tokens.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)      944 2019-05-16 20:39:48.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsaa/wsaa.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.747034 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsbfe/
+-rw-r--r--   0 lbaldi     (501) staff       (20)       62 2019-05-16 12:21:51.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsbfe/__init__.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)      218 2019-05-16 12:21:51.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsbfe/error.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)     3749 2021-01-25 20:28:10.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsbfe/invoice.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)    11123 2021-01-25 20:28:10.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsbfe/wsbfe.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.749276 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsct/
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)       60 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsct/__init__.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)      296 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsct/error.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     5025 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsct/invoice.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)    17475 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsct/wsct.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.753144 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfe/
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)       88 2021-01-28 18:46:39.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfe/__init__.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      248 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfe/error.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     4499 2021-05-05 19:00:39.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfe/invoice.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)      879 2021-02-19 18:45:11.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfe/qr_generator.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)    14310 2021-05-05 19:00:39.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfe/wsfe.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.756425 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfex/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)       62 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfex/__init__.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      222 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfex/error.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     4326 2022-08-02 17:19:38.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfex/invoice.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)    11372 2022-08-03 14:18:42.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfex/wsfex.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.758977 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wstesimbrefiscal/
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)       50 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wstesimbrefiscal/__init__.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)      282 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wstesimbrefiscal/error.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)     5574 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wstesimbrefiscal/wstesimbrefiscal.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.761487 l10n_ar_api-2.4.2/l10n_ar_api/anmat_webservices/
+-rw-r--r--   0 lbaldi     (501) staff       (20)       41 2019-05-16 12:24:14.000000 l10n_ar_api-2.4.2/l10n_ar_api/anmat_webservices/__init__.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)     4923 2019-05-16 12:24:14.000000 l10n_ar_api-2.4.2/l10n_ar_api/anmat_webservices/anmat.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)      199 2019-05-16 12:24:14.000000 l10n_ar_api-2.4.2/l10n_ar_api/anmat_webservices/config.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.763942 l10n_ar_api-2.4.2/l10n_ar_api/arba_webservices/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      939 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/arba_webservices/__init__.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      252 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/arba_webservices/config.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     1979 2019-06-27 13:49:55.000000 l10n_ar_api-2.4.2/l10n_ar_api/arba_webservices/iibb.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.768371 l10n_ar_api-2.4.2/l10n_ar_api/documents/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      101 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/documents/__init__.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      597 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/documents/invoice.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      611 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/documents/tax.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.771582 l10n_ar_api-2.4.2/l10n_ar_api/documents/tests/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)       85 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/documents/tests/__init__.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)     1568 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/documents/tests/test_gross_income.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)     2377 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/documents/tests/test_profit.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      246 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/documents/tests/test_tribute.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     3553 2023-04-06 19:31:40.000000 l10n_ar_api-2.4.2/l10n_ar_api/documents/tribute.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.774297 l10n_ar_api-2.4.2/l10n_ar_api/padron/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)       46 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/padron/__init__.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)    10346 2021-05-05 19:00:39.000000 l10n_ar_api-2.4.2/l10n_ar_api/padron/banks.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)       60 2019-05-16 12:21:51.000000 l10n_ar_api-2.4.2/l10n_ar_api/padron/config.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)      712 2022-09-26 14:13:58.000000 l10n_ar_api-2.4.2/l10n_ar_api/padron/contributor.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.776253 l10n_ar_api-2.4.2/l10n_ar_api/padron/test/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)       57 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/padron/test/__init__.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      836 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/padron/test/test_banks.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      899 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/padron/test/test_contributors.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.778431 l10n_ar_api-2.4.2/l10n_ar_api/presentations/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)       59 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/presentations/__init__.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)     2253 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/presentations/presentation.py
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)   138717 2022-12-14 20:20:07.000000 l10n_ar_api-2.4.2/l10n_ar_api/presentations/presentation_line.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.783746 l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)      209 2020-04-07 13:00:21.000000 l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/__init__.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)     8316 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/test_purchases_sales_presentation.py
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)     9156 2019-02-26 14:56:03.000000 l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/test_purchases_sales_presentation_line.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)     7411 2020-04-07 13:00:21.000000 l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/test_purchases_sales_vat_digital_book.py
+-rw-r--r--   0 lbaldi     (501) staff       (20)     8082 2020-04-07 13:00:21.000000 l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/test_purchases_sales_vat_digital_book_line.py
+drwxr-xr-x   0 lbaldi     (501) staff       (20)        0 2023-04-06 19:32:19.739892 l10n_ar_api-2.4.2/l10n_ar_api.egg-info/
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)      729 2023-04-06 19:32:19.000000 l10n_ar_api-2.4.2/l10n_ar_api.egg-info/PKG-INFO
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)     2776 2023-04-06 19:32:19.000000 l10n_ar_api-2.4.2/l10n_ar_api.egg-info/SOURCES.txt
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)        1 2023-04-06 19:32:19.000000 l10n_ar_api-2.4.2/l10n_ar_api.egg-info/dependency_links.txt
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)       77 2023-04-06 19:32:19.000000 l10n_ar_api-2.4.2/l10n_ar_api.egg-info/requires.txt
+-rwxrwxrwx   0 lbaldi     (501) staff       (20)       12 2023-04-06 19:32:19.000000 l10n_ar_api-2.4.2/l10n_ar_api.egg-info/top_level.txt
+-rw-r--r--   0 lbaldi     (501) staff       (20)       38 2023-04-06 19:32:19.784720 l10n_ar_api-2.4.2/setup.cfg
+-rwxr-xr-x   0 lbaldi     (501) staff       (20)     1278 2023-04-06 19:31:40.000000 l10n_ar_api-2.4.2/setup.py
```

### Comparing `l10n_ar_api-2.4.1/PKG-INFO` & `l10n_ar_api-2.4.2/PKG-INFO`

 * *Files 15% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: l10n_ar_api
-Version: 2.4.1
+Version: 2.4.2
 Summary: Libreria para localizacion Argentina
 Home-page: https://github.com/odoo-arg/l10n_ar_api
 Author: BLUEORANGE GROUP SRL
 Author-email: daniel@blueorange.com.ar
 License: UNKNOWN
 Description: Libreria para localizacion Argentina
 Keywords: Libreria para localizacion Argentina
```

### Comparing `l10n_ar_api-2.4.1/README.md` & `l10n_ar_api-2.4.2/README.md`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/config.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/config.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/ws_sr_padron/ws_sr_padron.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/ws_sr_padron/ws_sr_padron.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsaa/certificate.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsaa/certificate.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsaa/tokens.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsaa/tokens.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsaa/wsaa.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsaa/wsaa.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsbfe/invoice.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsbfe/invoice.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsbfe/wsbfe.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsbfe/wsbfe.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsct/invoice.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsct/invoice.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsct/wsct.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsct/wsct.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfe/invoice.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfe/invoice.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfe/qr_generator.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfe/qr_generator.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfe/wsfe.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfe/wsfe.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfex/invoice.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfex/invoice.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wsfex/wsfex.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wsfex/wsfex.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/afip_webservices/wstesimbrefiscal/wstesimbrefiscal.py` & `l10n_ar_api-2.4.2/l10n_ar_api/afip_webservices/wstesimbrefiscal/wstesimbrefiscal.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/anmat_webservices/anmat.py` & `l10n_ar_api-2.4.2/l10n_ar_api/anmat_webservices/anmat.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/arba_webservices/__init__.py` & `l10n_ar_api-2.4.2/l10n_ar_api/arba_webservices/__init__.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/arba_webservices/iibb.py` & `l10n_ar_api-2.4.2/l10n_ar_api/arba_webservices/iibb.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/documents/invoice.py` & `l10n_ar_api-2.4.2/l10n_ar_api/documents/invoice.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/documents/tax.py` & `l10n_ar_api-2.4.2/l10n_ar_api/documents/tax.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/documents/tests/test_gross_income.py` & `l10n_ar_api-2.4.2/l10n_ar_api/documents/tests/test_gross_income.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/documents/tests/test_profit.py` & `l10n_ar_api-2.4.2/l10n_ar_api/documents/tests/test_profit.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/documents/tribute.py` & `l10n_ar_api-2.4.2/l10n_ar_api/documents/tribute.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,13 @@
 # -*- coding: utf-8 -*-
 import math
 
-
 def apply_rounding(value, rounding=2):
     multiplier = 10 ** rounding
-    return math.ceil(value * multiplier) / multiplier
+    return math.floor(round(value * multiplier + 0.5, rounding)) / multiplier
 
 
 class Tribute:
 
     @staticmethod
     def get_tribute(tribute_type):
         """ Devuelve la instancia del tipo de percepcion deseado """
```

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/padron/banks.py` & `l10n_ar_api-2.4.2/l10n_ar_api/padron/banks.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/padron/contributor.py` & `l10n_ar_api-2.4.2/l10n_ar_api/padron/contributor.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/padron/test/test_banks.py` & `l10n_ar_api-2.4.2/l10n_ar_api/padron/test/test_banks.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/padron/test/test_contributors.py` & `l10n_ar_api-2.4.2/l10n_ar_api/padron/test/test_contributors.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/presentations/presentation.py` & `l10n_ar_api-2.4.2/l10n_ar_api/presentations/presentation.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/presentations/presentation_line.py` & `l10n_ar_api-2.4.2/l10n_ar_api/presentations/presentation_line.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/test_purchases_sales_presentation.py` & `l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/test_purchases_sales_presentation.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/test_purchases_sales_presentation_line.py` & `l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/test_purchases_sales_presentation_line.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/test_purchases_sales_vat_digital_book.py` & `l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/test_purchases_sales_vat_digital_book.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api/presentations/test/test_purchases_sales_vat_digital_book_line.py` & `l10n_ar_api-2.4.2/l10n_ar_api/presentations/test/test_purchases_sales_vat_digital_book_line.py`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api.egg-info/PKG-INFO` & `l10n_ar_api-2.4.2/l10n_ar_api.egg-info/PKG-INFO`

 * *Files 16% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: l10n-ar-api
-Version: 2.4.1
+Version: 2.4.2
 Summary: Libreria para localizacion Argentina
 Home-page: https://github.com/odoo-arg/l10n_ar_api
 Author: BLUEORANGE GROUP SRL
 Author-email: daniel@blueorange.com.ar
 License: UNKNOWN
 Description: Libreria para localizacion Argentina
 Keywords: Libreria para localizacion Argentina
```

### Comparing `l10n_ar_api-2.4.1/l10n_ar_api.egg-info/SOURCES.txt` & `l10n_ar_api-2.4.2/l10n_ar_api.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `l10n_ar_api-2.4.1/setup.py` & `l10n_ar_api-2.4.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -15,15 +15,15 @@
 if sys.version_info[0] >= 3:
     install_requires.append('bs4')
 else:
     install_requires.append('BeautifulSoup')
 
 setup(
     name='l10n_ar_api',
-    version='2.4.1',
+    version='2.4.2',
     description='Libreria para localizacion Argentina',
     long_description='Libreria para localizacion Argentina',
     url='https://github.com/odoo-arg/l10n_ar_api',
     author='BLUEORANGE GROUP SRL',
     author_email='daniel@blueorange.com.ar',
     license='',
     classifiers=[
```

