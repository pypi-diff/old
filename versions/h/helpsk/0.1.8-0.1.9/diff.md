# Comparing `tmp/helpsk-0.1.8.tar.gz` & `tmp/helpsk-0.1.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "helpsk-0.1.8.tar", last modified: Thu Feb 10 18:36:32 2022, max compression
+gzip compressed data, was "helpsk-0.1.9.tar", last modified: Fri Feb 11 18:31:16 2022, max compression
```

## Comparing `helpsk-0.1.8.tar` & `helpsk-0.1.9.tar`

### file list

```diff
@@ -1,47 +1,47 @@
-drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-10 18:36:32.111329 helpsk-0.1.8/
--rw-r--r--   0 shanekercheval   (501) staff       (20)     1072 2021-07-07 05:35:30.000000 helpsk-0.1.8/LICENSE
--rw-r--r--   0 shanekercheval   (501) staff       (20)     1051 2022-02-10 18:36:32.111387 helpsk-0.1.8/PKG-INFO
--rw-r--r--   0 shanekercheval   (501) staff       (20)      480 2022-01-26 17:53:10.000000 helpsk-0.1.8/README.md
-drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-10 18:36:32.099098 helpsk-0.1.8/docstring_markdown/
--rw-r--r--   0 shanekercheval   (501) staff       (20)        0 2021-08-17 22:02:37.000000 helpsk-0.1.8/docstring_markdown/__init__.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     8638 2021-08-25 03:44:09.000000 helpsk-0.1.8/docstring_markdown/build_markdown.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     1189 2021-08-17 15:13:31.000000 helpsk-0.1.8/docstring_markdown/custom_command.py
-drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-10 18:36:32.104668 helpsk-0.1.8/helpsk/
--rw-r--r--   0 shanekercheval   (501) staff       (20)      467 2022-02-02 01:42:15.000000 helpsk-0.1.8/helpsk/__init__.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     1177 2022-02-01 18:43:23.000000 helpsk-0.1.8/helpsk/color.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     9153 2021-09-24 16:18:59.000000 helpsk-0.1.8/helpsk/database.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     5204 2021-09-26 23:15:59.000000 helpsk-0.1.8/helpsk/database_base.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     6805 2021-11-25 23:20:16.000000 helpsk-0.1.8/helpsk/date.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)      584 2021-09-13 02:57:08.000000 helpsk-0.1.8/helpsk/exceptions.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    36913 2022-02-10 03:34:57.000000 helpsk-0.1.8/helpsk/pandas.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    10819 2021-12-04 00:02:08.000000 helpsk-0.1.8/helpsk/pandas_style.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    12606 2021-11-27 20:23:48.000000 helpsk-0.1.8/helpsk/plot.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)   125721 2022-02-09 05:12:32.000000 helpsk-0.1.8/helpsk/sklearn_eval.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     2365 2021-11-29 01:46:37.000000 helpsk-0.1.8/helpsk/sklearn_pipeline.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    15394 2022-02-09 04:03:58.000000 helpsk-0.1.8/helpsk/sklearn_search.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     3767 2021-08-21 17:46:06.000000 helpsk-0.1.8/helpsk/string.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     1691 2021-09-26 23:21:16.000000 helpsk-0.1.8/helpsk/utility.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    13598 2021-11-25 23:11:28.000000 helpsk-0.1.8/helpsk/validation.py
-drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-10 18:36:32.105440 helpsk-0.1.8/helpsk.egg-info/
--rw-r--r--   0 shanekercheval   (501) staff       (20)     1051 2022-02-10 18:36:32.000000 helpsk-0.1.8/helpsk.egg-info/PKG-INFO
--rw-r--r--   0 shanekercheval   (501) staff       (20)      917 2022-02-10 18:36:32.000000 helpsk-0.1.8/helpsk.egg-info/SOURCES.txt
--rw-r--r--   0 shanekercheval   (501) staff       (20)        1 2022-02-10 18:36:32.000000 helpsk-0.1.8/helpsk.egg-info/dependency_links.txt
--rw-r--r--   0 shanekercheval   (501) staff       (20)       95 2022-02-10 18:36:32.000000 helpsk-0.1.8/helpsk.egg-info/requires.txt
--rw-r--r--   0 shanekercheval   (501) staff       (20)       32 2022-02-10 18:36:32.000000 helpsk-0.1.8/helpsk.egg-info/top_level.txt
--rw-r--r--   0 shanekercheval   (501) staff       (20)      104 2021-08-17 14:40:43.000000 helpsk-0.1.8/pyproject.toml
--rw-r--r--   0 shanekercheval   (501) staff       (20)      739 2022-02-10 18:36:32.111704 helpsk-0.1.8/setup.cfg
-drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-10 18:36:32.110812 helpsk-0.1.8/tests/
--rw-r--r--   0 shanekercheval   (501) staff       (20)        0 2021-08-16 21:35:55.000000 helpsk-0.1.8/tests/__init__.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     5609 2022-02-04 22:45:06.000000 helpsk-0.1.8/tests/helpers.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     2583 2021-10-05 05:54:23.000000 helpsk-0.1.8/tests/test_color.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     8291 2021-10-05 05:54:23.000000 helpsk-0.1.8/tests/test_database.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    54278 2021-11-25 23:28:31.000000 helpsk-0.1.8/tests/test_date.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     6057 2021-09-24 20:21:31.000000 helpsk-0.1.8/tests/test_docstring_markdown.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    49181 2022-02-10 18:34:24.000000 helpsk-0.1.8/tests/test_pandas.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     5756 2022-02-04 22:51:06.000000 helpsk-0.1.8/tests/test_pandas_style.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     6309 2021-11-27 20:24:02.000000 helpsk-0.1.8/tests/test_plot.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    73157 2022-02-04 22:30:07.000000 helpsk-0.1.8/tests/test_sklearn_eval.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    26650 2022-02-09 05:15:22.000000 helpsk-0.1.8/tests/test_sklearn_search.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)     4548 2021-09-24 20:18:43.000000 helpsk-0.1.8/tests/test_string.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)      275 2021-10-05 05:56:30.000000 helpsk-0.1.8/tests/test_utility.py
--rw-r--r--   0 shanekercheval   (501) staff       (20)    36106 2021-11-25 22:21:39.000000 helpsk-0.1.8/tests/test_validation.py
+drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-11 18:31:16.914378 helpsk-0.1.9/
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     1072 2021-07-07 05:35:30.000000 helpsk-0.1.9/LICENSE
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     1051 2022-02-11 18:31:16.914595 helpsk-0.1.9/PKG-INFO
+-rw-r--r--   0 shanekercheval   (501) staff       (20)      480 2022-01-26 17:53:10.000000 helpsk-0.1.9/README.md
+drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-11 18:31:16.894645 helpsk-0.1.9/docstring_markdown/
+-rw-r--r--   0 shanekercheval   (501) staff       (20)        0 2021-08-17 22:02:37.000000 helpsk-0.1.9/docstring_markdown/__init__.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     8638 2021-08-25 03:44:09.000000 helpsk-0.1.9/docstring_markdown/build_markdown.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     1189 2021-08-17 15:13:31.000000 helpsk-0.1.9/docstring_markdown/custom_command.py
+drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-11 18:31:16.904271 helpsk-0.1.9/helpsk/
+-rw-r--r--   0 shanekercheval   (501) staff       (20)      467 2022-02-02 01:42:15.000000 helpsk-0.1.9/helpsk/__init__.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     1177 2022-02-01 18:43:23.000000 helpsk-0.1.9/helpsk/color.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     9256 2022-02-10 19:10:41.000000 helpsk-0.1.9/helpsk/database.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     5204 2021-09-26 23:15:59.000000 helpsk-0.1.9/helpsk/database_base.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     6849 2022-02-11 18:28:20.000000 helpsk-0.1.9/helpsk/date.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)      584 2021-09-13 02:57:08.000000 helpsk-0.1.9/helpsk/exceptions.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    36913 2022-02-10 03:34:57.000000 helpsk-0.1.9/helpsk/pandas.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    10819 2021-12-04 00:02:08.000000 helpsk-0.1.9/helpsk/pandas_style.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    12606 2021-11-27 20:23:48.000000 helpsk-0.1.9/helpsk/plot.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)   125715 2022-02-11 17:59:16.000000 helpsk-0.1.9/helpsk/sklearn_eval.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     2365 2021-11-29 01:46:37.000000 helpsk-0.1.9/helpsk/sklearn_pipeline.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    15421 2022-02-11 18:16:58.000000 helpsk-0.1.9/helpsk/sklearn_search.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     3767 2021-08-21 17:46:06.000000 helpsk-0.1.9/helpsk/string.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     1691 2021-09-26 23:21:16.000000 helpsk-0.1.9/helpsk/utility.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    13598 2021-11-25 23:11:28.000000 helpsk-0.1.9/helpsk/validation.py
+drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-11 18:31:16.906836 helpsk-0.1.9/helpsk.egg-info/
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     1051 2022-02-11 18:31:16.000000 helpsk-0.1.9/helpsk.egg-info/PKG-INFO
+-rw-r--r--   0 shanekercheval   (501) staff       (20)      917 2022-02-11 18:31:16.000000 helpsk-0.1.9/helpsk.egg-info/SOURCES.txt
+-rw-r--r--   0 shanekercheval   (501) staff       (20)        1 2022-02-11 18:31:16.000000 helpsk-0.1.9/helpsk.egg-info/dependency_links.txt
+-rw-r--r--   0 shanekercheval   (501) staff       (20)       95 2022-02-11 18:31:16.000000 helpsk-0.1.9/helpsk.egg-info/requires.txt
+-rw-r--r--   0 shanekercheval   (501) staff       (20)       32 2022-02-11 18:31:16.000000 helpsk-0.1.9/helpsk.egg-info/top_level.txt
+-rw-r--r--   0 shanekercheval   (501) staff       (20)      104 2021-08-17 14:40:43.000000 helpsk-0.1.9/pyproject.toml
+-rw-r--r--   0 shanekercheval   (501) staff       (20)      739 2022-02-11 18:31:16.915229 helpsk-0.1.9/setup.cfg
+drwxr-xr-x   0 shanekercheval   (501) staff       (20)        0 2022-02-11 18:31:16.913720 helpsk-0.1.9/tests/
+-rw-r--r--   0 shanekercheval   (501) staff       (20)        0 2021-08-16 21:35:55.000000 helpsk-0.1.9/tests/__init__.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     5609 2022-02-04 22:45:06.000000 helpsk-0.1.9/tests/helpers.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     2583 2021-10-05 05:54:23.000000 helpsk-0.1.9/tests/test_color.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     8291 2021-10-05 05:54:23.000000 helpsk-0.1.9/tests/test_database.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    54585 2022-02-11 18:28:57.000000 helpsk-0.1.9/tests/test_date.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     6057 2021-09-24 20:21:31.000000 helpsk-0.1.9/tests/test_docstring_markdown.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    49138 2022-02-11 00:58:22.000000 helpsk-0.1.9/tests/test_pandas.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     5756 2022-02-04 22:51:06.000000 helpsk-0.1.9/tests/test_pandas_style.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     6309 2021-11-27 20:24:02.000000 helpsk-0.1.9/tests/test_plot.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    73157 2022-02-04 22:30:07.000000 helpsk-0.1.9/tests/test_sklearn_eval.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    27072 2022-02-11 18:17:04.000000 helpsk-0.1.9/tests/test_sklearn_search.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)     4548 2021-09-24 20:18:43.000000 helpsk-0.1.9/tests/test_string.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)      275 2021-10-05 05:56:30.000000 helpsk-0.1.9/tests/test_utility.py
+-rw-r--r--   0 shanekercheval   (501) staff       (20)    36106 2021-11-25 22:21:39.000000 helpsk-0.1.9/tests/test_validation.py
```

### Comparing `helpsk-0.1.8/LICENSE` & `helpsk-0.1.9/LICENSE`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/PKG-INFO` & `helpsk-0.1.9/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: helpsk
-Version: 0.1.8
+Version: 0.1.9
 Summary: Python helper functions and classes.
 Home-page: https://github.com/shanekercheval/python-helpers
 Author: Shane Kercheval
 Author-email: shane.kercheval@gmail.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/shanekercheval/python-helpers/issues
 Platform: UNKNOWN
```

### Comparing `helpsk-0.1.8/docstring_markdown/build_markdown.py` & `helpsk-0.1.9/docstring_markdown/build_markdown.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/docstring_markdown/custom_command.py` & `helpsk-0.1.9/docstring_markdown/custom_command.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/color.py` & `helpsk-0.1.9/helpsk/color.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/database.py` & `helpsk-0.1.9/helpsk/database.py`

 * *Files 2% similar despite different names*

```diff
@@ -201,19 +201,22 @@
             config = SnowflakeConfigFile('/path/to/snowflake.config')
             with Snowflake.from_config(config) as snowflake:
                 snowflake.query("SELECT * FROM table LIMIT 100")
 
     Instructions for installing snowflake dependencies:
         https://docs.snowflake.com/en/user-guide/python-connector-install.html
 
-    I used v2.5.0, and python v3.9 (requirements_39):
+    I used v2.7.4, and python v3.9 (requirements_39):
+
+    This page shows the latest versions:
+        https://pypi.org/project/snowflake-connector-python/
 
     ```
-    pip install -r ......./snowflake-connector-python/v2.5.0/tested_requirements/requirements_39.reqs
-    pip install snowflake-connector-python==v2.5.0
+    pip install -r ......./snowflake-connector-python/v2.7.4/tested_requirements/requirements_39.reqs
+    pip install snowflake-connector-python==v2.7.4
     ```
 
     Additionally:
         https://docs.snowflake.com/en/user-guide/python-connector-pandas.html#installation
 
     ```
     pip install snowflake-connector-python[pandas]
```

### Comparing `helpsk-0.1.8/helpsk/database_base.py` & `helpsk-0.1.9/helpsk/database_base.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/date.py` & `helpsk-0.1.9/helpsk/date.py`

 * *Files 1% similar despite different names*

```diff
@@ -46,15 +46,16 @@
             Feb, 2, etc.) that corresponds to the first month of the fiscal year.
 
     Returns:
         date - the date rounded down to the nearest granularity
     """
     if isinstance(value, pd.Series):
         return pd.Series([floor(x, granularity=granularity, fiscal_start=fiscal_start) for x in value],
-                         name=value.name)
+                         name=value.name,
+                         index=value.index)
 
     if any_none_nan(value):
         return value
 
     if granularity == Granularity.DAY:
         if isinstance(value, datetime.datetime):
             return value.date()
```

### Comparing `helpsk-0.1.8/helpsk/exceptions.py` & `helpsk-0.1.9/helpsk/exceptions.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/pandas.py` & `helpsk-0.1.9/helpsk/pandas.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/pandas_style.py` & `helpsk-0.1.9/helpsk/pandas_style.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/plot.py` & `helpsk-0.1.9/helpsk/plot.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/sklearn_eval.py` & `helpsk-0.1.9/helpsk/sklearn_eval.py`

 * *Files 0% similar despite different names*

```diff
@@ -3259,4600 +3259,4600 @@
 0000cba0: 3d20 7469 746c 6520 2b20 6622 3c62 723e  = title + f"<br>
 0000cbb0: 3c73 7570 3e54 6865 2073 697a 6520 6f66  <sup>The size of
 0000cbc0: 2074 6865 2070 6f69 6e74 2063 6f72 7265   the point corre
 0000cbd0: 7370 6f6e 6473 2074 6f20 7468 6520 7661  sponds to the va
 0000cbe0: 6c75 6520 6f66 203c 623e 277b 7369 7a65  lue of <b>'{size
 0000cbf0: 7d27 3c2f 623e 2e3c 2f73 7570 3e22 0a0a  }'</b>.</sup>"..
 0000cc00: 2020 2020 2020 2020 6c61 6265 6c65 645f          labeled_
-0000cc10: 6466 203d 2072 6573 756c 7473 2e74 6f5f  df = results.to_
-0000cc20: 6c61 6265 6c65 645f 6461 7461 6672 616d  labeled_datafram
-0000cc30: 6528 7175 6572 793d 7175 6572 7929 0a20  e(query=query). 
-0000cc40: 2020 2020 2020 2069 6620 6661 6365 745f         if facet_
-0000cc50: 6279 3a0a 2020 2020 2020 2020 2020 2020  by:.            
-0000cc60: 6c61 6265 6c65 645f 6466 5b27 5472 6961  labeled_df['Tria
-0000cc70: 6c20 496e 6465 7827 5d20 3d20 6c61 6265  l Index'] = labe
-0000cc80: 6c65 645f 6466 2e67 726f 7570 6279 2866  led_df.groupby(f
-0000cc90: 6163 6574 5f62 7929 5b22 5472 6961 6c20  acet_by)["Trial 
-0000cca0: 496e 6465 7822 5d2e 7261 6e6b 286d 6574  Index"].rank(met
-0000ccb0: 686f 643d 2266 6972 7374 222c 0a20 2020  hod="first",.   
+0000cc10: 6466 203d 2073 656c 662e 746f 5f6c 6162  df = self.to_lab
+0000cc20: 656c 6564 5f64 6174 6166 7261 6d65 2871  eled_dataframe(q
+0000cc30: 7565 7279 3d71 7565 7279 290a 2020 2020  uery=query).    
+0000cc40: 2020 2020 6966 2066 6163 6574 5f62 793a      if facet_by:
+0000cc50: 0a20 2020 2020 2020 2020 2020 206c 6162  .            lab
+0000cc60: 656c 6564 5f64 665b 2754 7269 616c 2049  eled_df['Trial I
+0000cc70: 6e64 6578 275d 203d 206c 6162 656c 6564  ndex'] = labeled
+0000cc80: 5f64 662e 6772 6f75 7062 7928 6661 6365  _df.groupby(face
+0000cc90: 745f 6279 295b 2254 7269 616c 2049 6e64  t_by)["Trial Ind
+0000cca0: 6578 225d 2e72 616e 6b28 6d65 7468 6f64  ex"].rank(method
+0000ccb0: 3d22 6669 7273 7422 2c0a 2020 2020 2020  ="first",.      
 0000ccc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000ccd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000cce0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000ccf0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000cd00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000cd10: 2020 2020 2020 2061 7363 656e 6469 6e67         ascending
-0000cd20: 3d54 7275 6529 0a20 2020 2020 2020 2020  =True).         
-0000cd30: 2020 200a 2020 2020 2020 2020 6669 6720     .        fig 
-0000cd40: 3d20 7078 2e73 6361 7474 6572 280a 2020  = px.scatter(.  
-0000cd50: 2020 2020 2020 2020 2020 6461 7461 5f66            data_f
-0000cd60: 7261 6d65 3d6c 6162 656c 6564 5f64 662c  rame=labeled_df,
-0000cd70: 0a20 2020 2020 2020 2020 2020 2078 3d27  .            x='
-0000cd80: 5472 6961 6c20 496e 6465 7827 2c0a 2020  Trial Index',.  
-0000cd90: 2020 2020 2020 2020 2020 793d 7363 6f72            y=scor
-0000cda0: 655f 636f 6c75 6d6e 2c0a 2020 2020 2020  e_column,.      
-0000cdb0: 2020 2020 2020 7369 7a65 3d73 697a 652c        size=size,
-0000cdc0: 0a20 2020 2020 2020 2020 2020 2063 6f6c  .            col
-0000cdd0: 6f72 3d63 6f6c 6f72 2c0a 2020 2020 2020  or=color,.      
-0000cde0: 2020 2020 2020 636f 6c6f 725f 636f 6e74        color_cont
-0000cdf0: 696e 756f 7573 5f73 6361 6c65 3d63 6f6c  inuous_scale=col
-0000ce00: 6f72 5f63 6f6e 7469 6e75 6f75 735f 7363  or_continuous_sc
-0000ce10: 616c 652c 0a20 2020 2020 2020 2020 2020  ale,.           
-0000ce20: 2074 7265 6e64 6c69 6e65 3d27 6c6f 7765   trendline='lowe
-0000ce30: 7373 272c 0a20 2020 2020 2020 2020 2020  ss',.           
-0000ce40: 2066 6163 6574 5f63 6f6c 3d66 6163 6574   facet_col=facet
-0000ce50: 5f62 792c 0a20 2020 2020 2020 2020 2020  _by,.           
-0000ce60: 2066 6163 6574 5f63 6f6c 5f77 7261 703d   facet_col_wrap=
-0000ce70: 6661 6365 745f 6e75 6d5f 636f 6c2c 0a20  facet_num_col,. 
-0000ce80: 2020 2020 2020 2020 2020 206c 6162 656c             label
-0000ce90: 733d 7b0a 2020 2020 2020 2020 2020 2020  s={.            
-0000cea0: 2020 2020 7363 6f72 655f 636f 6c75 6d6e      score_column
-0000ceb0: 3a20 6622 4176 6572 6167 6520 4356 2053  : f"Average CV S
-0000cec0: 636f 7265 3c62 723e 287b 7265 7375 6c74  core<br>({result
-0000ced0: 732e 7072 696d 6172 795f 7363 6f72 655f  s.primary_score_
-0000cee0: 6e61 6d65 7d29 222c 0a20 2020 2020 2020  name})",.       
-0000cef0: 2020 2020 207d 2c0a 2020 2020 2020 2020       },.        
-0000cf00: 2020 2020 7469 746c 653d 7469 746c 652c      title=title,
-0000cf10: 0a20 2020 2020 2020 2020 2020 2063 7573  .            cus
-0000cf20: 746f 6d5f 6461 7461 3d5b 276c 6162 656c  tom_data=['label
-0000cf30: 275d 2c0a 2020 2020 2020 2020 2020 2020  '],.            
-0000cf40: 6865 6967 6874 3d68 6569 6768 742c 0a20  height=height,. 
-0000cf50: 2020 2020 2020 2020 2020 2077 6964 7468             width
-0000cf60: 3d77 6964 7468 2c0a 2020 2020 2020 2020  =width,.        
-0000cf70: 290a 2020 2020 2020 2020 6669 672e 7570  ).        fig.up
-0000cf80: 6461 7465 5f74 7261 6365 7328 0a20 2020  date_traces(.   
-0000cf90: 2020 2020 2020 2020 2068 6f76 6572 7465           hoverte
-0000cfa0: 6d70 6c61 7465 3d22 3c62 723e 222e 6a6f  mplate="<br>".jo
-0000cfb0: 696e 285b 0a20 2020 2020 2020 2020 2020  in([.           
-0000cfc0: 2020 2020 2022 5472 6961 6c20 496e 6465       "Trial Inde
-0000cfd0: 783a 2025 7b78 7d22 2c0a 2020 2020 2020  x: %{x}",.      
-0000cfe0: 2020 2020 2020 2020 2020 7363 6f72 655f            score_
-0000cff0: 636f 6c75 6d6e 202b 2022 3a20 2220 2b20  column + ": " + 
-0000d000: 2225 7b79 7d22 2c0a 2020 2020 2020 2020  "%{y}",.        
-0000d010: 2020 2020 2020 2020 223c 6272 3e50 6172          "<br>Par
-0000d020: 616d 6574 6572 733a 2025 7b63 7573 746f  ameters: %{custo
-0000d030: 6d64 6174 615b 305d 7d22 2c0a 2020 2020  mdata[0]}",.    
-0000d040: 2020 2020 2020 2020 5d29 0a20 2020 2020          ]).     
-0000d050: 2020 2029 0a20 2020 2020 2020 2072 6574     ).        ret
-0000d060: 7572 6e20 6669 670a 0a20 2020 2064 6566  urn fig..    def
-0000d070: 2070 6c6f 745f 7061 7261 6d65 7465 725f   plot_parameter_
-0000d080: 7661 6c75 6573 5f61 6372 6f73 735f 7472  values_across_tr
-0000d090: 6961 6c73 2873 656c 662c 0a20 2020 2020  ials(self,.     
+0000cd10: 2020 2020 6173 6365 6e64 696e 673d 5472      ascending=Tr
+0000cd20: 7565 290a 2020 2020 2020 2020 2020 2020  ue).            
+0000cd30: 0a20 2020 2020 2020 2066 6967 203d 2070  .        fig = p
+0000cd40: 782e 7363 6174 7465 7228 0a20 2020 2020  x.scatter(.     
+0000cd50: 2020 2020 2020 2064 6174 615f 6672 616d         data_fram
+0000cd60: 653d 6c61 6265 6c65 645f 6466 2c0a 2020  e=labeled_df,.  
+0000cd70: 2020 2020 2020 2020 2020 783d 2754 7269            x='Tri
+0000cd80: 616c 2049 6e64 6578 272c 0a20 2020 2020  al Index',.     
+0000cd90: 2020 2020 2020 2079 3d73 636f 7265 5f63         y=score_c
+0000cda0: 6f6c 756d 6e2c 0a20 2020 2020 2020 2020  olumn,.         
+0000cdb0: 2020 2073 697a 653d 7369 7a65 2c0a 2020     size=size,.  
+0000cdc0: 2020 2020 2020 2020 2020 636f 6c6f 723d            color=
+0000cdd0: 636f 6c6f 722c 0a20 2020 2020 2020 2020  color,.         
+0000cde0: 2020 2063 6f6c 6f72 5f63 6f6e 7469 6e75     color_continu
+0000cdf0: 6f75 735f 7363 616c 653d 636f 6c6f 725f  ous_scale=color_
+0000ce00: 636f 6e74 696e 756f 7573 5f73 6361 6c65  continuous_scale
+0000ce10: 2c0a 2020 2020 2020 2020 2020 2020 7472  ,.            tr
+0000ce20: 656e 646c 696e 653d 276c 6f77 6573 7327  endline='lowess'
+0000ce30: 2c0a 2020 2020 2020 2020 2020 2020 6661  ,.            fa
+0000ce40: 6365 745f 636f 6c3d 6661 6365 745f 6279  cet_col=facet_by
+0000ce50: 2c0a 2020 2020 2020 2020 2020 2020 6661  ,.            fa
+0000ce60: 6365 745f 636f 6c5f 7772 6170 3d66 6163  cet_col_wrap=fac
+0000ce70: 6574 5f6e 756d 5f63 6f6c 2c0a 2020 2020  et_num_col,.    
+0000ce80: 2020 2020 2020 2020 6c61 6265 6c73 3d7b          labels={
+0000ce90: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0000cea0: 2073 636f 7265 5f63 6f6c 756d 6e3a 2066   score_column: f
+0000ceb0: 2241 7665 7261 6765 2043 5620 5363 6f72  "Average CV Scor
+0000cec0: 653c 6272 3e28 7b73 656c 662e 7072 696d  e<br>({self.prim
+0000ced0: 6172 795f 7363 6f72 655f 6e61 6d65 7d29  ary_score_name})
+0000cee0: 222c 0a20 2020 2020 2020 2020 2020 207d  ",.            }
+0000cef0: 2c0a 2020 2020 2020 2020 2020 2020 7469  ,.            ti
+0000cf00: 746c 653d 7469 746c 652c 0a20 2020 2020  tle=title,.     
+0000cf10: 2020 2020 2020 2063 7573 746f 6d5f 6461         custom_da
+0000cf20: 7461 3d5b 276c 6162 656c 275d 2c0a 2020  ta=['label'],.  
+0000cf30: 2020 2020 2020 2020 2020 6865 6967 6874            height
+0000cf40: 3d68 6569 6768 742c 0a20 2020 2020 2020  =height,.       
+0000cf50: 2020 2020 2077 6964 7468 3d77 6964 7468       width=width
+0000cf60: 2c0a 2020 2020 2020 2020 290a 2020 2020  ,.        ).    
+0000cf70: 2020 2020 6669 672e 7570 6461 7465 5f74      fig.update_t
+0000cf80: 7261 6365 7328 0a20 2020 2020 2020 2020  races(.         
+0000cf90: 2020 2068 6f76 6572 7465 6d70 6c61 7465     hovertemplate
+0000cfa0: 3d22 3c62 723e 222e 6a6f 696e 285b 0a20  ="<br>".join([. 
+0000cfb0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+0000cfc0: 5472 6961 6c20 496e 6465 783a 2025 7b78  Trial Index: %{x
+0000cfd0: 7d22 2c0a 2020 2020 2020 2020 2020 2020  }",.            
+0000cfe0: 2020 2020 7363 6f72 655f 636f 6c75 6d6e      score_column
+0000cff0: 202b 2022 3a20 2220 2b20 2225 7b79 7d22   + ": " + "%{y}"
+0000d000: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+0000d010: 2020 223c 6272 3e50 6172 616d 6574 6572    "<br>Parameter
+0000d020: 733a 2025 7b63 7573 746f 6d64 6174 615b  s: %{customdata[
+0000d030: 305d 7d22 2c0a 2020 2020 2020 2020 2020  0]}",.          
+0000d040: 2020 5d29 0a20 2020 2020 2020 2029 0a20    ]).        ). 
+0000d050: 2020 2020 2020 2072 6574 7572 6e20 6669         return fi
+0000d060: 670a 0a20 2020 2064 6566 2070 6c6f 745f  g..    def plot_
+0000d070: 7061 7261 6d65 7465 725f 7661 6c75 6573  parameter_values
+0000d080: 5f61 6372 6f73 735f 7472 6961 6c73 2873  _across_trials(s
+0000d090: 656c 662c 0a20 2020 2020 2020 2020 2020  elf,.           
 0000d0a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000d0b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000d0c0: 2020 2020 2020 2071 7565 7279 3a20 7374         query: st
-0000d0d0: 7220 3d20 4e6f 6e65 2c0a 2020 2020 2020  r = None,.      
+0000d0c0: 2071 7565 7279 3a20 7374 7220 3d20 4e6f   query: str = No
+0000d0d0: 6e65 2c0a 2020 2020 2020 2020 2020 2020  ne,.            
 0000d0e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000d0f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000d100: 2020 2020 2020 6865 6967 6874 3a20 666c        height: fl
-0000d110: 6f61 7420 3d20 3630 302c 0a20 2020 2020  oat = 600,.     
+0000d100: 6865 6967 6874 3a20 666c 6f61 7420 3d20  height: float = 
+0000d110: 3630 302c 0a20 2020 2020 2020 2020 2020  600,.           
 0000d120: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000d130: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000d140: 2020 2020 2020 2077 6964 7468 3a20 666c         width: fl
-0000d150: 6f61 7420 3d20 3630 3020 2a20 474f 4c44  oat = 600 * GOLD
-0000d160: 454e 5f52 4154 494f 2920 2d3e 2070 6c6f  EN_RATIO) -> plo
-0000d170: 746c 792e 6772 6170 685f 6f62 6a65 6374  tly.graph_object
-0000d180: 732e 4669 6775 7265 3a0a 2020 2020 2020  s.Figure:.      
-0000d190: 2020 2222 220a 2020 2020 2020 2020 5265    """.        Re
-0000d1a0: 7475 726e 7320 6120 506c 6f74 6c79 2046  turns a Plotly F
-0000d1b0: 6967 7572 6520 2873 6361 7474 6572 2d70  igure (scatter-p
-0000d1c0: 6c6f 7420 7065 7220 6e75 6d65 7269 6320  lot per numeric 
-0000d1d0: 7061 7261 6d65 7465 7229 206f 6620 7468  parameter) of th
-0000d1e0: 6520 7061 7261 6d65 7465 7227 7320 7661  e parameter's va
-0000d1f0: 6c75 6573 2028 792d 6178 6973 2920 696e  lues (y-axis) in
-0000d200: 0a20 2020 2020 2020 206f 7264 6572 206f  .        order o
-0000d210: 6620 7472 6961 6c20 6578 6563 7574 696f  f trial executio
-0000d220: 6e20 2878 2d61 7869 7329 2e20 4573 7065  n (x-axis). Espe
-0000d230: 6369 616c 6c79 2075 7365 6675 6c20 666f  cially useful fo
-0000d240: 7220 652e 672e 2042 6179 6573 5365 6172  r e.g. BayesSear
-0000d250: 6368 4356 2e0a 0a20 2020 2020 2020 2041  chCV...        A
-0000d260: 7267 733a 0a20 2020 2020 2020 2020 2020  rgs:.           
-0000d270: 2071 7565 7279 3a0a 2020 2020 2020 2020   query:.        
-0000d280: 2020 2020 2020 2020 7374 7269 6e67 2074          string t
-0000d290: 6f20 6265 2070 6173 7365 6420 746f 2060  o be passed to `
-0000d2a0: 746f 5f64 6174 6166 7261 6d65 2829 603b  to_dataframe()`;
-0000d2b0: 2073 6565 2064 6f63 756d 656e 7461 7469   see documentati
-0000d2c0: 6f6e 2066 6f72 2074 6861 7420 6d65 7468  on for that meth
-0000d2d0: 6f64 2e0a 2020 2020 2020 2020 2020 2020  od..            
-0000d2e0: 6865 6967 6874 3a0a 2020 2020 2020 2020  height:.        
-0000d2f0: 2020 2020 2020 2020 5468 6520 6865 6967          The heig
-0000d300: 6874 206f 6620 7468 6520 706c 6f74 2e20  ht of the plot. 
-0000d310: 5468 6973 2076 616c 7565 2069 7320 7061  This value is pa
-0000d320: 7373 6564 2074 6f20 706c 6f74 6c79 2e0a  ssed to plotly..
-0000d330: 2020 2020 2020 2020 2020 2020 7769 6474              widt
-0000d340: 683a 0a20 2020 2020 2020 2020 2020 2020  h:.             
-0000d350: 2020 2054 6865 2077 6964 7468 206f 6620     The width of 
-0000d360: 7468 6520 706c 6f74 2e20 5468 6973 2076  the plot. This v
-0000d370: 616c 7565 2069 7320 7061 7373 6564 2074  alue is passed t
-0000d380: 6f20 706c 6f74 6c79 2e0a 2020 2020 2020  o plotly..      
-0000d390: 2020 2222 220a 2020 2020 2020 2020 636f    """.        co
-0000d3a0: 6c6f 725f 636f 6e74 696e 756f 7573 5f73  lor_continuous_s
-0000d3b0: 6361 6c65 203d 2070 782e 636f 6c6f 7273  cale = px.colors
-0000d3c0: 2e64 6976 6572 6769 6e67 2e52 6459 6c47  .diverging.RdYlG
-0000d3d0: 6e0a 2020 2020 2020 2020 6966 206e 6f74  n.        if not
-0000d3e0: 2073 656c 662e 6869 6768 6572 5f73 636f   self.higher_sco
-0000d3f0: 7265 5f69 735f 6265 7474 6572 3a0a 2020  re_is_better:.  
-0000d400: 2020 2020 2020 2020 2020 636f 6c6f 725f            color_
-0000d410: 636f 6e74 696e 756f 7573 5f73 6361 6c65  continuous_scale
-0000d420: 203d 2063 6f6c 6f72 5f63 6f6e 7469 6e75   = color_continu
-0000d430: 6f75 735f 7363 616c 652e 7265 7665 7273  ous_scale.revers
-0000d440: 6528 290a 0a20 2020 2020 2020 2073 636f  e()..        sco
-0000d450: 7265 5f63 6f6c 756d 6e20 3d20 7365 6c66  re_column = self
-0000d460: 2e70 7269 6d61 7279 5f73 636f 7265 5f6e  .primary_score_n
-0000d470: 616d 6520 2b20 2220 4d65 616e 220a 0a20  ame + " Mean".. 
-0000d480: 2020 2020 2020 206c 6162 656c 6564 5f64         labeled_d
-0000d490: 6620 3d20 7365 6c66 2e74 6f5f 6c61 6265  f = self.to_labe
-0000d4a0: 6c65 645f 6461 7461 6672 616d 6528 7175  led_dataframe(qu
-0000d4b0: 6572 793d 7175 6572 7929 2020 2020 0a20  ery=query)    . 
-0000d4c0: 2020 2020 2020 206c 6162 656c 6564 5f6c         labeled_l
-0000d4d0: 6f6e 6720 3d20 7064 2e6d 656c 7428 6c61  ong = pd.melt(la
-0000d4e0: 6265 6c65 645f 6466 2c0a 2020 2020 2020  beled_df,.      
+0000d140: 2077 6964 7468 3a20 666c 6f61 7420 3d20   width: float = 
+0000d150: 3630 3020 2a20 474f 4c44 454e 5f52 4154  600 * GOLDEN_RAT
+0000d160: 494f 2920 2d3e 2070 6c6f 746c 792e 6772  IO) -> plotly.gr
+0000d170: 6170 685f 6f62 6a65 6374 732e 4669 6775  aph_objects.Figu
+0000d180: 7265 3a0a 2020 2020 2020 2020 2222 220a  re:.        """.
+0000d190: 2020 2020 2020 2020 5265 7475 726e 7320          Returns 
+0000d1a0: 6120 506c 6f74 6c79 2046 6967 7572 6520  a Plotly Figure 
+0000d1b0: 2873 6361 7474 6572 2d70 6c6f 7420 7065  (scatter-plot pe
+0000d1c0: 7220 6e75 6d65 7269 6320 7061 7261 6d65  r numeric parame
+0000d1d0: 7465 7229 206f 6620 7468 6520 7061 7261  ter) of the para
+0000d1e0: 6d65 7465 7227 7320 7661 6c75 6573 2028  meter's values (
+0000d1f0: 792d 6178 6973 2920 696e 0a20 2020 2020  y-axis) in.     
+0000d200: 2020 206f 7264 6572 206f 6620 7472 6961     order of tria
+0000d210: 6c20 6578 6563 7574 696f 6e20 2878 2d61  l execution (x-a
+0000d220: 7869 7329 2e20 4573 7065 6369 616c 6c79  xis). Especially
+0000d230: 2075 7365 6675 6c20 666f 7220 652e 672e   useful for e.g.
+0000d240: 2042 6179 6573 5365 6172 6368 4356 2e0a   BayesSearchCV..
+0000d250: 0a20 2020 2020 2020 2041 7267 733a 0a20  .        Args:. 
+0000d260: 2020 2020 2020 2020 2020 2071 7565 7279             query
+0000d270: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
+0000d280: 2020 7374 7269 6e67 2074 6f20 6265 2070    string to be p
+0000d290: 6173 7365 6420 746f 2060 746f 5f64 6174  assed to `to_dat
+0000d2a0: 6166 7261 6d65 2829 603b 2073 6565 2064  aframe()`; see d
+0000d2b0: 6f63 756d 656e 7461 7469 6f6e 2066 6f72  ocumentation for
+0000d2c0: 2074 6861 7420 6d65 7468 6f64 2e0a 2020   that method..  
+0000d2d0: 2020 2020 2020 2020 2020 6865 6967 6874            height
+0000d2e0: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
+0000d2f0: 2020 5468 6520 6865 6967 6874 206f 6620    The height of 
+0000d300: 7468 6520 706c 6f74 2e20 5468 6973 2076  the plot. This v
+0000d310: 616c 7565 2069 7320 7061 7373 6564 2074  alue is passed t
+0000d320: 6f20 706c 6f74 6c79 2e0a 2020 2020 2020  o plotly..      
+0000d330: 2020 2020 2020 7769 6474 683a 0a20 2020        width:.   
+0000d340: 2020 2020 2020 2020 2020 2020 2054 6865               The
+0000d350: 2077 6964 7468 206f 6620 7468 6520 706c   width of the pl
+0000d360: 6f74 2e20 5468 6973 2076 616c 7565 2069  ot. This value i
+0000d370: 7320 7061 7373 6564 2074 6f20 706c 6f74  s passed to plot
+0000d380: 6c79 2e0a 2020 2020 2020 2020 2222 220a  ly..        """.
+0000d390: 2020 2020 2020 2020 636f 6c6f 725f 636f          color_co
+0000d3a0: 6e74 696e 756f 7573 5f73 6361 6c65 203d  ntinuous_scale =
+0000d3b0: 2070 782e 636f 6c6f 7273 2e64 6976 6572   px.colors.diver
+0000d3c0: 6769 6e67 2e52 6459 6c47 6e0a 2020 2020  ging.RdYlGn.    
+0000d3d0: 2020 2020 6966 206e 6f74 2073 656c 662e      if not self.
+0000d3e0: 6869 6768 6572 5f73 636f 7265 5f69 735f  higher_score_is_
+0000d3f0: 6265 7474 6572 3a0a 2020 2020 2020 2020  better:.        
+0000d400: 2020 2020 636f 6c6f 725f 636f 6e74 696e      color_contin
+0000d410: 756f 7573 5f73 6361 6c65 203d 2063 6f6c  uous_scale = col
+0000d420: 6f72 5f63 6f6e 7469 6e75 6f75 735f 7363  or_continuous_sc
+0000d430: 616c 652e 7265 7665 7273 6528 290a 0a20  ale.reverse().. 
+0000d440: 2020 2020 2020 2073 636f 7265 5f63 6f6c         score_col
+0000d450: 756d 6e20 3d20 7365 6c66 2e70 7269 6d61  umn = self.prima
+0000d460: 7279 5f73 636f 7265 5f6e 616d 6520 2b20  ry_score_name + 
+0000d470: 2220 4d65 616e 220a 0a20 2020 2020 2020  " Mean"..       
+0000d480: 206c 6162 656c 6564 5f64 6620 3d20 7365   labeled_df = se
+0000d490: 6c66 2e74 6f5f 6c61 6265 6c65 645f 6461  lf.to_labeled_da
+0000d4a0: 7461 6672 616d 6528 7175 6572 793d 7175  taframe(query=qu
+0000d4b0: 6572 7929 2020 2020 0a20 2020 2020 2020  ery)    .       
+0000d4c0: 206c 6162 656c 6564 5f6c 6f6e 6720 3d20   labeled_long = 
+0000d4d0: 7064 2e6d 656c 7428 6c61 6265 6c65 645f  pd.melt(labeled_
+0000d4e0: 6466 2c0a 2020 2020 2020 2020 2020 2020  df,.            
 0000d4f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000d500: 2020 2020 2020 2020 2069 645f 7661 7273           id_vars
-0000d510: 3d5b 2754 7269 616c 2049 6e64 6578 272c  =['Trial Index',
-0000d520: 2073 636f 7265 5f63 6f6c 756d 6e2c 2027   score_column, '
-0000d530: 6c61 6265 6c27 5d2c 0a20 2020 2020 2020  label'],.       
+0000d500: 2020 2069 645f 7661 7273 3d5b 2754 7269     id_vars=['Tri
+0000d510: 616c 2049 6e64 6578 272c 2073 636f 7265  al Index', score
+0000d520: 5f63 6f6c 756d 6e2c 2027 6c61 6265 6c27  _column, 'label'
+0000d530: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
 0000d540: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000d550: 2020 2020 2020 2020 7661 6c75 655f 7661          value_va
-0000d560: 7273 3d5b 7820 666f 7220 7820 696e 2073  rs=[x for x in s
-0000d570: 656c 662e 6e75 6d65 7269 635f 7061 7261  elf.numeric_para
-0000d580: 6d65 7465 7273 2069 6620 7820 696e 206c  meters if x in l
-0000d590: 6162 656c 6564 5f64 662e 636f 6c75 6d6e  abeled_df.column
-0000d5a0: 735d 2c0a 2020 2020 2020 2020 2020 2020  s],.            
-0000d5b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000d5c0: 2020 2076 6172 5f6e 616d 653d 2770 6172     var_name='par
-0000d5d0: 616d 6574 6572 2729 0a0a 2020 2020 2020  ameter')..      
-0000d5e0: 2020 6669 6720 3d20 7078 2e73 6361 7474    fig = px.scatt
-0000d5f0: 6572 280a 2020 2020 2020 2020 2020 2020  er(.            
-0000d600: 6461 7461 5f66 7261 6d65 3d6c 6162 656c  data_frame=label
-0000d610: 6564 5f6c 6f6e 672c 0a20 2020 2020 2020  ed_long,.       
-0000d620: 2020 2020 2078 3d27 5472 6961 6c20 496e       x='Trial In
-0000d630: 6465 7827 2c0a 2020 2020 2020 2020 2020  dex',.          
-0000d640: 2020 793d 2776 616c 7565 272c 0a20 2020    y='value',.   
-0000d650: 2020 2020 2020 2020 2063 6f6c 6f72 3d73           color=s
-0000d660: 636f 7265 5f63 6f6c 756d 6e2c 0a20 2020  core_column,.   
-0000d670: 2020 2020 2020 2020 2063 6f6c 6f72 5f63           color_c
-0000d680: 6f6e 7469 6e75 6f75 735f 7363 616c 653d  ontinuous_scale=
-0000d690: 636f 6c6f 725f 636f 6e74 696e 756f 7573  color_continuous
-0000d6a0: 5f73 6361 6c65 2c0a 2020 2020 2020 2020  _scale,.        
-0000d6b0: 2020 2020 6661 6365 745f 636f 6c3d 2770      facet_col='p
-0000d6c0: 6172 616d 6574 6572 272c 0a20 2020 2020  arameter',.     
-0000d6d0: 2020 2020 2020 2066 6163 6574 5f63 6f6c         facet_col
-0000d6e0: 5f77 7261 703d 332c 0a20 2020 2020 2020  _wrap=3,.       
-0000d6f0: 2020 2020 2074 7265 6e64 6c69 6e65 3d27       trendline='
-0000d700: 6c6f 7765 7373 272c 0a20 2020 2020 2020  lowess',.       
-0000d710: 2020 2020 206c 6162 656c 733d 7b0a 2020       labels={.  
-0000d720: 2020 2020 2020 2020 2020 2020 2020 2776                'v
-0000d730: 616c 7565 273a 2027 5061 7261 6d65 7465  alue': 'Paramete
-0000d740: 7220 5661 6c75 6527 2c0a 2020 2020 2020  r Value',.      
-0000d750: 2020 2020 2020 7d2c 0a20 2020 2020 2020        },.       
-0000d760: 2020 2020 2074 6974 6c65 3d22 5061 7261       title="Para
-0000d770: 6d65 7465 7220 5661 6c75 6573 2045 7661  meter Values Eva
-0000d780: 6c75 6174 6564 204f 7665 7220 5469 6d65  luated Over Time
-0000d790: 2028 4163 726f 7373 2054 7269 616c 7329   (Across Trials)
-0000d7a0: 3c62 723e 220a 2020 2020 2020 2020 2020  <br>".          
-0000d7b0: 2020 2020 2020 2020 223c 7375 703e 5468          "<sup>Th
-0000d7c0: 6973 2067 7261 7068 2073 686f 7773 2074  is graph shows t
-0000d7d0: 6865 2070 6172 616d 6574 6572 2076 616c  he parameter val
-0000d7e0: 7565 7320 6576 616c 7561 7465 6420 6163  ues evaluated ac
-0000d7f0: 726f 7373 2061 6c6c 2074 7269 616c 732e  ross all trials.
-0000d800: 3c62 723e 220a 2020 2020 2020 2020 2020  <br>".          
-0000d810: 2020 2020 2020 2020 2254 6865 2063 6f6c          "The col
-0000d820: 6f72 2063 6f72 7265 7370 6f6e 6473 2074  or corresponds t
-0000d830: 6f20 7468 6520 6176 6572 6167 6520 4356  o the average CV
-0000d840: 2073 636f 7265 2061 7373 6f63 6961 7465   score associate
-0000d850: 6420 7769 7468 2074 6861 7420 7472 6961  d with that tria
-0000d860: 6c2f 706f 696e 742e 3c2f 7375 703e 222c  l/point.</sup>",
-0000d870: 0a20 2020 2020 2020 2020 2020 2063 7573  .            cus
-0000d880: 746f 6d5f 6461 7461 3d5b 276c 6162 656c  tom_data=['label
-0000d890: 272c 2073 636f 7265 5f63 6f6c 756d 6e5d  ', score_column]
-0000d8a0: 2c0a 2020 2020 2020 2020 2020 2020 6865  ,.            he
-0000d8b0: 6967 6874 3d68 6569 6768 742c 0a20 2020  ight=height,.   
-0000d8c0: 2020 2020 2020 2020 2077 6964 7468 3d77           width=w
-0000d8d0: 6964 7468 2c0a 2020 2020 2020 2020 290a  idth,.        ).
-0000d8e0: 2020 2020 2020 2020 6669 672e 7570 6461          fig.upda
-0000d8f0: 7465 5f74 7261 6365 7328 0a20 2020 2020  te_traces(.     
-0000d900: 2020 2020 2020 2068 6f76 6572 7465 6d70         hovertemp
-0000d910: 6c61 7465 3d22 3c62 723e 222e 6a6f 696e  late="<br>".join
-0000d920: 285b 0a20 2020 2020 2020 2020 2020 2020  ([.             
-0000d930: 2020 2022 5472 6961 6c20 496e 6465 783a     "Trial Index:
-0000d940: 2025 7b78 7d22 2c0a 2020 2020 2020 2020   %{x}",.        
-0000d950: 2020 2020 2020 2020 2250 6172 616d 6574          "Paramet
-0000d960: 6572 2056 616c 7565 3a20 257b 797d 222c  er Value: %{y}",
-0000d970: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0000d980: 2073 636f 7265 5f63 6f6c 756d 6e20 2b20   score_column + 
-0000d990: 223a 2025 7b63 7573 746f 6d64 6174 615b  ": %{customdata[
-0000d9a0: 315d 7d22 2c0a 2020 2020 2020 2020 2020  1]}",.          
-0000d9b0: 2020 2020 2020 223c 6272 3e50 6172 616d        "<br>Param
-0000d9c0: 6574 6572 733a 2025 7b63 7573 746f 6d64  eters: %{customd
-0000d9d0: 6174 615b 305d 7d22 2c0a 2020 2020 2020  ata[0]}",.      
-0000d9e0: 2020 2020 2020 5d29 0a20 2020 2020 2020        ]).       
-0000d9f0: 2029 0a20 2020 2020 2020 2066 6967 2e75   ).        fig.u
-0000da00: 7064 6174 655f 7961 7865 7328 6d61 7463  pdate_yaxes(matc
-0000da10: 6865 733d 4e6f 6e65 2c20 7368 6f77 7469  hes=None, showti
-0000da20: 636b 6c61 6265 6c73 3d54 7275 6529 0a20  cklabels=True). 
-0000da30: 2020 2020 2020 2072 6574 7572 6e20 6669         return fi
-0000da40: 670a 0a20 2020 2064 6566 2070 6c6f 745f  g..    def plot_
-0000da50: 7061 7261 6c6c 656c 5f63 6f6f 7264 696e  parallel_coordin
-0000da60: 6174 6573 2873 656c 662c 0a20 2020 2020  ates(self,.     
+0000d550: 2020 7661 6c75 655f 7661 7273 3d5b 7820    value_vars=[x 
+0000d560: 666f 7220 7820 696e 2073 656c 662e 6e75  for x in self.nu
+0000d570: 6d65 7269 635f 7061 7261 6d65 7465 7273  meric_parameters
+0000d580: 2069 6620 7820 696e 206c 6162 656c 6564   if x in labeled
+0000d590: 5f64 662e 636f 6c75 6d6e 735d 2c0a 2020  _df.columns],.  
+0000d5a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000d5b0: 2020 2020 2020 2020 2020 2020 2076 6172               var
+0000d5c0: 5f6e 616d 653d 2770 6172 616d 6574 6572  _name='parameter
+0000d5d0: 2729 0a0a 2020 2020 2020 2020 6669 6720  ')..        fig 
+0000d5e0: 3d20 7078 2e73 6361 7474 6572 280a 2020  = px.scatter(.  
+0000d5f0: 2020 2020 2020 2020 2020 6461 7461 5f66            data_f
+0000d600: 7261 6d65 3d6c 6162 656c 6564 5f6c 6f6e  rame=labeled_lon
+0000d610: 672c 0a20 2020 2020 2020 2020 2020 2078  g,.            x
+0000d620: 3d27 5472 6961 6c20 496e 6465 7827 2c0a  ='Trial Index',.
+0000d630: 2020 2020 2020 2020 2020 2020 793d 2776              y='v
+0000d640: 616c 7565 272c 0a20 2020 2020 2020 2020  alue',.         
+0000d650: 2020 2063 6f6c 6f72 3d73 636f 7265 5f63     color=score_c
+0000d660: 6f6c 756d 6e2c 0a20 2020 2020 2020 2020  olumn,.         
+0000d670: 2020 2063 6f6c 6f72 5f63 6f6e 7469 6e75     color_continu
+0000d680: 6f75 735f 7363 616c 653d 636f 6c6f 725f  ous_scale=color_
+0000d690: 636f 6e74 696e 756f 7573 5f73 6361 6c65  continuous_scale
+0000d6a0: 2c0a 2020 2020 2020 2020 2020 2020 6661  ,.            fa
+0000d6b0: 6365 745f 636f 6c3d 2770 6172 616d 6574  cet_col='paramet
+0000d6c0: 6572 272c 0a20 2020 2020 2020 2020 2020  er',.           
+0000d6d0: 2066 6163 6574 5f63 6f6c 5f77 7261 703d   facet_col_wrap=
+0000d6e0: 332c 0a20 2020 2020 2020 2020 2020 2074  3,.            t
+0000d6f0: 7265 6e64 6c69 6e65 3d27 6c6f 7765 7373  rendline='lowess
+0000d700: 272c 0a20 2020 2020 2020 2020 2020 206c  ',.            l
+0000d710: 6162 656c 733d 7b0a 2020 2020 2020 2020  abels={.        
+0000d720: 2020 2020 2020 2020 2776 616c 7565 273a          'value':
+0000d730: 2027 5061 7261 6d65 7465 7220 5661 6c75   'Parameter Valu
+0000d740: 6527 2c0a 2020 2020 2020 2020 2020 2020  e',.            
+0000d750: 7d2c 0a20 2020 2020 2020 2020 2020 2074  },.            t
+0000d760: 6974 6c65 3d22 5061 7261 6d65 7465 7220  itle="Parameter 
+0000d770: 5661 6c75 6573 2045 7661 6c75 6174 6564  Values Evaluated
+0000d780: 204f 7665 7220 5469 6d65 2028 4163 726f   Over Time (Acro
+0000d790: 7373 2054 7269 616c 7329 3c62 723e 220a  ss Trials)<br>".
+0000d7a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000d7b0: 2020 223c 7375 703e 5468 6973 2067 7261    "<sup>This gra
+0000d7c0: 7068 2073 686f 7773 2074 6865 2070 6172  ph shows the par
+0000d7d0: 616d 6574 6572 2076 616c 7565 7320 6576  ameter values ev
+0000d7e0: 616c 7561 7465 6420 6163 726f 7373 2061  aluated across a
+0000d7f0: 6c6c 2074 7269 616c 732e 3c62 723e 220a  ll trials.<br>".
+0000d800: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000d810: 2020 2254 6865 2063 6f6c 6f72 2063 6f72    "The color cor
+0000d820: 7265 7370 6f6e 6473 2074 6f20 7468 6520  responds to the 
+0000d830: 6176 6572 6167 6520 4356 2073 636f 7265  average CV score
+0000d840: 2061 7373 6f63 6961 7465 6420 7769 7468   associated with
+0000d850: 2074 6861 7420 7472 6961 6c2f 706f 696e   that trial/poin
+0000d860: 742e 3c2f 7375 703e 222c 0a20 2020 2020  t.</sup>",.     
+0000d870: 2020 2020 2020 2063 7573 746f 6d5f 6461         custom_da
+0000d880: 7461 3d5b 276c 6162 656c 272c 2073 636f  ta=['label', sco
+0000d890: 7265 5f63 6f6c 756d 6e5d 2c0a 2020 2020  re_column],.    
+0000d8a0: 2020 2020 2020 2020 6865 6967 6874 3d68          height=h
+0000d8b0: 6569 6768 742c 0a20 2020 2020 2020 2020  eight,.         
+0000d8c0: 2020 2077 6964 7468 3d77 6964 7468 2c0a     width=width,.
+0000d8d0: 2020 2020 2020 2020 290a 2020 2020 2020          ).      
+0000d8e0: 2020 6669 672e 7570 6461 7465 5f74 7261    fig.update_tra
+0000d8f0: 6365 7328 0a20 2020 2020 2020 2020 2020  ces(.           
+0000d900: 2068 6f76 6572 7465 6d70 6c61 7465 3d22   hovertemplate="
+0000d910: 3c62 723e 222e 6a6f 696e 285b 0a20 2020  <br>".join([.   
+0000d920: 2020 2020 2020 2020 2020 2020 2022 5472               "Tr
+0000d930: 6961 6c20 496e 6465 783a 2025 7b78 7d22  ial Index: %{x}"
+0000d940: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+0000d950: 2020 2250 6172 616d 6574 6572 2056 616c    "Parameter Val
+0000d960: 7565 3a20 257b 797d 222c 0a20 2020 2020  ue: %{y}",.     
+0000d970: 2020 2020 2020 2020 2020 2073 636f 7265             score
+0000d980: 5f63 6f6c 756d 6e20 2b20 223a 2025 7b63  _column + ": %{c
+0000d990: 7573 746f 6d64 6174 615b 315d 7d22 2c0a  ustomdata[1]}",.
+0000d9a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000d9b0: 223c 6272 3e50 6172 616d 6574 6572 733a  "<br>Parameters:
+0000d9c0: 2025 7b63 7573 746f 6d64 6174 615b 305d   %{customdata[0]
+0000d9d0: 7d22 2c0a 2020 2020 2020 2020 2020 2020  }",.            
+0000d9e0: 5d29 0a20 2020 2020 2020 2029 0a20 2020  ]).        ).   
+0000d9f0: 2020 2020 2066 6967 2e75 7064 6174 655f       fig.update_
+0000da00: 7961 7865 7328 6d61 7463 6865 733d 4e6f  yaxes(matches=No
+0000da10: 6e65 2c20 7368 6f77 7469 636b 6c61 6265  ne, showticklabe
+0000da20: 6c73 3d54 7275 6529 0a20 2020 2020 2020  ls=True).       
+0000da30: 2072 6574 7572 6e20 6669 670a 0a20 2020   return fig..   
+0000da40: 2064 6566 2070 6c6f 745f 7061 7261 6c6c   def plot_parall
+0000da50: 656c 5f63 6f6f 7264 696e 6174 6573 2873  el_coordinates(s
+0000da60: 656c 662c 0a20 2020 2020 2020 2020 2020  elf,.           
 0000da70: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000da80: 2020 2020 2020 2020 2020 2020 2069 6e63               inc
-0000da90: 6c75 6465 5f61 6c6c 5f73 636f 7265 733a  lude_all_scores:
-0000daa0: 2062 6f6f 6c20 3d20 5472 7565 2c0a 2020   bool = True,.  
+0000da80: 2020 2020 2020 2069 6e63 6c75 6465 5f61         include_a
+0000da90: 6c6c 5f73 636f 7265 733a 2062 6f6f 6c20  ll_scores: bool 
+0000daa0: 3d20 5472 7565 2c0a 2020 2020 2020 2020  = True,.        
 0000dab0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000dac0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000dad0: 7175 6572 793a 2073 7472 203d 204e 6f6e  query: str = Non
-0000dae0: 652c 0a20 2020 2020 2020 2020 2020 2020  e,.             
-0000daf0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000db00: 2020 2020 2068 6569 6768 743a 2066 6c6f       height: flo
-0000db10: 6174 203d 2036 3030 2c0a 2020 2020 2020  at = 600,.      
+0000dac0: 2020 2020 2020 2020 2020 7175 6572 793a            query:
+0000dad0: 2073 7472 203d 204e 6f6e 652c 0a20 2020   str = None,.   
+0000dae0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000daf0: 2020 2020 2020 2020 2020 2020 2020 2068                 h
+0000db00: 6569 6768 743a 2066 6c6f 6174 203d 2036  eight: float = 6
+0000db10: 3030 2c0a 2020 2020 2020 2020 2020 2020  00,.            
 0000db20: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000db30: 2020 2020 2020 2020 2020 2020 7769 6474              widt
-0000db40: 683a 2066 6c6f 6174 203d 2036 3030 202a  h: float = 600 *
-0000db50: 2047 4f4c 4445 4e5f 5241 5449 4f29 202d   GOLDEN_RATIO) -
-0000db60: 3e20 706c 6f74 6c79 2e67 7261 7068 5f6f  > plotly.graph_o
-0000db70: 626a 6563 7473 2e46 6967 7572 653a 0a20  bjects.Figure:. 
-0000db80: 2020 2020 2020 2022 2222 0a20 2020 2020         """.     
-0000db90: 2020 2052 6574 7572 6e73 2061 2050 6c6f     Returns a Plo
-0000dba0: 746c 7920 4669 6775 7265 2028 7061 7261  tly Figure (para
-0000dbb0: 6c6c 656c 2d63 6f6f 7264 696e 6174 6573  llel-coordinates
-0000dbc0: 2920 6f66 2074 6865 206e 756d 6572 6963  ) of the numeric
-0000dbd0: 2070 6172 616d 6574 6572 7327 2076 616c   parameters' val
-0000dbe0: 7565 7320 2879 2d61 7869 7329 2c20 616c  ues (y-axis), al
-0000dbf0: 6f6e 6720 7769 7468 0a20 2020 2020 2020  ong with.       
-0000dc00: 2074 6865 2063 6f72 7265 7370 6f6e 6469   the correspondi
-0000dc10: 6e67 2073 636f 7265 2061 7665 7261 6765  ng score average
-0000dc20: 732e 0a0a 2020 2020 2020 2020 4172 6773  s...        Args
-0000dc30: 3a0a 2020 2020 2020 2020 2020 2020 696e  :.            in
-0000dc40: 636c 7564 655f 616c 6c5f 7363 6f72 6573  clude_all_scores
-0000dc50: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
-0000dc60: 2020 4f6e 6c79 2061 7070 6c69 6361 626c    Only applicabl
-0000dc70: 6520 6966 2074 6865 2072 6573 756c 7473  e if the results
-0000dc80: 2068 6176 6520 6d75 6c74 6970 6c65 2073   have multiple s
-0000dc90: 636f 7265 732e 0a20 2020 2020 2020 2020  cores..         
-0000dca0: 2020 2020 2020 2049 6620 5472 7565 2c20         If True, 
-0000dcb0: 696e 636c 7564 6573 2061 6c6c 206f 6620  includes all of 
-0000dcc0: 7468 6520 7363 6f72 6573 2e20 4966 2046  the scores. If F
-0000dcd0: 616c 7365 2c20 696e 636c 7564 6573 206f  alse, includes o
-0000dce0: 6e6c 7920 7468 6520 7072 696d 6172 7920  nly the primary 
-0000dcf0: 7363 6f72 652e 0a20 2020 2020 2020 2020  score..         
-0000dd00: 2020 2071 7565 7279 3a0a 2020 2020 2020     query:.      
-0000dd10: 2020 2020 2020 2020 2020 7374 7269 6e67            string
-0000dd20: 2074 6f20 6265 2070 6173 7365 6420 746f   to be passed to
-0000dd30: 2060 746f 5f64 6174 6166 7261 6d65 2829   `to_dataframe()
-0000dd40: 603b 2073 6565 2064 6f63 756d 656e 7461  `; see documenta
-0000dd50: 7469 6f6e 2066 6f72 2074 6861 7420 6d65  tion for that me
-0000dd60: 7468 6f64 2e0a 2020 2020 2020 2020 2020  thod..          
-0000dd70: 2020 6865 6967 6874 3a0a 2020 2020 2020    height:.      
-0000dd80: 2020 2020 2020 2020 2020 5468 6520 6865            The he
-0000dd90: 6967 6874 206f 6620 7468 6520 706c 6f74  ight of the plot
-0000dda0: 2e20 5468 6973 2076 616c 7565 2069 7320  . This value is 
-0000ddb0: 7061 7373 6564 2074 6f20 706c 6f74 6c79  passed to plotly
-0000ddc0: 2e0a 2020 2020 2020 2020 2020 2020 7769  ..            wi
-0000ddd0: 6474 683a 0a20 2020 2020 2020 2020 2020  dth:.           
-0000dde0: 2020 2020 2054 6865 2077 6964 7468 206f       The width o
-0000ddf0: 6620 7468 6520 706c 6f74 2e20 5468 6973  f the plot. This
-0000de00: 2076 616c 7565 2069 7320 7061 7373 6564   value is passed
-0000de10: 2074 6f20 706c 6f74 6c79 2e0a 2020 2020   to plotly..    
-0000de20: 2020 2020 2222 220a 2020 2020 2020 2020      """.        
-0000de30: 636f 6c6f 725f 636f 6e74 696e 756f 7573  color_continuous
-0000de40: 5f73 6361 6c65 203d 2070 782e 636f 6c6f  _scale = px.colo
-0000de50: 7273 2e64 6976 6572 6769 6e67 2e52 6459  rs.diverging.RdY
-0000de60: 6c47 6e0a 2020 2020 2020 2020 6966 206e  lGn.        if n
-0000de70: 6f74 2073 656c 662e 6869 6768 6572 5f73  ot self.higher_s
-0000de80: 636f 7265 5f69 735f 6265 7474 6572 3a0a  core_is_better:.
-0000de90: 2020 2020 2020 2020 2020 2020 636f 6c6f              colo
-0000dea0: 725f 636f 6e74 696e 756f 7573 5f73 6361  r_continuous_sca
-0000deb0: 6c65 203d 2063 6f6c 6f72 5f63 6f6e 7469  le = color_conti
-0000dec0: 6e75 6f75 735f 7363 616c 652e 7265 7665  nuous_scale.reve
-0000ded0: 7273 6528 290a 0a20 2020 2020 2020 2070  rse()..        p
-0000dee0: 7269 6d61 7279 5f73 636f 7265 5f63 6f6c  rimary_score_col
-0000def0: 756d 6e20 3d20 7365 6c66 2e70 7269 6d61  umn = self.prima
-0000df00: 7279 5f73 636f 7265 5f6e 616d 6520 2b20  ry_score_name + 
-0000df10: 2220 4d65 616e 220a 0a20 2020 2020 2020  " Mean"..       
-0000df20: 2069 6620 696e 636c 7564 655f 616c 6c5f   if include_all_
-0000df30: 7363 6f72 6573 3a0a 2020 2020 2020 2020  scores:.        
-0000df40: 2020 2020 7363 6f72 655f 636f 6c75 6d6e      score_column
-0000df50: 7320 3d20 5b73 636f 7265 202b 2022 204d  s = [score + " M
-0000df60: 6561 6e22 2066 6f72 2073 636f 7265 2069  ean" for score i
-0000df70: 6e20 7365 6c66 2e73 636f 7265 5f6e 616d  n self.score_nam
-0000df80: 6573 5d0a 2020 2020 2020 2020 656c 7365  es].        else
-0000df90: 3a0a 2020 2020 2020 2020 2020 2020 7363  :.            sc
-0000dfa0: 6f72 655f 636f 6c75 6d6e 7320 3d20 5b70  ore_columns = [p
-0000dfb0: 7269 6d61 7279 5f73 636f 7265 5f63 6f6c  rimary_score_col
-0000dfc0: 756d 6e5d 0a0a 2020 2020 2020 2020 2320  umn]..        # 
-0000dfd0: 4e4f 5445 3a20 736f 7274 5f62 795f 7363  NOTE: sort_by_sc
-0000dfe0: 6f72 653d 4661 6c73 6520 6265 6361 7573  ore=False becaus
-0000dff0: 6520 7468 6572 6520 6973 2061 2077 6569  e there is a wei
-0000e000: 7264 2062 7567 2069 6e20 706c 6f74 6c79  rd bug in plotly
-0000e010: 2073 7563 6820 7468 6174 2069 6620 7468   such that if th
-0000e020: 6520 696e 6465 7820 6973 0a20 2020 2020  e index is.     
-0000e030: 2020 2023 206e 6f74 2030 2d78 2074 6861     # not 0-x tha
-0000e040: 6e20 7468 6520 6f72 6465 7220 7365 656d  n the order seem
-0000e050: 7320 746f 2067 6574 206d 6573 7365 6420  s to get messed 
-0000e060: 7570 0a20 2020 2020 2020 2023 2068 7474  up.        # htt
-0000e070: 7073 3a2f 2f67 6974 6875 622e 636f 6d2f  ps://github.com/
-0000e080: 706c 6f74 6c79 2f70 6c6f 746c 792e 7079  plotly/plotly.py
-0000e090: 2f69 7373 7565 732f 3335 3736 0a20 2020  /issues/3576.   
-0000e0a0: 2020 2020 2023 2068 7474 7073 3a2f 2f67       # https://g
-0000e0b0: 6974 6875 622e 636f 6d2f 706c 6f74 6c79  ithub.com/plotly
-0000e0c0: 2f70 6c6f 746c 792e 7079 2f69 7373 7565  /plotly.py/issue
-0000e0d0: 732f 3335 3737 0a20 2020 2020 2020 2064  s/3577.        d
-0000e0e0: 6620 3d20 7365 6c66 2e74 6f5f 6461 7461  f = self.to_data
-0000e0f0: 6672 616d 6528 736f 7274 5f62 795f 7363  frame(sort_by_sc
-0000e100: 6f72 653d 4661 6c73 652c 2071 7565 7279  ore=False, query
-0000e110: 3d71 7565 7279 290a 2020 2020 2020 2020  =query).        
-0000e120: 6e75 6d65 7269 635f 636f 6c75 6d6e 7320  numeric_columns 
-0000e130: 3d20 5b78 2066 6f72 2078 2069 6e20 7365  = [x for x in se
-0000e140: 6c66 2e6e 756d 6572 6963 5f70 6172 616d  lf.numeric_param
-0000e150: 6574 6572 7320 6966 2078 2069 6e20 6466  eters if x in df
-0000e160: 2e63 6f6c 756d 6e73 5d0a 2020 2020 2020  .columns].      
-0000e170: 2020 6669 6720 3d20 7078 2e70 6172 616c    fig = px.paral
-0000e180: 6c65 6c5f 636f 6f72 6469 6e61 7465 7328  lel_coordinates(
-0000e190: 0a20 2020 2020 2020 2020 2020 2064 665b  .            df[
-0000e1a0: 6e75 6d65 7269 635f 636f 6c75 6d6e 7320  numeric_columns 
-0000e1b0: 2b20 7363 6f72 655f 636f 6c75 6d6e 735d  + score_columns]
-0000e1c0: 2e64 726f 706e 6128 6178 6973 3d30 292c  .dropna(axis=0),
-0000e1d0: 0a20 2020 2020 2020 2020 2020 2063 6f6c  .            col
-0000e1e0: 6f72 3d70 7269 6d61 7279 5f73 636f 7265  or=primary_score
-0000e1f0: 5f63 6f6c 756d 6e2c 0a20 2020 2020 2020  _column,.       
-0000e200: 2020 2020 2063 6f6c 6f72 5f63 6f6e 7469       color_conti
-0000e210: 6e75 6f75 735f 7363 616c 653d 636f 6c6f  nuous_scale=colo
-0000e220: 725f 636f 6e74 696e 756f 7573 5f73 6361  r_continuous_sca
-0000e230: 6c65 2c0a 2020 2020 2020 2020 2020 2020  le,.            
-0000e240: 6865 6967 6874 3d68 6569 6768 742c 0a20  height=height,. 
-0000e250: 2020 2020 2020 2020 2020 2077 6964 7468             width
-0000e260: 3d77 6964 7468 2c0a 2020 2020 2020 2020  =width,.        
-0000e270: 2020 2020 7469 746c 653d 2250 6172 616c      title="Paral
-0000e280: 6c65 6c20 436f 6f72 6469 6e61 7465 7320  lel Coordinates 
-0000e290: 6f66 2048 7970 6572 2d50 6172 616d 6574  of Hyper-Paramet
-0000e2a0: 6572 7320 616e 6420 5363 6f72 6520 4176  ers and Score Av
-0000e2b0: 6572 6167 6573 3c62 723e 220a 2020 2020  erages<br>".    
-0000e2c0: 2020 2020 290a 2020 2020 2020 2020 2320      ).        # 
-0000e2d0: 706c 6f74 6c79 2e6f 6666 6c69 6e65 2e70  plotly.offline.p
-0000e2e0: 6c6f 7428 6669 672c 2066 696c 656e 616d  lot(fig, filenam
-0000e2f0: 653d 2774 656d 702e 6874 6d6c 272c 2061  e='temp.html', a
-0000e300: 7574 6f5f 6f70 656e 3d54 7275 6529 0a20  uto_open=True). 
-0000e310: 2020 2020 2020 2072 6574 7572 6e20 6669         return fi
-0000e320: 670a 0a20 2020 2064 6566 2070 6c6f 745f  g..    def plot_
-0000e330: 7363 6174 7465 725f 6d61 7472 6978 2873  scatter_matrix(s
-0000e340: 656c 662c 0a20 2020 2020 2020 2020 2020  elf,.           
-0000e350: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000e360: 2069 6e63 6c75 6465 5f61 6c6c 5f73 636f   include_all_sco
-0000e370: 7265 733a 2062 6f6f 6c20 3d20 5472 7565  res: bool = True
-0000e380: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-0000e390: 2020 2020 2020 2020 2020 2020 2020 7175                qu
-0000e3a0: 6572 793a 2073 7472 203d 204e 6f6e 652c  ery: str = None,
-0000e3b0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0000e3c0: 2020 2020 2020 2020 2020 2020 2068 6569               hei
-0000e3d0: 6768 743a 2066 6c6f 6174 203d 2036 3030  ght: float = 600
-0000e3e0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-0000e3f0: 2020 2020 2020 2020 2020 2020 2020 7769                wi
-0000e400: 6474 683a 2066 6c6f 6174 203d 2036 3030  dth: float = 600
-0000e410: 202a 2047 4f4c 4445 4e5f 5241 5449 4f29   * GOLDEN_RATIO)
-0000e420: 202d 3e20 706c 6f74 6c79 2e67 7261 7068   -> plotly.graph
-0000e430: 5f6f 626a 6563 7473 2e46 6967 7572 653a  _objects.Figure:
-0000e440: 0a20 2020 2020 2020 2022 2222 0a20 2020  .        """.   
-0000e450: 2020 2020 2052 6574 7572 6e73 2061 2050       Returns a P
-0000e460: 6c6f 746c 7920 4669 6775 7265 2028 7363  lotly Figure (sc
-0000e470: 6174 7465 722d 6d61 7472 6978 2920 6f66  atter-matrix) of
-0000e480: 2074 6865 2061 6c6c 2070 6172 616d 6574   the all paramet
-0000e490: 6572 7320 616e 6420 7363 6f72 6573 2e0a  ers and scores..
-0000e4a0: 0a20 2020 2020 2020 2041 7267 733a 0a20  .        Args:. 
-0000e4b0: 2020 2020 2020 2020 2020 2069 6e63 6c75             inclu
-0000e4c0: 6465 5f61 6c6c 5f73 636f 7265 733a 0a20  de_all_scores:. 
-0000e4d0: 2020 2020 2020 2020 2020 2020 2020 204f                 O
-0000e4e0: 6e6c 7920 6170 706c 6963 6162 6c65 2069  nly applicable i
-0000e4f0: 6620 7468 6520 7265 7375 6c74 7320 6861  f the results ha
-0000e500: 7665 206d 756c 7469 706c 6520 7363 6f72  ve multiple scor
-0000e510: 6573 2e0a 2020 2020 2020 2020 2020 2020  es..            
-0000e520: 2020 2020 4966 2054 7275 652c 2069 6e63      If True, inc
-0000e530: 6c75 6465 7320 616c 6c20 6f66 2074 6865  ludes all of the
-0000e540: 2073 636f 7265 732e 2049 6620 4661 6c73   scores. If Fals
-0000e550: 652c 2069 6e63 6c75 6465 7320 6f6e 6c79  e, includes only
-0000e560: 2074 6865 2070 7269 6d61 7279 2073 636f   the primary sco
-0000e570: 7265 2e0a 2020 2020 2020 2020 2020 2020  re..            
-0000e580: 7175 6572 793a 0a20 2020 2020 2020 2020  query:.         
-0000e590: 2020 2020 2020 2073 7472 696e 6720 746f         string to
-0000e5a0: 2062 6520 7061 7373 6564 2074 6f20 6074   be passed to `t
-0000e5b0: 6f5f 6461 7461 6672 616d 6528 2960 3b20  o_dataframe()`; 
-0000e5c0: 7365 6520 646f 6375 6d65 6e74 6174 696f  see documentatio
-0000e5d0: 6e20 666f 7220 7468 6174 206d 6574 686f  n for that metho
-0000e5e0: 642e 0a20 2020 2020 2020 2020 2020 2068  d..            h
-0000e5f0: 6569 6768 743a 0a20 2020 2020 2020 2020  eight:.         
-0000e600: 2020 2020 2020 2054 6865 2068 6569 6768         The heigh
-0000e610: 7420 6f66 2074 6865 2070 6c6f 742e 2054  t of the plot. T
-0000e620: 6869 7320 7661 6c75 6520 6973 2070 6173  his value is pas
-0000e630: 7365 6420 746f 2070 6c6f 746c 792e 0a20  sed to plotly.. 
-0000e640: 2020 2020 2020 2020 2020 2077 6964 7468             width
-0000e650: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
-0000e660: 2020 5468 6520 7769 6474 6820 6f66 2074    The width of t
-0000e670: 6865 2070 6c6f 742e 2054 6869 7320 7661  he plot. This va
-0000e680: 6c75 6520 6973 2070 6173 7365 6420 746f  lue is passed to
-0000e690: 2070 6c6f 746c 792e 0a20 2020 2020 2020   plotly..       
-0000e6a0: 2022 2222 0a20 2020 2020 2020 2063 6f6c   """.        col
-0000e6b0: 6f72 5f63 6f6e 7469 6e75 6f75 735f 7363  or_continuous_sc
-0000e6c0: 616c 6520 3d20 7078 2e63 6f6c 6f72 732e  ale = px.colors.
-0000e6d0: 6469 7665 7267 696e 672e 5264 596c 476e  diverging.RdYlGn
-0000e6e0: 0a20 2020 2020 2020 2069 6620 6e6f 7420  .        if not 
-0000e6f0: 7365 6c66 2e68 6967 6865 725f 7363 6f72  self.higher_scor
-0000e700: 655f 6973 5f62 6574 7465 723a 0a20 2020  e_is_better:.   
-0000e710: 2020 2020 2020 2020 2063 6f6c 6f72 5f63           color_c
-0000e720: 6f6e 7469 6e75 6f75 735f 7363 616c 6520  ontinuous_scale 
-0000e730: 3d20 636f 6c6f 725f 636f 6e74 696e 756f  = color_continuo
-0000e740: 7573 5f73 6361 6c65 2e72 6576 6572 7365  us_scale.reverse
-0000e750: 2829 0a0a 2020 2020 2020 2020 7072 696d  ()..        prim
-0000e760: 6172 795f 7363 6f72 655f 636f 6c75 6d6e  ary_score_column
-0000e770: 203d 2073 656c 662e 7072 696d 6172 795f   = self.primary_
-0000e780: 7363 6f72 655f 6e61 6d65 202b 2022 204d  score_name + " M
-0000e790: 6561 6e22 0a0a 2020 2020 2020 2020 6966  ean"..        if
-0000e7a0: 2069 6e63 6c75 6465 5f61 6c6c 5f73 636f   include_all_sco
-0000e7b0: 7265 733a 0a20 2020 2020 2020 2020 2020  res:.           
-0000e7c0: 2073 636f 7265 5f63 6f6c 756d 6e73 203d   score_columns =
-0000e7d0: 205b 7363 6f72 6520 2b20 2220 4d65 616e   [score + " Mean
-0000e7e0: 2220 666f 7220 7363 6f72 6520 696e 2073  " for score in s
-0000e7f0: 656c 662e 7363 6f72 655f 6e61 6d65 735d  elf.score_names]
-0000e800: 0a20 2020 2020 2020 2065 6c73 653a 0a20  .        else:. 
-0000e810: 2020 2020 2020 2020 2020 2073 636f 7265             score
-0000e820: 5f63 6f6c 756d 6e73 203d 205b 7072 696d  _columns = [prim
-0000e830: 6172 795f 7363 6f72 655f 636f 6c75 6d6e  ary_score_column
-0000e840: 5d0a 0a20 2020 2020 2020 2023 204e 4f54  ]..        # NOT
-0000e850: 453a 2073 6f72 745f 6279 5f73 636f 7265  E: sort_by_score
-0000e860: 3d46 616c 7365 2062 6563 6175 7365 2074  =False because t
-0000e870: 6865 7265 2069 7320 6120 7765 6972 6420  here is a weird 
-0000e880: 6275 6720 696e 2070 6c6f 746c 7920 7375  bug in plotly su
-0000e890: 6368 2074 6861 7420 6966 2074 6865 2069  ch that if the i
-0000e8a0: 6e64 6578 2069 730a 2020 2020 2020 2020  ndex is.        
-0000e8b0: 2320 6e6f 7420 302d 7820 7468 616e 2074  # not 0-x than t
-0000e8c0: 6865 206f 7264 6572 2073 6565 6d73 2074  he order seems t
-0000e8d0: 6f20 6765 7420 6d65 7373 6564 2075 700a  o get messed up.
-0000e8e0: 2020 2020 2020 2020 2320 6874 7470 733a          # https:
-0000e8f0: 2f2f 6769 7468 7562 2e63 6f6d 2f70 6c6f  //github.com/plo
-0000e900: 746c 792f 706c 6f74 6c79 2e70 792f 6973  tly/plotly.py/is
-0000e910: 7375 6573 2f33 3537 360a 2020 2020 2020  sues/3576.      
-0000e920: 2020 2320 6874 7470 733a 2f2f 6769 7468    # https://gith
-0000e930: 7562 2e63 6f6d 2f70 6c6f 746c 792f 706c  ub.com/plotly/pl
-0000e940: 6f74 6c79 2e70 792f 6973 7375 6573 2f33  otly.py/issues/3
-0000e950: 3537 370a 2020 2020 2020 2020 6466 203d  577.        df =
-0000e960: 2073 656c 662e 746f 5f64 6174 6166 7261   self.to_datafra
-0000e970: 6d65 2873 6f72 745f 6279 5f73 636f 7265  me(sort_by_score
-0000e980: 3d46 616c 7365 2c20 7175 6572 793d 7175  =False, query=qu
-0000e990: 6572 7929 0a20 2020 2020 2020 2063 6f6c  ery).        col
-0000e9a0: 756d 6e73 203d 205b 7820 666f 7220 7820  umns = [x for x 
-0000e9b0: 696e 2073 656c 662e 7061 7261 6d65 7465  in self.paramete
-0000e9c0: 725f 6e61 6d65 7320 6966 2078 2069 6e20  r_names if x in 
-0000e9d0: 6466 2e63 6f6c 756d 6e73 5d0a 2020 2020  df.columns].    
-0000e9e0: 2020 2020 6669 6720 3d20 7078 2e73 6361      fig = px.sca
-0000e9f0: 7474 6572 5f6d 6174 7269 7828 6466 5b73  tter_matrix(df[s
-0000ea00: 636f 7265 5f63 6f6c 756d 6e73 202b 2063  core_columns + c
-0000ea10: 6f6c 756d 6e73 5d2c 0a20 2020 2020 2020  olumns],.       
+0000db30: 2020 2020 2020 7769 6474 683a 2066 6c6f        width: flo
+0000db40: 6174 203d 2036 3030 202a 2047 4f4c 4445  at = 600 * GOLDE
+0000db50: 4e5f 5241 5449 4f29 202d 3e20 706c 6f74  N_RATIO) -> plot
+0000db60: 6c79 2e67 7261 7068 5f6f 626a 6563 7473  ly.graph_objects
+0000db70: 2e46 6967 7572 653a 0a20 2020 2020 2020  .Figure:.       
+0000db80: 2022 2222 0a20 2020 2020 2020 2052 6574   """.        Ret
+0000db90: 7572 6e73 2061 2050 6c6f 746c 7920 4669  urns a Plotly Fi
+0000dba0: 6775 7265 2028 7061 7261 6c6c 656c 2d63  gure (parallel-c
+0000dbb0: 6f6f 7264 696e 6174 6573 2920 6f66 2074  oordinates) of t
+0000dbc0: 6865 206e 756d 6572 6963 2070 6172 616d  he numeric param
+0000dbd0: 6574 6572 7327 2076 616c 7565 7320 2879  eters' values (y
+0000dbe0: 2d61 7869 7329 2c20 616c 6f6e 6720 7769  -axis), along wi
+0000dbf0: 7468 0a20 2020 2020 2020 2074 6865 2063  th.        the c
+0000dc00: 6f72 7265 7370 6f6e 6469 6e67 2073 636f  orresponding sco
+0000dc10: 7265 2061 7665 7261 6765 732e 0a0a 2020  re averages...  
+0000dc20: 2020 2020 2020 4172 6773 3a0a 2020 2020        Args:.    
+0000dc30: 2020 2020 2020 2020 696e 636c 7564 655f          include_
+0000dc40: 616c 6c5f 7363 6f72 6573 3a0a 2020 2020  all_scores:.    
+0000dc50: 2020 2020 2020 2020 2020 2020 4f6e 6c79              Only
+0000dc60: 2061 7070 6c69 6361 626c 6520 6966 2074   applicable if t
+0000dc70: 6865 2072 6573 756c 7473 2068 6176 6520  he results have 
+0000dc80: 6d75 6c74 6970 6c65 2073 636f 7265 732e  multiple scores.
+0000dc90: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0000dca0: 2049 6620 5472 7565 2c20 696e 636c 7564   If True, includ
+0000dcb0: 6573 2061 6c6c 206f 6620 7468 6520 7363  es all of the sc
+0000dcc0: 6f72 6573 2e20 4966 2046 616c 7365 2c20  ores. If False, 
+0000dcd0: 696e 636c 7564 6573 206f 6e6c 7920 7468  includes only th
+0000dce0: 6520 7072 696d 6172 7920 7363 6f72 652e  e primary score.
+0000dcf0: 0a20 2020 2020 2020 2020 2020 2071 7565  .            que
+0000dd00: 7279 3a0a 2020 2020 2020 2020 2020 2020  ry:.            
+0000dd10: 2020 2020 7374 7269 6e67 2074 6f20 6265      string to be
+0000dd20: 2070 6173 7365 6420 746f 2060 746f 5f64   passed to `to_d
+0000dd30: 6174 6166 7261 6d65 2829 603b 2073 6565  ataframe()`; see
+0000dd40: 2064 6f63 756d 656e 7461 7469 6f6e 2066   documentation f
+0000dd50: 6f72 2074 6861 7420 6d65 7468 6f64 2e0a  or that method..
+0000dd60: 2020 2020 2020 2020 2020 2020 6865 6967              heig
+0000dd70: 6874 3a0a 2020 2020 2020 2020 2020 2020  ht:.            
+0000dd80: 2020 2020 5468 6520 6865 6967 6874 206f      The height o
+0000dd90: 6620 7468 6520 706c 6f74 2e20 5468 6973  f the plot. This
+0000dda0: 2076 616c 7565 2069 7320 7061 7373 6564   value is passed
+0000ddb0: 2074 6f20 706c 6f74 6c79 2e0a 2020 2020   to plotly..    
+0000ddc0: 2020 2020 2020 2020 7769 6474 683a 0a20          width:. 
+0000ddd0: 2020 2020 2020 2020 2020 2020 2020 2054                 T
+0000dde0: 6865 2077 6964 7468 206f 6620 7468 6520  he width of the 
+0000ddf0: 706c 6f74 2e20 5468 6973 2076 616c 7565  plot. This value
+0000de00: 2069 7320 7061 7373 6564 2074 6f20 706c   is passed to pl
+0000de10: 6f74 6c79 2e0a 2020 2020 2020 2020 2222  otly..        ""
+0000de20: 220a 2020 2020 2020 2020 636f 6c6f 725f  ".        color_
+0000de30: 636f 6e74 696e 756f 7573 5f73 6361 6c65  continuous_scale
+0000de40: 203d 2070 782e 636f 6c6f 7273 2e64 6976   = px.colors.div
+0000de50: 6572 6769 6e67 2e52 6459 6c47 6e0a 2020  erging.RdYlGn.  
+0000de60: 2020 2020 2020 6966 206e 6f74 2073 656c        if not sel
+0000de70: 662e 6869 6768 6572 5f73 636f 7265 5f69  f.higher_score_i
+0000de80: 735f 6265 7474 6572 3a0a 2020 2020 2020  s_better:.      
+0000de90: 2020 2020 2020 636f 6c6f 725f 636f 6e74        color_cont
+0000dea0: 696e 756f 7573 5f73 6361 6c65 203d 2063  inuous_scale = c
+0000deb0: 6f6c 6f72 5f63 6f6e 7469 6e75 6f75 735f  olor_continuous_
+0000dec0: 7363 616c 652e 7265 7665 7273 6528 290a  scale.reverse().
+0000ded0: 0a20 2020 2020 2020 2070 7269 6d61 7279  .        primary
+0000dee0: 5f73 636f 7265 5f63 6f6c 756d 6e20 3d20  _score_column = 
+0000def0: 7365 6c66 2e70 7269 6d61 7279 5f73 636f  self.primary_sco
+0000df00: 7265 5f6e 616d 6520 2b20 2220 4d65 616e  re_name + " Mean
+0000df10: 220a 0a20 2020 2020 2020 2069 6620 696e  "..        if in
+0000df20: 636c 7564 655f 616c 6c5f 7363 6f72 6573  clude_all_scores
+0000df30: 3a0a 2020 2020 2020 2020 2020 2020 7363  :.            sc
+0000df40: 6f72 655f 636f 6c75 6d6e 7320 3d20 5b73  ore_columns = [s
+0000df50: 636f 7265 202b 2022 204d 6561 6e22 2066  core + " Mean" f
+0000df60: 6f72 2073 636f 7265 2069 6e20 7365 6c66  or score in self
+0000df70: 2e73 636f 7265 5f6e 616d 6573 5d0a 2020  .score_names].  
+0000df80: 2020 2020 2020 656c 7365 3a0a 2020 2020        else:.    
+0000df90: 2020 2020 2020 2020 7363 6f72 655f 636f          score_co
+0000dfa0: 6c75 6d6e 7320 3d20 5b70 7269 6d61 7279  lumns = [primary
+0000dfb0: 5f73 636f 7265 5f63 6f6c 756d 6e5d 0a0a  _score_column]..
+0000dfc0: 2020 2020 2020 2020 2320 4e4f 5445 3a20          # NOTE: 
+0000dfd0: 736f 7274 5f62 795f 7363 6f72 653d 4661  sort_by_score=Fa
+0000dfe0: 6c73 6520 6265 6361 7573 6520 7468 6572  lse because ther
+0000dff0: 6520 6973 2061 2077 6569 7264 2062 7567  e is a weird bug
+0000e000: 2069 6e20 706c 6f74 6c79 2073 7563 6820   in plotly such 
+0000e010: 7468 6174 2069 6620 7468 6520 696e 6465  that if the inde
+0000e020: 7820 6973 0a20 2020 2020 2020 2023 206e  x is.        # n
+0000e030: 6f74 2030 2d78 2074 6861 6e20 7468 6520  ot 0-x than the 
+0000e040: 6f72 6465 7220 7365 656d 7320 746f 2067  order seems to g
+0000e050: 6574 206d 6573 7365 6420 7570 0a20 2020  et messed up.   
+0000e060: 2020 2020 2023 2068 7474 7073 3a2f 2f67       # https://g
+0000e070: 6974 6875 622e 636f 6d2f 706c 6f74 6c79  ithub.com/plotly
+0000e080: 2f70 6c6f 746c 792e 7079 2f69 7373 7565  /plotly.py/issue
+0000e090: 732f 3335 3736 0a20 2020 2020 2020 2023  s/3576.        #
+0000e0a0: 2068 7474 7073 3a2f 2f67 6974 6875 622e   https://github.
+0000e0b0: 636f 6d2f 706c 6f74 6c79 2f70 6c6f 746c  com/plotly/plotl
+0000e0c0: 792e 7079 2f69 7373 7565 732f 3335 3737  y.py/issues/3577
+0000e0d0: 0a20 2020 2020 2020 2064 6620 3d20 7365  .        df = se
+0000e0e0: 6c66 2e74 6f5f 6461 7461 6672 616d 6528  lf.to_dataframe(
+0000e0f0: 736f 7274 5f62 795f 7363 6f72 653d 4661  sort_by_score=Fa
+0000e100: 6c73 652c 2071 7565 7279 3d71 7565 7279  lse, query=query
+0000e110: 290a 2020 2020 2020 2020 6e75 6d65 7269  ).        numeri
+0000e120: 635f 636f 6c75 6d6e 7320 3d20 5b78 2066  c_columns = [x f
+0000e130: 6f72 2078 2069 6e20 7365 6c66 2e6e 756d  or x in self.num
+0000e140: 6572 6963 5f70 6172 616d 6574 6572 7320  eric_parameters 
+0000e150: 6966 2078 2069 6e20 6466 2e63 6f6c 756d  if x in df.colum
+0000e160: 6e73 5d0a 2020 2020 2020 2020 6669 6720  ns].        fig 
+0000e170: 3d20 7078 2e70 6172 616c 6c65 6c5f 636f  = px.parallel_co
+0000e180: 6f72 6469 6e61 7465 7328 0a20 2020 2020  ordinates(.     
+0000e190: 2020 2020 2020 2064 665b 6e75 6d65 7269         df[numeri
+0000e1a0: 635f 636f 6c75 6d6e 7320 2b20 7363 6f72  c_columns + scor
+0000e1b0: 655f 636f 6c75 6d6e 735d 2e64 726f 706e  e_columns].dropn
+0000e1c0: 6128 6178 6973 3d30 292c 0a20 2020 2020  a(axis=0),.     
+0000e1d0: 2020 2020 2020 2063 6f6c 6f72 3d70 7269         color=pri
+0000e1e0: 6d61 7279 5f73 636f 7265 5f63 6f6c 756d  mary_score_colum
+0000e1f0: 6e2c 0a20 2020 2020 2020 2020 2020 2063  n,.            c
+0000e200: 6f6c 6f72 5f63 6f6e 7469 6e75 6f75 735f  olor_continuous_
+0000e210: 7363 616c 653d 636f 6c6f 725f 636f 6e74  scale=color_cont
+0000e220: 696e 756f 7573 5f73 6361 6c65 2c0a 2020  inuous_scale,.  
+0000e230: 2020 2020 2020 2020 2020 6865 6967 6874            height
+0000e240: 3d68 6569 6768 742c 0a20 2020 2020 2020  =height,.       
+0000e250: 2020 2020 2077 6964 7468 3d77 6964 7468       width=width
+0000e260: 2c0a 2020 2020 2020 2020 2020 2020 7469  ,.            ti
+0000e270: 746c 653d 2250 6172 616c 6c65 6c20 436f  tle="Parallel Co
+0000e280: 6f72 6469 6e61 7465 7320 6f66 2048 7970  ordinates of Hyp
+0000e290: 6572 2d50 6172 616d 6574 6572 7320 616e  er-Parameters an
+0000e2a0: 6420 5363 6f72 6520 4176 6572 6167 6573  d Score Averages
+0000e2b0: 3c62 723e 220a 2020 2020 2020 2020 290a  <br>".        ).
+0000e2c0: 2020 2020 2020 2020 2320 706c 6f74 6c79          # plotly
+0000e2d0: 2e6f 6666 6c69 6e65 2e70 6c6f 7428 6669  .offline.plot(fi
+0000e2e0: 672c 2066 696c 656e 616d 653d 2774 656d  g, filename='tem
+0000e2f0: 702e 6874 6d6c 272c 2061 7574 6f5f 6f70  p.html', auto_op
+0000e300: 656e 3d54 7275 6529 0a20 2020 2020 2020  en=True).       
+0000e310: 2072 6574 7572 6e20 6669 670a 0a20 2020   return fig..   
+0000e320: 2064 6566 2070 6c6f 745f 7363 6174 7465   def plot_scatte
+0000e330: 725f 6d61 7472 6978 2873 656c 662c 0a20  r_matrix(self,. 
+0000e340: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000e350: 2020 2020 2020 2020 2020 2069 6e63 6c75             inclu
+0000e360: 6465 5f61 6c6c 5f73 636f 7265 733a 2062  de_all_scores: b
+0000e370: 6f6f 6c20 3d20 5472 7565 2c0a 2020 2020  ool = True,.    
+0000e380: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000e390: 2020 2020 2020 2020 7175 6572 793a 2073          query: s
+0000e3a0: 7472 203d 204e 6f6e 652c 0a20 2020 2020  tr = None,.     
+0000e3b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000e3c0: 2020 2020 2020 2068 6569 6768 743a 2066         height: f
+0000e3d0: 6c6f 6174 203d 2036 3030 2c0a 2020 2020  loat = 600,.    
+0000e3e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000e3f0: 2020 2020 2020 2020 7769 6474 683a 2066          width: f
+0000e400: 6c6f 6174 203d 2036 3030 202a 2047 4f4c  loat = 600 * GOL
+0000e410: 4445 4e5f 5241 5449 4f29 202d 3e20 706c  DEN_RATIO) -> pl
+0000e420: 6f74 6c79 2e67 7261 7068 5f6f 626a 6563  otly.graph_objec
+0000e430: 7473 2e46 6967 7572 653a 0a20 2020 2020  ts.Figure:.     
+0000e440: 2020 2022 2222 0a20 2020 2020 2020 2052     """.        R
+0000e450: 6574 7572 6e73 2061 2050 6c6f 746c 7920  eturns a Plotly 
+0000e460: 4669 6775 7265 2028 7363 6174 7465 722d  Figure (scatter-
+0000e470: 6d61 7472 6978 2920 6f66 2074 6865 2061  matrix) of the a
+0000e480: 6c6c 2070 6172 616d 6574 6572 7320 616e  ll parameters an
+0000e490: 6420 7363 6f72 6573 2e0a 0a20 2020 2020  d scores...     
+0000e4a0: 2020 2041 7267 733a 0a20 2020 2020 2020     Args:.       
+0000e4b0: 2020 2020 2069 6e63 6c75 6465 5f61 6c6c       include_all
+0000e4c0: 5f73 636f 7265 733a 0a20 2020 2020 2020  _scores:.       
+0000e4d0: 2020 2020 2020 2020 204f 6e6c 7920 6170           Only ap
+0000e4e0: 706c 6963 6162 6c65 2069 6620 7468 6520  plicable if the 
+0000e4f0: 7265 7375 6c74 7320 6861 7665 206d 756c  results have mul
+0000e500: 7469 706c 6520 7363 6f72 6573 2e0a 2020  tiple scores..  
+0000e510: 2020 2020 2020 2020 2020 2020 2020 4966                If
+0000e520: 2054 7275 652c 2069 6e63 6c75 6465 7320   True, includes 
+0000e530: 616c 6c20 6f66 2074 6865 2073 636f 7265  all of the score
+0000e540: 732e 2049 6620 4661 6c73 652c 2069 6e63  s. If False, inc
+0000e550: 6c75 6465 7320 6f6e 6c79 2074 6865 2070  ludes only the p
+0000e560: 7269 6d61 7279 2073 636f 7265 2e0a 2020  rimary score..  
+0000e570: 2020 2020 2020 2020 2020 7175 6572 793a            query:
+0000e580: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0000e590: 2073 7472 696e 6720 746f 2062 6520 7061   string to be pa
+0000e5a0: 7373 6564 2074 6f20 6074 6f5f 6461 7461  ssed to `to_data
+0000e5b0: 6672 616d 6528 2960 3b20 7365 6520 646f  frame()`; see do
+0000e5c0: 6375 6d65 6e74 6174 696f 6e20 666f 7220  cumentation for 
+0000e5d0: 7468 6174 206d 6574 686f 642e 0a20 2020  that method..   
+0000e5e0: 2020 2020 2020 2020 2068 6569 6768 743a           height:
+0000e5f0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0000e600: 2054 6865 2068 6569 6768 7420 6f66 2074   The height of t
+0000e610: 6865 2070 6c6f 742e 2054 6869 7320 7661  he plot. This va
+0000e620: 6c75 6520 6973 2070 6173 7365 6420 746f  lue is passed to
+0000e630: 2070 6c6f 746c 792e 0a20 2020 2020 2020   plotly..       
+0000e640: 2020 2020 2077 6964 7468 3a0a 2020 2020       width:.    
+0000e650: 2020 2020 2020 2020 2020 2020 5468 6520              The 
+0000e660: 7769 6474 6820 6f66 2074 6865 2070 6c6f  width of the plo
+0000e670: 742e 2054 6869 7320 7661 6c75 6520 6973  t. This value is
+0000e680: 2070 6173 7365 6420 746f 2070 6c6f 746c   passed to plotl
+0000e690: 792e 0a20 2020 2020 2020 2022 2222 0a20  y..        """. 
+0000e6a0: 2020 2020 2020 2063 6f6c 6f72 5f63 6f6e         color_con
+0000e6b0: 7469 6e75 6f75 735f 7363 616c 6520 3d20  tinuous_scale = 
+0000e6c0: 7078 2e63 6f6c 6f72 732e 6469 7665 7267  px.colors.diverg
+0000e6d0: 696e 672e 5264 596c 476e 0a20 2020 2020  ing.RdYlGn.     
+0000e6e0: 2020 2069 6620 6e6f 7420 7365 6c66 2e68     if not self.h
+0000e6f0: 6967 6865 725f 7363 6f72 655f 6973 5f62  igher_score_is_b
+0000e700: 6574 7465 723a 0a20 2020 2020 2020 2020  etter:.         
+0000e710: 2020 2063 6f6c 6f72 5f63 6f6e 7469 6e75     color_continu
+0000e720: 6f75 735f 7363 616c 6520 3d20 636f 6c6f  ous_scale = colo
+0000e730: 725f 636f 6e74 696e 756f 7573 5f73 6361  r_continuous_sca
+0000e740: 6c65 2e72 6576 6572 7365 2829 0a0a 2020  le.reverse()..  
+0000e750: 2020 2020 2020 7072 696d 6172 795f 7363        primary_sc
+0000e760: 6f72 655f 636f 6c75 6d6e 203d 2073 656c  ore_column = sel
+0000e770: 662e 7072 696d 6172 795f 7363 6f72 655f  f.primary_score_
+0000e780: 6e61 6d65 202b 2022 204d 6561 6e22 0a0a  name + " Mean"..
+0000e790: 2020 2020 2020 2020 6966 2069 6e63 6c75          if inclu
+0000e7a0: 6465 5f61 6c6c 5f73 636f 7265 733a 0a20  de_all_scores:. 
+0000e7b0: 2020 2020 2020 2020 2020 2073 636f 7265             score
+0000e7c0: 5f63 6f6c 756d 6e73 203d 205b 7363 6f72  _columns = [scor
+0000e7d0: 6520 2b20 2220 4d65 616e 2220 666f 7220  e + " Mean" for 
+0000e7e0: 7363 6f72 6520 696e 2073 656c 662e 7363  score in self.sc
+0000e7f0: 6f72 655f 6e61 6d65 735d 0a20 2020 2020  ore_names].     
+0000e800: 2020 2065 6c73 653a 0a20 2020 2020 2020     else:.       
+0000e810: 2020 2020 2073 636f 7265 5f63 6f6c 756d       score_colum
+0000e820: 6e73 203d 205b 7072 696d 6172 795f 7363  ns = [primary_sc
+0000e830: 6f72 655f 636f 6c75 6d6e 5d0a 0a20 2020  ore_column]..   
+0000e840: 2020 2020 2023 204e 4f54 453a 2073 6f72       # NOTE: sor
+0000e850: 745f 6279 5f73 636f 7265 3d46 616c 7365  t_by_score=False
+0000e860: 2062 6563 6175 7365 2074 6865 7265 2069   because there i
+0000e870: 7320 6120 7765 6972 6420 6275 6720 696e  s a weird bug in
+0000e880: 2070 6c6f 746c 7920 7375 6368 2074 6861   plotly such tha
+0000e890: 7420 6966 2074 6865 2069 6e64 6578 2069  t if the index i
+0000e8a0: 730a 2020 2020 2020 2020 2320 6e6f 7420  s.        # not 
+0000e8b0: 302d 7820 7468 616e 2074 6865 206f 7264  0-x than the ord
+0000e8c0: 6572 2073 6565 6d73 2074 6f20 6765 7420  er seems to get 
+0000e8d0: 6d65 7373 6564 2075 700a 2020 2020 2020  messed up.      
+0000e8e0: 2020 2320 6874 7470 733a 2f2f 6769 7468    # https://gith
+0000e8f0: 7562 2e63 6f6d 2f70 6c6f 746c 792f 706c  ub.com/plotly/pl
+0000e900: 6f74 6c79 2e70 792f 6973 7375 6573 2f33  otly.py/issues/3
+0000e910: 3537 360a 2020 2020 2020 2020 2320 6874  576.        # ht
+0000e920: 7470 733a 2f2f 6769 7468 7562 2e63 6f6d  tps://github.com
+0000e930: 2f70 6c6f 746c 792f 706c 6f74 6c79 2e70  /plotly/plotly.p
+0000e940: 792f 6973 7375 6573 2f33 3537 370a 2020  y/issues/3577.  
+0000e950: 2020 2020 2020 6466 203d 2073 656c 662e        df = self.
+0000e960: 746f 5f64 6174 6166 7261 6d65 2873 6f72  to_dataframe(sor
+0000e970: 745f 6279 5f73 636f 7265 3d46 616c 7365  t_by_score=False
+0000e980: 2c20 7175 6572 793d 7175 6572 7929 0a20  , query=query). 
+0000e990: 2020 2020 2020 2063 6f6c 756d 6e73 203d         columns =
+0000e9a0: 205b 7820 666f 7220 7820 696e 2073 656c   [x for x in sel
+0000e9b0: 662e 7061 7261 6d65 7465 725f 6e61 6d65  f.parameter_name
+0000e9c0: 7320 6966 2078 2069 6e20 6466 2e63 6f6c  s if x in df.col
+0000e9d0: 756d 6e73 5d0a 2020 2020 2020 2020 6669  umns].        fi
+0000e9e0: 6720 3d20 7078 2e73 6361 7474 6572 5f6d  g = px.scatter_m
+0000e9f0: 6174 7269 7828 6466 5b73 636f 7265 5f63  atrix(df[score_c
+0000ea00: 6f6c 756d 6e73 202b 2063 6f6c 756d 6e73  olumns + columns
+0000ea10: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
 0000ea20: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000ea30: 2020 2020 2020 2020 2063 6f6c 6f72 3d70           color=p
-0000ea40: 7269 6d61 7279 5f73 636f 7265 5f63 6f6c  rimary_score_col
-0000ea50: 756d 6e2c 0a20 2020 2020 2020 2020 2020  umn,.           
-0000ea60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000ea70: 2020 2020 2063 6f6c 6f72 5f63 6f6e 7469       color_conti
-0000ea80: 6e75 6f75 735f 7363 616c 653d 636f 6c6f  nuous_scale=colo
-0000ea90: 725f 636f 6e74 696e 756f 7573 5f73 6361  r_continuous_sca
-0000eaa0: 6c65 2c0a 2020 2020 2020 2020 2020 2020  le,.            
-0000eab0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000eac0: 2020 2020 6865 6967 6874 3d68 6569 6768      height=heigh
-0000ead0: 742c 0a20 2020 2020 2020 2020 2020 2020  t,.             
-0000eae0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000eaf0: 2020 2077 6964 7468 3d77 6964 7468 290a     width=width).
-0000eb00: 2020 2020 2020 2020 7265 7475 726e 2066          return f
-0000eb10: 6967 0a0a 2020 2020 6465 6620 706c 6f74  ig..    def plot
-0000eb20: 5f70 6572 666f 726d 616e 6365 5f6e 756d  _performance_num
-0000eb30: 6572 6963 5f70 6172 616d 7328 7365 6c66  eric_params(self
-0000eb40: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+0000ea30: 2020 2063 6f6c 6f72 3d70 7269 6d61 7279     color=primary
+0000ea40: 5f73 636f 7265 5f63 6f6c 756d 6e2c 0a20  _score_column,. 
+0000ea50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000ea60: 2020 2020 2020 2020 2020 2020 2020 2063                 c
+0000ea70: 6f6c 6f72 5f63 6f6e 7469 6e75 6f75 735f  olor_continuous_
+0000ea80: 7363 616c 653d 636f 6c6f 725f 636f 6e74  scale=color_cont
+0000ea90: 696e 756f 7573 5f73 6361 6c65 2c0a 2020  inuous_scale,.  
+0000eaa0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000eab0: 2020 2020 2020 2020 2020 2020 2020 6865                he
+0000eac0: 6967 6874 3d68 6569 6768 742c 0a20 2020  ight=height,.   
+0000ead0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000eae0: 2020 2020 2020 2020 2020 2020 2077 6964               wid
+0000eaf0: 7468 3d77 6964 7468 290a 2020 2020 2020  th=width).      
+0000eb00: 2020 7265 7475 726e 2066 6967 0a0a 2020    return fig..  
+0000eb10: 2020 6465 6620 706c 6f74 5f70 6572 666f    def plot_perfo
+0000eb20: 726d 616e 6365 5f6e 756d 6572 6963 5f70  rmance_numeric_p
+0000eb30: 6172 616d 7328 7365 6c66 2c0a 2020 2020  arams(self,.    
+0000eb40: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000eb50: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000eb60: 2020 2020 2020 2020 2020 7175 6572 793a            query:
-0000eb70: 2073 7472 203d 204e 6f6e 652c 0a20 2020   str = None,.   
+0000eb60: 2020 2020 7175 6572 793a 2073 7472 203d      query: str =
+0000eb70: 204e 6f6e 652c 0a20 2020 2020 2020 2020   None,.         
 0000eb80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000eb90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000eba0: 2020 2020 2068 6569 6768 743a 2066 6c6f       height: flo
-0000ebb0: 6174 203d 2036 3030 2c0a 2020 2020 2020  at = 600,.      
+0000eb90: 2020 2020 2020 2020 2020 2020 2020 2068                 h
+0000eba0: 6569 6768 743a 2066 6c6f 6174 203d 2036  eight: float = 6
+0000ebb0: 3030 2c0a 2020 2020 2020 2020 2020 2020  00,.            
 0000ebc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000ebd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000ebe0: 2020 7769 6474 683a 2066 6c6f 6174 203d    width: float =
-0000ebf0: 2036 3030 202a 2047 4f4c 4445 4e5f 5241   600 * GOLDEN_RA
-0000ec00: 5449 4f29 202d 3e20 706c 6f74 6c79 2e67  TIO) -> plotly.g
-0000ec10: 7261 7068 5f6f 626a 6563 7473 2e46 6967  raph_objects.Fig
-0000ec20: 7572 653a 0a20 2020 2020 2020 2022 2222  ure:.        """
-0000ec30: 0a20 2020 2020 2020 2052 6574 7572 6e73  .        Returns
-0000ec40: 2061 2050 6c6f 746c 7920 4669 6775 7265   a Plotly Figure
-0000ec50: 2028 7363 6174 7465 722d 6d61 7472 6978   (scatter-matrix
-0000ec60: 2920 6f66 2074 6865 2065 6163 6820 6f66  ) of the each of
-0000ec70: 2074 6865 206e 756d 6572 6963 2070 6172   the numeric par
-0000ec80: 616d 6574 6572 7327 2076 616c 7565 7320  ameters' values 
-0000ec90: 2878 2d61 7869 7329 2076 7320 7468 650a  (x-axis) vs the.
-0000eca0: 2020 2020 2020 2020 7072 696d 6172 7920          primary 
-0000ecb0: 7363 6f72 6520 2879 2d61 7869 7329 2e0a  score (y-axis)..
-0000ecc0: 0a20 2020 2020 2020 2041 7267 733a 0a20  .        Args:. 
-0000ecd0: 2020 2020 2020 2020 2020 2071 7565 7279             query
-0000ece0: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
-0000ecf0: 2020 7374 7269 6e67 2074 6f20 6265 2070    string to be p
-0000ed00: 6173 7365 6420 746f 2060 746f 5f64 6174  assed to `to_dat
-0000ed10: 6166 7261 6d65 2829 603b 2073 6565 2064  aframe()`; see d
-0000ed20: 6f63 756d 656e 7461 7469 6f6e 2066 6f72  ocumentation for
-0000ed30: 2074 6861 7420 6d65 7468 6f64 2e0a 2020   that method..  
-0000ed40: 2020 2020 2020 2020 2020 6865 6967 6874            height
-0000ed50: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
-0000ed60: 2020 5468 6520 6865 6967 6874 206f 6620    The height of 
-0000ed70: 7468 6520 706c 6f74 2e20 5468 6973 2076  the plot. This v
-0000ed80: 616c 7565 2069 7320 7061 7373 6564 2074  alue is passed t
-0000ed90: 6f20 706c 6f74 6c79 2e0a 2020 2020 2020  o plotly..      
-0000eda0: 2020 2020 2020 7769 6474 683a 0a20 2020        width:.   
-0000edb0: 2020 2020 2020 2020 2020 2020 2054 6865               The
-0000edc0: 2077 6964 7468 206f 6620 7468 6520 706c   width of the pl
-0000edd0: 6f74 2e20 5468 6973 2076 616c 7565 2069  ot. This value i
-0000ede0: 7320 7061 7373 6564 2074 6f20 706c 6f74  s passed to plot
-0000edf0: 6c79 2e0a 2020 2020 2020 2020 2222 220a  ly..        """.
-0000ee00: 2020 2020 2020 2020 636f 6c6f 725f 636f          color_co
-0000ee10: 6e74 696e 756f 7573 5f73 6361 6c65 203d  ntinuous_scale =
-0000ee20: 2070 782e 636f 6c6f 7273 2e64 6976 6572   px.colors.diver
-0000ee30: 6769 6e67 2e52 6459 6c47 6e0a 2020 2020  ging.RdYlGn.    
-0000ee40: 2020 2020 6966 206e 6f74 2073 656c 662e      if not self.
-0000ee50: 6869 6768 6572 5f73 636f 7265 5f69 735f  higher_score_is_
-0000ee60: 6265 7474 6572 3a0a 2020 2020 2020 2020  better:.        
-0000ee70: 2020 2020 636f 6c6f 725f 636f 6e74 696e      color_contin
-0000ee80: 756f 7573 5f73 6361 6c65 203d 2063 6f6c  uous_scale = col
-0000ee90: 6f72 5f63 6f6e 7469 6e75 6f75 735f 7363  or_continuous_sc
-0000eea0: 616c 652e 7265 7665 7273 6528 290a 0a20  ale.reverse().. 
-0000eeb0: 2020 2020 2020 2070 7269 6d61 7279 5f73         primary_s
-0000eec0: 636f 7265 5f63 6f6c 756d 6e20 3d20 7365  core_column = se
-0000eed0: 6c66 2e70 7269 6d61 7279 5f73 636f 7265  lf.primary_score
-0000eee0: 5f6e 616d 6520 2b20 2220 4d65 616e 220a  _name + " Mean".
-0000eef0: 0a20 2020 2020 2020 2064 6620 3d20 7365  .        df = se
-0000ef00: 6c66 2e74 6f5f 6c61 6265 6c65 645f 6461  lf.to_labeled_da
-0000ef10: 7461 6672 616d 6528 7175 6572 793d 7175  taframe(query=qu
-0000ef20: 6572 7929 0a20 2020 2020 2020 2063 6f6c  ery).        col
-0000ef30: 756d 6e73 203d 205b 7820 666f 7220 7820  umns = [x for x 
-0000ef40: 696e 2073 656c 662e 6e75 6d65 7269 635f  in self.numeric_
-0000ef50: 7061 7261 6d65 7465 7273 2069 6620 7820  parameters if x 
-0000ef60: 696e 2064 662e 636f 6c75 6d6e 735d 0a20  in df.columns]. 
-0000ef70: 2020 2020 2020 206c 6162 656c 6564 5f6c         labeled_l
-0000ef80: 6f6e 6720 3d20 7064 2e6d 656c 7428 6466  ong = pd.melt(df
-0000ef90: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-0000efa0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000efb0: 2069 645f 7661 7273 3d5b 7072 696d 6172   id_vars=[primar
-0000efc0: 795f 7363 6f72 655f 636f 6c75 6d6e 2c20  y_score_column, 
-0000efd0: 276c 6162 656c 275d 2c0a 2020 2020 2020  'label'],.      
+0000ebd0: 2020 2020 2020 2020 2020 2020 7769 6474              widt
+0000ebe0: 683a 2066 6c6f 6174 203d 2036 3030 202a  h: float = 600 *
+0000ebf0: 2047 4f4c 4445 4e5f 5241 5449 4f29 202d   GOLDEN_RATIO) -
+0000ec00: 3e20 706c 6f74 6c79 2e67 7261 7068 5f6f  > plotly.graph_o
+0000ec10: 626a 6563 7473 2e46 6967 7572 653a 0a20  bjects.Figure:. 
+0000ec20: 2020 2020 2020 2022 2222 0a20 2020 2020         """.     
+0000ec30: 2020 2052 6574 7572 6e73 2061 2050 6c6f     Returns a Plo
+0000ec40: 746c 7920 4669 6775 7265 2028 7363 6174  tly Figure (scat
+0000ec50: 7465 722d 6d61 7472 6978 2920 6f66 2074  ter-matrix) of t
+0000ec60: 6865 2065 6163 6820 6f66 2074 6865 206e  he each of the n
+0000ec70: 756d 6572 6963 2070 6172 616d 6574 6572  umeric parameter
+0000ec80: 7327 2076 616c 7565 7320 2878 2d61 7869  s' values (x-axi
+0000ec90: 7329 2076 7320 7468 650a 2020 2020 2020  s) vs the.      
+0000eca0: 2020 7072 696d 6172 7920 7363 6f72 6520    primary score 
+0000ecb0: 2879 2d61 7869 7329 2e0a 0a20 2020 2020  (y-axis)...     
+0000ecc0: 2020 2041 7267 733a 0a20 2020 2020 2020     Args:.       
+0000ecd0: 2020 2020 2071 7565 7279 3a0a 2020 2020       query:.    
+0000ece0: 2020 2020 2020 2020 2020 2020 7374 7269              stri
+0000ecf0: 6e67 2074 6f20 6265 2070 6173 7365 6420  ng to be passed 
+0000ed00: 746f 2060 746f 5f64 6174 6166 7261 6d65  to `to_dataframe
+0000ed10: 2829 603b 2073 6565 2064 6f63 756d 656e  ()`; see documen
+0000ed20: 7461 7469 6f6e 2066 6f72 2074 6861 7420  tation for that 
+0000ed30: 6d65 7468 6f64 2e0a 2020 2020 2020 2020  method..        
+0000ed40: 2020 2020 6865 6967 6874 3a0a 2020 2020      height:.    
+0000ed50: 2020 2020 2020 2020 2020 2020 5468 6520              The 
+0000ed60: 6865 6967 6874 206f 6620 7468 6520 706c  height of the pl
+0000ed70: 6f74 2e20 5468 6973 2076 616c 7565 2069  ot. This value i
+0000ed80: 7320 7061 7373 6564 2074 6f20 706c 6f74  s passed to plot
+0000ed90: 6c79 2e0a 2020 2020 2020 2020 2020 2020  ly..            
+0000eda0: 7769 6474 683a 0a20 2020 2020 2020 2020  width:.         
+0000edb0: 2020 2020 2020 2054 6865 2077 6964 7468         The width
+0000edc0: 206f 6620 7468 6520 706c 6f74 2e20 5468   of the plot. Th
+0000edd0: 6973 2076 616c 7565 2069 7320 7061 7373  is value is pass
+0000ede0: 6564 2074 6f20 706c 6f74 6c79 2e0a 2020  ed to plotly..  
+0000edf0: 2020 2020 2020 2222 220a 2020 2020 2020        """.      
+0000ee00: 2020 636f 6c6f 725f 636f 6e74 696e 756f    color_continuo
+0000ee10: 7573 5f73 6361 6c65 203d 2070 782e 636f  us_scale = px.co
+0000ee20: 6c6f 7273 2e64 6976 6572 6769 6e67 2e52  lors.diverging.R
+0000ee30: 6459 6c47 6e0a 2020 2020 2020 2020 6966  dYlGn.        if
+0000ee40: 206e 6f74 2073 656c 662e 6869 6768 6572   not self.higher
+0000ee50: 5f73 636f 7265 5f69 735f 6265 7474 6572  _score_is_better
+0000ee60: 3a0a 2020 2020 2020 2020 2020 2020 636f  :.            co
+0000ee70: 6c6f 725f 636f 6e74 696e 756f 7573 5f73  lor_continuous_s
+0000ee80: 6361 6c65 203d 2063 6f6c 6f72 5f63 6f6e  cale = color_con
+0000ee90: 7469 6e75 6f75 735f 7363 616c 652e 7265  tinuous_scale.re
+0000eea0: 7665 7273 6528 290a 0a20 2020 2020 2020  verse()..       
+0000eeb0: 2070 7269 6d61 7279 5f73 636f 7265 5f63   primary_score_c
+0000eec0: 6f6c 756d 6e20 3d20 7365 6c66 2e70 7269  olumn = self.pri
+0000eed0: 6d61 7279 5f73 636f 7265 5f6e 616d 6520  mary_score_name 
+0000eee0: 2b20 2220 4d65 616e 220a 0a20 2020 2020  + " Mean"..     
+0000eef0: 2020 2064 6620 3d20 7365 6c66 2e74 6f5f     df = self.to_
+0000ef00: 6c61 6265 6c65 645f 6461 7461 6672 616d  labeled_datafram
+0000ef10: 6528 7175 6572 793d 7175 6572 7929 0a20  e(query=query). 
+0000ef20: 2020 2020 2020 2063 6f6c 756d 6e73 203d         columns =
+0000ef30: 205b 7820 666f 7220 7820 696e 2073 656c   [x for x in sel
+0000ef40: 662e 6e75 6d65 7269 635f 7061 7261 6d65  f.numeric_parame
+0000ef50: 7465 7273 2069 6620 7820 696e 2064 662e  ters if x in df.
+0000ef60: 636f 6c75 6d6e 735d 0a20 2020 2020 2020  columns].       
+0000ef70: 206c 6162 656c 6564 5f6c 6f6e 6720 3d20   labeled_long = 
+0000ef80: 7064 2e6d 656c 7428 6466 2c0a 2020 2020  pd.melt(df,.    
+0000ef90: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000efa0: 2020 2020 2020 2020 2020 2069 645f 7661             id_va
+0000efb0: 7273 3d5b 7072 696d 6172 795f 7363 6f72  rs=[primary_scor
+0000efc0: 655f 636f 6c75 6d6e 2c20 276c 6162 656c  e_column, 'label
+0000efd0: 275d 2c0a 2020 2020 2020 2020 2020 2020  '],.            
 0000efe0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000eff0: 2020 2020 2020 2020 2076 616c 7565 5f76           value_v
-0000f000: 6172 733d 636f 6c75 6d6e 732c 0a20 2020  ars=columns,.   
+0000eff0: 2020 2076 616c 7565 5f76 6172 733d 636f     value_vars=co
+0000f000: 6c75 6d6e 732c 0a20 2020 2020 2020 2020  lumns,.         
 0000f010: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000f020: 2020 2020 2020 2020 2020 2020 7661 725f              var_
-0000f030: 6e61 6d65 3d27 7061 7261 6d65 7465 7227  name='parameter'
-0000f040: 290a 0a20 2020 2020 2020 2066 6967 203d  )..        fig =
-0000f050: 2070 782e 7363 6174 7465 7228 0a20 2020   px.scatter(.   
-0000f060: 2020 2020 2020 2020 2064 6174 615f 6672           data_fr
-0000f070: 616d 653d 6c61 6265 6c65 645f 6c6f 6e67  ame=labeled_long
-0000f080: 2c0a 2020 2020 2020 2020 2020 2020 783d  ,.            x=
-0000f090: 2776 616c 7565 272c 0a20 2020 2020 2020  'value',.       
-0000f0a0: 2020 2020 2079 3d70 7269 6d61 7279 5f73       y=primary_s
-0000f0b0: 636f 7265 5f63 6f6c 756d 6e2c 0a20 2020  core_column,.   
-0000f0c0: 2020 2020 2020 2020 2063 6f6c 6f72 3d70           color=p
-0000f0d0: 7269 6d61 7279 5f73 636f 7265 5f63 6f6c  rimary_score_col
-0000f0e0: 756d 6e2c 0a20 2020 2020 2020 2020 2020  umn,.           
-0000f0f0: 2063 6f6c 6f72 5f63 6f6e 7469 6e75 6f75   color_continuou
-0000f100: 735f 7363 616c 653d 636f 6c6f 725f 636f  s_scale=color_co
-0000f110: 6e74 696e 756f 7573 5f73 6361 6c65 2c0a  ntinuous_scale,.
-0000f120: 2020 2020 2020 2020 2020 2020 6661 6365              face
-0000f130: 745f 636f 6c3d 2770 6172 616d 6574 6572  t_col='parameter
-0000f140: 272c 0a20 2020 2020 2020 2020 2020 2066  ',.            f
-0000f150: 6163 6574 5f63 6f6c 5f77 7261 703d 322c  acet_col_wrap=2,
-0000f160: 0a20 2020 2020 2020 2020 2020 2074 7265  .            tre
-0000f170: 6e64 6c69 6e65 3d27 6c6f 7765 7373 272c  ndline='lowess',
-0000f180: 0a20 2020 2020 2020 2020 2020 206c 6162  .            lab
-0000f190: 656c 733d 7b0a 2020 2020 2020 2020 2020  els={.          
-0000f1a0: 2020 2020 2020 2776 616c 7565 273a 2027        'value': '
-0000f1b0: 5061 7261 6d65 7465 7220 5661 6c75 6527  Parameter Value'
-0000f1c0: 2c0a 2020 2020 2020 2020 2020 2020 7d2c  ,.            },
-0000f1d0: 0a20 2020 2020 2020 2020 2020 2074 6974  .            tit
-0000f1e0: 6c65 3d22 5661 7269 6162 6c65 2050 6572  le="Variable Per
-0000f1f0: 666f 726d 616e 6365 3c62 723e 3c73 7570  formance<br><sup
-0000f200: 3e4e 756d 6572 6963 2050 6172 616d 6574  >Numeric Paramet
-0000f210: 6572 733c 2f73 7570 3e22 2c0a 2020 2020  ers</sup>",.    
-0000f220: 2020 2020 2020 2020 6375 7374 6f6d 5f64          custom_d
-0000f230: 6174 613d 5b27 6c61 6265 6c27 2c20 7072  ata=['label', pr
-0000f240: 696d 6172 795f 7363 6f72 655f 636f 6c75  imary_score_colu
-0000f250: 6d6e 5d2c 0a20 2020 2020 2020 2020 2020  mn],.           
-0000f260: 2068 6569 6768 743d 6865 6967 6874 2c0a   height=height,.
-0000f270: 2020 2020 2020 2020 2020 2020 7769 6474              widt
-0000f280: 683d 7769 6474 680a 2020 2020 2020 2020  h=width.        
-0000f290: 290a 2020 2020 2020 2020 6669 672e 7570  ).        fig.up
-0000f2a0: 6461 7465 5f74 7261 6365 7328 0a20 2020  date_traces(.   
-0000f2b0: 2020 2020 2020 2020 2068 6f76 6572 7465           hoverte
-0000f2c0: 6d70 6c61 7465 3d22 3c62 723e 222e 6a6f  mplate="<br>".jo
-0000f2d0: 696e 285b 0a20 2020 2020 2020 2020 2020  in([.           
-0000f2e0: 2020 2020 2022 5061 7261 6d65 7465 7220       "Parameter 
-0000f2f0: 5661 6c75 653a 2025 7b78 7d22 2c0a 2020  Value: %{x}",.  
-0000f300: 2020 2020 2020 2020 2020 2020 2020 7072                pr
-0000f310: 696d 6172 795f 7363 6f72 655f 636f 6c75  imary_score_colu
-0000f320: 6d6e 202b 2022 3a20 257b 6375 7374 6f6d  mn + ": %{custom
-0000f330: 6461 7461 5b31 5d7d 222c 0a20 2020 2020  data[1]}",.     
-0000f340: 2020 2020 2020 2020 2020 2022 3c62 723e             "<br>
-0000f350: 5061 7261 6d65 7465 7273 3a20 257b 6375  Parameters: %{cu
-0000f360: 7374 6f6d 6461 7461 5b30 5d7d 222c 0a20  stomdata[0]}",. 
-0000f370: 2020 2020 2020 2020 2020 205d 290a 2020             ]).  
-0000f380: 2020 2020 2020 290a 2020 2020 2020 2020        ).        
-0000f390: 6669 672e 7570 6461 7465 5f78 6178 6573  fig.update_xaxes
-0000f3a0: 286d 6174 6368 6573 3d4e 6f6e 652c 2073  (matches=None, s
-0000f3b0: 686f 7774 6963 6b6c 6162 656c 733d 5472  howticklabels=Tr
-0000f3c0: 7565 290a 2020 2020 2020 2020 7265 7475  ue).        retu
-0000f3d0: 726e 2066 6967 0a0a 2020 2020 6465 6620  rn fig..    def 
-0000f3e0: 706c 6f74 5f70 6572 666f 726d 616e 6365  plot_performance
-0000f3f0: 5f6e 6f6e 5f6e 756d 6572 6963 5f70 6172  _non_numeric_par
-0000f400: 616d 7328 7365 6c66 2c0a 2020 2020 2020  ams(self,.      
+0000f020: 2020 2020 2020 7661 725f 6e61 6d65 3d27        var_name='
+0000f030: 7061 7261 6d65 7465 7227 290a 0a20 2020  parameter')..   
+0000f040: 2020 2020 2066 6967 203d 2070 782e 7363       fig = px.sc
+0000f050: 6174 7465 7228 0a20 2020 2020 2020 2020  atter(.         
+0000f060: 2020 2064 6174 615f 6672 616d 653d 6c61     data_frame=la
+0000f070: 6265 6c65 645f 6c6f 6e67 2c0a 2020 2020  beled_long,.    
+0000f080: 2020 2020 2020 2020 783d 2776 616c 7565          x='value
+0000f090: 272c 0a20 2020 2020 2020 2020 2020 2079  ',.            y
+0000f0a0: 3d70 7269 6d61 7279 5f73 636f 7265 5f63  =primary_score_c
+0000f0b0: 6f6c 756d 6e2c 0a20 2020 2020 2020 2020  olumn,.         
+0000f0c0: 2020 2063 6f6c 6f72 3d70 7269 6d61 7279     color=primary
+0000f0d0: 5f73 636f 7265 5f63 6f6c 756d 6e2c 0a20  _score_column,. 
+0000f0e0: 2020 2020 2020 2020 2020 2063 6f6c 6f72             color
+0000f0f0: 5f63 6f6e 7469 6e75 6f75 735f 7363 616c  _continuous_scal
+0000f100: 653d 636f 6c6f 725f 636f 6e74 696e 756f  e=color_continuo
+0000f110: 7573 5f73 6361 6c65 2c0a 2020 2020 2020  us_scale,.      
+0000f120: 2020 2020 2020 6661 6365 745f 636f 6c3d        facet_col=
+0000f130: 2770 6172 616d 6574 6572 272c 0a20 2020  'parameter',.   
+0000f140: 2020 2020 2020 2020 2066 6163 6574 5f63           facet_c
+0000f150: 6f6c 5f77 7261 703d 322c 0a20 2020 2020  ol_wrap=2,.     
+0000f160: 2020 2020 2020 2074 7265 6e64 6c69 6e65         trendline
+0000f170: 3d27 6c6f 7765 7373 272c 0a20 2020 2020  ='lowess',.     
+0000f180: 2020 2020 2020 206c 6162 656c 733d 7b0a         labels={.
+0000f190: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000f1a0: 2776 616c 7565 273a 2027 5061 7261 6d65  'value': 'Parame
+0000f1b0: 7465 7220 5661 6c75 6527 2c0a 2020 2020  ter Value',.    
+0000f1c0: 2020 2020 2020 2020 7d2c 0a20 2020 2020          },.     
+0000f1d0: 2020 2020 2020 2074 6974 6c65 3d22 5661         title="Va
+0000f1e0: 7269 6162 6c65 2050 6572 666f 726d 616e  riable Performan
+0000f1f0: 6365 3c62 723e 3c73 7570 3e4e 756d 6572  ce<br><sup>Numer
+0000f200: 6963 2050 6172 616d 6574 6572 733c 2f73  ic Parameters</s
+0000f210: 7570 3e22 2c0a 2020 2020 2020 2020 2020  up>",.          
+0000f220: 2020 6375 7374 6f6d 5f64 6174 613d 5b27    custom_data=['
+0000f230: 6c61 6265 6c27 2c20 7072 696d 6172 795f  label', primary_
+0000f240: 7363 6f72 655f 636f 6c75 6d6e 5d2c 0a20  score_column],. 
+0000f250: 2020 2020 2020 2020 2020 2068 6569 6768             heigh
+0000f260: 743d 6865 6967 6874 2c0a 2020 2020 2020  t=height,.      
+0000f270: 2020 2020 2020 7769 6474 683d 7769 6474        width=widt
+0000f280: 680a 2020 2020 2020 2020 290a 2020 2020  h.        ).    
+0000f290: 2020 2020 6669 672e 7570 6461 7465 5f74      fig.update_t
+0000f2a0: 7261 6365 7328 0a20 2020 2020 2020 2020  races(.         
+0000f2b0: 2020 2068 6f76 6572 7465 6d70 6c61 7465     hovertemplate
+0000f2c0: 3d22 3c62 723e 222e 6a6f 696e 285b 0a20  ="<br>".join([. 
+0000f2d0: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+0000f2e0: 5061 7261 6d65 7465 7220 5661 6c75 653a  Parameter Value:
+0000f2f0: 2025 7b78 7d22 2c0a 2020 2020 2020 2020   %{x}",.        
+0000f300: 2020 2020 2020 2020 7072 696d 6172 795f          primary_
+0000f310: 7363 6f72 655f 636f 6c75 6d6e 202b 2022  score_column + "
+0000f320: 3a20 257b 6375 7374 6f6d 6461 7461 5b31  : %{customdata[1
+0000f330: 5d7d 222c 0a20 2020 2020 2020 2020 2020  ]}",.           
+0000f340: 2020 2020 2022 3c62 723e 5061 7261 6d65       "<br>Parame
+0000f350: 7465 7273 3a20 257b 6375 7374 6f6d 6461  ters: %{customda
+0000f360: 7461 5b30 5d7d 222c 0a20 2020 2020 2020  ta[0]}",.       
+0000f370: 2020 2020 205d 290a 2020 2020 2020 2020       ]).        
+0000f380: 290a 2020 2020 2020 2020 6669 672e 7570  ).        fig.up
+0000f390: 6461 7465 5f78 6178 6573 286d 6174 6368  date_xaxes(match
+0000f3a0: 6573 3d4e 6f6e 652c 2073 686f 7774 6963  es=None, showtic
+0000f3b0: 6b6c 6162 656c 733d 5472 7565 290a 2020  klabels=True).  
+0000f3c0: 2020 2020 2020 7265 7475 726e 2066 6967        return fig
+0000f3d0: 0a0a 2020 2020 6465 6620 706c 6f74 5f70  ..    def plot_p
+0000f3e0: 6572 666f 726d 616e 6365 5f6e 6f6e 5f6e  erformance_non_n
+0000f3f0: 756d 6572 6963 5f70 6172 616d 7328 7365  umeric_params(se
+0000f400: 6c66 2c0a 2020 2020 2020 2020 2020 2020  lf,.            
 0000f410: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000f420: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000f430: 2020 2020 2020 7175 6572 793a 2073 7472        query: str
-0000f440: 203d 204e 6f6e 652c 0a20 2020 2020 2020   = None,.       
+0000f430: 7175 6572 793a 2073 7472 203d 204e 6f6e  query: str = Non
+0000f440: 652c 0a20 2020 2020 2020 2020 2020 2020  e,.             
 0000f450: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000f460: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000f470: 2020 2020 2068 6569 6768 743a 2066 6c6f       height: flo
-0000f480: 6174 203d 2036 3030 2c0a 2020 2020 2020  at = 600,.      
+0000f460: 2020 2020 2020 2020 2020 2020 2020 2068                 h
+0000f470: 6569 6768 743a 2066 6c6f 6174 203d 2036  eight: float = 6
+0000f480: 3030 2c0a 2020 2020 2020 2020 2020 2020  00,.            
 0000f490: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0000f4a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000f4b0: 2020 2020 2020 7769 6474 683a 2066 6c6f        width: flo
-0000f4c0: 6174 203d 2036 3030 202a 2047 4f4c 4445  at = 600 * GOLDE
-0000f4d0: 4e5f 5241 5449 4f29 202d 3e20 706c 6f74  N_RATIO) -> plot
-0000f4e0: 6c79 2e67 7261 7068 5f6f 626a 6563 7473  ly.graph_objects
-0000f4f0: 2e46 6967 7572 653a 0a20 2020 2020 2020  .Figure:.       
-0000f500: 2022 2222 0a20 2020 2020 2020 2052 6574   """.        Ret
-0000f510: 7572 6e73 2061 2050 6c6f 746c 7920 4669  urns a Plotly Fi
-0000f520: 6775 7265 2028 626f 782d 706c 6f74 2920  gure (box-plot) 
-0000f530: 6f66 2074 6865 2065 6163 6820 6f66 2074  of the each of t
-0000f540: 6865 206e 6f6e 2d6e 756d 6572 6963 2070  he non-numeric p
-0000f550: 6172 616d 6574 6572 7327 2076 616c 7565  arameters' value
-0000f560: 7320 2878 2d61 7869 7329 2076 730a 2020  s (x-axis) vs.  
-0000f570: 2020 2020 2020 7468 6520 7072 696d 6172        the primar
-0000f580: 7920 7363 6f72 6520 2879 2d61 7869 7329  y score (y-axis)
-0000f590: 2e0a 0a20 2020 2020 2020 2041 7267 733a  ...        Args:
-0000f5a0: 0a20 2020 2020 2020 2020 2020 2071 7565  .            que
-0000f5b0: 7279 3a0a 2020 2020 2020 2020 2020 2020  ry:.            
-0000f5c0: 2020 2020 7374 7269 6e67 2074 6f20 6265      string to be
-0000f5d0: 2070 6173 7365 6420 746f 2060 746f 5f64   passed to `to_d
-0000f5e0: 6174 6166 7261 6d65 2829 603b 2073 6565  ataframe()`; see
-0000f5f0: 2064 6f63 756d 656e 7461 7469 6f6e 2066   documentation f
-0000f600: 6f72 2074 6861 7420 6d65 7468 6f64 2e0a  or that method..
-0000f610: 2020 2020 2020 2020 2020 2020 6865 6967              heig
-0000f620: 6874 3a0a 2020 2020 2020 2020 2020 2020  ht:.            
-0000f630: 2020 2020 5468 6520 6865 6967 6874 206f      The height o
-0000f640: 6620 7468 6520 706c 6f74 2e20 5468 6973  f the plot. This
-0000f650: 2076 616c 7565 2069 7320 7061 7373 6564   value is passed
-0000f660: 2074 6f20 706c 6f74 6c79 2e0a 2020 2020   to plotly..    
-0000f670: 2020 2020 2020 2020 7769 6474 683a 0a20          width:. 
-0000f680: 2020 2020 2020 2020 2020 2020 2020 2054                 T
-0000f690: 6865 2077 6964 7468 206f 6620 7468 6520  he width of the 
-0000f6a0: 706c 6f74 2e20 5468 6973 2076 616c 7565  plot. This value
-0000f6b0: 2069 7320 7061 7373 6564 2074 6f20 706c   is passed to pl
-0000f6c0: 6f74 6c79 2e0a 2020 2020 2020 2020 2222  otly..        ""
-0000f6d0: 220a 2020 2020 2020 2020 2320 636f 6c6f  ".        # colo
-0000f6e0: 725f 636f 6e74 696e 756f 7573 5f73 6361  r_continuous_sca
-0000f6f0: 6c65 203d 2070 782e 636f 6c6f 7273 2e64  le = px.colors.d
-0000f700: 6976 6572 6769 6e67 2e52 6459 6c47 6e0a  iverging.RdYlGn.
-0000f710: 2020 2020 2020 2020 2320 6966 206e 6f74          # if not
-0000f720: 2073 656c 662e 6869 6768 6572 5f73 636f   self.higher_sco
-0000f730: 7265 5f69 735f 6265 7474 6572 3a0a 2020  re_is_better:.  
-0000f740: 2020 2020 2020 2320 2020 2020 636f 6c6f        #     colo
-0000f750: 725f 636f 6e74 696e 756f 7573 5f73 6361  r_continuous_sca
-0000f760: 6c65 203d 2063 6f6c 6f72 5f63 6f6e 7469  le = color_conti
-0000f770: 6e75 6f75 735f 7363 616c 652e 7265 7665  nuous_scale.reve
-0000f780: 7273 6528 290a 0a20 2020 2020 2020 2070  rse()..        p
-0000f790: 7269 6d61 7279 5f73 636f 7265 5f63 6f6c  rimary_score_col
-0000f7a0: 756d 6e20 3d20 7365 6c66 2e70 7269 6d61  umn = self.prima
-0000f7b0: 7279 5f73 636f 7265 5f6e 616d 6520 2b20  ry_score_name + 
-0000f7c0: 2220 4d65 616e 220a 0a20 2020 2020 2020  " Mean"..       
-0000f7d0: 2064 6620 3d20 7365 6c66 2e74 6f5f 6c61   df = self.to_la
-0000f7e0: 6265 6c65 645f 6461 7461 6672 616d 6528  beled_dataframe(
-0000f7f0: 7175 6572 793d 7175 6572 7929 0a20 2020  query=query).   
-0000f800: 2020 2020 2063 6f6c 756d 6e73 203d 205b       columns = [
-0000f810: 7820 666f 7220 7820 696e 2073 656c 662e  x for x in self.
-0000f820: 6e6f 6e5f 6e75 6d65 7269 635f 7061 7261  non_numeric_para
-0000f830: 6d65 7465 7273 2069 6620 7820 696e 2064  meters if x in d
-0000f840: 662e 636f 6c75 6d6e 735d 0a20 2020 2020  f.columns].     
-0000f850: 2020 206c 6162 656c 6564 5f6c 6f6e 6720     labeled_long 
-0000f860: 3d20 7064 2e6d 656c 7428 6466 2c0a 2020  = pd.melt(df,.  
+0000f4b0: 7769 6474 683a 2066 6c6f 6174 203d 2036  width: float = 6
+0000f4c0: 3030 202a 2047 4f4c 4445 4e5f 5241 5449  00 * GOLDEN_RATI
+0000f4d0: 4f29 202d 3e20 706c 6f74 6c79 2e67 7261  O) -> plotly.gra
+0000f4e0: 7068 5f6f 626a 6563 7473 2e46 6967 7572  ph_objects.Figur
+0000f4f0: 653a 0a20 2020 2020 2020 2022 2222 0a20  e:.        """. 
+0000f500: 2020 2020 2020 2052 6574 7572 6e73 2061         Returns a
+0000f510: 2050 6c6f 746c 7920 4669 6775 7265 2028   Plotly Figure (
+0000f520: 626f 782d 706c 6f74 2920 6f66 2074 6865  box-plot) of the
+0000f530: 2065 6163 6820 6f66 2074 6865 206e 6f6e   each of the non
+0000f540: 2d6e 756d 6572 6963 2070 6172 616d 6574  -numeric paramet
+0000f550: 6572 7327 2076 616c 7565 7320 2878 2d61  ers' values (x-a
+0000f560: 7869 7329 2076 730a 2020 2020 2020 2020  xis) vs.        
+0000f570: 7468 6520 7072 696d 6172 7920 7363 6f72  the primary scor
+0000f580: 6520 2879 2d61 7869 7329 2e0a 0a20 2020  e (y-axis)...   
+0000f590: 2020 2020 2041 7267 733a 0a20 2020 2020       Args:.     
+0000f5a0: 2020 2020 2020 2071 7565 7279 3a0a 2020         query:.  
+0000f5b0: 2020 2020 2020 2020 2020 2020 2020 7374                st
+0000f5c0: 7269 6e67 2074 6f20 6265 2070 6173 7365  ring to be passe
+0000f5d0: 6420 746f 2060 746f 5f64 6174 6166 7261  d to `to_datafra
+0000f5e0: 6d65 2829 603b 2073 6565 2064 6f63 756d  me()`; see docum
+0000f5f0: 656e 7461 7469 6f6e 2066 6f72 2074 6861  entation for tha
+0000f600: 7420 6d65 7468 6f64 2e0a 2020 2020 2020  t method..      
+0000f610: 2020 2020 2020 6865 6967 6874 3a0a 2020        height:.  
+0000f620: 2020 2020 2020 2020 2020 2020 2020 5468                Th
+0000f630: 6520 6865 6967 6874 206f 6620 7468 6520  e height of the 
+0000f640: 706c 6f74 2e20 5468 6973 2076 616c 7565  plot. This value
+0000f650: 2069 7320 7061 7373 6564 2074 6f20 706c   is passed to pl
+0000f660: 6f74 6c79 2e0a 2020 2020 2020 2020 2020  otly..          
+0000f670: 2020 7769 6474 683a 0a20 2020 2020 2020    width:.       
+0000f680: 2020 2020 2020 2020 2054 6865 2077 6964           The wid
+0000f690: 7468 206f 6620 7468 6520 706c 6f74 2e20  th of the plot. 
+0000f6a0: 5468 6973 2076 616c 7565 2069 7320 7061  This value is pa
+0000f6b0: 7373 6564 2074 6f20 706c 6f74 6c79 2e0a  ssed to plotly..
+0000f6c0: 2020 2020 2020 2020 2222 220a 2020 2020          """.    
+0000f6d0: 2020 2020 2320 636f 6c6f 725f 636f 6e74      # color_cont
+0000f6e0: 696e 756f 7573 5f73 6361 6c65 203d 2070  inuous_scale = p
+0000f6f0: 782e 636f 6c6f 7273 2e64 6976 6572 6769  x.colors.divergi
+0000f700: 6e67 2e52 6459 6c47 6e0a 2020 2020 2020  ng.RdYlGn.      
+0000f710: 2020 2320 6966 206e 6f74 2073 656c 662e    # if not self.
+0000f720: 6869 6768 6572 5f73 636f 7265 5f69 735f  higher_score_is_
+0000f730: 6265 7474 6572 3a0a 2020 2020 2020 2020  better:.        
+0000f740: 2320 2020 2020 636f 6c6f 725f 636f 6e74  #     color_cont
+0000f750: 696e 756f 7573 5f73 6361 6c65 203d 2063  inuous_scale = c
+0000f760: 6f6c 6f72 5f63 6f6e 7469 6e75 6f75 735f  olor_continuous_
+0000f770: 7363 616c 652e 7265 7665 7273 6528 290a  scale.reverse().
+0000f780: 0a20 2020 2020 2020 2070 7269 6d61 7279  .        primary
+0000f790: 5f73 636f 7265 5f63 6f6c 756d 6e20 3d20  _score_column = 
+0000f7a0: 7365 6c66 2e70 7269 6d61 7279 5f73 636f  self.primary_sco
+0000f7b0: 7265 5f6e 616d 6520 2b20 2220 4d65 616e  re_name + " Mean
+0000f7c0: 220a 0a20 2020 2020 2020 2064 6620 3d20  "..        df = 
+0000f7d0: 7365 6c66 2e74 6f5f 6c61 6265 6c65 645f  self.to_labeled_
+0000f7e0: 6461 7461 6672 616d 6528 7175 6572 793d  dataframe(query=
+0000f7f0: 7175 6572 7929 0a20 2020 2020 2020 2063  query).        c
+0000f800: 6f6c 756d 6e73 203d 205b 7820 666f 7220  olumns = [x for 
+0000f810: 7820 696e 2073 656c 662e 6e6f 6e5f 6e75  x in self.non_nu
+0000f820: 6d65 7269 635f 7061 7261 6d65 7465 7273  meric_parameters
+0000f830: 2069 6620 7820 696e 2064 662e 636f 6c75   if x in df.colu
+0000f840: 6d6e 735d 0a20 2020 2020 2020 206c 6162  mns].        lab
+0000f850: 656c 6564 5f6c 6f6e 6720 3d20 7064 2e6d  eled_long = pd.m
+0000f860: 656c 7428 6466 2c0a 2020 2020 2020 2020  elt(df,.        
 0000f870: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000f880: 2020 2020 2020 2020 2020 2020 2069 645f               id_
-0000f890: 7661 7273 3d5b 7072 696d 6172 795f 7363  vars=[primary_sc
-0000f8a0: 6f72 655f 636f 6c75 6d6e 2c20 276c 6162  ore_column, 'lab
-0000f8b0: 656c 275d 2c0a 2020 2020 2020 2020 2020  el'],.          
-0000f8c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000f8d0: 2020 2020 2076 616c 7565 5f76 6172 733d       value_vars=
-0000f8e0: 636f 6c75 6d6e 732c 0a20 2020 2020 2020  columns,.       
+0000f880: 2020 2020 2020 2069 645f 7661 7273 3d5b         id_vars=[
+0000f890: 7072 696d 6172 795f 7363 6f72 655f 636f  primary_score_co
+0000f8a0: 6c75 6d6e 2c20 276c 6162 656c 275d 2c0a  lumn, 'label'],.
+0000f8b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000f8c0: 2020 2020 2020 2020 2020 2020 2020 2076                 v
+0000f8d0: 616c 7565 5f76 6172 733d 636f 6c75 6d6e  alue_vars=column
+0000f8e0: 732c 0a20 2020 2020 2020 2020 2020 2020  s,.             
 0000f8f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000f900: 2020 2020 2020 2020 7661 725f 6e61 6d65          var_name
-0000f910: 3d27 7061 7261 6d65 7465 7227 290a 0a20  ='parameter').. 
-0000f920: 2020 2020 2020 2073 6361 7474 6572 203d         scatter =
-0000f930: 2070 782e 7363 6174 7465 7228 0a20 2020   px.scatter(.   
-0000f940: 2020 2020 2020 2020 2064 6174 615f 6672           data_fr
-0000f950: 616d 653d 6c61 6265 6c65 645f 6c6f 6e67  ame=labeled_long
-0000f960: 2c0a 2020 2020 2020 2020 2020 2020 783d  ,.            x=
-0000f970: 2776 616c 7565 272c 0a20 2020 2020 2020  'value',.       
-0000f980: 2020 2020 2079 3d70 7269 6d61 7279 5f73       y=primary_s
-0000f990: 636f 7265 5f63 6f6c 756d 6e2c 0a20 2020  core_column,.   
-0000f9a0: 2020 2020 2020 2020 2023 2063 6f6c 6f72           # color
-0000f9b0: 3d70 7269 6d61 7279 5f73 636f 7265 5f63  =primary_score_c
-0000f9c0: 6f6c 756d 6e2c 0a20 2020 2020 2020 2020  olumn,.         
-0000f9d0: 2020 2023 2063 6f6c 6f72 5f63 6f6e 7469     # color_conti
-0000f9e0: 6e75 6f75 735f 7363 616c 653d 636f 6c6f  nuous_scale=colo
-0000f9f0: 725f 636f 6e74 696e 756f 7573 5f73 6361  r_continuous_sca
-0000fa00: 6c65 2c0a 2020 2020 2020 2020 2020 2020  le,.            
-0000fa10: 6661 6365 745f 636f 6c3d 2770 6172 616d  facet_col='param
-0000fa20: 6574 6572 272c 0a20 2020 2020 2020 2020  eter',.         
-0000fa30: 2020 2066 6163 6574 5f63 6f6c 5f77 7261     facet_col_wra
-0000fa40: 703d 322c 0a20 2020 2020 2020 2020 2020  p=2,.           
-0000fa50: 206c 6162 656c 733d 7b0a 2020 2020 2020   labels={.      
-0000fa60: 2020 2020 2020 2020 2020 2776 616c 7565            'value
-0000fa70: 273a 2027 5061 7261 6d65 7465 7220 5661  ': 'Parameter Va
-0000fa80: 6c75 6527 2c0a 2020 2020 2020 2020 2020  lue',.          
-0000fa90: 2020 7d2c 0a20 2020 2020 2020 2020 2020    },.           
-0000faa0: 2074 6974 6c65 3d22 5661 7269 6162 6c65   title="Variable
-0000fab0: 2050 6572 666f 726d 616e 6365 3c62 723e   Performance<br>
-0000fac0: 3c73 7570 3e4e 6f6e 2d4e 756d 6572 6963  <sup>Non-Numeric
-0000fad0: 2050 6172 616d 6574 6572 733c 2f73 7570   Parameters</sup
-0000fae0: 3e22 2c0a 2020 2020 2020 2020 2020 2020  >",.            
-0000faf0: 6375 7374 6f6d 5f64 6174 613d 5b27 6c61  custom_data=['la
-0000fb00: 6265 6c27 2c20 7072 696d 6172 795f 7363  bel', primary_sc
-0000fb10: 6f72 655f 636f 6c75 6d6e 5d2c 0a20 2020  ore_column],.   
-0000fb20: 2020 2020 2020 2020 2068 6569 6768 743d           height=
-0000fb30: 6865 6967 6874 2c0a 2020 2020 2020 2020  height,.        
-0000fb40: 2020 2020 7769 6474 683d 7769 6474 682c      width=width,
-0000fb50: 0a20 2020 2020 2020 2029 0a20 2020 2020  .        ).     
-0000fb60: 2020 2073 6361 7474 6572 2e75 7064 6174     scatter.updat
-0000fb70: 655f 7472 6163 6573 280a 2020 2020 2020  e_traces(.      
-0000fb80: 2020 2020 2020 686f 7665 7274 656d 706c        hovertempl
-0000fb90: 6174 653d 223c 6272 3e22 2e6a 6f69 6e28  ate="<br>".join(
-0000fba0: 5b0a 2020 2020 2020 2020 2020 2020 2020  [.              
-0000fbb0: 2020 2250 6172 616d 6574 6572 2056 616c    "Parameter Val
-0000fbc0: 7565 3a20 257b 787d 222c 0a20 2020 2020  ue: %{x}",.     
-0000fbd0: 2020 2020 2020 2020 2020 2070 7269 6d61             prima
-0000fbe0: 7279 5f73 636f 7265 5f63 6f6c 756d 6e20  ry_score_column 
-0000fbf0: 2b20 223a 2025 7b63 7573 746f 6d64 6174  + ": %{customdat
-0000fc00: 615b 315d 7d22 2c0a 2020 2020 2020 2020  a[1]}",.        
-0000fc10: 2020 2020 2020 2020 223c 6272 3e50 6172          "<br>Par
-0000fc20: 616d 6574 6572 733a 2025 7b63 7573 746f  ameters: %{custo
-0000fc30: 6d64 6174 615b 305d 7d22 2c0a 2020 2020  mdata[0]}",.    
-0000fc40: 2020 2020 2020 2020 5d29 0a20 2020 2020          ]).     
-0000fc50: 2020 2029 0a20 2020 2020 2020 2073 6361     ).        sca
-0000fc60: 7474 6572 2e75 7064 6174 655f 7861 7865  tter.update_xaxe
-0000fc70: 7328 6d61 7463 6865 733d 4e6f 6e65 2c20  s(matches=None, 
-0000fc80: 7368 6f77 7469 636b 6c61 6265 6c73 3d54  showticklabels=T
-0000fc90: 7275 6529 0a20 2020 2020 2020 2066 6967  rue).        fig
-0000fca0: 203d 2070 782e 626f 7828 0a20 2020 2020   = px.box(.     
-0000fcb0: 2020 2020 2020 2064 6174 615f 6672 616d         data_fram
-0000fcc0: 653d 6c61 6265 6c65 645f 6c6f 6e67 2c0a  e=labeled_long,.
-0000fcd0: 2020 2020 2020 2020 2020 2020 783d 2776              x='v
-0000fce0: 616c 7565 272c 0a20 2020 2020 2020 2020  alue',.         
-0000fcf0: 2020 2079 3d70 7269 6d61 7279 5f73 636f     y=primary_sco
-0000fd00: 7265 5f63 6f6c 756d 6e2c 0a20 2020 2020  re_column,.     
-0000fd10: 2020 2020 2020 2066 6163 6574 5f63 6f6c         facet_col
-0000fd20: 3d27 7061 7261 6d65 7465 7227 2c0a 2020  ='parameter',.  
-0000fd30: 2020 2020 2020 2020 2020 6661 6365 745f            facet_
-0000fd40: 636f 6c5f 7772 6170 3d32 2c0a 2020 2020  col_wrap=2,.    
-0000fd50: 2020 2020 2020 2020 6c61 6265 6c73 3d7b          labels={
-0000fd60: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0000fd70: 2027 7661 6c75 6527 3a20 2750 6172 616d   'value': 'Param
-0000fd80: 6574 6572 2056 616c 7565 272c 0a20 2020  eter Value',.   
-0000fd90: 2020 2020 2020 2020 207d 2c0a 2020 2020           },.    
-0000fda0: 2020 2020 2020 2020 7469 746c 653d 2256          title="V
-0000fdb0: 6172 6961 626c 6520 5065 7266 6f72 6d61  ariable Performa
-0000fdc0: 6e63 653c 6272 3e3c 7375 703e 4e6f 6e2d  nce<br><sup>Non-
-0000fdd0: 4e75 6d65 7269 6320 5061 7261 6d65 7465  Numeric Paramete
-0000fde0: 7273 3c2f 7375 703e 222c 0a20 2020 2020  rs</sup>",.     
-0000fdf0: 2020 2020 2020 2063 7573 746f 6d5f 6461         custom_da
-0000fe00: 7461 3d5b 276c 6162 656c 272c 2070 7269  ta=['label', pri
-0000fe10: 6d61 7279 5f73 636f 7265 5f63 6f6c 756d  mary_score_colum
-0000fe20: 6e5d 2c0a 2020 2020 2020 2020 2020 2020  n],.            
-0000fe30: 6865 6967 6874 3d68 6569 6768 742c 0a20  height=height,. 
-0000fe40: 2020 2020 2020 2020 2020 2077 6964 7468             width
-0000fe50: 3d77 6964 7468 0a20 2020 2020 2020 2029  =width.        )
-0000fe60: 0a20 2020 2020 2020 2066 6f72 2078 2069  .        for x i
-0000fe70: 6e20 7261 6e67 6528 6c65 6e28 7363 6174  n range(len(scat
-0000fe80: 7465 722e 6461 7461 2929 3a0a 2020 2020  ter.data)):.    
-0000fe90: 2020 2020 2020 2020 6669 672e 6164 645f          fig.add_
-0000fea0: 7472 6163 6528 7363 6174 7465 722e 6461  trace(scatter.da
-0000feb0: 7461 5b78 5d29 0a0a 2020 2020 2020 2020  ta[x])..        
-0000fec0: 6669 672e 7570 6461 7465 5f78 6178 6573  fig.update_xaxes
-0000fed0: 286d 6174 6368 6573 3d4e 6f6e 652c 2073  (matches=None, s
-0000fee0: 686f 7774 6963 6b6c 6162 656c 733d 5472  howticklabels=Tr
-0000fef0: 7565 290a 2020 2020 2020 2020 7265 7475  ue).        retu
-0000ff00: 726e 2066 6967 0a0a 2020 2020 6465 6620  rn fig..    def 
-0000ff10: 706c 6f74 5f73 636f 7265 5f76 735f 7061  plot_score_vs_pa
-0000ff20: 7261 6d65 7465 7228 7365 6c66 2c0a 2020  rameter(self,.  
+0000f900: 2020 7661 725f 6e61 6d65 3d27 7061 7261    var_name='para
+0000f910: 6d65 7465 7227 290a 0a20 2020 2020 2020  meter')..       
+0000f920: 2073 6361 7474 6572 203d 2070 782e 7363   scatter = px.sc
+0000f930: 6174 7465 7228 0a20 2020 2020 2020 2020  atter(.         
+0000f940: 2020 2064 6174 615f 6672 616d 653d 6c61     data_frame=la
+0000f950: 6265 6c65 645f 6c6f 6e67 2c0a 2020 2020  beled_long,.    
+0000f960: 2020 2020 2020 2020 783d 2776 616c 7565          x='value
+0000f970: 272c 0a20 2020 2020 2020 2020 2020 2079  ',.            y
+0000f980: 3d70 7269 6d61 7279 5f73 636f 7265 5f63  =primary_score_c
+0000f990: 6f6c 756d 6e2c 0a20 2020 2020 2020 2020  olumn,.         
+0000f9a0: 2020 2023 2063 6f6c 6f72 3d70 7269 6d61     # color=prima
+0000f9b0: 7279 5f73 636f 7265 5f63 6f6c 756d 6e2c  ry_score_column,
+0000f9c0: 0a20 2020 2020 2020 2020 2020 2023 2063  .            # c
+0000f9d0: 6f6c 6f72 5f63 6f6e 7469 6e75 6f75 735f  olor_continuous_
+0000f9e0: 7363 616c 653d 636f 6c6f 725f 636f 6e74  scale=color_cont
+0000f9f0: 696e 756f 7573 5f73 6361 6c65 2c0a 2020  inuous_scale,.  
+0000fa00: 2020 2020 2020 2020 2020 6661 6365 745f            facet_
+0000fa10: 636f 6c3d 2770 6172 616d 6574 6572 272c  col='parameter',
+0000fa20: 0a20 2020 2020 2020 2020 2020 2066 6163  .            fac
+0000fa30: 6574 5f63 6f6c 5f77 7261 703d 322c 0a20  et_col_wrap=2,. 
+0000fa40: 2020 2020 2020 2020 2020 206c 6162 656c             label
+0000fa50: 733d 7b0a 2020 2020 2020 2020 2020 2020  s={.            
+0000fa60: 2020 2020 2776 616c 7565 273a 2027 5061      'value': 'Pa
+0000fa70: 7261 6d65 7465 7220 5661 6c75 6527 2c0a  rameter Value',.
+0000fa80: 2020 2020 2020 2020 2020 2020 7d2c 0a20              },. 
+0000fa90: 2020 2020 2020 2020 2020 2074 6974 6c65             title
+0000faa0: 3d22 5661 7269 6162 6c65 2050 6572 666f  ="Variable Perfo
+0000fab0: 726d 616e 6365 3c62 723e 3c73 7570 3e4e  rmance<br><sup>N
+0000fac0: 6f6e 2d4e 756d 6572 6963 2050 6172 616d  on-Numeric Param
+0000fad0: 6574 6572 733c 2f73 7570 3e22 2c0a 2020  eters</sup>",.  
+0000fae0: 2020 2020 2020 2020 2020 6375 7374 6f6d            custom
+0000faf0: 5f64 6174 613d 5b27 6c61 6265 6c27 2c20  _data=['label', 
+0000fb00: 7072 696d 6172 795f 7363 6f72 655f 636f  primary_score_co
+0000fb10: 6c75 6d6e 5d2c 0a20 2020 2020 2020 2020  lumn],.         
+0000fb20: 2020 2068 6569 6768 743d 6865 6967 6874     height=height
+0000fb30: 2c0a 2020 2020 2020 2020 2020 2020 7769  ,.            wi
+0000fb40: 6474 683d 7769 6474 682c 0a20 2020 2020  dth=width,.     
+0000fb50: 2020 2029 0a20 2020 2020 2020 2073 6361     ).        sca
+0000fb60: 7474 6572 2e75 7064 6174 655f 7472 6163  tter.update_trac
+0000fb70: 6573 280a 2020 2020 2020 2020 2020 2020  es(.            
+0000fb80: 686f 7665 7274 656d 706c 6174 653d 223c  hovertemplate="<
+0000fb90: 6272 3e22 2e6a 6f69 6e28 5b0a 2020 2020  br>".join([.    
+0000fba0: 2020 2020 2020 2020 2020 2020 2250 6172              "Par
+0000fbb0: 616d 6574 6572 2056 616c 7565 3a20 257b  ameter Value: %{
+0000fbc0: 787d 222c 0a20 2020 2020 2020 2020 2020  x}",.           
+0000fbd0: 2020 2020 2070 7269 6d61 7279 5f73 636f       primary_sco
+0000fbe0: 7265 5f63 6f6c 756d 6e20 2b20 223a 2025  re_column + ": %
+0000fbf0: 7b63 7573 746f 6d64 6174 615b 315d 7d22  {customdata[1]}"
+0000fc00: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+0000fc10: 2020 223c 6272 3e50 6172 616d 6574 6572    "<br>Parameter
+0000fc20: 733a 2025 7b63 7573 746f 6d64 6174 615b  s: %{customdata[
+0000fc30: 305d 7d22 2c0a 2020 2020 2020 2020 2020  0]}",.          
+0000fc40: 2020 5d29 0a20 2020 2020 2020 2029 0a20    ]).        ). 
+0000fc50: 2020 2020 2020 2073 6361 7474 6572 2e75         scatter.u
+0000fc60: 7064 6174 655f 7861 7865 7328 6d61 7463  pdate_xaxes(matc
+0000fc70: 6865 733d 4e6f 6e65 2c20 7368 6f77 7469  hes=None, showti
+0000fc80: 636b 6c61 6265 6c73 3d54 7275 6529 0a20  cklabels=True). 
+0000fc90: 2020 2020 2020 2066 6967 203d 2070 782e         fig = px.
+0000fca0: 626f 7828 0a20 2020 2020 2020 2020 2020  box(.           
+0000fcb0: 2064 6174 615f 6672 616d 653d 6c61 6265   data_frame=labe
+0000fcc0: 6c65 645f 6c6f 6e67 2c0a 2020 2020 2020  led_long,.      
+0000fcd0: 2020 2020 2020 783d 2776 616c 7565 272c        x='value',
+0000fce0: 0a20 2020 2020 2020 2020 2020 2079 3d70  .            y=p
+0000fcf0: 7269 6d61 7279 5f73 636f 7265 5f63 6f6c  rimary_score_col
+0000fd00: 756d 6e2c 0a20 2020 2020 2020 2020 2020  umn,.           
+0000fd10: 2066 6163 6574 5f63 6f6c 3d27 7061 7261   facet_col='para
+0000fd20: 6d65 7465 7227 2c0a 2020 2020 2020 2020  meter',.        
+0000fd30: 2020 2020 6661 6365 745f 636f 6c5f 7772      facet_col_wr
+0000fd40: 6170 3d32 2c0a 2020 2020 2020 2020 2020  ap=2,.          
+0000fd50: 2020 6c61 6265 6c73 3d7b 0a20 2020 2020    labels={.     
+0000fd60: 2020 2020 2020 2020 2020 2027 7661 6c75             'valu
+0000fd70: 6527 3a20 2750 6172 616d 6574 6572 2056  e': 'Parameter V
+0000fd80: 616c 7565 272c 0a20 2020 2020 2020 2020  alue',.         
+0000fd90: 2020 207d 2c0a 2020 2020 2020 2020 2020     },.          
+0000fda0: 2020 7469 746c 653d 2256 6172 6961 626c    title="Variabl
+0000fdb0: 6520 5065 7266 6f72 6d61 6e63 653c 6272  e Performance<br
+0000fdc0: 3e3c 7375 703e 4e6f 6e2d 4e75 6d65 7269  ><sup>Non-Numeri
+0000fdd0: 6320 5061 7261 6d65 7465 7273 3c2f 7375  c Parameters</su
+0000fde0: 703e 222c 0a20 2020 2020 2020 2020 2020  p>",.           
+0000fdf0: 2063 7573 746f 6d5f 6461 7461 3d5b 276c   custom_data=['l
+0000fe00: 6162 656c 272c 2070 7269 6d61 7279 5f73  abel', primary_s
+0000fe10: 636f 7265 5f63 6f6c 756d 6e5d 2c0a 2020  core_column],.  
+0000fe20: 2020 2020 2020 2020 2020 6865 6967 6874            height
+0000fe30: 3d68 6569 6768 742c 0a20 2020 2020 2020  =height,.       
+0000fe40: 2020 2020 2077 6964 7468 3d77 6964 7468       width=width
+0000fe50: 0a20 2020 2020 2020 2029 0a20 2020 2020  .        ).     
+0000fe60: 2020 2066 6f72 2078 2069 6e20 7261 6e67     for x in rang
+0000fe70: 6528 6c65 6e28 7363 6174 7465 722e 6461  e(len(scatter.da
+0000fe80: 7461 2929 3a0a 2020 2020 2020 2020 2020  ta)):.          
+0000fe90: 2020 6669 672e 6164 645f 7472 6163 6528    fig.add_trace(
+0000fea0: 7363 6174 7465 722e 6461 7461 5b78 5d29  scatter.data[x])
+0000feb0: 0a0a 2020 2020 2020 2020 6669 672e 7570  ..        fig.up
+0000fec0: 6461 7465 5f78 6178 6573 286d 6174 6368  date_xaxes(match
+0000fed0: 6573 3d4e 6f6e 652c 2073 686f 7774 6963  es=None, showtic
+0000fee0: 6b6c 6162 656c 733d 5472 7565 290a 2020  klabels=True).  
+0000fef0: 2020 2020 2020 7265 7475 726e 2066 6967        return fig
+0000ff00: 0a0a 2020 2020 6465 6620 706c 6f74 5f73  ..    def plot_s
+0000ff10: 636f 7265 5f76 735f 7061 7261 6d65 7465  core_vs_paramete
+0000ff20: 7228 7365 6c66 2c0a 2020 2020 2020 2020  r(self,.        
 0000ff30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000ff40: 2020 2020 2020 2020 2020 2020 2020 7061                pa
-0000ff50: 7261 6d65 7465 722c 0a20 2020 2020 2020  rameter,.       
+0000ff40: 2020 2020 2020 2020 7061 7261 6d65 7465          paramete
+0000ff50: 722c 0a20 2020 2020 2020 2020 2020 2020  r,.             
 0000ff60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000ff70: 2020 2020 2020 2020 2071 7565 7279 3a20           query: 
-0000ff80: 7374 7220 3d20 4e6f 6e65 2c0a 2020 2020  str = None,.    
+0000ff70: 2020 2071 7565 7279 3a20 7374 7220 3d20     query: str = 
+0000ff80: 4e6f 6e65 2c0a 2020 2020 2020 2020 2020  None,.          
 0000ff90: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000ffa0: 2020 2020 2020 2020 2020 2020 7369 7a65              size
-0000ffb0: 3d4e 6f6e 652c 0a20 2020 2020 2020 2020  =None,.         
+0000ffa0: 2020 2020 2020 7369 7a65 3d4e 6f6e 652c        size=None,
+0000ffb0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
 0000ffc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0000ffd0: 2020 2020 2020 2063 6f6c 6f72 3d4e 6f6e         color=Non
-0000ffe0: 652c 0a20 2020 2020 2020 2020 2020 2020  e,.             
-0000fff0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00010000: 2020 2068 6569 6768 743a 2066 6c6f 6174     height: float
-00010010: 203d 2036 3030 2c0a 2020 2020 2020 2020   = 600,.        
+0000ffd0: 2063 6f6c 6f72 3d4e 6f6e 652c 0a20 2020   color=None,.   
+0000ffe0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0000fff0: 2020 2020 2020 2020 2020 2020 2068 6569               hei
+00010000: 6768 743a 2066 6c6f 6174 203d 2036 3030  ght: float = 600
+00010010: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
 00010020: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00010030: 2020 2020 2020 2020 7769 6474 683a 2066          width: f
-00010040: 6c6f 6174 203d 2036 3030 202a 2047 4f4c  loat = 600 * GOL
-00010050: 4445 4e5f 5241 5449 4f29 202d 3e20 706c  DEN_RATIO) -> pl
-00010060: 6f74 6c79 2e67 7261 7068 5f6f 626a 6563  otly.graph_objec
-00010070: 7473 2e46 6967 7572 653a 0a20 2020 2020  ts.Figure:.     
-00010080: 2020 2022 2222 0a20 2020 2020 2020 2052     """.        R
-00010090: 6574 7572 6e73 2061 2050 6c6f 746c 7920  eturns a Plotly 
-000100a0: 4669 6775 7265 2028 7363 6174 7465 722d  Figure (scatter-
-000100b0: 706c 6f74 2920 6f66 2074 6865 2070 7269  plot) of the pri
-000100c0: 6d61 7279 2073 636f 7265 2028 792d 6178  mary score (y-ax
-000100d0: 6973 2920 7673 2061 2067 6976 656e 2070  is) vs a given p
-000100e0: 6172 616d 6574 6572 2028 782d 6178 6973  arameter (x-axis
-000100f0: 292e 0a0a 2020 2020 2020 2020 4172 6773  )...        Args
-00010100: 3a0a 2020 2020 2020 2020 2020 2020 7061  :.            pa
-00010110: 7261 6d65 7465 723a 0a20 2020 2020 2020  rameter:.       
-00010120: 2020 2020 2020 2020 2054 6865 206e 616d           The nam
-00010130: 6520 6f66 2061 2068 7970 6572 2d70 6172  e of a hyper-par
-00010140: 616d 6574 6572 2074 6f20 706c 6f74 2061  ameter to plot a
-00010150: 6761 696e 7374 2074 6865 2073 636f 7265  gainst the score
-00010160: 2c20 6f6e 2074 6865 2078 2d61 7869 732e  , on the x-axis.
-00010170: 0a20 2020 2020 2020 2020 2020 2071 7565  .            que
-00010180: 7279 3a0a 2020 2020 2020 2020 2020 2020  ry:.            
-00010190: 2020 2020 7374 7269 6e67 2074 6f20 6265      string to be
-000101a0: 2070 6173 7365 6420 746f 2060 746f 5f64   passed to `to_d
-000101b0: 6174 6166 7261 6d65 2829 603b 2073 6565  ataframe()`; see
-000101c0: 2064 6f63 756d 656e 7461 7469 6f6e 2066   documentation f
-000101d0: 6f72 2074 6861 7420 6d65 7468 6f64 2e0a  or that method..
-000101e0: 2020 2020 2020 2020 2020 2020 7369 7a65              size
-000101f0: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
-00010200: 2020 5468 6520 6e61 6d65 206f 6620 6120    The name of a 
-00010210: 6879 7065 722d 7061 7261 6d65 7465 722c  hyper-parameter,
-00010220: 2074 6865 2076 616c 7565 7320 6f66 2077   the values of w
-00010230: 6869 6368 2077 696c 6c20 6265 2075 7365  hich will be use
-00010240: 6420 746f 2064 6574 6572 6d69 6e65 2074  d to determine t
-00010250: 6865 2073 697a 6520 6f66 2074 6865 0a20  he size of the. 
-00010260: 2020 2020 2020 2020 2020 2020 2020 2063                 c
-00010270: 6f72 7265 7370 6f6e 6469 6e67 2070 6f69  orresponding poi
-00010280: 6e74 7320 696e 2074 6865 2070 6c6f 742e  nts in the plot.
-00010290: 2054 6869 7320 7661 6c75 6520 6973 2070   This value is p
-000102a0: 6173 7365 6420 746f 2070 6c6f 746c 792e  assed to plotly.
-000102b0: 0a20 2020 2020 2020 2020 2020 2063 6f6c  .            col
-000102c0: 6f72 3a0a 2020 2020 2020 2020 2020 2020  or:.            
-000102d0: 2020 2020 5468 6520 6e61 6d65 206f 6620      The name of 
-000102e0: 6120 6879 7065 722d 7061 7261 6d65 7465  a hyper-paramete
-000102f0: 722c 2074 6865 2076 616c 7565 7320 6f66  r, the values of
-00010300: 2077 6869 6368 2077 696c 6c20 6265 2075   which will be u
-00010310: 7365 6420 746f 2064 6574 6572 6d69 6e65  sed to determine
-00010320: 2074 6865 2063 6f6c 6f72 206f 6620 7468   the color of th
-00010330: 650a 2020 2020 2020 2020 2020 2020 2020  e.              
-00010340: 2020 636f 7272 6573 706f 6e64 696e 6720    corresponding 
-00010350: 706f 696e 7473 2069 6e20 7468 6520 706c  points in the pl
-00010360: 6f74 2e20 5468 6973 2076 616c 7565 2069  ot. This value i
-00010370: 7320 7061 7373 6564 2074 6f20 706c 6f74  s passed to plot
-00010380: 6c79 2e0a 2020 2020 2020 2020 2020 2020  ly..            
-00010390: 6865 6967 6874 3a0a 2020 2020 2020 2020  height:.        
-000103a0: 2020 2020 2020 2020 5468 6520 6865 6967          The heig
-000103b0: 6874 206f 6620 7468 6520 706c 6f74 2e20  ht of the plot. 
-000103c0: 5468 6973 2076 616c 7565 2069 7320 7061  This value is pa
-000103d0: 7373 6564 2074 6f20 706c 6f74 6c79 2e0a  ssed to plotly..
-000103e0: 2020 2020 2020 2020 2020 2020 7769 6474              widt
-000103f0: 683a 0a20 2020 2020 2020 2020 2020 2020  h:.             
-00010400: 2020 2054 6865 2077 6964 7468 206f 6620     The width of 
-00010410: 7468 6520 706c 6f74 2e20 5468 6973 2076  the plot. This v
-00010420: 616c 7565 2069 7320 7061 7373 6564 2074  alue is passed t
-00010430: 6f20 706c 6f74 6c79 2e0a 2020 2020 2020  o plotly..      
-00010440: 2020 2222 220a 2020 2020 2020 2020 636f    """.        co
-00010450: 6c6f 725f 636f 6e74 696e 756f 7573 5f73  lor_continuous_s
-00010460: 6361 6c65 203d 2070 782e 636f 6c6f 7273  cale = px.colors
-00010470: 2e64 6976 6572 6769 6e67 2e62 616c 616e  .diverging.balan
-00010480: 6365 0a20 2020 2020 2020 2069 6620 6e6f  ce.        if no
-00010490: 7420 7365 6c66 2e68 6967 6865 725f 7363  t self.higher_sc
-000104a0: 6f72 655f 6973 5f62 6574 7465 723a 0a20  ore_is_better:. 
-000104b0: 2020 2020 2020 2020 2020 2063 6f6c 6f72             color
-000104c0: 5f63 6f6e 7469 6e75 6f75 735f 7363 616c  _continuous_scal
-000104d0: 6520 3d20 636f 6c6f 725f 636f 6e74 696e  e = color_contin
-000104e0: 756f 7573 5f73 6361 6c65 2e72 6576 6572  uous_scale.rever
-000104f0: 7365 2829 0a0a 2020 2020 2020 2020 7072  se()..        pr
-00010500: 696d 6172 795f 7363 6f72 655f 636f 6c75  imary_score_colu
-00010510: 6d6e 203d 2073 656c 662e 7072 696d 6172  mn = self.primar
-00010520: 795f 7363 6f72 655f 6e61 6d65 202b 2022  y_score_name + "
-00010530: 204d 6561 6e22 0a20 2020 2020 2020 2074   Mean".        t
-00010540: 6974 6c65 203d 2066 2250 7269 6d61 7279  itle = f"Primary
-00010550: 2053 636f 7265 2028 7b73 656c 662e 7072   Score ({self.pr
-00010560: 696d 6172 795f 7363 6f72 655f 6e61 6d65  imary_score_name
-00010570: 7d29 2076 7320 3c62 3e7b 7061 7261 6d65  }) vs <b>{parame
-00010580: 7465 727d 3c2f 623e 220a 2020 2020 2020  ter}</b>".      
-00010590: 2020 6966 2073 697a 653a 0a20 2020 2020    if size:.     
-000105a0: 2020 2020 2020 2074 6974 6c65 203d 2074         title = t
-000105b0: 6974 6c65 202b 2066 223c 6272 3e3c 7375  itle + f"<br><su
-000105c0: 703e 5468 6520 7369 7a65 206f 6620 7468  p>The size of th
-000105d0: 6520 706f 696e 7420 636f 7272 6573 706f  e point correspo
-000105e0: 6e64 7320 746f 2074 6865 2076 616c 7565  nds to the value
-000105f0: 206f 6620 3c62 3e27 7b73 697a 657d 273c   of <b>'{size}'<
-00010600: 2f62 3e2e 3c2f 7375 703e 220a 0a20 2020  /b>.</sup>"..   
-00010610: 2020 2020 2066 6967 203d 2070 782e 7363       fig = px.sc
-00010620: 6174 7465 7228 0a20 2020 2020 2020 2020  atter(.         
-00010630: 2020 2064 6174 615f 6672 616d 653d 7365     data_frame=se
-00010640: 6c66 2e74 6f5f 6c61 6265 6c65 645f 6461  lf.to_labeled_da
-00010650: 7461 6672 616d 6528 7175 6572 793d 7175  taframe(query=qu
-00010660: 6572 7929 2c0a 2020 2020 2020 2020 2020  ery),.          
-00010670: 2020 783d 7061 7261 6d65 7465 722c 0a20    x=parameter,. 
-00010680: 2020 2020 2020 2020 2020 2079 3d70 7269             y=pri
-00010690: 6d61 7279 5f73 636f 7265 5f63 6f6c 756d  mary_score_colum
-000106a0: 6e2c 0a20 2020 2020 2020 2020 2020 2073  n,.            s
-000106b0: 697a 653d 7369 7a65 2c0a 2020 2020 2020  ize=size,.      
-000106c0: 2020 2020 2020 636f 6c6f 723d 636f 6c6f        color=colo
-000106d0: 722c 0a20 2020 2020 2020 2020 2020 2063  r,.            c
-000106e0: 6f6c 6f72 5f63 6f6e 7469 6e75 6f75 735f  olor_continuous_
-000106f0: 7363 616c 653d 636f 6c6f 725f 636f 6e74  scale=color_cont
-00010700: 696e 756f 7573 5f73 6361 6c65 2c0a 2020  inuous_scale,.  
-00010710: 2020 2020 2020 2020 2020 7472 656e 646c            trendl
-00010720: 696e 653d 276c 6f77 6573 7327 2c0a 2020  ine='lowess',.  
-00010730: 2020 2020 2020 2020 2020 6c61 6265 6c73            labels
-00010740: 3d7b 0a20 2020 2020 2020 2020 2020 2020  ={.             
-00010750: 2020 2070 7269 6d61 7279 5f73 636f 7265     primary_score
-00010760: 5f63 6f6c 756d 6e3a 2066 2241 7665 7261  _column: f"Avera
-00010770: 6765 2043 726f 7373 2056 616c 6964 6174  ge Cross Validat
-00010780: 696f 6e20 5363 6f72 6520 287b 7365 6c66  ion Score ({self
-00010790: 2e70 7269 6d61 7279 5f73 636f 7265 5f6e  .primary_score_n
-000107a0: 616d 657d 2922 2c0a 2020 2020 2020 2020  ame})",.        
-000107b0: 2020 2020 7d2c 0a20 2020 2020 2020 2020      },.         
-000107c0: 2020 2074 6974 6c65 3d74 6974 6c65 2c0a     title=title,.
-000107d0: 2020 2020 2020 2020 2020 2020 6375 7374              cust
-000107e0: 6f6d 5f64 6174 613d 5b27 6c61 6265 6c27  om_data=['label'
-000107f0: 5d2c 0a20 2020 2020 2020 2020 2020 2068  ],.            h
-00010800: 6569 6768 743d 6865 6967 6874 2c0a 2020  eight=height,.  
-00010810: 2020 2020 2020 2020 2020 7769 6474 683d            width=
-00010820: 7769 6474 682c 0a20 2020 2020 2020 2029  width,.        )
-00010830: 0a20 2020 2020 2020 2066 6967 2e75 7064  .        fig.upd
-00010840: 6174 655f 7472 6163 6573 280a 2020 2020  ate_traces(.    
-00010850: 2020 2020 2020 2020 686f 7665 7274 656d          hovertem
-00010860: 706c 6174 653d 223c 6272 3e22 2e6a 6f69  plate="<br>".joi
-00010870: 6e28 5b0a 2020 2020 2020 2020 2020 2020  n([.            
-00010880: 2020 2020 2250 6172 616d 6574 6572 2056      "Parameter V
-00010890: 616c 7565 3a20 257b 787d 222c 0a20 2020  alue: %{x}",.   
-000108a0: 2020 2020 2020 2020 2020 2020 2070 7269               pri
-000108b0: 6d61 7279 5f73 636f 7265 5f63 6f6c 756d  mary_score_colum
-000108c0: 6e20 2b20 223a 2022 202b 2022 257b 797d  n + ": " + "%{y}
-000108d0: 222c 0a20 2020 2020 2020 2020 2020 2020  ",.             
-000108e0: 2020 2022 3c62 723e 5061 7261 6d65 7465     "<br>Paramete
-000108f0: 7273 3a20 257b 6375 7374 6f6d 6461 7461  rs: %{customdata
-00010900: 5b30 5d7d 222c 0a20 2020 2020 2020 2020  [0]}",.         
-00010910: 2020 205d 290a 2020 2020 2020 2020 290a     ]).        ).
-00010920: 2020 2020 2020 2020 7265 7475 726e 2066          return f
-00010930: 6967 0a0a 2020 2020 6465 6620 706c 6f74  ig..    def plot
-00010940: 5f70 6172 616d 6574 6572 5f76 735f 7061  _parameter_vs_pa
-00010950: 7261 6d65 7465 7228 7365 6c66 2c0a 2020  rameter(self,.  
+00010030: 2020 7769 6474 683a 2066 6c6f 6174 203d    width: float =
+00010040: 2036 3030 202a 2047 4f4c 4445 4e5f 5241   600 * GOLDEN_RA
+00010050: 5449 4f29 202d 3e20 706c 6f74 6c79 2e67  TIO) -> plotly.g
+00010060: 7261 7068 5f6f 626a 6563 7473 2e46 6967  raph_objects.Fig
+00010070: 7572 653a 0a20 2020 2020 2020 2022 2222  ure:.        """
+00010080: 0a20 2020 2020 2020 2052 6574 7572 6e73  .        Returns
+00010090: 2061 2050 6c6f 746c 7920 4669 6775 7265   a Plotly Figure
+000100a0: 2028 7363 6174 7465 722d 706c 6f74 2920   (scatter-plot) 
+000100b0: 6f66 2074 6865 2070 7269 6d61 7279 2073  of the primary s
+000100c0: 636f 7265 2028 792d 6178 6973 2920 7673  core (y-axis) vs
+000100d0: 2061 2067 6976 656e 2070 6172 616d 6574   a given paramet
+000100e0: 6572 2028 782d 6178 6973 292e 0a0a 2020  er (x-axis)...  
+000100f0: 2020 2020 2020 4172 6773 3a0a 2020 2020        Args:.    
+00010100: 2020 2020 2020 2020 7061 7261 6d65 7465          paramete
+00010110: 723a 0a20 2020 2020 2020 2020 2020 2020  r:.             
+00010120: 2020 2054 6865 206e 616d 6520 6f66 2061     The name of a
+00010130: 2068 7970 6572 2d70 6172 616d 6574 6572   hyper-parameter
+00010140: 2074 6f20 706c 6f74 2061 6761 696e 7374   to plot against
+00010150: 2074 6865 2073 636f 7265 2c20 6f6e 2074   the score, on t
+00010160: 6865 2078 2d61 7869 732e 0a20 2020 2020  he x-axis..     
+00010170: 2020 2020 2020 2071 7565 7279 3a0a 2020         query:.  
+00010180: 2020 2020 2020 2020 2020 2020 2020 7374                st
+00010190: 7269 6e67 2074 6f20 6265 2070 6173 7365  ring to be passe
+000101a0: 6420 746f 2060 746f 5f64 6174 6166 7261  d to `to_datafra
+000101b0: 6d65 2829 603b 2073 6565 2064 6f63 756d  me()`; see docum
+000101c0: 656e 7461 7469 6f6e 2066 6f72 2074 6861  entation for tha
+000101d0: 7420 6d65 7468 6f64 2e0a 2020 2020 2020  t method..      
+000101e0: 2020 2020 2020 7369 7a65 3a0a 2020 2020        size:.    
+000101f0: 2020 2020 2020 2020 2020 2020 5468 6520              The 
+00010200: 6e61 6d65 206f 6620 6120 6879 7065 722d  name of a hyper-
+00010210: 7061 7261 6d65 7465 722c 2074 6865 2076  parameter, the v
+00010220: 616c 7565 7320 6f66 2077 6869 6368 2077  alues of which w
+00010230: 696c 6c20 6265 2075 7365 6420 746f 2064  ill be used to d
+00010240: 6574 6572 6d69 6e65 2074 6865 2073 697a  etermine the siz
+00010250: 6520 6f66 2074 6865 0a20 2020 2020 2020  e of the.       
+00010260: 2020 2020 2020 2020 2063 6f72 7265 7370           corresp
+00010270: 6f6e 6469 6e67 2070 6f69 6e74 7320 696e  onding points in
+00010280: 2074 6865 2070 6c6f 742e 2054 6869 7320   the plot. This 
+00010290: 7661 6c75 6520 6973 2070 6173 7365 6420  value is passed 
+000102a0: 746f 2070 6c6f 746c 792e 0a20 2020 2020  to plotly..     
+000102b0: 2020 2020 2020 2063 6f6c 6f72 3a0a 2020         color:.  
+000102c0: 2020 2020 2020 2020 2020 2020 2020 5468                Th
+000102d0: 6520 6e61 6d65 206f 6620 6120 6879 7065  e name of a hype
+000102e0: 722d 7061 7261 6d65 7465 722c 2074 6865  r-parameter, the
+000102f0: 2076 616c 7565 7320 6f66 2077 6869 6368   values of which
+00010300: 2077 696c 6c20 6265 2075 7365 6420 746f   will be used to
+00010310: 2064 6574 6572 6d69 6e65 2074 6865 2063   determine the c
+00010320: 6f6c 6f72 206f 6620 7468 650a 2020 2020  olor of the.    
+00010330: 2020 2020 2020 2020 2020 2020 636f 7272              corr
+00010340: 6573 706f 6e64 696e 6720 706f 696e 7473  esponding points
+00010350: 2069 6e20 7468 6520 706c 6f74 2e20 5468   in the plot. Th
+00010360: 6973 2076 616c 7565 2069 7320 7061 7373  is value is pass
+00010370: 6564 2074 6f20 706c 6f74 6c79 2e0a 2020  ed to plotly..  
+00010380: 2020 2020 2020 2020 2020 6865 6967 6874            height
+00010390: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
+000103a0: 2020 5468 6520 6865 6967 6874 206f 6620    The height of 
+000103b0: 7468 6520 706c 6f74 2e20 5468 6973 2076  the plot. This v
+000103c0: 616c 7565 2069 7320 7061 7373 6564 2074  alue is passed t
+000103d0: 6f20 706c 6f74 6c79 2e0a 2020 2020 2020  o plotly..      
+000103e0: 2020 2020 2020 7769 6474 683a 0a20 2020        width:.   
+000103f0: 2020 2020 2020 2020 2020 2020 2054 6865               The
+00010400: 2077 6964 7468 206f 6620 7468 6520 706c   width of the pl
+00010410: 6f74 2e20 5468 6973 2076 616c 7565 2069  ot. This value i
+00010420: 7320 7061 7373 6564 2074 6f20 706c 6f74  s passed to plot
+00010430: 6c79 2e0a 2020 2020 2020 2020 2222 220a  ly..        """.
+00010440: 2020 2020 2020 2020 636f 6c6f 725f 636f          color_co
+00010450: 6e74 696e 756f 7573 5f73 6361 6c65 203d  ntinuous_scale =
+00010460: 2070 782e 636f 6c6f 7273 2e64 6976 6572   px.colors.diver
+00010470: 6769 6e67 2e62 616c 616e 6365 0a20 2020  ging.balance.   
+00010480: 2020 2020 2069 6620 6e6f 7420 7365 6c66       if not self
+00010490: 2e68 6967 6865 725f 7363 6f72 655f 6973  .higher_score_is
+000104a0: 5f62 6574 7465 723a 0a20 2020 2020 2020  _better:.       
+000104b0: 2020 2020 2063 6f6c 6f72 5f63 6f6e 7469       color_conti
+000104c0: 6e75 6f75 735f 7363 616c 6520 3d20 636f  nuous_scale = co
+000104d0: 6c6f 725f 636f 6e74 696e 756f 7573 5f73  lor_continuous_s
+000104e0: 6361 6c65 2e72 6576 6572 7365 2829 0a0a  cale.reverse()..
+000104f0: 2020 2020 2020 2020 7072 696d 6172 795f          primary_
+00010500: 7363 6f72 655f 636f 6c75 6d6e 203d 2073  score_column = s
+00010510: 656c 662e 7072 696d 6172 795f 7363 6f72  elf.primary_scor
+00010520: 655f 6e61 6d65 202b 2022 204d 6561 6e22  e_name + " Mean"
+00010530: 0a20 2020 2020 2020 2074 6974 6c65 203d  .        title =
+00010540: 2066 2250 7269 6d61 7279 2053 636f 7265   f"Primary Score
+00010550: 2028 7b73 656c 662e 7072 696d 6172 795f   ({self.primary_
+00010560: 7363 6f72 655f 6e61 6d65 7d29 2076 7320  score_name}) vs 
+00010570: 3c62 3e7b 7061 7261 6d65 7465 727d 3c2f  <b>{parameter}</
+00010580: 623e 220a 2020 2020 2020 2020 6966 2073  b>".        if s
+00010590: 697a 653a 0a20 2020 2020 2020 2020 2020  ize:.           
+000105a0: 2074 6974 6c65 203d 2074 6974 6c65 202b   title = title +
+000105b0: 2066 223c 6272 3e3c 7375 703e 5468 6520   f"<br><sup>The 
+000105c0: 7369 7a65 206f 6620 7468 6520 706f 696e  size of the poin
+000105d0: 7420 636f 7272 6573 706f 6e64 7320 746f  t corresponds to
+000105e0: 2074 6865 2076 616c 7565 206f 6620 3c62   the value of <b
+000105f0: 3e27 7b73 697a 657d 273c 2f62 3e2e 3c2f  >'{size}'</b>.</
+00010600: 7375 703e 220a 0a20 2020 2020 2020 2066  sup>"..        f
+00010610: 6967 203d 2070 782e 7363 6174 7465 7228  ig = px.scatter(
+00010620: 0a20 2020 2020 2020 2020 2020 2064 6174  .            dat
+00010630: 615f 6672 616d 653d 7365 6c66 2e74 6f5f  a_frame=self.to_
+00010640: 6c61 6265 6c65 645f 6461 7461 6672 616d  labeled_datafram
+00010650: 6528 7175 6572 793d 7175 6572 7929 2c0a  e(query=query),.
+00010660: 2020 2020 2020 2020 2020 2020 783d 7061              x=pa
+00010670: 7261 6d65 7465 722c 0a20 2020 2020 2020  rameter,.       
+00010680: 2020 2020 2079 3d70 7269 6d61 7279 5f73       y=primary_s
+00010690: 636f 7265 5f63 6f6c 756d 6e2c 0a20 2020  core_column,.   
+000106a0: 2020 2020 2020 2020 2073 697a 653d 7369           size=si
+000106b0: 7a65 2c0a 2020 2020 2020 2020 2020 2020  ze,.            
+000106c0: 636f 6c6f 723d 636f 6c6f 722c 0a20 2020  color=color,.   
+000106d0: 2020 2020 2020 2020 2063 6f6c 6f72 5f63           color_c
+000106e0: 6f6e 7469 6e75 6f75 735f 7363 616c 653d  ontinuous_scale=
+000106f0: 636f 6c6f 725f 636f 6e74 696e 756f 7573  color_continuous
+00010700: 5f73 6361 6c65 2c0a 2020 2020 2020 2020  _scale,.        
+00010710: 2020 2020 7472 656e 646c 696e 653d 276c      trendline='l
+00010720: 6f77 6573 7327 2c0a 2020 2020 2020 2020  owess',.        
+00010730: 2020 2020 6c61 6265 6c73 3d7b 0a20 2020      labels={.   
+00010740: 2020 2020 2020 2020 2020 2020 2070 7269               pri
+00010750: 6d61 7279 5f73 636f 7265 5f63 6f6c 756d  mary_score_colum
+00010760: 6e3a 2066 2241 7665 7261 6765 2043 726f  n: f"Average Cro
+00010770: 7373 2056 616c 6964 6174 696f 6e20 5363  ss Validation Sc
+00010780: 6f72 6520 287b 7365 6c66 2e70 7269 6d61  ore ({self.prima
+00010790: 7279 5f73 636f 7265 5f6e 616d 657d 2922  ry_score_name})"
+000107a0: 2c0a 2020 2020 2020 2020 2020 2020 7d2c  ,.            },
+000107b0: 0a20 2020 2020 2020 2020 2020 2074 6974  .            tit
+000107c0: 6c65 3d74 6974 6c65 2c0a 2020 2020 2020  le=title,.      
+000107d0: 2020 2020 2020 6375 7374 6f6d 5f64 6174        custom_dat
+000107e0: 613d 5b27 6c61 6265 6c27 5d2c 0a20 2020  a=['label'],.   
+000107f0: 2020 2020 2020 2020 2068 6569 6768 743d           height=
+00010800: 6865 6967 6874 2c0a 2020 2020 2020 2020  height,.        
+00010810: 2020 2020 7769 6474 683d 7769 6474 682c      width=width,
+00010820: 0a20 2020 2020 2020 2029 0a20 2020 2020  .        ).     
+00010830: 2020 2066 6967 2e75 7064 6174 655f 7472     fig.update_tr
+00010840: 6163 6573 280a 2020 2020 2020 2020 2020  aces(.          
+00010850: 2020 686f 7665 7274 656d 706c 6174 653d    hovertemplate=
+00010860: 223c 6272 3e22 2e6a 6f69 6e28 5b0a 2020  "<br>".join([.  
+00010870: 2020 2020 2020 2020 2020 2020 2020 2250                "P
+00010880: 6172 616d 6574 6572 2056 616c 7565 3a20  arameter Value: 
+00010890: 257b 787d 222c 0a20 2020 2020 2020 2020  %{x}",.         
+000108a0: 2020 2020 2020 2070 7269 6d61 7279 5f73         primary_s
+000108b0: 636f 7265 5f63 6f6c 756d 6e20 2b20 223a  core_column + ":
+000108c0: 2022 202b 2022 257b 797d 222c 0a20 2020   " + "%{y}",.   
+000108d0: 2020 2020 2020 2020 2020 2020 2022 3c62               "<b
+000108e0: 723e 5061 7261 6d65 7465 7273 3a20 257b  r>Parameters: %{
+000108f0: 6375 7374 6f6d 6461 7461 5b30 5d7d 222c  customdata[0]}",
+00010900: 0a20 2020 2020 2020 2020 2020 205d 290a  .            ]).
+00010910: 2020 2020 2020 2020 290a 2020 2020 2020          ).      
+00010920: 2020 7265 7475 726e 2066 6967 0a0a 2020    return fig..  
+00010930: 2020 6465 6620 706c 6f74 5f70 6172 616d    def plot_param
+00010940: 6574 6572 5f76 735f 7061 7261 6d65 7465  eter_vs_paramete
+00010950: 7228 7365 6c66 2c0a 2020 2020 2020 2020  r(self,.        
 00010960: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00010970: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00010980: 2020 7061 7261 6d65 7465 725f 782c 0a20    parameter_x,. 
+00010970: 2020 2020 2020 2020 2020 2020 7061 7261              para
+00010980: 6d65 7465 725f 782c 0a20 2020 2020 2020  meter_x,.       
 00010990: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000109a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000109b0: 2020 2070 6172 616d 6574 6572 5f79 2c0a     parameter_y,.
+000109a0: 2020 2020 2020 2020 2020 2020 2070 6172               par
+000109b0: 616d 6574 6572 5f79 2c0a 2020 2020 2020  ameter_y,.      
 000109c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000109d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000109e0: 2020 2020 7175 6572 793a 2073 7472 203d      query: str =
-000109f0: 204e 6f6e 652c 0a20 2020 2020 2020 2020   None,.         
+000109d0: 2020 2020 2020 2020 2020 2020 2020 7175                qu
+000109e0: 6572 793a 2073 7472 203d 204e 6f6e 652c  ery: str = None,
+000109f0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
 00010a00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00010a10: 2020 2020 2020 2020 2020 2073 697a 653d             size=
-00010a20: 4e6f 6e65 2c0a 2020 2020 2020 2020 2020  None,.          
+00010a10: 2020 2020 2073 697a 653d 4e6f 6e65 2c0a       size=None,.
+00010a20: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00010a30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00010a40: 2020 2020 2020 2020 2020 6865 6967 6874            height
-00010a50: 3a20 666c 6f61 7420 3d20 3630 302c 0a20  : float = 600,. 
+00010a40: 2020 2020 6865 6967 6874 3a20 666c 6f61      height: floa
+00010a50: 7420 3d20 3630 302c 0a20 2020 2020 2020  t = 600,.       
 00010a60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00010a70: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00010a80: 2020 2077 6964 7468 3a20 666c 6f61 7420     width: float 
-00010a90: 3d20 3630 3020 2a20 474f 4c44 454e 5f52  = 600 * GOLDEN_R
-00010aa0: 4154 494f 2920 2d3e 2070 6c6f 746c 792e  ATIO) -> plotly.
-00010ab0: 6772 6170 685f 6f62 6a65 6374 732e 4669  graph_objects.Fi
-00010ac0: 6775 7265 3a0a 2020 2020 2020 2020 2222  gure:.        ""
-00010ad0: 220a 2020 2020 2020 2020 5265 7475 726e  ".        Return
-00010ae0: 7320 6120 506c 6f74 6c79 2046 6967 7572  s a Plotly Figur
-00010af0: 6520 2873 6361 7474 6572 2d70 6c6f 7429  e (scatter-plot)
-00010b00: 2062 6574 7765 656e 2074 776f 2068 7970   between two hyp
-00010b10: 6572 2d70 6172 616d 6574 6572 732e 0a0a  er-parameters...
-00010b20: 2020 2020 2020 2020 4172 6773 3a0a 2020          Args:.  
-00010b30: 2020 2020 2020 2020 2020 7061 7261 6d65            parame
-00010b40: 7465 725f 783a 0a20 2020 2020 2020 2020  ter_x:.         
-00010b50: 2020 2020 2020 2054 6865 206e 616d 6520         The name 
-00010b60: 6f66 2061 2068 7970 6572 2d70 6172 616d  of a hyper-param
-00010b70: 6574 6572 2074 6f20 706c 6f74 2061 6761  eter to plot aga
-00010b80: 696e 7374 2061 6e6f 7468 6572 2070 6172  inst another par
-00010b90: 616d 6574 6572 2c20 6f6e 2074 6865 2078  ameter, on the x
-00010ba0: 2d61 7869 732e 0a20 2020 2020 2020 2020  -axis..         
-00010bb0: 2020 2070 6172 616d 6574 6572 5f79 3a0a     parameter_y:.
-00010bc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00010bd0: 5468 6520 6e61 6d65 206f 6620 6120 6879  The name of a hy
-00010be0: 7065 722d 7061 7261 6d65 7465 7220 746f  per-parameter to
-00010bf0: 2070 6c6f 7420 6167 6169 6e73 7420 616e   plot against an
-00010c00: 6f74 6865 7220 7061 7261 6d65 7465 722c  other parameter,
-00010c10: 206f 6e20 7468 6520 792d 6178 6973 2e0a   on the y-axis..
-00010c20: 2020 2020 2020 2020 2020 2020 7175 6572              quer
-00010c30: 793a 0a20 2020 2020 2020 2020 2020 2020  y:.             
-00010c40: 2020 2073 7472 696e 6720 746f 2062 6520     string to be 
-00010c50: 7061 7373 6564 2074 6f20 6074 6f5f 6461  passed to `to_da
-00010c60: 7461 6672 616d 6528 2960 3b20 7365 6520  taframe()`; see 
-00010c70: 646f 6375 6d65 6e74 6174 696f 6e20 666f  documentation fo
-00010c80: 7220 7468 6174 206d 6574 686f 642e 0a20  r that method.. 
-00010c90: 2020 2020 2020 2020 2020 2073 697a 653a             size:
-00010ca0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00010cb0: 2054 6865 206e 616d 6520 6f66 2061 2068   The name of a h
-00010cc0: 7970 6572 2d70 6172 616d 6574 6572 2c20  yper-parameter, 
-00010cd0: 7468 6520 7661 6c75 6573 206f 6620 7768  the values of wh
-00010ce0: 6963 6820 7769 6c6c 2062 6520 7573 6564  ich will be used
-00010cf0: 2074 6f20 6465 7465 726d 696e 6520 7468   to determine th
-00010d00: 6520 7369 7a65 206f 6620 7468 650a 2020  e size of the.  
-00010d10: 2020 2020 2020 2020 2020 2020 2020 636f                co
-00010d20: 7272 6573 706f 6e64 696e 6720 706f 696e  rresponding poin
-00010d30: 7473 2069 6e20 7468 6520 706c 6f74 2e20  ts in the plot. 
-00010d40: 5468 6973 2076 616c 7565 2069 7320 7061  This value is pa
-00010d50: 7373 6564 2074 6f20 706c 6f74 6c79 2e0a  ssed to plotly..
-00010d60: 2020 2020 2020 2020 2020 2020 6865 6967              heig
-00010d70: 6874 3a0a 2020 2020 2020 2020 2020 2020  ht:.            
-00010d80: 2020 2020 5468 6520 6865 6967 6874 206f      The height o
-00010d90: 6620 7468 6520 706c 6f74 2e20 5468 6973  f the plot. This
-00010da0: 2076 616c 7565 2069 7320 7061 7373 6564   value is passed
-00010db0: 2074 6f20 706c 6f74 6c79 2e0a 2020 2020   to plotly..    
-00010dc0: 2020 2020 2020 2020 7769 6474 683a 0a20          width:. 
-00010dd0: 2020 2020 2020 2020 2020 2020 2020 2054                 T
-00010de0: 6865 2077 6964 7468 206f 6620 7468 6520  he width of the 
-00010df0: 706c 6f74 2e20 5468 6973 2076 616c 7565  plot. This value
-00010e00: 2069 7320 7061 7373 6564 2074 6f20 706c   is passed to pl
-00010e10: 6f74 6c79 2e0a 2020 2020 2020 2020 2222  otly..        ""
-00010e20: 220a 2020 2020 2020 2020 636f 6c6f 725f  ".        color_
-00010e30: 636f 6e74 696e 756f 7573 5f73 6361 6c65  continuous_scale
-00010e40: 203d 2070 782e 636f 6c6f 7273 2e64 6976   = px.colors.div
-00010e50: 6572 6769 6e67 2e52 6459 6c47 6e0a 2020  erging.RdYlGn.  
-00010e60: 2020 2020 2020 6966 206e 6f74 2073 656c        if not sel
-00010e70: 662e 6869 6768 6572 5f73 636f 7265 5f69  f.higher_score_i
-00010e80: 735f 6265 7474 6572 3a0a 2020 2020 2020  s_better:.      
-00010e90: 2020 2020 2020 636f 6c6f 725f 636f 6e74        color_cont
-00010ea0: 696e 756f 7573 5f73 6361 6c65 203d 2063  inuous_scale = c
-00010eb0: 6f6c 6f72 5f63 6f6e 7469 6e75 6f75 735f  olor_continuous_
-00010ec0: 7363 616c 652e 7265 7665 7273 6528 290a  scale.reverse().
-00010ed0: 0a20 2020 2020 2020 2070 7269 6d61 7279  .        primary
-00010ee0: 5f73 636f 7265 5f63 6f6c 756d 6e20 3d20  _score_column = 
-00010ef0: 7365 6c66 2e70 7269 6d61 7279 5f73 636f  self.primary_sco
-00010f00: 7265 5f6e 616d 6520 2b20 2220 4d65 616e  re_name + " Mean
-00010f10: 220a 2020 2020 2020 2020 7469 746c 6520  ".        title 
-00010f20: 3d20 6622 3c62 3e7b 7061 7261 6d65 7465  = f"<b>{paramete
-00010f30: 725f 797d 3c2f 623e 2076 7320 3c62 3e7b  r_y}</b> vs <b>{
-00010f40: 7061 7261 6d65 7465 725f 787d 3c2f 623e  parameter_x}</b>
-00010f50: 220a 0a20 2020 2020 2020 2073 6361 6c65  "..        scale
-00010f60: 645f 7369 7a65 203d 204e 6f6e 650a 2020  d_size = None.  
-00010f70: 2020 2020 2020 6c61 6265 6c65 645f 6466        labeled_df
-00010f80: 203d 2073 656c 662e 746f 5f6c 6162 656c   = self.to_label
-00010f90: 6564 5f64 6174 6166 7261 6d65 2871 7565  ed_dataframe(que
-00010fa0: 7279 3d71 7565 7279 290a 0a20 2020 2020  ry=query)..     
-00010fb0: 2020 2069 6620 7369 7a65 3a0a 2020 2020     if size:.    
-00010fc0: 2020 2020 2020 2020 7469 746c 6520 3d20          title = 
-00010fd0: 7469 746c 6520 2b20 6622 3c62 723e 3c73  title + f"<br><s
-00010fe0: 7570 3e54 6865 2073 697a 6520 6f66 2074  up>The size of t
-00010ff0: 6865 2070 6f69 6e74 2063 6f72 7265 7370  he point corresp
-00011000: 6f6e 6473 2074 6f20 7468 6520 7661 6c75  onds to the valu
-00011010: 6520 6f66 203c 623e 277b 7369 7a65 7d27  e of <b>'{size}'
-00011020: 3c2f 623e 2e3c 2f73 7570 3e22 0a20 2020  </b>.</sup>".   
-00011030: 2020 2020 2020 2020 2069 6620 7369 7a65           if size
-00011040: 2069 6e20 7365 6c66 2e6e 756d 6572 6963   in self.numeric
-00011050: 5f70 6172 616d 6574 6572 733a 0a20 2020  _parameters:.   
-00011060: 2020 2020 2020 2020 2020 2020 2023 206e               # n
-00011070: 6565 6420 746f 2064 6f20 7468 6973 206f  eed to do this o
-00011080: 7220 656c 7365 2074 6865 2070 6f69 6e74  r else the point
-00011090: 7320 6172 6520 616c 6c20 7468 6520 7361  s are all the sa
-000110a0: 6d65 2073 697a 650a 2020 2020 2020 2020  me size.        
-000110b0: 2020 2020 2020 2020 2320 6275 7420 6f6e          # but on
-000110c0: 6c79 2069 6620 7369 7a65 2068 6173 206e  ly if size has n
-000110d0: 756d 6572 6963 2076 616c 7565 730a 2020  umeric values.  
-000110e0: 2020 2020 2020 2020 2020 2020 2020 7363                sc
-000110f0: 616c 6564 5f73 697a 6520 3d20 4d69 6e4d  aled_size = MinM
-00011100: 6178 5363 616c 6572 2866 6561 7475 7265  axScaler(feature
-00011110: 5f72 616e 6765 3d28 302e 312c 2030 2e39  _range=(0.1, 0.9
-00011120: 2929 2e66 6974 5f74 7261 6e73 666f 726d  )).fit_transform
-00011130: 286c 6162 656c 6564 5f64 665b 5b73 697a  (labeled_df[[siz
-00011140: 655d 5d29 2e72 6573 6861 7065 2831 2c20  e]]).reshape(1, 
-00011150: 2d31 290a 2020 2020 2020 2020 2020 2020  -1).            
-00011160: 2020 2020 7363 616c 6564 5f73 697a 6520      scaled_size 
-00011170: 3d20 7363 616c 6564 5f73 697a 652e 746f  = scaled_size.to
-00011180: 6c69 7374 2829 5b30 5d0a 0a20 2020 2020  list()[0]..     
-00011190: 2020 2066 6967 203d 2070 782e 7363 6174     fig = px.scat
-000111a0: 7465 7228 0a20 2020 2020 2020 2020 2020  ter(.           
-000111b0: 2064 6174 615f 6672 616d 653d 6c61 6265   data_frame=labe
-000111c0: 6c65 645f 6466 2c0a 2020 2020 2020 2020  led_df,.        
-000111d0: 2020 2020 783d 7061 7261 6d65 7465 725f      x=parameter_
-000111e0: 782c 0a20 2020 2020 2020 2020 2020 2079  x,.            y
-000111f0: 3d70 6172 616d 6574 6572 5f79 2c0a 2020  =parameter_y,.  
-00011200: 2020 2020 2020 2020 2020 7369 7a65 3d73            size=s
-00011210: 6361 6c65 645f 7369 7a65 2c0a 2020 2020  caled_size,.    
-00011220: 2020 2020 2020 2020 636f 6c6f 723d 7072          color=pr
-00011230: 696d 6172 795f 7363 6f72 655f 636f 6c75  imary_score_colu
-00011240: 6d6e 2c0a 2020 2020 2020 2020 2020 2020  mn,.            
-00011250: 636f 6c6f 725f 636f 6e74 696e 756f 7573  color_continuous
-00011260: 5f73 6361 6c65 3d63 6f6c 6f72 5f63 6f6e  _scale=color_con
-00011270: 7469 6e75 6f75 735f 7363 616c 652c 0a20  tinuous_scale,. 
-00011280: 2020 2020 2020 2020 2020 2074 7265 6e64             trend
-00011290: 6c69 6e65 3d27 6c6f 7765 7373 272c 0a20  line='lowess',. 
-000112a0: 2020 2020 2020 2020 2020 2074 6974 6c65             title
-000112b0: 3d74 6974 6c65 2c0a 2020 2020 2020 2020  =title,.        
-000112c0: 2020 2020 6375 7374 6f6d 5f64 6174 613d      custom_data=
-000112d0: 5b27 6c61 6265 6c27 2c20 7072 696d 6172  ['label', primar
-000112e0: 795f 7363 6f72 655f 636f 6c75 6d6e 5d2c  y_score_column],
-000112f0: 0a20 2020 2020 2020 2020 2020 2068 6569  .            hei
-00011300: 6768 743d 6865 6967 6874 2c0a 2020 2020  ght=height,.    
-00011310: 2020 2020 2020 2020 7769 6474 683d 7769          width=wi
-00011320: 6474 682c 0a20 2020 2020 2020 2029 0a20  dth,.        ). 
-00011330: 2020 2020 2020 2066 6967 2e75 7064 6174         fig.updat
-00011340: 655f 7472 6163 6573 280a 2020 2020 2020  e_traces(.      
-00011350: 2020 2020 2020 686f 7665 7274 656d 706c        hovertempl
-00011360: 6174 653d 223c 6272 3e22 2e6a 6f69 6e28  ate="<br>".join(
-00011370: 5b0a 2020 2020 2020 2020 2020 2020 2020  [.              
-00011380: 2020 7061 7261 6d65 7465 725f 7820 2b20    parameter_x + 
-00011390: 223a 2025 7b78 7d22 2c0a 2020 2020 2020  ": %{x}",.      
-000113a0: 2020 2020 2020 2020 2020 7061 7261 6d65            parame
-000113b0: 7465 725f 7920 2b20 223a 2025 7b79 7d22  ter_y + ": %{y}"
-000113c0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-000113d0: 2020 7072 696d 6172 795f 7363 6f72 655f    primary_score_
-000113e0: 636f 6c75 6d6e 202b 2022 3a20 2220 2b20  column + ": " + 
-000113f0: 2225 7b63 7573 746f 6d64 6174 615b 315d  "%{customdata[1]
-00011400: 7d22 2c0a 2020 2020 2020 2020 2020 2020  }",.            
-00011410: 2020 2020 223c 6272 3e50 6172 616d 6574      "<br>Paramet
-00011420: 6572 733a 2025 7b63 7573 746f 6d64 6174  ers: %{customdat
-00011430: 615b 305d 7d22 2c0a 2020 2020 2020 2020  a[0]}",.        
-00011440: 2020 2020 5d29 0a20 2020 2020 2020 2029      ]).        )
-00011450: 0a20 2020 2020 2020 2072 6574 7572 6e20  .        return 
-00011460: 6669 670a 0a0a 2320 7079 6c69 6e74 3a20  fig...# pylint: 
-00011470: 6469 7361 626c 653d 746f 6f2d 6d61 6e79  disable=too-many
-00011480: 2d69 6e73 7461 6e63 652d 6174 7472 6962  -instance-attrib
-00011490: 7574 6573 0a23 2070 796c 696e 743a 2064  utes.# pylint: d
-000114a0: 6973 6162 6c65 3d74 6f6f 2d6d 616e 792d  isable=too-many-
-000114b0: 7075 626c 6963 2d6d 6574 686f 6473 0a23  public-methods.#
-000114c0: 2070 796c 696e 743a 2064 6973 6162 6c65   pylint: disable
-000114d0: 3d74 6f6f 2d6d 616e 792d 696e 7374 616e  =too-many-instan
-000114e0: 6365 2d61 7474 7269 6275 7465 732c 746f  ce-attributes,to
-000114f0: 6f2d 6d61 6e79 2d70 7562 6c69 632d 6d65  o-many-public-me
-00011500: 7468 6f64 730a 636c 6173 7320 5477 6f43  thods.class TwoC
-00011510: 6c61 7373 4576 616c 7561 746f 723a 0a20  lassEvaluator:. 
-00011520: 2020 2022 2222 5468 6973 2063 6c61 7373     """This class
-00011530: 2063 616c 6375 6c61 7465 7320 7661 7269   calculates vari
-00011540: 6f75 7320 6d65 7472 6963 7320 666f 7220  ous metrics for 
-00011550: 5477 6f20 436c 6173 7320 2869 2e65 2e20  Two Class (i.e. 
-00011560: 3027 732f 3127 7329 2070 7265 6469 6374  0's/1's) predict
-00011570: 696f 6e20 7363 656e 6172 696f 732e 2222  ion scenarios.""
-00011580: 220a 2020 2020 2320 7079 6c69 6e74 3a20  ".    # pylint: 
-00011590: 6469 7361 626c 653d 746f 6f2d 6d61 6e79  disable=too-many
-000115a0: 2d61 7267 756d 656e 7473 0a20 2020 2064  -arguments.    d
-000115b0: 6566 205f 5f69 6e69 745f 5f28 7365 6c66  ef __init__(self
-000115c0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-000115d0: 2020 2061 6374 7561 6c5f 7661 6c75 6573     actual_values
-000115e0: 3a20 6e70 2e6e 6461 7272 6179 2c0a 2020  : np.ndarray,.  
-000115f0: 2020 2020 2020 2020 2020 2020 2020 2070                 p
-00011600: 7265 6469 6374 6564 5f73 636f 7265 733a  redicted_scores:
-00011610: 206e 702e 6e64 6172 7261 792c 0a20 2020   np.ndarray,.   
-00011620: 2020 2020 2020 2020 2020 2020 2020 706f                po
-00011630: 7369 7469 7665 5f63 6c61 7373 3a20 7374  sitive_class: st
-00011640: 7220 3d20 2750 6f73 6974 6976 6520 436c  r = 'Positive Cl
-00011650: 6173 7327 2c0a 2020 2020 2020 2020 2020  ass',.          
-00011660: 2020 2020 2020 206e 6567 6174 6976 655f         negative_
-00011670: 636c 6173 733a 2073 7472 203d 2027 4e65  class: str = 'Ne
-00011680: 6761 7469 7665 2043 6c61 7373 272c 0a20  gative Class',. 
-00011690: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000116a0: 7363 6f72 655f 7468 7265 7368 6f6c 643a  score_threshold:
-000116b0: 2066 6c6f 6174 203d 2030 2e35 0a20 2020   float = 0.5.   
-000116c0: 2020 2020 2020 2020 2020 2020 2020 293a                ):
-000116d0: 0a20 2020 2020 2020 2022 2222 0a20 2020  .        """.   
-000116e0: 2020 2020 2041 7267 733a 0a20 2020 2020       Args:.     
-000116f0: 2020 2020 2020 2061 6374 7561 6c5f 7661         actual_va
-00011700: 6c75 6573 3a0a 2020 2020 2020 2020 2020  lues:.          
-00011710: 2020 2020 2020 6172 7261 7920 6f66 2030        array of 0
-00011720: 2773 2061 6e64 2031 2773 0a20 2020 2020  's and 1's.     
-00011730: 2020 2020 2020 2070 7265 6469 6374 6564         predicted
-00011740: 5f73 636f 7265 733a 0a20 2020 2020 2020  _scores:.       
-00011750: 2020 2020 2020 2020 2061 7272 6179 206f           array o
-00011760: 6620 6465 6369 6d61 6c2f 666c 6f61 7420  f decimal/float 
-00011770: 7661 6c75 6573 2066 726f 6d20 6070 7265  values from `pre
-00011780: 6469 6374 5f70 726f 6261 2829 603b 204e  dict_proba()`; N
-00011790: 4f54 2074 6865 2061 6374 7561 6c20 636c  OT the actual cl
-000117a0: 6173 730a 2020 2020 2020 2020 2020 2020  ass.            
-000117b0: 706f 7369 7469 7665 5f63 6c61 7373 3a0a  positive_class:.
-000117c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000117d0: 7374 7269 6e67 206f 6620 7468 6520 6e61  string of the na
-000117e0: 6d65 2f6c 6162 656c 206f 6620 7468 6520  me/label of the 
-000117f0: 706f 7369 7469 7665 2063 6c61 7373 2028  positive class (
-00011800: 692e 652e 2076 616c 7565 206f 6620 3129  i.e. value of 1)
-00011810: 2e20 496e 206f 7468 6572 2077 6f72 6473  . In other words
-00011820: 2c20 6e6f 740a 2020 2020 2020 2020 2020  , not.          
-00011830: 2020 2020 2020 2770 6f73 6974 6976 6527        'positive'
-00011840: 2069 6e20 7468 6520 7365 6e73 6520 6f66   in the sense of
-00011850: 2027 676f 6f64 2720 6275 7420 2770 6f73   'good' but 'pos
-00011860: 6974 6976 6527 2061 7320 696e 2027 5472  itive' as in 'Tr
-00011870: 7565 2f46 616c 7365 2050 6f73 6974 6976  ue/False Positiv
-00011880: 6527 2e0a 2020 2020 2020 2020 2020 2020  e'..            
-00011890: 6e65 6761 7469 7665 5f63 6c61 7373 3a0a  negative_class:.
-000118a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000118b0: 7374 7269 6e67 206f 6620 7468 6520 6e61  string of the na
-000118c0: 6d65 2f6c 6162 656c 206f 6620 7468 6520  me/label of the 
-000118d0: 6e65 6761 7469 7665 2063 6c61 7373 2028  negative class (
-000118e0: 692e 652e 2076 616c 7565 206f 6620 3029  i.e. value of 0)
-000118f0: 2e20 496e 206f 7468 6572 2077 6f72 6473  . In other words
-00011900: 2c20 6e6f 740a 2020 2020 2020 2020 2020  , not.          
-00011910: 2020 2020 2020 276e 6567 6174 6976 6527        'negative'
-00011920: 2069 6e20 7468 6520 7365 6e73 6520 6f66   in the sense of
-00011930: 2027 676f 6f64 2720 6275 7420 276e 6567   'good' but 'neg
-00011940: 6174 6976 6527 2061 7320 696e 2027 5472  ative' as in 'Tr
-00011950: 7565 2f46 616c 7365 204e 6567 6174 6976  ue/False Negativ
-00011960: 6527 2e0a 2020 2020 2020 2020 2020 2020  e'..            
-00011970: 7363 6f72 655f 7468 7265 7368 6f6c 643a  score_threshold:
-00011980: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00011990: 2074 6865 2073 636f 7265 2f70 726f 6261   the score/proba
-000119a0: 6269 6c69 7479 2074 6872 6573 686f 6c64  bility threshold
-000119b0: 2066 6f72 2074 7572 6e69 6e67 2073 636f   for turning sco
-000119c0: 7265 7320 696e 746f 2030 2773 2061 6e64  res into 0's and
-000119d0: 2031 2773 2061 6e64 2063 6f72 7265 7370   1's and corresp
-000119e0: 6f6e 6469 6e67 206c 6162 656c 730a 2020  onding labels.  
-000119f0: 2020 2020 2020 2222 220a 2020 2020 2020        """.      
-00011a00: 2020 6173 7365 7274 206c 656e 2861 6374    assert len(act
-00011a10: 7561 6c5f 7661 6c75 6573 2920 3d3d 206c  ual_values) == l
-00011a20: 656e 2870 7265 6469 6374 6564 5f73 636f  en(predicted_sco
-00011a30: 7265 7329 0a0a 2020 2020 2020 2020 6966  res)..        if
-00011a40: 206e 6f74 2061 6c6c 286e 702e 756e 6971   not all(np.uniq
-00011a50: 7565 2861 6374 7561 6c5f 7661 6c75 6573  ue(actual_values
-00011a60: 2920 3d3d 205b 302c 2031 5d29 3a0a 2020  ) == [0, 1]):.  
-00011a70: 2020 2020 2020 2020 2020 6d65 7373 6167            messag
-00011a80: 6520 3d20 6622 5661 6c75 6573 206f 6620  e = f"Values of 
-00011a90: 6061 6374 7561 6c5f 7661 6c75 6573 6020  `actual_values` 
-00011aa0: 7368 6f75 6c64 2030 206f 7220 312e 2046  should 0 or 1. F
-00011ab0: 6f75 6e64 2060 7b6e 702e 756e 6971 7565  ound `{np.unique
-00011ac0: 2861 6374 7561 6c5f 7661 6c75 6573 297d  (actual_values)}
-00011ad0: 6022 0a20 2020 2020 2020 2020 2020 2072  `".            r
-00011ae0: 6169 7365 2048 656c 7073 6b50 6172 616d  aise HelpskParam
-00011af0: 5661 6c75 6545 7272 6f72 286d 6573 7361  ValueError(messa
-00011b00: 6765 290a 0a20 2020 2020 2020 2069 6620  ge)..        if 
-00011b10: 6e6f 7420 616c 6c28 6e70 2e6c 6f67 6963  not all(np.logic
-00011b20: 616c 5f61 6e64 2870 7265 6469 6374 6564  al_and(predicted
-00011b30: 5f73 636f 7265 7320 3e3d 2030 2c20 7072  _scores >= 0, pr
-00011b40: 6564 6963 7465 645f 7363 6f72 6573 203c  edicted_scores <
-00011b50: 3d20 3129 293a 0a20 2020 2020 2020 2020  = 1)):.         
-00011b60: 2020 206d 6573 7361 6765 203d 2022 5661     message = "Va
-00011b70: 6c75 6573 206f 6620 6070 7265 6469 6374  lues of `predict
-00011b80: 6564 5f73 636f 7265 7360 2073 686f 756c  ed_scores` shoul
-00011b90: 6420 6265 2062 6574 7765 656e 2030 2061  d be between 0 a
-00011ba0: 6e64 2031 2e22 0a20 2020 2020 2020 2020  nd 1.".         
-00011bb0: 2020 2072 6169 7365 2048 656c 7073 6b50     raise HelpskP
-00011bc0: 6172 616d 5661 6c75 6545 7272 6f72 286d  aramValueError(m
-00011bd0: 6573 7361 6765 290a 0a20 2020 2020 2020  essage)..       
-00011be0: 2073 656c 662e 5f70 6f73 6974 6976 655f   self._positive_
-00011bf0: 636c 6173 7320 3d20 706f 7369 7469 7665  class = positive
-00011c00: 5f63 6c61 7373 0a20 2020 2020 2020 2073  _class.        s
-00011c10: 656c 662e 5f6e 6567 6174 6976 655f 636c  elf._negative_cl
-00011c20: 6173 7320 3d20 6e65 6761 7469 7665 5f63  ass = negative_c
-00011c30: 6c61 7373 0a20 2020 2020 2020 2073 656c  lass.        sel
-00011c40: 662e 5f61 6374 7561 6c5f 7661 6c75 6573  f._actual_values
-00011c50: 203d 2061 6374 7561 6c5f 7661 6c75 6573   = actual_values
-00011c60: 0a20 2020 2020 2020 2073 656c 662e 5f70  .        self._p
-00011c70: 7265 6469 6374 6564 5f73 636f 7265 7320  redicted_scores 
-00011c80: 3d20 7072 6564 6963 7465 645f 7363 6f72  = predicted_scor
-00011c90: 6573 0a20 2020 2020 2020 2073 656c 662e  es.        self.
-00011ca0: 7363 6f72 655f 7468 7265 7368 6f6c 6420  score_threshold 
-00011cb0: 3d20 7363 6f72 655f 7468 7265 7368 6f6c  = score_threshol
-00011cc0: 640a 2020 2020 2020 2020 7072 6564 6963  d.        predic
-00011cd0: 7465 645f 7661 6c75 6573 203d 206e 702e  ted_values = np.
-00011ce0: 7768 6572 6528 7072 6564 6963 7465 645f  where(predicted_
-00011cf0: 7363 6f72 6573 203e 2073 656c 662e 7363  scores > self.sc
-00011d00: 6f72 655f 7468 7265 7368 6f6c 642c 2031  ore_threshold, 1
-00011d10: 2c20 3029 0a20 2020 2020 2020 2073 656c  , 0).        sel
-00011d20: 662e 5f63 6f6e 6675 7369 6f6e 5f6d 6174  f._confusion_mat
-00011d30: 7269 7820 3d20 636f 6e66 7573 696f 6e5f  rix = confusion_
-00011d40: 6d61 7472 6978 2879 5f74 7275 653d 6163  matrix(y_true=ac
-00011d50: 7475 616c 5f76 616c 7565 732c 2079 5f70  tual_values, y_p
-00011d60: 7265 643d 7072 6564 6963 7465 645f 7661  red=predicted_va
-00011d70: 6c75 6573 290a 0a20 2020 2020 2020 2073  lues)..        s
-00011d80: 656c 662e 7361 6d70 6c65 5f73 697a 6520  elf.sample_size 
-00011d90: 3d20 6c65 6e28 6163 7475 616c 5f76 616c  = len(actual_val
-00011da0: 7565 7329 0a20 2020 2020 2020 2061 7373  ues).        ass
-00011db0: 6572 7420 7365 6c66 2e73 616d 706c 655f  ert self.sample_
-00011dc0: 7369 7a65 203d 3d20 7365 6c66 2e5f 636f  size == self._co
-00011dd0: 6e66 7573 696f 6e5f 6d61 7472 6978 2e73  nfusion_matrix.s
-00011de0: 756d 2829 0a0a 2020 2020 2020 2020 7472  um()..        tr
-00011df0: 7565 5f6e 6567 6174 6976 6573 2c20 6661  ue_negatives, fa
-00011e00: 6c73 655f 706f 7369 7469 7665 732c 2066  lse_positives, f
-00011e10: 616c 7365 5f6e 6567 6174 6976 6573 2c20  alse_negatives, 
-00011e20: 7472 7565 5f70 6f73 6974 6976 6573 203d  true_positives =
-00011e30: 2073 656c 662e 5f63 6f6e 6675 7369 6f6e   self._confusion
-00011e40: 5f6d 6174 7269 782e 7261 7665 6c28 290a  _matrix.ravel().
-00011e50: 0a20 2020 2020 2020 2073 656c 662e 5f61  .        self._a
-00011e60: 6374 7561 6c5f 706f 7369 7469 7665 7320  ctual_positives 
-00011e70: 3d20 7472 7565 5f70 6f73 6974 6976 6573  = true_positives
-00011e80: 202b 2066 616c 7365 5f6e 6567 6174 6976   + false_negativ
-00011e90: 6573 0a20 2020 2020 2020 2061 7373 6572  es.        asser
-00011ea0: 7420 7365 6c66 2e5f 6163 7475 616c 5f70  t self._actual_p
-00011eb0: 6f73 6974 6976 6573 203d 3d20 7375 6d28  ositives == sum(
-00011ec0: 7365 6c66 2e5f 6163 7475 616c 5f76 616c  self._actual_val
-00011ed0: 7565 7320 3d3d 2031 290a 0a20 2020 2020  ues == 1)..     
-00011ee0: 2020 2073 656c 662e 5f61 6374 7561 6c5f     self._actual_
-00011ef0: 6e65 6761 7469 7665 7320 3d20 7472 7565  negatives = true
-00011f00: 5f6e 6567 6174 6976 6573 202b 2066 616c  _negatives + fal
-00011f10: 7365 5f70 6f73 6974 6976 6573 0a0a 2020  se_positives..  
-00011f20: 2020 2020 2020 7365 6c66 2e5f 7472 7565        self._true
-00011f30: 5f6e 6567 6174 6976 6573 203d 2074 7275  _negatives = tru
-00011f40: 655f 6e65 6761 7469 7665 730a 2020 2020  e_negatives.    
-00011f50: 2020 2020 7365 6c66 2e5f 6661 6c73 655f      self._false_
-00011f60: 706f 7369 7469 7665 7320 3d20 6661 6c73  positives = fals
-00011f70: 655f 706f 7369 7469 7665 730a 2020 2020  e_positives.    
-00011f80: 2020 2020 7365 6c66 2e5f 6661 6c73 655f      self._false_
-00011f90: 6e65 6761 7469 7665 7320 3d20 6661 6c73  negatives = fals
-00011fa0: 655f 6e65 6761 7469 7665 730a 2020 2020  e_negatives.    
-00011fb0: 2020 2020 7365 6c66 2e5f 7472 7565 5f70      self._true_p
-00011fc0: 6f73 6974 6976 6573 203d 2074 7275 655f  ositives = true_
-00011fd0: 706f 7369 7469 7665 730a 0a20 2020 2020  positives..     
-00011fe0: 2020 2073 656c 662e 6175 6320 3d20 726f     self.auc = ro
-00011ff0: 635f 6175 635f 7363 6f72 6528 795f 7472  c_auc_score(y_tr
-00012000: 7565 3d61 6374 7561 6c5f 7661 6c75 6573  ue=actual_values
-00012010: 2c20 795f 7363 6f72 653d 7072 6564 6963  , y_score=predic
-00012020: 7465 645f 7363 6f72 6573 290a 0a20 2020  ted_scores)..   
-00012030: 2040 7072 6f70 6572 7479 0a20 2020 2064   @property.    d
-00012040: 6566 2074 7275 655f 706f 7369 7469 7665  ef true_positive
-00012050: 5f72 6174 6528 7365 6c66 2920 2d3e 2066  _rate(self) -> f
-00012060: 6c6f 6174 3a0a 2020 2020 2020 2020 2222  loat:.        ""
-00012070: 2254 7275 6520 506f 7369 7469 7665 2052  "True Positive R
-00012080: 6174 6522 2222 0a20 2020 2020 2020 2072  ate""".        r
-00012090: 6574 7572 6e20 3020 6966 2073 656c 662e  eturn 0 if self.
-000120a0: 5f61 6374 7561 6c5f 706f 7369 7469 7665  _actual_positive
-000120b0: 7320 3d3d 2030 2065 6c73 6520 7365 6c66  s == 0 else self
-000120c0: 2e5f 7472 7565 5f70 6f73 6974 6976 6573  ._true_positives
-000120d0: 202f 2073 656c 662e 5f61 6374 7561 6c5f   / self._actual_
-000120e0: 706f 7369 7469 7665 730a 0a20 2020 2040  positives..    @
-000120f0: 7072 6f70 6572 7479 0a20 2020 2064 6566  property.    def
-00012100: 2074 7275 655f 6e65 6761 7469 7665 5f72   true_negative_r
-00012110: 6174 6528 7365 6c66 2920 2d3e 2066 6c6f  ate(self) -> flo
-00012120: 6174 3a0a 2020 2020 2020 2020 2222 2254  at:.        """T
-00012130: 7275 6520 4e65 6761 7469 7665 2052 6174  rue Negative Rat
-00012140: 6520 692e 652e 2053 7065 6369 6669 6369  e i.e. Specifici
-00012150: 7479 2222 220a 2020 2020 2020 2020 7265  ty""".        re
-00012160: 7475 726e 2030 2069 6620 7365 6c66 2e5f  turn 0 if self._
-00012170: 6163 7475 616c 5f6e 6567 6174 6976 6573  actual_negatives
-00012180: 203d 3d20 3020 656c 7365 2073 656c 662e   == 0 else self.
-00012190: 5f74 7275 655f 6e65 6761 7469 7665 7320  _true_negatives 
-000121a0: 2f20 7365 6c66 2e5f 6163 7475 616c 5f6e  / self._actual_n
-000121b0: 6567 6174 6976 6573 0a0a 2020 2020 4070  egatives..    @p
-000121c0: 726f 7065 7274 790a 2020 2020 6465 6620  roperty.    def 
-000121d0: 6661 6c73 655f 6e65 6761 7469 7665 5f72  false_negative_r
-000121e0: 6174 6528 7365 6c66 2920 2d3e 2066 6c6f  ate(self) -> flo
-000121f0: 6174 3a0a 2020 2020 2020 2020 2222 2246  at:.        """F
-00012200: 616c 7365 204e 6567 6174 6976 6520 5261  alse Negative Ra
-00012210: 7465 2222 220a 2020 2020 2020 2020 7265  te""".        re
-00012220: 7475 726e 2030 2069 6620 7365 6c66 2e5f  turn 0 if self._
-00012230: 6163 7475 616c 5f70 6f73 6974 6976 6573  actual_positives
-00012240: 203d 3d20 3020 656c 7365 2073 656c 662e   == 0 else self.
-00012250: 5f66 616c 7365 5f6e 6567 6174 6976 6573  _false_negatives
-00012260: 202f 2073 656c 662e 5f61 6374 7561 6c5f   / self._actual_
-00012270: 706f 7369 7469 7665 730a 0a20 2020 2040  positives..    @
-00012280: 7072 6f70 6572 7479 0a20 2020 2064 6566  property.    def
-00012290: 2066 616c 7365 5f70 6f73 6974 6976 655f   false_positive_
-000122a0: 7261 7465 2873 656c 6629 202d 3e20 666c  rate(self) -> fl
-000122b0: 6f61 743a 0a20 2020 2020 2020 2022 2222  oat:.        """
-000122c0: 4661 6c73 6520 506f 7369 7469 7665 2052  False Positive R
-000122d0: 6174 6522 2222 0a20 2020 2020 2020 2072  ate""".        r
-000122e0: 6574 7572 6e20 3020 6966 2073 656c 662e  eturn 0 if self.
-000122f0: 5f61 6374 7561 6c5f 6e65 6761 7469 7665  _actual_negative
-00012300: 7320 3d3d 2030 2065 6c73 6520 7365 6c66  s == 0 else self
-00012310: 2e5f 6661 6c73 655f 706f 7369 7469 7665  ._false_positive
-00012320: 7320 2f20 7365 6c66 2e5f 6163 7475 616c  s / self._actual
-00012330: 5f6e 6567 6174 6976 6573 0a0a 2020 2020  _negatives..    
-00012340: 4070 726f 7065 7274 790a 2020 2020 6465  @property.    de
-00012350: 6620 6163 6375 7261 6379 2873 656c 6629  f accuracy(self)
-00012360: 202d 3e20 556e 696f 6e5b 666c 6f61 742c   -> Union[float,
-00012370: 204e 6f6e 655d 3a0a 2020 2020 2020 2020   None]:.        
-00012380: 2222 2261 6363 7572 6163 7922 2222 0a20  """accuracy""". 
-00012390: 2020 2020 2020 2072 6574 7572 6e20 4e6f         return No
-000123a0: 6e65 2069 6620 7365 6c66 2e73 616d 706c  ne if self.sampl
-000123b0: 655f 7369 7a65 203d 3d20 3020 656c 7365  e_size == 0 else
-000123c0: 205c 0a20 2020 2020 2020 2020 2020 2028   \.            (
-000123d0: 7365 6c66 2e5f 7472 7565 5f6e 6567 6174  self._true_negat
-000123e0: 6976 6573 202b 2073 656c 662e 5f74 7275  ives + self._tru
-000123f0: 655f 706f 7369 7469 7665 7329 202f 2073  e_positives) / s
-00012400: 656c 662e 7361 6d70 6c65 5f73 697a 650a  elf.sample_size.
-00012410: 0a20 2020 2040 7072 6f70 6572 7479 0a20  .    @property. 
-00012420: 2020 2064 6566 2065 7272 6f72 5f72 6174     def error_rat
-00012430: 6528 7365 6c66 2920 2d3e 2055 6e69 6f6e  e(self) -> Union
-00012440: 5b66 6c6f 6174 2c20 4e6f 6e65 5d3a 0a20  [float, None]:. 
-00012450: 2020 2020 2020 2022 2222 6572 726f 725f         """error_
-00012460: 7261 7465 2222 220a 2020 2020 2020 2020  rate""".        
-00012470: 7265 7475 726e 204e 6f6e 6520 6966 2073  return None if s
-00012480: 656c 662e 7361 6d70 6c65 5f73 697a 6520  elf.sample_size 
-00012490: 3d3d 2030 2065 6c73 6520 5c0a 2020 2020  == 0 else \.    
-000124a0: 2020 2020 2020 2020 2873 656c 662e 5f66          (self._f
-000124b0: 616c 7365 5f70 6f73 6974 6976 6573 202b  alse_positives +
-000124c0: 2073 656c 662e 5f66 616c 7365 5f6e 6567   self._false_neg
-000124d0: 6174 6976 6573 2920 2f20 7365 6c66 2e73  atives) / self.s
-000124e0: 616d 706c 655f 7369 7a65 0a0a 2020 2020  ample_size..    
-000124f0: 4070 726f 7065 7274 790a 2020 2020 6465  @property.    de
-00012500: 6620 706f 7369 7469 7665 5f70 7265 6469  f positive_predi
-00012510: 6374 6976 655f 7661 6c75 6528 7365 6c66  ctive_value(self
-00012520: 2920 2d3e 2066 6c6f 6174 3a0a 2020 2020  ) -> float:.    
-00012530: 2020 2020 2222 2250 6f73 6974 6976 6520      """Positive 
-00012540: 5072 6564 6963 7469 7665 2056 616c 7565  Predictive Value
-00012550: 2069 2e65 2e20 5072 6563 6973 696f 6e22   i.e. Precision"
-00012560: 2222 0a20 2020 2020 2020 2072 6574 7572  "".        retur
-00012570: 6e20 3020 6966 2028 7365 6c66 2e5f 7472  n 0 if (self._tr
-00012580: 7565 5f70 6f73 6974 6976 6573 202b 2073  ue_positives + s
-00012590: 656c 662e 5f66 616c 7365 5f70 6f73 6974  elf._false_posit
-000125a0: 6976 6573 2920 3d3d 2030 2065 6c73 6520  ives) == 0 else 
-000125b0: 5c0a 2020 2020 2020 2020 2020 2020 7365  \.            se
-000125c0: 6c66 2e5f 7472 7565 5f70 6f73 6974 6976  lf._true_positiv
-000125d0: 6573 202f 2028 7365 6c66 2e5f 7472 7565  es / (self._true
-000125e0: 5f70 6f73 6974 6976 6573 202b 2073 656c  _positives + sel
-000125f0: 662e 5f66 616c 7365 5f70 6f73 6974 6976  f._false_positiv
-00012600: 6573 290a 0a20 2020 2040 7072 6f70 6572  es)..    @proper
-00012610: 7479 0a20 2020 2064 6566 206e 6567 6174  ty.    def negat
-00012620: 6976 655f 7072 6564 6963 7469 7665 5f76  ive_predictive_v
-00012630: 616c 7565 2873 656c 6629 202d 3e20 666c  alue(self) -> fl
-00012640: 6f61 743a 0a20 2020 2020 2020 2022 2222  oat:.        """
-00012650: 4e65 6761 7469 7665 2050 7265 6469 6374  Negative Predict
-00012660: 6976 6520 5661 6c75 6522 2222 0a20 2020  ive Value""".   
-00012670: 2020 2020 2072 6574 7572 6e20 3020 6966       return 0 if
-00012680: 2028 7365 6c66 2e5f 7472 7565 5f6e 6567   (self._true_neg
-00012690: 6174 6976 6573 202b 2073 656c 662e 5f66  atives + self._f
-000126a0: 616c 7365 5f6e 6567 6174 6976 6573 2920  alse_negatives) 
-000126b0: 3d3d 2030 2065 6c73 6520 5c0a 2020 2020  == 0 else \.    
-000126c0: 2020 2020 2020 2020 7365 6c66 2e5f 7472          self._tr
-000126d0: 7565 5f6e 6567 6174 6976 6573 202f 2028  ue_negatives / (
-000126e0: 7365 6c66 2e5f 7472 7565 5f6e 6567 6174  self._true_negat
-000126f0: 6976 6573 202b 2073 656c 662e 5f66 616c  ives + self._fal
-00012700: 7365 5f6e 6567 6174 6976 6573 290a 0a20  se_negatives).. 
-00012710: 2020 2040 7072 6f70 6572 7479 0a20 2020     @property.   
-00012720: 2064 6566 2070 7265 7661 6c65 6e63 6528   def prevalence(
-00012730: 7365 6c66 2920 2d3e 2055 6e69 6f6e 5b66  self) -> Union[f
-00012740: 6c6f 6174 2c20 4e6f 6e65 5d3a 0a20 2020  loat, None]:.   
-00012750: 2020 2020 2022 2222 5072 6576 616c 656e       """Prevalen
-00012760: 6365 2222 220a 2020 2020 2020 2020 7265  ce""".        re
-00012770: 7475 726e 204e 6f6e 6520 6966 2073 656c  turn None if sel
-00012780: 662e 7361 6d70 6c65 5f73 697a 6520 3d3d  f.sample_size ==
-00012790: 2030 2065 6c73 6520 5c0a 2020 2020 2020   0 else \.      
-000127a0: 2020 2020 2020 7365 6c66 2e5f 6163 7475        self._actu
-000127b0: 616c 5f70 6f73 6974 6976 6573 202f 2073  al_positives / s
-000127c0: 656c 662e 7361 6d70 6c65 5f73 697a 650a  elf.sample_size.
-000127d0: 0a20 2020 2040 7072 6f70 6572 7479 0a20  .    @property. 
-000127e0: 2020 2064 6566 206b 6170 7061 2873 656c     def kappa(sel
-000127f0: 6629 202d 3e20 556e 696f 6e5b 666c 6f61  f) -> Union[floa
-00012800: 742c 204e 6f6e 655d 3a0a 2020 2020 2020  t, None]:.      
-00012810: 2020 2222 224b 6170 7061 2222 220a 2020    """Kappa""".  
-00012820: 2020 2020 2020 6966 2073 656c 662e 7361        if self.sa
-00012830: 6d70 6c65 5f73 697a 6520 3d3d 2030 206f  mple_size == 0 o
-00012840: 7220 5c0a 2020 2020 2020 2020 2020 2020  r \.            
-00012850: 2020 2020 2828 7365 6c66 2e5f 7472 7565      ((self._true
-00012860: 5f6e 6567 6174 6976 6573 202b 2073 656c  _negatives + sel
-00012870: 662e 5f66 616c 7365 5f6e 6567 6174 6976  f._false_negativ
-00012880: 6573 2920 2f20 7365 6c66 2e73 616d 706c  es) / self.sampl
-00012890: 655f 7369 7a65 2920 3d3d 2030 3a0a 2020  e_size) == 0:.  
-000128a0: 2020 2020 2020 2020 2020 7265 7475 726e            return
-000128b0: 204e 6f6e 650a 2020 2020 2020 2020 2320   None.        # 
-000128c0: 7072 6f70 6f72 7469 6f6e 206f 6620 7468  proportion of th
-000128d0: 6520 6163 7475 616c 2061 6772 6565 6d65  e actual agreeme
-000128e0: 6e74 730a 2020 2020 2020 2020 2320 6164  nts.        # ad
-000128f0: 6420 7468 6520 7072 6f70 6f72 7469 6f6e  d the proportion
-00012900: 206f 6620 616c 6c20 696e 7374 616e 6365   of all instance
-00012910: 7320 7768 6572 6520 7468 6520 7072 6564  s where the pred
-00012920: 6963 7465 6420 7479 7065 2061 6e64 2061  icted type and a
-00012930: 6374 7561 6c20 7479 7065 2061 6772 6565  ctual type agree
-00012940: 0a20 2020 2020 2020 2070 725f 6120 3d20  .        pr_a = 
-00012950: 2873 656c 662e 5f74 7275 655f 6e65 6761  (self._true_nega
-00012960: 7469 7665 7320 2b20 7365 6c66 2e5f 7472  tives + self._tr
-00012970: 7565 5f70 6f73 6974 6976 6573 2920 2f20  ue_positives) / 
-00012980: 7365 6c66 2e73 616d 706c 655f 7369 7a65  self.sample_size
-00012990: 0a20 2020 2020 2020 2023 2070 726f 6261  .        # proba
-000129a0: 6269 6c69 7479 206f 6620 626f 7468 2070  bility of both p
-000129b0: 7265 6469 6374 6564 2061 6e64 2061 6374  redicted and act
-000129c0: 7561 6c20 6265 696e 6720 6e65 6761 7469  ual being negati
-000129d0: 7665 0a20 2020 2020 2020 2070 5f6e 6567  ve.        p_neg
-000129e0: 6174 6976 655f 7072 6564 6963 7469 6f6e  ative_prediction
-000129f0: 5f61 6e64 5f61 6374 7561 6c20 3d20 5c0a  _and_actual = \.
-00012a00: 2020 2020 2020 2020 2020 2020 2828 7365              ((se
-00012a10: 6c66 2e5f 7472 7565 5f6e 6567 6174 6976  lf._true_negativ
-00012a20: 6573 202b 2073 656c 662e 5f66 616c 7365  es + self._false
-00012a30: 5f70 6f73 6974 6976 6573 2920 2f20 7365  _positives) / se
-00012a40: 6c66 2e73 616d 706c 655f 7369 7a65 2920  lf.sample_size) 
-00012a50: 2a20 5c0a 2020 2020 2020 2020 2020 2020  * \.            
-00012a60: 2828 7365 6c66 2e5f 7472 7565 5f6e 6567  ((self._true_neg
-00012a70: 6174 6976 6573 202b 2073 656c 662e 5f66  atives + self._f
-00012a80: 616c 7365 5f6e 6567 6174 6976 6573 2920  alse_negatives) 
-00012a90: 2f20 7365 6c66 2e73 616d 706c 655f 7369  / self.sample_si
-00012aa0: 7a65 290a 2020 2020 2020 2020 2320 7072  ze).        # pr
-00012ab0: 6f62 6162 696c 6974 7920 6f66 2062 6f74  obability of bot
-00012ac0: 6820 7072 6564 6963 7465 6420 616e 6420  h predicted and 
-00012ad0: 6163 7475 616c 2062 6569 6e67 2070 6f73  actual being pos
-00012ae0: 6974 6976 650a 2020 2020 2020 2020 705f  itive.        p_
-00012af0: 706f 7369 7469 7665 5f70 7265 6469 6374  positive_predict
-00012b00: 696f 6e5f 616e 645f 6163 7475 616c 203d  ion_and_actual =
-00012b10: 205c 0a20 2020 2020 2020 2020 2020 2073   \.            s
-00012b20: 656c 662e 7072 6576 616c 656e 6365 202a  elf.prevalence *
-00012b30: 2028 2873 656c 662e 5f66 616c 7365 5f70   ((self._false_p
-00012b40: 6f73 6974 6976 6573 202b 2073 656c 662e  ositives + self.
-00012b50: 5f74 7275 655f 706f 7369 7469 7665 7329  _true_positives)
-00012b60: 202f 2073 656c 662e 7361 6d70 6c65 5f73   / self.sample_s
-00012b70: 697a 6529 0a20 2020 2020 2020 2023 2070  ize).        # p
-00012b80: 726f 6261 6269 6c69 7479 2074 6861 7420  robability that 
-00012b90: 6368 616e 6365 2061 6c6f 6e65 2077 6f75  chance alone wou
-00012ba0: 6c64 206c 6561 6420 7468 6520 7072 6564  ld lead the pred
-00012bb0: 6963 7465 6420 616e 6420 6163 7475 616c  icted and actual
-00012bc0: 2076 616c 7565 7320 746f 206d 6174 6368   values to match
-00012bd0: 2c20 756e 6465 7220 7468 650a 2020 2020  , under the.    
-00012be0: 2020 2020 2320 6173 7375 6d70 7469 6f6e      # assumption
-00012bf0: 2074 6861 7420 626f 7468 2061 7265 2073   that both are s
-00012c00: 656c 6563 7465 6420 7261 6e64 6f6d 6c79  elected randomly
-00012c10: 2028 692e 652e 2069 6d70 6c69 6573 2069   (i.e. implies i
-00012c20: 6e64 6570 656e 6465 6e63 6529 2061 6363  ndependence) acc
-00012c30: 6f72 6469 6e67 2074 6f20 7468 6520 6f62  ording to the ob
-00012c40: 7365 7276 6564 0a20 2020 2020 2020 2023  served.        #
-00012c50: 2070 726f 706f 7274 696f 6e73 2028 7072   proportions (pr
-00012c60: 6f62 6162 696c 6974 7920 6f66 2069 6e64  obability of ind
-00012c70: 6570 656e 6465 6e74 2065 7665 6e74 7320  ependent events 
-00012c80: 3d20 5028 4120 2620 4229 203d 3d20 5028  = P(A & B) == P(
-00012c90: 4129 202a 2050 2842 290a 2020 2020 2020  A) * P(B).      
-00012ca0: 2020 7072 5f65 203d 2070 5f6e 6567 6174    pr_e = p_negat
-00012cb0: 6976 655f 7072 6564 6963 7469 6f6e 5f61  ive_prediction_a
-00012cc0: 6e64 5f61 6374 7561 6c20 2b20 705f 706f  nd_actual + p_po
-00012cd0: 7369 7469 7665 5f70 7265 6469 6374 696f  sitive_predictio
-00012ce0: 6e5f 616e 645f 6163 7475 616c 0a20 2020  n_and_actual.   
-00012cf0: 2020 2020 2072 6574 7572 6e20 2870 725f       return (pr_
-00012d00: 6120 2d20 7072 5f65 2920 2f20 2831 202d  a - pr_e) / (1 -
-00012d10: 2070 725f 6529 0a0a 2020 2020 4070 726f   pr_e)..    @pro
-00012d20: 7065 7274 790a 2020 2020 6465 6620 6631  perty.    def f1
-00012d30: 5f73 636f 7265 2873 656c 6629 202d 3e20  _score(self) -> 
-00012d40: 666c 6f61 743a 0a20 2020 2020 2020 2022  float:.        "
-00012d50: 2222 4631 2053 636f 7265 0a20 2020 2020  ""F1 Score.     
-00012d60: 2020 2068 7474 7073 3a2f 2f65 6e2e 7769     https://en.wi
-00012d70: 6b69 7065 6469 612e 6f72 672f 7769 6b69  kipedia.org/wiki
-00012d80: 2f46 2d73 636f 7265 0a20 2020 2020 2020  /F-score.       
-00012d90: 2022 2222 0a20 2020 2020 2020 2072 6574   """.        ret
-00012da0: 7572 6e20 7365 6c66 2e66 6265 7461 5f73  urn self.fbeta_s
-00012db0: 636f 7265 2862 6574 613d 3129 0a0a 2020  core(beta=1)..  
-00012dc0: 2020 6465 6620 6662 6574 615f 7363 6f72    def fbeta_scor
-00012dd0: 6528 7365 6c66 2c20 6265 7461 3a20 666c  e(self, beta: fl
-00012de0: 6f61 7429 202d 3e20 666c 6f61 743a 0a20  oat) -> float:. 
-00012df0: 2020 2020 2020 2022 2222 0a20 2020 2020         """.     
-00012e00: 2020 203a 7061 7261 6d20 6265 7461 3a20     :param beta: 
-00012e10: 5468 6520 6062 6574 6160 2070 6172 616d  The `beta` param
-00012e20: 6574 6572 2064 6574 6572 6d69 6e65 7320  eter determines 
-00012e30: 7468 6520 7765 6967 6874 206f 6620 7072  the weight of pr
-00012e40: 6563 6973 696f 6e20 696e 2074 6865 2063  ecision in the c
-00012e50: 6f6d 6269 6e65 6420 7363 6f72 652e 0a20  ombined score.. 
-00012e60: 2020 2020 2020 2020 2020 2060 6265 7461             `beta
-00012e70: 203c 2031 6020 6c65 6e64 7320 6d6f 7265   < 1` lends more
-00012e80: 2077 6569 6768 7420 746f 2070 7265 6369   weight to preci
-00012e90: 7369 6f6e 2028 692e 652e 2070 6f73 6974  sion (i.e. posit
-00012ea0: 6976 6520 7072 6564 6963 7469 7665 2076  ive predictive v
-00012eb0: 616c 7565 292c 2077 6869 6c65 0a20 2020  alue), while.   
-00012ec0: 2020 2020 2020 2020 2060 6265 7461 203e           `beta >
-00012ed0: 2031 6020 6661 766f 7273 2072 6563 616c   1` favors recal
-00012ee0: 6c20 2869 2e65 2e20 7472 7565 2070 6f73  l (i.e. true pos
-00012ef0: 6974 6976 6520 7261 7465 290a 2020 2020  itive rate).    
-00012f00: 2020 2020 2020 2020 2860 6265 7461 202d          (`beta -
-00012f10: 3e20 3060 2063 6f6e 7369 6465 7273 206f  > 0` considers o
-00012f20: 6e6c 7920 7072 6563 6973 696f 6e2c 2060  nly precision, `
-00012f30: 6265 7461 202d 3e20 696e 6660 206f 6e6c  beta -> inf` onl
-00012f40: 7920 7265 6361 6c6c 292e 0a20 2020 2020  y recall)..     
-00012f50: 2020 2020 2020 2068 7474 703a 2f2f 7363         http://sc
-00012f60: 696b 6974 2d6c 6561 726e 2e6f 7267 2f73  ikit-learn.org/s
-00012f70: 7461 626c 652f 6d6f 6475 6c65 732f 6765  table/modules/ge
-00012f80: 6e65 7261 7465 642f 736b 6c65 6172 6e2e  nerated/sklearn.
-00012f90: 6d65 7472 6963 732e 6662 6574 615f 7363  metrics.fbeta_sc
-00012fa0: 6f72 652e 6874 6d6c 0a20 2020 2020 2020  ore.html.       
-00012fb0: 203a 7265 7475 726e 3a0a 2020 2020 2020   :return:.      
-00012fc0: 2020 2222 220a 2020 2020 2020 2020 6966    """.        if
-00012fd0: 2073 656c 662e 706f 7369 7469 7665 5f70   self.positive_p
-00012fe0: 7265 6469 6374 6976 655f 7661 6c75 6520  redictive_value 
-00012ff0: 6973 204e 6f6e 6520 6f72 2073 656c 662e  is None or self.
-00013000: 7365 6e73 6974 6976 6974 7920 6973 204e  sensitivity is N
-00013010: 6f6e 6520 6f72 205c 0a20 2020 2020 2020  one or \.       
-00013020: 2020 2020 2020 2020 2028 7365 6c66 2e70           (self.p
-00013030: 6f73 6974 6976 655f 7072 6564 6963 7469  ositive_predicti
-00013040: 7665 5f76 616c 7565 202b 2073 656c 662e  ve_value + self.
-00013050: 7365 6e73 6974 6976 6974 7929 203d 3d20  sensitivity) == 
-00013060: 303a 0a20 2020 2020 2020 2020 2020 2072  0:.            r
-00013070: 6574 7572 6e20 300a 0a20 2020 2020 2020  eturn 0..       
-00013080: 2072 6574 7572 6e20 2831 202b 2028 6265   return (1 + (be
-00013090: 7461 202a 2a20 3229 2920 2a20 2873 656c  ta ** 2)) * (sel
-000130a0: 662e 706f 7369 7469 7665 5f70 7265 6469  f.positive_predi
-000130b0: 6374 6976 655f 7661 6c75 6520 2a20 7365  ctive_value * se
-000130c0: 6c66 2e73 656e 7369 7469 7669 7479 2920  lf.sensitivity) 
-000130d0: 2f20 5c0a 2020 2020 2020 2020 2020 2020  / \.            
-000130e0: 2020 2028 2828 6265 7461 202a 2a20 3229     (((beta ** 2)
-000130f0: 202a 2073 656c 662e 706f 7369 7469 7665   * self.positive
-00013100: 5f70 7265 6469 6374 6976 655f 7661 6c75  _predictive_valu
-00013110: 6529 202b 2073 656c 662e 7365 6e73 6974  e) + self.sensit
-00013120: 6976 6974 7929 0a0a 2020 2020 4070 726f  ivity)..    @pro
-00013130: 7065 7274 790a 2020 2020 6465 6620 7365  perty.    def se
-00013140: 6e73 6974 6976 6974 7928 7365 6c66 2920  nsitivity(self) 
-00013150: 2d3e 2066 6c6f 6174 3a0a 2020 2020 2020  -> float:.      
-00013160: 2020 2222 2253 656e 7369 7469 7669 7479    """Sensitivity
-00013170: 2069 2e65 2e20 5472 7565 2050 6f73 6974   i.e. True Posit
-00013180: 6976 6520 5261 7465 2222 220a 2020 2020  ive Rate""".    
-00013190: 2020 2020 7265 7475 726e 2073 656c 662e      return self.
-000131a0: 7472 7565 5f70 6f73 6974 6976 655f 7261  true_positive_ra
-000131b0: 7465 0a0a 2020 2020 4070 726f 7065 7274  te..    @propert
-000131c0: 790a 2020 2020 6465 6620 7370 6563 6966  y.    def specif
-000131d0: 6963 6974 7928 7365 6c66 2920 2d3e 2066  icity(self) -> f
-000131e0: 6c6f 6174 3a0a 2020 2020 2020 2020 2222  loat:.        ""
-000131f0: 2253 7065 6369 6669 6369 7479 2069 2e65  "Specificity i.e
-00013200: 2e20 5472 7565 204e 6567 6174 6976 6520  . True Negative 
-00013210: 5261 7465 2222 220a 2020 2020 2020 2020  Rate""".        
-00013220: 7265 7475 726e 2073 656c 662e 7472 7565  return self.true
-00013230: 5f6e 6567 6174 6976 655f 7261 7465 0a0a  _negative_rate..
-00013240: 2020 2020 4070 726f 7065 7274 790a 2020      @property.  
-00013250: 2020 6465 6620 7072 6563 6973 696f 6e28    def precision(
-00013260: 7365 6c66 2920 2d3e 2066 6c6f 6174 3a0a  self) -> float:.
-00013270: 2020 2020 2020 2020 2222 2250 7265 6369          """Preci
-00013280: 7369 6f6e 2069 2e65 2e20 506f 7369 7469  sion i.e. Positi
-00013290: 7665 2050 7265 6469 6374 6976 6520 5661  ve Predictive Va
-000132a0: 6c75 6522 2222 0a20 2020 2020 2020 2072  lue""".        r
-000132b0: 6574 7572 6e20 7365 6c66 2e70 6f73 6974  eturn self.posit
-000132c0: 6976 655f 7072 6564 6963 7469 7665 5f76  ive_predictive_v
-000132d0: 616c 7565 0a0a 2020 2020 4070 726f 7065  alue..    @prope
-000132e0: 7274 790a 2020 2020 6465 6620 7265 6361  rty.    def reca
-000132f0: 6c6c 2873 656c 6629 3a0a 2020 2020 2020  ll(self):.      
-00013300: 2020 2222 2252 6563 616c 6c20 692e 652e    """Recall i.e.
-00013310: 2054 7275 6520 506f 7369 7469 7665 2052   True Positive R
-00013320: 6174 6522 2222 0a20 2020 2020 2020 2072  ate""".        r
-00013330: 6574 7572 6e20 7365 6c66 2e74 7275 655f  eturn self.true_
-00013340: 706f 7369 7469 7665 5f72 6174 650a 0a20  positive_rate.. 
-00013350: 2020 2040 7072 6f70 6572 7479 0a20 2020     @property.   
-00013360: 2064 6566 2061 6c6c 5f6d 6574 7269 6373   def all_metrics
-00013370: 2873 656c 6629 202d 3e20 6469 6374 3a0a  (self) -> dict:.
-00013380: 2020 2020 2020 2020 2222 2241 6c6c 206f          """All o
-00013390: 6620 7468 6520 6d65 7472 6963 7320 6172  f the metrics ar
-000133a0: 6520 7265 7475 726e 6564 2061 7320 6120  e returned as a 
-000133b0: 6469 6374 696f 6e61 7279 2e22 2222 0a20  dictionary.""". 
-000133c0: 2020 2020 2020 2061 7563 5f6d 6573 7361         auc_messa
-000133d0: 6765 203d 2027 4172 6561 2075 6e64 6572  ge = 'Area under
-000133e0: 2074 6865 2052 4f43 2063 7572 7665 2028   the ROC curve (
-000133f0: 7472 7565 2070 6f73 2e20 7261 7465 2076  true pos. rate v
-00013400: 7320 6661 6c73 6520 706f 732e 2072 6174  s false pos. rat
-00013410: 6529 3b20 2720 5c0a 2020 2020 2020 2020  e); ' \.        
-00013420: 2020 2020 2020 2020 2020 2020 2020 2772                'r
-00013430: 616e 6765 7320 6672 6f6d 2030 2e35 2028  anges from 0.5 (
-00013440: 7075 7265 6c79 2072 616e 646f 6d20 636c  purely random cl
-00013450: 6173 7369 6669 6572 2920 746f 2031 2e30  assifier) to 1.0
-00013460: 2028 7065 7266 6563 7420 636c 6173 7369   (perfect classi
-00013470: 6669 6572 2927 0a0a 2020 2020 2020 2020  fier)'..        
-00013480: 7470 725f 6d65 7373 6167 6520 3d20 6627  tpr_message = f'
-00013490: 7b73 656c 662e 7472 7565 5f70 6f73 6974  {self.true_posit
-000134a0: 6976 655f 7261 7465 3a2e 3125 7d20 6f66  ive_rate:.1%} of
-000134b0: 2070 6f73 6974 6976 6520 696e 7374 616e   positive instan
-000134c0: 6365 7320 7765 7265 2063 6f72 7265 6374  ces were correct
-000134d0: 6c79 2069 6465 6e74 6966 6965 642e 3b20  ly identified.; 
-000134e0: 2720 5c0a 2020 2020 2020 2020 2020 2020  ' \.            
-000134f0: 2020 2020 2020 2020 2020 6627 692e 652e            f'i.e.
-00013500: 207b 7365 6c66 2e5f 7472 7565 5f70 6f73   {self._true_pos
-00013510: 6974 6976 6573 7d20 227b 7365 6c66 2e5f  itives} "{self._
-00013520: 706f 7369 7469 7665 5f63 6c61 7373 7d22  positive_class}"
-00013530: 206c 6162 656c 7320 7765 7265 2063 6f72   labels were cor
-00013540: 7265 6374 6c79 2027 205c 0a20 2020 2020  rectly ' \.     
-00013550: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00013560: 2066 2769 6465 6e74 6966 6965 6420 6f75   f'identified ou
-00013570: 7420 6f66 207b 7365 6c66 2e5f 6163 7475  t of {self._actu
-00013580: 616c 5f70 6f73 6974 6976 6573 7d20 696e  al_positives} in
-00013590: 7374 616e 6365 733b 2061 2e6b 2e61 2053  stances; a.k.a S
-000135a0: 656e 7369 7469 7669 7479 2f52 6563 616c  ensitivity/Recal
-000135b0: 6c27 0a0a 2020 2020 2020 2020 746e 725f  l'..        tnr_
-000135c0: 6d65 7373 6167 6520 3d20 6627 7b73 656c  message = f'{sel
-000135d0: 662e 7472 7565 5f6e 6567 6174 6976 655f  f.true_negative_
-000135e0: 7261 7465 3a2e 3125 7d20 6f66 206e 6567  rate:.1%} of neg
-000135f0: 6174 6976 6520 696e 7374 616e 6365 7320  ative instances 
-00013600: 7765 7265 2063 6f72 7265 6374 6c79 2069  were correctly i
-00013610: 6465 6e74 6966 6965 642e 3b20 2720 5c0a  dentified.; ' \.
+00010a70: 2020 2020 2020 2020 2020 2020 2077 6964               wid
+00010a80: 7468 3a20 666c 6f61 7420 3d20 3630 3020  th: float = 600 
+00010a90: 2a20 474f 4c44 454e 5f52 4154 494f 2920  * GOLDEN_RATIO) 
+00010aa0: 2d3e 2070 6c6f 746c 792e 6772 6170 685f  -> plotly.graph_
+00010ab0: 6f62 6a65 6374 732e 4669 6775 7265 3a0a  objects.Figure:.
+00010ac0: 2020 2020 2020 2020 2222 220a 2020 2020          """.    
+00010ad0: 2020 2020 5265 7475 726e 7320 6120 506c      Returns a Pl
+00010ae0: 6f74 6c79 2046 6967 7572 6520 2873 6361  otly Figure (sca
+00010af0: 7474 6572 2d70 6c6f 7429 2062 6574 7765  tter-plot) betwe
+00010b00: 656e 2074 776f 2068 7970 6572 2d70 6172  en two hyper-par
+00010b10: 616d 6574 6572 732e 0a0a 2020 2020 2020  ameters...      
+00010b20: 2020 4172 6773 3a0a 2020 2020 2020 2020    Args:.        
+00010b30: 2020 2020 7061 7261 6d65 7465 725f 783a      parameter_x:
+00010b40: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00010b50: 2054 6865 206e 616d 6520 6f66 2061 2068   The name of a h
+00010b60: 7970 6572 2d70 6172 616d 6574 6572 2074  yper-parameter t
+00010b70: 6f20 706c 6f74 2061 6761 696e 7374 2061  o plot against a
+00010b80: 6e6f 7468 6572 2070 6172 616d 6574 6572  nother parameter
+00010b90: 2c20 6f6e 2074 6865 2078 2d61 7869 732e  , on the x-axis.
+00010ba0: 0a20 2020 2020 2020 2020 2020 2070 6172  .            par
+00010bb0: 616d 6574 6572 5f79 3a0a 2020 2020 2020  ameter_y:.      
+00010bc0: 2020 2020 2020 2020 2020 5468 6520 6e61            The na
+00010bd0: 6d65 206f 6620 6120 6879 7065 722d 7061  me of a hyper-pa
+00010be0: 7261 6d65 7465 7220 746f 2070 6c6f 7420  rameter to plot 
+00010bf0: 6167 6169 6e73 7420 616e 6f74 6865 7220  against another 
+00010c00: 7061 7261 6d65 7465 722c 206f 6e20 7468  parameter, on th
+00010c10: 6520 792d 6178 6973 2e0a 2020 2020 2020  e y-axis..      
+00010c20: 2020 2020 2020 7175 6572 793a 0a20 2020        query:.   
+00010c30: 2020 2020 2020 2020 2020 2020 2073 7472               str
+00010c40: 696e 6720 746f 2062 6520 7061 7373 6564  ing to be passed
+00010c50: 2074 6f20 6074 6f5f 6461 7461 6672 616d   to `to_datafram
+00010c60: 6528 2960 3b20 7365 6520 646f 6375 6d65  e()`; see docume
+00010c70: 6e74 6174 696f 6e20 666f 7220 7468 6174  ntation for that
+00010c80: 206d 6574 686f 642e 0a20 2020 2020 2020   method..       
+00010c90: 2020 2020 2073 697a 653a 0a20 2020 2020       size:.     
+00010ca0: 2020 2020 2020 2020 2020 2054 6865 206e             The n
+00010cb0: 616d 6520 6f66 2061 2068 7970 6572 2d70  ame of a hyper-p
+00010cc0: 6172 616d 6574 6572 2c20 7468 6520 7661  arameter, the va
+00010cd0: 6c75 6573 206f 6620 7768 6963 6820 7769  lues of which wi
+00010ce0: 6c6c 2062 6520 7573 6564 2074 6f20 6465  ll be used to de
+00010cf0: 7465 726d 696e 6520 7468 6520 7369 7a65  termine the size
+00010d00: 206f 6620 7468 650a 2020 2020 2020 2020   of the.        
+00010d10: 2020 2020 2020 2020 636f 7272 6573 706f          correspo
+00010d20: 6e64 696e 6720 706f 696e 7473 2069 6e20  nding points in 
+00010d30: 7468 6520 706c 6f74 2e20 5468 6973 2076  the plot. This v
+00010d40: 616c 7565 2069 7320 7061 7373 6564 2074  alue is passed t
+00010d50: 6f20 706c 6f74 6c79 2e0a 2020 2020 2020  o plotly..      
+00010d60: 2020 2020 2020 6865 6967 6874 3a0a 2020        height:.  
+00010d70: 2020 2020 2020 2020 2020 2020 2020 5468                Th
+00010d80: 6520 6865 6967 6874 206f 6620 7468 6520  e height of the 
+00010d90: 706c 6f74 2e20 5468 6973 2076 616c 7565  plot. This value
+00010da0: 2069 7320 7061 7373 6564 2074 6f20 706c   is passed to pl
+00010db0: 6f74 6c79 2e0a 2020 2020 2020 2020 2020  otly..          
+00010dc0: 2020 7769 6474 683a 0a20 2020 2020 2020    width:.       
+00010dd0: 2020 2020 2020 2020 2054 6865 2077 6964           The wid
+00010de0: 7468 206f 6620 7468 6520 706c 6f74 2e20  th of the plot. 
+00010df0: 5468 6973 2076 616c 7565 2069 7320 7061  This value is pa
+00010e00: 7373 6564 2074 6f20 706c 6f74 6c79 2e0a  ssed to plotly..
+00010e10: 2020 2020 2020 2020 2222 220a 2020 2020          """.    
+00010e20: 2020 2020 636f 6c6f 725f 636f 6e74 696e      color_contin
+00010e30: 756f 7573 5f73 6361 6c65 203d 2070 782e  uous_scale = px.
+00010e40: 636f 6c6f 7273 2e64 6976 6572 6769 6e67  colors.diverging
+00010e50: 2e52 6459 6c47 6e0a 2020 2020 2020 2020  .RdYlGn.        
+00010e60: 6966 206e 6f74 2073 656c 662e 6869 6768  if not self.high
+00010e70: 6572 5f73 636f 7265 5f69 735f 6265 7474  er_score_is_bett
+00010e80: 6572 3a0a 2020 2020 2020 2020 2020 2020  er:.            
+00010e90: 636f 6c6f 725f 636f 6e74 696e 756f 7573  color_continuous
+00010ea0: 5f73 6361 6c65 203d 2063 6f6c 6f72 5f63  _scale = color_c
+00010eb0: 6f6e 7469 6e75 6f75 735f 7363 616c 652e  ontinuous_scale.
+00010ec0: 7265 7665 7273 6528 290a 0a20 2020 2020  reverse()..     
+00010ed0: 2020 2070 7269 6d61 7279 5f73 636f 7265     primary_score
+00010ee0: 5f63 6f6c 756d 6e20 3d20 7365 6c66 2e70  _column = self.p
+00010ef0: 7269 6d61 7279 5f73 636f 7265 5f6e 616d  rimary_score_nam
+00010f00: 6520 2b20 2220 4d65 616e 220a 2020 2020  e + " Mean".    
+00010f10: 2020 2020 7469 746c 6520 3d20 6622 3c62      title = f"<b
+00010f20: 3e7b 7061 7261 6d65 7465 725f 797d 3c2f  >{parameter_y}</
+00010f30: 623e 2076 7320 3c62 3e7b 7061 7261 6d65  b> vs <b>{parame
+00010f40: 7465 725f 787d 3c2f 623e 220a 0a20 2020  ter_x}</b>"..   
+00010f50: 2020 2020 2073 6361 6c65 645f 7369 7a65       scaled_size
+00010f60: 203d 204e 6f6e 650a 2020 2020 2020 2020   = None.        
+00010f70: 6c61 6265 6c65 645f 6466 203d 2073 656c  labeled_df = sel
+00010f80: 662e 746f 5f6c 6162 656c 6564 5f64 6174  f.to_labeled_dat
+00010f90: 6166 7261 6d65 2871 7565 7279 3d71 7565  aframe(query=que
+00010fa0: 7279 290a 0a20 2020 2020 2020 2069 6620  ry)..        if 
+00010fb0: 7369 7a65 3a0a 2020 2020 2020 2020 2020  size:.          
+00010fc0: 2020 7469 746c 6520 3d20 7469 746c 6520    title = title 
+00010fd0: 2b20 6622 3c62 723e 3c73 7570 3e54 6865  + f"<br><sup>The
+00010fe0: 2073 697a 6520 6f66 2074 6865 2070 6f69   size of the poi
+00010ff0: 6e74 2063 6f72 7265 7370 6f6e 6473 2074  nt corresponds t
+00011000: 6f20 7468 6520 7661 6c75 6520 6f66 203c  o the value of <
+00011010: 623e 277b 7369 7a65 7d27 3c2f 623e 2e3c  b>'{size}'</b>.<
+00011020: 2f73 7570 3e22 0a20 2020 2020 2020 2020  /sup>".         
+00011030: 2020 2069 6620 7369 7a65 2069 6e20 7365     if size in se
+00011040: 6c66 2e6e 756d 6572 6963 5f70 6172 616d  lf.numeric_param
+00011050: 6574 6572 733a 0a20 2020 2020 2020 2020  eters:.         
+00011060: 2020 2020 2020 2023 206e 6565 6420 746f         # need to
+00011070: 2064 6f20 7468 6973 206f 7220 656c 7365   do this or else
+00011080: 2074 6865 2070 6f69 6e74 7320 6172 6520   the points are 
+00011090: 616c 6c20 7468 6520 7361 6d65 2073 697a  all the same siz
+000110a0: 650a 2020 2020 2020 2020 2020 2020 2020  e.              
+000110b0: 2020 2320 6275 7420 6f6e 6c79 2069 6620    # but only if 
+000110c0: 7369 7a65 2068 6173 206e 756d 6572 6963  size has numeric
+000110d0: 2076 616c 7565 730a 2020 2020 2020 2020   values.        
+000110e0: 2020 2020 2020 2020 7363 616c 6564 5f73          scaled_s
+000110f0: 697a 6520 3d20 4d69 6e4d 6178 5363 616c  ize = MinMaxScal
+00011100: 6572 2866 6561 7475 7265 5f72 616e 6765  er(feature_range
+00011110: 3d28 302e 312c 2030 2e39 2929 2e66 6974  =(0.1, 0.9)).fit
+00011120: 5f74 7261 6e73 666f 726d 286c 6162 656c  _transform(label
+00011130: 6564 5f64 665b 5b73 697a 655d 5d29 2e72  ed_df[[size]]).r
+00011140: 6573 6861 7065 2831 2c20 2d31 290a 2020  eshape(1, -1).  
+00011150: 2020 2020 2020 2020 2020 2020 2020 7363                sc
+00011160: 616c 6564 5f73 697a 6520 3d20 7363 616c  aled_size = scal
+00011170: 6564 5f73 697a 652e 746f 6c69 7374 2829  ed_size.tolist()
+00011180: 5b30 5d0a 0a20 2020 2020 2020 2066 6967  [0]..        fig
+00011190: 203d 2070 782e 7363 6174 7465 7228 0a20   = px.scatter(. 
+000111a0: 2020 2020 2020 2020 2020 2064 6174 615f             data_
+000111b0: 6672 616d 653d 6c61 6265 6c65 645f 6466  frame=labeled_df
+000111c0: 2c0a 2020 2020 2020 2020 2020 2020 783d  ,.            x=
+000111d0: 7061 7261 6d65 7465 725f 782c 0a20 2020  parameter_x,.   
+000111e0: 2020 2020 2020 2020 2079 3d70 6172 616d           y=param
+000111f0: 6574 6572 5f79 2c0a 2020 2020 2020 2020  eter_y,.        
+00011200: 2020 2020 7369 7a65 3d73 6361 6c65 645f      size=scaled_
+00011210: 7369 7a65 2c0a 2020 2020 2020 2020 2020  size,.          
+00011220: 2020 636f 6c6f 723d 7072 696d 6172 795f    color=primary_
+00011230: 7363 6f72 655f 636f 6c75 6d6e 2c0a 2020  score_column,.  
+00011240: 2020 2020 2020 2020 2020 636f 6c6f 725f            color_
+00011250: 636f 6e74 696e 756f 7573 5f73 6361 6c65  continuous_scale
+00011260: 3d63 6f6c 6f72 5f63 6f6e 7469 6e75 6f75  =color_continuou
+00011270: 735f 7363 616c 652c 0a20 2020 2020 2020  s_scale,.       
+00011280: 2020 2020 2074 7265 6e64 6c69 6e65 3d27       trendline='
+00011290: 6c6f 7765 7373 272c 0a20 2020 2020 2020  lowess',.       
+000112a0: 2020 2020 2074 6974 6c65 3d74 6974 6c65       title=title
+000112b0: 2c0a 2020 2020 2020 2020 2020 2020 6375  ,.            cu
+000112c0: 7374 6f6d 5f64 6174 613d 5b27 6c61 6265  stom_data=['labe
+000112d0: 6c27 2c20 7072 696d 6172 795f 7363 6f72  l', primary_scor
+000112e0: 655f 636f 6c75 6d6e 5d2c 0a20 2020 2020  e_column],.     
+000112f0: 2020 2020 2020 2068 6569 6768 743d 6865         height=he
+00011300: 6967 6874 2c0a 2020 2020 2020 2020 2020  ight,.          
+00011310: 2020 7769 6474 683d 7769 6474 682c 0a20    width=width,. 
+00011320: 2020 2020 2020 2029 0a20 2020 2020 2020         ).       
+00011330: 2066 6967 2e75 7064 6174 655f 7472 6163   fig.update_trac
+00011340: 6573 280a 2020 2020 2020 2020 2020 2020  es(.            
+00011350: 686f 7665 7274 656d 706c 6174 653d 223c  hovertemplate="<
+00011360: 6272 3e22 2e6a 6f69 6e28 5b0a 2020 2020  br>".join([.    
+00011370: 2020 2020 2020 2020 2020 2020 7061 7261              para
+00011380: 6d65 7465 725f 7820 2b20 223a 2025 7b78  meter_x + ": %{x
+00011390: 7d22 2c0a 2020 2020 2020 2020 2020 2020  }",.            
+000113a0: 2020 2020 7061 7261 6d65 7465 725f 7920      parameter_y 
+000113b0: 2b20 223a 2025 7b79 7d22 2c0a 2020 2020  + ": %{y}",.    
+000113c0: 2020 2020 2020 2020 2020 2020 7072 696d              prim
+000113d0: 6172 795f 7363 6f72 655f 636f 6c75 6d6e  ary_score_column
+000113e0: 202b 2022 3a20 2220 2b20 2225 7b63 7573   + ": " + "%{cus
+000113f0: 746f 6d64 6174 615b 315d 7d22 2c0a 2020  tomdata[1]}",.  
+00011400: 2020 2020 2020 2020 2020 2020 2020 223c                "<
+00011410: 6272 3e50 6172 616d 6574 6572 733a 2025  br>Parameters: %
+00011420: 7b63 7573 746f 6d64 6174 615b 305d 7d22  {customdata[0]}"
+00011430: 2c0a 2020 2020 2020 2020 2020 2020 5d29  ,.            ])
+00011440: 0a20 2020 2020 2020 2029 0a20 2020 2020  .        ).     
+00011450: 2020 2072 6574 7572 6e20 6669 670a 0a0a     return fig...
+00011460: 2320 7079 6c69 6e74 3a20 6469 7361 626c  # pylint: disabl
+00011470: 653d 746f 6f2d 6d61 6e79 2d69 6e73 7461  e=too-many-insta
+00011480: 6e63 652d 6174 7472 6962 7574 6573 0a23  nce-attributes.#
+00011490: 2070 796c 696e 743a 2064 6973 6162 6c65   pylint: disable
+000114a0: 3d74 6f6f 2d6d 616e 792d 7075 626c 6963  =too-many-public
+000114b0: 2d6d 6574 686f 6473 0a23 2070 796c 696e  -methods.# pylin
+000114c0: 743a 2064 6973 6162 6c65 3d74 6f6f 2d6d  t: disable=too-m
+000114d0: 616e 792d 696e 7374 616e 6365 2d61 7474  any-instance-att
+000114e0: 7269 6275 7465 732c 746f 6f2d 6d61 6e79  ributes,too-many
+000114f0: 2d70 7562 6c69 632d 6d65 7468 6f64 730a  -public-methods.
+00011500: 636c 6173 7320 5477 6f43 6c61 7373 4576  class TwoClassEv
+00011510: 616c 7561 746f 723a 0a20 2020 2022 2222  aluator:.    """
+00011520: 5468 6973 2063 6c61 7373 2063 616c 6375  This class calcu
+00011530: 6c61 7465 7320 7661 7269 6f75 7320 6d65  lates various me
+00011540: 7472 6963 7320 666f 7220 5477 6f20 436c  trics for Two Cl
+00011550: 6173 7320 2869 2e65 2e20 3027 732f 3127  ass (i.e. 0's/1'
+00011560: 7329 2070 7265 6469 6374 696f 6e20 7363  s) prediction sc
+00011570: 656e 6172 696f 732e 2222 220a 2020 2020  enarios.""".    
+00011580: 2320 7079 6c69 6e74 3a20 6469 7361 626c  # pylint: disabl
+00011590: 653d 746f 6f2d 6d61 6e79 2d61 7267 756d  e=too-many-argum
+000115a0: 656e 7473 0a20 2020 2064 6566 205f 5f69  ents.    def __i
+000115b0: 6e69 745f 5f28 7365 6c66 2c0a 2020 2020  nit__(self,.    
+000115c0: 2020 2020 2020 2020 2020 2020 2061 6374               act
+000115d0: 7561 6c5f 7661 6c75 6573 3a20 6e70 2e6e  ual_values: np.n
+000115e0: 6461 7272 6179 2c0a 2020 2020 2020 2020  darray,.        
+000115f0: 2020 2020 2020 2020 2070 7265 6469 6374           predict
+00011600: 6564 5f73 636f 7265 733a 206e 702e 6e64  ed_scores: np.nd
+00011610: 6172 7261 792c 0a20 2020 2020 2020 2020  array,.         
+00011620: 2020 2020 2020 2020 706f 7369 7469 7665          positive
+00011630: 5f63 6c61 7373 3a20 7374 7220 3d20 2750  _class: str = 'P
+00011640: 6f73 6974 6976 6520 436c 6173 7327 2c0a  ositive Class',.
+00011650: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00011660: 206e 6567 6174 6976 655f 636c 6173 733a   negative_class:
+00011670: 2073 7472 203d 2027 4e65 6761 7469 7665   str = 'Negative
+00011680: 2043 6c61 7373 272c 0a20 2020 2020 2020   Class',.       
+00011690: 2020 2020 2020 2020 2020 7363 6f72 655f            score_
+000116a0: 7468 7265 7368 6f6c 643a 2066 6c6f 6174  threshold: float
+000116b0: 203d 2030 2e35 0a20 2020 2020 2020 2020   = 0.5.         
+000116c0: 2020 2020 2020 2020 293a 0a20 2020 2020          ):.     
+000116d0: 2020 2022 2222 0a20 2020 2020 2020 2041     """.        A
+000116e0: 7267 733a 0a20 2020 2020 2020 2020 2020  rgs:.           
+000116f0: 2061 6374 7561 6c5f 7661 6c75 6573 3a0a   actual_values:.
+00011700: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00011710: 6172 7261 7920 6f66 2030 2773 2061 6e64  array of 0's and
+00011720: 2031 2773 0a20 2020 2020 2020 2020 2020   1's.           
+00011730: 2070 7265 6469 6374 6564 5f73 636f 7265   predicted_score
+00011740: 733a 0a20 2020 2020 2020 2020 2020 2020  s:.             
+00011750: 2020 2061 7272 6179 206f 6620 6465 6369     array of deci
+00011760: 6d61 6c2f 666c 6f61 7420 7661 6c75 6573  mal/float values
+00011770: 2066 726f 6d20 6070 7265 6469 6374 5f70   from `predict_p
+00011780: 726f 6261 2829 603b 204e 4f54 2074 6865  roba()`; NOT the
+00011790: 2061 6374 7561 6c20 636c 6173 730a 2020   actual class.  
+000117a0: 2020 2020 2020 2020 2020 706f 7369 7469            positi
+000117b0: 7665 5f63 6c61 7373 3a0a 2020 2020 2020  ve_class:.      
+000117c0: 2020 2020 2020 2020 2020 7374 7269 6e67            string
+000117d0: 206f 6620 7468 6520 6e61 6d65 2f6c 6162   of the name/lab
+000117e0: 656c 206f 6620 7468 6520 706f 7369 7469  el of the positi
+000117f0: 7665 2063 6c61 7373 2028 692e 652e 2076  ve class (i.e. v
+00011800: 616c 7565 206f 6620 3129 2e20 496e 206f  alue of 1). In o
+00011810: 7468 6572 2077 6f72 6473 2c20 6e6f 740a  ther words, not.
+00011820: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00011830: 2770 6f73 6974 6976 6527 2069 6e20 7468  'positive' in th
+00011840: 6520 7365 6e73 6520 6f66 2027 676f 6f64  e sense of 'good
+00011850: 2720 6275 7420 2770 6f73 6974 6976 6527  ' but 'positive'
+00011860: 2061 7320 696e 2027 5472 7565 2f46 616c   as in 'True/Fal
+00011870: 7365 2050 6f73 6974 6976 6527 2e0a 2020  se Positive'..  
+00011880: 2020 2020 2020 2020 2020 6e65 6761 7469            negati
+00011890: 7665 5f63 6c61 7373 3a0a 2020 2020 2020  ve_class:.      
+000118a0: 2020 2020 2020 2020 2020 7374 7269 6e67            string
+000118b0: 206f 6620 7468 6520 6e61 6d65 2f6c 6162   of the name/lab
+000118c0: 656c 206f 6620 7468 6520 6e65 6761 7469  el of the negati
+000118d0: 7665 2063 6c61 7373 2028 692e 652e 2076  ve class (i.e. v
+000118e0: 616c 7565 206f 6620 3029 2e20 496e 206f  alue of 0). In o
+000118f0: 7468 6572 2077 6f72 6473 2c20 6e6f 740a  ther words, not.
+00011900: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00011910: 276e 6567 6174 6976 6527 2069 6e20 7468  'negative' in th
+00011920: 6520 7365 6e73 6520 6f66 2027 676f 6f64  e sense of 'good
+00011930: 2720 6275 7420 276e 6567 6174 6976 6527  ' but 'negative'
+00011940: 2061 7320 696e 2027 5472 7565 2f46 616c   as in 'True/Fal
+00011950: 7365 204e 6567 6174 6976 6527 2e0a 2020  se Negative'..  
+00011960: 2020 2020 2020 2020 2020 7363 6f72 655f            score_
+00011970: 7468 7265 7368 6f6c 643a 0a20 2020 2020  threshold:.     
+00011980: 2020 2020 2020 2020 2020 2074 6865 2073             the s
+00011990: 636f 7265 2f70 726f 6261 6269 6c69 7479  core/probability
+000119a0: 2074 6872 6573 686f 6c64 2066 6f72 2074   threshold for t
+000119b0: 7572 6e69 6e67 2073 636f 7265 7320 696e  urning scores in
+000119c0: 746f 2030 2773 2061 6e64 2031 2773 2061  to 0's and 1's a
+000119d0: 6e64 2063 6f72 7265 7370 6f6e 6469 6e67  nd corresponding
+000119e0: 206c 6162 656c 730a 2020 2020 2020 2020   labels.        
+000119f0: 2222 220a 2020 2020 2020 2020 6173 7365  """.        asse
+00011a00: 7274 206c 656e 2861 6374 7561 6c5f 7661  rt len(actual_va
+00011a10: 6c75 6573 2920 3d3d 206c 656e 2870 7265  lues) == len(pre
+00011a20: 6469 6374 6564 5f73 636f 7265 7329 0a0a  dicted_scores)..
+00011a30: 2020 2020 2020 2020 6966 206e 6f74 2061          if not a
+00011a40: 6c6c 286e 702e 756e 6971 7565 2861 6374  ll(np.unique(act
+00011a50: 7561 6c5f 7661 6c75 6573 2920 3d3d 205b  ual_values) == [
+00011a60: 302c 2031 5d29 3a0a 2020 2020 2020 2020  0, 1]):.        
+00011a70: 2020 2020 6d65 7373 6167 6520 3d20 6622      message = f"
+00011a80: 5661 6c75 6573 206f 6620 6061 6374 7561  Values of `actua
+00011a90: 6c5f 7661 6c75 6573 6020 7368 6f75 6c64  l_values` should
+00011aa0: 2030 206f 7220 312e 2046 6f75 6e64 2060   0 or 1. Found `
+00011ab0: 7b6e 702e 756e 6971 7565 2861 6374 7561  {np.unique(actua
+00011ac0: 6c5f 7661 6c75 6573 297d 6022 0a20 2020  l_values)}`".   
+00011ad0: 2020 2020 2020 2020 2072 6169 7365 2048           raise H
+00011ae0: 656c 7073 6b50 6172 616d 5661 6c75 6545  elpskParamValueE
+00011af0: 7272 6f72 286d 6573 7361 6765 290a 0a20  rror(message).. 
+00011b00: 2020 2020 2020 2069 6620 6e6f 7420 616c         if not al
+00011b10: 6c28 6e70 2e6c 6f67 6963 616c 5f61 6e64  l(np.logical_and
+00011b20: 2870 7265 6469 6374 6564 5f73 636f 7265  (predicted_score
+00011b30: 7320 3e3d 2030 2c20 7072 6564 6963 7465  s >= 0, predicte
+00011b40: 645f 7363 6f72 6573 203c 3d20 3129 293a  d_scores <= 1)):
+00011b50: 0a20 2020 2020 2020 2020 2020 206d 6573  .            mes
+00011b60: 7361 6765 203d 2022 5661 6c75 6573 206f  sage = "Values o
+00011b70: 6620 6070 7265 6469 6374 6564 5f73 636f  f `predicted_sco
+00011b80: 7265 7360 2073 686f 756c 6420 6265 2062  res` should be b
+00011b90: 6574 7765 656e 2030 2061 6e64 2031 2e22  etween 0 and 1."
+00011ba0: 0a20 2020 2020 2020 2020 2020 2072 6169  .            rai
+00011bb0: 7365 2048 656c 7073 6b50 6172 616d 5661  se HelpskParamVa
+00011bc0: 6c75 6545 7272 6f72 286d 6573 7361 6765  lueError(message
+00011bd0: 290a 0a20 2020 2020 2020 2073 656c 662e  )..        self.
+00011be0: 5f70 6f73 6974 6976 655f 636c 6173 7320  _positive_class 
+00011bf0: 3d20 706f 7369 7469 7665 5f63 6c61 7373  = positive_class
+00011c00: 0a20 2020 2020 2020 2073 656c 662e 5f6e  .        self._n
+00011c10: 6567 6174 6976 655f 636c 6173 7320 3d20  egative_class = 
+00011c20: 6e65 6761 7469 7665 5f63 6c61 7373 0a20  negative_class. 
+00011c30: 2020 2020 2020 2073 656c 662e 5f61 6374         self._act
+00011c40: 7561 6c5f 7661 6c75 6573 203d 2061 6374  ual_values = act
+00011c50: 7561 6c5f 7661 6c75 6573 0a20 2020 2020  ual_values.     
+00011c60: 2020 2073 656c 662e 5f70 7265 6469 6374     self._predict
+00011c70: 6564 5f73 636f 7265 7320 3d20 7072 6564  ed_scores = pred
+00011c80: 6963 7465 645f 7363 6f72 6573 0a20 2020  icted_scores.   
+00011c90: 2020 2020 2073 656c 662e 7363 6f72 655f       self.score_
+00011ca0: 7468 7265 7368 6f6c 6420 3d20 7363 6f72  threshold = scor
+00011cb0: 655f 7468 7265 7368 6f6c 640a 2020 2020  e_threshold.    
+00011cc0: 2020 2020 7072 6564 6963 7465 645f 7661      predicted_va
+00011cd0: 6c75 6573 203d 206e 702e 7768 6572 6528  lues = np.where(
+00011ce0: 7072 6564 6963 7465 645f 7363 6f72 6573  predicted_scores
+00011cf0: 203e 2073 656c 662e 7363 6f72 655f 7468   > self.score_th
+00011d00: 7265 7368 6f6c 642c 2031 2c20 3029 0a20  reshold, 1, 0). 
+00011d10: 2020 2020 2020 2073 656c 662e 5f63 6f6e         self._con
+00011d20: 6675 7369 6f6e 5f6d 6174 7269 7820 3d20  fusion_matrix = 
+00011d30: 636f 6e66 7573 696f 6e5f 6d61 7472 6978  confusion_matrix
+00011d40: 2879 5f74 7275 653d 6163 7475 616c 5f76  (y_true=actual_v
+00011d50: 616c 7565 732c 2079 5f70 7265 643d 7072  alues, y_pred=pr
+00011d60: 6564 6963 7465 645f 7661 6c75 6573 290a  edicted_values).
+00011d70: 0a20 2020 2020 2020 2073 656c 662e 7361  .        self.sa
+00011d80: 6d70 6c65 5f73 697a 6520 3d20 6c65 6e28  mple_size = len(
+00011d90: 6163 7475 616c 5f76 616c 7565 7329 0a20  actual_values). 
+00011da0: 2020 2020 2020 2061 7373 6572 7420 7365         assert se
+00011db0: 6c66 2e73 616d 706c 655f 7369 7a65 203d  lf.sample_size =
+00011dc0: 3d20 7365 6c66 2e5f 636f 6e66 7573 696f  = self._confusio
+00011dd0: 6e5f 6d61 7472 6978 2e73 756d 2829 0a0a  n_matrix.sum()..
+00011de0: 2020 2020 2020 2020 7472 7565 5f6e 6567          true_neg
+00011df0: 6174 6976 6573 2c20 6661 6c73 655f 706f  atives, false_po
+00011e00: 7369 7469 7665 732c 2066 616c 7365 5f6e  sitives, false_n
+00011e10: 6567 6174 6976 6573 2c20 7472 7565 5f70  egatives, true_p
+00011e20: 6f73 6974 6976 6573 203d 2073 656c 662e  ositives = self.
+00011e30: 5f63 6f6e 6675 7369 6f6e 5f6d 6174 7269  _confusion_matri
+00011e40: 782e 7261 7665 6c28 290a 0a20 2020 2020  x.ravel()..     
+00011e50: 2020 2073 656c 662e 5f61 6374 7561 6c5f     self._actual_
+00011e60: 706f 7369 7469 7665 7320 3d20 7472 7565  positives = true
+00011e70: 5f70 6f73 6974 6976 6573 202b 2066 616c  _positives + fal
+00011e80: 7365 5f6e 6567 6174 6976 6573 0a20 2020  se_negatives.   
+00011e90: 2020 2020 2061 7373 6572 7420 7365 6c66       assert self
+00011ea0: 2e5f 6163 7475 616c 5f70 6f73 6974 6976  ._actual_positiv
+00011eb0: 6573 203d 3d20 7375 6d28 7365 6c66 2e5f  es == sum(self._
+00011ec0: 6163 7475 616c 5f76 616c 7565 7320 3d3d  actual_values ==
+00011ed0: 2031 290a 0a20 2020 2020 2020 2073 656c   1)..        sel
+00011ee0: 662e 5f61 6374 7561 6c5f 6e65 6761 7469  f._actual_negati
+00011ef0: 7665 7320 3d20 7472 7565 5f6e 6567 6174  ves = true_negat
+00011f00: 6976 6573 202b 2066 616c 7365 5f70 6f73  ives + false_pos
+00011f10: 6974 6976 6573 0a0a 2020 2020 2020 2020  itives..        
+00011f20: 7365 6c66 2e5f 7472 7565 5f6e 6567 6174  self._true_negat
+00011f30: 6976 6573 203d 2074 7275 655f 6e65 6761  ives = true_nega
+00011f40: 7469 7665 730a 2020 2020 2020 2020 7365  tives.        se
+00011f50: 6c66 2e5f 6661 6c73 655f 706f 7369 7469  lf._false_positi
+00011f60: 7665 7320 3d20 6661 6c73 655f 706f 7369  ves = false_posi
+00011f70: 7469 7665 730a 2020 2020 2020 2020 7365  tives.        se
+00011f80: 6c66 2e5f 6661 6c73 655f 6e65 6761 7469  lf._false_negati
+00011f90: 7665 7320 3d20 6661 6c73 655f 6e65 6761  ves = false_nega
+00011fa0: 7469 7665 730a 2020 2020 2020 2020 7365  tives.        se
+00011fb0: 6c66 2e5f 7472 7565 5f70 6f73 6974 6976  lf._true_positiv
+00011fc0: 6573 203d 2074 7275 655f 706f 7369 7469  es = true_positi
+00011fd0: 7665 730a 0a20 2020 2020 2020 2073 656c  ves..        sel
+00011fe0: 662e 6175 6320 3d20 726f 635f 6175 635f  f.auc = roc_auc_
+00011ff0: 7363 6f72 6528 795f 7472 7565 3d61 6374  score(y_true=act
+00012000: 7561 6c5f 7661 6c75 6573 2c20 795f 7363  ual_values, y_sc
+00012010: 6f72 653d 7072 6564 6963 7465 645f 7363  ore=predicted_sc
+00012020: 6f72 6573 290a 0a20 2020 2040 7072 6f70  ores)..    @prop
+00012030: 6572 7479 0a20 2020 2064 6566 2074 7275  erty.    def tru
+00012040: 655f 706f 7369 7469 7665 5f72 6174 6528  e_positive_rate(
+00012050: 7365 6c66 2920 2d3e 2066 6c6f 6174 3a0a  self) -> float:.
+00012060: 2020 2020 2020 2020 2222 2254 7275 6520          """True 
+00012070: 506f 7369 7469 7665 2052 6174 6522 2222  Positive Rate"""
+00012080: 0a20 2020 2020 2020 2072 6574 7572 6e20  .        return 
+00012090: 3020 6966 2073 656c 662e 5f61 6374 7561  0 if self._actua
+000120a0: 6c5f 706f 7369 7469 7665 7320 3d3d 2030  l_positives == 0
+000120b0: 2065 6c73 6520 7365 6c66 2e5f 7472 7565   else self._true
+000120c0: 5f70 6f73 6974 6976 6573 202f 2073 656c  _positives / sel
+000120d0: 662e 5f61 6374 7561 6c5f 706f 7369 7469  f._actual_positi
+000120e0: 7665 730a 0a20 2020 2040 7072 6f70 6572  ves..    @proper
+000120f0: 7479 0a20 2020 2064 6566 2074 7275 655f  ty.    def true_
+00012100: 6e65 6761 7469 7665 5f72 6174 6528 7365  negative_rate(se
+00012110: 6c66 2920 2d3e 2066 6c6f 6174 3a0a 2020  lf) -> float:.  
+00012120: 2020 2020 2020 2222 2254 7275 6520 4e65        """True Ne
+00012130: 6761 7469 7665 2052 6174 6520 692e 652e  gative Rate i.e.
+00012140: 2053 7065 6369 6669 6369 7479 2222 220a   Specificity""".
+00012150: 2020 2020 2020 2020 7265 7475 726e 2030          return 0
+00012160: 2069 6620 7365 6c66 2e5f 6163 7475 616c   if self._actual
+00012170: 5f6e 6567 6174 6976 6573 203d 3d20 3020  _negatives == 0 
+00012180: 656c 7365 2073 656c 662e 5f74 7275 655f  else self._true_
+00012190: 6e65 6761 7469 7665 7320 2f20 7365 6c66  negatives / self
+000121a0: 2e5f 6163 7475 616c 5f6e 6567 6174 6976  ._actual_negativ
+000121b0: 6573 0a0a 2020 2020 4070 726f 7065 7274  es..    @propert
+000121c0: 790a 2020 2020 6465 6620 6661 6c73 655f  y.    def false_
+000121d0: 6e65 6761 7469 7665 5f72 6174 6528 7365  negative_rate(se
+000121e0: 6c66 2920 2d3e 2066 6c6f 6174 3a0a 2020  lf) -> float:.  
+000121f0: 2020 2020 2020 2222 2246 616c 7365 204e        """False N
+00012200: 6567 6174 6976 6520 5261 7465 2222 220a  egative Rate""".
+00012210: 2020 2020 2020 2020 7265 7475 726e 2030          return 0
+00012220: 2069 6620 7365 6c66 2e5f 6163 7475 616c   if self._actual
+00012230: 5f70 6f73 6974 6976 6573 203d 3d20 3020  _positives == 0 
+00012240: 656c 7365 2073 656c 662e 5f66 616c 7365  else self._false
+00012250: 5f6e 6567 6174 6976 6573 202f 2073 656c  _negatives / sel
+00012260: 662e 5f61 6374 7561 6c5f 706f 7369 7469  f._actual_positi
+00012270: 7665 730a 0a20 2020 2040 7072 6f70 6572  ves..    @proper
+00012280: 7479 0a20 2020 2064 6566 2066 616c 7365  ty.    def false
+00012290: 5f70 6f73 6974 6976 655f 7261 7465 2873  _positive_rate(s
+000122a0: 656c 6629 202d 3e20 666c 6f61 743a 0a20  elf) -> float:. 
+000122b0: 2020 2020 2020 2022 2222 4661 6c73 6520         """False 
+000122c0: 506f 7369 7469 7665 2052 6174 6522 2222  Positive Rate"""
+000122d0: 0a20 2020 2020 2020 2072 6574 7572 6e20  .        return 
+000122e0: 3020 6966 2073 656c 662e 5f61 6374 7561  0 if self._actua
+000122f0: 6c5f 6e65 6761 7469 7665 7320 3d3d 2030  l_negatives == 0
+00012300: 2065 6c73 6520 7365 6c66 2e5f 6661 6c73   else self._fals
+00012310: 655f 706f 7369 7469 7665 7320 2f20 7365  e_positives / se
+00012320: 6c66 2e5f 6163 7475 616c 5f6e 6567 6174  lf._actual_negat
+00012330: 6976 6573 0a0a 2020 2020 4070 726f 7065  ives..    @prope
+00012340: 7274 790a 2020 2020 6465 6620 6163 6375  rty.    def accu
+00012350: 7261 6379 2873 656c 6629 202d 3e20 556e  racy(self) -> Un
+00012360: 696f 6e5b 666c 6f61 742c 204e 6f6e 655d  ion[float, None]
+00012370: 3a0a 2020 2020 2020 2020 2222 2261 6363  :.        """acc
+00012380: 7572 6163 7922 2222 0a20 2020 2020 2020  uracy""".       
+00012390: 2072 6574 7572 6e20 4e6f 6e65 2069 6620   return None if 
+000123a0: 7365 6c66 2e73 616d 706c 655f 7369 7a65  self.sample_size
+000123b0: 203d 3d20 3020 656c 7365 205c 0a20 2020   == 0 else \.   
+000123c0: 2020 2020 2020 2020 2028 7365 6c66 2e5f           (self._
+000123d0: 7472 7565 5f6e 6567 6174 6976 6573 202b  true_negatives +
+000123e0: 2073 656c 662e 5f74 7275 655f 706f 7369   self._true_posi
+000123f0: 7469 7665 7329 202f 2073 656c 662e 7361  tives) / self.sa
+00012400: 6d70 6c65 5f73 697a 650a 0a20 2020 2040  mple_size..    @
+00012410: 7072 6f70 6572 7479 0a20 2020 2064 6566  property.    def
+00012420: 2065 7272 6f72 5f72 6174 6528 7365 6c66   error_rate(self
+00012430: 2920 2d3e 2055 6e69 6f6e 5b66 6c6f 6174  ) -> Union[float
+00012440: 2c20 4e6f 6e65 5d3a 0a20 2020 2020 2020  , None]:.       
+00012450: 2022 2222 6572 726f 725f 7261 7465 2222   """error_rate""
+00012460: 220a 2020 2020 2020 2020 7265 7475 726e  ".        return
+00012470: 204e 6f6e 6520 6966 2073 656c 662e 7361   None if self.sa
+00012480: 6d70 6c65 5f73 697a 6520 3d3d 2030 2065  mple_size == 0 e
+00012490: 6c73 6520 5c0a 2020 2020 2020 2020 2020  lse \.          
+000124a0: 2020 2873 656c 662e 5f66 616c 7365 5f70    (self._false_p
+000124b0: 6f73 6974 6976 6573 202b 2073 656c 662e  ositives + self.
+000124c0: 5f66 616c 7365 5f6e 6567 6174 6976 6573  _false_negatives
+000124d0: 2920 2f20 7365 6c66 2e73 616d 706c 655f  ) / self.sample_
+000124e0: 7369 7a65 0a0a 2020 2020 4070 726f 7065  size..    @prope
+000124f0: 7274 790a 2020 2020 6465 6620 706f 7369  rty.    def posi
+00012500: 7469 7665 5f70 7265 6469 6374 6976 655f  tive_predictive_
+00012510: 7661 6c75 6528 7365 6c66 2920 2d3e 2066  value(self) -> f
+00012520: 6c6f 6174 3a0a 2020 2020 2020 2020 2222  loat:.        ""
+00012530: 2250 6f73 6974 6976 6520 5072 6564 6963  "Positive Predic
+00012540: 7469 7665 2056 616c 7565 2069 2e65 2e20  tive Value i.e. 
+00012550: 5072 6563 6973 696f 6e22 2222 0a20 2020  Precision""".   
+00012560: 2020 2020 2072 6574 7572 6e20 3020 6966       return 0 if
+00012570: 2028 7365 6c66 2e5f 7472 7565 5f70 6f73   (self._true_pos
+00012580: 6974 6976 6573 202b 2073 656c 662e 5f66  itives + self._f
+00012590: 616c 7365 5f70 6f73 6974 6976 6573 2920  alse_positives) 
+000125a0: 3d3d 2030 2065 6c73 6520 5c0a 2020 2020  == 0 else \.    
+000125b0: 2020 2020 2020 2020 7365 6c66 2e5f 7472          self._tr
+000125c0: 7565 5f70 6f73 6974 6976 6573 202f 2028  ue_positives / (
+000125d0: 7365 6c66 2e5f 7472 7565 5f70 6f73 6974  self._true_posit
+000125e0: 6976 6573 202b 2073 656c 662e 5f66 616c  ives + self._fal
+000125f0: 7365 5f70 6f73 6974 6976 6573 290a 0a20  se_positives).. 
+00012600: 2020 2040 7072 6f70 6572 7479 0a20 2020     @property.   
+00012610: 2064 6566 206e 6567 6174 6976 655f 7072   def negative_pr
+00012620: 6564 6963 7469 7665 5f76 616c 7565 2873  edictive_value(s
+00012630: 656c 6629 202d 3e20 666c 6f61 743a 0a20  elf) -> float:. 
+00012640: 2020 2020 2020 2022 2222 4e65 6761 7469         """Negati
+00012650: 7665 2050 7265 6469 6374 6976 6520 5661  ve Predictive Va
+00012660: 6c75 6522 2222 0a20 2020 2020 2020 2072  lue""".        r
+00012670: 6574 7572 6e20 3020 6966 2028 7365 6c66  eturn 0 if (self
+00012680: 2e5f 7472 7565 5f6e 6567 6174 6976 6573  ._true_negatives
+00012690: 202b 2073 656c 662e 5f66 616c 7365 5f6e   + self._false_n
+000126a0: 6567 6174 6976 6573 2920 3d3d 2030 2065  egatives) == 0 e
+000126b0: 6c73 6520 5c0a 2020 2020 2020 2020 2020  lse \.          
+000126c0: 2020 7365 6c66 2e5f 7472 7565 5f6e 6567    self._true_neg
+000126d0: 6174 6976 6573 202f 2028 7365 6c66 2e5f  atives / (self._
+000126e0: 7472 7565 5f6e 6567 6174 6976 6573 202b  true_negatives +
+000126f0: 2073 656c 662e 5f66 616c 7365 5f6e 6567   self._false_neg
+00012700: 6174 6976 6573 290a 0a20 2020 2040 7072  atives)..    @pr
+00012710: 6f70 6572 7479 0a20 2020 2064 6566 2070  operty.    def p
+00012720: 7265 7661 6c65 6e63 6528 7365 6c66 2920  revalence(self) 
+00012730: 2d3e 2055 6e69 6f6e 5b66 6c6f 6174 2c20  -> Union[float, 
+00012740: 4e6f 6e65 5d3a 0a20 2020 2020 2020 2022  None]:.        "
+00012750: 2222 5072 6576 616c 656e 6365 2222 220a  ""Prevalence""".
+00012760: 2020 2020 2020 2020 7265 7475 726e 204e          return N
+00012770: 6f6e 6520 6966 2073 656c 662e 7361 6d70  one if self.samp
+00012780: 6c65 5f73 697a 6520 3d3d 2030 2065 6c73  le_size == 0 els
+00012790: 6520 5c0a 2020 2020 2020 2020 2020 2020  e \.            
+000127a0: 7365 6c66 2e5f 6163 7475 616c 5f70 6f73  self._actual_pos
+000127b0: 6974 6976 6573 202f 2073 656c 662e 7361  itives / self.sa
+000127c0: 6d70 6c65 5f73 697a 650a 0a20 2020 2040  mple_size..    @
+000127d0: 7072 6f70 6572 7479 0a20 2020 2064 6566  property.    def
+000127e0: 206b 6170 7061 2873 656c 6629 202d 3e20   kappa(self) -> 
+000127f0: 556e 696f 6e5b 666c 6f61 742c 204e 6f6e  Union[float, Non
+00012800: 655d 3a0a 2020 2020 2020 2020 2222 224b  e]:.        """K
+00012810: 6170 7061 2222 220a 2020 2020 2020 2020  appa""".        
+00012820: 6966 2073 656c 662e 7361 6d70 6c65 5f73  if self.sample_s
+00012830: 697a 6520 3d3d 2030 206f 7220 5c0a 2020  ize == 0 or \.  
+00012840: 2020 2020 2020 2020 2020 2020 2020 2828                ((
+00012850: 7365 6c66 2e5f 7472 7565 5f6e 6567 6174  self._true_negat
+00012860: 6976 6573 202b 2073 656c 662e 5f66 616c  ives + self._fal
+00012870: 7365 5f6e 6567 6174 6976 6573 2920 2f20  se_negatives) / 
+00012880: 7365 6c66 2e73 616d 706c 655f 7369 7a65  self.sample_size
+00012890: 2920 3d3d 2030 3a0a 2020 2020 2020 2020  ) == 0:.        
+000128a0: 2020 2020 7265 7475 726e 204e 6f6e 650a      return None.
+000128b0: 2020 2020 2020 2020 2320 7072 6f70 6f72          # propor
+000128c0: 7469 6f6e 206f 6620 7468 6520 6163 7475  tion of the actu
+000128d0: 616c 2061 6772 6565 6d65 6e74 730a 2020  al agreements.  
+000128e0: 2020 2020 2020 2320 6164 6420 7468 6520        # add the 
+000128f0: 7072 6f70 6f72 7469 6f6e 206f 6620 616c  proportion of al
+00012900: 6c20 696e 7374 616e 6365 7320 7768 6572  l instances wher
+00012910: 6520 7468 6520 7072 6564 6963 7465 6420  e the predicted 
+00012920: 7479 7065 2061 6e64 2061 6374 7561 6c20  type and actual 
+00012930: 7479 7065 2061 6772 6565 0a20 2020 2020  type agree.     
+00012940: 2020 2070 725f 6120 3d20 2873 656c 662e     pr_a = (self.
+00012950: 5f74 7275 655f 6e65 6761 7469 7665 7320  _true_negatives 
+00012960: 2b20 7365 6c66 2e5f 7472 7565 5f70 6f73  + self._true_pos
+00012970: 6974 6976 6573 2920 2f20 7365 6c66 2e73  itives) / self.s
+00012980: 616d 706c 655f 7369 7a65 0a20 2020 2020  ample_size.     
+00012990: 2020 2023 2070 726f 6261 6269 6c69 7479     # probability
+000129a0: 206f 6620 626f 7468 2070 7265 6469 6374   of both predict
+000129b0: 6564 2061 6e64 2061 6374 7561 6c20 6265  ed and actual be
+000129c0: 696e 6720 6e65 6761 7469 7665 0a20 2020  ing negative.   
+000129d0: 2020 2020 2070 5f6e 6567 6174 6976 655f       p_negative_
+000129e0: 7072 6564 6963 7469 6f6e 5f61 6e64 5f61  prediction_and_a
+000129f0: 6374 7561 6c20 3d20 5c0a 2020 2020 2020  ctual = \.      
+00012a00: 2020 2020 2020 2828 7365 6c66 2e5f 7472        ((self._tr
+00012a10: 7565 5f6e 6567 6174 6976 6573 202b 2073  ue_negatives + s
+00012a20: 656c 662e 5f66 616c 7365 5f70 6f73 6974  elf._false_posit
+00012a30: 6976 6573 2920 2f20 7365 6c66 2e73 616d  ives) / self.sam
+00012a40: 706c 655f 7369 7a65 2920 2a20 5c0a 2020  ple_size) * \.  
+00012a50: 2020 2020 2020 2020 2020 2828 7365 6c66            ((self
+00012a60: 2e5f 7472 7565 5f6e 6567 6174 6976 6573  ._true_negatives
+00012a70: 202b 2073 656c 662e 5f66 616c 7365 5f6e   + self._false_n
+00012a80: 6567 6174 6976 6573 2920 2f20 7365 6c66  egatives) / self
+00012a90: 2e73 616d 706c 655f 7369 7a65 290a 2020  .sample_size).  
+00012aa0: 2020 2020 2020 2320 7072 6f62 6162 696c        # probabil
+00012ab0: 6974 7920 6f66 2062 6f74 6820 7072 6564  ity of both pred
+00012ac0: 6963 7465 6420 616e 6420 6163 7475 616c  icted and actual
+00012ad0: 2062 6569 6e67 2070 6f73 6974 6976 650a   being positive.
+00012ae0: 2020 2020 2020 2020 705f 706f 7369 7469          p_positi
+00012af0: 7665 5f70 7265 6469 6374 696f 6e5f 616e  ve_prediction_an
+00012b00: 645f 6163 7475 616c 203d 205c 0a20 2020  d_actual = \.   
+00012b10: 2020 2020 2020 2020 2073 656c 662e 7072           self.pr
+00012b20: 6576 616c 656e 6365 202a 2028 2873 656c  evalence * ((sel
+00012b30: 662e 5f66 616c 7365 5f70 6f73 6974 6976  f._false_positiv
+00012b40: 6573 202b 2073 656c 662e 5f74 7275 655f  es + self._true_
+00012b50: 706f 7369 7469 7665 7329 202f 2073 656c  positives) / sel
+00012b60: 662e 7361 6d70 6c65 5f73 697a 6529 0a20  f.sample_size). 
+00012b70: 2020 2020 2020 2023 2070 726f 6261 6269         # probabi
+00012b80: 6c69 7479 2074 6861 7420 6368 616e 6365  lity that chance
+00012b90: 2061 6c6f 6e65 2077 6f75 6c64 206c 6561   alone would lea
+00012ba0: 6420 7468 6520 7072 6564 6963 7465 6420  d the predicted 
+00012bb0: 616e 6420 6163 7475 616c 2076 616c 7565  and actual value
+00012bc0: 7320 746f 206d 6174 6368 2c20 756e 6465  s to match, unde
+00012bd0: 7220 7468 650a 2020 2020 2020 2020 2320  r the.        # 
+00012be0: 6173 7375 6d70 7469 6f6e 2074 6861 7420  assumption that 
+00012bf0: 626f 7468 2061 7265 2073 656c 6563 7465  both are selecte
+00012c00: 6420 7261 6e64 6f6d 6c79 2028 692e 652e  d randomly (i.e.
+00012c10: 2069 6d70 6c69 6573 2069 6e64 6570 656e   implies indepen
+00012c20: 6465 6e63 6529 2061 6363 6f72 6469 6e67  dence) according
+00012c30: 2074 6f20 7468 6520 6f62 7365 7276 6564   to the observed
+00012c40: 0a20 2020 2020 2020 2023 2070 726f 706f  .        # propo
+00012c50: 7274 696f 6e73 2028 7072 6f62 6162 696c  rtions (probabil
+00012c60: 6974 7920 6f66 2069 6e64 6570 656e 6465  ity of independe
+00012c70: 6e74 2065 7665 6e74 7320 3d20 5028 4120  nt events = P(A 
+00012c80: 2620 4229 203d 3d20 5028 4129 202a 2050  & B) == P(A) * P
+00012c90: 2842 290a 2020 2020 2020 2020 7072 5f65  (B).        pr_e
+00012ca0: 203d 2070 5f6e 6567 6174 6976 655f 7072   = p_negative_pr
+00012cb0: 6564 6963 7469 6f6e 5f61 6e64 5f61 6374  ediction_and_act
+00012cc0: 7561 6c20 2b20 705f 706f 7369 7469 7665  ual + p_positive
+00012cd0: 5f70 7265 6469 6374 696f 6e5f 616e 645f  _prediction_and_
+00012ce0: 6163 7475 616c 0a20 2020 2020 2020 2072  actual.        r
+00012cf0: 6574 7572 6e20 2870 725f 6120 2d20 7072  eturn (pr_a - pr
+00012d00: 5f65 2920 2f20 2831 202d 2070 725f 6529  _e) / (1 - pr_e)
+00012d10: 0a0a 2020 2020 4070 726f 7065 7274 790a  ..    @property.
+00012d20: 2020 2020 6465 6620 6631 5f73 636f 7265      def f1_score
+00012d30: 2873 656c 6629 202d 3e20 666c 6f61 743a  (self) -> float:
+00012d40: 0a20 2020 2020 2020 2022 2222 4631 2053  .        """F1 S
+00012d50: 636f 7265 0a20 2020 2020 2020 2068 7474  core.        htt
+00012d60: 7073 3a2f 2f65 6e2e 7769 6b69 7065 6469  ps://en.wikipedi
+00012d70: 612e 6f72 672f 7769 6b69 2f46 2d73 636f  a.org/wiki/F-sco
+00012d80: 7265 0a20 2020 2020 2020 2022 2222 0a20  re.        """. 
+00012d90: 2020 2020 2020 2072 6574 7572 6e20 7365         return se
+00012da0: 6c66 2e66 6265 7461 5f73 636f 7265 2862  lf.fbeta_score(b
+00012db0: 6574 613d 3129 0a0a 2020 2020 6465 6620  eta=1)..    def 
+00012dc0: 6662 6574 615f 7363 6f72 6528 7365 6c66  fbeta_score(self
+00012dd0: 2c20 6265 7461 3a20 666c 6f61 7429 202d  , beta: float) -
+00012de0: 3e20 666c 6f61 743a 0a20 2020 2020 2020  > float:.       
+00012df0: 2022 2222 0a20 2020 2020 2020 203a 7061   """.        :pa
+00012e00: 7261 6d20 6265 7461 3a20 5468 6520 6062  ram beta: The `b
+00012e10: 6574 6160 2070 6172 616d 6574 6572 2064  eta` parameter d
+00012e20: 6574 6572 6d69 6e65 7320 7468 6520 7765  etermines the we
+00012e30: 6967 6874 206f 6620 7072 6563 6973 696f  ight of precisio
+00012e40: 6e20 696e 2074 6865 2063 6f6d 6269 6e65  n in the combine
+00012e50: 6420 7363 6f72 652e 0a20 2020 2020 2020  d score..       
+00012e60: 2020 2020 2060 6265 7461 203c 2031 6020       `beta < 1` 
+00012e70: 6c65 6e64 7320 6d6f 7265 2077 6569 6768  lends more weigh
+00012e80: 7420 746f 2070 7265 6369 7369 6f6e 2028  t to precision (
+00012e90: 692e 652e 2070 6f73 6974 6976 6520 7072  i.e. positive pr
+00012ea0: 6564 6963 7469 7665 2076 616c 7565 292c  edictive value),
+00012eb0: 2077 6869 6c65 0a20 2020 2020 2020 2020   while.         
+00012ec0: 2020 2060 6265 7461 203e 2031 6020 6661     `beta > 1` fa
+00012ed0: 766f 7273 2072 6563 616c 6c20 2869 2e65  vors recall (i.e
+00012ee0: 2e20 7472 7565 2070 6f73 6974 6976 6520  . true positive 
+00012ef0: 7261 7465 290a 2020 2020 2020 2020 2020  rate).          
+00012f00: 2020 2860 6265 7461 202d 3e20 3060 2063    (`beta -> 0` c
+00012f10: 6f6e 7369 6465 7273 206f 6e6c 7920 7072  onsiders only pr
+00012f20: 6563 6973 696f 6e2c 2060 6265 7461 202d  ecision, `beta -
+00012f30: 3e20 696e 6660 206f 6e6c 7920 7265 6361  > inf` only reca
+00012f40: 6c6c 292e 0a20 2020 2020 2020 2020 2020  ll)..           
+00012f50: 2068 7474 703a 2f2f 7363 696b 6974 2d6c   http://scikit-l
+00012f60: 6561 726e 2e6f 7267 2f73 7461 626c 652f  earn.org/stable/
+00012f70: 6d6f 6475 6c65 732f 6765 6e65 7261 7465  modules/generate
+00012f80: 642f 736b 6c65 6172 6e2e 6d65 7472 6963  d/sklearn.metric
+00012f90: 732e 6662 6574 615f 7363 6f72 652e 6874  s.fbeta_score.ht
+00012fa0: 6d6c 0a20 2020 2020 2020 203a 7265 7475  ml.        :retu
+00012fb0: 726e 3a0a 2020 2020 2020 2020 2222 220a  rn:.        """.
+00012fc0: 2020 2020 2020 2020 6966 2073 656c 662e          if self.
+00012fd0: 706f 7369 7469 7665 5f70 7265 6469 6374  positive_predict
+00012fe0: 6976 655f 7661 6c75 6520 6973 204e 6f6e  ive_value is Non
+00012ff0: 6520 6f72 2073 656c 662e 7365 6e73 6974  e or self.sensit
+00013000: 6976 6974 7920 6973 204e 6f6e 6520 6f72  ivity is None or
+00013010: 205c 0a20 2020 2020 2020 2020 2020 2020   \.             
+00013020: 2020 2028 7365 6c66 2e70 6f73 6974 6976     (self.positiv
+00013030: 655f 7072 6564 6963 7469 7665 5f76 616c  e_predictive_val
+00013040: 7565 202b 2073 656c 662e 7365 6e73 6974  ue + self.sensit
+00013050: 6976 6974 7929 203d 3d20 303a 0a20 2020  ivity) == 0:.   
+00013060: 2020 2020 2020 2020 2072 6574 7572 6e20           return 
+00013070: 300a 0a20 2020 2020 2020 2072 6574 7572  0..        retur
+00013080: 6e20 2831 202b 2028 6265 7461 202a 2a20  n (1 + (beta ** 
+00013090: 3229 2920 2a20 2873 656c 662e 706f 7369  2)) * (self.posi
+000130a0: 7469 7665 5f70 7265 6469 6374 6976 655f  tive_predictive_
+000130b0: 7661 6c75 6520 2a20 7365 6c66 2e73 656e  value * self.sen
+000130c0: 7369 7469 7669 7479 2920 2f20 5c0a 2020  sitivity) / \.  
+000130d0: 2020 2020 2020 2020 2020 2020 2028 2828               (((
+000130e0: 6265 7461 202a 2a20 3229 202a 2073 656c  beta ** 2) * sel
+000130f0: 662e 706f 7369 7469 7665 5f70 7265 6469  f.positive_predi
+00013100: 6374 6976 655f 7661 6c75 6529 202b 2073  ctive_value) + s
+00013110: 656c 662e 7365 6e73 6974 6976 6974 7929  elf.sensitivity)
+00013120: 0a0a 2020 2020 4070 726f 7065 7274 790a  ..    @property.
+00013130: 2020 2020 6465 6620 7365 6e73 6974 6976      def sensitiv
+00013140: 6974 7928 7365 6c66 2920 2d3e 2066 6c6f  ity(self) -> flo
+00013150: 6174 3a0a 2020 2020 2020 2020 2222 2253  at:.        """S
+00013160: 656e 7369 7469 7669 7479 2069 2e65 2e20  ensitivity i.e. 
+00013170: 5472 7565 2050 6f73 6974 6976 6520 5261  True Positive Ra
+00013180: 7465 2222 220a 2020 2020 2020 2020 7265  te""".        re
+00013190: 7475 726e 2073 656c 662e 7472 7565 5f70  turn self.true_p
+000131a0: 6f73 6974 6976 655f 7261 7465 0a0a 2020  ositive_rate..  
+000131b0: 2020 4070 726f 7065 7274 790a 2020 2020    @property.    
+000131c0: 6465 6620 7370 6563 6966 6963 6974 7928  def specificity(
+000131d0: 7365 6c66 2920 2d3e 2066 6c6f 6174 3a0a  self) -> float:.
+000131e0: 2020 2020 2020 2020 2222 2253 7065 6369          """Speci
+000131f0: 6669 6369 7479 2069 2e65 2e20 5472 7565  ficity i.e. True
+00013200: 204e 6567 6174 6976 6520 5261 7465 2222   Negative Rate""
+00013210: 220a 2020 2020 2020 2020 7265 7475 726e  ".        return
+00013220: 2073 656c 662e 7472 7565 5f6e 6567 6174   self.true_negat
+00013230: 6976 655f 7261 7465 0a0a 2020 2020 4070  ive_rate..    @p
+00013240: 726f 7065 7274 790a 2020 2020 6465 6620  roperty.    def 
+00013250: 7072 6563 6973 696f 6e28 7365 6c66 2920  precision(self) 
+00013260: 2d3e 2066 6c6f 6174 3a0a 2020 2020 2020  -> float:.      
+00013270: 2020 2222 2250 7265 6369 7369 6f6e 2069    """Precision i
+00013280: 2e65 2e20 506f 7369 7469 7665 2050 7265  .e. Positive Pre
+00013290: 6469 6374 6976 6520 5661 6c75 6522 2222  dictive Value"""
+000132a0: 0a20 2020 2020 2020 2072 6574 7572 6e20  .        return 
+000132b0: 7365 6c66 2e70 6f73 6974 6976 655f 7072  self.positive_pr
+000132c0: 6564 6963 7469 7665 5f76 616c 7565 0a0a  edictive_value..
+000132d0: 2020 2020 4070 726f 7065 7274 790a 2020      @property.  
+000132e0: 2020 6465 6620 7265 6361 6c6c 2873 656c    def recall(sel
+000132f0: 6629 3a0a 2020 2020 2020 2020 2222 2252  f):.        """R
+00013300: 6563 616c 6c20 692e 652e 2054 7275 6520  ecall i.e. True 
+00013310: 506f 7369 7469 7665 2052 6174 6522 2222  Positive Rate"""
+00013320: 0a20 2020 2020 2020 2072 6574 7572 6e20  .        return 
+00013330: 7365 6c66 2e74 7275 655f 706f 7369 7469  self.true_positi
+00013340: 7665 5f72 6174 650a 0a20 2020 2040 7072  ve_rate..    @pr
+00013350: 6f70 6572 7479 0a20 2020 2064 6566 2061  operty.    def a
+00013360: 6c6c 5f6d 6574 7269 6373 2873 656c 6629  ll_metrics(self)
+00013370: 202d 3e20 6469 6374 3a0a 2020 2020 2020   -> dict:.      
+00013380: 2020 2222 2241 6c6c 206f 6620 7468 6520    """All of the 
+00013390: 6d65 7472 6963 7320 6172 6520 7265 7475  metrics are retu
+000133a0: 726e 6564 2061 7320 6120 6469 6374 696f  rned as a dictio
+000133b0: 6e61 7279 2e22 2222 0a20 2020 2020 2020  nary.""".       
+000133c0: 2061 7563 5f6d 6573 7361 6765 203d 2027   auc_message = '
+000133d0: 4172 6561 2075 6e64 6572 2074 6865 2052  Area under the R
+000133e0: 4f43 2063 7572 7665 2028 7472 7565 2070  OC curve (true p
+000133f0: 6f73 2e20 7261 7465 2076 7320 6661 6c73  os. rate vs fals
+00013400: 6520 706f 732e 2072 6174 6529 3b20 2720  e pos. rate); ' 
+00013410: 5c0a 2020 2020 2020 2020 2020 2020 2020  \.              
+00013420: 2020 2020 2020 2020 2772 616e 6765 7320          'ranges 
+00013430: 6672 6f6d 2030 2e35 2028 7075 7265 6c79  from 0.5 (purely
+00013440: 2072 616e 646f 6d20 636c 6173 7369 6669   random classifi
+00013450: 6572 2920 746f 2031 2e30 2028 7065 7266  er) to 1.0 (perf
+00013460: 6563 7420 636c 6173 7369 6669 6572 2927  ect classifier)'
+00013470: 0a0a 2020 2020 2020 2020 7470 725f 6d65  ..        tpr_me
+00013480: 7373 6167 6520 3d20 6627 7b73 656c 662e  ssage = f'{self.
+00013490: 7472 7565 5f70 6f73 6974 6976 655f 7261  true_positive_ra
+000134a0: 7465 3a2e 3125 7d20 6f66 2070 6f73 6974  te:.1%} of posit
+000134b0: 6976 6520 696e 7374 616e 6365 7320 7765  ive instances we
+000134c0: 7265 2063 6f72 7265 6374 6c79 2069 6465  re correctly ide
+000134d0: 6e74 6966 6965 642e 3b20 2720 5c0a 2020  ntified.; ' \.  
+000134e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000134f0: 2020 2020 6627 692e 652e 207b 7365 6c66      f'i.e. {self
+00013500: 2e5f 7472 7565 5f70 6f73 6974 6976 6573  ._true_positives
+00013510: 7d20 227b 7365 6c66 2e5f 706f 7369 7469  } "{self._positi
+00013520: 7665 5f63 6c61 7373 7d22 206c 6162 656c  ve_class}" label
+00013530: 7320 7765 7265 2063 6f72 7265 6374 6c79  s were correctly
+00013540: 2027 205c 0a20 2020 2020 2020 2020 2020   ' \.           
+00013550: 2020 2020 2020 2020 2020 2066 2769 6465             f'ide
+00013560: 6e74 6966 6965 6420 6f75 7420 6f66 207b  ntified out of {
+00013570: 7365 6c66 2e5f 6163 7475 616c 5f70 6f73  self._actual_pos
+00013580: 6974 6976 6573 7d20 696e 7374 616e 6365  itives} instance
+00013590: 733b 2061 2e6b 2e61 2053 656e 7369 7469  s; a.k.a Sensiti
+000135a0: 7669 7479 2f52 6563 616c 6c27 0a0a 2020  vity/Recall'..  
+000135b0: 2020 2020 2020 746e 725f 6d65 7373 6167        tnr_messag
+000135c0: 6520 3d20 6627 7b73 656c 662e 7472 7565  e = f'{self.true
+000135d0: 5f6e 6567 6174 6976 655f 7261 7465 3a2e  _negative_rate:.
+000135e0: 3125 7d20 6f66 206e 6567 6174 6976 6520  1%} of negative 
+000135f0: 696e 7374 616e 6365 7320 7765 7265 2063  instances were c
+00013600: 6f72 7265 6374 6c79 2069 6465 6e74 6966  orrectly identif
+00013610: 6965 642e 3b20 2720 5c0a 2020 2020 2020  ied.; ' \.      
 00013620: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00013630: 2020 2020 2020 6627 692e 652e 207b 7365        f'i.e. {se
-00013640: 6c66 2e5f 7472 7565 5f6e 6567 6174 6976  lf._true_negativ
-00013650: 6573 7d20 227b 7365 6c66 2e5f 6e65 6761  es} "{self._nega
-00013660: 7469 7665 5f63 6c61 7373 7d22 206c 6162  tive_class}" lab
-00013670: 656c 7320 7765 7265 2063 6f72 7265 6374  els were correct
-00013680: 6c79 2027 205c 0a20 2020 2020 2020 2020  ly ' \.         
-00013690: 2020 2020 2020 2020 2020 2020 2066 2769               f'i
-000136a0: 6465 6e74 6966 6965 6420 6f75 7420 6f66  dentified out of
-000136b0: 207b 7365 6c66 2e5f 6163 7475 616c 5f6e   {self._actual_n
-000136c0: 6567 6174 6976 6573 7d20 696e 7374 616e  egatives} instan
-000136d0: 6365 7327 0a0a 2020 2020 2020 2020 6670  ces'..        fp
-000136e0: 725f 6d65 7373 6167 6520 3d20 6627 7b73  r_message = f'{s
-000136f0: 656c 662e 6661 6c73 655f 706f 7369 7469  elf.false_positi
-00013700: 7665 5f72 6174 653a 2e31 257d 206f 6620  ve_rate:.1%} of 
-00013710: 6e65 6761 7469 7665 2069 6e73 7461 6e63  negative instanc
-00013720: 6573 2077 6572 6520 696e 636f 7272 6563  es were incorrec
-00013730: 746c 7920 6964 656e 7469 6669 6564 2027  tly identified '
-00013740: 205c 0a20 2020 2020 2020 2020 2020 2020   \.             
-00013750: 2020 2020 2020 2020 2066 2761 7320 706f           f'as po
-00013760: 7369 7469 7665 3b20 2720 5c0a 2020 2020  sitive; ' \.    
-00013770: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00013780: 2020 6627 692e 652e 207b 7365 6c66 2e5f    f'i.e. {self._
-00013790: 6661 6c73 655f 706f 7369 7469 7665 737d  false_positives}
-000137a0: 2022 7b73 656c 662e 5f6e 6567 6174 6976   "{self._negativ
-000137b0: 655f 636c 6173 737d 2220 6c61 6265 6c73  e_class}" labels
-000137c0: 2077 6572 6520 696e 636f 7272 6563 746c   were incorrectl
-000137d0: 7920 2720 5c0a 2020 2020 2020 2020 2020  y ' \.          
-000137e0: 2020 2020 2020 2020 2020 2020 6627 6964              f'id
-000137f0: 656e 7469 6669 6564 2061 7320 227b 7365  entified as "{se
-00013800: 6c66 2e5f 706f 7369 7469 7665 5f63 6c61  lf._positive_cla
-00013810: 7373 7d22 2c20 6f75 7420 6f66 207b 7365  ss}", out of {se
-00013820: 6c66 2e5f 6163 7475 616c 5f6e 6567 6174  lf._actual_negat
-00013830: 6976 6573 7d20 696e 7374 616e 6365 7327  ives} instances'
-00013840: 0a0a 2020 2020 2020 2020 666e 725f 6d65  ..        fnr_me
-00013850: 7373 6167 6520 3d20 6627 7b73 656c 662e  ssage = f'{self.
-00013860: 6661 6c73 655f 6e65 6761 7469 7665 5f72  false_negative_r
-00013870: 6174 653a 2e31 257d 206f 6620 706f 7369  ate:.1%} of posi
-00013880: 7469 7665 2069 6e73 7461 6e63 6573 2077  tive instances w
-00013890: 6572 6520 696e 636f 7272 6563 746c 7920  ere incorrectly 
-000138a0: 6964 656e 7469 6669 6564 2027 205c 0a20  identified ' \. 
-000138b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000138c0: 2020 2020 2066 2761 7320 6e65 6761 7469       f'as negati
-000138d0: 7665 3b20 2720 5c0a 2020 2020 2020 2020  ve; ' \.        
-000138e0: 2020 2020 2020 2020 2020 2020 2020 6627                f'
-000138f0: 692e 652e 207b 7365 6c66 2e5f 6661 6c73  i.e. {self._fals
-00013900: 655f 6e65 6761 7469 7665 737d 2022 7b73  e_negatives} "{s
-00013910: 656c 662e 5f70 6f73 6974 6976 655f 636c  elf._positive_cl
-00013920: 6173 737d 2220 6c61 6265 6c73 2077 6572  ass}" labels wer
-00013930: 6520 696e 636f 7272 6563 746c 7920 2720  e incorrectly ' 
-00013940: 5c0a 2020 2020 2020 2020 2020 2020 2020  \.              
-00013950: 2020 2020 2020 2020 6627 6964 656e 7469          f'identi
-00013960: 6669 6564 2061 7320 227b 7365 6c66 2e5f  fied as "{self._
-00013970: 6e65 6761 7469 7665 5f63 6c61 7373 7d22  negative_class}"
-00013980: 2c20 6f75 7420 6f66 207b 7365 6c66 2e5f  , out of {self._
-00013990: 6163 7475 616c 5f70 6f73 6974 6976 6573  actual_positives
-000139a0: 7d20 696e 7374 616e 6365 7327 0a0a 2020  } instances'..  
-000139b0: 2020 2020 2020 7070 765f 6d65 7373 6167        ppv_messag
-000139c0: 6520 3d20 6627 5768 656e 2074 6865 206d  e = f'When the m
-000139d0: 6f64 656c 2063 6c61 696d 7320 616e 2069  odel claims an i
-000139e0: 6e73 7461 6e63 6520 6973 2070 6f73 6974  nstance is posit
-000139f0: 6976 652c 2069 7420 6973 2063 6f72 7265  ive, it is corre
-00013a00: 6374 2027 205c 0a20 2020 2020 2020 2020  ct ' \.         
-00013a10: 2020 2020 2020 2020 2020 2020 2066 277b               f'{
-00013a20: 7365 6c66 2e70 6f73 6974 6976 655f 7072  self.positive_pr
-00013a30: 6564 6963 7469 7665 5f76 616c 7565 3a2e  edictive_value:.
-00013a40: 3125 7d20 6f66 2074 6865 2074 696d 653b  1%} of the time;
-00013a50: 2027 205c 0a20 2020 2020 2020 2020 2020   ' \.           
-00013a60: 2020 2020 2020 2020 2020 2066 2769 2e65             f'i.e
-00013a70: 2e20 6f75 7420 6f66 2074 6865 207b 7365  . out of the {se
-00013a80: 6c66 2e5f 7472 7565 5f70 6f73 6974 6976  lf._true_positiv
-00013a90: 6573 202b 2073 656c 662e 5f66 616c 7365  es + self._false
-00013aa0: 5f70 6f73 6974 6976 6573 7d20 7469 6d65  _positives} time
-00013ab0: 7320 7468 6520 6d6f 6465 6c20 2720 5c0a  s the model ' \.
+00013630: 6627 692e 652e 207b 7365 6c66 2e5f 7472  f'i.e. {self._tr
+00013640: 7565 5f6e 6567 6174 6976 6573 7d20 227b  ue_negatives} "{
+00013650: 7365 6c66 2e5f 6e65 6761 7469 7665 5f63  self._negative_c
+00013660: 6c61 7373 7d22 206c 6162 656c 7320 7765  lass}" labels we
+00013670: 7265 2063 6f72 7265 6374 6c79 2027 205c  re correctly ' \
+00013680: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00013690: 2020 2020 2020 2066 2769 6465 6e74 6966         f'identif
+000136a0: 6965 6420 6f75 7420 6f66 207b 7365 6c66  ied out of {self
+000136b0: 2e5f 6163 7475 616c 5f6e 6567 6174 6976  ._actual_negativ
+000136c0: 6573 7d20 696e 7374 616e 6365 7327 0a0a  es} instances'..
+000136d0: 2020 2020 2020 2020 6670 725f 6d65 7373          fpr_mess
+000136e0: 6167 6520 3d20 6627 7b73 656c 662e 6661  age = f'{self.fa
+000136f0: 6c73 655f 706f 7369 7469 7665 5f72 6174  lse_positive_rat
+00013700: 653a 2e31 257d 206f 6620 6e65 6761 7469  e:.1%} of negati
+00013710: 7665 2069 6e73 7461 6e63 6573 2077 6572  ve instances wer
+00013720: 6520 696e 636f 7272 6563 746c 7920 6964  e incorrectly id
+00013730: 656e 7469 6669 6564 2027 205c 0a20 2020  entified ' \.   
+00013740: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00013750: 2020 2066 2761 7320 706f 7369 7469 7665     f'as positive
+00013760: 3b20 2720 5c0a 2020 2020 2020 2020 2020  ; ' \.          
+00013770: 2020 2020 2020 2020 2020 2020 6627 692e              f'i.
+00013780: 652e 207b 7365 6c66 2e5f 6661 6c73 655f  e. {self._false_
+00013790: 706f 7369 7469 7665 737d 2022 7b73 656c  positives} "{sel
+000137a0: 662e 5f6e 6567 6174 6976 655f 636c 6173  f._negative_clas
+000137b0: 737d 2220 6c61 6265 6c73 2077 6572 6520  s}" labels were 
+000137c0: 696e 636f 7272 6563 746c 7920 2720 5c0a  incorrectly ' \.
+000137d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000137e0: 2020 2020 2020 6627 6964 656e 7469 6669        f'identifi
+000137f0: 6564 2061 7320 227b 7365 6c66 2e5f 706f  ed as "{self._po
+00013800: 7369 7469 7665 5f63 6c61 7373 7d22 2c20  sitive_class}", 
+00013810: 6f75 7420 6f66 207b 7365 6c66 2e5f 6163  out of {self._ac
+00013820: 7475 616c 5f6e 6567 6174 6976 6573 7d20  tual_negatives} 
+00013830: 696e 7374 616e 6365 7327 0a0a 2020 2020  instances'..    
+00013840: 2020 2020 666e 725f 6d65 7373 6167 6520      fnr_message 
+00013850: 3d20 6627 7b73 656c 662e 6661 6c73 655f  = f'{self.false_
+00013860: 6e65 6761 7469 7665 5f72 6174 653a 2e31  negative_rate:.1
+00013870: 257d 206f 6620 706f 7369 7469 7665 2069  %} of positive i
+00013880: 6e73 7461 6e63 6573 2077 6572 6520 696e  nstances were in
+00013890: 636f 7272 6563 746c 7920 6964 656e 7469  correctly identi
+000138a0: 6669 6564 2027 205c 0a20 2020 2020 2020  fied ' \.       
+000138b0: 2020 2020 2020 2020 2020 2020 2020 2066                 f
+000138c0: 2761 7320 6e65 6761 7469 7665 3b20 2720  'as negative; ' 
+000138d0: 5c0a 2020 2020 2020 2020 2020 2020 2020  \.              
+000138e0: 2020 2020 2020 2020 6627 692e 652e 207b          f'i.e. {
+000138f0: 7365 6c66 2e5f 6661 6c73 655f 6e65 6761  self._false_nega
+00013900: 7469 7665 737d 2022 7b73 656c 662e 5f70  tives} "{self._p
+00013910: 6f73 6974 6976 655f 636c 6173 737d 2220  ositive_class}" 
+00013920: 6c61 6265 6c73 2077 6572 6520 696e 636f  labels were inco
+00013930: 7272 6563 746c 7920 2720 5c0a 2020 2020  rrectly ' \.    
+00013940: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00013950: 2020 6627 6964 656e 7469 6669 6564 2061    f'identified a
+00013960: 7320 227b 7365 6c66 2e5f 6e65 6761 7469  s "{self._negati
+00013970: 7665 5f63 6c61 7373 7d22 2c20 6f75 7420  ve_class}", out 
+00013980: 6f66 207b 7365 6c66 2e5f 6163 7475 616c  of {self._actual
+00013990: 5f70 6f73 6974 6976 6573 7d20 696e 7374  _positives} inst
+000139a0: 616e 6365 7327 0a0a 2020 2020 2020 2020  ances'..        
+000139b0: 7070 765f 6d65 7373 6167 6520 3d20 6627  ppv_message = f'
+000139c0: 5768 656e 2074 6865 206d 6f64 656c 2063  When the model c
+000139d0: 6c61 696d 7320 616e 2069 6e73 7461 6e63  laims an instanc
+000139e0: 6520 6973 2070 6f73 6974 6976 652c 2069  e is positive, i
+000139f0: 7420 6973 2063 6f72 7265 6374 2027 205c  t is correct ' \
+00013a00: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00013a10: 2020 2020 2020 2066 277b 7365 6c66 2e70         f'{self.p
+00013a20: 6f73 6974 6976 655f 7072 6564 6963 7469  ositive_predicti
+00013a30: 7665 5f76 616c 7565 3a2e 3125 7d20 6f66  ve_value:.1%} of
+00013a40: 2074 6865 2074 696d 653b 2027 205c 0a20   the time; ' \. 
+00013a50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00013a60: 2020 2020 2066 2769 2e65 2e20 6f75 7420       f'i.e. out 
+00013a70: 6f66 2074 6865 207b 7365 6c66 2e5f 7472  of the {self._tr
+00013a80: 7565 5f70 6f73 6974 6976 6573 202b 2073  ue_positives + s
+00013a90: 656c 662e 5f66 616c 7365 5f70 6f73 6974  elf._false_posit
+00013aa0: 6976 6573 7d20 7469 6d65 7320 7468 6520  ives} times the 
+00013ab0: 6d6f 6465 6c20 2720 5c0a 2020 2020 2020  model ' \.      
 00013ac0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00013ad0: 2020 2020 2020 6627 7072 6564 6963 7465        f'predicte
-00013ae0: 6420 227b 7365 6c66 2e5f 706f 7369 7469  d "{self._positi
-00013af0: 7665 5f63 6c61 7373 7d22 2c20 6974 2077  ve_class}", it w
-00013b00: 6173 2063 6f72 7265 6374 207b 7365 6c66  as correct {self
-00013b10: 2e5f 7472 7565 5f70 6f73 6974 6976 6573  ._true_positives
-00013b20: 7d20 2720 5c0a 2020 2020 2020 2020 2020  } ' \.          
-00013b30: 2020 2020 2020 2020 2020 2020 6627 7469              f'ti
-00013b40: 6d65 733b 2061 2e6b 2e61 2070 7265 6369  mes; a.k.a preci
-00013b50: 7369 6f6e 270a 0a20 2020 2020 2020 206e  sion'..        n
-00013b60: 7076 5f6d 6573 7361 6765 203d 2066 2757  pv_message = f'W
-00013b70: 6865 6e20 7468 6520 6d6f 6465 6c20 636c  hen the model cl
-00013b80: 6169 6d73 2061 6e20 696e 7374 616e 6365  aims an instance
-00013b90: 2069 7320 6e65 6761 7469 7665 2c20 6974   is negative, it
-00013ba0: 2069 7320 636f 7272 6563 7420 2720 5c0a   is correct ' \.
+00013ad0: 6627 7072 6564 6963 7465 6420 227b 7365  f'predicted "{se
+00013ae0: 6c66 2e5f 706f 7369 7469 7665 5f63 6c61  lf._positive_cla
+00013af0: 7373 7d22 2c20 6974 2077 6173 2063 6f72  ss}", it was cor
+00013b00: 7265 6374 207b 7365 6c66 2e5f 7472 7565  rect {self._true
+00013b10: 5f70 6f73 6974 6976 6573 7d20 2720 5c0a  _positives} ' \.
+00013b20: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00013b30: 2020 2020 2020 6627 7469 6d65 733b 2061        f'times; a
+00013b40: 2e6b 2e61 2070 7265 6369 7369 6f6e 270a  .k.a precision'.
+00013b50: 0a20 2020 2020 2020 206e 7076 5f6d 6573  .        npv_mes
+00013b60: 7361 6765 203d 2066 2757 6865 6e20 7468  sage = f'When th
+00013b70: 6520 6d6f 6465 6c20 636c 6169 6d73 2061  e model claims a
+00013b80: 6e20 696e 7374 616e 6365 2069 7320 6e65  n instance is ne
+00013b90: 6761 7469 7665 2c20 6974 2069 7320 636f  gative, it is co
+00013ba0: 7272 6563 7420 2720 5c0a 2020 2020 2020  rrect ' \.      
 00013bb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00013bc0: 2020 2020 2020 6627 7b73 656c 662e 6e65        f'{self.ne
-00013bd0: 6761 7469 7665 5f70 7265 6469 6374 6976  gative_predictiv
-00013be0: 655f 7661 6c75 653a 2e31 257d 206f 6620  e_value:.1%} of 
-00013bf0: 7468 6520 7469 6d65 3b20 2720 5c0a 2020  the time; ' \.  
-00013c00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00013c10: 2020 2020 6627 692e 652e 206f 7574 206f      f'i.e. out o
-00013c20: 6620 7468 6520 7b73 656c 662e 5f74 7275  f the {self._tru
-00013c30: 655f 6e65 6761 7469 7665 7320 2b20 7365  e_negatives + se
-00013c40: 6c66 2e5f 6661 6c73 655f 6e65 6761 7469  lf._false_negati
-00013c50: 7665 737d 2074 696d 6573 2074 6865 206d  ves} times the m
-00013c60: 6f64 656c 2027 205c 0a20 2020 2020 2020  odel ' \.       
-00013c70: 2020 2020 2020 2020 2020 2020 2020 2066                 f
-00013c80: 2770 7265 6469 6374 6564 2022 7b73 656c  'predicted "{sel
-00013c90: 662e 5f6e 6567 6174 6976 655f 636c 6173  f._negative_clas
-00013ca0: 737d 222c 2069 7420 7761 7320 636f 7272  s}", it was corr
-00013cb0: 6563 7420 7b73 656c 662e 5f74 7275 655f  ect {self._true_
-00013cc0: 6e65 6761 7469 7665 737d 2074 696d 6573  negatives} times
-00013cd0: 270a 0a20 2020 2020 2020 2066 315f 6d65  '..        f1_me
-00013ce0: 7373 6167 6520 3d20 2754 6865 2046 3120  ssage = 'The F1 
-00013cf0: 7363 6f72 6520 6361 6e20 6265 2069 6e74  score can be int
-00013d00: 6572 7072 6574 6564 2061 7320 6120 7765  erpreted as a we
-00013d10: 6967 6874 6564 2061 7665 7261 6765 206f  ighted average o
-00013d20: 6620 7468 6520 7072 6563 6973 696f 6e20  f the precision 
-00013d30: 616e 6420 7265 6361 6c6c 2c20 2720 5c0a  and recall, ' \.
-00013d40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00013d50: 2020 2020 2027 7768 6572 6520 616e 2046       'where an F
-00013d60: 3120 7363 6f72 6520 7265 6163 6865 7320  1 score reaches 
-00013d70: 6974 7320 6265 7374 2076 616c 7565 2061  its best value a
-00013d80: 7420 3120 616e 6420 776f 7273 7420 7363  t 1 and worst sc
-00013d90: 6f72 6520 6174 2030 2e27 0a0a 2020 2020  ore at 0.'..    
-00013da0: 2020 2020 6163 6375 7261 6379 5f6d 6573      accuracy_mes
-00013db0: 7361 6765 203d 2066 277b 7365 6c66 2e61  sage = f'{self.a
-00013dc0: 6363 7572 6163 793a 2e31 257d 206f 6620  ccuracy:.1%} of 
-00013dd0: 696e 7374 616e 6365 7320 7765 7265 2063  instances were c
-00013de0: 6f72 7265 6374 6c79 2069 6465 6e74 6966  orrectly identif
-00013df0: 6965 6427 0a20 2020 2020 2020 2065 7272  ied'.        err
-00013e00: 6f72 5f6d 6573 7361 6765 203d 2066 277b  or_message = f'{
-00013e10: 7365 6c66 2e65 7272 6f72 5f72 6174 653a  self.error_rate:
-00013e20: 2e31 257d 206f 6620 696e 7374 616e 6365  .1%} of instance
-00013e30: 7320 7765 7265 2069 6e63 6f72 7265 6374  s were incorrect
-00013e40: 6c79 2069 6465 6e74 6966 6965 6427 0a20  ly identified'. 
-00013e50: 2020 2020 2020 2070 7265 7661 6c65 6e63         prevalenc
-00013e60: 655f 6d65 7373 6167 6520 3d20 6627 7b73  e_message = f'{s
-00013e70: 656c 662e 7072 6576 616c 656e 6365 3a2e  elf.prevalence:.
-00013e80: 3125 7d20 6f66 2074 6865 2064 6174 6120  1%} of the data 
-00013e90: 6172 6520 706f 7369 7469 7665 3b20 692e  are positive; i.
-00013ea0: 652e 206f 7574 206f 6620 2720 5c0a 2020  e. out of ' \.  
+00013bc0: 6627 7b73 656c 662e 6e65 6761 7469 7665  f'{self.negative
+00013bd0: 5f70 7265 6469 6374 6976 655f 7661 6c75  _predictive_valu
+00013be0: 653a 2e31 257d 206f 6620 7468 6520 7469  e:.1%} of the ti
+00013bf0: 6d65 3b20 2720 5c0a 2020 2020 2020 2020  me; ' \.        
+00013c00: 2020 2020 2020 2020 2020 2020 2020 6627                f'
+00013c10: 692e 652e 206f 7574 206f 6620 7468 6520  i.e. out of the 
+00013c20: 7b73 656c 662e 5f74 7275 655f 6e65 6761  {self._true_nega
+00013c30: 7469 7665 7320 2b20 7365 6c66 2e5f 6661  tives + self._fa
+00013c40: 6c73 655f 6e65 6761 7469 7665 737d 2074  lse_negatives} t
+00013c50: 696d 6573 2074 6865 206d 6f64 656c 2027  imes the model '
+00013c60: 205c 0a20 2020 2020 2020 2020 2020 2020   \.             
+00013c70: 2020 2020 2020 2020 2066 2770 7265 6469           f'predi
+00013c80: 6374 6564 2022 7b73 656c 662e 5f6e 6567  cted "{self._neg
+00013c90: 6174 6976 655f 636c 6173 737d 222c 2069  ative_class}", i
+00013ca0: 7420 7761 7320 636f 7272 6563 7420 7b73  t was correct {s
+00013cb0: 656c 662e 5f74 7275 655f 6e65 6761 7469  elf._true_negati
+00013cc0: 7665 737d 2074 696d 6573 270a 0a20 2020  ves} times'..   
+00013cd0: 2020 2020 2066 315f 6d65 7373 6167 6520       f1_message 
+00013ce0: 3d20 2754 6865 2046 3120 7363 6f72 6520  = 'The F1 score 
+00013cf0: 6361 6e20 6265 2069 6e74 6572 7072 6574  can be interpret
+00013d00: 6564 2061 7320 6120 7765 6967 6874 6564  ed as a weighted
+00013d10: 2061 7665 7261 6765 206f 6620 7468 6520   average of the 
+00013d20: 7072 6563 6973 696f 6e20 616e 6420 7265  precision and re
+00013d30: 6361 6c6c 2c20 2720 5c0a 2020 2020 2020  call, ' \.      
+00013d40: 2020 2020 2020 2020 2020 2020 2020 2027                 '
+00013d50: 7768 6572 6520 616e 2046 3120 7363 6f72  where an F1 scor
+00013d60: 6520 7265 6163 6865 7320 6974 7320 6265  e reaches its be
+00013d70: 7374 2076 616c 7565 2061 7420 3120 616e  st value at 1 an
+00013d80: 6420 776f 7273 7420 7363 6f72 6520 6174  d worst score at
+00013d90: 2030 2e27 0a0a 2020 2020 2020 2020 6163   0.'..        ac
+00013da0: 6375 7261 6379 5f6d 6573 7361 6765 203d  curacy_message =
+00013db0: 2066 277b 7365 6c66 2e61 6363 7572 6163   f'{self.accurac
+00013dc0: 793a 2e31 257d 206f 6620 696e 7374 616e  y:.1%} of instan
+00013dd0: 6365 7320 7765 7265 2063 6f72 7265 6374  ces were correct
+00013de0: 6c79 2069 6465 6e74 6966 6965 6427 0a20  ly identified'. 
+00013df0: 2020 2020 2020 2065 7272 6f72 5f6d 6573         error_mes
+00013e00: 7361 6765 203d 2066 277b 7365 6c66 2e65  sage = f'{self.e
+00013e10: 7272 6f72 5f72 6174 653a 2e31 257d 206f  rror_rate:.1%} o
+00013e20: 6620 696e 7374 616e 6365 7320 7765 7265  f instances were
+00013e30: 2069 6e63 6f72 7265 6374 6c79 2069 6465   incorrectly ide
+00013e40: 6e74 6966 6965 6427 0a20 2020 2020 2020  ntified'.       
+00013e50: 2070 7265 7661 6c65 6e63 655f 6d65 7373   prevalence_mess
+00013e60: 6167 6520 3d20 6627 7b73 656c 662e 7072  age = f'{self.pr
+00013e70: 6576 616c 656e 6365 3a2e 3125 7d20 6f66  evalence:.1%} of
+00013e80: 2074 6865 2064 6174 6120 6172 6520 706f   the data are po
+00013e90: 7369 7469 7665 3b20 692e 652e 206f 7574  sitive; i.e. out
+00013ea0: 206f 6620 2720 5c0a 2020 2020 2020 2020   of ' \.        
 00013eb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00013ec0: 2020 2020 2020 2020 2020 2066 277b 7365             f'{se
-00013ed0: 6c66 2e73 616d 706c 655f 7369 7a65 7d20  lf.sample_size} 
-00013ee0: 746f 7461 6c20 6f62 7365 7276 6174 696f  total observatio
-00013ef0: 6e73 3b20 7b73 656c 662e 5f61 6374 7561  ns; {self._actua
-00013f00: 6c5f 706f 7369 7469 7665 737d 2061 7265  l_positives} are
-00013f10: 206c 6162 656c 6564 2027 205c 0a20 2020   labeled ' \.   
+00013ec0: 2020 2020 2066 277b 7365 6c66 2e73 616d       f'{self.sam
+00013ed0: 706c 655f 7369 7a65 7d20 746f 7461 6c20  ple_size} total 
+00013ee0: 6f62 7365 7276 6174 696f 6e73 3b20 7b73  observations; {s
+00013ef0: 656c 662e 5f61 6374 7561 6c5f 706f 7369  elf._actual_posi
+00013f00: 7469 7665 737d 2061 7265 206c 6162 656c  tives} are label
+00013f10: 6564 2027 205c 0a20 2020 2020 2020 2020  ed ' \.         
 00013f20: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00013f30: 2020 2020 2020 2020 2020 6627 6173 2022            f'as "
-00013f40: 7b73 656c 662e 5f70 6f73 6974 6976 655f  {self._positive_
-00013f50: 636c 6173 737d 2227 0a20 2020 2020 2020  class}"'.       
-00013f60: 2074 6f74 616c 5f6f 6273 5f6d 6573 7361   total_obs_messa
-00013f70: 6765 203d 2066 2754 6865 7265 2061 7265  ge = f'There are
-00013f80: 207b 7365 6c66 2e73 616d 706c 655f 7369   {self.sample_si
-00013f90: 7a65 7d20 746f 7461 6c20 6f62 7365 7276  ze} total observ
-00013fa0: 6174 696f 6e73 3b20 692e 652e 2073 616d  ations; i.e. sam
-00013fb0: 706c 6520 7369 7a65 270a 0a20 2020 2020  ple size'..     
-00013fc0: 2020 2072 6574 7572 6e20 7b27 4155 4327     return {'AUC'
-00013fd0: 3a20 2873 656c 662e 6175 632c 2061 7563  : (self.auc, auc
-00013fe0: 5f6d 6573 7361 6765 292c 0a20 2020 2020  _message),.     
-00013ff0: 2020 2020 2020 2020 2020 2027 5472 7565             'True
-00014000: 2050 6f73 6974 6976 6520 5261 7465 273a   Positive Rate':
-00014010: 2028 7365 6c66 2e74 7275 655f 706f 7369   (self.true_posi
-00014020: 7469 7665 5f72 6174 652c 2074 7072 5f6d  tive_rate, tpr_m
-00014030: 6573 7361 6765 292c 0a20 2020 2020 2020  essage),.       
-00014040: 2020 2020 2020 2020 2027 5472 7565 204e           'True N
-00014050: 6567 6174 6976 6520 5261 7465 273a 2028  egative Rate': (
-00014060: 7365 6c66 2e74 7275 655f 6e65 6761 7469  self.true_negati
-00014070: 7665 5f72 6174 652c 2074 6e72 5f6d 6573  ve_rate, tnr_mes
-00014080: 7361 6765 292c 0a20 2020 2020 2020 2020  sage),.         
-00014090: 2020 2020 2020 2027 4661 6c73 6520 506f         'False Po
-000140a0: 7369 7469 7665 2052 6174 6527 3a20 2873  sitive Rate': (s
-000140b0: 656c 662e 6661 6c73 655f 706f 7369 7469  elf.false_positi
-000140c0: 7665 5f72 6174 652c 2066 7072 5f6d 6573  ve_rate, fpr_mes
-000140d0: 7361 6765 292c 0a20 2020 2020 2020 2020  sage),.         
-000140e0: 2020 2020 2020 2027 4661 6c73 6520 4e65         'False Ne
-000140f0: 6761 7469 7665 2052 6174 6527 3a20 2873  gative Rate': (s
-00014100: 656c 662e 6661 6c73 655f 6e65 6761 7469  elf.false_negati
-00014110: 7665 5f72 6174 652c 2066 6e72 5f6d 6573  ve_rate, fnr_mes
-00014120: 7361 6765 292c 0a20 2020 2020 2020 2020  sage),.         
-00014130: 2020 2020 2020 2027 506f 7369 7469 7665         'Positive
-00014140: 2050 7265 6469 6374 6976 6520 5661 6c75   Predictive Valu
-00014150: 6527 3a20 2873 656c 662e 706f 7369 7469  e': (self.positi
-00014160: 7665 5f70 7265 6469 6374 6976 655f 7661  ve_predictive_va
-00014170: 6c75 652c 2070 7076 5f6d 6573 7361 6765  lue, ppv_message
-00014180: 292c 0a20 2020 2020 2020 2020 2020 2020  ),.             
-00014190: 2020 2027 4e65 6761 7469 7665 2050 7265     'Negative Pre
-000141a0: 6469 6374 6976 6520 5661 6c75 6527 3a20  dictive Value': 
-000141b0: 2873 656c 662e 6e65 6761 7469 7665 5f70  (self.negative_p
-000141c0: 7265 6469 6374 6976 655f 7661 6c75 652c  redictive_value,
-000141d0: 206e 7076 5f6d 6573 7361 6765 292c 0a20   npv_message),. 
-000141e0: 2020 2020 2020 2020 2020 2020 2020 2027                 '
-000141f0: 4631 2053 636f 7265 273a 2028 7365 6c66  F1 Score': (self
-00014200: 2e66 315f 7363 6f72 652c 2066 315f 6d65  .f1_score, f1_me
-00014210: 7373 6167 6529 2c0a 2020 2020 2020 2020  ssage),.        
-00014220: 2020 2020 2020 2020 2741 6363 7572 6163          'Accurac
-00014230: 7927 3a20 2873 656c 662e 6163 6375 7261  y': (self.accura
-00014240: 6379 2c20 6163 6375 7261 6379 5f6d 6573  cy, accuracy_mes
-00014250: 7361 6765 292c 0a20 2020 2020 2020 2020  sage),.         
-00014260: 2020 2020 2020 2027 4572 726f 7220 5261         'Error Ra
-00014270: 7465 273a 2028 7365 6c66 2e65 7272 6f72  te': (self.error
-00014280: 5f72 6174 652c 2065 7272 6f72 5f6d 6573  _rate, error_mes
-00014290: 7361 6765 292c 0a20 2020 2020 2020 2020  sage),.         
-000142a0: 2020 2020 2020 2027 2520 506f 7369 7469         '% Positi
-000142b0: 7665 273a 2028 7365 6c66 2e70 7265 7661  ve': (self.preva
-000142c0: 6c65 6e63 652c 2070 7265 7661 6c65 6e63  lence, prevalenc
-000142d0: 655f 6d65 7373 6167 6529 2c0a 2020 2020  e_message),.    
-000142e0: 2020 2020 2020 2020 2020 2020 2754 6f74              'Tot
-000142f0: 616c 204f 6273 6572 7661 7469 6f6e 7327  al Observations'
-00014300: 3a20 2873 656c 662e 7361 6d70 6c65 5f73  : (self.sample_s
-00014310: 697a 652c 2074 6f74 616c 5f6f 6273 5f6d  ize, total_obs_m
-00014320: 6573 7361 6765 297d 0a0a 2020 2020 2320  essage)}..    # 
-00014330: 7079 6c69 6e74 3a20 6469 7361 626c 653d  pylint: disable=
-00014340: 746f 6f2d 6d61 6e79 2d61 7267 756d 656e  too-many-argumen
-00014350: 7473 0a20 2020 2064 6566 2061 6c6c 5f6d  ts.    def all_m
-00014360: 6574 7269 6373 5f64 6628 7365 6c66 2c0a  etrics_df(self,.
+00013f30: 2020 2020 6627 6173 2022 7b73 656c 662e      f'as "{self.
+00013f40: 5f70 6f73 6974 6976 655f 636c 6173 737d  _positive_class}
+00013f50: 2227 0a20 2020 2020 2020 2074 6f74 616c  "'.        total
+00013f60: 5f6f 6273 5f6d 6573 7361 6765 203d 2066  _obs_message = f
+00013f70: 2754 6865 7265 2061 7265 207b 7365 6c66  'There are {self
+00013f80: 2e73 616d 706c 655f 7369 7a65 7d20 746f  .sample_size} to
+00013f90: 7461 6c20 6f62 7365 7276 6174 696f 6e73  tal observations
+00013fa0: 3b20 692e 652e 2073 616d 706c 6520 7369  ; i.e. sample si
+00013fb0: 7a65 270a 0a20 2020 2020 2020 2072 6574  ze'..        ret
+00013fc0: 7572 6e20 7b27 4155 4327 3a20 2873 656c  urn {'AUC': (sel
+00013fd0: 662e 6175 632c 2061 7563 5f6d 6573 7361  f.auc, auc_messa
+00013fe0: 6765 292c 0a20 2020 2020 2020 2020 2020  ge),.           
+00013ff0: 2020 2020 2027 5472 7565 2050 6f73 6974       'True Posit
+00014000: 6976 6520 5261 7465 273a 2028 7365 6c66  ive Rate': (self
+00014010: 2e74 7275 655f 706f 7369 7469 7665 5f72  .true_positive_r
+00014020: 6174 652c 2074 7072 5f6d 6573 7361 6765  ate, tpr_message
+00014030: 292c 0a20 2020 2020 2020 2020 2020 2020  ),.             
+00014040: 2020 2027 5472 7565 204e 6567 6174 6976     'True Negativ
+00014050: 6520 5261 7465 273a 2028 7365 6c66 2e74  e Rate': (self.t
+00014060: 7275 655f 6e65 6761 7469 7665 5f72 6174  rue_negative_rat
+00014070: 652c 2074 6e72 5f6d 6573 7361 6765 292c  e, tnr_message),
+00014080: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00014090: 2027 4661 6c73 6520 506f 7369 7469 7665   'False Positive
+000140a0: 2052 6174 6527 3a20 2873 656c 662e 6661   Rate': (self.fa
+000140b0: 6c73 655f 706f 7369 7469 7665 5f72 6174  lse_positive_rat
+000140c0: 652c 2066 7072 5f6d 6573 7361 6765 292c  e, fpr_message),
+000140d0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000140e0: 2027 4661 6c73 6520 4e65 6761 7469 7665   'False Negative
+000140f0: 2052 6174 6527 3a20 2873 656c 662e 6661   Rate': (self.fa
+00014100: 6c73 655f 6e65 6761 7469 7665 5f72 6174  lse_negative_rat
+00014110: 652c 2066 6e72 5f6d 6573 7361 6765 292c  e, fnr_message),
+00014120: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00014130: 2027 506f 7369 7469 7665 2050 7265 6469   'Positive Predi
+00014140: 6374 6976 6520 5661 6c75 6527 3a20 2873  ctive Value': (s
+00014150: 656c 662e 706f 7369 7469 7665 5f70 7265  elf.positive_pre
+00014160: 6469 6374 6976 655f 7661 6c75 652c 2070  dictive_value, p
+00014170: 7076 5f6d 6573 7361 6765 292c 0a20 2020  pv_message),.   
+00014180: 2020 2020 2020 2020 2020 2020 2027 4e65               'Ne
+00014190: 6761 7469 7665 2050 7265 6469 6374 6976  gative Predictiv
+000141a0: 6520 5661 6c75 6527 3a20 2873 656c 662e  e Value': (self.
+000141b0: 6e65 6761 7469 7665 5f70 7265 6469 6374  negative_predict
+000141c0: 6976 655f 7661 6c75 652c 206e 7076 5f6d  ive_value, npv_m
+000141d0: 6573 7361 6765 292c 0a20 2020 2020 2020  essage),.       
+000141e0: 2020 2020 2020 2020 2027 4631 2053 636f           'F1 Sco
+000141f0: 7265 273a 2028 7365 6c66 2e66 315f 7363  re': (self.f1_sc
+00014200: 6f72 652c 2066 315f 6d65 7373 6167 6529  ore, f1_message)
+00014210: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00014220: 2020 2741 6363 7572 6163 7927 3a20 2873    'Accuracy': (s
+00014230: 656c 662e 6163 6375 7261 6379 2c20 6163  elf.accuracy, ac
+00014240: 6375 7261 6379 5f6d 6573 7361 6765 292c  curacy_message),
+00014250: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00014260: 2027 4572 726f 7220 5261 7465 273a 2028   'Error Rate': (
+00014270: 7365 6c66 2e65 7272 6f72 5f72 6174 652c  self.error_rate,
+00014280: 2065 7272 6f72 5f6d 6573 7361 6765 292c   error_message),
+00014290: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000142a0: 2027 2520 506f 7369 7469 7665 273a 2028   '% Positive': (
+000142b0: 7365 6c66 2e70 7265 7661 6c65 6e63 652c  self.prevalence,
+000142c0: 2070 7265 7661 6c65 6e63 655f 6d65 7373   prevalence_mess
+000142d0: 6167 6529 2c0a 2020 2020 2020 2020 2020  age),.          
+000142e0: 2020 2020 2020 2754 6f74 616c 204f 6273        'Total Obs
+000142f0: 6572 7661 7469 6f6e 7327 3a20 2873 656c  ervations': (sel
+00014300: 662e 7361 6d70 6c65 5f73 697a 652c 2074  f.sample_size, t
+00014310: 6f74 616c 5f6f 6273 5f6d 6573 7361 6765  otal_obs_message
+00014320: 297d 0a0a 2020 2020 2320 7079 6c69 6e74  )}..    # pylint
+00014330: 3a20 6469 7361 626c 653d 746f 6f2d 6d61  : disable=too-ma
+00014340: 6e79 2d61 7267 756d 656e 7473 0a20 2020  ny-arguments.   
+00014350: 2064 6566 2061 6c6c 5f6d 6574 7269 6373   def all_metrics
+00014360: 5f64 6628 7365 6c66 2c0a 2020 2020 2020  _df(self,.      
 00014370: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014380: 2020 2020 2020 2072 6574 7572 6e5f 6578         return_ex
-00014390: 706c 616e 6174 696f 6e73 3a20 626f 6f6c  planations: bool
-000143a0: 203d 2054 7275 652c 0a20 2020 2020 2020   = True,.       
-000143b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000143c0: 6475 6d6d 795f 636c 6173 7369 6669 6572  dummy_classifier
-000143d0: 5f73 7472 6174 6567 793a 2055 6e69 6f6e  _strategy: Union
-000143e0: 5b73 7472 2c20 6c69 7374 2c20 4e6f 6e65  [str, list, None
-000143f0: 5d20 3d20 2770 7269 6f72 272c 0a20 2020  ] = 'prior',.   
-00014400: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014410: 2020 2020 6475 6d6d 795f 636c 6173 7369      dummy_classi
-00014420: 6669 6572 5f63 6f6e 7374 616e 743a 2055  fier_constant: U
-00014430: 6e69 6f6e 5b69 6e74 5d20 3d20 312c 0a20  nion[int] = 1,. 
+00014380: 2072 6574 7572 6e5f 6578 706c 616e 6174   return_explanat
+00014390: 696f 6e73 3a20 626f 6f6c 203d 2054 7275  ions: bool = Tru
+000143a0: 652c 0a20 2020 2020 2020 2020 2020 2020  e,.             
+000143b0: 2020 2020 2020 2020 2020 6475 6d6d 795f            dummy_
+000143c0: 636c 6173 7369 6669 6572 5f73 7472 6174  classifier_strat
+000143d0: 6567 793a 2055 6e69 6f6e 5b73 7472 2c20  egy: Union[str, 
+000143e0: 6c69 7374 2c20 4e6f 6e65 5d20 3d20 2770  list, None] = 'p
+000143f0: 7269 6f72 272c 0a20 2020 2020 2020 2020  rior',.         
+00014400: 2020 2020 2020 2020 2020 2020 2020 6475                du
+00014410: 6d6d 795f 636c 6173 7369 6669 6572 5f63  mmy_classifier_c
+00014420: 6f6e 7374 616e 743a 2055 6e69 6f6e 5b69  onstant: Union[i
+00014430: 6e74 5d20 3d20 312c 0a20 2020 2020 2020  nt] = 1,.       
 00014440: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014450: 2020 2020 2020 7265 7475 726e 5f73 7479        return_sty
-00014460: 6c65 3a20 626f 6f6c 203d 2046 616c 7365  le: bool = False
-00014470: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00014480: 2020 2020 2020 2020 2072 6f75 6e64 5f62           round_b
-00014490: 793a 204f 7074 696f 6e61 6c5b 696e 745d  y: Optional[int]
-000144a0: 203d 204e 6f6e 6529 202d 3e20 556e 696f   = None) -> Unio
-000144b0: 6e5b 7064 2e44 6174 6146 7261 6d65 2c20  n[pd.DataFrame, 
-000144c0: 5374 796c 6572 5d3a 0a20 2020 2020 2020  Styler]:.       
-000144d0: 2022 2222 416c 6c20 6f66 2074 6865 206d   """All of the m
-000144e0: 6574 7269 6373 2061 7265 2072 6574 7572  etrics are retur
-000144f0: 6e65 6420 6173 2061 2044 6174 6146 7261  ned as a DataFra
-00014500: 6d65 2e0a 0a20 2020 2020 2020 2041 7267  me...        Arg
-00014510: 733a 0a20 2020 2020 2020 2020 2020 2072  s:.            r
-00014520: 6574 7572 6e5f 6578 706c 616e 6174 696f  eturn_explanatio
-00014530: 6e73 3a0a 2020 2020 2020 2020 2020 2020  ns:.            
-00014540: 2020 2020 6966 2054 7275 652c 2074 6865      if True, the
-00014550: 6e20 7265 7475 726e 2064 6573 6372 6970  n return descrip
-00014560: 7469 6f6e 7320 6f66 2073 636f 7265 2061  tions of score a
-00014570: 6e64 206d 6f72 6520 696e 666f 726d 6174  nd more informat
-00014580: 696f 6e20 696e 2061 6e20 6164 6469 7469  ion in an additi
-00014590: 6f6e 616c 2063 6f6c 756d 6e0a 2020 2020  onal column.    
-000145a0: 2020 2020 2020 2020 6475 6d6d 795f 636c          dummy_cl
-000145b0: 6173 7369 6669 6572 5f73 7472 6174 6567  assifier_strateg
-000145c0: 793a 0a20 2020 2020 2020 2020 2020 2020  y:.             
-000145d0: 2020 2069 6620 6e6f 7420 4e6f 6e65 2c20     if not None, 
-000145e0: 7468 656e 2072 6574 7572 6e73 2063 6f6c  then returns col
-000145f0: 756d 6e28 7329 2063 6f72 7265 7370 6f6e  umn(s) correspon
-00014600: 6469 6e67 2074 6f20 7468 6520 7363 6f72  ding to the scor
-00014610: 6573 2066 726f 6d20 7072 6564 6963 7469  es from predicti
-00014620: 6f6e 7320 6f66 0a20 2020 2020 2020 2020  ons of.         
-00014630: 2020 2020 2020 2073 6b6c 6561 726e 2e64         sklearn.d
-00014640: 756d 6d79 2e44 756d 6d79 436c 6173 7369  ummy.DummyClassi
-00014650: 6669 6572 2c20 6261 7365 6420 6f6e 2074  fier, based on t
-00014660: 6865 2073 7472 6174 6567 7920 286f 7220  he strategy (or 
-00014670: 7374 7261 7465 6769 6573 2920 7072 6f76  strategies) prov
-00014680: 6964 6564 2e20 5661 6c69 6420 7661 6c75  ided. Valid valu
-00014690: 6573 0a20 2020 2020 2020 2020 2020 2020  es.             
-000146a0: 2020 2063 6f72 7265 7370 6f6e 6420 746f     correspond to
-000146b0: 2076 616c 7565 7320 6f66 2060 7374 7261   values of `stra
-000146c0: 7465 6779 6020 7061 7261 6d65 7465 7220  tegy` parameter 
-000146d0: 6c69 7374 6564 0a20 2020 2020 2020 2020  listed.         
-000146e0: 2020 2020 2020 2068 7474 7073 3a2f 2f73         https://s
-000146f0: 6369 6b69 742d 6c65 6172 6e2e 6f72 672f  cikit-learn.org/
-00014700: 7374 6162 6c65 2f6d 6f64 756c 6573 2f67  stable/modules/g
-00014710: 656e 6572 6174 6564 2f73 6b6c 6561 726e  enerated/sklearn
-00014720: 2e64 756d 6d79 2e44 756d 6d79 436c 6173  .dummy.DummyClas
-00014730: 7369 6669 6572 2e68 746d 6c0a 0a20 2020  sifier.html..   
-00014740: 2020 2020 2020 2020 2020 2020 2049 6620               If 
-00014750: 6120 6c69 7374 2069 7320 7061 7373 6564  a list is passed
-00014760: 2069 6e20 2865 2e67 2e20 5b27 7072 696f   in (e.g. ['prio
-00014770: 7227 2c20 2775 6e69 666f 726d 275d 2c20  r', 'uniform'], 
-00014780: 7468 656e 206f 6e65 2073 636f 7265 2063  then one score c
-00014790: 6f6c 756d 6e20 7065 7220 7661 6c75 6520  olumn per value 
-000147a0: 6973 0a20 2020 2020 2020 2020 2020 2020  is.             
-000147b0: 2020 2061 6464 6564 2e0a 0a20 2020 2020     added...     
-000147c0: 2020 2020 2020 2020 2020 2049 6620 4e6f             If No
-000147d0: 6e65 2069 7320 7061 7373 6564 2c20 7468  ne is passed, th
-000147e0: 656e 206e 6f20 6164 6469 7469 6f6e 616c  en no additional
-000147f0: 2063 6f6c 756d 6e73 2061 7265 2061 6464   columns are add
-00014800: 6564 2e0a 2020 2020 2020 2020 2020 2020  ed..            
-00014810: 6475 6d6d 795f 636c 6173 7369 6669 6572  dummy_classifier
-00014820: 5f63 6f6e 7374 616e 743a 0a20 2020 2020  _constant:.     
-00014830: 2020 2020 2020 2020 2020 2054 6865 2065             The e
-00014840: 7870 6c69 6369 7420 636f 6e73 7461 6e74  xplicit constant
-00014850: 2061 7320 7072 6564 6963 7465 6420 6279   as predicted by
-00014860: 2074 6865 20e2 809c 636f 6e73 7461 6e74   the ...constant
-00014870: e280 9d20 7374 7261 7465 6779 2066 6f72  ... strategy for
-00014880: 2074 6865 0a20 2020 2020 2020 2020 2020   the.           
-00014890: 2020 2020 2044 756d 6d79 436c 6173 7369       DummyClassi
-000148a0: 6669 6572 2e0a 2020 2020 2020 2020 2020  fier..          
-000148b0: 2020 2020 2020 5468 6973 2070 6172 616d        This param
-000148c0: 6574 6572 2069 7320 7573 6566 756c 206f  eter is useful o
-000148d0: 6e6c 7920 666f 7220 7468 6520 e280 9c63  nly for the ...c
-000148e0: 6f6e 7374 616e 74e2 809d 2064 756d 6d79  onstant... dummy
-000148f0: 5f63 6c61 7373 6966 6965 725f 7374 7261  _classifier_stra
-00014900: 7465 6779 2e0a 2020 2020 2020 2020 2020  tegy..          
-00014910: 2020 7265 7475 726e 5f73 7479 6c65 3a0a    return_style:.
-00014920: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014930: 6966 2054 7275 652c 2072 6574 7572 6e20  if True, return 
-00014940: 7374 796c 6572 206f 626a 6563 743b 2065  styler object; e
-00014950: 6c73 6520 7265 7475 726e 2064 6174 6166  lse return dataf
-00014960: 7261 6d65 0a20 2020 2020 2020 2020 2020  rame.           
-00014970: 2072 6f75 6e64 5f62 793a 0a20 2020 2020   round_by:.     
-00014980: 2020 2020 2020 2020 2020 2074 6865 206e             the n
-00014990: 756d 6265 7220 6f66 2064 6967 6974 7320  umber of digits 
-000149a0: 746f 2072 6f75 6e64 2062 793b 2069 6620  to round by; if 
-000149b0: 4e6f 6e65 2c20 7468 656e 2064 6f6e 2774  None, then don't
-000149c0: 2072 6f75 6e64 0a20 2020 2020 2020 2022   round.        "
-000149d0: 2222 0a20 2020 2020 2020 2072 6573 756c  "".        resul
-000149e0: 7420 3d20 7064 2e44 6174 6146 7261 6d65  t = pd.DataFrame
-000149f0: 2e66 726f 6d5f 6469 6374 287b 6b65 793a  .from_dict({key:
-00014a00: 2076 616c 7565 5b30 5d20 666f 7220 6b65   value[0] for ke
-00014a10: 792c 2076 616c 7565 2069 6e20 7365 6c66  y, value in self
-00014a20: 2e61 6c6c 5f6d 6574 7269 6373 2e69 7465  .all_metrics.ite
-00014a30: 6d73 2829 7d2c 0a20 2020 2020 2020 2020  ms()},.         
+00014450: 7265 7475 726e 5f73 7479 6c65 3a20 626f  return_style: bo
+00014460: 6f6c 203d 2046 616c 7365 2c0a 2020 2020  ol = False,.    
+00014470: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00014480: 2020 2072 6f75 6e64 5f62 793a 204f 7074     round_by: Opt
+00014490: 696f 6e61 6c5b 696e 745d 203d 204e 6f6e  ional[int] = Non
+000144a0: 6529 202d 3e20 556e 696f 6e5b 7064 2e44  e) -> Union[pd.D
+000144b0: 6174 6146 7261 6d65 2c20 5374 796c 6572  ataFrame, Styler
+000144c0: 5d3a 0a20 2020 2020 2020 2022 2222 416c  ]:.        """Al
+000144d0: 6c20 6f66 2074 6865 206d 6574 7269 6373  l of the metrics
+000144e0: 2061 7265 2072 6574 7572 6e65 6420 6173   are returned as
+000144f0: 2061 2044 6174 6146 7261 6d65 2e0a 0a20   a DataFrame... 
+00014500: 2020 2020 2020 2041 7267 733a 0a20 2020         Args:.   
+00014510: 2020 2020 2020 2020 2072 6574 7572 6e5f           return_
+00014520: 6578 706c 616e 6174 696f 6e73 3a0a 2020  explanations:.  
+00014530: 2020 2020 2020 2020 2020 2020 2020 6966                if
+00014540: 2054 7275 652c 2074 6865 6e20 7265 7475   True, then retu
+00014550: 726e 2064 6573 6372 6970 7469 6f6e 7320  rn descriptions 
+00014560: 6f66 2073 636f 7265 2061 6e64 206d 6f72  of score and mor
+00014570: 6520 696e 666f 726d 6174 696f 6e20 696e  e information in
+00014580: 2061 6e20 6164 6469 7469 6f6e 616c 2063   an additional c
+00014590: 6f6c 756d 6e0a 2020 2020 2020 2020 2020  olumn.          
+000145a0: 2020 6475 6d6d 795f 636c 6173 7369 6669    dummy_classifi
+000145b0: 6572 5f73 7472 6174 6567 793a 0a20 2020  er_strategy:.   
+000145c0: 2020 2020 2020 2020 2020 2020 2069 6620               if 
+000145d0: 6e6f 7420 4e6f 6e65 2c20 7468 656e 2072  not None, then r
+000145e0: 6574 7572 6e73 2063 6f6c 756d 6e28 7329  eturns column(s)
+000145f0: 2063 6f72 7265 7370 6f6e 6469 6e67 2074   corresponding t
+00014600: 6f20 7468 6520 7363 6f72 6573 2066 726f  o the scores fro
+00014610: 6d20 7072 6564 6963 7469 6f6e 7320 6f66  m predictions of
+00014620: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00014630: 2073 6b6c 6561 726e 2e64 756d 6d79 2e44   sklearn.dummy.D
+00014640: 756d 6d79 436c 6173 7369 6669 6572 2c20  ummyClassifier, 
+00014650: 6261 7365 6420 6f6e 2074 6865 2073 7472  based on the str
+00014660: 6174 6567 7920 286f 7220 7374 7261 7465  ategy (or strate
+00014670: 6769 6573 2920 7072 6f76 6964 6564 2e20  gies) provided. 
+00014680: 5661 6c69 6420 7661 6c75 6573 0a20 2020  Valid values.   
+00014690: 2020 2020 2020 2020 2020 2020 2063 6f72               cor
+000146a0: 7265 7370 6f6e 6420 746f 2076 616c 7565  respond to value
+000146b0: 7320 6f66 2060 7374 7261 7465 6779 6020  s of `strategy` 
+000146c0: 7061 7261 6d65 7465 7220 6c69 7374 6564  parameter listed
+000146d0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000146e0: 2068 7474 7073 3a2f 2f73 6369 6b69 742d   https://scikit-
+000146f0: 6c65 6172 6e2e 6f72 672f 7374 6162 6c65  learn.org/stable
+00014700: 2f6d 6f64 756c 6573 2f67 656e 6572 6174  /modules/generat
+00014710: 6564 2f73 6b6c 6561 726e 2e64 756d 6d79  ed/sklearn.dummy
+00014720: 2e44 756d 6d79 436c 6173 7369 6669 6572  .DummyClassifier
+00014730: 2e68 746d 6c0a 0a20 2020 2020 2020 2020  .html..         
+00014740: 2020 2020 2020 2049 6620 6120 6c69 7374         If a list
+00014750: 2069 7320 7061 7373 6564 2069 6e20 2865   is passed in (e
+00014760: 2e67 2e20 5b27 7072 696f 7227 2c20 2775  .g. ['prior', 'u
+00014770: 6e69 666f 726d 275d 2c20 7468 656e 206f  niform'], then o
+00014780: 6e65 2073 636f 7265 2063 6f6c 756d 6e20  ne score column 
+00014790: 7065 7220 7661 6c75 6520 6973 0a20 2020  per value is.   
+000147a0: 2020 2020 2020 2020 2020 2020 2061 6464               add
+000147b0: 6564 2e0a 0a20 2020 2020 2020 2020 2020  ed...           
+000147c0: 2020 2020 2049 6620 4e6f 6e65 2069 7320       If None is 
+000147d0: 7061 7373 6564 2c20 7468 656e 206e 6f20  passed, then no 
+000147e0: 6164 6469 7469 6f6e 616c 2063 6f6c 756d  additional colum
+000147f0: 6e73 2061 7265 2061 6464 6564 2e0a 2020  ns are added..  
+00014800: 2020 2020 2020 2020 2020 6475 6d6d 795f            dummy_
+00014810: 636c 6173 7369 6669 6572 5f63 6f6e 7374  classifier_const
+00014820: 616e 743a 0a20 2020 2020 2020 2020 2020  ant:.           
+00014830: 2020 2020 2054 6865 2065 7870 6c69 6369       The explici
+00014840: 7420 636f 6e73 7461 6e74 2061 7320 7072  t constant as pr
+00014850: 6564 6963 7465 6420 6279 2074 6865 20e2  edicted by the .
+00014860: 809c 636f 6e73 7461 6e74 e280 9d20 7374  ..constant... st
+00014870: 7261 7465 6779 2066 6f72 2074 6865 0a20  rategy for the. 
+00014880: 2020 2020 2020 2020 2020 2020 2020 2044                 D
+00014890: 756d 6d79 436c 6173 7369 6669 6572 2e0a  ummyClassifier..
+000148a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000148b0: 5468 6973 2070 6172 616d 6574 6572 2069  This parameter i
+000148c0: 7320 7573 6566 756c 206f 6e6c 7920 666f  s useful only fo
+000148d0: 7220 7468 6520 e280 9c63 6f6e 7374 616e  r the ...constan
+000148e0: 74e2 809d 2064 756d 6d79 5f63 6c61 7373  t... dummy_class
+000148f0: 6966 6965 725f 7374 7261 7465 6779 2e0a  ifier_strategy..
+00014900: 2020 2020 2020 2020 2020 2020 7265 7475              retu
+00014910: 726e 5f73 7479 6c65 3a0a 2020 2020 2020  rn_style:.      
+00014920: 2020 2020 2020 2020 2020 6966 2054 7275            if Tru
+00014930: 652c 2072 6574 7572 6e20 7374 796c 6572  e, return styler
+00014940: 206f 626a 6563 743b 2065 6c73 6520 7265   object; else re
+00014950: 7475 726e 2064 6174 6166 7261 6d65 0a20  turn dataframe. 
+00014960: 2020 2020 2020 2020 2020 2072 6f75 6e64             round
+00014970: 5f62 793a 0a20 2020 2020 2020 2020 2020  _by:.           
+00014980: 2020 2020 2074 6865 206e 756d 6265 7220       the number 
+00014990: 6f66 2064 6967 6974 7320 746f 2072 6f75  of digits to rou
+000149a0: 6e64 2062 793b 2069 6620 4e6f 6e65 2c20  nd by; if None, 
+000149b0: 7468 656e 2064 6f6e 2774 2072 6f75 6e64  then don't round
+000149c0: 0a20 2020 2020 2020 2022 2222 0a20 2020  .        """.   
+000149d0: 2020 2020 2072 6573 756c 7420 3d20 7064       result = pd
+000149e0: 2e44 6174 6146 7261 6d65 2e66 726f 6d5f  .DataFrame.from_
+000149f0: 6469 6374 287b 6b65 793a 2076 616c 7565  dict({key: value
+00014a00: 5b30 5d20 666f 7220 6b65 792c 2076 616c  [0] for key, val
+00014a10: 7565 2069 6e20 7365 6c66 2e61 6c6c 5f6d  ue in self.all_m
+00014a20: 6574 7269 6373 2e69 7465 6d73 2829 7d2c  etrics.items()},
+00014a30: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
 00014a40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014a50: 2020 2020 2020 2020 2020 2020 2020 206f                 o
-00014a60: 7269 656e 743d 2769 6e64 6578 272c 0a20  rient='index',. 
+00014a50: 2020 2020 2020 2020 206f 7269 656e 743d           orient=
+00014a60: 2769 6e64 6578 272c 0a20 2020 2020 2020  'index',.       
 00014a70: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00014a80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014a90: 2020 2020 2020 2063 6f6c 756d 6e73 3d5b         columns=[
-00014aa0: 2753 636f 7265 275d 290a 0a20 2020 2020  'Score'])..     
-00014ab0: 2020 2073 636f 7265 5f63 6f6c 756d 6e73     score_columns
-00014ac0: 203d 205b 2753 636f 7265 275d 0a0a 2020   = ['Score']..  
-00014ad0: 2020 2020 2020 6966 2064 756d 6d79 5f63        if dummy_c
-00014ae0: 6c61 7373 6966 6965 725f 7374 7261 7465  lassifier_strate
-00014af0: 6779 3a0a 2020 2020 2020 2020 2020 2020  gy:.            
-00014b00: 6966 2069 7369 6e73 7461 6e63 6528 6475  if isinstance(du
-00014b10: 6d6d 795f 636c 6173 7369 6669 6572 5f73  mmy_classifier_s
-00014b20: 7472 6174 6567 792c 2073 7472 293a 0a20  trategy, str):. 
-00014b30: 2020 2020 2020 2020 2020 2020 2020 2064                 d
-00014b40: 756d 6d79 5f63 6c61 7373 6966 6965 725f  ummy_classifier_
-00014b50: 7374 7261 7465 6779 203d 205b 6475 6d6d  strategy = [dumm
-00014b60: 795f 636c 6173 7369 6669 6572 5f73 7472  y_classifier_str
-00014b70: 6174 6567 795d 0a0a 2020 2020 2020 2020  ategy]..        
-00014b80: 2020 2020 666f 7220 7374 7261 7465 6779      for strategy
-00014b90: 2069 6e20 6475 6d6d 795f 636c 6173 7369   in dummy_classi
-00014ba0: 6669 6572 5f73 7472 6174 6567 793a 0a20  fier_strategy:. 
-00014bb0: 2020 2020 2020 2020 2020 2020 2020 2064                 d
-00014bc0: 756d 6d79 203d 2044 756d 6d79 436c 6173  ummy = DummyClas
-00014bd0: 7369 6669 6572 2873 7472 6174 6567 793d  sifier(strategy=
-00014be0: 7374 7261 7465 6779 2c20 636f 6e73 7461  strategy, consta
-00014bf0: 6e74 3d64 756d 6d79 5f63 6c61 7373 6966  nt=dummy_classif
-00014c00: 6965 725f 636f 6e73 7461 6e74 290a 2020  ier_constant).  
-00014c10: 2020 2020 2020 2020 2020 2020 2020 2320                # 
-00014c20: 6874 7470 733a 2f2f 7363 696b 6974 2d6c  https://scikit-l
-00014c30: 6561 726e 2e6f 7267 2f73 7461 626c 652f  earn.org/stable/
-00014c40: 6d6f 6475 6c65 732f 6765 6e65 7261 7465  modules/generate
-00014c50: 642f 736b 6c65 6172 6e2e 6475 6d6d 792e  d/sklearn.dummy.
-00014c60: 4475 6d6d 7943 6c61 7373 6966 6965 722e  DummyClassifier.
-00014c70: 6874 6d6c 0a20 2020 2020 2020 2020 2020  html.           
-00014c80: 2020 2020 2023 2022 416c 6c20 7374 7261       # "All stra
-00014c90: 7465 6769 6573 206d 616b 6520 7072 6564  tegies make pred
-00014ca0: 6963 7469 6f6e 7320 7468 6174 2069 676e  ictions that ign
-00014cb0: 6f72 6520 7468 6520 696e 7075 7420 6665  ore the input fe
-00014cc0: 6174 7572 6520 7661 6c75 6573 2070 6173  ature values pas
-00014cd0: 7365 6420 6173 2074 6865 2058 0a20 2020  sed as the X.   
-00014ce0: 2020 2020 2020 2020 2020 2020 2023 2061               # a
-00014cf0: 7267 756d 656e 7420 746f 2066 6974 2061  rgument to fit a
-00014d00: 6e64 2070 7265 6469 6374 2e20 5468 6520  nd predict. The 
-00014d10: 7072 6564 6963 7469 6f6e 732c 2068 6f77  predictions, how
-00014d20: 6576 6572 2c20 7479 7069 6361 6c6c 7920  ever, typically 
-00014d30: 6465 7065 6e64 206f 6e20 7661 6c75 6573  depend on values
-00014d40: 206f 6273 6572 7665 640a 2020 2020 2020   observed.      
-00014d50: 2020 2020 2020 2020 2020 2320 696e 2074            # in t
-00014d60: 6865 2079 2070 6172 616d 6574 6572 2070  he y parameter p
-00014d70: 6173 7365 6420 746f 2066 6974 2e22 0a20  assed to fit.". 
-00014d80: 2020 2020 2020 2020 2020 2020 2020 205f                 _
-00014d90: 203d 2064 756d 6d79 2e66 6974 2858 3d73   = dummy.fit(X=s
-00014da0: 656c 662e 5f61 6374 7561 6c5f 7661 6c75  elf._actual_valu
-00014db0: 6573 2c20 793d 7365 6c66 2e5f 6163 7475  es, y=self._actu
-00014dc0: 616c 5f76 616c 7565 7329 0a20 2020 2020  al_values).     
-00014dd0: 2020 2020 2020 2020 2020 2064 756d 6d79             dummy
-00014de0: 5f70 726f 6261 6269 6c69 7469 6573 203d  _probabilities =
-00014df0: 2064 756d 6d79 2e70 7265 6469 6374 5f70   dummy.predict_p
-00014e00: 726f 6261 2858 3d73 656c 662e 5f61 6374  roba(X=self._act
-00014e10: 7561 6c5f 7661 6c75 6573 290a 2020 2020  ual_values).    
-00014e20: 2020 2020 2020 2020 2020 2020 6475 6d6d              dumm
-00014e30: 795f 7072 6f62 6162 696c 6974 6965 7320  y_probabilities 
-00014e40: 3d20 6475 6d6d 795f 7072 6f62 6162 696c  = dummy_probabil
-00014e50: 6974 6965 735b 3a2c 2031 5d0a 2020 2020  ities[:, 1].    
-00014e60: 2020 2020 2020 2020 2020 2020 6475 6d6d              dumm
-00014e70: 795f 6576 616c 7561 746f 7220 3d20 5477  y_evaluator = Tw
-00014e80: 6f43 6c61 7373 4576 616c 7561 746f 7228  oClassEvaluator(
-00014e90: 6163 7475 616c 5f76 616c 7565 733d 7365  actual_values=se
-00014ea0: 6c66 2e5f 6163 7475 616c 5f76 616c 7565  lf._actual_value
-00014eb0: 732c 0a20 2020 2020 2020 2020 2020 2020  s,.             
+00014a90: 2063 6f6c 756d 6e73 3d5b 2753 636f 7265   columns=['Score
+00014aa0: 275d 290a 0a20 2020 2020 2020 2073 636f  '])..        sco
+00014ab0: 7265 5f63 6f6c 756d 6e73 203d 205b 2753  re_columns = ['S
+00014ac0: 636f 7265 275d 0a0a 2020 2020 2020 2020  core']..        
+00014ad0: 6966 2064 756d 6d79 5f63 6c61 7373 6966  if dummy_classif
+00014ae0: 6965 725f 7374 7261 7465 6779 3a0a 2020  ier_strategy:.  
+00014af0: 2020 2020 2020 2020 2020 6966 2069 7369            if isi
+00014b00: 6e73 7461 6e63 6528 6475 6d6d 795f 636c  nstance(dummy_cl
+00014b10: 6173 7369 6669 6572 5f73 7472 6174 6567  assifier_strateg
+00014b20: 792c 2073 7472 293a 0a20 2020 2020 2020  y, str):.       
+00014b30: 2020 2020 2020 2020 2064 756d 6d79 5f63           dummy_c
+00014b40: 6c61 7373 6966 6965 725f 7374 7261 7465  lassifier_strate
+00014b50: 6779 203d 205b 6475 6d6d 795f 636c 6173  gy = [dummy_clas
+00014b60: 7369 6669 6572 5f73 7472 6174 6567 795d  sifier_strategy]
+00014b70: 0a0a 2020 2020 2020 2020 2020 2020 666f  ..            fo
+00014b80: 7220 7374 7261 7465 6779 2069 6e20 6475  r strategy in du
+00014b90: 6d6d 795f 636c 6173 7369 6669 6572 5f73  mmy_classifier_s
+00014ba0: 7472 6174 6567 793a 0a20 2020 2020 2020  trategy:.       
+00014bb0: 2020 2020 2020 2020 2064 756d 6d79 203d           dummy =
+00014bc0: 2044 756d 6d79 436c 6173 7369 6669 6572   DummyClassifier
+00014bd0: 2873 7472 6174 6567 793d 7374 7261 7465  (strategy=strate
+00014be0: 6779 2c20 636f 6e73 7461 6e74 3d64 756d  gy, constant=dum
+00014bf0: 6d79 5f63 6c61 7373 6966 6965 725f 636f  my_classifier_co
+00014c00: 6e73 7461 6e74 290a 2020 2020 2020 2020  nstant).        
+00014c10: 2020 2020 2020 2020 2320 6874 7470 733a          # https:
+00014c20: 2f2f 7363 696b 6974 2d6c 6561 726e 2e6f  //scikit-learn.o
+00014c30: 7267 2f73 7461 626c 652f 6d6f 6475 6c65  rg/stable/module
+00014c40: 732f 6765 6e65 7261 7465 642f 736b 6c65  s/generated/skle
+00014c50: 6172 6e2e 6475 6d6d 792e 4475 6d6d 7943  arn.dummy.DummyC
+00014c60: 6c61 7373 6966 6965 722e 6874 6d6c 0a20  lassifier.html. 
+00014c70: 2020 2020 2020 2020 2020 2020 2020 2023                 #
+00014c80: 2022 416c 6c20 7374 7261 7465 6769 6573   "All strategies
+00014c90: 206d 616b 6520 7072 6564 6963 7469 6f6e   make prediction
+00014ca0: 7320 7468 6174 2069 676e 6f72 6520 7468  s that ignore th
+00014cb0: 6520 696e 7075 7420 6665 6174 7572 6520  e input feature 
+00014cc0: 7661 6c75 6573 2070 6173 7365 6420 6173  values passed as
+00014cd0: 2074 6865 2058 0a20 2020 2020 2020 2020   the X.         
+00014ce0: 2020 2020 2020 2023 2061 7267 756d 656e         # argumen
+00014cf0: 7420 746f 2066 6974 2061 6e64 2070 7265  t to fit and pre
+00014d00: 6469 6374 2e20 5468 6520 7072 6564 6963  dict. The predic
+00014d10: 7469 6f6e 732c 2068 6f77 6576 6572 2c20  tions, however, 
+00014d20: 7479 7069 6361 6c6c 7920 6465 7065 6e64  typically depend
+00014d30: 206f 6e20 7661 6c75 6573 206f 6273 6572   on values obser
+00014d40: 7665 640a 2020 2020 2020 2020 2020 2020  ved.            
+00014d50: 2020 2020 2320 696e 2074 6865 2079 2070      # in the y p
+00014d60: 6172 616d 6574 6572 2070 6173 7365 6420  arameter passed 
+00014d70: 746f 2066 6974 2e22 0a20 2020 2020 2020  to fit.".       
+00014d80: 2020 2020 2020 2020 205f 203d 2064 756d           _ = dum
+00014d90: 6d79 2e66 6974 2858 3d73 656c 662e 5f61  my.fit(X=self._a
+00014da0: 6374 7561 6c5f 7661 6c75 6573 2c20 793d  ctual_values, y=
+00014db0: 7365 6c66 2e5f 6163 7475 616c 5f76 616c  self._actual_val
+00014dc0: 7565 7329 0a20 2020 2020 2020 2020 2020  ues).           
+00014dd0: 2020 2020 2064 756d 6d79 5f70 726f 6261       dummy_proba
+00014de0: 6269 6c69 7469 6573 203d 2064 756d 6d79  bilities = dummy
+00014df0: 2e70 7265 6469 6374 5f70 726f 6261 2858  .predict_proba(X
+00014e00: 3d73 656c 662e 5f61 6374 7561 6c5f 7661  =self._actual_va
+00014e10: 6c75 6573 290a 2020 2020 2020 2020 2020  lues).          
+00014e20: 2020 2020 2020 6475 6d6d 795f 7072 6f62        dummy_prob
+00014e30: 6162 696c 6974 6965 7320 3d20 6475 6d6d  abilities = dumm
+00014e40: 795f 7072 6f62 6162 696c 6974 6965 735b  y_probabilities[
+00014e50: 3a2c 2031 5d0a 2020 2020 2020 2020 2020  :, 1].          
+00014e60: 2020 2020 2020 6475 6d6d 795f 6576 616c        dummy_eval
+00014e70: 7561 746f 7220 3d20 5477 6f43 6c61 7373  uator = TwoClass
+00014e80: 4576 616c 7561 746f 7228 6163 7475 616c  Evaluator(actual
+00014e90: 5f76 616c 7565 733d 7365 6c66 2e5f 6163  _values=self._ac
+00014ea0: 7475 616c 5f76 616c 7565 732c 0a20 2020  tual_values,.   
+00014eb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00014ec0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00014ed0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014ee0: 2020 2020 2020 2070 7265 6469 6374 6564         predicted
-00014ef0: 5f73 636f 7265 733d 6475 6d6d 795f 7072  _scores=dummy_pr
-00014f00: 6f62 6162 696c 6974 6965 732c 0a20 2020  obabilities,.   
+00014ee0: 2070 7265 6469 6374 6564 5f73 636f 7265   predicted_score
+00014ef0: 733d 6475 6d6d 795f 7072 6f62 6162 696c  s=dummy_probabil
+00014f00: 6974 6965 732c 0a20 2020 2020 2020 2020  ities,.         
 00014f10: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00014f20: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014f30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014f40: 2073 636f 7265 5f74 6872 6573 686f 6c64   score_threshold
-00014f50: 3d73 656c 662e 7363 6f72 655f 7468 7265  =self.score_thre
-00014f60: 7368 6f6c 6429 0a0a 2020 2020 2020 2020  shold)..        
-00014f70: 2020 2020 2020 2020 6475 6d6d 795f 7363          dummy_sc
-00014f80: 6f72 6573 203d 2064 756d 6d79 5f65 7661  ores = dummy_eva
-00014f90: 6c75 6174 6f72 2e61 6c6c 5f6d 6574 7269  luator.all_metri
-00014fa0: 6373 5f64 6628 7265 7475 726e 5f65 7870  cs_df(return_exp
-00014fb0: 6c61 6e61 7469 6f6e 733d 4661 6c73 652c  lanations=False,
-00014fc0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00014f30: 2020 2020 2020 2020 2020 2073 636f 7265             score
+00014f40: 5f74 6872 6573 686f 6c64 3d73 656c 662e  _threshold=self.
+00014f50: 7363 6f72 655f 7468 7265 7368 6f6c 6429  score_threshold)
+00014f60: 0a0a 2020 2020 2020 2020 2020 2020 2020  ..              
+00014f70: 2020 6475 6d6d 795f 7363 6f72 6573 203d    dummy_scores =
+00014f80: 2064 756d 6d79 5f65 7661 6c75 6174 6f72   dummy_evaluator
+00014f90: 2e61 6c6c 5f6d 6574 7269 6373 5f64 6628  .all_metrics_df(
+00014fa0: 7265 7475 726e 5f65 7870 6c61 6e61 7469  return_explanati
+00014fb0: 6f6e 733d 4661 6c73 652c 0a20 2020 2020  ons=False,.     
+00014fc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00014fd0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00014fe0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00014ff0: 2020 2020 2020 2020 2020 2020 2020 2064                 d
-00015000: 756d 6d79 5f63 6c61 7373 6966 6965 725f  ummy_classifier_
-00015010: 7374 7261 7465 6779 3d4e 6f6e 652c 0a20  strategy=None,. 
+00014ff0: 2020 2020 2020 2020 2064 756d 6d79 5f63           dummy_c
+00015000: 6c61 7373 6966 6965 725f 7374 7261 7465  lassifier_strate
+00015010: 6779 3d4e 6f6e 652c 0a20 2020 2020 2020  gy=None,.       
 00015020: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00015030: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00015040: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015050: 2020 2020 2020 2020 2020 2020 2072 6574               ret
-00015060: 7572 6e5f 7374 796c 653d 4661 6c73 6529  urn_style=False)
-00015070: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00015080: 2063 6f6c 756d 6e5f 6e61 6d65 203d 2066   column_name = f
-00015090: 2244 756d 6d79 2028 7b73 7472 6174 6567  "Dummy ({strateg
-000150a0: 797d 2922 0a20 2020 2020 2020 2020 2020  y})".           
-000150b0: 2020 2020 2073 636f 7265 5f63 6f6c 756d       score_colum
-000150c0: 6e73 203d 2073 636f 7265 5f63 6f6c 756d  ns = score_colum
-000150d0: 6e73 202b 205b 636f 6c75 6d6e 5f6e 616d  ns + [column_nam
-000150e0: 655d 0a20 2020 2020 2020 2020 2020 2020  e].             
-000150f0: 2020 2064 756d 6d79 5f73 636f 7265 7320     dummy_scores 
-00015100: 3d20 6475 6d6d 795f 7363 6f72 6573 2e72  = dummy_scores.r
-00015110: 656e 616d 6528 636f 6c75 6d6e 733d 7b27  ename(columns={'
-00015120: 5363 6f72 6527 3a20 636f 6c75 6d6e 5f6e  Score': column_n
-00015130: 616d 657d 290a 2020 2020 2020 2020 2020  ame}).          
-00015140: 2020 2020 2020 7265 7375 6c74 203d 2070        result = p
-00015150: 642e 636f 6e63 6174 285b 7265 7375 6c74  d.concat([result
-00015160: 2c20 6475 6d6d 795f 7363 6f72 6573 5d2c  , dummy_scores],
-00015170: 2061 7869 733d 3129 0a0a 2020 2020 2020   axis=1)..      
-00015180: 2020 6966 2072 6574 7572 6e5f 6578 706c    if return_expl
-00015190: 616e 6174 696f 6e73 3a0a 2020 2020 2020  anations:.      
-000151a0: 2020 2020 2020 6578 706c 616e 6174 696f        explanatio
-000151b0: 6e73 203d 2070 642e 4461 7461 4672 616d  ns = pd.DataFram
-000151c0: 652e 6672 6f6d 5f64 6963 7428 7b6b 6579  e.from_dict({key
-000151d0: 3a20 7661 6c75 655b 315d 2066 6f72 206b  : value[1] for k
-000151e0: 6579 2c20 7661 6c75 6520 696e 2073 656c  ey, value in sel
-000151f0: 662e 616c 6c5f 6d65 7472 6963 732e 6974  f.all_metrics.it
-00015200: 656d 7328 297d 2c0a 2020 2020 2020 2020  ems()},.        
+00015050: 2020 2020 2020 2072 6574 7572 6e5f 7374         return_st
+00015060: 796c 653d 4661 6c73 6529 0a20 2020 2020  yle=False).     
+00015070: 2020 2020 2020 2020 2020 2063 6f6c 756d             colum
+00015080: 6e5f 6e61 6d65 203d 2066 2244 756d 6d79  n_name = f"Dummy
+00015090: 2028 7b73 7472 6174 6567 797d 2922 0a20   ({strategy})". 
+000150a0: 2020 2020 2020 2020 2020 2020 2020 2073                 s
+000150b0: 636f 7265 5f63 6f6c 756d 6e73 203d 2073  core_columns = s
+000150c0: 636f 7265 5f63 6f6c 756d 6e73 202b 205b  core_columns + [
+000150d0: 636f 6c75 6d6e 5f6e 616d 655d 0a20 2020  column_name].   
+000150e0: 2020 2020 2020 2020 2020 2020 2064 756d               dum
+000150f0: 6d79 5f73 636f 7265 7320 3d20 6475 6d6d  my_scores = dumm
+00015100: 795f 7363 6f72 6573 2e72 656e 616d 6528  y_scores.rename(
+00015110: 636f 6c75 6d6e 733d 7b27 5363 6f72 6527  columns={'Score'
+00015120: 3a20 636f 6c75 6d6e 5f6e 616d 657d 290a  : column_name}).
+00015130: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00015140: 7265 7375 6c74 203d 2070 642e 636f 6e63  result = pd.conc
+00015150: 6174 285b 7265 7375 6c74 2c20 6475 6d6d  at([result, dumm
+00015160: 795f 7363 6f72 6573 5d2c 2061 7869 733d  y_scores], axis=
+00015170: 3129 0a0a 2020 2020 2020 2020 6966 2072  1)..        if r
+00015180: 6574 7572 6e5f 6578 706c 616e 6174 696f  eturn_explanatio
+00015190: 6e73 3a0a 2020 2020 2020 2020 2020 2020  ns:.            
+000151a0: 6578 706c 616e 6174 696f 6e73 203d 2070  explanations = p
+000151b0: 642e 4461 7461 4672 616d 652e 6672 6f6d  d.DataFrame.from
+000151c0: 5f64 6963 7428 7b6b 6579 3a20 7661 6c75  _dict({key: valu
+000151d0: 655b 315d 2066 6f72 206b 6579 2c20 7661  e[1] for key, va
+000151e0: 6c75 6520 696e 2073 656c 662e 616c 6c5f  lue in self.all_
+000151f0: 6d65 7472 6963 732e 6974 656d 7328 297d  metrics.items()}
+00015200: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
 00015210: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00015220: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015230: 2020 2020 2020 2020 2020 6f72 6965 6e74            orient
-00015240: 3d27 696e 6465 7827 2c0a 2020 2020 2020  ='index',.      
+00015230: 2020 2020 6f72 6965 6e74 3d27 696e 6465      orient='inde
+00015240: 7827 2c0a 2020 2020 2020 2020 2020 2020  x',.            
 00015250: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00015260: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015270: 2020 2020 2020 2020 2020 2020 636f 6c75              colu
-00015280: 6d6e 733d 5b27 4578 706c 616e 6174 696f  mns=['Explanatio
-00015290: 6e27 5d29 0a20 2020 2020 2020 2020 2020  n']).           
-000152a0: 2072 6573 756c 7420 3d20 7064 2e63 6f6e   result = pd.con
-000152b0: 6361 7428 5b72 6573 756c 742c 2065 7870  cat([result, exp
-000152c0: 6c61 6e61 7469 6f6e 735d 2c20 6178 6973  lanations], axis
-000152d0: 3d31 290a 0a20 2020 2020 2020 2069 6620  =1)..        if 
-000152e0: 726f 756e 645f 6279 3a0a 2020 2020 2020  round_by:.      
-000152f0: 2020 2020 2020 666f 7220 636f 6c75 6d6e        for column
-00015300: 2069 6e20 7363 6f72 655f 636f 6c75 6d6e   in score_column
-00015310: 733a 0a20 2020 2020 2020 2020 2020 2020  s:.             
-00015320: 2020 2072 6573 756c 745b 636f 6c75 6d6e     result[column
-00015330: 5d20 3d20 7265 7375 6c74 5b63 6f6c 756d  ] = result[colum
-00015340: 6e5d 2e72 6f75 6e64 2872 6f75 6e64 5f62  n].round(round_b
-00015350: 7929 0a0a 2020 2020 2020 2020 6966 2072  y)..        if r
-00015360: 6574 7572 6e5f 7374 796c 653a 0a20 2020  eturn_style:.   
-00015370: 2020 2020 2020 2020 2073 7562 7365 745f           subset_
-00015380: 7363 6f72 6573 203d 205b 7820 666f 7220  scores = [x for 
-00015390: 7820 696e 2072 6573 756c 742e 696e 6465  x in result.inde
-000153a0: 782e 7661 6c75 6573 2069 6620 7820 213d  x.values if x !=
-000153b0: 2027 546f 7461 6c20 4f62 7365 7276 6174   'Total Observat
-000153c0: 696f 6e73 275d 0a0a 2020 2020 2020 2020  ions']..        
-000153d0: 2020 2020 7375 6273 6574 5f73 636f 7265      subset_score
-000153e0: 7320 3d20 7064 2e49 6e64 6578 536c 6963  s = pd.IndexSlic
-000153f0: 655b 7265 7375 6c74 2e6c 6f63 5b73 7562  e[result.loc[sub
-00015400: 7365 745f 7363 6f72 6573 2c20 3a5d 2e69  set_scores, :].i
-00015410: 6e64 6578 2c20 7363 6f72 655f 636f 6c75  ndex, score_colu
-00015420: 6d6e 735d 0a20 2020 2020 2020 2020 2020  mns].           
-00015430: 2073 7562 7365 745f 6e65 6761 7469 7665   subset_negative
-00015440: 5f62 6164 203d 2070 642e 496e 6465 7853  _bad = pd.IndexS
-00015450: 6c69 6365 5b72 6573 756c 742e 6c6f 635b  lice[result.loc[
-00015460: 5b27 4661 6c73 6520 506f 7369 7469 7665  ['False Positive
-00015470: 2052 6174 6527 2c0a 2020 2020 2020 2020   Rate',.        
+00015270: 2020 2020 2020 636f 6c75 6d6e 733d 5b27        columns=['
+00015280: 4578 706c 616e 6174 696f 6e27 5d29 0a20  Explanation']). 
+00015290: 2020 2020 2020 2020 2020 2072 6573 756c             resul
+000152a0: 7420 3d20 7064 2e63 6f6e 6361 7428 5b72  t = pd.concat([r
+000152b0: 6573 756c 742c 2065 7870 6c61 6e61 7469  esult, explanati
+000152c0: 6f6e 735d 2c20 6178 6973 3d31 290a 0a20  ons], axis=1).. 
+000152d0: 2020 2020 2020 2069 6620 726f 756e 645f         if round_
+000152e0: 6279 3a0a 2020 2020 2020 2020 2020 2020  by:.            
+000152f0: 666f 7220 636f 6c75 6d6e 2069 6e20 7363  for column in sc
+00015300: 6f72 655f 636f 6c75 6d6e 733a 0a20 2020  ore_columns:.   
+00015310: 2020 2020 2020 2020 2020 2020 2072 6573               res
+00015320: 756c 745b 636f 6c75 6d6e 5d20 3d20 7265  ult[column] = re
+00015330: 7375 6c74 5b63 6f6c 756d 6e5d 2e72 6f75  sult[column].rou
+00015340: 6e64 2872 6f75 6e64 5f62 7929 0a0a 2020  nd(round_by)..  
+00015350: 2020 2020 2020 6966 2072 6574 7572 6e5f        if return_
+00015360: 7374 796c 653a 0a20 2020 2020 2020 2020  style:.         
+00015370: 2020 2073 7562 7365 745f 7363 6f72 6573     subset_scores
+00015380: 203d 205b 7820 666f 7220 7820 696e 2072   = [x for x in r
+00015390: 6573 756c 742e 696e 6465 782e 7661 6c75  esult.index.valu
+000153a0: 6573 2069 6620 7820 213d 2027 546f 7461  es if x != 'Tota
+000153b0: 6c20 4f62 7365 7276 6174 696f 6e73 275d  l Observations']
+000153c0: 0a0a 2020 2020 2020 2020 2020 2020 7375  ..            su
+000153d0: 6273 6574 5f73 636f 7265 7320 3d20 7064  bset_scores = pd
+000153e0: 2e49 6e64 6578 536c 6963 655b 7265 7375  .IndexSlice[resu
+000153f0: 6c74 2e6c 6f63 5b73 7562 7365 745f 7363  lt.loc[subset_sc
+00015400: 6f72 6573 2c20 3a5d 2e69 6e64 6578 2c20  ores, :].index, 
+00015410: 7363 6f72 655f 636f 6c75 6d6e 735d 0a20  score_columns]. 
+00015420: 2020 2020 2020 2020 2020 2073 7562 7365             subse
+00015430: 745f 6e65 6761 7469 7665 5f62 6164 203d  t_negative_bad =
+00015440: 2070 642e 496e 6465 7853 6c69 6365 5b72   pd.IndexSlice[r
+00015450: 6573 756c 742e 6c6f 635b 5b27 4661 6c73  esult.loc[['Fals
+00015460: 6520 506f 7369 7469 7665 2052 6174 6527  e Positive Rate'
+00015470: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
 00015480: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00015490: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000154a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000154b0: 2020 2020 2746 616c 7365 204e 6567 6174      'False Negat
-000154c0: 6976 6520 5261 7465 275d 2c20 7363 6f72  ive Rate'], scor
-000154d0: 655f 636f 6c75 6d6e 735d 2e69 6e64 6578  e_columns].index
-000154e0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+000154a0: 2020 2020 2020 2020 2020 2020 2020 2746                'F
+000154b0: 616c 7365 204e 6567 6174 6976 6520 5261  alse Negative Ra
+000154c0: 7465 275d 2c20 7363 6f72 655f 636f 6c75  te'], score_colu
+000154d0: 6d6e 735d 2e69 6e64 6578 2c0a 2020 2020  mns].index,.    
+000154e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000154f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015500: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015510: 2020 7363 6f72 655f 636f 6c75 6d6e 735d    score_columns]
-00015520: 0a20 2020 2020 2020 2020 2020 2073 7562  .            sub
-00015530: 7365 745f 7365 636f 6e64 6172 7920 3d20  set_secondary = 
-00015540: 7064 2e49 6e64 6578 536c 6963 655b 7265  pd.IndexSlice[re
-00015550: 7375 6c74 2e6c 6f63 5b5b 2741 6363 7572  sult.loc[['Accur
-00015560: 6163 7927 2c20 2745 7272 6f72 2052 6174  acy', 'Error Rat
-00015570: 6527 2c20 2725 2050 6f73 6974 6976 6527  e', '% Positive'
-00015580: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
+00015500: 2020 2020 2020 2020 2020 2020 7363 6f72              scor
+00015510: 655f 636f 6c75 6d6e 735d 0a20 2020 2020  e_columns].     
+00015520: 2020 2020 2020 2073 7562 7365 745f 7365         subset_se
+00015530: 636f 6e64 6172 7920 3d20 7064 2e49 6e64  condary = pd.Ind
+00015540: 6578 536c 6963 655b 7265 7375 6c74 2e6c  exSlice[result.l
+00015550: 6f63 5b5b 2741 6363 7572 6163 7927 2c20  oc[['Accuracy', 
+00015560: 2745 7272 6f72 2052 6174 6527 2c20 2725  'Error Rate', '%
+00015570: 2050 6f73 6974 6976 6527 5d2c 0a20 2020   Positive'],.   
+00015580: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00015590: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000155a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000155b0: 2020 2020 2020 2020 2020 2073 636f 7265             score
-000155c0: 5f63 6f6c 756d 6e73 5d2e 696e 6465 782c  _columns].index,
-000155d0: 2073 636f 7265 5f63 6f6c 756d 6e73 5d0a   score_columns].
-000155e0: 2020 2020 2020 2020 2020 2020 7375 6273              subs
-000155f0: 6574 5f74 6f74 616c 5f6f 6273 6572 7661  et_total_observa
-00015600: 7469 6f6e 7320 3d20 7064 2e49 6e64 6578  tions = pd.Index
-00015610: 536c 6963 655b 7265 7375 6c74 2e6c 6f63  Slice[result.loc
-00015620: 5b5b 2754 6f74 616c 204f 6273 6572 7661  [['Total Observa
-00015630: 7469 6f6e 7327 5d2c 0a20 2020 2020 2020  tions'],.       
+000155b0: 2020 2020 2073 636f 7265 5f63 6f6c 756d       score_colum
+000155c0: 6e73 5d2e 696e 6465 782c 2073 636f 7265  ns].index, score
+000155d0: 5f63 6f6c 756d 6e73 5d0a 2020 2020 2020  _columns].      
+000155e0: 2020 2020 2020 7375 6273 6574 5f74 6f74        subset_tot
+000155f0: 616c 5f6f 6273 6572 7661 7469 6f6e 7320  al_observations 
+00015600: 3d20 7064 2e49 6e64 6578 536c 6963 655b  = pd.IndexSlice[
+00015610: 7265 7375 6c74 2e6c 6f63 5b5b 2754 6f74  result.loc[['Tot
+00015620: 616c 204f 6273 6572 7661 7469 6f6e 7327  al Observations'
+00015630: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
 00015640: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00015650: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00015660: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015670: 2020 2020 2020 2020 2020 7363 6f72 655f            score_
-00015680: 636f 6c75 6d6e 735d 2e69 6e64 6578 2c20  columns].index, 
-00015690: 7363 6f72 655f 636f 6c75 6d6e 735d 0a0a  score_columns]..
-000156a0: 2020 2020 2020 2020 2020 2020 7265 7375              resu
-000156b0: 6c74 203d 2072 6573 756c 742e 7374 796c  lt = result.styl
-000156c0: 650a 0a20 2020 2020 2020 2020 2020 2069  e..            i
-000156d0: 6620 726f 756e 645f 6279 3a0a 2020 2020  f round_by:.    
-000156e0: 2020 2020 2020 2020 2020 2020 7265 7375              resu
-000156f0: 6c74 203d 2072 6573 756c 742e 666f 726d  lt = result.form
-00015700: 6174 2870 7265 6369 7369 6f6e 3d72 6f75  at(precision=rou
-00015710: 6e64 5f62 7929 0a0a 2020 2020 2020 2020  nd_by)..        
-00015720: 2020 2020 7265 7375 6c74 203d 2072 6573      result = res
-00015730: 756c 742e 666f 726d 6174 2873 7562 7365  ult.format(subse
-00015740: 743d 7375 6273 6574 5f74 6f74 616c 5f6f  t=subset_total_o
-00015750: 6273 6572 7661 7469 6f6e 732c 0a20 2020  bservations,.   
+00015670: 2020 2020 7363 6f72 655f 636f 6c75 6d6e      score_column
+00015680: 735d 2e69 6e64 6578 2c20 7363 6f72 655f  s].index, score_
+00015690: 636f 6c75 6d6e 735d 0a0a 2020 2020 2020  columns]..      
+000156a0: 2020 2020 2020 7265 7375 6c74 203d 2072        result = r
+000156b0: 6573 756c 742e 7374 796c 650a 0a20 2020  esult.style..   
+000156c0: 2020 2020 2020 2020 2069 6620 726f 756e           if roun
+000156d0: 645f 6279 3a0a 2020 2020 2020 2020 2020  d_by:.          
+000156e0: 2020 2020 2020 7265 7375 6c74 203d 2072        result = r
+000156f0: 6573 756c 742e 666f 726d 6174 2870 7265  esult.format(pre
+00015700: 6369 7369 6f6e 3d72 6f75 6e64 5f62 7929  cision=round_by)
+00015710: 0a0a 2020 2020 2020 2020 2020 2020 7265  ..            re
+00015720: 7375 6c74 203d 2072 6573 756c 742e 666f  sult = result.fo
+00015730: 726d 6174 2873 7562 7365 743d 7375 6273  rmat(subset=subs
+00015740: 6574 5f74 6f74 616c 5f6f 6273 6572 7661  et_total_observa
+00015750: 7469 6f6e 732c 0a20 2020 2020 2020 2020  tions,.         
 00015760: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015770: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015780: 7468 6f75 7361 6e64 733d 272c 272c 0a20  thousands=',',. 
+00015770: 2020 2020 2020 2020 2020 7468 6f75 7361            thousa
+00015780: 6e64 733d 272c 272c 0a20 2020 2020 2020  nds=',',.       
 00015790: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000157a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000157b0: 2020 7072 6563 6973 696f 6e3d 3029 0a0a    precision=0)..
-000157c0: 2020 2020 2020 2020 2020 2020 7265 7375              resu
-000157d0: 6c74 203d 2072 6573 756c 742e 205c 0a20  lt = result. \. 
-000157e0: 2020 2020 2020 2020 2020 2020 2020 2062                 b
-000157f0: 6172 2873 7562 7365 743d 7375 6273 6574  ar(subset=subset
-00015800: 5f73 636f 7265 732c 2063 6f6c 6f72 3d68  _scores, color=h
-00015810: 636f 6c6f 722e 436f 6c6f 7273 2e50 4947  color.Colors.PIG
-00015820: 4d45 4e54 5f47 5245 454e 2e76 616c 7565  MENT_GREEN.value
-00015830: 2c20 766d 696e 3d30 2c20 766d 6178 3d31  , vmin=0, vmax=1
-00015840: 292e 205c 0a20 2020 2020 2020 2020 2020  ). \.           
-00015850: 2020 2020 2062 6172 2873 7562 7365 743d       bar(subset=
-00015860: 7375 6273 6574 5f6e 6567 6174 6976 655f  subset_negative_
-00015870: 6261 642c 2063 6f6c 6f72 3d68 636f 6c6f  bad, color=hcolo
-00015880: 722e 436f 6c6f 7273 2e50 4f50 5059 2e76  r.Colors.POPPY.v
-00015890: 616c 7565 2c20 766d 696e 3d30 2c20 766d  alue, vmin=0, vm
-000158a0: 6178 3d31 292e 205c 0a20 2020 2020 2020  ax=1). \.       
-000158b0: 2020 2020 2020 2020 2062 6172 2873 7562           bar(sub
-000158c0: 7365 743d 7375 6273 6574 5f73 6563 6f6e  set=subset_secon
-000158d0: 6461 7279 2c20 636f 6c6f 723d 6863 6f6c  dary, color=hcol
-000158e0: 6f72 2e47 5241 592c 2076 6d69 6e3d 302c  or.GRAY, vmin=0,
-000158f0: 2076 6d61 783d 3129 0a0a 2020 2020 2020   vmax=1)..      
-00015900: 2020 7265 7475 726e 2072 6573 756c 740a    return result.
-00015910: 0a20 2020 2064 6566 2070 6c6f 745f 636f  .    def plot_co
-00015920: 6e66 7573 696f 6e5f 6d61 7472 6978 2873  nfusion_matrix(s
-00015930: 656c 6629 3a0a 2020 2020 2020 2020 2222  elf):.        ""
-00015940: 2250 6c6f 7473 2061 2068 6561 746d 6170  "Plots a heatmap
-00015950: 206f 6620 7468 6520 636f 6e66 7573 696f   of the confusio
-00015960: 6e20 6d61 7472 6978 2e22 2222 0a20 2020  n matrix.""".   
-00015970: 2020 2020 206c 6162 656c 7320 3d20 6e70       labels = np
-00015980: 2e61 7272 6179 285b 5b66 2754 7275 6520  .array([[f'True 
-00015990: 4e65 6761 7469 7665 735c 6e7b 7365 6c66  Negatives\n{self
-000159a0: 2e5f 7472 7565 5f6e 6567 6174 6976 6573  ._true_negatives
-000159b0: 7d5c 6e7b 7365 6c66 2e5f 7472 7565 5f6e  }\n{self._true_n
-000159c0: 6567 6174 6976 6573 202f 2073 656c 662e  egatives / self.
-000159d0: 7361 6d70 6c65 5f73 697a 653a 2e31 257d  sample_size:.1%}
-000159e0: 272c 2020 2320 7079 6c69 6e74 3a20 6469  ',  # pylint: di
-000159f0: 7361 626c 653d 6c69 6e65 2d74 6f6f 2d6c  sable=line-too-l
-00015a00: 6f6e 6720 2023 206e 6f71 610a 2020 2020  ong  # noqa.    
+000157a0: 2020 2020 2020 2020 2020 2020 7072 6563              prec
+000157b0: 6973 696f 6e3d 3029 0a0a 2020 2020 2020  ision=0)..      
+000157c0: 2020 2020 2020 7265 7375 6c74 203d 2072        result = r
+000157d0: 6573 756c 742e 205c 0a20 2020 2020 2020  esult. \.       
+000157e0: 2020 2020 2020 2020 2062 6172 2873 7562           bar(sub
+000157f0: 7365 743d 7375 6273 6574 5f73 636f 7265  set=subset_score
+00015800: 732c 2063 6f6c 6f72 3d68 636f 6c6f 722e  s, color=hcolor.
+00015810: 436f 6c6f 7273 2e50 4947 4d45 4e54 5f47  Colors.PIGMENT_G
+00015820: 5245 454e 2e76 616c 7565 2c20 766d 696e  REEN.value, vmin
+00015830: 3d30 2c20 766d 6178 3d31 292e 205c 0a20  =0, vmax=1). \. 
+00015840: 2020 2020 2020 2020 2020 2020 2020 2062                 b
+00015850: 6172 2873 7562 7365 743d 7375 6273 6574  ar(subset=subset
+00015860: 5f6e 6567 6174 6976 655f 6261 642c 2063  _negative_bad, c
+00015870: 6f6c 6f72 3d68 636f 6c6f 722e 436f 6c6f  olor=hcolor.Colo
+00015880: 7273 2e50 4f50 5059 2e76 616c 7565 2c20  rs.POPPY.value, 
+00015890: 766d 696e 3d30 2c20 766d 6178 3d31 292e  vmin=0, vmax=1).
+000158a0: 205c 0a20 2020 2020 2020 2020 2020 2020   \.             
+000158b0: 2020 2062 6172 2873 7562 7365 743d 7375     bar(subset=su
+000158c0: 6273 6574 5f73 6563 6f6e 6461 7279 2c20  bset_secondary, 
+000158d0: 636f 6c6f 723d 6863 6f6c 6f72 2e47 5241  color=hcolor.GRA
+000158e0: 592c 2076 6d69 6e3d 302c 2076 6d61 783d  Y, vmin=0, vmax=
+000158f0: 3129 0a0a 2020 2020 2020 2020 7265 7475  1)..        retu
+00015900: 726e 2072 6573 756c 740a 0a20 2020 2064  rn result..    d
+00015910: 6566 2070 6c6f 745f 636f 6e66 7573 696f  ef plot_confusio
+00015920: 6e5f 6d61 7472 6978 2873 656c 6629 3a0a  n_matrix(self):.
+00015930: 2020 2020 2020 2020 2222 2250 6c6f 7473          """Plots
+00015940: 2061 2068 6561 746d 6170 206f 6620 7468   a heatmap of th
+00015950: 6520 636f 6e66 7573 696f 6e20 6d61 7472  e confusion matr
+00015960: 6978 2e22 2222 0a20 2020 2020 2020 206c  ix.""".        l
+00015970: 6162 656c 7320 3d20 6e70 2e61 7272 6179  abels = np.array
+00015980: 285b 5b66 2754 7275 6520 4e65 6761 7469  ([[f'True Negati
+00015990: 7665 735c 6e7b 7365 6c66 2e5f 7472 7565  ves\n{self._true
+000159a0: 5f6e 6567 6174 6976 6573 7d5c 6e7b 7365  _negatives}\n{se
+000159b0: 6c66 2e5f 7472 7565 5f6e 6567 6174 6976  lf._true_negativ
+000159c0: 6573 202f 2073 656c 662e 7361 6d70 6c65  es / self.sample
+000159d0: 5f73 697a 653a 2e31 257d 272c 2020 2320  _size:.1%}',  # 
+000159e0: 7079 6c69 6e74 3a20 6469 7361 626c 653d  pylint: disable=
+000159f0: 6c69 6e65 2d74 6f6f 2d6c 6f6e 6720 2023  line-too-long  #
+00015a00: 206e 6f71 610a 2020 2020 2020 2020 2020   noqa.          
 00015a10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015a20: 2020 2020 2020 2020 6627 4661 6c73 6520          f'False 
-00015a30: 506f 7369 7469 7665 735c 6e7b 7365 6c66  Positives\n{self
-00015a40: 2e5f 6661 6c73 655f 706f 7369 7469 7665  ._false_positive
-00015a50: 737d 5c6e 7b73 656c 662e 5f66 616c 7365  s}\n{self._false
-00015a60: 5f70 6f73 6974 6976 6573 202f 2073 656c  _positives / sel
-00015a70: 662e 7361 6d70 6c65 5f73 697a 653a 2e31  f.sample_size:.1
-00015a80: 257d 275d 2c20 2023 2070 796c 696e 743a  %}'],  # pylint:
-00015a90: 2064 6973 6162 6c65 3d6c 696e 652d 746f   disable=line-to
-00015aa0: 6f2d 6c6f 6e67 2020 2320 6e6f 7161 0a20  o-long  # noqa. 
+00015a20: 2020 6627 4661 6c73 6520 506f 7369 7469    f'False Positi
+00015a30: 7665 735c 6e7b 7365 6c66 2e5f 6661 6c73  ves\n{self._fals
+00015a40: 655f 706f 7369 7469 7665 737d 5c6e 7b73  e_positives}\n{s
+00015a50: 656c 662e 5f66 616c 7365 5f70 6f73 6974  elf._false_posit
+00015a60: 6976 6573 202f 2073 656c 662e 7361 6d70  ives / self.samp
+00015a70: 6c65 5f73 697a 653a 2e31 257d 275d 2c20  le_size:.1%}'], 
+00015a80: 2023 2070 796c 696e 743a 2064 6973 6162   # pylint: disab
+00015a90: 6c65 3d6c 696e 652d 746f 6f2d 6c6f 6e67  le=line-too-long
+00015aa0: 2020 2320 6e6f 7161 0a20 2020 2020 2020    # noqa.       
 00015ab0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00015ac0: 2020 2020 2020 2020 2020 5b66 2746 616c            [f'Fal
-00015ad0: 7365 204e 6567 6174 6976 6573 5c6e 7b73  se Negatives\n{s
-00015ae0: 656c 662e 5f66 616c 7365 5f6e 6567 6174  elf._false_negat
-00015af0: 6976 6573 7d5c 6e7b 7365 6c66 2e5f 6661  ives}\n{self._fa
-00015b00: 6c73 655f 6e65 6761 7469 7665 7320 2f20  lse_negatives / 
-00015b10: 7365 6c66 2e73 616d 706c 655f 7369 7a65  self.sample_size
-00015b20: 3a2e 3125 7d27 2c20 2023 2070 796c 696e  :.1%}',  # pylin
-00015b30: 743a 2064 6973 6162 6c65 3d6c 696e 652d  t: disable=line-
-00015b40: 746f 6f2d 6c6f 6e67 2020 2320 6e6f 7161  too-long  # noqa
-00015b50: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00015b60: 2020 2020 2020 2020 2020 2020 2066 2754               f'T
-00015b70: 7275 6520 506f 7369 7469 7665 735c 6e7b  rue Positives\n{
-00015b80: 7365 6c66 2e5f 7472 7565 5f70 6f73 6974  self._true_posit
-00015b90: 6976 6573 7d5c 6e7b 7365 6c66 2e5f 7472  ives}\n{self._tr
-00015ba0: 7565 5f70 6f73 6974 6976 6573 202f 2073  ue_positives / s
-00015bb0: 656c 662e 7361 6d70 6c65 5f73 697a 653a  elf.sample_size:
-00015bc0: 2e31 257d 275d 5d29 2020 2320 7079 6c69  .1%}']])  # pyli
-00015bd0: 6e74 3a20 6469 7361 626c 653d 6c69 6e65  nt: disable=line
-00015be0: 2d74 6f6f 2d6c 6f6e 6720 2023 206e 6f71  -too-long  # noq
-00015bf0: 610a 0a20 2020 2020 2020 2061 7869 7320  a..        axis 
-00015c00: 3d20 706c 742e 7375 6270 6c6f 7428 290a  = plt.subplot().
-00015c10: 2020 2020 2020 2020 736e 732e 6865 6174          sns.heat
-00015c20: 6d61 7028 7365 6c66 2e5f 636f 6e66 7573  map(self._confus
-00015c30: 696f 6e5f 6d61 7472 6978 2c20 616e 6e6f  ion_matrix, anno
-00015c40: 743d 6c61 6265 6c73 2c20 636d 6170 3d27  t=labels, cmap='
-00015c50: 426c 7565 7327 2c20 6178 3d61 7869 732c  Blues', ax=axis,
-00015c60: 2066 6d74 3d27 2729 0a20 2020 2020 2020   fmt='').       
-00015c70: 2023 206c 6162 656c 732c 2074 6974 6c65   # labels, title
-00015c80: 2061 6e64 2074 6963 6b73 0a20 2020 2020   and ticks.     
-00015c90: 2020 2061 7869 732e 7365 745f 786c 6162     axis.set_xlab
-00015ca0: 656c 2827 5072 6564 6963 7465 6427 290a  el('Predicted').
-00015cb0: 2020 2020 2020 2020 6178 6973 2e73 6574          axis.set
-00015cc0: 5f79 6c61 6265 6c28 2741 6374 7561 6c27  _ylabel('Actual'
-00015cd0: 290a 2020 2020 2020 2020 2320 6178 6973  ).        # axis
-00015ce0: 2e73 6574 5f74 6974 6c65 2827 436f 6e66  .set_title('Conf
-00015cf0: 7573 696f 6e20 4d61 7472 6978 2729 3b0a  usion Matrix');.
-00015d00: 2020 2020 2020 2020 6178 6973 2e78 6178          axis.xax
-00015d10: 6973 2e73 6574 5f74 6963 6b6c 6162 656c  is.set_ticklabel
-00015d20: 7328 5b73 656c 662e 5f6e 6567 6174 6976  s([self._negativ
-00015d30: 655f 636c 6173 732c 2073 656c 662e 5f70  e_class, self._p
-00015d40: 6f73 6974 6976 655f 636c 6173 735d 290a  ositive_class]).
-00015d50: 2020 2020 2020 2020 6178 6973 2e79 6178          axis.yax
-00015d60: 6973 2e73 6574 5f74 6963 6b6c 6162 656c  is.set_ticklabel
-00015d70: 7328 5b73 656c 662e 5f6e 6567 6174 6976  s([self._negativ
-00015d80: 655f 636c 6173 732c 2073 656c 662e 5f70  e_class, self._p
-00015d90: 6f73 6974 6976 655f 636c 6173 735d 290a  ositive_class]).
-00015da0: 2020 2020 2020 2020 706c 742e 7469 6768          plt.tigh
-00015db0: 745f 6c61 796f 7574 2829 0a0a 2020 2020  t_layout()..    
-00015dc0: 6465 6620 5f67 6574 5f61 7563 5f63 7572  def _get_auc_cur
-00015dd0: 7665 5f64 6174 6166 7261 6d65 2873 656c  ve_dataframe(sel
-00015de0: 6629 202d 3e20 7064 2e44 6174 6146 7261  f) -> pd.DataFra
-00015df0: 6d65 3a0a 2020 2020 2020 2020 2222 220a  me:.        """.
-00015e00: 2020 2020 2020 2020 5265 7475 726e 7320          Returns 
-00015e10: 6120 6461 7461 6672 616d 6520 636f 6e74  a dataframe cont
-00015e20: 6169 6e69 6e67 2074 6865 2041 5543 206c  aining the AUC l
-00015e30: 696e 6520 2869 2e65 2e20 6120 636f 6c75  ine (i.e. a colu
-00015e40: 6d6e 206f 6620 7363 6f72 6520 7468 7265  mn of score thre
-00015e50: 7368 6f6c 6473 2c20 616e 6420 7468 6520  sholds, and the 
-00015e60: 636f 7272 6573 706f 6e64 696e 670a 2020  corresponding.  
-00015e70: 2020 2020 2020 5472 7565 2050 6f73 6974        True Posit
-00015e80: 6976 6520 616e 6420 4661 6c73 6520 506f  ive and False Po
-00015e90: 7369 7469 7665 2052 6174 6520 2861 7320  sitive Rate (as 
-00015ea0: 636f 6c75 6d6e 7329 2066 6f72 2074 6865  columns) for the
-00015eb0: 2063 6f72 7265 7370 6f6e 6469 6e67 2073   corresponding s
-00015ec0: 636f 7265 2074 6872 6573 686f 6c64 2e0a  core threshold..
-00015ed0: 0a20 2020 2020 2020 2028 4120 7363 6f72  .        (A scor
-00015ee0: 6520 7468 7265 7368 6f6c 6420 6973 2074  e threshold is t
-00015ef0: 6865 2076 616c 7565 2066 6f72 2077 6869  he value for whi
-00015f00: 6368 2079 6f75 2077 6f75 6c64 2070 7265  ch you would pre
-00015f10: 6469 6374 2061 2070 6f73 6974 6976 6520  dict a positive 
-00015f20: 6c61 6265 6c20 6966 2074 6865 2076 616c  label if the val
-00015f30: 7565 206f 6620 7468 6520 7363 6f72 650a  ue of the score.
-00015f40: 2020 2020 2020 2020 6973 2061 626f 7665          is above
-00015f50: 2074 6865 2074 6872 6573 686f 6c64 2028   the threshold (
-00015f60: 652e 672e 2075 7375 616c 6c79 2030 2e35  e.g. usually 0.5
-00015f70: 292e 0a20 2020 2020 2020 2022 2222 0a20  )..        """. 
-00015f80: 2020 2020 2020 2064 6566 2067 6574 5f74         def get_t
-00015f90: 7275 655f 706f 735f 6661 6c73 655f 706f  rue_pos_false_po
-00015fa0: 7328 7468 7265 7368 6f6c 6429 3a0a 2020  s(threshold):.  
-00015fb0: 2020 2020 2020 2020 2020 7465 6d70 5f65            temp_e
-00015fc0: 7661 6c20 3d20 5477 6f43 6c61 7373 4576  val = TwoClassEv
-00015fd0: 616c 7561 746f 7228 6163 7475 616c 5f76  aluator(actual_v
-00015fe0: 616c 7565 733d 7365 6c66 2e5f 6163 7475  alues=self._actu
-00015ff0: 616c 5f76 616c 7565 732c 0a20 2020 2020  al_values,.     
+00015ac0: 2020 2020 5b66 2746 616c 7365 204e 6567      [f'False Neg
+00015ad0: 6174 6976 6573 5c6e 7b73 656c 662e 5f66  atives\n{self._f
+00015ae0: 616c 7365 5f6e 6567 6174 6976 6573 7d5c  alse_negatives}\
+00015af0: 6e7b 7365 6c66 2e5f 6661 6c73 655f 6e65  n{self._false_ne
+00015b00: 6761 7469 7665 7320 2f20 7365 6c66 2e73  gatives / self.s
+00015b10: 616d 706c 655f 7369 7a65 3a2e 3125 7d27  ample_size:.1%}'
+00015b20: 2c20 2023 2070 796c 696e 743a 2064 6973  ,  # pylint: dis
+00015b30: 6162 6c65 3d6c 696e 652d 746f 6f2d 6c6f  able=line-too-lo
+00015b40: 6e67 2020 2320 6e6f 7161 0a20 2020 2020  ng  # noqa.     
+00015b50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00015b60: 2020 2020 2020 2066 2754 7275 6520 506f         f'True Po
+00015b70: 7369 7469 7665 735c 6e7b 7365 6c66 2e5f  sitives\n{self._
+00015b80: 7472 7565 5f70 6f73 6974 6976 6573 7d5c  true_positives}\
+00015b90: 6e7b 7365 6c66 2e5f 7472 7565 5f70 6f73  n{self._true_pos
+00015ba0: 6974 6976 6573 202f 2073 656c 662e 7361  itives / self.sa
+00015bb0: 6d70 6c65 5f73 697a 653a 2e31 257d 275d  mple_size:.1%}']
+00015bc0: 5d29 2020 2320 7079 6c69 6e74 3a20 6469  ])  # pylint: di
+00015bd0: 7361 626c 653d 6c69 6e65 2d74 6f6f 2d6c  sable=line-too-l
+00015be0: 6f6e 6720 2023 206e 6f71 610a 0a20 2020  ong  # noqa..   
+00015bf0: 2020 2020 2061 7869 7320 3d20 706c 742e       axis = plt.
+00015c00: 7375 6270 6c6f 7428 290a 2020 2020 2020  subplot().      
+00015c10: 2020 736e 732e 6865 6174 6d61 7028 7365    sns.heatmap(se
+00015c20: 6c66 2e5f 636f 6e66 7573 696f 6e5f 6d61  lf._confusion_ma
+00015c30: 7472 6978 2c20 616e 6e6f 743d 6c61 6265  trix, annot=labe
+00015c40: 6c73 2c20 636d 6170 3d27 426c 7565 7327  ls, cmap='Blues'
+00015c50: 2c20 6178 3d61 7869 732c 2066 6d74 3d27  , ax=axis, fmt='
+00015c60: 2729 0a20 2020 2020 2020 2023 206c 6162  ').        # lab
+00015c70: 656c 732c 2074 6974 6c65 2061 6e64 2074  els, title and t
+00015c80: 6963 6b73 0a20 2020 2020 2020 2061 7869  icks.        axi
+00015c90: 732e 7365 745f 786c 6162 656c 2827 5072  s.set_xlabel('Pr
+00015ca0: 6564 6963 7465 6427 290a 2020 2020 2020  edicted').      
+00015cb0: 2020 6178 6973 2e73 6574 5f79 6c61 6265    axis.set_ylabe
+00015cc0: 6c28 2741 6374 7561 6c27 290a 2020 2020  l('Actual').    
+00015cd0: 2020 2020 2320 6178 6973 2e73 6574 5f74      # axis.set_t
+00015ce0: 6974 6c65 2827 436f 6e66 7573 696f 6e20  itle('Confusion 
+00015cf0: 4d61 7472 6978 2729 3b0a 2020 2020 2020  Matrix');.      
+00015d00: 2020 6178 6973 2e78 6178 6973 2e73 6574    axis.xaxis.set
+00015d10: 5f74 6963 6b6c 6162 656c 7328 5b73 656c  _ticklabels([sel
+00015d20: 662e 5f6e 6567 6174 6976 655f 636c 6173  f._negative_clas
+00015d30: 732c 2073 656c 662e 5f70 6f73 6974 6976  s, self._positiv
+00015d40: 655f 636c 6173 735d 290a 2020 2020 2020  e_class]).      
+00015d50: 2020 6178 6973 2e79 6178 6973 2e73 6574    axis.yaxis.set
+00015d60: 5f74 6963 6b6c 6162 656c 7328 5b73 656c  _ticklabels([sel
+00015d70: 662e 5f6e 6567 6174 6976 655f 636c 6173  f._negative_clas
+00015d80: 732c 2073 656c 662e 5f70 6f73 6974 6976  s, self._positiv
+00015d90: 655f 636c 6173 735d 290a 2020 2020 2020  e_class]).      
+00015da0: 2020 706c 742e 7469 6768 745f 6c61 796f    plt.tight_layo
+00015db0: 7574 2829 0a0a 2020 2020 6465 6620 5f67  ut()..    def _g
+00015dc0: 6574 5f61 7563 5f63 7572 7665 5f64 6174  et_auc_curve_dat
+00015dd0: 6166 7261 6d65 2873 656c 6629 202d 3e20  aframe(self) -> 
+00015de0: 7064 2e44 6174 6146 7261 6d65 3a0a 2020  pd.DataFrame:.  
+00015df0: 2020 2020 2020 2222 220a 2020 2020 2020        """.      
+00015e00: 2020 5265 7475 726e 7320 6120 6461 7461    Returns a data
+00015e10: 6672 616d 6520 636f 6e74 6169 6e69 6e67  frame containing
+00015e20: 2074 6865 2041 5543 206c 696e 6520 2869   the AUC line (i
+00015e30: 2e65 2e20 6120 636f 6c75 6d6e 206f 6620  .e. a column of 
+00015e40: 7363 6f72 6520 7468 7265 7368 6f6c 6473  score thresholds
+00015e50: 2c20 616e 6420 7468 6520 636f 7272 6573  , and the corres
+00015e60: 706f 6e64 696e 670a 2020 2020 2020 2020  ponding.        
+00015e70: 5472 7565 2050 6f73 6974 6976 6520 616e  True Positive an
+00015e80: 6420 4661 6c73 6520 506f 7369 7469 7665  d False Positive
+00015e90: 2052 6174 6520 2861 7320 636f 6c75 6d6e   Rate (as column
+00015ea0: 7329 2066 6f72 2074 6865 2063 6f72 7265  s) for the corre
+00015eb0: 7370 6f6e 6469 6e67 2073 636f 7265 2074  sponding score t
+00015ec0: 6872 6573 686f 6c64 2e0a 0a20 2020 2020  hreshold...     
+00015ed0: 2020 2028 4120 7363 6f72 6520 7468 7265     (A score thre
+00015ee0: 7368 6f6c 6420 6973 2074 6865 2076 616c  shold is the val
+00015ef0: 7565 2066 6f72 2077 6869 6368 2079 6f75  ue for which you
+00015f00: 2077 6f75 6c64 2070 7265 6469 6374 2061   would predict a
+00015f10: 2070 6f73 6974 6976 6520 6c61 6265 6c20   positive label 
+00015f20: 6966 2074 6865 2076 616c 7565 206f 6620  if the value of 
+00015f30: 7468 6520 7363 6f72 650a 2020 2020 2020  the score.      
+00015f40: 2020 6973 2061 626f 7665 2074 6865 2074    is above the t
+00015f50: 6872 6573 686f 6c64 2028 652e 672e 2075  hreshold (e.g. u
+00015f60: 7375 616c 6c79 2030 2e35 292e 0a20 2020  sually 0.5)..   
+00015f70: 2020 2020 2022 2222 0a20 2020 2020 2020       """.       
+00015f80: 2064 6566 2067 6574 5f74 7275 655f 706f   def get_true_po
+00015f90: 735f 6661 6c73 655f 706f 7328 7468 7265  s_false_pos(thre
+00015fa0: 7368 6f6c 6429 3a0a 2020 2020 2020 2020  shold):.        
+00015fb0: 2020 2020 7465 6d70 5f65 7661 6c20 3d20      temp_eval = 
+00015fc0: 5477 6f43 6c61 7373 4576 616c 7561 746f  TwoClassEvaluato
+00015fd0: 7228 6163 7475 616c 5f76 616c 7565 733d  r(actual_values=
+00015fe0: 7365 6c66 2e5f 6163 7475 616c 5f76 616c  self._actual_val
+00015ff0: 7565 732c 0a20 2020 2020 2020 2020 2020  ues,.           
 00016000: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016010: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016020: 2020 2020 2070 7265 6469 6374 6564 5f73       predicted_s
-00016030: 636f 7265 733d 7365 6c66 2e5f 7072 6564  cores=self._pred
-00016040: 6963 7465 645f 7363 6f72 6573 2c0a 2020  icted_scores,.  
+00016010: 2020 2020 2020 2020 2020 2020 2020 2070                 p
+00016020: 7265 6469 6374 6564 5f73 636f 7265 733d  redicted_scores=
+00016030: 7365 6c66 2e5f 7072 6564 6963 7465 645f  self._predicted_
+00016040: 7363 6f72 6573 2c0a 2020 2020 2020 2020  scores,.        
 00016050: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00016060: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016070: 2020 2020 2020 2020 7363 6f72 655f 7468          score_th
-00016080: 7265 7368 6f6c 643d 7468 7265 7368 6f6c  reshold=threshol
-00016090: 6429 0a0a 2020 2020 2020 2020 2020 2020  d)..            
-000160a0: 7265 7475 726e 2074 6872 6573 686f 6c64  return threshold
-000160b0: 2c20 7465 6d70 5f65 7661 6c2e 7472 7565  , temp_eval.true
-000160c0: 5f70 6f73 6974 6976 655f 7261 7465 2c20  _positive_rate, 
-000160d0: 7465 6d70 5f65 7661 6c2e 6661 6c73 655f  temp_eval.false_
-000160e0: 706f 7369 7469 7665 5f72 6174 650a 0a20  positive_rate.. 
-000160f0: 2020 2020 2020 2061 7563 5f63 7572 7665         auc_curve
-00016100: 203d 205b 6765 745f 7472 7565 5f70 6f73   = [get_true_pos
-00016110: 5f66 616c 7365 5f70 6f73 2874 6872 6573  _false_pos(thres
-00016120: 686f 6c64 3d78 2920 666f 7220 7820 696e  hold=x) for x in
-00016130: 206e 702e 6172 616e 6765 2830 2e30 2c20   np.arange(0.0, 
-00016140: 312e 3031 2c20 302e 3031 295d 0a20 2020  1.01, 0.01)].   
-00016150: 2020 2020 2061 7563 5f63 7572 7665 203d       auc_curve =
-00016160: 2070 642e 4461 7461 4672 616d 6528 6175   pd.DataFrame(au
-00016170: 635f 6375 7276 652c 0a20 2020 2020 2020  c_curve,.       
+00016070: 2020 7363 6f72 655f 7468 7265 7368 6f6c    score_threshol
+00016080: 643d 7468 7265 7368 6f6c 6429 0a0a 2020  d=threshold)..  
+00016090: 2020 2020 2020 2020 2020 7265 7475 726e            return
+000160a0: 2074 6872 6573 686f 6c64 2c20 7465 6d70   threshold, temp
+000160b0: 5f65 7661 6c2e 7472 7565 5f70 6f73 6974  _eval.true_posit
+000160c0: 6976 655f 7261 7465 2c20 7465 6d70 5f65  ive_rate, temp_e
+000160d0: 7661 6c2e 6661 6c73 655f 706f 7369 7469  val.false_positi
+000160e0: 7665 5f72 6174 650a 0a20 2020 2020 2020  ve_rate..       
+000160f0: 2061 7563 5f63 7572 7665 203d 205b 6765   auc_curve = [ge
+00016100: 745f 7472 7565 5f70 6f73 5f66 616c 7365  t_true_pos_false
+00016110: 5f70 6f73 2874 6872 6573 686f 6c64 3d78  _pos(threshold=x
+00016120: 2920 666f 7220 7820 696e 206e 702e 6172  ) for x in np.ar
+00016130: 616e 6765 2830 2e30 2c20 312e 3031 2c20  ange(0.0, 1.01, 
+00016140: 302e 3031 295d 0a20 2020 2020 2020 2061  0.01)].        a
+00016150: 7563 5f63 7572 7665 203d 2070 642e 4461  uc_curve = pd.Da
+00016160: 7461 4672 616d 6528 6175 635f 6375 7276  taFrame(auc_curv
+00016170: 652c 0a20 2020 2020 2020 2020 2020 2020  e,.             
 00016180: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016190: 2020 2020 2020 2020 2020 636f 6c75 6d6e            column
-000161a0: 733d 5b27 7468 7265 7368 6f6c 6427 2c20  s=['threshold', 
-000161b0: 2754 7275 6520 506f 7369 7469 7665 2052  'True Positive R
-000161c0: 6174 6527 2c20 2746 616c 7365 2050 6f73  ate', 'False Pos
-000161d0: 6974 6976 6520 5261 7465 275d 290a 2020  itive Rate']).  
-000161e0: 2020 2020 2020 7265 7475 726e 2061 7563        return auc
-000161f0: 5f63 7572 7665 0a0a 2020 2020 6465 6620  _curve..    def 
-00016200: 5f67 6574 5f74 6872 6573 686f 6c64 5f63  _get_threshold_c
-00016210: 7572 7665 5f64 6174 6166 7261 6d65 2873  urve_dataframe(s
-00016220: 656c 662c 2073 636f 7265 5f74 6872 6573  elf, score_thres
-00016230: 686f 6c64 5f72 616e 6765 3a20 5475 706c  hold_range: Tupl
-00016240: 655b 666c 6f61 742c 2066 6c6f 6174 5d20  e[float, float] 
-00016250: 3d20 2830 2e31 2c20 302e 3929 2920 5c0a  = (0.1, 0.9)) \.
-00016260: 2020 2020 2020 2020 2020 2020 2d3e 2070              -> p
-00016270: 642e 4461 7461 4672 616d 653a 0a20 2020  d.DataFrame:.   
-00016280: 2020 2020 2022 2222 0a20 2020 2020 2020       """.       
-00016290: 2052 6574 7572 6e73 2061 2064 6174 6166   Returns a dataf
-000162a0: 7261 6d65 2063 6f6e 7461 696e 696e 6720  rame containing 
-000162b0: 7661 7269 6f75 7320 7363 6f72 6520 7468  various score th
-000162c0: 7265 7368 6f6c 6473 2066 726f 6d20 3020  resholds from 0 
-000162d0: 746f 2031 2028 692e 652e 2063 7574 6f66  to 1 (i.e. cutof
-000162e0: 6620 706f 696e 7420 7768 6572 6520 7363  f point where sc
-000162f0: 6f72 650a 2020 2020 2020 2020 7769 6c6c  ore.        will
-00016300: 2062 6520 6c61 6265 6c65 6420 6173 2061   be labeled as a
-00016310: 2027 706f 7369 7469 7665 2720 6576 656e   'positive' even
-00016320: 742c 2061 6e64 2076 6172 696f 7573 2072  t, and various r
-00016330: 6174 6573 2028 652e 672e 2054 7275 6520  ates (e.g. True 
-00016340: 506f 7369 7469 7665 2052 6174 652c 2046  Positive Rate, F
-00016350: 616c 7365 2050 6f73 6974 6976 650a 2020  alse Positive.  
-00016360: 2020 2020 2020 5261 7465 2c20 6574 632e        Rate, etc.
-00016370: 2920 666f 7220 7468 6520 636f 7272 6573  ) for the corres
-00016380: 706f 6e64 696e 6720 7363 6f72 6520 7468  ponding score th
-00016390: 7265 7368 6f6c 642e 0a0a 2020 2020 2020  reshold...      
-000163a0: 2020 2841 2073 636f 7265 2074 6872 6573    (A score thres
-000163b0: 686f 6c64 2069 7320 7468 6520 7661 6c75  hold is the valu
-000163c0: 6520 666f 7220 7768 6963 6820 796f 7520  e for which you 
-000163d0: 776f 756c 6420 7072 6564 6963 7420 6120  would predict a 
-000163e0: 706f 7369 7469 7665 206c 6162 656c 2069  positive label i
-000163f0: 6620 7468 6520 7661 6c75 6520 6f66 2074  f the value of t
-00016400: 6865 2073 636f 7265 0a20 2020 2020 2020  he score.       
-00016410: 2069 7320 6162 6f76 6520 7468 6520 7468   is above the th
-00016420: 7265 7368 6f6c 6420 2865 2e67 2e20 7573  reshold (e.g. us
-00016430: 7561 6c6c 7920 302e 3529 2e0a 0a20 2020  ually 0.5)...   
-00016440: 2020 2020 2041 7267 733a 0a20 2020 2020       Args:.     
-00016450: 2020 2020 2020 2073 636f 7265 5f74 6872         score_thr
-00016460: 6573 686f 6c64 5f72 616e 6765 3a0a 2020  eshold_range:.  
-00016470: 2020 2020 2020 2020 2020 2020 2020 7261                ra
-00016480: 6e67 6520 6f66 2073 636f 7265 2074 6872  nge of score thr
-00016490: 6573 686f 6c64 7320 746f 2070 6c6f 7420  esholds to plot 
-000164a0: 2878 2d61 7869 7329 3b20 7475 706c 6520  (x-axis); tuple 
-000164b0: 7769 7468 206d 696e 696d 756d 2074 6872  with minimum thr
-000164c0: 6573 686f 6c64 2069 6e20 6669 7273 7420  eshold in first 
-000164d0: 696e 6465 7820 616e 640a 2020 2020 2020  index and.      
-000164e0: 2020 2020 2020 2020 2020 6d61 7869 6d75            maximu
-000164f0: 6d20 7468 7265 7368 6f6c 6420 696e 2073  m threshold in s
-00016500: 6563 6f6e 6420 696e 6465 782e 0a20 2020  econd index..   
-00016510: 2020 2020 2022 2222 0a20 2020 2020 2020       """.       
-00016520: 2064 6566 2067 6574 5f74 6872 6573 686f   def get_thresho
-00016530: 6c64 5f73 636f 7265 7328 7468 7265 7368  ld_scores(thresh
-00016540: 6f6c 6429 3a0a 2020 2020 2020 2020 2020  old):.          
-00016550: 2020 7465 6d70 5f65 7661 6c20 3d20 5477    temp_eval = Tw
-00016560: 6f43 6c61 7373 4576 616c 7561 746f 7228  oClassEvaluator(
-00016570: 6163 7475 616c 5f76 616c 7565 733d 7365  actual_values=se
-00016580: 6c66 2e5f 6163 7475 616c 5f76 616c 7565  lf._actual_value
-00016590: 732c 0a20 2020 2020 2020 2020 2020 2020  s,.             
+00016190: 2020 2020 636f 6c75 6d6e 733d 5b27 7468      columns=['th
+000161a0: 7265 7368 6f6c 6427 2c20 2754 7275 6520  reshold', 'True 
+000161b0: 506f 7369 7469 7665 2052 6174 6527 2c20  Positive Rate', 
+000161c0: 2746 616c 7365 2050 6f73 6974 6976 6520  'False Positive 
+000161d0: 5261 7465 275d 290a 2020 2020 2020 2020  Rate']).        
+000161e0: 7265 7475 726e 2061 7563 5f63 7572 7665  return auc_curve
+000161f0: 0a0a 2020 2020 6465 6620 5f67 6574 5f74  ..    def _get_t
+00016200: 6872 6573 686f 6c64 5f63 7572 7665 5f64  hreshold_curve_d
+00016210: 6174 6166 7261 6d65 2873 656c 662c 2073  ataframe(self, s
+00016220: 636f 7265 5f74 6872 6573 686f 6c64 5f72  core_threshold_r
+00016230: 616e 6765 3a20 5475 706c 655b 666c 6f61  ange: Tuple[floa
+00016240: 742c 2066 6c6f 6174 5d20 3d20 2830 2e31  t, float] = (0.1
+00016250: 2c20 302e 3929 2920 5c0a 2020 2020 2020  , 0.9)) \.      
+00016260: 2020 2020 2020 2d3e 2070 642e 4461 7461        -> pd.Data
+00016270: 4672 616d 653a 0a20 2020 2020 2020 2022  Frame:.        "
+00016280: 2222 0a20 2020 2020 2020 2052 6574 7572  "".        Retur
+00016290: 6e73 2061 2064 6174 6166 7261 6d65 2063  ns a dataframe c
+000162a0: 6f6e 7461 696e 696e 6720 7661 7269 6f75  ontaining variou
+000162b0: 7320 7363 6f72 6520 7468 7265 7368 6f6c  s score threshol
+000162c0: 6473 2066 726f 6d20 3020 746f 2031 2028  ds from 0 to 1 (
+000162d0: 692e 652e 2063 7574 6f66 6620 706f 696e  i.e. cutoff poin
+000162e0: 7420 7768 6572 6520 7363 6f72 650a 2020  t where score.  
+000162f0: 2020 2020 2020 7769 6c6c 2062 6520 6c61        will be la
+00016300: 6265 6c65 6420 6173 2061 2027 706f 7369  beled as a 'posi
+00016310: 7469 7665 2720 6576 656e 742c 2061 6e64  tive' event, and
+00016320: 2076 6172 696f 7573 2072 6174 6573 2028   various rates (
+00016330: 652e 672e 2054 7275 6520 506f 7369 7469  e.g. True Positi
+00016340: 7665 2052 6174 652c 2046 616c 7365 2050  ve Rate, False P
+00016350: 6f73 6974 6976 650a 2020 2020 2020 2020  ositive.        
+00016360: 5261 7465 2c20 6574 632e 2920 666f 7220  Rate, etc.) for 
+00016370: 7468 6520 636f 7272 6573 706f 6e64 696e  the correspondin
+00016380: 6720 7363 6f72 6520 7468 7265 7368 6f6c  g score threshol
+00016390: 642e 0a0a 2020 2020 2020 2020 2841 2073  d...        (A s
+000163a0: 636f 7265 2074 6872 6573 686f 6c64 2069  core threshold i
+000163b0: 7320 7468 6520 7661 6c75 6520 666f 7220  s the value for 
+000163c0: 7768 6963 6820 796f 7520 776f 756c 6420  which you would 
+000163d0: 7072 6564 6963 7420 6120 706f 7369 7469  predict a positi
+000163e0: 7665 206c 6162 656c 2069 6620 7468 6520  ve label if the 
+000163f0: 7661 6c75 6520 6f66 2074 6865 2073 636f  value of the sco
+00016400: 7265 0a20 2020 2020 2020 2069 7320 6162  re.        is ab
+00016410: 6f76 6520 7468 6520 7468 7265 7368 6f6c  ove the threshol
+00016420: 6420 2865 2e67 2e20 7573 7561 6c6c 7920  d (e.g. usually 
+00016430: 302e 3529 2e0a 0a20 2020 2020 2020 2041  0.5)...        A
+00016440: 7267 733a 0a20 2020 2020 2020 2020 2020  rgs:.           
+00016450: 2073 636f 7265 5f74 6872 6573 686f 6c64   score_threshold
+00016460: 5f72 616e 6765 3a0a 2020 2020 2020 2020  _range:.        
+00016470: 2020 2020 2020 2020 7261 6e67 6520 6f66          range of
+00016480: 2073 636f 7265 2074 6872 6573 686f 6c64   score threshold
+00016490: 7320 746f 2070 6c6f 7420 2878 2d61 7869  s to plot (x-axi
+000164a0: 7329 3b20 7475 706c 6520 7769 7468 206d  s); tuple with m
+000164b0: 696e 696d 756d 2074 6872 6573 686f 6c64  inimum threshold
+000164c0: 2069 6e20 6669 7273 7420 696e 6465 7820   in first index 
+000164d0: 616e 640a 2020 2020 2020 2020 2020 2020  and.            
+000164e0: 2020 2020 6d61 7869 6d75 6d20 7468 7265      maximum thre
+000164f0: 7368 6f6c 6420 696e 2073 6563 6f6e 6420  shold in second 
+00016500: 696e 6465 782e 0a20 2020 2020 2020 2022  index..        "
+00016510: 2222 0a20 2020 2020 2020 2064 6566 2067  "".        def g
+00016520: 6574 5f74 6872 6573 686f 6c64 5f73 636f  et_threshold_sco
+00016530: 7265 7328 7468 7265 7368 6f6c 6429 3a0a  res(threshold):.
+00016540: 2020 2020 2020 2020 2020 2020 7465 6d70              temp
+00016550: 5f65 7661 6c20 3d20 5477 6f43 6c61 7373  _eval = TwoClass
+00016560: 4576 616c 7561 746f 7228 6163 7475 616c  Evaluator(actual
+00016570: 5f76 616c 7565 733d 7365 6c66 2e5f 6163  _values=self._ac
+00016580: 7475 616c 5f76 616c 7565 732c 0a20 2020  tual_values,.   
+00016590: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000165a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000165b0: 2020 2020 2020 2020 2020 2020 2070 7265               pre
-000165c0: 6469 6374 6564 5f73 636f 7265 733d 7365  dicted_scores=se
-000165d0: 6c66 2e5f 7072 6564 6963 7465 645f 7363  lf._predicted_sc
-000165e0: 6f72 6573 2c0a 2020 2020 2020 2020 2020  ores,.          
+000165b0: 2020 2020 2020 2070 7265 6469 6374 6564         predicted
+000165c0: 5f73 636f 7265 733d 7365 6c66 2e5f 7072  _scores=self._pr
+000165d0: 6564 6963 7465 645f 7363 6f72 6573 2c0a  edicted_scores,.
+000165e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000165f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016600: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016610: 7363 6f72 655f 7468 7265 7368 6f6c 643d  score_threshold=
-00016620: 7468 7265 7368 6f6c 6429 0a0a 2020 2020  threshold)..    
-00016630: 2020 2020 2020 2020 7265 7475 726e 2074          return t
-00016640: 6872 6573 686f 6c64 2c5c 0a20 2020 2020  hreshold,\.     
-00016650: 2020 2020 2020 2020 2020 2074 656d 705f             temp_
-00016660: 6576 616c 2e74 7275 655f 706f 7369 7469  eval.true_positi
-00016670: 7665 5f72 6174 652c 5c0a 2020 2020 2020  ve_rate,\.      
-00016680: 2020 2020 2020 2020 2020 7465 6d70 5f65            temp_e
-00016690: 7661 6c2e 6661 6c73 655f 706f 7369 7469  val.false_positi
-000166a0: 7665 5f72 6174 652c 5c0a 2020 2020 2020  ve_rate,\.      
-000166b0: 2020 2020 2020 2020 2020 7465 6d70 5f65            temp_e
-000166c0: 7661 6c2e 706f 7369 7469 7665 5f70 7265  val.positive_pre
-000166d0: 6469 6374 6976 655f 7661 6c75 652c 5c0a  dictive_value,\.
-000166e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000166f0: 7465 6d70 5f65 7661 6c2e 6661 6c73 655f  temp_eval.false_
-00016700: 6e65 6761 7469 7665 5f72 6174 652c 5c0a  negative_rate,\.
-00016710: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016720: 7465 6d70 5f65 7661 6c2e 7472 7565 5f6e  temp_eval.true_n
-00016730: 6567 6174 6976 655f 7261 7465 0a0a 2020  egative_rate..  
-00016740: 2020 2020 2020 7468 7265 7368 6f6c 645f        threshold_
-00016750: 6375 7276 6573 203d 205b 6765 745f 7468  curves = [get_th
-00016760: 7265 7368 6f6c 645f 7363 6f72 6573 2874  reshold_scores(t
-00016770: 6872 6573 686f 6c64 3d78 290a 2020 2020  hreshold=x).    
+00016600: 2020 2020 2020 2020 2020 7363 6f72 655f            score_
+00016610: 7468 7265 7368 6f6c 643d 7468 7265 7368  threshold=thresh
+00016620: 6f6c 6429 0a0a 2020 2020 2020 2020 2020  old)..          
+00016630: 2020 7265 7475 726e 2074 6872 6573 686f    return thresho
+00016640: 6c64 2c5c 0a20 2020 2020 2020 2020 2020  ld,\.           
+00016650: 2020 2020 2074 656d 705f 6576 616c 2e74       temp_eval.t
+00016660: 7275 655f 706f 7369 7469 7665 5f72 6174  rue_positive_rat
+00016670: 652c 5c0a 2020 2020 2020 2020 2020 2020  e,\.            
+00016680: 2020 2020 7465 6d70 5f65 7661 6c2e 6661      temp_eval.fa
+00016690: 6c73 655f 706f 7369 7469 7665 5f72 6174  lse_positive_rat
+000166a0: 652c 5c0a 2020 2020 2020 2020 2020 2020  e,\.            
+000166b0: 2020 2020 7465 6d70 5f65 7661 6c2e 706f      temp_eval.po
+000166c0: 7369 7469 7665 5f70 7265 6469 6374 6976  sitive_predictiv
+000166d0: 655f 7661 6c75 652c 5c0a 2020 2020 2020  e_value,\.      
+000166e0: 2020 2020 2020 2020 2020 7465 6d70 5f65            temp_e
+000166f0: 7661 6c2e 6661 6c73 655f 6e65 6761 7469  val.false_negati
+00016700: 7665 5f72 6174 652c 5c0a 2020 2020 2020  ve_rate,\.      
+00016710: 2020 2020 2020 2020 2020 7465 6d70 5f65            temp_e
+00016720: 7661 6c2e 7472 7565 5f6e 6567 6174 6976  val.true_negativ
+00016730: 655f 7261 7465 0a0a 2020 2020 2020 2020  e_rate..        
+00016740: 7468 7265 7368 6f6c 645f 6375 7276 6573  threshold_curves
+00016750: 203d 205b 6765 745f 7468 7265 7368 6f6c   = [get_threshol
+00016760: 645f 7363 6f72 6573 2874 6872 6573 686f  d_scores(thresho
+00016770: 6c64 3d78 290a 2020 2020 2020 2020 2020  ld=x).          
 00016780: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016790: 2020 2020 2020 2020 666f 7220 7820 696e          for x in
-000167a0: 206e 702e 6172 616e 6765 2873 636f 7265   np.arange(score
-000167b0: 5f74 6872 6573 686f 6c64 5f72 616e 6765  _threshold_range
-000167c0: 5b30 5d2c 0a20 2020 2020 2020 2020 2020  [0],.           
+00016790: 2020 666f 7220 7820 696e 206e 702e 6172    for x in np.ar
+000167a0: 616e 6765 2873 636f 7265 5f74 6872 6573  ange(score_thres
+000167b0: 686f 6c64 5f72 616e 6765 5b30 5d2c 0a20  hold_range[0],. 
+000167c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000167d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000167e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000167f0: 2020 2020 7363 6f72 655f 7468 7265 7368      score_thresh
-00016800: 6f6c 645f 7261 6e67 655b 315d 202b 2030  old_range[1] + 0
-00016810: 2e30 3235 2c0a 2020 2020 2020 2020 2020  .025,.          
+000167e0: 2020 2020 2020 2020 2020 2020 2020 7363                sc
+000167f0: 6f72 655f 7468 7265 7368 6f6c 645f 7261  ore_threshold_ra
+00016800: 6e67 655b 315d 202b 2030 2e30 3235 2c0a  nge[1] + 0.025,.
+00016810: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00016820: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016830: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016840: 2020 2020 2030 2e30 3235 295d 0a0a 2020       0.025)]..  
-00016850: 2020 2020 2020 7468 7265 7368 6f6c 645f        threshold_
-00016860: 6375 7276 6573 203d 2070 642e 4461 7461  curves = pd.Data
-00016870: 4672 616d 6528 7468 7265 7368 6f6c 645f  Frame(threshold_
-00016880: 6375 7276 6573 2c0a 2020 2020 2020 2020  curves,.        
+00016830: 2020 2020 2020 2020 2020 2020 2020 2030                 0
+00016840: 2e30 3235 295d 0a0a 2020 2020 2020 2020  .025)]..        
+00016850: 7468 7265 7368 6f6c 645f 6375 7276 6573  threshold_curves
+00016860: 203d 2070 642e 4461 7461 4672 616d 6528   = pd.DataFrame(
+00016870: 7468 7265 7368 6f6c 645f 6375 7276 6573  threshold_curves
+00016880: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
 00016890: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000168a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000168b0: 636f 6c75 6d6e 733d 5b27 5363 6f72 6520  columns=['Score 
-000168c0: 5468 7265 7368 6f6c 6427 2c0a 2020 2020  Threshold',.    
+000168a0: 2020 2020 2020 2020 2020 636f 6c75 6d6e            column
+000168b0: 733d 5b27 5363 6f72 6520 5468 7265 7368  s=['Score Thresh
+000168c0: 6f6c 6427 2c0a 2020 2020 2020 2020 2020  old',.          
 000168d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000168e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000168f0: 2020 2020 2020 2020 2020 2020 2027 5472               'Tr
-00016900: 7565 2050 6f73 2e20 5261 7465 2028 5265  ue Pos. Rate (Re
-00016910: 6361 6c6c 2927 2c0a 2020 2020 2020 2020  call)',.        
+000168f0: 2020 2020 2020 2027 5472 7565 2050 6f73         'True Pos
+00016900: 2e20 5261 7465 2028 5265 6361 6c6c 2927  . Rate (Recall)'
+00016910: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
 00016920: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00016930: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016940: 2020 2020 2020 2020 2027 4661 6c73 6520           'False 
-00016950: 506f 732e 2052 6174 6527 2c0a 2020 2020  Pos. Rate',.    
+00016940: 2020 2027 4661 6c73 6520 506f 732e 2052     'False Pos. R
+00016950: 6174 6527 2c0a 2020 2020 2020 2020 2020  ate',.          
 00016960: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00016970: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016980: 2020 2020 2020 2020 2020 2020 2027 506f               'Po
-00016990: 732e 2050 7265 6469 6374 6976 6520 5661  s. Predictive Va
-000169a0: 6c75 6520 2850 7265 6369 7369 6f6e 2927  lue (Precision)'
-000169b0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00016980: 2020 2020 2020 2027 506f 732e 2050 7265         'Pos. Pre
+00016990: 6469 6374 6976 6520 5661 6c75 6520 2850  dictive Value (P
+000169a0: 7265 6369 7369 6f6e 2927 2c0a 2020 2020  recision)',.    
+000169b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000169c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000169d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000169e0: 2020 2027 4661 6c73 6520 4e65 672e 2052     'False Neg. R
-000169f0: 6174 6527 2c0a 2020 2020 2020 2020 2020  ate',.          
+000169d0: 2020 2020 2020 2020 2020 2020 2027 4661               'Fa
+000169e0: 6c73 6520 4e65 672e 2052 6174 6527 2c0a  lse Neg. Rate',.
+000169f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00016a00: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00016a10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016a20: 2020 2020 2020 2027 5472 7565 204e 6567         'True Neg
-00016a30: 2e20 5261 7465 2028 5370 6563 6966 6963  . Rate (Specific
-00016a40: 6974 7929 275d 290a 2020 2020 2020 2020  ity)']).        
-00016a50: 7265 7475 726e 2074 6872 6573 686f 6c64  return threshold
-00016a60: 5f63 7572 7665 730a 0a20 2020 2023 2070  _curves..    # p
-00016a70: 796c 696e 743a 2064 6973 6162 6c65 3d69  ylint: disable=i
-00016a80: 6e63 6f6e 7369 7374 656e 742d 7265 7475  nconsistent-retu
-00016a90: 726e 2d73 7461 7465 6d65 6e74 730a 2020  rn-statements.  
-00016aa0: 2020 6465 6620 706c 6f74 5f61 7563 5f63    def plot_auc_c
-00016ab0: 7572 7665 2873 656c 662c 0a20 2020 2020  urve(self,.     
-00016ac0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016ad0: 2020 6669 6775 7265 5f73 697a 653a 2074    figure_size: t
-00016ae0: 7570 6c65 203d 2053 5441 4e44 4152 445f  uple = STANDARD_
-00016af0: 5749 4454 485f 4845 4947 4854 2c0a 2020  WIDTH_HEIGHT,.  
-00016b00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016b10: 2020 2020 2072 6574 7572 6e5f 706c 6f74       return_plot
-00016b20: 6c79 3a20 626f 6f6c 203d 2046 616c 7365  ly: bool = False
-00016b30: 2920 2d3e 2055 6e69 6f6e 5b4e 6f6e 652c  ) -> Union[None,
-00016b40: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00016a20: 2027 5472 7565 204e 6567 2e20 5261 7465   'True Neg. Rate
+00016a30: 2028 5370 6563 6966 6963 6974 7929 275d   (Specificity)']
+00016a40: 290a 2020 2020 2020 2020 7265 7475 726e  ).        return
+00016a50: 2074 6872 6573 686f 6c64 5f63 7572 7665   threshold_curve
+00016a60: 730a 0a20 2020 2023 2070 796c 696e 743a  s..    # pylint:
+00016a70: 2064 6973 6162 6c65 3d69 6e63 6f6e 7369   disable=inconsi
+00016a80: 7374 656e 742d 7265 7475 726e 2d73 7461  stent-return-sta
+00016a90: 7465 6d65 6e74 730a 2020 2020 6465 6620  tements.    def 
+00016aa0: 706c 6f74 5f61 7563 5f63 7572 7665 2873  plot_auc_curve(s
+00016ab0: 656c 662c 0a20 2020 2020 2020 2020 2020  elf,.           
+00016ac0: 2020 2020 2020 2020 2020 2020 6669 6775              figu
+00016ad0: 7265 5f73 697a 653a 2074 7570 6c65 203d  re_size: tuple =
+00016ae0: 2053 5441 4e44 4152 445f 5749 4454 485f   STANDARD_WIDTH_
+00016af0: 4845 4947 4854 2c0a 2020 2020 2020 2020  HEIGHT,.        
+00016b00: 2020 2020 2020 2020 2020 2020 2020 2072                 r
+00016b10: 6574 7572 6e5f 706c 6f74 6c79 3a20 626f  eturn_plotly: bo
+00016b20: 6f6c 203d 2046 616c 7365 2920 2d3e 2055  ol = False) -> U
+00016b30: 6e69 6f6e 5b4e 6f6e 652c 0a20 2020 2020  nion[None,.     
+00016b40: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00016b50: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00016b60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016b70: 2020 2020 2020 2020 2020 2020 205f 6669               _fi
-00016b80: 6775 7265 2e46 6967 7572 655d 3a0a 2020  gure.Figure]:.  
-00016b90: 2020 2020 2020 2222 2250 6c6f 7473 2074        """Plots t
-00016ba0: 6865 2052 4f43 2041 5543 0a0a 2020 2020  he ROC AUC..    
-00016bb0: 2020 2020 4172 6773 3a0a 2020 2020 2020      Args:.      
-00016bc0: 2020 2020 2020 6669 6775 7265 5f73 697a        figure_siz
-00016bd0: 653a 0a20 2020 2020 2020 2020 2020 2020  e:.             
-00016be0: 2020 2074 7570 6c65 2063 6f6e 7461 696e     tuple contain
-00016bf0: 696e 6720 6028 7769 6474 682c 2068 6569  ing `(width, hei
-00016c00: 6768 7429 6020 6f66 2070 6c6f 742e 2054  ght)` of plot. T
-00016c10: 6865 2064 6566 6175 6c74 2068 6569 6768  he default heigh
-00016c20: 7420 6973 2064 6566 696e 6564 2062 790a  t is defined by.
-00016c30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016c40: 6068 656c 7073 6b2e 706c 6f74 2e53 5441  `helpsk.plot.STA
-00016c50: 4e44 4152 445f 4845 4947 4854 602c 2061  NDARD_HEIGHT`, a
-00016c60: 6e64 2074 6865 2064 6566 6175 6c74 2077  nd the default w
-00016c70: 6964 7468 2069 730a 2020 2020 2020 2020  idth is.        
-00016c80: 2020 2020 2020 2020 6068 656c 7073 6b2e          `helpsk.
-00016c90: 706c 6f74 2e53 5441 4e44 4152 445f 4845  plot.STANDARD_HE
-00016ca0: 4947 4854 202f 2068 656c 7073 6b2e 706c  IGHT / helpsk.pl
-00016cb0: 6f74 2e47 4f4c 4445 4e5f 5241 5449 4f60  ot.GOLDEN_RATIO`
-00016cc0: 0a20 2020 2020 2020 2020 2020 2072 6574  .            ret
-00016cd0: 7572 6e5f 706c 6f74 6c79 3a0a 2020 2020  urn_plotly:.    
-00016ce0: 2020 2020 2020 2020 2020 2020 4966 2054              If T
-00016cf0: 7275 652c 2072 6574 7572 6e20 706c 6f74  rue, return plot
-00016d00: 6c79 206f 626a 6563 742e 204f 7468 6572  ly object. Other
-00016d10: 7769 7365 2c20 7573 6520 6d61 7470 6c6f  wise, use matplo
-00016d20: 746c 6962 2061 6e64 2065 6e64 2066 756e  tlib and end fun
-00016d30: 6374 696f 6e20 7769 7468 2063 616c 6c3a  ction with call:
-00016d40: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00016d50: 2060 706c 742e 7469 6768 745f 6c61 796f   `plt.tight_layo
-00016d60: 7574 2829 600a 2020 2020 2020 2020 2222  ut()`.        ""
-00016d70: 220a 2020 2020 2020 2020 706c 742e 6669  ".        plt.fi
-00016d80: 6775 7265 2866 6967 7369 7a65 3d66 6967  gure(figsize=fig
-00016d90: 7572 655f 7369 7a65 290a 2020 2020 2020  ure_size).      
-00016da0: 2020 6175 635f 6375 7276 6520 3d20 7365    auc_curve = se
-00016db0: 6c66 2e5f 6765 745f 6175 635f 6375 7276  lf._get_auc_curv
-00016dc0: 655f 6461 7461 6672 616d 6528 290a 0a20  e_dataframe().. 
-00016dd0: 2020 2020 2020 2069 6620 7265 7475 726e         if return
-00016de0: 5f70 6c6f 746c 793a 0a20 2020 2020 2020  _plotly:.       
-00016df0: 2020 2020 2066 6967 203d 2070 782e 6c69       fig = px.li
-00016e00: 6e65 280a 2020 2020 2020 2020 2020 2020  ne(.            
-00016e10: 2020 2020 6461 7461 5f66 7261 6d65 3d61      data_frame=a
-00016e20: 7563 5f63 7572 7665 2c0a 2020 2020 2020  uc_curve,.      
-00016e30: 2020 2020 2020 2020 2020 783d 2746 616c            x='Fal
-00016e40: 7365 2050 6f73 6974 6976 6520 5261 7465  se Positive Rate
-00016e50: 272c 0a20 2020 2020 2020 2020 2020 2020  ',.             
-00016e60: 2020 2079 3d27 5472 7565 2050 6f73 6974     y='True Posit
-00016e70: 6976 6520 5261 7465 272c 0a20 2020 2020  ive Rate',.     
-00016e80: 2020 2020 2020 2020 2020 2063 6f6c 6f72             color
-00016e90: 5f64 6973 6372 6574 655f 7365 7175 656e  _discrete_sequen
-00016ea0: 6365 3d5b 6863 6f6c 6f72 2e43 6f6c 6f72  ce=[hcolor.Color
-00016eb0: 732e 444f 5645 5f47 5241 592e 7661 6c75  s.DOVE_GRAY.valu
-00016ec0: 655d 2c0a 2020 2020 2020 2020 2020 2020  e],.            
-00016ed0: 2020 2020 6865 6967 6874 3d35 3530 2c0a      height=550,.
-00016ee0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00016ef0: 7769 6474 683d 3535 3020 2a20 474f 4c44  width=550 * GOLD
-00016f00: 454e 5f52 4154 494f 2c0a 2020 2020 2020  EN_RATIO,.      
-00016f10: 2020 2020 2020 2020 2020 7469 746c 653d            title=
-00016f20: 6622 4155 433a 207b 7365 6c66 2e61 7563  f"AUC: {self.auc
-00016f30: 3a2e 3366 7d3c 6272 3e3c 7375 623e 5468  :.3f}<br><sub>Th
-00016f40: 6520 7468 7265 7368 6f6c 6420 6f66 2030  e threshold of 0
-00016f50: 2e35 2069 7320 696e 6469 6361 7465 6420  .5 is indicated 
-00016f60: 7769 7468 2061 206c 6172 6765 2070 6f69  with a large poi
-00016f70: 6e74 2e3c 2f73 7562 3e22 2020 2320 7079  nt.</sub>"  # py
-00016f80: 6c69 6e74 3a20 6469 7361 626c 653d 6c69  lint: disable=li
-00016f90: 6e65 2d74 6f6f 2d6c 6f6e 6720 2023 206e  ne-too-long  # n
-00016fa0: 6f71 610a 2020 2020 2020 2020 2020 2020  oqa.            
-00016fb0: 290a 2020 2020 2020 2020 2020 2020 6669  ).            fi
-00016fc0: 672e 6164 645f 7472 6163 6528 0a20 2020  g.add_trace(.   
-00016fd0: 2020 2020 2020 2020 2020 2020 2070 782e               px.
-00016fe0: 7363 6174 7465 7228 0a20 2020 2020 2020  scatter(.       
-00016ff0: 2020 2020 2020 2020 2020 2020 2064 6174               dat
-00017000: 615f 6672 616d 653d 6175 635f 6375 7276  a_frame=auc_curv
-00017010: 652c 0a20 2020 2020 2020 2020 2020 2020  e,.             
-00017020: 2020 2020 2020 2078 3d27 4661 6c73 6520         x='False 
-00017030: 506f 7369 7469 7665 2052 6174 6527 2c0a  Positive Rate',.
-00017040: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00017050: 2020 2020 793d 2754 7275 6520 506f 7369      y='True Posi
-00017060: 7469 7665 2052 6174 6527 2c0a 2020 2020  tive Rate',.    
-00017070: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00017080: 636f 6c6f 723d 2774 6872 6573 686f 6c64  color='threshold
-00017090: 272c 0a20 2020 2020 2020 2020 2020 2020  ',.             
-000170a0: 2020 2029 2e64 6174 615b 305d 0a20 2020     ).data[0].   
-000170b0: 2020 2020 2020 2020 2029 0a20 2020 2020           ).     
-000170c0: 2020 2020 2020 2066 6967 2e61 6464 5f74         fig.add_t
-000170d0: 7261 6365 280a 2020 2020 2020 2020 2020  race(.          
-000170e0: 2020 2020 2020 7078 2e73 6361 7474 6572        px.scatter
-000170f0: 280a 2020 2020 2020 2020 2020 2020 2020  (.              
-00017100: 2020 2020 2020 6461 7461 5f66 7261 6d65        data_frame
-00017110: 3d61 7563 5f63 7572 7665 2e71 7565 7279  =auc_curve.query
-00017120: 2827 7468 7265 7368 6f6c 6420 3d3d 2030  ('threshold == 0
-00017130: 2e35 2729 2c0a 2020 2020 2020 2020 2020  .5'),.          
-00017140: 2020 2020 2020 2020 2020 783d 2746 616c            x='Fal
-00017150: 7365 2050 6f73 6974 6976 6520 5261 7465  se Positive Rate
-00017160: 272c 0a20 2020 2020 2020 2020 2020 2020  ',.             
-00017170: 2020 2020 2020 2079 3d27 5472 7565 2050         y='True P
-00017180: 6f73 6974 6976 6520 5261 7465 272c 0a20  ositive Rate',. 
-00017190: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000171a0: 2020 2073 697a 653d 5b32 5d2c 0a20 2020     size=[2],.   
-000171b0: 2020 2020 2020 2020 2020 2020 2029 2e64               ).d
-000171c0: 6174 615b 305d 0a20 2020 2020 2020 2020  ata[0].         
-000171d0: 2020 2029 0a20 2020 2020 2020 2020 2020     ).           
-000171e0: 2072 6574 7572 6e20 6669 670a 0a20 2020   return fig..   
-000171f0: 2020 2020 2061 7869 7320 3d20 736e 732e       axis = sns.
-00017200: 6c69 6e65 706c 6f74 2864 6174 613d 6175  lineplot(data=au
-00017210: 635f 6375 7276 652c 2078 3d27 4661 6c73  c_curve, x='Fals
-00017220: 6520 506f 7369 7469 7665 2052 6174 6527  e Positive Rate'
-00017230: 2c20 793d 2754 7275 6520 506f 7369 7469  , y='True Positi
-00017240: 7665 2052 6174 6527 2c20 6369 3d4e 6f6e  ve Rate', ci=Non
-00017250: 6529 0a20 2020 2020 2020 2061 7869 732e  e).        axis.
-00017260: 7365 745f 7469 746c 6528 6622 4155 433a  set_title(f"AUC:
-00017270: 207b 726f 756e 6428 7365 6c66 2e61 7563   {round(self.auc
-00017280: 2c20 3329 7d22 290a 2020 2020 2020 2020  , 3)}").        
-00017290: 666f 7220 692c 2028 782c 2079 2c20 7329  for i, (x, y, s)
-000172a0: 2069 6e20 656e 756d 6572 6174 6528 7a69   in enumerate(zi
-000172b0: 7028 6175 635f 6375 7276 655b 2746 616c  p(auc_curve['Fal
-000172c0: 7365 2050 6f73 6974 6976 6520 5261 7465  se Positive Rate
-000172d0: 275d 2c20 2023 2070 796c 696e 743a 2064  '],  # pylint: d
-000172e0: 6973 6162 6c65 3d69 6e76 616c 6964 2d6e  isable=invalid-n
-000172f0: 616d 650a 2020 2020 2020 2020 2020 2020  ame.            
+00016b70: 2020 2020 2020 205f 6669 6775 7265 2e46         _figure.F
+00016b80: 6967 7572 655d 3a0a 2020 2020 2020 2020  igure]:.        
+00016b90: 2222 2250 6c6f 7473 2074 6865 2052 4f43  """Plots the ROC
+00016ba0: 2041 5543 0a0a 2020 2020 2020 2020 4172   AUC..        Ar
+00016bb0: 6773 3a0a 2020 2020 2020 2020 2020 2020  gs:.            
+00016bc0: 6669 6775 7265 5f73 697a 653a 0a20 2020  figure_size:.   
+00016bd0: 2020 2020 2020 2020 2020 2020 2074 7570               tup
+00016be0: 6c65 2063 6f6e 7461 696e 696e 6720 6028  le containing `(
+00016bf0: 7769 6474 682c 2068 6569 6768 7429 6020  width, height)` 
+00016c00: 6f66 2070 6c6f 742e 2054 6865 2064 6566  of plot. The def
+00016c10: 6175 6c74 2068 6569 6768 7420 6973 2064  ault height is d
+00016c20: 6566 696e 6564 2062 790a 2020 2020 2020  efined by.      
+00016c30: 2020 2020 2020 2020 2020 6068 656c 7073            `helps
+00016c40: 6b2e 706c 6f74 2e53 5441 4e44 4152 445f  k.plot.STANDARD_
+00016c50: 4845 4947 4854 602c 2061 6e64 2074 6865  HEIGHT`, and the
+00016c60: 2064 6566 6175 6c74 2077 6964 7468 2069   default width i
+00016c70: 730a 2020 2020 2020 2020 2020 2020 2020  s.              
+00016c80: 2020 6068 656c 7073 6b2e 706c 6f74 2e53    `helpsk.plot.S
+00016c90: 5441 4e44 4152 445f 4845 4947 4854 202f  TANDARD_HEIGHT /
+00016ca0: 2068 656c 7073 6b2e 706c 6f74 2e47 4f4c   helpsk.plot.GOL
+00016cb0: 4445 4e5f 5241 5449 4f60 0a20 2020 2020  DEN_RATIO`.     
+00016cc0: 2020 2020 2020 2072 6574 7572 6e5f 706c         return_pl
+00016cd0: 6f74 6c79 3a0a 2020 2020 2020 2020 2020  otly:.          
+00016ce0: 2020 2020 2020 4966 2054 7275 652c 2072        If True, r
+00016cf0: 6574 7572 6e20 706c 6f74 6c79 206f 626a  eturn plotly obj
+00016d00: 6563 742e 204f 7468 6572 7769 7365 2c20  ect. Otherwise, 
+00016d10: 7573 6520 6d61 7470 6c6f 746c 6962 2061  use matplotlib a
+00016d20: 6e64 2065 6e64 2066 756e 6374 696f 6e20  nd end function 
+00016d30: 7769 7468 2063 616c 6c3a 0a20 2020 2020  with call:.     
+00016d40: 2020 2020 2020 2020 2020 2060 706c 742e             `plt.
+00016d50: 7469 6768 745f 6c61 796f 7574 2829 600a  tight_layout()`.
+00016d60: 2020 2020 2020 2020 2222 220a 2020 2020          """.    
+00016d70: 2020 2020 706c 742e 6669 6775 7265 2866      plt.figure(f
+00016d80: 6967 7369 7a65 3d66 6967 7572 655f 7369  igsize=figure_si
+00016d90: 7a65 290a 2020 2020 2020 2020 6175 635f  ze).        auc_
+00016da0: 6375 7276 6520 3d20 7365 6c66 2e5f 6765  curve = self._ge
+00016db0: 745f 6175 635f 6375 7276 655f 6461 7461  t_auc_curve_data
+00016dc0: 6672 616d 6528 290a 0a20 2020 2020 2020  frame()..       
+00016dd0: 2069 6620 7265 7475 726e 5f70 6c6f 746c   if return_plotl
+00016de0: 793a 0a20 2020 2020 2020 2020 2020 2066  y:.            f
+00016df0: 6967 203d 2070 782e 6c69 6e65 280a 2020  ig = px.line(.  
+00016e00: 2020 2020 2020 2020 2020 2020 2020 6461                da
+00016e10: 7461 5f66 7261 6d65 3d61 7563 5f63 7572  ta_frame=auc_cur
+00016e20: 7665 2c0a 2020 2020 2020 2020 2020 2020  ve,.            
+00016e30: 2020 2020 783d 2746 616c 7365 2050 6f73      x='False Pos
+00016e40: 6974 6976 6520 5261 7465 272c 0a20 2020  itive Rate',.   
+00016e50: 2020 2020 2020 2020 2020 2020 2079 3d27               y='
+00016e60: 5472 7565 2050 6f73 6974 6976 6520 5261  True Positive Ra
+00016e70: 7465 272c 0a20 2020 2020 2020 2020 2020  te',.           
+00016e80: 2020 2020 2063 6f6c 6f72 5f64 6973 6372       color_discr
+00016e90: 6574 655f 7365 7175 656e 6365 3d5b 6863  ete_sequence=[hc
+00016ea0: 6f6c 6f72 2e43 6f6c 6f72 732e 444f 5645  olor.Colors.DOVE
+00016eb0: 5f47 5241 592e 7661 6c75 655d 2c0a 2020  _GRAY.value],.  
+00016ec0: 2020 2020 2020 2020 2020 2020 2020 6865                he
+00016ed0: 6967 6874 3d35 3530 2c0a 2020 2020 2020  ight=550,.      
+00016ee0: 2020 2020 2020 2020 2020 7769 6474 683d            width=
+00016ef0: 3535 3020 2a20 474f 4c44 454e 5f52 4154  550 * GOLDEN_RAT
+00016f00: 494f 2c0a 2020 2020 2020 2020 2020 2020  IO,.            
+00016f10: 2020 2020 7469 746c 653d 6622 4155 433a      title=f"AUC:
+00016f20: 207b 7365 6c66 2e61 7563 3a2e 3366 7d3c   {self.auc:.3f}<
+00016f30: 6272 3e3c 7375 623e 5468 6520 7468 7265  br><sub>The thre
+00016f40: 7368 6f6c 6420 6f66 2030 2e35 2069 7320  shold of 0.5 is 
+00016f50: 696e 6469 6361 7465 6420 7769 7468 2061  indicated with a
+00016f60: 206c 6172 6765 2070 6f69 6e74 2e3c 2f73   large point.</s
+00016f70: 7562 3e22 2020 2320 7079 6c69 6e74 3a20  ub>"  # pylint: 
+00016f80: 6469 7361 626c 653d 6c69 6e65 2d74 6f6f  disable=line-too
+00016f90: 2d6c 6f6e 6720 2023 206e 6f71 610a 2020  -long  # noqa.  
+00016fa0: 2020 2020 2020 2020 2020 290a 2020 2020            ).    
+00016fb0: 2020 2020 2020 2020 6669 672e 6164 645f          fig.add_
+00016fc0: 7472 6163 6528 0a20 2020 2020 2020 2020  trace(.         
+00016fd0: 2020 2020 2020 2070 782e 7363 6174 7465         px.scatte
+00016fe0: 7228 0a20 2020 2020 2020 2020 2020 2020  r(.             
+00016ff0: 2020 2020 2020 2064 6174 615f 6672 616d         data_fram
+00017000: 653d 6175 635f 6375 7276 652c 0a20 2020  e=auc_curve,.   
+00017010: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00017020: 2078 3d27 4661 6c73 6520 506f 7369 7469   x='False Positi
+00017030: 7665 2052 6174 6527 2c0a 2020 2020 2020  ve Rate',.      
+00017040: 2020 2020 2020 2020 2020 2020 2020 793d                y=
+00017050: 2754 7275 6520 506f 7369 7469 7665 2052  'True Positive R
+00017060: 6174 6527 2c0a 2020 2020 2020 2020 2020  ate',.          
+00017070: 2020 2020 2020 2020 2020 636f 6c6f 723d            color=
+00017080: 2774 6872 6573 686f 6c64 272c 0a20 2020  'threshold',.   
+00017090: 2020 2020 2020 2020 2020 2020 2029 2e64               ).d
+000170a0: 6174 615b 305d 0a20 2020 2020 2020 2020  ata[0].         
+000170b0: 2020 2029 0a20 2020 2020 2020 2020 2020     ).           
+000170c0: 2066 6967 2e61 6464 5f74 7261 6365 280a   fig.add_trace(.
+000170d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000170e0: 7078 2e73 6361 7474 6572 280a 2020 2020  px.scatter(.    
+000170f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00017100: 6461 7461 5f66 7261 6d65 3d61 7563 5f63  data_frame=auc_c
+00017110: 7572 7665 2e71 7565 7279 2827 7468 7265  urve.query('thre
+00017120: 7368 6f6c 6420 3d3d 2030 2e35 2729 2c0a  shold == 0.5'),.
+00017130: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00017140: 2020 2020 783d 2746 616c 7365 2050 6f73      x='False Pos
+00017150: 6974 6976 6520 5261 7465 272c 0a20 2020  itive Rate',.   
+00017160: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00017170: 2079 3d27 5472 7565 2050 6f73 6974 6976   y='True Positiv
+00017180: 6520 5261 7465 272c 0a20 2020 2020 2020  e Rate',.       
+00017190: 2020 2020 2020 2020 2020 2020 2073 697a               siz
+000171a0: 653d 5b32 5d2c 0a20 2020 2020 2020 2020  e=[2],.         
+000171b0: 2020 2020 2020 2029 2e64 6174 615b 305d         ).data[0]
+000171c0: 0a20 2020 2020 2020 2020 2020 2029 0a20  .            ). 
+000171d0: 2020 2020 2020 2020 2020 2072 6574 7572             retur
+000171e0: 6e20 6669 670a 0a20 2020 2020 2020 2061  n fig..        a
+000171f0: 7869 7320 3d20 736e 732e 6c69 6e65 706c  xis = sns.linepl
+00017200: 6f74 2864 6174 613d 6175 635f 6375 7276  ot(data=auc_curv
+00017210: 652c 2078 3d27 4661 6c73 6520 506f 7369  e, x='False Posi
+00017220: 7469 7665 2052 6174 6527 2c20 793d 2754  tive Rate', y='T
+00017230: 7275 6520 506f 7369 7469 7665 2052 6174  rue Positive Rat
+00017240: 6527 2c20 6369 3d4e 6f6e 6529 0a20 2020  e', ci=None).   
+00017250: 2020 2020 2061 7869 732e 7365 745f 7469       axis.set_ti
+00017260: 746c 6528 6622 4155 433a 207b 726f 756e  tle(f"AUC: {roun
+00017270: 6428 7365 6c66 2e61 7563 2c20 3329 7d22  d(self.auc, 3)}"
+00017280: 290a 2020 2020 2020 2020 666f 7220 692c  ).        for i,
+00017290: 2028 782c 2079 2c20 7329 2069 6e20 656e   (x, y, s) in en
+000172a0: 756d 6572 6174 6528 7a69 7028 6175 635f  umerate(zip(auc_
+000172b0: 6375 7276 655b 2746 616c 7365 2050 6f73  curve['False Pos
+000172c0: 6974 6976 6520 5261 7465 275d 2c20 2023  itive Rate'],  #
+000172d0: 2070 796c 696e 743a 2064 6973 6162 6c65   pylint: disable
+000172e0: 3d69 6e76 616c 6964 2d6e 616d 650a 2020  =invalid-name.  
+000172f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00017300: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00017310: 2020 2020 2020 2020 2020 2020 2020 6175                au
-00017320: 635f 6375 7276 655b 2754 7275 6520 506f  c_curve['True Po
-00017330: 7369 7469 7665 2052 6174 6527 5d2c 0a20  sitive Rate'],. 
+00017310: 2020 2020 2020 2020 6175 635f 6375 7276          auc_curv
+00017320: 655b 2754 7275 6520 506f 7369 7469 7665  e['True Positive
+00017330: 2052 6174 6527 5d2c 0a20 2020 2020 2020   Rate'],.       
 00017340: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00017350: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00017360: 2020 2020 2020 2020 2061 7563 5f63 7572           auc_cur
-00017370: 7665 5b27 7468 7265 7368 6f6c 6427 5d29  ve['threshold'])
-00017380: 293a 0a20 2020 2020 2020 2020 2020 2069  ):.            i
-00017390: 6620 6920 2520 3520 3d3d 2030 3a0a 2020  f i % 5 == 0:.  
-000173a0: 2020 2020 2020 2020 2020 2020 2020 6178                ax
-000173b0: 6973 2e74 6578 7428 782c 2079 2c20 6627  is.text(x, y, f'
-000173c0: 7b73 3a2e 337d 2729 0a20 2020 2020 2020  {s:.3}').       
-000173d0: 2061 7869 732e 7365 745f 7874 6963 6b73   axis.set_xticks
-000173e0: 286e 702e 6172 616e 6765 2830 2c20 312e  (np.arange(0, 1.
-000173f0: 312c 202e 3129 290a 2020 2020 2020 2020  1, .1)).        
-00017400: 6178 6973 2e73 6574 5f79 7469 636b 7328  axis.set_yticks(
-00017410: 6e70 2e61 7261 6e67 6528 302c 2031 2e31  np.arange(0, 1.1
-00017420: 2c20 2e31 2929 0a20 2020 2020 2020 2070  , .1)).        p
-00017430: 6c74 2e67 7269 6428 290a 2020 2020 2020  lt.grid().      
-00017440: 2020 706c 742e 7469 6768 745f 6c61 796f    plt.tight_layo
-00017450: 7574 2829 0a0a 2020 2020 2320 7079 6c69  ut()..    # pyli
-00017460: 6e74 3a20 6469 7361 626c 653d 696e 636f  nt: disable=inco
-00017470: 6e73 6973 7465 6e74 2d72 6574 7572 6e2d  nsistent-return-
-00017480: 7374 6174 656d 656e 7473 0a20 2020 2064  statements.    d
-00017490: 6566 2070 6c6f 745f 7468 7265 7368 6f6c  ef plot_threshol
-000174a0: 645f 6375 7276 6573 2873 656c 662c 0a20  d_curves(self,. 
+00017360: 2020 2061 7563 5f63 7572 7665 5b27 7468     auc_curve['th
+00017370: 7265 7368 6f6c 6427 5d29 293a 0a20 2020  reshold'])):.   
+00017380: 2020 2020 2020 2020 2069 6620 6920 2520           if i % 
+00017390: 3520 3d3d 2030 3a0a 2020 2020 2020 2020  5 == 0:.        
+000173a0: 2020 2020 2020 2020 6178 6973 2e74 6578          axis.tex
+000173b0: 7428 782c 2079 2c20 6627 7b73 3a2e 337d  t(x, y, f'{s:.3}
+000173c0: 2729 0a20 2020 2020 2020 2061 7869 732e  ').        axis.
+000173d0: 7365 745f 7874 6963 6b73 286e 702e 6172  set_xticks(np.ar
+000173e0: 616e 6765 2830 2c20 312e 312c 202e 3129  ange(0, 1.1, .1)
+000173f0: 290a 2020 2020 2020 2020 6178 6973 2e73  ).        axis.s
+00017400: 6574 5f79 7469 636b 7328 6e70 2e61 7261  et_yticks(np.ara
+00017410: 6e67 6528 302c 2031 2e31 2c20 2e31 2929  nge(0, 1.1, .1))
+00017420: 0a20 2020 2020 2020 2070 6c74 2e67 7269  .        plt.gri
+00017430: 6428 290a 2020 2020 2020 2020 706c 742e  d().        plt.
+00017440: 7469 6768 745f 6c61 796f 7574 2829 0a0a  tight_layout()..
+00017450: 2020 2020 2320 7079 6c69 6e74 3a20 6469      # pylint: di
+00017460: 7361 626c 653d 696e 636f 6e73 6973 7465  sable=inconsiste
+00017470: 6e74 2d72 6574 7572 6e2d 7374 6174 656d  nt-return-statem
+00017480: 656e 7473 0a20 2020 2064 6566 2070 6c6f  ents.    def plo
+00017490: 745f 7468 7265 7368 6f6c 645f 6375 7276  t_threshold_curv
+000174a0: 6573 2873 656c 662c 0a20 2020 2020 2020  es(self,.       
 000174b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000174c0: 2020 2020 2020 2020 2020 2020 2073 636f               sco
-000174d0: 7265 5f74 6872 6573 686f 6c64 5f72 616e  re_threshold_ran
-000174e0: 6765 3a20 5475 706c 655b 666c 6f61 742c  ge: Tuple[float,
-000174f0: 2066 6c6f 6174 5d20 3d20 2830 2e31 2c20   float] = (0.1, 
-00017500: 302e 3929 2c0a 2020 2020 2020 2020 2020  0.9),.          
-00017510: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00017520: 2020 2020 6669 6775 7265 5f73 697a 653a      figure_size:
-00017530: 2074 7570 6c65 203d 2053 5441 4e44 4152   tuple = STANDAR
-00017540: 445f 5749 4454 485f 4845 4947 4854 2c0a  D_WIDTH_HEIGHT,.
+000174c0: 2020 2020 2020 2073 636f 7265 5f74 6872         score_thr
+000174d0: 6573 686f 6c64 5f72 616e 6765 3a20 5475  eshold_range: Tu
+000174e0: 706c 655b 666c 6f61 742c 2066 6c6f 6174  ple[float, float
+000174f0: 5d20 3d20 2830 2e31 2c20 302e 3929 2c0a  ] = (0.1, 0.9),.
+00017500: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00017510: 2020 2020 2020 2020 2020 2020 2020 6669                fi
+00017520: 6775 7265 5f73 697a 653a 2074 7570 6c65  gure_size: tuple
+00017530: 203d 2053 5441 4e44 4152 445f 5749 4454   = STANDARD_WIDT
+00017540: 485f 4845 4947 4854 2c0a 2020 2020 2020  H_HEIGHT,.      
 00017550: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00017560: 2020 2020 2020 2020 2020 2020 2020 7265                re
-00017570: 7475 726e 5f70 6c6f 746c 793a 2062 6f6f  turn_plotly: boo
-00017580: 6c20 3d20 4661 6c73 6529 202d 3e20 556e  l = False) -> Un
-00017590: 696f 6e5b 4e6f 6e65 2c0a 2020 2020 2020  ion[None,.      
+00017560: 2020 2020 2020 2020 7265 7475 726e 5f70          return_p
+00017570: 6c6f 746c 793a 2062 6f6f 6c20 3d20 4661  lotly: bool = Fa
+00017580: 6c73 6529 202d 3e20 556e 696f 6e5b 4e6f  lse) -> Union[No
+00017590: 6e65 2c0a 2020 2020 2020 2020 2020 2020  ne,.            
 000175a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000175b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000175c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000175d0: 2020 2020 2020 2020 2020 2020 2020 5f66                _f
-000175e0: 6967 7572 652e 4669 6775 7265 5d3a 0a20  igure.Figure]:. 
-000175f0: 2020 2020 2020 2022 2222 506c 6f74 7320         """Plots 
-00017600: 7661 7269 6f75 7320 7363 6f72 6573 2028  various scores (
-00017610: 652e 672e 2054 7275 6520 506f 7369 7469  e.g. True Positi
-00017620: 7665 2052 6174 652c 2046 616c 7365 2050  ve Rate, False P
-00017630: 6f73 6974 6976 6520 5261 7465 2c20 6574  ositive Rate, et
-00017640: 632e 2920 666f 7220 7661 7269 6f75 7320  c.) for various 
-00017650: 7363 6f72 650a 2020 2020 2020 2020 7468  score.        th
-00017660: 7265 7368 6f6c 6473 2e20 2841 2073 636f  resholds. (A sco
-00017670: 7265 2074 6872 6573 686f 6c64 2069 7320  re threshold is 
-00017680: 7468 6520 7661 6c75 6520 666f 7220 7768  the value for wh
-00017690: 6963 6820 796f 7520 776f 756c 6420 7072  ich you would pr
-000176a0: 6564 6963 7420 6120 706f 7369 7469 7665  edict a positive
-000176b0: 206c 6162 656c 2069 6620 7468 650a 2020   label if the.  
-000176c0: 2020 2020 2020 7661 6c75 6520 6f66 2074        value of t
-000176d0: 6865 2073 636f 7265 2069 7320 6162 6f76  he score is abov
-000176e0: 6520 7468 6520 7468 7265 7368 6f6c 6420  e the threshold 
-000176f0: 2865 2e67 2e20 7573 7561 6c6c 7920 302e  (e.g. usually 0.
-00017700: 3529 2e0a 0a20 2020 2020 2020 2041 7267  5)...        Arg
-00017710: 733a 0a20 2020 2020 2020 2020 2020 2073  s:.            s
-00017720: 636f 7265 5f74 6872 6573 686f 6c64 5f72  core_threshold_r
-00017730: 616e 6765 3a0a 2020 2020 2020 2020 2020  ange:.          
-00017740: 2020 2020 2020 7261 6e67 6520 6f66 2073        range of s
-00017750: 636f 7265 2074 6872 6573 686f 6c64 7320  core thresholds 
-00017760: 746f 2070 6c6f 7420 2878 2d61 7869 7329  to plot (x-axis)
-00017770: 3b20 7475 706c 6520 7769 7468 206d 696e  ; tuple with min
-00017780: 696d 756d 2074 6872 6573 686f 6c64 2069  imum threshold i
-00017790: 6e20 6669 7273 7420 696e 6465 7820 616e  n first index an
-000177a0: 640a 2020 2020 2020 2020 2020 2020 2020  d.              
-000177b0: 2020 6d61 7869 6d75 6d20 7468 7265 7368    maximum thresh
-000177c0: 6f6c 6420 696e 2073 6563 6f6e 6420 696e  old in second in
-000177d0: 6465 782e 0a20 2020 2020 2020 2020 2020  dex..           
-000177e0: 2066 6967 7572 655f 7369 7a65 3a0a 2020   figure_size:.  
-000177f0: 2020 2020 2020 2020 2020 2020 2020 7475                tu
-00017800: 706c 6520 636f 6e74 6169 6e69 6e67 2060  ple containing `
-00017810: 2877 6964 7468 2c20 6865 6967 6874 2960  (width, height)`
-00017820: 206f 6620 706c 6f74 2e20 5468 6520 6465   of plot. The de
-00017830: 6661 756c 7420 6865 6967 6874 2069 7320  fault height is 
-00017840: 6465 6669 6e65 6420 6279 0a20 2020 2020  defined by.     
-00017850: 2020 2020 2020 2020 2020 2060 6865 6c70             `help
-00017860: 736b 2e70 6c6f 742e 5354 414e 4441 5244  sk.plot.STANDARD
-00017870: 5f48 4549 4748 5460 2c20 616e 6420 7468  _HEIGHT`, and th
-00017880: 6520 6465 6661 756c 7420 7769 6474 6820  e default width 
-00017890: 6973 0a20 2020 2020 2020 2020 2020 2020  is.             
-000178a0: 2020 2060 6865 6c70 736b 2e70 6c6f 742e     `helpsk.plot.
-000178b0: 5354 414e 4441 5244 5f48 4549 4748 5420  STANDARD_HEIGHT 
-000178c0: 2f20 6865 6c70 736b 2e70 6c6f 742e 474f  / helpsk.plot.GO
-000178d0: 4c44 454e 5f52 4154 494f 600a 2020 2020  LDEN_RATIO`.    
-000178e0: 2020 2020 2020 2020 7265 7475 726e 5f70          return_p
-000178f0: 6c6f 746c 793a 0a20 2020 2020 2020 2020  lotly:.         
-00017900: 2020 2020 2020 2049 6620 5472 7565 2c20         If True, 
-00017910: 7265 7475 726e 2070 6c6f 746c 7920 6f62  return plotly ob
-00017920: 6a65 6374 2e20 4f74 6865 7277 6973 652c  ject. Otherwise,
-00017930: 2075 7365 206d 6174 706c 6f74 6c69 6220   use matplotlib 
-00017940: 616e 6420 656e 6420 6675 6e63 7469 6f6e  and end function
-00017950: 2077 6974 6820 6361 6c6c 3a0a 2020 2020   with call:.    
-00017960: 2020 2020 2020 2020 2020 2020 6070 6c74              `plt
-00017970: 2e74 6967 6874 5f6c 6179 6f75 7428 2960  .tight_layout()`
-00017980: 0a20 2020 2020 2020 2022 2222 0a20 2020  .        """.   
-00017990: 2020 2020 2070 6c74 2e66 6967 7572 6528       plt.figure(
-000179a0: 6669 6773 697a 653d 6669 6775 7265 5f73  figsize=figure_s
-000179b0: 697a 6529 0a0a 2020 2020 2020 2020 7468  ize)..        th
-000179c0: 7265 7368 6f6c 645f 6375 7276 6573 203d  reshold_curves =
-000179d0: 2073 656c 662e 5f67 6574 5f74 6872 6573   self._get_thres
-000179e0: 686f 6c64 5f63 7572 7665 5f64 6174 6166  hold_curve_dataf
-000179f0: 7261 6d65 2873 636f 7265 5f74 6872 6573  rame(score_thres
-00017a00: 686f 6c64 5f72 616e 6765 3d73 636f 7265  hold_range=score
-00017a10: 5f74 6872 6573 686f 6c64 5f72 616e 6765  _threshold_range
-00017a20: 290a 0a20 2020 2020 2020 2069 6620 7265  )..        if re
-00017a30: 7475 726e 5f70 6c6f 746c 793a 0a20 2020  turn_plotly:.   
-00017a40: 2020 2020 2020 2020 2063 7573 746f 6d5f           custom_
-00017a50: 636f 6c6f 7273 203d 205b 0a20 2020 2020  colors = [.     
-00017a60: 2020 2020 2020 2020 2020 2068 636f 6c6f             hcolo
-00017a70: 722e 436f 6c6f 7273 2e50 4153 5445 4c5f  r.Colors.PASTEL_
-00017a80: 424c 5545 2e76 616c 7565 2c0a 2020 2020  BLUE.value,.    
-00017a90: 2020 2020 2020 2020 2020 2020 6863 6f6c              hcol
-00017aa0: 6f72 2e43 6f6c 6f72 732e 4355 5354 4f4d  or.Colors.CUSTOM
-00017ab0: 5f47 5245 454e 2e76 616c 7565 2c0a 2020  _GREEN.value,.  
-00017ac0: 2020 2020 2020 2020 2020 2020 2020 6863                hc
-00017ad0: 6f6c 6f72 2e43 6f6c 6f72 732e 5945 4c4c  olor.Colors.YELL
-00017ae0: 4f57 5f50 4550 5045 522e 7661 6c75 652c  OW_PEPPER.value,
-00017af0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00017b00: 2068 636f 6c6f 722e 436f 6c6f 7273 2e43   hcolor.Colors.C
-00017b10: 5241 494c 2e76 616c 7565 2c0a 2020 2020  RAIL.value,.    
-00017b20: 2020 2020 2020 2020 2020 2020 6863 6f6c              hcol
-00017b30: 6f72 2e43 6f6c 6f72 732e 4341 444d 4955  or.Colors.CADMIU
-00017b40: 4d5f 4f52 414e 4745 2e76 616c 7565 2c0a  M_ORANGE.value,.
-00017b50: 2020 2020 2020 2020 2020 2020 5d0a 2020              ].  
-00017b60: 2020 2020 2020 2020 2020 6669 6720 3d20            fig = 
-00017b70: 7078 2e6c 696e 6528 0a20 2020 2020 2020  px.line(.       
-00017b80: 2020 2020 2020 2020 2064 6174 615f 6672           data_fr
-00017b90: 616d 653d 7064 2e6d 656c 7428 6672 616d  ame=pd.melt(fram
-00017ba0: 653d 7468 7265 7368 6f6c 645f 6375 7276  e=threshold_curv
-00017bb0: 6573 2c20 6964 5f76 6172 733d 5b27 5363  es, id_vars=['Sc
-00017bc0: 6f72 6520 5468 7265 7368 6f6c 6427 5d29  ore Threshold'])
-00017bd0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00017be0: 2020 783d 2753 636f 7265 2054 6872 6573    x='Score Thres
-00017bf0: 686f 6c64 272c 0a20 2020 2020 2020 2020  hold',.         
-00017c00: 2020 2020 2020 2079 3d27 7661 6c75 6527         y='value'
-00017c10: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00017c20: 2020 636f 6c6f 723d 2776 6172 6961 626c    color='variabl
-00017c30: 6527 2c0a 2020 2020 2020 2020 2020 2020  e',.            
-00017c40: 2020 2020 636f 6c6f 725f 6469 7363 7265      color_discre
-00017c50: 7465 5f73 6571 7565 6e63 653d 6375 7374  te_sequence=cust
-00017c60: 6f6d 5f63 6f6c 6f72 732c 0a20 2020 2020  om_colors,.     
-00017c70: 2020 2020 2020 2020 2020 206c 6162 656c             label
-00017c80: 733d 7b0a 2020 2020 2020 2020 2020 2020  s={.            
-00017c90: 2020 2020 2020 2020 2776 6172 6961 626c          'variabl
-00017ca0: 6527 3a20 2752 6174 6520 5479 7065 272c  e': 'Rate Type',
-00017cb0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-00017cc0: 2020 2020 2027 7661 6c75 6527 3a20 2752       'value': 'R
-00017cd0: 6174 6527 0a20 2020 2020 2020 2020 2020  ate'.           
-00017ce0: 2020 2020 207d 2c0a 2020 2020 2020 2020       },.        
-00017cf0: 2020 2020 2020 2020 6865 6967 6874 3d35          height=5
-00017d00: 3530 2c0a 2020 2020 2020 2020 2020 2020  50,.            
-00017d10: 2020 2020 7769 6474 683d 3535 3020 2a20      width=550 * 
-00017d20: 474f 4c44 454e 5f52 4154 494f 2c0a 2020  GOLDEN_RATIO,.  
-00017d30: 2020 2020 2020 2020 2020 2020 2020 7469                ti
-00017d40: 746c 653d 2254 7261 6465 6f66 6673 2041  tle="Tradeoffs A
-00017d50: 6372 6f73 7320 5661 7269 6f75 7320 5363  cross Various Sc
-00017d60: 6f72 6520 5468 7265 7368 6f6c 6473 3c62  ore Thresholds<b
-00017d70: 723e 3c73 7562 3e42 6c61 636b 206c 696e  r><sub>Black lin
-00017d80: 6520 6973 2064 6566 6175 6c74 2074 6872  e is default thr
-00017d90: 6573 686f 6c64 206f 6620 302e 352e 3c2f  eshold of 0.5.</
-00017da0: 7375 623e 2220 2023 2070 796c 696e 743a  sub>"  # pylint:
-00017db0: 2064 6973 6162 6c65 3d6c 696e 652d 746f   disable=line-to
-00017dc0: 6f2d 6c6f 6e67 2020 2320 6e6f 7161 0a20  o-long  # noqa. 
-00017dd0: 2020 2020 2020 2020 2020 2029 0a20 2020             ).   
-00017de0: 2020 2020 2020 2020 2066 6967 203d 2066           fig = f
-00017df0: 6967 2e61 6464 5f76 6c69 6e65 2878 3d30  ig.add_vline(x=0
-00017e00: 2e35 2c20 6c69 6e65 5f63 6f6c 6f72 3d68  .5, line_color=h
-00017e10: 636f 6c6f 722e 436f 6c6f 7273 2e42 4c41  color.Colors.BLA
-00017e20: 434b 5f53 4841 444f 572e 7661 6c75 6529  CK_SHADOW.value)
-00017e30: 0a20 2020 2020 2020 2020 2020 2072 6574  .            ret
-00017e40: 7572 6e20 6669 670a 0a20 2020 2020 2020  urn fig..       
-00017e50: 2061 7869 7320 3d20 736e 732e 6c69 6e65   axis = sns.line
-00017e60: 706c 6f74 2878 3d27 5363 6f72 6520 5468  plot(x='Score Th
-00017e70: 7265 7368 6f6c 6427 2c20 793d 2776 616c  reshold', y='val
-00017e80: 7565 272c 2068 7565 3d27 7661 7269 6162  ue', hue='variab
-00017e90: 6c65 272c 0a20 2020 2020 2020 2020 2020  le',.           
-00017ea0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00017eb0: 2064 6174 613d 7064 2e6d 656c 7428 6672   data=pd.melt(fr
-00017ec0: 616d 653d 7468 7265 7368 6f6c 645f 6375  ame=threshold_cu
-00017ed0: 7276 6573 2c20 6964 5f76 6172 733d 5b27  rves, id_vars=['
-00017ee0: 5363 6f72 6520 5468 7265 7368 6f6c 6427  Score Threshold'
-00017ef0: 5d29 290a 2020 2020 2020 2020 6178 6973  ])).        axis
-00017f00: 2e73 6574 5f78 7469 636b 7328 6e70 2e61  .set_xticks(np.a
-00017f10: 7261 6e67 6528 7363 6f72 655f 7468 7265  range(score_thre
-00017f20: 7368 6f6c 645f 7261 6e67 655b 305d 2c20  shold_range[0], 
-00017f30: 7363 6f72 655f 7468 7265 7368 6f6c 645f  score_threshold_
-00017f40: 7261 6e67 655b 315d 202b 2030 2e31 2c20  range[1] + 0.1, 
-00017f50: 302e 3129 290a 2020 2020 2020 2020 6178  0.1)).        ax
-00017f60: 6973 2e73 6574 5f79 7469 636b 7328 6e70  is.set_yticks(np
-00017f70: 2e61 7261 6e67 6528 302c 2031 2e31 2c20  .arange(0, 1.1, 
-00017f80: 2e31 2929 0a20 2020 2020 2020 2070 6c74  .1)).        plt
-00017f90: 2e76 6c69 6e65 7328 783d 7365 6c66 2e73  .vlines(x=self.s
-00017fa0: 636f 7265 5f74 6872 6573 686f 6c64 2c20  core_threshold, 
-00017fb0: 796d 696e 3d30 2c20 796d 6178 3d31 2c20  ymin=0, ymax=1, 
-00017fc0: 636f 6c6f 7273 3d27 626c 6163 6b27 290a  colors='black').
-00017fd0: 2020 2020 2020 2020 706c 742e 6772 6964          plt.grid
-00017fe0: 2829 0a20 2020 2020 2020 2070 6c74 2e74  ().        plt.t
-00017ff0: 6967 6874 5f6c 6179 6f75 7428 290a 0a20  ight_layout().. 
-00018000: 2020 2023 2070 796c 696e 743a 2064 6973     # pylint: dis
-00018010: 6162 6c65 3d69 6e63 6f6e 7369 7374 656e  able=inconsisten
-00018020: 742d 7265 7475 726e 2d73 7461 7465 6d65  t-return-stateme
-00018030: 6e74 730a 2020 2020 6465 6620 706c 6f74  nts.    def plot
-00018040: 5f70 7265 6369 7369 6f6e 5f72 6563 616c  _precision_recal
-00018050: 6c5f 7472 6164 656f 6666 2873 656c 662c  l_tradeoff(self,
-00018060: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000175d0: 2020 2020 2020 2020 5f66 6967 7572 652e          _figure.
+000175e0: 4669 6775 7265 5d3a 0a20 2020 2020 2020  Figure]:.       
+000175f0: 2022 2222 506c 6f74 7320 7661 7269 6f75   """Plots variou
+00017600: 7320 7363 6f72 6573 2028 652e 672e 2054  s scores (e.g. T
+00017610: 7275 6520 506f 7369 7469 7665 2052 6174  rue Positive Rat
+00017620: 652c 2046 616c 7365 2050 6f73 6974 6976  e, False Positiv
+00017630: 6520 5261 7465 2c20 6574 632e 2920 666f  e Rate, etc.) fo
+00017640: 7220 7661 7269 6f75 7320 7363 6f72 650a  r various score.
+00017650: 2020 2020 2020 2020 7468 7265 7368 6f6c          threshol
+00017660: 6473 2e20 2841 2073 636f 7265 2074 6872  ds. (A score thr
+00017670: 6573 686f 6c64 2069 7320 7468 6520 7661  eshold is the va
+00017680: 6c75 6520 666f 7220 7768 6963 6820 796f  lue for which yo
+00017690: 7520 776f 756c 6420 7072 6564 6963 7420  u would predict 
+000176a0: 6120 706f 7369 7469 7665 206c 6162 656c  a positive label
+000176b0: 2069 6620 7468 650a 2020 2020 2020 2020   if the.        
+000176c0: 7661 6c75 6520 6f66 2074 6865 2073 636f  value of the sco
+000176d0: 7265 2069 7320 6162 6f76 6520 7468 6520  re is above the 
+000176e0: 7468 7265 7368 6f6c 6420 2865 2e67 2e20  threshold (e.g. 
+000176f0: 7573 7561 6c6c 7920 302e 3529 2e0a 0a20  usually 0.5)... 
+00017700: 2020 2020 2020 2041 7267 733a 0a20 2020         Args:.   
+00017710: 2020 2020 2020 2020 2073 636f 7265 5f74           score_t
+00017720: 6872 6573 686f 6c64 5f72 616e 6765 3a0a  hreshold_range:.
+00017730: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00017740: 7261 6e67 6520 6f66 2073 636f 7265 2074  range of score t
+00017750: 6872 6573 686f 6c64 7320 746f 2070 6c6f  hresholds to plo
+00017760: 7420 2878 2d61 7869 7329 3b20 7475 706c  t (x-axis); tupl
+00017770: 6520 7769 7468 206d 696e 696d 756d 2074  e with minimum t
+00017780: 6872 6573 686f 6c64 2069 6e20 6669 7273  hreshold in firs
+00017790: 7420 696e 6465 7820 616e 640a 2020 2020  t index and.    
+000177a0: 2020 2020 2020 2020 2020 2020 6d61 7869              maxi
+000177b0: 6d75 6d20 7468 7265 7368 6f6c 6420 696e  mum threshold in
+000177c0: 2073 6563 6f6e 6420 696e 6465 782e 0a20   second index.. 
+000177d0: 2020 2020 2020 2020 2020 2066 6967 7572             figur
+000177e0: 655f 7369 7a65 3a0a 2020 2020 2020 2020  e_size:.        
+000177f0: 2020 2020 2020 2020 7475 706c 6520 636f          tuple co
+00017800: 6e74 6169 6e69 6e67 2060 2877 6964 7468  ntaining `(width
+00017810: 2c20 6865 6967 6874 2960 206f 6620 706c  , height)` of pl
+00017820: 6f74 2e20 5468 6520 6465 6661 756c 7420  ot. The default 
+00017830: 6865 6967 6874 2069 7320 6465 6669 6e65  height is define
+00017840: 6420 6279 0a20 2020 2020 2020 2020 2020  d by.           
+00017850: 2020 2020 2060 6865 6c70 736b 2e70 6c6f       `helpsk.plo
+00017860: 742e 5354 414e 4441 5244 5f48 4549 4748  t.STANDARD_HEIGH
+00017870: 5460 2c20 616e 6420 7468 6520 6465 6661  T`, and the defa
+00017880: 756c 7420 7769 6474 6820 6973 0a20 2020  ult width is.   
+00017890: 2020 2020 2020 2020 2020 2020 2060 6865               `he
+000178a0: 6c70 736b 2e70 6c6f 742e 5354 414e 4441  lpsk.plot.STANDA
+000178b0: 5244 5f48 4549 4748 5420 2f20 6865 6c70  RD_HEIGHT / help
+000178c0: 736b 2e70 6c6f 742e 474f 4c44 454e 5f52  sk.plot.GOLDEN_R
+000178d0: 4154 494f 600a 2020 2020 2020 2020 2020  ATIO`.          
+000178e0: 2020 7265 7475 726e 5f70 6c6f 746c 793a    return_plotly:
+000178f0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00017900: 2049 6620 5472 7565 2c20 7265 7475 726e   If True, return
+00017910: 2070 6c6f 746c 7920 6f62 6a65 6374 2e20   plotly object. 
+00017920: 4f74 6865 7277 6973 652c 2075 7365 206d  Otherwise, use m
+00017930: 6174 706c 6f74 6c69 6220 616e 6420 656e  atplotlib and en
+00017940: 6420 6675 6e63 7469 6f6e 2077 6974 6820  d function with 
+00017950: 6361 6c6c 3a0a 2020 2020 2020 2020 2020  call:.          
+00017960: 2020 2020 2020 6070 6c74 2e74 6967 6874        `plt.tight
+00017970: 5f6c 6179 6f75 7428 2960 0a20 2020 2020  _layout()`.     
+00017980: 2020 2022 2222 0a20 2020 2020 2020 2070     """.        p
+00017990: 6c74 2e66 6967 7572 6528 6669 6773 697a  lt.figure(figsiz
+000179a0: 653d 6669 6775 7265 5f73 697a 6529 0a0a  e=figure_size)..
+000179b0: 2020 2020 2020 2020 7468 7265 7368 6f6c          threshol
+000179c0: 645f 6375 7276 6573 203d 2073 656c 662e  d_curves = self.
+000179d0: 5f67 6574 5f74 6872 6573 686f 6c64 5f63  _get_threshold_c
+000179e0: 7572 7665 5f64 6174 6166 7261 6d65 2873  urve_dataframe(s
+000179f0: 636f 7265 5f74 6872 6573 686f 6c64 5f72  core_threshold_r
+00017a00: 616e 6765 3d73 636f 7265 5f74 6872 6573  ange=score_thres
+00017a10: 686f 6c64 5f72 616e 6765 290a 0a20 2020  hold_range)..   
+00017a20: 2020 2020 2069 6620 7265 7475 726e 5f70       if return_p
+00017a30: 6c6f 746c 793a 0a20 2020 2020 2020 2020  lotly:.         
+00017a40: 2020 2063 7573 746f 6d5f 636f 6c6f 7273     custom_colors
+00017a50: 203d 205b 0a20 2020 2020 2020 2020 2020   = [.           
+00017a60: 2020 2020 2068 636f 6c6f 722e 436f 6c6f       hcolor.Colo
+00017a70: 7273 2e50 4153 5445 4c5f 424c 5545 2e76  rs.PASTEL_BLUE.v
+00017a80: 616c 7565 2c0a 2020 2020 2020 2020 2020  alue,.          
+00017a90: 2020 2020 2020 6863 6f6c 6f72 2e43 6f6c        hcolor.Col
+00017aa0: 6f72 732e 4355 5354 4f4d 5f47 5245 454e  ors.CUSTOM_GREEN
+00017ab0: 2e76 616c 7565 2c0a 2020 2020 2020 2020  .value,.        
+00017ac0: 2020 2020 2020 2020 6863 6f6c 6f72 2e43          hcolor.C
+00017ad0: 6f6c 6f72 732e 5945 4c4c 4f57 5f50 4550  olors.YELLOW_PEP
+00017ae0: 5045 522e 7661 6c75 652c 0a20 2020 2020  PER.value,.     
+00017af0: 2020 2020 2020 2020 2020 2068 636f 6c6f             hcolo
+00017b00: 722e 436f 6c6f 7273 2e43 5241 494c 2e76  r.Colors.CRAIL.v
+00017b10: 616c 7565 2c0a 2020 2020 2020 2020 2020  alue,.          
+00017b20: 2020 2020 2020 6863 6f6c 6f72 2e43 6f6c        hcolor.Col
+00017b30: 6f72 732e 4341 444d 4955 4d5f 4f52 414e  ors.CADMIUM_ORAN
+00017b40: 4745 2e76 616c 7565 2c0a 2020 2020 2020  GE.value,.      
+00017b50: 2020 2020 2020 5d0a 2020 2020 2020 2020        ].        
+00017b60: 2020 2020 6669 6720 3d20 7078 2e6c 696e      fig = px.lin
+00017b70: 6528 0a20 2020 2020 2020 2020 2020 2020  e(.             
+00017b80: 2020 2064 6174 615f 6672 616d 653d 7064     data_frame=pd
+00017b90: 2e6d 656c 7428 6672 616d 653d 7468 7265  .melt(frame=thre
+00017ba0: 7368 6f6c 645f 6375 7276 6573 2c20 6964  shold_curves, id
+00017bb0: 5f76 6172 733d 5b27 5363 6f72 6520 5468  _vars=['Score Th
+00017bc0: 7265 7368 6f6c 6427 5d29 2c0a 2020 2020  reshold']),.    
+00017bd0: 2020 2020 2020 2020 2020 2020 783d 2753              x='S
+00017be0: 636f 7265 2054 6872 6573 686f 6c64 272c  core Threshold',
+00017bf0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00017c00: 2079 3d27 7661 6c75 6527 2c0a 2020 2020   y='value',.    
+00017c10: 2020 2020 2020 2020 2020 2020 636f 6c6f              colo
+00017c20: 723d 2776 6172 6961 626c 6527 2c0a 2020  r='variable',.  
+00017c30: 2020 2020 2020 2020 2020 2020 2020 636f                co
+00017c40: 6c6f 725f 6469 7363 7265 7465 5f73 6571  lor_discrete_seq
+00017c50: 7565 6e63 653d 6375 7374 6f6d 5f63 6f6c  uence=custom_col
+00017c60: 6f72 732c 0a20 2020 2020 2020 2020 2020  ors,.           
+00017c70: 2020 2020 206c 6162 656c 733d 7b0a 2020       labels={.  
+00017c80: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00017c90: 2020 2776 6172 6961 626c 6527 3a20 2752    'variable': 'R
+00017ca0: 6174 6520 5479 7065 272c 0a20 2020 2020  ate Type',.     
+00017cb0: 2020 2020 2020 2020 2020 2020 2020 2027                 '
+00017cc0: 7661 6c75 6527 3a20 2752 6174 6527 0a20  value': 'Rate'. 
+00017cd0: 2020 2020 2020 2020 2020 2020 2020 207d                 }
+00017ce0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00017cf0: 2020 6865 6967 6874 3d35 3530 2c0a 2020    height=550,.  
+00017d00: 2020 2020 2020 2020 2020 2020 2020 7769                wi
+00017d10: 6474 683d 3535 3020 2a20 474f 4c44 454e  dth=550 * GOLDEN
+00017d20: 5f52 4154 494f 2c0a 2020 2020 2020 2020  _RATIO,.        
+00017d30: 2020 2020 2020 2020 7469 746c 653d 2254          title="T
+00017d40: 7261 6465 6f66 6673 2041 6372 6f73 7320  radeoffs Across 
+00017d50: 5661 7269 6f75 7320 5363 6f72 6520 5468  Various Score Th
+00017d60: 7265 7368 6f6c 6473 3c62 723e 3c73 7562  resholds<br><sub
+00017d70: 3e42 6c61 636b 206c 696e 6520 6973 2064  >Black line is d
+00017d80: 6566 6175 6c74 2074 6872 6573 686f 6c64  efault threshold
+00017d90: 206f 6620 302e 352e 3c2f 7375 623e 2220   of 0.5.</sub>" 
+00017da0: 2023 2070 796c 696e 743a 2064 6973 6162   # pylint: disab
+00017db0: 6c65 3d6c 696e 652d 746f 6f2d 6c6f 6e67  le=line-too-long
+00017dc0: 2020 2320 6e6f 7161 0a20 2020 2020 2020    # noqa.       
+00017dd0: 2020 2020 2029 0a20 2020 2020 2020 2020       ).         
+00017de0: 2020 2066 6967 203d 2066 6967 2e61 6464     fig = fig.add
+00017df0: 5f76 6c69 6e65 2878 3d30 2e35 2c20 6c69  _vline(x=0.5, li
+00017e00: 6e65 5f63 6f6c 6f72 3d68 636f 6c6f 722e  ne_color=hcolor.
+00017e10: 436f 6c6f 7273 2e42 4c41 434b 5f53 4841  Colors.BLACK_SHA
+00017e20: 444f 572e 7661 6c75 6529 0a20 2020 2020  DOW.value).     
+00017e30: 2020 2020 2020 2072 6574 7572 6e20 6669         return fi
+00017e40: 670a 0a20 2020 2020 2020 2061 7869 7320  g..        axis 
+00017e50: 3d20 736e 732e 6c69 6e65 706c 6f74 2878  = sns.lineplot(x
+00017e60: 3d27 5363 6f72 6520 5468 7265 7368 6f6c  ='Score Threshol
+00017e70: 6427 2c20 793d 2776 616c 7565 272c 2068  d', y='value', h
+00017e80: 7565 3d27 7661 7269 6162 6c65 272c 0a20  ue='variable',. 
+00017e90: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00017ea0: 2020 2020 2020 2020 2020 2064 6174 613d             data=
+00017eb0: 7064 2e6d 656c 7428 6672 616d 653d 7468  pd.melt(frame=th
+00017ec0: 7265 7368 6f6c 645f 6375 7276 6573 2c20  reshold_curves, 
+00017ed0: 6964 5f76 6172 733d 5b27 5363 6f72 6520  id_vars=['Score 
+00017ee0: 5468 7265 7368 6f6c 6427 5d29 290a 2020  Threshold'])).  
+00017ef0: 2020 2020 2020 6178 6973 2e73 6574 5f78        axis.set_x
+00017f00: 7469 636b 7328 6e70 2e61 7261 6e67 6528  ticks(np.arange(
+00017f10: 7363 6f72 655f 7468 7265 7368 6f6c 645f  score_threshold_
+00017f20: 7261 6e67 655b 305d 2c20 7363 6f72 655f  range[0], score_
+00017f30: 7468 7265 7368 6f6c 645f 7261 6e67 655b  threshold_range[
+00017f40: 315d 202b 2030 2e31 2c20 302e 3129 290a  1] + 0.1, 0.1)).
+00017f50: 2020 2020 2020 2020 6178 6973 2e73 6574          axis.set
+00017f60: 5f79 7469 636b 7328 6e70 2e61 7261 6e67  _yticks(np.arang
+00017f70: 6528 302c 2031 2e31 2c20 2e31 2929 0a20  e(0, 1.1, .1)). 
+00017f80: 2020 2020 2020 2070 6c74 2e76 6c69 6e65         plt.vline
+00017f90: 7328 783d 7365 6c66 2e73 636f 7265 5f74  s(x=self.score_t
+00017fa0: 6872 6573 686f 6c64 2c20 796d 696e 3d30  hreshold, ymin=0
+00017fb0: 2c20 796d 6178 3d31 2c20 636f 6c6f 7273  , ymax=1, colors
+00017fc0: 3d27 626c 6163 6b27 290a 2020 2020 2020  ='black').      
+00017fd0: 2020 706c 742e 6772 6964 2829 0a20 2020    plt.grid().   
+00017fe0: 2020 2020 2070 6c74 2e74 6967 6874 5f6c       plt.tight_l
+00017ff0: 6179 6f75 7428 290a 0a20 2020 2023 2070  ayout()..    # p
+00018000: 796c 696e 743a 2064 6973 6162 6c65 3d69  ylint: disable=i
+00018010: 6e63 6f6e 7369 7374 656e 742d 7265 7475  nconsistent-retu
+00018020: 726e 2d73 7461 7465 6d65 6e74 730a 2020  rn-statements.  
+00018030: 2020 6465 6620 706c 6f74 5f70 7265 6369    def plot_preci
+00018040: 7369 6f6e 5f72 6563 616c 6c5f 7472 6164  sion_recall_trad
+00018050: 656f 6666 2873 656c 662c 0a20 2020 2020  eoff(self,.     
+00018060: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00018070: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018080: 2020 2020 2020 2020 7363 6f72 655f 7468          score_th
-00018090: 7265 7368 6f6c 645f 7261 6e67 653a 2054  reshold_range: T
-000180a0: 7570 6c65 5b66 6c6f 6174 2c20 666c 6f61  uple[float, floa
-000180b0: 745d 203d 2028 302e 312c 2030 2e39 292c  t] = (0.1, 0.9),
-000180c0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00018080: 2020 7363 6f72 655f 7468 7265 7368 6f6c    score_threshol
+00018090: 645f 7261 6e67 653a 2054 7570 6c65 5b66  d_range: Tuple[f
+000180a0: 6c6f 6174 2c20 666c 6f61 745d 203d 2028  loat, float] = (
+000180b0: 302e 312c 2030 2e39 292c 0a20 2020 2020  0.1, 0.9),.     
+000180c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000180d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000180e0: 2020 2020 2020 2020 6669 6775 7265 5f73          figure_s
-000180f0: 697a 653a 2074 7570 6c65 203d 2053 5441  ize: tuple = STA
-00018100: 4e44 4152 445f 5749 4454 485f 4845 4947  NDARD_WIDTH_HEIG
-00018110: 4854 2c0a 2020 2020 2020 2020 2020 2020  HT,.            
+000180e0: 2020 6669 6775 7265 5f73 697a 653a 2074    figure_size: t
+000180f0: 7570 6c65 203d 2053 5441 4e44 4152 445f  uple = STANDARD_
+00018100: 5749 4454 485f 4845 4947 4854 2c0a 2020  WIDTH_HEIGHT,.  
+00018110: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00018120: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018130: 2020 2020 2020 2020 2020 2072 6574 7572             retur
-00018140: 6e5f 706c 6f74 6c79 3a20 626f 6f6c 203d  n_plotly: bool =
-00018150: 2046 616c 7365 2920 2d3e 2055 6e69 6f6e   False) -> Union
-00018160: 5b4e 6f6e 652c 0a20 2020 2020 2020 2020  [None,.         
+00018130: 2020 2020 2072 6574 7572 6e5f 706c 6f74       return_plot
+00018140: 6c79 3a20 626f 6f6c 203d 2046 616c 7365  ly: bool = False
+00018150: 2920 2d3e 2055 6e69 6f6e 5b4e 6f6e 652c  ) -> Union[None,
+00018160: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
 00018170: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00018180: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00018190: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000181a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000181b0: 2020 2020 5f66 6967 7572 652e 4669 6775      _figure.Figu
-000181c0: 7265 5d3a 0a20 2020 2020 2020 2022 2222  re]:.        """
-000181d0: 506c 6f74 7320 7468 6520 7472 6164 656f  Plots the tradeo
-000181e0: 6666 2062 6574 7765 656e 2070 7265 6369  ff between preci
-000181f0: 7369 6f6e 2028 692e 652e 2070 6f73 6974  sion (i.e. posit
-00018200: 6976 6520 7072 6564 6963 7420 7661 6c75  ive predict valu
-00018210: 6529 2061 6e64 2072 6563 616c 6c20 2869  e) and recall (i
-00018220: 2e65 2e20 5472 7565 2050 6f73 6974 6976  .e. True Positiv
-00018230: 650a 2020 2020 2020 2020 5261 7465 2920  e.        Rate) 
-00018240: 666f 7220 7661 7269 6f75 7320 7363 6f72  for various scor
-00018250: 6520 7468 7265 7368 6f6c 6473 2e20 2841  e thresholds. (A
-00018260: 2073 636f 7265 2074 6872 6573 686f 6c64   score threshold
-00018270: 2069 7320 7468 6520 7661 6c75 6520 666f   is the value fo
-00018280: 7220 7768 6963 6820 796f 7520 776f 756c  r which you woul
-00018290: 6420 7072 6564 6963 7420 610a 2020 2020  d predict a.    
-000182a0: 2020 2020 706f 7369 7469 7665 206c 6162      positive lab
-000182b0: 656c 2069 6620 7468 6520 7661 6c75 6520  el if the value 
-000182c0: 6f66 2074 6865 2073 636f 7265 2069 7320  of the score is 
-000182d0: 6162 6f76 6520 7468 6520 7468 7265 7368  above the thresh
-000182e0: 6f6c 6420 2865 2e67 2e20 7573 7561 6c6c  old (e.g. usuall
-000182f0: 7920 302e 3529 2e0a 0a20 2020 2020 2020  y 0.5)...       
-00018300: 2041 7267 733a 0a20 2020 2020 2020 2020   Args:.         
-00018310: 2020 2073 636f 7265 5f74 6872 6573 686f     score_thresho
-00018320: 6c64 5f72 616e 6765 3a0a 2020 2020 2020  ld_range:.      
-00018330: 2020 2020 2020 2020 2020 7261 6e67 6520            range 
-00018340: 6f66 2073 636f 7265 2074 6872 6573 686f  of score thresho
-00018350: 6c64 7320 746f 2070 6c6f 7420 2878 2d61  lds to plot (x-a
-00018360: 7869 7329 3b20 7475 706c 6520 7769 7468  xis); tuple with
-00018370: 206d 696e 696d 756d 2074 6872 6573 686f   minimum thresho
-00018380: 6c64 2069 6e20 6669 7273 7420 696e 6465  ld in first inde
-00018390: 7820 616e 640a 2020 2020 2020 2020 2020  x and.          
-000183a0: 2020 2020 2020 6d61 7869 6d75 6d20 7468        maximum th
-000183b0: 7265 7368 6f6c 6420 696e 2073 6563 6f6e  reshold in secon
-000183c0: 6420 696e 6465 782e 0a20 2020 2020 2020  d index..       
-000183d0: 2020 2020 2066 6967 7572 655f 7369 7a65       figure_size
-000183e0: 3a0a 2020 2020 2020 2020 2020 2020 2020  :.              
-000183f0: 2020 7475 706c 6520 636f 6e74 6169 6e69    tuple containi
-00018400: 6e67 2060 2877 6964 7468 2c20 6865 6967  ng `(width, heig
-00018410: 6874 2960 206f 6620 706c 6f74 2e20 5468  ht)` of plot. Th
-00018420: 6520 6465 6661 756c 7420 6865 6967 6874  e default height
-00018430: 2069 7320 6465 6669 6e65 6420 6279 0a20   is defined by. 
-00018440: 2020 2020 2020 2020 2020 2020 2020 2060                 `
-00018450: 6865 6c70 736b 2e70 6c6f 742e 5354 414e  helpsk.plot.STAN
-00018460: 4441 5244 5f48 4549 4748 5460 2c20 616e  DARD_HEIGHT`, an
-00018470: 6420 7468 6520 6465 6661 756c 7420 7769  d the default wi
-00018480: 6474 6820 6973 0a20 2020 2020 2020 2020  dth is.         
-00018490: 2020 2020 2020 2060 6865 6c70 736b 2e70         `helpsk.p
-000184a0: 6c6f 742e 5354 414e 4441 5244 5f48 4549  lot.STANDARD_HEI
-000184b0: 4748 5420 2f20 6865 6c70 736b 2e70 6c6f  GHT / helpsk.plo
-000184c0: 742e 474f 4c44 454e 5f52 4154 494f 600a  t.GOLDEN_RATIO`.
-000184d0: 2020 2020 2020 2020 2020 2020 7265 7475              retu
-000184e0: 726e 5f70 6c6f 746c 793a 0a20 2020 2020  rn_plotly:.     
-000184f0: 2020 2020 2020 2020 2020 2049 6620 5472             If Tr
-00018500: 7565 2c20 7265 7475 726e 2070 6c6f 746c  ue, return plotl
-00018510: 7920 6f62 6a65 6374 2e20 4f74 6865 7277  y object. Otherw
-00018520: 6973 652c 2075 7365 206d 6174 706c 6f74  ise, use matplot
-00018530: 6c69 6220 616e 6420 656e 6420 6675 6e63  lib and end func
-00018540: 7469 6f6e 2077 6974 6820 6361 6c6c 3a0a  tion with call:.
-00018550: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018560: 6070 6c74 2e74 6967 6874 5f6c 6179 6f75  `plt.tight_layou
-00018570: 7428 2960 0a20 2020 2020 2020 2022 2222  t()`.        """
-00018580: 0a20 2020 2020 2020 2070 6c74 2e66 6967  .        plt.fig
-00018590: 7572 6528 6669 6773 697a 653d 6669 6775  ure(figsize=figu
-000185a0: 7265 5f73 697a 6529 0a0a 2020 2020 2020  re_size)..      
-000185b0: 2020 7468 7265 7368 6f6c 645f 6375 7276    threshold_curv
-000185c0: 6573 203d 2073 656c 662e 5f67 6574 5f74  es = self._get_t
-000185d0: 6872 6573 686f 6c64 5f63 7572 7665 5f64  hreshold_curve_d
-000185e0: 6174 6166 7261 6d65 2873 636f 7265 5f74  ataframe(score_t
-000185f0: 6872 6573 686f 6c64 5f72 616e 6765 3d73  hreshold_range=s
-00018600: 636f 7265 5f74 6872 6573 686f 6c64 5f72  core_threshold_r
-00018610: 616e 6765 290a 2020 2020 2020 2020 7468  ange).        th
-00018620: 7265 7368 6f6c 645f 6375 7276 6573 203d  reshold_curves =
-00018630: 2074 6872 6573 686f 6c64 5f63 7572 7665   threshold_curve
-00018640: 735b 5b27 5363 6f72 6520 5468 7265 7368  s[['Score Thresh
-00018650: 6f6c 6427 2c0a 2020 2020 2020 2020 2020  old',.          
+000181a0: 2020 2020 2020 2020 2020 2020 2020 5f66                _f
+000181b0: 6967 7572 652e 4669 6775 7265 5d3a 0a20  igure.Figure]:. 
+000181c0: 2020 2020 2020 2022 2222 506c 6f74 7320         """Plots 
+000181d0: 7468 6520 7472 6164 656f 6666 2062 6574  the tradeoff bet
+000181e0: 7765 656e 2070 7265 6369 7369 6f6e 2028  ween precision (
+000181f0: 692e 652e 2070 6f73 6974 6976 6520 7072  i.e. positive pr
+00018200: 6564 6963 7420 7661 6c75 6529 2061 6e64  edict value) and
+00018210: 2072 6563 616c 6c20 2869 2e65 2e20 5472   recall (i.e. Tr
+00018220: 7565 2050 6f73 6974 6976 650a 2020 2020  ue Positive.    
+00018230: 2020 2020 5261 7465 2920 666f 7220 7661      Rate) for va
+00018240: 7269 6f75 7320 7363 6f72 6520 7468 7265  rious score thre
+00018250: 7368 6f6c 6473 2e20 2841 2073 636f 7265  sholds. (A score
+00018260: 2074 6872 6573 686f 6c64 2069 7320 7468   threshold is th
+00018270: 6520 7661 6c75 6520 666f 7220 7768 6963  e value for whic
+00018280: 6820 796f 7520 776f 756c 6420 7072 6564  h you would pred
+00018290: 6963 7420 610a 2020 2020 2020 2020 706f  ict a.        po
+000182a0: 7369 7469 7665 206c 6162 656c 2069 6620  sitive label if 
+000182b0: 7468 6520 7661 6c75 6520 6f66 2074 6865  the value of the
+000182c0: 2073 636f 7265 2069 7320 6162 6f76 6520   score is above 
+000182d0: 7468 6520 7468 7265 7368 6f6c 6420 2865  the threshold (e
+000182e0: 2e67 2e20 7573 7561 6c6c 7920 302e 3529  .g. usually 0.5)
+000182f0: 2e0a 0a20 2020 2020 2020 2041 7267 733a  ...        Args:
+00018300: 0a20 2020 2020 2020 2020 2020 2073 636f  .            sco
+00018310: 7265 5f74 6872 6573 686f 6c64 5f72 616e  re_threshold_ran
+00018320: 6765 3a0a 2020 2020 2020 2020 2020 2020  ge:.            
+00018330: 2020 2020 7261 6e67 6520 6f66 2073 636f      range of sco
+00018340: 7265 2074 6872 6573 686f 6c64 7320 746f  re thresholds to
+00018350: 2070 6c6f 7420 2878 2d61 7869 7329 3b20   plot (x-axis); 
+00018360: 7475 706c 6520 7769 7468 206d 696e 696d  tuple with minim
+00018370: 756d 2074 6872 6573 686f 6c64 2069 6e20  um threshold in 
+00018380: 6669 7273 7420 696e 6465 7820 616e 640a  first index and.
+00018390: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000183a0: 6d61 7869 6d75 6d20 7468 7265 7368 6f6c  maximum threshol
+000183b0: 6420 696e 2073 6563 6f6e 6420 696e 6465  d in second inde
+000183c0: 782e 0a20 2020 2020 2020 2020 2020 2066  x..            f
+000183d0: 6967 7572 655f 7369 7a65 3a0a 2020 2020  igure_size:.    
+000183e0: 2020 2020 2020 2020 2020 2020 7475 706c              tupl
+000183f0: 6520 636f 6e74 6169 6e69 6e67 2060 2877  e containing `(w
+00018400: 6964 7468 2c20 6865 6967 6874 2960 206f  idth, height)` o
+00018410: 6620 706c 6f74 2e20 5468 6520 6465 6661  f plot. The defa
+00018420: 756c 7420 6865 6967 6874 2069 7320 6465  ult height is de
+00018430: 6669 6e65 6420 6279 0a20 2020 2020 2020  fined by.       
+00018440: 2020 2020 2020 2020 2060 6865 6c70 736b           `helpsk
+00018450: 2e70 6c6f 742e 5354 414e 4441 5244 5f48  .plot.STANDARD_H
+00018460: 4549 4748 5460 2c20 616e 6420 7468 6520  EIGHT`, and the 
+00018470: 6465 6661 756c 7420 7769 6474 6820 6973  default width is
+00018480: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00018490: 2060 6865 6c70 736b 2e70 6c6f 742e 5354   `helpsk.plot.ST
+000184a0: 414e 4441 5244 5f48 4549 4748 5420 2f20  ANDARD_HEIGHT / 
+000184b0: 6865 6c70 736b 2e70 6c6f 742e 474f 4c44  helpsk.plot.GOLD
+000184c0: 454e 5f52 4154 494f 600a 2020 2020 2020  EN_RATIO`.      
+000184d0: 2020 2020 2020 7265 7475 726e 5f70 6c6f        return_plo
+000184e0: 746c 793a 0a20 2020 2020 2020 2020 2020  tly:.           
+000184f0: 2020 2020 2049 6620 5472 7565 2c20 7265       If True, re
+00018500: 7475 726e 2070 6c6f 746c 7920 6f62 6a65  turn plotly obje
+00018510: 6374 2e20 4f74 6865 7277 6973 652c 2075  ct. Otherwise, u
+00018520: 7365 206d 6174 706c 6f74 6c69 6220 616e  se matplotlib an
+00018530: 6420 656e 6420 6675 6e63 7469 6f6e 2077  d end function w
+00018540: 6974 6820 6361 6c6c 3a0a 2020 2020 2020  ith call:.      
+00018550: 2020 2020 2020 2020 2020 6070 6c74 2e74            `plt.t
+00018560: 6967 6874 5f6c 6179 6f75 7428 2960 0a20  ight_layout()`. 
+00018570: 2020 2020 2020 2022 2222 0a20 2020 2020         """.     
+00018580: 2020 2070 6c74 2e66 6967 7572 6528 6669     plt.figure(fi
+00018590: 6773 697a 653d 6669 6775 7265 5f73 697a  gsize=figure_siz
+000185a0: 6529 0a0a 2020 2020 2020 2020 7468 7265  e)..        thre
+000185b0: 7368 6f6c 645f 6375 7276 6573 203d 2073  shold_curves = s
+000185c0: 656c 662e 5f67 6574 5f74 6872 6573 686f  elf._get_thresho
+000185d0: 6c64 5f63 7572 7665 5f64 6174 6166 7261  ld_curve_datafra
+000185e0: 6d65 2873 636f 7265 5f74 6872 6573 686f  me(score_thresho
+000185f0: 6c64 5f72 616e 6765 3d73 636f 7265 5f74  ld_range=score_t
+00018600: 6872 6573 686f 6c64 5f72 616e 6765 290a  hreshold_range).
+00018610: 2020 2020 2020 2020 7468 7265 7368 6f6c          threshol
+00018620: 645f 6375 7276 6573 203d 2074 6872 6573  d_curves = thres
+00018630: 686f 6c64 5f63 7572 7665 735b 5b27 5363  hold_curves[['Sc
+00018640: 6f72 6520 5468 7265 7368 6f6c 6427 2c0a  ore Threshold',.
+00018650: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00018660: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00018670: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018680: 2020 2020 2020 2027 5472 7565 2050 6f73         'True Pos
-00018690: 2e20 5261 7465 2028 5265 6361 6c6c 2927  . Rate (Recall)'
-000186a0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00018680: 2027 5472 7565 2050 6f73 2e20 5261 7465   'True Pos. Rate
+00018690: 2028 5265 6361 6c6c 2927 2c0a 2020 2020   (Recall)',.    
+000186a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000186b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000186c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000186d0: 2020 2027 506f 732e 2050 7265 6469 6374     'Pos. Predict
-000186e0: 6976 6520 5661 6c75 6520 2850 7265 6369  ive Value (Preci
-000186f0: 7369 6f6e 2927 5d5d 0a0a 2020 2020 2020  sion)']]..      
-00018700: 2020 6966 2072 6574 7572 6e5f 706c 6f74    if return_plot
-00018710: 6c79 3a0a 2020 2020 2020 2020 2020 2020  ly:.            
-00018720: 6375 7374 6f6d 5f63 6f6c 6f72 7320 3d20  custom_colors = 
-00018730: 5b0a 2020 2020 2020 2020 2020 2020 2020  [.              
-00018740: 2020 6863 6f6c 6f72 2e43 6f6c 6f72 732e    hcolor.Colors.
-00018750: 5041 5354 454c 5f42 4c55 452e 7661 6c75  PASTEL_BLUE.valu
-00018760: 652c 0a20 2020 2020 2020 2020 2020 2020  e,.             
-00018770: 2020 2023 2020 2020 2068 636f 6c6f 722e     #     hcolor.
-00018780: 436f 6c6f 7273 2e43 5553 544f 4d5f 4752  Colors.CUSTOM_GR
-00018790: 4545 4e2e 7661 6c75 652c 0a20 2020 2020  EEN.value,.     
-000187a0: 2020 2020 2020 2020 2020 2068 636f 6c6f             hcolo
-000187b0: 722e 436f 6c6f 7273 2e59 454c 4c4f 575f  r.Colors.YELLOW_
-000187c0: 5045 5050 4552 2e76 616c 7565 2c0a 2020  PEPPER.value,.  
-000187d0: 2020 2020 2020 2020 2020 2020 2020 2320                # 
-000187e0: 2020 2020 6863 6f6c 6f72 2e43 6f6c 6f72      hcolor.Color
-000187f0: 732e 4352 4149 4c2e 7661 6c75 652c 0a20  s.CRAIL.value,. 
-00018800: 2020 2020 2020 2020 2020 2020 2020 2023                 #
-00018810: 2020 2020 2068 636f 6c6f 722e 436f 6c6f       hcolor.Colo
-00018820: 7273 2e43 4144 4d49 554d 5f4f 5241 4e47  rs.CADMIUM_ORANG
-00018830: 452e 7661 6c75 652c 0a20 2020 2020 2020  E.value,.       
-00018840: 2020 2020 205d 0a0a 2020 2020 2020 2020       ]..        
-00018850: 2020 2020 6669 6720 3d20 7078 2e6c 696e      fig = px.lin
-00018860: 6528 0a20 2020 2020 2020 2020 2020 2020  e(.             
-00018870: 2020 2064 6174 615f 6672 616d 653d 7064     data_frame=pd
-00018880: 2e6d 656c 7428 6672 616d 653d 7468 7265  .melt(frame=thre
-00018890: 7368 6f6c 645f 6375 7276 6573 5b5b 2753  shold_curves[['S
-000188a0: 636f 7265 2054 6872 6573 686f 6c64 272c  core Threshold',
-000188b0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+000186c0: 2020 2020 2020 2020 2020 2020 2027 506f               'Po
+000186d0: 732e 2050 7265 6469 6374 6976 6520 5661  s. Predictive Va
+000186e0: 6c75 6520 2850 7265 6369 7369 6f6e 2927  lue (Precision)'
+000186f0: 5d5d 0a0a 2020 2020 2020 2020 6966 2072  ]]..        if r
+00018700: 6574 7572 6e5f 706c 6f74 6c79 3a0a 2020  eturn_plotly:.  
+00018710: 2020 2020 2020 2020 2020 6375 7374 6f6d            custom
+00018720: 5f63 6f6c 6f72 7320 3d20 5b0a 2020 2020  _colors = [.    
+00018730: 2020 2020 2020 2020 2020 2020 6863 6f6c              hcol
+00018740: 6f72 2e43 6f6c 6f72 732e 5041 5354 454c  or.Colors.PASTEL
+00018750: 5f42 4c55 452e 7661 6c75 652c 0a20 2020  _BLUE.value,.   
+00018760: 2020 2020 2020 2020 2020 2020 2023 2020               #  
+00018770: 2020 2068 636f 6c6f 722e 436f 6c6f 7273     hcolor.Colors
+00018780: 2e43 5553 544f 4d5f 4752 4545 4e2e 7661  .CUSTOM_GREEN.va
+00018790: 6c75 652c 0a20 2020 2020 2020 2020 2020  lue,.           
+000187a0: 2020 2020 2068 636f 6c6f 722e 436f 6c6f       hcolor.Colo
+000187b0: 7273 2e59 454c 4c4f 575f 5045 5050 4552  rs.YELLOW_PEPPER
+000187c0: 2e76 616c 7565 2c0a 2020 2020 2020 2020  .value,.        
+000187d0: 2020 2020 2020 2020 2320 2020 2020 6863          #     hc
+000187e0: 6f6c 6f72 2e43 6f6c 6f72 732e 4352 4149  olor.Colors.CRAI
+000187f0: 4c2e 7661 6c75 652c 0a20 2020 2020 2020  L.value,.       
+00018800: 2020 2020 2020 2020 2023 2020 2020 2068           #     h
+00018810: 636f 6c6f 722e 436f 6c6f 7273 2e43 4144  color.Colors.CAD
+00018820: 4d49 554d 5f4f 5241 4e47 452e 7661 6c75  MIUM_ORANGE.valu
+00018830: 652c 0a20 2020 2020 2020 2020 2020 205d  e,.            ]
+00018840: 0a0a 2020 2020 2020 2020 2020 2020 6669  ..            fi
+00018850: 6720 3d20 7078 2e6c 696e 6528 0a20 2020  g = px.line(.   
+00018860: 2020 2020 2020 2020 2020 2020 2064 6174               dat
+00018870: 615f 6672 616d 653d 7064 2e6d 656c 7428  a_frame=pd.melt(
+00018880: 6672 616d 653d 7468 7265 7368 6f6c 645f  frame=threshold_
+00018890: 6375 7276 6573 5b5b 2753 636f 7265 2054  curves[['Score T
+000188a0: 6872 6573 686f 6c64 272c 0a20 2020 2020  hreshold',.     
+000188b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000188c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 000188d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000188e0: 2020 2020 2020 2020 2020 2020 2754 7275              'Tru
-000188f0: 6520 506f 732e 2052 6174 6520 2852 6563  e Pos. Rate (Rec
-00018900: 616c 6c29 272c 0a20 2020 2020 2020 2020  all)',.         
+000188e0: 2020 2020 2020 2754 7275 6520 506f 732e        'True Pos.
+000188f0: 2052 6174 6520 2852 6563 616c 6c29 272c   Rate (Recall)',
+00018900: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
 00018910: 2020 2020 2020 2020 2020 2020 2020 2020                  
 00018920: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018930: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018940: 2020 2750 6f73 2e20 5072 6564 6963 7469    'Pos. Predicti
-00018950: 7665 2056 616c 7565 2028 5072 6563 6973  ve Value (Precis
-00018960: 696f 6e29 275d 5d2c 0a20 2020 2020 2020  ion)']],.       
+00018930: 2020 2020 2020 2020 2020 2020 2750 6f73              'Pos
+00018940: 2e20 5072 6564 6963 7469 7665 2056 616c  . Predictive Val
+00018950: 7565 2028 5072 6563 6973 696f 6e29 275d  ue (Precision)']
+00018960: 5d2c 0a20 2020 2020 2020 2020 2020 2020  ],.             
 00018970: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018980: 2020 2020 2020 2020 2020 2020 6964 5f76              id_v
-00018990: 6172 733d 5b27 5363 6f72 6520 5468 7265  ars=['Score Thre
-000189a0: 7368 6f6c 6427 5d29 2c0a 2020 2020 2020  shold']),.      
-000189b0: 2020 2020 2020 2020 2020 783d 2753 636f            x='Sco
-000189c0: 7265 2054 6872 6573 686f 6c64 272c 0a20  re Threshold',. 
-000189d0: 2020 2020 2020 2020 2020 2020 2020 2079                 y
-000189e0: 3d27 7661 6c75 6527 2c0a 2020 2020 2020  ='value',.      
-000189f0: 2020 2020 2020 2020 2020 636f 6c6f 723d            color=
-00018a00: 2776 6172 6961 626c 6527 2c0a 2020 2020  'variable',.    
-00018a10: 2020 2020 2020 2020 2020 2020 636f 6c6f              colo
-00018a20: 725f 6469 7363 7265 7465 5f73 6571 7565  r_discrete_seque
-00018a30: 6e63 653d 6375 7374 6f6d 5f63 6f6c 6f72  nce=custom_color
-00018a40: 732c 0a20 2020 2020 2020 2020 2020 2020  s,.             
-00018a50: 2020 206c 6162 656c 733d 7b0a 2020 2020     labels={.    
-00018a60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018a70: 2776 6172 6961 626c 6527 3a20 2752 6174  'variable': 'Rat
-00018a80: 6527 2c0a 2020 2020 2020 2020 2020 2020  e',.            
-00018a90: 2020 2020 2020 2020 2776 616c 7565 273a          'value':
-00018aa0: 2027 5661 6c75 6527 0a20 2020 2020 2020   'Value'.       
-00018ab0: 2020 2020 2020 2020 207d 2c0a 2020 2020           },.    
-00018ac0: 2020 2020 2020 2020 2020 2020 6865 6967              heig
-00018ad0: 6874 3d35 3530 2c0a 2020 2020 2020 2020  ht=550,.        
-00018ae0: 2020 2020 2020 2020 7769 6474 683d 3535          width=55
-00018af0: 3020 2a20 474f 4c44 454e 5f52 4154 494f  0 * GOLDEN_RATIO
-00018b00: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00018b10: 2020 7469 746c 653d 2250 7265 6369 7369    title="Precisi
-00018b20: 6f6e 2052 6563 616c 6c20 5472 6164 656f  on Recall Tradeo
-00018b30: 6666 3c62 723e 3c73 7562 3e42 6c61 636b  ff<br><sub>Black
-00018b40: 206c 696e 6520 6973 2064 6566 6175 6c74   line is default
-00018b50: 2074 6872 6573 686f 6c64 206f 6620 302e   threshold of 0.
-00018b60: 352e 3c2f 7375 623e 220a 2020 2020 2020  5.</sub>".      
-00018b70: 2020 2020 2020 290a 2020 2020 2020 2020        ).        
-00018b80: 2020 2020 6669 6720 3d20 6669 672e 6164      fig = fig.ad
-00018b90: 645f 766c 696e 6528 783d 302e 352c 206c  d_vline(x=0.5, l
-00018ba0: 696e 655f 636f 6c6f 723d 6863 6f6c 6f72  ine_color=hcolor
-00018bb0: 2e43 6f6c 6f72 732e 424c 4143 4b5f 5348  .Colors.BLACK_SH
-00018bc0: 4144 4f57 2e76 616c 7565 290a 2020 2020  ADOW.value).    
-00018bd0: 2020 2020 2020 2020 7265 7475 726e 2066          return f
-00018be0: 6967 0a20 2020 2020 2020 2061 7869 7320  ig.        axis 
-00018bf0: 3d20 736e 732e 6c69 6e65 706c 6f74 2878  = sns.lineplot(x
-00018c00: 3d27 5363 6f72 6520 5468 7265 7368 6f6c  ='Score Threshol
-00018c10: 6427 2c20 793d 2776 616c 7565 272c 2068  d', y='value', h
-00018c20: 7565 3d27 7661 7269 6162 6c65 272c 0a20  ue='variable',. 
+00018980: 2020 2020 2020 6964 5f76 6172 733d 5b27        id_vars=['
+00018990: 5363 6f72 6520 5468 7265 7368 6f6c 6427  Score Threshold'
+000189a0: 5d29 2c0a 2020 2020 2020 2020 2020 2020  ]),.            
+000189b0: 2020 2020 783d 2753 636f 7265 2054 6872      x='Score Thr
+000189c0: 6573 686f 6c64 272c 0a20 2020 2020 2020  eshold',.       
+000189d0: 2020 2020 2020 2020 2079 3d27 7661 6c75           y='valu
+000189e0: 6527 2c0a 2020 2020 2020 2020 2020 2020  e',.            
+000189f0: 2020 2020 636f 6c6f 723d 2776 6172 6961      color='varia
+00018a00: 626c 6527 2c0a 2020 2020 2020 2020 2020  ble',.          
+00018a10: 2020 2020 2020 636f 6c6f 725f 6469 7363        color_disc
+00018a20: 7265 7465 5f73 6571 7565 6e63 653d 6375  rete_sequence=cu
+00018a30: 7374 6f6d 5f63 6f6c 6f72 732c 0a20 2020  stom_colors,.   
+00018a40: 2020 2020 2020 2020 2020 2020 206c 6162               lab
+00018a50: 656c 733d 7b0a 2020 2020 2020 2020 2020  els={.          
+00018a60: 2020 2020 2020 2020 2020 2776 6172 6961            'varia
+00018a70: 626c 6527 3a20 2752 6174 6527 2c0a 2020  ble': 'Rate',.  
+00018a80: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00018a90: 2020 2776 616c 7565 273a 2027 5661 6c75    'value': 'Valu
+00018aa0: 6527 0a20 2020 2020 2020 2020 2020 2020  e'.             
+00018ab0: 2020 207d 2c0a 2020 2020 2020 2020 2020     },.          
+00018ac0: 2020 2020 2020 6865 6967 6874 3d35 3530        height=550
+00018ad0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+00018ae0: 2020 7769 6474 683d 3535 3020 2a20 474f    width=550 * GO
+00018af0: 4c44 454e 5f52 4154 494f 2c0a 2020 2020  LDEN_RATIO,.    
+00018b00: 2020 2020 2020 2020 2020 2020 7469 746c              titl
+00018b10: 653d 2250 7265 6369 7369 6f6e 2052 6563  e="Precision Rec
+00018b20: 616c 6c20 5472 6164 656f 6666 3c62 723e  all Tradeoff<br>
+00018b30: 3c73 7562 3e42 6c61 636b 206c 696e 6520  <sub>Black line 
+00018b40: 6973 2064 6566 6175 6c74 2074 6872 6573  is default thres
+00018b50: 686f 6c64 206f 6620 302e 352e 3c2f 7375  hold of 0.5.</su
+00018b60: 623e 220a 2020 2020 2020 2020 2020 2020  b>".            
+00018b70: 290a 2020 2020 2020 2020 2020 2020 6669  ).            fi
+00018b80: 6720 3d20 6669 672e 6164 645f 766c 696e  g = fig.add_vlin
+00018b90: 6528 783d 302e 352c 206c 696e 655f 636f  e(x=0.5, line_co
+00018ba0: 6c6f 723d 6863 6f6c 6f72 2e43 6f6c 6f72  lor=hcolor.Color
+00018bb0: 732e 424c 4143 4b5f 5348 4144 4f57 2e76  s.BLACK_SHADOW.v
+00018bc0: 616c 7565 290a 2020 2020 2020 2020 2020  alue).          
+00018bd0: 2020 7265 7475 726e 2066 6967 0a20 2020    return fig.   
+00018be0: 2020 2020 2061 7869 7320 3d20 736e 732e       axis = sns.
+00018bf0: 6c69 6e65 706c 6f74 2878 3d27 5363 6f72  lineplot(x='Scor
+00018c00: 6520 5468 7265 7368 6f6c 6427 2c20 793d  e Threshold', y=
+00018c10: 2776 616c 7565 272c 2068 7565 3d27 7661  'value', hue='va
+00018c20: 7269 6162 6c65 272c 0a20 2020 2020 2020  riable',.       
 00018c30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018c40: 2020 2020 2020 2020 2020 2064 6174 613d             data=
-00018c50: 7064 2e6d 656c 7428 6672 616d 653d 7468  pd.melt(frame=th
-00018c60: 7265 7368 6f6c 645f 6375 7276 6573 2c20  reshold_curves, 
-00018c70: 6964 5f76 6172 733d 5b27 5363 6f72 6520  id_vars=['Score 
-00018c80: 5468 7265 7368 6f6c 6427 5d29 290a 2020  Threshold'])).  
-00018c90: 2020 2020 2020 6178 6973 2e73 6574 5f78        axis.set_x
-00018ca0: 7469 636b 7328 6e70 2e61 7261 6e67 6528  ticks(np.arange(
-00018cb0: 7363 6f72 655f 7468 7265 7368 6f6c 645f  score_threshold_
-00018cc0: 7261 6e67 655b 305d 2c20 7363 6f72 655f  range[0], score_
-00018cd0: 7468 7265 7368 6f6c 645f 7261 6e67 655b  threshold_range[
-00018ce0: 315d 202b 2030 2e31 2c20 302e 3129 290a  1] + 0.1, 0.1)).
-00018cf0: 2020 2020 2020 2020 6178 6973 2e73 6574          axis.set
-00018d00: 5f79 7469 636b 7328 6e70 2e61 7261 6e67  _yticks(np.arang
-00018d10: 6528 302c 2031 2e31 2c20 2e31 2929 0a20  e(0, 1.1, .1)). 
-00018d20: 2020 2020 2020 2070 6c74 2e76 6c69 6e65         plt.vline
-00018d30: 7328 783d 7365 6c66 2e73 636f 7265 5f74  s(x=self.score_t
-00018d40: 6872 6573 686f 6c64 2c20 796d 696e 3d30  hreshold, ymin=0
-00018d50: 2c20 796d 6178 3d31 2c20 636f 6c6f 7273  , ymax=1, colors
-00018d60: 3d27 626c 6163 6b27 290a 2020 2020 2020  ='black').      
-00018d70: 2020 706c 742e 6772 6964 2829 0a20 2020    plt.grid().   
-00018d80: 2020 2020 2070 6c74 2e74 6967 6874 5f6c       plt.tight_l
-00018d90: 6179 6f75 7428 290a 0a20 2020 2023 2070  ayout()..    # p
-00018da0: 796c 696e 743a 2064 6973 6162 6c65 3d69  ylint: disable=i
-00018db0: 6e63 6f6e 7369 7374 656e 742d 7265 7475  nconsistent-retu
-00018dc0: 726e 2d73 7461 7465 6d65 6e74 730a 2020  rn-statements.  
-00018dd0: 2020 6465 6620 6361 6c63 756c 6174 655f    def calculate_
-00018de0: 6c69 6674 5f67 6169 6e28 7365 6c66 2c0a  lift_gain(self,.
+00018c40: 2020 2020 2064 6174 613d 7064 2e6d 656c       data=pd.mel
+00018c50: 7428 6672 616d 653d 7468 7265 7368 6f6c  t(frame=threshol
+00018c60: 645f 6375 7276 6573 2c20 6964 5f76 6172  d_curves, id_var
+00018c70: 733d 5b27 5363 6f72 6520 5468 7265 7368  s=['Score Thresh
+00018c80: 6f6c 6427 5d29 290a 2020 2020 2020 2020  old'])).        
+00018c90: 6178 6973 2e73 6574 5f78 7469 636b 7328  axis.set_xticks(
+00018ca0: 6e70 2e61 7261 6e67 6528 7363 6f72 655f  np.arange(score_
+00018cb0: 7468 7265 7368 6f6c 645f 7261 6e67 655b  threshold_range[
+00018cc0: 305d 2c20 7363 6f72 655f 7468 7265 7368  0], score_thresh
+00018cd0: 6f6c 645f 7261 6e67 655b 315d 202b 2030  old_range[1] + 0
+00018ce0: 2e31 2c20 302e 3129 290a 2020 2020 2020  .1, 0.1)).      
+00018cf0: 2020 6178 6973 2e73 6574 5f79 7469 636b    axis.set_ytick
+00018d00: 7328 6e70 2e61 7261 6e67 6528 302c 2031  s(np.arange(0, 1
+00018d10: 2e31 2c20 2e31 2929 0a20 2020 2020 2020  .1, .1)).       
+00018d20: 2070 6c74 2e76 6c69 6e65 7328 783d 7365   plt.vlines(x=se
+00018d30: 6c66 2e73 636f 7265 5f74 6872 6573 686f  lf.score_thresho
+00018d40: 6c64 2c20 796d 696e 3d30 2c20 796d 6178  ld, ymin=0, ymax
+00018d50: 3d31 2c20 636f 6c6f 7273 3d27 626c 6163  =1, colors='blac
+00018d60: 6b27 290a 2020 2020 2020 2020 706c 742e  k').        plt.
+00018d70: 6772 6964 2829 0a20 2020 2020 2020 2070  grid().        p
+00018d80: 6c74 2e74 6967 6874 5f6c 6179 6f75 7428  lt.tight_layout(
+00018d90: 290a 0a20 2020 2023 2070 796c 696e 743a  )..    # pylint:
+00018da0: 2064 6973 6162 6c65 3d69 6e63 6f6e 7369   disable=inconsi
+00018db0: 7374 656e 742d 7265 7475 726e 2d73 7461  stent-return-sta
+00018dc0: 7465 6d65 6e74 730a 2020 2020 6465 6620  tements.    def 
+00018dd0: 6361 6c63 756c 6174 655f 6c69 6674 5f67  calculate_lift_g
+00018de0: 6169 6e28 7365 6c66 2c0a 2020 2020 2020  ain(self,.      
 00018df0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018e00: 2020 2020 2020 2020 2020 2020 6e75 6d5f              num_
-00018e10: 6275 636b 6574 733a 2069 6e74 203d 2032  buckets: int = 2
-00018e20: 302c 0a20 2020 2020 2020 2020 2020 2020  0,.             
-00018e30: 2020 2020 2020 2020 2020 2020 2020 2072                 r
-00018e40: 6574 7572 6e5f 7374 796c 653a 2062 6f6f  eturn_style: boo
-00018e50: 6c20 3d20 4661 6c73 652c 0a20 2020 2020  l = False,.     
+00018e00: 2020 2020 2020 6e75 6d5f 6275 636b 6574        num_bucket
+00018e10: 733a 2069 6e74 203d 2032 302c 0a20 2020  s: int = 20,.   
+00018e20: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00018e30: 2020 2020 2020 2020 2072 6574 7572 6e5f           return_
+00018e40: 7374 796c 653a 2062 6f6f 6c20 3d20 4661  style: bool = Fa
+00018e50: 6c73 652c 0a20 2020 2020 2020 2020 2020  lse,.           
 00018e60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00018e70: 2020 2020 2020 2069 6e63 6c75 6465 5f61         include_a
-00018e80: 6c6c 5f69 6e66 6f3a 2062 6f6f 6c20 3d20  ll_info: bool = 
-00018e90: 4661 6c73 6529 202d 3e20 556e 696f 6e5b  False) -> Union[
-00018ea0: 7064 2e44 6174 6146 7261 6d65 2c20 5374  pd.DataFrame, St
-00018eb0: 796c 6572 5d3a 0a20 2020 2020 2020 2022  yler]:.        "
-00018ec0: 2222 0a20 2020 2020 2020 2068 7474 7073  "".        https
-00018ed0: 3a2f 2f77 7777 2e6c 6973 7465 6e64 6174  ://www.listendat
-00018ee0: 612e 636f 6d2f 3230 3134 2f30 382f 6578  a.com/2014/08/ex
-00018ef0: 6365 6c2d 7465 6d70 6c61 7465 2d67 6169  cel-template-gai
-00018f00: 6e2d 616e 642d 6c69 6674 2d63 6861 7274  n-and-lift-chart
-00018f10: 732e 6874 6d6c 0a0a 2020 2020 2020 2020  s.html..        
-00018f20: 4761 696e 2069 7320 7468 6520 2520 6f66  Gain is the % of
-00018f30: 2070 6f73 6974 6976 6520 2861 6374 7561   positive (actua
-00018f40: 6c29 2065 7665 6e74 7320 7765 2068 6176  l) events we hav
-00018f50: 6520 2763 6170 7475 7265 6427 2069 2e65  e 'captured' i.e
-00018f60: 2e20 6c6f 6361 7465 6420 6279 206c 6f6f  . located by loo
-00018f70: 6b69 6e67 2061 7420 7468 650a 2020 2020  king at the.    
-00018f80: 2020 2020 746f 7020 7825 206f 6620 7072      top x% of pr
-00018f90: 6564 6963 7465 6420 7363 6f72 6573 2c20  edicted scores, 
-00018fa0: 7375 6368 2074 6861 7420 7468 6520 6869  such that the hi
-00018fb0: 6768 6573 7420 7363 6f72 6573 2061 7265  ghest scores are
-00018fc0: 206c 6f6f 6b65 6420 6174 2066 6972 7374   looked at first
-00018fd0: 2e0a 2020 2020 2020 2020 466f 7220 6578  ..        For ex
-00018fe0: 616d 706c 652c 2069 6620 7468 6520 7065  ample, if the pe
-00018ff0: 7263 656e 7469 6c65 2069 7320 6035 2560  rcentile is `5%`
-00019000: 2061 6e64 2074 6865 2067 6169 6e20 7661   and the gain va
-00019010: 6c75 6520 6973 2060 302e 3360 2c20 7765  lue is `0.3`, we
-00019020: 2063 616e 2073 6179 2074 6861 7420 6966   can say that if
-00019030: 2077 6520 7261 6e64 6f6d 6c79 0a20 2020   we randomly.   
-00019040: 2020 2020 2073 6561 7263 6865 6420 6035       searched `5
-00019050: 2560 206f 6620 7468 6520 6461 7461 2c20  %` of the data, 
-00019060: 7765 2077 6f75 6c64 2065 7870 6563 7420  we would expect 
-00019070: 746f 2075 6e63 6f76 6572 2061 626f 7574  to uncover about
-00019080: 2060 3525 6020 6f66 2074 6865 2070 6f73   `5%` of the pos
-00019090: 6974 6976 6520 6576 656e 7473 3b0a 2020  itive events;.  
-000190a0: 2020 2020 2020 686f 7765 7665 722c 2077        however, w
-000190b0: 6520 6861 7665 2075 6e63 6f76 6572 6564  e have uncovered
-000190c0: 2033 3025 206f 6620 6576 656e 7473 2062   30% of events b
-000190d0: 7920 7365 6172 6368 696e 6720 7468 6520  y searching the 
-000190e0: 6869 6768 6573 7420 3525 206f 6620 7363  highest 5% of sc
-000190f0: 6f72 6573 2e0a 2020 2020 2020 2020 4c69  ores..        Li
-00019100: 6674 2069 7320 7369 6d70 6c79 2074 6865  ft is simply the
-00019110: 2072 6174 696f 206f 6620 7468 6520 7065   ratio of the pe
-00019120: 7263 656e 7420 6f66 2065 7665 6e74 7320  rcent of events 
-00019130: 7468 6174 2077 6861 7420 7765 2068 6176  that what we hav
-00019140: 6520 756e 636f 7665 7265 6420 666f 7220  e uncovered for 
-00019150: 6120 6769 7665 6e20 7065 7263 656e 7469  a given percenti
-00019160: 6c65 0a20 2020 2020 2020 206f 6620 6461  le.        of da
-00019170: 7461 2028 692e 652e 2067 6169 6e29 2064  ta (i.e. gain) d
-00019180: 6976 6964 6564 2062 7920 7768 6174 2077  ivided by what w
-00019190: 6520 776f 756c 6420 6861 7665 2065 7870  e would have exp
-000191a0: 6563 7465 6420 6279 2072 616e 646f 6d20  ected by random 
-000191b0: 6368 616e 6365 2028 692e 652e 2074 6865  chance (i.e. the
-000191c0: 2070 6572 6365 6e74 696c 6529 2e0a 2020   percentile)..  
-000191d0: 2020 2020 2020 536f 2069 6e20 7468 6520        So in the 
-000191e0: 7072 6576 696f 7573 2065 7861 6d70 6c65  previous example
-000191f0: 2c20 7765 2075 6e63 6f76 6572 6564 2033  , we uncovered 3
-00019200: 3025 206f 6620 706f 7369 7469 7665 2065  0% of positive e
-00019210: 7665 6e74 7320 6279 2073 6561 7263 6869  vents by searchi
-00019220: 6e67 2074 6865 2074 6f70 2035 2520 6f66  ng the top 5% of
-00019230: 2073 636f 7265 733b 0a20 2020 2020 2020   scores;.       
-00019240: 2077 6865 7265 6173 2069 6620 7765 2074   whereas if we t
-00019250: 6f6f 6b20 6120 7261 6e64 6f6d 2073 616d  ook a random sam
-00019260: 706c 652c 2077 6520 776f 756c 6420 6861  ple, we would ha
-00019270: 7665 206f 6e6c 7920 6578 7065 6374 6564  ve only expected
-00019280: 2074 6f20 6669 6e64 2035 2520 6f66 2074   to find 5% of t
-00019290: 6865 2070 6f73 6974 6976 6520 6576 656e  he positive even
-000192a0: 7473 2e0a 2020 2020 2020 2020 5468 6520  ts..        The 
-000192b0: 6c69 6674 2069 7320 6030 2e33 202f 2030  lift is `0.3 / 0
-000192c0: 2e30 3560 2077 6869 6368 2069 7320 6036  .05` which is `6
-000192d0: 603b 206d 6561 6e69 6e67 2077 6520 666f  `; meaning we fo
-000192e0: 756e 6420 6036 6020 7469 6d65 7320 7468  und `6` times th
-000192f0: 6520 616d 6f75 6e74 206f 6620 706f 7369  e amount of posi
-00019300: 7469 7665 2065 7665 6e74 7320 6279 0a20  tive events by. 
-00019310: 2020 2020 2020 2073 6561 7263 6869 6e67         searching
-00019320: 2074 6865 2074 6f70 2035 2520 6f66 2073   the top 5% of s
-00019330: 636f 7265 732c 2074 6861 6e20 6966 2077  cores, than if w
-00019340: 6520 7765 7265 2074 6f20 7261 6e64 6f6d  e were to random
-00019350: 6c79 2073 616d 706c 6520 7468 6520 6461  ly sample the da
-00019360: 7461 2e0a 2020 2020 2020 2020 2222 220a  ta..        """.
-00019370: 2020 2020 2020 2020 6461 7461 203d 2070          data = p
-00019380: 642e 4461 7461 4672 616d 6528 7b0a 2020  d.DataFrame({.  
-00019390: 2020 2020 2020 2020 2020 2770 7265 6469            'predi
-000193a0: 6374 6564 5f73 636f 7265 7327 3a20 7365  cted_scores': se
-000193b0: 6c66 2e5f 7072 6564 6963 7465 645f 7363  lf._predicted_sc
-000193c0: 6f72 6573 2c0a 2020 2020 2020 2020 2020  ores,.          
-000193d0: 2020 2761 6374 7561 6c5f 7661 6c75 6573    'actual_values
-000193e0: 273a 2073 656c 662e 5f61 6374 7561 6c5f  ': self._actual_
-000193f0: 7661 6c75 6573 2c0a 2020 2020 2020 2020  values,.        
-00019400: 7d29 0a20 2020 2020 2020 2064 6174 612e  }).        data.
-00019410: 736f 7274 5f76 616c 7565 7328 5b27 7072  sort_values(['pr
-00019420: 6564 6963 7465 645f 7363 6f72 6573 275d  edicted_scores']
-00019430: 2c20 6173 6365 6e64 696e 673d 4661 6c73  , ascending=Fals
-00019440: 652c 2069 6e70 6c61 6365 3d54 7275 6529  e, inplace=True)
-00019450: 0a0a 2020 2020 2020 2020 2320 2e71 6375  ..        # .qcu
-00019460: 7420 6765 7473 2070 6572 6365 6e74 696c  t gets percentil
-00019470: 6573 0a20 2020 2020 2020 2062 696e 7320  es.        bins 
-00019480: 3d20 7064 2e71 6375 7428 783d 6461 7461  = pd.qcut(x=data
-00019490: 5b27 7072 6564 6963 7465 645f 7363 6f72  ['predicted_scor
-000194a0: 6573 275d 2c0a 2020 2020 2020 2020 2020  es'],.          
-000194b0: 2020 2020 2020 2020 2020 2020 2071 3d6e               q=n
-000194c0: 756d 5f62 7563 6b65 7473 2c0a 2020 2020  um_buckets,.    
-000194d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-000194e0: 2020 206c 6162 656c 733d 6c69 7374 2872     labels=list(r
-000194f0: 616e 6765 2831 3030 2c20 302c 2072 6f75  ange(100, 0, rou
-00019500: 6e64 282d 3130 3020 2f20 6e75 6d5f 6275  nd(-100 / num_bu
-00019510: 636b 6574 7329 2929 290a 0a20 2020 2020  ckets))))..     
-00019520: 2020 2064 6174 615b 2750 6572 6365 6e74     data['Percent
-00019530: 696c 6527 5d20 3d20 6269 6e73 0a0a 2020  ile'] = bins..  
-00019540: 2020 2020 2020 6465 6620 6761 696e 5f67        def gain_g
-00019550: 726f 7570 696e 6728 6772 6f75 7029 3a0a  rouping(group):.
-00019560: 2020 2020 2020 2020 2020 2020 7265 7375              resu
-00019570: 6c74 7320 3d20 7b0a 2020 2020 2020 2020  lts = {.        
-00019580: 2020 2020 2020 2020 2723 206f 6620 4f62          '# of Ob
-00019590: 732e 273a 206c 656e 2867 726f 7570 2e61  s.': len(group.a
-000195a0: 6374 7561 6c5f 7661 6c75 6573 292c 0a20  ctual_values),. 
-000195b0: 2020 2020 2020 2020 2020 2020 2020 2027                 '
-000195c0: 2320 6f66 2050 6f73 2e20 4576 656e 7473  # of Pos. Events
-000195d0: 273a 2073 756d 2867 726f 7570 2e61 6374  ': sum(group.act
-000195e0: 7561 6c5f 7661 6c75 6573 203d 3d20 3129  ual_values == 1)
-000195f0: 0a20 2020 2020 2020 2020 2020 207d 0a20  .            }. 
-00019600: 2020 2020 2020 2020 2020 2072 6574 7572             retur
-00019610: 6e20 7064 2e53 6572 6965 7328 7265 7375  n pd.Series(resu
-00019620: 6c74 732c 2069 6e64 6578 3d5b 2723 206f  lts, index=['# o
-00019630: 6620 4f62 732e 272c 2027 2320 6f66 2050  f Obs.', '# of P
-00019640: 6f73 2e20 4576 656e 7473 275d 290a 0a20  os. Events']).. 
-00019650: 2020 2020 2020 2067 6169 6e5f 6c69 6674         gain_lift
-00019660: 5f64 6174 6120 3d20 6461 7461 2e67 726f  _data = data.gro
-00019670: 7570 6279 2827 5065 7263 656e 7469 6c65  upby('Percentile
-00019680: 2729 2e61 7070 6c79 2867 6169 6e5f 6772  ').apply(gain_gr
-00019690: 6f75 7069 6e67 290a 2020 2020 2020 2020  ouping).        
-000196a0: 7465 6d70 203d 2070 642e 4461 7461 4672  temp = pd.DataFr
-000196b0: 616d 6528 7b27 2320 6f66 204f 6273 2e27  ame({'# of Obs.'
-000196c0: 3a20 302c 2027 2320 6f66 2050 6f73 2e20  : 0, '# of Pos. 
-000196d0: 4576 656e 7473 273a 2030 7d2c 2069 6e64  Events': 0}, ind
-000196e0: 6578 3d5b 305d 290a 2020 2020 2020 2020  ex=[0]).        
-000196f0: 7465 6d70 2e69 6e64 6578 2e6e 616d 6573  temp.index.names
-00019700: 203d 205b 2750 6572 6365 6e74 696c 6527   = ['Percentile'
-00019710: 5d0a 2020 2020 2020 2020 6761 696e 5f6c  ].        gain_l
-00019720: 6966 745f 6461 7461 203d 2070 642e 636f  ift_data = pd.co
-00019730: 6e63 6174 285b 6761 696e 5f6c 6966 745f  ncat([gain_lift_
-00019740: 6461 7461 2c20 7465 6d70 5d29 0a20 2020  data, temp]).   
-00019750: 2020 2020 2067 6169 6e5f 6c69 6674 5f64       gain_lift_d
-00019760: 6174 612e 736f 7274 5f69 6e64 6578 2861  ata.sort_index(a
-00019770: 7363 656e 6469 6e67 3d54 7275 652c 2069  scending=True, i
-00019780: 6e70 6c61 6365 3d54 7275 6529 0a0a 2020  nplace=True)..  
-00019790: 2020 2020 2020 6761 696e 5f6c 6966 745f        gain_lift_
-000197a0: 6461 7461 5b27 4375 6d75 6c2e 2050 6f73  data['Cumul. Pos
-000197b0: 2e20 4576 656e 7473 275d 203d 2067 6169  . Events'] = gai
-000197c0: 6e5f 6c69 6674 5f64 6174 615b 2723 206f  n_lift_data['# o
-000197d0: 6620 506f 732e 2045 7665 6e74 7327 5d2e  f Pos. Events'].
-000197e0: 6375 6d73 756d 2829 0a20 2020 2020 2020  cumsum().       
-000197f0: 2067 6169 6e5f 6c69 6674 5f64 6174 615b   gain_lift_data[
-00019800: 2747 6169 6e27 5d20 3d20 6761 696e 5f6c  'Gain'] = gain_l
-00019810: 6966 745f 6461 7461 5b27 4375 6d75 6c2e  ift_data['Cumul.
-00019820: 2050 6f73 2e20 4576 656e 7473 275d 202f   Pos. Events'] /
-00019830: 2073 656c 662e 5f61 6374 7561 6c5f 706f   self._actual_po
-00019840: 7369 7469 7665 730a 2020 2020 2020 2020  sitives.        
-00019850: 6761 696e 5f6c 6966 745f 6461 7461 203d  gain_lift_data =
-00019860: 2067 6169 6e5f 6c69 6674 5f64 6174 612e   gain_lift_data.
-00019870: 6c6f 635b 7e28 6761 696e 5f6c 6966 745f  loc[~(gain_lift_
-00019880: 6461 7461 2e69 6e64 6578 203d 3d20 3029  data.index == 0)
-00019890: 2c20 3a5d 0a20 2020 2020 2020 2067 6169  , :].        gai
-000198a0: 6e5f 6c69 6674 5f64 6174 615b 274c 6966  n_lift_data['Lif
-000198b0: 7427 5d20 3d20 6761 696e 5f6c 6966 745f  t'] = gain_lift_
-000198c0: 6461 7461 5b27 4761 696e 275d 202f 2028  data['Gain'] / (
-000198d0: 6761 696e 5f6c 6966 745f 6461 7461 2e69  gain_lift_data.i
-000198e0: 6e64 6578 2e76 616c 7565 7320 2f20 3130  ndex.values / 10
-000198f0: 3029 0a0a 2020 2020 2020 2020 6966 206e  0)..        if n
-00019900: 6f74 2069 6e63 6c75 6465 5f61 6c6c 5f69  ot include_all_i
-00019910: 6e66 6f3a 0a20 2020 2020 2020 2020 2020  nfo:.           
-00019920: 2067 6169 6e5f 6c69 6674 5f64 6174 6120   gain_lift_data 
-00019930: 3d20 6761 696e 5f6c 6966 745f 6461 7461  = gain_lift_data
-00019940: 5b5b 2747 6169 6e27 2c20 274c 6966 7427  [['Gain', 'Lift'
-00019950: 5d5d 0a0a 2020 2020 2020 2020 6761 696e  ]]..        gain
-00019960: 5f6c 6966 745f 6461 7461 203d 2067 6169  _lift_data = gai
-00019970: 6e5f 6c69 6674 5f64 6174 612e 726f 756e  n_lift_data.roun
-00019980: 6428 3229 0a0a 2020 2020 2020 2020 6966  d(2)..        if
-00019990: 2072 6574 7572 6e5f 7374 796c 653a 0a20   return_style:. 
-000199a0: 2020 2020 2020 2020 2020 2067 6169 6e5f             gain_
-000199b0: 6c69 6674 5f64 6174 6120 3d20 6761 696e  lift_data = gain
-000199c0: 5f6c 6966 745f 6461 7461 2e73 7479 6c65  _lift_data.style
-000199d0: 0a20 2020 2020 2020 2020 2020 2067 6169  .            gai
-000199e0: 6e5f 6c69 6674 5f64 6174 612e 666f 726d  n_lift_data.form
-000199f0: 6174 2870 7265 6369 7369 6f6e 3d32 292e  at(precision=2).
-00019a00: 205c 0a20 2020 2020 2020 2020 2020 2020   \.             
-00019a10: 2020 2062 6172 2873 7562 7365 743d 2747     bar(subset='G
-00019a20: 6169 6e27 2c20 636f 6c6f 723d 6863 6f6c  ain', color=hcol
-00019a30: 6f72 2e43 6f6c 6f72 732e 5041 5354 454c  or.Colors.PASTEL
-00019a40: 5f42 4c55 452e 7661 6c75 652c 0a20 2020  _BLUE.value,.   
-00019a50: 2020 2020 2020 2020 2020 2020 2020 2020                  
-00019a60: 2076 6d69 6e3d 302c 2076 6d61 783d 3129   vmin=0, vmax=1)
-00019a70: 2e20 5c0a 2020 2020 2020 2020 2020 2020  . \.            
-00019a80: 2020 2020 6261 7228 7375 6273 6574 3d27      bar(subset='
-00019a90: 4c69 6674 272c 2063 6f6c 6f72 3d68 636f  Lift', color=hco
-00019aa0: 6c6f 722e 436f 6c6f 7273 2e50 4153 5445  lor.Colors.PASTE
-00019ab0: 4c5f 424c 5545 2e76 616c 7565 290a 0a20  L_BLUE.value).. 
-00019ac0: 2020 2020 2020 2072 6574 7572 6e20 6761         return ga
-00019ad0: 696e 5f6c 6966 745f 6461 7461 0a0a 2020  in_lift_data..  
-00019ae0: 2020 2320 7079 6c69 6e74 3a20 6469 7361    # pylint: disa
-00019af0: 626c 653d 696e 636f 6e73 6973 7465 6e74  ble=inconsistent
-00019b00: 2d72 6574 7572 6e2d 7374 6174 656d 656e  -return-statemen
-00019b10: 7473 0a20 2020 2064 6566 2070 6c6f 745f  ts.    def plot_
-00019b20: 7072 6564 6963 7465 645f 7363 6f72 6573  predicted_scores
-00019b30: 5f68 6973 746f 6772 616d 2873 656c 6629  _histogram(self)
-00019b40: 3a0a 2020 2020 2020 2020 2222 2252 6574  :.        """Ret
-00019b50: 7572 6e20 6120 6869 7374 6f67 7261 6d20  urn a histogram 
-00019b60: 6f66 2074 6865 2070 7265 6469 6374 6564  of the predicted
-00019b70: 2073 636f 7265 7322 2222 0a20 2020 2020   scores""".     
-00019b80: 2020 2073 6e73 2e68 6973 7470 6c6f 7428     sns.histplot(
-00019b90: 7365 6c66 2e5f 7072 6564 6963 7465 645f  self._predicted_
-00019ba0: 7363 6f72 6573 290a 2020 2020 2020 2020  scores).        
-00019bb0: 706c 742e 7469 6768 745f 6c61 796f 7574  plt.tight_layout
-00019bc0: 2829 0a0a 2020 2020 2320 7079 6c69 6e74  ()..    # pylint
-00019bd0: 3a20 6469 7361 626c 653d 696e 636f 6e73  : disable=incons
-00019be0: 6973 7465 6e74 2d72 6574 7572 6e2d 7374  istent-return-st
-00019bf0: 6174 656d 656e 7473 0a20 2020 2064 6566  atements.    def
-00019c00: 2070 6c6f 745f 6163 7475 616c 5f76 735f   plot_actual_vs_
-00019c10: 7072 6564 6963 745f 6869 7374 6f67 7261  predict_histogra
-00019c20: 6d28 7365 6c66 293a 0a20 2020 2020 2020  m(self):.       
-00019c30: 2022 2222 5265 7475 726e 2061 2068 6973   """Return a his
-00019c40: 746f 6772 616d 206f 6620 7468 6520 6163  togram of the ac
-00019c50: 7475 616c 2076 7320 7072 6564 6963 7465  tual vs predicte
-00019c60: 6420 7363 6f72 6573 2222 220a 2020 2020  d scores""".    
-00019c70: 2020 2020 6163 7475 616c 5f63 6174 6567      actual_categ
-00019c80: 6f72 6965 7320 3d20 7064 2e53 6572 6965  ories = pd.Serie
-00019c90: 7328 7365 6c66 2e5f 6163 7475 616c 5f76  s(self._actual_v
-00019ca0: 616c 7565 7329 2e5c 0a20 2020 2020 2020  alues).\.       
-00019cb0: 2020 2020 2072 6570 6c61 6365 287b 303a       replace({0:
-00019cc0: 2073 656c 662e 5f6e 6567 6174 6976 655f   self._negative_
-00019cd0: 636c 6173 732c 2031 3a20 7365 6c66 2e5f  class, 1: self._
-00019ce0: 706f 7369 7469 7665 5f63 6c61 7373 7d29  positive_class})
-00019cf0: 0a20 2020 2020 2020 2061 7865 7320 3d20  .        axes = 
-00019d00: 736e 732e 6469 7370 6c6f 7428 0a20 2020  sns.displot(.   
-00019d10: 2020 2020 2020 2020 2070 642e 4461 7461           pd.Data
-00019d20: 4672 616d 6528 7b0a 2020 2020 2020 2020  Frame({.        
-00019d30: 2020 2020 2020 2020 2750 7265 6469 6374          'Predict
-00019d40: 6564 2053 636f 7265 273a 2073 656c 662e  ed Score': self.
-00019d50: 5f70 7265 6469 6374 6564 5f73 636f 7265  _predicted_score
-00019d60: 732c 0a20 2020 2020 2020 2020 2020 2020  s,.             
-00019d70: 2020 2027 4163 7475 616c 2056 616c 7565     'Actual Value
-00019d80: 273a 2061 6374 7561 6c5f 6361 7465 676f  ': actual_catego
-00019d90: 7269 6573 0a20 2020 2020 2020 2020 2020  ries.           
-00019da0: 207d 292c 0a20 2020 2020 2020 2020 2020   }),.           
-00019db0: 2078 3d27 5072 6564 6963 7465 6420 5363   x='Predicted Sc
-00019dc0: 6f72 6527 2c0a 2020 2020 2020 2020 2020  ore',.          
-00019dd0: 2020 636f 6c3d 2741 6374 7561 6c20 5661    col='Actual Va
-00019de0: 6c75 6527 0a20 2020 2020 2020 2029 0a20  lue'.        ). 
-00019df0: 2020 2020 2020 2066 6f72 2061 7869 7320         for axis 
-00019e00: 696e 2061 7865 732e 6178 6573 2e66 6c61  in axes.axes.fla
-00019e10: 743a 0a20 2020 2020 2020 2020 2020 2061  t:.            a
-00019e20: 7869 732e 6178 766c 696e 6528 783d 302e  xis.axvline(x=0.
-00019e30: 352c 2079 6d69 6e3d 302c 2079 6d61 783d  5, ymin=0, ymax=
-00019e40: 3130 302c 2063 6f6c 6f72 3d27 7265 6427  100, color='red'
-00019e50: 290a 2020 2020 2020 2020 706c 742e 7469  ).        plt.ti
-00019e60: 6768 745f 6c61 796f 7574 2829 0a0a 0a63  ght_layout()...c
-00019e70: 6c61 7373 2052 6567 7265 7373 696f 6e45  lass RegressionE
-00019e80: 7661 6c75 6174 6f72 3a0a 2020 2020 2222  valuator:.    ""
-00019e90: 220a 2020 2020 4576 616c 7561 7465 7320  ".    Evaluates 
-00019ea0: 6d6f 6465 6c73 2066 6f72 2072 6567 7265  models for regre
-00019eb0: 7373 696f 6e20 2869 2e65 2e20 6e75 6d65  ssion (i.e. nume
-00019ec0: 7269 6320 6f75 7463 6f6d 6529 2070 726f  ric outcome) pro
-00019ed0: 626c 656d 732e 0a20 2020 2022 2222 0a20  blems..    """. 
-00019ee0: 2020 2064 6566 205f 5f69 6e69 745f 5f28     def __init__(
-00019ef0: 7365 6c66 2c0a 2020 2020 2020 2020 2020  self,.          
-00019f00: 2020 2020 2020 2061 6374 7561 6c5f 7661         actual_va
-00019f10: 6c75 6573 3a20 6e70 2e6e 6461 7272 6179  lues: np.ndarray
-00019f20: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-00019f30: 2020 2070 7265 6469 6374 6564 5f76 616c     predicted_val
-00019f40: 7565 733a 206e 702e 6e64 6172 7261 7929  ues: np.ndarray)
-00019f50: 3a0a 2020 2020 2020 2020 2222 220a 2020  :.        """.  
-00019f60: 2020 2020 2020 4172 6773 3a0a 2020 2020        Args:.    
-00019f70: 2020 2020 2020 2020 6163 7475 616c 5f76          actual_v
-00019f80: 616c 7565 733a 0a20 2020 2020 2020 2020  alues:.         
-00019f90: 2020 2020 2020 2074 6865 2061 6374 7561         the actua
-00019fa0: 6c20 7661 6c75 6573 0a20 2020 2020 2020  l values.       
-00019fb0: 2020 2020 2070 7265 6469 6374 6564 5f76       predicted_v
-00019fc0: 616c 7565 733a 0a20 2020 2020 2020 2020  alues:.         
-00019fd0: 2020 2020 2020 2074 6865 2070 7265 6469         the predi
-00019fe0: 6374 6564 2076 616c 7565 730a 2020 2020  cted values.    
-00019ff0: 2020 2020 2222 220a 0a20 2020 2020 2020      """..       
-0001a000: 2061 7373 6572 7420 6c65 6e28 6163 7475   assert len(actu
-0001a010: 616c 5f76 616c 7565 7329 203d 3d20 6c65  al_values) == le
-0001a020: 6e28 7072 6564 6963 7465 645f 7661 6c75  n(predicted_valu
-0001a030: 6573 290a 0a20 2020 2020 2020 2073 656c  es)..        sel
-0001a040: 662e 5f61 6374 7561 6c5f 7661 6c75 6573  f._actual_values
-0001a050: 203d 2061 6374 7561 6c5f 7661 6c75 6573   = actual_values
-0001a060: 0a20 2020 2020 2020 2073 656c 662e 5f70  .        self._p
-0001a070: 7265 6469 6374 6564 5f76 616c 7565 7320  redicted_values 
-0001a080: 3d20 7072 6564 6963 7465 645f 7661 6c75  = predicted_valu
-0001a090: 6573 0a20 2020 2020 2020 2073 656c 662e  es.        self.
-0001a0a0: 5f72 6573 6964 7561 6c73 203d 2061 6374  _residuals = act
-0001a0b0: 7561 6c5f 7661 6c75 6573 202d 2070 7265  ual_values - pre
-0001a0c0: 6469 6374 6564 5f76 616c 7565 730a 2020  dicted_values.  
-0001a0d0: 2020 2020 2020 7365 6c66 2e5f 7374 616e        self._stan
-0001a0e0: 6461 7264 5f64 6576 6961 7469 6f6e 203d  dard_deviation =
-0001a0f0: 206e 702e 7374 6428 6163 7475 616c 5f76   np.std(actual_v
-0001a100: 616c 7565 7329 0a20 2020 2020 2020 2073  alues).        s
-0001a110: 656c 662e 5f6d 6561 6e5f 7371 7561 7265  elf._mean_square
-0001a120: 645f 6572 726f 7220 3d20 666c 6f61 7428  d_error = float(
-0001a130: 6e70 2e6d 6561 6e28 6e70 2e73 7175 6172  np.mean(np.squar
-0001a140: 6528 6163 7475 616c 5f76 616c 7565 7320  e(actual_values 
-0001a150: 2d20 7072 6564 6963 7465 645f 7661 6c75  - predicted_valu
-0001a160: 6573 2929 290a 2020 2020 2020 2020 7365  es))).        se
-0001a170: 6c66 2e5f 6d65 616e 5f61 6273 6f6c 7574  lf._mean_absolut
-0001a180: 655f 6572 726f 7220 3d20 666c 6f61 7428  e_error = float(
-0001a190: 6e70 2e6d 6561 6e28 6e70 2e61 6273 2861  np.mean(np.abs(a
-0001a1a0: 6374 7561 6c5f 7661 6c75 6573 202d 2070  ctual_values - p
-0001a1b0: 7265 6469 6374 6564 5f76 616c 7565 7329  redicted_values)
-0001a1c0: 2929 0a20 2020 2020 2020 2073 656c 662e  )).        self.
-0001a1d0: 5f72 5f73 7175 6172 6564 203d 2072 325f  _r_squared = r2_
-0001a1e0: 7363 6f72 6528 795f 7472 7565 3d61 6374  score(y_true=act
-0001a1f0: 7561 6c5f 7661 6c75 6573 2c20 795f 7072  ual_values, y_pr
-0001a200: 6564 3d70 7265 6469 6374 6564 5f76 616c  ed=predicted_val
-0001a210: 7565 7329 0a0a 2020 2020 4070 726f 7065  ues)..    @prope
-0001a220: 7274 790a 2020 2020 6465 6620 6d65 616e  rty.    def mean
-0001a230: 5f61 6273 6f6c 7574 655f 6572 726f 7228  _absolute_error(
-0001a240: 7365 6c66 2920 2d3e 2066 6c6f 6174 3a0a  self) -> float:.
-0001a250: 2020 2020 2020 2020 2222 224d 6561 6e20          """Mean 
-0001a260: 4162 736f 6c75 7465 2045 7272 6f72 2222  Absolute Error""
-0001a270: 220a 2020 2020 2020 2020 7265 7475 726e  ".        return
-0001a280: 2073 656c 662e 5f6d 6561 6e5f 6162 736f   self._mean_abso
-0001a290: 6c75 7465 5f65 7272 6f72 0a0a 2020 2020  lute_error..    
-0001a2a0: 4070 726f 7065 7274 790a 2020 2020 6465  @property.    de
-0001a2b0: 6620 6d65 616e 5f73 7175 6172 6564 5f65  f mean_squared_e
-0001a2c0: 7272 6f72 2873 656c 6629 202d 3e20 666c  rror(self) -> fl
-0001a2d0: 6f61 743a 0a20 2020 2020 2020 2022 2222  oat:.        """
-0001a2e0: 4d65 616e 2053 7175 6172 6564 2045 7272  Mean Squared Err
-0001a2f0: 6f72 2222 220a 2020 2020 2020 2020 7265  or""".        re
-0001a300: 7475 726e 2073 656c 662e 5f6d 6561 6e5f  turn self._mean_
-0001a310: 7371 7561 7265 645f 6572 726f 720a 0a20  squared_error.. 
-0001a320: 2020 2040 7072 6f70 6572 7479 0a20 2020     @property.   
-0001a330: 2064 6566 2072 6f6f 745f 6d65 616e 5f73   def root_mean_s
-0001a340: 7175 6172 6564 5f65 7272 6f72 2873 656c  quared_error(sel
-0001a350: 6629 202d 3e20 666c 6f61 743a 0a20 2020  f) -> float:.   
-0001a360: 2020 2020 2022 2222 526f 6f74 204d 6561       """Root Mea
-0001a370: 6e20 5371 7561 7265 6420 4572 726f 7222  n Squared Error"
-0001a380: 2222 0a20 2020 2020 2020 2072 6574 7572  "".        retur
-0001a390: 6e20 6e70 2e73 7172 7428 7365 6c66 2e6d  n np.sqrt(self.m
-0001a3a0: 6561 6e5f 7371 7561 7265 645f 6572 726f  ean_squared_erro
-0001a3b0: 7229 0a0a 2020 2020 4070 726f 7065 7274  r)..    @propert
-0001a3c0: 790a 2020 2020 6465 6620 726d 7365 5f74  y.    def rmse_t
-0001a3d0: 6f5f 7374 5f64 6576 2873 656c 6629 202d  o_st_dev(self) -
-0001a3e0: 3e20 666c 6f61 743a 0a20 2020 2020 2020  > float:.       
-0001a3f0: 2022 2222 5468 6520 7261 7469 6f20 6f66   """The ratio of
-0001a400: 2052 4d53 4520 746f 2074 6865 2073 7461   RMSE to the sta
-0001a410: 6e64 6172 6420 6465 7669 6174 696f 6e20  ndard deviation 
-0001a420: 6f66 2074 6865 2061 6374 7561 6c20 7661  of the actual va
-0001a430: 6c75 6573 2e0a 2020 2020 2020 2020 4769  lues..        Gi
-0001a440: 7665 7320 616e 2069 6e64 6963 6174 696f  ves an indicatio
-0001a450: 6e20 6f66 2068 6f77 206c 6172 6765 2074  n of how large t
-0001a460: 6865 2065 7272 6f72 7320 6172 6520 746f  he errors are to
-0001a470: 2074 6865 2061 6374 7561 6c20 6461 7461   the actual data
-0001a480: 2e0a 2020 2020 2020 2020 2222 220a 2020  ..        """.  
-0001a490: 2020 2020 2020 7265 7475 726e 2073 656c        return sel
-0001a4a0: 662e 726f 6f74 5f6d 6561 6e5f 7371 7561  f.root_mean_squa
-0001a4b0: 7265 645f 6572 726f 7220 2f20 7365 6c66  red_error / self
-0001a4c0: 2e5f 7374 616e 6461 7264 5f64 6576 6961  ._standard_devia
-0001a4d0: 7469 6f6e 0a0a 2020 2020 4070 726f 7065  tion..    @prope
-0001a4e0: 7274 790a 2020 2020 6465 6620 725f 7371  rty.    def r_sq
-0001a4f0: 7561 7265 6428 7365 6c66 2920 2d3e 2066  uared(self) -> f
-0001a500: 6c6f 6174 3a0a 2020 2020 2020 2020 2222  loat:.        ""
-0001a510: 2252 2053 7175 6172 6564 2222 220a 2020  "R Squared""".  
-0001a520: 2020 2020 2020 7265 7475 726e 2073 656c        return sel
-0001a530: 662e 5f72 5f73 7175 6172 6564 0a0a 2020  f._r_squared..  
-0001a540: 2020 4070 726f 7065 7274 790a 2020 2020    @property.    
-0001a550: 6465 6620 746f 7461 6c5f 6f62 7365 7276  def total_observ
-0001a560: 6174 696f 6e73 2873 656c 6629 3a0a 2020  ations(self):.  
-0001a570: 2020 2020 2020 2222 2254 6865 2074 6f74        """The tot
-0001a580: 616c 206e 756d 6265 7220 6f66 206f 6273  al number of obs
-0001a590: 6572 7661 7469 6f6e 7320 692e 652e 2073  ervations i.e. s
-0001a5a0: 616d 706c 6520 7369 7a65 2e22 2222 0a20  ample size.""". 
-0001a5b0: 2020 2020 2020 2072 6574 7572 6e20 6c65         return le
-0001a5c0: 6e28 7365 6c66 2e5f 6163 7475 616c 5f76  n(self._actual_v
-0001a5d0: 616c 7565 7329 0a0a 2020 2020 4070 726f  alues)..    @pro
-0001a5e0: 7065 7274 790a 2020 2020 6465 6620 616c  perty.    def al
-0001a5f0: 6c5f 6d65 7472 6963 7328 7365 6c66 2920  l_metrics(self) 
-0001a600: 2d3e 2064 6963 743a 0a20 2020 2020 2020  -> dict:.       
-0001a610: 2022 2222 5265 7475 726e 7320 6120 6469   """Returns a di
-0001a620: 6374 696f 6e61 7279 206f 6620 7468 6520  ctionary of the 
-0001a630: 6d6f 7374 2063 6f6d 6d6f 6e20 6572 726f  most common erro
-0001a640: 7220 6d65 7472 6963 7320 666f 7220 7265  r metrics for re
-0001a650: 6772 6573 7369 6f6e 2070 726f 626c 656d  gression problem
-0001a660: 732e 2222 220a 2020 2020 2020 2020 7265  s.""".        re
-0001a670: 7475 726e 207b 274d 6561 6e20 4162 736f  turn {'Mean Abso
-0001a680: 6c75 7465 2045 7272 6f72 2028 4d41 4529  lute Error (MAE)
-0001a690: 273a 2073 656c 662e 6d65 616e 5f61 6273  ': self.mean_abs
-0001a6a0: 6f6c 7574 655f 6572 726f 722c 0a20 2020  olute_error,.   
-0001a6b0: 2020 2020 2020 2020 2020 2020 2027 526f               'Ro
-0001a6c0: 6f74 204d 6561 6e20 5371 7561 7265 6420  ot Mean Squared 
-0001a6d0: 4572 726f 7220 2852 4d53 4529 273a 2073  Error (RMSE)': s
-0001a6e0: 656c 662e 726f 6f74 5f6d 6561 6e5f 7371  elf.root_mean_sq
-0001a6f0: 7561 7265 645f 6572 726f 722c 0a20 2020  uared_error,.   
-0001a700: 2020 2020 2020 2020 2020 2020 2027 524d               'RM
-0001a710: 5345 2074 6f20 5374 616e 6461 7264 2044  SE to Standard D
-0001a720: 6576 6961 7469 6f6e 206f 6620 5461 7267  eviation of Targ
-0001a730: 6574 273a 2073 656c 662e 726d 7365 5f74  et': self.rmse_t
-0001a740: 6f5f 7374 5f64 6576 2c0a 2020 2020 2020  o_st_dev,.      
-0001a750: 2020 2020 2020 2020 2020 2752 2053 7175            'R Squ
-0001a760: 6172 6564 273a 2073 656c 662e 725f 7371  ared': self.r_sq
-0001a770: 7561 7265 642c 0a20 2020 2020 2020 2020  uared,.         
-0001a780: 2020 2020 2020 2027 546f 7461 6c20 4f62         'Total Ob
-0001a790: 7365 7276 6174 696f 6e73 273a 2073 656c  servations': sel
-0001a7a0: 662e 746f 7461 6c5f 6f62 7365 7276 6174  f.total_observat
-0001a7b0: 696f 6e73 7d0a 0a20 2020 2064 6566 2061  ions}..    def a
-0001a7c0: 6c6c 5f6d 6574 7269 6373 5f64 6628 7365  ll_metrics_df(se
-0001a7d0: 6c66 2c0a 2020 2020 2020 2020 2020 2020  lf,.            
-0001a7e0: 2020 2020 2020 2020 2020 2064 756d 6d79             dummy
-0001a7f0: 5f72 6567 7265 7373 6f72 5f73 7472 6174  _regressor_strat
-0001a800: 6567 793a 2055 6e69 6f6e 5b73 7472 2c20  egy: Union[str, 
-0001a810: 6c69 7374 2c20 4e6f 6e65 5d20 3d20 276d  list, None] = 'm
-0001a820: 6561 6e27 2c0a 2020 2020 2020 2020 2020  ean',.          
-0001a830: 2020 2020 2020 2020 2020 2020 2064 756d               dum
-0001a840: 6d79 5f72 6567 7265 7373 6f72 5f63 6f6e  my_regressor_con
-0001a850: 7374 616e 743a 2055 6e69 6f6e 5b69 6e74  stant: Union[int
-0001a860: 5d20 3d20 312c 0a20 2020 2020 2020 2020  ] = 1,.         
-0001a870: 2020 2020 2020 2020 2020 2020 2020 7265                re
-0001a880: 7475 726e 5f73 7479 6c65 3a20 626f 6f6c  turn_style: bool
-0001a890: 203d 2046 616c 7365 2c0a 2020 2020 2020   = False,.      
-0001a8a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001a8b0: 2072 6f75 6e64 5f62 793a 204f 7074 696f   round_by: Optio
-0001a8c0: 6e61 6c5b 696e 745d 203d 204e 6f6e 6529  nal[int] = None)
-0001a8d0: 202d 3e20 556e 696f 6e5b 7064 2e44 6174   -> Union[pd.Dat
-0001a8e0: 6146 7261 6d65 2c20 5374 796c 6572 5d3a  aFrame, Styler]:
-0001a8f0: 0a20 2020 2020 2020 2022 2222 416c 6c20  .        """All 
-0001a900: 6f66 2074 6865 206d 6574 7269 6373 2061  of the metrics a
-0001a910: 7265 2072 6574 7572 6e65 6420 6173 2061  re returned as a
-0001a920: 2044 6174 6146 7261 6d65 2e0a 0a20 2020   DataFrame...   
-0001a930: 2020 2020 2041 7267 733a 0a20 2020 2020       Args:.     
-0001a940: 2020 2020 2020 2064 756d 6d79 5f72 6567         dummy_reg
-0001a950: 7265 7373 6f72 5f73 7472 6174 6567 793a  ressor_strategy:
-0001a960: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001a970: 2069 6620 6e6f 7420 4e6f 6e65 2c20 7468   if not None, th
-0001a980: 656e 2072 6574 7572 6e73 2063 6f6c 756d  en returns colum
-0001a990: 6e28 7329 2063 6f72 7265 7370 6f6e 6469  n(s) correspondi
-0001a9a0: 6e67 2074 6f20 7468 6520 7363 6f72 6573  ng to the scores
-0001a9b0: 2066 726f 6d20 7072 6564 6963 7469 6f6e   from prediction
-0001a9c0: 7320 6f66 0a20 2020 2020 2020 2020 2020  s of.           
-0001a9d0: 2020 2020 2073 6b6c 6561 726e 2e64 756d       sklearn.dum
-0001a9e0: 6d79 2e44 756d 6d79 5265 6772 6573 736f  my.DummyRegresso
-0001a9f0: 722c 2062 6173 6564 206f 6e20 7468 6520  r, based on the 
-0001aa00: 7374 7261 7465 6779 2028 6f72 2073 7472  strategy (or str
-0001aa10: 6174 6567 6965 7329 2070 726f 7669 6465  ategies) provide
-0001aa20: 642e 2056 616c 6964 2076 616c 7565 730a  d. Valid values.
-0001aa30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001aa40: 636f 7272 6573 706f 6e64 2074 6f20 7661  correspond to va
-0001aa50: 6c75 6573 206f 6620 6073 7472 6174 6567  lues of `strateg
-0001aa60: 7960 2070 6172 616d 6574 6572 206c 6973  y` parameter lis
-0001aa70: 7465 640a 2020 2020 2020 2020 2020 2020  ted.            
-0001aa80: 2020 2020 6874 7470 733a 2f2f 7363 696b      https://scik
-0001aa90: 6974 2d6c 6561 726e 2e6f 7267 2f73 7461  it-learn.org/sta
-0001aaa0: 626c 652f 6d6f 6475 6c65 732f 6765 6e65  ble/modules/gene
-0001aab0: 7261 7465 642f 736b 6c65 6172 6e2e 6475  rated/sklearn.du
-0001aac0: 6d6d 792e 4475 6d6d 7952 6567 7265 7373  mmy.DummyRegress
-0001aad0: 6f72 2e68 746d 6c0a 0a20 2020 2020 2020  or.html..       
-0001aae0: 2020 2020 2020 2020 2049 6620 6120 6c69           If a li
-0001aaf0: 7374 2069 7320 7061 7373 6564 2069 6e20  st is passed in 
-0001ab00: 2865 2e67 2e20 5b27 7072 696f 7227 2c20  (e.g. ['prior', 
-0001ab10: 2775 6e69 666f 726d 275d 2c20 7468 656e  'uniform'], then
-0001ab20: 206f 6e65 2073 636f 7265 2063 6f6c 756d   one score colum
-0001ab30: 6e20 7065 7220 7661 6c75 6520 6973 0a20  n per value is. 
-0001ab40: 2020 2020 2020 2020 2020 2020 2020 2061                 a
-0001ab50: 6464 6564 2e0a 0a20 2020 2020 2020 2020  dded...         
-0001ab60: 2020 2020 2020 2049 6620 4e6f 6e65 2069         If None i
-0001ab70: 7320 7061 7373 6564 2c20 7468 656e 206e  s passed, then n
-0001ab80: 6f20 6164 6469 7469 6f6e 616c 2063 6f6c  o additional col
-0001ab90: 756d 6e73 2061 7265 2061 6464 6564 2e0a  umns are added..
-0001aba0: 2020 2020 2020 2020 2020 2020 6475 6d6d              dumm
-0001abb0: 795f 7265 6772 6573 736f 725f 636f 6e73  y_regressor_cons
-0001abc0: 7461 6e74 3a0a 2020 2020 2020 2020 2020  tant:.          
-0001abd0: 2020 2020 2020 5468 6520 6578 706c 6963        The explic
-0001abe0: 6974 2063 6f6e 7374 616e 7420 6173 2070  it constant as p
-0001abf0: 7265 6469 6374 6564 2062 7920 7468 6520  redicted by the 
-0001ac00: e280 9c63 6f6e 7374 616e 74e2 809d 2073  ...constant... s
-0001ac10: 7472 6174 6567 7920 666f 7220 7468 650a  trategy for the.
-0001ac20: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001ac30: 4475 6d6d 7952 6567 7265 7373 6f72 2e0a  DummyRegressor..
-0001ac40: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001ac50: 5468 6973 2070 6172 616d 6574 6572 2069  This parameter i
-0001ac60: 7320 7573 6566 756c 206f 6e6c 7920 666f  s useful only fo
-0001ac70: 7220 7468 6520 e280 9c63 6f6e 7374 616e  r the ...constan
-0001ac80: 74e2 809d 2064 756d 6d79 5f72 6567 7265  t... dummy_regre
-0001ac90: 7373 6f72 5f73 7472 6174 6567 792e 0a20  ssor_strategy.. 
-0001aca0: 2020 2020 2020 2020 2020 2072 6574 7572             retur
-0001acb0: 6e5f 7374 796c 653a 0a20 2020 2020 2020  n_style:.       
-0001acc0: 2020 2020 2020 2020 2069 6620 5472 7565           if True
-0001acd0: 2c20 7265 7475 726e 2073 7479 6c65 7220  , return styler 
-0001ace0: 6f62 6a65 6374 3b20 656c 7365 2072 6574  object; else ret
-0001acf0: 7572 6e20 6461 7461 6672 616d 650a 2020  urn dataframe.  
-0001ad00: 2020 2020 2020 2020 2020 726f 756e 645f            round_
-0001ad10: 6279 3a0a 2020 2020 2020 2020 2020 2020  by:.            
-0001ad20: 2020 2020 7468 6520 6e75 6d62 6572 206f      the number o
-0001ad30: 6620 6469 6769 7473 2074 6f20 726f 756e  f digits to roun
-0001ad40: 6420 6279 3b20 6966 204e 6f6e 652c 2074  d by; if None, t
-0001ad50: 6865 6e20 646f 6e27 7420 726f 756e 640a  hen don't round.
-0001ad60: 2020 2020 2020 2020 2222 220a 2020 2020          """.    
-0001ad70: 2020 2020 7265 7375 6c74 203d 2070 642e      result = pd.
-0001ad80: 4461 7461 4672 616d 652e 6672 6f6d 5f64  DataFrame.from_d
-0001ad90: 6963 7428 7365 6c66 2e61 6c6c 5f6d 6574  ict(self.all_met
-0001ada0: 7269 6373 2c20 6f72 6965 6e74 3d27 696e  rics, orient='in
-0001adb0: 6465 7827 2c20 636f 6c75 6d6e 733d 5b27  dex', columns=['
-0001adc0: 5363 6f72 6527 5d29 0a0a 2020 2020 2020  Score'])..      
-0001add0: 2020 7363 6f72 655f 636f 6c75 6d6e 7320    score_columns 
-0001ade0: 3d20 5b27 5363 6f72 6527 5d0a 0a20 2020  = ['Score']..   
-0001adf0: 2020 2020 2069 6620 6475 6d6d 795f 7265       if dummy_re
-0001ae00: 6772 6573 736f 725f 7374 7261 7465 6779  gressor_strategy
-0001ae10: 3a0a 2020 2020 2020 2020 2020 2020 6966  :.            if
-0001ae20: 2069 7369 6e73 7461 6e63 6528 6475 6d6d   isinstance(dumm
-0001ae30: 795f 7265 6772 6573 736f 725f 7374 7261  y_regressor_stra
-0001ae40: 7465 6779 2c20 7374 7229 3a0a 2020 2020  tegy, str):.    
-0001ae50: 2020 2020 2020 2020 2020 2020 6475 6d6d              dumm
-0001ae60: 795f 7265 6772 6573 736f 725f 7374 7261  y_regressor_stra
-0001ae70: 7465 6779 203d 205b 6475 6d6d 795f 7265  tegy = [dummy_re
-0001ae80: 6772 6573 736f 725f 7374 7261 7465 6779  gressor_strategy
-0001ae90: 5d0a 0a20 2020 2020 2020 2020 2020 2066  ]..            f
-0001aea0: 6f72 2073 7472 6174 6567 7920 696e 2064  or strategy in d
-0001aeb0: 756d 6d79 5f72 6567 7265 7373 6f72 5f73  ummy_regressor_s
-0001aec0: 7472 6174 6567 793a 0a20 2020 2020 2020  trategy:.       
-0001aed0: 2020 2020 2020 2020 2064 756d 6d79 203d           dummy =
-0001aee0: 2044 756d 6d79 5265 6772 6573 736f 7228   DummyRegressor(
-0001aef0: 7374 7261 7465 6779 3d73 7472 6174 6567  strategy=strateg
-0001af00: 792c 2063 6f6e 7374 616e 743d 6475 6d6d  y, constant=dumm
-0001af10: 795f 7265 6772 6573 736f 725f 636f 6e73  y_regressor_cons
-0001af20: 7461 6e74 290a 2020 2020 2020 2020 2020  tant).          
-0001af30: 2020 2020 2020 2320 6874 7470 733a 2f2f        # https://
-0001af40: 7363 696b 6974 2d6c 6561 726e 2e6f 7267  scikit-learn.org
-0001af50: 2f73 7461 626c 652f 6d6f 6475 6c65 732f  /stable/modules/
-0001af60: 6765 6e65 7261 7465 642f 736b 6c65 6172  generated/sklear
-0001af70: 6e2e 6475 6d6d 792e 4475 6d6d 7943 6c61  n.dummy.DummyCla
-0001af80: 7373 6966 6965 722e 6874 6d6c 0a20 2020  ssifier.html.   
-0001af90: 2020 2020 2020 2020 2020 2020 2023 2022               # "
-0001afa0: 416c 6c20 7374 7261 7465 6769 6573 206d  All strategies m
-0001afb0: 616b 6520 7072 6564 6963 7469 6f6e 7320  ake predictions 
-0001afc0: 7468 6174 2069 676e 6f72 6520 7468 6520  that ignore the 
-0001afd0: 696e 7075 7420 6665 6174 7572 6520 7661  input feature va
-0001afe0: 6c75 6573 2070 6173 7365 6420 6173 2074  lues passed as t
-0001aff0: 6865 2058 0a20 2020 2020 2020 2020 2020  he X.           
-0001b000: 2020 2020 2023 2061 7267 756d 656e 7420       # argument 
-0001b010: 746f 2066 6974 2061 6e64 2070 7265 6469  to fit and predi
-0001b020: 6374 2e20 5468 6520 7072 6564 6963 7469  ct. The predicti
-0001b030: 6f6e 732c 2068 6f77 6576 6572 2c20 7479  ons, however, ty
-0001b040: 7069 6361 6c6c 7920 6465 7065 6e64 206f  pically depend o
-0001b050: 6e20 7661 6c75 6573 206f 6273 6572 7665  n values observe
-0001b060: 640a 2020 2020 2020 2020 2020 2020 2020  d.              
-0001b070: 2020 2320 696e 2074 6865 2079 2070 6172    # in the y par
-0001b080: 616d 6574 6572 2070 6173 7365 6420 746f  ameter passed to
-0001b090: 2066 6974 2e22 0a20 2020 2020 2020 2020   fit.".         
-0001b0a0: 2020 2020 2020 205f 203d 2064 756d 6d79         _ = dummy
-0001b0b0: 2e66 6974 2858 3d73 656c 662e 5f61 6374  .fit(X=self._act
-0001b0c0: 7561 6c5f 7661 6c75 6573 2c20 793d 7365  ual_values, y=se
-0001b0d0: 6c66 2e5f 6163 7475 616c 5f76 616c 7565  lf._actual_value
-0001b0e0: 7329 0a20 2020 2020 2020 2020 2020 2020  s).             
-0001b0f0: 2020 2064 756d 6d79 5f70 7265 6469 6374     dummy_predict
-0001b100: 696f 6e73 203d 2064 756d 6d79 2e70 7265  ions = dummy.pre
-0001b110: 6469 6374 2858 3d73 656c 662e 5f61 6374  dict(X=self._act
-0001b120: 7561 6c5f 7661 6c75 6573 290a 2020 2020  ual_values).    
-0001b130: 2020 2020 2020 2020 2020 2020 6475 6d6d              dumm
-0001b140: 795f 6576 616c 7561 746f 7220 3d20 5265  y_evaluator = Re
-0001b150: 6772 6573 7369 6f6e 4576 616c 7561 746f  gressionEvaluato
-0001b160: 7228 6163 7475 616c 5f76 616c 7565 733d  r(actual_values=
-0001b170: 7365 6c66 2e5f 6163 7475 616c 5f76 616c  self._actual_val
-0001b180: 7565 732c 0a20 2020 2020 2020 2020 2020  ues,.           
+00018e70: 2069 6e63 6c75 6465 5f61 6c6c 5f69 6e66   include_all_inf
+00018e80: 6f3a 2062 6f6f 6c20 3d20 4661 6c73 6529  o: bool = False)
+00018e90: 202d 3e20 556e 696f 6e5b 7064 2e44 6174   -> Union[pd.Dat
+00018ea0: 6146 7261 6d65 2c20 5374 796c 6572 5d3a  aFrame, Styler]:
+00018eb0: 0a20 2020 2020 2020 2022 2222 0a20 2020  .        """.   
+00018ec0: 2020 2020 2068 7474 7073 3a2f 2f77 7777       https://www
+00018ed0: 2e6c 6973 7465 6e64 6174 612e 636f 6d2f  .listendata.com/
+00018ee0: 3230 3134 2f30 382f 6578 6365 6c2d 7465  2014/08/excel-te
+00018ef0: 6d70 6c61 7465 2d67 6169 6e2d 616e 642d  mplate-gain-and-
+00018f00: 6c69 6674 2d63 6861 7274 732e 6874 6d6c  lift-charts.html
+00018f10: 0a0a 2020 2020 2020 2020 4761 696e 2069  ..        Gain i
+00018f20: 7320 7468 6520 2520 6f66 2070 6f73 6974  s the % of posit
+00018f30: 6976 6520 2861 6374 7561 6c29 2065 7665  ive (actual) eve
+00018f40: 6e74 7320 7765 2068 6176 6520 2763 6170  nts we have 'cap
+00018f50: 7475 7265 6427 2069 2e65 2e20 6c6f 6361  tured' i.e. loca
+00018f60: 7465 6420 6279 206c 6f6f 6b69 6e67 2061  ted by looking a
+00018f70: 7420 7468 650a 2020 2020 2020 2020 746f  t the.        to
+00018f80: 7020 7825 206f 6620 7072 6564 6963 7465  p x% of predicte
+00018f90: 6420 7363 6f72 6573 2c20 7375 6368 2074  d scores, such t
+00018fa0: 6861 7420 7468 6520 6869 6768 6573 7420  hat the highest 
+00018fb0: 7363 6f72 6573 2061 7265 206c 6f6f 6b65  scores are looke
+00018fc0: 6420 6174 2066 6972 7374 2e0a 2020 2020  d at first..    
+00018fd0: 2020 2020 466f 7220 6578 616d 706c 652c      For example,
+00018fe0: 2069 6620 7468 6520 7065 7263 656e 7469   if the percenti
+00018ff0: 6c65 2069 7320 6035 2560 2061 6e64 2074  le is `5%` and t
+00019000: 6865 2067 6169 6e20 7661 6c75 6520 6973  he gain value is
+00019010: 2060 302e 3360 2c20 7765 2063 616e 2073   `0.3`, we can s
+00019020: 6179 2074 6861 7420 6966 2077 6520 7261  ay that if we ra
+00019030: 6e64 6f6d 6c79 0a20 2020 2020 2020 2073  ndomly.        s
+00019040: 6561 7263 6865 6420 6035 2560 206f 6620  earched `5%` of 
+00019050: 7468 6520 6461 7461 2c20 7765 2077 6f75  the data, we wou
+00019060: 6c64 2065 7870 6563 7420 746f 2075 6e63  ld expect to unc
+00019070: 6f76 6572 2061 626f 7574 2060 3525 6020  over about `5%` 
+00019080: 6f66 2074 6865 2070 6f73 6974 6976 6520  of the positive 
+00019090: 6576 656e 7473 3b0a 2020 2020 2020 2020  events;.        
+000190a0: 686f 7765 7665 722c 2077 6520 6861 7665  however, we have
+000190b0: 2075 6e63 6f76 6572 6564 2033 3025 206f   uncovered 30% o
+000190c0: 6620 6576 656e 7473 2062 7920 7365 6172  f events by sear
+000190d0: 6368 696e 6720 7468 6520 6869 6768 6573  ching the highes
+000190e0: 7420 3525 206f 6620 7363 6f72 6573 2e0a  t 5% of scores..
+000190f0: 2020 2020 2020 2020 4c69 6674 2069 7320          Lift is 
+00019100: 7369 6d70 6c79 2074 6865 2072 6174 696f  simply the ratio
+00019110: 206f 6620 7468 6520 7065 7263 656e 7420   of the percent 
+00019120: 6f66 2065 7665 6e74 7320 7468 6174 2077  of events that w
+00019130: 6861 7420 7765 2068 6176 6520 756e 636f  hat we have unco
+00019140: 7665 7265 6420 666f 7220 6120 6769 7665  vered for a give
+00019150: 6e20 7065 7263 656e 7469 6c65 0a20 2020  n percentile.   
+00019160: 2020 2020 206f 6620 6461 7461 2028 692e       of data (i.
+00019170: 652e 2067 6169 6e29 2064 6976 6964 6564  e. gain) divided
+00019180: 2062 7920 7768 6174 2077 6520 776f 756c   by what we woul
+00019190: 6420 6861 7665 2065 7870 6563 7465 6420  d have expected 
+000191a0: 6279 2072 616e 646f 6d20 6368 616e 6365  by random chance
+000191b0: 2028 692e 652e 2074 6865 2070 6572 6365   (i.e. the perce
+000191c0: 6e74 696c 6529 2e0a 2020 2020 2020 2020  ntile)..        
+000191d0: 536f 2069 6e20 7468 6520 7072 6576 696f  So in the previo
+000191e0: 7573 2065 7861 6d70 6c65 2c20 7765 2075  us example, we u
+000191f0: 6e63 6f76 6572 6564 2033 3025 206f 6620  ncovered 30% of 
+00019200: 706f 7369 7469 7665 2065 7665 6e74 7320  positive events 
+00019210: 6279 2073 6561 7263 6869 6e67 2074 6865  by searching the
+00019220: 2074 6f70 2035 2520 6f66 2073 636f 7265   top 5% of score
+00019230: 733b 0a20 2020 2020 2020 2077 6865 7265  s;.        where
+00019240: 6173 2069 6620 7765 2074 6f6f 6b20 6120  as if we took a 
+00019250: 7261 6e64 6f6d 2073 616d 706c 652c 2077  random sample, w
+00019260: 6520 776f 756c 6420 6861 7665 206f 6e6c  e would have onl
+00019270: 7920 6578 7065 6374 6564 2074 6f20 6669  y expected to fi
+00019280: 6e64 2035 2520 6f66 2074 6865 2070 6f73  nd 5% of the pos
+00019290: 6974 6976 6520 6576 656e 7473 2e0a 2020  itive events..  
+000192a0: 2020 2020 2020 5468 6520 6c69 6674 2069        The lift i
+000192b0: 7320 6030 2e33 202f 2030 2e30 3560 2077  s `0.3 / 0.05` w
+000192c0: 6869 6368 2069 7320 6036 603b 206d 6561  hich is `6`; mea
+000192d0: 6e69 6e67 2077 6520 666f 756e 6420 6036  ning we found `6
+000192e0: 6020 7469 6d65 7320 7468 6520 616d 6f75  ` times the amou
+000192f0: 6e74 206f 6620 706f 7369 7469 7665 2065  nt of positive e
+00019300: 7665 6e74 7320 6279 0a20 2020 2020 2020  vents by.       
+00019310: 2073 6561 7263 6869 6e67 2074 6865 2074   searching the t
+00019320: 6f70 2035 2520 6f66 2073 636f 7265 732c  op 5% of scores,
+00019330: 2074 6861 6e20 6966 2077 6520 7765 7265   than if we were
+00019340: 2074 6f20 7261 6e64 6f6d 6c79 2073 616d   to randomly sam
+00019350: 706c 6520 7468 6520 6461 7461 2e0a 2020  ple the data..  
+00019360: 2020 2020 2020 2222 220a 2020 2020 2020        """.      
+00019370: 2020 6461 7461 203d 2070 642e 4461 7461    data = pd.Data
+00019380: 4672 616d 6528 7b0a 2020 2020 2020 2020  Frame({.        
+00019390: 2020 2020 2770 7265 6469 6374 6564 5f73      'predicted_s
+000193a0: 636f 7265 7327 3a20 7365 6c66 2e5f 7072  cores': self._pr
+000193b0: 6564 6963 7465 645f 7363 6f72 6573 2c0a  edicted_scores,.
+000193c0: 2020 2020 2020 2020 2020 2020 2761 6374              'act
+000193d0: 7561 6c5f 7661 6c75 6573 273a 2073 656c  ual_values': sel
+000193e0: 662e 5f61 6374 7561 6c5f 7661 6c75 6573  f._actual_values
+000193f0: 2c0a 2020 2020 2020 2020 7d29 0a20 2020  ,.        }).   
+00019400: 2020 2020 2064 6174 612e 736f 7274 5f76       data.sort_v
+00019410: 616c 7565 7328 5b27 7072 6564 6963 7465  alues(['predicte
+00019420: 645f 7363 6f72 6573 275d 2c20 6173 6365  d_scores'], asce
+00019430: 6e64 696e 673d 4661 6c73 652c 2069 6e70  nding=False, inp
+00019440: 6c61 6365 3d54 7275 6529 0a0a 2020 2020  lace=True)..    
+00019450: 2020 2020 2320 2e71 6375 7420 6765 7473      # .qcut gets
+00019460: 2070 6572 6365 6e74 696c 6573 0a20 2020   percentiles.   
+00019470: 2020 2020 2062 696e 7320 3d20 7064 2e71       bins = pd.q
+00019480: 6375 7428 783d 6461 7461 5b27 7072 6564  cut(x=data['pred
+00019490: 6963 7465 645f 7363 6f72 6573 275d 2c0a  icted_scores'],.
+000194a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+000194b0: 2020 2020 2020 2071 3d6e 756d 5f62 7563         q=num_buc
+000194c0: 6b65 7473 2c0a 2020 2020 2020 2020 2020  kets,.          
+000194d0: 2020 2020 2020 2020 2020 2020 206c 6162               lab
+000194e0: 656c 733d 6c69 7374 2872 616e 6765 2831  els=list(range(1
+000194f0: 3030 2c20 302c 2072 6f75 6e64 282d 3130  00, 0, round(-10
+00019500: 3020 2f20 6e75 6d5f 6275 636b 6574 7329  0 / num_buckets)
+00019510: 2929 290a 0a20 2020 2020 2020 2064 6174  )))..        dat
+00019520: 615b 2750 6572 6365 6e74 696c 6527 5d20  a['Percentile'] 
+00019530: 3d20 6269 6e73 0a0a 2020 2020 2020 2020  = bins..        
+00019540: 6465 6620 6761 696e 5f67 726f 7570 696e  def gain_groupin
+00019550: 6728 6772 6f75 7029 3a0a 2020 2020 2020  g(group):.      
+00019560: 2020 2020 2020 7265 7375 6c74 7320 3d20        results = 
+00019570: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
+00019580: 2020 2723 206f 6620 4f62 732e 273a 206c    '# of Obs.': l
+00019590: 656e 2867 726f 7570 2e61 6374 7561 6c5f  en(group.actual_
+000195a0: 7661 6c75 6573 292c 0a20 2020 2020 2020  values),.       
+000195b0: 2020 2020 2020 2020 2027 2320 6f66 2050           '# of P
+000195c0: 6f73 2e20 4576 656e 7473 273a 2073 756d  os. Events': sum
+000195d0: 2867 726f 7570 2e61 6374 7561 6c5f 7661  (group.actual_va
+000195e0: 6c75 6573 203d 3d20 3129 0a20 2020 2020  lues == 1).     
+000195f0: 2020 2020 2020 207d 0a20 2020 2020 2020         }.       
+00019600: 2020 2020 2072 6574 7572 6e20 7064 2e53       return pd.S
+00019610: 6572 6965 7328 7265 7375 6c74 732c 2069  eries(results, i
+00019620: 6e64 6578 3d5b 2723 206f 6620 4f62 732e  ndex=['# of Obs.
+00019630: 272c 2027 2320 6f66 2050 6f73 2e20 4576  ', '# of Pos. Ev
+00019640: 656e 7473 275d 290a 0a20 2020 2020 2020  ents'])..       
+00019650: 2067 6169 6e5f 6c69 6674 5f64 6174 6120   gain_lift_data 
+00019660: 3d20 6461 7461 2e67 726f 7570 6279 2827  = data.groupby('
+00019670: 5065 7263 656e 7469 6c65 2729 2e61 7070  Percentile').app
+00019680: 6c79 2867 6169 6e5f 6772 6f75 7069 6e67  ly(gain_grouping
+00019690: 290a 2020 2020 2020 2020 7465 6d70 203d  ).        temp =
+000196a0: 2070 642e 4461 7461 4672 616d 6528 7b27   pd.DataFrame({'
+000196b0: 2320 6f66 204f 6273 2e27 3a20 302c 2027  # of Obs.': 0, '
+000196c0: 2320 6f66 2050 6f73 2e20 4576 656e 7473  # of Pos. Events
+000196d0: 273a 2030 7d2c 2069 6e64 6578 3d5b 305d  ': 0}, index=[0]
+000196e0: 290a 2020 2020 2020 2020 7465 6d70 2e69  ).        temp.i
+000196f0: 6e64 6578 2e6e 616d 6573 203d 205b 2750  ndex.names = ['P
+00019700: 6572 6365 6e74 696c 6527 5d0a 2020 2020  ercentile'].    
+00019710: 2020 2020 6761 696e 5f6c 6966 745f 6461      gain_lift_da
+00019720: 7461 203d 2070 642e 636f 6e63 6174 285b  ta = pd.concat([
+00019730: 6761 696e 5f6c 6966 745f 6461 7461 2c20  gain_lift_data, 
+00019740: 7465 6d70 5d29 0a20 2020 2020 2020 2067  temp]).        g
+00019750: 6169 6e5f 6c69 6674 5f64 6174 612e 736f  ain_lift_data.so
+00019760: 7274 5f69 6e64 6578 2861 7363 656e 6469  rt_index(ascendi
+00019770: 6e67 3d54 7275 652c 2069 6e70 6c61 6365  ng=True, inplace
+00019780: 3d54 7275 6529 0a0a 2020 2020 2020 2020  =True)..        
+00019790: 6761 696e 5f6c 6966 745f 6461 7461 5b27  gain_lift_data['
+000197a0: 4375 6d75 6c2e 2050 6f73 2e20 4576 656e  Cumul. Pos. Even
+000197b0: 7473 275d 203d 2067 6169 6e5f 6c69 6674  ts'] = gain_lift
+000197c0: 5f64 6174 615b 2723 206f 6620 506f 732e  _data['# of Pos.
+000197d0: 2045 7665 6e74 7327 5d2e 6375 6d73 756d   Events'].cumsum
+000197e0: 2829 0a20 2020 2020 2020 2067 6169 6e5f  ().        gain_
+000197f0: 6c69 6674 5f64 6174 615b 2747 6169 6e27  lift_data['Gain'
+00019800: 5d20 3d20 6761 696e 5f6c 6966 745f 6461  ] = gain_lift_da
+00019810: 7461 5b27 4375 6d75 6c2e 2050 6f73 2e20  ta['Cumul. Pos. 
+00019820: 4576 656e 7473 275d 202f 2073 656c 662e  Events'] / self.
+00019830: 5f61 6374 7561 6c5f 706f 7369 7469 7665  _actual_positive
+00019840: 730a 2020 2020 2020 2020 6761 696e 5f6c  s.        gain_l
+00019850: 6966 745f 6461 7461 203d 2067 6169 6e5f  ift_data = gain_
+00019860: 6c69 6674 5f64 6174 612e 6c6f 635b 7e28  lift_data.loc[~(
+00019870: 6761 696e 5f6c 6966 745f 6461 7461 2e69  gain_lift_data.i
+00019880: 6e64 6578 203d 3d20 3029 2c20 3a5d 0a20  ndex == 0), :]. 
+00019890: 2020 2020 2020 2067 6169 6e5f 6c69 6674         gain_lift
+000198a0: 5f64 6174 615b 274c 6966 7427 5d20 3d20  _data['Lift'] = 
+000198b0: 6761 696e 5f6c 6966 745f 6461 7461 5b27  gain_lift_data['
+000198c0: 4761 696e 275d 202f 2028 6761 696e 5f6c  Gain'] / (gain_l
+000198d0: 6966 745f 6461 7461 2e69 6e64 6578 2e76  ift_data.index.v
+000198e0: 616c 7565 7320 2f20 3130 3029 0a0a 2020  alues / 100)..  
+000198f0: 2020 2020 2020 6966 206e 6f74 2069 6e63        if not inc
+00019900: 6c75 6465 5f61 6c6c 5f69 6e66 6f3a 0a20  lude_all_info:. 
+00019910: 2020 2020 2020 2020 2020 2067 6169 6e5f             gain_
+00019920: 6c69 6674 5f64 6174 6120 3d20 6761 696e  lift_data = gain
+00019930: 5f6c 6966 745f 6461 7461 5b5b 2747 6169  _lift_data[['Gai
+00019940: 6e27 2c20 274c 6966 7427 5d5d 0a0a 2020  n', 'Lift']]..  
+00019950: 2020 2020 2020 6761 696e 5f6c 6966 745f        gain_lift_
+00019960: 6461 7461 203d 2067 6169 6e5f 6c69 6674  data = gain_lift
+00019970: 5f64 6174 612e 726f 756e 6428 3229 0a0a  _data.round(2)..
+00019980: 2020 2020 2020 2020 6966 2072 6574 7572          if retur
+00019990: 6e5f 7374 796c 653a 0a20 2020 2020 2020  n_style:.       
+000199a0: 2020 2020 2067 6169 6e5f 6c69 6674 5f64       gain_lift_d
+000199b0: 6174 6120 3d20 6761 696e 5f6c 6966 745f  ata = gain_lift_
+000199c0: 6461 7461 2e73 7479 6c65 0a20 2020 2020  data.style.     
+000199d0: 2020 2020 2020 2067 6169 6e5f 6c69 6674         gain_lift
+000199e0: 5f64 6174 612e 666f 726d 6174 2870 7265  _data.format(pre
+000199f0: 6369 7369 6f6e 3d32 292e 205c 0a20 2020  cision=2). \.   
+00019a00: 2020 2020 2020 2020 2020 2020 2062 6172               bar
+00019a10: 2873 7562 7365 743d 2747 6169 6e27 2c20  (subset='Gain', 
+00019a20: 636f 6c6f 723d 6863 6f6c 6f72 2e43 6f6c  color=hcolor.Col
+00019a30: 6f72 732e 5041 5354 454c 5f42 4c55 452e  ors.PASTEL_BLUE.
+00019a40: 7661 6c75 652c 0a20 2020 2020 2020 2020  value,.         
+00019a50: 2020 2020 2020 2020 2020 2076 6d69 6e3d             vmin=
+00019a60: 302c 2076 6d61 783d 3129 2e20 5c0a 2020  0, vmax=1). \.  
+00019a70: 2020 2020 2020 2020 2020 2020 2020 6261                ba
+00019a80: 7228 7375 6273 6574 3d27 4c69 6674 272c  r(subset='Lift',
+00019a90: 2063 6f6c 6f72 3d68 636f 6c6f 722e 436f   color=hcolor.Co
+00019aa0: 6c6f 7273 2e50 4153 5445 4c5f 424c 5545  lors.PASTEL_BLUE
+00019ab0: 2e76 616c 7565 290a 0a20 2020 2020 2020  .value)..       
+00019ac0: 2072 6574 7572 6e20 6761 696e 5f6c 6966   return gain_lif
+00019ad0: 745f 6461 7461 0a0a 2020 2020 2320 7079  t_data..    # py
+00019ae0: 6c69 6e74 3a20 6469 7361 626c 653d 696e  lint: disable=in
+00019af0: 636f 6e73 6973 7465 6e74 2d72 6574 7572  consistent-retur
+00019b00: 6e2d 7374 6174 656d 656e 7473 0a20 2020  n-statements.   
+00019b10: 2064 6566 2070 6c6f 745f 7072 6564 6963   def plot_predic
+00019b20: 7465 645f 7363 6f72 6573 5f68 6973 746f  ted_scores_histo
+00019b30: 6772 616d 2873 656c 6629 3a0a 2020 2020  gram(self):.    
+00019b40: 2020 2020 2222 2252 6574 7572 6e20 6120      """Return a 
+00019b50: 6869 7374 6f67 7261 6d20 6f66 2074 6865  histogram of the
+00019b60: 2070 7265 6469 6374 6564 2073 636f 7265   predicted score
+00019b70: 7322 2222 0a20 2020 2020 2020 2073 6e73  s""".        sns
+00019b80: 2e68 6973 7470 6c6f 7428 7365 6c66 2e5f  .histplot(self._
+00019b90: 7072 6564 6963 7465 645f 7363 6f72 6573  predicted_scores
+00019ba0: 290a 2020 2020 2020 2020 706c 742e 7469  ).        plt.ti
+00019bb0: 6768 745f 6c61 796f 7574 2829 0a0a 2020  ght_layout()..  
+00019bc0: 2020 2320 7079 6c69 6e74 3a20 6469 7361    # pylint: disa
+00019bd0: 626c 653d 696e 636f 6e73 6973 7465 6e74  ble=inconsistent
+00019be0: 2d72 6574 7572 6e2d 7374 6174 656d 656e  -return-statemen
+00019bf0: 7473 0a20 2020 2064 6566 2070 6c6f 745f  ts.    def plot_
+00019c00: 6163 7475 616c 5f76 735f 7072 6564 6963  actual_vs_predic
+00019c10: 745f 6869 7374 6f67 7261 6d28 7365 6c66  t_histogram(self
+00019c20: 293a 0a20 2020 2020 2020 2022 2222 5265  ):.        """Re
+00019c30: 7475 726e 2061 2068 6973 746f 6772 616d  turn a histogram
+00019c40: 206f 6620 7468 6520 6163 7475 616c 2076   of the actual v
+00019c50: 7320 7072 6564 6963 7465 6420 7363 6f72  s predicted scor
+00019c60: 6573 2222 220a 2020 2020 2020 2020 6163  es""".        ac
+00019c70: 7475 616c 5f63 6174 6567 6f72 6965 7320  tual_categories 
+00019c80: 3d20 7064 2e53 6572 6965 7328 7365 6c66  = pd.Series(self
+00019c90: 2e5f 6163 7475 616c 5f76 616c 7565 7329  ._actual_values)
+00019ca0: 2e5c 0a20 2020 2020 2020 2020 2020 2072  .\.            r
+00019cb0: 6570 6c61 6365 287b 303a 2073 656c 662e  eplace({0: self.
+00019cc0: 5f6e 6567 6174 6976 655f 636c 6173 732c  _negative_class,
+00019cd0: 2031 3a20 7365 6c66 2e5f 706f 7369 7469   1: self._positi
+00019ce0: 7665 5f63 6c61 7373 7d29 0a20 2020 2020  ve_class}).     
+00019cf0: 2020 2061 7865 7320 3d20 736e 732e 6469     axes = sns.di
+00019d00: 7370 6c6f 7428 0a20 2020 2020 2020 2020  splot(.         
+00019d10: 2020 2070 642e 4461 7461 4672 616d 6528     pd.DataFrame(
+00019d20: 7b0a 2020 2020 2020 2020 2020 2020 2020  {.              
+00019d30: 2020 2750 7265 6469 6374 6564 2053 636f    'Predicted Sco
+00019d40: 7265 273a 2073 656c 662e 5f70 7265 6469  re': self._predi
+00019d50: 6374 6564 5f73 636f 7265 732c 0a20 2020  cted_scores,.   
+00019d60: 2020 2020 2020 2020 2020 2020 2027 4163               'Ac
+00019d70: 7475 616c 2056 616c 7565 273a 2061 6374  tual Value': act
+00019d80: 7561 6c5f 6361 7465 676f 7269 6573 0a20  ual_categories. 
+00019d90: 2020 2020 2020 2020 2020 207d 292c 0a20             }),. 
+00019da0: 2020 2020 2020 2020 2020 2078 3d27 5072             x='Pr
+00019db0: 6564 6963 7465 6420 5363 6f72 6527 2c0a  edicted Score',.
+00019dc0: 2020 2020 2020 2020 2020 2020 636f 6c3d              col=
+00019dd0: 2741 6374 7561 6c20 5661 6c75 6527 0a20  'Actual Value'. 
+00019de0: 2020 2020 2020 2029 0a20 2020 2020 2020         ).       
+00019df0: 2066 6f72 2061 7869 7320 696e 2061 7865   for axis in axe
+00019e00: 732e 6178 6573 2e66 6c61 743a 0a20 2020  s.axes.flat:.   
+00019e10: 2020 2020 2020 2020 2061 7869 732e 6178           axis.ax
+00019e20: 766c 696e 6528 783d 302e 352c 2079 6d69  vline(x=0.5, ymi
+00019e30: 6e3d 302c 2079 6d61 783d 3130 302c 2063  n=0, ymax=100, c
+00019e40: 6f6c 6f72 3d27 7265 6427 290a 2020 2020  olor='red').    
+00019e50: 2020 2020 706c 742e 7469 6768 745f 6c61      plt.tight_la
+00019e60: 796f 7574 2829 0a0a 0a63 6c61 7373 2052  yout()...class R
+00019e70: 6567 7265 7373 696f 6e45 7661 6c75 6174  egressionEvaluat
+00019e80: 6f72 3a0a 2020 2020 2222 220a 2020 2020  or:.    """.    
+00019e90: 4576 616c 7561 7465 7320 6d6f 6465 6c73  Evaluates models
+00019ea0: 2066 6f72 2072 6567 7265 7373 696f 6e20   for regression 
+00019eb0: 2869 2e65 2e20 6e75 6d65 7269 6320 6f75  (i.e. numeric ou
+00019ec0: 7463 6f6d 6529 2070 726f 626c 656d 732e  tcome) problems.
+00019ed0: 0a20 2020 2022 2222 0a20 2020 2064 6566  .    """.    def
+00019ee0: 205f 5f69 6e69 745f 5f28 7365 6c66 2c0a   __init__(self,.
+00019ef0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+00019f00: 2061 6374 7561 6c5f 7661 6c75 6573 3a20   actual_values: 
+00019f10: 6e70 2e6e 6461 7272 6179 2c0a 2020 2020  np.ndarray,.    
+00019f20: 2020 2020 2020 2020 2020 2020 2070 7265               pre
+00019f30: 6469 6374 6564 5f76 616c 7565 733a 206e  dicted_values: n
+00019f40: 702e 6e64 6172 7261 7929 3a0a 2020 2020  p.ndarray):.    
+00019f50: 2020 2020 2222 220a 2020 2020 2020 2020      """.        
+00019f60: 4172 6773 3a0a 2020 2020 2020 2020 2020  Args:.          
+00019f70: 2020 6163 7475 616c 5f76 616c 7565 733a    actual_values:
+00019f80: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00019f90: 2074 6865 2061 6374 7561 6c20 7661 6c75   the actual valu
+00019fa0: 6573 0a20 2020 2020 2020 2020 2020 2070  es.            p
+00019fb0: 7265 6469 6374 6564 5f76 616c 7565 733a  redicted_values:
+00019fc0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+00019fd0: 2074 6865 2070 7265 6469 6374 6564 2076   the predicted v
+00019fe0: 616c 7565 730a 2020 2020 2020 2020 2222  alues.        ""
+00019ff0: 220a 0a20 2020 2020 2020 2061 7373 6572  "..        asser
+0001a000: 7420 6c65 6e28 6163 7475 616c 5f76 616c  t len(actual_val
+0001a010: 7565 7329 203d 3d20 6c65 6e28 7072 6564  ues) == len(pred
+0001a020: 6963 7465 645f 7661 6c75 6573 290a 0a20  icted_values).. 
+0001a030: 2020 2020 2020 2073 656c 662e 5f61 6374         self._act
+0001a040: 7561 6c5f 7661 6c75 6573 203d 2061 6374  ual_values = act
+0001a050: 7561 6c5f 7661 6c75 6573 0a20 2020 2020  ual_values.     
+0001a060: 2020 2073 656c 662e 5f70 7265 6469 6374     self._predict
+0001a070: 6564 5f76 616c 7565 7320 3d20 7072 6564  ed_values = pred
+0001a080: 6963 7465 645f 7661 6c75 6573 0a20 2020  icted_values.   
+0001a090: 2020 2020 2073 656c 662e 5f72 6573 6964       self._resid
+0001a0a0: 7561 6c73 203d 2061 6374 7561 6c5f 7661  uals = actual_va
+0001a0b0: 6c75 6573 202d 2070 7265 6469 6374 6564  lues - predicted
+0001a0c0: 5f76 616c 7565 730a 2020 2020 2020 2020  _values.        
+0001a0d0: 7365 6c66 2e5f 7374 616e 6461 7264 5f64  self._standard_d
+0001a0e0: 6576 6961 7469 6f6e 203d 206e 702e 7374  eviation = np.st
+0001a0f0: 6428 6163 7475 616c 5f76 616c 7565 7329  d(actual_values)
+0001a100: 0a20 2020 2020 2020 2073 656c 662e 5f6d  .        self._m
+0001a110: 6561 6e5f 7371 7561 7265 645f 6572 726f  ean_squared_erro
+0001a120: 7220 3d20 666c 6f61 7428 6e70 2e6d 6561  r = float(np.mea
+0001a130: 6e28 6e70 2e73 7175 6172 6528 6163 7475  n(np.square(actu
+0001a140: 616c 5f76 616c 7565 7320 2d20 7072 6564  al_values - pred
+0001a150: 6963 7465 645f 7661 6c75 6573 2929 290a  icted_values))).
+0001a160: 2020 2020 2020 2020 7365 6c66 2e5f 6d65          self._me
+0001a170: 616e 5f61 6273 6f6c 7574 655f 6572 726f  an_absolute_erro
+0001a180: 7220 3d20 666c 6f61 7428 6e70 2e6d 6561  r = float(np.mea
+0001a190: 6e28 6e70 2e61 6273 2861 6374 7561 6c5f  n(np.abs(actual_
+0001a1a0: 7661 6c75 6573 202d 2070 7265 6469 6374  values - predict
+0001a1b0: 6564 5f76 616c 7565 7329 2929 0a20 2020  ed_values))).   
+0001a1c0: 2020 2020 2073 656c 662e 5f72 5f73 7175       self._r_squ
+0001a1d0: 6172 6564 203d 2072 325f 7363 6f72 6528  ared = r2_score(
+0001a1e0: 795f 7472 7565 3d61 6374 7561 6c5f 7661  y_true=actual_va
+0001a1f0: 6c75 6573 2c20 795f 7072 6564 3d70 7265  lues, y_pred=pre
+0001a200: 6469 6374 6564 5f76 616c 7565 7329 0a0a  dicted_values)..
+0001a210: 2020 2020 4070 726f 7065 7274 790a 2020      @property.  
+0001a220: 2020 6465 6620 6d65 616e 5f61 6273 6f6c    def mean_absol
+0001a230: 7574 655f 6572 726f 7228 7365 6c66 2920  ute_error(self) 
+0001a240: 2d3e 2066 6c6f 6174 3a0a 2020 2020 2020  -> float:.      
+0001a250: 2020 2222 224d 6561 6e20 4162 736f 6c75    """Mean Absolu
+0001a260: 7465 2045 7272 6f72 2222 220a 2020 2020  te Error""".    
+0001a270: 2020 2020 7265 7475 726e 2073 656c 662e      return self.
+0001a280: 5f6d 6561 6e5f 6162 736f 6c75 7465 5f65  _mean_absolute_e
+0001a290: 7272 6f72 0a0a 2020 2020 4070 726f 7065  rror..    @prope
+0001a2a0: 7274 790a 2020 2020 6465 6620 6d65 616e  rty.    def mean
+0001a2b0: 5f73 7175 6172 6564 5f65 7272 6f72 2873  _squared_error(s
+0001a2c0: 656c 6629 202d 3e20 666c 6f61 743a 0a20  elf) -> float:. 
+0001a2d0: 2020 2020 2020 2022 2222 4d65 616e 2053         """Mean S
+0001a2e0: 7175 6172 6564 2045 7272 6f72 2222 220a  quared Error""".
+0001a2f0: 2020 2020 2020 2020 7265 7475 726e 2073          return s
+0001a300: 656c 662e 5f6d 6561 6e5f 7371 7561 7265  elf._mean_square
+0001a310: 645f 6572 726f 720a 0a20 2020 2040 7072  d_error..    @pr
+0001a320: 6f70 6572 7479 0a20 2020 2064 6566 2072  operty.    def r
+0001a330: 6f6f 745f 6d65 616e 5f73 7175 6172 6564  oot_mean_squared
+0001a340: 5f65 7272 6f72 2873 656c 6629 202d 3e20  _error(self) -> 
+0001a350: 666c 6f61 743a 0a20 2020 2020 2020 2022  float:.        "
+0001a360: 2222 526f 6f74 204d 6561 6e20 5371 7561  ""Root Mean Squa
+0001a370: 7265 6420 4572 726f 7222 2222 0a20 2020  red Error""".   
+0001a380: 2020 2020 2072 6574 7572 6e20 6e70 2e73       return np.s
+0001a390: 7172 7428 7365 6c66 2e6d 6561 6e5f 7371  qrt(self.mean_sq
+0001a3a0: 7561 7265 645f 6572 726f 7229 0a0a 2020  uared_error)..  
+0001a3b0: 2020 4070 726f 7065 7274 790a 2020 2020    @property.    
+0001a3c0: 6465 6620 726d 7365 5f74 6f5f 7374 5f64  def rmse_to_st_d
+0001a3d0: 6576 2873 656c 6629 202d 3e20 666c 6f61  ev(self) -> floa
+0001a3e0: 743a 0a20 2020 2020 2020 2022 2222 5468  t:.        """Th
+0001a3f0: 6520 7261 7469 6f20 6f66 2052 4d53 4520  e ratio of RMSE 
+0001a400: 746f 2074 6865 2073 7461 6e64 6172 6420  to the standard 
+0001a410: 6465 7669 6174 696f 6e20 6f66 2074 6865  deviation of the
+0001a420: 2061 6374 7561 6c20 7661 6c75 6573 2e0a   actual values..
+0001a430: 2020 2020 2020 2020 4769 7665 7320 616e          Gives an
+0001a440: 2069 6e64 6963 6174 696f 6e20 6f66 2068   indication of h
+0001a450: 6f77 206c 6172 6765 2074 6865 2065 7272  ow large the err
+0001a460: 6f72 7320 6172 6520 746f 2074 6865 2061  ors are to the a
+0001a470: 6374 7561 6c20 6461 7461 2e0a 2020 2020  ctual data..    
+0001a480: 2020 2020 2222 220a 2020 2020 2020 2020      """.        
+0001a490: 7265 7475 726e 2073 656c 662e 726f 6f74  return self.root
+0001a4a0: 5f6d 6561 6e5f 7371 7561 7265 645f 6572  _mean_squared_er
+0001a4b0: 726f 7220 2f20 7365 6c66 2e5f 7374 616e  ror / self._stan
+0001a4c0: 6461 7264 5f64 6576 6961 7469 6f6e 0a0a  dard_deviation..
+0001a4d0: 2020 2020 4070 726f 7065 7274 790a 2020      @property.  
+0001a4e0: 2020 6465 6620 725f 7371 7561 7265 6428    def r_squared(
+0001a4f0: 7365 6c66 2920 2d3e 2066 6c6f 6174 3a0a  self) -> float:.
+0001a500: 2020 2020 2020 2020 2222 2252 2053 7175          """R Squ
+0001a510: 6172 6564 2222 220a 2020 2020 2020 2020  ared""".        
+0001a520: 7265 7475 726e 2073 656c 662e 5f72 5f73  return self._r_s
+0001a530: 7175 6172 6564 0a0a 2020 2020 4070 726f  quared..    @pro
+0001a540: 7065 7274 790a 2020 2020 6465 6620 746f  perty.    def to
+0001a550: 7461 6c5f 6f62 7365 7276 6174 696f 6e73  tal_observations
+0001a560: 2873 656c 6629 3a0a 2020 2020 2020 2020  (self):.        
+0001a570: 2222 2254 6865 2074 6f74 616c 206e 756d  """The total num
+0001a580: 6265 7220 6f66 206f 6273 6572 7661 7469  ber of observati
+0001a590: 6f6e 7320 692e 652e 2073 616d 706c 6520  ons i.e. sample 
+0001a5a0: 7369 7a65 2e22 2222 0a20 2020 2020 2020  size.""".       
+0001a5b0: 2072 6574 7572 6e20 6c65 6e28 7365 6c66   return len(self
+0001a5c0: 2e5f 6163 7475 616c 5f76 616c 7565 7329  ._actual_values)
+0001a5d0: 0a0a 2020 2020 4070 726f 7065 7274 790a  ..    @property.
+0001a5e0: 2020 2020 6465 6620 616c 6c5f 6d65 7472      def all_metr
+0001a5f0: 6963 7328 7365 6c66 2920 2d3e 2064 6963  ics(self) -> dic
+0001a600: 743a 0a20 2020 2020 2020 2022 2222 5265  t:.        """Re
+0001a610: 7475 726e 7320 6120 6469 6374 696f 6e61  turns a dictiona
+0001a620: 7279 206f 6620 7468 6520 6d6f 7374 2063  ry of the most c
+0001a630: 6f6d 6d6f 6e20 6572 726f 7220 6d65 7472  ommon error metr
+0001a640: 6963 7320 666f 7220 7265 6772 6573 7369  ics for regressi
+0001a650: 6f6e 2070 726f 626c 656d 732e 2222 220a  on problems.""".
+0001a660: 2020 2020 2020 2020 7265 7475 726e 207b          return {
+0001a670: 274d 6561 6e20 4162 736f 6c75 7465 2045  'Mean Absolute E
+0001a680: 7272 6f72 2028 4d41 4529 273a 2073 656c  rror (MAE)': sel
+0001a690: 662e 6d65 616e 5f61 6273 6f6c 7574 655f  f.mean_absolute_
+0001a6a0: 6572 726f 722c 0a20 2020 2020 2020 2020  error,.         
+0001a6b0: 2020 2020 2020 2027 526f 6f74 204d 6561         'Root Mea
+0001a6c0: 6e20 5371 7561 7265 6420 4572 726f 7220  n Squared Error 
+0001a6d0: 2852 4d53 4529 273a 2073 656c 662e 726f  (RMSE)': self.ro
+0001a6e0: 6f74 5f6d 6561 6e5f 7371 7561 7265 645f  ot_mean_squared_
+0001a6f0: 6572 726f 722c 0a20 2020 2020 2020 2020  error,.         
+0001a700: 2020 2020 2020 2027 524d 5345 2074 6f20         'RMSE to 
+0001a710: 5374 616e 6461 7264 2044 6576 6961 7469  Standard Deviati
+0001a720: 6f6e 206f 6620 5461 7267 6574 273a 2073  on of Target': s
+0001a730: 656c 662e 726d 7365 5f74 6f5f 7374 5f64  elf.rmse_to_st_d
+0001a740: 6576 2c0a 2020 2020 2020 2020 2020 2020  ev,.            
+0001a750: 2020 2020 2752 2053 7175 6172 6564 273a      'R Squared':
+0001a760: 2073 656c 662e 725f 7371 7561 7265 642c   self.r_squared,
+0001a770: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001a780: 2027 546f 7461 6c20 4f62 7365 7276 6174   'Total Observat
+0001a790: 696f 6e73 273a 2073 656c 662e 746f 7461  ions': self.tota
+0001a7a0: 6c5f 6f62 7365 7276 6174 696f 6e73 7d0a  l_observations}.
+0001a7b0: 0a20 2020 2064 6566 2061 6c6c 5f6d 6574  .    def all_met
+0001a7c0: 7269 6373 5f64 6628 7365 6c66 2c0a 2020  rics_df(self,.  
+0001a7d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001a7e0: 2020 2020 2064 756d 6d79 5f72 6567 7265       dummy_regre
+0001a7f0: 7373 6f72 5f73 7472 6174 6567 793a 2055  ssor_strategy: U
+0001a800: 6e69 6f6e 5b73 7472 2c20 6c69 7374 2c20  nion[str, list, 
+0001a810: 4e6f 6e65 5d20 3d20 276d 6561 6e27 2c0a  None] = 'mean',.
+0001a820: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001a830: 2020 2020 2020 2064 756d 6d79 5f72 6567         dummy_reg
+0001a840: 7265 7373 6f72 5f63 6f6e 7374 616e 743a  ressor_constant:
+0001a850: 2055 6e69 6f6e 5b69 6e74 5d20 3d20 312c   Union[int] = 1,
+0001a860: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001a870: 2020 2020 2020 2020 7265 7475 726e 5f73          return_s
+0001a880: 7479 6c65 3a20 626f 6f6c 203d 2046 616c  tyle: bool = Fal
+0001a890: 7365 2c0a 2020 2020 2020 2020 2020 2020  se,.            
+0001a8a0: 2020 2020 2020 2020 2020 2072 6f75 6e64             round
+0001a8b0: 5f62 793a 204f 7074 696f 6e61 6c5b 696e  _by: Optional[in
+0001a8c0: 745d 203d 204e 6f6e 6529 202d 3e20 556e  t] = None) -> Un
+0001a8d0: 696f 6e5b 7064 2e44 6174 6146 7261 6d65  ion[pd.DataFrame
+0001a8e0: 2c20 5374 796c 6572 5d3a 0a20 2020 2020  , Styler]:.     
+0001a8f0: 2020 2022 2222 416c 6c20 6f66 2074 6865     """All of the
+0001a900: 206d 6574 7269 6373 2061 7265 2072 6574   metrics are ret
+0001a910: 7572 6e65 6420 6173 2061 2044 6174 6146  urned as a DataF
+0001a920: 7261 6d65 2e0a 0a20 2020 2020 2020 2041  rame...        A
+0001a930: 7267 733a 0a20 2020 2020 2020 2020 2020  rgs:.           
+0001a940: 2064 756d 6d79 5f72 6567 7265 7373 6f72   dummy_regressor
+0001a950: 5f73 7472 6174 6567 793a 0a20 2020 2020  _strategy:.     
+0001a960: 2020 2020 2020 2020 2020 2069 6620 6e6f             if no
+0001a970: 7420 4e6f 6e65 2c20 7468 656e 2072 6574  t None, then ret
+0001a980: 7572 6e73 2063 6f6c 756d 6e28 7329 2063  urns column(s) c
+0001a990: 6f72 7265 7370 6f6e 6469 6e67 2074 6f20  orresponding to 
+0001a9a0: 7468 6520 7363 6f72 6573 2066 726f 6d20  the scores from 
+0001a9b0: 7072 6564 6963 7469 6f6e 7320 6f66 0a20  predictions of. 
+0001a9c0: 2020 2020 2020 2020 2020 2020 2020 2073                 s
+0001a9d0: 6b6c 6561 726e 2e64 756d 6d79 2e44 756d  klearn.dummy.Dum
+0001a9e0: 6d79 5265 6772 6573 736f 722c 2062 6173  myRegressor, bas
+0001a9f0: 6564 206f 6e20 7468 6520 7374 7261 7465  ed on the strate
+0001aa00: 6779 2028 6f72 2073 7472 6174 6567 6965  gy (or strategie
+0001aa10: 7329 2070 726f 7669 6465 642e 2056 616c  s) provided. Val
+0001aa20: 6964 2076 616c 7565 730a 2020 2020 2020  id values.      
+0001aa30: 2020 2020 2020 2020 2020 636f 7272 6573            corres
+0001aa40: 706f 6e64 2074 6f20 7661 6c75 6573 206f  pond to values o
+0001aa50: 6620 6073 7472 6174 6567 7960 2070 6172  f `strategy` par
+0001aa60: 616d 6574 6572 206c 6973 7465 640a 2020  ameter listed.  
+0001aa70: 2020 2020 2020 2020 2020 2020 2020 6874                ht
+0001aa80: 7470 733a 2f2f 7363 696b 6974 2d6c 6561  tps://scikit-lea
+0001aa90: 726e 2e6f 7267 2f73 7461 626c 652f 6d6f  rn.org/stable/mo
+0001aaa0: 6475 6c65 732f 6765 6e65 7261 7465 642f  dules/generated/
+0001aab0: 736b 6c65 6172 6e2e 6475 6d6d 792e 4475  sklearn.dummy.Du
+0001aac0: 6d6d 7952 6567 7265 7373 6f72 2e68 746d  mmyRegressor.htm
+0001aad0: 6c0a 0a20 2020 2020 2020 2020 2020 2020  l..             
+0001aae0: 2020 2049 6620 6120 6c69 7374 2069 7320     If a list is 
+0001aaf0: 7061 7373 6564 2069 6e20 2865 2e67 2e20  passed in (e.g. 
+0001ab00: 5b27 7072 696f 7227 2c20 2775 6e69 666f  ['prior', 'unifo
+0001ab10: 726d 275d 2c20 7468 656e 206f 6e65 2073  rm'], then one s
+0001ab20: 636f 7265 2063 6f6c 756d 6e20 7065 7220  core column per 
+0001ab30: 7661 6c75 6520 6973 0a20 2020 2020 2020  value is.       
+0001ab40: 2020 2020 2020 2020 2061 6464 6564 2e0a           added..
+0001ab50: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001ab60: 2049 6620 4e6f 6e65 2069 7320 7061 7373   If None is pass
+0001ab70: 6564 2c20 7468 656e 206e 6f20 6164 6469  ed, then no addi
+0001ab80: 7469 6f6e 616c 2063 6f6c 756d 6e73 2061  tional columns a
+0001ab90: 7265 2061 6464 6564 2e0a 2020 2020 2020  re added..      
+0001aba0: 2020 2020 2020 6475 6d6d 795f 7265 6772        dummy_regr
+0001abb0: 6573 736f 725f 636f 6e73 7461 6e74 3a0a  essor_constant:.
+0001abc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001abd0: 5468 6520 6578 706c 6963 6974 2063 6f6e  The explicit con
+0001abe0: 7374 616e 7420 6173 2070 7265 6469 6374  stant as predict
+0001abf0: 6564 2062 7920 7468 6520 e280 9c63 6f6e  ed by the ...con
+0001ac00: 7374 616e 74e2 809d 2073 7472 6174 6567  stant... strateg
+0001ac10: 7920 666f 7220 7468 650a 2020 2020 2020  y for the.      
+0001ac20: 2020 2020 2020 2020 2020 4475 6d6d 7952            DummyR
+0001ac30: 6567 7265 7373 6f72 2e0a 2020 2020 2020  egressor..      
+0001ac40: 2020 2020 2020 2020 2020 5468 6973 2070            This p
+0001ac50: 6172 616d 6574 6572 2069 7320 7573 6566  arameter is usef
+0001ac60: 756c 206f 6e6c 7920 666f 7220 7468 6520  ul only for the 
+0001ac70: e280 9c63 6f6e 7374 616e 74e2 809d 2064  ...constant... d
+0001ac80: 756d 6d79 5f72 6567 7265 7373 6f72 5f73  ummy_regressor_s
+0001ac90: 7472 6174 6567 792e 0a20 2020 2020 2020  trategy..       
+0001aca0: 2020 2020 2072 6574 7572 6e5f 7374 796c       return_styl
+0001acb0: 653a 0a20 2020 2020 2020 2020 2020 2020  e:.             
+0001acc0: 2020 2069 6620 5472 7565 2c20 7265 7475     if True, retu
+0001acd0: 726e 2073 7479 6c65 7220 6f62 6a65 6374  rn styler object
+0001ace0: 3b20 656c 7365 2072 6574 7572 6e20 6461  ; else return da
+0001acf0: 7461 6672 616d 650a 2020 2020 2020 2020  taframe.        
+0001ad00: 2020 2020 726f 756e 645f 6279 3a0a 2020      round_by:.  
+0001ad10: 2020 2020 2020 2020 2020 2020 2020 7468                th
+0001ad20: 6520 6e75 6d62 6572 206f 6620 6469 6769  e number of digi
+0001ad30: 7473 2074 6f20 726f 756e 6420 6279 3b20  ts to round by; 
+0001ad40: 6966 204e 6f6e 652c 2074 6865 6e20 646f  if None, then do
+0001ad50: 6e27 7420 726f 756e 640a 2020 2020 2020  n't round.      
+0001ad60: 2020 2222 220a 2020 2020 2020 2020 7265    """.        re
+0001ad70: 7375 6c74 203d 2070 642e 4461 7461 4672  sult = pd.DataFr
+0001ad80: 616d 652e 6672 6f6d 5f64 6963 7428 7365  ame.from_dict(se
+0001ad90: 6c66 2e61 6c6c 5f6d 6574 7269 6373 2c20  lf.all_metrics, 
+0001ada0: 6f72 6965 6e74 3d27 696e 6465 7827 2c20  orient='index', 
+0001adb0: 636f 6c75 6d6e 733d 5b27 5363 6f72 6527  columns=['Score'
+0001adc0: 5d29 0a0a 2020 2020 2020 2020 7363 6f72  ])..        scor
+0001add0: 655f 636f 6c75 6d6e 7320 3d20 5b27 5363  e_columns = ['Sc
+0001ade0: 6f72 6527 5d0a 0a20 2020 2020 2020 2069  ore']..        i
+0001adf0: 6620 6475 6d6d 795f 7265 6772 6573 736f  f dummy_regresso
+0001ae00: 725f 7374 7261 7465 6779 3a0a 2020 2020  r_strategy:.    
+0001ae10: 2020 2020 2020 2020 6966 2069 7369 6e73          if isins
+0001ae20: 7461 6e63 6528 6475 6d6d 795f 7265 6772  tance(dummy_regr
+0001ae30: 6573 736f 725f 7374 7261 7465 6779 2c20  essor_strategy, 
+0001ae40: 7374 7229 3a0a 2020 2020 2020 2020 2020  str):.          
+0001ae50: 2020 2020 2020 6475 6d6d 795f 7265 6772        dummy_regr
+0001ae60: 6573 736f 725f 7374 7261 7465 6779 203d  essor_strategy =
+0001ae70: 205b 6475 6d6d 795f 7265 6772 6573 736f   [dummy_regresso
+0001ae80: 725f 7374 7261 7465 6779 5d0a 0a20 2020  r_strategy]..   
+0001ae90: 2020 2020 2020 2020 2066 6f72 2073 7472           for str
+0001aea0: 6174 6567 7920 696e 2064 756d 6d79 5f72  ategy in dummy_r
+0001aeb0: 6567 7265 7373 6f72 5f73 7472 6174 6567  egressor_strateg
+0001aec0: 793a 0a20 2020 2020 2020 2020 2020 2020  y:.             
+0001aed0: 2020 2064 756d 6d79 203d 2044 756d 6d79     dummy = Dummy
+0001aee0: 5265 6772 6573 736f 7228 7374 7261 7465  Regressor(strate
+0001aef0: 6779 3d73 7472 6174 6567 792c 2063 6f6e  gy=strategy, con
+0001af00: 7374 616e 743d 6475 6d6d 795f 7265 6772  stant=dummy_regr
+0001af10: 6573 736f 725f 636f 6e73 7461 6e74 290a  essor_constant).
+0001af20: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001af30: 2320 6874 7470 733a 2f2f 7363 696b 6974  # https://scikit
+0001af40: 2d6c 6561 726e 2e6f 7267 2f73 7461 626c  -learn.org/stabl
+0001af50: 652f 6d6f 6475 6c65 732f 6765 6e65 7261  e/modules/genera
+0001af60: 7465 642f 736b 6c65 6172 6e2e 6475 6d6d  ted/sklearn.dumm
+0001af70: 792e 4475 6d6d 7943 6c61 7373 6966 6965  y.DummyClassifie
+0001af80: 722e 6874 6d6c 0a20 2020 2020 2020 2020  r.html.         
+0001af90: 2020 2020 2020 2023 2022 416c 6c20 7374         # "All st
+0001afa0: 7261 7465 6769 6573 206d 616b 6520 7072  rategies make pr
+0001afb0: 6564 6963 7469 6f6e 7320 7468 6174 2069  edictions that i
+0001afc0: 676e 6f72 6520 7468 6520 696e 7075 7420  gnore the input 
+0001afd0: 6665 6174 7572 6520 7661 6c75 6573 2070  feature values p
+0001afe0: 6173 7365 6420 6173 2074 6865 2058 0a20  assed as the X. 
+0001aff0: 2020 2020 2020 2020 2020 2020 2020 2023                 #
+0001b000: 2061 7267 756d 656e 7420 746f 2066 6974   argument to fit
+0001b010: 2061 6e64 2070 7265 6469 6374 2e20 5468   and predict. Th
+0001b020: 6520 7072 6564 6963 7469 6f6e 732c 2068  e predictions, h
+0001b030: 6f77 6576 6572 2c20 7479 7069 6361 6c6c  owever, typicall
+0001b040: 7920 6465 7065 6e64 206f 6e20 7661 6c75  y depend on valu
+0001b050: 6573 206f 6273 6572 7665 640a 2020 2020  es observed.    
+0001b060: 2020 2020 2020 2020 2020 2020 2320 696e              # in
+0001b070: 2074 6865 2079 2070 6172 616d 6574 6572   the y parameter
+0001b080: 2070 6173 7365 6420 746f 2066 6974 2e22   passed to fit."
+0001b090: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001b0a0: 205f 203d 2064 756d 6d79 2e66 6974 2858   _ = dummy.fit(X
+0001b0b0: 3d73 656c 662e 5f61 6374 7561 6c5f 7661  =self._actual_va
+0001b0c0: 6c75 6573 2c20 793d 7365 6c66 2e5f 6163  lues, y=self._ac
+0001b0d0: 7475 616c 5f76 616c 7565 7329 0a20 2020  tual_values).   
+0001b0e0: 2020 2020 2020 2020 2020 2020 2064 756d               dum
+0001b0f0: 6d79 5f70 7265 6469 6374 696f 6e73 203d  my_predictions =
+0001b100: 2064 756d 6d79 2e70 7265 6469 6374 2858   dummy.predict(X
+0001b110: 3d73 656c 662e 5f61 6374 7561 6c5f 7661  =self._actual_va
+0001b120: 6c75 6573 290a 2020 2020 2020 2020 2020  lues).          
+0001b130: 2020 2020 2020 6475 6d6d 795f 6576 616c        dummy_eval
+0001b140: 7561 746f 7220 3d20 5265 6772 6573 7369  uator = Regressi
+0001b150: 6f6e 4576 616c 7561 746f 7228 6163 7475  onEvaluator(actu
+0001b160: 616c 5f76 616c 7565 733d 7365 6c66 2e5f  al_values=self._
+0001b170: 6163 7475 616c 5f76 616c 7565 732c 0a20  actual_values,. 
+0001b180: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b190: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b1a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b1b0: 2020 2020 2020 2020 2020 2070 7265 6469             predi
-0001b1c0: 6374 6564 5f76 616c 7565 733d 6475 6d6d  cted_values=dumm
-0001b1d0: 795f 7072 6564 6963 7469 6f6e 7329 0a0a  y_predictions)..
-0001b1e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b1f0: 6475 6d6d 795f 7363 6f72 6573 203d 2064  dummy_scores = d
-0001b200: 756d 6d79 5f65 7661 6c75 6174 6f72 2e61  ummy_evaluator.a
-0001b210: 6c6c 5f6d 6574 7269 6373 5f64 6628 6475  ll_metrics_df(du
-0001b220: 6d6d 795f 7265 6772 6573 736f 725f 7374  mmy_regressor_st
-0001b230: 7261 7465 6779 3d4e 6f6e 652c 0a20 2020  rategy=None,.   
+0001b1b0: 2020 2020 2070 7265 6469 6374 6564 5f76       predicted_v
+0001b1c0: 616c 7565 733d 6475 6d6d 795f 7072 6564  alues=dummy_pred
+0001b1d0: 6963 7469 6f6e 7329 0a0a 2020 2020 2020  ictions)..      
+0001b1e0: 2020 2020 2020 2020 2020 6475 6d6d 795f            dummy_
+0001b1f0: 7363 6f72 6573 203d 2064 756d 6d79 5f65  scores = dummy_e
+0001b200: 7661 6c75 6174 6f72 2e61 6c6c 5f6d 6574  valuator.all_met
+0001b210: 7269 6373 5f64 6628 6475 6d6d 795f 7265  rics_df(dummy_re
+0001b220: 6772 6573 736f 725f 7374 7261 7465 6779  gressor_strategy
+0001b230: 3d4e 6f6e 652c 0a20 2020 2020 2020 2020  =None,.         
 0001b240: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b250: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b260: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b270: 2020 2020 2020 2020 2020 2072 6574 7572             retur
-0001b280: 6e5f 7374 796c 653d 4661 6c73 6529 0a20  n_style=False). 
-0001b290: 2020 2020 2020 2020 2020 2020 2020 2063                 c
-0001b2a0: 6f6c 756d 6e5f 6e61 6d65 203d 2066 2244  olumn_name = f"D
-0001b2b0: 756d 6d79 2028 7b73 7472 6174 6567 797d  ummy ({strategy}
-0001b2c0: 2922 0a20 2020 2020 2020 2020 2020 2020  )".             
-0001b2d0: 2020 2073 636f 7265 5f63 6f6c 756d 6e73     score_columns
-0001b2e0: 203d 2073 636f 7265 5f63 6f6c 756d 6e73   = score_columns
-0001b2f0: 202b 205b 636f 6c75 6d6e 5f6e 616d 655d   + [column_name]
-0001b300: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001b310: 2064 756d 6d79 5f73 636f 7265 7320 3d20   dummy_scores = 
-0001b320: 6475 6d6d 795f 7363 6f72 6573 2e72 656e  dummy_scores.ren
-0001b330: 616d 6528 636f 6c75 6d6e 733d 7b27 5363  ame(columns={'Sc
-0001b340: 6f72 6527 3a20 636f 6c75 6d6e 5f6e 616d  ore': column_nam
-0001b350: 657d 290a 2020 2020 2020 2020 2020 2020  e}).            
-0001b360: 2020 2020 7265 7375 6c74 203d 2070 642e      result = pd.
-0001b370: 636f 6e63 6174 285b 7265 7375 6c74 2c20  concat([result, 
-0001b380: 6475 6d6d 795f 7363 6f72 6573 5d2c 2061  dummy_scores], a
-0001b390: 7869 733d 3129 0a0a 2020 2020 2020 2020  xis=1)..        
-0001b3a0: 6966 2072 6f75 6e64 5f62 7920 6973 206e  if round_by is n
-0001b3b0: 6f74 204e 6f6e 653a 0a20 2020 2020 2020  ot None:.       
-0001b3c0: 2020 2020 2072 6573 756c 742e 696c 6f63       result.iloc
-0001b3d0: 5b30 3a32 5d20 3d20 7265 7375 6c74 2e69  [0:2] = result.i
-0001b3e0: 6c6f 635b 303a 325d 2e72 6f75 6e64 2872  loc[0:2].round(r
-0001b3f0: 6f75 6e64 5f62 7929 0a0a 2020 2020 2020  ound_by)..      
-0001b400: 2020 6966 2072 6574 7572 6e5f 7374 796c    if return_styl
-0001b410: 653a 0a20 2020 2020 2020 2020 2020 2073  e:.            s
-0001b420: 7562 7365 745f 7363 6f72 6573 203d 2070  ubset_scores = p
-0001b430: 642e 496e 6465 7853 6c69 6365 5b72 6573  d.IndexSlice[res
-0001b440: 756c 742e 6c6f 635b 5b27 4d65 616e 2041  ult.loc[['Mean A
-0001b450: 6273 6f6c 7574 6520 4572 726f 7220 284d  bsolute Error (M
-0001b460: 4145 2927 2c0a 2020 2020 2020 2020 2020  AE)',.          
+0001b270: 2020 2020 2072 6574 7572 6e5f 7374 796c       return_styl
+0001b280: 653d 4661 6c73 6529 0a20 2020 2020 2020  e=False).       
+0001b290: 2020 2020 2020 2020 2063 6f6c 756d 6e5f           column_
+0001b2a0: 6e61 6d65 203d 2066 2244 756d 6d79 2028  name = f"Dummy (
+0001b2b0: 7b73 7472 6174 6567 797d 2922 0a20 2020  {strategy})".   
+0001b2c0: 2020 2020 2020 2020 2020 2020 2073 636f               sco
+0001b2d0: 7265 5f63 6f6c 756d 6e73 203d 2073 636f  re_columns = sco
+0001b2e0: 7265 5f63 6f6c 756d 6e73 202b 205b 636f  re_columns + [co
+0001b2f0: 6c75 6d6e 5f6e 616d 655d 0a20 2020 2020  lumn_name].     
+0001b300: 2020 2020 2020 2020 2020 2064 756d 6d79             dummy
+0001b310: 5f73 636f 7265 7320 3d20 6475 6d6d 795f  _scores = dummy_
+0001b320: 7363 6f72 6573 2e72 656e 616d 6528 636f  scores.rename(co
+0001b330: 6c75 6d6e 733d 7b27 5363 6f72 6527 3a20  lumns={'Score': 
+0001b340: 636f 6c75 6d6e 5f6e 616d 657d 290a 2020  column_name}).  
+0001b350: 2020 2020 2020 2020 2020 2020 2020 7265                re
+0001b360: 7375 6c74 203d 2070 642e 636f 6e63 6174  sult = pd.concat
+0001b370: 285b 7265 7375 6c74 2c20 6475 6d6d 795f  ([result, dummy_
+0001b380: 7363 6f72 6573 5d2c 2061 7869 733d 3129  scores], axis=1)
+0001b390: 0a0a 2020 2020 2020 2020 6966 2072 6f75  ..        if rou
+0001b3a0: 6e64 5f62 7920 6973 206e 6f74 204e 6f6e  nd_by is not Non
+0001b3b0: 653a 0a20 2020 2020 2020 2020 2020 2072  e:.            r
+0001b3c0: 6573 756c 742e 696c 6f63 5b30 3a32 5d20  esult.iloc[0:2] 
+0001b3d0: 3d20 7265 7375 6c74 2e69 6c6f 635b 303a  = result.iloc[0:
+0001b3e0: 325d 2e72 6f75 6e64 2872 6f75 6e64 5f62  2].round(round_b
+0001b3f0: 7929 0a0a 2020 2020 2020 2020 6966 2072  y)..        if r
+0001b400: 6574 7572 6e5f 7374 796c 653a 0a20 2020  eturn_style:.   
+0001b410: 2020 2020 2020 2020 2073 7562 7365 745f           subset_
+0001b420: 7363 6f72 6573 203d 2070 642e 496e 6465  scores = pd.Inde
+0001b430: 7853 6c69 6365 5b72 6573 756c 742e 6c6f  xSlice[result.lo
+0001b440: 635b 5b27 4d65 616e 2041 6273 6f6c 7574  c[['Mean Absolut
+0001b450: 6520 4572 726f 7220 284d 4145 2927 2c0a  e Error (MAE)',.
+0001b460: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b470: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b480: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b490: 2020 2020 2020 2020 2020 2020 2752 6f6f              'Roo
-0001b4a0: 7420 4d65 616e 2053 7175 6172 6564 2045  t Mean Squared E
-0001b4b0: 7272 6f72 2028 524d 5345 2927 5d2c 0a20  rror (RMSE)'],. 
+0001b490: 2020 2020 2020 2752 6f6f 7420 4d65 616e        'Root Mean
+0001b4a0: 2053 7175 6172 6564 2045 7272 6f72 2028   Squared Error (
+0001b4b0: 524d 5345 2927 5d2c 0a20 2020 2020 2020  RMSE)'],.       
 0001b4c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b4d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b4e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b4f0: 2020 2020 7363 6f72 655f 636f 6c75 6d6e      score_column
-0001b500: 735d 2e69 6e64 6578 2c0a 2020 2020 2020  s].index,.      
+0001b4e0: 2020 2020 2020 2020 2020 2020 2020 7363                sc
+0001b4f0: 6f72 655f 636f 6c75 6d6e 735d 2e69 6e64  ore_columns].ind
+0001b500: 6578 2c0a 2020 2020 2020 2020 2020 2020  ex,.            
 0001b510: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b520: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b530: 2020 2020 7363 6f72 655f 636f 6c75 6d6e      score_column
-0001b540: 735d 0a20 2020 2020 2020 2020 2020 2073  s].            s
-0001b550: 7562 7365 745f 7365 636f 6e64 6172 7920  ubset_secondary 
-0001b560: 3d20 7064 2e49 6e64 6578 536c 6963 655b  = pd.IndexSlice[
-0001b570: 7265 7375 6c74 2e6c 6f63 5b5b 2752 4d53  result.loc[['RMS
-0001b580: 4520 746f 2053 7461 6e64 6172 6420 4465  E to Standard De
-0001b590: 7669 6174 696f 6e20 6f66 2054 6172 6765  viation of Targe
-0001b5a0: 7427 2c0a 2020 2020 2020 2020 2020 2020  t',.            
+0001b520: 2020 2020 2020 2020 2020 2020 2020 7363                sc
+0001b530: 6f72 655f 636f 6c75 6d6e 735d 0a20 2020  ore_columns].   
+0001b540: 2020 2020 2020 2020 2073 7562 7365 745f           subset_
+0001b550: 7365 636f 6e64 6172 7920 3d20 7064 2e49  secondary = pd.I
+0001b560: 6e64 6578 536c 6963 655b 7265 7375 6c74  ndexSlice[result
+0001b570: 2e6c 6f63 5b5b 2752 4d53 4520 746f 2053  .loc[['RMSE to S
+0001b580: 7461 6e64 6172 6420 4465 7669 6174 696f  tandard Deviatio
+0001b590: 6e20 6f66 2054 6172 6765 7427 2c0a 2020  n of Target',.  
+0001b5a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b5b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b5c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b5d0: 2020 2020 2020 2020 2020 2020 2027 5220               'R 
-0001b5e0: 5371 7561 7265 6427 5d2c 0a20 2020 2020  Squared'],.     
+0001b5d0: 2020 2020 2020 2027 5220 5371 7561 7265         'R Square
+0001b5e0: 6427 5d2c 0a20 2020 2020 2020 2020 2020  d'],.           
 0001b5f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b600: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b610: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b620: 2020 2073 636f 7265 5f63 6f6c 756d 6e73     score_columns
-0001b630: 5d2e 696e 6465 782c 2073 636f 7265 5f63  ].index, score_c
-0001b640: 6f6c 756d 6e73 5d0a 2020 2020 2020 2020  olumns].        
-0001b650: 2020 2020 7375 6273 6574 5f74 6f74 616c      subset_total
-0001b660: 5f6f 6273 6572 7661 7469 6f6e 7320 3d20  _observations = 
-0001b670: 7064 2e49 6e64 6578 536c 6963 655b 7265  pd.IndexSlice[re
-0001b680: 7375 6c74 2e6c 6f63 5b5b 2754 6f74 616c  sult.loc[['Total
-0001b690: 204f 6273 6572 7661 7469 6f6e 7327 5d2c   Observations'],
-0001b6a0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001b610: 2020 2020 2020 2020 2020 2020 2073 636f               sco
+0001b620: 7265 5f63 6f6c 756d 6e73 5d2e 696e 6465  re_columns].inde
+0001b630: 782c 2073 636f 7265 5f63 6f6c 756d 6e73  x, score_columns
+0001b640: 5d0a 2020 2020 2020 2020 2020 2020 7375  ].            su
+0001b650: 6273 6574 5f74 6f74 616c 5f6f 6273 6572  bset_total_obser
+0001b660: 7661 7469 6f6e 7320 3d20 7064 2e49 6e64  vations = pd.Ind
+0001b670: 6578 536c 6963 655b 7265 7375 6c74 2e6c  exSlice[result.l
+0001b680: 6f63 5b5b 2754 6f74 616c 204f 6273 6572  oc[['Total Obser
+0001b690: 7661 7469 6f6e 7327 5d2c 0a20 2020 2020  vations'],.     
+0001b6a0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b6b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001b6c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b6d0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b6e0: 2020 7363 6f72 655f 636f 6c75 6d6e 735d    score_columns]
-0001b6f0: 2e69 6e64 6578 2c20 7363 6f72 655f 636f  .index, score_co
-0001b700: 6c75 6d6e 735d 0a20 2020 2020 2020 2020  lumns].         
-0001b710: 2020 2072 6573 756c 7420 3d20 7265 7375     result = resu
-0001b720: 6c74 2e73 7479 6c65 0a20 2020 2020 2020  lt.style.       
-0001b730: 2020 2020 2069 6620 726f 756e 645f 6279       if round_by
-0001b740: 2069 7320 6e6f 7420 4e6f 6e65 3a0a 2020   is not None:.  
-0001b750: 2020 2020 2020 2020 2020 2020 2020 7265                re
-0001b760: 7375 6c74 203d 2072 6573 756c 742e 666f  sult = result.fo
-0001b770: 726d 6174 2873 7562 7365 743d 7375 6273  rmat(subset=subs
-0001b780: 6574 5f73 636f 7265 732c 2074 686f 7573  et_scores, thous
-0001b790: 616e 6473 3d27 2c27 2c20 7072 6563 6973  ands=',', precis
-0001b7a0: 696f 6e3d 726f 756e 645f 6279 290a 2020  ion=round_by).  
-0001b7b0: 2020 2020 2020 2020 2020 656c 7365 3a0a            else:.
-0001b7c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001b7d0: 7265 7375 6c74 203d 2072 6573 756c 742e  result = result.
-0001b7e0: 666f 726d 6174 2873 7562 7365 743d 7375  format(subset=su
-0001b7f0: 6273 6574 5f73 636f 7265 732c 2074 686f  bset_scores, tho
-0001b800: 7573 616e 6473 3d27 2c27 290a 2020 2020  usands=',').    
-0001b810: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
-0001b820: 2072 6573 756c 742e 666f 726d 6174 2873   result.format(s
-0001b830: 7562 7365 743d 7375 6273 6574 5f73 6563  ubset=subset_sec
-0001b840: 6f6e 6461 7279 2c20 7072 6563 6973 696f  ondary, precisio
-0001b850: 6e3d 3329 0a20 2020 2020 2020 2020 2020  n=3).           
-0001b860: 2072 6573 756c 7420 3d20 7265 7375 6c74   result = result
-0001b870: 2e66 6f72 6d61 7428 7375 6273 6574 3d73  .format(subset=s
-0001b880: 7562 7365 745f 746f 7461 6c5f 6f62 7365  ubset_total_obse
-0001b890: 7276 6174 696f 6e73 2c20 7468 6f75 7361  rvations, thousa
-0001b8a0: 6e64 733d 272c 272c 2070 7265 6369 7369  nds=',', precisi
-0001b8b0: 6f6e 3d30 290a 0a20 2020 2020 2020 2072  on=0)..        r
-0001b8c0: 6574 7572 6e20 7265 7375 6c74 0a0a 2020  eturn result..  
-0001b8d0: 2020 6465 6620 706c 6f74 5f72 6573 6964    def plot_resid
-0001b8e0: 7561 6c73 5f76 735f 6669 7473 2873 656c  uals_vs_fits(sel
-0001b8f0: 662c 2066 6967 7572 655f 7369 7a65 3a20  f, figure_size: 
-0001b900: 7475 706c 6520 3d20 5354 414e 4441 5244  tuple = STANDARD
-0001b910: 5f57 4944 5448 5f48 4549 4748 5429 3a0a  _WIDTH_HEIGHT):.
-0001b920: 2020 2020 2020 2020 2222 2250 6c6f 7473          """Plots
-0001b930: 2072 6573 6964 7561 6c73 2076 7320 6669   residuals vs fi
-0001b940: 7474 6564 2076 616c 7565 730a 0a20 2020  tted values..   
-0001b950: 2020 2020 2041 7267 733a 0a20 2020 2020       Args:.     
-0001b960: 2020 2020 2020 2066 6967 7572 655f 7369         figure_si
-0001b970: 7a65 3a0a 2020 2020 2020 2020 2020 2020  ze:.            
-0001b980: 2020 2020 7475 706c 6520 636f 6e74 6169      tuple contai
-0001b990: 6e69 6e67 2060 2877 6964 7468 2c20 6865  ning `(width, he
-0001b9a0: 6967 6874 2960 206f 6620 706c 6f74 2e20  ight)` of plot. 
-0001b9b0: 5468 6520 6465 6661 756c 7420 6865 6967  The default heig
-0001b9c0: 6874 2069 7320 6465 6669 6e65 6420 6279  ht is defined by
-0001b9d0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001b9e0: 2060 6865 6c70 736b 2e70 6c6f 742e 5354   `helpsk.plot.ST
-0001b9f0: 414e 4441 5244 5f48 4549 4748 5460 2c20  ANDARD_HEIGHT`, 
-0001ba00: 616e 6420 7468 6520 6465 6661 756c 7420  and the default 
-0001ba10: 7769 6474 6820 6973 0a20 2020 2020 2020  width is.       
-0001ba20: 2020 2020 2020 2020 2060 6865 6c70 736b           `helpsk
-0001ba30: 2e70 6c6f 742e 5354 414e 4441 5244 5f48  .plot.STANDARD_H
-0001ba40: 4549 4748 5420 2f20 6865 6c70 736b 2e70  EIGHT / helpsk.p
-0001ba50: 6c6f 742e 474f 4c44 454e 5f52 4154 494f  lot.GOLDEN_RATIO
-0001ba60: 600a 2020 2020 2020 2020 2222 220a 2020  `.        """.  
-0001ba70: 2020 2020 2020 6c6f 7765 7373 203d 2073        lowess = s
-0001ba80: 6d2e 6e6f 6e70 6172 616d 6574 7269 632e  m.nonparametric.
-0001ba90: 6c6f 7765 7373 0a20 2020 2020 2020 206c  lowess.        l
-0001baa0: 6f65 7373 5f70 6f69 6e74 7320 3d20 6c6f  oess_points = lo
-0001bab0: 7765 7373 2873 656c 662e 5f72 6573 6964  wess(self._resid
-0001bac0: 7561 6c73 2c20 7365 6c66 2e5f 7072 6564  uals, self._pred
-0001bad0: 6963 7465 645f 7661 6c75 6573 290a 2020  icted_values).  
-0001bae0: 2020 2020 2020 6c6f 6573 735f 782c 206c        loess_x, l
-0001baf0: 6f65 7373 5f79 203d 207a 6970 282a 6c6f  oess_y = zip(*lo
-0001bb00: 6573 735f 706f 696e 7473 290a 0a20 2020  ess_points)..   
-0001bb10: 2020 2020 2070 6c74 2e66 6967 7572 6528       plt.figure(
-0001bb20: 6669 6773 697a 653d 6669 6775 7265 5f73  figsize=figure_s
-0001bb30: 697a 6529 0a20 2020 2020 2020 2070 6c74  ize).        plt
-0001bb40: 2e70 6c6f 7428 6c6f 6573 735f 782c 206c  .plot(loess_x, l
-0001bb50: 6f65 7373 5f79 2c20 636f 6c6f 723d 2772  oess_y, color='r
-0001bb60: 2729 0a20 2020 2020 2020 2070 6c74 2e73  ').        plt.s
-0001bb70: 6361 7474 6572 2878 3d73 656c 662e 5f70  catter(x=self._p
-0001bb80: 7265 6469 6374 6564 5f76 616c 7565 732c  redicted_values,
-0001bb90: 2079 3d73 656c 662e 5f72 6573 6964 7561   y=self._residua
-0001bba0: 6c73 2c20 733d 382c 2061 6c70 6861 3d30  ls, s=8, alpha=0
-0001bbb0: 2e35 290a 2020 2020 2020 2020 706c 742e  .5).        plt.
-0001bbc0: 7469 746c 6528 2752 6573 6964 7561 6c73  title('Residuals
-0001bbd0: 2076 732e 2046 6974 7465 6420 5661 6c75   vs. Fitted Valu
-0001bbe0: 6573 2729 0a20 2020 2020 2020 2070 6c74  es').        plt
-0001bbf0: 2e78 6c61 6265 6c28 2746 6974 7465 6420  .xlabel('Fitted 
-0001bc00: 5661 6c75 6573 2729 0a20 2020 2020 2020  Values').       
-0001bc10: 2070 6c74 2e79 6c61 6265 6c28 2752 6573   plt.ylabel('Res
-0001bc20: 6964 7561 6c73 2028 4163 7475 616c 202d  iduals (Actual -
-0001bc30: 2050 7265 6469 6374 6564 2927 290a 0a20   Predicted)').. 
-0001bc40: 2020 2064 6566 2070 6c6f 745f 7072 6564     def plot_pred
-0001bc50: 6963 7469 6f6e 735f 7673 5f61 6374 7561  ictions_vs_actua
-0001bc60: 6c73 2873 656c 662c 2066 6967 7572 655f  ls(self, figure_
-0001bc70: 7369 7a65 3a20 7475 706c 6520 3d20 5354  size: tuple = ST
-0001bc80: 414e 4441 5244 5f57 4944 5448 5f48 4549  ANDARD_WIDTH_HEI
-0001bc90: 4748 5429 3a0a 2020 2020 2020 2020 2222  GHT):.        ""
-0001bca0: 2250 6c6f 7473 2070 7265 6469 6374 696f  "Plots predictio
-0001bcb0: 6e73 2076 7320 6163 7475 616c 2076 616c  ns vs actual val
-0001bcc0: 7565 730a 0a20 2020 2020 2020 2041 7267  ues..        Arg
-0001bcd0: 733a 0a20 2020 2020 2020 2020 2020 2066  s:.            f
-0001bce0: 6967 7572 655f 7369 7a65 3a0a 2020 2020  igure_size:.    
-0001bcf0: 2020 2020 2020 2020 2020 2020 7475 706c              tupl
-0001bd00: 6520 636f 6e74 6169 6e69 6e67 2060 2877  e containing `(w
-0001bd10: 6964 7468 2c20 6865 6967 6874 2960 206f  idth, height)` o
-0001bd20: 6620 706c 6f74 2e20 5468 6520 6465 6661  f plot. The defa
-0001bd30: 756c 7420 6865 6967 6874 2069 7320 6465  ult height is de
-0001bd40: 6669 6e65 6420 6279 0a20 2020 2020 2020  fined by.       
-0001bd50: 2020 2020 2020 2020 2060 6865 6c70 736b           `helpsk
-0001bd60: 2e70 6c6f 742e 5354 414e 4441 5244 5f48  .plot.STANDARD_H
-0001bd70: 4549 4748 5460 2c20 616e 6420 7468 6520  EIGHT`, and the 
-0001bd80: 6465 6661 756c 7420 7769 6474 6820 6973  default width is
-0001bd90: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001bda0: 2060 6865 6c70 736b 2e70 6c6f 742e 5354   `helpsk.plot.ST
-0001bdb0: 414e 4441 5244 5f48 4549 4748 5420 2f20  ANDARD_HEIGHT / 
-0001bdc0: 6865 6c70 736b 2e70 6c6f 742e 474f 4c44  helpsk.plot.GOLD
-0001bdd0: 454e 5f52 4154 494f 600a 2020 2020 2020  EN_RATIO`.      
-0001bde0: 2020 2222 220a 2020 2020 2020 2020 6c6f    """.        lo
-0001bdf0: 7765 7373 203d 2073 6d2e 6e6f 6e70 6172  wess = sm.nonpar
-0001be00: 616d 6574 7269 632e 6c6f 7765 7373 0a20  ametric.lowess. 
-0001be10: 2020 2020 2020 206c 6f65 7373 5f70 6f69         loess_poi
-0001be20: 6e74 7320 3d20 6c6f 7765 7373 2873 656c  nts = lowess(sel
-0001be30: 662e 5f70 7265 6469 6374 6564 5f76 616c  f._predicted_val
-0001be40: 7565 732c 2073 656c 662e 5f61 6374 7561  ues, self._actua
-0001be50: 6c5f 7661 6c75 6573 290a 2020 2020 2020  l_values).      
-0001be60: 2020 6c6f 6573 735f 782c 206c 6f65 7373    loess_x, loess
-0001be70: 5f79 203d 207a 6970 282a 6c6f 6573 735f  _y = zip(*loess_
-0001be80: 706f 696e 7473 290a 0a20 2020 2020 2020  points)..       
-0001be90: 2070 6c74 2e66 6967 7572 6528 6669 6773   plt.figure(figs
-0001bea0: 697a 653d 6669 6775 7265 5f73 697a 6529  ize=figure_size)
-0001beb0: 0a20 2020 2020 2020 2070 6c74 2e70 6c6f  .        plt.plo
-0001bec0: 7428 6c6f 6573 735f 782c 206c 6f65 7373  t(loess_x, loess
-0001bed0: 5f79 2c20 636f 6c6f 723d 2772 272c 2061  _y, color='r', a
-0001bee0: 6c70 6861 3d30 2e35 2c20 6c61 6265 6c3d  lpha=0.5, label=
-0001bef0: 274c 6f65 7373 2028 5072 6564 6963 7469  'Loess (Predicti
-0001bf00: 6f6e 7320 7673 2041 6374 7561 6c73 2927  ons vs Actuals)'
-0001bf10: 290a 2020 2020 2020 2020 706c 742e 706c  ).        plt.pl
-0001bf20: 6f74 2873 656c 662e 5f61 6374 7561 6c5f  ot(self._actual_
-0001bf30: 7661 6c75 6573 2c20 7365 6c66 2e5f 6163  values, self._ac
-0001bf40: 7475 616c 5f76 616c 7565 732c 2063 6f6c  tual_values, col
-0001bf50: 6f72 3d27 6227 2c20 616c 7068 613d 302e  or='b', alpha=0.
-0001bf60: 352c 206c 6162 656c 3d27 5065 7266 6563  5, label='Perfec
-0001bf70: 7420 5072 6564 6963 7469 6f6e 2729 0a20  t Prediction'). 
-0001bf80: 2020 2020 2020 2070 6c74 2e73 6361 7474         plt.scatt
-0001bf90: 6572 2878 3d73 656c 662e 5f61 6374 7561  er(x=self._actua
-0001bfa0: 6c5f 7661 6c75 6573 2c20 793d 7365 6c66  l_values, y=self
-0001bfb0: 2e5f 7072 6564 6963 7465 645f 7661 6c75  ._predicted_valu
-0001bfc0: 6573 2c20 733d 382c 2061 6c70 6861 3d30  es, s=8, alpha=0
-0001bfd0: 2e35 290a 2020 2020 2020 2020 706c 742e  .5).        plt.
-0001bfe0: 7469 746c 6528 2750 7265 6469 6374 6564  title('Predicted
-0001bff0: 2056 616c 7565 7320 7673 2e20 4163 7475   Values vs. Actu
-0001c000: 616c 2056 616c 7565 7327 290a 2020 2020  al Values').    
-0001c010: 2020 2020 706c 742e 786c 6162 656c 2827      plt.xlabel('
-0001c020: 4163 7475 616c 7327 290a 2020 2020 2020  Actuals').      
-0001c030: 2020 706c 742e 796c 6162 656c 2827 5072    plt.ylabel('Pr
-0001c040: 6564 6963 7465 6427 290a 2020 2020 2020  edicted').      
-0001c050: 2020 6178 6973 203d 2070 6c74 2e67 6361    axis = plt.gca
-0001c060: 2829 0a20 2020 2020 2020 2068 616e 646c  ().        handl
-0001c070: 6573 2c20 6c61 6265 6c73 203d 2061 7869  es, labels = axi
-0001c080: 732e 6765 745f 6c65 6765 6e64 5f68 616e  s.get_legend_han
-0001c090: 646c 6573 5f6c 6162 656c 7328 290a 2020  dles_labels().  
-0001c0a0: 2020 2020 2020 6178 6973 2e6c 6567 656e        axis.legen
-0001c0b0: 6428 6861 6e64 6c65 732c 206c 6162 656c  d(handles, label
-0001c0c0: 7329 0a20 2020 2020 2020 2070 6c74 2e66  s).        plt.f
-0001c0d0: 6967 7465 7874 2830 2e39 392c 2030 2e30  igtext(0.99, 0.0
-0001c0e0: 312c 0a20 2020 2020 2020 2020 2020 2020  1,.             
-0001c0f0: 2020 2020 2020 2027 4e6f 7465 3a20 6f62         'Note: ob
-0001c100: 7365 7276 6174 696f 6e73 2061 626f 7665  servations above
-0001c110: 2062 6c75 6520 6c69 6e65 206d 6561 6e20   blue line mean 
-0001c120: 6d6f 6465 6c20 6973 206f 7665 722d 7072  model is over-pr
-0001c130: 6564 6963 7469 6e67 3b20 6265 6c6f 7720  edicting; below 
-0001c140: 6d65 616e 7320 756e 6465 722d 270a 2020  means under-'.  
-0001c150: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001c160: 2020 2770 7265 6469 6374 696e 672e 272c    'predicting.',
-0001c170: 2020 2320 6e6f 7161 0a20 2020 2020 2020    # noqa.       
-0001c180: 2020 2020 2020 2020 2020 2020 2068 6f72               hor
-0001c190: 697a 6f6e 7461 6c61 6c69 676e 6d65 6e74  izontalalignment
-0001c1a0: 3d27 7269 6768 7427 290a 2020 2020 2020  ='right').      
-0001c1b0: 2020 7265 7475 726e 2061 7869 730a 0a20    return axis.. 
-0001c1c0: 2020 2064 6566 2070 6c6f 745f 7265 7369     def plot_resi
-0001c1d0: 6475 616c 735f 7673 5f61 6374 7561 6c73  duals_vs_actuals
-0001c1e0: 2873 656c 662c 2066 6967 7572 655f 7369  (self, figure_si
-0001c1f0: 7a65 3a20 7475 706c 6520 3d20 5354 414e  ze: tuple = STAN
-0001c200: 4441 5244 5f57 4944 5448 5f48 4549 4748  DARD_WIDTH_HEIGH
-0001c210: 5429 3a0a 2020 2020 2020 2020 2222 2250  T):.        """P
-0001c220: 6c6f 7473 2072 6573 6964 7561 6c73 2076  lots residuals v
-0001c230: 7320 6163 7475 616c 7320 7661 6c75 6573  s actuals values
-0001c240: 0a0a 2020 2020 2020 2020 4172 6773 3a0a  ..        Args:.
-0001c250: 2020 2020 2020 2020 2020 2020 6669 6775              figu
-0001c260: 7265 5f73 697a 653a 0a20 2020 2020 2020  re_size:.       
-0001c270: 2020 2020 2020 2020 2074 7570 6c65 2063           tuple c
-0001c280: 6f6e 7461 696e 696e 6720 6028 7769 6474  ontaining `(widt
-0001c290: 682c 2068 6569 6768 7429 6020 6f66 2070  h, height)` of p
-0001c2a0: 6c6f 742e 2054 6865 2064 6566 6175 6c74  lot. The default
-0001c2b0: 2068 6569 6768 7420 6973 2064 6566 696e   height is defin
-0001c2c0: 6564 2062 790a 2020 2020 2020 2020 2020  ed by.          
-0001c2d0: 2020 2020 2020 6068 656c 7073 6b2e 706c        `helpsk.pl
-0001c2e0: 6f74 2e53 5441 4e44 4152 445f 4845 4947  ot.STANDARD_HEIG
-0001c2f0: 4854 602c 2061 6e64 2074 6865 2064 6566  HT`, and the def
-0001c300: 6175 6c74 2077 6964 7468 2069 730a 2020  ault width is.  
-0001c310: 2020 2020 2020 2020 2020 2020 2020 6068                `h
-0001c320: 656c 7073 6b2e 706c 6f74 2e53 5441 4e44  elpsk.plot.STAND
-0001c330: 4152 445f 4845 4947 4854 202f 2068 656c  ARD_HEIGHT / hel
-0001c340: 7073 6b2e 706c 6f74 2e47 4f4c 4445 4e5f  psk.plot.GOLDEN_
-0001c350: 5241 5449 4f60 0a20 2020 2020 2020 2022  RATIO`.        "
-0001c360: 2222 0a20 2020 2020 2020 206c 6f77 6573  "".        lowes
-0001c370: 7320 3d20 736d 2e6e 6f6e 7061 7261 6d65  s = sm.nonparame
-0001c380: 7472 6963 2e6c 6f77 6573 730a 2020 2020  tric.lowess.    
-0001c390: 2020 2020 6c6f 6573 735f 706f 696e 7473      loess_points
-0001c3a0: 203d 206c 6f77 6573 7328 7365 6c66 2e5f   = lowess(self._
-0001c3b0: 7265 7369 6475 616c 732c 2073 656c 662e  residuals, self.
-0001c3c0: 5f61 6374 7561 6c5f 7661 6c75 6573 290a  _actual_values).
-0001c3d0: 2020 2020 2020 2020 6c6f 6573 735f 782c          loess_x,
-0001c3e0: 206c 6f65 7373 5f79 203d 207a 6970 282a   loess_y = zip(*
-0001c3f0: 6c6f 6573 735f 706f 696e 7473 290a 0a20  loess_points).. 
-0001c400: 2020 2020 2020 2070 6c74 2e66 6967 7572         plt.figur
-0001c410: 6528 6669 6773 697a 653d 6669 6775 7265  e(figsize=figure
-0001c420: 5f73 697a 6529 0a20 2020 2020 2020 2070  _size).        p
-0001c430: 6c74 2e70 6c6f 7428 6c6f 6573 735f 782c  lt.plot(loess_x,
-0001c440: 206c 6f65 7373 5f79 2c20 636f 6c6f 723d   loess_y, color=
-0001c450: 2772 2729 0a20 2020 2020 2020 2070 6c74  'r').        plt
-0001c460: 2e73 6361 7474 6572 2878 3d73 656c 662e  .scatter(x=self.
-0001c470: 5f61 6374 7561 6c5f 7661 6c75 6573 2c20  _actual_values, 
-0001c480: 793d 7365 6c66 2e5f 7265 7369 6475 616c  y=self._residual
-0001c490: 732c 2073 3d38 2c20 616c 7068 613d 302e  s, s=8, alpha=0.
-0001c4a0: 3529 0a20 2020 2020 2020 2070 6c74 2e74  5).        plt.t
-0001c4b0: 6974 6c65 2827 5265 7369 6475 616c 7320  itle('Residuals 
-0001c4c0: 7673 2e20 4163 7475 616c 2056 616c 7565  vs. Actual Value
-0001c4d0: 7327 290a 2020 2020 2020 2020 706c 742e  s').        plt.
-0001c4e0: 786c 6162 656c 2827 4163 7475 616c 2729  xlabel('Actual')
-0001c4f0: 0a20 2020 2020 2020 2070 6c74 2e79 6c61  .        plt.yla
-0001c500: 6265 6c28 2752 6573 6964 7561 6c73 2028  bel('Residuals (
-0001c510: 4163 7475 616c 202d 2050 7265 6469 6374  Actual - Predict
-0001c520: 6564 2927 290a 2020 2020 2020 2020 706c  ed)').        pl
-0001c530: 742e 6669 6774 6578 7428 302e 3939 2c20  t.figtext(0.99, 
-0001c540: 302e 3031 2c0a 2020 2020 2020 2020 2020  0.01,.          
-0001c550: 2020 2020 2020 2020 2020 274e 6f74 653a            'Note:
-0001c560: 2041 6374 7561 6c20 3e20 5072 6564 6963   Actual > Predic
-0001c570: 7465 6420 3d3e 2055 6e64 6572 2d70 7265  ted => Under-pre
-0001c580: 6469 6374 696e 6720 2870 6f73 6974 6976  dicting (positiv
-0001c590: 6520 7265 7369 6475 616c 293b 206e 6567  e residual); neg
-0001c5a0: 6174 6976 6520 7265 7369 6475 616c 7320  ative residuals 
-0001c5b0: 270a 2020 2020 2020 2020 2020 2020 2020  '.              
-0001c5c0: 2020 2020 2020 276d 6561 6e20 6f76 6572        'mean over
-0001c5d0: 2d70 7265 6469 6374 696e 6727 2c20 2023  -predicting',  #
-0001c5e0: 206e 6f71 610a 2020 2020 2020 2020 2020   noqa.          
-0001c5f0: 2020 2020 2020 2020 2020 686f 7269 7a6f            horizo
-0001c600: 6e74 616c 616c 6967 6e6d 656e 743d 2772  ntalalignment='r
-0001c610: 6967 6874 2729 0a0a 0a63 6c61 7373 2054  ight')...class T
-0001c620: 776f 436c 6173 734d 6f64 656c 436f 6d70  woClassModelComp
-0001c630: 6172 6973 6f6e 3a0a 2020 2020 2222 2254  arison:.    """T
-0001c640: 6869 7320 636c 6173 7320 636f 6d70 6172  his class compar
-0001c650: 6573 206d 756c 7469 706c 6520 6d6f 6465  es multiple mode
-0001c660: 6c73 2074 7261 696e 6564 206f 6e20 5477  ls trained on Tw
-0001c670: 6f20 436c 6173 7320 2869 2e65 2e20 3027  o Class (i.e. 0'
-0001c680: 732f 3127 7329 2070 7265 6469 6374 696f  s/1's) predictio
-0001c690: 6e20 7363 656e 6172 696f 732e 2222 220a  n scenarios.""".
-0001c6a0: 0a20 2020 2023 2070 796c 696e 743a 2064  .    # pylint: d
-0001c6b0: 6973 6162 6c65 3d74 6f6f 2d6d 616e 792d  isable=too-many-
-0001c6c0: 6172 6775 6d65 6e74 730a 2020 2020 6465  arguments.    de
-0001c6d0: 6620 5f5f 696e 6974 5f5f 2873 656c 662c  f __init__(self,
-0001c6e0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001c6f0: 2020 6163 7475 616c 5f76 616c 7565 733a    actual_values:
-0001c700: 206e 702e 6e64 6172 7261 792c 0a20 2020   np.ndarray,.   
-0001c710: 2020 2020 2020 2020 2020 2020 2020 7072                pr
-0001c720: 6564 6963 7465 645f 7363 6f72 6573 3a20  edicted_scores: 
-0001c730: 4469 6374 5b73 7472 2c20 6e70 2e6e 6461  Dict[str, np.nda
-0001c740: 7272 6179 5d2c 0a20 2020 2020 2020 2020  rray],.         
-0001c750: 2020 2020 2020 2020 706f 7369 7469 7665          positive
-0001c760: 5f63 6c61 7373 3a20 7374 7220 3d20 2750  _class: str = 'P
-0001c770: 6f73 6974 6976 6520 436c 6173 7327 2c0a  ositive Class',.
-0001c780: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001c790: 206e 6567 6174 6976 655f 636c 6173 733a   negative_class:
-0001c7a0: 2073 7472 203d 2027 4e65 6761 7469 7665   str = 'Negative
-0001c7b0: 2043 6c61 7373 272c 0a20 2020 2020 2020   Class',.       
-0001c7c0: 2020 2020 2020 2020 2020 7363 6f72 655f            score_
-0001c7d0: 7468 7265 7368 6f6c 643a 2066 6c6f 6174  threshold: float
-0001c7e0: 203d 2030 2e35 0a20 2020 2020 2020 2020   = 0.5.         
-0001c7f0: 2020 2020 2020 2020 293a 0a20 2020 2020          ):.     
-0001c800: 2020 2022 2222 0a20 2020 2020 2020 2041     """.        A
-0001c810: 7267 733a 0a20 2020 2020 2020 2020 2020  rgs:.           
-0001c820: 2061 6374 7561 6c5f 7661 6c75 6573 3a0a   actual_values:.
-0001c830: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001c840: 6172 7261 7920 6f66 2030 2773 2061 6e64  array of 0's and
-0001c850: 2031 2773 0a20 2020 2020 2020 2020 2020   1's.           
-0001c860: 2070 7265 6469 6374 6564 5f73 636f 7265   predicted_score
-0001c870: 733a 0a20 2020 2020 2020 2020 2020 2020  s:.             
-0001c880: 2020 2064 6963 7469 6f6e 6172 7920 7065     dictionary pe
-0001c890: 7220 6d6f 6465 6c20 7769 7468 206b 6579  r model with key
-0001c8a0: 2061 7320 7468 6520 6e61 6d65 206f 6620   as the name of 
-0001c8b0: 7468 6520 6d6f 6465 6c20 616e 6420 7661  the model and va
-0001c8c0: 6c75 6520 7468 6174 2069 7320 616e 2061  lue that is an a
-0001c8d0: 7272 6179 206f 660a 2020 2020 2020 2020  rray of.        
-0001c8e0: 2020 2020 2020 2020 6465 6369 6d61 6c2f          decimal/
-0001c8f0: 666c 6f61 7420 7661 6c75 6573 2066 726f  float values fro
-0001c900: 6d20 6070 7265 6469 6374 5f70 726f 6261  m `predict_proba
-0001c910: 2829 603b 204e 4f54 2074 6865 2061 6374  ()`; NOT the act
-0001c920: 7561 6c20 636c 6173 730a 2020 2020 2020  ual class.      
-0001c930: 2020 2020 2020 706f 7369 7469 7665 5f63        positive_c
-0001c940: 6c61 7373 3a0a 2020 2020 2020 2020 2020  lass:.          
-0001c950: 2020 2020 2020 7374 7269 6e67 206f 6620        string of 
-0001c960: 7468 6520 6e61 6d65 2f6c 6162 656c 206f  the name/label o
-0001c970: 6620 7468 6520 706f 7369 7469 7665 2063  f the positive c
-0001c980: 6c61 7373 2028 692e 652e 2076 616c 7565  lass (i.e. value
-0001c990: 206f 6620 3129 2e20 496e 206f 7468 6572   of 1). In other
-0001c9a0: 2077 6f72 6473 2c20 6e6f 740a 2020 2020   words, not.    
-0001c9b0: 2020 2020 2020 2020 2020 2020 2770 6f73              'pos
-0001c9c0: 6974 6976 6527 2069 6e20 7468 6520 7365  itive' in the se
-0001c9d0: 6e73 6520 6f66 2027 676f 6f64 2720 6275  nse of 'good' bu
-0001c9e0: 7420 2770 6f73 6974 6976 6527 2061 7320  t 'positive' as 
-0001c9f0: 696e 2027 5472 7565 2f46 616c 7365 2050  in 'True/False P
-0001ca00: 6f73 6974 6976 6527 2e0a 2020 2020 2020  ositive'..      
-0001ca10: 2020 2020 2020 6e65 6761 7469 7665 5f63        negative_c
-0001ca20: 6c61 7373 3a0a 2020 2020 2020 2020 2020  lass:.          
-0001ca30: 2020 2020 2020 7374 7269 6e67 206f 6620        string of 
-0001ca40: 7468 6520 6e61 6d65 2f6c 6162 656c 206f  the name/label o
-0001ca50: 6620 7468 6520 6e65 6761 7469 7665 2063  f the negative c
-0001ca60: 6c61 7373 2028 692e 652e 2076 616c 7565  lass (i.e. value
-0001ca70: 206f 6620 3029 2e20 496e 206f 7468 6572   of 0). In other
-0001ca80: 2077 6f72 6473 2c20 6e6f 740a 2020 2020   words, not.    
-0001ca90: 2020 2020 2020 2020 2020 2020 276e 6567              'neg
-0001caa0: 6174 6976 6527 2069 6e20 7468 6520 7365  ative' in the se
-0001cab0: 6e73 6520 6f66 2027 676f 6f64 2720 6275  nse of 'good' bu
-0001cac0: 7420 276e 6567 6174 6976 6527 2061 7320  t 'negative' as 
-0001cad0: 696e 2027 5472 7565 2f46 616c 7365 204e  in 'True/False N
-0001cae0: 6567 6174 6976 6527 2e0a 2020 2020 2020  egative'..      
-0001caf0: 2020 2020 2020 7363 6f72 655f 7468 7265        score_thre
-0001cb00: 7368 6f6c 643a 0a20 2020 2020 2020 2020  shold:.         
-0001cb10: 2020 2020 2020 2074 6865 2073 636f 7265         the score
-0001cb20: 2f70 726f 6261 6269 6c69 7479 2074 6872  /probability thr
-0001cb30: 6573 686f 6c64 2066 6f72 2074 7572 6e69  eshold for turni
-0001cb40: 6e67 2073 636f 7265 7320 696e 746f 2030  ng scores into 0
-0001cb50: 2773 2061 6e64 2031 2773 2061 6e64 2063  's and 1's and c
-0001cb60: 6f72 7265 7370 6f6e 6469 6e67 206c 6162  orresponding lab
-0001cb70: 656c 730a 2020 2020 2020 2020 2222 220a  els.        """.
-0001cb80: 2020 2020 2020 2020 6173 7365 7274 2069          assert i
-0001cb90: 7369 6e73 7461 6e63 6528 7072 6564 6963  sinstance(predic
-0001cba0: 7465 645f 7363 6f72 6573 2c20 6469 6374  ted_scores, dict
-0001cbb0: 290a 0a20 2020 2020 2020 2066 6f72 2076  )..        for v
-0001cbc0: 616c 7565 7320 696e 2070 7265 6469 6374  alues in predict
-0001cbd0: 6564 5f73 636f 7265 732e 7661 6c75 6573  ed_scores.values
-0001cbe0: 2829 3a0a 2020 2020 2020 2020 2020 2020  ():.            
-0001cbf0: 6173 7365 7274 206c 656e 2861 6374 7561  assert len(actua
-0001cc00: 6c5f 7661 6c75 6573 2920 3d3d 206c 656e  l_values) == len
-0001cc10: 2876 616c 7565 7329 0a0a 2020 2020 2020  (values)..      
-0001cc20: 2020 7365 6c66 2e5f 706f 7369 7469 7665    self._positive
-0001cc30: 5f63 6c61 7373 203d 2070 6f73 6974 6976  _class = positiv
-0001cc40: 655f 636c 6173 730a 2020 2020 2020 2020  e_class.        
-0001cc50: 7365 6c66 2e5f 6e65 6761 7469 7665 5f63  self._negative_c
-0001cc60: 6c61 7373 203d 206e 6567 6174 6976 655f  lass = negative_
-0001cc70: 636c 6173 730a 2020 2020 2020 2020 7365  class.        se
-0001cc80: 6c66 2e5f 6163 7475 616c 5f76 616c 7565  lf._actual_value
-0001cc90: 7320 3d20 6163 7475 616c 5f76 616c 7565  s = actual_value
-0001cca0: 730a 2020 2020 2020 2020 7365 6c66 2e5f  s.        self._
-0001ccb0: 7072 6564 6963 7465 645f 7363 6f72 6573  predicted_scores
-0001ccc0: 203d 2070 7265 6469 6374 6564 5f73 636f   = predicted_sco
-0001ccd0: 7265 730a 2020 2020 2020 2020 7365 6c66  res.        self
-0001cce0: 2e73 636f 7265 5f74 6872 6573 686f 6c64  .score_threshold
-0001ccf0: 203d 2073 636f 7265 5f74 6872 6573 686f   = score_thresho
-0001cd00: 6c64 0a0a 2020 2020 2020 2020 7365 6c66  ld..        self
-0001cd10: 2e5f 6576 616c 7561 746f 7273 203d 207b  ._evaluators = {
-0001cd20: 6b65 793a 2054 776f 436c 6173 7345 7661  key: TwoClassEva
-0001cd30: 6c75 6174 6f72 2861 6374 7561 6c5f 7661  luator(actual_va
-0001cd40: 6c75 6573 3d61 6374 7561 6c5f 7661 6c75  lues=actual_valu
-0001cd50: 6573 2c0a 2020 2020 2020 2020 2020 2020  es,.            
+0001b6d0: 2020 2020 2020 2020 2020 2020 7363 6f72              scor
+0001b6e0: 655f 636f 6c75 6d6e 735d 2e69 6e64 6578  e_columns].index
+0001b6f0: 2c20 7363 6f72 655f 636f 6c75 6d6e 735d  , score_columns]
+0001b700: 0a20 2020 2020 2020 2020 2020 2072 6573  .            res
+0001b710: 756c 7420 3d20 7265 7375 6c74 2e73 7479  ult = result.sty
+0001b720: 6c65 0a20 2020 2020 2020 2020 2020 2069  le.            i
+0001b730: 6620 726f 756e 645f 6279 2069 7320 6e6f  f round_by is no
+0001b740: 7420 4e6f 6e65 3a0a 2020 2020 2020 2020  t None:.        
+0001b750: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
+0001b760: 2072 6573 756c 742e 666f 726d 6174 2873   result.format(s
+0001b770: 7562 7365 743d 7375 6273 6574 5f73 636f  ubset=subset_sco
+0001b780: 7265 732c 2074 686f 7573 616e 6473 3d27  res, thousands='
+0001b790: 2c27 2c20 7072 6563 6973 696f 6e3d 726f  ,', precision=ro
+0001b7a0: 756e 645f 6279 290a 2020 2020 2020 2020  und_by).        
+0001b7b0: 2020 2020 656c 7365 3a0a 2020 2020 2020      else:.      
+0001b7c0: 2020 2020 2020 2020 2020 7265 7375 6c74            result
+0001b7d0: 203d 2072 6573 756c 742e 666f 726d 6174   = result.format
+0001b7e0: 2873 7562 7365 743d 7375 6273 6574 5f73  (subset=subset_s
+0001b7f0: 636f 7265 732c 2074 686f 7573 616e 6473  cores, thousands
+0001b800: 3d27 2c27 290a 2020 2020 2020 2020 2020  =',').          
+0001b810: 2020 7265 7375 6c74 203d 2072 6573 756c    result = resul
+0001b820: 742e 666f 726d 6174 2873 7562 7365 743d  t.format(subset=
+0001b830: 7375 6273 6574 5f73 6563 6f6e 6461 7279  subset_secondary
+0001b840: 2c20 7072 6563 6973 696f 6e3d 3329 0a20  , precision=3). 
+0001b850: 2020 2020 2020 2020 2020 2072 6573 756c             resul
+0001b860: 7420 3d20 7265 7375 6c74 2e66 6f72 6d61  t = result.forma
+0001b870: 7428 7375 6273 6574 3d73 7562 7365 745f  t(subset=subset_
+0001b880: 746f 7461 6c5f 6f62 7365 7276 6174 696f  total_observatio
+0001b890: 6e73 2c20 7468 6f75 7361 6e64 733d 272c  ns, thousands=',
+0001b8a0: 272c 2070 7265 6369 7369 6f6e 3d30 290a  ', precision=0).
+0001b8b0: 0a20 2020 2020 2020 2072 6574 7572 6e20  .        return 
+0001b8c0: 7265 7375 6c74 0a0a 2020 2020 6465 6620  result..    def 
+0001b8d0: 706c 6f74 5f72 6573 6964 7561 6c73 5f76  plot_residuals_v
+0001b8e0: 735f 6669 7473 2873 656c 662c 2066 6967  s_fits(self, fig
+0001b8f0: 7572 655f 7369 7a65 3a20 7475 706c 6520  ure_size: tuple 
+0001b900: 3d20 5354 414e 4441 5244 5f57 4944 5448  = STANDARD_WIDTH
+0001b910: 5f48 4549 4748 5429 3a0a 2020 2020 2020  _HEIGHT):.      
+0001b920: 2020 2222 2250 6c6f 7473 2072 6573 6964    """Plots resid
+0001b930: 7561 6c73 2076 7320 6669 7474 6564 2076  uals vs fitted v
+0001b940: 616c 7565 730a 0a20 2020 2020 2020 2041  alues..        A
+0001b950: 7267 733a 0a20 2020 2020 2020 2020 2020  rgs:.           
+0001b960: 2066 6967 7572 655f 7369 7a65 3a0a 2020   figure_size:.  
+0001b970: 2020 2020 2020 2020 2020 2020 2020 7475                tu
+0001b980: 706c 6520 636f 6e74 6169 6e69 6e67 2060  ple containing `
+0001b990: 2877 6964 7468 2c20 6865 6967 6874 2960  (width, height)`
+0001b9a0: 206f 6620 706c 6f74 2e20 5468 6520 6465   of plot. The de
+0001b9b0: 6661 756c 7420 6865 6967 6874 2069 7320  fault height is 
+0001b9c0: 6465 6669 6e65 6420 6279 0a20 2020 2020  defined by.     
+0001b9d0: 2020 2020 2020 2020 2020 2060 6865 6c70             `help
+0001b9e0: 736b 2e70 6c6f 742e 5354 414e 4441 5244  sk.plot.STANDARD
+0001b9f0: 5f48 4549 4748 5460 2c20 616e 6420 7468  _HEIGHT`, and th
+0001ba00: 6520 6465 6661 756c 7420 7769 6474 6820  e default width 
+0001ba10: 6973 0a20 2020 2020 2020 2020 2020 2020  is.             
+0001ba20: 2020 2060 6865 6c70 736b 2e70 6c6f 742e     `helpsk.plot.
+0001ba30: 5354 414e 4441 5244 5f48 4549 4748 5420  STANDARD_HEIGHT 
+0001ba40: 2f20 6865 6c70 736b 2e70 6c6f 742e 474f  / helpsk.plot.GO
+0001ba50: 4c44 454e 5f52 4154 494f 600a 2020 2020  LDEN_RATIO`.    
+0001ba60: 2020 2020 2222 220a 2020 2020 2020 2020      """.        
+0001ba70: 6c6f 7765 7373 203d 2073 6d2e 6e6f 6e70  lowess = sm.nonp
+0001ba80: 6172 616d 6574 7269 632e 6c6f 7765 7373  arametric.lowess
+0001ba90: 0a20 2020 2020 2020 206c 6f65 7373 5f70  .        loess_p
+0001baa0: 6f69 6e74 7320 3d20 6c6f 7765 7373 2873  oints = lowess(s
+0001bab0: 656c 662e 5f72 6573 6964 7561 6c73 2c20  elf._residuals, 
+0001bac0: 7365 6c66 2e5f 7072 6564 6963 7465 645f  self._predicted_
+0001bad0: 7661 6c75 6573 290a 2020 2020 2020 2020  values).        
+0001bae0: 6c6f 6573 735f 782c 206c 6f65 7373 5f79  loess_x, loess_y
+0001baf0: 203d 207a 6970 282a 6c6f 6573 735f 706f   = zip(*loess_po
+0001bb00: 696e 7473 290a 0a20 2020 2020 2020 2070  ints)..        p
+0001bb10: 6c74 2e66 6967 7572 6528 6669 6773 697a  lt.figure(figsiz
+0001bb20: 653d 6669 6775 7265 5f73 697a 6529 0a20  e=figure_size). 
+0001bb30: 2020 2020 2020 2070 6c74 2e70 6c6f 7428         plt.plot(
+0001bb40: 6c6f 6573 735f 782c 206c 6f65 7373 5f79  loess_x, loess_y
+0001bb50: 2c20 636f 6c6f 723d 2772 2729 0a20 2020  , color='r').   
+0001bb60: 2020 2020 2070 6c74 2e73 6361 7474 6572       plt.scatter
+0001bb70: 2878 3d73 656c 662e 5f70 7265 6469 6374  (x=self._predict
+0001bb80: 6564 5f76 616c 7565 732c 2079 3d73 656c  ed_values, y=sel
+0001bb90: 662e 5f72 6573 6964 7561 6c73 2c20 733d  f._residuals, s=
+0001bba0: 382c 2061 6c70 6861 3d30 2e35 290a 2020  8, alpha=0.5).  
+0001bbb0: 2020 2020 2020 706c 742e 7469 746c 6528        plt.title(
+0001bbc0: 2752 6573 6964 7561 6c73 2076 732e 2046  'Residuals vs. F
+0001bbd0: 6974 7465 6420 5661 6c75 6573 2729 0a20  itted Values'). 
+0001bbe0: 2020 2020 2020 2070 6c74 2e78 6c61 6265         plt.xlabe
+0001bbf0: 6c28 2746 6974 7465 6420 5661 6c75 6573  l('Fitted Values
+0001bc00: 2729 0a20 2020 2020 2020 2070 6c74 2e79  ').        plt.y
+0001bc10: 6c61 6265 6c28 2752 6573 6964 7561 6c73  label('Residuals
+0001bc20: 2028 4163 7475 616c 202d 2050 7265 6469   (Actual - Predi
+0001bc30: 6374 6564 2927 290a 0a20 2020 2064 6566  cted)')..    def
+0001bc40: 2070 6c6f 745f 7072 6564 6963 7469 6f6e   plot_prediction
+0001bc50: 735f 7673 5f61 6374 7561 6c73 2873 656c  s_vs_actuals(sel
+0001bc60: 662c 2066 6967 7572 655f 7369 7a65 3a20  f, figure_size: 
+0001bc70: 7475 706c 6520 3d20 5354 414e 4441 5244  tuple = STANDARD
+0001bc80: 5f57 4944 5448 5f48 4549 4748 5429 3a0a  _WIDTH_HEIGHT):.
+0001bc90: 2020 2020 2020 2020 2222 2250 6c6f 7473          """Plots
+0001bca0: 2070 7265 6469 6374 696f 6e73 2076 7320   predictions vs 
+0001bcb0: 6163 7475 616c 2076 616c 7565 730a 0a20  actual values.. 
+0001bcc0: 2020 2020 2020 2041 7267 733a 0a20 2020         Args:.   
+0001bcd0: 2020 2020 2020 2020 2066 6967 7572 655f           figure_
+0001bce0: 7369 7a65 3a0a 2020 2020 2020 2020 2020  size:.          
+0001bcf0: 2020 2020 2020 7475 706c 6520 636f 6e74        tuple cont
+0001bd00: 6169 6e69 6e67 2060 2877 6964 7468 2c20  aining `(width, 
+0001bd10: 6865 6967 6874 2960 206f 6620 706c 6f74  height)` of plot
+0001bd20: 2e20 5468 6520 6465 6661 756c 7420 6865  . The default he
+0001bd30: 6967 6874 2069 7320 6465 6669 6e65 6420  ight is defined 
+0001bd40: 6279 0a20 2020 2020 2020 2020 2020 2020  by.             
+0001bd50: 2020 2060 6865 6c70 736b 2e70 6c6f 742e     `helpsk.plot.
+0001bd60: 5354 414e 4441 5244 5f48 4549 4748 5460  STANDARD_HEIGHT`
+0001bd70: 2c20 616e 6420 7468 6520 6465 6661 756c  , and the defaul
+0001bd80: 7420 7769 6474 6820 6973 0a20 2020 2020  t width is.     
+0001bd90: 2020 2020 2020 2020 2020 2060 6865 6c70             `help
+0001bda0: 736b 2e70 6c6f 742e 5354 414e 4441 5244  sk.plot.STANDARD
+0001bdb0: 5f48 4549 4748 5420 2f20 6865 6c70 736b  _HEIGHT / helpsk
+0001bdc0: 2e70 6c6f 742e 474f 4c44 454e 5f52 4154  .plot.GOLDEN_RAT
+0001bdd0: 494f 600a 2020 2020 2020 2020 2222 220a  IO`.        """.
+0001bde0: 2020 2020 2020 2020 6c6f 7765 7373 203d          lowess =
+0001bdf0: 2073 6d2e 6e6f 6e70 6172 616d 6574 7269   sm.nonparametri
+0001be00: 632e 6c6f 7765 7373 0a20 2020 2020 2020  c.lowess.       
+0001be10: 206c 6f65 7373 5f70 6f69 6e74 7320 3d20   loess_points = 
+0001be20: 6c6f 7765 7373 2873 656c 662e 5f70 7265  lowess(self._pre
+0001be30: 6469 6374 6564 5f76 616c 7565 732c 2073  dicted_values, s
+0001be40: 656c 662e 5f61 6374 7561 6c5f 7661 6c75  elf._actual_valu
+0001be50: 6573 290a 2020 2020 2020 2020 6c6f 6573  es).        loes
+0001be60: 735f 782c 206c 6f65 7373 5f79 203d 207a  s_x, loess_y = z
+0001be70: 6970 282a 6c6f 6573 735f 706f 696e 7473  ip(*loess_points
+0001be80: 290a 0a20 2020 2020 2020 2070 6c74 2e66  )..        plt.f
+0001be90: 6967 7572 6528 6669 6773 697a 653d 6669  igure(figsize=fi
+0001bea0: 6775 7265 5f73 697a 6529 0a20 2020 2020  gure_size).     
+0001beb0: 2020 2070 6c74 2e70 6c6f 7428 6c6f 6573     plt.plot(loes
+0001bec0: 735f 782c 206c 6f65 7373 5f79 2c20 636f  s_x, loess_y, co
+0001bed0: 6c6f 723d 2772 272c 2061 6c70 6861 3d30  lor='r', alpha=0
+0001bee0: 2e35 2c20 6c61 6265 6c3d 274c 6f65 7373  .5, label='Loess
+0001bef0: 2028 5072 6564 6963 7469 6f6e 7320 7673   (Predictions vs
+0001bf00: 2041 6374 7561 6c73 2927 290a 2020 2020   Actuals)').    
+0001bf10: 2020 2020 706c 742e 706c 6f74 2873 656c      plt.plot(sel
+0001bf20: 662e 5f61 6374 7561 6c5f 7661 6c75 6573  f._actual_values
+0001bf30: 2c20 7365 6c66 2e5f 6163 7475 616c 5f76  , self._actual_v
+0001bf40: 616c 7565 732c 2063 6f6c 6f72 3d27 6227  alues, color='b'
+0001bf50: 2c20 616c 7068 613d 302e 352c 206c 6162  , alpha=0.5, lab
+0001bf60: 656c 3d27 5065 7266 6563 7420 5072 6564  el='Perfect Pred
+0001bf70: 6963 7469 6f6e 2729 0a20 2020 2020 2020  iction').       
+0001bf80: 2070 6c74 2e73 6361 7474 6572 2878 3d73   plt.scatter(x=s
+0001bf90: 656c 662e 5f61 6374 7561 6c5f 7661 6c75  elf._actual_valu
+0001bfa0: 6573 2c20 793d 7365 6c66 2e5f 7072 6564  es, y=self._pred
+0001bfb0: 6963 7465 645f 7661 6c75 6573 2c20 733d  icted_values, s=
+0001bfc0: 382c 2061 6c70 6861 3d30 2e35 290a 2020  8, alpha=0.5).  
+0001bfd0: 2020 2020 2020 706c 742e 7469 746c 6528        plt.title(
+0001bfe0: 2750 7265 6469 6374 6564 2056 616c 7565  'Predicted Value
+0001bff0: 7320 7673 2e20 4163 7475 616c 2056 616c  s vs. Actual Val
+0001c000: 7565 7327 290a 2020 2020 2020 2020 706c  ues').        pl
+0001c010: 742e 786c 6162 656c 2827 4163 7475 616c  t.xlabel('Actual
+0001c020: 7327 290a 2020 2020 2020 2020 706c 742e  s').        plt.
+0001c030: 796c 6162 656c 2827 5072 6564 6963 7465  ylabel('Predicte
+0001c040: 6427 290a 2020 2020 2020 2020 6178 6973  d').        axis
+0001c050: 203d 2070 6c74 2e67 6361 2829 0a20 2020   = plt.gca().   
+0001c060: 2020 2020 2068 616e 646c 6573 2c20 6c61       handles, la
+0001c070: 6265 6c73 203d 2061 7869 732e 6765 745f  bels = axis.get_
+0001c080: 6c65 6765 6e64 5f68 616e 646c 6573 5f6c  legend_handles_l
+0001c090: 6162 656c 7328 290a 2020 2020 2020 2020  abels().        
+0001c0a0: 6178 6973 2e6c 6567 656e 6428 6861 6e64  axis.legend(hand
+0001c0b0: 6c65 732c 206c 6162 656c 7329 0a20 2020  les, labels).   
+0001c0c0: 2020 2020 2070 6c74 2e66 6967 7465 7874       plt.figtext
+0001c0d0: 2830 2e39 392c 2030 2e30 312c 0a20 2020  (0.99, 0.01,.   
+0001c0e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001c0f0: 2027 4e6f 7465 3a20 6f62 7365 7276 6174   'Note: observat
+0001c100: 696f 6e73 2061 626f 7665 2062 6c75 6520  ions above blue 
+0001c110: 6c69 6e65 206d 6561 6e20 6d6f 6465 6c20  line mean model 
+0001c120: 6973 206f 7665 722d 7072 6564 6963 7469  is over-predicti
+0001c130: 6e67 3b20 6265 6c6f 7720 6d65 616e 7320  ng; below means 
+0001c140: 756e 6465 722d 270a 2020 2020 2020 2020  under-'.        
+0001c150: 2020 2020 2020 2020 2020 2020 2770 7265              'pre
+0001c160: 6469 6374 696e 672e 272c 2020 2320 6e6f  dicting.',  # no
+0001c170: 7161 0a20 2020 2020 2020 2020 2020 2020  qa.             
+0001c180: 2020 2020 2020 2068 6f72 697a 6f6e 7461         horizonta
+0001c190: 6c61 6c69 676e 6d65 6e74 3d27 7269 6768  lalignment='righ
+0001c1a0: 7427 290a 2020 2020 2020 2020 7265 7475  t').        retu
+0001c1b0: 726e 2061 7869 730a 0a20 2020 2064 6566  rn axis..    def
+0001c1c0: 2070 6c6f 745f 7265 7369 6475 616c 735f   plot_residuals_
+0001c1d0: 7673 5f61 6374 7561 6c73 2873 656c 662c  vs_actuals(self,
+0001c1e0: 2066 6967 7572 655f 7369 7a65 3a20 7475   figure_size: tu
+0001c1f0: 706c 6520 3d20 5354 414e 4441 5244 5f57  ple = STANDARD_W
+0001c200: 4944 5448 5f48 4549 4748 5429 3a0a 2020  IDTH_HEIGHT):.  
+0001c210: 2020 2020 2020 2222 2250 6c6f 7473 2072        """Plots r
+0001c220: 6573 6964 7561 6c73 2076 7320 6163 7475  esiduals vs actu
+0001c230: 616c 7320 7661 6c75 6573 0a0a 2020 2020  als values..    
+0001c240: 2020 2020 4172 6773 3a0a 2020 2020 2020      Args:.      
+0001c250: 2020 2020 2020 6669 6775 7265 5f73 697a        figure_siz
+0001c260: 653a 0a20 2020 2020 2020 2020 2020 2020  e:.             
+0001c270: 2020 2074 7570 6c65 2063 6f6e 7461 696e     tuple contain
+0001c280: 696e 6720 6028 7769 6474 682c 2068 6569  ing `(width, hei
+0001c290: 6768 7429 6020 6f66 2070 6c6f 742e 2054  ght)` of plot. T
+0001c2a0: 6865 2064 6566 6175 6c74 2068 6569 6768  he default heigh
+0001c2b0: 7420 6973 2064 6566 696e 6564 2062 790a  t is defined by.
+0001c2c0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001c2d0: 6068 656c 7073 6b2e 706c 6f74 2e53 5441  `helpsk.plot.STA
+0001c2e0: 4e44 4152 445f 4845 4947 4854 602c 2061  NDARD_HEIGHT`, a
+0001c2f0: 6e64 2074 6865 2064 6566 6175 6c74 2077  nd the default w
+0001c300: 6964 7468 2069 730a 2020 2020 2020 2020  idth is.        
+0001c310: 2020 2020 2020 2020 6068 656c 7073 6b2e          `helpsk.
+0001c320: 706c 6f74 2e53 5441 4e44 4152 445f 4845  plot.STANDARD_HE
+0001c330: 4947 4854 202f 2068 656c 7073 6b2e 706c  IGHT / helpsk.pl
+0001c340: 6f74 2e47 4f4c 4445 4e5f 5241 5449 4f60  ot.GOLDEN_RATIO`
+0001c350: 0a20 2020 2020 2020 2022 2222 0a20 2020  .        """.   
+0001c360: 2020 2020 206c 6f77 6573 7320 3d20 736d       lowess = sm
+0001c370: 2e6e 6f6e 7061 7261 6d65 7472 6963 2e6c  .nonparametric.l
+0001c380: 6f77 6573 730a 2020 2020 2020 2020 6c6f  owess.        lo
+0001c390: 6573 735f 706f 696e 7473 203d 206c 6f77  ess_points = low
+0001c3a0: 6573 7328 7365 6c66 2e5f 7265 7369 6475  ess(self._residu
+0001c3b0: 616c 732c 2073 656c 662e 5f61 6374 7561  als, self._actua
+0001c3c0: 6c5f 7661 6c75 6573 290a 2020 2020 2020  l_values).      
+0001c3d0: 2020 6c6f 6573 735f 782c 206c 6f65 7373    loess_x, loess
+0001c3e0: 5f79 203d 207a 6970 282a 6c6f 6573 735f  _y = zip(*loess_
+0001c3f0: 706f 696e 7473 290a 0a20 2020 2020 2020  points)..       
+0001c400: 2070 6c74 2e66 6967 7572 6528 6669 6773   plt.figure(figs
+0001c410: 697a 653d 6669 6775 7265 5f73 697a 6529  ize=figure_size)
+0001c420: 0a20 2020 2020 2020 2070 6c74 2e70 6c6f  .        plt.plo
+0001c430: 7428 6c6f 6573 735f 782c 206c 6f65 7373  t(loess_x, loess
+0001c440: 5f79 2c20 636f 6c6f 723d 2772 2729 0a20  _y, color='r'). 
+0001c450: 2020 2020 2020 2070 6c74 2e73 6361 7474         plt.scatt
+0001c460: 6572 2878 3d73 656c 662e 5f61 6374 7561  er(x=self._actua
+0001c470: 6c5f 7661 6c75 6573 2c20 793d 7365 6c66  l_values, y=self
+0001c480: 2e5f 7265 7369 6475 616c 732c 2073 3d38  ._residuals, s=8
+0001c490: 2c20 616c 7068 613d 302e 3529 0a20 2020  , alpha=0.5).   
+0001c4a0: 2020 2020 2070 6c74 2e74 6974 6c65 2827       plt.title('
+0001c4b0: 5265 7369 6475 616c 7320 7673 2e20 4163  Residuals vs. Ac
+0001c4c0: 7475 616c 2056 616c 7565 7327 290a 2020  tual Values').  
+0001c4d0: 2020 2020 2020 706c 742e 786c 6162 656c        plt.xlabel
+0001c4e0: 2827 4163 7475 616c 2729 0a20 2020 2020  ('Actual').     
+0001c4f0: 2020 2070 6c74 2e79 6c61 6265 6c28 2752     plt.ylabel('R
+0001c500: 6573 6964 7561 6c73 2028 4163 7475 616c  esiduals (Actual
+0001c510: 202d 2050 7265 6469 6374 6564 2927 290a   - Predicted)').
+0001c520: 2020 2020 2020 2020 706c 742e 6669 6774          plt.figt
+0001c530: 6578 7428 302e 3939 2c20 302e 3031 2c0a  ext(0.99, 0.01,.
+0001c540: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001c550: 2020 2020 274e 6f74 653a 2041 6374 7561      'Note: Actua
+0001c560: 6c20 3e20 5072 6564 6963 7465 6420 3d3e  l > Predicted =>
+0001c570: 2055 6e64 6572 2d70 7265 6469 6374 696e   Under-predictin
+0001c580: 6720 2870 6f73 6974 6976 6520 7265 7369  g (positive resi
+0001c590: 6475 616c 293b 206e 6567 6174 6976 6520  dual); negative 
+0001c5a0: 7265 7369 6475 616c 7320 270a 2020 2020  residuals '.    
+0001c5b0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001c5c0: 276d 6561 6e20 6f76 6572 2d70 7265 6469  'mean over-predi
+0001c5d0: 6374 696e 6727 2c20 2023 206e 6f71 610a  cting',  # noqa.
+0001c5e0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001c5f0: 2020 2020 686f 7269 7a6f 6e74 616c 616c      horizontalal
+0001c600: 6967 6e6d 656e 743d 2772 6967 6874 2729  ignment='right')
+0001c610: 0a0a 0a63 6c61 7373 2054 776f 436c 6173  ...class TwoClas
+0001c620: 734d 6f64 656c 436f 6d70 6172 6973 6f6e  sModelComparison
+0001c630: 3a0a 2020 2020 2222 2254 6869 7320 636c  :.    """This cl
+0001c640: 6173 7320 636f 6d70 6172 6573 206d 756c  ass compares mul
+0001c650: 7469 706c 6520 6d6f 6465 6c73 2074 7261  tiple models tra
+0001c660: 696e 6564 206f 6e20 5477 6f20 436c 6173  ined on Two Clas
+0001c670: 7320 2869 2e65 2e20 3027 732f 3127 7329  s (i.e. 0's/1's)
+0001c680: 2070 7265 6469 6374 696f 6e20 7363 656e   prediction scen
+0001c690: 6172 696f 732e 2222 220a 0a20 2020 2023  arios."""..    #
+0001c6a0: 2070 796c 696e 743a 2064 6973 6162 6c65   pylint: disable
+0001c6b0: 3d74 6f6f 2d6d 616e 792d 6172 6775 6d65  =too-many-argume
+0001c6c0: 6e74 730a 2020 2020 6465 6620 5f5f 696e  nts.    def __in
+0001c6d0: 6974 5f5f 2873 656c 662c 0a20 2020 2020  it__(self,.     
+0001c6e0: 2020 2020 2020 2020 2020 2020 6163 7475              actu
+0001c6f0: 616c 5f76 616c 7565 733a 206e 702e 6e64  al_values: np.nd
+0001c700: 6172 7261 792c 0a20 2020 2020 2020 2020  array,.         
+0001c710: 2020 2020 2020 2020 7072 6564 6963 7465          predicte
+0001c720: 645f 7363 6f72 6573 3a20 4469 6374 5b73  d_scores: Dict[s
+0001c730: 7472 2c20 6e70 2e6e 6461 7272 6179 5d2c  tr, np.ndarray],
+0001c740: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001c750: 2020 706f 7369 7469 7665 5f63 6c61 7373    positive_class
+0001c760: 3a20 7374 7220 3d20 2750 6f73 6974 6976  : str = 'Positiv
+0001c770: 6520 436c 6173 7327 2c0a 2020 2020 2020  e Class',.      
+0001c780: 2020 2020 2020 2020 2020 206e 6567 6174             negat
+0001c790: 6976 655f 636c 6173 733a 2073 7472 203d  ive_class: str =
+0001c7a0: 2027 4e65 6761 7469 7665 2043 6c61 7373   'Negative Class
+0001c7b0: 272c 0a20 2020 2020 2020 2020 2020 2020  ',.             
+0001c7c0: 2020 2020 7363 6f72 655f 7468 7265 7368      score_thresh
+0001c7d0: 6f6c 643a 2066 6c6f 6174 203d 2030 2e35  old: float = 0.5
+0001c7e0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001c7f0: 2020 293a 0a20 2020 2020 2020 2022 2222    ):.        """
+0001c800: 0a20 2020 2020 2020 2041 7267 733a 0a20  .        Args:. 
+0001c810: 2020 2020 2020 2020 2020 2061 6374 7561             actua
+0001c820: 6c5f 7661 6c75 6573 3a0a 2020 2020 2020  l_values:.      
+0001c830: 2020 2020 2020 2020 2020 6172 7261 7920            array 
+0001c840: 6f66 2030 2773 2061 6e64 2031 2773 0a20  of 0's and 1's. 
+0001c850: 2020 2020 2020 2020 2020 2070 7265 6469             predi
+0001c860: 6374 6564 5f73 636f 7265 733a 0a20 2020  cted_scores:.   
+0001c870: 2020 2020 2020 2020 2020 2020 2064 6963               dic
+0001c880: 7469 6f6e 6172 7920 7065 7220 6d6f 6465  tionary per mode
+0001c890: 6c20 7769 7468 206b 6579 2061 7320 7468  l with key as th
+0001c8a0: 6520 6e61 6d65 206f 6620 7468 6520 6d6f  e name of the mo
+0001c8b0: 6465 6c20 616e 6420 7661 6c75 6520 7468  del and value th
+0001c8c0: 6174 2069 7320 616e 2061 7272 6179 206f  at is an array o
+0001c8d0: 660a 2020 2020 2020 2020 2020 2020 2020  f.              
+0001c8e0: 2020 6465 6369 6d61 6c2f 666c 6f61 7420    decimal/float 
+0001c8f0: 7661 6c75 6573 2066 726f 6d20 6070 7265  values from `pre
+0001c900: 6469 6374 5f70 726f 6261 2829 603b 204e  dict_proba()`; N
+0001c910: 4f54 2074 6865 2061 6374 7561 6c20 636c  OT the actual cl
+0001c920: 6173 730a 2020 2020 2020 2020 2020 2020  ass.            
+0001c930: 706f 7369 7469 7665 5f63 6c61 7373 3a0a  positive_class:.
+0001c940: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001c950: 7374 7269 6e67 206f 6620 7468 6520 6e61  string of the na
+0001c960: 6d65 2f6c 6162 656c 206f 6620 7468 6520  me/label of the 
+0001c970: 706f 7369 7469 7665 2063 6c61 7373 2028  positive class (
+0001c980: 692e 652e 2076 616c 7565 206f 6620 3129  i.e. value of 1)
+0001c990: 2e20 496e 206f 7468 6572 2077 6f72 6473  . In other words
+0001c9a0: 2c20 6e6f 740a 2020 2020 2020 2020 2020  , not.          
+0001c9b0: 2020 2020 2020 2770 6f73 6974 6976 6527        'positive'
+0001c9c0: 2069 6e20 7468 6520 7365 6e73 6520 6f66   in the sense of
+0001c9d0: 2027 676f 6f64 2720 6275 7420 2770 6f73   'good' but 'pos
+0001c9e0: 6974 6976 6527 2061 7320 696e 2027 5472  itive' as in 'Tr
+0001c9f0: 7565 2f46 616c 7365 2050 6f73 6974 6976  ue/False Positiv
+0001ca00: 6527 2e0a 2020 2020 2020 2020 2020 2020  e'..            
+0001ca10: 6e65 6761 7469 7665 5f63 6c61 7373 3a0a  negative_class:.
+0001ca20: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001ca30: 7374 7269 6e67 206f 6620 7468 6520 6e61  string of the na
+0001ca40: 6d65 2f6c 6162 656c 206f 6620 7468 6520  me/label of the 
+0001ca50: 6e65 6761 7469 7665 2063 6c61 7373 2028  negative class (
+0001ca60: 692e 652e 2076 616c 7565 206f 6620 3029  i.e. value of 0)
+0001ca70: 2e20 496e 206f 7468 6572 2077 6f72 6473  . In other words
+0001ca80: 2c20 6e6f 740a 2020 2020 2020 2020 2020  , not.          
+0001ca90: 2020 2020 2020 276e 6567 6174 6976 6527        'negative'
+0001caa0: 2069 6e20 7468 6520 7365 6e73 6520 6f66   in the sense of
+0001cab0: 2027 676f 6f64 2720 6275 7420 276e 6567   'good' but 'neg
+0001cac0: 6174 6976 6527 2061 7320 696e 2027 5472  ative' as in 'Tr
+0001cad0: 7565 2f46 616c 7365 204e 6567 6174 6976  ue/False Negativ
+0001cae0: 6527 2e0a 2020 2020 2020 2020 2020 2020  e'..            
+0001caf0: 7363 6f72 655f 7468 7265 7368 6f6c 643a  score_threshold:
+0001cb00: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001cb10: 2074 6865 2073 636f 7265 2f70 726f 6261   the score/proba
+0001cb20: 6269 6c69 7479 2074 6872 6573 686f 6c64  bility threshold
+0001cb30: 2066 6f72 2074 7572 6e69 6e67 2073 636f   for turning sco
+0001cb40: 7265 7320 696e 746f 2030 2773 2061 6e64  res into 0's and
+0001cb50: 2031 2773 2061 6e64 2063 6f72 7265 7370   1's and corresp
+0001cb60: 6f6e 6469 6e67 206c 6162 656c 730a 2020  onding labels.  
+0001cb70: 2020 2020 2020 2222 220a 2020 2020 2020        """.      
+0001cb80: 2020 6173 7365 7274 2069 7369 6e73 7461    assert isinsta
+0001cb90: 6e63 6528 7072 6564 6963 7465 645f 7363  nce(predicted_sc
+0001cba0: 6f72 6573 2c20 6469 6374 290a 0a20 2020  ores, dict)..   
+0001cbb0: 2020 2020 2066 6f72 2076 616c 7565 7320       for values 
+0001cbc0: 696e 2070 7265 6469 6374 6564 5f73 636f  in predicted_sco
+0001cbd0: 7265 732e 7661 6c75 6573 2829 3a0a 2020  res.values():.  
+0001cbe0: 2020 2020 2020 2020 2020 6173 7365 7274            assert
+0001cbf0: 206c 656e 2861 6374 7561 6c5f 7661 6c75   len(actual_valu
+0001cc00: 6573 2920 3d3d 206c 656e 2876 616c 7565  es) == len(value
+0001cc10: 7329 0a0a 2020 2020 2020 2020 7365 6c66  s)..        self
+0001cc20: 2e5f 706f 7369 7469 7665 5f63 6c61 7373  ._positive_class
+0001cc30: 203d 2070 6f73 6974 6976 655f 636c 6173   = positive_clas
+0001cc40: 730a 2020 2020 2020 2020 7365 6c66 2e5f  s.        self._
+0001cc50: 6e65 6761 7469 7665 5f63 6c61 7373 203d  negative_class =
+0001cc60: 206e 6567 6174 6976 655f 636c 6173 730a   negative_class.
+0001cc70: 2020 2020 2020 2020 7365 6c66 2e5f 6163          self._ac
+0001cc80: 7475 616c 5f76 616c 7565 7320 3d20 6163  tual_values = ac
+0001cc90: 7475 616c 5f76 616c 7565 730a 2020 2020  tual_values.    
+0001cca0: 2020 2020 7365 6c66 2e5f 7072 6564 6963      self._predic
+0001ccb0: 7465 645f 7363 6f72 6573 203d 2070 7265  ted_scores = pre
+0001ccc0: 6469 6374 6564 5f73 636f 7265 730a 2020  dicted_scores.  
+0001ccd0: 2020 2020 2020 7365 6c66 2e73 636f 7265        self.score
+0001cce0: 5f74 6872 6573 686f 6c64 203d 2073 636f  _threshold = sco
+0001ccf0: 7265 5f74 6872 6573 686f 6c64 0a0a 2020  re_threshold..  
+0001cd00: 2020 2020 2020 7365 6c66 2e5f 6576 616c        self._eval
+0001cd10: 7561 746f 7273 203d 207b 6b65 793a 2054  uators = {key: T
+0001cd20: 776f 436c 6173 7345 7661 6c75 6174 6f72  woClassEvaluator
+0001cd30: 2861 6374 7561 6c5f 7661 6c75 6573 3d61  (actual_values=a
+0001cd40: 6374 7561 6c5f 7661 6c75 6573 2c0a 2020  ctual_values,.  
+0001cd50: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001cd60: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001cd70: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001cd80: 2020 2020 2020 2070 7265 6469 6374 6564         predicted
-0001cd90: 5f73 636f 7265 733d 7661 6c75 652c 0a20  _scores=value,. 
+0001cd80: 2070 7265 6469 6374 6564 5f73 636f 7265   predicted_score
+0001cd90: 733d 7661 6c75 652c 0a20 2020 2020 2020  s=value,.       
 0001cda0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001cdb0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001cdc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001cdd0: 2020 706f 7369 7469 7665 5f63 6c61 7373    positive_class
-0001cde0: 3d70 6f73 6974 6976 655f 636c 6173 732c  =positive_class,
-0001cdf0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001cdc0: 2020 2020 2020 2020 2020 2020 706f 7369              posi
+0001cdd0: 7469 7665 5f63 6c61 7373 3d70 6f73 6974  tive_class=posit
+0001cde0: 6976 655f 636c 6173 732c 0a20 2020 2020  ive_class,.     
+0001cdf0: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001ce00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001ce10: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001ce20: 2020 2020 6e65 6761 7469 7665 5f63 6c61      negative_cla
-0001ce30: 7373 3d6e 6567 6174 6976 655f 636c 6173  ss=negative_clas
-0001ce40: 732c 0a20 2020 2020 2020 2020 2020 2020  s,.             
+0001ce10: 2020 2020 2020 2020 2020 2020 2020 6e65                ne
+0001ce20: 6761 7469 7665 5f63 6c61 7373 3d6e 6567  gative_class=neg
+0001ce30: 6174 6976 655f 636c 6173 732c 0a20 2020  ative_class,.   
+0001ce40: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001ce50: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001ce60: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001ce70: 2020 2020 2020 7363 6f72 655f 7468 7265        score_thre
-0001ce80: 7368 6f6c 643d 7363 6f72 655f 7468 7265  shold=score_thre
-0001ce90: 7368 6f6c 6429 0a20 2020 2020 2020 2020  shold).         
-0001cea0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001ceb0: 2020 2066 6f72 206b 6579 2c20 7661 6c75     for key, valu
-0001cec0: 6520 696e 2070 7265 6469 6374 6564 5f73  e in predicted_s
-0001ced0: 636f 7265 732e 6974 656d 7328 297d 0a0a  cores.items()}..
-0001cee0: 2020 2020 6465 6620 616c 6c5f 6d65 7472      def all_metr
-0001cef0: 6963 735f 6466 2873 656c 662c 0a20 2020  ics_df(self,.   
-0001cf00: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001cf10: 2020 2020 6475 6d6d 795f 636c 6173 7369      dummy_classi
-0001cf20: 6669 6572 5f73 7472 6174 6567 793a 2055  fier_strategy: U
-0001cf30: 6e69 6f6e 5b73 7472 2c20 6c69 7374 2c20  nion[str, list, 
-0001cf40: 4e6f 6e65 5d20 3d20 2770 7269 6f72 272c  None] = 'prior',
-0001cf50: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001cf60: 2020 2020 2020 2020 6475 6d6d 795f 636c          dummy_cl
-0001cf70: 6173 7369 6669 6572 5f63 6f6e 7374 616e  assifier_constan
-0001cf80: 743a 2055 6e69 6f6e 5b69 6e74 5d20 3d20  t: Union[int] = 
-0001cf90: 312c 0a20 2020 2020 2020 2020 2020 2020  1,.             
-0001cfa0: 2020 2020 2020 2020 2020 7265 7475 726e            return
-0001cfb0: 5f73 7479 6c65 3a20 626f 6f6c 203d 2046  _style: bool = F
-0001cfc0: 616c 7365 2c0a 2020 2020 2020 2020 2020  alse,.          
-0001cfd0: 2020 2020 2020 2020 2020 2020 2072 6f75               rou
-0001cfe0: 6e64 5f62 793a 204f 7074 696f 6e61 6c5b  nd_by: Optional[
-0001cff0: 696e 745d 203d 204e 6f6e 6529 202d 3e20  int] = None) -> 
-0001d000: 556e 696f 6e5b 7064 2e44 6174 6146 7261  Union[pd.DataFra
-0001d010: 6d65 2c20 5374 796c 6572 5d3a 0a20 2020  me, Styler]:.   
-0001d020: 2020 2020 2022 2222 416c 6c20 6f66 2074       """All of t
-0001d030: 6865 206d 6574 7269 6373 2061 7265 2072  he metrics are r
-0001d040: 6574 7572 6e65 6420 6173 2061 2044 6174  eturned as a Dat
-0001d050: 6146 7261 6d65 2e0a 0a20 2020 2020 2020  aFrame...       
-0001d060: 2041 7267 733a 0a20 2020 2020 2020 2020   Args:.         
-0001d070: 2020 2064 756d 6d79 5f63 6c61 7373 6966     dummy_classif
-0001d080: 6965 725f 7374 7261 7465 6779 3a0a 2020  ier_strategy:.  
-0001d090: 2020 2020 2020 2020 2020 2020 2020 6966                if
-0001d0a0: 206e 6f74 204e 6f6e 652c 2074 6865 6e20   not None, then 
-0001d0b0: 7265 7475 726e 7320 636f 6c75 6d6e 2873  returns column(s
-0001d0c0: 2920 636f 7272 6573 706f 6e64 696e 6720  ) corresponding 
-0001d0d0: 746f 2074 6865 2073 636f 7265 7320 6672  to the scores fr
-0001d0e0: 6f6d 2070 7265 6469 6374 696f 6e73 206f  om predictions o
-0001d0f0: 660a 2020 2020 2020 2020 2020 2020 2020  f.              
-0001d100: 2020 736b 6c65 6172 6e2e 6475 6d6d 792e    sklearn.dummy.
-0001d110: 4475 6d6d 7943 6c61 7373 6966 6965 722c  DummyClassifier,
-0001d120: 2062 6173 6564 206f 6e20 7468 6520 7374   based on the st
-0001d130: 7261 7465 6779 2028 6f72 2073 7472 6174  rategy (or strat
-0001d140: 6567 6965 7329 2070 726f 7669 6465 642e  egies) provided.
-0001d150: 2056 616c 6964 2076 616c 7565 730a 2020   Valid values.  
-0001d160: 2020 2020 2020 2020 2020 2020 2020 636f                co
-0001d170: 7272 6573 706f 6e64 2074 6f20 7661 6c75  rrespond to valu
-0001d180: 6573 206f 6620 6073 7472 6174 6567 7960  es of `strategy`
-0001d190: 2070 6172 616d 6574 6572 206c 6973 7465   parameter liste
-0001d1a0: 640a 2020 2020 2020 2020 2020 2020 2020  d.              
-0001d1b0: 2020 6874 7470 733a 2f2f 7363 696b 6974    https://scikit
-0001d1c0: 2d6c 6561 726e 2e6f 7267 2f73 7461 626c  -learn.org/stabl
-0001d1d0: 652f 6d6f 6475 6c65 732f 6765 6e65 7261  e/modules/genera
-0001d1e0: 7465 642f 736b 6c65 6172 6e2e 6475 6d6d  ted/sklearn.dumm
-0001d1f0: 792e 4475 6d6d 7943 6c61 7373 6966 6965  y.DummyClassifie
-0001d200: 722e 6874 6d6c 0a0a 2020 2020 2020 2020  r.html..        
-0001d210: 2020 2020 2020 2020 4966 2061 206c 6973          If a lis
-0001d220: 7420 6973 2070 6173 7365 6420 696e 2028  t is passed in (
-0001d230: 652e 672e 205b 2770 7269 6f72 272c 2027  e.g. ['prior', '
-0001d240: 756e 6966 6f72 6d27 5d2c 2074 6865 6e20  uniform'], then 
-0001d250: 6f6e 6520 7363 6f72 6520 636f 6c75 6d6e  one score column
-0001d260: 2070 6572 2076 616c 7565 2069 730a 2020   per value is.  
-0001d270: 2020 2020 2020 2020 2020 2020 2020 6164                ad
-0001d280: 6465 642e 0a0a 2020 2020 2020 2020 2020  ded...          
-0001d290: 2020 2020 2020 4966 204e 6f6e 6520 6973        If None is
-0001d2a0: 2070 6173 7365 642c 2074 6865 6e20 6e6f   passed, then no
-0001d2b0: 2061 6464 6974 696f 6e61 6c20 636f 6c75   additional colu
-0001d2c0: 6d6e 7320 6172 6520 6164 6465 642e 0a20  mns are added.. 
-0001d2d0: 2020 2020 2020 2020 2020 2064 756d 6d79             dummy
-0001d2e0: 5f63 6c61 7373 6966 6965 725f 636f 6e73  _classifier_cons
-0001d2f0: 7461 6e74 3a0a 2020 2020 2020 2020 2020  tant:.          
-0001d300: 2020 2020 2020 5468 6520 6578 706c 6963        The explic
-0001d310: 6974 2063 6f6e 7374 616e 7420 6173 2070  it constant as p
-0001d320: 7265 6469 6374 6564 2062 7920 7468 6520  redicted by the 
-0001d330: e280 9c63 6f6e 7374 616e 74e2 809d 2073  ...constant... s
-0001d340: 7472 6174 6567 7920 666f 7220 7468 650a  trategy for the.
-0001d350: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001d360: 4475 6d6d 7943 6c61 7373 6966 6965 722e  DummyClassifier.
-0001d370: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001d380: 2054 6869 7320 7061 7261 6d65 7465 7220   This parameter 
-0001d390: 6973 2075 7365 6675 6c20 6f6e 6c79 2066  is useful only f
-0001d3a0: 6f72 2074 6865 20e2 809c 636f 6e73 7461  or the ...consta
-0001d3b0: 6e74 e280 9d20 6475 6d6d 795f 636c 6173  nt... dummy_clas
-0001d3c0: 7369 6669 6572 5f73 7472 6174 6567 792e  sifier_strategy.
-0001d3d0: 0a20 2020 2020 2020 2020 2020 2072 6574  .            ret
-0001d3e0: 7572 6e5f 7374 796c 653a 0a20 2020 2020  urn_style:.     
-0001d3f0: 2020 2020 2020 2020 2020 2069 6620 5472             if Tr
-0001d400: 7565 2c20 7265 7475 726e 2073 7479 6c65  ue, return style
-0001d410: 7220 6f62 6a65 6374 3b20 656c 7365 2072  r object; else r
-0001d420: 6574 7572 6e20 6461 7461 6672 616d 650a  eturn dataframe.
-0001d430: 2020 2020 2020 2020 2020 2020 726f 756e              roun
-0001d440: 645f 6279 3a0a 2020 2020 2020 2020 2020  d_by:.          
-0001d450: 2020 2020 2020 7468 6520 6e75 6d62 6572        the number
-0001d460: 206f 6620 6469 6769 7473 2074 6f20 726f   of digits to ro
-0001d470: 756e 6420 6279 3b20 6966 204e 6f6e 652c  und by; if None,
-0001d480: 2074 6865 6e20 646f 6e27 7420 726f 756e   then don't roun
-0001d490: 640a 2020 2020 2020 2020 2222 220a 0a20  d.        """.. 
-0001d4a0: 2020 2020 2020 2072 6573 756c 7420 3d20         result = 
-0001d4b0: 4e6f 6e65 0a20 2020 2020 2020 206c 6173  None.        las
-0001d4c0: 745f 6b65 7920 3d20 6c69 7374 2873 656c  t_key = list(sel
-0001d4d0: 662e 5f65 7661 6c75 6174 6f72 732e 6b65  f._evaluators.ke
-0001d4e0: 7973 2829 295b 2d31 5d0a 0a20 2020 2020  ys())[-1]..     
-0001d4f0: 2020 2066 6f72 206b 6579 2c20 7661 6c75     for key, valu
-0001d500: 6520 696e 2073 656c 662e 5f65 7661 6c75  e in self._evalu
-0001d510: 6174 6f72 732e 6974 656d 7328 293a 0a20  ators.items():. 
-0001d520: 2020 2020 2020 2020 2020 2064 756d 6d79             dummy
-0001d530: 5f73 7472 6174 6567 7920 3d20 6475 6d6d  _strategy = dumm
-0001d540: 795f 636c 6173 7369 6669 6572 5f73 7472  y_classifier_str
-0001d550: 6174 6567 7920 6966 206b 6579 203d 3d20  ategy if key == 
-0001d560: 6c61 7374 5f6b 6579 2065 6c73 6520 4e6f  last_key else No
-0001d570: 6e65 0a0a 2020 2020 2020 2020 2020 2020  ne..            
-0001d580: 7363 6f72 6573 203d 2076 616c 7565 2e61  scores = value.a
-0001d590: 6c6c 5f6d 6574 7269 6373 5f64 6628 0a20  ll_metrics_df(. 
-0001d5a0: 2020 2020 2020 2020 2020 2020 2020 2072                 r
-0001d5b0: 6574 7572 6e5f 6578 706c 616e 6174 696f  eturn_explanatio
-0001d5c0: 6e73 3d46 616c 7365 2c0a 2020 2020 2020  ns=False,.      
-0001d5d0: 2020 2020 2020 2020 2020 6475 6d6d 795f            dummy_
-0001d5e0: 636c 6173 7369 6669 6572 5f73 7472 6174  classifier_strat
-0001d5f0: 6567 793d 6475 6d6d 795f 7374 7261 7465  egy=dummy_strate
-0001d600: 6779 2c0a 2020 2020 2020 2020 2020 2020  gy,.            
-0001d610: 2020 2020 6475 6d6d 795f 636c 6173 7369      dummy_classi
-0001d620: 6669 6572 5f63 6f6e 7374 616e 743d 6475  fier_constant=du
-0001d630: 6d6d 795f 636c 6173 7369 6669 6572 5f63  mmy_classifier_c
-0001d640: 6f6e 7374 616e 740a 2020 2020 2020 2020  onstant.        
-0001d650: 2020 2020 290a 2020 2020 2020 2020 2020      ).          
-0001d660: 2020 7363 6f72 6573 203d 2073 636f 7265    scores = score
-0001d670: 732e 7265 6e61 6d65 2863 6f6c 756d 6e73  s.rename(columns
-0001d680: 3d7b 2753 636f 7265 273a 206b 6579 7d29  ={'Score': key})
-0001d690: 0a20 2020 2020 2020 2020 2020 2072 6573  .            res
-0001d6a0: 756c 7420 3d20 7064 2e63 6f6e 6361 7428  ult = pd.concat(
-0001d6b0: 5b72 6573 756c 742c 2073 636f 7265 735d  [result, scores]
-0001d6c0: 2c20 6178 6973 3d31 290a 0a20 2020 2020  , axis=1)..     
-0001d6d0: 2020 2072 6573 756c 7420 3d20 7265 7375     result = resu
-0001d6e0: 6c74 2e6c 6f63 5b5b 0a20 2020 2020 2020  lt.loc[[.       
-0001d6f0: 2020 2020 2027 4155 4327 2c20 2746 3120       'AUC', 'F1 
-0001d700: 5363 6f72 6527 2c0a 2020 2020 2020 2020  Score',.        
-0001d710: 2020 2020 2754 7275 6520 506f 7369 7469      'True Positi
-0001d720: 7665 2052 6174 6527 2c20 2754 7275 6520  ve Rate', 'True 
-0001d730: 4e65 6761 7469 7665 2052 6174 6527 2c0a  Negative Rate',.
-0001d740: 2020 2020 2020 2020 2020 2020 2746 616c              'Fal
-0001d750: 7365 2050 6f73 6974 6976 6520 5261 7465  se Positive Rate
-0001d760: 272c 2027 4661 6c73 6520 4e65 6761 7469  ', 'False Negati
-0001d770: 7665 2052 6174 6527 2c0a 2020 2020 2020  ve Rate',.      
-0001d780: 2020 2020 2020 2750 6f73 6974 6976 6520        'Positive 
-0001d790: 5072 6564 6963 7469 7665 2056 616c 7565  Predictive Value
-0001d7a0: 272c 2027 4e65 6761 7469 7665 2050 7265  ', 'Negative Pre
-0001d7b0: 6469 6374 6976 6520 5661 6c75 6527 0a20  dictive Value'. 
-0001d7c0: 2020 2020 2020 205d 5d0a 0a20 2020 2020         ]]..     
-0001d7d0: 2020 2072 6573 756c 7420 3d20 7265 7375     result = resu
-0001d7e0: 6c74 2e74 7261 6e73 706f 7365 2829 0a0a  lt.transpose()..
-0001d7f0: 2020 2020 2020 2020 6966 2072 6f75 6e64          if round
-0001d800: 5f62 793a 0a20 2020 2020 2020 2020 2020  _by:.           
-0001d810: 2066 6f72 2063 6f6c 756d 6e20 696e 2072   for column in r
-0001d820: 6573 756c 742e 636f 6c75 6d6e 733a 0a20  esult.columns:. 
-0001d830: 2020 2020 2020 2020 2020 2020 2020 2072                 r
-0001d840: 6573 756c 745b 636f 6c75 6d6e 5d20 3d20  esult[column] = 
-0001d850: 7265 7375 6c74 5b63 6f6c 756d 6e5d 2e72  result[column].r
-0001d860: 6f75 6e64 2872 6f75 6e64 5f62 7929 0a0a  ound(round_by)..
-0001d870: 2020 2020 2020 2020 6966 2072 6574 7572          if retur
-0001d880: 6e5f 7374 796c 653a 0a20 2020 2020 2020  n_style:.       
-0001d890: 2020 2020 2070 6f73 6974 6976 655f 7363       positive_sc
-0001d8a0: 6f72 6573 203d 205b 7820 666f 7220 7820  ores = [x for x 
-0001d8b0: 696e 2072 6573 756c 742e 636f 6c75 6d6e  in result.column
-0001d8c0: 7320 6966 206e 6f74 2078 2e73 7461 7274  s if not x.start
-0001d8d0: 7377 6974 6828 2746 616c 7365 2729 5d0a  swith('False')].
-0001d8e0: 2020 2020 2020 2020 2020 2020 6e65 6761              nega
-0001d8f0: 7469 7665 5f73 636f 7265 7320 3d20 5b78  tive_scores = [x
-0001d900: 2066 6f72 2078 2069 6e20 7265 7375 6c74   for x in result
-0001d910: 2e63 6f6c 756d 6e73 2069 6620 782e 7374  .columns if x.st
-0001d920: 6172 7473 7769 7468 2827 4661 6c73 6527  artswith('False'
-0001d930: 295d 0a0a 2020 2020 2020 2020 2020 2020  )]..            
-0001d940: 7265 7375 6c74 203d 2072 6573 756c 742e  result = result.
-0001d950: 7374 796c 650a 0a20 2020 2020 2020 2020  style..         
-0001d960: 2020 2069 6620 726f 756e 645f 6279 3a0a     if round_by:.
-0001d970: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001d980: 7265 7375 6c74 203d 2072 6573 756c 742e  result = result.
-0001d990: 666f 726d 6174 2870 7265 6369 7369 6f6e  format(precision
-0001d9a0: 3d72 6f75 6e64 5f62 7929 0a0a 2020 2020  =round_by)..    
-0001d9b0: 2020 2020 2020 2020 7265 7375 6c74 203d          result =
-0001d9c0: 2072 6573 756c 742e 205c 0a20 2020 2020   result. \.     
-0001d9d0: 2020 2020 2020 2020 2020 2062 6172 2873             bar(s
-0001d9e0: 7562 7365 743d 706f 7369 7469 7665 5f73  ubset=positive_s
-0001d9f0: 636f 7265 732c 2063 6f6c 6f72 3d68 636f  cores, color=hco
-0001da00: 6c6f 722e 436f 6c6f 7273 2e50 4947 4d45  lor.Colors.PIGME
-0001da10: 4e54 5f47 5245 454e 2e76 616c 7565 2c20  NT_GREEN.value, 
-0001da20: 766d 696e 3d30 2c20 766d 6178 3d31 292e  vmin=0, vmax=1).
-0001da30: 205c 0a20 2020 2020 2020 2020 2020 2020   \.             
-0001da40: 2020 2062 6172 2873 7562 7365 743d 6e65     bar(subset=ne
-0001da50: 6761 7469 7665 5f73 636f 7265 732c 2063  gative_scores, c
-0001da60: 6f6c 6f72 3d68 636f 6c6f 722e 436f 6c6f  olor=hcolor.Colo
-0001da70: 7273 2e50 4f50 5059 2e76 616c 7565 2c20  rs.POPPY.value, 
-0001da80: 766d 696e 3d30 2c20 766d 6178 3d31 290a  vmin=0, vmax=1).
-0001da90: 0a20 2020 2020 2020 2072 6574 7572 6e20  .        return 
-0001daa0: 7265 7375 6c74 0a0a 2020 2020 6465 6620  result..    def 
-0001dab0: 706c 6f74 5f6d 6574 7269 6373 5f63 6f6d  plot_metrics_com
-0001dac0: 7061 7269 736f 6e28 7365 6c66 2c0a 2020  parison(self,.  
+0001ce70: 7363 6f72 655f 7468 7265 7368 6f6c 643d  score_threshold=
+0001ce80: 7363 6f72 655f 7468 7265 7368 6f6c 6429  score_threshold)
+0001ce90: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001cea0: 2020 2020 2020 2020 2020 2020 2066 6f72               for
+0001ceb0: 206b 6579 2c20 7661 6c75 6520 696e 2070   key, value in p
+0001cec0: 7265 6469 6374 6564 5f73 636f 7265 732e  redicted_scores.
+0001ced0: 6974 656d 7328 297d 0a0a 2020 2020 6465  items()}..    de
+0001cee0: 6620 616c 6c5f 6d65 7472 6963 735f 6466  f all_metrics_df
+0001cef0: 2873 656c 662c 0a20 2020 2020 2020 2020  (self,.         
+0001cf00: 2020 2020 2020 2020 2020 2020 2020 6475                du
+0001cf10: 6d6d 795f 636c 6173 7369 6669 6572 5f73  mmy_classifier_s
+0001cf20: 7472 6174 6567 793a 2055 6e69 6f6e 5b73  trategy: Union[s
+0001cf30: 7472 2c20 6c69 7374 2c20 4e6f 6e65 5d20  tr, list, None] 
+0001cf40: 3d20 2770 7269 6f72 272c 0a20 2020 2020  = 'prior',.     
+0001cf50: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001cf60: 2020 6475 6d6d 795f 636c 6173 7369 6669    dummy_classifi
+0001cf70: 6572 5f63 6f6e 7374 616e 743a 2055 6e69  er_constant: Uni
+0001cf80: 6f6e 5b69 6e74 5d20 3d20 312c 0a20 2020  on[int] = 1,.   
+0001cf90: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001cfa0: 2020 2020 7265 7475 726e 5f73 7479 6c65      return_style
+0001cfb0: 3a20 626f 6f6c 203d 2046 616c 7365 2c0a  : bool = False,.
+0001cfc0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001cfd0: 2020 2020 2020 2072 6f75 6e64 5f62 793a         round_by:
+0001cfe0: 204f 7074 696f 6e61 6c5b 696e 745d 203d   Optional[int] =
+0001cff0: 204e 6f6e 6529 202d 3e20 556e 696f 6e5b   None) -> Union[
+0001d000: 7064 2e44 6174 6146 7261 6d65 2c20 5374  pd.DataFrame, St
+0001d010: 796c 6572 5d3a 0a20 2020 2020 2020 2022  yler]:.        "
+0001d020: 2222 416c 6c20 6f66 2074 6865 206d 6574  ""All of the met
+0001d030: 7269 6373 2061 7265 2072 6574 7572 6e65  rics are returne
+0001d040: 6420 6173 2061 2044 6174 6146 7261 6d65  d as a DataFrame
+0001d050: 2e0a 0a20 2020 2020 2020 2041 7267 733a  ...        Args:
+0001d060: 0a20 2020 2020 2020 2020 2020 2064 756d  .            dum
+0001d070: 6d79 5f63 6c61 7373 6966 6965 725f 7374  my_classifier_st
+0001d080: 7261 7465 6779 3a0a 2020 2020 2020 2020  rategy:.        
+0001d090: 2020 2020 2020 2020 6966 206e 6f74 204e          if not N
+0001d0a0: 6f6e 652c 2074 6865 6e20 7265 7475 726e  one, then return
+0001d0b0: 7320 636f 6c75 6d6e 2873 2920 636f 7272  s column(s) corr
+0001d0c0: 6573 706f 6e64 696e 6720 746f 2074 6865  esponding to the
+0001d0d0: 2073 636f 7265 7320 6672 6f6d 2070 7265   scores from pre
+0001d0e0: 6469 6374 696f 6e73 206f 660a 2020 2020  dictions of.    
+0001d0f0: 2020 2020 2020 2020 2020 2020 736b 6c65              skle
+0001d100: 6172 6e2e 6475 6d6d 792e 4475 6d6d 7943  arn.dummy.DummyC
+0001d110: 6c61 7373 6966 6965 722c 2062 6173 6564  lassifier, based
+0001d120: 206f 6e20 7468 6520 7374 7261 7465 6779   on the strategy
+0001d130: 2028 6f72 2073 7472 6174 6567 6965 7329   (or strategies)
+0001d140: 2070 726f 7669 6465 642e 2056 616c 6964   provided. Valid
+0001d150: 2076 616c 7565 730a 2020 2020 2020 2020   values.        
+0001d160: 2020 2020 2020 2020 636f 7272 6573 706f          correspo
+0001d170: 6e64 2074 6f20 7661 6c75 6573 206f 6620  nd to values of 
+0001d180: 6073 7472 6174 6567 7960 2070 6172 616d  `strategy` param
+0001d190: 6574 6572 206c 6973 7465 640a 2020 2020  eter listed.    
+0001d1a0: 2020 2020 2020 2020 2020 2020 6874 7470              http
+0001d1b0: 733a 2f2f 7363 696b 6974 2d6c 6561 726e  s://scikit-learn
+0001d1c0: 2e6f 7267 2f73 7461 626c 652f 6d6f 6475  .org/stable/modu
+0001d1d0: 6c65 732f 6765 6e65 7261 7465 642f 736b  les/generated/sk
+0001d1e0: 6c65 6172 6e2e 6475 6d6d 792e 4475 6d6d  learn.dummy.Dumm
+0001d1f0: 7943 6c61 7373 6966 6965 722e 6874 6d6c  yClassifier.html
+0001d200: 0a0a 2020 2020 2020 2020 2020 2020 2020  ..              
+0001d210: 2020 4966 2061 206c 6973 7420 6973 2070    If a list is p
+0001d220: 6173 7365 6420 696e 2028 652e 672e 205b  assed in (e.g. [
+0001d230: 2770 7269 6f72 272c 2027 756e 6966 6f72  'prior', 'unifor
+0001d240: 6d27 5d2c 2074 6865 6e20 6f6e 6520 7363  m'], then one sc
+0001d250: 6f72 6520 636f 6c75 6d6e 2070 6572 2076  ore column per v
+0001d260: 616c 7565 2069 730a 2020 2020 2020 2020  alue is.        
+0001d270: 2020 2020 2020 2020 6164 6465 642e 0a0a          added...
+0001d280: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001d290: 4966 204e 6f6e 6520 6973 2070 6173 7365  If None is passe
+0001d2a0: 642c 2074 6865 6e20 6e6f 2061 6464 6974  d, then no addit
+0001d2b0: 696f 6e61 6c20 636f 6c75 6d6e 7320 6172  ional columns ar
+0001d2c0: 6520 6164 6465 642e 0a20 2020 2020 2020  e added..       
+0001d2d0: 2020 2020 2064 756d 6d79 5f63 6c61 7373       dummy_class
+0001d2e0: 6966 6965 725f 636f 6e73 7461 6e74 3a0a  ifier_constant:.
+0001d2f0: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001d300: 5468 6520 6578 706c 6963 6974 2063 6f6e  The explicit con
+0001d310: 7374 616e 7420 6173 2070 7265 6469 6374  stant as predict
+0001d320: 6564 2062 7920 7468 6520 e280 9c63 6f6e  ed by the ...con
+0001d330: 7374 616e 74e2 809d 2073 7472 6174 6567  stant... strateg
+0001d340: 7920 666f 7220 7468 650a 2020 2020 2020  y for the.      
+0001d350: 2020 2020 2020 2020 2020 4475 6d6d 7943            DummyC
+0001d360: 6c61 7373 6966 6965 722e 0a20 2020 2020  lassifier..     
+0001d370: 2020 2020 2020 2020 2020 2054 6869 7320             This 
+0001d380: 7061 7261 6d65 7465 7220 6973 2075 7365  parameter is use
+0001d390: 6675 6c20 6f6e 6c79 2066 6f72 2074 6865  ful only for the
+0001d3a0: 20e2 809c 636f 6e73 7461 6e74 e280 9d20   ...constant... 
+0001d3b0: 6475 6d6d 795f 636c 6173 7369 6669 6572  dummy_classifier
+0001d3c0: 5f73 7472 6174 6567 792e 0a20 2020 2020  _strategy..     
+0001d3d0: 2020 2020 2020 2072 6574 7572 6e5f 7374         return_st
+0001d3e0: 796c 653a 0a20 2020 2020 2020 2020 2020  yle:.           
+0001d3f0: 2020 2020 2069 6620 5472 7565 2c20 7265       if True, re
+0001d400: 7475 726e 2073 7479 6c65 7220 6f62 6a65  turn styler obje
+0001d410: 6374 3b20 656c 7365 2072 6574 7572 6e20  ct; else return 
+0001d420: 6461 7461 6672 616d 650a 2020 2020 2020  dataframe.      
+0001d430: 2020 2020 2020 726f 756e 645f 6279 3a0a        round_by:.
+0001d440: 2020 2020 2020 2020 2020 2020 2020 2020                  
+0001d450: 7468 6520 6e75 6d62 6572 206f 6620 6469  the number of di
+0001d460: 6769 7473 2074 6f20 726f 756e 6420 6279  gits to round by
+0001d470: 3b20 6966 204e 6f6e 652c 2074 6865 6e20  ; if None, then 
+0001d480: 646f 6e27 7420 726f 756e 640a 2020 2020  don't round.    
+0001d490: 2020 2020 2222 220a 0a20 2020 2020 2020      """..       
+0001d4a0: 2072 6573 756c 7420 3d20 4e6f 6e65 0a20   result = None. 
+0001d4b0: 2020 2020 2020 206c 6173 745f 6b65 7920         last_key 
+0001d4c0: 3d20 6c69 7374 2873 656c 662e 5f65 7661  = list(self._eva
+0001d4d0: 6c75 6174 6f72 732e 6b65 7973 2829 295b  luators.keys())[
+0001d4e0: 2d31 5d0a 0a20 2020 2020 2020 2066 6f72  -1]..        for
+0001d4f0: 206b 6579 2c20 7661 6c75 6520 696e 2073   key, value in s
+0001d500: 656c 662e 5f65 7661 6c75 6174 6f72 732e  elf._evaluators.
+0001d510: 6974 656d 7328 293a 0a20 2020 2020 2020  items():.       
+0001d520: 2020 2020 2064 756d 6d79 5f73 7472 6174       dummy_strat
+0001d530: 6567 7920 3d20 6475 6d6d 795f 636c 6173  egy = dummy_clas
+0001d540: 7369 6669 6572 5f73 7472 6174 6567 7920  sifier_strategy 
+0001d550: 6966 206b 6579 203d 3d20 6c61 7374 5f6b  if key == last_k
+0001d560: 6579 2065 6c73 6520 4e6f 6e65 0a0a 2020  ey else None..  
+0001d570: 2020 2020 2020 2020 2020 7363 6f72 6573            scores
+0001d580: 203d 2076 616c 7565 2e61 6c6c 5f6d 6574   = value.all_met
+0001d590: 7269 6373 5f64 6628 0a20 2020 2020 2020  rics_df(.       
+0001d5a0: 2020 2020 2020 2020 2072 6574 7572 6e5f           return_
+0001d5b0: 6578 706c 616e 6174 696f 6e73 3d46 616c  explanations=Fal
+0001d5c0: 7365 2c0a 2020 2020 2020 2020 2020 2020  se,.            
+0001d5d0: 2020 2020 6475 6d6d 795f 636c 6173 7369      dummy_classi
+0001d5e0: 6669 6572 5f73 7472 6174 6567 793d 6475  fier_strategy=du
+0001d5f0: 6d6d 795f 7374 7261 7465 6779 2c0a 2020  mmy_strategy,.  
+0001d600: 2020 2020 2020 2020 2020 2020 2020 6475                du
+0001d610: 6d6d 795f 636c 6173 7369 6669 6572 5f63  mmy_classifier_c
+0001d620: 6f6e 7374 616e 743d 6475 6d6d 795f 636c  onstant=dummy_cl
+0001d630: 6173 7369 6669 6572 5f63 6f6e 7374 616e  assifier_constan
+0001d640: 740a 2020 2020 2020 2020 2020 2020 290a  t.            ).
+0001d650: 2020 2020 2020 2020 2020 2020 7363 6f72              scor
+0001d660: 6573 203d 2073 636f 7265 732e 7265 6e61  es = scores.rena
+0001d670: 6d65 2863 6f6c 756d 6e73 3d7b 2753 636f  me(columns={'Sco
+0001d680: 7265 273a 206b 6579 7d29 0a20 2020 2020  re': key}).     
+0001d690: 2020 2020 2020 2072 6573 756c 7420 3d20         result = 
+0001d6a0: 7064 2e63 6f6e 6361 7428 5b72 6573 756c  pd.concat([resul
+0001d6b0: 742c 2073 636f 7265 735d 2c20 6178 6973  t, scores], axis
+0001d6c0: 3d31 290a 0a20 2020 2020 2020 2072 6573  =1)..        res
+0001d6d0: 756c 7420 3d20 7265 7375 6c74 2e6c 6f63  ult = result.loc
+0001d6e0: 5b5b 0a20 2020 2020 2020 2020 2020 2027  [[.            '
+0001d6f0: 4155 4327 2c20 2746 3120 5363 6f72 6527  AUC', 'F1 Score'
+0001d700: 2c0a 2020 2020 2020 2020 2020 2020 2754  ,.            'T
+0001d710: 7275 6520 506f 7369 7469 7665 2052 6174  rue Positive Rat
+0001d720: 6527 2c20 2754 7275 6520 4e65 6761 7469  e', 'True Negati
+0001d730: 7665 2052 6174 6527 2c0a 2020 2020 2020  ve Rate',.      
+0001d740: 2020 2020 2020 2746 616c 7365 2050 6f73        'False Pos
+0001d750: 6974 6976 6520 5261 7465 272c 2027 4661  itive Rate', 'Fa
+0001d760: 6c73 6520 4e65 6761 7469 7665 2052 6174  lse Negative Rat
+0001d770: 6527 2c0a 2020 2020 2020 2020 2020 2020  e',.            
+0001d780: 2750 6f73 6974 6976 6520 5072 6564 6963  'Positive Predic
+0001d790: 7469 7665 2056 616c 7565 272c 2027 4e65  tive Value', 'Ne
+0001d7a0: 6761 7469 7665 2050 7265 6469 6374 6976  gative Predictiv
+0001d7b0: 6520 5661 6c75 6527 0a20 2020 2020 2020  e Value'.       
+0001d7c0: 205d 5d0a 0a20 2020 2020 2020 2072 6573   ]]..        res
+0001d7d0: 756c 7420 3d20 7265 7375 6c74 2e74 7261  ult = result.tra
+0001d7e0: 6e73 706f 7365 2829 0a0a 2020 2020 2020  nspose()..      
+0001d7f0: 2020 6966 2072 6f75 6e64 5f62 793a 0a20    if round_by:. 
+0001d800: 2020 2020 2020 2020 2020 2066 6f72 2063             for c
+0001d810: 6f6c 756d 6e20 696e 2072 6573 756c 742e  olumn in result.
+0001d820: 636f 6c75 6d6e 733a 0a20 2020 2020 2020  columns:.       
+0001d830: 2020 2020 2020 2020 2072 6573 756c 745b           result[
+0001d840: 636f 6c75 6d6e 5d20 3d20 7265 7375 6c74  column] = result
+0001d850: 5b63 6f6c 756d 6e5d 2e72 6f75 6e64 2872  [column].round(r
+0001d860: 6f75 6e64 5f62 7929 0a0a 2020 2020 2020  ound_by)..      
+0001d870: 2020 6966 2072 6574 7572 6e5f 7374 796c    if return_styl
+0001d880: 653a 0a20 2020 2020 2020 2020 2020 2070  e:.            p
+0001d890: 6f73 6974 6976 655f 7363 6f72 6573 203d  ositive_scores =
+0001d8a0: 205b 7820 666f 7220 7820 696e 2072 6573   [x for x in res
+0001d8b0: 756c 742e 636f 6c75 6d6e 7320 6966 206e  ult.columns if n
+0001d8c0: 6f74 2078 2e73 7461 7274 7377 6974 6828  ot x.startswith(
+0001d8d0: 2746 616c 7365 2729 5d0a 2020 2020 2020  'False')].      
+0001d8e0: 2020 2020 2020 6e65 6761 7469 7665 5f73        negative_s
+0001d8f0: 636f 7265 7320 3d20 5b78 2066 6f72 2078  cores = [x for x
+0001d900: 2069 6e20 7265 7375 6c74 2e63 6f6c 756d   in result.colum
+0001d910: 6e73 2069 6620 782e 7374 6172 7473 7769  ns if x.startswi
+0001d920: 7468 2827 4661 6c73 6527 295d 0a0a 2020  th('False')]..  
+0001d930: 2020 2020 2020 2020 2020 7265 7375 6c74            result
+0001d940: 203d 2072 6573 756c 742e 7374 796c 650a   = result.style.
+0001d950: 0a20 2020 2020 2020 2020 2020 2069 6620  .            if 
+0001d960: 726f 756e 645f 6279 3a0a 2020 2020 2020  round_by:.      
+0001d970: 2020 2020 2020 2020 2020 7265 7375 6c74            result
+0001d980: 203d 2072 6573 756c 742e 666f 726d 6174   = result.format
+0001d990: 2870 7265 6369 7369 6f6e 3d72 6f75 6e64  (precision=round
+0001d9a0: 5f62 7929 0a0a 2020 2020 2020 2020 2020  _by)..          
+0001d9b0: 2020 7265 7375 6c74 203d 2072 6573 756c    result = resul
+0001d9c0: 742e 205c 0a20 2020 2020 2020 2020 2020  t. \.           
+0001d9d0: 2020 2020 2062 6172 2873 7562 7365 743d       bar(subset=
+0001d9e0: 706f 7369 7469 7665 5f73 636f 7265 732c  positive_scores,
+0001d9f0: 2063 6f6c 6f72 3d68 636f 6c6f 722e 436f   color=hcolor.Co
+0001da00: 6c6f 7273 2e50 4947 4d45 4e54 5f47 5245  lors.PIGMENT_GRE
+0001da10: 454e 2e76 616c 7565 2c20 766d 696e 3d30  EN.value, vmin=0
+0001da20: 2c20 766d 6178 3d31 292e 205c 0a20 2020  , vmax=1). \.   
+0001da30: 2020 2020 2020 2020 2020 2020 2062 6172               bar
+0001da40: 2873 7562 7365 743d 6e65 6761 7469 7665  (subset=negative
+0001da50: 5f73 636f 7265 732c 2063 6f6c 6f72 3d68  _scores, color=h
+0001da60: 636f 6c6f 722e 436f 6c6f 7273 2e50 4f50  color.Colors.POP
+0001da70: 5059 2e76 616c 7565 2c20 766d 696e 3d30  PY.value, vmin=0
+0001da80: 2c20 766d 6178 3d31 290a 0a20 2020 2020  , vmax=1)..     
+0001da90: 2020 2072 6574 7572 6e20 7265 7375 6c74     return result
+0001daa0: 0a0a 2020 2020 6465 6620 706c 6f74 5f6d  ..    def plot_m
+0001dab0: 6574 7269 6373 5f63 6f6d 7061 7269 736f  etrics_compariso
+0001dac0: 6e28 7365 6c66 2c0a 2020 2020 2020 2020  n(self,.        
 0001dad0: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001dae0: 2020 2020 2020 2020 2020 2020 2020 6475                du
-0001daf0: 6d6d 795f 636c 6173 7369 6669 6572 5f73  mmy_classifier_s
-0001db00: 7472 6174 6567 793a 2055 6e69 6f6e 5b73  trategy: Union[s
-0001db10: 7472 2c20 6c69 7374 2c20 4e6f 6e65 5d20  tr, list, None] 
-0001db20: 3d20 2770 7269 6f72 272c 0a20 2020 2020  = 'prior',.     
+0001dae0: 2020 2020 2020 2020 6475 6d6d 795f 636c          dummy_cl
+0001daf0: 6173 7369 6669 6572 5f73 7472 6174 6567  assifier_strateg
+0001db00: 793a 2055 6e69 6f6e 5b73 7472 2c20 6c69  y: Union[str, li
+0001db10: 7374 2c20 4e6f 6e65 5d20 3d20 2770 7269  st, None] = 'pri
+0001db20: 6f72 272c 0a20 2020 2020 2020 2020 2020  or',.           
 0001db30: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001db40: 2020 2020 2020 2020 2020 2064 756d 6d79             dummy
-0001db50: 5f63 6c61 7373 6966 6965 725f 636f 6e73  _classifier_cons
-0001db60: 7461 6e74 3a20 556e 696f 6e5b 696e 745d  tant: Union[int]
-0001db70: 203d 2031 2c0a 2020 2020 2020 2020 2020   = 1,.          
+0001db40: 2020 2020 2064 756d 6d79 5f63 6c61 7373       dummy_class
+0001db50: 6966 6965 725f 636f 6e73 7461 6e74 3a20  ifier_constant: 
+0001db60: 556e 696f 6e5b 696e 745d 203d 2031 2c0a  Union[int] = 1,.
+0001db70: 2020 2020 2020 2020 2020 2020 2020 2020                  
 0001db80: 2020 2020 2020 2020 2020 2020 2020 2020                  
-0001db90: 2020 2020 2020 2920 2d3e 205f 6669 6775        ) -> _figu
-0001dba0: 7265 2e46 6967 7572 653a 0a20 2020 2020  re.Figure:.     
-0001dbb0: 2020 2022 2222 0a20 2020 2020 2020 2052     """.        R
-0001dbc0: 6574 7572 6e73 2061 2050 6c6f 746c 7920  eturns a Plotly 
-0001dbd0: 6f62 6a65 6374 206f 6620 6120 6261 722d  object of a bar-
-0001dbe0: 6368 6172 7420 6f66 2074 6865 206d 6574  chart of the met
-0001dbf0: 7269 6373 2061 6372 6f73 7320 616c 6c20  rics across all 
-0001dc00: 6f66 2074 6865 206d 6f64 656c 732e 0a0a  of the models...
-0001dc10: 2020 2020 2020 2020 4172 6773 3a0a 2020          Args:.  
-0001dc20: 2020 2020 2020 2020 2020 6475 6d6d 795f            dummy_
-0001dc30: 636c 6173 7369 6669 6572 5f73 7472 6174  classifier_strat
-0001dc40: 6567 793a 0a20 2020 2020 2020 2020 2020  egy:.           
-0001dc50: 2020 2020 2069 6620 6e6f 7420 4e6f 6e65       if not None
-0001dc60: 2c20 7468 656e 2072 6574 7572 6e73 2063  , then returns c
-0001dc70: 6f6c 756d 6e28 7329 2063 6f72 7265 7370  olumn(s) corresp
-0001dc80: 6f6e 6469 6e67 2074 6f20 7468 6520 7363  onding to the sc
-0001dc90: 6f72 6573 2066 726f 6d20 7072 6564 6963  ores from predic
-0001dca0: 7469 6f6e 7320 6f66 0a20 2020 2020 2020  tions of.       
-0001dcb0: 2020 2020 2020 2020 2073 6b6c 6561 726e           sklearn
-0001dcc0: 2e64 756d 6d79 2e44 756d 6d79 436c 6173  .dummy.DummyClas
-0001dcd0: 7369 6669 6572 2c20 6261 7365 6420 6f6e  sifier, based on
-0001dce0: 2074 6865 2073 7472 6174 6567 7920 286f   the strategy (o
-0001dcf0: 7220 7374 7261 7465 6769 6573 2920 7072  r strategies) pr
-0001dd00: 6f76 6964 6564 2e20 5661 6c69 6420 7661  ovided. Valid va
-0001dd10: 6c75 6573 0a20 2020 2020 2020 2020 2020  lues.           
-0001dd20: 2020 2020 2063 6f72 7265 7370 6f6e 6420       correspond 
-0001dd30: 746f 2076 616c 7565 7320 6f66 2060 7374  to values of `st
-0001dd40: 7261 7465 6779 6020 7061 7261 6d65 7465  rategy` paramete
-0001dd50: 7220 6c69 7374 6564 0a20 2020 2020 2020  r listed.       
-0001dd60: 2020 2020 2020 2020 2068 7474 7073 3a2f           https:/
-0001dd70: 2f73 6369 6b69 742d 6c65 6172 6e2e 6f72  /scikit-learn.or
-0001dd80: 672f 7374 6162 6c65 2f6d 6f64 756c 6573  g/stable/modules
-0001dd90: 2f67 656e 6572 6174 6564 2f73 6b6c 6561  /generated/sklea
-0001dda0: 726e 2e64 756d 6d79 2e44 756d 6d79 436c  rn.dummy.DummyCl
-0001ddb0: 6173 7369 6669 6572 2e68 746d 6c0a 0a20  assifier.html.. 
-0001ddc0: 2020 2020 2020 2020 2020 2020 2020 2049                 I
-0001ddd0: 6620 6120 6c69 7374 2069 7320 7061 7373  f a list is pass
-0001dde0: 6564 2069 6e20 2865 2e67 2e20 5b27 7072  ed in (e.g. ['pr
-0001ddf0: 696f 7227 2c20 2775 6e69 666f 726d 275d  ior', 'uniform']
-0001de00: 2c20 7468 656e 206f 6e65 2073 636f 7265  , then one score
-0001de10: 2063 6f6c 756d 6e20 7065 7220 7661 6c75   column per valu
-0001de20: 6520 6973 0a20 2020 2020 2020 2020 2020  e is.           
-0001de30: 2020 2020 2061 6464 6564 2e0a 0a20 2020       added...   
-0001de40: 2020 2020 2020 2020 2020 2020 2049 6620               If 
-0001de50: 4e6f 6e65 2069 7320 7061 7373 6564 2c20  None is passed, 
-0001de60: 7468 656e 206e 6f20 6164 6469 7469 6f6e  then no addition
-0001de70: 616c 2063 6f6c 756d 6e73 2061 7265 2061  al columns are a
-0001de80: 6464 6564 2e0a 2020 2020 2020 2020 2020  dded..          
-0001de90: 2020 6475 6d6d 795f 636c 6173 7369 6669    dummy_classifi
-0001dea0: 6572 5f63 6f6e 7374 616e 743a 0a20 2020  er_constant:.   
-0001deb0: 2020 2020 2020 2020 2020 2020 2054 6865               The
-0001dec0: 2065 7870 6c69 6369 7420 636f 6e73 7461   explicit consta
-0001ded0: 6e74 2061 7320 7072 6564 6963 7465 6420  nt as predicted 
-0001dee0: 6279 2074 6865 20e2 809c 636f 6e73 7461  by the ...consta
-0001def0: 6e74 e280 9d20 7374 7261 7465 6779 2066  nt... strategy f
-0001df00: 6f72 2074 6865 0a20 2020 2020 2020 2020  or the.         
-0001df10: 2020 2020 2020 2044 756d 6d79 436c 6173         DummyClas
-0001df20: 7369 6669 6572 2e0a 2020 2020 2020 2020  sifier..        
-0001df30: 2020 2020 2020 2020 5468 6973 2070 6172          This par
-0001df40: 616d 6574 6572 2069 7320 7573 6566 756c  ameter is useful
-0001df50: 206f 6e6c 7920 666f 7220 7468 6520 e280   only for the ..
-0001df60: 9c63 6f6e 7374 616e 74e2 809d 2064 756d  .constant... dum
-0001df70: 6d79 5f63 6c61 7373 6966 6965 725f 7374  my_classifier_st
-0001df80: 7261 7465 6779 2e0a 2020 2020 2020 2020  rategy..        
-0001df90: 2222 220a 2020 2020 2020 2020 7363 6f72  """.        scor
-0001dfa0: 655f 6466 203d 2073 656c 662e 616c 6c5f  e_df = self.all_
-0001dfb0: 6d65 7472 6963 735f 6466 280a 2020 2020  metrics_df(.    
-0001dfc0: 2020 2020 2020 2020 6475 6d6d 795f 636c          dummy_cl
-0001dfd0: 6173 7369 6669 6572 5f73 7472 6174 6567  assifier_strateg
-0001dfe0: 793d 6475 6d6d 795f 636c 6173 7369 6669  y=dummy_classifi
-0001dff0: 6572 5f73 7472 6174 6567 792c 0a20 2020  er_strategy,.   
-0001e000: 2020 2020 2020 2020 2064 756d 6d79 5f63           dummy_c
-0001e010: 6c61 7373 6966 6965 725f 636f 6e73 7461  lassifier_consta
-0001e020: 6e74 3d64 756d 6d79 5f63 6c61 7373 6966  nt=dummy_classif
-0001e030: 6965 725f 636f 6e73 7461 6e74 0a20 2020  ier_constant.   
-0001e040: 2020 2020 2029 2e74 7261 6e73 706f 7365       ).transpose
-0001e050: 2829 0a0a 2020 2020 2020 2020 7363 6f72  ()..        scor
-0001e060: 655f 6466 203d 2073 636f 7265 5f64 662e  e_df = score_df.
-0001e070: 7265 7365 745f 696e 6465 7828 290a 0a20  reset_index().. 
-0001e080: 2020 2020 2020 2063 6f6c 6f72 7320 3d20         colors = 
-0001e090: 5b65 2e76 616c 7565 2066 6f72 2065 2069  [e.value for e i
-0001e0a0: 6e20 6863 6f6c 6f72 2e43 6f6c 6f72 735d  n hcolor.Colors]
-0001e0b0: 0a20 2020 2020 2020 2066 6967 203d 2070  .        fig = p
-0001e0c0: 782e 6261 7228 0a20 2020 2020 2020 2020  x.bar(.         
-0001e0d0: 2020 2064 6174 615f 6672 616d 653d 7363     data_frame=sc
-0001e0e0: 6f72 655f 6466 2e6d 656c 7428 6964 5f76  ore_df.melt(id_v
-0001e0f0: 6172 733d 2769 6e64 6578 2729 2c0a 2020  ars='index'),.  
-0001e100: 2020 2020 2020 2020 2020 793d 2776 6172            y='var
-0001e110: 6961 626c 6527 2c0a 2020 2020 2020 2020  iable',.        
-0001e120: 2020 2020 783d 2776 616c 7565 272c 0a20      x='value',. 
-0001e130: 2020 2020 2020 2020 2020 2066 6163 6574             facet
-0001e140: 5f63 6f6c 3d27 696e 6465 7827 2c0a 2020  _col='index',.  
-0001e150: 2020 2020 2020 2020 2020 6661 6365 745f            facet_
-0001e160: 636f 6c5f 7772 6170 3d32 2c0a 2020 2020  col_wrap=2,.    
-0001e170: 2020 2020 2020 2020 636f 6c6f 723d 2776          color='v
-0001e180: 6172 6961 626c 6527 2c0a 2020 2020 2020  ariable',.      
-0001e190: 2020 2020 2020 636f 6c6f 725f 6469 7363        color_disc
-0001e1a0: 7265 7465 5f73 6571 7565 6e63 653d 636f  rete_sequence=co
-0001e1b0: 6c6f 7273 2c0a 2020 2020 2020 2020 2020  lors,.          
-0001e1c0: 2020 6261 726d 6f64 653d 2767 726f 7570    barmode='group
-0001e1d0: 272c 0a20 2020 2020 2020 2020 2020 2068  ',.            h
-0001e1e0: 6569 6768 743d 3130 3030 2c0a 2020 2020  eight=1000,.    
-0001e1f0: 2020 2020 2020 2020 6c61 6265 6c73 3d7b          labels={
-0001e200: 2769 6e64 6578 273a 2027 5363 6f72 6527  'index': 'Score'
-0001e210: 7d2c 0a20 2020 2020 2020 2020 2020 2074  },.            t
-0001e220: 6974 6c65 3d22 4d6f 6465 6c20 436f 6d70  itle="Model Comp
-0001e230: 6172 6973 6f6e 220a 2020 2020 2020 2020  arison".        
-0001e240: 290a 2020 2020 2020 2020 6669 672e 7570  ).        fig.up
-0001e250: 6461 7465 5f6c 6179 6f75 7428 7368 6f77  date_layout(show
-0001e260: 6c65 6765 6e64 3d46 616c 7365 290a 2020  legend=False).  
-0001e270: 2020 2020 2020 6669 672e 7570 6461 7465        fig.update
-0001e280: 5f79 6178 6573 2874 6974 6c65 3d4e 6f6e  _yaxes(title=Non
-0001e290: 6529 0a20 2020 2020 2020 2072 6574 7572  e).        retur
-0001e2a0: 6e20 6669 670a 0a20 2020 2064 6566 2070  n fig..    def p
-0001e2b0: 6c6f 745f 726f 635f 6375 7276 6573 2873  lot_roc_curves(s
-0001e2c0: 656c 6629 202d 3e20 5f66 6967 7572 652e  elf) -> _figure.
-0001e2d0: 4669 6775 7265 3a0a 2020 2020 2020 2020  Figure:.        
-0001e2e0: 2222 2252 6574 7572 6e73 2061 2070 6c6f  """Returns a plo
-0001e2f0: 746c 7920 6f62 6a65 6374 2072 6570 7265  tly object repre
-0001e300: 7365 6e74 696e 6720 7468 6520 524f 4320  senting the ROC 
-0001e310: 6375 7276 6573 2061 6372 6f73 7320 616c  curves across al
-0001e320: 6c20 6d6f 6465 6c73 2e22 2222 0a20 2020  l models.""".   
-0001e330: 2020 2020 2072 6573 756c 7420 3d20 4e6f       result = No
-0001e340: 6e65 0a0a 2020 2020 2020 2020 666f 7220  ne..        for 
-0001e350: 6b65 792c 2076 616c 7565 2069 6e20 7365  key, value in se
-0001e360: 6c66 2e5f 6576 616c 7561 746f 7273 2e69  lf._evaluators.i
-0001e370: 7465 6d73 2829 3a0a 2020 2020 2020 2020  tems():.        
-0001e380: 2020 2020 6175 635f 6466 203d 2076 616c      auc_df = val
-0001e390: 7565 2e5f 6765 745f 6175 635f 6375 7276  ue._get_auc_curv
-0001e3a0: 655f 6461 7461 6672 616d 6528 2920 2023  e_dataframe()  #
-0001e3b0: 2070 796c 696e 743a 2064 6973 6162 6c65   pylint: disable
-0001e3c0: 3d70 726f 7465 6374 6564 2d61 6363 6573  =protected-acces
-0001e3d0: 7320 2320 6e6f 7161 0a20 2020 2020 2020  s # noqa.       
-0001e3e0: 2020 2020 2061 7563 5f64 665b 274d 6f64       auc_df['Mod
-0001e3f0: 656c 275d 203d 206b 6579 0a20 2020 2020  el'] = key.     
-0001e400: 2020 2020 2020 2072 6573 756c 7420 3d20         result = 
-0001e410: 7064 2e63 6f6e 6361 7428 5b72 6573 756c  pd.concat([resul
-0001e420: 742c 2061 7563 5f64 665d 2c20 6178 6973  t, auc_df], axis
-0001e430: 3d30 290a 0a20 2020 2020 2020 2063 6f6c  =0)..        col
-0001e440: 6f72 7320 3d20 5b65 2e76 616c 7565 2066  ors = [e.value f
-0001e450: 6f72 2065 2069 6e20 6863 6f6c 6f72 2e43  or e in hcolor.C
-0001e460: 6f6c 6f72 735d 0a20 2020 2020 2020 2066  olors].        f
-0001e470: 6967 203d 2070 782e 6c69 6e65 280a 2020  ig = px.line(.  
-0001e480: 2020 2020 2020 2020 2020 6461 7461 5f66            data_f
-0001e490: 7261 6d65 3d72 6573 756c 742c 0a20 2020  rame=result,.   
-0001e4a0: 2020 2020 2020 2020 2078 3d27 4661 6c73           x='Fals
-0001e4b0: 6520 506f 7369 7469 7665 2052 6174 6527  e Positive Rate'
-0001e4c0: 2c0a 2020 2020 2020 2020 2020 2020 793d  ,.            y=
-0001e4d0: 2754 7275 6520 506f 7369 7469 7665 2052  'True Positive R
-0001e4e0: 6174 6527 2c0a 2020 2020 2020 2020 2020  ate',.          
-0001e4f0: 2020 636f 6c6f 723d 274d 6f64 656c 272c    color='Model',
-0001e500: 0a20 2020 2020 2020 2020 2020 2063 6f6c  .            col
-0001e510: 6f72 5f64 6973 6372 6574 655f 7365 7175  or_discrete_sequ
-0001e520: 656e 6365 3d63 6f6c 6f72 732c 0a20 2020  ence=colors,.   
-0001e530: 2020 2020 2020 2020 2068 6569 6768 743d           height=
-0001e540: 3535 302c 0a20 2020 2020 2020 2020 2020  550,.           
-0001e550: 2077 6964 7468 3d35 3530 202a 2047 4f4c   width=550 * GOL
-0001e560: 4445 4e5f 5241 5449 4f2c 0a20 2020 2020  DEN_RATIO,.     
-0001e570: 2020 2020 2020 2063 7573 746f 6d5f 6461         custom_da
-0001e580: 7461 3d5b 2774 6872 6573 686f 6c64 272c  ta=['threshold',
-0001e590: 2027 4d6f 6465 6c27 5d2c 0a20 2020 2020   'Model'],.     
-0001e5a0: 2020 2020 2020 2074 6974 6c65 3d22 524f         title="RO
-0001e5b0: 4320 4375 7276 6520 6f66 204d 6f64 656c  C Curve of Model
-0001e5c0: 7322 2c0a 2020 2020 2020 2020 290a 2020  s",.        ).  
-0001e5d0: 2020 2020 2020 666f 7220 696e 6465 7820        for index 
-0001e5e0: 696e 2072 616e 6765 286c 656e 2873 656c  in range(len(sel
-0001e5f0: 662e 5f65 7661 6c75 6174 6f72 7329 293a  f._evaluators)):
-0001e600: 0a20 2020 2020 2020 2020 2020 2073 6361  .            sca
-0001e610: 7474 6572 5f31 203d 2070 782e 7363 6174  tter_1 = px.scat
-0001e620: 7465 7228 0a20 2020 2020 2020 2020 2020  ter(.           
-0001e630: 2020 2020 2064 6174 615f 6672 616d 653d       data_frame=
-0001e640: 7265 7375 6c74 2c0a 2020 2020 2020 2020  result,.        
-0001e650: 2020 2020 2020 2020 783d 2746 616c 7365          x='False
-0001e660: 2050 6f73 6974 6976 6520 5261 7465 272c   Positive Rate',
-0001e670: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001e680: 2079 3d27 5472 7565 2050 6f73 6974 6976   y='True Positiv
-0001e690: 6520 5261 7465 272c 0a20 2020 2020 2020  e Rate',.       
-0001e6a0: 2020 2020 2020 2020 2063 6f6c 6f72 3d27           color='
-0001e6b0: 4d6f 6465 6c27 2c0a 2020 2020 2020 2020  Model',.        
-0001e6c0: 2020 2020 2020 2020 636f 6c6f 725f 6469          color_di
-0001e6d0: 7363 7265 7465 5f73 6571 7565 6e63 653d  screte_sequence=
-0001e6e0: 636f 6c6f 7273 2c0a 2020 2020 2020 2020  colors,.        
-0001e6f0: 2020 2020 2020 2020 6375 7374 6f6d 5f64          custom_d
-0001e700: 6174 613d 5b27 7468 7265 7368 6f6c 6427  ata=['threshold'
-0001e710: 2c20 274d 6f64 656c 275d 2c0a 2020 2020  , 'Model'],.    
-0001e720: 2020 2020 2020 2020 290a 2020 2020 2020          ).      
-0001e730: 2020 2020 2020 7363 6174 7465 725f 312e        scatter_1.
-0001e740: 6461 7461 5b69 6e64 6578 5d5b 2773 686f  data[index]['sho
-0001e750: 776c 6567 656e 6427 5d20 3d20 4661 6c73  wlegend'] = Fals
-0001e760: 650a 2020 2020 2020 2020 2020 2020 6669  e.            fi
-0001e770: 672e 6164 645f 7472 6163 6528 0a20 2020  g.add_trace(.   
-0001e780: 2020 2020 2020 2020 2020 2020 2073 6361               sca
-0001e790: 7474 6572 5f31 2e64 6174 615b 696e 6465  tter_1.data[inde
-0001e7a0: 785d 0a20 2020 2020 2020 2020 2020 2029  x].            )
-0001e7b0: 0a20 2020 2020 2020 2020 2020 2071 7565  .            que
-0001e7c0: 7279 203d 2066 2274 6872 6573 686f 6c64  ry = f"threshold
-0001e7d0: 203d 3d20 302e 3520 2620 4d6f 6465 6c20   == 0.5 & Model 
-0001e7e0: 3d3d 2027 7b6c 6973 7428 7365 6c66 2e5f  == '{list(self._
-0001e7f0: 6576 616c 7561 746f 7273 2e6b 6579 7328  evaluators.keys(
-0001e800: 2929 5b69 6e64 6578 5d7d 2722 0a20 2020  ))[index]}'".   
-0001e810: 2020 2020 2020 2020 2073 6361 7474 6572           scatter
-0001e820: 5f32 203d 2070 782e 7363 6174 7465 7228  _2 = px.scatter(
-0001e830: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001e840: 2064 6174 615f 6672 616d 653d 7265 7375   data_frame=resu
-0001e850: 6c74 2e71 7565 7279 2871 7565 7279 292c  lt.query(query),
-0001e860: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001e870: 2078 3d27 4661 6c73 6520 506f 7369 7469   x='False Positi
-0001e880: 7665 2052 6174 6527 2c0a 2020 2020 2020  ve Rate',.      
-0001e890: 2020 2020 2020 2020 2020 793d 2754 7275            y='Tru
-0001e8a0: 6520 506f 7369 7469 7665 2052 6174 6527  e Positive Rate'
-0001e8b0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-0001e8c0: 2020 636f 6c6f 723d 274d 6f64 656c 272c    color='Model',
-0001e8d0: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
-0001e8e0: 2063 6f6c 6f72 5f64 6973 6372 6574 655f   color_discrete_
-0001e8f0: 7365 7175 656e 6365 3d5b 636f 6c6f 7273  sequence=[colors
-0001e900: 5b69 6e64 6578 5d5d 202b 2063 6f6c 6f72  [index]] + color
-0001e910: 732c 0a20 2020 2020 2020 2020 2020 2020  s,.             
-0001e920: 2020 2063 7573 746f 6d5f 6461 7461 3d5b     custom_data=[
-0001e930: 2774 6872 6573 686f 6c64 272c 2027 4d6f  'threshold', 'Mo
-0001e940: 6465 6c27 5d2c 0a20 2020 2020 2020 2020  del'],.         
-0001e950: 2020 2020 2020 2073 697a 653d 5b32 5d2c         size=[2],
-0001e960: 0a20 2020 2020 2020 2020 2020 2029 0a20  .            ). 
-0001e970: 2020 2020 2020 2020 2020 2073 6361 7474             scatt
-0001e980: 6572 5f32 2e64 6174 615b 305d 5b27 7368  er_2.data[0]['sh
-0001e990: 6f77 6c65 6765 6e64 275d 203d 2046 616c  owlegend'] = Fal
-0001e9a0: 7365 0a20 2020 2020 2020 2020 2020 2066  se.            f
-0001e9b0: 6967 2e61 6464 5f74 7261 6365 280a 2020  ig.add_trace(.  
-0001e9c0: 2020 2020 2020 2020 2020 2020 2020 7363                sc
-0001e9d0: 6174 7465 725f 322e 6461 7461 5b30 5d2c  atter_2.data[0],
-0001e9e0: 0a20 2020 2020 2020 2020 2020 2029 0a0a  .            )..
-0001e9f0: 2020 2020 2020 2020 6669 672e 7570 6461          fig.upda
-0001ea00: 7465 5f74 7261 6365 7328 0a20 2020 2020  te_traces(.     
-0001ea10: 2020 2020 2020 2068 6f76 6572 7465 6d70         hovertemp
-0001ea20: 6c61 7465 3d22 3c62 723e 222e 6a6f 696e  late="<br>".join
-0001ea30: 285b 0a20 2020 2020 2020 2020 2020 2020  ([.             
-0001ea40: 2020 2022 4d6f 6465 6c3a 2025 7b63 7573     "Model: %{cus
-0001ea50: 746f 6d64 6174 615b 315d 7d3c 6272 3e3c  tomdata[1]}<br><
-0001ea60: 6272 3e22 0a20 2020 2020 2020 2020 2020  br>".           
-0001ea70: 2020 2020 2022 4661 6c73 6520 506f 7369       "False Posi
-0001ea80: 7469 7665 2052 6174 653a 2025 7b78 7d22  tive Rate: %{x}"
-0001ea90: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
-0001eaa0: 2020 2254 7275 6520 506f 7369 7469 7665    "True Positive
-0001eab0: 2052 6174 653a 2025 7b79 7d22 2c0a 2020   Rate: %{y}",.  
-0001eac0: 2020 2020 2020 2020 2020 2020 2020 2254                "T
-0001ead0: 6872 6573 686f 6c64 3a20 257b 6375 7374  hreshold: %{cust
-0001eae0: 6f6d 6461 7461 5b30 5d7d 222c 0a20 2020  omdata[0]}",.   
-0001eaf0: 2020 2020 2020 2020 205d 290a 2020 2020           ]).    
-0001eb00: 2020 2020 290a 2020 2020 2020 2020 7265      ).        re
-0001eb10: 7475 726e 2066 6967 0a                   turn fig.
+0001db90: 2920 2d3e 205f 6669 6775 7265 2e46 6967  ) -> _figure.Fig
+0001dba0: 7572 653a 0a20 2020 2020 2020 2022 2222  ure:.        """
+0001dbb0: 0a20 2020 2020 2020 2052 6574 7572 6e73  .        Returns
+0001dbc0: 2061 2050 6c6f 746c 7920 6f62 6a65 6374   a Plotly object
+0001dbd0: 206f 6620 6120 6261 722d 6368 6172 7420   of a bar-chart 
+0001dbe0: 6f66 2074 6865 206d 6574 7269 6373 2061  of the metrics a
+0001dbf0: 6372 6f73 7320 616c 6c20 6f66 2074 6865  cross all of the
+0001dc00: 206d 6f64 656c 732e 0a0a 2020 2020 2020   models...      
+0001dc10: 2020 4172 6773 3a0a 2020 2020 2020 2020    Args:.        
+0001dc20: 2020 2020 6475 6d6d 795f 636c 6173 7369      dummy_classi
+0001dc30: 6669 6572 5f73 7472 6174 6567 793a 0a20  fier_strategy:. 
+0001dc40: 2020 2020 2020 2020 2020 2020 2020 2069                 i
+0001dc50: 6620 6e6f 7420 4e6f 6e65 2c20 7468 656e  f not None, then
+0001dc60: 2072 6574 7572 6e73 2063 6f6c 756d 6e28   returns column(
+0001dc70: 7329 2063 6f72 7265 7370 6f6e 6469 6e67  s) corresponding
+0001dc80: 2074 6f20 7468 6520 7363 6f72 6573 2066   to the scores f
+0001dc90: 726f 6d20 7072 6564 6963 7469 6f6e 7320  rom predictions 
+0001dca0: 6f66 0a20 2020 2020 2020 2020 2020 2020  of.             
+0001dcb0: 2020 2073 6b6c 6561 726e 2e64 756d 6d79     sklearn.dummy
+0001dcc0: 2e44 756d 6d79 436c 6173 7369 6669 6572  .DummyClassifier
+0001dcd0: 2c20 6261 7365 6420 6f6e 2074 6865 2073  , based on the s
+0001dce0: 7472 6174 6567 7920 286f 7220 7374 7261  trategy (or stra
+0001dcf0: 7465 6769 6573 2920 7072 6f76 6964 6564  tegies) provided
+0001dd00: 2e20 5661 6c69 6420 7661 6c75 6573 0a20  . Valid values. 
+0001dd10: 2020 2020 2020 2020 2020 2020 2020 2063                 c
+0001dd20: 6f72 7265 7370 6f6e 6420 746f 2076 616c  orrespond to val
+0001dd30: 7565 7320 6f66 2060 7374 7261 7465 6779  ues of `strategy
+0001dd40: 6020 7061 7261 6d65 7465 7220 6c69 7374  ` parameter list
+0001dd50: 6564 0a20 2020 2020 2020 2020 2020 2020  ed.             
+0001dd60: 2020 2068 7474 7073 3a2f 2f73 6369 6b69     https://sciki
+0001dd70: 742d 6c65 6172 6e2e 6f72 672f 7374 6162  t-learn.org/stab
+0001dd80: 6c65 2f6d 6f64 756c 6573 2f67 656e 6572  le/modules/gener
+0001dd90: 6174 6564 2f73 6b6c 6561 726e 2e64 756d  ated/sklearn.dum
+0001dda0: 6d79 2e44 756d 6d79 436c 6173 7369 6669  my.DummyClassifi
+0001ddb0: 6572 2e68 746d 6c0a 0a20 2020 2020 2020  er.html..       
+0001ddc0: 2020 2020 2020 2020 2049 6620 6120 6c69           If a li
+0001ddd0: 7374 2069 7320 7061 7373 6564 2069 6e20  st is passed in 
+0001dde0: 2865 2e67 2e20 5b27 7072 696f 7227 2c20  (e.g. ['prior', 
+0001ddf0: 2775 6e69 666f 726d 275d 2c20 7468 656e  'uniform'], then
+0001de00: 206f 6e65 2073 636f 7265 2063 6f6c 756d   one score colum
+0001de10: 6e20 7065 7220 7661 6c75 6520 6973 0a20  n per value is. 
+0001de20: 2020 2020 2020 2020 2020 2020 2020 2061                 a
+0001de30: 6464 6564 2e0a 0a20 2020 2020 2020 2020  dded...         
+0001de40: 2020 2020 2020 2049 6620 4e6f 6e65 2069         If None i
+0001de50: 7320 7061 7373 6564 2c20 7468 656e 206e  s passed, then n
+0001de60: 6f20 6164 6469 7469 6f6e 616c 2063 6f6c  o additional col
+0001de70: 756d 6e73 2061 7265 2061 6464 6564 2e0a  umns are added..
+0001de80: 2020 2020 2020 2020 2020 2020 6475 6d6d              dumm
+0001de90: 795f 636c 6173 7369 6669 6572 5f63 6f6e  y_classifier_con
+0001dea0: 7374 616e 743a 0a20 2020 2020 2020 2020  stant:.         
+0001deb0: 2020 2020 2020 2054 6865 2065 7870 6c69         The expli
+0001dec0: 6369 7420 636f 6e73 7461 6e74 2061 7320  cit constant as 
+0001ded0: 7072 6564 6963 7465 6420 6279 2074 6865  predicted by the
+0001dee0: 20e2 809c 636f 6e73 7461 6e74 e280 9d20   ...constant... 
+0001def0: 7374 7261 7465 6779 2066 6f72 2074 6865  strategy for the
+0001df00: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001df10: 2044 756d 6d79 436c 6173 7369 6669 6572   DummyClassifier
+0001df20: 2e0a 2020 2020 2020 2020 2020 2020 2020  ..              
+0001df30: 2020 5468 6973 2070 6172 616d 6574 6572    This parameter
+0001df40: 2069 7320 7573 6566 756c 206f 6e6c 7920   is useful only 
+0001df50: 666f 7220 7468 6520 e280 9c63 6f6e 7374  for the ...const
+0001df60: 616e 74e2 809d 2064 756d 6d79 5f63 6c61  ant... dummy_cla
+0001df70: 7373 6966 6965 725f 7374 7261 7465 6779  ssifier_strategy
+0001df80: 2e0a 2020 2020 2020 2020 2222 220a 2020  ..        """.  
+0001df90: 2020 2020 2020 7363 6f72 655f 6466 203d        score_df =
+0001dfa0: 2073 656c 662e 616c 6c5f 6d65 7472 6963   self.all_metric
+0001dfb0: 735f 6466 280a 2020 2020 2020 2020 2020  s_df(.          
+0001dfc0: 2020 6475 6d6d 795f 636c 6173 7369 6669    dummy_classifi
+0001dfd0: 6572 5f73 7472 6174 6567 793d 6475 6d6d  er_strategy=dumm
+0001dfe0: 795f 636c 6173 7369 6669 6572 5f73 7472  y_classifier_str
+0001dff0: 6174 6567 792c 0a20 2020 2020 2020 2020  ategy,.         
+0001e000: 2020 2064 756d 6d79 5f63 6c61 7373 6966     dummy_classif
+0001e010: 6965 725f 636f 6e73 7461 6e74 3d64 756d  ier_constant=dum
+0001e020: 6d79 5f63 6c61 7373 6966 6965 725f 636f  my_classifier_co
+0001e030: 6e73 7461 6e74 0a20 2020 2020 2020 2029  nstant.        )
+0001e040: 2e74 7261 6e73 706f 7365 2829 0a0a 2020  .transpose()..  
+0001e050: 2020 2020 2020 7363 6f72 655f 6466 203d        score_df =
+0001e060: 2073 636f 7265 5f64 662e 7265 7365 745f   score_df.reset_
+0001e070: 696e 6465 7828 290a 0a20 2020 2020 2020  index()..       
+0001e080: 2063 6f6c 6f72 7320 3d20 5b65 2e76 616c   colors = [e.val
+0001e090: 7565 2066 6f72 2065 2069 6e20 6863 6f6c  ue for e in hcol
+0001e0a0: 6f72 2e43 6f6c 6f72 735d 0a20 2020 2020  or.Colors].     
+0001e0b0: 2020 2066 6967 203d 2070 782e 6261 7228     fig = px.bar(
+0001e0c0: 0a20 2020 2020 2020 2020 2020 2064 6174  .            dat
+0001e0d0: 615f 6672 616d 653d 7363 6f72 655f 6466  a_frame=score_df
+0001e0e0: 2e6d 656c 7428 6964 5f76 6172 733d 2769  .melt(id_vars='i
+0001e0f0: 6e64 6578 2729 2c0a 2020 2020 2020 2020  ndex'),.        
+0001e100: 2020 2020 793d 2776 6172 6961 626c 6527      y='variable'
+0001e110: 2c0a 2020 2020 2020 2020 2020 2020 783d  ,.            x=
+0001e120: 2776 616c 7565 272c 0a20 2020 2020 2020  'value',.       
+0001e130: 2020 2020 2066 6163 6574 5f63 6f6c 3d27       facet_col='
+0001e140: 696e 6465 7827 2c0a 2020 2020 2020 2020  index',.        
+0001e150: 2020 2020 6661 6365 745f 636f 6c5f 7772      facet_col_wr
+0001e160: 6170 3d32 2c0a 2020 2020 2020 2020 2020  ap=2,.          
+0001e170: 2020 636f 6c6f 723d 2776 6172 6961 626c    color='variabl
+0001e180: 6527 2c0a 2020 2020 2020 2020 2020 2020  e',.            
+0001e190: 636f 6c6f 725f 6469 7363 7265 7465 5f73  color_discrete_s
+0001e1a0: 6571 7565 6e63 653d 636f 6c6f 7273 2c0a  equence=colors,.
+0001e1b0: 2020 2020 2020 2020 2020 2020 6261 726d              barm
+0001e1c0: 6f64 653d 2767 726f 7570 272c 0a20 2020  ode='group',.   
+0001e1d0: 2020 2020 2020 2020 2068 6569 6768 743d           height=
+0001e1e0: 3130 3030 2c0a 2020 2020 2020 2020 2020  1000,.          
+0001e1f0: 2020 6c61 6265 6c73 3d7b 2769 6e64 6578    labels={'index
+0001e200: 273a 2027 5363 6f72 6527 7d2c 0a20 2020  ': 'Score'},.   
+0001e210: 2020 2020 2020 2020 2074 6974 6c65 3d22           title="
+0001e220: 4d6f 6465 6c20 436f 6d70 6172 6973 6f6e  Model Comparison
+0001e230: 220a 2020 2020 2020 2020 290a 2020 2020  ".        ).    
+0001e240: 2020 2020 6669 672e 7570 6461 7465 5f6c      fig.update_l
+0001e250: 6179 6f75 7428 7368 6f77 6c65 6765 6e64  ayout(showlegend
+0001e260: 3d46 616c 7365 290a 2020 2020 2020 2020  =False).        
+0001e270: 6669 672e 7570 6461 7465 5f79 6178 6573  fig.update_yaxes
+0001e280: 2874 6974 6c65 3d4e 6f6e 6529 0a20 2020  (title=None).   
+0001e290: 2020 2020 2072 6574 7572 6e20 6669 670a       return fig.
+0001e2a0: 0a20 2020 2064 6566 2070 6c6f 745f 726f  .    def plot_ro
+0001e2b0: 635f 6375 7276 6573 2873 656c 6629 202d  c_curves(self) -
+0001e2c0: 3e20 5f66 6967 7572 652e 4669 6775 7265  > _figure.Figure
+0001e2d0: 3a0a 2020 2020 2020 2020 2222 2252 6574  :.        """Ret
+0001e2e0: 7572 6e73 2061 2070 6c6f 746c 7920 6f62  urns a plotly ob
+0001e2f0: 6a65 6374 2072 6570 7265 7365 6e74 696e  ject representin
+0001e300: 6720 7468 6520 524f 4320 6375 7276 6573  g the ROC curves
+0001e310: 2061 6372 6f73 7320 616c 6c20 6d6f 6465   across all mode
+0001e320: 6c73 2e22 2222 0a20 2020 2020 2020 2072  ls.""".        r
+0001e330: 6573 756c 7420 3d20 4e6f 6e65 0a0a 2020  esult = None..  
+0001e340: 2020 2020 2020 666f 7220 6b65 792c 2076        for key, v
+0001e350: 616c 7565 2069 6e20 7365 6c66 2e5f 6576  alue in self._ev
+0001e360: 616c 7561 746f 7273 2e69 7465 6d73 2829  aluators.items()
+0001e370: 3a0a 2020 2020 2020 2020 2020 2020 6175  :.            au
+0001e380: 635f 6466 203d 2076 616c 7565 2e5f 6765  c_df = value._ge
+0001e390: 745f 6175 635f 6375 7276 655f 6461 7461  t_auc_curve_data
+0001e3a0: 6672 616d 6528 2920 2023 2070 796c 696e  frame()  # pylin
+0001e3b0: 743a 2064 6973 6162 6c65 3d70 726f 7465  t: disable=prote
+0001e3c0: 6374 6564 2d61 6363 6573 7320 2320 6e6f  cted-access # no
+0001e3d0: 7161 0a20 2020 2020 2020 2020 2020 2061  qa.            a
+0001e3e0: 7563 5f64 665b 274d 6f64 656c 275d 203d  uc_df['Model'] =
+0001e3f0: 206b 6579 0a20 2020 2020 2020 2020 2020   key.           
+0001e400: 2072 6573 756c 7420 3d20 7064 2e63 6f6e   result = pd.con
+0001e410: 6361 7428 5b72 6573 756c 742c 2061 7563  cat([result, auc
+0001e420: 5f64 665d 2c20 6178 6973 3d30 290a 0a20  _df], axis=0).. 
+0001e430: 2020 2020 2020 2063 6f6c 6f72 7320 3d20         colors = 
+0001e440: 5b65 2e76 616c 7565 2066 6f72 2065 2069  [e.value for e i
+0001e450: 6e20 6863 6f6c 6f72 2e43 6f6c 6f72 735d  n hcolor.Colors]
+0001e460: 0a20 2020 2020 2020 2066 6967 203d 2070  .        fig = p
+0001e470: 782e 6c69 6e65 280a 2020 2020 2020 2020  x.line(.        
+0001e480: 2020 2020 6461 7461 5f66 7261 6d65 3d72      data_frame=r
+0001e490: 6573 756c 742c 0a20 2020 2020 2020 2020  esult,.         
+0001e4a0: 2020 2078 3d27 4661 6c73 6520 506f 7369     x='False Posi
+0001e4b0: 7469 7665 2052 6174 6527 2c0a 2020 2020  tive Rate',.    
+0001e4c0: 2020 2020 2020 2020 793d 2754 7275 6520          y='True 
+0001e4d0: 506f 7369 7469 7665 2052 6174 6527 2c0a  Positive Rate',.
+0001e4e0: 2020 2020 2020 2020 2020 2020 636f 6c6f              colo
+0001e4f0: 723d 274d 6f64 656c 272c 0a20 2020 2020  r='Model',.     
+0001e500: 2020 2020 2020 2063 6f6c 6f72 5f64 6973         color_dis
+0001e510: 6372 6574 655f 7365 7175 656e 6365 3d63  crete_sequence=c
+0001e520: 6f6c 6f72 732c 0a20 2020 2020 2020 2020  olors,.         
+0001e530: 2020 2068 6569 6768 743d 3535 302c 0a20     height=550,. 
+0001e540: 2020 2020 2020 2020 2020 2077 6964 7468             width
+0001e550: 3d35 3530 202a 2047 4f4c 4445 4e5f 5241  =550 * GOLDEN_RA
+0001e560: 5449 4f2c 0a20 2020 2020 2020 2020 2020  TIO,.           
+0001e570: 2063 7573 746f 6d5f 6461 7461 3d5b 2774   custom_data=['t
+0001e580: 6872 6573 686f 6c64 272c 2027 4d6f 6465  hreshold', 'Mode
+0001e590: 6c27 5d2c 0a20 2020 2020 2020 2020 2020  l'],.           
+0001e5a0: 2074 6974 6c65 3d22 524f 4320 4375 7276   title="ROC Curv
+0001e5b0: 6520 6f66 204d 6f64 656c 7322 2c0a 2020  e of Models",.  
+0001e5c0: 2020 2020 2020 290a 2020 2020 2020 2020        ).        
+0001e5d0: 666f 7220 696e 6465 7820 696e 2072 616e  for index in ran
+0001e5e0: 6765 286c 656e 2873 656c 662e 5f65 7661  ge(len(self._eva
+0001e5f0: 6c75 6174 6f72 7329 293a 0a20 2020 2020  luators)):.     
+0001e600: 2020 2020 2020 2073 6361 7474 6572 5f31         scatter_1
+0001e610: 203d 2070 782e 7363 6174 7465 7228 0a20   = px.scatter(. 
+0001e620: 2020 2020 2020 2020 2020 2020 2020 2064                 d
+0001e630: 6174 615f 6672 616d 653d 7265 7375 6c74  ata_frame=result
+0001e640: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+0001e650: 2020 783d 2746 616c 7365 2050 6f73 6974    x='False Posit
+0001e660: 6976 6520 5261 7465 272c 0a20 2020 2020  ive Rate',.     
+0001e670: 2020 2020 2020 2020 2020 2079 3d27 5472             y='Tr
+0001e680: 7565 2050 6f73 6974 6976 6520 5261 7465  ue Positive Rate
+0001e690: 272c 0a20 2020 2020 2020 2020 2020 2020  ',.             
+0001e6a0: 2020 2063 6f6c 6f72 3d27 4d6f 6465 6c27     color='Model'
+0001e6b0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+0001e6c0: 2020 636f 6c6f 725f 6469 7363 7265 7465    color_discrete
+0001e6d0: 5f73 6571 7565 6e63 653d 636f 6c6f 7273  _sequence=colors
+0001e6e0: 2c0a 2020 2020 2020 2020 2020 2020 2020  ,.              
+0001e6f0: 2020 6375 7374 6f6d 5f64 6174 613d 5b27    custom_data=['
+0001e700: 7468 7265 7368 6f6c 6427 2c20 274d 6f64  threshold', 'Mod
+0001e710: 656c 275d 2c0a 2020 2020 2020 2020 2020  el'],.          
+0001e720: 2020 290a 2020 2020 2020 2020 2020 2020    ).            
+0001e730: 7363 6174 7465 725f 312e 6461 7461 5b69  scatter_1.data[i
+0001e740: 6e64 6578 5d5b 2773 686f 776c 6567 656e  ndex]['showlegen
+0001e750: 6427 5d20 3d20 4661 6c73 650a 2020 2020  d'] = False.    
+0001e760: 2020 2020 2020 2020 6669 672e 6164 645f          fig.add_
+0001e770: 7472 6163 6528 0a20 2020 2020 2020 2020  trace(.         
+0001e780: 2020 2020 2020 2073 6361 7474 6572 5f31         scatter_1
+0001e790: 2e64 6174 615b 696e 6465 785d 0a20 2020  .data[index].   
+0001e7a0: 2020 2020 2020 2020 2029 0a20 2020 2020           ).     
+0001e7b0: 2020 2020 2020 2071 7565 7279 203d 2066         query = f
+0001e7c0: 2274 6872 6573 686f 6c64 203d 3d20 302e  "threshold == 0.
+0001e7d0: 3520 2620 4d6f 6465 6c20 3d3d 2027 7b6c  5 & Model == '{l
+0001e7e0: 6973 7428 7365 6c66 2e5f 6576 616c 7561  ist(self._evalua
+0001e7f0: 746f 7273 2e6b 6579 7328 2929 5b69 6e64  tors.keys())[ind
+0001e800: 6578 5d7d 2722 0a20 2020 2020 2020 2020  ex]}'".         
+0001e810: 2020 2073 6361 7474 6572 5f32 203d 2070     scatter_2 = p
+0001e820: 782e 7363 6174 7465 7228 0a20 2020 2020  x.scatter(.     
+0001e830: 2020 2020 2020 2020 2020 2064 6174 615f             data_
+0001e840: 6672 616d 653d 7265 7375 6c74 2e71 7565  frame=result.que
+0001e850: 7279 2871 7565 7279 292c 0a20 2020 2020  ry(query),.     
+0001e860: 2020 2020 2020 2020 2020 2078 3d27 4661             x='Fa
+0001e870: 6c73 6520 506f 7369 7469 7665 2052 6174  lse Positive Rat
+0001e880: 6527 2c0a 2020 2020 2020 2020 2020 2020  e',.            
+0001e890: 2020 2020 793d 2754 7275 6520 506f 7369      y='True Posi
+0001e8a0: 7469 7665 2052 6174 6527 2c0a 2020 2020  tive Rate',.    
+0001e8b0: 2020 2020 2020 2020 2020 2020 636f 6c6f              colo
+0001e8c0: 723d 274d 6f64 656c 272c 0a20 2020 2020  r='Model',.     
+0001e8d0: 2020 2020 2020 2020 2020 2063 6f6c 6f72             color
+0001e8e0: 5f64 6973 6372 6574 655f 7365 7175 656e  _discrete_sequen
+0001e8f0: 6365 3d5b 636f 6c6f 7273 5b69 6e64 6578  ce=[colors[index
+0001e900: 5d5d 202b 2063 6f6c 6f72 732c 0a20 2020  ]] + colors,.   
+0001e910: 2020 2020 2020 2020 2020 2020 2063 7573               cus
+0001e920: 746f 6d5f 6461 7461 3d5b 2774 6872 6573  tom_data=['thres
+0001e930: 686f 6c64 272c 2027 4d6f 6465 6c27 5d2c  hold', 'Model'],
+0001e940: 0a20 2020 2020 2020 2020 2020 2020 2020  .               
+0001e950: 2073 697a 653d 5b32 5d2c 0a20 2020 2020   size=[2],.     
+0001e960: 2020 2020 2020 2029 0a20 2020 2020 2020         ).       
+0001e970: 2020 2020 2073 6361 7474 6572 5f32 2e64       scatter_2.d
+0001e980: 6174 615b 305d 5b27 7368 6f77 6c65 6765  ata[0]['showlege
+0001e990: 6e64 275d 203d 2046 616c 7365 0a20 2020  nd'] = False.   
+0001e9a0: 2020 2020 2020 2020 2066 6967 2e61 6464           fig.add
+0001e9b0: 5f74 7261 6365 280a 2020 2020 2020 2020  _trace(.        
+0001e9c0: 2020 2020 2020 2020 7363 6174 7465 725f          scatter_
+0001e9d0: 322e 6461 7461 5b30 5d2c 0a20 2020 2020  2.data[0],.     
+0001e9e0: 2020 2020 2020 2029 0a0a 2020 2020 2020         )..      
+0001e9f0: 2020 6669 672e 7570 6461 7465 5f74 7261    fig.update_tra
+0001ea00: 6365 7328 0a20 2020 2020 2020 2020 2020  ces(.           
+0001ea10: 2068 6f76 6572 7465 6d70 6c61 7465 3d22   hovertemplate="
+0001ea20: 3c62 723e 222e 6a6f 696e 285b 0a20 2020  <br>".join([.   
+0001ea30: 2020 2020 2020 2020 2020 2020 2022 4d6f               "Mo
+0001ea40: 6465 6c3a 2025 7b63 7573 746f 6d64 6174  del: %{customdat
+0001ea50: 615b 315d 7d3c 6272 3e3c 6272 3e22 0a20  a[1]}<br><br>". 
+0001ea60: 2020 2020 2020 2020 2020 2020 2020 2022                 "
+0001ea70: 4661 6c73 6520 506f 7369 7469 7665 2052  False Positive R
+0001ea80: 6174 653a 2025 7b78 7d22 2c0a 2020 2020  ate: %{x}",.    
+0001ea90: 2020 2020 2020 2020 2020 2020 2254 7275              "Tru
+0001eaa0: 6520 506f 7369 7469 7665 2052 6174 653a  e Positive Rate:
+0001eab0: 2025 7b79 7d22 2c0a 2020 2020 2020 2020   %{y}",.        
+0001eac0: 2020 2020 2020 2020 2254 6872 6573 686f          "Thresho
+0001ead0: 6c64 3a20 257b 6375 7374 6f6d 6461 7461  ld: %{customdata
+0001eae0: 5b30 5d7d 222c 0a20 2020 2020 2020 2020  [0]}",.         
+0001eaf0: 2020 205d 290a 2020 2020 2020 2020 290a     ]).        ).
+0001eb00: 2020 2020 2020 2020 7265 7475 726e 2066          return f
+0001eb10: 6967 0a                                  ig.
```

### Comparing `helpsk-0.1.8/helpsk/sklearn_pipeline.py` & `helpsk-0.1.9/helpsk/sklearn_pipeline.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/sklearn_search.py` & `helpsk-0.1.9/helpsk/sklearn_search.py`

 * *Files 0% similar despite different names*

```diff
@@ -191,14 +191,15 @@
     @staticmethod
     def _search_space_support_vector_classification_linear(C=(1e-6, 100),  # noqa
                                                            imputer_strategies=['mean', 'median', 'most_frequent'],  # noqa
                                                            random_state=None):
         from skopt.space import Real, Categorical
 
         model = LinearSVC(
+            max_iter=1000,
             random_state=random_state
         )
 
         search_space = {
             'model': Categorical([model]),
             'model__C': Real(C[0], C[1], prior='log-uniform'),
         }
```

### Comparing `helpsk-0.1.8/helpsk/string.py` & `helpsk-0.1.9/helpsk/string.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/utility.py` & `helpsk-0.1.9/helpsk/utility.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk/validation.py` & `helpsk-0.1.9/helpsk/validation.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/helpsk.egg-info/PKG-INFO` & `helpsk-0.1.9/helpsk.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: helpsk
-Version: 0.1.8
+Version: 0.1.9
 Summary: Python helper functions and classes.
 Home-page: https://github.com/shanekercheval/python-helpers
 Author: Shane Kercheval
 Author-email: shane.kercheval@gmail.com
 License: UNKNOWN
 Project-URL: Bug Tracker, https://github.com/shanekercheval/python-helpers/issues
 Platform: UNKNOWN
```

### Comparing `helpsk-0.1.8/helpsk.egg-info/SOURCES.txt` & `helpsk-0.1.9/helpsk.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/setup.cfg` & `helpsk-0.1.9/setup.cfg`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = helpsk
-version = 0.1.8
+version = 0.1.9
 author = Shane Kercheval
 author_email = shane.kercheval@gmail.com
 description = Python helper functions and classes.
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/shanekercheval/python-helpers
 project_urls =
```

### Comparing `helpsk-0.1.8/tests/helpers.py` & `helpsk-0.1.9/tests/helpers.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/tests/test_color.py` & `helpsk-0.1.9/tests/test_color.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/tests/test_database.py` & `helpsk-0.1.9/tests/test_database.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/tests/test_date.py` & `helpsk-0.1.9/tests/test_date.py`

 * *Files 1% similar despite different names*

```diff
@@ -790,15 +790,15 @@
                                     fiscal_start=6),
                          parse('2021-12-01').date())
         self.assertEqual(date.floor(parse('2021-12-31'), granularity=date.Granularity.QUARTER,
                                     fiscal_start=6),
                          parse('2021-12-01').date())
 
     def test_floor_series(self):
-        date_series = pd.Series(pd.to_datetime([
+        datetimes = pd.to_datetime([
             '2021-01-01 00:00:00', '2021-01-01 00:00:01',
             np.NaN,
             '2021-01-02 00:00:01', '2021-01-02 23:59:59',
             '2021-02-01 00:00:00', '2021-02-01 00:00:01',
             np.NaN,
             '2021-02-02 00:00:01', '2021-02-02 23:59:59',
             '2021-03-01 00:00:00', '2021-03-01 00:00:01',
@@ -827,15 +827,17 @@
             '2021-10-02 00:00:01', '2021-10-02 23:59:59',
             '2021-11-01 00:00:00', '2021-11-01 00:00:01',
             np.NaN,
             '2021-11-02 00:00:01', '2021-11-02 23:59:59',
             '2021-12-01 00:00:00', '2021-12-01 00:00:01',
             np.NaN,
             '2021-12-02 00:00:01', '2021-12-02 23:59:59',
-        ]))
+        ])
+        index_values = list(reversed(range(0, len(datetimes))))
+        date_series = pd.Series(datetimes, index=index_values)
         expected_day = pd.Series(pd.to_datetime([
             '2021-01-01', '2021-01-01',
             np.NaN,
             '2021-01-02', '2021-01-02',
             '2021-02-01', '2021-02-01',
             np.NaN,
             '2021-02-02', '2021-02-02',
@@ -865,15 +867,15 @@
             '2021-10-02', '2021-10-02',
             '2021-11-01', '2021-11-01',
             np.NaN,
             '2021-11-02', '2021-11-02',
             '2021-12-01', '2021-12-01',
             np.NaN,
             '2021-12-02', '2021-12-02',
-        ]))
+        ]), index=index_values)
         expected_month = pd.Series(pd.to_datetime([
             '2021-01-01', '2021-01-01',
             np.NaN,
             '2021-01-01', '2021-01-01',
             '2021-02-01', '2021-02-01',
             np.NaN,
             '2021-02-01', '2021-02-01',
@@ -903,15 +905,15 @@
             '2021-10-01', '2021-10-01',
             '2021-11-01', '2021-11-01',
             np.NaN,
             '2021-11-01', '2021-11-01',
             '2021-12-01', '2021-12-01',
             np.NaN,
             '2021-12-01', '2021-12-01',
-        ]))
+        ]), index=index_values)
         expected_quarter = pd.Series(pd.to_datetime([
             '2021-01-01', '2021-01-01',
             np.NaN,
             '2021-01-01', '2021-01-01',
             '2021-01-01', '2021-01-01',
             np.NaN,
             '2021-01-01', '2021-01-01',
@@ -941,53 +943,54 @@
             '2021-10-01', '2021-10-01',
             '2021-10-01', '2021-10-01',
             np.NaN,
             '2021-10-01', '2021-10-01',
             '2021-10-01', '2021-10-01',
             np.NaN,
             '2021-10-01', '2021-10-01',
-        ]))
+        ]), index=index_values)
 
         # without series.name
         validation.assert_dataframes_match([
             pd.DataFrame(date_series.dt.date),
             pd.DataFrame(expected_day.dt.date),
             pd.DataFrame(date.floor(date_series, granularity=date.Granularity.DAY))
-        ])
+        ], ignore_indexes=False)
 
         validation.assert_dataframes_match([
             pd.DataFrame(expected_month.dt.date),
             pd.DataFrame(date.floor(date_series, granularity=date.Granularity.MONTH))
-        ])
+        ], ignore_indexes=False)
 
         validation.assert_dataframes_match([
             pd.DataFrame(expected_quarter.dt.date),
             pd.DataFrame(date.floor(date_series, granularity=date.Granularity.QUARTER))
-        ])
+        ], ignore_indexes=False)
 
         # with series.name
         date_series.name = 'date_day'
         expected_day.name = 'date_day'
         actual_values = date.floor(date_series, granularity=date.Granularity.DAY)
+
         self.assertEqual(actual_values.name, 'date_day')
         validation.assert_dataframes_match([
             pd.DataFrame(expected_day.dt.date),
             pd.DataFrame(actual_values)
-        ])
+        ], ignore_indexes=False)
 
         date_series.name = 'date_month'
         expected_day.name = 'date_month'
         actual_values = date.floor(date_series, granularity=date.Granularity.MONTH)
         self.assertEqual(actual_values.name, 'date_month')
         validation.assert_dataframes_match([
             pd.DataFrame(expected_month.dt.date),
             pd.DataFrame(actual_values)
-        ])
+        ], ignore_indexes=False)
 
         date_series.name = 'date_quarter'
         expected_day.name = 'date_quarter'
         actual_values = date.floor(date_series, granularity=date.Granularity.QUARTER)
         self.assertEqual(actual_values.name, 'date_quarter')
         validation.assert_dataframes_match([
             pd.DataFrame(expected_quarter.dt.date),
             pd.DataFrame(actual_values)
-        ])
+        ], ignore_indexes=False)
```

### Comparing `helpsk-0.1.8/tests/test_docstring_markdown.py` & `helpsk-0.1.9/tests/test_docstring_markdown.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/tests/test_pandas.py` & `helpsk-0.1.9/tests/test_pandas.py`

 * *Files 0% similar despite different names*

```diff
@@ -550,15 +550,15 @@
 
         self.helper_test_summary(get_test_path() + '/test_files/pandas/test_non_numeric_summary__style__credit__all_missing.html',
                                  clean_formatted_dataframe(non_numeric_summary(test_data, return_style=True, sort_by_columns=False).render()))
 
         self.helper_test_summary(get_test_path() + '/test_files/pandas/test_non_numeric_summary__style__credit__all_missing__sorted.html',
                                  clean_formatted_dataframe(non_numeric_summary(test_data, return_style=True, sort_by_columns=True).render()))
 
-    def test_non_numeric_summarytest_non_numeric_summary_test(self):
+    def test_non_numeric_summary2(self):
         test_data = self.credit_data.copy()
         test_data['purpose'] = test_data['purpose'].replace({'radio/tv': '1111111111222222222233333333334444444444'})
         test_data.loc[25:75, ['checking_status']] = np.nan
 
         self.helper_test_summary(get_test_path() + '/test_files/pandas/test_non_numeric_summary__style__credit.html',
                                  clean_formatted_dataframe(non_numeric_summary(test_data, return_style=True, sort_by_columns=False).render()))
 
@@ -732,17 +732,17 @@
             counts = count_groups(dataframe=data,
                                   group_1=group_1,
                                   group_2=group_2,
                                   group_sum=group_sum,
                                   remove_first_level_duplicates=remove_first_level_duplicates,
                                   return_style=False)
 
-            file_name = get_test_path() + f'/test_files/pandas/count_groups_{group_1}_{group_2}_' \
-                                          f'{group_sum}_{remove_first_level_duplicates}.txt'
-            with redirect_stdout_to_file(file_name):
+            name = get_test_path() + f'/test_files/pandas/count_groups_{group_1}_{group_2}_' \
+                                     f'{group_sum}_{remove_first_level_duplicates}.txt'
+            with redirect_stdout_to_file(name):
                 print_dataframe(counts)
             return counts
 
         results_1 = test_count_groups(group_1='target', remove_first_level_duplicates=False)
         self.assertEqual(results_1[('target', 'Count')].sum(),  data.shape[0])
         assert_is_close(results_1[('target', 'Count Perc')].sum(), 1)
```

### Comparing `helpsk-0.1.8/tests/test_pandas_style.py` & `helpsk-0.1.9/tests/test_pandas_style.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/tests/test_plot.py` & `helpsk-0.1.9/tests/test_plot.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/tests/test_sklearn_eval.py` & `helpsk-0.1.9/tests/test_sklearn_eval.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/tests/test_sklearn_search.py` & `helpsk-0.1.9/tests/test_sklearn_search.py`

 * *Files 1% similar despite different names*

```diff
@@ -131,15 +131,14 @@
         del logistic_space
 
         # search space for logistic regression with modified params
         logistic_space = ClassifierSearchSpace._search_space_logistic(
             solver='sag',
             max_iter=999,
             C=(1e-5, 1e+3),  # noqa
-            C_prior='uniform',  # noqa
             imputer_strategies=['most_frequent'],  # noqa
             random_state=42
         )
         self.assertEqual(list(logistic_space.keys()),
                          ['model',
                           'model__C',
                           'prep__numeric__imputer__transformer',
@@ -150,18 +149,22 @@
         del logistic_space
 
         # default space for xgboost
         xgboost_space = ClassifierSearchSpace._search_space_xgboost()
         self.assertEqual(list(xgboost_space.keys()),
                          ['model',
                           'model__max_depth',
-                          'model__n_estimators',
                           'model__learning_rate',
-                          'model__colsample_bytree',
+                          'model__n_estimators',
+                          'model__min_child_weight',
                           'model__subsample',
+                          'model__colsample_bytree',
+                          'model__colsample_bylevel',
+                          'model__reg_alpha',
+                          'model__reg_lambda',
                           'prep__numeric__imputer__transformer',
                           'prep__numeric__scaler__transformer',
                           'prep__non_numeric__encoder__transformer'])
         with open(get_test_path() + '/test_files/sklearn_search/xgboost_space_default.txt', 'w') as file:
             file.write(to_string(xgboost_space))
         del xgboost_space
 
@@ -176,18 +179,22 @@
             subsample=(0.1111, 0.999),
             imputer_strategies=['median'],
             random_state=42
         )
         self.assertEqual(list(xgboost_space.keys()),
                          ['model',
                           'model__max_depth',
-                          'model__n_estimators',
                           'model__learning_rate',
-                          'model__colsample_bytree',
+                          'model__n_estimators',
+                          'model__min_child_weight',
                           'model__subsample',
+                          'model__colsample_bytree',
+                          'model__colsample_bylevel',
+                          'model__reg_alpha',
+                          'model__reg_lambda',
                           'prep__numeric__imputer__transformer',
                           'prep__numeric__scaler__transformer',
                           'prep__non_numeric__encoder__transformer'])
         with open(get_test_path() + '/test_files/sklearn_search/xgboost_space_modified.txt', 'w') as file:
             file.write(to_string(xgboost_space))
         del xgboost_space
 
@@ -203,17 +210,14 @@
 
         mappings = self.default_search_space.param_name_mappings()
         with open(get_test_path() + '/test_files/sklearn_search/param_name_mappings_default.txt', 'w') as file:
             file.write(to_string(mappings))
 
     def test_MLExperimentResults_multi_model(self):
 
-        from xgboost import XGBClassifier
-        XGBClassifier()
-
         results = MLExperimentResults.from_sklearn_search_cv(
             searcher=self.bayes_search,
             higher_score_is_better=True,
             description='BayesSearchCV using ClassifierSearchSpace',
             parameter_name_mappings=self.search_space_used.param_name_mappings()
         )
 
@@ -481,12 +485,13 @@
         del labels
 
         _ = results.plot_performance_across_trials(facet_by='model')
         _ = results.plot_performance_across_trials(query='model == "XGBClassifier(...)"')
         _ = results.plot_parameter_values_across_trials(query='model == "XGBClassifier(...)"')
         _ = results.plot_parallel_coordinates(query='model == "XGBClassifier(...)"')
         _ = results.plot_scatter_matrix(query='model == "XGBClassifier(...)"')
-        _ = results.plot_score_vs_parameter(query='model == "XGBClassifier(...)"')
+        _ = results.plot_score_vs_parameter(parameter='max_depth', query='model == "XGBClassifier(...)"')
         _ = results.plot_parameter_values_across_trials(query='model == "XGBClassifier(...)"')
-        _ = results.plot_parameter_vs_parameter(query='model == "XGBClassifier(...)"')
+        _ = results.plot_parameter_vs_parameter(parameter_x='max_depth', parameter_y='min_child_weight',
+                                                query='model == "XGBClassifier(...)"')
         _ = results.plot_performance_non_numeric_params(query='model == "XGBClassifier(...)"')
         _ = results.plot_performance_numeric_params(query='model == "XGBClassifier(...)"')
```

### Comparing `helpsk-0.1.8/tests/test_string.py` & `helpsk-0.1.9/tests/test_string.py`

 * *Files identical despite different names*

### Comparing `helpsk-0.1.8/tests/test_validation.py` & `helpsk-0.1.9/tests/test_validation.py`

 * *Files identical despite different names*

