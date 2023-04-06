# Comparing `tmp/plone.app.vocabularies-5.0.1.tar.gz` & `tmp/plone.app.vocabularies-5.0.2.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "plone.app.vocabularies-5.0.1.tar", last modified: Tue Mar 21 23:09:42 2023, max compression
+gzip compressed data, was "plone.app.vocabularies-5.0.2.tar", last modified: Thu Apr  6 10:33:04 2023, max compression
```

## Comparing `plone.app.vocabularies-5.0.1.tar` & `plone.app.vocabularies-5.0.2.tar`

### file list

```diff
@@ -1,55 +1,55 @@
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:09:42.387739 plone.app.vocabularies-5.0.1/
--rw-r--r--   0 maurits    (501) staff       (20)    15734 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/CHANGES.rst
--rw-r--r--   0 maurits    (501) staff       (20)       70 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/CONTRIBUTING.rst
--rw-r--r--   0 maurits    (501) staff       (20)    15220 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/LICENSE.GPL
--rw-r--r--   0 maurits    (501) staff       (20)      684 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/LICENSE.txt
--rw-r--r--   0 maurits    (501) staff       (20)      152 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/MANIFEST.in
--rw-r--r--   0 maurits    (501) staff       (20)    23595 2023-03-21 23:09:42.387874 plone.app.vocabularies-5.0.1/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)     6839 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/README.rst
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:09:42.376930 plone.app.vocabularies-5.0.1/plone/
--rw-r--r--   0 maurits    (501) staff       (20)       56 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:09:42.379226 plone.app.vocabularies-5.0.1/plone/app/
--rw-r--r--   0 maurits    (501) staff       (20)       56 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/__init__.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:09:42.385458 plone.app.vocabularies-5.0.1/plone/app/vocabularies/
--rw-r--r--   0 maurits    (501) staff       (20)     1992 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     1724 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/actions.py
--rw-r--r--   0 maurits    (501) staff       (20)    30841 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/catalog.py
--rw-r--r--   0 maurits    (501) staff       (20)     5907 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/configure.zcml
--rw-r--r--   0 maurits    (501) staff       (20)     7842 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/datetimerelated.py
--rw-r--r--   0 maurits    (501) staff       (20)      890 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/editors.py
--rw-r--r--   0 maurits    (501) staff       (20)     5449 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/groups.py
--rw-r--r--   0 maurits    (501) staff       (20)      951 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/images.py
--rw-r--r--   0 maurits    (501) staff       (20)     1735 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/interfaces.py
--rw-r--r--   0 maurits    (501) staff       (20)     4032 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/language.py
--rw-r--r--   0 maurits    (501) staff       (20)     2450 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/metadatafields.py
--rw-r--r--   0 maurits    (501) staff       (20)     9462 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/principals.py
--rw-r--r--   0 maurits    (501) staff       (20)      534 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/searchabletextsource.pt
--rw-r--r--   0 maurits    (501) staff       (20)     2926 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/security.py
--rw-r--r--   0 maurits    (501) staff       (20)     2097 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/skins.py
--rw-r--r--   0 maurits    (501) staff       (20)     1928 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/syndication.py
--rw-r--r--   0 maurits    (501) staff       (20)     3287 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/terms.py
--rw-r--r--   0 maurits    (501) staff       (20)      605 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/testing.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:09:42.387468 plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/
--rw-r--r--   0 maurits    (501) staff       (20)        0 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/__init__.py
--rw-r--r--   0 maurits    (501) staff       (20)     3859 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/base.py
--rw-r--r--   0 maurits    (501) staff       (20)      972 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_editors.py
--rw-r--r--   0 maurits    (501) staff       (20)      728 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_imagesvocabularies.py
--rw-r--r--   0 maurits    (501) staff       (20)    19195 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_principals.py
--rw-r--r--   0 maurits    (501) staff       (20)     3373 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_subjects_under_context.py
--rw-r--r--   0 maurits    (501) staff       (20)     2775 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_timezonevocabularies.py
--rw-r--r--   0 maurits    (501) staff       (20)     3515 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_vocabularies.py
--rw-r--r--   0 maurits    (501) staff       (20)    10406 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/types.py
--rw-r--r--   0 maurits    (501) staff       (20)     5586 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/users.py
--rw-r--r--   0 maurits    (501) staff       (20)      741 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/utils.py
--rw-r--r--   0 maurits    (501) staff       (20)     8080 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/plone/app/vocabularies/workflow.py
-drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-03-21 23:09:42.378912 plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/
--rw-r--r--   0 maurits    (501) staff       (20)    23595 2023-03-21 23:09:42.000000 plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/PKG-INFO
--rw-r--r--   0 maurits    (501) staff       (20)     1655 2023-03-21 23:09:42.000000 plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/SOURCES.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2023-03-21 23:09:42.000000 plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/dependency_links.txt
--rw-r--r--   0 maurits    (501) staff       (20)       16 2023-03-21 23:09:42.000000 plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/namespace_packages.txt
--rw-r--r--   0 maurits    (501) staff       (20)        1 2023-03-21 23:09:42.000000 plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/not-zip-safe
--rw-r--r--   0 maurits    (501) staff       (20)      272 2023-03-21 23:09:42.000000 plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/requires.txt
--rw-r--r--   0 maurits    (501) staff       (20)        6 2023-03-21 23:09:42.000000 plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/top_level.txt
--rw-r--r--   0 maurits    (501) staff       (20)     1797 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/pyproject.toml
--rw-r--r--   0 maurits    (501) staff       (20)      217 2023-03-21 23:09:42.388335 plone.app.vocabularies-5.0.1/setup.cfg
--rw-r--r--   0 maurits    (501) staff       (20)     1870 2023-03-21 23:09:41.000000 plone.app.vocabularies-5.0.1/setup.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:33:04.251399 plone.app.vocabularies-5.0.2/
+-rw-r--r--   0 maurits    (501) staff       (20)    15924 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/CHANGES.rst
+-rw-r--r--   0 maurits    (501) staff       (20)       70 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/CONTRIBUTING.rst
+-rw-r--r--   0 maurits    (501) staff       (20)    15220 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/LICENSE.GPL
+-rw-r--r--   0 maurits    (501) staff       (20)      684 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/LICENSE.txt
+-rw-r--r--   0 maurits    (501) staff       (20)      152 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/MANIFEST.in
+-rw-r--r--   0 maurits    (501) staff       (20)    23785 2023-04-06 10:33:04.251522 plone.app.vocabularies-5.0.2/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)     6839 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/README.rst
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:33:04.239185 plone.app.vocabularies-5.0.2/plone/
+-rw-r--r--   0 maurits    (501) staff       (20)       56 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:33:04.241459 plone.app.vocabularies-5.0.2/plone/app/
+-rw-r--r--   0 maurits    (501) staff       (20)       56 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/__init__.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:33:04.248471 plone.app.vocabularies-5.0.2/plone/app/vocabularies/
+-rw-r--r--   0 maurits    (501) staff       (20)     1992 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1724 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/actions.py
+-rw-r--r--   0 maurits    (501) staff       (20)    30846 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/catalog.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5907 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/configure.zcml
+-rw-r--r--   0 maurits    (501) staff       (20)     7842 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/datetimerelated.py
+-rw-r--r--   0 maurits    (501) staff       (20)      890 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/editors.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5449 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/groups.py
+-rw-r--r--   0 maurits    (501) staff       (20)      951 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/images.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1735 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/interfaces.py
+-rw-r--r--   0 maurits    (501) staff       (20)     4032 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/language.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2450 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/metadatafields.py
+-rw-r--r--   0 maurits    (501) staff       (20)     9462 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/principals.py
+-rw-r--r--   0 maurits    (501) staff       (20)      534 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/searchabletextsource.pt
+-rw-r--r--   0 maurits    (501) staff       (20)     2926 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/security.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2097 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/skins.py
+-rw-r--r--   0 maurits    (501) staff       (20)     1928 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/syndication.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3287 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/terms.py
+-rw-r--r--   0 maurits    (501) staff       (20)      605 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/testing.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:33:04.251102 plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/
+-rw-r--r--   0 maurits    (501) staff       (20)        0 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/__init__.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3859 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/base.py
+-rw-r--r--   0 maurits    (501) staff       (20)      972 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_editors.py
+-rw-r--r--   0 maurits    (501) staff       (20)      728 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_imagesvocabularies.py
+-rw-r--r--   0 maurits    (501) staff       (20)    19195 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_principals.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3356 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_subjects_under_context.py
+-rw-r--r--   0 maurits    (501) staff       (20)     2775 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_timezonevocabularies.py
+-rw-r--r--   0 maurits    (501) staff       (20)     3515 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_vocabularies.py
+-rw-r--r--   0 maurits    (501) staff       (20)    10406 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/types.py
+-rw-r--r--   0 maurits    (501) staff       (20)     5586 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/users.py
+-rw-r--r--   0 maurits    (501) staff       (20)      741 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/utils.py
+-rw-r--r--   0 maurits    (501) staff       (20)     8080 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/plone/app/vocabularies/workflow.py
+drwxr-xr-x   0 maurits    (501) staff       (20)        0 2023-04-06 10:33:04.241231 plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/
+-rw-r--r--   0 maurits    (501) staff       (20)    23785 2023-04-06 10:33:04.000000 plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/PKG-INFO
+-rw-r--r--   0 maurits    (501) staff       (20)     1655 2023-04-06 10:33:04.000000 plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/SOURCES.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 10:33:04.000000 plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/dependency_links.txt
+-rw-r--r--   0 maurits    (501) staff       (20)       16 2023-04-06 10:33:04.000000 plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/namespace_packages.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        1 2023-04-06 10:33:04.000000 plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/not-zip-safe
+-rw-r--r--   0 maurits    (501) staff       (20)      255 2023-04-06 10:33:04.000000 plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/requires.txt
+-rw-r--r--   0 maurits    (501) staff       (20)        6 2023-04-06 10:33:04.000000 plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/top_level.txt
+-rw-r--r--   0 maurits    (501) staff       (20)     1797 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/pyproject.toml
+-rw-r--r--   0 maurits    (501) staff       (20)      217 2023-04-06 10:33:04.251963 plone.app.vocabularies-5.0.2/setup.cfg
+-rw-r--r--   0 maurits    (501) staff       (20)     1842 2023-04-06 10:33:03.000000 plone.app.vocabularies-5.0.2/setup.py
```

### Comparing `plone.app.vocabularies-5.0.1/CHANGES.rst` & `plone.app.vocabularies-5.0.2/CHANGES.rst`

 * *Files 1% similar despite different names*

```diff
@@ -4,14 +4,25 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+5.0.2 (2023-04-06)
+------------------
+
+Bug fixes:
+
+
+- Import navigation root specific from plone.base.
+  And so remove transitive circular dependency on plone.app.layout.
+  [jensens] (#74)
+
+
 5.0.1 (2023-03-22)
 ------------------
 
 Internal:
 
 
 - Update configuration files.
@@ -376,15 +387,15 @@
 - Cleanup.
   [thet]
 
 
 2.1.15 (2014-04-11)
 -------------------
 
-- Make ``KeywordsVocabulary`` more customizeable using an ``keyword_index``
+- Make ``KeywordsVocabulary`` more customizable using an ``keyword_index``
   class variable to allow users to inherit and just override that attribute
   to build their own keyword vocabularies.
   [saily]
 
 - Add datetime related vocabularies: timezones, weekdays, months.
   This are moved from ``plone.app.event`` and extended by to be more
   complete.
```

### Comparing `plone.app.vocabularies-5.0.1/LICENSE.GPL` & `plone.app.vocabularies-5.0.2/LICENSE.GPL`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/LICENSE.txt` & `plone.app.vocabularies-5.0.2/LICENSE.txt`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/PKG-INFO` & `plone.app.vocabularies-5.0.2/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: plone.app.vocabularies
-Version: 5.0.1
+Version: 5.0.2
 Summary: Collection of generally useful vocabularies for Plone.
 Home-page: https://github.com/plone/plone.app.vocabularies
 Author: Plone Foundation
 Author-email: plone-developers@lists.sourceforge.net
 License: GPL version 2
 Keywords: Plone Zope vocabularies
 Classifier: Development Status :: 6 - Mature
@@ -234,14 +234,25 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+5.0.2 (2023-04-06)
+------------------
+
+Bug fixes:
+
+
+- Import navigation root specific from plone.base.
+  And so remove transitive circular dependency on plone.app.layout.
+  [jensens] (#74)
+
+
 5.0.1 (2023-03-22)
 ------------------
 
 Internal:
 
 
 - Update configuration files.
@@ -606,15 +617,15 @@
 - Cleanup.
   [thet]
 
 
 2.1.15 (2014-04-11)
 -------------------
 
-- Make ``KeywordsVocabulary`` more customizeable using an ``keyword_index``
+- Make ``KeywordsVocabulary`` more customizable using an ``keyword_index``
   class variable to allow users to inherit and just override that attribute
   to build their own keyword vocabularies.
   [saily]
 
 - Add datetime related vocabularies: timezones, weekdays, months.
   This are moved from ``plone.app.event`` and extended by to be more
   complete.
```

### Comparing `plone.app.vocabularies-5.0.1/README.rst` & `plone.app.vocabularies-5.0.2/README.rst`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/__init__.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/__init__.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/actions.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/actions.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/catalog.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/catalog.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 from BTrees.IIBTree import intersection
-from plone.app.layout.navigation.root import getNavigationRootObject
 from plone.app.vocabularies import SlicableVocabulary
 from plone.app.vocabularies.terms import BrowsableTerm
 from plone.app.vocabularies.terms import safe_simplevocabulary_from_values
 from plone.app.vocabularies.utils import parseQueryString
+from plone.base.navigationroot import get_navigation_root_object
 from plone.base.utils import safe_text
 from plone.memoize import request
 from plone.memoize.instance import memoize
 from plone.registry.interfaces import IRegistry
 from plone.uuid.interfaces import IUUID
 from Products.CMFCore.utils import getToolByName
 from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
@@ -473,15 +473,15 @@
     def section(self, context):
         """gets section from which subjects are used."""
         registry = queryUtility(IRegistry)
         if registry is None:
             return None
         if registry.get("plone.subjects_of_navigation_root", False):
             portal = getToolByName(context, "portal_url").getPortalObject()
-            return getNavigationRootObject(context, portal)
+            return get_navigation_root_object(context, portal)
         return None
 
     def all_keywords(self, kwfilter):
         site = getSite()
         self.catalog = getToolByName(site, "portal_catalog", None)
         if self.catalog is None:
             return SimpleVocabulary([])
@@ -643,15 +643,15 @@
             if "sort_order" in query:
                 parsed["sort_order"] = str(query["sort_order"])
 
         # If no path is specified check if we are in a sub-site and use that
         # as the path root for catalog searches
         if "path" not in parsed:
             site = getSite()
-            nav_root = getNavigationRootObject(context, site)
+            nav_root = get_navigation_root_object(context, site)
             site_path = site.getPhysicalPath()
             if nav_root and nav_root.getPhysicalPath() != site_path:
                 parsed["path"] = {
                     "query": "/".join(nav_root.getPhysicalPath()),
                     "depth": -1,
                 }
         return CatalogVocabulary.fromItems(parsed, context)
@@ -791,15 +791,15 @@
         if title_template:
             self.title_template = title_template
 
     @property
     @memoize
     def nav_root_path(self):
         site = getSite()
-        nav_root = getNavigationRootObject(site, site)
+        nav_root = get_navigation_root_object(site, site)
         return "/".join(nav_root.getPhysicalPath())
 
     def get_brain_path(self, brain):
         nav_root_path = self.nav_root_path
         path = brain.getPath()
         if path.startswith(nav_root_path):
             path = path[len(nav_root_path) :]
```

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/configure.zcml` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/configure.zcml`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/datetimerelated.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/datetimerelated.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/editors.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/editors.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/groups.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/groups.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/images.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/images.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/interfaces.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/interfaces.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/language.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/language.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/metadatafields.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/metadatafields.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/principals.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/principals.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/searchabletextsource.pt` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/searchabletextsource.pt`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/security.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/security.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/skins.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/skins.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/syndication.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/syndication.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/terms.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/terms.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/testing.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/testing.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/base.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/base.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_editors.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_editors.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_imagesvocabularies.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_imagesvocabularies.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_principals.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_principals.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_subjects_under_context.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_subjects_under_context.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,9 +1,9 @@
-from plone.app.layout.navigation.interfaces import INavigationRoot
 from plone.app.vocabularies.testing import PAVocabularies_INTEGRATION_TESTING
+from plone.base.interfaces import INavigationRoot
 from unittest import mock
 from zope.interface import alsoProvides
 
 import unittest
 
 
 class TestKeywordsUnderContext(unittest.TestCase):
```

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_timezonevocabularies.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_timezonevocabularies.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/tests/test_vocabularies.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/tests/test_vocabularies.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/types.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/types.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/users.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/users.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/utils.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/utils.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone/app/vocabularies/workflow.py` & `plone.app.vocabularies-5.0.2/plone/app/vocabularies/workflow.py`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/PKG-INFO` & `plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/PKG-INFO`

 * *Files 2% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: plone.app.vocabularies
-Version: 5.0.1
+Version: 5.0.2
 Summary: Collection of generally useful vocabularies for Plone.
 Home-page: https://github.com/plone/plone.app.vocabularies
 Author: Plone Foundation
 Author-email: plone-developers@lists.sourceforge.net
 License: GPL version 2
 Keywords: Plone Zope vocabularies
 Classifier: Development Status :: 6 - Mature
@@ -234,14 +234,25 @@
 .. You should *NOT* be adding new change log entries to this file.
    You should create a file in the news directory instead.
    For helpful instructions, please see:
    https://github.com/plone/plone.releaser/blob/master/ADD-A-NEWS-ITEM.rst
 
 .. towncrier release notes start
 
+5.0.2 (2023-04-06)
+------------------
+
+Bug fixes:
+
+
+- Import navigation root specific from plone.base.
+  And so remove transitive circular dependency on plone.app.layout.
+  [jensens] (#74)
+
+
 5.0.1 (2023-03-22)
 ------------------
 
 Internal:
 
 
 - Update configuration files.
@@ -606,15 +617,15 @@
 - Cleanup.
   [thet]
 
 
 2.1.15 (2014-04-11)
 -------------------
 
-- Make ``KeywordsVocabulary`` more customizeable using an ``keyword_index``
+- Make ``KeywordsVocabulary`` more customizable using an ``keyword_index``
   class variable to allow users to inherit and just override that attribute
   to build their own keyword vocabularies.
   [saily]
 
 - Add datetime related vocabularies: timezones, weekdays, months.
   This are moved from ``plone.app.event`` and extended by to be more
   complete.
```

### Comparing `plone.app.vocabularies-5.0.1/plone.app.vocabularies.egg-info/SOURCES.txt` & `plone.app.vocabularies-5.0.2/plone.app.vocabularies.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/pyproject.toml` & `plone.app.vocabularies-5.0.2/pyproject.toml`

 * *Files identical despite different names*

### Comparing `plone.app.vocabularies-5.0.1/setup.py` & `plone.app.vocabularies-5.0.2/setup.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 from setuptools import find_packages
 from setuptools import setup
 
 
-version = "5.0.1"
+version = "5.0.2"
 
 setup(
     name="plone.app.vocabularies",
     version=version,
     description="Collection of generally useful vocabularies for Plone.",
     long_description="{}\n{}".format(
         open("README.rst").read(), open("CHANGES.rst").read()
@@ -37,15 +37,14 @@
     zip_safe=False,
     python_requires=">=3.8",
     install_requires=[
         "BTrees",
         "Products.ZCatalog",
         "plone.app.querystring",
         "plone.base",
-        "plone.app.layout",
         "plone.memoize",
         "plone.namedfile",
         "plone.registry",
         "plone.uuid",
         "pytz",
         "setuptools",
         "z3c.formwidget.query",
```

