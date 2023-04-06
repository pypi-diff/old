# Comparing `tmp/dragonfly-core-1.8.1.tar.gz` & `tmp/dragonfly-core-1.9.0.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "dist/dragonfly-core-1.8.1.tar", last modified: Sat Jan 18 22:17:24 2020, max compression
+gzip compressed data, was "dist/dragonfly-core-1.9.0.tar", last modified: Mon Jan 20 19:33:18 2020, max compression
```

## Comparing `dragonfly-core-1.8.1.tar` & `dragonfly-core-1.9.0.tar`

### file list

```diff
@@ -1,55 +1,55 @@
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/.github/
--rw-rw-r--   0 travis    (2000) travis    (2000)     1742 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/.github/project-manager.yml
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/docs/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/docs/_build/
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/docs/_build/docs/
--rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/docs/_build/docs/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/docs/_build/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/docs/_build/.nojekyll
--rw-rw-r--   0 travis    (2000) travis    (2000)      369 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/docs/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)     6563 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/docs/conf.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      251 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/docs/index.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)       77 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/docs/modules.rst
--rw-rw-r--   0 travis    (2000) travis    (2000)      279 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/CODE_OF_CONDUCT.md
--rw-rw-r--   0 travis    (2000) travis    (2000)       45 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/requirements.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)     2559 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/PKG-INFO
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/dragonfly_core.egg-info/
--rw-rw-r--   0 travis    (2000) travis    (2000)     2559 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/dragonfly_core.egg-info/PKG-INFO
--rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/dragonfly_core.egg-info/dependency_links.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       10 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/dragonfly_core.egg-info/top_level.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)      990 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/dragonfly_core.egg-info/SOURCES.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)       45 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/dragonfly_core.egg-info/requires.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)      294 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/.releaserc.json
--rw-rw-r--   0 travis    (2000) travis    (2000)     1553 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/README.md
--rw-rw-r--   0 travis    (2000) travis    (2000)      142 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/.gitignore
--rw-rw-r--   0 travis    (2000) travis    (2000)      445 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/CONTRIBUTING.md
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/dragonfly/
--rw-rw-r--   0 travis    (2000) travis    (2000)    50734 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/room2d.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5756 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/subdivide.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     7617 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/context.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     3075 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/_base.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    31262 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/building.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     4984 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/extensionutil.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    18088 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/properties.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      655 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    33731 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/windowparameter.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    16492 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/model.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    20850 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/shadingparameter.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    19209 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dragonfly/story.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      102 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/setup.cfg
--rw-rw-r--   0 travis    (2000) travis    (2000)     1054 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/.travis.yml
--rw-rw-r--   0 travis    (2000) travis    (2000)    35149 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/LICENSE
--rw-rw-r--   0 travis    (2000) travis    (2000)      184 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/dev-requirements.txt
--rw-rw-r--   0 travis    (2000) travis    (2000)      976 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/setup.py
--rw-rw-r--   0 travis    (2000) travis    (2000)      165 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/deploy.sh
-drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-18 22:17:24.000000 dragonfly-core-1.8.1/tests/
--rw-rw-r--   0 travis    (2000) travis    (2000)    15267 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/tests/story_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     8002 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/tests/shadingparameter_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    23543 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/tests/model_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     5867 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/tests/context_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)     2496 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/tests/subdivide_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    13094 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/tests/windowparameter_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/tests/__init__.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    20699 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/tests/building_test.py
--rw-rw-r--   0 travis    (2000) travis    (2000)    24636 2020-01-18 22:16:41.000000 dragonfly-core-1.8.1/tests/room2d_test.py
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/.github/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1742 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/.github/project-manager.yml
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/docs/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/docs/_build/
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/docs/_build/docs/
+-rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/docs/_build/docs/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)       16 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/docs/_build/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/docs/_build/.nojekyll
+-rw-rw-r--   0 travis    (2000) travis    (2000)      369 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/docs/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)     6563 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/docs/conf.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      251 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/docs/index.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)       77 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/docs/modules.rst
+-rw-rw-r--   0 travis    (2000) travis    (2000)      279 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/CODE_OF_CONDUCT.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)       45 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/requirements.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2559 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/PKG-INFO
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/dragonfly_core.egg-info/
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2559 2020-01-20 19:33:17.000000 dragonfly-core-1.9.0/dragonfly_core.egg-info/PKG-INFO
+-rw-rw-r--   0 travis    (2000) travis    (2000)        1 2020-01-20 19:33:17.000000 dragonfly-core-1.9.0/dragonfly_core.egg-info/dependency_links.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       10 2020-01-20 19:33:17.000000 dragonfly-core-1.9.0/dragonfly_core.egg-info/top_level.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      990 2020-01-20 19:33:17.000000 dragonfly-core-1.9.0/dragonfly_core.egg-info/SOURCES.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)       45 2020-01-20 19:33:17.000000 dragonfly-core-1.9.0/dragonfly_core.egg-info/requires.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      294 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/.releaserc.json
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1553 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/README.md
+-rw-rw-r--   0 travis    (2000) travis    (2000)      142 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/.gitignore
+-rw-rw-r--   0 travis    (2000) travis    (2000)      445 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/CONTRIBUTING.md
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/dragonfly/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    50713 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/room2d.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5756 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/subdivide.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     7617 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/context.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     3075 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/_base.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    31262 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/building.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     4984 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/extensionutil.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    18088 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/properties.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      655 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    33523 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/windowparameter.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    16492 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/model.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    20850 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/shadingparameter.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    19209 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dragonfly/story.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      102 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/setup.cfg
+-rw-rw-r--   0 travis    (2000) travis    (2000)     1054 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/.travis.yml
+-rw-rw-r--   0 travis    (2000) travis    (2000)    35149 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/LICENSE
+-rw-rw-r--   0 travis    (2000) travis    (2000)      184 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/dev-requirements.txt
+-rw-rw-r--   0 travis    (2000) travis    (2000)      976 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/setup.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)      165 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/deploy.sh
+drwxrwxr-x   0 travis    (2000) travis    (2000)        0 2020-01-20 19:33:18.000000 dragonfly-core-1.9.0/tests/
+-rw-rw-r--   0 travis    (2000) travis    (2000)    15267 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/tests/story_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     8002 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/tests/shadingparameter_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    23543 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/tests/model_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     5867 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/tests/context_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)     2496 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/tests/subdivide_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    13006 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/tests/windowparameter_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)        0 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/tests/__init__.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    20699 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/tests/building_test.py
+-rw-rw-r--   0 travis    (2000) travis    (2000)    24636 2020-01-20 19:32:35.000000 dragonfly-core-1.9.0/tests/room2d_test.py
```

### Comparing `dragonfly-core-1.8.1/.github/project-manager.yml` & `dragonfly-core-1.9.0/.github/project-manager.yml`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/docs/conf.py` & `dragonfly-core-1.9.0/docs/conf.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/PKG-INFO` & `dragonfly-core-1.9.0/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dragonfly-core
-Version: 1.8.1
+Version: 1.9.0
 Summary: :dragon: dragonfly core library
 Home-page: https://github.com/ladybug-tools/dragonfly-core
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: UNKNOWN
 Description: [![Build Status](https://travis-ci.org/ladybug-tools/dragonfly-core.svg?branch=master)](https://travis-ci.org/ladybug-tools/dragonfly-core)
         [![Coverage Status](https://coveralls.io/repos/github/ladybug-tools/dragonfly-core/badge.svg?branch=master)](https://coveralls.io/github/ladybug-tools/dragonfly-core)
```

### Comparing `dragonfly-core-1.8.1/dragonfly_core.egg-info/PKG-INFO` & `dragonfly-core-1.9.0/dragonfly_core.egg-info/PKG-INFO`

 * *Files 1% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: dragonfly-core
-Version: 1.8.1
+Version: 1.9.0
 Summary: :dragon: dragonfly core library
 Home-page: https://github.com/ladybug-tools/dragonfly-core
 Author: Ladybug Tools
 Author-email: info@ladybug.tools
 License: UNKNOWN
 Description: [![Build Status](https://travis-ci.org/ladybug-tools/dragonfly-core.svg?branch=master)](https://travis-ci.org/ladybug-tools/dragonfly-core)
         [![Coverage Status](https://coveralls.io/repos/github/ladybug-tools/dragonfly-core/badge.svg?branch=master)](https://coveralls.io/github/ladybug-tools/dragonfly-core)
```

### Comparing `dragonfly-core-1.8.1/dragonfly_core.egg-info/SOURCES.txt` & `dragonfly-core-1.9.0/dragonfly_core.egg-info/SOURCES.txt`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/README.md` & `dragonfly-core-1.9.0/README.md`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/room2d.py` & `dragonfly-core-1.9.0/dragonfly/room2d.py`

 * *Files 1% similar despite different names*

```diff
@@ -1,13 +1,13 @@
 # coding: utf-8
 """Dragonfly Room2D."""
 from ._base import _BaseGeometry
 from .properties import Room2DProperties
 import dragonfly.windowparameter as glzpar
-from dragonfly.windowparameter import _WindowParameterBase, _DetailedParameterBase
+from dragonfly.windowparameter import _WindowParameterBase, _AsymmetricBase
 import dragonfly.shadingparameter as shdpar
 from dragonfly.shadingparameter import _ShadingParameterBase
 
 from honeybee.typing import float_positive
 import honeybee.boundarycondition as hbc
 from honeybee.boundarycondition import boundary_conditions as bcs
 from honeybee.boundarycondition import _BoundaryCondition, Outdoors, Surface
@@ -268,15 +268,15 @@
         if polygon.is_clockwise:
             polygon = polygon.reverse()
             if boundary_conditions is not None:
                 boundary_conditions = list(reversed(boundary_conditions))
             if window_parameters is not None:
                 new_win_pars = []
                 for seg, win_par in zip(polygon.segments, reversed(window_parameters)):
-                    if isinstance (win_par, _DetailedParameterBase):
+                    if isinstance (win_par, _AsymmetricBase):
                         new_win_pars.append(win_par.flip(seg.length))
                     else:
                         new_win_pars.append(win_par)
                 window_parameters = new_win_pars
             if shading_parameters is not None:
                 shading_parameters = list(reversed(shading_parameters))
 
@@ -924,15 +924,15 @@
         # go through the boundary and ensure detailed parameters are flipped
         new_bcs = []
         new_win_pars = []
         new_shd_pars = []
         for i, seg in enumerate(original_geo.boundary_segments):
             new_bcs.append(bcs[i])
             win_par = win_pars[i]
-            if isinstance (win_par, _DetailedParameterBase):
+            if isinstance (win_par, _AsymmetricBase):
                 new_win_pars.append(win_par.flip(seg.length))
             else:
                 new_win_pars.append(win_par)
             new_shd_pars.append(shd_pars[i])
         
         # reverse the lists of wall-assigned objects on the floor boundary
         new_bcs.reverse()
```

### Comparing `dragonfly-core-1.8.1/dragonfly/subdivide.py` & `dragonfly-core-1.9.0/dragonfly/subdivide.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/context.py` & `dragonfly-core-1.9.0/dragonfly/context.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/_base.py` & `dragonfly-core-1.9.0/dragonfly/_base.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/building.py` & `dragonfly-core-1.9.0/dragonfly/building.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/extensionutil.py` & `dragonfly-core-1.9.0/dragonfly/extensionutil.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/properties.py` & `dragonfly-core-1.9.0/dragonfly/properties.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/__init__.py` & `dragonfly-core-1.9.0/dragonfly/__init__.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/windowparameter.py` & `dragonfly-core-1.9.0/dragonfly/windowparameter.py`

 * *Files 2% similar despite different names*

```diff
@@ -451,42 +451,40 @@
     def __repr__(self):
         return 'RepeatingWindowRatio:\n ratio: {}\n window_height: {}\n sill_height:' \
             ' {}\n horizontal: {}\n vertical: {}'.format(
                 self._window_ratio, self.window_height, self.sill_height,
                 self.horizontal_separation, self.vertical_separation)
 
 
-class _DetailedParameterBase(_WindowParameterBase):
-    """Base class for all detailed WindowParameters.
-
-    Detailed parameters allow for the specification of several individual windows
-    within a given Wall plane.
+class _AsymmetricBase(_WindowParameterBase):
+    """Base class for WindowParameters that can make asymmetric windows on a wall.
     """
 
-    def flip(self, segment):
-        """Flip the direction of the windows along a segment.
+    def flip(self, seg_length):
+        """Flip the direction of the windows along a wall segment.
 
-        This is needed for detailed window specifications since windows can exist
-        asymmetically across the wall segment and operations like reflecting the
-        Room2D across a plane will require the window parameters to be flipped.
+        This is needed since windows can exist asymmetically across the wall
+        segment and operations like reflecting the Room2D across a plane will
+        require the window parameters to be flipped.
 
         Args:
-            segment: A LineSegment3D to which these parameters are applied.
+            seg_length: The length of the segment along which the parameters are
+                being flipped.
         """
         return self
 
 
-class DetailedRectangularWindows(_DetailedParameterBase):
+class RectangularWindows(_AsymmetricBase):
     """Instructions for several rectangular windows, defined by origin, width and height.
 
     Note that, if these parameters are applied to a base wall that is too short
     or too narrow such that the windows fall outside the boundary of the wall, the
     generated windows will automatically be shortened or excluded. This way, a
     certain pattern of repating rectangular windows can be encoded in a single
-    DetailedRectangularWindows instance and applied to multiple Room2D segments.
+    RectangularWindows instance and applied to multiple Room2D segments.
 
     Properties:
         * origins
         * widths
         * heights
 
     Args:
@@ -500,15 +498,15 @@
             of this list must match the length of the origins.
         heights: An array of postive numbers for the window heights. The length
             of this list must match the length of the origins.
     """
     __slots__ = ('_origins', '_widths', '_heights')
 
     def __init__(self, origins, widths, heights):
-        """Initialize DetailedRectangularWindows."""
+        """Initialize RectangularWindows."""
         if not isinstance(origins, tuple):
             origins = tuple(origins)
         for point in origins:
             assert isinstance(point, Point2D), \
                 'Expected Point2D for window origin. Got {}'.format(type(point))
         self._origins = origins
         
@@ -588,15 +586,15 @@
         """Get a scaled version of these WindowParameters.
         
         This method is called within the scale methods of the Room2D.
         
         Args:
             factor: A number representing how much the object should be scaled.
         """
-        return DetailedRectangularWindows(
+        return RectangularWindows(
             tuple(Point2D(pt.x * factor, pt.y * factor) for pt in self.origins),
             tuple(width * factor for width in self.widths),
             tuple(height * factor for height in self.heights))
 
     def flip(self, seg_length):
         """Flip the direction of the windows along a segment.
 
@@ -618,64 +616,64 @@
                 new_widths.append(width)
                 new_heights.append(height)
             elif new_x + width > seg_length * 0.001:  # partially within the boundary
                 new_widths.append(width + new_x - (seg_length * 0.001))
                 new_x = seg_length * 0.001
                 new_origins.append(Point2D(new_x, o.y))
                 new_heights.append(height)
-        return DetailedRectangularWindows(new_origins, new_widths, new_heights)
+        return RectangularWindows(new_origins, new_widths, new_heights)
 
     @classmethod
     def from_dict(cls, data):
-        """Create DetailedRectangularWindows from a dictionary.
+        """Create RectangularWindows from a dictionary.
 
         .. code-block:: python
 
             {
-            "type": "DetailedRectangularWindows",
+            "type": "RectangularWindows",
             "origins": [(1, 1), (3, 0.5)],  # array of (x, y) floats in wall plane
             "widths": [1, 3],  # array of floats for window widths
             "heights": [1, 2.5]  # array of floats for window heights
             }
         """
-        assert data['type'] == 'DetailedRectangularWindows', \
-            'Expected DetailedRectangularWindows. Got {}.'.format(data['type'])
+        assert data['type'] == 'RectangularWindows', \
+            'Expected RectangularWindows. Got {}.'.format(data['type'])
         return cls(tuple(Point2D.from_array(pt) for pt in data['origins']),
                    data['widths'], data['heights'])
 
     def to_dict(self):
-        """Get DetailedRectangularWindows as a dictionary."""
-        return {'type': 'DetailedRectangularWindows',
+        """Get RectangularWindows as a dictionary."""
+        return {'type': 'RectangularWindows',
                 'origins': [pt.to_array() for pt in self.origins],
                 'widths': self.widths,
                 'heights': self.heights
                 }
 
     def __copy__(self):
-        return DetailedRectangularWindows(self.origins, self.widths, self.heights)
+        return RectangularWindows(self.origins, self.widths, self.heights)
 
     def __key(self):
         """A tuple based on the object properties, useful for hashing."""
         return (hash(self.origins), hash(self.widths), hash(self.heights))
 
     def __hash__(self):
         return hash(self.__key())
 
     def __eq__(self, other):
-        return isinstance(other, DetailedRectangularWindows) and \
+        return isinstance(other, RectangularWindows) and \
             self.__key() == other.__key()
 
     def __ne__(self, other):
         return not self.__eq__(other)
 
     def __repr__(self):
-        return 'DetailedRectangularWindows:\n {} windows'.format(len(self.origins))
+        return 'RectangularWindows:\n {} windows'.format(len(self.origins))
 
 
-class DetailedWindows(_DetailedParameterBase):
+class DetailedWindows(_AsymmetricBase):
     """Instructions for detailed windows, defined by 2D Polygons (lists of 2D vertices).
 
     Note that these parameters are intended to represent windows that are specific
     to a particular segment and, unlike the other WindowParameters, this class
     performs no automatic checks to ensure that the windows lie within the
     boundary of the wall they have been assigned to.
```

### Comparing `dragonfly-core-1.8.1/dragonfly/model.py` & `dragonfly-core-1.9.0/dragonfly/model.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/shadingparameter.py` & `dragonfly-core-1.9.0/dragonfly/shadingparameter.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/dragonfly/story.py` & `dragonfly-core-1.9.0/dragonfly/story.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/.travis.yml` & `dragonfly-core-1.9.0/.travis.yml`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/LICENSE` & `dragonfly-core-1.9.0/LICENSE`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/setup.py` & `dragonfly-core-1.9.0/setup.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/tests/story_test.py` & `dragonfly-core-1.9.0/tests/story_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/tests/shadingparameter_test.py` & `dragonfly-core-1.9.0/tests/shadingparameter_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/tests/model_test.py` & `dragonfly-core-1.9.0/tests/model_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/tests/context_test.py` & `dragonfly-core-1.9.0/tests/context_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/tests/subdivide_test.py` & `dragonfly-core-1.9.0/tests/subdivide_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/tests/windowparameter_test.py` & `dragonfly-core-1.9.0/tests/windowparameter_test.py`

 * *Files 2% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 # coding=utf-8
 import pytest
 
 from dragonfly.windowparameter import SingleWindow, SimpleWindowRatio, \
-    RepeatingWindowRatio, DetailedRectangularWindows, DetailedWindows
+    RepeatingWindowRatio, RectangularWindows, DetailedWindows
 
 from honeybee.face import Face
 
 from ladybug_geometry.geometry2d.pointvector import Point2D
 from ladybug_geometry.geometry2d.polygon import Polygon2D
 from ladybug_geometry.geometry3d.pointvector import Point3D, Vector3D
 from ladybug_geometry.geometry3d.line import LineSegment3D
@@ -178,89 +178,89 @@
     assert len(face.apertures) == 3
     ap_area = sum([ap.area for ap in face.apertures])
     assert ashrae_base.area_from_segment(seg, height) == \
         pytest.approx(ap_area, rel=1e-3) == width * height * 0.4
 
 
 def test_detailed_rectangular_init():
-    """Test the initalization of DetailedRectangularWindows and basic properties."""
+    """Test the initalization of RectangularWindows and basic properties."""
     origins = (Point2D(2, 1), Point2D(5, 0.5))
     widths = (1, 3)
     heights = (1, 2)
-    detailed_window = DetailedRectangularWindows(origins, widths, heights)
+    detailed_window = RectangularWindows(origins, widths, heights)
     str(detailed_window)  # test the string representation
 
     assert detailed_window.origins == origins
     assert detailed_window.widths == widths
     assert detailed_window.heights == heights
 
 
 def test_detailed_rectangular_equality():
-    """Test the equality of DetailedRectangularWindows."""
+    """Test the equality of RectangularWindows."""
     origins = (Point2D(2, 1), Point2D(5, 0.5))
     widths = (1, 3)
     heights = (1, 2)
     heights_alt = (1, 1)
-    detailed_window = DetailedRectangularWindows(origins, widths, heights)
+    detailed_window = RectangularWindows(origins, widths, heights)
     detailed_window_dup = detailed_window.duplicate()
-    detailed_window_alt = DetailedRectangularWindows(origins, widths, heights_alt)
+    detailed_window_alt = RectangularWindows(origins, widths, heights_alt)
 
     assert detailed_window is detailed_window
     assert detailed_window is not detailed_window_dup
     assert detailed_window == detailed_window_dup
     assert hash(detailed_window) == hash(detailed_window_dup)
     assert detailed_window != detailed_window_alt
     assert hash(detailed_window) != hash(detailed_window_alt)
 
 
 def test_detailed_rectangular_dict_methods():
     """Test the to/from dict methods."""
     origins = (Point2D(2, 1), Point2D(5, 0.5))
     widths = (1, 3)
     heights = (1, 2)
-    detailed_window = DetailedRectangularWindows(origins, widths, heights)
+    detailed_window = RectangularWindows(origins, widths, heights)
 
     glz_dict = detailed_window.to_dict()
-    new_detailed_window = DetailedRectangularWindows.from_dict(glz_dict)
+    new_detailed_window = RectangularWindows.from_dict(glz_dict)
     assert new_detailed_window == detailed_window
     assert glz_dict == new_detailed_window.to_dict()
 
 
 def test_detailed_rectangular_scale():
     """Test the scale method."""
     origins = (Point2D(2, 1), Point2D(5, 0.5))
     widths = (1, 3)
     heights = (1, 2)
-    detailed_window = DetailedRectangularWindows(origins, widths, heights)
+    detailed_window = RectangularWindows(origins, widths, heights)
 
     new_detailed_window  = detailed_window.scale(2)
     assert new_detailed_window.origins == (Point2D(4, 2), Point2D(10, 1))
     assert new_detailed_window.widths == (2, 6)
     assert new_detailed_window.heights == (2, 4)
 
 
 def test_detailed_rectangular_flip():
     """Test the flip method."""
     origins = (Point2D(2, 1), Point2D(5, 0.5))
     widths = (1, 3)
     heights = (1, 2)
-    detailed_window = DetailedRectangularWindows(origins, widths, heights)
+    detailed_window = RectangularWindows(origins, widths, heights)
 
     new_detailed_window  = detailed_window.flip(10)
     assert new_detailed_window.origins == (Point2D(7, 1), Point2D(2, 0.5))
     assert new_detailed_window.widths == widths
     assert new_detailed_window.heights == heights
 
 
 def test_single_window_add_window_to_face():
     """Test the add_window_to_face method."""
     origins = (Point2D(2, 1), Point2D(5, 0.5))
     widths = (1, 3)
     heights = (1, 2)
-    detailed_window = DetailedRectangularWindows(origins, widths, heights)
+    detailed_window = RectangularWindows(origins, widths, heights)
     height = 3
     width = 10
     seg = LineSegment3D.from_end_points(Point3D(0, 0, 2), Point3D(width, 0, 2))
     face = Face('test face', Face3D.from_extrusion(seg, Vector3D(0, 0, height)))
     detailed_window.add_window_to_face(face, 0.01)
 
     assert len(face.apertures) == 2
```

### Comparing `dragonfly-core-1.8.1/tests/building_test.py` & `dragonfly-core-1.9.0/tests/building_test.py`

 * *Files identical despite different names*

### Comparing `dragonfly-core-1.8.1/tests/room2d_test.py` & `dragonfly-core-1.9.0/tests/room2d_test.py`

 * *Files identical despite different names*

