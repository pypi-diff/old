# Comparing `tmp/earthengine-api-0.1.97.tar.gz` & `tmp/earthengine-api-0.1.99.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/earthengine-api-0.1.97.tar", last modified: Thu Sep 29 23:07:51 2016, max compression
+gzip compressed data, was "dist/earthengine-api-0.1.99.tar", last modified: Fri Oct 28 18:28:42 2016, max compression
```

## Comparing `earthengine-api-0.1.97.tar` & `earthengine-api-0.1.99.tar`

### file list

```diff
@@ -1,73 +1,73 @@
-drwxr-x---   0 mdewitt  (167619) eng       (5000)        0 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/
--rw-r-----   0 mdewitt  (167619) eng       (5000)     2227 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/setup.py
-drwxr-x---   0 mdewitt  (167619) eng       (5000)        0 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/earthengine_api.egg-info/
--rw-r-----   0 mdewitt  (167619) eng       (5000)        3 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/earthengine_api.egg-info/top_level.txt
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1436 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/earthengine_api.egg-info/SOURCES.txt
--rw-r-----   0 mdewitt  (167619) eng       (5000)       51 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/earthengine_api.egg-info/entry_points.txt
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1043 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/earthengine_api.egg-info/PKG-INFO
--rw-r-----   0 mdewitt  (167619) eng       (5000)        1 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/earthengine_api.egg-info/dependency_links.txt
--rw-r-----   0 mdewitt  (167619) eng       (5000)       40 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/earthengine_api.egg-info/requires.txt
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1043 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/PKG-INFO
--rw-r-----   0 mdewitt  (167619) eng       (5000)       59 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/setup.cfg
-drwxr-x---   0 mdewitt  (167619) eng       (5000)        0 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/ee/
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1618 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/ee_number.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     6048 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/function.py
-drwxr-x---   0 mdewitt  (167619) eng       (5000)        0 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/ee/tests/
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1134 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/tests/deserializer_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     5216 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/tests/collection_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     2866 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/tests/function_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1213 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/tests/string_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     5919 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/tests/image_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1374 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/tests/_helpers_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    12607 2016-09-29 21:53:59.000000 earthengine-api-0.1.97/ee/tests/geometry_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    17268 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/tests/batch_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1793 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/tests/list_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1248 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/tests/dictionary_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    12834 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/tests/ee_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)      936 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/tests/computedobject_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     2168 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/tests/imagecollection_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     6525 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/tests/filter_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)      905 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/tests/number_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1692 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/tests/element_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     3741 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/tests/featurecollection_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     2167 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/tests/apifunction_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     2621 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/tests/feature_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1559 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/tests/oauth_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     2869 2016-09-29 21:54:03.000000 earthengine-api-0.1.97/ee/tests/serializer_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     5154 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/tests/data_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1448 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/tests/date_test.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1880 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/dictionary.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     3753 2016-09-29 21:54:03.000000 earthengine-api-0.1.97/ee/imagecollection.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)      646 2016-09-29 21:54:03.000000 earthengine-api-0.1.97/ee/terrain.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    38678 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/apitestcase.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     4900 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/deserializer.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1200 2016-09-29 21:54:03.000000 earthengine-api-0.1.97/ee/deprecation.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)      618 2016-09-29 21:54:03.000000 earthengine-api-0.1.97/ee/encodable.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     2430 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/ee_date.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     5372 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/featurecollection.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     6434 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/computedobject.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    36485 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/batch.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     8019 2016-09-29 21:54:03.000000 earthengine-api-0.1.97/ee/apifunction.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     3972 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/_helpers.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     3108 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/element.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     3023 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/ee_types.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     7607 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/collection.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1926 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/ee_string.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    24088 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/data.py
-drwxr-x---   0 mdewitt  (167619) eng       (5000)        0 2016-09-29 23:07:51.000000 earthengine-api-0.1.97/ee/cli/
--rw-r-----   0 mdewitt  (167619) eng       (5000)    28457 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/cli/commands.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     8737 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/cli/utils.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)      906 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/cli/eecli_wrapper.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     2090 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/cli/eecli.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)       83 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/cli/__init__.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    27935 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/geometry.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     1628 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/ee_list.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    17656 2016-09-29 21:54:03.000000 earthengine-api-0.1.97/ee/mapclient.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     5021 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/customfunction.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     5559 2016-09-29 21:54:04.000000 earthengine-api-0.1.97/ee/serializer.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    11846 2016-09-29 21:54:03.000000 earthengine-api-0.1.97/ee/__init__.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    14418 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/image.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)      155 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/ee_exception.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)    11587 2016-09-29 21:54:02.000000 earthengine-api-0.1.97/ee/filter.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     2890 2016-09-29 21:54:00.000000 earthengine-api-0.1.97/ee/oauth.py
--rw-r-----   0 mdewitt  (167619) eng       (5000)     5480 2016-09-29 21:54:01.000000 earthengine-api-0.1.97/ee/feature.py
+drwxr-x---   0 mdh      (94479) eng       (5000)        0 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/
+-rw-r-----   0 mdh      (94479) eng       (5000)     1043 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/PKG-INFO
+drwxr-x---   0 mdh      (94479) eng       (5000)        0 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/earthengine_api.egg-info/
+-rw-r-----   0 mdh      (94479) eng       (5000)     1436 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/earthengine_api.egg-info/SOURCES.txt
+-rw-r-----   0 mdh      (94479) eng       (5000)     1043 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/earthengine_api.egg-info/PKG-INFO
+-rw-r-----   0 mdh      (94479) eng       (5000)        1 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/earthengine_api.egg-info/dependency_links.txt
+-rw-r-----   0 mdh      (94479) eng       (5000)       51 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/earthengine_api.egg-info/entry_points.txt
+-rw-r-----   0 mdh      (94479) eng       (5000)       41 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/earthengine_api.egg-info/requires.txt
+-rw-r-----   0 mdh      (94479) eng       (5000)        3 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/earthengine_api.egg-info/top_level.txt
+-rw-r-----   0 mdh      (94479) eng       (5000)       59 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/setup.cfg
+-rw-r-----   0 mdh      (94479) eng       (5000)     2227 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/setup.py
+drwxr-x---   0 mdh      (94479) eng       (5000)        0 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/ee/
+-rw-r-----   0 mdh      (94479) eng       (5000)     4900 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/deserializer.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     3023 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/ee_types.py
+-rw-r-----   0 mdh      (94479) eng       (5000)      155 2016-10-28 18:22:46.000000 earthengine-api-0.1.99/ee/ee_exception.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     3972 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/_helpers.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1618 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/ee_number.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1200 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/deprecation.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     5372 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/featurecollection.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1880 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/dictionary.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     5021 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/customfunction.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     2430 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/ee_date.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     9109 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/filter.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    27935 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/geometry.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     6434 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/computedobject.py
+drwxr-x---   0 mdh      (94479) eng       (5000)        0 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/ee/cli/
+-rw-r-----   0 mdh      (94479) eng       (5000)      906 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/cli/eecli_wrapper.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     8737 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/cli/utils.py
+-rw-r-----   0 mdh      (94479) eng       (5000)       83 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/cli/__init__.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     2090 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/cli/eecli.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    28457 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/cli/commands.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    38025 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/batch.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    11846 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/__init__.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1926 2016-10-28 18:22:46.000000 earthengine-api-0.1.99/ee/ee_string.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     3803 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/feature.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1628 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/ee_list.py
+-rw-r-----   0 mdh      (94479) eng       (5000)      618 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/encodable.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    38678 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/apitestcase.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     7607 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/collection.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     3753 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/imagecollection.py
+-rw-r-----   0 mdh      (94479) eng       (5000)      646 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/terrain.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    17656 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/mapclient.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     2890 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/oauth.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     5559 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/serializer.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     3108 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/element.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    14418 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/image.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     8019 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/apifunction.py
+drwxr-x---   0 mdh      (94479) eng       (5000)        0 2016-10-28 18:28:42.000000 earthengine-api-0.1.99/ee/tests/
+-rw-r-----   0 mdh      (94479) eng       (5000)     1248 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/tests/dictionary_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1374 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/tests/_helpers_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1692 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/tests/element_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     2168 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/tests/imagecollection_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    12834 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/tests/ee_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1134 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/tests/deserializer_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     4203 2016-10-28 18:22:46.000000 earthengine-api-0.1.99/ee/tests/filter_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     2621 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/tests/feature_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     2866 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/tests/function_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     5919 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/tests/image_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    12607 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/tests/geometry_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)      905 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/tests/number_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1213 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/tests/string_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)      936 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/tests/computedobject_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     5154 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/tests/data_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     2869 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/tests/serializer_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1448 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/tests/date_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1559 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/tests/oauth_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     3741 2016-10-28 18:22:47.000000 earthengine-api-0.1.99/ee/tests/featurecollection_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     5216 2016-10-28 18:22:48.000000 earthengine-api-0.1.99/ee/tests/collection_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     2167 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/tests/apifunction_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     1793 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/tests/list_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    17714 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/tests/batch_test.py
+-rw-r-----   0 mdh      (94479) eng       (5000)    24088 2016-10-28 18:22:50.000000 earthengine-api-0.1.99/ee/data.py
+-rw-r-----   0 mdh      (94479) eng       (5000)     6048 2016-10-28 18:22:49.000000 earthengine-api-0.1.99/ee/function.py
```

### Comparing `earthengine-api-0.1.97/setup.py` & `earthengine-api-0.1.99/setup.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/earthengine_api.egg-info/SOURCES.txt` & `earthengine-api-0.1.99/earthengine_api.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/earthengine_api.egg-info/PKG-INFO` & `earthengine-api-0.1.99/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: earthengine-api
-Version: 0.1.97
+Version: 0.1.99
 Summary: Earth Engine Python API
 Home-page: http://code.google.com/p/earthengine-api/
 Author: Noel Gorelick
 Author-email: gorelick@google.com
 License: UNKNOWN
 Description: =======================
         Earth Engine Python API
```

### Comparing `earthengine-api-0.1.97/PKG-INFO` & `earthengine-api-0.1.99/earthengine_api.egg-info/PKG-INFO`

 * *Files 11% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.1
 Name: earthengine-api
-Version: 0.1.97
+Version: 0.1.99
 Summary: Earth Engine Python API
 Home-page: http://code.google.com/p/earthengine-api/
 Author: Noel Gorelick
 Author-email: gorelick@google.com
 License: UNKNOWN
 Description: =======================
         Earth Engine Python API
```

### Comparing `earthengine-api-0.1.97/ee/ee_number.py` & `earthengine-api-0.1.99/ee/ee_number.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/function.py` & `earthengine-api-0.1.99/ee/function.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/deserializer_test.py` & `earthengine-api-0.1.99/ee/tests/deserializer_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/collection_test.py` & `earthengine-api-0.1.99/ee/tests/collection_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/function_test.py` & `earthengine-api-0.1.99/ee/tests/function_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/string_test.py` & `earthengine-api-0.1.99/ee/tests/string_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/image_test.py` & `earthengine-api-0.1.99/ee/tests/image_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/_helpers_test.py` & `earthengine-api-0.1.99/ee/tests/_helpers_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/geometry_test.py` & `earthengine-api-0.1.99/ee/tests/geometry_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/batch_test.py` & `earthengine-api-0.1.99/ee/tests/batch_test.py`

 * *Files 3% similar despite different names*

```diff
@@ -246,14 +246,24 @@
             'driveFileNamePrefix': 'fooExport',
             'driveFolder': 'foo',
             'maxPixels': 10**10,
             'crs_transform': 'bar',  # Transformed by _ConvertToServerParams.
         },
         drive_task_with_old_keys.config)
 
+  def testExportImageFileDimensions(self):
+    """Verifies proper handling of the fileDimensions parameter."""
+    number_task = ee.batch.Export.image.toDrive(
+        image=ee.Image(1), fileDimensions=100)
+    self.assertEquals(100, number_task.config['fileDimensions'])
+
+    tuple_task = ee.batch.Export.image.toDrive(
+        image=ee.Image(1), fileDimensions=(100, 200))
+    self.assertEquals('100,200', tuple_task.config['fileDimensions'])
+
   def testExportMapToCloudStorage(self):
     """Verifies the task created by Export.map.toCloudStorage()."""
     config = dict(
         image=ee.Image(1), bucket='test-bucket', maxZoom=7, path='foo/gcs/path')
 
     # Test keyed parameters.
     task_keyed = ee.batch.Export.map.toCloudStorage(
```

### Comparing `earthengine-api-0.1.97/ee/tests/list_test.py` & `earthengine-api-0.1.99/ee/tests/list_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/dictionary_test.py` & `earthengine-api-0.1.99/ee/tests/dictionary_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/ee_test.py` & `earthengine-api-0.1.99/ee/tests/ee_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/computedobject_test.py` & `earthengine-api-0.1.99/ee/tests/computedobject_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/imagecollection_test.py` & `earthengine-api-0.1.99/ee/tests/imagecollection_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/filter_test.py` & `earthengine-api-0.1.99/ee/tests/filter_test.py`

 * *Files 24% similar despite different names*

```diff
@@ -11,59 +11,48 @@
 from ee import apitestcase
 
 
 class FilterTest(apitestcase.ApiTestCase):
 
   def testConstructors(self):
     """Verifies that constructors understand valid parameters."""
-    empty = ee.Filter()
-    self.assertEquals(0, empty.predicateCount())
-
     from_static_method = ee.Filter.gt('foo', 1)
-    self.assertEquals(1, from_static_method.predicateCount())
-
     from_computed_object = ee.Filter(
         ee.ApiFunction.call_('Filter.greaterThan', 'foo', 1))
-    self.assertEquals(1, from_computed_object.predicateCount())
     self.assertEquals(from_static_method, from_computed_object)
 
     copy = ee.Filter(from_static_method)
     self.assertEquals(from_static_method, copy)
 
-  def testAppend(self):
-    """Verifies that appending filters with instance methods works."""
-    multi_filter = ee.Filter().eq('foo', 1).eq('bar', 2).eq('baz', 3)
-    self.assertEquals(3, multi_filter.predicateCount())
-
   def testMetadata(self):
     """Verifies that the metadata_() method works."""
     self.assertEquals(
         ee.ApiFunction.call_('Filter.equals', 'x', 1),
         ee.Filter.metadata_('x', 'equals', 1))
     self.assertEquals(
         ee.Filter.metadata_('x', 'equals', 1),
-        ee.Filter().eq('x', 1))
+        ee.Filter.eq('x', 1))
     self.assertEquals(
         ee.Filter.metadata_('x', 'EQUALS', 1),
-        ee.Filter().eq('x', 1))
+        ee.Filter.eq('x', 1))
     self.assertEquals(
         ee.Filter.metadata_('x', 'not_equals', 1),
-        ee.Filter().neq('x', 1))
+        ee.Filter.neq('x', 1))
     self.assertEquals(
         ee.Filter.metadata_('x', 'less_than', 1),
-        ee.Filter().lt('x', 1))
+        ee.Filter.lt('x', 1))
     self.assertEquals(
         ee.Filter.metadata_('x', 'not_greater_than', 1),
-        ee.Filter().lte('x', 1))
+        ee.Filter.lte('x', 1))
     self.assertEquals(
         ee.Filter.metadata_('x', 'greater_than', 1),
-        ee.Filter().gt('x', 1))
+        ee.Filter.gt('x', 1))
     self.assertEquals(
         ee.Filter.metadata_('x', 'not_less_than', 1),
-        ee.Filter().gte('x', 1))
+        ee.Filter.gte('x', 1))
 
   def testLogicalCombinations(self):
     """Verifies that the and() and or() methods work."""
     f1 = ee.Filter.eq('x', 1)
     f2 = ee.Filter.eq('x', 2)
 
     or_filter = ee.Filter.Or(f1, f2)
@@ -115,54 +104,14 @@
         ee.Filter.geometry(collection))
 
   def testInList(self):
     """Verifies that list membership filters work."""
     self.assertEquals(
         ee.Filter.listContains(None, None, 'foo', [1, 2]),
         ee.Filter.inList('foo', [1, 2]))
-    self.assertEquals(
-        ee.Filter.inList('foo', [1, 2]),
-        ee.Filter().inList('foo', [1, 2]))
-
-  def testStaticVersions(self):
-    """Verifies that static filter methods are equivalent to instance ones."""
-    self.assertEquals(ee.Filter().eq('foo', 1), ee.Filter.eq('foo', 1))
-    self.assertEquals(ee.Filter().neq('foo', 1), ee.Filter.neq('foo', 1))
-    self.assertEquals(ee.Filter().lt('foo', 1), ee.Filter.lt('foo', 1))
-    self.assertEquals(ee.Filter().gt('foo', 1), ee.Filter.gt('foo', 1))
-    self.assertEquals(ee.Filter().lte('foo', 1), ee.Filter.lte('foo', 1))
-    self.assertEquals(ee.Filter().gte('foo', 1), ee.Filter.gte('foo', 1))
-
-    self.assertEquals(ee.Filter().contains('foo', 1),
-                      ee.Filter.contains('foo', 1))
-    self.assertEquals(ee.Filter().not_contains('foo', 1),
-                      ee.Filter.not_contains('foo', 1))
-    self.assertEquals(ee.Filter().starts_with('foo', 1),
-                      ee.Filter.starts_with('foo', 1))
-    self.assertEquals(ee.Filter().not_starts_with('foo', 1),
-                      ee.Filter.not_starts_with('foo', 1))
-    self.assertEquals(ee.Filter().ends_with('foo', 1),
-                      ee.Filter.ends_with('foo', 1))
-    self.assertEquals(ee.Filter().not_ends_with('foo', 1),
-                      ee.Filter.not_ends_with('foo', 1))
-
-    f1 = ee.Filter().And(ee.Filter().eq('foo', 1), ee.Filter().eq('foo', 2))
-    f2 = ee.Filter.And(ee.Filter.eq('foo', 1), ee.Filter().eq('foo', 2))
-    self.assertEquals(f1, f2)
-
-    ring1 = ee.Geometry.Polygon(1, 2, 3, 4, 5, 6)
-    f1 = ee.Filter().geometry(ring1)
-    f2 = ee.Filter.geometry(ring1)
-    self.assertEquals(f1, f2)
-
-    d1 = datetime.datetime.strptime('1/1/2000', '%m/%d/%Y')
-    d2 = datetime.datetime.strptime('1/1/2001', '%m/%d/%Y')
-    f1 = ee.Filter().date(d1, d2)
-    f2 = ee.Filter.date(d1, d2)
-    self.assertEquals(f1, f2)
 
   def testInternals(self):
     """Test eq(), ne() and hash()."""
     a = ee.Filter.eq('x', 1)
     b = ee.Filter.eq('x', 2)
     c = ee.Filter.eq('x', 1)
```

### Comparing `earthengine-api-0.1.97/ee/tests/number_test.py` & `earthengine-api-0.1.99/ee/tests/number_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/element_test.py` & `earthengine-api-0.1.99/ee/tests/element_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/featurecollection_test.py` & `earthengine-api-0.1.99/ee/tests/featurecollection_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/apifunction_test.py` & `earthengine-api-0.1.99/ee/tests/apifunction_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/feature_test.py` & `earthengine-api-0.1.99/ee/tests/feature_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/oauth_test.py` & `earthengine-api-0.1.99/ee/tests/oauth_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/serializer_test.py` & `earthengine-api-0.1.99/ee/tests/serializer_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/data_test.py` & `earthengine-api-0.1.99/ee/tests/data_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/tests/date_test.py` & `earthengine-api-0.1.99/ee/tests/date_test.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/dictionary.py` & `earthengine-api-0.1.99/ee/dictionary.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/imagecollection.py` & `earthengine-api-0.1.99/ee/imagecollection.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/terrain.py` & `earthengine-api-0.1.99/ee/terrain.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/apitestcase.py` & `earthengine-api-0.1.99/ee/apitestcase.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/deserializer.py` & `earthengine-api-0.1.99/ee/deserializer.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/deprecation.py` & `earthengine-api-0.1.99/ee/deprecation.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/encodable.py` & `earthengine-api-0.1.99/ee/encodable.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/ee_date.py` & `earthengine-api-0.1.99/ee/ee_date.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/featurecollection.py` & `earthengine-api-0.1.99/ee/featurecollection.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/computedobject.py` & `earthengine-api-0.1.99/ee/computedobject.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/batch.py` & `earthengine-api-0.1.99/ee/batch.py`

 * *Files 2% similar despite different names*

```diff
@@ -252,15 +252,15 @@
     # Disable argument usage check; arguments are accessed using locals().
     # pylint: disable=unused-argument
     @staticmethod
     def toCloudStorage(image, description='myExportImageTask',
                        bucket=None, fileNamePrefix=None,
                        dimensions=None, region=None, scale=None,
                        crs=None, crsTransform=None, maxPixels=None,
-                       **kwargs):
+                       shardSize=None, fileDimensions=None, **kwargs):
       """Creates a task to export an EE Image to Google Cloud Storage.
 
       Args:
         image: The image to be exported.
         description: Human-readable name of the task.
         bucket: The name of a Cloud Storage bucket for the export.
         fileNamePrefix: Cloud Storage object name prefix for the export.
@@ -281,14 +281,22 @@
             the affine transform of the coordinate reference system of the
             exported image's projection, in the order: xScale, yShearing,
             xShearing, yScale, xTranslation and yTranslation. Defaults to
             the image's native CRS transform.
         maxPixels: The maximum allowed number of pixels in the exported
             image. The task will fail if the exported region covers more
             pixels in the specified projection. Defaults to 100,000,000.
+        shardSize: Size in pixels of the shards in which this image will be
+            computed. Defaults to 256.
+        fileDimensions: The dimensions in pixels of each image file, if the
+            image is too large to fit in a single file. May specify a
+            single number to indicate a square shape, or a tuple of two
+            dimensions to indicate (width,height). Note that the image will
+            still be clipped to the overall image dimensions. Must be a
+            multiple of shardSize.
         **kwargs: Holds other keyword arguments that may have been deprecated
             such as 'crs_transform'.
 
       Returns:
         An unstarted Task that exports the image to Google Cloud Storage.
       """
       # _CopyDictFilterNone must be called first because it copies locals to
@@ -304,15 +312,15 @@
       return _CreateTask(
           Task.Type.EXPORT_IMAGE, image, description, config)
 
     @staticmethod
     def toDrive(image, description='myExportImageTask', folder=None,
                 fileNamePrefix=None, dimensions=None, region=None,
                 scale=None, crs=None, crsTransform=None, maxPixels=None,
-                **kwargs):
+                shardSize=None, fileDimensions=None, **kwargs):
       """Creates a task to export an EE Image to Drive.
 
       Args:
         image: The image to be exported.
         description: Human-readable name of the task.
         folder: The name of a unique folder in your Drive account to
             export into. Defaults to the root of the drive.
@@ -334,14 +342,22 @@
             the affine transform of the coordinate reference system of the
             exported image's projection, in the order: xScale, yShearing,
             xShearing, yScale, xTranslation and yTranslation. Defaults to
             the image's native CRS transform.
         maxPixels: The maximum allowed number of pixels in the exported
             image. The task will fail if the exported region covers more
             pixels in the specified projection. Defaults to 100,000,000.
+        shardSize: Size in pixels of the shards in which this image will be
+            computed. Defaults to 256.
+        fileDimensions: The dimensions in pixels of each image file, if the
+            image is too large to fit in a single file. May specify a
+            single number to indicate a square shape, or a tuple of two
+            dimensions to indicate (width,height). Note that the image will
+            still be clipped to the overall image dimensions. Must be a
+            multiple of shardSize.
         **kwargs: Holds other keyword arguments that may have been deprecated
             such as 'crs_transform', 'driveFolder', and 'driveFileNamePrefix'.
 
       Returns:
         An unstarted Task that exports the image to Drive.
       """
       # _CopyDictFilterNone must be called first because it copies locals to
@@ -371,15 +387,15 @@
 
     # Disable argument usage check; arguments are accessed using locals().
     # pylint: disable=unused-argument
     @staticmethod
     def toCloudStorage(image, description='myExportMapTask', bucket=None,
                        fileFormat=None, path=None, writePublicTiles=None,
                        maxZoom=None, scale=None, minZoom=None,
-                       region=None, **kwargs):
+                       region=None, skipEmptyTiles=None, **kwargs):
       """Creates a task to export an Image as a pyramid of map tiles.
 
       Exports a rectangular pyramid of map tiles for use with web map
       viewers. The map tiles will be accompanied by a reference
       index.html file that displays them using the Google Maps API.
 
       Args:
@@ -401,14 +417,16 @@
             maximum zoom level at the equator.
         minZoom: The optional minimum zoom level of the map tiles to export.
         region: The lon,lat coordinates for a LinearRing or Polygon
             specifying the region to export. Can be specified as a nested
             lists of numbers or a serialized string. Map tiles will be
             produced in the rectangular region containing this geometry.
             Defaults to the image's region.
+        skipEmptyTiles: If true, skip writing empty (i.e. fully-transparent)
+            map tiles.
         **kwargs: Holds other keyword arguments that may have been deprecated
             such as 'crs_transform'.
 
       Returns:
         An unstarted Task that exports the image to Google Cloud Storage.
 
       """
@@ -795,14 +813,23 @@
   if 'kwargs' in configDict:
     configDict.update(configDict['kwargs'])
     del configDict['kwargs']
 
   if 'crsTransform' in configDict:
     configDict['crs_transform'] = configDict.pop('crsTransform')
 
+  # Convert iterable fileDimensions to a comma-separated string.
+  if 'fileDimensions' in configDict:
+    dimensions = configDict['fileDimensions']
+    try:
+      configDict['fileDimensions'] = ','.join('%d' % dim for dim in dimensions)
+    except TypeError:
+      # We pass numbers straight through.
+      pass
+
   if destination is Task.ExportDestination.GCS:
     if 'bucket' in configDict:
       configDict['outputBucket'] = configDict.pop('bucket')
 
     if 'fileNamePrefix' in configDict:
       if 'outputPrefix' not in configDict:
         configDict['outputPrefix'] = configDict.pop('fileNamePrefix')
```

### Comparing `earthengine-api-0.1.97/ee/apifunction.py` & `earthengine-api-0.1.99/ee/apifunction.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/_helpers.py` & `earthengine-api-0.1.99/ee/_helpers.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/element.py` & `earthengine-api-0.1.99/ee/element.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/ee_types.py` & `earthengine-api-0.1.99/ee/ee_types.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/collection.py` & `earthengine-api-0.1.99/ee/collection.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/ee_string.py` & `earthengine-api-0.1.99/ee/ee_string.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/data.py` & `earthengine-api-0.1.99/ee/data.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/cli/commands.py` & `earthengine-api-0.1.99/ee/cli/commands.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/cli/utils.py` & `earthengine-api-0.1.99/ee/cli/utils.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/cli/eecli_wrapper.py` & `earthengine-api-0.1.99/ee/cli/eecli_wrapper.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/cli/eecli.py` & `earthengine-api-0.1.99/ee/cli/eecli.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/geometry.py` & `earthengine-api-0.1.99/ee/geometry.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/ee_list.py` & `earthengine-api-0.1.99/ee/ee_list.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/mapclient.py` & `earthengine-api-0.1.99/ee/mapclient.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/customfunction.py` & `earthengine-api-0.1.99/ee/customfunction.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/serializer.py` & `earthengine-api-0.1.99/ee/serializer.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/__init__.py` & `earthengine-api-0.1.99/ee/__init__.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 #!/usr/bin/env python
 """The EE Python library."""
 
 
-__version__ = '0.1.97'
+__version__ = '0.1.99'
 
 # Using lowercase function naming to match the JavaScript names.
 # pylint: disable=g-bad-name
 
 # pylint: disable=g-bad-import-order
 import collections
 import datetime
```

### Comparing `earthengine-api-0.1.97/ee/image.py` & `earthengine-api-0.1.99/ee/image.py`

 * *Files identical despite different names*

### Comparing `earthengine-api-0.1.97/ee/oauth.py` & `earthengine-api-0.1.99/ee/oauth.py`

 * *Files identical despite different names*

