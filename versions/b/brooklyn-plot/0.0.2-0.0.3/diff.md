# Comparing `tmp/brooklyn_plot-0.0.2.tar.gz` & `tmp/brooklyn_plot-0.0.3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "brooklyn_plot-0.0.2.tar", last modified: Fri Mar 31 20:45:52 2023, max compression
+gzip compressed data, was "brooklyn_plot-0.0.3.tar", last modified: Thu Apr  6 17:50:59 2023, max compression
```

## Comparing `brooklyn_plot-0.0.2.tar` & `brooklyn_plot-0.0.3.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-03-31 20:45:52.844884 brooklyn_plot-0.0.2/
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)     1091 2023-03-29 18:17:30.000000 brooklyn_plot-0.0.2/LICENSE
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)       27 2023-03-29 18:17:30.000000 brooklyn_plot-0.0.2/MANIFEST.in
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)     1603 2023-03-31 20:45:52.844884 brooklyn_plot-0.0.2/PKG-INFO
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)      695 2023-03-29 18:17:30.000000 brooklyn_plot-0.0.2/README.rst
-drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-03-31 20:45:52.844884 brooklyn_plot-0.0.2/brooklyn_plot/
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)        1 2023-03-29 18:17:30.000000 brooklyn_plot-0.0.2/brooklyn_plot/__init__.py
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)     3499 2023-03-31 20:43:43.000000 brooklyn_plot-0.0.2/brooklyn_plot/__main__.py
-drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-03-31 20:45:52.844884 brooklyn_plot-0.0.2/brooklyn_plot/libs/
--rwxr-xr-x   0 apatil8   (1000) apatil8   (1000)     3689 2023-03-31 19:12:16.000000 brooklyn_plot-0.0.2/brooklyn_plot/libs/coexpression.py
--rwxr-xr-x   0 apatil8   (1000) apatil8   (1000)     1955 2023-03-31 20:44:05.000000 brooklyn_plot-0.0.2/brooklyn_plot/libs/parse.py
--rwxr-xr-x   0 apatil8   (1000) apatil8   (1000)     3025 2023-03-31 19:11:48.000000 brooklyn_plot-0.0.2/brooklyn_plot/libs/summary.py
-drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-03-31 20:45:52.844884 brooklyn_plot-0.0.2/brooklyn_plot/rScripts/
--rwxr-xr-x   0 apatil8   (1000) apatil8   (1000)     2101 2023-03-31 19:11:34.000000 brooklyn_plot-0.0.2/brooklyn_plot/rScripts/brooklynPlot.R
-drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-03-31 20:45:52.844884 brooklyn_plot-0.0.2/brooklyn_plot.egg-info/
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)     1603 2023-03-31 20:45:52.000000 brooklyn_plot-0.0.2/brooklyn_plot.egg-info/PKG-INFO
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)      446 2023-03-31 20:45:52.000000 brooklyn_plot-0.0.2/brooklyn_plot.egg-info/SOURCES.txt
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)        1 2023-03-31 20:45:52.000000 brooklyn_plot-0.0.2/brooklyn_plot.egg-info/dependency_links.txt
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)       63 2023-03-31 20:45:52.000000 brooklyn_plot-0.0.2/brooklyn_plot.egg-info/entry_points.txt
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)       26 2023-03-31 20:45:52.000000 brooklyn_plot-0.0.2/brooklyn_plot.egg-info/requires.txt
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)       14 2023-03-31 20:45:52.000000 brooklyn_plot-0.0.2/brooklyn_plot.egg-info/top_level.txt
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)       38 2023-03-31 20:45:52.844884 brooklyn_plot-0.0.2/setup.cfg
--rw-r--r--   0 apatil8   (1000) apatil8   (1000)     1577 2023-03-31 20:45:33.000000 brooklyn_plot-0.0.2/setup.py
+drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-04-06 17:50:59.858055 brooklyn_plot-0.0.3/
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)     1091 2023-04-06 17:42:20.000000 brooklyn_plot-0.0.3/LICENSE
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)       28 2023-04-06 17:47:54.000000 brooklyn_plot-0.0.3/MANIFEST.in
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)     1539 2023-04-06 17:50:59.858055 brooklyn_plot-0.0.3/PKG-INFO
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)      631 2023-04-01 00:03:36.000000 brooklyn_plot-0.0.3/README.rst
+drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-04-06 17:50:59.858055 brooklyn_plot-0.0.3/brooklyn_plot/
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)        1 2023-03-29 18:17:30.000000 brooklyn_plot-0.0.3/brooklyn_plot/__init__.py
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)     3499 2023-03-31 20:43:43.000000 brooklyn_plot-0.0.3/brooklyn_plot/__main__.py
+drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-04-06 17:50:59.858055 brooklyn_plot-0.0.3/brooklyn_plot/libs/
+-rwxr-xr-x   0 apatil8   (1000) apatil8   (1000)     3689 2023-03-31 19:12:16.000000 brooklyn_plot-0.0.3/brooklyn_plot/libs/coexpression.py
+-rwxr-xr-x   0 apatil8   (1000) apatil8   (1000)     1950 2023-04-05 17:30:26.000000 brooklyn_plot-0.0.3/brooklyn_plot/libs/parse.py
+-rwxr-xr-x   0 apatil8   (1000) apatil8   (1000)     3599 2023-04-05 17:30:26.000000 brooklyn_plot-0.0.3/brooklyn_plot/libs/summary.py
+drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-04-06 17:50:59.858055 brooklyn_plot-0.0.3/brooklyn_plot/rScripts/
+-rwxr-xr-x   0 apatil8   (1000) apatil8   (1000)     2101 2023-03-31 19:11:34.000000 brooklyn_plot-0.0.3/brooklyn_plot/rScripts/brooklynPlot.R
+drwxr-xr-x   0 apatil8   (1000) apatil8   (1000)        0 2023-04-06 17:50:59.858055 brooklyn_plot-0.0.3/brooklyn_plot.egg-info/
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)     1539 2023-04-06 17:50:59.000000 brooklyn_plot-0.0.3/brooklyn_plot.egg-info/PKG-INFO
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)      446 2023-04-06 17:50:59.000000 brooklyn_plot-0.0.3/brooklyn_plot.egg-info/SOURCES.txt
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)        1 2023-04-06 17:50:59.000000 brooklyn_plot-0.0.3/brooklyn_plot.egg-info/dependency_links.txt
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)       62 2023-04-06 17:50:59.000000 brooklyn_plot-0.0.3/brooklyn_plot.egg-info/entry_points.txt
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)       26 2023-04-06 17:50:59.000000 brooklyn_plot-0.0.3/brooklyn_plot.egg-info/requires.txt
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)       14 2023-04-06 17:50:59.000000 brooklyn_plot-0.0.3/brooklyn_plot.egg-info/top_level.txt
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)       38 2023-04-06 17:50:59.858055 brooklyn_plot-0.0.3/setup.cfg
+-rw-r--r--   0 apatil8   (1000) apatil8   (1000)     1577 2023-04-06 17:50:34.000000 brooklyn_plot-0.0.3/setup.py
```

### Comparing `brooklyn_plot-0.0.2/LICENSE` & `brooklyn_plot-0.0.3/LICENSE`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 MIT License
 
-Copyright (c) 2020 Arun H. Patil and Marc K. Halushka
+Copyright (c) 2022 Arun H. Patil and Marc K. Halushka
 
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
```

### Comparing `brooklyn_plot-0.0.2/PKG-INFO` & `brooklyn_plot-0.0.3/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: brooklyn_plot
-Version: 0.0.2
+Version: 0.0.3
 Summary: Gene co-expression and transcriptional bursting pattern recognition tool in single cell/nucleus RNA-sequencing data
 Home-page: https://github.com/mhalushka/brooklyn/
 Author: Arun Patil and Marc Halushka
 Author-email: mhalush1@jhmi.edu
 License: MIT
 Keywords: brooklyn,single cell,single nucleus,single cell-RNA,single nucleus-RNA,RNA analysis,cellxgene,RNA-seq,bioinformatics tools,co-expression,transcriptional bursting,sc-RNAseq,sn-RNAseq
 Platform: UNKNOWN
@@ -18,25 +18,23 @@
 Requires-Python: >=3.7
 License-File: LICENSE
 
 ========
 Brooklyn
 ========
 
-
-Brooklyn plot for single cell/nuclei RNA sequencing data. This package enables the pair-wise (ie., many to many) gene comparison and reports the co-expressed genes spanning few kilo basepairs and plots a brooklyn plot for visualization. More about this in the documentation below. 
+Brooklyn plot for single cell/nuclei RNA sequencing data. This package enables a Pearson pairwise (ie., many to many) gene comparison and outputs co-expression patterns of genes across the genome. It generates a Brooklyn plot for visualization. More about this in the documentation below.
 
 Links
 -----
 
-* `Documentation <https://mirge3.readthedocs.io/en/master/>`_
-* `Source code <https://github.com/mhalushka/brooklyn/>`_
-* `Frequently asked questions <https://mirge3.readthedocs.io/en/latest/faqs.html>`_
-* `Report an issue <https://github.com/mhalushka/brooklyn/issues>`_
-* `Project page on PyPI <https://pypi.python.org/pypi/brooklyn/>`_
+* `Documentation <https://brooklyn-plot.readthedocs.io/en/latest/>`_
+* `Source code <https://github.com/arunhpatil/brooklyn/>`_
+* `Report an issue <https://github.com/arunhpatil/brooklyn/issues>`_
+* `Project page on PyPI <https://pypi.python.org/pypi/brooklyn-plot/>`_
 
 ========
 Citation
 ========
```

### Comparing `brooklyn_plot-0.0.2/brooklyn_plot/__main__.py` & `brooklyn_plot-0.0.3/brooklyn_plot/__main__.py`

 * *Files identical despite different names*

### Comparing `brooklyn_plot-0.0.2/brooklyn_plot/libs/coexpression.py` & `brooklyn_plot-0.0.3/brooklyn_plot/libs/coexpression.py`

 * *Files identical despite different names*

### Comparing `brooklyn_plot-0.0.2/brooklyn_plot/libs/parse.py` & `brooklyn_plot-0.0.3/brooklyn_plot/libs/parse.py`

 * *Files 5% similar despite different names*

```diff
@@ -2,24 +2,25 @@
 import sys
 import argparse
 import subprocess
 from pkg_resources import get_distribution
 
 def parseArg():
     version = get_distribution("brooklyn_plot").version
-    parser = argparse.ArgumentParser(description='Brooklyn (Gene co-expression and transcriptional bursting pattern recognition tool in single cell/nucleus RNA-sequencing data)',usage='brooklyn [options]',formatter_class=argparse.RawTextHelpFormatter,)
+    parser = argparse.ArgumentParser(description='Brooklyn (Gene co-expression and transcriptional bursting pattern recognition tool in single cell/nucleus RNA-sequencing data)',usage='brooklyn_plot [options]',formatter_class=argparse.RawTextHelpFormatter,)
     if len(sys.argv)==1:
         parser.print_help(sys.stderr)
         sys.exit(1)
     parser.add_argument('--version', action='version', version='%s'%(version))
-    group = parser.add_argument_group("Options",description='''-h5,    --h5ad            input file in .h5ad format (accepts .h5ad) 
+    group = parser.add_argument_group("Options",description='''
+-h5,   --h5ad               input file in .h5ad format (accepts .h5ad) 
 -ba,   --biomart            the reference gene annotations (in .csv format) 
 -od,   --outDir             the directory of the outputs (Default: brooklyn-date-hh-mm-ss) 
--of,   --outFile            the name of summarized brooklyn file as CSV file and a brooklyn plot in PDF (Default: brooklyn-date-hh-mm-ss)
--ql,   --query              the list of genes to be queired upon (one gene per line and in .csv format)
+-of,   --outFile            the name of summarized brooklyn file as CSV file and a brooklyn plot in PDF (Default: brooklyn)
+-ql,   --query              the list of genes to be queried upon (one gene per line and in .csv format)
 -sl,   --subject            the list of genes to be compared with (one gene per line and in .csv format)
 -cpu,  --threads            the number of processors to use for trimming, qc, and alignment (Default: 1)
 ''')
     group.add_argument('-h5', '--h5ad', required=True, help=argparse.SUPPRESS) 
     group.add_argument('-ba', '--biomart', required=True, help=argparse.SUPPRESS)
     group.add_argument('-od', '--outDir', help=argparse.SUPPRESS)
     group.add_argument('-of', '--outFile', help=argparse.SUPPRESS)
```

### Comparing `brooklyn_plot-0.0.2/brooklyn_plot/libs/summary.py` & `brooklyn_plot-0.0.3/brooklyn_plot/libs/summary.py`

 * *Files 13% similar despite different names*

```diff
@@ -46,18 +46,18 @@
     summarizedDF = pd.DataFrame(new_emptyList, columns = ['gene', 'r', 'p', 'bon', 'neg_log10_p', 'hgnc_symbol','chromosome_name', 'start_position', 'xMean', 'end_position', 'band', 'occurence', 'denominator', 'percent_occurence'])
     summarizedDF = summarizedDF.round(decimals = 2)
     summarizedDF.to_csv(brookSum, index=False)
 
     df2 = summarizedDF
     # Create chromosome order and sort accordingly
     chrOrder = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', 'X', 'Y', 'M', 'MT']
-    chrIndex = dict(zip(chrOrder, range(len(chrOrder))))
-    df2 = df2[df2['chromosome_name'].notna()]
-    df2['chromosome_name'] = df2['chromosome_name'].astype('string')
-    df2['ChrOrder'] = df2['chromosome_name'].map(chrIndex)
-    df2.to_csv("chrorder_temp.csv", index=False)
-    df2['ChrOrder'] = df2['ChrOrder'].astype('int')
-    df2.sort_values(['ChrOrder', 'end_position'], ascending = True, inplace = True)
-    df2.drop(columns='ChrOrder', inplace = True)
-    df2.to_csv(brookSumSorted, index=False)
+    chrIndex = dict(zip(chrOrder, range(len(chrOrder)))) # Creates a dictionary of chromosomes and a serial number as value
+    df2 = df2[df2['chromosome_name'].notna()] # Filter out any rows which don't represent any chromosomes (such as blank lines at the EOF)
+    df2['chromosome_name'] = df2['chromosome_name'].astype('string') # Making sure the column chromosome name is a string data type
+    df2 = df2.loc[df2['chromosome_name'].isin(chrOrder)] # Check for only chromosomes and avoid any patches
+    df2['ChrOrder'] = df2['chromosome_name'].map(chrIndex) # Creating a new column chrOrder which defines the order of each chromosomes.
+    df2['ChrOrder'] = df2['ChrOrder'].astype('int') # Making sure the column chrOrder is a integer 
+    df2.sort_values(['ChrOrder', 'end_position'], ascending = True, inplace = True) # Sort based on chromosome order and end position of each gene 
+    df2.drop(columns='ChrOrder', inplace = True) # Drop column chromosome order which is no longer required
+    df2.to_csv(brookSumSorted, index=False) # Write the sorted dataframe to a CSV file
     globalend_time = time.perf_counter()
     print(f'\nThe summary is completed in {round(globalend_time-globalstart, 4)} second(s)\n')
```

### Comparing `brooklyn_plot-0.0.2/brooklyn_plot/rScripts/brooklynPlot.R` & `brooklyn_plot-0.0.3/brooklyn_plot/rScripts/brooklynPlot.R`

 * *Files identical despite different names*

### Comparing `brooklyn_plot-0.0.2/brooklyn_plot.egg-info/PKG-INFO` & `brooklyn_plot-0.0.3/brooklyn_plot.egg-info/PKG-INFO`

 * *Files 18% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: brooklyn-plot
-Version: 0.0.2
+Version: 0.0.3
 Summary: Gene co-expression and transcriptional bursting pattern recognition tool in single cell/nucleus RNA-sequencing data
 Home-page: https://github.com/mhalushka/brooklyn/
 Author: Arun Patil and Marc Halushka
 Author-email: mhalush1@jhmi.edu
 License: MIT
 Keywords: brooklyn,single cell,single nucleus,single cell-RNA,single nucleus-RNA,RNA analysis,cellxgene,RNA-seq,bioinformatics tools,co-expression,transcriptional bursting,sc-RNAseq,sn-RNAseq
 Platform: UNKNOWN
@@ -18,25 +18,23 @@
 Requires-Python: >=3.7
 License-File: LICENSE
 
 ========
 Brooklyn
 ========
 
-
-Brooklyn plot for single cell/nuclei RNA sequencing data. This package enables the pair-wise (ie., many to many) gene comparison and reports the co-expressed genes spanning few kilo basepairs and plots a brooklyn plot for visualization. More about this in the documentation below. 
+Brooklyn plot for single cell/nuclei RNA sequencing data. This package enables a Pearson pairwise (ie., many to many) gene comparison and outputs co-expression patterns of genes across the genome. It generates a Brooklyn plot for visualization. More about this in the documentation below.
 
 Links
 -----
 
-* `Documentation <https://mirge3.readthedocs.io/en/master/>`_
-* `Source code <https://github.com/mhalushka/brooklyn/>`_
-* `Frequently asked questions <https://mirge3.readthedocs.io/en/latest/faqs.html>`_
-* `Report an issue <https://github.com/mhalushka/brooklyn/issues>`_
-* `Project page on PyPI <https://pypi.python.org/pypi/brooklyn/>`_
+* `Documentation <https://brooklyn-plot.readthedocs.io/en/latest/>`_
+* `Source code <https://github.com/arunhpatil/brooklyn/>`_
+* `Report an issue <https://github.com/arunhpatil/brooklyn/issues>`_
+* `Project page on PyPI <https://pypi.python.org/pypi/brooklyn-plot/>`_
 
 ========
 Citation
 ========
```

### Comparing `brooklyn_plot-0.0.2/setup.py` & `brooklyn_plot-0.0.3/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 from setuptools import setup, find_packages, find_namespace_packages
 
 with open("README.rst", "r") as fh:
     long_description = fh.read()
 
 setup(
         name='brooklyn_plot',
-        version='0.0.2',
+        version='0.0.3',
         author='Arun Patil and Marc Halushka',
         author_email='mhalush1@jhmi.edu',
         url='https://github.com/mhalushka/brooklyn/',
         description='Gene co-expression and transcriptional bursting pattern recognition tool in single cell/nucleus RNA-sequencing data',
         long_description=long_description,
         keywords=['brooklyn', 'single cell', 'single nucleus', 'single cell-RNA', 'single nucleus-RNA', 'RNA analysis', 'cellxgene', 'RNA-seq', 'bioinformatics tools', 'co-expression', 'transcriptional bursting', 'sc-RNAseq', 'sn-RNAseq'],  # arbitrary keywords
         license='MIT',
```

