# Comparing `tmp/astro-metadata-translator-26.0.0a20230400.tar.gz` & `tmp/astro-metadata-translator-26.0.0a20230500.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "astro-metadata-translator-26.0.0a20230400.tar", last modified: Thu Jan 26 09:56:29 2023, max compression
+gzip compressed data, was "astro-metadata-translator-26.0.0a20230500.tar", last modified: Thu Feb  2 14:04:54 2023, max compression
```

## Comparing `astro-metadata-translator-26.0.0a20230400.tar` & `astro-metadata-translator-26.0.0a20230500.tar`

### file list

```diff
@@ -1,78 +1,78 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.735427 astro-metadata-translator-26.0.0a20230400/
--rw-r--r--   0 runner    (1001) docker     (123)      188 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/CHANGES.md
--rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       19 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     1655 2023-01-26 09:56:29.735427 astro-metadata-translator-26.0.0a20230400/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      874 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      271 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/pyproject.toml
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.723427 astro-metadata-translator-26.0.0a20230400/python/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.727427 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/
--rw-r--r--   0 runner    (1001) docker     (123)      595 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/__init__.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.727427 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/bin/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/bin/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    13318 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/bin/translateheader.py
--rw-r--r--   0 runner    (1001) docker     (123)     4296 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/bin/writeindex.py
--rw-r--r--   0 runner    (1001) docker     (123)     5394 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/bin/writesidecar.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.727427 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/cli/
--rw-r--r--   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/cli/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     7159 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/cli/astrometadata.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.723427 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.735427 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00042600.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00120200.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00120400.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00120600.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00120800.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121000.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121200.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121400.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121600.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121800.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00122000.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00122800.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00123000.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00123200.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00123800.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124000.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124200.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124400.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124600.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124800.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00186800.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00187000.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00187200.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00187400.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00187600.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00188000.yaml
--rw-r--r--   0 runner    (1001) docker     (123)       17 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00188200.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     9751 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/file_helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)    18997 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/headers.py
--rw-r--r--   0 runner    (1001) docker     (123)    14763 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/indexing.py
--rw-r--r--   0 runner    (1001) docker     (123)     8397 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/observationGroup.py
--rw-r--r--   0 runner    (1001) docker     (123)    27152 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/observationInfo.py
--rw-r--r--   0 runner    (1001) docker     (123)    12872 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/properties.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.735427 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/serialize/
--rw-r--r--   0 runner    (1001) docker     (123)      427 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/serialize/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)     3805 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/serialize/fits.py
--rw-r--r--   0 runner    (1001) docker     (123)    10976 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/tests.py
--rw-r--r--   0 runner    (1001) docker     (123)    49768 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translator.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.735427 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/
--rw-r--r--   0 runner    (1001) docker     (123)      560 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14905 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/decam.py
--rw-r--r--   0 runner    (1001) docker     (123)     6681 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/fits.py
--rw-r--r--   0 runner    (1001) docker     (123)     6566 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/helpers.py
--rw-r--r--   0 runner    (1001) docker     (123)     8204 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/hsc.py
--rw-r--r--   0 runner    (1001) docker     (123)     9942 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/megaprime.py
--rw-r--r--   0 runner    (1001) docker     (123)     9019 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/sdss.py
--rw-r--r--   0 runner    (1001) docker     (123)     1461 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/subaru.py
--rw-r--r--   0 runner    (1001) docker     (123)     8441 2023-01-26 09:56:15.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/suprimecam.py
--rw-r--r--   0 runner    (1001) docker     (123)       58 2023-01-26 09:56:29.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/version.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-01-26 09:56:29.727427 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1655 2023-01-26 09:56:29.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-01-26 09:56:29.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:29.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)      156 2023-01-26 09:56:29.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       28 2023-01-26 09:56:29.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       26 2023-01-26 09:56:29.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-01-26 09:56:29.000000 astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/zip-safe
--rw-r--r--   0 runner    (1001) docker     (123)     1456 2023-01-26 09:56:29.735427 astro-metadata-translator-26.0.0a20230400/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.813594 astro-metadata-translator-26.0.0a20230500/
+-rw-r--r--   0 runner    (1001) docker     (123)      188 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/CHANGES.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1518 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       19 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1655 2023-02-02 14:04:54.813594 astro-metadata-translator-26.0.0a20230500/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      874 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      271 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/pyproject.toml
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.805594 astro-metadata-translator-26.0.0a20230500/python/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.805594 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/
+-rw-r--r--   0 runner    (1001) docker     (123)      595 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/__init__.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.809594 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/bin/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/bin/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    13318 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/bin/translateheader.py
+-rw-r--r--   0 runner    (1001) docker     (123)     4296 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/bin/writeindex.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5394 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/bin/writesidecar.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.809594 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/cli/
+-rw-r--r--   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/cli/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     7159 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/cli/astrometadata.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.805594 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.809594 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00042600.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00120200.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00120400.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00120600.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00120800.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121000.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121200.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121400.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121600.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00121800.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00122000.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00122800.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00123000.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00123200.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00123800.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124000.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124200.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124400.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124600.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00124800.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00186800.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00187000.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00187200.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00187400.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00187600.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00188000.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       17 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/corrections/HSC/HSC-HSCA00188200.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     9751 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/file_helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    18997 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/headers.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14763 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/indexing.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8397 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/observationGroup.py
+-rw-r--r--   0 runner    (1001) docker     (123)    27152 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/observationInfo.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12872 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/properties.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.813594 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/serialize/
+-rw-r--r--   0 runner    (1001) docker     (123)      427 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/serialize/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     3805 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/serialize/fits.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10976 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/tests.py
+-rw-r--r--   0 runner    (1001) docker     (123)    49768 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translator.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.813594 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/
+-rw-r--r--   0 runner    (1001) docker     (123)      560 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14905 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/decam.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6681 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/fits.py
+-rw-r--r--   0 runner    (1001) docker     (123)     6566 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/helpers.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8204 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/hsc.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9942 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/megaprime.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9019 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/sdss.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1461 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/subaru.py
+-rw-r--r--   0 runner    (1001) docker     (123)     8441 2023-02-02 14:04:40.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/suprimecam.py
+-rw-r--r--   0 runner    (1001) docker     (123)       58 2023-02-02 14:04:54.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-02-02 14:04:54.805594 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1655 2023-02-02 14:04:54.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     3754 2023-02-02 14:04:54.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:04:54.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      156 2023-02-02 14:04:54.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       28 2023-02-02 14:04:54.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       26 2023-02-02 14:04:54.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-02-02 14:04:54.000000 astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/zip-safe
+-rw-r--r--   0 runner    (1001) docker     (123)     1456 2023-02-02 14:04:54.813594 astro-metadata-translator-26.0.0a20230500/setup.cfg
```

### Comparing `astro-metadata-translator-26.0.0a20230400/LICENSE` & `astro-metadata-translator-26.0.0a20230500/LICENSE`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/PKG-INFO` & `astro-metadata-translator-26.0.0a20230500/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: astro-metadata-translator
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: A translator for astronomical metadata.
 Home-page: https://github.com/lsst/astro_metadata_translator
 Author: Rubin Observatory Data Management
 Author-email: dm-admin@lists.lsst.org
 License: BSD 3-Clause License
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
```

### Comparing `astro-metadata-translator-26.0.0a20230400/README.md` & `astro-metadata-translator-26.0.0a20230500/README.md`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/__init__.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/__init__.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/bin/translateheader.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/bin/translateheader.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/bin/writeindex.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/bin/writeindex.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/bin/writesidecar.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/bin/writesidecar.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/cli/astrometadata.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/cli/astrometadata.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/file_helpers.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/file_helpers.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/headers.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/headers.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/indexing.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/indexing.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/observationGroup.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/observationGroup.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/observationInfo.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/observationInfo.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/properties.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/properties.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/serialize/fits.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/serialize/fits.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/tests.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/tests.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translator.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translator.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/__init__.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/__init__.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/decam.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/decam.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/fits.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/fits.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/helpers.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/helpers.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/hsc.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/hsc.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/megaprime.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/megaprime.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/sdss.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/sdss.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/subaru.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/subaru.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator/translators/suprimecam.py` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator/translators/suprimecam.py`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/PKG-INFO` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: astro-metadata-translator
-Version: 26.0.0a20230400
+Version: 26.0.0a20230500
 Summary: A translator for astronomical metadata.
 Home-page: https://github.com/lsst/astro_metadata_translator
 Author: Rubin Observatory Data Management
 Author-email: dm-admin@lists.lsst.org
 License: BSD 3-Clause License
 Keywords: lsst
 Classifier: Intended Audience :: Science/Research
```

### Comparing `astro-metadata-translator-26.0.0a20230400/python/astro_metadata_translator.egg-info/SOURCES.txt` & `astro-metadata-translator-26.0.0a20230500/python/astro_metadata_translator.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `astro-metadata-translator-26.0.0a20230400/setup.cfg` & `astro-metadata-translator-26.0.0a20230500/setup.cfg`

 * *Files identical despite different names*

