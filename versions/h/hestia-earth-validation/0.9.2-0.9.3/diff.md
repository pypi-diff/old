# Comparing `tmp/hestia-earth-validation-0.9.2.tar.gz` & `tmp/hestia-earth-validation-0.9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/hestia-earth-validation-0.9.2.tar", last modified: Thu Mar 17 10:47:08 2022, max compression
+gzip compressed data, was "dist/hestia-earth-validation-0.9.3.tar", last modified: Thu Mar 17 12:47:33 2022, max compression
```

## Comparing `hestia-earth-validation-0.9.2.tar` & `hestia-earth-validation-0.9.3.tar`

### file list

```diff
@@ -1,58 +1,58 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/
--rw-rw-rw-   0 root         (0) root         (0)    35149 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/LICENSE
--rw-rw-rw-   0 root         (0) root         (0)       18 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/MANIFEST.in
--rw-r--r--   0 root         (0) root         (0)     1225 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/PKG-INFO
--rw-rw-rw-   0 root         (0) root         (0)      821 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/bin/
--rwxrwxrwx   0 root         (0) root         (0)     1653 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/bin/hestia-validate-data
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/hestia_earth/
--rw-rw-rw-   0 root         (0) root         (0)       56 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/
--rw-rw-rw-   0 root         (0) root         (0)      896 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     1244 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/gee.py
--rw-rw-rw-   0 root         (0) root         (0)      507 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/geojson.py
--rw-rw-rw-   0 root         (0) root         (0)     1323 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/log.py
--rw-rw-rw-   0 root         (0) root         (0)     5336 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/utils.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/
--rw-rw-rw-   0 root         (0) root         (0)     3089 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)    11334 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/cycle.py
--rw-rw-rw-   0 root         (0) root         (0)      977 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/data_completeness.py
--rw-rw-rw-   0 root         (0) root         (0)     1951 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/impact_assessment.py
--rw-rw-rw-   0 root         (0) root         (0)     2050 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/indicator.py
--rw-rw-rw-   0 root         (0) root         (0)      780 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/infrastructure.py
--rw-rw-rw-   0 root         (0) root         (0)     2609 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/input.py
--rw-rw-rw-   0 root         (0) root         (0)    10280 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/measurement.py
--rw-rw-rw-   0 root         (0) root         (0)     1704 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/organisation.py
--rw-rw-rw-   0 root         (0) root         (0)     4750 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/practice.py
--rw-rw-rw-   0 root         (0) root         (0)     3531 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/product.py
--rw-rw-rw-   0 root         (0) root         (0)     3861 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/property.py
--rw-rw-rw-   0 root         (0) root         (0)    18407 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/shared.py
--rw-rw-rw-   0 root         (0) root         (0)     5899 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/site.py
--rw-rw-rw-   0 root         (0) root         (0)     3237 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/validators/transformation.py
--rw-rw-rw-   0 root         (0) root         (0)       18 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/hestia_earth/validation/version.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/hestia_earth_validation.egg-info/
--rw-r--r--   0 root         (0) root         (0)     1225 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/hestia_earth_validation.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1829 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/hestia_earth_validation.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/hestia_earth_validation.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)      113 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/hestia_earth_validation.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       19 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/hestia_earth_validation.egg-info/top_level.txt
--rw-rw-rw-   0 root         (0) root         (0)       79 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/setup.cfg
--rw-rw-rw-   0 root         (0) root         (0)      889 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/tests/
-drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 10:47:08.000000 hestia-earth-validation-0.9.2/tests/validators/
--rw-rw-rw-   0 root         (0) root         (0)        0 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/__init__.py
--rw-rw-rw-   0 root         (0) root         (0)     6895 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_cycle.py
--rw-rw-rw-   0 root         (0) root         (0)     1931 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_data_completeness.py
--rw-rw-rw-   0 root         (0) root         (0)      327 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_impact_assessment.py
--rw-rw-rw-   0 root         (0) root         (0)     1439 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_indicator.py
--rw-rw-rw-   0 root         (0) root         (0)      770 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_infrastructure.py
--rw-rw-rw-   0 root         (0) root         (0)     2377 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_input.py
--rw-rw-rw-   0 root         (0) root         (0)    11041 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_measurement.py
--rw-rw-rw-   0 root         (0) root         (0)     1153 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_organisation.py
--rw-rw-rw-   0 root         (0) root         (0)     6116 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_practice.py
--rw-rw-rw-   0 root         (0) root         (0)     4476 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_product.py
--rw-rw-rw-   0 root         (0) root         (0)     1839 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_property.py
--rw-rw-rw-   0 root         (0) root         (0)    20904 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_shared.py
--rw-rw-rw-   0 root         (0) root         (0)     2845 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_site.py
--rw-rw-rw-   0 root         (0) root         (0)     3229 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_transformation.py
--rw-rw-rw-   0 root         (0) root         (0)     1313 2022-03-17 10:46:45.000000 hestia-earth-validation-0.9.2/tests/validators/test_validators.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 12:47:33.000000 hestia-earth-validation-0.9.3/
+-rw-rw-rw-   0 root         (0) root         (0)    35149 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/LICENSE
+-rw-rw-rw-   0 root         (0) root         (0)       18 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/MANIFEST.in
+-rw-r--r--   0 root         (0) root         (0)     1225 2022-03-17 12:47:33.000000 hestia-earth-validation-0.9.3/PKG-INFO
+-rw-rw-rw-   0 root         (0) root         (0)      821 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/bin/
+-rwxrwxrwx   0 root         (0) root         (0)     1653 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/bin/hestia-validate-data
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/hestia_earth/
+-rw-rw-rw-   0 root         (0) root         (0)       56 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/
+-rw-rw-rw-   0 root         (0) root         (0)      896 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     1244 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/gee.py
+-rw-rw-rw-   0 root         (0) root         (0)      507 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/geojson.py
+-rw-rw-rw-   0 root         (0) root         (0)     1323 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/log.py
+-rw-rw-rw-   0 root         (0) root         (0)     5336 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/utils.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/
+-rw-rw-rw-   0 root         (0) root         (0)     3089 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)    11334 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/cycle.py
+-rw-rw-rw-   0 root         (0) root         (0)      977 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/data_completeness.py
+-rw-rw-rw-   0 root         (0) root         (0)     1951 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/impact_assessment.py
+-rw-rw-rw-   0 root         (0) root         (0)     2050 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/indicator.py
+-rw-rw-rw-   0 root         (0) root         (0)      780 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/infrastructure.py
+-rw-rw-rw-   0 root         (0) root         (0)     2609 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/input.py
+-rw-rw-rw-   0 root         (0) root         (0)    10280 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/measurement.py
+-rw-rw-rw-   0 root         (0) root         (0)     1704 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/organisation.py
+-rw-rw-rw-   0 root         (0) root         (0)     4750 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/practice.py
+-rw-rw-rw-   0 root         (0) root         (0)     3531 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/product.py
+-rw-rw-rw-   0 root         (0) root         (0)     3861 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/property.py
+-rw-rw-rw-   0 root         (0) root         (0)    18373 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/shared.py
+-rw-rw-rw-   0 root         (0) root         (0)     5899 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/site.py
+-rw-rw-rw-   0 root         (0) root         (0)     3237 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/validators/transformation.py
+-rw-rw-rw-   0 root         (0) root         (0)       18 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/hestia_earth/validation/version.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/hestia_earth_validation.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     1225 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/hestia_earth_validation.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1829 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/hestia_earth_validation.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/hestia_earth_validation.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)      113 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/hestia_earth_validation.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       19 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/hestia_earth_validation.egg-info/top_level.txt
+-rw-rw-rw-   0 root         (0) root         (0)       79 2022-03-17 12:47:33.000000 hestia-earth-validation-0.9.3/setup.cfg
+-rw-rw-rw-   0 root         (0) root         (0)      889 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 12:47:32.000000 hestia-earth-validation-0.9.3/tests/
+drwxr-xr-x   0 root         (0) root         (0)        0 2022-03-17 12:47:33.000000 hestia-earth-validation-0.9.3/tests/validators/
+-rw-rw-rw-   0 root         (0) root         (0)        0 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/__init__.py
+-rw-rw-rw-   0 root         (0) root         (0)     6895 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_cycle.py
+-rw-rw-rw-   0 root         (0) root         (0)     1931 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_data_completeness.py
+-rw-rw-rw-   0 root         (0) root         (0)      327 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_impact_assessment.py
+-rw-rw-rw-   0 root         (0) root         (0)     1439 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_indicator.py
+-rw-rw-rw-   0 root         (0) root         (0)      770 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_infrastructure.py
+-rw-rw-rw-   0 root         (0) root         (0)     2377 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_input.py
+-rw-rw-rw-   0 root         (0) root         (0)    11041 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_measurement.py
+-rw-rw-rw-   0 root         (0) root         (0)     1153 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_organisation.py
+-rw-rw-rw-   0 root         (0) root         (0)     6116 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_practice.py
+-rw-rw-rw-   0 root         (0) root         (0)     4476 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_product.py
+-rw-rw-rw-   0 root         (0) root         (0)     1839 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_property.py
+-rw-rw-rw-   0 root         (0) root         (0)    20904 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_shared.py
+-rw-rw-rw-   0 root         (0) root         (0)     2845 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_site.py
+-rw-rw-rw-   0 root         (0) root         (0)     3229 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_transformation.py
+-rw-rw-rw-   0 root         (0) root         (0)     1313 2022-03-17 12:47:09.000000 hestia-earth-validation-0.9.3/tests/validators/test_validators.py
```

### Comparing `hestia-earth-validation-0.9.2/LICENSE` & `hestia-earth-validation-0.9.3/LICENSE`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/PKG-INFO` & `hestia-earth-validation-0.9.3/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hestia-earth-validation
-Version: 0.9.2
+Version: 0.9.3
 Summary: Hestia Data Validation library
 Home-page: https://gitlab.com/hestia-earth/hestia-data-validation
 Author: Guillaume Royer
 Author-email: guillaumeroyer.mail@gmail.com
 License: GPL-3.0-or-later
 Keywords: hestia,data,validation
 Platform: UNKNOWN
```

### Comparing `hestia-earth-validation-0.9.2/README.md` & `hestia-earth-validation-0.9.3/README.md`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/bin/hestia-validate-data` & `hestia-earth-validation-0.9.3/bin/hestia-validate-data`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/__init__.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/__init__.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/gee.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/gee.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/log.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/log.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/utils.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/utils.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/__init__.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/__init__.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/cycle.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/cycle.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/data_completeness.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/data_completeness.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/impact_assessment.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/impact_assessment.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/indicator.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/indicator.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/infrastructure.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/infrastructure.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/input.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/input.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/measurement.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/measurement.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/organisation.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/organisation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/practice.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/practice.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/product.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/product.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/property.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/property.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/shared.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/shared.py`

 * *Files 1% similar despite different names*

```diff
@@ -267,15 +267,15 @@
         }
     }
 
 
 def validate_region_size(node: dict):
     region_id = node.get('region', node.get('country', {})).get('@id')
     region = download_hestia(region_id) if region_id else {}
-    area = region.get('area', get_region_size(region_id)) or 0  # fallback fetch size from GEE if full term has no area
+    area = region.get('area', get_region_size(region_id) if region_id else None) or 0
     return area < MAX_AREA_SIZE or {
         'level': 'warning',
         'dataPath': f".{'region' if node.get('region') else 'country'}",
         'message': 'should be lower than max size',
         'params': {
             'current': area,
             'expected': MAX_AREA_SIZE
```

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/site.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/site.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth/validation/validators/transformation.py` & `hestia-earth-validation-0.9.3/hestia_earth/validation/validators/transformation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/hestia_earth_validation.egg-info/PKG-INFO` & `hestia-earth-validation-0.9.3/hestia_earth_validation.egg-info/PKG-INFO`

 * *Files 10% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: hestia-earth-validation
-Version: 0.9.2
+Version: 0.9.3
 Summary: Hestia Data Validation library
 Home-page: https://gitlab.com/hestia-earth/hestia-data-validation
 Author: Guillaume Royer
 Author-email: guillaumeroyer.mail@gmail.com
 License: GPL-3.0-or-later
 Keywords: hestia,data,validation
 Platform: UNKNOWN
```

### Comparing `hestia-earth-validation-0.9.2/hestia_earth_validation.egg-info/SOURCES.txt` & `hestia-earth-validation-0.9.3/hestia_earth_validation.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/setup.py` & `hestia-earth-validation-0.9.3/setup.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_cycle.py` & `hestia-earth-validation-0.9.3/tests/validators/test_cycle.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_data_completeness.py` & `hestia-earth-validation-0.9.3/tests/validators/test_data_completeness.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_indicator.py` & `hestia-earth-validation-0.9.3/tests/validators/test_indicator.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_infrastructure.py` & `hestia-earth-validation-0.9.3/tests/validators/test_infrastructure.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_input.py` & `hestia-earth-validation-0.9.3/tests/validators/test_input.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_measurement.py` & `hestia-earth-validation-0.9.3/tests/validators/test_measurement.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_organisation.py` & `hestia-earth-validation-0.9.3/tests/validators/test_organisation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_practice.py` & `hestia-earth-validation-0.9.3/tests/validators/test_practice.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_product.py` & `hestia-earth-validation-0.9.3/tests/validators/test_product.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_property.py` & `hestia-earth-validation-0.9.3/tests/validators/test_property.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_shared.py` & `hestia-earth-validation-0.9.3/tests/validators/test_shared.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_site.py` & `hestia-earth-validation-0.9.3/tests/validators/test_site.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_transformation.py` & `hestia-earth-validation-0.9.3/tests/validators/test_transformation.py`

 * *Files identical despite different names*

### Comparing `hestia-earth-validation-0.9.2/tests/validators/test_validators.py` & `hestia-earth-validation-0.9.3/tests/validators/test_validators.py`

 * *Files identical despite different names*

