# Comparing `tmp/AbsBox-0.9.2.tar.gz` & `tmp/AbsBox-0.9.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "AbsBox-0.9.2.tar", last modified: Sat Mar 18 15:29:40 2023, max compression
+gzip compressed data, was "AbsBox-0.9.3.tar", last modified: Sat Mar 18 16:16:46 2023, max compression
```

## Comparing `AbsBox-0.9.2.tar` & `AbsBox-0.9.3.tar`

### file list

```diff
@@ -1,21 +1,21 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 15:29:40.538883 AbsBox-0.9.2/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 15:29:40.538883 AbsBox-0.9.2/AbsBox.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     1743 2023-03-18 15:29:40.000000 AbsBox-0.9.2/AbsBox.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      335 2023-03-18 15:29:40.000000 AbsBox-0.9.2/AbsBox.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-18 15:29:40.000000 AbsBox-0.9.2/AbsBox.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       75 2023-03-18 15:29:40.000000 AbsBox-0.9.2/AbsBox.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)        7 2023-03-18 15:29:40.000000 AbsBox-0.9.2/AbsBox.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (123)    11346 2023-03-18 15:29:24.000000 AbsBox-0.9.2/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)     1743 2023-03-18 15:29:40.538883 AbsBox-0.9.2/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      957 2023-03-18 15:29:24.000000 AbsBox-0.9.2/README.md
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 15:29:40.538883 AbsBox-0.9.2/absbox/
--rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-18 15:29:24.000000 AbsBox-0.9.2/absbox/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    12306 2023-03-18 15:29:24.000000 AbsBox-0.9.2/absbox/client.py
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 15:29:40.538883 AbsBox-0.9.2/absbox/local/
--rw-r--r--   0 runner    (1001) docker     (123)     1810 2023-03-18 15:29:24.000000 AbsBox-0.9.2/absbox/local/base.py
--rw-r--r--   0 runner    (1001) docker     (123)    14282 2023-03-18 15:29:24.000000 AbsBox-0.9.2/absbox/local/china.py
--rw-r--r--   0 runner    (1001) docker     (123)    45013 2023-03-18 15:29:24.000000 AbsBox-0.9.2/absbox/local/component.py
--rw-r--r--   0 runner    (1001) docker     (123)     5890 2023-03-18 15:29:24.000000 AbsBox-0.9.2/absbox/local/generic.py
--rw-r--r--   0 runner    (1001) docker     (123)     9354 2023-03-18 15:29:24.000000 AbsBox-0.9.2/absbox/local/util.py
--rw-r--r--   0 runner    (1001) docker     (123)       79 2023-03-18 15:29:40.542883 AbsBox-0.9.2/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (123)     1646 2023-03-18 15:29:24.000000 AbsBox-0.9.2/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 16:16:46.031669 AbsBox-0.9.3/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 16:16:46.027669 AbsBox-0.9.3/AbsBox.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1743 2023-03-18 16:16:46.000000 AbsBox-0.9.3/AbsBox.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      335 2023-03-18 16:16:46.000000 AbsBox-0.9.3/AbsBox.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-03-18 16:16:46.000000 AbsBox-0.9.3/AbsBox.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       75 2023-03-18 16:16:46.000000 AbsBox-0.9.3/AbsBox.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-03-18 16:16:46.000000 AbsBox-0.9.3/AbsBox.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (123)    11346 2023-03-18 16:16:31.000000 AbsBox-0.9.3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)     1743 2023-03-18 16:16:46.031669 AbsBox-0.9.3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      957 2023-03-18 16:16:31.000000 AbsBox-0.9.3/README.md
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 16:16:46.027669 AbsBox-0.9.3/absbox/
+-rw-r--r--   0 runner    (1001) docker     (123)      360 2023-03-18 16:16:31.000000 AbsBox-0.9.3/absbox/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    12306 2023-03-18 16:16:31.000000 AbsBox-0.9.3/absbox/client.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-03-18 16:16:46.031669 AbsBox-0.9.3/absbox/local/
+-rw-r--r--   0 runner    (1001) docker     (123)     1810 2023-03-18 16:16:31.000000 AbsBox-0.9.3/absbox/local/base.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14282 2023-03-18 16:16:31.000000 AbsBox-0.9.3/absbox/local/china.py
+-rw-r--r--   0 runner    (1001) docker     (123)    45071 2023-03-18 16:16:31.000000 AbsBox-0.9.3/absbox/local/component.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5683 2023-03-18 16:16:31.000000 AbsBox-0.9.3/absbox/local/generic.py
+-rw-r--r--   0 runner    (1001) docker     (123)     9354 2023-03-18 16:16:31.000000 AbsBox-0.9.3/absbox/local/util.py
+-rw-r--r--   0 runner    (1001) docker     (123)       79 2023-03-18 16:16:46.031669 AbsBox-0.9.3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)     1646 2023-03-18 16:16:32.000000 AbsBox-0.9.3/setup.py
```

### Comparing `AbsBox-0.9.2/AbsBox.egg-info/PKG-INFO` & `AbsBox-0.9.3/AbsBox.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: AbsBox
-Version: 0.9.2
+Version: 0.9.3
 Summary: an analytical library for cashflow modeling on ABS/MBS products
 Home-page: https://github.com/yellowbean/PyABS
 Download-URL: https://github.com/yellowbean/PyABS/archive/refs/tags/pre-release.tar.gz
 Author: xiaoyu,zhang
 Author-email: always.zhang@gmail.com
 License: Apache
 Keywords: MBS,ABS,Modelling,StructuredFinance,Cashflow
```

### Comparing `AbsBox-0.9.2/LICENSE` & `AbsBox-0.9.3/LICENSE`

 * *Files identical despite different names*

### Comparing `AbsBox-0.9.2/PKG-INFO` & `AbsBox-0.9.3/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: AbsBox
-Version: 0.9.2
+Version: 0.9.3
 Summary: an analytical library for cashflow modeling on ABS/MBS products
 Home-page: https://github.com/yellowbean/PyABS
 Download-URL: https://github.com/yellowbean/PyABS/archive/refs/tags/pre-release.tar.gz
 Author: xiaoyu,zhang
 Author-email: always.zhang@gmail.com
 License: Apache
 Keywords: MBS,ABS,Modelling,StructuredFinance,Cashflow
```

### Comparing `AbsBox-0.9.2/README.md` & `AbsBox-0.9.3/README.md`

 * *Files identical despite different names*

### Comparing `AbsBox-0.9.2/absbox/client.py` & `AbsBox-0.9.3/absbox/client.py`

 * *Files identical despite different names*

### Comparing `AbsBox-0.9.2/absbox/local/base.py` & `AbsBox-0.9.3/absbox/local/base.py`

 * *Files identical despite different names*

### Comparing `AbsBox-0.9.2/absbox/local/china.py` & `AbsBox-0.9.3/absbox/local/china.py`

 * *Files identical despite different names*

### Comparing `AbsBox-0.9.2/absbox/local/component.py` & `AbsBox-0.9.3/absbox/local/component.py`

 * *Files 0% similar despite different names*

```diff
@@ -956,15 +956,15 @@
     match x:
         case {"贴现日": pricingDay, "贴现曲线": xs} | {"PVDate": pricingDay, "PVCurve": xs}:
             # return [pricingDay, {"tag": "PricingCurve", "contents": xs}]
             return mkTag(("DiscountCurve",[pricingDay, mkTs("IRateCurve",xs)]))
         case {"债券":bnd_with_price,"利率曲线":rdps} | {"bonds":bnd_with_price,"curve":rdps}:
             return mkTag(("RunZSpread",[mkTs("IRateCurve",rdps) ,bnd_with_price ]))
         case _:
-            None
+            raise RuntimeError(f"Failed to match pricing assumption: {x}")
 
 # "{\"tag\":\"RunZSpread\",\"contents\":[{\"tag\":\"IRateCurve\",\"contents\":[[\"2020-01-01\",1.0e-2]]}
 #                                        ,{\"A\":[\"2021-01-01\",100.3]}]}"
 
 def mkLiqProviderType(x):
     match x:
         case {"总额度": amt} | {"Total": amt}:
```

### Comparing `AbsBox-0.9.2/absbox/local/generic.py` & `AbsBox-0.9.3/absbox/local/generic.py`

 * *Files 6% similar despite different names*

```diff
@@ -122,12 +122,10 @@
         output['pool'] = {}
         output['pool']['flow'] = pd.DataFrame([_['contents'] for _ in resp[0]['pool']['futureCf']]
                                               , columns=english_mortgage_flow_fields_d)
         pool_idx = 'Date'
         output['pool']['flow'] = output['pool']['flow'].set_index(pool_idx)
         output['pool']['flow'].index.rename(pool_idx, inplace=True)
 
-        output['pricing'] = pd.DataFrame.from_dict(resp[3]
-                                                   , orient='index'
-                                                   , columns=["pricing", "face", "WAL", "duration", "accure interest"]) if resp[3] else None
+        output['pricing'] = readPricingResult(resp[3], 'en')
 
         return output
```

### Comparing `AbsBox-0.9.2/absbox/local/util.py` & `AbsBox-0.9.3/absbox/local/util.py`

 * *Files identical despite different names*

### Comparing `AbsBox-0.9.2/setup.py` & `AbsBox-0.9.3/setup.py`

 * *Files 0% similar despite different names*

```diff
@@ -11,15 +11,15 @@
     setup(
         name = 'AbsBox',
         package_dir = {
             'absbox':'absbox',
             'absbox.local':local
         },
         packages = ['absbox','absbox.local'],
-        version = '0.9.2',
+        version = '0.9.3',
         license='Apache',
         description = 'an analytical library for cashflow modeling on ABS/MBS products',
         long_description_content_type='text/markdown',
         long_description = long_description,
         author = 'xiaoyu,zhang',
         author_email = 'always.zhang@gmail.com',
         url = 'https://github.com/yellowbean/PyABS',
```

