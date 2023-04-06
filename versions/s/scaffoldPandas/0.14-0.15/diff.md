# Comparing `tmp/scaffoldpandas-0.14.tar.gz` & `tmp/scaffoldpandas-0.15.tar.gz`

## Comparing `scaffoldpandas-0.14.tar` & `scaffoldpandas-0.15.tar`

### file list

```diff
@@ -1,8 +1,9 @@
--rw-r--r--   0        0        0      398 2020-02-02 00:00:00.000000 scaffoldpandas-0.14/setup.py
--rw-r--r--   0        0        0       21 2020-02-02 00:00:00.000000 scaffoldpandas-0.14/scaffoldPandas/__init__.py
--rw-r--r--   0        0        0    11153 2020-02-02 00:00:00.000000 scaffoldpandas-0.14/scaffoldPandas/scaffoldPandas.py
--rw-r--r--   0        0        0     1961 2020-02-02 00:00:00.000000 scaffoldpandas-0.14/.gitignore
--rw-r--r--   0        0        0    35823 2020-02-02 00:00:00.000000 scaffoldpandas-0.14/LICENSE
--rw-r--r--   0        0        0     3486 2020-02-02 00:00:00.000000 scaffoldpandas-0.14/README.md
--rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 scaffoldpandas-0.14/pyproject.toml
--rw-r--r--   0        0        0     3943 2020-02-02 00:00:00.000000 scaffoldpandas-0.14/PKG-INFO
+-rw-r--r--   0        0        0      137 2020-02-02 00:00:00.000000 scaffoldpandas-0.15/requirements.txt
+-rw-r--r--   0        0        0      398 2020-02-02 00:00:00.000000 scaffoldpandas-0.15/setup.py
+-rw-r--r--   0        0        0       21 2020-02-02 00:00:00.000000 scaffoldpandas-0.15/scaffoldPandas/__init__.py
+-rw-r--r--   0        0        0    13072 2020-02-02 00:00:00.000000 scaffoldpandas-0.15/scaffoldPandas/pdscaffold.py
+-rw-r--r--   0        0        0     1961 2020-02-02 00:00:00.000000 scaffoldpandas-0.15/.gitignore
+-rw-r--r--   0        0        0    35823 2020-02-02 00:00:00.000000 scaffoldpandas-0.15/LICENSE
+-rw-r--r--   0        0        0     3486 2020-02-02 00:00:00.000000 scaffoldpandas-0.15/README.md
+-rw-r--r--   0        0        0      599 2020-02-02 00:00:00.000000 scaffoldpandas-0.15/pyproject.toml
+-rw-r--r--   0        0        0     3943 2020-02-02 00:00:00.000000 scaffoldpandas-0.15/PKG-INFO
```

### Comparing `scaffoldpandas-0.14/scaffoldPandas/scaffoldPandas.py` & `scaffoldpandas-0.15/scaffoldPandas/pdscaffold.py`

 * *Files 17% similar despite different names*

```diff
@@ -292,30 +292,72 @@
 ## Connect two or more dataframes together that probably overlap, dropping 
 ## whatever is duplicated
 #firstDataFrame = pandas.DataFrame()
 #secondDataFrame = pandas.DataFrame()
 #newDataFrame = pandas.concat( [firstDataFrame , firstDataFrame] ).drop_duplicates()
 #
 #
+## Connect two dataframes that *don't* overlap, using either merge or concat
+#
+## concat requires implicit connecion criteria
+#newdataframe = pandas.concat([onedf, otherdf], axis=1, join="inner")
+#
+## merge requires explicit connection criteria
+#newdataframe = pandas.merge(onedf, otherdf, on=CONNECTIONCOLUMN)
+#
+#
 ## Change the encoding of NotANumber on import - useful when your data has 
 ## inadvertent entries that are not null, like sodium (NA)
 #from pandas._libs.parsers import STR_NA_VALUES
 #
+## NOTE: STR_NA_VALUES is a set, so you can use set operations on it (add(), remove(), clear())
+#
 #disable_na_values = { "NA" }
-#my_default_na_values = STR_NA_VALUES - disable_na_values
+#my_default_na_values = STR_NA_VALUES.remove(disable_na_values)
 #df = pandas.read_csv( "myCSVfile.csv" , na_values = my_default_na_values )
 #
 #
 ## Pad out values with 4 leading zeros on pandas.read_csv()
 #df = pandas.read_csv("myCSVfile.csv", converters={'UnpaddedColumn1': '{:0>4}'.format, 'UnpaddedColumn2': '{:0>4}'.format}) 
 #
 #
+## Put all information for a given ID from multiple rows to a single row
+#
+#raw_data = {'patient': [1, 1, 1, 2, 2],
+#                'obs': [1, 2, 3, 1, 2],
+#          'treatment': [0, 1, 0, 1, 0],
+#              'score': [6252, 24243, 2345, 2342, 23525],
+#            'onetime': ["thing",pandas.NA,pandas.NA,"stuff",pandas.NA]}
+#
+#topivot = pandas.DataFrame(raw_data, columns = ['patient', 'obs', 'treatment', 'score', 'onetime'])
+#topivot.head
+#pivoted = topivot.pivot(index='patient', columns='obs', values='score')
+#pivoted.head
+#
+## Propogate the first value down a column based on another column value (ID) 
+## (push demographic data for person X to all person X rows).
+#df.columnToFill = df.groupby("ID").columnToFill.transform("first")
+#
 ## Filter a dataframe into a subset that all meets a criteria.
 ## In the example case, we use pandas.factorize() to get all of the values, 
 ## because it _should_ be a small set, but there are mispellings, other 
 ## weirdness that we have to find, so this pattern lets us group all rows 
 ## that have the set of values in the list
 #
 #pos = ['DÉTECTÉ', 'DÉTEDÉTECTÉ', 'detecté', 'detecte', '03DÉTECTÉ']
 #
 #posCases = firstDataFrame[firstDataFrame["RESULTAT"].isin(pos)]
-
+#
+#
+## Take a series of rows that are sparse but related rows with an identifying 
+## column, and turn them into a "flat" dataframe where there is just one row 
+## per identifier. Look at "aggregate" functions.
+#
+#df = pandas.DataFrame([{"id":0,"a":1,"b":pandas.NA,"c":pandas.NA,},{"id":0,"a":pandas.NA,"b":1,"c":pandas.NA,},{"id":0,"a":pandas.NA,"b":pandas.NA,"c":1,},{"id":0,"a":pandas.NA,"b":pandas.NA,"c":pandas.NA,}])
+#
+#flatDF = df.groupby("id").first()
+#
+#
+## If you have accents in your column headings, it can be a PITA to type and
+## use. You can extract the column headings into a list, and then replace then
+## by index, preventing you from typing anything difficult.
+# df.columns.values[2] = "newname"
```

### Comparing `scaffoldpandas-0.14/.gitignore` & `scaffoldpandas-0.15/.gitignore`

 * *Files identical despite different names*

### Comparing `scaffoldpandas-0.14/LICENSE` & `scaffoldpandas-0.15/LICENSE`

 * *Files identical despite different names*

### Comparing `scaffoldpandas-0.14/README.md` & `scaffoldpandas-0.15/README.md`

 * *Files identical despite different names*

### Comparing `scaffoldpandas-0.14/pyproject.toml` & `scaffoldpandas-0.15/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["hatchling"]
 build-backend = "hatchling.build"
 
 [project]
 name = "scaffoldPandas"
-version = "0.14"
+version = "0.15"
 authors = [
   { name="William Witteman", email="william@witteman.ca" },
 ]
 description = "Helpful functions for pandas"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

### Comparing `scaffoldpandas-0.14/PKG-INFO` & `scaffoldpandas-0.15/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: scaffoldPandas
-Version: 0.14
+Version: 0.15
 Summary: Helpful functions for pandas
 Project-URL: Homepage, https://github.com/PatrickArchambault-EquipeRecherche/scaffold-pandas
 Author-email: William Witteman <william@witteman.ca>
 License-File: LICENSE
 Classifier: License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)
 Classifier: Operating System :: OS Independent
 Classifier: Programming Language :: Python :: 3
```

