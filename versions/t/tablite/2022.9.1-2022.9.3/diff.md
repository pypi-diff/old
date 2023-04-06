# Comparing `tmp/tablite-2022.9.1-py3-none-any.whl.zip` & `tmp/tablite-2022.9.3-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,20 +1,20 @@
-Zip file size: 58880 bytes, number of entries: 18
+Zip file size: 58991 bytes, number of entries: 18
 -rw-rw-rw-  2.0 fat      181 b- defN 22-Jul-08 17:21 tablite/__init__.py
 -rw-rw-rw-  2.0 fat      800 b- defN 22-Jul-26 10:22 tablite/config.py
--rw-rw-rw-  2.0 fat   109776 b- defN 22-Aug-18 12:03 tablite/core.py
+-rw-rw-rw-  2.0 fat   109851 b- defN 22-Aug-19 10:04 tablite/core.py
 -rw-rw-rw-  2.0 fat    26932 b- defN 22-Aug-18 11:40 tablite/datatypes.py
--rw-rw-rw-  2.0 fat     7862 b- defN 22-Jul-26 16:26 tablite/file_reader_utils.py
+-rw-rw-rw-  2.0 fat     8113 b- defN 22-Aug-19 10:04 tablite/file_reader_utils.py
 -rw-rw-rw-  2.0 fat     4944 b- defN 22-Jul-08 17:21 tablite/groupby_utils.py
 -rw-rw-rw-  2.0 fat    50898 b- defN 22-Aug-16 11:28 tablite/memory_manager.py
 -rw-rw-rw-  2.0 fat     6057 b- defN 22-Jul-08 17:21 tablite/sortation.py
 -rw-rw-rw-  2.0 fat     8035 b- defN 22-Jul-08 17:21 tablite/utils.py
--rw-rw-rw-  2.0 fat      134 b- defN 22-Aug-18 12:04 tablite/version.py
--rw-rw-rw-  2.0 fat     1069 b- defN 22-Jul-08 17:21 tablite-2022.9.1.data/data/LICENSE
--rw-rw-rw-  2.0 fat     6073 b- defN 22-Aug-09 21:37 tablite-2022.9.1.data/data/README.md
--rw-rw-rw-  2.0 fat      203 b- defN 22-Aug-06 15:08 tablite-2022.9.1.data/data/requirements.txt
--rw-rw-rw-  2.0 fat     1069 b- defN 22-Aug-18 12:06 tablite-2022.9.1.dist-info/LICENSE
--rw-rw-rw-  2.0 fat     7591 b- defN 22-Aug-18 12:06 tablite-2022.9.1.dist-info/METADATA
--rw-rw-rw-  2.0 fat       92 b- defN 22-Aug-18 12:06 tablite-2022.9.1.dist-info/WHEEL
--rw-rw-rw-  2.0 fat        8 b- defN 22-Aug-18 12:06 tablite-2022.9.1.dist-info/top_level.txt
-?rw-rw-r--  2.0 fat     1456 b- defN 22-Aug-18 12:06 tablite-2022.9.1.dist-info/RECORD
-18 files, 233180 bytes uncompressed, 56512 bytes compressed:  75.8%
+-rw-rw-rw-  2.0 fat      134 b- defN 22-Aug-19 10:04 tablite/version.py
+-rw-rw-rw-  2.0 fat     1069 b- defN 22-Jul-08 17:21 tablite-2022.9.3.data/data/LICENSE
+-rw-rw-rw-  2.0 fat     6073 b- defN 22-Aug-09 21:37 tablite-2022.9.3.data/data/README.md
+-rw-rw-rw-  2.0 fat      203 b- defN 22-Aug-06 15:08 tablite-2022.9.3.data/data/requirements.txt
+-rw-rw-rw-  2.0 fat     1069 b- defN 22-Aug-19 10:14 tablite-2022.9.3.dist-info/LICENSE
+-rw-rw-rw-  2.0 fat     7591 b- defN 22-Aug-19 10:14 tablite-2022.9.3.dist-info/METADATA
+-rw-rw-rw-  2.0 fat       92 b- defN 22-Aug-19 10:14 tablite-2022.9.3.dist-info/WHEEL
+-rw-rw-rw-  2.0 fat        8 b- defN 22-Aug-19 10:14 tablite-2022.9.3.dist-info/top_level.txt
+?rw-rw-r--  2.0 fat     1456 b- defN 22-Aug-19 10:14 tablite-2022.9.3.dist-info/RECORD
+18 files, 233506 bytes uncompressed, 56623 bytes compressed:  75.8%
```

## zipnote {}

```diff
@@ -24,32 +24,32 @@
 
 Filename: tablite/utils.py
 Comment: 
 
 Filename: tablite/version.py
 Comment: 
 
-Filename: tablite-2022.9.1.data/data/LICENSE
+Filename: tablite-2022.9.3.data/data/LICENSE
 Comment: 
 
-Filename: tablite-2022.9.1.data/data/README.md
+Filename: tablite-2022.9.3.data/data/README.md
 Comment: 
 
-Filename: tablite-2022.9.1.data/data/requirements.txt
+Filename: tablite-2022.9.3.data/data/requirements.txt
 Comment: 
 
-Filename: tablite-2022.9.1.dist-info/LICENSE
+Filename: tablite-2022.9.3.dist-info/LICENSE
 Comment: 
 
-Filename: tablite-2022.9.1.dist-info/METADATA
+Filename: tablite-2022.9.3.dist-info/METADATA
 Comment: 
 
-Filename: tablite-2022.9.1.dist-info/WHEEL
+Filename: tablite-2022.9.3.dist-info/WHEEL
 Comment: 
 
-Filename: tablite-2022.9.1.dist-info/top_level.txt
+Filename: tablite-2022.9.3.dist-info/top_level.txt
 Comment: 
 
-Filename: tablite-2022.9.1.dist-info/RECORD
+Filename: tablite-2022.9.3.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## tablite/core.py

```diff
@@ -816,14 +816,18 @@
             additional_configs["tqdm"] = tqdm if tqdm is not None else iter
 
         if not isinstance(strip_leading_and_tailing_whitespace, bool):
             raise TypeError()
         
         if columns is None:
             sample = get_headers(path)
+            
+            if "is_empty" in sample:
+                return Table()
+
             if import_as in {'csv', 'txt'}:
                 columns = {k:'f' for k in sample[path.name][0]}
             elif sheet is not None:
                 columns = sample[sheet][0]
             else:
                 pass  # let it fail later.
         if not first_row_has_headers:
@@ -2646,15 +2650,15 @@
         ".csv": ',',
         ".tsv": '\t',
         ".txt": '|'
     }
     delimiter = delimiters.get(path.suffix)
 
     with path.open('w', encoding='utf-8') as fo:
-        fo.write(delimiter.join(f'"{c}"' for c in table.columns)+'\n')
+        fo.write(delimiter.join(c for c in table.columns)+'\n')
         for row in _tqdm(table.rows, total=len(table)):
             fo.write(delimiter.join(txt(c) for c in row)+'\n')
 
 def sql_writer(table, path):
     _check_input(table,path)
     with path.open('w', encoding='utf-8') as fo:
         fo.write(table.to_sql())
```

## tablite/file_reader_utils.py

```diff
@@ -150,14 +150,15 @@
     # determined by the first line, which almost always is a line of headers,
     # the text characters will be utf-8,16 or ascii letters plus white space.
     # This leaves the characters ,;:| and \t as potential separators, with one
     # exception: files that use whitespace as separator. My logic is therefore
     # to (1) find the set of characters that intersect with ',;:|\t' which in
     # practice is a single character, unless (2) it is empty whereby it must
     # be whitespace.
+    if len(text) == 0: return None
     seps = {',', '\t', ';', ':', '|'}.intersection(text)
     if not seps:
         if " " in text:
             return " "
         else:
             raise ValueError("separator not detected")
     if len(seps) == 1:
@@ -220,12 +221,17 @@
             lines = []
             for n, line in enumerate(fi):
                 line = line.rstrip('\n')
                 lines.append(line)
                 if n > linecount:
                     break  # break on first
             d['delimiter'] = delimiter = detect_seperator('\n'.join(lines))
+
+            if delimiter is None:
+                d['delimiter'] = delimiters[path.suffix] # pickup the default one
+                d['is_empty'] = True # mark as empty to return an empty table instead of throwing
+
             d[path.name] = [line.split(delimiter) for line in lines]
         return d
     except Exception:
         raise ValueError(f"can't read {path.suffix}")
```

## tablite/version.py

```diff
@@ -1,3 +1,3 @@
-major, minor, patch = 2022, 9, 1
+major, minor, patch = 2022, 9, 3
 __version_info__ = (major, minor, patch)
 __version__ = '.'.join(str(i) for i in __version_info__)
```

## Comparing `tablite-2022.9.1.data/data/LICENSE` & `tablite-2022.9.3.data/data/LICENSE`

 * *Files identical despite different names*

## Comparing `tablite-2022.9.1.data/data/README.md` & `tablite-2022.9.3.data/data/README.md`

 * *Files identical despite different names*

## Comparing `tablite-2022.9.1.dist-info/LICENSE` & `tablite-2022.9.3.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `tablite-2022.9.1.dist-info/METADATA` & `tablite-2022.9.3.dist-info/METADATA`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: tablite
-Version: 2022.9.1
+Version: 2022.9.3
 Summary: multiprocessing enabled out-of-memory data analysis library for tabular data.
 Home-page: https://github.com/root-11/tablite
 Author: https://github.com/root-11
 License: MIT
 Keywords: all,any,average,column,columns,count,csv,excel,filter,first,from,groupby,in-memory,index,indexing,inner join,is sorted,json,last,left join,list on disk,log,max,median,min,mode,ods,out-of-memory,outer join,pivot,pivot table,product,rows,show,sort,standard deviation,stored list,sum,table,tables,tablite,to,txt,unique,use disk,xlsx,zip
 Platform: any
 Classifier: Development Status :: 5 - Production/Stable
```

## Comparing `tablite-2022.9.1.dist-info/RECORD` & `tablite-2022.9.3.dist-info/RECORD`

 * *Files 9% similar despite different names*

```diff
@@ -1,18 +1,18 @@
 tablite/__init__.py,sha256=iSmLQ-5qetDrOlJkqm6Pm6QYGDgJLPLbGIpCquYVvL0,181
 tablite/config.py,sha256=UczTGYUyLabOpi3-lBNBEGtVg5RJHyqaQ6ndivznHc8,800
-tablite/core.py,sha256=mFv-2ZdMB8lg479YbDpG-3yrM0KuouER68hyolXCgWo,109776
+tablite/core.py,sha256=DPGV9mJRwnoLVFGcku-OP7H_5vfE--wQD1Rwmo5heIU,109851
 tablite/datatypes.py,sha256=m5jGbWEvP5dFFbi5ZWj3YVW6wlZLEdcBM9dTAe_qS8I,26932
-tablite/file_reader_utils.py,sha256=SqOm6A6Z2tSeGaiQelceojOxfwhttkpmEDuVQXMI9eY,7862
+tablite/file_reader_utils.py,sha256=yELdb08iVwnjHWUXqLWPgSCKdLAuTSj0LtpVGp0yMZc,8113
 tablite/groupby_utils.py,sha256=BSQy1cAiKc3eyZcbRlJTxzyAGRRBUT-kW7itGjnVfIA,4944
 tablite/memory_manager.py,sha256=_FxnFhdLOYUGHiC3RH1EL7UvD8JbYwpNGNjDZboPGkg,50898
 tablite/sortation.py,sha256=Jxp4T6Dbc-G5mUBq3c42ILku2lvtrvVGUvgDypKgu5s,6057
 tablite/utils.py,sha256=AokT2dfBuYfTABiecXj-XxW3EODnI9eK1J34HkUH_ZU,8035
-tablite/version.py,sha256=76MiEWoSI-vX3nPm56aMPiz8BlFLzHdHtTSZBZs-8O8,134
-tablite-2022.9.1.data/data/LICENSE,sha256=DzHDlst_HKcG2siTMmSx3QBYn1DfYj8Thz7d189Hd_M,1069
-tablite-2022.9.1.data/data/README.md,sha256=BHHmI-qHyrjd-CVbl4CuiJyoyUMgpLC-k1t4bG7qRGA,6073
-tablite-2022.9.1.data/data/requirements.txt,sha256=Rn6f8WDDJwXlvXphtbmDdIsF3O7hPjbXewLIqdG__lo,203
-tablite-2022.9.1.dist-info/LICENSE,sha256=DzHDlst_HKcG2siTMmSx3QBYn1DfYj8Thz7d189Hd_M,1069
-tablite-2022.9.1.dist-info/METADATA,sha256=PafKH-dYObJ_6S-J3PKr6pIjUenD0C31yGfBGW6uBDw,7591
-tablite-2022.9.1.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
-tablite-2022.9.1.dist-info/top_level.txt,sha256=wLPhlgUC10JlueE5ZhtCVSrs2VnvMQgNlhdCNsxPXPg,8
-tablite-2022.9.1.dist-info/RECORD,,
+tablite/version.py,sha256=xrDhNA1J-lheilHeW0dNnvFhSVYpLsRCwrB16MqUFqM,134
+tablite-2022.9.3.data/data/LICENSE,sha256=DzHDlst_HKcG2siTMmSx3QBYn1DfYj8Thz7d189Hd_M,1069
+tablite-2022.9.3.data/data/README.md,sha256=BHHmI-qHyrjd-CVbl4CuiJyoyUMgpLC-k1t4bG7qRGA,6073
+tablite-2022.9.3.data/data/requirements.txt,sha256=Rn6f8WDDJwXlvXphtbmDdIsF3O7hPjbXewLIqdG__lo,203
+tablite-2022.9.3.dist-info/LICENSE,sha256=DzHDlst_HKcG2siTMmSx3QBYn1DfYj8Thz7d189Hd_M,1069
+tablite-2022.9.3.dist-info/METADATA,sha256=lWL0HoEa2OSD8KyF-KrHTjS2jnkf5RrFFS43hiKs0I4,7591
+tablite-2022.9.3.dist-info/WHEEL,sha256=G16H4A3IeoQmnOrYV4ueZGKSjhipXx8zc8nu9FGlvMA,92
+tablite-2022.9.3.dist-info/top_level.txt,sha256=wLPhlgUC10JlueE5ZhtCVSrs2VnvMQgNlhdCNsxPXPg,8
+tablite-2022.9.3.dist-info/RECORD,,
```

