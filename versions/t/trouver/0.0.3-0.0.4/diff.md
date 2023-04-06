# Comparing `tmp/trouver-0.0.3.tar.gz` & `tmp/trouver-0.0.4.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "trouver-0.0.3.tar", last modified: Tue Jan 31 13:55:19 2023, max compression
+gzip compressed data, was "trouver-0.0.4.tar", last modified: Thu Apr  6 14:19:05 2023, max compression
```

## Comparing `trouver-0.0.3.tar` & `trouver-0.0.4.tar`

### file list

```diff
@@ -1,54 +1,56 @@
-drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-31 13:55:19.052499 trouver-0.0.3/
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    11357 2023-01-24 14:21:12.000000 trouver-0.0.3/LICENSE
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      111 2022-12-29 00:02:40.000000 trouver-0.0.3/MANIFEST.in
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    41965 2023-01-31 13:55:19.052499 trouver-0.0.3/PKG-INFO
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    41100 2023-01-31 13:51:19.000000 trouver-0.0.3/README.md
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     1088 2023-01-31 13:55:12.000000 trouver-0.0.3/settings.ini
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)       38 2023-01-31 13:55:19.052499 trouver-0.0.3/setup.cfg
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     2541 2022-12-29 00:02:40.000000 trouver-0.0.3/setup.py
-drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-31 13:55:19.048499 trouver-0.0.3/trouver/
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)       22 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/__init__.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)   133213 2023-01-27 14:26:17.000000 trouver-0.0.3/trouver/_modidx.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      142 2022-12-29 00:02:40.000000 trouver-0.0.3/trouver/core.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    21696 2023-01-27 14:26:17.000000 trouver-0.0.3/trouver/helper.py
-drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-31 13:55:19.052499 trouver-0.0.3/trouver/latex/
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/latex/__init__.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    54997 2023-01-31 13:51:19.000000 trouver-0.0.3/trouver/latex/convert.py
-drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-31 13:55:19.052499 trouver-0.0.3/trouver/markdown/
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/__init__.py
-drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-31 13:55:19.052499 trouver-0.0.3/trouver/markdown/markdown/
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/markdown/__init__.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    49976 2023-01-27 14:25:56.000000 trouver-0.0.3/trouver/markdown/markdown/file.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      823 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/markdown/heading.py
-drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-31 13:55:19.052499 trouver-0.0.3/trouver/markdown/obsidian/
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/__init__.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     3432 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/footnotes.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    18910 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/links.py
-drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-31 13:55:19.052499 trouver-0.0.3/trouver/markdown/obsidian/personal/
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/__init__.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     2131 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/authors.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    15600 2023-01-27 14:26:17.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/index_notes.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    19555 2023-01-27 14:26:17.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/information_notes.py
-drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-31 13:55:19.052499 trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      692 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/__init__.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     3377 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/database_update.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    13281 2023-01-27 14:25:56.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/information_note_types.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    11113 2023-01-16 22:14:02.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/notation.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    11305 2023-01-27 14:25:56.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/notation_identification.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    20994 2023-01-27 14:25:56.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     1333 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/notations.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    37379 2023-01-27 14:26:17.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/notation.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     5220 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/note_processing.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    10439 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/note_type.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     2676 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/notes.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    45152 2023-01-27 14:26:17.000000 trouver-0.0.3/trouver/markdown/obsidian/personal/reference.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     1206 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/tags.py
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    23521 2023-01-24 14:31:26.000000 trouver-0.0.3/trouver/markdown/obsidian/vault.py
-drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-31 13:55:19.052499 trouver-0.0.3/trouver.egg-info/
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    41965 2023-01-31 13:55:19.000000 trouver-0.0.3/trouver.egg-info/PKG-INFO
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     1651 2023-01-31 13:55:19.000000 trouver-0.0.3/trouver.egg-info/SOURCES.txt
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        1 2023-01-31 13:55:19.000000 trouver-0.0.3/trouver.egg-info/dependency_links.txt
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)       57 2023-01-31 13:55:19.000000 trouver-0.0.3/trouver.egg-info/entry_points.txt
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        1 2022-12-29 00:17:43.000000 trouver-0.0.3/trouver.egg-info/not-zip-safe
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      114 2023-01-31 13:55:19.000000 trouver-0.0.3/trouver.egg-info/requires.txt
--rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        8 2023-01-31 13:55:19.000000 trouver-0.0.3/trouver.egg-info/top_level.txt
+drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-04-06 14:19:05.124606 trouver-0.0.4/
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    11357 2023-01-24 14:21:12.000000 trouver-0.0.4/LICENSE
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      111 2022-12-29 00:02:40.000000 trouver-0.0.4/MANIFEST.in
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    43614 2023-04-06 14:19:05.124606 trouver-0.0.4/PKG-INFO
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    42749 2023-04-06 14:13:10.000000 trouver-0.0.4/README.md
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      873 2023-04-06 14:13:10.000000 trouver-0.0.4/settings.ini
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)       38 2023-04-06 14:19:05.124606 trouver-0.0.4/setup.cfg
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     2541 2022-12-29 00:02:40.000000 trouver-0.0.4/setup.py
+drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-04-06 14:19:05.120606 trouver-0.0.4/trouver/
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)       22 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/__init__.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)   136124 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/_modidx.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      280 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/_nbdev.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      142 2022-12-29 00:02:40.000000 trouver-0.0.4/trouver/core.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    22039 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/helper.py
+drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-04-06 14:19:05.120606 trouver-0.0.4/trouver/latex/
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/latex/__init__.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    57371 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/latex/convert.py
+drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-04-06 14:19:05.120606 trouver-0.0.4/trouver/markdown/
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/__init__.py
+drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-04-06 14:19:05.120606 trouver-0.0.4/trouver/markdown/markdown/
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/markdown/__init__.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    50601 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/markdown/file.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      823 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/markdown/heading.py
+drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-04-06 14:19:05.120606 trouver-0.0.4/trouver/markdown/obsidian/
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        0 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/__init__.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     3432 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/footnotes.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    18910 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/links.py
+drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-04-06 14:19:05.124606 trouver-0.0.4/trouver/markdown/obsidian/personal/
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      136 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/__init__.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     2131 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/authors.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    15600 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/index_notes.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    19555 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/information_notes.py
+drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-04-06 14:19:05.124606 trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      692 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/__init__.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     3377 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/database_update.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     3232 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/definition_identification.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    13281 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/information_note_types.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    11113 2023-01-16 22:14:02.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/notation.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    11305 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/notation_identification.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    19988 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     1333 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/notations.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    37932 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/notation.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     5220 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/note_processing.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    10439 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/note_type.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     2676 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/notes.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    46282 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/personal/reference.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     1206 2023-01-24 14:31:26.000000 trouver-0.0.4/trouver/markdown/obsidian/tags.py
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    23886 2023-04-06 14:13:10.000000 trouver-0.0.4/trouver/markdown/obsidian/vault.py
+drwxrwxr-x   0 hyunjong  (1000) hyunjong  (1000)        0 2023-04-06 14:19:05.120606 trouver-0.0.4/trouver.egg-info/
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)    43614 2023-04-06 14:19:05.000000 trouver-0.0.4/trouver.egg-info/PKG-INFO
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)     1750 2023-04-06 14:19:05.000000 trouver-0.0.4/trouver.egg-info/SOURCES.txt
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        1 2023-04-06 14:19:05.000000 trouver-0.0.4/trouver.egg-info/dependency_links.txt
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)       57 2023-04-06 14:19:05.000000 trouver-0.0.4/trouver.egg-info/entry_points.txt
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        1 2022-12-29 00:17:43.000000 trouver-0.0.4/trouver.egg-info/not-zip-safe
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)      119 2023-04-06 14:19:05.000000 trouver-0.0.4/trouver.egg-info/requires.txt
+-rw-rw-r--   0 hyunjong  (1000) hyunjong  (1000)        8 2023-04-06 14:19:05.000000 trouver-0.0.4/trouver.egg-info/top_level.txt
```

### Comparing `trouver-0.0.3/LICENSE` & `trouver-0.0.4/LICENSE`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/PKG-INFO` & `trouver-0.0.4/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trouver
-Version: 0.0.3
+Version: 0.0.4
 Summary: Create and maintain mathematical Obsidian.md notes, and gather data from them to train ML models
 Home-page: https://github.com/hyunjongkimmath/trouver
 Author: Hyun Jong Kim
 Author-email: hyunjongkim96@gmail.com
 License: Apache Software License 2.0
 Keywords: nbdev jupyter notebook python
 Platform: UNKNOWN
@@ -31,23 +31,45 @@
 - [GitHub repository](https://github.com/hyunjongkimmath/trouver#readme)
 - [Documentation website](https://hyunjongkimmath.github.io/trouver/)
 - [pypi page](https://pypi.org/project/trouver/)
 
 Mathematicians constantly need to learn and read about concepts with
 which they are unfamiliar. Keeping mathematical notes in an
 [`Obsidian.md`](https://obsidian.md/) vault can help with this learning
-process as `Obsidian.md`.
+process as `Obsidian.md` makes it easy to edit notes, link notes to one
+another, organize notes, read notes, and access notes.
+
+This library currently includes functionalities to 1. Parse LaTeX
+documents (e.g. those available on [`arxiv.org`](https://arxiv.org/))
+and divide them into reasonably lengthed parts/notes/excerpts as `.md`
+files, especially for viewing and editing on `Obsidian.md`. 2. Use a
+machine learning model to categorize the type of text each excerpt is
+(e.g. introducing definitions/notations, presenting a concept,
+presenting a proof). 3. Use a machine learning model to identify
+notations introduced in each excerpt. 4. Create accompanying notes for
+each notation as more `.md` files. 5. Use a machine learning model to
+summarize what these notations denote in the created accompanying notes.
+
+As some of these functionalities use machine learning models, they
+ultimately cannot run perfectly. Nevertheless, some of these models,
+particularly those described in 2 and 3, perform well enough that these
+functionalities are quite useful as tools to help reading mathematical
+papers.
+
+Moreover, the results of the machine learning models are recorded in the
+notes/`.md` files. One can very well correct these recorded results by
+manually editing the affected `.md` files with any file editor.
 
 ## Disclaimer
 
-At the time of this writing (01/18/2023), there is only one
+At the time of this writing (04/03/2023), there is only one
 author/contributor of this library. Nevertheless, the author often
-refers to himself as “the author”, “the authors”, or “the
-author/authors” in writing this library. Moreover, the author often uses
-the [“editorial we”](https://en.wikipedia.org/wiki/We#Editorial_we) in
+refers to himself as *the author*, *the authors*, or *the
+author/authors* in writing this library. Moreover, the author often uses
+the [*editorial we*](https://en.wikipedia.org/wiki/We#Editorial_we) in
 writing this library.
 
 Use this library at your own risk as using this library can write or
 modify files in your computer and as the documentation of some
 components of this library may be inaccurate or outdated. By using this
 library, you agree that the author/authors of this library is/are not
 responsible for any damages from this library and related components.
@@ -57,31 +79,38 @@
 changes.
 
 The author/authors of this library is/are also not affiliated with
 `Obsidian.md`, `fast.ai`, or `Hugging Face`.
 
 ## Install
 
-``` python
-# TODO Write installation instructions
-```
+We recommend having at least 3GB of free space to install `trouver` and
+related components.
 
 ``` sh
 pip install trouver
 ```
 
 You may also have to manually install other libraries which are required
 by the `fast.ai` and/or `Hugging Face` libraries.
 
+We recommend installing [Obsidian.md](https://obsidian.md/) to view,
+edit, and modify mathematical notes created by or which interact with
+`trouver`.
+
+See `how_to.install_trouver` for more details on installation.
+
 # How to use
 
+See also `tutorial.walkthrough` to set up a basic `trouver` workflow.
+
 ## Parse LaTeX documents and split them into parts
 
-`Trouver` can parse `LaTeX` documents and split them up into “parts”
-which are convenient to read in `Obsidian.md` and to take notes on. For
+`Trouver` can parse `LaTeX` documents and split them up into parts which
+are convenient to read in `Obsidian.md` and to take notes on. For
 example, the following code splits up this
 [paper](https://arxiv.org/abs/2106.10586) in creates a folder in an
 Obsidian.md vault\[^4\].
 
 ``` python
 import os
 from pathlib import Path
@@ -123,26 +152,31 @@
 ```
 
 ![The created folder in Obsidian.md looks like this in `Obsidian.md` The
 text in magenta are links, each to a file in the `Obsidian.md`
 vault](.\images/index_setup_reference_from_latex_parts_demonstration.png)
 
 While `Obsidian.md` is not strictly necessary to use `trouver` or to
-read and write the files created by `setup_reference_from_latex_parts`
+read and write the files created by
+[`setup_reference_from_latex_parts`](https://hyunjongkimmath.github.io/trouver/latex.convert.html#setup_reference_from_latex_parts)
 (in fact, any traditional file reader/writer can be used for such
 purposes), reading and writing the files on `Obsidian.md` can be
-convenient.
+convenient. Moreover, even when you use Obsidian, your data is in a
+local folder. In particular, even if `Obsidian.md` happens to get shut
+down, get bought, or change privacy policy, you will (supposedly) not
+lose access to your data.
 
 ## ML model utilities
 
 We have trained a few ML models to detect/predict and provide
-information about “short” mathematical text. These ML models are
-available on [`Hugging Face`](https://huggingface.co/) and as such, they
-can be downloaded to and used from one’s local machines. Please note
-that ML models can be large and the locations that the Hugging Face
+information about short (or at least not-too-long) mathematical text.
+These ML models are available on
+[`Hugging Face`](https://huggingface.co/) and as such, they can be
+downloaded to and used from one’s local machines. Please note that ML
+models can be large and the locations that the Hugging Face
 [Transformers](https://huggingface.co/docs/transformers/index) library
 downloads such models to can vary from machine to machine.
 
 For each of these models, we may or may not have also written some
 instructions on how to train similar models given appropriately
 formatted data[^1].
 
@@ -333,15 +367,15 @@
 
     This is what the same note looks like after predicting its note type:
 
 
     ---
     cssclass: clean-embeds
     aliases: [number_theory_reference_1_ring]
-    tags: [_meta/literature_note, _reference/number_theory_reference_1, _auto/_meta/definition]
+    tags: [_reference/number_theory_reference_1, _meta/literature_note, _auto/_meta/definition]
     ---
     # Ring[^1]
 
     A **(commutative) ring** is a set $R$, equipped with two binary operators, denoted $+$ and $\cdot$, such that the following hold:
 
     1. $R$ is an abelian group under $+$ with identity element $0$.
     2. $R$ is an commutative monoid under $\cdot$ with identity element $1$.
@@ -485,33 +519,39 @@
     ('False', tensor(0), tensor([1.0000e+00, 4.8617e-06]))
 
 ``` python
 # TODO: examples of using functions in markdown.obsidian.personal.machine_learning.notation_identifcation.
 ```
 
 Similarly as with the `information_note_type` model, `trouver` provides
-functions (namely `automatically_mark_notations`) which locate within
-notes mathematical notations that are newly introduced in the text of
-the notes and record on these notes locations of such notations (by
-surrounding double asterisks `**` to LaTeX math mode strings). Note that
-this is done by applying the `notation_identification` model’s `predict`
-method as many times on a single piece of text as there are LaTeX math
-mode strings in the text. As such, these predictions often take a long
-time.
+functions (namely
+[`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations))
+which locate within notes mathematical notations that are newly
+introduced in the text of the notes and record on these notes locations
+of such notations (by surrounding double asterisks `**` to LaTeX math
+mode strings). Note that this is done by applying the
+`notation_identification` model’s `predict` method as many times on a
+single piece of text as there are LaTeX math mode strings in the text.
+As such, these predictions often take a long time.
 
-To save time, it is recommended to apply `automatically_mark_notations`
+To save time, it is recommended to apply
+[`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
 only on notes which have the `_meta/definition` or `_meta/notation` tags
 (or `_auto/_meta/definittion` or `_auto/_meta/notation`) in their
 frontmatter YAML metadata[^2].
 
-> **Warning** The `automatically_mark_notations` function note only adds
-> double asterisks `**` to LaTeX math mode strings, but also removes
-> components such as links and footnotes from the text of the note. It
-> is recommended to only apply this function to notes whose text has not
-> been embellished with such components[^3].
+> **Warning** The
+> [`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
+> function not only adds double asterisks `**` to LaTeX math mode
+> strings, but also removes components such as links and footnotes from
+> the text of the note. It is recommended to only apply this function to
+> notes whose text has not been embellished with such components[^3].
+> Moreover, the
+> [`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
+> is currently buggy and should not be applied to the same note twice
 
 The test vault used in the below example contains a single note which
 has already been marked with the `_meta/definition` and `_meta/notation`
 notes. The following example in particular locates notations in that
 note at the very least.
 
 ``` python
@@ -589,15 +629,15 @@
 
     This is what the same note looks like after locating notations introduced:
 
 
     ---
     cssclass: clean-embeds
     aliases: [number_theory_reference_1_ring_of_integers_modulo_n]
-    tags: [_meta/literature_note, _auto/s, _auto/F, _meta/definition, _reference/number_theory_reference_1, _auto/a, _auto/e, _auto/l, _meta/notation]
+    tags: [_meta/literature_note, _auto/l, _auto/e, _auto/F, _meta/notation, _auto/a, _meta/definition, _reference/number_theory_reference_1, _auto/s]
     ---
     # Topic[^1]
     The ring of integers modulo $n$, denoted **$\mathbb{Z}/n\mathbb{Z}$** has the elements $[m]$ for each integer $m$ where $[m_1] = [m_2]$ if and only if $m_1-m_2$ is divisible by $n$. As a ring, it has the following structure:
 
     1. $[m_1] + [m_2] = [m_1+m_2]$
     2. $[m_1] \cdot [m_2] = [m_1 \cdot m_2]$.
 
@@ -652,15 +692,15 @@
 
 ``` python
 summarizer("summarize:Let us now define the upper half plane $\mathbb{H}$ as the set of all complex numbers of real part greater than $1$.\n\n\nlatex_in_original: $\mathbb{H}$")
 ```
 
     Your max_length is set to 200, but you input_length is only 54. You might consider decreasing max_length manually, e.g. summarizer('...', max_length=27)
 
-    [{'summary_text': 'the upper half plane of the complex plane $\\ mathbb{ H} $. It is defined as the set of all complex numbers of real part greater than $1$.'}]
+    [{'summary_text': 'the upper half plane of the real part greater than $1$. It is defined as the set of all complex numbers of real parts greater than $$.'}]
 
 In the above example, the summarizer determines that the notation
 `$\mathbb{H}$` introduced in the text
 
 ``` markdown
 Let us now define the upper half plane $\mathbb{H}$ as the set of all complex numbers of real part greater than $1$.
 ```
@@ -669,22 +709,23 @@
 `'the upper half plane of the complex plane $\\ mathbb{ H} $. It is defined as the set of all complex numbers of real part greater than $1$.'`.
 
 Once we mark notations introduced in information notes by surrounding
 LaTeX math mode strings with double asterisks `**` (manually and/or by
 using the `notation_identification` model, see [the section about the
 `notation_identification`
 model](#use-an-ml-model-to-find-notations-introduced-in-text) above), we
-can use the `make_notation_notes_from_double_asts` function to make
-notation notes dedicated to those introduced notations and to link these
-newly created notation notes to the information notes.
+can use the
+[`make_notation_notes_from_double_asts`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.notation.html#make_notation_notes_from_double_asts)
+function to make notation notes dedicated to those introduced notations
+and to link these newly created notation notes to the information notes.
 
 After making these notation notes, we can use the
-`append_summary_to_notation_note` function to predict what each notation
-is supposed to denote and add these predicted summaries to the notation
-notes themselves.
+[`append_summary_to_notation_note`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_summarization.html#append_summary_to_notation_note)
+function to predict what each notation is supposed to denote and add
+these predicted summaries to the notation notes themselves.
 
 For the example below, there is at least one information note with
 notations already marked with double asterisks `**`.
 
 ``` python
 from trouver.markdown.obsidian.personal.notation import make_notation_notes_from_double_asts, notation_notes_linked_in_see_also_section
 from trouver.markdown.obsidian.personal.machine_learning.notation_summarization import append_summary_to_notation_note
@@ -791,22 +832,22 @@
 
 
     ---
     detect_regex: []
     latex_in_original: [R/I]
     tags: [_auto/notation_summary]
     ---
-    $R/I$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring $R/I$ where $R$ is a ring and $I$ is an ideal. It is given by $$\begin{align*} [x]+[y] &= [x+y]\\[x],\cdot [y]$. [$][x]$ is the ring whose elements are the equivalence classes of elements of $R = [\3]$ given by 
+    $R/I$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring of the ideal $R/I$. It is the ring whose elements are the equivalence classes of elements of $R$. 
 
     ---
     detect_regex: []
     latex_in_original: ["\\sim"]
     tags: [_auto/notation_summary]
     ---
-    $\sim$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring $R/I$ given by $x\sim y$ where $R$ is a ring and $I$ is an ideal. 
+    $\sim$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring of the ideal $R/I$. It is the ring whose elements are the equivalence classes of elements of a ring $R$. 
 
 At the time of this writing (1/30/2023), the author of `trouver`
 believes that this summarization model could be improved upon with more
 data; thus far, this model was trained on less than 1700 data points.
 
 # How the examples/tests are structured
 
@@ -910,77 +951,44 @@
 library.
 
 `trouver` was built using [`nbdev`](https://nbdev.fast.ai/) as a
 template.
 
 # Release notes
 
-## Ver. 0
-
-#### Ver. 0.0.3
-
-- Fixed [issue \#
-  32](https://github.com/hyunjongkimmath/trouver/issues/32) in which
-  setting up an `Obsidian.md` vault folder from a LaTeX document was not
-  numbering sections and theorem-like environments correctly with a
-  theorem-like environment of the form
-  `\numbertheorem{theorem}{Theorem}[section]` was being defined.
-- Finished implementing `append_summary_to_notation_note`
-- Modified `dict_to_metadata` function to escape and enquote strings if
-  necessary to take into consideration that `yaml.safe_load` does uses
-  quotations to consider strings as escaped.
-- Fixed a bug in `notation_notes_linked_in_see_also_section` where the
-  main of notation where the `VaultNote` objects were incorrectly
-  constructed by passing an argument to the `rel_path` parameter as
-  opposed to the `name` parameter.
-- Fixed a bug in `_obsidian_vault_plugin_configs_file`; I had realized
-  that files for non-core `Obsidian.md` plugins are stored in
-  `.obsidian/plugins/<plugin_name>` in the vault directory.
-- Changed the default `template_location` argument from `'.'` to `'/'`
-  in `markdown.obsidian.personal.reference`.
-- Move `latex_to_path_accepted_string` function from
-  `20_markdown.obsidian.personal.notation.ipynb` to `00_helper.ipynb`
-- Modify `_consider_part_to_add` in `16_latex.convert` so that
-  multi-line section titles in LaTeX documents get parsed as single-line
-  titles
-- Modify `convert_title_to_folder_name` in
-  `12_markdown.obsidian.personal.index_notes.ipynb` and
-  `_create_note_for_part` in `16_latex.convert.ipynb` to use
-  `sanitize_filename`
-
-#### Ver. 0.0.2
-
-- I made the mistake of note including much of the contents of
-  `index.ipynb` in the `pypi` library release, so that should be fixed..
-
-#### Ver. 0.0.1
-
-- Initial release
+See `release_notes`.
 
 [^1]: Given time, the author of `trouver` eventually plans on writing
     instructions on training each of the models.
 
 [^2]: At the time of this writing (1/30/2023), the
     `information_note_type` model is fairly good at telling when a note
     introduces a definition or a notation, but will often conflate the
     two. In other words, the model may predict that a note ought to have
     the `_meta/definition` tag assigned to it when the `_meta/notation`
     tag should be assigned to it and vice versa, but the model will
     fairly usually assign at least one of the tags when the note
     introduces a definition or a notation and will assign neither of the
     tags when the note does not introduce a definition or a notation.
 
-[^3]: More precisely, `automatically_mark_notations` first applies
-    `process_standard_information_note` to a `MarkdownFile` object
-    constructed from the `VaultNote` object to roughly obtain the “raw
-    text” of the note, uses that raw text to locate notations, marks the
-    notations in the raw text, and then replaces the text from the note
-    with the raw text with notations marked. In the process of obtaining
-    the “raw text”, the `process_standard_information_note` function
-    removes components such as links and footnotes from the text.
+[^3]: More precisely,
+    [`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
+    first applies
+    [`process_standard_information_note`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.note_processing.html#process_standard_information_note)
+    to a
+    [`MarkdownFile`](https://hyunjongkimmath.github.io/trouver/markdown.markdown.file.html#markdownfile)
+    object constructed from the
+    [`VaultNote`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.vault.html#vaultnote)
+    object to roughly obtain the *raw text* of the note, uses that raw
+    text to locate notations, marks the notations in the raw text, and
+    then replaces the text from the note with the raw text with
+    notations marked. In the process of obtaining the raw text, the
+    [`process_standard_information_note`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.note_processing.html#process_standard_information_note)
+    function removes components such as links and footnotes from the
+    text.
 
 [^4]: There seems to be a bug in the above example where inexplicable
     tags (e.g. `_auto/s`, `_auto/a`) are added to the note along with
     the double asterisks `**`. This issue is reported as [Issue
     \#33](https://github.com/hyunjongkimmath/trouver/issues/33).
 
 [^5]: cf. [nbdev’s End-To-End
```

### Comparing `trouver-0.0.3/README.md` & `trouver-0.0.4/README.md`

 * *Files 3% similar despite different names*

```diff
@@ -8,23 +8,45 @@
 - [GitHub repository](https://github.com/hyunjongkimmath/trouver#readme)
 - [Documentation website](https://hyunjongkimmath.github.io/trouver/)
 - [pypi page](https://pypi.org/project/trouver/)
 
 Mathematicians constantly need to learn and read about concepts with
 which they are unfamiliar. Keeping mathematical notes in an
 [`Obsidian.md`](https://obsidian.md/) vault can help with this learning
-process as `Obsidian.md`.
+process as `Obsidian.md` makes it easy to edit notes, link notes to one
+another, organize notes, read notes, and access notes.
+
+This library currently includes functionalities to 1. Parse LaTeX
+documents (e.g. those available on [`arxiv.org`](https://arxiv.org/))
+and divide them into reasonably lengthed parts/notes/excerpts as `.md`
+files, especially for viewing and editing on `Obsidian.md`. 2. Use a
+machine learning model to categorize the type of text each excerpt is
+(e.g. introducing definitions/notations, presenting a concept,
+presenting a proof). 3. Use a machine learning model to identify
+notations introduced in each excerpt. 4. Create accompanying notes for
+each notation as more `.md` files. 5. Use a machine learning model to
+summarize what these notations denote in the created accompanying notes.
+
+As some of these functionalities use machine learning models, they
+ultimately cannot run perfectly. Nevertheless, some of these models,
+particularly those described in 2 and 3, perform well enough that these
+functionalities are quite useful as tools to help reading mathematical
+papers.
+
+Moreover, the results of the machine learning models are recorded in the
+notes/`.md` files. One can very well correct these recorded results by
+manually editing the affected `.md` files with any file editor.
 
 ## Disclaimer
 
-At the time of this writing (01/18/2023), there is only one
+At the time of this writing (04/03/2023), there is only one
 author/contributor of this library. Nevertheless, the author often
-refers to himself as “the author”, “the authors”, or “the
-author/authors” in writing this library. Moreover, the author often uses
-the [“editorial we”](https://en.wikipedia.org/wiki/We#Editorial_we) in
+refers to himself as *the author*, *the authors*, or *the
+author/authors* in writing this library. Moreover, the author often uses
+the [*editorial we*](https://en.wikipedia.org/wiki/We#Editorial_we) in
 writing this library.
 
 Use this library at your own risk as using this library can write or
 modify files in your computer and as the documentation of some
 components of this library may be inaccurate or outdated. By using this
 library, you agree that the author/authors of this library is/are not
 responsible for any damages from this library and related components.
@@ -34,31 +56,38 @@
 changes.
 
 The author/authors of this library is/are also not affiliated with
 `Obsidian.md`, `fast.ai`, or `Hugging Face`.
 
 ## Install
 
-``` python
-# TODO Write installation instructions
-```
+We recommend having at least 3GB of free space to install `trouver` and
+related components.
 
 ``` sh
 pip install trouver
 ```
 
 You may also have to manually install other libraries which are required
 by the `fast.ai` and/or `Hugging Face` libraries.
 
+We recommend installing [Obsidian.md](https://obsidian.md/) to view,
+edit, and modify mathematical notes created by or which interact with
+`trouver`.
+
+See `how_to.install_trouver` for more details on installation.
+
 # How to use
 
+See also `tutorial.walkthrough` to set up a basic `trouver` workflow.
+
 ## Parse LaTeX documents and split them into parts
 
-`Trouver` can parse `LaTeX` documents and split them up into “parts”
-which are convenient to read in `Obsidian.md` and to take notes on. For
+`Trouver` can parse `LaTeX` documents and split them up into parts which
+are convenient to read in `Obsidian.md` and to take notes on. For
 example, the following code splits up this
 [paper](https://arxiv.org/abs/2106.10586) in creates a folder in an
 Obsidian.md vault\[^4\].
 
 ``` python
 import os
 from pathlib import Path
@@ -100,26 +129,31 @@
 ```
 
 ![The created folder in Obsidian.md looks like this in `Obsidian.md` The
 text in magenta are links, each to a file in the `Obsidian.md`
 vault](.\images/index_setup_reference_from_latex_parts_demonstration.png)
 
 While `Obsidian.md` is not strictly necessary to use `trouver` or to
-read and write the files created by `setup_reference_from_latex_parts`
+read and write the files created by
+[`setup_reference_from_latex_parts`](https://hyunjongkimmath.github.io/trouver/latex.convert.html#setup_reference_from_latex_parts)
 (in fact, any traditional file reader/writer can be used for such
 purposes), reading and writing the files on `Obsidian.md` can be
-convenient.
+convenient. Moreover, even when you use Obsidian, your data is in a
+local folder. In particular, even if `Obsidian.md` happens to get shut
+down, get bought, or change privacy policy, you will (supposedly) not
+lose access to your data.
 
 ## ML model utilities
 
 We have trained a few ML models to detect/predict and provide
-information about “short” mathematical text. These ML models are
-available on [`Hugging Face`](https://huggingface.co/) and as such, they
-can be downloaded to and used from one’s local machines. Please note
-that ML models can be large and the locations that the Hugging Face
+information about short (or at least not-too-long) mathematical text.
+These ML models are available on
+[`Hugging Face`](https://huggingface.co/) and as such, they can be
+downloaded to and used from one’s local machines. Please note that ML
+models can be large and the locations that the Hugging Face
 [Transformers](https://huggingface.co/docs/transformers/index) library
 downloads such models to can vary from machine to machine.
 
 For each of these models, we may or may not have also written some
 instructions on how to train similar models given appropriately
 formatted data[^1].
 
@@ -310,15 +344,15 @@
 
     This is what the same note looks like after predicting its note type:
 
 
     ---
     cssclass: clean-embeds
     aliases: [number_theory_reference_1_ring]
-    tags: [_meta/literature_note, _reference/number_theory_reference_1, _auto/_meta/definition]
+    tags: [_reference/number_theory_reference_1, _meta/literature_note, _auto/_meta/definition]
     ---
     # Ring[^1]
 
     A **(commutative) ring** is a set $R$, equipped with two binary operators, denoted $+$ and $\cdot$, such that the following hold:
 
     1. $R$ is an abelian group under $+$ with identity element $0$.
     2. $R$ is an commutative monoid under $\cdot$ with identity element $1$.
@@ -462,33 +496,39 @@
     ('False', tensor(0), tensor([1.0000e+00, 4.8617e-06]))
 
 ``` python
 # TODO: examples of using functions in markdown.obsidian.personal.machine_learning.notation_identifcation.
 ```
 
 Similarly as with the `information_note_type` model, `trouver` provides
-functions (namely `automatically_mark_notations`) which locate within
-notes mathematical notations that are newly introduced in the text of
-the notes and record on these notes locations of such notations (by
-surrounding double asterisks `**` to LaTeX math mode strings). Note that
-this is done by applying the `notation_identification` model’s `predict`
-method as many times on a single piece of text as there are LaTeX math
-mode strings in the text. As such, these predictions often take a long
-time.
+functions (namely
+[`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations))
+which locate within notes mathematical notations that are newly
+introduced in the text of the notes and record on these notes locations
+of such notations (by surrounding double asterisks `**` to LaTeX math
+mode strings). Note that this is done by applying the
+`notation_identification` model’s `predict` method as many times on a
+single piece of text as there are LaTeX math mode strings in the text.
+As such, these predictions often take a long time.
 
-To save time, it is recommended to apply `automatically_mark_notations`
+To save time, it is recommended to apply
+[`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
 only on notes which have the `_meta/definition` or `_meta/notation` tags
 (or `_auto/_meta/definittion` or `_auto/_meta/notation`) in their
 frontmatter YAML metadata[^2].
 
-> **Warning** The `automatically_mark_notations` function note only adds
-> double asterisks `**` to LaTeX math mode strings, but also removes
-> components such as links and footnotes from the text of the note. It
-> is recommended to only apply this function to notes whose text has not
-> been embellished with such components[^3].
+> **Warning** The
+> [`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
+> function not only adds double asterisks `**` to LaTeX math mode
+> strings, but also removes components such as links and footnotes from
+> the text of the note. It is recommended to only apply this function to
+> notes whose text has not been embellished with such components[^3].
+> Moreover, the
+> [`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
+> is currently buggy and should not be applied to the same note twice
 
 The test vault used in the below example contains a single note which
 has already been marked with the `_meta/definition` and `_meta/notation`
 notes. The following example in particular locates notations in that
 note at the very least.
 
 ``` python
@@ -566,15 +606,15 @@
 
     This is what the same note looks like after locating notations introduced:
 
 
     ---
     cssclass: clean-embeds
     aliases: [number_theory_reference_1_ring_of_integers_modulo_n]
-    tags: [_meta/literature_note, _auto/s, _auto/F, _meta/definition, _reference/number_theory_reference_1, _auto/a, _auto/e, _auto/l, _meta/notation]
+    tags: [_meta/literature_note, _auto/l, _auto/e, _auto/F, _meta/notation, _auto/a, _meta/definition, _reference/number_theory_reference_1, _auto/s]
     ---
     # Topic[^1]
     The ring of integers modulo $n$, denoted **$\mathbb{Z}/n\mathbb{Z}$** has the elements $[m]$ for each integer $m$ where $[m_1] = [m_2]$ if and only if $m_1-m_2$ is divisible by $n$. As a ring, it has the following structure:
 
     1. $[m_1] + [m_2] = [m_1+m_2]$
     2. $[m_1] \cdot [m_2] = [m_1 \cdot m_2]$.
 
@@ -629,15 +669,15 @@
 
 ``` python
 summarizer("summarize:Let us now define the upper half plane $\mathbb{H}$ as the set of all complex numbers of real part greater than $1$.\n\n\nlatex_in_original: $\mathbb{H}$")
 ```
 
     Your max_length is set to 200, but you input_length is only 54. You might consider decreasing max_length manually, e.g. summarizer('...', max_length=27)
 
-    [{'summary_text': 'the upper half plane of the complex plane $\\ mathbb{ H} $. It is defined as the set of all complex numbers of real part greater than $1$.'}]
+    [{'summary_text': 'the upper half plane of the real part greater than $1$. It is defined as the set of all complex numbers of real parts greater than $$.'}]
 
 In the above example, the summarizer determines that the notation
 `$\mathbb{H}$` introduced in the text
 
 ``` markdown
 Let us now define the upper half plane $\mathbb{H}$ as the set of all complex numbers of real part greater than $1$.
 ```
@@ -646,22 +686,23 @@
 `'the upper half plane of the complex plane $\\ mathbb{ H} $. It is defined as the set of all complex numbers of real part greater than $1$.'`.
 
 Once we mark notations introduced in information notes by surrounding
 LaTeX math mode strings with double asterisks `**` (manually and/or by
 using the `notation_identification` model, see [the section about the
 `notation_identification`
 model](#use-an-ml-model-to-find-notations-introduced-in-text) above), we
-can use the `make_notation_notes_from_double_asts` function to make
-notation notes dedicated to those introduced notations and to link these
-newly created notation notes to the information notes.
+can use the
+[`make_notation_notes_from_double_asts`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.notation.html#make_notation_notes_from_double_asts)
+function to make notation notes dedicated to those introduced notations
+and to link these newly created notation notes to the information notes.
 
 After making these notation notes, we can use the
-`append_summary_to_notation_note` function to predict what each notation
-is supposed to denote and add these predicted summaries to the notation
-notes themselves.
+[`append_summary_to_notation_note`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_summarization.html#append_summary_to_notation_note)
+function to predict what each notation is supposed to denote and add
+these predicted summaries to the notation notes themselves.
 
 For the example below, there is at least one information note with
 notations already marked with double asterisks `**`.
 
 ``` python
 from trouver.markdown.obsidian.personal.notation import make_notation_notes_from_double_asts, notation_notes_linked_in_see_also_section
 from trouver.markdown.obsidian.personal.machine_learning.notation_summarization import append_summary_to_notation_note
@@ -768,22 +809,22 @@
 
 
     ---
     detect_regex: []
     latex_in_original: [R/I]
     tags: [_auto/notation_summary]
     ---
-    $R/I$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring $R/I$ where $R$ is a ring and $I$ is an ideal. It is given by $$\begin{align*} [x]+[y] &= [x+y]\\[x],\cdot [y]$. [$][x]$ is the ring whose elements are the equivalence classes of elements of $R = [\3]$ given by 
+    $R/I$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring of the ideal $R/I$. It is the ring whose elements are the equivalence classes of elements of $R$. 
 
     ---
     detect_regex: []
     latex_in_original: ["\\sim"]
     tags: [_auto/notation_summary]
     ---
-    $\sim$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring $R/I$ given by $x\sim y$ where $R$ is a ring and $I$ is an ideal. 
+    $\sim$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring of the ideal $R/I$. It is the ring whose elements are the equivalence classes of elements of a ring $R$. 
 
 At the time of this writing (1/30/2023), the author of `trouver`
 believes that this summarization model could be improved upon with more
 data; thus far, this model was trained on less than 1700 data points.
 
 # How the examples/tests are structured
 
@@ -887,77 +928,44 @@
 library.
 
 `trouver` was built using [`nbdev`](https://nbdev.fast.ai/) as a
 template.
 
 # Release notes
 
-## Ver. 0
-
-#### Ver. 0.0.3
-
-- Fixed [issue \#
-  32](https://github.com/hyunjongkimmath/trouver/issues/32) in which
-  setting up an `Obsidian.md` vault folder from a LaTeX document was not
-  numbering sections and theorem-like environments correctly with a
-  theorem-like environment of the form
-  `\numbertheorem{theorem}{Theorem}[section]` was being defined.
-- Finished implementing `append_summary_to_notation_note`
-- Modified `dict_to_metadata` function to escape and enquote strings if
-  necessary to take into consideration that `yaml.safe_load` does uses
-  quotations to consider strings as escaped.
-- Fixed a bug in `notation_notes_linked_in_see_also_section` where the
-  main of notation where the `VaultNote` objects were incorrectly
-  constructed by passing an argument to the `rel_path` parameter as
-  opposed to the `name` parameter.
-- Fixed a bug in `_obsidian_vault_plugin_configs_file`; I had realized
-  that files for non-core `Obsidian.md` plugins are stored in
-  `.obsidian/plugins/<plugin_name>` in the vault directory.
-- Changed the default `template_location` argument from `'.'` to `'/'`
-  in `markdown.obsidian.personal.reference`.
-- Move `latex_to_path_accepted_string` function from
-  `20_markdown.obsidian.personal.notation.ipynb` to `00_helper.ipynb`
-- Modify `_consider_part_to_add` in `16_latex.convert` so that
-  multi-line section titles in LaTeX documents get parsed as single-line
-  titles
-- Modify `convert_title_to_folder_name` in
-  `12_markdown.obsidian.personal.index_notes.ipynb` and
-  `_create_note_for_part` in `16_latex.convert.ipynb` to use
-  `sanitize_filename`
-
-#### Ver. 0.0.2
-
-- I made the mistake of note including much of the contents of
-  `index.ipynb` in the `pypi` library release, so that should be fixed..
-
-#### Ver. 0.0.1
-
-- Initial release
+See `release_notes`.
 
 [^1]: Given time, the author of `trouver` eventually plans on writing
     instructions on training each of the models.
 
 [^2]: At the time of this writing (1/30/2023), the
     `information_note_type` model is fairly good at telling when a note
     introduces a definition or a notation, but will often conflate the
     two. In other words, the model may predict that a note ought to have
     the `_meta/definition` tag assigned to it when the `_meta/notation`
     tag should be assigned to it and vice versa, but the model will
     fairly usually assign at least one of the tags when the note
     introduces a definition or a notation and will assign neither of the
     tags when the note does not introduce a definition or a notation.
 
-[^3]: More precisely, `automatically_mark_notations` first applies
-    `process_standard_information_note` to a `MarkdownFile` object
-    constructed from the `VaultNote` object to roughly obtain the “raw
-    text” of the note, uses that raw text to locate notations, marks the
-    notations in the raw text, and then replaces the text from the note
-    with the raw text with notations marked. In the process of obtaining
-    the “raw text”, the `process_standard_information_note` function
-    removes components such as links and footnotes from the text.
+[^3]: More precisely,
+    [`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
+    first applies
+    [`process_standard_information_note`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.note_processing.html#process_standard_information_note)
+    to a
+    [`MarkdownFile`](https://hyunjongkimmath.github.io/trouver/markdown.markdown.file.html#markdownfile)
+    object constructed from the
+    [`VaultNote`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.vault.html#vaultnote)
+    object to roughly obtain the *raw text* of the note, uses that raw
+    text to locate notations, marks the notations in the raw text, and
+    then replaces the text from the note with the raw text with
+    notations marked. In the process of obtaining the raw text, the
+    [`process_standard_information_note`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.note_processing.html#process_standard_information_note)
+    function removes components such as links and footnotes from the
+    text.
 
 [^4]: There seems to be a bug in the above example where inexplicable
     tags (e.g. `_auto/s`, `_auto/a`) are added to the note along with
     the double asterisks `**`. This issue is reported as [Issue
     \#33](https://github.com/hyunjongkimmath/trouver/issues/33).
 
 [^5]: cf. [nbdev’s End-To-End
```

### Comparing `trouver-0.0.3/setup.py` & `trouver-0.0.4/setup.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/_modidx.py` & `trouver-0.0.4/trouver/_modidx.py`

 * *Files 2% similar despite different names*

```diff
@@ -54,14 +54,16 @@
                                                                                   'trouver/latex/convert.py'),
                                        'trouver.latex.convert._append_non_environment_accumulation_to_parts_if_non_empty': ( 'latex.convert.html#_append_non_environment_accumulation_to_parts_if_non_empty',
                                                                                                                              'trouver/latex/convert.py'),
                                        'trouver.latex.convert._argument_detection': ( 'latex.convert.html#_argument_detection',
                                                                                       'trouver/latex/convert.py'),
                                        'trouver.latex.convert._change_counters': ( 'latex.convert.html#_change_counters',
                                                                                    'trouver/latex/convert.py'),
+                                       'trouver.latex.convert._commands_from_newcommand_and_declaremathoperator': ( 'latex.convert.html#_commands_from_newcommand_and_declaremathoperator',
+                                                                                                                    'trouver/latex/convert.py'),
                                        'trouver.latex.convert._consider_part_to_add': ( 'latex.convert.html#_consider_part_to_add',
                                                                                         'trouver/latex/convert.py'),
                                        'trouver.latex.convert._create_note_for_part': ( 'latex.convert.html#_create_note_for_part',
                                                                                         'trouver/latex/convert.py'),
                                        'trouver.latex.convert._create_notes_from_parts': ( 'latex.convert.html#_create_notes_from_parts',
                                                                                            'trouver/latex/convert.py'),
                                        'trouver.latex.convert._create_part_or_update': ( 'latex.convert.html#_create_part_or_update',
@@ -84,18 +86,18 @@
                                                                                                                                   'trouver/latex/convert.py'),
                                        'trouver.latex.convert._node_numbering': ( 'latex.convert.html#_node_numbering',
                                                                                   'trouver/latex/convert.py'),
                                        'trouver.latex.convert._node_warrants_own_part': ( 'latex.convert.html#_node_warrants_own_part',
                                                                                           'trouver/latex/convert.py'),
                                        'trouver.latex.convert._numbering_helper': ( 'latex.convert.html#_numbering_helper',
                                                                                     'trouver/latex/convert.py'),
-                                       'trouver.latex.convert._part_is_of_section': ( 'latex.convert.html#_part_is_of_section',
-                                                                                      'trouver/latex/convert.py'),
-                                       'trouver.latex.convert._part_is_of_subsection': ( 'latex.convert.html#_part_is_of_subsection',
-                                                                                         'trouver/latex/convert.py'),
+                                       'trouver.latex.convert._part_starts_section': ( 'latex.convert.html#_part_starts_section',
+                                                                                       'trouver/latex/convert.py'),
+                                       'trouver.latex.convert._part_starts_subsection': ( 'latex.convert.html#_part_starts_subsection',
+                                                                                          'trouver/latex/convert.py'),
                                        'trouver.latex.convert._process_node': ( 'latex.convert.html#_process_node',
                                                                                 'trouver/latex/convert.py'),
                                        'trouver.latex.convert._replace_command': ( 'latex.convert.html#_replace_command',
                                                                                    'trouver/latex/convert.py'),
                                        'trouver.latex.convert._replace_custom_commands_in_parts': ( 'latex.convert.html#_replace_custom_commands_in_parts',
                                                                                                     'trouver/latex/convert.py'),
                                        'trouver.latex.convert._search_counters_by_pattern': ( 'latex.convert.html#_search_counters_by_pattern',
@@ -395,14 +397,20 @@
                                                                                                                                                                                           'trouver/markdown/obsidian/personal/information_notes.py'),
                                                                       'trouver.markdown.obsidian.personal.information_notes.reference_of_information_note': ( 'markdown.obsidian.personal.information_notes.html#reference_of_information_note',
                                                                                                                                                               'trouver/markdown/obsidian/personal/information_notes.py')},
             'trouver.markdown.obsidian.personal.machine_learning.database_update': { 'trouver.markdown.obsidian.personal.machine_learning.database_update.append_to_database': ( 'markdown.obsidian.personal.machine_learninig.database_update.html#append_to_database',
                                                                                                                                                                                  'trouver/markdown/obsidian/personal/machine_learning/database_update.py'),
                                                                                      'trouver.markdown.obsidian.personal.machine_learning.database_update.max_ID': ( 'markdown.obsidian.personal.machine_learninig.database_update.html#max_id',
                                                                                                                                                                      'trouver/markdown/obsidian/personal/machine_learning/database_update.py')},
+            'trouver.markdown.obsidian.personal.machine_learning.definition_identification': { 'trouver.markdown.obsidian.personal.machine_learning.definition_identification.definition_identification_data_from_note': ( 'markdown.obsidian.personal.machine_learning.definition_identification.html#definition_identification_data_from_note',
+                                                                                                                                                                                                                           'trouver/markdown/obsidian/personal/machine_learning/definition_identification.py'),
+                                                                                               'trouver.markdown.obsidian.personal.machine_learning.definition_identification.definitions_in_text': ( 'markdown.obsidian.personal.machine_learning.definition_identification.html#definitions_in_text',
+                                                                                                                                                                                                      'trouver/markdown/obsidian/personal/machine_learning/definition_identification.py'),
+                                                                                               'trouver.markdown.obsidian.personal.machine_learning.definition_identification.gather_definition_identification_data': ( 'markdown.obsidian.personal.machine_learning.definition_identification.html#gather_definition_identification_data',
+                                                                                                                                                                                                                        'trouver/markdown/obsidian/personal/machine_learning/definition_identification.py')},
             'trouver.markdown.obsidian.personal.machine_learning.information_note_types': { 'trouver.markdown.obsidian.personal.machine_learning.information_note_types._append_single_predicted_tag': ( 'markdown.obsidian.personal.machine_learning.information_note_types.html#_append_single_predicted_tag',
                                                                                                                                                                                                          'trouver/markdown/obsidian/personal/machine_learning/information_note_types.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.information_note_types._auto_prediction': ( 'markdown.obsidian.personal.machine_learning.information_note_types.html#_auto_prediction',
                                                                                                                                                                                              'trouver/markdown/obsidian/personal/machine_learning/information_note_types.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.information_note_types._change_label_tags_for_single_note': ( 'markdown.obsidian.personal.machine_learning.information_note_types.html#_change_label_tags_for_single_note',
                                                                                                                                                                                                                'trouver/markdown/obsidian/personal/machine_learning/information_note_types.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.information_note_types._has_any_label_tags': ( 'markdown.obsidian.personal.machine_learning.information_note_types.html#_has_any_label_tags',
@@ -453,14 +461,16 @@
                                                                                                                                                                                                       'trouver/markdown/obsidian/personal/machine_learning/notation_identification.py'),
                                                                                              'trouver.markdown.obsidian.personal.machine_learning.notation_identification.notation_data_from_text': ( 'markdown.obsidian.personal.machine_learning.notation_identification.html#notation_data_from_text',
                                                                                                                                                                                                       'trouver/markdown/obsidian/personal/machine_learning/notation_identification.py')},
             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization': { 'trouver.markdown.obsidian.personal.machine_learning.notation_summarization._escape_latex_in_original_in_metadata': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#_escape_latex_in_original_in_metadata',
                                                                                                                                                                                                                   'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization._get_summary': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#_get_summary',
                                                                                                                                                                                          'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
+                                                                                            'trouver.markdown.obsidian.personal.machine_learning.notation_summarization._metadata_dict_has_auto_notation_summary_tag': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#_metadata_dict_has_auto_notation_summary_tag',
+                                                                                                                                                                                                                         'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization._notation_has_been_summarized': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#_notation_has_been_summarized',
                                                                                                                                                                                                           'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization._notation_note_has_auto_summary_tag': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#_notation_note_has_auto_summary_tag',
                                                                                                                                                                                                                 'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization._write_summary_to_notation_note': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#_write_summary_to_notation_note',
                                                                                                                                                                                                             'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization.append_column_for_single_text': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#append_column_for_single_text',
@@ -473,16 +483,16 @@
                                                                                                                                                                                                    'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization.gather_notation_note_summaries': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#gather_notation_note_summaries',
                                                                                                                                                                                                            'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization.get_latex_in_original_from_parsed_notation_note_data': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#get_latex_in_original_from_parsed_notation_note_data',
                                                                                                                                                                                                                                  'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization.notation_summarization_data_from_note': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#notation_summarization_data_from_note',
                                                                                                                                                                                                                   'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
-                                                                                            'trouver.markdown.obsidian.personal.machine_learning.notation_summarization.single_input': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#single_input',
-                                                                                                                                                                                         'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
+                                                                                            'trouver.markdown.obsidian.personal.machine_learning.notation_summarization.single_input_for_notation_summarization': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#single_input_for_notation_summarization',
+                                                                                                                                                                                                                    'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py'),
                                                                                             'trouver.markdown.obsidian.personal.machine_learning.notation_summarization.summarize_notation': ( 'markdown.obsidian.personal.machine_learning.notation_summarization.html#summarize_notation',
                                                                                                                                                                                                'trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py')},
             'trouver.markdown.obsidian.personal.machine_learning.notations': {},
             'trouver.markdown.obsidian.personal.notation': { 'trouver.markdown.obsidian.personal.notation._build_replacables_from_groups': ( 'markdown.obsidian.personal.notation.html#_build_replacables_from_groups',
                                                                                                                                              'trouver/markdown/obsidian/personal/notation.py'),
                                                              'trouver.markdown.obsidian.personal.notation._divide_bulleted_list_mf_at_end': ( 'markdown.obsidian.personal.notation.html#_divide_bulleted_list_mf_at_end',
                                                                                                                                               'trouver/markdown/obsidian/personal/notation.py'),
```

### Comparing `trouver-0.0.3/trouver/helper.py` & `trouver-0.0.4/trouver/helper.py`

 * *Files 2% similar despite different names*

```diff
@@ -9,14 +9,15 @@
 import errno
 import glob
 from graphlib import TopologicalSorter
 from itertools import product
 import os
 from os import PathLike
 from pathlib import Path
+from pathvalidate import sanitize_filename
 import platform
 import re
 from typing import Callable, Optional, Pattern, Sequence, Union
 
 from deprecated import deprecated
 from natsort import natsorted
 
@@ -158,16 +159,18 @@
         text, pattern='\*\*\$\$[^$]+\$\$\*\*|\*\*\$[^$]+\$\*\*')
     # I previous used this, but it was not picking up notation LaTeX str
     # containing asterisks, e.g. `**$\pi^*$**``, `**$\pi_*$**`.`
     return find_regex_in_text(
         text, pattern='\*\*\$\$[^*$]+\$\$\*\*|\*\*\$[^*$]+\$\*\*')
 
 
-def definition_asterisk_indices(text: str) -> list[tuple[int]]:
-    """Returns the indices of definition text surrounded by double asterisks.
+def definition_asterisk_indices(
+        text: str # The str in which to find the indices of the definitions surrounded by double asterisks.
+        ) -> list[tuple[int]]: # Each tuple is of the form `(start,end)`, where `text[start:end]` is a substring in `text` surrounded by double asterisks, including the double asterisks.
+    """Return the indices of definition text surrounded by double asterisks.
     
     A double-asterisk-surrounded-text is a definition almost always
     when it is not purely LaTeX math mode text.
     
     Assumes that no LaTeX math mode string has double asterisks and that no
     LaTeX math mode string has the dollar sign character within it.
     """
@@ -559,8 +562,9 @@
 def latex_to_path_accepted_string(latex: str) -> str:
     """Convert a latex string to a path accepted string
     """
     for to_remove in TO_REMOVE:
         latex, _ = re.subn(re.escape(to_remove), '', latex)
     for to_underscore in TO_UNDERSCORE:
         latex, _ = re.subn(re.escape(to_underscore), '_', latex)
+    latex = sanitize_filename(latex)
     return latex
```

### Comparing `trouver-0.0.3/trouver/latex/convert.py` & `trouver-0.0.4/trouver/latex/convert.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,14 +1,14 @@
 # AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/16_latex.convert.ipynb.
 
 # %% auto 0
-__all__ = ['DEFAULT_NUMBERED_ENVIRONMENTS', 'DEFAULT_ENVIRONMENTS_TO_NOT_DIVIDE_ALONG', 'COMMON_SECTION_TITLES',
-           'remove_comments', 'divide_preamble', 'NoDocumentNodeError', 'find_document_node', 'environment_names_used',
-           'numbered_newtheorems_counters_in_preamble', 'numberwithins_in_preamble', 'display_names_of_environments',
-           'get_node_from_simple_text', 'swap_numbers_invoked', 'divide_latex_text',
+__all__ = ['DEFAULT_NUMBERED_ENVIRONMENTS', 'DEFAULT_ENVIRONMENTS_TO_NOT_DIVIDE_ALONG', 'UNTITLED_SECTION_TITLE',
+           'COMMON_SECTION_TITLES', 'remove_comments', 'divide_preamble', 'NoDocumentNodeError', 'find_document_node',
+           'environment_names_used', 'numbered_newtheorems_counters_in_preamble', 'numberwithins_in_preamble',
+           'display_names_of_environments', 'get_node_from_simple_text', 'swap_numbers_invoked', 'divide_latex_text',
            'section_and_subsection_titles_from_latex_parts', 'custom_commands', 'regex_pattern_detecting_command',
            'replace_command_in_text', 'replace_commands_in_text', 'replace_commands_in_latex_document',
            'adjust_common_syntax_to_markdown', 'setup_reference_from_latex_parts']
 
 # %% ../../nbs/16_latex.convert.ipynb 3
 from collections import OrderedDict
 from itertools import product
@@ -750,98 +750,136 @@
 
 
 
 
 
 
 # %% ../../nbs/16_latex.convert.ipynb 113
-def _part_is_of_section(
+def _part_starts_section(
         part: tuple[str, str]):
-    """Return `True` if `part` specifies a section, cf. `divide_latex_text`."""
+    """
+    Return `True` if `part` starts a section (explicitly),
+    cf. `divide_latex_text`.
+    """
     return part[1].startswith(r'\section')
     # node = get_node_from_simple_text(part[1])
     # return _is_section_node(node)
 
 
-def _part_is_of_subsection(
+def _part_starts_subsection(
         part: tuple[str, str]):
-    """Return `True` if `part` specifies a subsection, cf. `divide_latex_text`."""
+    """Return `True` if `part` starts a subsection, cf. `divide_latex_text`."""
     return part[1].startswith(r'\subsection')
     # node = get_node_from_simple_text(part[1])
     # return _is_subsection_node(node)
 
 # %% ../../nbs/16_latex.convert.ipynb 115
+UNTITLED_SECTION_TITLE = 'Untitled Section'
 def section_and_subsection_titles_from_latex_parts(
         parts: list[tuple[str, str]], # An output of `divide_latex_text`
         # verbose_sections: bool = False, # 
         # short_subsections: bool = False,
         # section_name: str = 'section',
         # subsection_name: str = 'subsection')\
         ) -> list[list[str]]: # Each list corresponds to a section. The first entry of the list is the title of the section and the other entries are the titles of the subsections. 
     """
     Return a list of lists of titles for the sections and subsections in `parts`
 
     Unnumbered sections get their own list. Unnumbered subsections are also included in lists.
-    All the titles are striped.
+    All the titles are striped (of leading and trailing whitespaces).
     """
     sections_and_subsections = []
     for part in parts:
        _consider_part_to_add(part, sections_and_subsections) 
     return sections_and_subsections
 
 
 def _consider_part_to_add(
         part: list[tuple[str, str]],
         sections_and_subsections: list[list[str]]):
-    """Add the title of part appropriately if part is of a section or subsection."""
+    """Add the title of `part` to `sections_and_subsections`
+    if `part` starts a section or subsection."""
     title = part[0].strip()
-    if _part_is_of_section(part):
+    if _part_starts_section(part):
         sections_and_subsections.append([title])
-    elif _part_is_of_subsection(part):
+    elif _part_starts_subsection(part):
         sections_and_subsections[-1].append(title)
+    elif not sections_and_subsections:
+        # If sections and subsections is empty and the very first `part`
+        # does not explicitly start a section, then we are in an untitled
+        # section.
+        sections_and_subsections.append([UNTITLED_SECTION_TITLE])
         
 
 
-# %% ../../nbs/16_latex.convert.ipynb 121
+# %% ../../nbs/16_latex.convert.ipynb 130
 def custom_commands(
         preamble: str, # The preamble of a LaTeX document.
         ) -> list[tuple[str, int, Union[str, None], str]]: # Each tuple consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
     """
     Return a dict mapping commands (and math operators) defined in `preamble` to
     the number of arguments display text of the commands.
 
     Assumes that the newcommands only have at most one default parameter (newcommands with
     multiple default parameters are not valid in LaTeX).
 
     Ignores all comented newcommands.
     """
     preamble = remove_comments(preamble)
-    newcommand_regex = regex.compile(
-        r'(?<!%)\s*\\(?:(?:re)?newcommand|DeclareMathOperator)\s*\{\\\s*(\w+)\s*\}\s*(\[(\d+)\]\s*(?:\[(\w+)\])?)?\s*\{((?>[^{}]+|\{(?5)\})*)\}', re.MULTILINE)
+    latex_commands = _commands_from_newcommand_and_declaremathoperator(preamble)
+    # tex_commands = _commands_from_def(preamble)
+    return latex_commands
+
+
+def _commands_from_newcommand_and_declaremathoperator(
+        preamble: str, # The preamble of a LaTeX document
+        ) -> list[tuple[str, int, Union[str, None], str]]: # Each tuple consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
+    """
+    Get custom commands from invocations of `\newcommand` and `DeclareMathOperator`
+    in the preamble.
+    """
     # newcommand_regex = regex.compile(
-    #     r'(?<!%)\s*\\(?:re)?newcommand\s*\{\\\s*(\w+)\s*\}\s*(\[(\d+)\]\s*(?:\[(\w+)\])?)?\s*\{\s*(.*)\s*\}', re.MULTILINE)
+    #     r'(?<!%)\s*\\(?:(?:re)?newcommand|DeclareMathOperator)\s*\{\\\s*(\w+)\s*\}\s*(?:\[(\d+)\]\s*(?:\[(\w+)\])?)?\s*\{((?>[^{}]+|\{(?4)\})*)\}', re.MULTILINE)
+    newcommand_regex = regex.compile(
+        r'(?<!%)\s*\\(?:(?:re)?newcommand|DeclareMathOperator)\s*(?:\{\\\s*(\w+)\s*\}|\\\s*(\w+))\s*(?:\[(\d+)\]\s*(?:\[(\w+)\])?)?\s*\{((?>[^{}]+|\{(?5)\})*)\}', re.MULTILINE)
+
     commands = []
     for match in newcommand_regex.finditer(preamble):
-        name = match.group(1)
+        name_surrounded_in_parentheses = match.group(1) # e.g. \newcommand{\A}
+        name_without_parentheses = match.group(2) # e.g. \newcommand\A
         num_args = match.group(3)
         optional_default_arg = match.group(4)
         definition = match.group(5)
 
+        if name_surrounded_in_parentheses is not None:
+            name = name_surrounded_in_parentheses
+        else:
+            name = name_without_parentheses
+
         # Convert the number of arguments to an integer, if it was specified
         if num_args is not None:
             num_args = int(num_args)
         else:
             num_args = 0
 
         commands.append((name, num_args, optional_default_arg, definition))
     return commands
 
 
+# def _commands_from_def(
+#         preamble: str
+#         ) -> list[tuple[str, int, Union[str, None], str]]: # Each tuple consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
+#     """
+#     """
+#     def_regex = regex.compile(
+#         r'(?<!%)\s*\\def\s*(\\[a-z0-9]+)'
+#     )
+
 
-# %% ../../nbs/16_latex.convert.ipynb 124
+# %% ../../nbs/16_latex.convert.ipynb 133
 def regex_pattern_detecting_command(
         command_tuple: tuple[str, int, Union[None, str], str], # Consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
         ) -> regex.Pattern:
     """Return a `regex.pattern` object (not a `re.pattern` object) detecting
     the command with the specified number of parameters, optional argument,
     and display text.
 
@@ -867,15 +905,15 @@
         pattern = f"{backslash_name}(?![^\W_])"
     return regex.compile(pattern)
 
 def _argument_detection(group_num: int):
     return "\{((?>[^{}]+|\{(?1)\})*)\}".replace("1", str(group_num))
     
 
-# %% ../../nbs/16_latex.convert.ipynb 126
+# %% ../../nbs/16_latex.convert.ipynb 135
 def replace_command_in_text(
         text: str,
         command_tuple: tuple[str, int, Union[None, str], str], # Consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
     ):
     """
     Replaces all invocations of the specified command in `text` with the display text
     with the arguments used in the display text.
@@ -908,30 +946,30 @@
         replaced_string = regex.sub(command_pattern, replace_pattern, matched_string_to_replace)
         return replaced_string
     else:
         return regex.sub(command_pattern, replace_pattern, matched_string_to_replace)
 
 
 
-# %% ../../nbs/16_latex.convert.ipynb 128
+# %% ../../nbs/16_latex.convert.ipynb 137
 def replace_commands_in_text(
         text: str, # The text in which to replace the commands. This should not include the preamble of a latex document.
         command_tuples: tuple[str, int, Union[None, str], str], # An output of `custom_commands`. Each tuple Consists of 1. the name of the custom command 2. the number of parameters 3. The default argument if specified or `None` otherwise, and 4. the display text of the command.
     ) -> str:
     """
     Replaces all invocations of the specified commands in `text` with the
     display text with the arguments used in the display text.
 
     Assumes that '\1', '\2', '\3', etc. are not part of the display text. 
     """
     for command_tuple in command_tuples:
         text = replace_command_in_text(text, command_tuple)
     return text
 
-# %% ../../nbs/16_latex.convert.ipynb 130
+# %% ../../nbs/16_latex.convert.ipynb 139
 def replace_commands_in_latex_document(
         docment: str
         ) -> str:
     """Return the latex document (without the preamble) with invocations
     of custom commands/operators replaced with their display text.
 
     Assumes that all custom commands and operators are defined in the
@@ -947,47 +985,49 @@
     # Note that `command_tuple[0]` is the name of the command.
     unique_commands = {command_tuple[0]: command_tuple for command_tuple in commands} 
     for _, command_tuple in unique_commands.items():
         document = replace_command_in_text(document, command_tuple)
     return document
     
 
-# %% ../../nbs/16_latex.convert.ipynb 134
+# %% ../../nbs/16_latex.convert.ipynb 143
+# TODO: give the option to replace quotations ``'' and `enquote`, e.g. ```unlikely intersections''` into `"unlikely intersections"`
+# TODO: give the option to replace emph with `****`, e.g. ``\emph{special}``.
 def adjust_common_syntax_to_markdown(
         text) -> str:
     """
     Adjust some common syntax, such as math mode delimiters and equation/align
     environments, for Markdown.
 
     Assumes that the tokens for math mode delimiters (e.g. `\( \)` and `\[ \]`)
     are not used otherwise.
     """
     # TODO: see if I need to add more substitutions.
     text = re.sub(r'\\\(|\\\)', '$', text)
     text = re.sub(r'\\\[|\\]', '$$', text)
-    text = re.sub(r'(\\begin\{(?:align|equation)\*?\})', r'$$\1', text)
-    text = re.sub(r'(\\end\{(?:align|equation)\*?\})', r'\1$$', text)
+    text = re.sub(r'(\\begin\{(?:align|equation|eqnarray)\*?\})', r'$$\1', text)
+    text = re.sub(r'(\\end\{(?:align|equation|eqnarray)\*?\})', r'\1$$', text)
     return text
 
-# %% ../../nbs/16_latex.convert.ipynb 137
+# %% ../../nbs/16_latex.convert.ipynb 146
 def _replace_custom_commands_in_parts(
         parts: list[tuple[str, str]],
         custom_commands: list[tuple[str, int, Union[str, None], str]]
         ) -> list[tuple[str, str]]:
     return [(title, replace_commands_in_text(text, custom_commands))
             for title, text in parts]
 
 
 def _adjust_common_syntax_to_markdown_in_parts(
         parts: list[tuple[str, str]]
         ) -> list[tuple[str, str]]:
     return [(title, adjust_common_syntax_to_markdown(text))
             for title, text in parts]
 
-# %% ../../nbs/16_latex.convert.ipynb 139
+# %% ../../nbs/16_latex.convert.ipynb 148
 def _adjust_common_section_titles_in_parts(
         parts: list[tuple[str, str]],
         reference_name: str):
     """Adjust common section titles in `parts`
 
     Common section titles include, but are not limited to,
     `Introduction`, `Notations`,
@@ -1020,15 +1060,15 @@
         return title
     _, section_title = _section_title(text)
     if section_title.lower() in COMMON_SECTION_TITLES:
         return f'{title}_{reference_name}'
     else:
         return title 
 
-# %% ../../nbs/16_latex.convert.ipynb 142
+# %% ../../nbs/16_latex.convert.ipynb 151
 def _create_notes_from_parts(
         parts: list[tuple[str, str]],
         chapters: list[list[str]],
         index_note: VaultNote, # The index note of the reference that was created.
         vault: Path,
         reference_folder: Path,
         reference_name: str,
@@ -1037,14 +1077,15 @@
     """Create notes for the vault from `parts`."""
     # headings_folder_correspondence = correspond_headings_with_folder(
     #     index_note, vault)
     title_numbering_folder_map = {
         title: convert_title_to_folder_name(title)
         for section in chapters
         for title in section}
+
     current_section, current_subsection = chapters[0][0], '' # section/subsection titles
     # Dict of dict of list of str. The top level keys
     # are section titles and the corresponding values are dicts whose
     # keys are subsection titles and values are lists of bulleted links texts
     # of the form `- [[linke_to_note]], Title/identifying information` to add.
     links_to_make = {current_section: {current_subsection: []}}  
     for part in parts:
@@ -1103,21 +1144,21 @@
         ) -> tuple[str, str]:
     """
     Consider `part` for creating a new note or for updating
     `current_section` and `current_subsection`
 
     Also append to `links_to_make` for each note that is created.
     """
-    if _part_is_of_section(part):
+    if _part_starts_section(part):
         current_section = part[0]
         current_subsection = ''
         links_to_make[current_section] = {'': []}
         folder = title_numbering_folder_map[current_section]
         return current_section, current_subsection
-    elif _part_is_of_subsection(part):
+    elif _part_starts_subsection(part):
         current_subsection = part[0]
         links_to_make[current_section][current_subsection] = []
         return current_section, current_subsection
 
     created_note = _create_note_for_part(
         part, title_numbering_folder_map, vault, reference_folder,
         reference_name, template_mf, current_section, current_subsection)
@@ -1181,17 +1222,20 @@
         f'- [[{created_note.name}]], {note_title}'
     )
     
 
 
 
 
-# %% ../../nbs/16_latex.convert.ipynb 143
+# %% ../../nbs/16_latex.convert.ipynb 152
 # TODO: test parts without a subsection.
 # TODO: somehow contents before a section are not inclued. Fix this bug.
+# TODO: If section titles are completely empty, e.g. https://arxiv.org/abs/math/0212208,
+# Make section titles based on reference name.
+# TODO: give the option to not included commented out content from latex files.
 def setup_reference_from_latex_parts(
         parts: list[tuple[str, str]], # Output of `divide_latex_text`
         custom_commands: list[tuple[str, int, Union[str, None], str]], # Output of `custom_commands` applied to the preamble of the LaTeX ddocument.`
         vault: PathLike, # An Obsidian.md vault,
         location: PathLike, # The path to make the new reference folder. Relative to `vault`.
         reference_name: PathLike, # The name of the new reference.
         authors: Union[str, list[str]], # Each str is the family name of each author.
@@ -1234,14 +1278,16 @@
     file names for sections in different reference folders do not have the same name.
 
     Text/parts that precede explicitly given sections are included in the 
     first section's folder and are linked in the first section's index file.
     """
     parts = _adjust_common_section_titles_in_parts(parts, reference_name)
     chapters = section_and_subsection_titles_from_latex_parts(parts)
+    if chapters[0][0] == UNTITLED_SECTION_TITLE:
+        chapters[0][0] = f'{reference_name} {UNTITLED_SECTION_TITLE}'
     setup_folder_for_new_reference(
         reference_name, location, authors, vault, author_folder,
         references_folder, templates_folder, template_file_name,
         notation_index_template_file_name, 
         glossary_template_file_name, chapters, setup_temp_folder,
         make_second_template_file_in_reference_directory,
         copy_obsidian_configs, overwrite, confirm_overwrite, verbose)
```

### Comparing `trouver-0.0.3/trouver/markdown/markdown/file.py` & `trouver-0.0.4/trouver/markdown/markdown/file.py`

 * *Files 2% similar despite different names*

```diff
@@ -569,16 +569,24 @@
                       if part['type'] != MarkdownLineEnum.META]
     
     def has_tag(
             self,
             tag: str # The tag. Does not start with the hashtag `'#'`.
             ) -> bool:
         """
-        Return `True` if the MarkdownFile has the specified tag in its yaml
-        frontmatter meta.
+        Return `True` if the Markdown file has the specified tag in its
+        YAML frontmatter metadata.
+
+        More specifically, return `True` if the `MarkdownFile` objeect
+
+        1. has YAML frontmatter metadata,
+        2. the metadata has a `'tags'` section,, and
+        3. the `'tags'` section is a list with the specified tag.
+
+        Note that `tag` should not start with the hashtag `#` charater.
         """
         if not self.has_metadata():
             return False
         metadata = self.metadata()
         return (bool(metadata) and 'tags' in metadata
                 and tag in metadata['tags'])
     
@@ -614,24 +622,31 @@
         self.replace_metadata(metadata)
         
     def remove_tags(
             self,
             tags: list[str] # The str representing the tags. May or may not start with `'#'`, e.g. `'#_meta/definition'` or `'_meta/definition'`.
             ) -> None:
         """
-        Remove tags from the frontmatter metadata, if they exist.
+        Remove specified tags from the frontmatter metadata, if
+        the frontmatter metadata and the specified tags.
+
+        If the `MarkdownFile` object does not have a frontmatter or
+        if the frontmatter does not include a `tags` line, then
+        the `MarkdownFile` object is not modified.
         
         Assumes that this MarkdownFile object has a frontmatter and
         that the frontmatter includes a tags line.
         
         Any repeated tags are either merged into one (if the tag is 
         not in `tags`) or are removed (if the tag is in `tags`).
         """
         tags = [tag[1:] if tag.startswith('#') else tag for tag in tags]
         metadata = self.metadata()
+        if metadata is None or not 'tags' in metadata:
+            return
         set_of_tags = set(metadata['tags'])
         set_of_tags -= set(tags)
         metadata['tags'] = list(set_of_tags)
         self.replace_metadata(metadata)
     
     def replace_auto_tags_with_regular_tags(
             self, exclude: list[str] = None
```

### Comparing `trouver-0.0.3/trouver/markdown/markdown/heading.py` & `trouver-0.0.4/trouver/markdown/markdown/heading.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/footnotes.py` & `trouver-0.0.4/trouver/markdown/obsidian/footnotes.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/links.py` & `trouver-0.0.4/trouver/markdown/obsidian/links.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/authors.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/authors.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/index_notes.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/index_notes.py`

 * *Files 0% similar despite different names*

```diff
@@ -193,15 +193,15 @@
     for note in notes:
         note_folder = os.path.dirname(note.rel_path)
         if destination_folder == note_folder:
             continue
         note.move_to_folder(Path(parent_folder) / destination_folder)
 
 
-# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 22
+# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 23
 def move_information_notes_to_correct_folder_for_all_indices(
         index_of_index_notes: VaultNote, # The index note indexing other index notes; `index_of_index_notes` is intended to be an index note for an entire reference whereas the index notes are intended to correspond to chapters/sections in the reference.
         vault: PathLike,
         hints: list[PathLike] = [] # Hints on where the information notes are likely to be found at.  Each path is relative to `vault` and points to a directory.
         ) -> None:
     """
     Moves the information notes for all index notes belonging to the reference as
@@ -214,15 +214,15 @@
                    for start, end in index_files]
     for link in index_files:
         index_note_name = link.file_name
         index_note = VaultNote(vault, name=index_note_name)
         move_information_notes_to_correct_folder(
             index_note, vault, hints=hints+[index_note.rel_path])
 
-# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 32
+# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 33
 def convert_title_to_folder_name(title: str) -> str:
     # TODO: remove left/right
     """
     Returns a folder name for the given string, e.g. replaces spaces
     with underscore.
     
     **Parameters**
@@ -241,15 +241,15 @@
     for character in characters_to_remove:
         title = title.replace(character, '')
     for character in characters_to_turn_to_underscore:
         title = title.replace(character, '_')
     title = sanitize_filename(title)
     return title
 
-# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 34
+# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 35
 def convert_heading_to_folder_name(
         heading: str # Matches regex `\# (\w+?)\. (.*?)`
         ) -> str:
     """Converts a heading to a valid name for a folder.
     
     TODO Might not work correctly.
 
@@ -264,15 +264,15 @@
     except AttributeError:
         raise ValueError(
             f"`convert_heading_to_folder_name` unsuccessfully attempted"
             f" to match the following: {heading}")
         #print(heading)
     return f'{alphanumeric}_{convert_title_to_folder_name(title)}'    
 
-# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 36
+# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 37
 def make_folders_from_index_note_headers(
         index_note: VaultNote
         ) -> None:
     """
     Make folders in the same directory as index note whose names
     are the titles of the headers of the index note.
 
@@ -286,15 +286,15 @@
     directory = Path(os.path.dirname(index_note.path()))
     for folder_name in folder_names:
         try:
             os.mkdir(directory / folder_name)
         except OSError as error:
             pass
 
-# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 39
+# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 40
 # TODO: do an example of the `include_embedded_notes` paramtere.
 def get_notes_from_index_note(
         vault: PathLike, # The path to the Obsidian vault directory
         index_note: VaultNote, # The VaultNote object for the index note.
         as_vault_notes: bool = True, # If `True`, returns the ``VaultNote`` objects for the index notes. Otherwise, returns the names of these notes 
         include_embedded_notes: bool = False # If `True`, include in the list the embedded notes. Defaults to `False`.
         ) -> list[Union[str, VaultNote]]: # Either of the names of the index notes in the vault or of the index notes as VaultNote objects, depending on `as_vault_notes`.
@@ -314,15 +314,15 @@
         links = [link for link in links if not link.is_embedded]
     index_notes = [link.file_name for link in links]
     if as_vault_notes:
         index_notes = [VaultNote(vault, name=index_note)
                        for index_note in index_notes]
     return index_notes
 
-# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 45
+# %% ../../../../nbs/12_markdown.obsidian.personal.index_notes.ipynb 46
 def add_link_in_index_note_after_note_link(
         index_note: VaultNote,
         note_to_add_link_after: VaultNote,
         link_to_add: ObsidianLink) -> None:
     """
     Adds a link in the index note.
```

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/information_notes.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/information_notes.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/__init__.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/__init__.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/database_update.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/database_update.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/information_note_types.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/information_note_types.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/notation.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/notation.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/notation_identification.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/notation_identification.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,18 +1,19 @@
 # AUTOGENERATED! DO NOT EDIT! File to edit: ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb.
 
 # %% auto 0
 __all__ = ['get_latex_in_original_from_parsed_notation_note_data', 'notation_summarization_data_from_note',
-           'gather_notation_note_summaries', 'append_to_notation_note_summarization_database', 'single_input',
-           'append_column_for_single_text', 'fix_summary_formatting', 'summarize_notation',
-           'append_summary_to_notation_note']
+           'gather_notation_note_summaries', 'append_to_notation_note_summarization_database',
+           'single_input_for_notation_summarization', 'append_column_for_single_text', 'fix_summary_formatting',
+           'summarize_notation', 'append_summary_to_notation_note']
 
 # %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 3
 import os
 from os import PathLike
+from pathlib import Path
 import re
 from typing import Optional, Union
 
 import pandas as pd
 from transformers import pipeline, pipelines
 
 from .....helper import current_time_formatted_to_minutes
@@ -153,15 +154,15 @@
         main_mf: VaultNote
         ) -> bool:
     text = str(main_mf).strip()
     return len(text) > 0 and '#_meta/TODO' not in text
 
 
 
-# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 21
+# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 22
 def gather_notation_note_summaries(
         vault: PathLike,
         notes: list[VaultNote]
         ) -> pd.DataFrame: # Has columns `Time added`, `Time modified`, `Notation note name`, `Notation`, `Latex in original`, 'Summary', 'Main note name', and 'Processed main note contents'. 
     """
     Return a `pandas.DataFrame` encapsulating the data of notation note
     summaries.
@@ -178,87 +179,24 @@
     current_time = current_time_formatted_to_minutes()
     for row in summary_data:
         row['Time added'] = current_time
         row['Time modified'] = current_time
     return pd.DataFrame(summary_data)
     
 
-# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 24
-def append_to_notation_note_summarization_database(
-        vault: PathLike, # The vault freom which the data is drawn
-        file: PathLike, # The path to a CSV file
-        notes: list[VaultNote], # the notation notes to consider adding to the database. 
-        backup: bool = True # If `True`, makes a copy of `file` in the same directory and with the same name, except with an added extension of `.bak`.
-        ) -> None:
-    """
-    Either create a `csv` file containing data for information note type
-    labels or append to an existing `csv` file.
-
-    The columns of the database file are as follows:
-
-    - `Time added` - The time when the row was added.
-    - `Time modified` - The time when the labels of the row 
-    - `Notation note name` - The name of the note from which the data for the row
-      was derived.
-    - 'Notation' - The notation which is being summarized
-    - 'Latex in original' - The entry of the `latex_in_original` field of the
-      note if available, cf. `make_a_notation_note`
-    - `"Summary"` - The summary of the notation.
-    - `"Main note name"` - The name of the main note of the
-      notation note
-    - `"Processed main note contents"` - The processed contents of the
-      main note
-
-    All timestamps are in UTC time and specify time to minutes
-    (i.e. no seconds/microseconds).
-    
-    TODO: implement updating rows and rewrite the next paragraph to
-    accurately reflect the implementation. I would like the 'Notation', 'Latex in original',
-    'Summary', 'processed main note contents' to be the "pivot_cols"
-
-    If a "new" note has the same processed content as a pre-existing
-    note and anything is different about the "new" note, then update
-    the row of the existing note. In particular, the following are updated:
-    - Time modified (set to current time)
-    - Notation (overwritten)
-    - Latex in original (overwritten)
-    - Summary (overwritten)
-    - Main note name (overwritten)
-    - Processed main note contents (overwritten)
-    
-    This method assumes that all the processed content in the
-    CSV file are all distinct if the CSV file exists.
-    """
-    if not notes:
-        return
-        file = Path(file)
-    df = pd.read_csv(file) if os.path.exists(file) else None
-    # start_ID_from = max_ID(df) + 1 if not df is None else 1
-    new_df = gather_notation_note_summaries(vault, notes)
-    if new_df.empty:
-        return
-    cols = [
-        'Time added', 'Time modified', 'Notation note name',
-        'Notation', 'Latex in original', 'Summary', 'Main note name',
-        'Processed main note contents']
-    cols_to_update = [
-      'Time modified', 'Notation note name', 'Notation', 'Latex in original', 'Summary', 'Main note name']
-    append_to_database(
-        file, new_df, cols, 'Processed main note contents', cols_to_update, backup)
-
 # %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 25
 def append_to_notation_note_summarization_database(
         vault: PathLike, # The vault freom which the data is drawn
         file: PathLike, # The path to a CSV file
         notes: list[VaultNote], # the notation notes to consider adding to the database. 
         backup: bool = True # If `True`, makes a copy of `file` in the same directory and with the same name, except with an added extension of `.bak`.
         ) -> None:
     """
-    Either create a `csv` file containing data for information note type
-    labels or append to an existing `csv` file.
+    Either create a `csv` file containing data for notation note
+    summarization or append to an existing `csv` file.
 
     The columns of the database file are as follows:
 
     - `Time added` - The time when the row was added.
     - `Time modified` - The time when the labels of the row 
     - `Notation note name` - The name of the note from which the data for the row
       was derived.
@@ -289,51 +227,62 @@
     - Processed main note contents (overwritten)
     
     This method assumes that all the processed content in the
     CSV file are all distinct if the CSV file exists.
     """
     if not notes:
         return
-        file = Path(file)
+    file = Path(file)
     df = pd.read_csv(file) if os.path.exists(file) else None
     # start_ID_from = max_ID(df) + 1 if not df is None else 1
     new_df = gather_notation_note_summaries(vault, notes)
     if new_df.empty:
         return
     cols = [
         'Time added', 'Time modified', 'Notation note name',
         'Notation', 'Latex in original', 'Summary', 'Main note name',
         'Processed main note contents']
     cols_to_update = [
-      'Time modified', 'Notation note name', 'Notation', 'Latex in original', 'Summary', 'Main note name']
+      'Time modified', 'Processed main note contents', 'Notation', 'Latex in original', 'Summary', 'Main note name']
     append_to_database(
-        file, new_df, cols, 'Processed main note contents', cols_to_update, backup)
+        file, new_df, cols, 'Notation note name', cols_to_update, backup)
+# TODO: think about whether the 'Notation note name' column would make for an
+# appropriate pivot.
 
 # %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 34
-def single_input(
-        main_note_content: str, # The text from which to summarize a notation
+def single_input_for_notation_summarization(
+        main_note_content: str, # The mathematical text that introduces the notation and from which to summarize a notation.
         latex_in_original: str, # A substring in main_note_content which is a latex string in which the notation is introduced.
-        ) -> str: 
+        ) -> str:
+    """
+    Format an input for a
+    `transformers.pipelines.text2text_generation.SummarizationPipeline`
+    object to summarize a notation introduced in a mathematical text.
 
+    Note that this function is used to format data used to train/validate
+    the summarization model within the `SummarizationPipeline`.
+    """
     return f"{main_note_content}\n\nlatex_in_original: {latex_in_original}"
 
-# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 37
+# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 38
 # TODO: I wonder if I should also keep text that doesn't take 
 # Latex in original but rather the notation itself.
 def append_column_for_single_text(
         df: pd.DataFrame # Assumed to be structured just as a dataframe of a CSV file created/modified by append_to_notation_note_summarization_database``
         ) -> None:
     """Append a column `"Single text"` to the notation note summarization
     DataFrame to represent the input into an ML model as a single text
     """
     single_text_column = df.apply(
-        lambda row: single_input(row["Processed main note contents"], row["Latex in original"]), axis=1)
+        lambda row: single_input_for_notation_summarization(
+            row["Processed main note contents"], row["Latex in original"]),
+        axis=1)
     df["Single text"] = single_text_column
 
-# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 43
+# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 44
 def fix_summary_formatting(
         summary: str
         ) -> str:
     """Fix some latex formatting issues in a summarized text
     """
     summary = summary.replace(r'\ ', '\\')
     summary = summary.replace(r'{ ', r'{')
@@ -344,36 +293,36 @@
     # make `\` stick to the previous chunk of things
     # (e.g. r'd\in\mathbb{Z}_{\geq 0}`, then give it some
     # space, e.g. r'd \in \mathbb{Z}_{\geq 0}'.
     return summary
 
 
 
-# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 47
+# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 48
 def summarize_notation(
         main_content: str,
         latex_in_original: str,
         summarizer: pipelines.text2text_generation.SummarizationPipeline,
         fix_formatting: bool = True, # If `True`, run `fix_summary_formatting` on `summarizer`'s summary before retuning it.
         ) -> str:
     """Summarize a notation introduced in a mathematical text using
     a huggingface pipeline.
 
     Assumes that `main_content` is a mathematical text introducing
     a notation and that `latex_in_original` is a substring of
     `main_content` in which a notation is introduced.
     """
     summarizer_output = summarizer(
-        single_input(main_content, latex_in_original))
+        single_input_for_notation_summarization(main_content, latex_in_original))
     summary = summarizer_output[0]['summary_text']
     if fix_formatting:
         summary = fix_summary_formatting(summary)
     return summary
 
-# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 49
+# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 50
 def _escape_latex_in_original_in_metadata(notation_mf: MarkdownFile):
     """Escape the `latex_in_original` field in the metadata.
     
     Assumes that `notation_mf` is a MarkdownFile object derived
     from a notation note.
     """
     metadata = notation_mf.metadata()
@@ -384,67 +333,82 @@
         _enquote(raw_notation.replace('\\', '\\\\'))
         for raw_notation in latex_in_original]
     metadata['latex_in_original'] = latex_in_original
     notation_mf.replace_metadata(metadata)
 
 
 
-# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 51
+# %% ../../../../../nbs/25_markdown.obsidian.personal.machine_learning.notation_summarization.ipynb 52
 def append_summary_to_notation_note(
         notation_note: VaultNote,
         vault: PathLike,
-        summarizer: pipelines.text2text_generation.SummarizationPipeline,
-        main_note: Optional[VaultNote] = None # The main note from which the notation comes from. If this is `None`, then the `main_note` is obtained via the `main_of_notation` function.
+        summarizer: pipelines.text2text_generation.SummarizationPipeline, # Contains an ML model which summarizes the notation, see `summarize_notation` function.
+        main_note: Optional[VaultNote] = None, # The main note from which the notation comes from. If this is `None`, then the `main_note` is obtained via the `main_of_notation` function.
+        overwrite_previous_autogenerated_summary: bool = False # If `True`, overwrite previously autogenerated summaries
     ) -> None:
     """Summarize a notation introduced in a mathematical text
     using a huggingface pipeline and append said summarization to
     `notation_note`.
 
-    If `main_note` is `None` and no main note of `notation_note` can
-    be determined via the `main_of_notation` function, then the
-    summarization does not happen.
-
     If `notation_note` does not have a YAML frontmatter meta or
     does not have a `latex_in_original` field in its YAML frontmatter
     meta, then the actual notation is used as the `latex_in_original`.
 
-    If `notation_note` already has some content, then the
-    summarization does not happen.
+    The following describes the circumstances under which the
+    summarization does not happen:
+
+    - If `main_note` is `None` and no main note of `notation_note` can
+    be determined via the `main_of_notation` function.
+    - If `overwrite_previous_autogenerated_summary` is `False` and
+    `notation_note` has the `_auto/notation_summary` tag in its
+    YAML frontmatter meta (if available).
+    - If `notation_note` does not have a YAML frontmatter meta or 
+    the `_auto/notation_summary` tag is not present in the
+    YAML frontmatter meta and `notation_note` has nontrivial
+    content (i.e. its content is not merely of the form
+    `$<notation>$ [[<link_to_main_note|denotes]]`).
 
     If an auto-generated summary is appended, then this function
     adds an `_auto/notation_summary` tag to the notation note's
-    YAML frontmatter. This tag is intended to be used as follows:
+    YAML frontmatter, if not already present.
+    This tag is intended to be used as follows:
 
     - The presence of this tag tells the reader that the summary
       has been autogenerated by this function.
     - The `notation_summarization_data_from_note` function (and
       by extension, the `gather_notation_note_summaries` and
       `append_to_notation_note_summarization_database` functions)
       avoids gathering notation summarization data from notation
       notes marked with this tag
     - The owner of the `Obsidian.md` vault can manually make
       modifications to the notation note if necessary and remove this
       tag to indicate that the summary is appropriate to be added
       to the note summarization database.
     """
-
-    metadata, notation_str, _, notation_note_content_mf, _\
+    metadata, notation_str, main_note_name,\
+        notation_note_content_mf, _\
         = parse_notation_note(notation_note, vault)
-    if main_note is None:
-        main_note = main_of_notation(notation_note, as_note=True)
+    if main_note is None and main_note_name is not None:
+        main_note = VaultNote(vault, name=main_note_name)
+        # main_note = main_of_notation(notation_note, as_note=True)
 
     if main_note is None:
         return
     main_mf = MarkdownFile.from_vault_note(main_note)
     process_standard_information_note(main_mf, vault)
+    if (not overwrite_previous_autogenerated_summary 
+            and _metadata_dict_has_auto_notation_summary_tag(metadata)):
+        return
     notation_note_content = str(notation_note_content_mf)
-    if len(notation_note_content.strip()) != 0:
+    if (not _metadata_dict_has_auto_notation_summary_tag(metadata)
+            and len(notation_note_content.strip()) != 0):
         # TODO: warn that the notation note already had
         # contents, so no new ones were added.
         return
+    
     summary = _get_summary(metadata, notation_str, main_mf, summarizer)
     _write_summary_to_notation_note(notation_note, summary)
 
 
 def _get_summary(
         metadata, notation_str, main_mf, summarizer) -> str:
     """
@@ -467,9 +431,19 @@
     notation_note_mf.parts[-1]['line'] += summary
     notation_note_mf.add_tags(['_auto/notation_summary'])
 
     # _escape_latex_in_original_in_metadata(notation_note_mf)
     notation_note_mf.write(notation_note)
 
 
+def _metadata_dict_has_auto_notation_summary_tag(
+        metadata: Union[dict, None]):
+    """
+    This is a helper function of `append_summary_to_notation_note`.
+    """
+    return (metadata is not None
+            and 'tags' in metadata
+            and '_auto/notation_summary' in metadata['tags'])
+    
+
```

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/machine_learning/notations.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/machine_learning/notations.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/notation.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/notation.py`

 * *Files 1% similar despite different names*

```diff
@@ -629,23 +629,30 @@
     notation_notes_of_main_note = [
         VaultNote(vault, name=notation_note) for notation_note, info_note
         in notation_notes_in_folder.items()
         if main_note.name == info_note]
 
     all_latex_in_original = Multiset()
     for notat_note in notation_notes_of_main_note:
+        # TODO: assert that _latex_in_original_in_notat outputs list of str;
+        # I came across an example where it outputs a list of a list
+        # by virtue of the `latex_in_original` field of a notation note
+        # being `[[ Y(S)]]`, when it should have been `["[ Y(S)]"]` instead.
         all_latex_in_original.update(_latex_in_original_in_notat(notat_note))
     return all_latex_in_original
 
 
 MAX_NOTE_NAME_LENGTH = 80
 def _make_new_notes_from_sifted_double_asts(
         main_note: VaultNote, vault: PathLike, reference_name: str,
         notations: list[str], destination: Optional[PathLike],
         overwrite: bool, add_to_main: bool) -> list[VaultNote]:
+    # TODO: write a test for making a new note from the notation 
+    # `\begin{equation} \label{escape rate} 	G_{F_t}(z,w) = \lim_{n\to\infty} \frac{1}{d^n} \log \| F_t^n(z,w) \|, \end{equation}`
+    # in particular, test that file path has been sanitized.
     """
     Actually makes the notation notes found from the double asterisked LaTeX
     str's
     """
     # TODO: test that note names aren't too long.
     new_notes = []
     for notation in reversed(notations):
```

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/note_processing.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/note_processing.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/note_type.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/note_type.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/notes.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/notes.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/personal/reference.py` & `trouver-0.0.4/trouver/markdown/obsidian/personal/reference.py`

 * *Files 1% similar despite different names*

```diff
@@ -566,33 +566,40 @@
     temp_note = VaultNote(vault, rel_path = temp_file_path)
     temp_note.create()
 
 # %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 40
 def copy_obsidian_vault_configs(
         vault: PathLike,
         reference_directory: PathLike, # The folder into which to copy the Obsidian configs. Relative to `vault`.
-        configs_folder: PathLike # The folder containing the Obsidian configs. This is either an absolute path or relative to the current working directory.
+        configs_folder: PathLike, # The folder containing the Obsidian configs. This is either an absolute path or relative to the current working directory.
+        dirs_exist_ok: bool = False, # If `dirs_exist_ok` is `False` and `reference_directory` already exists, then a FileExistsError is raised. If `dirs_exist_ok` is true, the copying operation will continue if it encounters existing directories, and files within the destination tree will be overwritten by corresponding files from the source tree. See also the [`shutil.copytree`](https://docs.python.org/3/library/shutil.html#shutil.copytree) function.
         ) -> None:
     """
     Copy the vault's Obsidian config files into the reference directory.
+
+    **Raises**
+    - `FileExistsError`
+        - If `dirs_exist_ok` is `False` and `reference_directory` already exists.
     """
-    shutil.copytree(configs_folder, vault / reference_directory / '.obsidian')
+    shutil.copytree(
+        configs_folder, vault / reference_directory / '.obsidian',
+        dirs_exist_ok=dirs_exist_ok)
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 43
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 44
 def _obsidian_vault_plugin_configs_file(
         vault: PathLike,
         plugin_name: str, # The folder name of the Obsidian plugin. This can be found either in the `.obsidian` directory or in the `.obsidian/plugins` directory in the vault .
         plugin_is_core: bool #`True` if the plugin is a core Obsidian.md plugin. `False` if the plugin is a community plugin.
         ) -> Path:
     if plugin_is_core:
         return Path(vault) / '.obsidian' / f'{plugin_name}.json'
     else:
         return Path(vault) / '.obsidian' / 'plugins' / plugin_name / 'data.json'
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 45
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 46
 def get_obsidian_vault_plugin_configs(
         vault: PathLike,
         plugin_name: str, # The folder name of the Obsidian plugin. This can be found in the `.obsidian` directory in the vault.
         plugin_is_core: bool #`True` if the plugin is a core Obsidian.md plugin. `False` if the plugin is a community plugin.
         ) -> dict[str, Union[str, int, float, bool, None, list, dict]]: # A json dict. 
     """Obtain the JSON object representing the `data.json` file of
     an Obsidian plugin.
@@ -600,15 +607,15 @@
     This function assumes that the the Obsidian plugin exists in `vault` in that the plugin
     has a `data.json` file.
     """
     with open(_obsidian_vault_plugin_configs_file(vault, plugin_name, plugin_is_core), 'r') as file:
         return json.load(file)
     
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 47
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 48
 def modify_obsidian_vault_plugin_configs(
         vault: PathLike,
         plugin_name: str, # The folder name of the Obsidian plugin. This can be found in the `.obsidian` directory in the vault.
         plugin_is_core: bool, #`True` if the plugin is a core Obsidian.md plugin. `False` if the plugin is a community plugin.
         field: str, # The field to modify
         value: Union[str, int, float, bool, None, list, dict], # The JSON value to set the field as
         ) -> None:
@@ -620,15 +627,15 @@
 
     """
     configs = get_obsidian_vault_plugin_configs(vault, plugin_name, plugin_is_core)
     configs[field] = value
     with open(_obsidian_vault_plugin_configs_file(vault, plugin_name, plugin_is_core), 'w') as file:
         json.dump(configs, file, indent=2)
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 49
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 50
 def _modify_fast_link_edit_and_templates(
         vault: PathLike,
         reference_name: str, # The value to change the `referenceName` field in the `fast-link-edit` plugin into.
         template_location: str = '/' # The value to change the `folder` field in the `templates` plugin into.
     ) -> None:
     """Modify the `fast-link-edit` and `templates` Obsidian plugins for a vault if
     each exists."""
@@ -646,33 +653,35 @@
             vault, 'templates', True, 'folder', template_location)
     except FileNotFoundError:
         warnings.warn(
             "Attempted to modify the the new reference folder's configuration file"
             " for the `templates` plugin, but the file does not exist.",
             UserWarning)
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 51
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 52
 def copy_obsidian_vault_configs_with_nice_modifications(
         vault: PathLike,
         reference_directory: PathLike, # The folder into which to copy the Obsidian configs. Relative to `vault`.
-        configs_folder: PathLike, # The folder containing the Obsidian configs. This is either an absolute path or relative to the current working directory.
+        configs_folder: PathLike, # The folder containing the Obsidian configs to copy. This is either an absolute path or relative to the current working directory.
         reference_name: str = None, # The name of the reference and the value to change the `referenceName` field in the `fast-link-edit` plugin into. If `None`, then the reference name should be obtained as the name of `reference_directory`
-        template_location: str = '/' # The location of the template file(s) and the value to change the `folder` field in the `templates` plugin into.
+        template_location: str = '/', # The location of the template file(s) and the value to change the `folder` field in the `templates` plugin into.
+        dirs_exist_ok: bool = False, # If `dirs_exist_ok` is `False` and `reference_directory` already exists, then a FileExistsError is raised. If `dirs_exist_ok` is true, the copying operation will continue if it encounters existing directories, and files within the destination tree will be overwritten by corresponding files from the source tree. See also the [`shutil.copytree`](https://docs.python.org/3/library/shutil.html#shutil.copytree) function.
         ) -> None:
     """
     Copy the vault's Obsidian config files into the reference directory and make some nice moodifications
     """
-    copy_obsidian_vault_configs(vault, reference_directory, configs_folder)
+    copy_obsidian_vault_configs(
+        vault, reference_directory, configs_folder, dirs_exist_ok=dirs_exist_ok)
     if reference_name is None:
         reference_name = path_name_no_ext(reference_directory)
     # Note that the config file that is being modified belongs to the "subvault",
     # i.e. the reference folder.
     _modify_fast_link_edit_and_templates(vault / reference_directory, reference_name, template_location)
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 55
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 56
 # TODO: add reference link in index note of parent folder
 # TODO: Make another template file in the reference folder
 # TODO: When copying over configs, change some things.
 # TODO: add verbose option. 
 #     Done: Verbose in _make_reference_folder
 # TODO: add type hinting in hidden methods and docstrings.
 # TODO: make a method for deleting reference.
@@ -786,15 +795,15 @@
             vault, reference_directory, configs_folder)
         # Modify 
     if verbose:
         print(f'Created a new reference folder at {location}.'\
             ' Make sure to update the reference file and'\
             ' The files for new mathematicians!')
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 61
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 62
 def get_index_notes_from_subdirectory(
         vault: PathLike, # The path to the Obsidian vault directory.
         subdirectory: PathLike, # The path, relative to `vault` of the subdirectory of of the vault for the reference.
         main_index_note: bool = False, # If `True`, include the main index note for the reference. This index note should be in the directory specified by `subdirectory`.
         as_vault_notes: bool = True # If `True`, returns the ``VaultNote`` objects for the index notes.  Otherwise, returns the paths to the index notes as paths, represented by str.
         ) -> list[Union[str, VaultNote]]: # Either of the names of the index notes in the vault or of the index notes as VaultNote objects, depending on `as_vault_notes`.
     """Returns list of index note files for reference
@@ -808,15 +817,15 @@
         index_notes = [index_note for index_note in index_notes
                        if Path(os.path.dirname(index_note)) != reference_directory]
     index_notes = [os.path.relpath(index_note, vault) for index_note in index_notes]
     if as_vault_notes:
         index_notes = [VaultNote(vault, rel_path=index_note) for index_note in index_notes]
     return index_notes
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 63
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 64
 # TODO: reformat
 def get_index_notes_from_index_note(
         vault: PathLike, reference_name: str,
         as_vault_notes: bool = True) -> list[Union[str, VaultNote]]:
     """Returns the list of index notes for the reference in the order
     that they are listed in the reference's main index note.
     
@@ -855,15 +864,15 @@
     links = links_from_text(text)
     index_notes = [link.file_name for link in links]
     if as_vault_notes:
         index_notes = [VaultNote(vault, name=index_note)
                        for index_note in index_notes]
     return index_notes
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 66
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 67
 def reference_folders_in_vault(vault: PathLike) -> dict[str, str]:
     """Returns a dict of reference folders in vault.
     
     **Parameters**
     - vault - PathLike
         - The path to the Obsidian vault directory.
 
@@ -894,15 +903,15 @@
             if not os.path.exists(vault / directory /\
                                  f'_notation_{reference_name}.md'):
                 warnings.warn(f'''The notation file for this reference
                               seems misnamed: {reference_name}''')
     return reference_folders
 
 
-# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 69
+# %% ../../../../nbs/10_markdown.obsidian.personal.reference.ipynb 70
 # TODO: reformat
 def files_in_reference_folder(
         vault: PathLike, reference: str, as_list: bool = False,
         search_index_notes: bool = False,
         exclude_notes_of_type: list[PersonalNoteTypeEnum] = None)\
         -> Union[list[str], dict[str, str]]:
     """Returns a dict or list of files in a reference folder of a vault.
```

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/tags.py` & `trouver-0.0.4/trouver/markdown/obsidian/tags.py`

 * *Files identical despite different names*

### Comparing `trouver-0.0.3/trouver/markdown/obsidian/vault.py` & `trouver-0.0.4/trouver/markdown/obsidian/vault.py`

 * *Files 1% similar despite different names*

```diff
@@ -264,29 +264,38 @@
         - The name of the note in the vault. Defaults to the empty str.
             - If `None`, then the `rel_path` parameter should be used 
             to determine `self.name` instead. 
             - If not `None`, then the note must uniquely exist in the
             vault.
     - `subdirectory` - Union[PathLike, None]
     - `hints` - list[PathLike]
+
+    **Raises**
+    
+    - ValueError
+        - if `rel_path` and `name` are both `None`.
     """
     
     cache = {}
     
     # TODO: make the constructor take an optional update_cache parameter.
     def __init__(
             self,
             vault: PathLike, # The (relative or absolute) path of the Obsidian vault that the note is located in.
             rel_path: PathLike = None, # The note's path relative to the vault. If `None`, then the `name` parameter is used to determine the note instead. Defaults to `None`.
             name: str = None, # The name of the note. If `None`, then the `rel_path` parameter is used to determine the note instead. Defaults to `None` 
             subdirectory: Union[PathLike, None] = '', # The relative path to a subdirectory in the Obsidian vault. If `None`, then denotes the root of the vault. Defaults to the empty str. 
             hints: list[PathLike] = [] # Paths, relative to `subdirectory`, to directories where the note file may be found. This is for speedup. Defaults to the empty list, in which case the vault note is searched in all of `subdirectory`.
             ):
         self.vault = Path(vault)
-        assert rel_path or name
+        if rel_path is None and name is None:
+            raise ValueError(
+                "In constructing a `VaultNote` object, the parameters `rel_path`"
+                " and `name` parameters were expected to be given arguments, but"
+                " both parameters are given `None` as arguments.")
         if rel_path is not None:
             self.rel_path = str(rel_path)
             self.name = note_name_from_path(self.rel_path)
         else:
             self.name = name
             self.rel_path = None
             self.identify_rel_path(update_cache=True)
```

### Comparing `trouver-0.0.3/trouver.egg-info/PKG-INFO` & `trouver-0.0.4/trouver.egg-info/PKG-INFO`

 * *Files 3% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: trouver
-Version: 0.0.3
+Version: 0.0.4
 Summary: Create and maintain mathematical Obsidian.md notes, and gather data from them to train ML models
 Home-page: https://github.com/hyunjongkimmath/trouver
 Author: Hyun Jong Kim
 Author-email: hyunjongkim96@gmail.com
 License: Apache Software License 2.0
 Keywords: nbdev jupyter notebook python
 Platform: UNKNOWN
@@ -31,23 +31,45 @@
 - [GitHub repository](https://github.com/hyunjongkimmath/trouver#readme)
 - [Documentation website](https://hyunjongkimmath.github.io/trouver/)
 - [pypi page](https://pypi.org/project/trouver/)
 
 Mathematicians constantly need to learn and read about concepts with
 which they are unfamiliar. Keeping mathematical notes in an
 [`Obsidian.md`](https://obsidian.md/) vault can help with this learning
-process as `Obsidian.md`.
+process as `Obsidian.md` makes it easy to edit notes, link notes to one
+another, organize notes, read notes, and access notes.
+
+This library currently includes functionalities to 1. Parse LaTeX
+documents (e.g. those available on [`arxiv.org`](https://arxiv.org/))
+and divide them into reasonably lengthed parts/notes/excerpts as `.md`
+files, especially for viewing and editing on `Obsidian.md`. 2. Use a
+machine learning model to categorize the type of text each excerpt is
+(e.g. introducing definitions/notations, presenting a concept,
+presenting a proof). 3. Use a machine learning model to identify
+notations introduced in each excerpt. 4. Create accompanying notes for
+each notation as more `.md` files. 5. Use a machine learning model to
+summarize what these notations denote in the created accompanying notes.
+
+As some of these functionalities use machine learning models, they
+ultimately cannot run perfectly. Nevertheless, some of these models,
+particularly those described in 2 and 3, perform well enough that these
+functionalities are quite useful as tools to help reading mathematical
+papers.
+
+Moreover, the results of the machine learning models are recorded in the
+notes/`.md` files. One can very well correct these recorded results by
+manually editing the affected `.md` files with any file editor.
 
 ## Disclaimer
 
-At the time of this writing (01/18/2023), there is only one
+At the time of this writing (04/03/2023), there is only one
 author/contributor of this library. Nevertheless, the author often
-refers to himself as “the author”, “the authors”, or “the
-author/authors” in writing this library. Moreover, the author often uses
-the [“editorial we”](https://en.wikipedia.org/wiki/We#Editorial_we) in
+refers to himself as *the author*, *the authors*, or *the
+author/authors* in writing this library. Moreover, the author often uses
+the [*editorial we*](https://en.wikipedia.org/wiki/We#Editorial_we) in
 writing this library.
 
 Use this library at your own risk as using this library can write or
 modify files in your computer and as the documentation of some
 components of this library may be inaccurate or outdated. By using this
 library, you agree that the author/authors of this library is/are not
 responsible for any damages from this library and related components.
@@ -57,31 +79,38 @@
 changes.
 
 The author/authors of this library is/are also not affiliated with
 `Obsidian.md`, `fast.ai`, or `Hugging Face`.
 
 ## Install
 
-``` python
-# TODO Write installation instructions
-```
+We recommend having at least 3GB of free space to install `trouver` and
+related components.
 
 ``` sh
 pip install trouver
 ```
 
 You may also have to manually install other libraries which are required
 by the `fast.ai` and/or `Hugging Face` libraries.
 
+We recommend installing [Obsidian.md](https://obsidian.md/) to view,
+edit, and modify mathematical notes created by or which interact with
+`trouver`.
+
+See `how_to.install_trouver` for more details on installation.
+
 # How to use
 
+See also `tutorial.walkthrough` to set up a basic `trouver` workflow.
+
 ## Parse LaTeX documents and split them into parts
 
-`Trouver` can parse `LaTeX` documents and split them up into “parts”
-which are convenient to read in `Obsidian.md` and to take notes on. For
+`Trouver` can parse `LaTeX` documents and split them up into parts which
+are convenient to read in `Obsidian.md` and to take notes on. For
 example, the following code splits up this
 [paper](https://arxiv.org/abs/2106.10586) in creates a folder in an
 Obsidian.md vault\[^4\].
 
 ``` python
 import os
 from pathlib import Path
@@ -123,26 +152,31 @@
 ```
 
 ![The created folder in Obsidian.md looks like this in `Obsidian.md` The
 text in magenta are links, each to a file in the `Obsidian.md`
 vault](.\images/index_setup_reference_from_latex_parts_demonstration.png)
 
 While `Obsidian.md` is not strictly necessary to use `trouver` or to
-read and write the files created by `setup_reference_from_latex_parts`
+read and write the files created by
+[`setup_reference_from_latex_parts`](https://hyunjongkimmath.github.io/trouver/latex.convert.html#setup_reference_from_latex_parts)
 (in fact, any traditional file reader/writer can be used for such
 purposes), reading and writing the files on `Obsidian.md` can be
-convenient.
+convenient. Moreover, even when you use Obsidian, your data is in a
+local folder. In particular, even if `Obsidian.md` happens to get shut
+down, get bought, or change privacy policy, you will (supposedly) not
+lose access to your data.
 
 ## ML model utilities
 
 We have trained a few ML models to detect/predict and provide
-information about “short” mathematical text. These ML models are
-available on [`Hugging Face`](https://huggingface.co/) and as such, they
-can be downloaded to and used from one’s local machines. Please note
-that ML models can be large and the locations that the Hugging Face
+information about short (or at least not-too-long) mathematical text.
+These ML models are available on
+[`Hugging Face`](https://huggingface.co/) and as such, they can be
+downloaded to and used from one’s local machines. Please note that ML
+models can be large and the locations that the Hugging Face
 [Transformers](https://huggingface.co/docs/transformers/index) library
 downloads such models to can vary from machine to machine.
 
 For each of these models, we may or may not have also written some
 instructions on how to train similar models given appropriately
 formatted data[^1].
 
@@ -333,15 +367,15 @@
 
     This is what the same note looks like after predicting its note type:
 
 
     ---
     cssclass: clean-embeds
     aliases: [number_theory_reference_1_ring]
-    tags: [_meta/literature_note, _reference/number_theory_reference_1, _auto/_meta/definition]
+    tags: [_reference/number_theory_reference_1, _meta/literature_note, _auto/_meta/definition]
     ---
     # Ring[^1]
 
     A **(commutative) ring** is a set $R$, equipped with two binary operators, denoted $+$ and $\cdot$, such that the following hold:
 
     1. $R$ is an abelian group under $+$ with identity element $0$.
     2. $R$ is an commutative monoid under $\cdot$ with identity element $1$.
@@ -485,33 +519,39 @@
     ('False', tensor(0), tensor([1.0000e+00, 4.8617e-06]))
 
 ``` python
 # TODO: examples of using functions in markdown.obsidian.personal.machine_learning.notation_identifcation.
 ```
 
 Similarly as with the `information_note_type` model, `trouver` provides
-functions (namely `automatically_mark_notations`) which locate within
-notes mathematical notations that are newly introduced in the text of
-the notes and record on these notes locations of such notations (by
-surrounding double asterisks `**` to LaTeX math mode strings). Note that
-this is done by applying the `notation_identification` model’s `predict`
-method as many times on a single piece of text as there are LaTeX math
-mode strings in the text. As such, these predictions often take a long
-time.
+functions (namely
+[`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations))
+which locate within notes mathematical notations that are newly
+introduced in the text of the notes and record on these notes locations
+of such notations (by surrounding double asterisks `**` to LaTeX math
+mode strings). Note that this is done by applying the
+`notation_identification` model’s `predict` method as many times on a
+single piece of text as there are LaTeX math mode strings in the text.
+As such, these predictions often take a long time.
 
-To save time, it is recommended to apply `automatically_mark_notations`
+To save time, it is recommended to apply
+[`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
 only on notes which have the `_meta/definition` or `_meta/notation` tags
 (or `_auto/_meta/definittion` or `_auto/_meta/notation`) in their
 frontmatter YAML metadata[^2].
 
-> **Warning** The `automatically_mark_notations` function note only adds
-> double asterisks `**` to LaTeX math mode strings, but also removes
-> components such as links and footnotes from the text of the note. It
-> is recommended to only apply this function to notes whose text has not
-> been embellished with such components[^3].
+> **Warning** The
+> [`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
+> function not only adds double asterisks `**` to LaTeX math mode
+> strings, but also removes components such as links and footnotes from
+> the text of the note. It is recommended to only apply this function to
+> notes whose text has not been embellished with such components[^3].
+> Moreover, the
+> [`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
+> is currently buggy and should not be applied to the same note twice
 
 The test vault used in the below example contains a single note which
 has already been marked with the `_meta/definition` and `_meta/notation`
 notes. The following example in particular locates notations in that
 note at the very least.
 
 ``` python
@@ -589,15 +629,15 @@
 
     This is what the same note looks like after locating notations introduced:
 
 
     ---
     cssclass: clean-embeds
     aliases: [number_theory_reference_1_ring_of_integers_modulo_n]
-    tags: [_meta/literature_note, _auto/s, _auto/F, _meta/definition, _reference/number_theory_reference_1, _auto/a, _auto/e, _auto/l, _meta/notation]
+    tags: [_meta/literature_note, _auto/l, _auto/e, _auto/F, _meta/notation, _auto/a, _meta/definition, _reference/number_theory_reference_1, _auto/s]
     ---
     # Topic[^1]
     The ring of integers modulo $n$, denoted **$\mathbb{Z}/n\mathbb{Z}$** has the elements $[m]$ for each integer $m$ where $[m_1] = [m_2]$ if and only if $m_1-m_2$ is divisible by $n$. As a ring, it has the following structure:
 
     1. $[m_1] + [m_2] = [m_1+m_2]$
     2. $[m_1] \cdot [m_2] = [m_1 \cdot m_2]$.
 
@@ -652,15 +692,15 @@
 
 ``` python
 summarizer("summarize:Let us now define the upper half plane $\mathbb{H}$ as the set of all complex numbers of real part greater than $1$.\n\n\nlatex_in_original: $\mathbb{H}$")
 ```
 
     Your max_length is set to 200, but you input_length is only 54. You might consider decreasing max_length manually, e.g. summarizer('...', max_length=27)
 
-    [{'summary_text': 'the upper half plane of the complex plane $\\ mathbb{ H} $. It is defined as the set of all complex numbers of real part greater than $1$.'}]
+    [{'summary_text': 'the upper half plane of the real part greater than $1$. It is defined as the set of all complex numbers of real parts greater than $$.'}]
 
 In the above example, the summarizer determines that the notation
 `$\mathbb{H}$` introduced in the text
 
 ``` markdown
 Let us now define the upper half plane $\mathbb{H}$ as the set of all complex numbers of real part greater than $1$.
 ```
@@ -669,22 +709,23 @@
 `'the upper half plane of the complex plane $\\ mathbb{ H} $. It is defined as the set of all complex numbers of real part greater than $1$.'`.
 
 Once we mark notations introduced in information notes by surrounding
 LaTeX math mode strings with double asterisks `**` (manually and/or by
 using the `notation_identification` model, see [the section about the
 `notation_identification`
 model](#use-an-ml-model-to-find-notations-introduced-in-text) above), we
-can use the `make_notation_notes_from_double_asts` function to make
-notation notes dedicated to those introduced notations and to link these
-newly created notation notes to the information notes.
+can use the
+[`make_notation_notes_from_double_asts`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.notation.html#make_notation_notes_from_double_asts)
+function to make notation notes dedicated to those introduced notations
+and to link these newly created notation notes to the information notes.
 
 After making these notation notes, we can use the
-`append_summary_to_notation_note` function to predict what each notation
-is supposed to denote and add these predicted summaries to the notation
-notes themselves.
+[`append_summary_to_notation_note`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_summarization.html#append_summary_to_notation_note)
+function to predict what each notation is supposed to denote and add
+these predicted summaries to the notation notes themselves.
 
 For the example below, there is at least one information note with
 notations already marked with double asterisks `**`.
 
 ``` python
 from trouver.markdown.obsidian.personal.notation import make_notation_notes_from_double_asts, notation_notes_linked_in_see_also_section
 from trouver.markdown.obsidian.personal.machine_learning.notation_summarization import append_summary_to_notation_note
@@ -791,22 +832,22 @@
 
 
     ---
     detect_regex: []
     latex_in_original: [R/I]
     tags: [_auto/notation_summary]
     ---
-    $R/I$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring $R/I$ where $R$ is a ring and $I$ is an ideal. It is given by $$\begin{align*} [x]+[y] &= [x+y]\\[x],\cdot [y]$. [$][x]$ is the ring whose elements are the equivalence classes of elements of $R = [\3]$ given by 
+    $R/I$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring of the ideal $R/I$. It is the ring whose elements are the equivalence classes of elements of $R$. 
 
     ---
     detect_regex: []
     latex_in_original: ["\\sim"]
     tags: [_auto/notation_summary]
     ---
-    $\sim$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring $R/I$ given by $x\sim y$ where $R$ is a ring and $I$ is an ideal. 
+    $\sim$ [[number_theory_reference_1_Definition 2.3|denotes]] the quotient ring of the ideal $R/I$. It is the ring whose elements are the equivalence classes of elements of a ring $R$. 
 
 At the time of this writing (1/30/2023), the author of `trouver`
 believes that this summarization model could be improved upon with more
 data; thus far, this model was trained on less than 1700 data points.
 
 # How the examples/tests are structured
 
@@ -910,77 +951,44 @@
 library.
 
 `trouver` was built using [`nbdev`](https://nbdev.fast.ai/) as a
 template.
 
 # Release notes
 
-## Ver. 0
-
-#### Ver. 0.0.3
-
-- Fixed [issue \#
-  32](https://github.com/hyunjongkimmath/trouver/issues/32) in which
-  setting up an `Obsidian.md` vault folder from a LaTeX document was not
-  numbering sections and theorem-like environments correctly with a
-  theorem-like environment of the form
-  `\numbertheorem{theorem}{Theorem}[section]` was being defined.
-- Finished implementing `append_summary_to_notation_note`
-- Modified `dict_to_metadata` function to escape and enquote strings if
-  necessary to take into consideration that `yaml.safe_load` does uses
-  quotations to consider strings as escaped.
-- Fixed a bug in `notation_notes_linked_in_see_also_section` where the
-  main of notation where the `VaultNote` objects were incorrectly
-  constructed by passing an argument to the `rel_path` parameter as
-  opposed to the `name` parameter.
-- Fixed a bug in `_obsidian_vault_plugin_configs_file`; I had realized
-  that files for non-core `Obsidian.md` plugins are stored in
-  `.obsidian/plugins/<plugin_name>` in the vault directory.
-- Changed the default `template_location` argument from `'.'` to `'/'`
-  in `markdown.obsidian.personal.reference`.
-- Move `latex_to_path_accepted_string` function from
-  `20_markdown.obsidian.personal.notation.ipynb` to `00_helper.ipynb`
-- Modify `_consider_part_to_add` in `16_latex.convert` so that
-  multi-line section titles in LaTeX documents get parsed as single-line
-  titles
-- Modify `convert_title_to_folder_name` in
-  `12_markdown.obsidian.personal.index_notes.ipynb` and
-  `_create_note_for_part` in `16_latex.convert.ipynb` to use
-  `sanitize_filename`
-
-#### Ver. 0.0.2
-
-- I made the mistake of note including much of the contents of
-  `index.ipynb` in the `pypi` library release, so that should be fixed..
-
-#### Ver. 0.0.1
-
-- Initial release
+See `release_notes`.
 
 [^1]: Given time, the author of `trouver` eventually plans on writing
     instructions on training each of the models.
 
 [^2]: At the time of this writing (1/30/2023), the
     `information_note_type` model is fairly good at telling when a note
     introduces a definition or a notation, but will often conflate the
     two. In other words, the model may predict that a note ought to have
     the `_meta/definition` tag assigned to it when the `_meta/notation`
     tag should be assigned to it and vice versa, but the model will
     fairly usually assign at least one of the tags when the note
     introduces a definition or a notation and will assign neither of the
     tags when the note does not introduce a definition or a notation.
 
-[^3]: More precisely, `automatically_mark_notations` first applies
-    `process_standard_information_note` to a `MarkdownFile` object
-    constructed from the `VaultNote` object to roughly obtain the “raw
-    text” of the note, uses that raw text to locate notations, marks the
-    notations in the raw text, and then replaces the text from the note
-    with the raw text with notations marked. In the process of obtaining
-    the “raw text”, the `process_standard_information_note` function
-    removes components such as links and footnotes from the text.
+[^3]: More precisely,
+    [`automatically_mark_notations`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.machine_learning.notation_identification.html#automatically_mark_notations)
+    first applies
+    [`process_standard_information_note`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.note_processing.html#process_standard_information_note)
+    to a
+    [`MarkdownFile`](https://hyunjongkimmath.github.io/trouver/markdown.markdown.file.html#markdownfile)
+    object constructed from the
+    [`VaultNote`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.vault.html#vaultnote)
+    object to roughly obtain the *raw text* of the note, uses that raw
+    text to locate notations, marks the notations in the raw text, and
+    then replaces the text from the note with the raw text with
+    notations marked. In the process of obtaining the raw text, the
+    [`process_standard_information_note`](https://hyunjongkimmath.github.io/trouver/markdown.obsidian.personal.note_processing.html#process_standard_information_note)
+    function removes components such as links and footnotes from the
+    text.
 
 [^4]: There seems to be a bug in the above example where inexplicable
     tags (e.g. `_auto/s`, `_auto/a`) are added to the note along with
     the double asterisks `**`. This issue is reported as [Issue
     \#33](https://github.com/hyunjongkimmath/trouver/issues/33).
 
 [^5]: cf. [nbdev’s End-To-End
```

### Comparing `trouver-0.0.3/trouver.egg-info/SOURCES.txt` & `trouver-0.0.4/trouver.egg-info/SOURCES.txt`

 * *Files 0% similar despite different names*

```diff
@@ -1,14 +1,15 @@
 LICENSE
 MANIFEST.in
 README.md
 settings.ini
 setup.py
 trouver/__init__.py
 trouver/_modidx.py
+trouver/_nbdev.py
 trouver/core.py
 trouver/helper.py
 trouver.egg-info/PKG-INFO
 trouver.egg-info/SOURCES.txt
 trouver.egg-info/dependency_links.txt
 trouver.egg-info/entry_points.txt
 trouver.egg-info/not-zip-safe
@@ -32,12 +33,13 @@
 trouver/markdown/obsidian/personal/notation.py
 trouver/markdown/obsidian/personal/note_processing.py
 trouver/markdown/obsidian/personal/note_type.py
 trouver/markdown/obsidian/personal/notes.py
 trouver/markdown/obsidian/personal/reference.py
 trouver/markdown/obsidian/personal/machine_learning/__init__.py
 trouver/markdown/obsidian/personal/machine_learning/database_update.py
+trouver/markdown/obsidian/personal/machine_learning/definition_identification.py
 trouver/markdown/obsidian/personal/machine_learning/information_note_types.py
 trouver/markdown/obsidian/personal/machine_learning/notation.py
 trouver/markdown/obsidian/personal/machine_learning/notation_identification.py
 trouver/markdown/obsidian/personal/machine_learning/notation_summarization.py
 trouver/markdown/obsidian/personal/machine_learning/notations.py
```

