# Comparing `tmp/uplc-0.6.1.tar.gz` & `tmp/uplc-0.6.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "uplc-0.6.1.tar", last modified: Fri Mar 31 13:07:42 2023, max compression
+gzip compressed data, was "uplc-0.6.2.tar", last modified: Thu Apr  6 19:25:25 2023, max compression
```

## Comparing `uplc-0.6.1.tar` & `uplc-0.6.2.tar`

### file list

```diff
@@ -1,37 +1,37 @@
-drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-03-31 13:07:42.772958 uplc-0.6.1/
--rw-r--r--   0 travis    (1000) travis    (1000)     1077 2023-03-31 13:00:10.000000 uplc-0.6.1/LICENSE.txt
--rw-r--r--   0 travis    (1000) travis    (1000)     2807 2023-03-31 13:07:42.772958 uplc-0.6.1/PKG-INFO
--rw-r--r--   0 travis    (1000) travis    (1000)     2034 2023-03-31 13:00:10.000000 uplc-0.6.1/README.md
--rw-r--r--   0 travis    (1000) travis    (1000)       38 2023-03-31 13:07:42.772958 uplc-0.6.1/setup.cfg
--rw-r--r--   0 travis    (1000) travis    (1000)     2056 2023-03-31 13:00:10.000000 uplc-0.6.1/setup.py
-drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-03-31 13:07:42.764958 uplc-0.6.1/uplc/
--rw-r--r--   0 travis    (1000) travis    (1000)      555 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/__init__.py
--rw-r--r--   0 travis    (1000) travis    (1000)     4935 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/__main__.py
--rw-r--r--   0 travis    (1000) travis    (1000)    26560 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/ast.py
--rw-r--r--   0 travis    (1000) travis    (1000)     9066 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/flat_decoder.py
--rw-r--r--   0 travis    (1000) travis    (1000)    10052 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/flat_encoder.py
--rw-r--r--   0 travis    (1000) travis    (1000)     1202 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/lexer.py
--rw-r--r--   0 travis    (1000) travis    (1000)     3357 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/machine.py
-drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-03-31 13:07:42.768958 uplc-0.6.1/uplc/optimizer/
--rw-r--r--   0 travis    (1000) travis    (1000)        0 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/optimizer/__init__.py
--rw-r--r--   0 travis    (1000) travis    (1000)      653 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/optimizer/pre_evaluation.py
--rw-r--r--   0 travis    (1000) travis    (1000)    10960 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/parser.py
-drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-03-31 13:07:42.768958 uplc-0.6.1/uplc/tests/
--rw-r--r--   0 travis    (1000) travis    (1000)        0 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/tests/__init__.py
--rw-r--r--   0 travis    (1000) travis    (1000)     3391 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/tests/test_acceptance.py
--rw-r--r--   0 travis    (1000) travis    (1000)    13614 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/tests/test_hypothesis.py
--rw-r--r--   0 travis    (1000) travis    (1000)   211128 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/tests/test_misc.py
--rw-r--r--   0 travis    (1000) travis    (1000)     2094 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/tools.py
-drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-03-31 13:07:42.772958 uplc-0.6.1/uplc/transformer/
--rw-r--r--   0 travis    (1000) travis    (1000)        0 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/transformer/__init__.py
--rw-r--r--   0 travis    (1000) travis    (1000)      784 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/transformer/debrujin_variables.py
--rw-r--r--   0 travis    (1000) travis    (1000)      938 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/transformer/undebrujin_variables.py
--rw-r--r--   0 travis    (1000) travis    (1000)     1643 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/transformer/unique_variables.py
--rw-r--r--   0 travis    (1000) travis    (1000)     2961 2023-03-31 13:00:10.000000 uplc-0.6.1/uplc/util.py
-drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-03-31 13:07:42.768958 uplc-0.6.1/uplc.egg-info/
--rw-r--r--   0 travis    (1000) travis    (1000)     2807 2023-03-31 13:07:42.000000 uplc-0.6.1/uplc.egg-info/PKG-INFO
--rw-r--r--   0 travis    (1000) travis    (1000)      673 2023-03-31 13:07:42.000000 uplc-0.6.1/uplc.egg-info/SOURCES.txt
--rw-r--r--   0 travis    (1000) travis    (1000)        1 2023-03-31 13:07:42.000000 uplc-0.6.1/uplc.egg-info/dependency_links.txt
--rw-r--r--   0 travis    (1000) travis    (1000)       44 2023-03-31 13:07:42.000000 uplc-0.6.1/uplc.egg-info/entry_points.txt
--rw-r--r--   0 travis    (1000) travis    (1000)      110 2023-03-31 13:07:42.000000 uplc-0.6.1/uplc.egg-info/requires.txt
--rw-r--r--   0 travis    (1000) travis    (1000)        5 2023-03-31 13:07:42.000000 uplc-0.6.1/uplc.egg-info/top_level.txt
+drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-04-06 19:25:25.615665 uplc-0.6.2/
+-rw-r--r--   0 travis    (1000) travis    (1000)     1077 2023-04-06 19:17:37.000000 uplc-0.6.2/LICENSE.txt
+-rw-r--r--   0 travis    (1000) travis    (1000)     2807 2023-04-06 19:25:25.615665 uplc-0.6.2/PKG-INFO
+-rw-r--r--   0 travis    (1000) travis    (1000)     2034 2023-04-06 19:17:37.000000 uplc-0.6.2/README.md
+-rw-r--r--   0 travis    (1000) travis    (1000)       38 2023-04-06 19:25:25.615665 uplc-0.6.2/setup.cfg
+-rw-r--r--   0 travis    (1000) travis    (1000)     2056 2023-04-06 19:17:37.000000 uplc-0.6.2/setup.py
+drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-04-06 19:25:25.607665 uplc-0.6.2/uplc/
+-rw-r--r--   0 travis    (1000) travis    (1000)      555 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/__init__.py
+-rw-r--r--   0 travis    (1000) travis    (1000)     4935 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/__main__.py
+-rw-r--r--   0 travis    (1000) travis    (1000)    26560 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/ast.py
+-rw-r--r--   0 travis    (1000) travis    (1000)     9066 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/flat_decoder.py
+-rw-r--r--   0 travis    (1000) travis    (1000)    10052 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/flat_encoder.py
+-rw-r--r--   0 travis    (1000) travis    (1000)     1202 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/lexer.py
+-rw-r--r--   0 travis    (1000) travis    (1000)     3357 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/machine.py
+drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-04-06 19:25:25.611665 uplc-0.6.2/uplc/optimizer/
+-rw-r--r--   0 travis    (1000) travis    (1000)        0 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/optimizer/__init__.py
+-rw-r--r--   0 travis    (1000) travis    (1000)      630 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/optimizer/pre_evaluation.py
+-rw-r--r--   0 travis    (1000) travis    (1000)    10960 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/parser.py
+drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-04-06 19:25:25.615665 uplc-0.6.2/uplc/tests/
+-rw-r--r--   0 travis    (1000) travis    (1000)        0 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/tests/__init__.py
+-rw-r--r--   0 travis    (1000) travis    (1000)     3391 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/tests/test_acceptance.py
+-rw-r--r--   0 travis    (1000) travis    (1000)    13912 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/tests/test_hypothesis.py
+-rw-r--r--   0 travis    (1000) travis    (1000)   211128 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/tests/test_misc.py
+-rw-r--r--   0 travis    (1000) travis    (1000)     1998 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/tools.py
+drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-04-06 19:25:25.615665 uplc-0.6.2/uplc/transformer/
+-rw-r--r--   0 travis    (1000) travis    (1000)        0 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/transformer/__init__.py
+-rw-r--r--   0 travis    (1000) travis    (1000)      784 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/transformer/debrujin_variables.py
+-rw-r--r--   0 travis    (1000) travis    (1000)      938 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/transformer/undebrujin_variables.py
+-rw-r--r--   0 travis    (1000) travis    (1000)     1815 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/transformer/unique_variables.py
+-rw-r--r--   0 travis    (1000) travis    (1000)     3009 2023-04-06 19:17:37.000000 uplc-0.6.2/uplc/util.py
+drwxr-xr-x   0 travis    (1000) travis    (1000)        0 2023-04-06 19:25:25.611665 uplc-0.6.2/uplc.egg-info/
+-rw-r--r--   0 travis    (1000) travis    (1000)     2807 2023-04-06 19:25:25.000000 uplc-0.6.2/uplc.egg-info/PKG-INFO
+-rw-r--r--   0 travis    (1000) travis    (1000)      673 2023-04-06 19:25:25.000000 uplc-0.6.2/uplc.egg-info/SOURCES.txt
+-rw-r--r--   0 travis    (1000) travis    (1000)        1 2023-04-06 19:25:25.000000 uplc-0.6.2/uplc.egg-info/dependency_links.txt
+-rw-r--r--   0 travis    (1000) travis    (1000)       44 2023-04-06 19:25:25.000000 uplc-0.6.2/uplc.egg-info/entry_points.txt
+-rw-r--r--   0 travis    (1000) travis    (1000)      110 2023-04-06 19:25:25.000000 uplc-0.6.2/uplc.egg-info/requires.txt
+-rw-r--r--   0 travis    (1000) travis    (1000)        5 2023-04-06 19:25:25.000000 uplc-0.6.2/uplc.egg-info/top_level.txt
```

### Comparing `uplc-0.6.1/LICENSE.txt` & `uplc-0.6.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/PKG-INFO` & `uplc-0.6.2/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: uplc
-Version: 0.6.1
+Version: 0.6.2
 Summary: Python implementation of untyped plutus language core
 Home-page: https://github.com/opshin/uplc
 Author: nielstron
 Author-email: n.muendler@web.de
 License: MIT
 Keywords: python cardano smart contract blockchain verification haskell
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `uplc-0.6.1/README.md` & `uplc-0.6.2/README.md`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/setup.py` & `uplc-0.6.2/setup.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/__init__.py` & `uplc-0.6.2/uplc/__init__.py`

 * *Files 21% similar despite different names*

```diff
@@ -1,15 +1,15 @@
 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
 
 
 import logging
 
 
-VERSION = (0, 6, 1)
+VERSION = (0, 6, 2)
 
 __version__ = ".".join([str(i) for i in VERSION])
 __author__ = "nielstron"
 __author_email__ = "n.muendler@web.de"
 __copyright__ = "Copyright (C) 2023 nielstron"
 __license__ = "MIT"
 __url__ = "https://github.com/opshin/uplc"
```

### Comparing `uplc-0.6.1/uplc/__main__.py` & `uplc-0.6.2/uplc/__main__.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/ast.py` & `uplc-0.6.2/uplc/ast.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/flat_decoder.py` & `uplc-0.6.2/uplc/flat_decoder.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/flat_encoder.py` & `uplc-0.6.2/uplc/flat_encoder.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/lexer.py` & `uplc-0.6.2/uplc/lexer.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/machine.py` & `uplc-0.6.2/uplc/machine.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/optimizer/pre_evaluation.py` & `uplc-0.6.2/uplc/optimizer/pre_evaluation.py`

 * *Files 19% similar despite different names*

```diff
@@ -1,9 +1,7 @@
-from copy import copy
-
 from ..util import NodeTransformer
 from ..ast import Program, AST
 from ..machine import Machine
 
 """
 Optimizes code by pre-evaluating each subterm
 If it throws an error, assume it is not safe to pre-evaluate and don't replace, otherwise replace by result.
```

### Comparing `uplc-0.6.1/uplc/parser.py` & `uplc-0.6.2/uplc/parser.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/tests/test_acceptance.py` & `uplc-0.6.2/uplc/tests/test_acceptance.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/tests/test_hypothesis.py` & `uplc-0.6.2/uplc/tests/test_hypothesis.py`

 * *Files 2% similar despite different names*

```diff
@@ -199,37 +199,45 @@
         UPLCDialect.Aiken,
     )
     def test_dumps_parse_roundtrip(self, p, dialect):
         self.assertEqual(parse(dumps(p, dialect)), p)
 
     @hypothesis.given(uplc_program)
     @hypothesis.settings(max_examples=1000, deadline=datetime.timedelta(seconds=10))
+    @hypothesis.example(
+        parse("(program 0.0.0 [(force (builtin mkCons)) (lam _ (error))])")
+    )
+    @hypothesis.example(
+        parse("(program 0.0.0 (lam _ [(builtin mkPairData) (lam ' _)]))")
+    )
     @hypothesis.example(parse("(program 0.0.0 (lam _ _))"))
     @hypothesis.example(parse("(program 0.0.0 [(lam x0 (lam _ x0)) (con integer 0)])"))
     @hypothesis.example(parse("(program 0.0.0 [(lam _ (delay _)) (con integer 0)])"))
     @hypothesis.example(parse("(program 0.0.0 (lam _ '))"))
     @hypothesis.example(parse("(program 0.0.0 (delay _))"))
     def test_rewrite_no_semantic_change(self, p):
         code = dumps(p)
         try:
-            rewrite_p = unique_variables.UniqueVariableTransformer().visit(p)
+            rewrite_p = unique_variables.UniqueVariableTransformer().visit(parse(code))
         except unique_variables.FreeVariableError:
             return
         try:
             res = eval(p)
             res = unique_variables.UniqueVariableTransformer().visit(res)
+            res = res.dumps()
         except unique_variables.FreeVariableError:
             self.fail(f"Free variable error occurred after evaluation in {code}")
         except Exception as e:
             res = e.__class__
         try:
             rewrite_res = eval(rewrite_p)
             rewrite_res = unique_variables.UniqueVariableTransformer().visit(
                 rewrite_res
             )
+            rewrite_res = rewrite_res.dumps()
         except unique_variables.FreeVariableError:
             self.fail(f"Free variable error occurred after evaluation in {code}")
         except Exception as e:
             rewrite_res = e.__class__
         self.assertEqual(
             res,
             rewrite_res,
```

### Comparing `uplc-0.6.1/uplc/tests/test_misc.py` & `uplc-0.6.2/uplc/tests/test_misc.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/tools.py` & `uplc-0.6.2/uplc/tools.py`

 * *Files 16% similar despite different names*

```diff
@@ -1,26 +1,23 @@
-import copy
-
 import cbor2
 import rply.errors
 
 from .lexer import strip_comments, Lexer
 from .parser import Parser
 from .machine import Machine
 from .ast import AST, UPLCDialect, Program, plutus_cbor_dumps, PlutusByteString
 from .flat_encoder import FlatEncodingVisitor
 from .flat_decoder import UplcDeserializer
 from .transformer.debrujin_variables import DeBrujinVariableTransformer
 from .transformer.undebrujin_variables import UnDeBrujinVariableTransformer
-from .transformer.unique_variables import UniqueVariableTransformer
 
 
 def flatten(x: Program) -> bytes:
     """Returns the properly CBOR wrapped program"""
-    x_debrujin = DeBrujinVariableTransformer().visit(copy.deepcopy(x))
+    x_debrujin = DeBrujinVariableTransformer().visit(x)
     flattener = FlatEncodingVisitor()
     flattener.visit(x_debrujin)
     x_flattened = flattener.bit_writer.finalize()
     return cbor2.dumps(x_flattened)
 
 
 def unflatten(x_cbor: bytes) -> Program:
```

### Comparing `uplc-0.6.1/uplc/transformer/debrujin_variables.py` & `uplc-0.6.2/uplc/transformer/debrujin_variables.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/transformer/undebrujin_variables.py` & `uplc-0.6.2/uplc/transformer/undebrujin_variables.py`

 * *Files identical despite different names*

### Comparing `uplc-0.6.1/uplc/transformer/unique_variables.py` & `uplc-0.6.2/uplc/transformer/unique_variables.py`

 * *Files 12% similar despite different names*

```diff
@@ -51,11 +51,16 @@
             self.push_map(k)
         nc = copy(node)
         nc.term = self.visit(node.term)
         for _ in node.state.keys():
             self.pop_map()
         return nc
 
+    def visit_ForcedBuiltIn(self, node: ForcedBuiltIn):
+        nc = copy(node)
+        nc.bound_arguments = [self.visit(a) for a in nc.bound_arguments]
+        return nc
+
     def visit_Variable(self, node: Variable):
         nc = copy(node)
         nc.name = self.get_map(node.name)
         return nc
```

### Comparing `uplc-0.6.1/uplc/util.py` & `uplc-0.6.2/uplc/util.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,8 +1,9 @@
 from ast import iter_fields
+from copy import copy
 
 
 class NodeVisitor(object):
     """
     A node visitor base class that walks the abstract syntax tree and calls a
     visitor function for every node found.  This function may return a value
     which is forwarded by the `visit` method.
@@ -66,14 +67,15 @@
 
     Usually you use the transformer like this::
 
        node = YourTransformer().visit(node)
     """
 
     def generic_visit(self, node):
+        node = copy(node)
         for field, old_value in iter_fields(node):
             new_node = self.visit(old_value)
             if new_node is None:
                 delattr(node, field)
             else:
                 setattr(node, field, new_node)
         return node
```

### Comparing `uplc-0.6.1/uplc.egg-info/PKG-INFO` & `uplc-0.6.2/uplc.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: uplc
-Version: 0.6.1
+Version: 0.6.2
 Summary: Python implementation of untyped plutus language core
 Home-page: https://github.com/opshin/uplc
 Author: nielstron
 Author-email: n.muendler@web.de
 License: MIT
 Keywords: python cardano smart contract blockchain verification haskell
 Classifier: Development Status :: 3 - Alpha
```

### Comparing `uplc-0.6.1/uplc.egg-info/SOURCES.txt` & `uplc-0.6.2/uplc.egg-info/SOURCES.txt`

 * *Files identical despite different names*

