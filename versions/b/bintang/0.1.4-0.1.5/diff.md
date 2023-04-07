# Comparing `tmp/bintang-0.1.4-py3-none-any.whl.zip` & `tmp/bintang-0.1.5-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,16 +1,16 @@
-Zip file size: 20948 bytes, number of entries: 14
+Zip file size: 21210 bytes, number of entries: 14
 -rw-rw-rw-  2.0 fat       25 b- defN 22-Sep-15 02:00 bintang/__init__.py
 -rw-rw-rw-  2.0 fat     6439 b- defN 22-Jul-05 11:25 bintang/besqlite.py
 -rw-rw-rw-  2.0 fat     1319 b- defN 22-Dec-22 23:56 bintang/cell.py
 -rw-rw-rw-  2.0 fat      566 b- defN 23-Mar-29 02:17 bintang/column.py
--rw-rw-rw-  2.0 fat    23302 b- defN 23-Apr-03 09:05 bintang/core.py
+-rw-rw-rw-  2.0 fat    23341 b- defN 23-Apr-07 05:18 bintang/core.py
 -rw-rw-rw-  2.0 fat      186 b- defN 23-Feb-13 06:10 bintang/log.py
 -rw-rw-rw-  2.0 fat     1385 b- defN 22-Dec-21 22:40 bintang/row.py
--rw-rw-rw-  2.0 fat    44748 b- defN 23-Apr-06 03:53 bintang/table.py
+-rw-rw-rw-  2.0 fat    45915 b- defN 23-Apr-07 04:30 bintang/table.py
 -rw-rw-rw-  2.0 fat     4981 b- defN 23-Feb-20 03:30 bintang/travdict.py
--rw-rw-rw-  2.0 fat     1092 b- defN 23-Apr-06 04:02 bintang-0.1.4.dist-info/LICENSE
--rw-rw-rw-  2.0 fat      249 b- defN 23-Apr-06 04:02 bintang-0.1.4.dist-info/METADATA
--rw-rw-rw-  2.0 fat       92 b- defN 23-Apr-06 04:02 bintang-0.1.4.dist-info/WHEEL
--rw-rw-rw-  2.0 fat        8 b- defN 23-Apr-06 04:02 bintang-0.1.4.dist-info/top_level.txt
-?rw-rw-r--  2.0 fat     1043 b- defN 23-Apr-06 04:02 bintang-0.1.4.dist-info/RECORD
-14 files, 85435 bytes uncompressed, 19248 bytes compressed:  77.5%
+-rw-rw-rw-  2.0 fat     1092 b- defN 23-Apr-07 06:22 bintang-0.1.5.dist-info/LICENSE
+-rw-rw-rw-  2.0 fat      249 b- defN 23-Apr-07 06:22 bintang-0.1.5.dist-info/METADATA
+-rw-rw-rw-  2.0 fat       92 b- defN 23-Apr-07 06:22 bintang-0.1.5.dist-info/WHEEL
+-rw-rw-rw-  2.0 fat        8 b- defN 23-Apr-07 06:22 bintang-0.1.5.dist-info/top_level.txt
+?rw-rw-r--  2.0 fat     1043 b- defN 23-Apr-07 06:22 bintang-0.1.5.dist-info/RECORD
+14 files, 86641 bytes uncompressed, 19510 bytes compressed:  77.5%
```

## zipnote {}

```diff
@@ -21,23 +21,23 @@
 
 Filename: bintang/table.py
 Comment: 
 
 Filename: bintang/travdict.py
 Comment: 
 
-Filename: bintang-0.1.4.dist-info/LICENSE
+Filename: bintang-0.1.5.dist-info/LICENSE
 Comment: 
 
-Filename: bintang-0.1.4.dist-info/METADATA
+Filename: bintang-0.1.5.dist-info/METADATA
 Comment: 
 
-Filename: bintang-0.1.4.dist-info/WHEEL
+Filename: bintang-0.1.5.dist-info/WHEEL
 Comment: 
 
-Filename: bintang-0.1.4.dist-info/top_level.txt
+Filename: bintang-0.1.5.dist-info/top_level.txt
 Comment: 
 
-Filename: bintang-0.1.4.dist-info/RECORD
+Filename: bintang-0.1.5.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## bintang/core.py

```diff
@@ -1,13 +1,14 @@
 from openpyxl import load_workbook
 import pyodbc
 import os
 import json
 import copy
 from bintang.table import Table, Table_Path
+from bintang.table import _match_primitive, _match_caseless, _match_caseless_unicode
 from bintang import travdict
 from pathlib import Path
 from bintang.log import log
 from thefuzz import process as thefuzzprocess
 # import logging
 
 # log = logging.getLogger(__name__)
@@ -207,21 +208,21 @@
             # suggest = process.extract(tablename, tablenames, limit=2)
             # print('hello',suggest)
             # print('yes')
             # quit()
             raise ValueError('Tablename {} does not exist.'.format(tablename))
 
 
-    def iterrows(self, tablename, columns=None, result_as = 'dict', rowid=False):
+    def iterrows(self, tablename, columns=None, row_type = 'dict', rowid=False):
         """get the table form the collection
         then yield idx and row from table's iterrows()
         """
         
         self.raise_valueerror_tablename(tablename)
-        for idx, row in self.get_table(tablename).iterrows(columns, result_as=result_as, rowid=rowid):
+        for idx, row in self.get_table(tablename).iterrows(columns, row_type=row_type, rowid=rowid):
             yield idx, row
             
 
     def dev_read_db(self, connstr, tablename, columns = None):
         self.create_table(tablename)
         self[tablename].connstr = connstr
         import pyodbc
@@ -283,24 +284,22 @@
                         sql_ = "INSERT INTO {} (name) VALUES ('{}');".format(tablename.lower()+'_columns', col)
                         log.debug(sql_)
                         cursor.execute(sql_)
         cursor.close()
         conn.close() 
 
 
-    def read_excel(self, path, sheetname, name=None):
-        tablename = None
-        if name is None:
-            tablename = sheetname
-        else:
-            tablename = name
+    def read_excel(self, path, sheetname, table=None):
+        table_ = sheetname
+        if table is not None:
+            table_ = table
   
-        self.create_table(tablename)        
+        self.create_table(table_)        
         if self.__be is not None:
-            self.__be.create_table(tablename)
+            self.__be.create_table(table_)
         wb = load_workbook(path, read_only=True, data_only=True)
         ws = wb[sheetname]
         columns = []
         Nonecolumn_cnt = 0
         for rownum, row_cells in enumerate(ws.iter_rows(),start=1):
             values = [] # hold column value for each row
             if rownum == 1:
@@ -313,17 +312,17 @@
                         columns.append(cell.value)
                 if Nonecolumn_cnt > 0:
                     log.warning('Warning! Noname column detected!')          
             
             if rownum > 1:
                 for cell in row_cells:
                     values.append(cell.value)
-                self.get_table(tablename).insert(columns, values)
+                self.get_table(table_).insert(columns, values)
         if self.__be is not None:
-            self.get_table(tablename).add_row_into_be()
+            self.get_table(table_).add_row_into_be()
 
 
     def read_dict(self, dict_obj, tablepaths=[]):
         debug = False
         for tprow in travdict.traverse_dict(dict_obj, tablepaths):
             # if debug:
             #     print("\n---------------------in bintang---------------------")
@@ -498,30 +497,29 @@
         numof_keys = len(on) #(lkeys)
         # loop left table
         for lidx, lrow in self.iterrows(ltable, columns=lkeys, rowid=rowid):
             # loop right table
             for ridx, rrow in self.iterrows(rtable, columns=rkeys, rowid=rowid):
                 matches = 0 # store matches for each rrow
                 # compare value for any matching keys, if TRUE then increment matches
-                for i in range(numof_keys):
-                    #if lrow[on[0]] == rrow[on[1]]:
-                    if lrow[lkeys[i]] == rrow[rkeys[i]]:
+                for i in range(numof_keys): 
+                    if _match_caseless_unicode(lrow[lkeys[i]], rrow[rkeys[i]]):
                         matches += 1 # incremented!
                 if matches == numof_keys: # if fully matched, create the row & add into the output table
                     #debug merged.insert(["lrowid","rrowid"], [lrow["_rowid"], rrow["_rowid"]])
                     #and add the row to output table
                     outrow = out_tobj.make_row()
                     # add cells from left table
                     outrow = self._add_lcell(lidx, ltable, outrow, out_table, out_lcolumns, rowid)
                     # add cells from right table
                     outrow = self._add_rcell(ridx, rtable, outrow, out_table, out_rcolumns, rcol_resolved, rowid)   
                     out_tobj.add_row(outrow)
         #debug merged.print() 
         return out_tobj
-
+                
 
     def leftjoin(self,ltable, rtable, lkeys, rkeys
                 ,out_lcolumns=None
                 ,out_rcolumns=None
                 ,rowid=False):
 
         # validate input eg. column etc
@@ -546,15 +544,15 @@
             outrow = out_tobj.make_row()
             # add cells for ltable
             outrow = self._add_lcell(lidx, ltable, outrow, out_table, out_lcolumns, rowid)
             for ridx, rrow in self.iterrows(rtable, columns=rkeys, rowid=rowid):
                 matches = 0 # store matches for each rrow
                 # evaluate any matching keys, if so increment matches
                 for i in range(numof_keys):
-                    if lrow[lkeys[i]] == rrow[rkeys[i]]:
+                    if _match_caseless_unicode(lrow[lkeys[i]] == rrow[rkeys[i]]):
                         matches += 1 # increment
                 if matches == numof_keys: # if fully matched, create the row & add into the output table
                     #debug merged.insert(["lrowid","rrowid"], [lrow["_rowid"], rrow["_rowid"]])
                     # add cells for rtable
                     outrow = self._add_rcell(ridx, rtable, outrow, out_table, out_rcolumns, ltable, rowid)   
             out_tobj.add_row(outrow)             
         #debug merged.print()
```

## bintang/table.py

```diff
@@ -2,14 +2,15 @@
 from bintang.cell import Cell
 from bintang.row import Row
 import json
 import sqlite3
 import uuid
 import re
 import types
+import unicodedata
 from bintang.log import log
 # import logging
 
 # log = logging.getLogger(__name__)
 # FORMAT = "[%(filename)s:%(lineno)s - %(funcName)10s() ] %(message)s"
 # logging.basicConfig(format=FORMAT)
 # log.setLevel(logging.DEBUG)
@@ -80,15 +81,15 @@
         sql_cols_withtype = self.set_sql_datatype(dest_columns, conn, schemaname, table)
         sql_cols_withliteral = self.set_sql_literal(sql_cols_withtype, conn)
         
         # start insert to sql
         cursor = conn.cursor()
         temp_rows = []  
         total_rowcount = 0 # to hold total record affected
-        for idx, values in self.iterrows(src_cols, result_as='list'):
+        for idx, values in self.iterrows(src_cols, row_type='list'):
             ## question: can values and d_cols_withliteral align???????
             sql_record = self.gen_sql_literal_record(values, sql_cols_withliteral)
             temp_rows.append(sql_record)
             if len(temp_rows) == max_rows:
                 stmt = str_stmt + ' {}'.format(",".join(temp_rows))
                 #log.debug(stmt)
                 cursor.execute(stmt)
@@ -171,15 +172,15 @@
         # create as prepared statement
         sql_template = 'INSERT INTO {}.{} ({}) VALUES {}'
         param_markers = self.gen_row_param_markers(numof_col, mrpb)
         prep_stmt = sql_template.format(schemaname,table,",".join(['"{}"'.format(x) for x in dest_columns]),param_markers)
         cursor = conn.cursor()
         temp_rows = []
         total_rowcount = 0
-        for idx, row in self.iterrows(src_cols, result_as='list'):
+        for idx, row in self.iterrows(src_cols, row_type='list'):
             for v in row:
                 temp_rows.append(v)
             if len(temp_rows) == (mrpb * numof_col):
                 try:
                     cursor.execute(prep_stmt, temp_rows)
                     total_rowcount += cursor.rowcount
                 except Exception as e:
@@ -673,25 +674,25 @@
 
 
     def _gen_row_aslist(self, row, columnids):
         #columnids = self.get_columnids(columns)
         return row.get_values(columnids)
 
        
-    def iterrows(self, columns=None, result_as='dict', rowid=False):
+    def iterrows(self, columns=None, row_type='dict', rowid=False):
         if columns is None:
                 columns = self.get_columns() # assign all available column names
-        if result_as == 'dict': 
+        if row_type == 'dict': 
             if self.__be is None:
                 for idx, row in self.__rows.items():
                     yield idx, self._gen_row_asdict(row,columns,rowid)
             if self.__be is not None:
                 for idx, row in self.__be.iterrows_asdict(self.name, columns):
                     yield idx, row
-        elif result_as == 'list':
+        elif row_type == 'list':
             columnids = self.get_columnids(columns)
             for idx, row in self.__rows.items():
                 yield idx, self._gen_row_aslist(row,columnids)
 
 
     def set_data_props(self):
         """ scan table to obtain columns properties - data type, column size (if str type then the max of len of string)"""
@@ -745,15 +746,15 @@
         # get and print out rowresult_as
         for row in rows_values:
             print(row)
 
 
     def print_aslist(self, top=None, columns=None):
         print("idx",self.get_columns(columns))
-        for idx, row in self.iterrows(result_as='list',columns=columns):
+        for idx, row in self.iterrows(row_type='list',columns=columns):
             print(idx, row)
 
 
     def print_asdict(self, top=None, columns=None):
         for idx, row in self.iterrows(columns=columns):
             print(idx, row)
 
@@ -1000,15 +1001,16 @@
                 item_ = tuple([valid_column,item[1]])
                 valid_out_rcolumns.append(item_)
         numof_keys = len(on)
         for lidx, lrow in self.iterrows(lkeys, rowid=True):
             for ridx, rrow in rtable.iterrows():
                 matches = 0
                 for i in range(numof_keys):
-                    if lrow[lkeys[i]] == rrow[rkeys[i]]:
+                    # if lrow[lkeys[i]] == rrow[rkeys[i]]:
+                    if _match_caseless_unicode(lrow[lkeys[i]], rrow[rkeys[i]]):
                         matches += 1 # increment
                 if matches == numof_keys:
                     # update this table lrow for each out_rcolumns
                     for item in valid_out_rcolumns:
                         if isinstance(item, str): # if item is a column
                             value = rtable[ridx][item]
                             if item in lcolumn_prematch:
@@ -1016,43 +1018,43 @@
                                 self.update_row(lidx, rtable.name + '_' + item, value)
                             else:
                                 self.update_row(lidx, item, value)
                         if isinstance(item, tuple): # if a tuple
                             value = rtable[ridx][item[0]]
                             self.update_row(lidx, item[1], value)
 
-    def groupbycount(self, columnname):
+    def groupbycount(self, column):
         res_dict = {}
-        for idx, row in self.iterrows(columnname):
+        for idx, row in self.iterrows(column):
             value = next(iter(row.values()))
             if value not in res_dict:
                 res_dict[value] = 1
             else:
                 res_dict[value] += 1
         return res_dict
     
     
     
     def groupby2count(self, columns):
         res_dict = {} #key=a tuple of columns, value=count
-        for idx, row in self.iterrows(columns, result_as='list'):
+        for idx, row in self.iterrows(columns, row_type='list'):
             # DEPRECATED - No need tobe a string trow = tuple([str(x or 'None') for x in row])
             trow = tuple(row)
             keys = res_dict.keys()
             if trow not in res_dict.keys():
                 res_dict[trow] = 1
             else:
                 res_dict[trow] += 1       
         return res_dict
     
     
     def DEV_groupby3count(self, columns):
         group_tobj = Table('test')
         res_dict = {} #key=a tuple of columns, value=count
-        for idx, row in self.iterrows(columns, result_as='list'):
+        for idx, row in self.iterrows(columns, row_type='list'):
             trow = tuple(row)
             if trow not in res_dict.keys():
                 res_dict[trow] = 1
             else:
                 res_dict[trow] += 1
                 
         for k, v in res_dict.items():
@@ -1061,15 +1063,15 @@
             group_tobj.insert(columns_, values)       
         return group_tobj
     
 
     def DEV_groupby_count(self, columns, count_column):
         group_tobj = Table('test')
         res_dict = {} #key=a tuple of columns, value=count
-        for idx, row in self.iterrows(columns, result_as='list'):
+        for idx, row in self.iterrows(columns, row_type='list'):
             trow = tuple(row)
             if trow not in res_dict.keys():
                 res_dict[trow] = 1
             else:
                 res_dict[trow] += 1
                 
         for k, v in res_dict.items():
@@ -1091,19 +1093,19 @@
             if index == True:
                 columns.insert(0,'_idx')
             if index != True:
                 columns.insert(0,str(index))        
         ws.append(columns)
         # add row
         if index:
-            for idx, row in self.iterrows(result_as='list'):
+            for idx, row in self.iterrows(row_type='list'):
                 row.insert(0,idx)
                 ws.append(row)
         if not index:
-            for idx, row in self.iterrows(result_as='list'):
+            for idx, row in self.iterrows(row_type='list'):
                 ws.append(row)          
         wb.save(path)
 
     def to_list(self, column):
         if isinstance(column, str):
             res_list = []
             for idx, row in self.iterrows([column]):
@@ -1138,14 +1140,45 @@
         for node in self.path.split("/"):
             if node == '': # if the 1st one. 1st node have discarded by split
                 path_as_list.append('/')
             else:
                 path_as_list.append(node)
         return path_as_list        
 
+def _match_primitive(value1, value2):
+    "Ascii case sensitive matching"
+    if value1 == value2:
+        return True
+    
+def _match_caseless(value1, value2):
+    "Ascii ase insensitive matching"
+    if isinstance(value1, str) and isinstance(value2, str):
+        if value1.lower() == value2.lower():
+            return True
+    elif isinstance(value1, str) or isinstance(value2, str):
+        if str(value1) == str(value2):
+            return True    
+    else:
+        if value1 == value2:
+            return True    
+        
+def _match_caseless_unicode(value1, value2):
+    "Unicode case insensetive matching"
+    if isinstance(value1, str) and isinstance(value2, str):
+        if _normalize_caseless(value1) == _normalize_caseless(value2):
+            return True
+    elif isinstance(value1, str) or isinstance(value2, str):
+        if str(value1) == str(value2):
+            return True
+    else:
+        if value1 == value2:
+            return True
+
+def _normalize_caseless(string):
+    return unicodedata.normalize("NFKD", string.casefold())
 
 type_map = {
     'sqlserver': {
                 'str':'nvarchar'
                 ,'int':'int'
                 ,'datetime':'datetime'
                 ,'float':'float'
```

## Comparing `bintang-0.1.4.dist-info/LICENSE` & `bintang-0.1.5.dist-info/LICENSE`

 * *Files identical despite different names*

