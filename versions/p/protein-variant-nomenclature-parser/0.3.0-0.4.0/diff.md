# Comparing `tmp/protein-variant-nomenclature-parser-0.3.0.tar.gz` & `tmp/protein-variant-nomenclature-parser-0.4.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "protein-variant-nomenclature-parser-0.3.0.tar", last modified: Thu Apr  6 17:57:27 2023, max compression
+gzip compressed data, was "protein-variant-nomenclature-parser-0.4.0.tar", last modified: Thu Apr  6 18:54:01 2023, max compression
```

## Comparing `protein-variant-nomenclature-parser-0.3.0.tar` & `protein-variant-nomenclature-parser-0.4.0.tar`

### file list

```diff
@@ -1,23 +1,18 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 17:57:27.630196 protein-variant-nomenclature-parser-0.3.0/
--rw-r--r--   0 root         (0) root         (0)     1067 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     2754 2023-04-06 17:57:27.630196 protein-variant-nomenclature-parser-0.3.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2039 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 17:57:27.618196 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/__init__.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 17:57:27.630196 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/
--rw-r--r--   0 root         (0) root         (0)  3582047 2023-04-06 17:57:18.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/HUGOLexer.py
--rw-r--r--   0 root         (0) root         (0)  3590956 2023-04-06 17:57:15.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/ProteinVariantLexer.py
--rw-r--r--   0 root         (0) root         (0)     1999 2023-04-06 17:57:15.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/ProteinVariantListener.py
--rw-r--r--   0 root         (0) root         (0)    35246 2023-04-06 17:57:15.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/ProteinVariantParser.py
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 17:57:18.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/generated/__init__.py
--rw-r--r--   0 root         (0) root         (0)     1898 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/parser.py
--rw-r--r--   0 root         (0) root         (0)     1450 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/test_parser.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 17:57:27.622196 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2754 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      808 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       33 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       36 2023-04-06 17:57:27.000000 protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)      696 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 17:57:27.634196 protein-variant-nomenclature-parser-0.3.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)      329 2023-04-06 17:56:23.000000 protein-variant-nomenclature-parser-0.3.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 18:54:01.459484 protein-variant-nomenclature-parser-0.4.0/
+-rw-r--r--   0 root         (0) root         (0)     1067 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     2895 2023-04-06 18:54:01.459484 protein-variant-nomenclature-parser-0.4.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2180 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 18:54:01.455484 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   181180 2023-04-06 18:53:54.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/hugo.py
+-rw-r--r--   0 root         (0) root         (0)     1662 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/parser.py
+-rw-r--r--   0 root         (0) root         (0)     2175 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/test_parser.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 18:54:01.459484 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2895 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      524 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       33 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/requires.txt
+-rw-r--r--   0 root         (0) root         (0)       36 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      696 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 18:54:01.459484 protein-variant-nomenclature-parser-0.4.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      329 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/setup.py
```

### Comparing `protein-variant-nomenclature-parser-0.3.0/LICENSE` & `protein-variant-nomenclature-parser-0.4.0/LICENSE`

 * *Files identical despite different names*

### Comparing `protein-variant-nomenclature-parser-0.3.0/PKG-INFO` & `protein-variant-nomenclature-parser-0.4.0/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: protein-variant-nomenclature-parser
-Version: 0.3.0
+Version: 0.4.0
 Summary: An ANTLR based parser for colloquial protein variant nomenclature
 Home-page: https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Author: Jeff Quinn
 Author-email: Jeff Quinn <quinnj2@mskcc.org>
 Project-URL: Homepage, https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Project-URL: Bug Tracker, https://github.com/tansey-lab/protein-variant-nomenclature-parser/issues
 Classifier: Programming Language :: Python :: 3
@@ -18,15 +18,15 @@
 
 This repository contains a Python library for parsing and validating colloquial protein variant nomenclature
 strings like `BRAF V600E` that commonly appear in manuscripts.
 
 ## Features
 
 - Parse protein variant nomenclature strings in the following formats:
-  - Single amino acid substitution, e.g.: `BRAF V600E`, `BRAFV600E`, `PTEN R130G`, `TP53 R175H`
+  - Single amino acid substitution, e.g.: `BRAF V600E`, `BRAFV600E`, `BRAFᵛ⁶⁰⁰ᵉ`
   - Range of amino acid substitutions: `BRAFVK600_601>E`
 - Extract the components of the nomenclature string, such as gene name, prefix amino acid, position or range, and suffix amino acid
 - Validate whether a given string conforms to the expected format
 
 ## Usage
 
 For parsing:
@@ -61,14 +61,17 @@
 
 ## Supported Nomenclature
 
 The parser supports all HUGO gene names.
 
 The parser supports the following amino acid single letter codes and stop codon (*).
 
+The parser supports situations where the variant has no space between the gene name in the substitution,
+which unfortunately comes up sometimes.
+
 ## Installation
 
 ### From PyPI
 
 ```bash
 pip install protein-variant-nomenclature-parser
 ```
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `protein-variant-nomenclature-parser-0.3.0/README.md` & `protein-variant-nomenclature-parser-0.4.0/README.md`

 * *Files 8% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 
 This repository contains a Python library for parsing and validating colloquial protein variant nomenclature
 strings like `BRAF V600E` that commonly appear in manuscripts.
 
 ## Features
 
 - Parse protein variant nomenclature strings in the following formats:
-  - Single amino acid substitution, e.g.: `BRAF V600E`, `BRAFV600E`, `PTEN R130G`, `TP53 R175H`
+  - Single amino acid substitution, e.g.: `BRAF V600E`, `BRAFV600E`, `BRAFᵛ⁶⁰⁰ᵉ`
   - Range of amino acid substitutions: `BRAFVK600_601>E`
 - Extract the components of the nomenclature string, such as gene name, prefix amino acid, position or range, and suffix amino acid
 - Validate whether a given string conforms to the expected format
 
 ## Usage
 
 For parsing:
@@ -45,14 +45,17 @@
 
 ## Supported Nomenclature
 
 The parser supports all HUGO gene names.
 
 The parser supports the following amino acid single letter codes and stop codon (*).
 
+The parser supports situations where the variant has no space between the gene name in the substitution,
+which unfortunately comes up sometimes.
+
 ## Installation
 
 ### From PyPI
 
 ```bash
 pip install protein-variant-nomenclature-parser
 ```
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser/test_parser.py` & `protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/test_parser.py`

 * *Files 6% similar despite different names*

```diff
@@ -1,28 +1,43 @@
 import unittest
 from protein_variant_nomenclature_parser.parser import (
-    parse_ProteinVariant_string,
     InvalidProteinVariantError,
     parse,
     ProteinVariant,
     NumberOrRange,
 )
 
 
 class TestParser(unittest.TestCase):
-    def test_simple_mutation(self):
+    def test_simple_mutation_with_space(self):
         input_string = "ZSWIM9 V600E"
         expected_output = ProteinVariant("ZSWIM9", "V", NumberOrRange(600), "E")
         self.assertEqual(parse(input_string), expected_output)
 
     def test_simple_mutation_no_space(self):
         input_string = "BRAFV600E"
         expected_output = ProteinVariant("BRAF", "V", NumberOrRange(600), "E")
         self.assertEqual(parse(input_string), expected_output)
 
+    def test_ambiguous_hugo_prefix(self):
+        # This is an ambiguous one if there's not any whitespace, we should
+        # handle this in the future
+        input_string = "CGA SS600E"
+        expected_output = ProteinVariant("CGA", "SS", NumberOrRange(600), "E")
+        self.assertEqual(parse(input_string), expected_output)
+
+        input_string = "CGASS600E"
+        expected_output = ProteinVariant("CGAS", "S", NumberOrRange(600), "E")
+        self.assertEqual(parse(input_string), expected_output)
+
+    def test_simple_mutation_superscript(self):
+        input_string = "BRAFᵛ⁶⁰⁰ᵉ"
+        expected_output = ProteinVariant("BRAF", "V", NumberOrRange(600), "E")
+        self.assertEqual(parse(input_string), expected_output)
+
     def test_range_mutation(self):
         input_string = "BRAFVK600_601>E"
         expected_output = ProteinVariant("BRAF", "VK", NumberOrRange(600, 601), "E")
 
         self.assertEqual(parse(input_string), expected_output)
 
     def test_invalid_mutation(self):
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO` & `protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: protein-variant-nomenclature-parser
-Version: 0.3.0
+Version: 0.4.0
 Summary: An ANTLR based parser for colloquial protein variant nomenclature
 Home-page: https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Author: Jeff Quinn
 Author-email: Jeff Quinn <quinnj2@mskcc.org>
 Project-URL: Homepage, https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Project-URL: Bug Tracker, https://github.com/tansey-lab/protein-variant-nomenclature-parser/issues
 Classifier: Programming Language :: Python :: 3
@@ -18,15 +18,15 @@
 
 This repository contains a Python library for parsing and validating colloquial protein variant nomenclature
 strings like `BRAF V600E` that commonly appear in manuscripts.
 
 ## Features
 
 - Parse protein variant nomenclature strings in the following formats:
-  - Single amino acid substitution, e.g.: `BRAF V600E`, `BRAFV600E`, `PTEN R130G`, `TP53 R175H`
+  - Single amino acid substitution, e.g.: `BRAF V600E`, `BRAFV600E`, `BRAFᵛ⁶⁰⁰ᵉ`
   - Range of amino acid substitutions: `BRAFVK600_601>E`
 - Extract the components of the nomenclature string, such as gene name, prefix amino acid, position or range, and suffix amino acid
 - Validate whether a given string conforms to the expected format
 
 ## Usage
 
 For parsing:
@@ -61,14 +61,17 @@
 
 ## Supported Nomenclature
 
 The parser supports all HUGO gene names.
 
 The parser supports the following amino acid single letter codes and stop codon (*).
 
+The parser supports situations where the variant has no space between the gene name in the substitution,
+which unfortunately comes up sometimes.
+
 ## Installation
 
 ### From PyPI
 
 ```bash
 pip install protein-variant-nomenclature-parser
 ```
```

#### encoding

```diff
@@ -1 +1 @@
-us-ascii
+utf-8
```

### Comparing `protein-variant-nomenclature-parser-0.3.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt` & `protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt`

 * *Files 21% similar despite different names*

```diff
@@ -1,17 +1,13 @@
 LICENSE
 README.md
 pyproject.toml
 setup.py
 protein_variant_nomenclature_parser/__init__.py
+protein_variant_nomenclature_parser/hugo.py
 protein_variant_nomenclature_parser/parser.py
 protein_variant_nomenclature_parser/test_parser.py
 protein_variant_nomenclature_parser.egg-info/PKG-INFO
 protein_variant_nomenclature_parser.egg-info/SOURCES.txt
 protein_variant_nomenclature_parser.egg-info/dependency_links.txt
 protein_variant_nomenclature_parser.egg-info/requires.txt
-protein_variant_nomenclature_parser.egg-info/top_level.txt
-protein_variant_nomenclature_parser/generated/HUGOLexer.py
-protein_variant_nomenclature_parser/generated/ProteinVariantLexer.py
-protein_variant_nomenclature_parser/generated/ProteinVariantListener.py
-protein_variant_nomenclature_parser/generated/ProteinVariantParser.py
-protein_variant_nomenclature_parser/generated/__init__.py
+protein_variant_nomenclature_parser.egg-info/top_level.txt
```

### Comparing `protein-variant-nomenclature-parser-0.3.0/pyproject.toml` & `protein-variant-nomenclature-parser-0.4.0/pyproject.toml`

 * *Files 1% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "protein-variant-nomenclature-parser"
-version = "0.3.0"
+version = "0.4.0"
 authors = [
   { name="Jeff Quinn", email="quinnj2@mskcc.org" },
 ]
 description = "An ANTLR based parser for colloquial protein variant nomenclature"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

