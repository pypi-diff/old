# Comparing `tmp/leafmap-0.9.5.tar.gz` & `tmp/leafmap-0.9.6.tar.gz`

## filetype from file(1)

```diff
@@ -1 +1 @@
-gzip compressed data, was "leafmap-0.9.5.tar", last modified: Mon Jun 27 03:58:58 2022, max compression
+gzip compressed data, was "leafmap-0.9.6.tar", last modified: Fri Jul  1 19:50:36 2022, max compression
```

## Comparing `leafmap-0.9.5.tar` & `leafmap-0.9.6.tar`

### file list

```diff
@@ -1,49 +1,50 @@
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 03:58:58.295454 leafmap-0.9.5/
--rw-r--r--   0 runner    (1001) docker     (121)     1070 2022-06-27 03:58:49.000000 leafmap-0.9.5/LICENSE
--rw-r--r--   0 runner    (1001) docker     (121)      277 2022-06-27 03:58:49.000000 leafmap-0.9.5/MANIFEST.in
--rw-r--r--   0 runner    (1001) docker     (121)     9243 2022-06-27 03:58:58.295454 leafmap-0.9.5/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)     8395 2022-06-27 03:58:49.000000 leafmap-0.9.5/README.md
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 03:58:58.295454 leafmap-0.9.5/leafmap/
--rw-r--r--   0 runner    (1001) docker     (121)      714 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)    18901 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/basemaps.py
--rw-r--r--   0 runner    (1001) docker     (121)    10175 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/colormaps.py
--rw-r--r--   0 runner    (1001) docker     (121)   192998 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/common.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 03:58:58.295454 leafmap-0.9.5/leafmap/data/
--rw-r--r--   0 runner    (1001) docker     (121)    70055 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/data/census_data.json
--rw-r--r--   0 runner    (1001) docker     (121)     7707 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/data/pc_inventory.json
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 03:58:58.295454 leafmap-0.9.5/leafmap/data/template/
--rw-r--r--   0 runner    (1001) docker     (121)     1353 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/data/template/legend.html
--rw-r--r--   0 runner    (1001) docker     (121)     2197 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/data/template/legend.txt
--rw-r--r--   0 runner    (1001) docker     (121)     9586 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/deck.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 03:58:58.295454 leafmap-0.9.5/leafmap/examples/
--rw-r--r--   0 runner    (1001) docker     (121)     1306 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/examples/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)      703 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/examples/datasets.txt
--rw-r--r--   0 runner    (1001) docker     (121)   111656 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/foliumap.py
--rw-r--r--   0 runner    (1001) docker     (121)    25561 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/heremap.py
--rw-r--r--   0 runner    (1001) docker     (121)    17640 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/kepler.py
--rw-r--r--   0 runner    (1001) docker     (121)   148918 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/leafmap.py
--rw-r--r--   0 runner    (1001) docker     (121)    23935 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/legends.py
--rw-r--r--   0 runner    (1001) docker     (121)    26029 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/osm.py
--rw-r--r--   0 runner    (1001) docker     (121)     3527 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/pc.py
--rw-r--r--   0 runner    (1001) docker     (121)    30325 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/plotlymap.py
--rw-r--r--   0 runner    (1001) docker     (121)   162814 2022-06-27 03:58:49.000000 leafmap-0.9.5/leafmap/toolbar.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 03:58:58.295454 leafmap-0.9.5/leafmap.egg-info/
--rw-r--r--   0 runner    (1001) docker     (121)     9243 2022-06-27 03:58:58.000000 leafmap-0.9.5/leafmap.egg-info/PKG-INFO
--rw-r--r--   0 runner    (1001) docker     (121)      886 2022-06-27 03:58:58.000000 leafmap-0.9.5/leafmap.egg-info/SOURCES.txt
--rw-r--r--   0 runner    (1001) docker     (121)      212 2022-06-27 03:58:58.000000 leafmap-0.9.5/leafmap.egg-info/dependency_links.txt
--rw-r--r--   0 runner    (1001) docker     (121)        1 2022-06-27 03:58:58.000000 leafmap-0.9.5/leafmap.egg-info/not-zip-safe
--rw-r--r--   0 runner    (1001) docker     (121)      834 2022-06-27 03:58:58.000000 leafmap-0.9.5/leafmap.egg-info/requires.txt
--rw-r--r--   0 runner    (1001) docker     (121)        8 2022-06-27 03:58:58.000000 leafmap-0.9.5/leafmap.egg-info/top_level.txt
--rw-r--r--   0 runner    (1001) docker     (121)      211 2022-06-27 03:58:49.000000 leafmap-0.9.5/requirements.txt
--rw-r--r--   0 runner    (1001) docker     (121)      344 2022-06-27 03:58:49.000000 leafmap-0.9.5/requirements_dev.txt
--rw-r--r--   0 runner    (1001) docker     (121)      304 2022-06-27 03:58:49.000000 leafmap-0.9.5/requirements_docs.txt
--rw-r--r--   0 runner    (1001) docker     (121)      390 2022-06-27 03:58:58.295454 leafmap-0.9.5/setup.cfg
--rw-r--r--   0 runner    (1001) docker     (121)     2368 2022-06-27 03:58:49.000000 leafmap-0.9.5/setup.py
-drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-06-27 03:58:58.295454 leafmap-0.9.5/tests/
--rw-r--r--   0 runner    (1001) docker     (121)       37 2022-06-27 03:58:49.000000 leafmap-0.9.5/tests/__init__.py
--rw-r--r--   0 runner    (1001) docker     (121)     4343 2022-06-27 03:58:49.000000 leafmap-0.9.5/tests/test_colormaps.py
--rw-r--r--   0 runner    (1001) docker     (121)     2171 2022-06-27 03:58:49.000000 leafmap-0.9.5/tests/test_common.py
--rw-r--r--   0 runner    (1001) docker     (121)    18205 2022-06-27 03:58:49.000000 leafmap-0.9.5/tests/test_foliumap.py
--rw-r--r--   0 runner    (1001) docker     (121)    16934 2022-06-27 03:58:49.000000 leafmap-0.9.5/tests/test_leafmap.py
--rw-r--r--   0 runner    (1001) docker     (121)     1299 2022-06-27 03:58:49.000000 leafmap-0.9.5/tests/test_osm.py
--rw-r--r--   0 runner    (1001) docker     (121)     2375 2022-06-27 03:58:49.000000 leafmap-0.9.5/tests/test_toolbar.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-01 19:50:36.958071 leafmap-0.9.6/
+-rw-r--r--   0 runner    (1001) docker     (121)     1070 2022-07-01 19:50:26.000000 leafmap-0.9.6/LICENSE
+-rw-r--r--   0 runner    (1001) docker     (121)      277 2022-07-01 19:50:26.000000 leafmap-0.9.6/MANIFEST.in
+-rw-r--r--   0 runner    (1001) docker     (121)     9243 2022-07-01 19:50:36.958071 leafmap-0.9.6/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)     8395 2022-07-01 19:50:26.000000 leafmap-0.9.6/README.md
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-01 19:50:36.958071 leafmap-0.9.6/leafmap/
+-rw-r--r--   0 runner    (1001) docker     (121)      742 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18901 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/basemaps.py
+-rw-r--r--   0 runner    (1001) docker     (121)    10175 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/colormaps.py
+-rw-r--r--   0 runner    (1001) docker     (121)   196669 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/common.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-01 19:50:36.958071 leafmap-0.9.6/leafmap/data/
+-rw-r--r--   0 runner    (1001) docker     (121)    70055 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/data/census_data.json
+-rw-r--r--   0 runner    (1001) docker     (121)     7707 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/data/pc_inventory.json
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-01 19:50:36.958071 leafmap-0.9.6/leafmap/data/template/
+-rw-r--r--   0 runner    (1001) docker     (121)     1353 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/data/template/legend.html
+-rw-r--r--   0 runner    (1001) docker     (121)     2197 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/data/template/legend.txt
+-rw-r--r--   0 runner    (1001) docker     (121)     9586 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/deck.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-01 19:50:36.958071 leafmap-0.9.6/leafmap/examples/
+-rw-r--r--   0 runner    (1001) docker     (121)     1306 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/examples/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)      703 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/examples/datasets.txt
+-rw-r--r--   0 runner    (1001) docker     (121)   111656 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/foliumap.py
+-rw-r--r--   0 runner    (1001) docker     (121)    25561 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/heremap.py
+-rw-r--r--   0 runner    (1001) docker     (121)    17640 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/kepler.py
+-rw-r--r--   0 runner    (1001) docker     (121)   148918 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/leafmap.py
+-rw-r--r--   0 runner    (1001) docker     (121)    23935 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/legends.py
+-rw-r--r--   0 runner    (1001) docker     (121)    26029 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/osm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     3527 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/pc.py
+-rw-r--r--   0 runner    (1001) docker     (121)    30325 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/plotlymap.py
+-rw-r--r--   0 runner    (1001) docker     (121)      652 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/report.py
+-rw-r--r--   0 runner    (1001) docker     (121)   162814 2022-07-01 19:50:26.000000 leafmap-0.9.6/leafmap/toolbar.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-01 19:50:36.958071 leafmap-0.9.6/leafmap.egg-info/
+-rw-r--r--   0 runner    (1001) docker     (121)     9243 2022-07-01 19:50:36.000000 leafmap-0.9.6/leafmap.egg-info/PKG-INFO
+-rw-r--r--   0 runner    (1001) docker     (121)      904 2022-07-01 19:50:36.000000 leafmap-0.9.6/leafmap.egg-info/SOURCES.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      219 2022-07-01 19:50:36.000000 leafmap-0.9.6/leafmap.egg-info/dependency_links.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        1 2022-07-01 19:50:36.000000 leafmap-0.9.6/leafmap.egg-info/not-zip-safe
+-rw-r--r--   0 runner    (1001) docker     (121)      848 2022-07-01 19:50:36.000000 leafmap-0.9.6/leafmap.egg-info/requires.txt
+-rw-r--r--   0 runner    (1001) docker     (121)        8 2022-07-01 19:50:36.000000 leafmap-0.9.6/leafmap.egg-info/top_level.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      218 2022-07-01 19:50:26.000000 leafmap-0.9.6/requirements.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      351 2022-07-01 19:50:26.000000 leafmap-0.9.6/requirements_dev.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      304 2022-07-01 19:50:26.000000 leafmap-0.9.6/requirements_docs.txt
+-rw-r--r--   0 runner    (1001) docker     (121)      390 2022-07-01 19:50:36.958071 leafmap-0.9.6/setup.cfg
+-rw-r--r--   0 runner    (1001) docker     (121)     2368 2022-07-01 19:50:26.000000 leafmap-0.9.6/setup.py
+drwxr-xr-x   0 runner    (1001) docker     (121)        0 2022-07-01 19:50:36.958071 leafmap-0.9.6/tests/
+-rw-r--r--   0 runner    (1001) docker     (121)       37 2022-07-01 19:50:26.000000 leafmap-0.9.6/tests/__init__.py
+-rw-r--r--   0 runner    (1001) docker     (121)     4343 2022-07-01 19:50:26.000000 leafmap-0.9.6/tests/test_colormaps.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2171 2022-07-01 19:50:26.000000 leafmap-0.9.6/tests/test_common.py
+-rw-r--r--   0 runner    (1001) docker     (121)    18205 2022-07-01 19:50:26.000000 leafmap-0.9.6/tests/test_foliumap.py
+-rw-r--r--   0 runner    (1001) docker     (121)    16934 2022-07-01 19:50:26.000000 leafmap-0.9.6/tests/test_leafmap.py
+-rw-r--r--   0 runner    (1001) docker     (121)     1299 2022-07-01 19:50:26.000000 leafmap-0.9.6/tests/test_osm.py
+-rw-r--r--   0 runner    (1001) docker     (121)     2375 2022-07-01 19:50:26.000000 leafmap-0.9.6/tests/test_toolbar.py
```

### Comparing `leafmap-0.9.5/LICENSE` & `leafmap-0.9.6/LICENSE`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/PKG-INFO` & `leafmap-0.9.6/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: leafmap
-Version: 0.9.5
+Version: 0.9.6
 Summary: A Python package for geospatial analysis and interactive mapping in a Jupyter environment.
 Home-page: https://github.com/giswqs/leafmap
 Author: Qiusheng Wu
 Author-email: giswqs@gmail.com
 License: MIT license
 Keywords: leafmap
 Platform: UNKNOWN
```

### Comparing `leafmap-0.9.5/README.md` & `leafmap-0.9.6/README.md`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/__init__.py` & `leafmap-0.9.6/leafmap/__init__.py`

 * *Files 8% similar despite different names*

```diff
@@ -1,12 +1,12 @@
 """Top-level package for leafmap."""
 
 __author__ = """Qiusheng Wu"""
 __email__ = "giswqs@gmail.com"
-__version__ = "0.9.5"
+__version__ = "0.9.6"
 
 import os
 
 
 def _in_colab_shell():
     """Tests if the code is being executed within Google Colab."""
     import sys
@@ -30,7 +30,9 @@
 else:
     from .leafmap import *
 
     if _in_colab_shell():
         from google.colab import output
 
         output.enable_custom_widget_manager()
+
+from .report import Report
```

### Comparing `leafmap-0.9.5/leafmap/basemaps.py` & `leafmap-0.9.6/leafmap/basemaps.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/colormaps.py` & `leafmap-0.9.6/leafmap/colormaps.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/common.py` & `leafmap-0.9.6/leafmap/common.py`

 * *Files 1% similar despite different names*

```diff
@@ -5754,7 +5754,118 @@
             raise Exception(f"{cmap} is not a valid colormap.")
     elif isinstance(cmap, Box):
         return list(cmap["default"])
     elif isinstance(cmap, list) or isinstance(cmap, tuple):
         return cmap
     else:
         raise Exception(f"{cmap} is not a valid colormap.")
+
+
+def plot_raster(
+    image,
+    band=None,
+    cmap="terrain",
+    proj="EPSG:3857",
+    figsize=None,
+    open_kwargs={},
+    **kwargs,
+):
+    """Plot a raster image.
+
+    Args:
+        image (str | xarray.DataArray ): The input raster image, can be a file path, HTTP URL, or xarray.DataArray.
+        band (int, optional): The band index, starting from zero. Defaults to None.
+        cmap (str, optional): The matplotlib colormap to use. Defaults to "terrain".
+        proj (str, optional): The EPSG projection code. Defaults to "EPSG:3857".
+        figsize (tuple, optional): The figure size as a tuple, such as (10, 8). Defaults to None.
+        open_kwargs (dict, optional): The keyword arguments to pass to rioxarray.open_rasterio. Defaults to {}.
+        **kwargs: Additional keyword arguments to pass to xarray.DataArray.plot().
+
+    """
+    if os.environ.get("USE_MKDOCS") is not None:
+        return
+
+    try:
+        import pvxarray
+        import rioxarray
+        import xarray
+    except ImportError:
+        raise ImportError(
+            "pyxarray and rioxarray are required for plotting. Please install them using 'pip install rioxarray pyvista-xarray'."
+        )
+
+    if isinstance(image, str):
+        da = rioxarray.open_rasterio(image, **open_kwargs)
+    elif isinstance(image, xarray.DataArray):
+        da = image
+    else:
+        raise ValueError("image must be a string or xarray.Dataset.")
+
+    if band is not None:
+        da = da[dict(band=band)]
+
+    da = da.rio.reproject(proj)
+    kwargs["cmap"] = cmap
+    kwargs["figsize"] = figsize
+    da.plot(**kwargs)
+
+
+def plot_raster_3d(
+    image,
+    band=None,
+    cmap="terrain",
+    factor=1.0,
+    proj="EPSG:3857",
+    background=None,
+    open_kwargs={},
+    mesh_kwargs={},
+    **kwargs,
+):
+    """Plot a raster image in 3D.
+
+    Args:
+        image (str | xarray.DataArray ): The input raster image, can be a file path, HTTP URL, or xarray.DataArray.
+        band (int, optional): The band index, starting from zero. Defaults to None.
+        cmap (str, optional): The matplotlib colormap to use. Defaults to "terrain".
+        factor (float, optional): The scaling factor for the raster. Defaults to 1.0.
+        proj (str, optional): The EPSG projection code. Defaults to "EPSG:3857".
+        background (str, optional): The background color. Defaults to None.
+        open_kwargs (dict, optional): The keyword arguments to pass to rioxarray.open_rasterio. Defaults to {}.
+        mesh_kwargs (dict, optional): The keyword arguments to pass to pyvista.mesh.warp_by_scalar(). Defaults to {}.
+        **kwargs: Additional keyword arguments to pass to xarray.DataArray.plot().
+    """
+
+    if os.environ.get("USE_MKDOCS") is not None:
+        return
+
+    try:
+        import pvxarray
+        import pyvista
+        import rioxarray
+        import xarray
+    except ImportError:
+        raise ImportError(
+            "pyxarray and rioxarray are required for plotting. Please install them using 'pip install rioxarray pyvista-xarray'."
+        )
+
+    if isinstance(background, str):
+        pyvista.global_theme.background = background
+
+    if isinstance(image, str):
+        da = rioxarray.open_rasterio(image, **open_kwargs)
+    elif isinstance(image, xarray.DataArray):
+        da = image
+    else:
+        raise ValueError("image must be a string or xarray.Dataset.")
+
+    if band is not None:
+        da = da[dict(band=band)]
+
+    da = da.rio.reproject(proj)
+    mesh_kwargs["factor"] = factor
+    kwargs["cmap"] = cmap
+
+    # Grab the mesh object for use with PyVista
+    mesh = da.pyvista.mesh
+
+    # Warp top and plot in 3D
+    mesh.warp_by_scalar(**mesh_kwargs).plot(**kwargs)
```

### Comparing `leafmap-0.9.5/leafmap/data/census_data.json` & `leafmap-0.9.6/leafmap/data/census_data.json`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/data/pc_inventory.json` & `leafmap-0.9.6/leafmap/data/pc_inventory.json`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/data/template/legend.html` & `leafmap-0.9.6/leafmap/data/template/legend.html`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/data/template/legend.txt` & `leafmap-0.9.6/leafmap/data/template/legend.txt`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/deck.py` & `leafmap-0.9.6/leafmap/deck.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/examples/__init__.py` & `leafmap-0.9.6/leafmap/examples/__init__.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/examples/datasets.txt` & `leafmap-0.9.6/leafmap/examples/datasets.txt`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/foliumap.py` & `leafmap-0.9.6/leafmap/foliumap.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/heremap.py` & `leafmap-0.9.6/leafmap/heremap.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/kepler.py` & `leafmap-0.9.6/leafmap/kepler.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/leafmap.py` & `leafmap-0.9.6/leafmap/leafmap.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/legends.py` & `leafmap-0.9.6/leafmap/legends.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/osm.py` & `leafmap-0.9.6/leafmap/osm.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/pc.py` & `leafmap-0.9.6/leafmap/pc.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/plotlymap.py` & `leafmap-0.9.6/leafmap/plotlymap.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap/toolbar.py` & `leafmap-0.9.6/leafmap/toolbar.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/leafmap.egg-info/PKG-INFO` & `leafmap-0.9.6/leafmap.egg-info/PKG-INFO`

 * *Files 0% similar despite different names*

```diff
@@ -1,10 +1,10 @@
 Metadata-Version: 2.1
 Name: leafmap
-Version: 0.9.5
+Version: 0.9.6
 Summary: A Python package for geospatial analysis and interactive mapping in a Jupyter environment.
 Home-page: https://github.com/giswqs/leafmap
 Author: Qiusheng Wu
 Author-email: giswqs@gmail.com
 License: MIT license
 Keywords: leafmap
 Platform: UNKNOWN
```

### Comparing `leafmap-0.9.5/leafmap.egg-info/SOURCES.txt` & `leafmap-0.9.6/leafmap.egg-info/SOURCES.txt`

 * *Files 1% similar despite different names*

```diff
@@ -15,14 +15,15 @@
 leafmap/heremap.py
 leafmap/kepler.py
 leafmap/leafmap.py
 leafmap/legends.py
 leafmap/osm.py
 leafmap/pc.py
 leafmap/plotlymap.py
+leafmap/report.py
 leafmap/toolbar.py
 leafmap.egg-info/PKG-INFO
 leafmap.egg-info/SOURCES.txt
 leafmap.egg-info/dependency_links.txt
 leafmap.egg-info/not-zip-safe
 leafmap.egg-info/requires.txt
 leafmap.egg-info/top_level.txt
```

### Comparing `leafmap-0.9.5/leafmap.egg-info/requires.txt` & `leafmap-0.9.6/leafmap.egg-info/requires.txt`

 * *Files 2% similar despite different names*

```diff
@@ -11,14 +11,15 @@
 matplotlib
 numpy
 pandas
 pycrs
 pyshp>=2.1.3
 pystac-client
 python-box
+scooby
 whiteboxgui>=0.6.0
 xyzservices
 
 [all]
 black
 black[jupyter]
 codespell
@@ -39,15 +40,15 @@
 owslib
 palettable
 panel
 plotly
 psycopg2
 pydeck
 pyntcloud[las]
-pyvista
+pyvista-xarray
 rio-cogeo
 rioxarray
 sqlalchemy
 streamlit-folium
 xarray_leaflet
 
 [apps]
```

### Comparing `leafmap-0.9.5/setup.py` & `leafmap-0.9.6/setup.py`

 * *Files 4% similar despite different names*

```diff
@@ -68,10 +68,10 @@
     keywords="leafmap",
     name="leafmap",
     packages=find_packages(include=["leafmap", "leafmap.*"]),
     setup_requires=setup_requirements,
     test_suite="tests",
     tests_require=test_requirements,
     url="https://github.com/giswqs/leafmap",
-    version="0.9.5",
+    version="0.9.6",
     zip_safe=False,
 )
```

### Comparing `leafmap-0.9.5/tests/test_colormaps.py` & `leafmap-0.9.6/tests/test_colormaps.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/tests/test_common.py` & `leafmap-0.9.6/tests/test_common.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/tests/test_foliumap.py` & `leafmap-0.9.6/tests/test_foliumap.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/tests/test_leafmap.py` & `leafmap-0.9.6/tests/test_leafmap.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/tests/test_osm.py` & `leafmap-0.9.6/tests/test_osm.py`

 * *Files identical despite different names*

### Comparing `leafmap-0.9.5/tests/test_toolbar.py` & `leafmap-0.9.6/tests/test_toolbar.py`

 * *Files identical despite different names*

