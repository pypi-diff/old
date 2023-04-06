# Comparing `tmp/protein-variant-nomenclature-parser-0.4.0.tar.gz` & `tmp/protein-variant-nomenclature-parser-0.5.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "protein-variant-nomenclature-parser-0.4.0.tar", last modified: Thu Apr  6 18:54:01 2023, max compression
+gzip compressed data, was "protein-variant-nomenclature-parser-0.5.0.tar", last modified: Thu Apr  6 19:18:04 2023, max compression
```

## Comparing `protein-variant-nomenclature-parser-0.4.0.tar` & `protein-variant-nomenclature-parser-0.5.0.tar`

### file list

```diff
@@ -1,18 +1,17 @@
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 18:54:01.459484 protein-variant-nomenclature-parser-0.4.0/
--rw-r--r--   0 root         (0) root         (0)     1067 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/LICENSE
--rw-r--r--   0 root         (0) root         (0)     2895 2023-04-06 18:54:01.459484 protein-variant-nomenclature-parser-0.4.0/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)     2180 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/README.md
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 18:54:01.455484 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/
--rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/__init__.py
--rw-r--r--   0 root         (0) root         (0)   181180 2023-04-06 18:53:54.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/hugo.py
--rw-r--r--   0 root         (0) root         (0)     1662 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/parser.py
--rw-r--r--   0 root         (0) root         (0)     2175 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/test_parser.py
-drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 18:54:01.459484 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/
--rw-r--r--   0 root         (0) root         (0)     2895 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO
--rw-r--r--   0 root         (0) root         (0)      524 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt
--rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/dependency_links.txt
--rw-r--r--   0 root         (0) root         (0)       33 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/requires.txt
--rw-r--r--   0 root         (0) root         (0)       36 2023-04-06 18:54:01.000000 protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/top_level.txt
--rw-r--r--   0 root         (0) root         (0)      696 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/pyproject.toml
--rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 18:54:01.459484 protein-variant-nomenclature-parser-0.4.0/setup.cfg
--rw-r--r--   0 root         (0) root         (0)      329 2023-04-06 18:53:20.000000 protein-variant-nomenclature-parser-0.4.0/setup.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:18:04.959274 protein-variant-nomenclature-parser-0.5.0/
+-rw-r--r--   0 root         (0) root         (0)     1067 2023-04-06 19:17:31.000000 protein-variant-nomenclature-parser-0.5.0/LICENSE
+-rw-r--r--   0 root         (0) root         (0)     2942 2023-04-06 19:18:04.959274 protein-variant-nomenclature-parser-0.5.0/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)     2227 2023-04-06 19:17:31.000000 protein-variant-nomenclature-parser-0.5.0/README.md
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:18:04.955274 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser/
+-rw-r--r--   0 root         (0) root         (0)        0 2023-04-06 19:17:31.000000 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser/__init__.py
+-rw-r--r--   0 root         (0) root         (0)   181180 2023-04-06 19:17:56.000000 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser/hugo.py
+-rw-r--r--   0 root         (0) root         (0)     1662 2023-04-06 19:17:31.000000 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser/parser.py
+-rw-r--r--   0 root         (0) root         (0)     2175 2023-04-06 19:17:31.000000 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser/test_parser.py
+drwxr-xr-x   0 root         (0) root         (0)        0 2023-04-06 19:18:04.959274 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser.egg-info/
+-rw-r--r--   0 root         (0) root         (0)     2942 2023-04-06 19:18:04.000000 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO
+-rw-r--r--   0 root         (0) root         (0)      466 2023-04-06 19:18:04.000000 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser.egg-info/SOURCES.txt
+-rw-r--r--   0 root         (0) root         (0)        1 2023-04-06 19:18:04.000000 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser.egg-info/dependency_links.txt
+-rw-r--r--   0 root         (0) root         (0)       36 2023-04-06 19:18:04.000000 protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser.egg-info/top_level.txt
+-rw-r--r--   0 root         (0) root         (0)      696 2023-04-06 19:17:31.000000 protein-variant-nomenclature-parser-0.5.0/pyproject.toml
+-rw-r--r--   0 root         (0) root         (0)       38 2023-04-06 19:18:04.959274 protein-variant-nomenclature-parser-0.5.0/setup.cfg
+-rw-r--r--   0 root         (0) root         (0)      280 2023-04-06 19:17:31.000000 protein-variant-nomenclature-parser-0.5.0/setup.py
```

### Comparing `protein-variant-nomenclature-parser-0.4.0/LICENSE` & `protein-variant-nomenclature-parser-0.5.0/LICENSE`

 * *Files identical despite different names*

### Comparing `protein-variant-nomenclature-parser-0.4.0/PKG-INFO` & `protein-variant-nomenclature-parser-0.5.0/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: protein-variant-nomenclature-parser
-Version: 0.4.0
+Version: 0.5.0
 Summary: An ANTLR based parser for colloquial protein variant nomenclature
 Home-page: https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Author: Jeff Quinn
 Author-email: Jeff Quinn <quinnj2@mskcc.org>
 Project-URL: Homepage, https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Project-URL: Bug Tracker, https://github.com/tansey-lab/protein-variant-nomenclature-parser/issues
 Classifier: Programming Language :: Python :: 3
@@ -22,14 +22,15 @@
 ## Features
 
 - Parse protein variant nomenclature strings in the following formats:
   - Single amino acid substitution, e.g.: `BRAF V600E`, `BRAFV600E`, `BRAFᵛ⁶⁰⁰ᵉ`
   - Range of amino acid substitutions: `BRAFVK600_601>E`
 - Extract the components of the nomenclature string, such as gene name, prefix amino acid, position or range, and suffix amino acid
 - Validate whether a given string conforms to the expected format
+- Pure python with zero dependencies and no dependency on an internet connection
 
 ## Usage
 
 For parsing:
 
 ```python
 from protein_variant_nomenclature_parser.parser import parse
@@ -37,15 +38,15 @@
 mutation_string = "BRAF V600E"
 parsed_components = parse(mutation_string)
 
 print(parsed_components)
 ```
 
 ```
-ProteinVariant(gene='BRAF', amino_acid_before='V', number_or_range=NumberOrRange(start=600, end=None), amino_acid_after='E')
+ProteinVariant(gene='BRAF', ref='V', position=NumberOrRange(start=600, end=None), alt='E')
 ```
 
 For validation:
 
 ```python
 from protein_variant_nomenclature_parser.parser import parse
 from protein_variant_nomenclature_parser.parser import InvalidProteinVariantError
```

### Comparing `protein-variant-nomenclature-parser-0.4.0/README.md` & `protein-variant-nomenclature-parser-0.5.0/README.md`

 * *Files 5% similar despite different names*

```diff
@@ -6,14 +6,15 @@
 ## Features
 
 - Parse protein variant nomenclature strings in the following formats:
   - Single amino acid substitution, e.g.: `BRAF V600E`, `BRAFV600E`, `BRAFᵛ⁶⁰⁰ᵉ`
   - Range of amino acid substitutions: `BRAFVK600_601>E`
 - Extract the components of the nomenclature string, such as gene name, prefix amino acid, position or range, and suffix amino acid
 - Validate whether a given string conforms to the expected format
+- Pure python with zero dependencies and no dependency on an internet connection
 
 ## Usage
 
 For parsing:
 
 ```python
 from protein_variant_nomenclature_parser.parser import parse
@@ -21,15 +22,15 @@
 mutation_string = "BRAF V600E"
 parsed_components = parse(mutation_string)
 
 print(parsed_components)
 ```
 
 ```
-ProteinVariant(gene='BRAF', amino_acid_before='V', number_or_range=NumberOrRange(start=600, end=None), amino_acid_after='E')
+ProteinVariant(gene='BRAF', ref='V', position=NumberOrRange(start=600, end=None), alt='E')
 ```
 
 For validation:
 
 ```python
 from protein_variant_nomenclature_parser.parser import parse
 from protein_variant_nomenclature_parser.parser import InvalidProteinVariantError
```

### Comparing `protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/hugo.py` & `protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser/hugo.py`

 * *Files identical despite different names*

### Comparing `protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/parser.py` & `protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser/parser.py`

 * *Files identical despite different names*

### Comparing `protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser/test_parser.py` & `protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser/test_parser.py`

 * *Files identical despite different names*

### Comparing `protein-variant-nomenclature-parser-0.4.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO` & `protein-variant-nomenclature-parser-0.5.0/protein_variant_nomenclature_parser.egg-info/PKG-INFO`

 * *Files 6% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: protein-variant-nomenclature-parser
-Version: 0.4.0
+Version: 0.5.0
 Summary: An ANTLR based parser for colloquial protein variant nomenclature
 Home-page: https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Author: Jeff Quinn
 Author-email: Jeff Quinn <quinnj2@mskcc.org>
 Project-URL: Homepage, https://github.com/tansey-lab/protein-variant-nomenclature-parser
 Project-URL: Bug Tracker, https://github.com/tansey-lab/protein-variant-nomenclature-parser/issues
 Classifier: Programming Language :: Python :: 3
@@ -22,14 +22,15 @@
 ## Features
 
 - Parse protein variant nomenclature strings in the following formats:
   - Single amino acid substitution, e.g.: `BRAF V600E`, `BRAFV600E`, `BRAFᵛ⁶⁰⁰ᵉ`
   - Range of amino acid substitutions: `BRAFVK600_601>E`
 - Extract the components of the nomenclature string, such as gene name, prefix amino acid, position or range, and suffix amino acid
 - Validate whether a given string conforms to the expected format
+- Pure python with zero dependencies and no dependency on an internet connection
 
 ## Usage
 
 For parsing:
 
 ```python
 from protein_variant_nomenclature_parser.parser import parse
@@ -37,15 +38,15 @@
 mutation_string = "BRAF V600E"
 parsed_components = parse(mutation_string)
 
 print(parsed_components)
 ```
 
 ```
-ProteinVariant(gene='BRAF', amino_acid_before='V', number_or_range=NumberOrRange(start=600, end=None), amino_acid_after='E')
+ProteinVariant(gene='BRAF', ref='V', position=NumberOrRange(start=600, end=None), alt='E')
 ```
 
 For validation:
 
 ```python
 from protein_variant_nomenclature_parser.parser import parse
 from protein_variant_nomenclature_parser.parser import InvalidProteinVariantError
```

### Comparing `protein-variant-nomenclature-parser-0.4.0/pyproject.toml` & `protein-variant-nomenclature-parser-0.5.0/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 [build-system]
 requires = ["setuptools", "wheel"]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "protein-variant-nomenclature-parser"
-version = "0.4.0"
+version = "0.5.0"
 authors = [
   { name="Jeff Quinn", email="quinnj2@mskcc.org" },
 ]
 description = "An ANTLR based parser for colloquial protein variant nomenclature"
 readme = "README.md"
 requires-python = ">=3.7"
 classifiers = [
```

