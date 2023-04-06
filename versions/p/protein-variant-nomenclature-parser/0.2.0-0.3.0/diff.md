# Comparing `tmp/protein-variant-nomenclature-parser-0.2.0.tar.gz` & `tmp/protein-variant-nomenclature-parser-0.3.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "protein-variant-nomenclature-parser-0.2.0.tar", last modified: Tue Apr  4 18:12:32 2023, max compression
+gzip compressed data, was "protein-variant-nomenclature-parser-0.3.0.tar", last modified: Thu Apr  6 17:57:27 2023, max compression
```

## Comparing `protein-variant-nomenclature-parser-0.2.0.tar` & `protein-variant-nomenclature-parser-0.3.0.tar`

### file list

```diff
@@ -1,23 +1,23 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 18:12:32.436436 protein-variant-nomenclature-parser-0.2.0/
--rw-r--r--   0 root         (0) root         (0)     1067 2023-04-04 18:11:34.000000 protein-variant-nomenclature-parser-0.2.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     2754 2023-04-04 18:12:32.436436 protein-variant-nomenclature-parser-0.2.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2039 2023-04-04 18:11:34.000000 protein-variant-nomenclature-parser-0.2.0/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 18:12:32.428436 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-04 18:11:34.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 18:12:32.436436 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/generated/
--rw-r--r--   0 root         (0) root         (0)  3431883 2023-04-04 18:12:22.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/generated/HUGOLexer.py
--rw-r--r--   0 root         (0) root         (0)  3433357 2023-04-04 18:12:16.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/generated/ProteinVariantLexer.py
--rw-r--r--   0 root         (0) root         (0)     1999 2023-04-04 18:12:16.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/generated/ProteinVariantListener.py
--rw-r--r--   0 root         (0) root         (0)    11198 2023-04-04 18:12:16.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/generated/ProteinVariantParser.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-04 18:12:22.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/generated/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1898 2023-04-04 18:11:34.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/parser.py
--rw-r--r--   0 root         (0) root         (0)     1446 2023-04-04 18:11:34.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/test_parser.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-04 18:12:32.428436 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2754 2023-04-04 18:12:32.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      808 2023-04-04 18:12:32.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-04 18:12:32.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       33 2023-04-04 18:12:32.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       36 2023-04-04 18:12:32.000000 protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)      696 2023-04-04 18:11:34.000000 protein-variant-nomenclature-parser-0.2.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-04 18:12:32.436436 protein-variant-nomenclature-parser-0.2.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)      329 2023-04-04 18:11:34.000000 protein-variant-nomenclature-parser-0.2.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 17:57:27.630196 protein-variant-nomenclature-parser-0.3.0/
+-rw-r--r--   0 root         (0) root         (0)     1067 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     2754 2023-04-06 17:57:27.630196 protein-variant-nomenclature-parser-0.3.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2039 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 17:57:27.618196 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/__init__.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 17:57:27.630196 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/
+-rw-r--r--   0 root         (0) root         (0)  3582047 2023-04-06 17:57:18.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/HUGOLexer.py
+-rw-r--r--   0 root         (0) root         (0)  3590956 2023-04-06 17:57:15.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/ProteinVariantLexer.py
+-rw-r--r--   0 root         (0) root         (0)     1999 2023-04-06 17:57:15.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/ProteinVariantListener.py
+-rw-r--r--   0 root         (0) root         (0)    35246 2023-04-06 17:57:15.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/ProteinVariantParser.py
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 17:57:18.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/__init__.py
+-rw-r--r--   0 root         (0) root         (0)     1898 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/parser.py
+-rw-r--r--   0 root         (0) root         (0)     1450 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/test_parser.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 17:57:27.622196 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2754 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      808 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       33 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       36 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      696 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 17:57:27.634196 protein-variant-nomenclature-parser-0.3.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      329 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/setup.py
```

### Comparing `protein-variant-nomenclature-parser-0.2.0/LICENSE` & `protein-variant-nomenclature-parser-0.3.0/LICENSE`

 * *Files identical despite different names*

### Comparing `protein-variant-nomenclature-parser-0.2.0/PKG-INFO` & `protein-variant-nomenclature-parser-0.3.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: protein-variant-nomenclature-parser
-Version: 0.2.0
+Version: 0.3.0
 Summary: An ANTLR based parser for colloquial protein variant nomenclature
 Home-page: https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Author: Jeff Quinn
 Author-email: Jeff Quinn <quinnj2@mskcc.org>
 Project-URL: Homepage, https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Project-URL: Bug Tracker, https://github.com/tansey-lab/protein-variant-nomenclature-parser/issues
 Classifier: Programming Language :: Python :: 3
```

### Comparing `protein-variant-nomenclature-parser-0.2.0/README.md` & `protein-variant-nomenclature-parser-0.3.0/README.md`

 * *Files identical despite different names*

### Comparing `protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/generated/ProteinVariantListener.py` & `protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/ProteinVariantListener.py`

 * *Ordering differences only*

 * *Files 0% similar despite different names*

```diff
@@ -4,29 +4,29 @@
     from .ProteinVariantParser import ProteinVariantParser
 else:
     from ProteinVariantParser import ProteinVariantParser
 
 # This class defines a complete listener for a parse tree produced by ProteinVariantParser.
 class ProteinVariantListener(ParseTreeListener):
 
-    # Enter a parse tree produced by ProteinVariantParser#mutation.
-    def enterMutation(self, ctx:ProteinVariantParser.MutationContext):
+    # Enter a parse tree produced by ProteinVariantParser#gene.
+    def enterGene(self, ctx:ProteinVariantParser.GeneContext):
         pass
 
-    # Exit a parse tree produced by ProteinVariantParser#mutation.
-    def exitMutation(self, ctx:ProteinVariantParser.MutationContext):
+    # Exit a parse tree produced by ProteinVariantParser#gene.
+    def exitGene(self, ctx:ProteinVariantParser.GeneContext):
         pass
 
 
-    # Enter a parse tree produced by ProteinVariantParser#gene.
-    def enterGene(self, ctx:ProteinVariantParser.GeneContext):
+    # Enter a parse tree produced by ProteinVariantParser#mutation.
+    def enterMutation(self, ctx:ProteinVariantParser.MutationContext):
         pass
 
-    # Exit a parse tree produced by ProteinVariantParser#gene.
-    def exitGene(self, ctx:ProteinVariantParser.GeneContext):
+    # Exit a parse tree produced by ProteinVariantParser#mutation.
+    def exitMutation(self, ctx:ProteinVariantParser.MutationContext):
         pass
 
 
     # Enter a parse tree produced by ProteinVariantParser#number_or_range.
     def enterNumber_or_range(self, ctx:ProteinVariantParser.Number_or_rangeContext):
         pass
```

### Comparing `protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/parser.py` & `protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/parser.py`

 * *Files identical despite different names*

### Comparing `protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser/test_parser.py` & `protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/test_parser.py`

 * *Files 8% similar despite different names*

```diff
@@ -6,16 +6,16 @@
     ProteinVariant,
     NumberOrRange,
 )
 
 
 class TestParser(unittest.TestCase):
     def test_simple_mutation(self):
-        input_string = "BRAF V600E"
-        expected_output = ProteinVariant("BRAF", "V", NumberOrRange(600), "E")
+        input_string = "ZSWIM9 V600E"
+        expected_output = ProteinVariant("ZSWIM9", "V", NumberOrRange(600), "E")
         self.assertEqual(parse(input_string), expected_output)
 
     def test_simple_mutation_no_space(self):
         input_string = "BRAFV600E"
         expected_output = ProteinVariant("BRAF", "V", NumberOrRange(600), "E")
         self.assertEqual(parse(input_string), expected_output)
```

### Comparing `protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO` & `protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: protein-variant-nomenclature-parser
-Version: 0.2.0
+Version: 0.3.0
 Summary: An ANTLR based parser for colloquial protein variant nomenclature
 Home-page: https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Author: Jeff Quinn
 Author-email: Jeff Quinn <quinnj2@mskcc.org>
 Project-URL: Homepage, https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Project-URL: Bug Tracker, https://github.com/tansey-lab/protein-variant-nomenclature-parser/issues
 Classifier: Programming Language :: Python :: 3
```

### Comparing `protein-variant-nomenclature-parser-0.2.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt` & `protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `protein-variant-nomenclature-parser-0.2.0/pyproject.toml` & `protein-variant-nomenclature-parser-0.3.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "protein-variant-nomenclature-parser"
-version = "0.2.0"
+version = "0.3.0"
 authors = [
   { name="Jeff Quinn", email="quinnj2@mskcc.org" },
 ]
 description = "An ANTLR based parser for colloquial protein variant nomenclature"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

