# Comparing `tmp/temporal-lib-0.0.4.tar.gz` & `tmp/temporal-lib-0.0.5.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "temporal-lib-0.0.4.tar", last modified: Mon Mar 20 15:55:07 2023, max compression
+gzip compressed data, was "temporal-lib-0.0.5.tar", last modified: Fri Apr  7 01:52:54 2023, max compression
```

## Comparing `temporal-lib-0.0.4.tar` & `temporal-lib-0.0.5.tar`

### file list

```diff
@@ -1,28 +1,28 @@
-drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-03-20 15:55:07.409438 temporal-lib-0.0.4/
--rw-r--r--   0 sysop     (1000) sysop     (1000)     1070 2023-03-11 23:45:16.000000 temporal-lib-0.0.4/LICENSE
--rw-r--r--   0 sysop     (1000) sysop     (1000)     2221 2023-03-20 15:55:07.409438 temporal-lib-0.0.4/PKG-INFO
--rw-r--r--   0 sysop     (1000) sysop     (1000)     1850 2023-03-08 16:52:08.000000 temporal-lib-0.0.4/README.md
--rw-r--r--   0 sysop     (1000) sysop     (1000)     1112 2023-03-20 15:55:00.000000 temporal-lib-0.0.4/pyproject.toml
--rw-r--r--   0 sysop     (1000) sysop     (1000)       38 2023-03-20 15:55:07.409438 temporal-lib-0.0.4/setup.cfg
-drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-03-20 15:55:07.405438 temporal-lib-0.0.4/src/
-drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-03-20 15:55:07.405438 temporal-lib-0.0.4/src/temporal_lib/
--rw-r--r--   0 sysop     (1000) sysop     (1000)     4058 2023-03-20 15:34:46.000000 temporal-lib-0.0.4/src/temporal_lib/__init__.py
--rw-r--r--   0 sysop     (1000) sysop     (1000)     6329 2023-03-19 23:43:59.000000 temporal-lib-0.0.4/src/temporal_lib/calendar.py
--rw-r--r--   0 sysop     (1000) sysop     (1000)     8058 2023-03-19 23:49:03.000000 temporal-lib-0.0.4/src/temporal_lib/core.py
-drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-03-20 15:55:07.405438 temporal-lib-0.0.4/src/temporal_lib/cron/
--rw-r--r--   0 sysop     (1000) sysop     (1000)     5899 2023-03-20 15:25:39.000000 temporal-lib-0.0.4/src/temporal_lib/cron/__init__.py
--rw-r--r--   0 sysop     (1000) sysop     (1000)     5966 2023-03-19 23:49:09.000000 temporal-lib-0.0.4/src/temporal_lib/tlib_date.py
--rw-r--r--   0 sysop     (1000) sysop     (1000)     9489 2023-03-20 15:29:47.000000 temporal-lib-0.0.4/src/temporal_lib/tlib_types.py
--rw-r--r--   0 sysop     (1000) sysop     (1000)     6964 2023-03-20 15:33:51.000000 temporal-lib-0.0.4/src/temporal_lib/tlib_week.py
--rw-r--r--   0 sysop     (1000) sysop     (1000)     2800 2023-03-19 23:26:05.000000 temporal-lib-0.0.4/src/temporal_lib/tlib_weekday.py
--rw-r--r--   0 sysop     (1000) sysop     (1000)     1040 2023-03-19 23:39:57.000000 temporal-lib-0.0.4/src/temporal_lib/tlib_year.py
-drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-03-20 15:55:07.405438 temporal-lib-0.0.4/src/temporal_lib.egg-info/
--rw-r--r--   0 sysop     (1000) sysop     (1000)     2221 2023-03-20 15:55:07.000000 temporal-lib-0.0.4/src/temporal_lib.egg-info/PKG-INFO
--rw-r--r--   0 sysop     (1000) sysop     (1000)      562 2023-03-20 15:55:07.000000 temporal-lib-0.0.4/src/temporal_lib.egg-info/SOURCES.txt
--rw-r--r--   0 sysop     (1000) sysop     (1000)        1 2023-03-20 15:55:07.000000 temporal-lib-0.0.4/src/temporal_lib.egg-info/dependency_links.txt
--rw-r--r--   0 sysop     (1000) sysop     (1000)      211 2023-03-20 15:55:07.000000 temporal-lib-0.0.4/src/temporal_lib.egg-info/requires.txt
--rw-r--r--   0 sysop     (1000) sysop     (1000)       13 2023-03-20 15:55:07.000000 temporal-lib-0.0.4/src/temporal_lib.egg-info/top_level.txt
-drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-03-20 15:55:07.405438 temporal-lib-0.0.4/tests/
--rw-r--r--   0 sysop     (1000) sysop     (1000)     2137 2023-03-19 22:14:07.000000 temporal-lib-0.0.4/tests/test_basics.py
--rw-r--r--   0 sysop     (1000) sysop     (1000)     2258 2023-03-19 23:48:00.000000 temporal-lib-0.0.4/tests/test_cron.py
--rw-r--r--   0 sysop     (1000) sysop     (1000)     4590 2023-03-19 23:49:43.000000 temporal-lib-0.0.4/tests/test_weeks.py
+drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-04-07 01:52:54.311199 temporal-lib-0.0.5/
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     1070 2023-03-11 23:45:16.000000 temporal-lib-0.0.5/LICENSE
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     2221 2023-04-07 01:52:54.311199 temporal-lib-0.0.5/PKG-INFO
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     1850 2023-03-08 16:52:08.000000 temporal-lib-0.0.5/README.md
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     1112 2023-04-07 01:41:39.000000 temporal-lib-0.0.5/pyproject.toml
+-rw-r--r--   0 sysop     (1000) sysop     (1000)       38 2023-04-07 01:52:54.311199 temporal-lib-0.0.5/setup.cfg
+drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-04-07 01:52:54.307198 temporal-lib-0.0.5/src/
+drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-04-07 01:52:54.311199 temporal-lib-0.0.5/src/temporal_lib/
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     4058 2023-03-20 15:34:46.000000 temporal-lib-0.0.5/src/temporal_lib/__init__.py
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     6329 2023-03-19 23:43:59.000000 temporal-lib-0.0.5/src/temporal_lib/calendar.py
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     7844 2023-04-07 01:43:41.000000 temporal-lib-0.0.5/src/temporal_lib/core.py
+drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-04-07 01:52:54.311199 temporal-lib-0.0.5/src/temporal_lib/cron/
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     5899 2023-03-20 15:25:39.000000 temporal-lib-0.0.5/src/temporal_lib/cron/__init__.py
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     5966 2023-03-19 23:49:09.000000 temporal-lib-0.0.5/src/temporal_lib/tlib_date.py
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     9489 2023-03-20 15:29:47.000000 temporal-lib-0.0.5/src/temporal_lib/tlib_types.py
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     6964 2023-03-20 15:33:51.000000 temporal-lib-0.0.5/src/temporal_lib/tlib_week.py
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     2800 2023-03-19 23:26:05.000000 temporal-lib-0.0.5/src/temporal_lib/tlib_weekday.py
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     1040 2023-03-19 23:39:57.000000 temporal-lib-0.0.5/src/temporal_lib/tlib_year.py
+drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-04-07 01:52:54.311199 temporal-lib-0.0.5/src/temporal_lib.egg-info/
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     2221 2023-04-07 01:52:54.000000 temporal-lib-0.0.5/src/temporal_lib.egg-info/PKG-INFO
+-rw-r--r--   0 sysop     (1000) sysop     (1000)      562 2023-04-07 01:52:54.000000 temporal-lib-0.0.5/src/temporal_lib.egg-info/SOURCES.txt
+-rw-r--r--   0 sysop     (1000) sysop     (1000)        1 2023-04-07 01:52:54.000000 temporal-lib-0.0.5/src/temporal_lib.egg-info/dependency_links.txt
+-rw-r--r--   0 sysop     (1000) sysop     (1000)      211 2023-04-07 01:52:54.000000 temporal-lib-0.0.5/src/temporal_lib.egg-info/requires.txt
+-rw-r--r--   0 sysop     (1000) sysop     (1000)       13 2023-04-07 01:52:54.000000 temporal-lib-0.0.5/src/temporal_lib.egg-info/top_level.txt
+drwxr-xr-x   0 sysop     (1000) sysop     (1000)        0 2023-04-07 01:52:54.311199 temporal-lib-0.0.5/tests/
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     2137 2023-03-19 22:14:07.000000 temporal-lib-0.0.5/tests/test_basics.py
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     2258 2023-03-19 23:48:00.000000 temporal-lib-0.0.5/tests/test_cron.py
+-rw-r--r--   0 sysop     (1000) sysop     (1000)     4590 2023-03-19 23:49:43.000000 temporal-lib-0.0.5/tests/test_weeks.py
```

### Comparing `temporal-lib-0.0.4/LICENSE` & `temporal-lib-0.0.5/LICENSE`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/PKG-INFO` & `temporal-lib-0.0.5/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: temporal-lib
-Version: 0.0.4
+Version: 0.0.5
 Summary: A library for working with datetime and other temporal concepts.
 Author-email: Datahenge LLC <brian@datahenge.com>
 License: MIT
 Keywords: datetime,cron
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
```

### Comparing `temporal-lib-0.0.4/README.md` & `temporal-lib-0.0.5/README.md`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/pyproject.toml` & `temporal-lib-0.0.5/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -17,15 +17,15 @@
 ]
 description = "A library for working with datetime and other temporal concepts."
 # dynamic =["version" ]
 keywords = ["datetime", "cron"]
 license = {text = "MIT"}
 requires-python = ">=3.7"
 readme = "README.md"
-version = "0.0.4"
+version = "0.0.5"
 
 
 dependencies = [
     "cron-converter",
     "cron-descriptor",
     "local-crontab",
     "python-dateutil>=2.8.2",
```

### Comparing `temporal-lib-0.0.4/src/temporal_lib/__init__.py` & `temporal-lib-0.0.5/src/temporal_lib/__init__.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/src/temporal_lib/calendar.py` & `temporal-lib-0.0.5/src/temporal_lib/calendar.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/src/temporal_lib/core.py` & `temporal-lib-0.0.5/src/temporal_lib/core.py`

 * *Files 8% similar despite different names*

```diff
@@ -105,22 +105,14 @@
 
 def make_datetime_naive(any_datetime):
 	"""
 	Takes a timezone-aware datetime, and makes it naive.
 	"""
 	return any_datetime.replace(tzinfo=None)
 
-def make_datetime_tz_aware(naive_datetime):
-	"""
-	Add the ERP system time zone to any naive datetime.
-	"""
-	if naive_datetime.tz_info:
-		raise ValueError("Datetime is already localized and time zone aware.")
-
-
 def localize_datetime(any_datetime, any_timezone):
 	"""
 	Given a naive datetime and time zone, return the localized datetime.
 
 	Necessary because Python is -extremely- confusing when it comes to datetime + timezone.
 	"""
 	if not isinstance(any_datetime, DateTimeType):
@@ -163,15 +155,15 @@
 
 def date_range(start_date, end_date) -> Generator:
 	"""
 	Generator for an inclusive range of dates.
 	It's very weird this isn't part of Python Standard Library or datetime  :/
 	"""
 
-	# As always, convert ERPNext strings into dates...
+	# Convert from Strings to Dates, if necessary.
 	start_date = any_to_date(start_date)
 	end_date = any_to_date(end_date)
 	# Important to add +1, otherwise the range is -not- inclusive.
 	for number_of_days in range(int((end_date - start_date).days) + 1):
 		yield start_date + timedelta(number_of_days)
 
 def date_range_from_strdates(start_date_str, end_date_str):
```

### Comparing `temporal-lib-0.0.4/src/temporal_lib/cron/__init__.py` & `temporal-lib-0.0.5/src/temporal_lib/cron/__init__.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/src/temporal_lib/tlib_date.py` & `temporal-lib-0.0.5/src/temporal_lib/tlib_date.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/src/temporal_lib/tlib_types.py` & `temporal-lib-0.0.5/src/temporal_lib/tlib_types.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/src/temporal_lib/tlib_week.py` & `temporal-lib-0.0.5/src/temporal_lib/tlib_week.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/src/temporal_lib/tlib_weekday.py` & `temporal-lib-0.0.5/src/temporal_lib/tlib_weekday.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/src/temporal_lib/tlib_year.py` & `temporal-lib-0.0.5/src/temporal_lib/tlib_year.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/src/temporal_lib.egg-info/PKG-INFO` & `temporal-lib-0.0.5/src/temporal_lib.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: temporal-lib
-Version: 0.0.4
+Version: 0.0.5
 Summary: A library for working with datetime and other temporal concepts.
 Author-email: Datahenge LLC <brian@datahenge.com>
 License: MIT
 Keywords: datetime,cron
 Classifier: Programming Language :: Python :: 3
 Requires-Python: >=3.7
 Description-Content-Type: text/markdown
```

### Comparing `temporal-lib-0.0.4/src/temporal_lib.egg-info/SOURCES.txt` & `temporal-lib-0.0.5/src/temporal_lib.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/tests/test_basics.py` & `temporal-lib-0.0.5/tests/test_basics.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/tests/test_cron.py` & `temporal-lib-0.0.5/tests/test_cron.py`

 * *Files identical despite different names*

### Comparing `temporal-lib-0.0.4/tests/test_weeks.py` & `temporal-lib-0.0.5/tests/test_weeks.py`

 * *Files identical despite different names*

