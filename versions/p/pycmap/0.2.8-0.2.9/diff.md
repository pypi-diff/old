# Comparing `tmp/pycmap-0.2.8-py3-none-any.whl.zip` & `tmp/pycmap-0.2.9-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,27 +1,27 @@
-Zip file size: 45933 bytes, number of entries: 25
--rw-r--r--  2.0 unx      400 b- defN 21-Dec-07 18:18 pycmap/__init__.py
+Zip file size: 46045 bytes, number of entries: 25
+-rw-r--r--  2.0 unx      400 b- defN 21-Dec-07 19:15 pycmap/__init__.py
 -rw-r--r--  2.0 unx     2267 b- defN 19-Jul-22 20:52 pycmap/annotatedHeatmap.py
 -rw-r--r--  2.0 unx    10635 b- defN 19-Sep-02 18:45 pycmap/baseGraph.py
 -rw-r--r--  2.0 unx     2269 b- defN 19-Aug-12 00:45 pycmap/clean.py
 -rw-r--r--  2.0 unx      373 b- defN 19-Jun-24 23:15 pycmap/cmap.py
 -rw-r--r--  2.0 unx     3285 b- defN 20-Mar-30 19:38 pycmap/colorMaps.py
 -rw-r--r--  2.0 unx     6980 b- defN 21-Nov-25 05:14 pycmap/common.py
 -rw-r--r--  2.0 unx      162 b- defN 19-Sep-19 05:34 pycmap/deepC.py
 -rw-r--r--  2.0 unx     2491 b- defN 19-Jun-30 00:33 pycmap/export.py
 -rw-r--r--  2.0 unx     5858 b- defN 20-Sep-04 16:50 pycmap/foliumHeat.py
 -rw-r--r--  2.0 unx     6161 b- defN 19-Sep-07 18:29 pycmap/hist.py
 -rw-r--r--  2.0 unx    11764 b- defN 19-Oct-30 18:47 pycmap/map.py
 -rw-r--r--  2.0 unx    14443 b- defN 20-May-22 02:48 pycmap/match.py
 -rw-r--r--  2.0 unx    26314 b- defN 21-Nov-24 18:13 pycmap/rest.py
--rw-r--r--  2.0 unx     7097 b- defN 21-Dec-07 18:18 pycmap/sample.py
+-rw-r--r--  2.0 unx     7427 b- defN 21-Dec-07 19:15 pycmap/sample.py
 -rw-r--r--  2.0 unx    13125 b- defN 19-Oct-30 18:46 pycmap/section.py
 -rw-r--r--  2.0 unx    16494 b- defN 19-Aug-06 20:30 pycmap/supervised.py
 -rw-r--r--  2.0 unx     8332 b- defN 19-Sep-03 00:39 pycmap/trend.py
 -rw-r--r--  2.0 unx    17434 b- defN 20-Sep-04 16:51 pycmap/viz.py
 -rw-r--r--  2.0 unx     3918 b- defN 19-Jun-24 02:24 pycmap/w3.py
--rw-r--r--  2.0 unx     1089 b- defN 21-Dec-07 18:18 pycmap-0.2.8.dist-info/LICENSE
--rw-r--r--  2.0 unx     7287 b- defN 21-Dec-07 18:18 pycmap-0.2.8.dist-info/METADATA
--rw-r--r--  2.0 unx       92 b- defN 21-Dec-07 18:18 pycmap-0.2.8.dist-info/WHEEL
--rw-r--r--  2.0 unx        7 b- defN 21-Dec-07 18:18 pycmap-0.2.8.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx     1851 b- defN 21-Dec-07 18:18 pycmap-0.2.8.dist-info/RECORD
-25 files, 170128 bytes uncompressed, 43049 bytes compressed:  74.7%
+-rw-r--r--  2.0 unx     1089 b- defN 21-Dec-07 19:20 pycmap-0.2.9.dist-info/LICENSE
+-rw-r--r--  2.0 unx     7287 b- defN 21-Dec-07 19:20 pycmap-0.2.9.dist-info/METADATA
+-rw-r--r--  2.0 unx       92 b- defN 21-Dec-07 19:20 pycmap-0.2.9.dist-info/WHEEL
+-rw-r--r--  2.0 unx        7 b- defN 21-Dec-07 19:20 pycmap-0.2.9.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx     1851 b- defN 21-Dec-07 19:20 pycmap-0.2.9.dist-info/RECORD
+25 files, 170458 bytes uncompressed, 43161 bytes compressed:  74.7%
```

## zipnote {}

```diff
@@ -54,23 +54,23 @@
 
 Filename: pycmap/viz.py
 Comment: 
 
 Filename: pycmap/w3.py
 Comment: 
 
-Filename: pycmap-0.2.8.dist-info/LICENSE
+Filename: pycmap-0.2.9.dist-info/LICENSE
 Comment: 
 
-Filename: pycmap-0.2.8.dist-info/METADATA
+Filename: pycmap-0.2.9.dist-info/METADATA
 Comment: 
 
-Filename: pycmap-0.2.8.dist-info/WHEEL
+Filename: pycmap-0.2.9.dist-info/WHEEL
 Comment: 
 
-Filename: pycmap-0.2.8.dist-info/top_level.txt
+Filename: pycmap-0.2.9.dist-info/top_level.txt
 Comment: 
 
-Filename: pycmap-0.2.8.dist-info/RECORD
+Filename: pycmap-0.2.9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## pycmap/__init__.py

```diff
@@ -11,10 +11,10 @@
 if sys.version_info < (3, 0):
     warnings.warn(
         ('Python 2 is not supported anymore. '
          'Please transition to Python 3 to be able to receive updates and fixes.'),
         UserWarning
     )
 
-__version__ = '0.2.8'
+__version__ = '0.2.9'
 # __all__ = []
```

## pycmap/sample.py

```diff
@@ -11,21 +11,25 @@
 import datetime
 import concurrent.futures
 import pandas as pd
 from dateutil.parser import parse
 
 
 
+def alias(varName, tableName):
+    """Return an alias for a variable name."""
+    return f"__CMAP__{varName}__{tableName}"
+
 
 def add_target_columns(df, targets):
     """
     Adds new columns (empty) to the dataframe form each target variable.
     """
     for env in targets.values():
-        for v in env.get("variables"):
+        for v in env.get("aliases"):
             if v not in df.columns: df[v] = None
     return df
     
 
 def add_target_meta(api, targets):
     """
     Adds new entries (metadata) to the `targets` dictionary including the 
@@ -35,14 +39,17 @@
     for table, env in targets.items():
         df = api.query(f"SELECT MIN([time]) startTime, MAX([time]) endTime FROM {table}")
         if len(df) > 0:
             targets[table]["startTime"] = df.loc[0, "startTime"]
             targets[table]["endTime"] = df.loc[0, "endTime"]
         targets[table]["hasDepth"] = api.has_field(table, "depth")
         targets[table]["isClimatology"] = api.is_climatology(table)
+        targets[table]["aliases"] = []
+        for varName in targets[table]["variables"]:
+            targets[table]["aliases"].append(alias(varName, table))
     return targets
 
 
 def match(df, api, targets, rowIndex, totalRows):
     """
     Takes a single-row of the source dataframe and colocalizes with the 
     target variables specified by `targets`. The tolerance parametrs 
@@ -64,26 +71,27 @@
         return not (
                     parse(sourceDT) < parse(targetMinDT) or 
                     parse(sourceDT) > parse(targetMaxDT)
                     )
 
     def construc_query(table, env, t, lat, lon, depth):
         variables = env["variables"] 
+        aliases = env["aliases"] 
         timeTolerance = env["tolerances"][0] 
         latTolerance = env["tolerances"][1] 
         lonTolerance = env["tolerances"][2]  
         depthTolerance = env["tolerances"][3]  
         hasDepth = env["hasDepth"] 
         isClimatology = env["isClimatology"]
         inTimeRange = True
         if not isClimatology:
             startTime = env["startTime"]
             endTime = env["endTime"]    
             inTimeRange = in_time_window(t, startTime, endTime)
-        selectClause = "SELECT " + ", ".join([f"AVG({v}) {v}" for v in variables]) + " FROM " + table
+        selectClause = "SELECT " + ", ".join([f"AVG({v}) {a}" for v, a in zip(variables, aliases)]) + " FROM " + table
         timeClause = f" WHERE [time] BETWEEN '{shift_dt(t, -timeTolerance)}' AND '{shift_dt(t, timeTolerance)}' "
         if not inTimeRange or isClimatology: timeClause = f" WHERE [month]={get_month(t)} "
         latClause = f" AND lat BETWEEN {lat-latTolerance} AND {lat+latTolerance} "
         lonClause = f" AND lon BETWEEN {lon-lonTolerance} AND {lon+lonTolerance} "
         depthClause = f" AND depth BETWEEN {depth-depthTolerance} AND {depth+depthTolerance} "
         if not hasDepth: depthClause = ""                
         return selectClause + timeClause + latClause + lonClause + depthClause        
@@ -102,15 +110,15 @@
         print(f"{rowIndex} / {totalRows} ... sampling {table}", end="\r")
         # do the colocalization: if either the target dataset has depth field (it's not sattelite, for example) or 
         # the depth of source measurement is less than `MAX_SURFACE_DEPTH`
         if env["hasDepth"] or depth <= MAX_SURFACE_DEPTH:       
             query = construc_query(table, env, t, lat, lon, depth)
             matchedEnv = api.query(query, servers=["rossby"])
             if len(matchedEnv)>0:
-                for v in env["variables"]: df.at[0, v] = matchedEnv.iloc[0][v] 
+                for v in env["aliases"]: df.at[0, v] = matchedEnv.iloc[0][v] 
     return df
 
 
 def Sample(source, targets):
     """
     placeholder for the `Sample` class.
```

## Comparing `pycmap-0.2.8.dist-info/LICENSE` & `pycmap-0.2.9.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `pycmap-0.2.8.dist-info/METADATA` & `pycmap-0.2.9.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pycmap
-Version: 0.2.8
+Version: 0.2.9
 Summary: Simons CMAP API python client
 Home-page: https://github.com/simonscmap/pycmap
 Author: Mohammad D. Ashkezari
 Author-email: mdehghan@uw.edu
 License: UNKNOWN
 Keywords: ocean oceanography data visualization satellite model in-situ remote sensing machine learning
 Platform: UNKNOWN
```

## Comparing `pycmap-0.2.8.dist-info/RECORD` & `pycmap-0.2.9.dist-info/RECORD`

 * *Files 8% similar despite different names*

```diff
@@ -1,25 +1,25 @@
-pycmap/__init__.py,sha256=B91qDLRx6LksVnQ3xnOOOAYv9hZv3KzyXcYmt1qkJzk,400
+pycmap/__init__.py,sha256=_bZwn08W7hopBkGIuLGeYFHkl0smwe0cSOIfH5P10cY,400
 pycmap/annotatedHeatmap.py,sha256=GrxKY-LtJinKRkpVWHR0AZCmlnr9INFqc8QS6YwIsIk,2267
 pycmap/baseGraph.py,sha256=gQ3USZmeOIB-e7iS9vSjWb-wTfpToxKK8puh04maMDo,10635
 pycmap/clean.py,sha256=Ok2aNF2lnvbf1ygKu1t7p8ZYAvZtuRL1GDQ6DiDXYKE,2269
 pycmap/cmap.py,sha256=qPQe8nCUXO_2slGzXoh8byL9q6r-c-F9wOnbwdatJzw,373
 pycmap/colorMaps.py,sha256=smPC0A24DLo-F4EkYqN3vFtXXOZAE1e8KCA0ftNy85E,3285
 pycmap/common.py,sha256=g54zV0fgJHvhh8HclFoUk193auVxMbM2mlKiDh-2Gvk,6980
 pycmap/deepC.py,sha256=3_9Mbcm6992PoVwj407XRob6xN3e76JAqYfLhsqkvaI,162
 pycmap/export.py,sha256=gkdO3VMeiITAsam9UF0EG3CycECmB7n-AB64eGZht10,2491
 pycmap/foliumHeat.py,sha256=fUNbCj6x1h42Y8aVtzigOm4YNJG_XwADK2uv8wZu__g,5858
 pycmap/hist.py,sha256=mlhJUrqJVIOwomYjO9y_GBHqubtaz-9GIM-WrYGIw20,6161
 pycmap/map.py,sha256=Wyn2jTjPpcKgju1zirb5T2zEN36AnQbe99V9Wr07PDQ,11764
 pycmap/match.py,sha256=c9gP3BPGkb57aTkrnJsMRC-V3O7roF5Yry6TWXejtJc,14443
 pycmap/rest.py,sha256=rm_6fjEliDsv3NJEpP9jg-Qd9uIgHj8nSFG796YyLdc,26314
-pycmap/sample.py,sha256=9XFItRRrKZUQNxquN6lX87SVG-HKv1UnX13lMw2niXM,7097
+pycmap/sample.py,sha256=mUCeDJKq4paeNA2Cb36fDlzJd1frXYAx-A-ZF5e1Kds,7427
 pycmap/section.py,sha256=48Uet5kAU4QnN3WbK6ms8AdSSS7QdQdF0Gz0OHkWl5w,13125
 pycmap/supervised.py,sha256=Ud9FV8_XFVvrPTP68E8jXdmfKPZyzg9FTzOgFYgCyKQ,16494
 pycmap/trend.py,sha256=elP8voj4x1Mi9J4lI2SEIWun0tVhGofcE5HO8ab8r3c,8332
 pycmap/viz.py,sha256=yUD5iRYaUHLnbKMrbtWXC3BmAzV1XDo8fYPqPUrDksw,17434
 pycmap/w3.py,sha256=q8P_WPQzkQPtALByV_h7qFypuXp0--Rqb9xhl0JZYoE,3918
-pycmap-0.2.8.dist-info/LICENSE,sha256=CO-rj8Ow4Kylvz7U14fEag0Y0HX_n4Fx5mbJPJ618PY,1089
-pycmap-0.2.8.dist-info/METADATA,sha256=SjOtzEDZRlVCb09vkRJKKwXoeu0AQ5rBGBypazCSgW4,7287
-pycmap-0.2.8.dist-info/WHEEL,sha256=g4nMs7d-Xl9-xC9XovUrsDHGXt-FT0E17Yqo92DEfvY,92
-pycmap-0.2.8.dist-info/top_level.txt,sha256=0kEiq9xSGcl_FNxUYM2b4PQpdlf-v_vKUyuHcl1ytcU,7
-pycmap-0.2.8.dist-info/RECORD,,
+pycmap-0.2.9.dist-info/LICENSE,sha256=CO-rj8Ow4Kylvz7U14fEag0Y0HX_n4Fx5mbJPJ618PY,1089
+pycmap-0.2.9.dist-info/METADATA,sha256=ULYd7dgoAzaVa9zULAWaaCArSQuJC_9S-lRP-aDu7hk,7287
+pycmap-0.2.9.dist-info/WHEEL,sha256=g4nMs7d-Xl9-xC9XovUrsDHGXt-FT0E17Yqo92DEfvY,92
+pycmap-0.2.9.dist-info/top_level.txt,sha256=0kEiq9xSGcl_FNxUYM2b4PQpdlf-v_vKUyuHcl1ytcU,7
+pycmap-0.2.9.dist-info/RECORD,,
```

