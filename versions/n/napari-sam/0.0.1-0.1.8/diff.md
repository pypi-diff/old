# Comparing `tmp/napari-sam-0.0.1.tar.gz` & `tmp/napari-sam-0.1.8.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "napari-sam-0.0.1.tar", last modified: Thu Apr  6 11:40:33 2023, max compression
+gzip compressed data, was "napari-sam-0.1.8.tar", last modified: Thu Apr  6 12:27:33 2023, max compression
```

## Comparing `napari-sam-0.0.1.tar` & `napari-sam-0.1.8.tar`

### file list

```diff
@@ -1,20 +1,20 @@
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:33.507979 napari-sam-0.0.1/
--rw-r--r--   0 runner    (1001) docker     (123)     1490 2023-04-06 11:40:17.000000 napari-sam-0.0.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (123)       96 2023-04-06 11:40:17.000000 napari-sam-0.0.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (123)     3989 2023-04-06 11:40:33.507979 napari-sam-0.0.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)     2764 2023-04-06 11:40:17.000000 napari-sam-0.0.1/README.md
--rw-r--r--   0 runner    (1001) docker     (123)      180 2023-04-06 11:40:17.000000 napari-sam-0.0.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (123)     1715 2023-04-06 11:40:33.507979 napari-sam-0.0.1/setup.cfg
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:33.503978 napari-sam-0.0.1/src/
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:33.507979 napari-sam-0.0.1/src/napari_sam.egg-info/
--rw-r--r--   0 runner    (1001) docker     (123)     3989 2023-04-06 11:40:33.000000 napari-sam-0.0.1/src/napari_sam.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (123)      440 2023-04-06 11:40:33.000000 napari-sam-0.0.1/src/napari_sam.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 11:40:33.000000 napari-sam-0.0.1/src/napari_sam.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (123)       80 2023-04-06 11:40:33.000000 napari-sam-0.0.1/src/napari_sam.egg-info/entry_points.txt
--rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-06 11:40:33.000000 napari-sam-0.0.1/src/napari_sam.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (123)       24 2023-04-06 11:40:33.000000 napari-sam-0.0.1/src/napari_sam.egg-info/top_level.txt
-drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 11:40:33.507979 napari-sam-0.0.1/src/napari_segment_anything/
--rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-06 11:40:17.000000 napari-sam-0.0.1/src/napari_segment_anything/__init__.py
--rw-r--r--   0 runner    (1001) docker     (123)    14515 2023-04-06 11:40:17.000000 napari-sam-0.0.1/src/napari_segment_anything/_widget.py
--rw-r--r--   0 runner    (1001) docker     (123)      326 2023-04-06 11:40:17.000000 napari-sam-0.0.1/src/napari_segment_anything/napari.yaml
--rw-r--r--   0 runner    (1001) docker     (123)     1980 2023-04-06 11:40:17.000000 napari-sam-0.0.1/src/napari_segment_anything/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:27:33.978078 napari-sam-0.1.8/
+-rw-r--r--   0 runner    (1001) docker     (123)    11358 2023-04-06 12:27:18.000000 napari-sam-0.1.8/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)       96 2023-04-06 12:27:18.000000 napari-sam-0.1.8/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     3842 2023-04-06 12:27:33.978078 napari-sam-0.1.8/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     2607 2023-04-06 12:27:18.000000 napari-sam-0.1.8/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      180 2023-04-06 12:27:18.000000 napari-sam-0.1.8/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)     1686 2023-04-06 12:27:33.982078 napari-sam-0.1.8/setup.cfg
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:27:33.978078 napari-sam-0.1.8/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:27:33.978078 napari-sam-0.1.8/src/napari_sam/
+-rw-r--r--   0 runner    (1001) docker     (123)       84 2023-04-06 12:27:18.000000 napari-sam-0.1.8/src/napari_sam/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)    14451 2023-04-06 12:27:18.000000 napari-sam-0.1.8/src/napari_sam/_widget.py
+-rw-r--r--   0 runner    (1001) docker     (123)      274 2023-04-06 12:27:18.000000 napari-sam-0.1.8/src/napari_sam/napari.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     1980 2023-04-06 12:27:18.000000 napari-sam-0.1.8/src/napari_sam/utils.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-06 12:27:33.978078 napari-sam-0.1.8/src/napari_sam.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     3842 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      388 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       54 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/entry_points.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       89 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)       11 2023-04-06 12:27:33.000000 napari-sam-0.1.8/src/napari_sam.egg-info/top_level.txt
```

### Comparing `napari-sam-0.0.1/README.md` & `napari-sam-0.1.8/README.md`

 * *Files 19% similar despite different names*

```diff
@@ -1,15 +1,15 @@
-# napari-segment-anything
+# napari-sam
 
-[![License BSD-3](https://img.shields.io/pypi/l/napari-segment-anything.svg?color=green)](https://github.com/Karol-G/napari-segment-anything/raw/main/LICENSE)
-[![PyPI](https://img.shields.io/pypi/v/napari-segment-anything.svg?color=green)](https://pypi.org/project/napari-segment-anything)
-[![Python Version](https://img.shields.io/pypi/pyversions/napari-segment-anything.svg?color=green)](https://python.org)
-[![tests](https://github.com/Karol-G/napari-segment-anything/workflows/tests/badge.svg)](https://github.com/Karol-G/napari-segment-anything/actions)
-[![codecov](https://codecov.io/gh/Karol-G/napari-segment-anything/branch/main/graph/badge.svg)](https://codecov.io/gh/Karol-G/napari-segment-anything)
-[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-segment-anything)](https://napari-hub.org/plugins/napari-segment-anything)
+[![License Apache Software License 2.0](https://img.shields.io/pypi/l/napari-sam.svg?color=green)](https://github.com/MIC-DKFZ/napari-sam/raw/main/LICENSE)
+[![PyPI](https://img.shields.io/pypi/v/napari-sam.svg?color=green)](https://pypi.org/project/napari-sam)
+[![Python Version](https://img.shields.io/pypi/pyversions/napari-sam.svg?color=green)](https://python.org)
+[![tests](https://github.com/MIC-DKFZ/napari-sam/workflows/tests/badge.svg)](https://github.com/MIC-DKFZ/napari-sam/actions)
+[![codecov](https://codecov.io/gh/MIC-DKFZ/napari-sam/branch/main/graph/badge.svg)](https://codecov.io/gh/MIC-DKFZ/napari-sam)
+[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-sam)](https://napari-hub.org/plugins/napari-sam)
 
 Segment anything with Meta AI's new SAM model!
 
 ----------------------------------
 
 This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.
 
@@ -19,34 +19,34 @@
 
 and review the napari docs for plugin developers:
 https://napari.org/stable/plugins/index.html
 -->
 
 ## Installation
 
-You can install `napari-segment-anything` via [pip]:
+You can install `napari-sam` via [pip]:
 
     pip install napari-sam
 
 
 
 To install latest development version :
 
-    pip install git+https://github.com/Karol-G/napari-segment-anything.git
+    pip install git+https://github.com/MIC-DKFZ/napari-sam.git
 
 
 ## Contributing
 
 Contributions are very welcome. Tests can be run with [tox], please ensure
 the coverage at least stays the same before you submit a pull request.
 
 ## License
 
-Distributed under the terms of the [BSD-3] license,
-"napari-segment-anything" is free and open source software
+Distributed under the terms of the [Apache Software License 2.0] license,
+"napari-sam" is free and open source software
 
 ## Issues
 
 If you encounter any problems, please [file an issue] along with a detailed description.
 
 [napari]: https://github.com/napari/napari
 [Cookiecutter]: https://github.com/audreyr/cookiecutter
@@ -55,13 +55,13 @@
 [BSD-3]: http://opensource.org/licenses/BSD-3-Clause
 [GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
 [GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
 [Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
 [Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
 [cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
 
-[file an issue]: https://github.com/Karol-G/napari-segment-anything/issues
+[file an issue]: https://github.com/MIC-DKFZ/napari-sam/issues
 
 [napari]: https://github.com/napari/napari
 [tox]: https://tox.readthedocs.io/en/latest/
 [pip]: https://pypi.org/project/pip/
 [PyPI]: https://pypi.org/
```

### Comparing `napari-sam-0.0.1/setup.cfg` & `napari-sam-0.1.8/setup.cfg`

 * *Files 9% similar despite different names*

```diff
@@ -1,23 +1,23 @@
 [metadata]
 name = napari-sam
-version = attr: napari_segment_anything.__version__
+version = attr: napari_sam.__version__
 description = Segment anything with Meta AI's new SAM model!
 long_description = file: README.md
 long_description_content_type = text/markdown
 url = https://github.com/MIC-DKFZ/napari-sam
 author = Karol Gotkowski
 author_email = karol.gotkowski@dkfz.de
-license = BSD-3-Clause
+license = Apache-2.0
 license_files = LICENSE
 classifiers = 
 	Development Status :: 2 - Pre-Alpha
 	Framework :: napari
 	Intended Audience :: Developers
-	License :: OSI Approved :: BSD License
+	License :: OSI Approved :: Apache Software License
 	Operating System :: OS Independent
 	Programming Language :: Python
 	Programming Language :: Python :: 3
 	Programming Language :: Python :: 3 :: Only
 	Programming Language :: Python :: 3.8
 	Programming Language :: Python :: 3.9
 	Programming Language :: Python :: 3.10
@@ -42,15 +42,15 @@
 	=src
 
 [options.packages.find]
 where = src
 
 [options.entry_points]
 napari.manifest = 
-	napari-segment-anything = napari_segment_anything:napari.yaml
+	napari-sam = napari_sam:napari.yaml
 
 [options.extras_require]
 testing = 
 	tox
 	pytest  # https://docs.pytest.org/en/latest/contents.html
 	pytest-cov  # https://pytest-cov.readthedocs.io/en/latest/
 	pytest-qt  # https://pytest-qt.readthedocs.io/en/latest/
```

### Comparing `napari-sam-0.0.1/src/napari_segment_anything/_widget.py` & `napari-sam-0.1.8/src/napari_sam/_widget.py`

 * *Files 1% similar despite different names*

```diff
@@ -2,15 +2,15 @@
 from qtpy import QtCore
 import napari
 import numpy as np
 from enum import Enum
 from collections import deque
 import inspect
 from segment_anything import SamPredictor, sam_model_registry
-from napari_segment_anything.utils import get_weights_path, get_cached_weight_types
+from napari_sam.utils import get_weights_path, get_cached_weight_types
 import torch
 from vispy.util.keys import CONTROL
 
 
 class AnnotatorMode(Enum):
     NONE = 0
     CLICK = 1
@@ -270,17 +270,14 @@
             image = self.image_layer.data
             if not self.image_layer.rgb:
                 image = np.stack((image,)*3, axis=-1)  # Expand to 3-channel image
             image = image[..., :3]  # Remove a potential alpha channel
             self.sam_predictor.set_image(image)
 
     def do_click(self, coords, is_positive):
-        print("Click")
-        print(is_positive)
-
         self.point_coords.append(coords)
         self.point_labels.append(is_positive)
 
         prediction, _, self.sam_logits = self.sam_predictor.predict(
             point_coords=np.flip(self.point_coords, axis=-1),
             point_labels=np.asarray(self.point_labels),
             mask_input=self.sam_logits,
```

### Comparing `napari-sam-0.0.1/src/napari_segment_anything/utils.py` & `napari-sam-0.1.8/src/napari_sam/utils.py`

 * *Files identical despite different names*

