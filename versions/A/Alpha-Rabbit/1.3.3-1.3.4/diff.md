# Comparing `tmp/Alpha_Rabbit-1.3.3.tar.gz` & `tmp/Alpha_Rabbit-1.3.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "Alpha_Rabbit-1.3.3.tar", last modified: Fri Apr  7 05:49:57 2023, max compression
+gzip compressed data, was "Alpha_Rabbit-1.3.4.tar", last modified: Fri Apr  7 05:59:00 2023, max compression
```

## Comparing `Alpha_Rabbit-1.3.3.tar` & `Alpha_Rabbit-1.3.4.tar`

### file list

```diff
@@ -1,19 +1,19 @@
-drwxrwxrwx   0        0        0        0 2023-04-07 05:49:57.439457 Alpha_Rabbit-1.3.3/
-drwxrwxrwx   0        0        0        0 2023-04-07 05:49:57.431866 Alpha_Rabbit-1.3.3/Alpha_Rabbit/
--rw-rw-rw-   0        0        0    21291 2023-04-07 05:49:30.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit/Alpha_Rabbit.py
--rw-rw-rw-   0        0        0    13938 2023-03-24 06:59:51.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit/Factor_Calculator.py
--rw-rw-rw-   0        0        0    22640 2023-03-24 01:41:23.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit/Factor_Def_and_Get_Method.py
--rw-rw-rw-   0        0        0        0 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit/__init__.py
--rw-rw-rw-   0        0        0     1522 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit/trade_strategy.py
-drwxrwxrwx   0        0        0        0 2023-04-07 05:49:57.438464 Alpha_Rabbit-1.3.3/Alpha_Rabbit.egg-info/
--rw-rw-rw-   0        0        0      787 2023-04-07 05:49:57.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      411 2023-04-07 05:49:57.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2023-04-07 05:49:57.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       48 2023-04-07 05:49:57.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit.egg-info/requires.txt
--rw-rw-rw-   0        0        0       13 2023-04-07 05:49:57.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit.egg-info/top_level.txt
--rw-rw-rw-   0        0        0        2 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.3/Alpha_Rabbit.egg-info/zip-safe
--rw-rw-rw-   0        0        0     1094 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.3/LICENSE.txt
--rw-rw-rw-   0        0        0      787 2023-04-07 05:49:57.439457 Alpha_Rabbit-1.3.3/PKG-INFO
--rw-rw-rw-   0        0        0       69 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.3/README.md
--rw-rw-rw-   0        0        0       85 2023-04-07 05:49:57.440458 Alpha_Rabbit-1.3.3/setup.cfg
--rw-rw-rw-   0        0        0     1229 2023-04-07 05:49:41.000000 Alpha_Rabbit-1.3.3/setup.py
+drwxrwxrwx   0        0        0        0 2023-04-07 05:59:00.757271 Alpha_Rabbit-1.3.4/
+drwxrwxrwx   0        0        0        0 2023-04-07 05:59:00.752129 Alpha_Rabbit-1.3.4/Alpha_Rabbit/
+-rw-rw-rw-   0        0        0    21287 2023-04-07 05:53:45.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit/Alpha_Rabbit.py
+-rw-rw-rw-   0        0        0    13938 2023-03-24 06:59:51.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit/Factor_Calculator.py
+-rw-rw-rw-   0        0        0    22640 2023-03-24 01:41:23.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit/Factor_Def_and_Get_Method.py
+-rw-rw-rw-   0        0        0        0 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit/__init__.py
+-rw-rw-rw-   0        0        0     1522 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit/trade_strategy.py
+drwxrwxrwx   0        0        0        0 2023-04-07 05:59:00.756274 Alpha_Rabbit-1.3.4/Alpha_Rabbit.egg-info/
+-rw-rw-rw-   0        0        0      787 2023-04-07 05:59:00.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      411 2023-04-07 05:59:00.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-04-07 05:59:00.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       48 2023-04-07 05:59:00.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       13 2023-04-07 05:59:00.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit.egg-info/top_level.txt
+-rw-rw-rw-   0        0        0        2 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.4/Alpha_Rabbit.egg-info/zip-safe
+-rw-rw-rw-   0        0        0     1094 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.4/LICENSE.txt
+-rw-rw-rw-   0        0        0      787 2023-04-07 05:59:00.757271 Alpha_Rabbit-1.3.4/PKG-INFO
+-rw-rw-rw-   0        0        0       69 2023-02-27 02:16:19.000000 Alpha_Rabbit-1.3.4/README.md
+-rw-rw-rw-   0        0        0       85 2023-04-07 05:59:00.758780 Alpha_Rabbit-1.3.4/setup.cfg
+-rw-rw-rw-   0        0        0     1229 2023-04-07 05:58:52.000000 Alpha_Rabbit-1.3.4/setup.py
```

### Comparing `Alpha_Rabbit-1.3.3/Alpha_Rabbit/Alpha_Rabbit.py` & `Alpha_Rabbit-1.3.4/Alpha_Rabbit/Alpha_Rabbit.py`

 * *Files 0% similar despite different names*

```diff
@@ -93,15 +93,15 @@
         std_pvalue = data.groupby(level = 'date').apply(lambda x:x.std()).apply(lambda x: adfuller(x)[1])
         skew_pvalue = data.groupby(level = 'date').apply(lambda x:x.skew()).apply(lambda x: adfuller(x)[1])
         kurt_pvalue = data.groupby(level = 'date').apply(lambda x:x.kurt()).apply(lambda x: adfuller(x)[1])
         yarn_pvalue = pd.concat([mean_pvalue,std_pvalue,skew_pvalue,kurt_pvalue],axis = 1)
         yarn_pvalue.columns = ['mean','std','skew','kurt']
         return yarn_pvalue
     
-    def multif_cal_weight(self,factordf,factorlist,return_col,weight_type:str):
+    def multif_cal_weight(self,factordf,factorlist,return_col,weight_type):
         # factordf: pd.DataFrame
         # multiindex: timestamp,code
         # columns: factorname1, factorname2...,returndata
         # factorlist: strlist
         # return_col: column name, str
         df = factordf.copy()
         ret_k = df.groupby(level = 'date').apply(lambda x: sm.formula.ols(return_col+'~'+'+'.join(factorlist),data = x).fit().params)
```

### Comparing `Alpha_Rabbit-1.3.3/Alpha_Rabbit/Factor_Calculator.py` & `Alpha_Rabbit-1.3.4/Alpha_Rabbit/Factor_Calculator.py`

 * *Files identical despite different names*

### Comparing `Alpha_Rabbit-1.3.3/Alpha_Rabbit/Factor_Def_and_Get_Method.py` & `Alpha_Rabbit-1.3.4/Alpha_Rabbit/Factor_Def_and_Get_Method.py`

 * *Files identical despite different names*

### Comparing `Alpha_Rabbit-1.3.3/Alpha_Rabbit/trade_strategy.py` & `Alpha_Rabbit-1.3.4/Alpha_Rabbit/trade_strategy.py`

 * *Files identical despite different names*

### Comparing `Alpha_Rabbit-1.3.3/Alpha_Rabbit.egg-info/PKG-INFO` & `Alpha_Rabbit-1.3.4/Alpha_Rabbit.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Alpha-Rabbit
-Version: 1.3.3
+Version: 1.3.4
 Summary: Alpha_Rabbit
 Home-page: UNKNOWN
 Author: lijiongting
 Author-email: 448986334@qq.com
 License: MIT
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `Alpha_Rabbit-1.3.3/LICENSE.txt` & `Alpha_Rabbit-1.3.4/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `Alpha_Rabbit-1.3.3/PKG-INFO` & `Alpha_Rabbit-1.3.4/PKG-INFO`

 * *Files 12% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: Alpha_Rabbit
-Version: 1.3.3
+Version: 1.3.4
 Summary: Alpha_Rabbit
 Home-page: UNKNOWN
 Author: lijiongting
 Author-email: 448986334@qq.com
 License: MIT
 Platform: UNKNOWN
 Classifier: Intended Audience :: Developers
```

### Comparing `Alpha_Rabbit-1.3.3/setup.py` & `Alpha_Rabbit-1.3.4/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -9,15 +9,15 @@
 from setuptools import setup, find_packages
 
 with open("README.md", "r") as fh:
     long_description = fh.read()
 
 setup(
     name="Alpha_Rabbit",
-    version="1.3.3",
+    version="1.3.4",
     author="lijiongting",
     author_email="448986334@qq.com",
     description="Alpha_Rabbit",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license="MIT",
     url="",
```

