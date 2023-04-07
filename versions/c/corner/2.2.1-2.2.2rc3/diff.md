# Comparing `tmp/corner-2.2.1.tar.gz` & `tmp/corner-2.2.2rc3.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "corner-2.2.1.tar", last modified: Tue Mar  9 20:41:38 2021, max compression
+gzip compressed data, was "corner-2.2.2rc3.tar", last modified: Fri Apr  7 14:53:40 2023, max compression
```

## Comparing `corner-2.2.1.tar` & `corner-2.2.2rc3.tar`

### file list

```diff
@@ -1,28 +1,31 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-03-09 20:41:38.572809 corner-2.2.1/
--rw-r--r--   0 runner    (1001) docker     (121)       61 2021-03-09 20:41:27.000000 corner-2.2.1/.coveragerc
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-03-09 20:41:38.564808 corner-2.2.1/.github/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-03-09 20:41:38.568808 corner-2.2.1/.github/workflows/
--rw-r--r--   0 runner    (1001) docker     (121)     2704 2021-03-09 20:41:27.000000 corner-2.2.1/.github/workflows/tests.yml
--rw-r--r--   0 runner    (1001) docker     (121)      143 2021-03-09 20:41:27.000000 corner-2.2.1/.gitignore
--rw-r--r--   0 runner    (1001) docker     (121)      529 2021-03-09 20:41:27.000000 corner-2.2.1/.pre-commit-config.yaml
--rw-r--r--   0 runner    (1001) docker     (121)     1526 2021-03-09 20:41:27.000000 corner-2.2.1/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      138 2021-03-09 20:41:27.000000 corner-2.2.1/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     2499 2021-03-09 20:41:38.572809 corner-2.2.1/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     1410 2021-03-09 20:41:27.000000 corner-2.2.1/README.rst
--rw-r--r--   0 runner    (1001) docker     (121)      462 2021-03-09 20:41:27.000000 corner-2.2.1/pyproject.toml
--rw-r--r--   0 runner    (1001) docker     (121)       38 2021-03-09 20:41:38.572809 corner-2.2.1/setup.cfg
--rwxr-xr-x   0 runner    (1001) docker     (121)     2522 2021-03-09 20:41:27.000000 corner-2.2.1/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-03-09 20:41:38.568808 corner-2.2.1/src/
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-03-09 20:41:38.572809 corner-2.2.1/src/corner/
--rw-r--r--   0 runner    (1001) docker     (121)      963 2021-03-09 20:41:27.000000 corner-2.2.1/src/corner/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4938 2021-03-09 20:41:27.000000 corner-2.2.1/src/corner/arviz_corner.py
--rw-r--r--   0 runner    (1001) docker     (121)    23954 2021-03-09 20:41:27.000000 corner-2.2.1/src/corner/core.py
--rw-r--r--   0 runner    (1001) docker     (121)     9164 2021-03-09 20:41:27.000000 corner-2.2.1/src/corner/corner.py
--rw-r--r--   0 runner    (1001) docker     (121)       22 2021-03-09 20:41:38.000000 corner-2.2.1/src/corner/corner_version.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2021-03-09 20:41:38.572809 corner-2.2.1/src/corner.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     2499 2021-03-09 20:41:38.000000 corner-2.2.1/src/corner.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      446 2021-03-09 20:41:38.000000 corner-2.2.1/src/corner.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-03-09 20:41:38.000000 corner-2.2.1/src/corner.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)      300 2021-03-09 20:41:38.000000 corner-2.2.1/src/corner.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        7 2021-03-09 20:41:38.000000 corner-2.2.1/src/corner.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2021-03-09 20:41:38.000000 corner-2.2.1/src/corner.egg-info/zip-safe
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 14:53:40.620858 corner-2.2.2rc3/
+-rw-r--r--   0 runner    (1001) docker     (123)       61 2023-04-07 14:53:27.000000 corner-2.2.2rc3/.coveragerc
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 14:53:40.616857 corner-2.2.2rc3/.github/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 14:53:40.616857 corner-2.2.2rc3/.github/workflows/
+-rw-r--r--   0 runner    (1001) docker     (123)     2430 2023-04-07 14:53:27.000000 corner-2.2.2rc3/.github/workflows/tests.yml
+-rw-r--r--   0 runner    (1001) docker     (123)      129 2023-04-07 14:53:27.000000 corner-2.2.2rc3/.gitignore
+-rw-r--r--   0 runner    (1001) docker     (123)      785 2023-04-07 14:53:27.000000 corner-2.2.2rc3/.pre-commit-config.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)     5468 2023-04-07 14:53:27.000000 corner-2.2.2rc3/CODE_OF_CONDUCT.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1355 2023-04-07 14:53:27.000000 corner-2.2.2rc3/CONTRIBUTING.md
+-rw-r--r--   0 runner    (1001) docker     (123)     1311 2023-04-07 14:53:27.000000 corner-2.2.2rc3/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (123)      138 2023-04-07 14:53:27.000000 corner-2.2.2rc3/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (123)     1748 2023-04-07 14:53:40.620858 corner-2.2.2rc3/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)     1038 2023-04-07 14:53:27.000000 corner-2.2.2rc3/README.md
+-rw-r--r--   0 runner    (1001) docker     (123)      330 2023-04-07 14:53:27.000000 corner-2.2.2rc3/noxfile.py
+-rw-r--r--   0 runner    (1001) docker     (123)     1474 2023-04-07 14:53:27.000000 corner-2.2.2rc3/pyproject.toml
+-rw-r--r--   0 runner    (1001) docker     (123)      269 2023-04-07 14:53:27.000000 corner-2.2.2rc3/readthedocs.yaml
+-rw-r--r--   0 runner    (1001) docker     (123)       38 2023-04-07 14:53:40.620858 corner-2.2.2rc3/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (123)      143 2023-04-07 14:53:27.000000 corner-2.2.2rc3/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 14:53:40.616857 corner-2.2.2rc3/src/
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 14:53:40.620858 corner-2.2.2rc3/src/corner/
+-rw-r--r--   0 runner    (1001) docker     (123)      263 2023-04-07 14:53:27.000000 corner-2.2.2rc3/src/corner/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (123)     5091 2023-04-07 14:53:27.000000 corner-2.2.2rc3/src/corner/arviz_corner.py
+-rw-r--r--   0 runner    (1001) docker     (123)    29684 2023-04-07 14:53:27.000000 corner-2.2.2rc3/src/corner/core.py
+-rw-r--r--   0 runner    (1001) docker     (123)    10202 2023-04-07 14:53:27.000000 corner-2.2.2rc3/src/corner/corner.py
+-rw-r--r--   0 runner    (1001) docker     (123)      163 2023-04-07 14:53:40.000000 corner-2.2.2rc3/src/corner/version.py
+drwxr-xr-x   0 runner    (1001) docker     (123)        0 2023-04-07 14:53:40.620858 corner-2.2.2rc3/src/corner.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (123)     1748 2023-04-07 14:53:40.000000 corner-2.2.2rc3/src/corner.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (123)      472 2023-04-07 14:53:40.000000 corner-2.2.2rc3/src/corner.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        1 2023-04-07 14:53:40.000000 corner-2.2.2rc3/src/corner.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (123)      142 2023-04-07 14:53:40.000000 corner-2.2.2rc3/src/corner.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (123)        7 2023-04-07 14:53:40.000000 corner-2.2.2rc3/src/corner.egg-info/top_level.txt
```

### Comparing `corner-2.2.1/.github/workflows/tests.yml` & `corner-2.2.2rc3/.github/workflows/tests.yml`

 * *Files 22% similar despite different names*

```diff
@@ -1,103 +1,91 @@
 name: Tests
+
 on:
   push:
-    branches: [main]
+    branches:
+      - main
+    tags:
+      - "*"
   pull_request:
-    branches: [main]
-  release:
-    types: [published]
 
 jobs:
   tests:
-    name: "py${{ matrix.python-version }}; ${{ matrix.arviz-version }}"
-    runs-on: "ubuntu-latest"
+    runs-on: ${{ matrix.os }}
     strategy:
+      fail-fast: false
       matrix:
-        python-version: ["3.9"]
-        arviz-version:
-          - ""
-          - "arviz~=0.9"
-          - "arviz~=0.10"
-          - "arviz~=0.11"
-          - "https://github.com/arviz-devs/arviz/archive/main.zip"
+        os: ["ubuntu-latest"]
+        python-version: ["3.9", "3.10", "3.11"]
+        nox-session: ["tests"]
         include:
-          - python-version: "3.6"
-            arviz-version: "arviz"
-          - python-version: "3.7"
-            arviz-version: "arviz"
-          - python-version: "3.8"
-            arviz-version: "arviz"
+          - os: macos-latest
+            python-version: "3.10"
+            nox-session: "tests"
+          - os: ubuntu-latest
+            python-version: "3.10"
+            nox-session: "lint"
 
     steps:
-      - uses: actions/checkout@v2
-
-      - name: Set up Python ${{ matrix.python-version }}
-        uses: actions/setup-python@v2
+      - name: Checkout
+        uses: actions/checkout@v3
+        with:
+          submodules: true
+          fetch-depth: 0
+      - name: Configure Python
+        uses: actions/setup-python@v4
         with:
           python-version: ${{ matrix.python-version }}
-
-      - name: Install dependencies
+      - name: Cache pre-commit environments
+        if: ${{ matrix.nox-session == 'lint' }}
+        uses: actions/cache@v3
+        with:
+          path: ~/.cache/pre-commit
+          key: ${{ runner.os }}-pre-commit-${{ hashFiles('.pre-commit-config.yaml') }}
+          restore-keys: |
+            ${{ runner.os }}-pre-commit-
+      - name: Install nox
         run: |
           python -m pip install -U pip
-          python -m pip install $ARVIZ ".[test]"
-        env:
-          ARVIZ: ${{ matrix.arviz-version }}
-
-      - name: Run the unit tests
-        run: python -m pytest -v tests
-
-      - uses: actions/upload-artifact@v2
-        if: ${{ failure() }}
+          python -m pip install -U nox
+      - name: Run tests
+        run: python -m nox --non-interactive -s ${{ matrix.nox-session }}
+      - name: Upload generated images on failure
+        uses: actions/upload-artifact@v3
+        if: ${{ failure() && matrix.nox-session == 'tests' }}
         with:
+          name: images-${{ matrix.os }}-${{ matrix.python-version }}
           path: ./result_images
 
   build:
-    name: Build source distribution
     runs-on: ubuntu-latest
     steps:
-      - uses: actions/checkout@v2
+      - uses: actions/checkout@v3
         with:
           fetch-depth: 0
-
-      - uses: actions/setup-python@v2
+      - uses: actions/setup-python@v4
         name: Install Python
         with:
-          python-version: "3.9"
-
-      - name: Build
+          python-version: "3.10"
+      - name: Build sdist and wheel
         run: |
           python -m pip install -U pip
           python -m pip install -U build
           python -m build .
-
-      - name: Test the sdist
-        run: |
-          python -m venv venv-sdist
-          venv-sdist/bin/python -m pip install dist/corner*.tar.gz
-          venv-sdist/bin/python -c "import corner;print(corner.__version__)"
-
-      - name: Test the wheel
-        run: |
-          python -m venv venv-wheel
-          venv-wheel/bin/python -m pip install dist/corner*.whl
-          venv-wheel/bin/python -c "import corner;print(corner.__version__)"
-
-      - uses: actions/upload-artifact@v2
+      - uses: actions/upload-artifact@v3
         with:
           path: dist/*
 
   upload_pypi:
     needs: [tests, build]
     runs-on: ubuntu-latest
-    if: github.event_name == 'release' && github.event.action == 'published'
+    if: startsWith(github.ref, 'refs/tags/')
     steps:
-      - uses: actions/download-artifact@v2
+      - uses: actions/download-artifact@v3
         with:
           name: artifact
           path: dist
 
-      - uses: pypa/gh-action-pypi-publish@master
+      - uses: pypa/gh-action-pypi-publish@v1.8.4
         with:
           user: __token__
           password: ${{ secrets.pypi_password }}
-          # To test: repository_url: https://test.pypi.org/legacy/
```

### Comparing `corner-2.2.1/LICENSE` & `corner-2.2.2rc3/LICENSE`

 * *Files 16% similar despite different names*

```diff
@@ -1,27 +1,24 @@
-Copyright (c) 2013-2020 Daniel Foreman-Mackey
+BSD 2-Clause License
 
-All rights reserved.
+Copyright (c) 2013-2022 Dan Foreman-Mackey
 
 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:
 
 1. Redistributions of source code must retain the above copyright notice, this
    list of conditions and the following disclaimer.
+
 2. Redistributions in binary form must reproduce the above copyright notice,
    this list of conditions and the following disclaimer in the documentation
    and/or other materials provided with the distribution.
 
-THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
-ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
-WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
-DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
-ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
-(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
-LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
-ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
-(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
-SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
-
-The views and conclusions contained in the software and documentation are those
-of the authors and should not be interpreted as representing official policies,
-either expressed or implied, of the FreeBSD Project.
+THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
+AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
+IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
+DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
+FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
+DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
+SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
+CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
+OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
+OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

### Comparing `corner-2.2.1/README.rst` & `corner-2.2.2rc3/README.md`

 * *Files 21% similar despite different names*

```diff
@@ -1,36 +1,26 @@
-corner.py
-=========
+# corner.py
 
-.. image:: https://github.com/dfm/corner.py/workflows/Tests/badge.svg?style=flat
-    :target: https://github.com/dfm/corner.py/actions
-.. image:: https://readthedocs.org/projects/corner/badge/?version=latest
-    :target: https://corner.readthedocs.io/en/latest/?badge=latest
-.. image:: http://img.shields.io/badge/license-BSD-blue.svg?style=flat
-    :target: https://github.com/dfm/corner.py/blob/main/LICENSE
-.. image:: https://zenodo.org/badge/4729/dfm/corner.py.svg?style=flat
-    :target: https://zenodo.org/badge/latestdoi/4729/dfm/corner.py
-.. image:: http://joss.theoj.org/papers/10.21105/joss.00024/status.svg?style=flat
-    :target: http://dx.doi.org/10.21105/joss.00024
+[![Tests](https://github.com/dfm/corner.py/workflows/Tests/badge.svg?style=flat)](https://github.com/dfm/corner.py/actions)
+[![License](https://img.shields.io/badge/license-BSD-blue.svg?style=flat)](https://github.com/dfm/corner.py/blob/main/LICENSE)
+[![DOI](https://zenodo.org/badge/4729/dfm/corner.py.svg?style=flat)](https://zenodo.org/badge/latestdoi/4729/dfm/corner.py)
+[![Paper](https://joss.theoj.org/papers/10.21105/joss.00024/status.svg?style=flat)](http://dx.doi.org/10.21105/joss.00024)
 
-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
-Read `the documentation <http://corner.readthedocs.io/>`_.
-++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+## Read [the documentation](http://corner.readthedocs.io/)
 
-If you make use of this code, please cite `the JOSS paper
-<http://dx.doi.org/10.21105/joss.00024>`_:
+If you make use of this code, please cite [the JOSS paper](http://dx.doi.org/10.21105/joss.00024):
 
-.. code-block:: tex
-
-    @article{corner,
-      doi = {10.21105/joss.00024},
-      url = {https://doi.org/10.21105/joss.00024},
-      year  = {2016},
-      month = {jun},
-      publisher = {The Open Journal},
-      volume = {1},
-      number = {2},
-      pages = {24},
-      author = {Daniel Foreman-Mackey},
-      title = {corner.py: Scatterplot matrices in Python},
-      journal = {The Journal of Open Source Software}
-    }
+```tex
+@article{corner,
+  doi = {10.21105/joss.00024},
+  url = {https://doi.org/10.21105/joss.00024},
+  year  = {2016},
+  month = {jun},
+  publisher = {The Open Journal},
+  volume = {1},
+  number = {2},
+  pages = {24},
+  author = {Daniel Foreman-Mackey},
+  title = {corner.py: Scatterplot matrices in Python},
+  journal = {The Journal of Open Source Software}
+}
+```
```

### Comparing `corner-2.2.1/src/corner/arviz_corner.py` & `corner-2.2.2rc3/src/corner/arviz_corner.py`

 * *Files 2% similar despite different names*

```diff
@@ -19,15 +19,14 @@
 
     def _get_labels(plotters, labeller=None):
         return [
             make_label(var_name, selection)
             for var_name, selection, _ in plotters
         ]
 
-
 except ImportError:
     from arviz.labels import BaseLabeller
     from arviz.sel_utils import xarray_to_ndarray, xarray_var_iter
 
     def _get_labels(plotters, labeller=None):
         if labeller is None:
             labeller = BaseLabeller()
@@ -42,16 +41,17 @@
 
 def arviz_corner(
     data,
     bins=20,
     *,
     # Original corner parameters
     range=None,
+    axes_scale="linear",
     weights=None,
-    color="k",
+    color=None,
     hist_bin_factor=1,
     smooth=None,
     smooth1d=None,
     labels=None,
     label_kwargs=None,
     titles=None,
     show_titles=False,
@@ -73,15 +73,15 @@
     group="posterior",
     var_names=None,
     filter_vars=None,
     coords=None,
     divergences=False,
     divergences_kwargs=None,
     labeller=None,
-    **hist2d_kwargs
+    **hist2d_kwargs,
 ):
     is_np = False
     if isinstance(data, np.ndarray):
         is_np = True
         if data.ndim == 1:
             data = data[None, :, :]
         elif data.ndim == 2:
@@ -133,14 +133,15 @@
 
     # Coerce the samples into the expected format
     samples = np.stack([x[-1].flatten() for x in plotters], axis=-1)
     fig = corner_impl(
         samples,
         bins=bins,
         range=range,
+        axes_scale=axes_scale,
         weights=weights,
         color=color,
         hist_bin_factor=hist_bin_factor,
         smooth=smooth,
         smooth1d=smooth1d,
         labels=labels,
         label_kwargs=label_kwargs,
@@ -171,10 +172,15 @@
             divergent_data = convert_to_dataset(data, group=divergent_group)
             _, diverging_mask = xarray_to_ndarray(
                 divergent_data, var_names=("diverging",), combined=True
             )
             diverging_mask = np.squeeze(diverging_mask)
             if divergences_kwargs is None:
                 divergences_kwargs = {"color": "C1", "ms": 1}
-            overplot_points(fig, samples[diverging_mask], **divergences_kwargs)
+            overplot_points(
+                fig,
+                samples[diverging_mask],
+                reverse=reverse,
+                **divergences_kwargs,
+            )
 
     return fig
```

### Comparing `corner-2.2.1/src/corner/core.py` & `corner-2.2.2rc3/src/corner/core.py`

 * *Files 12% similar despite different names*

```diff
@@ -7,65 +7,88 @@
     "overplot_lines",
     "overplot_points",
 ]
 
 import copy
 import logging
 
+import matplotlib
 import numpy as np
 from matplotlib import pyplot as pl
 from matplotlib.colors import LinearSegmentedColormap, colorConverter
-from matplotlib.ticker import MaxNLocator, NullLocator, ScalarFormatter
+from matplotlib.ticker import (
+    LogFormatterMathtext,
+    LogLocator,
+    MaxNLocator,
+    NullLocator,
+    ScalarFormatter,
+)
 
 try:
     from scipy.ndimage import gaussian_filter
 except ImportError:
     gaussian_filter = None
 
 
 def corner_impl(
     xs,
     bins=20,
     range=None,
+    axes_scale="linear",
     weights=None,
-    color="k",
+    color=None,
     hist_bin_factor=1,
     smooth=None,
     smooth1d=None,
     labels=None,
     label_kwargs=None,
     titles=None,
     show_titles=False,
     title_fmt=".2f",
     title_kwargs=None,
     truths=None,
     truth_color="#4682b4",
     scale_hist=False,
     quantiles=None,
+    title_quantiles=None,
     verbose=False,
     fig=None,
     max_n_ticks=5,
     top_ticks=False,
     use_math_text=False,
     reverse=False,
     labelpad=0.0,
     hist_kwargs=None,
-    **hist2d_kwargs
+    **hist2d_kwargs,
 ):
     if quantiles is None:
         quantiles = []
     if title_kwargs is None:
         title_kwargs = dict()
     if label_kwargs is None:
         label_kwargs = dict()
 
     # If no separate titles are set, copy the axis labels
     if titles is None:
         titles = labels
 
+    # deal with title quantiles so they much quantiles unless desired otherwise
+    if title_quantiles is None:
+        if len(quantiles) > 0:
+            title_quantiles = quantiles
+        else:
+            # a default for when quantiles not supplied.
+            title_quantiles = [0.16, 0.5, 0.84]
+
+    if show_titles and len(title_quantiles) != 3:
+        raise ValueError(
+            "'title_quantiles' must contain exactly three values; "
+            "pass a length-3 list or array using the 'title_quantiles' argument"
+        )
+
     # Deal with 1D sample lists.
     xs = _parse_input(xs)
     assert xs.shape[0] <= xs.shape[1], (
         "I don't believe that you want more " "dimensions than samples!"
     )
 
     # Parse the weight array.
@@ -85,30 +108,38 @@
     else:
         lbdim = 0.5 * factor  # size of left/bottom margin
         trdim = 0.2 * factor  # size of top/right margin
     whspace = 0.05  # w/hspace size
     plotdim = factor * K + factor * (K - 1.0) * whspace
     dim = lbdim + plotdim + trdim
 
+    # Make axes_scale into a list if necessary, otherwise check length
+    if isinstance(axes_scale, str):
+        axes_scale = [axes_scale] * K
+    else:
+        assert (
+            len(axes_scale) == K
+        ), "'axes_scale' should contain as many elements as data dimensions"
+
     # Create a new figure if one wasn't provided.
     new_fig = True
     if fig is None:
         fig, axes = pl.subplots(K, K, figsize=(dim, dim))
     else:
-        new_fig = False
-        axes = _get_fig_axes(fig, K)
+        axes, new_fig = _get_fig_axes(fig, K)
 
     # Format the figure.
     lb = lbdim / dim
     tr = (lbdim + plotdim) / dim
     fig.subplots_adjust(
         left=lb, bottom=lb, right=tr, top=tr, wspace=whspace, hspace=whspace
     )
 
     # Parse the parameter ranges.
+    force_range = False
     if range is None:
         if "extents" in hist2d_kwargs:
             logging.warning(
                 "Deprecated keyword argument 'extents'. "
                 "Use 'range' instead."
             )
             range = hist2d_kwargs.pop("extents")
@@ -125,14 +156,16 @@
                         "Please provide a `range` argument."
                     ).format(
                         ", ".join(map("{0}".format, np.arange(len(m))[m]))
                     )
                 )
 
     else:
+        force_range = True
+
         # If any of the extents are percentiles, convert them to ranges.
         # Also make sure it's a normal list.
         range = list(range)
         for i, _ in enumerate(range):
             try:
                 emin, emax = range[i]
             except TypeError:
@@ -152,14 +185,18 @@
         hist_bin_factor = [float(hist_bin_factor) for _ in range]
     except TypeError:
         if len(hist_bin_factor) != len(range):
             raise ValueError(
                 "Dimension mismatch between hist_bin_factor and " "range"
             )
 
+    # Set up the default plotting arguments.
+    if color is None:
+        color = matplotlib.rcParams["ytick.color"]
+
     # Set up the default histogram keywords.
     if hist_kwargs is None:
         hist_kwargs = dict()
     hist_kwargs["color"] = hist_kwargs.get("color", color)
     if smooth1d is None:
         hist_kwargs["histtype"] = hist_kwargs.get("histtype", "step")
 
@@ -173,31 +210,37 @@
         else:
             if reverse:
                 ax = axes[K - i - 1, K - i - 1]
             else:
                 ax = axes[i, i]
 
         # Plot the histograms.
-        if smooth1d is None:
-            bins_1d = int(max(1, np.round(hist_bin_factor[i] * bins[i])))
-            n, _, _ = ax.hist(
-                x,
-                bins=bins_1d,
-                weights=weights,
-                range=np.sort(range[i]),
-                **hist_kwargs,
+        n_bins_1d = int(max(1, np.round(hist_bin_factor[i] * bins[i])))
+        if axes_scale[i] == "linear":
+            bins_1d = np.linspace(min(range[i]), max(range[i]), n_bins_1d + 1)
+        elif axes_scale[i] == "log":
+            bins_1d = np.logspace(
+                np.log10(min(range[i])), np.log10(max(range[i])), n_bins_1d + 1
             )
         else:
+            raise ValueError(
+                "Scale "
+                + axes_scale[i]
+                + "for dimension "
+                + str(i)
+                + "not supported. Use 'linear' or 'log'"
+            )
+        if smooth1d is None:
+            n, _, _ = ax.hist(x, bins=bins_1d, weights=weights, **hist_kwargs)
+        else:
             if gaussian_filter is None:
                 raise ImportError("Please install scipy for smoothing")
-            n, b = np.histogram(
-                x, bins=bins[i], weights=weights, range=np.sort(range[i])
-            )
+            n, _ = np.histogram(x, bins=bins_1d, weights=weights)
             n = gaussian_filter(n, smooth1d)
-            x0 = np.array(list(zip(b[:-1], b[1:]))).flatten()
+            x0 = np.array(list(zip(bins_1d[:-1], bins_1d[1:]))).flatten()
             y0 = np.array(list(zip(n, n))).flatten()
             ax.plot(x0, y0, **hist_kwargs)
 
         # Plot quantiles if wanted.
         if len(quantiles) > 0:
             qvalues = quantile(x, quantiles, weights=weights)
             for q in qvalues:
@@ -208,23 +251,23 @@
                 print([item for item in zip(quantiles, qvalues)])
 
         if show_titles:
             title = None
             if title_fmt is not None:
                 # Compute the quantiles for the title. This might redo
                 # unneeded computation but who cares.
-                q_16, q_50, q_84 = quantile(
-                    x, [0.16, 0.5, 0.84], weights=weights
+                q_lo, q_mid, q_hi = quantile(
+                    x, title_quantiles, weights=weights
                 )
-                q_m, q_p = q_50 - q_16, q_84 - q_50
+                q_m, q_p = q_mid - q_lo, q_hi - q_mid
 
                 # Format the quantile display.
                 fmt = "{{0:{0}}}".format(title_fmt).format
                 title = r"${{{0}}}_{{-{1}}}^{{+{2}}}$"
-                title = title.format(fmt(q_50), fmt(q_m), fmt(q_p))
+                title = title.format(fmt(q_mid), fmt(q_m), fmt(q_p))
 
                 # Add in the column name if it's given.
                 if titles is not None:
                     title = "{0} = {1}".format(titles[i], title)
 
             elif titles is not None:
                 title = "{0}".format(titles[i])
@@ -239,40 +282,49 @@
                         title_kwargs_new = title_kwargs
 
                     ax.set_xlabel(title, **title_kwargs_new)
                 else:
                     ax.set_title(title, **title_kwargs)
 
         # Set up the axes.
-        _set_xlim(new_fig, ax, range[i])
+        _set_xlim(force_range, new_fig, ax, range[i])
+        ax.set_xscale(axes_scale[i])
         if scale_hist:
             maxn = np.max(n)
-            _set_ylim(new_fig, ax, [-0.1 * maxn, 1.1 * maxn])
+            _set_ylim(force_range, new_fig, ax, [-0.1 * maxn, 1.1 * maxn])
 
         else:
-            _set_ylim(new_fig, ax, [0, 1.1 * np.max(n)])
+            _set_ylim(force_range, new_fig, ax, [0, 1.1 * np.max(n)])
 
         ax.set_yticklabels([])
         if max_n_ticks == 0:
             ax.xaxis.set_major_locator(NullLocator())
             ax.yaxis.set_major_locator(NullLocator())
         else:
-            ax.xaxis.set_major_locator(MaxNLocator(max_n_ticks, prune="lower"))
+            if axes_scale[i] == "linear":
+                ax.xaxis.set_major_locator(
+                    MaxNLocator(max_n_ticks, prune="lower")
+                )
+            elif axes_scale[i] == "log":
+                ax.xaxis.set_major_locator(LogLocator(numticks=max_n_ticks))
             ax.yaxis.set_major_locator(NullLocator())
 
         if i < K - 1:
             if top_ticks:
                 ax.xaxis.set_ticks_position("top")
                 [l.set_rotation(45) for l in ax.get_xticklabels()]
+                [l.set_rotation(45) for l in ax.get_xticklabels(minor=True)]
             else:
                 ax.set_xticklabels([])
+                ax.set_xticklabels([], minor=True)
         else:
             if reverse:
                 ax.xaxis.tick_top()
-            [lbl.set_rotation(45) for lbl in ax.get_xticklabels()]
+            [l.set_rotation(45) for l in ax.get_xticklabels()]
+            [l.set_rotation(45) for l in ax.get_xticklabels(minor=True)]
             if labels is not None:
                 if reverse:
                     if "labelpad" in label_kwargs.keys():
                         label_kwargs_new = copy.copy(label_kwargs)
                         del label_kwargs_new["labelpad"]
                         label_kwargs_new["pad"] = label_kwargs["labelpad"]
                     else:
@@ -284,17 +336,20 @@
                     )
 
                 else:
                     ax.set_xlabel(labels[i], **label_kwargs)
                     ax.xaxis.set_label_coords(0.5, -0.3 - labelpad)
 
             # use MathText for axes ticks
-            ax.xaxis.set_major_formatter(
-                ScalarFormatter(useMathText=use_math_text)
-            )
+            if axes_scale[i] == "linear":
+                ax.xaxis.set_major_formatter(
+                    ScalarFormatter(useMathText=use_math_text)
+                )
+            elif axes_scale[i] == "log":
+                ax.xaxis.set_major_formatter(LogFormatterMathtext())
 
         for j, y in enumerate(xs):
             if np.shape(xs)[0] == 1:
                 ax = axes
             else:
                 if reverse:
                     ax = axes[K - i - 1, K - j - 1]
@@ -313,75 +368,99 @@
                 y = y.compressed()
 
             hist2d(
                 y,
                 x,
                 ax=ax,
                 range=[range[j], range[i]],
+                axes_scale=[axes_scale[j], axes_scale[i]],
                 weights=weights,
                 color=color,
                 smooth=smooth,
                 bins=[bins[j], bins[i]],
                 new_fig=new_fig,
+                force_range=force_range,
                 **hist2d_kwargs,
             )
 
             if max_n_ticks == 0:
                 ax.xaxis.set_major_locator(NullLocator())
                 ax.yaxis.set_major_locator(NullLocator())
             else:
-                ax.xaxis.set_major_locator(
-                    MaxNLocator(max_n_ticks, prune="lower")
-                )
-                ax.yaxis.set_major_locator(
-                    MaxNLocator(max_n_ticks, prune="lower")
-                )
+                if axes_scale[j] == "linear":
+                    ax.xaxis.set_major_locator(
+                        MaxNLocator(max_n_ticks, prune="lower")
+                    )
+                elif axes_scale[j] == "log":
+                    ax.xaxis.set_major_locator(
+                        LogLocator(numticks=max_n_ticks)
+                    )
+
+                if axes_scale[i] == "linear":
+                    ax.yaxis.set_major_locator(
+                        MaxNLocator(max_n_ticks, prune="lower")
+                    )
+                elif axes_scale[i] == "log":
+                    ax.yaxis.set_major_locator(
+                        LogLocator(numticks=max_n_ticks)
+                    )
 
             if i < K - 1:
                 ax.set_xticklabels([])
+                ax.set_xticklabels([], minor=True)
             else:
                 if reverse:
                     ax.xaxis.tick_top()
                 [l.set_rotation(45) for l in ax.get_xticklabels()]
+                [l.set_rotation(45) for l in ax.get_xticklabels(minor=True)]
                 if labels is not None:
                     ax.set_xlabel(labels[j], **label_kwargs)
                     if reverse:
                         ax.xaxis.set_label_coords(0.5, 1.4 + labelpad)
                     else:
                         ax.xaxis.set_label_coords(0.5, -0.3 - labelpad)
 
                 # use MathText for axes ticks
-                ax.xaxis.set_major_formatter(
-                    ScalarFormatter(useMathText=use_math_text)
-                )
+                if axes_scale[j] == "linear":
+                    ax.xaxis.set_major_formatter(
+                        ScalarFormatter(useMathText=use_math_text)
+                    )
+                elif axes_scale[j] == "log":
+                    ax.xaxis.set_major_formatter(LogFormatterMathtext())
 
             if j > 0:
                 ax.set_yticklabels([])
+                ax.set_yticklabels([], minor=True)
             else:
                 if reverse:
                     ax.yaxis.tick_right()
                 [l.set_rotation(45) for l in ax.get_yticklabels()]
+                [l.set_rotation(45) for l in ax.get_yticklabels(minor=True)]
                 if labels is not None:
                     if reverse:
                         ax.set_ylabel(labels[i], rotation=-90, **label_kwargs)
                         ax.yaxis.set_label_coords(1.3 + labelpad, 0.5)
                     else:
                         ax.set_ylabel(labels[i], **label_kwargs)
                         ax.yaxis.set_label_coords(-0.3 - labelpad, 0.5)
 
                 # use MathText for axes ticks
-                ax.yaxis.set_major_formatter(
-                    ScalarFormatter(useMathText=use_math_text)
-                )
+                if axes_scale[i] == "linear":
+                    ax.yaxis.set_major_formatter(
+                        ScalarFormatter(useMathText=use_math_text)
+                    )
+                elif axes_scale[i] == "log":
+                    ax.yaxis.set_major_formatter(LogFormatterMathtext())
 
     if truths is not None:
-        overplot_lines(fig, truths, color=truth_color)
+        overplot_lines(fig, truths, reverse=reverse, color=truth_color)
         overplot_points(
             fig,
             [[np.nan if t is None else t for t in truths]],
+            reverse=reverse,
             marker="s",
             color=truth_color,
         )
 
     return fig
 
 
@@ -439,14 +518,15 @@
 
 
 def hist2d(
     x,
     y,
     bins=20,
     range=None,
+    axes_scale=["linear", "linear"],
     weights=None,
     levels=None,
     smooth=None,
     ax=None,
     color=None,
     quiet=False,
     plot_datapoints=True,
@@ -455,28 +535,31 @@
     no_fill_contours=False,
     fill_contours=False,
     contour_kwargs=None,
     contourf_kwargs=None,
     data_kwargs=None,
     pcolor_kwargs=None,
     new_fig=True,
-    **kwargs
+    force_range=False,
+    **kwargs,
 ):
-
     """
     Plot a 2-D histogram of samples.
 
     Parameters
     ----------
     x : array_like[nsamples,]
        The samples.
 
     y : array_like[nsamples,]
        The samples.
 
+    axes_scale : iterable (2,)
+        Scale (``"linear"``, ``"log"``) to use for each dimension.
+
     quiet : bool
         If true, suppress warnings for small datasets.
 
     levels : array_like
         The contour levels to draw.
 
     ax : matplotlib.Axes
@@ -525,53 +608,90 @@
             )
             range = kwargs["extent"]
         else:
             range = [[x.min(), x.max()], [y.min(), y.max()]]
 
     # Set up the default plotting arguments.
     if color is None:
-        color = "k"
+        color = matplotlib.rcParams["ytick.color"]
 
     # Choose the default "sigma" contour levels.
     if levels is None:
         levels = 1.0 - np.exp(-0.5 * np.arange(0.5, 2.1, 0.5) ** 2)
 
+    # This is the base color of the axis (background color)
+    base_color = ax.get_facecolor()
+
     # This is the color map for the density plot, over-plotted to indicate the
     # density of the points near the center.
     density_cmap = LinearSegmentedColormap.from_list(
-        "density_cmap", [color, (1, 1, 1, 0)]
+        "density_cmap", [color, colorConverter.to_rgba(base_color, alpha=0.0)]
     )
 
     # This color map is used to hide the points at the high density areas.
-    white_cmap = LinearSegmentedColormap.from_list(
-        "white_cmap", [(1, 1, 1), (1, 1, 1)], N=2
+    base_cmap = LinearSegmentedColormap.from_list(
+        "base_cmap", [base_color, base_color], N=2
     )
 
     # This "color map" is the list of colors for the contour levels if the
     # contours are filled.
     rgba_color = colorConverter.to_rgba(color)
     contour_cmap = [list(rgba_color) for l in levels] + [rgba_color]
     for i, l in enumerate(levels):
         contour_cmap[i][-1] *= float(i) / (len(levels) + 1)
 
+    # Parse the bin specifications.
+    try:
+        bins = [int(bins) for _ in range]
+    except TypeError:
+        if len(bins) != len(range):
+            raise ValueError("Dimension mismatch between bins and range")
+
     # We'll make the 2D histogram to directly estimate the density.
+    bins_2d = []
+    if axes_scale[0] == "linear":
+        bins_2d.append(np.linspace(min(range[0]), max(range[0]), bins[0] + 1))
+    elif axes_scale[0] == "log":
+        bins_2d.append(
+            np.logspace(
+                np.log10(min(range[0])),
+                np.log10(max(range[0])),
+                bins[0] + 1,
+            )
+        )
+
+    if axes_scale[1] == "linear":
+        bins_2d.append(np.linspace(min(range[1]), max(range[1]), bins[1] + 1))
+    elif axes_scale[1] == "log":
+        bins_2d.append(
+            np.logspace(
+                np.log10(min(range[1])),
+                np.log10(max(range[1])),
+                bins[1] + 1,
+            )
+        )
+
     try:
         H, X, Y = np.histogram2d(
             x.flatten(),
             y.flatten(),
-            bins=bins,
-            range=list(map(np.sort, range)),
+            bins=bins_2d,
             weights=weights,
         )
     except ValueError:
         raise ValueError(
             "It looks like at least one of your sample columns "
             "have no dynamic range. You could try using the "
             "'range' argument."
         )
+    if H.sum() == 0:
+        raise ValueError(
+            "It looks like the provided 'range' is not valid "
+            "or the sample is empty."
+        )
 
     if smooth is not None:
         if gaussian_filter is None:
             raise ImportError("Please install scipy for smoothing")
         H = gaussian_filter(H, smooth)
 
     if plot_contours or plot_density:
@@ -637,15 +757,15 @@
     # Plot the base fill to hide the densest data points.
     if (plot_contours or plot_density) and not no_fill_contours:
         ax.contourf(
             X2,
             Y2,
             H2.T,
             [V.min(), H.max()],
-            cmap=white_cmap,
+            cmap=base_cmap,
             antialiased=False,
         )
 
     if plot_contours and fill_contours:
         if contourf_kwargs is None:
             contourf_kwargs = dict()
         contourf_kwargs["colors"] = contourf_kwargs.get("colors", contour_cmap)
@@ -670,108 +790,135 @@
     # Plot the contour edge colors.
     if plot_contours:
         if contour_kwargs is None:
             contour_kwargs = dict()
         contour_kwargs["colors"] = contour_kwargs.get("colors", color)
         ax.contour(X2, Y2, H2.T, V, **contour_kwargs)
 
-    _set_xlim(new_fig, ax, range[0])
-    _set_ylim(new_fig, ax, range[1])
+    _set_xlim(force_range, new_fig, ax, range[0])
+    _set_ylim(force_range, new_fig, ax, range[1])
+    ax.set_xscale(axes_scale[0])
+    ax.set_yscale(axes_scale[1])
 
 
-def overplot_lines(fig, xs, **kwargs):
+def overplot_lines(fig, xs, reverse=False, **kwargs):
     """
     Overplot lines on a figure generated by ``corner.corner``
 
     Parameters
     ----------
     fig : Figure
         The figure generated by a call to :func:`corner.corner`.
 
     xs : array_like[ndim]
        The values where the lines should be plotted. This must have ``ndim``
        entries, where ``ndim`` is compatible with the :func:`corner.corner`
        call that originally generated the figure. The entries can optionally
        be ``None`` to omit the line in that axis.
 
+    reverse: bool
+       A boolean flag that should be set to 'True' if the corner plot itself
+       was plotted with 'reverse=True'.
+
     **kwargs
         Any remaining keyword arguments are passed to the ``ax.axvline``
         method.
 
     """
     K = len(xs)
-    axes = _get_fig_axes(fig, K)
-    for k1 in range(K):
-        if xs[k1] is not None:
-            axes[k1, k1].axvline(xs[k1], **kwargs)
-        for k2 in range(k1 + 1, K):
+    axes, _ = _get_fig_axes(fig, K)
+    if reverse:
+        for k1 in range(K):
+            if xs[k1] is not None:
+                axes[K - k1 - 1, K - k1 - 1].axvline(xs[k1], **kwargs)
+            for k2 in range(k1 + 1, K):
+                if xs[k1] is not None:
+                    axes[K - k2 - 1, K - k1 - 1].axvline(xs[k1], **kwargs)
+                if xs[k2] is not None:
+                    axes[K - k2 - 1, K - k1 - 1].axhline(xs[k2], **kwargs)
+
+    else:
+        for k1 in range(K):
             if xs[k1] is not None:
-                axes[k2, k1].axvline(xs[k1], **kwargs)
-            if xs[k2] is not None:
-                axes[k2, k1].axhline(xs[k2], **kwargs)
+                axes[k1, k1].axvline(xs[k1], **kwargs)
+            for k2 in range(k1 + 1, K):
+                if xs[k1] is not None:
+                    axes[k2, k1].axvline(xs[k1], **kwargs)
+                if xs[k2] is not None:
+                    axes[k2, k1].axhline(xs[k2], **kwargs)
 
 
-def overplot_points(fig, xs, **kwargs):
+def overplot_points(fig, xs, reverse=False, **kwargs):
     """
     Overplot points on a figure generated by ``corner.corner``
 
     Parameters
     ----------
     fig : Figure
         The figure generated by a call to :func:`corner.corner`.
 
     xs : array_like[nsamples, ndim]
        The coordinates of the points to be plotted. This must have an ``ndim``
        that is compatible with the :func:`corner.corner` call that originally
        generated the figure.
 
+    reverse: bool
+       A boolean flag that should be set to 'True' if the corner plot itself
+       was plotted with 'reverse=True'.
+
     **kwargs
         Any remaining keyword arguments are passed to the ``ax.plot``
         method.
 
     """
     kwargs["marker"] = kwargs.pop("marker", ".")
     kwargs["linestyle"] = kwargs.pop("linestyle", "none")
     xs = _parse_input(xs)
     K = len(xs)
-    axes = _get_fig_axes(fig, K)
-    for k1 in range(K):
-        for k2 in range(k1 + 1, K):
-            axes[k2, k1].plot(xs[k1], xs[k2], **kwargs)
+    axes, _ = _get_fig_axes(fig, K)
+    if reverse:
+        for k1 in range(K):
+            for k2 in range(k1):
+                axes[K - k1 - 1, K - k2 - 1].plot(xs[k2], xs[k1], **kwargs)
+
+    else:
+        for k1 in range(K):
+            for k2 in range(k1 + 1, K):
+                axes[k2, k1].plot(xs[k1], xs[k2], **kwargs)
 
 
 def _parse_input(xs):
     xs = np.atleast_1d(xs)
     if len(xs.shape) == 1:
         xs = np.atleast_2d(xs)
     else:
         assert len(xs.shape) == 2, "The input sample array must be 1- or 2-D."
         xs = xs.T
     return xs
 
 
 def _get_fig_axes(fig, K):
     if not fig.axes:
-        return fig.subplots(K, K)
+        return fig.subplots(K, K), True
     try:
-        return np.array(fig.axes).reshape((K, K))
+        return np.array(fig.axes).reshape((K, K)), False
     except ValueError:
         raise ValueError(
             (
                 "Provided figure has {0} axes, but data has "
                 "dimensions K={1}"
             ).format(len(fig.axes), K)
         )
 
 
-def _set_xlim(new_fig, ax, new_xlim):
-    if new_fig:
+def _set_xlim(force, new_fig, ax, new_xlim):
+    if force or new_fig:
         return ax.set_xlim(new_xlim)
     xlim = ax.get_xlim()
     return ax.set_xlim([min(xlim[0], new_xlim[0]), max(xlim[1], new_xlim[1])])
 
 
-def _set_ylim(new_fig, ax, new_ylim):
-    if new_fig:
+def _set_ylim(force, new_fig, ax, new_ylim):
+    if force or new_fig:
         return ax.set_ylim(new_ylim)
     ylim = ax.get_ylim()
     return ax.set_ylim([min(ylim[0], new_ylim[0]), max(ylim[1], new_ylim[1])])
```

### Comparing `corner-2.2.1/src/corner/corner.py` & `corner-2.2.2rc3/src/corner/corner.py`

 * *Files 7% similar despite different names*

```diff
@@ -2,37 +2,39 @@
 
 __all__ = "corner"
 
 import logging
 
 import numpy as np
 
-from .core import corner_impl
+from corner.core import corner_impl
 
 try:
-    from .arviz_corner import arviz_corner
+    from corner.arviz_corner import arviz_corner
 except ImportError:
     arviz_corner = None
 
 
 def corner(
     data,
     bins=20,
     *,
     # Original corner parameters
     range=None,
+    axes_scale="linear",
     weights=None,
-    color="k",
+    color=None,
     hist_bin_factor=1,
     smooth=None,
     smooth1d=None,
     labels=None,
     label_kwargs=None,
     titles=None,
     show_titles=False,
+    title_quantiles=None,
     title_fmt=".2f",
     title_kwargs=None,
     truths=None,
     truth_color="#4682b4",
     scale_hist=False,
     quantiles=None,
     verbose=False,
@@ -47,15 +49,15 @@
     group="posterior",
     var_names=None,
     filter_vars=None,
     coords=None,
     divergences=False,
     divergences_kwargs=None,
     labeller=None,
-    **hist2d_kwargs
+    **hist2d_kwargs,
 ):
     """
     Make a *sick* corner plot showing the projections of a data set in a
     multi-dimensional space. kwargs are passed to hist2d() or used for
     `matplotlib` styling.
 
     Parameters
@@ -114,16 +116,22 @@
 
     smooth, smooth1d : float
        The standard deviation for Gaussian kernel passed to
        `scipy.ndimage.gaussian_filter` to smooth the 2-D and 1-D histograms
        respectively. If `None` (default), no smoothing is applied.
 
     labels : iterable (ndim,)
-        A list of names for the dimensions. If a ``xs`` is a
-        ``pandas.DataFrame``, labels will default to column names.
+        A list of names for the dimensions.
+
+        .. deprecated:: 2.2.1
+            If a ``xs`` is a ``pandas.DataFrame`` *and* ArviZ is installed,
+            labels will default to column names.
+            This behavior will be removed in version 3;
+            either use ArviZ data structures instead or pass
+            ``labels=dataframe.columns`` manually.
 
     label_kwargs : dict
         Any extra keyword arguments to send to the `set_xlabel` and
         `set_ylabel` methods. Note that passing the `labelpad` keyword
         in this dictionary will not have the desired effect. Use the
         `labelpad` keyword in this function instead.
 
@@ -131,14 +139,19 @@
         A list of titles for the dimensions. If `None` (default),
         uses labels as titles.
 
     show_titles : bool
         Displays a title above each 1-D histogram showing the 0.5 quantile
         with the upper and lower errors supplied by the quantiles argument.
 
+    title_quantiles : iterable
+        A list of 3 fractional quantiles to show as the the upper and lower
+        errors. If `None` (default), inherit the values from quantiles, unless
+        quantiles is `None`, in which case it defaults to [0.16,0.5,0.84]
+
     title_fmt : string
         The format string for the quantiles given in titles. If you explicitly
         set ``show_titles=True`` and ``title_fmt=None``, the labels will be
         shown as the titles. (default: ``.2f``)
 
     title_kwargs : dict
         Any extra keyword arguments to send to the `set_title` command.
@@ -146,14 +159,18 @@
     range : iterable (ndim,)
         A list where each element is either a length 2 tuple containing
         lower and upper bounds or a float in range (0., 1.)
         giving the fraction of samples to include in bounds, e.g.,
         [(0.,10.), (1.,5), 0.999, etc.].
         If a fraction, the bounds are chosen to be equal-tailed.
 
+    axes_scale : str or iterable (ndim,)
+        Scale (``"linear"``, ``"log"``) to use for each data dimension. If only
+        one scale is specified, use that for all dimensions.
+
     truths : iterable (ndim,)
         A list of reference values to indicate on the plots.  Individual
         values can be omitted by using ``None``.
 
     truth_color : str
         A ``matplotlib`` style color for the ``truths`` makers.
 
@@ -185,26 +202,31 @@
 
     max_n_ticks: int
         Maximum number of ticks to try to use
 
     top_ticks : bool
         If true, label the top ticks of each axis
 
-    fig : matplotlib.Figure
+    fig : `~matplotlib.figure.Figure`
         Overplot onto the provided figure object, which must either have no
         axes yet, or ``ndim * ndim`` axes already present.  If not set, the
         plot will be drawn on a newly created figure.
 
     hist_kwargs : dict
         Any extra keyword arguments to send to the 1-D histogram plots.
 
     **hist2d_kwargs
         Any remaining keyword arguments are sent to :func:`corner.hist2d` to
         generate the 2-D histogram plots.
 
+    Returns
+    -------
+    fig : `~matplotlib.figure.Figure`
+        The ``matplotlib`` figure instance for the corner plot.
+
     """
     if arviz_corner is None:
         if not (
             isinstance(data, np.ndarray)
             or data.__class__.__name__ == "DataFrame"
         ):
             raise ImportError(
@@ -223,23 +245,25 @@
                 "Please install arviz to use the advanced features of corner"
             )
 
         return corner_impl(
             data,
             bins=bins,
             range=range,
+            axes_scale=axes_scale,
             weights=weights,
             color=color,
             hist_bin_factor=hist_bin_factor,
             smooth=smooth,
             smooth1d=smooth1d,
             labels=labels,
             label_kwargs=label_kwargs,
             titles=titles,
             show_titles=show_titles,
+            title_quantiles=title_quantiles,
             title_fmt=title_fmt,
             title_kwargs=title_kwargs,
             truths=truths,
             truth_color=truth_color,
             scale_hist=scale_hist,
             quantiles=quantiles,
             verbose=verbose,
@@ -253,23 +277,25 @@
             **hist2d_kwargs,
         )
 
     return arviz_corner(
         data,
         bins=bins,
         range=range,
+        axes_scale=axes_scale,
         weights=weights,
         color=color,
         hist_bin_factor=hist_bin_factor,
         smooth=smooth,
         smooth1d=smooth1d,
         labels=labels,
         label_kwargs=label_kwargs,
         titles=titles,
         show_titles=show_titles,
+        title_quantiles=title_quantiles,
         title_fmt=title_fmt,
         title_kwargs=title_kwargs,
         truths=truths,
         truth_color=truth_color,
         scale_hist=scale_hist,
         quantiles=quantiles,
         verbose=verbose,
```

