# Comparing `tmp/skynamo-0.0.8.tar.gz` & `tmp/skynamo-0.0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "skynamo-0.0.8.tar", last modified: Thu Mar 23 11:56:58 2023, max compression
+gzip compressed data, was "skynamo-0.0.9.tar", last modified: Thu Mar 23 12:31:48 2023, max compression
```

## Comparing `skynamo-0.0.8.tar` & `skynamo-0.0.9.tar`

### file list

```diff
@@ -1,63 +1,63 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.529729 skynamo-0.0.8/
--rw-r--r--   0 root         (0) root         (0)     1063 2023-03-06 12:30:39.000000 skynamo-0.0.8/LICENSE.txt
--rw-r--r--   0 root         (0) root         (0)      226 2023-03-23 11:56:58.529729 skynamo-0.0.8/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     5249 2023-03-06 12:40:05.000000 skynamo-0.0.8/README.md
--rw-r--r--   0 root         (0) root         (0)       38 2023-03-23 11:56:58.529729 skynamo-0.0.8/setup.cfg
--rw-r--r--   0 root         (0) root         (0)      862 2023-03-23 11:56:38.000000 skynamo-0.0.8/setup.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.509729 skynamo-0.0.8/skynamo/
--rw-r--r--   0 root         (0) root         (0)      480 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.517728 skynamo-0.0.8/skynamo/main/
--rw-r--r--   0 root         (0) root         (0)      333 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/main/CreditRequest.py
--rw-r--r--   0 root         (0) root         (0)      339 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/main/CustomForm.py
--rw-r--r--   0 root         (0) root         (0)     1335 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/main/Customer.py
--rw-r--r--   0 root         (0) root         (0)      325 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/main/Order.py
--rw-r--r--   0 root         (0) root         (0)      796 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/main/Product.py
--rw-r--r--   0 root         (0) root         (0)      325 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/main/Quote.py
--rw-r--r--   0 root         (0) root         (0)     3661 2023-03-08 09:29:24.000000 skynamo-0.0.8/skynamo/main/Reader.py
--rw-r--r--   0 root         (0) root         (0)     3828 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/main/Writer.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/main/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.521729 skynamo-0.0.8/skynamo/models/
--rw-r--r--   0 root         (0) root         (0)      546 2023-03-06 12:40:05.000000 skynamo-0.0.8/skynamo/models/Address.py
--rw-r--r--   0 root         (0) root         (0)      912 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/CustomFieldsToCreate.py
--rw-r--r--   0 root         (0) root         (0)      592 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/CustomFormBase.py
--rw-r--r--   0 root         (0) root         (0)     1809 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/Invoice.py
--rw-r--r--   0 root         (0) root         (0)      624 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/InvoiceItem.py
--rw-r--r--   0 root         (0) root         (0)      604 2023-03-06 12:40:05.000000 skynamo-0.0.8/skynamo/models/LineItem.py
--rw-r--r--   0 root         (0) root         (0)      456 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/Location.py
--rw-r--r--   0 root         (0) root         (0)      215 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/OrderUnit.py
--rw-r--r--   0 root         (0) root         (0)      678 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/Price.py
--rw-r--r--   0 root         (0) root         (0)      867 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/StockLevel.py
--rw-r--r--   0 root         (0) root         (0)     1662 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/Transaction.py
--rw-r--r--   0 root         (0) root         (0)      318 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/User.py
--rw-r--r--   0 root         (0) root         (0)      485 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/Warehouse.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/models/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.525729 skynamo-0.0.8/skynamo/outputters/
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/outputters/__init__.py
--rw-r--r--   0 root         (0) root         (0)      970 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/outputters/csvWriter.py
--rw-r--r--   0 root         (0) root         (0)     1606 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/outputters/emailer.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.525729 skynamo-0.0.8/skynamo/reader/
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/reader/__init__.py
--rw-r--r--   0 root         (0) root         (0)     3220 2023-03-08 09:29:24.000000 skynamo-0.0.8/skynamo/reader/jsonToObjects.py
--rw-r--r--   0 root         (0) root         (0)     5206 2023-03-08 09:29:24.000000 skynamo-0.0.8/skynamo/reader/sync.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.529729 skynamo-0.0.8/skynamo/refresher/
--rw-r--r--   0 root         (0) root         (0)     3744 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/refresher/CustomFieldArg.py
--rw-r--r--   0 root         (0) root         (0)     6416 2023-03-23 11:56:38.000000 skynamo-0.0.8/skynamo/refresher/InstanceClassContentsCls.py
--rw-r--r--   0 root         (0) root         (0)     1302 2023-03-08 09:29:24.000000 skynamo-0.0.8/skynamo/refresher/__init__.py
--rw-r--r--   0 root         (0) root         (0)      618 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/refresher/refreshHelpers.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.529729 skynamo-0.0.8/skynamo/shared/
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/shared/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1521 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/shared/api.py
--rw-r--r--   0 root         (0) root         (0)     2137 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/shared/helpers.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.529729 skynamo-0.0.8/skynamo/writer/
--rw-r--r--   0 root         (0) root         (0)      236 2023-03-23 11:11:21.000000 skynamo-0.0.8/skynamo/writer/WriteErrorCls.py
--rw-r--r--   0 root         (0) root         (0)      364 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/writer/WriteOperationCls.py
--rw-r--r--   0 root         (0) root         (0)     4225 2023-03-22 15:20:51.000000 skynamo-0.0.8/skynamo/writer/WriterBase.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/writer/__init__.py
--rw-r--r--   0 root         (0) root         (0)     2101 2023-03-23 11:11:21.000000 skynamo-0.0.8/skynamo/writer/execute.py
--rw-r--r--   0 root         (0) root         (0)     4502 2023-03-06 12:30:39.000000 skynamo-0.0.8/skynamo/writer/writeHelpers.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 11:56:58.509729 skynamo-0.0.8/skynamo.egg-info/
--rw-r--r--   0 root         (0) root         (0)      226 2023-03-23 11:56:58.000000 skynamo-0.0.8/skynamo.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     1401 2023-03-23 11:56:58.000000 skynamo-0.0.8/skynamo.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-03-23 11:56:58.000000 skynamo-0.0.8/skynamo.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)        9 2023-03-23 11:56:58.000000 skynamo-0.0.8/skynamo.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)        8 2023-03-23 11:56:58.000000 skynamo-0.0.8/skynamo.egg-info/top_level.txt
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.611447 skynamo-0.0.9/
+-rw-r--r--   0 root         (0) root         (0)     1063 2023-03-06 12:30:39.000000 skynamo-0.0.9/LICENSE.txt
+-rw-r--r--   0 root         (0) root         (0)      226 2023-03-23 12:31:48.611447 skynamo-0.0.9/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     5249 2023-03-06 12:40:05.000000 skynamo-0.0.9/README.md
+-rw-r--r--   0 root         (0) root         (0)       38 2023-03-23 12:31:48.611447 skynamo-0.0.9/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      862 2023-03-23 12:31:10.000000 skynamo-0.0.9/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.591447 skynamo-0.0.9/skynamo/
+-rw-r--r--   0 root         (0) root         (0)      480 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.595447 skynamo-0.0.9/skynamo/main/
+-rw-r--r--   0 root         (0) root         (0)      333 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/main/CreditRequest.py
+-rw-r--r--   0 root         (0) root         (0)      339 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/main/CustomForm.py
+-rw-r--r--   0 root         (0) root         (0)     1335 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/main/Customer.py
+-rw-r--r--   0 root         (0) root         (0)      325 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/main/Order.py
+-rw-r--r--   0 root         (0) root         (0)      796 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/main/Product.py
+-rw-r--r--   0 root         (0) root         (0)      325 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/main/Quote.py
+-rw-r--r--   0 root         (0) root         (0)     3661 2023-03-08 09:29:24.000000 skynamo-0.0.9/skynamo/main/Reader.py
+-rw-r--r--   0 root         (0) root         (0)     3828 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/main/Writer.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/main/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.603447 skynamo-0.0.9/skynamo/models/
+-rw-r--r--   0 root         (0) root         (0)      546 2023-03-06 12:40:05.000000 skynamo-0.0.9/skynamo/models/Address.py
+-rw-r--r--   0 root         (0) root         (0)      912 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/CustomFieldsToCreate.py
+-rw-r--r--   0 root         (0) root         (0)      592 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/CustomFormBase.py
+-rw-r--r--   0 root         (0) root         (0)     1809 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/Invoice.py
+-rw-r--r--   0 root         (0) root         (0)      624 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/InvoiceItem.py
+-rw-r--r--   0 root         (0) root         (0)      604 2023-03-06 12:40:05.000000 skynamo-0.0.9/skynamo/models/LineItem.py
+-rw-r--r--   0 root         (0) root         (0)      456 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/Location.py
+-rw-r--r--   0 root         (0) root         (0)      215 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/OrderUnit.py
+-rw-r--r--   0 root         (0) root         (0)      678 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/Price.py
+-rw-r--r--   0 root         (0) root         (0)      867 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/StockLevel.py
+-rw-r--r--   0 root         (0) root         (0)     1662 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/Transaction.py
+-rw-r--r--   0 root         (0) root         (0)      318 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/User.py
+-rw-r--r--   0 root         (0) root         (0)      485 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/Warehouse.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/models/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.603447 skynamo-0.0.9/skynamo/outputters/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/outputters/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      970 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/outputters/csvWriter.py
+-rw-r--r--   0 root         (0) root         (0)     1606 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/outputters/emailer.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.603447 skynamo-0.0.9/skynamo/reader/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/reader/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     3220 2023-03-08 09:29:24.000000 skynamo-0.0.9/skynamo/reader/jsonToObjects.py
+-rw-r--r--   0 root         (0) root         (0)     5206 2023-03-08 09:29:24.000000 skynamo-0.0.9/skynamo/reader/sync.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.607447 skynamo-0.0.9/skynamo/refresher/
+-rw-r--r--   0 root         (0) root         (0)     3744 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/refresher/CustomFieldArg.py
+-rw-r--r--   0 root         (0) root         (0)     6416 2023-03-23 11:56:38.000000 skynamo-0.0.9/skynamo/refresher/InstanceClassContentsCls.py
+-rw-r--r--   0 root         (0) root         (0)     1302 2023-03-08 09:29:24.000000 skynamo-0.0.9/skynamo/refresher/__init__.py
+-rw-r--r--   0 root         (0) root         (0)      618 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/refresher/refreshHelpers.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.607447 skynamo-0.0.9/skynamo/shared/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/shared/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1521 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/shared/api.py
+-rw-r--r--   0 root         (0) root         (0)     2137 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/shared/helpers.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.611447 skynamo-0.0.9/skynamo/writer/
+-rw-r--r--   0 root         (0) root         (0)      236 2023-03-23 11:11:21.000000 skynamo-0.0.9/skynamo/writer/WriteErrorCls.py
+-rw-r--r--   0 root         (0) root         (0)      364 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/writer/WriteOperationCls.py
+-rw-r--r--   0 root         (0) root         (0)     4247 2023-03-23 12:31:10.000000 skynamo-0.0.9/skynamo/writer/WriterBase.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/writer/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     2101 2023-03-23 11:11:21.000000 skynamo-0.0.9/skynamo/writer/execute.py
+-rw-r--r--   0 root         (0) root         (0)     4502 2023-03-06 12:30:39.000000 skynamo-0.0.9/skynamo/writer/writeHelpers.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-03-23 12:31:48.591447 skynamo-0.0.9/skynamo.egg-info/
+-rw-r--r--   0 root         (0) root         (0)      226 2023-03-23 12:31:48.000000 skynamo-0.0.9/skynamo.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     1401 2023-03-23 12:31:48.000000 skynamo-0.0.9/skynamo.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-03-23 12:31:48.000000 skynamo-0.0.9/skynamo.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)        9 2023-03-23 12:31:48.000000 skynamo-0.0.9/skynamo.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)        8 2023-03-23 12:31:48.000000 skynamo-0.0.9/skynamo.egg-info/top_level.txt
```

### Comparing `skynamo-0.0.8/LICENSE.txt` & `skynamo-0.0.9/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/README.md` & `skynamo-0.0.9/README.md`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/setup.py` & `skynamo-0.0.9/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -10,15 +10,15 @@
                 packageName=dependancy.split('/')[-1]
                 dependancy=packageName+" @ "+dependancy
             install_requires.append(dependancy)
 
 if __name__ == "__main__":
     setup(
         name='skynamo',
-        version='0.0.8',
+        version='0.0.9',
         author='Daniel van Niekerk',
         author_email='daniel@skynamo.com',
         description='Skynamo Public API SDK',
         url='https://github.com/skynamo/skynamo-python-sdk',
         packages=find_packages(),
         install_requires=install_requires
     )
```

### Comparing `skynamo-0.0.8/skynamo/main/Customer.py` & `skynamo-0.0.9/skynamo/main/Customer.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/main/Product.py` & `skynamo-0.0.9/skynamo/main/Product.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/main/Reader.py` & `skynamo-0.0.9/skynamo/main/Reader.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/main/Writer.py` & `skynamo-0.0.9/skynamo/main/Writer.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/models/Address.py` & `skynamo-0.0.9/skynamo/models/Address.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/models/CustomFieldsToCreate.py` & `skynamo-0.0.9/skynamo/models/CustomFieldsToCreate.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/models/CustomFormBase.py` & `skynamo-0.0.9/skynamo/models/CustomFormBase.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/models/Invoice.py` & `skynamo-0.0.9/skynamo/models/Invoice.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/models/InvoiceItem.py` & `skynamo-0.0.9/skynamo/models/InvoiceItem.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/models/LineItem.py` & `skynamo-0.0.9/skynamo/models/LineItem.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/models/Price.py` & `skynamo-0.0.9/skynamo/models/Price.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/models/StockLevel.py` & `skynamo-0.0.9/skynamo/models/StockLevel.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/models/Transaction.py` & `skynamo-0.0.9/skynamo/models/Transaction.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/outputters/csvWriter.py` & `skynamo-0.0.9/skynamo/outputters/csvWriter.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/outputters/emailer.py` & `skynamo-0.0.9/skynamo/outputters/emailer.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/reader/jsonToObjects.py` & `skynamo-0.0.9/skynamo/reader/jsonToObjects.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/reader/sync.py` & `skynamo-0.0.9/skynamo/reader/sync.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/refresher/CustomFieldArg.py` & `skynamo-0.0.9/skynamo/refresher/CustomFieldArg.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/refresher/InstanceClassContentsCls.py` & `skynamo-0.0.9/skynamo/refresher/InstanceClassContentsCls.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/refresher/__init__.py` & `skynamo-0.0.9/skynamo/refresher/__init__.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/refresher/refreshHelpers.py` & `skynamo-0.0.9/skynamo/refresher/refreshHelpers.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/shared/api.py` & `skynamo-0.0.9/skynamo/shared/api.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/shared/helpers.py` & `skynamo-0.0.9/skynamo/shared/helpers.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/writer/WriterBase.py` & `skynamo-0.0.9/skynamo/writer/WriterBase.py`

 * *Files 2% similar despite different names*

```diff
@@ -64,11 +64,11 @@
 		self.writeOperations.append(WriteOperation("integrations", "post", {'action':'AddCustomFields','fields_to_add':customFieldsToCreate.fields_to_add},canBeCombinedWithOtherWritesInAList=False))
 
 	def addWarehouseCreate(self,name:str,order_email:str='',credit_request_email:str='',quote_email:str='',active:bool=True):
 		body=getBodyForWriteOperation(locals())
 		self.writeOperations.append(WriteOperation("warehouses", "post", body))
 
 	def addWarehouseUpdate(self,warehouse:Warehouse,fieldsToUpdate:List[Literal['name','order_email','credit_request_email','quote_email','active']]):
-		body={'id':warehouse.id}
+		body={'id':warehouse.id,'name':warehouse.name}
 		for field in fieldsToUpdate:
 			body[field]=getattr(warehouse,field)
 		self.writeOperations.append(WriteOperation("warehouses", "patch", body))
```

### Comparing `skynamo-0.0.8/skynamo/writer/execute.py` & `skynamo-0.0.9/skynamo/writer/execute.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo/writer/writeHelpers.py` & `skynamo-0.0.9/skynamo/writer/writeHelpers.py`

 * *Files identical despite different names*

### Comparing `skynamo-0.0.8/skynamo.egg-info/SOURCES.txt` & `skynamo-0.0.9/skynamo.egg-info/SOURCES.txt`

 * *Files identical despite different names*

