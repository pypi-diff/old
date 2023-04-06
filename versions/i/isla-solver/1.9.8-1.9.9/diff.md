# Comparing `tmp/isla-solver-1.9.8.tar.gz` & `tmp/isla-solver-1.9.9.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "isla-solver-1.9.8.tar", last modified: Tue Dec 20 14:36:29 2022, max compression
+gzip compressed data, was "isla-solver-1.9.9.tar", last modified: Thu Dec 22 09:30:16 2022, max compression
```

## Comparing `isla-solver-1.9.8.tar` & `isla-solver-1.9.9.tar`

### file list

```diff
@@ -1,68 +1,68 @@
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.051520 isla-solver-1.9.8/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)       25 2022-11-24 14:30:35.000000 isla-solver-1.9.8/MANIFEST.in
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    12951 2022-12-20 14:36:29.051821 isla-solver-1.9.8/PKG-INFO
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    12117 2022-12-20 09:13:17.000000 isla-solver-1.9.8/README.md
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1073 2022-12-20 11:30:22.000000 isla-solver-1.9.8/pyproject.toml
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1528 2022-12-20 14:36:29.052768 isla-solver-1.9.8/setup.cfg
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)      118 2022-11-24 14:30:35.000000 isla-solver-1.9.8/setup.py
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.018347 isla-solver-1.9.8/src/
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.031573 isla-solver-1.9.8/src/isla/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)      766 2022-12-20 11:30:19.000000 isla-solver-1.9.8/src/isla/__init__.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)      778 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/__main__.py
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.034005 isla-solver-1.9.8/src/isla/bnf/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)        0 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/bnf/__init__.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     2849 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/bnf/bnfLexer.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1181 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/bnf/bnfListener.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     8373 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/bnf/bnfParser.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    52582 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla/cli.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    26963 2022-12-16 10:03:47.000000 isla-solver-1.9.8/src/isla/derivation_tree.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    49960 2022-12-20 13:56:06.000000 isla-solver-1.9.8/src/isla/evaluator.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    25531 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla/existential_helpers.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    19812 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla/fuzzer.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    25417 2022-12-15 15:51:50.000000 isla-solver-1.9.8/src/isla/helpers.py
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.037071 isla-solver-1.9.8/src/isla/isla_language/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    18910 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/isla_language/IslaLanguageLexer.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    10661 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/isla_language/IslaLanguageListener.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    69207 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/isla_language/IslaLanguageParser.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)        0 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/isla_language/__init__.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    21556 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla/isla_predicates.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     2948 2022-12-15 15:51:50.000000 isla-solver-1.9.8/src/isla/isla_shortcuts.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)   154876 2022-12-20 13:57:49.000000 isla-solver-1.9.8/src/isla/language.py
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.038236 isla-solver-1.9.8/src/isla/mexpr_lexer/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     3543 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/mexpr_lexer/MexprLexer.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)        0 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/mexpr_lexer/__init__.py
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.039997 isla-solver-1.9.8/src/isla/mexpr_parser/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     9872 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/mexpr_parser/MexprParser.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1807 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/mexpr_parser/MexprParserListener.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)        0 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/mexpr_parser/__init__.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     5567 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla/mutator.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    28675 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla/optimizer.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    17129 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/parser.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    40813 2022-12-16 09:19:12.000000 isla-solver-1.9.8/src/isla/performance_evaluator.py
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.040470 isla-solver-1.9.8/src/isla/resources/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1112 2022-12-20 11:48:59.000000 isla-solver-1.9.8/src/isla/resources/.islarc
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.042328 isla-solver-1.9.8/src/isla/resources/cli_stubs/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1423 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/resources/cli_stubs/README.md
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     3043 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/resources/cli_stubs/constraint.isla
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)      894 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/resources/cli_stubs/grammar.bnf
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)      902 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/resources/cli_stubs/grammar.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)   136699 2022-12-20 11:28:32.000000 isla-solver-1.9.8/src/isla/solver.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     3371 2022-12-20 13:43:04.000000 isla-solver-1.9.8/src/isla/three_valued_truth.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     3358 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla/trie.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1129 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla/type_defs.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    24935 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla/z3_helpers.py
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.047532 isla-solver-1.9.8/src/isla_formalizations/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)      743 2022-11-24 14:30:35.000000 isla-solver-1.9.8/src/isla_formalizations/__init__.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     4230 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla_formalizations/csv.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    11457 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla_formalizations/rest.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     4189 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla_formalizations/scriptsizec.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     7910 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla_formalizations/simple_tar.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    33396 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla_formalizations/tar.py
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     5378 2022-12-15 10:40:58.000000 isla-solver-1.9.8/src/isla_formalizations/xml_lang.py
-drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-20 14:36:29.051142 isla-solver-1.9.8/src/isla_solver.egg-info/
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)    12951 2022-12-20 14:36:29.000000 isla-solver-1.9.8/src/isla_solver.egg-info/PKG-INFO
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1647 2022-12-20 14:36:29.000000 isla-solver-1.9.8/src/isla_solver.egg-info/SOURCES.txt
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)        1 2022-12-20 14:36:29.000000 isla-solver-1.9.8/src/isla_solver.egg-info/dependency_links.txt
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)       39 2022-12-20 14:36:29.000000 isla-solver-1.9.8/src/isla_solver.egg-info/entry_points.txt
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)      510 2022-12-20 14:36:29.000000 isla-solver-1.9.8/src/isla_solver.egg-info/requires.txt
--rw-r--r--   0 dsteinhoefel   (501) staff       (20)       25 2022-12-20 14:36:29.000000 isla-solver-1.9.8/src/isla_solver.egg-info/top_level.txt
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.594619 isla-solver-1.9.9/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)       25 2022-11-24 14:30:35.000000 isla-solver-1.9.9/MANIFEST.in
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    12951 2022-12-22 09:30:16.594789 isla-solver-1.9.9/PKG-INFO
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    12117 2022-12-22 09:28:00.000000 isla-solver-1.9.9/README.md
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1073 2022-12-22 09:29:13.000000 isla-solver-1.9.9/pyproject.toml
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1528 2022-12-22 09:30:16.595832 isla-solver-1.9.9/setup.cfg
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)      118 2022-11-24 14:30:35.000000 isla-solver-1.9.9/setup.py
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.567370 isla-solver-1.9.9/src/
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.575861 isla-solver-1.9.9/src/isla/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)      766 2022-12-22 09:29:03.000000 isla-solver-1.9.9/src/isla/__init__.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)      778 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/__main__.py
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.577726 isla-solver-1.9.9/src/isla/bnf/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)        0 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/bnf/__init__.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     2849 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/bnf/bnfLexer.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1181 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/bnf/bnfListener.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     8373 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/bnf/bnfParser.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    52582 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla/cli.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    27616 2022-12-22 09:28:01.000000 isla-solver-1.9.9/src/isla/derivation_tree.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    49960 2022-12-22 09:28:00.000000 isla-solver-1.9.9/src/isla/evaluator.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    25531 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla/existential_helpers.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    19812 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla/fuzzer.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    25417 2022-12-15 15:51:50.000000 isla-solver-1.9.9/src/isla/helpers.py
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.580930 isla-solver-1.9.9/src/isla/isla_language/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    18910 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/isla_language/IslaLanguageLexer.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    10661 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/isla_language/IslaLanguageListener.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    69207 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/isla_language/IslaLanguageParser.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)        0 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/isla_language/__init__.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    21556 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla/isla_predicates.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     2948 2022-12-15 15:51:50.000000 isla-solver-1.9.9/src/isla/isla_shortcuts.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)   154876 2022-12-22 09:28:00.000000 isla-solver-1.9.9/src/isla/language.py
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.581917 isla-solver-1.9.9/src/isla/mexpr_lexer/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     3543 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/mexpr_lexer/MexprLexer.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)        0 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/mexpr_lexer/__init__.py
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.583780 isla-solver-1.9.9/src/isla/mexpr_parser/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     9872 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/mexpr_parser/MexprParser.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1807 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/mexpr_parser/MexprParserListener.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)        0 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/mexpr_parser/__init__.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     5567 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla/mutator.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    28675 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla/optimizer.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    17129 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/parser.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    40813 2022-12-22 09:28:00.000000 isla-solver-1.9.9/src/isla/performance_evaluator.py
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.584241 isla-solver-1.9.9/src/isla/resources/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1112 2022-12-22 09:28:00.000000 isla-solver-1.9.9/src/isla/resources/.islarc
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.586689 isla-solver-1.9.9/src/isla/resources/cli_stubs/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1423 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/resources/cli_stubs/README.md
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     3043 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/resources/cli_stubs/constraint.isla
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)      894 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/resources/cli_stubs/grammar.bnf
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)      902 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/resources/cli_stubs/grammar.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)   136699 2022-12-22 09:28:00.000000 isla-solver-1.9.9/src/isla/solver.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     3371 2022-12-22 09:28:00.000000 isla-solver-1.9.9/src/isla/three_valued_truth.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     3358 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla/trie.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1129 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla/type_defs.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    24935 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla/z3_helpers.py
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.591436 isla-solver-1.9.9/src/isla_formalizations/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)      743 2022-11-24 14:30:35.000000 isla-solver-1.9.9/src/isla_formalizations/__init__.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     4230 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla_formalizations/csv.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    11457 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla_formalizations/rest.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     4189 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla_formalizations/scriptsizec.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     7910 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla_formalizations/simple_tar.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    33396 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla_formalizations/tar.py
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     5378 2022-12-15 10:40:58.000000 isla-solver-1.9.9/src/isla_formalizations/xml_lang.py
+drwxr-xr-x   0 dsteinhoefel   (501) staff       (20)        0 2022-12-22 09:30:16.594224 isla-solver-1.9.9/src/isla_solver.egg-info/
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)    12951 2022-12-22 09:30:16.000000 isla-solver-1.9.9/src/isla_solver.egg-info/PKG-INFO
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)     1647 2022-12-22 09:30:16.000000 isla-solver-1.9.9/src/isla_solver.egg-info/SOURCES.txt
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)        1 2022-12-22 09:30:16.000000 isla-solver-1.9.9/src/isla_solver.egg-info/dependency_links.txt
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)       39 2022-12-22 09:30:16.000000 isla-solver-1.9.9/src/isla_solver.egg-info/entry_points.txt
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)      510 2022-12-22 09:30:16.000000 isla-solver-1.9.9/src/isla_solver.egg-info/requires.txt
+-rw-r--r--   0 dsteinhoefel   (501) staff       (20)       25 2022-12-22 09:30:16.000000 isla-solver-1.9.9/src/isla_solver.egg-info/top_level.txt
```

### Comparing `isla-solver-1.9.8/PKG-INFO` & `isla-solver-1.9.9/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: isla-solver
-Version: 1.9.8
+Version: 1.9.9
 Summary: The ISLa Input Specification Language and its solver.
 Home-page: https://github.com/rindPHI/isla
 Author: Dominic Steinhoefel
 Author-email: Dominic Steinhoefel <dominic.steinhoefel@cispa.de>
 Project-URL: Homepage, https://github.com/rindPHI/isla/
 Project-URL: Bug Tracker, https://github.com/rindPHI/isla/issues
 Classifier: Intended Audience :: Science/Research
```

### Comparing `isla-solver-1.9.8/README.md` & `isla-solver-1.9.9/README.md`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/pyproject.toml` & `isla-solver-1.9.9/pyproject.toml`

 * *Files 2% similar despite different names*

```diff
@@ -4,15 +4,15 @@
     "setuptools-antlr",
     "wheel"
 ]
 build-backend = "setuptools.build_meta"
 
 [project]
 name = "isla-solver"
-version = "1.9.8"
+version = "1.9.9"
 authors = [
     { name = "Dominic Steinhoefel", email = "dominic.steinhoefel@cispa.de" },
 ]
 description = "The ISLa Input Specification Language and its solver."
 readme = "README.md"
 license = { file = "LICENSE" }
 requires-python = ">=3.10"
```

### Comparing `isla-solver-1.9.8/setup.cfg` & `isla-solver-1.9.9/setup.cfg`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/__init__.py` & `isla-solver-1.9.9/src/isla/__init__.py`

 * *Files 1% similar despite different names*

```diff
@@ -12,8 +12,8 @@
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with ISLa.  If not, see <http://www.gnu.org/licenses/>.
 
-__version__ = "1.9.8"
+__version__ = "1.9.9"
```

### Comparing `isla-solver-1.9.8/src/isla/__main__.py` & `isla-solver-1.9.9/src/isla/__main__.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/bnf/bnfLexer.py` & `isla-solver-1.9.9/src/isla/bnf/bnfLexer.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/bnf/bnfListener.py` & `isla-solver-1.9.9/src/isla/bnf/bnfListener.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/bnf/bnfParser.py` & `isla-solver-1.9.9/src/isla/bnf/bnfParser.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/cli.py` & `isla-solver-1.9.9/src/isla/cli.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/derivation_tree.py` & `isla-solver-1.9.9/src/isla/derivation_tree.py`

 * *Files 1% similar despite different names*

```diff
@@ -28,14 +28,15 @@
     Tuple,
     List,
     Callable,
     Union,
     Generator,
 )
 
+import graphviz
 import ijson
 from grammar_graph import gg
 from graphviz import Digraph
 
 from isla.helpers import is_nonterminal, traverse, TRAVERSE_POSTORDER
 from isla.trie import SubtreesTrie
 from isla.type_defs import Path, ParseTree
@@ -810,19 +811,38 @@
 
     def __str__(self) -> str:
         return self.to_string(show_open_leaves=True)
 
     def to_dot(self) -> str:
         dot = Digraph(comment="Derivation Tree")
         dot.attr("node", shape="plain")
+        levels: Dict[int, List[DerivationTree]] = {}
 
-        def action(_, t: DerivationTree):
+        def action(path: Path, t: DerivationTree):
             dot.node(
                 repr(t.id),
                 "<" + html.escape(t.value) + f' <FONT COLOR="gray">({t.id})</FONT>>',
             )
             for child in t.children or []:
                 dot.edge(repr(t.id), repr(child.id))
 
+            levels.setdefault(len(path), []).append(t)
+
         self.traverse(action)
 
+        # Ensure that nodes at the same levels actually appear at the same levels,
+        # and in the right orders.
+        for nodes in levels.values():
+            if len(nodes) < 2:
+                continue
+
+            child_graph = graphviz.Digraph()
+            child_graph.attr(rank="same")
+
+            for idx in range(len(nodes) - 1):
+                child_graph.edge(
+                    repr(nodes[idx].id), repr(nodes[idx + 1].id), style="invis"
+                )
+
+            dot.subgraph(child_graph)
+
         return dot.source
```

### Comparing `isla-solver-1.9.8/src/isla/evaluator.py` & `isla-solver-1.9.9/src/isla/evaluator.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/existential_helpers.py` & `isla-solver-1.9.9/src/isla/existential_helpers.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/fuzzer.py` & `isla-solver-1.9.9/src/isla/fuzzer.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/helpers.py` & `isla-solver-1.9.9/src/isla/helpers.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/isla_language/IslaLanguageLexer.py` & `isla-solver-1.9.9/src/isla/isla_language/IslaLanguageLexer.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/isla_language/IslaLanguageListener.py` & `isla-solver-1.9.9/src/isla/isla_language/IslaLanguageListener.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/isla_language/IslaLanguageParser.py` & `isla-solver-1.9.9/src/isla/isla_language/IslaLanguageParser.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/isla_predicates.py` & `isla-solver-1.9.9/src/isla/isla_predicates.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/isla_shortcuts.py` & `isla-solver-1.9.9/src/isla/isla_shortcuts.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/language.py` & `isla-solver-1.9.9/src/isla/language.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/mexpr_lexer/MexprLexer.py` & `isla-solver-1.9.9/src/isla/mexpr_lexer/MexprLexer.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/mexpr_parser/MexprParser.py` & `isla-solver-1.9.9/src/isla/mexpr_parser/MexprParser.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/mexpr_parser/MexprParserListener.py` & `isla-solver-1.9.9/src/isla/mexpr_parser/MexprParserListener.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/mutator.py` & `isla-solver-1.9.9/src/isla/mutator.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/optimizer.py` & `isla-solver-1.9.9/src/isla/optimizer.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/parser.py` & `isla-solver-1.9.9/src/isla/parser.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/performance_evaluator.py` & `isla-solver-1.9.9/src/isla/performance_evaluator.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/resources/.islarc` & `isla-solver-1.9.9/src/isla/resources/.islarc`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/resources/cli_stubs/README.md` & `isla-solver-1.9.9/src/isla/resources/cli_stubs/README.md`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/resources/cli_stubs/constraint.isla` & `isla-solver-1.9.9/src/isla/resources/cli_stubs/constraint.isla`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/resources/cli_stubs/grammar.bnf` & `isla-solver-1.9.9/src/isla/resources/cli_stubs/grammar.bnf`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/resources/cli_stubs/grammar.py` & `isla-solver-1.9.9/src/isla/resources/cli_stubs/grammar.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/solver.py` & `isla-solver-1.9.9/src/isla/solver.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/three_valued_truth.py` & `isla-solver-1.9.9/src/isla/three_valued_truth.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/trie.py` & `isla-solver-1.9.9/src/isla/trie.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/type_defs.py` & `isla-solver-1.9.9/src/isla/type_defs.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla/z3_helpers.py` & `isla-solver-1.9.9/src/isla/z3_helpers.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla_formalizations/__init__.py` & `isla-solver-1.9.9/src/isla_formalizations/__init__.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla_formalizations/csv.py` & `isla-solver-1.9.9/src/isla_formalizations/csv.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla_formalizations/rest.py` & `isla-solver-1.9.9/src/isla_formalizations/rest.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla_formalizations/scriptsizec.py` & `isla-solver-1.9.9/src/isla_formalizations/scriptsizec.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla_formalizations/simple_tar.py` & `isla-solver-1.9.9/src/isla_formalizations/simple_tar.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla_formalizations/tar.py` & `isla-solver-1.9.9/src/isla_formalizations/tar.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla_formalizations/xml_lang.py` & `isla-solver-1.9.9/src/isla_formalizations/xml_lang.py`

 * *Files identical despite different names*

### Comparing `isla-solver-1.9.8/src/isla_solver.egg-info/PKG-INFO` & `isla-solver-1.9.9/src/isla_solver.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: isla-solver
-Version: 1.9.8
+Version: 1.9.9
 Summary: The ISLa Input Specification Language and its solver.
 Home-page: https://github.com/rindPHI/isla
 Author: Dominic Steinhoefel
 Author-email: Dominic Steinhoefel <dominic.steinhoefel@cispa.de>
 Project-URL: Homepage, https://github.com/rindPHI/isla/
 Project-URL: Bug Tracker, https://github.com/rindPHI/isla/issues
 Classifier: Intended Audience :: Science/Research
```

### Comparing `isla-solver-1.9.8/src/isla_solver.egg-info/SOURCES.txt` & `isla-solver-1.9.9/src/isla_solver.egg-info/SOURCES.txt`

 * *Files identical despite different names*

