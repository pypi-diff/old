# Comparing `tmp/cldcatplot-0.8.tar.gz` & `tmp/cldcatplot-0.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "cldcatplot-0.8.tar", last modified: Fri Nov  4 11:56:30 2022, max compression
+gzip compressed data, was "cldcatplot-0.9.tar", last modified: Mon Mar 27 11:38:24 2023, max compression
```

## Comparing `cldcatplot-0.8.tar` & `cldcatplot-0.9.tar`

### file list

```diff
@@ -1,16 +1,16 @@
-drwxrwxrwx   0        0        0        0 2022-11-04 11:56:30.747013 cldcatplot-0.8/
--rw-rw-rw-   0        0        0        3 2022-11-04 09:43:31.000000 cldcatplot-0.8/LICENSE
--rw-rw-rw-   0        0        0      222 2022-11-04 11:56:30.747013 cldcatplot-0.8/PKG-INFO
--rw-rw-rw-   0        0        0        0 2022-11-04 09:43:31.000000 cldcatplot-0.8/README.md
--rw-rw-rw-   0        0        0       86 2022-11-04 11:56:30.756043 cldcatplot-0.8/setup.cfg
--rw-rw-rw-   0        0        0      429 2022-11-04 11:56:12.000000 cldcatplot-0.8/setup.py
-drwxrwxrwx   0        0        0        0 2022-11-04 11:56:30.624240 cldcatplot-0.8/src/
-drwxrwxrwx   0        0        0        0 2022-11-04 11:56:30.676554 cldcatplot-0.8/src/cldcatplot/
--rw-rw-rw-   0        0        0        0 2022-11-04 09:43:32.000000 cldcatplot-0.8/src/cldcatplot/__init__.py
--rw-rw-rw-   0        0        0     9126 2022-11-04 11:55:40.000000 cldcatplot-0.8/src/cldcatplot/cldcatplot.py
-drwxrwxrwx   0        0        0        0 2022-11-04 11:56:30.739271 cldcatplot-0.8/src/cldcatplot.egg-info/
--rw-rw-rw-   0        0        0      222 2022-11-04 11:56:30.000000 cldcatplot-0.8/src/cldcatplot.egg-info/PKG-INFO
--rw-rw-rw-   0        0        0      281 2022-11-04 11:56:30.000000 cldcatplot-0.8/src/cldcatplot.egg-info/SOURCES.txt
--rw-rw-rw-   0        0        0        1 2022-11-04 11:56:30.000000 cldcatplot-0.8/src/cldcatplot.egg-info/dependency_links.txt
--rw-rw-rw-   0        0        0       38 2022-11-04 11:56:30.000000 cldcatplot-0.8/src/cldcatplot.egg-info/requires.txt
--rw-rw-rw-   0        0        0       11 2022-11-04 11:56:30.000000 cldcatplot-0.8/src/cldcatplot.egg-info/top_level.txt
+drwxrwxrwx   0        0        0        0 2023-03-27 11:38:24.335239 cldcatplot-0.9/
+-rw-rw-rw-   0        0        0        3 2022-11-04 09:43:31.000000 cldcatplot-0.9/LICENSE
+-rw-rw-rw-   0        0        0      222 2023-03-27 11:38:24.335239 cldcatplot-0.9/PKG-INFO
+-rw-rw-rw-   0        0        0        0 2022-11-04 09:43:31.000000 cldcatplot-0.9/README.md
+-rw-rw-rw-   0        0        0       86 2023-03-27 11:38:24.354490 cldcatplot-0.9/setup.cfg
+-rw-rw-rw-   0        0        0      429 2023-03-27 11:37:14.000000 cldcatplot-0.9/setup.py
+drwxrwxrwx   0        0        0        0 2023-03-27 11:38:23.987880 cldcatplot-0.9/src/
+drwxrwxrwx   0        0        0        0 2023-03-27 11:38:24.181485 cldcatplot-0.9/src/cldcatplot/
+-rw-rw-rw-   0        0        0        0 2022-11-04 09:43:32.000000 cldcatplot-0.9/src/cldcatplot/__init__.py
+-rw-rw-rw-   0        0        0     9346 2023-03-27 11:36:36.000000 cldcatplot-0.9/src/cldcatplot/cldcatplot.py
+drwxrwxrwx   0        0        0        0 2023-03-27 11:38:24.319294 cldcatplot-0.9/src/cldcatplot.egg-info/
+-rw-rw-rw-   0        0        0      222 2023-03-27 11:38:22.000000 cldcatplot-0.9/src/cldcatplot.egg-info/PKG-INFO
+-rw-rw-rw-   0        0        0      281 2023-03-27 11:38:22.000000 cldcatplot-0.9/src/cldcatplot.egg-info/SOURCES.txt
+-rw-rw-rw-   0        0        0        1 2023-03-27 11:38:22.000000 cldcatplot-0.9/src/cldcatplot.egg-info/dependency_links.txt
+-rw-rw-rw-   0        0        0       38 2023-03-27 11:38:22.000000 cldcatplot-0.9/src/cldcatplot.egg-info/requires.txt
+-rw-rw-rw-   0        0        0       11 2023-03-27 11:38:22.000000 cldcatplot-0.9/src/cldcatplot.egg-info/top_level.txt
```

### Comparing `cldcatplot-0.8/src/cldcatplot/cldcatplot.py` & `cldcatplot-0.9/src/cldcatplot/cldcatplot.py`

 * *Files 2% similar despite different names*

```diff
@@ -19,14 +19,18 @@
         kwargs["letterSize"] = matplotlib.rcParams["font.size"]
     letterSize = kwargs["letterSize"]
     del kwargs["letterSize"]
     if "pointStyle" not in kwargs:
         kwargs["pointStyle"] = None
     pointStyle = kwargs["pointStyle"]
     del kwargs["pointStyle"]
+    if "printTest" not in kwargs:
+        kwargs["printTest"] = False
+    printTest = kwargs["printTest"]
+    del kwargs["printTest"]
     if "separateCld" not in kwargs:
         kwargs["separateCld"] = False
     separateCld = kwargs["separateCld"]
     if separateCld:
         filterFacet_vars = ["row","col"]
     else:
         filterFacet_vars = []
@@ -50,14 +54,17 @@
     letters = []
     for filterVal in tk["filterFacets"].unique().tolist():
         tkf = tk[tk["filterFacets"] == filterVal]
         tukey = pairwise_tukeyhsd(endog=tkf['values'],
                             groups=tkf['comb'],
                             alpha=0.05)
         tukey_df = pd.DataFrame(data=tukey._results_table.data[1:], columns=tukey._results_table.data[0])
+        if printTest:
+            print(filterVal)
+            print(tukey_df)
         letters_df = makeletters(tukey_df,alpha=0.05,sortingOrder=median_df.index.tolist())
         letters.extend([[x[1],x[2]] for x in letters_df.reset_index().values.tolist()])
 
     def sortCustom(a,b):
         aj = json.loads(a[0])
         bj = json.loads(b[0])
         for var in facets:
```

