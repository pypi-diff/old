# Comparing `tmp/libtmux-0.8.5.tar.gz` & `tmp/libtmux-0.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/libtmux-0.8.5.tar", last modified: Sun Oct 25 16:16:18 2020, max compression
+gzip compressed data, was "dist/libtmux-0.9.0.tar", last modified: Mon Jun 14 16:20:53 2021, max compression
```

## Comparing `libtmux-0.8.5.tar` & `libtmux-0.9.0.tar`

### file list

```diff
@@ -1,45 +1,45 @@
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2020-10-25 16:16:18.000000 libtmux-0.8.5/
--rw-r--r--   0 t         (1000) t         (1000)      566 2020-10-11 13:33:12.000000 libtmux-0.8.5/.tmuxp.yaml
--rw-r--r--   0 t         (1000) t         (1000)     7824 2020-10-25 16:15:12.000000 libtmux-0.8.5/CHANGES
--rw-r--r--   0 t         (1000) t         (1000)     1078 2020-10-11 13:33:12.000000 libtmux-0.8.5/LICENSE
--rw-r--r--   0 t         (1000) t         (1000)      118 2020-10-11 13:33:12.000000 libtmux-0.8.5/MANIFEST.in
--rw-r--r--   0 t         (1000) t         (1000)     8234 2020-10-25 16:16:18.000000 libtmux-0.8.5/PKG-INFO
--rw-r--r--   0 t         (1000) t         (1000)     5404 2020-10-11 13:33:12.000000 libtmux-0.8.5/README.rst
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2020-10-25 16:16:18.000000 libtmux-0.8.5/docs/
--rw-r--r--   0 t         (1000) t         (1000)     4052 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/about.rst
--rw-r--r--   0 t         (1000) t         (1000)     2325 2020-10-25 16:12:33.000000 libtmux-0.8.5/docs/api.rst
--rw-r--r--   0 t         (1000) t         (1000)     1752 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/glossary.rst
--rw-r--r--   0 t         (1000) t         (1000)      103 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/history.rst
--rw-r--r--   0 t         (1000) t         (1000)      300 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/index.rst
--rw-r--r--   0 t         (1000) t         (1000)      438 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/panes.rst
--rw-r--r--   0 t         (1000) t         (1000)     5289 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/properties.rst
--rw-r--r--   0 t         (1000) t         (1000)     8876 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/quickstart.rst
--rw-r--r--   0 t         (1000) t         (1000)      475 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/servers.rst
--rw-r--r--   0 t         (1000) t         (1000)      318 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/sessions.rst
--rw-r--r--   0 t         (1000) t         (1000)     1815 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/traversal.rst
--rw-r--r--   0 t         (1000) t         (1000)      299 2020-10-11 13:33:12.000000 libtmux-0.8.5/docs/windows.rst
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2020-10-25 16:16:18.000000 libtmux-0.8.5/libtmux/
--rw-r--r--   0 t         (1000) t         (1000)      458 2020-10-25 16:15:10.000000 libtmux-0.8.5/libtmux/__about__.py
--rw-r--r--   0 t         (1000) t         (1000)      314 2020-10-25 16:12:33.000000 libtmux-0.8.5/libtmux/__init__.py
--rw-r--r--   0 t         (1000) t         (1000)     2420 2020-10-25 16:06:48.000000 libtmux-0.8.5/libtmux/_compat.py
--rw-r--r--   0 t         (1000) t         (1000)    18995 2020-10-25 16:12:45.000000 libtmux-0.8.5/libtmux/common.py
--rw-r--r--   0 t         (1000) t         (1000)     1163 2020-10-11 13:33:12.000000 libtmux-0.8.5/libtmux/exc.py
--rw-r--r--   0 t         (1000) t         (1000)     1933 2020-10-11 13:33:12.000000 libtmux-0.8.5/libtmux/formats.py
--rw-r--r--   0 t         (1000) t         (1000)     7437 2020-10-25 16:12:33.000000 libtmux-0.8.5/libtmux/pane.py
--rw-r--r--   0 t         (1000) t         (1000)    15725 2020-10-25 16:12:41.000000 libtmux-0.8.5/libtmux/server.py
--rw-r--r--   0 t         (1000) t         (1000)    14168 2020-10-25 16:12:33.000000 libtmux-0.8.5/libtmux/session.py
--rw-r--r--   0 t         (1000) t         (1000)     6243 2020-10-11 13:33:12.000000 libtmux-0.8.5/libtmux/test.py
--rw-r--r--   0 t         (1000) t         (1000)    15611 2020-10-25 16:12:33.000000 libtmux-0.8.5/libtmux/window.py
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2020-10-25 16:16:18.000000 libtmux-0.8.5/libtmux.egg-info/
--rw-r--r--   0 t         (1000) t         (1000)     8234 2020-10-25 16:16:18.000000 libtmux-0.8.5/libtmux.egg-info/PKG-INFO
--rw-r--r--   0 t         (1000) t         (1000)      705 2020-10-25 16:16:18.000000 libtmux-0.8.5/libtmux.egg-info/SOURCES.txt
--rw-r--r--   0 t         (1000) t         (1000)        1 2020-10-25 16:16:18.000000 libtmux-0.8.5/libtmux.egg-info/dependency_links.txt
--rw-r--r--   0 t         (1000) t         (1000)        1 2020-10-12 13:00:53.000000 libtmux-0.8.5/libtmux.egg-info/not-zip-safe
--rw-r--r--   0 t         (1000) t         (1000)        8 2020-10-25 16:16:18.000000 libtmux-0.8.5/libtmux.egg-info/top_level.txt
--rw-r--r--   0 t         (1000) t         (1000)     2308 2020-10-25 16:15:53.000000 libtmux-0.8.5/pyproject.toml
-drwxr-xr-x   0 t         (1000) t         (1000)        0 2020-10-25 16:16:18.000000 libtmux-0.8.5/requirements/
--rw-r--r--   0 t         (1000) t         (1000)       28 2020-10-11 13:33:12.000000 libtmux-0.8.5/requirements/dev.txt
--rw-r--r--   0 t         (1000) t         (1000)       68 2020-10-11 13:33:12.000000 libtmux-0.8.5/requirements/doc.txt
--rw-r--r--   0 t         (1000) t         (1000)       29 2020-10-11 13:33:12.000000 libtmux-0.8.5/requirements/test.txt
--rw-r--r--   0 t         (1000) t         (1000)      658 2020-10-25 16:16:18.000000 libtmux-0.8.5/setup.cfg
--rw-r--r--   0 t         (1000) t         (1000)     1863 2020-10-11 13:33:12.000000 libtmux-0.8.5/setup.py
+drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-06-14 16:20:53.000000 libtmux-0.9.0/
+-rw-r--r--   0 t         (1000) t         (1000)      566 2020-11-14 13:44:34.000000 libtmux-0.9.0/.tmuxp.yaml
+-rw-r--r--   0 t         (1000) t         (1000)     8142 2021-06-14 16:20:22.000000 libtmux-0.9.0/CHANGES
+-rw-r--r--   0 t         (1000) t         (1000)     1078 2020-11-14 13:44:34.000000 libtmux-0.9.0/LICENSE
+-rw-r--r--   0 t         (1000) t         (1000)      118 2020-11-14 13:44:34.000000 libtmux-0.9.0/MANIFEST.in
+-rw-r--r--   0 t         (1000) t         (1000)     8365 2021-06-14 16:20:53.000000 libtmux-0.9.0/PKG-INFO
+-rw-r--r--   0 t         (1000) t         (1000)     5545 2021-06-14 16:04:18.000000 libtmux-0.9.0/README.rst
+drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-06-14 16:20:53.000000 libtmux-0.9.0/docs/
+-rw-r--r--   0 t         (1000) t         (1000)     4052 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/about.rst
+-rw-r--r--   0 t         (1000) t         (1000)     2325 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/api.rst
+-rw-r--r--   0 t         (1000) t         (1000)     1752 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/glossary.rst
+-rw-r--r--   0 t         (1000) t         (1000)      103 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/history.rst
+-rw-r--r--   0 t         (1000) t         (1000)      300 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/index.rst
+-rw-r--r--   0 t         (1000) t         (1000)      438 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/panes.rst
+-rw-r--r--   0 t         (1000) t         (1000)     5289 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/properties.rst
+-rw-r--r--   0 t         (1000) t         (1000)     8876 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/quickstart.rst
+-rw-r--r--   0 t         (1000) t         (1000)      475 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/servers.rst
+-rw-r--r--   0 t         (1000) t         (1000)      318 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/sessions.rst
+-rw-r--r--   0 t         (1000) t         (1000)     1815 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/traversal.rst
+-rw-r--r--   0 t         (1000) t         (1000)      299 2020-11-14 13:44:34.000000 libtmux-0.9.0/docs/windows.rst
+drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-06-14 16:20:53.000000 libtmux-0.9.0/libtmux/
+-rw-r--r--   0 t         (1000) t         (1000)      458 2021-06-14 16:19:47.000000 libtmux-0.9.0/libtmux/__about__.py
+-rw-r--r--   0 t         (1000) t         (1000)      290 2021-06-14 16:04:18.000000 libtmux-0.9.0/libtmux/__init__.py
+-rw-r--r--   0 t         (1000) t         (1000)      625 2021-06-14 16:17:53.000000 libtmux-0.9.0/libtmux/_compat.py
+-rw-r--r--   0 t         (1000) t         (1000)    18971 2021-06-14 16:14:12.000000 libtmux-0.9.0/libtmux/common.py
+-rw-r--r--   0 t         (1000) t         (1000)     1066 2021-06-14 16:04:18.000000 libtmux-0.9.0/libtmux/exc.py
+-rw-r--r--   0 t         (1000) t         (1000)     1835 2021-06-14 16:04:18.000000 libtmux-0.9.0/libtmux/formats.py
+-rw-r--r--   0 t         (1000) t         (1000)     7338 2021-06-14 16:17:53.000000 libtmux-0.9.0/libtmux/pane.py
+-rw-r--r--   0 t         (1000) t         (1000)    15624 2021-06-14 16:14:12.000000 libtmux-0.9.0/libtmux/server.py
+-rw-r--r--   0 t         (1000) t         (1000)    14033 2021-06-14 16:04:18.000000 libtmux-0.9.0/libtmux/session.py
+-rw-r--r--   0 t         (1000) t         (1000)     6140 2021-06-14 16:04:18.000000 libtmux-0.9.0/libtmux/test.py
+-rw-r--r--   0 t         (1000) t         (1000)    15513 2021-06-14 16:04:18.000000 libtmux-0.9.0/libtmux/window.py
+drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-06-14 16:20:53.000000 libtmux-0.9.0/libtmux.egg-info/
+-rw-r--r--   0 t         (1000) t         (1000)     8365 2021-06-14 16:20:53.000000 libtmux-0.9.0/libtmux.egg-info/PKG-INFO
+-rw-r--r--   0 t         (1000) t         (1000)      705 2021-06-14 16:20:53.000000 libtmux-0.9.0/libtmux.egg-info/SOURCES.txt
+-rw-r--r--   0 t         (1000) t         (1000)        1 2021-06-14 16:20:53.000000 libtmux-0.9.0/libtmux.egg-info/dependency_links.txt
+-rw-r--r--   0 t         (1000) t         (1000)        1 2020-11-26 14:36:29.000000 libtmux-0.9.0/libtmux.egg-info/not-zip-safe
+-rw-r--r--   0 t         (1000) t         (1000)        8 2021-06-14 16:20:53.000000 libtmux-0.9.0/libtmux.egg-info/top_level.txt
+-rw-r--r--   0 t         (1000) t         (1000)     1858 2021-06-14 16:19:47.000000 libtmux-0.9.0/pyproject.toml
+drwxr-xr-x   0 t         (1000) t         (1000)        0 2021-06-14 16:20:53.000000 libtmux-0.9.0/requirements/
+-rw-r--r--   0 t         (1000) t         (1000)       23 2021-06-14 16:04:18.000000 libtmux-0.9.0/requirements/dev.txt
+-rw-r--r--   0 t         (1000) t         (1000)       68 2021-06-14 16:04:18.000000 libtmux-0.9.0/requirements/doc.txt
+-rw-r--r--   0 t         (1000) t         (1000)       27 2021-06-14 16:04:18.000000 libtmux-0.9.0/requirements/test.txt
+-rw-r--r--   0 t         (1000) t         (1000)      658 2021-06-14 16:20:53.000000 libtmux-0.9.0/setup.cfg
+-rw-r--r--   0 t         (1000) t         (1000)     1814 2021-06-14 16:04:18.000000 libtmux-0.9.0/setup.py
```

### Comparing `libtmux-0.8.5/.tmuxp.yaml` & `libtmux-0.9.0/.tmuxp.yaml`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/CHANGES` & `libtmux-0.9.0/CHANGES`

 * *Files 3% similar despite different names*

```diff
@@ -4,14 +4,24 @@
 
 Here you can find the recent changes to libtmux
 
 current
 -------
 - *Insert changes/features/fixes for next release here*
 
+libtmux 0.9.0 (2021-06-14)
+--------------------------
+Python 2.7 support dropped.
+
+- :issue:`306`: chore: Remove python 2.7 support
+- :issue:`314`: chore: Python 3.x syntax tweaks
+- :issue:`312`: ci: Add tmux 3.2a to CI
+- chore: Update black to `21.6b0
+  <https://github.com/psf/black/blob/21.6b0/CHANGES.md#216b0>`_
+
 libtmux 0.8.5 (2020-10-25)
 --------------------------
 - :issue:`297`: Enchance subprocess interaction std[in|out|err]. Needed
   for interact with big buffer, fixes :issue:`251`, thank you
   @gil-obradors!
 - :issue:`303` Add ``common.get_libtmux_version`` which gives the tmux
   version as a loose constraint. Fix linking to terms inside docs, and
```

### Comparing `libtmux-0.8.5/LICENSE` & `libtmux-0.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/PKG-INFO` & `libtmux-0.9.0/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: libtmux
-Version: 0.8.5
+Version: 0.9.0
 Summary: scripting library / orm for tmux
 Home-page: https://github.com/tmux-python/libtmux
 Author: Tony Narlock
 Author-email: tony@git-pull.com
 License: MIT
 Download-URL: https://pypi.org/project/libtmux/
 Project-URL: Documentation, https://libtmux.git-pull.com
@@ -18,14 +18,19 @@
         
         it builds upon tmux's `target`_ and `formats`_ to create an object
         mapping to traverse, inspect and interact with live tmux sessions.
         
         view the `documentation`_ homepage,  `API`_ information and `architectural
         details`_.
         
+        Python 2.x will be deprecated in libtmux 0.9. The backports branch is
+        `v0.8.x`_.
+        
+        .. _v0.8.x: https://github.com/tmux-python/libtmux/tree/v0.8.x
+        
         install
         -------
         
         .. code-block:: sh
         
             $ [sudo] pip install libtmux
         
@@ -184,15 +189,15 @@
         value you get out of the project.
         
         See donation options at https://git-pull.com/support.html.
         
         Project details
         ---------------
         - tmux support: 1.8, 1.9a, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
-        - python support: 2.7, >= 3.3, pypy, pypy3
+        - python support: >= 3.5, pypy, pypy3
         - Source: https://github.com/tmux-python/libtmux
         - Docs: https://libtmux.git-pull.com
         - API: https://libtmux.git-pull.com/api.html
         - Changelog: https://libtmux.git-pull.com/history.html
         - Issues: https://github.com/tmux-python/libtmux/issues
         - Test Coverage: https://codecov.io/gh/tmux-python/libtmux
         - pypi: https://pypi.python.org/pypi/libtmux
@@ -225,14 +230,13 @@
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX
 Classifier: Operating System :: MacOS :: MacOS X
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 2.7
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: Implementation :: PyPy
 Classifier: Topic :: Utilities
 Classifier: Topic :: System :: Shells
```

### Comparing `libtmux-0.8.5/README.rst` & `libtmux-0.9.0/README.rst`

 * *Files 2% similar despite different names*

```diff
@@ -6,14 +6,19 @@
 
 it builds upon tmux's `target`_ and `formats`_ to create an object
 mapping to traverse, inspect and interact with live tmux sessions.
 
 view the `documentation`_ homepage,  `API`_ information and `architectural
 details`_.
 
+Python 2.x will be deprecated in libtmux 0.9. The backports branch is
+`v0.8.x`_.
+
+.. _v0.8.x: https://github.com/tmux-python/libtmux/tree/v0.8.x
+
 install
 -------
 
 .. code-block:: sh
 
     $ [sudo] pip install libtmux
 
@@ -172,15 +177,15 @@
 value you get out of the project.
 
 See donation options at https://git-pull.com/support.html.
 
 Project details
 ---------------
 - tmux support: 1.8, 1.9a, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
-- python support: 2.7, >= 3.3, pypy, pypy3
+- python support: >= 3.5, pypy, pypy3
 - Source: https://github.com/tmux-python/libtmux
 - Docs: https://libtmux.git-pull.com
 - API: https://libtmux.git-pull.com/api.html
 - Changelog: https://libtmux.git-pull.com/history.html
 - Issues: https://github.com/tmux-python/libtmux/issues
 - Test Coverage: https://codecov.io/gh/tmux-python/libtmux
 - pypi: https://pypi.python.org/pypi/libtmux
```

### Comparing `libtmux-0.8.5/docs/about.rst` & `libtmux-0.9.0/docs/about.rst`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/docs/api.rst` & `libtmux-0.9.0/docs/api.rst`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/docs/glossary.rst` & `libtmux-0.9.0/docs/glossary.rst`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/docs/properties.rst` & `libtmux-0.9.0/docs/properties.rst`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/docs/quickstart.rst` & `libtmux-0.9.0/docs/quickstart.rst`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/docs/traversal.rst` & `libtmux-0.9.0/docs/traversal.rst`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/libtmux/common.py` & `libtmux-0.9.0/libtmux/common.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,8 +1,7 @@
-# -*- coding: utf-8 -*-
 # flake8: NOQA W605
 """Helper methods and mixins.
 
 libtmux.common
 ~~~~~~~~~~~~~~
 
 """
```

### Comparing `libtmux-0.8.5/libtmux/exc.py` & `libtmux-0.9.0/libtmux/exc.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,15 +1,13 @@
-# -*- coding: utf-8 -*-
 """libtmux exceptions.
 
 libtmux.exc
 ~~~~~~~~~~~
 
 """
-from __future__ import absolute_import, unicode_literals, with_statement
 
 
 class LibTmuxException(Exception):
 
     """Base Exception for libtmux Errors."""
```

### Comparing `libtmux-0.8.5/libtmux/formats.py` & `libtmux-0.9.0/libtmux/formats.py`

 * *Files 10% similar despite different names*

```diff
@@ -1,19 +1,16 @@
-# -*- coding: utf-8 -*-
 """Format variables for tmux objects.
 
 libtmux.formats
 ~~~~~~~~~~~~~~~
 
 For reference: https://github.com/tmux/tmux/blob/master/format.c
 
 """
 
-from __future__ import absolute_import, unicode_literals, with_statement
-
 SESSION_FORMATS = [
     'session_name',
     'session_windows',
     'session_width',
     'session_height',
     'session_id',
     'session_created',
```

### Comparing `libtmux-0.8.5/libtmux/pane.py` & `libtmux-0.9.0/libtmux/pane.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,17 +1,14 @@
-# -*- coding: utf-8 -*-
 # flake8: NOQA W605
 """Pythonization of the :ref:`tmux(1)` pane.
 
 libtmux.pane
 ~~~~~~~~~~~~
 
 """
-from __future__ import absolute_import, unicode_literals, with_statement
-
 import logging
 
 from . import exc
 from .common import TmuxMappingObject, TmuxRelationalObject
 
 logger = logging.getLogger(__name__)
 
@@ -147,15 +144,15 @@
             self.cmd('display-message', cmd)
 
     def clear(self):
         """Clear pane."""
         self.send_keys('reset')
 
     def reset(self):
-        """Reset and clear pane history. """
+        """Reset and clear pane history."""
 
         self.cmd('send-keys', r'-R \; clear-history')
 
     def split_window(
         self, attach=False, vertical=True, start_directory=None, percent=None
     ):
         """
```

### Comparing `libtmux-0.8.5/libtmux/server.py` & `libtmux-0.9.0/libtmux/server.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,16 +1,13 @@
-# -*- coding: utf-8 -*-
 """Pythonization of the :term:`tmux(1)` server.
 
 libtmux.server
 ~~~~~~~~~~~~~~
 
 """
-from __future__ import absolute_import, unicode_literals, with_statement
-
 import logging
 import os
 
 from . import exc, formats
 from .common import (
     EnvironmentMixin,
     TmuxRelationalObject,
@@ -109,19 +106,19 @@
         .. versionchanged:: 0.8
 
             Renamed from ``.tmux`` to ``.cmd``.
         """
 
         args = list(args)
         if self.socket_name:
-            args.insert(0, '-L{0}'.format(self.socket_name))
+            args.insert(0, '-L{}'.format(self.socket_name))
         if self.socket_path:
-            args.insert(0, '-S{0}'.format(self.socket_path))
+            args.insert(0, '-S{}'.format(self.socket_path))
         if self.config_file:
-            args.insert(0, '-f{0}'.format(self.config_file))
+            args.insert(0, '-f{}'.format(self.config_file))
         if self.colors:
             if self.colors == 256:
                 args.insert(0, '-2')
             elif self.colors == 88:
                 args.insert(0, '-8')
             else:
                 raise ValueError('Server.colors must equal 88 or 256')
```

### Comparing `libtmux-0.8.5/libtmux/session.py` & `libtmux-0.9.0/libtmux/session.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,21 +1,17 @@
-# -*- coding: utf-8 -*-
 """Pythonization of the :term:`tmux(1)` session.
 
 libtmux.session
 ~~~~~~~~~~~~~~~
 
 """
-from __future__ import absolute_import, unicode_literals, with_statement
-
 import logging
 import os
 
 from . import exc, formats
-from ._compat import text_type
 from .common import (
     EnvironmentMixin,
     TmuxMappingObject,
     TmuxRelationalObject,
     handle_option_error,
     has_version,
     session_check_name,
@@ -92,15 +88,15 @@
         Notes
         -----
         .. versionchanged:: 0.8
 
             Renamed from ``.tmux`` to ``.cmd``.
         """
         # if -t is not set in any arg yet
-        if not any('-t' in text_type(x) for x in args):
+        if not any('-t' in str(x) for x in args):
             # insert -t immediately after 1st arg, as per tmux format
             new_args = [args[0]]
             new_args += ['-t', self.id]
             new_args += args[1:]
             args = new_args
         return self.server.cmd(*args, **kwargs)
```

### Comparing `libtmux-0.8.5/libtmux/test.py` & `libtmux-0.9.0/libtmux/test.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,8 @@
-# -*- coding: utf-8 -*-
 """Helper methods for libtmux and downstream libtmux libraries."""
-
-from __future__ import absolute_import, unicode_literals, with_statement
-
 import contextlib
 import logging
 import os
 import tempfile
 import time
 
 logger = logging.getLogger(__name__)
@@ -35,18 +31,18 @@
     bool
         True if time passed since retry() invoked less than seconds param.
 
     Examples
     --------
 
     >>> while retry():
-    ...      p = w.attached_pane
-    ...      p.server._update_panes()
-    ...      if p.current_path == pane_path:
-    ...          break
+    ...     p = w.attached_pane
+    ...     p.server._update_panes()
+    ...     if p.current_path == pane_path:
+    ...         break
     """
     return (lambda: time.time() < time.time() + seconds)()
 
 
 def get_test_session_name(server, prefix=TEST_SESSION_PREFIX):
     """
     Faker to create a session name that doesn't exist.
```

### Comparing `libtmux-0.8.5/libtmux/window.py` & `libtmux-0.9.0/libtmux/window.py`

 * *Files 0% similar despite different names*

```diff
@@ -1,16 +1,13 @@
-# -*- coding: utf-8 -*-
 """Pythonization of the :term:`tmux(1)` window.
 
 libtmux.window
 ~~~~~~~~~~~~~~
 
 """
-from __future__ import absolute_import, unicode_literals, with_statement
-
 import logging
 import os
 import shlex
 
 from . import exc, formats
 from .common import TmuxMappingObject, TmuxRelationalObject, handle_option_error
 from .pane import Pane
```

### Comparing `libtmux-0.8.5/libtmux.egg-info/PKG-INFO` & `libtmux-0.9.0/libtmux.egg-info/PKG-INFO`

 * *Files 4% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 1.2
 Name: libtmux
-Version: 0.8.5
+Version: 0.9.0
 Summary: scripting library / orm for tmux
 Home-page: https://github.com/tmux-python/libtmux
 Author: Tony Narlock
 Author-email: tony@git-pull.com
 License: MIT
 Download-URL: https://pypi.org/project/libtmux/
 Project-URL: Documentation, https://libtmux.git-pull.com
@@ -18,14 +18,19 @@
         
         it builds upon tmux's `target`_ and `formats`_ to create an object
         mapping to traverse, inspect and interact with live tmux sessions.
         
         view the `documentation`_ homepage,  `API`_ information and `architectural
         details`_.
         
+        Python 2.x will be deprecated in libtmux 0.9. The backports branch is
+        `v0.8.x`_.
+        
+        .. _v0.8.x: https://github.com/tmux-python/libtmux/tree/v0.8.x
+        
         install
         -------
         
         .. code-block:: sh
         
             $ [sudo] pip install libtmux
         
@@ -184,15 +189,15 @@
         value you get out of the project.
         
         See donation options at https://git-pull.com/support.html.
         
         Project details
         ---------------
         - tmux support: 1.8, 1.9a, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6
-        - python support: 2.7, >= 3.3, pypy, pypy3
+        - python support: >= 3.5, pypy, pypy3
         - Source: https://github.com/tmux-python/libtmux
         - Docs: https://libtmux.git-pull.com
         - API: https://libtmux.git-pull.com/api.html
         - Changelog: https://libtmux.git-pull.com/history.html
         - Issues: https://github.com/tmux-python/libtmux/issues
         - Test Coverage: https://codecov.io/gh/tmux-python/libtmux
         - pypi: https://pypi.python.org/pypi/libtmux
@@ -225,14 +230,13 @@
 Classifier: Development Status :: 5 - Production/Stable
 Classifier: License :: OSI Approved :: MIT License
 Classifier: Operating System :: POSIX
 Classifier: Operating System :: MacOS :: MacOS X
 Classifier: Environment :: Web Environment
 Classifier: Intended Audience :: Developers
 Classifier: Programming Language :: Python
-Classifier: Programming Language :: Python :: 2.7
 Classifier: Programming Language :: Python :: 3.5
 Classifier: Programming Language :: Python :: 3.6
 Classifier: Programming Language :: Python :: 3.7
 Classifier: Programming Language :: Python :: Implementation :: PyPy
 Classifier: Topic :: Utilities
 Classifier: Topic :: System :: Shells
```

### Comparing `libtmux-0.8.5/libtmux.egg-info/SOURCES.txt` & `libtmux-0.9.0/libtmux.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/pyproject.toml` & `libtmux-0.9.0/pyproject.toml`

 * *Files 19% similar despite different names*

```diff
@@ -1,25 +1,24 @@
 [tool.black]
 skip-string-normalization = true
 
 [tool.poetry]
 name = "libtmux"
-version = "0.8.5"
+version = "0.9.0"
 description = "scripting library / orm for tmux"
 license = "MIT"
 authors = ["Tony Narlock <tony@git-pull.com>"]
 classifiers = [
   "Development Status :: 5 - Production/Stable",
   "License :: OSI Approved :: MIT License",
   "Operating System :: POSIX",
   "Operating System :: MacOS :: MacOS X",
   "Environment :: Web Environment",
   "Intended Audience :: Developers",
   "Programming Language :: Python",
-  "Programming Language :: Python :: 2.7",
   "Programming Language :: Python :: 3.5",
   "Programming Language :: Python :: 3.6",
   "Programming Language :: Python :: 3.7",
   "Programming Language :: Python :: 3.8",
   "Programming Language :: Python :: Implementation :: PyPy",
   "Topic :: Utilities",
   "Topic :: System :: Shells"
@@ -31,52 +30,36 @@
 
 [tool.poetry.urls]
 "Bug Tracker" = "https://github.com/tmux-python/libtmux/issues"
 Documentation = "https://libtmux.git-pull.com"
 Repository = "https://github.com/tmux-python/libtmux"
 
 [tool.poetry.dependencies]
-python = "~2.7 || ^3.5"
+python = "^3.5"
 
 [tool.poetry.dev-dependencies]
 ### Docs ###
-sphinx = [
-  {version="<2", python="<3"},
-  {version="*", python=">=3"}
-]
+sphinx = "*"
 recommonmark = {version = "^0.6.0"}
 alagitpull = {version = "~0.1.0"}
 sphinx-issues = {version = "^1.2.0"}
 
 ### Testing ###
-pytest = [
-  {version="<4.7.0", python="<3"},
-  {version="*", python=">=3"}
-]
-pathlib2 = {version="<2.3.5", python="<3"}  # Untangle pytest peer-dependency
+pytest = "*"
 pytest-rerunfailures = "*"
-pytest-mock = [
-  {version="<3.0.0", python="<3"},
-  {version="*", python=">=3"}
-]
+pytest-mock = "*"
 
 ### Coverage ###
 codecov = "*"
 coverage = "*"
-pytest-cov = [
-  {version="<2.10.0", python="<3"},
-  {version="*", python=">=3"}
-]
+pytest-cov = "*"
 
 ### Format ###
-black = {version="==20.08b1", python="^3.6"}
-isort = [
-  {version="<5", python="<3.6"},
-  {version="*", python=">=3.6"}
-]
+black = {version="==21.6b0", python="^3.6.2"}
+isort = "*"
 
 ### Lint ###
 flake8 = "*"
 
 ### Deploy ###
 twine = "*"
```

### Comparing `libtmux-0.8.5/setup.cfg` & `libtmux-0.9.0/setup.cfg`

 * *Files identical despite different names*

### Comparing `libtmux-0.8.5/setup.py` & `libtmux-0.9.0/setup.py`

 * *Files 3% similar despite different names*

```diff
@@ -49,15 +49,14 @@
         "Development Status :: 5 - Production/Stable",
         "License :: OSI Approved :: MIT License",
         "Operating System :: POSIX",
         "Operating System :: MacOS :: MacOS X",
         "Environment :: Web Environment",
         "Intended Audience :: Developers",
         "Programming Language :: Python",
-        "Programming Language :: Python :: 2.7",
         "Programming Language :: Python :: 3.5",
         "Programming Language :: Python :: 3.6",
         "Programming Language :: Python :: 3.7",
         "Programming Language :: Python :: Implementation :: PyPy",
         "Topic :: Utilities",
         "Topic :: System :: Shells",
     ],
```

