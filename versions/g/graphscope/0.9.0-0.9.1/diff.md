# Comparing `tmp/graphscope-0.9.0-py2.py3-none-macosx_10_9_x86_64.whl.zip` & `tmp/graphscope-0.9.1-py2.py3-none-macosx_11_0_arm64.whl.zip`

## zipinfo {}

```diff
@@ -1,7 +1,7 @@
-Zip file size: 9089 bytes, number of entries: 5
--rw-rw-r--  2.0 unx      382 b- defN 21-Dec-03 13:05 graphscope-0.9.0.dist-info/RECORD
--rw-r--r--  2.0 unx      140 b- defN 21-Dec-03 13:05 graphscope-0.9.0.dist-info/WHEEL
--rw-r--r--  2.0 unx        4 b- defN 21-Dec-03 13:05 graphscope-0.9.0.dist-info/top_level.txt
--rw-r--r--  2.0 unx    20122 b- defN 21-Dec-03 13:05 graphscope-0.9.0.dist-info/METADATA
--rw-r--r--  2.0 unx      711 b- defN 21-Dec-03 11:09 foo/__init__.py
-5 files, 21359 bytes uncompressed, 8377 bytes compressed:  60.8%
+Zip file size: 9116 bytes, number of entries: 5
+-rw-r--r--  2.0 unx      711 b- defN 21-Nov-14 07:52 foo/__init__.py
+-rw-rw-r--  2.0 unx      382 b- defN 21-Dec-23 08:11 graphscope-0.9.1.dist-info/RECORD
+-rw-r--r--  2.0 unx      138 b- defN 21-Dec-23 08:11 graphscope-0.9.1.dist-info/WHEEL
+-rw-r--r--  2.0 unx        4 b- defN 21-Dec-23 08:11 graphscope-0.9.1.dist-info/top_level.txt
+-rw-r--r--  2.0 unx    20267 b- defN 21-Dec-23 08:11 graphscope-0.9.1.dist-info/METADATA
+5 files, 21502 bytes uncompressed, 8404 bytes compressed:  60.9%
```

## zipnote {}

```diff
@@ -1,16 +1,16 @@
-Filename: graphscope-0.9.0.dist-info/RECORD
+Filename: foo/__init__.py
 Comment: 
 
-Filename: graphscope-0.9.0.dist-info/WHEEL
+Filename: graphscope-0.9.1.dist-info/RECORD
 Comment: 
 
-Filename: graphscope-0.9.0.dist-info/top_level.txt
+Filename: graphscope-0.9.1.dist-info/WHEEL
 Comment: 
 
-Filename: graphscope-0.9.0.dist-info/METADATA
+Filename: graphscope-0.9.1.dist-info/top_level.txt
 Comment: 
 
-Filename: foo/__init__.py
+Filename: graphscope-0.9.1.dist-info/METADATA
 Comment: 
 
 Zip file comment:
```

## Comparing `graphscope-0.9.0.dist-info/METADATA` & `graphscope-0.9.1.dist-info/METADATA`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: graphscope
-Version: 0.9.0
+Version: 0.9.1
 Summary: UNKNOWN
 Home-page: https://github.com/alibaba/GraphScope
 Author: GraphScope Team, Damo Academy
 Author-email: graphscope@alibaba-inc.com
 License: Apache License 2.0
 Keywords: GraphScope,Graph Computations
 Platform: UNKNOWN
@@ -18,30 +18,31 @@
 Classifier: Programming Language :: Python
 Classifier: Programming Language :: Python :: 3
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: 3.8
 Classifier: Programming Language :: Python :: 3.9
 Description-Content-Type: text/markdown
-Requires-Dist: gs-coordinator (>=0.9.0)
-Requires-Dist: gs-jython (>=0.9.0)
-Requires-Dist: gs-lib (>=0.9.0)
-Requires-Dist: gs-engine (>=0.9.0)
-Requires-Dist: gs-include (>=0.9.0)
+Requires-Dist: gs-coordinator (>=0.9.1)
+Requires-Dist: gs-jython (>=0.9.1)
+Requires-Dist: gs-lib (>=0.9.1)
+Requires-Dist: gs-engine (>=0.9.1)
+Requires-Dist: gs-include (>=0.9.1)
 
 <h1 align="center">
     <img src="https://graphscope.io/assets/images/graphscope-logo.svg" width="400" alt="graphscope-logo">
 </h1>
 <p align="center">
     A One-Stop Large-Scale Graph Computing System from Alibaba
 </p>
 
 [![GraphScope CI](https://github.com/alibaba/GraphScope/workflows/GraphScope%20CI/badge.svg)](https://github.com/alibaba/GraphScope/actions?workflow=GraphScope+CI)
 [![Coverage](https://codecov.io/gh/alibaba/GraphScope/branch/main/graph/badge.svg)](https://codecov.io/gh/alibaba/GraphScope)
 [![Playground](https://shields.io/badge/JupyterLab-Try%20GraphScope%20Now!-F37626?logo=jupyter)](https://try.graphscope.app)
+[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/alibaba/GraphScope)
 [![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/graphscope)](https://artifacthub.io/packages/helm/graphscope/graphscope)
 [![Docs-en](https://shields.io/badge/Docs-English-blue?logo=Read%20The%20Docs)](https://graphscope.io/docs)
 [![FAQ-en](https://img.shields.io/badge/-FAQ-blue?logo=Read%20The%20Docs)](https://graphscope.io/docs/frequently_asked_questions.html)
 [![Docs-zh](https://shields.io/badge/Docs-%E4%B8%AD%E6%96%87-blue?logo=Read%20The%20Docs)](https://graphscope.io/docs/zh/)
 [![FAQ-zh](https://img.shields.io/badge/-FAQ%E4%B8%AD%E6%96%87-blue?logo=Read%20The%20Docs)](https://graphscope.io/docs/zh/frequently_asked_questions.html)
 [![README-zh](https://shields.io/badge/README-%E4%B8%AD%E6%96%87-blue)](README-zh.md)
 
@@ -394,15 +395,15 @@
 Documentation can be generated using Sphinx. Users can build the documentation using:
 
 ```bash
 # build the docs
 make graphscope-docs
 
 # to open preview on local
-open docs/_build/html/index.html
+open docs/_build/latest/html/index.html
 ```
 
 The latest version of online documentation can be found at https://graphscope.io/docs
 
 
 ## License
```

