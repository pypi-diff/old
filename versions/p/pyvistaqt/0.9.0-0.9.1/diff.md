# Comparing `tmp/pyvistaqt-0.9.0.tar.gz` & `tmp/pyvistaqt-0.9.1.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/pyvistaqt-0.9.0.tar", last modified: Wed Apr  6 16:18:35 2022, max compression
+gzip compressed data, was "pyvistaqt-0.9.1.tar", last modified: Tue Feb  7 14:52:08 2023, max compression
```

## Comparing `pyvistaqt-0.9.0.tar` & `pyvistaqt-0.9.1.tar`

### file list

```diff
@@ -1,31 +1,80 @@
-drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/
--rw-r--r--   0 vsts      (1001) docker     (121)      776 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/AUTHORS.rst
--rw-r--r--   0 vsts      (1001) docker     (121)     1088 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/LICENSE
--rw-r--r--   0 vsts      (1001) docker     (121)      171 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/MANIFEST.in
--rw-r--r--   0 vsts      (1001) docker     (121)     5224 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/PKG-INFO
--rw-r--r--   0 vsts      (1001) docker     (121)     3607 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/README.rst
-drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/docs/
--rw-r--r--   0 vsts      (1001) docker     (121)     1010 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/docs/api_reference.rst
--rw-r--r--   0 vsts      (1001) docker     (121)     7660 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/docs/conf.py
--rw-r--r--   0 vsts      (1001) docker     (121)     2416 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/docs/index.rst
--rw-r--r--   0 vsts      (1001) docker     (121)     4577 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/docs/usage.rst
-drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/pyvistaqt/
--rwxr-xr-x   0 vsts      (1001) docker     (121)     1209 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/__init__.py
--rw-r--r--   0 vsts      (1001) docker     (121)      157 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/_version.py
--rw-r--r--   0 vsts      (1001) docker     (121)      845 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/counter.py
-drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/pyvistaqt/data/
--rw-r--r--   0 vsts      (1001) docker     (121)   107789 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/data/pyvista_logo_square.png
--rw-r--r--   0 vsts      (1001) docker     (121)     7248 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/dialog.py
--rw-r--r--   0 vsts      (1001) docker     (121)     3782 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/editor.py
--rw-r--r--   0 vsts      (1001) docker     (121)    36514 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/plotting.py
--rw-r--r--   0 vsts      (1001) docker     (121)    27580 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/rwi.py
--rw-r--r--   0 vsts      (1001) docker     (121)     1827 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/utils.py
--rw-r--r--   0 vsts      (1001) docker     (121)     1239 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/pyvistaqt/window.py
-drwxr-xr-x   0 vsts      (1001) docker     (121)        0 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/pyvistaqt.egg-info/
--rw-r--r--   0 vsts      (1001) docker     (121)     5224 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/pyvistaqt.egg-info/PKG-INFO
--rw-r--r--   0 vsts      (1001) docker     (121)      503 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/pyvistaqt.egg-info/SOURCES.txt
--rw-r--r--   0 vsts      (1001) docker     (121)        1 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/pyvistaqt.egg-info/dependency_links.txt
--rw-r--r--   0 vsts      (1001) docker     (121)       28 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/pyvistaqt.egg-info/requires.txt
--rw-r--r--   0 vsts      (1001) docker     (121)       10 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/pyvistaqt.egg-info/top_level.txt
--rw-r--r--   0 vsts      (1001) docker     (121)       38 2022-04-06 16:18:35.000000 pyvistaqt-0.9.0/setup.cfg
--rw-r--r--   0 vsts      (1001) docker     (121)     1478 2022-04-06 16:16:50.000000 pyvistaqt-0.9.0/setup.py
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.418856 pyvistaqt-0.9.1/
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.408631 pyvistaqt-0.9.1/.ci/
+-rw-r--r--   0 larsoner   (501) staff       (20)     9536 2023-01-26 13:09:07.000000 pyvistaqt-0.9.1/.ci/azure-pipelines.yml
+-rwxr-xr-x   0 larsoner   (501) staff       (20)      405 2023-02-06 19:00:44.000000 pyvistaqt-0.9.1/.ci/setup_headless_display.sh
+-rw-r--r--   0 larsoner   (501) staff       (20)      191 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/.codeclimate.yml
+-rw-r--r--   0 larsoner   (501) staff       (20)      467 2022-07-15 20:34:41.000000 pyvistaqt-0.9.1/.codespellrc
+-rw-r--r--   0 larsoner   (501) staff       (20)      207 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/.coveragerc
+-rw-r--r--   0 larsoner   (501) staff       (20)      860 2022-07-15 20:34:41.000000 pyvistaqt-0.9.1/.flake8
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.408862 pyvistaqt-0.9.1/.github/
+-rw-r--r--   0 larsoner   (501) staff       (20)      450 2022-07-15 20:34:41.000000 pyvistaqt-0.9.1/.github/dependabot.yml
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.409528 pyvistaqt-0.9.1/.github/workflows/
+-rw-r--r--   0 larsoner   (501) staff       (20)     5668 2023-02-06 16:03:06.000000 pyvistaqt-0.9.1/.github/workflows/ci.yml
+-rw-r--r--   0 larsoner   (501) staff       (20)      830 2023-01-26 13:09:07.000000 pyvistaqt-0.9.1/.github/workflows/pre-commit-update.yml
+-rw-r--r--   0 larsoner   (501) staff       (20)     1052 2023-01-26 13:09:07.000000 pyvistaqt-0.9.1/.github/workflows/pythonpackage.yml
+-rw-r--r--   0 larsoner   (501) staff       (20)      796 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/.gitignore
+-rw-r--r--   0 larsoner   (501) staff       (20)      478 2022-07-15 20:34:41.000000 pyvistaqt-0.9.1/.isort.cfg
+-rw-r--r--   0 larsoner   (501) staff       (20)      229 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/.mailmap
+-rw-r--r--   0 larsoner   (501) staff       (20)     2490 2023-01-26 13:09:07.000000 pyvistaqt-0.9.1/.pre-commit-config.yaml
+-rw-r--r--   0 larsoner   (501) staff       (20)      143 2022-07-15 20:34:41.000000 pyvistaqt-0.9.1/.pycodestyle
+-rw-r--r--   0 larsoner   (501) staff       (20)    16597 2023-02-06 16:03:06.000000 pyvistaqt-0.9.1/.pylintrc
+-rw-r--r--   0 larsoner   (501) staff       (20)      776 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/AUTHORS.rst
+-rw-r--r--   0 larsoner   (501) staff       (20)      671 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/CODE_OF_CONDUCT.md
+-rw-r--r--   0 larsoner   (501) staff       (20)      559 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/CONTRIBUTING.md
+-rw-r--r--   0 larsoner   (501) staff       (20)     1088 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/LICENSE
+-rw-r--r--   0 larsoner   (501) staff       (20)      171 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/MANIFEST.in
+-rw-r--r--   0 larsoner   (501) staff       (20)     1878 2022-07-15 20:34:41.000000 pyvistaqt-0.9.1/Makefile
+-rw-r--r--   0 larsoner   (501) staff       (20)     4407 2023-02-07 14:52:08.418689 pyvistaqt-0.9.1/PKG-INFO
+-rw-r--r--   0 larsoner   (501) staff       (20)     3607 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/README.rst
+-rw-r--r--   0 larsoner   (501) staff       (20)      394 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/codecov.yml
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.410858 pyvistaqt-0.9.1/docs/
+-rw-r--r--   0 larsoner   (501) staff       (20)      736 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/docs/Makefile
+-rw-r--r--   0 larsoner   (501) staff       (20)      419 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/docs/README.md
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.412449 pyvistaqt-0.9.1/docs/_static/
+-rw-r--r--   0 larsoner   (501) staff       (20)     1232 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/docs/_static/copybutton.css
+-rw-r--r--   0 larsoner   (501) staff       (20)   249558 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/docs/_static/pyvista_logo.png
+-rw-r--r--   0 larsoner   (501) staff       (20)   107789 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/docs/_static/pyvista_logo_square.png
+-rw-r--r--   0 larsoner   (501) staff       (20)     2023 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/docs/_static/style.css
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.412654 pyvistaqt-0.9.1/docs/_templates/
+-rw-r--r--   0 larsoner   (501) staff       (20)     1444 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/docs/_templates/layout.html
+-rw-r--r--   0 larsoner   (501) staff       (20)     1010 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/docs/api_reference.rst
+-rw-r--r--   0 larsoner   (501) staff       (20)     7660 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/docs/conf.py
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.401658 pyvistaqt-0.9.1/docs/images/
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.413508 pyvistaqt-0.9.1/docs/images/user-generated/
+-rw-r--r--   0 larsoner   (501) staff       (20)    39055 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/docs/images/user-generated/qt_multiplot.png
+-rw-r--r--   0 larsoner   (501) staff       (20)    25790 2022-05-20 17:50:54.000000 pyvistaqt-0.9.1/docs/images/user-generated/qt_plotting_sphere.png
+-rw-r--r--   0 larsoner   (501) staff       (20)     2416 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/docs/index.rst
+-rw-r--r--   0 larsoner   (501) staff       (20)     4577 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/docs/usage.rst
+-rw-r--r--   0 larsoner   (501) staff       (20)      300 2023-02-06 19:00:44.000000 pyvistaqt-0.9.1/environment.yml
+-rw-r--r--   0 larsoner   (501) staff       (20)       30 2022-07-15 20:34:41.000000 pyvistaqt-0.9.1/ignore_words.txt
+-rw-r--r--   0 larsoner   (501) staff       (20)      293 2022-07-15 20:34:41.000000 pyvistaqt-0.9.1/mypy.ini
+-rw-r--r--   0 larsoner   (501) staff       (20)      144 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/mypy_checklist.txt
+-rw-r--r--   0 larsoner   (501) staff       (20)      437 2022-07-15 20:34:41.000000 pyvistaqt-0.9.1/pyproject.toml
+-rw-r--r--   0 larsoner   (501) staff       (20)      802 2023-01-26 13:09:07.000000 pyvistaqt-0.9.1/pytest.ini
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.416341 pyvistaqt-0.9.1/pyvistaqt/
+-rwxr-xr-x   0 larsoner   (501) staff       (20)     1209 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/pyvistaqt/__init__.py
+-rw-r--r--   0 larsoner   (501) staff       (20)      157 2023-02-07 14:48:39.000000 pyvistaqt-0.9.1/pyvistaqt/_version.py
+-rw-r--r--   0 larsoner   (501) staff       (20)      845 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/pyvistaqt/counter.py
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.417231 pyvistaqt-0.9.1/pyvistaqt/data/
+-rw-r--r--   0 larsoner   (501) staff       (20)   107789 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/pyvistaqt/data/pyvista_logo_square.png
+-rw-r--r--   0 larsoner   (501) staff       (20)     7248 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/pyvistaqt/dialog.py
+-rw-r--r--   0 larsoner   (501) staff       (20)     4427 2023-01-26 13:09:07.000000 pyvistaqt-0.9.1/pyvistaqt/editor.py
+-rw-r--r--   0 larsoner   (501) staff       (20)    37582 2023-02-06 19:00:44.000000 pyvistaqt-0.9.1/pyvistaqt/plotting.py
+-rw-r--r--   0 larsoner   (501) staff       (20)    27580 2023-02-06 18:49:41.000000 pyvistaqt-0.9.1/pyvistaqt/rwi.py
+-rw-r--r--   0 larsoner   (501) staff       (20)     1827 2022-05-24 20:01:47.000000 pyvistaqt-0.9.1/pyvistaqt/utils.py
+-rw-r--r--   0 larsoner   (501) staff       (20)     1239 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/pyvistaqt/window.py
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.417095 pyvistaqt-0.9.1/pyvistaqt.egg-info/
+-rw-r--r--   0 larsoner   (501) staff       (20)     4407 2023-02-07 14:52:08.000000 pyvistaqt-0.9.1/pyvistaqt.egg-info/PKG-INFO
+-rw-r--r--   0 larsoner   (501) staff       (20)     1341 2023-02-07 14:52:08.000000 pyvistaqt-0.9.1/pyvistaqt.egg-info/SOURCES.txt
+-rw-r--r--   0 larsoner   (501) staff       (20)        1 2023-02-07 14:52:08.000000 pyvistaqt-0.9.1/pyvistaqt.egg-info/dependency_links.txt
+-rw-r--r--   0 larsoner   (501) staff       (20)       28 2023-02-07 14:52:08.000000 pyvistaqt-0.9.1/pyvistaqt.egg-info/requires.txt
+-rw-r--r--   0 larsoner   (501) staff       (20)       10 2023-02-07 14:52:08.000000 pyvistaqt-0.9.1/pyvistaqt.egg-info/top_level.txt
+-rw-r--r--   0 larsoner   (501) staff       (20)      335 2023-01-26 13:09:07.000000 pyvistaqt-0.9.1/requirements_docs.txt
+-rw-r--r--   0 larsoner   (501) staff       (20)      446 2023-02-07 14:48:39.000000 pyvistaqt-0.9.1/requirements_test.txt
+-rw-r--r--   0 larsoner   (501) staff       (20)       38 2023-02-07 14:52:08.418909 pyvistaqt-0.9.1/setup.cfg
+-rw-r--r--   0 larsoner   (501) staff       (20)     1476 2023-02-07 14:52:03.000000 pyvistaqt-0.9.1/setup.py
+drwxr-xr-x   0 larsoner   (501) staff       (20)        0 2023-02-07 14:52:08.418334 pyvistaqt-0.9.1/tests/
+-rw-r--r--   0 larsoner   (501) staff       (20)        0 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/tests/__init__.py
+-rw-r--r--   0 larsoner   (501) staff       (20)     3323 2023-01-26 13:09:07.000000 pyvistaqt-0.9.1/tests/conftest.py
+-rw-r--r--   0 larsoner   (501) staff       (20)    32146 2023-02-06 19:00:44.000000 pyvistaqt-0.9.1/tests/test_plotting.py
+-rw-r--r--   0 larsoner   (501) staff       (20)      470 2022-05-20 18:26:57.000000 pyvistaqt-0.9.1/tests/test_qt.py
```

### filetype from file(1)

```diff
@@ -1 +1 @@
-POSIX tar archive (GNU)
+POSIX tar archive
```

### Comparing `pyvistaqt-0.9.0/AUTHORS.rst` & `pyvistaqt-0.9.1/AUTHORS.rst`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/LICENSE` & `pyvistaqt-0.9.1/LICENSE`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/README.rst` & `pyvistaqt-0.9.1/README.rst`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/docs/api_reference.rst` & `pyvistaqt-0.9.1/docs/api_reference.rst`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/docs/conf.py` & `pyvistaqt-0.9.1/docs/conf.py`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/docs/index.rst` & `pyvistaqt-0.9.1/docs/index.rst`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/docs/usage.rst` & `pyvistaqt-0.9.1/docs/usage.rst`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/pyvistaqt/__init__.py` & `pyvistaqt-0.9.1/pyvistaqt/__init__.py`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/pyvistaqt/counter.py` & `pyvistaqt-0.9.1/pyvistaqt/counter.py`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/pyvistaqt/data/pyvista_logo_square.png` & `pyvistaqt-0.9.1/docs/_static/pyvista_logo_square.png`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/pyvistaqt/dialog.py` & `pyvistaqt-0.9.1/pyvistaqt/dialog.py`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/pyvistaqt/editor.py` & `pyvistaqt-0.9.1/pyvistaqt/editor.py`

 * *Files 23% similar despite different names*

```diff
@@ -1,9 +1,10 @@
 """This module contains the Qt scene editor."""
 
+import weakref
 from typing import List
 
 from pyvista import Renderer
 from qtpy.QtCore import Qt
 from qtpy.QtWidgets import (
     QCheckBox,
     QDialog,
@@ -24,14 +25,15 @@
 class Editor(QDialog):
     """Basic scene editor."""
 
     def __init__(self, parent: MainWindow, renderers: List[Renderer]) -> None:
         """Initialize the Editor."""
         super().__init__(parent=parent)
         self.renderers = renderers
+        del renderers
 
         self.tree_widget = QTreeWidget()
         self.tree_widget.setHeaderHidden(True)
         self.stacked_widget = QStackedWidget()
         self.layout = QHBoxLayout()
         self.layout.addWidget(self.tree_widget)
         self.layout.addWidget(self.stacked_widget)
@@ -74,52 +76,72 @@
         else:
             self.show()
 
 
 def _get_renderer_widget(renderer: Renderer) -> QWidget:
     widget = QWidget()
     layout = QVBoxLayout()
+    axes = QCheckBox("Axes")
+    if hasattr(renderer, "axes_widget"):
+        axes.setChecked(renderer.axes_widget.GetEnabled())
+    else:
+        axes.setChecked(False)
+
+    renderer_ref = weakref.ref(renderer)
+    del renderer
 
     # axes
     def _axes_callback(state: bool) -> None:
+        renderer = renderer_ref()
+        if renderer is None:  # pragma: no cover
+            return
         if state:
             renderer.show_axes()
         else:
             renderer.hide_axes()
 
-    axes = QCheckBox("Axes")
-    if hasattr(renderer, "axes_widget"):
-        axes.setChecked(renderer.axes_widget.GetEnabled())
-    else:
-        axes.setChecked(False)
     axes.toggled.connect(_axes_callback)
     layout.addWidget(axes)
 
     widget.setLayout(layout)
     return widget
 
 
 def _get_actor_widget(actor: vtkActor) -> QWidget:
     widget = QWidget()
     layout = QVBoxLayout()
 
     prop = actor.GetProperty()
 
     # visibility
+    set_vis_ref = weakref.ref(actor.SetVisibility)
+
+    def _set_vis(visibility: bool) -> None:  # pragma: no cover
+        set_vis = set_vis_ref()
+        if set_vis is not None:
+            set_vis(visibility)
+
     visibility = QCheckBox("Visibility")
     visibility.setChecked(actor.GetVisibility())
-    visibility.toggled.connect(actor.SetVisibility)
+    visibility.toggled.connect(_set_vis)
     layout.addWidget(visibility)
 
     if prop is not None:
         # opacity
         tmp_layout = QHBoxLayout()
         opacity = QDoubleSpinBox()
         opacity.setMaximum(1.0)
         opacity.setValue(prop.GetOpacity())
-        opacity.valueChanged.connect(prop.SetOpacity)
+        set_opacity_ref = weakref.ref(prop.SetOpacity)
+
+        def _set_opacity(opacity: float) -> None:  # pragma: no cover
+            set_opacity = set_opacity_ref()
+            if set_opacity is not None:
+                set_opacity(opacity)
+
+        opacity.valueChanged.connect(_set_opacity)
         tmp_layout.addWidget(QLabel("Opacity"))
         tmp_layout.addWidget(opacity)
         layout.addLayout(tmp_layout)
 
     widget.setLayout(layout)
     return widget
```

### Comparing `pyvistaqt-0.9.0/pyvistaqt/plotting.py` & `pyvistaqt-0.9.1/pyvistaqt/plotting.py`

 * *Files 2% similar despite different names*

```diff
@@ -167,15 +167,15 @@
     point_smoothing :
         If True, enable point smothing
 
     polygon_smoothing :
         If True, enable polygon smothing
 
     auto_update :
-        Automatic update rate in seconds.  Useful for automatically
+        Number of updates per second.  Useful for automatically
         updating the render window when actors are change without
         being automatically ``Modified``.
     """
 
     # pylint: disable=too-many-instance-attributes
     # pylint: disable=too-many-statements
 
@@ -200,15 +200,15 @@
         """Initialize Qt interactor."""
         LOG.debug("QtInteractor init start")
         self.url: QtCore.QUrl = None
 
         # Cannot use super() here because
         # QVTKRenderWindowInteractor silently swallows all kwargs
         # because they use **kwargs in their constructor...
-        qvtk_kwargs = dict(parent=parent)
+        qvtk_kwargs = {"parent": parent}
         for key in ("stereo", "iren", "rw", "wflags"):
             if key in kwargs:
                 qvtk_kwargs[key] = kwargs.pop(key)
         with _no_base_plotter_init():
             QVTKRenderWindowInteractor.__init__(self, **qvtk_kwargs)
         BasePlotter.__init__(self, **kwargs)
         # backward compat for when we had this as a separate class
@@ -250,28 +250,31 @@
         else:
             self._setup_key_press()
 
         # Make the render timer but only activate if using auto update
         self.render_timer = QTimer(parent=parent)
         if float(auto_update) > 0.0:  # Can be False as well
             # Spawn a thread that updates the render window.
-            # Sometimes directly modifiying object data doesn't trigger
+            # Sometimes directly modifying object data doesn't trigger
             # Modified() and upstream objects won't be updated.  This
             # ensures the render window stays updated without consuming too
             # many resources.
             twait = int((auto_update**-1) * 1000.0)
             self.render_timer.timeout.connect(self.render)
             self.render_timer.start(twait)
 
         if global_theme.depth_peeling["enabled"]:
             if self.enable_depth_peeling():
                 for renderer in self.renderers:
                     renderer.enable_depth_peeling()
 
+        # Set some private attributes that let BasePlotter know
+        #   that this is safely rendering
         self._first_time = False  # Crucial!
+        # self._rendered = True  # this is handled in render()
         LOG.debug("QtInteractor init stop")
 
     def _setup_interactor(self, off_screen: bool) -> None:
         if off_screen:
             self.iren: Any = None
         else:
             self.iren = RenderWindowInteractor(
@@ -307,15 +310,19 @@
     def _render(self, *args: Any, **kwargs: Any) -> BasePlotter.render:
         """Wrap ``BasePlotter.render``."""
         return BasePlotter.render(self, *args, **kwargs)
 
     @conditional_decorator(threaded, platform.system() == "Darwin")
     def render(self) -> None:
         """Override the ``render`` method to handle threading issues."""
-        return self.render_signal.emit()
+        self._rendered = True  # Crucial for BasePlotter to know this has rendered
+        try:
+            return self.render_signal.emit()
+        except RuntimeError:  #  wrapped C/C++ object has been deleted
+            return None
 
     @wraps(BasePlotter.enable)
     def enable(self) -> None:
         """Wrap ``BasePlotter.enable``."""
         self.setEnabled(True)
         return BasePlotter.enable(self)
 
@@ -360,15 +367,15 @@
                 f"but {other_views.dtype} is given"
             )
 
         renderer = self.renderers[view]
         for view_index in other_views:
             other_plotter.renderers[view_index].camera = renderer.camera
 
-    # pylint: disable=invalid-name,no-self-use
+    # pylint: disable=invalid-name
     def dragEnterEvent(self, event: QtGui.QDragEnterEvent) -> None:
         """Event is called when something is dropped onto the vtk window.
 
         Only triggers event when event contains file paths that
         exist.  User can drop anything in this window and we only want
         to allow files.
         """
@@ -396,14 +403,24 @@
         """Quit application."""
         if self._closed:
             return
         if hasattr(self, "render_timer"):
             self.render_timer.stop()
         BasePlotter.close(self)
         QVTKRenderWindowInteractor.close(self)
+        # Qt LeaveEvent requires _Iren so we use _FakeIren instead of None
+        # to resolve the ref to vtkGenericRenderWindowInteractor
+        self._Iren = (  # pylint: disable=invalid-name,attribute-defined-outside-init
+            _FakeEventHandler()
+        )
+        for key in ("_RenderWindow", "renderer"):
+            try:
+                setattr(self, key, None)
+            except AttributeError:
+                pass
 
 
 class BackgroundPlotter(QtInteractor):
     """Qt interactive plotter.
 
     Background plotter for pyvista that allows you to maintain an
     interactive plotting window without blocking the main python
@@ -733,16 +750,15 @@
         self.app_window.setBaseSize(*window_size)
         self.app_window.resize(*window_size)
         # NOTE: setting BasePlotter is unnecessary and Segfaults CI
         # BasePlotter.window_size.fset(self, window_size)
 
     def __del__(self) -> None:  # pragma: no cover
         """Delete the qt plotter."""
-        if not self._closed:
-            self.app_window.close()
+        self.close()
 
     def add_callback(
         self, func: Callable, interval: int = 1000, count: Optional[int] = None
     ) -> None:
         """Add a function that can update the scene in the background.
 
         Parameters
@@ -1010,7 +1026,18 @@
         -------
         plotter : BackgroundPlotter
             The selected plotter.
         """
         row, col = idx
         self._plotter = self._plotters[row * self._ncols + col]
         return self._plotter
+
+
+class _FakeEventHandler:
+    # pylint: disable=too-few-public-methods
+
+    def _noop(self, *args: tuple, **kwargs: dict) -> None:
+        pass
+
+    SetDPI = EnterEvent = MouseMoveEvent = LeaveEvent = SetSize = _noop
+    SetEventInformation = ConfigureEvent = SetEventInformationFlipY = _noop
+    KeyReleaseEvent = CharEvent = _noop
```

### Comparing `pyvistaqt-0.9.0/pyvistaqt/rwi.py` & `pyvistaqt-0.9.1/pyvistaqt/rwi.py`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/pyvistaqt/utils.py` & `pyvistaqt-0.9.1/pyvistaqt/utils.py`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/pyvistaqt/window.py` & `pyvistaqt-0.9.1/pyvistaqt/window.py`

 * *Files identical despite different names*

### Comparing `pyvistaqt-0.9.0/setup.py` & `pyvistaqt-0.9.1/setup.py`

 * *Files 9% similar despite different names*

```diff
@@ -29,22 +29,22 @@
         'Development Status :: 4 - Beta',
         'Intended Audience :: Science/Research',
         'Topic :: Scientific/Engineering :: Information Analysis',
         'License :: OSI Approved :: MIT License',
         'Operating System :: Microsoft :: Windows',
         'Operating System :: POSIX',
         'Operating System :: MacOS',
-        'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
         'Programming Language :: Python :: 3.8',
+        'Programming Language :: Python :: 3.9',
     ],
 
     url='https://github.com/pyvista/pyvistaqt',
     keywords='vtk numpy plotting mesh qt',
-    python_requires='>=3.6.*',
+    python_requires='>=3.7',
     install_requires=[
         'pyvista>=0.32.0',
         'QtPy>=1.9.0',
     ],
     package_data={'pyvistaqt': [
         os.path.join('data', '*.png'),
     ]}
```

