# Comparing `tmp/ydata_core-0.3.0-py2.py3-none-any.whl.zip` & `tmp/ydata_core-0.4.0rc1-py2.py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,11 +1,13 @@
-Zip file size: 3620 bytes, number of entries: 9
--rw-r--r--  2.0 unx        0 b- defN 23-Mar-28 08:11 ydata/core/__init__.py
--rw-r--r--  2.0 unx       67 b- defN 23-Mar-28 08:11 ydata/core/enum/__init__.py
--rw-r--r--  2.0 unx      664 b- defN 23-Mar-28 08:11 ydata/core/enum/string_enum.py
--rw-r--r--  2.0 unx       70 b- defN 23-Mar-28 08:11 ydata/core/error/__init__.py
--rw-r--r--  2.0 unx     1744 b- defN 23-Mar-28 08:11 ydata/core/error/fabric_error.py
--rw-r--r--  2.0 unx     1479 b- defN 23-Mar-28 08:11 ydata_core-0.3.0.dist-info/METADATA
--rw-r--r--  2.0 unx      110 b- defN 23-Mar-28 08:11 ydata_core-0.3.0.dist-info/WHEEL
--rw-r--r--  2.0 unx        6 b- defN 23-Mar-28 08:11 ydata_core-0.3.0.dist-info/top_level.txt
--rw-rw-r--  2.0 unx      726 b- defN 23-Mar-28 08:11 ydata_core-0.3.0.dist-info/RECORD
-9 files, 4866 bytes uncompressed, 2356 bytes compressed:  51.6%
+Zip file size: 4194 bytes, number of entries: 11
+-rw-r--r--  2.0 unx        0 b- defN 23-Apr-06 13:45 ydata/core/__init__.py
+-rw-r--r--  2.0 unx       59 b- defN 23-Apr-06 13:45 ydata/core/connectors/__init__.py
+-rw-r--r--  2.0 unx      134 b- defN 23-Apr-06 13:45 ydata/core/connectors/write_mode.py
+-rw-r--r--  2.0 unx       67 b- defN 23-Apr-06 13:45 ydata/core/enum/__init__.py
+-rw-r--r--  2.0 unx      664 b- defN 23-Apr-06 13:45 ydata/core/enum/string_enum.py
+-rw-r--r--  2.0 unx       70 b- defN 23-Apr-06 13:45 ydata/core/error/__init__.py
+-rw-r--r--  2.0 unx     1744 b- defN 23-Apr-06 13:45 ydata/core/error/fabric_error.py
+-rw-r--r--  2.0 unx     1482 b- defN 23-Apr-06 13:45 ydata_core-0.4.0rc1.dist-info/METADATA
+-rw-r--r--  2.0 unx      110 b- defN 23-Apr-06 13:45 ydata_core-0.4.0rc1.dist-info/WHEEL
+-rw-r--r--  2.0 unx        6 b- defN 23-Apr-06 13:45 ydata_core-0.4.0rc1.dist-info/top_level.txt
+-rw-rw-r--  2.0 unx      917 b- defN 23-Apr-06 13:45 ydata_core-0.4.0rc1.dist-info/RECORD
+11 files, 5253 bytes uncompressed, 2618 bytes compressed:  50.2%
```

## zipnote {}

```diff
@@ -1,28 +1,34 @@
 Filename: ydata/core/__init__.py
 Comment: 
 
+Filename: ydata/core/connectors/__init__.py
+Comment: 
+
+Filename: ydata/core/connectors/write_mode.py
+Comment: 
+
 Filename: ydata/core/enum/__init__.py
 Comment: 
 
 Filename: ydata/core/enum/string_enum.py
 Comment: 
 
 Filename: ydata/core/error/__init__.py
 Comment: 
 
 Filename: ydata/core/error/fabric_error.py
 Comment: 
 
-Filename: ydata_core-0.3.0.dist-info/METADATA
+Filename: ydata_core-0.4.0rc1.dist-info/METADATA
 Comment: 
 
-Filename: ydata_core-0.3.0.dist-info/WHEEL
+Filename: ydata_core-0.4.0rc1.dist-info/WHEEL
 Comment: 
 
-Filename: ydata_core-0.3.0.dist-info/top_level.txt
+Filename: ydata_core-0.4.0rc1.dist-info/top_level.txt
 Comment: 
 
-Filename: ydata_core-0.3.0.dist-info/RECORD
+Filename: ydata_core-0.4.0rc1.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## Comparing `ydata_core-0.3.0.dist-info/METADATA` & `ydata_core-0.4.0rc1.dist-info/METADATA`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: ydata-core
-Version: 0.3.0
+Version: 0.4.0rc1
 Summary: Core functionality for all python packages at YData
 Home-page: https://github.com/ydataai/python-core
 Author: YData
 Author-email: developers@ydata.ai
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python :: 3 :: Only
 Classifier: Topic :: Software Development :: Libraries :: Python Modules
```

## Comparing `ydata_core-0.3.0.dist-info/RECORD` & `ydata_core-0.4.0rc1.dist-info/RECORD`

 * *Files 21% similar despite different names*

```diff
@@ -1,9 +1,11 @@
 ydata/core/__init__.py,sha256=47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZG3hSuFU,0
+ydata/core/connectors/__init__.py,sha256=rsifccFDjMFl71_MOEzejh-4lOLbgHLdgtrHd8l6efw,59
+ydata/core/connectors/write_mode.py,sha256=uUZMVD6yx3GJLR7_dLJyIOHrVZO1WaSjpulZA23aN-M,134
 ydata/core/enum/__init__.py,sha256=R5LgZ-ZFiZJGW19f8ejDodDf6EZjSJ0a_LXxIyhkOdo,67
 ydata/core/enum/string_enum.py,sha256=l11UUEBKXvQYBdnuvExMHEU-PnIrIpAIoRNBb6rZpmo,664
 ydata/core/error/__init__.py,sha256=tA7nd8DVnbFyTexySXzNXDhmloFjPKzjJ_Wmz2IBl-Y,70
 ydata/core/error/fabric_error.py,sha256=AYHnwBa4FHhDgtNoFcn7NOoEDLymTZsHYnERaND8eRI,1744
-ydata_core-0.3.0.dist-info/METADATA,sha256=xNDl3-wB1bRdcYWDjM2dHfOWdVLYlH-KGFp8tOMhqsk,1479
-ydata_core-0.3.0.dist-info/WHEEL,sha256=a-zpFRIJzOq5QfuhBzbhiA1eHTzNCJn8OdRvhdNX0Rk,110
-ydata_core-0.3.0.dist-info/top_level.txt,sha256=s4ySCHuzMHwZ8NeXGj2CkDdJaGLv0YzfNsi3JW3V8gQ,6
-ydata_core-0.3.0.dist-info/RECORD,,
+ydata_core-0.4.0rc1.dist-info/METADATA,sha256=2kayZqjZEr51vUmdGMwNuS10gWau0m_3grzNJz45HBk,1482
+ydata_core-0.4.0rc1.dist-info/WHEEL,sha256=a-zpFRIJzOq5QfuhBzbhiA1eHTzNCJn8OdRvhdNX0Rk,110
+ydata_core-0.4.0rc1.dist-info/top_level.txt,sha256=s4ySCHuzMHwZ8NeXGj2CkDdJaGLv0YzfNsi3JW3V8gQ,6
+ydata_core-0.4.0rc1.dist-info/RECORD,,
```

