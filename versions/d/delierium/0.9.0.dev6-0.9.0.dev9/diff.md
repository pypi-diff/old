# Comparing `tmp/delierium-0.9.0.dev6-py3-none-any.whl.zip` & `tmp/delierium-0.9.0.dev9-py3-none-any.whl.zip`

## zipinfo {}

```diff
@@ -1,11 +1,11 @@
-Zip file size: 15456 bytes, number of entries: 9
+Zip file size: 15427 bytes, number of entries: 9
 -rw-rw-r--  2.0 unx     6136 b- defN 23-Apr-05 11:00 delierium/DerivativeOperators.py
--rw-rw-r--  2.0 unx    13186 b- defN 23-Apr-06 17:30 delierium/Infinitesimals.py
+-rw-rw-r--  2.0 unx    13095 b- defN 23-Apr-06 17:38 delierium/Infinitesimals.py
 -rw-rw-r--  2.0 unx      538 b- defN 23-Apr-05 13:25 delierium/__init__.py
 -rw-rw-r--  2.0 unx    15332 b- defN 23-Apr-05 11:00 delierium/helpers.py
--rw-rw-r--  2.0 unx     1065 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/LICENSE
--rw-rw-r--  2.0 unx     4504 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/METADATA
--rw-rw-r--  2.0 unx       92 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/WHEEL
--rw-rw-r--  2.0 unx       16 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/top_level.txt
-?rw-rw-r--  2.0 unx      750 b- defN 23-Apr-06 17:35 delierium-0.9.0.dev6.dist-info/RECORD
-9 files, 41619 bytes uncompressed, 14162 bytes compressed:  66.0%
+-rw-rw-r--  2.0 unx     1065 b- defN 23-Apr-06 17:38 delierium-0.9.0.dev9.dist-info/LICENSE
+-rw-rw-r--  2.0 unx     4504 b- defN 23-Apr-06 17:38 delierium-0.9.0.dev9.dist-info/METADATA
+-rw-rw-r--  2.0 unx       92 b- defN 23-Apr-06 17:38 delierium-0.9.0.dev9.dist-info/WHEEL
+-rw-rw-r--  2.0 unx       16 b- defN 23-Apr-06 17:38 delierium-0.9.0.dev9.dist-info/top_level.txt
+?rw-rw-r--  2.0 unx      750 b- defN 23-Apr-06 17:38 delierium-0.9.0.dev9.dist-info/RECORD
+9 files, 41528 bytes uncompressed, 14133 bytes compressed:  66.0%
```

## zipnote {}

```diff
@@ -6,23 +6,23 @@
 
 Filename: delierium/__init__.py
 Comment: 
 
 Filename: delierium/helpers.py
 Comment: 
 
-Filename: delierium-0.9.0.dev6.dist-info/LICENSE
+Filename: delierium-0.9.0.dev9.dist-info/LICENSE
 Comment: 
 
-Filename: delierium-0.9.0.dev6.dist-info/METADATA
+Filename: delierium-0.9.0.dev9.dist-info/METADATA
 Comment: 
 
-Filename: delierium-0.9.0.dev6.dist-info/WHEEL
+Filename: delierium-0.9.0.dev9.dist-info/WHEEL
 Comment: 
 
-Filename: delierium-0.9.0.dev6.dist-info/top_level.txt
+Filename: delierium-0.9.0.dev9.dist-info/top_level.txt
 Comment: 
 
-Filename: delierium-0.9.0.dev6.dist-info/RECORD
+Filename: delierium-0.9.0.dev9.dist-info/RECORD
 Comment: 
 
 Zip file comment:
```

## delierium/Infinitesimals.py

```diff
@@ -14,17 +14,14 @@
 from sage.calculus.var import function, var
 from sage.misc.html import html
 from sage.symbolic.operators import FDerivativeOperator
 from sage.symbolic.relation import solve
 
 from delierium.DerivativeOperators import FrechetD
 from delierium.helpers import latexer, ExpressionTree
-#from delierium.JanetBasis import Janet_Basis
-
-from IPython.core.debugger import set_trace
 from IPython.display import Math
 
 def prolongationFunction(f: list, x: list, order) -> list:
     '''
     >>> x, y, z = var("x y z")
     >>> f = function("f")(x, y, z)
     >>> set(prolongationFunction([f], [x, y, z], 2)) == set(
```

## Comparing `delierium-0.9.0.dev6.dist-info/LICENSE` & `delierium-0.9.0.dev9.dist-info/LICENSE`

 * *Files identical despite different names*

## Comparing `delierium-0.9.0.dev6.dist-info/METADATA` & `delierium-0.9.0.dev9.dist-info/METADATA`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: delierium
-Version: 0.9.0.dev6
+Version: 0.9.0.dev9
 Summary: Symmetry Analysis for ODEs/PDEs using SageMath
 Home-page: UNKNOWN
 Author: Martin Mayerhofer-Schöpf
 Author-email: tapir@aon.at
 License: MIT
 Project-URL: Source, https://github.com/tapir442/delierium
 Keywords: ODE PDE Lie Symmetry
```

