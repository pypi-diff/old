# Comparing `tmp/hshshshs-0.0.7.tar.gz` & `tmp/hshshshs-0.0.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "hshshshs-0.0.7.tar", last modified: Thu Apr  6 09:44:56 2023, max compression
+gzip compressed data, was "hshshshs-0.0.8.tar", last modified: Thu Apr  6 10:28:51 2023, max compression
```

## Comparing `hshshshs-0.0.7.tar` & `hshshshs-0.0.8.tar`

### file list

```diff
@@ -1,13 +1,13 @@
-drwxrwxrwx   0        0        0        0 2023-04-06 09:44:56.004462 hshshshs-0.0.7/
--rw-rw-rw-   0        0        0      261 2023-04-06 09:44:56.004462 hshshshs-0.0.7/PKG-INFO
-drwxrwxrwx   0        0        0        0 2023-04-06 09:44:56.004462 hshshshs-0.0.7/hshshshs/
--rw-rw-rw-   0        0        0        0 2023-03-17 08:41:46.000000 hshshshs-0.0.7/hshshshs/__init__.py
--rw-rw-rw-   0        0        0     1935 2023-03-29 12:36:59.000000 hshshshs-0.0.7/hshshshs/cFunction.py
-drwxrwxrwx   0        0        0        0 2023-04-06 09:44:56.004462 hshshshs-0.0.7/hshshshs.egg-info/
--rw-rw-rw-   0        0        0      261 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      210 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0        8 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/requires.txt
--rw-rw-rw-   0        0        0        9 2023-04-06 09:44:55.000000 hshshshs-0.0.7/hshshshs.egg-info/top_level.txt
--rw-rw-rw-   0        0        0       42 2023-04-06 09:44:56.004462 hshshshs-0.0.7/setup.cfg
--rw-rw-rw-   0        0        0      978 2023-04-06 09:44:20.000000 hshshshs-0.0.7/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:28:51.760508 hshshshs-0.0.8/
+-rw-rw-rw-   0        0        0      261 2023-04-06 10:28:51.759508 hshshshs-0.0.8/PKG-INFO
+drwxrwxrwx   0        0        0        0 2023-04-06 10:28:51.734528 hshshshs-0.0.8/hshshshs/
+-rw-rw-rw-   0        0        0        0 2023-03-17 08:41:46.000000 hshshshs-0.0.8/hshshshs/__init__.py
+-rw-rw-rw-   0        0        0     2834 2023-04-06 10:27:40.000000 hshshshs-0.0.8/hshshshs/cFunction.py
+drwxrwxrwx   0        0        0        0 2023-04-06 10:28:51.758509 hshshshs-0.0.8/hshshshs.egg-info/
+-rw-rw-rw-   0        0        0      261 2023-04-06 10:28:51.000000 hshshshs-0.0.8/hshshshs.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      210 2023-04-06 10:28:51.000000 hshshshs-0.0.8/hshshshs.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-06 10:28:51.000000 hshshshs-0.0.8/hshshshs.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0        8 2023-04-06 10:28:51.000000 hshshshs-0.0.8/hshshshs.egg-info/requires.txt
+-rw-rw-rw-   0        0        0        9 2023-04-06 10:28:51.000000 hshshshs-0.0.8/hshshshs.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0       42 2023-04-06 10:28:51.760508 hshshshs-0.0.8/setup.cfg
+-rw-rw-rw-   0        0        0      978 2023-04-06 10:27:10.000000 hshshshs-0.0.8/setup.py
```

### Comparing `hshshshs-0.0.7/hshshshs/cFunction.py` & `hshshshs-0.0.8/hshshshs/cFunction.py`

 * *Files 20% similar despite different names*

```diff
@@ -58,8 +58,38 @@
             month = month +1
             backNum = backNum - 1;
             if month == 0:
                 year = year + 1
                 month = Week.last_week_of_year(year).week  
     
     newYearMonth = str(year)+str(month).zfill(2)
-    return newYearMonth
+    return newYearMonth
+
+
+import datetime
+from dateutil.relativedelta import relativedelta
+def monthCal(yearMonthDay, dayCal,flag = True):
+    year = 0
+    month = 0
+    day = 0
+    dividyear = 4
+    dividmonth = 6
+
+    if type(yearMonthDay) == str :
+            year  = yearMonthDay[:dividyear]
+            month = yearMonthDay[dividyear:dividmonth]
+            day = yearMonthDay[dividmonth:]
+            year = int(year)
+            month = int(month)
+            day = int(day)
+
+
+    if type(dayCal) == str:
+            dayCal = int(dayCal)
+    if flag == True:
+        checkMonth = datetime.date(year,month,day) + relativedelta(months=dayCal)
+        calChekMonth = str(checkMonth.year) + str(checkMonth.month).zfill(2)
+    else:
+        checkMonth = datetime.date(year,month,day) + relativedelta(months=dayCal)
+        calChekMonth = str(checkMonth.year) + str(checkMonth.month).zfill(2)
+    
+    return calChekMonth
```

### Comparing `hshshshs-0.0.7/setup.py` & `hshshshs-0.0.8/setup.py`

 * *Files 13% similar despite different names*

```diff
@@ -15,15 +15,15 @@
                 module_name = "%(base)s.%(item)s" % vars()
             else:
                 module_name = item
             packages[module_name] = dir
             packages.update(find_packages(dir, module_name))
     return packages
 setup(  name="hshshshs",
-        version="0.0.7",
+        version="0.0.8",
         url="http://github.com/kimhansu/hshshshs",
         license="MIT",
         author="kimhansu",
         author_email="gimhansu@naver.com",
         keywords=["calendar","isoweek","listsum"],
         description="math function",
         packages=find_packages("."),
```

