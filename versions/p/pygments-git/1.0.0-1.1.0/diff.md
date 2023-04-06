# Comparing `tmp/pygments_git-1.0.0.tar.gz` & `tmp/pygments_git-1.1.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "pygments_git-1.0.0.tar", last modified: Tue Apr  4 13:13:34 2023, max compression
+gzip compressed data, was "pygments_git-1.1.0.tar", last modified: Thu Apr  6 08:53:41 2023, max compression
```

## Comparing `pygments_git-1.0.0.tar` & `pygments_git-1.1.0.tar`

### file list

```diff
@@ -1,22 +1,22 @@
-drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-04 13:13:34.842631 pygments_git-1.0.0/
--rw-r--r--   0 adamjohnson   (501) staff       (20)       87 2023-04-04 13:13:31.000000 pygments_git-1.0.0/CHANGELOG.rst
--rw-r--r--   0 adamjohnson   (501) staff       (20)     1069 2023-04-01 11:07:54.000000 pygments_git-1.0.0/LICENSE
--rw-r--r--   0 adamjohnson   (501) staff       (20)      103 2023-04-01 11:04:32.000000 pygments_git-1.0.0/MANIFEST.in
--rw-r--r--   0 adamjohnson   (501) staff       (20)     3196 2023-04-04 13:13:34.842691 pygments_git-1.0.0/PKG-INFO
--rw-r--r--   0 adamjohnson   (501) staff       (20)     2046 2023-04-01 13:40:26.000000 pygments_git-1.0.0/README.rst
--rw-r--r--   0 adamjohnson   (501) staff       (20)      448 2023-04-01 13:54:14.000000 pygments_git-1.0.0/pyproject.toml
--rw-r--r--   0 adamjohnson   (501) staff       (20)     1553 2023-04-04 13:13:34.842984 pygments_git-1.0.0/setup.cfg
-drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-04 13:13:34.840561 pygments_git-1.0.0/src/
-drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-04 13:13:34.841581 pygments_git-1.0.0/src/pygments_git/
--rw-r--r--   0 adamjohnson   (501) staff       (20)     3636 2023-04-04 13:11:58.000000 pygments_git-1.0.0/src/pygments_git/__init__.py
--rw-r--r--   0 adamjohnson   (501) staff       (20)        0 2023-04-01 11:04:33.000000 pygments_git-1.0.0/src/pygments_git/py.typed
-drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-04 13:13:34.842397 pygments_git-1.0.0/src/pygments_git.egg-info/
--rw-r--r--   0 adamjohnson   (501) staff       (20)     3196 2023-04-04 13:13:34.000000 pygments_git-1.0.0/src/pygments_git.egg-info/PKG-INFO
--rw-r--r--   0 adamjohnson   (501) staff       (20)      432 2023-04-04 13:13:34.000000 pygments_git-1.0.0/src/pygments_git.egg-info/SOURCES.txt
--rw-r--r--   0 adamjohnson   (501) staff       (20)        1 2023-04-04 13:13:34.000000 pygments_git-1.0.0/src/pygments_git.egg-info/dependency_links.txt
--rw-r--r--   0 adamjohnson   (501) staff       (20)       61 2023-04-04 13:13:34.000000 pygments_git-1.0.0/src/pygments_git.egg-info/entry_points.txt
--rw-r--r--   0 adamjohnson   (501) staff       (20)        1 2023-04-04 13:13:34.000000 pygments_git-1.0.0/src/pygments_git.egg-info/not-zip-safe
--rw-r--r--   0 adamjohnson   (501) staff       (20)        9 2023-04-04 13:13:34.000000 pygments_git-1.0.0/src/pygments_git.egg-info/requires.txt
--rw-r--r--   0 adamjohnson   (501) staff       (20)       13 2023-04-04 13:13:34.000000 pygments_git-1.0.0/src/pygments_git.egg-info/top_level.txt
-drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-04 13:13:34.842515 pygments_git-1.0.0/tests/
--rw-r--r--   0 adamjohnson   (501) staff       (20)     4011 2023-04-04 13:11:58.000000 pygments_git-1.0.0/tests/test_pygments_git.py
+drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-06 08:53:41.296082 pygments_git-1.1.0/
+-rw-r--r--   0 adamjohnson   (501) staff       (20)      293 2023-04-06 08:53:38.000000 pygments_git-1.1.0/CHANGELOG.rst
+-rw-r--r--   0 adamjohnson   (501) staff       (20)     1069 2023-04-01 11:07:54.000000 pygments_git-1.1.0/LICENSE
+-rw-r--r--   0 adamjohnson   (501) staff       (20)      103 2023-04-01 11:04:32.000000 pygments_git-1.1.0/MANIFEST.in
+-rw-r--r--   0 adamjohnson   (501) staff       (20)     4324 2023-04-06 08:53:41.296136 pygments_git-1.1.0/PKG-INFO
+-rw-r--r--   0 adamjohnson   (501) staff       (20)     3174 2023-04-06 08:51:20.000000 pygments_git-1.1.0/README.rst
+-rw-r--r--   0 adamjohnson   (501) staff       (20)      448 2023-04-01 13:54:14.000000 pygments_git-1.1.0/pyproject.toml
+-rw-r--r--   0 adamjohnson   (501) staff       (20)     1662 2023-04-06 08:53:41.296412 pygments_git-1.1.0/setup.cfg
+drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-06 08:53:41.293787 pygments_git-1.1.0/src/
+drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-06 08:53:41.295024 pygments_git-1.1.0/src/pygments_git/
+-rw-r--r--   0 adamjohnson   (501) staff       (20)     9522 2023-04-05 10:16:13.000000 pygments_git-1.1.0/src/pygments_git/__init__.py
+-rw-r--r--   0 adamjohnson   (501) staff       (20)        0 2023-04-01 11:04:33.000000 pygments_git-1.1.0/src/pygments_git/py.typed
+drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-06 08:53:41.295847 pygments_git-1.1.0/src/pygments_git.egg-info/
+-rw-r--r--   0 adamjohnson   (501) staff       (20)     4324 2023-04-06 08:53:41.000000 pygments_git-1.1.0/src/pygments_git.egg-info/PKG-INFO
+-rw-r--r--   0 adamjohnson   (501) staff       (20)      432 2023-04-06 08:53:41.000000 pygments_git-1.1.0/src/pygments_git.egg-info/SOURCES.txt
+-rw-r--r--   0 adamjohnson   (501) staff       (20)        1 2023-04-06 08:53:41.000000 pygments_git-1.1.0/src/pygments_git.egg-info/dependency_links.txt
+-rw-r--r--   0 adamjohnson   (501) staff       (20)      172 2023-04-06 08:53:41.000000 pygments_git-1.1.0/src/pygments_git.egg-info/entry_points.txt
+-rw-r--r--   0 adamjohnson   (501) staff       (20)        1 2023-04-06 08:53:41.000000 pygments_git-1.1.0/src/pygments_git.egg-info/not-zip-safe
+-rw-r--r--   0 adamjohnson   (501) staff       (20)        9 2023-04-06 08:53:41.000000 pygments_git-1.1.0/src/pygments_git.egg-info/requires.txt
+-rw-r--r--   0 adamjohnson   (501) staff       (20)       13 2023-04-06 08:53:41.000000 pygments_git-1.1.0/src/pygments_git.egg-info/top_level.txt
+drwxr-xr-x   0 adamjohnson   (501) staff       (20)        0 2023-04-06 08:53:41.295965 pygments_git-1.1.0/tests/
+-rw-r--r--   0 adamjohnson   (501) staff       (20)     7519 2023-04-05 10:19:23.000000 pygments_git-1.1.0/tests/test_pygments_git.py
```

### Comparing `pygments_git-1.0.0/LICENSE` & `pygments_git-1.1.0/LICENSE`

 * *Files identical despite different names*

### Comparing `pygments_git-1.0.0/PKG-INFO` & `pygments_git-1.1.0/PKG-INFO`

 * *Files 26% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: pygments_git
-Version: 1.0.0
+Version: 1.1.0
 Summary: Pygments lexers for Git output and files.
 Home-page: https://github.com/adamchainz/pygments-git
 Author: Adam Johnson
 Author-email: me@adamj.eu
 License: MIT
 Project-URL: Changelog, https://github.com/adamchainz/pygments-git/blob/main/CHANGELOG.rst
 Project-URL: Mastodon, https://fosstodon.org/@adamchainz
@@ -71,27 +71,54 @@
 =====
 
 With the package installed, Pygments will autodiscover the below lexers.
 
 When using Pygments directly, you can refer to them by name.
 Within Sphinx/docutils, you can refer to them in ``code-block`` directives:
 
-.. code-block:: console
+.. code-block:: restructuredtext
 
     .. code-block:: git-console
 
         $ git log --oneline
         82fbbd3 D'oh! Fix math proof
         91e9879 Aye carumba! Grammar mistake
         61c4c08 Cowabunga! Update bibliography
 
+``git-commit-edit-msg``
+-----------------------
+
+A lexer for the ``COMMIT_EDITMSG`` file that Git opens when you run ``git commit``.
+It calls out to |DiffLexer|__ for highlighting any diff, as added by |git commit --verbose|__.
+
+.. |DiffLexer| replace:: ``DiffLexer``
+__ https://pygments.org/docs/lexers/#pygments.lexers.diff.DiffLexer
+
+.. |git commit --verbose| replace:: ``git commit --verbose``
+__ https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--v
+
 ``git-console``
 ---------------
 
-A lexer for displaying interactive shell sessions with Git.
-It calls out to |BashLexer|__ for highlighting commands on lines starting with a ``$`` and |DiffLexer|__ for highlighting inline diffs.
+A lexer for interactive shell sessions with Git.
+It calls out to |BashLexer|__ for highlighting commands on lines starting with a ``$`` and |DiffLexer2|__ for highlighting inline diffs.
 
 .. |BashLexer| replace:: ``BashLexer``
 __ https://pygments.org/docs/lexers/#pygments.lexers.shell.BashLexer
 
-.. |DiffLexer| replace:: ``DiffLexer``
+.. |DiffLexer2| replace:: ``DiffLexer``
+__ https://pygments.org/docs/lexers/#pygments.lexers.diff.DiffLexer
+
+``git-rebase-todo``
+-------------------
+
+A lexer for the ``git-rebase-todo`` file that Git opens when you run |git rebase --interactive|__.
+It calls out to |BashLexer2|__ for highlighting commands on lines starting with ``x`` or ``exerc`` a ``$`` and |DiffLexer3|__ for highlighting inline diffs.
+
+.. |git rebase --interactive| replace:: ``git rebase --interactive``
+__ https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--i
+
+.. |BashLexer2| replace:: ``BashLexer``
+__ https://pygments.org/docs/lexers/#pygments.lexers.shell.BashLexer
+
+.. |DiffLexer3| replace:: ``DiffLexer``
 __ https://pygments.org/docs/lexers/#pygments.lexers.diff.DiffLexer
```

### Comparing `pygments_git-1.0.0/README.rst` & `pygments_git-1.1.0/README.rst`

 * *Files 26% similar despite different names*

```diff
@@ -42,27 +42,54 @@
 =====
 
 With the package installed, Pygments will autodiscover the below lexers.
 
 When using Pygments directly, you can refer to them by name.
 Within Sphinx/docutils, you can refer to them in ``code-block`` directives:
 
-.. code-block:: console
+.. code-block:: restructuredtext
 
     .. code-block:: git-console
 
         $ git log --oneline
         82fbbd3 D'oh! Fix math proof
         91e9879 Aye carumba! Grammar mistake
         61c4c08 Cowabunga! Update bibliography
 
+``git-commit-edit-msg``
+-----------------------
+
+A lexer for the ``COMMIT_EDITMSG`` file that Git opens when you run ``git commit``.
+It calls out to |DiffLexer|__ for highlighting any diff, as added by |git commit --verbose|__.
+
+.. |DiffLexer| replace:: ``DiffLexer``
+__ https://pygments.org/docs/lexers/#pygments.lexers.diff.DiffLexer
+
+.. |git commit --verbose| replace:: ``git commit --verbose``
+__ https://git-scm.com/docs/git-commit#Documentation/git-commit.txt--v
+
 ``git-console``
 ---------------
 
-A lexer for displaying interactive shell sessions with Git.
-It calls out to |BashLexer|__ for highlighting commands on lines starting with a ``$`` and |DiffLexer|__ for highlighting inline diffs.
+A lexer for interactive shell sessions with Git.
+It calls out to |BashLexer|__ for highlighting commands on lines starting with a ``$`` and |DiffLexer2|__ for highlighting inline diffs.
 
 .. |BashLexer| replace:: ``BashLexer``
 __ https://pygments.org/docs/lexers/#pygments.lexers.shell.BashLexer
 
-.. |DiffLexer| replace:: ``DiffLexer``
+.. |DiffLexer2| replace:: ``DiffLexer``
+__ https://pygments.org/docs/lexers/#pygments.lexers.diff.DiffLexer
+
+``git-rebase-todo``
+-------------------
+
+A lexer for the ``git-rebase-todo`` file that Git opens when you run |git rebase --interactive|__.
+It calls out to |BashLexer2|__ for highlighting commands on lines starting with ``x`` or ``exerc`` a ``$`` and |DiffLexer3|__ for highlighting inline diffs.
+
+.. |git rebase --interactive| replace:: ``git rebase --interactive``
+__ https://git-scm.com/docs/git-rebase#Documentation/git-rebase.txt--i
+
+.. |BashLexer2| replace:: ``BashLexer``
+__ https://pygments.org/docs/lexers/#pygments.lexers.shell.BashLexer
+
+.. |DiffLexer3| replace:: ``DiffLexer``
 __ https://pygments.org/docs/lexers/#pygments.lexers.diff.DiffLexer
```

### Comparing `pygments_git-1.0.0/setup.cfg` & `pygments_git-1.1.0/setup.cfg`

 * *Files 9% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 [metadata]
 name = pygments_git
-version = 1.0.0
+version = 1.1.0
 description = Pygments lexers for Git output and files.
 long_description = file: README.rst
 long_description_content_type = text/x-rst
 url = https://github.com/adamchainz/pygments-git
 author = Adam Johnson
 author_email = me@adamj.eu
 license = MIT
@@ -40,15 +40,17 @@
 zip_safe = False
 
 [options.packages.find]
 where = src
 
 [options.entry_points]
 pygments.lexers = 
-	git-console=pygments_git:GitSessionLexer
+	git-commit-edit-msg=pygments_git:GitCommitEditMsgLexer
+	git-console=pygments_git:GitBashSessionLexer
+	git-rebase-todo=pygments_git:GitRebaseTodoLexer
 
 [coverage:run]
 branch = True
 parallel = True
 source = 
 	pygments_git
 	tests
```

